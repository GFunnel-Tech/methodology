# MDA Run 001 — A self-healing, error-correcting pipeline

*Run 2026-09-28 · Instrument: [`DESIGN-ALGORITHM.md`](DESIGN-ALGORITHM.md) (derivation) · Target chosen by the author*

**Target.** A pipeline that moves items through several transformation stages and must deliver output accuracy far higher than any single stage achieves, and must repair damage without someone standing over it. Deliberately medium-neutral: the same design serves a software data pipeline, a manufacturing line, or a document/lead workflow.

Each step below records **what the algorithm forced**, and — in italics — **an honest note on whether the framework did the work or the framework merely hosted it.** That second column is the point: a scaffold that takes credit for what any engineer would do is not a scaffold, it is decoration.

---

## 1 · The job as a state change

**From:** items arriving with unknown, individually low correctness; some malformed, some subtly wrong, a few corrupted mid-flight.
**To:** items delivered at a stated accuracy far above per-stage accuracy, with every rejected item accounted for and no silent loss.

*Forced by the algorithm:* the phrase **"and no silent loss"**. Step 1 demands the "to" state be observable, which rules out "mostly fine" as a target and requires a delivered-accuracy number plus an accounting rule. A design brief without that gets written all the time.

## 2 · The gradient, and how work is drawn from it

**Gradient:** the difference between an item's arriving form and its accepted form. Work is done as that difference collapses; when it is zero the pipeline has nothing to do.

**Coupling choice — (a) stored quantum, deliberately.** Correction capacity is held as a *buffered reserve* (queue depth, spare workers, a maintenance window) and spent on demand, rather than each stage correcting only at the instant an error arrives. Reason: error arrival is bursty and the reserve decouples supply from demand. **Named conversion loss:** buffered capacity decays — a queued item ages, a reserved worker idles, a held lock blocks. Budget the decay explicitly.

*Honest note:* **this is the weakest step of the run.** For a non-physical mechanism "the gradient" is a metaphor, and the algorithm cannot say what it is; I chose it. What step 2 *did* contribute is the forced (a)/(b) choice and the demand to name a conversion loss — and the conversion loss (capacity decays while reserved) is a real design item that a naive design omits. Credit the fork, not the metaphor.

## 3 · Level, or rate of change

**Rate, not level.** The pipeline monitors the *change* in error rate against its recent baseline, not the absolute count.

Consequence, and this is the substantive one: a constant background error rate is **adapted away** rather than alarmed on, and a *step change* triggers response even when the absolute rate is still low. A level-regulated design does the opposite — it is quiet while a slow degradation walks the baseline upward, then screams once a threshold trips, by which time the cause is weeks old.

*Forced by the algorithm:* yes, genuinely. Step 3 exists only because a measured biological mechanism refused to have a set-point (F-071), and it puts a choice in front of the designer that is normally made by default and never revisited. **Both** regulators are needed in practice — a rate monitor for drift and a level guard for absolute catastrophe — but the design now says so on purpose instead of shipping one and discovering the other in an incident review.

## 4 · The operation chain, with occupants named

| Slot | Occupant | Note |
| --- | --- | --- |
| **DETECT** | per-stage validator: a cheap invariant check at each boundary (schema, checksum, range, tolerance) | must be cheap enough to run on every item, or it will be sampled and then skipped |
| **PROCESS** | the classifier that decides *which* failure this is: transient, malformed, or corrupt | |
| **RESPOND** | the matched action: retry, repair, or quarantine — one per class |  |
| **TERMINATE** | bounded retry budget per item; on exhaustion, quarantine and escalate once; re-arm on a new deploy or a criterion change | |

**Two slots where the algorithm earned its place:**

- **PROCESS may be empty, and for the cheapest checks it should be.** For a checksum failure there is no classification worth doing: detect and respond are the same event — reject, re-request. Forcing a classifier in front of every check buys latency and a new failure mode for nothing. Reserve the informational step for the failures that genuinely have classes. *This came from step 4's rule (F-065), and it is the opposite of what a "proper" layered design would do.*
- **TERMINATE is the omission this step is for.** Unbounded retry is the classic self-healing failure: a pipeline that heals itself into a retry storm, converting a small fault into an outage. The budget, the single escalation, and the explicit re-arm condition all come from this slot existing. *A naive design has detect/process/respond and no stop.*

## 5 · What is discarded, and what is kept

**The design's core, and the step the audit had to correct canon to get.**

