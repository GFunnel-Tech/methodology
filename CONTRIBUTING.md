# Contributing — The Iteration Protocol

The GFunnel Methodology grows by **iteration**, under its own Document Update Protocol (Layer I.G — the Capsule). This file translates that protocol into a GitHub workflow. Contributions here are not ordinary "edits" — they are **iterations that load the current version as substrate.**

## The one rule

> **The base code does not change.** A valid iteration **narrows a held-open variable, holds it open honestly, or opens a new one** (per Gödel: resolutions create new questions). No variable is filled with assumption to sound complete. Nothing already established is lost.

If your proposed change rewrites the base spine rather than operating *on* it, it is out of scope — propose it as a separate discussion, not an iteration.

## What counts as an iteration

- **Narrowing** a variable the framework currently holds open (with the *structure* that narrows it — evidence, derivation, or logical necessity).
- **Recognizing** two open variables as one, or re-tiering a mis-filed structure (as v5.3 did with Layer ◇).
- **Opening** a new, honestly-named variable that a resolution created.
- **Running a test** the framework already named (e.g. a v5.4 §14 item) and logging the result — pass *or* fail. Executed runs live in [`framework/tests/`](framework/tests/README.md) with a reproducible script; they are **variable evidence**, not a version. Declaring a version from them is the maintainer's call.
- **Adding architecture** (rare, as in v5.3) — must be *recognized, not invented*, and logged explicitly as a departure.

## The workflow

1. **Open an issue first**, using the right template ([`.github/ISSUE_TEMPLATE`](.github/ISSUE_TEMPLATE)):
   - *Iteration proposal* — you want to propose a new version or a variable movement.
   - *Variable evidence* — you have evidence bearing on a held-open variable.
   - *Application / Usage report* — you used the framework and want to report how (also a usage signal).
   - *Transcription fix* — a canonical file diverges from the authored original.
2. **Discuss and classify.** Use the Forcing Test outcome classes from [`framework/registers.md`](framework/registers.md): forced-fill · live hypothesis · stipulation · proven-open. Be honest about which one applies.
3. **Do not edit released version files.** Versions in [`versions/`](versions/README.md) are immutable. A refinement becomes a **new** version directory (`vX.Y/`), which loads the prior as substrate. (The only edits to a released file are transcription fixes that bring it *closer* to the authored original — logged in `CHANGELOG.md`.)
4. **Log the movement.** Add a row to the Iteration Ledger in [`framework/registers.md`](framework/registers.md) **and** the new version's own ledger: what narrowed, what stayed open, what newly opened, and confirmation the base code didn't change.
5. **Open a pull request** referencing the issue. Fill in the PR template — especially the honesty checklist.

## Honesty checklist (every iteration PR must pass)

- [ ] Loads the current version as substrate; nothing prior is lost or silently overwritten.
- [ ] Classifies each movement (forced-fill / live hypothesis / stipulation / proven-open).
- [ ] Does **not** fill a held-open variable with assumption.
- [ ] Does **not** claim more than is forced (no promoting a live hypothesis to a law).
- [ ] Updates the Iteration Ledger and `CHANGELOG.md`.
- [ ] Confirms the base code is unchanged (or, for a rare architectural addition, logs it explicitly as a departure that operates *on* the base).

## Style & transcription

- Keep the canonical documents faithful to the authored source. Preserve heading hierarchy, tables, and section order.
- Prose iterations follow the framework's own register: name the mechanism, run its structure, place it, hold variables open honestly.
- Deep links: if you rename a heading in a canonical file, update the anchors in `framework/*.md` in the same change.

## Licensing of contributions

This repository is published under **[CC BY 4.0](LICENSE)**. By opening a pull request or an issue proposing text, you agree that your contribution is licensed under the same terms — free for anyone to share and adapt, with credit — and you confirm you have the right to license it that way.

Contributors are credited in the git history, in the accepting version's Iteration Ledger, and, for substantive iterations, in the version document itself. Submitting an iteration does not transfer your copyright; it licenses it under CC BY 4.0 alongside the rest of the work.

Do not paste in material you do not hold the rights to. If you quote another source, cite it inline and name its license — the Variable Principle applies to provenance too: do not fill an unknown source with assumption.

## Governance

Final authority on what enters the canon rests with the author/maintainer (**Cameron Garlick / GFunnel**). Anyone — human or AI — may propose; acceptance is a maintainer decision. See [`AGENTS.md`](AGENTS.md) for the AI-contributor protocol.
