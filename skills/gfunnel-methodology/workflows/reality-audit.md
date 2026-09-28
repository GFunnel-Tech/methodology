# Workflow — Reality Audit and Knowledge Containers

Use for: any work in `audit/`, `containers/`, `substrate/`, `tools/validate_*.py`, or a phase of the Reality Audit.

**Status: derivation / work in progress, not canon.** Nothing here enters the canon until the author declares a version. Say so whenever you cite it.

## Read first (in full, in this order)

1. `tasks/reality-audit/TASK.md`: the standing brief. §3 *Hard rules for the executor*, §8 *Phases and PR plan*, §9 *Definition of done*, §10 *When to stop and ask the author*.
2. `audit/README.md` (the governing Master Meta-Algorithm run), `audit/SCHEMA.md` (vocabularies and record formats: the specification), `audit/FINDINGS.md`, `audit/COVERAGE.md`.
3. `containers/README.md`, `containers/TEMPLATE.md`, `containers/INDEX.md`.
4. `substrate/README.md` and the dated substrate file(s).
5. Canon: v5.1 *Scientific Inquiry* algorithm, Appendix A (100-Stage Progression), Appendix D (Constants & Laws); v5.3 §1–§3 (Forcing Test, Anti-Operation); v5.4 §5, §11–§14. Use `SECTIONS.md` for line ranges.

## Per-item procedure

1. Pick the item and phase from `TASK.md` §8. Check `audit/COVERAGE.md` so you do not duplicate work.
2. Create the record from `audit/SCHEMA.md` §4 (or §5 for a container): correct id pattern, directory and front matter.
3. Fill **Canon says** (quote with the location) and **Reality shows** (each observation: measured quantity, uncertainty, reproducibility grade, a permitted source from SCHEMA §2, retrieval date; no interpretive wording).
4. Run the **Scientific Inquiry** algorithm step by step. If a step cannot be completed, write `BLOCKED:` with the reason and stop there.
5. Run the **Forcing Test** (A → D) and assign the outcome class; run the **Anti-Operation** and name the gap it opens.
6. For unmapped observations, run the **exclusion diagnosis first** (`TASK.md` §5.1; vocabulary in `audit/SCHEMA.md` §1.4), then the audit.
7. For solved items, create a container: at least one open edge; an equation **only** if measured or derived with a shown trace (otherwise numbered steps or `held-open`); a falsifier on every live hypothesis; list it in `containers/INDEX.md`.
8. Update `audit/COVERAGE.md`, `audit/FINDINGS.md` (new `F-###` rows), and ledger rows where a variable moved.
9. **Validate** (both must exit 0):

```bash
python3 tools/validate_audit.py
python3 tools/validate_containers.py
```

If the validator and `audit/SCHEMA.md` disagree, the schema wins and the validator has a bug.

## Hard rules (from TASK.md §3, abbreviated; the file is authoritative)

- Never edit released `versions/` files; corrections go to a `versions/v5.5/` **draft** awaiting author declaration.
- Never fill a held-open variable; never promote a live hypothesis or a stipulation.
- Every observation cites a measurement source. Where physical constants disagree with CODATA/PDG, reality wins: flag it `conflict`.
- Never invent an equation.
- Label everything canon does not name as a derivation.
- Stop and ask the author in the cases `TASK.md` §10 lists.
