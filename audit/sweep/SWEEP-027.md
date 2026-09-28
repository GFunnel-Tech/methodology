---
id: SWEEP-027
canon_ref: "v5.1 Layer I.D, 'The Dynamic Middle — The Zhongyong Principle' and 'Why The Middle Must Shift — Not Just Balance', with the Biological row of 'The Dynamic Middle Across All Domains'"
canon_label: "The Dynamic Middle — a continuously recalibrating centre that shifts in response to system state"
proposed_label: "Measured threshold growth rate of acetate overflow (λ_ac) and its shift under proteome burden"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: live-hypothesis
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Layer I.D:

> "The middle is not the absence of Yin or Yang. It is the point of maximum adaptability ... This point is NOT fixed. It shifts continuously in response to system state."
> "A fixed middle is a dead middle. It is the distinction between a thermostat and a living organism. Both respond to temperature deviation. But the thermostat maintains a fixed set-point. The living organism adjusts its set-point based on environmental demands, seasonal cycles, developmental stage, and accumulated adaptation."

Layer I.D, "The Dynamic Middle Across All Domains", Biological row: "Yang Extreme: Chronic sympathetic — burnout | Yin Extreme: Chronic parasympathetic — fatigue | Dynamic Middle: HRV — heart rate variability."

**Split (RUNBOOK rule 4).** *Factual core graded here:* biological systems hold an operating point that is not fixed, and it moves with the state of the system.

*Framework mapping (not graded; see Narrative stripped):* Yin/Yang polarity; the chess "draw"; the Three-States table (Dynamic / Rigid / Collapsed middle).

Canon's only biological instance is a vertebrate one (HRV). It names no bacterial quantity, no unit, and no value.

## Reality shows

Reference organism: *Escherichia coli* K-12 derivatives (NQ-series), aerobic batch and titratable-uptake cultures.

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Form of the dependence of acetate excretion rate J_ac on growth rate λ | threshold-linear: J_ac = S_ac·(λ − λ_ac) for λ ≥ λ_ac, and 0 below | as published (the "acetate line") | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC4843128/ | 2026-09-28 |
| Threshold growth rate λ_ac, wild type, multiple carbon sources | ≈ 0.76 h⁻¹ (55 min per doubling) | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC4843128/ | 2026-09-28 |
| λ_ac with "useless" protein expressed (LacZ at φ_Z ≈ 8%) | 0.66 ± 0.05 h⁻¹ (model prediction 0.61) | ± as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC4843128/ | 2026-09-28 |
| λ_ac with LacZ at φ_Z ≈ 16% | 0.48 ± 0.22 h⁻¹ (model prediction 0.47) | ± as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC4843128/ | 2026-09-28 |
| λ_ac with flagellar (motility-protein) knockout — i.e. burden *removed* | 0.96 ± 0.02 h⁻¹ (model prediction 0.88) | ± as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC4843128/ | 2026-09-28 |
| λ_ac with 2 / 4 / 8 mM chloramphenicol | 0.54 ± 0.02 / 0.46 ± 0.02 / 0.26 ± 0.04 h⁻¹ | ± as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC4843128/ | 2026-09-28 |
| Law governing the shift | λ(φ_Z) = λ_ac·(1 − φ_Z/φ_max), with φ_max ≈ 47% the extrapolated useless-protein fraction at which growth rate vanishes | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC4843128/ | 2026-09-28 |
| Slope S_ac of the acetate line under those perturbations | unchanged (11.0 ± 1.2 and 9.1 ± 1.3 mM/OD vs nominal 10.0) — perturbations shift the threshold, not the slope | ± as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC4843128/ | 2026-09-28 |
| Mechanistic cause, tested directly | the proteome cost of energy biogenesis by respiration exceeds that by fermentation, "quantitatively confirmed by direct measurement of protein abundances via quantitative mass spectrometry" | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC4843128/ | 2026-09-28 |
| Whether the shift in λ_ac is an "adjustment of a set-point" by the cell or a moving optimum of a fixed allocation rule | a fixed allocation rule with three proteomic cost parameters reproduces every measured shift and predicts new ones | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC4843128/ | 2026-09-28 |

## Scientific Inquiry run

