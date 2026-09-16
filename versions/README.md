# Versions — Canonical Documents

This directory holds the **canonical, faithful text** of each release of the GFunnel Methodology. These are the source of truth. Everything in [`framework/`](../framework/README.md) and [`docs/`](../docs/) navigates *into* these files; it never restates or overrides them.

## Convention

- **One directory per version.** `vX.Y/GFunnel-Methodology-vX.Y.md`.
- **Versions are immutable once released.** Do not edit released text to "fix" it — corrections and refinements happen in a *new* version, so the lineage stays honest and nothing is lost. (Typo-level transcription fixes to match the authored original are the only exception; log them in `CHANGELOG.md`.)
- **Each version loads the prior as substrate.** See [`LATEST.md`](LATEST.md) for load order.

## Contents

| Version | Title | Summary |
| --- | --- | --- |
| [v5.1](v5.1/GFunnel-Methodology-v5.1.md) | The Complete System — Operational Edition | The full architecture. 17 layers, 10 Universal Process Domains, 70+ algorithms, the 100-Stage Progression, four appendices. Self-contained. |
| [v5.2](v5.2/GFunnel-Methodology-v5.2.md) | Deep-Lens on Every Mechanism | The framework executing its own Document Update Protocol on itself. Five deep-lens runs; nine variable movements; no base-code change. |
| [v5.3](v5.3/GFunnel-Methodology-v5.3.md) | The Meta-Tier | Names Layer ⊙, the Container — the framework run against itself, made architectural. The first structural addition; the object-level layers are untouched. |
| v5.4 *(proposed)* | Run 8 — Line-Field, Knot-Line, Lamina | **Canonical text not yet in this repository.** Ledger and glossary updates have landed; the version directory has not. See [`../CHANGELOG.md`](../CHANGELOG.md). |

## A note on formatting

The v5.1 and v5.2 texts were transcribed from the authored source documents into Markdown, preserving heading hierarchy, tables, quote callouts, and section order. The intent is a **faithful** rendering suitable for reading, diffing, and loading into AI context — not an editorial rewrite. If you spot a transcription discrepancy against the authored original, open an issue with the `transcription` label.
