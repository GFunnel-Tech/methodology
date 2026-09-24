---
id: STAGE-024
canon_ref: v5.1 Appendix A, Stage 24
canon_label: "Ion Gradients / Membrane Potentials"
diff_state: methodology-gap
exclusion_diagnosis: not-reached
claim_outcome: forced-fill
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix A, table "Stages 23–49", row 24 (line 1770):

> | 24 | Ion Gradients / Membrane Potentials | Na+/K+ ATPase establishes electrochemical asymmetry. Polarity deliberately created and maintained. |

**Factual core (graded):** the Na+/K+-ATPase establishes the electrochemical asymmetry (ion gradients, membrane potential) across cell membranes.
**Framework mapping (not graded):** "Polarity deliberately created and maintained."

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Na+,K+-ATPase exchange per ATP hydrolysis cycle | 3 Na+ out, 2 K+ in (electrogenic: one net positive charge out per cycle, by arithmetic) | stoichiometric | measured-single | doi:10.1038/nature06419 (PubMed 18075585), via https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=18075585 | 2026-09-24 |
| Crystal structure resolution, pig renal Na+,K+-ATPase with 2 Rb+ occluded | 3.5 Å | as published | measured-single | doi:10.1038/nature06419 (PubMed 18075585) | 2026-09-24 |
| Primary pump energizing the plasma-membrane potential, by eukaryotic group | H+-ATPase in plants and fungi; Na+,K+-ATPase in animals | n/a | measured-single | doi:10.1038/nature06417 (PubMed 18075595), via efetch id=18075595 | 2026-09-24 |
| Na+,K+-ATPase maintains Na+ and K+ concentration gradients; established role in "essentially every cell" (animal context) | observed | n/a | derived | doi:10.1002/cphy.c200018 (PubMed 34964112; review), via efetch id=34964112 | 2026-09-24 |
| Respiratory complexes generate a transmembrane proton gradient (mitochondria) | observed | n/a | measured-reproduced | doi:10.1007/978-981-10-7757-9_7 (PubMed 29464561), via Europe PMC REST search | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): Does the Na+/K+-ATPase establish cellular ion gradients and membrane potential, and is it the general mechanism across life?
2. What an answer must look like: measured pump stoichiometry; distribution of primary plasma-membrane pumps across groups.
3. Falsifiability condition: falsified if Na+/K+-ATPase did not move Na+ and K+ against their gradients, or (for generality) if other groups build membrane potential by other pumps.
4. Variables: measurable: stoichiometry; pump distribution. Held open: bacterial/archaeal plasma-membrane mechanisms in detail (not fetched beyond respiratory proton pumping).
5. Test designed: fetch the Na+,K+-ATPase structure paper, the plant/fungal H+-ATPase structure paper, and a review.
6. Data (unfiltered): table above. 3 Na+ / 2 K+ per ATP in animals. Plants and fungi energize the plasma membrane with an H+-ATPase instead. Respiring membranes build a proton gradient by electron transport.
7. Variable Principle applied: Na+/K+-ATPase function = measured. Its role as the mechanism of the stage = true for animals only.
8. Model update (Capsule): the factual core is correct for animal cells. The stage title ("Ion Gradients / Membrane Potentials") is general, but the note names only the animal pump. Reality shows other primary pumps (H+-ATPase in plants and fungi; respiratory proton pumping) that canon's item leaves out.
9. Documented: this file.
10. Next baseline: canon qualifies "Na+/K+ ATPase" as the animal case, or lists the primary pump per group.

## Forcing Test
- Test A (Ground): Grounded (structure and stoichiometry measured).
- Test B (Uniqueness): For animals, one candidate (Na+/K+-ATPase) survives as the primary plasma-membrane pump. Across eukaryotes, two survive (Na+/K+-ATPase; H+-ATPase).
- Test C (Direction): Forced: the pump moves Na+ out and K+ in using ATP.
- Test D (Falsifiability): Yes (step 3).
- **Outcome:** forced-fill (for the Na+/K+-ATPase's function). The gap is scope, not a contradiction.

## Anti-Operation (the gap this opens)
Canon's stage sequence places Stage 24 (Na+/K+ gradients) after Stage 22 (proton-driven ATP synthesis), but proton gradients (Stages 13, 21, 22) are themselves ion gradients. The stage conflates "ion gradients" in general with one animal-specific pump. Also opened: bacterial and archaeal plasma-membrane potentials, not fetched in this run.

## Narrative stripped (if any)
- "Polarity deliberately created and maintained" maps the Hermetic principle of Polarity onto membrane potential; "deliberately" attributes intent. Reality neither forces nor contradicts the mapping; measurement shows an ATP-driven pump, not intent. No change to the grade.
- The label is observational; no new label proposed.
