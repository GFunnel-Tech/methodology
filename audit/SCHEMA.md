# Audit Schema — Vocabularies and Record Formats

> **Status: derivation.** Canon does not name an audit record, a diff state, an exclusion diagnosis, or a knowledge container. This file defines them for the Reality Audit (brief §5). They are labeled derivations until the author declares them into a version (brief §3 rule 9). Where a term *is* canonical, its source is given.

`tools/validate_audit.py` and `tools/validate_containers.py` enforce everything in this file that can be checked mechanically. If this file and a validator disagree, this file is the specification and the validator has a bug.

---

## 1. Status vocabularies (use these exact terms)

### 1.1 Observation grade (the reality log)

| Term | Meaning |
| --- | --- |
| `measured-reproduced` | Independently reproduced measurement. |
| `measured-single` | Measured, not independently reproduced. |
| `derived` | Inferred from measurements by an explicit derivation (shown). |
| `held-open` | No measurement possible or available. Say why. |

*Source:* derivation. Operationalizes the Variable Principle's measured / structurally derived / held open (v5.1; [`framework/registers.md`](../framework/registers.md) §1) for the reality side.

**Substrate item 8 (weak observations cannot force change):** only `measured-reproduced` may drive an `adjusted` intake result. A `measured-single` observation that differs from canon goes to `open`.

### 1.2 Claim outcome (the methodology log, from the Forcing Test)

| Term | Meaning | Source |
| --- | --- | --- |
| `forced-fill` | One candidate survives by logical necessity (Output 1). | v5.3 |
| `live-hypothesis` | Plausible, not forced; carries an attached falsifier. | v5.3 |
| `stipulation` | An operator or presentation choice, not a forced result. | v5.3 |
| `proven-open` | Cannot be closed from inside the system (Output 4). | v5.3 ("proven-unforceable") |
| `forced-no` | Tested and ruled out. | v5.4 §9, §12 (see FINDINGS F-008) |

### 1.3 Diff state (the comparison)

| Reality | Methodology | Diff state | Consequence |
| --- | --- | --- | --- |
| has it | has it, consistent | `accounted` | Candidate for a container |
| has it | lacks it | `methodology-gap` | Methodology adapts (after diagnosis) |
| lacks it | has it | `unobserved-claim` | Held open until reality shows it |
| has it | contradicts it | `conflict` | Reality wins; methodology adapts |
| has it | no stage or domain to hold it | `unmapped` | Diagnose; may reveal a missing stage |

**Extension (derivation, this file):** `n/a` is permitted only in `GOV-###` files, where the item is a governance rule rather than a claim about reality.

### 1.4 Exclusion diagnosis

**Required before** any `methodology-gap`, `conflict`, or `unmapped` item is classified. For every other diff state, write `n/a`.

| Term | Meaning |
| --- | --- |
| `not-reached` | The log has not grown to this point. |
| `reached-conflicting` | It contradicts an existing entry. |
| `unverified` | The observation is not reproduced. |
| `beyond-depth` | The log cannot hold it yet without overreaching (concentration discipline, substrate item 3). |

### 1.5 Intake result

| Term | Meaning |
| --- | --- |
| `integrated` | It fits as it is. |
| `adjusted` | It is real but conflicts, so the methodology re-forms around it. Record the adjustment and the reason. |
| `open` | Unresolved. Held at the edge, never forced. **Must carry a `review_after` date** (`YYYY-MM-DD`). Open must not decay into ignored. |

---

## 2. Permitted measurement sources (reference points only)

Primary measurement databases and the peer-reviewed measurement papers they cite. Take the **number and its uncertainty**, never the source's narrative. Examples: CODATA/NIST (constants), PDG (particle data), Planck/COBE/WMAP data releases, primordial abundance measurements, NIST chemistry and spectral data, genome databases, geological dating datasets.

Every observation row records:

| Field | Rule |
| --- | --- |
| `quantity` | What was measured, in neutral words. |
| `value` | The number, with units. |
| `uncertainty` | As published (1σ unless stated). `exact` for defined SI values. |
| `grade` | §1.1. |
| `source` | Stable URL or DOI. |
| `retrieved` | `YYYY-MM-DD`. |

If a value cannot be verified from a primary source, grade it `held-open` and say why. Scripts that compute or check values follow the [`framework/tests/`](../framework/tests/README.md) convention: Python standard library only, constants declared at the top, reproducible.

---

## 3. File identifiers

