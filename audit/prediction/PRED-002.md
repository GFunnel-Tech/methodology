---
id: PRED-002
target: "Energy source of the archaeal swimming motor (archaellum): ATP hydrolysis, or a transmembrane ion gradient"
organism: "Archaea (e.g. Halobacterium, Methanocaldococcus, Sulfolobus) — any archaeon whose archaellum has been characterised"
framework_route: "v5.1 Appendix A Stage 23 ('ATP Hydrolysis / Cellular Work … motor proteins, ion pumps … Universal currency') against the audit's proposed correction (SWEEP-003, finding F-d: gradient-driven mechanical work)"
prediction_kind: structural
tolerance: "Canon-as-written HITS if the archaellum is driven by ATP hydrolysis. The audit's correction HITS if it is driven by an ion-motive force. If both contribute, or the answer is unresolved in the literature, the verdict is 'partial' and neither position is credited."
contamination_risk: high
discriminating: yes
lookup_status: revealed
phase_a_commit: 753827e461cea846cd8a5a40f7285e408a128226
verdict: hit
---

## Target

Archaea swim with a motor (the archaellum) that is evolutionarily unrelated to the bacterial flagellum — it descends from the type IV pilus machinery, not from a rotary ion turbine. It is therefore an independent instance of the same problem: convert stored energy into rotation. The target is which energy source it uses.

This is a **fork between canon as written and the audit's proposed correction to it**, so it tests the audit as much as the framework.

## Framework route (the algorithm, run literally)

1. v5.1 Appendix A Stage 23 states: *"ATP Hydrolysis / Cellular Work — Energy captured by molecular machines: motor proteins, ion pumps, ribosomes, polymerases. **Universal currency.**"* Read literally, "universal currency" admits no exception: a motor protein is powered by ATP.
2. Layer II (Correspondence) says the same structure recurs at every scale where it applies. Canon therefore predicts the archaellum, being a molecular motor, runs on ATP.
3. The audit's sweep of the bacterial flagellar motor (SWEEP-003) found Stage 23 **forced-no** for that motor: it is driven directly by the proton-motive force, and its speed tracks that force. Finding F-d proposed relabelling Stage 23 to *"…from ATP Hydrolysis **or** Directly from an Ion-Motive Force"*, on the grounds that canon's own Stage 13 and Layer I.E already make the gradient primary.
4. These two readings make opposite predictions for an independent motor. Canon-as-written: ATP. The audit's correction, if it is a general principle rather than a patch for one case: ion-motive force.

## Derivation trace

The audit corrected Stage 23 from a single measured counterexample. A correction derived from one case may be a general truth (mechanical work in cells is gradient-driven) or an over-generalisation from the one motor that happens to be a turbine. An evolutionarily independent motor is the cleanest available test of which. If the archaellum runs on ATP, canon's "universal currency" survives the flagellar exception as a general rule with one exception, and the audit's proposed relabel is the weaker claim. If it runs on a gradient, the audit's correction is the general case.

## Prediction

**Canon as written predicts: ATP hydrolysis.** The audit's correction predicts: an ion-motive force. This file seals both, and records which one the measurement selects. The executor's own expectation is stated in the contamination disclosure below rather than hidden.

## Tolerance (what counts as a hit / a miss)

As in the front matter. Additionally: if the literature shows the motor's rotation is ATP-driven while the *switching* or a secondary function is gradient-dependent, that counts as ATP for the rotation and is noted, not scored as partial. "Unresolved" requires the absence of a primary characterisation, not merely a minority dissenting paper.

## Framework-free default

Without any framework, a molecular machine could plausibly use either; both are common in cells. A coin flip. The framework's contribution is that Stage 23 as written forbids one of the two outcomes, which is what makes it falsifiable here.

## Contamination disclosure

Graded **high**, and this is the weakest of the three predictions for that reason. The executor has a prior impression that the archaellum is ATP-driven via an associated ATPase, inherited from the type IV pilus machinery. No source has been consulted and no value retrieved, but a HIT for canon here should be discounted heavily: it may be recall rather than derivation.

It is sealed anyway because the *informative* outcome does not depend on the executor's cleanliness. If canon's ATP reading wins, the audit learns that its own correction (F-d) was over-generalised from one case — a finding against the audit, which no amount of executor contamination manufactures.

<!-- PHASE B BELOW THIS LINE — must be empty when Phase A is committed -->
## Measured

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Archaellar motor torque, *Halobacterium salinarum*, under varied viscous load | 160 pN·nm, constant and independent of rotation speed | as stated | measured-single | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1038/s42003-019-0422-6%22 (Commun Biol 2019, PMID 31149643) | 2026-09-28 |
| Energy source of archaellar rotation | ATP hydrolysis by the hexameric ATPase motor protein FlaI | — | measured-reproduced | as above, plus the review https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1007/s12551-019-00564-9%22 (PMID 31321734): *"there exists another ATP-driven protein motor in life: the rotary machinery that rotates archaeal flagella (archaella)"* | 2026-09-28 |
| Work per rotation vs ATP available in the hexamer | about **twice** the energy expected from hydrolysing six ATP, so more than six ATP are needed per rotation | as stated | measured-single | PMID 31149643 | 2026-09-28 |

## Verdict

**HIT for canon as written. The audit's own correction (F-d) is the thing that fails.**

The archaellum is ATP-driven. Appendix A Stage 23's *"motor proteins … Universal currency"* is correct for this evolutionarily independent motor, and the sweep's proposed relabel — treating gradient-driven mechanical work as the general case — was over-generalised from the single motor that happens to be an ion turbine.

The correct statement is the disjunction, not either branch alone: cells drive rotary mechanical work **either** from ATP (archaellum, F₁ portion of ATP synthase) **or** directly from an ion-motive force (bacterial flagellum). Two independent solutions to one problem, in two domains of life.

## What this does and does not show

**Shows:** the audit can be wrong, and this run caught it. Finding F-d is revised here, before it ever reached the v5.5 draft: Stage 23's ATP claim needs widening to a disjunction, not replacement by a gradient claim. Recorded against the audit, not against canon.

**Does not show** that the framework predicted anything. Contamination was graded **high** in Phase A for exactly this outcome: the executor suspected the archaellum was ATP-driven before sealing, and says so in the sealed text. Canon's "hit" here is a correct statement canon already contained, not a derivation — and the same Stage 23 sentence remains **forced-no** as an exclusive claim, because the bacterial flagellum still contradicts "universal".

Unresolved and left open: the measured work per rotation exceeds what six ATP supply, so the stoichiometry of this motor is not settled. Canon says nothing about it either way.
