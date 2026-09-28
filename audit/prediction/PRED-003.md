---
id: PRED-003
target: "Whether any free-living organism conserves energy without maintaining a transmembrane ion gradient (i.e. whether chemiosmotic coupling has a known exception)"
organism: "n/a — a survey claim across free-living prokaryotes"
framework_route: "v5.1 Layer I.E, Resolution Four and 'The Practical Implication' ('Per Correspondence: same answer at every scale. Zero exceptions.'); with Appendix A Stage 13 (chemiosmosis as the mechanism) and Layer II (Correspondence)"
prediction_kind: structural
tolerance: "HIT if no free-living organism is known to conserve energy without maintaining a transmembrane ion gradient — i.e. chemiosmotic coupling is reported as universal among free-living cells. MISS if at least one free-living organism is characterised as lacking it (e.g. conserving energy by substrate-level phosphorylation alone, with no maintained ion gradient). Obligate intracellular parasites, organelles and viruses are outside the claim and do not count either way; canon's claim is about systems that must establish their own gradients."
contamination_risk: low
discriminating: yes
lookup_status: revealed
phase_a_commit: 753827e461cea846cd8a5a40f7285e408a128226
verdict: partial
---

## Target

Canon makes an explicitly exceptionless claim about how energy continuation works. The target is whether that claim has a known counterexample among free-living organisms: is there a cell that lives without maintaining an ion gradient across its membrane?

## Framework route (the algorithm, run literally)

1. v5.1 Layer I.E, *The Practical Implication*, states: *"Stop chasing energy creation and start engineering gradient establishment and collapse. Every healthy cell, business, relationship, and civilization is doing this continuously. The mitochondrion does not ask where ATP comes from. It establishes a proton gradient, channels its collapse productively, and trusts the next gradient will be ready when the substrate arrives. This is the operational form of the answer. **Per Correspondence: same answer at every scale. Zero exceptions.**"*
2. Appendix A Stage 13 makes the gradient the founding mechanism: *"Natural proton gradients across mineral membranes. Energy harvested from polarity. The mechanism the ETC will refine."*
3. Layer ◇ gives the matching falsifier for the layer: *"Discovery of a self-sustaining process operating without polarity establishment and collapse."*
4. Run literally, canon predicts: **no free-living cell conserves energy without establishing and collapsing a transmembrane gradient.** The falsifier is a single characterised exception.

## Derivation trace

This is canon's own falsifier, applied to the domain where it is most nearly checkable. Layer I.E does not merely describe gradients as common; it stakes "zero exceptions" on them and names what would disprove it. The claim is therefore testable in exactly the way canon asks: look for a cell that lives without one. Unlike PRED-001 and PRED-002, nothing here is derived by analogy — the prediction is canon's stated content.

Note what the prediction is *not*: it is not that every cell makes ATP chemiosmotically (fermenting cells make ATP by substrate-level phosphorylation, which canon's wording does not forbid). It is that no free-living cell dispenses with the maintained gradient altogether. A fermenter that still maintains a gradient for transport and motility is consistent with canon.

## Prediction

**No exception exists.** Every characterised free-living organism maintains a transmembrane ion gradient, and canon's "zero exceptions" holds for this claim.

## Tolerance (what counts as a hit / a miss)

As in the front matter. One clearly characterised free-living exception is a MISS: canon staked "zero exceptions", so its own standard does not permit "rare" as a defence. A borderline case (an organism whose gradient maintenance is disputed in the literature) scores `partial`, and the dispute is recorded rather than resolved.

## Framework-free default

The framework-free default is *not* the same claim. Standard biology teaches chemiosmotic coupling as near-universal but does not, as a rule, assert exceptionlessness; a working biologist's prior would be "very widespread, probably with odd exceptions somewhere". So the framework's prediction is strictly stronger than the default, and the two come apart on exactly one question: does an exception exist? That is what makes this the most discriminating of the three predictions.

## Contamination disclosure

Graded **low**. The executor has general knowledge that chemiosmotic coupling is taught as near-universal, but no recollection of a specific catalogued exception or of a survey that settles the question either way — which is why this target was chosen. No source has been consulted.

The executor's honest expectation is that this is the prediction most likely to come back `partial`: biology's edge cases (obligate fermenters, minimal-genome organisms, extremophiles with unusual bioenergetics) are where an exception would hide, and the literature may not state a clean verdict. A `partial` here is itself a finding about canon: an exceptionless claim whose exception-status cannot be determined is not operational, which is what FINDINGS F-042/F-043 already say about other canonical falsifiers.

<!-- PHASE B BELOW THIS LINE — must be empty when Phase A is committed -->
## Measured

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| A catalogued free-living organism that conserves energy with **no** maintained transmembrane ion gradient | **none found** in this run's searches | — | held-open | Europe PMC searches over chemiosmotic universality, obligate fermenters, and minimal bioenergetics (queries recorded in the session log) | 2026-09-28 |
| A primary source asserting that chemiosmotic coupling is **universal** among free-living cells | **none found** | — | held-open | as above | 2026-09-28 |
| Nearest relevant statement found | *"The common ancestor of all cells used ATP synthase to convert proton gradients into ATP. However, pumps generating proton gradients and lipids maintaining proton gradients are **not universally conserved across all lineages**."* | as stated | measured-single | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1016/j.xcrp.2025.102461%22 (Cell Rep Phys Sci 2025, PMID 40123866) | 2026-09-28 |

## Verdict

**PARTIAL.** Neither branch of the Phase A tolerance was satisfied. No exception was found, so canon is not refuted; but no source asserting universality was found either, so canon is not confirmed. The one directly relevant statement retrieved says the *machinery* for making and holding proton gradients is not universally conserved across lineages — which bears on the claim without settling it, since an organism can maintain a gradient by other means.

This is the outcome Phase A predicted as most likely, and said so before the lookup.

## What this does and does not show

**Shows** what the audit has now found five times over (FINDINGS F-042, F-043, and the two exceptionless-law failures in the sweep): canon's "zero exceptions" claims are **not operational**. This one is stated in canon's strongest form, with a falsifier attached by Layer ◇, and a directed literature search still cannot determine whether the falsifier has fired. A claim whose exception-status cannot be established is doing no predictive work, whatever its truth.

**Does not show** that the claim is false. Chemiosmotic coupling may well be universal among free-living cells. The finding is about the claim's testability as canon words it, not about bioenergetics.

**What would settle it:** a systematic survey of characterised free-living prokaryotes for maintained ion gradients, or a bioenergetics review that states the universality claim explicitly and names the hard cases. Until one exists, this stays **held open** — and canon should not assert "zero exceptions" while it does.
