# Formulas — Every Formula in the Repository

One place for every formula, equation, scoring rule and quantitative identity in the repository. Each entry gives:

- where the formula is written;
- what status it carries;
- whether anything in the repository has run it, and the result.

> **This page is a navigation aid, not canon.** Where it and a version document differ, the version document wins (released versions are immutable). Status words are the repository's own vocabulary (`framework/registers.md` §2, `audit/SCHEMA.md` §1).

**Columns**
- **Where**: `file:line`. `v5.1` is `versions/v5.1/GFunnel-Methodology-v5.1.md`, and likewise for the other versions.
- **Kind**:
  - *canon*: written in a released version.
  - *imported*: an established law or constant that canon cites.
  - *derivation*: built in this repository and not declared into a version.
- **Status**:
  - *forced*: one candidate survives.
  - *live*: live hypothesis, falsifier attached.
  - *stipulation*: an operator choice.
  - *proven-open*.
  - *forced-no*: tested and ruled out.
  - *held open*: no value is supplied.
- **Run?**: ✅ executed in the repository, with its result · ◐ partly · ⛔ not runnable as written · — never run.

**Read this first.** The executed audit found that **no canon formula outputs a quantity it did not first import** (v5.4 §7: "zero novel predictions"; `audit/cost/README.md` §B: knowledge produced, $0). Canon formulas fall into four kinds:

- imported physics or mathematics;
- a business scoring rubric (BEAS);
- an arithmetic illustration;
- a fit to already-known data (Koide δ = 2/9).

The derivations in §8 produce values only from measured inputs.

---

## Contents

