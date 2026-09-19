---
name: legalcode-boi-filing-prep
description: Prepares and audits Beneficial Ownership Information (BOI) reports for FinCEN under the Corporate
  Transparency Act (CTA), 31 U.S.C. § 5336.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Prepares and audits Beneficial Ownership Information (BOI) reports for FinCEN under the Corporate Transparency Act (CTA), 31 U.S.C. § 5336. Covers reporting company identification and exemption screening (including the March 2025 interim final rule exempting domestic U.S. entities), beneficial owner determination using the 25% ownership threshold and substantial control four-category test, company applicant identification, FinCEN ID strategy, required information gathering and document checklist, filing deadlines and update obligations (30-day change window), correction safe harbor (90 days), civil and criminal penalty exposure, and ongoing compliance monitoring. Use this skill whenever a client asks whether they must file a BOI report, who qualifies as a beneficial owner, when a report is due, how to update or correct a prior filing, or what information FinCEN requires. Also triggers for "Corporate Transparency Act compliance," "CTA reporting," "FinCEN beneficial ownership," "BOIR filing," or any question about exemptions from BOI reporting obligations.


# BOI Filing Preparation — Corporate Transparency Act

> **Disclaimer**: This skill provides a framework for AI-assisted BOI compliance preparation.
> It does not constitute legal advice. All outputs must be reviewed by a qualified attorney
> licensed in the relevant jurisdiction before filing. The Corporate Transparency Act is
> subject to ongoing litigation and regulatory change — including the March 26, 2025 interim
> final rule significantly narrowing its scope — and the current requirements may differ
> materially from this skill's descriptions. AI systems can hallucinate legal citations,
> misapply exemption criteria, and miss fact-specific compliance considerations; never file
> a BOIR without independent professional review. Verify all regulatory references against
> current FinCEN guidance at fincen.gov/boi before relying on them.

---

## Purpose and Scope

This skill prepares attorneys, compliance officers, and business owners to complete,
update, and maintain Beneficial Ownership Information (BOI) reports submitted to FinCEN
under the Corporate Transparency Act (CTA). It provides a structured workflow for
determining:

- Whether an entity is a "reporting company" subject to CTA obligations
- Which individuals qualify as "beneficial owners" under the ownership and control tests
- Which individuals qualify as "company applicants"
- What information and documents must be gathered for each required person
- When initial, updated, and corrected BOIRs are due
- How to use the FinCEN Identifier (FinCEN ID) system to simplify reporting
- What civil and criminal penalties apply and how to preserve safe harbor protection

**Covers:**

- Reporting company definition and all 23 exemption categories
- Large operating company exemption (three-prong analysis)
- Subsidiary exemption rules
- 25% ownership threshold calculation (direct, indirect, through intermediaries)
- Substantial control four-category test (senior officers, appointment authority, important decisions, catch-all)
- Exempt beneficial owner categories (minors, nominees, employees, heirs, creditors)
- Company applicant identification and address rules
- Required information for each beneficial owner and company applicant
- Acceptable identifying documents and FinCEN ID strategy
- Initial filing deadlines (current and historical)
- 30-day update obligation after changes
- 90-day correction safe harbor
- Civil penalties ($500/day) and criminal penalties (up to $10,000 / 2 years imprisonment)
- Current legal status: March 2025 interim final rule and ongoing litigation
- BOI E-Filing System submission process

**Does not:**

- Substitute for review by qualified legal counsel
- Address state-level beneficial ownership or similar reporting requirements
- Cover beneficial ownership reporting for financial institutions under the FinCEN CDD Rule
  (31 C.F.R. § 1010.230) — see `legalcode-aml-kyc-compliance` for that framework
- Provide definitive legal advice on the constitutionality of the CTA (currently disputed
  in multiple federal circuits) or the binding effect of the interim final rule
- Replace independent verification of exemption status with FinCEN's current published guidance

**Related skills:**

- `legalcode-aml-kyc-compliance` — AML/BSA compliance including FinCEN CDD Rule beneficial
  ownership requirements for financial institutions
- `legalcode-entity-formation-advisor` — Entity selection with BOI post-formation obligations
- `legalcode-corporate-governance-audit` — Governance review including ownership structure analysis

---

## Jurisdiction and Governing Law

**Primary jurisdiction**: United States (federal)

**Governing statute**: Corporate Transparency Act, 31 U.S.C. § 5336 (enacted as part of the
National Defense Authorization Act for FY2021, Pub. L. 116-283, Div. F, §§ 6001–6403)

**Implementing regulation**: 31 C.F.R. § 1010.380 (FinCEN's Beneficial Ownership Information
Reporting Rule, effective January 1, 2024)

**Administering agency**: Financial Crimes Enforcement Network (FinCEN), U.S. Department of
the Treasury

### Critical Regulatory Status (as of March 2026)

**March 26, 2025 Interim Final Rule** — FinCEN published an interim final rule that
fundamentally narrowed the CTA's scope:

- **All U.S. domestic entities are now exempt** from BOI reporting requirements
- **All U.S. persons are exempt** from reporting as beneficial owners or company applicants
- **Only foreign entities** registered to do business in U.S. states or tribal jurisdictions
  remain subject to BOI reporting obligations
- FinCEN has indicated intent to finalize this rule by late 2025/early 2026 [VERIFY current
  finalization status]

**Ongoing Litigation** — The CTA's constitutionality remains disputed:

- _Texas Top Cop Shop, Inc. v. Garland_ (E.D. Tex.): nationwide injunction issued December 2024
- _Smith v. U.S. Department of the Treasury_ (E.D. Tex.): second nationwide injunction
- U.S. Supreme Court stayed the first injunction (January 2025) but a second injunction
  briefly remained
- Eleventh Circuit upheld CTA's constitutionality on December 16, 2025 [VERIFY]
- Circuit split continues; Supreme Court review remains possible

**Practice guidance**: Always verify current FinCEN guidance at fincen.gov/boi before filing.
The skill's substantive analysis reflects the full CTA framework; apply the applicability
determination gate in Step 3 to screen for the interim rule exemption.

---

## Interactive Clarification

This skill uses **⟁ CLARIFY** markers at key decision points. When the symbol appears, pause
and gather the indicated information before proceeding. The answer will materially change which
sections apply, what information must be gathered, and what deadlines govern. If the user has
already provided the information, skip the question and continue.

Batch/non-interactive runs may proceed with disclosed assumptions where marked.

---

## Workflow

### Step 1: Accept Input and Establish Context

Accept any of the following inputs:

- Entity name, formation jurisdiction, and description of ownership/governance structure
- Existing BOIR draft or filed report (for update/correction review)
- Specific question about applicability, beneficial owner identification, or deadlines
- Client questionnaire or intake form

