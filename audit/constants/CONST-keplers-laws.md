---
id: CONST-keplers-laws
canon_ref: v5.1 Appendix D, Dynamical Laws
canon_label: "Kepler's Three Laws of Planetary Motion"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Dynamical Laws*, row Kepler's Three Laws of Planetary Motion, Astronomy. **Text:** "Planets orbit in ellipses, sweep equal areas in equal times, and have orbital period² ∝ semi-major axis³. Per Correspondence: the same gravitational mechanics that holds an electron near a nucleus holds Earth near the Sun."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Mercury total perihelion precession (MESSENGER ranging, Park et al. 2017) | 575.3100″/century | ± 0.0015″/century | measured-single | https://api.crossref.org/works/10.3847/1538-3881/aa5be2 | 2026-09-24 |
| ratio of gravitational to Coulomb attraction, proton–electron (CODATA 2022 G, mₑ, mₚ, e, ε₀) | 4.408×10⁻⁴⁰ | dominated by G (2.2×10⁻⁵ rel.) | derived | audit/constants/check_law_derivations.py | 2026-09-24 |
| G, mₑ, mₚ, e, ε₀ inputs | CODATA 2022 | as published | measured-reproduced | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | 2026-09-24 |

Kepler's laws are the two-body Newtonian limit: ellipses precess under perturbations from other planets, solar oblateness (J₂) and general relativity, hence Mercury's 575″/century.

## Scientific Inquiry run
1. Question (precise): Does the law, as canon states it, match its measured form and domain of validity? And is the electron–Earth correspondence physically correct?
2. What an answer must look like: Measured deviation from closed ellipses; the force that binds an electron.
3. Falsifiability condition: Orbits exactly closed; or gravity binding the electron.
4. Variables: measurable / bounded / held open: Measured: perihelion precession; constants. Derived: force ratio.
5. Test designed: Literature fetch; `audit/constants/check_law_derivations.py` for the force ratio.
6. Data (unfiltered): Kepler's laws hold as the two-body limit; real orbits precess (Mercury 575.31″/century total). The role text's physics claim is wrong: an electron is bound to a nucleus by the electromagnetic force, which is 1/(4.4×10⁻⁴⁰) ≈ 2×10³⁹ times stronger than gravity for a proton–electron pair, and atomic states are quantum (no classical orbits; a classical orbiting charge would radiate and spiral in).
7. Variable Principle applied: No variable open.
8. Model update (Capsule: what the failed parts contribute): Laws survive as a limit; the Correspondence sentence is factually false and should be removed or rewritten.
9. Documented: this file.
10. Next baseline: Re-run on the next PDG edition (2026 Review of Particle Physics) or on the named experiment's next result (Phase 9).

## Forcing Test
- Test A (Ground): Measurement plus derivation.
- Test B (Uniqueness): One candidate (Newtonian two-body limit).
- Test C (Direction): Measurement → text. Reality is the authority (substrate item 1); the canonical wording is what is tested.
- Test D (Falsifiability): Falsifier fired for the Correspondence sentence (wrong force, wrong mechanics).
- **Outcome:** forced-fill (laws, as a limit); role claim forced-no

## Anti-Operation (the gap this opens)
Canon uses the atom–solar-system analogy (the 1913 Bohr/Rutherford picture) as a Correspondence example. The analogy fails on force (EM, not gravity) and on mechanics (quantum). A Correspondence example that survives measurement is the gap.

## Narrative stripped (if any)
Removed: "Per Correspondence:" — the mapping. The rest of that sentence is not interpretation but a false physical statement, graded below.

### Framework Role text — claim-by-claim (graded separately from the value)
| Role-text claim | Reality | Verdict |
| --- | --- | --- |
| Ellipses, equal areas, P² ∝ a³ | Two-body limit; orbits precess (Mercury 575.31″/cy) | accounted (limit) |
| Same gravitational mechanics holds an electron near a nucleus | Electron bound by EM (gravity 4.4×10⁻⁴⁰ as strong); quantum, not orbital | forced-no (factually wrong) |

**Role-text verdict:** laws correct as a limit; 'the same gravitational mechanics that holds an electron near a nucleus' is false.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Canon rows quoted; audit text is an
adaptation, not endorsed by the author.
```
