---
name: legalcode-au-fair-work-compliance
description: Assess compliance with the Fair Work Act 2009 (Cth) — including the 11 National Employment
  Standards (NES), modern award coverage and minimum entitlements, enterprise agreement obligations, general
  protections and adverse action exposure, sham contracting risk, termination and unfair dismissal procedural
  fairness, record-keeping obligations, and FWO enforcement risk profiling. Use when auditing employment
  agreements, award compliance, wage and hour practices, casual conversion eligibility, flexible work
  policies, termination procedures, contractor classification, or any workplace practice for Fair Work
  Act compliance.
metadata:
  jurisdiction: Australia
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Assess compliance with the Fair Work Act 2009 (Cth) — including the 11 National Employment Standards (NES), modern award coverage and minimum entitlements, enterprise agreement obligations, general protections and adverse action exposure, sham contracting risk, termination and unfair dismissal procedural fairness, record-keeping obligations, and FWO enforcement risk profiling. Fully covers the Closing Loopholes Acts (2023–2024): right to disconnect, new casual definition, fixed-term contract limits, wage theft criminalisation (effective 1 January 2025), labour hire same-job-same-pay orders, employee-like platform worker standards, and flexible work request reforms. Generates COMPLIANT / PARTIAL / NON-COMPLIANT findings with CRITICAL / HIGH / MEDIUM / LOW risk tiers, clause-level remediation language with revised drafts, penalty exposure estimates, and a prioritised remediation roadmap. Use when auditing employment agreements, award compliance, wage and hour practices, casual conversion eligibility, flexible work policies, termination procedures, contractor classification, or any workplace practice for Fair Work Act compliance. Jurisdiction: Australia (national — all states and territories). Enforced by Fair Work Ombudsman (FWO) and Fair Work Commission (FWC). Supports employer, employee, and adviser perspectives.


# Legalcode — Australian Fair Work Act Compliance Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted Fair Work Act 2009
> compliance assessment. It does not constitute legal advice. All outputs require review
> by an Australian-qualified employment lawyer or industrial relations practitioner before
> reliance, particularly in relation to penalty exposure, modern award classification,
> sham contracting determinations, and FWO enforcement risk. The Fair Work Act 2009 (Cth)
> and its supporting instruments are frequently amended — the Closing Loopholes Acts
> (2023–2024) introduced substantial reforms with staggered commencement dates. Verify
> current applicability of all statutory provisions, modern award rates, penalty thresholds,
> and case law against authoritative sources (Federal Register of Legislation, FWC website,
> Fair Work Ombudsman) before acting. Section numbers, penalty amounts, and case citations
> referenced from memory carry hallucination risk — mark all such references with [VERIFY]
> unless independently confirmed.

---

## Purpose and Scope

This skill assesses employment arrangements, workplace policies, and business practices
for compliance with the Fair Work Act 2009 (Cth) and its subordinate instruments.

**Covers:**

- Employment status: employee vs. independent contractor (post-_Personnel Contracting_ [2022] HCA 1 [VERIFY])
- Modern award coverage and minimum classification rates
- All 11 National Employment Standards (NES), including the Closing Loopholes additions
- Enterprise agreement currency, BOOT compliance, and post-approval obligations
- General protections: adverse action, workplace rights, coercion, and misrepresentation
- Sham contracting detection (FWA ss 357–359 [VERIFY])
- Unfair dismissal: procedural fairness, valid reason, Small Business Fair Dismissal Code
- Genuine redundancy: redeployment obligation and consultation requirements
- Closing Loopholes reforms: right to disconnect, new casual definition, fixed-term contract limits, wage theft criminalisation, labour hire orders, employee-like worker standards
- Record-keeping and payslip obligations (Part 3-6, FW Regulations reg 3.33–3.46 [VERIFY])
- FWO enforcement risk profiling: civil penalties, compliance notices, undertakings
- COMPLIANT / PARTIAL / NON-COMPLIANT classification with CRITICAL / HIGH / MEDIUM / LOW risk tiers
- Clause-level remediation with revised draft language and fallback positions
- Compliance program gap assessment and remediation roadmap

**Does not:**

- Provide legal advice or replace qualified employment counsel
- Cover state-specific long service leave legislation in detail (preserved under s 113; state laws vary [VERIFY])
- Cover the Work Health and Safety Act 2011 (Cth) or state WHS equivalents
- Cover the Australian Privacy Act 1988 (Cth) — see `australia-privacy-act-ndb-breach-notification-operations`
- Cover the Migration Act 1958 (Cth) work rights or visa conditions
- Cover the Superannuation Guarantee (Administration) Act 1992 (Cth) in depth (though NES superannuation entitlement is assessed)
- Cover the National Disability Insurance Scheme or aged care sector-specific industrial instruments in detail

**Related skills:**

- `legalcode-au-consumer-law-compliance` — ACL and consumer-facing practice
- `legalcode-franchise-agreement-review-au` — Franchising Code + ACL for franchise agreements
- `australia-privacy-act-ndb-breach-notification-operations` — Privacy Act NDB compliance
- `legalcode-employment-agreement-review` — General (jurisdiction-agnostic) employment contract review

---

## Jurisdiction and Governing Law

### The National System

The Fair Work Act 2009 (Cth) ("FWA" or "the Act") applies to **national system employers
and employees**. This covers most private-sector employers across Australia due to the
corporations power (Constitution s 51(xx)) and referrals from all states except (in part)
Western Australia.

**Covered by the national system:**

- Constitutional corporations (Pty Ltd, Ltd, incorporated associations)
- Commonwealth government employers
- Employers in the territories
- Employers in Victoria, South Australia, Tasmania, ACT, NT (by reference)
- In Queensland, New South Wales: most private sector employers

**Not fully covered (state systems):**

- Western Australia (state government employers, some unincorporated entities)
- Some state/territory government employers
- Sole traders and partnerships that are not constitutional corporations (in some states)

**Intersection with state laws:**

- Long service leave: state/territory laws preserved (s 113)
- Workplace health and safety: parallel systems — national WHS Act and state equivalents
- Workers' compensation: state/territory schemes
- Anti-discrimination: federal (FWA Part 3-1) + state laws may both apply

**Key regulators:**

- **Fair Work Commission (FWC)**: Independent tribunal — makes, varies, and terminates
  modern awards; approves enterprise agreements; resolves unfair dismissal and general
  protections disputes; handles anti-bullying and right to disconnect applications
- **Fair Work Ombudsman (FWO)**: Independent statutory office — investigates, enforces,
  issues compliance notices and infringement notices; brings civil penalty proceedings
- **Federal Circuit and Family Court of Australia (FCFCA)** and **Federal Court of Australia**:
  civil remedy proceedings

---

## Closing Loopholes Acts — Key Reforms (2023–2024)

The following reforms materially affect compliance obligations. Effective dates are
staggered — verify current commencement status against Federal Register of Legislation.

