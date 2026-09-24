---
id: CONST-reduced-planck-constant
canon_ref: v5.1 Appendix D, Physical Constants
canon_label: "ℏ — Reduced Planck Constant"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Physical Constants* table. **Value:** 1.0546×10⁻³⁴ J·s. **Framework Role:** "The quantum of action. Sets the scale at which classical mechanics fails and quantum mechanics applies."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| reduced Planck constant ħ | 1.054 571 817… × 10⁻³⁴ J s | exact (h is a 2019 SI defining constant) | measured-reproduced | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): Does canon's ħ match CODATA 2022?
2. What an answer must look like: A primary-source value with uncertainty, compared with canon at canon's own stated precision; a separate statement of whether the role text is measured, modeled, or interpretive.
3. Falsifiability condition: CODATA ħ outside 1.05455–1.05465 × 10⁻³⁴.
4. Variables: measurable / bounded / held open: Measurable: ħ (exact). Held open: none for the value.
5. Test designed: Rounding-consistency check in `audit/constants/check_physical_constants.py`: canon passes if |canon − measured| ≤ half a unit of canon's last digit + measured 1σ.
6. Data (unfiltered): CODATA 2022: 1.054 571 817… × 10⁻³⁴ J s (exact). Script: consistent.
7. Variable Principle applied: The value is graded by measurement. The role text is graded separately (see Narrative stripped); no open variable is filled.
8. Model update (Capsule: what the failed parts contribute): Nothing failed in the value. Interpretive clauses that measurement does not support are retained in the lineage (v5.1 text is unchanged) and proposed for status tags in v5.5.
9. Documented: this file; `audit/constants/check_physical_constants.py`.
10. Next baseline: Re-run on the next CODATA adjustment / cosmology data release (Phase 9).

## Forcing Test
- Test A (Ground): Within-system — a measured quantity compared with a written value.
- Test B (Uniqueness): One candidate.
- Test C (Direction): The comparison runs from measurement to text: reality is the authority (substrate item 1).
- Test D (Falsifiability): Falsifier stated in step 3; it did not fire for the value.
- **Outcome:** forced-fill (value); see Anti-Operation for the role text

## Anti-Operation (the gap this opens)
"Sets the scale at which classical mechanics fails" is only partly true: the classical/quantum boundary also depends on decoherence rate, not ħ alone (v5.4 §7 carries 'environmental decay rates' as a required caution). Open edge: the boundary is a rate, not a constant.

## Narrative stripped (if any)
None beyond the Layer I.C cross-reference, which is a pointer, not a claim.
