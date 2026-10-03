---
id: SWEEP-030
canon_ref: "v5.1 Appendix D, Biological & Scaling Laws, row 'Hayflick Limit'; with v5.1 Layer III, 'The Cell — All Seven Hermetic Principles in One Unit', Rhythm row"
canon_label: "Hayflick Limit — ~50 cell divisions before senescence; the cell cycle as a bounded, repeating rhythm"
proposed_label: "Bacterial division timing and the measured adder rule for size homeostasis"
diff_state: conflict
exclusion_diagnosis: reached-conflicting
claim_outcome: forced-no
intake_result: adjusted
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix D, Biological & Scaling Laws:

> "Hayflick Limit | ~50 cell divisions before senescence | Built-in cellular apoptosis trigger. Per Domain 9: the mechanism by which the cell complies with Step 07 (Repetition) — the cycle is bounded and the next baseline is clean."

v5.1 Layer III, the cell table, Rhythm row: "Cell cycle: growth → replication → division → growth. Circadian rhythm. All cellular processes oscillate."

**Split (RUNBOOK rule 4).** *Factual core graded here:* the cell cycle is bounded at roughly 50 divisions, after which senescence follows; this bound is the mechanism by which "the cell" completes a bounded cycle.

*Framework mapping (not graded; see Narrative stripped):* "Per Domain 9: ... Step 07 (Repetition) ... the next baseline is clean"; Rhythm as a Hermetic principle.

The registry states this as a *biological & scaling law*, alongside Kleiber's Law whose "bacteria to whales" claim is already graded `forced-no` in `audit/constants/CONST-kleiber-law.md`. Canon names no size-control rule, no division protein, and no bacterial division timing.

## Reality shows

Reference organisms: *Escherichia coli* and *Bacillus subtilis* (adder, microfluidic single-cell); *Caulobacter crescentus* (independent adder confirmation); *E. coli* (divisome).

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Size-homeostasis rule, *E. coli* and *B. subtilis*, hundreds of thousands of cells in a microfluidic "mother machine" across a wide range of steady-state growth conditions | "cells add a constant volume each generation, irrespective of their newborn sizes", i.e. the constant-Δ ("adder") model | as published | measured-reproduced | https://pubmed.ncbi.nlm.nih.gov/25544609/ | 2026-09-28 |
| Same rule, independently, in *E. coli* and the evolutionarily distant *Caulobacter crescentus*, by single-cell microscopy and modelling | cells "grow, on average, the same amount between divisions, irrespective of cell length at birth"; "direct experimental evidence disproving the critical size paradigm" | as published | measured-reproduced | https://pubmed.ncbi.nlm.nih.gov/25480302/ | 2026-09-28 |
| Number of parameters needed to reproduce all growth and division distributions in both species, in all conditions, with no adjustable parameters | two: the growth rate λ and the added size Δ | as published | measured-reproduced | https://pubmed.ncbi.nlm.nih.gov/25544609/ | 2026-09-28 |
| Coefficient of variation, division size vs generation time | ~10% vs 40–60% | as published | measured-reproduced | https://pubmed.ncbi.nlm.nih.gov/25544609/ | 2026-09-28 |
| Ordering of variability across six rescaled distributions | septum position s₁/₂ narrowest; added size Δ widest; all collapse when rescaled by their means (scale invariance) | as published | measured-reproduced | https://pubmed.ncbi.nlm.nih.gov/25544609/ | 2026-09-28 |
| Predicted and confirmed mother–daughter generation-time correlation under the adder | −1/4; autocorrelations of birth size, division size and generation time decay by a factor 2 each generation | as published | measured-reproduced | https://pubmed.ncbi.nlm.nih.gov/25544609/ | 2026-09-28 |
| *B. subtilis* average doubling times across the four conditions used | 16.9 to 38.9 minutes | as published | measured-reproduced | https://pubmed.ncbi.nlm.nih.gov/25544609/ | 2026-09-28 |
| Where in the cycle the constant extension is implemented | "at or close to division" | as published | measured-reproduced | https://pubmed.ncbi.nlm.nih.gov/25480302/ | 2026-09-28 |
| Rate-limiting component for the onset of constriction, *E. coli*, moderately fast growth, by quantitative up- and down-regulation in microfluidics | FtsZ numbers are rate-limiting; FtsN and FtsA are **not** at physiological levels (FtsN accelerates and FtsA inhibits only when strongly overexpressed; FtsA becomes inhibitory at 50% overexpression) | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC11569214/ | 2026-09-28 |
| FtsZ polymer treadmilling speed | ~30 nm/s "in all bacterial species examined so far" | as published, across 6 cited studies | derived | https://pmc.ncbi.nlm.nih.gov/articles/PMC12260396/ | 2026-09-28 |
| Speed of the septal-PG synthase on its own track, after leaving the Z-track | ~8 to 9 nm/s | as published | derived | https://pmc.ncbi.nlm.nih.gov/articles/PMC12260396/ | 2026-09-28 |
| Whether FtsZ is required throughout constriction | essential for the early stage, **dispensable for the late stage** of cell wall constriction | as published | derived | https://pmc.ncbi.nlm.nih.gov/articles/PMC12260396/ | 2026-09-28 |
| A division-count bound (Hayflick-type) in *E. coli* or *B. subtilis* | none found; the adder papers track hundreds of thousands of cells over many generations in steady state with no senescence bound reported | n/a | held-open | absence of a reported bound in these datasets is not the same as a measurement that no bound exists; recorded as held-open rather than as a measured zero | 2026-09-28 |

