# Pattern Catalogue — Recurring Mechanisms Across Cell Processes

> **Status: derivation / work-in-progress. Not canon.** Each pattern is pulled from the **measured and derived tiers** of a run, never from the framework-mapping tier alone. A pattern seen in one process is a single instance. It becomes a recurring pattern only when another run shows it independently. Nothing here is promoted to a law.

## How to add

1. Finish a run. List its patterns at the end of the run file.
2. If a pattern already exists here, add the run to its **Instances** column. Do not add a duplicate.
3. If it is new, add a row with the next `P-##` id.
4. If a later run **contradicts** a pattern, record it under **Counter-instances**. Do not delete the row.

## Catalogue

| ID | Pattern | Instances | Counter-instances | Candidate correspondence (unchecked) |
| --- | --- | --- | --- | --- |
| P-01 | **Gated commitment.** Energy is spent only after the input is fully detected. | [Run 01](membrane/run-01-na-k-pump.md) (Na+/K+ pump) | — | Held open until another run tests it |
| P-02 | **Alternating access.** The gate is never open to both sides at once; the cargo is held during the switch. | Run 01 | — | Held open |
| P-03 | **Fixed-rate conversion.** One energy store is converted to another at a fixed integer ratio. | Run 01 | — | Held open |
| P-04 | **Ratio vs. ceiling trade-off.** Units moved per unit of fuel trade against the maximum gradient that can be held. | Run 01 (measured variant in brine shrimp) | — | Held open |
| P-05 | **Self-loading output.** The output changes the cost of the next cycle. | Run 01 | — | Held open |
| P-06 | **Cleaning sets the variation rate.** The same error-correction pipeline that keeps the record clean sets how much variation reaches selection. | [Information](information/README.md) B1 → F1 (N1–N3) | — | Canon's "optimal mutation rate" (IG-04) — held open |
| P-07 | **Threshold memory.** A weak or brief input does not flip the switch; a strong one flips it and the new state outlasts the input. | Information A1 / D2 (N7) | — | Reality Filter item 8, *weak observations cannot force change* — candidate fit |
| P-08 | **Recycle the material, erase the information.** Degradation returns building blocks while the item's state is lost. | Information C1–C2 (N9; recycling detail *source pending*) | — | Matches the audit's restatement of Layer I.G (b): the discriminating structure is kept, the item is not — F-067, IG-01 |

For P-01 – P-05 the correspondence column stays empty until Deep-Lens step K (correspondence check) runs, which comes after the step-E blocker (see [run 01](membrane/run-01-na-k-pump.md)). P-06 – P-08 carry candidates from the information area's correspondence check; they are unchecked.
