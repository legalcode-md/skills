---
name: legalcode-ccpa-admt-compliance
description: Assess and implement California CPRA Automated Decision-Making Technology (ADMT) compliance
  for businesses using AI or algorithmic systems that make or substantially replace human decision-making
  for significant decisions. Use when deploying AI systems for hiring/recruitment, credit decisions, insurance
  underwriting, tenant screening, healthcare eligibility, educational assessment, or other consequential
  automated decisions affecting California consumers; conducting ADMT risk assessments; drafting ADMT
  pre-use notices and privacy policy disclosures; implementing opt-out mechanisms for significant decisions;
  designing human appeal processes for ADMT decisions; or building an ADMT compliance program for California
  operations.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Assess and implement California CPRA Automated Decision-Making Technology (ADMT) compliance for businesses using AI or algorithmic systems that make or substantially replace human decision-making for significant decisions. Covers ADMT scope determination and significant decision classification (employment, lending, housing, healthcare, education, insurance), pre-use notice drafting (11 CCR 7220), consumer opt-out mechanism implementation (11 CCR 7221), access request response procedures (11 CCR 7222), alternative human review process design, risk assessment requirements for ADMT under 11 CCR 7150-7157, ADMT training data documentation obligations (11 CCR 7153), profiling disclosure requirements, and ongoing compliance monitoring. Aligned with CPPA final regulations effective January 1, 2026, with full ADMT compliance required by January 1, 2027, and risk assessment submission deadlines (April 1, 2028). Integrates with broader CCPA/CPRA consumer rights framework (Cal. Civ. Code 1798.100 et seq.), CPPA enforcement priorities, and cross-references EU AI Act, Colorado SB 24-205, and NYC Local Law 144 for multi-jurisdiction AI governance. Use when deploying AI systems for hiring/recruitment, credit decisions, insurance underwriting, tenant screening, healthcare eligibility, educational assessment, or other consequential automated decisions affecting California consumers; conducting ADMT risk assessments; drafting ADMT pre-use notices and privacy policy disclosures; implementing opt-out mechanisms for significant decisions; designing human appeal processes for ADMT decisions; or building an ADMT compliance program for California operations. Produces compliance gap analysis, pre-use notice templates, opt-out mechanism specifications, access request response procedures, risk assessment documentation, human oversight design, remediation roadmaps, and Glass Box audit trails suitable for CPPA regulatory submission and internal governance.


# Legalcode CCPA ADMT Compliance

> **Disclaimer**: This skill provides a framework for AI-assisted CCPA Automated Decision-Making
> Technology compliance assessment. It does not constitute legal advice, regulatory compliance
> certification, or authorization to deploy an ADMT system. All outputs require review by qualified
> legal counsel licensed in California before implementation. CPPA regulations are recent (effective
> January 1, 2026), actively being interpreted, and subject to ongoing enforcement guidance — verify
> current requirements before relying on any provision described here. Statutory, regulatory, and
> enforcement references cited from training-data knowledge carry hallucination risk — verify against
> authoritative primary sources (California Legislative Information, CPPA official website) before
> relying on them. Mark all unverified references [VERIFY].

---

## Purpose and Scope

This skill assesses and implements compliance with California's CCPA/CPRA Automated Decision-Making
Technology (ADMT) regulations under 11 CCR Article 11 (Sections 7200-7222) and the broader risk
assessment requirements under Article 10 (Sections 7150-7157). It helps organizations determine
whether their AI systems qualify as ADMT for significant decisions, implement required consumer
rights mechanisms, draft compliant notices, and build sustainable ADMT governance programs.

**Covers:**

- ADMT scope determination (is this system covered?)
- Significant decision classification (employment, lending, housing, healthcare, education, insurance)
- Pre-use notice drafting (11 CCR 7220)
- Consumer opt-out mechanism design and implementation (11 CCR 7221)
- Access request response procedures (11 CCR 7222)
- Alternative human review process design
- ADMT risk assessment documentation (11 CCR 7150-7157)
- ADMT training data documentation (11 CCR 7153)
- Profiling disclosure requirements
- Privacy policy ADMT disclosure updates
- Compliance gap analysis with remediation roadmaps
- CPPA submission preparation (risk assessment summaries)

**Does not:**

- Provide definitive legal determination of CPRA applicability (only qualified California counsel can)
- Execute technical implementation of ADMT systems
- Replace CPPA guidance or formal legal opinions
- Guarantee regulatory compliance or safe harbor
- Address ADMT requirements outside California (see related skills for EU AI Act, Colorado SB 24-205,
  NYC LL 144)
- Apply to processing that does not qualify as ADMT or does not involve significant decisions

**Related skills:**

- `legalcode-algorithmic-impact-assessment` — Multi-jurisdiction algorithmic impact assessment
  covering EU AI Act Art. 27 FRIA, NYC LL 144, Colorado SB 24-205, and California CPRA ADMT
- `legalcode-ai-governance-framework-builder` — Organizational AI governance framework aligned with
  ISO/IEC 42001:2023 and NIST AI RMF
- `legalcode-dpia-generator` — GDPR Article 35 Data Protection Impact Assessment
- `ccpa-cpra-consumer-rights-operations` — California CCPA/CPRA consumer rights operations for
  deletion, access, correction, and opt-out requests

---

## Jurisdiction and Governing Law

This skill is **California-specific**, addressing:

- California Consumer Privacy Act of 2018, as amended by the California Privacy Rights Act (Cal. Civ.
  Code 1798.100-1798.199.100)
- California Privacy Protection Agency regulations (11 CCR 7000 et seq.)
- Specifically: Article 10 (Risk Assessments, 11 CCR 7150-7157) and Article 11 (Automated
  Decisionmaking Technology, 11 CCR 7200-7222)

**Regulatory timeline:**

