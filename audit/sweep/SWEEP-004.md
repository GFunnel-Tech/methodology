---
id: SWEEP-004
canon_ref: v5.1 Layer I.C Domain 9 Biological Process Algorithm, step 4; v5.1 Layer 0 (RESPOND)
canon_label: "Respond with corrective action. The organism that achieves stasis without correction is dead."
diff_state: methodology-gap
exclusion_diagnosis: not-reached
claim_outcome: stipulation
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says

v5.1 Domain 9 Biological Process Algorithm, step 4: "Respond with corrective action. The organism that achieves stasis without correction is dead."

v5.1 Layer 0: "RESPOND | Output is generated. The response becomes the next cycle's input. The loop closes and reopens simultaneously."

v5.1 Layer I.D (Yin/Yang & The Dynamic Middle) supplies canon's only account of a two-state system holding a centre: "the continuously recalibrating center between overextension and paralysis."

Canon names no switch, no binary output, and no rotational direction. Nothing in canon holds a device whose output is one of exactly two discrete states.

**Split.** *Factual core:* a control loop ends in a discrete corrective output. *Framework mapping:* Layer I.D's dynamic middle as the general form of a two-state balance; RESPOND as an operation distinct from PROCESS.

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Rotational symmetry of the C ring (containing FliM and FliN), cryo-EM reconstruction, Salmonella | varies from 32-fold to 36-fold | range across reconstructions; no correlation with M-ring symmetry | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=17015643&rettype=abstract&retmode=text (Thomas et al. 2006, J Bacteriol 188:7039) | 2026-09-28 |
| Rotational symmetry of the M ring, same reconstruction | varies from 24-fold to 26-fold | range as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=17015643&rettype=abstract&retmode=text | 2026-09-28 |
| Location of FliG relative to the two rings | C-terminal motor domain of FliG docked in the C ring, interacting with FliM; a further FliG domain contributes a thickening on the M-ring face with M-ring symmetry | hypothetical docking, from measured density features | derived | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=17015643&rettype=abstract&retmode=text | 2026-09-28 |
| Input-output relation between intracellular CheY~P and single-motor output, measured with fluorescence correlation spectroscopy | identical steep input-output relation across different bacteria; motors "actively contribute to signal amplification in chemotaxis" | qualitative in the retrievable abstract | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=10698740&rettype=abstract&retmode=text (Cluzel, Surette & Leibler 2000, Science 287:1652) | 2026-09-28 |
| Hill coefficient of motor switching versus CheY~P at fixed FliM content | not stated in the retrievable abstract; reported only as "about twice as large as those observed before" and as "the highest known for allosteric protein complexes, either biological or synthetic" | numeric value not obtained | held-open | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=23454041&rettype=abstract&retmode=text (Yuan & Berg 2013, J Mol Biol 425:1760) — PMC full text blocked by an access check this run, so the number was not fetched | 2026-09-28 |
| Mechanism of motor adaptation to steady-state CheY~P | the motor adjusts the number of FliM molecules to which CheY~P binds | as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=23454041&rettype=abstract&retmode=text | 2026-09-28 |
| Cooperativity of CheY~P binding to FliM compared with cooperativity of switching, in vivo FRET | binding much less cooperative than motor switching | as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=12232047&rettype=abstract&retmode=text (Sourjik & Berg 2002, PNAS 99:12669) | 2026-09-28 |
| Distribution of clockwise and counterclockwise intervals, tethered cells | exponential, fitted by first-order rate constants; threshold-crossing models are excluded because they predict far too many long events | as published | measured-single | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=6339475&rettype=abstract&retmode=text (Block, Segall & Berg 1983, J Bacteriol 154:312) | 2026-09-28 |