| Reform                                 | Act                            | Effective Date                                                            | Key Obligation                                                                                                                                                                                          |
| -------------------------------------- | ------------------------------ | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Wage theft criminalisation**         | Closing Loopholes No. 1 (2023) | 1 January 2025                                                            | Intentional underpayment is a criminal offence. Penalties: individual up to 10 years imprisonment / $1.565M [VERIFY]; body corporate up to $7.825M [VERIFY]                                             |
| **Right to disconnect**                | Closing Loopholes No. 2 (2024) | 26 Aug 2024 (large employers); 26 Aug 2025 (small business <15 employees) | Employees may refuse contact outside work hours unless refusal is unreasonable. FWC jurisdiction to issue stop orders. New FWA Part 2-9 Division 12 [VERIFY]                                            |
| **New casual definition**              | Closing Loopholes No. 2 (2024) | 26 August 2024                                                            | Casual employee: no firm advance commitment to continuing and indefinite work; assessed by work pattern over 12 months (not just contractual terms). Replaces _WorkPac v Rossato_ codification [VERIFY] |
| **Casual conversion — new pathway**    | Closing Loopholes No. 2 (2024) | 26 August 2024                                                            | After 6 months' employment (12 for small business), employee can notify FWC if employer disputes conversion. Reformed s 66A–66MA [VERIFY]                                                               |
| **Fixed-term contract limits**         | Closing Loopholes No. 1 (2023) | 6 December 2023                                                           | New ss 333M–333R [VERIFY]: maximum 2-year duration; maximum 2 consecutive contracts for same role. Information statement required. Exceptions apply                                                     |
| **Labour hire — same job same pay**    | Closing Loopholes No. 1 (2023) | 1 November 2024                                                           | Regulated labour hire arrangement orders: FWC may order that labour hire workers receive the protected rate of pay applicable to host employer's enterprise agreement                                   |
| **Employee-like workers (gig)**        | Closing Loopholes No. 1 (2023) | 26 August 2024                                                            | FWC can make minimum standards orders and collective agreements for "employee-like" platform workers; new Part 3A-1 [VERIFY]                                                                            |
| **Sham contracting — amended defence** | Closing Loopholes No. 2 (2024) | 26 February 2024                                                          | Old defence: employer "did not know" it was employment. New defence: employer "reasonably believed" it was a services contract — lower fault threshold for prosecution [VERIFY]                         |
| **Independent contractor definition**  | Closing Loopholes No. 2 (2024) | 26 August 2024                                                            | High-income earners (above contractor high income threshold [VERIFY]) may opt-out of employee characterisation provisions. New objection procedure                                                      |
| **Superannuation as NES**              | Closing Loopholes No. 1 (2023) | 1 January 2024                                                            | Super contributions added as the 11th NES under s 124A [VERIFY]. FWO can now pursue unpaid super claims alongside other FWA claims                                                                      |
| **Workplace delegates rights**         | Closing Loopholes No. 1 (2023) | 1 July 2024                                                               | New protected rights for union workplace delegates: reasonable communication, access to facilities, paid training leave [VERIFY]                                                                        |
| **Flexible work — FWC arbitration**    | Closing Loopholes No. 2 (2024) | 6 June 2023 (in part)                                                     | Employee can apply to FWC if employer refuses flexible work or fails to respond within 21 days. FWC can arbitrate [VERIFY]                                                                              |

> **[VERIFY]** All section numbers, effective dates, and penalty amounts above require
> independent verification against the Federal Register of Legislation and FWC website.
> These instruments have complex commencement provisions.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. The workflow pauses
to ask when:

- The answer would change the scope or direction of the assessment
- Different industry awards, employee types, or employer sizes apply different rules
- A pending FWO investigation or FWC application affects risk profiling
- Multiple valid assessment approaches exist

Use the **⟁ CLARIFY** pattern: structured options with descriptions. Skip questions the
user has already answered.

---

## Workflow

### Step 1: Accept the Input

Accept input in any of these formats:

- **Employment contracts** (PDFs, DOCXs, or pasted text)
- **Workplace policies**: leave policies, flexible work procedures, dismissal procedures
- **Termination documentation**: letters, performance warnings, redundancy notices
- **Payslips and wage records**: for underpayment/award compliance audits
- **Enterprise agreement** or modern award extracts
- **Narrative description**: "We engage 12 casual food service workers; here is how we rostered them…"
- **Specific scenario**: "We want to terminate a long-term casual employee — assess the risks"

If no document is provided, prompt the user to supply one or describe the scenario.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask these questions (skip any already answered):

1. **Assessment scope**: What should this review focus on?
   - Options: Full Fair Work compliance audit | Employment agreement terms only |
     Wages and award rate compliance | Termination / unfair dismissal procedures |
     Casual employee obligations | Contractor classification risk | Right to disconnect
     readiness | Fixed-term contract limits | FWC application preparation | Other
   - _Why_: Different scopes engage different pillars. A wages audit requires payroll
     records; a termination review requires correspondence.

2. **Industry and sector**: What industry does this employer operate in?
   - Options: Retail | Hospitality and tourism | Construction | Professional services |
     Healthcare and social assistance | Education | Manufacturing | Transport and logistics |
     Mining | Agricultural, horticultural and forestry | Other
   - _Why_: Modern award coverage is determined by industry and classification. The
     applicable award affects minimum rates, penalty rates, allowances, and overtime.
     FWO enforcement priorities also differ by sector.

3. **Employer size**: How many employees does this employer have?
   - Options: Small business (<15 employees) | Medium (15–99) | Large (100+)
   - _Why_: Small Business Fair Dismissal Code applies to small businesses. Right to
     disconnect commencement date differs (26 August 2024 vs. 26 August 2025 for small
     business). Casual conversion notice periods differ.

4. **Perspective**: Who are you representing?
   - Options: Employer / Employer's legal adviser | Employee / Employee's representative |
     Independent adviser or HR professional
   - _Why_: The risk profile, remediation recommendations, and drafting tone differ
     by perspective. An employer needs to know corrective steps; an employee needs to
     know their rights and claim options.

5. **Workforce composition**: What types of workers are involved?
   - Options: Full-time employees | Part-time employees | Casual employees |
     Independent contractors | Labour hire workers | Platform/gig workers | Mixed
   - _Why_: NES application, casual definition, and sham contracting exposure all
     depend on workforce classification.

6. **Known concerns**: Are there existing complaints, claims, or investigations?
   - Options: FWO complaint filed or expected | FWC application filed or expected |
     Internal grievance in progress | Underpayment suspected or identified |
     No known issues — proactive audit | Other
   - _Why_: Known proceedings accelerate risk tier and require prioritised analysis.

7. **Modern award or enterprise agreement**: Do you know which modern award or enterprise
   agreement applies?
   - Options: Yes — specify name | I believe it is [award name] but need confirmation |
     No — need determination | Enterprise agreement applies (specify if known)
   - _Why_: Award identification is the foundation of wages and classification assessment.
     If unknown, Step 4 will identify it.

If context is partial, proceed with stated assumptions and flag them explicitly.

### Step 3: Load Relevant Instruments

Identify the applicable industrial instruments:

**Modern award determination:**

1. Check if the employer is a national system employer (see Jurisdiction section above)
2. Identify the applicable modern award from the FWC modern award list:
   - Retail Industry Award, General Retail Industry Award, Hospitality Award,
     Building and Construction General On-Site Award, Professional Employees Award,
     Clerks — Private Sector Award, Restaurant Industry Award, etc.
3. If the classification is unclear, apply the **industry/occupation hierarchy**: industry
   awards take precedence; occupation awards cover workers not covered by industry awards
4. Confirm the most recent FWC Annual Wage Review determination (typically takes effect
   1 July each year) for current minimum rates

**Enterprise agreement check:**

- Is there a registered enterprise agreement? Is it current (not expired)?
- Does it pass the **Better Off Overall Test (BOOT)**? [Post-Closing Loopholes: FWC
  applies a revised BOOT that considers the interests of the employee cohort overall, not
  individual "notional" employees — VERIFY current test formulation]
- Is the agreement still operative, or has it nominally expired (and if so, does it still
  apply by default under s 58 [VERIFY])?

**⟁ CLARIFY** — If award or agreement coverage is disputed or unclear:

- "I cannot confirm award coverage without more information about the role's primary duties
  and the employer's industry. Can you describe: (a) what the employee primarily does, and
  (b) the nature of the employer's business?"
- If multiple awards could apply: "Two awards may apply — [Award A] (industry-based) and
  [Award B] (occupation-based). The correct award depends on the employer's primary
  industry. Please confirm."

### Step 4: Gather Legal Authority

Use **legalcode-mcp** to retrieve current authority:

1. **Current FWA text**: Retrieve the current Fair Work Act 2009 (Cth) provisions
   relevant to the scope (e.g., NES sections, general protections, unfair dismissal criteria)
2. **Modern award text**: Retrieve the applicable modern award, including current wage
   rates, classification definitions, and any recent FWC variations
3. **FWO enforcement actions**: Search for relevant sector enforcement actions in the
   past 24 months to inform risk tier classification
4. **Leading cases**: Retrieve key Federal Court/FCFCA decisions relevant to the assessment
   scope (employee/contractor distinction, adverse action reverse onus, sham contracting)
5. **FWC guidance**: Retrieve any relevant FWC Benchbook chapters or practice notes

Save results to `/tmp/legalcode-au-fw-authority.md`:

```markdown
# Fair Work Act Authority Reference

## Date: [date]

## Scope: [employer/industry/assessment topic]

### Current Statutory Provisions

- [Section, current text or summary]

### Modern Award — [Award Name]

- [Current minimum rates, classification definitions, penalty rates]

### Key Cases

- [Case name, citation, key holding]

### FWO Enforcement Context

- [Recent relevant actions, penalties imposed, FWO strategic priorities]
```

**If legalcode-mcp is not connected:**

