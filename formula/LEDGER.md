# The Gap Ledger — the formula as a living asset

> **Status: derivation, not canon.** It is built on `omni_gap.py` (the Omni Gap Formula) and on the canon's own Iteration Ledger discipline: what narrowed, what stayed open, what newly opened. The current state is in [`ledger/REPORT.md`](ledger/REPORT.md), which the ledger regenerates on every run.

`omni_gap.py` fills gaps in one table, once. The ledger keeps the formula running on **open questions** as evidence accumulates. Each gap is one quantity that science has not settled. Every new result narrows it, corroborates it, or exposes a conflict. The ledger records each movement and scores its own past predictions.

## The loop

```
add evidence  →  run  →  every gap re-evaluated  →  movements logged  →  REPORT.md rewritten
                  ↑                                                              │
                  └──── seal predictions → later evidence scores them → learned widening ┘
```

1. **DETECT.** Group the evidence by independent method. Repeat results from one method share its systematics, so they count as a single witness.
2. **PROCESS.** Combine the witnesses by precision weighting, then test whether they agree (chi-square).
3. **RESPOND.** Each gap gets one of these statuses:

   | Status | Condition | Output |
   | --- | --- | --- |
   | `held-open` | no evidence | Ranges and narrowing routes only. **Never filled.** |
   | `live (single witness)` | one method | A value and range, flagged as uncorroborated. |
   | `narrowed (corroborated)` | ≥2 methods that agree | A combined value and a narrower range. |
   | `conflict` | methods disagree (p < 0.01) | No point value. It reports the tension in σ, **which witness, removed, restores agreement** (the location of the work), and the precision a decisive next measurement needs. |

4. **TERMINATE.** A gap with no evidence stops at `held-open`. The Big Bang's first moment (G-005) sits there by design: no tested law holds there, there are no analogues, and there is nothing to calibrate against. Canon files it as proven-open (v5.4, Gap 1).
5. **LEARN (the Capsule loop).** `seal` freezes a gap's current range as a prediction, with a date and a hash. Measurements published later score it. Every score, hit or miss, shows how wide the range should have been. Once nine predictions are scored (the minimum for a valid 90% quantile), that widening factor is applied to every range automatically.

## What the replay already shows

The ledger was replayed through the evidence as it arrived: 2013 → 2018 → 2019 → 2021 → 2022 → 2024.

- **H₀** moved through three statuses. In 2018 it was a single witness (Planck). In 2019 it was **corroborated** (TRGB agreed). In 2021 it went into **conflict** (SH0ES, 4.9σ). Removing either the Cepheid ladder or the CMB inference restores agreement. So the ledger locates the gap between the two methods, not inside either one, which is exactly where cosmologists are looking.
- **W boson mass.** One witness (CDF, 2022), then a **7.2σ conflict** once the LHC results arrived. Removing CDF alone makes the remaining three agree at p = 0.65. The ledger names CDF as the location of the work.
- **Neutron lifetime.** Beam vs. bottle, 4.4σ conflict.
- **Primordial lithium.** BBN theory vs. halo-star observation, 4.0σ conflict. The ledger also holds open the most likely resolution: the two witnesses may not measure the same quantity, because stars can destroy lithium.

**The finding that matters most.** Backtest seals placed at past dates hit only **17%** of later measurements, against a stated 90%. At these frontiers, published uncertainties understate real error. The ledger has measured by how much: about **3.3×** so far, from six scored cases. This does not prove foresight, since the later results were already known; the report keeps backtests separate. It is the calibration the ledger will apply once it has nine cases.

**Real seals were placed on 2026-10-19** for G-001 to G-004. Any measurement published after that date scores them. Predictive power stays **held open** until those scores exist.

## Keeping it alive

```bash
python3 formula/ledger.py add G-001 --value 70.4 --sigma 1.9 --method "TRGB (JWST)" \
    --source "Author et al. YYYY, Journal" --url https://arxiv.org/abs/XXXX.XXXXX --date YYYY-MM-DD
python3 formula/ledger.py run          # re-evaluate, log movements, rewrite REPORT.md
python3 formula/ledger.py seal G-001   # freeze a new prediction, then commit before adding more evidence
python3 formula/ledger.py new G-006 "question" --quantity "..." --unit "..."
python3 formula/ledger.py run --as-of 2019-12-31   # replay what was known on a date
```

Rules that keep it honest:

- **Every evidence row carries a source URL and a date.** An entry without a primary source is not added.
- **The evidence date is the publication date, not the entry date.** Evidence published before a seal never scores that seal. A result can't be used to "confirm" a prediction it was known before.
- **Theory predictions are witnesses, but they never score a seal.** Only new measurements do.
- **A witness is an independent method.** Splitting one experiment into several "methods" would fake agreement.
- **Commit after every `seal`.** The git timestamp is the proof that the prediction came first (`audit/prediction/PROTOCOL.md`).

## Held open about the ledger itself

- **The seed is incomplete.** It holds the landmark results for each gap, not every result. Newer measurements exist for H₀ (JWST-era TRGB/JAGB/Cepheid, 2024–2026) and need to be added with their publication dates. The current statuses reflect the seed, not the full literature.
- **The method is ordinary statistics.** Weighted combination, chi-square consistency and leave-one-out tests are the standard tools of meta-analysis (as in the Particle Data Group's scale factors). The framework contributes the discipline around them: statuses, refusing to fill boundaries, locating the work, sealed self-scoring, and the movement log.
- **It cannot decide *why* witnesses disagree.** It can say which one is out of line, and how precise the next measurement must be. Whether the cause is a systematic error or new physics stays held open until that measurement exists.
- **It does not solve boundary gaps.** It narrows them only from their measurable side.
