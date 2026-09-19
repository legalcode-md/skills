---
name: legalcode-au-asic-regulatory-compliance
description: Assess compliance with the Australian Securities and Investments Commission (ASIC) regulatory
  framework. Use when auditing AFS licensees, credit licensees, responsible entities, managed investment
  scheme operators, securities dealers, superannuation trustees, financial advisers, insurance providers,
  BNPL providers, or any entity regulated by ASIC under the Corporations Act 2001, ASIC Act 2001, or NCCP
  Act 2009.
metadata:
  jurisdiction: Australia
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Assess compliance with the Australian Securities and Investments Commission (ASIC) regulatory framework. Covers all major ASIC-regulated obligations: Australian Financial Services Licence (AFSL) general obligations under s 912A Corporations Act 2001 (Cth) (efficient/honest/fair, risk management, conflicts of interest, responsible managers, financial resources, professional indemnity insurance); responsible lending conduct under the National Consumer Credit Protection Act 2009 (Cth) including unsuitable credit assessment, BNPL reforms effective 10 June 2025, and hardship obligations; Design and Distribution Obligations (DDO) under Part 7.8A — target market determinations, distribution conditions, significant dealing notifications, and review triggers; Internal Dispute Resolution (IDR) under ASIC RG 271 — complaint timeframes (30/21/45 days), written IDR responses, complaints register, AFCA referral obligations, and biannual IDR data reporting; breach reporting under s 912DAA — reportable situations, 30-day lodgement, significant breach thresholds, and the 2023 modification for repeat circumstances; market integrity rules — continuous disclosure (Part 6CA), insider trading (Part 7.10), and manipulation; sustainability/climate reporting obligations (mandatory from 1 July 2026 for large entities); and ASIC enforcement risk profiling (2024–2025 priorities: greenwashing, DDO, predatory lending, financial hardship, cyber security). Generates COMPLIANT / PARTIAL / NON-COMPLIANT findings with CRITICAL / HIGH / MEDIUM / LOW risk tiers, clause-level remediation language, penalty exposure estimates, and a prioritised compliance roadmap. Use when auditing AFS licensees, credit licensees, responsible entities, managed investment scheme operators, securities dealers, superannuation trustees, financial advisers, insurance providers, BNPL providers, or any entity regulated by ASIC under the Corporations Act 2001, ASIC Act 2001, or NCCP Act 2009. Jurisdiction: Australia (Commonwealth — federal). Enforced by ASIC, AFCA (EDR), and the Financial Services and Credit Panel (adviser disciplinary body).


# Legalcode — ASIC Regulatory Compliance Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted ASIC regulatory compliance
> assessment. It does not constitute legal advice. All outputs require review by an
> Australian-qualified financial services lawyer before reliance, particularly in relation to
> enforcement risk, specific penalty exposure, remediation strategy, and AFSL licence
> conditions. The Corporations Act 2001 (Cth), NCCP Act 2009, and ASIC regulatory guides are
> frequently updated — ASIC's enforcement priorities, penalty thresholds, and guidance evolve
> continuously. Verify current applicability of all statutory provisions, penalty amounts,
> regulatory guide references, and case law against authoritative sources (Federal Register
> of Legislation, ASIC website, ASIC Regulatory Portal, Federal Court of Australia) before
> acting. Section numbers, penalty amounts, and regulatory guide references cited from memory
> carry hallucination risk — mark all such references with [VERIFY] unless independently
> confirmed against authoritative sources.

---

## Purpose and Scope

This skill assesses the practices, policies, agreements, and operational systems of
ASIC-regulated entities for compliance with the major ASIC regulatory frameworks.

**Covers:**

- **AFSL obligations** — s 912A Corporations Act 2001 general obligations (efficient, honest,
  and fair; adequate risk management; conflicts of interest; responsible managers; compensation
  arrangements; financial resources; professional indemnity insurance)
- **Responsible lending conduct** — NCCP Act 2009: unsuitable credit assessment, reasonable
  inquiries, verification, hardship (s 72 National Credit Code), and BNPL reforms (from
  10 June 2025)
- **Design and Distribution Obligations (DDO)** — Part 7.8A Corporations Act: target market
  determinations (TMDs), distribution conditions, significant dealing notifications, review
  triggers, and product intervention powers (Part 7.9A)
- **Internal Dispute Resolution (IDR)** — ASIC RG 271: complaint timeframes, written IDR
  response requirements, complaints register, AFCA referral, and biannual IDR data reporting
  (updated December 2025 handbook)
- **Breach reporting** — s 912DAA Corporations Act: reportable situations, 30-day lodgement,
  significant breach analysis, repeat-circumstance extension (90 days from October 2023)
- **Market integrity rules** — continuous disclosure (Part 6CA, ASX Listing Rule 3.1 [VERIFY]),
  insider trading (Part 7.10), market manipulation, and short-selling reporting
- **Sustainability and climate reporting** — mandatory from 1 July 2026 for Group 1 entities;
  ASIC RG 280 (published March 2025); AASB S1/S2 standards
- **ASIC enforcement risk profiling** — 2024–2025 priorities, civil penalty regime, and
  recent enforcement precedents

**Does not:**

- Provide legal advice or replace qualified Australian financial services legal counsel
- Cover the Australian Competition and Consumer Act 2010 / ACL
  (see `legalcode-au-consumer-law-compliance`)
- Cover the Privacy Act 1988 (Cth) or Notifiable Data Breach scheme in depth
  (see `australia-privacy-act-ndb-breach-notification-operations`)
- Cover the Fair Work Act 2009 (Cth) employment obligations
  (see `legalcode-au-fair-work-compliance`)
- Cover the Superannuation Industry (Supervision) Act 1993 (Cth) in depth — superannuation
  trustee duties are referenced where they intersect AFSL obligations but not fully assessed
- Cover state-based financial services licensing (all states have referred financial services
  powers to the Commonwealth)
- Cover anti-money-laundering obligations under the Anti-Money Laundering and Counter-
  Terrorism Financing Act 2006 (Cth) — AML/CTF is a separate framework administered by AUSTRAC

**Related skills:**

- `legalcode-au-consumer-law-compliance` — ACL compliance assessment
- `legalcode-au-fair-work-compliance` — Fair Work Act employment compliance
- `australia-privacy-act-ndb-breach-notification-operations` — Privacy Act + NDB scheme
- `legalcode-contract-review` — General commercial contract review (jurisdiction-agnostic)

---

## Jurisdiction and Governing Law

### Why ASIC Compliance Requires a Dedicated Skill

ASIC administers a highly complex, multi-layered regulatory framework under federal
legislation. Unlike general commercial law principles, ASIC compliance obligations are:

- **Statute-specific**: Duties are created and defined by the Corporations Act 2001 (Cth),
  the ASIC Act 2001 (Cth), and the NCCP Act 2009 — general common law principles
  supplement but do not replace these statutory frameworks.
- **Entity-type dependent**: AFSL obligations differ materially depending on whether the
  entity is an AFS licensee, credit licensee, responsible entity, securities dealer,
  insurance provider, or superannuation trustee. Each category has tailored obligations.
- **Instrument-dense**: ASIC issues dozens of regulatory guides (RGs), class orders (COs),
  and legislative instruments that modify or clarify statutory obligations. Compliance
  analysis requires knowledge of current operative instruments.
- **Rapidly evolving**: Major reforms have occurred since 2019 (Hayne Royal Commission
  response, DDO commencement October 2021, breach reporting October 2021, IDR RG 271
  October 2021, BNPL regulation June 2025, mandatory climate reporting July 2026).
- **High-consequence enforcement**: Post-2019 civil penalty regime dramatically increased
  maximum penalties. ASIC obtained record civil penalties in 2024–2025.

### Primary Legislation