- Mark all statutory references [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed using general Fair Work knowledge; flag that award rates require independent
  verification at the FWC website and FWO Pay and Conditions Tool (PACT)

### Step 5: Conduct Compliance Assessment — Six Pillars

Assess against all six pillars relevant to the scope. Mark each finding with its
classification (COMPLIANT / PARTIAL / NON-COMPLIANT) and risk tier (CRITICAL / HIGH /
MEDIUM / LOW). Apply Self-Interrogation for every CRITICAL finding.

---

## Compliance Assessment Reference

### Pillar 1: Employment Status and Award Coverage

#### 1.1 Employee vs. Independent Contractor

**Governing authority**: Fair Work Act 2009 (Cth) ss 14, 357–359; _CFMMEU v Personnel
Contracting Pty Ltd_ [2022] HCA 1 [VERIFY]; _ZG Operations Australia Pty Ltd v Jamsek_
[2022] HCA 2 [VERIFY]; Closing Loopholes No. 2 Act 2024 — amended contractor provisions.

**Test after _Personnel Contracting_ / _Jamsek_ [VERIFY]:**
Where a written contract governs the relationship, the characterisation is determined
primarily by the legal rights and duties in that contract — not the parties' subsequent
conduct. Apply the multi-factor test to the written agreement:

| Factor            | Employee Indicators                   | Contractor Indicators                  |
| ----------------- | ------------------------------------- | -------------------------------------- |
| Control over work | Employer directs how work is done     | Worker controls how work is done       |
| Integration       | Work integral to business operations  | Work accessory to business             |
| Equipment/tools   | Employer provides                     | Worker provides own                    |
| Risk and reward   | Fixed wages; no financial risk        | Bears commercial risk; can profit/loss |
| Other engagements | Exclusivity required                  | Free to work for others                |
| Leave/benefits    | Annual leave, sick leave entitlements | No leave entitlements                  |
| Tax/invoicing     | Employer withholds PAYG               | Worker invoices (ABN)                  |
| Delegation        | Cannot delegate                       | Can subcontract                        |

**High-income opt-out (post-Closing Loopholes):** High-income earners (above the
contractor high income threshold — [VERIFY current amount at FWC]) may opt out of employee
characterisation provisions if both parties sign a compliant opt-out agreement.

**Key compliance checks:**

- [ ] The written contract reflects the genuine agreed terms (not a misleading description)
- [ ] Worker is not performing work under employer's sustained direction and control
      while labelled "contractor"
- [ ] ABN/GST registration is not the sole indicator of contractor status
- [ ] No sham contracting indicators present (see Pillar 5)

**Risk flags (CRITICAL):**

- Written agreement says "contractor" but employer directs every aspect of work,
  supplies all tools, and prohibits other engagements
- No written contract — oral or implied arrangement assessed by conduct (higher
  uncertainty post-_Personnel Contracting_)
- "Uber-style" arrangement: worker supplies only labour via app, no equipment risk,
  no separate client base → employee-like worker provisions may now apply

#### 1.2 Modern Award Coverage

**Governing authority**: FWA Part 2-3 (modern awards); FWC Modern Awards List (FWC
website — updated annually); FWA ss 46–49 (coverage) [VERIFY].

**Key compliance checks:**

- [ ] Employer has identified the correct modern award (by industry and classification)
- [ ] Employee is classified at the correct classification level under that award
- [ ] Minimum rates applied are current (annual wage review, effective 1 July) [VERIFY]
- [ ] All applicable penalty rates, overtime loadings, and allowances are paid
- [ ] Award flexibility arrangements (Individual Flexibility Arrangements, IFAs)
      are in writing, signed, and genuinely better off overall

**Risk flags:**

- Using outdated award classification schedule (CRITICAL — wage theft exposure if underpaid)
- Applying the wrong award to a classification (HIGH — systemic underpayment risk)
- Removing penalty rates by verbal agreement or generic contract clause (HIGH — void)
- Individual flexibility arrangement that leaves worker worse off overall (HIGH — invalid)

---

### Pillar 2: National Employment Standards (11 NES)

**Governing authority**: FWA Part 2-2, Divisions 3–13 [VERIFY]; FWA ss 55–131.

The 11 NES are minimum entitlements — any contractual or industrial instrument term
that is less favourable is void (s 55) [VERIFY]:

#### NES 1 — Maximum Weekly Hours (s 62) [VERIFY]

- **Entitlement**: 38 ordinary hours per week; employer may request reasonable additional
  hours
- **Reasonableness factors**: s 62(3) — health, safety, personal circumstances, needs of
  workplace, usual hours in the industry, etc. [VERIFY]
- **Key checks**: [ ] Employer not requiring >38 hours as a condition of employment without
  "reasonable additional hours" justification; [ ] Overtime premium paid where award applies

#### NES 2 — Flexible Working Arrangements (s 65) [VERIFY]

- **Eligibility**: Employees with 12 months continuous service; eligible categories:
  carer, disability, over 55, domestic violence victim, pregnancy
- **Employer obligation**: Must respond in 21 days in writing. If refusing, must specify
  reasonable business grounds and other options considered
- **Post-Closing Loopholes (from 6 June 2023 [VERIFY])**: Employee can apply to FWC if
  employer refuses or fails to respond. FWC may conciliate or arbitrate. FWC can make
  orders requiring the employer to grant the request
- **Key checks**: [ ] Written 21-day response procedure exists; [ ] Refusal reasons
  documented; [ ] FWC application procedure known if employee challenges

#### NES 3 — Parental Leave (ss 67–85) [VERIFY]

- **Entitlement**: Up to 12 months unpaid parental leave (plus 12-month extension right)
  for an employee with 12 months continuous service
- **Note**: Paid Parental Leave is governed by the _Paid Parental Leave Act 2010_ (Cth)
  (separate legislation) — FWA unpaid leave is additional
- **Key checks**: [ ] Return-to-work guarantee (same position or comparable); [ ] No adverse
  action taken during or after parental leave; [ ] Notice requirements met

#### NES 4 — Annual Leave (ss 86–94) [VERIFY]

- **Entitlement**: 4 weeks per year (5 for certain shift workers); accrues on a weekly basis
- **Cashing out**: Permitted by agreement but worker must retain at least 4 weeks post-
  cash-out; limit once per 12 months unless award provides otherwise [VERIFY]
- **Direction to take leave**: Employer may direct excessive annual leave (>8 weeks,
  or >6 in some awards) with reasonable notice [VERIFY]
- **Loading**: 17.5% annual leave loading applies under most modern awards [VERIFY]
- **Key checks**: [ ] Leave accrual tracked correctly; [ ] Cash-out agreements in writing;
  [ ] Leave loading paid; [ ] Leave balance available on payslip

#### NES 5 — Personal/Carer's Leave and Compassionate Leave (ss 95–107) [VERIFY]

- **Personal/carer's leave**: 10 days per year (paid); accrues progressively
- **Unpaid carer's leave**: 2 days per occasion (casual employees or when paid leave exhausted)
- **Compassionate leave**: 2 days per occasion on death or serious illness of immediate
  family or household member
- **Evidence**: Employer may require reasonable evidence (e.g., medical certificate)
- **Family and domestic violence leave**: 10 days paid per year (added to NES — effective
  1 February 2023 for large employers, 1 August 2023 for small business [VERIFY])
  Separate NES provision; confidentiality obligations on employer
- **Key checks**: [ ] Leave accrual tracked separately for personal and carer's leave;
  [ ] Evidence requirements are "reasonable" and not excessive; [ ] FDV leave available
  and confidentiality protected

#### NES 6 — Community Service Leave (ss 108–112) [VERIFY]

- **Jury duty**: Unpaid leave; employer must pay "make-up pay" (difference between jury
  allowance and ordinary earnings) for the first 10 days [VERIFY for current obligations]
- **Emergency management**: Unpaid leave for voluntary emergency workers; no duration cap
- **Key checks**: [ ] Policy covers both types; [ ] Make-up pay for jury duty calculated correctly

#### NES 7 — Long Service Leave (s 113) [VERIFY]

- **Entitlement**: Preserved pre-existing rights; state/territory laws apply (varies
  significantly — 13 weeks after 10 years in some states, 8.67 weeks after 7 years in
  Victoria, etc.) [VERIFY per state]
- **National system employer complication**: Pre-2010 entitlements under state laws
  preserved; new accrual under state laws continues
- **Key checks**: [ ] Correct state law identified; [ ] Leave tracked correctly; [ ] Accrual
  not inadvertently forfeited on casual conversions or related entity moves

#### NES 8 — Public Holidays (ss 114–116) [VERIFY]

- **Entitlement**: Reasonable day off on each public holiday (national and
  state/territory holidays)
- **Reasonable request to work**: Employer may request; employee may refuse if refusal
  is reasonable (having regard to employee's personal circumstances, nature of the work,
  adequate notice, etc.)
- **Substitution**: By written agreement, employer and employee may substitute another day
- **Key checks**: [ ] Penalty rates paid for public holiday work; [ ] Substitute day
  provisions documented; [ ] Refusal requests considered fairly

#### NES 9 — Notice of Termination and Redundancy Pay (ss 117–123) [VERIFY]

- **Minimum notice periods** (s 117) by period of continuous service [VERIFY]:
  - Less than 1 year: 1 week
  - 1–3 years: 2 weeks
  - 3–5 years: 3 weeks
  - Over 5 years: 4 weeks
  - Extra 1 week if employee is 45+ and has at least 2 years continuous service
- **Redundancy pay scale** (s 119) by period of continuous service [VERIFY]:
  - 1–2 years: 4 weeks
  - 2–3 years: 6 weeks
  - 3–4 years: 7 weeks
  - 4–5 years: 8 weeks
  - 5–6 years: 10 weeks
  - 6–7 years: 11 weeks
  - 7–8 years: 13 weeks
  - 8–9 years: 14 weeks
  - 9–10 years: 16 weeks
  - 10+ years: 12 weeks
- **Redundancy pay exceptions**: Small business employers (s 121) [VERIFY]; genuine
  redeployment within employer's enterprise or associated entity (s 120 [VERIFY])
- **Key checks**: [ ] Notice period meets or exceeds NES minimum; [ ] Payment in lieu
  documented; [ ] Redundancy pay correctly calculated; [ ] Consultation requirements
  under award met before notice

#### NES 10 — Fair Work Information Statement and Casual Employment Information Statement

(ss 125–125A) [VERIFY]

- **Obligation**: Employer must give new employees a copy of the Fair Work Information
  Statement (FWIS) before or on commencement; casual employees must also receive the
  Casual Employment Information Statement (CEIS)
- **CEIS — frequency**: After 12 months (and at each anniversary) for casuals
- **Key checks**: [ ] FWIS provided on commencement; [ ] CEIS provided to casuals at
  engagement and annually; [ ] Current version used (FWO publishes updated versions)

#### NES 11 — Superannuation (s 124A) [VERIFY — effective 1 January 2024]

- **Entitlement**: Employees entitled to employer superannuation contributions under
  the Superannuation Guarantee (Administration) Act 1992 (Cth) as an NES entitlement
- **Practical effect**: FWO can now pursue unpaid super alongside other FWA claims
  (previously limited to ATO enforcement)
- **Key checks**: [ ] Super contributions paid at the correct rate and to correct fund;
  [ ] Contributions paid on time (quarterly deadline — failure incurs SG Charge)

---

### Pillar 3: Modern Award and Enterprise Agreement Compliance

#### 3.1 Modern Award Obligations

**Key compliance checks:**

- [ ] Employee engaged at correct classification level under the applicable award
- [ ] Minimum hourly rate meets or exceeds the current award rate for that classification
- [ ] Penalty rates applied (evenings, weekends, public holidays) where award specifies
- [ ] Overtime calculated correctly for hours beyond ordinary hours
- [ ] Allowances paid: leading hand, tool, uniform, meal, travel, first aid — as applicable
- [ ] Rostering and shift arrangements comply with minimum hours and maximum shift lengths
- [ ] Rest and meal break entitlements observed
- [ ] Annualised salary arrangements (where permitted): written agreement, reconciliation
      obligation, back-pay if shortfall (annual or on termination) [VERIFY re award-specific
      requirements post-Moschetta v Chandler Macleod Group [2023 FCA VERIFY]]

**Underpayment assessment:**

1. Identify the applicable classification and period
2. Apply the correct award rate for each pay period (indexed rates — annual review)
3. Add applicable loadings (penalty rates, overtime)
4. Compare total paid vs. total owed
5. Quantify underpayment exposure and applicable limitation period (generally 6 years
   for civil claims [VERIFY])

**Wage theft risk (from 1 January 2025):**

- Intentional underpayment is now a criminal offence — prosecuted by the Commonwealth
  Director of Public Prosecutions on referral from FWO
- Civil remedies for underpayment remain available concurrently
- Penalties: body corporate up to $7.825M per contravention [VERIFY]; individual up to
  10 years imprisonment or $1.565M [VERIFY]
- "Dishonest underpayment" — less serious than wage theft but subject to higher civil
  penalties [VERIFY]

#### 3.2 Enterprise Agreement Compliance

**Key compliance checks:**

- [ ] Enterprise agreement is not nominally expired (or confirm continued operation if expired)
- [ ] The agreement passed the BOOT at approval: each employee would be "better off
      overall" compared to the applicable award [VERIFY current BOOT formulation post-
      Closing Loopholes No. 2]
