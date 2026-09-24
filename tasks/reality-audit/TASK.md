# TASK — The Reality Audit & The Container System

**Repository:** `GFunnel-Tech/methodology` (the algorium)
**Substrate:** v5.1 + v5.2 + v5.3 + v5.4 (load in that order, per `versions/LATEST.md`)
**Author / maintainer:** Cameron Garlick (Cam)
**Executor:** Claude Code
**Time constraint:** none. Use as many PRs as the work needs. Correctness over speed.

> Commit this file to the repo in PR 1 at `tasks/reality-audit/TASK.md`. It is the standing brief for every phase below.

---

## 0. Read this first

Before any edit, read in full:

1. `AGENTS.md`: the operating protocol. Every rule there still applies unless this task explicitly scopes it (see §2).
2. `CONTRIBUTING.md`: the Iteration Protocol. Every PR follows it.
3. `framework/registers.md`: the Variable Principle, outcome classes, and Iteration Ledger (note its numbering offset).
4. `framework/gaps.md`, `framework/tests/README.md`.
5. `versions/v5.1/GFunnel-Methodology-v5.1.md`, especially the Master Meta-Algorithm, the Scientific Inquiry Algorithm, Appendix A (100-Stage Unified Progression), and Appendix D (Fundamental Constants & Laws Registry).
6. `versions/v5.3/…`: the Container ⊙, the Forcing Test, and the Anti-Operation.
7. `versions/v5.4/…`: especially §5 (Big Bang ruling: *event false, phase forced*), §11, §12, §13, §14.

**Do not improvise.** This task uses the methodology's own machinery. Where it needs something the methodology does not name, it states that the item is a **derivation** and labels it as one (AGENTS.md rules 4 and 7).

---

## 1. Purpose

Compare the **two logs** and let reality do the filtering:

| Log | What it is | Where it lives |
| --- | --- | --- |
| **Reality (implicit log)** | Reality records itself in its own structure: element abundances record stellar history, DNA records survival, strata record time. We never hold reality directly. We hold reproducible observations of it. | `audit/`: observation entries with measurement sources |
| **The methodology (explicit log)** | The ever-growing written record of what is known. | `versions/`, `framework/` |

For every stage, constant, domain, and label in the methodology, determine whether reality supports it. For every observation reality shows that the methodology does not hold, diagnose **why** before classifying it. Every item that is solved or gained leaves behind a **container**: an open-ended reference point with an algorithm or equation, so no one has to re-study it from zero.

---

## 2. Governing model (decided by the author; record it as substrate)

These conclusions were reached with the author on 2026-09-24. They are the substrate for this task. Write them into `substrate/2026-09-24-reality-filter.md` (PR 1) as a **substrate document, not canon**.

1. **Reality is the authority. The methodology adapts.** When observation differs from what the methodology predicts, the methodology changes. Reality does not.
2. **The methodology is the ever-growing log of the known.** It forms to reality the way surface tension forms to a liquid. The boundary is made by the substance itself, never forced onto it, and it adapts continuously as the substance grows. It grows without bound. Completeness is a direction, not a state.
3. **Concentration discipline (molarity).** The log must not claim more than its content supports (a thin film bursts), and it must not hold content it has not integrated (pressure builds). Growth keeps the ratio intact.
4. **No outside models imported.** External theories are not brought in as structure. They can be *discovered* through the process. If they are real, the audit will reach their observations. Names and narratives are interpretations and survive only if reality forces them. **Observations stay, narratives go.**
5. **Reference points, filtered.** External material may be used only as a source of *measurements*. Strip the interpretation and keep the measured quantity.
6. **Every solved or gained item becomes a container**, open-ended, with an algorithm or an equation. Each container is the fast starting point for future work.
7. **The base-code rule is scoped.** "The base code does not change" is now **"The base code holds until reality contradicts it."** This is a governance departure and must be logged as one (see Phase 1).
8. **Weak observations cannot force change.** The Variable Principle applies to the reality log exactly as it applies to claims. An unreproduced observation goes to *Open*. It cannot adjust the methodology.

---

## 3. Hard rules for the executor

