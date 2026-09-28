---
id: SWEEP-029
canon_ref: none
canon_label: none
proposed_label: "Bacterial cell envelope: peptidoglycan sacculus, its synthesis machinery, and measured turgor pressure"
diff_state: unmapped
exclusion_diagnosis: not-reached
claim_outcome: live-hypothesis
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

Nothing, on the mechanical envelope. The nearest canonical items, quoted in full so the absence is checkable:

v5.1 Appendix A, Stage 12: "Lipid Bilayer / Protocell Formation | First boundary between inside and outside. Detection becomes possible because there is now a self."

v5.1 Layer III, "The Cell — All Seven Hermetic Principles in One Unit", Polarity row: "Anabolic (building) vs. catabolic (breaking down) — both continuously operating. Balance = health."

Neither reaches the load-bearing wall. No stage in Appendix A's progression, and no row of Appendix D's Biological & Scaling Laws, names peptidoglycan, a cell wall, turgor pressure, the elongasome, or the divisome. Stage 12 gives the cell a *membrane* and then moves directly to chemiosmosis (13) and LUCA (14). `canon_ref: none` is therefore not an oversight in this record — it is the finding.

## Reality shows

Reference organism: *Escherichia coli* (turgor, wall elasticity, sacculus thickness); *Pseudomonas aeruginosa* given for contrast where the same study measured it.

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Turgor pressure in living *E. coli*, from atomic force microscopy on intact and bulging cells | 29 ± 3 kPa | ±3 kPa as published | measured-single | https://pubmed.ncbi.nlm.nih.gov/22107320/ | 2026-09-28 |
| Young's modulus of the *E. coli* cell wall in intact (pressurised) cells, axial and circumferential | 23 ± 8 MPa and 49 ± 20 MPa | ± as published | measured-single | https://pubmed.ncbi.nlm.nih.gov/22107320/ | 2026-09-28 |
| Stress-stiffening exponent of the *E. coli* cell wall (power law) | 1.22 ± 0.12 | ±0.12 as published | measured-single | https://pubmed.ncbi.nlm.nih.gov/22107320/ | 2026-09-28 |
| Comparison of pressurised with unpressurised sacculi | the wall is "significantly stiffer in intact cells than in unpressurised sacculi" — the mechanical property depends on the load | as published | measured-single | https://pubmed.ncbi.nlm.nih.gov/22107320/ | 2026-09-28 |
| Thickness of air-dried *E. coli* sacculi by atomic force microscopy | 3.0 nm (*P. aeruginosa*: 1.5 nm); on rehydration both "swelled to double their anhydrous thickness" | as published | measured-single | https://pubmed.ncbi.nlm.nih.gov/10559150/ | 2026-09-28 |
| Independent check on that thickness | computer simulation with a 0.3 nm Debye shielding length gives a mass-distribution full width at half height of 2.4 nm, "in essential agreement" | as published | derived | https://pubmed.ncbi.nlm.nih.gov/10559150/ | 2026-09-28 |
| Glycan interstrand spacing in sacculi, and inferred natural spacing in cells | 1.3 nm measured (Burge et al.); natural spacing in cells inferred at 1.6–2.0 nm | as published | derived | https://pubmed.ncbi.nlm.nih.gov/10559150/ | 2026-09-28 |
| What cells expand in proportion to biomass growth | **surface area**, not volume; the surface-to-mass ratio remains nearly constant on the generation timescale | as published, quantitative phase microscopy | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC8364103/ | 2026-09-28 |
| Determinant of cell width, and hence of dry-mass density | cell width is controlled independently of surface-to-mass coupling, with "an important influence of turgor pressure"; plastic width changes after nutrient shifts are driven by turgor variations | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC8364103/ | 2026-09-28 |
| Constancy of bacterial dry-mass density | **not constant** — "our findings overturn a long-standing paradigm of mass-density constancy in bacteria" | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC8364103/ | 2026-09-28 |
| Processive rate of septal peptidoglycan synthesis by the FtsWIQLB–FtsN complex on the "sPG track" | ~8 to 9 nm/s | as published | derived | https://pmc.ncbi.nlm.nih.gov/articles/PMC12260396/ | 2026-09-28 |
| Consequence of losing one wall-synthesis enzyme at the division site: PBP1b produces a wedge-like density of PG; its loss weakens the site, making it "hypersusceptible to osmotic lysis" | as stated, in situ cryo-electron tomography | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC13423804/ | 2026-09-28 |
| Rate of peptidoglycan turnover per generation in *E. coli* | not retrieved | n/a | held-open | no primary measurement reached this run; not filled from memory | 2026-09-28 |

