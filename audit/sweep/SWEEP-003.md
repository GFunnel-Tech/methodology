---
id: SWEEP-003
canon_ref: v5.1 Appendix A, Stage 23 (ATP Hydrolysis / Cellular Work); v5.1 Appendix A, Stage 22 (ATP Synthase / Chemiosmotic Coupling)
canon_label: "ATP Hydrolysis / Cellular Work — energy captured by molecular machines: motor proteins, ion pumps, ribosomes, polymerases. Universal currency."
proposed_label: "Cellular Work from ATP Hydrolysis or Directly from an Ion-Motive Force"
diff_state: conflict
exclusion_diagnosis: reached-conflicting
claim_outcome: forced-no
intake_result: adjusted
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix A, Stage 23: "ATP Hydrolysis / Cellular Work | Energy captured by molecular machines: motor proteins, ion pumps, ribosomes, polymerases. Universal currency."

v5.1 Appendix A, Stage 22: "ATP Synthase / Chemiosmotic Coupling | Protons flow back through ATP synthase. Mechanical rotation drives ADP → ATP. ≈32 ATP per glucose. Dynamic middle of all energy metabolism."

v5.1 Appendix A, Stage 24: "Ion Gradients / Membrane Potentials | Na+/K+ ATPase establishes electrochemical asymmetry. Polarity deliberately created and maintained."

Canon names no flagellum and no rotary motor other than ATP synthase. In canon's sequence, the proton gradient is spent on ATP (Stage 22), and mechanical work follows from ATP hydrolysis (Stage 23).

**Split.** *Factual core:* mechanical work in cells is done by molecular machines powered by ATP hydrolysis, ATP being the universal currency. *Framework mapping:* Stage 22 as "the dynamic middle of all energy metabolism"; Stage 24 as polarity "deliberately created".

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Flagellar motor rotation speed as a function of protonmotive force, E. coli, light load | proportional to pmf over the whole accessible range, 0–270 Hz; stator units are ion-translocating, not ATP-hydrolysing | as published | measured-reproduced | https://pmc.ncbi.nlm.nih.gov/articles/PMC166384/ (Gabel & Berg 2003, PNAS 100:8748) and https://pmc.ncbi.nlm.nih.gov/articles/PMC1472430/ (Reid et al. 2006, PNAS 103:8066) | 2026-09-28 |
| Protonmotive force assumed for a fully energized E. coli cell in that analysis | ≈150 mV | stated as an assumption from the cited literature | derived | https://pmc.ncbi.nlm.nih.gov/articles/PMC166384/ | 2026-09-28 |
| Components of the pmf at external pH 7.0 and cytoplasmic pH 7.6 | Δψ ≈ −115 mV; −59ΔpH ≈ 35 mV | as published | derived | https://pmc.ncbi.nlm.nih.gov/articles/PMC166384/ | 2026-09-28 |
| Motor torque near stall, measured with an optical trap, tethered E. coli | ≈4,500 pN nm (one cell ≈4,800 pN nm) | approximate; source notes uncertainty from optical perturbation | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC25012/ (Berry & Berg 1997, PNAS 94:14433) | 2026-09-28 |
| Force at the periphery of the C ring implied by that torque | ≈200 pN total; ≈25 pN from each of eight force-generating elements | derived in source from the torque and the C-ring radius | derived | https://pmc.ncbi.nlm.nih.gov/articles/PMC25012/ | 2026-09-28 |
| Torque-speed relationship, E. coli, 23 °C | torque approximately constant to a knee speed near 200 Hz, then falls rapidly to zero-torque speed ≈350 Hz | as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=10653817&rettype=abstract&retmode=text (Chen & Berg 2000, Biophys J 78:1036) | 2026-09-28 |
| Temperature dependence of torque by regime | low-speed regime insensitive to temperature; high-speed regime decreases markedly at lower temperature (22.7, 17.7, 15.8 °C) | as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=10653817&rettype=abstract&retmode=text | 2026-09-28 |
| Maximum number of torque-generating stator units resolved by resurrection, E. coli, three stator combinations | at least 11 | at least; distinct speed increments counted | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC1472430/ | 2026-09-28 |
| Equivalence of stator units in a fully induced motor | not equivalent — speed increments at high unit numbers are smaller than at low unit numbers | as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC1472430/ | 2026-09-28 |
| Gene products required for motor assembly, E. coli, and number present in the final structure | ≈40 required; ≈20 present in the structure | approximate as published | measured-single | https://pmc.ncbi.nlm.nih.gov/articles/PMC1472430/ | 2026-09-28 |

