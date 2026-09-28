#!/usr/bin/env python3
"""Validate prediction records under audit/prediction/ — enforces the two-phase seal.

Specification: audit/prediction/PROTOCOL.md. Standard library only.

The load-bearing check: a file with `lookup_status: withheld` must contain NO measured
value and NO verdict. That is what makes a sealed prediction a prediction. A Phase B file
must name the Phase A commit that sealed it, and that commit must exist in git history and
must actually have contained the file while still sealed.

Usage:
  python3 tools/validate_prediction.py              # validate every prediction
  python3 tools/validate_prediction.py --selftest
Exit status 0 if no errors.
"""

import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frontmatter as fm  # noqa: E402

KINDS = {"quantitative", "ordinal", "structural"}
RISKS = {"low", "medium", "high"}
STATUSES = {"withheld", "revealed"}
VERDICTS = {"hit", "partial", "miss", "non-discriminating", "void"}
YESNO = {"yes", "no"}
REQUIRED_KEYS = ["id", "target", "organism", "framework_route", "prediction_kind", "tolerance",
                 "contamination_risk", "discriminating", "lookup_status", "phase_a_commit", "verdict"]
PHASE_A_SECTIONS = ["Target", "Framework route", "Derivation trace", "Prediction", "Tolerance",
                    "Framework-free default", "Contamination disclosure"]
PHASE_B_SECTIONS = ["Measured", "Verdict", "What this does and does not show"]
ID_RE = re.compile(r"^PRED-\d{3}$")
SEAL = "<!-- PHASE B BELOW THIS LINE"

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRED_DIR = os.path.join(ROOT, "audit", "prediction")


def git(*args):
    try:
        return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True,
                              timeout=30).stdout
    except Exception:
        return ""


def check(text, filename):
    errors, warnings = [], []
    fields, body, perr = fm.parse(text)
    errors += perr
    if fields is None:
        return errors, warnings

    for k in REQUIRED_KEYS:
        if k not in fields:
            errors.append(f"missing required key '{k}'")
    for k in fields:
        if k not in REQUIRED_KEYS:
            errors.append(f"unknown key '{k}'")

    pid = fields.get("id") or ""
    if not ID_RE.match(pid):
        errors.append(f"id '{pid}' does not match PRED-###")
    elif not (filename == f"{pid}.md" or filename.startswith(pid + "-")):
        errors.append(f"file name '{filename}' does not start with id '{pid}'")
    if fields.get("prediction_kind") not in KINDS:
        errors.append(f"prediction_kind must be one of {sorted(KINDS)}")
    if fields.get("contamination_risk") not in RISKS:
        errors.append(f"contamination_risk must be one of {sorted(RISKS)}")
    if str(fields.get("discriminating")).lower() not in YESNO:
        errors.append("discriminating must be yes or no")
    status = fields.get("lookup_status")
    if status not in STATUSES:
        errors.append(f"lookup_status must be one of {sorted(STATUSES)}")
    if not fields.get("tolerance"):
        errors.append("tolerance is empty — a prediction with no stated tolerance scores 'void'")
    if not fields.get("framework_route"):
        errors.append("framework_route is empty — name the algorithm that was run")

    secs = fm.sections(body)
    for name in PHASE_A_SECTIONS:
        t = fm.find_section(secs, name)
        if t is None:
            errors.append(f"missing section '## {name}'")
        elif not fm.meaningful(t):
            errors.append(f"section '## {name}' is empty")
    if SEAL not in body:
        errors.append("missing the phase separator comment (see PROTOCOL.md)")

    after = body.split(SEAL, 1)[1] if SEAL in body else ""
    measured = fm.find_section(secs, "Measured")
    verdict_text = fm.find_section(secs, "Verdict")

    if status == "withheld":
        # The seal: nothing measured may be present.
        if fm.meaningful(measured):
            errors.append("SEAL BROKEN: '## Measured' has content while lookup_status is withheld")
        if fm.meaningful(verdict_text):
            errors.append("SEAL BROKEN: '## Verdict' has content while lookup_status is withheld")
        if fields.get("verdict") is not None:
            errors.append("SEAL BROKEN: verdict is set while lookup_status is withheld")
        if fields.get("phase_a_commit") is not None:
            errors.append("phase_a_commit must be null until Phase B")
        # A URL after the seal means a source was already consulted.
        for m in re.finditer(r"https?://\S+", after):
            errors.append(f"SEAL BROKEN: source URL present after the phase separator: {m.group(0)[:60]}")
    elif status == "revealed":
        for name in PHASE_B_SECTIONS:
            t = fm.find_section(secs, name)
            if t is None:
                errors.append(f"missing section '## {name}'")
            elif not fm.meaningful(t):
                errors.append(f"section '## {name}' is empty in a revealed prediction")
        v = fields.get("verdict")
        if v not in VERDICTS:
            errors.append(f"verdict must be one of {sorted(VERDICTS)}")
        if str(fields.get("discriminating")).lower() == "no" and v == "hit":
            errors.append("a non-discriminating prediction cannot score 'hit' — use 'non-discriminating'")
        commit = fields.get("phase_a_commit")
        if not commit:
            errors.append("phase_a_commit is required in Phase B (the commit that sealed the prediction)")
        else:
            if not git("cat-file", "-t", commit).strip() == "commit":
                errors.append(f"phase_a_commit '{commit}' is not a commit in this repository")
            else:
                sealed = git("show", f"{commit}:audit/prediction/{filename}")
                if not sealed:
                    errors.append(f"file was not present in phase_a_commit '{commit}'")
                else:
                    sf, sbody, _ = fm.parse(sealed)
                    if (sf or {}).get("lookup_status") != "withheld":
                        errors.append(f"in commit '{commit}' this file was not sealed (lookup_status != withheld)")
                    a_now = body.split(SEAL, 1)[0]
                    a_then = sbody.split(SEAL, 1)[0] if SEAL in sbody else sbody
                    if a_now.strip() != a_then.strip():
                        errors.append("Phase A text was edited after sealing — the prediction no longer matches "
                                      "what was committed (PROTOCOL: Phase A is never edited)")
        if not re.search(r"https?://", measured or ""):
            errors.append("'## Measured' has no source URL")
    return errors, warnings


