---
id: SWEEP-023
canon_ref: "v5.1 Layer I.E, 'Resolution Four — The Spiral Runs On Gradients, Not Energy In The Naive Sense'; with v5.1 Appendix A Stages 13 and 21"
canon_label: "The Electron Transport Chain establishes a polarity whose controlled collapse does work"
proposed_label: "Transmembrane proton electrochemical potential difference (Δp) and its two components"
diff_state: methodology-gap
exclusion_diagnosis: not-reached
claim_outcome: forced-fill
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Layer I.E, Resolution Four:

> "The Electron Transport Chain produces ATP not because energy was created but because a polarity was established and then collapsed in a controlled fashion. The energy was already there. The polarity is what made it available to do work."

v5.1 Appendix A Stage 13: "Chemiosmosis at Alkaline Hydrothermal Vents | Natural proton gradients across mineral membranes. Energy harvested from polarity."
v5.1 Appendix A Stage 21: "Electron Transport Chain | ... Cascade through Complexes I → III → IV pumps protons. Polarity created."

**Split (RUNBOOK rule 4).** *Factual core graded here:* a proton gradient across the membrane is established by respiration and its controlled collapse is what makes energy available to do work.

*Framework mapping (not graded; see Narrative stripped):* "Polarity" as Hermetic Principle IV; "the collapse IS the seed".

Canon treats the gradient as a single, scalar "polarity". It names no components, no magnitude, and no consumers other than ATP synthase.

## Reality shows

Reference organism: *Escherichia coli* K-12 MG1655 (fermentative growth, acid-stress series) and *E. coli* strains used in flagellar-motor voltmetry.

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Δp (total proton motive force), MG1655, no acid stress (pH_ex 7.6 → 6.5 over 3.5 h) | −103 mV | as published (single condition mean) | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC13273468/ | 2026-09-28 |
| ΔΨ (membrane potential) and ΔpH, same condition | ΔΨ = −105 mV; ΔpH ≈ 0 | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC13273468/ | 2026-09-28 |
| Δp, ΔΨ, ΔpH under mild acid stress (pH_ex 6.5), μ = 0.47 h⁻¹ | Δp = −157 mV; ΔΨ = −94 mV; ΔpH = 1.02 units (= −63 mV) | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC13273468/ | 2026-09-28 |
| Δp, ΔΨ, ΔpH under moderate acid stress (pH_ex 5.8), μ = 0.22 h⁻¹ | Δp = −209 mV; ΔΨ = −109 mV; ΔpH = 1.62 units (= −100 mV) | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC13273468/ | 2026-09-28 |
| Proton flux rate J(H⁺) and membrane proton conductance, no stress vs moderate stress | 3.68 → 1.04 mM min⁻¹; 35.7 → 5.0 nM min⁻¹ mV⁻¹ per 10⁹ cells | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC13273468/ | 2026-09-28 |
| Nernst factor Z = RT/F used to convert ΔpH to mV at 37 °C | 61.1 mV per pH unit | exact at stated T | derived | https://pmc.ncbi.nlm.nih.gov/articles/PMC13273468/ | 2026-09-28 |
| Interconversion of the two components at fixed total: ΔΨ driven 125 mV → 0 mV by valinomycin while ΔpH rises 35 → 70 mV; beyond that point ΔpH alone carries Δp | ΔΨ 125 → 0 mV; ΔpH 35 → 70 mV | as published | measured-single | https://pubmed.ncbi.nlm.nih.gov/6354293/ | 2026-09-28 |
| Plateau in total Δp across external pH 5.5–6.6 "where delta pH is converted to delta psi" | peak-plateau over ~1.1 pH units | as published | measured-single | https://pubmed.ncbi.nlm.nih.gov/6354293/ | 2026-09-28 |
| Periplasmic pH tracks external pH exactly; cytoplasmic pH falls to 5.6–6.5 within 10–20 s of an external shift 7.5 → 5.5, then recovers | as stated | 4 s time resolution | measured-single | https://pubmed.ncbi.nlm.nih.gov/17545292/ | 2026-09-28 |
| Lateral PMF homogenization along the membrane is faster than proton diffusion; motor response time constants τ↓ ≈ 100 ms, τ↑ ≈ 30 ms; membrane capacitance C ≈ 10⁻¹⁴ F; respiration source V_r ≈ 360 mV | as stated | circuit-model inference from measured motor speeds | derived | https://pmc.ncbi.nlm.nih.gov/articles/PMC11114223/ | 2026-09-28 |
| Complete list of Δp consumers in *E. coli* with a measured per-consumer budget share | not retrieved | n/a | held-open | no primary source reached this run that partitions Δp consumption across ATP synthase, flagellar motor, transport and leak in one measurement | 2026-09-28 |

