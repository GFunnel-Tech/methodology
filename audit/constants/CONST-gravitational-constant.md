---
id: CONST-gravitational-constant
canon_ref: v5.1 Appendix D, Physical Constants
canon_label: "G — Gravitational Constant"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Physical Constants* table. **Value:** 6.674×10⁻¹¹ N·m²/kg². **Framework Role:** "The strength of gravitational attraction. Per Polarity at cosmic scale: the universal Yin force — pulling, gathering, contracting. Counterbalances the expansionary forces (Yang)."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Newtonian constant of gravitation G | 6.674 30 × 10⁻¹¹ m³ kg⁻¹ s⁻² | 0.000 15 × 10⁻¹¹ (22 ppm) | measured-reproduced | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): Does canon's G match CODATA 2022 at canon's precision?
2. What an answer must look like: A primary-source value with uncertainty, compared with canon at canon's own stated precision; a separate statement of whether the role text is measured, modeled, or interpretive.
3. Falsifiability condition: CODATA G outside 6.6735–6.6745 × 10⁻¹¹.
4. Variables: measurable / bounded / held open: Measurable: G (22 ppm, the least precise fundamental constant; independent determinations scatter beyond their stated errors). Held open: the cause of that scatter.
5. Test designed: Rounding-consistency check in `audit/constants/check_physical_constants.py`: canon passes if |canon − measured| ≤ half a unit of canon's last digit + measured 1σ.
6. Data (unfiltered): CODATA 2022: 6.674 30(15) × 10⁻¹¹. Canon 6.674 × 10⁻¹¹. Script: consistent.
7. Variable Principle applied: The value is graded by measurement. The role text is graded separately (see Narrative stripped); no open variable is filled.
8. Model update (Capsule: what the failed parts contribute): Nothing failed in the value. Interpretive clauses that measurement does not support are retained in the lineage (v5.1 text is unchanged) and proposed for status tags in v5.5.
9. Documented: this file; `audit/constants/check_physical_constants.py`.
10. Next baseline: Re-run on the next CODATA adjustment / cosmology data release (Phase 9).

## Forcing Test
- Test A (Ground): Within-system — a measured quantity compared with a written value.
- Test B (Uniqueness): One candidate survives at 4 significant figures.
- Test C (Direction): The comparison runs from measurement to text: reality is the authority (substrate item 1).
- Test D (Falsifiability): Falsifier stated in step 3; it did not fire for the value.
- **Outcome:** forced-fill (value); see Anti-Operation for the role text

## Anti-Operation (the gap this opens)
G's independent measurements disagree with each other by more than their quoted uncertainties (CODATA inflates the uncertainty to cover this). The value is settled to 4 figures; the 5th is an open edge.

## Narrative stripped (if any)
"The universal Yin force … counterbalances the expansionary forces (Yang)" — framework mapping. v5.4 §5 already forces a correction relevant here: gravitation's sign is attract / repel / neutral-by-group (convergence ∝ ρ+3p), so "G = pulling" is incomplete by canon's own later run. The mapping is stripped; the value stays.
