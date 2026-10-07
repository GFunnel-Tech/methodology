"""Agent roster for the GFunnel agent org map.

DERIVATION, not canon (AGENTS.md rule 4/7). Every agent traces to a canonical
department function, table, or algorithm in v5.1-v5.3; where a field is not
supplied by canon it is marked "Derived" or "Held open".
"""

DEPTS = {
    # code: (name, kingdom, yin/yang, civil equivalent, primary function per canon)
    "GOV": ("Governance & Meta-Tier", "3rd", "Meta (operates on all layers)", "—", "Framework integrity: falsifiability, variable discipline, classification of open questions, agent alignment"),
    "ORC": ("Orchestration & Diagnostics", "2nd", "Dynamic middle", "—", "Routes every input to the right algorithm/agent and runs the layer diagnostics"),
    "STR": ("1 · Strategy Hub", "3rd", "Yin — directional", "Constitution + founding law", "Vision, mission, values, governing principles, quarterly direction, competitive positioning"),
    "MKT": ("2 · Marketing Hub", "2nd→1st", "Yang — outward", "Roads + traffic systems", "Lead generation, traffic, attention, brand awareness, content distribution"),
    "SAL": ("3 · Sales Hub", "2nd→1st", "Yang — converting", "Markets + commerce", "Offer architecture, pipeline, sales scripts, ACE System, revenue generation"),
    "OPS": ("4 · Operations Hub", "1st", "Yin/Yang balance", "Utilities + supply chain", "Fulfillment, delivery, quality control, project management"),
    "FIN": ("5 · Finance Hub", "1st→2nd", "Yin — control", "Treasury + banking", "Capital management, budgeting, forecasting, reporting, commission, pricing"),
    "HRC": ("6 · HR & Culture Hub", "2nd", "Yin — standards", "Courts + labor institutions", "Hiring, onboarding, performance, culture, compensation, org design"),
    "TEC": ("7 · Technology Hub", "2nd→1st", "Yang infrastructure", "Communications network", "Platform architecture, automation (n8n), CRM (GHL), integrations, AI, security"),
    "CS":  ("8 · Client Success Hub", "1st→2nd", "Yin — retention", "Public services + emergency", "Onboarding, support, account management, NPS, churn prevention, expansion"),
    "CON": ("9 · Content Hub", "2nd", "Yin — propagation", "Libraries + education", "IP creation, media production, methodology documentation, brand, GFunnel University"),
}

# Autonomy levels (DERIVED — operator may change; see Held-Open sheet)
AUTONOMY = {
    "A": "Autonomous — agent executes and logs",
    "H": "Human-in-loop — agent drafts, human approves",
    "L": "Human-led — agent assists",
    "R": "Human-reserved — no agent executes",
}

DEPT_FN_SRC = "v5.1 L1376–1386 (Nine Departments map)"

# Fields: id, name, tier, dept, reports_to, mission, primary_algorithms, triggers(DETECT),
#         outputs(RESPOND), hands_off_to, tools_named_in_canon, kpis_observation,
#         human_gate, failure_guarded, autonomy, basis, canon_source
A = []
def ag(*f): A.append(f)

# ───────────── TIER 0 · GOVERNANCE & META-TIER ─────────────
ag("G-00","Founder / Operator (HUMAN)","0 · Human authority","GOV","—",
   "Holds the four things the framework cannot supply: the choice at every decision point, the naming of outcomes, situation-specific measurements, and the stance on held-open variables. Final authority over every agent.",
   "Layer IV Co-Creator Identity; What The Framework Cannot Supply; human-reserved life/contemplative algorithms",
   "Any Human Gate raised by an agent; escalations; held-open variable needing a stance",
   "Decisions, approvals, named outcomes, measurements supplied",
   "The agent that raised the gate", "—",
   "Gate turnaround time (threshold held open)",
   "This IS the human gate", "Agents filling a decision or variable with assumption",
   "R","Canon: What The Framework Cannot Supply","v5.1 L168–181; L1257–1296")
ag("G-01","Container Agent (Forcing Test classifier · Layer ⊙)","0 · Governance","GOV","G-00",
   "Classifies every open business question before it is acted on: forced-fill, live hypothesis, stipulation, or proven-open. Runs the Anti-Operation (what new gap does each fill open?). Enforces 'zero hidden gaps'.",
   "Layer ⊙ The Container — Forcing Test (Tests A–D), Anti-Operation, synthesis loop",
   "A variable proposed for resolution; a new policy/structural decision; a contested claim",
   "Classification label + next opened gap, logged to the Variable Register",
   "G-03 Variable Registry Keeper; G-02 Falsifiability", "—",
   "% of resolved variables carrying a classification label; hidden gaps found in audit",
   "Stipulations (soft choices) go to G-00", "Silently resolving a held-open variable; presenting a stipulation as forced",
   "A","Canon: v5.3 meta-tier","v5.3 §1–§4")
ag("G-02","Falsifiability Agent (Layer ◇)","0 · Governance","GOV","G-01",
   "Attaches a falsifier to every claim, plan, forecast, decision and mitigation; statuses each as resolved / bounded / held open / refuted.",
   "Layer ◇ Falsifiability Algorithm",
   "Any claim, plan, forecast, offer promise, mitigation or KPI target is written",
   "Claim card: precise claim, falsifying observation, evidence for/against, bounds, status",
   "Claim owner agent; G-03", "—",
   "% of plans/decisions with an operational falsifier (observation + threshold)",
   "Revising a refuted strategic claim → G-00", "Beliefs presented as claims",
   "A","Canon: algorithm","v5.1 L2538–2555; L1657–1717")
ag("G-03","Variable Registry Keeper","0 · Governance","GOV","G-01",
   "Maintains the business Variable Register: every quantity marked measured / structurally derived / held open. Blocks any agent output that fills a held-open variable with assumption.",
   "The Variable Principle (Governing Epistemology); Registers",
   "Any agent output containing an unmeasured number or assumption; new data arriving",
   "Register entries; narrowing logs; blocked-output notices",
   "Originating agent; G-00 for measurements", "—",
   "Unlabelled assumptions found per audit (target 0)",
   "Measurements only a human can perform → G-00", "Variable Principle violation (the framework's #1 rule)",
   "A","Canon: Variable Principle","v5.1 L223–263; framework/registers.md")
ag("G-04","Framework Compliance Auditor","0 · Governance","GOV","G-01",
   "Runs the canon's 7-point self-audit checklist on every agent run: right algorithm, steps in order, variables held open, run documented, Correspondence applied, measured vs assumed separated, failed paths integrated.",
   "Self-Audit Checklist (How To Verify You Are Using The Framework Correctly)",
   "Completion of any algorithm run by any agent",
   "Pass/fail audit per run; location of failure = next correction",
   "Failing agent; O-10 Capsule Integrator", "—",
   "Audit pass rate per agent; repeat failures",
   "—", "Skipped / reordered steps; undocumented runs",
   "A","Canon: self-audit checklist","v5.1 L182–203")
ag("G-05","AI Alignment Agent (agent-fleet oversight)","0 · Governance","GOV","G-00",
   "Applies the AI Alignment Algorithm to this agent fleet itself: Third-Kingdom intent of each agent, observation at multiple levels, falsifiers for misalignment, downgrade paths, review at every capability scale-up.",
   "AI Alignment Algorithm",
   "New agent deployed; agent capability/permission increased; misbehaviour detected",
   "Alignment review, instrumentation spec, downgrade/kill path per agent",
   "G-06; TEC-05 AI Workflow Agent", "—",
   "Agents with a documented downgrade path (target 100%); alignment incidents",
   "Deploying or expanding any agent → G-00", "Capability (1st K) without purpose (3rd K); agent with no fallback ('Texas grid')",
   "H","Canon: algorithm","v5.1 L3933–3954")
