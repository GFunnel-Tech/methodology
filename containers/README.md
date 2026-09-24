# Knowledge Containers (KC)

> **Status: derivation / work-in-progress. Not canon.** Canon has no standard unit for "a solved item, written so no one has to re-study it" (FINDINGS [F-007](../audit/FINDINGS.md)). This directory defines one. It is a derivation until the author declares it into a version.

## What a container is

A **knowledge container** is the reference point left behind by every item the Reality Audit solves or gains. It carries:

1. **Observations**: the measured quantities it rests on, each with uncertainty, grade, and source.
2. **Form**: an **equation** (only if measured, or derived with a shown trace), an **algorithm** (numbered steps: the fastest route from this reference point), or both. If neither can be stated honestly, the form is `held-open`.
3. **Trace**: how it was reached, step by step.
4. **Open edge**: at least one gap the solution opens. This keeps the container open-ended.
5. **Re-formation log**: dated entries each time reality re-shapes it.

It corresponds to two things canon already names:

- **v5.1 Master Meta-Algorithm step 11** — *"if it is not written, it does not exist as a process."* A container is the written form of a result.
- **The Anti-Operation** (v5.3; used throughout v5.4) — every fill opens a conjugate gap. That is why a container with no open edge is invalid.

Whether this correspondence is forced, a refinement, or a stipulation is classified in Phase 1 (PR 5).

## "KC" is not "⊙"

The prefix **KC** ("knowledge container") keeps these files distinct from **Layer ⊙, the Container** (v5.3's meta-tier). ⊙ is the framework run against itself: the classifier, the generator, the falsifiability component, and the loop. A KC is a single result. How the two relate is FINDINGS [F-004](../audit/FINDINGS.md) / [F-007](../audit/FINDINGS.md), audited in Phase 1. Do not treat a KC as an instance of ⊙ until that audit says so.

## Rules

- Create containers for `forced-fill` items, and for `integrated` observations that have a measured equation or a derived algorithm.
- A `live-hypothesis` container says so plainly and carries its **falsifier**. It is never presented as solved.
- **Never invent an equation.** An equation enters only if it is measured or derived with a shown trace. Otherwise write an algorithm, or mark the form `held-open`.
- **Every container has at least one open edge.**
- **Re-form, do not overwrite.** When reality changes a container, append a dated entry to its re-formation log and update `last_reformed`. Never delete prior entries.
- **Name by observation, not narrative.** The `name` field describes what is measured, not a story about it.
- **Link by Correspondence.** `links_up` / `links_down` point to the container one scale up and one scale down, when they exist.
- Register every container in [`INDEX.md`](INDEX.md).

## Files

- [`TEMPLATE.md`](TEMPLATE.md) — copy this to start a container.
- [`INDEX.md`](INDEX.md) — every container, by canonical item and by scale.
- `KC-####-<slug>.md` — the containers (none yet; population is Phase 7).

## Validate

```bash
python3 tools/validate_containers.py
```

Checks required fields and vocabularies, a non-empty trace, at least one open edge, at least one dated re-formation entry, equation/algorithm presence matching `form`, a falsifier on live hypotheses, link targets that exist, and an `INDEX.md` entry for every container. Full specification: [`../audit/SCHEMA.md`](../audit/SCHEMA.md) §5.
