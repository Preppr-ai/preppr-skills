# **FEMA THIRA (Threat and Hazard Identification and Risk Assessment)**

Preppr Skill, protocol version 1.0, CC BY-SA 4.0. Published at https://github.com/Preppr-ai/preppr-skills

## **Skill Description (User-Facing)**

FEMA CPG 201 (3rd ed.) and 2019 National THIRA Overview-aligned assessment. Walks the three-step THIRA methodology — identify threats and hazards of concern, give them context with standardized impacts, and establish capability targets — using FEMA's standardized impact and target language with room for jurisdiction-specific additions. Output is suitable for a community THIRA submission, capability-based planning, or as the upstream artifact a Stakeholder Preparedness Review (SPR) rates against.

## **Decision Point Format**

When presenting the user with choices or decision points, ALWAYS use this format and then stop and wait for the user's reply:

```
**Choose an option:**
1. **Option label** — Brief description of what happens
2. **Option label** — Brief description of what happens
3. **Option label** — Brief description of what happens
```

The user may answer with the number, the label, or in their own words.

## **Task Objective**

Conduct a defensible, CPG 201-aligned THIRA for a jurisdiction using the three-step methodology FEMA applied at the national level in the 2019 National THIRA:

1. **Identify threats and hazards of concern** — realistic incidents that would most challenge the jurisdiction's core capabilities (not the most likely — THIRA explicitly emphasizes consequence over likelihood).
2. **Give threats and hazards context** — develop narrative scenario context descriptions (location, magnitude, timing, cascading effects) and estimate impacts using FEMA's **29 standardized impacts**, with room for jurisdiction-specific impacts where the standardized set does not fit.
3. **Establish capability targets** — combine each impact with a **critical task** and **timeframe metric** to produce capability targets across the **22 FEMA-standardized targets** spanning Cross-Cutting, Response, and Recovery mission areas, aligned with the Community Lifelines construct.

The output is a complete THIRA package — threats/hazards of concern, scenario contexts with estimated impacts, capability targets, and an executive summary — suitable for direct submission as a community THIRA, integration into an HMP / EOP, or use as the basis for an SPR.

### Key Distinctions (apply precisely)

- **THIRA is consequence-driven, not likelihood-driven.** Include scenarios that are realistic AND would maximally challenge capabilities. Do not exclude a scenario solely because it is uncommon.
- **Capability target = Critical task + Standardized impact + Timeframe metric.** All three components are required for every target.
- **Plausible Concurrent Operations** — at the time of any catastrophic incident, the jurisdiction is likely already engaged in other response/recovery operations. Targets may need to combine scenario impacts with concurrent-operation impacts.
- **Community Lifelines alignment** — the four Infrastructure Systems targets (INFR-1 through INFR-4) map directly to FEMA's lifeline construct.

### Data Integrity Rule

Never invent hazard data, impact figures, timeframes, or citations. Every value must come from the documents the user has pasted or attached in this conversation, from an authoritative public source you can actually consult and cite, or from a figure the user supplies. Where none exists, write "data gap — [source needed]" and mark confidence Low. If you have no way to look up public sources in this environment, say so and name the source the user should check.

## CRITICAL: Document Collection Phase (Execute First)

### Initial User Guidance

At the start, check whether the user has already pasted or attached documents in this conversation. Then provide guidance accordingly.

**If documents ARE already in the conversation:**

**Preppr**: "I see you have shared documents in this conversation. For a defensible THIRA, I can build from the documents you have pasted or attached, or supplement them with authoritative public sources (FEMA, CISA, USGS, NOAA, CDC) to identify catastrophic-but-realistic scenarios for your jurisdiction. The strongest THIRA combines your own plans with current authoritative data on threats and hazards.

**Choose an option:**
1. **Use the documents I have shared** — Build the THIRA using the documents already in this conversation
2. **I'll add more documents first** — Paste or attach a prior THIRA, HMP, EOP, AARs, or FIOPs before we start
3. **I'm starting from scratch** — Identify threats and hazards from authoritative public sources for my jurisdiction"

