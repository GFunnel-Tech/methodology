# Findings — Running List

> **Status: derivation / work-in-progress. Not canon.** A finding is a confirmed difference between the explicit log (canon) and either reality or the audit's governing model. A finding is not a resolution. Each one resolves in the phase named, through an audit file and, where a variable moves, an Iteration Ledger row.

Add every new finding as `F-###` with the same columns. Never delete a finding; when it resolves, set its status and link the file that resolved it.

Status legend: ☐ open · ◐ in progress · ✅ resolved (classified) · ❓ question for the author (brief §10)

| # | Finding | Evidence | Resolution path | Phase | Status |
| --- | --- | --- | --- | --- | --- |
| F-001 | **Stage 5 label "Big Bang Nucleosynthesis"** imports an origin narrative. v5.4 §5 already rules the Big Bang *as an event* forced-false and keeps only the phase and its observations. | v5.1 App. A Stage 5; v5.4 §5 (*"event false, phase forced"*); v5.4 §9 row 6 | Keep the observations (light-element abundances). Remove the name. Propose "Primordial Light-Element Formation." Re-label proposed for v5.5. | 2 (PR 6) | ✅ [STAGE-005](stages/STAGE-005.md) — abundances match PDG 2024; relabel proposed |
| F-002 | **Stage 3 "Symmetry Breaking / Inflation":** inflation is a model with indirect support, filed without a status tag. | v5.1 App. A Stage 3 | Tag `live-hypothesis`. Separate what is observed from what is modeled. | 2 (PR 6) | ✅ [STAGE-003](stages/STAGE-003.md) — live-hypothesis; tensor modes undetected (r < 0.036) |
| F-003 | **The base-code rule conflicts with "reality is the authority."** | [`CONTRIBUTING.md`](../CONTRIBUTING.md) "The one rule"; [`AGENTS.md`](../AGENTS.md) "What you must not do"; substrate §1 item 7 | Scope to "holds until reality contradicts it." Log as a governance departure. Record as stipulation (operator decision) unless the Forcing Test forces it outright. Wording drafted in Phase 1, applied only in the v5.5 draft. | 1 (PR 2) | ✅ [GOV-001](governance/GOV-001.md) — **forced-fill by canon's own ◇**, not only an operator decision |
| F-004 | **The Container ⊙ definition vs. the log-as-surface-tension model.** v5.3 files ⊙ as the capstone meta-tier. The substrate model defines the methodology as a self-forming, ever-growing log. | v5.3 §3; substrate §1 item 2 | Forcing Test: same structure seen two ways, a refinement, or a conflict? Carry v5.3's open question ("what is the Container a component of?"). If unresolved, ask the author (brief §10). | 1 (PR 3) | ❓ [GOV-002](governance/GOV-002.md) — refinement (adds an intake step), not forced |
| F-005 | **No exclusion-diagnosis step exists.** Canon classifies what is in scope but has no procedure to ask *why* something is missing. | [`CONTRIBUTING.md`](../CONTRIBUTING.md); [`framework/registers.md`](../framework/registers.md) | Added as a derivation in [`SCHEMA.md`](SCHEMA.md) §1.4. Classify, and propose into v5.5. | 1 (PR 4) | ✅ [GOV-003](governance/GOV-003.md) — need forced; four terms a stipulation |
| F-006 | **Implicit log vs. explicit log.** Reality records itself in structure; the methodology is the written copy. This relates to I.F (Multi-Level Observation) and I.G (the Capsule) but is not stated. | brief §1; substrate §0; v5.1 I.F, I.G | Forcing Test for Correspondence with I.F / I.G. | 1 (PR 4) | ✅ [GOV-004](governance/GOV-004.md) — Correspondence of I.F's record levels |
| F-007 | **No container unit exists.** Master Meta step 11 ("if it is not written, it does not exist as a process") and v5.4's conjugate-gap rule imply it, but there is no standard form. | v5.1 Master Meta-Algorithm step 11; v5.3 §3 (Anti-Operation); v5.4 §0 | `containers/` created as a derivation (Phase 0: schema); classify (Phase 1); populate (Phase 7). | 0 → 1 (PR 5) → 7 | ✅ [GOV-005](governance/GOV-005.md) — unit forced (step 11); open-edge rule live |
| F-008 | **`forced-no` is used as an outcome class but is not in the register's outcome table.** [`framework/registers.md`](../framework/registers.md) §2 lists four classes (forced-fill, live hypothesis, stipulation, proven-open), following v5.3. v5.4 §9 and §12 log thirteen items as **forced-no**, `registers.md` §4 uses the term, and the brief's claim-outcome vocabulary includes it. The class is used but never defined in canon. | v5.3 §3 (four outputs); v5.4 §9, §12; `registers.md` §2 vs. §4 | Found in Phase 0 while writing [`SCHEMA.md`](SCHEMA.md). Forcing Test: is forced-no a fifth output, or the negative case of forced-fill (Test B leaves zero candidates)? Classify in Phase 1 (PR 4, with the exclusion diagnosis, since both concern classification procedure). | 1 (PR 4) | ✅ [GOV-006](governance/GOV-006.md) — a candidate-elimination record, not a fifth output |
| F-009 | **The brief names an issue template that does not exist.** Phase 0 asks for the "Docs / navigation / tooling" issue template; [`.github/ISSUE_TEMPLATE`](../.github/ISSUE_TEMPLATE) has only Iteration proposal, Variable evidence, Application / Usage report, and Transcription fix. "Docs / navigation / tooling" exists only as a change-type checkbox in the PR template. | `.github/ISSUE_TEMPLATE/`; `.github/PULL_REQUEST_TEMPLATE.md` | Repository tooling, not canon. Phase 0's issue body is drafted in [`issues/`](issues/) using the PR template's change type. Whether to add a matching issue template is the author's call. | 0 | ❓ author |

