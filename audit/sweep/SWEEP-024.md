---
id: SWEEP-024
canon_ref: "v5.1 Appendix A, Stage 22 'ATP Synthase / Chemiosmotic Coupling'; with v5.1 Appendix D, Biological & Scaling Laws, row 'ATP Yield Per Glucose'"
canon_label: "ATP Synthase / Chemiosmotic Coupling"
proposed_label: "F1Fo ATP synthase: measured rotor stoichiometry and proton-per-ATP ratio"
diff_state: methodology-gap
exclusion_diagnosis: not-reached
claim_outcome: live-hypothesis
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix A, Stage 22:

> "ATP Synthase / Chemiosmotic Coupling | Protons flow back through ATP synthase. Mechanical rotation drives ADP → ATP. ≈32 ATP per glucose. Dynamic middle of all energy metabolism."

**Split (RUNBOOK rule 4).** *Factual core graded here:* protons flowing back through ATP synthase drive mechanical rotation which phosphorylates ADP; the yield is ≈32 ATP per glucose.

*Framework mapping (not graded; see Narrative stripped):* "Dynamic middle of all energy metabolism."

Canon gives no rotor stoichiometry, no proton-per-ATP ratio, and no statement that the enzyme is reversible. The ≈32 figure is eukaryotic (see `audit/constants/CONST-atp-yield-per-glucose.md`, which grades it `live-hypothesis` within a 28–32 range); canon states no bacterial value.

## Reality shows

Reference organism: *Escherichia coli* for structure; chloroplast enzyme for the thermodynamic ratio (stated, because no *E. coli* thermodynamic H⁺/ATP measurement was reached this run).

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Rotational symmetry of the *E. coli* F1 and Fo motors, from nine cryo-EM structures in four discrete rotational sub-states | 3-fold (F1) and 10-fold (Fo), i.e. a c₁₀ ring | 3.1–3.4 Å resolution | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC7251095/ | 2026-09-28 |
| Structural H⁺/ATP for *E. coli*, from the c-ring : β-subunit ratio | 10/3 = 3.33 | exact given c₁₀ and 3 catalytic sites | derived | https://pmc.ncbi.nlm.nih.gov/articles/PMC7251095/ | 2026-09-28 |
| Thermodynamic H⁺/ATP ratio, chloroplast H⁺-ATP synthase, from the shift of the synthesis equilibrium with ΔpH (meta-analysis of the full published dataset) | 4.0 ± 0.1 | ±0.1 as published | measured-reproduced | https://pubmed.ncbi.nlm.nih.gov/26940516/ | 2026-09-28 |
| Structural H⁺/ATP for the same chloroplast enzyme, c/β | 14/3 = 4.7 | exact given c₁₄ | derived | https://pubmed.ncbi.nlm.nih.gov/26940516/ | 2026-09-28 |
| Ratio of thermodynamic to structural H⁺/ATP ("efficiency of the chemiosmotic energy conversion within the enzyme") | 0.85 | from the two rows above | derived | https://pubmed.ncbi.nlm.nih.gov/26940516/ | 2026-09-28 |
| Standard free energy for ATP synthesis (reference reaction) | ΔG°(ref) = 33.8 ± 1.3 kJ/mol | ±1.3 as published | measured-reproduced | https://pubmed.ncbi.nlm.nih.gov/26940516/ | 2026-09-28 |
| At equilibrium, ΔpH and ΔΨ are energetically equivalent for driving synthesis | as stated | meta-analysis conclusion | measured-reproduced | https://pubmed.ncbi.nlm.nih.gov/26940516/ | 2026-09-28 |
| Structural basis of directional control in a bacterial F1Fo: an F1 self-inhibition mechanism supporting "a unidirectional ratchet mechanism to avoid wasteful ATP consumption" (*Acinetobacter baumannii*) | as stated, three conformational states | cryo-EM, single study | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC8849298/ | 2026-09-28 |
| Measured in-vivo reverse flux (ATP hydrolysis pumping protons) through *E. coli* F1Fo during fermentative growth, as a rate | not retrieved | n/a | held-open | reversibility is standard textbook biochemistry, but no primary measurement of the *E. coli* reverse flux magnitude was reached this run; not filled from memory | 2026-09-28 |

Note the direction of the two ratio rows: the thermodynamic ratio (4.0) is *lower* than the structural ratio (4.7) in the one enzyme where both are measured. If the same 0.85 ratio held for *E. coli*, its thermodynamic H⁺/ATP would be near 2.8 rather than 3.33 — this is a derivation by analogy, **not** a measurement, and is not entered as one.

## Scientific Inquiry run