- **January 1, 2026**: CPPA final regulations effective (including ADMT provisions)
- **January 1, 2027**: Full compliance required for ADMT use in significant decisions
- **April 1, 2028**: First risk assessment submission deadline to CPPA (covering 2026-2027)
- **Annually thereafter**: Risk assessment summary submissions

**Enforcement context:**

- CPPA has enforcement authority with hundreds of open investigations as of late 2025
- Consumer complaints rising (~150/week as of Q4 2025) [VERIFY current enforcement statistics]
- Penalties up to $7,500 per intentional violation
- No private right of action for ADMT violations (AG/CPPA enforcement only)
- CPPA has signaled ADMT as an enforcement priority area

[VERIFY] Check CPPA website (cppa.ca.gov) for current enforcement actions, guidance documents, and
FAQs related to ADMT compliance.

---

## Key Definitions (11 CCR 7001)

### Automated Decisionmaking Technology (ADMT)

Any technology that processes personal information and uses computation to execute a decision,
replace human decisionmaking, or **substantially assist** human decisionmaking.

**Includes:**

- Machine learning models making or recommending decisions
- Rule-based algorithmic systems
- AI systems that score, rank, classify, or filter individuals
- Profiling technology that derives or infers characteristics about individuals

**Excludes (basic computational tools):**

- Databases and data storage systems
- Spam filters and antivirus software
- Spellcheckers and grammar tools
- Basic calculators and spreadsheets
- Tools that do not replace human judgment in decisions

**"Substantially assist"** means the technology's output is a principal basis for the decision, and
the human reviewer:

- Does NOT interpret the output meaningfully
- Does NOT analyze other relevant information independent of the output
- Does NOT have authority to alter the decision based on their own judgment

If meaningful human review occurs (interpretation + analysis + authority to override), the system may
not qualify as ADMT even if AI-assisted.

### Significant Decision

A decision that results in the **provision or denial** of:

- Financial or lending services (credit approval, loan terms, credit limits)
- Housing or lodging (rental applications, tenant screening)
- Employment or independent contracting (hiring, promotion, termination, compensation, task
  allocation)
- Education enrollment or opportunities (admissions, scholarships, academic tracking)
- Essential government services
- Healthcare services (eligibility, coverage, treatment access)
- Insurance (underwriting, pricing, claims)

**Excludes (not significant decisions):**

- Advertising and marketing decisions (covered separately under profiling)
- Content recommendation (absent denial of essential services)
- Fraud detection (unless it results in denial of service)

### Profiling

Any form of automated processing of personal information to evaluate certain aspects of an
individual, particularly analyzing or predicting:

- Work performance
- Economic situation
- Health
- Personal preferences
- Interests
- Reliability
- Behavior
- Location
- Movements

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points marked with **CLARIFY**. At
each CLARIFY point, present structured options with explanatory context (why the answer matters).
If the user has already provided the information, skip the question and proceed.

For batch or non-interactive runs, proceed with the following defaults and state them explicitly:

- Scope: Assess all described ADMT systems
- Decision context: As described in the input
- Compliance deadline: January 1, 2027 (full compliance)
- Risk tolerance: Conservative (comply with all requirements; no reliance on ambiguities)

---

## Workflow

### Step 1: Accept Input

Accept information about the organization's AI/algorithmic systems in any of these formats:

- **System inventory**: List of AI systems with descriptions, inputs, outputs, and decision contexts
- **Vendor documentation**: AI vendor system specifications, model cards, or data sheets
- **Process descriptions**: Business process descriptions involving automated decisions
- **Existing compliance materials**: Privacy policies, risk assessments, notices already in place
- **Single system focus**: Detailed description of one specific ADMT system to assess

If no input is provided, prompt the user to supply at minimum:

- A description of the AI/algorithmic system(s) in use
- The decision context(s) where the system is used
- Whether the system affects California consumers

### Step 2: Gather Context

**CLARIFY** — Before beginning the assessment, ask these questions (skip any already answered):

**1. Business Applicability**
Does your organization meet CCPA/CPRA business thresholds?

- Yes, we are a covered business (annual revenue > $25M, or process 100K+ consumers/households
  annually, or derive 50%+ revenue from selling/sharing personal information)
- Uncertain — need to verify threshold applicability
- We are a service provider/contractor acting on behalf of a business
- We believe we are exempt (describe basis)
  _Why this matters: ADMT obligations apply only to "businesses" as defined under CCPA. Service
  providers have different, derived obligations._

**2. System Inventory**
How many AI/algorithmic systems do you want to assess?

- Single system (provide detailed description)
- Multiple systems (provide inventory or list)
- All systems making automated decisions (conduct full inventory)
- Uncertain what qualifies — need scoping guidance
  _Why this matters: Determines scope of assessment and level of detail for each system._

**3. Decision Contexts**
In which contexts are your AI systems used? (Select all that apply)

- Employment (hiring, screening, performance, compensation, termination)
- Credit/lending (loan approval, pricing, limits, adverse action)
- Insurance (underwriting, pricing, claims)
- Housing/tenant screening
- Healthcare (eligibility, treatment access, benefits)
- Education (admissions, scholarships, academic decisions)
- Advertising/marketing only (may not trigger ADMT obligations)
- Customer service/support
- Fraud detection/prevention
- Other (describe)
  _Why this matters: Only "significant decisions" trigger full ADMT compliance obligations. Advertising
  decisions are excluded from the significant decision definition but may trigger profiling disclosures._

**4. Compliance Status**
What is your current ADMT compliance status?

- No ADMT-specific compliance measures in place
- Partial compliance (describe what exists)
- Compliance program exists but needs audit/refresh
- Preparing for January 1, 2027 deadline
  _Why this matters: Determines whether this is a gap analysis, full implementation, or audit._

**5. Human Oversight Design**
What human oversight exists for your AI-assisted decisions?