### Found by the audit (F-010 onward)

Each row links the audit file that holds the sources. "Canon" is v5.1 unless stated. Resolutions are **proposals for v5.5**; nothing in `versions/` is changed.

#### A. Canon states something reality contradicts

| # | Finding | Evidence (see file) | Proposed resolution | Status |
| --- | --- | --- | --- | --- |
| F-010 | **Λ value unreadable:** App. D writes `~1.1×10⁻µ² m⁻²`. | Derived from Planck 2018: 1.091(20) × 10⁻⁵² m⁻² — [CONST-cosmological-constant](constants/CONST-cosmological-constant.md) | Transcription-fix issue: author checks original; "10⁻⁵²" is consistent. | ❓ author |
| F-011 | **Stage 16 joins two processes:** "Fermentation / Anaerobic Respiration". Anaerobic respiration uses an ETC with non-O₂ acceptors. | KEGG; biochem literature — [STAGE-016](stages/STAGE-016.md) | Relabel "Fermentation"; place anaerobic respiration with the ETC stages. | proposal |
| F-012 | **Stage 30 "first time biology encodes information digitally"**: the genetic code is discrete and older; *Paramecium* fires all-or-none spikes. | [STAGE-030](stages/STAGE-030.md) | Drop "first", or narrow to nervous systems. | proposal |
| F-013 | **Stage 31 "a billion years before language":** dated gap ≈ 0.6–0.8 Gyr. | dos Reis 2015; Hublin 2017 — [STAGE-031](stages/STAGE-031.md) | Reword; held open (one analysis). | open |
| F-014 | **Domain 8 "spontaneous reactions move toward higher entropy":** H₂ + ½O₂ → H₂O(l) is spontaneous with ΔS_sys = −163 J/(mol·K). | NIST/CODATA — [DOMAIN-08](domains/DOMAIN-08.md) | "Spontaneous when ΔG < 0; *total* entropy increases." | proposal |
| F-015 | **Kepler role text:** "the same gravitational mechanics that holds an electron near a nucleus." The binding is electromagnetic; F_grav/F_Coulomb = 4.4 × 10⁻⁴⁰. | [CONST-keplers-laws](constants/CONST-keplers-laws.md) | Remove the sentence. | proposal |
| F-016 | **Le Chatelier stated as exceptionless** (and equated with the Garlick Equilibrium). Adding N₂ above x = 0.5 shifts NH₃ synthesis toward more N₂. | derived; Uline & Corti 2006 — [CONST-le-chatelier-principle](constants/CONST-le-chatelier-principle.md) | State as a rule of thumb with its domain; carry to Layer V. | proposal |
| F-017 | **Fibonacci "the growth pattern of all living systems":** 17.7% of sunflower counts are non-Fibonacci. | Swinton 2016 — [CONST-fibonacci-sequence](constants/CONST-fibonacci-sequence.md) | "Frequent in plant phyllotaxis." | proposal |
| F-018 | **√2 "three thousand years early"** (before Gödel): ≈ 2,400 years. | [CONST-sqrt-2](constants/CONST-sqrt-2.md) | Correct the figure. | proposal |
| F-019 | **Lepton number "why electrons persist":** electron stability is charge conservation; lepton *flavour* is measured violated (neutrino oscillation). | PDG 2024 — [CONST-lepton-number-conservation](constants/CONST-lepton-number-conservation.md) | Re-attribute; add flavour/total split. | proposal |
| F-020 | **"Hermetic principles articulated 2,000 years before QM"** (App. B, Domain 5 ◈, Layer I "thousands of years"). *The Kybalion* is 1908; canon's own glossary says so. | LCCN 08018560; Gutenberg #14209 — [CLAIM-018](claims/CLAIM-018.md), [DOMAIN-05](domains/DOMAIN-05.md), [LABEL-109](labels/LABEL-109-layer-II.md) | Correct the date; withdraw it as the basis for "tightened toward discovered". | proposal |
| F-021 | **"Quantum observer effect provides physics-level evidence"** for irreducible consciousness. Interference loss is measured to follow physical coupling to the environment. | Hornberger 2003; Hackermüller 2004; Myatt 2000 — [CLAIM-001](claims/CLAIM-001.md) | Remove as evidence; define "observation" operationally; carry the measurement-problem caution. | proposal |
| F-022 | **"Confirmed at quantum (Feynman)"** for slime-mold integration. The path integral is a formulation "mathematically equivalent" to QM, not a measurement. | Feynman 1948 abstract — [CLAIM-010](claims/CLAIM-010.md) | Remove "Confirmed"; cite the measured *Physarum* results instead. | proposal |
| F-023 | **"Every path's data preserved — confirmed in biological and cognitive substrates."** Forgetting is measured; archaic ancestry is 1–6% and partly purged. | Murre & Dros 2015; Jégou 2017 — [CLAIM-012](claims/CLAIM-012.md) | "Partial retention measured; full conservation held open." | proposal |
| F-024 | **Layer 0 "The DNA Metaphor — Why It Is Exact, Not Approximate":** DNA is not invariant across cells (V(D)J recombination; somatic mutation). | Tonegawa 1983; Milholland 2017 — [LABEL-101](labels/LABEL-101-layer-0.md) | "The DNA Analogy — Where It Holds and Where It Breaks." | proposal |
| F-025 | **"The Tao Te Ching's zhongyong"** (line 670). Zhongyong is Confucian (Liji); canon's glossary (line 4158) says so. | ctext.org — [LABEL-105](labels/LABEL-105-layer-I.D.md) | Correct the attribution. | proposal |
| F-026 | **Slime mold solves mazes "that confounded mathematicians until very recently"** (line 932). Dijkstra 1959. | [LABEL-108](labels/LABEL-108-layer-I.G.md) | Remove the clause. | proposal |
| F-027 | **v5.4 §2 over-grades Stage 3 and Stage 1→2:** the SM electroweak transition is a crossover (no false vacuum); no cosmic strings; the Casimir effect is lab-scale only. | [STAGE-001](stages/STAGE-001.md)–[003](stages/STAGE-003.md) | Downgrade the cosmic applications to live-hypothesis; keep Casimir and the Higgs mechanism forced. | ❓ author (changes a v5.4 forced-fill — brief §10) |
| F-028 | **Domain 10:** punctuated equilibrium misapplied to mass extinctions; "identical inputs produce identical outputs" contradicted by independent eye origins. | Gould & Eldredge 1993; Fernald 2006 — [DOMAIN-10](domains/DOMAIN-10.md) | Correct both. | proposal |
| F-029 | **Smaller corrections:** Domain 4 (Bostrom is a trilemma, not a derivation); Domain 6 (strong Sapir-Whorf); Domain 9 (apoptosis resistance is one of several cancer capabilities); Newton III, second law ("does not decrease"), baryon violation stated as fact, π in Maxwell (unit-dependent), hurricane/electron angular-momentum examples, Mandelbrot definition. | the linked files in `domains/` and `constants/` | Wording fixes in v5.5. | proposal |

