---
id: PRED-001
target: "Fraction of total protein mass that a bacterium allocates to ribosomal protein at its maximum growth rate"
organism: "E. coli K-12 (or the best-measured bacterium at maximal growth rate)"
framework_route: "v5.1 Layer III+ (Integration Density), 'The Golden Ratio Of Integrated Purpose' and the Application table; with Layer III 'Why φ = 1.618... Is the Ratio'"
prediction_kind: quantitative
tolerance: "HIT if the measured fraction falls within ±0.03 of 0.618 or within ±0.03 of 0.382. MISS otherwise. (±0.03 is chosen as roughly the measurement spread such proteome fractions are usually quoted with; it is fixed here and may not be widened later.)"
contamination_risk: medium
discriminating: yes
lookup_status: withheld
phase_a_commit: null
verdict: null
---

## Target

At its maximum growth rate, a bacterium divides its protein between the machinery that makes more protein (ribosomes) and everything else. The target is that split: ribosomal protein as a fraction of total protein mass, at the highest growth rate at which it has been measured.

This is a real allocation optimum, which is what makes it a fair test of a claim about optimal allocation: a cell growing as fast as it can has settled the trade-off between building machinery and using it.

## Framework route (the algorithm, run literally)

v5.1 Layer III+, *The Golden Ratio Of Integrated Purpose*, run as stated:

1. Canon states: *"each cycle's integration is informed by the two prior cycles' integrations, which are themselves informed by their prior pairs, and so on. The recursion produces a ratio that approaches phi (1.618) — not by coincidence but by the same structural mathematics."*
2. Canon's *Application — How To Operate At Integration Density* table gives three regimes: **Below Threshold (Searching)** · **At Threshold (Phi)** · **Above Threshold (Rigid)**.
3. Layer III, *Why φ = 1.618... Is the Ratio*, states φ is where *"a system divides itself such that the ratio of the whole to the larger part equals the ratio of the larger part to the smaller part"*, and calls the Fibonacci recursion *"the optimal growth sequence"*.
4. A bacterium at maximum growth rate is, by canon's own table, at threshold: it is neither searching (sub-optimal) nor rigid (over-committed). Canon's placement for that state is **At Threshold (Phi)**.
5. The system divides one quantity (total protein) into a larger and a smaller part. Canon's φ division of a whole into two parts gives 0.618 / 0.382.
6. Therefore canon locates the optimal allocation at a φ division: the growth machinery is either the larger part (0.618) or the smaller part (0.382).

## Derivation trace

Canon asserts, for any system at its optimum, that the split between its parts approaches φ, and it asserts this of growth specifically (*"the optimal growth sequence"*, *"the growth pattern of all living systems"*). A bacterium at maximum growth rate is a system at a growth optimum, dividing itself in two. If canon's claim has content beyond metaphor, this is exactly where it should show: the measured fraction should be one of the two φ parts. Which of the two is not fixed by canon, so both are allowed — this makes the test *easier* for canon, deliberately.

## Prediction

The measured ribosomal-protein mass fraction at maximum growth rate is **0.618 ± 0.03**, or **0.382 ± 0.03**.

## Tolerance (what counts as a hit / a miss)

- **HIT:** inside either band.
- **MISS:** outside both bands. No wider band, no third φ-derived value, and no rescaling of the denominator will be accepted after the reveal. If the best-measured value is a range, the hit requires the whole quoted range to fall inside a band.

## Framework-free default

Without the framework there is no reason to expect φ. A cell must allocate *some* protein to ribosomes and cannot allocate all of it; the prior is "somewhere between a few per cent and about half", flat across that interval. The framework's prediction is a sharp claim inside that interval, so the test discriminates: a hit is unlikely by chance (the two bands together cover 0.06 of a roughly 0.5-wide plausible interval, about 12%), and a miss is informative.

## Contamination disclosure

The executor is a language model trained on the scientific literature and may carry prior knowledge of this quantity. Graded **medium**: proteome-allocation figures for fast-growing *E. coli* are widely published, and the executor has a vague impression that the value is well below 0.618, which is why both φ parts are allowed rather than only the larger. That impression is not a retrieved value and no source has been consulted. A reader should treat a MISS here as more trustworthy than a HIT, since a hit could reflect recall of a value near 0.382.

This session has already handled measured bacterial data from three sweep workers. None of them reported this quantity as a fraction of total protein at maximum growth rate; what was reported (an inactive-ribosome fraction, and a proteome share at *slow* growth) is a different quantity at a different growth rate. The executor is nonetheless not a clean-room predictor, and the protocol's own remedy applies: the author can re-run this test by sealing a prediction before anyone fetches the number.

<!-- PHASE B BELOW THIS LINE — must be empty when Phase A is committed -->
## Measured

## Verdict

## What this does and does not show