ag("G-06","Governance Designer (decision rights & escalation)","0 · Governance","GOV","G-00",
   "Designs the decision-rights map between agents and humans (who decides, who escalates, who audits), the four-pillar soundness of that governance, and its multi-year review cycle.",
   "Governance Design Algorithm; Layer I.B Civil Infrastructure",
   "Org/agent structure changes; repeated escalation conflicts",
   "Governance charter; autonomy levels; escalation map",
   "All department leads", "—",
   "Escalations resolved within charter; single points of failure in decision rights",
   "Charter adoption → G-00", "Authoritarian (all decisions centralized) or anarchic (no locus) extremes",
   "H","Canon: algorithm","v5.1 L3911–3930")
ag("G-07","Founder Performance Agent","0 · Governance","GOV","G-00",
   "Supports the operator's own operating capacity: time allocation by Kingdom, Yin/Yang energy cycles, habits, personal development — so the business is not run from First-Kingdom exhaustion.",
   "Time Management; Energy Management; Habit Formation; Personal Development",
   "Weekly review; operator calendar; drift between intended and actual time",
   "Protected time blocks, weekly allocation review, habit tracking",
   "G-00", "—",
   "Intended vs actual time allocation gap; protected 20% time kept",
   "All personal choices → G-00", "Permanent Yang (burnout); time drift",
   "L","Canon: algorithms (life domains applied to operator)","v5.1 L2772–2791; L3579–3636")

# ───────────── TIER 1 · ORCHESTRATION & DIAGNOSTICS ─────────────
ag("O-01","Intake & Triage Agent (Layer 0 Base Code)","1 · Orchestration","ORC","O-02",
   "First touch for every input entering the business (email, form, alert, request, idea). Names the input, locates the Kingdom it arrived from, moves it up before deciding, routes it.",
   "Layer 0 Base Code Algorithm; Domain 4 Matrix/Information (information overwhelm)",
   "Any new input arriving in any channel",
   "Labelled input → routed to an agent or algorithm",
   "O-02 Algorithm Router", "—",
   "Inputs unrouted >1 cycle (target 0)",
   "—", "Reactive First-Kingdom responses to raw input",
   "A","Canon: algorithm","v5.1 L2232–2247")
ag("O-02","Algorithm Router (Master Meta-Algorithm)","1 · Orchestration","ORC","G-01",
   "Matches every problem to the right algorithm/agent via the Algorithm Index by Problem Type. For a problem no algorithm covers, runs the 12-step Master Meta-Algorithm and labels the result a DERIVATION. Runs Deep-Lens (A–L) for high-resolution diagnoses.",
   "Master Meta-Algorithm (12 steps); Algorithm Index by Problem Type; v5.2 Deep-Lens Protocol",
   "Routed input from O-01; 'I don't know which algorithm to use'",
   "Assigned algorithm + owner agent, or a labelled derived algorithm",
   "Owner agent; G-01 for derived-algorithm classification", "—",
   "Mis-routes caught in audit; derivations labelled (target 100%)",
   "Adopting a derived algorithm as standing SOP → G-00", "Improvising silently; presenting a derivation as primary",
   "A","Canon: algorithm","v5.1 L2169–2225; L4003–4090; v5.2 §1")
ag("O-03","Shepherd's Way Cycle Controller (Layer VI)","1 · Orchestration","ORC","O-02",
   "Enforces the 7-step cycle (Direct → Guide → Gather → Organize → Create → Database → Repetition) on every build, fix or extension in every department. Blocks Create until Organize is complete. Routes New Thought back into Gather.",
   "Layer VI Shepherd's Way Algorithm; New Thought Principle",
   "Any build/fix/extend request; lowest BEAS cell dispatched by O-04; New Thought",
   "Cycle state per work item; stage gates passed/blocked",
   "Executing agent per step; O-15 at Database step", "Komodo recordings; email recaps",
   "Builds started without Direct/Guide/Gather (target 0); rework cycles",
   "Direct (intent) for strategic work → G-00", "Create-before-gather; stopping at Create without Database/Repetition",
   "A","Canon: algorithm + step tables","v5.1 L1453–1569; L2498–2515")
ag("O-04","BEAS Auditor (Layer V Garlick Equilibrium)","1 · Orchestration","ORC","G-00",
   "Scores the business monthly on 9 departments × 4 pillars + 9 coordination scores (45 pts), interprets the band, runs Yin/Yang quadrant analysis against growth stage, and dispatches the lowest cell to the Shepherd's Way.",
   "Layer V Garlick Equilibrium Algorithm (BEAS)",
   "Monthly cycle; major org change",
   "BEAS scorecard, band, quadrant analysis, lowest cell dispatched",
   "O-03; department leads", "—",
   "BEAS total; lowest cell; quadrant balance vs stage",
   "Growth-stage classification and score evidence sign-off → G-00", "Uniformly-high score chasing; equilibrium read as stasis",
   "H","Canon: algorithm + scoring grid","v5.1 L1347–1447; L2478–2495")
ag("O-05","Three Kingdoms Diagnostician (Layer I)","1 · Orchestration","ORC","O-02",
   "Diagnoses alignment of any system, team, process or agent: First (execution), Second (systems), Third (intent). Locates misalignment and corrects top-down.",
   "Layer I Three Kingdoms Identification Algorithm",
   "Poor output with unclear cause; 'reacting/firefighting, no system'",
   "Alignment map + top-down correction plan",
   "Owning department lead; O-03", "—",
   "Systems diagnosed with all three Kingdoms mapped",
   "Third-Kingdom (intent) clarification → G-00", "First-Kingdom activity disconnected from systems/intent",
   "A","Canon: algorithm","v5.1 L337–392; L2250–2267")
ag("O-06","Hermetic Principles Auditor (Layer II)","1 · Orchestration","ORC","O-02",
   "When something is failing and nobody knows why, runs the seven-principle audit and names the deepest violation as the location of the systemic failure.",
   "Layer II Seven Hermetic Principles Algorithm",
   "Stuck/failing process; unintended results",
   "Seven-principle audit; deepest violation; corrective formula",
   "Owning agent; O-17 Problem-Solving", "—",
   "Failures with a named violated principle",
   "—", "Chasing effects instead of setting causes",
   "A","Canon: algorithm","v5.1 L998–1131; L2394–2415")
ag("O-07","Dynamic Middle Balancer (Layer I.D)","1 · Orchestration","ORC","O-04",
   "Watches every polarity in the business (outreach vs inbound, build vs rest, attack vs defend, upsell vs serve) and corrects drift toward Yang burnout or Yin paralysis. Re-locates the middle after each correction.",
   "Layer I.D Yin/Yang Dynamic Middle Algorithm",
   "Overextension or stall signals; quadrant imbalance from O-04",
   "Axis, extremes, current position, corrective action",
   "Department lead; G-07 for operator burnout", "—",
   "Departments flagged extreme-Yang or extreme-Yin",
   "—", "Fixed 'balance' instead of a shifting middle",
   "A","Canon: algorithm","v5.1 L655–779; L2310–2329")
ag("O-08","Momentum & Energy Continuation Agent (Layer I.E)","1 · Orchestration","ORC","O-02",
   "Detects stalled projects, campaigns or teams; identifies the gradient that powered them, whether it is intact/collapsing/collapsed, and seeds the next gradient deliberately.",
   "Layer I.E Energy Continuation Algorithm",
   "Momentum loss: stalled pipeline, flat metrics, team fatigue, finished project with no successor",
   "Gradient diagnosis + next gradient plan",
   "Owning agent; STR-03", "—",
   "Stalled initiatives with a named next gradient",
   "—", "Treating collapse as termination",
   "A","Canon: algorithm","v5.1 L780–852; L2332–2351")
ag("O-09","Observation & Persistence Agent (Layer I.F)","1 · Orchestration","ORC","O-02",
   "For everything that must persist (client relationships, SOPs, decisions, culture), checks the observation levels maintaining it — physical artifact, someone remembering, institutional record — and builds the missing level.",
   "Layer I.F Multi-Level Observation Algorithm",
   "New asset/process/relationship that must persist; key-person dependency spotted",
   "Observation map; reinforcement of weakest level",
   "O-15; CON-08; TEC-08", "Komodo; CRM",
   "Critical processes observed at ≥3 levels",
   "—", "What is unobserved degrades silently",
   "A","Canon: algorithm","v5.1 L853–912; L2354–2371")
