# Run 01 — The Na+/K+ Pump (Na+,K+-ATPase)

> **Status: derivation / pilot run. Not canon.** No primary algorithm exists for this mechanism. The framework mapping below is derived from the v5.2 Deep-Lens Protocol (§1, steps A–L). The measured and derived tiers stand on their own sources and do not depend on the mapping.
>
> **Run outcome: stopped at Deep-Lens step E** (blocker logged below). Steps A–D are complete. Steps F–L were not run in the framework tier.

**Position in the breakdown:** L4 leaf — C (exchange) → C3 (primary active transport) → P-type ATPases → Na+/K+ pump **(animals only)**. See [README](README.md). *Run out of order as a pilot of the run format. The parent runs (L0, L1 C, L2 C3) come first. The plant and fungal sibling is the H+ pump ([gaps.md](gaps.md) MG-01).* · **Canon anchor:** v5.1 Appendix A Stage 24 (Ion Gradients / Membrane Potentials); Stage 23 (ATP Hydrolysis / Cellular Work); Domain 9 (Biological).

---

## Tier 1 — Measured

| # | Quantity | Value | Uncertainty | Grade | Source |
| --- | --- | --- | --- | --- | --- |
| M1 | Activity of the membrane ATPase depends on Na+ **and** K+ together | qualitative | — | measured-reproduced | Skou 1957, [doi:10.1016/0006-3002(57)90343-8](https://doi.org/10.1016/0006-3002(57)90343-8) |
| M2 | Coupling ratio per ATP hydrolysed (animal cells) | 3 Na+ out : 2 K+ in : 1 ATP | constant across ionic conditions, methods, cell types and tissues (as reviewed) | measured-reproduced | Post & Jolly 1957 (*Biochim. Biophys. Acta*); reviewed in Peluffo & Hernández 2023, [doi:10.1007/s12551-023-01082-5](https://doi.org/10.1007/s12551-023-01082-5) |
| M3 | Net charge moved per cycle; pump current depends on voltage | 1 positive charge out per cycle; pump current falls steadily from a maximum near 0 mV to very small at −140 mV (guinea-pig ventricular myocytes) | as published | measured-reproduced | Gadsby et al. 1985, *Nature* 315:63, [doi:10.1038/315063a0](https://doi.org/10.1038/315063a0) |
| M4 | Ion-binding sites captured in an occluded state (no open path to either side) | atomic structure, PDB 3B8E | crystallographic | measured-single | Morth et al. 2007, *Nature* 450:1043, [doi:10.1038/nature06419](https://doi.org/10.1038/nature06419) |
| M5 | Coupling ratio of the brine-shrimp α2KK variant (up-regulated in extreme salinity) | 2 Na+ : 1 K+ per cycle | as published | measured-single | Artigas et al. 2023, *PNAS*, [doi:10.1073/pnas.2313999120](https://doi.org/10.1073/pnas.2313999120) (⁸⁶Rb⁺ uptake under voltage clamp) |
| M6 | Share of ATP-coupled O₂ use spent by this pump | whole body (mammal) 19–28%; brain 50–60%; kidney 40–70% | ranges as published | derived (compiled from inhibitor studies) | Rolfe & Brown 1997, *Physiol. Rev.* 77:731, [doi:10.1152/physrev.1997.77.3.731](https://doi.org/10.1152/physrev.1997.77.3.731) |
| M7 | Maximum turnover | 150 s⁻¹ | not given | derived (computed from ATPase activity *assuming* 3:2:1) | [BioNumbers 104181](https://bionumbers.hms.harvard.edu/bionumber.aspx?id=104181), citing Jørgensen 1974, *Biochim. Biophys. Acta* 356:36. The entry is labelled "beef brain" but cites a kidney purification paper — unresolved, see Open edge. |
| M8 | Representative mammalian inputs (37 °C) | [Na+] in 15 / out 140 mM; [K+] in 120 / out 4 mM; ΔG(ATP) −54.0 kJ/mol; resting Vm −85 to −75 mV | representative, varies by cell type | measured-reproduced (typical ranges) | as tabulated in Peluffo & Hernández 2023 (M2) |

All values retrieved 2026-10-02. Interpretive wording in the sources (for example, the review's claim that 3:2 was *selected by evolution* for efficiency) is **not** carried into this tier. It goes to the Open edge.

---

## Tier 2 — Derived

### Equation — work per cycle vs. the fuel per cycle

Free energy the pump must supply per mole of cycles, moving *n*Na Na+ out and *n*K K+ in across a membrane at potential *V*m (inside relative to outside):

```
W = nNa · RT · ln([Na]out / [Na]in)
  + nK  · RT · ln([K]in  / [K]out)
  − (nNa − nK) · F · Vm

The cycle can run only while  W ≤ |ΔG(ATP)|.
Stall voltage:  Vm* = −( |ΔG(ATP)| − W(0) ) / ((nNa − nK) · F)
```

**Trace.** Each Na+ climbs its concentration gradient (first term). Each K+ climbs its own (second term). The net charge moved out per cycle, (nNa − nK), crosses the voltage. With the inside negative, that costs energy (third term). This is the standard electrochemical-potential sum. It uses only M2, M3 and M8.

**Reproduced** by [`../scripts/na_k_pump_energetics.py`](../scripts/na_k_pump_energetics.py) (stdlib only; asserts against the source's published values):

| Stoichiometry | W at 0 mV | W at −50 mV | W at −80 mV | Share of ATP used at −80 mV | Stall Vm |
| --- | --- | --- | --- | --- | --- |
| **3 Na : 2 K** (measured, M2) | 34.82 | 39.65 | 42.54 | 79% | −198.8 mV |
| 4 Na : 3 K (hypothetical) | 49.35 | 54.18 | 57.07 | >100% — cannot run | −48.2 mV |
| 4 Na : 2 K (hypothetical) | 40.58 | 50.23 | 56.02 | >100% — cannot run | −69.5 mV |
| 2 Na : 1 K (measured in brine shrimp, M5) | 20.29 | 25.11 | 28.01 | 52% | −349.4 mV |

kJ/mol of cycles. The brine-shrimp row uses **mammalian** concentrations only to show the trade-off. Its real operating point needs brine-shrimp concentrations, which this run does not have (see Open edge).

**Derived reading (forced by the equation, no narrative):** fewer ions per ATP means more free energy per ion moved, so the pump can hold a steeper gradient before stalling. More ions per ATP means more throughput per ATP but a shallower maximum gradient. The 3:2 ratio leaves headroom far below the resting potential (stall at about −199 mV against a resting Vm of −75 to −85 mV). The ratios 4:3 and 4:2 would stall within or above the normal resting range.

### Algorithm — the reaction cycle (Post–Albers), as numbered steps

From the cycle as reviewed in Peluffo & Hernández 2023 (M2), with the occluded state confirmed structurally (M4):

1. **E1, open to the inside:** bind MgATP and 3 Na+ from the cytoplasm.
2. **Gate:** phosphorylation of the enzyme's aspartate happens only once Na+ is bound. The 3 Na+ become occluded (no path to either side).
3. Release ADP.
4. **Switch to E2P, open to the outside:** de-occlude and release 3 Na+ to the outside.
5. Bind 2 K+ from the outside.
6. **Gate:** K+ binding drives dephosphorylation. The 2 K+ become occluded.
7. Release inorganic phosphate.
8. **Switch back to E1, open to the inside:** release 2 K+ into the cytoplasm. Return to step 1.

Net per cycle: 1 ATP spent; 3 Na+ out; 2 K+ in; 1 positive charge out.

---

## Tier 3 — Framework mapping (Deep-Lens, v5.2 §1) — derivation

**A. NAME & REFRAME.** *Surface:* a transporter that moves sodium out and potassium in. *Function:* a converter. It turns one store of free energy (ATP) into another (two ion gradients plus a voltage) at a fixed exchange rate (M2). Other membrane processes then spend that second store: secondary transport, electrical signalling, volume control. Those are queued as membrane items 2.6, 3.1–3.2 and 2.7, and their runs must confirm the dependency. It works like a battery charger more than a doorway.

**B. STRUCTURE.** The base code maps, but **as two half-loops per cycle, not one**:

| | Half-loop 1 (inside face) | Half-loop 2 (outside face) |
| --- | --- | --- |
| DETECT | 3 Na+ bound from inside (step 1) | 2 K+ bound from outside (step 5) |
| PROCESS | Phosphorylation, occlusion, conformational switch (steps 2–4) | Dephosphorylation, occlusion, switch back (steps 6–8) |
| RESPOND | 3 Na+ released outside (step 4) | 2 K+ released inside (step 8) → enzyme back in E1 = input state for the next cycle |

A third, slower loop runs at cell scale. The pump's output (the gradient and Vm) feeds back into the cost of its next cycle through the −(nNa − nK)·F·Vm term (M3). *Mapping note:* the doubled DETECT is a measured feature of the mechanism. It is recorded as a structural observation about how the base code fits here, not smoothed into one loop.

**C. PLACEMENT.**
- **Kingdom:** First. The pump is cellular machinery, which the v5.1 Domain 9 row places in the First Kingdom. The gene encoding it sits in the Second.
- **Domains:** 9 (Biological) and 8 (Chemical).
- **Operative Hermetic principle:** Polarity. Canon already files gradient establishment and collapse under Polarity (v5.1, the Energy Continuation section on the ETC, and Stage 24).
- **Principle whose violation produces the characteristic failure:** Polarity. With the pump stopped, the gradient it maintains is no longer renewed. *The rate at which the gradient then runs down is not measured in this run; it is held for run 3.1 (resting potential).*

**D. GRADIENT & DYNAMIC MIDDLE.**
- **Gradient consumed:** ATP hydrolysis, about −54 kJ/mol (M8).
- **Gradient established:** Na+ and K+ concentration gradients plus about one charge per cycle of voltage.
- **Yang extreme (overextension):** a ratio or a voltage that demands more than one ATP supplies. Hypothetical 4:3 stalls at −48 mV, which is inside the normal operating range, so it cannot run (Tier 2). The energy bill is also heavy where demand is high: 50–60% of ATP-coupled O₂ in brain (M6).
- **Yin extreme (paralysis):** pump not running; the gradient is not renewed.
- **Middle (derived numerically):** 3:2 runs at about 64–79% of ATP's free energy between 0 and −80 mV, with headroom to about −199 mV. Brine shrimp shift the middle (2:1, M5) when the outside becomes extreme. The middle is a tuned, measurable operating point, and it moves when the environment moves.

**E. FORCED vs. GUIDED — ⛔ BLOCKED. Run stops here.**

Step E asks what the mechanism looks like "run on the operator (guidance refused) vs. received in participation." That requires an operator able to receive or refuse guidance. No measurement in Tier 1 shows such an operator at the scale of a single protein. Filling the step anyway would mean importing intent into a molecule. That fills a held-open variable with assumption, which AGENTS.md rule 5 and the Variable Principle forbid.

Per the invariant run form, **the run stops at E. The blocker is the location of the work.**

**Blocker, named:** *Deep-Lens steps E, F (keys and doors: Decode / Drown / Numb), and J (the operator's act-vs-ruminate choice) are written for a scale where an operator exists. The protocol does not say how to run them on a sub-cellular mechanism.* Every molecular process in this atlas will hit the same blocker, so it has to be resolved once, before the atlas scales.

**F–L: not run.** Preview only, not results: G (boundary class), H (failure mode), I (falsifiability and variable ledger), K (correspondence) and L (document) do not appear to need an operator and could run as written.

---

## Patterns extracted

From the **measured and derived tiers only**. These do not depend on the blocked framework steps. Added to [`../patterns.md`](../patterns.md).

| ID | Pattern | Grounding |
| --- | --- | --- |
| P-01 | **Gated commitment.** The cycle spends energy only after its input is fully detected (phosphorylation needs 3 Na+ bound). | M2 review, step 2 |
| P-02 | **Alternating access.** The gate is never open to both sides at once; the cargo is held (occluded) during the switch. | M4, steps 2 and 6 |
| P-03 | **Fixed-rate conversion.** One energy store is converted to another at an integer exchange rate (1 ATP → 3 Na+ + 2 K+). | M2 |
| P-04 | **Ratio vs. ceiling trade-off.** Units moved per unit of fuel trade against the maximum gradient that can be held. | Tier 2 equation; M5 is the measured instance |
| P-05 | **Self-loading output.** The output (voltage) feeds into the cost of the next cycle. | M3; the Vm term |

---

## Container-ready block (not yet a container)

- **name:** "Na+/K+-ATPase: 3 Na+ out, 2 K+ in per ATP; work per cycle vs. ΔG(ATP)"
- **status:** forced-fill, **for the measured mechanism and the derived equation only**. The Tier 3 mapping is not part of the container.
- **form:** both. Equation and Trace are in Tier 2; Algorithm is the 8-step cycle.
- **canon_refs:** v5.1 Appendix A Stage 24, Stage 23; v5.1 Domain 9
- **diff state vs. Stage 24:** `accounted`. Reality shows the pump establishing Na+/K+ asymmetry, as the stage says. *Narrative stripped:* "Polarity **deliberately** created and maintained." Nothing measured forces "deliberately," so it is flagged for the Reality Audit label phase, not changed here.

## Open edge

1. **Deep-Lens blocker (steps E, F, J at molecular scale).** This needs a decision before the atlas scales.
2. **Brine-shrimp operating point.** The α2KK pump's real stall voltage needs measured brine-shrimp intra- and extracellular concentrations and Vm.
3. **Turnover source mismatch (M7).** The BioNumbers entry says "beef brain" but cites a kidney purification paper, and the value assumes 3:2:1. Find a direct measurement.
4. **"Why 3:2?"** The review argues 3:2 was selected for efficiency and headroom. The equation shows that 3:2 *has* headroom; it does not show that headroom is *why* 3:2 exists. That stays held open.
5. **Gradient run-down rate when the pump stops.** Unmeasured here; held for run 3.1.

## Re-formation log

- 2026-10-02 — Created. Pilot run of the Cell Atlas. Tiers 1–2 complete and reproduced by script; Tier 3 stopped at step E.

```
Source: GFunnel Methodology (Omni Process) v5.1/v5.2, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0.
Framework steps applied (adapted) to a mechanism canon does not name; not endorsed by the author.
```
