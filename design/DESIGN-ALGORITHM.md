# The Mechanism Design Algorithm (MDA)

> **Status: derivation, not canon** (AGENTS.md rule 4). Canon has no design algorithm: every one of its 70+ algorithms either *diagnoses* an existing system or *runs* a process. This one is derived from the **Master Meta-Algorithm** and labelled a derivation. It enters a version only if the author declares it.

## What it is for

Canon's instruments answer *"what is this system doing, and where is it broken?"* This one answers *"I must build a mechanism that does X — what must I decide, in what order, and what must I not assume?"*

## What it can and cannot supply

Established by the Reality Audit's full run against a real system ([`../audit/FINDINGS.md`](../audit/FINDINGS.md), [`../audit/sweep/`](../audit/sweep/), [`../audit/prediction/`](../audit/prediction/)):

**It can** force the decisions a design must make, in an order that surfaces omissions, and name what is still unknown. That is a scaffold, and a scaffold is worth having.

**It cannot** supply a value, choose a mechanism, or predict a measurement. The audit found **zero** confirmed cases of canon stating a quantity before it was measured. Any number in a design produced by this algorithm comes from measurement or engineering judgement, never from the algorithm. **Where the algorithm cannot supply something, it must say so rather than guess** — that is the Variable Principle applied to design.

## Provenance of each step

Every step names the canonical source it derives from, and — where the audit found canon wrong — the correction it carries. A step marked **corrected** would give a worse design if canon were followed as written.

