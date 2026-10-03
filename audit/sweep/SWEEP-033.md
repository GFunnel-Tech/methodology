---
id: SWEEP-033
canon_ref: "v5.1 Layer I.C Domain 9 — Biological Process, the Algorithm row ('DETECT: Internal deviation or external threat. PROCESS: Cellular response — gene expression, protein synthesis, metabolic shift, immune activation. RESPOND: Adapted state, corrected equilibrium.')"
canon_label: "Domain 9 Biological Process Algorithm — DETECT internal deviation → PROCESS cellular response → RESPOND adapted state"
proposed_label: "Stringent response, sporulation and persistence as measured starvation-signalling mechanisms"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: live-hypothesis
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Layer I.C, Domain 9 — Biological Process, Algorithm row:

> "DETECT: Internal deviation or external threat. PROCESS: Cellular response — gene expression, protein synthesis, metabolic shift, immune activation. RESPOND: Adapted state, corrected equilibrium."

Domain 9, Homeostasis row: "The organism continuously monitors deviation, processes the signal through cascading regulatory pathways, and responds to correct. Equilibrium is dynamic correction at every moment. **The organism that achieves stasis is dead.**"

**Split (RUNBOOK rule 4).** *Factual core graded here:* a cell detects deviation, processes the signal through regulatory pathways, and responds with an adapted state; a cell in stasis is dead.

*Framework mapping (not graded; see Narrative stripped):* the Three-Kingdoms assignment (Third → Second → First); "Immune Process as Shepherd's Way"; "corrected equilibrium".

Canon names no bacterial stress signal, no alarmone, no dormant state and no sporulation. Its dormancy-adjacent items are the Hayflick Limit (graded in SWEEP-030) and apoptosis (graded in SWEEP-034).

## Reality shows

Reference organisms: *Escherichia coli* (stringent response, persisters) and *Bacillus subtilis* (sporulation) — the latter named because it is the best-measured sporulation system and *E. coli* does not sporulate.

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Intracellular ppGpp concentration, *E. coli*, exponential phase | ~40 µM | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC5591245/ | 2026-09-28 |
| ppGpp on entry to stationary phase, then at steady stationary phase | up to 800 µM, then stabilising at 150 µM | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC5591245/ | 2026-09-28 |
| Total dynamic range of ppGpp and pppGpp across the growth curve and acute stringent response (mupirocin, 150 µg/ml) | 40-fold and ≥ 8-fold respectively | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC5591245/ | 2026-09-28 |
| GTP over the same window | declines steadily from 1100 µM in mid-logarithmic phase | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC5591245/ | 2026-09-28 |
| Half-life of the signal molecules | ppGpp 30–200 s (estimated range); pppGpp ~10 s; ATP ~0.1 s | as published, citing primary kinetics | derived | https://pmc.ncbi.nlm.nih.gov/articles/PMC5591245/ | 2026-09-28 |
| Downstream effects of (p)ppGpp | repression of stable RNA synthesis, growth and cell division; promotion of amino-acid biosynthesis, survival, persistence and virulence, via interaction with RNA polymerase and biosynthetic factors | as published | derived | https://pmc.ncbi.nlm.nih.gov/articles/PMC9965611/ | 2026-09-28 |
| Persister frequency in *E. coli* | "approximately one in a million" survive prolonged antibiotic exposure | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC1482909/ | 2026-09-28 |
| Persister frequency conferred by the *hipA7* allele | ca. 10% of cells | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC1482909/ | 2026-09-28 |
| Nature of the HipA-induced state | inhibition of protein, RNA and DNA synthesis in vivo; a transient dormant state in a sizable fraction, a prolonged dormant state in the rest, **fully reversible by expression of the cognate antitoxin** *hipB* | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC1482909/ | 2026-09-28 |
| Dissociation of two persistence-related activities | *hipA7* confers high persistence *without* markedly inhibiting protein synthesis, so the two functions are separable | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC1482909/ | 2026-09-28 |
| Time course of the *B. subtilis* sporulation master regulator Spo0A | level and activity increase **gradually over the first 2 h** of sporulation, both under nutrient limitation and under artificial kinase induction | as published | measured-single | https://pubmed.ncbi.nlm.nih.gov/16166384/ | 2026-09-28 |
| Whether the gradualness matters | yes: sporulation can be triggered at high efficiency by inducing any one of three histidine kinases, and the gradual increase "plays a critical role in triggering sporulation and requires the action of the phosphorelay" | as published | measured-single | https://pubmed.ncbi.nlm.nih.gov/16166384/ | 2026-09-28 |
| Measured asymmetry between abrupt and gradual induction | abrupt induction of Spo0A* yields ≈5% sporulation; gradual KinA phosphorelay accumulation yields ≈52% | as reported, citing Fujita & Losick 2005 | derived | https://pmc.ncbi.nlm.nih.gov/articles/PMC13496463/ | 2026-09-28 |
| Whether *E. coli* cells in stationary phase or persistence are dead | no: they retain measurable elongation rate ~8 aa/s (SWEEP-032) and persisters resume growth on antibiotic removal | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC5346290/ | 2026-09-28 |

## Scientific Inquiry run