- Fully automated — no human review before decision
- Human-in-the-loop — human reviews every AI recommendation
- Human-on-the-loop — human monitors but AI executes decisions
- Appeals only — human review available after adverse decision
- Uncertain — need to map current process
  _Why this matters: The level of human oversight affects both (a) whether the system qualifies as ADMT
  and (b) whether opt-out exceptions apply._

**6. Organizational Playbook**
Does your organization have existing AI governance policies?

- Yes, with defined ADMT or algorithmic accountability framework
- Yes, general AI/ethics policy (no ADMT-specific provisions)
- No, use regulatory baseline
  _Why this matters: Existing policies may already address some requirements; assessment will identify
  gaps against CPPA requirements._

### Step 3: Load Organizational Context

Check for existing compliance materials:

- Privacy policy (look for existing ADMT disclosures)
- AI governance policy or acceptable use policy
- Existing risk assessments for AI systems
- Vendor contracts and data processing agreements
- Consumer rights request procedures

If found, extract current state for gap analysis.

### Step 4: Gather Regulatory Authority

Research current CPPA guidance and enforcement.

**With legalcode-mcp connected (preferred):**

Search for:

- Current 11 CCR 7000+ regulatory text
- CPPA guidance documents on ADMT compliance
- CPPA enforcement actions related to ADMT or automated decisions
- CPPA FAQs and interpretive guidance
- California AG enforcement priorities
- Any CPPA proposed rulemaking that may affect ADMT (check for amendments)

Save findings to: `/tmp/ccpa-admt-authority.md`

**Without legalcode-mcp:**

Mark all regulatory citations with [VERIFY]. Note in Glass Box: `external_tools_used: "None — manual
verification required"`. Include notice: "All regulatory citations require independent verification
by qualified California counsel before implementation."

Authoritative sources for manual verification:

- CPPA official website: cppa.ca.gov
- California Legislative Information: leginfo.legislature.ca.gov
- California Office of Administrative Law: oal.ca.gov
- 11 CCR 7000+ regulations text

### Step 5: ADMT Scope Determination

For each system in scope, determine whether it qualifies as ADMT under CPPA regulations.

**5a. ADMT Classification Test**

Apply the following decision tree:

```
1. Does the system process personal information?
   NO → Not ADMT (stop)
   YES → Continue

2. Does the system use computation to execute, replace, or substantially assist
   human decisionmaking?
   NO → Not ADMT (stop)
   YES → Continue

3. Is the system used for basic computational functions only (database, spam
   filter, spellcheck, calculator)?
   YES → Not ADMT (stop)
   NO → Continue

4. Is there meaningful human review with:
   (a) Interpretation of the output, AND
   (b) Analysis of other relevant information, AND
   (c) Authority to override or alter the decision?
   YES (all three) → May not qualify as ADMT — document human oversight process
   NO (any missing) → Qualifies as ADMT → Continue to Step 5b
```

**5b. Significant Decision Classification**

For each ADMT system, determine whether it is used for significant decisions:

| Decision Domain               | Significant Decision? | Examples                                                                              |
| ----------------------------- | --------------------- | ------------------------------------------------------------------------------------- |
| Employment/contracting        | YES                   | Hiring, promotion, termination, compensation, task allocation, performance monitoring |
| Credit/lending                | YES                   | Loan approval, credit limits, interest rates, adverse action                          |
| Insurance                     | YES                   | Underwriting, premium pricing, claims decisions                                       |
| Housing/lodging               | YES                   | Tenant screening, rental approval, lease terms                                        |
| Healthcare                    | YES                   | Eligibility, coverage, treatment access, benefits                                     |
| Education                     | YES                   | Admissions, scholarships, academic tracking, expulsion                                |
| Essential government services | YES                   | Benefits eligibility, public housing, emergency services                              |
| Advertising/marketing         | NO                    | Ad targeting, personalization, recommendations (unless denies essential service)      |
| Fraud prevention              | DEPENDS               | Only if results in denial of service                                                  |
| Customer service              | DEPENDS               | Only if determines eligibility for significant service                                |

**CLARIFY** — For systems in the "DEPENDS" category, ask: "Does this system's output result in the
provision or denial of a significant service (credit, housing, employment, healthcare, etc.), or is
it advisory only?"

**5c. Document Scope Determination**

For each system, document:

| System | ADMT?  | Significant Decision? | Domain   | Compliance Required By       |
| ------ | ------ | --------------------- | -------- | ---------------------------- |
| [Name] | Yes/No | Yes/No/Depends        | [Domain] | Jan 1, 2027 / Not applicable |

### Step 6: Pre-Use Notice Requirements (11 CCR 7220)

For each ADMT system used for significant decisions, draft compliant pre-use notices.

**Required Elements (Plain Language):**

1. **Purpose Statement** — Specific purpose for which ADMT is used (not generic)
   - BAD: "We use AI to improve your experience"
   - GOOD: "We use automated technology to evaluate your job application by analyzing your resume,
     assessing your responses to screening questions, and predicting your fit for the role"

2. **Logic and Parameters** — How the ADMT works
   - What inputs/data the system uses
   - What analysis or scoring it performs
   - What outputs or decisions it produces
   - Key parameters or factors that influence the decision

3. **Decision Outcomes** — What decisions the ADMT makes or influences
   - Possible outcomes (approval, denial, ranking, scoring)
   - How the output is used in the decision process
   - Whether the decision is binding or a recommendation

4. **Opt-Out Rights** — Consumer's right to opt out
   - Clear statement of the right to opt out of ADMT for this significant decision
   - Link or method to exercise opt-out (must provide at least two methods)
   - What happens after opt-out (alternative human process)

5. **Alternative Process** — What happens if consumer opts out
   - Description of the human review alternative
   - Timeline for alternative process
   - Any differences in outcome or timeline

