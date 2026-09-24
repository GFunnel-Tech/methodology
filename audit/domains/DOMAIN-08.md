---
id: DOMAIN-08
canon_ref: v5.1 Layer I.C Domain 8 (Universal Process Registry); v5.1 "Domain 8 — Chemical / Physical Process Algorithm"
canon_label: "Chemical Process"
diff_state: conflict
exclusion_diagnosis: reached-conflicting
claim_outcome: forced-no
intake_result: adjusted
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Layer I.C, Domain 8:

- *Algorithm:* "DETECT: Reactants contact / activation energy threshold crossed. PROCESS: Bond breaking and forming, energy exchange, electron redistribution. RESPOND: Products + energy change."
- *Catalysis:* "A catalyst accelerates a reaction without being consumed."
- *Le Chatelier's Principle:* "A system at equilibrium, when disturbed, shifts to oppose the disturbance and re-establish equilibrium. This is the Garlick Equilibrium at the molecular level. Structurally identical."
- *Entropy in Chemistry:* "Spontaneous reactions move toward higher entropy. Biological systems locally reverse entropy by consuming energy."
- *Yin/Yang:* "Endothermic (Yin) vs. exothermic (Yang)."
- Domain 8 Algorithm step 5: "Apply Conservation Laws. Energy, momentum, charge, and information must balance." Step 6: "Spontaneous reactions move toward higher entropy. Local entropy reversal requires energy throughput."

**Split.** *Factual core:* reactions proceed when reactants meet and an activation barrier is crossed; bonds break and form; catalysts are not consumed; Le Chatelier's principle; spontaneous reactions move toward higher entropy; energy, momentum, charge, and information are conserved. *Framework mapping:* "Garlick Equilibrium ... Structurally identical", Yin/Yang assignment, GFunnel-as-catalyst.

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Standard molar entropy, H2O (liquid), 298.15 K, 1 bar | 69.95 J/(mol·K) | ± 0.03 | measured-reproduced | https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Units=SI&Mask=2 (CODATA key value, Cox, Wagman et al. 1984) | 2026-09-24 |
| Standard molar entropy, H2 (gas), 1 bar | 130.680 J/(mol·K) | ± 0.003 | measured-reproduced | https://webbook.nist.gov/cgi/cbook.cgi?ID=C1333740&Mask=1 (CODATA key value) | 2026-09-24 |
| Standard molar entropy, O2 (gas), 1 bar | 205.152 J/(mol·K) | ± 0.005 | measured-reproduced | https://webbook.nist.gov/cgi/cbook.cgi?ID=C7782447&Mask=1 (CODATA key value) | 2026-09-24 |
| Standard enthalpy of formation, H2O (liquid) | −285.830 kJ/mol | ± 0.040 | measured-reproduced | https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Units=SI&Mask=2 (CODATA key value) | 2026-09-24 |
| Reaction entropy of the system, H2(g) + ½O2(g) → H2O(l), 298.15 K: ΔS_sys = S(H2O,l) − S(H2) − ½S(O2) | −163.306 J/(mol·K) | ± 0.030 (quadrature) | derived | computed from the four rows above (Python stdlib) | 2026-09-24 |
| Gibbs energy of the same reaction: ΔG = ΔH − TΔS_sys | −237.14 kJ/mol | ± 0.041 (quadrature) | derived | computed from the rows above | 2026-09-24 |
| Entropy change of surroundings, −ΔH/T | +958.68 J/(mol·K) | ± 0.13 | derived | computed from the rows above | 2026-09-24 |
| Total entropy change, ΔS_sys + ΔS_surr | +795.37 J/(mol·K) | ± 0.14 | derived | computed from the rows above | 2026-09-24 |
| IUPAC definitions of catalyst and Gibbs energy; statement of Le Chatelier's principle | not verified: goldbook.iupac.org returned a bot-challenge page to this run | none | held-open | https://goldbook.iupac.org/terms/view/C00876 (blocked) | 2026-09-24 |
| "Information" as a conserved quantity in chemical reactions | not a standard conservation law of chemistry; no primary source fetched stating it | none | held-open | canon names no source | 2026-09-24 |

Derivation (Python standard library, values as above):
```
S_H2O_l = 69.95; S_H2 = 130.680; S_O2 = 205.152   # J/(mol K)
dH = -285.830                                      # kJ/mol
T = 298.15                                         # K
dS_sys  = S_H2O_l - S_H2 - 0.5*S_O2                # -163.306 J/(mol K)
dG      = dH - T*dS_sys/1000                       # -237.140 kJ/mol
dS_surr = -dH*1000/T                               # +958.679 J/(mol K)
dS_tot  = dS_sys + dS_surr                         # +795.373 J/(mol K)
```