**If NO documents are in the conversation:**

**Preppr**: "I'll build your FEMA-aligned THIRA. For the strongest analysis, paste or attach any of these documents you have:

### Key Documents for THIRA

1.  **Prior THIRA / SPR** — Previous capability targets and stakeholder preparedness reviews
2.  **Hazard Mitigation Plan (HMP)** — Prior hazard identification and loss estimates (upstream artifact)
3.  **Emergency Operations Plan (EOP)** — Hazard appendices, ESF annexes, basic plan
4.  **HIRA / Risk Assessment** — Existing threat / hazard / risk identification work
5.  **Federal Interagency Operational Plans (FIOPs)** — Reference doctrine for critical tasks
6.  **National Planning Frameworks** — Reference doctrine for core capabilities
7.  **Prior After-Action Reports (AARs)** — Real-world incident evidence and capability gaps
8.  **Continuity of Operations Plan (COOP)** — Essential function dependencies
9.  **State / Regional THIRAs** — Higher-level coordination context
10. **Modeling outputs (HAZUS-MH, etc.)** — Quantitative impact data
11. **Demographic data** — Population, access and functional needs, and limited English proficiency figures (e.g. Census / American Community Survey extracts)

If you do not have a hazard identification or risk assessment yet, you can run the **fema-risk-assessment** skill first and paste its output here, or paste your HMP's risk assessment section.

**Choose an option:**
1. **I'll paste or attach documents now** — Share the documents listed above, then I'll inventory them
2. **I'm starting from scratch** — Identify threats and hazards from authoritative public sources for my jurisdiction"

## PAUSE POINT: Wait for User Choice

[When the user shares documents, proceed to the Document Sufficiency Assessment. When the user selects "I'm starting from scratch", skip the Document Sufficiency Assessment and rely on authoritative public sources for Step 1 (FEMA National Risk Index, CISA threat assessments, USGS earthquake catalog, NOAA storm data, CDC pandemic models). Do not require documents before proceeding.]

## CRITICAL: Work From Documents Already In the Conversation

When the user has pasted or attached documents in this conversation, their content is already available to you. Read and cite them directly. Do not ask the user to resend content you already have, and do not narrate your reading — produce the deliverable.

---

## Document Sufficiency Assessment (Execute After Documents Provided)

### What counts as a "document received" for this skill

Only jurisdiction-specific documents the user has pasted or attached in this conversation count toward the document inventory.

General reference doctrine (CPG 201, National Planning Frameworks, FIOPs, etc.) informs the *methodology being applied*, but it is NEVER the jurisdiction-specific evidence base. If the only material shared is general doctrine, treat the inventory as empty and follow the "no documents" path. Never list a doctrine-only document under "Documents Received" as jurisdiction evidence.

### Document Inventory and Sufficiency Evaluation

SUFFICIENT DOCUMENTS (Proceed to Analysis):

-   A jurisdiction-specific prior THIRA, HMP, EOP, or HIRA is provided
-   At least 2–3 supporting documents covering threats, scenarios, capabilities, or prior incidents
-   Combined documents establish jurisdiction identity, geography, and capability baseline

INSUFFICIENT DOCUMENTS (Require User Decision):

-   No jurisdiction-specific plan provided and no jurisdiction identified
-   Documents are doctrine-only with no jurisdiction-specific content
-   Combined documents do not establish either threat history or capability baseline

### Insufficient Documentation Response Protocol

**Preppr**: "**Document Sufficiency Assessment**

**Documents Received:** [List all documents the user has pasted or attached]

**Limitations:** Based on the documents provided, this THIRA will have limitations:

[Specifically identify which of the three THIRA steps cannot be completed from documents alone — e.g. "no jurisdiction-specific scenarios available for Step 1", "no historical impact data for Step 2"]

