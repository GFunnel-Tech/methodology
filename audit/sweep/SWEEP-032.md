---
id: SWEEP-032
canon_ref: "v5.1 Appendix D, Biological & Scaling Laws, rows 'Kleiber’s Law' and 'Allometric Scaling Laws' (the registry's only entries for laws governing growth and composition across biological scales)"
canon_label: "Kleiber’s Law / Allometric Scaling Laws — biological quantity ∝ mass^k"
proposed_label: "Bacterial growth laws: ribosome mass fraction and translational elongation rate as functions of growth rate"
diff_state: methodology-gap
exclusion_diagnosis: not-reached
claim_outcome: live-hypothesis
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix D, Biological & Scaling Laws:

> "Kleiber’s Law | Metabolic rate ∝ mass^(3/4) | Across nearly all biological scales — from bacteria to whales. Per Correspondence: the same scaling law governs living systems across 27 orders of magnitude."
> "Allometric Scaling Laws | Biological quantity ∝ mass^k | Heart rate, lifespan, brain size, cellular density all follow power laws of mass with characteristic exponents. The mathematical signature of biological self-similarity."

Appendix D's header: "Per Layer III: biological systems are the highest-density expression of organized complexity. The following laws are the Process Density mechanism made visible."

**Split (RUNBOOK rule 4).** *Factual core graded here:* the laws governing growth and composition in living systems are power laws of *mass*, holding from bacteria upward.

*Framework mapping (not graded; see Narrative stripped):* "Per Correspondence"; "the mathematical signature of biological self-similarity".

Canon's registry contains **no law relating a bacterium's composition to its growth rate**. Its only bacteria-inclusive scaling claim is Kleiber's Law, whose universality is already graded `forced-no` in `audit/constants/CONST-kleiber-law.md` on measurements showing a prokaryotic exponent of 1.7–2.0, not 3/4.

## Reality shows

Reference organism: wild-type *Escherichia coli* K-12, exponential growth in saturating minimal media with varied carbon and nitrogen sources, plus antibiotic-inhibited and stationary-phase conditions.

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Range of growth rates probed | doubling time 20 minutes to 20 hours (λ from ~2 h⁻¹ down to near zero), plus stationary phase | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC5346290/ | 2026-09-28 |
| Relation between RNA/protein ratio (a measured proxy for ribosome mass fraction φ_Rb) and growth rate λ | **linear in the fast-growth regime λ > 0.7 h⁻¹**; the linear fit is explicitly restricted to that regime, and the relation departs from it below | as published (dashed linear fit to data) | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC5346290/ | 2026-09-28 |
| Cross-check that RNA/protein tracks ribosome content | ribosome abundance φ_Rb by quantitative mass spectrometry "correlate[s] well" with the RNA/protein ratio | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC5346290/ | 2026-09-28 |
| Dependence of translational elongation rate on the translational apparatus | Michaelis–Menten in the abundance of ternary complexes, established for all growth conditions tested | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC5346290/ | 2026-09-28 |
| Elongation rate close to zero growth (20 h doubling) and in stationary phase | > 9 amino acids/s; ~8 aa/s in stationary phase | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC5346290/ | 2026-09-28 |
| Independent agreement of those elongation rates with earlier work by different methods | in agreement with sporadic previous studies by several different methods | as published | measured-reproduced | https://pmc.ncbi.nlm.nih.gov/articles/PMC5346290/ | 2026-09-28 |
| How slow-growing cells maintain elongation rate | by "a drastic reduction in the fraction of active ribosomes" — f_active falls rather than elongation slowing | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC5346290/ | 2026-09-28 |
| Inactive-ribosome protein mass fraction, moderate to fast growth (λ > 0.5 h⁻¹) | constant at 1.1% of the proteome; rises linearly as λ falls below 0.5 h⁻¹ | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC5346290/ | 2026-09-28 |
| Peak burden of inactive ribosome equivalents | over 20% of the proteome for some conditions | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC5346290/ | 2026-09-28 |
| Effect of chloramphenicol, tetracycline, erythromycin | a substantial reduction in the pool of *active* ribosomes, "instead of slowing down translational elongation as commonly thought" | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC5346290/ | 2026-09-28 |
| Existence of intrinsic constraints on proteome allocation that make growth rate and gene expression mutually predictive | established phenomenologically; the theory "accurately predict[s] how cell proliferation and gene expression affect one another" | as published | measured-single | https://pubmed.ncbi.nlm.nih.gov/21097934/ | 2026-09-28 |
| Extrapolated "useless protein" fraction at which growth rate vanishes | φ_max ≈ 47% | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC4843128/ | 2026-09-28 |
| Slope and intercept of φ_Rb versus λ as audited numbers with uncertainties | not retrieved | n/a | held-open | the fit parameters sit in the paper's Supplementary Table 3 and figure axes, not in the retrievable text; the *form* of the relation and its regime of validity are recorded instead, and no slope is supplied from memory | 2026-09-28 |

## Scientific Inquiry run

