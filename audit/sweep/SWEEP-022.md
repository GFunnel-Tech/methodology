---
id: SWEEP-022
canon_ref: "v5.1 Layer I.G, Slime Mold Stack, Biological row (mentions 'methylation patterns') and v5.1 Appendix A Stage 26 ('Tissue Differentiation / Gene Expression — Same DNA, different expression')"
canon_label: "Slime Mold Stack — Biological row / Stage 26 Tissue Differentiation"
diff_state: methodology-gap
exclusion_diagnosis: not-reached
claim_outcome: stipulation
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Layer I.G, Slime Mold Stack, Biological row: surviving variants carry "the structural information of failed ones in regulatory regions, **methylation patterns**, transposable elements."

v5.1 Appendix A, Stage 26: "Tissue Differentiation / Gene Expression — **Same DNA, different expression.** Second Kingdom directs First Kingdom according to Third Kingdom regulatory context."

v5.1 Layer 0: "The cell type changes ... the code is invariant across all of them."

**Split (RUNBOOK rule 4).** *Factual core graded here:* canon's only account of differing states on one genome is *developmental differentiation in a multicellular organism*, and its only mention of methylation casts it as a residue of failed evolutionary paths. Neither reaches a measured bacterial fact: genetically identical cells in one clonal population holding different stable states. *Framework mapping (not graded):* "Second Kingdom directs First Kingdom according to Third Kingdom regulatory context."

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Methylated bases mapped genome-wide in a pathogenic E. coli strain (O104:H4) by single-molecule real-time sequencing, with strand-specific and per-position frequency information | 49,311 putative 6-methyladenine and 1,407 putative 5-methylcytosine positions | as published | measured-single | https://doi.org/10.1038/nbt.2432 | 2026-09-28 |
| Consequence of removing one methyltransferase-endonuclease system | global transcriptional changes and gene amplification — i.e. methylation state feeds back on expression, not only on restriction | qualitative, as published | measured-single | https://doi.org/10.1038/nbt.2432 | 2026-09-28 |
| Bistability of the E. coli lactose utilization network: phase diagram of internal states as inputs are varied | hysteretic (bistable) response in the wild-type network; convertible to an ultrasensitive graded response | as published | measured-single | https://doi.org/10.1038/nature02298 | 2026-09-28 |
| Persistence as a phenotypic switch: switching occurs between normally growing cells and slow-growing persister cells, and persistence is linked to pre-existing heterogeneity rather than to mutation (cells regrown from persisters remain sensitive) | mechanism established by single-cell microfluidics | qualitative, as published | measured-single | https://doi.org/10.1126/science.1099390 | 2026-09-28 |
| Probability that a non-growing E. coli MG1655 cell is a persister, estimated from single-cell observation of over one million cells with killing-curve calibration | 8.4e-2 | ± 2.2e-2 | measured-single | https://doi.org/10.7554/elife.79517 | 2026-09-28 |
| Range of persister (surviving cell) frequencies in bacterial populations as collected by the same single-cell study | 1e-6 to 1e-3 | range as published from prior work | measured-single | https://doi.org/10.7554/elife.79517 | 2026-09-28 |
| Medium dependence of persister frequency in post-exponential populations | about 100-fold higher in M9 than in LB for MG1655; about 10-fold for the MF1 strain | as published | measured-single | https://doi.org/10.7554/elife.79517 | 2026-09-28 |

## Scientific Inquiry run

1. Question (precise): Does a canonical item hold bacterial epigenetic and phenotypic memory — methylation, bistable switches, persistence — and does DPR fit the measured mechanism?
2. What an answer must look like: a canonical item covering distinct heritable states on one genome outside development, plus measured methylation counts and switch/persistence frequencies.
3. Falsifiability condition: the gap claim fails if any canonical item names a bistable state, a phenotypic switch, or heritable non-sequence state in a single-celled organism.
4. Variables: measurable / bounded / held open: Measurable: methylation site counts, hysteresis, persister probability and frequency range. Bounded: the persister fraction is bounded between about 1e-6 and 1e-3 and is medium-dependent, so no single number describes it. Held open: the per-generation memory duration of a bistable state in E. coli (not retrieved this run).
5. Test designed: fetch a genome-wide methylome, the bistability phase diagram, and both the founding and a recent single-cell persistence measurement.
6. Data (unfiltered): table above. Canon's grep yields no bistability, no switch, no persistence, and methylation only as an evolutionary residue.
7. Variable Principle applied: canon holds "same DNA, different expression" only for tissue differentiation, where an external developmental context does the directing. The bacterial case removes the external director: identical cells in identical medium hold different stable states. That is a measured case where canon's "Third Kingdom regulatory context" has no referent — and the framework should not be given one by assumption.
8. Model update (Capsule: what the failed parts contribute): the surviving useful statement is that stable state can live in something other than sequence (methylation marks, a feedback loop's occupancy, a growth-arrest state), and that its persistence is measurable. Applied to canon's Layer 0, this is a third independent way in which "the code is invariant, the expression varies" is too coarse: here neither the code nor the environment varies, and the expression still does.
9. Documented: this file. Correspondence: one scale down, hemimethylation of GATC sites through the replication cycle as a molecular memory of strand age; one scale up, canon's own Stage 26 differentiation case, which is the multicellular version of the same phenomenon and is the only version canon holds.
10. Next baseline: a canonical item for non-sequence heritable state; a PRED candidate on the measured relation persister frequency = s times the non-growing fraction.

## Forcing Test

- Test A (Ground): Grounded. Four independent primary measurements (methylome, phase diagram, two persistence studies from different laboratories).
- Test B (Uniqueness): The gap classification is unique given the grep; canon has no competing item.
- Test C (Direction): Measurement points toward stable multi-state behaviour in isogenic populations under fixed conditions.
- Test D (Falsifiability): The gap claim's falsifier did not fire.
- **Outcome:** `stipulation`. DPR mapping is **after-the-fact** for bistability and persistence: a bistable switch has no detect step — its state is set by history, and the measured object is a hysteresis loop, whose defining property is that the same input maps to two outputs. That is the direct negation of canon's Layer 0 statement "Same input + different processing architecture = completely different output" *only if* the architecture is allowed to include history; canon does not say whether it does, so the point is recorded, not resolved.
## Anti-Operation (the gap this opens)

Hysteresis means the present output is not a function of the present input. The framework's base loop is stated as a function of input and architecture, with history entering only through "the baseline integrates all prior cycles" (the Capsule). Gap: canon has no way to say *how much* of the past a system carries — and the bacterial switch supplies exactly the measurable quantity that would settle it (the memory duration of a bistable state, in generations). That value was not retrieved this run and is held open.

## Narrative stripped (if any)

- Removed: methylation read as "the structural information of failed paths". Measured methylation in E. coli marks self versus foreign DNA and strand age; nothing fetched here shows it storing information about failed evolutionary variants.
- Removed: "Third Kingdom regulatory context" as the director of differing states. In an isogenic bacterial population under fixed conditions there is no external director; the state is set by feedback and history.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; grading not endorsed by the author.
```