**⟁ CLARIFY** — Engagement context

**Option A: Initial filing preparation**

- New entity has not yet filed a BOIR
- _Why this matters_: Determines whether focus is on deadline compliance, initial
  data gathering, or both

**Option B: Update to existing filing**

- Entity has filed and a reportable change has occurred
- _Why this matters_: Triggers 30-day update analysis; need to identify what changed
  and whether update deadline has been met or missed

**Option C: Correction of prior filing**

- Entity filed an inaccurate BOIR and needs to correct it
- _Why this matters_: Triggers 90-day safe harbor analysis and correction procedure

**Option D: Applicability assessment only**

- Determine whether entity must file at all
- _Why this matters_: Steps 2–4 are the complete deliverable; later data-gathering
  steps apply only if entity is a reporting company

**Option E: Audit of existing compliance program**

- Review existing BOI records, processes, and tracking systems
- _Why this matters_: Expands scope to ongoing monitoring and update tracking

---

### Step 2: Identify the Entity and Formation Jurisdiction

Gather the following information about the entity before proceeding:

| Item                           | Required Detail                                                          |
| ------------------------------ | ------------------------------------------------------------------------ |
| Legal name                     | Full registered legal name                                               |
| Trade names / DBAs             | All "doing business as" names and assumed names                          |
| Entity type                    | Corporation, LLC, limited partnership, etc.                              |
| Formation jurisdiction         | U.S. state, Indian tribe, or foreign country                             |
| Date of formation/registration | Exact date document was filed with secretary of state                    |
| Principal business address     | Physical street address (not P.O. Box) of primary operations             |
| EIN / TIN                      | Employer Identification Number or Taxpayer ID                            |
| U.S. registration states       | Any U.S. states where a foreign entity has registered to do business     |
| Ownership structure            | Summary of how the entity is owned (individuals, entities, trusts, etc.) |
| Governance structure           | Officers, directors, managers, general partners                          |

---

### Step 3: Reporting Company Applicability Gate

**⟁ CLARIFY** — Is the entity domestic (formed in a U.S. state) or foreign (formed abroad)?

