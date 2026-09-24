---
id: CONST-fibonacci-sequence
canon_ref: v5.1 Appendix D, Mathematical Constants
canon_label: "Fibonacci Sequence — Recursive Growth Sequence"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Mathematical Constants*, row Fibonacci Sequence. **Value:** 1, 1, 2, 3, 5, 8, 13, 21, 34, 55… **Framework Role:** "Each term is the sum of the two prior. Already operationalized in Layer III (Fibonacci Build Sequence) and Layer III+ (Integration Density). The growth pattern of all living systems. The ratio of consecutive terms approaches φ."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| first 10 Fibonacci terms | 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 | exact | derived | audit/constants/check_math_constants.py | 2026-09-24 |
| ∣F₄₀/F₃₉ − φ∣ | 1.12×10⁻¹⁶ | n/a | derived | audit/constants/check_math_constants.py | 2026-09-24 |
| sunflower (Helianthus annuus) parastichy numbers that are Fibonacci (Swinton et al. 2016, R. Soc. Open Sci., 657 heads) | 565 of 768 | count | measured-single | https://api.crossref.org/works/10.1098/rsos.160091 | 2026-09-24 |
| … with other predefined Fibonacci structure | 67 of 768 | count | measured-single | https://api.crossref.org/works/10.1098/rsos.160091 | 2026-09-24 |
| … without Fibonacci structure (768 − 565 − 67) | 136 of 768 (17.7%) | count | derived | audit/constants/check_math_constants.py | 2026-09-24 |

These values are defined or proven, not measured: the grade is `derived` and the derivation is the script. Every computed digit comes from `audit/constants/check_math_constants.py` (Python standard library, run 2026-09-24). The sunflower rows test the role text ('all living systems'); the study also reports quasi-regular heads with no assignable parastichy number.

## Scientific Inquiry run
1. Question (precise): Are canon's terms and the φ limit correct, and is 'the growth pattern of all living systems' supported?
2. What an answer must look like: Computed terms; convergence; the largest systematic dataset on the textbook biological example.
3. Falsifiability condition: Terms wrong; ratio does not converge to φ; living systems observed without Fibonacci structure.
4. Variables: measurable / bounded / held open: Derived: terms, limit. Measured: sunflower parastichy counts. Held open: frequency across all taxa (no dataset covers 'all living systems').
5. Test designed: `audit/constants/check_math_constants.py`; Swinton et al. abstract (Crossref).
6. Data (unfiltered): Terms PASS; limit PASS. In the canonical example (sunflowers), 136/768 = 17.7% of parastichy numbers had no Fibonacci structure, and some heads had no assignable parastichy number at all. Many organisms (e.g. radially symmetric animals, bacteria dividing by binary fission) show no Fibonacci pattern; no source claims universality.
7. Variable Principle applied: The universal claim is not filled. What is measured: Fibonacci structure is frequent, not universal, even in phyllotaxis.
8. Model update (Capsule: what the failed parts contribute): Value survives. 'Growth pattern of all living systems' fails its own falsifier on the best-studied case; it narrows to 'common in plant phyllotaxis'.
9. Documented: this file; `audit/constants/check_math_constants.py`.
10. Next baseline: No re-run needed for the value (a definition does not drift). Re-audit only if canon's wording of the role text changes (Phase 9).

## Forcing Test
- Test A (Ground): Within-system: a defined mathematical object, checked by explicit computation (no measurement involved).
- Test B (Uniqueness): One candidate for the sequence.
- Test C (Direction): Definition → value. The computation runs from the definition to the digits; canon's string is the thing tested.
- Test D (Falsifiability): Falsifier stated; did not fire for the value; fired for the universal biological claim (counter-examples measured).
- **Outcome:** forced-fill (value); role claim 'all living systems' = forced-no

## Anti-Operation (the gap this opens)
The frequency of Fibonacci phyllotaxis across plant taxa, and the mechanism that produces the non-Fibonacci cases, are open (the study reports competing biomathematical models). That is the gap.

## Narrative stripped (if any)
Removed: links to Layer III (Fibonacci Build Sequence) and Layer III+ (framework mapping). The universal-biology sentence is not narrative but a factual over-claim; it is graded in the table below.

### Framework Role text — claim-by-claim (graded separately from the value)
| Role-text claim | Reality | Verdict |
| --- | --- | --- |
| Each term is the sum of the two prior; ratio → φ | Verified | accounted |
| The growth pattern of all living systems | 17.7% of sunflower parastichies non-Fibonacci (Swinton 2016); no universality evidence | forced-no (over-claim) |

**Role-text verdict:** value correct; 'growth pattern of all living systems' is an over-claim contradicted by measurement — narrow to 'frequent in plant phyllotaxis'.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Canon rows quoted; audit text is an
adaptation, not endorsed by the author.
```
