---
id: CONST-electron-mass
canon_ref: v5.1 Appendix D, Physical Constants
canon_label: "m_e — Electron Mass"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Physical Constants* table. **Value:** 9.109×10⁻³¹ kg. **Framework Role:** "The mass of the lightest charged particle. Determines atomic structure. Per Layer I.C Domain 8: the unit currency of chemistry."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| electron mass m_e | 9.109 383 7139 × 10⁻³¹ kg | 0.000 000 0028 × 10⁻³¹ (0.31 ppb) | measured-reproduced | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): Does canon's m_e match CODATA 2022, and is 'lightest charged particle' correct?
2. What an answer must look like: A primary-source value with uncertainty, compared with canon at canon's own stated precision; a separate statement of whether the role text is measured, modeled, or interpretive.
3. Falsifiability condition: CODATA m_e outside 9.1085–9.1095 × 10⁻³¹; or a charged particle lighter than the electron.
4. Variables: measurable / bounded / held open: Measurable: m_e.
5. Test designed: Rounding-consistency check in `audit/constants/check_physical_constants.py`: canon passes if |canon − measured| ≤ half a unit of canon's last digit + measured 1σ.
6. Data (unfiltered): CODATA 2022: 9.109 383 7139(28) × 10⁻³¹ kg. Script: consistent. No lighter charged particle is known (neutrinos are neutral).
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
v5.4 §6 uses m_e as the input to the Koide/trefoil run ([framework/tests/koide-delta.md](../../framework/tests/koide-delta.md)); the lepton mass *ratios* are the open edge, not m_e itself.

## Narrative stripped (if any)
"Unit currency of chemistry" — framework mapping; harmless, not forced.