#### B. Canon contradicts itself

| # | Finding | Evidence | Proposed resolution | Status |
| --- | --- | --- | --- | --- |
| F-030 | App. B "Energy Continuation Mechanism: **Resolved**" vs Layer I.E "Total System Question Is Open". | line 1884 — [CLAIM-008](claims/CLAIM-008.md) | "Bounded". | proposal |
| F-031 | Process density called "empirically settled" (Governing Epistemology; `registers.md` §1) vs "Open" (◇, Registry); no metric exists. | [CLAIM-003](claims/CLAIM-003.md) | Remove from the "measured" examples. | proposal |
| F-032 | Stage 48 "continuation structurally implied" vs Part IX (conditional) and Registry ◇ (held open). | [STAGE-048](stages/STAGE-048.md) | Make conditional. | proposal |
| F-033 | Stage 96 (open) vs App. B "tightened toward structural necessity"; Stages 50–100 open/predicted bands disagree between the Honest Statement and the section headers. | [STAGE-096](stages/STAGE-096.md) | Reconcile the bands. | proposal |
| F-034 | "None of these have been observed" (revision conditions) vs "Quantum mechanics appears to challenge" Correspondence in the same register. | [CLAIM-014](claims/CLAIM-014.md) | Reconcile. | proposal |

#### C. Status more confident than the evidence

