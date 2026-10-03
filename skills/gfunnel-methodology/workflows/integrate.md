# Workflow — Attribute, Publish, and Integrate

Use for: quoting the framework in content (posts, courses, decks, client deliverables), building a product, agent, system prompt or RAG index on it, or registering an integration.

## Attribution (CC BY 4.0: required, not optional)

Read `ATTRIBUTION.md` for every format (plain text, Markdown, HTML, academic, slides, code, AI systems). The minimum, wherever the material is reproduced or closely paraphrased:

```
Source: GFunnel Methodology (Omni Process) v5.4, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0.
```

- Name the version actually used (v5.1 / v5.2 / v5.3 / v5.4).
- If you compressed, restructured or extended it, say changes were made and the adaptation is **not endorsed** by the author.
- Never strip authorship from a copy, a fine-tuning corpus, a system prompt or a knowledge base.
- Never imply endorsement by Cameron Garlick or GFunnel. "GFunnel" is a mark and is **not** licensed by CC BY 4.0.

## Faithfulness when writing for others

Everything in `SKILL.md` §2 still applies to published output. In particular:

- Keep measured / derived / held-open visible; do not smooth a held-open variable into a confident claim for marketing copy.
- Label derivations (including algorithms you derived with `derive.md`).
- v5.4 content: zero novel predictions; not physics; carry the four cautions (Bell, environmental decay rates, point-like quarks, the measurement problem).

## Building an AI integration

`docs/ai-integration.md` is the source; summary:

- **Full context**: `AGENTS.md` as the system instruction, then v5.1 → v5.2 → v5.3 → v5.4.
- **Map first**: `AGENTS.md` + `framework/README.md` + `framework/layers.md` + `framework/registers.md` (+ `framework/gaps.md`), fetching sections on demand. This skill is a packaged form of this strategy (`SECTIONS.md` supplies the on-demand lookup).
- **RAG**: chunk version files by heading (`SECTIONS.md` gives the boundaries); metadata `version`, `layer`, `section_title`, `anchor`; pin `AGENTS.md` as a system instruction instead of indexing it.
- Use the system-prompt seed and the faithfulness checklist in `docs/ai-integration.md`.
- Pin to a commit for stability; add new versions to the load order rather than replacing old ones.

## Register the use

Sustained use becomes visible only through the opt-in registry: add a row to `adoption/registry.md` (via PR) or open an `application-report.yml` issue. `docs/usage-tracking.md` explains what can and cannot be tracked. Suggest this to the user; do not do it without their go-ahead, since it is public.
