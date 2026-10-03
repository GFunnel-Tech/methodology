# Cell Information — How the Cell Cleans, Keeps and Updates What It Knows

> **Status: derivation / work-in-progress. Not canon.** Canon names pieces of this (v5.1 Domain 9: homeostasis, immune memory, apoptosis, "DNA as Base Code"; Domain 10: variation → selection → inheritance; Layer I.G: the Capsule) but gives no algorithm for how a cell keeps its information clean. Everything below is a derivation, built top-down by the rule in [`../membrane/README.md`](../membrane/README.md) (gap MF-03).

## What this area covers

"Cleaning of knowledge" is read here as four things the cell does with information:

1. **Filters** what comes in: signal vs. noise.
2. **Keeps** its stored record correct while copying and reading it.
3. **Erases** what is wrong, damaged or no longer needed.
4. **Updates** — within one lifetime (adaptation, memory) and across generations (evolution).

This is a **function area**, not a structure. It runs through the membrane, nucleus, cytoplasm and organelles. That exposes a gap in the atlas layout ([`gaps.md`](gaps.md) IG-07).

## Measured anchors

All values retrieved 2026-10-03. Grades follow [`audit/SCHEMA.md`](../../../audit/SCHEMA.md) §1.1.

| # | Quantity | Value | Grade | Source |
| --- | --- | --- | --- | --- |
| N1 | Replication fidelity contributed by proofreading (yeast nuclear DNA, URA3 reporter) | ~160-fold (leading strand), ~1000-fold (lagging) | measured-single | St Charles et al. 2015, *DNA Repair*, [doi:10.1016/j.dnarep.2015.04.006](https://doi.org/10.1016/j.dnarep.2015.04.006) |
| N2 | Replication fidelity contributed by mismatch repair (same study) | ~65-fold (leading), ~250-fold (lagging) | measured-single | as N1 |
| N3 | Human germline mutation rate | 1.20 × 10⁻⁸ per nucleotide per generation (mean father's age 29.7); about 2 more mutations per extra year of father's age | measured-single (78 trios) | Kong et al. 2012, *Nature* 488:471, [doi:10.1038/nature11396](https://doi.org/10.1038/nature11396) |
| N4 | Translation missense error (yeast, tRNA-Lys near-cognate codons) | 8 × 10⁻⁵ to 6.9 × 10⁻⁴ per codon | measured-single | Kramer et al. 2010, *RNA* 16:1797, [doi:10.1261/rna.2201210](https://doi.org/10.1261/rna.2201210) |
| N5 | Human genome under purifying selection | 8.2% (7.1–9.2%); only 2.2% constrained in both human and mouse since they diverged | derived (from comparative sequence) | Rands et al. 2014, *PLoS Genet.*, [doi:10.1371/journal.pgen.1004525](https://doi.org/10.1371/journal.pgen.1004525) |
| N6 | Share of human genome derived from transposable elements | about half | measured-reproduced | Lander et al. 2001, *Nature* 409:860, [doi:10.1038/35057062](https://doi.org/10.1038/35057062) |
| N7 | All-or-none, irreversible cell-fate switch built from positive feedback (Xenopus oocyte maturation) | bistable; persists after the stimulus is removed | measured-single | Xiong & Ferrell 2003, *Nature* 426:460, [doi:10.1038/nature02089](https://doi.org/10.1038/nature02089) |
| N8 | Gene-expression noise in yeast is controllable and gene-specific | qualitative | measured-single | Raser & O'Shea 2004, *Science* 304:1811, [doi:10.1126/science.1098641](https://doi.org/10.1126/science.1098641) |
| N9 | Autophagy is a genetically defined process (autophagy-defective yeast mutants isolated) | qualitative | measured-reproduced | Tsukada & Ohsumi 1993, *FEBS Lett.* 333:169 |

---

## L0 — The cell's information loop

| Role | At whole-cell scale |
| --- | --- |
| **Records held** | Genome (generations) · epigenome (cell divisions) · RNA and protein levels (hours) · signalling states (seconds to minutes) |
| **DETECT** | Outside, through the membrane (→ [membrane E](../membrane/README.md)); inside, through damage, misfolding and level sensors |
| **PROCESS** | Filter the input → compare it with the stored record → decide (switch, threshold, integrate) |
| **RESPOND** | Act (change expression) · store (memory) · **clean** (correct or erase) → new cell state |
| **Across generations** | Pass the record on (inheritance) with residual errors (variation). The environment selects what persists → next generation's baseline (canon Domain 10) |

---

## L1 → L2

Legend: ☐ queued · *source pending* = no measured source attached yet.

### A. Intake filtering — separating signal from noise

- ☐ A1 Thresholds, ultrasensitivity and bistable switches (N7)
- ☐ A2 Proofreading by delay at recognition (kinetic proofreading, Hopfield 1974 — a model; which steps are measured enters at the run)
- ☐ A3 Persistence filters: a signal must last long enough to count — *source pending*
- ☐ A4 Relative (fold-change) detection rather than absolute level — *source pending*
- ☐ A5 Noise: controlled and sometimes used (N8)

### B. Record fidelity — keeping the stored record correct

- ☐ B1 DNA copying: base selection → proofreading → mismatch repair (N1, N2)
- ☐ B2 DNA damage repair — *source pending*
- ☐ B3 Transcription fidelity — *source pending*
- ☐ B4 Translation fidelity (N4)
- ☐ B5 Protein folding quality control (chaperones) — *source pending*

### C. Erasure — removing what is wrong, damaged or no longer needed

- ☐ C1 Protein degradation (ubiquitin–proteasome) — *source pending*
- ☐ C2 Autophagy: bulk self-digestion and recycling (N9)
- ☐ C3 RNA decay, including decay of RNAs carrying premature stop signals (nonsense-mediated decay) — *source pending*
- ☐ C4 Signal termination (→ [membrane F4](../membrane/README.md))
- ☐ C5 Epigenetic resetting between generations — *source pending*
- ☐ C6 Removal of the whole cell: apoptosis (canon Domain 9 row)

### D. Memory — holding information over time

- ☐ D1 Short-term: modification states, ion levels
- ☐ D2 Switch memory: bistable states that outlast the signal (N7)
- ☐ D3 Epigenetic memory: chromatin marks, DNA methylation — *source pending*
- ☐ D4 Transcriptional memory: faster re-response to a repeated signal — *source pending*
- ☐ D5 Immune memory (organism scale; canon Domain 9 "Shepherd's Way" row)

### E. Adaptation within a lifetime

- ☐ E1 Desensitization: response fades under a constant signal
- ☐ E2 Set-point control: homeostasis (canon "Garlick Equilibrium" row)
- ☐ E3 Stress programs: heat shock, unfolded-protein response — *source pending*
- ☐ E4 Bet-hedging: noise splits a population across states (N8 as the basis)
- ☐ E5 Selection inside the body: immune-receptor gene rearrangement and hypermutation — *source pending*

### F. Evolution across generations

- ☐ F1 Variation: residual mutation (N3), set by the fidelity pipeline B1
- ☐ F2 Recombination (meiosis) — *source pending*
- ☐ F3 Selection: purifying selection removes harmful variants (N5)
- ☐ F4 What persists without being selected for: transposable-element-derived sequence (N6)
- ☐ F5 Inheritance outside the DNA sequence — **held open** ([`gaps.md`](gaps.md) IG-06)
- ☐ F6 Acquisition by merger: endosymbiosis (canon Stage 18)

---

## Correspondence check — the cell vs. the repository's own knowledge-cleaning rules

The Reality Audit has its own knowledge-cleaning rules (the [Reality Filter](../../../substrate/2026-09-24-reality-filter.md) and container rules). Checking them against what the cell does is a Correspondence test, one scale down. **Derivation; each row is a candidate, not a result.**

| Repository rule | Cell counterpart | Fit |
| --- | --- | --- |
| Filter item 8: *weak observations cannot force change* | Thresholds and bistable switches: a weak or brief input does not flip the switch (A1, D2, N7) | **Fits** |
| Filter item 1: *reality is the authority; the log adapts* | Selection: the environment decides which records persist; the genome adapts (F3) | **Fits**, at the generation scale |
| Container rule: *re-form, do not overwrite* | Mismatch repair and degradation **overwrite or erase**; the error and the old state are not kept (B1, C1–C3) | **Counter-instance** → IG-03 |
| Layer I.G (the Capsule): *nothing is discarded* | Erasure at every level; most sequence is not maintained (N5) | **Candidate conflict** → IG-01 |
| Shepherd's Way step 03, *Gather*: *filter nothing* | The cell filters at intake (A); its variation, by contrast, enters unfiltered and is filtered afterwards by selection (F1 → F3) | **Split by scale** → IG-02 |
| Filter item 3: *concentration discipline* | No clear counterpart found yet | Open |

## Patterns from this area

Added to [`../patterns.md`](../patterns.md) as P-06 to P-08.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Adapted; not endorsed by the author.
```
