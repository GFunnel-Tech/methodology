# Agent Org Map — Task-Specific Agents for a Business Operation

> **Status: derivation, not canon** (AGENTS.md rules 4 and 7). This map turns the methodology into an operating structure of AI agents and human gates. Nothing here is a primary algorithm, and nothing here changes the base code `DETECT → PROCESS → RESPOND`.

**[`GFunnel-Agent-Org-Map.xlsx`](GFunnel-Agent-Org-Map.xlsx)** — 148 agents (incl. 27 team leads) · 1,237 owned responsibilities · all 77 v5.1 algorithms (662 steps) mapped · 182 operational-table elements mapped · 19 end-to-end workflows · 80 deliverables with an accountable manager · an Operating Rhythm of 21 reports and channels to the Owner · 21 human gates · 14 held-open variables.

| Tab | What it holds |
| --- | --- |
| README | Scope, sources, legend, attribution, live totals |
| Deliverables | "I need X done" → the accountable manager agent and the team that does it (e.g. Newsletter issue → CON-T1 Editorial & Email Team Lead) |
| Operating Rhythm | Every report and channel to the Owner: cadence (continuous → quarterly), from, to, contents, canon anchor |
| Org Chart | The reporting hierarchy as an indented tree: level, solid line, dotted line, direct reports, reporting path, span of control |
| Agent Roster | Every agent (now with a Dotted Line column): mission, DETECT triggers, RESPOND outputs, hand-offs, tools named in canon, KPIs, human gate, failure mode guarded, autonomy, canon source |
| Responsibilities | One row per atomic responsibility: owner, source algorithm/table, canon line, cadence, trigger, output, hand-off |
| Algorithm Coverage | All 77 algorithms → owner, coverage status, steps in canon vs steps mapped |
| Canon Element Coverage | Every row of the operational tables (nine hubs' functions, Shepherd's Way, Immersion, ACE, pipeline, 7-step script, I.A.C.E., offer tiers, Four Pillars, BEAS, Five Modes, self-audit, Forcing Test, Deep-Lens…) → mapped responsibility |
| BEAS Accountability | Working 45-point BEAS scorer (yellow input cells) with the accountable agent per cell, band, canon action, lowest department, quadrant averages |
| Workflows | Lead-to-Cash, Immersion→Build, Expansion, Shepherd's Way, monthly BEAS, Hiring, Crisis, New Thought, Unknown-problem routing, Failure integration, Decisions, Vendors, Five-Mode propagation, Quarterly review, Agent-fleet change |
| Human Gates | Decisions no agent may take (the framework cannot supply the choice, the naming, or the measurement) |
| Held-Open Variables | What canon does not supply — KPI thresholds, BEAS band calibration, whether the co-creator proof holds for AI, etc. Never filled with assumption |
| Gap Check | Live formulas: agents with no responsibility, unowned responsibilities, unmapped algorithm steps, uncovered table elements — all must be 0 |

**[`GFunnel-Agent-Operating-System.drawio`](GFunnel-Agent-Operating-System.drawio)** — the whole system in draw.io, five pages: (1) Operating Model — Owner, Owner Liaison, intake → router → work board → teams → Shepherd's Way, governance checks, project signals; (2) Org Chart — every agent; (3) Reporting & Communication — every report and channel by cadence, sender lane → receiver lane; (4) Work Suggestion Loop — signals → proposal card → Owner decision → board → delivery → actual-vs-expected → integration; (5) Team at Work — one newsletter issue through the Editorial & Email team on the work board. Open at app.diagrams.net or in the draw.io desktop app; rebuild with `build_drawio.py`.

**[`org-chart.html`](org-chart.html)** — interactive org chart (search a deliverable to find its owner; select an agent for its full card). Rebuild with `build_org_chart.py` after the workbook is recalculated.

## Structure

- **Tier 0 — Governance & meta-tier:** the human Founder/Operator (G-00), Container/Forcing Test (⊙), Falsifiability (◇), Variable Registry, Compliance Auditor, AI Alignment (applied to this fleet), Governance Designer, Founder Performance.
- **Tier 1 — Orchestration & diagnostics:** headed by the Algorithm Router (chief-of-staff role); Layer 0 intake, Master Meta-Algorithm router, Shepherd's Way controller, BEAS auditor, one agent per layer algorithm (I, I.B–I.G, II, III, III+), Database/Documentation, plus the cross-functional cognitive algorithms (Decision, Problem-Solving, Critical Thinking, Crisis, Pattern, Synthesis, Research).
- **Owner channel and work system (derived):** **O-23 Owner Liaison** is the Owner's single channel — daily brief, weekly report, approvals inbox, decision log, and Owner requests turned into work. **O-25 Work Board Dispatcher** keeps one board for all work and dispatches to team leads. **O-24 Work Suggestion Agent** proposes the next work from project signals (lowest BEAS cell, stalls, lowest funnel step, clients' next step, risks, patterns), each with an expected outcome and a falsifier, for the Owner to approve.
- **Tier 2 — the Nine Hubs' leads** (v5.1 Layer V), reporting directly to the founder, with dotted lines to the BEAS Auditor and the Shepherd's Way controller: Strategy, Marketing, Sales, Operations, Finance, HR & Culture, Technology, Client Success, Content.
- **Tier 3 — team leads (27):** every deliverable has one accountable manager agent that takes the request, runs the Shepherd's Way at team scale, assigns its team, approves the output and closes it with documentation. Example: the **Editorial & Email Team Lead (CON-T1)** manages a Newsletter Producer, Email Copywriter, Writing Agent, Editor & Proofreader, Brand Voice & Claims Checker, Editorial Calendar & Send Scheduler and Email Performance Analyst, and the team runs the Writing Algorithm between them (the lead owns steps 1, 2 and 9).
- **Tier 4 — task agents:** one per canonical department function and per operational table role (e.g. Instant Response, Lead Qualification, Pipeline, Call Copilot, I.A.C.E. Coach, Offer Architect, Pre-Immersion Prep, Blueprint, Churn Prevention, Expansion & Referral…).

Life-domain, contemplative and care algorithms (Health, Relationships, Parenting, Grief, Major Life Transition, Meditation, Spiritual, Religious, Psychological) are **human-reserved**, not delegated to agents. Domains 8–10 are kept as a Correspondence reference library for the Process Cartographer. v5.4 is excluded: its constructs are not business operations, and it states zero novel predictions.

Reporting lines, teams and deliverable owners are **derived** (canon names hubs and functions, not who reports to whom); redraw them freely in `agents_data.py`.

## Regenerate

```bash
python3 operations/agent-org-map/build_agent_map.py   # workbook
# recalculate the workbook (open and save in Excel/LibreOffice), then:
python3 operations/agent-org-map/build_org_chart.py    # org-chart.html
python3 operations/agent-org-map/build_drawio.py       # GFunnel-Agent-Operating-System.drawio
```

The builder reads `versions/v5.1` directly, so every algorithm step is pulled from canon rather than retyped. The roster lives in `agents_data.py`. openpyxl writes formulas without cached values, so recalculate after a rebuild (for example, open the file in Excel or LibreOffice and save it) before reading totals programmatically.

## Attribution

Source: GFunnel Methodology (Omni Process) v5.1–v5.3, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. This workbook is an adaptation (restructured into an agent org map); the adaptation is not endorsed by the author.
