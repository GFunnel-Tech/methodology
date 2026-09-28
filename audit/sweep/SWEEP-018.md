---
id: SWEEP-018
canon_ref: none
canon_label: none
diff_state: unmapped
exclusion_diagnosis: not-reached
claim_outcome: stipulation
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

Nothing. Searched v5.1 for chaperone, folding, quality control, tmRNA, misfolding, degradation, protease: no canonical item names any of them. The nearest items are v5.1 Appendix A Stage 23 ("ribosomes" as ATP consumers) and Domain 9's "Apoptosis" row (programmed *cell* death, not protein triage), neither of which holds this component.

The canonical claim this bears on is v5.1 Layer I.C's closing line: "DETECT → PROCESS → RESPOND · Ten Domains · One Algorithm · **Zero Exceptions**", and Domain 9's claim that gene expression *is* the algorithm at molecular level — which stops at "expressed protein".

**Split (RUNBOOK rule 4).** *Factual core graded here:* the existence of a post-expression triage stage (stalled-ribosome rescue, chaperone-dependent folding, tagging for degradation) that canon's pipeline does not reach. *Framework mapping (not graded):* whether "zero exceptions" is a claim about coverage or about the loop.

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Fraction of all protein syntheses in E. coli that terminate with tmRNA tagging and ribosome rescue during normal exponential growth | about 0.4 percent | as published | measured-single | https://doi.org/10.1111/j.1365-2958.2005.04832.x | 2026-09-28 |
| Capacity headroom of the rescue system: tagging did not increase when tmRNA and SmpB were overexpressed, but increased substantially when non-stop mRNA was overproduced | rescue system normally operates well below capacity | qualitative, as published | measured-single | https://doi.org/10.1111/j.1365-2958.2005.04832.x | 2026-09-28 |
| E. coli proteins that interact with the chaperonin GroEL | about 250 | as published | measured-single | https://doi.org/10.1016/j.cell.2005.05.028 | 2026-09-28 |
| Proteins obligately dependent on GroEL/GroES (cannot reach native state via trigger factor or DnaK alone), including essential proteins | about 85 obligate substrates, of which 13 essential; these occupy more than 75 percent of GroEL capacity | as published | measured-single | https://doi.org/10.1016/j.cell.2005.05.028 | 2026-09-28 |
| Measured fate of the tmRNA-tagged nascent chain in wild-type cells | the wild-type tag promotes rapid degradation of the rescued protein (a mutant tag was required to observe tagging at all) | qualitative, as published | measured-single | https://doi.org/10.1111/j.1365-2958.2005.04832.x | 2026-09-28 |

## Scientific Inquiry run

1. Question (precise): Is there a canonical item that holds ribosome quality control, trans-translation and chaperone-assisted folding — and does DPR fit their measured mechanisms?
2. What an answer must look like: a canonical location naming any of these components, or a reasoned statement that none exists, plus measured frequencies and dependencies.
3. Falsifiability condition: the unmapped classification fails if any canonical item names protein folding, chaperones, quality control or protein degradation.
4. Variables: measurable / bounded / held open: Measurable: tagging frequency (0.4 percent), GroEL interactor and obligate-substrate counts. Bounded: rescue demand is bounded well below capacity in normal growth. Held open: the fraction of *all* nascent chains requiring chaperone assistance (the fetched source counts interactors, not flux).
5. Test designed: grep canon for the relevant terms; fetch the in vivo tmRNA tagging frequency and the proteome-wide GroEL dependence measurement.
6. Data (unfiltered): table above; canon: no hits.
7. Variable Principle applied: canon's molecular pipeline ends at "expressed protein". Measurement shows two further mandatory stages (folding assistance for about 85 proteins obligately, rescue for about 0.4 percent of syntheses) and that the normal output of the rescue stage is *destruction of the product*. The framework's claim of zero exceptions is not contradicted by this — but it is untested here, because no canonical item reaches this far.
8. Model update (Capsule: what the failed parts contribute): the loop can be applied (DETECT = an A site empty of mRNA, sensed by tmRNA-SmpB; PROCESS = trans-translation, tag synthesis; RESPOND = release plus proteolysis) and the boundaries here are measured and separable. So the loop fits; what is missing is a canonical *place* for it, and a canonical acknowledgement that a normal loop output can be the deletion of the loop's own product — again against Axiom 14 (see SWEEP-012).
9. Documented: this file. Correspondence: one scale down, the chaperonin cage's encapsulation cycle; one scale up, immune clearance of damaged cells; canon's Domain 9 names apoptosis but not molecular triage.
10. Next baseline: propose a canonical item "post-expression triage" holding folding and rescue, with the tagging frequency as its first measured quantity.

## Forcing Test

- Test A (Ground): Grounded on the reality side (two independent proteome-scale measurements); canon has no ground here at all.
- Test B (Uniqueness): The unmapped classification is unique given the grep result — no canonical item competes for this component.
- Test C (Direction): Measurement points toward the pipeline continuing past protein synthesis with a mandatory triage stage.
- Test D (Falsifiability): Falsifier (a canonical mention of folding or quality control) did not fire.
- **Outcome:** `stipulation` — canon's "Ten Domains · Zero Exceptions" is a presentation choice about the *proof set*, not a tested coverage claim; a measured component with no canonical home shows the set was chosen, not derived. The DPR mapping itself **fits** the tmRNA mechanism at measured boundaries.

## Anti-Operation (the gap this opens)

0.4 percent of syntheses end in rescue and the rescued product is then destroyed. So the measured output of a normal molecular loop is sometimes the deliberate deletion of its own output. The framework has no operation for that (RESPOND is defined as output becoming next input). Gap: define, and try to measure, the framework's discard operation — the same gap SWEEP-012 opens from the repair side.

## Narrative stripped (if any)

None in canon to strip: there is no canonical narrative here. Noted instead: the absence is itself informative. The framework's registry of ten domains is presented as "the proof set that the base code has zero exceptions"; an unmapped, well-measured component shows the registry is a selection of examples.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; grading not endorsed by the author.
```
