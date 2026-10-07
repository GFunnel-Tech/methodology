# Instant Delivery inside GFunnel: Build Spec

> **Status: derivation, not canon.** This spec makes the agent org map run in real time inside GFunnel. It derives from v5.1 (ACE "zero lag" first response, Communication step 5, Shepherd's Way Step 05, System Architecture steps 2, 5 and 8). The tier boundaries, latency targets and component choices are **design decisions**, not measurements.

**Goal (Owner decision):** everything runs inside GFunnel and reaches the Owner as close to instantly as possible. Where GFunnel lacks a piece, it gets built.

## 1. Principles

1. **Every action is an event.** Agents do not "report later". Each state change emits a typed event the moment it happens.
2. **One channel to the Owner (O-23).** Nothing reaches the Owner around it. This keeps one inbox, one decision log and one place to tune noise.
3. **Instant but tiered.** Canon warns against more density than the receiver can hold (Communication step 5). Instant delivery therefore means *instant routing*. Only decisions and emergencies interrupt; everything else streams to a live feed or rolls up on demand.
4. **The Owner's tap is an event too.** A decision travels back over the same bus, unblocks the board item and dispatches the team without anyone relaying it.
5. **Speed never skips steps.** Canon: *"Because the blueprint exists, builds that would take weeks take hours. Speed comes from prior thoroughness."* Every recurring deliverable gets a **standing blueprint** (Direct, Guide, Gather and Organize done in advance). Create then runs on demand, and O-03 still blocks any Create that has no blueprint.
6. **Never silent.** Every P0/P1 delivery has a fallback channel. Every failure emits `delivery.failed`.

## 2. Priority tiers

| Tier | Name | What qualifies | Delivery in GFunnel | Target (to be measured) |
| --- | --- | --- | --- | --- |
| **P0** | Interrupt | Confirmed crisis, security incident, client delivery stopped | Mobile push + in-app alert that persists until acknowledged; second channel if unanswered | ≤ 10 s event → device |
| **P1** | Push now | Human Gate (decision needed), work proposal, blocked item needing the Owner, receipt of an Owner request, Closed Won, client's first result, agent change | Mobile push + **Owner Inbox** card with one-tap approve / defer / decline | ≤ 60 s |
| **P2** | Live feed | Item state changes, completions, recaps, funnel and BEAS movement, routine numbers | Live dashboard + activity feed, no push | ≤ 5 s to appear |
| **P3** | Rollup | Summaries across events: digest, weekly, monthly, quarterly | Generated on demand ("brief me now") and on schedule | ≤ 60 s to generate |

The line between P1 and P2 is held open (V-16). O-23 tracks pushes the Owner marks as noise and proposes re-tiering. The Owner approves any change to what interrupts them.

## 3. Event envelope

Every event, from every agent, uses one envelope:

```json
{
  "event_id": "evt_01J...",
  "type": "gate.raised",
  "tier": "P1",
  "emitted_by": "SAL-08",
  "emitted_at": "2026-10-07T14:03:22.418Z",
  "item_id": "itm_...",
  "correlation_id": "the request or proposal this belongs to",
  "payload": { },
  "needs_owner": true,
  "dedupe_key": "gate:itm_...:HG-08"
}
```

- `tier` is set by the emitter as a default and may be overridden by the router's rules.
- `dedupe_key` lets the router update an existing Owner Inbox card instead of sending a second push (O-24 keeps one open proposal per signal).
- `emitted_at` and the router's delivery receipt give the end-to-end latency that TEC-09 measures.

The full event catalogue (15 types, payload fields, consumers, tier) is on the workbook's **Instant Delivery** tab.

## 4. Components: reuse or build

| Component | Job | Likely GFunnel building block | Decision |
| --- | --- | --- | --- |
| Event bus | Fan out typed events to subscribers | n8n webhooks + Lead Connector workflow triggers/webhooks | Reuse if fan-out is reliable; else a small event service |
| Notification router | Apply tiers and noise rules, pick channel, retry, fall back | Lead Connector workflows (internal notifications, mobile app push) + n8n logic | Reuse + configure |
| **Owner Inbox** | Everything waiting on the Owner; one-tap decisions from the phone | Lead Connector tasks / custom object + mobile app, or a GFunnel page | Build if one-tap actions aren't native |
| Work board | One board; item = owner team lead + Shepherd's Way step + due time + blockers | Lead Connector custom object or pipeline (stages = Shepherd's Way steps) | Reuse + configure |
| Live dashboard + feed | P2 stream | GFunnel dashboards/reporting | Reuse if near-real-time; else build |
| Digest generator | P3 on demand and scheduled | Flows AI / AI workflow over the event log | Build |
| Event log | Every event kept: recaps, audits, digests | GFunnel/Lead Connector records + an event table | Reuse or build |
| Standing blueprints | Pre-organized templates per recurring deliverable | SOP library + templates in GFunnel | Build per deliverable |
| Latency monitor | Event→device time per tier; breach alerts | n8n + logging | Build |

