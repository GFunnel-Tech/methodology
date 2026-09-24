---
id: CONST-pareto-principle
canon_ref: "v5.1 Appendix D, Economic, Network & Social Laws, row 'Pareto Principle (80/20 Rule)' (versions/v5.1/GFunnel-Methodology-v5.1.md line 2098)"
canon_label: "Pareto Principle (80/20 Rule)"
diff_state: conflict
exclusion_diagnosis: reached-conflicting
claim_outcome: forced-no
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix D (Fundamental Constants & Laws Registry), *Economic, Network & Social Laws*, line 2098:

> **Law:** Pareto Principle (80/20 Rule)  
> **Statement:** 80% of effects come from 20% of causes  
> **Framework Role:** Vilfredo Pareto, 1896. Per Cause and Effect: not random — structural. Identifying the 20% is the highest-leverage application of the algorithm.

**Split (RUNBOOK rule 4).** *Factual core graded here:* 80% of effects come from 20% of causes (attributed to Pareto, 1896), as a structural law.

*Framework mapping (not graded; see Narrative stripped):* 'Per Cause and Effect: not random — structural. Identifying the 20% is the highest-leverage application of the algorithm.'

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Share held by top 20% under a Pareto distribution, α = 1.5 / 2 / 3 | 58.5% / 44.7% / 34.2% | exact given α | derived | audit/constants/appendix_d_checks.py | 2026-09-24 |
| Pareto α that gives exactly 80/20 | 1.161 | exact | derived | audit/constants/appendix_d_checks.py | 2026-09-24 |
| Share of word tokens from the top 20% of word types, Moby-Dick (219 065 tokens, 16 957 types) | 88.2% | single text | measured-single | https://www.gutenberg.org/cache/epub/2701/pg2701.txt (computed by audit/constants/appendix_d_checks.py) | 2026-09-24 |
| Power-law behaviour in 24 empirical data sets | consistent for some, ruled out for others | see paper | measured-single | https://arxiv.org/abs/0706.1062 | 2026-09-24 |

The 80/20 split is a property of one exponent, not a law. The Moby-Dick split is not 80/20. Pareto's 1896 attribution was not checked in this run (primary text not retrieved) and is held open.

## Scientific Inquiry run

1. Question (precise): Is '80% of effects from 20% of causes' a general law?
2. What an answer must look like: Top-20% shares across distributions and data.
3. Falsifiability condition: Shares that differ materially from 80% in real heavy-tailed data.
4. Variables: measurable / bounded / held open: Measurable: concentration shares. Bounded: depends on α. Held open: attribution to Pareto 1896.
5. Test designed: Derive the share as a function of α; measure one corpus.
6. Data (unfiltered): Share = 0.2^(1−1/α): 80% only at α ≈ 1.16. Moby-Dick: 88.2%.
7. Variable Principle applied: The ratio is a variable (a function of α), not a constant; canon fills it with 80/20.
8. Model update (Capsule: what the failed parts contribute): Re-word: 'a small fraction of causes often accounts for a large fraction of effects; the split depends on the distribution'.
9. Documented: This file; appendix_d_checks.py sections 4 and 6.
10. Next baseline: Open until the re-wording is adopted.

## Forcing Test

- Test A (Ground): Derived plus single measurement.
- Test B (Uniqueness): Not unique: every α gives a different split.
- Test C (Direction): n/a.
- Test D (Falsifiability): Tested; a fixed 80/20 fails.
- **Outcome:** `forced-no` for 80/20 as a law; it is a rule of thumb.

## Anti-Operation (the gap this opens)

Canon does not say how to find 'the 20%' when the distribution's exponent is unknown. Estimating α from data is the real work, and the registry is silent on it (see Clauset et al. 2009).

## Narrative stripped

Removed: 'Per Cause and Effect: not random — structural' and 'highest-leverage application of the algorithm'. Heavy tails arise from many mechanisms, some random (e.g. multiplicative noise). Reality does not force 'structural, not random'.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
