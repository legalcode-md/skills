---
name: legalcode-ie-company-formation
description: Guides Irish company formation under the Companies Act 2014 — entity type selection (LTD,
  DAC, PLC, CLG, UC), CRO registration and Form A1 preparation, constitution drafting, director and company
  secretary requirements (including EEA residency and Section 137 bond), annual return obligations, audit
  exemption qualification, and Section 110 SPV structures under the Taxes Consolidation Act 1997. Use
  when forming a new Irish company, advising on entity type choice, setting up a Section 110 SPV, checking
  post-incorporation compliance obligations, reviewing CRO filing requirements, or auditing annual return
  status and audit exemption eligibility. Covers all Companies Registration Office procedures, Revenue
  tax registration, and ongoing statutory compliance for Irish companies.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Irish Company Formation

> **Disclaimer**: This skill provides a framework for AI-assisted guidance on Irish
> company formation and corporate compliance. It does not constitute legal or tax advice.
> All outputs should be reviewed by a qualified solicitor and, where tax matters are
> involved, a qualified tax adviser, both licensed to practise in Ireland before use.
> Company law and Revenue practice change; verify current requirements with the
> Companies Registration Office (cro.ie), Revenue Commissioners (revenue.ie), and the
> Law Society of Ireland (lawsociety.ie) before relying on any provision described here.
> Statutory and regulatory references cited carry hallucination risk — verify against
> authoritative sources.

## Purpose and Scope

This skill guides formation of Irish-registered companies under the **Companies Act 2014**
and associated legislation. It supports entity type selection, CRO registration, constitution
drafting, director and secretary appointment, post-incorporation compliance, and specialist
structures such as Section 110 SPVs.

**Covers:**

- Entity type selection: LTD, DAC, PLC, CLG, UC
- CRO registration workflow: Form A1, name reservation, CORE platform
- Constitution drafting: mandatory vs. optional provisions, statutory defaults
- Director requirements: minimum numbers, EEA residency, Section 137 bond
- Company secretary requirements and obligations
- Annual return (Form B1) filing, deadlines, and penalties
- Audit exemption eligibility criteria and loss conditions
- Section 110 SPV formation and qualifying conditions
- Share capital structuring and registered office requirements
- Post-incorporation compliance: statutory registers, company seal, AGM
- Revenue tax registration: corporation tax, VAT, PAYE
- Business name registration under the Registration of Business Names Act 1963
- Ongoing corporate maintenance and officer change notifications

**Does not:**

- Provide legal advice or replace qualified Irish solicitors
- Cover financial services regulatory authorisation (CBI authorisation is a separate process)
- Cover partnership formation, sole trader registration, or co-operative structures
- Address employment law or GDPR compliance in depth (separate skills cover these)
- Constitute tax advice — engage a Chartered Tax Adviser for Revenue-specific guidance

## Jurisdiction and Governing Law

This skill is **specific to Ireland** (Republic of Ireland). The primary legislative
framework is:

- **Companies Act 2014** (as amended) — consolidates 17 prior Companies Acts into
  1,448 sections and 17 Schedules; in force from 1 June 2015
- **Registration of Business Names Act 1963** — business name registration
- **Taxes Consolidation Act 1997 (TCA 1997)** — Section 110 SPV tax regime
- **Companies (Accounting) Act 2017** — financial reporting
- **European Communities (Single-Member Private Limited Companies) Regulations 1994**

Key regulatory bodies:

- **CRO (Companies Registration Office)** — company registration and filings (cro.ie)
- **Revenue Commissioners** — tax registration and compliance (revenue.ie)
- **Corporate Enforcement Authority (CEA)** — company law enforcement
- **Central Bank of Ireland (CBI)** — financial services regulation (separate from
  standard company formation)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming the user's intent, the workflow pauses and asks when:

- The entity type choice is unclear or multiple types could be appropriate
- The director/shareholder structure creates EEA residency compliance issues
- The intended business activities trigger regulated sector restrictions
- The constitution requires bespoke provisions beyond statutory defaults
- Section 110 SPV structuring decisions require tax and legal specialist input

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

### Step 1: Accept the Instruction

Accept instructions in any of these formats:

- **Formation request**: "Form a new Irish company for [business purpose] with
  [shareholders/directors]"
- **Review request**: "Review our CRO filing / annual return / audit exemption status"
- **Section 110 query**: "Set up a Section 110 SPV for [asset type]"
- **Compliance audit**: "What are our ongoing obligations after incorporation?"

If no specific details are provided, gather context via Step 2.

### Step 2: Gather Context

**⟁ CLARIFY** — Ask the following questions before proceeding (skip any already answered):

1. **Business purpose and activities**
   - What will the company do? (commercial trading, holding company, SPV, charity, etc.)
   - Are any activities regulated by the Central Bank of Ireland, Competition and
     Consumer Protection Commission, or other regulators?
   - _Why this matters_: Business purpose determines entity type and whether regulatory
     authorisation is required before incorporation can be completed.

2. **Shareholder and ownership structure**
   - Who are the shareholders and what percentages do they hold?
   - Are any shareholders non-EEA residents?
   - Is there a single member or multiple members?
   - _Why this matters_: EEA residency affects director requirements; single-member
     companies have specific constitution requirements.

3. **Director composition**
   - Who are the proposed directors? Are any EEA residents?
   - If no EEA-resident director is available, is the company prepared to obtain a
     Section 137 bond?
   - _Why this matters_: At least one director must be EEA-resident, or a €25,000
     Section 137 bond must be held. Non-compliance is a criminal offence.

4. **Entity type preference**
   - Options: **LTD** (default for most commercial uses), **DAC** (where objects clause
     is desired), **PLC** (public/listed), **CLG** (non-profit/guarantee), **UC**
     (privacy of financial statements), or **unsure — advise me**
   - _Why this matters_: Entity type determines constitutional structure, minimum
     director numbers, AGM obligations, share capital requirements, and public filing duties.

5. **Timeline and urgency**
   - Standard CRO processing: 5 working days; expedited (Fé Phráinn): same/next day
   - Is there a business or contract deadline driving urgency?
   - _Why this matters_: Determines whether to use standard or expedited registration.

