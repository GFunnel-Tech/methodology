---
id: CONST-lucas-sequence
canon_ref: v5.1 Appendix D, Mathematical Constants
canon_label: "Lucas Sequence — Companion to Fibonacci"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Mathematical Constants*, row Lucas Sequence. **Value:** 2, 1, 3, 4, 7, 11, 18, 29, 47… **Framework Role:** "Same recursion (each term = sum of two prior) with different seed. Demonstrates that the recursion itself, not the starting point, produces the φ attractor. Per Variable Principle: the structural truth survives changes in initial conditions."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| first 9 Lucas terms | 2, 1, 3, 4, 7, 11, 18, 29, 47 | exact | derived | audit/constants/check_math_constants.py | 2026-09-24 |
| ∣L₄₀/L₃₉ − φ∣ | 2.93×10⁻¹⁶ | n/a | derived | audit/constants/check_math_constants.py | 2026-09-24 |
| ratio after 30 steps from seed (1, ψ), ψ = (1−√5)/2 | −0.618033988750 (= ψ, not φ) | 70-digit Decimal | derived | audit/constants/check_math_constants.py | 2026-09-24 |

These values are defined or proven, not measured: the grade is `derived` and the derivation is the script. Every computed digit comes from `audit/constants/check_math_constants.py` (Python standard library, run 2026-09-24).

## Scientific Inquiry run
1. Question (precise): Are the Lucas terms correct, and does the ratio reach φ independent of the seed?
2. What an answer must look like: Terms computed; convergence shown; the general solution aφⁿ + bψⁿ used to find seeds where it fails.
3. Falsifiability condition: Terms wrong, or a seed for which the ratio does not converge to φ.
4. Variables: measurable / bounded / held open: Derived only.
5. Test designed: `audit/constants/check_math_constants.py`: generate terms; test convergence; test the seed (1, ψ).
6. Data (unfiltered): Terms PASS; L₄₀/L₃₉ → φ PASS. Exception: any seed proportional to (1, ψ) has a = 0, so the ratio stays at ψ = −0.618…; the seed (0, 0) gives no ratio. For every other seed the ratio → φ, because |ψ| < 1.
7. Variable Principle applied: No variable open; the exception is exact.
8. Model update (Capsule: what the failed parts contribute): Canon's claim survives with a measure-zero exception: 'every seed except multiples of (1, ψ) and (0, 0)'.
9. Documented: this file; `audit/constants/check_math_constants.py`.
10. Next baseline: No re-run needed for the value (a definition does not drift). Re-audit only if canon's wording of the role text changes (Phase 9).

## Forcing Test
- Test A (Ground): Within-system: a defined mathematical object, checked by explicit computation (no measurement involved).
- Test B (Uniqueness): One candidate.
- Test C (Direction): Definition → value. The computation runs from the definition to the digits; canon's string is the thing tested.
- Test D (Falsifiability): Falsifier stated; fired only on the exceptional seed family.
- **Outcome:** forced-fill (value); role claim accounted with a stated exception

## Anti-Operation (the gap this opens)
Canon generalises from this to 'structural truth survives changes in initial conditions'. For linear recurrences that holds generically; for non-linear recursions (e.g. the Mandelbrot map, next row) it does not. The class of systems where the generalisation holds is the gap.

## Narrative stripped (if any)
Removed: "Per Variable Principle: the structural truth survives changes in initial conditions." A framework mapping; the mathematics supports it only for this linear recurrence with the stated exception.

### Framework Role text — claim-by-claim (graded separately from the value)
| Role-text claim | Reality | Verdict |
| --- | --- | --- |
| The recursion, not the starting point, produces φ | True for all seeds except multiples of (1, ψ) and (0, 0) | accounted with exception |

**Role-text verdict:** correct with a measure-zero exception canon does not state.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Canon rows quoted; audit text is an
adaptation, not endorsed by the author.
```
