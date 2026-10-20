# The Estimate Protocol — Every Open Variable Gets a Calculated, Tagged Value

*Substrate document · 2026-10-20 · Decision by the author (Cameron Garlick) · Loads v5.1–v5.4, the Reality Audit and `formulas/` as prior substrate*

> **Status: substrate — an author decision, logged as a governance departure.** It changes no released version. It changes the **operating protocol** (`AGENTS.md`, the skill) now, and is drafted here for the next version's Variable Principle wording. The Forcing Test has not yet been run on it; until it is, it is recorded as an operator decision, the way `2026-09-24-reality-filter.md` item 7 was.

---

## §0 · The failure this corrects

A user ran a low-commitment test: an AI was given a snapshot of their situation six months earlier and their goals, and asked to predict what happened since, once with the methodology loaded and once without. With the methodology it **missed the hard numbers, analysed worse, and took 3–4× longer**.

The repository's own audit predicts this result. The Variable Principle as operationalised in rule 5 (*"never fill a held-open variable with assumption"*) does not distinguish two different acts:

| Act | What it is | What rule 5 did with it |
| --- | --- | --- |
| **An untagged guess** | a value stated as if known, with no range and nothing that could prove it wrong | forbade it, correctly |
| **A calculated estimate** | a value built from the evidence that exists (base rate, structure, analogue, trend), with a range, a tag saying how it was made, and a falsifier | **also forbade it**, by omission: the protocol gave the AI no permitted way to state one |

An AI following rule 5 literally therefore answers a forecast with a list of held-open variables. That is not honesty. The canon's own Forecasting Algorithm (v5.1 step 1) asks for *"what is being predicted, by when, with what confidence interval"*: the interval was always the intended form. The operating protocol never said so.

The audit found the same gap from the other side: canon has produced **zero** quantities before measurement (`audit/cost/README.md` §B). A framework that only records and never estimates cannot be tested, and cannot be useful on a question whose answer is not yet in the record.

## §1 · The rule, restated

> **Never fill a variable silently.** Every open variable carries the best value the evidence supports, a range, a tag that says how the value was made, and the observation that would prove it wrong. A tagged, calculated estimate is not an assumption. An untagged value is — even when it is right.

The original wording is kept inside it: *never fill with assumption* becomes *never fill without a tag*. "Hold it open" becomes "keep it visibly open **while** stating the best current value", which is what the Gap Ledger already does for H₀ (a value, a range, a conflict flag, and the measurement that would decide it).

## §2 · The tags

Every quantity in an output carries exactly one tag. The vocabulary extends the three statuses in `framework/registers.md` §1 (measured / derived / held open) without removing any:

| Tag | Meaning | Must carry |
| --- | --- | --- |
| `measured` | taken from a source, with uncertainty | source, date |
| `forced` | follows by logical necessity from measured values (one candidate survives) | the identities used |
| `estimate` | calculated from stated evidence: prior (the Capsule), structure (relations in the same record), analogue (Correspondence), or trend (Rhythm); range calibrated where possible | value, range, method, falsifier |
| `assumption` | a value supplied by judgement with no evidence base beyond it. **Permitted**, because a decision sometimes needs one and an unstated assumption is worse. Scored separately from estimates so its reliability is learned. | value, range, falsifier, and the word *assumption* |
| `held-open` | **no value**, allowed only when the test in §3 passes | the reason, and what would narrow it |
| `conflict` | the evidence disagrees with itself beyond its stated errors | the witnesses, and which one restores agreement if removed |

Measured / forced / estimate correspond to the audit's observation grades (`audit/SCHEMA.md` §1). `assumption` and `conflict` are the two slots the audit found missing (`audit/VERDICT.md`: "two vocabularies are missing the same slot").

## §3 · When `held-open` without a value is allowed

Only when all four are absent:

1. **No prior.** Nothing of this kind has been measured before (so no base rate exists).
2. **No structure.** No identity or measured relation links it to anything known.
3. **No analogue.** No case at another scale or in another domain corresponds to it.
4. **No trend.** No earlier readings of the same quantity exist.

If any one is present, a value can be calculated and must be. "I don't know" fails the test whenever a base rate exists: anything that has happened before has one. The Big Bang's first moment passes the test (v5.4 Gap 1, proven-open). A person's revenue six months from now does not.

## §4 · How an estimate is made (the formula, in words)

This is `formulas/omni_gap.py` (EQ-140) stated for use without a table:

1. **Prior.** What does this quantity usually look like for things of this kind? That is the Capsule: all prior paths. State it.
2. **Structure.** What do the *known* values in this very situation imply about it? Identities first (they force); relations second (they narrow).
3. **Analogue.** What happened in the nearest comparable cases? Correspondence, one scale up or down if needed.
4. **Trend.** If earlier readings exist, where is it heading? Rhythm.
5. **Combine**, weighting each channel by how well it has recovered known values before. If no such record exists, say the weights are judgement (tag the result `assumption`, not `estimate`).
6. **Range.** State the interval and its coverage. Calibrated if there is history; judged if not, and say which.
7. **Falsifier.** The observation and threshold that would show the value wrong.
8. **Next measurement.** The one thing that would narrow the range most.

Steps 1–4 are the Forecasting Algorithm's steps 3–6 (v5.1:3749–3770) made explicit. Nothing is new; the protocol now requires them to **produce a number**.

## §5 · The cost problem (the "3–4× longer")

A forecast does not need the content layers. The operating protocol should load, for an estimate task, only the instruments: the Variable Principle, the Forecasting Algorithm, the Forcing Test, the falsifier rule, and this protocol. The Three Kingdoms placement, the Hermetic principle, and the dynamic middle are diagnostic steps for a *stuck* process; on a forecast they consume the budget and add no accuracy (the audit graded them `vacuous` or `fails` on a real system). This is a routing change in the skill, not a change to canon.

## §6 · How it is tested

`formulas/forecast.py` runs the user's test as a protocol: a sealed prediction sheet in two arms (framework-free vs. methodology), every metric estimated and tagged in both, committed before actuals, then scored per metric: hit rate against stated coverage, error against each metric's own decision tolerance, and the breakdown by tag. The question it answers is the one the user asked: *does the methodology arm estimate better, and does it still refuse anywhere?* A `held-open` count above zero on a question that fails §3 is itself a finding against the protocol.

## §7 · What this does not claim

- It does not claim estimates will be accurate. It claims they will be **stated, tagged, and scorable**, so that their accuracy becomes a measured quantity instead of an unknown.
- It does not change the base code, any released version, or the canon's wording. The v5.1 sentence *"Never fill a variable with assumption"* stands; this protocol defines *assumption* as *untagged*, which the canon left implicit.
- It does not remove `held-open`. It narrows when it may be used without a value (§3).

## §8 · Held open about this protocol

- **Is the §3 test complete?** Four absences are named. A fifth kind of evidence may exist. Open until a case fails all four and still admits a value.
- **Calibration of `assumption` rows.** Until enough are scored, their reliability is unknown. `forecast.py` scores them separately so this becomes measurable.
- **Whether the Forcing Test classifies this as forced or stipulation.** Not yet run.

---

```
Source: GFunnel Methodology (Omni Process) v5.4, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0.
```
