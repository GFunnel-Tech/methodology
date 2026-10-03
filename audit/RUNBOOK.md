# Audit Runbook — How to Audit One Item

> **Status: derivation / work-in-progress.** The operating procedure for writing one audit file. It restates [`SCHEMA.md`](SCHEMA.md) and brief §3 as steps. Where the two disagree, `SCHEMA.md` wins.

## Before you start

Read: [`SCHEMA.md`](SCHEMA.md), [`../AGENTS.md`](../AGENTS.md), and the canonical text of the item you are auditing. Do not audit from memory of canon: quote it.

## The hard rules

1. **Never edit `versions/`, `framework/`, `CONTRIBUTING.md`, `AGENTS.md`.** Audit files only.
2. **Every number is fetched, not remembered.** A value enters `## Reality shows` only if it was retrieved from a primary source *during the run* (NIST/CODATA, PDG, Planck Legacy Archive / papers on arXiv, NCBI / PubMed, USGS, peer-reviewed measurement papers). Record the URL actually fetched and the retrieval date. If the source cannot be reached or does not state the value, grade the row `held-open` and say why. **A plausible number from memory is an assumption; the Variable Principle forbids it.**
3. **Observations are neutral.** The Quantity column names what was measured ("primordial helium-4 mass fraction Y_p"), never what it means ("the substrate set at the moment of creation").
4. **Split every canonical note into two claims.**
   - **The factual core**: what canon asserts happens or happened (e.g. "hydrogen, helium, trace lithium are formed"). This is what `diff_state`, `claim_outcome`, and `intake_result` grade.
   - **The framework mapping**: the Hermetic principle, Kingdom, or layer the note assigns (e.g. "Per Cause and Effect: all later atoms caused at this moment"). This is interpretation. Put it under `## Narrative stripped`, state whether reality forces it (usually: reality neither forces nor contradicts a mapping — say so), and do not let it change the grade of the factual core.
5. **Diff state is about the factual core.** Consistent with measurement → `accounted`. Canon states a number or fact that measurement contradicts → `conflict` with `exclusion_diagnosis: reached-conflicting`, `intake_result: adjusted` only if the contradicting measurement is `measured-reproduced`, else `open`. Canon asserts something no measurement reaches → `unobserved-claim`, `intake_result: open`, `review_after` set. Reality shows something canon's item leaves out that matters to the item → `methodology-gap` with a diagnosis.
6. **Outcome classes are honest.** `forced-fill` only when measurement leaves one candidate. A model with indirect support (e.g. inflation) is `live-hypothesis`. Canon's held-open items stay `proven-open` or `live-hypothesis`: **do not resolve them.**
7. **Labels.** If the canonical name carries a narrative reality does not force, set `proposed_label` to an observation-based name and explain under `## Narrative stripped`. Otherwise omit `proposed_label`.
8. **Run steps literally.** Fill all 10 Scientific Inquiry steps and all 4 Forcing Test tests plus Outcome. If a step cannot be completed, write `BLOCKED: <why>` at that step and leave the later steps empty.
9. **Anti-Operation.** Name at least one gap the result opens.
10. **`review_after`** for every `open` item: `2027-09-24` unless a scheduled data release justifies an earlier date (name it).
11. **Leave** `container: null` and `ledger_row: null` (filled in Phases 7/8).
12. **Validate:** `python3 tools/validate_audit.py <your files>` must report 0 errors.

## File skeleton

Copy from [`SCHEMA.md`](SCHEMA.md) §4. File path: `audit/<dir>/<ID>.md` (e.g. `audit/stages/STAGE-005.md`, `audit/constants/CONST-speed-of-light.md`, `audit/domains/DOMAIN-08.md`).

## Reporting back

Do not edit `FINDINGS.md` or `COVERAGE.md` directly when working in parallel with others; report findings to the coordinator, who consolidates them. Each finding: the item, what canon says, what reality shows (with source), and the proposed resolution.
