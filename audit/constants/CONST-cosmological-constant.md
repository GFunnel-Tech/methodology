---
id: CONST-cosmological-constant
canon_ref: v5.1 Appendix D, Physical Constants
canon_label: "Λ — Cosmological Constant"
diff_state: conflict
exclusion_diagnosis: reached-conflicting
claim_outcome: forced-fill
intake_result: open
review_after: 2027-09-24
container: null
ledger_row: null
---

## Canon says
v5.1 Appendix D, *Physical Constants* table. **Value:** ~1.1×10⁻µ² m⁻² (as written). **Framework Role:** "Dark energy density. Drives accelerating cosmic expansion. Per Layer I.E Resolution Three: the unidentified mechanism by which energy continues at cosmological scale. The deepest open variable in physics."

**The value as transcribed is not a number:** `~1.1×10⁻µ² m⁻²`. The superscript `µ` is not a digit.

## Reality shows
| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Hubble constant H₀ (CMB, base-ΛCDM inferred) | 67.4 km s⁻¹ Mpc⁻¹ | 0.5 | derived | https://arxiv.org/abs/1807.06209 | 2026-09-24 |
| matter density parameter Ω_m | 0.315 | 0.007 | derived | https://arxiv.org/abs/1807.06209 | 2026-09-24 |
| Λ = 3(1−Ω_m)H₀²/c² (computed, flat base-ΛCDM) | 1.091 × 10⁻⁵² m⁻² | 0.020 × 10⁻⁵² | derived | https://arxiv.org/abs/1807.06209 | 2026-09-24 |
| deceleration parameter q₀ (SNe Ia) | −0.51 | 0.024 | measured-single | https://arxiv.org/abs/2112.04510 | 2026-09-24 |

## Scientific Inquiry run
1. Question (precise): Does canon's stated value of Λ match the value derived from primary cosmological measurements?
2. What an answer must look like: A primary-source value with uncertainty, compared with canon at canon's own stated precision; a separate statement of whether the role text is measured, modeled, or interpretive.
3. Falsifiability condition: Derived Λ not within ~10% of 1.1 × 10⁻⁵² m⁻² (the only reading of canon's text that is a number).
4. Variables: measurable / bounded / held open: Measurable: H₀ and Ω_m (model-inferred), q₀ < 0 (acceleration). Derived: Λ. Held open: what Λ is (canon: 'the deepest open variable' — kept open).
5. Test designed: Rounding-consistency check in `audit/constants/check_physical_constants.py`: canon passes if |canon − measured| ≤ half a unit of canon's last digit + measured 1σ.
6. Data (unfiltered): As tabled; computed by `audit/constants/check_physical_constants.py`: Λ = 1.091(20) × 10⁻⁵² m⁻².
7. Variable Principle applied: The value is graded by measurement. The role text is graded separately (see Narrative stripped); no open variable is filled.
8. Model update (Capsule: what the failed parts contribute): The failed comparison locates a defect in the explicit log, not in reality. Interpretive clauses that measurement does not support are retained in the lineage (v5.1 text is unchanged) and proposed for status tags in v5.5.
9. Documented: this file; `audit/constants/check_physical_constants.py`.
10. Next baseline: Re-run on the next CODATA adjustment / cosmology data release (Phase 9).

## Forcing Test
- Test A (Ground): Within-system — a measured quantity compared with a written value.
- Test B (Uniqueness): The number canon intends is forced by the data if the exponent is −52. As written ('10⁻µ²') the text is not a number, so the canonical value cannot be compared at all.
- Test C (Direction): The comparison runs from measurement to text: reality is the authority (substrate item 1).
- Test D (Falsifiability): Falsifier stated in step 3; it fired or could not be evaluated as written — see Reality shows.
- **Outcome:** forced-fill (value); see Anti-Operation for the role text

## Anti-Operation (the gap this opens)
The canonical text is defective at exactly the value. Only the author's original can say whether '⁻µ²' is a transcription error of '⁻⁵²'. Open edge: a transcription-fix issue. Separately, the vacuum-energy discrepancy (v5.4 §11) stays open.

## Narrative stripped (if any)
"Drives accelerating cosmic expansion" — the measurement is that expansion accelerates (q₀ < 0); 'drives' assigns a cause that ΛCDM models but no measurement isolates. "The unidentified mechanism by which energy continues" — framework mapping, not forced. Both stripped.
