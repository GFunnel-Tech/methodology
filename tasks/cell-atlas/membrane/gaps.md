# Plasma Membrane — Gap Register

> **Status: derivation / work-in-progress. Not canon.** IDs use **MG** (membrane inventory gaps) and **MF** (framework / method gaps) so they do not collide with canon's Gap 1–5 ([`framework/gaps.md`](../../../framework/gaps.md)).

**How the gaps were found.** I built the top-down breakdown ([`README.md`](README.md)) from the base code first (L0 loop → roles → categories). Then I checked it against three things:

1. the first inventory;
2. what canon says about membranes;
3. the eukaryotes the scope claims to cover.

A gap is anything that one of these has and another lacks.

**Status vocabulary:**
- **solved** = filled from a measured source and added to the tree.
- **solved by derivation** = a proposed rule, labelled, awaiting the author.
- **held open** = cannot be filled honestly yet; the data that would narrow it is named.
- **needs decision** = the author's call.

All sources retrieved 2026-10-02.

---

## Summary

| ID | Gap | Status |
| --- | --- | --- |
| MG-01 | Scope was animal-only, but "eukaryote" includes plants, fungi and protists | **solved** (tree re-scoped; H+ pump and cell-wall interface added) |
| MG-02 | No self-sensing: how the membrane detects its own state | **partly solved / held open** — reframed 2026-10-03: sensors read physical properties, not composition (B1a–B1c) |
| MG-03 | DETECT covered only chemical signals; physical sensing missing | **solved** |
| MG-04 | RESPOND had no outward signals beyond secretion | **solved** (source for G3 pending) |
| MG-05 | Missing categories: shape and mechanics, spatial organization, through-passage | **solved** (categories I, J, item C7) |
| MG-06 | Protein supply missing (only lipid supply was listed) | **solved** |
| MG-07 | ER–plasma-membrane contact sites missing | **solved** |
| MG-08 | The membrane's electrical property (capacitance) missing | **solved** |
| MG-09 | No whole-membrane level: the first list started at mechanisms | **solved** (L0 and the levels L1–L4) |
| MG-10 | Scope tags (U / A / PF / S) are coarse and unchecked | **held open** |
| MF-01 | Deep-Lens steps E, F, J assume an operator | **needs decision** |
| MF-02 | What counts as PROCESS? Does a protein-free bilayer run the base code? | **held open** — bears on canon Stage 12 |
| MF-03 | Canon has no rule for breaking a system into sub-processes | **solved by derivation** (awaiting author) |
| MF-04 | Three Kingdoms placement below the cell scale | **held open** |
| MF-05 | No rule for counting loops (run 01 found two half-loops per cycle) | **held open** |

---

## Inventory gaps (MG)

### MG-01 — The scope said "eukaryote" but the inventory was animal-only — **solved**

**Found by:** checking the pilot's own subject against the scope. The Na+/K+ pump is an animal pump. In plants and fungi, the main primary pump in the plasma membrane is an **H+-ATPase**: a P-type pump like Na+/K+, but it builds a proton gradient instead.