**Not yet verified:** the Lead Connector (GFunnel) and n8n connectors were not authorized in the session that wrote this, so none of these building blocks has been checked against the live instance. Authorize both in claude.ai connector settings and the "reuse or build" column can be settled from the real configuration.

## 5. Owner Inbox card

| Field | Content |
| --- | --- |
| Title | One line: what is being decided |
| From | Agent ID + team |
| Options | 2–4 options, the dynamic middle marked, and the recommendation labeled as a recommendation |
| Measured vs open | What is known; what is held open (never filled with assumption) |
| Falsifier | What would show this decision was wrong, and the threshold |
| Deadline | When the item blocks if undecided |
| Actions | **Approve · Defer · Decline · Ask** (Ask opens a reply to the agent) |

On tap: `gate.decided` or `proposal.decided` is emitted, O-23 logs the decision with its expected outcome (Decision-Making step 9), O-25 unblocks or creates the board item, and the team lead is dispatched immediately.

## 6. Work board

- **Stages:** Requested → 01 Direct → 02 Guide → 03 Gather → 04 Organize → 05 Create → Review → 06 Database → 07 Repetition / Done.
- **Required fields:** owner team lead, current step, due time, blockers, source (Owner request / proposal / routed), correlation ID.
- **Rules:** nothing is dispatched straight to a task agent (team lead first). O-03 blocks a move into Create without an Organize output or a standing blueprint. Every move emits `item.state_changed`.

## 7. Build order (dependency order, Fibonacci)

1. **Event envelope + event log.** Everything else consumes it.
2. **Work board** with Shepherd's Way stages, emitting events.
3. **Router + P1 Owner Inbox** with one-tap actions, plus the return path to the board.
4. **P0 interrupt** with persistent alert and fallback channel.
5. **P2 live dashboard/feed.**
6. **P3 digest generator** (on demand first, then scheduled).
7. **O-24 signal subscriptions** (BEAS, stalls, funnel, client milestones, risks, patterns).
8. **Latency monitor.** Replace targets with measured numbers in the Variable Register (V-15).
9. **Standing blueprints**, starting with the highest-volume deliverables (newsletter, email sequences, recaps, proposals).

## 8. Acceptance checks

- [ ] A test `gate.raised` reaches the Owner's phone and the Owner Inbox; the tap unblocks the board item; latency is logged.
- [ ] A P0 test that is not acknowledged escalates to the second channel.
- [ ] Two `signal.changed` events for the same signal produce one Inbox card (dedupe), not two pushes.
- [ ] An Owner request sent from the phone yields a pushed receipt and a board item with an owner team lead.
- [ ] "Brief me now" returns a digest built from the event log.
- [ ] Killing the primary push channel triggers `delivery.failed` and the fallback.
- [ ] A board move into Create without a blueprint is blocked by O-03.

## 9. Held open (not filled)

- **V-15:** actual latency per tier. The figures above are targets until TEC-09 measures them.
- **V-16:** where P1 ends and P2 begins for this Owner.
- **V-08:** which GFunnel features exist natively; this needs the connectors authorized.

---

Source: GFunnel Methodology (Omni Process) v5.1–v5.3, Cameron Garlick / GFunnel, https://github.com/GFunnel-Tech/methodology, CC BY 4.0. This spec adapts the methodology into an operating design; the adaptation is not endorsed by the author.