## Scientific Inquiry run
1. Question (precise): Is "Spontaneous reactions move toward higher entropy" correct as written, are the other chemical statements consistent with measurement, and is the DETECT → PROCESS → RESPOND mapping forced?
2. What an answer must look like: a measured spontaneous reaction whose system entropy change can be computed from reference data, with ΔG and total entropy; a named observation that would count as non-mapping.
3. Falsifiability condition: Canon's sentence (read as the entropy of the reacting system) is falsified by any spontaneous reaction with ΔS_sys < 0.
4. Variables: measurable / bounded / held open: measurable: standard entropies and enthalpies (CODATA). Derived: ΔS_sys, ΔG, ΔS_surr, ΔS_total. Held open: IUPAC wording for catalyst / Le Chatelier (source blocked); "information" conservation.
5. Test designed: Take the formation of liquid water from H2 and O2 at 298.15 K, 1 bar; fetch CODATA key values from the NIST WebBook; compute ΔS_sys, ΔG, ΔS_surr, ΔS_total.
6. Data (unfiltered): ΔS_sys = −163.306 J/(mol·K); ΔG = −237.14 kJ/mol (spontaneous); ΔS_surr = +958.68 J/(mol·K); ΔS_total = +795.37 J/(mol·K).
7. Variable Principle applied: The reaction is spontaneous (ΔG < 0) while the system's entropy *decreases*. Canon's sentence is false for the system and true only for the total (system + surroundings). The correct statement at constant temperature and pressure: a process is spontaneous when ΔG < 0, equivalently when total entropy increases. The second sentence ("Biological systems locally reverse entropy by consuming energy") is consistent with the same accounting and does not need the false first sentence. Activation energy, bond rearrangement, catalysis, Le Chatelier: standard textbook content, not contradicted; primary IUPAC wording held open (blocked). "Information must balance" is not a chemistry conservation law and is held open.
8. Model update (Capsule: what the failed parts contribute): Adjustment (proposed, canon not edited): replace "Spontaneous reactions move toward higher entropy" (Registry and Algorithm step 6) with "At constant temperature and pressure, reactions are spontaneous when ΔG = ΔH − TΔS < 0; the total entropy of system plus surroundings increases, although the system's own entropy may fall (e.g. H2 + ½O2 → H2O(l): ΔS_sys = −163.3 J/(mol·K), ΔG = −237.1 kJ/mol)." Remove "information" from step 5 or hold it open. Reason: the contradicting data are CODATA key values (measured-reproduced).
9. Documented: This file.
10. Next baseline: Entropy sentence: adjusted wording. Other chemical content: accounted in substance, primary IUPAC wording pending. "Information" conservation: open.

## Forcing Test
- Test A (Ground): CODATA reference values; reproduced measurements.
- Test B (Uniqueness): With these values, ΔS_sys has one value (−163.3 J/(mol·K)); no reading of "the reacting system's entropy increases" survives.
- Test C (Direction): Spontaneous (ΔG < 0), system entropy down, total entropy up. The direction canon states holds only for the total.
- Test D (Falsifiability): The sentence was falsifiable and one counterexample falsifies it as a general rule.
- **Outcome:** forced-no for "Spontaneous reactions move toward higher entropy" read as system entropy; the correct form (ΔG < 0 / total entropy increases) is forced by the data. Intake `adjusted` (proposed wording in step 8). Mapping: stipulation.

## Anti-Operation (the gap this opens)

- Spontaneity depends on ΔH and ΔS together (ΔG = ΔH − TΔS). The Yin/Yang assignment (endothermic = Yin, exothermic = Yang) uses ΔH alone and does not say what it predicts about spontaneity or equilibrium. Open.
- "Information must balance" (Algorithm step 5): what conservation law is meant? Open.
- "Structurally identical" (Le Chatelier = Garlick Equilibrium) needs a shared quantitative form to be tested; canon gives none.

## Narrative stripped (if any)

- **"This is the Garlick Equilibrium at the molecular level. Structurally identical."**: a framework analogy. Reality neither forces nor contradicts it; no shared equation is given.
- **"GFunnel as catalyst, not reactant"**: business analogy.
- **Mapping verdict: stipulation.** A reaction has no detector: "reactants contact / activation energy threshold crossed" is relabeled as DETECT. Molecules do not detect; they collide. The mapping fits by relabeling an event as a detection. Per canon's own rule a domain that resists should become a named variable; canon names none here. No observation is named that would count as failure to map.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; audit commentary is not endorsed by the author.
```
