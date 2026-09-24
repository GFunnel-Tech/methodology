#!/usr/bin/env python3
"""Validate Reality Audit records under audit/.

Specification: audit/SCHEMA.md §1, §3, §4. Standard library only.

Usage:
  python3 tools/validate_audit.py            # validate every audit file
  python3 tools/validate_audit.py FILE ...   # validate specific files
  python3 tools/validate_audit.py --selftest # run the built-in checks on the validator itself
  python3 tools/validate_audit.py --today YYYY-MM-DD   # date used for overdue review_after warnings

Exit status: 0 if no errors (warnings allowed), 1 otherwise.
"""

import datetime
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frontmatter as fm  # noqa: E402

# ---- Vocabularies (audit/SCHEMA.md §1) -------------------------------------------------

OBSERVATION_GRADES = {"measured-reproduced", "measured-single", "derived", "held-open"}
CLAIM_OUTCOMES = {"forced-fill", "live-hypothesis", "stipulation", "proven-open", "forced-no"}
DIFF_STATES = {"accounted", "methodology-gap", "unobserved-claim", "conflict", "unmapped"}
DIAGNOSES = {"not-reached", "reached-conflicting", "unverified", "beyond-depth"}
NEEDS_DIAGNOSIS = {"methodology-gap", "conflict", "unmapped"}
INTAKE_RESULTS = {"integrated", "adjusted", "open"}

REQUIRED_KEYS = [
    "id", "canon_ref", "canon_label", "diff_state", "exclusion_diagnosis",
    "claim_outcome", "intake_result", "review_after", "container", "ledger_row",
]
OPTIONAL_KEYS = {"proposed_label"}

REQUIRED_SECTIONS = [
    "Canon says", "Reality shows", "Scientific Inquiry run", "Forcing Test", "Anti-Operation",
]

# ---- Identifiers (audit/SCHEMA.md §3) --------------------------------------------------

ID_RULES = {
    "governance": re.compile(r"^GOV-\d{3}$"),
    "labels": re.compile(r"^LABEL-\d{3}$"),
    "stages": re.compile(r"^STAGE-(\d{3})$"),
    "constants": re.compile(r"^CONST-[a-z0-9]+(?:-[a-z0-9]+)*$"),
    "domains": re.compile(r"^DOMAIN-(\d{2})$"),
    "unmapped": re.compile(r"^UNMAPPED-\d{4}$"),
    "claims": re.compile(r"^CLAIM-\d{3}$"),
}
CONTAINER_RE = re.compile(r"^KC-\d{4}$")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIT_DIR = os.path.join(ROOT, "audit")