1. Question (precise): Does a canonical item hold the measured bacterial growth laws — in particular the relation between ribosome fraction and growth rate — and does DETECT → PROCESS → RESPOND fit the measured mechanism?
2. What an answer must look like: canon's relevant registry rows; the measured form of the ribosome-fraction/growth-rate relation with its regime of validity; and a DPR assignment tested for boundaries.
3. Falsifiability condition: the `methodology-gap` grade fails if any canonical item relates a bacterium's macromolecular composition to its growth rate. Appendix D's registry, Appendix A's stages and Layer III's cell table contain no such item; the registry's scaling variable is *mass*, not growth rate.
4. Variables: measurable / bounded / held open: **Measurable** — RNA/protein ratio, φ_Rb, elongation rate, f_active, doubling time. **Bounded** — linearity of φ_Rb in λ holds for λ > 0.7 h⁻¹; inactive fraction constant at 1.1% for λ > 0.5 h⁻¹; elongation rate stays above ~8 aa/s everywhere. **Held open** — the numeric slope and intercept.
5. Test designed: search canon for any composition–growth-rate law; then fetch the measured relation across the widest available growth-rate range, deliberately including slow growth, where a claimed linear law would be most likely to break.
6. Data (unfiltered): the table above. Recorded in full, including the part that spoils the tidy version: the linear growth law is **not** universal — it is fitted only above 0.7 h⁻¹, and below that the cell holds elongation rate nearly constant by idling ribosomes instead, with the idle pool reaching over 20% of the proteome.
7. Variable Principle applied: it would be easy, and wrong, to record "ribosome fraction is linear in growth rate" as a law of bacterial physiology. The measurement supports it in a stated regime and shows a different mechanism outside that regime. The regime boundary (λ ≈ 0.5–0.7 h⁻¹) is itself the measured content, and it is recorded rather than smoothed away.
8. Model update (Capsule: what the failed parts contribute): Appendix D should carry a bacterial growth law whose independent variable is growth rate, not mass — and it should carry the regime boundary with it. The failed part contributes the third instance of one pattern in Appendix D: a relation measured in one regime or taxon is stated as covering all of biology (Kleiber, Hayflick per SWEEP-030, and now the absence of any growth-rate law at all).
9. Documented: this file. Attempted DPR assignment: **DETECT** → the cell's assessment of nutrient sufficiency; **PROCESS** → reallocation of proteome between ribosomal and metabolic sectors; **RESPOND** → the new ribosome fraction and growth rate. The DETECT step has a partial molecular referent — ppGpp does signal amino-acid sufficiency (SWEEP-033) and does regulate rRNA synthesis — so unlike SWEEP-026 and SWEEP-031, this assignment is not empty. But the measured law itself is not a regulated response to a detected signal: it is a *constraint*, a relation that must hold because ribosomes make ribosomes. The distinction matters because the slow-growth data discriminate them: if the cell were responding to a detected nutrient level, elongation rate would be the natural thing to adjust; instead it is held nearly constant and the active *fraction* absorbs the change, which is what a constraint plus idling looks like, not a set-point. **DPR mapping: applied after the fact** — the arrow canon needs (signal → response) points the wrong way for a law that is a conservation constraint.
10. Next baseline: the numeric fit parameters, and a measurement of what sets the 0.5–0.7 h⁻¹ regime boundary. Re-review 2027-09-24.

## Forcing Test

- Test A (Ground): Grounded across a 60-fold range of doubling times, with elongation rates independently reproduced by earlier methods.
- Test B (Uniqueness): Canon's mass-based allometry is not unique and is not the relevant law here. The growth-rate-based relation is well established in its regime; it is not unique as a *universal* law, because it demonstrably fails below 0.7 h⁻¹.
- Test C (Direction): Measured and signed: faster growth → higher ribosome fraction, above the regime boundary; below it, ribosome fraction changes little and the active fraction falls instead.
- Test D (Falsifiability): Highly falsifiable and partly falsified — which is why the regime restriction is load-bearing and is recorded.
- **Outcome:** `live-hypothesis`. Canon's registry makes no claim here to be confirmed or refuted; its implicit claim, that mass-based allometry is the form biological scaling laws take, is not supported for bacteria.

## Anti-Operation (the gap this opens)

The idle-ribosome result opens a gap that reaches Layer I.F and Layer III together. A slow-growing *E. coli* devotes over 20% of its proteome to ribosomes that are not translating. On canon's own accounting that is neither "perfect process" (it is not optimised) nor "the draw" (it is not an equilibrium being held) — it is measured, reproducible waste that buys readiness. Canon has no item for capacity held in reserve at a cost, and Layer I.F's claim that the observation constraint pushes every system into one of two configurations has, here, a counterexample sitting in the majority of *E. coli*'s natural growth range.

## Narrative stripped (if any)

Removed: "Per Correspondence: the same scaling law governs living systems across 27 orders of magnitude" and "the mathematical signature of biological self-similarity". The first is graded `forced-no` already in `CONST-kleiber-law.md`; this record adds that the law that *does* govern bacterial composition uses a different independent variable entirely, so the failure is not a matter of the exponent's value but of which variable is scaling. The second phrase attributes self-similarity to power laws as such; a power law fitted over a restricted range is evidence of neither similarity nor its absence.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
