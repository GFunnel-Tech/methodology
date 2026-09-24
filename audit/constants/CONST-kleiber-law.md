---
id: CONST-kleiber-law
canon_ref: "v5.1 Appendix D, Biological & Scaling Laws, row 'Kleiber’s Law' (versions/v5.1/GFunnel-Methodology-v5.1.md line 2078)"
canon_label: "Kleiber’s Law"
diff_state: conflict
exclusion_diagnosis: reached-conflicting
claim_outcome: forced-no
intake_result: adjusted
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix D (Fundamental Constants & Laws Registry), *Biological & Scaling Laws*, line 2078:

> **Law:** Kleiber’s Law  
> **Statement / Value:** Metabolic rate ∝ mass^(3/4)  
> **Framework Role:** Across nearly all biological scales — from bacteria to whales. Per Correspondence: the same scaling law governs living systems across 27 orders of magnitude.

**Split (RUNBOOK rule 4).** *Factual core graded here:* metabolic rate ∝ mass^(3/4) across nearly all biological scales, from bacteria to whales, over 27 orders of magnitude.

*Framework mapping (not graded; see Narrative stripped):* 'Per Correspondence: the same scaling law governs living systems.'

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Whole-organism metabolic-rate exponent α, heterotrophic prokaryotes (active / inactive) | 1.7 / 2.0 | RMA ± SE in paper | measured-single | https://pubmed.ncbi.nlm.nih.gov/20616006/ ; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC2919978/ | 2026-09-24 |
| Same, protists (active / inactive) | 1.0 / 1.1 | RMA ± SE in paper | measured-single | https://pubmed.ncbi.nlm.nih.gov/20616006/ | 2026-09-24 |
| Same, metazoans (active / inactive) | 0.76 / 0.79 | RMA ± SE in paper | measured-single | https://pubmed.ncbi.nlm.nih.gov/20616006/ | 2026-09-24 |
| Mammalian BMR exponent (619 species, 19 orders, 5 orders of magnitude in M; corrected for T_b, digestive state, phylogeny) | 2/3; 'no support' for 3/4 | see paper | measured-reproduced | https://pubmed.ncbi.nlm.nih.gov/12637681/ | 2026-09-24 |
| Mammal/bird BMR re-analysis of Heusner, Kleiber, Brody et al. data | little evidence for rejecting 2/3 in favour of 3/4 | see paper | measured-reproduced | https://arxiv.org/abs/physics/0007096 (Dodds, Rothman, Weitz) | 2026-09-24 |
| Shape of log BMR vs log M (mammals) | convex curvature; not a pure power law | see paper | measured-single | https://pubmed.ncbi.nlm.nih.gov/20360740/ | 2026-09-24 |
| Claimed span of 3/4 scaling | 27 orders of magnitude (organisms, cells, mitochondria, enzyme molecules) | model-based | derived | https://pubmed.ncbi.nlm.nih.gov/11875197/ | 2026-09-24 |

Two independent re-analyses (White & Seymour 2003; Dodds et al. 2001) fail to support 3/4 for mammals, hence `measured-reproduced` for 'exponent not established as 3/4 in mammals'. DeLong et al. 2010 state directly that 'Kleiber's 3/4 power scaling law does not apply universally across organisms'.

## Scientific Inquiry run

1. Question (precise): Is metabolic rate ∝ M^(3/4) across bacteria to whales?
2. What an answer must look like: Fitted exponents by taxon, with uncertainty.
3. Falsifiability condition: Exponents that differ from 3/4 beyond error in some major group.
4. Variables: measurable / bounded / held open: Measurable: α per taxon. Bounded: metazoan α near 0.67–0.79 depending on analysis. Held open: whether any single mechanism sets α.
5. Test designed: Collect independent fits across prokaryotes, protists, metazoans and mammals.
6. Data (unfiltered): Prokaryotes 1.7–2.0; protists 1.0–1.1; metazoans 0.76–0.79; mammals 2/3 (White & Seymour) with curvature (Kolokotrones). The 27-orders claim is a model-based argument (West et al. 2002).
7. Variable Principle applied: The single value 3/4 is not filled across life. α is a taxon-dependent variable.
8. Model update (Capsule: what the failed parts contribute): Adjust: 'Within metazoans, metabolic rate scales roughly as M^0.67–0.79 (contested); the exponent differs in protists (~1) and prokaryotes (>1).' The 'bacteria to whales' clause fails.
9. Documented: This file.
10. Next baseline: Adjusted form carried forward.

## Forcing Test

- Test A (Ground): Grounded in reproduced fits.
- Test B (Uniqueness): 3/4 is not unique even within mammals (2/3 fits).
- Test C (Direction): Direction: superlinear in prokaryotes, the opposite of canon's universal sublinear law.
- Test D (Falsifiability): Tested and failed as a universal law.
- **Outcome:** `forced-no` for 'one 3/4 law across all life'; the metazoan exponent remains a live variable.

## Anti-Operation (the gap this opens)

Canon does not say which exponent it would accept as confirming 'Correspondence'. If any exponent counts, the law cannot test Correspondence at all. That criterion is held open.

## Narrative stripped

Removed: 'Per Correspondence: the same scaling law governs living systems across 27 orders of magnitude.' The measured exponents differ between prokaryotes, protists and metazoans, so reality does not force one scaling law across life. The factual part of this role text is graded above as failing.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