def check_record(text, subdir, filename, today):
    """Return (errors, warnings) for one audit record."""
    errors, warnings = [], []
    fields, body, perr = fm.parse(text)
    errors += perr
    if fields is None:
        return errors, warnings

    for key in REQUIRED_KEYS:
        if key not in fields:
            errors.append(f"missing required key '{key}'")
    for key in fields:
        if key not in REQUIRED_KEYS and key not in OPTIONAL_KEYS:
            errors.append(f"unknown key '{key}'")

    rid = fields.get("id") or ""
    rule = ID_RULES.get(subdir)
    if rule is None:
        errors.append(f"audit records do not belong in '{subdir}/'")
    else:
        m = rule.match(rid)
        if not m:
            errors.append(f"id '{rid}' does not match the {subdir}/ pattern {rule.pattern}")
        elif subdir == "stages" and not 1 <= int(m.group(1)) <= 100:
            errors.append(f"stage number out of range 001-100: {rid}")
        elif subdir == "domains" and not 1 <= int(m.group(1)) <= 10:
            errors.append(f"domain number out of range 01-10: {rid}")
    stem = filename[:-3] if filename.endswith(".md") else filename
    if rid and not (stem == rid or stem.startswith(rid + "-")):
        errors.append(f"file name '{filename}' does not start with id '{rid}'")

    for key in ("canon_ref", "canon_label"):
        if key in fields and not fields[key]:
            errors.append(f"'{key}' is empty (use 'none' only for unmapped items)")
        if fields.get(key) == "none" and fields.get("diff_state") != "unmapped":
            errors.append(f"'{key}: none' is allowed only when diff_state is unmapped")

    diff = fields.get("diff_state")
    allowed_diff = DIFF_STATES | ({"n/a"} if subdir == "governance" else set())
    if diff not in allowed_diff:
        errors.append(f"diff_state '{diff}' not in {sorted(allowed_diff)}")

    diag = fields.get("exclusion_diagnosis")
    if diff in NEEDS_DIAGNOSIS:
        if diag not in DIAGNOSES:
            errors.append(
                f"diff_state '{diff}' requires an exclusion_diagnosis in {sorted(DIAGNOSES)} "
                f"(got '{diag}')")
    elif diag != "n/a":
        errors.append(f"exclusion_diagnosis must be 'n/a' when diff_state is '{diff}' (got '{diag}')")

    if fields.get("claim_outcome") not in CLAIM_OUTCOMES:
        errors.append(f"claim_outcome '{fields.get('claim_outcome')}' not in {sorted(CLAIM_OUTCOMES)}")

    intake = fields.get("intake_result")
    if intake not in INTAKE_RESULTS:
        errors.append(f"intake_result '{intake}' not in {sorted(INTAKE_RESULTS)}")

    review = fields.get("review_after")
    if review is not None and not fm.DATE_RE.match(review):
        errors.append(f"review_after must be YYYY-MM-DD or null (got '{review}')")
    if intake == "open":
        if review is None:
            errors.append("intake_result 'open' requires a review_after date (open must not decay into ignored)")
        elif fm.DATE_RE.match(review) and review < today:
            warnings.append(f"review_after {review} is overdue (today {today}) — re-review this open item")

    container = fields.get("container")
    if container is not None and not CONTAINER_RE.match(container):
        errors.append(f"container must be KC-#### or null (got '{container}')")

    secs = fm.sections(body)
    for name in REQUIRED_SECTIONS:
        if fm.find_section(secs, name) is None:
            errors.append(f"missing section '## {name}'")

    reality = fm.find_section(secs, "Reality shows") or ""
    grades = set()
    for line in reality.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 6 and cells[0].lower() != "quantity" and not re.fullmatch(r"[-: ]+", cells[0] or "-"):
            grade = cells[3]
            if grade not in OBSERVATION_GRADES:
                errors.append(f"Reality shows: grade '{grade}' not in {sorted(OBSERVATION_GRADES)}")
            else:
                grades.add(grade)
            if not cells[4]:
                errors.append(f"Reality shows: row '{cells[0]}' has no source")
            if not fm.DATE_RE.match(cells[5]):
                errors.append(f"Reality shows: row '{cells[0]}' retrieved date must be YYYY-MM-DD")
    if intake == "adjusted" and "measured-reproduced" not in grades:
        errors.append("intake_result 'adjusted' requires at least one measured-reproduced observation "
                      "(weak observations cannot force change)")

    for name, count in (("Scientific Inquiry run", 10), ("Forcing Test", 5)):
        text = fm.find_section(secs, name)
        if text is not None:
            errors += check_steps(name, text, count)

    return errors, warnings


def check_steps(name, text, count):
    """Every step must be filled, unless an earlier step recorded BLOCKED:."""
    errors, blocked = [], False
    if name == "Forcing Test":
        items = re.findall(r"^\s*-\s*(.+?):(.*)$", text, flags=re.M)
    else:
        items = re.findall(r"^\s*(\d+)\.\s*(.+?):(.*)$", text, flags=re.M)
        items = [(f"{n}. {label}", rest) for n, label, rest in items]
    if len(items) < count:
        errors.append(f"{name}: expected {count} steps, found {len(items)}")
    for label, rest in items:
        content = rest.strip().strip("*").strip()
        if "BLOCKED:" in rest:
            blocked = True
            continue
        if not content and not blocked:
            errors.append(f"{name}: step '{label.strip('* ')}' is empty "
                          f"(fill it, or record 'BLOCKED: <blocker>' at the step that could not be completed)")
    return errors


def iter_files():
    for subdir in sorted(ID_RULES):
        path = os.path.join(AUDIT_DIR, subdir)
        if not os.path.isdir(path):
            continue
        for name in sorted(os.listdir(path)):
            if name.endswith(".md") and name.upper() != "README.MD":
                yield subdir, name, os.path.join(path, name)


