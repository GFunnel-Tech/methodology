---
id: PRED-005
target: "The neutrino mass ordering and the sum of the three neutrino masses"
organism: "n/a — particle physics"
framework_route: "v5.4 §6 (mass spectrum: Brannen form, partition = phase per §4a.5) and §14 item 1 'then neutrinos'; branches selected by v5.4 §3 closure (a branch that oversteps a measured boundary unties) and weighted by Bayesian updating"
prediction_kind: quantitative
tolerance: "Ordering: HIT if normal ordering is established at >=5 sigma, or by >=2 independent methods (reactor, accelerator, atmospheric) at >=3 sigma each; MISS on the same bar for inverted. Sum: HIT if a cosmological or direct measurement places the sum within 0.055-0.065 eV at 68% confidence; MISS if the 95% interval excludes 0.0591 eV. Paired rule: inverted ordering scores PARTIAL only if the sum is then measured at 0.102 +/- 0.01 eV, otherwise MISS."
contamination_risk: high
discriminating: partial
lookup_status: withheld
phase_a_commit: null
verdict: null
---

## Target

Which way the three neutrino masses are ordered (normal: m₁ < m₂ < m₃; inverted: m₃ lightest), and the sum of the three masses. Neither is measured at the time of sealing. Oscillation experiments measure only the two squared-mass gaps, which are used here as inputs.

## Framework route (the algorithm, run literally — numbered steps, no skipping)

1. **Form (v5.4 §6, §4a.5):** three masses as three phases of one mode, √mₖ = μ[1 + √2 cos(2πk/3 + δ)]. This forces Koide's Q = 2/3 for any δ.
2. **Inputs (reality filter item 5, measurements only):** the two oscillation gaps, NuFIT 5.3 (2024): Δm²₂₁ = 7.41×10⁻⁵ eV², Δm²₃₁ = 2.511×10⁻³ eV² (normal) / Δm²₃₂ = −2.498×10⁻³ eV² (inverted).
3. **Solve:** three masses, two gaps and Q = 2/3 leave no free number. Every sign pattern of the roots, in both orderings, is tried (`framework/tests/koide_neutrino.py`).
4. **Closure (v5.4 §3):** a branch persists until it reaches a boundary it cannot pass. All-positive roots: no solution in either ordering, so it unties. δ fixed at 2/9: inconsistent with the gaps, so it unties. Inverted ordering with one negative root: sum 0.102 eV oversteps the cosmology cap (Σ < 0.072 eV, DESI 2024), so it is strongly disfavoured but not removed (reality filter item 8: the cap is contested). Normal ordering with one negative root: inside every boundary.
5. **Weighting:** each measurement multiplies a branch's weight by its compatibility, then renormalise. Cosmology favours normal by ~6×; oscillation data by 1.7× to 23× (1–2.5σ, the dataset dispute). Result P(normal) = 0.91–0.99.
6. **Anti-Operation:** the fill opens two gaps: why one root is negative, and why δ_ν ≈ 0.478 rad rather than 2/9.

## Derivation trace

Script output (reproduce with `python3 framework/tests/koide_neutrino.py`):

```
normal   signs (-,+,+): m1=3.598e-4  m2=8.616e-3  m3=5.011e-2 eV   sum=0.0591 eV   delta=0.478 rad
inverted signs (+,+,-): m1=4.932e-2  m2=5.007e-2  m3=2.925e-3 eV   sum=0.1023 eV   (excluded by cosmology cap)
1-sigma propagation of the gaps: m1 3.45-3.75e-4 eV, sum 0.0587-0.0595 eV, delta 0.472-0.483 rad
P(normal) = 0.911 / 0.950 / 0.993 for an oscillation preference of 1.0 / 1.5 / 2.5 sigma
```

## Prediction

**Normal ordering. Sum of masses 0.0591 eV (0.0587–0.0595). Lightest mass 3.6×10⁻⁴ eV. Weight on normal ≈ 95% (91–99%).** Paired branch, held at ≈ 5%: inverted ordering with sum 0.102 eV.

## Tolerance (what counts as a hit / a miss)

As in the front matter. The ordering bar requires independent confirmation so that a single experiment's systematic error cannot settle it either way.

## Framework-free default (what you would say without the framework)

- **Ordering:** current global fits already lean normal at 1–2.5σ. A framework-free forecaster would also say "normal, probably". **The ordering part is non-discriminating.**
- **Sum:** a framework-free forecaster would give the allowed band, 0.0587–0.072 eV for normal ordering, with no preferred value. The prediction picks a point (0.0591 eV) one-twentieth of the way into that band. **The sum part is discriminating**, but cosmology at ±0.02 eV cannot separate 0.0591 from the 0.0587 floor for years.

## Contamination disclosure

Graded **high**. The formula is Koide's (1981) and Brannen's (2006), and Brannen published neutrino masses from the same form with a negative root. The executor is a language model trained on that literature and may have recalled the structure of the answer. The numbers here were computed from current (2024) inputs, not copied, and the paired branch and weights are new to this record, but the route was not independent of the published one. Per the protocol, the honest re-run is by the author: seal a prediction without the executor, then compare.

<!-- PHASE B BELOW THIS LINE — must be empty when Phase A is committed -->