1. **Never edit released files in `versions/`.** Only transcription fixes are permitted there, and only per CONTRIBUTING.md. All corrections go into a new `versions/v5.5/` draft.
2. **Never fill a held-open variable with assumption.** If the answer is unknown, the status is *held open*.
3. **Never promote.** A live hypothesis stays live. A stipulation stays a stipulation.
4. **Names come from observation.** Where a methodology label carries narrative that reality does not force, propose an observation-based name. Keep the old name in the lineage (nothing is lost).
5. **Every observation cites a measurement source** (§5.2) and states the measured quantity, its uncertainty, and its reproducibility grade. Do not use interpretive wording in the observation field.
6. **Every container carries at least one open edge.** A container with no open edge is invalid (Anti-Operation: every fill opens a conjugate gap).
7. **Never invent an equation.** An equation enters a container only if it is measured or derived with a shown trace. Otherwise write an algorithm (numbered steps) or mark the form *held open*.
8. **Run algorithms literally** (invariant run form): steps in order, no skipping. **If a step cannot be completed, stop, and log the blocker.** The blocker is the location of the work.
9. **Label derivations.** Anything this task creates that canon does not name (the audit schema, the container unit, the exclusion diagnosis) is labeled a derivation until the author declares it into a version.
10. **Versions are the author's call.** Prepare `v5.5` as a **draft** in a PR marked `awaiting author declaration`. Do not merge it as released.
11. **Attribution.** Outputs that reproduce canon carry the CC BY 4.0 credit line from `ATTRIBUTION.md`.
12. **Honesty checklist.** Every PR fills the PR template's honesty checklist completely.

---

## 4. The instruments (all derived from canon)

| Need | Canonical instrument | Where |
| --- | --- | --- |
| Run the whole task | **Master Meta-Algorithm** (12 steps) | v5.1 |
| Test each item against reality | **Scientific Inquiry Algorithm** (10 steps) | v5.1 |
| Classify each result | **Forcing Test**: Tests A (Ground), B (Uniqueness), C (Direction), D (Falsifiability) → outcome class | v5.3 |
| Name the gap each fill opens | **Anti-Operation** | v5.3 |
| Status of every claim and observation | **Variable Principle**: measured / structurally derived / held open | v5.1, registers.md |
| Record every movement | **Iteration Ledger** + CHANGELOG | registers.md |
| Integrate failures | **Capsule (I.G)**: nothing is lost | v5.1 |
| Intake of observation | **Observation Principle (I.F)** | v5.1 |
| The category list (reference skeleton) | **Appendix A** (Stages 1–100), **Appendix D** (Constants & Laws), **I.C** (Ten Domains) | v5.1 |

### 4.1 The task, run through the Master Meta-Algorithm

Record this run in `audit/README.md` as the governing run.

1. **Domain:** reconciliation of the explicit log (the algorium) against the implicit log (reality).
2. **Kingdom:** Second (the framework), executed into First (repository commits).
3. **Current state:** v5.4 canon; Appendices A–D; the gap register; `tests/`; the session substrate (§2), not yet committed.
4. **Desired state:** every stage, constant, domain, and label carries a reality status. Every observation that is unmapped is diagnosed. Every solved item has a container. Session conclusions enter canon via a v5.5 draft.
5. **Dynamic middle:** the Yang extreme is rewriting canon; the Yin extreme is leaving everything as notes. The middle is substrate → audit → containers → v5.5 draft.
6. **Violated principle:** Correspondence. Structures were being built beside canon instead of corresponding to it. Correction: every audit file maps to a canonical item.
7. **Gradient:** the difference between the two logs. The audit output *is* the gradient.
8. **Cause:** run the Scientific Inquiry Algorithm on every item against observation.
9. **Structure:** intent (reality is the authority) → organization (schemas, files) → execution (commits and PRs). Do not skip the organization step.
10. **Run** the phases below.
11. **Document** every run: audit files, containers, ledger rows, CHANGELOG.
12. **Restart at higher baseline** (Phase 9).

---

## 5. Vocabularies and schemas

### 5.1 Status vocabularies (use these exact terms)

**Observation grade** (reality log):
- `measured-reproduced`: independently reproduced measurement.
- `measured-single`: measured, not independently reproduced.
- `derived`: inferred from measurements by explicit derivation.
- `held-open`: no measurement possible or available.

**Claim outcome** (methodology log, from the Forcing Test):
- `forced-fill` · `live-hypothesis` · `stipulation` · `proven-open` · `forced-no`

**Diff state** (the comparison):

| Reality | Methodology | Diff state | Consequence |
| --- | --- | --- | --- |
| has it | has it, consistent | `accounted` | Candidate for a container |
| has it | lacks it | `methodology-gap` | Methodology adapts (after diagnosis) |
| lacks it | has it | `unobserved-claim` | Held open until reality shows it |
| has it | contradicts it | `conflict` | Reality wins; methodology adapts |
| has it | no stage or domain to hold it | `unmapped` | Diagnose; may reveal a missing stage |

