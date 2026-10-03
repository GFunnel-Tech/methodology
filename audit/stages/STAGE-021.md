---
id: STAGE-021
canon_ref: v5.1 Appendix A, Stage 21
canon_label: "Electron Transport Chain"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix A, table "Stages 1–22", row 21 (line 1759):

> | 21 | Electron Transport Chain | NADH and FADH₂ donate electrons. Cascade through Complexes I → III → IV pumps protons. Polarity created. Same logic as alkaline vents 4 Bya, now internalized. |

**Factual core (graded):** (a) NADH and FAD-linked carriers donate electrons to the chain; (b) complexes I, III and IV pump protons; (c) a proton gradient results.
**Separate scientific clause (graded in STAGE-013, not here):** "Same logic as alkaline vents 4 Bya, now internalized" — an evolutionary-lineage claim with a date; a live hypothesis.
**Framework mapping (not graded):** "Polarity created."

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Proton-pumping complexes of the mitochondrial respiratory chain | complexes I, III and IV pump protons; complex II (succinate dehydrogenase) does not, but supplies reduced ubiquinone | n/a | measured-reproduced | doi:10.1007/978-981-10-7757-9_7 (PubMed 29464561) and independently doi:10.1016/j.cub.2022.05.006 (PubMed 35728541), both via https://www.ebi.ac.uk/europepmc/webservices/rest/search | 2026-09-24 |
| Electron donor to complex II side of the chain (KEGG R02164) | succinate → fumarate reduces quinone to quinol | exact (curated) | measured-reproduced | https://rest.kegg.jp/get/R02164 | 2026-09-24 |
| Non-pumping alternative NADH dehydrogenase and mitochondrial glycerol-phosphate dehydrogenase (yeast D. hansenii) | present; "lack proton pump activity" | n/a | measured-single | doi:10.1016/j.bbabio.2013.07.011 (PubMed 23933018), via Europe PMC REST search | 2026-09-24 |
| Complex I proton pumping driven by quinone reduction (mechanism study) | coupling over ~200 Å; Asp→Asn mutation inhibits Q-reductase activity by 75% | as published | measured-single | doi:10.1073/pnas.1503761112 (PubMed 26330610), via https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=26330610 | 2026-09-24 |
| Cytochrome c oxidase (complex IV) reduces O2 to water and pumps protons | observed | n/a | measured-single | doi:10.1016/j.bbabio.2015.04.007 (PubMed 25896562), via efetch id=25896562 | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): In the mitochondrial respiratory chain, which complexes pump protons, and do NADH and FAD-linked carriers feed electrons into it?
2. What an answer must look like: biochemical/structural consensus on pumping sites; reaction stoichiometry for electron entry.
3. Falsifiability condition: falsified if complex II pumped protons, or if any of I, III, IV did not.
4. Variables: measurable: pumping per complex; electron entry points. Held open: the alkaline-vent lineage clause and its date (see STAGE-013).
5. Test designed: fetch reviews and primary studies on respiratory complexes; fetch KEGG entry for complex II reaction.
6. Data (unfiltered): table above. I, III, IV pump; II does not. Some organisms add non-pumping NADH dehydrogenases, which changes the proton yield per NADH.
7. Variable Principle applied: (a)–(c) measured. Lineage clause held open.
8. Model update (Capsule): accounted. Refinement: canon's "Complexes I → III → IV" is correct for NADH; FAD-linked electrons from succinate enter at complex II (non-pumping) and join at quinone. The chain described is the mitochondrial one; bacterial and yeast chains vary (non-pumping branches).
9. Documented: this file.
10. Next baseline: STAGE-022 uses the pumping stoichiometry via measured P/O ratios.

## Forcing Test
- Test A (Ground): Grounded in structural and biochemical measurements.
- Test B (Uniqueness): One assignment survives (I, III, IV pump; II does not).
- Test C (Direction): Forced: electrons flow from NADH/succinate to O2; protons are pumped out of the matrix.
- Test D (Falsifiability): Yes (step 3).
- **Outcome:** forced-fill (for the mitochondrial ETC core). The "alkaline vents 4 Bya" clause is a live hypothesis graded in STAGE-013 and is not covered by this outcome.

## Anti-Operation (the gap this opens)
The row embeds a live hypothesis with a date ("alkaline vents 4 Bya") inside a measured stage without marking it held open. LUCA's inferred age (4.09–4.33 Ga; STAGE-014) makes the date and the lineage direction both open. Also opened: non-pumping branches (alternative NADH dehydrogenases) make "the" ETC organism-specific, so a single proton yield is not universal.

## Narrative stripped (if any)
- "Polarity created" maps the Hermetic principle of Polarity onto the proton gradient. Reality neither forces nor contradicts it.
- "now internalized" is part of the vent-lineage hypothesis (STAGE-013). The label "Electron Transport Chain" is observational; no new label proposed.