If the user provides partial context, proceed with stated defaults and **explicitly
state assumptions** made (e.g., "Assuming no EEA-resident director is available —
I will flag the Section 137 bond requirement"). Do not assume silently.

### Step 3: Entity Type Assessment

Assess the appropriate entity type using the **Entity Type Selection Framework** below.
Present the recommendation with reasoning.

**⟁ CLARIFY** — If the assessment reveals that the intended activities suggest a
regulated sector (financial services, insurance, investment funds, credit institutions),
flag this to the user:

> "The activities you describe may require Central Bank of Ireland authorisation in
> addition to CRO registration. CBI authorisation timelines (6–24 months depending
> on licence type) may need to be factored into your planning. Would you like me to
> flag the relevant CBI regime, or proceed with the CRO formation steps on the
> assumption that CBI authorisation is being handled separately?"

### Step 4: Gather Legal Authority

Use **legalcode-mcp** (if connected) to search for current requirements:

- Any Companies Act 2014 amendments enacted since the skill's knowledge date
- Current CRO filing fees (verify against cro.ie/publications/fees)
- Recent Revenue guidance on corporation tax registration
- CEA enforcement guidance on director disqualification

**If legalcode-mcp is not connected:**

- Proceed with the statutory framework below
- Mark any fee amounts and procedural details with [VERIFY] against current CRO/Revenue
  guidance
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`

### Step 5: Constitution Analysis

Draft or review the company constitution against the requirements in the
**Constitution Requirements** section below.

**⟁ CLARIFY** — For LTD companies, ask:

> "Do you want to rely entirely on the Companies Act 2014 statutory defaults, or
> do you need bespoke provisions for any of the following: (a) share class rights,
> (b) director appointment/removal mechanisms, (c) dividend policy, (d) restrictions
> on share transfers, (e) quorum requirements, (f) AGM dispensation?"

This determines whether a custom constitution or a minimal-form constitution is
appropriate.

### Step 6: Assess Director and Officer Compliance

Apply the **Director and Company Secretary Requirements** framework. Flag any
non-compliance risks (especially EEA residency and Section 137 bond).

**⟁ CLARIFY** — If no EEA-resident director has been identified:

> "No EEA-resident director has been identified. There are two options:
> (A) Appoint an EEA-resident director (natural person, resident in the EEA for more
> than 6 months of the year); or
> (B) Obtain a Section 137 bond covering €25,000 in potential fines — valid for
> 2 years, must be renewed or replaced with an EEA director before expiry.
> Non-compliance is a criminal offence. Which path would you like to take?"

### Step 7: Annual Return and Audit Exemption Analysis

Apply the **Annual Return and Audit Exemption** framework to:

- Identify the company's first Annual Return Date (ARD)
- Calculate the 56-day filing window for current and future returns
- Assess audit exemption eligibility and flag any Schedule 5 exclusions
- Check whether any prior late filings have triggered a 2-year exemption loss

### Step 8: Section 110 SPV Analysis (if applicable)

If the formation involves a Section 110 structure, apply the **Section 110 SPV
Framework** below. Flag any structuring risks and recommended specialist review.

### Step 9: Post-Incorporation Compliance Roadmap

Generate a **Post-Incorporation Compliance Roadmap** covering:

- First 30 days: Revenue tax registration, registered office confirmation
- First 6 months: First annual return (no financial statements required)
- Within 18 months: First AGM (unless dispensed with by member resolution)
- Ongoing: Annual return filing, statutory register maintenance, officer change notifications

### Step 10: Quality Verification

Before delivering analysis:

1. Run the 5 Citation Quality Gates silently. Revise any failures.
2. For every HIGH-severity compliance issue, run Self-Interrogation (3-pass review).
3. Apply Confidence Scoring to all statutory references.
4. Generate the Glass Box Audit Trail.

---

## Entity Type Selection Framework

### Overview of Irish Company Types

| Type    | Full Name                         | Min. Directors | Objects Clause? | AGM Required?           | Min. Share Capital    | Best For                                                              |
| ------- | --------------------------------- | -------------- | --------------- | ----------------------- | --------------------- | --------------------------------------------------------------------- |
| **LTD** | Private Company Limited by Shares | 1              | No              | Optional (can dispense) | None                  | Most commercial uses — default choice                                 |
| **DAC** | Designated Activity Company       | 2              | Yes (mandatory) | Yes (if 2+ members)     | None                  | SPVs with defined activities; subsidiaries requiring restricted scope |
| **PLC** | Public Limited Company            | 2              | No              | Yes                     | €25,000 (25% paid up) | Listed companies; public fundraising                                  |
| **CLG** | Company Limited by Guarantee      | 2              | Optional        | Yes                     | None (no shares)      | Charities, non-profits, sports clubs, professional bodies             |
| **UC**  | Unlimited Company                 | 2              | Optional        | Yes                     | None                  | Privacy of financial statements; holding structures                   |

### LTD — Private Company Limited by Shares

**Characteristics:**

- Most common company type in Ireland (>90% of registered companies)
- No stated objects or restrictions on business activities — can do anything lawful
- Single-document constitution (no separate memorandum and articles)
- Can have a single director (if accompanied by a separate company secretary)
- Can dispense with AGM if all members sign a written resolution in lieu
- No minimum share capital requirement
- 151 optional statutory defaults in the Act that can be varied by constitution
- Statutory defaults fill gaps where constitution is silent

**Automatic RED flags:**

- If intended activities require a DAC objects clause → entity mismatch
- If listing on a stock exchange is planned → PLC required
- If no share capital and no profit distribution → CLG may be more appropriate
- If privacy of financial statements is paramount → UC may be preferable

**Recommended for:**

- Trading companies, consultancies, holding companies, startups, subsidiaries
- Any commercial purpose not requiring a defined objects clause

### DAC — Designated Activity Company

**Characteristics:**

- Unique feature: constitution must include a Memorandum of Association with Objects Clause
- Company is restricted to activities specified in the memorandum
- Minimum 2 directors required (cannot be single-director)
- Must hold AGM if 2 or more members
- Ultra vires risk: acts outside objects clause may be void [VERIFY post-CA2014 third-party protections]

**Recommended for:**

- Section 110 SPVs (where tax neutrality depends on defined qualifying activities)
- Structured finance vehicles
- Subsidiaries where parent company requires restricted scope
- Companies requiring constitutional activity limits for investor comfort

### PLC — Public Limited Company

**Characteristics:**

- Minimum issued share capital of €25,000 (at least 25% fully paid before commencing business)
- Can offer shares to the public; no statutory limit on number of shareholders
- Stricter corporate governance and disclosure requirements
- Prospectus requirements if listing securities (Prospectus Regulation (EU) 2017/1129)
- Minimum 2 directors

**Recommended for:**

- Companies intending to list on Euronext Dublin or another exchange
- Companies seeking public fundraising via share issuance

### CLG — Company Limited by Guarantee

**Characteristics:**

- No share capital; members are guarantors rather than shareholders
- Guarantee amount typically €1-€10 nominal
- Members' liability limited to guarantee amount
- Cannot distribute profits to members in most configurations
- Minimum 2 directors

**Recommended for:**

- Charities, NGOs, voluntary organisations, sports bodies
- Professional associations and trade bodies
- Social enterprises

### UC — Unlimited Company

**Characteristics:**

- Shareholders have unlimited personal liability for company debts
- Certain UC structures (EPLC, EPUC) can be exempt from filing financial statements
- Financial privacy benefit: no public accounts at CRO
- Minimum 2 directors

**Recommended for:**

- Holding structures where financial privacy is a priority
- Structures where unlimited liability is commercially acceptable (e.g., inter-group)

---

## CRO Registration Workflow

### Step-by-Step Registration Process

**Phase 1 — Pre-Registration Preparation**

1. **Search and reserve company name** (cro.ie/registration/company/name-search)
   - Name must end with "Limited", "Ltd", "Teoranta", or "Teo" (for LTD companies)
   - Name must not be identical or misleadingly similar to an existing registered name
   - Name reservation costs €25 (valid 28 days) — optional but recommended
   - Certain words require ministerial approval ("Bank", "Insurance", "College", etc.)

2. **Prepare Form A1** — the incorporation form. Required contents:
   - Company name and type
   - Registered office address in Ireland (cannot be a PO Box)
   - Details of every director: full name, date of birth, PPS number (or equivalent),
     occupation, address, date of appointment
   - Details of company secretary: name, occupation, address, date of appointment
   - Subscriber details: names, addresses, and share allocations
   - Declaration of compliance with the Companies Act 2014
   - Signed consents from all directors and the company secretary
   - Statement of the company's intended principal business activities

3. **Prepare constitution**
   - For LTD: single-document constitution
   - For other types: Memorandum of Association + Articles of Association
   - Must be signed by at least one subscriber before registration

**Phase 2 — Submission via CORE Platform**

- Submit via **CORE** (cro.ie/core) — the CRO's online filing system
- Preferred submission method: online (faster processing, lower risk of rejection)
- Paper filing also available but slower

**Phase 3 — CRO Processing and Certificate of Incorporation**

| Method                     | Timeline              | Notes                              |
| -------------------------- | --------------------- | ---------------------------------- |
| **Standard Online A1**     | 5 working days        | Standard online submission         |
| **Fé Phráinn (Expedited)** | Same/next working day | Higher fees; urgent incorporations |
| **Ordinary Online**        | 10 working days       | Lower-priority queue               |
| **Paper submission**       | Variable              | Not recommended; slower            |

- On successful registration, CRO issues a **Certificate of Incorporation** with a unique
  company registration number
- Certificate is conclusive evidence of due incorporation (CA 2014, s.25)

**CRO Filing Fees (current as at knowledge date — [VERIFY] against cro.ie/publications/fees):**

| Item                                    | Fee |
| --------------------------------------- | --- |
| Standard Form A1                        | €50 |
| Company name reservation                | €25 |
| Business name registration (electronic) | €20 |
| Business name registration (paper)      | €40 |
| Annual return (B1) — electronic         | €20 |
| Annual return (B1) — paper              | €40 |

**Common Form A1 Rejection Causes:**

- Unsigned or undated director consent declarations
- Company name format error (missing "Limited"/"Ltd" suffix)
- Missing company secretary consent for single-director LTD
- Incorrect or incomplete PPS numbers / equivalent identification
- Registered office address outside the Republic of Ireland
- Constitution not signed by subscriber(s)

---

## Constitution Requirements

### LTD Company — Single Document Constitution

The LTD constitution is a single document. Under CA 2014, the Act's statutory defaults
apply to fill gaps — no need to replicate default provisions in the constitution.

**Mandatory constitutional provisions:**

- Company name (including "Limited" or "Ltd" suffix)
- Statement that the company is a private company limited by shares
- Registered office location (county or county borough sufficient; full address filed via A1)
- Any variation of statutory defaults the founders wish to make

**Key statutory defaults for LTD (151 optional provisions):**
Statutory defaults apply unless the constitution expressly varies them. Notable defaults:

| Default provision        | Default rule                                              | Common variation                    |
| ------------------------ | --------------------------------------------------------- | ----------------------------------- |
| AGM                      | Required unless all members consent to written resolution | Disapply AGM requirement            |
| Director appointment     | Majority board approval                                   | Specify shareholder vote required   |
| Director removal         | Ordinary resolution                                       | Require special resolution          |
| Share transfer           | Board approval required                                   | Specify pre-emption procedures      |
| Quorum                   | 2 members (or 1 if single-member)                         | Vary quorum requirements            |
| Dividends                | Declared by ordinary resolution                           | Restrict to director recommendation |
| Authorised share capital | Unlimited                                                 | Set cap if desired                  |
| Written resolutions      | Unanimous for all resolutions                             | N/A (set by statute)                |

**Common bespoke provisions:**

- Share classes with different rights (voting, dividend, capital)
- Pre-emption rights on share transfers (if departing from default)
- Director appointment rights reserved for specific shareholders (founder protection)
- Drag-along / tag-along rights (common in venture-backed companies)
- Reserved matters requiring supermajority or specific director consent

### DAC — Memorandum and Articles of Association

**Memorandum of Association must contain:**

- Company name
- Statement that it is a designated activity company
- Objects clause (restricted to specified activities) — **mandatory and material**
- Statement of limited liability
- Statement of share capital (if applicable)
- Association clause signed by subscribers

**Objects clause drafting guidance:**

- Define all intended activities; include ancillary powers
- Include a general catch-all for activities "incidental or conducive to the main objects"
- For Section 110 SPVs: objects must be limited to holding and managing qualifying assets
  under s.110 TCA 1997 — [VERIFY current Revenue guidance on permissible s.110 objects]

---

## Director and Company Secretary Requirements

### Director Requirements

**Minimum numbers:**
| Company Type | Minimum Directors |
|-------------|------------------|
| LTD | 1 (natural person only) |
| DAC, PLC, CLG, UC | 2 |

**Eligibility requirements:**

- Natural person (bodies corporate cannot be directors)
- Age: minimum 18 years
- Not an undischarged bankrupt
- Not subject to a disqualification order or undertaking under CA 2014 Parts 14-16
- For PLCs and listed companies: additional fit and proper requirements

**EEA Residency Requirement — Section 137 CA 2014 (CRITICAL)**

> **Every Irish company must have at least one director who is ordinarily resident in an
> EEA state.** This is a residency requirement, not a citizenship requirement: an EU
> national living outside the EEA does not satisfy it; a non-EU national with EEA residency
> does.

EEA states: All 27 EU member states + Iceland, Norway, and Liechtenstein.

**Alternative — Section 137 Bond:**
If no EEA-resident director is or can be appointed, the company may hold a bond:

- Bond amount: **€25,000** (covers potential fines under company law offences)
- Duration: **2 years** from issue date
- Must be renewed before expiry, or an EEA-resident director must be appointed
- Non-compliance with s.137 (neither EEA director nor bond) is a **criminal offence**
- Bond providers: typically specialist insurance companies or banks

**Classification of EEA Director requirement:**

| Situation                                     | Classification           | Required action                                |
| --------------------------------------------- | ------------------------ | ---------------------------------------------- |
| EEA-resident director confirmed               | COMPLIANT                | Document residency confirmation                |
| No EEA director; valid bond held              | COMPLIANT (temporary)    | Track bond expiry; calendar renewal            |
| No EEA director; bond expiring within 60 days | WARNING                  | Renew bond or appoint EEA director immediately |
| No EEA director; no bond                      | NON-COMPLIANT / CRITICAL | Criminal offence; rectify before submission    |
| Bond lapsed without renewal                   | NON-COMPLIANT / CRITICAL | Criminal offence; obtain new bond urgently     |

**Disqualification grounds (CA 2014, ss.839-840):**

- Undischarged bankruptcy
- Conviction on indictment for offences under the Companies Acts or related enactments
- Court disqualification order (typically 5-year minimum; can be up to life)
- Disqualification undertaking accepted by the CEA
- Involuntary strike-off and CEA proceedings under s.842(h)

**Annual disclosure obligations:**

- Directors must declare interests in contracts with the company (s.231 CA 2014)
- Directors must maintain register of their interests in company shares (s.267 CA 2014)
- Directors must notify the company of any disqualification or restriction order

### Company Secretary Requirements

**Legal requirement:**
Every Irish company must have a company secretary. The role cannot be vacant.

- **LTD with single director**: The sole director cannot also be the company secretary —
  a **separate** secretary must be appointed
- **All other companies**: A director may also be company secretary
- **Corporate secretary**: A body corporate may act as company secretary

**Qualification requirements:**

- **Private companies**: No formal qualification required; directors must be satisfied
  the secretary has the skill and knowledge necessary to discharge statutory duties
- **PLCs**: Secretary must have requisite knowledge and experience of company secretarial
  functions — [VERIFY: requirement typically met by ICSA/Chartered Governance Institute qualification]

**Key secretary obligations:**

1. Ensure the company complies with the Companies Act 2014 requirements
2. Act as primary liaison with the CRO
3. Maintain all 7 statutory registers (see Post-Incorporation section)
4. Organise and record board meetings and general meetings
5. Prepare minutes of all meetings
6. File annual returns (Form B1) before deadlines
7. Ensure compliance with all CRO filing obligations
8. Notify CRO of changes to directors, secretary, and registered office

**Personal liability exposure:**

- Fines up to €5,000 for breaches of CA 2014 filing obligations
- Prosecution for persistent non-compliance

---

## Annual Return (Form B1) Requirements

### Filing Deadlines — Critical Compliance

Annual returns are **the most common area of Irish company law non-compliance** and
trigger automatic penalties and loss of audit exemption.

**First Annual Return:**

- Due exactly **6 months** after the date of incorporation
- **No financial statements** are required with the first annual return
- Filing the first return on time is important to preserve the audit exemption going forward

**Subsequent Annual Returns:**

- Every company has an Annual Return Date (ARD) — typically the anniversary of the first ARD
- The return must be filed within **56 days** of the ARD
- Where financial statements are required: the earlier of (a) ARD + 56 days, or
  (b) financial year-end + 9 months + 56 days
- A return cannot be filed more than **7 days before** the ARD

**Summary deadline table:**

| Return              | Deadline                    | Financial statements required? |
| ------------------- | --------------------------- | ------------------------------ |
| First annual return | 6 months from incorporation | No                             |
| Subsequent returns  | ARD + 56 days               | Yes (if not audit exempt)      |
| If audit exempt     | ARD + 56 days               | Abridged balance sheet only    |

### Late Filing Consequences

| Consequence                 | Trigger                                                  | Amount/Duration                                      |
| --------------------------- | -------------------------------------------------------- | ---------------------------------------------------- |
| Late filing fee             | Day after 56-day deadline                                | **€100**                                             |
| Daily default fee           | Each subsequent day                                      | **€3/day** (maximum €1,200)                          |
| **Loss of audit exemption** | Late filing in any year                                  | **2 full financial years** following the late filing |
| **Repeat late filing**      | Late filing AND prior late filing in any of past 5 years | Loss of audit exemption for 2 years following        |
| Prosecution risk            | Persistent non-compliance                                | Directors and company officers personally            |
| Involuntary strike-off      | Extended non-compliance                                  | Company removed from register                        |
| Director exposure           | Involuntary strike-off                                   | CEA may seek restriction/disqualification orders     |

> **Practice warning**: The loss of audit exemption is frequently underestimated. A
> single late filing (even by one day) costs the exemption for two years. For small
> companies, the audit cost (typically €2,000–€8,000+) far exceeds the €100 late fee.
> Calendar annual return deadlines as high-priority compliance events.

### Annual Return Contents (Form B1)

- Company name, registered number, registered office
- Directors and secretaries: current details, any changes since last return
- Share capital and shareholders (principal holders)
- Beneficial owners information (where applicable)
- Declaration claiming audit exemption (if applicable)
- Financial statements (if required):
  - **Audit-exempt companies**: Abridged balance sheet + directors' declaration
  - **Non-exempt companies**: Full audited financial statements

---

## Audit Exemption Framework

### Qualifying Criteria for Audit Exemption (CA 2014, s.360)

A private company (LTD) can claim audit exemption if it satisfies **at least 2 of these
3 size criteria** for the current and prior financial year:

| Criterion           | Threshold     |
| ------------------- | ------------- |
| Annual turnover     | ≤ €12 million |
| Balance sheet total | ≤ €6 million  |
| Average employees   | ≤ 50          |

### Mandatory Exclusions — Schedule 5 Companies

Even if a company meets the size criteria, it **cannot** claim audit exemption if it
carries on any activity listed in Schedule 5 to CA 2014. Key excluded categories:

| Category              | Description                                  |
| --------------------- | -------------------------------------------- |
| Financial services    | Banks, credit institutions, mortgage lenders |
| Insurance             | Insurance and reinsurance undertakings       |
| Investment            | Investment firms, UCITS, AIFs                |
| Credit                | Credit unions, moneylenders                  |
| Leasing/hire purchase | Finance leasing companies                    |
| Trade unions          | Trade union bodies                           |
| Holding companies     | Holding companies of Schedule 5 subsidiaries |

> [VERIFY] Current Schedule 5 list — additions may have been made by statutory instrument.

### Classification for Audit Exemption Assessment

| Status                                 | Classification                         | Action                                    |
| -------------------------------------- | -------------------------------------- | ----------------------------------------- |
| Meets 2+ criteria; not Schedule 5      | ELIGIBLE                               | Ensure annual returns filed on time       |
| Meets 2+ criteria; Schedule 5 activity | EXCLUDED                               | Full audit required; budget accordingly   |
| Fails 2+ criteria                      | INELIGIBLE                             | Full audit required                       |
| Previously filed late                  | INELIGIBLE (2 years)                   | Full audit required for 2 financial years |
| Subsidiary of large group              | [VERIFY] group consolidation exemption | Assess under group audit exemption rules  |

### Directors' Obligations When Claiming Exemption

- Balance sheet must contain a **directors' declaration** claiming the exemption
- Company must not have received written notice from members holding ≥10% shares
  requiring a full audit [VERIFY s.334 CA 2014]
- Annual return must be filed on time (exemption lost for 2 years if late)

---

## Section 110 SPV Framework

### Overview and Purpose

Section 110 of the Taxes Consolidation Act 1997 (TCA 1997) provides a **tax-neutral
regime** for Irish-resident special purpose vehicles engaged in securitisation and
structured finance transactions.

Section 110 SPVs are a significant component of Ireland's international financial services
sector. By 2017, Ireland hosted the largest structured finance vehicle pool in the EU.

### Tax Treatment of Section 110 Companies

| Tax                               | Treatment                                                |
| --------------------------------- | -------------------------------------------------------- |
| Corporation tax on trading income | Effectively zero — "profit participating note" deduction |
| Capital gains tax                 | Typically zero on qualifying assets                      |
| Withholding tax on interest       | Subject to conditions, typically exempt or reduced       |
| VAT                               | No VAT applies to most s.110 transactions                |
| Stamp duty                        | No stamp duty on qualifying asset acquisitions           |

The mechanism: the SPV issues **profit participating notes (PPNs)** to investors.
Interest payments on PPNs are deductible, reducing taxable income to near zero. The
noteholders (not the SPV) bear economic exposure.

### Qualifying Requirements for Section 110 Status

A company is a "qualifying company" under s.110 TCA 1997 if it meets **all** of the
following:

| Requirement                   | Details                                                                                    |
| ----------------------------- | ------------------------------------------------------------------------------------------ |
| **Irish tax residence**       | Must be Irish tax resident (typically: incorporated and managed and controlled in Ireland) |
| **Qualifying assets**         | Must hold and/or manage "qualifying assets" as its business                                |
| **Minimum transaction value** | First transaction must have a value of at least **€10 million**                            |
| **Notification to Revenue**   | Must notify Revenue of its election to be treated as a s.110 company                       |
| **Ancillary activities only** | Can only undertake activities incidental to holding/managing qualifying assets             |
| **Filing obligations**        | Must file accounts and tax returns with Revenue                                            |

### Qualifying Assets (s.110(1) TCA 1997)

The definition of qualifying assets is broad and includes:

- Financial assets: loans, mortgages, bonds, debentures, shares, leases
- Commodities (certain types)
- Plant and machinery (in certain structures)
- Insurance policies and insurance contracts
- Derivatives (swaps, options, forwards)
- Intellectual property rights (in certain structures)
- Carbon credits (since Finance Act 2012)

> [VERIFY] Most recent Finance Act amendments to the qualifying assets definition.

### Entity Type for Section 110 SPVs

Section 110 companies are almost always structured as:

- **DAC** (most common): allows restricted objects clause limiting activities to
  qualifying asset management — this provides structural comfort to investors and
  clearly delineates the SPV's authority
- Occasionally LTD: used where maximum constitutional flexibility is preferred, with
  contractual restrictions instead

### Section 110 Constitution — Objects Clause

For a DAC used as a Section 110 vehicle, the objects clause should:

- Define the permitted qualifying asset types with precision
- Include power to issue notes, bonds, and other securities
- Include power to enter hedging arrangements
- Include incidental powers (open accounts, grant security, etc.)
- **Exclude** all activities not incidental to the qualifying asset business
- Reference s.110 TCA 1997 notification and compliance obligations [VERIFY drafting standards]

### Classification of Section 110 Compliance Issues

| Issue                                               | Classification   | Action                                         |
| --------------------------------------------------- | ---------------- | ---------------------------------------------- |
| Qualifying assets clearly identified                | COMPLIANT        | Document and maintain asset schedule           |
| First transaction below €10M                        | NON-COMPLIANT    | Cannot use s.110 regime; consider alternatives |
| No Revenue notification filed                       | NON-COMPLIANT    | File notification immediately                  |
| Activities beyond qualifying asset scope            | NON-COMPLIANT    | May invalidate s.110 status; seek tax advice   |
| Objects clause too broad for DAC                    | STRUCTURAL ISSUE | Redraft to restrict to qualifying activities   |
| Profit participating notes not structured correctly | HIGH RISK        | Tax specialist review required                 |

> **Warning**: Section 110 structures attract Revenue scrutiny. Abusive arrangements (e.g.,
> charitable purposes s.110s targeting Irish residential mortgages) led to Finance Act 2016
> amendments restricting the regime. Engage specialist tax and legal advisers for any
> s.110 structuring. Legalcode cannot substitute for specialist s.110 advice.

---

## Share Capital and Registered Office

### Share Capital

| Company Type          | Minimum Capital                                                    |
| --------------------- | ------------------------------------------------------------------ |
| LTD                   | None — no minimum                                                  |
| DAC, CLG (shares), UC | None — no minimum                                                  |
| PLC                   | €25,000 issued (at least 25% paid up before business commencement) |

**Practical share capital structuring for LTDs:**

- Minimum practical amount: €1 (100 shares at €0.01 each) to €100 (100 shares at €1 each)
- For founder equity: consider 100 shares at €1 each, with room to issue new shares
  under approved share option plans
- Authorized share capital: not mandatory under CA 2014; LTDs can have unlimited
  authorized shares (statutory default)
- Preference shares: require express constitution provisions defining rights
- Share classes: ordinary, preference, A/B/C founders' shares — define in constitution

**Payment of shares:**

- Shares do not need to be fully paid on allotment for LTDs
- Shareholder liability is limited to the unpaid amount on their shares
- PLC shares: minimum 25% of nominal value + full share premium must be paid on allotment

### Registered Office

- Every Irish company must have a registered office **in Ireland** (Republic of Ireland)
- Must be a physical, identifiable address — PO Box is not sufficient
- Company name must be displayed at registered office
- All statutory registers must be maintained at registered office (or another location in
  the State, notified to CRO)
- Changes to registered office: notify CRO via Form B2 or annual return

---

## Post-Incorporation Compliance Roadmap

### The 7 Statutory Registers

Every Irish company must maintain these registers:

| Register                                     | Contents                                                                               | Retention                  |
| -------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------- |
| 1. **Register of Members**                   | Shareholder details, shareholdings, transfer history                                   | Company lifetime + 6 years |
| 2. **Register of Directors and Secretaries** | Officer names, addresses, dates of appointment/resignation                             | Company lifetime + 6 years |
| 3. **Register of Directors' Interests**      | Directors' and secretaries' interests in company shares and debentures                 | Company lifetime + 6 years |
| 4. **Register of Debenture Holders**         | Debenture holder details (PLCs)                                                        | Company lifetime + 6 years |
| 5. **Register of Beneficial Owners**         | Persons with Significant Control (PSC) / UBO — per EU Anti-Money Laundering Directives | Company lifetime + 6 years |
| 6. **Register of Charges**                   | Security interests (mortgages, charges, debentures) over company assets                | Company lifetime + 6 years |
| 7. **Accounting Records**                    | Complete financial records supporting accounts                                         | 6 years minimum            |

**Beneficial Owners Register — important note:**
Ireland transposed the EU Anti-Money Laundering Directives requiring maintenance of a
beneficial ownership register. Companies must:

- Identify and record all "beneficial owners" (natural persons ultimately owning or
  controlling ≥25% of shares, voting rights, or ownership interest)
- File with the CRO Central Register of Beneficial Ownership (RBO — rbo.gov.ie) [VERIFY]
- Update within 14 days of any change [VERIFY current timeframe]

### Company Seal

Every Irish company must hold a **Common Seal** (company seal):

- Must have the company name engraved in legible characters
- Required for: share certificates, deeds, certain formal documents
- Under CA 2014, use of the seal must be authorised by the board and witnessed
- Modern practice: some documents may use electronic execution alternatives [VERIFY
  current position on e-signing and seal requirements]

### First AGM Requirements

| Company Type      | AGM Obligation                                                                                           |
| ----------------- | -------------------------------------------------------------------------------------------------------- |
| LTD               | Not required if all members consent to written resolutions in lieu; first AGM otherwise within 18 months |
| DAC, PLC, CLG, UC | Required annually; first AGM within 18 months of incorporation                                           |

### Revenue Tax Registration Timeline

Must register within **30 days** of commencing to trade:

| Tax             | Registration Form | Threshold                                         |
| --------------- | ----------------- | ------------------------------------------------- |
| Corporation Tax | Form TR2          | All companies — mandatory                         |
| VAT             | Form TR2          | €37,500 (services) / €75,000 (goods) or voluntary |
| PAYE/Employer   | Form TR2          | If employing any staff                            |

Registration via Revenue Online Service (ROS) at ros.ie:

- Obtain company's Tax Reference Number
- Required for invoicing, contract compliance, and payroll
- Cannot register for tax until CRO registration number is issued

### Compliance Calendar Template

| Timeframe                       | Obligation                                          | Source               |
| ------------------------------- | --------------------------------------------------- | -------------------- |
| **Day 1 (incorporation)**       | Confirm registered office address                   | CA 2014              |
| **Within 30 days of trading**   | Register with Revenue (TR2)                         | TCA 1997             |
| **Within 30 days of trading**   | Register for RBO (beneficial ownership)             | SI 110/2019 [VERIFY] |
| **6 months from incorporation** | File first annual return (no accounts)              | CA 2014, s.343       |
| **Within 18 months**            | Hold first AGM or sign written resolution           | CA 2014, s.175       |
| **Annually (ARD + 56 days)**    | File annual return with financial statements        | CA 2014              |
| **Within 14 days of change**    | Notify CRO of director/secretary changes (Form B10) | CA 2014              |
| **Within 14 days of change**    | Update beneficial ownership register                | SI [VERIFY]          |
| **Continuously**                | Maintain statutory registers                        | CA 2014              |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise any failures before delivery.

| Gate           | Rule                                                                                                                        | Fail Action                                            |
| -------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **Source**     | Every legal claim cites a specific section of CA 2014, TCA 1997, or other identified statute                                | Add citation or mark "[UNVERIFIED]"                    |
| **Format**     | Citations follow consistent Irish legal citation format (e.g., "CA 2014, s.137")                                            | Fix format                                             |
| **Currency**   | Every cited provision checked against potential Finance Act amendments                                                      | Flag "[CHECK CURRENCY — Finance Act may have amended]" |
| **Domain**     | Analysis stays within Irish company law — do not bleed in UK Companies Act 2006 provisions without flagging the distinction | Remove or flag cross-jurisdictional bleed              |
| **Confidence** | Uncertainty explicitly stated, not hidden                                                                                   | Add confidence qualifier                               |

### Self-Interrogation for Critical Compliance Items

For any item classified at the CRITICAL or HIGH severity level, apply this 3-pass review:

**Pass 1 — Legal chain integrity**: Does the risk assessment follow logically from the
cited CA 2014 / TCA 1997 provision? Would the CRO or Revenue actually take the described
enforcement action?

**Pass 2 — Completeness**: Have all relevant statutory provisions been considered? Are
there exemptions or carve-outs that might apply (e.g., group audit exemption for
subsidiaries)?

**Pass 3 — Challenge**: What is the strongest argument that the compliance issue is less
severe? Under what circumstances might a company legitimately be in this position?
(e.g., the Section 137 bond may already be held but simply not documented in the intake
information)

### Confidence Scoring

| Level        | Range     | Meaning                                                  | Action                                     |
| ------------ | --------- | -------------------------------------------------------- | ------------------------------------------ |
| **Definite** | 0.95–1.0  | Clear CA 2014 statutory text                             | State with confidence; cite section        |
| **High**     | 0.80–0.94 | Strong authority, minor interpretive questions           | State with brief caveat                    |
| **Probable** | 0.60–0.79 | Good arguments, could differ in edge cases               | State with reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuinely uncertain — e.g., recent Finance Act amendment | Flag for professional review               |
| **Unlikely** | 0.0–0.39  | Speculative or relying on outdated authority             | Do not assert; flag "[UNCERTAIN — verify]" |

### Glass Box Audit Trail Template

```yaml
glass_box:
  skill_name: "legalcode-ie-company-formation"
  mode: "Company formation advisory"
  topic: "Irish company formation — Companies Act 2014"
  jurisdiction: "Ireland (Republic of Ireland)"
  company_type_assessed: "[LTD / DAC / PLC / CLG / UC]"
  eea_director_status: "[Confirmed / Bond held / NON-COMPLIANT]"
  audit_exemption_status: "[Eligible / Excluded / Ineligible / Unknown]"
  section_110_applicable: "[Yes / No]"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[path or 'Not created']"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "All fee amounts should be verified against current CRO published fees schedule"
    - "Finance Act amendments post-knowledge date may have changed qualifying conditions"
    - "Section 110 structuring requires specialist tax and legal adviser review"
    - "CBI authorisation requirements are outside the scope of this skill"
  reviewer: "AI-assisted — requires review by qualified Irish solicitor and tax adviser"
```

---

## Anti-Patterns

What NOT to do when advising on or conducting Irish company formation.

1. **Treating an LTD as having an objects clause.** LTD companies have no objects
   clause under CA 2014. Advising that an LTD is "restricted to X activities" or that
   activities "outside its objects" are void is incorrect — only DAC and certain other
   types have objects clauses. This conflates the old Companies Acts pre-2015 regime.

2. **Confusing EEA residency with EEA citizenship.** The Section 137 requirement is
   about where the director is ordinarily resident (≥6 months per year in an EEA state),
   not about citizenship or passport. An Irish passport holder living in the US does
   not satisfy the requirement.

3. **Ignoring the Section 137 bond renewal.** The bond is valid for only 2 years.
   Failing to track its expiry and renew it leaves the company criminally non-compliant
   from the expiry date. This is one of the most commonly missed compliance obligations
   for foreign-owned Irish companies.

4. **Filing the first annual return late on the assumption it does not matter because
   no accounts are attached.** The first return (6 months from incorporation) matters
   enormously: filing it late triggers a 2-year loss of audit exemption, even though
   no financial statements are required.

5. **Using a DAC constitution template for an LTD.** DAC constitutions include a
   Memorandum of Association with an objects clause — this document is structurally
   incompatible with LTD incorporation. Using it for an LTD will cause Form A1 rejection.

6. **Treating Irish company formation as identical to UK (English) company formation.**
   Ireland and the UK have separate Companies Acts since Brexit (CA 2014 vs. CA 2006).
   Key differences: LTD vs. Ltd/plc structure, no UK-style model articles, different AGM
   rules, different audit exemption thresholds, Irish-specific s.137 bond requirement,
   separate CRO and Companies House systems.

7. **Assuming a single director can also be the company secretary in all cases.**
   For an LTD with a single director, the sole director cannot be the company secretary —
   a separate person or body corporate must be appointed. Overlooking this causes Form A1
   rejection and ongoing compliance failure.

8. **Recommending "no share capital" for a trading LTD.** While technically permissible,
   operating an LTD with zero issued share capital creates practical problems (banking,
   opening accounts, investor perception). Recommend at minimum €100 in issued capital.

9. **Stating the company can begin trading immediately upon CRO incorporation.** In
   regulated sectors (financial services, insurance, healthcare, food production, alcohol
   retail, etc.), CBI authorisation or other regulatory licences are required before
   trading lawfully begins. Incorporation and authorisation to trade are distinct steps.

10. **Advising that audit exemption is automatic.** Audit exemption must be claimed
    annually and depends on meeting 2 of 3 size criteria and not triggering any Schedule 5
    exclusion. It is lost for 2 years after a late annual return. It is not permanent
    and cannot be assumed from one year to the next.

11. **Ignoring the Beneficial Ownership Register (RBO) filing.** Under Irish AML
    transposition, companies must identify and register beneficial owners (PSC/UBO) with
    the RBO (rbo.gov.ie). Failure to file is a criminal offence under the relevant SI.
    This step is separate from and in addition to the CRO registration.

12. **Using Section 110 status casually for non-qualifying activities.** Section 110 is
    a narrow tax regime for qualifying assets in structured finance contexts. Attempting
    to use it for standard trading companies, general holding companies, or investment
    in non-qualifying assets risks Revenue challenge and retrospective loss of tax-neutral
    status — potentially exposing the company to significant unpaid tax liabilities plus
    interest and penalties.

13. **Drafting a Section 110 objects clause that is too broad.** A DAC used as a s.110
    vehicle should have a tightly drafted objects clause restricted to qualifying asset
    activities. Over-broad objects undermine investor comfort and may attract Revenue
    scrutiny over whether the company genuinely qualifies under s.110.

14. **Omitting the company seal from post-incorporation setup.** Every Irish company
    must hold a company seal. Attempting to execute share certificates, deeds, or other
    documents requiring the seal without one causes legal invalidity or at minimum
    execution delays.

15. **Not calendaring the Revenue registration deadline.** Every company must register
    with Revenue within 30 days of commencing to trade. Missing this deadline exposes
    the directors to penalties and delays the issuance of the company's tax reference
    number, which is required for invoicing and payroll.

16. **Assuming constitution can be amended informally.** Constitution amendments require
    a **special resolution** (75% of members) and must be filed with the CRO within
    **15 days** of being passed. Informal board decisions cannot amend the constitution.

17. **Not tracking ARD changes.** The Annual Return Date can be changed (extended once)
    by filing before the current ARD. If a company extends its ARD without properly
    understanding the resulting new deadline, it may inadvertently file late.

---

## Writing Standards

Before delivering any output:

- **State the entity type recommendation first**: Lead with the conclusion ("Based on
  the information provided, an LTD is the most appropriate entity type because..."),
  then the reasoning.
- **Number compliance issues**: Use numbered lists for multi-issue compliance reports
  so the user can act on items sequentially.
- **Flag CRITICAL issues immediately**: EEA director non-compliance and Section 137
  bond lapses are CRITICAL — flag at the top of any output, not buried in a list.
- **Use tables for deadlines and fees**: Tabular format makes compliance timelines and
  fee schedules immediately scannable.
- **Distinguish CRO requirements from Revenue requirements**: They are separate
  regulatory bodies with different obligations; confusion causes errors.
- **Do not assert Section 110 compliance**: Always recommend specialist tax adviser
  involvement for s.110 structuring; do not state that a proposed structure "qualifies"
  without that qualification.
- **Cite section numbers**: Every statutory reference should include the section number
  (e.g., "CA 2014, s.137" not just "the Companies Act").
- **Mark uncertain items explicitly**: Use [VERIFY] for any provision that may have
  been amended or where current CRO/Revenue practice may differ from statutory text.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for: "Companies Act 2014 Ireland director requirements", "Section 110 TCA 1997
  qualifying company", "CRO annual return penalties Ireland"
- Verify: current Section 137 bond amount and duration
- Verify: current audit exemption thresholds (turnover €12M / balance sheet €6M / 50 employees)
- Verify: current s.110 qualifying asset definition following any Finance Act amendments
- Save results to `/tmp/legalcode-ie-formation-research.md`
- Mark legalcode-mcp sourced citations as VERIFIED in Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with statutory framework in this skill
- Mark all fee amounts and Finance Act-dependent provisions with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Recommend that the user verify current CRO fees at cro.ie/publications/fees and
  Revenue guidance at revenue.ie before relying on specific figures

---

## Output Format Template

````markdown
# Irish Company Formation Analysis

**Company name proposed:** [name]
**Analysis date:** [date]
**Jurisdiction:** Ireland (Republic of Ireland)
**Skill version:** legalcode-ie-company-formation

---

## 1. Entity Type Recommendation

**Recommended type:** [LTD / DAC / PLC / CLG / UC]
**Confidence:** [Definite / High / Probable]

**Rationale:**
[2-3 sentence explanation of why this entity type is recommended]

**Alternatives considered:**

- [Type]: [Why not recommended]
- [Type]: [Why not recommended]

---

## 2. Director and Officer Compliance

### Director Assessment

| Director | EEA Resident? | Compliant?                  | Notes |
| -------- | ------------- | --------------------------- | ----- |
| [Name]   | [Yes/No]      | [COMPLIANT / NON-COMPLIANT] |       |

**EEA Residency Status:** [COMPLIANT / NON-COMPLIANT / Bond required]

[If bond required:]

> **ACTION REQUIRED**: No EEA-resident director identified. A Section 137 bond
> covering €25,000 must be obtained before incorporation. Bond is valid for 2 years.

### Company Secretary Assessment

| Secretary | Eligible? | Notes |
| --------- | --------- | ----- |
| [Name]    | [Yes/No]  |       |

---

## 3. Constitution Summary

**Constitution type:** [Single document (LTD) / Memorandum and Articles (DAC/other)]

**Mandatory provisions to include:**

- [ ] Company name with correct suffix
- [ ] Company type statement
- [ ] Registered office location
- [ ] [Other mandatory items]

**Recommended bespoke provisions:**

- [ ] [Bespoke item 1]
- [ ] [Bespoke item 2]

---

## 4. CRO Registration Checklist

**Estimated timeline:** [Standard 5 working days / Expedited same/next day]
**Estimated fee:** [€50 + any extras] [VERIFY current fee]

- [ ] Company name reserved (if desired) — €25 [VERIFY]
- [ ] Form A1 prepared and all consents signed
- [ ] Constitution prepared and signed by subscriber(s)
- [ ] EEA director confirmed or Section 137 bond arranged
- [ ] Registered office confirmed (Irish address required)
- [ ] All director/secretary details verified (PPS/equivalent)
- [ ] Submission via CORE platform

---

## 5. Annual Return and Audit Exemption

**First Annual Return Date (ARD):** [6 months from incorporation = date]
**First filing deadline:** [ARD date]

**Audit Exemption Assessment:**

| Criterion                    | Status                             | Notes |
| ---------------------------- | ---------------------------------- | ----- |
| Turnover ≤ €12M              | [Eligible/Ineligible/Unknown]      |       |
| Balance sheet ≤ €6M          | [Eligible/Ineligible/Unknown]      |       |
| Employees ≤ 50               | [Eligible/Ineligible/Unknown]      |       |
| Schedule 5 exclusion         | [None / [Category]]                |       |
| **Overall exemption status** | [ELIGIBLE / EXCLUDED / INELIGIBLE] |       |

---

## 6. Section 110 Assessment (if applicable)

[If not applicable: "Section 110 SPV structure not applicable for this formation."]

**Qualifying status:** [COMPLIANT / NON-COMPLIANT / PENDING REVENUE NOTIFICATION]

| Requirement                  | Status | Notes |
| ---------------------------- | ------ | ----- |
| Irish tax residence          |        |       |
| Qualifying assets identified |        |       |
| First transaction ≥ €10M     |        |       |
| Revenue notification         |        |       |

**Specialist advice required:** [Yes — engage specialist tax and legal advisers before proceeding]

---

## 7. Post-Incorporation Compliance Roadmap

| Deadline                  | Obligation                              | Priority |
| ------------------------- | --------------------------------------- | -------- |
| Incorporation day         | Confirm registered office               | HIGH     |
| Within 30 days of trading | Revenue tax registration (TR2)          | HIGH     |
| Within 30 days            | RBO beneficial ownership registration   | HIGH     |
| [Date = 6 months]         | First annual return (no accounts)       | CRITICAL |
| [Date = 18 months]        | First AGM / written resolution in lieu  | HIGH     |
| [Date = ARD + 56 days]    | Annual return with financial statements | CRITICAL |

---

## 8. Issues and Recommendations

### CRITICAL Issues

[None / List of critical issues]

### HIGH Issues

[None / List of high issues]

### MEDIUM Issues

[None / List of medium issues]

---

## 9. Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-ie-company-formation"
  company_type_assessed: "[type]"
  eea_director_status: "[status]"
  audit_exemption_status: "[status]"
  section_110_applicable: "[Yes/No]"
  legalcode_mcp: "[Connected/Not connected]"
  citations_verified: "[X VERIFIED / Y UNVERIFIED]"
  confidence: "[HIGH/MEDIUM/LOW]"
  limitations:
    - "[specific limitations for this analysis]"
  reviewer: "AI-assisted — requires review by qualified Irish solicitor and tax adviser"
```
````

```

---

## Localization Notes

This skill is specific to the **Republic of Ireland** and applies Irish law only.

**Distinction from Northern Ireland (UK):** Northern Ireland is part of the United Kingdom
and companies incorporated in Northern Ireland are registered with Companies House (UK)
under the Companies Act 2006. Irish law (CA 2014) does not apply. If the user is forming
a company in Northern Ireland, this skill does not apply — use a UK company formation skill.

**Cross-border structures:** Many Irish holding company structures involve both an Irish
holding entity and operating subsidiaries in other EU member states. This skill covers
only the Irish entity. Subsidiaries in Germany, France, or other EU states are governed
by their own national company laws and should be assessed under the relevant
jurisdiction-specific skills.

**GDPR / Data Protection:** Irish companies are subject to GDPR (administered by the
Data Protection Commission — dataprotection.ie) and the Data Protection Act 2018. GDPR
compliance is outside the scope of this skill. Use the `gdpr-data-processing-addendum`
or equivalent skill for data protection advice.

**Employment law:** Post-incorporation employment law compliance (employment contracts,
WRC obligations) is covered by the `fixed-term-employment-contract-ie` skill and
applicable general employment skills, not this skill.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:
- Companies Act 2014 (as amended) — Irish Statute Book (irishstatutebook.ie)
- Taxes Consolidation Act 1997, s.110 — Irish Statute Book
- CRO official guidance — cro.ie (registration methods, fees, annual returns, audit exemption)
- Law Society of Ireland Practice Notes on incorporation of LTD under Companies Act 2014
- Revenue Commissioners guidance — revenue.ie (tax registration, corporation tax)
- Arthur Cox, Matheson, Mason Hayes & Curran, and William Fry published client guides
- Wikipedia entry on Irish Section 110 SPV (structure and legislative history)
- Computershare / Matheson guidance on EEA director requirement and Section 137 bond

Attribution: Legalcode original synthesis.
```