- [ ] Agreement terms have not been unilaterally changed since approval
- [ ] New employees engaged after commencement: confirm agreement still covers them
- [ ] Bargaining process was compliant: protected industrial action, good faith bargaining
- [ ] Any NUE (non-union enterprise agreement) consultation requirements observed
- [ ] Union right-of-entry provisions respected (if applicable to the site)

---

### Pillar 4: General Protections and Adverse Action

**Governing authority**: FWA Part 3-1, ss 340–365 [VERIFY].

#### 4.1 Workplace Rights (s 341) [VERIFY]

A person has a **workplace right** if they:

- Are entitled to the benefit of a workplace law or instrument
- Have a role or responsibility under a workplace law or instrument
- Are entitled to initiate a process under a workplace law or instrument (e.g., making
  an FWO complaint, applying to FWC)

**Protected actions include:**

- Exercising any right under the FWA or a modern award (taking leave, requesting flexible
  work, receiving correct pay)
- Making a complaint or inquiry about employment conditions
- Participating in FWC proceedings
- Union membership or non-membership

#### 4.2 Adverse Action (s 342) [VERIFY]

An employer must not take **adverse action** against an employee because the employee
exercised, or proposed to exercise, a workplace right.

**Adverse action includes:**

- Dismissing an employee
- Injuring an employee in their employment
- Altering an employee's position to their prejudice
- Discriminating between the employee and other employees

**Reverse onus of proof (s 361) [VERIFY]**: If an employee makes a general protections
claim, it is **presumed** that the adverse action was taken for the alleged prohibited
reason — the burden shifts to the **employer** to prove it was not. This is a powerful
provision that makes general protections claims strategically useful.

**Key compliance checks:**

- [ ] No management decisions made within temporal proximity to an employee exercising
      a right (raises inference of prohibited reason)
- [ ] Managers trained on general protections — they must not reduce hours, restructure
      roles, or terminate employment as a response to leave requests, complaints, or union activity
- [ ] Performance management processes not initiated in response to a workplace rights
      complaint
- [ ] Right to disconnect refusals: employer's response to a refusal is not adverse action
      (if refusal was not unreasonable)

**General protections vs. unfair dismissal:**
| Feature | General Protections | Unfair Dismissal |
|---------|--------------------|--------------------|
| Eligibility | All FWA employees (no minimum period) | Minimum employment period required |
| Time limit | 21 days from dismissal (for dismissal claims); no limit for non-dismissal | 21 days from dismissal |
| Reverse onus | Yes — employer must disprove prohibited reason | No — employee must prove unfairness |
| Remedies | Reinstatement, compensation, civil penalties | Reinstatement (preferred), compensation |
| Non-dismissal | Yes — can claim without dismissal | No |
| Scope | Broader — any exercise of workplace right | Narrower — dismissal only |

**⟁ CLARIFY** — If a termination scenario involves both potential general protections and
unfair dismissal issues:

- "This scenario may support both an unfair dismissal claim and a general protections claim.
  A general protections claim has no minimum employment period requirement and carries a
  reverse onus. Do you want me to assess both pathways?"

#### 4.3 Coercion, Misrepresentation, and Undue Influence

**Key checks:**

- [ ] No coercion to join, not join, or leave a union (ss 348–349 [VERIFY])
- [ ] No misrepresentation about workplace rights (s 345 [VERIFY])
- [ ] No undue influence on enterprise agreement bargaining
- [ ] No taking adverse action against industrial association (ss 346–347 [VERIFY])

---

### Pillar 5: Sham Contracting

**Governing authority**: FWA ss 357–359 [VERIFY]; Closing Loopholes No. 2 Act 2024
(amended defence provision).

**The three sham contracting prohibitions:**

