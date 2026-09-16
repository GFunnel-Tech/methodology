# Test 1 — The Koide / δ = 2/9 Prediction Run

**v5.4 §14, item 1** (unchanged by §4a):** *"Run the Koide prediction: m_e in, δ = 2/9, trefoil form → m_μ, m_τ out; then neutrinos."*
**v5.4 §6 states the stakes:** *"A hit makes the model physics; a miss with a stated law makes it forced-no."*

Script: [`koide_delta.py`](koide_delta.py) · standard library only · PDG 2024 masses.

---

## Result: it is a hit

With **δ = 2/9 fixed exactly** and a single free scale μ, the Brannen form reproduces all three charged-lepton masses:

| Anchored on | Predicted | Observed | Error |
| --- | --- | --- | --- |
| m_e | m_μ = 105.6594145 | 105.6583755 | **+0.0010 %** |
| m_e | m_τ = 1776.98497 | 1776.93 | **+0.0031 %** |
| m_μ | m_e = 0.5109939 | 0.5109990 | −0.0010 % |
| m_μ | m_τ = 1776.96750 | 1776.93 | +0.0021 % |
| m_τ | m_e = 0.5109831 | 0.5109990 | −0.0031 % |
| m_τ | m_μ = 105.6561459 | 105.6583755 | −0.0021 % |

Fitting δ from data instead of assuming it:

```
δ (fitted)  = 0.2222265138 ± 0.0000103007   (1σ, from m_τ = 1776.93 ± 0.09 MeV)
2/9         = 0.2222222222
difference  = +4.29e-06  =  +0.42 σ
```

**δ = 2/9 is consistent with the measured lepton masses at 0.42σ.** The claim in v5.4 §6 survives its own stated test.

---

## Four cautions that must travel with this result

**1. Koide's 2/3 is built into the form and is not evidence for the trefoil.**
For `√m_k = μ(1 + √2 cos(2πk/3 + δ))`, the sums are `Σ√m = 3μ` and `Σm = 6μ²` for *any* δ, so `Q = 6μ²/9μ² = 2/3` identically. The famous 6 ppm agreement is a property of the parametrization, not a test passed by it. **All testable content is in δ.** v5.4 §6 presents "Koide 2/3 and δ = 2/9 matched" as two matches; it is one.

**2. The test is one number, matched post hoc.**
Three masses, two parameters (μ, δ) → one prediction, which is Koide. Fixing δ = 2/9 buys one more. So this is a genuine 2-prediction test — but δ = 2/9 was chosen *after* the masses were known. A post-hoc match of one number, however precise, is a **live hypothesis** under the framework's own Forcing Test (Test B, uniqueness, is not met: nothing forces the trefoil over any other structure yielding 2/9).

*Updated after §4a.* The **partition = phase** reframing (§4a.5) improves the picture without changing this verdict. The Brannen form *is* three phases 120° apart with offset δ, so reading the partition as phase rather than as spatial strands costs nothing and removes a false picture — it is the honest description of what this script actually computes. Test B is still unmet: the reframing says *what* the partition is, not *why there are three*. That needs the tension law.

§4a also lands a real **forced-no** in this sector, which this run confirms: generations as **integer harmonics** (1:2:3) fails outright — the measured ratios are **1 : 206.8 : 3477.4**. Ruling that out is a genuine narrowing, and it is the kind of result the framework should be logging.

**3. §6's dichotomy is too strong, and should be softened in a future version.**
*"A hit makes the model physics"* does not follow. This hit produces **no novel prediction** — it retrodicts three already-measured masses. It is fully consistent with v5.4 §7's own honest status line ("zero novel predictions"), and the two statements should be reconciled in canon. The miss branch is sound: a miss *would* have been forced-no.

**4. The conditioning is lopsided, which changes what counts as a sharp test.**

```
d ln(m_e)/dδ   = −51.49
d ln(m_μ)/dδ   =  +4.66
d ln(m_τ)/dδ   =  −0.26          m_e is 197× more sensitive than m_τ
```

m_e is the **sharpest probe** of δ, not the safest anchor. §14's phrasing ("m_e in → m_μ, m_τ out") runs the test in the direction that *hides* δ-error rather than exposing it. The stronger form of the test is the reverse: anchor on m_τ and check m_e, where a 1×10⁻⁵ error in δ shows up as a 5×10⁻⁴ error in m_e.

---

## The falsifier this creates (new, attached)

The test is **precision-limited by m_τ**, whose ±0.09 MeV uncertainty (5×10⁻⁵ relative) is the same order as the residual. This gives a sharp, dated falsifier:

> **If a future m_τ measurement moves the fitted δ more than 3σ from 2/9, the trefoil form is forced-no.**

At current precision δ sits 0.42σ away. A tau-mass measurement an order of magnitude tighter would either confirm δ = 2/9 at the 10⁻⁶ level or kill it. This is the cheapest decisive test the framework now has, and it depends on no new theory.

## What could not be run

**"Then neutrinos"** — not runnable. Absolute neutrino masses are unmeasured; oscillation gives only Δm² (and the ordering is unsettled). Koide-type relations for neutrinos are unconstrained in the absolute scale that this test requires. **Held open**, not attempted.

---

## Ledger movement

| Narrowed | Newly opened | Status |
| --- | --- | --- |
| δ = 2/9 survives at 0.42σ; all three lepton masses to ≤3.1×10⁻⁵ from one scale; §14 item 1 discharged | Whether any structure *other* than the trefoil forces 2/9 (Test B still unmet); m_τ precision as the binding limit; §6's "a hit makes it physics" needs softening against §7 | ◐ |

The **tension law** remains the missing input (Gap 2). Nothing here touches it.
