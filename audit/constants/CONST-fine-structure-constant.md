---
id: CONST-fine-structure-constant
canon_ref: v5.1 Appendix D, Physical Constants
canon_label: "α — Fine-Structure Constant"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Physical Constants* table. **Value:** 1/137.036…. **Framework Role:** "The strength of electromagnetic interaction. Dimensionless — pure number. If α were 4% different, no carbon, no life. Per Layer I.G: the most-cited candidate for fine-tuning evidence at cosmological scale."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| inverse fine-structure constant α⁻¹ | 137.035 999 177 | 0.000 000 021 | measured-reproduced | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): Does canon's α match CODATA 2022, and is the counterfactual '4% different → no carbon' a measurement?
2. What an answer must look like: A primary-source value with uncertainty, compared with canon at canon's own stated precision; a separate statement of whether the role text is measured, modeled, or interpretive.
3. Falsifiability condition: CODATA α⁻¹ outside 137.0355–137.0365.
4. Variables: measurable / bounded / held open: Measurable: α (0.15 ppb). Held open: any counterfactual about other values of α — no measurement can reach a universe with a different α.
5. Test designed: Rounding-consistency check in `audit/constants/check_physical_constants.py`: canon passes if |canon − measured| ≤ half a unit of canon's last digit + measured 1σ.
6. Data (unfiltered): CODATA 2022: α⁻¹ = 137.035 999 177(21). Script: consistent.
7. Variable Principle applied: The value is graded by measurement. The role text is graded separately (see Narrative stripped); no open variable is filled.
8. Model update (Capsule: what the failed parts contribute): Nothing failed in the value. Interpretive clauses that measurement does not support are retained in the lineage (v5.1 text is unchanged) and proposed for status tags in v5.5.
9. Documented: this file; `audit/constants/check_physical_constants.py`.
10. Next baseline: Re-run on the next CODATA adjustment / cosmology data release (Phase 9).

## Forcing Test
- Test A (Ground): Within-system — a measured quantity compared with a written value.
- Test B (Uniqueness): One candidate for the value. The '4% → no carbon' clause has no measured referent.
- Test C (Direction): The comparison runs from measurement to text: reality is the authority (substrate item 1).
- Test D (Falsifiability): Falsifier stated in step 3; it did not fire for the value.
- **Outcome:** forced-fill (value); see Anti-Operation for the role text

## Anti-Operation (the gap this opens)
The value is forced; the fine-tuning clause is a model-derived counterfactual (stellar-nucleosynthesis calculations), unobservable in principle. It is not evidence of anything by itself. Open edge: whether α varies in time or space (tested by quasar spectra and atomic clocks; bounded, not closed).

## Narrative stripped (if any)
"If α were 4% different, no carbon, no life" and "most-cited candidate for fine-tuning evidence" — a theoretical counterfactual, not an observation. Stripped from the entry's graded core; if kept, it must be tagged live-hypothesis (model result), not presented alongside measured values.