## Scientific Inquiry run

1. Question (precise): Does a canonical item hold bacterial division timing and size control, and does DETECT → PROCESS → RESPOND fit the measured mechanism?
2. What an answer must look like: canon's division-related rows quoted; the measured size-control rule with independent reproduction; measured division-machinery rates; and a DPR assignment tested for boundaries.
3. Falsifiability condition: canon's Appendix D row fails, as a *biological law*, if the organisms in the same registry's other rows ("bacteria to whales") show no division-count bound and instead follow a different, measured rule. Two independent 2014–2015 studies establish the different rule.
4. Variables: measurable / bounded / held open: **Measurable** — Δ, λ, CVs, correlation coefficients, treadmilling speed, doubling times. **Bounded** — *B. subtilis* doubling 16.9–38.9 min in the conditions used; FtsZ treadmilling ~30 nm/s. **Held open** — whether any division-count bound exists in bacteria.
5. Test designed: establish the measured bacterial size-control rule from two independent labs; establish which divisome component is rate-limiting; then test canon's row against both.
6. Data (unfiltered): the table above, including the two results that complicate a simple story — FtsZ is rate-limiting for constriction *onset* yet dispensable for late constriction, and the added size Δ is the *widest* distribution, not the narrowest, so the adder is a robust rule implemented by a noisy quantity.
7. Variable Principle applied: canon fills "how is the cell cycle bounded" with a division count taken from human fibroblasts. Measurement in bacteria gives a different kind of bound entirely — a constant size increment per generation, which bounds *size* not *lineage*. The bacterial division-count question is held open, not answered with a zero.
8. Model update (Capsule: what the failed parts contribute): Appendix D's Hayflick row must be restricted to the cells in which it was measured, and a second row added for the bacterial rule: size homeostasis by constant added size Δ, with λ and Δ sufficient to generate all other distributions. The failed part contributes the general finding that Appendix D's registry mixes measurements from one taxon with claims about all life, exactly as `CONST-kleiber-law.md` found; this is now the second instance and it is a pattern, not an isolated slip.
9. Documented: this file. Attempted DPR assignment: **DETECT** → accumulation of FtsZ to the threshold that triggers constriction onset (measured to be rate-limiting); **PROCESS** → Z-ring treadmilling at ~30 nm/s corralling the FtsWIQLB–FtsN synthase complex; **RESPOND** → septal PG synthesis and constriction. This assignment has a *partly* real boundary, and it is worth being precise about which part. The PROCESS and RESPOND steps are separable: the synthase demonstrably leaves the Z-track and continues on its own at 8–9 nm/s, and FtsZ becomes dispensable late — so there really are two distinct mechanisms with a measured hand-off. The DETECT step is not real: FtsZ accumulation is not a measurement of anything, it is a concentration rising until a polymerisation threshold is crossed, and crucially the *adder* rule that actually sets division timing has no molecular detector at all — Δ is a statistical regularity whose implementation is still open. **DPR mapping: after-the-fact overall, with one genuine internal boundary (Z-track → sPG-track) that DPR does not name.**
10. Next baseline: the molecular implementation of the adder; and a deliberate test for a division-count bound in a bacterium.

## Forcing Test

- Test A (Ground): Grounded, and the adder is independently reproduced in three species by two labs.
- Test B (Uniqueness): Canon's division-count bound is not unique and is not the bacterial mechanism; the adder is uniquely selected over sizer and timer by the cited data ("direct experimental evidence disproving the critical size paradigm").
- Test C (Direction): Measured and signed: a cell born small takes longer to divide (mother–daughter generation-time correlation −1/4), which is the adder's signature and the opposite of a timer's.
- Test D (Falsifiability): Falsifiable and failed, as a claim about "the cell".
- **Outcome:** `forced-no` for "the cell cycle is bounded by ~50 divisions" read as a general biological law. The Hayflick measurement itself is not challenged in the cells where it was made; its generalisation is.

## Anti-Operation (the gap this opens)

Canon's Hayflick row does double duty: it is offered as a *law* and as the mechanism by which the cell "complies with Step 07 (Repetition)". Removing its generality removes the only mechanism canon offers for bounded repetition at cellular scale, and the bacterial replacement does not restore it: the adder bounds *size*, and size homeostasis is not a completion criterion — an *E. coli* lineage in steady state never completes anything. Canon must either supply a different mechanism for Step 07 at cellular scale, or accept that Step 07 is an organisational prescription with no cellular correspondence, which weakens the Correspondence argument at the scale where canon presses it hardest.

## Narrative stripped (if any)

Removed: "Built-in cellular apoptosis trigger" and "the next baseline is clean". Replicative senescence in fibroblasts is not apoptosis (senescent cells persist and remain metabolically active), and nothing in the bacterial data supports a "clean baseline" — the adder's own scale-invariant distributions show variation carried forward and damped over generations rather than reset. Also removed: "All cellular processes oscillate" (Layer III Rhythm row). In steady-state exponential growth the measured quantities of a bacterial population do not oscillate; they are constant, and the single-cell cycle is a repeated increment, not an oscillation about a mean.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