## Scientific Inquiry run
1. Question (precise): Does a canonical item hold the flagellar switch complex, and is the PROCESS-to-RESPOND boundary physically locatable in the measured switch or is it drawn by the reader?
2. What an answer must look like: the canonical item covering a discrete two-state output; and a measurement that locates the amplification and the state change at a specific molecular interface.
3. Falsifiability condition: the PROCESS/RESPOND boundary is real if the amplification step and the binding step are measurably separate. It is imposed if the switch is a smooth function of its input with no resolvable transition.
4. Variables: measurable / bounded / held open: measurable — ring symmetries, binding cooperativity versus switching cooperativity, interval distributions, FliM-number adaptation. Bounded — FliG docking (inferred from density). Held open — the Hill coefficient of switching at fixed FliM, which could not be fetched this run.
5. Test designed: fetch the rotor reconstruction, the single-cell input-output measurement, the in vivo binding-cooperativity measurement, and the interval statistics; check whether binding and switching are separable.
6. Data (unfiltered): the C ring has 32–36-fold symmetry and the M ring 24–26-fold, uncorrelated. FliG's motor domain sits in the C ring interacting with FliM. CheY~P binding to FliM is much less cooperative than switching, so the steep step is downstream of occupancy. The motor adapts by changing how many FliM molecules are available to bind. Switching intervals are exponential and are not generated by threshold crossing of a fluctuating regulator. The Hill coefficient of switching at fixed FliM is reported as the highest known for any allosteric complex but the number was not retrievable this run.
7. Variable Principle applied: **Measured** — ring symmetries, the binding/switching cooperativity gap, exponential intervals, FliM-number adaptation. **Structurally derived** — FliG placement. **Held open** — the Hill coefficient, held open rather than filled from memory. The DPR mapping: DETECT = nothing here; PROCESS = CheY~P occupancy of FliM sites; RESPOND = the concerted conformational change of the C ring that reverses the sense of rotation. The boundary between the last two is genuinely locatable: occupancy and switching have *different measured cooperativities*, which is exactly the signature of a distinct downstream step. This is the one place in the sweep where a measurement, not a narrative, puts a line between two of the three operations. It is also where canon has the least to say: no canonical item holds a binary actuator, and Layer I.D's "continuously recalibrating centre" is the wrong shape — the measured device does not sit in the middle, it flips between two extremes with exponentially distributed dwell times, and the *bias* (the time-average) is what is graded.
8. Model update (Capsule: what the failed parts contribute): Layer I.D's dynamic middle is contradicted in form and recovered in statistics. The switch never occupies a middle state; the middle exists only as a dwell-time ratio over many events. That is a substantive refinement available to canon: at molecular scale the dynamic middle is not a position, it is a duty cycle. The failed literal reading contributes the corrected one.
9. Documented: this file.
10. Next baseline: PROCESS/RESPOND boundary — supported by measurement. Canon coverage — absent. Held open and scheduled: the Hill coefficient number, needed before any claim about the size of the amplification at the switch.

## Forcing Test
- Test A (Ground): grounded for structure, binding cooperativity and interval statistics. Not grounded for the switching Hill coefficient, which is recorded `held-open`.
- Test B (Uniqueness): the location of the amplification (downstream of binding) is forced by the cooperativity gap. The reading of that location as a *boundary between operations* is not forced — it is equally describable as one PROCESS with a nonlinear output stage.
- Test C (Direction): canon derives the need for a RESPOND step from the algorithm. The measurement derives a discrete state change from the cooperativity gap. The two arrive at the same place from opposite directions, which is the strongest agreement in this sweep.
- Test D (Falsifiability): the condition at step 3 was met (binding and switching are measurably separate), so the boundary is not merely imposed. The Hill-coefficient gap prevents any quantitative claim.
- **Outcome:** `stipulation` for canon's claim, which does not reach this device; the DPR mapping at this interface is **supported by measurement** rather than applied after the fact. `methodology-gap`, diagnosis `not-reached`: canon has no item for a discrete two-state actuator.

## Anti-Operation (the gap this opens)

- If the dynamic middle at molecular scale is a duty cycle rather than a position, then Layer I.D and Layer V's BEAS "draw" need a stated scale at which each reading holds. None is given.
- Ring symmetries vary (32–36, 24–26) and are uncorrelated with each other. Canon's Appendix D collects fixed constants; it has no category for a machine whose stoichiometry is a distribution rather than a number.
- The Hill coefficient is held open. Until it is fetched, the claim "the motor amplifies" is directional only, and any correspondence argument built on the size of that amplification is unsupported.

## Narrative stripped (if any)

- "The organism that achieves stasis without correction is dead" (step 4): true as a slogan, but the measured switch is *always* switching, including in the absence of any stimulus, and that idling is not correction. Spontaneous switching is not forced by canon's framing and is not accounted for by it.
- Layer I.D's "continuously recalibrating center": stripped as a literal description at this scale; retained only as a statement about the time-average.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; audit commentary is not endorsed by the author.
```
