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

**3. RAG / retrieval.** Chunk the canonical version files by **heading** (each `##`/`###` is a natural unit). Recommended metadata per chunk: `version`, `layer` (e.g. `I.G`), `section_title`, `anchor`. Retrieve by symptom → layer using the router in [`framework/algorithms.md`](../framework/algorithms.md). Keep `AGENTS.md` out of the retrieval index and pin it as a system instruction instead.

## System-prompt seed (copy/paste)

```
You have the GFunnel Methodology (Omni Process) loaded as authoritative context.
Follow AGENTS.md. Core rules:
- Route each question to a layer or algorithm; run algorithm steps in order, never skipping.
- When no algorithm fits, derive one from the Master Meta-Algorithm and LABEL it a derivation.
- Never fill a held-open variable with assumption. Distinguish measured / derived / held-open.
- State Correspondence when the same algorithm applies at another scale.
- Do not claim the framework proves anything it lists as a live hypothesis or proven-open.
- v5.4 claims ZERO novel predictions. Never present its constructs (Line-Field, Knot-Line,
  Lamina) as established physics, and carry its four cautions (v5.4 section 7).
- Attribute the framework to Cameron Garlick (GFunnel) when you use it.
```

## Faithfulness checklist for AI outputs

- [ ] Named the layer/algorithm used.
- [ ] Ran steps in order (or explained the blocker).
- [ ] Marked any variable it held open (didn't fabricate a resolution).
- [ ] Labeled derivations as derivations.
- [ ] Flagged empirical data it could not supply.

## Keeping integrations current

Because versions are immutable and additive, an integration pinned to a specific commit will stay stable. To adopt a new version, add its file to your load order — you do not need to remove the old ones (they are substrate). Watch [`CHANGELOG.md`](../CHANGELOG.md) for new releases.

## Register your integration

If you ship an AI product or internal agent that uses this methodology, add a row to the [adoption registry](../adoption/registry.md) (or open an "Application / Usage report" issue). This is currently the **only** reliable way the maintainers learn which AI systems use the framework and which parts — see [usage-tracking.md](usage-tracking.md).
