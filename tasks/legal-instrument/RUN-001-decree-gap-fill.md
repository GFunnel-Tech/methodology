# Run 001 — Estimate Protocol applied to a legal instrument

> **Status: domain derivation. Not canon.** The framework names no legal domain and no algorithm for drafting an instrument. This run applies the **Estimate Protocol** (`substrate/2026-10-20-estimate-protocol.md`) to a domain the canon does not name, per `AGENTS.md` rules 4 and 7. Nothing here is promoted to a released version.

**Date:** 2026-11-10 · **Mode:** Estimate (instruments only) · **Operator:** Claude, directed by the author
**Instrument:** a proposed final decree with four empty variables
**Loaded:** Variable Principle · Estimate Protocol §§1–4 · falsifier rule
**Not loaded:** the 17 layers, the Three Kingdoms, the Hermetic principles, the Dynamic Middle — per §5, a routing error on an estimate task

---

## §1 · The gap table as found

Four variables, empty in the draft instrument. Under rule 5 as amended, each must carry a value unless it passes the §3 four-absence test.

| # | Variable | §3 result | Resolution |
|---|---|---|---|
| 1 | Counterparty monthly net resources | prior ✓ structure ✓ | value produced |
| 2 | Child's health premium share | prior ✓ structure ✓ | value produced |
| 3 | Child's dental premium share | prior ✓ structure ✓ | value produced |
| 4 | Account number of a specific deposit | all four absent | `held-open`, correctly |

**§3 passed cleanly.** Three of four gaps admitted a value; the fourth — an arbitrary identifier with no prior, no structure, no analogue and no trend — is exactly the shape §3 was written to protect.

## §2 · Measured tier

From a single counterparty payslip (one two-week period, plus year-to-date totals):

| Quantity | Value | Grade |
|---|---|---|
| Gross per period | $3,360.46 | `measured` |
| Year-to-date gross | $67,209.17 | `measured` |
| Statutory tax withholding per period | $257.34 | `measured` |
| Total pre-tax deductions per period | $336.05 | `measured` |

## §3 · The identity that promoted an assumption to a measurement

Pay frequency and rate constancy were initially an `assumption` — a payslip shows one period, not a schedule.

```
year-to-date gross ÷ gross per period = 67,209.17 ÷ 3,360.46 = 20.00
```

An exact integer. A non-constant rate, or a different frequency, produces a fractional quotient. The identity therefore **forces** biweekly pay at a constant rate, and annual gross follows:

```
3,360.46 × 26 = $87,371.96    monthly $7,281.00    [forced]
```

This is §4 step 2 working as written — *identities first, they force; relations second, they narrow* — and it is worth recording because the promotion was free. No additional source was consulted. The cross-check lived inside the single document already in hand.

**Pattern (candidate):** *when a record carries both a unit figure and a running total, their quotient is an identity that tests the unit's own frequency and constancy. Check it before tagging either as `assumption`.*

## §4 · Where structure beat prior by a factor of three

Gap 2 (child's share of a health premium) was first approached through **prior** — published averages for employer-sponsored dependent coverage. That channel returned roughly $150–$250 per month.

The **structure** channel returned something much tighter. Total pre-tax deductions are measured at $728/month. The dominant component is a retirement contribution at 8–9% of gross `assumption`, consuming $582–$655. The residue available for *all* insurance — both people, health and dental and vision together — is therefore bounded:

```
$728 − $655  ≤  all insurance  ≤  $728 − $582
$73          ≤  all insurance  ≤  $146   per month
```

The child's share must sit inside that. Final estimate **$55/month, range $35–$85** — about one third of what the prior channel returned, and the prior was outside the structural bound entirely.

**Finding:** on this run the prior channel was not merely less precise, it was **excluded by structure**. §4 step 5 weights channels by how well each has recovered known values before; this is one observation in favour of weighting structure above prior whenever a measured relation closes on the target. One run is not a calibration.

## §5 · A fifth reason to hold open, offered against §8's open question

The Estimate Protocol §8 asks: *"Is the §3 test complete? Four absences are named. A fifth kind of evidence may exist."*

This run met a gap that fails §3 — a prior exists, structure exists, the value is knowable — and yet **no value may be emitted**, because the output is not the estimator's to produce. In the instrument, one field records the deciding authority's own stated reasoning. Supplying it would not be an estimate; it would be a forgery of someone else's act.

This is not a fifth kind of *evidence*. It is a fifth reason to hold open, orthogonal to the four:

> **`held-open (authority)`** — the value is knowable and the evidence admits one, but the act of stating it belongs to a party other than the estimator. The hold is institutional, not epistemic.

It needs a distinct tag because the two holds behave differently. An epistemic hold closes when a measurement arrives. An authority hold closes only when the authorised party acts, and no amount of evidence shortens it. Scoring them together would make the protocol's calibration look worse than it is — the authority rows are not failed estimates.

**This is a proposal, not a change.** Released files are immutable and canon corrections are logged rather than applied. It is recorded here for the author to accept, reject, or send to the Forcing Test.

## §6 · What this run does *not* establish

The task that commissioned this run asked to record the methodology as a universal system across all domains. This run does not support that, and the repository's own rules forbid writing it:

- **Rule 7** requires a domain derivation to be *labelled* a derivation. It does not permit promoting one to a general claim.
- **One derivation is one observation.** The Estimate Protocol worked here. That is evidence of applicability in this domain, not evidence of universality across domains the framework has never met.
- **The prohibition is explicit:** *do not present a derived algorithm as a primary one.* A universality claim built on a single run would be exactly that.

What can honestly be said: the Estimate Protocol's §3 test, the channel order in §4, and the routing rule in §5 each behaved as specified on a domain the canon does not name. That is a second independent domain after the Cell Atlas. Universality would need the claim stated as falsifiable, a domain sample that could fail it, and a run that *does* fail.

**Held open:** whether any domain exists in which §3's four absences all hold yet a value is still obtainable. Still unanswered; this run did not test it.

## §7 · Next measurement

The single observation that would most narrow this run's estimates: the counterparty's benefits election statement, showing the employee-only premium tier against the employee-plus-child tier. It would collapse gaps 2 and 3 from `estimate` to `measured` in one document, and would also test the 8–9% retirement `assumption` by subtraction.

---

```
Source: GFunnel Methodology (Omni Process) v5.4, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0.
Adapted for a domain the canon does not name; the adaptation is not endorsed by the author.
```
