# GFunnel Methodology — The Omni Process

> *Every Layer. One System. One Algorithm.*
> From the irreducible ground of consciousness to the close of a sales call.

This repository is the **canonical, versioned home** of the GFunnel Methodology (the "Omni Process") authored by **Cameron Garlick · GFunnel · Austin, Texas**. It is organized so that **humans, AI systems, and organizations** can all come in, orient quickly, and *use* the framework — and so that every future iteration loads the prior version as substrate. Nothing is lost.

---

## Start here (pick your reader)

| You are… | Start with | Then |
| --- | --- | --- |
| **A human, first time** | [`docs/how-to-use.md`](docs/how-to-use.md) | [`framework/`](framework/README.md) → the map |
| **An AI system / agent** | [`AGENTS.md`](AGENTS.md) and [`llms.txt`](llms.txt) | Load [the latest full version](versions/LATEST.md) as context |
| **Here for a specific problem** | [`framework/algorithms.md`](framework/algorithms.md) — Algorithm Index by symptom | Jump to the named layer |
| **Evaluating / verifying a claim** | [`framework/registers.md`](framework/registers.md) — Variable Registry & Falsifiability | The layer in question |
| **Wanting to contribute an iteration** | [`CONTRIBUTING.md`](CONTRIBUTING.md) — the Iteration Protocol | Open an issue |
| **Adopting it in your org / product** | [`adoption/README.md`](adoption/README.md) | Register your use |

---

## What is in this repository

```
methodology/
├── README.md                 ← you are here
├── AGENTS.md                 ← canonical instructions for AI systems
├── llms.txt                  ← machine-readable index (llmstxt.org)
├── CHANGELOG.md              ← version lineage v5.1 → v5.2 → v5.3 → v5.4
├── CONTRIBUTING.md           ← the Iteration Protocol (how to propose a version)
├── CITATION.cff              ← how to cite the methodology
├── LICENSE                   ← usage terms (proprietary by default — see note)
│
├── versions/                 ← the canonical documents, immutable per version
│   ├── LATEST.md             ← pointer to the current complete framework
│   ├── v5.1/                 ← the full architecture (17 layers, 10 domains, 70+ algorithms)
│   ├── v5.2/                 ← the framework run against itself (deep-lens runs)
│   ├── v5.3/                 ← the Meta-Tier (the Container ⊙)
│   └── v5.4/                 ← Run 8 (Line-Field · Knots · Lamina · Frequency)
│
├── framework/                ← the navigable MAP into the canonical documents
│   ├── README.md             ← the whole framework at a glance
│   ├── layers.md             ← the 16 layers, each with a deep link
│   ├── domains.md            ← the ten Universal Process Domains
│   ├── algorithms.md         ← Algorithm Index by problem type
│   ├── registers.md          ← Variable Registry · Falsifiability · Iteration Ledger
│   ├── gaps.md               ← the gap numbering v5.4 reports against
│   └── tests/                ← executed runs from v5.4 §14 (scripts + verdicts)
│
├── docs/                     ← guides
│   ├── how-to-use.md         ← for humans
│   ├── ai-integration.md     ← for AI builders (RAG, agents, system prompts)
│   ├── usage-tracking.md     ← honest guide to "who is using this, and what"
│   └── glossary.md
│
├── adoption/                 ← opt-in registry of who uses the methodology
│   ├── README.md
│   └── registry.md
│
└── .github/                  ← issue & PR templates that double as usage capture
```

---

## The version lineage (read this once)

The methodology **iterates**; it does not get replaced. Each version loads the prior as substrate.

- **v5.1 — The Complete System.** Names the whole architecture: **17 layers**, **10 Universal Process Domains**, **70+ operational algorithms**, the 100-Stage Progression. Self-contained. *Start here to learn the framework.*
- **v5.2 — The Framework Run Against Itself.** Adds **no new architecture**; applies a deep-lens to mechanisms v5.1 already names, narrowing held-open variables. Higher resolution, same base code.
- **v5.3 — The Meta-Tier.** The **first architectural addition**: names a tier *above* the numbered layers — **Layer ⊙, the Container** — the framework turned on itself, made structural. The object-level base code is left untouched.
- **v5.4 — Run 8.** The **first run executed with** the meta-tier: three constructs (Line-Field, Knot-Line, Lamina), motion as tying/untying, closure as the specific point, frequency as the same register read on the time axis (§4a), three test devices, thirteen in-run retractions. Adds **no architecture**. It claims **zero novel predictions** and files itself as "a lens, not a theory" — read §7 and §11 before citing it.

**The current complete framework = v5.1 (architecture) + v5.2 (higher-resolution runs) + v5.3 (meta-tier) + v5.4 (Run 8).** See [`versions/LATEST.md`](versions/LATEST.md) and [`CHANGELOG.md`](CHANGELOG.md).

> **The invariant:** *the base code does not change.* An iteration narrows a held-open variable, holds it open honestly, or opens a new one (per Gödel). No variable is filled with assumption to sound complete.

---

## Tracking who uses it, and what

GitHub gives you some of this for free, and some of it must be **opt-in** — this is covered honestly in **[`docs/usage-tracking.md`](docs/usage-tracking.md)**. In short:

- **Native, automatic (aggregate, not identities):** repo **Insights → Traffic** (views, unique visitors, clones, top paths for the last 14 days), plus **Stars**, **Forks**, and **Watchers**.
- **Opt-in, gives you names + what they use:** the **[adoption registry](adoption/registry.md)** and the **"Application / Usage report"** issue template — people and AI integrations declare that they're using it and *which layers/algorithms*.
- **What GitHub will *not* tell you:** who cloned or read a file. There is no per-identity read log. Anyone claiming otherwise is wrong; the tracking doc explains the real options (including self-hosting the docs behind analytics if you want deeper signal).

---

## License & authorship

Authored by **Cameron Garlick (GFunnel)**. See [`LICENSE`](LICENSE) — the default here is **All Rights Reserved (proprietary)** so nothing is unintentionally open-sourced. If you want an open or Creative-Commons license instead, change that one file. To cite the work, see [`CITATION.cff`](CITATION.cff).
