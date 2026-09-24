# Tools — Reality Audit Validators

> **Status: derivation / work-in-progress tooling.** These scripts check the Reality Audit's record formats. They check form, not truth: a file that passes has the required fields, vocabularies, and sections. Whether its content is right is the audit's job.

Standard library only (Python 3.8+), same convention as [`framework/tests/`](../framework/tests/README.md). No dependencies.

| Script | Checks | Specification |
| --- | --- | --- |
| [`validate_audit.py`](validate_audit.py) | Every file in `audit/{governance,labels,stages,constants,domains,unmapped}/`: front-matter keys and vocabularies; id pattern matches directory and file name; exclusion diagnosis present for `methodology-gap` / `conflict` / `unmapped`; `review_after` date on every `open` item (warns when overdue); observation rows carry a grade, a source, and a retrieval date; `adjusted` only on a `measured-reproduced` observation; required sections; every Scientific Inquiry and Forcing Test step filled unless an earlier step records `BLOCKED:`; no duplicate ids. | [`audit/SCHEMA.md`](../audit/SCHEMA.md) §1, §3, §4 |
| [`validate_containers.py`](validate_containers.py) | Every `containers/KC-####*.md`: required fields and vocabularies; non-empty trace; at least one open edge; at least one dated re-formation entry; an equation when `form` is `equation`/`both`, numbered steps when `algorithm`/`both`; a falsifier on every live hypothesis; `links_up` / `links_down` / `audit_refs` targets exist; every container listed in `containers/INDEX.md`. | [`audit/SCHEMA.md`](../audit/SCHEMA.md) §5 |
| [`frontmatter.py`](frontmatter.py) | Shared reader for the small YAML subset the schemas use. Anything outside that subset is an error, not a guess. | — |

## Run

```bash
python3 tools/validate_audit.py                 # all audit files
python3 tools/validate_audit.py audit/stages/STAGE-005.md   # specific files
python3 tools/validate_audit.py --today 2026-12-31          # check overdue review dates as of a date
python3 tools/validate_containers.py            # all containers + INDEX.md

python3 tools/validate_audit.py --selftest      # the validators test themselves
python3 tools/validate_containers.py --selftest
```

Exit status is `0` when there are no errors (warnings allowed) and `1` otherwise, so either script can gate a PR. Every audit and container PR runs both (brief §9).

If a validator and [`audit/SCHEMA.md`](../audit/SCHEMA.md) disagree, the schema is the specification and the validator has a bug.
