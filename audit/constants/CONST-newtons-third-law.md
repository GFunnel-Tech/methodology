---
id: CONST-newtons-third-law
canon_ref: v5.1 Appendix D, Dynamical Laws
canon_label: "Newton's Third Law (Action-Reaction)"
diff_state: methodology-gap
exclusion_diagnosis: not-reached
claim_outcome: live-hypothesis
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Dynamical Laws*, row Newton's Third Law (Action-Reaction), Classical Mechanics. **Text:** "For every action there is an equal and opposite reaction. Per Polarity: the universal expression of dual poles. No force exists without its counterforce."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| magnetic forces between two moving point charges (q₁ at origin moving +x; q₂ at (0,1,0) moving +y), low-velocity Biot–Savart | F on 1 = 0; F on 2 = (1.0×10⁻⁷, 0, 0) N (q = 1 C, v = 1 m s⁻¹, d = 1 m) | exact (classical EM) | derived | audit/constants/check_law_derivations.py | 2026-09-24 |
| μ₀ used in the derivation (CODATA 2022) | 1.256 637 061 27×10⁻⁶ N A⁻² | 0.000 000 000 20×10⁻⁶ | measured-reproduced | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | 2026-09-24 |

Classical electrodynamics: the pairwise forces are not equal and opposite; total momentum is conserved only when the electromagnetic field's momentum is counted.

## Scientific Inquiry run
1. Question (precise): Does the law, as canon states it, match its measured form and domain of validity?
2. What an answer must look like: A case in which the strong form fails, derived from measured electromagnetism.
3. Falsifiability condition: Two interacting bodies with unequal/non-opposite mutual forces.
4. Variables: measurable / bounded / held open: Derived: EM counter-example. Held open: none.
5. Test designed: `audit/constants/check_law_derivations.py`: Biot–Savart fields and Lorentz forces for two perpendicular moving charges.
6. Data (unfiltered): F₁₂ + F₂₁ = (1.0×10⁻⁷, 0, 0) N ≠ 0. The third law holds for contact forces and central static forces; it fails for velocity-dependent electromagnetic forces, where momentum conservation is restored by field momentum. So 'No force exists without its counterforce' is not universal between bodies.
7. Variable Principle applied: No variable open; but the derivation is `derived`, not `measured-reproduced`, so the intake is open rather than adjusted (substrate item 8).
8. Model update (Capsule: what the failed parts contribute): Law survives in its classical-mechanics domain; the universal clause fails. Momentum conservation (CONST-momentum-conservation) is the general law; the third law is its special case when fields carry no momentum.
9. Documented: this file; `audit/constants/check_law_derivations.py`.
10. Next baseline: Re-run on the next PDG edition (2026 Review of Particle Physics) or on the named experiment's next result (Phase 9).

## Forcing Test
- Test A (Ground): Derivation from measured EM.
- Test B (Uniqueness): One candidate: the strong form is not universal.
- Test C (Direction): Measurement → text. Reality is the authority (substrate item 1); the canonical wording is what is tested.
- Test D (Falsifiability): Falsifier fired for the universal clause.
- **Outcome:** live-hypothesis (third law as universal) → narrows to 'holds for contact and static central forces'

## Anti-Operation (the gap this opens)
Canon's 'universal expression of dual poles' is built on a law that fails when interactions are carried by fields with their own momentum. Where the counterforce goes (the field) is the gap: methodology-gap, not-reached.

## Narrative stripped (if any)
Removed: "Per Polarity: the universal expression of dual poles." Mapping; and the physics it rests on is not universal.

### Framework Role text — claim-by-claim (graded separately from the value)
| Role-text claim | Reality | Verdict |
| --- | --- | --- |
| Equal and opposite reaction | Holds for contact / static central forces | accounted (domain) |
| No force exists without its counterforce (universal) | Fails for moving charges; field momentum restores conservation | contradicted as universal |

**Role-text verdict:** 'No force exists without its counterforce' is not universal; the general law is momentum conservation including fields.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Canon rows quoted; audit text is an
adaptation, not endorsed by the author.
```
