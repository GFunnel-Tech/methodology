# Test 5 — D1 Lamina Shield: First Engineering Estimate

**v5.4 §14, item 5:** *"D1 energy budget with fold storage — first engineering estimate."*
**v5.4 §8 states:** *"rifle round ~3 kJ → hundreds of tesla if field-only; plasma is the cheaper route."*

Script: [`d1_budget.py`](d1_budget.py) · standard library only.

---

## Result: the number is right; the stated reason is not

**"Hundreds of tesla" is confirmed** — but it does not follow from the 3 kJ figure. It follows from a *pressure* criterion that §8 does not state.

**The energy-density route (what "~3 kJ" invites) does not give that answer:**

| Interaction volume | u = KE/V (J/m³) | B (T) |
| --- | --- | --- |
| 1 m³ | 3.00×10³ | 0.09 |
| 1 L | 3.00×10⁶ | 2.75 |
| 0.1 cm³ | 3.00×10¹⁰ | 274.59 |

This only reaches hundreds of tesla at ~0.1 cm³, and it is the wrong criterion regardless: storing 3 kJ in a nearby field decelerates nothing.

**The pressure route does, and is correct.** A projectile is resisted when shield pressure meets its dynamic pressure `P = ½ρv²`:

| Projectile | P_dyn (Pa) | B required (T) |
| --- | --- | --- |
| 5.56 NATO | 4.42×10⁹ | **105** |
| 7.62 NATO | 3.53×10⁹ | 94 |
| 12.7 mm AP | 3.18×10⁹ | 89 |
| APFSDS (tungsten) | 2.30×10¹⁰ | **241** |

Against records of ~45 T continuous, ~100 T pulsed non-destructive, ~1200 T destructive: **small arms sit at the edge of pulsed-magnet practice; a tungsten long rod is beyond non-destructive practice.**

---

## A correction to §8's reasoning

§8 calls plasma "the cheaper route." **It is the only route.** A neutral projectile carries no charge and no current, so a magnetic field exerts no force on it at all — field-only stopping of an uncharged round is not expensive, it is impossible. The field's actual job is to *confine plasma*, and the plasma takes the momentum.

This strengthens the design's logic rather than weakening it, and it makes the recommendation forced rather than preferential. Suggested wording for a future version: *"plasma is forced; the field confines it."*

## Where the real gap is

Plasma must supply ~4.4 GPa of stagnation pressure:

| T (K) | n required (m⁻³) | % of solid density |
| --- | --- | --- |
| 10⁴ | 3.20×10²⁸ | 32.0 % |
| 10⁵ | 3.20×10²⁷ | 3.2 % |
| 10⁶ | 3.20×10²⁶ | 0.32 % |
| 10⁷ | 3.20×10²⁵ | 0.032 % |

The plasma-window precedent (Hershcovitch, BNL) operates near 1 atm — **a factor of ~44,000 below requirement.**

**Verdict: no physics prohibition. The binding constraint is confining a dense plasma at ~4 GPa** — a materials-and-power problem. This matches v5.4's own status for D1 ("physics-permitted, energy-bound, partial precedent") and now supplies the number behind it.

## On "fold storage collapses store and barrier into one structure" (§8)

Not evaluable yet. It depends on D2's open variable — a fold both deep and cheaply reversible — which v5.4 states does not currently exist (chemical is shallow/reversible, nuclear is deep/irreversible). **Held open**; the D1 estimate above assumes conventional stored energy.

---

## Ledger movement

| Narrowed | Newly opened | Status |
| --- | --- | --- |
| D1 quantified: ~105 T (small arms) to ~241 T (long rod) by pressure criterion; plasma shown **forced**, not preferred; gap to precedent is ~4×10⁴ in pressure | Dense-plasma confinement at ~4 GPa as D1's binding constraint; whether §8's energy-density framing should be replaced by the pressure criterion in canon | ◐ |