## Scientific Inquiry run

1. Question (precise): Does a canonical item hold the measured proton motive force of a bacterial cell — its magnitude, its two components, and its consumers — and does DETECT → PROCESS → RESPOND fit the measured mechanism?
2. What an answer must look like: canon's wording located; measured Δp with its ΔΨ and ΔpH split under stated conditions; a named assignment of each DPR operation to a physical step, with a statement of whether a boundary exists there.
3. Falsifiability condition: canon's factual core fails if ATP synthesis proceeds at measured rates with the proton gradient abolished, or if no transmembrane proton electrochemical difference is measurable in a respiring cell. It did not fail.
4. Variables: measurable / bounded / held open: **Measurable** — ΔΨ, ΔpH, Δp, J(H⁺), membrane conductance. **Bounded** — Δp between about −100 and −210 mV across the conditions retrieved. **Held open** — the per-consumer partition of Δp; whether any canonical item is intended to hold the component structure.
5. Test designed: locate the canonical text; fetch measured ΔΨ/ΔpH/Δp for *E. coli* K-12 from a primary paper; fetch an independent demonstration that the two components interconvert; then attempt the DPR assignment step by step and record where a boundary exists.
6. Data (unfiltered): the table above. Note the direction: as acid stress rises, growth rate falls (0.47 → 0.22 → 0.16 h⁻¹) while total Δp *rises* in magnitude (−157 → −209 mV) and proton flux falls. High Δp is therefore not a proxy for good performance.
7. Variable Principle applied: canon's single word "polarity" is one measured quantity split into two that trade off. The trade-off is measured; the budget of consumers is held open and is not filled here.
8. Model update (Capsule: what the failed parts contribute): canon's Resolution Four survives as stated and is the strongest-supported factual core in this sweep. What fails is its resolution: a scalar "polarity" cannot express the measured fact that ΔΨ and ΔpH substitute for one another at roughly conserved total. The failed part contributes a concrete metric where canon has a word.
9. Documented: this file. Attempted DPR assignment: **DETECT** → binding of a periplasmic proton at the a/c interface; **PROCESS** → transmembrane translocation; **RESPOND** → release into the cytoplasm. Each of these is a single elementary step of one reaction coordinate. There is no sensor, no comparison against a set-point, and no branch point, so nothing in the measured mechanism distinguishes the three. The assignment is arbitrary: the same three labels could be applied in any order, or to the two half-reactions of quinone oxidation instead, with equal fit. **DPR mapping: applied after the fact.**
10. Next baseline: a measured partition of Δp consumption in one organism under one condition would let the "consumers" row close. Re-review 2027-09-24.

## Forcing Test

- Test A (Ground): Grounded. Δp, ΔΨ and ΔpH are directly measured in *E. coli* K-12 under stated conditions.
- Test B (Uniqueness): For the narrow claim — that a transmembrane proton electrochemical difference is the obligatory intermediate between respiration and ATP synthesis in *E. coli* — no alternative candidate survives measurement. Unique. For canon's broader reading (every functional process runs on a polarity), not tested here.
- Test C (Direction): Directional and measurable: protons are pumped outward, Δp is negative inside, and collapse through ATP synthase is what phosphorylates ADP.
- Test D (Falsifiability): Falsifiable and repeatedly tested by uncoupler and ionophore experiments, including the valinomycin series above.
- **Outcome:** `forced-fill` for the narrow chemiosmotic claim. The *component structure* canon omits is a `methodology-gap`, not a failure of the claim.

## Anti-Operation (the gap this opens)

Two gaps. (i) If ΔΨ and ΔpH substitute for one another at near-constant total, then the regulated quantity is the sum, and canon has no item that names a regulated sum — Layer I.D's "dynamic middle" is the nearest, but its domain table assigns the Biological row to heart rate variability, not to bacterial bioenergetics, so the measured instance has no canonical home. (ii) Measured Δp rises as growth rate falls. Any framework reading "larger gradient" as "better process" is falsified by this dataset; canon does not state which direction it predicts.

## Narrative stripped (if any)

Removed: "the collapse IS the seed" and "Per Polarity: every functional process in the universe runs on a polarity." The first is a metaphor about succession that the measurement neither forces nor contradicts — proton return through ATP synthase does not seed a new gradient, it consumes the existing one, and the next gradient is re-established by continued substrate oxidation, not by the collapse. The second is a universal generalisation from one case; reality here supplies one confirming instance and no warrant for "zero exceptions".

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
