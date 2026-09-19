---
name: legalcode-uk-residential-tenancy
description: Reviews UK residential tenancies in England and Wales — audits compliance with assured shorthold
  tenancy (AST) requirements, deposit protection obligations (Tenancy Deposit Scheme/DPS/mydeposits),
  Section 21 no-fault eviction preconditions and notice validity, Section 8 possession grounds and notice
  requirements, Renters' Rights Act 2025 abolition of ASTs and new possession regime, rent increase procedure
  under s.13 Housing Act 1988, Homes (Fitness for Human Habitation) Act 2018 obligations, HHSRS hazards,
  EPC and MEES energy efficiency obligations, gas safety certificate requirements, electrical installation
  condition reports (EICRs), tenant right to repair, HMO licensing, Right to Rent checks, and Tenant Fees
  Act 2019 compliance.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Reviews UK residential tenancies in England and Wales — audits compliance with assured shorthold tenancy (AST) requirements, deposit protection obligations (Tenancy Deposit Scheme/DPS/mydeposits), Section 21 no-fault eviction preconditions and notice validity, Section 8 possession grounds and notice requirements, Renters' Rights Act 2025 abolition of ASTs and new possession regime, rent increase procedure under s.13 Housing Act 1988, Homes (Fitness for Human Habitation) Act 2018 obligations, HHSRS hazards, EPC and MEES energy efficiency obligations, gas safety certificate requirements, electrical installation condition reports (EICRs), tenant right to repair, HMO licensing, Right to Rent checks, and Tenant Fees Act 2019 compliance. Use when auditing a landlord's statutory compliance before serving a possession notice, reviewing an AST for illegal terms, checking a Section 21 or Section 8 notice for validity, advising a tenant on their rights, assessing deposit protection penalties, reviewing a rent increase notice, or onboarding a new letting. Jurisdiction: England and Wales only. Covers Renters' Rights Act 2025 (Royal Assent 27 October 2025) including transitional provisions and the expected post- commencement periodic tenancy regime.


# Legalcode UK Residential Tenancy Review (England & Wales)

> **Disclaimer**: This skill provides a framework for AI-assisted review of residential
> tenancy matters under the law of England and Wales. It does not constitute legal advice.
> All outputs should be reviewed by a qualified solicitor admitted in England and Wales before
> use. Laws change; verify current applicability before relying on any provision described here.
> Statutory and case law references cited from memory carry hallucination risk -- verify against
> authoritative sources before relying on them. This skill does not apply to tenancies in
> Scotland, Northern Ireland, or Wales where devolved legislation applies distinct rules.

## Purpose and Scope

This skill audits residential tenancy matters in England and Wales against applicable statutory
obligations and common law requirements. It supports landlords, tenants, letting agents, and
advisers working with assured shorthold tenancies (ASTs) and the new periodic tenancy regime
under the Renters' Rights Act 2025.

**Covers:**

- Statutory compliance audit (all preconditions for possession and ongoing obligations)
- Tenancy agreement review (illegal clauses, missing provisions, Tenant Fees Act compliance)
- Possession notice validity check (Section 21 and Section 8)
- Renters' Rights Act 2025 transition assessment (current law vs. post-commencement regime)
- Deposit protection compliance and penalty risk assessment
- Energy performance and safety obligation audit (EPC, gas, EICR, MEES)
- Rent increase procedure review (Section 13 HA 1988)
- HMO licensing status assessment
- Right to Rent compliance review
- Tenant rights and remedies assessment

**Does not:**

- Advise on commercial or agricultural tenancies (separate regimes apply)
- Cover Scottish or Northern Irish tenancy law (distinct devolved legislation)
- Cover Welsh tenancies under the Renting Homes (Wales) Act 2016
- Draft new tenancy agreements (see drafting-specific skills)
- Provide legal advice or replace instruction of a qualified solicitor

## Jurisdiction and Governing Law

This skill applies exclusively to **England and Wales** under the Housing Act 1988 (as amended),
Housing Act 2004, Landlord and Tenant Act 1985, Homes (Fitness for Human Habitation) Act 2018,
Deregulation Act 2015, Tenant Fees Act 2019, and Renters' Rights Act 2025.

**Current legislative regime**: The Renters' Rights Act 2025 (c. 26) received Royal Assent on
27 October 2025. As of early 2026, most substantive provisions are not yet in force pending
Commencement No. 2 regulations expected circa May 2026. The main changes on commencement are:
abolition of the AST category, conversion of all ASTs to periodic assured tenancies, abolition
of Section 21 no-fault eviction, introduction of new and amended Schedule 2 possession grounds,
rental bidding prohibition, and new anti-discrimination protections.

**Wales note**: Wales has its own devolved tenancy regime under the Renting Homes (Wales) Act
2016, which replaces ASTs with Occupation Contracts. This skill applies to England only unless
the user specifies a Welsh property and requests Wales-specific analysis.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. The workflow pauses and
asks when:

- The answer would change the direction of the analysis
- The applicable legal regime (pre- or post-RRA 2025 commencement) is unclear
- The user's perspective (landlord vs. tenant) affects which risks to prioritise
- Severity of a finding depends on business or personal context only the user can supply

Use the **CLARIFY** convention (structured options with descriptions and "why this matters")
wherever marked below. If the user has already provided the information, skip the question
and proceed. For partial context, state assumptions explicitly before proceeding.

---

## Workflow

### Step 1: Accept Materials

Accept materials in any of these formats:

- **Tenancy agreement**: PDF, DOCX, or pasted text of the AST or tenancy agreement
- **Possession notice**: Form 6A (s.21), Form 3 (s.8), or pasted text
- **Safety documents**: Gas safety record (CP12), EICR, EPC — file or description
- **Correspondence**: Letters, emails, or screenshots relevant to the dispute or audit
- **Description only**: If no documents are available, proceed on the basis of the
  user's description; mark all findings as requiring document verification

If no materials are provided, prompt the user to supply the relevant documents or describe
the tenancy in enough detail to proceed.

### Step 2: Gather Context

**CLARIFY** -- Before beginning the review, ask the user these questions:

1. **Use case**: What are you trying to achieve?
   - Options: (A) Pre-possession compliance audit -- checking whether all preconditions for
     serving a notice are met; (B) Section 21 notice validity check -- reviewing a notice
     already served or about to be served; (C) Section 8 notice validity check; (D) Full
     tenancy agreement review -- checking terms for illegal or problematic clauses;
     (E) Tenant rights assessment -- understanding what rights and remedies are available;
     (F) Deposit protection penalty assessment -- whether a penalty claim is available;
     (G) Rent increase challenge -- checking s.13 notice validity and tribunal referral
     right; (H) Ongoing compliance audit -- checking all landlord obligations are being met
   - _Why this matters_: Determines which of the 12 compliance categories to analyse in
     depth and what the output should focus on.

2. **Which side are you on?**
   - Options: Landlord (or their agent/solicitor), Tenant, Adviser (neutral/third party)
   - _Why this matters_: The entire analysis flips. A landlord needs to know what might
     invalidate a notice; a tenant needs to know which defences are available.

3. **Tenancy details**: When did the tenancy begin, and what type is it?
   - Options: Fixed-term AST (state length), Statutory periodic tenancy (AST has expired),
     Contractual periodic tenancy (periodic from the start), New tenancy (not yet started),
     Unknown
   - _Why this matters_: Determines which statutory regime applies, whether the RRA 2025
     transition is imminent, and which notice periods and forms are required.

4. **Is the property an HMO?**
   - Options: Yes (multiple households sharing); No; Unsure (describe property)
   - _Why this matters_: HMOs have additional licensing and management obligations; some
     HMO failures bar Section 21 and expose the landlord to rent repayment orders.

5. **Relevant background**: Any specific concerns or context?
   - Free text. Examples: tenant has complained about disrepair; local authority has
     visited; deposit was paid late; landlord is a company; property is in a selective
     licensing area; tenant receives housing benefit.
   - _Why this matters_: Retaliatory eviction protection, deposit protection bars, and
     licensing obligations depend on specific factual circumstances.

### Step 3: Determine Applicable Legal Regime

Identify which legal regime governs this tenancy and possession route:

**Pre-commencement regime (current law)**:
Applies to all tenancies where the Renters' Rights Act 2025 Commencement No. 2 SI has
not yet taken effect (expected circa May 2026 [VERIFY when SI is published]). Under this
regime: ASTs remain valid; Section 21 no-fault eviction is available; Section 8 grounds
operate under the pre-RRA 2025 Schedule 2.