| Prohibition                            | What is prohibited                                                                                                         | Amended after Closing Loopholes?                                                                                                                                                                      |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **s 357**: Misrepresentation           | Employer must not represent a contract of employment as a services contract                                                | No change                                                                                                                                                                                             |
| **s 358**: Dismissal and re-engagement | Employer must not dismiss an employee to re-engage them as a contractor to perform the same or substantially the same work | No change                                                                                                                                                                                             |
| **s 359**: Inducement                  | Employer must not induce an employee to become a contractor under a false representation                                   | **Old**: defence if employer did not know it was employment. **New (from 26 Feb 2024)**: defence only if employer "reasonably believed" it was a services contract — higher bar to establish [VERIFY] |

**Sham contracting indicators (high-risk combination):**

- Worker performs the same role before and after "conversion" to contractor
- No change in place of work, hours, or tasks
- Employer continued to direct and control how work is done
- Worker has no genuine commercial independence (no other clients, no business structure)
- ABN obtained to satisfy employer, not driven by genuine business operation
- Worker classified as contractor but no written services contract in place
- Previous underpayment claims triggered the "conversion"

**Key compliance checks:**

- [ ] Any contractor arrangement reflects a genuine commercial services relationship
- [ ] Written services contract specifying deliverables, not hours worked
- [ ] Contractor has genuine independence (other clients, own tools/risk)
- [ ] Conversion from employment to contractor has a legitimate commercial basis and
      change in the nature of the relationship
- [ ] Post-Closing Loopholes: employer cannot rely solely on label — must have reasonably
      believed the arrangement was a genuine services contract

---

### Pillar 6: Termination, Unfair Dismissal, and Redundancy

**Governing authority**: FWA Part 3-2, ss 385–405 [VERIFY]; Small Business Fair Dismissal
Code (for employers <15 employees).

#### 6.1 The Four-Stage Unfair Dismissal Test (s 385) [VERIFY]

For an unfair dismissal claim to succeed, the employee must establish:

1. They were **dismissed** (including constructive dismissal — s 386 [VERIFY])
2. The dismissal was **harsh, unjust, or unreasonable** (s 387 factors below)
3. The dismissal was **not a case of genuine redundancy** (s 389 [VERIFY])
4. The dismissal was **not consistent with the Small Business Fair Dismissal Code**
   (if a small business employer — s 388 [VERIFY])

**Eligibility requirements:**

- Minimum employment period: **6 months** (or **12 months** for a small business employer)
  [VERIFY — must be employed for this period at time of dismissal]
- Not covered by an excluded category (e.g., certain apprentices, trainees in specified
  programs) [VERIFY]
- High income threshold: No unfair dismissal if earnings exceed the high income threshold
  AND not covered by a modern award or enterprise agreement [VERIFY current threshold at FWC]

#### 6.2 Section 387 Factors [VERIFY]

FWC considers these factors in assessing whether dismissal was harsh, unjust, or
unreasonable:

| Factor                                              | Key Questions                                                                                 |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **s 387(a)**: Valid reason                          | Was there a sound, defensible reason based on capacity, conduct, or operational requirements? |
| **s 387(b)**: Notification                          | Was the employee notified of the reason (in clear terms) before dismissal?                    |
| **s 387(c)**: Opportunity to respond                | Was the employee given a genuine opportunity to respond to the allegations?                   |
| **s 387(d)**: Support person                        | Was the employee unreasonably refused a support person in any discussions?                    |
| **s 387(e)**: Warning of unsatisfactory performance | Were warnings given (if dismissal for performance)?                                           |
| **s 387(f)**: Size of employer                      | Did the size of the employer's enterprise impact procedures?                                  |
| **s 387(g)**: HR expertise                          | Was there dedicated HR management and procedures?                                             |
| **s 387(h)**: Any other matters                     | All other relevant circumstances                                                              |

**Practical guidance on s 387:**

- No single factor is decisive — FWC weighs them in combination
- Serious misconduct (theft, violence, sexual harassment) may justify immediate dismissal
  without warning — but documentation is still critical
- Performance dismissal: typically requires prior warnings, reasonable opportunity to
  improve, documented support, clear timeframes
- Show cause letters should be specific (not generic), give adequate time to respond,
  and allow a support person

#### 6.3 Genuine Redundancy (s 389) [VERIFY]

A dismissal is a **genuine redundancy** if:

1. The employer no longer required the work to be done (operational requirement)
2. Applicable consultation obligations (under modern award or enterprise agreement)
   have been complied with
3. It was not **reasonable in all the circumstances** to redeploy the employee within
   the employer's enterprise or associated entity

**Redundancy checklist:**

- [ ] Documented operational reason (restructure, automation, downturn — not manufactured)
- [ ] Award/agreement consultation provisions followed: notify, consult, consider alternatives
- [ ] Genuine redeployment consideration: positions searched in related entities
- [ ] Selection process (if multiple made redundant) transparent and non-discriminatory
- [ ] NES redundancy pay calculated and paid
- [ ] Payment in lieu of notice where applicable

#### 6.4 Right to Disconnect (new — Closing Loopholes No. 2 Act 2024)

**Governing authority**: FWA new Part 2-9, Division 12 [VERIFY section numbers] —
effective 26 August 2024 (large employers); 26 August 2025 (small business).

- Employees may refuse to monitor, read, or respond to contact from employer (or contact
  from a third party relating to work) **outside work hours** unless the refusal is
  unreasonable
- **Unreasonable refusal factors** [VERIFY]: nature of employee's role and responsibilities;
  whether compensated for availability; urgency of the contact; personal circumstances
- **FWC dispute resolution**: Either party can apply to FWC if dispute cannot be resolved
  in the workplace. FWC can make **stop orders** against both unreasonable refusals AND
  unreasonable employer contact
- **Key compliance checks**:
  - [ ] Right to disconnect policy developed and communicated
  - [ ] Manager training on the right — emails/calls after hours must have genuine
        business urgency unless employee is compensated for availability
  - [ ] On-call arrangements and availability loadings reviewed under applicable award
  - [ ] No adverse action taken against employees who exercise the right to disconnect

#### 6.5 Fixed-Term Contract Limits (Closing Loopholes No. 1 Act 2023)

**Governing authority**: FWA new ss 333M–333R [VERIFY] — effective 6 December 2023.

**New restrictions:**

- A fixed-term contract must not have a term (including extensions) exceeding **2 years** [VERIFY]
- Employer must not engage an employee on successive fixed-term contracts for the
  same or substantially the same role if the total period exceeds 2 years **or** more
  than **2 contracts** have been made [VERIFY]
- **Fixed Term Contract Information Statement**: Employer must provide to each fixed-term
  employee at engagement [VERIFY]

**Exceptions** [VERIFY — confirm against legislation]:

- Earnings exceeding the high income threshold (with no award/agreement coverage)
- Specified government-funded positions (where position is contingent on grant)
- Training arrangements (apprenticeships, traineeships)
- Governance positions (e.g., board appointees, statutory officeholders)
- Seasonal work arrangements
- Positions requiring a specialist skill not otherwise available in the business

**Key compliance checks:**

- [ ] All current fixed-term contracts audited for 2-year/2-contract compliance
- [ ] Renewal decisions assessed against statutory exceptions before extending
- [ ] Fixed Term Contract Information Statement provided at engagement
- [ ] Contracts not created to circumvent the restrictions (sham arrangements)

#### 6.6 Casual Conversion (post-Closing Loopholes No. 2 Act 2024)

**New casual definition** [VERIFY — from 26 August 2024]:
A **casual employee** is one engaged under an arrangement where there is **no firm advance
commitment** to continuing and indefinite work on an agreed pattern of work. This is
assessed by looking at the work pattern actually worked over the preceding 12 months,
not solely by reference to contractual terms.

**Casual conversion pathway:**

- After **6 months** of employment (12 for small business employers), a casual employee
  may give a **written notification** to the employer requesting to convert to
  permanent (full-time or part-time)
- Employer must consult and respond within 21 days
- If employer refuses, employee may apply to FWC
- Where the work pattern shows regularity and systematic engagement, conversion
  presumption strengthens

**Key compliance checks:**

- [ ] Casual Employment Information Statement given to casuals on engagement and annually
- [ ] Casual conversion eligibility assessed at 6-month mark
- [ ] Work patterns of casuals monitored: regular systematic rostering that looks like
      permanent engagement triggers conversion right
- [ ] Casual loading paid (typically 25% in modern awards [VERIFY]) to compensate for
      absence of leave entitlements
- [ ] "Casual" classification is not used to avoid ongoing engagement obligations

---

### Step 6: Classify and Score Each Finding

