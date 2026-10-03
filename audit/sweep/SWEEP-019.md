---
id: SWEEP-019
canon_ref: "v5.1 Layer I.C Domain 9, 'Immune Process as Shepherd's Way' row ('memory cell formation ... Memory formation = Shepherd's Way Steps 06-07 at biological level'), read against v5.1 Layer 0 'The code is invariant across all of them'"
canon_label: "Domain 9 — Immune Process as Shepherd's Way"
diff_state: conflict
exclusion_diagnosis: reached-conflicting
claim_outcome: forced-no
intake_result: adjusted
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Domain 9, Immune Process row: "DETECT: Foreign antigen. PROCESS: Recognition, amplification, clonal expansion, targeted antibody production. RESPOND: Pathogen elimination + memory cell formation. **Memory formation = Shepherd's Way Steps 06-07 at biological level.**"

v5.1 Layer 0: "The code does not change between expressions. The cell type changes ... **The code is invariant across all of them.**"

**Split (RUNBOOK rule 4).** *Factual core graded here:* (a) canon's only model of immune memory is *cellular* (memory cells), and (b) DNA is invariant within an organism/lineage. In bacteria, adaptive immunity is measured to work by **writing the memory into the genome**. *Framework mapping (not graded):* the identification with Shepherd's Way steps 06-07.

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| CRISPR adaptation in E. coli type I-E: new spacers are acquired from foreign DNA and integrated into the chromosomal CRISPR array; acquisition is replication-dependent and promoted by double-strand breaks at stalled forks | mechanism established; chromosomal protospacer hotspots at Ter show about 7 to 20 fold higher protospacer density than surrounding regions | as published | measured-reproduced | https://doi.org/10.1038/nature14302 | 2026-09-28 |
| Self/non-self discrimination: fraction of spacers taken from the host's own chromosome rises in recB, recC, recD deletion strains | about 10-fold higher than wild type, matching the 14-fold enrichment of Chi sites (one about every 5 kb) on the chromosome | as published | measured-single | https://doi.org/10.1038/nature14302 | 2026-09-28 |
| Primed adaptation: a partially matching spacer that no longer confers defence still guides the acquisition machinery to the foreign DNA, restoring protection (independent laboratory) | mechanism established; acquisition machinery moves along the DNA selecting fragments | as published | measured-reproduced | https://doi.org/10.1038/ncomms1937 | 2026-09-28 |
| Sequence bias in prespacer selection during primed adaptation: presence of the consensus PAM trinucleotide AAG within the candidate sequence strongly lowers acquisition efficiency | measured depletion; no such trend in naive adaptation | as published | measured-single | https://doi.org/10.1128/mbio.02169-18 | 2026-09-28 |
| Restriction-modification as the non-adaptive layer: m6A and m5C sites mapped genome-wide in a pathogenic E. coli strain by single-molecule real-time sequencing; deleting a phage-encoded methyltransferase-endonuclease system caused global transcriptional changes and gene amplification | 49,311 putative m6A and 1,407 putative m5C sites (strain O104:H4, not K-12) | as published | measured-single | https://doi.org/10.1038/nbt.2432 | 2026-09-28 |
| Efficiency of plating of unmodified phage against a type I restriction-modification system (comparator organism Lactococcus lactis, since no EcoKI figure was retrievable this run) | 1e4-fold reduction | as published | measured-single | https://doi.org/10.1099/00221287-146-2-435 | 2026-09-28 |
| An EcoKI-specific quantitative restriction efficiency for E. coli K-12 | not retrieved: the fetched EcoKI papers report alleviation of restriction qualitatively, without a baseline plating efficiency | n/a | held-open | https://doi.org/10.1128/jb.179.6.1852-1856.1997 | 2026-09-28 |

## Scientific Inquiry run

1. Question (precise): Does a canonical item hold bacterial adaptive immunity, and does the measured mechanism contradict canon's claim that the code is invariant across expressions?
2. What an answer must look like: a measured, reproduced mechanism by which a bacterium's own chromosomal sequence changes as a *recorded response to experience*, not as an error.
3. Falsifiability condition: canon's invariance claim is falsified for bacteria by any reproduced, programmed insertion of new sequence into the genome as a memory of an encounter.
4. Variables: measurable / bounded / held open: Measurable: acquisition dependence on replication and RecBCD, hotspot densities, self/non-self bias, methylation site counts. Bounded: acquisition is biased, not uniform (PAM avoidance, Chi-site limits). Held open: a per-generation spacer acquisition rate in wild-type cells, and an EcoKI restriction efficiency — neither retrievable this run.
5. Test designed: fetch two independent primary CRISPR adaptation studies plus a genome-wide methylome and restriction-modification study; compare with canon's cellular-memory-only model and with Layer 0's invariance claim.
6. Data (unfiltered): table above. Spacer acquisition inserts new DNA into the host chromosome; it is directed (replication-dependent, RecBCD-limited, PAM-biased); it is heritable; and it is *the* memory.
7. Variable Principle applied: canon's "memory cell formation" is a vertebrate-specific mechanism presented as the biological case. In bacteria the measured memory is genomic. Therefore Layer 0's "the code is invariant across all expressions" is contradicted in the clearest possible way: in bacteria the code is the notebook. This extends LABEL-101 (which used vertebrate V(D)J recombination and somatic mutation) into prokaryotes, where canon's Correspondence argument is strongest and the counterexample is most direct.
8. Model update (Capsule: what the failed parts contribute): the honest general statement is "an information-processing system records experience into the most stable substrate it has access to" — DNA in bacteria, cell populations in vertebrates. That is a stronger and testable claim; it is a derivation, not canon.
9. Documented: this file. Correspondence: one scale down, Cas1-Cas2 integrase chemistry; one scale up, restriction-modification is the innate layer (self marked by methylation), so bacteria have both layers canon's Domain 9 describes only for vertebrates.
10. Next baseline: canon's invariance claim needs an explicit exception clause for programmed genomic memory; proposed for v5.5, not applied (versions immutable).

## Forcing Test

- Test A (Ground): Grounded. Two independent laboratories' primary measurements of spacer acquisition; plus a genome-wide methylome.
- Test B (Uniqueness): For "bacterial DNA is invariant across expressions", zero candidates survive: acquisition is programmed, directed and heritable.
- Test C (Direction): Measurement points one way: the genome is a writable medium under experience.
- Test D (Falsifiability): The claim's falsifier fired.
- **Outcome:** `forced-no` for code invariance in bacteria. DPR mapping: DETECT = PAM recognition on a foreign fragment produced by RecBCD processing of a break; PROCESS = Cas1-Cas2 prespacer capture and integration at the leader end; RESPOND = crRNA-guided interference on the next encounter. These boundaries are measured and separable (naive vs primed adaptation; interference-free systems), so the loop **fits** — but its RESPOND writes the genome, which canon's Layer 0 forbids.

## Anti-Operation (the gap this opens)

Acquisition is measured to be *biased against the very motif required for the memory to work* (AAG PAM depletion during primed adaptation). So the recording machinery systematically degrades the usefulness of what it records. Canon's Shepherd's Way steps 06-07 ("if it isn't written, it doesn't exist as a process") have no representation for a recording step that corrupts the record. Open: is there a measured optimum between recording rate and record fidelity?

## Narrative stripped (if any)

- Removed: "Memory formation = Shepherd's Way Steps 06-07 at biological level." The equation of a documentation step in a business cycle with memory-cell formation is a mapping; reality neither forces nor contradicts it, and the bacterial case it is meant to generalise over works by a different substrate.
- Removed: the implication that immune memory is always cellular.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; grading not endorsed by the author.
```
