---
id: CONST-bremermann-limit
canon_ref: "v5.1 Appendix D, Information & Computation Laws, row 'Bremermann’s Limit' (versions/v5.1/GFunnel-Methodology-v5.1.md line 2059)"
canon_label: "Bremermann’s Limit"
diff_state: conflict
exclusion_diagnosis: reached-conflicting
claim_outcome: forced-fill
intake_result: adjusted
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix D (Fundamental Constants & Laws Registry), *Information & Computation Laws*, line 2059:

> **Law:** Bremermann’s Limit  
> **Statement:** ~1.36×10⁵° bits/second/kg  
> **Framework Role:** Maximum rate of computation per unit mass. Per Process Density (Layer III): there is a physics ceiling on how much organized complexity can fit per unit substrate.

**Split (RUNBOOK rule 4).** *Factual core graded here:* the maximum computation rate per unit mass is ~1.36 × 10⁵° bit s⁻¹ kg⁻¹ (as printed).

*Framework mapping (not graded; see Narrative stripped):* 'a physics ceiling on how much organized complexity can fit per unit substrate' (Process Density).

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Speed of light in vacuum c | 299 792 458 m s⁻¹ | exact (defined SI value) | measured-reproduced | https://physics.nist.gov/cgi-bin/cuu/Value?c | 2026-09-24 |
| Planck constant h | 6.626 070 15 × 10⁻³⁴ J Hz⁻¹ | exact (defined SI value) | measured-reproduced | https://physics.nist.gov/cgi-bin/cuu/Value?h | 2026-09-24 |
| Bremermann limit c²/h (computed) | 1.3564 × 10⁵⁰ bit s⁻¹ kg⁻¹ | exact given c, h | derived | audit/constants/appendix_d_checks.py | 2026-09-24 |

c and h are exact defined SI values (CODATA); they are graded `measured-reproduced` as the defining reference values. The limit itself is a theoretical bound (mass-energy plus a quantum speed limit); no experiment tests it directly.

## Scientific Inquiry run

1. Question (precise): What is c²/h, and does canon print it correctly?
2. What an answer must look like: A number in bit s⁻¹ kg⁻¹ compared with canon's printed value.
3. Falsifiability condition: Canon's printed value differs from c²/h.
4. Variables: measurable / bounded / held open: Measurable: c, h (exact). Bounded: n/a. Held open: whether the bound is ever physically approached.
5. Test designed: Compute c²/h with the stdlib script from CODATA values.
6. Data (unfiltered): c²/h = 1.3564 × 10⁵⁰. Canon prints '~1.36×10⁵°' (a degree sign where the superscript zero of 10⁵⁰ should be).
7. Variable Principle applied: The mantissa matches; the exponent is corrupted in transcription. Read literally, canon says 10⁵ (or is unreadable).
8. Model update (Capsule: what the failed parts contribute): Correct to '~1.36 × 10⁵⁰ bits/second/kg'.
9. Documented: This file; appendix_d_checks.py section 1.
10. Next baseline: Adjusted value carried forward.

## Forcing Test

- Test A (Ground): Grounded in exact constants.
- Test B (Uniqueness): One value.
- Test C (Direction): n/a.
- Test D (Falsifiability): Arithmetic check; canon fails on the exponent.
- **Outcome:** `forced-fill` for the corrected value 1.36 × 10⁵⁰.

## Anti-Operation (the gap this opens)

The bound assumes all rest mass is available as computational energy. How close any real substrate can come is not measured; the registry treats a theoretical ceiling as if it were a known operating limit.

## Narrative stripped

Removed: 'Per Process Density ... organized complexity per unit substrate'. Bremermann's limit bounds bit operations per second per kilogram; it says nothing about 'organized complexity'. Reality does not force the mapping.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
