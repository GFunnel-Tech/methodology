---
id: STAGE-005
canon_ref: v5.1 Appendix A, Stage 5
canon_label: "Big Bang Nucleosynthesis"
proposed_label: "Primordial Light-Element Formation"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: adjusted
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix A, row 5:

> **5 · Big Bang Nucleosynthesis** — "Hydrogen, helium, trace lithium. Substrate set. Per Cause and Effect: all later atoms caused at this moment."

v5.4 §5: "**Big Bang.** As an event at a place: forced-false. As the line in motion everywhere (Stage 2): forced — CMB 2.7 K ..., 75/25 H/He, isotropy 1 in 10⁵. The register holds: *event false, phase forced.*" v5.4 §9 row 6: "'The Big Bang never happened'" → "Event false; phase forced".

**Factual core graded here:** in an early hot, dense phase, hydrogen, helium and trace lithium formed (before stars).

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Primordial helium-4 mass fraction Y_p (PDG adopted, from 7 independent HII-region analyses) | 0.245 | 0.003 | measured-reproduced | https://pdg.lbl.gov/2024/reviews/rpp2024-rev-bbang-nucleosynthesis.pdf (eq. 24.3) | 2026-09-24 |
| Primordial helium-4 mass fraction Y_p (PDG astrophysical constants table) | 0.2448 | 0.0033 | measured-reproduced | https://pdg.lbl.gov/2024/reviews/rpp2024-rev-astrophysical-constants.pdf | 2026-09-24 |
| Primordial deuterium D/H x 1e6 (weighted mean, 11 quasar absorption systems) | 25.47 | 0.29 | measured-reproduced | https://pdg.lbl.gov/2024/reviews/rpp2024-rev-bbang-nucleosynthesis.pdf (eq. 24.2) | 2026-09-24 |
| Observed lithium-7 Li/H (Spite plateau, halo stars) | 1.6e-10 | 0.3e-10 | measured-reproduced | https://pdg.lbl.gov/2024/reviews/rpp2024-rev-bbang-nucleosynthesis.pdf (eq. 24.4) | 2026-09-24 |
| Predicted primordial Li/H at concordance baryon density | 4.72e-10 (factor 3.1 above observed; 4.4 sigma) | 0.7e-10 | derived | https://pdg.lbl.gov/2024/reviews/rpp2024-rev-bbang-nucleosynthesis.pdf (sec. 24.5) | 2026-09-24 |
| Baryon-to-photon ratio from BBN (D/H + He concordance) eta_10 | 6.040 | 0.118 | derived | https://pdg.lbl.gov/2024/reviews/rpp2024-rev-bbang-nucleosynthesis.pdf (eq. 24.5) | 2026-09-24 |
| Baryon density from BBN Omega_b h^2 | 0.02205 | 0.00043 | derived | https://pdg.lbl.gov/2024/reviews/rpp2024-rev-bbang-nucleosynthesis.pdf (eq. 24.6) | 2026-09-24 |
| Baryon density from CMB (independent) Omega_b h^2 | 0.0224 | 0.0001 | measured-single | https://arxiv.org/abs/1807.06209 | 2026-09-24 |
| Stellar effect on deuterium | stars destroy D; any detection is a lower limit to primordial D/H | qualitative | derived | https://pdg.lbl.gov/2024/reviews/rpp2024-rev-bbang-nucleosynthesis.pdf (sec. 24.3) | 2026-09-24 |

## Scientific Inquiry run