1. Question (precise): Does Domain 9's algorithm hold the measured bacterial stress and dormancy machinery, and does DETECT → PROCESS → RESPOND fit the measured mechanism, or is it applied after the fact?
2. What an answer must look like: canon's algorithm quoted; a measured signal molecule with concentrations and a dynamic range; a measured sensor; measured downstream effects; and a DPR assignment in which each label is attached to a named molecule and the boundaries between them are tested.
3. Falsifiability condition: canon's algorithm fails here if the measured starvation response has no identifiable detection step, or if detection, processing and response cannot be perturbed independently. Neither holds: they can.
4. Variables: measurable / bounded / held open: **Measurable** — ppGpp and pppGpp concentrations and half-lives, GTP, persister frequency, Spo0A time course, sporulation efficiency. **Bounded** — ppGpp 40–800 µM; persister frequency 10⁻⁶ to 10⁻¹ depending on allele. **Held open** — the molecular identity of what makes an individual cell become a persister (the cited work separates the activities but does not resolve the trigger).
5. Test designed: take canon's most mechanism-shaped claim (the Domain 9 algorithm) and test it against the best-measured bacterial signalling cascade, looking specifically for whether a physical sensor exists.
6. Data (unfiltered): the table above, including the two rows that cut against canon: persistence is reversible dormancy, not correction toward equilibrium, and *hipA7* separates dormancy from growth inhibition, so "the response" is not one thing.
7. Variable Principle applied: the trigger of individual persistence is held open rather than attributed to ppGpp, even though ppGpp promotes persistence — promotion is measured, causation of the single-cell switch is not.
8. Model update (Capsule: what the failed parts contribute): Domain 9's algorithm survives here better than any other canonical item in this sweep. What fails is the Homeostasis row's "The organism that achieves stasis is dead." A bacterial spore and a persister are measurably near-static and measurably not dead — a spore is the limiting case of stasis-as-survival strategy. The failed clause contributes a genuine correction: canon's identification of stasis with death is contradicted by the most successful survival mechanisms in the domain canon is describing.
9. Documented: this file. Attempted DPR assignment, done step by step with the boundary test: **DETECT** → an uncharged tRNA occupying the ribosomal A site, sensed by RelA, and separately the phosphorelay kinases (KinA and two others) that sense nutrient limitation in *B. subtilis*. These are *named molecules whose job is sensing*, with a measured stimulus and a measured output; a mutation in the sensor abolishes detection while leaving the downstream machinery intact. **PROCESS** → synthesis of (p)ppGpp at 40 → 800 µM, a diffusible second messenger with a measured half-life of 30–200 s, or graded phosphorylation of Spo0A over 2 h. The signal is a *distinct chemical species* from both the stimulus and the effector — this is the strongest evidence of a real boundary anywhere in this sweep. **RESPOND** → ppGpp binding RNA polymerase, repressing stable RNA synthesis and inducing amino-acid biosynthesis; or Spo0A crossing the commitment threshold and initiating sporulation. Each of the three steps is separately perturbable and separately measurable. **DPR mapping: fits.** Two qualifications, recorded so the fit is not overclaimed: (i) the fit is with a *signal-transduction* system, which is the class of biological mechanism DPR was abstracted from, so this is close to a definitional success rather than a prediction; (ii) canon's RESPOND is "corrected equilibrium", and the measured response to starvation is not correction — the cell does not fix the nutrient shortage, it shuts down. The *shape* fits and the *direction* does not.
10. Next baseline: the single-cell persistence trigger.

## Forcing Test

- Test A (Ground): Well grounded. Concentrations, half-lives, dynamic ranges, frequencies and time courses, all from primary measurement.
- Test B (Uniqueness): The mechanism is uniquely identified (RelA/SpoT–ppGpp–RNAP is the stringent response). Canon's three-step abstraction is not unique: any signal-transduction description partitions the same cascade the same way, so the fit does not discriminate canon from standard molecular biology.
- Test C (Direction): Measured direction runs against canon's stated endpoint. Canon says "corrected equilibrium"; measurement shows growth arrest, reversible dormancy, and in *B. subtilis* an irreversible developmental commitment. None of these is a correction.
- Test D (Falsifiability): Falsifiable. Canon's algorithm is confirmed in shape here; its "corrected equilibrium" endpoint and its "stasis is death" clause are falsified.
- **Outcome:** `live-hypothesis`. This is the sweep's best fit for DPR, and it earns canon less than it appears to: the fit is with the one class of mechanism from which the abstraction was drawn, and the specific predictions canon attaches to it (correction, stasis = death) fail.

## Anti-Operation (the gap this opens)

The gradual-versus-abrupt result (≈52% versus ≈5% sporulation for the same final regulator level) opens a gap canon cannot express. The *rate of change* of a signal, not its level, determines the outcome — the cell integrates a trajectory. Canon's algorithm is a state machine: DETECT, PROCESS, RESPOND has no place to hold a time derivative, and Layer I.D's "the middle moves" describes the set-point moving, not the *speed* of approach mattering. Any framework claiming one invariant algorithm must say where history-dependence lives.

## Narrative stripped (if any)

Removed: the Three-Kingdoms assignment "Third (homeostatic regulatory intelligence) → Second (genetic code, signaling pathways) → First (cellular machinery)". The measured cascade runs in the opposite order from canon's hierarchy — an uncharged tRNA (First Kingdom machinery) is the stimulus, and the regulatory outcome follows — and no measurement reaches "regulatory intelligence". Removed: "Immune Process as Shepherd's Way ... Memory formation = Shepherd's Way Steps 06–07 at biological level"; nothing in the bacterial stringent response forms memory, and reality neither forces nor contradicts the management-cycle mapping.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
