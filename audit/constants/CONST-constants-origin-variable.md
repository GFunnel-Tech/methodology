---
id: CONST-constants-origin-variable
canon_ref: v5.1 Appendix D, Physical Constants
canon_label: "◈ VARIABLE — origin of the physical constants"
diff_state: unobserved-claim
exclusion_diagnosis: n/a
claim_outcome: live-hypothesis
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Physical Constants* table. **Value:** (held-open variable, no value). **Framework Role:** "Whether the physical constants above are mathematically necessary, anthropically selected from a multiverse, or integrated from prior cosmological cycles per Layer I.G. The framework tightens toward integration: the cycle-integration explanation requires fewer assumptions than multiverse selection while remaining empirically compatible. Held open. Range narrows."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| any measurement distinguishing necessity / selection / prior-cycle origin of constants | none available | n/a | held-open | https://physics.nist.gov/cuu/Constants/ (constants are measured; their origin is not) | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): Does any measurement bear on why the constants have their values, and is canon's 'tightens toward integration' supported by one?
2. What an answer must look like: A primary-source value with uncertainty, compared with canon at canon's own stated precision; a separate statement of whether the role text is measured, modeled, or interpretive.
3. Falsifiability condition: For 'tightens toward integration': a measurement that one of the three candidates predicts and the others do not. None is named.
4. Variables: measurable / bounded / held open: Held open: all three candidates. Measurable: none.
5. Test designed: Rounding-consistency check in `audit/constants/check_physical_constants.py`: canon passes if |canon − measured| ≤ half a unit of canon's last digit + measured 1σ.
6. Data (unfiltered): No measurement found that discriminates between the three candidates.
7. Variable Principle applied: The value is graded by measurement. The role text is graded separately (see Narrative stripped); no open variable is filled.
8. Model update (Capsule: what the failed parts contribute): The failed comparison locates a defect in the explicit log, not in reality. Interpretive clauses that measurement does not support are retained in the lineage (v5.1 text is unchanged) and proposed for status tags in v5.5.
9. Documented: this file; `audit/constants/check_physical_constants.py`.
10. Next baseline: Re-run on the next CODATA adjustment / cosmology data release (Phase 9).

## Forcing Test
- Test A (Ground): Within-system — a measured quantity compared with a written value.
- Test B (Uniqueness): Three candidates survive; no observation eliminates any. 'Fewer assumptions' is a parsimony judgment, not a measurement.
- Test C (Direction): The comparison runs from measurement to text: reality is the authority (substrate item 1).
- Test D (Falsifiability): Falsifier stated in step 3; it fired or could not be evaluated as written — see Reality shows.
- **Outcome:** live-hypothesis

## Anti-Operation (the gap this opens)
Canon holds the variable open (honest) but states a lean ('tightens toward integration') with no measured basis. Under the Variable Principle a variable narrows by structure or evidence, not by preference. Open edge: name a discriminating observation, or drop the lean.

## Narrative stripped (if any)
"Tightens toward integration … requires fewer assumptions" — a preference, stripped from the status. The variable stays open with all three candidates equal.
