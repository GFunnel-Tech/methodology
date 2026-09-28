---
id: SWEEP-026
canon_ref: "v5.1 Appendix A, Stages 15, 19 and 20 (Glycolysis, Pyruvate Oxidation → Acetyl-CoA, Krebs Cycle); with v5.1 Appendix D, Biological & Scaling Laws, row 'Krebs Cycle Stoichiometry'"
canon_label: "Glycolysis → Pyruvate Oxidation → Krebs Cycle as the central metabolic sequence"
proposed_label: "Central carbon flux distribution, including the pentose phosphate pathway and the PEP–glyoxylate cycle"
diff_state: methodology-gap
exclusion_diagnosis: not-reached
claim_outcome: live-hypothesis
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix A:

> "15 | Glycolysis | Most ancient metabolic pathway. Glucose split anaerobically. Universal across nearly all life."
> "19 | Pyruvate Oxidation → Acetyl-CoA | Bridge step. Substrate prepared for next processing layer."
> "20 | Krebs Cycle | Acetyl-CoA fully oxidized. CO₂, ATP, and high-energy electron carriers produced. Shepherd's Way at biochemical scale."

v5.1 Appendix D: "Krebs Cycle Stoichiometry | 1 acetyl-CoA → 3 NADH + 1 FADH₂ + 1 GTP + 2 CO₂ | The exact accounting of energy capture in cellular respiration."

**Split (RUNBOOK rule 4).** *Factual core graded here:* central metabolism consists of glycolysis, a pyruvate-oxidation bridge, and the Krebs cycle, in that order, with the stated per-turn stoichiometry.

*Framework mapping (not graded; see Narrative stripped):* "Shepherd's Way at biochemical scale"; "Bridge step. Substrate prepared for next processing layer."

Canon names **no pentose phosphate pathway**, no Entner–Doudoroff pathway, no glyoxylate shunt, and no PEP–glyoxylate cycle, anywhere in Appendix A or Appendix D that this audit reached. It presents central metabolism as a linear chain with one branch point (acetyl-CoA), and it states no flux distribution.

## Reality shows

Reference organism: *Escherichia coli* K-12, glucose- and galactose-limited, ¹³C metabolic flux analysis.

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Dependence of total cellular carbon influx on dilution rate, glucose-limited chemostat | linear | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC1392909/ | 2026-09-28 |
| Dependence of the *distribution* of major intracellular fluxes on dilution rate | "the distribution of almost all major fluxes varied **nonlinearly** with dilution rate" | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC1392909/ | 2026-09-28 |
| Location of the glyoxylate-shunt maximum and the concomitant TCA-cycle minimum | dilution rates 0.05–0.2 h⁻¹ (distinct maximum / minimum); low or absent at higher or extremely low dilution rates | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC1392909/ | 2026-09-28 |
| Identity of that flux on glucose | the PEP–glyoxylate cycle, which oxidises PEP (or pyruvate) to CO₂ | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC1392909/ | 2026-09-28 |
| Step change in pentose phosphate pathway activity | a step increase at around 0.2 h⁻¹ | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC1392909/ | 2026-09-28 |
| NADPH formation relative to anabolic demand, all dilution rates | 20 to 50% in excess of demand | as published range | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC1392909/ | 2026-09-28 |
| Effect of transcriptional regulators on flux, 91 regulator mutants on glucose and galactose | about 2/3 of regulators affected absolute flux rates, but "the partitioning between different pathways remained largely stable", with transcriptional control focused primarily on the acetyl-CoA branch point | as published | measured-single | https://pubmed.ncbi.nlm.nih.gov/21451587/ | 2026-09-28 |
| Number of transcription factors controlling flux distribution on glucose | nine (including ArcA, Fur, PdhR, IHF A, IHF B); on galactose exclusively cAMP-dependent Crp regulation of PEP–glyoxylate cycle flux | as published | measured-single | https://pubmed.ncbi.nlm.nih.gov/21451587/ | 2026-09-28 |
| Fully respiratory galactose metabolism | depends *exclusively* on the PEP–glyoxylate cycle, in contrast to respiro-fermentative glucose metabolism | as published | measured-single | https://pubmed.ncbi.nlm.nih.gov/21451587/ | 2026-09-28 |
| A single numeric glycolysis : pentose-phosphate split ratio for *E. coli* on glucose with published uncertainty | not retrieved | n/a | held-open | the flux-map values sit in figures and supplementary tables of the papers above, which were not machine-readable this run; the qualitative step-change at 0.2 h⁻¹ is recorded instead and no percentage is supplied from memory | 2026-09-28 |

## Scientific Inquiry run