**Post-commencement regime (RRA 2025)**:
Once the commencement SI takes effect: all ASTs automatically convert to periodic assured
tenancies; fixed-term provisions become void; Section 21 is repealed; only Section 8
and the new/amended Schedule 2 grounds are available. Transitional provisions in
Schedule 6 RRA 2025 allow s.21 notices served before commencement to be pursued within
a limited window (the shorter of: 6 months from notice date, or 3 months from
commencement date).

**CLARIFY** -- If the commencement date is uncertain at the time of review:

- "The Renters' Rights Act 2025 main provisions are expected to come into force circa
  May 2026 but the commencement SI has not yet been published. Should I analyse this:
  (A) Under current law (Section 21 still available); (B) Under the post-commencement
  RRA 2025 regime; (C) Under both -- flagging which route applies to which timeline?"
- If analysing a s.21 notice, confirm whether it was served before the expected
  commencement date and whether proceedings have been or will be issued within the
  transitional window.

### Step 4: Gather Legal Authority

Use **legalcode-mcp** -- the Legalcode law, regulatory, and case law database -- to
build a working reference file for this review.

**Search for the following authorities:**

- Housing Act 1988 ss.1, 5, 13-14, 19A, 20A, 21, 21A, 21B; Schedule 1, Schedule 2
- Housing Act 2004 ss.213-215 (deposit protection); Part 1 HHSRS; Part 2 HMO licensing
- Landlord and Tenant Act 1985 ss.11-14, 16-17
- Homes (Fitness for Human Habitation) Act 2018 (s.9A LTA 1985)
- Deregulation Act 2015 ss.33-39 (retaliatory eviction, prescribed requirements)
- Tenant Fees Act 2019 Schedules 1 and 2
- Renters' Rights Act 2025 ss.1-2, 6-9, 20, 56-57; Schedule 2 (amended grounds);
  Schedule 6 (transitional provisions)
- Assured Shorthold Tenancy Notices and Prescribed Requirements (England) Regulations
  2015 (SI 2015/1646)
- Energy Efficiency (Private Rented Property)(England and Wales) Regulations 2015
  (SI 2015/962)
- Electrical Safety Standards in the Private Rented Sector (England) Regulations 2020
  (SI 2020/312)
- Gas Safety (Installation and Use) Regulations 1998 (SI 1998/2451) reg. 36
- Key case law: _Trecarrell House Ltd v Rouncefield_ [2020] EWCA Civ 760; _Charalambous
  v Ng_ [2014] EWCA Civ 1604; _McDonald v McDonald_ [2016] UKSC 28; _Quick v Taff Ely
  BC_ [1986] QB 809; _Edwards v Kumarasamy_ [2016] UKSC 40

**Save results** to `/tmp/legalcode-uk-residential-tenancy-authority.md` structured as:

```
# Legal Authority Reference -- UK Residential Tenancy
## Date Gathered: [date]

### Statutes & Regulations
- [Statute name, section, current text or summary]

### Case Law
- [Case name, citation, key holding]

### Regulatory Guidance
- [Source, guidance, relevance]
```

**If legalcode-mcp is not connected:**

- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed on the basis of the statutory framework set out in this skill

### Step 5: Statutory Compliance Audit

Conduct the compliance audit across all applicable categories from the **Compliance
Analysis Reference** section. For each category:

- Assess whether the landlord has complied with the relevant obligation
- Classify as COMPLIANT, ADVISORY, or NON-COMPLIANT (see **Compliance Classification**)
- Note the specific deficiency and its legal consequences

**CLARIFY** -- For a pre-possession audit, ask the user before proceeding:

- "To complete the Section 21 preconditions checklist, I need to confirm the following.
  Please answer yes/no for each: (1) Was an EPC provided to the tenant before or at
  tenancy start? (2) Was a gas safety certificate (CP12) provided before or at move-in?
  (3) Has the current version of the How to Rent guide been provided? (4) Was the
  deposit protected and prescribed information given within 30 days? (5) Has an EICR
  been obtained and given to the tenant? (6) Has the local authority served any
  improvement notices? (7) Has the tenant made any written complaint about property
  condition that was not adequately responded to within 14 days?"

For any 'no' answer, classify that item as NON-COMPLIANT and flag as a bar to s.21.

### Step 6: Tenancy Agreement Review

If a tenancy agreement has been provided, review it against the following:

**CLARIFY** -- For comprehensive agreement review, ask:

- "Is this a standard letting agent template, a landlord-drafted agreement, or an
  online template? This affects how carefully to check for non-standard clauses."
- If this is a new agreement (not yet signed): focus on identifying provisions that
  are illegal under the Tenant Fees Act 2019 or void under the Housing Act 1988
  before signing.

Review in these areas (see **Agreement Review Reference** in the analysis section):

1. Required written terms (parties, property, rent, term, deposit)
2. Prohibited fees and charges under Tenant Fees Act 2019
3. Illegal or void terms (e.g., waiving repair obligations, excluding Homes Act 2018)
4. Deposit amount compliance (5 or 6 weeks' rent cap)
5. Notice provisions (compatibility with statutory notice periods)
6. Rent review clauses (validity under RRA 2025 if not yet in force)
7. Access provisions (compliance with s.16 LTA 1985 24-hour notice requirement)
8. Sub-letting and assignment provisions
9. Pet clauses (RRA 2025 s.11 right to request pet with insurance [NOT YET IN FORCE])

### Step 7: Possession Notice Review

If a possession notice has been provided or is being considered, review its validity.

**CLARIFY** -- Ask: "Is this a (A) Section 21 notice (Form 6A), (B) Section 8 notice
(Form 3), or (C) a notice to quit served by the tenant?"

**For Section 21 notices:**
Run all precondition checks in the **Section 21 Validity Checklist** (see analysis
reference). Any single bar to a valid s.21 renders the notice invalid; proceedings
under it will be struck out. Identify every applicable bar and, where possible, whether
it can be remedied.

**For Section 8 notices:**

- Confirm the grounds are stated on the notice and apply to the facts
- Confirm the notice period for each ground was given
- For Ground 8 (rent arrears): confirm arrears subsisted at the date of the notice
  AND will subsist at the hearing; advise pleading Grounds 8, 10, and 11 together
- Confirm proceedings are or will be issued within 12 months of the notice date
- For Grounds 7A and 14 (anti-social behaviour): confirm the expedited procedure
  was correctly invoked if applicable
- Under RRA 2025 (post-commencement): verify the notice period matches the new
  enhanced periods (4 months for Grounds 1, 1A, 1B, 2, 6, 6B; 4 weeks for
  Grounds 8, 10, 11, 18)

**For tenant notices to quit (or notices under RRA 2025):**

- Pre-commencement: minimum 4 weeks' notice or a full period, whichever is longer
  (s.5(3A) HA 1988)
- Post-commencement (RRA 2025 s.20): minimum 2 months' notice for tenant to end
  an assured periodic tenancy

**CLARIFY** -- If the notice has potential defects:

- "I have identified [N] potential defects in this notice. These range from [severity
  summary]. Do you want me to: (A) Identify whether any defect is curable and how;
  (B) Assess the risk that the defect would be raised as a defence in proceedings;
  (C) Both?"

### Step 8: Classify Findings

Apply the **Compliance Classification** system to every finding:

- **COMPLIANT (GREEN)**: Requirement met; no action needed
- **ADVISORY (AMBER)**: Minor non-compliance or latent risk; should rectify
- **NON-COMPLIANT (RED)**: Material failure; bars action or exposes to penalty

**CLARIFY** -- For borderline ADVISORY vs. NON-COMPLIANT findings, ask rather than assume:

- "The [specific document/obligation] was provided [X days] after the statutory deadline.
  Late provision may or may not cure this particular bar to s.21, depending on the case
  law. Should I classify this as ADVISORY (may be cured) or NON-COMPLIANT (risk remains)
  pending solicitor advice?" Present the relevant case law (e.g., _Trecarrell_ on late
  gas safety certificates).

For every NON-COMPLIANT finding, generate a **Remediation Action** using the format in
the **Remediation Action Format** section.

### Step 9: Prioritisation and Action Plan

Organise all findings using the **Prioritisation Framework** into:

