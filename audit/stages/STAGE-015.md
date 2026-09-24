---
id: STAGE-015
canon_ref: v5.1 Appendix A, Stage 15
canon_label: "Glycolysis"
diff_state: unobserved-claim
exclusion_diagnosis: n/a
claim_outcome: live-hypothesis
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix A, table "Stages 1–22", row 15 (line 1753):

> | 15 | Glycolysis | Most ancient metabolic pathway. Glucose split anaerobically. Universal across nearly all life. |

**Factual core (graded):** (a) glycolysis splits glucose without oxygen; (b) glycolysis is the most ancient metabolic pathway; (c) it is universal across nearly all life.
**Framework mapping (not graded):** none beyond its place in the stage sequence.

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Reaction equations, Embden–Meyerhof glycolysis (KEGG module M00001): hexokinase R01786 and phosphofructokinase R04779 consume ATP; GAPDH R01061 reduces NAD+; phosphoglycerate kinase R01512 and pyruvate kinase R00200 form ATP; no O2 in any step | as listed | exact (curated stoichiometry) | measured-reproduced | https://rest.kegg.jp/get/M00001 ; https://rest.kegg.jp/get/R01786 ; /R04779 ; /R01061 ; /R01512 ; /R00200 | 2026-09-24 |
| Net ATP and NADH per glucose via EMP glycolysis (derivation: −2 ATP at R01786+R04779; +2 ATP at R01512 ×2 trioses; +2 ATP at R00200 ×2; +2 NADH at R01061 ×2) | net 2 ATP, 2 NADH | exact under the pathway stoichiometry | derived | derived from the KEGG entries above | 2026-09-24 |
| Glycolysis variants in Archaea | Archaea use modified EMP and Entner–Doudoroff variants; many "classical" pathways absent | n/a (review) | derived | doi:10.1128/MMBR.00041-13 (PubMed 24600042), via https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=24600042 | 2026-09-24 |
| Distribution of bifunctional FBP aldolase/phosphatase | present in virtually all archaeal groups and deeply branching bacteria; authors propose gluconeogenesis preceded glycolysis | n/a | measured-single | doi:10.1038/nature08884 (PubMed 20348906), via efetch id=20348906 | 2026-09-24 |
| Non-enzymatic glycolysis-like reactions in an Archean-ocean mimetic, Fe(II)-dependent | 29 reactions, including glucose → pyruvate interconversions | not stated | measured-single | doi:10.1002/msb.20145228 (PubMed 24771084), via efetch id=24771084 | 2026-09-24 |
| Inferred LUCA metabolism | anaerobic acetogen (Wood–Ljungdahl-type autotrophy) | model inference | derived | doi:10.1038/s41559-024-02461-1 (PubMed 38997462), via efetch id=38997462 | 2026-09-24 |
| Which metabolic pathway is the most ancient | none | n/a | held-open | Competing inferences (glycolysis, gluconeogenesis-first, acetyl-CoA pathway) are all indirect; no measurement ranks them. | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): Does glycolysis proceed without O2; is it universal across nearly all life; is it the most ancient metabolic pathway?
2. What an answer must look like: pathway stoichiometry; distribution across the three domains; evidence ranking pathway ages.
3. Falsifiability condition: "Anaerobic" is falsified if any EMP step required O2. "Most ancient" is falsified if another pathway is shown to be older (e.g. gluconeogenic direction first, or a carbon-fixation pathway in LUCA preceding sugar catabolism).
4. Variables: measurable: stoichiometry, gene distribution. Derived: net yield. Held open: pathway age ranking.
5. Test designed: fetch KEGG reaction equations; fetch primary work on archaeal variants, gluconeogenic ancestry, non-enzymatic analogs, LUCA metabolism.
6. Data (unfiltered): table above. No EMP step uses O2. Net 2 ATP, 2 NADH per glucose. Archaea run modified variants. A gluconeogenesis-first proposal and an acetogenic LUCA inference compete with "glycolysis most ancient". Non-enzymatic glycolysis-like chemistry exists; a follow-up found it favored by mildly acidic or neutral conditions with Fe(II) (doi:10.1126/sciadv.1501235, PubMed 26824074, fetched via efetch id=26824074, 2026-09-24).
7. Variable Principle applied: (a) measured; (c) "nearly all life" holds only if "glycolysis" includes archaeal variants; (b) held open.
8. Model update (Capsule): (a) accounted. (b) is a live hypothesis written as fact. (c) needs the qualifier "in classical or modified form".
9. Documented: this file.
10. Next baseline: phylogenetic dating of glycolytic vs gluconeogenic enzymes against LUCA reconstructions.

## Forcing Test
- Test A (Ground): (a) grounded; (b) not grounded in a measurement.
- Test B (Uniqueness): (b) fails: at least two competitors survive (gluconeogenesis-first; acetyl-CoA pathway in LUCA).
- Test C (Direction): Not forced. The Say & Fuchs data are read by their authors as gluconeogenic direction first, the reverse of canon's order.
- Test D (Falsifiability): Yes. Falsifier: phylogenetic evidence that the core glycolytic enzymes post-date LUCA or post-date gluconeogenic enzymes.
- **Outcome:** live-hypothesis (for "most ancient"); the anaerobic stoichiometry is accounted.

## Anti-Operation (the gap this opens)
Canon places glycolysis (Stage 15) after LUCA (Stage 14) yet calls it the "most ancient metabolic pathway". If LUCA was an acetogen, carbon fixation (not glucose splitting) may be the older process. The stage sequence 13 → 14 → 15 embeds an ordering of metabolic origins that is open.

## Narrative stripped (if any)
None graded. The label "Glycolysis" is the observational name; no new label proposed. The descriptor "most ancient" is a scientific claim (graded above), not a framework mapping.
