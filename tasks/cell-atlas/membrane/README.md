# Plasma Membrane — Top-Down Breakdown

> **Status: derivation / work-in-progress. Not canon.** Scope: the eukaryotic plasma membrane. Internal membranes (ER, Golgi, mitochondria, nucleus) get their own areas later.

**Canon anchor:** v5.1 Appendix A Stage 12 (Lipid Bilayer / Protocell Formation), Stage 13 (Chemiosmosis), Stage 24 (Ion Gradients / Membrane Potentials); Domain 9 (Biological).

**Completeness: held open.** Gaps found while building this breakdown are in [`gaps.md`](gaps.md).

---

## How this is broken down (derivation)

Canon has no rule for decomposing a system into its sub-processes. The Master Meta-Algorithm locates a domain, Kingdom and principle, but it never says how to split a whole into parts (gap **MF-03**). The rule below is derived from the base code and labelled a derivation:

| Level | What it is | Rule |
| --- | --- | --- |
| **L0** | The membrane as one process | Run DETECT → PROCESS → RESPOND on the whole. |
| **L1** | Functional categories | Split by the role each part plays in the L0 loop, plus three things every loop needs: the substrate it runs on (A), the loop run on itself (B), and its lifecycle (K). |
| **L2** | Subcategories | Split each category by *what* is handled: matter, charge, information, contact, shape. |
| **L3** | Mechanism families | Mechanisms that share one physical principle. |
| **L4** | Specific mechanisms | One molecule or one complex. |

Runs go **top-down**: L0, then each L1, then L2 and below. A lower level is run only after its parent, so patterns found at a higher level can be checked at the levels below.

[Run 01 (Na+/K+ pump)](run-01-na-k-pump.md) is an **L4 leaf**. It was run out of order as a pilot of the run format. Its patterns stay single instances until the L1 category C and L2 C3 runs place them.

**Scope tags:** **U** = expected in all eukaryotes · **A** = animals · **PF** = plants and fungi · **S** = specialized cell types · **?** = scope not yet checked. Tags are coarse, and checking them is an open gap (**MG-10**).

---

## L0 — The plasma membrane as one process

| Role | At the scale of the whole membrane |
| --- | --- |
| **Precondition** | A boundary exists: there is an inside and an outside (canon Stage 12). |
| **DETECT** | Changes at the boundary: chemical (ligands), physical (stretch, voltage, temperature, osmotic pressure), contact (other cells, matrix), and the membrane's own state. |
| **PROCESS** | Transduction at or next to the membrane: conformational change, second messengers, lipid signalling, clustering. |
| **RESPOND** | Change what crosses, what is released, the cell's shape and contacts, and the membrane's own composition → a new boundary state, which is the next cycle's input. |

---

## L1 → L2 → L3 (→ L4 examples)

Legend: ✅ run complete · ◐ partial · ☐ queued. **New** = added from the gap pass ([`gaps.md`](gaps.md)).

### A. Boundary — existence and structure *(the substrate the loop runs on; not itself D, P or R)*

- ☐ A1 Self-assembly: bilayer formation by the hydrophobic effect **(U)**
- ☐ A2 Composition: lipid classes, sterols, membrane proteins, glycans **(U)**
- ☐ A3 Physical state: fluidity and phase, thickness, permeability **(U)**
- ☐ A4 Electrical property: the bilayer as a capacitor (~0.9 µF/cm², measured) **(U?)** — **new**, MG-08

### B. Self-maintenance — the membrane running the loop on itself *(D → P → R)*

- ☐ B1 Self-sensing: packing, saturation, sterol level, tension — **new**, MG-02 (partly held open)
- ☐ B2 Lipid supply: synthesis in the ER; delivery by vesicles and by contact sites **(U)**
- ☐ B3 Protein supply: insertion and topology set in the ER; delivery to the surface **(U)** — **new**, MG-06
- ☐ B4 Asymmetry upkeep: flippases, floppases, scramblases **(U)**
- ☐ B5 Fluidity adjustment: sterols; fatty-acid remodelling with temperature **(U)**
- ☐ B6 Repair: Ca²⁺-triggered patching **(?)**
- ☐ B7 Turnover: endocytic removal and degradation of proteins and lipids **(U)**

