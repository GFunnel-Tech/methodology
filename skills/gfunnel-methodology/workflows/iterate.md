# Workflow — Contribute an Iteration

Use for: proposing a new version, narrowing or opening a variable, reporting evidence, running a v5.4 §14 test, fixing a transcription, opening an issue or PR against `GFunnel-Tech/methodology`.

Read `CONTRIBUTING.md` in full first. It is the governing text; this workflow is its checklist.

## The one rule

**The base code does not change.** A valid iteration narrows a held-open variable, holds it open honestly, or opens a new one. Nothing established is lost. A change that rewrites the base spine is not an iteration.

## Steps

1. **Load substrate.** Read the current version per `versions/LATEST.md` (v5.1 → v5.4 in order, via `SECTIONS.md`), then `framework/registers.md` (note its numbering offset against v5.4's ledger), `framework/gaps.md` and `framework/tests/README.md`.
2. **Classify the contribution.** Pick one:

   | Kind | Issue template (`.github/ISSUE_TEMPLATE/`) |
   | --- | --- |
   | New version or variable movement | `iteration-proposal.yml` |
   | Evidence bearing on a held-open variable | `variable-evidence.yml` |
   | A §14 test executed | `variable-evidence.yml` + a file and a stdlib-only script in `framework/tests/` |
   | Canonical file diverges from the authored original | `transcription-fix.yml` |
   | "We use it" report | `application-report.yml` |

3. **Run the Forcing Test** (v5.3 §1 is the worked example) on each movement: **A Ground** (within-system?) → **B Uniqueness** (does exactly one candidate survive?) → **C Direction** → **D Falsifiability** (name what would prove it wrong). Assign the outcome class: *forced-fill*, *live hypothesis* (attach the falsifier), *stipulation*, or *proven-open*. Then run the **Anti-Operation**: name the gap this fill opens.
4. **Open the issue first**, filling the template honestly. If you cannot open issues (no GitHub access), write the issue body to a file and tell the user.
5. **Write the change, following the file rules:**
   - **Never edit a released file in `versions/`** except a transcription fix that brings it closer to the authored original (log it in `CHANGELOG.md`).
   - A refinement is a **new** directory `versions/vX.Y/` that loads prior versions as substrate. Declaring a version is the maintainer's decision, so mark a draft as awaiting author declaration.
   - Test runs go in `framework/tests/` with a reproducible Python script (standard library only), the numbers, and an honest verdict, including when the verdict is less favourable than the canon's wording.
   - If you rename a canonical heading, update the anchors in `framework/*.md` in the same change, and regenerate the skill index: `python3 tools/build_skill.py --index-only`.
6. **Log the movement**: a row in the Iteration Ledger in `framework/registers.md` **and** in the new version's own ledger (what narrowed, what stayed open, what newly opened, confirmation the base code is unchanged); a `CHANGELOG.md` entry.
7. **Open the PR** using `.github/PULL_REQUEST_TEMPLATE.md`. Fill every honesty-checklist box; note any that is only partial.

## Honesty checklist (must all hold)

- Loads the current version as substrate; nothing prior lost or silently overwritten.
- Each movement classified (forced-fill / live hypothesis / stipulation / proven-open).
- No held-open variable filled with assumption.
- Nothing claimed beyond what is forced (no promoting a live hypothesis to a law).
- Iteration Ledger and `CHANGELOG.md` updated.
- Base code unchanged, or an architectural addition logged explicitly as a departure (as v5.3 did with ⊙).

## Governance

Anyone, human or AI, may propose; acceptance is the maintainer's decision (Cameron Garlick / GFunnel). Contributions are licensed CC BY 4.0. Do not paste material you do not hold rights to; cite quoted sources and their licenses.
