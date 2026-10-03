---
id: CONST-elementary-charge
canon_ref: v5.1 Appendix D, Physical Constants
canon_label: "e — Elementary Charge"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Physical Constants* table. **Value:** 1.602×10⁻¹⁹ C. **Framework Role:** "The fundamental unit of electric charge. All free charges are integer multiples of e (charge quantization)."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| elementary charge e | 1.602 176 634 × 10⁻¹⁹ C | exact (2019 SI defining constant) | measured-reproduced | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): Does canon's e match CODATA 2022, and is 'all free charges are integer multiples of e' consistent with observation?
2. What an answer must look like: A primary-source value with uncertainty, compared with canon at canon's own stated precision; a separate statement of whether the role text is measured, modeled, or interpretive.
3. Falsifiability condition: CODATA e outside 1.6015–1.6025 × 10⁻¹⁹; or an isolated fractional charge observed.
4. Variables: measurable / bounded / held open: Measurable: e (exact). Bounded: searches for free fractional charges (none found). Held open: why charge is quantized.
5. Test designed: Rounding-consistency check in `audit/constants/check_physical_constants.py`: canon passes if |canon − measured| ≤ half a unit of canon's last digit + measured 1σ.
6. Data (unfiltered): CODATA 2022: exact. Script: consistent. Quarks carry ⅓e and ⅔e but have not been observed free; canon's 'free' qualifier makes the statement correct.
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
Why charge is quantized is not explained by measurement (magnetic monopoles would explain it; none observed). Open edge.

## Narrative stripped (if any)
None.
