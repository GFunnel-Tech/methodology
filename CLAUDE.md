# CLAUDE.md — How an AI operates in this repository

> **FIRST, before anything else — three lines you must act on:**
> 1. **Pick the mode and say it** in your first line: `Mode: Answer | Diagnose | Estimate | Both | Contribute` (§1). Diagnose = full methodology, every step. Estimate = instruments only, route to `formulas/`.
> 2. **Every quantity carries a tag**: `measured` · `forced` · `estimate` · `assumption` · `held-open` · `conflict`, with a range and a falsifier on every estimate/assumption (§2). A value may be omitted only when no prior, no structure, no analogue and no trend exists.
> 3. **Your answer is linted on Stop** (`tools/check_output.py`, wired in `.claude/settings.json`). An estimate-shaped answer with untagged numbers, or a refusal without the four-part reason, is sent back to you before the user sees it.

Read [`AGENTS.md`](AGENTS.md) first; it is the canonical protocol and this file does not replace it. This file adds the **runbook**: which mode to work in, which tool to run, and the exact commands. The packaged form is the `gfunnel-methodology` skill ([`skills/gfunnel-methodology/SKILL.md`](skills/gfunnel-methodology/SKILL.md)); when it is available, invoke it and follow its workflow files.

## 1. Pick the mode before reading anything else

Everything in the methodology is one of two kinds of work. Decide which the task is **first**, because the two load different parts of the repository and loading the wrong one costs 3–4× the time for no accuracy (`audit/VERDICT.md`; `substrate/2026-10-20-estimate-protocol.md` §5).

| The user wants… | Mode | Load | Workflow |
| --- | --- | --- | --- |
| to understand a concept, layer, domain or term | **Answer** | the one section named in `skills/gfunnel-methodology/SECTIONS.md` | `workflows/answer.md` |
| to know *why* something is stuck or failing, or to run a named algorithm on their situation | **Diagnose — the full methodology** | v5.1 (route by `framework/algorithms.md`), the layer's section, the algorithm's text; v5.2–v5.4 as needed | `workflows/run-algorithm.md` (derive via `workflows/derive.md` if no algorithm fits) |
| **a number that is not yet in the record**: fill gaps in a table, forecast, compare datasets, narrow an open question, calculate one system from another | **Estimate — the instruments only** | the Variable Principle · the Forecasting Algorithm · Layer ◇ step 2 · the Forcing Test outcomes · the Estimate Protocol | **`workflows/estimate.md`** |
| both (diagnose, then put numbers on it) | Diagnose, then Estimate | as above, in that order | both |
| to contribute, audit, or integrate | — | `CONTRIBUTING.md`, `audit/`, `docs/ai-integration.md` | `workflows/iterate.md`, `reality-audit.md`, `integrate.md` |

**Say which mode you chose and what you did not load.** A forecast that cites the Hermetic principles is a routing error. A diagnosis that skips the Three Kingdoms is also one.

## 2. The rule that governs every output (rule 5, as amended 2026-10-20)

**Never fill a variable silently; never refuse to fill one that has a prior, structure, analogue or trend.** Every quantity you emit carries one tag:

`measured` · `forced` · `estimate` · `assumption` · `held-open` · `conflict`

with a range and a falsifier on every `estimate` and `assumption`. A value may be omitted (`held-open`) only when **no prior, no structure, no analogue and no trend** exists. Anything that has happened before has a prior. The Big Bang's first moment passes that test; next quarter's revenue does not.

## 3. The formulas: when to run which

All in [`formulas/`](formulas/README.md). Standard-library Python; nothing to install. The catalogue of **every** formula in the repository, with status and test result, is [`formulas/README.md`](formulas/README.md).

| Input shape | Tool | What comes back |
| --- | --- | --- |
| a table with empty cells | `formulas/omni_gap.py` — `OmniGap(...).fill()` | per cell: value, 90% range, tag, falsifier, next measurement |
| one quantity, several measurements that may disagree | `formulas/ledger.py` — `new` / `add` / `run` / `seal` | per gap: narrowed · conflict · held-open; the witness whose removal restores agreement; the precision a decisive measurement needs |
| a situation and a request to predict its metrics | `formulas/forecast.py` — `new` → fill → commit → `score` | a sealed two-arm sheet, every metric tagged; later a scored hit rate and error per tag |
| two systems that may correspond, one thin | `OmniGap(..., correspondences=[Correspondence(...)])`; pattern in `formulas/correspondence_test.py` | estimates in the thin system from the rich one, and a verdict per column: correspondence **held** / **not supported here** |
| a question in conversation, no file | the protocol by hand: `workflows/estimate.md` §3 | the same card, written out |
| what has already been computed, and how reliable each tag has been | `formulas/memory.py show` (every run records itself; pass `memory=Memory()` to `OmniGap` to pool calibration with prior runs of the same expression and size) | earned calibration per variable; hit rate and required widening per tag; the conjugate gaps past runs named |

Exact invocations, with the arguments explained: `workflows/estimate.md` §2. The visual of the whole pipeline and this router: [`formulas/diagrams/`](formulas/diagrams/README.md).

## 4. Before you finish

- Mode named; loaded and not-loaded named.
- Every number tagged; every estimate ranged and falsifiable; nothing left blank that has a prior.
- Derivations labelled; held-open items listed with the measurement that would close them.
- Canon text reproduced → credit line (`AGENTS.md` → Attribution).
- Repository changed → `python3 tools/build_skill.py --check` passes; formulas touched → `python3 formulas/benchmark.py` and `python3 formulas/correspondence_test.py` still run; `formulas/README.md` has a row for any new formula.
- Released files in `versions/` are never edited. Corrections to canon are logged (`formulas/README.md` §10, `CHANGELOG.md`), not applied.
