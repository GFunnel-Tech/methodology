# The Methodology as an Agent Skill

[`gfunnel-methodology/`](gfunnel-methodology/SKILL.md) packages this **entire repository** as an [Agent Skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): Claude loads it automatically when a request touches the framework, follows the canon's own AI protocol, and reads only the sections it needs.

> **Status:** navigation / tooling. The skill restates the operating protocol from [`AGENTS.md`](../AGENTS.md) and routes into the canon; it adds no framework content and changes no version.

## How it is built

The skill loads in three stages, so a 390 KB corpus costs almost nothing until it is used:

| Level | File | Loaded |
| --- | --- | --- |
| 1 | `SKILL.md` front matter (name + description) | Always: this is how Claude knows the skill exists and when to use it |
| 2 | `SKILL.md` body: the eight rules, the prohibitions, the workflow router, the corpus map, the credit line | When the skill triggers |
| 3 | `workflows/*.md` (answer · run-algorithm · derive · iterate · reality-audit · integrate) | The one workflow the task needs |
| 3 | `SECTIONS.md`: every heading in v5.1–v5.4, `TASK.md`, `SCHEMA.md`, `registers.md` with its **line range** | To jump into one section (e.g. a single algorithm) instead of loading 80k tokens of v5.1 |
| 3 | The corpus: every file in this repo | Section by section, on demand |

**One source, no duplicated canon.** Inside this repo the corpus *is* the repo. For places that cannot see the repo, [`tools/build_skill.py`](../tools/build_skill.py) copies every tracked file into `corpus/` in a bundle. Released versions are immutable, so the line numbers in `SECTIONS.md` do not drift; the script regenerates them if a heading ever changes.

## Install it

### Claude Code, working in this repository: nothing to do

[`.claude/skills/gfunnel-methodology/SKILL.md`](../.claude/skills/gfunnel-methodology/SKILL.md) registers the skill for every Claude Code session opened in a clone (local, desktop, web). Check with `/skills`.

### Claude Code, in any other project: install as a plugin

This repository is also a plugin marketplace ([`.claude-plugin/`](../.claude-plugin/marketplace.json)):

```
/plugin marketplace add GFunnel-Tech/methodology
/plugin install gfunnel-methodology@gfunnel
```

The plugin carries the whole repository, so the skill reads the canon directly. (The repository must be readable by the installing account.)

Alternatively, copy the built bundle into a project or your user skills folder:

```bash
python3 tools/build_skill.py
cp -r dist/gfunnel-methodology ~/.claude/skills/            # all projects
# or: cp -r dist/gfunnel-methodology <project>/.claude/skills/
```

### claude.ai (web, desktop, mobile)

```bash
python3 tools/build_skill.py        # → dist/gfunnel-methodology.zip (~275 KB; limit 30 MB)
```

Upload `dist/gfunnel-methodology.zip` under **Settings → Capabilities → Skills → Upload skill** (code execution must be enabled). On Team/Enterprise plans an owner can provision it for the whole organization.

### Claude API / Agent SDK

Upload the folder `dist/gfunnel-methodology/` through the Skills API (`POST /v1/skills`, every file with its relative path) and attach the returned `skill_id` in the `container.skills` of a Messages request with the code-execution tool. For the Agent SDK, place the folder in the project's `.claude/skills/`.

### Other agents (Codex, Cursor, Gemini CLI, custom)

Most read [`AGENTS.md`](../AGENTS.md) automatically. To give them the skill's workflows too, point them at `skills/gfunnel-methodology/SKILL.md`, or add the built bundle to their knowledge/context folder. The format is the open Agent Skills layout (a folder with `SKILL.md` + resources).

## Maintain it

```bash
python3 tools/build_skill.py --check        # stale index? malformed front matter? broken path? → exit 1
python3 tools/build_skill.py --index-only   # regenerate SECTIONS.md after a heading change
python3 tools/build_skill.py                # regenerate + build dist/ (git-ignored)
```

Run `--check` in any PR that touches `versions/`, `framework/registers.md`, `audit/SCHEMA.md`, `tasks/reality-audit/TASK.md`, or the skill itself. When a new version (v5.5, …) is released, add it to `INDEXED` in `tools/build_skill.py` and to the corpus map and load order in `SKILL.md`, then bump `version` in `.claude-plugin/plugin.json`.

## Attribution

A bundle built from this repository contains the full CC BY 4.0 text with its `LICENSE`, `ATTRIBUTION.md` and `CITATION.cff`; keep them when you redistribute it. The skill itself instructs Claude to attach the credit line whenever it reproduces or closely paraphrases the material. Using the skill does not imply endorsement by Cameron Garlick or GFunnel.
