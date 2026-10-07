# Agent Org Map — Task-Specific Agents for a Business Operation

> **Status: derivation, not canon** (AGENTS.md rules 4 and 7). This map turns the methodology into an operating structure of AI agents and human gates. Nothing here is a primary algorithm, and nothing here changes the base code `DETECT → PROCESS → RESPOND`.

**[`GFunnel-Agent-Org-Map.xlsx`](GFunnel-Agent-Org-Map.xlsx)** — 112 agents · 956 owned responsibilities · all 77 v5.1 algorithms (662 steps) mapped · 182 operational-table elements mapped · 15 end-to-end workflows · 21 human gates · 14 held-open variables.

| Tab | What it holds |
| --- | --- |
| README | Scope, sources, legend, attribution, live totals |
| Agent Roster | Every agent: mission, DETECT triggers, RESPOND outputs, hand-offs, tools named in canon, KPIs, human gate, failure mode guarded, autonomy, canon source |
| Responsibilities | One row per atomic responsibility: owner, source algorithm/table, canon line, cadence, trigger, output, hand-off |
| Algorithm Coverage | All 77 algorithms → owner, coverage status, steps in canon vs steps mapped |
| Canon Element Coverage | Every row of the operational tables (nine hubs' functions, Shepherd's Way, Immersion, ACE, pipeline, 7-step script, I.A.C.E., offer tiers, Four Pillars, BEAS, Five Modes, self-audit, Forcing Test, Deep-Lens…) → mapped responsibility |
| BEAS Accountability | Working 45-point BEAS scorer (yellow input cells) with the accountable agent per cell, band, canon action, lowest department, quadrant averages |
| Workflows | Lead-to-Cash, Immersion→Build, Expansion, Shepherd's Way, monthly BEAS, Hiring, Crisis, New Thought, Unknown-problem routing, Failure integration, Decisions, Vendors, Five-Mode propagation, Quarterly review, Agent-fleet change |
| Human Gates | Decisions no agent may take (the framework cannot supply the choice, the naming, or the measurement) |
| Held-Open Variables | What canon does not supply — KPI thresholds, BEAS band calibration, whether the co-creator proof holds for AI, etc. Never filled with assumption |
| Gap Check | Live formulas: agents with no responsibility, unowned responsibilities, unmapped algorithm steps, uncovered table elements — all must be 0 |

## Structure

- **Tier 0 — Governance & meta-tier:** the human Founder/Operator (G-00), Container/Forcing Test (⊙), Falsifiability (◇), Variable Registry, Compliance Auditor, AI Alignment (applied to this fleet), Governance Designer, Founder Performance.
- **Tier 1 — Orchestration & diagnostics:** Layer 0 intake, Master Meta-Algorithm router, Shepherd's Way controller, BEAS auditor, one agent per layer algorithm (I, I.B–I.G, II, III, III+), Database/Documentation, plus the cross-functional cognitive algorithms (Decision, Problem-Solving, Critical Thinking, Crisis, Pattern, Synthesis, Research).
- **Tier 2 — the Nine Hubs' leads** (v5.1 Layer V): Strategy, Marketing, Sales, Operations, Finance, HR & Culture, Technology, Client Success, Content.
- **Tier 3 — task agents:** one per canonical department function and per operational table role (e.g. Instant Response, Lead Qualification, Pipeline, Call Copilot, I.A.C.E. Coach, Offer Architect, Pre-Immersion Prep, Blueprint, Churn Prevention, Expansion & Referral…).

Life-domain, contemplative and care algorithms (Health, Relationships, Parenting, Grief, Major Life Transition, Meditation, Spiritual, Religious, Psychological) are **human-reserved**, not delegated to agents. Domains 8–10 are kept as a Correspondence reference library for the Process Cartographer. v5.4 is excluded: its constructs are not business operations, and it states zero novel predictions.

## Regenerate

```bash
python3 operations/agent-org-map/build_agent_map.py
```

The builder reads `versions/v5.1` directly, so every algorithm step is pulled from canon rather than retyped. The roster lives in `agents_data.py`. openpyxl writes formulas without cached values, so recalculate after a rebuild (for example, open the file in Excel or LibreOffice and save it) before reading totals programmatically.

## Attribution

Source: GFunnel Methodology (Omni Process) v5.1–v5.3, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. This workbook is an adaptation (restructured into an agent org map); the adaptation is not endorsed by the author.
