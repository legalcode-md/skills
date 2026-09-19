---
name: legalcode-matter-triage-workflow
description: Route incoming legal requests to the appropriate resource based on matter type, urgency,
  complexity, and organizational risk. Use when a new legal request arrives, when prioritizing a backlog
  of open matters, or when deciding whether to handle a matter in-house or refer to outside counsel.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Route incoming legal requests to the appropriate resource based on matter type, urgency, complexity, and organizational risk. Use when a new legal request arrives, when prioritizing a backlog of open matters, or when deciding whether to handle a matter in-house or refer to outside counsel. Covers intake classification across all practice areas (contracts, employment, litigation, regulatory, IP, corporate, real estate, finance, tax), urgency scoring with SLA targets (CRITICAL/HIGH/STANDARD/LOW), complexity assessment (ROUTINE/MODERATE/COMPLEX/BET-THE-COMPANY), resource matching (self-service, paralegal, junior counsel, senior counsel, GC, outside counsel, specialist, ALSP), budget routing with authority levels, and escalation protocols for matters crossing risk thresholds. Supports configurable routing rules by business unit, geography, and matter type. Integrates with ticketing and matter management systems. Produces a structured routing recommendation with resource assignment, SLA target, estimated cost, and escalation determination. Jurisdiction-agnostic with localization markers. Related: legalcode-client-intake-workflow, legalcode-conflict-check, legalcode-contract-review.


# Legalcode Matter Triage Workflow

> **Disclaimer**: This skill provides a framework for AI-assisted legal matter triage and
> routing. It does not constitute legal advice. All triage outputs should be reviewed by a
> qualified legal professional before a matter is assigned, escalated, or declined. Professional
> responsibility rules, regulatory requirements, and organizational authority levels change;
> verify current applicability before relying on any threshold or protocol described here.
> Statutory and regulatory references cited from memory carry hallucination risk — verify
> against authoritative sources before relying on them.

## Purpose and Scope

This skill routes incoming legal requests to the appropriate resource — from self-service
template libraries through in-house counsel tiers to outside counsel and crisis teams — based
on a structured assessment of matter type, urgency, complexity, and organizational risk.

**Covers:**

- Intake classification across 12 practice area categories with subcategories
- Urgency scoring (CRITICAL / HIGH / STANDARD / LOW) with SLA targets
- Complexity assessment (ROUTINE / MODERATE / COMPLEX / BET-THE-COMPANY) with weighted scoring
- Risk profiling (financial exposure, reputational risk, regulatory dimension, criminal exposure)
- Resource matching across the full legal service delivery stack
- Budget routing with configurable authority levels
- Auto-escalation triggers for matters crossing defined risk thresholds
- Configurable routing rules by business unit, geography, and matter type
- Integration with matter management systems, CLM platforms, and ticketing tools
- Structured routing recommendation with resource assignment, SLA, cost estimate, and escalation determination

**Does not:**

- Perform conflict of interest checks (see `legalcode-conflict-check`)
- Handle full client intake and onboarding (see `legalcode-client-intake-workflow`)
- Review contract clauses or generate redlines (see `legalcode-contract-review`)
- Replace attorney judgment on matter acceptance, strategy, or escalation decisions
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers

**Related skills:**

- `legalcode-client-intake-workflow` — full client onboarding workflow
- `legalcode-conflict-check` — conflict of interest screening
- `legalcode-contract-review` — clause-by-clause contract analysis

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic. The matter's legal context, the organization's home
jurisdiction, and applicable regulatory frameworks determine which legal requirements apply.

[JURISDICTION-SPECIFIC] When localizing this skill, research and apply:

- **Professional responsibility rules**: Bar rules on matter acceptance, unauthorized practice
  of law, fee arrangements, and conflicts across applicable jurisdictions (ABA Model Rules,
  SRA Handbook, Law Society guidelines, etc.)
- **Regulatory notification obligations**: Mandatory reporting timelines for data breaches,
  anti-money laundering suspicious activity reports, regulatory filings
- **Employment law urgency triggers**: Statute of limitations periods vary significantly by
  jurisdiction and claim type (e.g., EEOC charge filing: 180/300 days in US; UK Employment
  Tribunal: 3 months; EU varies by Member State)
- **Outside counsel qualification requirements**: Some jurisdictions require local admission
  for certain matter types; verify outside counsel authorization before routing
- **Attorney-client privilege scope**: Privilege rules differ between common law and civil
  law systems; in-house counsel privilege varies by jurisdiction (not uniformly recognized
  in EU civil law jurisdictions)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the urgency tier or routing recommendation
- The matter description is too vague to classify accurately
- Multiple practice areas are involved and priority must be established
- Organizational configuration (authority levels, panel firms, routing rules) is unknown
- Risk factors are ambiguous and could change the escalation determination

When you reach a **⟁ CLARIFY** block, ask the user before proceeding — do not silently assume
defaults. Use the harness's structured question tool when one is available:

- **Claude Code / Agent SDK:** invoke the `AskUserQuestion` tool. Limits: 1–4 questions per
  call, 2–4 options each, header ≤ 12 characters. Pass the CLARIFY options as the `options`
  array.
- **OpenAI Codex CLI:** invoke `ask_user_question` (runtime) or, in plan mode,
  `request_user_input`. Pass the CLARIFY options as choices.
- **No structured tool available (other harnesses, CI, headless mode without a `canUseTool`
  callback):** emit the CLARIFY questions as numbered plain text and **stop until the user
  replies**. Do not proceed with assumed answers.

Skip any CLARIFY question the user has already answered in the initial prompt or prior
conversation. When you proceed with partial context, state every assumption explicitly so the
user can correct it.

---

## Workflow

### Step 1: Accept the Matter Request

Accept matter intake information in any of these formats:

- **Structured intake form**: Fields populated via matter management system, CLM portal, or
  dedicated intake form (Streamline AI, Checkbox, LawVu, Jira Service Management, etc.)
- **Unstructured email / message**: Email or Slack/Teams message describing the request
- **Verbal summary**: Description provided by the requestor in conversation
- **Pasted matter details**: Matter description pasted directly into the conversation

**Minimum required information to proceed with triage:**

1. Matter description (what is being requested)
2. Requestor name and business unit
3. Any known deadline or urgency driver
4. Counterparty or adverse party name (if applicable)
5. Contract, transaction, or dispute value (if applicable)

If minimum information is not provided, prompt the requestor for the missing fields before
proceeding. Do not triage on insufficient information — incomplete triage leads to mis-routing.

### Step 2: Gather Context

**⟁ CLARIFY** — Before classifying, gather context. Ask the following if not already provided
in the intake. Present as structured options where applicable:

1. **Practice area**: What type of legal work is this?
   - Options: Contracts & Commercial, Employment & Labor, Litigation & Disputes,
     Regulatory & Compliance, Privacy & Data Protection, Intellectual Property,
     Corporate & Governance, Mergers & Acquisitions, Real Estate, Tax, Finance & Treasury,
     General Advisory
   - _Why this matters_: Practice area drives which attorney pool to route to, which
     regulatory frameworks apply, and what SLA benchmarks are appropriate.

2. **Urgency driver**: What is creating time pressure on this matter?
   - Options: Court/regulatory filing deadline (specify date), Contract execution date,
     Board or executive meeting, Active investigation with response window,
     No hard deadline — general urgency, No urgency — planning horizon
   - _Why this matters_: The urgency tier determines the SLA commitment and whether
     priority resourcing is needed.

3. **Financial exposure**: What is the estimated value at stake?
   - Options: Below $50K, $50K–$500K, $500K–$5M, Above $5M, Unknown / not applicable
   - _Why this matters_: Financial exposure is the primary driver of complexity tier
     and budget authority level required.

4. **Jurisdiction(s)**: Where is the legal activity taking place?
   - Options: Single jurisdiction (specify), Multi-jurisdictional — within one country,
     Multi-jurisdictional — cross-border, Unknown
   - _Why this matters_: Multi-jurisdictional matters require more senior resource allocation
     and may require local counsel in addition to in-house team.

5. **Risk flags**: Are any of these present?
   - Options (multi-select): Regulatory investigation or enforcement action,
     Criminal exposure (individual or corporate), Board or investor notification required,
     Media or reputational risk, Data breach or cybersecurity incident,
     Class action or mass tort threat, None of these apply
   - _Why this matters_: Any of these triggers auto-escalation regardless of other factors.

