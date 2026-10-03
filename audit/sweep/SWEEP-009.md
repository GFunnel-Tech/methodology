---
id: SWEEP-009
canon_ref: v5.1 Appendix A, Stage 29 (Sensory Transduction); v5.1 Layer 0 Cross-Domain Convergence Table, Biological row
canon_label: "Sensory Transduction — DETECT becomes specialized hardware. Photons, sound waves, pressure all transduced into electrochemical signal."
proposed_label: "Dedicated Signal-Transduction Hardware (prokaryotic two-component systems onward)"
diff_state: conflict
exclusion_diagnosis: reached-conflicting
claim_outcome: forced-no
intake_result: adjusted
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix A places sensory transduction at Stage 29, after: Stage 25 "Multicellularity", Stage 26 "Tissue Differentiation / Gene Expression", Stage 27 "Organ Systems / Homeostasis", Stage 28 "Nervous System | First organ whose function is processing itself. Body builds Second Kingdom organ. Process Density crosses emergence threshold."

Stage 29: "Sensory Transduction | DETECT becomes specialized hardware. Photons, sound waves, pressure all transduced into electrochemical signal."

Stage 14 is "LUCA — Last Universal Common Ancestor | All extant life descends from this single processing architecture. Three Kingdoms now coordinate at biological scale." Stages 15–16 are glycolysis and fermentation.

v5.1 Layer 0, Biological row: "PROCESS: Cellular signaling cascade + gene expression."

**Split.** *Factual core:* (a) detection is carried out by dedicated molecular hardware; (b) that hardware appears in the progression at position 29, after multicellularity and after the nervous system. *Framework mapping:* "Process Density crosses emergence threshold" at the nervous system; the Three Kingdoms reading of LUCA.

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Genes encoding two-component phosphotransfer signal transducers in the E. coli genome | at least 62 open reading frames: 32 response regulators, 23 orthodox sensory kinases, 5 hybrid sensory kinases | "at least"; complete-genome compilation | measured-reproduced | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=9205844&rettype=abstract&retmode=text (Mizuno 1997, DNA Res 4:161) and https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=15522865&rettype=abstract&retmode=text (Yamamoto et al. 2005, J Biol Chem 280:1448) | 2026-09-28 |
| Independent count of E. coli two-component components, biochemical survey | 30 sensor histidine kinases and 34 response regulators suggested to exist; catalytic domains of 27 HKs and all 34 RRs purified; self-phosphorylation detected for 25 HKs | counts differ slightly from the 1997 compilation | measured-reproduced | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=15522865&rettype=abstract&retmode=text | 2026-09-28 |
| Time for trans-phosphorylation from a phosphorylated histidine kinase to its cognate response regulator, in vitro, all pairs tested | all trans-phosphorylation took place within less than 1/2 min | as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=15522865&rettype=abstract&retmode=text | 2026-09-28 |
| Fraction of non-cognate kinase-regulator pairs showing detectable cross-talk in vitro | about 3% | as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=15522865&rettype=abstract&retmode=text | 2026-09-28 |
| Relation between self-phosphorylation rate and phosphorylation level across kinases | generally correlated, with named exceptions: level low for ArcB, HydH, NarQ, NtrB despite fast reaction; level high for slow species BasS, CheA, CreC | as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=15522865&rettype=abstract&retmode=text | 2026-09-28 |
| Phylogenetic origin of two-component signal transduction | "TCST systems are of bacterial origin and radiated into archaea and eukaryotes by lateral gene transfer"; trees built from 183 histidine kinases and 220 response regulators across 14 complete and 6 partial genomes; eukaryotic sequences fall almost exclusively in one cluster | inferred from distance-method phylogeny | derived | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=11110912&rettype=abstract&retmode=text (Koretke et al. 2000, Mol Biol Evol 17:1956) | 2026-09-28 |
| Architecture of the pathway | sensor histidine kinase receives the input stimulus and phosphorylates a response regulator, which effects a change in cellular physiology; the proteins have "an intrinsic modularity that separates signal input, phosphotransfer, and output response" | as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22746333&rettype=abstract&retmode=text (Capra & Laub 2012, Annu Rev Microbiol 66:325) | 2026-09-28 |