For each finding from the six pillars, apply the **severity classification framework**:

#### Severity Classification

**Status dimension:**

| Status            | Definition                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **COMPLIANT**     | Meets Fair Work Act, NES, and applicable award/enterprise agreement requirements. No remediation needed.                       |
| **PARTIAL**       | Some requirements met; gaps or improvements identified. Remediation recommended within defined timeline.                       |
| **NON-COMPLIANT** | Clear breach of the Fair Work Act, NES, modern award, or enterprise agreement. Remediation required; legal advice recommended. |

**Risk tier dimension (FWO-enforcement calibrated):**

| Tier         | Definition                                                                                                                                                                        | FWO Signal                                                                     | Timeline                                    |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------- |
| **CRITICAL** | Direct breach of NES minimum entitlements, award minimum rates, or wage theft exposure; general protections adverse action; sham contracting; right to disconnect stop-order risk | FWO has pursued comparable proceedings; active enforcement sector              | Immediate — legal advice within 48–72 hours |
| **HIGH**     | Material Fair Work breach with significant penalty exposure; systemic underpayment; unfair dismissal procedural failures; fixed-term contract violations                          | Within current FWO enforcement priorities; defensibility questionable          | Within 2–4 weeks                            |
| **MEDIUM**   | Compliance gap affecting minority of workers or involving non-NES obligations; lower FWO enforcement frequency but defensibility uncertain                                        | FWO not current headline priority, but captured in routine compliance activity | Within 4–8 weeks                            |
| **LOW**      | Best practice improvement; no direct Fair Work breach; recommended for stronger compliance posture                                                                                | FWO unlikely to prioritise                                                     | Next review cycle                           |

**Automatic CRITICAL triggers:**

The following findings must be classified CRITICAL regardless of other circumstances:

- Any identified underpayment of award minimum wages (wage theft exposure post-1 Jan 2025)
- Termination of employee for exercising a workplace right (adverse action)
- Sham contracting arrangement with multiple indicators
- Failure to provide NES entitlements (e.g., no leave accrual for a casual who is actually permanent)
- Dismissal of an employee during parental leave without valid grounds

### Step 7: Generate Remediation for Each Finding

For each NON-COMPLIANT or PARTIAL finding, produce an actionable finding block (see
Output Format Template below).

**⟁ CLARIFY** — If the underpayment amount cannot be calculated without additional data:

- "To quantify the underpayment exposure, I need the employee's pay rate, hours worked,
  and pay history. Can you provide: (a) applicable classification, (b) pay rate per
  period, and (c) number of weeks of potential underpayment?"

**⟁ CLARIFY** — For termination scenarios where procedural history is unclear:

- "To assess unfair dismissal risk fully, I need to know: (a) Were written warnings given?
  (b) Was the employee given an opportunity to respond before dismissal? (c) Did the
  employee request or were they offered a support person? Please confirm."

### Step 8: FWO Enforcement Risk Profile

Assess the overall enforcement risk based on:

1. **Sector priority**: Is this employer in a sector where FWO has active enforcement
   campaigns (e.g., hospitality, retail, construction, agriculture, cleaning, security)?
2. **Contravention type**: Wage theft, sham contracting, and adverse action attract the
   highest FWO priority
3. **Scale**: Systemic underpayment affecting many workers attracts higher scrutiny than
   isolated errors
4. **Prior history**: Any prior FWO notices, undertakings, or court findings multiply risk
5. **Anonymous reporting**: FWO receives substantial anonymous complaints — every
   underpaid worker is a potential whistleblower

**Civil penalty exposure** [VERIFY current amounts — indexed to penalty units]:

- Non-serious contravention: body corporate up to $93,900 per contravention [VERIFY];
  individual up to $18,780 [VERIFY]
- Serious contravention (employer knew or was reckless): body corporate up to $939,000
  [VERIFY]; individual up to $93,900 [VERIFY]
- Wage theft (criminal — from 1 Jan 2025): individual up to 10 years / $1.565M [VERIFY];
  body corporate up to $7.825M [VERIFY]
- Each underpaid employee on each pay period = a separate contravention

### Step 9: Compile Remediation Roadmap

Consolidate all findings into a prioritised remediation roadmap with:

- Priority 1 — Immediate (CRITICAL): action within 48–72 hours
- Priority 2 — Urgent (HIGH): action within 2–4 weeks
- Priority 3 — Scheduled (MEDIUM): action within 4–8 weeks
- Priority 4 — Review cycle (LOW): next scheduled review

### Step 10: Quality Verification

Before delivering output, run the full quality assurance framework:

1. Run all 5 Citation Quality Gates silently; revise failures before delivery
2. For every CRITICAL finding, run the 3-pass Self-Interrogation
3. Assign Confidence Score to each material finding
4. Verify: all 6 pillars assessed (or documented reason for exclusion)
5. Generate the Glass Box Audit Trail and append to output

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivery. Revise any failure before output.

| Gate           | Rule                                                                                                                                                                          | Fail Action                                                       |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Source**     | Every Fair Work compliance claim cites a specific FWA section, modern award clause, FWC decision, or established principle                                                    | Add citation or mark "[UNVERIFIED — counsel to confirm]"          |
| **Format**     | All citations follow Australian legal citation format (e.g., Fair Work Act 2009 (Cth) s 324; [2024] FWC 1234; [2022] HCA 1)                                                   | Fix format                                                        |
| **Currency**   | Every cited FWA provision checked for amendments; modern award rates and terms verified as current (indexed annually 1 July); penalty amounts verified                        | Flag "[CHECK CURRENCY — indexed annually; verify at FWC website]" |
| **Domain**     | Analysis stays within FWA 2009 (Cth) and applicable instruments. No imports of state employment law unless explicitly scoped. NES applies only to employees — not contractors | Remove or flag jurisdictional bleed                               |
| **Confidence** | Uncertainty explicitly stated. Where FWO enforcement outcome or penalty amount cannot be confirmed, say so                                                                    | Add confidence qualifier                                          |

### Self-Interrogation for CRITICAL and NON-COMPLIANT Findings

For any finding classified CRITICAL or NON-COMPLIANT, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**:

- Does the classification follow logically from the FWA section or award provision cited?
- Would the FWO, FCFCA, or Federal Court agree on these facts?
- What is the strongest counter-argument ("This is compliant because…")?

**Pass 2 — Completeness**:

- Have all relevant FWA sections and modern award provisions been considered?
- Are there FWC decisions or FWO guidance that distinguish or support the finding?
- Is there an enterprise agreement override, individual flexibility arrangement, or
  other instrument that changes the analysis?
- Has the Closing Loopholes commencement date been accounted for (the obligation may
  not have applied at the relevant time)?

**Pass 3 — Challenge**:

- What is the strongest argument that this practice COMPLIES with Fair Work Act?
- Under what circumstances might a reasonable employment lawyer accept this risk?
- Is CRITICAL classification proportionate, or is this actually HIGH with mitigations?

Mark the audit trail `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                                                                       | Action                                                |
| ------------ | --------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled Fair Work law, clear statute, no reasonable dispute                                   | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong authority from FWC/Federal Court, clear award language, minor interpretation questions | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments but reasonable employment lawyers could differ                                 | State with reasoning and counter-indicators           |
| **Possible** | 0.40–0.59 | Genuinely uncertain, fact-dependent or competing authorities                                  | Flag for counsel review with both sides               |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                                                                       | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every assessment output MUST include this Glass Box section:

```yaml
glass_box:
  skill: "legalcode-au-fair-work-compliance"
  date: "[Date of assessment]"
  subject: "[Organization name or description of materials assessed]"
  sector: "[Industry sector]"
  employer_size: "[Small business <15 / Medium 15-99 / Large 100+]"
  perspective: "[Employer / Employee / Adviser]"
  workforce_types_assessed:
    - "[Full-time / Part-time / Casual / Contractor / Labour hire / Gig / Mixed]"
  scope_assessed:
    - "[e.g., Employment agreements, NES compliance, Award rate audit, Termination procedures]"
  pillars_assessed:
    - "[List: Employment status, NES, Modern award, General protections, Sham contracting, Termination]"
  findings_summary:
    critical: "[number]"
    high: "[number]"
    medium: "[number]"
    low: "[number]"
    compliant: "[number]"
  applicable_modern_award: "[Award name and FWC determination code, or 'EA applies', or 'N/A']"
  closing_loopholes_provisions_assessed:
    - "[List applicable reforms: right to disconnect, casual definition, fixed-term limits, etc.]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-au-fw-authority.md or 'Not created']"
  statutes_consulted:
    - "Fair Work Act 2009 (Cth) — [VERIFIED / UNVERIFIED]"
    - "[Modern Award name, FWC Determination — VERIFIED / UNVERIFIED]"
    - "[Case citation — VERIFIED / UNVERIFIED]"
  cases_consulted:
    - "[Case name, citation — VERIFIED / UNVERIFIED]"
  penalty_thresholds:
    body_corporate_standard: "Up to $93,900 per contravention [VERIFY — indexed]"
    body_corporate_serious: "Up to $939,000 per contravention [VERIFY — indexed]"
    individual_standard: "Up to $18,780 per contravention [VERIFY — indexed]"
    wage_theft_criminal: "Up to $7.825M (body corporate) or 10 years / $1.565M (individual) — effective 1 Jan 2025 [VERIFY]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL or NON-COMPLIANT findings)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[e.g., No payroll records provided — underpayment amount estimated only]"
    - "Modern award rates indexed annually — verify current rates at FWC website or FWO Pay and Conditions Tool (PACT)"
    - "Closing Loopholes commencement dates vary — verify applicable date for each reform"
    - "State/territory long service leave laws not fully assessed in this review"
    - "FWO enforcement priorities evolve — verify current strategic enforcement plan"
  reviewer: "AI-assisted — requires review by a qualified employment lawyer or industrial relations practitioner"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in Fair Work Act compliance assessment:

1. **Treating contractor labels as conclusive**: A written "contractor" label does not
   make someone an independent contractor. Post-_Personnel Contracting_ [2022] HCA 1,
   characterisation is based on the rights and duties in the written contract. Post-
   Closing Loopholes, conduct over 12 months can also inform the assessment for casual
   workers. An ABN and an invoice do not create a genuine contractor relationship.

2. **Applying pre-Closing Loopholes frameworks to post-August 2024 situations**: Many
   compliance guides and templates have not been updated for the Closing Loopholes reforms.
   Right to disconnect, new casual definition, fixed-term limits, and casual conversion
   reform all took effect in 2024. Applying the old framework (e.g., "Rossato codification"
   for casuals, old casual conversion s 64A-H) to a post-2024 situation is a material error.

3. **Treating "at-will employment" as an Australian concept**: Australia has no at-will
   employment doctrine. All terminations of national system employees must comply with
   NES minimum notice periods and are subject to the Fair Work Act unfair dismissal and
   general protections framework. Advising an employer they can "terminate at any time for
   any reason" is dangerously wrong.

4. **Ignoring the reverse onus of proof in general protections claims**: Under s 361,
   once a general protections claim is made, the employer must prove the adverse action
   was NOT for a prohibited reason. This flips the evidentiary burden. Assessing general
   protections risk without accounting for this reversal produces unreliable advice.

5. **Assuming a fixed-term employee cannot make an unfair dismissal claim**: Where a
   fixed-term employee is dismissed before their contract end date, they may have an
   unfair dismissal claim. Where a fixed-term contract ends and the employer has breached
   the fixed-term contract limits (2-year/2-contract), broader claims may also arise.

6. **Using the old BOOT test formulation for enterprise agreements post-Closing Loopholes**:
   The BOOT was modified. FWC now considers the interests of the employee cohort overall,
   not individual hypothetical "notional" employees in every possible circumstance. Applying
   the stricter pre-2024 test to a post-Closing Loopholes agreement approval may be incorrect.

7. **Quantifying underpayment exposure as prospective-only**: If award rates were not
   applied correctly, the underpayment exposure runs from the date of breach — potentially
   years of back-pay liability. Correction going forward does not extinguish the historic
   obligation. Always quantify the full retrospective exposure.

8. **Skipping redundancy consultation requirements**: Genuine redundancy under s 389
   requires compliance with applicable consultation obligations in the modern award or
   enterprise agreement. Failing to consult before giving notice of redundancy destroys the
   "genuine redundancy" defence and exposes the dismissal to unfair dismissal challenge.

9. **Treating all serious misconduct as grounds for immediate dismissal**: Serious
   misconduct (theft, fraud, violence, refusal to carry out lawful instructions) may justify
   summary dismissal but still requires reasonable investigation, putting the allegation
   to the employee, and giving opportunity to respond. Skipping these steps in "obvious"
   cases is a common source of successful unfair dismissal claims.

10. **Ignoring the 21-day time limit for FWC applications**: Unfair dismissal and general
    protections dismissal applications must be lodged within 21 days of dismissal. Late
    applications require FWC permission (rare and subject to stringent criteria). Employers
    relying on a time-bar defence should not be the reason the assessment missed this.

11. **Treating long service leave as uniform across Australia**: Long service leave is
    preserved under s 113 but is governed by state/territory laws that differ materially
    in entitlement period, qualifying period, and portability. Applying NSW rates to a
    Victorian employee (or vice versa) is a concrete error.

12. **Classifying casual employees as "no entitlements"**: Casual employees are entitled
    to the Fair Work Information Statement, the Casual Employment Information Statement,
    unpaid carer's leave, compassionate leave, community service leave, and (post-NES 11)
    superannuation. After Closing Loopholes, casual employees who meet the new definition
    tests may be entitled to convert to permanent — the 25% casual loading does not
    extinguish conversion rights.

13. **Assuming an expired enterprise agreement no longer applies**: An enterprise
    agreement that has nominally expired continues to apply by operation of the Fair Work
    Act (ss 57–58 [VERIFY]) until replaced by a new agreement or terminated by FWC.
    Employees covered by the agreement continue to receive its terms. "It expired in 2021"
    does not release the employer from its obligations.

14. **Copying policy templates without updating for Closing Loopholes**: Right to
    disconnect policies, casual employment policies, and fixed-term contract templates
    from pre-2024 sources will not reflect the new statutory obligations. Verify that any
    template is current as of August 2024 or later.

15. **Ignoring the wage theft criminal threshold for management exposure**: From 1 January
    2025, knowing underpayment of employees exposes individual managers (not just the
    corporate entity) to criminal prosecution. HR managers, payroll officers, and company
    directors who knowingly authorise or permit underpayments are personally exposed. This
    changes the risk profile for compliance governance — document all award rate checks.

16. **Applying the Minimum Employment Period as a blanket defence**: The minimum
    employment period (6 months or 12 months for small business) applies to unfair dismissal
    claims only. General protections claims under Part 3-1 (adverse action) have no minimum
    employment period — a new starter dismissed the first week for making a complaint about
    wages can bring a general protections claim.

17. **Failing to account for penalty rate reductions under awards post-2017**: Some modern
    awards had penalty rates reduced for Sunday and public holiday work by FWC transitional
    determinations (2017–2020). These reductions are award-specific and sector-specific.
    Do not assume any penalty rate without checking the specific award and its variation history.

18. **Overlooking right to disconnect policy obligations for on-call and emergency workers**:
    The right to disconnect has exceptions and specific considerations for workers who are
    compensated for availability (e.g., on-call loading). Blanket right-to-disconnect
    policies that do not address compensated availability may inadvertently create disputes
    or undermine legitimate on-call arrangements.

19. **Treating the 25% casual loading as automatically offsetting all permanent entitlements**:
    The casual loading compensates for the absence of leave entitlements and job security.
    It does not override the right to convert to permanent employment where the new casual
    definition tests are met. A casual who has been engaged regularly and systematically for
    more than 12 months cannot be denied conversion rights simply because they received a
    casual loading.

20. **Assuming pay in lieu of notice extinguishes procedural obligations**: Payment in
    lieu of notice satisfies the NES notice obligation (s 117(2) [VERIFY]). It does not
    satisfy the obligation to follow a fair procedure before dismissal for conduct or
    performance reasons. Procedural fairness under s 387 is separate from and additional
    to notice entitlements.

---

## Writing Standards

Apply plain-language discipline to all output:

**For remediation language (shared with employer or employee)**:

- Plain language — no Latin, no unexplained abbreviations
- Active voice: "The employer must pay" not "Payment must be made by the employer"
- Short sentences — one point per sentence
- Name the actor: "The payroll manager must verify" not "verification is required"
- Specific: "Apply the Hospitality Industry (General) Award 2020 classification Level 3"
  not "apply the applicable award rate"

**For internal analysis:**

- Same plain-language standards
- Technical FWA terminology where precise (e.g., "adverse action under s 342")
- Confidence qualifiers where genuinely uncertain
- Glass Box appended

**Quality gates before delivery:**

