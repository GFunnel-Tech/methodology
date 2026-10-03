---
id: CONST-hardy-weinberg-equilibrium
canon_ref: v5.1 Appendix D, Dynamical Laws
canon_label: "Hardy-Weinberg Equilibrium"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Dynamical Laws*, row Hardy-Weinberg Equilibrium, Population Genetics. **Text:** "Allele frequencies remain constant absent specific evolutionary pressures. The genetic baseline against which evolution is measured."

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Hardy 1908, Science 28:49–50, 'Mendelian Proportions in a Mixed Population' (bibliographic record) | original statement | n/a | derived | https://api.crossref.org/works/10.1126/science.28.706.49 | 2026-09-24 |
| one generation of random mating from (AA, Aa, aa) = (0.5, 0.1, 0.4) | → (0.3025, 0.495, 0.2025); allele frequency p = 0.550 unchanged | exact | derived | audit/constants/check_law_derivations.py | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): Is canon's statement of Hardy–Weinberg correct and complete?
2. What an answer must look like: The derivation and its assumptions.
3. Falsifiability condition: Allele frequencies changing under the model's assumptions.
4. Variables: measurable / bounded / held open: Derived only (a mathematical null model).
5. Test designed: `audit/constants/check_law_derivations.py`: one generation of random mating.
6. Data (unfiltered): Allele frequency conserved; genotype frequencies reach p², 2pq, q² after one generation. Assumptions: random mating, infinite (very large) population, no selection, mutation or migration. Canon's 'specific evolutionary pressures' covers selection/mutation/migration but omits random mating and genetic drift (finite population), and omits the genotype-proportion half of the result.
7. Variable Principle applied: No variable open.
8. Model update (Capsule: what the failed parts contribute): Statement survives; assumptions incomplete.
9. Documented: this file.
10. Next baseline: No re-run needed for the value (a definition does not drift). Re-audit only if canon's wording of the role text changes (Phase 9).

## Forcing Test
- Test A (Ground): Mathematical derivation.
- Test B (Uniqueness): One candidate.
- Test C (Direction): Assumptions → result.
- Test D (Falsifiability): Falsifier stated; did not fire.
- **Outcome:** forced-fill (as a null model)

## Anti-Operation (the gap this opens)
Real populations are finite; drift alone changes allele frequencies. Which deviations from HW in a real dataset are due to drift vs selection is the empirical gap canon's one-line statement does not address.

## Narrative stripped (if any)
None beyond the row; 'the genetic baseline against which evolution is measured' is a fair description of its use as a null model.

### Framework Role text — claim-by-claim (graded separately from the value)
| Role-text claim | Reality | Verdict |
| --- | --- | --- |
| Allele frequencies constant absent pressures | Correct given random mating + infinite population | accounted (assumptions incomplete) |

**Role-text verdict:** correct; assumptions incomplete.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Canon rows quoted; audit text is an
adaptation, not endorsed by the author.
```