**Option A: Domestic U.S. entity** (formed under a U.S. state's laws)

- Under the March 26, 2025 interim final rule, **domestic entities are currently exempt**
  from BOI reporting
- _Why this matters_: If interim rule applies and holds, no filing is required; analysis
  ends here for now, but client should monitor for rule finalization or court-ordered
  resumption of broader obligations
- Proceed to **Step 3a** for domestic exemption analysis

**Option B: Foreign entity registered to do business in a U.S. state**

- Foreign entities remain subject to BOI reporting under the interim rule
- _Why this matters_: Filing is required; proceed through full workflow
- Proceed to **Step 3b** for foreign entity analysis

#### Step 3a: Domestic Entity — Current Exemption Status

Under the March 2025 interim final rule (31 C.F.R. § 1010.380 as amended), domestic
reporting companies are exempted from BOI reporting requirements. Advise the client:

1. **Current status**: No BOI reporting obligation under the interim rule
2. **Monitoring obligation**: The interim final rule has not been finalized [VERIFY]; monitor
   FinCEN's rulemaking docket for finalization or legislative changes
3. **Litigation risk**: If a court invalidates the interim rule or the CTA is reinstated
   in its original scope, reporting obligations may resume — potentially with compressed
   deadlines
4. **Recommended action**: Maintain a complete beneficial ownership record internally even
   if no BOIR filing is currently required; this minimizes disruption if obligations resume

Document this exemption determination in the Glass Box audit trail and proceed to Step 10
(output) with an applicability determination of EXEMPT — INTERIM RULE.

**⟁ CLARIFY** — Does the client also want analysis under the original CTA framework (i.e.,
as if the interim rule did not apply)? This may be useful for contingency planning if the
interim rule is rescinded.

**Option A: Yes — analyze under full CTA framework for contingency planning**

- Proceed through Steps 3b–9 with hypothetical reporting company status
- Mark all findings as contingent on restoration of original CTA scope

**Option B: No — current exemption analysis is sufficient**

- Document exemption and proceed to Step 10

#### Step 3b: Foreign Entity — 23-Exemption Screening

For foreign entities, apply the 23 exemption categories sequentially. If the entity meets
any exemption, it is not a reporting company for that category.

**Exemption 1 — SEC-Registered Issuers**: Securities listed on a U.S. national exchange
(§ 12 of the Securities Exchange Act of 1934) or required to file reports under § 15(d)

**Exemption 2 — Investment Companies**: Registered under the Investment Company Act of 1940

**Exemption 3 — Investment Advisers**: Registered with the SEC under the Investment Advisers
Act of 1940

**Exemption 4 — Commodity Pool Operators**: Registered with the CFTC

**Exemption 5 — Commodity Trading Advisers**: Registered with the CFTC

**Exemption 6 — Banks**: As defined in 12 U.S.C. § 1813 or 12 U.S.C. § 1813(a)(1)

**Exemption 7 — Credit Unions**: As defined in 12 U.S.C. § 1752

**Exemption 8 — Bank Holding Companies**: As defined in 12 U.S.C. § 1841

**Exemption 9 — Savings and Loan Holding Companies**: As defined in 12 U.S.C. § 1467a

**Exemption 10 — Registered Brokers or Dealers**: As defined in § 3 of the Securities
Exchange Act of 1934, registered under § 15

**Exemption 11 — Money Services Businesses**: Registered as an MSB under 31 C.F.R. § 1022.380

**Exemption 12 — Insurance Companies**: Domiciled in a U.S. state and subject to the
supervision of a state insurance commissioner

**Exemption 13 — State-Licensed Insurance Producers**: Authorized by state law and subject
to state insurance commissioner supervision

**Exemption 14 — Registered Entities Under Commodity Exchange Act**: Subject to CFTC
oversight per § 4(k) of the CEA

**Exemption 15 — Accounting Firms**: Regulated by a state board of accountancy

**Exemption 16 — Public Utilities**: Subject to regulation under applicable law

**Exemption 17 — Financial Market Utilities**: Designated under Title VIII of the Dodd-Frank Act

**Exemption 18 — Pooled Investment Vehicles**: Operated/advised by an exempt investment adviser,
broker-dealer, bank, or credit union

**Exemption 19 — Tax-Exempt Organizations**: 26 U.S.C. § 501(c) organizations, §§ 527/4947(a)(1)
political organizations; in each case, with IRS determination letters

**Exemption 20 — Entity Assisting Tax-Exempt Organizations**: Controlled exclusively by
tax-exempt organizations

**Exemption 21 — Large Operating Companies** (see detailed three-prong analysis below)

**Exemption 22 — Subsidiaries of Exempt Entities**: Ownership interests 100% owned and
controlled by one or more exempt entities

**Exemption 23 — Inactive Entities**: Formed before January 1, 2020; not engaged in active
business; not owned by a foreign person; no changes in ownership in prior 12 months;
not sent or received funds >$1,000 in prior 12 months; holds no assets

**Classification**: Apply each exemption and document:

- ✅ EXEMPT — with citation to applicable exemption number and authority
- ❌ NOT EXEMPT — with brief explanation of why the exemption does not apply
- ⚠️ UNCERTAIN — fact-specific inquiry needed; flag for counsel

#### Step 3c: Large Operating Company Exemption — Three-Prong Analysis

This exemption requires **all three prongs** to be satisfied simultaneously. Failure on any
single prong disqualifies the entity.

**Prong 1 — U.S. Employee Headcount (>20 full-time employees)**

- Count only full-time employees (≥30 hours/week or ≥130 hours/calendar month)
- Count only employees located in the United States
- ⚠️ CRITICAL: Employee counts **cannot be aggregated across affiliated entities** — each
  entity applies the threshold to its own employees only
- Part-time and contract workers do not count toward the 20-employee threshold
- Temporary employees provided by a staffing agency count for the staffing agency, not the
  entity using their services [VERIFY]

**Prong 2 — Physical U.S. Office**

- Entity must maintain and operate a physical office location in the United States
- Office must be owned or leased by the entity
- Must be regularly occupied for business operations
- Virtual offices, registered agent addresses, and co-working space (without dedicated tenancy)
  do not satisfy this requirement [VERIFY current FinCEN guidance]
- Remote-only workforces do not satisfy this prong even if employees are U.S.-based

**Prong 3 — Prior-Year Revenue (>$5,000,000 gross receipts or sales)**

- Revenue demonstrated by filing a federal income tax or information return for the prior
  calendar year showing >$5,000,000 in gross receipts or sales
- Revenue **may be calculated on a consolidated basis** across affiliated entities (unlike
  the employee headcount prong)
- New entities that have not yet filed a prior-year return may not immediately qualify

**Common trap**: Many entities aggregate employee headcounts across subsidiaries to reach
the 20-employee threshold. FinCEN regulations expressly prohibit this; each entity must
independently satisfy the employee prong.

#### Step 3d: Subsidiary Exemption Analysis

An entity qualifies for the subsidiary exemption only if:

- 100% of its ownership interests are owned and controlled by one or more exempt entities
- Any fractional non-exempt ownership (e.g., 99% exempt / 1% non-exempt) destroys the
  exemption
- The controlling exempt entity itself must independently qualify for its exemption

---

### Step 4: Identify Company Applicants (Entities Formed After January 1, 2024)

For reporting companies formed or registered on or after January 1, 2024:

**Definition**: A company applicant is any individual who:

1. **Directly files** the document creating (domestic) or registering (foreign) the company
   with a secretary of state or equivalent office; **or**
2. **Directs or controls** the filing of that document — typically the attorney, compliance
   officer, or supervising professional who instructs the direct filer

**Maximum of two company applicants** per reporting company. If only one individual both
directed and executed the filing, report only one.

**⟁ CLARIFY** — Business vs. residential address for company applicants

**Option A: Company applicant works in entity formation as a regular business activity**
(e.g., attorney at a law firm, registered agent, corporate service provider)

- Use the company applicant's **business street address**

**Option B: Company applicant is an employee, officer, or owner filing as a one-time act**

- Use the company applicant's **current residential street address**

Gather for each company applicant:

- Full legal name
- Date of birth
- Current street address (business or residential per above)
- Unique identifying number from an acceptable document
- Jurisdiction issuing the document
- Image of the identifying document (or FinCEN ID if the applicant has one)

---

### Step 5: Beneficial Owner Determination

Apply both prongs of the beneficial owner definition. An individual is a beneficial owner if
they satisfy **either** prong (ownership threshold **or** substantial control).

#### Step 5a: 25% Ownership Threshold Analysis

**Direct ownership**: Calculate the individual's direct percentage ownership stake in the
reporting company.

**Indirect ownership through entities**: Trace through each layer of intermediary entities
by multiplying ownership percentages at each level.

_Example_: Maria owns 60% of Entity A. Entity A owns 40% of the reporting company.
Maria's indirect ownership = 60% × 40% = 24% (below threshold).
But if Maria also owns 5% directly, her total ownership = 24% + 5% = 29% (meets threshold).

**Treatment of instruments**: Options, warrants, and convertible instruments are treated as
if fully exercised when calculating ownership percentages.

**Complex/uncertain structures**: If the structure is sufficiently complex that precise
calculation is impossible, any individual who **could** own ≥25% under any reasonable
interpretation should be treated as a beneficial owner.

**For each potential 25% owner, document**:

- Name and ownership calculation methodology
- Whether ownership is direct, indirect, or combined
- Any instruments included in the calculation
- Resulting percentage: MEETS THRESHOLD (≥25%) / BELOW THRESHOLD (<25%)

#### Step 5b: Substantial Control Four-Category Test

An individual exercises substantial control through **any one** of the following:

**Category 1 — Senior Officers**

Report any individual holding any of these positions, by title or function:

- President
- Chief Executive Officer (CEO)
- Chief Financial Officer (CFO)
- Chief Operating Officer (COO)
- General Counsel
- Any individual performing **substantially similar functions** regardless of title

_Note_: Title is not controlling. An individual called "Managing Director" who performs
the functions of a CEO is a senior officer. An individual called "CEO" who is a figurehead
with no actual authority may not be a senior officer [VERIFY on specific facts].

**Category 2 — Authority to Appoint or Remove Senior Officers or Board Members**

Report any individual with authority to:

- Appoint or remove a senior officer
- Appoint, remove, or replace a majority of the board of directors (or equivalent governing
  body)

_Example_: A majority shareholder with the contractual right to designate a majority of
directors exercises substantial control under Category 2 even if they own less than 25%.

**Category 3 — Important Decision Authority**

Report any individual who directs, determines, or has **substantial influence** over
important decisions of the reporting company, including:

_Business decisions_: Strategic direction, business focus, creation or termination of ventures,
significant operational changes

_Financial decisions_: Major asset transactions/dispositions, capital allocation, significant
budget approvals, financial restructuring, debt financing above ordinary course thresholds

_Structural decisions_: Corporate reorganizations, mergers/acquisitions, amendments to
governance documents, subsidiary creation or dissolution, capital structure changes

**Category 4 — Any Other Form of Substantial Control**

Catch-all category designed to prevent evasion through creative structures. May include:

- Contractual veto rights over key decisions
- Control through information rights that enable direction of the entity
- Control through key customer or supplier relationships managed by the individual
- De facto control exercised through influence over other officers or directors

**For each potential substantial control holder, document**:

- Name and which category (1–4) applies
- Specific facts supporting the classification
- Classification: SUBSTANTIAL CONTROL / NOT APPLICABLE / UNCERTAIN (flag for counsel)

#### Step 5c: Exempt Beneficial Owners

Do NOT report the following individuals even if they meet the ownership or control tests:

| Exempt Category           | Conditions                                                                                 | Caveat                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| Minor children            | Individual has not reached the age of majority under applicable state law                  | Report the parent's or guardian's information instead; update report when minor reaches majority |
| Nominees / intermediaries | Individual acts solely on behalf of another person                                         | The actual beneficial owner (principal) must be reported                                         |
| Employees                 | Acting solely as an employee; control/economic benefit derives exclusively from employment | Does NOT exempt senior officers (Category 1 above)                                               |
| Heirs                     | Interest is solely a future right of inheritance not yet vested                            | Once interest vests, individual becomes a beneficial owner                                       |
| Creditors                 | Bona fide creditor with a predetermined, fixed-amount debt                                 | Conversion rights, profit participation, or covenant-based control may destroy this exemption    |

---

### Step 6: Required Information Gathering

Once all beneficial owners and company applicants are identified, gather the following:

#### For the Reporting Company

| Field                           | Detail                                                         |
| ------------------------------- | -------------------------------------------------------------- |
| Legal name                      | Full registered legal name                                     |
| Trade names                     | All DBAs and assumed names                                     |
| EIN/TIN                         | Employer Identification Number or Taxpayer ID                  |
| Principal business address      | Physical street address (no P.O. Box); city, state, ZIP        |
| Jurisdiction of formation       | State (domestic) or country (foreign)                          |
| U.S. registration jurisdictions | Each state where a foreign entity is registered to do business |

#### For Each Beneficial Owner and Company Applicant

| Field                              | Detail                                                                                         |
| ---------------------------------- | ---------------------------------------------------------------------------------------------- |
| Full legal name                    | As it appears on the identifying document                                                      |
| Date of birth                      | Exact date; must match the identifying document                                                |
| Current residential street address | Physical address; for company applicants who form entities as a business, use business address |
| Unique identifying number          | From an acceptable document (see below)                                                        |
| Document jurisdiction              | State or country issuing the document                                                          |
| Document image                     | Legible scan or photograph of the front of the document                                        |

#### Acceptable Identifying Documents (Preference Order)

1. U.S. passport
2. State-issued driver's license
3. State-issued identification card (non-driver)
4. U.S. military identification
5. Foreign passport (only if no U.S. document is available)
6. Document issued by a foreign government, Indian tribe, or U.S. territory

**Document image requirements**: The image must be legible, clearly show the identifying
number, and be in a format accepted by FinCEN's BOI E-Filing System (JPEG, PNG, or PDF).

#### FinCEN Identifier (FinCEN ID) Strategy

A FinCEN ID is a 12-digit number issued by FinCEN upon request. When a beneficial owner
or company applicant supplies their FinCEN ID, the reporting company may submit the FinCEN
ID **in lieu of** all personal information for that individual (name, DOB, address, document
number, jurisdiction, and image).

**When a FinCEN ID is advantageous**:

- Individual appears as a beneficial owner or company applicant in multiple reporting companies
- Individual prefers to minimize disclosure of personal information across multiple filings
- Update management is simplified: if the individual updates their FinCEN ID record, each
  associated reporting company's BOIR is automatically current for that individual's information

**How to obtain a FinCEN ID**: Apply at fincenid.fincen.gov (no cost; immediate issuance
upon approval after providing the same personal information that would otherwise appear in
the BOIR).

**Limitation**: A reporting company using a FinCEN ID for a beneficial owner remains
responsible for ensuring the underlying information is accurate.

---

### Step 7: Filing Deadlines and Update Obligations

**⟁ CLARIFY** — Entity type and registration date for deadline calculation

**Option A: Foreign entity registered before March 26, 2025**

- Initial BOIR deadline: **April 25, 2025** [VERIFY — confirm whether this deadline
  has passed and whether any extensions have been granted]
- If deadline has passed without filing, advise on penalty exposure and remediation

**Option B: Foreign entity first registered on or after March 26, 2025**

- Initial BOIR deadline: **30 calendar days** from the date the entity receives notice
  of its registration (typically the date the secretary of state issues the certificate
  of authority or equivalent)

**Option C: Domestic entity analyzing obligations under the original CTA framework**
(contingency planning if the March 2025 interim rule is rescinded)

- Entities formed before January 1, 2024: Original deadline was January 1, 2025
- Entities formed January 1 – December 31, 2024: 90 calendar days from formation notice
- Entities formed on or after January 1, 2025: 30 calendar days from formation notice

#### Update Obligation (30-Day Rule)

A reporting company must file an updated BOIR within **30 calendar days** of any change to:

- The identity of a beneficial owner (addition, removal, or change in qualifying status)
- The personal information of a beneficial owner (address, legal name change, new identifying
  document)
- The identity or information of a company applicant
- Any information about the reporting company itself (legal name, address, EIN, trade names)

**Monitoring triggers to establish**:

- Officer/director appointments and resignations
- Ownership transfers of any stake (not just transfers crossing the 25% threshold)
- Changes in control arrangements or shareholder agreements
- Address changes for beneficial owners
- Passport/driver's license renewals or reissuances
- Mergers, reorganizations, or structural changes

#### Correction Safe Harbor

If a BOIR contains inaccurate information, the reporting company may correct it voluntarily:

- Corrections filed within **90 days** of the original filing deadline: civil and criminal
  penalty safe harbor applies (good faith correction)
- Corrections filed after 90 days: no safe harbor; penalties may apply, but correction is
  still required and will be considered in enforcement discretion
- Intentional misstatements are not protected by the safe harbor regardless of when corrected

---

### Step 8: Penalty Exposure Analysis

Apply this assessment when a potential violation has occurred or is at risk:

| Violation Type                                           | Civil Penalty             | Criminal Penalty                                         |
| -------------------------------------------------------- | ------------------------- | -------------------------------------------------------- |
| Failure to file BOIR by deadline                         | Up to $500/day (accruing) | Up to $10,000 fine and/or 2 years imprisonment (willful) |
| Failure to update BOIR within 30 days                    | Up to $500/day (accruing) | Same as above                                            |
| Filing false or fraudulent information                   | Up to $500/day            | Up to $10,000 fine and/or 2 years imprisonment           |
| Willful violation while committing another federal crime | Enhanced                  | Up to $250,000–$500,000 and/or 5–10 years imprisonment   |

**Civil penalty cap**: The $500/day civil penalty accrues up to a maximum of **$10,000** per
violation (31 U.S.C. § 5336(h)(3)(A)) [VERIFY current penalty amounts, as FinCEN may adjust
for inflation].

**Willfulness**: Criminal penalties require proof that the individual **knew** of the filing
obligation and **intentionally** disregarded it. Innocent mistake or good-faith
misinterpretation of the law is generally not willful. Receiving professional legal advice
that the entity was exempt — even if incorrect — may support a non-willfulness defense.

**Senior officer liability**: Senior officers who **cause** a reporting company to violate
its BOI obligations may face personal civil and criminal liability even if they are not
themselves the reporting company.

**Remediation approach when a violation has occurred**:

1. File the overdue BOIR immediately
2. Document the reason for the delay and any good-faith reliance on legal advice
3. If within the 90-day correction window, file corrected BOIR
4. Preserve all documentation of beneficial owner research methodology
5. Consult with criminal defense/white-collar counsel if willfulness is arguable

---

### Step 9: Classify Filing Readiness

Assign each required element a filing readiness classification:

| Status         | Symbol | Meaning                                                                                |
| -------------- | ------ | -------------------------------------------------------------------------------------- |
| **COMPLETE**   | ✅     | Information is accurate, documented, and ready for submission                          |
| **INCOMPLETE** | ⚠️     | Information is partially gathered; clarification or additional detail needed           |
| **MISSING**    | ❌     | Required element is absent; cannot proceed to filing without remediation               |
| **CRITICAL**   | 🚨     | Absence or error would trigger BOIR rejection or penalty exposure; address immediately |

Apply this classification to each section of the output template:

- Reporting company information
- Each beneficial owner's information
- Each company applicant's information (if applicable)
- Filing deadline status
- Document image quality and completeness

---

### Step 10: Prepare Output and Deliver

Deliver the BOI Filing Preparation Report using the output format template in the final
section. Include:

1. Executive summary with overall filing readiness status
2. Applicability determination with exemption analysis
3. Beneficial owner register with classification status for each individual
4. Company applicant information (if applicable)
5. Required information checklist with status per field
6. Filing deadline summary and update obligation triggers
7. Remediation roadmap for any MISSING or CRITICAL items
8. Glass Box Audit Trail

---

## BOI Filing Reference Framework

### The Two-Prong Beneficial Owner Test (Decision Tree)

```
For each individual connected to the reporting company:
│
├─ Does the individual own ≥25% of any class/type of ownership interests
│  (directly, indirectly, or through instruments treated as exercised)?
│  │
│  ├─ YES → BENEFICIAL OWNER (ownership prong)
│  │
│  └─ NO → Continue to control analysis
│
├─ Does the individual serve as a senior officer (President/CEO/CFO/COO/GC
│  or functional equivalent)?
│  │
│  ├─ YES → BENEFICIAL OWNER (control prong, Category 1)
│  │
│  └─ NO → Continue
│
├─ Does the individual have authority to appoint/remove senior officers or
│  a majority of the board of directors?
│  │
│  ├─ YES → BENEFICIAL OWNER (control prong, Category 2)
│  │
│  └─ NO → Continue
│
├─ Does the individual direct, determine, or have substantial influence over
│  important business, financial, or structural decisions?
│  │
│  ├─ YES → BENEFICIAL OWNER (control prong, Category 3)
│  │
│  └─ NO → Continue
│
├─ Does the individual exercise any other form of substantial control?
│  │
│  ├─ YES → BENEFICIAL OWNER (control prong, Category 4)
│  │
│  └─ NO → NOT A BENEFICIAL OWNER for this reporting company
│
└─ Apply exempt beneficial owner categories: minors, nominees, employees
   (not senior officers), heirs, bona fide creditors
```

### 23 Exemption Category Quick Reference

| #   | Category                                    | Key Qualifier                                                                      |
| --- | ------------------------------------------- | ---------------------------------------------------------------------------------- |
| 1   | SEC-Registered Issuers                      | Listed on national exchange or required to file under § 15(d)                      |
| 2   | Investment Companies                        | Registered under Investment Company Act of 1940                                    |
| 3   | Investment Advisers                         | SEC-registered under Investment Advisers Act                                       |
| 4   | Commodity Pool Operators                    | CFTC-registered                                                                    |
| 5   | Commodity Trading Advisers                  | CFTC-registered                                                                    |
| 6   | Banks                                       | Federally chartered or state-chartered; FDIC-insured                               |
| 7   | Credit Unions                               | Federal or state credit union                                                      |
| 8   | Bank Holding Companies                      | Registered under Bank Holding Company Act                                          |
| 9   | Savings and Loan Holding Companies          | As defined in Home Owners' Loan Act                                                |
| 10  | Registered Broker-Dealers                   | Registered under § 15 of Securities Exchange Act                                   |
| 11  | Money Services Businesses                   | FinCEN-registered MSB                                                              |
| 12  | Insurance Companies                         | State-domiciled; regulated by state commissioner                                   |
| 13  | State-Licensed Insurance Producers          | Authorized under state insurance law                                               |
| 14  | CEA-Regulated Entities                      | § 4(k) of the Commodity Exchange Act                                               |
| 15  | Accounting Firms                            | Regulated by state board of accountancy                                            |
| 16  | Public Utilities                            | Regulated public utility                                                           |
| 17  | Financial Market Utilities                  | Designated under Title VIII of Dodd-Frank                                          |
| 18  | Pooled Investment Vehicles                  | Operated/advised by an exempt entity                                               |
| 19  | Tax-Exempt Organizations                    | 501(c), § 527, 4947(a)(1) political organizations                                  |
| 20  | Entities Assisting Tax-Exempt Organizations | Controlled exclusively by 501(c) entity                                            |
| 21  | Large Operating Companies                   | >20 U.S. FT employees + U.S. office + >$5M prior-year revenue (all three required) |
| 22  | Subsidiaries                                | 100% owned and controlled by one or more exempt entities                           |
| 23  | Inactive Entities                           | Pre-2020 formation; dormant; no foreign ownership; no large transactions           |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                                                                | Fail Action                                                  |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Source**     | Every legal claim cites a specific statute, regulation, FinCEN guidance, or established principle                                                   | Add citation or mark `[UNVERIFIED — counsel to confirm]`     |
| **Format**     | All citations follow consistent format: statute (31 U.S.C. § 5336), regulation (31 C.F.R. § 1010.380), section reference (§ 5336(h)(3)(A))          | Fix format                                                   |
| **Currency**   | Every cited provision checked for amendments; confirm March 2025 interim rule status and any subsequent modifications                               | Flag `[CHECK CURRENCY — regulatory environment is evolving]` |
| **Domain**     | Analysis stays within U.S. federal CTA framework; do not assume state-level equivalents or conflate with FinCEN CDD Rule under 31 C.F.R. § 1010.230 | Remove or flag jurisdictional bleed                          |
| **Confidence** | Litigation-related uncertainty (CTA constitutionality, interim rule finalization) explicitly stated, not hidden                                     | Add confidence qualifier                                     |

### Self-Interrogation for CRITICAL Findings

For any item classified as CRITICAL (🚨), apply this three-pass review:

**Pass 1 — Regulatory Chain Integrity**:

- Does the CRITICAL classification follow logically from the specific statutory or
  regulatory text cited?
- Would FinCEN actually take enforcement action on this specific fact pattern?
- Has the interim final rule or any court order potentially modified this obligation?

**Pass 2 — Completeness**:

- Have all relevant exemptions been considered before classifying as a reporting company?
- Have all beneficial owner exemption categories been applied before classifying as a
  required beneficial owner?
- Is there a FinCEN FAQ or Small Entity Compliance Guide that addresses this specific issue?

**Pass 3 — Challenge**:

- What is the strongest argument that this CRITICAL finding is actually wrong?
- Could a good-faith compliance professional reasonably take a different position?
- If the interim final rule has been finalized or modified, how does that change the analysis?

Mark the Glass Box audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                                             | Action                                   |
| ------------ | --------- | ------------------------------------------------------------------- | ---------------------------------------- |
| **Definite** | 0.95–1.0  | Clear statutory text; FinCEN Small Entity Compliance Guide confirms | State with confidence                    |
| **High**     | 0.80–0.94 | Strong regulatory authority; consistent FinCEN FAQ guidance         | State with brief caveat                  |
| **Probable** | 0.60–0.79 | Good arguments but litigation risk or unsettled interim rule        | State with explicit reasoning and caveat |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing interpretations exist                | Flag for professional review             |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative; not supported by current FinCEN guidance   | Do not assert; mark `[UNCERTAIN]`        |

**Note**: Given the CTA's evolving regulatory and litigation status, most exemption
determinations that rely on the March 2025 interim rule should be scored **Probable**
(0.60–0.79) pending rule finalization.

---

## Glass Box Audit Trail

Include this YAML block in every BOI Filing Preparation Report:

```yaml
glass_box:
  skill_name: "legalcode-boi-filing-prep"
  entity_name: "[Legal name of reporting company]"
  entity_type: "[Corporation / LLC / LP / foreign entity type]"
  formation_jurisdiction: "[U.S. state or foreign country]"
  assessment_date: "[YYYY-MM-DD]"
  engagement_type: "[Initial filing / Update / Correction / Applicability assessment / Audit]"
  applicability_determination: "[REPORTING COMPANY / EXEMPT — INTERIM RULE / EXEMPT — [Category N] / UNCERTAIN]"
  exemption_applied: "[Category N — description, or 'N/A']"
  beneficial_owners_identified: "[count]"
  company_applicants_identified: "[count or 'N/A — pre-2024 entity']"
  fincen_id_strategy: "[Recommended / Not applicable / In use for [N] individuals]"
  filing_deadline: "[Date or 'See analysis']"
  deadline_status: "[MET / MISSED / UPCOMING — [N] days]"
  legalcode_mcp: "Connected / Not connected"
  statutes_consulted:
    - "31 U.S.C. § 5336 — [VERIFIED / UNVERIFIED]"
    - "31 C.F.R. § 1010.380 — [VERIFIED / UNVERIFIED]"
    - "March 26, 2025 Interim Final Rule — [VERIFIED / UNVERIFIED]"
  citations_verified: "[N VERIFIED] / [N UNVERIFIED]"
  self_interrogation: "[PASS / REVISED / NOT APPLICABLE]"
  confidence_overall: "[Level] — [Rationale, including note on CTA litigation uncertainty]"
  limitations:
    - "CTA constitutionality disputed in multiple federal circuits as of assessment date"
    - "March 2025 interim final rule not yet finalized; subject to modification"
    - "[Any entity-specific factual assumptions]"
    - "[Any areas requiring additional fact investigation]"
  reviewer: "AI-assisted — requires review by qualified legal counsel before filing"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do when preparing BOI reports:

1. **Reporting business entities as beneficial owners** — The CTA requires reporting of
   **natural persons only**. If a trust, LLC, or corporation owns 30% of the reporting
   company, trace through that entity to find the individuals who own or control it.
   Listing an entity as a beneficial owner causes BOIR rejection and requires correction.

2. **Stopping the ownership trace at the first entity layer** — The beneficial ownership
   analysis must follow the chain of ownership all the way to natural persons. A private
   equity fund owning 40% of the reporting company is not the answer; the individuals who
   control the fund's investment decisions may be.

3. **Aggregating employee headcounts to qualify for the large operating company exemption**
   — FinCEN's final rule expressly prohibits consolidating employee counts across affiliated
   entities for the 20-employee prong. Each entity must meet the threshold independently.
   This is the most frequently misapplied aspect of this exemption.

4. **Assuming that a 25% owner is the only type of beneficial owner** — The substantial
   control test is independent of the ownership threshold. A CEO with no equity stake is
   still a beneficial owner. A general counsel is still a beneficial owner. Omitting
   substantial control holders is a filing error with penalty exposure.

5. **Missing beneficial owners with indirect ownership** — Failing to calculate indirect
   ownership through intermediary entities. If an individual owns 80% of a holding company
   that owns 35% of the reporting company, that individual's indirect stake is 28% —
   above the 25% threshold.

6. **Relying on the large operating company exemption without verifying the physical office prong**
   — Virtual offices, registered agent addresses, and co-working memberships without
   dedicated tenancy do not satisfy the physical office requirement. Verify the entity's
   actual lease or ownership documentation before claiming this exemption.

7. **Failing to identify company applicants for post-2023 entities** — Entities formed
   or registered on or after January 1, 2024 must report company applicants. Omitting
   company applicants from a BOIR for a new entity is a filing deficiency.

8. **Using P.O. Box addresses for beneficial owner residential addresses** — FinCEN requires
   physical street addresses. P.O. Boxes will cause BOIR rejection. Many filers discover
   this only after submission fails.

9. **Submitting illegible or incomplete document images** — The identifying document image
   must clearly show the document number and be legible throughout. A blurry photograph
   or a document image that cuts off the number field will cause submission failure.

10. **Failing to monitor for update-triggering events** — The 30-day update obligation is
    triggered by many events companies do not associate with "ownership changes": address
    changes, name changes, document renewals, officer resignations, new hires into senior
    officer roles. Without a compliance calendar flagging these events, companies
    routinely miss update deadlines.

11. **Missing the 90-day correction safe harbor window** — When a filing error is discovered,
    companies often delay while investigating the correct information. The 90-day safe harbor
    is measured from the **original filing deadline**, not from when the error is discovered.
    Move quickly; penalties begin accruing when the window closes.

12. **Paying a third party to file a BOIR** — Filing through FinCEN's BOI E-Filing System
    is free. Any company charging a fee for filing assistance may be a scam. Legitimate
    service providers may charge for consulting and preparation — not for the act of
    submission.

13. **Treating the March 2025 interim rule exemption as permanent** — The exemption of
    domestic entities is an interim final rule, not final. It may be modified, withdrawn,
    or superseded by court order or legislative action. Companies relying on this exemption
    should maintain internal beneficial ownership records as if reporting were still required.

14. **Conflating the CTA with the FinCEN Customer Due Diligence (CDD) Rule** — The CTA
    (31 U.S.C. § 5336) imposes BOI reporting on reporting companies to FinCEN. The CDD
    Rule (31 C.F.R. § 1010.230) imposes beneficial ownership collection obligations on
    covered financial institutions from their customers. These are different rules with
    different thresholds, definitions, and obligations.

15. **Assuming a nominee arrangement protects beneficial owner privacy** — Nominees must
    not be reported as beneficial owners; the actual principal behind the nominee must be
    reported. Structuring ownership through nominees to obscure beneficial ownership from
    FinCEN is a CTA violation and may constitute money laundering.

16. **Failing to account for trusts in the ownership structure** — Trusts do not themselves
    appear as beneficial owners, but the trustee, grantor (if retaining control), or
    beneficiary (depending on trust structure) may qualify as a beneficial owner of the
    reporting company. Trust-heavy structures require careful analysis and typically
    specialist counsel [VERIFY].

17. **Assuming all 23 exemptions are available for the same entity** — Some exemptions are
    mutually exclusive; analyze each independently and document why the entity qualifies.
    Do not blend exemptions (e.g., claiming the subsidiary exemption and the large operating
    company exemption simultaneously unless both independently apply).

18. **Ignoring the senior officer catch-all** — "Any officer performing similar functions"
    to a President, CFO, CEO, COO, or General Counsel is a senior officer beneficial owner.
    A company with unusual title conventions (e.g., "Chief Revenue Officer," "Managing
    Partner") must assess functional equivalence, not just title.

---

## Writing Standards

Apply plain-language discipline to all BOI filing documents, instructions, and reports:

**For client-facing output** (Filing Preparation Reports, checklists, remediation roadmaps):

- Use plain English; define every legal term on first use
- Active voice: "You must file an updated BOIR within 30 days" not "An updated BOIR is
  required to be filed within 30 days of the triggering event"
- Name the actor and the deadline: "The reporting company must [action] by [specific date]"
- One obligation per sentence; do not compound multiple requirements
- Non-lawyer business stakeholders should understand the Executive Summary without
  reading the full report

**For legal analysis sections**:

- Every legal conclusion must cite a specific provision or FinCEN guidance document
- Clearly distinguish what is settled (clear statutory text), what is probable (consistent
  FinCEN FAQ guidance), and what is uncertain (evolving litigation/interim rule status)
- Never state an exemption conclusion without identifying the specific exemption number and
  the factual basis for it

**Quality gates before delivery**:

1. Does every beneficial owner finding identify which prong (ownership vs. control,
   and which category if control) supports the classification?
2. Does every exemption determination cite the specific exemption number and the three-prong
   or single-prong basis?
3. Has the March 2025 interim rule been applied to the applicability analysis?
4. Does the filing deadline section specify an exact date, not a relative reference?
5. Has the Glass Box audit trail been completed with all fields populated?

---

## External Tool Integration

**With legalcode-mcp connected (preferred)**:

- Search for current FinCEN BOI guidance, FinCEN FAQs, and Small Entity Compliance Guide
  updates
- Verify current status of pending litigation (Texas Top Cop Shop, Fifth Circuit, Supreme Court)
- Confirm status of the March 2025 interim final rule (finalized or still interim)
- Search for recent FinCEN enforcement actions and penalty guidance
- Save search results to `/tmp/boi-filing-research-[date].md`

**Without legalcode-mcp**:

- Use WebSearch to verify current FinCEN guidance at fincen.gov/boi
- Use WebSearch to verify current litigation status
- Mark all regulatory references `[VERIFY — check fincen.gov/boi for current guidance]`
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Advise client to independently verify exemption status and deadlines with current FinCEN
  published guidance before filing

**FinCEN's BOI E-Filing System**: boiefiling.fincen.gov
**FinCEN ID Portal**: fincenid.fincen.gov
**FinCEN BOI FAQ**: fincen.gov/boi-faqs
**FinCEN Small Entity Compliance Guide**: Available at fincen.gov/boi reference materials

---

## Output Format Template

```markdown
# BOI Filing Preparation Report

**Prepared for**: [Entity name and/or client name]
**Assessment date**: [YYYY-MM-DD]
**Engagement type**: [Initial filing / Update / Correction / Applicability assessment]
**Skill version**: legalcode-boi-filing-prep
**Prepared by**: [AI-assisted — requires legal review]

---

## Executive Summary

**Overall filing readiness**: [READY TO FILE / INCOMPLETE — [N] items outstanding / EXEMPT]

| Category                          | Status              | Notes                        |
| --------------------------------- | ------------------- | ---------------------------- |
| Applicability determination       | [✅ / ⚠️ / ❌ / 🚨] | [Exempt / Reporting company] |
| Company information               | [✅ / ⚠️ / ❌]      | [Items missing]              |
| Beneficial owner identification   | [✅ / ⚠️ / ❌ / 🚨] | [N] owners identified        |
| Beneficial owner information      | [✅ / ⚠️ / ❌ / 🚨] | [Items missing]              |
| Company applicant (if applicable) | [✅ / ⚠️ / N/A]     | [Items missing]              |
| Filing deadline                   | [✅ / ⚠️ / 🚨]      | [Date and status]            |

**Top priority actions**:

1. 🚨 [CRITICAL action] — Owner: [Role] — Deadline: [Date]
2. ❌ [MISSING element] — Owner: [Role] — Deadline: [Date]
3. ⚠️ [INCOMPLETE element] — Owner: [Role] — Deadline: [Date]

---

## Applicability Determination

**Entity**: [Name]
**Type**: [Entity type]
**Formation jurisdiction**: [State or country]
**Formation date**: [Date]

**Reporting company status**: [REPORTING COMPANY / EXEMPT]

[If EXEMPT]:
**Applicable exemption**: Exemption [N] — [Name]
**Basis**: [Specific facts satisfying the exemption]
**Confidence**: [Level]
**Caveat**: [Any uncertainty, particularly re: March 2025 interim rule status]

[If REPORTING COMPANY]:
**Exemptions evaluated and rejected**:
| Exemption | Category | Reason Not Applicable |
|-----------|----------|----------------------|
| [N] | [Name] | [Specific factual basis for rejection] |

---

## Beneficial Owner Register

| #   | Name        | Prong                 | Category             | Classification         | Status         |
| --- | ----------- | --------------------- | -------------------- | ---------------------- | -------------- |
| 1   | [Full name] | [Ownership / Control] | [25% / Category 1-4] | BENEFICIAL OWNER       | [✅ / ⚠️ / ❌] |
| 2   | [Full name] | [Ownership + Control] | [25% + Category 1]   | BENEFICIAL OWNER       | [✅ / ⚠️ / ❌] |
| N   | [Full name] | N/A                   | N/A                  | NOT A BENEFICIAL OWNER | ✅             |

### Ownership Calculation Summary

| Individual | Direct % | Indirect % | Total % | Threshold Met? |
| ---------- | -------- | ---------- | ------- | -------------- |
| [Name]     | [%]      | [%]        | [%]     | [YES / NO]     |

### Substantial Control Analysis

| Individual | Category 1 | Category 2 | Category 3 | Category 4 | Conclusion    |
| ---------- | ---------- | ---------- | ---------- | ---------- | ------------- |
| [Name]     | [YES/NO]   | [YES/NO]   | [YES/NO]   | [YES/NO]   | [BO / Not BO] |

---

## Required Information Checklist

### Reporting Company Information

| Field                           | Status          | Current Value | Missing/Needed   |
| ------------------------------- | --------------- | ------------- | ---------------- |
| Legal name                      | [✅ / ❌]       | [Value]       | [What is needed] |
| Trade names / DBAs              | [✅ / ⚠️ / ❌]  | [Value]       |                  |
| EIN / TIN                       | [✅ / ❌]       | [Value]       |                  |
| Principal business address      | [✅ / ❌]       | [Value]       |                  |
| Jurisdiction of formation       | [✅ / ❌]       | [Value]       |                  |
| U.S. registration jurisdictions | [✅ / N/A / ❌] | [Value]       |                  |

### Beneficial Owner [N] — [Name]

| Field                     | Status         | Notes                                   |
| ------------------------- | -------------- | --------------------------------------- |
| Full legal name           | [✅ / ❌]      |                                         |
| Date of birth             | [✅ / ❌]      |                                         |
| Residential address       | [✅ / ⚠️ / ❌] | [P.O. Box? Physical address confirmed?] |
| Identifying document type | [✅ / ❌]      | [Passport / DL / ID]                    |
| Document number           | [✅ / ❌]      |                                         |
| Issuing jurisdiction      | [✅ / ❌]      |                                         |
| Document image            | [✅ / ⚠️ / ❌] | [Legible? Complete?]                    |
| FinCEN ID (if using)      | [✅ / N/A]     |                                         |

[Repeat for each beneficial owner]

---

## Filing Deadline Summary

| Event                           | Deadline                   | Status                                |
| ------------------------------- | -------------------------- | ------------------------------------- |
| Initial BOIR                    | [Specific date]            | [MET / UPCOMING — N days / 🚨 MISSED] |
| Correction safe harbor expiry   | [Date if applicable]       | [Status]                              |
| Next anticipated update trigger | [Event and estimated date] | [Monitoring recommended]              |

**Update monitoring obligations**: The following events will trigger a 30-day update
obligation if they occur:

- [List of monitored events specific to this entity's structure]

---

## Remediation Roadmap

### IMMEDIATE (File or correct within 30 days)

- [ ] [Action] — Owner: [Role] — Deadline: [Specific date]
- [ ] [Action] — Owner: [Role] — Deadline: [Specific date]

### NEAR-TERM (30–90 days)

- [ ] [Action] — Owner: [Role] — Deadline: [Date or rolling]

### ONGOING MONITORING

- [ ] Establish calendar alerts for beneficial owner change triggers
- [ ] Review BOI records annually for accuracy
- [ ] Monitor FinCEN rulemaking for interim rule finalization [VERIFY]
- [ ] Monitor litigation developments for any court-ordered resumption of broader obligations

---

## Glass Box Audit Trail

[YAML block — see Glass Box Audit Trail section above]
```

---

## Localization Notes

The CTA is a U.S. federal statute with no direct equivalent in other jurisdictions. However,
related beneficial ownership transparency frameworks exist in other jurisdictions that may
affect entities operating cross-border:

| Jurisdiction       | Framework                                                                                           | Key Parallels                                                                          |
| ------------------ | --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **European Union** | EU Anti-Money Laundering Directives (AMLD4/5/6); beneficial ownership registries required per AMLD5 | Similar 25% threshold; register typically public or semi-public                        |
| **United Kingdom** | PSC (Persons with Significant Control) Register; Companies Act 2006, Part 21A                       | Similar 25% ownership threshold; filed with Companies House                            |
| **Canada**         | CBCA transparency register for federal corporations; provincial variants                            | Similar beneficial ownership disclosure framework [VERIFY current provincial coverage] |
| **Australia**      | AML/CTF Act beneficial ownership requirements                                                       | Applies to reporting entities; different threshold structure                           |

**For foreign entities subject to CTA**: Verify whether the entity's home country also
requires beneficial ownership disclosure; dual-reporting obligations may apply.

**For U.S. entities with international operations**: CTA obligations (if restored for
domestic entities) apply regardless of where the entity's beneficial owners are located.
Foreign persons who are beneficial owners of U.S. reporting companies must still be reported;
however, under the March 2025 interim final rule, U.S. persons need not be reported as
beneficial owners of any entity.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis combining deep research on the
Corporate Transparency Act (31 U.S.C. § 5336), FinCEN's implementing regulations
(31 C.F.R. § 1010.380), the March 26, 2025 interim final rule narrowing CTA scope to
foreign entities, ongoing litigation developments through December 2025, FinCEN Small
Entity Compliance Guide guidance, and structural patterns drawn from the legalcode
gold-standard skill methodology. Incorporates all 18 required Legalcode quality elements
adapted for a compliance/regulatory submission context.
