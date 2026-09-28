---
id: PRED-004
target: "Whether correlated failure across nominally independent checking stages is reported as the dominant limit on achieved reliability in layered/defence-in-depth systems"
organism: "n/a — engineered high-reliability systems"
framework_route: "design/DESIGN-ALGORITHM.md (derivation from the Master Meta-Algorithm), steps 5, 6 and 8, as run in design/RUN-001-self-healing-pipeline.md"
prediction_kind: structural
tolerance: "HIT if reliability-engineering sources identify correlated / common-cause failure across redundant or layered stages as a dominant (not incidental) limit on achieved reliability, such that the product-of-independent-stages calculation overstates real performance. MISS if the literature treats stage independence as generally safe to assume, or identifies some other factor as dominant while treating correlation as minor. PARTIAL if sources disagree or the question is not addressed in those terms."
contamination_risk: medium
discriminating: yes
lookup_status: withheld
phase_a_commit: null
verdict: null
---

## Target

The design produced in [`../../design/RUN-001-self-healing-pipeline.md`](../../design/RUN-001-self-healing-pipeline.md) rests on one architectural claim (step 5): accuracy is bought by **several independent cheap checks in series**, because the failure rates multiply. Step 8 then named the assumption that claim depends on — **independence** — and flagged it as the design's single largest risk, before any engineering source was consulted.

The target is whether real reliability engineering agrees that this is where such designs actually fail.

## Framework route (the algorithm, run literally)

1. Step 5 of the Mechanism Design Algorithm forces the designer to decide what is discarded and what is kept, and produced: serial independent checks, each rejecting, with multiplicative accuracy.
2. Step 6 forces a signed direction for the operating point, and produced: *add a stage rather than tighten one* — because adding is multiplicative while tightening is marginal.
3. Step 8 forbids filling a needed variable with a plausible value, and so forced the independence assumption into the open as a **held-open variable** rather than leaving it implicit in the arithmetic.
4. Step 9 then required an operational falsifier, and named the most likely cause if it fires: **the independence assumption in step 8.**
5. Therefore the design predicts, about the class of systems built this way: where such designs underperform their calculated reliability, the cause is that the stages were not independent.

## Derivation trace

The prediction is not about biology and not about any one system. It follows from steps 5, 6 and 8 in combination: the moment accuracy is claimed as a *product* of stage pass-rates, the whole claim's weight rests on the stages being uncorrelated, and step 8's rule turns that from a hidden assumption into the named risk. If the algorithm is worth anything as a design instrument, the risk it surfaces first should be the risk practitioners actually fight.

Note what this tests: not whether the framework knows a number, but whether **running the steps in order surfaces the right dominant risk early**. That is precisely the claim made for the algorithm — that it is a scaffold which catches omissions — so it is the right thing to seal.

## Prediction

Reliability-engineering practice identifies **correlated / common-cause failure across nominally independent layers** as a dominant limit on achieved reliability, and treats the naive product-of-independent-stages calculation as optimistic.

## Tolerance (what counts as a hit / a miss)

As in the front matter. Additionally: a HIT requires the correlation problem to be treated as a *first-order* concern (named, modelled, or designed against), not merely mentioned. A source that only says "assume independence carefully" is PARTIAL.

## Framework-free default

A designer with no framework who wrote down "three checks at 1% each gives one in a million" would, in the ordinary case, **believe the arithmetic** — that is why the mistake is common enough to have a name. The framework-free default here is therefore the *optimistic* reading, which is what makes this discriminating: the algorithm's step 8 pushed against the default rather than restating it.

## Contamination disclosure

Graded **medium**. The executor is a language model and has general familiarity with reliability engineering, including the existence of common-cause failure as a known concern; that familiarity is why the risk was easy to name at step 8. What the executor has *not* done is consult any source in this run, and what remains genuinely uncertain is whether the literature treats correlation as **dominant** or as one hazard among many — which is the part the tolerance turns on.

The honest reading if this hits: it is weak evidence about the framework's originality and better evidence about the *ordering* of the algorithm's steps — the risk surfaced at step 8, early and cheaply, rather than after the design was built. That is a claim about process, not about knowledge, and it is the claim the design run actually makes.

<!-- PHASE B BELOW THIS LINE — must be empty when Phase A is committed -->
## Measured

## Verdict

## What this does and does not show
