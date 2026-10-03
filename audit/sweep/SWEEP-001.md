---
id: SWEEP-001
canon_ref: v5.1 Layer I.C Domain 9 (Biological Process), Algorithm row; v5.1 Layer 0 Cross-Domain Convergence Table, Biological row
canon_label: "Biological Process — DETECT: internal deviation or external threat; PROCESS: cellular signaling cascade + gene expression; RESPOND: adapted equilibrium"
diff_state: methodology-gap
exclusion_diagnosis: not-reached
claim_outcome: stipulation
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Layer 0, Cross-Domain Convergence Table, Biological row: "DETECT: Homeostatic deviation or threat | PROCESS: Cellular signaling cascade + gene expression | RESPOND: Adapted equilibrium."

v5.1 Layer I.C Domain 9, Algorithm row: "DETECT: Internal deviation or external threat. PROCESS: Cellular response — gene expression, protein synthesis, metabolic shift, immune activation. RESPOND: Adapted state, corrected equilibrium."

Domain 9 Biological Process Algorithm, step 1: "Identify the biological system and its homeostatic set-point for each measurable variable." Step 2: "Detect deviations from set-point."

Canon names no chemoreceptor, no receptor array, no covalent adaptation mechanism, and no post-translational signalling anywhere in the 17 layers, the ten domains, Appendix A, or Appendix D. Searched: `chemotax`, `receptor array`, `methylation` as an adaptation mechanism — absent.

**Split.** *Factual core:* a cell detects an external chemical, processes the signal, and adapts. *Framework mapping:* the assignment of DETECT / PROCESS / RESPOND to particular molecular events, and the claim that the processing content is "gene expression, protein synthesis, metabolic shift, immune activation".

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Chemoreceptor array lattice, centre-to-centre hexagon spacing, 13 distantly related bacterial species across several phyla | 12 nm | reported as "consistently 12 nm"; no formal σ given | measured-reproduced | https://pmc.ncbi.nlm.nih.gov/articles/PMC2761316/ (Briegel et al. 2009, PNAS 106:17181) | 2026-09-28 |
| Distance from inner membrane to CheA/CheW base plate, E. coli | 22 nm (range 21–31 nm across the 13 species) | constant within each species | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC2761316/ | 2026-09-28 |
| Estimated receptors per polar array, E. coli (from array surface area ≈53,000 nm2, hexagonal trimer-of-dimers packing) | ≈5,200 | estimate from measured surface area | derived | https://pmc.ncbi.nlm.nih.gov/articles/PMC2761316/ | 2026-09-28 |
| Apparent dissociation constant for MeAsp response, wild-type E. coli, FRET (CheY/CheZ) | K_D = 2.6 µM | ± 0.5 µM | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC117525/ (Sourjik & Berg 2002, PNAS 99:123) | 2026-09-28 |
| Apparent dissociation constant, adaptation-deficient cheRcheB (EEEE) strain, same assay | K_D1 = 38 µM, K_D2 = 83 mM | ± 5 µM; ± 17 mM | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC117525/ | 2026-09-28 |
| Ratio of half-maximal response concentration, cheRcheB to wild type (sensitivity gained by methylation-based adaptation) | 35 | as published | derived | https://pmc.ncbi.nlm.nih.gov/articles/PMC117525/ | 2026-09-28 |
| Hill coefficient of the FRET dose-response, wild-type cells | 1.2 | ± 0.1 | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC117525/ | 2026-09-28 |
| Slope of FRET response versus fractional change in receptor occupancy (amplification at the kinase) | −36 (attractant addition); 27 (attractant removal) | ± 1; ± 2 | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC117525/ | 2026-09-28 |
| Number of methylation sites on Tar (glutamates, two expressed as glutamines deamidated by CheB) | 4 | exact count | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC117525/ | 2026-09-28 |
| Adaptation time of cheRcheB cells to a step of attractant | no adaptation over periods up to 12 s; partial adaptation with decay time >30 s in a flow cell | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC387059/ (Segall, Block & Berg 1986, PNAS 83:8987) | 2026-09-28 |