6. **No Retaliation Statement** — Anti-retaliation commitment
   - Clear statement that exercising opt-out right will not result in retaliation or denial of
     service (absent legitimate business reason)

**Timing:**

- Pre-use notice must be provided **before** collecting or processing personal information via ADMT
- May be integrated into notice at collection (Cal. Civ. Code 1798.100)
- Must be provided each time ADMT is used for a new significant decision affecting the consumer

**Format:**

- Plain language (avoid technical jargon)
- Accessible format
- Prominent placement (not buried in lengthy privacy policy)
- May use layered approach (summary with link to full details)

### Step 7: Consumer Opt-Out Mechanism (11 CCR 7221)

Design and document compliant opt-out mechanisms.

**Opt-Out Requirements:**

1. **Methods** — Provide at least two easy methods
   - One method must match the primary interaction channel (web form for web, in-app for mobile)
   - Examples: online form, toll-free number, email address, in-app toggle
   - Do NOT require account creation solely to opt out
   - Do NOT bury opt-out in cookie consent banners
   - Treat Global Privacy Control (GPC) signals equivalently where applicable

2. **No Verification (Generally)**
   - Opt-out requests do not require verification **unless** the business has not yet processed
     personal information via ADMT
   - If processing has not yet occurred, may verify to prevent fraudulent requests

3. **Processing Timeline**
   - Cease ADMT processing **as soon as feasible**
   - No later than **15 business days** after request receipt
   - Notify service providers/contractors to cease ADMT processing

4. **Confirmation**
   - Confirm receipt of opt-out request
   - Confirm when ADMT processing has ceased
   - Describe alternative process provided

5. **No Re-Ask**
   - Do not ask consumer to reconsider opt-out for **12 months** after request

6. **Authorized Agents**
   - Accept opt-out requests from authorized agents with signed permission

**Exceptions to Opt-Out Obligation:**

- Business offers a **human appeal process** where a qualified reviewer can overturn the ADMT decision
- Narrow hiring/admissions exception: ADMT solely assesses objective performance criteria without
  discrimination
  [VERIFY: Confirm current scope of exceptions under 11 CCR 7221]

**Alternative Human Process Requirements:**
When consumer opts out, provide a human review process that:

- Is conducted by a qualified human reviewer
- Reviewer has authority to interpret information and override/alter the decision
- Timeline is comparable to (or disclosed if longer than) the ADMT process
- Does not require unreasonable burden on consumer

### Step 8: Access Request Procedures (11 CCR 7222)

Design and document procedures for responding to consumer access requests about ADMT.

**Consumer Right:**
Consumers may request information about ADMT use for significant decisions affecting them.

**Response Requirements:**

1. **Acknowledgment** — Within **10 business days** of verified request receipt

2. **Full Response** — Within **45 calendar days** (extendable by 45 additional days with notice)

3. **Required Disclosures (Plain Language):**
   - Purpose for which ADMT was used
   - Logic and parameters of the ADMT
   - Output or decision the ADMT produced for this consumer
   - How the output was used in the decision
   - Future planned uses of ADMT for this consumer (if known)

4. **Verification** — Standard CCPA verification procedures apply

5. **Exemptions:**
   - Trade secrets (but must still provide non-trade-secret information)
   - Security information (if disclosure would compromise system security)
   - Cannot refuse entire request based on partial exemption

**Integration with General CCPA Access Requests:**

- ADMT access requests may be submitted through existing CCPA request channels
- Response procedures should integrate with existing consumer rights operations
- Consider combining ADMT-specific disclosures with general access responses when consumer requests
  both

### Step 9: Risk Assessment Requirements (11 CCR 7150-7157)

Document risk assessment obligations for ADMT processing.

**When Risk Assessment Required (11 CCR 7150):**

- Using ADMT for significant decisions
- Using ADMT for automated profiling
- Training ADMT with personal information
- Using facial recognition or biometric identification

**Risk Assessment Timing:**

- **Before** starting high-risk processing activity
- **Within 45 days** of material changes to processing
- **Review every 3 years** (or upon material change)
- **Submit to CPPA**: April 1, 2028 for 2026-2027 assessments; annually thereafter

**Required Documentation (11 CCR 7152):**

| Element                     | What to Document                                                   |
| --------------------------- | ------------------------------------------------------------------ |
| **Processing purpose**      | Specific purpose for ADMT use (not generic)                        |
| **Categories of PI**        | What personal information is processed                             |
| **Context**                 | Where and how processing occurs                                    |
| **Collection methods**      | How PI is collected for ADMT                                       |
| **Retention periods**       | How long PI and ADMT outputs are retained                          |
| **Consumers affected**      | Number and categories of consumers                                 |
| **Benefits**                | Benefits of ADMT processing (to business and consumers)            |
| **Privacy risks**           | Risks to consumer privacy and security (quantified where possible) |
| **Benefit-risk analysis**   | Does processing benefit outweigh privacy risks?                    |
| **Safeguards/mitigations**  | Technical and organizational measures to reduce risk               |
| **Residual risk**           | Risks remaining after safeguards applied                           |
| **Stakeholder involvement** | Relevant stakeholders consulted (11 CCR 7151)                      |
| **Approval**                | Who approved the processing and when                               |

**ADMT Training Documentation (11 CCR 7153):**
For ADMT training with personal information, additionally document:

- Training datasets used (categories, sources, size)
- Training process and methodology
- Model outputs and performance metrics
- Bias assessments conducted
- Fairness testing results
- Model validation procedures

**Decision Threshold:**
If privacy risks outweigh benefits, the business must **halt or not proceed** with processing until
risks are adequately mitigated.

**Retention:**

- Retain risk assessments for **5 years** after processing ends
- Make available to CPPA and California AG upon request

### Step 10: Privacy Policy and Notice Updates

Identify required updates to existing privacy notices and policies.