- **Priority 1 (Immediate)**: Bars to serving/relying on a possession notice; criminal
  liability; penalty claims currently accruing
- **Priority 2 (Before service)**: Issues to cure before serving any new notice
- **Priority 3 (Ongoing)**: Compliance obligations to maintain throughout the tenancy

Provide a chronological action plan with specific steps, responsible party (landlord or
agent), and urgency.

### Step 10: Quality Verification

Before delivering the analysis, run the quality checks in the **Quality Assurance
Framework** section:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every NON-COMPLIANT (RED) finding, run the 3-pass Self-Interrogation.
3. Apply confidence scoring to each finding.
4. Complete the Glass Box Audit Trail.
5. Run the Writing Standards quality gates.

---

## Compliance Analysis Reference

This reference covers the 12 compliance categories. For each category, the analysis
identifies key requirements, common deficiencies, and legal consequences.

---

### Category A: Pre-Tenancy Documentation

**Requirements for Section 21 preconditions (SI 2015/1646):**

All four of the following must be provided to the tenant **before or at tenancy start**
for a valid s.21 notice to be served in the future:

| Document                                                                                                                                           | Legal Basis                                                  | Timing                                                                             | Form                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------- | ------------------------ |
| Energy Performance Certificate (EPC)                                                                                                               | SI 2012/3118 reg. 9; SI 2015/1646 reg. 2(1)(a)               | Before tenancy start (not: before marketing)                                       | Free copy to tenant      |
| Gas Safety Record (CP12)                                                                                                                           | SI 1998/2451 reg. 36(6)(a); SI 2015/1646 reg. 2(1)(b)        | Before tenant moves in                                                             | Current record only      |
| How to Rent guide                                                                                                                                  | s.21B HA 1988 (as ins. by DA 2015 s.39); SI 2015/1646 reg. 3 | Before tenancy commences; re-provide if updated version published since last given | Current MHCLG version    |
| EICR [VERIFY: exact bar on s.21 for EICR non-provision is under SI 2020/312 not SI 2015/1646 -- confirm whether failure to provide EICR bars s.21] | SI 2020/312 reg. 3                                           | Before new tenancy; within 28 days for existing tenants                            | Copy of full EICR report |

**Common deficiencies:**

- Using an outdated version of the How to Rent guide (must be the version current at
  the date it is provided; providing a new copy on renewal is required if the guide
  has been updated since last given)
- Providing the EPC after the tenancy start date (bars s.21 permanently for that
  tenancy -- cannot be cured by late provision for an already-served notice)
- Gas safety certificate provided to tenant **after** the tenancy commences: following
  _Trecarrell House Ltd v Rouncefield_ [2020] EWCA Civ 760, late provision **can** cure
  the s.21 bar going forwards (the landlord may serve a valid s.21 after providing
  it), but a s.21 notice served **before** the certificate was provided remains invalid
- Providing the EICR only to the incoming tenant without having first obtained one
  (the obligation to inspect arises before tenancy start, not after)

---

### Category B: Deposit Protection

**Statutory framework**: Housing Act 2004 ss.213-215.

**Core obligations (both must be completed within 30 days of receipt of deposit):**

1. Protect the deposit in one of the three government-authorised schemes: Tenancy
   Deposit Scheme (TDS), Deposit Protection Service (DPS), or mydeposits.
2. Provide the tenant (and any relevant person who paid the deposit) with all
   **prescribed information** under SI 2007/797 (as amended):
   - The amount of the deposit
   - The address of the rented property
   - Which scheme holds it and the scheme's contact details
   - The scheme's dispute resolution service
   - The landlord/agent's name and contact details
   - Third-party payer details (if applicable)
   - Circumstances in which deductions may be made
   - Deposit return procedures
   - What to do if the landlord cannot be contacted at tenancy end
   - How to raise a dispute

**Deposit amount cap** (Tenant Fees Act 2019 s.3; Schedule 1):

- Annual rent below £50,000: maximum **5 weeks' rent**
- Annual rent £50,000 or above: maximum **6 weeks' rent**
- Holding deposit (separate from tenancy deposit): maximum **1 week's rent**

**Consequences of non-compliance (s.214 HA 2004):**

- County court must order repayment of deposit plus a penalty of **1x to 3x the deposit
  amount** within 14 days
- Section 21 bar (s.215 HA 2004): a valid s.21 notice cannot be served while the deposit
  is unprotected or prescribed information has not been given; can be cured by returning
  the deposit in full to the tenant

**Periodic tenancy issue (\***Charalambous v Ng**\* [2014] EWCA Civ 1604 [VERIFY]):**
When an AST expires and a statutory periodic tenancy arises, a **new** tenancy is created.
The landlord must re-protect the deposit (or confirm existing protection covers the new
tenancy) and re-serve prescribed information for the statutory periodic tenancy within
30 days. Failure to do so bars s.21 for the periodic tenancy.

**Common deficiencies:**

- Late protection (even by one day) triggers the penalty, though late protection cures
  the s.21 bar prospectively
- Prescribed information served but missing required items (partial service is
  insufficient -- all prescribed items must be given)
- Deposit not re-confirmed/re-served on renewal or roll-over to periodic tenancy
- Excess deposit taken (above the 5 or 6-week cap) -- bars s.21 and attracts TFA 2019
  penalty until the excess is refunded

---

### Category C: Tenancy Agreement Terms and Tenant Fees Act 2019

**Permitted payments only (TFA 2019 Schedule 1):**
A landlord or letting agent may charge only:

