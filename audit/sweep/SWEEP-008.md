---
id: SWEEP-008
canon_ref: v5.1 Appendix A, Stage 24 (Ion Gradients / Membrane Potentials); v5.1 Appendix A, Stage 29 (Sensory Transduction)
canon_label: "Ion Gradients / Membrane Potentials — Na+/K+ ATPase establishes electrochemical asymmetry. Polarity deliberately created and maintained."
diff_state: methodology-gap
exclusion_diagnosis: not-reached
claim_outcome: stipulation
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix A, Stage 24: "Ion Gradients / Membrane Potentials | Na+/K+ ATPase establishes electrochemical asymmetry. Polarity deliberately created and maintained."

v5.1 Appendix A, Stage 29: "Sensory Transduction | DETECT becomes specialized hardware. Photons, sound waves, pressure all transduced into electrochemical signal."

v5.1 Layer I.D supplies the dynamic-middle account of holding a centre between extremes; Layer I.E (Energy Continuation) supplies "collapse seeds the next gradient".

Canon names no mechanosensitive channel, no osmotic regulation, and no release valve. Stage 24's only named mechanism is the eukaryotic Na+/K+ ATPase, which E. coli does not have. Stage 29 places pressure transduction at position 29, after multicellularity (25), tissue differentiation (26), organ systems (27) and the nervous system (28).

**Split.** *Factual core:* cells establish and maintain ion gradients across membranes; pressure is transduced into an electrochemical signal by specialized hardware. *Framework mapping:* "deliberately created"; the stage position of sensory transduction; Layer I.D's dynamic middle.

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Midpoint membrane tension for opening MscL, purified protein reconstituted in liposomes, tension calculated from pressure and measured patch curvature | T(1/2) = 11.8 dyn/cm | as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=10102934&rettype=abstract&retmode=text (Sukharev et al. 1999, J Gen Physiol 113:525) | 2026-09-28 |
| Maximal slope sensitivity of MscL open/closed ratio | 0.63 dyn/cm per e-fold | as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=10102934&rettype=abstract&retmode=text | 2026-09-28 |
| Energy difference between closed and fully open MscL in an unstressed membrane | ΔE = 18.6 k_B T | as published, Boltzmann two-state fit | derived | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=10102934&rettype=abstract&retmode=text | 2026-09-28 |
| In-plane area change on MscL opening | ΔA = 6.5 nm2 (two-state analysis); 6 nm2 summed over all transitions | as published | derived | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=10102934&rettype=abstract&retmode=text | 2026-09-28 |
| Number of conducting states of MscL | four conducting states plus a closed state; the rate-limiting step is the transition from closed to the lowest conductance substate | as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=10102934&rettype=abstract&retmode=text | 2026-09-28 |
| Midpoint membrane tension for opening MscS, purified 31 kDa protein in soybean asolectin liposomes | 5.5 dyn/cm | ± 0.1 dyn/cm | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=12080120&rettype=abstract&retmode=text (Sukharev 2002, Biophys J 83:290) | 2026-09-28 |
| Energy of opening and area change for MscS | ΔG = 11.4 k_B T; ΔA = 8.4 nm2 | ± 0.5 k_B T; ± 0.4 nm2 | derived | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=12080120&rettype=abstract&retmode=text | 2026-09-28 |
| Activation pressures for MscS in patches | 20–60 mm Hg | as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=12080120&rettype=abstract&retmode=text | 2026-09-28 |
| Gating requirement for MscS | the isolated protein alone is sufficient to form a channel gated directly by tension in the lipid bilayer | as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=12080120&rettype=abstract&retmode=text | 2026-09-28 |
| Set-point of the channels relative to cell failure, E. coli mutants lacking YggB (MscS) and MscL | mechanosensitive channels "open at a pressure change just below that which would cause cell disruption leading to death" | as published, from mutant survival on osmotic downshock | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=10202137&rettype=abstract&retmode=text (Levina et al. 1999, EMBO J 18:1730) | 2026-09-28 |
| Size of the MscL gene product | a unique protein of only 136 amino acids | exact from sequence | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=7511799&rettype=abstract&retmode=text (Sukharev et al. 1994, Nature 368:265) | 2026-09-28 |