| # | Finding | Evidence | Proposed resolution | Status |
| --- | --- | --- | --- | --- |
| F-035 | **"Tightened toward …"** (consciousness foundational, local-observation identity, Omni Force conscious, hard problem) rests on the framework's own premises, not measurement. | [CLAIM-015](claims/CLAIM-015.md)–[017](claims/CLAIM-017.md) | Reserve "tightened" for measured movement; add a status such as "framework-preferred". | ❓ author |
| F-036 | **Physical constants origin:** "tightens toward integration … fewer assumptions" — a parsimony preference, no discriminating observation. | [CONST-constants-origin-variable](constants/CONST-constants-origin-variable.md) | Hold all three candidates equally open. | proposal |
| F-037 | **Origin-of-life stages written as history:** RNA world, protocells, alkaline-vent chemiosmosis ("4 Bya"), glycolysis "most ancient", endosymbiosis mechanism. | [STAGE-011](stages/STAGE-011.md)–[018](stages/STAGE-018.md) | Tag live-hypothesis; name the Asgard archaeal host. | proposal |
| F-038 | **Stages 81–84** state cosmic contraction as fact; measurement shows accelerating expansion; DESI hints below 5σ. | [STAGE-081](stages/STAGE-081.md)–[084](stages/STAGE-084.md) | Reword as "whether …". | proposal |
| F-039 | **Planck length/time labelled "Minimum Meaningful Length/Duration"** — asserts what v5.4 holds open. | [CONST-planck-length](constants/CONST-planck-length.md) | "Planck length (unit √(ħG/c³))". | proposal |
| F-040 | **Counterfactual fine-tuning** ("if α were 4% different, no carbon") listed beside measured values. | [CONST-fine-structure-constant](constants/CONST-fine-structure-constant.md) | Tag as model result (live-hypothesis). | proposal |
| F-041 | **Convergence used as evidence without an independence rule** ("seven independent traditions", "five independent lines", "Tao convergence"). | [CLAIM-001](claims/CLAIM-001.md), [LABEL-112](labels/LABEL-112-layer-IV.md) | Adopt a rule for when lines of reasoning count as independent. | ❓ author (A4) |

#### D. Falsifiers that cannot fire

| # | Finding | Evidence | Proposed resolution | Status |
| --- | --- | --- | --- | --- |
| F-042 | **"Maps cleanly … zero exceptions"** (10 domains; Universal Algorithm): no observation is named that would count as a failure to map; in Domains 5, 8, 10 DETECT has no detector; failures convert to "named variables". | [DOMAIN-01](domains/DOMAIN-01.md)–[10](domains/DOMAIN-10.md), [CLAIM-007](claims/CLAIM-007.md) | File the mapping as **stipulation** (a lens), or state an operational falsifier. This is also the open edge of GOV-001. | ❓ author |
| F-043 | **Process Density, Selfish-Selfless convergence, Dynamic Middle, Correspondence, revision conditions 1–3:** undefined quantities or definitions that absorb every counterexample. | [CLAIM-003](claims/CLAIM-003.md)–[006](claims/CLAIM-006.md), [CLAIM-014](claims/CLAIM-014.md) | Define each measurably, or re-file as stipulation. | proposal |
| F-044 | **◇ "Current Evidence" cells cite no sources.** | [LABEL-116](labels/LABEL-116-layer-diamond.md) | Add a source column. | proposal |

