# [Tooling] Reality Audit — Phase 0: Foundation

*Drafted issue body. The `gh` CLI is not available to the executor, so per the brief (§8) the issue is written here and referenced from the PR.*

**Template:** the brief names a "Docs / navigation / tooling" issue template; none exists in `.github/ISSUE_TEMPLATE` (see FINDINGS F-009). This body follows the PR template's matching change type: **Docs / navigation / tooling (no change to canonical text).**

## What

Lay the foundation for the Reality Audit (`tasks/reality-audit/TASK.md`): the standing brief, the governing model as substrate, the audit and container skeletons with their schemas, and two stdlib validators. Link the new areas from `README.md` and `llms.txt` as derivation / work-in-progress.

## Why

The audit compares the explicit log (canon) with the implicit log (reality). Before any item is audited, the record formats, vocabularies, and checks have to exist, so every later phase writes to the same schema (Master Meta-Algorithm step 9: do not skip the organization step).

## Scope

- `tasks/reality-audit/TASK.md` — the brief, committed verbatim.
- `substrate/README.md`, `substrate/2026-09-24-reality-filter.md` — the governing model, as substrate, unclassified.
- `audit/README.md` (governing Master Meta run), `SCHEMA.md`, `FINDINGS.md` (F-001 – F-007 seeded; F-008, F-009 found), `COVERAGE.md` (scope counted from canon; nothing audited).
- `containers/README.md`, `TEMPLATE.md`, `INDEX.md` (no containers yet; Phase 7 seed candidates listed).
- `tools/validate_audit.py`, `tools/validate_containers.py`, `tools/frontmatter.py`, `tools/README.md`.
- `README.md` "Start here" and repository map; `llms.txt`; `CHANGELOG.md` repository-change entry.

## Out of scope

Any change to canonical text: `versions/`, `framework/`, `CONTRIBUTING.md`, `AGENTS.md`, the PR template. No variable moves; no Iteration Ledger row.

## Variable movement

None. Two new findings are opened as questions for later phases (F-008: `forced-no` used but undefined as an outcome class; F-009: missing issue template).
