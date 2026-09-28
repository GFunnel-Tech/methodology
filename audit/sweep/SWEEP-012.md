---
id: SWEEP-012
canon_ref: "v5.1 Layer I.G 'The Slime Mold Integration Principle' ('Conservation Of Information As Conservation Of Energy': 'information is conserved across all paths; nothing is discarded') and Core Axiom 14"
canon_label: "The Slime Mold Integration Principle (the Capsule) / Axiom 14 — Every Path Is Integrated"
diff_state: conflict
exclusion_diagnosis: reached-conflicting
claim_outcome: forced-no
intake_result: adjusted
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Layer I.G: "Per Layer I.E: energy is conserved across all transformations; nothing is destroyed. Per Layer I.G: **information is conserved across all paths; nothing is discarded.** These are the same principle stated at different abstraction levels."

Core Axiom 14: "Per the Capsule: nothing is lost. Every explored path — successful, failed, partial, collapsed — contributes its full information to the integrated substrate of the present moment ... **Failures are load-bearing, not discarded.**"

Layer I.G's own table asserts the biological row is "Confirmed".

**Split (RUNBOOK rule 4).** *Factual core graded here:* at molecular scale, information about a failed path is not discarded. *Framework mapping (not graded):* the theological and cosmological readings of the Capsule.

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Error discrimination by exonucleolytic proofreading in E. coli (mutD5 mutL vs mutL strains, lacI sequencing) | 40 to 200 fold | range across error types as published | measured-single | https://doi.org/10.1016/s0021-9258(20)80446-3 | 2026-09-28 |
| Error discrimination by postreplicative mismatch repair (mutL vs wild type) | 20 to 400 fold | range across error types as published | measured-single | https://doi.org/10.1016/s0021-9258(20)80446-3 | 2026-09-28 |
| Mismatch repair reduces the wild-type mutation rate and changes its spectrum (independent lab, mutation accumulation plus whole-genome sequencing; wild-type rate 1e-3 per genome per generation, bias G:C to A:T, reversing to A:T to G:C without MMR) | MMR-dependent reduction confirmed independently of the lacI assay | as published | measured-reproduced | https://doi.org/10.1073/pnas.1210309109 | 2026-09-28 |
| Total serial discrimination of the three-stage fidelity architecture | 1.6e8 to 1.6e11 fold | derived: base selection 2e5-2e6 times proofreading 40-200 times MMR 20-400 | derived | https://doi.org/10.1016/s0021-9258(20)80446-3 | 2026-09-28 |
| Size of the damage-containing oligonucleotide excised and released by E. coli nucleotide excision repair (sequenced directly) | 13-mer ssDNA, unwound from the duplex by UvrD and then exposed to exonuclease | as published | measured-single | https://doi.org/10.1073/pnas.1700230114 | 2026-09-28 |

## Scientific Inquiry run

1. Question (precise): Does any canonical item hold proofreading and mismatch repair, and does the measured mechanism preserve the information of the failed path, as Layer I.G and Axiom 14 require?
2. What an answer must look like: the measured fate of a mis-incorporated nucleotide and of a damaged base — retained anywhere in the cell as a record, or hydrolysed.
3. Falsifiability condition: "nothing is discarded" is falsified at this scale by a reproduced mechanism whose measured function is to remove a molecule from the informational polymer and not record it.
4. Variables: measurable / bounded / held open: Measurable: discrimination factors of each stage; size of the excised oligo. Bounded: the *rate* of discard is bounded by the error rate it corrects (about 1e-10 per bp after all three stages). Held open: whether the thermodynamic trace of a hydrolysed nucleotide counts as "information conserved" — a definitional variable canon does not fix, so it is not resolved here.
5. Test designed: fetch the measured efficiencies of each error-avoidance stage in E. coli and the measured fate of the removed material.
6. Data (unfiltered): table above. Proofreading excises the mis-paired terminal nucleotide as a mononucleotide; mismatch repair excises a tract containing the error; NER releases a 13-mer which is then unwound and degraded. The identity of the removed base is not written anywhere in the cell.
7. Variable Principle applied: canon states the conservation of information as a principle with no error term and lists the biological row as "Confirmed". Measurement shows the opposite at this scale: three serial machines whose *function* is discard, and whose measured efficiency is the reason the code is stable at all. Canon's "Confirmed" is not supported by the fetched measurements; the correct grade is that the molecular row is contradicted.
8. Model update (Capsule: what the failed parts contribute): the surviving honest form of the claim is narrower and still interesting: *what is conserved is the discrimination, not the discarded item.* The cell keeps the machinery that rejected the error, not the error. The slime-mold analogy fails exactly here: retracted protoplasm is re-used mass; a hydrolysed nucleotide is returned to a pool with its sequence identity destroyed.
9. Documented: this file. Correspondence: one scale down, the kinetics of the epsilon subunit's exonuclease site; one scale up, immune negative selection (clonal deletion), another measured discard mechanism canon's Domain 9 immune row does not mention.
10. Next baseline: canon's "nothing is discarded" should carry an explicit exception at molecular scale, or be restated as "the discriminating structure is conserved". Not applied to canon (versions are immutable); proposed for v5.5.

## Forcing Test

- Test A (Ground): Grounded. Two independent measurement lines (lacI mutational spectra; mutation accumulation plus whole-genome sequencing) both show a mismatch-repair stage whose action is removal.
- Test B (Uniqueness): For the claim "at molecular scale nothing is discarded", zero candidates survive. Discard is the measured function.
- Test C (Direction): Measurement points one way: fidelity is bought by discarding, in three serial stages.
- Test D (Falsifiability): The claim had a clean falsifier and it fired.
- **Outcome:** `forced-no` for "information is conserved across all paths; nothing is discarded" at molecular scale. DPR mapping: DETECT = mismatch recognition by MutS; PROCESS = MutL/MutH incision and excision tract removal; RESPOND = resynthesis. This parse *does* land on measured boundaries (MutS binding, incision, resynthesis are separable steps with separable mutants), so here the loop fits the mechanism rather than being applied after the fact — but the loop's output is a deletion, which Axiom 14 forbids.

## Anti-Operation (the gap this opens)

If discard is load-bearing at molecular scale, the framework needs a measured criterion for *when* a system must discard rather than integrate. Canon has no such criterion, and the dynamic middle (Layer I.D) is stated qualitatively. Open question: is there a measurable optimum between discard cost and error cost — i.e. why three stages and not four?

## Narrative stripped (if any)

Removed: the theological extension ("nothing is wasted", the problem of evil) as *support* for the molecular claim. It is a reading of the principle, not evidence for it, and the molecular row it leans on is the row measurement contradicts.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; grading not endorsed by the author.
```
