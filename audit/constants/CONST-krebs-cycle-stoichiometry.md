---
id: CONST-krebs-cycle-stoichiometry
canon_ref: "v5.1 Appendix D, Biological & Scaling Laws, row 'Krebs Cycle Stoichiometry' (versions/v5.1/GFunnel-Methodology-v5.1.md line 2081)"
canon_label: "Krebs Cycle Stoichiometry"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix D (Fundamental Constants & Laws Registry), *Biological & Scaling Laws*, line 2081:

> **Law:** Krebs Cycle Stoichiometry  
> **Statement / Value:** 1 acetyl-CoA → 3 NADH + 1 FADH₂ + 1 GTP + 2 CO₂  
> **Framework Role:** The exact accounting of energy capture in cellular respiration. Per Stage 20-22 of Appendix A: the algorithm at biochemical scale.

**Split (RUNBOOK rule 4).** *Factual core graded here:* one turn of the citric acid cycle converts one acetyl-CoA into 3 NADH + 1 FADH₂ + 1 GTP + 2 CO₂.

*Framework mapping (not graded; see Narrative stripped):* 'Per Stage 20-22 of Appendix A: the algorithm at biochemical scale.'

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| NAD⁺-reducing steps per turn (isocitrate DH R00709, 2-oxoglutarate DH R08549, malate DH R00342) | 3 NADH | exact (stoichiometry) | measured-reproduced | https://rest.kegg.jp/get/M00009 | 2026-09-24 |
| CO₂-releasing steps per turn (R00709, R08549) | 2 CO₂ | exact | measured-reproduced | https://rest.kegg.jp/get/R00709 ; https://rest.kegg.jp/get/R08549 | 2026-09-24 |
| Succinate dehydrogenase acceptor (R02164) | ubiquinone → ubiquinol (FAD is the enzyme-bound cofactor) | n/a | measured-reproduced | https://rest.kegg.jp/get/R02164 | 2026-09-24 |
| Succinyl-CoA synthetase nucleotide | ADP-forming (R00405) and GDP-forming (R00432) forms both exist | n/a | measured-reproduced | https://rest.kegg.jp/get/R00405 ; https://rest.kegg.jp/get/R00432 | 2026-09-24 |

Counts are read from KEGG reaction equations (C00003 NAD⁺ → C00004 NADH; C00011 CO₂).

## Scientific Inquiry run

1. Question (precise): Is the per-turn stoichiometry 3 NADH + 1 FADH₂ + 1 GTP + 2 CO₂?
2. What an answer must look like: Counts from reaction equations.
3. Falsifiability condition: A count that differs.
4. Variables: measurable / bounded / held open: Measurable: stoichiometric coefficients. Bounded: n/a. Held open: none.
5. Test designed: Count from KEGG reactions of module M00009.
6. Data (unfiltered): 3 NADH, 2 CO₂, one quinone reduction via the FAD-containing succinate DH, one GTP *or* ATP depending on enzyme form.
7. Variable Principle applied: No variable filled.
8. Model update (Capsule: what the failed parts contribute): Optional precision: 'FADH₂' is textbook shorthand (the electrons pass to ubiquinone); 'GTP' is 'GTP or ATP'.
9. Documented: This file.
10. Next baseline: Integrated.

## Forcing Test

- Test A (Ground): Grounded in reaction stoichiometry.
- Test B (Uniqueness): Unique.
- Test C (Direction): n/a.
- Test D (Falsifiability): Passes.
- **Outcome:** `forced-fill`.

## Anti-Operation (the gap this opens)

Canon's 'exact accounting of energy capture' stops at carriers; the ATP each carrier yields depends on P/O ratios, which are measured, not exact (see CONST-atp-yield-per-glucose).

## Narrative stripped

Removed: 'the algorithm at biochemical scale'. The stoichiometry is chemistry; reading it as DETECT→PROCESS→RESPOND is interpretation. Reality does not force it.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