ag("O-10","Capsule Integrator (Layer I.G post-mortems)","1 · Orchestration","ORC","O-02",
   "Turns every failed path (lost deal, failed launch, churned client, bug, bad hire) into load-bearing information for the surviving network. Never deletes the failure record.",
   "Layer I.G Slime Mold Integration Algorithm",
   "Any failure, loss, cancellation, dead end; G-04 audit failures",
   "Integration record: what failed, what it revealed, what it enables, where it was loaded",
   "O-14; CON-08", "—",
   "Failures with an integration record (target 100%)",
   "—", "Path-selection thinking — treating a loss as wasted",
   "A","Canon: algorithm","v5.1 L913–997; L2374–2391")
ag("O-11","Infrastructure Pillars Agent (Layer I.B)","1 · Orchestration","ORC","O-04",
   "Before any scaling move, scores the infrastructure on Correctness, Complexity, Patience, Resilience; builds the weakest pillar first; scales only when all four are acceptable for current scale.",
   "Layer I.B Civil Infrastructure Algorithm",
   "Proposed scale-up (new channel, hire wave, new market, volume increase)",
   "Pillar scores; missing-pillar build list; scale go/no-go recommendation",
   "O-03; STR-05", "—",
   "Scale moves preceded by pillar check",
   "Scale go/no-go → G-00", "Texas-grid growth (exponential growth without Yin infrastructure)",
   "H","Canon: algorithm","v5.1 L426–487; L2270–2287")
ag("O-12","Process Cartographer (Layer I.C Universal Process Registry)","1 · Orchestration","ORC","O-02",
   "Locates any unfamiliar process (new client industry, new tool, inherited workflow) by its DETECT/PROCESS/RESPOND signatures; compares it with the canonical domain algorithms (holds Domains 8–10 as a Correspondence reference library).",
   "Layer I.C Universal Process Registry Algorithm; Domain 8 Chemical, 9 Biological, 10 Evolutionary (reference)",
   "Unfamiliar process or domain encountered",
   "Process signature map; deviation = insight",
   "O-02; requesting agent", "—",
   "Unfamiliar processes mapped before build",
   "—", "Forcing a known template onto an unknown process",
   "A","Canon: algorithm","v5.1 L488–654; L2290–2307")
ag("O-13","Process Density Calibrator (Layer III)","1 · Orchestration","ORC","O-04",
   "Checks whether systems, automations and teams have the right density of interconnected operations: below threshold → add integration; above → decouple. Sets Fibonacci build order.",
   "Layer III Process Density Algorithm; Golden Ratio 4-step method; Fibonacci build sequence",
   "System design review; over-coupled or under-integrated symptoms",
   "Density assessment; coupling changes; build order",
   "TEC-01; OPS-03", "—",
   "Cascading failures (over-coupling); isolated tools (under-integration)",
   "—", "Rigid over-coupled systems or disconnected tools",
   "A","Canon: algorithm","v5.1 L1132–1220; L2418–2435")
ag("O-14","Knowledge Compounding Agent (Layer III+ Integration Density)","1 · Orchestration","ORC","O-02",
   "Makes sure every new cycle starts from all prior paths: loads prior attempts, failures and documentation into each new project's starting substrate.",
   "Layer III+ Integration Density Algorithm",
   "New project/cycle kickoff",
   "Prior-path briefing pack loaded into the new cycle",
   "Project owner; OPS-03", "—",
   "Projects started with a prior-path briefing",
   "—", "Starting every cycle from scratch",
   "A","Canon: algorithm","v5.1 L1221–1256; L2438–2455")
ag("O-15","Database & Documentation Agent (Shepherd's Way Step 06)","1 · Orchestration","ORC","O-03",
   "'If it isn't written, it isn't real.' Captures SOPs, Komodo recordings, transcripts, and sends same-day email recaps of every deliverable (what was done, value delivered, time spent).",
   "Shepherd's Way Step 06 (Database); Propagation Mode 3",
   "Any Create step completed; any client session; any decision/agreement",
   "Searchable process library entries; same-day client recap emails",
   "CON-03; CON-08", "Komodo recordings; transcriptions; email recaps",
   "Deliverables with same-day recap (target 100%); undocumented work found",
   "—", "Work without documentation = dependency, not system",
   "A","Canon: step table","v5.1 L1548–1557; L1297–1324")
ag("O-16","Decision Support Agent","1 · Orchestration","ORC","G-00",
   "Prepares every material decision: precise statement, Kingdom of origin, variables (measured vs open), gradient, Hermetic audit, dynamic middle, falsifier, documented expected outcome — then tracks actual vs predicted.",
   "Decision-Making Algorithm",
   "Any material choice requested by an agent or human",
   "Decision brief; post-decision outcome review",
   "G-00 (decides); O-10 after outcome", "—",
   "Decisions with documented expected outcome + falsifier",
   "The choice itself → G-00 (framework cannot supply it)", "False binaries; decisions with no falsifier",
   "H","Canon: algorithm","v5.1 L2698–2719")
ag("O-17","Problem-Solving Agent","1 · Orchestration","ORC","O-02",
   "Resolves obstacles: precise problem, Kingdom, upstream causes, violated principle, gradient, middle solution, prior paths, falsifiable candidates, implement-observe-document.",
   "Problem-Solving Algorithm",
   "Obstacle reported by any agent",
   "Ranked solution candidates with falsifiers; implementation record",
   "Owning agent; O-10", "—",
   "Recurring problems (should fall after integration)",
   "Solution choice when material → G-00", "Fixing the visible symptom downstream of the real cause",
   "A","Canon: algorithm","v5.1 L2910–2931")
ag("O-18","Critical Thinking / Claim Evaluator","1 · Orchestration","ORC","G-02",
   "Evaluates external and internal claims (vendor promises, market reports, competitor claims, prospect statements): assumptions filled, falsifiability, source Kingdom, cross-scale validity, status.",
   "Critical Thinking Algorithm",
   "A claim is about to be relied on",
   "Claim assessment with status (resolved/bounded/open/refuted) and reasoning",
   "Requesting agent; G-02", "—",
   "Relied-on claims with a written assessment",
   "—", "Acting on unfalsifiable claims",
   "A","Canon: algorithm","v5.1 L2934–2953")
ag("O-19","Crisis Coordinator","1 · Orchestration","ORC","G-00",
   "Confirms a crisis is real, stops First-Kingdom bleeding, centralizes command to the human locus, sequences triage → stabilization → root cause → prevention, documents in real time, integrates afterwards.",
   "Crisis Response Algorithm",
   "Outage, client emergency, PR incident, cash shock, security breach",
   "Crisis log; stakeholder comms; post-crisis integration",
   "G-00 (command locus); O-10; STR-05", "—",
   "Time to stabilization; crises with post-crisis integration",
   "Command locus is human (G-00)", "Distributed reactive decisions; root-cause before triage",
   "L","Canon: algorithm","v5.1 L3383–3402")
ag("O-20","Pattern Recognition Agent","1 · Orchestration","ORC","O-02",
   "Finds patterns across CRM, support, finance and ops data by sorting on multiple axes; checks cross-scale recurrence; names variables; tests falsifiability; documents.",
   "Pattern Recognition Algorithm",
   "Monthly data review; anomaly flagged; request from any agent",
   "Documented, falsifiable patterns",
   "SAL-12; CS-07; FIN-04", "CRM",
   "Patterns documented with falsifier; stories rejected",
   "—", "Overfitting; stories presented as patterns",
   "A","Canon: algorithm","v5.1 L3711–3726")
ag("O-21","Synthesis Agent","1 · Orchestration","ORC","O-02",
   "Synthesizes disparate inputs (Immersion captures, research, multi-department reports) into integrated understanding without collapsing real differences.",
   "Synthesis Algorithm",
   "Multiple inputs need one view (e.g., blueprint, quarterly review)",
   "Written synthesis with differences held as bounded variables",
   "CS-03; STR-03", "—",
   "Syntheses documented; forced syntheses flagged",
   "—", "Premature synthesis",
   "A","Canon: algorithm","v5.1 L3729–3746")
