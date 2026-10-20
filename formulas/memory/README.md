# Memory — the by-product of running the formula

> Derivation, not canon. Code: [`../memory.py`](../memory.py). Test: [`../memory_test.py`](../memory_test.py).

There is no memory layer to fill. Every run of a formula appends one **record** to `runs.jsonl`:

| Field | What it holds | What it never holds |
| --- | --- | --- |
| `fingerprint` | a hash of the inputs' shape and per-column summary | the raw data |
| `expression` | what the formula did: per variable, the channels actually available (`P`, `P+R+S`, `P+C1+R+S` …), the learned weights, the 90% half-width **in sd units**, the number of calibration cases, the correspondence verdict | — |
| `output` | tag counts, mean narrowing, and for forecasts and ledger seals the scored rows (tag, hit, required widening) | — |
| `conjugate` | the measurement the run most often named as the one that would narrow its gaps | — |

Records are content-addressed: the same inputs and expression produce the same id, so nothing is stored twice and "has this been computed?" is a lookup. The log **is** the memory (Layer VI step 6: *if it isn't written, it isn't real*). Everything the system "remembers" is recomputed from it on demand (Layer I.G: the present is the integration of every prior path).

## What is recomputed from the log

| Call | Returns | Used by |
| --- | --- | --- |
| `recall(variable, expression, n)` | calibration earned on this variable by prior runs **with the same expression and the same size regime** (log₂ bucket of calibration cases): pooled weights and half-width in sd units | `OmniGap` when its own calibration rests on few cases (`POOL_BELOW`, default 30): the width is pooled by case count and the output says so (`note: calibration pooled with memory (k runs, n cases, same expression and size regime)`) |
| `reliability()` | per tag (`estimate`, `assumption`, `ledger-range` …): how often it was right, and the widening that would have made 90% of them hits, across every scored forecast and sealed prediction | the Estimate Protocol's learned widening; `forecast.py score` and `ledger.py run` write the scored rows |
| `show()` | what the system knows and from how many runs | you |

## What the test found (and kept as controls)

`python3 formulas/memory_test.py` teaches from one run on the full Auto-MPG table, then fills thin tables with and without memory, 40 tables per regime.

| Design | Regime | Coverage of the stated 90% range | Verdict |
| --- | --- | --- | --- |
| memory keyed by **variable** (first attempt) | 16-row tables | **66%** | wrong: the full table's narrow width was learned with structure and analogue channels the thin tables could not fit |
| keyed by variable + **expression** | 28-row tables, same channels | **71.5%** | still wrong: an estimator trained on 20 rows is not the estimator trained on 300, even with the same channels |
| keyed by variable + expression + **size regime** (current) | A · 16-row, different expression | 91.2% (vs 94.1% alone) | does not pool across regimes; harmless |
|  | B · 28-row, different regime from the teacher | 92.2% (vs 92.3% alone) | same |
|  | C · 28-row after 40 prior 28-row tables | 91.1% (vs 92.3% alone), ranges **4% tighter**, mis-calibration 5.4% vs 5.7% | the one legitimate regime: a modest gain |

**The finding that matters:** calibration is a property of the *calculation and its regime*, not of the variable. Carried across regimes it is an assumption, and the test measured what that assumption costs (24 points of coverage). The engine now refuses that transfer by construction. What memory can carry across runs without harm: the same expression in the same regime (a small stabiliser), the reliability of each **tag** across every scored prediction, the correspondence verdicts, the conjugate gaps, and the fact that a computation already exists.

## Rules

1. **No raw data enters memory.** Fingerprints and statistics only. The log can be committed.
2. **Memory never overrides measurement.** A run that can calibrate itself on ≥ 30 cases ignores memory. Below that, widths are pooled by case count and the source is named in the output.
3. **Only self-calibrated runs teach** (≥ 9 cases, source "this run"). A run that was itself pooled does not re-teach what it borrowed.
4. **Append only.** Records are never edited; a corrected result is a new record whose note says what it corrects.

`runs.jsonl` in this directory is the repository's own log. It starts empty; `benchmark.py` and `correspondence_test.py` do not write to it (they pass no memory), and `memory_test.py` uses a temporary one. `ledger.py run` and `forecast.py score` write to it once real predictions are scored.

```
Source: GFunnel Methodology (Omni Process) v5.4, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Adapted; not endorsed by the author.
```
