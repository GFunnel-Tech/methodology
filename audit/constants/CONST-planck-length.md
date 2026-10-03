---
id: CONST-planck-length
canon_ref: v5.1 Appendix D, Physical Constants
canon_label: "Planck length — Minimum Meaningful Length"
proposed_label: "Planck length (unit √(ħG/c³))"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Physical Constants* table. **Value:** 1.616×10⁻³⁵ m. **Framework Role:** "Below this, spacetime as currently described breaks down. Per Mentalism: the boundary at which First Kingdom geometry yields to whatever the Third Kingdom substrate is."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Planck length √(ħG/c³) | 1.616 255 × 10⁻³⁵ m | 0.000 018 × 10⁻³⁵ | derived | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): Does canon's Planck length match CODATA 2022, and is it measured to be a minimum length?
2. What an answer must look like: A primary-source value with uncertainty, compared with canon at canon's own stated precision; a separate statement of whether the role text is measured, modeled, or interpretive.
3. Falsifiability condition: CODATA value outside 1.6155–1.6165 × 10⁻³⁵; for the 'minimum' clause: no measurement reaches this scale, so it cannot be falsified now.
4. Variables: measurable / bounded / held open: Derived: the unit (from G, ħ, c). Held open: any physical meaning of the scale (no experiment probes within ~15 orders of magnitude).
5. Test designed: Rounding-consistency check in `audit/constants/check_physical_constants.py`: canon passes if |canon − measured| ≤ half a unit of canon's last digit + measured 1σ.
6. Data (unfiltered): CODATA 2022: 1.616 255(18) × 10⁻³⁵ m. Script: consistent.
7. Variable Principle applied: The value is graded by measurement. The role text is graded separately (see Narrative stripped); no open variable is filled.
8. Model update (Capsule: what the failed parts contribute): Nothing failed in the value. Interpretive clauses that measurement does not support are retained in the lineage (v5.1 text is unchanged) and proposed for status tags in v5.5.
9. Documented: this file; `audit/constants/check_physical_constants.py`.
10. Next baseline: Re-run on the next CODATA adjustment / cosmology data release (Phase 9).

## Forcing Test
- Test A (Ground): Within-system — a measured quantity compared with a written value.
- Test B (Uniqueness): Value: one candidate. 'Minimum meaningful length': a live hypothesis (several quantum-gravity programmes; unobserved).
- Test C (Direction): The comparison runs from measurement to text: reality is the authority (substrate item 1).
- Test D (Falsifiability): Falsifier stated in step 3; it did not fire for the value.
- **Outcome:** forced-fill (value); see Anti-Operation for the role text

## Anti-Operation (the gap this opens)
v5.4 already holds 'line identity below Planck' proven-open. The label 'Minimum Meaningful Length' asserts what canon elsewhere holds open. Open edge: the label must carry the hypothesis status.

## Narrative stripped (if any)
The label "Minimum Meaningful Length" and "geometry yields to the Third Kingdom substrate" — the scale is a unit built from three constants; that spacetime 'breaks down' there is an extrapolation of current theory, not a measurement. Proposed label drops the claim.