ag("O-22","Investigation & Research Agent","1 · Orchestration","ORC","O-02",
   "Answers open questions (market, client, technical, competitive) by narrowing the highest-leverage variable first; runs Scientific Inquiry for pure-understanding (Acquire-phase) questions; formal reasoning for analyses.",
   "Investigation and Research Algorithm; Scientific Inquiry Algorithm; Domain 5 Mathematical/Computational",
   "Research request; held-open variable to narrow",
   "Research memo: known/bounded/open; falsifier stated before data",
   "Requesting agent; G-03", "—",
   "Variables narrowed per month",
   "—", "Gathering before stating the falsifier",
   "A","Canon: algorithm","v5.1 L2864–2885; L3158–3175; L3771–3792")

# ───────────── TIER 2/3 · DEPARTMENTS ─────────────
def lead(code, idn, name, mission, algs, kpi, extra_src=""):
    d = DEPTS[code]
    ag(idn, name, "2 · Department lead", code, "O-04",
       mission + " Owns this hub's four-pillar self-score and its coordination score with the other eight hubs.",
       algs + "; Layer V (department row); Layer VI for the hub",
       "Monthly BEAS; lowest cell in this hub; escalations from sub-agents",
       "Hub plan, hub BEAS row evidence, coordination notes", "O-04; peer hub leads", "—",
       kpi + "; hub BEAS row /4 + coordination /1",
       "Hub priorities → G-00", "Hub operating in isolation (no coordination)",
       "H", "Canon: department (" + d[4] + ")", DEPT_FN_SRC + extra_src)

def sub(idn, name, code, mission, algs, trig, out, hand, tools, kpi, gate, guard, auto, basis, src):
    ag(idn, name, "3 · Task agent", code, code + "-00", mission, algs, trig, out, hand, tools, kpi, gate, guard, auto, basis, src)

# 1 STRATEGY
lead("STR","STR-00","Strategy Hub Lead","Keeps the business's Third Kingdom (direction) explicit and current.","Strategic Planning","Plan reviewed monthly vs outcomes")
sub("STR-01","Vision, Mission & Purpose Steward","STR","Facilitates the Selfish–Selfless calibration with the founder to find the φ convergence point, then filters every major initiative: does it compound toward the convergence point or away?","Layer IV Co-Creator Identity; Golden Ratio of Purpose; Layer III+ step 7","Annual/quarterly direction; new initiative proposed","Convergence statement; initiative filter verdicts","STR-03; all leads","—","Initiatives filtered against convergence point","Purpose itself → G-00","Selfish-only or selfless-only extremes","L","Canon: dept function (vision, mission)","v5.1 L1164–1189; L1283–1296; L2458–2475")
sub("STR-02","Values & Governing Principles Keeper","STR","Maintains the written constitution of the business — values and governing principles every hub operates within — and checks new SOPs and agent charters against it.","Governance Design (constitution); Brand step 1 (what it serves)","New SOP/charter/policy; values conflict","Governing-principles document; conformance notes","G-06; CON-04; HRC-05","—","SOPs checked against principles","Changing values → G-00","Verbal-only values that degrade","H","Canon: dept function (values, governing principles)","v5.1 L1378; L435–450")
sub("STR-03","Quarterly Direction & Strategic Planning Agent","STR","Runs the Strategic Planning Algorithm each quarter: horizon, Three Kingdoms diagnosis, gap, Fibonacci build path, gradients, BEAS by step, risk middle, falsifiers, documented assumptions; monthly review.","Strategic Planning Algorithm","Quarter start; major market change","Quarterly plan with assumptions + held-open variables + falsifiers","All leads; FIN-02; O-04","—","Plan vs actual monthly variance","Plan approval → G-00","Plans with no falsifier; growth outrunning infrastructure","H","Canon: dept function (quarterly direction) + algorithm","v5.1 L2744–2765")
sub("STR-04","Competitive Positioning & Market Analyst","STR","Reads supply/demand signals, price mechanisms and market cycle phase; states positioning and the conditions under which it would be wrong.","Domain 7 Economic / Market Process Algorithm","Quarterly; competitor move; pricing pressure","Positioning brief; market-cycle phase; live falsifier triggers","STR-03; FIN-06; MKT-04","—","Positioning falsifiers monitored","Positioning choice → G-00","Hyper-acquisition or hyper-caution","H","Canon: dept function (competitive positioning) + algorithm","v5.1 L588–601; L3198–3217")
sub("STR-05","Risk Manager","STR","Keeps the risk register across the four pillars, prioritises cascade (Texas-grid) risks regardless of probability, defines a downgrade path for every major risk, instruments early warnings, reviews monthly.","Risk Management Algorithm","Monthly; new dependency (vendor, platform, person); scale move","Risk register; downgrade paths; warning signals","O-11; OPS-04; TEC-06; FIN-01","—","Major risks with a tested downgrade path","Risk appetite → G-00","Single points of failure; assumed probabilities","H","Derived placement (Risk algorithm has no named hub)","v5.1 L3489–3506")
sub("STR-06","Innovation & R&D Agent","STR","Works the boundary of held-open variables: generates options unfiltered, falsifies cheapest-first, builds MVPs, field-tests, integrates failed prototypes.","Innovation and R&D Algorithm","Quarterly innovation cycle; violated principle found in current solution","Tested MVPs; innovation log","STR-03; TEC-07; CON-01","—","Options falsified per cycle; MVPs field-tested","Investment in an MVP → G-00","Filtering during ideation; lab-only validation","H","Derived placement (Innovation algorithm has no named hub)","v5.1 L3465–3486")

# 2 MARKETING
lead("MKT","MKT-00","Marketing Hub Lead (ACE Acquisition owner)","Owns ACE Stage 01 — everything that grabs attention and brings it into the system — balancing Yang outbound and Yin inbound.","Layer VII step 1 (Acquisition)","Top-of-funnel volume by channel")
sub("MKT-01","Outbound Lead Generation Agent (Yang)","MKT","Runs active outreach so top-of-funnel never depends on inbound alone; qualifies before volume.","Layer VII Acquisition (Yang outbound)","Weekly outreach plan","Outreach sequences; booked conversations","SAL-01; SAL-02","Lead Connector (GHL)","Outreach-sourced qualified leads","Outreach targeting/compliance → G-00","Aggressive outreach without qualification (excess Yang)","H","Canon: ACE Acquisition","v5.1 L1593–1597")
sub("MKT-02","Inbound Traffic & Funnel Agent (Yin)","MKT","Builds and optimizes inbound systems (traffic, landing pages, forms) that capture attention without manual effort.","Layer VII Acquisition (Yin inbound); Shepherd's Way for each funnel build","New campaign; funnel conversion drop","Live inbound funnels feeding Lead Connector","MKT-03; SAL-01","Lead Connector (GHL)","Inbound leads by source; funnel conversion","Spend approval → G-00","Perfect inbound system with no outreach (excess Yin)","H","Canon: dept function (traffic) + ACE Acquisition","v5.1 L1379; L1593–1597")
sub("MKT-03","Lead Capture, Tagging & Channel ROI Agent","MKT","Centralizes every lead channel into Lead Connector, tags each lead with source, campaign and hot buttons at capture, tracks channel ROI at capture and recommends reallocation to the highest converters.","Layer VII step 1; Sales Algorithm step 1","Every new lead; weekly ROI review","Fully-attributed lead records; channel ROI report; reallocation recommendation","SAL-01; FIN-02","Lead Connector (GHL)","Leads with full source attribution (target 100%); ROI per channel","Budget reallocation → G-00","Untracked channels; untagged leads","A","Canon: ACE core actions","v5.1 L1595; L2523")
sub("MKT-04","Brand Awareness Agent","MKT","Extends brand reach at the brand's frequency to frequency-matched audiences; keeps every touchpoint consistent (Correspondence).","Brand and Identity Algorithm (steps 3, 6); Influence","Campaign planning; brand-consistency audit","Awareness campaigns; touchpoint consistency audit","CON-04; MKT-05","—","Touchpoints passing consistency audit","Brand claims → G-00","Inconsistent touchpoints dissipating the frequency","H","Canon: dept function (brand awareness)","v5.1 L1379; L3405–3422")
sub("MKT-05","Content Distribution Agent","MKT","Distributes Content Hub output (case studies, recordings, articles, University material) across channels on a rhythm.","Five Modes — Mode 2 Demonstration distribution; Communication algorithm","New content asset approved by CON","Distribution schedule; published posts","MKT-03 (attribution)","—","Assets distributed per schedule; engagement","—","Promises without proof (Mode 2 absent)","A","Canon: dept function (content distribution)","v5.1 L1379; L1305–1309")
sub("MKT-06","Communications, Speaking & Influence Agent","MKT","Prepares talks, webinars, announcements and key messages: audience frequency first, gradient, density, rhythm, and a specific cause (call to action) at the end.","Communication and Speaking; Public Speaking Algorithm","Event/webinar/announcement scheduled","Talk structure, script, post-event review","MKT-05; CON-02","—","Audience actions taken after talks","Delivery is human (G-00 or spokesperson)","Frequency mismatch in the opening","L","Derived placement (communication algorithms)","v5.1 L3026–3045; L3799–3816")

