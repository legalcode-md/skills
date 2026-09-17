---
name: legalcode-coppa-compliance-assessment
description: COPPA compliance assessment for operators of websites and online services directed to children
  or with actual knowledge of child users. Use when a website operator, app developer, EdTech platform,
  gaming company, streaming service, or AdTech provider needs to determine COPPA compliance posture, prepare
  for FTC inquiry, assess a product or feature for child- audience risk, build a COPPA compliance program
  from scratch, respond to a parental complaint, or evaluate compliance with the 2025 amendments ahead
  of the April 2026 deadline.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

COPPA compliance assessment for operators of websites and online services directed to children or with actual knowledge of child users. Covers the Children's Online Privacy Protection Act (15 U.S.C. §§ 6501–6506) and the FTC's COPPA Rule (16 C.F.R. Part 312), including the 2025 amendments (effective June 23, 2025; compliance deadline April 22, 2026). Assesses all five operator obligation domains: (1) privacy notice requirements including new retention disclosure mandate; (2) direct notice to parents; (3) verifiable parental consent (VPC) including all 10 approved methods and new separate consent for third-party sharing, targeted advertising, and AI training; (4) parental access and deletion rights; and (5) children's data security including the new written information security program requirement. Covers operator applicability determination (directed-to- children multi-factor test + actual knowledge standard + mixed-audience platform rules), expanded PII definitions (biometric identifiers, government-issued identifiers, mobile phone numbers), data minimization and retention limits, safe harbor programs (CARU, kidSAFE, ESRB, iKeepSafe, TRUSTe, PRIVO), third-party SDK and vendor liability, and state children's privacy law overlay (California AADC, Texas SCOPE Act, Utah CSPA, Colorado, Connecticut, Maryland Kids Code). Produces COMPLIANT/PARTIAL/NON-COMPLIANT/ CRITICAL DEFICIENCY assessments with remediation roadmaps, FTC enforcement exposure estimates, and Glass Box audit trail. Use when a website operator, app developer, EdTech platform, gaming company, streaming service, or AdTech provider needs to determine COPPA compliance posture, prepare for FTC inquiry, assess a product or feature for child- audience risk, build a COPPA compliance program from scratch, respond to a parental complaint, or evaluate compliance with the 2025 amendments ahead of the April 2026 deadline.


# COPPA Compliance Assessment

> **Disclaimer**: This skill provides an AI-assisted framework for assessing compliance
> with the Children's Online Privacy Protection Act of 1998 (15 U.S.C. §§ 6501–6506) and
> the FTC's COPPA Rule (16 C.F.R. Part 312), including the 2025 amendments. It does not
> constitute legal advice, regulatory guidance, or a compliance certification. COPPA
> requirements and FTC enforcement guidance evolve — verify all statutory references,
> regulatory thresholds, and penalty figures against current FTC guidance and CFR text
> before relying on them. AI-generated legal analysis carries hallucination risk for cited
> authority: any statutory citations, FTC guidance references, safe harbor program details,
> or enforcement interpretations should be independently verified by a qualified attorney
> with children's privacy expertise before use. This skill does not certify COPPA
> compliance; it produces a structured framework to support a human-led compliance review.

## Purpose and Scope

This skill assesses an operator's compliance posture under COPPA and the 2025 amended
COPPA Rule, from initial applicability determination through remediation planning.

**Covers:**

- Operator applicability determination (directed-to-children test, actual knowledge
  standard, mixed-audience platform analysis)
- Expanded personal information definitions under the 2025 amendments (biometric
  identifiers, government-issued identifiers, mobile phone numbers for VPC)
- Privacy notice requirements: home-page posting, per-collection-point notice, new
  retention timeline disclosure, third-party categories disclosure
- Direct notice to parents before data collection
- Verifiable parental consent (VPC): all 10 approved methods, method adequacy for use
  case, neutral age-screen requirements, separate consent for third-party sharing /
  targeted advertising / AI training
- Data minimization and written retention policy requirements (new 2025)
- Written children's data security program requirements (new 2025)
- Parental access and deletion rights: review, correction, deletion, opt-out workflow
- Third-party SDK, analytics, and ad network liability exposure
- Safe harbor programs: CARU, kidSAFE, ESRB, iKeepSafe, TRUSTe, PRIVO — benefits and
  certification workflow
- State children's privacy law overlay: California AADC, Texas SCOPE Act, Utah CSPA,
  Colorado, Connecticut, Maryland Kids Code, Nebraska, Vermont
- FTC civil penalty exposure modeling (current maximum: $53,088 per violation per day)
- Remediation roadmap with IMMEDIATE / NEAR-TERM / BACKGROUND prioritization

**Does not:**

- Certify COPPA compliance — only a qualified attorney or accredited auditor can certify
- Constitute a Safe Harbor program audit — those require submission to CARU, kidSAFE, or
  another FTC-approved program
- Provide legal opinions on specific FTC investigation strategy or litigation exposure
- Assess FERPA compliance for K-12 educational institutions in full depth — FERPA
  intersects with COPPA for EdTech but requires its own specialized analysis
- Analyze non-US children's privacy regimes (e.g., GDPR Article 8, UK Children's Code,
  Canada PIPEDA/Bill C-27) — those require separate skills
- Apply the assessment to adults-only platforms with no child-audience connection

**Related skills:**

- `legalcode-ccpa-admt-compliance` — California Consumer Privacy Act and Automated
  Decision-Making Technology; use when assessing CCPA obligations alongside COPPA
- `legalcode-us-breach-notification-triage` — all 50 states + federal overlays; use when
  determining breach notification obligations for a children's data breach
- `legalcode-vendor-privacy-assessment` — TPRM framework; use when auditing third-party
  SDK and vendor COPPA compliance as part of broader vendor due diligence
- `legalcode-data-mapping-workflow` — data inventory; use to map children's data flows
  before this assessment if no prior inventory exists
- `legalcode-consent-mechanism-review` — consent UX analysis; use to evaluate the VPC
  mechanism's design for manipulative patterns or neutral-screen compliance
- `legalcode-advertising-marketing-compliance` — FTC Act § 5 advertising compliance;
  use when assessing child-directed advertising on top of COPPA obligations
- `legalcode-privacy-policy-drafter` — privacy notice drafting; use after this assessment
  to draft or update the operator's COPPA-compliant privacy notice

---

## Jurisdiction and Governing Law

**Primary legislation**: Children's Online Privacy Protection Act of 1998, Pub. L. 105-277,
Title XIII, §§ 1301–1312, codified at 15 U.S.C. §§ 6501–6506.

**Primary regulation**: Children's Online Privacy Protection Rule, 16 C.F.R. Part 312.

**2025 Amendments** (the assessment covers these throughout):

- Final Rule published: April 22, 2025 (Federal Register)
- Effective date: June 23, 2025
- General compliance deadline: April 22, 2026 (one year from publication)
- Safe harbor program updated guidelines submission deadline: October 22, 2025
- Safe harbor program public member list publication deadline: July 21, 2025

**Enforcement authority**: Federal Trade Commission (FTC), acting under Section 5 of the
FTC Act (15 U.S.C. § 45) and 15 U.S.C. § 6502(c). State attorneys general may also bring
civil actions under 15 U.S.C. § 6504.

**Civil penalty authority**: FTC Act § 5(l); maximum penalty per violation per day is
$53,088 (2025 inflation-adjusted figure) [VERIFY current adjusted figure at
ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/civil-penalty-amounts].
Each child whose data is unlawfully collected or used may constitute a separate violation.

**COPPA preemption**: COPPA expressly preempts inconsistent state laws (15 U.S.C.
§ 6502(d)), but does NOT preempt consistent or more stringent state children's privacy
protections. Multiple states have enacted laws going substantially beyond COPPA.

**US-only scope**: COPPA applies to operators subject to US FTC Act jurisdiction.
Non-US operators serving US children face COPPA jurisdiction based on US user base.

---

## Interactive Clarification

This skill uses **⟁ CLARIFY** markers at key decision points. When you encounter a CLARIFY
marker, pause and ask the user the structured questions shown. Only ask when the answer
will materially change the analysis. If the user has already provided the information,
skip the question and proceed.

**Standard clarification format:**

```
⟁ CLARIFY — [Decision point name]

[Short context: why this question matters]

1. [Option A]: [Description]
2. [Option B]: [Description]
3. [Option C]: [Description]

**Why this matters**: [One sentence on how the answer changes the analysis direction]
```

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:

- **Organization description**: Operator name, type of website/service/app, target
  audience description, age of typical users, types of data collected, existing consent
  mechanisms, states of operation
- **Document set**: Privacy policy, terms of service, VPC workflow screenshots, data flow
  diagrams, retention schedule, security policies, vendor agreements, any prior FTC inquiry