| Statute                                                                                                | Coverage                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Corporations Act 2001 (Cth)                                                                            | AFSL obligations (Ch 7), DDO (Pt 7.8A), breach reporting (s 912DAA), market integrity (Pt 6CA, Pt 7.10), managed investment schemes (Ch 5C) |
| ASIC Act 2001 (Cth)                                                                                    | ASIC's powers; consumer protection in financial services (ss 12BAA–12GBT, parallel to ACL for financial products)                           |
| National Consumer Credit Protection Act 2009 (Cth)                                                     | Credit licensee obligations, responsible lending, National Credit Code (Schedule 1)                                                         |
| Treasury Laws Amendment (Design and Distribution Obligations and Product Intervention Powers) Act 2019 | DDO regime, product intervention powers                                                                                                     |
| Financial Sector Reform (Hayne Royal Commission Response – Better Advice) Act 2021                     | Breach reporting, responsible manager regime, Financial Services and Credit Panel                                                           |
| Treasury Laws Amendment (Financial Market Infrastructure and Other Measures) Act 2024                  | Mandatory sustainability reporting framework                                                                                                |
| Competition and Consumer (Industry Codes — Buy Now Pay Later) Regulations 2025 [VERIFY]                | BNPL credit licence obligations from 10 June 2025                                                                                           |

### Key Regulatory Guides Referenced

| RG     | Title                                                             | Relevance                    |
| ------ | ----------------------------------------------------------------- | ---------------------------- |
| RG 78  | Breach Reporting by AFS Licensees and Credit Licensees (Dec 2023) | Reportable situations regime |
| RG 104 | AFS Licensing: Meeting the General Obligations                    | s 912A compliance            |
| RG 105 | AFS Licensing: Organisational Competence                          | Responsible managers         |
| RG 121 | Doing Financial Services Business in Australia                    | Licensing thresholds         |
| RG 175 | Licensing: Financial Product Advisers                             | Advice obligations           |
| RG 209 | Credit Licensing: Responsible Lending Conduct                     | NCCP Act obligations         |
| RG 255 | Providing entity-specific advice                                  | Individual suitability       |
| RG 265 | ASIC Market Integrity Rules (Securities Markets)                  | Market conduct               |
| RG 271 | Internal Dispute Resolution                                       | IDR complaint handling       |
| RG 272 | Product Intervention Power                                        | PIP exercise criteria        |
| RG 274 | Product Design and Distribution Obligations                       | DDO compliance               |
| RG 280 | Sustainability Reporting (Mar 2025)                               | Climate disclosures          |
| RG 281 | Low Cost Credit Contracts                                         | BNPL obligations             |

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The entity type would determine which ASIC regime applies
- The scope of products/services affects which DDO or responsible lending obligations apply
- Ambiguity in the materials requires resolution before accurate classification
- Risk tolerance or business context is needed to calibrate severity correctly

Use the **⟁ CLARIFY** pattern (structured options with descriptions) wherever marked below.
If the user has already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept the Assessment Materials

Accept any of these inputs:

- **Policy/procedure documents**: Compliance frameworks, dispute resolution procedures,
  TMDs, credit assessment procedures, breach reporting policies
- **Contracts or agreements**: Client agreements, advisory agreements, distribution
  agreements, managed investment scheme constitutions
- **Operational descriptions**: Descriptions of current practices, sales processes,
  product design processes, complaints handling workflows
- **Regulatory correspondence**: ASIC notices, infringement notices, enforceable
  undertakings, court orders
- **File descriptions**: Description of files, products, or services to be assessed

If no materials are provided, proceed with a general compliance gap assessment against
all seven ASIC compliance pillars.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user these questions (skip if already answered):

1. **Entity type** — What type of ASIC-regulated entity is being assessed?
   - Options:
     - AFS Licensee (financial services — product issuer, dealer, adviser, insurance)
     - Credit Licensee (consumer credit — lender, broker, BNPL provider)
     - Responsible Entity (managed investment scheme operator)
     - Both AFS and Credit Licensee (dual-regulated)
     - Listed entity (continuous disclosure obligations in addition)
     - Other ASIC-regulated entity (specify)
   - _Why this matters_: AFSL obligations, responsible lending, and DDO apply to different
     entity types. Assessment scope is determined by entity classification.

2. **Products and services scope** — Which financial products or credit products are involved?
   - Options: Financial advice, investment products, insurance, superannuation, credit
     products, managed funds/schemes, securities dealing, BNPL, other
   - Allow multiple selections.
   - _Why this matters_: DDO applies to issuers of financial products with TMD obligations;
     responsible lending applies to credit; IDR and breach reporting apply broadly.

3. **Assessment focus** — What is the primary compliance concern?
   - Options: Full ASIC regulatory audit (all 7 pillars), AFSL obligations only, Responsible
     lending only, DDO/TMD compliance only, IDR process review, Breach reporting readiness,
     Market integrity, Sustainability reporting readiness, Enforcement risk profiling
   - _Why this matters_: Determines the depth and ordering of the analysis.

4. **Trigger event** — What prompted this assessment?
   - Options: Proactive compliance audit, ASIC surveillance inquiry or notice, Internal
     breach or incident identified, Regulatory change (specify), Pre-licence application,
     M&A due diligence, Other (specify)
   - _Why this matters_: ASIC inquiries require immediate prioritisation of material gaps;
     proactive audits can proceed more methodically.

5. **Recent ASIC communications** — Has the entity received any ASIC correspondence,
   infringement notices, or enforceable undertakings in the last 24 months?
   - _Why this matters_: Prior ASIC contact escalates severity classification and influences
     remediation urgency.

If partial context is provided, proceed with stated assumptions clearly labelled.

### Step 3: Load Legal Authority via legalcode-mcp

Use **legalcode-mcp** to search for jurisdiction-relevant authority across:

- Current text of key provisions: Corporations Act ss 912A, 912DAA, Parts 7.8A, 7.9A,
  7.10, 6CA; NCCP Act 2009 ss 115–133 (unsuitable credit), Schedule 1 (National Credit
  Code) s 72 (hardship)
- Recent ASIC enforcement actions and Federal Court judgments relevant to the entity type
- Current operative versions of relevant ASIC regulatory guides
- Treasury instruments modifying penalty unit values

Save results to `/tmp/legalcode-asic-authority.md`. Mark all citations sourced from
legalcode-mcp as VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**

- Mark all statutory and regulatory guide citations with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with analysis using the provisions described in this skill, noting that
  verification against current law is required before reliance

### Step 4: AFSL General Obligations Assessment (Pillar 1)

Assess compliance with the AFS licensee obligations under s 912A(1) Corporations Act [VERIFY]:

#### 4.1 Efficient, Honest, and Fairly Obligation (s 912A(1)(a))

- Review client-facing materials, internal procedures, and service delivery processes
- Identify practices that may fall below the "efficient, honest and fair" standard
- Note: courts and ASIC interpret this as a composite obligation encompassing not just
  honesty but also efficient execution and procedurally fair dealing

**Classification trigger — CRITICAL**: Evidence of systematic misconduct, deliberate
non-disclosure, or dishonest dealing with retail clients.

**Classification trigger — HIGH**: Process failures creating material risk of
inefficient, unfair, or misleading service delivery; failure to act on known deficiencies.

#### 4.2 Risk Management Systems (s 912A(1)(h))

- Confirm documented risk management framework covering financial, operational, and
  compliance risks
- Assess whether risk management systems identify, assess, manage, and monitor
  all material business risks
- Review evidence of periodic risk review and board/senior management oversight
- Note: ASIC's 2025 review of responsible entities found widespread compliance plan
  deficiencies — most failed to adequately address DDO, IDR, and reportable situations

**CRITICAL gap**: No documented risk management framework.

**HIGH gap**: Risk management system exists but does not address material ASIC-specific
risks (DDO, breach reporting, IDR) or lacks documented review cycle.

