---
name: legalcode-residential-lease-review
description: Review residential leases and tenancy agreements for tenants, landlords, and property managers
  — identify problematic clauses, flag illegal provisions, generate compliance checklists, and produce
  jurisdiction-specific remediation actions. Use when reviewing an Assured Shorthold Tenancy (AST) or
  periodic assured tenancy in England and Wales, a US state residential lease, an Australian residential
  tenancy agreement, or a German Mietvertrag (tenancy contract under BGB).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review residential leases and tenancy agreements for tenants, landlords, and property managers — identify problematic clauses, flag illegal provisions, generate compliance checklists, and produce jurisdiction-specific remediation actions. Use when reviewing an Assured Shorthold Tenancy (AST) or periodic assured tenancy in England and Wales, a US state residential lease, an Australian residential tenancy agreement, or a German Mietvertrag (tenancy contract under BGB). Covers: rent and payment terms, security deposit / bond / Kaution, tenant and landlord rights, maintenance and repairs, habitability standards, termination and eviction grounds, rent control and increase limits, fair housing and anti-discrimination obligations, renewal provisions, and statutory compliance gaps. Jurisdiction-agnostic framework with deep coverage of UK (Renters' Rights Act 2025), US (implied warranty of habitability, Fair Housing Act, state rent control), Australia (2024 state tenancy reforms), and Germany (BGB §535–580a, Mietpreisbremse, Kündigungsschutz). Triggers on: residential lease review, tenancy agreement check, landlord tenant dispute, rent control compliance, eviction notice analysis, deposit dispute, AST review, Mietvertrag prüfen, rental agreement analysis.


# Legalcode Residential Lease Review

> **Disclaimer**: This skill provides a framework for AI-assisted residential lease review.
> It does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before use. Residential tenancy law
> changes frequently — statutory references cited here carry hallucination risk and may
> have been amended or superseded. Verify all legal citations against authoritative sources
> before relying on them. This skill does not represent either landlord or tenant in any
> legal proceeding.

## Purpose and Scope

This skill reviews residential lease and tenancy agreements from either the tenant's or
the landlord's perspective. It identifies problematic, illegal, or missing provisions,
classifies issues by severity, and generates actionable remediation steps tailored to
the governing jurisdiction.

**Covers:**

- Clause-by-clause analysis of any residential lease or tenancy agreement
- Identification of statutory non-compliance (void clauses, missing mandatory terms)
- Deviation classification (GREEN / YELLOW / RED)
- Jurisdiction-specific tenant rights and landlord obligations
- Missing provision detection (habitability, deposit protection, anti-discrimination)
- Fair housing and anti-discrimination compliance
- Rent control and rent increase limit analysis
- Eviction procedure and notice period compliance
- Remediation actions and negotiation points
- Quality-verified output with Glass Box audit trail

**Does not:**

- Provide legal advice or replace qualified legal counsel
- Draft new leases from scratch (use a drafting-specific skill for that)
- Adjudicate disputes or determine liability
- Apply exclusively to one jurisdiction — uses jurisdiction-agnostic framework with
  deep [JURISDICTION-SPECIFIC] analysis for UK, US, AU, and DE

**Best used for:**

- Tenants reviewing a lease before signing
- Landlords checking their own leases for statutory compliance
- Property managers auditing tenancy agreements in a portfolio
- Legal professionals conducting preliminary lease screening

## Jurisdiction and Governing Law

This skill is jurisdiction-aware. The lease's stated governing law or the property's
physical location determines which legal framework applies. The review identifies the
jurisdiction early and adapts the analysis accordingly.

**Primary jurisdictions covered with deep analysis:**

| Jurisdiction        | Key Statutory Framework                                                      |
| ------------------- | ---------------------------------------------------------------------------- |
| **England & Wales** | Housing Act 1988/2004 + Renters' Rights Act 2025 (effective May 2026)        |
| **United States**   | State landlord-tenant codes + Fair Housing Act (42 U.S.C. §§ 3601–3619)      |
| **Australia**       | State Residential Tenancies Acts (NSW, VIC, QLD, WA, SA, TAS) + 2024 reforms |
| **Germany**         | BGB §§ 535–580a + Mietpreisbremse + WoBindG + state housing laws             |

[JURISDICTION-SPECIFIC] For other jurisdictions, apply the general framework and mark
jurisdiction-specific elements as [VERIFY]:

- France: Loi du 6 juillet 1989, Loi ALUR 2014
- Netherlands: Huurrecht (BW Book 7, Title 4), Woningwet
- Canada: Provincial Residential Tenancy Acts (BC, ON, AB, QC, etc.)
- Spain: Ley de Arrendamientos Urbanos (LAU) 1994/2023

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- The user's side (tenant vs. landlord) would flip the risk assessment
- Jurisdiction-specific rules require disambiguation
- The severity of an issue depends on context the user must provide

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

### Step 1: Accept the Lease

Accept the residential lease or tenancy agreement in any of these formats:

- **File**: PDF, DOCX, or image scan of the agreement
- **URL**: Link to a lease in cloud storage or a property management system
- **Pasted text**: Lease text pasted directly into the conversation

If no lease is provided, prompt the user to supply one before proceeding.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask the user these questions. Present them
as a structured set of options where possible:

1. **Which side are you on?**
   - Options: Tenant (reviewing before signing or during tenancy), Landlord (checking
     compliance or pre-letting), Property Manager (portfolio audit), Legal Professional
   - _Why this matters_: What protects a tenant may be a compliance risk for the landlord,
     and vice versa. The analysis, severity classifications, and remediation actions all
     depend on which side the user represents.

2. **Jurisdiction / Property location?**
   - Options: England & Wales, Scotland, Northern Ireland, United States (specify state),
     Australia (specify state/territory), Germany, Other (specify)
   - _Why this matters_: Residential tenancy law is highly jurisdiction-specific. The
     same clause can be perfectly legal in one jurisdiction and void in another. Without
     the jurisdiction, no accurate legal analysis is possible.

3. **Stage of the tenancy?**
   - Options: Pre-signing (considering whether to sign), Active tenancy (reviewing in
     place), Dispute (specific issue has arisen), End of tenancy (deposit/exit dispute)
   - _Why this matters_: Pre-signing analysis focuses on negotiation and walk-away
     decisions. Active tenancy analysis focuses on rights and remedies. Dispute analysis
     focuses on the specific contested clause.

4. **Specific concerns?**
   - Options: Deposit / bond terms, Rent increase provisions, Maintenance / repairs,
     Eviction / notice periods, Pets or occupancy restrictions, Habitability / condition,
     Anti-discrimination compliance, Subletting restrictions, No specific concern — full
     review
   - Allow multiple selections.
   - _Why this matters_: Leads the analysis with what matters most to the user.

5. **Tenancy duration and type (if known)?**
   - Free text or options: Fixed-term (specify months/years), Periodic (month-to-month,
     week-to-week), Unknown from the document
   - _Why this matters_: Fixed-term and periodic tenancies have different rights,
     protections, and termination rules across all jurisdictions.

If the user provides partial context, proceed with stated assumptions and flag them
explicitly: "I'm assuming this is a tenant-side review under English law — let me know
if that is incorrect."

### Step 3: Identify Jurisdiction and Load Legal Framework

1. Read the lease for explicit governing law provisions, property address, or other
   jurisdiction indicators.

   **⟁ CLARIFY** — If any of the following are true, ask before proceeding:
   - **No governing law or property address found**: Ask the user to confirm the
     jurisdiction. Flag the absence of a governing law clause as a RED gap for commercial
     leases (though residential tenancy law generally applies by operation of law).
   - **Property address and governing law conflict**: Confirm which governs the review.
   - **US lease with no state identified**: Ask which state, as laws vary materially
     across states (e.g., California's AB 1482 rent control vs. Texas with no statewide
     rent control).

2. Load the applicable statutory framework from the **Jurisdiction-Specific Analysis**
   section below. Note the mandatory provisions that must be present in every lease
   under that law.

3. Flag the jurisdiction at the top of the output so the user can verify it is correct
   before relying on the analysis.

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** to build a working legal reference for this review.

**Research targets (adapt to the identified jurisdiction):**

```markdown
# Legal Authority Reference — [Lease Identifier]

## Jurisdiction: [identified jurisdiction]

## Date: [date]

### Mandatory Lease Provisions

- [What the applicable statute requires to be in every residential lease]

### Tenant Rights

- [Statutory minimum rights that cannot be contracted away]

### Landlord Obligations

- [Non-waivable obligations imposed by statute]

### Rent Control / Increase Rules

- [Applicable caps, notice requirements, frequency limits]

### Deposit / Bond Rules

- [Maximum amounts, lodgement requirements, return timelines]

### Eviction / Possession Grounds

- [Valid grounds, notice periods, procedure]

### Recent Amendments

- [Any laws in transition (e.g., UK Renters' Rights Act May 2026)]
```

**If legalcode-mcp is not connected:**

- Mark all statutory references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus on structural and commercial risk rather than statutory certainty
- Do not create the authority reference file

### Step 5: Clause-by-Clause Analysis

Read the entire lease before flagging issues — clauses interact (e.g., a broad repair
obligation on the tenant may be partially overridden by an implied habitability warranty,
and a deposit clause may be rendered void by non-compliance with a separate statutory
requirement).

**⟁ CLARIFY** — For long or complex leases (25+ pages, multiple schedules, or
incorporated documents):

- Ask whether to perform a **full review** of all 16 clause categories, or a **priority
  review** focused on the user's stated concerns plus any RED items discovered.
- If the lease incorporates external documents by reference (e.g., house rules, pet
  addendum), ask whether to review those as well.

Cover all 16 clause categories below. For each, assess against statutory requirements
and market standards for the identified jurisdiction.

| #   | Clause Category                       | Depth    | Key Review Points                                                         |
| --- | ------------------------------------- | -------- | ------------------------------------------------------------------------- |
| 1   | Parties and Property Description      | Standard | Identity verification, property address, fixtures included                |
| 2   | Rent and Payment Terms                | Deep     | Amount, due date, payment method, late fees, rent-free periods            |
| 3   | Security Deposit / Bond / Kaution     | Deep     | Amount, lodgement requirement, interest, deduction rules, return timeline |
| 4   | Lease Term and Renewal                | Deep     | Fixed vs. periodic, auto-renewal, notice to vacate, holdover              |
| 5   | Termination and Eviction              | Deep     | Grounds, notice periods, procedure, statutory compliance                  |
| 6   | Rent Increase Provisions              | Deep     | Frequency cap, notice period, amount limits, challenge rights             |
| 7   | Maintenance and Repairs               | Deep     | Landlord vs. tenant allocation, statutory duties, reporting procedure     |
| 8   | Habitability and Minimum Standards    | Deep     | Implied warranty, statutory standards, utilities, safety certificates     |
| 9   | Landlord's Right of Entry             | Standard | Notice period, permitted purposes, emergency access                       |
| 10  | Alterations and Improvements          | Standard | Permission requirements, restoration obligations                          |
| 11  | Occupants, Subletting, and Assignment | Standard | Permitted occupants, subletting restrictions, assignment rights           |
| 12  | Pets and Animals                      | Standard | Permission, restrictions, deposit requirements, service animals           |
| 13  | Utilities and Services                | Standard | Who pays, what is included, meter responsibilities                        |
| 14  | Anti-Discrimination and Fair Housing  | Deep     | Protected classes, prohibited clauses, accessibility                      |
| 15  | Insurance                             | Standard | Contents insurance, liability, landlord building insurance                |
| 16  | Definitions and Boilerplate           | Standard | Entire agreement, severability, notices, amendment procedure              |

### Step 6: Missing Provision Detection

After analyzing clauses present in the lease, check for mandatory or important provisions
that are entirely absent.

For each of the 16 clause categories:

- If the category is absent, flag it and assess whether the absence is a legal gap or
  commercially acceptable
- Classify the absence using the GREEN/YELLOW/RED system

**Common missing provision issues across jurisdictions:**

- No deposit protection or bond lodgement reference (RED in UK/AU)
- No habitability/repair obligations stated (RED in US, implied by law but should be explicit)
- No valid notice period for termination stated (RED — likely violates statute)
- No rent increase notice requirements (YELLOW — statute fills gap but tenant should know rights)
- No entry notice requirements stated (YELLOW — statute fills gap but should be explicit)
- Missing mandatory disclosures (RED — e.g., US lead paint disclosure for pre-1978 property)
- No emergency contact / landlord identity provision (YELLOW to RED depending on jurisdiction)
- Missing fair housing / anti-discrimination statement (YELLOW — statute applies regardless)

**⟁ CLARIFY** — When the severity of a missing provision depends on context:

- "This lease has no reference to deposit protection. Is a deposit being taken? If yes,
  this is a RED compliance gap in [UK/AU]. If no deposit is charged, it is fine."
- "No habitability clause is present. Does the property have known issues? This affects
  whether to treat the absence as YELLOW or RED."

### Step 7: Flag Issues

Classify each issue using the three-tier system in **Issue Severity Classification**
below. For each issue:

- **GREEN**: Note for awareness. No action required.
- **YELLOW**: Generate a specific remediation action, negotiation point, or compliance
  step. Estimate the practical impact of leaving it unresolved.
- **RED**: Explain the specific risk with legal basis, provide the required correction,
  estimate the exposure (financial, legal, or practical), and recommend the next step
  (seek legal advice, refuse to sign, negotiate removal).

**⟁ CLARIFY** — For borderline classifications:

- **YELLOW vs. RED**: When a clause is aggressive but potentially acceptable depending
  on the user's situation: "This deposit deduction clause is broader than market standard.
  For a tenant, should I classify this as RED (refuse to sign without amendment) or YELLOW
  (negotiate)? It depends on whether this is a must-have property."
- **Statutory uncertainty**: When a clause's legality is unclear or depends on the specific
  local implementation, flag it as [VERIFY] rather than asserting illegality.

### Step 8: Generate Remediation Actions

For each YELLOW and RED issue, generate a specific remediation action using the
**Remediation Format** below.

**⟁ CLARIFY** — Before generating remediation actions:

- **Negotiation position**: Is this a lease the user has leverage to negotiate (private
  landlord, pre-signing stage), or a standard-form lease with little room to negotiate
  (large property management company, competitive rental market)?
- **Priority focus**: "I've found [N] items requiring attention. Should I generate
  remediation actions for all of them, or focus on the [X] most critical?"

### Step 9: Overall Assessment

Provide an overall assessment covering:

- **Overall risk / compliance rating**: High-risk / Medium-risk / Low-risk (for tenants);
  Compliant / Partially Compliant / Non-Compliant (for landlords)
- **Top 3 issues**: The most important items to address
- **Statutory compliance summary**: Whether the lease meets minimum legal requirements
  for the identified jurisdiction
- **Recommended next steps**: Specific actions with priority order

### Step 10: Quality Verification

Before delivering the analysis:

1. Run the 5 Citation Quality Gates silently. Revise failures before delivery.
2. For every RED-classified item, run the 3-pass Self-Interrogation. Revise if a pass
   reveals weakness.
3. Assign a Confidence Score to each material clause analysis.
4. Verify completeness: confirm all 16 clause categories have been addressed.
5. Check for jurisdiction bleed: confirm no concepts from the wrong legal system have
   leaked into the analysis.
6. Generate the Glass Box Audit Trail and append it to the output.

---

## Clause Analysis Reference

### 1. Parties and Property Description

**Key elements to review:**

- Full legal names of landlord and all tenants (vs. pseudonyms or initials)
- Property address with sufficient specificity (unit number, postcode/zip)
- Whether fixtures, furnishings, and inclusions are listed (inventory)
- Whether the lease correctly identifies the type of tenancy
- Landlord's contact information and emergency contact (mandatory in some jurisdictions)

**Common issues:**

- Landlord identified only by agent name (tenant cannot serve notices on actual landlord)
- Property description omits unit number (matters for notice service)
- No inventory attached but furnished property claimed (deposit dispute risk)
- No agent's details where agent manages property

[JURISDICTION-SPECIFIC]:

- **England & Wales**: Landlord's name and address must be provided under s.1 Landlord
  and Tenant Act 1985 [VERIFY]. Failure is a criminal offence.
- **Germany**: Landlord and all tenant names must appear; joint and several liability
  applies to all named tenants.
- **Australia**: Managing agent details are mandatory in most states alongside landlord
  details.

### 2. Rent and Payment Terms

**Key elements to review:**

- Monthly (or weekly) rent amount stated clearly
- Due date and payment method specified
- Late payment fee: amount, grace period, and whether the amount is reasonable/lawful
- Accepted payment methods (no requirement to pay in cash only)
- No penalty clauses that exceed actual loss (penalty doctrine)
- Rent-free periods or move-in concessions documented
- Whether rent includes any service charges or utilities

**Common issues:**

- Late fee disproportionate to administrative cost (may be void as penalty)
- Requirement to pay by a single specific method (e.g., cash only) — can be restrictive
- Automatic rent increase tied to index without proper notice (may violate rent-increase rules)
- Unclear whether quoted rent is inclusive or exclusive of utilities or service charges

[JURISDICTION-SPECIFIC]:

- **England & Wales**: Late fees are governed by the Tenant Fees Act 2019. Prohibited
  payments (beyond rent, deposit, and certain permitted payments) are unlawful. Late
  payment fees may only be charged after 14 days of arrears and capped at 3% above Bank
  of England base rate on the outstanding amount [VERIFY].
- **United States**: Late fees are regulated by state law. Many states cap late fees at
  a percentage of monthly rent (e.g., CA: max $25 or 6% of monthly rent [VERIFY]; NY:
  permitted but must be reasonable [VERIFY]). Grace periods vary by state (typically
  3–5 days).
- **Australia**: Landlord cannot charge late fees or interest on overdue rent above the
  prescribed rate (varies by state; typically prohibited or strictly capped). No bond
  (security deposit) may be demanded beyond the statutory maximum.
- **Germany**: Late payment interest defaults to BGB § 288 (5 percentage points above
  the base rate for consumer contracts) [VERIFY]. Additional flat fees in standard-form
  leases may be void under AGB-Recht (BGB §§ 307–309).

### 3. Security Deposit / Bond / Kaution

**Key elements to review:**

- Amount of deposit relative to statutory maximum
- Whether and how the deposit will be protected or lodged
- Timeline for protecting the deposit (if applicable)
- Information provided to tenant about the protection scheme
- Deduction rules: what can and cannot be deducted
- Return timeline after tenancy ends
- Whether interest accrues on the deposit (jurisdiction-specific)
- Disputed deduction procedure

**Common issues:**

- Deposit exceeds statutory maximum (void or creates liability)
- No reference to deposit protection scheme (RED in UK, AU)
- Vague or excessively broad deduction provisions ("tenant is responsible for any and all
  damages" without distinguishing fair wear and tear)
- No timeline for return stated or timeline exceeds statutory maximum
- No procedure for disputing deductions

[JURISDICTION-SPECIFIC]:

- **England & Wales**: Deposits must be protected in a government-approved scheme (TDS,
  DPS, or mydeposits) within 30 days of receipt. Prescribed information must be served
  on the tenant within the same 30-day period (Housing Act 2004, ss. 212–215) [VERIFY].
  Maximum deposit: 5 weeks' rent for annual rent under £50,000; 6 weeks' rent above
  £50,000 (Tenant Fees Act 2019, s.3) [VERIFY]. Non-protection triggers a penalty of
  1–3× the deposit amount plus loss of the right to use Section 21 (now abolished) and
  certain Section 8 grounds.
- **United States**: Security deposit limits and rules are entirely state-law driven.
  Examples: CA: max 1 month's rent (unfurnished; AB 12, effective July 2024) [VERIFY];
  NY: max 1 month's rent (HSTPA 2019) [VERIFY]; TX: no statutory maximum but must be
  returned within 30 days. Many states require deposit held in separate account; some
  (e.g., MA, NJ) require interest to accrue.
- **Australia**: Maximum bond is 4 weeks' rent in most states. Bond must be lodged with
  the relevant state authority (e.g., Rental Bonds Board in NSW, RTA in QLD) within 10
  business days of receipt. Bond cannot increase unless 11 months have elapsed since the
  last increase or tenancy commencement [VERIFY].
- **Germany**: Kaution is capped at 3 months' cold rent (Kaltmiete, excluding utility
  costs) (BGB § 551) [VERIFY]. Must be held in a separately managed account and bear
  interest at the prevailing savings rate. Return timeline: landlord has up to 3–6 months
  after tenancy end to reconcile Betriebskosten before returning balance [VERIFY].

### 4. Lease Term and Renewal

**Key elements to review:**

- Start and end dates (for fixed-term leases)
- Whether fixed-term or periodic tenancy
- Auto-renewal provisions: do they apply, and what notice is required to prevent renewal?
- Holdover provisions: what happens if tenant stays beyond the end date?
- Break clauses (fixed-term leases): conditions, notice period, consequences
- Notice period required to end a periodic tenancy (from both parties)

**Common issues:**

- Auto-renewal with an insufficient or unclear notice window (tenant may be locked in
  without realising)
- Holdover clause with punitive rent escalation (e.g., double rent — may be void)
- Break clause conditions that are practically impossible to satisfy
- Fixed-term lease with no break clause on multi-year agreements (tenant trapped)
- No notice period stated for periodic tenancy termination

[JURISDICTION-SPECIFIC]:

- **England & Wales**: From May 1, 2026 (Renters' Rights Act 2025), all new and existing
  ASTs become periodic assured tenancies. Fixed-term tenancies are abolished for new
  lets. Tenants may terminate by giving 2 months' written notice at any time. Landlord
  can only end the tenancy using the expanded Section 8 grounds (37 grounds) [VERIFY].
  This is a fundamental change — any fixed-term clause in a new post-May 2026 lease is
  void by operation of law.
- **United States**: Lease term structure is governed by state law. Month-to-month
  tenancies typically require 30 days' notice to terminate (tenant or landlord); some
  states (CA, OR, WA) require 60–90 days for landlords after long tenancies [VERIFY].
  Fixed-term leases continue until end date without notice; tenant may owe rent through
  term end on early departure (subject to landlord's duty to mitigate in most states).
- **Australia**: Both fixed-term and periodic tenancies are recognized. 'No-grounds'
  eviction at end of fixed term is abolished in NSW (Oct 2024), QLD (Oct 2024), VIC,
  ACT, and SA [VERIFY]. Landlord must specify a valid reason to end tenancy even at
  expiry. Tenant notice to vacate: typically 14–28 days on periodic tenancy.
- **Germany**: Open-ended (unbefristete) tenancies are the standard and strongly
  protected. Fixed-term (Zeitmietvertrag) is only valid if the landlord can state a
  statutory reason (BGB § 575: personal use planned, demolition/renovation, or letting
  to employee) [VERIFY]. An invalid fixed-term clause converts the lease to open-ended.

### 5. Termination and Eviction

**Key elements to review:**

- Valid grounds for landlord to terminate
- Notice period requirements for each ground
- Whether grounds align with statutory requirements
- Tenant's right to challenge eviction
- Procedure for serving notice (method, address)
- Protection from retaliatory eviction

**Common issues:**

- Lease purports to allow termination "at will" or without stated grounds (RED — void in
  most modern residential tenancy jurisdictions)
- Notice periods shorter than statutory minimums (void — statute prevails)
- No provision for tenant to remedy breach before eviction notice takes effect
- Invalid or insufficient service methods specified (may invalidate notices)
- No mention of tenant's right to challenge possession claim

[JURISDICTION-SPECIFIC]:

- **England & Wales**: Section 21 (no-fault eviction) is abolished from May 1, 2026.
  Any Section 21 clause or no-grounds termination provision in a new lease after that
  date is void. Possession can only be obtained via Section 8 on one of 37 prescribed
  grounds (Grounds 1–8 mandatory; Grounds 9–17 discretionary). Key grounds include:
  Ground 8 (2+ months' rent arrears — mandatory), Ground 14 (anti-social behaviour —
  mandatory), Grounds 1/1A (landlord intent to sell or occupy). Minimum notice periods
  range from 2 weeks (Ground 8) to 4 months (Grounds 1/1A) [VERIFY].
- **United States**: Eviction procedure is entirely state-governed. Grounds generally
  include: non-payment of rent (3–14 days' notice to pay or quit), material lease
  violation (3–30 days' cure notice), and end of lease term. Just Cause eviction laws
  in CA (AB 1482), NY (HSTPA 2019), NJ, OR, and WA require landlords in covered units
  to have qualifying "just cause" even at end of term [VERIFY]. VAWA (Violence Against
  Women Act) prohibits eviction based on domestic violence victim status [VERIFY].
- **Australia**: No-grounds eviction is now abolished in NSW, QLD, VIC, ACT, SA, and
  TAS (WA under review). Valid grounds include: non-payment of rent, damage to property,
  endangering safety, end of social housing eligibility, intent to sell or occupy. Notice
  periods vary by state: typically 14–90 days depending on ground and state [VERIFY].
- **Germany**: Landlord may only terminate for one of three grounds (BGB § 573): breach
  of lease, Eigenbedarf (personal/family use), or prevention of reasonable economic
  use of the property. Eviction can only be enforced via court judgment. Standard notice
  period: 3 months (extending to 6 months after 5 years, 9 months after 8 years of
  tenancy). Tenant can invoke Sozialklausel (BGB § 574) to delay or avert eviction on
  hardship grounds (age, illness, pregnancy, disability) [VERIFY].

### 6. Rent Increase Provisions

**Key elements to review:**

- How rent increases are triggered (notice, index, review)
- Frequency of permitted increases
- Amount limits (percentage cap, index, comparable rent)
- Minimum notice period before increase takes effect
- Tenant's right to challenge the increase
- Whether increases are consistent with applicable rent control laws

**Common issues:**

- Automatic annual rent increases without proper statutory notice (likely void or
  non-enforceable without following statutory process)
- Rent review clause with no cap or benchmark (RED — creates open-ended exposure)
- Notice period for increase shorter than statutory minimum
- CPI or index clause without a floor/ceiling (may violate rent control caps)
- No challenge mechanism stated (tenant should know their rights)

[JURISDICTION-SPECIFIC]:

- **England & Wales**: Rent can only be increased once every 12 months via a Section 13
  Notice (Housing Act 1988, s.13) [VERIFY]. Minimum 2 months' written notice required.
  Tenant can challenge a proposed increase at the First-tier Tribunal (Property Chamber)
  before the increase takes effect. Any contractual rent increase clause that purports
  to operate without a Section 13 Notice is invalid for periodic tenancies post-May 2026.
- **United States**: Rent control applies only in specific states and localities. Statewide
  rent control states (as of 2025): California (AB 1482: max 5% + local CPI or 10%
  whichever is lower, for covered units), Oregon (SB 608: max 7% + CPI for covered units),
  New York (HSTPA 2019: rent stabilization rates set annually for NYC/covered units)
  [VERIFY]. In non-controlled jurisdictions, landlords can raise rent at lease renewal
  to any amount with proper notice (typically 30–60 days). Check whether the specific
  unit is covered before applying rent control analysis.
- **Australia**: As of 2024, rent increases are capped at once per 12 months across all
  states. Minimum 60 days' written notice is required in most states (NSW, VIC, QLD,
  WA, SA, TAS). No absolute dollar cap at state level, but tenants can apply to the
  relevant tribunal to challenge an above-market increase [VERIFY]. Bond cannot be
  increased within 11 months of commencement or last bond increase.
- **Germany**: Two mechanisms for increases on existing tenancies: (a) Ortsübliche
  Vergleichsmiete increase (BGB § 558): rent can be increased to the local comparative
  rent (Mietspiegel), capped at 20% within 3 years (15% in designated strained-housing
  areas — Kappungsgrenze, BGB § 558(3)) [VERIFY]; (b) Staffelmiete or Indexmiete: if
  agreed in writing at outset, preset increases or index-linked changes apply. For new
  leases in areas with strained housing markets (Gebiete mit angespanntem Wohnungsmarkt),
  the Mietpreisbremse applies: initial rent capped at 10% above local comparative rent
  (BGB §§ 556d–556g) [VERIFY]. Tenant must assert Mietpreisbremse claim in writing
  to recover excess rent.

### 7. Maintenance and Repairs

**Key elements to review:**

- Division of responsibility between landlord and tenant
- Whether landlord's obligations meet statutory minimums
- Procedure for reporting defects
- Timeline for landlord to respond and repair
- Tenant's remedy if landlord fails to repair (rent reduction, repair-and-deduct)
- Whether minor repairs obligation on tenant is reasonable or exceeds statutory scope
- Emergency repair procedures

**Common issues:**

- Clause shifts statutory landlord repair obligations onto tenant (void — cannot contract
  out of implied habitability warranty)
- No reporting procedure specified (leaves tenant without clear process)
- No repair response timeline (landlord delay becomes open-ended)
- Cosmetic repair obligations on tenant stated without qualification (may be void —
  see Schönheitsreparaturen in Germany)
- No emergency repair contact or procedure

[JURISDICTION-SPECIFIC]:

- **England & Wales**: Landlord is responsible for structure, exterior, and installations
  for water, gas, electricity, and sanitation under Landlord and Tenant Act 1985, s.11
  (applies to leases under 7 years) [VERIFY]. Cannot be excluded by contract. Tenants
  cannot waive these rights. From 2024, Awaab's Law (via Renters' Rights Act 2025 for
  private sector) may impose timelines for investigating and repairing damp and mould [VERIFY].
- **United States**: The implied warranty of habitability requires landlords to maintain
  the property in safe, habitable condition (recognised in all 50 states following Javins
  v. First National Realty Corp. (D.C. Cir. 1970) and state equivalents) [VERIFY].
  This warranty cannot be waived by lease agreement. Most states allow tenant remedies
  including: repair-and-deduct (deduct repair cost from rent), rent withholding (place
  rent in escrow), and lease termination for material breach of habitability.
- **Australia**: Landlords must provide and maintain premises in a reasonable state of
  cleanliness and repair. Tenants cannot be made responsible for non-minor repairs.
  Specific urgent repair categories (e.g., burst pipe, broken heater, security failure)
  must be addressed within 24–48 hours in most states [VERIFY].
- **Germany**: Landlord's duty to maintain habitability (BGB § 535) is non-waivable. Tenant
  can reduce rent proportionally if a defect materially reduces fitness for use (BGB § 536)
  [VERIFY]. Schönheitsreparaturen (cosmetic repair) clauses are frequently void if they
  impose repairs regardless of actual wear (BGH confirmed rigid cosmetic repair schedules
  void multiple times) [VERIFY]. Tenant has no obligation to make structural or major repairs.

### 8. Habitability and Minimum Standards

**Key elements to review:**

- Whether the property is confirmed as fit for habitation
- Safety certificates referenced (gas, electrical, EPC/energy rating)
- Working smoke and carbon monoxide detectors
- Damp, mould, pest, and structural issues
- Minimum heating provision
- Water supply (hot and cold)
- Compliance with housing health and safety standards

**Common issues:**

- No confirmation of habitability status or outstanding disrepair
- Missing safety certificate references (RED compliance gap in UK; required in many
  US states and AU states)
- No smoke detector or CO detector provision (may be statutory requirement)
- Known disrepair not disclosed (fraudulent or negligent misrepresentation risk)

[JURISDICTION-SPECIFIC]:

- **England & Wales**: Landlord must provide a valid Gas Safety Certificate before
  tenancy starts (Gas Safety (Installation and Use) Regulations 1998) [VERIFY].
  Electrical Installation Condition Report (EICR) required every 5 years (Electrical
  Safety Standards in the Private Rented Sector (England) Regulations 2020) [VERIFY].
  Energy Performance Certificate (EPC) of at least rating E required (minimum F by 2028
  under proposed reform — check current status) [VERIFY]. Smoke alarms on every floor
  and CO alarms in rooms with solid fuel appliances required by law [VERIFY]. Housing
  Health and Safety Rating System (HHSRS) applies.
- **United States**: No federal habitability certificate. State and local housing codes
  define minimum standards (vary widely). Lead paint disclosure required for pre-1978
  housing (42 U.S.C. § 4852d) — landlord must disclose known lead paint hazards and
  provide EPA pamphlet [VERIFY]. Some states require CO detector and smoke detector
  provisions in the lease.
- **Australia**: Properties must meet minimum habitability standards (varies by state).
  NSW requires minimum standards including weatherproofing, functioning plumbing,
  natural light, and adequate ventilation (Fair Trading Residential Tenancy Act 2010
  reforms, Oct 2024) [VERIFY]. QLD requires properties to be free of significant pests,
  have functioning locks, and provide adequate hot water [VERIFY].
- **Germany**: Property must be free of defects that impair fitness for agreed use (BGB
  § 536). Landlord must maintain compliance with public building law and safety standards.
  Energy performance certificate (Energieausweis) must be provided to prospective tenants
  before signing (EnEV / GEG) [VERIFY]. CO and smoke detectors required in most German
  states under state building regulations (Landesbauordnungen) [VERIFY].

### 9. Landlord's Right of Entry

**Key elements to review:**

- Notice period for non-emergency entry
- Permitted purposes for entry (inspection, repairs, showing)
- Emergency access provisions
- Whether notice can be waived or shortened by agreement
- Restriction on excessive or harassing entry attempts

**Common issues:**

- No minimum notice period stated (landlord may claim a right to enter without notice)
- Entry for any purpose at landlord's discretion (too broad)
- No limit on frequency of inspections
- No emergency access limitation (what constitutes an emergency must be defined)
- Failure to mention tenant's right to refuse entry without proper notice

[JURISDICTION-SPECIFIC]:

- **England & Wales**: No specific statutory notice period for entry under the Housing
  Act 1988, but common law quiet enjoyment requires reasonable notice (generally
  accepted as 24 hours) [VERIFY]. Harassment by unlawful entry is a criminal offence
  (Protection from Eviction Act 1977) [VERIFY].
- **United States**: Most states require 24–48 hours' written notice before non-emergency
  entry. CA: 24 hours (Civil Code § 1954) [VERIFY]. NY: no specific statutory period for
  non-emergency but implied covenant of quiet enjoyment applies. Emergency access without
  notice is universally permitted but must be genuine emergency.
- **Australia**: Minimum notice periods vary by state. NSW: 24 hours for general
  inspections (Residential Tenancies Act 2010, s.53) [VERIFY]. QLD: 24 hours [VERIFY].
  VIC: 24 hours [VERIFY]. Landlord entry without valid notice or for excessive purposes
  constitutes breach of quiet enjoyment.
- **Germany**: Landlord has no general right to enter. Entry requires tenant consent
  or statutory justification. Typical notice: 2–3 business days for inspections; immediate
  entry only for genuine emergencies (BGB § 535 Gewährleistung, and tenant's implied duty
  to permit access for necessary repairs) [VERIFY].

### 10. Alterations and Improvements

**Key elements to review:**

- Whether tenant can make any alterations
- Consent requirement (withholding: can it be unreasonably withheld?)
- Restoration obligation at end of tenancy
- Whether decorating or painting is covered
- Smart home / minor modifications provisions

**Common issues:**

- Blanket prohibition on all alterations (may conflict with disability accommodation
  obligations in US/UK)
- Restoration obligation with no qualification for fair wear and tear
- Provisions that could be used to charge tenant for decoration that predates the tenancy

[JURISDICTION-SPECIFIC]:

- **England & Wales**: Tenants may have a right to make certain modifications for
  disability-related reasons (Equality Act 2010) [VERIFY]. The Renters' Rights Act 2025
  introduces a right for tenants to request permission for certain reasonable modifications
  (landlord cannot unreasonably refuse) [VERIFY].
- **United States**: Fair Housing Act requires landlords to permit reasonable modifications
  for disabled tenants at the tenant's expense, with a right to require restoration on
  departure (42 U.S.C. § 3604(f)(3)) [VERIFY].
- **Australia**: Minor modifications (e.g., picture hooks, installing battery smoke
  detectors) are increasingly protected — some states introduced a positive right to
  make minor modifications without landlord consent (VIC from 2021, QLD and NSW 2024) [VERIFY].
- **Germany**: Tenants may make modifications with landlord consent. Consent must not
  be unreasonably withheld for minor improvements. Restoration obligation on departure
  is generally enforceable if included in the lease; however, cosmetic restoration
  clauses tied to rigid schedules are frequently void [VERIFY].

### 11. Occupants, Subletting, and Assignment

**Key elements to review:**

- List of permitted occupants
- Rules about additional occupants (guests vs. permanent residents)
- Subletting: is it permitted? Under what conditions?
- Assignment: can tenant assign the tenancy to another person?
- Short-term letting (Airbnb-type): is it prohibited?

**Common issues:**

- Absolute prohibition on subletting (may be too broad — tenant may have rights to
  sublet in some jurisdictions with landlord consent)
- Overly broad guest restrictions that may discriminate against family members
- No right of assignment on change in personal circumstances
- Short-term letting prohibition buried in boilerplate

[JURISDICTION-SPECIFIC]:

- **England & Wales**: Subletting without consent is generally a breach of AST terms.
  However, landlord consent to sublet must not be unreasonably withheld in some
  circumstances (check specific lease terms) [VERIFY].
- **United States**: Most states require landlord consent for subletting but prohibit
  unreasonable withholding. CA: landlord cannot unreasonably withhold consent to
  subletting (Civil Code § 1995.310) [VERIFY]. Fair Housing Act may limit occupancy
  policies that effectively exclude families.
- **Germany**: Tenant has a qualified right to sublet part of the property to a third
  party with landlord's consent. Landlord may withhold consent only for a substantial
  reason in the person of the subtenant (BGB § 553) [VERIFY]. Full subletting requires
  express agreement.

### 12. Pets and Animals

**Key elements to review:**

- Whether pets are permitted or prohibited
- Types and sizes of permitted pets
- Whether consent can be unreasonably withheld
- Service animals / assistance animals / emotional support animals
- Additional deposits or fees for pets

[JURISDICTION-SPECIFIC]:

- **England & Wales**: The Renters' Rights Act 2025 gives tenants a right to request
  permission to keep a pet. Landlord can only refuse on reasonable grounds. Landlord
  may require tenant to take out pet damage insurance [VERIFY].
- **United States**: Service animals and emotional support animals cannot be refused under
  the Fair Housing Act or ADA even in "no pets" units. A "pet deposit" cannot be charged
  for a service or assistance animal (HUD guidance) [VERIFY]. Regular pets remain at
  landlord's discretion.
- **Australia**: Victoria (2020), Queensland (2024), NSW (2024): tenants have improved
  rights to keep pets; landlord cannot unreasonably refuse, and refusals must specify
  valid reasons [VERIFY]. Standard "no pets" clauses are increasingly void in covered
  jurisdictions.

### 13. Utilities and Services

**Key elements to review:**

- What utilities are included in rent (if any)
- What utilities tenant is responsible for contracting and paying
- Whether the lease requires specific utility providers
- Service charges or strata/building management fees
- Internet and data provisions

[JURISDICTION-SPECIFIC]:

- **Germany (Betriebskosten)**: Landlords may pass through operating costs (Nebenkosten/
  Betriebskosten) to tenants, but only if expressly stated in the lease and only for cost
  items listed in the Betriebskostenverordnung (BetrKV) [VERIFY]. A Betriebskostenpauschale
  (flat-rate) or Betriebskostenvorauszahlung (advance payment with annual reconciliation)
  must be clearly specified. Failure to specify type and amount means ancillary costs
  cannot be charged.
- **England & Wales**: Service charges in purpose-built blocks must comply with the
  Landlord and Tenant Act 1985 consultation requirements. "Admin fees" prohibited under
  Tenant Fees Act 2019 [VERIFY].

### 14. Anti-Discrimination and Fair Housing

**Key elements to review:**

- Any clause that explicitly or implicitly discriminates on protected grounds
- Occupancy policies that effectively exclude families or protected groups
- "No children" or "adults only" clauses
- Clauses that could be used to discriminate against disability, religion, national origin,
  or other protected characteristics
- Advertising language incorporated by reference

**Common illegal clauses (RED in most jurisdictions):**

- "No families with children" or "no children allowed"
- "Must speak English" (can constitute national origin or race discrimination)
- "No Housing Benefit tenants" (UK: source of income discrimination, Equality Act 2010
  s.36 indirect disability discrimination likely) [VERIFY]
- Any clause conditioned on applicant's race, religion, sex, national origin, disability,
  or familial status
- Unequal terms offered to different tenants on protected grounds

[JURISDICTION-SPECIFIC]:

- **United States**: Fair Housing Act (42 U.S.C. §§ 3601–3619) prohibits discrimination
  in housing on grounds of: race, colour, religion, national origin, sex (including gender
  identity and sexual orientation per HUD 2021 guidance), disability, and familial status.
  Many states and cities add: marital status, source of income (vouchers), age, student
  status. Reasonable accommodation for disability must be provided if requested [VERIFY].
- **England & Wales**: Equality Act 2010 — nine protected characteristics (age, disability,
  gender reassignment, marriage/civil partnership, pregnancy/maternity, race, religion/
  belief, sex, sexual orientation). "No DSS" clauses (refusing Housing Benefit recipients)
  are increasingly found to constitute indirect disability discrimination [VERIFY].
- **Germany**: General Equal Treatment Act (AGG) prohibits discrimination in housing
  contracts on grounds of: race/ethnic origin, gender, religion/belief, disability, age,
  sexual identity. Applies to all tenancy agreements [VERIFY].
- **Australia**: Racial Discrimination Act 1975, Sex Discrimination Act 1984, Disability
  Discrimination Act 1992, and state anti-discrimination laws apply. No "no children"
  clauses. Refusal to rent to LGBTQI+ individuals unlawful in most states [VERIFY].

### 15. Insurance

**Key elements to review:**

- Whether tenant is required to hold contents insurance
- Whether landlord has building insurance
- Any mandatory insurance requirements
- Liability insurance obligations

**Common issues:**

- Clause requiring tenant to insure the building structure (this is the landlord's
  obligation)
- Clause holding tenant liable for all damage even if caused by third parties (may be
  excessive)
- Unenforceable waiver of insurance subrogation rights against tenant

### 16. Definitions and Boilerplate

**Key elements to review:**

- Key terms consistently defined and used
- Entire agreement clause (limits what the landlord can claim was "verbally agreed")
- Severability clause (prevents void clause from invalidating entire agreement)
- Notice provisions: who, how, and where to serve notices
- Amendment provisions: any changes must be in writing
- Order of precedence if multiple documents form the agreement
- Jurisdiction clause (courts, dispute resolution)

**Common issues:**

- Notice provisions specify addresses that are out of date or different from the
  property address (service of eviction notices may fail)
- No entire agreement clause (landlord may claim pre-contractual representations)
- No severability clause (one void provision may threaten the whole agreement)
- Dispute resolution clause requires expensive or inaccessible process

---

## Issue Severity Classification

### GREEN — Acceptable / Compliant

The provision aligns with statutory requirements and market standards. No action required.

**Examples:**

- Deposit at statutory maximum or below, with correct protection scheme named
- Notice period for entry equal to or greater than the statutory minimum
- Rent increase mechanism consistent with the applicable rent control rules

**Action**: Note for awareness only.

### YELLOW — Flag / Negotiate / Verify

The provision is sub-optimal, may conflict with statutory requirements depending on
exact facts, or creates material practical risk but is not clearly void or illegal.
Requires attention and likely action before or during the tenancy.

**Examples:**

- Late fee that may exceed the permitted level (exact amount needs to be checked against
  applicable state law)
- Maintenance responsibility clause that pushes borderline items onto tenant
- Automatic rent increase clause without express Section 13 notice requirement (UK)
- No emergency contact specified for landlord/agent

**Action**: Generate a specific remediation action or negotiation point. Provide the
required correction language. Estimate practical impact.

### RED — Non-Compliant / Illegal / Seek Advice

The provision is likely void, illegal, or exposes the user to serious legal or financial
risk. Should not be accepted without removal, correction, or qualified legal advice.

**Examples:**

- Deposit above statutory maximum (void by operation of law)
- No deposit protection scheme reference (statutory breach in UK/AU)
- Section 21 no-fault eviction clause in a new England & Wales lease after May 2026
- "No children" or other discriminatory clause (illegal in all covered jurisdictions)
- Purported waiver of implied warranty of habitability (void in all US states)
- Cosmetc repair (Schönheitsreparaturen) clause using rigid schedule (frequently void
  under German law)
- Rent increase clause with no notice period or frequency limit

**Action**: Identify the specific legal provision making this clause problematic.
Provide the required correction. State whether the clause is void automatically or
only after the tenant exercises a right. Recommend qualified legal advice.

---

## Remediation Format

For each YELLOW and RED issue, generate a remediation action in this format:

```
**Clause**: [Section reference and clause name]
**Issue**: [What is wrong with this provision]
**Severity**: [YELLOW / RED]
**Legal basis**: [Applicable statute, principle, or case — or "General residential
  tenancy standards" — mark [VERIFY] if uncertain]
**Jurisdiction**: [Applicable jurisdiction]
**Tenant action** (if reviewing for tenant):
  [What the tenant should do: negotiate removal, request amendment, seek legal advice,
  withhold signature, report to authority]
**Landlord action** (if reviewing for landlord):
  [What the landlord should do to achieve compliance: amend clause, obtain missing
  certificate, register with authority, serve required notice]
**Suggested replacement language** (if applicable):
  "[Specific alternative clause language]"
**Priority**: [Tier 1 — must resolve / Tier 2 — should resolve / Tier 3 — nice to resolve]
**Confidence**: [Definite / High / Probable / Possible] — [brief rationale]
```

---

## Prioritization Framework

### Tier 1 — Must Resolve (Pre-Signing)

Issues that present a direct legal violation, statutory breach, or risk of serious
financial or personal harm:

- Deposit exceeding statutory maximum or no protection scheme referenced
- Eviction grounds or notice periods that violate statutory minimums
- Discriminatory clauses prohibited by law
- Missing mandatory safety disclosures (lead paint, gas safety, EICR)
- Clauses that purport to waive non-waivable statutory rights (habitability, quiet
  enjoyment, minimum notice periods)
- Post-2026 England & Wales leases with Section 21 or fixed-term clauses

### Tier 2 — Should Resolve (Negotiate Before Signing or Address Promptly)

Issues that create material practical risk or are sub-optimal but not clearly illegal:

- Vague or over-broad maintenance and repair responsibilities
- Rent increase provisions without clear frequency or notice limits
- Absent emergency contact / landlord identity information
- No defined procedure for dispute resolution or deposit return
- Entry notice shorter than statutory guidance (not clearly in breach but sub-optimal)
- Ambiguous holdover provisions

### Tier 3 — Nice to Resolve (Concession Candidates)

Issues that can be improved but are unlikely to cause serious practical harm:

- Preferred governing law or dispute venue (where alternative is acceptable)
- Minor definitional improvements
- Insurance certificate requirements not specified
- Boilerplate refinements
- Purely cosmetic improvements to clarity

**Prioritization strategy**: Resolve Tier 1 items before signing or immediately if in an
active tenancy. Trade Tier 3 asks to secure Tier 2 wins. Never proceed without addressing
Tier 1 items — they represent either statutory breach or serious risk.

---

## Jurisdiction-Specific Analysis Reference

### UK: England & Wales — Renters' Rights Act 2025 Framework

**Effective Date**: The Renters' Rights Act 2025 (Royal Assent: October 27, 2025)
introduces most reforms from **May 1, 2026**. Any lease signed after this date must
comply with the new regime.

**Transition Issues to flag on pre-existing leases:**

- ASTs signed before May 1, 2026 convert to periodic assured tenancies automatically
- Section 21 notices served before May 1, 2026 remain valid only if proceedings are
  issued within 6 months of service or 3 months after May 1, 2026

**Key compliance checklist for England & Wales leases:**

| Obligation                              | Statutory Source             | Timing                    |
| --------------------------------------- | ---------------------------- | ------------------------- |
| Deposit protection (TDS/DPS/mydeposits) | Housing Act 2004             | Within 30 days of receipt |
| Prescribed information served           | Housing Act 2004             | Within 30 days of receipt |
| Gas Safety Certificate provided         | Gas Safety Regs 1998         | Before tenancy starts     |
| EICR provided                           | Electrical Safety Regs 2020  | Before tenancy starts     |
| EPC (min E rating) provided             | MEES Regs 2015               | Before tenancy starts     |
| "How to Rent" guide provided            | Deregulation Act 2015        | Before tenancy starts     |
| Smoke alarm on every storey             | Smoke and CO Alarm Regs 2015 | Throughout                |
| CO alarm in rooms with solid fuel       | Smoke and CO Alarm Regs 2015 | Throughout                |
| Right to Rent check                     | Immigration Act 2014         | Before tenancy starts     |
| No prohibited payments                  | Tenant Fees Act 2019         | Throughout                |

[VERIFY all citations above against authoritative government sources before relying on them]

### US: Implied Warranty of Habitability and Rent Control Matrix

**Habitability minimum standards (applicable in all 50 states):**

- Weatherproof roof and walls
- Hot and cold running water
- Working heat in winter
- Functioning plumbing and sewage
- Working electrical systems
- Free of significant pest/rodent infestation
- Free of serious structural hazards
- Functioning locks on doors and windows
- Smoke detectors (required by law in most states)

**Rent control coverage matrix (key jurisdictions):**

| Jurisdiction  | Coverage                                            | Maximum Increase              | Notes                        |
| ------------- | --------------------------------------------------- | ----------------------------- | ---------------------------- |
| California    | AB 1482: buildings 15+ years old, not single-family | 5% + local CPI or 10% (lower) | Local cities may be stricter |
| New York      | HSTPA 2019: most NYC rental units                   | Rate set by RGB annually      | Complex exemptions apply     |
| Oregon        | SB 608: buildings 15+ years old                     | 7% + CPI or 10%               | Statewide law                |
| Washington    | Local (Seattle, etc.)                               | Varies                        | No statewide law             |
| Texas, FL, AZ | No rent control                                     | None                          | Prohibited at state level    |

[VERIFY all jurisdiction-specific details before relying on them]

**Federal protections applicable to all US residential leases:**

- Fair Housing Act (42 U.S.C. §§ 3601–3619) — protected classes
- VAWA protections (42 U.S.C. § 14043e-11) — domestic violence victim protections
- Lead paint disclosure (42 U.S.C. § 4852d) — pre-1978 housing
- Americans with Disabilities Act (ADA) — reasonable modifications/accommodations

### Australia: State Residential Tenancy Acts — 2024 Reform Summary

**Key reforms effective 2024 (confirm current status per state):**

| State | 12-Month Rent Increase Cap | No-Grounds Eviction Abolished              | Bond Authority                                   |
| ----- | -------------------------- | ------------------------------------------ | ------------------------------------------------ |
| NSW   | ✅ (Oct 31, 2024)          | ✅ (Oct 31, 2024)                          | NSW Fair Trading                                 |
| QLD   | ✅ (Oct 1, 2024)           | ✅ (Oct 1, 2024)                           | RTA Queensland                                   |
| VIC   | ✅ (existing)              | ✅ (existing)                              | RTBA Victoria                                    |
| WA    | ✅ (Jul 2024)              | Under review                               | Bond Administrator WA                            |
| SA    | ✅ (existing)              | ✅ (Jul 2024)                              | Consumer Business Services SA                    |
| TAS   | ✅ (existing)              | ✅ (existing)                              | Consumer, Building and Occupational Services TAS |
| ACT   | ✅ (existing)              | ✅ (existing)                              | ACT Revenue Office                               |
| NT    | Varies                     | No (landlord can terminate at end of term) | NT Department of Attorney-General                |

[VERIFY all state-specific details before relying on them]

### Germany: BGB Mietrecht Framework

**Key structural rules for German residential lease review:**

| Aspect                  | Rule                                                                       | BGB Reference       |
| ----------------------- | -------------------------------------------------------------------------- | ------------------- |
| Lease formation         | Written form recommended; oral valid but unenforceable for >1yr            | § 550               |
| Fixed term              | Only valid if statutory reason stated (personal use, demolition, employee) | § 575               |
| Rent brake (new leases) | Max 10% above Mietspiegel in designated areas                              | §§ 556d–556g        |
| Increase cap            | 20% within 3 years (15% in designated areas)                               | § 558(3)            |
| Kaution (deposit)       | Max 3 months Kaltmiete; held separately with interest                      | § 551               |
| Entry                   | No general right; requires tenant consent except genuine emergency         | § 535 ff.           |
| Termination             | Must state Eigenbedarf, economic use, or breach                            | § 573               |
| Notice periods          | 3 months (0–5 yrs), 6 months (5–8 yrs), 9 months (8+ yrs)                  | § 573c              |
| Hardship defense        | Tenant can invoke Sozialklausel against justified eviction                 | § 574               |
| Cosmetic repairs        | Rigid schedule clauses frequently void (BGH)                               | § 307               |
| Operating costs         | Must be expressly listed; reconciliation annually                          | §§ 556–556c, BetrKV |
| Property sale           | Kauf bricht nicht Miete — lease survives property sale                     | § 566               |

[VERIFY all citations before relying on them]

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                                                   | Fail Action                                                 |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Source**     | Every statutory or legal claim cites a specific act, section, regulation, or established principle                                                                     | Add citation or mark "[UNVERIFIED — verify before relying]" |
| **Format**     | All citations follow a consistent, recognisable format for the jurisdiction                                                                                            | Fix format                                                  |
| **Currency**   | Every cited provision checked for amendments, repeal, or transition (especially UK Renters' Rights Act 2025, AU 2024 reforms)                                          | Flag "[CHECK CURRENCY — may have been amended]"             |
| **Domain**     | Analysis stays within the jurisdiction's governing law. No concepts imported from another legal system (e.g., no US "work-for-hire" analysis in a German lease review) | Remove or flag jurisdictional bleed                         |
| **Confidence** | Uncertainty explicitly stated. If unsure of a legal position, say so clearly                                                                                           | Add confidence qualifier or [VERIFY] tag                    |

### Self-Interrogation for RED Items

For any clause classified as RED, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity:**

- Does the risk assessment follow logically from the cited statute or principle?
- Would a court in the identified jurisdiction actually hold this clause void or illegal?
- What is the counterparty's strongest argument that the clause is valid?

**Pass 2 — Completeness:**

- Have all relevant statutes, regulations, and case law been considered?
- Are there recent legislative changes (e.g., UK Renters' Rights Act 2025 transition,
  AU 2024 state reforms) that affect the analysis?
- Are there regulatory or local ordinance dimensions not yet addressed?

**Pass 3 — Challenge:**

- What is the strongest argument that this provision is acceptable?
- Under what circumstances might a reasonable tenant or landlord accept this clause?
- Is the RED classification proportionate, or is this actually YELLOW with appropriate
  mitigation?

Mark the audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

Assign a confidence level to each material clause analysis:

| Level        | Range     | Meaning                                          | Action                                                |
| ------------ | --------- | ------------------------------------------------ | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, clear statute, no ambiguity         | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments, reasonable minds could differ    | State with reasoning and contra-indicators            |
| **Possible** | 0.40–0.59 | Genuinely uncertain, competing authorities       | Flag for professional review with both sides          |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                          | Do not assert; flag "[UNCERTAIN — seek legal advice]" |

---

## Glass Box Audit Trail

Every lease review output MUST include a Glass Box audit section at the end.

```yaml
glass_box:
  skill_name: "legalcode-residential-lease-review"
  lease_identifier: "[property address or file name]"
  review_date: "[date]"
  user_side: "[Tenant / Landlord / Property Manager / Legal Professional]"
  tenancy_stage: "[Pre-signing / Active / Dispute / End of Tenancy]"
  jurisdiction: "[Identified jurisdiction]"
  jurisdiction_confidence: "[HIGH / MEDIUM / LOW — rationale]"
  tenancy_type: "[Fixed-term / Periodic / Unknown]"
  clauses_reviewed: 16
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  issues_found:
    RED: "[number]"
    YELLOW: "[number]"
    GREEN: "[number]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  jurisdiction_transition_risk: "[YES — Renters' Rights Act May 2026 / YES — AU 2024 reforms / NO]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified legal review"
```

---

## Multi-Stakeholder Mapping

For every residential lease review, identify all affected parties — not just the two
signing parties:

| Stakeholder                         | Role            | Affected Clauses          | Impact            | Action Required                             |
| ----------------------------------- | --------------- | ------------------------- | ----------------- | ------------------------------------------- |
| Tenant(s)                           | Primary party   | All                       | Direct            | Review, negotiate, sign                     |
| Landlord                            | Primary party   | All                       | Direct            | Compliance, sign                            |
| Managing Agent                      | Agent           | Entry, notices, repairs   | Operational       | Ensure they understand obligations          |
| Co-tenants / Joint tenants          | Party           | Rent, liability           | Joint and several | All must sign; all bound                    |
| Guarantor                           | Secondary party | Rent, damage, duration    | Financial         | Separate guaranty review advised            |
| Local authority / Housing authority | Regulator       | Habitability, licensing   | Compliance        | HMO licence, selective licensing checks     |
| Previous tenant                     | Third party     | Deposit, condition report | Historical        | Condition report from previous tenant       |
| Mortgage lender                     | Third party     | Subletting, assignment    | Consents          | Buy-to-let mortgage may restrict subletting |

---

## Anti-Patterns

What NOT to do in residential lease review:

1. **Applying the wrong jurisdiction's law** — Residential tenancy law is hyper-local.
   A clause that is void under English law (e.g., a Section 21 clause post-May 2026) may
   be perfectly legal in Texas. Never apply one jurisdiction's tenant-protection framework
   to a lease governed by another jurisdiction without verifying the correct rules.

2. **Treating void clauses as enforceable** — In residential tenancy, many statutory
   protections are non-waivable. A clause that purports to exclude the implied warranty
   of habitability (US), the landlord's repair obligations under s.11 LTA 1985 (UK), or
   the minimum notice periods under BGB § 573c (DE) is void by operation of law — but
   do not simply call it "unenforceable" without citing the specific statutory provision.

3. **Missing the transition risk** — Several major jurisdictions are in or approaching a
   statutory transition (UK Renters' Rights Act May 2026; AU state-by-state 2024 reforms).
   Failing to flag that a lease currently valid may become non-compliant on a specific date
   is a material omission.

4. **Overlooking missing provisions** — Focusing only on what is in the lease and ignoring
   what is absent. Missing mandatory disclosures (lead paint in the US), missing deposit
   protection reference (UK/AU), and missing safety certificates are as important as
   problematic clauses that are present.

5. **Ignoring fair housing / anti-discrimination** — Discriminatory clauses are sometimes
   buried in guest, occupancy, or pet policies rather than explicitly stated. "No more
   than 2 persons per bedroom" can be a coded family-status restriction. "Must be employed"
   can exclude disability income recipients. Screen all clauses for disparate impact.

6. **Confusing Kaltmiete and Warmmiete in German leases** — German leases distinguish
   cold rent (Kaltmiete, excluding utilities) from warm rent (Warmmiete, including Nebenkosten).
   Kaution, rent control caps, and increase rules all reference Kaltmiete. Applying
   calculations to Warmmiete produces incorrect results.

7. **Failing to flag cosmetic repair clauses (Schönheitsreparaturen) in German leases**
   — German landlords routinely include cosmetic repair schedules that are frequently void
   under BGH case law if they impose obligations regardless of actual condition. This is
   one of the most common exploitative clauses in German residential leases.

8. **Treating deposit rules as uniform** — Deposit maximums, protection requirements,
   lodgement authorities, and return timelines are radically different across jurisdictions
   and even within US states. Never apply one state's deposit rule to another.

9. **Assuming rent control applies (or does not apply) without checking coverage** — US
   rent control is unit-specific, not just city-specific. CA's AB 1482 excludes single-
   family homes with proper notice, condos sold separately, and units built within 15 years.
   NYC rent stabilization has complex coverage rules. Always verify whether the specific
   unit is covered before opining on rent control.

10. **Ignoring the interplay between lease terms and statutory defaults** — In many
    jurisdictions, statute fills gaps where the lease is silent (e.g., implied warranty of
    habitability in the US applies regardless of the lease; BGB § 535 duties apply in
    Germany regardless of what the lease says). Silence is not the same as no right. Flag
    when an absent clause is filled by statute and when it creates an actual gap.

11. **Missing service animal / assistance animal requirements (US)** — The failure to
    flag a "no pets" clause that does not contain a service/assistance animal carve-out
    is a Fair Housing Act compliance error. This is one of HUD's most-enforced provisions.

12. **Reviewing for one side while unconsciously protecting the other** — The analysis must
    be squarely from the user's stated side. What is a risk for a tenant (e.g., a broad
    deposit deduction clause) is a protection for the landlord. Confirm the side before
    every classification decision.

13. **Stating a clause is void without explaining the consequence** — Saying "this clause
    is void" is incomplete. Explain: (a) what law makes it void, (b) what replaces it
    (statutory default), and (c) whether the landlord faces any additional sanction
    (e.g., UK deposit non-protection triggers 1–3× penalty, not just return of deposit).

14. **Ignoring the "How to Rent" guide and prescribed information (UK)** — These are not
    part of the lease itself, but their non-service has legal consequences (restriction on
    using Section 21 under the old regime; restriction on certain Section 8 grounds under
    the new regime). Always ask whether these were provided.

15. **Assuming the tenancy type without checking the legislation** — "Fixed-term AST"
    language in a UK lease signed after May 1, 2026, is not legally operative. The tenancy
    is a periodic assured tenancy by operation of law regardless of what the document says.
    Do not analyse the lease as a fixed-term AST without first confirming the date.

16. **Underweighting the Sozialklausel (Germany)** — Many German lease reviews focus on
    Eigenbedarf eviction grounds without explaining that even a valid Eigenbedarf can be
    blocked or delayed by the Sozialklausel if the tenant can demonstrate exceptional
    personal hardship. This is a significant tenant protection that is frequently missed.

---

## Writing Standards

Apply plain-language discipline to all output:

**For remediation actions (shared with counterparty or for filing with authority):**

- Plain language. No jargon.
- Active voice: "The landlord must register the deposit within 30 days" not "The deposit
  is required to be registered."
- Short sentences. One point per sentence.
- Name the actor: "The tenant should..." not "It is recommended that..."
- Specific, not vague: cite the relevant provision and state the exact correction required.

**For internal analysis:**

- Same plain-language standards.
- May include more technical legal analysis.
- Confidence qualifiers throughout.
- Glass Box audit trail appended.

**Quality gates before delivery:**

1. Can a non-lawyer tenant or landlord understand the key findings section?
2. Is every RED-classified issue backed by a specific citation (or clearly marked [VERIFY])?
3. Is every remediation action specific enough to act on immediately?
4. Are any phrases vague, hedging, or ambiguous? If yes, fix.
5. Has jurisdiction bleed been checked and removed?
6. Have all UK Renters' Rights Act 2025 transition issues been addressed where relevant?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for jurisdiction-relevant statutes, regulations, and recent case law
- Focus searches on: current deposit protection rules, current rent control limits, current
  eviction grounds, and mandatory disclosure requirements for the identified jurisdiction
- Save the most relevant results to a local temp file (`/tmp/legalcode-lease-authority.md`)
- Reference verified authority from the temp file throughout the clause analysis
- For RED items, search for case law supporting or challenging the classification
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail
- Check whether UK Renters' Rights Act 2025 implementation dates have changed

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus the analysis on structural issues and well-established general principles
- Add a prominent notice: "Statutory references in this review require independent
  verification before relying on them. Residential tenancy law changes frequently."

---

## Localization Notes

This skill is jurisdiction-aware with deep coverage of UK, US, AU, and DE. When reviewing
a lease from another jurisdiction:

1. Use the general framework (16 clause categories, GREEN/YELLOW/RED classification,
   remediation format) — these apply universally.
2. Apply [JURISDICTION-SPECIFIC] markers for any analysis that depends on local law.
3. Use legalcode-mcp to research the specific jurisdiction's mandatory provisions.
4. Note local language requirements — some jurisdictions (e.g., QC, France) require
   leases to be in the local official language.
5. Flag any local registration, notarization, or filing requirements.
6. Check whether the jurisdiction uses common law (implied warranty of habitability,
   quiet enjoyment) or civil law (statutory codification — BGB, French Code Civil)
   principles — this affects whether gaps in the lease are filled by statute or by
   common law implication.

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Residential Lease Review Summary

**Property**: [address]
**Reviewing for**: [Tenant / Landlord / Property Manager]
**Jurisdiction**: [identified jurisdiction — flag if uncertain]
**Tenancy type**: [Fixed-term / Periodic / Unknown]
**Stage**: [Pre-signing / Active / Dispute / End of Tenancy]
**Review date**: [date]
**Note**: [If UK post-May 2026 or AU 2024 transition flags apply]

---

## Overall Assessment

**Risk rating** (tenant): [High-Risk / Medium-Risk / Low-Risk]
**Compliance rating** (landlord): [Compliant / Partially Compliant / Non-Compliant]
**Summary**: [2–3 sentence plain-language summary of the lease]

---

## Key Findings

[Top 3–5 issues with severity flags (RED/YELLOW) and one-line summaries]

---

## Missing Provisions

[List any of the 16 clause categories absent from the lease, with severity assessment]

---

## Clause-by-Clause Analysis

### [Clause Category] — [GREEN / YELLOW / RED] | Confidence: [level]

**Lease says**: [summary of the provision]
**Statutory / market standard**: [what is required or expected]
**Issue**: [description of the problem, if any]
**Practical impact**: [what this means for the user]
**Remediation** (if YELLOW or RED): [specific action, replacement language, or advice]

[Repeat for each of the 16 clause categories]

---

## Jurisdiction Compliance Checklist

[List of mandatory items for the identified jurisdiction — check/flag against lease]

---

## Prioritized Action List

**Tier 1 — Must Resolve**: [list with brief rationale for each]
**Tier 2 — Should Resolve**: [list]
**Tier 3 — Nice to Resolve**: [list]

**Recommended sequence**: [order in which to raise issues if negotiating]

---

## Stakeholder Notes

[Any relevant multi-stakeholder considerations — guarantor, co-tenants, managing agent]

---

## Next Steps

[Specific actions with suggested owner and priority — e.g., "Request deposit
protection certificate from landlord before paying deposit (Tier 1)"]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis created via Mode A (new skill
creation) using the legalcode-skill-enhancement methodology. Legal research conducted via
WebSearch covering UK Renters' Rights Act 2025 (Royal Assent Oct 27, 2025), US Fair Housing
Act and state rent control laws (CA AB 1482, NY HSTPA 2019, OR SB 608), Australian state
residential tenancy reforms (NSW Oct 2024, QLD Oct 2024 and equivalents), and German BGB
§§ 535–580a Mietrecht framework including Mietpreisbremse and Kündigungsschutz. Reference
standard: `skills/general/contracts/legalcode-contract-review/SKILL.md`.

All statutory citations carry hallucination risk and are marked [VERIFY] — verify against
authoritative government and legal sources before relying on them in any legal proceeding
or advice.