**Privacy Policy ADMT Disclosures:**

1. **General ADMT Disclosure**
   - Statement that business uses ADMT for significant decisions
   - Categories of significant decisions affected
   - Consumer rights regarding ADMT (opt-out, access)

2. **Profiling Disclosure (if applicable)**
   - Statement that business engages in profiling
   - Categories of profiling activities
   - Consumer rights regarding profiling

3. **Link to ADMT-Specific Information**
   - Link to detailed ADMT disclosures or pre-use notices
   - Instructions for exercising ADMT-related rights

**Notice at Collection Updates:**

- Add ADMT-related disclosures to notice at collection where ADMT is used
- May consolidate pre-use notice with notice at collection

### Step 11: Compliance Gap Analysis

Compare current state against requirements and identify gaps.

**Gap Analysis Matrix:**

| Requirement                 | Regulatory Citation | Current State | Gap? | Priority | Remediation |
| --------------------------- | ------------------- | ------------- | ---- | -------- | ----------- |
| ADMT scope inventory        | 11 CCR 7200         |               |      |          |             |
| Pre-use notices             | 11 CCR 7220         |               |      |          |             |
| Opt-out mechanisms          | 11 CCR 7221         |               |      |          |             |
| Access request procedures   | 11 CCR 7222         |               |      |          |             |
| Human review alternative    | 11 CCR 7221         |               |      |          |             |
| Risk assessments            | 11 CCR 7150-7157    |               |      |          |             |
| Training data documentation | 11 CCR 7153         |               |      |          |             |
| Privacy policy disclosures  | 11 CCR 7200+        |               |      |          |             |
| Record retention            | 11 CCR 7152         |               |      |          |             |

**Classify Each Gap:**

| Classification    | Meaning                                | Action                                 |
| ----------------- | -------------------------------------- | -------------------------------------- |
| **COMPLIANT**     | Meets or exceeds requirements          | Document and maintain                  |
| **PARTIAL**       | Some elements present; gaps remain     | Remediate before deadline              |
| **NON-COMPLIANT** | Requirement not met                    | Immediate remediation priority         |
| **CRITICAL**      | Material gap creating enforcement risk | Escalate; halt processing if necessary |

### Step 12: Remediation Roadmap

Build prioritized remediation plan.

**Priority Levels:**

| Priority       | Criteria                                                 | Timeline    |
| -------------- | -------------------------------------------------------- | ----------- |
| **IMMEDIATE**  | Critical gaps; enforcement risk; halt processing trigger | 30-60 days  |
| **NEAR-TERM**  | Non-compliant items; January 1, 2027 deadline            | 60-180 days |
| **BACKGROUND** | Partial compliance items; process improvements           | 180+ days   |

**Remediation Actions by Category:**

**Notices and Disclosures:**

- Draft pre-use notices for each ADMT system
- Update privacy policy with ADMT disclosures
- Update notice at collection
- Implement notice delivery mechanisms

**Consumer Rights:**

- Build or update opt-out request intake channels
- Train staff on ADMT opt-out processing
- Document human review alternative process
- Build ADMT access request response procedures
- Update consumer rights SLA tracking for ADMT-specific timelines

**Risk Assessments:**

- Conduct risk assessments for each ADMT system
- Document training data governance (if applicable)
- Establish 3-year review cycle
- Prepare for April 2028 CPPA submission

**Governance:**

- Update AI governance policy for ADMT compliance
- Assign ADMT compliance ownership
- Establish monitoring and audit procedures
- Train relevant personnel

### Step 13: Quality Verification

Before delivering the assessment, run quality checks.

**13a. Completeness Check**

Verify all required elements are addressed:

| Element                             | Present | Quality | Notes |
| ----------------------------------- | ------- | ------- | ----- |
| ADMT scope determination            |         |         |       |
| Significant decision classification |         |         |       |
| Pre-use notice templates            |         |         |       |
| Opt-out mechanism design            |         |         |       |
| Access request procedures           |         |         |       |
| Human review alternative            |         |         |       |
| Risk assessment requirements        |         |         |       |
| Privacy policy updates              |         |         |       |
| Gap analysis                        |         |         |       |
| Remediation roadmap                 |         |         |       |
| Timeline to compliance              |         |         |       |

**13b. Citation Quality Gates**

Run these 5 gates silently before delivering output:

| Gate           | Rule                                                                                    | Fail Action                       |
| -------------- | --------------------------------------------------------------------------------------- | --------------------------------- |
| **Source**     | Every regulatory claim cites specific 11 CCR section or Cal. Civ. Code section          | Add citation or mark [VERIFY]     |
| **Format**     | All citations use consistent California citation format                                 | Fix format                        |
| **Currency**   | Verify regulatory text reflects January 1, 2026 effective regulations                   | Flag [CHECK CURRENCY]             |
| **Scope**      | Analysis limited to California CPRA; no importing requirements from other jurisdictions | Remove or flag jurisdiction bleed |
| **Confidence** | Uncertainty explicitly stated                                                           | Add confidence qualifier          |

**13c. Self-Interrogation for Critical Gaps**

For any CRITICAL or NON-COMPLIANT finding, apply 3-pass review:

**Pass 1 — Regulatory Basis:**

- Is this requirement clearly stated in 11 CCR or Cal. Civ. Code?
- Is there CPPA guidance that clarifies or contradicts this interpretation?
- Could a reasonable attorney read the regulation differently?

**Pass 2 — Completeness:**

- Have all relevant sections been considered (7200-7222, 7150-7157)?
- Are there exemptions or exceptions that might apply?
- Is the significant decision classification correct?

**Pass 3 — Proportionality:**

- Is CRITICAL classification proportionate to the actual risk?
- What is the likelihood and severity of enforcement?
- Are there mitigating factors not yet considered?

### Step 14: Generate Deliverables

Produce the assessment outputs.