#### 4.3 Conflicts of Interest (s 912A(1)(aa))

- Identify arrangements where licensee, representatives, or related parties have
  interests that may conflict with client interests
- Review conflict identification, management, and disclosure procedures
- Assess whether conflicted remuneration arrangements exist and whether they comply
  with the conflicted remuneration ban (Div 4, Pt 7.7A for retail clients) [VERIFY]

**CRITICAL**: Undisclosed material conflicts affecting client outcomes, particularly
conflicted remuneration in advice context.

**HIGH**: Conflict identification exists but management procedures are inadequate or
disclosure to clients is deficient.

#### 4.4 Responsible Managers (s 912A(1)(e), RG 105)

- Confirm that nominated responsible managers (RMs) remain current, hold appropriate
  authorisations, and meet competency requirements
- Verify RM details are lodged on the ASIC Regulatory Portal (from 16 June 2025,
  all AFSL variations are made through the Portal)
- Assess whether organisational competence requirements (RG 105) are met for each
  financial services authorisation on the AFSL
- Flag where RMs have departed and replacements have not been nominated

**CRITICAL**: No responsible managers nominated, or all RMs have departed without replacement.

**HIGH**: RMs nominated but competency evidence is deficient or authorisations have expired.

#### 4.5 Adequate Financial Resources (s 912A(1)(d))

- Confirm minimum Surplus Liquid Funds (SLF) requirements are met
- For licensees holding client money or property valued at ≥ $100,000: minimum SLF of
  $50,000 [VERIFY — confirm current ASIC instrument threshold]
- Review financial accounts and cash flow projections for evidence of financial resilience
- Confirm professional indemnity insurance (PI insurance) arrangements are current and
  meet ASIC's requirements (ASIC Class Order [CO 01/1296] or successor instruments [VERIFY])

**CRITICAL**: SLF below minimum requirement or PI insurance lapsed.

**HIGH**: Financial resources technically sufficient but trending toward minimum thresholds
without documented mitigation.

#### 4.6 Compensation Arrangements (s 912B)

- Confirm compensation arrangements are in place for clients who suffer loss from a
  breach of a financial services obligation
- PI insurance is the most common form; confirm coverage adequacy for the services provided
- Assess whether coverage terms exclude any categories of the licensee's actual services

**CRITICAL**: No qualifying compensation arrangements in place.

**HIGH**: Compensation arrangements exist but have material coverage gaps relative to
services authorised under the AFSL.

### Step 5: Responsible Lending Assessment (Pillar 2)

Applies to credit licensees under the NCCP Act 2009. Skip this step if the entity holds
no credit licence. For dual-regulated entities, complete both Steps 4 and 5.

#### 5.1 Unsuitable Credit Assessment (ss 115–133 NCCP Act) [VERIFY]

**Three-limb unsuitable credit test** — A credit contract is unsuitable if any of the
following is established at the time of assessment:

| Limb                         | Condition                                                                |
| ---------------------------- | ------------------------------------------------------------------------ |
| 1 — Needs/objectives         | Contract does not meet the consumer's stated requirements and objectives |
| 2 — Repayment capacity       | Consumer cannot make required repayments without substantial hardship    |
| 3 — Significant disadvantage | Contract is otherwise unsuitable for the consumer                        |

**Assessment procedure requirements:**

- Inquiries made **no more than 90 days prior** to entering or materially increasing credit
- Reasonable inquiries into: requirements and objectives, income, expenses, existing debts,
  assets, employment status, dependants
- Reasonable steps to verify: financial situation (payslips, bank statements, ATO notices)
- Documented assessment file maintained

**Recent enforcement — ASIC v Money3 Loans Pty Ltd [2025] FCA [VERIFY]:**
Court found Money3 failed to make reasonable inquiries about/verify borrowers' living
expenses for five loans and failed to inquire about broker fee financing on one loan.
Note: court applied nuanced view on what constitutes unreasonable expense calculations —
per se mechanical failures were not sufficient without evidence of unsuitable outcomes.

**⟁ CLARIFY** — For BNPL providers being assessed for the first time under the June 2025
reforms: confirm whether the entity held a credit licence prior to 10 June 2025 or whether
it was relying on the transitional arrangement (application lodged by 11 May 2025).

#### 5.2 BNPL Reforms (from 10 June 2025)

Under reforms effective 10 June 2025, BNPL contracts are regulated under the NCCP Act:

- BNPL providers must hold a valid credit licence from ASIC
- Modified responsible lending obligations apply (RG 281 — Low Cost Credit Contracts)
- Transitional arrangement: providers who lodged applications by 11 May 2025 and had
  applications accepted by 10 June 2025 may operate pending determination
- ASIC Consultation Paper 382 (CP 382, February 2025) sets out modified obligations

**CRITICAL**: BNPL provider operating after 10 June 2025 without a credit licence and
without lodging a valid transitional application.

**HIGH**: Credit licence held but internal procedures not updated to reflect BNPL-specific
modified responsible lending obligations under RG 281.

#### 5.3 Financial Hardship Obligations (s 72 National Credit Code) [VERIFY]

- Consumer may apply for hardship variation at any time credit contract is in force
- Licensee must respond within **21 days** to a hardship request
- Available variations: extended loan term, reduced repayments, interest-only period,
  postponement, repayment holiday, capitalisation of arrears, interest rate reduction
- Financial hardship is an ASIC enforcement priority for 2024–2025 (see Step 9)
- ASIC enforcement action against NAB/AFSH: $15.5M penalty for financial hardship failures

**CRITICAL**: Systematic failure to process hardship requests, refusal to offer
hardship variations without proper assessment, or failure to respond within 21 days.

**HIGH**: Hardship procedures exist but are not consistently applied; timeframes
frequently exceeded; staff training on hardship is inadequate.

### Step 6: Design and Distribution Obligations Assessment (Pillar 3)

Applies to issuers and distributors of financial products for retail clients under
Part 7.8A Corporations Act. Skip for entities issuing wholesale-only products.

#### 6.1 Target Market Determination (TMD) Requirements (s 994B) [VERIFY]

**A TMD must be made before distributing any product to retail clients.** The TMD must:

- Describe the target market (class of consumers for whom the product is likely appropriate)
- Specify distribution conditions and restrictions
- State review triggers (events that would suggest the TMD is no longer appropriate)
- Set a review timeframe for the first and subsequent reviews
- Specify the frequency of complaint reports from distributors to the issuer
- Describe information requirements — data distributors must provide to the issuer

**CRITICAL**: Product distributed to retail clients without a TMD.

**HIGH**: TMD exists but does not adequately describe the target market, omits required
distribution conditions, or lacks specified review triggers and timeframes.

**MEDIUM**: TMD is technically compliant but review timeframes are significantly longer
than industry practice warrants, increasing risk that an outdated TMD remains operative.

#### 6.2 Distribution Obligations (s 994E) [VERIFY]

- Issuers and distributors must take **reasonable steps** to ensure distribution is
  consistent with the TMD
- Distributors must not distribute the product in a way that is not consistent with the TMD
- "Reasonable steps" are assessed by reference to: the nature of the product, the likely
  characteristics of the consumer, the steps available to the distributor, and ASIC guidance

**Check:**

- Does distribution documentation confirm consistency with TMD?
- Are distribution conditions operationalised in sales scripts, onboarding processes,
  and customer eligibility checks?
- Are distributors (including third-party distributors and referrers) trained on TMD
  requirements and distribution conditions?

#### 6.3 Significant Dealing Notification (s 994F) [VERIFY]

**Issuer obligations:**

- If a distributor notifies the issuer of a significant dealing (dealing inconsistent
  with the TMD), the issuer must notify ASIC within **10 business days** of becoming aware
- Notification made via ASIC Regulatory Portal online form

**Distributor obligations:**

