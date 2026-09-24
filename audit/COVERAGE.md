# Coverage Map

> **Status: derivation / work-in-progress.** Updated after every audit block (brief §8, §9). A cell reads **audited / in scope**. "Sparse" and "blind" areas are named, not hidden: an unnamed blind spot is a hidden gap, which the Container's Perfection Criterion (v5.3 §3: zero **hidden** gaps) does not allow.

**As of:** 2026-09-24, after the first canon → reality pass (Phases 1–5). **Not yet run:** the reality → canon sweep (Phase 6), which looks for what the methodology does not hold.

Legend: ☐ not started · ◐ partial · ✅ covered · ⚠ sparse · ⛔ blind (no measurement source available)

---

## 1. Governance findings (Phase 1)

| Finding | Audit file | State |
| --- | --- | --- |
| F-003 base-code rule | [GOV-001](governance/GOV-001.md) | ✅ |
| F-004 Container ⊙ vs. log model | [GOV-002](governance/GOV-002.md) | ✅ (author question) |
| F-005 exclusion diagnosis | [GOV-003](governance/GOV-003.md) | ✅ |
| F-006 implicit vs. explicit log | [GOV-004](governance/GOV-004.md) | ✅ |
| F-007 container unit | [GOV-005](governance/GOV-005.md) | ✅ |
| F-008 forced-no as an outcome class | [GOV-006](governance/GOV-006.md) | ✅ |

## 2. Labels (Phase 2)

| Label class | Source in canon | In scope | Audited | State |
| --- | --- | --- | --- | --- |
| Stage names 1–49 | v5.1 Appendix A | 49 | 49 (in stage files, `proposed_label`) | ✅ |
| Stage names 50–100 | v5.1 Appendix A | 51 | 51 (in stage files) | ✅ |
| Domain names | v5.1 Layer I.C | 10 | 10 (in domain files) | ✅ |
| Layer names | v5.1 + v5.3 (⊙) | 17 | 17 ([LABEL-101–117](labels/)) | ✅ |
| Appendix D entry names | v5.1 Appendix D | 86 | in constant files | ◐ |

## 3. Stages (Phase 3)

| PR | Stages | In scope | Audited | Expected character | State |
| --- | --- | --- | --- | --- | --- |
| 9 | 1–4 | 4 | 4 | Pre-geometric through hadronization. Stage 1 largely held open (v5.4 Gap 1: first boundary proven-open). | ✅ |
| 10 | 5–10 | 6 | 6 | Light elements, decoupling, stars, supernovae, planets, prebiotic chemistry. Measurement-rich. | ✅ |
| 11 | 11–16 | 6 | 6 | RNA world through fermentation. Mixed. | ✅ |
| 12 | 17–24 | 8 | 8 | Photosynthesis through membrane potentials. Measurement-rich. | ✅ |
| 13 | 25–35 | 11 | 11 | Multicellularity through cognition. Measurement-rich. | ✅ |
| 14 | 36–49 | 14 | 14 | Self-awareness through cycle restart. Heavy in structurally derived claims. | ✅ |
| 15 | 50–85 | 36 | 36 | Projected stages. Expect mostly `unobserved-claim` (not failure). | ✅ |
| 16 | 86–100 | 15 | 15 | The variable frontier. Held open by design; confirm, do not resolve. | ✅ |
| | **Total** | **100** | **100** | | |

## 4. Constants & laws (Phase 4)

Counted from the entry rows of each table in v5.1 Appendix D (header rows excluded).

| Appendix D section | Entries | Audited | Measurement source class | State |
| --- | --- | --- | --- | --- |
| Mathematical constants | 12 | 12 | defined / computed (substrate-independent) | ✅ |
| Physical constants | 12 (+1 held-open variable row) | 13 | CODATA / NIST; PDG; Planck data releases | ✅ |
| Conservation laws | 8 | 8 | PDG limits; primary measurements | ✅ |
| Dynamical laws | 12 | 12 | primary measurements | ✅ |
| Information & computation laws | 11 | 0 | theorems (proof, not measurement) + physical bounds | ◐ in progress |
| Biological & scaling laws | 9 | 0 | primary biological datasets | ◐ in progress |
| Economic, network & social laws | 12 | 0 | empirical datasets (reproducibility varies) | ◐ in progress |
| Hermetic & framework invariants | 10 | 0 | none external — framework-internal counts | ◐ in progress |
| **Total** | **86** | **45 + pending** | | |