- **Assessment trigger**: Routine annual review, product launch review, response to
  parental complaint, FTC inquiry preparation, 2025 amendment gap assessment
- **Feature or product**: A specific new feature or product requiring COPPA analysis before
  launch (e.g., a new account registration flow, a new data collection point, a new SDK
  integration, an AI feature trained on user data)

**Minimum required context**: Platform type (website, mobile app, gaming platform, EdTech,
IoT, connected toy, streaming service, social media, advertising network), description of
intended user base including approximate age range, and types of personal information
collected from or about users.

### Step 2: Gather Context

**⟁ CLARIFY** — Gather context before beginning. Ask all questions not already answered:

1. **Assessment mode**: What is the primary objective?
   - _Full COPPA compliance assessment_: All five obligation domains, applicability gate,
     safe harbor analysis, state law overlay — comprehensive baseline or annual review
   - _2025 amendment gap analysis_: Focused on what changed (biometric PII, separate
     third-party consent, retention policy, written security program, new VPC methods,
     new privacy notice content requirements) vs. what the operator already has
   - _Operator applicability determination only_: Assess whether COPPA applies; stop if
     the operator is clearly out of scope
   - _Pre-launch product review_: Rapid COPPA risk screen for a new feature or product
     before deployment
   - _VPC mechanism review_: Deep assessment of the consent mechanism, age-screen design,
     and method adequacy
   - _FTC inquiry preparation_: Compliance posture documentation for a potential or
     pending FTC investigation
   - **Why this matters**: Scope controls depth, output format, and priority of findings.

2. **Operator type**: What type of online service is this?
   - _Consumer website or app (general-purpose)_: Social media, search, lifestyle, news
   - _Directed-to-children website or app_: Content, entertainment, or services designed
     primarily for children under 13
   - _Mixed-audience platform_: Service appealing to both children and adults (gaming,
     streaming, social media, content platforms)
   - _EdTech platform_: Educational technology serving K-12 schools and students
   - _Connected toy / IoT device_: Hardware product with online services (smart speakers,
     interactive toys, wearables)
   - _AdTech / data broker_: Third-party data collector operating through other sites
   - _App store or distribution platform_: Distribution platform for child-directed apps
   - **Why this matters**: Operator type determines applicability path and which compliance
     elements are most material (e.g., IoT has unique VPC delivery challenges; EdTech
     involves school-as-agent exception; AdTech creates third-party operator liability).

3. **Data collection profile**: What personal information is collected?
   - Select all that apply: Name, email address, phone number, home/physical address,
     geolocation, persistent identifier (cookie/device ID/IP address), photo/video/audio,
     username that functions as contact, biometric identifier (NEW 2025), government-issued
     ID number (NEW 2025), health data, financial information, user-generated content
   - **Why this matters**: The 2025 amendments expanded the PII definition significantly;
     operators who previously did not collect "personal information" under the old rule
     may now be in scope with biometric or government-ID collection.

4. **Existing compliance posture**: What is currently in place?
   - _No COPPA program_: No privacy notice, no VPC mechanism, no age screen — starting
     from scratch
   - _Legacy program (pre-2025 amendments)_: Compliant with the 2013 rule but not yet
     updated for the 2025 amendments
   - _Partial program_: Some elements in place (e.g., privacy notice exists but no VPC
     for third-party sharing; retention policy exists but not written or published)
   - _Mature program_: Comprehensive COPPA compliance program; seeking gap analysis
     against the 2025 amendments or preparing for FTC scrutiny
   - _Safe harbor member_: Currently participating in CARU, kidSAFE, ESRB, or another
     approved program; seeking review against updated safe harbor guidelines
   - **Why this matters**: Assessment depth and remediation framing differ substantially
     between a greenfield build and an amendment-gap analysis.

5. **Third-party data sharing profile**: Are any of these present?
   - Third-party analytics SDKs (Google Analytics, Amplitude, Mixpanel, etc.)
   - Advertising SDKs or ad networks serving targeted advertising
   - Social media login or share buttons
   - AI/ML vendors receiving user data for model training
   - Data brokers or data resellers receiving children's data
   - Payment processors
   - Cloud hosting providers (acting as service providers)
   - **Why this matters**: The 2025 amendments require separate VPC for any third-party
     data sharing other than service providers integral to the core service. Each SDK
     creating a separate data flow is a potential standalone COPPA violation.

6. **State law scope**: Which states are users based in, or where is the service marketed?
   - _California_: AADC (under active litigation — largely enjoined — [VERIFY current
     status]; CCPA minor provisions)
   - _Texas_: SCOPE Act (effective July 1, 2024 — social interaction services)
   - _Utah_: Child and Teen Safety Act / Minor Protection Act (parental consent for account
     creation; curfew provisions)
   - _Connecticut_: 2024 amendments prohibiting targeted advertising to minors regardless
     of consent; prohibiting engagement-maximizing features
   - _Colorado_: 2024 amendments to CPA — heightened minor protections
   - _Maryland_: Kids Code (effective October 1, 2024 — default privacy; geolocation ban)
   - _Nebraska / Vermont_: Age-Appropriate Design Code Acts (2025)
   - _All states or unclear_: Assess federal COPPA only; flag most stringent state laws
     for separate review
   - **Why this matters**: State children's privacy laws go significantly beyond COPPA for
     teens (ages 13-17); operators with broad US user bases face layered obligations.

### Step 3: Gather Legal Authority

Before assessing, gather current authority to ensure the assessment reflects current law:

**With legalcode-mcp connected:**

- Search: "COPPA 16 CFR Part 312 2025 amendments final rule" — verify current rule text
- Search: "FTC COPPA enforcement actions 2024 2025 civil penalties" — verify recent cases
- Search: "FTC COPPA verifiable parental consent methods 2025" — verify approved methods
- Search: "COPPA safe harbor programs CARU kidSAFE 2025 updated guidelines" — verify SHP
  status
- Search: "[State] children's online privacy law 2024 2025" — verify state law status
- Save results to `/tmp/coppa-assessment-research.md`
- Mark all verified citations as VERIFIED in Glass Box

**Without legalcode-mcp:**