- Distributors must notify issuers of significant dealings within **10 business days**
  of becoming aware
- "Significant dealing" — assessed by reference to the circumstances; no bright-line
  threshold; ASIC guidance (RG 274) provides factors to consider

**CRITICAL**: Significant dealing identified but not reported to ASIC; issuer not notified
by distributor within required timeframe.

**HIGH**: Monitoring systems do not capture information needed to identify potential
significant dealings; no documented process for escalating significant dealing notifications.

#### 6.4 Product Review Obligations (s 994C) [VERIFY]

- Issuers must review TMDs when review triggers occur and when required review
  periods expire
- Common review triggers: high volume of complaints, complaints indicating product
  is being distributed outside target market, regulatory changes affecting the product,
  market conditions materially changing product risk profile, significant dealings reported

**Check:**

- Are review trigger thresholds documented and operationally monitored?
- Is there a documented TMD review log evidencing completed reviews?
- Has the TMD been updated following any identified trigger events?

#### 6.5 Product Intervention Powers (Part 7.9A, ss 1023C–1023G) [VERIFY]

ASIC may make a product intervention order (PIO) if a financial product has resulted
in or is likely to result in significant detriment to retail clients. The assessment
should identify whether the entity's products are in categories where ASIC has
previously exercised PIP (e.g., short-term credit, CFDs, binary options, credit
insurance add-ons). Where ASIC has issued a PIO affecting the product category, confirm:

- Full compliance with the PIO conditions
- Internal monitoring for continuing PIO compliance
- Whether any PIO is subject to a sunset or review date

### Step 7: Internal Dispute Resolution Assessment (Pillar 4)

ASIC RG 271 (October 2021, IDR Data Reporting Handbook updated December 2025) applies
to AFS licensees, credit licensees, unlicensed product issuers, and certain other
ASIC-regulated entities.

#### 7.1 Complaint Handling Timeframes

| Category                                                           | Maximum IDR Timeframe                                                               | Notes                        |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------- | ---------------------------- |
| Standard complaints                                                | **30 calendar days**                                                                | Reduced from 45 days in 2021 |
| Financial difficulty complaints                                    | **21 calendar days**                                                                | Hardship context             |
| Superannuation/traditional trustee complaints                      | **45 calendar days**                                                                | Reduced from 90 days         |
| Complaints resolved within 5 business days (with consumer consent) | **Informal resolution** — no written IDR response required unless consumer requests | Exception pathway            |

**CRITICAL**: Systematic failure to meet complaint timeframes; no IDR procedure.

**HIGH**: IDR procedure exists but timeframes are consistently exceeded; no monitoring
of timeframe compliance.

#### 7.2 Written IDR Response Requirements (RG 271.87–271.99) [VERIFY]

A written IDR response is required when:

- The complainant requests one, OR
- The complaint involves: financial difficulty, a declined insurance claim, claim
  valuation dispute, or a superannuation trustee decision
- **Even if the complaint is resolved within 5 business days** in those categories

The written IDR response must:

- Clearly state whether the complaint is upheld or rejected
- Set out the key reasons for the decision
- Advise the complainant of their right to escalate to AFCA (and provide AFCA contact details)
- Be expressed in plain, accessible language

**HIGH**: Written IDR response not being provided when required; responses lack required
elements (AFCA referral information, key reasons).

**MEDIUM**: Written responses technically compliant but language is jargon-heavy, creating
risk that consumers do not understand their rights.

#### 7.3 Complaints Register and Data Quality (RG 271.133–271.150) [VERIFY]

The complaints register must:

- Record each complaint received (by date, category, product/service, outcome, timeframe)
- Enable ASIC's biannual IDR data reporting requirements to be met
- Use ASIC's prescribed data categories and product type classifications
- Capture complaints received through all channels (phone, in-person, email, online, mail)

**Updated IDR Data Reporting:**

- New IDR data reporting handbook published **1 December 2025**
- First submission under the updated handbook: **July–August 2026** window
- Covers complaints received/closed from **1 January 2026** onwards

**HIGH**: Complaints register does not capture all required data elements; categories
do not align with ASIC's prescribed classifications; data is not clean enough to support
biannual reporting.

**MEDIUM**: Register exists and reporting occurs but data quality is inconsistent
(missing fields, inconsistent categorisation, gaps in closed date recording).

#### 7.4 AFCA Referral Obligations

- AFS licensees and credit licensees must be members of AFCA
- IDR responses must advise complainants of their right to escalate to AFCA and
  provide AFCA's contact details
- AFCA membership must be current; confirm annual fee is paid and membership is active

**CRITICAL**: Entity is not a member of AFCA when membership is required.

**HIGH**: AFCA contact details not included in IDR responses; AFCA membership lapsed.

### Step 8: Breach Reporting Assessment (Pillar 5)

Under s 912DAA Corporations Act (operative from 1 October 2021) [VERIFY], AFS licensees
and credit licensees must report certain "reportable situations" to ASIC.

#### 8.1 What Must Be Reported — Reportable Situations

| Category                             | Trigger                                                                                                                                                                                                |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Significant breach**               | Licensee has reasonable grounds to believe a significant breach of a "core obligation" has occurred or is likely                                                                                       |
| **Ongoing investigation**            | An investigation into a potential breach has been commenced and is still ongoing after **30 days** — this is an automatic reportable situation on Day 31 regardless of whether a breach has been found |
| **Investigation conclusion**         | An investigation concludes (whether or not a breach is found) — if the investigation was reported as ongoing, the conclusion must also be reported                                                     |
| **Gross negligence / serious fraud** | Conduct of a licensee or representative constituting gross negligence or serious fraud                                                                                                                 |
| **Representative conduct**           | Conduct of financial advisers or mortgage brokers (as representatives of other licensees) in prescribed circumstances                                                                                  |

**"Core obligations"** include: s 912A general obligations, licence conditions, conduct
obligations under Chapter 7, and obligations under the National Credit Code [VERIFY for
current complete list per RG 78].

#### 8.2 What Constitutes a "Significant" Breach

A breach is significant if it is significant having regard to (all of): [VERIFY per RG 78]

- The number of clients affected
- The financial loss to clients
- Whether the breach was caused by intentional, reckless, or negligent conduct
- The duration of the breach
- The loss of consumer trust or confidence likely to result

**ASIC does not publish a bright-line threshold.** The determination requires a
qualitative, multi-factor analysis. Legal advice should be obtained for borderline cases.

#### 8.3 Reporting Timeframe

- **30 calendar days** after the licensee **first knows** (or is reckless as to whether)
  there are reasonable grounds to believe a reportable situation exists
- Note: The 30-day clock starts from the date of first knowledge — this can be **before**
  management or legal involvement (e.g., when a frontline staff member first identifies
  the incident)
- **Modified timeframe from 20 October 2023**: Where the current reportable situation
  has underlying circumstances that are the same as, or substantially similar to, a
  situation previously reported to ASIC, the timeframe is extended to **90 days** [VERIFY]

**CRITICAL**: No breach reporting procedure; material incidents not being assessed for
reportability; incidents assessed for reportability but not reported within 30 days.

**HIGH**: Breach reporting procedure exists but the 30-day clock is miscalculated
(typically: starting clock from management awareness rather than first knowledge, or
conflating the investigation conclusion with the initial report trigger).

**MEDIUM**: Procedure is technically correct but documentation trail is insufficient to
evidence the first knowledge date and the reasonable grounds determination.

#### 8.4 Breach Register

A breach register (or "reportable situations register") should:

- Record all incidents assessed for reportability (including non-reportable incidents
  with the reasons for that determination)
- Record the date of first knowledge, the date of report to ASIC, and the disposition
- Be maintained even for matters determined to be non-reportable (to evidence the
  assessment process)

### Step 9: Market Integrity Assessment (Pillar 6)