**Source:** Palmgren 2001, *Annu. Rev. Plant Physiol. Plant Mol. Biol.* 52:817, [doi:10.1146/annurev.arplant.52.1.817](https://doi.org/10.1146/annurev.arplant.52.1.817).

**Fill:** the tree now carries scope tags. C3 lists the H+ pump beside Na+/K+ under one L3 family (P-type ATPases). H4 (cell-wall interface) is added for plants and fungi.

**What this exposes:** "build an ion gradient with a P-type pump" is the general L3 process. The ion used (Na+/K+ vs. H+) is lineage-specific. That is exactly why run 01 should not have been the starting point: it is one lineage's instance of a more general process.

**Open edge:** protists are not yet checked (folds into MG-10).

### MG-02 — Self-sensing: how does the membrane detect its own state? — **partly solved / held open**

**Found by:** the L0 loop. If the membrane maintains its own composition (category B), something must DETECT that composition. The first inventory listed only the corrections (fluidity, asymmetry, repair), not the detection.

**Measured so far:**

| What is sensed | Sensor | Where | Source |
| --- | --- | --- | --- |
| Lipid packing / saturation | Mga2 transmembrane helix (controls unsaturated fatty-acid production) | **ER membrane**, fungi | Covino et al. 2016, *Mol. Cell*, [doi:10.1016/j.molcel.2016.05.015](https://doi.org/10.1016/j.molcel.2016.05.015) |
| Mechanical force on the membrane | Piezo1 / Piezo2 mechanically activated channels | Plasma membrane | Coste et al. 2010, *Science* 330:55, [doi:10.1126/science.1193270](https://doi.org/10.1126/science.1193270) |

**Held open (as first framed, 2026-10-02):** a measured sensor that reads the **plasma membrane's** lipid composition directly. The composition sensor found here sits in the ER, where the lipids are made. So the plasma membrane may be regulated at its source rather than sensed in place.

#### Reframe (2026-10-03) — raised by the author's question "would the molecular makeup be self-sensing?"

**Derived reframe, not established.** The first framing asked for a sensor of *composition*. None of the measured sensors reads composition directly. They read the **physical properties the composition produces**: packing, curvature, tension. Self-sensing therefore splits into three layers, now B1a–B1c in the breakdown:

| Layer | What happens | Status |
| --- | --- | --- |
| **B1a** Lipids alone | The bilayer reorganizes itself (phase separation, curvature sorting, phase change with temperature). The makeup and the response are the same molecules; there is no separate detector. | **Held open.** Counts as sensing only if MF-02 says a response with no distinct PROCESS step qualifies. Under the MF-02 criterion as proposed, this is self-organization, not self-sensing. Measurements of bare bilayers enter at the A3 run. |
| **B1b** Proteins read the bilayer's physical state | Packing: Mga2 (above) and the ALPS motif, which is unstructured in solution and folds into a helix only where lipids are loosely packed (Bigay et al. 2005, *EMBO J.* 24:2244, [doi:10.1038/sj.emboj.7600714](https://doi.org/10.1038/sj.emboj.7600714)). Curvature: BAR domains, crescent-shaped dimers that bind highly curved membranes (Peter et al. 2004, *Science* 303:495, [doi:10.1126/science.1092586](https://doi.org/10.1126/science.1092586)). Tension: Piezo (above). | **Measured** for the sensors listed. Where each one acts (plasma membrane vs. ER vs. Golgi) is not yet checked per sensor. |
| **B1c** Specific lipids read as labels | Protein domains bind particular lipids: PIP₂ marks the plasma membrane's inner leaflet; phosphatidylserine on the outer surface marks an apoptotic cell (→ K4). | **Sources pending.** Enter at the B1c run. |

**Open edge (what would solve it):**
1. A measured **plasma-membrane-resident sensor of packing** (B1b currently has PM tension via Piezo, but its packing sensors are ER- or curvature-associated).
2. The author's ruling on **MF-02**, which decides whether B1a is sensing.
3. Sources for B1c.
4. A check of whether composition control at the plasma membrane acts only through supply (B2) or also through in-place sensing (B1b).

### MG-03 — DETECT covered only chemical signals — **solved**

**Found by:** the L0 DETECT row lists chemical, physical, contact and self inputs. The first inventory had receptors for chemical signals only.

**Fill:** E2 mechanical (Piezo, source as in MG-02), E3 thermal and osmotic, D3 voltage sensing. **Open edge:** sources for E3 and D3 are pending; they enter at the E and D runs.

### MG-04 — RESPOND had no outward signals beyond secretion — **solved (one source pending)**

**Found by:** the L0 RESPOND row ("what is released") had only exocytosis behind it.

**Fill:**
- **G2, extracellular vesicles that bud from the plasma membrane (ectosomes).** Source: Théry et al. 2018 (MISEV2018), *J. Extracell. Vesicles* 7:1535750, [doi:10.1080/20013078.2018.1535750](https://doi.org/10.1080/20013078.2018.1535750). That paper names ectosomes and microvesicles among cell-released membranous structures.
- **G3, lipid-derived mediators released from membrane lipids.** Source pending: the G run must supply one.

### MG-05 — Three structural categories missing — **solved**

**Found by:** applying L2's "what is handled" split (matter, charge, information, contact, **shape**). Nothing in the first inventory handled shape, position on the surface, or passage straight through the cell.

**Fill:** category **I** (shape, mechanics, motility), category **J** (spatial organization: domains, polarity, cilium), item **C7** (transcytosis). Sources enter at each run.

### MG-06 — Protein supply missing — **solved**

**Found by:** category B (self-maintenance) listed lipid supply but not protein supply. A plasma-membrane protein's orientation is fixed when it is inserted in the ER, before it reaches the surface.

**Fill:** B3. A source enters at the B run.

### MG-07 — ER–plasma-membrane contact sites missing — **solved**

**Found by:** asking how lipids and signals reach the membrane other than by vesicles.

**Measured instance:** store-operated Ca²⁺ entry. An ER Ca²⁺ sensor, STIM1, couples to a plasma-membrane channel, Orai1, when ER Ca²⁺ stores are depleted.
- Liou et al. 2005, *Curr. Biol.* 15:1235, [doi:10.1016/j.cub.2005.05.055](https://doi.org/10.1016/j.cub.2005.05.055)
- Feske et al. 2006, *Nature* 441:179, [doi:10.1038/nature05122](https://doi.org/10.1038/nature05122)

**Fill:** J4.

**Cross-check:** this is a DETECT in one membrane (ER) driving a RESPOND in another (plasma membrane). The membrane's loop is not closed inside the plasma membrane alone. That is a scope note for the whole atlas: the membrane areas will need cross-links.

### MG-08 — The membrane's electrical property missing — **solved**

**Found by:** category D (electrical) had potentials but not the physical property that holds them.

**Measured:** specific membrane capacitance 0.9 µF/cm². The value is the same for all three neuron classes measured. Gentet, Stuart & Clements 2000, *Biophys. J.* 79:314, [doi:10.1016/S0006-3495(00)76293-X](https://doi.org/10.1016/S0006-3495(00)76293-X). Grade: measured-single for this value; whether it holds across eukaryotic cell types is **held open**, hence the "U?" tag.

**Fill:** A4.

### MG-09 — No whole-membrane level — **solved**

**Found by:** the user's review. The first inventory started at mechanism level, and the pilot jumped straight to one molecule.

**Fill:** levels L0–L4, with the rule that runs go top-down. Run 01 is re-filed as an L4 leaf under C (exchange) → C3 (primary active) → P-type ATPases.

### MG-10 — Scope tags are coarse and unchecked — **held open**

Several items are tagged **?**. Protists are not yet represented.

**Data that would narrow it:** a per-lineage presence check for each L3 family (animals, plants, fungi, at least one protist group).

---

## Framework / method gaps (MF)

### MF-01 — Deep-Lens steps E, F, J assume an operator — **needs decision**

Found in [run 01](run-01-na-k-pump.md). It applies to every molecular and membrane-level run, including L0: nothing measured shows an operator at the membrane scale either.

**Options:**
1. A scale-scoped Deep-Lens that marks E, F and J "not applicable below operator scale" (recommended).
2. Run E, F and J one scale up.
3. Keep stopping at E.

### MF-02 — What counts as PROCESS? — **held open; bears on canon Stage 12**

Canon Stage 12 reads: *"First boundary between inside and outside. Detection becomes possible because there is now a self."*

A **protein-free** lipid bilayer responds to its surroundings physically. For example, it changes phase with temperature and swells under osmotic stress. Is that DETECT → PROCESS → RESPOND, or a direct physical response with no PROCESS step?

The base code does not define a minimum PROCESS. Without that definition, the boundary for "detection becomes possible" can't be placed: it could sit at the bare bilayer (Stage 12 as written) or at the first membrane protein that gates a response.

**Proposed criterion (derivation, for the author):** PROCESS is present when the output depends on an internal state that can change independently of the input, as in gating. Under that criterion, the Na+/K+ pump's Na+-gated phosphorylation qualifies (run 01, step 2). Whether a bare bilayer qualifies is **not decided here**. The physical measurements of bare bilayers belong to the A3 run.

**Not filled.** Stage 12 is not edited.

### MF-03 — No decomposition rule in canon — **solved by derivation, awaiting author**

The Master Meta-Algorithm locates a domain, but no algorithm says how to split a system into sub-processes. The L0–L4 rule in [`README.md`](README.md) is the proposed derivation: split by base-code role, plus substrate, self-loop and lifecycle, then by what is handled, then by mechanism family. If the author accepts it, it is reusable for every cell area and at other scales.

### MF-04 — Three Kingdoms placement below the cell — **held open**

v5.1 Domain 9 places "homeostatic regulatory intelligence" in the Third Kingdom, at the level of the cell or organism. What, if anything, is Third Kingdom at the scale of a membrane process is not stated. **Not filled.**

### MF-05 — No rule for counting loops — **held open**

Run 01 found **two** DETECT events per pump cycle (Na+ inside, K+ outside). MG-07 found one loop spanning **two** membranes (ER and plasma membrane).

The base code does not say whether one physical cycle is one loop, or how to treat a loop that spans components. Patterns that count loops cannot be compared across runs until this is fixed.

---

```
Source: GFunnel Methodology (Omni Process) v5.1/v5.2, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0.
Adapted; not endorsed by the author.
```