1. [The base and meta-tier (structure, not arithmetic)](#1--the-base-and-meta-tier)
2. [v5.1 operational and business formulas](#2--v51-operational-and-business-formulas)
3. [v5.1 Appendix D: constants and laws registry](#3--v51-appendix-d-constants-and-laws-registry)
4. [v5.4 Run 8: frequency, mass, Koide, devices](#4--v54-run-8)
5. [Executed tests (`framework/tests/`)](#5--executed-tests)
6. [Cell Atlas](#6--cell-atlas)
7. [Reality Audit: cost, prediction and design rules](#7--reality-audit-cost-prediction-and-design-rules)
8. [The Omni Gap Formula and the Gap Ledger](#8--the-omni-gap-formula-and-the-gap-ledger)
9. [Operations: the BEAS spreadsheet](#9--operations-the-beas-spreadsheet)
10. [Transcription and arithmetic problems found in canon](#10--problems-found-in-canon)
11. [Adding a formula](#11--adding-a-formula)

---

## 1 · The base and meta-tier

These are canon's structural rules. None of them computes a number. They are listed here because every formula below runs inside them.

| ID | Name | Form | Where | Kind | Status |
| --- | --- | --- | --- | --- | --- |
| EQ-001 | Base code | `DETECT → PROCESS → RESPOND` (recursive; restarts at a higher baseline) | v5.1:264–318 | canon | Bounded per canon. The audit graded it `fails` on cross-cycle behaviour (`audit/VERDICT.md`) and proposed adding TERMINATE (F-066). |
| EQ-002 | Variable Principle | `UNMEASURED → CREATE VARIABLE → MAP SURROUNDINGS → NARROW RANGE → RESOLVE OR HOLD` | v5.1:223–233 | canon | The audit rates it the framework's strongest element. **Operating-protocol amendment 2026-10-20:** "hold" now means *state the best tagged value and range while keeping it visibly open*; see the [Estimate Protocol](../substrate/2026-10-20-estimate-protocol.md). |
| EQ-003 | Master Meta-Algorithm | 12 ordered steps, Identify domain → Restart at higher baseline | v5.1:2178–2205 | canon | Graded `not-applicable` on a bacterium. |
| EQ-004 | Forcing Test | Tests A Ground · B Uniqueness · C Direction · D Falsifiability, giving four outcomes: forced-fill / live / stipulation / proven-open | v5.3:21–37 | canon | Graded `works-forced`, the best single result in the audit. |
| EQ-005 | Anti-Operation | each fill's conjugate returns the next gap | v5.3:48–67 | canon | **live** (it holds only under involutive structure). |

## 2 · v5.1 operational and business formulas

| ID | Name | Formula as written | Where | Kind | Status | Run? |
| --- | --- | --- | --- | --- | --- | --- |
| EQ-010 | Error Probability | "97% accuracy → 16% probability of perfection over 60 sequential decisions", i.e. **P = pⁿ = 0.97⁶⁰** | v5.1:1094, 1364; v5.2:227 | canon | Arithmetic correct. | ✅ 0.97⁶⁰ = 0.1608 (`audit/labels/LABEL-113-layer-V.md:22`). Valid only if the steps are independent, which canon does not state. |
| EQ-011 | Process Density | "organized, interdependent complexity per unit volume"; scale table (atom 1 Å … galaxy 10⁵ ly) | v5.1:1135–1147 | canon | Open (v5.1:1670). The audit: no metric, no units. | ◐ The cell row is 120–350× too large in volume (`audit/VERDICT.md`). Candidate metric: macromolecular crowding, 0.3–0.4 g/ml (F-077). |
| EQ-012 | Golden ratio | **(a+b)/a = a/b**, φ = (1+√5)/2 = 1.6180339887… | v5.1:1172–1175, 1968 | imported | forced | ✅ Digits to 10⁻⁶⁹ (`audit/constants/check_math_constants.py`). |
| EQ-013 | 4-Step Golden Ratio Method | selfish desire → selfless desire → convergence = purpose | v5.1:1178–1189, 2458–2475 | canon | Bounded (v5.1:1671); audit: stipulation. | — No step returns a number to compare with φ. |
| EQ-014 | Fibonacci Build Sequence | **F(n) = F(n−1) + F(n−2)**, mapped to 1,1 foundation / 2 first expression / 3 refinement / 5 systems / 8 team / 13 segments / 21+ platform | v5.1:1190–1206 | canon | Sequence: forced. Business mapping: untested. | ✅ The ratio converges to φ. 17.7% of measured sunflower heads are non-Fibonacci (F-017). The measured cross-generation coefficient in *E. coli* is −1/4 (RUN-001). |
| EQ-015 | Integration Density threshold | "integration ratio … approximating 1.618?" below = searching / at = stable / above = rigid | v5.1:1235–1250, 2451 | canon | Held open (v5.1:1250). | ⛔ A part/whole ratio lies in [0, 1], so 1.618 cannot be reached (`audit/VERDICT.md`). PRED-001 (φ in ribosome fraction) is still sealed. |
| EQ-016 | Process Density Algorithm | below / at / above an emergence threshold → build / maintain / reduce coupling | v5.1:2418–2437 | canon | — | ⛔ Blocked: no counting rule, threshold or units. |
| EQ-017 | **BEAS** cell | each cell ∈ {0, 0.5, 1} | v5.1:1398 | canon | v5.2 Run 4: "honest diagnostic, ordinal" | see EQ-020 |
| EQ-018 | BEAS department total | **Dept = Correctness + Complexity + Patience + Resilience** (max 4) | v5.1:1400 | canon | — | ✅ as a spreadsheet formula (§9) |
| EQ-019 | BEAS total | **BEAS = Σ 36 pillar cells + Σ 9 coordination scores** (max 45) | v5.1:1392, 1402–1404 | canon | — | ✅ as a spreadsheet formula (§9) |
| EQ-020 | BEAS bands | 40–45 Dynamic Middle–Sustained · 32–39 Equilibrium–Functional · 24–31 Imbalance–Managed · 16–23 Imbalance–Exposed · 0–15 Collapse Risk | v5.1:1424–1435 | canon | v5.2: band calibration held open | ◐ Run on a bacterium: 7 cells defensible, 8 contradicted, 25 arbitrary, 5 unfillable. 56% of the score is operator discretion (`audit/VERDICT.md`). Half-point totals (e.g. 39.5) fall between bands. |
| EQ-021 | BEAS growth-stage targets | "Sales + Ops both 3+ of 4"; "BEAS target: 35+ of 45" | v5.1:767–771 | canon | — | — |
| EQ-022 | BEAS Yin/Yang quadrants | High Yang = Marketing, Sales, Ops; High Yin = Strategy, Finance, HR, Content; Bridging = Tech, Client Success | v5.1:1436–1446 | canon | — | ✅ as quadrant averages (§9) |
| EQ-023 | Risk score | **risk = probability × impact**; a cascade risk takes priority regardless of probability | v5.1:3494–3496 | canon | Both factors held as variables until measured. | — |
| EQ-024 | Pareto operational rule | "20% of activities / variables / unknowns drive 80%" | v5.1:3584, 3762, 3778 | canon | **forced-no** as a law (`audit/constants/CONST-pareto-principle.md`) | ✅ see EQ-061 |
| EQ-025 | Conversion rule | measure conversion at each step; improve the lowest-converting step first | v5.1:2533 | canon | — | ◐ On the bacterium it picks the wrong channel (`audit/VERDICT.md`). |
| EQ-026 | Civil-infrastructure ratios | Katrina "~400× the pre-event corrective investment"; Texas 2021 "246 deaths, $195 B"; 2008 "$22 trillion" | v5.1:469, 475, 481 | canon (case figures) | held open (`audit/labels/LABEL-103-layer-I.B.md:26`) | — |
| EQ-027 | Timing rules | hiring 30/60/90-day reviews; onboarding 48 h / 30 days / 90 days; habit 21–66 days; BEAS re-score monthly | v5.1:2671, 2685–2689, 3636, 2495 | canon | — | — |

## 3 · v5.1 Appendix D: constants and laws registry

The registry is at v5.1:1946–2150. The audit gives each entry a record in `audit/constants/`; the four check scripts there execute what can be executed. Outcomes across all 87 records: **51 forced-fill · 16 live · 13 stipulation · 6 forced-no · 1 proven-open.**

| ID | Name | Formula | Where | Audit outcome | Run? |
| --- | --- | --- | --- | --- | --- |
| EQ-040 | π, e, i, √2 | 3.14159…; d/dx eˣ = eˣ; i = √(−1); √2 = 1.41421… | v5.1:1967–1974 | forced-fill | ✅ Digits pass. √2's "three thousand years early" **fails**: the gap is 2,420–2,500 years. |
| EQ-041 | Lucas sequence | L = 2, 1, 3, 4, 7, 11… ; L(n+1)/L(n) → φ | v5.1:1976 | forced-fill | ✅ Exception: seed (1, ψ) → ψ = −0.618 |
| EQ-042 | Game of Life | B3/S23 | v5.1:1977 | forced-fill | ✅ blinker, block, glider |
| EQ-043 | Mandelbrot | **zₙ₊₁ = zₙ² + c** | v5.1:1978 | forced-fill | ✅ |
| EQ-044 | Physical constants | c, G, ℏ, k_B, α = 1/137.036, mₑ, mₚ (mₚ/mₑ ≈ 1836), e, Planck length and time | v5.1:1990–2001 | forced-fill | ✅ All 11 consistent with CODATA 2022 (`check_physical_constants.py`) |
| EQ-045 | Cosmological constant | canon "~1.1×10⁻µ² m⁻²" (garbled); **Λ = 3Ω_Λ H₀²/c²** | v5.1:1998 | forced-fill | ✅ 1.091×10⁻⁵² m⁻² |
| EQ-046 | Hubble constant | "~67–73" | v5.1:1999 | forced-fill | ✅ 67.4 ± 0.5 vs 73.04 ± 1.04, 4.9σ apart. This is now tracked live as G-001 (§8). |
| EQ-047 | Newton | **F = ma**; action = −reaction | v5.1:2034 | 2nd: forced-fill · 3rd: **live** | ✅ Third law: the Biot–Savart counterexample gives a net magnetic force of 10⁻⁷ N ≠ 0. |
| EQ-048 | Mass–energy | **E = mc²**; E² = (pc)² + (mc²)² | v5.1:2036 | forced-fill | cited tests to 4×10⁻⁷ |
| EQ-049 | Schrödinger | **iℏ ∂ψ/∂t = Ĥψ** | v5.1:2037 | forced-fill | — |
| EQ-050 | Heisenberg | **Δx·Δp ≥ ℏ/2** | v5.1:2038 | forced-fill | — |
| EQ-051 | Einstein field equations | **G_μν + Λg_μν = (8πG/c⁴) T_μν** | v5.1:2040 | live | falsifier: PPN or gravitational-wave-speed deviation |
| EQ-052 | Le Chatelier | "this IS the Garlick Equilibrium at molecular scale" | v5.1:609, 2042 | **forced-no** as a universal law | ✅ N₂ + 3H₂ ⇌ 2NH₃ shifts **left** when x_N₂ > ½ |
| EQ-053 | Kepler | **T² ∝ a³** | v5.1:2044 | forced-fill | ✅ |
| EQ-054 | Maxwell | four equations | v5.1 registry | forced-fill | ✅ μ₀/(4π·10⁻⁷) − 1 = −1.3×10⁻¹⁰ |
| EQ-055 | Shannon entropy | **H = −Σ pᵢ log₂ pᵢ** | v5.1:2056 | forced-fill | — |
| EQ-056 | Shannon–Hartley | **C = B log₂(1 + S/N)** | v5.1:2057 | forced-fill | — |
| EQ-057 | Landauer | **E = kT ln 2** | v5.1:2058 | forced-fill | ✅ 2.871×10⁻²¹ J at 300 K |
| EQ-058 | Bremermann | canon "1.36×10⁵°" (garbled); **c²/h** | v5.1:2059 | forced-fill (corrected) | ✅ 1.3564×10⁵⁰ bits/s/kg |
| EQ-059 | Bekenstein | canon "information ∝ area"; true form **S ≤ 2πRE/(ℏc)** | v5.1:2060 | live, conflict | Canon's wording is the holographic bound (F-060). |
| EQ-060 | Holevo | n qubits → ≤ n bits | v5.1:2066 | forced-fill | — |
| EQ-061 | Pareto distribution | **P(X > x) ∝ x^(−α)**; top-p share = p^(1−1/α) | v5.1:2098–2099 | **forced-no** ("everything is a power law") | ✅ α = 1.161 gives exactly 80/20 |
| EQ-062 | Zipf · Metcalfe · Reed | f ∝ 1/rank · value ∝ n² · value ∝ 2ⁿ | v5.1:2100–2102 | Zipf forced-fill; Metcalfe and Reed live, unobserved | ✅ Zipf (network script) |
| EQ-063 | Moore · Wright | doubling ~2 yr · cost ∝ production^(−β) | v5.1:2103–2104 | forced-fill (form) | ✅ Moore (network script) |
| EQ-064 | Lindy | **E[T − t \| T > t] = t/(α − 1)** | v5.1:2108 | live, unobserved | ✅ α = 2 gives 1.0× current age |
| EQ-065 | Kleiber · allometric | ∝ M^(3/4) · ∝ M^k | v5.1:2078–2079 | Kleiber **forced-no** as one universal law; allometric live | — |
| EQ-066 | Hayflick · Dunbar · Miller | ~50 divisions · ~150 · 7 ± 2 | v5.1:2080, 2085, 2086 | Miller **forced-no** (~4 measured) | — |
| EQ-067 | Krebs stoichiometry | 1 acetyl-CoA → 3 NADH + 1 FADH₂ + 1 GTP + 2 CO₂ | v5.1:2081 | forced-fill | — |
| EQ-068 | ATP per glucose | "≈32"; **ATP = 8·P/O_NADH + 2·P/O_succ + 2·shuttle + 4** | v5.1:1760, 2082 | live (range 28–32) | ✅ 32.0 / 30.0 / 29.8 / 28.0 depending on P/O and shuttle |
| EQ-069 | Hardy–Weinberg | **p² + 2pq + q² = 1** | v5.1 registry | forced-fill | ✅ (0.3025, 0.495, 0.2025) |
| EQ-070 | Framework invariants | 3, 4, 5, 6, 7, 9 (= 3 Kingdoms × 3 operations), 10, 17, 49 (= 7×7), 100 (= 10²) | v5.1:2119–2130 | stipulation; 7, 9, 49 in conflict | No 3×3 grid exists in the department table (F-063). |

## 4 · v5.4 Run 8

The status is v5.4's own (§4a.7, §12). v5.4 itself says these are **measured physics placed on the lines** and that the run made **zero novel predictions**. Use them with v5.4's four cautions: **Bell**, **environmental decay rates**, **point-like quarks**, **the measurement problem**.

| ID | Name | Formula | Where | Status | Run? |
| --- | --- | --- | --- | --- | --- |
| EQ-080 | Frequency definition | frequency = line × node (a two-place relation) | v5.4:80–83 | forced | — |
| EQ-081 | Planck–Einstein | **E = hf** | v5.4:88 | forced | — standard |
| EQ-082 | Compton frequency | **f = mc²/h** (electron 1.24×10²⁰ Hz) | v5.4:89 | forced | value checks: 1.2356×10²⁰ Hz |
| EQ-083 | de Broglie | **p = h/λ** | v5.4:90 | forced | — |
| EQ-084 | Lifetime ↔ linewidth | **Δf·Δt ≥ 1/4π → τ = 1/(2πΔf)** | v5.4:92, 121 | forced | Top quark: ℏ/Γ = 4.7×10⁻²⁵ s ✓. The τ form is the linewidth definition, not a consequence of the bound (see §10). |
| EQ-085 | Temperature | **kT ≈ hf**; "CMB 2.7 K ↔ 160 GHz peak" | v5.4:93 | forced | ⚠ kT/h at 2.7255 K = **56.8 GHz**. 160 GHz is the Wien peak, hf = 2.821 kT (see §10). |
| EQ-086 | Frequency ladder | Planck 1.9×10⁴³ Hz → Hubble ~2×10⁻¹⁸ Hz, "~61 orders of magnitude" | v5.4:98–116 | forced | spot checks consistent |
| EQ-087 | Raychaudhuri focusing | convergence ∝ **ρ + 3p**; intrinsic neutral at **ρ + 3p = 0** | v5.4:125, 146, 172–174 | forced; neutral held open | — |
| EQ-088 | Self-dual center | **E = pc** (light, its own antiparticle) | v5.3:60; v5.4:149 | proven-open (center); W1 live route | — |
| EQ-089 | Invariant mass | **(mc²)² = E² − (pc)²** (FT eq. 6) | v5.4:176 | canon | ⛔ FT eq. 6 is not in the repository (`framework/tests/not-runnable.md`) |
| EQ-090 | Involution | z·z* (FT eq. 2): the anti-container | v5.4:36 | forced | ⛔ FT eq. 2 is not in the repository |
| EQ-091 | Koide ratio | **Q = Σm / (Σ√m)² = 2/3** ("6 ppm") | v5.4:196 | "fact" | ✅ 3.3 ppm (PDG 2024) or 9.2 ppm (v5.4's cited m_τ), not 6 ppm. Q ≡ 2/3 is built into the Brannen form. |
| EQ-092 | Brannen form | **√m_k = μ[1 + √2 cos(2πk/3 + δ)]**, δ = 2/9 | v5.4:196 | live (the one live handle) | ✅ δ = 0.2222265 ± 0.0000103, **+0.42σ** from 2/9; masses to ≤0.0031%. Post hoc. |
| EQ-093 | Trefoil form | (2,3) torus knot: 2/3 = winding fraction; **2/9 = 2/3 ÷ 3** (partition) | v5.4:198–200 | form derived; partition identity **stipulation** | ⛔ needs the tension law |
| EQ-094 | Projection rule | line value 2/3 invariant; ÷ partition → 2/9 (3-fold), 1/3 (2-fold, mesons) | v5.4:204, 256 | proposed | ⛔ no observable specified |
| EQ-095 | Quark Koide triplets | (u,c,t) 0.849 · (d,s,b) 0.731 · (c,b,t) 0.6695 | v5.4:202, 277 | (c,b,t) live | — |
| EQ-096 | Generations as integer harmonics | 1 : 2 : 3 | v5.4:145, 162 | **forced-no** | ✅ measured 1 : 206.8 : 3477.4 |
| EQ-097 | D1 Lamina Shield | ~3 kJ round → "hundreds of tesla if field-only" | v5.4:226 | physics-permitted | ✅ see EQ-111 |
| EQ-098 | D2 fold storage | chemical 10⁷ · nuclear 10¹⁴ · mass-energy 10¹⁷ J/kg; second-law tax ~95% best, 100% forced-no | v5.4:228 | folds as a source **forced-no** | — |
| EQ-099 | Lamina plateau | nuclear saturation ~0.16 nucleons/fm³ | v5.4:180 | falsifier attached | ◐ see EQ-112 |
| EQ-100 | Vacuum-density discrepancy | QFT ~10¹¹³ vs measured ~10⁻⁹ J/m³ | v5.4:36, 150 | held open | — |

## 5 · Executed tests

Each test lives in `framework/tests/` and is logged as variable evidence in `framework/registers.md`, rows 16–18.

| ID | Test | Formulas executed | Result |
| --- | --- | --- | --- |
| EQ-110 | Koide δ = 2/9 (`koide_delta.py`) | Brannen bracket; Q; δ by bisection; μ = √m_anchor / bracket; sensitivity **d ln m_k/dδ = −2√2 sin(2πk/3 + δ) / bracket** | **Passes** at 0.42σ. Sensitivities −51.49 / +4.66 / −0.26 (mₑ is the sharp probe). Falsifier: a future m_τ measurement that moves δ >3σ from 2/9. |
| EQ-111 | D1 energy budget (`d1_budget.py`) | **B = √(2μ₀p)**; **u = KE/V**; **P_dyn = ½ρv²**; **n = P/(k_B T)** | **105 T** (5.56 mm round) to **241 T** (long rod) under the pressure criterion. Plasma is **forced**. The plasma window falls about 4.4×10⁴ short of the needed pressure. |
| EQ-112 | Lamina falsifier | n₀ ≈ 0.16 fm⁻³ | One plateau confirmed. Undecidable as worded: it needs a stated plateau spacing. |
| — | Meson 1/3 · partition = phase | — | ⛔ not runnable (`framework/tests/not-runnable.md`) |

## 6 · Cell Atlas

Derivation, not canon (`tasks/cell-atlas/`).

| ID | Name | Formula | Where | Result |
| --- | --- | --- | --- | --- |
| EQ-120 | Na⁺/K⁺ pump work | **W = n_Na·RT·ln([Na]out/[Na]in) + n_K·RT·ln([K]in/[K]out) − (n_Na − n_K)·F·Vm**; runs only if **W ≤ \|ΔG_ATP\|** | `tasks/cell-atlas/scripts/na_k_pump_energetics.py:30–32`; `membrane/run-01-na-k-pump.md:35–40` | ✅ 3:2 uses 34.8 kJ/mol at 0 mV and 42.5 at −80 mV (79% of ATP's 54 kJ/mol). |
| EQ-121 | Stall voltage | **Vm\* = −(\|ΔG_ATP\| − W(0)) / ((n_Na − n_K)·F)** | same | ✅ 3:2 stalls at −199 mV. 4:3 stalls at −48 mV, so it cannot run at a resting potential, which is why the measured ratio is 3:2. |

## 7 · Reality Audit: cost, prediction and design rules

Derivation, not canon.

| ID | Name | Formula | Where | Result |
| --- | --- | --- | --- | --- |
| EQ-130 | Currency conversion | **usd = amount × FX[year]** | `audit/cost/compute_cost.py:66–70` | ✅ |
| EQ-131 | Inflation to 2025 $ | **usd₂₀₂₅ = usd × CPI[2025] / CPI[year]** | `compute_cost.py:73–74` | ✅ Facilities $147–164 B ($41–58 B excluding the ISS); world R&D 1996–2023 ≈ $62.8 T |
| EQ-132 | Cost per study | **cost per study = cost per paper × k** (k held open); Route A: field R&D ÷ field articles | `audit/cost/unit_costs.md:89–95` | ✅ Knowledge **contained** $158–177 B; knowledge **produced** **$0** |
| EQ-133 | Prediction verdict rule | hit only if inside the Phase-A tolerance **and** discriminating **and** low-contamination | `audit/prediction/PROTOCOL.md:74–84` | PRED-002 hit (high contamination); PRED-003 partial; PRED-004 hit (on process); PRED-001 still sealed |
| EQ-134 | Multi-stage accuracy (product rule) | **error_total = Π error_stage** (three stages at 10⁻² → 10⁻⁶), valid only if the stages are independent | `design/RUN-001-self-healing-pipeline.md:52, 99–109` | ◐ Independence is held open. PRED-004 hit: correlated failure is the binding limit. |

## 8 · The Omni Gap Formula and the Gap Ledger

Derivation, not canon. These are the only formulas in the repository built to **fill and narrow gaps**. Documentation: [`OMNI-GAP.md`](OMNI-GAP.md) and [`LEDGER.md`](LEDGER.md).

| ID | Name | Formula | Where | Result |
| --- | --- | --- | --- | --- |
| EQ-140 | **Omni Gap Formula** | **x\* = Π_F[ Σ_k w_k μ_k(x\|E) ]**, k ∈ {P prior, S structure, R correspondence}; **I = x\* ± q₁₋α**; **status = FT(F, I, τ)** | [`omni_gap.py`](omni_gap.py) | ✅ Beat mean, k-NN, ridge and chained (MICE-style) imputation on all 3 tables, by 4–9% in error. Intervals are calibrated: 91–93% coverage against a stated 90%. |
| EQ-141 | Stacking weights | **w = argmin_{w≥0} Σ (y − Σ w_k μ_k)²** on hidden known values | `omni_gap.py` `_stack_weights` | ✅ |
| EQ-142 | Conformal half-width | **q = |residual|₍⌈(1−α)(n+1)⌉₎**; valid from **n ≥ (1−α)/α** (= 9 at 90%) | `omni_gap.py` `_quantile`, `_calibrate_identities` | ✅ |
| EQ-143 | Identity conditioning | **μ' = μ + K(b − Aμ)**, **K = ΣAᵀ(AΣAᵀ)⁻¹**, **Σ' = Σ − KAΣ** | `omni_gap.py` `_condition` | ✅ Forced fills are exact |
| EQ-144 | Narrowing | **narrowing = 1 − width / prior width** | `omni_gap.py` `_respond` | ✅ |
| EQ-145 | Inverse-variance combination | **μ = Σ(v/σ²) / Σ(1/σ²)**, **σ = (Σ 1/σ²)^(−½)**, **χ² = Σ((v − μ)/σ)²** | [`ledger.py`](ledger.py) `combine` | ✅ |
| EQ-146 | Conflict test and tension | conflict if **p(χ², dof) < 0.01**; **tension = \|a − b\| / √(σₐ² + σ_b²)**; scale factor **S = √(χ²/dof)** | `ledger.py` `evaluate` | ✅ H₀ 4.9σ · neutron lifetime 4.4σ · lithium-7 4.0σ · W mass 7.2σ |
| EQ-147 | Decisive next measurement | **σ_next ≤ \|a − b\| / (3√2)** | `ledger.py` `evaluate` | ✅ e.g. H₀ needs σ ≤ 1.33 km/s/Mpc |
| EQ-149 | **Forecast test harness** | two arms × every metric; each row: value, low, high, tag ∈ {measured, forced, estimate, assumption, held-open}, falsifier; scored as **hit = low ≤ actual ≤ high**, **scaled error = \|value − actual\| / tolerance**, per arm and per tag | [`forecast.py`](forecast.py); protocol in [`substrate/2026-10-20-estimate-protocol.md`](../substrate/2026-10-20-estimate-protocol.md) | Harness validated on an illustrative fill. No real run scored yet. |
| EQ-148 | Prediction score and learned widening | **r = \|x − mid\| / √(half² + (Zσ)²)**, hit if r ≤ 1; **widening = conformal quantile of r**, applied once n ≥ 9 | `ledger.py` `required_widening`, `learned_factor` | ✅ Backtest hit rate 17% (stated 90%); learned widening ×3.26 from 6 cases, not yet applied. Real seals placed 2026-10-19. |

## 9 · Operations: the BEAS spreadsheet

`operations/agent-org-map/build_agent_map.py:648–682` writes canon's BEAS (EQ-017 to EQ-022) as live spreadsheet formulas into `GFunnel-Agent-Org-Map.xlsx`:

- `=SUM(C,E,G,I)` per department.
- BEAS total `=K14+L14`.
- A band from nested `IF` with ≥40 / ≥32 / ≥24 / ≥16 thresholds. This settles the half-point gaps in EQ-020.
- The lowest department via `INDEX/MATCH(MIN(K5:K13))`.
- Quadrant averages: Yang `AVERAGE(K6:K8)`, Yin `AVERAGE(K5,K9,K10,K13)`, Bridging `AVERAGE(K11:K12)`.
- Input validation: cells limited to {0, 0.5, 1}.

## 10 · Problems found in canon

Released versions are immutable, so these are **logged, not edited**. A correction belongs in a future version or a transcription-fix issue (`CONTRIBUTING.md`).

| # | Where | Problem | Checked value |
| --- | --- | --- | --- |
| 1 | v5.4:196 | Koide agreement stated as "6 ppm" | 3.3 ppm (PDG 2024 m_τ = 1776.93) or 9.2 ppm (m_τ = 1776.86). Also, 2/3 is built into the Brannen form, so it is one test, not two (`framework/tests/koide-delta.md`). |
| 2 | v5.4:93 | "kT ≈ hf; CMB 2.7 K ↔ 160 GHz" | kT/h = 56.8 GHz. 160.2 GHz is the Wien frequency peak, hf = 2.821 kT. |
| 3 | v5.4:92 | τ = 1/(2πΔf) presented as following from Δf·Δt ≥ 1/4π | The two use different constants. The first is the Lorentzian linewidth definition, the second a lower bound. |
| 4 | v5.1:2059 | Bremermann "1.36×10⁵°" | 1.36×10⁵⁰ bits/s/kg (garbled exponent) |
| 5 | v5.1:1998 | Λ "~1.1×10⁻µ² m⁻²" | 1.09×10⁻⁵² m⁻² (garbled exponent) |
| 6 | v5.1:1974 | √2 "three thousand years early" | 2,420–2,500 years |
| 7 | v5.1:1235–1250, 2451 | a part/whole ratio compared with φ = 1.618 | A part/whole ratio lies in [0, 1]. The test is unattainable as written. |
| 8 | v5.1:1427–1433 | BEAS bands are integers, but cells score in halves | Totals such as 39.5 are unassigned. The spreadsheet uses ≥ thresholds. |
| 9 | v5.1:1094, 1364 | 97% → 16% over 60 decisions | Arithmetic correct (0.1608). It assumes independent steps, which canon never states. |
| 10 | v5.4:226 | D1 reasoning via energy density | The number is right; the correct criterion is pressure (`framework/tests/d1-energy-budget.md`). |

## 11 · Adding a formula

When a formula enters the repository (canon, test, audit or derivation), add a row here in the same change:

```
| EQ-### | Name | Formula exactly as written (bold the equation) | file:line | Kind / status | Run? result, or — |
```

Rules, carried from `AGENTS.md` and the Variable Principle:

- **Quote, don't improve.** Write canon's formula as canon writes it. Put the checked value in the Run? column or in §10, never in place of the original.
- **No status above its evidence.** A formula is not *forced* because it looks right. It is forced when one candidate survives.
- **Name what it outputs.** If the formula only re-expresses an imported value, say so. If it has produced a value before measurement, link the sealed prediction that proves it.
- **Keep the ID stable.** IDs are never reused. A retired formula keeps its row, marked forced-no or superseded.

---

```
Source: GFunnel Methodology (Omni Process) v5.1–v5.4, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0.
Adapted: this index compresses and cross-references the canonical text; it is not endorsed by the author.
```