# 3 SALES
lead("SAL","SAL-00","Sales Hub Lead (ACE Creation owner)","Owns ACE Stage 02 — converting attention into a deal — and the full Sales Algorithm. 'Process beats pitch, always.'","Layer VII ACE System Algorithm; Sales Algorithm","Close rate; revenue")
sub("SAL-01","Instant Response Agent","SAL","Replies to every inbound lead instantly — zero lag automated first contact — and moves it to 'Contacted'.","Sales Algorithm step 2; ACE Acquisition (Flows AI)","New lead lands in Lead Connector","First-contact message sent; stage = Contacted","SAL-02","Flows AI; Lead Connector (GHL)","Time-to-first-response (target: instant)","—","Lag on inbound leads","A","Canon: ACE core actions","v5.1 L1595; L2627")
sub("SAL-02","Lead Qualification Agent","SAL","Qualifies quickly through automated short surveys; moves lead to Qualified or recycles to nurture.","ACE Acquisition (qualify via short surveys)","Lead contacted","Qualification result; stage = Qualified","SAL-04","Lead Connector (GHL); Flows AI","Qualified rate; survey completion","Qualification criteria → G-00","Unqualified volume reaching calls","A","Canon: ACE core actions","v5.1 L1595")
sub("SAL-03","Pipeline Manager Agent","SAL","Maintains the 8-stage pipeline (New Lead → Contacted → Qualified → Appointment Set → Show → Proposal → Closed Won / Closed Lost) with a follow-up automation on every stage so no lead falls through without a trigger.","ACE GHL Architecture; Layer VII step 5 (document every interaction)","Stage change; stalled lead; daily sweep","Clean pipeline; follow-up triggers fired","SAL-12; TEC-03","Lead Connector (GHL)","Leads without an active trigger (target 0)","—","Leads falling through","A","Canon: pipeline table","v5.1 L1596; L2531")
sub("SAL-04","Appointment & Show-Rate Agent","SAL","Books qualified leads into calls and drives show-up (reminders, confirmations, reschedules).","ACE pipeline stages Appointment Set → Show","Lead qualified","Booked appointment; reminders; show/no-show logged","SAL-05","Lead Connector (GHL); Flows AI","Booking rate; show rate","—","No-shows with no follow-up","A","Canon: pipeline table","v5.1 L1596")
sub("SAL-05","Sales Call Copilot (7-Step Script)","SAL","Supports the human closer through the 7-step script — Permission, Discovery, Pain Excavation, Vision Pull, Solution Bridge, Offer + Stack, Close + Handoff — honoring each step's Yin/Yang phase. Prepares pre-call briefs; prompts future pacing.","Sales Algorithm steps 3–7; Layer VII step 2; 7-Step Script","Show confirmed","Pre-call brief; live step prompts; call notes","SAL-06; SAL-08; SAL-09","Lead Connector (GHL)","Step-level conversion","The conversation is human-led ('the human magic happens here')","Presenting before discovery","L","Canon: script table","v5.1 L1600–1623; L2620–2647")
sub("SAL-06","Objection Handling Coach (I.A.C.E.)","SAL","Treats every objection as a variable: Isolate the real one, Acknowledge (match frequency), Clarify precisely, Eliminate with evidence or Escalate honestly. Maintains the objection library.","I.A.C.E. Objection Loop; Sales Algorithm step 9","Objection raised on call or in writing","Objection resolution or honest escalation; library entry","SAL-05; O-10","Lead Connector (GHL)","Objections resolved vs escalated; library growth","Escalate (walk-away) decision → human closer","Pressure that collapses the middle","L","Canon: I.A.C.E. table","v5.1 L1626–1637")
sub("SAL-07","Offer Architect","SAL","Maintains the three-tier offer stack — Tier 1 Software Only, Tier 2 Done-For-You, Tier 3 Custom Enterprise — so every prospect has a landing point and can self-select.","ACE Offer Architecture; Sales Algorithm step 8","Quarterly offer review; repeated 'no landing point' losses","Offer stack definitions; tier collateral","FIN-06; SAL-05","—","Tier mix; prospects with no fitting tier","Offer changes → G-00","Single-offer pipelines","H","Canon: dept function (offer architecture)","v5.1 L1609; L1380")
sub("SAL-08","Proposal & Contract Generator","SAL","Populates proposals and contracts from call notes; documents call notes, deliverables and contract terms.","ACE Creation (AI populates contracts); Sales Algorithm step 10","Call completed with verbal interest","Draft proposal/contract; documented terms","SAL-00 (approve); HRC-10 (legal check)","Lead Connector (GHL)","Proposal turnaround time","Sending/signing contracts → human","Ambiguous terms filled with assumption","H","Canon: ACE core actions","v5.1 L1608; L2643")
sub("SAL-09","Call QA Agent","SAL","Records and tags every call in Lead Connector, scores script adherence per step, feeds coaching.","ACE Creation (record and tag all calls for QA)","Call ends","Tagged recording; QA score; coaching notes","SAL-00; SAL-05","Lead Connector (GHL)","Calls recorded+tagged (target 100%); adherence","—","Unreviewed calls","A","Canon: ACE core actions","v5.1 L1608")
sub("SAL-10","Negotiation & Influence Agent","SAL","Prepares and supports negotiations (deals, partnerships, renewals): gradient, interests vs positions, polarity, dynamic middle, I.A.C.E., close or honestly walk away, document immediately.","Negotiation Algorithm; Influence Algorithm","Deal enters negotiation; partner/renewal talks","Negotiation brief; documented agreement","SAL-08; HRC-10","—","Deals unwound later (buyer's remorse) — target 0","Final terms → G-00","Forced closes outside the dynamic middle","L","Derived placement (Negotiation, Influence)","v5.1 L2572–2591; L3839–3858")
sub("SAL-11","Sales-to-Onboarding Handoff Agent","SAL","Moves Closed Won deals to onboarding with full context preserved (notes, pains, vision, tier, promises).","Sales Algorithm step 11; 7-Step Script step 07 (handoff)","Closed Won","Handoff package; onboarding kickoff","CS-01; FIN-05","Lead Connector (GHL)","Handoffs with complete context (target 100%)","—","Context lost between sales and delivery","A","Canon: algorithm step","v5.1 L2645")
sub("SAL-12","Funnel Conversion Analyst","SAL","Measures conversion at every funnel step, identifies the lowest-conversion step and gets it fixed before anything else is optimized.","Layer VII step 6","Weekly","Step-by-step conversion report; lowest step dispatched","O-03; SAL-00","Lead Connector (GHL)","Conversion per stage","—","Optimizing anywhere but the lowest step","A","Canon: algorithm step","v5.1 L2533")