**Named in advance (not yet findings):** the information-and-computation section is mostly theorems, which are proved rather than measured, so their "reality" grade needs a rule; the Hermetic & framework invariants have no external measurement source by construction. Phase 4 must say how each is graded before auditing it.

## 5. Domains (Phase 5)

| # | Domain (v5.1 I.C) | Audited | State |
| --- | --- | --- | --- |
| 01 | Spiritual Process | 1 | ✅ |
| 02 | Religious Process | 1 | ✅ |
| 03 | Psychological / Cognitive Process | 1 | ✅ |
| 04 | Matrix Processes | 1 | ✅ |
| 05 | Mathematical / Computational Process | 1 | ✅ |
| 06 | Linguistic / Communication Process | 1 | ✅ |
| 07 | Economic / Market Process | 1 | ✅ |
| 08 | Chemical Process | 1 | ✅ |
| 09 | Biological Process | 1 | ✅ |
| 10 | Evolutionary Process | 1 | ✅ |

## 6. Unmapped sweep (Phase 6)

The neutral detection grid is a **search tool for the reality side**, not a category system for the methodology (brief Phase 6). Cells hold the count of `UNMAPPED-####` files found; `—` means not yet swept.

### 6.1 Scale × Organization

| Scale ↓ / Organization → | physical | chemical | biological | mental | social / systemic |
| --- | --- | --- | --- | --- | --- |
| subatomic | — | — | — | — | — |
| atomic | — | — | — | — | — |
| molecular | — | — | — | — | — |
| cellular | — | — | — | — | — |
| organism | — | — | — | — | — |
| ecosystem | — | — | — | — | — |
| planetary | — | — | — | — | — |
| stellar | — | — | — | — | — |
| galactic | — | — | — | — | — |
| cosmic | — | — | — | — | — |

### 6.2 Time axis

| instantaneous | seconds | years | geological | cosmic |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

### 6.3 Gaps in the grid itself

When the methodology predicts something the grid does not contain, it is recorded here. The check runs both ways.

| Methodology item | Why the grid misses it | Proposed grid change |
| --- | --- | --- |
| *(none yet)* | | |

## 7. Containers (Phase 7)

| Scale batch | Containers | Validated | State |
| --- | --- | --- | --- |
| *(none yet)* | 0 | — | ☐ |

---

## Additional scope (extension)

| Area | Source in canon | Audited | State |
| --- | --- | --- | --- |
| Falsifiability Register (◇) rows, revision conditions | v5.1 ◇ | 13 rows + 4 conditions → [CLAIM-001–014](claims/) | ✅ |
| Appendix B / C, Document Variable Registry "tightened" rows | v5.1 | → [CLAIM-008–019](claims/) | ✅ |
| Core Axioms with a factual core | v5.1 | Axioms 5, 7, 10, 12–16 (grouped into CLAIM files); others listed as stipulations | ◐ — Axiom 1 (business failure) not audited |

## Sparse and blind areas (named)

- **The reality → canon direction (Phase 6) has not been run.** Everything above tests what canon *says*. It cannot find what canon *omits*, except by accident (F-045 – F-051). This is the largest blind area.
- **Layers V, VI, VII (business methods):** labels audited; their empirical claims (e.g. conversion rates, BEAS calibration, "you start as a draw") are not.
- **Layer I.B case figures** (deaths, costs, $22T) — not checked; GAO source blocked.
- **Canon's per-layer and domain-specific algorithms (70+)** — not audited; most are procedures, not claims about reality.
- **v5.2 and v5.4 body text** — only where a stage or constant cited it.
- **Sources:** several rows rest on abstracts or bibliographic records rather than full text; they are graded accordingly in each file.
