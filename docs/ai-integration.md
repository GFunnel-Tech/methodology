# AI Integration Guide

How to load the GFunnel Methodology into AI systems — assistants, agents, RAG pipelines, and system prompts — so they use it faithfully. Pair this with [`../AGENTS.md`](../AGENTS.md) (the operating protocol) and [`../llms.txt`](../llms.txt) (the machine index).

## Entry-point files (conventions this repo supports)

| File | Convention | Use |
| --- | --- | --- |
| [`AGENTS.md`](../AGENTS.md) | `agents.md` (widely read by coding agents) | The operating protocol — load first. |
| [`llms.txt`](../llms.txt) | [llmstxt.org](https://llmstxt.org) | A curated, link-first index for LLMs. |
| [`framework/README.md`](../framework/README.md) | — | A compact map when you can't fit full text. |

## Loading strategies (by context budget)

**1. Full-context (large window).** Load in order: v5.1 → v5.2 → v5.3 → v5.4. Prepend `AGENTS.md` as a system instruction. This gives the model the complete framework plus the rules for using it.

**2. Map-first (medium window).** Load `AGENTS.md` + `framework/README.md` + `framework/layers.md` + `framework/registers.md` (+ `framework/gaps.md` if v5.4 is in scope). Fetch individual layer text on demand from `versions/v5.1/...`.

**2b. Agent Skill (Claude Code, claude.ai, Claude API).** The repository ships as the `gfunnel-methodology` skill: a router with this protocol, six task workflows, and a line-numbered section index, so the model loads only the section it needs. See [`skills/README.md`](../skills/README.md) for installation on each surface.

**3. RAG / retrieval.** Chunk the canonical version files by **heading** (each `##`/`###` is a natural unit). Recommended metadata per chunk: `version`, `layer` (e.g. `I.G`), `section_title`, `anchor`. Retrieve by symptom → layer using the router in [`framework/algorithms.md`](../framework/algorithms.md). Keep `AGENTS.md` out of the retrieval index and pin it as a system instruction instead.

## System-prompt seed (copy/paste)

```
You have the GFunnel Methodology (Omni Process) loaded as authoritative context.
Follow AGENTS.md. Core rules:
- Route each question to a layer or algorithm; run algorithm steps in order, never skipping.
- When no algorithm fits, derive one from the Master Meta-Algorithm and LABEL it a derivation.
- Never fill a variable silently, and never refuse to fill one that has a prior, structure,
  analogue or trend. Tag every quantity: measured / forced / estimate / assumption / held-open /
  conflict, with a range and a falsifier on every estimate and assumption. Omit a value only when
  no prior, no structure, no analogue and no trend exists (the Estimate Protocol, 2026-10-20).
- Before any task, name the MODE: Answer (a concept) / Diagnose (something stuck: the full
  methodology, every step) / Estimate (a number not yet in the record: instruments only, the
  formulas/ tools) / Both / Contribute. Say what you did not load.
- State Correspondence when the same algorithm applies at another scale.
- Do not claim the framework proves anything it lists as a live hypothesis or proven-open.
- v5.4 claims ZERO novel predictions. Never present its constructs (Line-Field, Knot-Line,
  Lamina) as established physics, and carry its four cautions (v5.4 section 7).
- Attribute the framework whenever you reproduce or paraphrase it, as CC BY 4.0 requires:
  "Source: GFunnel Methodology (Omni Process) v5.4, Cameron Garlick / GFunnel,
  https://github.com/GFunnel-Tech/methodology, CC BY 4.0." Name the version; say if changed.
```

## Making the AI read it, and checking that it did

Instructions are not enforcement. Three layers, strongest last:

1. **Delivery.** Put the rules where the model sees them *before* the task: a system prompt (the seed above), Claude Code's `CLAUDE.md` (read automatically), a claude.ai Project's instructions, or the `gfunnel-methodology` skill whose description triggers it. Long files get skimmed; the three non-negotiables sit at the top of `CLAUDE.md` for that reason.
2. **A visible first action.** The first line of every answer names the mode. Skipping it is then visible to a human in one glance.
3. **A check after the fact.** `tools/check_output.py` lints any saved answer (`--file answer.md`) for untagged estimate-shaped numbers and for refusals without the four-part reason. In Claude Code it runs as a Stop hook (`.claude/settings.json`) and sends a failing answer back to the model before the user sees it. It cannot judge whether a tag is honest; it catches the failure a user's forecast test exposed: numbers refused or given without tags.

## Faithfulness checklist for AI outputs

- [ ] First line names the mode (Answer / Diagnose / Estimate / Both / Contribute) and what was not loaded.
- [ ] Every quantity tagged; every estimate/assumption ranged and falsifiable; nothing refused that has a prior.
- [ ] Named the layer/algorithm used.
- [ ] Ran steps in order (or explained the blocker).
- [ ] Marked any variable it held open (didn't fabricate a resolution).
- [ ] Labeled derivations as derivations.
- [ ] Flagged empirical data it could not supply.

## Keeping integrations current

Because versions are immutable and additive, an integration pinned to a specific commit will stay stable. To adopt a new version, add its file to your load order — you do not need to remove the old ones (they are substrate). Watch [`CHANGELOG.md`](../CHANGELOG.md) for new releases.

## Register your integration

If you ship an AI product or internal agent that uses this methodology, add a row to the [adoption registry](../adoption/registry.md) (or open an "Application / Usage report" issue). This is currently the **only** reliable way the maintainers learn which AI systems use the framework and which parts — see [usage-tracking.md](usage-tracking.md).