**Exclusion diagnosis** (required *before* classifying any `methodology-gap`, `conflict`, or `unmapped` item):
- `not-reached`: the log has not grown to this point.
- `reached-conflicting`: it contradicts an existing entry.
- `unverified`: the observation is not reproduced.
- `beyond-depth`: the log cannot hold it yet without overreaching (molarity).

**Intake result:**
- `integrated`: it fits as it is.
- `adjusted`: it is real but conflicts, so the methodology re-forms around it. Record the adjustment and the reason.
- `open`: unresolved. It is held at the edge, never forced. **It must carry a `review_after` date.** Open must not decay into ignored.

### 5.2 Permitted measurement sources (reference points only)

Use primary measurement databases and the peer-reviewed measurement papers they cite. Take the **number and its uncertainty**, never the source's narrative. Examples: CODATA/NIST (constants), PDG (particle data), Planck/COBE/WMAP data releases (background radiation measurements), primordial abundance measurements, NIST chemistry and spectral data, genome databases (sequence data), geological dating datasets.

Every observation records: `quantity`, `value`, `uncertainty`, `source` (with a stable URL or DOI), `grade`, and `retrieved` (date). If a value cannot be verified from a primary source, grade it `held-open` and say why.

Scripts that compute or check values follow the `framework/tests/` convention: Python standard library only, constants declared at the top, reproducible.

### 5.3 Audit record schema

One Markdown file per audited item. YAML front matter, then body.

```markdown
---
id: STAGE-005            # STAGE-###, CONST-<slug>, DOMAIN-##, LABEL-###, UNMAPPED-####
canon_ref: v5.1 Appendix A, Stage 5
canon_label: "Big Bang Nucleosynthesis"
proposed_label: "Primordial Light-Element Formation"   # only if the label carries unforced narrative
diff_state: accounted     # §5.1
exclusion_diagnosis: n/a  # required for methodology-gap / conflict / unmapped
claim_outcome: forced-fill   # for the methodology's claim here
intake_result: adjusted   # integrated / adjusted / open
review_after: null        # required if intake_result = open
container: KC-0003        # link if one was created
ledger_row: null          # filled when logged
---

## Canon says
(quote or closely paraphrase canon, with location)

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |

## Scientific Inquiry run
1. Question (precise):
2. What an answer must look like:
3. Falsifiability condition:
4. Variables: measurable / bounded / held open:
5. Test designed:
6. Data (unfiltered):
7. Variable Principle applied:
8. Model update (Capsule: what the failed parts contribute):
9. Documented:
10. Next baseline:

## Forcing Test
- Test A (Ground):
- Test B (Uniqueness):
- Test C (Direction):
- Test D (Falsifiability):
- **Outcome:**

## Anti-Operation (the gap this opens)

## Narrative stripped (if any)
(what interpretation was removed and why reality does not force it)
```

### 5.4 Container schema (derivation: the container unit)

Containers live in `containers/`, one file each, IDs `KC-####`. The prefix **KC** ("knowledge container") keeps them distinct from Layer ⊙ (the Container meta-tier). Their relationship is audited in Phase 1.

```markdown
---
id: KC-0001
name: "<named by the observation, not the narrative>"
status: forced-fill        # forced-fill / live-hypothesis / stipulation / proven-open
form: equation             # equation / algorithm / both / held-open
canon_refs: [v5.4 §5, v5.1 Appendix A Stage 6]
audit_refs: [STAGE-006]
links_up: [KC-00xx]        # Correspondence: one scale up
links_down: [KC-00yy]      # Correspondence: one scale down
created: 2026-09-24
last_reformed: 2026-09-24
---

## Observations
| Quantity | Value | Uncertainty | Grade | Source |

## Form
### Equation (only if measured or derived, with the trace below)
### Algorithm (numbered steps: the fastest route from this reference point)

## Trace
How this was reached, step by step, so it never has to be re-studied.

## Open edge (required, at least one)
The gap this solution opens. This is what keeps the container open-ended.

## Re-formation log
Dated entries each time reality re-shapes this container. Never delete prior entries.
```

**Container rules:**
- Create containers for `forced-fill` items and for `integrated` observations that have a measured equation or a derived algorithm.
- A `live-hypothesis` may have a container only if its status says so plainly and it carries its falsifier. It is never presented as solved.
- Containers are re-formed, not overwritten. When reality changes one, append to its re-formation log.
- `containers/INDEX.md` maps every container to its Stage, Constant, or Domain, and lists it by scale for Correspondence.