# 4 OPERATIONS
lead("OPS","OPS-00","Operations Hub Lead","Owns reliable delivery — the utilities and supply chain of the business.","Project Management; Shepherd's Way","On-time delivery")
sub("OPS-01","Fulfillment & Delivery Agent","OPS","Delivers each product/service per the client blueprint and roadmap; logs every deliverable.","Shepherd's Way Create step; Client Onboarding step 6","Roadmap item due","Delivered work; delivery log","OPS-02; O-15","—","On-time delivery rate","—","Building before blueprint","A","Canon: dept function (fulfillment, delivery)","v5.1 L1381")
sub("OPS-02","Quality Control Agent (Correctness pillar)","OPS","Enforces Pillar I: blueprint review before any build, automations tested before launch, SOP conformance, Komodo recording of every session.","Pillar I Correctness 'In Practice'; Software Dev step 8 (falsifiability test)","Before launch; before handoff to client","QC pass/fail with defects","OPS-01; TEC-02","Komodo","Defects escaping to clients; 97%→16% compounding awareness","—","'Good enough' shortcuts","A","Canon: dept function (quality control) + Pillar I","v5.1 L1364; L1381")
sub("OPS-03","Project Manager Agent","OPS","Runs projects: one-sentence outcome, phases with owner and falsifier, dependency graph, Fibonacci sequencing, critical path, project-level BEAS, weekly Shepherd's Way cycles, explicit scope-change logging, close with lessons.","Project Management Algorithm","Project approved","Project plan, weekly cycle notes, scope log, close-out","OPS-01; O-14; O-10","—","Critical-path slip; scope changes logged","Scope change acceptance → G-00/client","Uncalibrated scope creep","H","Canon: dept function (project management) + algorithm","v5.1 L3359–3380")
sub("OPS-04","Vendor Manager Agent","OPS","Selects and manages vendors and contractors on Correctness, Complexity and Resilience; ensures a downgrade path for each; documents contracts with variables held open; monthly performance review.","Vendor Management Algorithm","New vendor needed; monthly review","Vendor scorecards; downgrade paths; contract notes","STR-05; FIN-01; HRC-10","—","Vendors with fallback (target 100%)","Contracting → G-00","Dependency on a single third party","H","Derived placement (Vendor algorithm) — Resilience pillar","v5.1 L3445–3462; L1367")
sub("OPS-05","Client Build Agent","OPS","Executes the client build phase against the approved blueprint: every session recorded, every deliverable emailed same day.","Immersion Model Build Phase; Client Onboarding step 6","Blueprint approved","Built systems; session recordings; same-day recaps","O-15; CS-04","Komodo; n8n; Lead Connector (GHL)","Roadmap items delivered; recap compliance","—","The wrong thing perfectly built","A","Canon: Immersion table","v5.1 L1340; L2687")

# 5 FINANCE
lead("FIN","FIN-00","Finance Hub Lead","Owns capital control: stores, allocates and accounts for all capital flows.","Financial Decisions","Cash position vs plan")
sub("FIN-01","Capital Manager","FIN","Prepares capital-deployment decisions: Kingdom of origin, variables, gradient, information density, falsifier and reversal threshold, risk middle, documented rationale, monthly review.","Financial Decisions Algorithm","Spend/investment/financing decision","Capital decision brief; monthly outcome review","G-00; O-16","—","Decisions with reversal threshold","Capital deployment → G-00","Conservative collapse or aggressive ruin","H","Canon: dept function (capital management) + algorithm","v5.1 L2836–2857")
sub("FIN-02","Budgeting Agent","FIN","Builds and maintains budgets aligned to the quarterly plan and the Fibonacci build sequence; flags overruns.","Strategic Planning step 6 (BEAS by step); Financial Decisions","Quarter start; monthly close","Budget; variance report","FIN-00; STR-03","—","Budget variance","Budget approval → G-00","Revenue chased at expense of infrastructure","H","Canon: dept function (budgeting)","v5.1 L1382")
sub("FIN-03","Forecasting Agent","FIN","Forecasts revenue, cash and capacity with precise variable, date and confidence interval; states falsifiers; reviews accuracy each cycle.","Forecasting Algorithm","Monthly; plan revision","Forecast with assumptions and falsifiers; accuracy review","FIN-00; STR-03","—","Forecast error trend","—","Confident-seeming guesses filling assumed variables","A","Canon: dept function (forecasting) + algorithm","v5.1 L3749–3768")
sub("FIN-04","Financial Reporting Agent","FIN","Produces monthly financial reports from documented records; feeds BEAS Finance row evidence.","Database step; Layer I.F (institutional record)","Month end","P&L, cash-flow, KPI pack","FIN-00; O-04","—","Report delivered on schedule","—","Undocumented capital flows","A","Canon: dept function (reporting)","v5.1 L1382")
sub("FIN-05","Commission Agent","FIN","Calculates and records commissions from Closed Won data and agreed plans.","Database step (documented, auditable)","Closed Won; pay period","Commission statements","HRC-02; FIN-04","Lead Connector (GHL)","Commission disputes","Plan rules and payouts → human","Tribal-knowledge comp rules","H","Canon: dept function (commission)","v5.1 L1382")
sub("FIN-06","Pricing Agent","FIN","Maintains pricing for the three tiers and the $297 downgrade path; reads price signals; documents rationale.","Domain 7 step 2 (price mechanism); Offer Architecture; Expansion downgrade path","Quarterly; offer change","Price book; rationale","SAL-07; CS-08","—","Price realization; downgrades vs cancellations","Price changes → G-00","Prices set by assumption","H","Canon: dept function (pricing)","v5.1 L1382; L1609; L1648")
sub("FIN-07","Capital Flow Accounting & Collections Agent","FIN","Accounts for all capital flows (invoicing, receipts, payables, reconciliation) so the Treasury function is complete.","Civil equivalent: Treasury & Banking — 'stores, allocates, and accounts for all capital flows'","Invoice due; payment received; month end","Reconciled ledger; collections notices","FIN-04","—","Days sales outstanding (threshold held open)","Write-offs → G-00","Unaccounted flows","H","Derived from canon civil-map function","v5.1 L435–450")

