---
id: CONST-imaginary-unit
canon_ref: v5.1 Appendix D, Mathematical Constants
canon_label: "i — Imaginary Unit"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Mathematical Constants*, row i. **Value:** √(-1). **Framework Role:** "The number whose square is -1. Allows representation of rotation, oscillation, and quantum phase. Without i, quantum mechanics cannot be written. Per Polarity at maximum abstraction: i is the axis perpendicular to the real number line — the geometric expression of 'opposites at right angles to each other.'"

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| i² in Python complex arithmetic | −1 + 0j | exact | derived | audit/constants/check_math_constants.py | 2026-09-24 |
| arg(i) | π/2 (1.5707963267948966) | float precision | derived | audit/constants/check_math_constants.py | 2026-09-24 |
| real-number standard QM vs complex QM, superconducting-qubit network test (Chen et al., PRL 128, 040403) | real-number bound 7.66 beaten by 43σ | as published | measured-reproduced | https://arxiv.org/abs/2103.08123 | 2026-09-24 |
| same test, photonic network (Li et al., PRL 128, 040402) | real QM constraints violated by >4.5σ | as published | measured-reproduced | https://arxiv.org/abs/2111.15128 | 2026-09-24 |
| theory: real/complex QM distinguishable in network scenarios (Renou et al., Nature 600, 625) | prediction of the test above | n/a | derived | https://arxiv.org/abs/2101.10873 | 2026-09-24 |
| theory (preprint, 2025): a real-number QM with modified tensor-product rule claimed consistent and experimentally indistinguishable | claim, not yet reproduced | n/a | held-open | https://arxiv.org/abs/2504.02808 | 2026-09-24 |

These values are defined or proven, not measured: the grade is `derived` and the derivation is the script. Every computed digit comes from `audit/constants/check_math_constants.py` (Python standard library, run 2026-09-24). The QM rows test the role-text claim, not the value.

## Scientific Inquiry run
1. Question (precise): Is i² = −1 (value), and is 'without i, quantum mechanics cannot be written' supported by measurement?
2. What an answer must look like: Value by computation; the QM claim by experiments that distinguish real- from complex-number quantum theory.
3. Falsifiability condition: Value: i² ≠ −1. Role claim: an experiment matching real-number QM where complex QM fails, or a consistent real formulation.
4. Variables: measurable / bounded / held open: Derived: i² = −1. Measured: two independent network experiments rule out the *standard* real-number formulation. Held open: whether some *other* real formulation (Hoffreumon & Woods 2025) is viable.
5. Test designed: `audit/constants/check_math_constants.py` for the value; literature fetch for the QM claim.
6. Data (unfiltered): i² = −1 PASS; arg i = π/2 PASS. Chen et al. and Li et al. independently exclude real-number standard QM (43σ, >4.5σ). Hoffreumon & Woods (arXiv:2504.02808) argue a different real formulation (different composition rule) is consistent and indistinguishable. Unresolved in the literature as of retrieval.
7. Variable Principle applied: The role claim is held open between 'standard formalism needs i' (measured) and 'no formalism can avoid i' (contested). Not filled.
8. Model update (Capsule: what the failed parts contribute): The value survives. The role text's absolute wording ('cannot be written') narrows to: the standard tensor-product formalism with real numbers is experimentally excluded; whether any real formalism works is open.
9. Documented: this file; `audit/constants/check_math_constants.py`.
10. Next baseline: No re-run needed for the value (a definition does not drift). Re-audit only if canon's wording of the role text changes (Phase 9).

## Forcing Test
- Test A (Ground): Within-system: a defined mathematical object, checked by explicit computation (no measurement involved).
- Test B (Uniqueness): One candidate (up to the sign choice ±i, which is a convention).
- Test C (Direction): Definition → value. The computation runs from the definition to the digits; canon's string is the thing tested.
- Test D (Falsifiability): Falsifier stated; did not fire for the value. For the role claim, a live counter-proposal exists.
- **Outcome:** forced-fill (value); role claim 'QM cannot be written without i' = live-hypothesis

## Anti-Operation (the gap this opens)
Whether complex numbers are *necessary* for quantum theory, or only for its standard composition rule, is an open question in the literature (2021 experiments vs 2025 preprint). That boundary is the gap.

## Narrative stripped (if any)
Removed: "Per Polarity at maximum abstraction … opposites at right angles to each other". The geometric fact (i rotates the plane by 90°) is kept; its reading as Polarity is interpretation that reality neither forces nor contradicts.

### Framework Role text — claim-by-claim (graded separately from the value)
| Role-text claim | Reality | Verdict |
| --- | --- | --- |
| Represents rotation, oscillation, quantum phase | Multiplication by i = 90° rotation; standard | accounted |
| Without i, QM cannot be written | Standard real-number formalism excluded by two experiments; alternative real formalism proposed (preprint) | live-hypothesis — wording too absolute |

**Role-text verdict:** value correct; 'cannot be written' should read 'the standard formalism requires complex numbers (experimentally tested); necessity in general is contested'.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Canon rows quoted; audit text is an
adaptation, not endorsed by the author.
```
