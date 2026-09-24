# Substrate — Input, Not Canon

> **Status: derivation / work-in-progress.** Nothing in this directory is canon. It is not a version, and it does not change any version.

## What substrate is

The Document Update Protocol (v5.1, Layer I.G — the Capsule) says every iteration **loads the prior version as substrate**. v5.3 and v5.4 extend this: each loads *declared substrate documents* alongside the prior versions (the Forcing Test module, the Container Capstone, the Forcing-Test Audit Paper, the Feb-2026 Omni Force chain). v5.4 §0 names them. [`framework/gaps.md`](../framework/gaps.md) records the cost of those documents being absent from this repository: references to them cannot be resolved here.

This directory exists so that does not happen again. A substrate document is:

- **an input** a future iteration loads, alongside the released versions;
- **dated**, and never edited after it is committed, except to fix a transcription error (same rule as `versions/`);
- **not canon.** Its content enters a version only when a Forcing Test classifies it and the author declares that version.

A substrate document may state conclusions reached with the author. Those conclusions still receive an outcome class (forced-fill / live hypothesis / stipulation / proven-open / forced-no) when a run tests them. A conclusion does not become forced because the author reached it; it becomes a **stipulation (operator decision)** unless the Forcing Test forces it outright.

## Contents

| File | Date | What it holds | Loaded by |
| --- | --- | --- | --- |
| [`2026-09-24-reality-filter.md`](2026-09-24-reality-filter.md) | 2026-09-24 | The governing model of the Reality Audit: reality is the authority, the methodology is the growing log of the known, concentration discipline, no imported models, containers, the scoped base-code rule, weak observations cannot force change. | [`tasks/reality-audit/TASK.md`](../tasks/reality-audit/TASK.md) and every audit phase; the v5.5 draft (Phase 8) |

## How to cite a substrate document

Name it by path and date, and say it is substrate, e.g. *"substrate/2026-09-24-reality-filter.md §2.7 (substrate, unclassified)"*. Do not cite it as a version.
