---
id: SWEEP-005
canon_ref: v5.1 Layer I.C Domain 9 Biological Process Algorithm, steps 1–2; v5.1 Layer I.C Domain 9, "Homeostasis as Garlick Equilibrium"
canon_label: "Identify the biological system and its homeostatic set-point for each measurable variable; detect deviations from set-point"
proposed_label: "Identify the regulated quantity, which may be a level or a rate of change"
diff_state: conflict
exclusion_diagnosis: reached-conflicting
claim_outcome: forced-no
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Domain 9 Biological Process Algorithm, step 1: "Identify the biological system and its homeostatic set-point for each measurable variable." Step 2: "Detect deviations from set-point. Continuous monitoring is the organism's baseline state."

v5.1 Layer I.C Domain 9, Homeostasis row: "The organism continuously monitors deviation, processes the signal through cascading regulatory pathways, and responds to correct. Equilibrium is dynamic correction at every moment."

v5.1 Layer 0, Biological row: DETECT is "Homeostatic deviation or threat".

**Split.** *Factual core:* biological regulation works by detecting deviation from a set-point for each measurable variable. *Framework mapping:* homeostasis as the Garlick Equilibrium; "equilibrium is dynamic correction at every moment".

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Run and tumble duration distributions, E. coli, 3D tracking of 2,551 motile cells over 14,188 s of trajectory | approximately exponential, characteristic times 0.64 s (run) and 0.19 s (tumble) | as published; stated to be similar to earlier tracking | measured-reproduced | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4659942/fullTextXML (Taute et al. 2015, Nat Commun 6:8776) | 2026-09-28 |
| Population mean turning angle, same dataset | 57° | population mean; earlier report 68° | measured-single | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4659942/fullTextXML | 2026-09-28 |
| Population mean swimming speed, same dataset | 40 µm s^-1 | earlier report 14 µm s^-1; source attributes the difference to growth and motility media | measured-single | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4659942/fullTextXML | 2026-09-28 |
| Temporal weighting used by wild-type cells, tethered-cell impulse, step, ramp and sine stimuli | 4 s window: the past 1 s weighted positively, the previous 3 s negatively; the cell responds to the difference | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC387059/ (Segall, Block & Berg 1986, PNAS 83:8987) | 2026-09-28 |
| Regulated quantity identified from exponential-ramp stimuli | the rotational bias tracks the *rate of change* of chemoreceptor occupancy, not its level; behaviour fits proportional control on the difference between current occupancy and occupancy averaged over the recent past | as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=6339475&rettype=abstract&retmode=text (Block, Segall & Berg 1983, J Bacteriol 154:312) | 2026-09-28 |
| Range of ambient attractant concentrations to which wild-type cells adapt and still respond to further steps, in vivo FRET | adapted responses measured at ambient 0, 0.1, 0.5 and 5 mM MeAsp; families of dose-response curves collapse onto one curve when plotted against fractional change in receptor occupancy | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC117525/ (Sourjik & Berg 2002, PNAS 99:123) | 2026-09-28 |
| Sensitivity of the pathway (gain) | the change in occupancy of one receptor molecule produces a significant response | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC387059/ | 2026-09-28 |
| Amplification between fractional receptor occupancy change and kinase output | slope −36 (addition), 27 (removal) | ± 1; ± 2 | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC117525/ | 2026-09-28 |
| Behaviour of adaptation-deficient cheRcheB cells | weight the past second like wild type but make no short-term temporal comparisons; no adaptation over 12 s | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC387059/ | 2026-09-28 |

