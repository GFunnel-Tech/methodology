---
id: CONST-game-of-life-rules
canon_ref: v5.1 Appendix D, Mathematical Constants
canon_label: "Conway's Game of Life Rules — Cellular Automaton"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Mathematical Constants*, row Conway's Game of Life Rules. **Value:** 3 rules. **Framework Role:** "Live cell with 2 or 3 live neighbors survives. Dead cell with exactly 3 live neighbors becomes alive. Otherwise dies/stays dead. Per Process Density (Layer III): three rules at sufficient density produce infinite emergent complexity, including self-replicating Turing-complete computation. Proof by example that complexity emerges from minimal rules."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| canon's rules (B3/S23) reproduce the blinker (period 2), block (still life), glider (translates (1,1) per 4 generations) | all three PASS | exact | derived | audit/constants/check_math_constants.py | 2026-09-24 |
| Turing completeness of Life ('There is a universal computer with finitely many alive cells', Conway, Winning Ways 1982) | theorem | n/a | derived | https://esolangs.org/wiki/Game_of_Life | 2026-09-24 |
| first self-constructing (self-replicating) pattern: Gemini, A. J. Wade | 2010 | n/a | measured-single | http://b3s23life.blogspot.com/2013/01/replicator-redux.html | 2026-09-24 |
| original publication of the rules (Gardner, Sci. Am. 223:120–123) | October 1970 | n/a | measured-reproduced | https://api.crossref.org/works/10.1038/scientificamerican1070-120 | 2026-09-24 |

These values are defined or proven, not measured: the grade is `derived` and the derivation is the script. Every computed digit comes from `audit/constants/check_math_constants.py` (Python standard library, run 2026-09-24).

## Scientific Inquiry run
1. Question (precise): Are the stated rules the Life rules, and are 'Turing-complete' and 'self-replicating' established?
2. What an answer must look like: A simulation with canon's rules reproducing known patterns; a citation for universality; a citation for a self-replicator.
3. Falsifiability condition: Canon's rules fail to reproduce standard Life patterns; no universality proof; no self-replicator.
4. Variables: measurable / bounded / held open: Derived: rule behaviour; universality (theorem). Measured (constructed artefact): Gemini. Held open: none.
5. Test designed: `audit/constants/check_math_constants.py`: set-based Life step with canon's survive {2,3} / birth {3}.
6. Data (unfiltered): Rules PASS (blinker, block, glider). Universality: theorem attributed to Conway (Winning Ways, 1982). Self-construction: Gemini (Wade, 2010) — 'self-constructing circuitry was no longer just a theoretical possibility but an accomplished fact'. 'Three rules' is a counting convention (usually stated as two: B3, S23). 'At sufficient density' is not a parameter of Life; 'infinite emergent complexity' is not a defined quantity — Turing-completeness means unbounded computation is possible, and consequently many long-run questions about patterns are undecidable.
7. Variable Principle applied: No variable open for the rules. 'Infinite complexity' is held as unquantified.
8. Model update (Capsule: what the failed parts contribute): Rules and headline results survive. The Process-Density mapping and 'infinite complexity' are interpretation.
9. Documented: this file; `audit/constants/check_math_constants.py`.
10. Next baseline: No re-run needed for the value (a definition does not drift). Re-audit only if canon's wording of the role text changes (Phase 9).

## Forcing Test
- Test A (Ground): Within-system: a defined mathematical object, checked by explicit computation (no measurement involved).
- Test B (Uniqueness): One candidate (B3/S23).
- Test C (Direction): Definition → value. The computation runs from the definition to the digits; canon's string is the thing tested.
- Test D (Falsifiability): Falsifier stated; did not fire.
- **Outcome:** forced-fill (rules and universality); 'infinite complexity' ungraded (undefined)

## Anti-Operation (the gap this opens)
Canon offers Life as 'proof by example that complexity emerges from minimal rules' but gives no complexity measure. Most 2-state outer-totalistic rules do not produce universality; which property of B3/S23 does is the open edge.

## Narrative stripped (if any)
Removed: "Per Process Density (Layer III): three rules at sufficient density …" — framework mapping; density is not a parameter of the rule. "Proof by example that complexity emerges from minimal rules" is an existence statement that the universality theorem does support, provided 'complexity' is read as 'universal computation'.

### Framework Role text — claim-by-claim (graded separately from the value)
| Role-text claim | Reality | Verdict |
| --- | --- | --- |
| Rules as stated | B3/S23; verified by simulation | accounted |
| Turing-complete | Theorem (Conway 1982) | accounted |
| Self-replicating | Gemini (Wade 2010) | accounted |
| Infinite emergent complexity | Unbounded computation possible; 'infinite complexity' undefined | over-stated wording |

**Role-text verdict:** factually correct; 'infinite complexity' and 'sufficient density' are unquantified.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Canon rows quoted; audit text is an
adaptation, not endorsed by the author.
```