- Proceed with rule text from training data; mark all penalty figures and citation-specific
  items [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Particularly flag [VERIFY] on:
  - Current inflation-adjusted civil penalty amount per violation per day
  - 2025 amendment compliance deadline (April 22, 2026 absent further FTC action)
  - California AADC injunction status (was largely enjoined as of early 2026)
  - Safe harbor program updated guideline submission and approval status
  - State law enactments after August 2025 (knowledge cutoff)
  - Status of any pending FTC rulemakings or guidance documents

### Step 4: Operator Applicability Gate

**BINARY GATE — Apply before assessing any compliance obligations.**

This step determines whether COPPA applies to the operator. If the operator is clearly
outside scope, issue a determination and stop. If in scope, identify the applicable
coverage path before proceeding.

#### 4a. "Operator" Definition (16 C.F.R. § 312.2)

COPPA applies to an "operator" defined as a person who:

1. Operates a commercial website or online service directed to children; OR
2. Operates any commercial website or online service and has **actual knowledge** that it
   is collecting personal information from a child under 13.

**Threshold question**: Is this entity commercial in nature? Nonprofit organizations are
generally outside COPPA's scope unless the FTC determines they are commercial in character
and have children as a primary audience. [VERIFY current FTC guidance on nonprofit scope]

#### 4b. "Directed to Children" — Multi-Factor Test (16 C.F.R. § 312.2)

Apply the totality-of-circumstances test using all factors below. No single factor is
determinative. A "yes" on multiple factors strongly indicates directed-to-children status.

| Factor                                                                                 | Yes | No  | Notes |
| -------------------------------------------------------------------------------------- | --- | --- | ----- |
| Subject matter of the site or service targets children                                 |     |     |       |
| Visual content uses animated characters, cartoons, or child-oriented imagery           |     |     |       |
| Child-oriented activities or incentives (games, prizes, stickers, badges)              |     |     |       |
| Music or audio content appeals primarily to children                                   |     |     |       |
| Age of models/avatars depicted is predominantly child-apparent                         |     |     |       |
| Child celebrities or celebrities who appeal to children are featured                   |     |     |       |
| Advertising or marketing directed at children appears on the site                      |     |     |       |
| **2025 NEW**: Marketing or promotional materials represent the service as for children |     |     |       |
| **2025 NEW**: Representations to consumers or third parties indicate child audience    |     |     |       |
| **2025 NEW**: Reviews by users or third parties reflect child usage                    |     |     |       |
| **2025 NEW**: Age of users on similar services indicates child audience                |     |     |       |
| Competent empirical evidence shows children constitute a substantial portion of users  |     |     |       |

**Result classification:**

- **Clearly directed to children**: 6+ "yes" factors, or subject matter is inherently for
  children (children's educational content, interactive toy, kids' game). COPPA applies to
  ALL users — treat all users as potentially under 13 or use age-screening to segment.
- **Possibly directed to children**: 2–5 "yes" factors. Apply CLARIFY with user before
  concluding. Consider whether the service is a "mixed-audience" platform.
- **General audience**: 0–1 "yes" factors and no content specifically targeted at children.
  COPPA does not apply unless actual knowledge is obtained. Document this determination.

**⟁ CLARIFY** — When the directed-to-children determination is unclear (2–5 factors),
ask:

1. Has the operator conducted a user research study or audience measurement showing the
   actual age composition of its users?
2. Has the operator or its marketing team described the service as appropriate for or
   targeted at children in any external communication, pitch deck, or investor materials?
3. Has the operator received parental complaints or queries suggesting children are users?
   **Why this matters**: A borderline determination materially changes compliance scope — a
   directed-to-children finding triggers strict liability for all users; actual-knowledge
   only means COPPA attaches upon knowledge of each child.

#### 4c. "Actual Knowledge" Standard (16 C.F.R. § 312.2)

For general-audience services, COPPA applies when the operator has actual knowledge of a
child under 13. Document whether any of these actual knowledge triggers are present:

| Knowledge Trigger                                                                  | Present? | Notes |
| ---------------------------------------------------------------------------------- | -------- | ----- |
| Age gate or registration form returned date of birth indicating user is under 13   |          |       |
| User explicitly stated age under 13 in a profile, chat message, or support inquiry |          |       |
| Parent or guardian contacted operator reporting child uses the service             |          |       |
| Registration question responses imply age under 13 (e.g., grade level in school)   |          |       |
| Staff member personally observed or was informed the user is under 13              |          |       |

**If actual knowledge is found**: COPPA obligations attach immediately for that child.
Assess whether the operator has collected personal information from that child without
VPC. If yes, this is a CRITICAL DEFICIENCY regardless of platform type.

#### 4d. Mixed-Audience Platform Analysis (16 C.F.R. § 312.2(b))

If the service is directed to children but does NOT target children as its primary
audience (a "mixed-audience website or online service"), the operator may use age
screening to differentiate users:

**Permissible approach:**

1. Operator age-screens all users at the point of personal information collection
2. Age screen is **neutral** — no pre-populated fields, no default adult selection, no
   visual cues that nudge toward declaring an adult age, no immediate rewards for being
   over 13
3. Before the age screen, operator collects only the **minimum** personal information
   needed solely for age estimation — no other personal information may be collected
4. Users under 13 are routed to a child-protective flow with full COPPA compliance
5. Users 13 and over proceed to normal data collection under standard privacy standards

**Age-screen neutrality audit:**

- [ ] No pre-populated birth year or age selection (defaults to "over 13")
- [ ] No immediate reward, accelerated flow, or visual encouragement for selecting "over 13"
- [ ] Child-identification screen is not designed to be easily circumvented
- [ ] No year-of-birth selection that makes child-age selection cumbersome (e.g., only
      scroll back through 80 years of calendar options)
- [ ] Knowledge-based questions (if used) supplement, not replace, direct age inquiry

**OUT OF SCOPE result**: If the operator is a general-audience service with no actual
knowledge triggers, issue a determination of COPPA NOT CURRENTLY APPLICABLE with a note
on what would create applicability, and stop. Document the determination.

### Step 5: Core Obligation Domain Assessment

Assess each of the five COPPA obligation domains. For each domain, evaluate the current
state and assign a classification:

| Classification          | Criteria                                                                                                               |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **COMPLIANT**           | Requirement fully met; documented; no material gaps                                                                    |
| **PARTIAL**             | Requirement partially met; material gaps identified; remediation needed                                                |
| **NON-COMPLIANT**       | Requirement not met; clear COPPA violation; requires prompt remediation                                                |
| **CRITICAL DEFICIENCY** | Complete absence of required element, or active ongoing violation; highest enforcement risk; IMMEDIATE action required |
| **N/A**                 | Requirement does not apply given operator's specific data practices                                                    |

---

#### Domain 1: Privacy Notice Requirements (16 C.F.R. § 312.4)

**Requirement**: Post a clearly and understandably written privacy notice on the home page
and at each area where personal information is collected from children. The notice must
meet all content requirements.

**1a. Privacy Notice Posting Locations**

| Requirement                                                                          | Status | Finding |
| ------------------------------------------------------------------------------------ | ------ | ------- |
| Notice posted on **home page** of the website or main landing page of the service    |        |         |
| Notice posted **at each area** where personal information is collected from children |        |         |
| Notice is **clearly and understandably written** (plain language, not legalese)      |        |         |
| Notice is **complete** (contains all required content — see 1b below)                |        |         |
| Link is prominently placed (not buried in site-wide footer in small type)            |        |         |

**1b. Required Privacy Notice Content (16 C.F.R. § 312.4(d))**

| Content Element                                                                                                                                                                             | Present? | Accurate? | Notes |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------- | ----- |
| **Operator identification**: name and contact info of all operators collecting PI from children using the site                                                                              |          |           |       |
| **PI categories collected**: complete and accurate list of all personal information collected                                                                                               |          |           |       |
| **Uses of PI**: how each category of PI is used                                                                                                                                             |          |           |       |
| **Third-party categories** (**2025 NEW**): whether PI is disclosed to third parties and the specific categories of third parties receiving PI                                               |          |           |       |
| **Retention policy** (**2025 NEW**): how long each category of PI is retained (specific timeline required; "as long as necessary" is insufficient)                                          |          |           |       |
| **VPC mechanism**: description of how parents can provide VPC or, for existing programs, how parents can review and delete PI and refuse further collection                                 |          |           |       |
| **Parental rights notice**: explicit statement of parental review, correction, and deletion rights and how to exercise them                                                                 |          |           |       |
| **No condition on participation**: notice that the operator may not condition a child's participation in an activity on disclosure of more PI than reasonably necessary (16 C.F.R. § 312.7) |          |           |       |

**2025 Gap Focus**: The two new content requirements — third-party categories and retention
timeline — are the most likely gaps for operators with pre-2025 privacy notices. Even
well-compliant operators must update their notices to add these elements before April 22, 2026.

**Domain 1 Classification**: Assign COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY

---

#### Domain 2: Direct Notice to Parents (16 C.F.R. § 312.4(b)–(c))

**Requirement**: Before collecting, using, or disclosing personal information from a child,
make reasonable efforts to provide direct notice to the child's parent.

**2a. Timing of Direct Notice**

| Requirement                                                                                                                                      | Status | Notes |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------ | ----- |
| Direct notice sent **before** or **at the time** personal information collection begins                                                          |        |       |
| Notice is sent directly to the **parent** (not only to the child)                                                                                |        |       |
| Notice method is reasonably calculated to reach the actual parent (email is standard; must be deliverable to parent, not just the child's inbox) |        |       |

**2b. Required Direct Notice Content (16 C.F.R. § 312.4(b))**

| Content Element                                                                                                                                      | Present? | Notes |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ----- |
| Operator name and contact information                                                                                                                |          |       |
| What personal information will be collected from the child                                                                                           |          |       |
| How the personal information will be used                                                                                                            |          |       |
| Whether PI will be disclosed to third parties                                                                                                        |          |       |
| **2025 NEW**: Categories of third parties that will receive PI                                                                                       |          |       |
| Statement that parental consent is required before collection (or, for internal-operations-only collection, description of the lighter process used) |          |       |
| How the parent can provide VPC                                                                                                                       |          |       |
| How the parent can review and request deletion of the child's PI                                                                                     |          |       |

**2c. No-Contact Exceptions (16 C.F.R. § 312.5(c))**

Identify which exceptions to the pre-collection parental contact requirement apply, if any:

| Exception                                                                                                                                          | Applicable? | Operator Practice |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------- |
| **One-time request exception**: Online contact info collected once to respond to child's one-time specific request; no retention or further use    |             |                   |
| **Newsletter exception**: Online contact info to provide newsletter with parent notification and opt-out opportunity                               |             |                   |
| **Child safety exception**: Name and online contact info collected to protect child safety, with parent notification and opt-out opportunity       |             |                   |
| **Internal operations only (persistent identifier)**: Persistent ID collected solely for internal operations; no third-party sharing; no profiling |             |                   |
| **School-as-agent exception (EdTech)**: School provides VPC on parents' behalf for educational purposes only (no commercial use)                   |             |                   |

**Domain 2 Classification**: COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY

---

#### Domain 3: Verifiable Parental Consent (VPC) (16 C.F.R. § 312.5)

**Requirement**: Before collecting, using, or disclosing personal information from children
(beyond limited exceptions), obtain verifiable parental consent using an FTC-approved
method appropriate to the data's intended use.

**3a. VPC Method Adequacy**

Assess whether the operator's VPC method is (a) on the FTC-approved list and (b)
appropriate for the use case:

| Approved VPC Method                                                                                                                                               | Operator Uses? | Appropriate for Use Case? |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------- |
| **Print-and-sign / mail or fax**: Parent signs consent form and returns by mail, fax, or electronic scan                                                          |                |                           |
| **Credit/debit card or other payment transaction** (amended 2025 — no longer requires monetary transaction)                                                       |                |                           |
| **Video conference**: Trained operator personnel confirms parent identity in real time                                                                            |                |                           |
| **Government photo ID check**: Operator verifies government-issued photo ID against parent info; ID deleted promptly after verification                           |                |                           |
| **Email plus** (internal operations only): Email + confirmation via return email, letter, or phone call                                                           |                |                           |
| **Electronic signature with identity verification**                                                                                                               |                |                           |
| **Facial recognition + government ID** (**NEW 2025**): Facial recognition + human review matching live image to government photo ID; both images deleted promptly |                |                           |
| **Knowledge-based authentication (KBA)** (**NEW 2025**): Dynamic, multiple-choice questions difficult for a child under 13 to answer correctly                    |                |                           |
| **Text plus** (**NEW 2025**): Text message to parent's mobile phone + confirmation response                                                                       |                |                           |

**Method adequacy matrix:**

| Use Case                                                         | Email Plus Sufficient?     | Higher-Reliability Method Required?          |
| ---------------------------------------------------------------- | -------------------------- | -------------------------------------------- |
| Internal operations only (persistent ID; no third-party sharing) | Yes                        | No                                           |
| General data collection and service delivery                     | Yes (email + confirmation) | No, but higher-reliability is best practice  |
| Third-party sharing for advertising                              | **No**                     | **Yes** — higher-reliability method required |
| Third-party data sales or data brokerage                         | **No**                     | **Yes**                                      |
| AI model training using children's data                          | **No**                     | **Yes** — separate consent required          |
| Disclosure to third parties not integral to service              | **No**                     | **Yes**                                      |

**3b. Age-Screen Neutrality Review** (for mixed-audience operators)

Apply the neutrality criteria from Step 4d and assign finding here.

**3c. Separate Consent for Third-Party Sharing (2025 NEW — 16 C.F.R. § 312.5(a)(1)(ii))**

**This is the highest-impact 2025 amendment for most operators.**

The 2025 amendments require a **separate and distinct consent event** before disclosing
children's personal information to any third party whose receipt of the data is NOT
integral to the core service. The FTC expressly ruled that the following are **never**
integral and therefore **always** require separate consent:

| Use                                                                                           | Requires Separate VPC? | Notes                                                 |
| --------------------------------------------------------------------------------------------- | ---------------------- | ----------------------------------------------------- |
| Targeted advertising                                                                          | **YES — always**       | Cannot be bundled with general consent                |
| Behavioral advertising based on cross-site tracking                                           | **YES — always**       |                                                       |
| Monetary compensation (data sale or data brokerage)                                           | **YES — always**       |                                                       |
| Developing or training AI / ML technologies                                                   | **YES — always**       |                                                       |
| Other third-party data sharing not integral to service                                        | **YES**                | Assess integrality case-by-case                       |
| Disclosure to service providers integral to delivering the service (e.g., cloud hosting, CDN) | No                     | Must be genuinely integral; apply narrow construction |

**Consent bundling audit**: Review the VPC flow and determine whether:

- [ ] The consent for third-party sharing is presented separately from general service consent
- [ ] The parent can consent to the service without consenting to third-party sharing for advertising or AI training
- [ ] The consent form or screen clearly identifies the categories of third parties
- [ ] The VPC method used for third-party sharing is a higher-reliability method

**3d. Consent Record Retention**

| Requirement                                                                                         | Status | Notes |
| --------------------------------------------------------------------------------------------------- | ------ | ----- |
| VPC records are retained in accessible, auditable form                                              |        |       |
| Records document: which method was used, date of consent, parent identity basis                     |        |       |
| Records are retained for the period during which the child's data is held + reasonable period after |        |       |

**Domain 3 Classification**: COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY

**Auto-CRITICAL DEFICIENCY triggers for Domain 3:**

- No VPC mechanism in place and operator is directed to children or has actual knowledge
- VPC mechanism in place but email-plus used for targeted advertising or AI training
- Consent bundled in ToS click-through without separate parent interaction
- Age-screen designed to steer users toward declaring age over 13

---

#### Domain 4: Parental Access and Deletion Rights (16 C.F.R. § 312.6)

**Requirement**: Provide a mechanism for parents to exercise their rights to review,
correct, and delete their child's personal information, and to refuse further collection.

**4a. Parental Access Rights**

| Right                                                                                                                                                                                                                      | Mechanism Exists? | Adequacy Notes |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | -------------- |
| **Right to review**: Parent can review PI the operator has collected from their child                                                                                                                                      |                   |                |
| **Right to correction**: Parent can correct inaccuracies in child's PI                                                                                                                                                     |                   |                |
| **Right to deletion**: Parent can request deletion of child's PI; operator must comply and direct service providers to delete                                                                                              |                   |                |
| **Right to opt out**: Parent can refuse permission for further collection or use of child's PI                                                                                                                             |                   |                |
| **Right to refuse third-party sharing**: Parent can refuse consent to any disclosure to third parties while allowing the child to continue using the service (where the service is not conditioned on third-party sharing) |                   |                |

**4b. Parent Identity Verification for Rights Requests**

| Requirement                                                                                                | Status | Notes |
| ---------------------------------------------------------------------------------------------------------- | ------ | ----- |
| Operator uses a reasonable method to verify the requestor is actually the child's parent or legal guardian |        |       |
| Verification method is not so burdensome that it effectively deprives parents of their rights              |        |       |
| Verification does not require more PI than necessary for verification                                      |        |       |

**4c. Deletion Completeness**

The Amazon Alexa enforcement action confirmed that deletion must be complete across all
systems, including backup and secondary storage. Assess:

| Requirement                                                                                                  | Status | Notes |
| ------------------------------------------------------------------------------------------------------------ | ------ | ----- |
| Deletion workflow covers **all primary databases** and data stores                                           |        |       |
| Deletion extends to **backup, archive, and secondary storage** systems                                       |        |       |
| Deletion workflow reaches **service providers and third-party processors** that have received the child's PI |        |       |
| Operator has documented confirmation process to verify deletion was completed                                |        |       |
| Response time to parental deletion requests is reasonable (FTC practice: 30 days or less)                    |        |       |

**4d. No Conditioning on PI Disclosure (16 C.F.R. § 312.7)**

| Requirement                                                                                                                                            | Status | Notes |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ | ----- |
| Operator does not condition a child's participation in any activity on disclosure of more PI than reasonably necessary to participate in that activity |        |       |

**Domain 4 Classification**: COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY

---

#### Domain 5: Children's Data Security and Integrity (16 C.F.R. § 312.8)

**Requirement**: Establish and maintain reasonable procedures to protect the
confidentiality, security, and integrity of children's personal information. The 2025
amendments added explicit requirements for a written information security program.

**5a. Written Information Security Program (NEW 2025 — 16 C.F.R. § 312.8(b))**

| Requirement                                                                                                                               | Status | Notes |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------ | ----- |
| **Documented program**: Written children's PI security program exists                                                                     |        |       |
| **Program ownership**: Designated personnel responsible for coordinating the program                                                      |        |       |
| **Annual risk assessment**: At least annual identification and assessment of internal and external risks to the security of children's PI |        |       |
| **Safeguard implementation**: Safeguards implemented to address identified risks (technical, administrative, physical)                    |        |       |
| **Testing and monitoring**: Safeguards regularly tested and monitored for effectiveness                                                   |        |       |
| **Annual review**: Program evaluated and modified at least annually based on testing and operational changes                              |        |       |
| **Scalability**: Program is scaled to the operator's size, complexity, and business activities                                            |        |       |

**5b. Third-Party Security Assurances (16 C.F.R. § 312.8(c))**

| Requirement                                                                                                                                                                          | Status | Notes |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ | ----- |
| Before disclosing children's PI to service providers or third parties, operator takes reasonable steps to verify the recipient can maintain confidentiality, security, and integrity |        |       |
| Operator obtains **written assurances** from third parties committing to reasonable security measures for children's PI                                                              |        |       |
| Written assurances cover all categories of service providers receiving children's PI                                                                                                 |        |       |
| Operator retains copies of written assurances in accessible form                                                                                                                     |        |       |

**5c. Baseline Security Controls**

| Control Area                                                                          | In Place? | Notes |
| ------------------------------------------------------------------------------------- | --------- | ----- |
| Access controls limiting employee access to children's PI to those with business need |           |       |
| Encryption of children's PI in transit                                                |           |       |
| Encryption of children's PI at rest (especially biometric and government-ID data)     |           |       |
| Audit logging of access to children's PI                                              |           |       |
| Incident response plan covering children's PI breaches                                |           |       |
| Vendor agreements requiring COPPA-compliant security measures                         |           |       |

**Domain 5 Classification**: COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY

**Auto-CRITICAL DEFICIENCY triggers for Domain 5:**

- No written information security program and operator has active children's PI collection
- No vendor/third-party security assurances for any third party receiving children's PI

---

#### Domain 6: Data Minimization and Retention (16 C.F.R. § 312.10)

**Requirement**: Collect only personal information reasonably necessary for the purpose
for which it is collected. Retain it only as long as reasonably necessary for that
specific purpose. Written retention policy required.

**6a. Data Minimization**

| Requirement                                                                                          | Status | Notes |
| ---------------------------------------------------------------------------------------------------- | ------ | ----- |
| Data collection is limited to what is reasonably necessary for the specific stated purpose           |        |       |
| Each PI field collected from children has a documented, specific purpose                             |        |       |
| No "just-in-case" or speculative collection of children's PI                                         |        |       |
| Mixed-audience operator collects only the minimum PI needed for age estimation before the age screen |        |       |

**6b. Written Retention Policy (NEW 2025 — 16 C.F.R. § 312.10(b))**

| Requirement                                                                                                      | Status | Notes |
| ---------------------------------------------------------------------------------------------------------------- | ------ | ----- |
| **Written retention policy exists** covering all categories of children's PI collected                           |        |       |
| Policy includes the **specific business need** justifying retention of each PI category                          |        |       |
| Policy includes a **specific timeline** for deletion of each PI category                                         |        |       |
| Policy prohibits indefinite retention — no PI retained without a documented, specific justification and timeline |        |       |
| **Retention policy is posted** in the privacy notice on the website/service                                      |        |       |

**6c. Retention Enforcement**

| Requirement                                                                             | Status | Notes |
| --------------------------------------------------------------------------------------- | ------ | ----- |
| Automated or procedural deletion workflow exists and runs on the retention schedule     |        |       |
| Deletion extends to all copies including backup and secondary storage                   |        |       |
| Deletion verified and documented for each PI category                                   |        |       |
| Inactive accounts or users identified as children are deleted on the retention schedule |        |       |

**Domain 6 Classification**: COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY

---

### Step 6: Third-Party SDK and Vendor Liability Assessment

Operators are liable for COPPA violations committed by third-party SDKs and analytics
tools they integrate into their services. The FTC's September 2025 guidance confirmed:
"Outsourcing functionality does not outsource liability."

**SDK and Third-Party Inventory**

| Third Party / SDK                                                                 | Data Collected from Children? | COPPA-Compliant by Design? | Written Assurances Obtained? | Finding |
| --------------------------------------------------------------------------------- | ----------------------------- | -------------------------- | ---------------------------- | ------- |
| [List all SDKs, analytics tools, ad networks, social login providers, AI vendors] |                               |                            |                              |         |

**Assessment criteria for each third party:**

1. **Data collection scope**: Does this SDK/vendor collect any personal information from
   children as defined under the 2025 rule (including persistent identifiers, IP addresses,
   and behavioral data that constitute personal information)?

2. **COPPA-by-design status**: Does the SDK/vendor offer a "COPPA-compliant mode" or
   "children's mode" that limits data collection to internal operations only, disabling
   behavioral targeting and third-party sharing for child-identified users?
   - Google Analytics: `_GA_DISABLE_ANALYTICS` / COPPA child-directed treatment flag
   - YouTube Embedded: `yt_disableRelatedVideo` / child-directed content flag
   - Firebase: Restricted data collection mode
   - Advertising SDKs (Admob, Facebook Audience Network): Child-directed treatment tags

3. **Written assurances**: Has the operator obtained a written commitment from this vendor
   to maintain appropriate security and COPPA-compliant data practices?

4. **Separate VPC coverage**: If this SDK collects data for purposes beyond core service
   delivery (advertising, AI training), has separate VPC been obtained for that disclosure?

**⟁ CLARIFY** — If the operator cannot identify all SDKs and third-party integrations,
recommend a technical audit using network traffic analysis or a software composition
analysis tool before completing this domain. The FTC has consistently found that operators
fail to inventory all data collection points, particularly for SDKs integrated late in
development cycles or through third-party frameworks.

### Step 7: State Children's Privacy Law Overlay

Assess applicable state laws based on the operator's user geography and platform type.
Note that state laws primarily cover ages 13-17, filling the gap COPPA leaves above the
under-13 threshold.

| State Law                                                                  | Applicable? | Key Requirements Beyond COPPA                                                                                                          | Current Legal Status                                           |
| -------------------------------------------------------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **California AADC** (AB 2273) — users under 18                             |             | DPIAs; default high-privacy; no targeted advertising to minors; no location collection; no dark patterns nudging toward weaker privacy | Largely enjoined [VERIFY current status — 9th Cir. March 2026] |
| **California CCPA — Minor Provisions** (Cal. Civ. Code § 1798.120)         |             | No sale of personal information of minors under 16 without affirmative authorization                                                   | In effect                                                      |
| **Texas SCOPE Act** (effective July 1, 2024) — social interaction services |             | Parental controls; limits on collection/use of minors' information                                                                     | In effect                                                      |
| **Utah Child and Teen Safety Act / Minor Protection Act**                  |             | Parental consent for account creation; content curfew 10:30 PM–6:30 AM absent parental permission                                      | In effect [VERIFY current enforcement status]                  |
| **Connecticut 2024 amendments** — users under 18                           |             | No targeted advertising to minors regardless of consent; prohibition on engagement-maximizing features (endless scroll, autoplay)      | In effect (October 1, 2024)                                    |
| **Colorado 2024 amendments (CPA)** — users under 18                        |             | Heightened minor protections equivalent to Connecticut                                                                                 | In effect                                                      |
| **Maryland Kids Code** (effective October 1, 2024)                         |             | Default high-privacy settings; no collection of precise geolocation; DPIAs for products likely accessed by minors                      | In effect                                                      |
| **Nebraska / Vermont Age-Appropriate Design Code Acts (2025)**             |             | Similar to California AADC model                                                                                                       | [VERIFY enactment and effective dates]                         |

**⟁ CLARIFY** — For operators with nationwide user bases, ask whether a comprehensive
state law gap analysis is in scope. The state laws above primarily affect ages 13-17,
which COPPA does not cover, and involve design obligations (default settings, dark
patterns, geolocation) that go well beyond COPPA's consent-and-notice framework. If the
operator intends to serve teenage users, a standalone state law gap analysis is warranted
following this COPPA assessment.

### Step 8: Safe Harbor Program Assessment

Assess whether the operator participates in, or would benefit from, an FTC-approved safe
harbor program.

**Currently FTC-Approved Programs:**

- **CARU** (Children's Advertising Review Unit, BBB National Programs) — broadest scope
- **kidSAFE** — oriented toward gaming, apps, and digital media
- **ESRB Privacy Certified** — gaming and entertainment industry
- **iKeepSafe** — educational technology
- **TRUSTe** — general web and mobile
- **PRIVO** (Privacy Vaults Online) — children's consent management

**2025 Safe Harbor Program Updates:**

- Safe harbor programs must post updated member lists publicly by July 21, 2025
- Programs must submit updated guidelines reflecting 2025 rule amendments to FTC by
  October 22, 2025
- Programs must comply with enhanced annual reporting and independent assessment requirements

**Assessment questions:**

| Question                                                                                                                                                   | Finding |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| Is the operator currently a member of any FTC-approved safe harbor program?                                                                                |         |
| If yes: Has the program submitted updated guidelines to FTC reflecting 2025 amendments?                                                                    |         |
| If yes: Does the operator's certified practices reflect the 2025 amendments?                                                                               |         |
| If no: Would safe harbor membership provide material protection and compliance support?                                                                    |         |
| Is the operator's platform type well-served by one of the existing programs (e.g., EdTech → iKeepSafe; gaming → ESRB or kidSAFE; general consumer → CARU)? |         |

**Benefits of safe harbor membership to assess:**

- FTC defers to safe harbor program's review and discipline procedures for most violations
- Ongoing compliance monitoring, alerts, and annual reviews reduce internal compliance burden
- Certification seal provides marketing/credibility benefit with parents and partners
- Provides structured framework for implementing the 2025 amendments with program support

### Step 9: FTC Civil Penalty Exposure Modeling

For each NON-COMPLIANT or CRITICAL DEFICIENCY finding, estimate the FTC civil penalty
exposure to contextualize remediation priority for the operator.

**Civil Penalty Framework:**

- Maximum penalty: **$53,088 per violation per day** (2025 inflation-adjusted) [VERIFY]
- Each child is potentially a separate "violation" for each day of ongoing violation
- FTC considers: number of children affected, volume and type of data involved, duration
  of violation, whether data was shared with third parties, company size, cooperation,
  prior violations or consent orders

**Enforcement Benchmarks:**
| Case | Year | Violation Type | Penalty |
|------|------|---------------|---------|
| Musical.ly / TikTok | 2019 | Children's PI collected without VPC; no notice to parents | $5.7 million |
| Google / YouTube | 2019 | Behavioral advertising to child-directed channel viewers without VPC | $170 million |
| Epic Games / Fortnite | 2022 | Voice/text chat enabled for children without VPC; children's PI retained | $275 million (COPPA) |
| Amazon Alexa | 2023 | Indefinite retention of children's voice recordings; incomplete deletion | $25 million |
| TikTok / ByteDance | 2024+ | Active DOJ litigation — ongoing violation of prior consent order | Up to $51,744/day sought [VERIFY] |
| Disney / YouTube | 2025 | Child-directed videos not designated "Made for Kids"; behavioral advertising | $10 million |

**Per-finding exposure estimate:**
For each CRITICAL DEFICIENCY, estimate:

1. How many children are potentially affected?
2. How long has the violation been ongoing?
3. Were children's PI shared with third parties for advertising or AI training?
4. Is this a repeat violation or does the operator have a prior COPPA consent order?

**Exposure formula (rough estimate):**

- Low exposure: < 100 children affected × 1–30 days × no third-party sharing → $5,000–$500,000
- Medium exposure: 100–10,000 children × 30–365 days × no third-party sharing → $500,000–$50M
- High exposure: > 10,000 children × > 365 days × third-party data sharing → $50M–$200M+
- Note: Exposure models are illustrative only; actual FTC penalties depend on enforcement
  discretion and cooperation. Self-disclosure and remediation significantly reduce exposure.

### Step 10: Quality Verification

Before delivering the assessment, run all quality checks:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every CRITICAL DEFICIENCY finding, run the 3-pass Self-Interrogation.
3. Confirm all [VERIFY] markers are appropriately placed on unverified citations.
4. Confirm Glass Box YAML is populated accurately.
5. Confirm all 2025 amendment items are clearly flagged as new requirements.
6. Confirm no jurisdiction-specific assumptions outside COPPA/US law context.

---

## Domain Assessment: Classification System

### Four-Tier Classification

| Tier | Label                   | Enforcement Risk                                                                  | Action Required                                 |
| ---- | ----------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------- |
| ✅   | **COMPLIANT**           | Low — requirement fully met with documentation                                    | Monitor; maintain                               |
| ⚠️   | **PARTIAL**             | Moderate — gaps exist; vulnerability if FTC investigates                          | NEAR-TERM remediation                           |
| ❌   | **NON-COMPLIANT**       | High — clear COPPA violation identified                                           | IMMEDIATE or NEAR-TERM remediation              |
| 🔴   | **CRITICAL DEFICIENCY** | Very high — active, ongoing, or systemic violation; likely largest exposure items | IMMEDIATE action; consider voluntary disclosure |

### Automatic CRITICAL DEFICIENCY Triggers

The following conditions automatically result in CRITICAL DEFICIENCY regardless of other
positive compliance factors:

1. **No privacy notice** — Directed-to-children or actual-knowledge operator with no
   COPPA-compliant privacy notice posted anywhere
2. **No VPC mechanism** — Collecting personal information from known children with no
   parental consent process in place
3. **Bundled consent only** — Relying on ToS click-through as "parental consent" with no
   separate parent-directed VPC flow
4. **Targeted advertising without VPC** — Serving behavioral or targeted advertising to
   child users without separate verifiable parental consent (post-June 23, 2025: applies
   to all operators with known child users)
5. **AI training on children's data without separate consent** — Using children's PI to
   train or improve any AI/ML model without separate, higher-reliability VPC (post-June
   23, 2025)
6. **No deletion workflow** — Retaining children's PI indefinitely with no process to
   honor parental deletion requests
7. **Incomplete deletion** — Deletion process exists but fails to cover all data stores
   including backup and secondary storage
8. **No written information security program** — Post-April 22, 2026 compliance deadline:
   absence of a written, documented children's PI security program
9. **Prior FTC consent order violation** — Any practice that violates a prior FTC COPPA
   consent order (dramatically increases per-violation penalty exposure)
10. **SDK liability ignored** — Integrating third-party SDKs that collect children's PI
    for advertising or AI purposes without any COPPA-compliant mode activation or separate
    consent

---

## Prioritization Framework

### Three-Tier Remediation Priority

#### IMMEDIATE (0–30 days)

Active violations causing ongoing COPPA exposure. Risk of FTC inquiry, parental
complaints, or third-party enforcement is highest. Stop the violation first; build the
program second.

Priority items:

- Any CRITICAL DEFICIENCY (complete absence of required element)
- Targeted advertising or AI training using children's PI without VPC
- No privacy notice posted
- SDK collecting children's data for advertising without consent
- Violation of any prior FTC consent order

#### NEAR-TERM (30–120 days)

Material compliance gaps where no active violation is ongoing but enforcement risk is
material. Address before April 22, 2026 compliance deadline for 2025 amendments.

Priority items:

- Privacy notice not updated to include third-party categories or retention timeline (2025)
- VPC mechanism uses bundled consent where separate consent is now required
- Written retention policy not yet drafted or published
- Parental deletion workflow incomplete or not covering all data stores
- Vendor agreements not including COPPA written assurances

#### BACKGROUND (120+ days)

Gaps that reduce compliance quality or create future risk but do not constitute current
active violations. Address as part of ongoing compliance program maintenance.

Priority items:

- Written information security program not yet at mature state
- Safe harbor membership evaluation not yet conducted
- State law gap analysis (ages 13–17) not yet assessed
- Age-screen UX not yet audited for neutrality
- COPPA training program not yet formalized

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any assessment output. If any gate fails,
revise before delivering.

| Gate           | Rule                                                                                                                                    | Fail Action                                                            |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Source**     | Every COPPA compliance finding cites a specific CFR section, FTC guidance, or enforcement action                                        | Add citation or mark "[UNVERIFIED]"                                    |
| **Format**     | All 16 C.F.R. and 15 U.S.C. citations follow correct citation format                                                                    | Fix format                                                             |
| **Currency**   | Every cited provision checked for 2025 amendment applicability                                                                          | Flag "[CHECK CURRENCY — may have changed under 2025 COPPA amendments]" |
| **Domain**     | Analysis stays within FTC/COPPA/US children's privacy scope; EU GDPR Art. 8 and UK Children's Code not confused with COPPA requirements | Remove or flag jurisdictional bleed                                    |
| **Confidence** | Penalty amounts, compliance deadlines, and safe harbor status explicitly marked [VERIFY] if not independently confirmed                 | Add confidence qualifier                                               |

### Self-Interrogation for CRITICAL DEFICIENCY Items

For any CRITICAL DEFICIENCY finding, apply this 3-pass review before delivery:

**Pass 1 — Legal Chain Integrity**: Does the violation assessment follow logically from the
cited COPPA Rule provision? Does 16 C.F.R. Part 312 actually require this element for
this type of operator? Does the operator's situation match the applicable coverage path
(directed-to-children vs. actual knowledge)?

**Pass 2 — Completeness**: Have all relevant COPPA Rule provisions been considered for this
finding? Have the 2025 amendment applicability dates been checked (effective June 23, 2025;
compliance deadline April 22, 2026)? Are any available exceptions that could legitimize
the practice (e.g., internal operations exception, school-as-agent) considered and ruled out?

**Pass 3 — Challenge**: What is the strongest argument that this is NOT a CRITICAL
DEFICIENCY? Under what circumstances could this practice be defensible? If the strongest
counter-argument is weak, maintain the classification. If it is strong, consider whether
PARTIAL or NON-COMPLIANT is more appropriate.

### Confidence Scoring

| Level        | Range     | Meaning                                                                                   | Action                                                       |
| ------------ | --------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Definite** | 0.95–1.0  | Unambiguous COPPA Rule text; clear violation or compliance                                | State with confidence                                        |
| **High**     | 0.80–0.94 | Strong authority (16 C.F.R. Part 312 + FTC guidance); minor interpretive questions        | State with brief caveat                                      |
| **Probable** | 0.60–0.79 | Good arguments; FTC has not directly ruled on this specific fact pattern                  | State with reasoning and note FTC has not addressed          |
| **Possible** | 0.40–0.59 | Genuinely uncertain; 2025 amendment implementation guidance pending; fact pattern unusual | Flag for attorney review with both sides                     |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative; no clear authority                                               | Do not assert; flag "[UNCERTAIN — attorney review required]" |

---

## Anti-Patterns

The following are the most common COPPA compliance failures, organized by domain. Every
item in this list is traceable to an actual FTC enforcement action, published FTC guidance,
or identifiable compliance gap.

1. **Relying on ToS click-through as VPC** — Terms of service acceptance is never
   verifiable parental consent under any circumstances. COPPA requires a distinct,
   parent-directed consent event. (Pattern from: widespread; Epic Games enforcement noted
   general lack of parent-specific consent flow)

2. **Bundling third-party consent with service consent post-2025** — After June 23, 2025,
   obtaining a single parent consent that covers both "use the service" and "share data
   with advertising partners" violates the separate-consent requirement for third-party
   sharing. (Pattern from: 2025 COPPA Rule amendment, 16 C.F.R. § 312.5(a)(1)(ii))

3. **Ignoring SDK data collection as your own** — Treating SDK-generated data flows as "not
   my problem" because a third party does the collecting. The FTC's September 2025 Apitor
   enforcement action confirmed that the operator of the child-directed app bears liability
   for every COPPA violation committed by an integrated SDK, regardless of who wrote the
   code. (Pattern from: Apitor enforcement, FTC blog September 2025)

4. **Incomplete deletion — backup blindspot** — Honoring a parental deletion request from
   primary databases while leaving the child's data in backup or archive systems. The
   Amazon Alexa $25M enforcement turned on precisely this failure. Written in the FTC
   complaint: voice transcripts remained in secondary databases long after parents believed
   data had been deleted. (Pattern from: FTC v. Amazon.com, Inc., 2023)

5. **Wrong audience designation at the wrong level** — Designating a content channel or
   app as child-directed at the platform level but failing to apply the designation to
   individual pieces of content. YouTube's post-2019 consent order required per-video
   "Made for Kids" designation; Disney's 2025 $10M enforcement action arose precisely from
   this gap — failing to review each video. (Pattern from: FTC v. Disney, 2025)

6. **Age gate designed to discourage child selection** — Designing an age gate that
   pre-populates an adult year of birth, puts "under 13" last in a long scroll list,
   presents the child-selection path with friction (additional warning screens), or uses
   language suggesting only adult users are welcome. A skewed age gate does not satisfy
   the neutral-screen requirement and does not prevent actual knowledge from being
   imputed. (Pattern from: 2025 COPPA Rule § 312.2(b) commentary)

7. **General audience defense with child-appealing marketing** — Claiming general-audience
   status while marketing the service with animated characters, child-friendly language,
   gamification, and appeals to school-age audiences. Marketing materials are now
   explicitly part of the directed-to-children multi-factor test under the 2025 amendments.
   (Pattern from: FTC directed-to-children test amendments, 2025 Rule)

8. **No written retention policy post-2025** — Retaining children's PI "as long as
   necessary" without a written, published policy specifying the concrete retention period
   for each data category and the business justification. Post-April 22, 2026: this alone
   is a COPPA violation independent of whether actual retention is reasonable. (Pattern
   from: 2025 COPPA Rule § 312.10(b))

9. **Training AI models on children's data without separate consent** — Using children's
   behavioral data, voice recordings, chat logs, or biometric data to train AI or ML
   models under the assumption that general platform consent covers AI purposes. The FTC
   has explicitly ruled this is not integral to service delivery and therefore requires
   separate higher-reliability VPC. (Pattern from: 2025 Rule amendment commentary;
   Amazon Alexa enforcement; FTC blog on AI and children's data)

10. **EdTech school-consent misuse** — Using student data collected under the school-as-
    agent exception for commercial purposes beyond the specific educational use that
    justified the school's consent. The school can consent on parents' behalf only for the
    educational purpose; any extension to advertising, analytics products, or AI training
    is a COPPA violation. (Pattern from: FTC guidance; FTC blog on EdTech)

11. **Biometric data collection without recognizing new PII status** — Collecting voice
    recordings, facial templates, or behavioral biometric data from children (e.g., a
    connected toy that records children's voices) without recognizing that such data
    constitutes "personal information" under the 2025 expanded definition. (Pattern from:
    2025 COPPA Rule § 312.2 biometric identifier addition)

12. **Persistent identifier as an invisible COPPA trigger** — Deploying analytics or
    advertising tracking via cookies, device IDs, or other persistent identifiers on a
    child-directed service without treating those identifiers as personal information
    requiring VPC (unless strictly limited to internal operations). The Google/YouTube
    $170M settlement arose from precisely this pattern — cookies and device IDs used for
    behavioral advertising on child-directed channels without parental consent. (Pattern
    from: FTC v. Google/YouTube, 2019)

13. **No direct notice to parents before collection** — Having a privacy policy posted on
    the website but failing to deliver direct notice to parents before data collection
    begins. A static privacy policy link is not a substitute for direct parental notice.
    (Pattern from: 16 C.F.R. § 312.4(b) requirement; common enforcement observation)

14. **Third-party vendor agreements without COPPA security assurances** — Disclosing
    children's PI to vendors (cloud providers, processors, analytics firms) without
    obtaining written assurances that the vendor will maintain appropriate security.
    Post-2025, these written assurances are an explicit Rule requirement. (Pattern from:
    2025 COPPA Rule § 312.8(c))

15. **Assuming prior compliance is permanent** — Treating a COPPA compliance assessment
    conducted before the 2025 amendments as current. The 2025 amendments introduced eight
    new substantive requirements; operators with "clean" pre-2025 programs may have four
    to eight compliance gaps that did not exist under the 2013 rule. (Pattern from: 2025
    amendment scope; compliance deadline April 22, 2026)

16. **Ignoring actual knowledge when it arises** — Collecting PI from a user who has
    revealed their age as under 13 (by stating it, by age-screen result, or by parental
    complaint) and continuing to process that data without obtaining VPC or deleting it.
    Actual knowledge creates immediate COPPA obligations; delay creates additional violation
    days at up to $53,088 per day per affected child. (Pattern from: Musical.ly/TikTok 2019;
    TikTok/ByteDance 2024 DOJ complaint)

17. **Underestimating "personal information" post-2025** — Treating only traditional PII
    (name, email, address) as triggering COPPA obligations while overlooking that IP
    addresses, persistent device identifiers, photographs, audio recordings, and now
    biometric identifiers and government-issued ID numbers all constitute personal
    information under 16 C.F.R. § 312.2. (Pattern from: 2025 Rule § 312.2 definitional
    expansion)

---

## Writing Standards

Before delivering the assessment output, apply these quality gates:

1. **Plain language**: Every finding must be understandable to a non-lawyer technical
   product manager or business operator. Avoid COPPA jargon without explanation.

2. **Cite specifically**: Every finding must cite the specific CFR section, FTC guidance
   document, or enforcement action that supports it. "COPPA requires X" is incomplete;
   "16 C.F.R. § 312.5(a)(1)(ii) requires X" is complete.

3. **Mark uncertainty**: All penalty amounts, compliance deadline dates, state law
   status, and safe harbor program certification status must be marked [VERIFY] if not
   independently confirmed against current sources.

4. **2025 amendment callouts**: Every finding that arises from the 2025 amendments (not
   the 2013 rule) must be flagged as **NEW (2025)** so the operator understands this is
   a new requirement, not a pre-existing gap.

5. **Actionable findings only**: Every finding must include a specific, actionable
   remediation step — not a generic "review your practices" recommendation. "Update the
   privacy notice to add a data retention timeline for each PI category, per 16 C.F.R.
   § 312.4(d)(5)" is actionable. "Review your privacy notice" is not.

6. **No absolute guarantees**: Never state that following these recommendations will result
   in "full COPPA compliance" or that "no FTC enforcement action will follow." The
   assessment produces a compliance posture framework; only a qualified attorney can assess
   legal exposure.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- Search for current FTC COPPA Rule text at 16 C.F.R. Part 312 (post-2025 amendment)
- Verify the current inflation-adjusted civil penalty maximum
- Search for recent FTC enforcement actions and consent orders involving COPPA
- Verify state children's privacy law enactments and current enforcement status
- Check safe harbor program updated guideline submission and approval status
- Save research to `/tmp/coppa-assessment-research.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in Glass Box

**Without legalcode-mcp:**

- Proceed with Rule text and enforcement data from training data
- Mark all penalty amounts, compliance deadlines, state law status, and safe harbor program
  status with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Specifically flag:
  - Current inflation-adjusted civil penalty amount
  - April 22, 2026 compliance deadline (confirm no FTC extension or enforcement moratorium)
  - California AADC current injunction status (largely enjoined as of early 2026 but subject
    to ongoing appellate proceedings)
  - Safe harbor program updated guideline submission and FTC approval status
  - State law developments after August 2025

---

## Glass Box Audit Trail

Include this YAML block in every delivered assessment:

```yaml
glass_box:
  skill_name: "legalcode-coppa-compliance-assessment"
  assessment_date: "[date]"
  operator_name: "[name or description]"
  platform_type: "[website/mobile app/gaming/EdTech/IoT/AdTech/streaming/mixed]"
  coppa_applicability_path: "[directed-to-children / actual knowledge / mixed-audience / not applicable]"
  assessment_mode: "[full assessment / 2025 amendment gap / applicability only / pre-launch / VPC review / FTC prep]"
  rule_version_assessed: "16 C.F.R. Part 312 (2025 amendments, effective June 23, 2025)"
  compliance_deadline_flag: "April 22, 2026 (one year from publication) [VERIFY no FTC extension]"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[path or 'Not created']"
  domains_assessed:
    domain_1_privacy_notice: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]"
    domain_2_direct_notice: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]"
    domain_3_vpc: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]"
    domain_4_parental_rights: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]"
    domain_5_security: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]"
    domain_6_minimization_retention: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]"
  critical_deficiency_count: "[number]"
  non_compliant_count: "[number]"
  partial_count: "[number]"
  compliant_count: "[number]"
  third_party_sdks_assessed: "[number or 'not assessed']"
  state_law_overlay_assessed: "[list of states or 'not assessed']"
  safe_harbor_status: "[member program / evaluated / not evaluated]"
  ftc_exposure_modeled: "[yes / no]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED — marked [VERIFY]]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or operator-specific caveats]"
    - "2025 amendment compliance deadline: April 22, 2026 — verify no FTC extension granted"
    - "Penalty amounts reflect 2025 inflation-adjusted maximum — verify current figure"
    - "State law status as of March 2026 — evolving rapidly; verify before advising"
  reviewer: "AI-assisted — requires qualified children's privacy attorney review before reliance"
