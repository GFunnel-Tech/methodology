---
id: CONST-sqrt-2
canon_ref: v5.1 Appendix D, Mathematical Constants
canon_label: "√2 — Diagonal of Unit Square"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Mathematical Constants*, row √2. **Value:** 1.41421356… **Framework Role:** "The first irrational number discovered (Pythagoreans). Geometric expression of the impossibility of perfect rational measurement of the simplest non-trivial figure. Per Gödel: a foretaste of incompleteness, three thousand years early."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| √2 (Decimal sqrt, 60 digits) | 1.41421356237309504880… | exact (defined) | derived | audit/constants/check_math_constants.py | 2026-09-24 |
| Pythagoras' dates (MacTutor) | born c. 570 BC, died c. 490 BC; discovery of irrationals 'certainly attributed to the Pythagoreans but … unlikely … Pythagoras himself' | 'about' | measured-single | https://mathshistory.st-andrews.ac.uk/Biographies/Pythagoras/ | 2026-09-24 |
| which magnitude was first shown incommensurable (SEP, Pythagoreanism) | no ancient source connects Hippasus or a specific figure to the discovery; von Fritz (1945) proposed the pentagon/dodecahedron — 'pure speculation' | n/a | held-open | https://plato.stanford.edu/entries/pythagoreanism/ | 2026-09-24 |
| von Fritz 1945, Ann. Math. 46:242 (bibliographic record) | argues incommensurability found via the regular pentagon (golden section), not √2 | n/a | measured-single | https://api.crossref.org/works/10.2307/1969021 | 2026-09-24 |
| Gödel's incompleteness paper (bibliographic record) | 1931 | exact | measured-reproduced | https://api.crossref.org/works/10.1007/BF01700692 | 2026-09-24 |
| years from Pythagoras' lifetime to 1931 | 2,420–2,500 | ± span of Pythagoras' lifetime | derived | audit/constants/check_math_constants.py | 2026-09-24 |

These values are defined or proven, not measured: the grade is `derived` and the derivation is the script. Every computed digit comes from `audit/constants/check_math_constants.py` (Python standard library, run 2026-09-24). The historical rows test the role text.

## Scientific Inquiry run
1. Question (precise): Is canon's √2 string correct, and are 'first irrational discovered (Pythagoreans)' and 'three thousand years early' supported?
2. What an answer must look like: Digits by computation; historical claims against scholarly sources; the year gap computed.
3. Falsifiability condition: Digit mismatch; a source establishing a different first irrational; a year gap outside ~3,000.
4. Variables: measurable / bounded / held open: Derived: digits; year gap. Measured (scholarship): Pythagorean attribution. Held open: which magnitude was first.
5. Test designed: `audit/constants/check_math_constants.py`: Decimal sqrt; year-gap check (Gödel 1931 minus Pythagoras' lifetime).
6. Data (unfiltered): Digits PASS. Year gap: 2,420–2,500 years, not 3,000 → the script's check FAILS. Attribution to the Pythagorean school: supported (MacTutor). 'First irrational = √2': not established — SEP says no ancient source ties the discovery to a specific figure; von Fritz argued for the pentagon.
7. Variable Principle applied: Which irrational came first is held open, not filled with the textbook √2 story.
8. Model update (Capsule: what the failed parts contribute): The value survives. The role text contributes two corrections: the gap is ~2,400–2,500 years; √2 as 'first' is traditional, not established.
9. Documented: this file; `audit/constants/check_math_constants.py`.
10. Next baseline: No re-run needed for the value (a definition does not drift). Re-audit only if canon's wording of the role text changes (Phase 9).

## Forcing Test
- Test A (Ground): Within-system: a defined mathematical object, checked by explicit computation (no measurement involved).
- Test B (Uniqueness): One candidate for the value.
- Test C (Direction): Definition → value. The computation runs from the definition to the digits; canon's string is the thing tested.
- Test D (Falsifiability): Falsifier stated; did not fire for the value; fired for 'three thousand years'.
- **Outcome:** forced-fill (value); role text: 'three thousand years' contradicted by computation; 'first irrational' held open

## Anti-Operation (the gap this opens)
The historical order of incommensurability discoveries (√2 vs the pentagon's diagonal/side, √5) is unresolved in the scholarship. That is the open edge.

## Narrative stripped (if any)
Removed: "Geometric expression of the impossibility of perfect rational measurement …" (a correct mathematical fact dressed in interpretive wording — kept as: the diagonal and side of a square are incommensurable) and "Per Gödel: a foretaste of incompleteness" (analogy; irrationality and incompleteness are different theorems — reality does not force the link).

### Framework Role text — claim-by-claim (graded separately from the value)
| Role-text claim | Reality | Verdict |
| --- | --- | --- |
| First irrational discovered | Attributed to the Pythagoreans; which magnitude first is unknown (SEP; von Fritz proposes pentagon) | held open |
| Three thousand years before Gödel | 2,420–2,500 years (computed) | contradicted (numeric error ~20%) |

**Role-text verdict:** value correct; 'three thousand years' is wrong (≈2,400–2,500); 'first irrational' is traditional, not established.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Canon rows quoted; audit text is an
adaptation, not endorsed by the author.
```