Applies primarily to listed entities, securities dealers, and market participants.
Skip for unlisted credit-only licensees with no market activity.

#### 9.1 Continuous Disclosure (Part 6CA, Corporations Act; ASX Listing Rule 3.1) [VERIFY]

Listed entities on ASX must immediately disclose any information that a reasonable
person would expect to have a material effect on the price or value of the entity's
securities, unless the information falls within the carve-outs (confidential, incomplete
negotiations, board consideration) [VERIFY current test post-2021 amendment].

**Post-2021 Amendment**: The continuous disclosure reforms in 2021 [VERIFY specific
amending Act] amended the test to require knowledge, recklessness, or negligence for
civil liability (removing strict liability for civil contraventions). Criminal liability
still requires intent.

**Assessment checks:**

- Does the entity have a board-approved continuous disclosure policy?
- Is the disclosure decision-making process documented and auditable?
- Are trading windows and blackout periods operationalised?
- Is there a designated disclosure committee and escalation process?

#### 9.2 Insider Trading (Part 7.10, ss 1042A–1043O) [VERIFY]

It is prohibited to trade in securities while in possession of inside information —
information that is not generally available and that a reasonable person would expect
to have a material effect on the price of the securities.

**Key features of the insider trading prohibition:**

- No requirement to prove the person used or relied upon the inside information — mere
  possession at the time of trading is sufficient
- No need to prove connection to a company — applies to any person with inside information
- Tipping liability (s 1043A(2)): communicating inside information to a third party who
  you know or ought to know may trade is also prohibited [VERIFY]

**Assessment checks:**

- Insider trading policy in place and signed by all officers and connected parties?
- Trading restriction notifications sent to connected parties before blackout periods?
- Information barriers (Chinese walls) implemented where different business units may
  hold inside information simultaneously?

#### 9.3 Market Manipulation (s 1041A) [VERIFY]

Prohibition on conduct (alone or with others) intended to create a false or misleading
appearance of trading activity or price/value of financial products.

**Assessment check**: For market participants — are trading surveillance systems in
place; does the compliance team review unusual trading patterns?

### Step 10: Sustainability Reporting Assessment (Pillar 7)

#### 10.1 Mandatory Climate Reporting (from 1 July 2026 for Group 1 Entities)

Under the Treasury Laws Amendment (Financial Market Infrastructure and Other Measures)
Act 2024 [VERIFY] and ASIC RG 280 (March 2025), mandatory sustainability reporting
applies on a phased basis:

| Group   | Threshold                                                                                | First Report                       |
| ------- | ---------------------------------------------------------------------------------------- | ---------------------------------- |
| Group 1 | ≥ 500 employees AND (≥ $1B consolidated assets OR ≥ $500M revenue) [VERIFY thresholds]   | FY commencing on/after 1 July 2025 |
| Group 2 | ≥ 250 employees AND (≥ $500M consolidated assets OR ≥ $200M revenue) [VERIFY thresholds] | FY commencing on/after 1 July 2026 |
| Group 3 | ≥ 100 employees AND (≥ $25M consolidated assets OR ≥ $50M revenue) [VERIFY thresholds]   | FY commencing on/after 1 July 2027 |

**Modified declaration (transitional)**: For the first 3 years (until 31 December 2027
[VERIFY]), directors may sign a "reasonable steps" declaration rather than a full
compliance declaration. This is a transitional protection, not an indefinite exemption.

**Assessment checks:**

- Has the entity determined which Group it falls into?
- Is a climate-related financial disclosure framework being implemented (AASB S1/S2)?
- Has a board declaration process been established?
- Is the entity's public climate-related communications (including investor reports and
  marketing) consistent with planned sustainability disclosures (greenwashing risk)?

#### 10.2 Greenwashing Enforcement Risk

ASIC has identified **sustainable finance and tackling greenwashing** as a top enforcement
priority for 2024–2025. Greenwashing encompasses:

- Misleading statements about environmental or sustainability credentials of products
- ESG/sustainability claims in marketing materials that are not supportable or are
  selectively measured
- Labelling investment products as "sustainable," "responsible," or "green" without
  robust underlying criteria

**Assessment check**: Review all investor-facing communications, product disclosure
statements, and marketing materials for sustainability claims. Apply the same
"misleading or deceptive conduct" standard as under ACL s 18 (which is mirrored in
ASIC Act s 12DA for financial services) [VERIFY].

---

## Severity Classification System

### Status Classification

| Status            | Meaning                                                                                                                    |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **COMPLIANT**     | Practice, procedure, or document meets current ASIC regulatory requirements. No action required.                           |
| **PARTIAL**       | Practice or procedure exists but contains gaps, outdated provisions, or inconsistent implementation. Remediation required. |
| **NON-COMPLIANT** | Practice, procedure, or document does not meet current ASIC regulatory requirements. Immediate remediation required.       |

### Risk Tier Classification

| Tier         | Criteria                                                                                                                                                           | Typical Penalty Exposure                                                                    | Timeline                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **CRITICAL** | Active or historical breach of a core ASIC obligation; reportable situation threshold likely met; significant client harm likely; ASIC enforcement action probable | Potential civil penalties; possible criminal referral; licence suspension/cancellation risk | Immediate (within 24–48 hrs): engage specialist counsel and assess breach reporting obligations |
| **HIGH**     | Material gap in compliance with a significant ASIC obligation; client harm possible but not yet demonstrated; ASIC surveillance or inquiry risk elevated           | Civil penalties if not remediated; ASIC improvement notice risk                             | Urgent (within 2–4 weeks): remediation plan and implementation                                  |
| **MEDIUM**   | Procedural gap that does not currently create direct client harm but represents a compliance risk that ASIC may identify on review                                 | Infringement notice; improvement notice                                                     | Near-term (within 1–3 months): scheduled remediation                                            |
| **LOW**      | Best practice gap; process improvement identified; minor documentation deficiency with no current compliance consequence                                           | No penalty risk; process improvement only                                                   | Background (within 6 months): include in annual compliance review cycle                         |

### Applying the Combined Classification

Use the combined notation `[STATUS] / [RISK TIER]` in all findings, e.g.:

- `NON-COMPLIANT / CRITICAL` — Breach of core obligation, immediate action required
- `PARTIAL / HIGH` — Procedure exists but material gap, urgent remediation required
- `PARTIAL / MEDIUM` — Procedure exists but process gap, near-term action required
- `COMPLIANT / LOW` — Compliant but opportunity for best practice improvement

---

## Actionable Output Per Finding

For every `NON-COMPLIANT / CRITICAL` or `NON-COMPLIANT / HIGH` finding, provide:

