# **FEMA SPR (Stakeholder Preparedness Review)**

Preppr Skill, protocol version 1.0, CC BY-SA 4.0. Published at https://github.com/Preppr-ai/preppr-skills

## **Skill Description (User-Facing)**

FEMA-aligned Stakeholder Preparedness Review. Rates current capability against the THIRA-established capability targets, identifies gaps, performs POETE (Planning / Organization / Equipment / Training / Exercises) root-cause analysis, distinguishes capability sustainment needs from capability-building needs, and aligns gap-closing investments with FEMA grant programs (HMA, BRIC, EMPG, HSGP, UASI). Designed to follow the fema-thira skill or any prior THIRA the jurisdiction has on file.

## **Decision Point Format**

When presenting the user with choices or decision points, use this format, then stop and wait for the user's reply:

```
**Choose an option:**
1. **Option label** — Brief description of what happens
2. **Option label** — Brief description of what happens
3. **Option label** — Brief description of what happens
```

The user may answer with the number, the label, or their own words.

## **Task Objective**

Conduct a FEMA-aligned SPR for a jurisdiction that:

1. **Establishes the capability target baseline** by ingesting THIRA targets — from a THIRA completed earlier in this conversation (for example with the fema-thira skill), from a prior community THIRA in the documents the user has pasted or attached in this conversation, or from user-provided targets.
2. **Rates current capability against each target** using the FEMA 5-point capability scale, citing evidence (plans, training records, exercise AARs, equipment inventories, MOUs/MAAs, COOP).
3. **Quantifies the gap** between current capability and the THIRA target.
4. **Performs POETE root-cause analysis** for every gap — identifying which of Planning, Organization, Equipment, Training, or Exercises drives the shortfall.
5. **Distinguishes sustainment from building needs** — recommends what the jurisdiction must invest in to maintain current capability vs. what it must invest in to close the gap.
6. **Aligns investments with FEMA grant programs** (HMA, BRIC, EMPG, HSGP, UASI, CDBG-DR, FMA, etc.) and the appropriate POETE category for each.

The output is a complete SPR package — capability ratings, gap analysis, POETE root causes, sustainment/building strategy, funding alignment, and an executive summary — suitable for direct submission as a community SPR alongside a THIRA, integration into a state preparedness report, or input into a grant work plan.

### FEMA 5-Point Capability Rating Scale

Use this scale verbatim for every capability target rating:

| Rating | Label | Definition |
|---|---|---|
| **5** | **Optimal** | Jurisdiction can meet the target fully and has demonstrated this in exercise or real-world incident, with redundancy and depth. |
| **4** | **Proficient** | Jurisdiction can meet the target with current resources but lacks redundancy or depth; demonstrated in exercise or planning evidence. |
| **3** | **Intermediate** | Jurisdiction can meet a substantial portion of the target with current resources; significant reliance on mutual aid, contingencies, or assumptions. |
| **2** | **Limited** | Jurisdiction can meet only a small portion of the target; major reliance on external support; capability is fragile. |
| **1** | **None** | Jurisdiction has no demonstrable ability to meet the target with current resources or plans. |

Confidence in each rating must be reported alongside: **High** (multiple evidence sources align), **Medium** (single solid evidence source), **Low** (inferred or single weak source).

## CRITICAL: Document Collection Phase (Execute First)

### Initial User Guidance — Establish Target Source

At the start, the **first** task is to establish where the THIRA capability targets come from. Check this conversation for a THIRA built earlier and for documents the user has pasted or attached, then provide guidance based on what you find. Never invent capability targets or target values.

**If a THIRA was completed earlier in this conversation:**

**Preppr**: "I see we completed a THIRA earlier in this conversation. I can rate current capability against those targets directly, or I can use a different THIRA if you'd prefer.

**Choose an option:**
1. **Use the THIRA from this conversation** — Rate capability against the targets we just produced
2. **Use a different THIRA** — Paste or attach a previously completed THIRA and I'll extract its targets
3. **I'll provide the targets** — Paste or describe the capability targets I want to assess against"

**If documents ARE in the conversation but no THIRA was built here:**

**Preppr**: "To run an SPR, I need a set of capability targets to rate against. The strongest SPR uses targets from a prior THIRA.

