#!/usr/bin/env python3
"""Validate knowledge containers (KC-####) under containers/.

Specification: audit/SCHEMA.md §5 and containers/README.md. Standard library only.

Usage:
  python3 tools/validate_containers.py            # validate every container + INDEX.md
  python3 tools/validate_containers.py --selftest # run the built-in checks on the validator itself

Exit status: 0 if no errors, 1 otherwise.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frontmatter as fm  # noqa: E402

STATUSES = {"forced-fill", "live-hypothesis", "stipulation", "proven-open"}
FORMS = {"equation", "algorithm", "both", "held-open"}
REQUIRED_KEYS = [
    "id", "name", "status", "form", "canon_refs", "audit_refs",
    "links_up", "links_down", "created", "last_reformed",
]
LIST_KEYS = {"canon_refs", "audit_refs", "links_up", "links_down"}
ID_RE = re.compile(r"^KC-\d{4}$")
AUDIT_ID_RE = re.compile(r"^(GOV-\d{3}|LABEL-\d{3}|STAGE-\d{3}|CONST-[a-z0-9-]+|DOMAIN-\d{2}|UNMAPPED-\d{4})$")
SKIP = {"README.md", "TEMPLATE.md", "INDEX.md"}

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTAINER_DIR = os.path.join(ROOT, "containers")
AUDIT_DIR = os.path.join(ROOT, "audit")


def check_container(text, filename):
    """Return (fields, errors) for one container. Cross-file checks happen in run()."""
    errors = []
    fields, body, perr = fm.parse(text)
    errors += perr
    if fields is None:
        return {}, errors

    for key in REQUIRED_KEYS:
        if key not in fields:
            errors.append(f"missing required key '{key}'")
    for key in fields:
        if key not in REQUIRED_KEYS:
            errors.append(f"unknown key '{key}'")
    for key in LIST_KEYS:
        if key in fields and not isinstance(fields[key], list):
            errors.append(f"'{key}' must be a list, e.g. [] or [KC-0001]")

    cid = fields.get("id") or ""
    if not ID_RE.match(cid):
        errors.append(f"id '{cid}' does not match KC-####")
    elif not (filename == f"{cid}.md" or filename.startswith(cid + "-")):
        errors.append(f"file name '{filename}' does not start with id '{cid}'")
    if not fields.get("name"):
        errors.append("'name' is empty")
    if fields.get("status") not in STATUSES:
        errors.append(f"status '{fields.get('status')}' not in {sorted(STATUSES)}")
    form = fields.get("form")
    if form not in FORMS:
        errors.append(f"form '{form}' not in {sorted(FORMS)}")
    for key in ("created", "last_reformed"):
        val = fields.get(key)
        if not (isinstance(val, str) and fm.DATE_RE.match(val)):
            errors.append(f"'{key}' must be YYYY-MM-DD (got '{val}')")
    if (isinstance(fields.get("created"), str) and isinstance(fields.get("last_reformed"), str)
            and fields["last_reformed"] < fields["created"]):
        errors.append("last_reformed is earlier than created")
    for key in ("links_up", "links_down"):
        for ref in fields.get(key) or []:
            if not ID_RE.match(ref):
                errors.append(f"{key}: '{ref}' is not a KC-#### id")
            elif ref == cid:
                errors.append(f"{key}: container links to itself")
    for ref in fields.get("audit_refs") or []:
        if not AUDIT_ID_RE.match(ref):
            errors.append(f"audit_refs: '{ref}' is not an audit id")

    secs = fm.sections(body)
    for name in ("Observations", "Form", "Trace", "Open edge", "Re-formation log"):
        if fm.find_section(secs, name) is None:
            errors.append(f"missing section '## {name}'")

    trace = fm.find_section(secs, "Trace")
    if not fm.meaningful(trace) or "(how this was reached" in (trace or ""):
        errors.append("'## Trace' is empty — every container shows how it was reached")

    edge = fm.find_section(secs, "Open edge") or ""
    edge = re.sub(r"<!--.*?-->", "", edge, flags=re.S)
    items = [l for l in edge.splitlines() if re.match(r"^\s*(?:[-*]|\d+\.)\s+\S", l)]
    placeholder = [l for l in items if re.search(r"\(the gap this solution opens", l)]
    if not items or len(items) == len(placeholder):
        errors.append("no open edge — a container must carry at least one (Anti-Operation)")

    log = fm.find_section(secs, "Re-formation log") or ""
    if not re.search(r"^\s*[-*]\s*\d{4}-\d{2}-\d{2}\b", log, flags=re.M):
        errors.append("'## Re-formation log' has no dated entry (- YYYY-MM-DD — ...)")

    form_text = fm.find_section(secs, "Form") or ""
    subs = fm.sections(form_text, level=3)
    if form in ("equation", "both"):
        if not fm.meaningful(fm.find_section(subs, "Equation")):
            errors.append(f"form '{form}' requires a non-empty '### Equation'")
    if form in ("algorithm", "both"):
        algo = fm.find_section(subs, "Algorithm") or ""
        if not re.search(r"^\s*1\.\s+\S", algo, flags=re.M) or "(numbered steps" in algo:
            errors.append(f"form '{form}' requires numbered steps under '### Algorithm'")

    if fields.get("status") == "live-hypothesis" and "falsifier" not in body.lower():
        errors.append("live-hypothesis container must state its falsifier")

    return fields, errors


def audit_ids():
    ids = set()
    for dirpath, _, files in os.walk(AUDIT_DIR):
        for name in files:
            if name.endswith(".md"):
                with open(os.path.join(dirpath, name), encoding="utf-8") as f:
                    fields, _, _ = fm.parse(f.read())
                if fields and fields.get("id"):
                    ids.add(fields["id"])
    return ids


def run():
    names = sorted(n for n in os.listdir(CONTAINER_DIR) if n.endswith(".md") and n not in SKIP)
    all_fields, n_err = {}, 0
    report = []
    for name in names:
        with open(os.path.join(CONTAINER_DIR, name), encoding="utf-8") as f:
            fields, errors = check_container(f.read(), name)
        cid = fields.get("id")
        if cid in all_fields:
            errors.append(f"duplicate id '{cid}'")
        if cid:
            all_fields[cid] = fields
        report.append((name, errors))

    known_audit = audit_ids()
    index_path = os.path.join(CONTAINER_DIR, "INDEX.md")
    index = open(index_path, encoding="utf-8").read() if os.path.exists(index_path) else ""
    for name, errors in report:
        cid = next((k for k, v in all_fields.items() if name.startswith(k)), None)
        fields = all_fields.get(cid, {})
        for key in ("links_up", "links_down"):
            for ref in fields.get(key) or []:
                if ID_RE.match(ref) and ref not in all_fields:
                    errors.append(f"{key}: '{ref}' does not exist")
        for ref in fields.get("audit_refs") or []:
            if AUDIT_ID_RE.match(ref) and ref not in known_audit:
                errors.append(f"audit_refs: '{ref}' has no audit file")
        if cid and not re.search(rf"\b{re.escape(cid)}\b", index):
            errors.append(f"'{cid}' is not listed in containers/INDEX.md")
        for e in errors:
            print(f"ERROR   containers/{name}: {e}")
        n_err += len(errors)
    if not index:
        print("ERROR   containers/INDEX.md is missing")
        n_err += 1
    print(f"validate_containers: {len(names)} container(s), {n_err} error(s)")
    return 1 if n_err else 0


# ---- Self-test -------------------------------------------------------------------------

GOOD = """---
id: KC-0001
name: "Primordial helium-4 mass fraction"
status: forced-fill
form: both
canon_refs: [v5.4 §5, v5.1 Appendix A Stage 5]
audit_refs: [STAGE-005]
links_up: []
links_down: []
created: 2026-09-24
last_reformed: 2026-09-24
---