- Rent (no front-loading arrangements where initial rent is higher than later rent)
- Tenancy deposit (up to 5 or 6 weeks' rent)
- Holding deposit (up to 1 week's rent; return obligations apply)
- Default payments: late rent interest (max 3% above Bank of England base rate);
  evidenced actual cost of replacing lost keys
- Contract variation/novation: greater of £50 or reasonable actual costs
- Early termination: landlord's actual losses only (must be evidenced)
- Utilities, council tax, TV licence, and communication services if required by the
  tenancy agreement

**Prohibited payments penalty (TFA 2019 s.8):**

- First breach: financial penalty up to **£5,000**
- Second or aggravated breach within 5 years: up to **£30,000** or prosecution as a
  banning order offence
- TFA 2019 s.17: landlord cannot serve a valid s.21 while a prohibited payment
  has been made and not repaid

**Void terms (HA 1988 s.11; LTA 1985 s.11; common law):**
The following provisions in a tenancy agreement are void:

- Any term purporting to exclude or restrict the landlord's s.11 LTA 1985 repair
  obligations or the s.9A LTA 1985 fitness covenant
- Any term imposing a prohibited payment on the tenant
- Any term requiring the tenant to use a particular supplier of utilities or services
  unless the tenant has been given a genuine choice and fair opportunity to switch
- Under RRA 2025 (post-commencement): any fixed-term provision; any term requiring
  a rent period of more than 1 month; any term forbidding tenant notice to quit

**Review checklist for tenancy agreements:**

| Clause                           | Red Flags                                                                                                                         |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Parties and property description | Missing landlord address; no property address; no licence/HMO licence number if required                                          |
| Rent and payment terms           | Front-loaded rent; charges for late payment exceeding 3% above base rate; payment frequency >1 month post-RRA 2025                |
| Deposit clause                   | Amount exceeds cap; no scheme identified; no prescribed information attached                                                      |
| Repair obligations               | Attempts to transfer s.11 obligation to tenant; requires tenant to redecorate at fixed intervals                                  |
| Access and inspection            | Does not give the 24-hour written notice required by s.16 LTA 1985                                                                |
| Permitted use                    | Residential only clause acceptable; specific prohibition on pets may conflict with RRA 2025 s.11                                  |
| Sub-letting                      | Absolute prohibition is permissible; must not require unreasonable consent fees                                                   |
| Alterations                      | Must not prohibit reasonable disability adjustments (EA 2010 Schedule 4)                                                          |
| Termination by landlord          | No notice clause or clause shorter than 2 months for s.21 purposes                                                                |
| Termination by tenant            | If stated notice period is less than 4 weeks (pre-RRA 2025) or 2 months (post-RRA 2025), it is void and statutory minimum applies |

---

### Category D: Right to Rent Checks

**Statutory framework**: Immigration Act 2014 Part 3; SI 2014/2354 (prescribed documents);
Home Office Code of Practice January 2024.

**Obligations:**

- Before a new tenancy commences, the landlord must check that every adult occupier
  (aged 18+) has the right to rent in the United Kingdom
- Check method: verify original documents (List A for unlimited right; List B for
  time-limited right) or use the Home Office online checking service for biometric
  residence permit holders
- Retain copies for the duration of the tenancy plus **1 year** after it ends
- For List B occupiers: conduct a follow-up check before the earlier of the
  document's expiry date or 12 months after the previous check

**Penalties for non-compliance (as of February 2024 [VERIFY exact SI]):**

- Up to **£20,000** per adult occupier found to be disqualified (increased from £3,000)
- Criminal offence for knowingly renting to a disqualified person: up to **5 years'
  imprisonment**

**Discrimination risk**: Right to Rent checks must be conducted consistently for all
prospective tenants. Checking only those perceived to be foreign nationals constitutes
unlawful discrimination under the Equality Act 2010.

---

### Category E: Property Fitness and HHSRS

**Homes (Fitness for Human Habitation) Act 2018 (s.9A LTA 1985):**
The landlord covenants that the dwelling-house:

- Is fit for human habitation at the time of the letting; and
- Will remain fit throughout the tenancy

**Fitness is assessed by reference to the 29 HHSRS hazard categories** under the Housing
Health and Safety Rating System (HA 2004 Part 1), including:

- Category 1 hazards (mandatory LA enforcement): excess cold, falls on stairs, damp and
  mould, electrical hazards, structural collapse risk
- Category 2 hazards (discretionary enforcement)

**Tenant's remedy**: Civil claim in county court without prior LA notification. Court
may order specific performance and/or award damages. Any exclusion clause is void.

**Section 21 bar via retaliatory eviction (DA 2015 s.33):**
If the following sequence occurs, s.21 is barred for 6 months:

1. Tenant makes a **written complaint** to the landlord about property condition
2. Landlord fails to respond adequately within **14 days** (or responds inadequately)
3. Tenant complains to the local housing authority
4. LA serves a relevant notice (HHSRS improvement notice or emergency remedial action)

A s.21 notice served after the retaliatory eviction trigger is invalid and proceedings
under it will be struck out.

**s.11 LTA 1985 repair obligations** (tenancies under 7 years):
The landlord must keep in repair:

1. The structure and exterior (including drains, gutters, external pipes)
2. Installations for water, gas, electricity and sanitation (including baths, sinks)
3. Installations for space heating and hot water

**Scope**: Obligation to repair requires notice of the defect (except for defects in
parts the landlord controls or common parts). Obligation is to repair, not to improve
or rebuild (_Quick v Taff Ely BC_ [1986] QB 809 [VERIFY citation]).

**Access**: Landlord may enter on 24 hours' written notice (s.16 LTA 1985) to inspect;
no right of entry without notice except for genuine emergency.

---

### Category F: Energy Performance and MEES

**EPC obligations:**

- Landlord must have a valid EPC (10-year validity) for the property and must provide a
  copy free of charge to the prospective tenant before tenancy commences
- No valid EPC bars s.21 notice service

**Minimum Energy Efficiency Standards (MEES):**
Energy Efficiency (Private Rented Property)(England and Wales) Regulations 2015
(SI 2015/962). As of **1 April 2020**: landlords **cannot** let a property with EPC
rating F or G (below band E) without a registered exemption.

**Valid exemptions (must be registered on PRS Exemptions Register):**

- Cost-cap exemption: all improvements costing up to £3,500 (inc. VAT) have been made
  and the property is still below band E
- Third-party consent exemption: consent from superior landlord, planning authority,
  or listed building consent was sought and refused
- Devaluation exemption: works would reduce property value by 5%+ (written RICS report
  required)
- New landlord exemption: 6-month exemption after a property is inherited in tenanted
  condition

**MEES penalties (SI 2015/962 reg. 40 [VERIFY current penalty levels]):**

- Breach <3 months: up to **£2,000** + publication penalty
- Breach ≥3 months: up to **£4,000** + publication penalty
- False/misleading exemption registration: up to **£1,000**
- Maximum total for a single reg. 23 breach: **£5,000**

**Proposed uplift to EPC band C**: Government has stated intention to raise minimum to
band C by 2030 (new tenancies) and 2033 (all tenancies) but no implementing SI has been
enacted as of March 2026 [VERIFY status].

---

### Category G: Gas and Electrical Safety

**Gas Safety (SI 1998/2451 reg. 36):**

| Obligation               | Requirement                                                                                                                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Annual inspection        | Gas Safe registered engineer; every 12 months                                                                                                                                                |
| Gas Safety Record (CP12) | Obtained after each inspection; retained 2 years                                                                                                                                             |
| Provision to tenant      | Before new tenant moves in; within 28 days of annual check for existing tenants                                                                                                              |
| Section 21 bar           | Failure to provide before tenancy start: s.21 barred until provided (late provision cures bar for future notices: _Trecarrell House Ltd v Rouncefield_ [2020] EWCA Civ 760 [VERIFY holding]) |
| Criminal liability       | Up to £6,000 fine per breach; HSW Act 1974 for serious offences                                                                                                                              |

**Electrical Safety (SI 2020/312):**

| Obligation          | Requirement                                                                          |
| ------------------- | ------------------------------------------------------------------------------------ |
| EICR inspection     | Qualified electrician; every 5 years or earlier if EICR specifies                    |
| Standard            | 18th Edition Wiring Regulations (BS 7671)                                            |
| Provision to tenant | Before new tenancy (from the inspection date); within 28 days for existing tenants   |
| Remediation         | Required work must be completed within 28 days (or shorter period if EICR specifies) |
| Penalty             | Up to **£40,000** financial penalty                                                  |

---

### Category H: HMO Licensing

**Mandatory HMO licensing** (HA 2004 s.55; SI 2018/221):
A licence is required if the property:

- Is occupied by **5 or more persons**
- From **2 or more separate households**
- Any storey is used for the residential purposes of the HMO
- Meets the standard, self-contained flat, or converted building test (s.254 HA 2004)

**Additional licensing**: Local authorities may extend licensing to HMOs of 3-4 persons;
check local council website for current designations.

**Selective licensing (HA 2004 s.80)**: Local authorities may require all PRS landlords
in designated areas to obtain a licence regardless of HMO status; check council website.

**Consequences of operating without a licence:**

- Unlimited fine on summary conviction
- Rent Repayment Order (RRO): tenants may reclaim up to **12 months' rent** (extended
  to **24 months** under RRA 2025 when in force [VERIFY])
- Local authority may make a Management Order taking over management of the property
- Unlicensed HMO status bars Section 21

**HMO minimum room sizes (SI 2018/221):**

- 1 person aged 10+: minimum **6.51 m²**
- 2 persons aged 10+: minimum **10.22 m²**
- Children under 10: minimum **4.64 m²**
- Rooms below minimum must not be occupied; rooms between 4.64 m² and 6.51 m² are
  limited to one child under 10

---

### Category I: Section 21 Validity Checklist

Use this checklist for every s.21 analysis. Each item is a **hard bar** if failed:

| #   | Precondition                                       | Legal Basis               | Bar to s.21?              | Curable?                                                                 |
| --- | -------------------------------------------------- | ------------------------- | ------------------------- | ------------------------------------------------------------------------ |
| 1   | EPC provided before tenancy start                  | SI 2015/1646 reg. 2(1)(a) | YES                       | Only by returning deposit + serving fresh notice after compliance        |
| 2   | Gas safety record provided before move-in          | SI 2015/1646 reg. 2(1)(b) | YES                       | Late provision cures bar (_Trecarrell_): can then serve valid s.21       |
| 3   | Current How to Rent guide provided                 | SI 2015/1646 reg. 3       | YES                       | Provide current version; can then serve                                  |
| 4   | EICR provided to tenant [VERIFY bar on s.21]       | SI 2020/312               | LIKELY YES                | Provide EICR; then serve                                                 |
| 5   | Deposit protected in authorised scheme             | s.215 HA 2004             | YES                       | Return deposit in full or achieve compliance; can then serve             |
| 6   | Deposit prescribed information served              | s.215 HA 2004             | YES                       | Serve prescribed info; can then serve (subject to penalty still payable) |
| 7   | Deposit amount within cap                          | TFA 2019 s.17             | YES                       | Refund excess; can then serve                                            |
| 8   | No prohibited payments outstanding                 | TFA 2019 s.17             | YES                       | Repay prohibited payment; can then serve                                 |
| 9   | No improvement notice within last 6 months         | s.21A HA 1988             | YES                       | Wait for 6-month bar to expire                                           |
| 10  | No retaliatory eviction trigger                    | DA 2015 s.33              | YES                       | Wait for 6-month bar to expire                                           |
| 11  | Property not an unlicensed HMO                     | HA 2004                   | YES                       | Obtain licence first                                                     |
| 12  | Form 6A used (current version)                     | SI 2015/1646 reg. 4       | YES if outdated form used | Re-serve using current Form 6A                                           |
| 13  | Notice gives minimum 2 months                      | s.21(4) HA 1988           | YES if shorter            | Re-serve with correct period                                             |
| 14  | Notice not served within 4 months of tenancy start | s.21(4B) HA 1988          | YES if too early          | Re-serve after 4-month point                                             |
| 15  | Proceedings issued within 6 months of notice       | s.21(4D) HA 1988          | YES if expired            | Re-serve new notice                                                      |
| 16  | Section 21 not yet abolished (pre-commencement)    | RRA 2025                  | YES if post-commencement  | Use s.8 / RRA 2025 grounds                                               |

**Note on notice alignment**: England removed the requirement that s.21 notices expire on
the last day of a period for post-October 2015 tenancies (DA 2015 s.35).

---

### Category J: Section 8 Grounds Reference

**Notice**: Form 3 (prescribed form). Proceedings must begin within **12 months** of
service of the notice.

**Mandatory grounds (court MUST order possession if proved):**

| Ground        | Basis                                                   | Notice Period                                   | Key Requirement                                                                                                                                                                   |
| ------------- | ------------------------------------------------------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1             | Landlord/family member occupation                       | 2 months                                        | Prior written notice at tenancy start required (court can dispense with reasonable grounds); extended to grandparents/siblings under RRA 2025                                     |
| 2             | Mortgagee exercising power of sale                      | 2 months                                        | Mortgage must pre-date tenancy or notice given at start                                                                                                                           |
| 4A (RRA 2025) | Student HMO (June-September)                            | 4 months [post-commencement]                    | Prior written notice required at tenancy start                                                                                                                                    |
| 7A            | Serious criminal offence, ASB injunction, closure order | 1 month (periodic)                              | Conviction or order must subsist                                                                                                                                                  |
| 7B            | Immigration disqualification                            | 2 weeks                                         | Home Office notice in force                                                                                                                                                       |
| 8             | Rent arrears                                            | 2 weeks (pre-RRA 2025); 4 weeks (post-RRA 2025) | Current threshold: weekly/fortnightly ≥8 weeks; monthly ≥2 months (post-RRA 2025: raised to 13 weeks/3 months respectively). Arrears must subsist at BOTH notice AND hearing date |

**Ground 8 tactical note**: Advise pleading Grounds **8, 10, and 11 together**. Tenants
who partially repay arrears between notice and hearing defeat Ground 8 (mandatory) but
not Grounds 10 and 11 (discretionary). Grounds 10/11 allow the court to order possession
if it is reasonable to do so.

**New grounds under RRA 2025 (post-commencement, not yet in force):**

| Ground | Basis                                       | Notice Period |
| ------ | ------------------------------------------- | ------------- |
| 1A     | Landlord intends to sell                    | 4 months      |
| 1B     | Rent-to-buy scheme (social landlords)       | 4 months      |
| 6B     | Landlord compliance with enforcement action | 4 months      |

**Discretionary grounds (court MAY order possession if reasonable):**

| Ground | Basis                                           | Notice Period |
| ------ | ----------------------------------------------- | ------------- |
| 9      | Suitable alternative accommodation available    | 2 months      |
| 10     | Some rent arrears at notice + proceedings       | 2 weeks       |
| 11     | Persistent late payment                         | 2 weeks       |
| 12     | Breach of tenancy obligation (other than rent)  | 2 weeks       |
| 13     | Property deterioration through tenant neglect   | 2 weeks       |
| 14     | Nuisance/annoyance to neighbours or illegal use | Immediate     |
| 15     | Deterioration of furniture                      | 2 weeks       |
| 17     | Tenant induced tenancy by false statement       | 2 weeks       |

---

### Category K: Rent Increase Procedure

**Contractual rent review**: If the tenancy agreement contains a valid rent review clause,
rent may be increased in accordance with it. Under RRA 2025 (post-commencement), contractual
escalation clauses are void; only the s.13 procedure or written agreement following that
procedure is permitted [NOT YET IN FORCE -- VERIFY when SI takes effect].

**Section 13 HA 1988 procedure (for statutory and contractual periodic tenancies without
a rent review clause):**

1. Landlord serves a **Form 4** notice proposing a new rent (or equivalent notice meeting
   statutory requirements)
2. Minimum notice periods: yearly tenancy: **6 months**; monthly tenancy: **1 month**;
   weekly tenancy: **1 month**
3. New rent takes effect at the start of the next rental period after the notice period
   expires
4. Annual cap: rent may only be increased **once per 52 weeks** (s.13(2) HA 1988)
5. **Tenant's right to challenge**: Before the new period begins, tenant may refer to the
   First-tier Tribunal (Property Chamber) -- Residential Property. The Tribunal sets
   the open-market rent; the increase is suspended pending determination. Tenant must
   apply before the new rent period begins (not after).

**Post-RRA 2025 changes to s.13 (not yet in force):** Tribunal cannot set a rent higher
than the amount proposed in the landlord's notice; proposed rent in the notice is the
ceiling, not a floor.

---

### Category L: Renters' Rights Act 2025 Transition

**Current status**: Most substantive provisions not in force as of March 2026. Expected
commencement circa May 2026 [VERIFY].

**For landlords with fixed-term ASTs:**

- At commencement: the fixed-term provisions become void. The tenancy converts to a
  periodic assured tenancy.
- Rent period alignment: if the current rent period exceeds 1 month, it must be brought
  into compliance within [VERIFY transitional period in Schedule 6].

**Section 21 transitional window (Schedule 6 RRA 2025):**

- A s.21 notice **validly served before the commencement date** may be relied upon
  in proceedings, provided those proceedings are commenced within the shorter of:
  - 6 months from the date of the s.21 notice; or
  - 3 months from the commencement date
- After that window closes, s.21 is permanently unavailable.

**Planning ahead for post-commencement possession:**

- Landlords wishing to regain possession must use the s.8 route and prove a ground
- Ground 1A (sale intention) requires the tenancy to have been running for at least
  1 year and gives 4 months' notice
- Ground 1 (own occupation) also requires minimum 1-year tenancy; extended family
  members (grandparents, siblings) qualify; 4 months' notice
- Ground 8 rent arrears threshold raised to 13 weeks (weekly) / 3 months (monthly)

---

## Compliance Classification

### COMPLIANT (GREEN)

All statutory requirements for this category are met. No deficiencies identified.
The landlord may proceed with serving a possession notice or continuing the tenancy
without risk on this point.

**Action**: Record compliance in the Glass Box. No further action required.

### ADVISORY (AMBER)

A minor non-compliance, potential gap, or latent risk exists. The obligation may be
met in substance but documentation is unclear, timing was imperfect, or there is
ongoing exposure to a low-probability claim. Should be rectified to reduce risk.

**Examples**:

- EICR obtained but not provided to tenant within the 28-day window
- How to Rent guide provided but not the most current version (guide updated between
  tenancy renewals and new version not re-served)
- Periodic tenancy deposit prescribed information not re-served after statutory rollover
  but original tenancy prescribed information was complete

**Action**: Generate a Remediation Action with urgency "Before service of next notice".

### NON-COMPLIANT (RED)

A material failure that either bars the landlord from serving a possession notice,
creates significant penalty exposure (financial or criminal), or materially compromises
the tenant's statutory rights.

**Immediate triggers for NON-COMPLIANT:**

- Any single s.21 precondition bar (EPC, gas, deposit, How to Rent, improvement notice,
  retaliatory eviction protection)
- Deposit not protected or prescribed information not given (penalty of 1-3x deposit)
- Prohibited payment taken and not repaid (TFA 2019 bars s.21 + penalty up to £30,000)
- MEES breach (F or G EPC, no registered exemption) -- up to £5,000 penalty
- No mandatory HMO licence -- unlimited fine + rent repayment order risk
- Right to Rent checks not conducted -- up to £20,000 per occupant
- Section 21 served after commencement of RRA 2025 without transitional window compliance
- Form 6A (s.21) or Form 3 (s.8) does not meet prescribed requirements

**Action**: Generate a Remediation Action with urgency "Immediate" and flag the specific
legal consequence.

---

## Remediation Action Format

For every ADVISORY or NON-COMPLIANT finding, generate a remediation using this format:

```
**Category**: [Compliance category A-L]
**Finding**: [Description of the specific non-compliance or risk]
**Severity**: [ADVISORY (AMBER) / NON-COMPLIANT (RED)]
**Legal basis**: [Statute, regulation, or case -- or "[VERIFY]"]
**Risk**: [Consequence if not remediated -- penalty amount, bar to action, criminal liability]
**Remediation**: [Specific action to take; who must take it; what document/step is needed]
**Urgency**: [Immediate / Before service of any notice / Before tenancy renewal / Ongoing obligation]
**Confidence**: [Confidence level per scoring scale]
**Curable**: [Yes -- describe cure / No -- existing notices invalid; must re-serve / Partial]
```

---

## Prioritisation Framework

### Priority 1 -- Immediate

Items that must be addressed before any other action. These are either:

- Live bars to a possession notice already served or about to be served
- Active financial penalties currently accruing (e.g., deposit penalty period running)
- Criminal liability risks (e.g., unlicensed HMO, gas safety, Right to Rent failure)

**Rule**: Address Priority 1 items before issuing court proceedings. A s.21 notice with
a Priority 1 bar will be struck out; a s.8 notice for rent arrears will still proceed
but the landlord faces concurrent liability on the uncured issue.

### Priority 2 -- Before Service of Next Notice

Items that must be cured before a new possession notice can be validly served:

- Missing pre-tenancy documents (EPC, gas, How to Rent, EICR) where late provision
  would cure the bar under current case law
- Outstanding prohibited payments where repayment would lift the TFA 2019 bar
- Deposit protection and prescribed information gaps where compliance is achievable

**Rule**: Cure all Priority 2 items, verify cure in writing, then serve the notice.
Do not serve the notice and attempt to cure simultaneously.

### Priority 3 -- Ongoing

Obligations that must be maintained throughout the tenancy to preserve the ability
to act later and avoid penalty:

- Annual gas safety inspections and certificate provision
- 5-yearly EICR renewal
- Maintaining minimum EPC band E (or registered exemption)
- Right to Rent follow-up checks for tenants with time-limited leave
- Compliance with repair obligations (s.11 LTA 1985; Homes Act 2018)
- Maintaining HMO licence currency

**Rule**: Prioritise ongoing obligations by risk severity: criminal liability (gas,
Right to Rent) → financial penalties (electrical, MEES) → s.21 bar risk (deposit,
How to Rent updates) → civil liability (disrepair, fitness).

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Before beginning the audit, confirm: (1) which compliance categories are
relevant to the user's use case; (2) which documents have been provided; (3) which
side is being advised; (4) whether RRA 2025 transitional analysis is required.

**DO**: Work systematically through each applicable compliance category. Document every
finding before classifying it. Do not classify without a specific legal basis.

**CHECK**: Run the Citation Quality Gates on every finding. Apply Self-Interrogation
to every NON-COMPLIANT item. Apply Confidence Scoring before delivery.

**ACT**: Revise any finding that fails the quality gates. Update the Glass Box.
Deliver the report only after all quality checks pass.

---

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                         | Fail Action                                                      |
| -------------- | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established principle                             | Add citation or mark "[UNVERIFIED -- solicitor to confirm]"      |
| **Format**     | All citations follow English law format (e.g., _Case Name_ [year] court citation; SI year/number)            | Fix format                                                       |
| **Currency**   | Check that cited provisions have not been amended or repealed; note RRA 2025 provisions not yet in force     | Flag "[CHECK CURRENCY -- RRA 2025 commencement may affect this]" |
| **Domain**     | All analysis is under the law of England and Wales; no Scottish, Welsh, or NI rules applied without flagging | Remove or flag jurisdictional bleed                              |
| **Confidence** | Uncertainty explicitly stated, not hidden; no confident assertion where law is transitional                  | Add confidence qualifier; mark uncertain points [VERIFY]         |

**Jurisdiction-specific Currency Gate note**: The Renters' Rights Act 2025 is enacted
but not fully in force. Any provision from the Act must be marked "[NOT YET IN FORCE --
check commencement]" unless it was brought into force by Commencement No. 1 (SI 2025/1354,
certain provisions only). Verify the commencement status of each provision before advising.

