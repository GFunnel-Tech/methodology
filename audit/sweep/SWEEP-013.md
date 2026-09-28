---
id: SWEEP-013
canon_ref: "v5.1 Layer I.C Domain 9 (Biological Process), 'Algorithm' row: 'DETECT: Internal deviation or external threat. PROCESS: Cellular response — gene expression, protein synthesis, metabolic shift, immune activation. RESPOND: Adapted state, corrected equilibrium.'"
canon_label: "Domain 9 — Biological Process (Algorithm row)"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: live-hypothesis
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Domain 9, Algorithm row: "DETECT: Internal deviation or external threat. PROCESS: Cellular response — gene expression, protein synthesis, metabolic shift, immune activation. RESPOND: Adapted state, corrected equilibrium."

Domain 9, Homeostasis row: "The organism continuously monitors deviation, processes the signal through cascading regulatory pathways, and responds to correct."

**Split (RUNBOOK rule 4).** *Factual core graded here:* a damage-induced bacterial repair response consists of a detection event, a distinct processing/derepression step, and a repair output. *Framework mapping (not graded):* "Homeostasis as Garlick Equilibrium"; "Equilibrium is dynamic correction at every moment."

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| SOS inducing signal: LexA repressor cleavage promoted by RecA bound to single-stranded DNA; after UV the major induction pathway requires an active replication fork; cleavage detectable within minutes and in the absence of protein synthesis | qualitative mechanism plus minutes-scale kinetics | as published | measured-single | https://doi.org/10.1016/0022-2836(90)90306-7 | 2026-09-28 |
| Single-cell recA promoter activity after UV: discrete activity peaks, up to three within the experiment; number of peaks increases with dose while peak amplitude saturates | doses 10, 20 and 50 J/m2; peak-time standard deviation / mean under 10 percent | as published | measured-single | https://doi.org/10.1371/journal.pbio.0030238 | 2026-09-28 |
| Nucleotide excision repair product in E. coli, directly sequenced | 13-mer oligo containing the cyclobutane pyrimidine dimer; UvrD unwinds it from the duplex | as published | measured-single | https://doi.org/10.1073/pnas.1700230114 | 2026-09-28 |
| Transcription-coupled repair: deleting mfd shifts the transcribed-strand / non-transcribed-strand repair ratio down by a factor of about 2 for the most highly transcribed genes | factor about 2 | as published | measured-single | https://doi.org/10.1073/pnas.1700230114 | 2026-09-28 |
| Induction threshold as a single number (a dose or a ssDNA length at which SOS switches on) | not stated by either fetched primary source; the measured response is graded in peak *count* rather than switching at one threshold | n/a | held-open | https://doi.org/10.1371/journal.pbio.0030238 | 2026-09-28 |

## Scientific Inquiry run

1. Question (precise): Does Domain 9's algorithm row hold the measured bacterial DNA-damage response (SOS, RecA, NER), and does the three-step parse sit on measured boundaries — including a measured induction threshold?
2. What an answer must look like: named molecular events for each of the three operations, each separable by mutation or by measurement, plus whatever threshold the measurements actually show.
3. Falsifiability condition: the mapping fails if detection and response cannot be separated experimentally, or if the response is continuous in damage with no processing step.
4. Variables: measurable / bounded / held open: Measurable: LexA cleavage kinetics, peak count and timing, excised oligo length, Mfd's contribution. Bounded: the response is bounded above — amplitude saturates with dose. Held open: a single numeric induction threshold; the fetched sources report dose-dependent peak *number*, not one switching point.
5. Test designed: fetch the primary SOS signal paper, a single-cell SOS dynamics paper, and a genome-wide excision-repair mapping paper; check whether the three operations correspond to separable measured events.
6. Data (unfiltered): table above. The three events are separable: RecA-ssDNA formation (detection), LexA cleavage and derepression (processing), uvrABC/umuDC action (response). LexA cleavage occurs without protein synthesis, so processing is separable from the response it triggers. The response is pulsatile, not monotone.
7. Variable Principle applied: the mapping is supported but the framework's implied *analogue* correction ("dynamic correction at every moment") is not what is measured: single cells fire discrete pulses whose count, not amplitude, encodes dose. That is a measured refinement canon does not carry, and no single threshold number should be asserted — held open.
8. Model update (Capsule: what the failed parts contribute): "continuous monitoring" survives; "continuous correcting" does not. Canon's homeostasis row should carry the pulsatile case.
9. Documented: this file. Correspondence: one scale down, the RecA filament's cooperative ssDNA binding; one scale up, the mammalian p53 pulse trains the same paper compares itself to (not fetched here; held open).
10. Next baseline: a PRED test on dose-to-peak-count encoding (see SWEEP report, candidate 6).

## Forcing Test

- Test A (Ground): Grounded. Each of the three operations names a measured, separately mutable molecular event.
- Test B (Uniqueness): Not unique — the same pathway is routinely described in four or five steps (damage, signal, derepression, repair, shutoff), and shutoff (LexA reaccumulation) has no home in the three-operation parse.
- Test C (Direction): Measurement supports the direction: detection precedes derepression precedes repair, established by the protein-synthesis-independent cleavage result.
- Test D (Falsifiability): Falsifier named (inseparability of detection and response); it did not fire.
- **Outcome:** `live-hypothesis`. The DPR mapping **fits** the measured mechanism here — this is the strongest fit found in this sweep — with the falsifier that a measured pathway step (response shutoff / LexA reaccumulation) falls outside the three operations.

## Anti-Operation (the gap this opens)

The loop has no operation for *terminating* a response. Measured SOS shutoff is an explicit, timed step (LexA reaccumulation, UmuD cleavage-dependent pause). Canon's RESPOND is defined as the output becoming the next input, which does not distinguish "response continues" from "response is switched off". Second gap: no canonical quantity predicts why dose is encoded in pulse count rather than amplitude.

## Narrative stripped (if any)

Removed: "Equilibrium is dynamic correction at every moment" as a description of this system. Measurement shows intermittent, precisely timed pulses, not moment-by-moment correction. Reality contradicts the *continuity*, not the loop.

```
Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel,
https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; grading not endorsed by the author.
```
