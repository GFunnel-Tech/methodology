# Test 1b — The Neutrino Half of the Koide Run

**v5.4 §14, item 1, second clause:** *"…then neutrinos."* The charged-lepton half is [`koide-delta.md`](koide-delta.md) (a hit, with four cautions). This file runs the neutrino half.

Script: [`koide_neutrino.py`](koide_neutrino.py) · standard library only · NuFIT 6.0 (2024) splittings · DESI DR2 (2025) cosmological bound.

*Run 2026-10-31 under the container frame of [`../../substrate/2026-10-31-container-superposition.md`](../../substrate/2026-10-31-container-superposition.md) (substrate, unclassified).*

---

## Inputs

| Quantity | Value | Tag |
| --- | --- | --- |
| Δm²₂₁ | 7.49 × 10⁻⁵ eV² | measured (NuFIT 6.0) |
| Δm²₃₁ (NO) | +2.513 × 10⁻³ eV² | measured |
| Δm²₃₂ (IO) | −2.484 × 10⁻³ eV² | measured |
| Σm_ν bound | < 0.064 eV (95 %) | measured (DESI DR2 + CMB, 2025) |

Absolute neutrino masses are **not** measured. The Brannen form has two free parameters (μ, δ); two splittings fix both. The form therefore *predicts* the absolute masses, with no freedom left.

---

## Result A — the charged-lepton container does not hold the neutrinos (forced-no)

With all three `√m` positive — the only case in which Koide's `Q = 2/3` holds exactly — every factor `1 + √2 cos(2πk/3 + δ)` must be positive, which confines δ to `|δ| < π/12`. Inside that window the μ-independent ratio `R = (m₃² − m₁²)/(m₂² − m₁²)` ranges over:

| Ordering | Available R | Measured R |
| --- | --- | --- |
| NO | [194.5, ∞) | 33.55 |
| IO | [1.000, 1.005] | 33.16 |

**No δ reproduces either ordering.** The exact Koide form that fits the charged leptons at δ = 2/9 is forced-no for the neutrino triplet. [forced]

## Result B — one root negative: one solution per ordering

Allowing one `√m` negative (Brannen 2006; Q with positive roots is then ≠ 2/3) gives exactly one mass set per ordering:

| Ordering | δ_ν (rad) | m₁, m₂, m₃ (meV) | Σm_ν | vs DESI DR2 |
| --- | --- | --- | --- | --- |
| NO | 0.4793 | 0.36 · 8.66 · 50.13 | **0.0592 eV** | survives (at the floor) |
| IO | 1.0419 | 2.92 · 49.17 · 49.93 | 0.1020 eV | **excluded** |

(The script reports each solution twice; the second root is the reflection δ ↦ 2π/3 − δ and yields the same masses.)

**Prediction carried forward:** Σm_ν = 0.059 eV, lightest neutrino ≈ 0.4 meV, normal ordering. [estimate · range ±0.002 eV from splitting uncertainties · falsifiers: Σm_ν measured above ~0.07 eV (Euclid/DESI final), or JUNO establishing inverted ordering]

Note δ_ν = 0.4793 against `2/9 + π/12 = 0.4840` — 1 % apart. Brannen's relation, not derived here. [conflict at 1 %; held-open]

---

## What the container frame adds (live hypothesis, not a derivation)

v5.4 §4a.2 reads a negative-frequency mode as *the line run backward — the anti-container*. Under the substrate frame, the neutrino triplet is one line with three closures, **one of which runs backward**. A container with a backward closure is its own anti-container. The one fermion that may be its own antiparticle is the neutrino (Majorana). This is a correspondence between the sign Brannen needed and the Majorana question, which physics has not connected to Koide.

- **Status:** live hypothesis.
- **Falsifier:** 0νββ searches (KamLAND-Zen, LEGEND) pushing m_ββ below the value this mass set permits for any Majorana phases, or a Dirac-nature result.
- **Not claimed:** that this derives the sign, the masses, or Majorana nature. Brannen's numbers are Brannen's. The reading is the only new line.

---

## Cautions

1. **Result B's hit is not evidence for the form.** Two parameters fit two numbers exactly by construction; the content is the third number (Σm_ν) and the ordering it selects.
2. **Result A is the stronger result** and it cuts against v5.4 §6: the "three generations as overtones of one knot" picture, as parametrized, does not transfer from charged leptons to neutrinos without a sign change. Gap 2 (the tension law) must produce that sign or the picture is two-pattern, not one.
3. NuFIT central values only; no error propagation beyond the stated range.

## Ledger movement

| # | Narrowed | Newly opened | Status |
| --- | --- | --- | --- |
| 13 (Gap 2) | exact Koide form forced-no for neutrinos; signed form predicts NO, Σm_ν ≈ 0.059 eV | why one closure runs backward; backward closure ↔ Majorana | ◐ |