---

### Self-Interrogation for NON-COMPLIANT Items

For every NON-COMPLIANT (RED) finding, apply this 3-pass review before delivery:

**Pass 1 -- Legal Chain Integrity**: Does the non-compliance finding follow logically
from the statute or regulation cited? Would a district judge in the county court or a
First-tier Tribunal member actually reach this conclusion on these facts? Is there a
technical cure (e.g., late provision of a document) that the current case law permits?

**Pass 2 -- Completeness**: Have all relevant statutory provisions been considered?
Have any regulations that modify the primary legislation been checked? Have the relevant
transitional provisions of the Renters' Rights Act 2025 been applied where relevant?
Is the penalty figure current and not superseded by amendment?

**Pass 3 -- Challenge**: What is the strongest argument that the landlord is **not**
in breach on this point? Under what circumstances might a court or tribunal accept the
landlord's position? Is the NON-COMPLIANT classification proportionate to the actual
risk, or should this be ADVISORY with a caveat?

After each pass: if a weakness is identified, revise the finding before delivery.
Mark with `self_interrogation: PASS` or `self_interrogation: REVISED` in Glass Box.

---

### Confidence Scoring

| Level        | Range     | Meaning                                                        | Action                                                   |
| ------------ | --------- | -------------------------------------------------------------- | -------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled law; clear statutory text; no ambiguity                | State with confidence                                    |
| **High**     | 0.80-0.94 | Strong authority; minor interpretation questions               | State with brief caveat                                  |
| **Probable** | 0.60-0.79 | Good arguments; reasonable minds could differ                  | State with reasoning and contra-indicators               |
| **Possible** | 0.40-0.59 | Genuinely uncertain; competing authorities or transitional law | Flag for solicitor review with both sides                |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative; no supporting authority               | Do not assert; flag "[UNCERTAIN -- solicitor to advise]" |

