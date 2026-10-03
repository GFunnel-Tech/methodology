---
id: CONST-mandelbrot-set
canon_ref: v5.1 Appendix D, Mathematical Constants
canon_label: "Mandelbrot Set Equation — Recursive Fractal Generator"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Mathematical Constants*, row Mandelbrot Set Equation. **Value:** zₙ₊₁ = zₙ² + c. **Framework Role:** "Per Correspondence at maximum: a single recursive equation produces infinite self-similar complexity at every zoom level. The mathematical proof that self-similarity is structural, not coincidental."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| orbit of 0 under z ↦ z² + c stays bounded (∣z∣ ≤ 2, 1000 iterations) | c ∈ {0, −1, −2, i, 0.25}: bounded; c ∈ {1, 0.26, 2i, −2.1}: escape | iteration cutoff | derived | audit/constants/check_math_constants.py | 2026-09-24 |
| Hausdorff dimension of ∂M (Shishikura) | 2 | exact (theorem) | derived | https://arxiv.org/abs/math/9201282 | 2026-09-24 |

These values are defined or proven, not measured: the grade is `derived` and the derivation is the script. Every computed digit comes from `audit/constants/check_math_constants.py` (Python standard library, run 2026-09-24). Canon's equation omits the two conditions that define the set: z₀ = 0 and 'c such that the orbit stays bounded'.

## Scientific Inquiry run
1. Question (precise): Is zₙ₊₁ = zₙ² + c the Mandelbrot iteration, and is the set 'self-similar at every zoom level'?
2. What an answer must look like: Membership checks; the known structure theorems.
3. Falsifiability condition: Wrong iteration; or a theorem showing exact self-similarity fails.
4. Variables: measurable / bounded / held open: Derived only.
5. Test designed: `audit/constants/check_math_constants.py`: escape-time test on reference points; Shishikura's theorem.
6. Data (unfiltered): Iteration PASS (with z₀ = 0 supplied). Self-similarity: M contains infinitely many small quasi-copies of itself, but it is not exactly self-similar (the copies are distorted and decorated differently); its boundary has Hausdorff dimension 2 (Shishikura). So 'infinite complexity' is supported; 'self-similar at every zoom level' is approximate, not exact.
7. Variable Principle applied: No variable open; the precise statement replaces the loose one.
8. Model update (Capsule: what the failed parts contribute): Equation survives with its definitional conditions added; 'self-similar' narrows to 'quasi-self-similar'.
9. Documented: this file; `audit/constants/check_math_constants.py`.
10. Next baseline: No re-run needed for the value (a definition does not drift). Re-audit only if canon's wording of the role text changes (Phase 9).

## Forcing Test
- Test A (Ground): Within-system: a defined mathematical object, checked by explicit computation (no measurement involved).
- Test B (Uniqueness): One candidate.
- Test C (Direction): Definition → value. The computation runs from the definition to the digits; canon's string is the thing tested.
- Test D (Falsifiability): Falsifier stated; fired for the exact-self-similarity reading.
- **Outcome:** forced-fill (equation); 'self-similar at every zoom level' narrows to quasi-self-similar

## Anti-Operation (the gap this opens)
Whether the Mandelbrot set is locally connected (the MLC conjecture) is an open problem; canon's 'proof that self-similarity is structural' rests on a set whose basic topology is still unsettled.

## Narrative stripped (if any)
Removed: "Per Correspondence at maximum … The mathematical proof that self-similarity is structural, not coincidental." The Mandelbrot set shows that one iteration can generate quasi-self-similar structure; it is not a proof about self-similarity elsewhere in reality. Reality does not force the Correspondence reading.

### Framework Role text — claim-by-claim (graded separately from the value)
| Role-text claim | Reality | Verdict |
| --- | --- | --- |
| Single recursive equation produces unbounded complexity | Boundary dimension 2 (Shishikura) | accounted |
| Self-similar at every zoom level | Quasi-self-similar, not exactly | over-stated |
| Proof that self-similarity is structural, not coincidental | Non sequitur (one example is not a general proof) | narrative |

**Role-text verdict:** equation correct but missing z₀ = 0 and the boundedness criterion; 'self-similar' over-stated.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Canon rows quoted; audit text is an
adaptation, not endorsed by the author.
```
