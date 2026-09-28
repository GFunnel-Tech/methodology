---
id: SWEEP-010
canon_ref: v5.1 Layer I.C Domain 9 (Biological Process); v5.1 Layer I.C Domain 6 (Linguistic / Communication)
canon_label: "Biological Process (organism-level regulation); Linguistic / Communication (encoding and transmission of process)"
diff_state: methodology-gap
exclusion_diagnosis: not-reached
claim_outcome: stipulation
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Layer I.C Domain 9 is written at the scale of one organism: "The organism continuously monitors deviation... The organism that achieves stasis is dead." Its named mechanisms are homeostasis, immune response, apoptosis, gene expression and autonomic balance.

v5.1 Layer I.C Domain 6, from `framework/domains.md`: "Linguistic / Communication | Second | Encoding and transmission of process." Layer 0's Linguistic row: "DETECT: Communicative intent | PROCESS: Encoding → transmission → decoding | RESPOND: Shared understanding or named misalignment."

v5.1 Appendix A, Stage 25: "Multicellularity | Cells stop competing and start specializing."

Canon names no cell-to-cell signalling among single-celled organisms, no population-level sensing, and no threshold-triggered collective behaviour. Searched for `quorum`, `biofilm`: zero hits.

Reference organisms: this record departs from E. coli K-12, whose LuxI/LuxR system is absent. The best-measured systems are *Vibrio harveyi* (single-cell quantification of AI-1 and AI-2 integration) and *Vibrio fischeri* (autoinducer diffusion and dose-response).

**Split.** *Factual core:* (a) single-celled organisms communicate chemically and change behaviour with population density; (b) canon's Domain 9 is organism-scaled and its Domain 6 is about intent-bearing communication. *Framework mapping:* Stage 25's "cells stop competing and start specializing" as the point at which cells begin to coordinate.

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Inhibition constant for autoinducer AI-1, single-cell fluorescence dose-response of a Qrr4 promoter reporter, V. harveyi | K = 6.9 nM | ± 0.5 nM | measured-single | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2661960/fullTextXML (Long et al. 2009, PLoS Biol 7:e68) | 2026-09-28 |
| Inhibition constant for autoinducer AI-2, same assay | K = 6.4 nM | ± 0.5 nM | measured-single | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2661960/fullTextXML | 2026-09-28 |
| Hill coefficient of the single-cell dose-response to each autoinducer | 1 (each curve described by a simple Hill function with Hill coefficient equal to one) | as published | measured-single | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2661960/fullTextXML | 2026-09-28 |
| Rule by which the two autoinducer signals are combined | strictly additively in a shared phosphorelay, with nearly equal weight from each signal | as published | measured-single | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2661960/fullTextXML | 2026-09-28 |
| Cell-to-cell variability of the response | single-peaked distributions with standard deviation over mean always below 0.4, 100 cells per data point; population can reliably distinguish several distinct autoinducer conditions | as published | measured-single | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2661960/fullTextXML | 2026-09-28 |
| Molecules per cell volume corresponding to 1 nM autoinducer | approximately one molecule in the volume of a single V. harveyi cell | as published | derived | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2661960/fullTextXML | 2026-09-28 |
| Lowest autoinducer concentration sufficient for induction of luminescence, V. fischeri, tritiated autoinducer | as low as 10 nM, equivalent to 1 or 2 molecules per cell | as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=3897188&rettype=abstract&retmode=text (Kaplan & Greenberg 1985, J Bacteriol 163:1210) | 2026-09-28 |
| Concentration at which the response to autoinducer is maximal, same system | about 200 nM | as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=3897188&rettype=abstract&retmode=text | 2026-09-28 |
| Mechanism and reversibility of autoinducer association with cells | association is by simple diffusion (cellular concentration equalled external concentration, equilibration within 20 s; 85–99.5% of tracer escaped on transfer to autoinducer-free buffer); binding to its active site is reversible; lowering external concentration below 10 nM after induction had commenced stopped the induction response | as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=3897188&rettype=abstract&retmode=text | 2026-09-28 |