**Classification thresholds:**

- NON-COMPLIANT (RED) requires confidence HIGH (0.80+). If confidence is below 0.80,
  classify as ADVISORY and flag for solicitor review.
- ADVISORY (AMBER) requires confidence PROBABLE (0.60+). If below 0.60, flag for
  solicitor review regardless of classification.
- COMPLIANT (GREEN) requires confidence HIGH (0.80+). If uncertain whether requirements
  are met, classify as ADVISORY.

---

## Glass Box Audit Trail

Append the following YAML block to every delivered report:

```yaml
glass_box:
  skill: "legalcode-uk-residential-tenancy"
  governing_law: "Laws of England and Wales"
  use_case: "[Pre-possession audit / Agreement review / Section 21 validity / Section 8 validity / Tenant rights / Deposit / Rent increase / Ongoing compliance audit]"
  party_advised: "[Landlord / Tenant / Agent / Neutral]"
  tenancy_type: "[Fixed-term AST / Statutory periodic / Contractual periodic / Unknown]"
  tenancy_start: "[date or 'Not provided']"
  legal_regime: "[Pre-RRA 2025 commencement / Post-commencement / Both / Unknown]"
  rra_2025_commencement_verified: "Yes [SI reference] / No -- assumed [date] / Unknown"
  categories_audited:
    pre_tenancy_docs: "COMPLIANT / ADVISORY / NON-COMPLIANT / Not assessed"
    deposit_protection: "COMPLIANT / ADVISORY / NON-COMPLIANT / Not assessed"
    tenancy_agreement: "COMPLIANT / ADVISORY / NON-COMPLIANT / Not assessed"
    right_to_rent: "COMPLIANT / ADVISORY / NON-COMPLIANT / Not assessed"
    property_fitness: "COMPLIANT / ADVISORY / NON-COMPLIANT / Not assessed"
    energy_epc_mees: "COMPLIANT / ADVISORY / NON-COMPLIANT / Not assessed"
    gas_electrical_safety: "COMPLIANT / ADVISORY / NON-COMPLIANT / Not assessed"
    hmo_licensing: "COMPLIANT / ADVISORY / NON-COMPLIANT / Not assessed"
    section_21_validity: "VALID / INVALID / Not assessed -- [bars identified]"
    section_8_validity: "VALID / INVALID / Not assessed -- [grounds assessed]"
    rent_increase: "COMPLIANT / NON-COMPLIANT / Not assessed"
    rra_2025_transition: "Assessed / Not assessed"
  overall_classification: "COMPLIANT / ADVISORY / NON-COMPLIANT"
  noncompliant_items: "[number] -- [brief list]"
  advisory_items: "[number]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "Housing Act 1988 ss.21, 21A, 21B -- [VERIFIED/UNVERIFIED]"
    - "Housing Act 2004 ss.213-215 -- [VERIFIED/UNVERIFIED]"
    - "Landlord and Tenant Act 1985 ss.11, 16 -- [VERIFIED/UNVERIFIED]"
    - "Homes (Fitness for Human Habitation) Act 2018 -- [VERIFIED/UNVERIFIED]"
    - "Tenant Fees Act 2019 -- [VERIFIED/UNVERIFIED]"
    - "Renters' Rights Act 2025 -- [VERIFIED/UNVERIFIED] -- commencement status noted"
    - "SI 2015/1646 -- [VERIFIED/UNVERIFIED]"
    - "SI 2020/312 -- [VERIFIED/UNVERIFIED]"
    - "SI 1998/2451 reg. 36 -- [VERIFIED/UNVERIFIED]"
  cases_consulted:
    - "Trecarrell House Ltd v Rouncefield [2020] EWCA Civ 760 -- [VERIFIED/UNVERIFIED]"
    - "Charalambous v Ng [2014] EWCA Civ 1604 -- [VERIFIED/UNVERIFIED]"
    - "McDonald v McDonald [2016] UKSC 28 -- [VERIFIED/UNVERIFIED]"
    - "[additional cases as applicable]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no NON-COMPLIANT items)"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  confidence: "HIGH / MEDIUM / LOW -- [rationale]"
  limitations:
    - "RRA 2025 commencement date not confirmed by SI at time of review -- transitional analysis based on expected May 2026 commencement"
    - "[Any other scope limitations, missing documents, or assumptions]"
  reviewer: "AI-assisted -- requires qualified solicitor review"
```