## Scientific Inquiry run
1. Question (precise): Does the measured run-and-tumble system have a homeostatic set-point for a measurable variable, as canon's Domain 9 algorithm step 1 requires, and does the DETECT operation correspond to "deviation from set-point"?
2. What an answer must look like: an identification of the regulated quantity from stimulus-response measurements, and a statement of whether that quantity is a level (which can have a set-point) or a derivative (which cannot, in the same sense).
3. Falsifiability condition: step 1 read as universal fails if a well-measured biological control system regulates a rate of change rather than a level, and adapts away any level.
4. Variables: measurable / bounded / held open: measurable — run and tumble time constants, turn angle, speed, temporal weighting, ramp responses, dose-response collapse across four ambient concentrations, gain. Bounded — absolute gain in molecules. Held open — whether a derivative-regulating loop should still be called homeostatic.
5. Test designed: fetch 3D tracking statistics (independent lab, 2015), the tethered-cell temporal-comparison analysis (1986), the ramp analysis (1983) and the FRET adaptation series (2002); ask each whether a concentration set-point exists.
6. Data (unfiltered): runs and tumbles are exponentially distributed with time constants 0.64 s and 0.19 s; mean turn 57°; mean speed 40 µm s^-1 versus 14 µm s^-1 in the earlier report. The cell compares the last 1 s against the previous 3 s and responds to the difference. Under exponential ramps the bias moves with the *rate* of occupancy change and holds a new stable level for the duration of the ramp. Adapted cells give the same response to the same *fractional* occupancy change at ambient 0, 0.1, 0.5 and 5 mM. Deleting CheR and CheB removes the comparison but not the immediate weighting. Gain is at the single-receptor level.
7. Variable Principle applied: **Measured** — the interval statistics, the 4 s bilobed window, derivative control, adaptation across four ambient levels, the gain statement. **Structurally derived** — none load-bearing. **Held open** — the definition question at step 4. Concretely, canon's DETECT ("deviation from set-point") cannot be assigned: there is no attractant concentration the cell is holding. The cell adapts to whatever level it finds and then measures the derivative. DETECT here is a *comparison between two time windows of the same variable*, which is a different operation from comparison against a stored reference. PROCESS and RESPOND map as in SWEEP-002 and SWEEP-004. So the failure is specifically at DETECT and specifically at the word "set-point".
8. Model update (Capsule: what the failed parts contribute): step 1 must not require a set-point for every measurable variable. Proposed wording: "Identify the regulated quantity, which may be a level (set-point control) or a rate of change (derivative control), and state which." The failed universal reading contributes the distinction, and the distinction is useful upward: canon's own Layer VI (Shepherd's Way) and Layer V (BEAS scoring) both assume level control, so an organization tracking growth *rate* rather than absolute revenue is derivative control and is currently unnamed in the framework. That is a correspondence claim the audit can raise but not settle.
9. Documented: this file.
10. Next baseline: "homeostatic set-point for each measurable variable" is ruled out as universal; the replacement wording is proposed. Intake stays `open`, not `adjusted`: the two measurements that establish derivative control (1983, 1986) come from one laboratory lineage, so per substrate item 8 they are not independent reproduction, even though the run/tumble statistics themselves are reproduced by an independent group (2015). `review_after` set.

## Forcing Test
- Test A (Ground): grounded. Four measurement papers, two laboratories, fetched this run. The interval statistics are independently reproduced; the derivative-control result is not.
- Test B (Uniqueness): unique for the negative claim. No account with a concentration set-point survives dose-response collapse across four ambient levels spanning a factor of 50 plus the ramp results.
- Test C (Direction): canon runs set-point → deviation → correction. The measurement runs ambient level → adapt it away → measure the derivative → bias the random walk. The arrows are incompatible at the first step, compatible thereafter.
- Test D (Falsifiability): the condition at step 3 was stated in advance and is met.
- **Outcome:** `forced-no` for Domain 9 algorithm step 1 read as universal ("a homeostatic set-point for each measurable variable"). `conflict`, diagnosis `reached-conflicting`, intake `open` with `review_after` — the contradicting observation is `measured-single` in the sense that matters, so it may not force an adjustment. DPR mapping: **after the fact at DETECT** (canon's detection criterion cannot be instantiated), sound at PROCESS and RESPOND.

## Anti-Operation (the gap this opens)

- Derivative control means the system is indifferent to its absolute state. Canon's Garlick Equilibrium, BEAS scoring and "dynamic middle" all measure position, not velocity. Whether a derivative-controlled organization is healthy or blind is now an open question the framework cannot answer.
- Tumbles are 0.19 s and runs 0.64 s, both exponential. Canon's Layer II Rhythm asserts cyclicity; an exponentially distributed, memoryless alternation is the opposite of a rhythm. No canonical item distinguishes periodic from Poissonian alternation.
- Mean speed differs by a factor of ~3 between two datasets because of media composition. Canon states no measurement protocol for any of its biological claims, so no canonical number here could be checked even if one existed.

## Narrative stripped (if any)

- "Equilibrium is dynamic correction at every moment" (Homeostasis row): the measured cell is not correcting toward anything; it is climbing a gradient it cannot represent, using a 4 s memory and a biased coin. "Correction" imports a target. Reality does not force it.
- "Homeostasis as Garlick Equilibrium": the analogy is retained by canon and neither forced nor contradicted as an analogy, but it cannot be used to *derive* step 1's set-point requirement, which measurement rules out.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; audit commentary is not endorsed by the author.
```