```

---

## Localization Notes

COPPA is a US federal statute with no direct equivalent in other jurisdictions. When an
operator is subject to multiple jurisdictions' children's privacy regimes:

- **GDPR Article 8 (EU)**: Age of consent for processing children's data under GDPR is set
  by each member state, typically 13–16. GDPR Article 8 requires parental consent for
  children below the member-state threshold for social media and similar services, but
  differs from COPPA in scope, consent standards, and enforcement. Use a separate EU
  children's privacy skill for GDPR Article 8 analysis.
- **UK Children's Code (Age-Appropriate Design Code)**: Substantially more design-oriented
  than COPPA; applies to all under-18 users; enforced by the ICO. Not preempted by COPPA.
- **Canada PIPEDA / Bill C-27 (proposed Consumer Privacy Protection Act)**: Canada does
  not have a COPPA equivalent; children's data is addressed through PIPEDA's meaningful
  consent standard and provinces' private-sector privacy laws. Bill C-27 would strengthen
  protections [VERIFY enactment status].
- **Australia Privacy Act 1988 (as amended)**: Australian Privacy Principles apply to
  children; the Privacy Act 2024 amendments [VERIFY status] strengthen protections.

When an operator faces multiple jurisdictions' children's privacy obligations, COPPA
compliance does not satisfy EU, UK, Canadian, or Australian requirements and vice versa.
Build a jurisdiction matrix if multi-regime compliance is required.

---

## Output Format Template

Deliver the assessment in this format:

---

# COPPA Compliance Assessment

**Operator**: [name]
**Platform type**: [type]
**Assessment date**: [date]
**Assessment mode**: [mode]
**Rule version**: 16 C.F.R. Part 312 (2025 amendments; compliance deadline April 22, 2026)

---

## Executive Summary

| Domain                                  | Classification                                              | Key Finding        |
| --------------------------------------- | ----------------------------------------------------------- | ------------------ |
| Operator Applicability                  | [APPLICABLE / NOT APPLICABLE / PARTIAL]                     | [one-line summary] |
| Domain 1: Privacy Notice                | [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY] | [one-line]         |
| Domain 2: Direct Notice to Parents      | [classification]                                            | [one-line]         |
| Domain 3: Verifiable Parental Consent   | [classification]                                            | [one-line]         |
| Domain 4: Parental Access & Deletion    | [classification]                                            | [one-line]         |
| Domain 5: Children's Data Security      | [classification]                                            | [one-line]         |
| Domain 6: Data Minimization & Retention | [classification]                                            | [one-line]         |
| Third-Party SDK Liability               | [classification]                                            | [one-line]         |
| State Law Overlay                       | [assessed / not assessed]                                   | [one-line]         |

**Overall compliance posture**: [HIGH RISK / MODERATE RISK / LOW RISK — one-paragraph summary]

**FTC enforcement exposure**: [IMMEDIATE / ELEVATED / MODERATE / LOW — one-paragraph summary]

---

## Critical Deficiencies (IMMEDIATE Action Required)

For each CRITICAL DEFICIENCY:

### CD-[N]: [Short title]

**Domain**: [Domain name]
**COPPA provision**: [16 C.F.R. § 312.X or 15 U.S.C. § 650X]
**2025 amendment**: [YES — NEW REQUIREMENT / NO — existing requirement]
**Finding**: [Specific description of the violation or gap]
**FTC enforcement risk**: [Description of enforcement exposure]
**Remediation**: [Specific, actionable steps to remediate]
**Timeline**: IMMEDIATE (0–30 days)
**Confidence**: [Definite / High / Probable] — [brief basis]

---

## Non-Compliant Findings (NEAR-TERM Action Required)

[Same format as Critical Deficiencies, marked NEAR-TERM]

---

## Partial Compliance Findings (NEAR-TERM to BACKGROUND)

[Same format, lighter detail]

---

## Safe Harbor Assessment

**Current status**: [member / not member]
**Recommended program**: [CARU / kidSAFE / ESRB / iKeepSafe / TRUSTe / PRIVO / none recommended]
**Rationale**: [Why this program fits this operator's platform type]
**2025 update status**: [whether the program has submitted updated guidelines]

---

## State Law Overlay Summary

[Table of applicable state laws, key requirements beyond COPPA, and recommended next steps]

---

## FTC Civil Penalty Exposure Estimate

**Basis**: $53,088 per violation per day (2025 inflation-adjusted) [VERIFY]
**Primary exposure items**: [List top 3 findings by estimated exposure]
**Aggregate exposure estimate**: [LOW / MODERATE / HIGH / VERY HIGH with reasoning]
**Mitigating factors**: [Cooperation, self-disclosure, remediation plans, good-faith efforts]

---

## Remediation Roadmap

### IMMEDIATE (0–30 days)

- [ ] [Specific action] — [responsible team] — [outcome]
- [ ] ...

### NEAR-TERM (30–120 days)

- [ ] [Specific action] — [responsible team] — [outcome]
- [ ] ...

### BACKGROUND (120+ days)

- [ ] [Specific action] — [responsible team] — [outcome]
- [ ] ...

---

## Glass Box Audit Trail

[YAML block as defined in the Glass Box section above]

---

_Assessment produced by legalcode-coppa-compliance-assessment. This is an AI-assisted
compliance framework, not legal advice. All findings should be reviewed by a qualified
attorney with children's privacy expertise before reliance or regulatory disclosure._

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis via Mode A skill creation workflow:
deep research on COPPA (15 U.S.C. §§ 6501–6506; 16 C.F.R. Part 312 including 2025
amendments finalized January 16, 2025, published April 22, 2025, effective June 23, 2025);
FTC enforcement actions (Musical.ly/TikTok 2019 $5.7M; Google/YouTube 2019 $170M; Epic
Games/Fortnite 2022 $275M; Amazon Alexa 2023 $25M; TikTok/ByteDance 2024 DOJ suit; Disney
2025 $10M); FTC guidance on COPPA compliance, safe harbor programs, and SDK liability; state
children's privacy law developments (CA AADC, TX SCOPE Act, UT CSPA, CT/CO 2024 amendments,
MD Kids Code); FTC blog posts on 2025 rule amendments. Quality framework adapted from the
legalcode-hipaa-compliance-assessment and legalcode-contract-review reference standards.
