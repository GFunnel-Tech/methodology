# The Reality Audit

> **Status: derivation / work-in-progress. Not canon.** The audit schema, the diff states, the exclusion diagnosis, and the container unit are all derivations created by this task. They enter a version only when the author declares one (Phase 8, v5.5 draft).

The audit compares two logs:

| Log | What it is | Where it lives |
| --- | --- | --- |
| **Reality (the implicit log)** | Reality records itself in its own structure. We hold reproducible observations of it, each with a measurement source. | `audit/`: observation tables inside each audit file |
| **The methodology (the explicit log)** | The written record of what is known. | [`versions/`](../versions/README.md), [`framework/`](../framework/README.md) |

For every stage, constant, domain, and label in canon, the audit asks whether reality supports it. For every reproducible observation the methodology does not hold, the audit diagnoses **why** before classifying it. Every item that is solved or gained leaves a **container** in [`../containers/`](../containers/README.md).

- The standing brief: [`../tasks/reality-audit/TASK.md`](../tasks/reality-audit/TASK.md)
- The governing model (substrate): [`../substrate/2026-09-24-reality-filter.md`](../substrate/2026-09-24-reality-filter.md)
- The record formats: [`SCHEMA.md`](SCHEMA.md)
- What is confirmed so far: [`FINDINGS.md`](FINDINGS.md)
- What is covered, sparse, or blind: [`COVERAGE.md`](COVERAGE.md)

---

## The governing run (Master Meta-Algorithm, v5.1)

The task itself is run through the 12 steps of the Master Meta-Algorithm, in order. This is the record of that run. Each later phase reports against it.

1. **Identify the domain.** Reconciliation of the explicit log (the methodology) against the implicit log (reality).
2. **Locate the Three Kingdoms alignment.** Second Kingdom (the framework), executed into First Kingdom (repository commits).
3. **Identify the current state.** v5.4 canon; v5.1 Appendices A–D; the gap register ([`framework/gaps.md`](../framework/gaps.md)); the executed tests ([`framework/tests/`](../framework/tests/README.md)); the session substrate (committed in Phase 0 as [`substrate/2026-09-24-reality-filter.md`](../substrate/2026-09-24-reality-filter.md)).
4. **Identify the desired state.** Every stage, constant, domain, and label carries a reality status. Every unmapped observation is diagnosed. Every solved item has a container. The session conclusions enter canon through a v5.5 draft that the author declares.
5. **Locate the dynamic middle.** Yang extreme: rewriting canon. Yin extreme: leaving everything as notes. Middle: substrate → audit → containers → v5.5 draft.
6. **Identify the violated Hermetic principle.** Correspondence. Structures were being built beside canon instead of corresponding to it. Correction: every audit file maps to a canonical item (`canon_ref` is a required field).
7. **Identify the gradient.** The difference between the two logs. The audit output *is* the gradient.
8. **Set the cause.** Run the Scientific Inquiry Algorithm (v5.1, 10 steps) on every item against observation, then the Forcing Test (v5.3, Tests A–D).
9. **Build the structure.** Intent (reality is the authority) → organization (schemas, files, validators — Phase 0) → execution (audit files, containers, PRs — Phases 1–8). The organization step is not skipped.
10. **Run the cycle.** Phases 1–8 of the brief.
11. **Document the result.** Audit files, containers, Iteration Ledger rows, CHANGELOG entries.
12. **Restart at higher baseline.** Phase 9: re-review every `open` item on its `review_after` date; re-sweep sparse cells; re-audit when new measurement releases appear. Each cycle loads all prior cycles (Capsule).

### Run status

| Step | State | Note |
| --- | --- | --- |
| 1–9 | ✅ done in Phase 0 | Organization built: this directory, [`SCHEMA.md`](SCHEMA.md), [`../containers/`](../containers/README.md), [`../tools/`](../tools/README.md). |
| 10 | ☐ queued | Phase 1 onward. |
| 11 | ◐ ongoing | Every phase documents as it goes. |
| 12 | ☐ queued | Phase 9. |

---

## How to read an audit file

Each file under `stages/`, `constants/`, `domains/`, `labels/`, `unmapped/`, and `governance/` is one audited item. Front matter first, then the body.

1. **`canon_ref` / `canon_label`**: which canonical item this is, and where.
2. **`diff_state`**: how the two logs compare (`accounted`, `methodology-gap`, `unobserved-claim`, `conflict`, `unmapped`).
3. **`exclusion_diagnosis`**: *why* something is missing or conflicting. Required before any `methodology-gap`, `conflict`, or `unmapped` item is classified.
4. **`claim_outcome`**: the Forcing Test outcome for the methodology's claim.
5. **`intake_result`**: what happened to the observation (`integrated`, `adjusted`, `open`). An `open` item always carries a `review_after` date.
6. **Reality shows**: the measured quantities, each with value, uncertainty, grade, source, and retrieval date. No interpretive wording.
7. **Scientific Inquiry run** and **Forcing Test**: the literal runs, step by step. If a step could not be completed, the file says so and stops there. The blocker is the location of the work.
8. **Anti-Operation**: the gap this result opens.
9. **Narrative stripped**: interpretation removed because reality does not force it.

The full vocabularies are in [`SCHEMA.md`](SCHEMA.md).

## Directory layout

```
audit/
  README.md        ← this file (the governing run)
  SCHEMA.md        ← vocabularies and record formats
  FINDINGS.md      ← running list of confirmed findings
  COVERAGE.md      ← what is audited, what is sparse, what is blind
  governance/      ← GOV-### Forcing Test runs on governance findings (Phase 1)
  stages/          ← STAGE-001 … STAGE-100 (Phase 3)
  constants/       ← CONST-<slug> (Phase 4)
  domains/         ← DOMAIN-01 … DOMAIN-10 (Phase 5)
  labels/          ← LABEL-### (Phase 2)
  unmapped/        ← UNMAPPED-#### (Phase 6)
  issues/          ← drafted issue bodies (the `gh` CLI is not available to the executor)
```

## Validating

```bash
python3 tools/validate_audit.py          # every audit file: front matter, vocabularies, required sections
python3 tools/validate_containers.py     # every container: fields, trace, ≥1 open edge, index entry
```

Standard library only. See [`../tools/README.md`](../tools/README.md).

---

```
Source: GFunnel Methodology (Omni Process) v5.4, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0.
```
