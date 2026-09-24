---
id: CONST-shannon-entropy
canon_ref: "v5.1 Appendix D, Information & Computation Laws, row 'Shannon Information Entropy' (versions/v5.1/GFunnel-Methodology-v5.1.md line 2056)"
canon_label: "Shannon Information Entropy"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix D (Fundamental Constants & Laws Registry), *Information & Computation Laws*, line 2056:

> **Law:** Shannon Information Entropy  
> **Statement:** H = -Σ p_i log₂(p_i)  
> **Framework Role:** Quantifies the uncertainty in a message — exactly what the Variable Principle describes qualitatively. Information IS resolved variability.

**Split (RUNBOOK rule 4).** *Factual core graded here:* the Shannon entropy of a discrete source is H = -Σ p_i log₂ p_i (bits).

*Framework mapping (not graded; see Narrative stripped):* 'exactly what the Variable Principle describes qualitatively'; 'Information IS resolved variability'.

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Paper defining the entropy of a discrete source (bibliographic record) | Shannon, 'A Mathematical Theory of Communication', Bell System Technical Journal, 1948-07 | n/a | derived | https://api.crossref.org/works/10.1002/j.1538-7305.1948.tb01338.x | 2026-09-24 |

A proved theorem is not a measurement. Rows graded `derived` record the published statement the canon wording was checked against; no experiment can raise or lower their grade. The paper text itself was not retrieved in this run; the formula is checked against its standard form (a definition plus Shannon's uniqueness theorem), which canon reproduces exactly, including the base-2 logarithm for bits.

## Scientific Inquiry run

1. Question (precise): Is H = -Σ p_i log₂(p_i) the correct statement of Shannon entropy?
2. What an answer must look like: A match or mismatch between canon's formula and the published definition.
3. Falsifiability condition: Canon's formula differs from the definition (sign, base, or summand).
4. Variables: measurable / bounded / held open: Measurable: none (definition). Bounded: n/a. Held open: none.
5. Test designed: Compare canon's formula with the definition in Shannon (1948).
6. Data (unfiltered): Canon: H = -Σ p_i log₂(p_i). Standard definition: identical (base 2 gives bits).
7. Variable Principle applied: Nothing is held open for the formula; the mapping to the Variable Principle is interpretation.
8. Model update (Capsule: what the failed parts contribute): No update needed for the core. The mapping is filed as narrative.
9. Documented: This file.
10. Next baseline: Formula integrated as stated.

## Forcing Test

- Test A (Ground): Grounded in a proved definition/theorem, not a measurement.
- Test B (Uniqueness): Unique: given Shannon's axioms, H is unique up to the log base.
- Test C (Direction): Canon's direction (minus sign, p log p) is correct.
- Test D (Falsifiability): Falsifiable only as a transcription check; passes.
- **Outcome:** `forced-fill` for the formula. The 'Information IS resolved variability' reading is not forced.

## Anti-Operation (the gap this opens)

Canon does not say which *probability model* the p_i come from. For any empirical system the entropy depends on the chosen partition and model; that choice is a held-open variable the registry does not name.

## Narrative stripped

Removed: 'exactly what the Variable Principle describes'. Shannon entropy is a functional of a probability distribution; it does not refer to the Variable Principle. Reality neither forces nor contradicts the analogy; it is interpretation.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