1. Question (precise): Does a canonical item hold the measured flux distribution of bacterial central metabolism — including the pentose phosphate pathway and the PEP–glyoxylate cycle — and does DETECT → PROCESS → RESPOND fit the measured mechanism by which flux is partitioned?
2. What an answer must look like: canon's stages and stoichiometry quoted; measured evidence on whether the distribution is fixed or varies, and with what; and a named DPR assignment tested for boundaries.
3. Falsifiability condition: canon's linear reading fails if a measured, quantitatively significant central pathway exists that appears in no canonical stage, and if the partition among pathways is measured to vary non-monotonically with growth conditions. Both hold.
4. Variables: measurable / bounded / held open: **Measurable** — pathway fluxes by ¹³C labelling; NADPH surplus; the location of the PPP step change. **Bounded** — the glyoxylate-shunt maximum lies in 0.05–0.2 h⁻¹; the PPP step change near 0.2 h⁻¹. **Held open** — the numeric split ratios.
5. Test designed: fetch a ¹³C flux study across a range of growth rates, and a large-scale regulator study, and ask (i) whether canon names every measured pathway, (ii) whether the distribution is constant.
6. Data (unfiltered): the table above. Two results cut against different intuitions and are recorded together: the distribution varies non-linearly with growth rate (so there is no single flux map), *and* it is largely robust to deleting individual transcriptional regulators (so the variation is not a transcriptional program).
7. Variable Principle applied: canon's "exact accounting" language implies one stoichiometry with one outcome. Measurement gives a per-turn stoichiometry that is exact and a *flux distribution* that is condition-dependent. These are two different variables and canon has only one. The numeric split is held open rather than estimated.
8. Model update (Capsule: what the failed parts contribute): canon's central-metabolism stages need at minimum a pentose-phosphate entry (it supplies ribose for the RNA of canon's own Stage 11 and NADPH for biosynthesis) and an entry for the glyoxylate/PEP–glyoxylate route. The failed part contributes a specific, named absence: canon's Appendix A cannot express a *branch*, only a chain, so no arrangement of its existing stages can hold a split ratio.
9. Documented: this file. Attempted DPR assignment: **DETECT** → arrival of glucose-6-phosphate at the branch point between phosphoglucose isomerase and glucose-6-phosphate dehydrogenase; **PROCESS** → the competing enzyme kinetics that set the split; **RESPOND** → downstream flux in each arm. There is no boundary at the first step: nothing in the cell detects G6P at that node. The split is set by the relative concentrations, Km values and reversibility of two enzymes acting on a shared substrate — a continuous physical competition with no threshold, no signal and no decision. Labelling one side of a bifurcation "DETECT" is arbitrary; the branch is symmetric with respect to the label. **DPR mapping: applied after the fact.** (Contrast SWEEP-025 and SWEEP-033, where a real sensor exists.)
10. Next baseline: numeric split ratios from the supplementary flux maps of either paper. Re-review 2027-09-24.

## Forcing Test

- Test A (Ground): Grounded for the existence and condition-dependence of the unnamed pathways; not grounded numerically.
- Test B (Uniqueness): Not unique. Canon's three-stage chain is one of several possible descriptions and it is the only one that omits measured, quantitatively major routes.
- Test C (Direction): A direction is measured but it is not the one canon implies: flux distribution is non-monotonic in growth rate, so there is no single progression through the pathways.
- Test D (Falsifiability): Falsifiable. The linear reading fails on the presence of unnamed pathways; the Krebs per-turn stoichiometry itself survives.
- **Outcome:** `live-hypothesis`. Canon's per-turn stoichiometry is sound; its claim to be a description of central metabolism is not, because whole measured pathways are absent.

## Anti-Operation (the gap this opens)

The NADPH surplus row (20–50% above anabolic demand at all dilution rates) opens a gap canon cannot currently hold: a cell running a systematic surplus of a reducing cofactor is not optimising, and the excess must be dissipated. Any framework claiming that biology runs "perfect process" or holds "the draw" must say what a measured, condition-independent 20–50% overproduction is. Neither "perfect process" nor "the draw" predicts it.

## Narrative stripped (if any)

Removed: "Shepherd's Way at biochemical scale" (Stage 20) and "Bridge step. Substrate prepared for next processing layer" (Stage 19). The Krebs cycle is a cycle with eight enzymes and several entry and exit points (it is also, measurably, run in branched and partial modes); mapping it onto a seven-step management cycle is an interpretation reality neither forces nor contradicts. The phrase "the exact accounting of energy capture in cellular respiration" overstates: the per-turn stoichiometry is exact, but the accounting of respiration depends on flux distribution, which the measurements above show is not fixed.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
