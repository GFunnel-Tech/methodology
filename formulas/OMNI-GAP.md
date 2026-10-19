# The Omni Gap Formula

> **Status: derivation, not canon** (AGENTS.md rules 4 and 7). It is derived from the Master Meta-Algorithm, the Variable Principle, and Layers I.G, II, ◇ and ⊙ (v5.1–v5.4). It also carries the Reality Audit's corrections (`audit/VERDICT.md`, `audit/FINDINGS.md`). It becomes part of a version only if the author declares it. Nothing in `versions/` was changed.

**What it is for.** You have a table: records × variables. Some cells are empty. For each empty cell the formula:

- fills it when the record's own structure supports a value;
- narrows it to a range when it cannot support a value;
- refuses when nothing beats the base rate.

Every output carries a calibrated interval, a status, a falsifier, and the next measurement worth taking. The result is a prediction you can act on and check before any testing, because it says in advance how often it will be wrong.

---

## 1 · The formula

For an empty cell *x* (variable *j*, record *i*), with *E* the measured values in that record:

```
                ┌                                   ┐
   x* =  Π_F    │   Σ_k  w_k · μ_k(x | E)           │          k ∈ { P, S, R }
                └                                   ┘
   I  =  x* ± q_{1-α}
   σ  =  FT( F, I, τ )
```

| Symbol | What it is | Where it comes from |
| --- | --- | --- |
| **F** | The feasible set: the bounds and linear identities the record must obey (e.g. `revenue − cogs = gross`). | Variable Principle: *"map what IS measurable on either side"* |
| **Π_F** | Projection onto F. It conditions the estimate on the identities. When the identities leave one value, the cell is **forced**. | Forcing Test, Output 1 (v5.3) |
| **μ_P** | The **Capsule prior**: the variable across every prior record. | Layer I.G: *the present integrates all prior paths* |
| **μ_S** | **Process structure**: the variable's measured relation to the other variables in the same record (regression). | Layer 0 / I.C: name the occupant that carries the signal |
| **μ_R** | **Correspondence**: the same variable in the nearest analogous records (k-nearest). | Layer II, Correspondence: *"solve it at one scale…"* |
| **w_k** | Channel weights. They are learned by hiding values that **are** known and measuring which channel recovers them (non-negative least squares). | Layer I.G + MMA step 12: every failed path is integrated |
| **q_{1−α}** | The interval half-width. It is the (1−α) quantile of the errors made on those hidden known values, with the identity step included (split-conformal). The stated miss rate is therefore a **measured** miss rate. | Layer ◇: a claim must say what would prove it wrong |
| **τ** | Decision tolerance: the widest interval you can still act on. The default is half a column standard deviation. | MMA step 4: the desired state defines the work |
| **FT** | The Forcing Test classifier. It returns the status below. | Layer ⊙ (v5.3) |

### The loop, run as the Master Meta-Algorithm

```
DETECT     find the gap; build F from bounds + identities
PROCESS    μ_P, μ_S, μ_R  →  weighted by w  →  conditioned on F
RESPOND    value or range, status, falsifier, next measurement
TERMINATE  if no channel beats the prior, or I is wider than τ: stop, hold open
RESTART    each measurement later revealed joins the calibration set (MMA step 12)
```

TERMINATE is the Reality Audit's correction F-066. Canon's loop has no stopping step. Here, stopping is the step that keeps the formula from guessing.

### Two rules enforced in code

1. **A fill is never an input to another fill.** Only measured values feed the channels, so one guess never becomes the premise of the next. This is the Variable Principle applied to the method itself. It is also the main design difference from chained (MICE-style) imputation, which re-uses its own fills.
2. **A filled value is never reported as measured.** Every cell carries one of the statuses below.

### Output statuses (the Forcing Test classes, plus the two the audit found missing)

| Status | Meaning | Point value emitted? |
| --- | --- | --- |
| `measured` | The cell was in the data. | It is the data. |
| `forced-fill` | The identities leave exactly one value. | Yes, exact. |
| `live-fill` | Live hypothesis: the calibrated interval is within τ, and a falsifier is attached. | Yes, with its interval. |
| `held-open` | The range is narrowed, but it is wider than τ. | **No.** Range only, plus the measurement that would narrow it most. |
| `held-open/no-signal` | Nothing in the record beats the base rate. | No. |
| `conflict` | Either the structure and the analogues disagree beyond anything seen in calibration, or the measured values break an identity. | No. The record itself is the place to look (*"reality wins"*, substrate item 1). |

---

## 2 · Does it beat known methods? (measured)

`python3 formulas/benchmark.py` runs the test. For each table it hides 20% of the **measured** cells at random, fills them with every method, and scores the fills against the hidden truth. The scores are averaged over five masks. NRMSE is error divided by the column's standard deviation; lower is better, and 1.0 means "no better than the average".

