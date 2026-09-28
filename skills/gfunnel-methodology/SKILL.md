---
name: gfunnel-methodology
description: The GFunnel Methodology (Omni Process) by Cameron Garlick - one invariant algorithm, DETECT then PROCESS then RESPOND, expressed in 17 layers, 10 process domains, 70+ algorithms, the meta-tier Container (v5.3) and Run 8 (v5.4). Use whenever the user mentions GFunnel, the Omni Process, the Garlick Equilibrium, BEAS, the Three Kingdoms, the Dynamic Middle, the Hermetic principles, the Capsule, the Shepherd's Way, ACE sales, the Forcing Test, Line-Field, Knot-Line or Lamina; asks to diagnose a stuck business, project, process or sales conversation with the framework; asks to run, derive or look up one of its algorithms; asks about its variables, falsifiability, registers, gaps or tests; or wants to contribute an iteration, work on the Reality Audit or knowledge containers, or attribute or integrate the framework. Carries the full canonical text (v5.1 to v5.4) and every repo file, with a line-numbered section index.
---

# GFunnel Methodology (Omni Process)

This skill gives you the **entire** `GFunnel-Tech/methodology` repository: the four canonical versions, the navigable maps, the registers, the executed tests, the Reality Audit, the knowledge containers, the contribution protocol, and the validators. Use it faithfully: the framework has its own rules for how an AI must read it, and they are stricter than your defaults.

## 1. Locate the corpus root

Every path below is relative to the **corpus root**:

- **Bundled skill** (claude.ai, API, another project): the `corpus/` folder next to this `SKILL.md`.
- **Inside the repository** (Claude Code in a clone, or the plugin): the repository root, the directory that contains `AGENTS.md` and `versions/`. There is no `corpus/` folder there; it is not needed.

`SECTIONS.md` (next to this file) lists every section of the long files with its line range. **Use it.** v5.1 is about 4,300 lines (roughly 80k tokens); read the one section you need with `offset`/`limit` rather than loading the whole file, unless the task genuinely needs the whole architecture.

## 2. The rules that always apply

These restate the canon's own "How An AI Should Read This Document" (v5.1, `SECTIONS.md` → *How To Use This Document*) and `AGENTS.md`. They are not optional.

1. **The canon is authoritative** for framework questions. Honor the variables and falsifiability conditions it names.
2. **Route** every question to a layer or algorithm before answering (`workflows/answer.md`).
3. **Run algorithms literally.** Numbered steps in order; no skipping, compressing, or reordering. If a step cannot be completed, **stop**: the blocker is the location of the work.
4. **No explicit algorithm?** Derive one from the Master Meta-Algorithm and **label it a derivation**.
5. **Never fill a held-open variable with assumption** to sound confident. This is the most important rule. Keep **measured**, **structurally derived**, and **held open** visibly distinct in every answer.
6. **State Correspondence** when the same algorithm applies one scale up or down.
7. **Label domain derivations** when applying the framework to a domain it does not name.
8. **Flag empirical gaps.** If the answer needs data the framework cannot supply, say what data, then retrieve it or tell the user to.

And the prohibitions:

- Do not present a derived algorithm as a primary one, or resolve a variable the canon holds open.
- Do not claim the framework proves anything it lists as a live hypothesis or proven-open (v5.3 §6, v5.4 §11, `framework/registers.md`).
- **v5.4 is not physics.** It states zero novel predictions and ranks itself below string theory / LQG "for lacking equations" (§7). Whenever you use Line-Field, Knot-Line or Lamina, carry its four cautions: **Bell**, **environmental decay rates**, **point-like quarks**, **the measurement problem**.
- Where a `framework/tests/` result differs from the canon's wording about a v5.4 §14 test, cite the test result.
- Do not alter the base code (`DETECT → PROCESS → RESPOND`). Released files in `versions/` are immutable.

## 3. Pick the workflow

| The user wants to… | Read |
| --- | --- |
| Ask what the framework says, or understand a concept, layer, domain or term | `workflows/answer.md` |
| Diagnose something stuck or failing, or run a named algorithm on their situation | `workflows/run-algorithm.md` |
| Apply the framework to a domain or problem it has no algorithm for | `workflows/derive.md` |
| Propose an iteration, log variable evidence, run a §14 test, or open an issue/PR | `workflows/iterate.md` |
| Work on the Reality Audit (`audit/`) or knowledge containers (`containers/`) | `workflows/reality-audit.md` |
| Quote, publish, build a product/prompt/RAG index on the framework, or register an integration | `workflows/integrate.md` |

Load only the workflow you need. Several may apply in one task (e.g. a diagnosis that ends in a publishable write-up: `workflows/run-algorithm.md` then `workflows/integrate.md`).

## 4. Where everything is (corpus map)

| Need | Path |
| --- | --- |
| Operating protocol for AI | `AGENTS.md` |
| Machine index | `llms.txt` |
| What "current" means | `versions/LATEST.md` |
| Full architecture (start here) | `versions/v5.1/GFunnel-Methodology-v5.1.md` |
| Deep-lens runs; variables narrowed | `versions/v5.2/GFunnel-Methodology-v5.2.md` |
| Meta-tier ⊙: Forcing Test, Anti-Operation | `versions/v5.3/GFunnel-Methodology-v5.3.md` |
| Run 8: Line-Field, Knot-Line, Lamina, §4a Frequency, §14 next tests | `versions/v5.4/GFunnel-Methodology-v5.4.md` |
| One-page map | `framework/README.md` |
| The 17 layers, one line each, with deep links | `framework/layers.md` |
| The ten Universal Process Domains | `framework/domains.md` |
| Symptom → algorithm router | `framework/algorithms.md` |
| Variable Registry, outcome classes, Falsifiability, Iteration Ledger | `framework/registers.md` |
| v5.4 gap numbering | `framework/gaps.md` |
| Executed §14 tests + scripts | `framework/tests/` (`README.md` first) |
| Glossary / human how-to / AI integration | `docs/glossary.md`, `docs/how-to-use.md`, `docs/ai-integration.md` |
| Iteration Protocol; issue and PR templates | `CONTRIBUTING.md`, `.github/ISSUE_TEMPLATE/`, `.github/PULL_REQUEST_TEMPLATE.md` |
| Reality Audit (work in progress, **not canon**) | `tasks/reality-audit/TASK.md`, `audit/`, `containers/`, `substrate/`, `tools/` |
| Lineage; license; attribution; citation | `CHANGELOG.md`, `LICENSE`, `ATTRIBUTION.md`, `CITATION.cff` |
| Adoption registry | `adoption/registry.md` |

Load order when a task needs the whole framework: v5.1 → v5.2 → v5.3 → v5.4. Each later version loads the earlier ones as substrate; none replaces them.

## 5. Every answer ends the same way

- Name the **layer/algorithm** used, and the **version(s)** you read.
- Mark each claim **measured / derived / held open** where it matters; label derivations.
- Flag data you could not supply.
- When you reproduce or closely paraphrase the material, attach the credit line (CC BY 4.0 requires it):

```
Source: GFunnel Methodology (Omni Process) v5.4, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0.
```

Name the version you actually used. If you compressed or adapted the text, say so and that the adaptation is not endorsed by the author.