## Scientific Inquiry run
1. Question (precise): Does a canonical item hold quorum sensing, and is the measured input-output behaviour a threshold (switch) or a graded response? Does DETECT → PROCESS → RESPOND fit a mechanism whose detected quantity is the population itself?
2. What an answer must look like: a measured dose-response with a stated Hill coefficient and inhibition constants, at single-cell resolution so that population averaging cannot manufacture a threshold; plus an explicit DPR assignment.
3. Falsifiability condition: the common description of quorum sensing as *threshold* behaviour fails if the single-cell dose-response is measured to be graded with Hill coefficient 1 over the physiological range.
4. Variables: measurable / bounded / held open: measurable — inhibition constants, Hill coefficient, additivity, noise, induction and saturation concentrations, diffusion and reversibility. Bounded — molecules per cell (derived from concentration and cell volume). Held open — whether the switch-like behaviour of a *growing culture* arises from the sensing step or from downstream feedback; no measurement fetched this run separates them.
5. Test designed: fetch the single-cell dose-response study (2009) and the original radiotracer dose-response study (1985); read the Hill coefficient and the induction and saturation concentrations directly.
6. Data (unfiltered): K = 6.9 ± 0.5 nM for AI-1 and 6.4 ± 0.5 nM for AI-2, strikingly similar. Hill coefficient equal to one for each. The two signals add, with equal weight. Response noise stays below 40% of the mean, and the population distinguishes several distinct conditions. 1 nM is about one molecule per cell volume. In V. fischeri, induction begins at 10 nM — one or two molecules per cell — and saturates near 200 nM, a range of about a factor of 20. Autoinducer enters by simple diffusion, equilibrates in 20 s, leaves almost completely, and binding is reversible; dropping the external concentration after induction had begun stopped the response.
7. Variable Principle applied: **Measured** — the two inhibition constants, the Hill coefficient of 1, additivity, the noise bound, the 10-to-200 nM working range, diffusive and reversible association. **Structurally derived** — molecules per cell volume. **Held open** — the origin of culture-level switch behaviour. The DPR mapping: DETECT = autoinducer binding the membrane receptor LuxN or the periplasmic binding protein and LuxPQ; PROCESS = the shared phosphorelay that sums the two inputs; RESPOND = transcription of the target promoter. Those boundaries are real, and they are the same architecture as SWEEP-002 and SWEEP-009 — a two-component relay — so the mapping fits for the same reason. What does *not* survive is the framing: the quantity detected is not a stimulus from the environment but the *number of organisms like the detector*. Canon's Domain 9 has no scale above the organism and Stage 25 puts cell coordination at multicellularity; canon's Domain 6 (Linguistic) has a communication slot, but its DETECT is "communicative intent", which a diffusing molecule at one molecule per cell does not have. So the mechanism falls between two canonical domains and is held by neither.
8. Model update (Capsule: what the failed parts contribute): two adjustments are proposed. (a) The threshold reading of quorum sensing is not what is measured at the sensing step: the dose-response is graded, Hill coefficient 1, over a 20-fold concentration range, and the switch — where one exists — must be located downstream, in feedback, not in detection. (b) Canon needs a scale between Domain 9's organism and Stage 25's multicellular body: a population of genetically identical free-living cells that regulates collectively. The failed attempt to place this in Domain 6 contributes the sharper point: chemical communication without intent is measurable, so Domain 6's "communicative intent" as DETECT is an organism-scale assumption that does not generalize downward.
9. Documented: this file.
10. Next baseline: the sensing step is graded and accounted by measurement; the population scale is a gap. Held open with `review_after`: whether the culture-level switch is generated by positive feedback, which would need a further fetched measurement.

## Forcing Test
- Test A (Ground): grounded. One single-cell fluorescence study and one radiotracer dose-response study, independent by 24 years and different techniques, fetched this run.
- Test B (Uniqueness): unique for the negative claim about thresholds. A Hill coefficient of one, measured cell by cell, admits no cooperative-switch account of the detection step.
- Test C (Direction): canon runs intent → encoding → transmission → decoding → shared understanding (Domain 6). The measurement runs production → diffusion → equal-weight summation → graded transcription, with no intent and no encoding: the molecule *is* the message and its only content is its concentration.
- Test D (Falsifiability): the condition at step 3 was stated in advance and is met.
- **Outcome:** `stipulation`. Canon holds neither the mechanism nor its scale; the DPR mapping fits at real boundaries because the machinery is a two-component relay, but canon's framing of both candidate domains fails — Domain 9 stops at the organism, Domain 6 requires intent. `methodology-gap`, diagnosis `not-reached`. Intake `open`: every contradicting row is `measured-single`, so it may not force canon to re-form.

## Anti-Operation (the gap this opens)

- The detected quantity is the detector's own kind. Canon's Layer I.F (observation as the intake organ of creation) never addresses a system whose observation target is its own population size. Self-census is unmapped, and it is the closest biological analogue to the framework's own self-application claim in Layer ⊙.
- A response is graded at the single-cell level and switch-like at the culture level. Canon has no vocabulary for a property that exists only at the aggregate — Correspondence as stated ("solve it once and apply it everywhere") predicts scale-invariance, and here the *shape of the response* is not scale-invariant. That is a direct pressure point on Correspondence and this record does not resolve it.
- The two inhibition constants for chemically unrelated molecules agree to within 8%. Canon's Appendix D has no category for a tuning coincidence, and the audit has no criterion for when matched constants are evidence of anything.

## Narrative stripped (if any)

- "Cells stop competing and start specializing" at Stage 25 (Multicellularity): free-living Vibrio cells coordinate gene expression across a population while remaining separate organisms. Coordination does not require multicellularity, so Stage 25 is not the point at which cells begin to cooperate. Stripped as a claim about when coordination becomes possible.
- "Communicative intent" as the Linguistic DETECT (Layer 0): stripped for this scale. Reality shows transmission and reception with no intent-bearing sender; nothing in the measurement forces intent, and importing it would make the domain inapplicable to the best-measured case of chemical communication.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; audit commentary is not endorsed by the author.
```
