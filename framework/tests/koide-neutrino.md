# Test 1b — "Then neutrinos": the Koide form applied to neutrino masses

**v5.4 §14, item 1** ends *"…then neutrinos."* [`koide-delta.md`](koide-delta.md) held this step open: *"not runnable — absolute neutrino masses are unmeasured."* **It is runnable.** The Brannen form forces Q = 2/3 for any δ; oscillation experiments measure two mass gaps; three masses under two gaps plus Q = 2/3 leave nothing free. This file runs it and writes the result down **before** the deciding data arrives.

Script: [`koide_neutrino.py`](koide_neutrino.py) · standard library only · NuFIT 5.3 (2024) oscillation fits · DESI 2024 cosmology limit.

> **Status: live hypothesis, recorded as a dated prediction (2026-11-23).** Not canon. It is the framework's first candidate *novel* prediction: a number mainstream physics does not supply.

---

## Result

| | Normal ordering | Inverted ordering |
| --- | --- | --- |
| Solution exists? | **yes**, with one negative root (signs −, +, +) | yes, with one negative root (signs +, +, −) |
| m₁ / m₂ / m₃ (eV) | **3.6×10⁻⁴ / 8.6×10⁻³ / 5.01×10⁻²** | 4.93×10⁻² / 5.01×10⁻² / 2.9×10⁻³ |
| Sum of masses | **0.0591 eV** | 0.102 eV |
| Against cosmology (Σ < 0.072 eV, DESI 2024) | **allowed** | **excluded** |
| δ (Brannen phase) | 0.478 rad | — |

With all-positive roots there is **no** solution in either ordering. Propagating the 1σ oscillation errors:

```
m1    = 3.45e-4 … 3.75e-4 eV
sum   = 0.0587 … 0.0595 eV      (normal-ordering floor with m1 = 0: 0.0587 eV)
delta = 0.472 … 0.483 rad
```

**Prediction:** normal ordering; lightest mass ≈ 3.6×10⁻⁴ eV; sum ≈ 0.059 eV.

## Cautions that travel with it

1. **The negative root is a stipulation.** Nothing in canon forces which root carries the sign. It is the same freedom Brannen used (2006). Without it, the form fails for neutrinos outright, which is itself worth recording.
2. **The prediction sits just above the normal-ordering floor** (0.0591 vs 0.0587 eV). Cosmology alone cannot separate "Koide" from "m₁ = 0" for years; the sharp discriminator is the **ordering**.
3. **The phase does not repeat 2/9.** δ_ν ≈ 0.478 rad, not 2/9 = 0.222. It lies near Brannen's conjecture δ_ν = 2/9 + π/12 = 0.484 rad (just outside the 1σ band above). Whether the trefoil reading forces any offset is **open**; the canon's partition = phase reading (§4a.5) would need to say why neutrinos shift.
4. **The form is not original to the framework** (Koide 1981; Brannen 2006). What the framework adds is the reading and the commitment to the number in advance.

## Falsifiers (dated)

- **JUNO reports inverted ordering** (expected around 2029–2032) → **forced-no.**
- **Cosmology measures Σ outside ≈ 0.058–0.065 eV**, once Euclid + CMB reach ~±0.02 eV → forced-no.
- **A direct measurement of m₁ well above 10⁻³ eV** → forced-no.

## Ledger movement

| Narrowed | Newly opened | Status |
| --- | --- | --- |
| §14 item 1 "then neutrinos" run: normal ordering, Σ ≈ 0.059 eV, positive-root form fails; inverted solution excluded by cosmology | why the negative root; why δ_ν ≠ 2/9 (offset ≈ π/12?) | ◐ live, dated |

---

*Source: GFunnel Methodology (Omni Process) v5.4, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. The neutrino run is a derivation from it, not endorsed by the author.*
