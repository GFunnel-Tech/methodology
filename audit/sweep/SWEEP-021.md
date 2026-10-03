---
id: SWEEP-021
canon_ref: "v5.1 Layer I.D, 'The Dynamic Middle Across All Domains', Evolutionary row ('Yang extreme: excess variation — chaos; Yin extreme: excess selection — stasis; Dynamic Middle: optimal mutation rate') and v5.1 Layer I.G Slime Mold Stack, Biological row ('Confirmed')"
canon_label: "The Dynamic Middle — Evolutionary row (optimal mutation rate)"
diff_state: unobserved-claim
exclusion_diagnosis: n/a
claim_outcome: live-hypothesis
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Layer I.D, Dynamic Middle table, Evolutionary row: Yang extreme "Excess variation — chaos"; Yin extreme "Excess selection — stasis"; Dynamic Middle "**Optimal mutation rate**".

v5.1 Layer I.G, Slime Mold Stack, Biological row: "Mutation as genome's exploration of fitness space, with most variants retracting and **the surviving ones carrying forward the structural information of failed ones** in regulatory regions, methylation patterns, transposable elements. — **Confirmed** (genomic conservation; junk DNA; immune memory)."

**Split (RUNBOOK rule 4).** *Factual core graded here:* (a) there is an optimal mutation rate, and (b) surviving lineages carry forward the information of the variants that failed. Canon marks (b) "Confirmed". *Framework mapping (not graded):* the Yin/Yang assignment.

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Wild-type E. coli mutation rate, mutation accumulation plus whole-genome sequencing over thousands of generations | about 1e-3 per genome per generation | as published | measured-single | https://doi.org/10.1073/pnas.1210309109 | 2026-09-28 |
| Same rate expressed per base pair | 2.2e-10 per bp per generation | derived: 1e-3 divided by the 4,641,652 bp K-12 genome | derived | https://doi.org/10.1073/pnas.1210309109 | 2026-09-28 |
| Rate of small (4 nt or fewer) insertions and deletions relative to base substitutions genome-wide | about one tenth the genomic rate of base-pair substitutions | as published | measured-single | https://doi.org/10.1073/pnas.1210309109 | 2026-09-28 |
| Mutational bias, wild type vs mismatch-repair defective | G:C to A:T in wild type; reverses to A:T to G:C without MMR | as published | measured-single | https://doi.org/10.1073/pnas.1210309109 | 2026-09-28 |
| Strand asymmetry of replication-associated transitions | A:T to G:C transitions preferentially with A templating the lagging strand and T the leading strand; G:C to A:T with C templating the lagging strand and G the leading strand | as published | measured-single | https://doi.org/10.1073/pnas.1210309109 | 2026-09-28 |
| Whether mismatch repair capacity is itself variable in nature (bearing on an optimum) | bacteria isolated from nature often lack MMR capacity, and MMR activity is genetically regulated, suggesting modulation of MMR can be adaptive | qualitative, as published | measured-single | https://doi.org/10.1073/pnas.1210309109 | 2026-09-28 |
| A measured value of the "optimal" mutation rate, or a measured fitness optimum as a function of mutation rate, for E. coli | not retrieved this run; the fetched mutation-accumulation study reports the realised rate, not an optimum | n/a | held-open | https://doi.org/10.1073/pnas.1210309109 | 2026-09-28 |
| Luria-Delbruck fluctuation test: original numeric mutation-rate estimate | not retrieved: the 1943 Genetics article is available as a scanned record whose full text was not machine-retrievable from PMC or Europe PMC in this run (abstract field empty, full-text endpoints returned no text) | n/a | held-open | https://doi.org/10.1093/genetics/28.6.491 | 2026-09-28 |
| Any measurement showing that a surviving lineage retains the information of variants that were selected against | none retrieved; the mutation-accumulation record shows lost variants leaving no sequence trace in the survivors | n/a | held-open | https://doi.org/10.1073/pnas.1210309109 | 2026-09-28 |

## Scientific Inquiry run