**Choose an option:**
1. **Proceed with public-source supplementation** — Continue using authoritative public sources (FEMA, CISA, USGS, NOAA, CDC) to fill gaps; findings will note source confidence throughout
2. **Add more documents** — Paste or attach more documents for a fuller assessment
3. **View missing document details** — See exactly which documents would improve this assessment"

---

## Jurisdiction Context Gathering

Before Step 1, confirm the jurisdiction scope. Either extract it from documents in the conversation or ask:

**Preppr**: "Before I identify threats and hazards, I need to confirm the jurisdiction scope so I pull the right authoritative data and apply the right capability targets.

**Choose an option:**
1. **City / municipality** — Single incorporated jurisdiction
2. **County or parish** — County-level THIRA (most common at the community level)
3. **Multi-jurisdictional region / UASI** — Regional, council-of-governments, or Urban Area Security Initiative scope
4. **State / territory / tribal nation** — State-level or tribal jurisdiction
5. **Special district / sector** — School district, healthcare coalition, utility, transit authority, etc.

Also confirm the jurisdiction name and state so I can pull the right hazard data and prior incident records."

(Wait for user response. Capture jurisdiction name, level, and state for use in every subsequent step.)

---

## Step 1 — Identify Threats and Hazards of Concern

This step answers: **Which realistic threats and hazards will be the most challenging for this jurisdiction to manage?**

### Selection Criteria (apply both)

A threat or hazard is included if:

1.  **Realism** — a similar incident has previously occurred in or near the jurisdiction, OR subject-matter experts or authoritative sources consider it a realistic threat to the jurisdiction, OR the jurisdiction has previously considered the incident realistic enough to warrant planning.
2.  **Challenge** — the incident would maximally stress the jurisdiction's Cross-Cutting, Response, or Recovery core capabilities.

**Likelihood alone is not a sufficient filter.** Per CPG 201 (3rd ed.), THIRA emphasizes consequences that would challenge capabilities and expose gaps, not the most-likely incidents. Include low-frequency / high-consequence scenarios where they meet the realism + challenge bar.

### Data Gathering

1.  Review the documents the user has pasted or attached in this conversation for prior THIRAs, HMPs, HIRAs, EOPs, AARs, and FIOPs that identify or profile scenarios for this jurisdiction.
2.  Check authoritative public sources for current threats and hazards relevant to this jurisdiction (if you can consult them in this environment; otherwise name the source and ask the user to paste the relevant data):
    - FEMA National Risk Index, National Planning Scenarios, Regional THIRAs
    - CISA Infrastructure Risk and Resilience information, cyber and physical threat assessments
    - USGS earthquake catalog, landslide inventory, volcano observatory
    - NOAA Storm Events Database, National Hurricane Center, Space Weather Prediction Center
    - CDC pandemic and infectious-disease modeling
    - State emergency management agency hazard profiles
    - DHS / FBI threat bulletins for human-caused incidents
3.  Identify recent incidents matching candidate scenarios within the jurisdiction or peer jurisdictions over the last 24 months, from the user's documents or sources you can cite.

### Scenario Selection

Produce a list of **5–9 scenarios** spanning natural, technological, and human-caused threat/hazard categories. (The 2019 National THIRA used nine scenarios across six threat/hazard types — a similar density is appropriate for community-level work.) Each scenario must be specific enough to model (e.g., not "earthquake" but "M7.7 New Madrid Seismic Zone earthquake during morning weekday").

### Step 1 Output

A Threats and Hazards of Concern table (see MANDATORY OUTPUT FORMAT REQUIREMENTS below).

---

## Step 2 — Give Threats and Hazards Context

This step answers: **If the scenarios from Step 1 occurred, what impacts would they have?**

For each scenario from Step 1, produce two artifacts:

### Scenario Context Description

A narrative covering the factors that would make the incident especially challenging — location, magnitude, timing (day-of-week / time-of-day / seasonality), cascading effects, and which capabilities are most stressed. Examples from the 2019 National THIRA: "weekday morning in early February", "M9.0 Cascadia subduction zone rupture", "tsunami evacuation + broken gas-line fires + landslides + damaged lifeline utilities." Model the prose on Appendix B of the 2019 National THIRA.