## Scientific Inquiry run
1. Question (precise): Does a canonical item hold the bacterial flagellar motor, and is canon's Stage 23 claim — that cellular mechanical work is done by machines running on ATP as the universal currency — consistent with the measured energetics of the largest bacterial motor?
2. What an answer must look like: a direct measurement of the motor's energy source and its dependence on that source, plus the canonical sentence that would have to change.
3. Falsifiability condition: Stage 23 read as "molecular machines that do mechanical work are powered by ATP hydrolysis" fails if a major molecular machine's output is measured to depend on an ion-motive force and not on ATP.
4. Variables: measurable / bounded / held open: measurable — speed versus pmf, torque near stall, torque-speed curve, stator count, gene counts. Bounded — absolute pmf (assumed at 150 mV). Held open — whether canon intends Stage 23's "motor proteins" to include prokaryotic motors it does not name.
5. Test designed: fetch the speed-versus-pmf measurement, the stall-torque measurement, the torque-speed curve, and the stator-resurrection count; check whether any of them involves ATP.
6. Data (unfiltered): speed is proportional to pmf across 0–270 Hz; the stator units MotA/MotB are ion translocators; torque near stall ≈4,500 pN nm; torque is flat to a ≈200 Hz knee then falls to zero near 350 Hz; low-speed torque is temperature-insensitive and high-speed torque is not; at least 11 stator units contribute, and they are not equivalent; ≈40 gene products are needed to build the motor and ≈20 remain in it. ATP appears nowhere in the motor's energetics.
7. Variable Principle applied: **Measured** — proportionality of speed to pmf, torque magnitudes, stator count, non-equivalence of stators. **Structurally derived** — per-element force (25 pN), pmf components. **Held open** — canon's intended scope for "motor proteins". The DPR mapping: the motor has no DETECT and no PROCESS. Its input is a scalar thermodynamic quantity (pmf) and its output is torque; its only informational input, CheY~P, acts on the switch, not on the torque generators (see SWEEP-004). Naming the motor a RESPOND organ is defensible; naming any part of it DETECT or PROCESS requires relabeling a thermodynamic driving force as a "signal". Reality does not supply a boundary inside the motor where processing occurs.
8. Model update (Capsule: what the failed parts contribute): Stage 23's "universal currency" is false as stated for mechanical work. Proposed adjustment: Stage 23 becomes "Cellular work from ATP hydrolysis *or* directly from an ion-motive force"; and the flagellar motor belongs beside Stage 22, not after Stage 23, because it taps the same gradient ATP synthase taps rather than the ATP that synthase makes. The failed part contributes the more general statement: the gradient — not ATP — is the primary currency, and ATP is one of at least two things cells spend it on. That strengthens canon's own Stage 13 (chemiosmosis at alkaline vents) and Layer I.E (energy continuation), which both put the gradient first.
9. Documented: this file.
10. Next baseline: Stage 23's universality claim is ruled out for mechanical work; the proposed relabel and re-placement are recorded. Open at a lower level: whether canon's Stage 24 (which names only the eukaryotic Na+/K+ ATPase) can hold prokaryotic membrane energetics at all — carried to SWEEP-008.

## Forcing Test
- Test A (Ground): grounded. Two independent groups (Harvard, Oxford) measured pmf-driven operation by different techniques (azide de-energization with two-motor referencing; back-focal-plane interferometry during stator resurrection).
- Test B (Uniqueness): unique on the point that matters. Given speed proportional to pmf across the full range and ion-translocating stators, no ATP-powered account of motor torque survives.
- Test C (Direction): canon runs gradient → ATP → work. Measurement runs gradient → work directly, in parallel with gradient → ATP. Canon's arrow is not wrong, it is incomplete: it omits the branch.
- Test D (Falsifiability): the condition at step 3 was stated and is met. Stage 23's universality claim is falsified as stated.
- **Outcome:** `forced-no` for "ATP is the universal currency of cellular mechanical work". `conflict`, diagnosis `reached-conflicting`, intake `adjusted` — the contradicting observation is `measured-reproduced` across two independent groups, which is what substrate item 8 requires before the methodology re-forms. The adjustment: Stage 23 is relabeled and the flagellar motor is placed with Stage 22's chemiosmotic branch. DPR mapping inside the motor: **no** — the motor is a single-operation device.

## Anti-Operation (the gap this opens)

- If a machine can be a pure RESPOND with no DETECT or PROCESS of its own, then "every system runs the full base code" is false at this scale, and the claim has to be restated as "every *control loop* runs it". Which canonical items are loops and which are organs of a loop is now undefined.
- Stators are not equivalent: the 11th unit adds less speed than the 2nd. Canon's Layer III (Process Density) and Layer V (departments × pillars) both assume additive contribution from parallel units. A measured sub-additivity has no canonical home.
- Canon gives ≈32 ATP per glucose (Stage 22) but no figure for protons per revolution or work per proton. The audit cannot check the motor's efficiency against canon because canon states no energy budget for work, only for synthesis.

## Narrative stripped (if any)

- "Universal currency" (Stage 23): a claim of universality that measurement narrows to a claim of prevalence. Stripped.
- "Polarity deliberately created and maintained" (Stage 24): "deliberately" imports intent into a pump. Not forced.
- "Dynamic middle of all energy metabolism" (Stage 22): ATP synthase is one consumer of the gradient among several. Calling it *the* middle is a presentation choice.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; audit commentary is not endorsed by the author.
```