1. Question (precise): Is there a measured bacterial optimum, does it move, and if so does the movement support canon's Layer I.D claim that a living system "adjusts its set-point"?
2. What an answer must look like: a named measurable quantity with a threshold value, plus that threshold measured again under at least two perturbations, with uncertainties.
3. Falsifiability condition: canon's claim fails if the measured operating point is fixed across perturbations of system state. It does not fail: λ_ac moves from 0.26 to 0.96 h⁻¹, a factor of 3.7, in one strain background.
4. Variables: measurable / bounded / held open: **Measurable** — λ_ac, S_ac, φ_Z, φ_max. **Bounded** — λ_ac in 0.26–0.96 h⁻¹ over the perturbations tested. **Held open** — whether any mechanism in the cell *represents* the threshold; nothing measured here locates one.
5. Test designed: take canon's strongest and most specific claim (the middle moves with system state), and find a bacterial quantity measured under several system states.
6. Data (unfiltered): the table above. Note the direction of the flagellar knockout: removing a protein burden moves the threshold *up*, so the movement is not homeostatic restoration toward a preferred value but a straightforward consequence of freed proteome.
7. Variable Principle applied: this is the one place in the sweep where canon's claim meets a matching measurement, and the honest statement is narrow. What is measured is that an observable optimum moves, predictably, under a stated law. What is *not* measured is that the cell adjusts anything: the same data are fully reproduced by a fixed allocation rule whose optimum happens to sit elsewhere when the constraints change. Canon's "living thermostat" reading is not forced.
8. Model update (Capsule: what the failed parts contribute): Layer I.D can and should carry λ_ac ≈ 0.76 h⁻¹ as its first measured bacterial instance, with the shift law λ(φ_Z) = λ_ac(1 − φ_Z/φ_max). The part that fails is canon's *mechanism*: "the living organism adjusts its set-point" is not what the measurement shows. A moving optimum of a fixed rule is indistinguishable, in this dataset, from a fixed rule with a moving optimum — and canon's own contrast with a thermostat requires that distinction to be made.
9. Documented: this file. Attempted DPR assignment: **DETECT** → the cell's sensing of its own growth rate; **PROCESS** → reallocation between respiratory and fermentative proteome sectors; **RESPOND** → acetate excretion. The first step has no measured referent: no molecule in *E. coli* has been shown to measure λ, and the model that predicts every data point contains no growth-rate sensor. The threshold in the data is a kink in a constrained-optimum curve, not a triggered switch. **DPR mapping: applied after the fact** — and specifically, the DETECT step is unoccupied.
10. Next baseline: whether λ_ac shifts in the same way under a perturbation that alters *respiratory* rather than ribosomal proteome cost would discriminate the two readings in step 8.

## Forcing Test

- Test A (Ground): Well grounded. One quantity, one threshold-linear law, seven measured threshold values with uncertainties.
- Test B (Uniqueness): Not unique. Canon's "the middle shifts" is consistent with these data, but so is proteome-allocation optimisation with no middle and no adjustment. Consistency with one framework does not select it.
- Test C (Direction): Measured and signed: burden down → threshold up; burden up → threshold down. Canon predicts movement but not its sign, so it does not earn this result.
- Test D (Falsifiability): The measurement is highly falsifiable. Canon's claim, as written, is not: because canon names no quantity, no observed value of λ_ac could contradict it.
- **Outcome:** `live-hypothesis`. This is the best available confirming instance of Layer I.D, and it still does not force canon's mechanism.

## Anti-Operation (the gap this opens)

Canon's claim survives here only because it is too weak to be threatened. The gap: Layer I.D must name, for at least one system, the quantity that is at a middle and the direction the middle moves when a stated variable changes — otherwise every measured shift confirms it and no measured fixity could refute it, which makes it unfalsifiable in the same way `CLAIM-003` found Process Density unfalsifiable. The λ_ac dataset is offered as the test case: canon should state, before looking, whether removing a protein burden raises or lowers the middle.

## Narrative stripped (if any)

Removed: the Yin/Yang assignment (fermentation as Yang overextension, respiration as Yin) and the chess "draw" analogy. Neither is forced: the measured trade-off is between two proteome costs, is single-axis and continuous, and has no measured extremes of the kind Polarity requires. Also removed: the Three-States table's "Rigid Middle / Collapsed Middle" diagnostics, which have no measured counterpart here — an *E. coli* strain held below λ_ac is not dysfunctional, it is carbon-limited.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
