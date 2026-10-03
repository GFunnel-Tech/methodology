---
id: CONST-eulers-number
canon_ref: v5.1 Appendix D, Mathematical Constants
canon_label: "e — Euler's Number"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Mathematical Constants*, row e. **Value:** 2.71828182845904… **Framework Role:** "The base of natural growth. The unique number where d/dx(e^x) = e^x — the function that is its own derivative. The mathematical signature of compound interest, exponential decay, radioactive process, biological growth before constraint, and information entropy. Per Cause and Effect: the rate at which causes compound when no friction is present."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| e = Σ 1/n! (60 digits) | 2.71828182845904523536… | exact (defined) | derived | audit/constants/check_math_constants.py | 2026-09-24 |
| ∣d/dx eˣ − e∣ at x = 1 (central difference, independent series) | 1.1×10⁻⁴⁴ | n/a | derived | audit/constants/check_math_constants.py | 2026-09-24 |

These values are defined or proven, not measured: the grade is `derived` and the derivation is the script. Every computed digit comes from `audit/constants/check_math_constants.py` (Python standard library, run 2026-09-24).

## Scientific Inquiry run
1. Question (precise): Does canon's e string match Σ1/n!, and is the self-derivative property correctly stated?
2. What an answer must look like: Computed digits; the derivative property verified; wording checked.
3. Falsifiability condition: Digit mismatch, or d/dx eˣ ≠ eˣ.
4. Variables: measurable / bounded / held open: Derived only.
5. Test designed: `audit/constants/check_math_constants.py`: factorial series; central-difference derivative of an independently summed exp series at x = 1.
6. Data (unfiltered): Digits PASS (14-decimal truncation). Derivative equals e to 1.1×10⁻⁴⁴. Wording: the property characterises the base (b = e is the unique b with d/dx bˣ = bˣ); the functions equal to their own derivative are C·eˣ, so 'the function' is a slight compression. 'Information entropy' uses e only when entropy is measured in nats; the base is a unit choice (bits use 2).
7. Variable Principle applied: No variable open for the value. The Cause-and-Effect 'friction' reading is interpretation, not filled as fact.
8. Model update (Capsule: what the failed parts contribute): The value survives; the role text contributes two precision notes (unique base, not unique function; entropy base is a unit choice).
9. Documented: this file; `audit/constants/check_math_constants.py`.
10. Next baseline: No re-run needed for the value (a definition does not drift). Re-audit only if canon's wording of the role text changes (Phase 9).

## Forcing Test
- Test A (Ground): Within-system: a defined mathematical object, checked by explicit computation (no measurement involved).
- Test B (Uniqueness): One candidate.
- Test C (Direction): Definition → value. The computation runs from the definition to the digits; canon's string is the thing tested.
- Test D (Falsifiability): Falsifier stated; did not fire.
- **Outcome:** forced-fill (value); role text graded separately below

## Anti-Operation (the gap this opens)
'Biological growth before constraint' is exponential only in idealised models; which real populations were measured in an exponential phase, and for how long, is not specified by canon. The gap is an empirical dataset, not a mathematical one.

## Narrative stripped (if any)
Removed: "Per Cause and Effect: the rate at which causes compound when no friction is present" — a framework mapping; e is not a rate and reality does not force the reading.

### Framework Role text — claim-by-claim (graded separately from the value)
| Role-text claim | Reality | Verdict |
| --- | --- | --- |
| Unique number with d/dx(eˣ) = eˣ | Unique *base*; C·eˣ all satisfy f′ = f | accounted (compressed wording) |
| Signature of compound interest, decay, radioactive process | Continuous-compounding limit and first-order decay use eˣ | accounted |
| Signature of information entropy | Only in nats; base is a unit choice | convention |

**Role-text verdict:** value correct; minor wording compression.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Canon rows quoted; audit text is an
adaptation, not endorsed by the author.
```