1. Question (precise): Do measured primordial abundances of D, 4He and 7Li show that H, He and trace Li formed in an early hot phase before stars, and do they agree with the baryon density measured independently from the CMB?
2. What an answer must look like: Primordial abundances with uncertainties from several independent systems, and a single baryon density that fits them and the CMB.
3. Falsifiability condition: No single baryon density fits D/H and Y_p; or the BBN-derived Omega_b h^2 disagrees with the CMB value; or deuterium has a known stellar source.
4. Variables: measurable / bounded / held open: Measurable: Y_p, D/H, Li/H (plateau), Omega_b h^2 (CMB). Derived: eta_10 = 6.040 +/- 0.118. Held open: the cause of the lithium discrepancy (systematics in stellar Li, stellar depletion, nuclear inputs, or new physics; PDG lists all four).
5. Test designed: Fetch PDG 2024 BBN review and constants table and the Planck 2018 parameters abstract; compare BBN-derived baryon density to CMB-derived baryon density; check lithium separately.
6. Data (unfiltered): Y_p = 0.245 +/- 0.003; D/H = (25.47 +/- 0.29)e-6; these two agree at eta_10 = 6.040 +/- 0.118, giving Omega_b h^2 = 0.02205 +/- 0.00043. The CMB gives 0.0224 +/- 0.0001 (difference 0.00035, about 0.8 sigma of the BBN error; computed here). Lithium does not fit: observed 1.6e-10 vs predicted 4.72e-10 (factor 3.1, 4.4 sigma). Stars destroy deuterium, so observed D is primordial or a lower limit. v5.4 §5's "75/25 H/He" agrees with Y_p = 0.245 by mass (rounded).
7. Variable Principle applied: H/He/D formation in an early phase is measured and cross-checked by an independent probe. "Trace lithium" is consistent in kind (trace amounts exist), but the lithium amount is a live discrepancy: held open, not filled.
8. Model update (Capsule: what the failed parts contribute): The lithium failure is the useful part: it is the one place the stage does not close, and canon's note ("trace lithium") does not record it. The label is adjusted (F-001); the lithium problem is logged as the open edge.
9. Documented: This file. Resolves FINDINGS F-001 as proposed. Correspondence: one scale down, the neutron-proton freeze-out ratio sets Y_p ("Yp = 2(n/p)" counting argument, PDG sec. 24.2); one scale up, stellar nucleosynthesis (STAGE-007) builds on this light-element substrate.
10. Next baseline: PDG 2026 BBN review and new D/H systems. Re-review of the lithium edge 2027-09-24.

## Forcing Test

- Test A (Ground): Grounded in reproduced abundance measurements (Y_p from 7 independent analyses; D/H from 11 systems) and an independent CMB baryon density.
- Test B (Uniqueness): Stars destroy D and cannot supply the uniform Y_p ~ 0.245 floor, so stellar production is excluded as the source of primordial D and 4He. One candidate survives: formation in an early hot, dense phase at the measured baryon density.
- Test C (Direction): Forced: light elements before stars (D is destroyed, not made, by later processing).
- Test D (Falsifiability): Falsifiable (step 3) and survived for D and 4He. Lithium is an unresolved exception, not a falsification of D/He formation.
- **Outcome:** forced-fill for the formation of H, He, D in an early phase; the lithium amount is held open.

## Anti-Operation (the gap this opens)

The lithium problem: predicted primordial Li/H = (4.72 +/- 0.7)e-10 vs observed (1.6 +/- 0.3)e-10, a factor of 3.1 at 4.4 sigma (PDG 2024, sec. 24.5). Canon's "trace lithium" is true in kind but silent on the discrepancy. The gap opened: the stage's one unclosed abundance. Held open with review_after 2027-09-24 (tracked in the finding, not in this item's intake, which is adjusted for the label).

## Narrative stripped (if any)

- **Label.** "Big Bang Nucleosynthesis" names the process after an origin event. v5.4 §5 already rules the Big Bang *as an event at a place* forced-false and keeps only the phase and its observations. The observations are light-element abundances formed in an early hot phase. Proposed label: **"Primordial Light-Element Formation"** (F-001). The standard physics term BBN can be kept as a cross-reference, not as the stage name.
- "Substrate set": framework mapping; neither forced nor contradicted.
- "Per Cause and Effect: all later atoms caused at this moment": framework mapping. Read literally it overreaches: heavier elements form later in stars and mergers (STAGE-007, STAGE-008). As a Hermetic mapping it is not graded, and it does not change the grade.

```
Source: GFunnel Methodology (Omni Process) v5.1 Appendix A and v5.4 §5, §9, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Audit record adapted; not endorsed by the author.
```
