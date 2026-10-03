# Knowledge map: what research programs the audited canon rests on

Step 1 of the "cost of gaining the knowledge" estimate. Machine-readable: [`knowledge_map.json`](knowledge_map.json) (one row per item) and [`new_programs.json`](new_programs.json) (programs still to cost). Facility ids reuse [`facilities.json`](facilities.json).

Scope: 234 audited items (100 stages, 87 constants, 10 domains, 20 claims, 17 labels) plus 14 `CANON-*` items read from the canonical text (v5.1 Layer I.B civil-infrastructure cases; v5.4 physics).

## Rules used

- `facility`: a named program or facility produced a measurement the audit cites. Where the audit cites a paper, the program named is the one that produced its data (e.g. arXiv 1807.06209 -> `planck`, 2112.04510 -> `hubble`, 2110.00483 -> `bicep-keck`).
- `studies`: ordinary research papers. `n_studies` counts distinct primary papers in the item's "Reality shows" table (DOI/PMID/arXiv/paper URL, de-duplicated when one paper is given by DOI and PMID). Database and reference pages (PDG, NIST/CODATA, KEGG, NCBI tables, SEP, Wikipedia, Scholarpedia, Nobel press releases, repository files, audit scripts) are not counted.
- On `facility` items, `n_studies` counts only the papers that are **not** outputs of a listed program. So a paper is never costed twice within one item.
- `reference`: the core value comes from a compilation (CODATA via `nist`, `pdg`, `kegg`, `ncbi`). A `studies` item may also list a reference body in `programs` when it plays a minor part (e.g. Landauer: 3 experiments + CODATA k).
- `proof`: mathematical or theoretical result with no measurement. `n_studies` there counts the theory/history papers cited, for scholars'-time costing, and is reported separately below.
- `none`: nothing measured (framework construct, projected stage, count of canon's own text, or bibliographic dates only). `n_studies` is 0.
- `CANON-*` items: `n_studies` counts only sources the canon itself names (mostly 0). Their `studies` basis says what kind of work the figure would rest on. It is not a count.

## Counts by knowledge basis

| Basis | Stages | Constants | Domains | Claims | Labels | Canon extra | **Total** |
|---|---:|---:|---:|---:|---:|---:|---:|
| facility | 17 | 8 | 0 | 1 | 0 | 3 | **29** |
| studies | 29 | 25 | 6 | 11 | 3 | 9 | **83** |
| reference | 4 | 16 | 1 | 2 | 0 | 1 | **24** |
| proof | 1 | 26 | 2 | 0 | 1 | 1 | **31** |
| none | 49 | 12 | 1 | 6 | 13 | 0 | **81** |
| **Total** | 100 | 87 | 10 | 20 | 17 | 14 | **248** |

## Programs ranked by the number of items that rely on them

| # | Program | Status | Items | Used by |
|---:|---|---|---:|---|
| 1 | `nist` | in facilities.json | 23 | STAGE-001, CONST-boltzmann-constant, CONST-bremermann-limit, CONST-einstein-field-equations, CONST-electron-mass, CONST-elementary-charge, CONST-fine-structure-constant, CONST-gravitational-constant, CONST-heisenberg-uncertainty, CONST-keplers-laws, CONST-landauer-principle, CONST-maxwells-equations, CONST-newtons-third-law, CONST-planck-length, CONST-planck-time, CONST-proton-mass, CONST-reduced-planck-constant, CONST-schrodinger-equation, CONST-speed-of-light, DOMAIN-08, CLAIM-002, CLAIM-010, CLAIM-011 |
| 2 | `pdg` | **new** | 16 | STAGE-001, STAGE-002, STAGE-003, STAGE-005, STAGE-006, STAGE-007, CONST-angular-momentum-conservation, CONST-baryon-number-conservation, CONST-charge-conservation, CONST-cpt-symmetry, CONST-lepton-number-conservation, CONST-maxwells-equations, CLAIM-002, CLAIM-014, CANON-v54-koide, CANON-v54-lifetime-linewidth |
| 3 | `planck` | in facilities.json | 11 | STAGE-001, STAGE-002, STAGE-003, STAGE-005, STAGE-006, STAGE-007, STAGE-081, STAGE-083, CONST-cosmological-constant, CONST-hubble-constant, CLAIM-008 |
| 4 | `kegg` | **new** | 7 | STAGE-015, STAGE-016, STAGE-019, STAGE-020, STAGE-021, CONST-atp-yield-per-glucose, CONST-krebs-cycle-stoichiometry |
| 5 | `borexino` | in facilities.json | 3 | STAGE-007, CONST-charge-conservation, CONST-lepton-number-conservation |
| 6 | `ligo` | in facilities.json | 3 | STAGE-008, CONST-einstein-field-equations, CANON-v54-nuclear-saturation |
| 7 | `super-kamiokande` | in facilities.json | 3 | CONST-baryon-number-conservation, CONST-lepton-number-conservation, CANON-v54-lifetime-linewidth |
| 8 | `bicep-keck` | **new** | 2 | STAGE-001, STAGE-003 |
| 9 | `desi` | in facilities.json | 2 | STAGE-081, CLAIM-008 |
| 10 | `eso-vlt` | **new** | 2 | STAGE-007, STAGE-008 |
| 11 | `hubble` | in facilities.json | 2 | CONST-cosmological-constant, CONST-hubble-constant |
| 12 | `lhc` | in facilities.json | 2 | STAGE-003, STAGE-004 |
| 13 | `messenger` | **new** | 2 | CONST-einstein-field-equations, CONST-keplers-laws |
| 14 | `alma` | **new** | 1 | STAGE-009 |
| 15 | `cassini` | in facilities.json | 1 | CONST-einstein-field-equations |
| 16 | `cobe` | in facilities.json | 1 | STAGE-006 |
| 17 | `darpa-hafnium-isomer` | **new** | 1 | CANON-v54-hafnium-isomer |
| 18 | `exa-cel-clinical-program` | **new** | 1 | STAGE-065 |
| 19 | `fermi` | **new** | 1 | CONST-einstein-field-equations |
| 20 | `iss` | in facilities.json | 1 | STAGE-063 |
| 21 | `jwst` | in facilities.json | 1 | STAGE-007 |
| 22 | `kamland` | in facilities.json | 1 | CONST-lepton-number-conservation |
| 23 | `meg` | **new** | 1 | CONST-lepton-number-conservation |
| 24 | `microscope` | **new** | 1 | CONST-newtons-first-law |
| 25 | `ncbi` | **new** | 1 | CONST-genetic-code-universality |
| 26 | `nicer` | **new** | 1 | CANON-v54-nuclear-saturation |
| 27 | `nustar` | **new** | 1 | STAGE-008 |
| 28 | `osiris-rex` | in facilities.json | 1 | STAGE-010 |
| 29 | `pew-global-religion` | **new** | 1 | STAGE-045 |
| 30 | `rhic` | in facilities.json | 1 | STAGE-004 |
| 31 | `un-wup` | **new** | 1 | STAGE-043 |
| 32 | `us-census-bfs` | **new** | 1 | STAGE-042 |
| 33 | `wmap` | in facilities.json | 1 | STAGE-006 |

Facilities in `facilities.json` that no item relies on: `hgp`. The genome and phylogeny items (Stages 14-31, LABEL-101, CLAIM-010/012) cite individual phylogenomic and sequencing papers. None of them cites a Human Genome Project dataset, so `hgp` is not assigned. That these studies depend on the reference genome is plausible, but it is inferred and held open.

## Studies by field

Sums of `n_studies`. Empirical = `studies` + `facility` + `reference` items. Proof = theory/history papers on `proof` items.

| Field | Empirical studies | Proof/theory papers | Total |
|---|---:|---:|---:|
| physics | 36 | 10 | 46 |
| biochemistry | 32 | 0 | 32 |
| neuroscience | 31 | 0 | 31 |
| cell-biology | 27 | 0 | 27 |
| genetics-evolution | 26 | 1 | 27 |
| other | 14 | 0 | 14 |
| computer-science | 7 | 6 | 13 |
| psychology | 12 | 0 | 12 |
| social-science | 9 | 0 | 9 |
| earth-science | 9 | 0 | 9 |
| mathematics | 1 | 7 | 8 |
| chemistry | 5 | 1 | 6 |
| economics | 5 | 0 | 5 |
| astronomy | 5 | 0 | 5 |
| **Total** | **219** | **25** | **244** |

These are per-item sums. Some papers are cited by more than one item (e.g. Bérut 2012, the dos Reis 2015 molecular clock, the Cogitate test, the decoherence experiments). If each paper is costed once, the number of distinct papers is lower than the total.

## Caveats (held open)

- The audit cites what it fetched, not everything the knowledge rests on. A value taken from PDG or CODATA rests on many experiments, and this map stops at the compiling body. Costing `pdg`/`nist` as compilation operations understates what the underlying experiments cost. This variable stays open.
- 81 items are `none`. They contribute no knowledge-acquisition cost. That is not a finding that the cost is zero; nothing was measured.
- `CANON-IB-*` figures ($14.5B, 246 deaths, $195B, $22T, 2,000 yr, 15-20 yr) have no source cited in the canon. What they cost to establish is held open until each one is traced (LABEL-103 routes them to CLAIM audits).

```
Source: GFunnel Methodology (Omni Process) v5.1 / v5.4 and its Reality Audit, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Mapping adapted; not endorsed by the author.
```
