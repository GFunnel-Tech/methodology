---
id: CONST-zipf-law
canon_ref: "v5.1 Appendix D, Economic, Network & Social Laws, row 'Zipf’s Law' (versions/v5.1/GFunnel-Methodology-v5.1.md line 2100)"
canon_label: "Zipf’s Law"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix D (Fundamental Constants & Laws Registry), *Economic, Network & Social Laws*, line 2100:

> **Law:** Zipf’s Law  
> **Statement:** Frequency ∝ 1/rank  
> **Framework Role:** In any large corpus, frequency of nth-most-common word ≈ frequency of most-common / n. Linguistic application of Pareto. Per Domain 6: the structural signature of language self-organization.

**Split (RUNBOOK rule 4).** *Factual core graded here:* in a large corpus, word frequency ∝ 1/rank (approximately).

*Framework mapping (not graded; see Narrative stripped):* 'Linguistic application of Pareto. Per Domain 6: the structural signature of language self-organization.'

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Rank–frequency log–log slope, ranks 1–1000, Moby-Dick | −1.072 | R² = 0.9949 (OLS) | measured-single | https://www.gutenberg.org/cache/epub/2701/pg2701.txt (computed by audit/constants/appendix_d_checks.py) | 2026-09-24 |
| f(1)/f(10), f(1)/f(100), same text | 6.83, 51.37 (Zipf predicts 10, 100) | single text | measured-single | https://www.gutenberg.org/cache/epub/2701/pg2701.txt | 2026-09-24 |
| Status in the literature | language 'approximately follows' Zipf's law, with reliable structure beyond it; no account explains all facts | review | measured-reproduced | https://pubmed.ncbi.nlm.nih.gov/24664880/ (Piantadosi 2014) | 2026-09-24 |

The slope near −1 is consistent with Zipf; the ratio test shows the top ranks are flatter than exact 1/rank.

## Scientific Inquiry run

1. Question (precise): Does word frequency fall as 1/rank?
2. What an answer must look like: A rank–frequency slope near −1.
3. Falsifiability condition: A slope far from −1 in large corpora.
4. Variables: measurable / bounded / held open: Measurable: counts. Bounded: slope ≈ −1. Held open: the mechanism.
5. Test designed: Fit one public-domain corpus; check the review.
6. Data (unfiltered): Slope −1.07; review confirms approximate law with structure.
7. Variable Principle applied: Approximate law accepted; mechanism held open (Piantadosi).
8. Model update (Capsule: what the failed parts contribute): Keep 'approximately'.
9. Documented: This file.
10. Next baseline: Integrated.

## Forcing Test

- Test A (Ground): Grounded.
- Test B (Uniqueness): Approximately unique exponent (~1).
- Test C (Direction): n/a.
- Test D (Falsifiability): Passes.
- **Outcome:** `forced-fill` (approximate).

## Anti-Operation (the gap this opens)

Piantadosi notes no mechanism is established. Canon's 'signature of language self-organization' names a mechanism the data do not select.

## Narrative stripped

Removed: 'the structural signature of language self-organization'. The mechanism of Zipf's law is open; Piantadosi (2014) reviews many competing accounts, none established. Reality does not force the mapping.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