| Table | mean | k-NN | ridge | chained (MICE-style) | **omni** | omni vs best baseline |
| --- | --- | --- | --- | --- | --- | --- |
| Auto-MPG (UCI, real, 398 × 7) | 1.014 | 0.448 | 0.470 | 0.477 | **0.426** | −4.9% error |
| Palmer penguins (real, 344 × 4) | 0.988 | 0.584 | 0.655 | 0.659 | **0.561** | −3.9% error |
| P&L with 2 identities (**synthetic**, 300 × 6) | 1.026 | 0.422 | 0.256 | 0.287 | **0.234** | −8.6% error |

**Calibration.** Omni's 90% intervals contained the hidden truth 91.0%, 92.6% and 92.2% of the time (the last figure excludes the exact forced fills). The stated miss rate is the actual miss rate.

**Selective filling earns its keep.**

- On Auto-MPG omni filled 37% of the gaps. On those cells its error was 0.285 sd, against 0.300–0.323 for the baselines on the same cells. The cells it refused would have carried 0.545 sd of error.
- On the P&L it filled 65% of the gaps (64% forced, which are exact). On those cells its error was 0.024 sd, against 0.049–0.428 for the baselines.
- On the penguins table it filled **nothing**. Four body measurements do not pin each other down to within half a standard deviation, and the formula said so rather than guessing.

`python3 formulas/example.py` runs the formula on six gaps nobody created: cars whose horsepower was never recorded in the UCI table. At a ±10 hp decision tolerance it narrows each one by 69% against the base rate. It emits no point value, because its calibrated interval is ±17.5 hp.

---

## 3 · What it does not do (held open, not filled)

- **It is not "better than any known metric".** It beat four standard methods on three tables by 4–9%. That is real, modest, and specific to these tables. No method can beat the best possible inference from the same information; gains come only from **more structure**: identities, analogues, and calibrated restraint. Stronger learners (gradient-boosted trees, Gaussian processes, deep imputers) were not tested and may beat it. **Held open until run.**
- **It is built from known parts.** The parts are stacked regression, k-nearest neighbours, Gaussian conditioning on linear constraints, and split-conformal intervals. The framework contributes the **discipline**: which channels to use, the refusal to chain guesses, a status on every cell, an attached falsifier, and a stop rule. It does not contribute new mathematics.
- **No canon layer supplies a value.** The Reality Audit found **zero** cases of canon stating a quantity before measurement (`design/DESIGN-ALGORITHM.md`, `audit/cost/README.md` §B). This formula keeps that finding intact: every number it emits comes from measured data in the table, never from a layer's content claims.
- **The interval is only as honest as its assumption.** Split-conformal coverage assumes the gaps are missing at random relative to the calibration cells. If values are missing **because** they are extreme (for example, unreported losses), the intervals will be too narrow. **Held open:** a missing-not-at-random check.
- **Prediction before testing has its own proof standard.** A fill is a live hypothesis, not knowledge. The repository already has the test that would turn one into evidence: `audit/prediction/PROTOCOL.md`. Seal the fill and its interval in git before the measurement is fetched, then score it.

## 4 · Conjugate gaps this opens (the Anti-Operation, logged now while cheap)

1. **Rhythm channel (T).** Records ordered in time should add a trend channel. It is not built.
2. **Correlated channel errors under identities.** These are handled by measuring the width end-to-end, not by modelling the correlation. A joint model could make tighter, still-honest intervals.
3. **Categorical variables** (species, region, plan tier) are not yet channels.
4. **Cross-table Correspondence.** Analogues are drawn only from the same table. Borrowing from another table with a shared scale is the literal form of "as above, so below", and it is untested.

## 5 · The living version: the Gap Ledger

The formula is also run continuously on open scientific questions (the Hubble tension, neutron lifetime, primordial lithium, W mass, and the Big Bang boundary). New evidence narrows each gap or exposes a conflict. Every movement is logged, and the ledger seals and scores its own predictions. See [`LEDGER.md`](LEDGER.md) and the live [`ledger/REPORT.md`](ledger/REPORT.md).

## 6 · Use

```python
from formulas.omni_gap import OmniGap
og = OmniGap(columns, rows,                      # rows: lists of float or None
             identities=[({"revenue": 1, "cogs": -1, "gross": -1}, 0.0)],
             bounds={"revenue": (0, None)},
             tolerance={"gross": 50_000},       # widest interval you can act on
             alpha=0.10)                        # stated (and measured) miss rate
for f in og.fill():
    print(f.row, f.column, f.status, f.value, (f.lo, f.hi), f.falsifier, f.next_measurement)
```

Standard library only, like the rest of the repository. `data/mpg.csv` is the UCI Auto-MPG dataset (CC BY 4.0). `data/penguins.csv` is Palmer Penguins (Horst, Hill & Gorman, CC0). Both are vendored from the seaborn-data repository so the benchmark runs offline.

---

```
Source: GFunnel Methodology (Omni Process) v5.4, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0.
Adapted: this formula is a derivation built on v5.1–v5.4; it is not endorsed by the author.
```