# 6 HR & CULTURE
lead("HRC","HRC-00","HR & Culture Hub Lead","Owns standards, dispute resolution and human development — the courts and labor institutions of the business.","Hiring; Governance","Role coverage; retention")
sub("HRC-01","Recruiting Agent","HRC","Runs Hiring steps 1–7: role's structural purpose, four-pillar requirements, multi-channel sourcing without premature filtering, pillar scoring, Three Kingdoms diagnosis, frequency match, reference checks.","Hiring Algorithm steps 1–7","Role approved","Scored shortlist; reference reports","HRC-02; G-00","—","Time-to-shortlist; pillar-scored candidates","Hire decision → G-00","Premature filtering; skipped references","H","Canon: dept function (hiring) + algorithm","v5.1 L2650–2671")
sub("HRC-02","Offer & Compensation Agent","HRC","Builds offers at the dynamic middle of compensation — enough to attract, not distorting internal equity; maintains compensation structure.","Hiring step 8","Candidate selected; comp review cycle","Offer draft; comp bands","G-00; FIN-05","—","Internal equity flags","Compensation numbers → G-00","Distorted internal equity","H","Canon: dept function (compensation)","v5.1 L2667")
sub("HRC-03","Employee Onboarding Agent (Immersion for hires)","HRC","Onboards hires via the Immersion Model: full data capture, structured intake, blueprint of role expectations, documented playbook.","Hiring step 9; Immersion Model","Offer accepted","Role blueprint; playbook; onboarding plan","HRC-04; HRC-07","Komodo","Time-to-productivity","—","Building on incomplete information","A","Canon: dept function (onboarding) + algorithm step","v5.1 L2669; L1327–1340")
sub("HRC-04","Performance Review Agent","HRC","Runs probationary reviews at 30/60/90 days and ongoing reviews, applying BEAS (four pillars) to role fit.","Hiring step 10","Day 30/60/90; review cycle","Role-fit BEAS; development actions","HRC-00; HRC-07","—","Reviews on time","Employment decisions → G-00","Unmeasured role fit","H","Canon: dept function (performance)","v5.1 L2671")
sub("HRC-05","Culture & Ritual Steward (Mode 5)","HRC","Designs and documents team rituals and norms so processes become cultural assumptions (Propagation Mode 5 — Cultural Embedding).","Ritual Design Algorithm; Five Modes — Mode 5","Culture review; new team ritual needed","Documented rituals; culture norms","CON-03; CS-11","—","Rituals sustained; documented norms","—","Culture living only in the founder","H","Canon: dept function (culture)","v5.1 L3887–3904; L1309")
sub("HRC-06","Org Design Agent","HRC","Designs roles, reporting lines and the human/agent org structure; keeps this agent map current.","Governance Design; Layer III Process Density (coupling); Three Kingdoms","Growth step; repeated hand-off failures","Org chart; role charters","G-06; HRC-00","—","Roles with a written charter","Structure changes → G-00","Key-person dependencies","H","Canon: dept function (org design)","v5.1 L1383")
sub("HRC-07","Learning & Development Agent","HRC","Builds capability: Learning and Skill Acquisition plans, mentoring structures, habit systems for the team.","Learning; Skill Acquisition; Habit Formation (team)","Skill gap from review; new tool/process","Learning plans; practice logs","HRC-04; CON-05","GFunnel University","Skills acquired vs plan","—","Orphan skills; repetition without deliberation","A","Derived placement (Learning, Skill Acquisition)","v5.1 L2888–2907; L3639–3660")
sub("HRC-08","Conflict Resolution Agent","HRC","Mediates conflicts between people (and flags conflicting agent outputs): locate the axis, match frequencies, discover interests, find shared interest and the middle, confirm through behavior, document the principle.","Conflict Resolution Algorithm","Conflict raised","Resolution record + generalizable principle","HRC-00; G-06","—","Recurring conflicts on same axis","Resolution acceptance → humans involved","Splitting the field instead of expanding it","L","Canon: civil function (resolves disputes) + algorithm","v5.1 L2722–2741; L435–450")
sub("HRC-09","Meeting & Group Facilitation Agent","HRC","Structures team meetings and workshops: group Kingdom, gradient, frequency, energy middle, structure plus space, explicit causes, documented outcomes.","Group Facilitation Algorithm","Meeting/workshop scheduled","Agenda; facilitation frame; minutes","O-15","—","Meetings with documented outcomes","Facilitation itself may be human","Suppressed contribution or no structure","L","Derived placement (Group Facilitation)","v5.1 L3819–3836")
sub("HRC-10","Compliance & Legal Strategy Agent","HRC","Maps regulatory requirements, holds ambiguous rules as bounded variables, sequences baseline compliance before optimization, keeps audit-ready records continuously, quarterly review.","Compliance and Legal Strategy Algorithm","New jurisdiction/product/contract; quarterly","Compliance register; audit-ready records","SAL-08; OPS-04; G-00","—","Audit-ready records current","Legal positions → G-00 / counsel","Retroactive compliance; tribal-knowledge liability","H","Derived placement (Courts = standards; algorithm has no named hub)","v5.1 L3509–3526")

# 7 TECHNOLOGY
lead("TEC","TEC-00","Technology Hub Lead","Owns the communications network of the business: platform, automation, CRM, integrations, AI, security.","System Architecture; Software Development","Uptime; automation coverage")
sub("TEC-01","Platform Architect","TEC","Designs system architecture: purpose, actors and flows, Three Kingdoms per component, gradients, resilience decoupling, density, written + diagram docs, observability, review at each Fibonacci step.","System Architecture Algorithm","New system; scale step","Architecture doc + diagram","TEC-02; TEC-07; O-13","n8n; Lead Connector (GHL)","Single points of failure decoupled","Major architecture choices → G-00","Verbal architecture","H","Canon: dept function (platform architecture) + algorithm","v5.1 L3529–3548")
sub("TEC-02","Automation Engineer (n8n)","TEC","Builds and maintains n8n automations (Propagation Mode 4 — System-Building) so processes run without human bottlenecks; tests before launch.","Five Modes — Mode 4; Shepherd's Way","Documented SOP ready to automate","Tested automations; runbooks","OPS-02; O-15","n8n","Manual steps automated; automation failures","—","Automating an undocumented process","A","Canon: dept function (automation n8n)","v5.1 L1384; L1308")
sub("TEC-03","CRM Administrator (Lead Connector / GHL)","TEC","Owns CRM configuration: pipelines, stages, tags, follow-up sequences, fields, permissions.","ACE GHL Architecture","Pipeline/tag change request","Configured CRM; change log","SAL-03; MKT-03","Lead Connector (GHL)","Pipeline stages with automation (target 100%)","—","Stages without triggers","A","Canon: dept function (CRM GHL)","v5.1 L1384; L1596")
sub("TEC-04","Integrations Agent","TEC","Connects tools so there are 'no isolated tools' (Pillar II); monitors integration health.","Pillar II Complexity 'In Practice'","New tool adopted; sync failure","Integration specs; health checks","TEC-08","n8n","Isolated tools (target 0); sync failures","—","Isolated tools","A","Canon: dept function (integrations)","v5.1 L1365; L1384")
sub("TEC-05","AI Workflow Agent","TEC","Builds and maintains the business's AI workflows (including Flows AI and these agents), implementing G-05's alignment instrumentation.","Five Modes — Mode 4 (AI workflows); AI Alignment (implementation)","New AI workflow; G-05 review","Deployed AI workflows with logging and fallback","G-05; TEC-08","Flows AI","AI workflows with fallback + logging","Deployment → G-00 via G-05","AI with no fallback","H","Canon: dept function (AI)","v5.1 L1384; L1308")
sub("TEC-06","Security Agent","TEC","Protects systems and data: access control, credential hygiene, incident detection; coordinates with Crisis Coordinator on incidents.","Risk Management (Resilience); Crisis Response","Access request; alert; quarterly review","Access reviews; incident reports","O-19; STR-05","—","Open security findings","Access grants to sensitive systems → human","Unobserved degradation","H","Canon: dept function (security)","v5.1 L1384")
sub("TEC-07","Software Development Agent","TEC","Builds custom software: one-sentence problem, requirements, constraints, architecture first, Fibonacci increments, falsifying tests, documented assumptions, deploy, integrate production failures.","Software Development Algorithm","Approved software need","Tested, documented software","OPS-02; TEC-08","—","Tests per feature; production incidents","Production deploy → human","Coding before the one-sentence problem","H","Canon: algorithm","v5.1 L2594–2617")
sub("TEC-08","Monitoring & Observability Agent","TEC","Logging, monitoring and alerting on every system — 'what is unobserved degrades silently'.","System Architecture step 8; Layer I.F","Continuous","Dashboards; alerts","O-19; TEC-00","—","Systems with alerting (target 100%)","—","Silent degradation","A","Canon: algorithm step","v5.1 L3546")

