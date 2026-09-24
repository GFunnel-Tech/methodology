---
id: CONST-proton-mass
canon_ref: v5.1 Appendix D, Physical Constants
canon_label: "m_p — Proton Mass"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Physical Constants* table. **Value:** 1.673×10⁻²⁷ kg; m_p/m_e ≈ 1836. **Framework Role:** "The mass of the heavy positive nucleon. Ratio m_p/m_e ≈ 1836 — another fine-tuned dimensionless number."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| proton mass m_p | 1.672 621 925 95 × 10⁻²⁷ kg | 0.000 000 000 52 × 10⁻²⁷ | measured-reproduced | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | 2026-09-24 |
| proton-electron mass ratio | 1836.152 673 426 | 0.000 000 032 | measured-reproduced | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): Do canon's m_p and m_p/m_e match CODATA 2022?
2. What an answer must look like: A primary-source value with uncertainty, compared with canon at canon's own stated precision; a separate statement of whether the role text is measured, modeled, or interpretive.
3. Falsifiability condition: CODATA m_p outside 1.6725–1.6735 × 10⁻²⁷, or ratio outside 1835.5–1836.5.
4. Variables: measurable / bounded / held open: Measurable: both.
5. Test designed: Rounding-consistency check in `audit/constants/check_physical_constants.py`: canon passes if |canon − measured| ≤ half a unit of canon's last digit + measured 1σ.
6. Data (unfiltered): CODATA 2022 as tabled. Script: both consistent.
7. Variable Principle applied: The value is graded by measurement. The role text is graded separately (see Narrative stripped); no open variable is filled.
8. Model update (Capsule: what the failed parts contribute): Nothing failed in the value. Interpretive clauses that measurement does not support are retained in the lineage (v5.1 text is unchanged) and proposed for status tags in v5.5.
9. Documented: this file; `audit/constants/check_physical_constants.py`.
10. Next baseline: Re-run on the next CODATA adjustment / cosmology data release (Phase 9).

## Forcing Test
- Test A (Ground): Within-system — a measured quantity compared with a written value.
- Test B (Uniqueness): One candidate for each value.
- Test C (Direction): The comparison runs from measurement to text: reality is the authority (substrate item 1).
- Test D (Falsifiability): Falsifier stated in step 3; it did not fire for the value.
- **Outcome:** forced-fill (value); see Anti-Operation for the role text

## Anti-Operation (the gap this opens)
~99% of the proton's mass is not the rest mass of its quarks (it comes from the strong interaction), which is what v5.4 §6 is trying to model. Open edge: no framework derivation of 1836.15 exists.

## Narrative stripped (if any)
"Another fine-tuned dimensionless number" — interpretation; no measurement shows the ratio is 'tuned'. Stripped.