**Architecture: several independent checks in series, each cheap, each rejecting.** Output accuracy is the product of what each stage lets through, so three independent stages at 10⁻² each give 10⁻⁶ overall. Accuracy is *bought by discarding*, not by keeping.

**What is kept: the criterion. What is discarded: the item.**
- The validators, tolerances, and classifier rules are the accumulated learning — they are versioned, reviewed, and they only ever get sharper. Every past rejection is represented *in the rule*, not in a stored copy of the reject.
- Rejected items are **not** retained on the theory that nothing should be lost. That theory is what canon got wrong (CLAIM-021), and following it here produces the failure mode directly: an ever-growing dead-letter store that nobody reads, that ages into a liability, and that quietly becomes the largest thing in the system.

**Discard paths, each named with its cost:**

| Path | Cost | Where the item goes |
| --- | --- | --- |
| Transient failure → retry | latency; duplicate-work risk | back to the stage head, with an attempt counter |
| Malformed → repair | CPU/handling; risk of a wrong repair | forward, **flagged as repaired**, never silently |
| Corrupt or budget-exhausted → quarantine | storage; review attention | quarantine with a **bounded lifetime and a named owner** |
| Rejected at final gate → drop | the item itself | counted, sampled into the criterion review, then deleted |

**Quarantine has a lifetime and an owner.** Without both it is a leak dressed as diligence.

**The feedback loop that makes it self-healing rather than merely self-protecting:** a sample of rejects is reviewed on a schedule, and the review updates the *criterion*. That is the only channel by which failures improve the system. Nothing else about a reject is retained.

*Forced by the algorithm:* yes, and this is the run's strongest result. Serial multiplicative checking is standard engineering, so the architecture itself is `works-descriptive`. But **"keep the criterion, discard the item"** and the consequent rejection of an unbounded dead-letter store came from the corrected step 5, and it contradicts what canon-as-written would have told a designer to do. The audit's correction is doing real design work here.

## 6 · The operating point

- **Too much checking:** throughput collapses, latency exceeds the item's useful life, and reviewers stop reading rejects — at which point the checks are theatre.
- **Too little:** errors reach the consumer and the criterion never sharpens, because nothing is caught to learn from.
- **Measured quantity:** rejects per thousand items at each stage, against delivered defect rate and end-to-end latency.
- **Which constraint moves the optimum, and which way:** *cheapen a check and the optimum moves toward more checking* (add a stage rather than tighten one — adding is multiplicative, tightening is marginal). *Raise the cost of a missed error and the optimum also moves toward more checking.* *Shorten the item's useful life and it moves toward less.*

*Forced by the algorithm:* the **direction** statements. Step 6 refuses "balance" and demands a quantity and a signed direction, per F-078 — and "add a stage rather than tighten one" is a real, arguable design rule that falls out of naming the direction.

## 7 · Observation levels

| Level | What records that it ran |
| --- | --- |
| Physical trace | per-item audit log: which stage passed, which rejected, which repaired |
| Operator memory | the scheduled reject review — the only level that updates the criterion |
| Institutional record | versioned criteria with their change rationale; incident write-ups |
| Downstream consumer | delivered-accuracy report the consumer can check independently |

**The missing level is where it dies quietly.** With a log but no review, the criterion never sharpens. With a review but no versioned criteria, the learning leaves with the reviewer.

**Readiness is budgeted, not apologised for.** The pipeline holds spare correction capacity it is not using. That is neither maximum throughput nor equilibrium, and it is correct: it is what absorbs a burst. *This slot exists because a real organism was measured holding >20% of its proteome idle (F-079) — canon as written had no room for it.*

## 8 · Held open (not filled)

| Variable | Status |
| --- | --- |
| Per-stage error rates in *this* medium | **held open** — must be measured; the 10⁻² figure above is illustrative arithmetic, not a claim |
| Independence of the checks | **held open, and the design's main risk.** Multiplicative accuracy assumes independent stages. Shared libraries, shared assumptions, or one author writing all three break it, and the product rule then overstates real accuracy, possibly by orders of magnitude |
| Correct retry budget | held open — depends on measured transient-vs-permanent mix |
| Quarantine lifetime | held open — depends on review capacity and retention obligations |
| Reject sampling rate | held open |

*Forced by the algorithm:* the independence entry. Step 8's rule against filling a variable to look finished is what keeps the design's headline arithmetic honest, and it identifies where this design most plausibly fails in practice.

## 9 · Falsifier (operational)