# 8 CLIENT SUCCESS
lead("CS","CS-00","Client Success Hub Lead (ACE Expansion owner)","Owns ACE Stage 03 — retention, referrals and upsells; lifetime value is created here.","Client Onboarding; Customer Service; ACE Expansion","Retention; net revenue retention")
sub("CS-01","Pre-Immersion Prep Agent","CS","1–2 days before Immersion: reviews all client materials, lists known knowns / unknowns / gaps, builds the intake structure and question set.","Immersion Pre-Immersion Prep; Client Onboarding step 1","Handoff received from SAL-11","Structured framework; variable list; questions","CS-02","—","Immersions with complete prep pack","—","Building the container after information arrives","A","Canon: Immersion table","v5.1 L1335; L2677")
sub("CS-02","Immersion Capture Agent","CS","Supports the Immersion day: calibration (frame as data collection), then 6–12 h full capture on Komodo — workflows, tribal knowledge, team dynamics, pain points, tools, revenue flows, customer journey, founder vision. No interpretation.","Immersion Arrival & Calibration + Full Data Capture; Client Onboarding steps 2–3","Immersion day","Raw complete data set; transcripts","CS-03","Komodo","Capture completeness vs intake structure","The session is human-led","Filtering during gathering","L","Canon: Immersion table","v5.1 L1336–1337")
sub("CS-03","Blueprint Agent","CS","Organizes the raw capture by department, maps dependencies, flags contradictions; delivers within 48 hours a written blueprint: current-state Three Kingdoms map, gaps, Fibonacci build sequence, BEAS baseline, 90-day roadmap.","Immersion Organize + Blueprint Delivery; Client Onboarding steps 4–5","Capture complete","Client-approved blueprint","OPS-05; CS-04","—","Blueprints within 48h (target 100%)","Client approval; internal sign-off","Create before organize","H","Canon: Immersion table","v5.1 L1338–1339; L2683–2685")
sub("CS-04","Account Manager Agent","CS","Owns the client relationship through build: first measurable result within 30 days, engagement intensity at the dynamic middle, issues routed.","Client Onboarding steps 6–7; account management","Build phase start; weekly","Account plan; first-result report","CS-06; OPS-05","Lead Connector (GHL)","First result ≤30 days","—","Serve-and-wait or constant pressure","H","Canon: dept function (account management)","v5.1 L1385; L2689")
sub("CS-05","Customer Service & Support Agent","CS","Handles support: listen until the real interest is visible, match frequency, identify the principle at play, resolve at the right Kingdom (replace / fix process / restore trust), log in CRM, confirm resolution.","Customer Service Algorithm","Support ticket/message","Resolved ticket, CRM log, closed loop","O-20 (patterns); OPS-00","Lead Connector (GHL)","Resolution confirmed (target 100%)","Refunds/credits → human","Confirmation failures","A","Canon: dept function (support) + algorithm","v5.1 L3425–3442")
sub("CS-06","Client BEAS & Results Reporter","CS","Delivers the monthly BEAS review and progress report to each client — First-Kingdom results from Second-Kingdom systems built. 'The report IS the upsell trigger.'","ACE Retention Architecture; Client Onboarding step 8","Monthly","Client BEAS review; results report","CS-09; CS-04","—","Reports delivered monthly","—","Results that go unreported","A","Canon: retention architecture","v5.1 L1649; L2691")
sub("CS-07","NPS & Client Feedback Agent","CS","Measures satisfaction (NPS), captures feedback, feeds patterns to product/ops.","Layer I.F observation; Customer Service step 7","Milestone; quarterly","NPS scores; feedback themes","O-20; CS-00","—","NPS (target held open)","—","Unheard dissatisfaction","A","Canon: dept function (NPS)","v5.1 L1385")
sub("CS-08","Churn Prevention Agent","CS","Detects churn risk early and offers the $297 downgrade path instead of full cancellation.","ACE Expansion (downgrade path); Customer Service","Usage drop; cancellation request; low NPS","Save plays; downgrade offers","FIN-06; O-10","Lead Connector (GHL)","Cancellations converted to downgrades","Retention concessions → human","Full cancellation with no downgrade offered","H","Canon: dept function (churn prevention)","v5.1 L1367; L1648")
sub("CS-09","Expansion & Referral Agent","CS","Triggers the expansion sequence after the first successful deliverable: automated referral sequences, hour-bonus upgrade conversations, upsell timing at the Yin/Yang middle.","Sales Algorithm step 12; ACE Expansion; Layer VII step 4","First successful deliverable; positive report","Referral asks; upgrade conversations","SAL-01; SAL-05","Flows AI; Lead Connector (GHL)","Referrals; expansion revenue","Upsell offers above threshold → human","Constant upsell (burns clients)","H","Canon: dept function (expansion)","v5.1 L1640–1650; L2647")
sub("CS-10","Quarterly Immersion Review Agent","CS","Runs the quarterly re-capture: update the client's blueprint and identify the next Fibonacci step.","Client Onboarding step 9; ACE Retention Architecture","Quarter","Updated blueprint; next-step proposal","CS-09; OPS-05","Komodo","Quarterly reviews held","—","Blueprint going stale","H","Canon: retention architecture","v5.1 L1649; L2693")
sub("CS-11","Community & Movement Agent","CS","Builds the client community and social network that create stickiness beyond the product; applies Movement Building so the methodology propagates through all five modes.","Movement Building Algorithm; ACE Expansion (community)","Community calendar; new members","Community programs; engagement","HRC-05; CON-05","—","Active community members","—","Transactional relationships","H","Canon: ACE Expansion (community) + algorithm","v5.1 L1648; L3957–3976")

# 9 CONTENT
lead("CON","CON-00","Content Hub Lead (Propagation owner)","Owns propagation: the libraries and education system that store and transmit the knowledge base.","Five Modes of Propagation; Creative Work","Assets shipped; University usage")
sub("CON-01","IP Creation Agent","CON","Creates new intellectual property (frameworks, products, courses) through the Creative Work Algorithm.","Creative Work Algorithm","Content plan; innovation output","New IP assets","CON-00; MKT-05","—","IP assets shipped","IP publication → G-00","Work below/above density threshold","H","Canon: dept function (IP creation) + algorithm","v5.1 L2978–3001")
sub("CON-02","Media Production Agent (Mode 2 Demonstration)","CON","Produces recordings, case studies and testimonials — results that do the marketing.","Five Modes — Mode 2 Demonstration","Successful client result; recorded session","Videos, case studies, testimonials","MKT-05","Komodo","Proof assets per month","Client consent → human","Promises without proof","H","Canon: dept function (media production)","v5.1 L1306; L1386")
sub("CON-03","Methodology & SOP Documentation Steward (Mode 3)","CON","Keeps the SOP library and methodology documentation complete, current and transferable.","Five Modes — Mode 3 Documentation","New/changed process from O-15","SOP library","CON-08; TEC-02","—","Processes with a current SOP","—","Tribal knowledge","A","Canon: dept function (methodology documentation)","v5.1 L1307; L1386")
sub("CON-04","Brand Standards Agent","CON","Defines and documents brand standards (Third-Kingdom purpose, convergence point, frequency, language/visual/experience encoding) and iterates them with each market interaction.","Brand and Identity Algorithm","Brand review; new touchpoint","Brand standards document","MKT-04; STR-02","—","Touchpoints conforming","Brand changes → G-00","Brand living only in the founder's head","H","Canon: dept function (brand) + algorithm","v5.1 L3405–3422")
sub("CON-05","GFunnel University Curriculum Agent","CON","Builds courses and mentoring material (Mode 1 Direct Teaching at scale) with the Teaching and Mentoring Algorithm.","Teaching and Mentoring Algorithm; Five Modes — Mode 1","Curriculum plan; repeated client questions","Courses, lessons, assessments","HRC-07; CS-11","GFunnel University","Learners completing with artifacts","—","Teaching without learner artifacts","H","Canon: dept function (GFunnel University)","v5.1 L3048–3069; L1386")
sub("CON-06","Writing Agent","CON","Writes long-form, emails, docs and copy: reader, gradient, structure before prose, precise words, subtractive edit, read-aloud test; precise communication.","Writing Algorithm; Domain 6 Linguistic / Communication","Writing request","Drafts and edited copy","Requester; CON-04","—","Edit pass rate","Publication of claims → G-00","Writing that fails through addition","H","Derived placement (Writing)","v5.1 L3004–3023; L3178–3195")
sub("CON-07","Case Study & Proof Library Agent","CON","Maintains the searchable library of proof (results, testimonials, before/after BEAS) for sales and marketing.","What Sustains Propagation — results that speak","New proof asset","Indexed proof library","SAL-05; MKT-05","—","Proof assets per offer tier","—","Proof not findable when needed","A","Canon: sustains-propagation table","v5.1 L1321")
sub("CON-08","Knowledge Base Librarian (Memory & Recall)","CON","Organisational memory: multi-level storage, dense cross-links, spaced review of key knowledge, everything beyond recall horizon documented.","Memory and Recall Algorithm; Layer I.F (civilizational record)","New documentation; quarterly review","Linked knowledge base; review schedule","All agents","—","Knowledge retrieval success","—","Knowledge rediscovered at full cost","A","Derived placement (Memory)","v5.1 L2956–2971")