## Scientific Inquiry run
1. Question (precise): Does canon's Stage 29 hold two-component signal transduction, and does canon's stage *sequence* place dedicated detection hardware correctly in time?
2. What an answer must look like: the measured phylogenetic distribution and abundance of the hardware, compared against the canonical stage at which canon says such hardware appears.
3. Falsifiability condition: Stage 29's placement fails if dedicated signal-transduction hardware is measured to be present in organisms belonging to canon's Stages 14–16, i.e. prokaryotes, and therefore to predate Stages 25–28 by the whole span between them.
4. Variables: measurable / bounded / held open: measurable — gene counts in a complete genome, purification and phosphotransfer of the proteins, cross-talk fraction, transfer times. Bounded — phylogenetic origin (inference from trees, graded `derived`). Held open — the absolute age of the systems; no dating measurement was fetched, so the argument is ordinal, not in years.
5. Test designed: fetch two independent genome-scale inventories of E. coli two-component systems, the biochemical survey of all pairs, and a phylogenetic study of their distribution; compare against canon's stage ordering.
6. Data (unfiltered): E. coli alone carries at least 62 two-component ORFs on one independent count and 30 HKs plus 34 RRs on another. All cognate pairs tested transfer phosphate in under 30 s. About 3% of non-cognate pairs cross-talk. The systems are of bacterial origin and reached eukaryotes by lateral transfer. Their modularity explicitly separates input, phosphotransfer and output. Canon places "DETECT becomes specialized hardware" at Stage 29, fifteen stages after LUCA and one stage after the nervous system.
7. Variable Principle applied: **Measured** — the inventories, the phosphotransfer times, the cross-talk fraction. **Structurally derived** — the bacterial origin and lateral radiation. **Held open** — absolute dates. The DPR mapping here is the best fit in the entire corpus, and for a reason worth stating: the measured proteins are *modular by design*, and the modules are named in the literature as input, phosphotransfer, and output. DETECT = the sensor domain of the histidine kinase binding its stimulus; PROCESS = autophosphorylation on the conserved histidine and transfer to the aspartate of the response regulator; RESPOND = the phosphorylated regulator changing transcription or behaviour. Each is a separate domain of a separate protein with separately measurable kinetics. This is not a relabeling. The failure is not in the mapping; it is in the *placement*: canon's own Appendix A asserts an ordering that measurement contradicts by roughly two billion years of the progression's own span.
8. Model update (Capsule: what the failed parts contribute): Appendix A requires a prokaryotic sensory-transduction stage between Stage 14 (LUCA) and Stage 17 (oxygenic photosynthesis), and Stage 29 must be relabeled from "DETECT becomes specialized hardware" to something like "Multicellular sensory organs (specialized detection tissue)". The failed placement contributes the framework's strongest single piece of evidence: the base code's three operations are physically separable protein domains in the organisms canon places at Stage 14–16, which is a better demonstration of Layer 0 than anything canon currently cites for it. Canon loses evidence by placing the item late.
9. Documented: this file.
10. Next baseline: Stage 29's placement is ruled out; the proposed insertion and relabel are recorded. The mapping itself is accounted. Next: whether the same ordinal error affects other Appendix A stages whose mechanism is prokaryotic (see SWEEP-008 on Stage 24, which names a eukaryotic pump).

## Forcing Test
- Test A (Ground): grounded. Two independent genome-scale inventories (Nagoya 1997; Kinki/Nara 2005), one biochemical survey of every pair, one phylogenetic analysis across 20 genomes.
- Test B (Uniqueness): unique. Given 62 two-component ORFs in one bacterium and a bacterial origin for the family, no ordering that places dedicated detection hardware after multicellularity survives.
- Test C (Direction): canon runs complexity → organs → sensory hardware. Measurement runs sensory hardware → (much later) organs. The arrow is reversed for this item.
- Test D (Falsifiability): the condition at step 3 was stated in advance and is met.
- **Outcome:** `forced-no` for Stage 29's placement of specialized detection hardware after the nervous system. `conflict`, diagnosis `reached-conflicting`, intake `adjusted`: the contradicting observation — that prokaryotes carry dozens of dedicated, modular signal-transduction systems — is `measured-reproduced` across two independent inventories, which is what substrate item 8 requires. The adjustment is the stage insertion and relabel in step 8. DPR mapping: **fits**, with genuine step boundaries.

## Anti-Operation (the gap this opens)

- If the base code's three operations are literally three protein domains in a bacterium, then the strongest evidence for Layer 0 is prokaryotic, and the framework's Three Kingdoms hierarchy — which puts Third-Kingdom domains first and treats prokaryotes as First Kingdom — is ranking the evidence in the opposite order to its strength. That tension is unresolved.
- About 3% of non-cognate pairs cross-talk. Canon has no account of crosstalk, leakage, or specificity cost in any layer. A framework of clean cascades has nothing to say about the 3%.
- The audit graded a phylogenetic inference `derived`, not `measured`. The ordinal claim in this record therefore rests on an inference, not on a dated measurement. A molecular-clock or fossil-constrained date for two-component systems is the missing datum, and without it the conflict is about ordering only, not about elapsed time.

## Narrative stripped (if any)

- "Process Density crosses emergence threshold" at the nervous system (Stage 28): the quantity Process Density is not defined operationally anywhere in canon, so no threshold crossing can be checked. Not forced; not contradicted; unmeasurable as written.
- "Three Kingdoms now coordinate at biological scale" at LUCA (Stage 14): unaffected by this record either way. The measured fact — that LUCA-lineage organisms carry modular input/transfer/output hardware — neither forces nor forbids the Kingdom reading.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; audit commentary is not endorsed by the author.
```