### C. Exchange of matter — crossing the boundary *(mostly RESPOND; a passive baseline)*

- ☐ C1 Passive: diffusion through the bilayer **(U)**
- ☐ C2 Facilitated: channels (selectivity, gating) · carriers / uniporters · water channels **(U)**
- ☐ C3 Active, primary: pumps that spend ATP
  - L3: P-type ATPases
    - ✅ L4: Na+/K+ pump **(A)** → [run 01](run-01-na-k-pump.md)
    - ☐ L4: H+ pump (plasma-membrane H+-ATPase) **(PF)** — **new**, MG-01
    - ☐ L4: Ca²⁺ pump (PMCA) **(?)**
  - L3: ABC transporters **(U?)**
- ☐ C4 Active, secondary: symporters and antiporters that spend a gradient **(U)**
- ☐ C5 Bulk entry: clathrin · caveolae **(A)** · macropinocytosis · phagocytosis **(S)**
- ☐ C6 Bulk exit: constitutive and regulated exocytosis (SNARE fusion) **(U)**
- ☐ C7 Through-passage: transcytosis **(S)** — **new**, MG-05
- ☐ C8 Volume and osmotic balance **(U)**

### D. Electrical — charge separation as a store and a signal

- ☐ D1 Resting membrane potential **(U)**
- ☐ D2 Action potentials **(S; also some plants and protists)**
- ☐ D3 Voltage sensing (voltage-sensor domains) — **new**, MG-03

### E. Sensing — *DETECT*

- ☐ E1 Chemical: G-protein-coupled receptors **(?)** · receptor kinases · ligand-gated channels · nutrient sensors
- ☐ E2 Mechanical: stretch-activated channels (Piezo family, measured) **(?)** — **new**, MG-03
- ☐ E3 Thermal and osmotic sensing **(?)** — **new**, MG-03
- ☐ E4 Contact sensing: adhesion receptors that signal **(?)**
- ☐ E5 Self-sensing → see B1

### F. Transduction at the membrane — *PROCESS*

- ☐ F1 Conformational relay (receptor → coupled protein)
- ☐ F2 Lipid second messengers (PIP₂ → IP₃ + DAG)
- ☐ F3 Clustering and nanodomains as signalling platforms
- ☐ F4 Termination and desensitization

### G. Output — signals sent outward *(RESPOND)*

- ☐ G1 Regulated secretion (→ C6)
- ☐ G2 Extracellular vesicles budded from the plasma membrane (ectosomes) — **new**, MG-04
- ☐ G3 Lipid-derived mediators released from membrane lipids — **new**, MG-04
- ☐ G4 Surface display: presenting molecules for other cells to read **(S)**

### H. Contact and identity

- ☐ H1 Glycocalyx; self/non-self recognition **(?)**
- ☐ H2 Junctions: tight · adherens · desmosomes · gap junctions **(A)**
- ☐ H3 Cell–matrix adhesion **(A)**
- ☐ H4 Cell wall interface **(PF)** — **new**, MG-01

### I. Shape, mechanics and motility — **new category**, MG-05

- ☐ I1 Curvature generation and sensing
- ☐ I2 Membrane tension as a cell-wide variable
- ☐ I3 Cytoskeleton anchoring
- ☐ I4 Protrusions: lamellipodia, filopodia, blebs, microvilli **(A)**

### J. Spatial organization — **new category**, MG-05

- ☐ J1 Lateral domains (rafts / microdomains)
- ☐ J2 Polarity: apical vs. basolateral domains **(S)**
- ☐ J3 Specialized compartments: primary cilium membrane **(?)**
- ☐ J4 Membrane contact sites: ER–plasma membrane (lipid transfer; store-operated Ca²⁺ entry, measured) **(?)** — **new**, MG-07

### K. Lifecycle

- ☐ K1 Growth: surface area added before division
- ☐ K2 Division: membrane remodelling in cytokinesis
- ☐ K3 Fusion: cell–cell fusion **(S)**
- ☐ K4 Death: phosphatidylserine exposure ("eat-me" signal) in apoptosis; membrane rupture in other death modes **(?)**

---

## Open edge

- Each L1 run must check whether its mechanisms depend on a process missing from this tree and add it. The current gaps are in [`gaps.md`](gaps.md).
