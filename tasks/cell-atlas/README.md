# Cell Atlas — Every Process of the Eukaryotic Cell, Run Through the Methodology

> **Status: derivation / work-in-progress. Not canon.** Canon names the cell (v5.1 Domain 9; "The Cell — All Seven Hermetic Principles in One Unit"; Appendix A Stages 12, 13, 23, 24) but gives no algorithm for any single cellular process. Every run here is a **derivation** from the Master Meta-Algorithm via the v5.2 Deep-Lens Protocol (AGENTS.md rules 4 and 7).

## Goal

Break the eukaryotic cell into every known process, run each one through the methodology, and pull out the algorithm and the recurring patterns. Start with the plasma membrane (the lipid bilayer and everything it does), then move inward.

Breakdown is **top-down**: the whole structure as one process (L0), then functional categories (L1), subcategories (L2), mechanism families (L3), and specific mechanisms (L4). Runs follow the same order. The decomposition rule is a derivation: see [`membrane/README.md`](membrane/README.md) and gap MF-03.

Completeness is a **held-open variable**. Cell biology is still finding membrane mechanisms. The inventory carries an open edge and grows; it never claims to be final.

## Method (applied identically to every process)

Each process gets one run file. A run has three tiers that are **never mixed**:

| Tier | What goes here | Rule |
| --- | --- | --- |
| **Measured** | Quantities with value, uncertainty, grade, source (DOI or stable URL) | Grades from [`audit/SCHEMA.md`](../../audit/SCHEMA.md) §1.1. Numbers only; strip the source's narrative. |
| **Derived** | The mechanism as numbered steps; any equation, with a shown trace and a reproducible stdlib script in [`scripts/`](scripts/) | No invented equations. |
| **Framework mapping** | The Deep-Lens steps A–L (v5.2 §1) | Labelled a derivation. Where a step cannot be completed honestly, **stop at that step and log the blocker** — do not fill it. |

Each run ends with:

1. **Patterns extracted** — reusable, mechanism-level patterns, added to [`patterns.md`](patterns.md).
2. **Container-ready block** — the measured equation and/or algorithm in the form a `KC-####` container needs ([`containers/README.md`](../../containers/README.md)). Containers are not created yet: the Reality Audit schedules container population for Phase 7, so turning runs into containers is the maintainer's call.

## Areas

| Area | Inventory | Runs done |
| --- | --- | --- |
| Plasma membrane | [`membrane/README.md`](membrane/README.md) · gaps: [`membrane/gaps.md`](membrane/gaps.md) | L0 mapped; 11 L1 categories queued; 1 L4 pilot (out of order) |
| **Function area:** information — filter, keep, erase, update | [`information/README.md`](information/README.md) · gaps: [`information/gaps.md`](information/gaps.md) | L0 mapped; 6 L1 categories queued |
| *(next: cytoskeleton, nucleus, ER, Golgi, mitochondria, lysosome, …)* | — | — |

## Files

- [`membrane/`](membrane/README.md) — the membrane breakdown, its gap register, and its runs.
- [`patterns.md`](patterns.md) — the cross-process pattern catalogue. This is where "the algorithm/patterns from each" accumulate.
- [`scripts/`](scripts/) — reproducible checks, Python standard library only (same convention as [`framework/tests/`](../../framework/tests/README.md)).

```
Source: GFunnel Methodology (Omni Process) v5.1/v5.2, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0.
```
