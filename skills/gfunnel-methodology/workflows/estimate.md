# Workflow — Estimate, Fill a Gap, Forecast, or Compare Systems

Use for: "fill in the blanks", "predict what happened / will happen", "what's the missing number", "compare these two datasets", "where do these measurements disagree", "narrow this open question", "can system A tell us about system B", and any task whose deliverable is **a number that is not yet in the record**.

This workflow is the Estimate Protocol (`substrate/2026-10-20-estimate-protocol.md`) made operational. Its rule: **never fill a variable silently; never refuse to fill one that has a prior, structure, analogue or trend.** Every quantity you emit carries a tag, a range and a falsifier.

## 0. Decide what to load (this is where the time goes)

| Task | Load | Do **not** load |
| --- | --- | --- |
| Estimate / forecast / fill a gap / compare | this workflow · the Variable Principle · the Forecasting Algorithm (v5.1 `SECTIONS.md` → *Forecasting Algorithm*) · Layer ◇ step 2 (the falsifier rule) · the Forcing Test outcomes (`framework/registers.md` §2) | Layers I–VII content (Three Kingdoms placement, Hermetic principle, dynamic middle). They are **diagnostic** steps for a stuck process; on an estimate they consume the budget and add no accuracy (`audit/VERDICT.md`). |
| Diagnose something stuck or failing | `workflows/run-algorithm.md` — the full methodology | — |
| Both ("why is it stuck *and* what will revenue be") | run `run-algorithm.md` for the diagnosis, then **this** workflow for every number the diagnosis leaves open | — |

Say which you loaded. A forecast that quotes the Hermetic principles is a routing error, not thoroughness.

## 1. Route to the tool

All tools are in `formulas/` (standard library Python; `python3 formulas/<tool>`). Pick by the shape of the input:

| The input is… | Run | It returns |
| --- | --- | --- |
| **A table with empty cells** (rows × variables; spreadsheets, P&Ls, lab tables, CRM exports) | `omni_gap.py` → `OmniGap(columns, rows, identities, bounds, tolerance).fill()` | one tagged estimate per empty cell: value, 90% range, tag, falsifier, next measurement |
| **One quantity, several measurements or theories that may disagree** (an open scientific or business question) | `ledger.py` → `new`, `add`, `run`, `seal` | status per gap (narrowed / conflict / held-open), the witness that restores agreement, the precision a decisive measurement needs |
| **A situation now (or N months ago) and a request to predict metrics** | `forecast.py` → `new`, fill the sheet, commit, `score` | a sealed, two-arm prediction sheet with every metric tagged; later, a scored hit rate and error per tag |
| **Two systems, one thin, one rich, that may correspond** | `omni_gap.py` with `correspondences=[Correspondence(name, cols, rows, mapping)]`; pattern in `correspondence_test.py` | estimates in the thin system using the rich system's relation, plus a per-column verdict: correspondence **held** / **not supported here** |
| **No table, no file — the user wants a number in conversation** | run the protocol **by hand** (§3 below) | the same card, written out |

Several can apply. A forecast of a P&L is `forecast.py` for the protocol and `omni_gap.py` for the cells.

## 2. Run it (exact invocations)

```bash
# table with gaps
python3 - <<'EOF'
import sys; sys.path.insert(0, "formulas")
from omni_gap import OmniGap, Correspondence
og = OmniGap(columns, rows,                         # rows: lists of float or None (None = the gap)
             identities=[({"revenue": 1, "cogs": -1, "gross": -1}, 0.0)],   # exact relations, if any
             bounds={"revenue": (0, None)},
             tolerance={"gross": 50_000},             # the error size that would change a decision
             alpha=0.10)                              # stated (and measured) miss rate
for f in og.fill():
    print(f.row, f.column, f.status, f.value, (f.lo, f.hi), f.falsifier, f.next_measurement)
EOF

# open question with competing measurements
python3 formulas/ledger.py new G-006 "question" --quantity "..." --unit "..."
python3 formulas/ledger.py add G-006 --value 70.4 --sigma 1.9 --method "independent method name" \
    --source "Author et al. YYYY, Journal" --url https://... --date YYYY-MM-DD
python3 formulas/ledger.py run            # re-evaluates every gap, logs movements, rewrites ledger/REPORT.md
python3 formulas/ledger.py seal G-006     # freezes the current range as a prediction; commit before adding evidence

# forecast test (two arms)
python3 formulas/forecast.py new situation.json sheet.json   # then fill EVERY row in both arms
git add sheet.json && git commit -m "seal forecast"           # the commit is the seal
python3 formulas/forecast.py score sheet.json actuals.json   # only after the actuals exist

# correspondence: a thin system calculated from a parallel one
python3 formulas/correspondence_test.py   # the pattern; copy its Correspondence(...) call for your pair
```

Rules the tools enforce and you must keep when working by hand:

- **Only measured values feed an estimate.** A fill never becomes the input to another fill.
- **The evidence date is the publication date.** Evidence known before a seal never scores it.
- **One witness = one independent method.** Repeat results from one experiment are combined first.
- **Log-transform power laws** before using Correspondence; the transfer is linear in standardized space.

## 3. The protocol by hand (no file, just a question)

For every quantity the user needs, produce this card:

```
<quantity>: <value> <unit>   [tag: measured | forced | estimate | assumption | held-open | conflict]
  range   : <low> – <high> (<coverage>%)
  method  : prior (what things of this kind usually look like) ·
            structure (what the known values in THIS case imply) ·
            analogue (nearest comparable cases) ·
            trend (earlier readings of the same quantity)
  falsifier: <the observation and threshold that would show the value wrong>
  next     : <the one measurement that would narrow this most>
```

- `estimate` when at least one of prior / structure / analogue / trend is stated and used.
- `assumption` when the value rests on judgement alone. Still give a range and a falsifier. Say the word.
- `held-open` **without a value only if all four are absent.** Anything that has happened before has a prior. "I don't know" is not a reason.
- `forced` when identities leave one value. `conflict` when the evidence disagrees with itself: name the witnesses and which one, removed, restores agreement.

## 4. Report

- Lead with the numbers, tagged. The protocol exists so the user gets the value *and* its honesty, not the honesty instead of the value.
- Name the tool or the by-hand route, the inputs used, and what you did **not** load (§0).
- List what stayed open and the measurement that would close each item.
- If any output was a prediction, say it is sealed only once it is committed, and how it will be scored.
- Attach the credit line when canon text is reproduced (`SKILL.md` §5).

## Never

- Return a list of held-open variables as the answer to a request for a number.
- Report an estimate or assumption as measured, or promote an open variable to resolved.
- Use a filled value as an input to another fill.
- Call Correspondence "held" by assumption. It is held when the engine (or your by-hand check against known cases) shows the transfer recovers known values; otherwise say *not supported here*.