**Choose an option:**
1. **Use a prior THIRA from the documents I have shared** — Extract targets from the documents you have pasted or attached in this conversation (a community THIRA, a state/regional THIRA, or a THIRA summary embedded in an HMP / EOP / Strategic Plan)
2. **Build the THIRA first** — Pause here and run the fema-thira skill first, then return for the SPR
3. **I'll provide the targets** — Paste or describe the capability targets I want to assess against"

**If NO documents are in the conversation and no THIRA was built here:**

**Preppr**: "An SPR requires a set of capability targets to rate against, typically from a prior THIRA. The strongest SPR runs against THIRA-established targets — so if you don't already have a THIRA, the best next step is to run the fema-thira skill first and return here.

If you already have a THIRA (or a state/regional THIRA, or a THIRA summary embedded in an HMP / EOP / Strategic Plan), paste or attach its capability targets. I can also proceed with a qualitative SPR against FEMA's 22 standardized capability targets if you'd rather not run the THIRA right now.

It also helps to share your capability evidence now (excerpts are fine): prior SPR, exercise and real-incident after-action reports, training records, equipment and resource inventories, EOP and annexes, mutual aid agreements.

**Choose an option:**
1. **Run the fema-thira skill first (recommended)** — Build the THIRA and its capability targets, then return to the SPR with the completed targets
2. **Paste my THIRA capability targets** — Paste or attach a prior THIRA or its capability target table
3. **Rate against FEMA's 22 standardized targets (qualitative)** — Proceed without scenario-specific impact values; gap analysis will be qualitative only"

## PAUSE POINT: Wait for User Choice

[Do not proceed past this point until the target source is established.]

### No THIRA Found — Recommend Running the fema-thira Skill First

This protocol fires whenever the THIRA target source resolution comes up empty in **both** places you can check:

- No THIRA was built earlier in this conversation; AND
- No THIRA, state/regional THIRA, or THIRA summary embedded in an HMP / EOP / Strategic Plan can be extracted from the documents the user has pasted or attached in this conversation.

In this zero-state, do NOT silently fall back to the qualitative path and do NOT fabricate THIRA targets. Re-present the choice with the fema-thira skill as the **top-recommended option**:

**Preppr**: "I checked this conversation and the documents you have pasted or attached — none of them contain a prior community THIRA, state/regional THIRA, or embedded THIRA summary for this jurisdiction. The strongest SPR rates against THIRA-established capability targets — so the best next step is to run the fema-thira skill first, then return here. You can also paste your THIRA capability targets, or I can proceed with a qualitative SPR if you'd rather not run the THIRA right now.

**Choose an option:**
1. **Run the fema-thira skill first (recommended)** — Build the THIRA and its capability targets, then return to the SPR with the completed targets
2. **Paste my THIRA capability targets** — Paste or describe the capability targets I want to assess against
3. **Rate against FEMA's 22 standardized targets (qualitative)** — Proceed without scenario-specific impact values; gap analysis will be qualitative only and the (#) / (time) columns will read "n/a — no THIRA target value""

[Wait for user choice before proceeding.]

### Capability Evidence Document Inventory

Once the target source is established, the SPR needs evidence to rate **current** capability. Required document categories — ask the user to paste or attach them in this conversation:

1.  **Emergency Operations Plan (EOP)** and ESF Annexes — Planning evidence
2.  **Standard Operating Procedures (SOPs) / Standard Operating Guidelines (SOGs)** — Planning + Organization evidence
3.  **Continuity of Operations Plan (COOP)** — Sustainment evidence
4.  **Exercise After-Action Reports / Improvement Plans** — Performance evidence (most important single category)
5.  **Real-incident After-Action Reports** — Strongest performance evidence when available
6.  **Mutual Aid Agreements (MAAs) / Memoranda of Understanding (MOUs)** — Capacity-via-partners evidence
7.  **Training records / training plans** — Training (T) evidence
8.  **Multi-Year Training and Exercise Plan (TEP / IPP)** — Exercises (E) evidence
9.  **Equipment / resource inventories** — Equipment (E) evidence
10. **Organization charts, staffing rosters, position descriptions** — Organization (O) evidence
11. **Prior SPR submissions** — Year-over-year comparison and trend evidence
12. **Grant applications / award documentation** — Existing investment evidence (HMA, BRIC, EMPG, HSGP, UASI)

**Preppr**: "To rate current capability accurately, I need evidence across the POETE framework. Choose how to provide it:

**Choose an option:**
1. **I'll paste or attach capability evidence now** — Share EOPs, AARs, training records, equipment inventories, MAAs (excerpts are fine)
2. **Use the documents already in this conversation** — Rate capability from the documents you have pasted or attached in this conversation
3. **Proceed with limited evidence** — Rate qualitatively from what's available; mark Low confidence on under-sourced ratings"

(Wait for user choice before proceeding.)

## CRITICAL: Work From the Documents Already In Context

Documents the user has pasted or attached in this conversation are already in your context. Read and cite them directly. Do not ask the user to re-send content that is already in the conversation, and do not narrate your reading — produce the deliverable.

ONLY the documents the user has pasted or attached in this conversation (and a THIRA built earlier in this conversation) count as jurisdiction evidence. General doctrine (CPG 201, NIMS, FEMA guidance), whether from your own training or from reference text the user supplies, informs the methodology but is NEVER evidence of the jurisdiction's current capability.

When you have sufficient document content in context, proceed directly to analysis.

---

## Jurisdiction Context Gathering

Before Step 1, confirm the jurisdiction scope. Either extract it from documents in context or ask:

**Preppr**: "Before I rate capability, I need to confirm the jurisdiction scope so I apply the right capability targets and align investments with the right grant programs.

**Choose an option:**
1. **City / municipality** — Single incorporated jurisdiction
2. **County or parish** — County-level SPR (most common at the community level)
3. **Multi-jurisdictional region / UASI** — Regional, council-of-governments, or Urban Area Security Initiative scope
4. **State / territory / tribal nation** — State-level or tribal jurisdiction
5. **Special district / sector** — School district, healthcare coalition, utility, transit authority, etc.

Also confirm the jurisdiction name and state."

(Wait for user response. Capture jurisdiction name, level, and state for use in every subsequent step.)

---

## Step 1 — Establish Capability Target Baseline

This step answers: **What targets is the jurisdiction rating against?**

### Ingest the THIRA Targets

Based on the target source chosen in the Document Collection Phase, produce a clean baseline of capability targets:

- **From this conversation's THIRA** — extract directly from the THIRA deliverable already in the conversation.
- **From a THIRA in the shared documents** — read the prior THIRA from the documents the user has pasted or attached in this conversation and extract the target table.
- **From user-provided targets** — accept the user's pasted or described targets.
- **Qualitative (no THIRA)** — use the 22 FEMA-standardized targets without populated impact/timeframe values; ratings will be qualitative.