| Step | Derived from | Correction carried |
| --- | --- | --- |
| 1 | Master Meta 3–4 (current / desired state) | — |
| 2 | Layer I.E; Appendix A Stage 13 | **corrected:** work comes from a stored quantum **or** directly from a gradient — a disjunction, per [PRED-002](../audit/prediction/PRED-002.md) |
| 3 | Layer I.C Domain 9 step 1 | **corrected:** the regulated quantity may be a level **or** a rate of change, per F-071 |
| 4 | Layer 0 (`DETECT → PROCESS → RESPOND`) | **corrected:** a fourth operation, **TERMINATE**, per F-066; and PROCESS may have no occupant, per F-065 |
| 5 | Layer I.G, Axiom 14 | **corrected:** conserve the **discriminating structure**, not the discarded item, per [CLAIM-021](../audit/claims/CLAIM-021.md) |
| 6 | Layer I.D (dynamic middle) | **corrected:** state the quantity and the direction, or the claim is unfalsifiable, per F-078 |
| 7 | Layer I.F (six observation levels) | **corrected:** readiness/idle capacity is a legitimate third configuration, per F-079 |
| 8 | The Variable Principle | — (canon's strongest element; carried unchanged) |
| 9 | Layer ◇ | **corrected:** the falsifier must be operational — name the observation and the threshold, per F-042/F-043 |
| 10 | Layer ⊙, the Anti-Operation | carried as **live hypothesis**, per GOV-005 |
| 11 | Layer I.B (Four Pillars) | — |
| 12 | Layer VI (Shepherd's Way); Master Meta 11–12 | — |

---

## The algorithm

Run the steps **in order**. Do not skip. If a step cannot be completed, **stop and record the blocker** — the blocker is the design's real location of risk, and proceeding past it is how the failure gets built in.

**1 · Name the job as a state change.** From what state, to what state, in what medium. If you cannot state the "from" and the "to" as observable conditions, you do not yet have a mechanism to design.

**2 · Name the gradient, and choose how work is drawn from it.** Every functional mechanism runs on a difference that is established and collapsed. Name it. Then choose the coupling, explicitly:
   - **(a)** from a **stored quantum** (a charged carrier spent on demand), or
   - **(b)** **directly from the gradient** (the difference does the work as it collapses).
   (b) is usually simpler and has fewer failure modes; (a) decouples supply from demand and buys timing freedom. Name the conversion loss if you convert between them — there always is one.

**3 · Decide what is regulated: a level, or a rate of change.** A level-regulated mechanism holds a set-point and corrects deviation. A rate-regulated mechanism compares recent history against earlier history and responds to the difference; it has **no set-point** and adapts away constant conditions automatically. Most designers default to level control without noticing the choice exists. State which, and why.

**4 · Lay out the operation chain, and name the physical occupant of each slot.**
   `DETECT → PROCESS → RESPOND → TERMINATE`
   - For each slot, name the thing that does it. A slot with no named occupant is an unfinished design, not a clever abstraction.
   - **If PROCESS has no occupant, that may be correct.** A device where sensing and responding are the same physical event — a pressure valve, a shear pin, a thermal cutout — is simpler and more reliable than sensor-plus-controller-plus-actuator. Ask whether the job genuinely needs an informational step.
   - **TERMINATE is not optional.** A response with no stopping mechanism is the most common serious omission in control design. Name what ends it, and what re-arms it.

**5 · Decide what is discarded, and what is kept.** This is the step canon gets wrong and the one that does the most work in a self-correcting design.
   - Accuracy is *bought* by discarding. You do not get a high-fidelity output by keeping everything; you get it by rejecting, at several independent stages, whatever fails a test.
   - **What the system keeps is the discriminating structure** — the test itself, the machinery that tells good from bad. **What it discards is the rejected item.** Do not try to retain the reject; retain the criterion.
   - Name each discard path, what it costs (energy, time, throughput), and where the rejected material goes. An unnamed discard path becomes a leak, a clog, or a silent corruption.

**6 · Locate the operating point between the two extremes.** Name the extreme of too much (overextension, waste, thrash) and of too little (paralysis, starvation, missed signal). State the quantity you would measure to know where the mechanism is sitting, and **which constraint moves the optimum, and in which direction.** If you cannot name the quantity and the direction, you have a slogan, not a design parameter.

**7 · Set the observation levels that keep it alive.** Name, at each level that applies, what records that the mechanism ran: physical trace, operator memory, institutional record, downstream consumer. The missing levels are where the mechanism will silently die. Note: a mechanism may legitimately sit in a **readiness** regime — holding idle capacity it is not using — and that is neither optimal throughput nor equilibrium. Budget for it deliberately rather than treating it as waste.

**8 · Name the held-open variables.** List every quantity the design needs and does not have. Do **not** fill one with a plausible value to make the design look finished: that is exactly where it will fail, and the failure will look like bad luck instead of the decision it was. Mark each as measured / derived / held open.

**9 · State the falsifier, operationally.** Name the observation that would show this design is wrong, with a threshold and an instrument. *"If it doesn't work we'll see"* is not a falsifier. A design with no operational falsifier cannot be debugged, only replaced.

**10 · Name the conjugate gap.** Every fill opens a new gap. What problem does this design create that did not exist before? Write it down now, while it is cheap. (Canon files this rule as a live hypothesis, not a law — but it costs nothing and catches real problems.)

**11 · Review against the Four Pillars.**
   - **Correctness** — is it right at the smallest unit, or right only in aggregate?
   - **Complexity** — is every part load-bearing, or is some there to look thorough?
   - **Patience** — what breaks if it is rushed into service?
   - **Resilience** — what happens at the edge condition, not the design condition?

**12 · Build in order, and document so it is re-enterable.** Define before gathering; blueprint before creating; record before repeating. If it is not written, it is not a process — it is a dependency on whoever built it. Then restart at a higher baseline: the next cycle loads this one.

---

## Failure modes of the algorithm itself

- **Skipping step 4's TERMINATE** gives a mechanism that starts and never stops.
- **Skipping step 5** gives a design that tries to keep everything and therefore cannot be accurate.
- **Filling a step-8 variable with a guess** converts an honest unknown into a scheduled failure.
- **Treating step 6 as satisfied by "balance"** without a quantity and a direction gives an unfalsifiable parameter.
- **Running it as a checklist after designing** instead of in order while designing: the order is what surfaces the omissions.

## Runs

| Run | Target | Outcome |
| --- | --- | --- |
| [`RUN-001-self-healing-pipeline.md`](RUN-001-self-healing-pipeline.md) | A self-healing, error-correcting processing pipeline | see file |