## Scientific Inquiry run
1. Question (precise): Does a canonical item hold bacterial mechanosensation and osmotic sensing, and does DETECT → PROCESS → RESPOND fit a channel that is gated directly by bilayer tension?
2. What an answer must look like: the canonical item that would cover it; the molecule and event assigned to each operation; and a statement of whether any step intervenes between stimulus and output.
3. Falsifiability condition: the three-operation decomposition fails for this mechanism if the stimulus acts on the output element directly, with no intervening transduction step — that is, if DETECT and RESPOND are the same physical event in the same molecule.
4. Variables: measurable / bounded / held open: measurable — midpoint tensions, slope sensitivity, activation pressures, sufficiency of the isolated protein, survival phenotype, protein length. Bounded — ΔG and ΔA (fitted from a two-state model). Held open — whether a two-operation device counts as an instance of a three-operation algorithm.
5. Test designed: fetch the MscL and MscS gating-parameter measurements and the genetic osmotic-downshock study; compare midpoint tensions; ask where a processing step could be located.
6. Data (unfiltered): MscL opens with midpoint tension 11.8 dyn/cm, MscS with 5.5 ± 0.1 dyn/cm — MscS opens at less than half the tension MscL needs. MscS gating needs nothing but the purified protein and a lipid bilayer under tension. MscL has four conducting states, not two. Both channels open just below the pressure change that would kill the cell. MscL is 136 amino acids.
7. Variable Principle applied: **Measured** — the two midpoint tensions, slope sensitivity, activation pressures, sufficiency, the lethality threshold relation. **Structurally derived** — ΔG, ΔA. **Held open** — the operation count. The DPR mapping: DETECT = tension in the lipid bilayer; RESPOND = the open pore releasing solute. There is **no PROCESS**. The tension acts on the channel's in-plane area directly; the same 6.5 nm2 expansion that *is* the response is also what *registers* the stimulus. Assigning a PROCESS step here requires calling the conformational change both the detection and the processing, which is exactly the relabeling the brief asks to be flagged. This is the clearest measured counterexample in the sweep to the claim that the algorithm has three irreducible operations: here it has two, and they are the same event viewed from either side of the membrane.
8. Model update (Capsule: what the failed parts contribute): canon should either (a) state that DETECT and RESPOND may be co-located in one molecule with PROCESS reduced to the identity, or (b) restate the base code as a minimum of two operations with PROCESS as the variable-quality third. The audit does not choose between them — that is the author's declaration to make. What the failure contributes is the *sharpest* instance of canon's own central claim that "processing architecture is everything": in a direct-gated channel the processing architecture is a protein's mechanical compliance, and its quality is measurable as the slope sensitivity, 0.63 dyn/cm per e-fold.
9. Documented: this file.
10. Next baseline: unmapped-in-effect and graded as a gap against Stage 24, whose only named mechanism is eukaryotic. The two-versus-three operation question is named and held open, joined with the variable opened in SWEEP-007.

## Forcing Test
- Test A (Ground): grounded. Two independent reconstitution studies and one genetic study, fetched this run.
- Test B (Uniqueness): unique for the negative claim. Given that the purified protein in a bare bilayer is sufficient, no account with an intervening transduction molecule survives.
- Test C (Direction): canon runs stimulus → transduction → electrochemical signal → response (Stage 29). The measurement runs stimulus → response, with the "electrochemical signal" being the response itself (solute efflux).
- Test D (Falsifiability): the condition at step 3 was stated in advance and is met.
- **Outcome:** `stipulation` for canon's items, which do not reach the mechanism: Stage 24 names a eukaryotic pump and Stage 29 places pressure transduction after nervous systems. DPR mapping: **no** — the measured device has two operations, not three, and the third can only be supplied by relabeling. `methodology-gap`, diagnosis `not-reached`. Intake `open`, not `adjusted`: each gating measurement is `measured-single`, so per substrate item 8 it may not force canon to re-form.

## Anti-Operation (the gap this opens)

- A two-operation device in a framework built on three. The variable named in SWEEP-007 is now supported by a second, independent instance, and it is the deepest open question this sweep produces: what measurement would show that PROCESS is a *necessary* operation rather than a describable one?
- MscS opens at 5.5 dyn/cm and MscL at 11.8 dyn/cm — a graded, two-threshold release system. Canon's Layer I.D has one middle, not a staged sequence of relief valves. Multi-threshold safety architecture is unmapped.
- The channels are tuned to open just below lethal tension. That is a measured relationship between a control set-point and a failure point. Canon asserts resilience as a Pillar (Layer I.B, Layer V) but names no quantity relating the trigger to the failure limit.

## Narrative stripped (if any)

- "Polarity deliberately created and maintained" (Stage 24): the measured gradient across an E. coli membrane is maintained by respiration and spent by, among other things, a motor (SWEEP-003) and released by a tension-gated hole. "Deliberately" is not forced.
- "DETECT becomes specialized hardware" at Stage 29: the hardware exists in a 136-amino-acid bacterial protein, which by canon's own Appendix A ordering would be available from Stage 14 onward. The stage placement is stripped as a claim about time; see SWEEP-009 for the general form of this error.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; audit commentary is not endorsed by the author.
```