**The design is wrong if:** measured delivered defect rate fails to fall as the product of measured per-stage pass rates, by more than a stated factor, across at least three independent fault injections.

**Instrument:** deliberate fault injection at known rates; compare predicted against measured end-to-end defect rate.
**Most likely cause if it fires:** the independence assumption in step 8.

*Forced by the algorithm:* yes. Step 9's demand for a threshold and an instrument (per F-042/F-043) converts "we'll monitor quality" into a test that can actually fail — and it names in advance which held-open variable the failure would implicate.

## 10 · The conjugate gap this design opens

**The criterion becomes the single point of failure.** Once learning is concentrated in the validators rather than in retained items, a wrong criterion is systematic: it rejects good items at scale, or admits a whole class of bad ones, and no stored copy of the rejects exists to reconstruct what was lost. Mitigations follow directly — version the criterion, stage its changes, and keep a small randomly sampled hold-back set that bypasses the criterion, precisely so the criterion can be audited against something it did not filter.

*Forced by the algorithm:* yes, and it is the most useful thing on this page. Step 10 turned step 5's strength into its exposure, and produced the hold-back set — a design element that does not appear anywhere else in this run.

## 11 · Four Pillars review

| Pillar | Verdict |
| --- | --- |
| **Correctness** | Right at the unit: each check is a per-item invariant, not an aggregate statistic. Aggregate-only checking would pass a batch whose individual items are all subtly wrong. |
| **Complexity** | Every stage must justify itself by measured rejects. A stage that rejects nothing over a full cycle is removed, not kept for reassurance. |
| **Patience** | What breaks if rushed: the criterion. Shipping validators before measuring the real error mix produces checks tuned to imagined failures and blind to actual ones. |
| **Resilience** | Edge condition is the burst, not the average. Behaviour when the quarantine fills, the retry budget exhausts across many items at once, and the reviewer is absent must be specified — that is where self-healing designs fail. |

## 12 · Build order, and documentation

1. **Direct** — state the delivered-accuracy target and the accounting rule (step 1).
2. **Guide** — instrument first: measure the real error mix before writing a single validator.
3. **Gather** — collect the measured rates; fill step 8's held-open variables with data.
4. **Organize** — design the stages and the discard paths on paper, including quarantine ownership.
5. **Create** — build the cheapest, highest-yield check first; add stages, do not tighten one.
6. **Database** — version the criteria with rationale; wire the audit log and the hold-back set.
7. **Repetition** — run the reject review on a schedule; each cycle sharpens the criterion.

**Restart at higher baseline:** the next cycle loads the measured rates and criterion versions from this one.

---

## Verdict on the instrument

| | |
| --- | --- |
| **Design produced** | A coherent, buildable specification with named occupants, named discard paths and costs, an operational falsifier, five honestly held-open variables, and a named conjugate gap with its mitigation. |
| **What the framework genuinely forced** | TERMINATE as a first-class operation (step 4) · permission to leave PROCESS empty (step 4) · *keep the criterion, discard the item*, and the rejection of an unbounded dead-letter store (step 5, **only after the audit corrected canon**) · rate-vs-level as a deliberate choice (step 3) · signed directions for the operating point, giving "add a stage rather than tighten one" (step 6) · readiness capacity as legitimate (step 7) · the independence risk named rather than assumed (step 8) · an operational falsifier (step 9) · the hold-back set (step 10). |
| **What it did not supply** | Every number. The medium. The mechanism of each check. The whole quantitative content is held open or illustrative. |
| **Where it strained** | Step 2. "The gradient" has no non-metaphorical referent for an information pipeline; the useful part was the forced (a)/(b) fork and the demand to name a conversion loss, not the gradient language. |
| **Honest overall grade** | **`works-descriptive` with three `works-forced` elements.** Serial multiplicative checking is standard engineering and the algorithm cannot claim it. The forced elements are TERMINATE, *keep-the-criterion-discard-the-item*, and the hold-back set — three real design decisions a competent engineer can miss, produced in order, early, and cheaply. |
| **The honest caveat** | Two of those three came from **corrections the audit made to canon**, not from canon as written. Canon as written would have told this designer to retain every reject — the exact failure mode step 5 now forbids. The scaffold that works is canon **plus the audit**, and that is a real result: the audit is not only subtracting from the framework, it is making it usable. |

**Sealed prediction from this run:** [`../audit/prediction/PRED-004.md`](../audit/prediction/PRED-004.md) — step 5's architecture claim, stated before any engineering source was consulted.
