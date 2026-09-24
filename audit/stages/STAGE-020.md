---
id: STAGE-020
canon_ref: v5.1 Appendix A, Stage 20
canon_label: "Krebs Cycle"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix A, table "Stages 1–22", row 20 (line 1758):

> | 20 | Krebs Cycle | Acetyl-CoA fully oxidized. CO₂, ATP, and high-energy electron carriers produced. Shepherd’s Way at biochemical scale. |

**Factual core (graded):** the acetyl group of acetyl-CoA is fully oxidized to CO2 with production of ATP (or equivalent) and reduced electron carriers.
**Framework mapping (not graded):** "Shepherd’s Way at biochemical scale."

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Oxidative decarboxylations per turn: isocitrate dehydrogenase (NAD) R00709 and 2-oxoglutarate dehydrogenase R08549 | 2 CO2, 2 NADH | exact (curated stoichiometry) | measured-reproduced | https://rest.kegg.jp/get/R00709 ; https://rest.kegg.jp/get/R08549 ; module https://rest.kegg.jp/get/M00009 | 2026-09-24 |
| Malate dehydrogenase R00342 | 1 NADH per turn | exact | measured-reproduced | https://rest.kegg.jp/get/R00342 | 2026-09-24 |
| Succinate:quinone oxidoreductase R02164 (succinate + quinone ⇌ fumarate + quinol) | 1 reduced quinone per turn | exact | measured-reproduced | https://rest.kegg.jp/get/R02164 | 2026-09-24 |
| Succinyl-CoA ligase: ADP-forming R00405 or GDP-forming R00432 | 1 ATP or 1 GTP per turn | exact | measured-reproduced | https://rest.kegg.jp/get/R00405 ; https://rest.kegg.jp/get/R00432 | 2026-09-24 |
| Per glucose (derivation: 2 acetyl-CoA from STAGE-019 × one turn each) | 4 CO2, 6 NADH, 2 reduced quinone (FAD-linked), 2 ATP/GTP | exact under the pathway stoichiometry | derived | derived from the KEGG entries above | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): Does one turn of the cycle oxidize the two acetyl carbons to CO2 while producing ATP/GTP and reduced carriers?
2. What an answer must look like: curated reaction equations for each dehydrogenase, decarboxylation and substrate-level phosphorylation step.
3. Falsifiability condition: falsified if the cycle's decarboxylations did not release two CO2 per acetyl-CoA, or if no substrate-level phosphorylation occurred.
4. Variables: measurable: stoichiometry. Held open: none for the core.
5. Test designed: fetch KEGG module M00009 and its reaction entries.
6. Data (unfiltered): table above. Two CO2, three NADH, one reduced quinone, one ATP or GTP per turn. (The two CO2 released in a given turn are not carbon atoms of the acetyl group that entered that turn — carbon tracing not fetched here; the net carbon balance is two CO2 per acetyl.)
7. Variable Principle applied: measured / derived.
8. Model update (Capsule): accounted. Refinement: the substrate-level product is ATP or GTP depending on the succinyl-CoA ligase isoform; the FAD-linked carrier is enzyme-bound and passes electrons to quinone (R02164), not a free FADH2.
9. Documented: this file.
10. Next baseline: none required.

## Forcing Test
- Test A (Ground): Grounded in curated stoichiometry.
- Test B (Uniqueness): One stoichiometry survives.
- Test C (Direction): Forced for the oxidative cycle (reductive variants exist in some autotrophs; not fetched here).
- Test D (Falsifiability): Yes (step 3).
- **Outcome:** forced-fill.

## Anti-Operation (the gap this opens)
The KEGG module lists alternative enzymes (e.g. 2-oxoglutarate:ferredoxin oxidoreductase, K00174/K00175, in M00009). A ferredoxin-linked, reversible version of the cycle is a variable canon's single forward-running "Krebs Cycle" stage does not hold, and it bears on whether the cycle predates oxygen (Stage 17). Held open; not measured here.

## Narrative stripped (if any)
- "Shepherd’s Way at biochemical scale" is a framework mapping. Reality neither forces nor contradicts it. The label "Krebs Cycle" is observational; no new label proposed.
