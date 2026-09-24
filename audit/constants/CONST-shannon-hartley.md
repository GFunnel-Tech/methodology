---
id: CONST-shannon-hartley
canon_ref: "v5.1 Appendix D, Information & Computation Laws, row 'Shannon-Hartley Theorem' (versions/v5.1/GFunnel-Methodology-v5.1.md line 2057)"
canon_label: "Shannon-Hartley Theorem"
diff_state: accounted
exclusion_diagnosis: n/a
claim_outcome: forced-fill
intake_result: integrated
review_after: null
container: null
ledger_row: null
---

## Canon says

v5.1 Appendix D (Fundamental Constants & Laws Registry), *Information & Computation Laws*, line 2057:

> **Law:** Shannon-Hartley Theorem  
> **Statement:** C = B · log₂(1 + S/N)  
> **Framework Role:** Maximum information transmission rate is bounded by bandwidth and signal-to-noise ratio. Per Vibration: the physics of communication channels.

**Split (RUNBOOK rule 4).** *Factual core graded here:* channel capacity C = B · log₂(1 + S/N).

*Framework mapping (not graded; see Narrative stripped):* 'Per Vibration: the physics of communication channels.'

## Reality shows

| Quantity | Value | Uncertainty | Grade | Source | Retrieved |
| --- | --- | --- | --- | --- | --- |
| Paper deriving capacity of a band-limited channel with noise (bibliographic record) | Shannon, 'Communication in the Presence of Noise', Proceedings of the IRE, 1949-01 | n/a | derived | https://api.crossref.org/works/10.1109/JRPROC.1949.232969 | 2026-09-24 |

A proved theorem is not a measurement. Rows graded `derived` record the published statement the canon wording was checked against; no experiment can raise or lower their grade. Paper text not retrieved; canon's formula matches the standard statement. The theorem holds for a band-limited channel with additive white Gaussian noise and average-power constraint; canon omits these conditions.

## Scientific Inquiry run

1. Question (precise): Is C = B·log₂(1+S/N) the correct capacity statement, and under what conditions?
2. What an answer must look like: Formula match plus the stated conditions.
3. Falsifiability condition: Canon's formula differs, or canon applies it outside its conditions.
4. Variables: measurable / bounded / held open: Measurable: B, S, N for a given channel. Bounded: n/a. Held open: none.
5. Test designed: Compare with Shannon (1949).
6. Data (unfiltered): Formula matches. Conditions (AWGN, band-limited, power-constrained) are omitted in canon.
7. Variable Principle applied: No variable filled; the omission is recorded rather than assumed away.
8. Model update (Capsule: what the failed parts contribute): Add the AWGN condition when the row is re-issued.
9. Documented: This file.
10. Next baseline: Integrated with the condition noted.

## Forcing Test

- Test A (Ground): Proved theorem.
- Test B (Uniqueness): Unique for the AWGN channel.
- Test C (Direction): Correct direction.
- Test D (Falsifiability): Transcription check passes; conditions missing.
- **Outcome:** `forced-fill` (for AWGN channels).

## Anti-Operation (the gap this opens)

Canon's statement is silent on non-Gaussian and fading channels, where capacity takes other forms. Which channel model a framework application assumes is held open.

## Narrative stripped

Removed: 'Per Vibration'. The theorem is about bandwidth and noise power; it does not require or imply the Hermetic Principle of Vibration. Reality does not force the mapping.

---

*Audit record (derivation). Quotes canon from:* Source: GFunnel Methodology (Omni Process) v5.1, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. Quoted for audit; the grading and commentary are not endorsed by the author.
