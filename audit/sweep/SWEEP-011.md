---
id: SWEEP-011
canon_ref: "v5.1 Layer 0, 'The DNA Metaphor — Why It Is Exact, Not Approximate' (transcription, translation, cellular execution) and v5.1 Appendix A Stage 23 ('polymerases' as ATP-consuming machines)"
canon_label: "The Base Code — The Universal DNA / Stage 23 ATP Hydrolysis / Cellular Work"
diff_state: methodology-gap
exclusion_diagnosis: not-reached
claim_outcome: stipulation
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Layer 0: "DNA is not a description of an organism. It is the base code from which the organism is expressed — through **transcription, translation, and cellular execution** — into every structure ... The code is invariant across all of them."

v5.1 Appendix A, Stage 23 (ATP Hydrolysis / Cellular Work): "Energy captured by molecular machines: motor proteins, ion pumps, ribosomes, polymerases. Universal currency."

**Split (RUNBOOK rule 4).** *Factual core graded here:* canon's account of how the code reaches its expressions names three operations — transcription, translation, cellular execution — and mentions polymerases only as consumers of ATP. **Copying the code itself (DNA replication) is named by no canonical item, and no fidelity or rate is anywhere in canon.**

*Framework mapping (not graded):* "Layer 0 is the codon. Every layer that follows is a protein"; "This is law, not analogy."

**Grading rubric used in SWEEP-011..022 for the DPR question.** `live-hypothesis` = the three-step parse lands on boundaries that are themselves measured (a distinct discrimination step, a distinct commitment step); `stipulation` = the parse is an operator's labelling choice with no measured boundary at the cut; `forced-no` = measurement rules the canonical claim out.

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Processivity of E. coli Pol III holoenzyme in leading-strand synthesis coupled to DnaB helicase, single-molecule | 10.5 kb (8-fold higher than Pol III alone) | as published; no interval in fetched text | measured-single | https://doi.org/10.1038/nsmb.1381 | 2026-09-28 |
| Replication fork speed in growing E. coli cells, DNA combing, single-molecule | 653 nt/s average; most forks 550-750 nt/s | ± 9 nt/s (SEM) | measured-single | https://doi.org/10.1111/mmi.12386 | 2026-09-28 |
| Fork speed in a dnaE173 strain whose Pol III elongates at 300 nt/s (wild-type Pol III 900 nt/s) | 264 nt/s | ± 9 nt/s (SEM) | measured-single | https://doi.org/10.1111/mmi.12386 | 2026-09-28 |
| Discrimination against errors by base selection alone (mutD5 mutL strain, lacI sequencing) | 2e5 to 2e6 fold, depending on error type | range as published across error types | measured-single | https://doi.org/10.1016/s0021-9258(20)80446-3 | 2026-09-28 |
| E. coli K-12 MG1655 genome length (GCF_000005845.2) | 4,641,652 bp | exact (assembly) | measured-reproduced | https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.gff.gz | 2026-09-28 |
| Net wild-type mutation rate per base pair per generation | 2.2e-10 | derived: 1e-3 per genome per generation divided by 4,641,652 bp | derived | https://doi.org/10.1073/pnas.1210309109 | 2026-09-28 |
| Rate at which DnaB unwinding is slowed when translesion Pol II or Pol IV holds the beta-clamp | as little as 1 bp/s | as published | measured-single | https://doi.org/10.1073/pnas.0901403106 | 2026-09-28 |

Reference organism: E. coli K-12 (Pham 2013 uses a thymidine-requiring K-12 derivative; Tanner 2008 is reconstituted E. coli protein).

## Scientific Inquiry run

1. Question (precise): Does a canonical item hold DNA replication — the replisome, Pol III, processivity, measured fidelity — and does DETECT → PROCESS → RESPOND fit the measured mechanism at a real boundary?
2. What an answer must look like: a canonical location that names replication (not only "polymerases" as an ATP sink), plus measured rate and fidelity values to compare against any canonical figure.
3. Falsifiability condition: the gap claim fails if any canonical item names DNA replication or states a replication rate or error rate.
4. Variables: measurable / bounded / held open: Measurable: fork speed, processivity, base-selection discrimination, net per-bp rate. Bounded: fidelity is finite and non-zero, so "the code does not change between expressions" is bounded at ~1e-10 per bp per generation, not zero. Held open: whether the framework's three operations have any measured counterpart in the replisome.
5. Test designed: grep canon for replication / polymerase / fidelity; fetch primary single-molecule and in-vivo measurements for rate, processivity and error discrimination.
6. Data (unfiltered): table above. Canon mentions "polymerases" once (Stage 23) and "transcription, translation, cellular execution" in Layer 0. No canonical item states a replication rate, a processivity, or an error rate.
7. Variable Principle applied: the copying operation that makes code invariance possible at all is absent from canon; invariance is therefore asserted without its mechanism and without its measured error term. The DPR assignment offered by the framework's own Domain 9 row (signal → transcription/translation → protein) does not reach replication.
8. Model update (Capsule: what the failed parts contribute): an honest parse is available but is a labelling choice: DETECT = template base pairing / clamp loading at the primer terminus; PROCESS = phosphodiester bond formation by Pol III alpha; RESPOND = translocation and hand-off of the extended primer. The measured mechanism has no boundary at the DETECT/PROCESS cut: base selection and catalysis are the same kinetic event (selection *is* the differential rate of insertion), which is why Schaaper's "base selection" is measured as a discrimination factor, not as a separate step. So the fit is after-the-fact.
9. Documented: this file. Correspondence: one scale down, nucleotide insertion kinetics (no separable detect step); one scale up, the cell cycle's initiation-at-oriC decision, which *does* have a measured threshold and would parse better.
10. Next baseline: an audit item for replication as a named component, carrying the fork speed and the serial-fidelity architecture (see SWEEP-012), and a PRED test on the fork-speed / Pol-III-speed relation.

## Forcing Test

- Test A (Ground): Grounded on the reality side (fork speed, processivity, discrimination factors all measured); ungrounded on the canon side, where no item names replication.
- Test B (Uniqueness): The three-step parse is not unique. At least two other parses of the replisome fit equally (helicase/polymerase/ligase; initiation/elongation/termination). Measurement does not select among them.
- Test C (Direction): Measurement points toward a serial-stage fidelity architecture (selection, then proofreading, then repair) rather than a single three-operation loop.
- Test D (Falsifiability): The gap claim is falsifiable by one canonical line naming replication; none was found in v5.1.
- **Outcome:** `stipulation` — assigning DETECT → PROCESS → RESPOND to the replisome is an operator's presentation choice, applied after the fact. The methodology gap (replication unnamed) stands; `intake_result: open`.

## Anti-Operation (the gap this opens)

Fork speed tracks Pol III's own chain elongation rate but does not equal it (900 → 653 nt/s wild type; 300 → 264 nt/s mutant). The ratio moves the wrong way for a simple rate-limiting model (0.73 vs 0.88). What sets the shortfall — and does any framework quantity predict it? Canon supplies no rate at any scale, so it cannot be tested there yet. Second gap: nothing in canon states what a *copy* operation is, as distinct from a response.

## Narrative stripped (if any)

Removed: "This is law, not analogy" as applied to copying. Nothing measured here forces the identification of a polymerase with a codon or a layer with a protein. Reality neither forces nor contradicts the mapping; it simply does not reach it.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; grading not endorsed by the author.
```
