---
id: STAGE-022
canon_ref: v5.1 Appendix A, Stage 22
canon_label: "ATP Synthase / Chemiosmotic Coupling"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix A, table "Stages 1–22", row 22 (line 1760):

> | 22 | ATP Synthase / Chemiosmotic Coupling | Protons flow back through ATP synthase. Mechanical rotation drives ADP → ATP. ≈32 ATP per glucose. Dynamic middle of all energy metabolism. |

Also v5.1 line 2082: "ATP Yield Per Glucose | ~32 ATP (eukaryotic)".

**Factual core (graded):** (a) proton back-flow through ATP synthase drives ATP synthesis; (b) by mechanical rotation; (c) yield ≈32 ATP per glucose (full aerobic oxidation, eukaryotic).
**Framework mapping (not graded):** "Dynamic middle of all energy metabolism."

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Rotation of F1-ATPase γ-subunit (Bacillus PS3), single-molecule | >100 revolutions, anticlockwise from membrane side; torque >40 pN·nm | as published | measured-reproduced | doi:10.1038/386299a0 (PubMed 9069291); reproduced in E. coli F1 with the same torque and direction, doi:10.1006/bbrc.1999.0885 (PubMed 10403811); both via https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=9069291,10403811 | 2026-09-24 |
| c-ring size, bovine mitochondrial F-ATPase | c8 (8 subunits) | structure | measured-single | doi:10.1073/pnas.1011099107 (PubMed 20847295), via efetch id=20847295 | 2026-09-24 |
| Protons per ATP by the F-ATPase with a c8 ring (3 ATP per 360°) | 2.7 | derived from c8 / 3 | derived | doi:10.1073/pnas.1011099107 (PubMed 20847295) | 2026-09-24 |
| c-ring sizes in fungi, eubacteria, chloroplasts | c10–c15 (3.3–5 H+/ATP) | range | measured-reproduced | doi:10.1073/pnas.1011099107 (PubMed 20847295; stated as observed across multiple prior structures) | 2026-09-24 |
| Mitochondrial P/O ratio, NADH-linked substrates | ~2.5 (alternative ~2.3 if H+/ATP = 10/3) | "about" | measured-reproduced | doi:10.1016/j.bbabio.2004.09.004 (PubMed 15620362; review of studies since 1937), via efetch id=15620362 | 2026-09-24 |
| Mitochondrial P/O ratio, succinate | ~1.5 (alternative ~1.4) | "about" | measured-reproduced | doi:10.1016/j.bbabio.2004.09.004 (PubMed 15620362) | 2026-09-24 |
| ATP per glucose, full aerobic oxidation (derivation below), cytosolic NADH entering at P/O 2.5 | 32 | depends on P/O | derived | derived: STAGE-015, -019, -020 stoichiometry (KEGG) × Hinkle P/O | 2026-09-24 |
| ATP per glucose, cytosolic NADH entering at P/O 1.5 (quinone-level entry) | 30 | depends on P/O | derived | as above | 2026-09-24 |
| ATP per glucose using the alternative P/O 2.3 / 1.4 | 29.8 (NADH at 2.3) to 28 (cytosolic NADH at 1.4) | depends on P/O | derived | as above | 2026-09-24 |

**Derivation (shown).** Per glucose, from the KEGG stoichiometry in STAGE-015, -019, -020: substrate-level ATP/GTP = 2 (glycolysis net) + 2 (succinyl-CoA ligase) = 4. NADH = 2 (glycolysis, cytosolic) + 2 (PDH) + 6 (Krebs) = 10. Reduced quinone via complex II = 2.
- Case A, all NADH at P/O 2.5, succinate-derived at 1.5: 4 + 10×2.5 + 2×1.5 = 4 + 25 + 3 = **32**.
- Case B, the 2 cytosolic NADH enter at quinone level (P/O 1.5): 4 + 8×2.5 + 2×1.5 + 2×1.5 = 4 + 20 + 3 + 3 = **30**.
- Case C, alternative P/O 2.3 / 1.4: 4 + 10×2.3 + 2×1.4 = **29.8**; with cytosolic NADH at 1.4: 4 + 8×2.3 + 4×1.4 = **28.0**.
Which route cytosolic NADH takes (shuttle) is organism- and tissue-dependent; the route mix was not measured in this run. These are mechanistic maxima: measured P/O values already include ATP export costs as far as the cited measurements capture them, but not in-vivo proton leak (not measured here).

## Scientific Inquiry run
1. Question (precise): Does proton back-flow drive rotary ATP synthesis, and what ATP yield per glucose do measured P/O ratios support?
2. What an answer must look like: direct rotation measurement; c-ring stoichiometry; measured P/O ratios; explicit arithmetic over pathway stoichiometry.
3. Falsifiability condition: (a)/(b) falsified if F1 did not rotate or rotation were not coupled to synthesis. (c) falsified if the derived yield from measured P/O excluded ~32.
4. Variables: measurable: rotation, torque, c-ring size, P/O. Derived: yield per glucose. Held open: shuttle route mix; in-vivo leak; the exact H+/ATP (2.7 for c8 vs 10/3 assumed in Hinkle's alternative).
5. Test designed: fetch single-molecule rotation papers, the bovine c-ring structure, and the P/O review; derive yield.
6. Data (unfiltered): table and derivation above. Rotation reproduced across two species. Derived yield 28–32 depending on assumptions; 32 is the top of the range.
7. Variable Principle applied: (a), (b) measured-reproduced. (c) derived; the value is a range, not a point.
8. Model update (Capsule): accounted. Canon's "≈32" equals the Case A maximum. A more exact statement: "≈30–32 (theoretical maximum; depends on shuttle route and H+/ATP)". The c8 ring (2.7 H+/ATP) is lower than the 10/3 in Hinkle's alternative, so Case C is not the lower bound for mammals; mammal-specific P/O from c8 was not fetched and stays open.
9. Documented: this file.
10. Next baseline: measured in-vivo ATP yield per glucose (with leak) in a named tissue.

## Forcing Test
- Test A (Ground): Grounded (rotation, c-ring, P/O all measured).
- Test B (Uniqueness): Mechanism: one candidate (rotary chemiosmotic coupling) survives. Yield: a range (28–32), not one value.
- Test C (Direction): Forced: protons flow down the gradient into the matrix through Fo; F1 synthesizes ATP (the reverse, ATP-driven rotation, was what the single-molecule assays observed).
- Test D (Falsifiability): Yes (step 3).
- **Outcome:** forced-fill for the mechanism; the ≈32 yield is consistent as the upper value of a derived range.

## Anti-Operation (the gap this opens)
Canon writes one number (≈32) for a quantity that depends on two held-open variables: the cytosolic-NADH route and the organism's c-ring size (c8 in vertebrates, c10–c15 elsewhere). The yield is therefore organism-specific. "~32 ATP (eukaryotic)" at line 2082 is not one value across eukaryotes (fungi and plants have larger c-rings per Watt et al.).

## Narrative stripped (if any)
- "Dynamic middle of all energy metabolism" is a framework mapping (Garlick Equilibrium). Reality neither forces nor contradicts it. The label is observational; no new label proposed.
