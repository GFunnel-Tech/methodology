---
id: STAGE-016
canon_ref: v5.1 Appendix A, Stage 16
canon_label: "Fermentation / Anaerobic Respiration"
proposed_label: "Fermentation (anaerobic respiration is a separate, ETC-based process)"
diff_state: conflict
exclusion_diagnosis: reached-conflicting
claim_outcome: forced-no
intake_result: adjusted
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix A, table "Stages 1–22", row 16 (line 1754):

> | 16 | Fermentation / Anaerobic Respiration | Pyruvate processed without oxygen. Low-yield, but functional. Dynamic middle of pre-oxygen metabolism. |

**Factual core (graded):** (a) pyruvate is processed without oxygen at low yield; (b) the label treats fermentation and anaerobic respiration as one stage (the note describes only the fermentation case).
**Framework mapping (not graded):** "Dynamic middle of pre-oxygen metabolism."

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Lactate dehydrogenase reaction (KEGG R00703): (S)-lactate + NAD+ ⇌ pyruvate + NADH + H+ (run in reverse in lactic fermentation, regenerating NAD+ without an external electron acceptor) | as listed | exact (curated stoichiometry) | measured-reproduced | https://rest.kegg.jp/get/R00703 | 2026-09-24 |
| Net ATP per glucose, glycolysis + lactate fermentation (derivation: EMP net 2 ATP, see STAGE-015; R00703 adds no ATP) | 2 ATP | exact under the pathway stoichiometry | derived | derived from https://rest.kegg.jp/get/M00001 and /R00703 | 2026-09-24 |
| Bacterial switch from O2 to alternative terminal electron acceptors (e.g. nitrate) when O2 is limiting; controlled by FNR in E. coli | observed | n/a | measured-reproduced | doi:10.1042/BST0361144 (PubMed 19021513), via https://www.ebi.ac.uk/europepmc/webservices/rest/search (query on "anaerobic respiration" / "terminal electron acceptor") | 2026-09-24 |
| E. coli anaerobic respiration with nitrate or fumarate as terminal electron acceptor | observed | n/a | measured-reproduced | doi:10.1074/jbc.M111.243261 (PubMed 21642439, PMC3143622), via Europe PMC REST search as above | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): Are fermentation and anaerobic respiration the same process, and is anaerobic pyruvate processing low-yield?
2. What an answer must look like: reaction stoichiometry for fermentation; measured anaerobic respiratory chains with non-O2 terminal acceptors.
3. Falsifiability condition: The conflation holds only if anaerobic respiration uses no external terminal electron acceptor / no respiratory chain. Measured nitrate/fumarate respiration falsifies it.
4. Variables: measurable: reaction stoichiometry; electron acceptors used. Derived: net ATP. Held open: which of the two appeared first in Earth history (not claimed by canon; not measured here).
5. Test designed: fetch KEGG LDH reaction; fetch primary studies of anaerobic respiration in E. coli.
6. Data (unfiltered): table above. Fermentation (e.g. pyruvate → lactate) regenerates NAD+ internally; ATP comes only from glycolysis (net 2 per glucose). Anaerobic respiration uses a respiratory chain with nitrate, fumarate or other acceptors instead of O2.
7. Variable Principle applied: (a) measured for fermentation. (b) measured-reproduced contradiction: the two are distinct processes.
8. Model update (Capsule): the note's content (pyruvate processed without O2, low yield) is correct for fermentation. The label's pairing with anaerobic respiration is ruled out. Anaerobic respiration belongs mechanistically with Stages 21–22 (a respiratory chain with a different terminal acceptor).
9. Documented: this file.
10. Next baseline: canon relabels Stage 16 as Fermentation and places anaerobic respiration with the electron-transport stages, or opens a separate stage for it.

## Forcing Test
- Test A (Ground): Grounded: stoichiometry and acceptor use are measured.
- Test B (Uniqueness): One reading survives: fermentation and anaerobic respiration are distinct.
- Test C (Direction): Forced: the conflation is ruled out.
- Test D (Falsifiability): Yes (step 3); the falsifier is met.
- **Outcome:** forced-no (for "fermentation = anaerobic respiration"). The fermentation note itself is accounted.

## Anti-Operation (the gap this opens)
If anaerobic respiration is split out, canon's order becomes open: respiratory chains with non-O2 acceptors need not wait for Stage 17 (oxygen) or Stage 18 (mitochondria). The linear order 16 → 17 → 18 → 21 then no longer describes when electron transport chains appeared.

## Narrative stripped (if any)
- "Dynamic middle of pre-oxygen metabolism" is a framework mapping (Garlick Equilibrium's dynamic middle). Reality neither forces nor contradicts it.
- Label: "Fermentation / Anaerobic Respiration" joins two measured-distinct processes. Proposed label: "Fermentation", with anaerobic respiration noted as a separate, ETC-based process.

**Recorded adjustment (intake: adjusted):** the pairing in the label is replaced by "Fermentation"; reason: measured-reproduced observation that anaerobic respiration uses non-O2 terminal electron acceptors via a respiratory chain, unlike fermentation. The canonical text is not edited; this adjustment is a proposal to the coordinator.
