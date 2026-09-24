---
id: CONST-hubble-constant
canon_ref: v5.1 Appendix D, Physical Constants
canon_label: "H₀ — Hubble Constant"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Physical Constants* table. **Value:** ~67-73 km/s/Mpc. **Framework Role:** "Rate of cosmic expansion. Currently a measured tension between methods (“Hubble tension”) — itself a variable held open in cosmology."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| H₀, CMB (base-ΛCDM inferred) | 67.4 km s⁻¹ Mpc⁻¹ | 0.5 | derived | https://arxiv.org/abs/1807.06209 | 2026-09-24 |
| H₀, Cepheid–SN Ia distance ladder | 73.04 km s⁻¹ Mpc⁻¹ | 1.04 | measured-single | https://arxiv.org/abs/2112.04510 | 2026-09-24 |
| H₀, TRGB + Cepheid combined (same team) | 72.53 km s⁻¹ Mpc⁻¹ | 0.99 | measured-single | https://arxiv.org/abs/2112.04510 | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): Is canon's range ~67–73 and its statement of a tension consistent with the primary measurements?
2. What an answer must look like: A primary-source value with uncertainty, compared with canon at canon's own stated precision; a separate statement of whether the role text is measured, modeled, or interpretive.
3. Falsifiability condition: Either primary measurement outside ~67–73, or the two methods agreeing within errors.
4. Variables: measurable / bounded / held open: Measurable: both H₀ values. Held open: the cause of the tension.
5. Test designed: Rounding-consistency check in `audit/constants/check_physical_constants.py`: canon passes if |canon − measured| ≤ half a unit of canon's last digit + measured 1σ.
6. Data (unfiltered): Planck 67.4 ± 0.5; SH0ES 73.04 ± 1.04. Both inside canon's range. Difference 4.9σ (`audit/constants/check_physical_constants.py`).
7. Variable Principle applied: The value is graded by measurement. The role text is graded separately (see Narrative stripped); no open variable is filled.
8. Model update (Capsule: what the failed parts contribute): Nothing failed in the value. Interpretive clauses that measurement does not support are retained in the lineage (v5.1 text is unchanged) and proposed for status tags in v5.5.
9. Documented: this file; `audit/constants/check_physical_constants.py`.
10. Next baseline: Re-run on the next CODATA adjustment / cosmology data release (Phase 9).

## Forcing Test
- Test A (Ground): Within-system — a measured quantity compared with a written value.
- Test B (Uniqueness): The range and the existence of a tension are both forced by the two measurements. The cause is not.
- Test C (Direction): The comparison runs from measurement to text: reality is the authority (substrate item 1).
- Test D (Falsifiability): Falsifier stated in step 3; it did not fire for the value.
- **Outcome:** forced-fill (value); see Anti-Operation for the role text

## Anti-Operation (the gap this opens)
Canon correctly holds the tension open. Open edge: whether it is a systematic error or new physics; Phase 9 re-audits on new releases (e.g. JWST distance-ladder results).

## Narrative stripped (if any)
None — this entry already reads as measured-plus-open. It is the model for how the other entries should read.
