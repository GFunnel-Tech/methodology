---
id: CONST-landauer-principle
canon_ref: "v5.1 Appendix D, Information & Computation Laws, row 'Landauer’s Principle' (versions/v5.1/GFunnel-Methodology-v5.1.md line 2058)"
canon_label: "Landauer’s Principle"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix D (Fundamental Constants & Laws Registry), *Information & Computation Laws*, line 2058:

> **Law:** Landauer’s Principle  
> **Statement:** Erasing 1 bit dissipates kT·ln(2) joules  
> **Framework Role:** Information has thermodynamic cost. Per Layer I.E + I.G: information conservation has a physical floor — erasing information requires energy expenditure, confirming the Capsule mechanism’s thermodynamic necessity.

**Split (RUNBOOK rule 4).** *Factual core graded here:* erasing one bit dissipates kT·ln 2 of energy. (Measured form: *at least* kT·ln 2 on average.)

*Framework mapping (not graded; see Narrative stripped):* 'confirming the Capsule mechanism's thermodynamic necessity'; 'information conservation has a physical floor'.

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Boltzmann constant k | 1.380 649 × 10⁻²³ J K⁻¹ | exact (defined SI value) | measured-reproduced | https://physics.nist.gov/cgi-bin/cuu/Value?k | 2026-09-24 |
| kT·ln 2 at 300 K (computed) | 2.8710 × 10⁻²¹ J (17.92 meV) | exact given T | derived | audit/constants/appendix_d_checks.py | 2026-09-24 |
| Mean heat to erase one bit, colloidal particle in double well, long-cycle limit | saturates at the Landauer bound | see paper | measured-reproduced | https://arxiv.org/abs/1503.06537 (Bérut et al.; Nature paper: https://api.crossref.org/works/10.1038/nature10872) | 2026-09-24 |
| Work to erase one bit, feedback trap (colloid) | at least kT ln 2; single cycles can fall below (Jarzynski) | see paper | measured-reproduced | https://arxiv.org/abs/1408.5089 (Jun, Gavrilov, Bechhoefer 2014) | 2026-09-24 |
| Minimum energy dissipated switching a nanomagnetic bit | consistent with k_B T ln 2 | see paper | measured-reproduced | https://api.crossref.org/works/10.1126/sciadv.1501492 (Hong et al. 2016) | 2026-09-24 |

Three independent groups (two colloidal systems, one nanomagnetic) report agreement with the bound, hence `measured-reproduced`.

## Scientific Inquiry run

1. Question (precise): Does erasing one bit cost kT ln 2, and is canon's wording ('dissipates kT·ln(2)') correct?
2. What an answer must look like: Measured erasure heat/work compared with kT ln 2.
3. Falsifiability condition: Reproduced erasure below kT ln 2 on average.
4. Variables: measurable / bounded / held open: Measurable: heat/work per erasure, T. Bounded: the mean is ≥ kT ln 2. Held open: none for the bound.
5. Test designed: Collect independent erasure experiments.
6. Data (unfiltered): Bérut et al.: saturates at the bound in the long-cycle limit. Jun et al.: 'at least kT ln 2'; individual cycles can go below. Hong et al.: consistent with the limit.
7. Variable Principle applied: The bound is a minimum, not an exact cost. Canon's 'dissipates kT·ln(2)' reads as an equality; the measured form is ≥.
8. Model update (Capsule: what the failed parts contribute): Re-word: 'erasing one bit dissipates at least kT·ln 2 on average'.
9. Documented: This file.
10. Next baseline: Integrated as a lower bound.

## Forcing Test

- Test A (Ground): Grounded in reproduced measurement.
- Test B (Uniqueness): One bound value (kT ln 2) survives.
- Test C (Direction): Direction: minimum, not equality.
- Test D (Falsifiability): Falsifiable and tested; passed.
- **Outcome:** `forced-fill` for the lower bound.

## Anti-Operation (the gap this opens)

Real devices dissipate orders of magnitude above the bound; the gap between the Landauer floor and practical erasure cost is not addressed by the registry.

## Narrative stripped

Removed: 'confirming the Capsule mechanism's thermodynamic necessity' and 'information conservation'. Landauer's principle prices *erasure*, the logically irreversible removal of information from a memory (its entropy is exported to the environment). It does not show that information is integrated or conserved in the Capsule sense. Reality neither forces nor contradicts the Capsule mapping.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
