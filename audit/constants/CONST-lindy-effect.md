---
id: CONST-lindy-effect
canon_ref: "v5.1 Appendix D, Economic, Network & Social Laws, row 'Lindy Effect' (versions/v5.1/GFunnel-Methodology-v5.1.md line 2108)"
canon_label: "Lindy Effect"
diff_state: unobserved-claim
exclusion_diagnosis: n/a
claim_outcome: live-hypothesis
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix D (Fundamental Constants & Laws Registry), *Economic, Network & Social Laws*, line 2108:

> **Law:** Lindy Effect  
> **Statement:** Life expectancy ∝ current age (for non-perishable phenomena)  
> **Framework Role:** An idea, technology, or institution that has lasted X years can be expected to last another X. Per Layer I.G: the integration density a phenomenon has accumulated predicts its future persistence.

**Split (RUNBOOK rule 4).** *Factual core graded here:* for non-perishable things, expected remaining life ∝ current age; something that has lasted X years can be expected to last another X.

*Framework mapping (not graded; see Narrative stripped):* 'the integration density a phenomenon has accumulated predicts its future persistence.'

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Expected remaining life under a Pareto(α) lifetime law | t/(α−1): 2t at α=1.5, t at α=2, 0.5t at α=3 | exact given α | derived | audit/constants/appendix_d_checks.py | 2026-09-24 |
| Mathematical treatment (bibliographic record) | Eliazar, 'Lindy's Law', Physica A, 2017 | n/a | held-open | https://api.crossref.org/works/10.1016/j.physa.2017.05.077 | 2026-09-24 |

Proportionality holds for any Pareto lifetime; the 'another X' version needs α = 2 exactly. No empirical measurement of α for ideas, technologies or institutions was retrieved.

## Scientific Inquiry run

1. Question (precise): Is remaining life ∝ age, with ratio 1?
2. What an answer must look like: Measured lifetime distributions of non-perishables.
3. Falsifiability condition: Lifetime distributions that are not power-law, or α far from 2.
4. Variables: measurable / bounded / held open: Measurable: survival data. Bounded: none retrieved. Held open: α.
5. Test designed: Derive the ratio; look for data.
6. Data (unfiltered): Ratio = 1/(α−1); no data retrieved.
7. Variable Principle applied: α held open; canon fills it with 2.
8. Model update (Capsule: what the failed parts contribute): Re-word: 'remaining life ∝ age if lifetimes are power-law; the constant depends on the exponent'.
9. Documented: This file; appendix_d_checks.py section 5.
10. Next baseline: Open.

## Forcing Test

- Test A (Ground): Derived only.
- Test B (Uniqueness): Not unique (depends on α).
- Test C (Direction): n/a.
- Test D (Falsifiability): Falsifiable with survival data; untested here.
- **Outcome:** `live-hypothesis`.

## Anti-Operation (the gap this opens)

Canon does not define 'non-perishable'. The class of things the law applies to is open.

## Narrative stripped

Removed: 'integration density ... predicts its future persistence'. The Lindy effect is a property of a lifetime distribution; 'integration density' is not measured. Reality does not force it.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
