# Findings — Running List

> **Status: derivation / work-in-progress. Not canon.** A finding is a confirmed difference between the explicit log (canon) and either reality or the audit's governing model. A finding is not a resolution. Each one resolves in the phase named, through an audit file and, where a variable moves, an Iteration Ledger row.

Add every new finding as `F-###` with the same columns. Never delete a finding; when it resolves, set its status and link the file that resolved it.

Status legend: ☐ open · ◐ in progress · ✅ resolved (classified) · ❓ question for the author (brief §10)

| # | Finding | Evidence | Resolution path | Phase | Status |
| --- | --- | --- | --- | --- | --- |
| F-001 | **Stage 5 label "Big Bang Nucleosynthesis"** imports an origin narrative. v5.4 §5 already rules the Big Bang *as an event* forced-false and keeps only the phase and its observations. | v5.1 App. A Stage 5; v5.4 §5 (*"event false, phase forced"*); v5.4 §9 row 6 | Keep the observations (light-element abundances). Remove the name. Propose "Primordial Light-Element Formation." Re-label proposed for v5.5. | 2 (PR 6) | ☐ |
| F-002 | **Stage 3 "Symmetry Breaking / Inflation":** inflation is a model with indirect support, filed without a status tag. | v5.1 App. A Stage 3 | Tag `live-hypothesis`. Separate what is observed from what is modeled. | 2 (PR 6) | ☐ |
| F-003 | **The base-code rule conflicts with "reality is the authority."** | [`CONTRIBUTING.md`](../CONTRIBUTING.md) "The one rule"; [`AGENTS.md`](../AGENTS.md) "What you must not do"; substrate §1 item 7 | Scope to "holds until reality contradicts it." Log as a governance departure. Record as stipulation (operator decision) unless the Forcing Test forces it outright. Wording drafted in Phase 1, applied only in the v5.5 draft. | 1 (PR 2) | ☐ |
| F-004 | **The Container ⊙ definition vs. the log-as-surface-tension model.** v5.3 files ⊙ as the capstone meta-tier. The substrate model defines the methodology as a self-forming, ever-growing log. | v5.3 §3; substrate §1 item 2 | Forcing Test: same structure seen two ways, a refinement, or a conflict? Carry v5.3's open question ("what is the Container a component of?"). If unresolved, ask the author (brief §10). | 1 (PR 3) | ☐ |
| F-005 | **No exclusion-diagnosis step exists.** Canon classifies what is in scope but has no procedure to ask *why* something is missing. | [`CONTRIBUTING.md`](../CONTRIBUTING.md); [`framework/registers.md`](../framework/registers.md) | Added as a derivation in [`SCHEMA.md`](SCHEMA.md) §1.4. Classify, and propose into v5.5. | 1 (PR 4) | ◐ schema in place |
| F-006 | **Implicit log vs. explicit log.** Reality records itself in structure; the methodology is the written copy. This relates to I.F (Multi-Level Observation) and I.G (the Capsule) but is not stated. | brief §1; substrate §0; v5.1 I.F, I.G | Forcing Test for Correspondence with I.F / I.G. | 1 (PR 4) | ☐ |
| F-007 | **No container unit exists.** Master Meta step 11 ("if it is not written, it does not exist as a process") and v5.4's conjugate-gap rule imply it, but there is no standard form. | v5.1 Master Meta-Algorithm step 11; v5.3 §3 (Anti-Operation); v5.4 §0 | `containers/` created as a derivation (Phase 0: schema); classify (Phase 1); populate (Phase 7). | 0 → 1 (PR 5) → 7 | ◐ schema in place |
| F-008 | **`forced-no` is used as an outcome class but is not in the register's outcome table.** [`framework/registers.md`](../framework/registers.md) §2 lists four classes (forced-fill, live hypothesis, stipulation, proven-open), following v5.3. v5.4 §9 and §12 log thirteen items as **forced-no**, `registers.md` §4 uses the term, and the brief's claim-outcome vocabulary includes it. The class is used but never defined in canon. | v5.3 §3 (four outputs); v5.4 §9, §12; `registers.md` §2 vs. §4 | Found in Phase 0 while writing [`SCHEMA.md`](SCHEMA.md). Forcing Test: is forced-no a fifth output, or the negative case of forced-fill (Test B leaves zero candidates)? Classify in Phase 1 (PR 4, with the exclusion diagnosis, since both concern classification procedure). | 1 (PR 4) | ☐ |
| F-009 | **The brief names an issue template that does not exist.** Phase 0 asks for the "Docs / navigation / tooling" issue template; [`.github/ISSUE_TEMPLATE`](../.github/ISSUE_TEMPLATE) has only Iteration proposal, Variable evidence, Application / Usage report, and Transcription fix. "Docs / navigation / tooling" exists only as a change-type checkbox in the PR template. | `.github/ISSUE_TEMPLATE/`; `.github/PULL_REQUEST_TEMPLATE.md` | Repository tooling, not canon. Phase 0's issue body is drafted in [`issues/`](issues/) using the PR template's change type. Whether to add a matching issue template is the author's call. | 0 | ❓ author |

---

## Questions for the author (brief §10)

- **F-009.** Add a "Docs / navigation / tooling" issue template, or keep using the PR template's change type for tooling work?