## Observations
| Quantity | Value | Uncertainty | Grade | Source |
| --- | --- | --- | --- | --- |
| Y_p | 0.245 | 0.003 | measured-reproduced | https://example.org |

## Form
### Equation
Y_p = 2 (n/p) / (1 + n/p)

### Algorithm
1. Read n/p at freeze-out.
2. Apply the equation.

## Trace
1. Step one.

## Open edge
- The lithium-7 abundance.

## Re-formation log
- 2026-09-24 — Created.
"""


def selftest():
    cases = [
        ("valid container", GOOD, "KC-0001-helium.md", 0),
        ("no open edge", GOOD.replace("- The lithium-7 abundance.", ""), "KC-0001.md", 1),
        ("empty trace", GOOD.replace("1. Step one.", ""), "KC-0001.md", 1),
        ("equation form without equation",
         GOOD.replace("Y_p = 2 (n/p) / (1 + n/p)", ""), "KC-0001.md", 1),
        ("live hypothesis without falsifier",
         GOOD.replace("status: forced-fill", "status: live-hypothesis"), "KC-0001.md", 1),
        ("undated re-formation log", GOOD.replace("- 2026-09-24 — Created.", "- Created."), "KC-0001.md", 1),
        ("bad status and form",
         GOOD.replace("status: forced-fill", "status: solved").replace("form: both", "form: prose"),
         "KC-0001.md", 2),
        ("template placeholders rejected", open(os.path.join(CONTAINER_DIR, "TEMPLATE.md"), encoding="utf-8")
         .read().replace("KC-0000", "KC-0009"), "KC-0009.md", 6),
    ]
    failed = 0
    for label, text, name, expected in cases:
        _, errors = check_container(text, name)
        ok = len(errors) == expected
        failed += not ok
        print(f"{'ok  ' if ok else 'FAIL'} {label}: expected {expected} error(s), got {len(errors)}")
        if not ok:
            for e in errors:
                print(f"       {e}")
    print(f"selftest: {'passed' if not failed else f'{failed} case(s) failed'}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else run())