**Primary Deliverables:**

1. **ADMT Compliance Assessment Report** — Full analysis per Output Format Template
2. **Pre-Use Notice Templates** — Customized for each ADMT system
3. **Opt-Out Mechanism Specifications** — Technical requirements for implementation
4. **Access Request Procedure SOP** — Standard operating procedure for ADMT access requests
5. **Risk Assessment Template** — Pre-populated template for each ADMT system
6. **Privacy Policy Redlines** — Tracked changes for ADMT disclosures
7. **Remediation Roadmap** — Prioritized action items with owners and deadlines
8. **Glass Box Audit Trail** — Compliance traceability documentation

---

## Severity Classification

### COMPLIANT

System or process meets all CPRA ADMT requirements. No remediation needed.

**Examples:**

- Pre-use notice contains all required elements and is provided before ADMT processing
- Two opt-out methods available and functioning
- Risk assessment documented and current
- Human review alternative available with qualified reviewers

**Action**: Document and maintain. Include in ongoing monitoring.

### PARTIAL

Some requirements met; gaps remain that must be addressed before January 1, 2027.

**Examples:**

- Pre-use notice exists but missing logic/parameters disclosure
- One opt-out method available but regulation requires two
- Risk assessment started but not completed
- Human review available but reviewers not trained

**Action**: Prioritize remediation. Document current state and gap.

### NON-COMPLIANT

Requirement not met. Material gap requiring immediate attention.

**Examples:**

- No pre-use notice for ADMT significant decision
- No opt-out mechanism available
- No risk assessment conducted
- ADMT used for significant decision with no human oversight or alternative

**Action**: Remediate before January 1, 2027 deadline. Escalate if needed.

### CRITICAL

Material gap creating active enforcement risk. Processing should be halted or fundamentally
restructured.

**Examples:**

- ADMT making fully automated significant decisions with no opt-out or human alternative
- Consumer rights requests being denied or ignored
- Deceptive ADMT disclosures (dark patterns)
- CPPA investigation pending or enforcement action imminent

**Action**: Halt processing pending remediation. Escalate to senior leadership and counsel. Engage
outside counsel if necessary.

---

## Actionable Remediation Framework

For each finding, provide specific remediation:

```
**Finding**: [Description]
**Classification**: COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL
**Regulatory Basis**: [11 CCR section or Cal. Civ. Code section]
**Current State**: [What exists now]
**Required State**: [What compliance requires]
**Gap**: [Specific gap description]
**Remediation Action**: [Specific steps to close gap]
**Owner**: [Suggested owner — Legal, IT, Privacy, Business]
**Timeline**: [IMMEDIATE / NEAR-TERM / BACKGROUND]
**Dependencies**: [Other items that must be completed first]
**Verification**: [How to confirm remediation is complete]
```

---

## Prioritization Framework

### Tier 1 — Critical Path (Deadline: Immediate)

Issues that create active enforcement risk or require halting processing:

- ADMT used for significant decisions with no consumer opt-out
- Consumer rights requests not being processed
- Deceptive or misleading ADMT disclosures
- CPPA investigation or AG inquiry

### Tier 2 — Compliance Deadline (Deadline: January 1, 2027)

Issues that must be resolved for full compliance:

- Pre-use notice drafting and deployment
- Opt-out mechanism implementation
- Access request procedures
- Human review alternative design
- Privacy policy updates

### Tier 3 — Governance Foundation (Deadline: April 1, 2028)

Issues for ongoing compliance and CPPA submission:

- Risk assessment documentation
- Training data documentation
- Submission preparation
- Ongoing monitoring program
- Audit and review cycles

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output:

| Gate           | Rule                                                                                        | Fail Action                        |
| -------------- | ------------------------------------------------------------------------------------------- | ---------------------------------- |
| **Source**     | Every regulatory requirement cites 11 CCR section, Cal. Civ. Code section, or CPPA guidance | Add citation or mark [VERIFY]      |
| **Format**     | California regulatory citations use proper format (11 CCR 7XXX)                             | Fix format                         |
| **Currency**   | Verify requirements reflect regulations effective January 1, 2026                           | Flag [CHECK CURRENCY] if uncertain |
| **Scope**      | Analysis applies only to California; do not import EU/Colorado/NYC requirements             | Remove or flag jurisdiction bleed  |
| **Confidence** | If uncertain about interpretation, state uncertainty explicitly                             | Add confidence qualifier           |

---

## Self-Interrogation for Critical Findings

For any CRITICAL or enforcement-risk finding, apply this 3-pass review:

**Pass 1 — Regulatory Chain:**

- Is this requirement explicitly stated in 11 CCR 7200-7222 or 7150-7157?
- Is there CPPA guidance or FAQ that clarifies the requirement?
- Could a reasonable California privacy attorney read this differently?
- What is the strongest counter-argument?

**Pass 2 — Completeness:**

- Have all relevant regulatory sections been considered?
- Are there exemptions (e.g., human appeal exception to opt-out)?
- Is the significant decision classification correct per 11 CCR 7001?
- Have service provider vs. business obligations been correctly applied?

**Pass 3 — Proportionality:**

- Is CRITICAL classification proportionate to actual enforcement risk?
- What enforcement actions has CPPA taken in similar situations?
- Are there mitigating factors (good faith efforts, partial compliance)?
- Would a court or CPPA likely view this as a material violation?

Mark in Glass Box: `self_interrogation: PASS | REVISED | N/A`

---

## Confidence Scoring

Assign confidence levels to interpretive findings:

| Level        | Range     | Meaning                                       | Action                               |
| ------------ | --------- | --------------------------------------------- | ------------------------------------ |
| **Definite** | 0.95-1.0  | Clear regulatory text; no ambiguity           | State with confidence                |
| **High**     | 0.80-0.94 | Regulatory text clear; minor interpretation   | Brief caveat                         |
| **Probable** | 0.60-0.79 | Good arguments; reasonable minds could differ | State reasoning; note alternatives   |
| **Possible** | 0.40-0.59 | Genuinely uncertain; limited guidance         | Flag for counsel; present both sides |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative                       | Do not assert; flag [UNCERTAIN]      |

---

## Glass Box Audit Trail

Every CCPA ADMT compliance assessment MUST include this audit section:

```yaml
glass_box:
  skill_name: "legalcode-ccpa-admt-compliance"
  assessment_date: "[date]"
  organization: "[organization name or 'Not disclosed']"
  systems_assessed: "[number]"
  significant_decision_domains:
    - "[domain 1]"
    - "[domain 2]"
  compliance_deadline: "January 1, 2027"
  risk_assessment_deadline: "April 1, 2028"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  regulations_consulted:
    - "11 CCR 7200-7222 (ADMT) — [VERIFIED / VERIFY]"
    - "11 CCR 7150-7157 (Risk Assessments) — [VERIFIED / VERIFY]"
    - "Cal. Civ. Code 1798.100-1798.199 — [VERIFIED / VERIFY]"
  cppa_guidance_consulted:
    - "[Guidance document if any — VERIFIED / VERIFY]"
  findings_summary:
    compliant: "[number]"
    partial: "[number]"
    non_compliant: "[number]"
    critical: "[number]"
  self_interrogation: "PASS / REVISED / N/A"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[scope limitations]"
    - "[information gaps]"
    - "[assumptions made]"
  reviewer: "AI-assisted — requires qualified California legal counsel review"
```

---

## Anti-Patterns

What NOT to do in CCPA ADMT compliance:

1. **Treating ADMT as a future problem** — January 1, 2027 deadline requires significant implementation
   time. Starting late risks non-compliance.

2. **Conflating ADMT with all AI** — Not all AI is ADMT under CPRA. Basic computational tools and
   advisory systems with meaningful human oversight may not qualify. Over-scoping wastes resources;
   under-scoping creates compliance gaps.

3. **Generic pre-use notices** — "We use AI to improve your experience" fails the specificity
   requirement. Notices must describe specific purpose, logic, and outcomes.

4. **Single opt-out method** — Regulation requires at least two easy methods. Web form alone is
   insufficient.

5. **Burying opt-out in cookie banners** — CPPA has signaled this is not compliant. Opt-out must be
   prominent and easy to find.

6. **Requiring account creation to opt out** — Creates friction that may constitute dark pattern.
   Opt-out should be available without account.

7. **Ignoring GPC signals** — Global Privacy Control signals should be treated equivalently to
   explicit opt-out requests where applicable.

8. **No human alternative after opt-out** — If consumer opts out, business must provide meaningful
   human review alternative, not just refuse service.

9. **Human-in-the-loop theater** — Rubber-stamping AI recommendations without meaningful
   interpretation, analysis, or override authority does not constitute human review under 11 CCR 7001.

10. **Confusing opt-out processing timeline** — 15 business days is the maximum; "as soon as
    feasible" is the standard. Do not default to maximum.

11. **Failing to notify service providers** — Upon opt-out, business must notify service
    providers/contractors to cease ADMT processing. Forgetting downstream processors creates
    continued violation.

12. **Risk assessment as checkbox** — Risk assessments must include genuine benefit-risk analysis.
    If privacy risks outweigh benefits, processing must halt. Perfunctory assessments create liability.

13. **Neglecting training data documentation** — For ADMT trained on personal information, 11 CCR
    7153 requires specific documentation. Many organizations forget this requirement.

14. **One-time compliance** — ADMT compliance requires ongoing monitoring, 3-year risk assessment
    reviews, and annual CPPA submissions. Set-and-forget creates drift.

15. **Importing EU/Colorado requirements** — CPRA ADMT is California-specific. EU AI Act, Colorado
    SB 24-205, and NYC LL 144 have different requirements. Do not conflate jurisdictions.

16. **Skipping cross-functional coordination** — ADMT compliance requires Legal, IT, Product,
    Business, and Privacy working together. Siloed implementation fails.

17. **No testing of opt-out mechanisms** — Opt-out mechanisms must actually work. Many organizations
    implement but never test. Build testing into launch process.

18. **Delayed access request responses** — 10-day acknowledgment and 45-day response deadlines are
    firm. Building ADMT access into existing CCPA request workflows requires lead time.

19. **Overlooking vendor ADMT** — If vendors provide ADMT as service providers, business remains
    responsible for compliance. Vendor contracts must address ADMT obligations.

20. **Assuming advertising is excluded** — While advertising decisions are not "significant
    decisions," profiling for advertising may trigger separate disclosure requirements. Don't assume
    complete exemption.

---

## Writing Standards

Apply plain-language discipline to all output:

**For compliance documentation:**

- Plain language accessible to business stakeholders, not just lawyers
- Active voice: "The business must provide two opt-out methods"
- Specific: cite 11 CCR section numbers
- Actionable: each finding includes specific remediation steps

**For pre-use notices:**

- Consumer-friendly language (8th grade reading level)
- No legal jargon
- Concrete examples where helpful
- Accessible format

**Quality gates before delivery:**

1. Can a non-lawyer business stakeholder understand the executive summary?
2. Are all regulatory citations accurate and verifiable?
3. Is each finding actionable with specific remediation steps?
4. Are timelines clear and tied to regulatory deadlines?
5. Would CPPA view these disclosures as compliant?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- Search for current 11 CCR regulatory text and amendments
- Search for CPPA guidance documents and FAQs
- Search for California AG enforcement related to ADMT
- Search for CPPA enforcement actions and priorities
- Verify citations against authoritative sources
- Check for proposed rulemakings that may affect requirements
- Mark verified citations as VERIFIED in Glass Box

