---
id: CONST-atp-yield-per-glucose
canon_ref: "v5.1 Appendix D, Biological & Scaling Laws, row 'ATP Yield Per Glucose' (versions/v5.1/GFunnel-Methodology-v5.1.md line 2082)"
canon_label: "ATP Yield Per Glucose"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: live-hypothesis
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix D (Fundamental Constants & Laws Registry), *Biological & Scaling Laws*, line 2082:

> **Law:** ATP Yield Per Glucose  
> **Statement / Value:** ~32 ATP (eukaryotic)  
> **Framework Role:** The output of full aerobic respiration. Per Layer I.E: the energy conserved across all stages from photon to ATP, transformed in form, identical in quantity.

**Split (RUNBOOK rule 4).** *Factual core graded here:* full aerobic respiration yields ~32 ATP per glucose in eukaryotes.

*Framework mapping (not graded; see Narrative stripped):* 'the energy conserved across all stages from photon to ATP, transformed in form, identical in quantity.'

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Mechanistic P/O ratio, NADH-linked substrates / succinate | about 2.5 / 1.5 | 'consistent with most reports' | measured-reproduced | https://pubmed.ncbi.nlm.nih.gov/15620362/ (Hinkle 2005) | 2026-09-24 |
| Alternative P/O if H⁺/ATP = 10/3 | 2.3 / 1.4 | possible, per same review | measured-single | https://pubmed.ncbi.nlm.nih.gov/15620362/ | 2026-09-24 |
| ATP/glucose, P/O 2.5/1.5, malate–aspartate / glycerol-phosphate shuttle | 32.0 / 30.0 | from P/O | derived | audit/constants/appendix_d_checks.py | 2026-09-24 |
| ATP/glucose, P/O 2.3/1.4, same two shuttles | 29.8 / 28.0 | from P/O | derived | audit/constants/appendix_d_checks.py | 2026-09-24 |
| Reducing equivalents per glucose (glycolysis R01061 ×2, PDH R00209 ×2, TCA ×2 turns) | 10 NADH, 2 succinate oxidations, 4 net substrate-level ATP/GTP | exact | measured-reproduced | https://rest.kegg.jp/get/M00009 ; https://rest.kegg.jp/get/R01061 ; https://rest.kegg.jp/get/R00209 | 2026-09-24 |

The yield is derived: carriers × P/O + substrate-level phosphorylation. Proton-leak and transport costs are not modelled in the stdlib script.

## Scientific Inquiry run

1. Question (precise): Is ~32 ATP per glucose correct?
2. What an answer must look like: A derived range from measured P/O ratios.
3. Falsifiability condition: A derived range excluding 32.
4. Variables: measurable / bounded / held open: Measurable: P/O ratios. Bounded: 28–32. Held open: which shuttle and which H⁺/ATP value apply in a given cell.
5. Test designed: Derive yield from KEGG stoichiometry and Hinkle's P/O ratios.
6. Data (unfiltered): 32.0 (2.5/1.5, malate–aspartate), 30.0 (glycerol-phosphate), 29.8 / 28.0 with H⁺/ATP = 10/3.
7. Variable Principle applied: ~32 is the upper end of a 28–32 range; not a single value.
8. Model update (Capsule: what the failed parts contribute): State '~30–32 (upper bound of mechanistic estimates)'. Canon's ≈32 is within range.
9. Documented: This file; appendix_d_checks.py section 3.
10. Next baseline: Integrated with range.

## Forcing Test

- Test A (Ground): Grounded in measured P/O ratios.
- Test B (Uniqueness): Not unique: 28–32 depending on shuttle and H⁺/ATP.
- Test C (Direction): n/a.
- Test D (Falsifiability): Falsifiable via P/O measurement.
- **Outcome:** `live-hypothesis` for the point value; the range 28–32 is well bounded.

## Anti-Operation (the gap this opens)

Yield per glucose in vivo also depends on proton leak and transport costs, which no row of the registry covers.

## Narrative stripped

Removed and flagged: 'the energy conserved ... identical in quantity'. Total energy is conserved (first law), but only part of glucose's free energy is captured as ATP; the rest is released as heat. 'Identical in quantity' is wrong if read as ATP capture. The capture efficiency itself was not computed here (ΔG values not fetched).

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
