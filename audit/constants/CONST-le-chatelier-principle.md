---
id: CONST-le-chatelier-principle
canon_ref: v5.1 Appendix D, Dynamical Laws
canon_label: "Le Chatelier's Principle"
diff_state: conflict
exclusion_diagnosis: reached-conflicting
claim_outcome: forced-no
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Dynamical Laws*, row Le Chatelier's Principle, Chemistry. **Text:** "A system at equilibrium, when disturbed, shifts to oppose the disturbance. Per Layer I.D + V: this IS the Garlick Equilibrium at molecular scale. The dynamic middle made law."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| ammonia synthesis N₂ + 3H₂ ⇌ 2NH₃, ideal gas, constant T and P: sign of ∂lnQ/∂n_N₂ at equilibrium | negative (shift right) for x_N₂ = 0.222; positive (shift LEFT, producing more N₂) for x_N₂ = 0.667; crossover x_N₂ = 1/2 | exact (ideal gas) | derived | audit/constants/check_law_derivations.py | 2026-09-24 |
| Uline & Corti 2006, J. Chem. Educ. 83, 138: 'The Ammonia Synthesis Reaction: An Exception to the Le Châtelier Principle and Effects of Nonideality' (bibliographic record) | exception confirmed; crossover mole fraction depends on T and P with nonideality | n/a | derived | https://api.semanticscholar.org/graph/v1/paper/DOI:10.1021/ed083p138 | 2026-09-24 |

Derivation: Q = x_NH₃²/(x_N₂ x_H₂³)·P⁻². Adding dn of N₂ at fixed T, P gives ∂lnQ/∂n_N₂ = −1/n_N₂ + 2/n_tot, positive when x_N₂ > 1/2; then Q > K and the reaction runs backward, producing more of the added species.

## Scientific Inquiry run
1. Question (precise): Does 'a system at equilibrium, when disturbed, shifts to oppose the disturbance' hold without exception?
2. What an answer must look like: A counter-example derived from equilibrium thermodynamics, or a proof that none exists.
3. Falsifiability condition: An equilibrium that shifts to *increase* the added species.
4. Variables: measurable / bounded / held open: Derived: the ammonia exception. Held open: none.
5. Test designed: `audit/constants/check_law_derivations.py`: reaction-quotient derivative for the ammonia equilibrium at constant T, P.
6. Data (unfiltered): Counter-example: adding N₂ when x_N₂ > 0.5 shifts the equilibrium toward N₂. The published literature treats this as a standard exception and notes that the principle's 'scientific inadequacy has long been documented'. Le Chatelier's principle is a heuristic; the law is ΔG = RT ln(Q/K).
7. Variable Principle applied: No variable open. The contradicting result is `derived`, not `measured-reproduced`, so the intake is open rather than adjusted (substrate item 8).
8. Model update (Capsule: what the failed parts contribute): The principle survives as a heuristic valid in many cases; the universal wording fails. The law is Q vs K.
9. Documented: this file; `audit/constants/check_law_derivations.py`.
10. Next baseline: Re-audit when the Garlick Equilibrium (Layer I.D / V) is audited (Phase 5): its identification with this principle inherits the exception.

## Forcing Test
- Test A (Ground): Derivation within equilibrium thermodynamics.
- Test B (Uniqueness): The universal statement leaves zero candidates (counter-example exists).
- Test C (Direction): Measurement → text. Reality is the authority (substrate item 1); the canonical wording is what is tested.
- Test D (Falsifiability): Falsifier fired.
- **Outcome:** forced-no (as a universal law)

## Anti-Operation (the gap this opens)
Canon identifies the Garlick Equilibrium with this principle ('this IS'). If the principle has exceptions, the identification either inherits them or needs a stated domain. The domain is the gap.

## Narrative stripped (if any)
Removed: "Per Layer I.D + V: this IS the Garlick Equilibrium at molecular scale. The dynamic middle made law." Mapping; reality does not force it, and the 'law' it names is not exceptionless.

### Framework Role text — claim-by-claim (graded separately from the value)
| Role-text claim | Reality | Verdict |
| --- | --- | --- |
| Shifts to oppose the disturbance | Counter-example (ammonia, x_N₂ > 0.5) | contradicted as universal |
| IS the Garlick Equilibrium | Mapping | narrative |

**Role-text verdict:** the law as stated has a derived counter-example; it is a heuristic, not a law.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Canon rows quoted; audit text is an
adaptation, not endorsed by the author.
```