If the requestor cannot answer all questions, proceed with available information and
**state assumptions explicitly** in the triage recommendation (e.g., "Assuming single
jurisdiction based on requestor's description — re-triage if cross-border elements exist").

### Step 3: Check for Auto-Escalation Triggers

Before proceeding with standard triage, run the **Auto-Escalation Check** against the
Escalation Protocol Triggers section of this skill.

If **any auto-escalation trigger is present**:

- Immediately route to GC / CLO regardless of other factors
- Issue CRITICAL urgency tier override
- Notify GC and CEO/CFO in parallel
- Activate outside counsel standby protocol
- Skip remaining triage steps; go directly to Step 10 (Output)
- Document trigger in the Glass Box audit trail

If no auto-escalation trigger is present, continue to Step 4.

**⟁ CLARIFY** — If you identify a potential auto-escalation trigger but are uncertain
whether it applies, ask:

- "The matter description mentions [X]. Is there an active government investigation /
  criminal exposure / board notification requirement? If so, this matter auto-escalates to
  GC-level regardless of other factors."

### Step 4: Classify Practice Area and Sub-Category

Using the **Matter Type Taxonomy** section of this skill, assign:

1. **Primary practice area** (one of 12 top-level categories)
2. **Sub-category** (specific matter type within the practice area)
3. **Matter type** (one of: Advisory / Transactional / Litigation / Regulatory / Compliance)

**Multi-practice matters**: Where a matter spans multiple practice areas (e.g., M&A with
significant employment, tax, and IP dimensions), designate the primary practice area based
on the dominant legal question, and note secondary practice areas in the triage record.

**⟁ CLARIFY** — If the matter could reasonably be classified in two different practice areas
with different routing implications, present both options:

- "This matter could be classified as [Practice Area A] or [Practice Area B]. [Practice Area A]
  would route to [resource X] with [SLA Y]. [Practice Area B] would route to [resource Z]
  with [SLA W]. Which classification is more accurate?"

### Step 5: Assess Urgency Tier

Apply the **Urgency Scoring Framework** to assign one of four urgency tiers:

| Tier | Label    | Definition                                            | Acknowledgment SLA | Initial Response SLA    |
| ---- | -------- | ----------------------------------------------------- | ------------------ | ----------------------- |
| U1   | CRITICAL | Immediate action required; material harm within hours | Within 30 min      | Within 2 hours          |
| U2   | HIGH     | Action needed within 1-2 business days                | Within 2 hours     | Within 4 business hours |
| U3   | STANDARD | Action needed within 1-2 weeks                        | Same business day  | 1 business day          |
| U4   | LOW      | No urgent deadline; background/planning work          | 2 business days    | 3 business days         |

**SLA override rule**: Court filing deadlines, regulatory response windows, and board
notification requirements auto-override the requester-set urgency tier. Recalculate from
the hard deadline working backwards.

**Urgency inflation prevention**: Require VP-level or above authorization to designate U1
(CRITICAL) urgency. If the requestor designates U1 without a verifiable hard deadline,
flag for confirmation before activating crisis protocols.

**⟁ CLARIFY** — If no urgency driver has been provided:

- "What is the earliest date by which this matter needs initial attention? And is there a
  hard external deadline (court date, regulatory filing, contract execution) or an internal
  target?"

### Step 6: Assess Complexity Tier

Apply the **Complexity Assessment Criteria** to assign one of four complexity tiers and
a weighted complexity score (0–40 scale):

| Tier | Label           | Score Range | Definition                                                                     |
| ---- | --------------- | ----------- | ------------------------------------------------------------------------------ |
| T1   | ROUTINE         | 0–10        | Template-driven, low risk, single jurisdiction, well-precedented               |
| T2   | MODERATE        | 11–20       | Some customization, moderate risk, limited cross-border                        |
| T3   | COMPLEX         | 21–30       | Bespoke, high risk, multi-jurisdictional, significant stakeholder involvement  |
| T4   | BET-THE-COMPANY | 31–40       | Existential risk, criminal/regulatory exposure, board-level decision authority |

Assess each factor on the Complexity Scoring Matrix (see **Complexity Assessment Criteria**
section) and sum the weighted scores to assign the tier.

### Step 7: Build Risk Profile

Build a risk profile across four dimensions:

1. **Financial exposure**:
   - LOW: Deal/dispute value < $50K and no indirect financial exposure
   - MEDIUM: Deal/dispute value $50K–$1M OR significant indirect exposure
   - HIGH: Deal/dispute value $1M–$10M OR material litigation or regulatory fine
   - CRITICAL: Deal/dispute value > $10M OR exposure exceeding insurance limits / going concern risk

2. **Reputational risk**:
   - LOW: Internal matter, no external visibility
   - MEDIUM: External counterparty, limited visibility, no media dimension
   - HIGH: Counterparty with media profile, public company disclosure possible
   - CRITICAL: Active media inquiry, whistleblower, class action, regulatory enforcement with press release

3. **Regulatory risk**:
   - NONE: No regulatory dimension
   - INDIRECT: Regulatory compliance aspect (data privacy clause, AML provision) but no investigation
   - DIRECT: Regulatory inquiry, investigation, or enforcement action

4. **Criminal exposure**:
   - YES / NO / POSSIBLE

Record the risk profile in the triage record. A CRITICAL financial exposure or DIRECT
regulatory risk with any criminal exposure triggers escalation review even if the
complexity tier is T2 or T3.

### Step 8: Match Resource

Using the Risk Profile, Urgency Tier, and Complexity Tier, apply the **Resource Matching
Matrix** to identify the appropriate resource tier:

**Primary routing rule**: Match the most junior resource capable of handling the matter
at the assessed complexity level within the assessed urgency SLA. This preserves senior
capacity for matters that genuinely require it.

**Resource override rules**:

- Financial exposure CRITICAL → minimum Senior Counsel
- Regulatory risk DIRECT → minimum Senior Counsel or Outside Counsel
- Criminal exposure YES → GC + Outside Counsel (specialist)
- Reputational risk CRITICAL → GC notification regardless of assignment

**Capacity check**: Verify current open matter count against the assigned attorney's
workload threshold (typically 85% of defined capacity). If at or above threshold, route
to the next-available attorney in the same resource tier or escalate to the next tier.

**⟁ CLARIFY** — For matters where outside counsel engagement may be appropriate:

- "This matter's complexity / urgency profile suggests outside counsel may be needed.
  Does your organization have a pre-approved panel of outside counsel firms for [practice
  area]? If yes, which panel firm should be engaged? If no, do you have preferred firms?"

**⟁ CLARIFY** — For budget authority:

- "The estimated budget for this matter is [range]. What is your organization's approval
  threshold for outside counsel engagement? Who has authority to approve spend at this level?"

### Step 9: Determine Budget Routing and Authority

Apply the **Budget Routing and Authority Framework** to determine:

1. **Estimated budget**: Low / Medium / High / Major (see framework thresholds)
2. **Authority level required**: Who must authorize spend at this level
3. **Pre-authorization status**: Has outside counsel been pre-authorized on panel?

If outside counsel is recommended and no panel firm exists or no pre-authorization has
been obtained, flag as a routing condition — the matter cannot fully proceed until
counsel is authorized.

For matters above the GC authority threshold, document the board / CLO / CFO co-approval
requirement as a condition on the routing recommendation.

### Step 10: Determine Triage Status

Based on all preceding assessments, assign one of three triage statuses:

| Status     | Definition                                                                                                | Routing Action                                                                                               |
| ---------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **GREEN**  | Proceed to assignment — all triage factors within normal parameters                                       | Assign immediately to recommended resource; SLA clock starts                                                 |
| **YELLOW** | Proceed with conditions — one or more conditions must be satisfied before substantive work begins         | Assign to recommended resource; document conditions; work begins on conditions before substantive engagement |
| **RED**    | Escalate immediately — auto-escalation trigger present, or matter requires authority above normal routing | Escalate to GC/CLO; do not assign to normal resource pool; activate escalation protocol                      |

**GREEN requires ALL of the following:**

- No auto-escalation trigger identified
- Urgency tier assigned and SLA feasible with available resources
- Complexity tier assessed and appropriate resource identified
- Financial exposure within authority level of recommended resource
- No outstanding conditions (budget approval, conflict check, outside counsel authorization)

**YELLOW requires ANY of the following:**

- Urgency U1 or U2 but resource not yet confirmed available
- Budget approval needed before outside counsel engagement
- Conflict check not yet completed
- Insufficient information to confirm complexity — re-triage pending additional facts
- Outside counsel panel engagement requires additional authorization
- Matter spans BU/geographies requiring cross-team coordination

**RED requires ANY of the following:**

- Any auto-escalation trigger (see Step 3 and Escalation Protocol Triggers section)
- Criminal exposure identified (individual or corporate)
- Financial exposure CRITICAL and matter value exceeds GC unilateral authority
- Regulatory enforcement action with imminent response deadline
- Board or public company disclosure obligation triggered
- Reputational risk CRITICAL with active media inquiry

### Step 11: Quality Verification

Apply the PLAN-DO-CHECK-ACT quality cycle before delivering the triage recommendation:

**PLAN**: Confirm the assessed urgency tier, complexity tier, and risk profile are internally
consistent. A ROUTINE complexity matter with CRITICAL financial exposure is a contradiction
— re-assess before proceeding.

**DO**: Confirm all triage steps were executed. Verify no auto-escalation trigger was
missed. Verify the resource match reflects current capacity.

**CHECK**: Run the Citation Quality Gates on any regulatory or statutory references
included in the triage record. Run the Confidence Scoring check on the final triage
status.

**ACT**: Document any exceptions, assumptions, or conditions in the Glass Box audit trail.
If confidence is POSSIBLE (0.40–0.59) or lower, escalate rather than assign.

For any **RED** triage status, run the Self-Interrogation 3-pass review:

- **Pass 1 (Legal Chain Integrity)**: Does the escalation classification follow logically
  from the facts presented? Would a GC actually need to be involved immediately?
- **Pass 2 (Completeness)**: Have all risk dimensions been assessed? Is there a regulatory
  dimension that has not been surfaced?
- **Pass 3 (Challenge)**: What is the strongest argument that this matter does NOT need
  immediate escalation? Under what circumstances might it be handled at a lower tier?

### Step 12: Deliver Routing Recommendation

Generate the structured **Matter Triage Recommendation** output using the **Output Format
Template** at the end of this skill.

Deliver the recommendation to:

- The requestor (acknowledgment + triage result)
- The assigned attorney or team (matter details + context)
- Legal operations / matter management system (structured record for tracking)
- GC / supervisor (for YELLOW and RED matters)

Where the triage recommendation identifies conditions (YELLOW), ensure conditions are
tracked and re-triage is triggered when conditions are satisfied.

---

## Matter Type Taxonomy

### 1. Contracts & Commercial

| Sub-Category               | Examples                                  | Matter Type   |
| -------------------------- | ----------------------------------------- | ------------- |
| Commercial agreements      | Sales, procurement, vendor, supply chain  | Transactional |
| SaaS / technology          | Software licensing, API, cloud services   | Transactional |
| NDAs / confidentiality     | Mutual, unilateral, employee, third-party | Transactional |
| Distribution & channel     | Reseller, distributor, channel partner    | Transactional |
| MSA / SOW                  | Master services, statements of work       | Transactional |
| Joint ventures             | JV formation, JV operating                | Transactional |
| Subscription / SaaS review | Standard vendor terms review              | Advisory      |

### 2. Employment & Labor

| Sub-Category             | Examples                                                | Matter Type |
| ------------------------ | ------------------------------------------------------- | ----------- |
| Hiring & onboarding      | Offer letters, employment agreements, background checks | Advisory    |
| Terminations & severance | At-will termination, redundancy, WARN Act               | Advisory    |
| Workplace investigations | Harassment, discrimination, misconduct                  | Compliance  |
| Non-competes & covenants | Non-solicitation, garden leave, IP assignment           | Advisory    |
| Benefits & compensation  | Equity plans, deferred comp, benefits disputes          | Advisory    |
| Labor relations          | Collective bargaining, union matters, strikes           | Regulatory  |
| Wage & hour              | Overtime, classification, FLSA/state law compliance     | Compliance  |
| OSHA & safety            | Workplace safety incidents, OSHA inspections            | Regulatory  |
| Employment litigation    | Discrimination suits, wrongful termination, PAGA        | Litigation  |

### 3. Litigation & Disputes

| Sub-Category               | Examples                                         | Matter Type |
| -------------------------- | ------------------------------------------------ | ----------- |
| Commercial litigation      | Breach of contract, business tort                | Litigation  |
| Employment litigation      | Discrimination, wrongful termination, harassment | Litigation  |
| Class actions & collective | Class certification, FLSA collective action      | Litigation  |
| Arbitration & mediation    | Commercial arbitration, employment mediation     | Litigation  |
| Regulatory enforcement     | Government investigation defense                 | Regulatory  |
| Collections & enforcement  | Debt recovery, judgment enforcement              | Litigation  |
| Subpoenas & discovery      | Third-party subpoena response, preservation      | Litigation  |
| Appeals                    | Appellate briefing, amicus filings               | Litigation  |

### 4. Regulatory & Compliance

| Sub-Category              | Examples                                                  | Matter Type |
| ------------------------- | --------------------------------------------------------- | ----------- |
| Antitrust & competition   | Merger notification, cartel defense, abuse investigations | Regulatory  |
| Export controls           | OFAC, EAR, ITAR, sanctions compliance                     | Compliance  |
| Environmental             | EPA compliance, Superfund, permitting                     | Regulatory  |
| Financial regulatory      | Banking, securities, insurance oversight                  | Regulatory  |
| Healthcare regulatory     | FDA, HIPAA, CMS                                           | Regulatory  |
| Consumer protection       | FTC Act, CFPB, state UDAP                                 | Regulatory  |
| Government investigations | DOJ, FBI, SEC, FTC, CFPB, multi-agency                    | Regulatory  |

### 5. Privacy & Data Protection

| Sub-Category               | Examples                                       | Matter Type   |
| -------------------------- | ---------------------------------------------- | ------------- |
| GDPR compliance            | DPIAs, LIAs, data subject rights               | Compliance    |
| US state privacy           | CCPA/CPRA, CPA, CTDPA, VCDPA                   | Compliance    |
| Data breach response       | Notification obligations, regulatory reporting | Compliance    |
| Data processing agreements | DPAs, SCCs, BCRs, processing records           | Transactional |
| Cookie & consent           | Consent mechanisms, cookie audits              | Compliance    |
| Cross-border transfers     | SCCs, adequacy, derogations                    | Compliance    |

### 6. Intellectual Property

| Sub-Category     | Examples                                         | Matter Type         |
| ---------------- | ------------------------------------------------ | ------------------- |
| Patent           | Prosecution, portfolio management, litigation    | Advisory/Litigation |
| Trademark        | Registration, clearance, opposition, enforcement | Advisory/Litigation |
| Copyright        | Registration, DMCA, licensing                    | Advisory/Litigation |
| Trade secrets    | Misappropriation, non-disclosure, DTSA           | Advisory/Litigation |
| IP licensing     | In-licensing, out-licensing, cross-licensing     | Transactional       |
| Open source      | License compliance, policy review                | Compliance          |
| IP due diligence | M&A IP audit, freedom to operate                 | Advisory            |

### 7. Corporate & Governance

| Sub-Category           | Examples                                                  | Matter Type   |
| ---------------------- | --------------------------------------------------------- | ------------- |
| Board & governance     | Board resolutions, minutes, governance policies           | Advisory      |
| Corporate housekeeping | Subsidiary management, entity maintenance, annual reports | Compliance    |
| Entity transactions    | Formation, dissolution, conversion                        | Transactional |
| Securities issuance    | Equity, cap table, 409A, Section 12                       | Transactional |
| Equity plans           | Stock options, RSUs, ESPP administration                  | Advisory      |
| Proxy & annual meeting | Proxy statement, director nominations                     | Compliance    |

### 8. Mergers & Acquisitions

| Sub-Category               | Examples                                  | Matter Type   |
| -------------------------- | ----------------------------------------- | ------------- |
| M&A due diligence          | Legal DD, data room review                | Advisory      |
| Share/asset purchase       | SPA, APA, schedules                       | Transactional |
| Merger                     | Statutory merger, reorganization          | Transactional |
| Carve-out & divestiture    | Separation agreement, transition services | Transactional |
| Venture & growth financing | VC/PE investment, SAFE, convertible note  | Transactional |
| Post-close integration     | Integration workstreams, earnout disputes | Advisory      |

### 9. Real Estate

| Sub-Category           | Examples                         | Matter Type   |
| ---------------------- | -------------------------------- | ------------- |
| Commercial lease       | Office, retail, industrial lease | Transactional |
| Property acquisition   | Purchase, sale, development      | Transactional |
| Lease amendments       | Extension, expansion, sublease   | Transactional |
| Construction contracts | GC agreements, design-build      | Transactional |
| Land use & zoning      | Permitting, variances, easements | Regulatory    |

### 10. Tax

| Sub-Category      | Examples                             | Matter Type |
| ----------------- | ------------------------------------ | ----------- |
| Transactional tax | M&A structuring, tax efficiency      | Advisory    |
| Transfer pricing  | TP policies, documentation, disputes | Compliance  |
| Tax controversy   | Audits, appeals, tax court           | Litigation  |
| VAT / GST         | Cross-border indirect tax            | Compliance  |

### 11. Finance & Treasury

| Sub-Category          | Examples                                 | Matter Type   |
| --------------------- | ---------------------------------------- | ------------- |
| Loan & credit         | Credit facilities, term loans, revolvers | Transactional |
| Derivatives & hedging | ISDA, hedging agreements                 | Transactional |
| Insurance             | Policy review, coverage disputes         | Advisory      |
| Surety & bonding      | Performance bonds, bid bonds             | Transactional |

### 12. General Advisory

| Sub-Category            | Examples                                       | Matter Type |
| ----------------------- | ---------------------------------------------- | ----------- |
| Ad hoc legal advice     | General legal questions, policy interpretation | Advisory    |
| Policy drafting         | Company policies, procedures, codes of conduct | Compliance  |
| Training                | Legal training requests, education materials   | Advisory    |
| Internal investigations | Non-employment misconduct, fraud               | Compliance  |
| Ethics & conflicts      | Internal ethics inquiries, COI disclosures     | Compliance  |

---

## Urgency Scoring Framework

### Four-Tier Urgency Model

| Tier | Label    | Acknowledgment SLA | Initial Response SLA | Resolution Target  | SLA Clock      |
| ---- | -------- | ------------------ | -------------------- | ------------------ | -------------- |
| U1   | CRITICAL | 30 minutes         | 2 hours              | Same business day  | Calendar time  |
| U2   | HIGH     | 2 hours            | 4 business hours     | 1–2 business days  | Calendar time  |
| U3   | STANDARD | Same business day  | 1 business day       | 5–10 business days | Business hours |
| U4   | LOW      | 2 business days    | 3 business days      | 20+ business days  | Business hours |

### U1 (CRITICAL) Qualifying Conditions

Any one of the following qualifies a matter as CRITICAL:

- Court filing, hearing, or response deadline within 48 hours
- Regulatory response deadline within 72 hours
- Active injunction or TRO application (either side)
- Data breach with notification obligation clock running (GDPR 72-hour rule [VERIFY], US state laws)
- Active government enforcement with imminent preservation obligation
- Board or investor rights trigger requiring same-day response
- Dawn raid or government search and seizure in progress

### U2 (HIGH) Qualifying Conditions

Any one of the following qualifies a matter as HIGH:

- Court or regulatory deadline within 5 business days
- Contract execution needed before an imminent transaction close
- Board meeting within 5 business days requiring legal deliverable
- Active negotiation with counterparty deadline communicated
- Investigation response window expiring within the week
- Employment matter with active escalation (active grievance, EEOC charge pending)

### Urgency Override Rules

- Hard external deadlines always override requestor-set urgency — recalculate from deadline
- U1 designation requires VP-level or above authorization (prevents urgency inflation)
- SLA breaches on U1/U2 matters trigger automatic supervisor notification
- Requestors may set initial urgency; legal team may escalate or de-escalate on triage review

[JURISDICTION-SPECIFIC] Statute of limitations deadlines, notice periods, and regulatory
response windows vary significantly by jurisdiction and claim type. Verify the applicable
period before setting the urgency tier on litigation and regulatory matters.

---

## Complexity Assessment Criteria

### Four-Tier Complexity Model

| Tier | Label           | Score | Characteristics                                                                                               |
| ---- | --------------- | ----- | ------------------------------------------------------------------------------------------------------------- |
| T1   | ROUTINE         | 0–10  | Template-driven; single jurisdiction; no novel question; low financial exposure; pre-approved playbook exists |
| T2   | MODERATE        | 11–20 | Some customization; moderate risk; limited cross-border; research required; multiple stakeholders             |
| T3   | COMPLEX         | 21–30 | Bespoke; high risk; multi-jurisdictional; significant stakeholder involvement; direct regulatory dimension    |
| T4   | BET-THE-COMPANY | 31–40 | Existential risk; criminal exposure; board-level decision authority; systemic regulatory threat               |

### Complexity Scoring Matrix

Score each factor on a 1–5 scale; apply the stated multiplier:

| Factor               | Weight (×) | 1 (Low)         | 3 (Medium)            | 5 (High)             | Max Score |
| -------------------- | ---------- | --------------- | --------------------- | -------------------- | --------- |
| Financial exposure   | ×2         | < $50K          | $50K–$1M              | > $1M                | 10        |
| Criminal exposure    | ×2         | None            | Possible              | Confirmed            | 10        |
| Regulatory dimension | ×2         | None            | Indirect (compliance) | Active investigation | 10        |
| Reputational risk    | ×1.5       | Internal only   | External, limited     | Media/public company | 7.5       |
| Jurisdictional scope | ×1         | Single          | Multi (same country)  | Cross-border         | 5         |
| Novelty              | ×1         | Template exists | Precedent exists      | No precedent         | 5         |
| Stakeholder count    | ×0.5       | 1–2             | 3–5                   | 6+                   | 2.5       |
| Strategic importance | ×1         | Low             | Moderate              | Business-critical    | 5         |

**Maximum score**: 55 (adjusted scale; use 0–40 for tier assignment by proportional mapping)

**Note**: Criminal exposure and regulatory dimension are asymmetric — any confirmed criminal
exposure or active regulatory investigation moves the matter to T4 regardless of aggregate score.

### Complexity vs. Urgency Independence

Complexity and urgency are independent dimensions. **Do not equate them**:

- A routine NDA needed in 2 hours = T1 complexity + U2 urgency
- A complex M&A transaction with a 90-day timeline = T3 complexity + U4 urgency
- A data breach response = T3 complexity + U1 urgency
- Annual policy review = T1 complexity + U4 urgency

Routing must account for both dimensions separately.

---

## Resource Matching Matrix

### Resource Tier Definitions and Routing Criteria

**Tier 0 — Self-Service (No Legal Review)**

- **Profile**: Business user handles with approved template or guidance; no attorney involvement
- **Routing criteria**: T1 complexity; below deal-value threshold (org-configured, default $25K–$50K);
  template exists with no required redlines; no regulatory dimension; requestor authorized
- **Resources**: Template library, CLM self-service portal, FAQ knowledge base, approved playbook
- **Not suitable for**: Any matter with novel facts, regulatory dimension, financial exposure above threshold, or counterparty requesting material changes

**Tier 1 — Paralegal / Legal Operations Specialist**

- **Profile**: Process execution within defined scope; legal judgment not required
- **Routing criteria**: Administrative or procedural tasks; T1 complexity; defined checklist exists
- **Examples**: Subpoena coordination, discovery logistics, entity maintenance, trademark filings,
  contract data extraction, invoice review, matter management system administration
- **Not suitable for**: Matters requiring legal advice, interpretation, or judgment

**Tier 2 — Junior In-House Counsel (0–4 years)**

- **Profile**: Standard commercial work; some negotiation; research required but well-precedented
- **Routing criteria**: T1–T2 complexity; financial exposure < $500K; single jurisdiction preferred;
  no active regulatory investigation; no criminal exposure
- **Examples**: Standard commercial contracts (moderate redlines), routine employment advice,
  compliance monitoring, policy review, vendor contract review, basic IP licensing

**Tier 3 — Senior In-House Counsel (5+ years)**

- **Profile**: Complex commercial work; significant negotiation; multi-jurisdictional; cross-functional
- **Routing criteria**: T2–T3 complexity; financial exposure $500K–$5M; direct regulatory dimension
  permitted; no criminal exposure
- **Examples**: Complex commercial agreements, significant employment matters, regulatory compliance
  strategy, M&A support (non-lead), significant disputes, major IP licensing

**Tier 4 — GC / Deputy GC**

- **Profile**: Strategic decisions; board-level matters; matters with existential or organizational risk
- **Routing criteria**: T3–T4 complexity; financial exposure > $5M; criminal risk possible; board/investor
  notification; cross-company strategic decisions
- **Examples**: Major M&A, significant regulatory enforcement, board governance, CLO-level advocacy,
  matters with cross-functional or public company implications

**Tier 5 — Outside Counsel (General Panel)**

- **Profile**: Litigation management; specialist expertise; capacity overflow; jurisdictions without
  in-house presence; independence required
- **Routing criteria**: Litigation requiring court appearance; niche area without in-house expertise;
  internal capacity exceeded; outside perspective required (regulatory, IP, employment)
- **Engagement trigger**: Authorization from Senior Counsel or above required; panel firm selection per org guidelines

**Tier 6 — Outside Counsel (Specialist / Boutique)**

- **Profile**: Deep niche expertise not available in-house or at general panel firms
- **Routing criteria**: T3–T4 complexity; specific expertise required (patent prosecution, antitrust,
  SEC enforcement, appellate, arbitration)
- **Examples**: IP boutique for patent prosecution; white-collar boutique for SEC enforcement;
  competition specialist for antitrust; appellate specialist for circuit court briefing

**Tier 7 — Outside Counsel (Big Law / AmLaw 50)**

- **Profile**: Bet-the-company stakes; high-profile transactions; major litigation
- **Routing criteria**: T4 complexity; financial exposure > $50M; criminal/regulatory existence risk;
  high-profile transaction with market significance; hostile takeover defense
- **Engagement trigger**: GC + CFO (and often Board) authorization required

**Tier 8 — Alternative Legal Service Provider (ALSP)**

- **Profile**: High-volume, commoditized work requiring scale rather than judgment
- **Routing criteria**: Volume exceeds team capacity; work is process-intensive (document review,
  due diligence screening, contract extraction); cost efficiency primary driver
- **Examples**: eDiscovery document review; due diligence screening; mass contract data extraction;
  high-volume NDA processing during peak periods

---

## Budget Routing and Authority Framework

### Default Authority Level Matrix

Configure the specific thresholds for your organization; the following represent common
industry ranges observed in practice:

| Authority Level       | Typical Matter Value | Outside Counsel Budget | Approval Required            |
| --------------------- | -------------------- | ---------------------- | ---------------------------- |
| Self-service          | < $50K               | $0 (template only)     | None                         |
| Team lead / paralegal | < $50K               | < $10K                 | Team lead sign-off           |
| Junior counsel        | < $500K              | < $25K                 | Counsel authorization        |
| Senior counsel        | $500K–$5M            | $25K–$250K             | Senior counsel authorization |
| GC / Deputy GC        | $5M–$50M             | $250K–$1M              | GC approval                  |
| GC + CFO              | $50M+                | $1M–$5M                | Joint GC + CFO approval      |
| Board / executive     | Contingency          | > $5M                  | Board authorization          |

### Budget Override Triggers

- Matter budget exceeds approved estimate by > 15%: Re-authorization required at same level
- New claims or defendants added to litigation: Budget re-assessment
- Regulatory scope expansion: Immediate GC notification; budget re-authorization
- Settlement offer: Board approval required above GC unilateral authority threshold (org-defined)
- Annual outside counsel rate increases: GC approval on panel rate schedule changes

### Outside Counsel Pre-Authorization

Matters routed to outside counsel should wherever possible use a **pre-approved panel firm**:

1. **Panel engagement** (preferred): Select firm from pre-authorized panel for practice area;
   engagement letter on standard terms; pre-negotiated rates; no additional procurement
2. **Off-panel engagement** (requires approval): Submit business case to GC; competitive
   pitch preferred for engagements > $100K; single-source justification required if below threshold
3. **Emergency engagement**: Crisis counsel authorized immediately by GC; documentation follows

[JURISDICTION-SPECIFIC] Outside counsel billing guidelines, rate governance, and panel structures
vary by organization. Verify whether your organization has outside counsel guidelines (OCGs)
requiring specific protocols (timekeeping, staffing ratios, technology billing restrictions)
before routing to outside counsel.

---

## Escalation Protocol Triggers

The following conditions **auto-escalate** to GC/CLO regardless of triage classification.
If any trigger is present, skip standard routing and activate the escalation protocol.

### Category 1: Criminal / Quasi-Criminal Risk

- [ ] DOJ, FBI, or state AG criminal investigation or inquiry received
- [ ] Grand jury subpoena received
- [ ] Corporate criminal exposure (FCPA, fraud, antitrust cartel)
- [ ] Individual executive criminal exposure
- [ ] Parallel civil and criminal proceedings

### Category 2: Regulatory Enforcement (High-Stakes)

- [ ] SEC enforcement action or Wells Notice received
- [ ] FTC civil investigative demand (CID) received
- [ ] CFPB supervisory action or enforcement notice
- [ ] EPA Superfund designation or consent decree negotiation
- [ ] Multi-state attorney general coordinated investigation
- [ ] Foreign regulatory enforcement (EU Commission, FCA, FINMA) [JURISDICTION-SPECIFIC]
- [ ] OFAC / sanctions designation or blocked transaction

### Category 3: Board / Investor Triggers

- [ ] Shareholder demand letter or derivative suit filed
- [ ] Activist investor engagement with legal demands
- [ ] Matter requiring board approval or disclosure
- [ ] Public company SEC disclosure triggered (8-K, Form 6-K)
- [ ] Investor rights clause triggered (drag-along, MAC, protective provision)

### Category 4: Media / Reputational

- [ ] Media inquiry received with legal exposure dimension
- [ ] Whistleblower complaint filed (internally or to regulator)
- [ ] Active social media crisis with legal implications
- [ ] Class action complaint filed or threatened with significant plaintiff class

### Category 5: Data / Privacy Crisis

- [ ] Data breach with notification obligation (GDPR 72-hour; US state varies) [VERIFY currency]
- [ ] Ransomware or cyberattack affecting business operations
- [ ] Regulatory inquiry triggered by breach (ICO, CNIL, DPC, state AG)
- [ ] Data subject complaint to supervisory authority (GDPR Art. 77)

### Category 6: Existential Business Risk

- [ ] Financial exposure exceeding insurance limits or going concern risk
- [ ] Loss of key license, permit, or regulatory approval
- [ ] Hostile takeover defense
- [ ] Insolvency or restructuring event with legal dimension
- [ ] Force majeure with material business interruption and legal exposure

### Escalation Protocol Steps

When any trigger is confirmed:

1. **Immediate**: Route to GC / CLO; notify CEO and CFO simultaneously
2. **Within 1 hour**: Outside counsel on standby; activate pre-approved crisis counsel if applicable
3. **Within 2 hours**: Litigation hold notice issued if applicable; preservation protocol activated
4. **Within 4 hours**: Board notification assessment completed; disclosure counsel engaged if public company
5. **Ongoing**: Privilege protocol activated — all sensitive communications via attorney-client
   channels only; no Slack/Teams for substantive facts; mark all materials "PRIVILEGED AND CONFIDENTIAL"

---

## Configurable Routing Rules

### Routing Configuration Framework

The following routing dimensions should be configured for your organization's specific structure.
This skill supports three configuration models:

**Model A — Centralized**

- Single intake queue; routing within team by practice area specialty
- Best for: Companies below $500M revenue, single-jurisdiction, limited practice diversity
- Configuration: Practice area → attorney mapping; skills matrix maintained in matter management system

**Model B — Hub-and-Spoke**

- BU-embedded attorneys handle day-to-day matters; central team handles complexity/specialists
- Routing rule: T1–T2 matters → embedded BU counsel; T3–T4 matters → central team
- Best for: Multi-BU companies ($500M–$5B revenue)
- Configuration: BU → embedded counsel mapping; central team escalation triggers

**Model C — Decentralized / Regional**

- Regional GCs or BU GCs with own teams; central function handles global/cross-border
- Routing rule: Jurisdiction-based routing → regional team; cross-border → central coordination
- Best for: Truly multinational companies (> $5B revenue)
- Configuration: Geography → regional team mapping; cross-border coordination trigger

### Routing Rule Dimensions

Configure routing rules across these dimensions:

| Dimension     | Configuration Variables                                      | Default (if not configured)                    |
| ------------- | ------------------------------------------------------------ | ---------------------------------------------- |
| Practice area | Practice area → attorney pool mapping                        | Route to GC or designated cover                |
| Business unit | BU → embedded counsel or central team routing                | Route to central team                          |
| Geography     | Jurisdiction → regional team or local counsel                | Route to central team; flag for local review   |
| Matter value  | Dollar thresholds → authority level mapping                  | See Budget Routing defaults                    |
| Matter type   | Advisory/Transactional/Litigation/Regulatory → resource tier | Match complexity tier                          |
| Language      | Non-English jurisdiction → bilingual counsel required        | Flag; route to GC for local counsel engagement |

### Routing Rule Maintenance

- Review routing rules quarterly (at minimum)
- Update on attorney arrivals, departures, and practice area changes
- Update on organizational restructuring (new BUs, regional changes)
- Version-control routing ruleset; record effective date; log in Glass Box audit trail

---

## Matter Management System Integration

### System Integration Points

This skill integrates with the following system categories:

**Enterprise Legal Management (ELM) Platforms**

- TeamConnect (Mitratech), Legal Tracker (Thomson Reuters), Onit, SimpleLegal, Lawcadia,
  MatterSuite, Dazychain, Xakia
- Integration: Triage recommendation → matter record creation; matter ID assignment;
  SLA tracking; workload dashboard; budget authorization workflow

**Intake-First Platforms**

- Streamline AI, Checkbox, LawVu
- Integration: Intake form → triage logic → auto-routing; Slack/Teams/email intake channels;
  automated acknowledgment; SLA clock start

**CLM Platforms (when matter originates from a contract)**

- Ironclad, DocuSign CLM, Juro, Agiloft, Icertis, Conga
- Integration: Contract request → triage routing; executed contract → matter record link;
  renewal calendar → urgency trigger

**Ticketing / ITSM Integration**

- Jira Service Management (legal service management template): Customizable for legal intake;
  Confluence knowledge base integration; automation rules for SLA enforcement
- ServiceNow Legal Service Delivery: Enterprise-grade; integrates with IT/HR workflows;
  strong for organizations with existing ServiceNow investment
- Tonkean: Process orchestration layer; integrates with Teams, Slack, Jira, ServiceNow, CLM tools

**Spend Management (post-routing)**

- Brightflag, Apperio, CounselLink
- Integration: Approved outside counsel engagement → e-billing setup; budget monitoring;
  spend threshold alerts to GC

### Integration Architecture Options

1. **Native API integration**: Matter management system API connects directly to CLM, e-billing,
   and finance systems
2. **Email-to-matter parsing**: AI parses inbound email; extracts intake fields; creates draft
   matter record for attorney review
3. **Intake channel connectors**: Slack/Teams bots accept requests; create matter records;
   send automated acknowledgments
4. **Webhook-based escalation**: System events (spend threshold breach, SLA breach, escalation
   trigger) fire webhooks to notify GC/CLO immediately
5. **Middleware**: Mulesoft, Boomi, or Zapier as integration layer between siloed systems

### Graceful Degradation (No System Connected)

If no matter management system is available:

- Record triage recommendation in shared document or spreadsheet tracker
- Send structured triage output (see Output Format Template) directly to requestor and assigned attorney
- Calendar SLA deadlines manually
- Log triage IDs sequentially; maintain routing history for audit purposes

---

## Triage Classification Framework

### Three-Tier Classification

**GREEN — Proceed to Assignment**

_All of the following must be true:_

- [ ] No auto-escalation trigger identified
- [ ] Urgency tier assigned; SLA feasible with available resources
- [ ] Complexity tier assessed; appropriate resource identified and available
- [ ] Financial exposure within authority level of recommended resource
- [ ] No outstanding conditions (budget, conflict check, outside counsel authorization)
- [ ] Confidence scoring ≥ HIGH (0.80+)

_Action_: Assign immediately to recommended resource; SLA clock starts upon assignment
notification. Record triage in matter management system.

---

**YELLOW — Proceed with Conditions**

_Any one of the following is present:_

- [ ] Urgency U1 or U2 but assigned resource not yet confirmed available
- [ ] Budget approval needed before outside counsel engagement begins
- [ ] Conflict of interest check not yet completed
- [ ] Insufficient information — re-triage pending additional facts
- [ ] Outside counsel authorization or panel engagement requires additional step
- [ ] Matter spans BU/geographies requiring cross-team coordination before assignment
- [ ] Confidence scoring PROBABLE (0.60–0.79) — flag for attorney confirmation

_Action_: Assign to resource with conditions documented. List each condition with owner
and resolution deadline. Substantive work does not begin until conditions are satisfied
(or waived in writing by GC). Re-triage is triggered when conditions are cleared.

---

**RED — Escalate Immediately**

_Any one of the following is present:_

- [ ] Any auto-escalation trigger confirmed (see Escalation Protocol Triggers)
- [ ] Criminal exposure identified (individual or corporate)
- [ ] Financial exposure CRITICAL and exceeds GC unilateral authority
- [ ] Regulatory enforcement action with response deadline within 72 hours
- [ ] Board or public company disclosure obligation triggered
- [ ] Reputational risk CRITICAL with active media inquiry
- [ ] Confidence scoring POSSIBLE (0.40–0.59) or lower on triage classification

_Action_: Route to GC/CLO immediately. Activate escalation protocol (5-step). Do not
assign to standard attorney pool. Document all escalation triggers in Glass Box.

---

## Prioritization Framework

When a legal team faces multiple concurrent matters, apply this prioritization hierarchy:

**Tier 1 — Mandatory (Act Now)**

- RED triage status matters
- Hard external deadlines (court, regulatory) within 48 hours
- U1 CRITICAL urgency regardless of triage status

**Tier 2 — High Priority (Act Within SLA)**

- YELLOW triage status matters with active conditions
- U2 HIGH urgency within SLA window
- T3–T4 complexity matters newly assigned
- Active litigation with upcoming court dates

**Tier 3 — Standard (Process in Queue)**

- GREEN triage status, U3 STANDARD urgency
- Routine commercial contract reviews
- Compliance monitoring and advisory work
- Policy review and updates

**Tier 4 — Background (When Capacity Permits)**

- U4 LOW urgency matters
- T1 ROUTINE, no deadline pressure
- Training, template development, proactive research

**Capacity Management Rule**: When attorney workload exceeds 85% of defined capacity threshold,
escalate to team lead for reallocation rather than accepting new T2+ matters at standard queue.

---

## Citation Quality Gates

Run these five gates silently before delivering any triage recommendation containing regulatory
or legal references. If any gate fails, revise before delivering.

| Gate           | Rule                                                                                                                                                 | Fail Action                            |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **Source**     | Every regulatory reference (SLA obligation, notification deadline, filing requirement) cites a specific statute, regulation, or established standard | Add citation or mark `[UNVERIFIED]`    |
| **Format**     | All citations follow a consistent recognizable format for the jurisdiction                                                                           | Fix format                             |
| **Currency**   | Every cited provision checked for amendments, repeal, or recent regulatory change                                                                    | Flag `[CHECK CURRENCY]`                |
| **Domain**     | Analysis stays within the matter's governing jurisdiction — no cross-jurisdictional bleed                                                            | Remove or flag out-of-scope references |
| **Confidence** | Any uncertainty about regulatory timing, threshold, or requirement is explicitly stated                                                              | Add confidence qualifier               |

---

## Self-Interrogation for RED Triage Classifications

For any **RED** triage status, apply this 3-pass adversarial review before delivering:

**Pass 1 — Legal Chain Integrity**
Does the RED classification follow logically from the facts presented? Would a GC actually
need to be involved immediately? Is the auto-escalation trigger confirmed, or only suspected?

**Pass 2 — Completeness**
Have all risk dimensions been assessed? Is there a regulatory dimension not yet surfaced?
Is there criminal exposure that has not been explicitly confirmed or ruled out? Has the
financial exposure been verified against actual exposure, not a worst-case number?

**Pass 3 — Challenge**
What is the strongest argument that this matter does NOT need RED / immediate escalation?
Under what circumstances might a reasonable senior attorney accept it at YELLOW? Document
the counter-argument; if it is compelling, re-assess the classification.

**If RED is confirmed after 3-pass review**: Deliver with confidence. Document the
self-interrogation result in the Glass Box audit trail.

---

## Confidence Scoring

| Level        | Range     | Meaning                                                         | Triage Action                                             |
| ------------ | --------- | --------------------------------------------------------------- | --------------------------------------------------------- |
| **Definite** | 0.95–1.0  | All intake facts confirmed; complete information; clear routing | Proceed with full confidence; deliver recommendation      |
| **High**     | 0.80–0.94 | Minor ambiguities but resolvable; key facts confirmed           | Proceed; note assumption; monitor for re-triage trigger   |
| **Probable** | 0.60–0.79 | Some uncertainty; missing information that could change tier    | Flag for attorney confirmation before substantive work    |
| **Possible** | 0.40–0.59 | Significant gaps; multiple factors could change routing         | Escalate to attorney for manual triage; do not auto-route |
| **Unlikely** | 0.0–0.39  | Major information gaps; could not reliably classify             | Do not deliver triage; request complete intake; escalate  |

---

## Glass Box Audit Trail

Every triage recommendation generates a Glass Box record for traceability:

```yaml
glass_box:
  triage_id: "[Sequential ID, e.g., TRG-2026-0042]"
  matter_title: "[Auto-generated or requestor-provided]"
  received_date: "[ISO date]"
  triaged_date: "[ISO date]"
  requestor: "[Name, BU, contact]"
  intake_channel: "Form / Email / Slack / Teams / Phone / Manual"
  skill_version: "legalcode-matter-triage-workflow v1.0"

  classification:
    primary_practice_area: "[Category from taxonomy]"
    sub_category: "[Specific sub-type]"
    matter_type: "Advisory / Transactional / Litigation / Regulatory / Compliance"
    jurisdictions: "[List]"
    business_unit: "[BU name]"
    geography: "[Region/country]"

  urgency:
    tier: "U1 CRITICAL / U2 HIGH / U3 STANDARD / U4 LOW"
    rationale: "[1-2 sentence explanation]"
    hard_deadline: "[Date or N/A]"
    sla_acknowledgment: "[Date/time]"
    sla_initial_response: "[Date/time]"
    sla_resolution: "[Date range]"
    urgency_override: "Yes / No — [if yes, state authority who authorized]"

  complexity:
    tier: "T1 ROUTINE / T2 MODERATE / T3 COMPLEX / T4 BET-THE-COMPANY"
    weighted_score: "[n/40]"
    key_factors: "[List of top 3 scoring factors]"

  risk_profile:
    financial_exposure: "LOW / MEDIUM / HIGH / CRITICAL"
    estimated_value: "[Dollar amount or range]"
    reputational_risk: "LOW / MEDIUM / HIGH / CRITICAL"
    regulatory_risk: "NONE / INDIRECT / DIRECT"
    criminal_exposure: "YES / NO / POSSIBLE"
    board_disclosure_trigger: "YES / NO / POSSIBLE"

  auto_escalation:
    triggered: "YES / NO"
    triggers_present: "[List of confirmed triggers, or N/A]"

  routing:
    triage_status: "GREEN / YELLOW / RED"
    recommended_resource_tier: "[Tier 0–8 label]"
    assigned_to: "[Name(s)]"
    outside_counsel_authorized: "YES / NO / CONDITIONAL"
    outside_counsel_firm: "[Firm name, or N/A]"
    budget_authority_level: "[Level required]"
    estimated_budget: "[Range]"
    conditions: "[List conditions for YELLOW, or N/A]"

  quality_assurance:
    auto_escalation_check: "COMPLETED / NOT COMPLETED"
    self_interrogation_passes: "[0 / 1 / 2 / 3 — applies to RED only]"
    confidence: "DEFINITE (0.95+) / HIGH (0.80-0.94) / PROBABLE (0.60-0.79) / POSSIBLE (0.40-0.59) / UNLIKELY (<0.40)"
    confidence_rationale: "[Brief explanation]"
    citation_gates_passed: "ALL / [list failing gates]"

  legalcode_mcp: "Connected / Not connected"
  assumptions:
    - "[Any assumption made due to incomplete intake information]"
  information_gaps:
    - "[Missing information that could change the routing]"

  reviewer: "AI-assisted — requires qualified legal review before matter assignment"
  approved_by: "[Attorney name if manual override applied, or N/A]"
  override_reason: "[If automated classification overridden, or N/A]"
```

---

## Anti-Patterns

The following are documented failure modes in legal matter triage. Do not reproduce them.

1. **Email-only intake (the "black hole inbox")**: Relying on unstructured email as the sole
   intake channel makes consistent triage impossible. Requests get lost, duplicated, or handled
   based on who reads their email first. Always establish a structured intake channel with mandatory
   fields.

2. **Urgency inflation by requestors**: Without governance controls (VP approval required for
   CRITICAL designation), business users mark everything urgent. When everything is urgent,
   nothing is. Implement requester-level controls and enforce de-escalation on review.

3. **No acknowledgment SLA**: Failing to send automated acknowledgments leaves requestors without
   confirmation their request was received, generating follow-up email chains and eroding confidence
   in the legal department. Acknowledgment SLA must be the first metric tracked.

4. **Routing to the first available person instead of the best-fit person**: Ad hoc availability-based
   assignment rather than skills-based routing produces attorney-matter mismatches, re-work, and
   re-routing delays. Always match the matter to the closest-fit expertise first.

5. **Complexity underestimation at intake**: Insufficient intake questions that fail to surface
   financial exposure, jurisdictional scope, or regulatory dimensions lead to under-resourcing.
   Matters begin with junior counsel and require emergency escalation mid-stream.

6. **No self-service tier**: Forcing all requests through legal — including requests that could
   be resolved with an approved template or FAQ — consumes attorney capacity that should be
   reserved for matters requiring judgment.

7. **Static routing rules**: Routing rules built at implementation and never updated fail to
   account for attorney arrivals and departures, organizational restructuring, and new regulatory
   requirements. Version-control and review routing rules quarterly.

8. **No feedback loop from outcomes to rules**: Triage decisions are not reviewed against matter
   outcomes (was the urgency tier correct? did this actually need outside counsel?). Without
   outcome data, routing rules cannot improve.

9. **Privilege blind spots**: Using shared intake queues, Slack, or standard email for sensitive
   matters (investigations, board matters, M&A targets) before privilege is established. Route
   sensitive matters through attorney-client privileged channels from the first contact.

10. **Conflating urgency with complexity**: Automatically assigning complex resources (senior
    attorney, outside counsel) to any urgent matter regardless of complexity. A template NDA
    needed same-day is urgent but routine — it does not need a senior attorney. Assess the
    dimensions independently.

11. **Failure to capture matter metadata at intake**: Not recording business unit, jurisdiction,
    practice area, deal value, and deadline at intake means legal operations data is unusable
    for workload reporting, resource planning, and budget forecasting.

12. **No outside counsel pre-authorization framework**: Absence of a pre-approved panel means
    every outside counsel engagement triggers a new procurement process, adding 1–4 weeks of
    delay before substantive work begins on time-sensitive matters.

13. **Treating triage as a one-time event**: Failing to re-triage when scope expands or new
    facts surface. A T2 matter can become T4 mid-stream (e.g., employment dispute becomes class
    action). Establish re-triage triggers for scope changes.

14. **No hard-coded escalation floor for criminal/regulatory triggers**: Over-reliance on
    automated classification for matters that always require human GC-level judgment. Auto-escalation
    for confirmed criminal exposure or board-level triggers must be hard-coded, not optional.

15. **Ignoring business context in routing**: Routing based solely on legal taxonomy without
    considering business unit sensitivity, counterparty relationships, or strategic context. A
    routine contract with a key strategic customer may warrant more senior attention than deal
    value alone suggests.

---

## Writing Standards

Apply these standards before delivering any triage recommendation:

1. **State the classification explicitly**: Every output includes the urgency tier, complexity
   tier, triage status, and recommended resource — stated plainly, not buried in a paragraph.

2. **Cite the basis for RED/YELLOW classifications**: For any non-GREEN status, explicitly list
   the condition(s) that prevented GREEN classification. "YELLOW because budget approval is
   pending for outside counsel engagement" is more actionable than "needs review."

3. **Name the assumptions**: Every assumption made due to incomplete intake information is
   stated explicitly in the output. Do not silently assume.

4. **SLA dates, not durations**: State "Acknowledgment due by [date/time]" not "acknowledgment
   due in 30 minutes." Durations become ambiguous; dates do not.

5. **Avoid legal jargon in the requestor-facing output**: The requestor section of the triage
   recommendation should be readable by a non-lawyer. Reserve legal terminology for the attorney
   section.

6. **Escalation instructions must be actionable**: "Escalate to GC" is not actionable. "Route
   to [GC name] at [contact]; send notification to CEO and CFO; activate outside counsel standby
   protocol" is actionable.

7. **One recommendation per output**: The triage recommendation identifies a single primary
   resource assignment. If multiple options are genuinely equivalent, present the preferred
   option first with brief rationale for alternatives.

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

When legalcode-mcp is available, use it to gather jurisdiction-specific legal authority:

- Verify notification deadlines for data breaches, EEOC/employment complaints, regulatory filings
- Confirm statute of limitations for claim types relevant to the matter
- Verify current outside counsel authorization requirements for specific jurisdictions
- Confirm regulatory investigation response window requirements

Save verified references to a temporary file (`/tmp/legalcode-triage-authority.md`) for
use during triage. Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box.

### Without legalcode-mcp

- Proceed with triage using the frameworks in this skill
- Mark all regulatory timing references with `[VERIFY]`
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Flag jurisdiction-specific deadlines for attorney verification before SLA clock starts

### With Matter Management System Connected

If a matter management system API is accessible:

- Create a matter record upon completing triage
- Populate all Glass Box fields into the matter record
- Set the SLA calendar based on urgency tier
- Trigger assignment notification to the recommended attorney
- Create budget authorization workflow if outside counsel engagement is recommended

---

## Output Format Template

Every triage recommendation follows this structure:

---

```markdown
# MATTER TRIAGE RECOMMENDATION

**Triage ID**: [TRG-YYYY-####]
**Generated**: [ISO timestamp]
**Requestor**: [Name, Business Unit, Contact]

---

## Triage Status: [🟢 GREEN — Proceed / 🟡 YELLOW — Conditions / 🔴 RED — Escalate]

---

## Matter Summary

- **Matter Title**: [Auto-generated or requestor-provided]
- **Matter Description**: [1-3 sentence summary]
- **Practice Area**: [Primary category — Sub-category]
- **Matter Type**: [Advisory / Transactional / Litigation / Regulatory / Compliance]
- **Jurisdiction(s)**: [List]
- **Business Unit**: [BU name]
- **Counterparty / Adverse Party**: [Name(s), if applicable]
- **Intake Channel**: [Form / Email / Slack / Manual]

---

## Assessment

### Urgency: [U1 CRITICAL / U2 HIGH / U3 STANDARD / U4 LOW]

- **Rationale**: [1-2 sentence explanation]
- **Hard Deadline**: [Date, or N/A]
- **Acknowledgment Due**: [Date/time]
- **Initial Response Due**: [Date/time]
- **Resolution Target**: [Date range]

### Complexity: [T1 ROUTINE / T2 MODERATE / T3 COMPLEX / T4 BET-THE-COMPANY]

- **Weighted Score**: [n/40]
- **Key Factors**:
  - [Factor 1: score and explanation]
  - [Factor 2: score and explanation]
  - [Factor 3: score and explanation]

### Risk Profile

| Dimension                | Level                            | Basis             |
| ------------------------ | -------------------------------- | ----------------- |
| Financial Exposure       | [LOW / MEDIUM / HIGH / CRITICAL] | [Estimated value] |
| Reputational Risk        | [LOW / MEDIUM / HIGH / CRITICAL] | [Basis]           |
| Regulatory Risk          | [NONE / INDIRECT / DIRECT]       | [Basis]           |
| Criminal Exposure        | [YES / NO / POSSIBLE]            | [Basis]           |
| Board Disclosure Trigger | [YES / NO / POSSIBLE]            | [Basis]           |

### Auto-Escalation Triggers

- **Triggered**: [YES / NO]
- **Triggers Present**: [List, or None identified]

---

## Routing Recommendation

### Recommended Resource

**Resource Tier**: [Tier 0 Self-Service / Tier 1 Paralegal / Tier 2 Junior Counsel / Tier 3 Senior Counsel / Tier 4 GC / Tier 5-7 Outside Counsel / Tier 8 ALSP]
**Assigned To**: [Name(s) or [PENDING ASSIGNMENT]]
**Outside Counsel**: [Not required / Pre-authorized: [Firm name] / Requires authorization]

### Budget

- **Estimated Budget**: [Range]
- **Authority Level Required**: [Level]
- **Authorization Status**: [Approved / Pending / Not yet submitted]

---

## Conditions (YELLOW matters only)

| #   | Condition               | Owner  | Resolution Deadline |
| --- | ----------------------- | ------ | ------------------- |
| 1   | [Condition description] | [Name] | [Date]              |
| 2   | [Condition description] | [Name] | [Date]              |

_Substantive work on this matter begins when all conditions are satisfied._

---

## Escalation Instructions (RED matters only)

1. **Immediate**: Route to [GC/CLO name]; notify [CEO name] and [CFO name]
2. **Within 1 hour**: Activate outside counsel standby — engage [firm name / crisis counsel]
3. **Within 2 hours**: Issue litigation hold; activate preservation protocol
4. **Within 4 hours**: [Board notification / disclosure counsel engagement if applicable]
5. **Ongoing**: Privilege protocol activated — attorney-client channels only

---

## Assumptions and Information Gaps

**Assumptions Made**:

- [Assumption 1 due to incomplete intake]
- [Assumption 2]

**Information Gaps** (re-triage if resolved):

- [Missing information that could change routing]

---

## Confidence

**Score**: [DEFINITE (0.95+) / HIGH (0.80-0.94) / PROBABLE (0.60-0.79) / POSSIBLE (0.40-0.59) / UNLIKELY (<0.40)]
**Rationale**: [Brief explanation of confidence level]
```

---

## Localization Notes

This skill is jurisdiction-agnostic. When adapting to a specific jurisdiction:

1. **Regulatory notification deadlines**: Replace [VERIFY] placeholders with confirmed local
   deadlines for data breach notification, employment complaint filing, regulatory filings
2. **Statute of limitations**: Build jurisdiction-specific SoL tables for major claim types
   into the urgency scoring section
3. **Professional responsibility rules**: Update bar rule references with the applicable rules
   of professional conduct for the firm's home jurisdiction(s)
4. **In-house counsel privilege**: Explicitly note whether the jurisdiction recognizes attorney-client
   privilege for in-house counsel (not recognized in some EU civil law systems)
5. **Outside counsel qualification**: Verify outside counsel admission requirements for local
   court and regulatory appearances
6. **Currency thresholds**: Convert all dollar thresholds in the Budget Framework to local currency
   and market-appropriate amounts for the jurisdiction
7. **Language requirements**: Some jurisdictions mandate contracts and regulatory submissions in
   the local language — flag this as a routing condition where applicable

---

## Provenance

Created by Legalcode (2026-03-02). Legalcode original synthesis built from:

- 2-agent research pipeline (structural analysis of reference skills +
  legal operations web research via WebSearch/WebFetch)
- Reference standard: `legalcode-client-intake-workflow` (workflow structure, PDCA quality
  cycle, Glass Box model, CLARIFY pattern)
- Reference standard: `legalcode-conflict-check` (3-pass self-interrogation, confidence scoring)
- Reference standard: `legalcode-contract-review` (citation quality gates, quality frameworks)
- Legal operations sources: CLOC State of the Industry 2025; Streamline AI intake/triage
  frameworks; Axiom Law two-step resource allocation model; Brightflag matter management
  best practices; Dazychain Legal Intake Workflow Guide; Juralio noslegal taxonomy framework;
  Lawcadia intake automation guides; HyperStart legal ticketing systems overview
- Practice area taxonomy aligned with SALI LMSS (Legal Matter Specification Standard) [VERIFY]
- Resource tier model incorporating Axiom's Digital/Industrial/Artisanal classification
- Integration landscape: Streamline AI, Checkbox, LawVu, TeamConnect, Legal Tracker, Onit,
  Brightflag, Apperio, Jira Service Management, ServiceNow Legal Service Delivery

All regulatory citations and specific SLA thresholds marked [VERIFY] require verification
against current law and your organization's specific authority levels before reliance.