## Scientific Inquiry run
1. Question (precise): Does any canonical item hold the E. coli chemoreceptor array and its methylation-based adaptation, and does DETECT → PROCESS → RESPOND map onto the measured mechanism at distinguishable step boundaries?
2. What an answer must look like: (a) a named canonical item whose text covers a transmembrane receptor cluster and a covalent adaptation memory, or a demonstration that none exists; (b) for each of the three operations, the molecule and the chemical event assigned to it, plus a statement of whether the measured mechanism has a boundary there.
3. Falsifiability condition: the mapping is *after the fact* if two of the three operations are carried by the same molecule undergoing the same class of change, so that the split between them is a naming choice rather than a measurable transition. It fits if each operation corresponds to a distinct measurable chemical event.
4. Variables: measurable / bounded / held open: measurable — lattice spacing, base-plate distance, K_D per modification state, Hill coefficient, amplification slope, methylation site count. Bounded — receptor number per array (derived from area). Held open — whether canon intends Domain 9 to cover prokaryotic chemosensing at all, since it names none.
5. Test designed: grep the whole canonical corpus for chemotaxis and receptor-array terms; then fetch the cryo-ET array measurement (Briegel 2009) and the in vivo FRET dose-response series across methylation states (Sourjik & Berg 2002) and assign DPR explicitly.
6. Data (unfiltered): the 12-nm hexagonal array is conserved across 13 species from several phyla. In E. coli the array holds ≈5,200 receptors at one pole. Wild-type K_D = 2.6 ± 0.5 µM; the adaptation-deficient cheRcheB strain responds only at K_D1 = 38 ± 5 µM and K_D2 = 83 ± 17 mM — 35-fold less sensitive. Hill coefficient of the dose-response is 1.2 ± 0.1, i.e. the receptor is not itself a cooperative switch; the amplification (slope −36 ± 1) sits between receptor occupancy and kinase activity. Canon mentions none of this. Canon's grep returns zero hits for chemotaxis.
7. Variable Principle applied: **Measured** — array geometry, K_D per modification state, amplification slope, methylation site count, absence of adaptation without CheR/CheB. **Structurally derived** — receptor count per array. **Held open** — the DPR assignment itself. Concretely: DETECT = MeAsp or aspartate binding the Tar periplasmic domain; PROCESS = the change in receptor-array modification state (methyl-glutamate occupancy) and the resulting shift in the active/inactive equilibrium of the coupled CheA; RESPOND = the change in CheA kinase activity. The DETECT boundary is real and measurable (ligand occupancy is an independent observable, and the reported slope is taken against it). The DETECT/PROCESS boundary is **not** a mechanical boundary: ligand binding and methylation act on the *same* receptor dimer, shifting the *same* two-state equilibrium in opposite directions — that is why methylation "compensates for attractant binding". Calling one of the two chemical modifications of one molecule "detection" and the other "processing" is a relabeling, not a measured transition. Canon's stated PROCESS content ("gene expression, protein synthesis, metabolic shift, immune activation") is absent here: no transcription occurs at any point in chemotactic adaptation.
8. Model update (Capsule: what the failed parts contribute): Domain 9's PROCESS list is transcription-centric and misses the whole class of post-translational, covalent-modification signalling — the dominant fast-signalling mode in the domain of life that contains most of its biomass. The failed part is informative: it shows Domain 9 was written from a metazoan homeostasis template (set-point, hormone cascade, immune memory, HRV), and that template does not reach the prokaryotic case. Proposed addition to Domain 9's PROCESS: "covalent modification of an existing protein (phosphorylation, methylation) without transcription".
9. Documented: this file.
10. Next baseline: array geometry and adaptation sensitivity are accounted by measurement and unmapped by canon; the DETECT assignment is defensible, the DETECT/PROCESS split is a stipulation. Held open: whether canon will name a prokaryotic sensing item at all.

## Forcing Test
- Test A (Ground): grounded. Cryo-ET on 13 species and in vivo FRET across engineered modification states are direct measurements, fetched this run.
- Test B (Uniqueness): not unique. At least two assignments of DPR to this machinery are equally consistent with the data (ligand binding as DETECT with methylation as PROCESS; or the whole receptor as DETECT with the phosphorelay as PROCESS — see SWEEP-002). Nothing in the measurement selects one.
- Test C (Direction): canon runs from the algorithm to the mechanism (the mechanism is expected to exhibit three operations). The measurement runs from the molecule outward and finds one receptor dimer integrating two opposed covalent inputs into one equilibrium. The directions differ.
- Test D (Falsifiability): the condition set at step 3 was met — two operations are carried by one molecule via the same class of change — so the mapping is applied after the fact at that boundary.
- **Outcome:** `stipulation`. Canon has no item that holds the chemoreceptor array; the closest (Domain 9) names a PROCESS content that does not occur here. The DETECT assignment survives; the DETECT/PROCESS boundary does not. `methodology-gap`, diagnosis `not-reached`: the registry has not grown to post-translational signalling.

## Anti-Operation (the gap this opens)

- If one molecule can carry both DETECT and PROCESS, the three operations are not guaranteed to be three *parts*. What measurement would distinguish "three operations in one molecule" from "one operation described three ways"? Unanswered, and it applies to every layer.
- The 12-nm lattice is conserved across phyla that diverged billions of years ago. Canon has no item for a conserved *geometry* — only for conserved code (DNA) and conserved algorithm. A third conserved thing is unaccounted for.
- Canon's Appendix D holds constants and laws but no biological structural invariants. 12 nm is a candidate; the audit has no test for admitting one.

## Narrative stripped (if any)

- "Homeostatic deviation or threat" as the universal DETECT input: an attractant gradient is neither a deviation from an internal set-point nor a threat. The narrative frames detection as *defensive*; the measured system spends its sensing budget on opportunity, not danger. Reality does not force the defensive framing.
- "Third (homeostatic regulatory intelligence)" as the Kingdom lean of Domain 9: the measured adaptation mechanism is two enzymes, CheR and CheB, acting on four glutamates. No observation forces or forbids the "intelligence" label; it adds nothing measurable.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; audit commentary is not endorsed by the author.
```