**Without legalcode-mcp:**

- Mark all regulatory citations with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Include prominent notice that all citations require independent verification
- Direct user to cppa.ca.gov and leginfo.legislature.ca.gov for verification
- Focus on structural compliance rather than interpretive certainty

---

## Multi-Jurisdiction Considerations

While this skill is California-specific, organizations subject to CPRA ADMT may also face:

**EU AI Act (Regulation 2024/1689)**

- Art. 27 FRIA for high-risk AI systems
- Art. 14 human oversight requirements
- Annex III high-risk categories overlap with CPRA significant decisions
- See `legalcode-ai-fundamental-rights-impact-assessment` and `legalcode-eu-ai-act-high-risk-compliance`

**Colorado SB 24-205 (effective June 30, 2026)**

- Pre-deployment impact assessment for consequential decisions
- Consumer notification and appeal rights
- NIST AI RMF or ISO 42001 safe harbor
- See `legalcode-algorithmic-impact-assessment`

**NYC Local Law 144**

- Annual bias audit for employment AEDTs
- Candidate notification requirements
- See `legalcode-algorithmic-impact-assessment`

**Federal (EEOC/CFPB/FTC)**

- Title VII adverse impact for employment ADMT
- ECOA adverse action for credit ADMT
- FTC Section 5 unfairness doctrine
- See `legalcode-algorithmic-impact-assessment`

For multi-jurisdiction AI governance, consider building a unified framework that satisfies California
CPRA ADMT and other applicable regimes simultaneously.

---

## Output Format Template

Structure the final deliverable as:

```markdown
# CCPA ADMT Compliance Assessment

**Organization**: [Name or "Not disclosed"]
**Assessment Date**: [Date]
**Compliance Deadline**: January 1, 2027
**Risk Assessment Deadline**: April 1, 2028
**Assessment Scope**: [Number] ADMT systems across [domains]

---

## Executive Summary

[2-3 paragraph summary of compliance posture, key gaps, and priority actions]

**Overall Compliance Status**: COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL

**Key Statistics**:

- Systems assessed: [N]
- Systems requiring ADMT compliance: [N]
- Compliant: [N]
- Partial: [N]
- Non-Compliant: [N]
- Critical: [N]

---

## ADMT Inventory and Scope Determination

| System     | ADMT?  | Significant Decision? | Domain   | Compliance Required |
| ---------- | ------ | --------------------- | -------- | ------------------- |
| [System 1] | Yes/No | Yes/No                | [Domain] | Yes/No              |
| [System 2] |        |                       |          |                     |

---

## Compliance Gap Analysis

### Pre-Use Notices (11 CCR 7220)

**Status**: COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL

[Analysis and findings]

### Opt-Out Mechanisms (11 CCR 7221)

**Status**: COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL

[Analysis and findings]

### Access Request Procedures (11 CCR 7222)

**Status**: COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL

[Analysis and findings]

### Human Review Alternative

**Status**: COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL

[Analysis and findings]

### Risk Assessments (11 CCR 7150-7157)

**Status**: COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL

[Analysis and findings]

### Privacy Policy Disclosures

**Status**: COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL

[Analysis and findings]

---

## Remediation Roadmap

### Tier 1 — Critical Path (IMMEDIATE)

| Item | Gap | Remediation | Owner | Deadline |
| ---- | --- | ----------- | ----- | -------- |
|      |     |             |       |          |

### Tier 2 — Compliance Deadline (January 1, 2027)

| Item | Gap | Remediation | Owner | Deadline |
| ---- | --- | ----------- | ----- | -------- |
|      |     |             |       |          |

### Tier 3 — Governance Foundation (April 1, 2028)

| Item | Gap | Remediation | Owner | Deadline |
| ---- | --- | ----------- | ----- | -------- |
|      |     |             |       |          |

---

## Deliverable Attachments

1. Pre-Use Notice Templates (Attachment A)
2. Opt-Out Mechanism Specifications (Attachment B)
3. Access Request Procedure SOP (Attachment C)
4. Risk Assessment Template (Attachment D)
5. Privacy Policy Redlines (Attachment E)

---

## Glass Box Audit Trail

[YAML block per Glass Box section]

---

## Next Steps

1. [Specific action with owner and deadline]
2. [Specific action with owner and deadline]
3. [Specific action with owner and deadline]

---

## Disclaimer

This assessment is AI-assisted and does not constitute legal advice. All findings require review
by qualified California legal counsel before implementation. Regulatory requirements are current
as of the assessment date; verify against CPPA.ca.gov for updates.
```

---

## Localization Notes

This skill is California-specific by design. It should NOT be localized for other jurisdictions.

For other jurisdictions, use:

- **EU**: `legalcode-ai-fundamental-rights-impact-assessment`, `legalcode-eu-ai-act-high-risk-compliance`
- **Colorado**: `legalcode-algorithmic-impact-assessment` (Colorado SB 24-205 coverage)
- **NYC**: `legalcode-algorithmic-impact-assessment` (NYC LL 144 coverage)
- **Multi-jurisdiction**: `legalcode-algorithmic-impact-assessment` (consolidated framework)

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis based on:

- California Consumer Privacy Act, as amended by CPRA (Cal. Civ. Code 1798.100-1798.199.100)
- CPPA Final Regulations effective January 1, 2026 (11 CCR 7000+)
- Article 10: Risk Assessments (11 CCR 7150-7157)
- Article 11: Automated Decisionmaking Technology (11 CCR 7200-7222)
- CPPA enforcement guidance and priorities (as of March 2026)
- Cross-reference with EU AI Act, Colorado SB 24-205, NYC LL 144 for multi-jurisdiction context

Research conducted via Perplexity search for current regulatory status, effective dates, and
enforcement context. All citations should be verified against CPPA.ca.gov and California Legislative
Information before implementation.
