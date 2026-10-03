---
id: CONST-pareto-distribution
canon_ref: "v5.1 Appendix D, Economic, Network & Social Laws, row 'Pareto Distribution (Power Law)' (versions/v5.1/GFunnel-Methodology-v5.1.md line 2099)"
canon_label: "Pareto Distribution (Power Law)"
diff_state: conflict
exclusion_diagnosis: reached-conflicting
claim_outcome: forced-no
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix D (Fundamental Constants & Laws Registry), *Economic, Network & Social Laws*, line 2099:

> **Law:** Pareto Distribution (Power Law)  
> **Statement:** P(X > x) ∝ x^(-α)  
> **Framework Role:** Mathematical expression of the 80/20 Rule. Wealth, city size, word frequency, file size, network connectivity all follow power laws. Per Correspondence: same distribution, every social scale.

**Split (RUNBOOK rule 4).** *Factual core graded here:* P(X > x) ∝ x^(−α); wealth, city size, word frequency, file size and network connectivity all follow power laws.

*Framework mapping (not graded; see Narrative stripped):* 'Per Correspondence: same distribution, every social scale.'

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Networks with strongest evidence of scale-free (power-law) degree distribution | 4% of nearly 1000 networks | see paper | measured-single | https://arxiv.org/abs/1801.03400 (Broido & Clauset 2019) | 2026-09-24 |
| Networks with weakest-possible evidence | 52% | see paper | measured-single | https://arxiv.org/abs/1801.03400 | 2026-09-24 |
| Social networks | at best weakly scale-free | see paper | measured-single | https://arxiv.org/abs/1801.03400 | 2026-09-24 |
| 24 data sets conjectured to be power laws | some consistent; power law ruled out for others | see paper | measured-single | https://arxiv.org/abs/0706.1062 (Clauset, Shalizi, Newman 2009) | 2026-09-24 |

Both studies share an author and methods, so they are graded `measured-single`; they are large-sample tests, but not independent replications of each other.

## Scientific Inquiry run

1. Question (precise): Do the listed quantities all follow power laws?
2. What an answer must look like: Goodness-of-fit and likelihood-ratio tests per data set.
3. Falsifiability condition: Many data sets where the power law is rejected or an alternative (e.g. log-normal) fits better.
4. Variables: measurable / bounded / held open: Measurable: tail distributions. Bounded: per data set. Held open: which of canon's five examples pass.
5. Test designed: Use the large-corpus tests.
6. Data (unfiltered): Scale-free networks rare (4% strong); some of 24 classic data sets fail.
7. Variable Principle applied: 'All follow power laws' is filled by assumption; it is a per-data-set variable.
8. Model update (Capsule: what the failed parts contribute): Re-word: 'many heavy-tailed quantities are approximately power-law in their tails; network degree distributions mostly are not'.
9. Documented: This file.
10. Next baseline: Open.

## Forcing Test

- Test A (Ground): Grounded in large-sample tests.
- Test B (Uniqueness): Not unique: log-normal and others compete.
- Test C (Direction): n/a.
- Test D (Falsifiability): Tested; universality fails for networks.
- **Outcome:** `forced-no` for 'all follow power laws'.

## Anti-Operation (the gap this opens)

Canon uses power laws as evidence of Correspondence. If the distributions differ across domains, that evidence weakens; what distribution-level result would count for or against Correspondence is not stated.

## Narrative stripped

Removed: 'same distribution, every social scale'. The data show different distributions across domains. Reality does not force the mapping and partly contradicts it.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