| Prefix | Pattern | Directory | Phase |
| --- | --- | --- | --- |
| Governance | `GOV-###` | `audit/governance/` | 1 |
| Label | `LABEL-###` | `audit/labels/` | 2 |
| Stage | `STAGE-###` (001–100) | `audit/stages/` | 3 |
| Constant | `CONST-<slug>` (lowercase, digits, hyphens) | `audit/constants/` | 4 |
| Domain | `DOMAIN-##` (01–10) | `audit/domains/` | 5 |
| Unmapped | `UNMAPPED-####` | `audit/unmapped/` | 6 |
| Claim | `CLAIM-###` | `audit/claims/` | 3–5 (extension) |

The file name is `<id>.md` (a `-<slug>` suffix is allowed after the id, e.g. `LABEL-005-stage-5.md`). The `CLAIM` prefix (extension, derivation) covers canonical claims that are not a stage, constant, domain, or label: rows of the Falsifiability Register (v5.1 ◇), Appendix B/C entries, and Core Axioms with a factual core. The `GOV` prefix is an extension made by this file (brief Phase 1 allows "a dedicated `audit/governance/` file").

---

## 4. Audit record

One Markdown file per audited item. YAML front matter, then body.

```markdown
---
id: STAGE-005            # see §3
canon_ref: v5.1 Appendix A, Stage 5
canon_label: "Big Bang Nucleosynthesis"
proposed_label: "Primordial Light-Element Formation"   # only if the label carries unforced narrative
diff_state: accounted     # §1.3
exclusion_diagnosis: n/a  # §1.4 — required for methodology-gap / conflict / unmapped
claim_outcome: forced-fill   # §1.2 — for the methodology's claim here
intake_result: adjusted   # §1.5
review_after: null        # YYYY-MM-DD, required if intake_result = open
container: KC-0003        # link if one was created, else null
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

### Field rules (enforced by `tools/validate_audit.py`)

- **Required keys:** `id`, `canon_ref`, `canon_label`, `diff_state`, `exclusion_diagnosis`, `claim_outcome`, `intake_result`, `review_after`, `container`, `ledger_row`. `proposed_label` is optional.
- `unmapped` items may set `canon_ref: none` and `canon_label: none` — that is what unmapped means.
- `exclusion_diagnosis` must be one of §1.4 when `diff_state` is `methodology-gap`, `conflict`, or `unmapped`; otherwise `n/a`.
- `review_after` must be a date when `intake_result` is `open`; otherwise `null` or a date. A past `review_after` on an `open` item is reported as **overdue** (warning).
- `container`, when set, must match `KC-####`.
- **Required body sections:** `## Canon says`, `## Reality shows`, `## Scientific Inquiry run`, `## Forcing Test`, `## Anti-Operation`.
- **Blocked runs:** if a Scientific Inquiry or Forcing Test step cannot be completed, write `BLOCKED:` followed by the blocker at that step and leave the later steps empty. The validator accepts empty steps only after a `BLOCKED:` line.
- **Honest `adjusted`:** `intake_result: adjusted` requires at least one `measured-reproduced` row in `## Reality shows` (substrate item 8).

---

## 5. Container record (derivation: the container unit)

Containers live in [`../containers/`](../containers/README.md), one file each, IDs `KC-####`. The prefix **KC** ("knowledge container") keeps them distinct from Layer ⊙ (the Container meta-tier, v5.3). Their relationship is audited in Phase 1 (FINDINGS F-004, F-007).

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

### Container rules (enforced by `tools/validate_containers.py` where mechanical)

- Create containers for `forced-fill` items, and for `integrated` observations that have a measured equation or a derived algorithm.
- A `live-hypothesis` container must say so plainly and carry its falsifier (the word **falsifier** must appear in the body). It is never presented as solved.
- `form: equation` or `both` requires a non-empty `### Equation` subsection **and** a non-empty `## Trace`. No invented equations (brief §3 rule 7).
- `form: algorithm` or `both` requires numbered steps under `### Algorithm`.
- `## Open edge` must contain at least one non-empty item. A container with no open edge is invalid (Anti-Operation).
- `## Re-formation log` must contain at least one dated entry (`YYYY-MM-DD`). Containers are re-formed, not overwritten: append, never delete.
- Every `links_up` / `links_down` / `audit_refs` target must exist.
- [`../containers/INDEX.md`](../containers/INDEX.md) must list every container id.

---

```
Source: GFunnel Methodology (Omni Process) v5.4, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0.
```
