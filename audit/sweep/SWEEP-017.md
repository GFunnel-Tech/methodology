---
id: SWEEP-017
canon_ref: "v5.1 Appendix D, Biological & Scaling Laws, row 'Genetic Code Universality' (line 2083), read with Layer 0 'Layer 0 is the codon'"
canon_label: "Genetic Code Universality"
diff_state: methodology-gap
exclusion_diagnosis: not-reached
claim_outcome: forced-fill
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix D: "**Genetic Code Universality** — Same 64 codons → same 20 amino acids across nearly all life. Per LUCA (Stage 14): all known life uses one base code. Per Correspondence at biological scale: one algorithm, one substrate."

v5.1 Layer 0: "Layer 0 is the codon. Every layer that follows is a protein."

**Split (RUNBOOK rule 4).** *Factual core graded here:* the counts (64 codons, 20 amino acids) and the claim of one code. Already graded `accounted` in `audit/constants/CONST-genetic-code-universality.md`. **What this sweep adds from the reality side: degeneracy, wobble, and the decoding compression — none of which any canonical item holds.** *Framework mapping (not graded):* "one algorithm, one substrate".

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Codons in the standard code, NCBI table 1 (parsed from the fetched file this run) | 64: 61 sense plus 3 stop | exact | measured-reproduced | https://ftp.ncbi.nih.gov/entrez/misc/data/gc.prt | 2026-09-28 |
| Distinct amino acids encoded by table 1 (parsed this run) | 20 | exact | measured-reproduced | https://ftp.ncbi.nih.gov/entrez/misc/data/gc.prt | 2026-09-28 |
| Genetic-code tables NCBI recognises (ids 1-6, 9-16, 21-33; counted this run) | 27 tables: the standard code plus 26 variants | exact count of listed tables | measured-reproduced | https://ftp.ncbi.nih.gov/entrez/misc/data/gc.prt | 2026-09-28 |
| tRNA genes annotated in E. coli K-12 MG1655 (GCF_000005845.2, counted from the fetched GFF this run) | 86 | exact (annotation) | measured-reproduced | https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.gff.gz | 2026-09-28 |
| Distinct tRNA isoacceptor species by amino acid and anticodon in the same annotation (counted this run) | 41 distinct amino-acid/anticodon combinations, covering 21 distinct tRNA products | exact (annotation) | measured-reproduced | https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.gff.gz | 2026-09-28 |
| Decoding compression implied: sense codons per distinct anticodon species | 61 sense codons read by 41 anticodon species = 1.49 codons per anticodon; wobble is therefore obligatory, not optional | derived from the two annotation counts above | derived | https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.gff.gz | 2026-09-28 |

## Scientific Inquiry run

1. Question (precise): Does canon's "genetic code" item hold the code's measured internal structure — degeneracy, wobble decoding, variant tables — and does the code fit DETECT → PROCESS → RESPOND at all?
2. What an answer must look like: the codon and amino-acid counts (canon states them), plus the decoding counts canon does not state, from a primary annotation.
3. Falsifiability condition: canon's counts fail if the standard table does not have 64 codons or 20 amino acids. The "no exceptions" reading fails if variant tables exist. The gap claim fails if canon anywhere names degeneracy or wobble.
4. Variables: measurable / bounded / held open: Measurable: all counts above. Bounded: "universality" is bounded by 26 variant tables and by the 41-anticodon decoding set. Held open: why this code (frozen accident vs optimisation) — already held open in the constant's audit and not resolved here.
5. Test designed: fetch and parse NCBI's genetic-code file and the RefSeq annotation of the reference organism; count codons, amino acids, tables, tRNA genes and anticodon species.
6. Data (unfiltered): table above. Counts confirm canon's 64 and 20. Canon states neither the 61/3 split, nor degeneracy, nor that 61 sense codons are read by 41 anticodon species, nor wobble.
7. Variable Principle applied: canon's row is correct and hedged ("nearly all life"). What it omits is the code's *compression*: the mapping is 61 to 41 to 20, two lossy stages, not one clean lookup. Calling Layer 0 "the codon" imports the codon's uniqueness but not its degeneracy, which is the codon's most consequential measured property.
8. Model update (Capsule: what the failed parts contribute): degeneracy is the molecular form of an error-tolerant encoding — a synonymous substitution is a change in the code that produces no change in the expression. That is a measured counterexample to the idea that the code is the invariant and the expression the variable: here the code varies while the expression does not.
9. Documented: this file. Correspondence: one scale down, wobble base pairing at the third position; one scale up, the 26 variant tables show the "one code" claim is a strong regularity with documented exceptions, not a law.
10. Next baseline: an explicit canonical item for degeneracy and for the 61-to-41-to-20 compression; keep "why this code" held open.

## Forcing Test

- Test A (Ground): Grounded. All counts come from primary files fetched and parsed in this run.
- Test B (Uniqueness): For the counts, yes: one standard table, uniquely 61 sense plus 3 stop to 20 amino acids.
- Test C (Direction): The variant tables direct the claim from "universal" to "near-universal with catalogued exceptions"; canon's own wording already hedges this way.
- Test D (Falsifiability): Canon's counts had a clean falsifier (a different count); it did not fire.
- **Outcome:** `forced-fill` for the counts. DPR mapping: **after-the-fact.** A codon table is a static mapping; it has no temporal detect step, no processing step and no response. Assigning the three operations to "codon in, ribosome processes, amino acid out" describes the ribosome (SWEEP-016), not the code. `methodology-gap` stands for degeneracy and wobble.

## Anti-Operation (the gap this opens)

Degeneracy means the code is not the invariant canon needs: 1.49 codons per anticodon and up to six codons per amino acid mean many distinct codes produce identical expressions. The framework's Layer 0 metaphor requires the code to be the thing that does not change; measurement shows the code carries slack by design. What is the framework's analogue of a synonymous substitution — a change in the base loop that provably cannot change the output?

## Narrative stripped (if any)

Removed: "one algorithm, one substrate" (already stripped in the constant's audit) and "Layer 0 is the codon". A shared code is evidence of common descent, not of a universal algorithm across non-living scales.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; grading not endorsed by the author.
```