1. **Finding**: Precise description of the non-compliance (referencing the specific
   provision: e.g., "s 912A(1)(h) risk management systems — no documented risk
   management framework")
2. **Basis**: The legal authority (statute section + RG reference + any relevant case)
3. **Client harm pathway**: How this gap could result in client harm or regulatory action
4. **Breach reporting assessment**: Does this gap meet the threshold of a "reportable
   situation" under s 912DAA? (Yes / No / Uncertain — obtain legal advice)
5. **Remediation action**: Specific steps to remediate, in priority order
6. **Draft remediation language**: Draft policy text, procedure update, or document
   revision to achieve compliance (where feasible)
7. **Verification step**: How compliance can be evidenced after remediation
8. **Timeline**: Recommended remediation window (per risk tier)

For `PARTIAL` findings, provide:

1. **Finding**: What exists and what is missing
2. **Gap analysis**: Specific provisions or requirements not yet met
3. **Draft gap fill**: Targeted language or procedural steps to close the gap
4. **Verification step**: How the gap closure can be evidenced

---

## Prioritisation Framework

### Tier 1 — Immediate Action (CRITICAL findings)

Findings that may already constitute reportable situations under s 912DAA, create
immediate enforcement risk, or expose clients to ongoing harm. Take these actions
concurrently:

- **Engage specialist financial services counsel immediately**
- **Assess breach reporting obligation** — if the finding reveals a significant breach
  of a core obligation, the 30-day reporting clock may already be running
- **Preserve evidence** — do not destroy, alter, or remediate in a way that destroys
  the evidentiary record before taking legal advice
- **Brief board/senior management** within 24 hours
- **Implement interim protective measures** where possible (e.g., suspending the
  non-compliant product distribution pending TMD review)

### Tier 2 — Urgent Remediation (HIGH findings)

Material gaps that elevate ASIC surveillance or enforcement risk. Remediate within
2–4 weeks:

- Assign named responsible manager/owner for each remediation item
- Document the remediation plan with milestones
- Report progress to compliance committee at each milestone
- Update breach register to record assessment and monitoring

### Tier 3 — Scheduled Remediation (MEDIUM findings)

Process and documentation improvements that reduce compliance risk over time.
Include in the rolling compliance improvement program:

- Assign to the regular compliance improvement cycle
- Document in the compliance work plan with target completion dates
- Include in next internal audit scope

### Tier 4 — Best Practice (LOW findings)

Improvements that are not strictly required but reduce future compliance friction:

- Log in the compliance improvement register
- Consider at the next periodic review of compliance frameworks

---

## ASIC Enforcement Risk Profiling

### 2024–2025 ASIC Enforcement Priorities

Calibrate assessment severity against ASIC's stated enforcement priorities. Findings
in priority areas warrant elevation of risk tier by one level:

| Priority Area                                    | Assessment Calibration Note                                                                                                                          |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sustainable finance / greenwashing**           | Any sustainability claim in marketing or product disclosure triggers HIGH scrutiny — apply ASIC Act s 12DA test to all ESG assertions                |
| **DDO compliance in managed investment schemes** | ASIC's 2025 review found widespread TMD deficiencies — treat TMD gaps as HIGH even where currently only MEDIUM by severity alone                     |
| **Predatory lending practices**                  | High-cost credit products targeting vulnerable consumers — assess not just mechanical RLO compliance but overall suitability of product structure    |
| **Reportable situations regime**                 | ASIC is actively scrutinising breach reporting compliance — failure to report constitutes a second independent breach                                |
| **Insurance claims handling delays**             | Post-2021 financial services reforms — claims handling is now a financial service; delays in assessment trigger IDR and potentially breach reporting |
| **Financial hardship obligations**               | ASIC v NAB/AFSH ($15.5M) — systematic hardship failures attract large civil penalties                                                                |
| **Technology and operational resilience**        | ASIC v FIIG Securities ($2.5M for cyber security failures) — adequate risk management (s 912A(1)(h)) extends to cyber security controls              |
| **Superannuation member services failures**      | IDR and member communication failures in superannuation context                                                                                      |
| **Used car financing**                           | High-cost credit to vulnerable consumers — intersects responsible lending and predatory lending priorities                                           |

### Civil Penalty Regime

Under the Treasury Laws Amendment (Strengthening Corporate and Financial Sector
Penalties) Act 2019, the maximum civil penalties for Corporations Act contraventions
were significantly increased [VERIFY current penalty unit amounts]:

- **Penalty unit value**: $330 per unit (as of 7 November 2024) [VERIFY — updated
  periodically by CPI indexation]
- **Body corporate maximum**: Generally the greater of: (a) 50,000 penalty units
  ($16.5M at $330/unit) [VERIFY for specific provision]; OR (b) 3× the benefit obtained;
  OR (c) 10% of annual turnover
- **Individual maximum**: Generally 5,000 penalty units ($1.65M) [VERIFY for specific provision]

**Note**: The applicable maximum varies by provision. The figures above are indicative
only — verify the specific penalty maximum for the provision at issue.

**Recent enforcement benchmarks (use as calibration reference):**

| Case                                                      | Penalty             | Year | Provision                                |
| --------------------------------------------------------- | ------------------- | ---- | ---------------------------------------- |
| NAB/AFSH                                                  | $15.5M              | 2025 | Financial hardship failures              |
| FIIG Securities                                           | $2.5M + $500K costs | 2025 | Cyber security / s 912A risk management  |
| RM Capital & SMSF Club                                    | $575K + $350K       | 2025 | Conflicted remuneration breaches         |
| Lanterne Fund Services                                    | $1.25M              | 2024 | Six general obligation failures (s 912A) |
| [VERIFY all amounts and citation details before reliance] |                     |      |                                          |

---

## Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                                                                              | Fail Action                         |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every ASIC compliance assertion cites a specific statutory provision (e.g., s 912A(1)(a)) or identified regulatory guide (e.g., RG 271.87)                        | Add citation or mark [UNVERIFIED]   |
| **Format**     | All statutory citations follow the form: [Act name] [year] (Cth) s [section number]                                                                               | Fix format                          |
| **Currency**   | All cited provisions checked for amendments — particularly DDO (Oct 2021), breach reporting (Oct 2021), BNPL (Jun 2025), sustainability reporting (Jul 2026)      | Flag [CHECK CURRENCY]               |
| **Domain**     | Analysis stays within ASIC's regulatory scope — do not bleed in ACL, privacy law, or AML/CTF obligations without noting the separate framework                    | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty stated explicitly — particularly for penalty amounts (indexed annually), TMD "significant dealing" assessments, and significant breach determinations | Add confidence qualifier            |

---

## Self-Interrogation for CRITICAL Findings

For any finding classified as `NON-COMPLIANT / CRITICAL`, apply this 3-pass review
before including it in the output:

**Pass 1 — Legal chain integrity**: Does the CRITICAL classification follow logically
from the cited provision? Would ASIC and a court actually reach this conclusion on the
facts described? Is there a plausible compliance argument the entity could advance?

**Pass 2 — Completeness**: Have all relevant ASIC regulatory guides, class orders, and
relief instruments been considered? Could a legislative instrument or individual ASIC
relief apply that would modify the obligation? Is there a transitional arrangement that
might apply (e.g., BNPL June 2025 transitional)?

**Pass 3 — Challenge**: What is the strongest argument that this is not CRITICAL?
Under what circumstances might a reasonable financial services lawyer characterise this
as HIGH rather than CRITICAL? If there is a plausible HIGH classification, note this
and recommend specialist legal advice to determine the correct classification.

---

## Confidence Scoring

| Level        | Range     | Meaning                                                                           | Action                                                       |
| ------------ | --------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Definite** | 0.95–1.0  | Clear statutory obligation; no genuine interpretive uncertainty                   | State with confidence                                        |
| **High**     | 0.80–0.94 | Strong ASIC guidance or settled enforcement practice; minor questions             | State with brief caveat                                      |
| **Probable** | 0.60–0.79 | Good arguments for the position; reasonable counter-arguments exist               | State with reasoning and contra-indicators                   |
| **Possible** | 0.40–0.59 | Genuinely uncertain — e.g., "significant breach" threshold in novel circumstances | Flag for specialist legal review with both sides of argument |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                                                           | Do not assert; flag [UNCERTAIN]                              |

Apply confidence scoring most carefully to:

- Significant breach determinations (reportable situation or not?)
- "Reasonable steps" assessments for DDO distribution obligations
- Suitability of credit assessments in novel lending structures
- Greenwashing characterisations of marketing claims

---

## Glass Box Audit Trail

Include this YAML block at the end of every compliance assessment report:

```yaml
glass_box:
  skill_name: "legalcode-au-asic-regulatory-compliance"
  assessment_date: "[YYYY-MM-DD]"
  entity_type: "[AFS Licensee / Credit Licensee / Responsible Entity / Other]"
  products_services_assessed: "[List key products/services assessed]"
  assessment_scope:
    afsl_obligations: "[Assessed / Skipped — reason]"
    responsible_lending: "[Assessed / Skipped — reason]"
    ddo: "[Assessed / Skipped — reason]"
    idr: "[Assessed / Skipped — reason]"
    breach_reporting: "[Assessed / Skipped — reason]"
    market_integrity: "[Assessed / Skipped — reason]"
    sustainability_reporting: "[Assessed / Skipped — reason]"
  legalcode_mcp: "[Connected / Not connected]"
  citations_verified: "[N VERIFIED] / [N UNVERIFIED — marked [VERIFY]]"
  findings_summary:
    critical: "[N]"
    high: "[N]"
    medium: "[N]"
    low: "[N]"
  breach_reporting_triggered: "[Yes / No / Uncertain — obtain legal advice]"
  enforcement_risk_calibration: "[ASIC priority areas identified: list]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "[Any scope limitations, entity-specific assumptions, or areas not assessed]"
    - "All [VERIFY] tags require independent verification against current law before reliance"
    - "Significant breach and reportable situation determinations require specialist legal advice"
  reviewer: "AI-assisted — requires review by Australian financial services lawyer before reliance"
```

---

## Anti-Patterns

What NOT to do when assessing ASIC regulatory compliance:

1. **Treating AFSL obligations as a checklist** — s 912A(1)(a) ("efficient, honest and fair")
   is a principles-based obligation that cannot be reduced to a mechanical list. Assess the
   totality of the entity's conduct and culture, not just whether individual policies exist.

2. **Missing the 30-day breach reporting clock start** — The most common error is treating
   the breach reporting clock as starting from management awareness or legal involvement.
   The clock starts when any person in the organisation first has knowledge (or is reckless
   as to whether) reasonable grounds exist. Frontline staff findings can trigger the clock.

3. **Confusing the investigation trigger with the breach trigger** — A 30-day investigation
   is itself a reportable situation (automatic on Day 31) regardless of whether a breach
   is ultimately found. Do not wait for the investigation to conclude before assessing
   reportability.

4. **DDO compliance without operational evidence** — A TMD document alone does not establish
   DDO compliance. The distribution conditions must be operationalised — embedded in sales
   scripts, eligibility checks, distributor training, and monitoring systems.

5. **Treating RG 271 as IDR policy compliance only** — RG 271 compliance requires not just
   a compliant policy document but: a trained complaints-handling team, a functioning
   complaints register, accurate categorisation of complaints, biannual data reporting,
   and consistent application of the policy in practice. Policy without practice = PARTIAL.

6. **Ignoring BNPL** — From 10 June 2025, BNPL providers operating without a credit licence
   are in direct contravention of the NCCP Act. Do not assume pre-2025 BNPL operations
   are grandfathered without checking licence status.

7. **Applying standard ACL analysis to ASIC Act financial services** — The ASIC Act contains
   its own consumer protection provisions (ss 12BAA–12GBT) that parallel the ACL for
   financial products and services. The ACL does not directly apply to financial products —
   analyse the ASIC Act provisions, not ACL provisions, for financial product conduct.

8. **Underestimating the scope of DDO** — DDO applies to issuers of financial products for
   retail clients, not just to managed funds. Insurance products, superannuation funds,
   margin loans, structured products, and listed investment companies may all require TMDs.
   Do not assume DDO is limited to managed investment schemes.

9. **Treating "not yet enforced = compliant"** — ASIC's enforcement priorities shift annually.
   Greenwashing and DDO compliance were low-priority areas in 2020; they are top priorities
   in 2024–2025. The absence of prior enforcement action does not indicate compliance.

10. **Forgetting the ASIC Act parallel obligations** — For consumer-facing financial services
    conduct (misleading representations, unconscionable conduct), the ASIC Act s 12DA
    (misleading or deceptive conduct) is the operative provision — not ACL s 18.
    Ensure analysis cites the correct act.

11. **Missing the compensation arrangement obligation for PI insurance gaps** — If PI
    insurance lapses or contains coverage gaps, the entity immediately risks breaching s 912B
    (compensation arrangements) in addition to any underlying conduct breach. The s 912B
    breach may itself be reportable.

12. **Assuming wholesale-only exemption from DDO** — If any retail client is within scope
    of a financial product distribution, the product requires a TMD. Verify the actual
    client base against the retail/wholesale distinction under s 761G before concluding
    DDO does not apply.

13. **Ignoring the "significant dealing" notification chain** — Both the distributor's
    obligation to notify the issuer AND the issuer's obligation to notify ASIC are on
    10 business day clocks. An issuer who relies solely on the distributor to identify
    significant dealings without its own monitoring is exposed if the distributor fails
    to notify.

14. **Treating sustainability reporting as a future problem** — Group 1 entities (large
    entities) must report from 1 July 2026. The preparation period — governance framework,
    data systems, AASB S2 scenario analysis, board training — requires 12–18 months of
    lead time. An entity that has not commenced preparation by early 2025 is already behind.

15. **Confusing RG 209 "reasonable inquiries" with a fixed list** — The responsible lending
    obligation requires inquiries that are reasonable in the circumstances. What is reasonable
    varies with loan size, consumer vulnerability, product type, and broker involvement. A
    mechanical checklist without contextual assessment does not satisfy the obligation.

16. **Failing to assess representative conduct** — AFSL obligations extend to the conduct
    of authorised representatives. A licensee can breach s 912A through its representatives'
    conduct even where the licensee's own direct procedures are compliant. Representative
    training, supervision, and monitoring are integral to AFSL compliance.

17. **Underestimating cyber security as an ASIC risk** — Following ASIC v FIIG Securities
    (2025), inadequate cyber security controls constitute a breach of s 912A(1)(h) (risk
    management systems). Cyber security is not solely an IT matter; it is now a financial
    services regulatory compliance obligation.

18. **Delaying IDR data reporting setup** — The December 2025 updated IDR data reporting
    handbook changes data categories and product types. Entities that have not updated their
    complaints register to capture data under the new handbook before 1 January 2026 will
    be unable to comply with the July–August 2026 reporting obligation.

---

## Writing Standards

Before delivering the compliance assessment report, verify:

- [ ] **Plain language**: All findings expressed in plain English accessible to a compliance
      manager — not ASIC officer-style regulatory drafting
- [ ] **Specificity**: Each finding references the specific statutory provision (s 912A(1)(a))
      or regulatory guide reference (RG 271.87) — not generic descriptions ("IDR obligations")
- [ ] **Action-oriented**: Every finding is paired with at least one specific remediation action
- [ ] **[VERIFY] discipline**: All [VERIFY] tags are applied consistently; no statutory reference
      is presented as settled law without [VERIFY] unless verified via legalcode-mcp
- [ ] **No legal advice creep**: The report provides compliance analysis, not legal advice.
      For CRITICAL findings, the report recommends specialist legal counsel, not specific
      legal positions
- [ ] **Consistent classification**: Each finding uses the combined STATUS / RISK TIER notation
- [ ] **Breach reporting flag**: The report explicitly addresses whether any finding may
      constitute a reportable situation under s 912DAA and recommends legal review if uncertain
- [ ] **Penalty figures qualified**: All penalty figures are followed by [VERIFY — indexed
      annually] and a note that applicable maximums vary by provision

---

## External Tool Integration

### legalcode-mcp (Preferred)

Use legalcode-mcp in Step 3 to verify:

- Current text of Corporations Act ss 912A, 912DAA, Parts 7.8A, 7.9A, 7.10; NCCP Act
  ss 115–133; National Credit Code s 72
- Current penalty unit value (CPI-indexed annually from the base of $330 as at
  7 November 2024 [VERIFY])
- Recent ASIC enforcement actions in the Federal Court relating to the entity type
- Current operative versions of RG 78, RG 104, RG 105, RG 209, RG 271, RG 274, RG 280, RG 281

**Without legalcode-mcp:**

- Mark all statutory references with [VERIFY]
- Mark all regulatory guide references with [VERIFY — confirm current version on asic.gov.au]
- Focus the assessment on structural compliance gaps and process analysis rather than
  precise legislative text analysis
- Note in the Glass Box: `legalcode_mcp: "Not connected"`

### ASIC Regulatory Portal (Reference Only)

ASIC's online portal (regulatory.asic.gov.au) is the authoritative source for:

- Current AFSL licence details and authorisations
- Responsible manager nominations
- DDO significant dealing notification submission
- Breach reporting (reportable situations) lodgement
- IDR data reporting submissions

The skill does not interact with the ASIC Regulatory Portal directly. All portal
actions require authorised personnel of the regulated entity.

---

## Localization Notes

This skill is specific to Australian federal law (Commonwealth). Key localization notes:

- **States and territories**: All states and territories have referred their financial
  services and consumer credit powers to the Commonwealth. ASIC's regulatory framework
  applies nationally without state-specific variation.
- **ASX-listed entities**: Continuous disclosure obligations (Part 6CA and ASX Listing
  Rule 3.1) apply in addition to AFSL obligations. ASX Listing Rules are not legislation
  but are contractually binding on listed entities — treat breaches with equivalent
  seriousness to statutory breaches.
- **APRA intersection**: For entities regulated by both ASIC and APRA (superannuation
  funds, authorised deposit-taking institutions, insurance companies), this skill covers
  only ASIC-administered obligations. APRA prudential standards are a separate framework.
- **New Zealand**: ASIC's authority does not extend to New Zealand. For trans-Tasman
  financial services, the Financial Markets Conduct Act 2013 (NZ) applies to NZ operations.

---

## Output Format Template

```markdown
# ASIC Regulatory Compliance Assessment Report

## [Entity Name or Type]

**Assessment Date**: [YYYY-MM-DD]
**Prepared by**: Legalcode ASIC Compliance Skill (AI-assisted — requires legal review)
**Scope**: [Entity type, products/services, pillars assessed]
**Trigger**: [Proactive audit / ASIC inquiry / Incident response / Other]

---

## Executive Summary

**Overall compliance status**: [COMPLIANT / PARTIAL / NON-COMPLIANT]

| Pillar                               | Status         | Risk Tier    |
| ------------------------------------ | -------------- | ------------ |
| 1. AFSL General Obligations          | [STATUS]       | [TIER]       |
| 2. Responsible Lending (NCCP)        | [STATUS / N/A] | [TIER / N/A] |
| 3. Design and Distribution (DDO)     | [STATUS / N/A] | [TIER / N/A] |
| 4. Internal Dispute Resolution (IDR) | [STATUS]       | [TIER]       |
| 5. Breach Reporting                  | [STATUS]       | [TIER]       |
| 6. Market Integrity                  | [STATUS / N/A] | [TIER / N/A] |
| 7. Sustainability Reporting          | [STATUS]       | [TIER]       |

**Breach Reporting Assessment**: [No reportable situations identified / Potential reportable
situation identified — legal review required urgently / Reportable situation confirmed —
report to ASIC within [N] days]

**ASIC Enforcement Calibration**: [List priority areas activated by this assessment]

---

## Pillar 1: AFSL General Obligations

### Finding 1.1: [Finding title]

- **Status / Risk Tier**: [NON-COMPLIANT / CRITICAL]
- **Provision**: Corporations Act 2001 (Cth) s 912A(1)([x]) [VERIFY]; RG [N].[ para]
- **Description**: [Precise description of the non-compliance]
- **Client Harm Pathway**: [How this gap could result in client harm or regulatory action]
- **Breach Reporting Assessment**: [Yes / No / Uncertain — obtain legal advice]
- **Remediation Actions**:
  1. [First specific action]
  2. [Second specific action]
- **Draft Remediation Language**: [Draft policy text or procedure update]
- **Verification Step**: [How compliance is evidenced after remediation]
- **Timeline**: [Immediate / Within 2 weeks / Within 3 months]
- **Confidence**: [Level] — [Brief rationale]

[Repeat for each finding within this pillar]

---

## Pillar 2: Responsible Lending Conduct (NCCP Act)

[As above — repeat pattern for each pillar assessed]

---

## Pillar 3: Design and Distribution Obligations

[...]

---

## Pillar 4: Internal Dispute Resolution

[...]

---

## Pillar 5: Breach Reporting

[...]

---

## Pillar 6: Market Integrity

[...]

---

## Pillar 7: Sustainability Reporting

[...]

---

## Remediation Roadmap

### Tier 1 — Immediate Action (within 24–48 hours)

| Finding      | Action   | Owner | Deadline |
| ------------ | -------- | ----- | -------- |
| [Finding ID] | [Action] | [TBA] | [Date]   |

### Tier 2 — Urgent Remediation (within 2–4 weeks)

| Finding      | Action   | Owner | Deadline |
| ------------ | -------- | ----- | -------- |
| [Finding ID] | [Action] | [TBA] | [Date]   |

### Tier 3 — Scheduled Remediation (within 1–3 months)

| Finding | Action | Owner | Deadline |
| ------- | ------ | ----- | -------- |

### Tier 4 — Best Practice (within 6 months)

| Finding | Action | Owner | Deadline |
| ------- | ------ | ----- | -------- |

---

## Breach Reporting Summary

[Explicit section addressing whether any finding meets the threshold of a "reportable
situation" under s 912DAA Corporations Act. Must include one of:]

**No reportable situations identified**: Based on this assessment, no finding meets the
threshold of a significant breach of a core obligation under s 912DAA. However, this
assessment is AI-assisted and should be reviewed by specialist legal counsel before
reliance, particularly for any CRITICAL findings.

**[OR]**

**Potential reportable situation — urgent legal review required**: Finding [X] may
constitute a reportable situation under s 912DAA. The 30-day reporting clock may be
running. Engage specialist financial services counsel immediately.

---

## Glass Box Audit Trail

[Insert populated YAML template from the Glass Box Audit Trail section]

---

> **Important Notice**: This report is AI-assisted and does not constitute legal advice.
> All CRITICAL and HIGH findings require review by a qualified Australian financial
> services lawyer before reliance. All [VERIFY] tags must be confirmed against current
> law before acting. Significant breach and reportable situation determinations require
> specialist legal advice before any disclosure obligation is triggered.
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on:

- Corporations Act 2001 (Cth) Chapter 7, ss 912A, 912DAA, Parts 7.8A, 7.9A, 7.10
- National Consumer Credit Protection Act 2009 (Cth), Schedule 1 (National Credit Code)
- ASIC Regulatory Guides: RG 78, RG 104, RG 105, RG 121, RG 175, RG 209, RG 265,
  RG 271, RG 272, RG 274, RG 280, RG 281
- Financial Sector Reform (Hayne Royal Commission Response – Better Advice) Act 2021
- Treasury Laws Amendment (Design and Distribution Obligations and Product Intervention
  Powers) Act 2019
- Treasury Laws Amendment (Financial Market Infrastructure and Other Measures) Act 2024
- ASIC Corporate Plan 2024–25 (enforcement priorities)
- ASIC enforcement benchmarks: ASIC v FIIG Securities (2025), ASIC v NAB/AFSH (2025),
  ASIC v RM Capital & SMSF Club (2025), ASIC v Lanterne Fund Services (2024),
  ASIC v Money3 Loans Pty Ltd (2025)
- Legalcode quality frameworks from `legalcode-contract-review`, `legalcode-au-consumer-law-compliance`,
  and `legalcode-au-fair-work-compliance`
- Research methodology: Web-backed research via ASIC regulatory guides and enforcement
  publications; structural analysis using Legalcode 2-agent enhancement methodology
- All statutory and regulatory guide citations marked [VERIFY] unless independently
  confirmed. Verify current applicability before reliance.
