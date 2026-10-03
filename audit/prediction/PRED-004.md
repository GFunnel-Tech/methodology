---
id: PRED-004
target: "Whether correlated failure across nominally independent checking stages is reported as the dominant limit on achieved reliability in layered/defence-in-depth systems"
organism: "n/a — engineered high-reliability systems"
framework_route: "design/DESIGN-ALGORITHM.md (derivation from the Master Meta-Algorithm), steps 5, 6 and 8, as run in design/RUN-001-self-healing-pipeline.md"
prediction_kind: structural
tolerance: "HIT if reliability-engineering sources identify correlated / common-cause failure across redundant or layered stages as a dominant (not incidental) limit on achieved reliability, such that the product-of-independent-stages calculation overstates real performance. MISS if the literature treats stage independence as generally safe to assume, or identifies some other factor as dominant while treating correlation as minor. PARTIAL if sources disagree or the question is not addressed in those terms."
contamination_risk: medium
discriminating: yes
lookup_status: revealed
phase_a_commit: 323f73dcb1e98907e2b7f94cbfbd258a0b56214d
verdict: hit
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

Source: **NASA, *Probabilistic Risk Assessment Procedures Guide for NASA Managers and Practitioners*, Second Edition** (Stamatelatos et al., December 2011), https://ntrs.nasa.gov/api/citations/20120001369/downloads/20120001369.pdf — retrieved 2026-09-28. Text extracted from the PDF locally; quotes verbatim.

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Whether the independence calculation is optimistic | *"Therefore, if A and B represent failure of a function, the actual probability of failure of both will be **higher** than the expected probability calculated based on the assumption of independence."* | as stated | derived | as above | 2026-09-28 |
| Standing of correlated failure in the method | A dedicated chapter and a mandatory screening stage: *"Preliminary Identification of Common Cause Failure Vulnerabilities (Screening Analysis)"*, whose objective is *"to identify potential common cause vulnerabilities and to determine those that are insignificant contributors to system unavailability and to the overall risk"* | as stated | derived | as above | 2026-09-28 |
| Why independence gets assumed anyway | *"Assumption C makes the models mathematically tractable — by assuming independence of the failures, the joint pdf … can often be solved analytically"* | as stated | derived | as above | 2026-09-28 |
| Worked instance in the guide's own example | a fault tree in which *"Leak not detected will result from Controller fails **OR** Pressure Transducers fail due to Common Cause OR** Pressure Transducer 1 fails AND Pressure Transducer 2 fails"* — the correlated term sits beside, and defeats, the redundant AND-term | as stated | derived | as above | 2026-09-28 |

## Verdict

**HIT.** Both halves of the Phase A tolerance are satisfied:

1. **The product calculation is optimistic** — stated in almost exactly the design's terms.
2. **Correlation is a first-order concern, not an incidental one** — it has its own chapter, its own mandatory screening stage before detailed analysis, and it appears as a distinct OR-branch in the guide's worked fault tree, positioned exactly where it defeats redundancy.

The third row is the sharpest part and was not anticipated in Phase A: the guide states plainly that independence is assumed **because it makes the mathematics tractable**, not because it is true. That is the precise failure mode step 8 of the design algorithm exists to prevent — a variable filled for convenience rather than measured.

## What this does and does not show

**Shows** that the design algorithm's step ordering works as claimed. Step 5 produced the multiplicative architecture; step 8 refused to let its key assumption stay implicit; step 9 named the independence failure as the most likely cause if the falsifier fires. A 300-page agency methodology reaches the same place, and reaches it by dedicating a chapter to it. The scaffold surfaced the dominant risk **before** any engineering source was consulted, early and cheaply — which is the only claim [`../../design/RUN-001-self-healing-pipeline.md`](../../design/RUN-001-self-healing-pipeline.md) makes for itself.

**Does not show** that the framework knew anything new. Contamination was graded **medium** in the sealed text and should be discounted accordingly: common-cause failure is a known concept and the executor said so before looking. What was genuinely uncertain — and is now settled — is whether the literature treats it as first-order. It does.

**Does not show** that canon-as-written would have produced this. Step 8 is the Variable Principle, which is canon's strongest element and carried unchanged. But step 5, which generated the architecture whose assumption step 8 then caught, required the audit's correction to Layer I.G ([CLAIM-021](CLAIM-021.md)): canon as written would have told the designer to retain every reject. **The scaffold that worked is canon plus the audit.**

**Credit where it is due:** this is the first prediction in the audit to score a hit that was *not* a restatement of something canon already contained. It is a hit for the framework's **process** — run the steps in order and the omission surfaces — rather than for its content. That is a narrower claim than the framework makes for itself, and it is real.
