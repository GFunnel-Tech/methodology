# Test 1c — Paired branches, weights and the decision rule (addendum to test 1b)

The neutrino half of v5.4 §14 item 1 was **first run on 2026-10-31** in [`koide-neutrino.md`](koide-neutrino.md) (script [`koide_neutrino.py`](koide_neutrino.py)): exact form forced-no; signed form predicts normal ordering and Σm_ν ≈ 0.059 eV. This addendum, from 2026-11-23, reran it independently with older inputs and added three things the first run does not have: **both branches with weights**, a **decision rule fixed before data**, and the **sealed prediction record** [`../../audit/prediction/PRED-005.md`](../../audit/prediction/PRED-005.md).

Script: [`koide_neutrino_weights.py`](koide_neutrino_weights.py) · standard library only. With no argument it uses the 2026-10-31 inputs (NuFIT 6.0, DESI DR2 cap 0.064 eV); with `--pred005` it uses the inputs sealed in PRED-005 (NuFIT 5.3, DESI 2024 cap 0.072 eV).

> **File history.** PRED-005 cites `framework/tests/koide_neutrino.py`. That was this script's name when PRED-005 was sealed. It was renamed when the 2026-10-31 run was merged, so that run keeps its file. The sealed version is recoverable exactly: `git show 168156c:framework/tests/koide_neutrino.py`.

---

## Both runs agree

| | 2026-10-31 run (NuFIT 6.0, DESI DR2) | 2026-11-23 run (NuFIT 5.3, DESI 2024) |
| --- | --- | --- |
| Positive-root form | forced-no | no solution |
| Normal ordering, one negative root | Σ = 0.0592 eV, δ = 0.4793 | Σ = 0.0591 eV, δ = 0.478 |
| Inverted ordering, one negative root | Σ = 0.1020 eV, excluded | Σ = 0.1023 eV, excluded |

## Paired branches and their weights

The formula ties ordering to the sum, so both branches are recorded, each with its own number:

| Branch | Sum | Weight, current inputs | Weight, PRED-005 inputs |
| --- | --- | --- | --- |
| Normal | 0.059 eV | ≈ 97% (94–99.6%) | ≈ 95% (91–99%) |
| Inverted | 0.102 eV | ≈ 3% (0.4–6%) | ≈ 5% (1–9%) |

Weights come from multiplying each branch by its compatibility with current measurements (cosmology cap ~10× for normal with the DR2 cap, ~6× with the 2024 cap; oscillation data 1.7–23× for normal, the spread being the dataset dispute), then renormalising. The script prints them.

**Decision rule (fixed before data):** the prediction fails if inverted ordering is established at ≥5σ, or by ≥2 independent methods at ≥3σ each, unless the sum is then measured at 0.102 ± 0.01 eV. It is confirmed by the same bar for normal ordering together with a sum inside 0.055–0.065 eV.

## Cautions that travel with it

1. **The negative root is a stipulation.** Nothing in canon forces which root carries the sign. It is the same freedom Brannen used (2006). Without it, the form fails for neutrinos outright, which is itself worth recording.
2. **The prediction sits just above the normal-ordering floor** (0.0591 vs 0.0587 eV). Cosmology alone cannot separate "Koide" from "m₁ = 0" for years; the sharp discriminator is the **ordering**.
3. **The phase does not repeat 2/9.** δ_ν ≈ 0.478 rad, not 2/9 = 0.222. It lies near Brannen's conjecture δ_ν = 2/9 + π/12 = 0.484 rad (just outside the 1σ band of the 2026-11-23 run, 0.472–0.483). Whether the trefoil reading forces any offset is **open**; the canon's partition = phase reading (§4a.5) would need to say why neutrinos shift.
4. **The form is not original to the framework** (Koide 1981; Brannen 2006). What the framework adds is the reading and the commitment to the number in advance.

## Falsifiers (dated)

- **JUNO reports inverted ordering** (expected around 2029–2032) → **forced-no.**
- **Cosmology measures Σ outside ≈ 0.058–0.065 eV**, once Euclid + CMB reach ~±0.02 eV → forced-no.
- **A direct measurement of m₁ well above 10⁻³ eV** → forced-no.

## Regrading and what the calculation was missing (added later on 2026-11-23)

The sealed record is not edited; these notes sit below it.

1. **Non-discriminating.** PRED-005 graded the sum as discriminating. It is not: the framework-free guess "normal ordering, lightest ≈ 0" gives Σ = 0.0587 eV, 0.0004 eV from 0.0591 eV, far below any planned sensitivity (cosmology ≈ ±0.01–0.02 eV). The whole prediction is non-discriminating as it stands.
2. **Borrowed.** Under the acceptance gate (`skills/gfunnel-methodology/workflows/accept.md`) the form, the negative root and the phase are non-self (Koide 1981, Brannen 2006). The prediction is public and dated as a borrowed prediction, not the methodology's own.
3. **The cosmology cap is model-dependent.** The 0.064 eV cap assumes constant dark energy. With evolving dark energy (DESI w₀wₐ fits) it loosens to roughly 0.12–0.20 eV, which would readmit the inverted branch (0.102 eV). The ≈97% weight assumes constant dark energy.
4. **The weighting is crude.** The cap is modelled as a half-Gaussian at zero; the actual DESI likelihood prefers a sum below the oscillation floor, which disfavours both branches.
5. **Implied quantities, computed now** (NuFIT 6.0 mixing): m_ββ = 1.3–4.0 meV (range from the unknown Majorana phases), m_β = 8.8 meV. Both are far below LEGEND-1000 (~9–20 meV) and Project 8 (~40 meV), so the double-beta falsifier of test 1b is not testable soon.
6. **What would make it discriminating:** a canon-derived phase shift Δ = δ_ν − δₑ, sealed before JUNO's precision result, predicts the gap ratio Δm²₃₁/Δm²₂₁ (measured 33.55 ± ~1.0; JUNO to ~0.4%). For reference only, Brannen's external rule Δ = π/12 gives 32.43. See [`../../substrate/2026-11-23-gap-network.md`](../../substrate/2026-11-23-gap-network.md).

## Ledger movement

| Narrowed | Newly opened | Status |
| --- | --- | --- |
| §14 item 1 "then neutrinos" run: normal ordering, Σ ≈ 0.059 eV, positive-root form fails; inverted solution excluded by cosmology | why the negative root; why δ_ν ≠ 2/9 (offset ≈ π/12?) | ◐ live, dated |

---

*Source: GFunnel Methodology (Omni Process) v5.4, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. The neutrino run is a derivation from it, not endorsed by the author.*