## Scientific Inquiry run

1. Question (precise): Does any canonical item hold the bacterial cell envelope — the peptidoglycan sacculus, its synthesis machinery, and the turgor pressure it contains — and does DETECT → PROCESS → RESPOND fit the measured mechanism of wall growth?
2. What an answer must look like: either a canonical stage or layer row that names a cell wall or a mechanical load, or a demonstration that none exists; plus measured turgor, wall stiffness and sacculus thickness with uncertainties.
3. Falsifiability condition: the `unmapped` grade fails if any canonical item names a cell wall, peptidoglycan, turgor, or mechanical load. Searching Appendix A's 100 stages, Appendix D's law registry, Layer I.C Domains 8–10 and Layer III's cell table found none.
4. Variables: measurable / bounded / held open: **Measurable** — turgor, Young's modulus (two axes), stress-stiffening exponent, sacculus thickness, sPG synthesis rate. **Bounded** — turgor 26–32 kPa; sacculus 3–6 nm depending on hydration. **Held open** — PG turnover rate; whether the author intends any stage to hold the envelope.
5. Test designed: search canon for the component; then fetch the primary measurements of the mechanical quantities; then attempt the DPR assignment for wall growth.
6. Data (unfiltered): the table above. Note the two results that cut against tidy expectations: wall stiffness is anisotropic by roughly a factor of two between axes, and dry-mass density is *not* constant — both are properties a framework built on self-similarity and balance would not predict.
7. Variable Principle applied: the absence in canon is recorded as an absence, not as an implicit presence inside Stage 12's "boundary". Stage 12 names a lipid bilayer; a bilayer cannot hold 29 kPa, so reading the wall into that stage would fill a variable with an assumption.
8. Model update (Capsule: what the failed parts contribute): canon needs an envelope item, and it will not fit as a stage in a progression, because the wall is not a step between two others: it is a *constraint that operates during every later step*. The failed placement contributes a structural point — Appendix A can express sequence but not concurrent constraint, which is the same limitation SWEEP-026 found for branches.
9. Documented: this file. Attempted DPR assignment: **DETECT** → mechanical strain in the existing sacculus (turgor stretches it, and turgor is measured to be required for surface expansion); **PROCESS** → insertion of new glycan strands by the elongasome, whose rate depends on that strain; **RESPOND** → expanded surface at constant surface-to-mass ratio. This is the most defensible DPR assignment in the sweep after SWEEP-025 and SWEEP-033, because the mechanical load genuinely feeds back on the enzymes. But it has no boundary at the DETECT step: strain is not detected by anything, it lowers a free-energy barrier. The "detector" is the same molecule as the "processor", and there is no signal, so the three labels partition nothing. **DPR mapping: applied after the fact** — this is mechanics, and mechanics has no information step.
10. Next baseline: a PG turnover measurement, and a decision from the author on whether concurrent constraints get stages. Re-review 2027-09-24.

## Forcing Test

- Test A (Ground): Grounded for every mechanical quantity recorded.
- Test B (Uniqueness): No canonical candidate exists to be unique or not. That is what `unmapped` records.
- Test C (Direction): Measured: turgor loads the wall, the wall constrains shape, and shape plus surface-to-mass coupling set dry-mass density.
- Test D (Falsifiability): The `unmapped` grade is falsifiable by producing the canonical item that holds this. None was found.
- **Outcome:** `live-hypothesis` — for canon's implicit claim that its 17 layers and 100 stages hold every process. A whole load-bearing subsystem of the best-studied organism on Earth is absent, so the claim stands as a hypothesis with a counterexample pending placement, not as a demonstrated result.

## Anti-Operation (the gap this opens)

Two gaps. (i) A framework with no cell wall has no account of *lysis* — the measured failure mode in which a cell dies from its own internal pressure when one enzyme is missing. Canon's Layer I.E treats cell death as gradient-seeding (apoptosis) and its Domain 9 treats it as function-completion; osmotic rupture is neither, and it is the commonest way a bacterium dies. (ii) Anisotropic stiffness and non-constant mass density are measured facts about a system canon calls the highest-density expression of organised complexity; if the density is not constant, `CLAIM-003`'s "per unit volume" metric has a moving denominator.

## Narrative stripped (if any)

Stripped from the nearest canonical item, Stage 12: "Detection becomes possible because there is now a self." Reality forces neither clause. A lipid vesicle establishes a diffusion barrier; it does not establish detection (no measured sensor), and "a self" is an interpretation with no measurable referent at this stage. The measured content of Stage 12 is compartmentalisation, which is real and important, and which this record leaves intact.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