---

## 6. Directory layout to create

```
tasks/reality-audit/TASK.md            ← this file
substrate/
  README.md                            ← what substrate is (loaded as input, not canon)
  2026-09-24-reality-filter.md         ← §2 governing model, full
audit/
  README.md                            ← governing Master Meta run (§4.1), how to read the audit
  SCHEMA.md                            ← §5 in full
  FINDINGS.md                          ← running list of confirmed findings (§7)
  COVERAGE.md                          ← coverage map: what's audited, what's sparse, what's blind
  stages/STAGE-001.md … STAGE-100.md
  constants/CONST-<slug>.md
  domains/DOMAIN-01.md … DOMAIN-10.md
  labels/LABEL-###.md                  ← narrative-vs-observation label findings
  unmapped/UNMAPPED-####.md            ← reality observations with no canonical home
  issues/                              ← drafted issue bodies (if `gh` is unavailable)
containers/
  README.md                            ← what a container is; the rules in §5.4
  TEMPLATE.md
  INDEX.md
  KC-0001-<slug>.md …
tools/
  validate_audit.py                    ← stdlib only: checks front matter fields and vocabularies
  validate_containers.py               ← stdlib only: checks required fields, ≥1 open edge, trace present
versions/v5.5/                         ← DRAFT only (Phase 8)
```

---

## 7. Known findings to seed `audit/FINDINGS.md`

These are already confirmed. Seed them in PR 1 and resolve them in the phases shown.

| # | Finding | Evidence | Resolution path |
| --- | --- | --- | --- |
| F-001 | **Stage 5 label "Big Bang Nucleosynthesis"** imports an origin narrative. v5.4 §5 already rules the Big Bang *as an event* forced-false and keeps only the phase and its observations. | v5.1 App. A Stage 5; v5.4 §5 | Keep the observations (light-element abundances). Remove the name. Propose "Primordial Light-Element Formation." Phase 2 → v5.5 re-label. |
| F-002 | **Stage 3 "Symmetry Breaking / Inflation":** inflation is a model with indirect support, filed without a status tag. | v5.1 App. A Stage 3 | Tag `live-hypothesis`. Separate what is observed from what is modeled. Phase 2. |
| F-003 | **The base-code rule conflicts with "reality is the authority."** | CONTRIBUTING.md, AGENTS.md vs. §2.7 | Scope to "holds until reality contradicts it." Log as a governance departure. Phase 1. |
| F-004 | **The Container ⊙ definition vs. the log-as-surface-tension model.** v5.3 files ⊙ as the capstone meta-tier. The session model defines the methodology as a self-forming, ever-growing log. | v5.3; §2.2 | Forcing Test: are these the same structure seen two ways, a refinement, or a conflict? Phase 1. |
| F-005 | **No exclusion-diagnosis step exists.** Canon classifies what is in scope but has no procedure to ask *why* something is missing. | CONTRIBUTING.md; registers.md | Add the diagnosis as a derivation (§5.1). Propose it into v5.5. Phase 1. |
| F-006 | **Implicit log vs. explicit log.** Reality records itself in structure; the methodology is the written copy. This relates to I.F and I.G but is not stated. | §1; v5.1 I.F, I.G | Forcing Test for Correspondence with I.F/I.G. Phase 1. |
| F-007 | **No container unit exists.** Master Meta step 11 ("documented derivation becomes substrate") and v5.4's conjugate-gap rule imply it, but there is no standard form. | v5.1 Master Meta step 11; v5.4 | Create `containers/` as a derivation. Phase 0 (schema), Phase 7 (population). |

Add every new finding as `F-###` with the same columns.

---

## 8. Phases and PR plan