#### E. What reality has that the stage list misses (methodology-gap)

| # | Finding | Evidence | Proposed resolution | Status |
| --- | --- | --- | --- | --- |
| F-045 | **Lithium problem** at Stage 5: observed Li/H 3.1× below prediction (4.4σ). | PDG 2024 — [STAGE-005](stages/STAGE-005.md) | Record as Stage 5's open edge. | open |
| F-046 | **Heavy-element sources:** neutron-star mergers and stellar winds, not only supernovae (Stage 8); ~half of beyond-iron elements are r-process. | [STAGE-007](stages/STAGE-007.md), [STAGE-008](stages/STAGE-008.md) | Broaden Stage 8. | open |
| F-047 | **No stage for reionization** (z ≈ 7.7). | [STAGE-007](stages/STAGE-007.md) | Candidate new stage (Phase 6). | open |
| F-048 | **Transitions that happened more than once** (multicellularity, neurons, eyes, self-recognition) and capacities older than their stage (sensory transduction in bacteria). The stage list is linear. | [STAGE-025](stages/STAGE-025.md), [028](stages/STAGE-028.md), [029](stages/STAGE-029.md), [036](stages/STAGE-036.md) | Decide how the progression represents repeated and earlier-than-stage transitions. | ❓ author (architectural) |
| F-049 | **Projected stages already reached:** Stage 63 (continuous off-planet habitation since Nov 2000); Stage 51 instantiated by this repository. Appendix A's order is not a time order. | NASA — [STAGE-063](stages/STAGE-063.md), [STAGE-051](stages/STAGE-051.md) | Add a reached / projected marker. | proposal |
| F-050 | **Energy conservation stated without its domain:** undefined globally in an expanding universe — and Layer I.E rests on it. | [CONST-energy-conservation](constants/CONST-energy-conservation.md) | Add the domain limit; carry to Layer I.E. | open |
| F-051 | **Sustained oscillation** (e.g. the repressilator) is a measured stable regime that "perfect process or the draw — no third configuration" neither includes nor excludes. | Elowitz & Leibler 2000 — [CLAIM-013](claims/CLAIM-013.md) | Name as a candidate third configuration. | open |

#### F. Architectural questions for the author (brief §10)

| # | Question | Where |
| --- | --- | --- |
| A1 | **Layer II — the Seven Hermetic Principles** are an outside model (*The Kybalion*, 1908) used as structure (substrate item 4). Keep, re-ground each principle on an observation that forces it, or re-file as "lenses"? | [LABEL-109](labels/LABEL-109-layer-II.md) |
| A2 | **Layer I.D — Yin/Yang** (imported Taoist frame). Keep the terms, or re-ground as two-pole balance? | [LABEL-105](labels/LABEL-105-layer-I.D.md) |
| A3 | **Layer IV — Co-Creator Identity** depends on Mentalism, which canon holds open. Keep the claim in the layer name? | [LABEL-112](labels/LABEL-112-layer-IV.md) |
| A4 | **Independence rule for convergence evidence** (F-041). | — |

#### G. Schema findings (the audit's own instrument)

| # | Finding | Proposed resolution |
| --- | --- | --- |
| F-052 | Observation grades fit measurements, not bibliographic facts (publication dates, text locations). Workers used measured-reproduced for two agreeing catalogues. | Define that rule in SCHEMA.md §1.1. |
| F-053 | Exclusion-diagnosis taxonomy may need `mis-filed` (GOV-003 open edge). | Test in Phase 6. |

---

## Questions for the author (brief §10)

- **F-003 / GOV-001:** the scoped base-code rule is forced by canon's own ◇ — confirm the drafted wording.
- **F-004 / GOV-002:** accept "refinement (adds an intake step to ⊙)"?
- **F-010, F-027, F-035, F-042, F-048** and **A1–A4** above.
- **F-009.** Add a "Docs / navigation / tooling" issue template, or keep using the PR template's change type for tooling work?