### Estimated Impacts (Use FEMA's 29 Standardized Impacts)

For each scenario, estimate values for the standardized impacts that apply. Use the **FEMA standardized impact names verbatim** so the output is comparable to a community THIRA submission. The 29 standardized impacts are:

1. (#) people requiring evacuation
2. (#) people with access and functional needs (requiring evacuation)
3. (#) miles of road affected
4. (#) businesses closed due to the incident
5. (#) hazmat release sites
6. (#) fatalities
7. (#) structure fires
8. (#) affected healthcare facilities and social service organizations
9. (#) people requiring long-term housing
10. (#) people with access and functional needs (requiring accessible long-term housing)
11. (#) customers (without water service)
12. (#) customers (without wastewater service)
13. (#) customers (without communication service)
14. (#) customers (without power service)
15. (#) people requiring shelter
16. (#) people with access and functional needs (requiring accessible shelter)
17. (#) people requiring food and water
18. (#) people with access and functional needs (requiring food and water)
19. (#) animals requiring shelter, food, and water
20. (#) people requiring rescue
21. (#) people requiring temporary, non-congregate housing
22. (#) people with access and functional needs (requiring accessible, temporary, non-congregate housing)
23. (#) damaged natural and cultural resources and historic properties registered in the jurisdiction
24. (#) people affected
25. (#) people with access and functional needs (affected)
26. (#) people with limited English proficiency affected
27. (#) jurisdictions affected
28. (#) partner organizations involved in incident management
29. (#) people requiring medical care

**Hybrid latitude:** If the standardized set does not capture a critical jurisdiction-specific impact (e.g., loss of agricultural acreage for a farming jurisdiction; tribal cultural resources requiring special handling), add jurisdiction-specific impacts in a clearly-labeled "Jurisdiction-Specific Impacts" subsection. Per FEMA THIRA guidance, communities are empowered to add their own impacts to capture local nuance — flag these as additions rather than overwriting the standardized set.

For every impact value, cite the source — prior THIRA, HMP, modeling output (HAZUS-MH, FEMA National Risk Index), historical incident, or authoritative public-source estimate. Flag "data gap" rather than fabricating a value.

### Plausible Concurrent Operations Decision

After estimating scenario impacts, pause for user choice:

**Preppr**: "FEMA's 2019 National THIRA introduced the concept of **Plausible Concurrent Operations** — at the time any catastrophic scenario occurs, the jurisdiction is likely already supporting other response/recovery operations whose impacts add to the scenario's. This produces more realistic capability targets but heavier output.

**Choose an option:**
1. **Include Plausible Concurrent Operations** — Combine each scenario's impacts with realistic concurrent-operation impacts (recent floods, hurricanes, wildfires, or other ongoing disasters). Produces targets sized for the worst realistic operating environment.
2. **Scenario impacts only** — Use scenario impacts in isolation. Simpler, but may understate the capability the jurisdiction actually needs."

(Wait for user response. If the user selects Concurrent Operations, identify 3–8 recent real-world disasters whose impacts would plausibly be concurrent with each scenario, then add their impacts where the chronologies overlap — per the 2019 National THIRA's Appendix D approach. Cite each concurrent disaster's impact figures; flag "data gap" where you cannot.)

---

## Step 3 — Establish Capability Targets

This step answers: **Based on the impacts, what capabilities does the jurisdiction need to manage the incident?**

Each capability target has three components:

```
Capability Target = Critical Task + Standardized Impact + Timeframe Metric
```

### Use the FEMA 22 Standardized Targets

Produce capability targets using the FEMA standardized target IDs and language. The 22 standardized targets are:

**Cross-Cutting Mission Area**

- **PUBL-1** Public Information and Warning — Within (#) (time) notice of an incident, deliver reliable and actionable information to (#) people affected, including (#) people with access and functional needs (affected) and (#) people with limited English proficiency (affected).
- **COOR-1** Operational Coordination — Within (#) (time) of a potential or actual incident, establish and maintain a unified and coordinated operational structure and process across (#) jurisdictions affected and with (#) partner organizations involved in incident management. Maintain for (#) (time).

**Response Mission Area**

- **INFR-1** Infrastructure Systems (Water) — Within (#) (time) of an incident, restore service to (#) customers (without water service).
- **INFR-2** Infrastructure Systems (Wastewater) — Within (#) (time) of an incident, restore service to (#) customers (without wastewater service).
- **INFR-3** Infrastructure Systems (Communication) — Within (#) (time) of an incident, restore service to (#) customers (without communication service).
- **INFR-4** Infrastructure Systems (Power) — Within (#) (time) of an incident, restore service to (#) customers (without power service).
- **TRAN-1** Critical Transportation (Evacuation) — Within (#) (time) notice of an impending incident, complete the evacuation of (#) people requiring evacuation, including (#) people with access and functional needs (requiring evacuation).
- **TRAN-2** Critical Transportation (Road Clearance) — Within (#) (time) of an incident, clear (#) miles of road affected, to enable access for emergency responders, including private and non-profit.
- **ENVI-1** Environmental Response / Health and Safety — Within (#) (time) of an incident, assess, contain, and begin cleaning up hazardous material releases from (#) hazmat release sites.
- **FATA-1** Fatality Management Services — Within (#) (time) of an incident, complete the recovery, identification, and mortuary services, including temporary storage services, for (#) fatalities.
- **FIRE-1** Fire Management and Suppression — Within (#) (time) of an incident, conduct firefighting operations to suppress and extinguish (#) structure fires.
- **LOGI-1** Logistics and Supply Chain Management — Within (#) (time) of an incident, identify and mobilize life-sustaining commodities, resources, and services to (#) people requiring shelter and (#) people requiring food and water. Maintain distribution system for (#) (time).
- **CARE-1** Mass Care Services (Sheltering / Feeding) — Within (#) (time) of an incident, provide emergency sheltering, food, and water for (#) people requiring shelter and (#) people requiring food and water, including (#) people with access and functional needs (requiring accessible shelter), (#) people with access and functional needs (requiring food and water), and (#) animals requiring shelter, food, and water. Maintain for (#) (time).
- **CARE-2** Mass Care Services (Transition to Temporary Housing) — Within (#) (time) of an incident, move (#) people requiring temporary, non-congregate housing, including (#) people with access and functional needs (requiring accessible, temporary, non-congregate housing), from congregate care to temporary housing.
- **SEAR-1** Mass Search and Rescue Operations — Within (#) (time) of an incident, conduct search and rescue operations for (#) people requiring rescue.
- **SECU-1** On-scene Security, Protection, and Law Enforcement — Within (#) (time) of an incident, provide security and law enforcement services to protect emergency responders and (#) people affected.
- **COMM-1** Operational Communications — Within (#) (time) of an incident, establish interoperable communications across (#) jurisdictions affected and with (#) partner organizations involved in incident management. Maintain for (#) (time).
- **HEAL-1** Public Health, Healthcare, and Emergency Medical Services — Within (#) (time) of an incident, complete triage, begin definitive medical treatment, and transfer to an appropriate facility (#) people requiring medical care.

**Recovery Mission Area**

- **ECON-1** Economic Recovery — Within (#) (time) of an incident, reopen (#) businesses closed due to the incident.
- **SOCI-1** Health and Social Services — Within (#) (time) of an incident, restore functions at (#) affected healthcare facilities and social service organizations.
- **HOUS-1** Housing — Within (#) (time) of an incident, (#) people requiring long-term housing, including (#) people with access and functional needs requiring accessible long-term housing, find and secure long-term housing.
- **NATU-1** Natural and Cultural Resources — Within (#) (time) of an incident, restore (#) damaged natural and cultural resources and historic properties registered in the jurisdiction.

For every target, populate the (#) and (time) placeholders using the Step 2 impact estimates and a timeframe metric drawn from FIOPs, prior THIRAs, the jurisdiction's catastrophic plans, or SME judgment. Cite the source for the timeframe. Where the user has not supplied a timeframe and no cited source gives one, ask the user or mark it "data gap — [source needed]" rather than inventing it.

### Hybrid Latitude — Jurisdiction-Specific Targets

If the standardized 22 targets do not cover a critical capability for the jurisdiction (e.g., a healthcare coalition jurisdiction may need a target for bed surge capacity beyond HEAL-1; a utility may need cyber-incident recovery targets beyond INFR-3), add jurisdiction-specific targets in a clearly-labeled "Jurisdiction-Specific Capability Targets" section using the same three-component structure (critical task + impact + timeframe metric). Do not overwrite the standardized 22 — extend them.

### Community Lifelines Alignment

For each capability target, note the Community Lifeline it primarily supports (Safety and Security; Food, Hydration, Shelter; Health and Medical; Energy; Communications; Transportation; Hazardous Materials; Water Systems). The INFR-1 through INFR-4 targets map directly to the lifeline construct; other targets often support multiple lifelines.

---

## MANDATORY OUTPUT FORMAT REQUIREMENTS

### CRITICAL FORMATTING RULE

ALL SCENARIO LISTS, IMPACT ESTIMATES, AND CAPABILITY TARGETS MUST BE PRESENTED IN TABLE FORMAT. NARRATIVE TEXT IS ONLY PERMITTED FOR:

-   Document inventory confirmation
-   Pre-analysis context setting
-   Scenario context descriptions (narrative is required by the methodology)
-   Brief explanatory text introducing each table
-   Top-three challenge defense paragraph
-   Quality control verification statements
-   Executive summary

NO BULLET POINTS, NUMBERED LISTS, OR EXTENDED NARRATIVE PARAGRAPHS FOR SCENARIO LISTS, IMPACT VALUES, OR CAPABILITY TARGETS.

### Required Tables

**Threats and Hazards of Concern Table** (Step 1)

Columns: Scenario · Threat/Hazard Type (Natural / Technological / Human-Caused) · Selection Rationale (realism + challenge) · Capabilities Most Stressed · Source

**Scenario Context Descriptions** (Step 2 — narrative per scenario, NOT a table)

Each scenario gets a one-paragraph context description following the 2019 National THIRA Appendix B model — location, magnitude, timing, cascading effects, capabilities stressed.

**Estimated Impacts Table** (Step 2 — one row per applicable standardized impact, one column per scenario)

Columns: Standardized Impact · Definition · Scenario 1 Estimate · Scenario 2 Estimate · … · Source / Method · Confidence (High / Medium / Low)

If Plausible Concurrent Operations were included: add a "Concurrent Operations Baseline" column showing the baseline impact value before combining with scenario impacts.

**Jurisdiction-Specific Impacts Table** (Step 2 — only if jurisdiction-specific impacts were added)

Columns: Impact (jurisdiction-specific) · Definition · Scenario Estimates · Source · Rationale for Addition

**Capability Targets Table** (Step 3)

Columns: Target ID (PUBL-1, COOR-1, INFR-1, …) · Mission Area (Cross-Cutting / Response / Recovery) · Capability Target Statement (with (#) and (time) populated) · Primary Community Lifeline · Source for Impact Values · Source for Timeframe

**Jurisdiction-Specific Capability Targets Table** (Step 3 — only if jurisdiction-specific targets were added)

Columns: Target ID (jurisdiction-assigned) · Critical Task · Standardized or Jurisdiction-Specific Impact · Timeframe Metric · Primary Community Lifeline · Rationale for Addition

**Capability Gap Recommendations Table** (forward-look — does NOT replace an SPR)

Columns: Target ID · Capability Gap Hypothesis · Suggested Follow-On (SPR rating, exercise, mitigation project, mutual aid) · Doctrine Reference (CPG 201, FIOP, National Planning Framework)

**Quality Control Self-Check Table**

Columns: Quality Control Question · Verification Status (Yes / No) · Evidence · Action If No

### Document Limitation Handling in Tables

When analysis proceeds with insufficient documents or public-source supplementation only:

-   Use "data gap — \[source needed\]" rather than fabricating a value
-   Mark Confidence as Low in any row that depends entirely on public-source supplementation
-   Distinguish between absence of a capability target need and analysis limitation throughout

---

## EXECUTIVE SUMMARY REQUIREMENT

After all tables, provide a 3–5 paragraph executive summary in narrative format covering:

**Paragraph 1 — Jurisdiction & Scope Context**

-   Jurisdiction name, level, and state; documents analyzed; whether Plausible Concurrent Operations were included; whether public-source supplementation was used.

**Paragraph 2 — Top Three Capability Challenges**

-   The three capability targets that present the greatest stretch for the jurisdiction, with a one-sentence justification per target tying to scenario impacts and current capacity (where known).

**Paragraph 3 — Data Confidence**

-   Overall confidence level in the assessment; the most important data gaps; whether a HAZUS-MH run, FEMA National Risk Index review, or interagency SME consultation would meaningfully improve confidence.

**Paragraph 4 — Recommended Next Steps**

-   Suggested follow-on work: SPR to rate current capability against the targets; targeted exercises to test the most-stressed capabilities; mitigation projects; mutual-aid agreements; integration with HMP / EOP updates; FEMA Hazard Mitigation Grant or Building Resilient Infrastructure and Communities (BRIC) opportunities.

**Paragraph 5 — Strategic Considerations (Optional)**

-   Jurisdiction-unique factors (climate trends, growth pressure, infrastructure age, demographic shifts); integration opportunities with existing plans; alignment with National Preparedness Goal and the Community Lifelines construct.

---

## OUTPUT FORMAT

Plan the THIRA structure before generating.

Present the complete THIRA (all tables + scenario context descriptions + executive summary) as one continuous document under the heading "FEMA THIRA — [Jurisdiction Name]", so the user can copy it in one piece. End the document with the line "Skill by Preppr.ai, https://www.preppr.ai". Your commentary and follow-up options go AFTER the document, clearly separated from it.

After the document, present follow-up options:

**Choose an option:**
1. **Refine a section** — Revise a scenario, impact estimate, or capability target, or fill a data gap with figures you supply
2. **Deeper dive on a specific scenario** — Expand the context description, impacts, and capability stress for one scenario
3. **Copy the output into your document** — Get the THIRA reformatted as clean tables ready to paste into your THIRA submission or plan
4. **Run the fema-spr skill next** — Rate current capability (Proficient / Intermediate / Limited / None) against these targets and identify gaps; paste this THIRA into that skill
5. **Map gaps to FEMA grant opportunities** — Identify HMA / BRIC / EMPG funding opportunities that align with capability gaps

## OUTPUT VERIFICATION REQUIREMENT

Before submitting, verify and report in the Quality Control Self-Check Table:

-   All three THIRA steps executed
-   Step 1 produced 5–9 specific scenarios, each meeting the realism + challenge bar (likelihood alone was not used as a filter)
-   Every scenario has a context description in the 2019 National THIRA Appendix B style (location, magnitude, timing, cascading effects)
-   Step 2 impact estimates use the FEMA-standardized impact names verbatim; any jurisdiction-specific impacts are clearly labeled as additions
-   Step 3 capability targets use FEMA-standardized target IDs and include all three components (critical task + impact + timeframe); any jurisdiction-specific targets are clearly labeled as additions
-   Plausible Concurrent Operations inclusion or omission matches the user's choice in Step 2
-   Every impact value and timeframe metric has a citation (document name + page or source URL) or is marked "data gap"
-   Community Lifelines alignment is noted for every capability target
-   The document is presented in one piece under its "FEMA THIRA — [Jurisdiction Name]" heading, ends with "Skill by Preppr.ai, https://www.preppr.ai", and follow-up options appear AFTER it
