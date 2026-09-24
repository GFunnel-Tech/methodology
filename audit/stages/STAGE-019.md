---
id: STAGE-019
canon_ref: v5.1 Appendix A, Stage 19
canon_label: "Pyruvate Oxidation → Acetyl-CoA"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix A, table "Stages 1–22", row 19 (line 1757):

> | 19 | Pyruvate Oxidation → Acetyl-CoA | Bridge step. Substrate prepared for next processing layer. |

**Factual core (graded):** pyruvate is oxidized to acetyl-CoA, linking glycolysis to the Krebs cycle.
**Framework mapping (not graded):** "Substrate prepared for next processing layer."

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Pyruvate dehydrogenase overall reaction (KEGG R00209): pyruvate + CoA + NAD+ ⇌ acetyl-CoA + CO2 + NADH + H+ | 1 NADH, 1 CO2 per pyruvate | exact (curated stoichiometry) | measured-reproduced | https://rest.kegg.jp/get/R00209 | 2026-09-24 |
| Enzyme systems listed for pyruvate → acetyl-CoA (KEGG module M00307) | pyruvate dehydrogenase complex (K00161/K00162/K00163, K00627, K00382) and alternatives incl. pyruvate:ferredoxin oxidoreductase (K00169–K00172, K00189) | n/a | measured-reproduced | https://rest.kegg.jp/get/M00307 | 2026-09-24 |
| Per glucose (derivation: 2 pyruvate from EMP glycolysis, STAGE-015; × R00209) | 2 NADH, 2 CO2 | exact under the pathway stoichiometry | derived | derived from https://rest.kegg.jp/get/M00001 and /R00209 | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): Is pyruvate oxidatively decarboxylated to acetyl-CoA, and with what stoichiometry?
2. What an answer must look like: curated reaction equation and enzyme assignment.
3. Falsifiability condition: falsified if acetyl-CoA were not the product that enters the Krebs cycle from pyruvate.
4. Variables: measurable: reaction stoichiometry. Held open: none for the core claim.
5. Test designed: fetch KEGG reaction and module entries.
6. Data (unfiltered): table above. PDH yields acetyl-CoA, CO2 and NADH. KEGG lists more than one enzyme system for this step (PDH complex; pyruvate:ferredoxin oxidoreductase, EC 1.2.7.1, named as ferredoxin-linked in https://rest.kegg.jp/get/K00169, retrieved 2026-09-24).
7. Variable Principle applied: measured.
8. Model update (Capsule): accounted. Canon's generic wording ("Pyruvate Oxidation → Acetyl-CoA") covers both enzyme systems.
9. Documented: this file.
10. Next baseline: none required for the core; see Anti-Operation for the ordering question.

## Forcing Test
- Test A (Ground): Grounded in curated enzyme stoichiometry.
- Test B (Uniqueness): One product (acetyl-CoA) survives.
- Test C (Direction): Forced: pyruvate → acetyl-CoA (the PDH reaction is written reversibly in KEGG but is physiologically the oxidative direction; direction not quantified in this run).
- Test D (Falsifiability): Yes (step 3).
- **Outcome:** forced-fill.

## Anti-Operation (the gap this opens)
KEGG lists a ferredoxin-dependent alternative (PFOR) to the NAD-linked PDH complex. Canon places this step after oxygenation and endosymbiosis (Stages 17–18). Whether pyruvate → acetyl-CoA is older than those stages (in anaerobes) is a variable the stage order hides. Not measured here; held open.

## Narrative stripped (if any)
- "Substrate prepared for next processing layer" is a framework mapping (processing layers). Reality neither forces nor contradicts it.
- "Bridge step" is a conventional textbook descriptor, not a framework claim. The label is observational; no new label proposed.