def run():
    if not os.path.isdir(PRED_DIR):
        print("validate_prediction: no audit/prediction/ directory")
        return 0
    names = sorted(n for n in os.listdir(PRED_DIR) if n.endswith(".md") and n != "PROTOCOL.md")
    n_err = n_warn = 0
    for name in names:
        with open(os.path.join(PRED_DIR, name), encoding="utf-8") as f:
            errors, warnings = check(f.read(), name)
        for e in errors:
            print(f"ERROR   audit/prediction/{name}: {e}")
        for w in warnings:
            print(f"WARNING audit/prediction/{name}: {w}")
        n_err += len(errors); n_warn += len(warnings)
    print(f"validate_prediction: {len(names)} prediction(s), {n_err} error(s), {n_warn} warning(s)")
    return 1 if n_err else 0


SEALED = """---
id: PRED-001
target: "ratio of X to Y"
organism: "E. coli K-12"
framework_route: "v5.1 Layer I.C Domain 9 algorithm, steps 1-7"
prediction_kind: structural
tolerance: "within a factor of 3"
contamination_risk: low
discriminating: yes
lookup_status: withheld
phase_a_commit: null
verdict: null
---

## Target
The ratio.

## Framework route (the algorithm, run literally)
1. Step one.

## Derivation trace
Because of the gradient.

## Prediction
The ratio exceeds 1.

## Tolerance (what counts as a hit / a miss)
Hit if > 1; miss otherwise.

## Framework-free default
No expectation either way.

## Contamination disclosure
Executor is a language model; risk graded low because the quantity is organism-specific.

<!-- PHASE B BELOW THIS LINE — must be empty when Phase A is committed -->
## Measured

## Verdict

## What this does and does not show
"""


def selftest():
    cases = [
        ("valid sealed Phase A", SEALED, "PRED-001.md", 0),
        ("seal broken: measured value present",
         SEALED.replace("## Measured\n", "## Measured\n| r | 4.2 | 0.1 | measured-single | https://x | 2026-09-28 |\n"),
         "PRED-001.md", 2),
        ("seal broken: verdict set in front matter",
         SEALED.replace("verdict: null", "verdict: hit"), "PRED-001.md", 1),
        ("no tolerance stated",
         SEALED.replace('tolerance: "within a factor of 3"', "tolerance: null")
               .replace("Hit if > 1; miss otherwise.", ""), "PRED-001.md", 2),
        ("bad vocabulary", SEALED.replace("contamination_risk: low", "contamination_risk: none"),
         "PRED-001.md", 1),
        ("revealed without phase_a_commit",
         SEALED.replace("lookup_status: withheld", "lookup_status: revealed")
               .replace("verdict: null", "verdict: hit")
               .replace("## Measured\n", "## Measured\n| r | 4.2 | 0.1 | measured-single | https://x | 2026-09-28 |\n")
               .replace("## Verdict\n", "## Verdict\nHit.\n")
               .replace("## What this does and does not show\n", "## What this does and does not show\nLittle.\n"),
         "PRED-001.md", 1),
        ("missing phase separator", SEALED.replace(SEAL, "## Phase B"), "PRED-001.md", 1),
    ]
    failed = 0
    for label, text, name, expected in cases:
        errors, _ = check(text, name)
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
