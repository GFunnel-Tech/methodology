---
id: CONST-moore-law
canon_ref: "v5.1 Appendix D, Economic, Network & Social Laws, row 'Moore’s Law (empirical, slowing)' (versions/v5.1/GFunnel-Methodology-v5.1.md line 2103)"
canon_label: "Moore’s Law (empirical, slowing)"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix D (Fundamental Constants & Laws Registry), *Economic, Network & Social Laws*, line 2103:

> **Law:** Moore’s Law (empirical, slowing)  
> **Statement:** Transistor density doubles ~every 2 years  
> **Framework Role:** Held for ~50 years before physical limits began binding. Per Process Density: the empirical demonstration of compounding density at one specific substrate.

**Split (RUNBOOK rule 4).** *Factual core graded here:* transistor density doubles ~every 2 years; held ~50 years; now slowing.

*Framework mapping (not graded; see Narrative stripped):* 'Per Process Density: the empirical demonstration of compounding density at one specific substrate.'

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Doubling time of transistors per microprocessor, 1971–2021 (99 chips) | 1.99 yr | OLS R² = 0.980 | measured-single | https://raw.githubusercontent.com/karlrupp/microprocessor-trend-data/master/50yrs/transistors.dat (fit by audit/constants/appendix_d_checks.py) | 2026-09-24 |
| Same, 1990–2005 / 2005–2022 / 2010–2022 | 1.84 / 2.01 / 2.06 yr | R² 0.91 / 0.92 / 0.89 | measured-single | https://raw.githubusercontent.com/karlrupp/microprocessor-trend-data/master/50yrs/transistors.dat | 2026-09-24 |
| Moore's 1965 paper (bibliographic record) | 'Cramming more components onto integrated circuits', Electronics 38(8) | n/a | derived | https://api.crossref.org/works/10.1109/N-SSC.2006.4785860 | 2026-09-24 |
| Moore-type exponential improvement vs Wright's law across 62 technologies | Moore's law 'not far behind' Wright's in hindcasts | see paper | measured-reproduced | https://pubmed.ncbi.nlm.nih.gov/23468837/ | 2026-09-24 |

Rupp's data are transistor *count per chip*, not density. In count terms, no slowing is visible through 2021 (doubling 2.0–2.1 yr). Density (per mm²) was not fetched and is held open.

## Scientific Inquiry run

1. Question (precise): Has transistor count/density doubled ~every 2 years, and has it slowed?
2. What an answer must look like: Doubling times by era.
3. Falsifiability condition: A doubling time far from 2 years, or no slowing when canon says slowing.
4. Variables: measurable / bounded / held open: Measurable: transistor counts. Bounded: 1.8–2.4 yr by era. Held open: density; future trend.
5. Test designed: Fit log₂(count) vs year by era.
6. Data (unfiltered): 1.99 yr overall; 2.01 (2005–22) and 2.06 (2010–22).
7. Variable Principle applied: 'Slowing' is not visible in count data; density held open. Canon's 'slowing' is not filled from this data either way.
8. Model update (Capsule: what the failed parts contribute): State the measured quantity (count per chip) and hold 'slowing' open pending density data.
9. Documented: This file; appendix_d_checks.py section 7.
10. Next baseline: Open on the 'slowing' clause.

## Forcing Test

- Test A (Ground): Grounded in data.
- Test B (Uniqueness): One historical rate (~2 yr).
- Test C (Direction): n/a.
- Test D (Falsifiability): Passes for the rate; the slowing clause is untested here.
- **Outcome:** `forced-fill` for the historical ~2-year doubling of count per chip.

## Anti-Operation (the gap this opens)

Count per chip can keep doubling through larger dies and multi-die packages while density or cost per transistor behaves differently. Which quantity canon means is open.

## Narrative stripped

Removed: 'the empirical demonstration of compounding density'. The data show compounding count per chip; reading this as 'Process Density' is interpretation. Reality does not force it.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