---

## Anti-Patterns

What NOT to do when reviewing UK residential tenancy matters:

1. **Treating the Section 21 precondition bars as a checklist to pass once** -- The
   bars must be met continuously. A deposit that was protected but not re-confirmed
   for a statutory periodic tenancy re-activates the bar. How to Rent guide updates
   published after the last serving require a fresh copy. The analysis must assess
   compliance at the date the notice was served, not just at tenancy start.

2. **Conflating current law with the Renters' Rights Act 2025** -- The Act received
   Royal Assent but is not yet in force in most respects. Advising on Section 21 under
   a regime that has already abolished it (or advising on the new periodic tenancy regime
   as if it is current law) is a significant error. Always identify which regime applies
   and flag commencement uncertainty.

3. **Assuming late document provision always cures the s.21 bar** -- _Trecarrell_ held
   that late provision of a gas safety certificate **can** cure the bar for future s.21
   notices, but the notice already served before provision remains invalid. Not all
   precondition bars are curable by late provision (e.g., the EPC bar is widely treated
   as incurable for a notice already served; [VERIFY current position]).

4. **Failing to spot the periodic tenancy deposit problem** -- Many practitioners know
   to protect on the fixed-term start but miss the _Charalambous_ requirement to re-
   protect (or confirm protection covers) and re-serve prescribed information when the
   tenancy rolls over to statutory periodic. This is a common source of invalid s.21
   notices.

5. **Citing Ground 8 in isolation** -- Ground 8 (mandatory rent arrears) requires arrears
   to subsist at **both** the date of the notice **and** the hearing. Tenants frequently
   reduce arrears below the threshold before the hearing, defeating Ground 8 in isolation.
   Always plead Grounds 8, 10, and 11 together.

6. **Using an outdated Form 6A or Form 3** -- Prescribed forms are periodically updated.
   An outdated form invalidates the notice. Confirm the form is the current prescribed
   version before serving. Do not assume a form downloaded previously is still current.

7. **Missing the 6-month proceedings deadline for s.21** -- A valid s.21 notice becomes
   worthless if court proceedings are not issued within 6 months of the notice date (or
   within 4 months of the date specified in the notice if that date is more than 2 months
   from service). Landlords who delay proceedings must re-serve a fresh notice.

8. **Advising on retaliatory eviction based only on verbal complaints** -- The retaliatory
   eviction bar under DA 2015 s.33 requires a **written** tenant complaint to the landlord.
   Verbal complaints do not trigger the statutory protection. Conversely, tenants who have
   complained verbally should be advised to put the complaint in writing to protect themselves.

9. **Ignoring MEES exemptions on the register** -- A property with EPC F or G may be lawfully
   let if a valid exemption is registered on the PRS Exemptions Register. Always check the
   register before classifying a breach; advise unregistered landlords to register an
   exemption if they qualify before serving any notice or continuing a tenancy.

10. **Treating selective licensing as an HMO issue only** -- Selective licensing schemes
    cover all PRS properties in a designated area, not just HMOs. In areas with active
    designations (e.g., parts of London, Manchester, Liverpool), a single-occupancy
    flat still requires a licence. Failure to check local council designations is a
    common error.

11. **Overlooking the Right to Rent follow-up obligation** -- Initial checks are commonly
    done; follow-up checks for tenants with time-limited leave are frequently missed. The
    follow-up obligation triggers when the earlier of the relevant document's expiry or
    12 months from the previous check. Missing a follow-up check exposes the landlord to
    the same penalty as missing the initial check (up to £20,000 per occupant).

12. **Applying the wrong deposit cap** -- The 5-week cap applies to tenancies where annual
    rent is below £50,000. The 6-week cap applies above £50,000. Applying the wrong cap
    is a prohibited payment and bars s.21 until the excess is refunded.

13. **Confusing s.11 LTA 1985 with the Homes Act 2018** -- Section 11 covers structural
    disrepair; the Homes Act 2018 (s.9A LTA 1985) covers fitness. Condensation and damp
    from poor design may not be "disrepair" under _Quick v Taff Ely_ but may still breach
    the fitness covenant. Always consider both bases; do not dismiss a tenant claim on
    the s.11 analysis alone without also checking the 2018 Act.

14. **Ignoring the McDonald v McDonald limitation** -- Tenants in private tenancies cannot
    use Article 8 ECHR as a defence to possession proceedings brought by a private landlord
    (_McDonald v McDonald_ [2016] UKSC 28 [VERIFY]). Do not advise tenants that Article 8
    is a viable defence in this context.

15. **Missing the 4-month rule for s.21** -- Section 21 notices cannot be served within
    4 months of the tenancy commencing (not 4 months from the date of an AST that has
    expired into periodic -- the 4-month period runs from the **original** tenancy start,
    including for replacement tenancies of the same property between the same parties).
    A notice served too early is invalid.

16. **Treating post-RRA 2025 transitional s.21 as perpetually available** -- The Schedule
    6 RRA 2025 transitional window is short (6 months from notice date or 3 months from
    commencement, whichever is shorter). Landlords with pre-commencement s.21 notices
    must issue proceedings promptly or the window closes. This is not a grace period of
    general duration.

17. **Single-pass review without cross-checking** -- The s.21 precondition bars interact.
    A landlord may be clear on deposit protection but have a latent retaliatory eviction
    bar from a repair complaint made months earlier. Review all 16 precondition items in
    the checklist before confirming a s.21 is valid; do not stop at the first clear item.

---

## Writing Standards

**For remediation actions** (to be shared with landlords, agents, or tenants):

- Plain language. One action per step. No legal jargon without explanation.
- Active voice: "Provide the tenant with a copy of the gas safety record" not "The gas
  safety record should be provided."
- Name the actor: "You (the landlord) must..." or "The letting agent must..."
- Specific, not vague: cite the statutory provision; state the exact document; give the
  deadline.
- British English: organisation, licence, favour, defence, authorise, programme.

**For legal analysis** (internal to the review):

- Cite every legal claim to a specific provision or case
- State confidence level where the law is transitional or unclear
- Note "[NOT YET IN FORCE]" for every RRA 2025 provision pending commencement
- Mark all unverified citations [VERIFY]