1. Question (precise): Does a canonical item hold the measured c-ring stoichiometry, proton-per-ATP ratio and reversibility of bacterial ATP synthase, and does DETECT → PROCESS → RESPOND fit the measured rotary mechanism?
2. What an answer must look like: canon's Stage 22 text; a measured rotor symmetry for *E. coli*; a measured H⁺/ATP with its uncertainty; a statement on reversibility with a source; and a named DPR assignment with its boundary test.
3. Falsifiability condition: canon's factual core fails if ATP synthase is shown not to rotate, or if phosphorylation is shown not to be driven by proton flow. It did not fail.
4. Variables: measurable / bounded / held open: **Measurable** — c-ring copy number, rotational sub-states, thermodynamic H⁺/ATP, ΔG°(ref). **Bounded** — *E. coli* structural H⁺/ATP = 10/3; its thermodynamic ratio bounded below 10/3 if the chloroplast efficiency carries over. **Held open** — the *E. coli* thermodynamic H⁺/ATP; the in-vivo reverse flux magnitude.
5. Test designed: fetch the *E. coli* structure paper for rotor symmetry; fetch a thermodynamic H⁺/ATP measurement; fetch structural evidence on directionality; then assign DPR and test the boundaries.
6. Data (unfiltered): the table above, including the row that fails to resolve — no *E. coli* thermodynamic ratio was reached.
7. Variable Principle applied: canon's "≈32 ATP per glucose" is filled; the bacterial ratios are held open. The gap between a *structural* ratio (countable from a structure) and a *thermodynamic* ratio (measured from an equilibrium shift) is a distinction canon does not make, and collapsing them would fill a variable with an assumption.
8. Model update (Capsule: what the failed parts contribute): canon's Stage 22 should carry the bacterial ratio 10/3 alongside the eukaryotic yield, and should state that the structural and thermodynamic ratios differ by a measured factor. The failed part — "≈32 ATP per glucose" used as if organism-independent — contributes the discovery that canon's energy accounting has no bacterial branch at all.
9. Documented: this file. Attempted DPR assignment: **DETECT** → protonation of the conserved carboxylate on a c-subunit from the periplasmic half-channel; **PROCESS** → rotation of the c₁₀ ring and the coupled γ-subunit, driving conformational cycling of the three β catalytic sites; **RESPOND** → release of ATP. Two objections make this arbitrary. First, the enzyme is reversible: run in the ATP-hydrolysis direction the same physical steps occur in reverse, so what was labelled RESPOND becomes the input and what was labelled DETECT becomes the output. A mapping whose direction flips with thermodynamic driving force is not detecting anything. Second, the 3-fold/10-fold symmetry mismatch means there is no fixed correspondence between one "detection" and one "response" — 10 proton events per 3 ATP, accommodated by measured torsional flexing. **DPR mapping: applied after the fact.**
10. Next baseline: a thermodynamic H⁺/ATP for *E. coli*, and a measured reverse-flux rate. Re-review 2027-09-24.

## Forcing Test

- Test A (Ground): Grounded for structure and for the chloroplast thermodynamic ratio; not grounded for the *E. coli* thermodynamic ratio.
- Test B (Uniqueness): Rotary chemiosmotic coupling is unique as the mechanism. "Dynamic middle of all energy metabolism" is not unique — canon names no quantity that would be at a middle, and no value it would take.
- Test C (Direction): Measured direction exists but is *reversible*, which canon does not state. The measured sign of the flux depends on Δp versus the phosphorylation potential.
- Test D (Falsifiability): The mechanism claim is falsifiable and has survived. The "dynamic middle" label is not falsifiable as written: no measurable quantity is named.
- **Outcome:** `live-hypothesis`. The mechanism half is well grounded; the framework label carried in the same cell of the table is unmeasurable as stated and travels on the mechanism's credibility.

## Anti-Operation (the gap this opens)

The structural ratio is countable and the thermodynamic ratio is measurable, and in the one enzyme where both exist they differ by 15%. That difference is the interesting quantity — energy that passes through the enzyme without shifting the ATP/(ADP·Pi) ratio — and canon has no item that can hold a systematic loss inside a machine it describes as a "dynamic middle". Naming the loss requires admitting that the coupling is not perfect, which is in tension with Layer I.E's "the energy did not diminish by one quantum".

## Narrative stripped (if any)

Removed: "Dynamic middle of all energy metabolism." No measurable quantity is named, no value is predicted, and no falsifier is attached, so this is a label rather than a claim. Also removed by implication: Layer I.E's "identical in quantity" reading, already graded in `CONST-atp-yield-per-glucose.md`; the 0.85 efficiency row above is a direct measurement that some throughput does not reach ATP.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