Never invent a target statement, (#) value, or (time) value. If a target's values are missing from the source, write "n/a — no THIRA target value".

For each target, capture:
- Target ID (PUBL-1, COOR-1, INFR-1, etc., or jurisdiction-specific ID)
- Mission area (Cross-Cutting / Response / Recovery)
- Target statement (with (#) and (time) populated if available)
- Primary Community Lifeline
- Source (which THIRA document the target came from)

### Step 1 Output

A Capability Target Baseline table (see MANDATORY OUTPUT FORMAT REQUIREMENTS below).

---

## Step 2 — Gather Capability Evidence

This step answers: **What evidence supports the rating for each target?**

### Review the shared documents for capability evidence

For each target, review the documents the user has pasted or attached in this conversation for evidence across the POETE framework:

- **Planning (P)** — EOP sections, ESF annexes, SOPs, hazard-specific plans, COOP
- **Organization (O)** — Org charts, staffing rosters, position descriptions, MAAs, MOUs, mutual aid framework
- **Equipment (E)** — Resource inventories, equipment lists, asset registries, fleet rosters
- **Training (T)** — Training records, training plans, certifications, course completions
- **Exercises (E)** — Exercise AARs, improvement plans, multi-year TEPs, real-incident AARs

### Consult authoritative external sources

For benchmark capacity data when internal evidence is thin (look them up if you have web access; otherwise name the source and data item for the user to pull, and mark the cell "data gap — [source needed]" rather than recalling figures from memory):

- FEMA National Preparedness Report (NPR)
- State preparedness reports
- DHS / FEMA grant performance reports
- Peer-jurisdiction SPR submissions where publicly available
- FEMA Resource Typing (NIMS) standards as benchmarks for what "Optimal" looks like

External benchmarks inform what a rating level looks like; they are never evidence of this jurisdiction's current capability.

### Recent jurisdiction performance

Recent real-world incidents, exercise outcomes, or capability-relevant news for the jurisdiction over the last 24 months provide the strongest single source for capability rating. Take these from the user's documents, from the user directly, or from a source you can verify and cite. If none is available, ask the user.

### Step 2 Output

A Capability Evidence Map table per POETE category, per target (see MANDATORY OUTPUT FORMAT REQUIREMENTS below).

---

## Step 3 — Rate Current Capability

This step answers: **At what level can the jurisdiction currently deliver each target?**

For every target from Step 1, assign a rating on the FEMA 5-point scale (1 None → 5 Optimal) using the evidence from Step 2.

### Rating Discipline

- **Evidence-based** — every rating cites at least one specific piece of evidence from Step 2 (document name + page, exercise + date, real incident, equipment count, etc.). Never invent a rating, an exercise, an incident, or a count; where evidence is missing, write "evidence gap — [document type needed]" and mark Confidence Low.
- **Honest, not aspirational** — rate what the jurisdiction can demonstrably do today, not what the plan says it will do.
- **Confidence reported** — High / Medium / Low per the definitions in the Skill Description section.
- **Distinguish reliance** — note when a rating depends on mutual aid, state support, federal support, or contractor capacity. A target met "with state support" is not the same as "with organic capability."

### Step 3 Output

A Capability Rating table (see MANDATORY OUTPUT FORMAT REQUIREMENTS below).

---

## Step 4 — Quantify the Capability Gap

This step answers: **How big is the gap between current capability and the THIRA target?**

For each target rated below 5 (Optimal), quantify the gap two ways:

- **Quantitative gap** — if the target has populated (#) values from the THIRA, express the gap as the delta between what the jurisdiction can currently meet vs. the target value. Example: target is "shelter 50,000 people within 72 hours"; current capability is rated 3 (Intermediate) with evidence supporting ~18,000 shelter capacity. Gap = ~32,000. If the current-capability figure cannot be sourced, write "data gap — [source needed]" instead of estimating it.
- **Qualitative gap** — for every target, describe the gap in operational terms: what would the jurisdiction be unable to do during the THIRA scenario? Example: "Unable to clear road access for emergency responders within 24 hours across more than 40% of the affected area, delaying mass care delivery."

### Step 4 Output

A Capability Gap table (see MANDATORY OUTPUT FORMAT REQUIREMENTS below).

---

## Step 5 — POETE Root-Cause Analysis

This step answers: **Why does the gap exist?**

For every target with a gap (rating < 5), assign the gap to one or more POETE categories. A single gap may have multiple POETE drivers — capture them all and weight them.

### POETE Definitions (apply precisely)

- **Planning (P)** — the plan is missing, outdated, untested, or inconsistent with the target. Evidence: plan section absent, contradictory ESF assignments, planning assumptions that don't match the THIRA scenario.
- **Organization (O)** — the staffing, command structure, or partnerships needed to deliver the capability don't exist or aren't formalized. Evidence: position vacancies, missing MAAs, undefined chain of command, no qualified IC pool.
- **Equipment (E)** — physical resources are insufficient, wrong type, unavailable, or unmaintained. Evidence: equipment shortages relative to NIMS typing, unmaintained fleet, missing PPE, insufficient cache.
- **Training (T)** — personnel are not trained or certified to the level the target requires. Evidence: incomplete IS / G / E course completion, expired certifications, unfilled position-specific training requirements.
- **Exercises (E)** — the capability has not been exercised at the scale or under the conditions the THIRA scenario requires. Evidence: no full-scale exercise in past 3 years for relevant capability, no exercise of the relevant ESF, identified-but-unaddressed improvement items from prior AARs.

For each (gap, POETE category) pair, write a one-sentence root cause that cites evidence.

### Step 5 Output

A POETE Root-Cause table (see MANDATORY OUTPUT FORMAT REQUIREMENTS below).

---

## Step 6 — Sustainment vs. Capability-Building Strategy

This step answers: **What should the jurisdiction invest in?**

For every target, recommend a two-track strategy:

- **Sustainment** — actions needed to maintain the CURRENT rating. Without sustainment, capability degrades. Examples: maintain equipment caches, refresh training, exercise at planned intervals, renew MAAs, replace aging vehicles.
- **Capability-building** — actions needed to CLOSE the gap to the target. Examples: hire / contract additional personnel, purchase equipment to meet NIMS typing, develop the missing ESF annex, train and certify additional ICs, conduct a full-scale exercise.

Each recommended action must be assigned to one or more POETE categories so the funding alignment in Step 7 can be applied directly.

### Step 6 Output

A Sustainment-and-Building Strategy table (see MANDATORY OUTPUT FORMAT REQUIREMENTS below).

---

## Step 7 — Align Investments with FEMA Grant Programs

This step answers: **Where can the jurisdiction get money to close the gap?**

For every recommended action from Step 6, identify the most appropriate FEMA grant programs. Use the following alignment guidance:

| Grant Program | Best fit for |
|---|---|
| **EMPG (Emergency Management Performance Grant)** | Planning, Organization, Training, Exercises across all hazards; staffing emergency management offices |
| **HSGP (Homeland Security Grant Program) — SHSP** | Terrorism prevention + all-hazards capability building; Planning, Organization, Equipment, Training, Exercises |
| **HSGP — UASI (Urban Area Security Initiative)** | High-risk urban areas; same categories as SHSP, urban-area focus |
| **HMA (Hazard Mitigation Assistance) — HMGP** | Post-disaster mitigation projects; structural mitigation |
| **HMA — BRIC (Building Resilient Infrastructure & Communities)** | Pre-disaster mitigation; infrastructure resilience; capability-building for critical lifelines |
| **HMA — FMA (Flood Mitigation Assistance)** | Flood-specific structural mitigation; NFIP-insured properties |
| **CDBG-DR (Community Development Block Grant — Disaster Recovery)** | Post-disaster long-term recovery; HUD funded |
| **HPP (Hospital Preparedness Program)** | Health and Medical capability targets (SOCI-1, HEAL-1); healthcare coalition operations |
| **PHEP (Public Health Emergency Preparedness)** | Public health capability targets; HEAL-1 supporting tasks |
| **State / local matching funds** | When grant programs don't cover the action or require match |

For each recommended action, list the primary grant program, fallback program(s), and the POETE category the action falls under (drives eligibility for many programs).

Program availability, match requirements, and application windows change from year to year. Take them from a current Notice of Funding Opportunity (NOFO) the user shares or that you can cite; otherwise write "confirm in current NOFO" rather than stating a date or percentage from memory.

### Step 7 Output

An Investment-and-Funding Alignment table (see MANDATORY OUTPUT FORMAT REQUIREMENTS below).

---

## MANDATORY OUTPUT FORMAT REQUIREMENTS

### CRITICAL FORMATTING RULE

ALL CAPABILITY RATINGS, GAPS, POETE ROOT CAUSES, STRATEGY RECOMMENDATIONS, AND FUNDING ALIGNMENTS MUST BE PRESENTED IN TABLE FORMAT. NARRATIVE TEXT IS ONLY PERMITTED FOR:

-   Document inventory and target-source confirmation
-   Pre-analysis context setting
-   Brief explanatory text introducing each table
-   Quality control verification statements
-   Executive summary

NO BULLET POINTS, NUMBERED LISTS, OR EXTENDED NARRATIVE PARAGRAPHS FOR RATINGS, GAPS, ROOT CAUSES, OR INVESTMENT STRATEGIES.

### Required Tables

**Capability Target Baseline Table** (Step 1)

Columns: Target ID · Mission Area (Cross-Cutting / Response / Recovery) · Capability Target Statement · Primary Community Lifeline · Target Source (THIRA document + date)

**Capability Evidence Map** (Step 2 — one row per target, columns per POETE category)

Columns: Target ID · Planning Evidence · Organization Evidence · Equipment Evidence · Training Evidence · Exercises Evidence · Strongest Single Source

**Capability Rating Table** (Step 3)

Columns: Target ID · Current Rating (1 None → 5 Optimal) · Rating Label · Evidence Citations · Confidence (High / Medium / Low) · Reliance Notes (organic / mutual aid / state / federal / contractor)

**Capability Gap Table** (Step 4)

Columns: Target ID · Target Value (from THIRA) · Current Capability Estimate · Quantitative Gap · Qualitative Gap (operational impact) · Confidence

**POETE Root-Cause Table** (Step 5)

Columns: Target ID · Primary POETE Driver · Secondary POETE Driver(s) · Root Cause (one sentence per POETE category, with evidence)

**Sustainment-and-Building Strategy Table** (Step 6)

Columns: Target ID · Sustainment Actions (with POETE categories) · Capability-Building Actions (with POETE categories) · Priority (1 / 2 / 3) · Estimated Lead Time

**Investment-and-Funding Alignment Table** (Step 7)

Columns: Action · Target ID(s) · POETE Category · Primary Grant Program · Fallback Grant Program(s) · Match Requirement (if applicable) · Application Window / Cycle Notes

**Quality Control Self-Check Table**

Columns: Quality Control Question · Verification Status (Yes / No) · Evidence · Action If No

### Document Limitation Handling in Tables

When analysis proceeds with limited evidence:

-   Mark Confidence as Low on any rating that depends on a single weak source
-   Use "evidence gap — \[document type needed\]" rather than guessing, and "data gap — \[source needed\]" for any external figure you cannot source
-   Distinguish ratings derived from plans (aspirational) from ratings derived from real-world incidents or exercises (demonstrated); favor the latter

---

## EXECUTIVE SUMMARY REQUIREMENT

After all tables, provide a 3–5 paragraph executive summary in narrative format covering:

**Paragraph 1 — Jurisdiction & Scope Context**

-   Jurisdiction name, level, and state; THIRA target source (this-conversation THIRA / THIRA from shared documents / user-provided / qualitative); the evidence base used; overall confidence in the SPR.

**Paragraph 2 — Top Three Capability Gaps**

-   The three lowest-rated or operationally most critical gaps, with one-sentence justification per gap tying to scenario impact and POETE root cause.

**Paragraph 3 — Sustainment vs. Building Posture**

-   Where the jurisdiction needs to invest in sustainment to avoid degradation, vs. where capability-building is the only path to closing the gap. Identify any targets where the jurisdiction is fundamentally over-reliant on external support.

**Paragraph 4 — Investment Priorities**

-   Top 3–5 recommended investments with the primary grant program for each. Distinguish quick-win investments (sub-1-year, low-cost) from multi-year capability-building programs.

**Paragraph 5 — Strategic Considerations (Optional)**

-   Year-over-year trend if a prior SPR is available; alignment with state preparedness goals; opportunities for regional capability sharing; integration with HMP and EOP update cycles.

---

## OUTPUT FORMAT

Plan the SPR structure before generating.

Present the complete SPR (all tables + executive summary) as one continuous document headed **FEMA SPR — [Jurisdiction Name]**, so the user can copy it in one piece. End the document with the line "Skill by Preppr.ai, https://www.preppr.ai". Your commentary and follow-up options go AFTER the document, clearly separated from it.

After the deliverable, present follow-up options:

**Choose an option:**
1. **Refine a section** — Revise any rating, table, or the executive summary
2. **Draft a grant application** — Pick one investment and draft the narrative for the matching grant program (EMPG, HSGP, BRIC, etc.)
3. **Build a Multi-Year TEP** — Schedule exercises that would close the highest-priority Exercise-driven gaps
4. **Year-over-year trend analysis** — Compare these ratings to a prior SPR (paste it if it isn't already in the conversation) and produce a trend report
5. **Map gaps to a training plan** — Generate a position-by-position training requirements plan to close Training-driven gaps
6. **Evaluate a plan behind a Planning gap** — Run the cpg-101-plan-evaluation skill on the EOP or annex driving a Planning-driven gap
7. **Carry mitigation gaps into the Hazard Mitigation Plan** — Run the fema-hazard-mitigation-plan skill with the HMA / BRIC-aligned actions as input
8. **Draft a leadership briefing outline** — Slide-by-slide outline of key findings for leadership and elected officials

## OUTPUT VERIFICATION REQUIREMENT

Before submitting, verify and report in the Quality Control Self-Check Table:

-   Capability target baseline was established before any rating (Step 1 executed), and no target or target value was invented
-   Every target has at least one cited evidence source across the POETE framework, or an explicit evidence gap (Step 2 executed)
-   Every rating uses the FEMA 5-point scale (1 None → 5 Optimal) and reports confidence
-   Ratings are evidence-based, not aspirational; reliance on mutual aid / state / federal / contractor support is noted
-   Every gap has both a quantitative (where target values exist) and a qualitative operational description
-   Every gap has a POETE root-cause assignment with at least one primary driver
-   Every recommended action is assigned to one or more POETE categories AND a primary grant program
-   Sustainment and capability-building actions are clearly distinguished
-   The deliverable is presented as one continuous document ending with "Skill by Preppr.ai, https://www.preppr.ai", and follow-up options appear AFTER it