1. Can a business owner without legal training understand the executive summary?
2. Can a qualified employment lawyer understand the basis for each finding?
3. Is every non-compliant finding backed by a specific FWA section or award clause?
4. Are any findings vague ("may have issues") rather than specific ("Section X requires Y")?
5. Could any sentence be shorter without losing meaning?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for current FWA text, applicable modern award, FWC decisions, and
  FWO enforcement data
- Save results to `/tmp/legalcode-au-fw-authority.md`
- Verify modern award minimum rates and classification levels against FWC database
- Check Closing Loopholes commencement dates for each applicable reform
- Search for relevant FWO enforcement precedents for risk tier calibration
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Direct the user to authoritative sources for verification:
  - Modern award rates: FWC website (fwc.gov.au) — Modern Awards Pay Database
  - FWO Pay and Conditions Tool (PACT): calculate minimum pay and entitlements
  - Federal Register of Legislation (legislation.gov.au): current FWA text
  - FWO website (fairwork.gov.au): enforcement priorities, fact sheets, compliance tools
- Focus the assessment on structural compliance gaps, procedural obligations, and
  qualitative sham contracting / adverse action analysis rather than precise wage
  quantum calculations

---

## Output Format Template

Structure the final deliverable as:

```markdown
# Fair Work Act Compliance Assessment

**Organization / Subject**: [name or description]
**Perspective**: [Employer / Employee / Adviser]
**Assessment Date**: [date]
**Scope**: [full audit / targeted review — specify]
**Industry / Sector**: [industry]
**Employer size**: [small / medium / large]
**Applicable Award / Agreement**: [name or TBC]
**Review Basis**: [NES + [Award Name] / Enterprise Agreement / General FWA standards]

---

## Executive Summary

[2–3 sentences: overall compliance posture, most critical findings, immediate actions required]

**Findings at a glance:**
| Tier | Count | Key Issues |
|------|-------|-----------|
| CRITICAL | [n] | [brief] |
| HIGH | [n] | [brief] |
| MEDIUM | [n] | [brief] |
| LOW | [n] | [brief] |
| COMPLIANT | [n] | — |

---

## Key Findings — Immediate Action Required

### CRITICAL Findings

> [Brief, bold statement of each CRITICAL finding. Employee and employer can act on these immediately.]

---

## Assessment by Pillar

### Pillar 1: Employment Status and Award Coverage

[COMPLIANT / PARTIAL / NON-COMPLIANT + Risk Tier summary + key findings]

### Pillar 2: National Employment Standards

[Assessment of applicable NES with finding for each relevant standard]

### Pillar 3: Modern Award / Enterprise Agreement Compliance

[Classification, rates, loadings, IFA analysis]

### Pillar 4: General Protections and Adverse Action

[Workplace rights, adverse action risk, management exposure]

### Pillar 5: Sham Contracting

[If applicable — contractor characterisation analysis]

### Pillar 6: Termination, Unfair Dismissal, and Redundancy

[Procedural fairness, s 387 factors, genuine redundancy, right to disconnect]

---

## Detailed Findings

For each finding:

---

**Finding [#]: [Short descriptive title]**

**Fair Work Pillar**: [Pillar name]
**Classification**: NON-COMPLIANT / PARTIAL / COMPLIANT
**Risk Tier**: CRITICAL / HIGH / MEDIUM / LOW
**Confidence**: [Definite / High / Probable / Possible]

**What was found**:
[Description of the non-compliant element — quote or describe precisely]

**Why it's an issue**:
[Fair Work Act basis — cite specific section and principle]

**FWO enforcement context**:
[Relevant FWO enforcement action, FWC decision, or statutory penalty — with [VERIFY] where applicable]

**Potential exposure**:
[Underpayment quantum if quantifiable / Civil penalty exposure / Criminal risk / FWC claim risk]

**Required action**:
[Specific remediation step — named actor, specific action]

**Revised language / procedure** (if applicable):

> [Draft compliant clause or procedure]

**Fallback position** (if applicable):

> [Alternative that still complies if primary revision is not feasible]

**Dependencies**:
[Other changes required — e.g., payroll system update, manager training, FWC notification]

---

## Remediation Roadmap

### Priority 1 — Immediate (CRITICAL)

| Finding | Action   | Owner   | Target Date   |
| ------- | -------- | ------- | ------------- |
| [#]     | [action] | [owner] | [48–72 hours] |

### Priority 2 — Urgent (HIGH)

| Finding | Action   | Owner   | Target Date        |
| ------- | -------- | ------- | ------------------ |
| [#]     | [action] | [owner] | [within 2–4 weeks] |

### Priority 3 — Scheduled (MEDIUM)

| Finding | Action   | Owner   | Target Date        |
| ------- | -------- | ------- | ------------------ |
| [#]     | [action] | [owner] | [within 4–8 weeks] |

### Priority 4 — Review Cycle (LOW)

| Finding | Action   | Owner   | Target Date   |
| ------- | -------- | ------- | ------------- |
| [#]     | [action] | [owner] | [next review] |

---

## Fair Work Compliance Program Gaps

**Systemic issues to address beyond individual findings:**

- [e.g., No award rate review process — annual FWC determinations not tracked]
- [e.g., No right to disconnect policy — immediate requirement for large employers]
- [e.g., No termination checklist — procedural fairness steps not documented]
- [e.g., No casual review process — conversion eligibility not monitored]

**Training or policy updates needed:**

- [Policy 1 — e.g., Updated Right to Disconnect Policy]
- [Policy 2 — e.g., Manager training on general protections / adverse action]
- [Policy 3 — e.g., Fixed-term contract review procedure]

---

## Next Steps

1. [Immediate legal review recommended — specify area]
2. [Payroll audit / back-pay calculation required — specify scope]
3. [FWC or FWO engagement recommendation — if applicable]
4. [Closing Loopholes commencement audit — verify which reforms now apply]

---

## Glass Box Audit Trail

[Insert Glass Box YAML as per template above]
```

---

## Localization Notes

This skill applies exclusively to **national system employers** under the Fair Work Act
2009 (Cth). Consider the following intersections:

**Western Australia**: State government agencies and some unincorporated businesses
operate under the WA Industrial Relations Act 1979 and the Western Australian Industrial
Relations Commission (WAIRC). The national system applies to constitutional corporations
in WA. Confirm which system applies before proceeding with any WA assessment.

**State/Territory long service leave**: State and territory long service leave laws are
preserved by FWA s 113. These laws vary significantly — particularly in qualifying period,
accrual rate, and portability between related employers. Always identify the applicable
state/territory law for long service leave assessment.

**Public sector**: State and territory public sector employees are generally governed by
state/territory industrial relations systems. Commonwealth public servants are national
system employees.

**Sector-specific awards and codes**: Some industries have specific instruments:

- Building and construction: Building Code 2024 (Commonwealth) [VERIFY]
- Oil industry: Petroleum and Gas (Production and Processing) Award 2020 [VERIFY]
- Agricultural workers: Agricultural Award 2020 [VERIFY]; seasonal worker visa conditions
  intersect with FWO compliance

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

- Legalcode 2-agent research pipeline: structural analysis of `legalcode-au-consumer-law-compliance`
  and `legalcode-contract-review` reference skills; deep web research on Fair Work Act 2009
  (Cth) as amended by the Closing Loopholes Acts (2023–2024)
- Key statutory sources: Fair Work Act 2009 (Cth); Fair Work Legislation Amendment
  (Closing Loopholes) Act 2023; Fair Work Legislation Amendment (Closing Loopholes No. 2)
  Act 2024; Fair Work Regulations 2009 (Cth)
- Key authorities consulted: _CFMMEU v Personnel Contracting Pty Ltd_ [2022] HCA 1;
  _ZG Operations Australia Pty Ltd v Jamsek_ [2022] HCA 2; _WorkPac Pty Ltd v Rossato_
  [2021] HCA 23; FWC s 387 jurisprudence; FWO strategic enforcement materials
- Structural patterns: adapted from `legalcode-au-consumer-law-compliance` (6-pillar
  compliance assessment, COMPLIANT/PARTIAL/NON-COMPLIANT + CRITICAL/HIGH/MEDIUM/LOW
  severity matrix, FWO-calibrated enforcement risk tiers) and `legalcode-contract-review`
  (CLARIFY pattern, Glass Box audit trail, Citation Quality Gates, Self-Interrogation,
  Confidence Scoring, Writing Standards)
- All section numbers, penalty thresholds, effective dates, and case citations marked
  [VERIFY] require independent verification against authoritative sources before reliance