1. Question (precise): Do canon's two claims — an optimal mutation rate, and survivors carrying forward failed variants' information — correspond to anything measured at the population level in bacteria?
2. What an answer must look like: for the first, a fitness-versus-mutation-rate curve with an interior maximum; for the second, a measured informational residue of eliminated variants in a survivor genome.
3. Falsifiability condition: claim (b) as marked "Confirmed" is falsified if mutation-accumulation sequencing shows eliminated variants leaving no trace, and no other mechanism supplies one.
4. Variables: measurable / bounded / held open: Measurable: the realised mutation rate, its spectrum, its strand asymmetry, the indel/substitution ratio. Bounded: the rate is modulable (MMR is regulated, and natural isolates vary), so an optimum is plausible. **Held open: the optimum itself, and any informational residue of failed variants.** Not filled.
5. Test designed: fetch the reference mutation-accumulation measurement; attempt the original fluctuation-test source; look for a measured residue of eliminated variants.
6. Data (unfiltered): table above, including three held-open rows recorded with their reasons.
7. Variable Principle applied: canon's "optimal mutation rate" is a plausible structure with no fetched measurement behind it — it stays `live-hypothesis`, and the optimum is **not** filled in. Canon's "Confirmed" on the Layer I.G biological row is not supported by anything fetched here: conservation, non-coding DNA and immune memory are separate phenomena and none of them is a record of *eliminated* variants. The correct status is `unobserved-claim`, and this audit does not close it.
8. Model update (Capsule: what the failed parts contribute): the measured facts that survive and are useful are the modulability of the rate (MMR is regulated; natural isolates lack it) and the strand asymmetry, which shows the mutation process is not an undirected exploration but a structured one keyed to replication geometry. Canon's "exploration of fitness space" is therefore an under-description, not a confirmation.
9. Documented: this file. Correspondence: one scale down, the three-stage fidelity architecture (SWEEP-012) is what *sets* the rate, so the "optimal mutation rate" is an optimum over the amount of discarding the cell does; one scale up, population-level Luria-Delbruck statistics, which the fetched sources use as a method but whose original numbers were not retrievable.
10. Next baseline: a PRED test on the modulability relation (mutation rate as a function of MMR gene dosage or MMR status) rather than on the unmeasured optimum.

## Forcing Test

- Test A (Ground): Partially grounded. The realised rate and spectrum are measured; the optimum and the informational residue are not.
- Test B (Uniqueness): Not forced. Many mutation-rate models fit the single measured rate; nothing selects an optimum.
- Test C (Direction): Direction available for the modulation claim (MMR status changes rate and spectrum), not for the optimum.
- Test D (Falsifiability): Canon's Layer I.G "Confirmed" had a falsifier (no residue of eliminated variants) and the fetched record does not support the confirmation. Canon's optimum claim has no falsifier stated in canon; that is itself the finding.
- **Outcome:** `live-hypothesis` for the optimal mutation rate, with the attached falsifier: exhibit a fitness-versus-mutation-rate curve for a bacterium with no interior maximum. **Canon's "Confirmed" label on the Layer I.G biological row is withdrawn to `unobserved-claim`.** DPR mapping for mutation and selection: **after-the-fact** — the three operations are distributed across different entities and different timescales (variation in an individual genome, selection in a population, frequency change over generations), so no single system runs the loop.

## Anti-Operation (the gap this opens)

The realised mutation rate is set by machinery whose function is discard (SWEEP-012), and is modulable. So "optimal mutation rate" is really "optimal discard rate". Canon nowhere connects its Dynamic Middle to its conservation-of-information axiom, and at this scale the two are in tension: the dynamic middle requires discarding at some rate, the Capsule forbids discard. That tension is unresolved in canon and is the largest structural gap this sweep found.

## Narrative stripped (if any)

- Removed: "Confirmed (genomic conservation; junk DNA; immune memory)" as support for failed-variant information being carried forward. Genomic conservation records what survived; non-coding DNA is not a ledger of eliminated variants; immune memory (SWEEP-019) records encounters, not failed mutations.
- Removed: the Yin/Yang assignment of variation and selection. No measurement fetched here forces or contradicts it.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; grading not endorsed by the author.
```