Branch naming: `audit/phase-<n>-<slug>`. One coherent unit per PR. Each PR links an issue (open it with `gh issue create` using the repo's templates; if `gh` is unavailable, write the issue body to `audit/issues/` and note it in the PR). Each PR fills the template's honesty checklist.

### Phase 0: Foundation (PR 1)
**Issue template:** Docs / navigation / tooling.
- Commit this file to `tasks/reality-audit/TASK.md`.
- Create `substrate/` with the §2 model written out in full.
- Create `audit/` skeleton: `README.md` (with the §4.1 run), `SCHEMA.md`, `FINDINGS.md` seeded with §7, `COVERAGE.md` (empty map).
- Create `containers/` skeleton: `README.md`, `TEMPLATE.md`, `INDEX.md`.
- Create `tools/validate_audit.py` and `tools/validate_containers.py` (stdlib only), and document how to run them.
- Link the new areas from `README.md` "Start here" and `llms.txt` as **derivation / work-in-progress**, not canon.
- **No canonical text changes.**

### Phase 1: Governance reconciliation (PRs 2–5, one per finding)
**Issue template:** Iteration proposal. Substrate: v5.4.

For each finding, run the full Forcing Test in an audit file under `audit/labels/` or a dedicated `audit/governance/` file, and log the result.
- **PR 2: F-003, base-code rule.** Classify the scoping ("holds until reality contradicts it") and log it explicitly as a governance departure that operates *on* the base. Draft the replacement wording for CONTRIBUTING.md, AGENTS.md, and the PR template, but apply it only in the v5.5 draft PR. The author has decided this, so record it as **stipulation (operator decision)** unless the Forcing Test forces it outright; say which.
- **PR 3: F-004, Container ⊙ vs. the log model.** Determine: same structure, refinement, or conflict? If it is a refinement, name precisely what v5.5 adds. Carry v5.3's open question ("what is the Container a component of?") and state whether the growing-log model narrows it. Do not claim closure unless forced.
- **PR 4: F-005 and F-006,** the exclusion diagnosis and the implicit/explicit log. Classify each and state its correspondence to I.F / I.G.
- **PR 5: F-007, the container unit.** Classify it and confirm its correspondence to Master Meta step 11 and v5.4's conjugate-gap rule.

Each of these PRs adds a ledger row to `framework/registers.md` (respect the numbering note) marked `☐ queued for v5.5`.

### Phase 2: Label audit (PRs 6–8)
Audit **every** canonical label for narrative that reality does not force: all 100 Stage names, all Domain names, all Appendix D entry names, and all Layer names.
- **PR 6:** Stages 1–49 labels (resolve F-001 and F-002 here).
- **PR 7:** Stages 50–100 labels. Most are projections; note that a label for an unobserved stage can be fine as long as its *status* is honest.
- **PR 8:** Domain, Layer, and Appendix D labels.

Output: `audit/labels/LABEL-###.md` files, each stating the old name, the stripped narrative, the proposed observation-based name (if any), and the reasoning. **Nothing is renamed in canon.** Renames are proposals for v5.5.

### Phase 3: The stage audit (PRs 9–16)
Run the §5.3 audit on every stage, in blocks. Each block is a PR.

| PR | Stages | Expected character |
| --- | --- | --- |
| 9 | 1–4 | Pre-geometric through hadronization. Stage 1 is largely held open (v5.4 Gap 1: the first boundary is proven-open). Distinguish observed from modeled. |
| 10 | 5–10 | Light elements, decoupling, stars, supernovae, planets, prebiotic chemistry. Measurement-rich. |
| 11 | 11–16 | RNA world through fermentation. Mixed: some measured, some live. |
| 12 | 17–24 | Photosynthesis through membrane potentials. Measurement-rich (biochemistry). |
| 13 | 25–35 | Multicellularity through cognition. Measurement-rich (biology, neuroscience). |
| 14 | 36–49 | Self-awareness through cycle restart. Heavy in structurally derived claims; grade honestly. |
| 15 | 50–85 | Projected stages. Expect mostly `unobserved-claim`. **This is not failure;** tag them held open, and note any stage where present-day observation already bears on it (e.g. 50–56). |
| 16 | 86–100 | The variable frontier. Canon holds these open by design. Confirm the status is honest; do not "resolve" any. |

Update `audit/COVERAGE.md` after every block.

### Phase 4: The constants audit (PRs 17+)
Audit Appendix D section by section (one PR per section: mathematical constants, physical constants, laws, and so on).
- Mathematical constants: verify the values; they are substrate-independent. Separate the value (measured or defined) from the "Framework Role" text (interpretation). Grade the role text by the Forcing Test.
- Physical constants: check each value and uncertainty against CODATA/PDG. **Flag any mismatch as `conflict`: reality wins.**
- Laws: state each law in its measured form and grade the framework's interpretive note separately.

### Phase 5: The domain audit (PRs, one per domain or pair)
For each of the ten domains in I.C, test the claim that `DETECT → PROCESS → RESPOND` maps cleanly. Per canon, a domain that resists becomes a **named variable, not a disproof**. Grade the mapping honestly.

### Phase 6: The unmapped sweep (PRs, one per sweep region)
This is where the audit looks for what the methodology does *not* hold.

Use a **neutral detection grid** as the sweep instrument. This grid is a *search tool for the reality side*, not a category system for the methodology:
- **Scale:** subatomic → atomic → molecular → cellular → organism → ecosystem → planetary → stellar → galactic → cosmic
- **Organization:** physical → chemical → biological → mental → social/systemic
- **Time:** instantaneous → seconds → years → geological → cosmic

For each cell, list reproducible observations and ask: *which stage, constant, or domain holds this?* If none does, create `audit/unmapped/UNMAPPED-####.md`, run the **exclusion diagnosis first**, then the full audit. An unmapped observation may reveal a missing stage. Propose it; do not insert it.

The grid itself is a log. When the methodology predicts something the grid does not contain, record that as a gap in the *grid*. The check runs both ways.

### Phase 7: Container population (PRs, batched by scale)
From every `accounted` / `forced-fill` / `integrated` result across Phases 1–6, create containers per §5.4.
- Seed with the items canon has already forced or tested: for example the v5.4 forced rows in the Iteration Ledger (first motion as reflection at a boundary, lines as geodesics at First Kingdom scale, the gravitation sign, frequency = line × node) and the executed tests in `framework/tests/` (Koide δ = 2/9, D1 energy budget). Carry each one's stated caveats and open edges exactly.
- Batch by scale so Correspondence links (`links_up` / `links_down`) can be set within each batch.
- Run `tools/validate_containers.py` in every PR.

### Phase 8: v5.5 draft (1 PR, marked `awaiting author declaration`)
**Issue template:** Iteration proposal. Substrate: v5.1–v5.4 + `substrate/2026-09-24-reality-filter.md` + the full audit.

Create `versions/v5.5/GFunnel-Methodology-v5.5.md` as an **iteration that loads all prior versions as substrate**. It contains:
1. The governing model (§2) as classified by Phase 1, with each item's outcome class.
2. The scoped base-code rule, logged as a departure.
3. The label re-mappings from Phase 2 (old name → new name → reason). Nothing is lost; old names remain in v5.1.
4. Stage, constant, and domain status changes from Phases 3–5.
5. Proposed new stages or domain entries from Phase 6, each with its evidence and status.
6. The container system (§5.4) and the exclusion diagnosis (§5.1), filed as derivations or promoted per their Forcing Test outcome.
7. Its own Iteration Ledger, and an explicit "What v5.5 does not claim" list extending v5.4 §11.

Also in this PR: CHANGELOG entry; `versions/LATEST.md`, `versions/README.md`, `llms.txt`, `AGENTS.md`, `CITATION.cff`, `framework/*.md` navigation updated; the governance wording from PR 2 applied to CONTRIBUTING.md, AGENTS.md, and the PR template. **Do not merge.** The author declares the version.

### Phase 9: Restart at higher baseline (ongoing)
- Re-review every `open` item on its `review_after` date.
- Re-run the unmapped sweep on sparse cells in `COVERAGE.md`.
- When new measurements appear (new CODATA or PDG releases), re-audit the affected items and re-form their containers.
- Each cycle loads all prior cycles (Capsule).

---

## 9. Definition of done (per phase)

A phase is done when:
- Every item in scope has an audit file that passes `tools/validate_audit.py`.
- Every container passes `tools/validate_containers.py` and has at least one open edge.
- `audit/COVERAGE.md` shows the phase's scope as covered, with sparse or blind areas named.
- Ledger rows and CHANGELOG entries are added where a variable moved.
- No released version file was edited.
- The PR honesty checklist is fully checked, with notes where an item is partial.

The **whole task** is never "done": completeness is a direction. It reaches a **baseline** when Phase 8's draft is declared by the author, and then it restarts (Phase 9).

---

## 10. When to stop and ask the author

Stop and write the question into the PR description (and `audit/FINDINGS.md`) when:
- A finding would change a `forced-fill` in canon to anything else.
- A Forcing Test result depends on an operator choice (a stipulation) that the author has not made.
- A proposed new stage or layer would be architectural (like v5.3's ⊙).
- A primary measurement source cannot be found for something canon treats as measured.
- The Container ⊙ reconciliation (F-004) does not resolve cleanly.

---

## 11. Credit line (for outputs that reproduce canon)

```
Source: GFunnel Methodology (Omni Process) v5.4, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0.
```
