---
id: CONST-speed-of-light
canon_ref: v5.1 Appendix D, Physical Constants
canon_label: "c — Speed of Light"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Physical Constants* table. **Value:** 299,792,458 m/s. **Framework Role:** "The maximum speed at which information can propagate. Per Vibration: the upper bound of the vibrational spectrum. Per Cause and Effect: defines the causal horizon — no event can causally affect another faster than c. Einstein’s relativity is the mathematics of this constraint."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| speed of light in vacuum | 299 792 458 m s⁻¹ | exact (2019 SI defining constant, fixed from prior reproduced measurements) | measured-reproduced | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): Does canon's value for c match the primary reference, and is its factual core (c as the maximum signal speed) consistent with measurement?
2. What an answer must look like: A primary-source value with uncertainty, compared with canon at canon's own stated precision; a separate statement of whether the role text is measured, modeled, or interpretive.
3. Falsifiability condition: A CODATA value differing from 299,792,458 m/s at canon's precision; or a reproduced measurement of a signal faster than c.
4. Variables: measurable / bounded / held open: Measurable: c (exact by definition). Bounded: none. Held open: none for the value.
5. Test designed: Rounding-consistency check in `audit/constants/check_physical_constants.py`: canon passes if |canon − measured| ≤ half a unit of canon's last digit + measured 1σ.
6. Data (unfiltered): CODATA 2022: 299 792 458 m s⁻¹, exact. Script output: consistent.
7. Variable Principle applied: The value is graded by measurement. The role text is graded separately (see Narrative stripped); no open variable is filled.
8. Model update (Capsule: what the failed parts contribute): Nothing failed in the value. Interpretive clauses that measurement does not support are retained in the lineage (v5.1 text is unchanged) and proposed for status tags in v5.5.
9. Documented: this file; `audit/constants/check_physical_constants.py`.
10. Next baseline: Re-run on the next CODATA adjustment / cosmology data release (Phase 9).

## Forcing Test
- Test A (Ground): Within-system — a measured quantity compared with a written value.
- Test B (Uniqueness): One candidate survives: canon's value equals the defined value exactly.
- Test C (Direction): The comparison runs from measurement to text: reality is the authority (substrate item 1).
- Test D (Falsifiability): Falsifier stated in step 3; it did not fire for the value.
- **Outcome:** forced-fill (value); see Anti-Operation for the role text

## Anti-Operation (the gap this opens)
c is exact because the metre is defined from it; the audit therefore tests canon's transcription, not nature. What is measured is the constancy of c across frames and frequencies — that is the open edge a future container carries.

## Narrative stripped (if any)
"Per Vibration: the upper bound of the vibrational spectrum" — a framework mapping; reality neither forces nor contradicts it. Note that frequency has no measured upper bound tied to c (c bounds signal speed, not frequency), so the mapping as worded is not what measurement shows; keep the factual core (maximum signal speed) and drop the spectrum wording.