**Quality gates before delivery:**

1. Can a landlord or tenant with no legal background understand the action plan?
2. Is every NON-COMPLIANT finding supported by a specific statutory provision?
3. Has every RRA 2025 provision been correctly labelled with its commencement status?
4. Are all citations in correct English law format?
5. Has British English spelling been used throughout?
6. Is the report concise: findings in order of urgency, action plan clear?
7. Has the Glass Box been completed and appended?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for all statutes, SIs, and key cases listed in that step
- Save verified authorities to `/tmp/legalcode-uk-residential-tenancy-authority.md`
- Check currency of RRA 2025 commencement -- search for the Commencement No. 2 SI to
  confirm whether it has been published and which provisions it brings into force
- Verify the current prescribed form versions (Form 6A, Form 3, Form 4)
- Check for any MEES penalty uplift SIs or EPC band C commencement SIs
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Include a prominent notice that legal citations require independent verification
  before relying on them in proceedings
- Focus analysis on the compliance framework and structural risk, flagging that
  specific penalty figures and case law holdings require current-source verification

---

## Output Format Template

```markdown
## UK Residential Tenancy Review (England & Wales)

**Property**: [address]
**Landlord**: [name]
**Tenant(s)**: [names]
**Tenancy start date**: [date]
**Tenancy type**: [Fixed-term AST / Statutory periodic / Contractual periodic]
**Use case**: [Pre-possession audit / Agreement review / etc.]
**Party advised**: [Landlord / Tenant / Agent / Neutral]
**Legal regime**: [Pre-RRA 2025 commencement / Post-commencement]
**Review basis**: [Documents reviewed / Description only]
**Date of review**: [date]

---

## Compliance Overview

| Category                    | Status                               | Priority Items     |
| --------------------------- | ------------------------------------ | ------------------ |
| A. Pre-Tenancy Documents    | COMPLIANT / ADVISORY / NON-COMPLIANT | [summary]          |
| B. Deposit Protection       | COMPLIANT / ADVISORY / NON-COMPLIANT | [summary]          |
| C. Agreement / Tenant Fees  | COMPLIANT / ADVISORY / NON-COMPLIANT | [summary]          |
| D. Right to Rent            | COMPLIANT / ADVISORY / NON-COMPLIANT | [summary]          |
| E. Property Fitness / HHSRS | COMPLIANT / ADVISORY / NON-COMPLIANT | [summary]          |
| F. EPC / MEES               | COMPLIANT / ADVISORY / NON-COMPLIANT | [summary]          |
| G. Gas / Electrical Safety  | COMPLIANT / ADVISORY / NON-COMPLIANT | [summary]          |
| H. HMO Licensing            | COMPLIANT / ADVISORY / NON-COMPLIANT | [summary]          |
| I. Section 21 Validity      | VALID / INVALID / N/A                | [bars identified]  |
| J. Section 8 Grounds        | VALID / ISSUES / N/A                 | [grounds assessed] |
| K. Rent Increase            | COMPLIANT / NON-COMPLIANT / N/A      | [summary]          |
| L. RRA 2025 Transition      | Assessed / N/A                       | [summary]          |

**Overall status**: COMPLIANT / ADVISORY / NON-COMPLIANT

---

## Key Findings

[Top 3-5 issues with severity and one-line summaries. Lead with any bars to
possession or criminal liability risks.]

---

## Issues Found

### [Issue 1 -- NON-COMPLIANT / ADVISORY] | Category [X] | Priority [1/2/3]

**Category**: [A-L]
**Finding**: [Description]
**Severity**: NON-COMPLIANT (RED) / ADVISORY (AMBER)
**Legal basis**: [Statute/case]
**Risk**: [Consequence]
**Remediation**: [Specific action]
**Urgency**: [Immediate / Before notice / Ongoing]
**Curable**: [Yes/No/Partial -- explain]
**Confidence**: [Confidence level]

[Repeat for each issue]

---

## Section 21 Validity Assessment (if applicable)

**Notice validity**: [VALID / INVALID -- [bars identified]]
**Preconditions checklist**:

| #                           | Precondition               | Status      | Notes  |
| --------------------------- | -------------------------- | ----------- | ------ |
| 1                           | EPC provided               | PASS / FAIL | [note] |
| 2                           | Gas safety record provided | PASS / FAIL | [note] |
| 3                           | How to Rent guide          | PASS / FAIL | [note] |
| 4                           | EICR provided              | PASS / FAIL | [note] |
| 5                           | Deposit protected          | PASS / FAIL | [note] |
| [continue for all 16 items] |                            |             |        |

**Conclusion**: [Can s.21 proceed? What must be cured first? Is re-service required?]

---

## Section 8 Assessment (if applicable)

**Ground(s) relied on**: [e.g., Grounds 8, 10, 11]
**Notice period**: [Given / Required / Status]

| Ground               | Mandatory/Discretionary | Notice Period | Status    | Notes                         |
| -------------------- | ----------------------- | ------------- | --------- | ----------------------------- |
| 8                    | Mandatory               | 2 weeks       | PASS/FAIL | [arrears amount; subsisting?] |
| [additional grounds] |                         |               |           |                               |

---

## RRA 2025 Transitional Assessment (if applicable)

**Applicable**: [Yes -- transitional window analysis / No -- pre-commencement]
**Key issue**: [e.g., Outstanding s.21 notice -- must issue proceedings by [date]]
**Post-commencement route**: [Best available ground under new regime]

---

## Action Plan

**Priority 1 -- Immediate action required:**

1. [Specific action, owner, urgency]

**Priority 2 -- Before serving any notice:**

1. [Specific action, owner, timing]

**Priority 3 -- Ongoing obligations:**

1. [Specific action, owner, frequency]

---

## Next Steps

1. [e.g., Obtain current gas safety certificate and provide to tenant before serving s.21]
2. [e.g., Register MEES exemption on PRS Exemptions Register within 30 days]
3. [e.g., Consult a solicitor on the retaliatory eviction bar before proceeding]

---

## Glass Box Audit Trail

[YAML block as defined in Glass Box section]
```

---

## Localization Notes

This skill covers England and Wales only. The following jurisdictional variants may be
needed for users in adjacent jurisdictions:

**Scotland**: Scottish tenancies are governed by the Private Housing (Tenancies) (Scotland)
Act 2016, which introduced the Private Residential Tenancy (PRT). Section 21 has no Scottish
equivalent; a landlord must prove a ground from Schedule 3 of the 2016 Act. A separate skill
would be required for Scotland.

**Wales**: Welsh tenancies are governed by the Renting Homes (Wales) Act 2016 (RHWA 2016),
effective 1 December 2022. The Act replaced ASTs with Occupation Contracts (standard or
secure contracts). Section 21 is replaced by a s.186 RHWA 2016 no-fault possession notice,
which requires 6 months' notice for a standard contract (from 1 June 2023). A separate
skill would be required for Wales.

**Northern Ireland**: Northern Irish private tenancies are governed by the Private Tenancies
(Northern Ireland) Order 2006, with separate deposit protection, notice, and fitness
requirements. A separate skill would be required for Northern Ireland.

**England -- London supplement**: Some obligations (e.g., selective licensing schemes) are
particularly prevalent in London boroughs. When reviewing a London property, check the
relevant borough council website for active selective licensing and additional HMO licensing
designations, which are more common than in other English regions.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis for England and Wales residential
tenancy compliance, drawing on primary legislation (Housing Act 1988, Housing Act 2004,
Landlord and Tenant Act 1985, Deregulation Act 2015, Tenant Fees Act 2019, Renters' Rights
Act 2025), subordinate legislation (SI 2015/1646, SI 2020/312, SI 1998/2451, SI 2015/962),
and leading case law (_Trecarrell House Ltd v Rouncefield_ [2020] EWCA Civ 760,
_Charalambous v Ng_ [2014] EWCA Civ 1604, _McDonald v McDonald_ [2016] UKSC 28,
_Quick v Taff Ely BC_ [1986] QB 809, _Edwards v Kumarasamy_ [2016] UKSC 40).
Structural patterns and quality frameworks adapted from the legalcode-contract-review
gold standard skill. All statutory and case law references require verification against
authoritative sources. The Renters' Rights Act 2025 commencement status must be verified
at the date of use; most substantive provisions are expected to come into force circa
May 2026 but the commencement SI had not been published as of March 2026.
