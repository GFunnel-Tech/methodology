# Prediction Protocol — the withheld-answer test

> **Status: derivation.** Canon has no procedure for testing whether the framework can *produce* knowledge rather than record it. This file defines one. It is a derivation until the author declares it into a version.

## Why this exists

The Reality Audit's first pass tested what canon **says** against measurement. It found that canon's measured content matches the scientific record because it was recorded from it, and that v5.4 states **zero novel predictions** ([`../cost/README.md`](../cost/README.md) §B). That answers "is it right?" but not the question the author actually cares about:

> Could the methodology have **found** this, from its principles, without being told the answer?

A framework that only matches what it copied has organizing value. A framework that states a measured quantity **before** the measurement is consulted has predictive value. The two are not the same, and only the second is evidence that the principles do work.

## The rule that makes it a test

> **The prediction is committed to git before the measurement is fetched.**

The commit hash and its timestamp are the record. A prediction written after the lookup is not a prediction, and the git history is what distinguishes them. Each `PRED-###` file therefore has two phases:

**Phase A — sealed.** `lookup_status: withheld`. The file states: the target, the framework route, the derivation trace, the prediction, the tolerance that counts as a hit, and the contamination grade. **No measured value anywhere in the file.** Committed and pushed. Nothing else may be in that commit.

**Phase B — revealed.** Only after Phase A is pushed: fetch the measurement from a primary source, record it with its URL and retrieval date, and score against the tolerance Phase A already fixed. `lookup_status: revealed`. The Phase A text is never edited — corrections go in the Phase B section.

Scoring is fixed in Phase A so it cannot be loosened afterwards. A prediction whose tolerance is not stated in Phase A scores `void`.

## The contamination problem (stated, not solved)

The executor here is a language model trained on the scientific literature. It may already know the answer it is "predicting". **This cannot be fully excluded, and the protocol does not pretend otherwise.** What it does instead:

1. **Grade the risk.** Every prediction carries `contamination_risk`:
   - `high` — a textbook constant the executor almost certainly knows (ribosome count, genome size). Such a prediction is **worth little as evidence** even if it hits.
   - `medium` — a quantity in the literature but not commonly memorised.
   - `low` — a quantity that is obscure, recently measured, or organism-specific enough that recall is unlikely; or a *structural* prediction whose content is a relationship the framework forces, not a number to recall.
2. **Prefer structure over recall.** The strongest test is not "guess the number" but "the framework says these two quantities must stand in this relation" — a claim that is wrong in a checkable way.
3. **State the alternative.** Phase A must name what a framework-free guess would say. If the framework's prediction is the same as the obvious default, the test discriminates nothing, and that is recorded as `non-discriminating` however well it hits.
4. **A human can do better.** The honest version of this test is run by someone who fetches the measurement only after the author's prediction is sealed. This protocol is built so the author can re-run it that way; the executor's own runs are labelled as the weaker version they are.

## Required front matter

```yaml
id: PRED-001
target: "what is being predicted, in neutral words"
organism: "E. coli K-12"            # or n/a
framework_route: "v5.1 Layer I.C Domain 9 algorithm, steps 1-7"   # which algorithm, run literally
prediction_kind: quantitative       # quantitative / ordinal / structural
tolerance: "within a factor of 3"   # fixed in Phase A; what counts as a hit
contamination_risk: low             # low / medium / high
discriminating: yes                 # does it differ from the framework-free default?
lookup_status: withheld             # withheld (Phase A) / revealed (Phase B)
phase_a_commit: null                # filled in Phase B with the Phase A commit hash
verdict: null                       # hit / miss / partial / void / non-discriminating
```

## Required sections

```markdown
## Target
## Framework route (the algorithm, run literally — numbered steps, no skipping)
## Derivation trace
## Prediction
## Tolerance (what counts as a hit / a miss)
## Framework-free default (what you would say without the framework)
## Contamination disclosure
<!-- PHASE B BELOW THIS LINE — must be empty when Phase A is committed -->
## Measured
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
## Verdict
## What this does and does not show
```

## Verdicts

| Verdict | Meaning |
| --- | --- |
| `hit` | Inside the Phase A tolerance, and discriminating. |
| `partial` | Right relation, wrong magnitude; or right for part of the claim. |
| `miss` | Outside tolerance. **A miss is a result, not a failure of the exercise** — it locates where the principles do not reach. |
| `non-discriminating` | Hit, but a framework-free default says the same. No evidence either way. |
| `void` | Protocol broken (no tolerance fixed in Phase A; the answer appeared before the seal; the route was not run literally). |

A run of `non-discriminating` hits is the most likely outcome and must not be reported as predictive success. Per the Variable Principle: the framework's predictive power stays **held open** until a `hit` that is both discriminating and low-contamination exists.

## What a pass would mean

One discriminating, low-contamination `hit` would be the first entry in "knowledge the methodology produced" ([`../cost/README.md`](../cost/README.md) §B, currently $0). It would not make the framework a theory; v5.4's own bar is a measured mass ratio from the tension law. It would make the principles *load-bearing* rather than descriptive — which is exactly what the audit so far cannot show.
