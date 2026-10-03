---
id: CONST-planck-time
canon_ref: v5.1 Appendix D, Physical Constants
canon_label: "Planck time — Minimum Meaningful Duration"
proposed_label: "Planck time (unit √(ħG/c⁵))"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Physical Constants* table. **Value:** 5.391×10⁻⁴⁴ s. **Framework Role:** "Below this, time as currently described breaks down. The first DETECT event of stage 2 cannot be smaller than this."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Planck time √(ħG/c⁵) | 5.391 247 × 10⁻⁴⁴ s | 0.000 060 × 10⁻⁴⁴ | derived | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): Does canon's Planck time match CODATA 2022, and is it measured to be a minimum duration?
2. What an answer must look like: A primary-source value with uncertainty, compared with canon at canon's own stated precision; a separate statement of whether the role text is measured, modeled, or interpretive.
3. Falsifiability condition: CODATA value outside 5.3905–5.3915 × 10⁻⁴⁴; the 'minimum' clause is not falsifiable with current measurement.
4. Variables: measurable / bounded / held open: Derived: the unit. Held open: physical meaning of the scale; the Stage 2 clause.
5. Test designed: Rounding-consistency check in `audit/constants/check_physical_constants.py`: canon passes if |canon − measured| ≤ half a unit of canon's last digit + measured 1σ.
6. Data (unfiltered): CODATA 2022: 5.391 247(60) × 10⁻⁴⁴ s. Script: consistent.
7. Variable Principle applied: The value is graded by measurement. The role text is graded separately (see Narrative stripped); no open variable is filled.
8. Model update (Capsule: what the failed parts contribute): Nothing failed in the value. Interpretive clauses that measurement does not support are retained in the lineage (v5.1 text is unchanged) and proposed for status tags in v5.5.
9. Documented: this file; `audit/constants/check_physical_constants.py`.
10. Next baseline: Re-run on the next CODATA adjustment / cosmology data release (Phase 9).

## Forcing Test
- Test A (Ground): Within-system — a measured quantity compared with a written value.
- Test B (Uniqueness): Value: one candidate. Minimum-duration and Stage 2 clauses: unobserved.
- Test C (Direction): The comparison runs from measurement to text: reality is the authority (substrate item 1).
- Test D (Falsifiability): Falsifier stated in step 3; it did not fire for the value.
- **Outcome:** forced-fill (value); see Anti-Operation for the role text

## Anti-Operation (the gap this opens)
"The first DETECT event of stage 2 cannot be smaller than this" constrains Stage 2 by a hypothesis. Open edge: carried to the Stage 2 audit (STAGE-002).

## Narrative stripped (if any)
Same as the Planck length: the label asserts a minimum no measurement shows.