def run(paths, today):
    targets = []
    if paths:
        for p in paths:
            ap = os.path.abspath(p)
            targets.append((os.path.basename(os.path.dirname(ap)), os.path.basename(ap), ap))
    else:
        targets = list(iter_files())

    seen, n_err, n_warn = {}, 0, 0
    for subdir, name, path in targets:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        errors, warnings = check_record(text, subdir, name, today)
        fields, _, _ = fm.parse(text)
        rid = (fields or {}).get("id")
        if rid:
            if rid in seen:
                errors.append(f"duplicate id '{rid}' (also in {seen[rid]})")
            seen[rid] = os.path.relpath(path, ROOT)
        rel = os.path.relpath(path, ROOT)
        for e in errors:
            print(f"ERROR   {rel}: {e}")
        for w in warnings:
            print(f"WARNING {rel}: {w}")
        n_err += len(errors)
        n_warn += len(warnings)
    print(f"validate_audit: {len(targets)} file(s), {n_err} error(s), {n_warn} warning(s)")
    return 1 if n_err else 0


# ---- Self-test -------------------------------------------------------------------------

GOOD = """---
id: STAGE-005
canon_ref: v5.1 Appendix A, Stage 5
canon_label: "Big Bang Nucleosynthesis"   # quoted, with a comment
proposed_label: "Primordial Light-Element Formation"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
Quote.

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| helium-4 mass fraction | 0.245 | 0.003 | measured-reproduced | https://example.org/x | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): q
2. What an answer must look like: a
3. Falsifiability condition: f
4. Variables: measurable / bounded / held open: v
5. Test designed: BLOCKED: no primary source reachable
6. Data (unfiltered):
7. Variable Principle applied:
8. Model update (Capsule: what the failed parts contribute):
9. Documented:
10. Next baseline:

## Forcing Test
- Test A (Ground): a
- Test B (Uniqueness): b
- Test C (Direction): c
- Test D (Falsifiability): d
- **Outcome:** forced-fill

## Anti-Operation (the gap this opens)
Gap.
"""


def selftest():
    today = "2026-09-24"
    cases = [
        ("valid record with a BLOCKED step", GOOD, "stages", "STAGE-005.md", 0),
        ("bad vocabulary", GOOD.replace("diff_state: accounted", "diff_state: fine"), "stages", "STAGE-005.md", 1),
        ("gap without diagnosis", GOOD.replace("diff_state: accounted", "diff_state: conflict"),
         "stages", "STAGE-005.md", 1),
        ("open without review_after", GOOD.replace("intake_result: integrated", "intake_result: open"),
         "stages", "STAGE-005.md", 1),
        ("adjusted on a single measurement",
         GOOD.replace("intake_result: integrated", "intake_result: adjusted")
             .replace("| measured-reproduced |", "| measured-single |"), "stages", "STAGE-005.md", 1),
        ("empty step without BLOCKED", GOOD.replace("BLOCKED: no primary source reachable", ""),
         "stages", "STAGE-005.md", 5),
        ("id / file / directory mismatch", GOOD, "constants", "CONST-pi.md", 2),
        ("missing section", GOOD.replace("## Anti-Operation (the gap this opens)\nGap.\n", ""),
         "stages", "STAGE-005.md", 1),
        ("stage out of range", GOOD.replace("STAGE-005", "STAGE-101"), "stages", "STAGE-101.md", 1),
    ]
    failed = 0
    for label, text, subdir, name, expected in cases:
        errors, _ = check_record(text, subdir, name, today)
        ok = len(errors) == expected
        failed += not ok
        print(f"{'ok  ' if ok else 'FAIL'} {label}: expected {expected} error(s), got {len(errors)}")
        if not ok:
            for e in errors:
                print(f"       {e}")
    _, warnings = check_record(GOOD.replace("intake_result: integrated", "intake_result: open")
                               .replace("review_after: null", "review_after: 2026-01-01"),
                               "stages", "STAGE-005.md", today)
    ok = len(warnings) == 1
    failed += not ok
    print(f"{'ok  ' if ok else 'FAIL'} overdue review_after warns: got {len(warnings)} warning(s)")
    print(f"selftest: {'passed' if not failed else f'{failed} case(s) failed'}")
    return 1 if failed else 0


def main(argv):
    today = datetime.date.today().isoformat()
    if "--today" in argv:
        i = argv.index("--today")
        today = argv[i + 1]
        del argv[i:i + 2]
    if "--selftest" in argv:
        return selftest()
    return run(argv, today)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
