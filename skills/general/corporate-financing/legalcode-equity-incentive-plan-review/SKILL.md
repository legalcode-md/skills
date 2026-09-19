---
name: legalcode-equity-incentive-plan-review
description: Review equity incentive plans — stock option plans (ISO/NSO), RSU plans, RSA plans, phantom
  equity, SARs, and performance share plans — clause-by-clause to flag deviations from market standards,
  generate confidence-scored redlines, and produce an auditable analysis of plan design, 409A compliance,
  vesting mechanics, acceleration triggers, tax treatment, and SEC registration status. Use when reviewing
  a company's stock incentive plan, equity compensation plan, LTIP, management incentive plan, option
  agreement, RSU award agreement, or any equity compensation document.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review equity incentive plans — stock option plans (ISO/NSO), RSU plans, RSA plans, phantom equity, SARs, and performance share plans — clause-by-clause to flag deviations from market standards, generate confidence-scored redlines, and produce an auditable analysis of plan design, 409A compliance, vesting mechanics, acceleration triggers, tax treatment, and SEC registration status. Use when reviewing a company's stock incentive plan, equity compensation plan, LTIP, management incentive plan, option agreement, RSU award agreement, or any equity compensation document. Covers share reserve sizing and evergreen provisions, 409A safe harbor compliance, ISO/NSO distinctions and the $100K annual cap, 83(b) election mechanics, single vs. double trigger acceleration, change-of-control plan treatment, clawback provisions (Dodd-Frank/SOX), plan amendment and termination authority, SEC registration under Form S-8 and Rule 701, and plan administration governance. Jurisdiction-aware for US (IRC §§ 409A/422/83/280G, DGCL, Dodd-Frank/SEC), UK (EMI/CSOP under ITEPA 2003, Companies Act 2006), and international equity sub-plans. GREEN/YELLOW/RED severity classification with specific redline language. Produces a fully diluted dilution model, employee value delivery assessment, tax efficiency analysis, exit scenario walkthrough, and Glass Box audit trail.


# Legalcode Equity Incentive Plan Review

> **Disclaimer**: This skill provides a framework for AI-assisted equity plan review. It does
> not constitute legal, tax, or securities advice. All outputs must be reviewed by a qualified
> attorney and tax professional licensed in the relevant jurisdiction before any reliance or
> action. Laws, regulations, and IRS/HMRC guidance change; verify current applicability before
> relying on any provision described here. Statutory and case law references cited from memory
> carry hallucination risk — verify against authoritative sources. Nothing here constitutes
> securities advice under the Securities Exchange Act, advice regarding registered securities
> offerings, or ERISA plan advice.

---

## Purpose and Scope

This skill reviews equity incentive plans and related award documents against market standards
and applicable law. It identifies design deficiencies, drafting gaps, and compliance risks,
then generates actionable recommendations.

**Covers:**

- Stock option plans (ISO and NSO), RSU plans, RSA plans, SARs, and phantom equity plans
- IRC § 409A compliance analysis for deferred compensation elements
- ISO qualification under IRC § 422 including the $100K annual limit
- Vesting schedule design: cliff, graded, milestone, and hybrid
- Acceleration triggers: single-trigger, double-trigger, and hybrid mechanics
- Change-of-control plan treatment: assumption, substitution, and cash-out
- Post-termination exercise windows and treatment of vested/unvested awards
- Share reserve sizing, evergreen (automatic replenishment) provisions, and dilution impact
- 83(b) election availability and mechanics for restricted stock
- Clawback / recoupment provisions under Dodd-Frank §954 and SOX §304
- Plan administration governance: committee authority, delegation, and conflicts of interest
- SEC registration: Form S-8 eligibility and Rule 701 exemption thresholds
- UK Enterprise Management Incentives (EMI) and Company Share Option Plans (CSOP)
- International sub-plan design and multi-jurisdiction compliance flags

**Does not:**

- Draft new equity plans (use a drafting-specific skill)
- Provide tax advice or model individual tax outcomes
- Value shares or compute FMV (requires a 409A valuation provider)
- Advise on ERISA pension or welfare plan compliance (different regime entirely)
- Review public company proxy disclosure (CD&A narrative)
- Provide securities law advice on authorized offerings or prospectus requirements

---

## Jurisdiction and Governing Law

This skill is jurisdiction-aware with three primary tracks:

**US Track (primary):**

- IRC §§ 83, 422, 409A, 280G, and 4999 (tax compliance and golden parachute rules)
- DGCL §§ 151, 157, 161 (share authorization and option authority) [VERIFY]
- Exchange Act §§ 10(b)/10D and SEC Rule 10D-1 (Dodd-Frank clawback) [VERIFY]
- Securities Act §§ 4(a)(2), Rule 701, Form S-8 (registration exemptions)
- Dodd-Frank Wall Street Reform Act §954 (enhanced clawback for listed companies) [VERIFY]

**UK Track:**

- Income Tax (Earnings and Pensions) Act 2003 (ITEPA 2003) Sch. 5 (EMI) and Sch. 4 (CSOP) [VERIFY]
- Companies Act 2006 §§ 549–551, 560–577 (share allotment authority and pre-emption rights) [VERIFY]
- Employment Rights Act 1996 (impact on vesting and termination treatment)
- HMRC technical guidance: Share Schemes Manual (ESSUM) [VERIFY — check currency]

**International Track:**

- Sub-plan design principles for non-US/UK participants
- [JURISDICTION-SPECIFIC] securities law registration obligations by country
- [JURISDICTION-SPECIFIC] foreign exchange control approvals (India: FEMA; China: SAFE)
- [JURISDICTION-SPECIFIC] payroll withholding and social charge obligations

[JURISDICTION-SPECIFIC] Before delivering any analysis involving non-US or non-UK participants,
identify the applicable local law and flag country-specific compliance issues. Each jurisdiction
has different income recognition events, withholding triggers, and securities registration requirements.

---

## Interactive Clarification

This skill uses **⟁ CLARIFY** at key decision points. Rather than assuming intent, the workflow
pauses and asks when:

- The answer would change the direction of the analysis
- Multiple valid approaches exist and user's preference matters
- Risk classification depends on context not yet provided
- Tax or securities law analysis requires fact-specific information

Present structured options wherever possible. If the user has already provided the information,
skip the question and proceed. State all assumptions explicitly.

---

## Workflow

### Step 1: Accept the Plan Document

Accept the equity plan in any of these formats:

- **File**: PDF, DOCX, or other document format uploaded to the conversation
- **URL**: Link to the plan in a document management system, data room, or cloud storage
- **Pasted text**: Plan text pasted directly into the conversation
- **Multiple documents**: Master plan + form award agreements + board/committee resolutions

If no document is provided, prompt the user to supply one.

**⟁ CLARIFY** — At the outset, identify what documents are available:

- Is this the master plan document only, or are there also form award agreements (option agreement,
  RSU award agreement), vesting schedules, or exhibits?
- Are there board or compensation committee resolutions authorizing specific grants or amendments?
- Are there sub-plans for non-US participants?
- Is there a prior 409A valuation report for reference?

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask these questions. Present as structured options:

1. **Which perspective are you reviewing from?**
   - Options: **Company/Plan Sponsor** (designing or reviewing own plan), **Participant/Employee**
     (evaluating grants received), **Acquirer/Investor** (diligence on target company equity),
     **Outside Counsel** (advising company or participant)
   - _Why this matters_: The analysis emphasis shifts entirely. Participants care about treatment
     on termination and exit. Acquirers care about dilution and acceleration triggers.

2. **Company stage and status?**
   - Options: Pre-revenue startup, Series A–C stage (VC-backed), Late-stage pre-IPO,
     Public company, Post-acquisition integration
   - _Why this matters_: Market standards for pool size, vesting, acceleration, and exercise
     windows vary by stage. 409A valuation approaches also differ.

3. **Primary concerns for this review?**
   - Options: 409A compliance risk, ISO qualification issues, Vesting/acceleration design,
     Change-of-control treatment, Dilution and pool sizing, Clawback provisions,
     UK EMI/CSOP qualification, International sub-plan compliance, Full plan review
   - Allow multiple selections.
   - _Why this matters_: Prioritizes the analysis depth on what matters most to the user.

4. **Is this a review of an existing plan, a proposed amendment, or initial plan adoption?**
   - Options: Existing plan in operation, Proposed plan amendment (specific provisions),
     Initial plan being adopted, Plan refresh for IPO readiness, Acquisition diligence
   - _Why this matters_: Determines whether to compare against prior versions and flag
     what is changing.

5. **What is the governing law of the company's incorporation?**
   - Options: Delaware, Other US state, England & Wales, Other UK, Non-US/UK
   - _Why this matters_: Share authorization and option authority rules are state/jurisdiction
     specific. DGCL § 157 (Delaware) governs differently than other states.

If partial context is provided, proceed with assumptions stated explicitly.

### Step 3: Load Playbook or Standards Baseline

Check for the organization's equity compensation playbook in local configuration files
(e.g., `equity.local.md` or similar).

If no playbook is configured:

**⟁ CLARIFY** — Inform the user and ask:

- **Option A: Establish standards now** — Define the company's preferred positions on key
  elements (pool size, vesting schedule, acceleration, post-termination exercise windows).
  Produces more precise analysis.
- **Option B: Market standards by stage** — Use comparable-company market data (e.g.,
  Radford/AON, Compensia, Carta data) as the baseline. Note the company's stage.
- **Option C: Provide positions as we go** — Start the review and ask about preferred
  positions at each relevant clause.

Label the review clearly if proceeding without a playbook: "Reviewed against market standards
for [stage] stage company — not organizational positions."

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Identify the governing law from the plan document and the company's jurisdiction of
incorporation. Then use **legalcode-mcp** to build a working legal reference for this review.

**Research targets for US plans:**

- IRC § 409A final regulations (Treas. Reg. §§ 1.409A-1 through 1.409A-4) and any recent IRS guidance
- IRC § 422 requirements for ISO qualification (including §422(d) $100K annual limit and holding
  periods under §422(a)(1))
- IRC § 83 income inclusion rules and §83(b) election mechanics and deadline
- IRC § 280G golden parachute excess parachute payment test and §4999 excise tax
- DGCL § 157 option authority and § 161 share issuance authority
- SEC Rule 701 thresholds for private companies (aggregate sales threshold, financial
  disclosure trigger)
- Exchange Act Rule 10D-1 and SEC final clawback rules (effective October 2022)
- Dodd-Frank Act § 954 listing standards compliance for listed companies

**Research targets for UK plans:**

- ITEPA 2003 Schedule 5 (EMI): working time requirement (25h/75%), £30,000 individual
  limit per employee, £3 million company aggregate limit, disqualifying events
- ITEPA 2003 Schedule 4 (CSOP): £60,000 individual option limit (increased April 2023),
  qualifying share requirements, three-year exercise window
- HMRC ESSUM (Share Schemes Manual): notification deadlines, annual returns (Employment
  Related Securities return)
- Companies Act 2006 §§ 549–551: shareholders' authority to allot shares and pre-emption
  rights

Save relevant results to `/tmp/legalcode-equity-plan-authority.md`.

**If legalcode-mcp is not connected:**

- Mark every statutory and case law reference with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Flag that tax law citations require independent verification with qualified tax counsel
- Proceed with the analysis using the frameworks in this skill, with heightened reliance on
  [VERIFY] markers

### Step 5: Build Plan Architecture Overview

Before clause-by-clause analysis, map the plan's architecture:

| Parameter                       | Plan Provision                                 | Market Standard (by Stage)                                  | Assessment         |
| ------------------------------- | ---------------------------------------------- | ----------------------------------------------------------- | ------------------ |
| Plan type                       | [ISO/NSO/RSU/RSA/SAR/Phantom]                  | Option plan (seed-Series B); RSU (Series C+/public)         | [GREEN/YELLOW/RED] |
| Total authorized share pool     | [shares / % FDC]                               | 10–15% FDC (Series A); 5–8% (Series C+)                     | [GREEN/YELLOW/RED] |
| Evergreen provision             | Yes / No / [%/year]                            | Common pre-IPO; less common post-IPO                        | [GREEN/YELLOW/RED] |
| Exercise price methodology      | FMV on grant date / formula / board discretion | 409A FMV (US); market value (UK)                            | [GREEN/YELLOW/RED] |
| Vesting schedule (standard)     | [yr/cliff details]                             | 4yr / 1yr cliff (US); 3yr / 1yr cliff (UK EMI)              | [GREEN/YELLOW/RED] |
| Acceleration (single/double)    | [trigger type]                                 | Double-trigger (CoC + involuntary termination)              | [GREEN/YELLOW/RED] |
| Post-termination exercise (NSO) | [days/months]                                  | 90 days (standard) / 3–12 months (generous)                 | [GREEN/YELLOW/RED] |
| Post-termination exercise (ISO) | [days]                                         | 90 days post-termination (IRC § 422 requirement)            | [GREEN/YELLOW/RED] |
| Plan term (expiration)          | [years]                                        | 10 years from adoption                                      | [GREEN/YELLOW/RED] |
| Amendment authority             | Board / shareholders / committee               | Board for most; shareholder approval for material expansion | [GREEN/YELLOW/RED] |
| ISO vs. NSO designation         | Explicit / board discretion                    | Explicit at grant (for 409A and ISO compliance)             | [GREEN/YELLOW/RED] |
| Clawback provision              | Dodd-Frank/SOX compliant / absent              | Required for listed companies (listed: RED if absent)       | [GREEN/YELLOW/RED] |
| 409A compliance language        | Present / absent / general                     | Explicit § 409A savings clause and FMV methodology          | [GREEN/YELLOW/RED] |

Flag RED items in the overview before proceeding to detailed analysis.

### Step 6: Read the Plan Holistically

Before clause-by-clause analysis:

- Read the entire plan document (including all exhibits, schedules, and form award agreements)
- Identify cross-references between sections (e.g., vesting acceleration referencing the
  "Cause" definition in termination provisions)
- Note how the plan interacts with the company's charter, bylaws, and any existing
  investor rights agreement, right of first refusal, or co-sale provisions
- Count authorized shares and confirm alignment with the company's capitalization table

**⟁ CLARIFY** — For complex plans (50+ pages, multiple exhibit suites, sub-plans):

- Full review of all 12 clause categories, or **priority review** focused on user's stated
  concerns from Step 2?
- Are form award agreements being reviewed as an integrated set, or is only the master
  plan document in scope?
- Does the review extend to any applicable capitalization table to assess dilution impact?

### Step 7: Clause-by-Clause Analysis

Analyze all 12 clause categories below. For each:

- Assess against the playbook or market standards
- Note whether the clause is present, absent, or unusual
- Apply GREEN/YELLOW/RED classification
- For YELLOW/RED: generate specific redline language using the format in the Redline section

| #   | Clause Category                       | Depth    | Key Review Points                                                                     |
| --- | ------------------------------------- | -------- | ------------------------------------------------------------------------------------- |
| 1   | Plan Purpose, Authority & Eligibility | Deep     | Board/stockholder authorization, eligible participants, securities law compliance     |
| 2   | Share Reserve & Evergreen             | Deep     | Pool size, replenishment mechanics, recycling provisions, dilution impact             |
| 3   | Award Types & Design                  | Deep     | ISO/NSO distinction, RSU/RSA structure, SAR/phantom equity mechanics                  |
| 4   | Exercise Price & 409A Compliance      | Deep     | FMV methodology, safe harbor, pricing of different award types                        |
| 5   | Vesting Schedules & Cliffs            | Deep     | Time-based vesting, milestone vesting, cliff duration, acceleration mechanics         |
| 6   | Change-of-Control & Acceleration      | Deep     | Single/double trigger, definition of CoC, assumption vs. cash-out, 280G interaction   |
| 7   | Post-Termination Exercise Windows     | Deep     | Treatment by termination reason (cause, without cause, death, disability, retirement) |
| 8   | Plan Amendment & Termination          | Deep     | Board vs. stockholder approval triggers, materiality threshold, participant consent   |
| 9   | Plan Administration & Governance      | Standard | Committee authority, delegation, conflict of interest, decisions as final             |
| 10  | Tax Compliance Provisions             | Standard | 409A savings clause, withholding mechanics, ISO holding period notices                |
| 11  | Clawback & Recoupment                 | Standard | Dodd-Frank/SOX compliance, scope, trigger events, disgorgement mechanics              |
| 12  | Securities Law & Registration         | Standard | Rule 701 / Form S-8 eligibility, legends, lock-up, transferability restrictions       |

### Step 8: Missing Clause Detection

After analyzing present clauses, check for important provisions that are entirely absent.

**Common critical absences (RED):**

- No definition of "Change of Control" — ambiguity creates exit disputes and litigation risk
- No IRC § 409A savings / compliance language in a plan covering US participants
- No vesting schedule (or vesting left entirely to award agreement without plan-level constraints)
- No post-termination exercise provision — creates indefinite options and tax issues
- No plan expiration date — mandatory for ISO compliance (IRC § 422(b)(5): 10-year limit)
- No clawback provision for an SEC-listed company — Exchange Act Rule 10D-1 compliance required
- No share reserve or authorized share count — fundamental plan validity question

**Common important absences (YELLOW):**

- No acceleration provision — retention risk in M&A or leadership change scenarios
- No "Cause" definition — creates disputes and inconsistent administration
- No "Good Reason" definition — participants cannot protect against constructive termination
- No plan-level adjustment mechanics — no protection against dilutive transactions
- No disability or death treatment provisions — creates gap in unusual terminations
- No ISO $100K limit tracking language — ISO grants in excess of limit convert to NSOs silently
- No committee composition / independence requirements — governance gap for public companies
- No sub-plan authorization language for non-US participants — blocks international grants

**⟁ CLARIFY** when severity depends on context:

- "This plan has no acceleration provision. Is retention through an M&A or leadership change
  a priority for this company? If yes, this is a YELLOW gap. If retention is handled by
  separate agreement, note and proceed."
- "There is no Dodd-Frank clawback provision. Is this company listed on a national securities
  exchange? If yes, this is a RED gap — Exchange Act Rule 10D-1 compliance required."

### Step 9: Classify Deviations and Generate Redlines

Use the **Deviation Severity Classification** (below) to classify each deviation.

For each YELLOW and RED deviation, generate a redline using the **Redline Format** (below).

**⟁ CLARIFY** for borderline classifications:

- "The post-termination exercise window for NSOs is 3 months (market standard). For a
  company that retains strong employees post-departure, should this be treated as GREEN
  (market standard) or YELLOW (consider extending to 6–12 months for retention signaling)?"
- "The acceleration clause is single-trigger only (Change of Control with no termination
  requirement). Single trigger is common for founders and executives at seed stage, but
  creates IRC § 280G exposure. Should I classify as YELLOW (recommend review) or RED
  (requires 280G analysis before IPO)?"

### Step 10: Dilution and Equity Impact Analysis

After clause analysis, model the equity dilution impact:

**Dilution table:**
| Category | Shares | % FDC |
|----------|--------|-------|
| Common stock (issued) | [shares] | [%] |
| Options outstanding (vested) | [shares] | [%] |
| Options outstanding (unvested) | [shares] | [%] |
| RSUs outstanding | [shares] | [%] |
| Plan pool (unallocated reserve) | [shares] | [%] |
| Warrants and convertible instruments | [shares] | [%] |
| **Total fully diluted** | [shares] | 100% |

**Metrics to calculate:**

- **Pool utilization**: Options/RSUs granted as % of plan pool authorized
- **Burn rate**: Annual grants as % of total shares outstanding
- **Dilution from full pool**: If all remaining pool were granted and exercised, total
  dilution impact on existing holders
- **Overhang**: (Options outstanding + pool remaining) ÷ total shares outstanding

**⟁ CLARIFY** — If the capitalization table is not available:

- "Provide a cap table or share count to compute dilution metrics. Without it, I can
  assess plan design but cannot compute the actual dilution footprint."

### Step 11: Exit Scenario Analysis

Model plan treatment in three representative exit scenarios:

**Scenario A — Acquirer assumes the plan (share-for-share roll-over):**

- How does the plan address assumption? Is it mandatory, discretionary, or silent?
- Will unvested awards continue vesting under the acquirer's schedule?
- Are acceleration provisions triggered by the assumption itself (single trigger)?
- Employee outcome: equivalent unvested equity in acquirer; continued vesting

**Scenario B — Cash-out on acquisition:**

- How does the plan address cash settlement? Is the company required to cash out?
- What price applies for in-the-money options (typically merger consideration per share)?
- Are underwater options cancelled without consideration?
- Employee outcome: immediate liquidity for vested in-the-money awards; unvested awards
  may be accelerated (if double trigger satisfied) or forfeited

**Scenario C — IPO (plan conversion and registration):**

- Does the plan's term accommodate post-IPO grants?
- Is the plan designed for Form S-8 registration eligibility?
- Does the plan include "lock-up" provisions aligning with underwriter requirements?
- Do evergreen provisions comply with investor expectations post-IPO?
- Employee outcome: options/RSUs converted to tradeable securities subject to lock-up

### Step 12: Quality Verification

Before delivering the analysis:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every RED-classified item, run the 3-pass Self-Interrogation. Revise if any pass
   reveals a weakness.
3. Assign Confidence Scores to each material clause analysis.
4. Verify completeness: confirm all 12 clause categories have been addressed.
5. Generate the Glass Box Audit Trail and append to the output.

---

## Clause Analysis Reference

### 1. Plan Purpose, Authority & Eligibility

**Key elements to review:**

- Whether the plan document recites stockholder approval or board authorization as the
  source of authority for issuance
- Eligible participants: employees only, or also directors, consultants, advisors?
- ISO eligibility: ISOs can only be granted to employees (not consultants or directors
  who are not employees) under IRC § 422(b)(1)
- Whether the participant definition aligns with Rule 701 or Form S-8 eligibility
- Whether the plan acknowledges it is not an ERISA "employee benefit plan" (important
  distinction — discretionary equity plans are generally not subject to ERISA Title I)

**Common issues:**

- Participant definition that includes consultants for ISO grants — ISOs to non-employees
  are void; they convert to NSOs (or result in 409A issues if not corrected)
- No reference to stockholder approval — necessary for ISO qualification and for many
  exchange listing standards
- Overly broad participant class creating Rule 701 exemption calculation complexity

[JURISDICTION-SPECIFIC] **UK EMI eligibility requirements:**

- Company must not be under the control of another company (independence test)
- Company's gross assets must not exceed £30 million [VERIFY — check currency]
- Employee must work at least 25 hours per week OR (if less) at least 75% of working time
  for the company (working time requirement)
- Individual grant limit: £250,000 in unexercised options at any time [VERIFY]
- Company limit: £3 million total unexercised EMI options outstanding at any time [VERIFY]
- Employees on EMI must not hold more than 30% of ordinary share capital at the time of grant

[JURISDICTION-SPECIFIC] **UK CSOP eligibility:**

- £60,000 individual limit (increased from £30,000 effective April 6, 2023) [VERIFY]
- Options must be exercisable between 3 and 10 years from grant
- Shares must be fully paid up, not redeemable, and not subject to restrictions (other than
  limited pre-emption or forfeiture provisions)

### 2. Share Reserve & Evergreen Provisions

**Key elements to review:**

- Total shares authorized under the plan (absolute number and as % of fully diluted)
- Whether shares that are cancelled, forfeited, or expire unexercised are returned to the pool
  (recycling provision)
- Whether shares withheld for tax or exercise price payment are returned to the pool
- Evergreen / automatic replenishment: percentage of outstanding shares added annually,
  and whether there is a cap on annual additions
- Separate ISO sub-limit (if any): ISOs cannot be granted in excess of the number of shares
  authorized for ISO grants under IRC § 422

**Common issues:**

- Pool size significantly below market for company stage — insufficient runway for grants
- Evergreen percentage so large it creates material annual dilution without stockholder approval
- No recycling of forfeited/cancelled awards — leaves pool stranded
- Shares withheld for tax purposes not returned to the pool — reduces available pool faster
  than necessary
- Missing ISO sub-limit when plan authorizes ISO grants — required for ISO compliance
- No cap on total shares issuable as ISOs across all grant years

**Market standards by stage:**
| Stage | Pool % FDC | Evergreen (typical) |
|-------|-----------|---------------------|
| Seed / Pre-Series A | 15–20% | None (common) |
| Series A | 10–15% | 5% per year (sometimes) |
| Series B–C | 8–12% | 3–5% per year |
| Late-stage pre-IPO | 5–8% | 3–5% per year |
| Post-IPO | 1–3% annual replenishment | 1–2% or none |

[JURISDICTION-SPECIFIC] Post-IPO evergreen provisions must comply with ISS and Glass Lewis
institutional proxy voting policies. Many institutional investors oppose automatic evergreen
provisions that replenish shares without annual stockholder approval.

### 3. Award Types & Design

**Key elements to review:**

**Stock Options (ISO and NSO):**

- Whether the plan explicitly authorizes both ISO and NSO grants and allows the grant
  instrument to specify which type is being granted
- ISO designation must be made at grant — retroactive conversion is not permitted
- NSOs may be granted to any participant (employees, consultants, directors)
- Exercise price for ISOs must equal at least 100% FMV at grant date (110% for 10%+ stockholders)
- ISO exercise period cannot exceed 10 years from grant (5 years for 10%+ stockholders)
- $100K annual limit (IRC § 422(d)): ISOs first exercisable in any calendar year cannot
  exceed $100K in value (measured at grant-date FMV). Options above the limit are treated
  as NSOs. Whether the plan includes tracking language or notice to participants

**Restricted Stock Units (RSUs):**

- RSUs are unfunded promises to deliver shares on a future date — they are "deferred
  compensation" and must comply with IRC § 409A if settlement is deferrable
- Standard market design: RSUs settle (shares delivered) on vesting — this design
  avoids § 409A classification as deferred compensation
- Settlement timing: If settlement occurs more than 2½ months after year-end of the year
  in which the RSU vests, § 409A applies and must be satisfied
- No exercise price required (and none should be set)

**Restricted Stock Awards (RSAs):**

- RSAs involve actual share issuance at a nominal or FMV price, subject to forfeiture
  restrictions that lapse over time
- The § 83(b) election opportunity is significant: participants can elect to include
  the spread in income at grant date rather than at vesting. Election must be filed within
  30 days of the transfer (IRC § 83(b)). The plan should inform participants of this right.
- After an 83(b) election, subsequent appreciation is taxed at long-term capital gains rates
  if shares are held for more than 1 year from the 83(b) election date

**Stock Appreciation Rights (SARs):**

- SARs grant the right to receive the appreciation in share value above a base price,
  payable in cash or shares
- Cash-settled SARs: classified as deferred compensation under § 409A — must comply
- Stock-settled SARs with a base price equal to or greater than FMV at grant: exempt from
  § 409A (like a stock option)
- Phantom equity: typically cash-settled; § 409A compliance is mandatory

**Common issues:**

- Plan does not distinguish between ISO and NSO — creates ambiguity and potential § 409A issues
- RSUs with deferral elections or settlement timing that triggers § 409A without compliance language
- RSAs issued without § 83(b) election information — participants miss the election window
- Cash-settled SARs or phantom equity without § 409A compliance mechanism

### 4. Exercise Price & 409A Compliance

**Key elements to review:**

- How is "Fair Market Value" defined in the plan?
- For private companies: does the FMV methodology satisfy the § 409A safe harbor?
- For public companies: does FMV mean closing price, average of high and low, or other?
- Is there a specific 409A savings clause?
- How does the plan address options granted between 409A valuations (staleness risk)?

**IRC § 409A Safe Harbor Requirements (private companies) [VERIFY]:**
The IRS provides three safe harbors for private company FMV determination:

1. **Independent appraisal safe harbor**: Qualified independent appraisal performed within
   12 months preceding the grant date, following the reasonable application of a recognized
   valuation method (Treas. Reg. § 1.409A-1(b)(5)(iv)(B))
2. **Formula safe harbor**: Good faith, reasonable formula consistently applied, using
   reasonably available information
3. **Illiquid startup safe harbor**: Applies to companies less than 10 years old with no
   readily tradeable securities and no IPO or acquisition in the next 12 months (Treas. Reg.
   § 1.409A-1(b)(5)(iv)(B)(2)) [VERIFY]

**Consequences of 409A noncompliance:**

- Immediate income inclusion for all affected deferred compensation in the year of vesting
- Interest on underpayments
- Additional 20% penalty tax on the amount included in income (IRC § 409A(a)(1)(B))
- Potential for IRS audit and significant participant tax liability — often discovered at IPO
  or acquisition

**Common issues:**

- FMV definition refers to "board determination" without a methodology — fails the safe harbor
- Plan does not require updating the 409A valuation after material events (fundraising round,
  M&A activity, business change) — creates staleness risk
- Valuation performed more than 12 months before grant date — outside safe harbor window
- No 409A savings clause — if any provision is noncompliant, no mechanism to cure

**409A Savings Clause — Market Standard Language:**

> "Notwithstanding anything in this Plan to the contrary, this Plan shall be interpreted,
> administered, and construed in a manner that does not result in the imposition of additional
> taxes, penalties, or interest under Section 409A of the Code. If any award is subject to
> Section 409A, the Plan and the applicable award agreement shall be administered in accordance
> with Section 409A. Any provision that would constitute a violation of Section 409A shall be
> disregarded to the extent necessary to comply with Section 409A."

[JURISDICTION-SPECIFIC] **UK plans:** Exercise price must equal "market value" at grant date
to qualify for EMI or CSOP income tax advantages. HMRC must approve a "Unrestricted Market
Value" (UMV) or "Actual Market Value" (AMV) for private companies. ESSUM guidance applies.

### 5. Vesting Schedules & Cliffs

**Key elements to review:**

- Standard vesting schedule: 4-year with 1-year cliff is the dominant US market standard
- Whether the plan sets minimum vesting requirements or leaves it entirely to award agreements
- Milestone-based vesting: how are milestones defined, by whom, and when assessed?
- Whether unvested awards are forfeited on termination (standard) or continue in some cases
- Treatment of vesting upon death or disability

**Market standards by participant type:**
| Participant | Typical Vesting | Cliff | Acceleration |
|-------------|----------------|-------|--------------|
| Employee (standard) | 4 years | 1 year | Double-trigger on CoC |
| Founder (early) | 4 years | Sometimes waived for prior service credit | Full or partial single-trigger |
| Executive hire | 4 years | 1 year | Double-trigger; sometimes enhanced severance |
| Non-employee director | 1 year or monthly | Often no cliff | Single-trigger on CoC (common for directors) |
| Consultant/advisor | 1–2 years | Varies | Varies |

**Common issues:**

- No cliff at all — immediate vesting allows participants to vest and depart quickly
- Cliff longer than 1 year — creates retention risk when participants leave just before cliff
- Performance vesting with no objectively determinable milestones — creates § 409A risk if
  vesting determination is discretionary
- No disability treatment provision — creates gap for long-term disability situations

[JURISDICTION-SPECIFIC] **UK EMI:** No mandatory vesting schedule, but HMRC requires that
the exercise conditions be objective and determinable. Purely discretionary vesting by employer
can create income tax and NIC issues at exercise.

### 6. Change-of-Control & Acceleration

**Key elements to review:**

**Definition of "Change of Control":**

- A clear, well-defined CoC definition is critical — ambiguity creates disputes at exit
- Market standard elements: (1) acquisition of >50% of voting power; (2) sale of all or
  substantially all assets; (3) merger or consolidation where existing stockholders hold
  <50% of the surviving entity
- Watch for formulations that: capture small minority acquisitions, are triggered by Board
  changes alone without ownership change, or fail to cover asset sales

**Acceleration Mechanics:**

| Type                     | Description                                                                                         | Typical Use                      | 280G Risk                                 |
| ------------------------ | --------------------------------------------------------------------------------------------------- | -------------------------------- | ----------------------------------------- |
| **Single-trigger**       | Acceleration on CoC alone                                                                           | Founders; non-employee directors | Higher (especially for large grants)      |
| **Double-trigger**       | Acceleration requires both CoC AND qualifying termination within specified window (e.g., 24 months) | Standard for employees           | Lower (reduced excess parachute exposure) |
| **Partial acceleration** | Fixed % (e.g., 25–50%) accelerates on CoC; remainder on qualifying termination                      | Hybrid approach                  | Moderate                                  |
| **No acceleration**      | Unvested awards assumed or converted                                                                | Lean plan design                 | Minimal                                   |

**Qualifying termination (second trigger):**

- Typically: involuntary termination Without Cause, or resignation for Good Reason
- "Good Reason" definition is critical — should include: material reduction in compensation,
  material diminution in duties/authority, required office relocation beyond a threshold
  distance, acquirer's failure to assume the plan
- Watch for "Good Reason" defined so narrowly that constructive termination is not captured

**IRC § 280G golden parachute considerations:**

- Excess parachute payments (parachute payments exceeding 3× the individual's "base amount")
  trigger: (1) non-deductibility for the company and (2) 20% excise tax for the individual
- Equity acceleration is a "parachute payment" — must be included in the 280G analysis
- Best practice: plan should either include a Section 280G "best net" or "safe harbor cutback"
  provision, or specifically permit a 280G tax gross-up (rare post-2012 for general employees)
- Plans without any 280G provision leave participants and the company exposed

**Common issues:**

- No definition of "Change of Control" — most common RED finding
- "Change of Control" defined too broadly (e.g., capturing a minority investment)
- Single-trigger full acceleration for all participants — creates 280G exposure at scale
- No "Good Reason" definition or too narrow — fails to protect participants on constructive
  termination post-acquisition
- Acceleration provision that conflicts with acquirer assumption obligations — creates tension
  with deal mechanics

### 7. Post-Termination Exercise Windows

**Key elements to review:**

- ISO exercise window after termination: IRC § 422(a)(2) requires exercise within 3 months
  after termination of employment to retain ISO status. Exercise after 3 months converts
  the option to an NSO.
- NSO exercise window: no statutory requirement; market standard is 90 days for termination
  without cause and immediate forfeiture on termination for cause
- Treatment on death: typically 12 months from date of death for estate to exercise
- Treatment on disability: typically 12 months from date of disability
- Treatment on retirement: varies; some plans extend to option expiration
- Post-termination period for options subject to company repurchase right (for unvested shares
  converted on exercise)

**Extended post-termination windows (trend):**
An increasing number of high-profile companies extend NSO post-termination windows from
90 days to 5–10 years after termination (notably Quora, Stripe, Asana pre-IPO). This
increases participant tax flexibility by allowing NSOs to remain outstanding until a liquidity
event. The primary considerations:

- NSOs exercised after 90 days post-termination (for former employees) retain NSO character —
  no ISO treatment issue since the option is already NSO after the ISO window closes
- Extended windows must comply with the plan's expiration date (typically 10 years from grant)
- 409A impact: if a stock option has an exercise price equal to or greater than FMV at grant,
  the post-termination window length does not trigger § 409A regardless of length [VERIFY]

**Termination reason matrix:**
| Termination Reason | Typical Vested Option Window | Unvested Awards |
|--------------------|----------------------------|-----------------|
| Voluntary resignation | 90 days (NSO); ISO window closes at 90 days | Forfeited |
| Involuntary (Without Cause) | 90 days to 1 year | Forfeited |
| For Cause | Immediate forfeiture (0 days) | Forfeited |
| Death | 12 months (estate) | Accelerated or forfeited per plan |
| Disability | 12 months | Accelerated or forfeited per plan |
| Retirement | Plan term / varies | Varies |

**Common issues:**

- No differentiation by termination reason — same window for "for cause" as for "without cause"
  (punitive for affected participants; not market standard)
- ISO window stated as longer than 3 months — this is a drafting error; options exercised after
  3 months post-termination lose ISO status but can still be exercised as NSOs; plan language
  should acknowledge the ISO/NSO reclassification
- "Cause" defined so broadly that routine performance issues trigger immediate forfeiture

### 8. Plan Amendment & Termination

**Key elements to review:**

- Which body has authority to amend (Board, Compensation Committee, stockholders)?
- When is stockholder approval required for amendments?
  - Exchange listing standards (NYSE/Nasdaq) require stockholder approval for: material
    increases in plan shares, extension of option terms, reduction of exercise prices
    (repricing), changes to eligible participants in a way that expands the class materially
  - ISO qualification: plan term cannot exceed 10 years unless reapproved by stockholders
  - Rule 701: if aggregate sales cause the company to exceed the Rule 701 threshold, revised
    disclosures and potentially registration may be required without formal plan amendment
- Whether participant consent is required for adverse amendments affecting outstanding awards
- Plan expiration date: without a 10-year term, ISO grants are not valid under IRC § 422(b)(5)
- No-repricing provision: most well-drafted modern plans prohibit reducing exercise prices
  without stockholder approval (prevents dilutive repricing)

**Common issues:**

- No plan expiration date — ISO invalidity risk for grants made under an expired plan
- Board can amend without any participant consent rights — particularly problematic if plan
  allows retroactive reduction of exercise prices or forfeiture of vested awards
- No anti-repricing provision — allows board to reduce exercise prices without stockholder
  approval (governance/dilution concern; required for Nasdaq/NYSE compliance)
- Amendment provision allows board to add shares to the plan without stockholder approval
  beyond evergreen — may conflict with exchange listing standards
- Broad board discretion to terminate plan and cancel all outstanding awards — no participant
  protection

### 9. Plan Administration & Governance

**Key elements to review:**

- Who administers the plan? Board, Compensation Committee, or delegated authority?
- For public companies: compensation committee composition and independence requirements
  (NYSE/Nasdaq listing standards; SEC Rule 16b-3 for Section 16 compliance)
- Delegation of authority to CEO or officers for grants below a size threshold?
- Committee's authority described as final and binding (standard language to limit litigation)
- Expenses of plan administration — borne by company or participants?
- Clawback/forfeiture authority — can the committee claw back awards for cause or misconduct?

**Market standards:**

- Pre-IPO: Board or sub-committee of independent directors
- Post-IPO: Independent Compensation Committee (meeting NYSE/Nasdaq independence standards)
- SEC Rule 16b-3 safe harbor: for insiders (officers and directors), grants should be approved
  by the full board or a committee of two or more non-employee directors to receive Section 16
  exemption [VERIFY]

**Common issues:**

- No committee independence requirements (RED for listed companies)
- Unlimited delegation to management with no grant size cap
- No conflicts-of-interest provision preventing self-dealing on grants
- Administrator decisions not expressly stated as final and binding — creates litigation risk

### 10. Tax Compliance Provisions

**Key elements to review:**

- **409A savings clause**: See Section 4 above
- **Withholding authorization**: Does the plan authorize the company to withhold from any
  payment, or require the participant to make arrangements for tax withholding?
- **ISO holding period notification**: Does the plan or award agreement require participants
  to notify the company of a disqualifying disposition (sale before 2-year holding from grant
  or 1-year from exercise)? Required for the company to report/withhold accurately.
- **$100K ISO limit tracking**: Does the plan include tracking or notice provisions to
  identify when ISO grants in a given year exceed the § 422(d) limit and convert to NSOs?
- **83(b) election notice for RSAs**: Does the plan or award agreement inform participants
  of the 83(b) election option and the 30-day filing deadline?
- **Section 280G compliance language**: In plans with single-trigger acceleration,
  does the plan include a 280G "best net" or safe harbor cutback provision?

**IRC § 422 ISO holding period requirements [VERIFY]:**
To receive ISO tax treatment:

- Participant must hold shares for at least 2 years from the grant date, AND
- At least 1 year from the exercise date
- Disposition before either holding period is a "disqualifying disposition" — ordinary
  income on the spread at exercise (or at sale, if less), company gets a compensation deduction
- Long-term capital gains treatment on post-exercise appreciation is lost

**Common issues:**

- No withholding authorization — company may be unable to net-settle or withhold for taxes
- No disqualifying disposition notification requirement — company may under-withhold for tax
- No ISO $100K tracking — generates silent NSOs without participant notice
- No 83(b) election provision in RSA plan — participants miss the election window inadvertently

[JURISDICTION-SPECIFIC] **UK EMI/CSOP:**

- EMI: Income tax and NIC-free on exercise provided the option was granted with UMV exercise
  price and the holding period post-exercise triggers entrepreneurs' relief (now BADR) —
  generally 2 years from grant date to disposal [VERIFY]
- CSOP: No income tax on exercise (within £60K limit); CGT on disposal; company must register
  with HMRC and file annual ERS returns [VERIFY]
- Annual ERS (Employment Related Securities) return must be filed by 6 July following the end
  of each UK tax year for all share schemes [VERIFY]

### 11. Clawback & Recoupment

**Key elements to review:**

- Does the plan include a clawback/recoupment provision?
- For SEC-listed companies: does the provision comply with Exchange Act Rule 10D-1 (effective
  October 2, 2023 for listed companies adopting the rule, with full enforcement from
  February 2, 2026)? [VERIFY — confirm current effective dates]
- Rule 10D-1 / Dodd-Frank § 954 requirements [VERIFY]:
  - Applies to "executive officers" (as defined)
  - Requires recovery of incentive-based compensation (including equity awards) that was
    received based on attainment of a financial reporting measure
  - Triggered by accounting restatement (both "Big R" restatements and "little r" corrections)
  - Lookback period: 3 years preceding the date of restatement determination
  - Recovery without regard to fault
- SOX § 304 clawback (for CEOs and CFOs only; requires SEC enforcement action) [VERIFY]
- For private companies: clawback provisions less standard but increasingly common for
  senior executives, particularly in VC-backed companies with investor requests

**Common issues:**

- No clawback provision at all for a listed company — RED; Rule 10D-1 requires exchange
  listing rules to enforce clawback policies
- Clawback only triggered by "willful" misconduct — too narrow for Rule 10D-1 compliance
  (Rule 10D-1 requires recovery without fault determination)
- Clawback does not cover equity award value at vesting — only cash bonus; incomplete
- Clawback provision does not specify who determines the restatement-linked recovery amount
- No mechanism for the company to recover shares/proceeds (no disgorgement language)

### 12. Securities Law & Registration

**Key elements to review:**

**Rule 701 (private companies) [VERIFY]:**

- Rule 701 exempts offers and sales of securities to employees, directors, officers, and
  consultants under written compensatory plans from Securities Act registration
- Annual threshold (aggregate sales price): if aggregate sales during a rolling 12-month
  period exceed $10 million [VERIFY — check for inflation adjustments], additional disclosure
  is required within 30 days (including risk factors, financial statements, and plan documents)
- Plan must be a written compensatory plan (the written document requirement)
- Consultants must be natural persons; no contractors providing investor relations services

**Form S-8 (public companies) [VERIFY]:**

- Companies registered under Exchange Act § 12 use Form S-8 to register securities to be
  offered to employees under employee benefit plans
- Form S-8 requires: plan document, reoffer prospectus for resales by affiliates
- Consultants and advisors: S-8 covers securities issued to bona fide consultants and advisors
  who provide genuine services not in connection with capital-raising

**Plan transferability restrictions:**

- Non-qualified options may be transferred to family members or trusts in well-designed plans
- ISOs cannot be transferred (other than by will or laws of descent) — any transfer
  disqualifies the option from ISO treatment
- Whether the plan includes a right of first refusal on shares acquired through option
  exercise (common in private companies; must be exercised within a specified window)

**Common issues:**

- Plan does not acknowledge Rule 701 requirements — creates exposure if aggregate sales
  exceed the threshold without required disclosure
- Form S-8 not filed promptly after IPO — creates resale restrictions and possible violations
- ROFR provision not time-limited — creates indefinite restriction on liquidity
- Consultant grants without bona fide services documentation — Rule 701/S-8 eligibility risk

---

## Deviation Severity Classification

### GREEN — Acceptable

The provision aligns with or exceeds market standards and applicable law. No immediate action required.

**Examples:**

- 4-year vesting with 1-year cliff (market standard)
- Double-trigger acceleration within 24 months following a Change of Control
- 409A savings clause present and complete
- Evergreen provision at 3% of outstanding shares per year with compensation committee discretion
- Post-termination exercise window of 12 months (above standard 90 days — better for employees)
- Plan term of 10 years from board adoption (ISO compliant)

**Action**: Note for awareness. No redline required.

### YELLOW — Negotiate / Amend

The provision falls outside the standard position but within a negotiable range. Requires attention
and likely amendment, but not a critical compliance issue.

**Examples:**

- Vesting cliff of 18 months instead of market-standard 12 months
- Single-trigger acceleration for executive grants without 280G analysis or safe harbor
- Pool size at 7% FDC for a Series A company (below standard 10–15%)
- Post-termination exercise window uniformly 90 days regardless of termination reason
- No "Good Reason" definition — participants lack protection on constructive termination
- No anti-repricing provision — governance concern for listed or pre-IPO companies
- 409A FMV defined as "board determination" without specifying required methodology

**Action**: Generate specific redline language with fallback. Estimate business impact.

### RED — Escalate / Fix Immediately

The provision is outside the acceptable range, likely noncompliant with applicable law, or poses
material risk to the company or participants. Requires counsel review and prompt remediation.

**Examples:**

- No IRC § 409A savings clause in a US plan with deferred compensation elements
- No definition of "Change of Control" — ambiguity at exit creates litigation
- No plan expiration date — ISO grants under an open-ended plan lose ISO qualification
- No clawback provision for an SEC-listed company (Rule 10D-1 compliance gap)
- Exercise price described as "at board discretion" without FMV floor — 409A violation risk
- ISO grants to consultants or non-employees — ISOs are void if granted to non-employees
- RSUs structured to be freely deferrable without § 409A compliance language
- Plan term exceeds 10 years (if ISOs authorized) without stockholder reapproval
- Unlimited repricing authority without stockholder approval for a Nasdaq/NYSE listed company

**Action**: Explain the specific risk with legal basis. Provide market-standard alternative
language. Estimate participant and company exposure. Recommend escalation path.

---

## Redline Format

For each YELLOW and RED deviation, generate a redline using this format:

```
**Clause**: [Section reference and clause name]
**Current language**: "[exact quote from the plan]"
**Issue**: [One sentence identifying the problem]
**Proposed redline**: "[specific alternative language — ready to insert]"
**Rationale**: [1-2 sentences explaining why, suitable for external sharing]
**Legal basis**: [Specific statute, regulation, IRS guidance, or market standard]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative position if primary redline is rejected]
**Tax consequence**: [409A, ISO, 280G, or withholding impact if applicable]
**Confidence**: [Definite / High / Probable / Possible / Unlikely]
```

### Redline Best Practices

1. **Be specific**: Provide exact language, not general guidance. The redline should be
   ready to insert into the plan document.
2. **Be balanced**: Propose language that is firm on legal requirements but commercially
   reasonable. Overly aggressive changes to equity plans can damage employee relations.
3. **Explain the rationale**: Include a brief, professional rationale suitable for sharing
   with the board or outside counsel.
4. **Provide fallback positions**: For YELLOW items, provide an alternative if the primary
   redline is rejected.
5. **Prioritize by legal risk**: Lead with 409A, ISO, and clawback compliance issues (legal
   requirements), then governance improvements, then market standard refinements.
6. **Reference applicable law**: Cite the specific IRC section, IRS regulation, or SEC rule.
   If citing from memory, mark with [VERIFY].
7. **Quantify impact**: When possible, estimate the number of participants affected, the
   potential tax exposure, or the dilution impact.

---

## Negotiation Priority Framework

Organize findings by priority when presenting to the board, compensation committee, or outside
counsel:

### Tier 1 — Must-Haves (Legal Compliance)

Failures to address these create material legal, tax, or regulatory risk:

- IRC § 409A compliance (savings clause, FMV methodology)
- ISO qualification requirements (participant eligibility, exercise price, plan expiration)
- Clawback policy compliance for listed companies (Rule 10D-1)
- No definition of Change of Control when acceleration provisions exist
- Plan authority (no board or stockholder authorization for issuance)

### Tier 2 — Should-Haves (Market Standard Governance)

Material improvements that reduce litigation risk and align with market practice:

- Double-trigger acceleration (vs. single-trigger) for all non-founder participants
- "Good Reason" definition covering constructive termination
- Anti-repricing provision for pre-IPO and post-IPO plans
- 280G best-net or safe harbor cutback provision
- Differentiated post-termination windows by reason for termination

### Tier 3 — Nice-to-Haves (Participant-Friendly Improvements)

Items that improve employee experience and retention signaling, but are not legally required:

- Extended post-termination exercise windows (beyond 90 days) for NSOs
- Enhanced disability and death treatment provisions
- Partial acceleration at time of Change of Control (before the second trigger)
- Broad pool recycling (return of withheld shares to pool)

**Strategy**: Address all Tier 1 items immediately. Trade Tier 3 concessions to secure
Tier 2 wins with the board. Never concede on Tier 1 items without escalation to outside counsel.

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Identify the plan type, reviewer's perspective, company stage, and primary legal
concerns. Classify the plan's complexity (simple option plan, multi-award plan, international
plan with sub-plans).

**DO**: Execute the clause-by-clause analysis and missing clause detection. Generate redlines.
Classify severity. Model dilution and exit scenarios.

**CHECK**: Run the 5 Citation Quality Gates. For any RED item, run the 3-pass Self-Interrogation.
Assign Confidence Scores. Verify all 12 clause categories addressed.

**ACT**: Note any novel patterns (unusual CoC definitions, bespoke acceleration provisions,
emerging market positions on extended exercise windows). Flag for equity plan playbook update.

### Citation Quality Gates

Run these 5 gates silently before delivering any output:

| Gate           | Rule                                                                                                                                                                          | Fail Action                                              |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific IRC section, IRS regulation, SEC rule, or established market standard                                                                      | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format (e.g., IRC § 409A(a)(1); Treas. Reg. § 1.409A-1(b)(5); Exchange Act Rule 10D-1)                                        | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments — IRC § 409A regulations last comprehensively updated 2007; SEC Rule 10D-1 effective 2022; UK CSOP £60K limit changed April 2023 | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the plan's governing law and jurisdiction. No US IRC concepts imported into pure UK plans or vice versa                                                 | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden. 409A tax analysis is highly fact-specific — acknowledge when a professional tax opinion is required                                | Add confidence qualifier                                 |

### Self-Interrogation for RED Items

For any clause classified RED, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity:**

- Does the risk assessment follow logically from the IRC section or SEC rule cited?
- Would the IRS or SEC actually challenge this plan provision under these facts?
- Is there a counter-argument the plan sponsor's counsel will make?

**Pass 2 — Completeness:**

- Have all relevant IRC sections been considered (not just § 409A, but also §§ 83, 422, 280G)?
- Have exchange listing standards been checked alongside SEC rules?
- Are there state law considerations not yet addressed?

**Pass 3 — Challenge:**

- What is the strongest argument that this clause IS acceptable?
- Under what circumstances might a qualified tax attorney accept this design?
- Is the RED classification proportionate to the actual risk, or is this YELLOW with mitigations?

If any pass reveals a weakness, revise before delivery. Record `self_interrogation: PASS` or
`self_interrogation: REVISED` in the Glass Box audit trail.

### Confidence Scoring

Assign a confidence level to each material clause analysis:

| Level        | Range     | Meaning                                          | Action                                                    |
| ------------ | --------- | ------------------------------------------------ | --------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, clear statute, no ambiguity         | State with confidence                                     |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions | State with brief caveat                                   |
| **Probable** | 0.60–0.79 | Good arguments, reasonable minds could differ    | State with explicit reasoning                             |
| **Possible** | 0.40–0.59 | Genuinely uncertain, competing interpretations   | Flag for tax counsel with both sides                      |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                          | Do not assert; flag "[UNCERTAIN — tax counsel to advise]" |

**Examples:**

- "ISO $100K annual limit: DEFINITE — IRC § 422(d) is clear and unambiguous"
- "409A compliance of this RSU design: HIGH — standard vesting-date settlement is generally
  exempt from 409A, but consult tax counsel on any deferral elections"
- "280G exposure from single-trigger acceleration: PROBABLE — depends on base amount
  calculations not yet performed"
- "EMI qualification for this company: POSSIBLE — gross asset threshold requires current
  balance sheet verification"

---

## Anti-Patterns

Explicit catalogue of what NOT to do in equity incentive plan review:

1. **Single-pass document review** — Plan documents are internally cross-referencing. Read
   the entire plan before flagging issues. An acceleration provision may reference a "Cause"
   definition in the termination section; both must be read together.

2. **Ignoring IRC § 409A entirely** — If the plan covers RSUs, cash-settled SARs, phantom
   equity, or any deferred compensation, § 409A compliance is mandatory. Skipping it is the
   most common and consequential error in equity plan review.

3. **Treating all options as ISOs** — ISOs have strict eligibility rules (employees only),
   grant limitations ($100K annual cap per § 422(d)), and a 10-year plan term requirement.
   NSOs are far more flexible. Never assume option type without reading the plan.

4. **Missing the 409A FMV safe harbor analysis** — "Fair Market Value" in an equity plan
   is not self-defining. The plan must specify a methodology that satisfies the § 409A safe
   harbor. "Board determination" without more fails the safe harbor.

5. **Assuming "Change of Control" is well-defined** — The CoC definition is the most
   litigated concept at M&A exits. If it is absent or poorly defined, flag it RED. Never
   assume a boilerplate definition is adequate without reading it.

6. **Single-trigger acceleration for all employees without 280G analysis** — Single-trigger
   full acceleration for a broad employee population can create significant § 280G excess
   parachute exposure. Always flag for 280G analysis before recommending single-trigger
   designs at scale.

7. **Missing the ISO post-termination window** — ISOs exercised more than 3 months after
   termination (for reasons other than death or disability) lose ISO status. Plans that
   extend the exercise window to 12 months for ISOs must acknowledge the ISO/NSO reclassification
   after month 3. Failure to do so misleads participants about their tax treatment.

8. **Ignoring the § 83(b) election for RSAs** — For restricted stock awards, the 30-day
   election window is non-waivable and non-extendable. Plans that fail to inform participants
   of the election create material tax disadvantage and potential malpractice claims against
   the company's advisors.

9. **Reviewing the plan in isolation from the cap table** — Dilution analysis requires the
   capitalization table. A plan that looks moderate in isolation may represent 25% dilution
   when analyzed against the actual fully diluted share count. Always request the cap table.

10. **Importing US § 409A analysis into UK-only plans** — § 409A is a US concept. It has no
    UK equivalent. UK equity plans are governed by ITEPA 2003, Companies Act 2006, and HMRC
    guidance. Applying US tax analysis to UK plans misinforms rather than helps.

11. **Ignoring the evergreen provision dilution math** — Evergreen provisions that add 5%
    of outstanding shares annually look benign in Year 1 but compound significantly. Model
    the cumulative dilution over the plan's life before classifying as acceptable.

12. **Assuming "board discretion" means unlimited authority** — Court decisions and fiduciary
    duty principles constrain board discretion in equity plans, particularly for public
    companies. Discretion to reprice options, cancel awards, or alter vesting retroactively
    faces legal and governance challenge.

13. **Redlines without fallback positions** — "Delete this clause" without alternative is
    a negotiation dead-end. Always provide a fallback that achieves the required compliance
    outcome while preserving legitimate business flexibility.

14. **Confidence assertions without legal basis** — Never state "this plan violates § 409A"
    without identifying the specific regulatory provision that is violated. Confident assertions
    without authority create worse problems than acknowledged uncertainty.

15. **Skipping the exit scenario analysis** — The true test of an equity plan is how it
    performs for participants at a liquidity event. A plan that looks clean in isolation may
    produce adverse outcomes in an acquisition (e.g., underwater options cancelled, no
    acceleration, no cash-out obligation on the company). Always model the exit scenarios.

16. **Overlooking clawback compliance for listed companies** — Exchange Act Rule 10D-1 and
    related listing standards require listed companies to adopt and enforce clawback policies
    meeting specific standards. A clawback provision that requires "fault" does not comply.

17. **Missing HMRC registration deadlines for UK schemes** — UK companies that adopt EMI
    or CSOP schemes must register with HMRC and file annual ERS returns by 6 July following
    each tax year-end. Missing these deadlines can disqualify the scheme. Always flag in UK
    plan reviews.

---

## Writing Standards

Apply plain-language discipline to all equity plan review output:

**For redline rationales** (shared with board and outside counsel):

- Plain language. No jargon ("§ 409A noncompliant" needs an explanation, not just a label)
- Active voice: "This provision fails the 409A FMV safe harbor" not "The 409A safe harbor
  is failed by this provision"
- Short sentences. One point per sentence.
- Name the actor: "The compensation committee must approve" not "Approval is required"
- Specific citations: "IRC § 422(b)(5) requires a 10-year plan term" not "there may be
  ISO qualification issues"

**For participant-facing analysis** (when reviewing from an employee/participant perspective):

- Avoid heavy tax law jargon — explain what the provision means practically
- Quantify where possible: "Your 90-day window means you have until [date] to decide
  whether to exercise your vested options after leaving the company"
- Flag key elections (83(b), cashless exercise) in plain language with action steps

**Quality gates before delivery:**

1. Can a non-lawyer compensation committee member understand the executive summary?
2. Can outside counsel reviewing this analysis verify and rely on every citation?
3. Is every legal claim backed by a specific IRC section, IRS regulation, or market standard
   (or flagged [VERIFY])?
4. Are any phrases vague or hedging without justification? If yes, fix or add confidence qualifier.
5. Could any sentence be shorter without losing meaning? If yes, shorten.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.
legalcode-mcp is a law, regulatory, and case law database with powerful search across
jurisdictions.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for IRC §§ 409A, 422, 83, 280G regulations and IRS guidance
- Search for SEC Rule 10D-1 and Exchange Act clawback requirements
- Retrieve ITEPA 2003 Schedule 5 (EMI) and Schedule 4 (CSOP) provisions and HMRC ESSUM guidance
- Save the most relevant results to `/tmp/legalcode-equity-plan-authority.md`
- Reference verified authority throughout the clause analysis
- For RED items, search for additional IRS guidance or SEC releases to support or challenge
  the classification
- Check statutory currency — IRC § 409A final regs (2007); Rule 10D-1 (2022); UK CSOP
  £60K limit (April 2023)
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all IRC, IRS, and SEC references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Include a prominent notice that tax citations require independent verification with
  qualified tax counsel before reliance
- Focus the analysis on structural and governance issues rather than tax law certainty
- Do not create the local authority reference file

---

## Multi-Stakeholder Mapping

Identify all affected stakeholders before beginning the analysis:

| Stakeholder                               | Role                     | Affected Provisions                                    | Impact                          | Action Required                 |
| ----------------------------------------- | ------------------------ | ------------------------------------------------------ | ------------------------------- | ------------------------------- |
| Current employees (participants)          | Primary beneficiaries    | All vesting, acceleration, post-termination provisions | High — compensation and tax     | Review award agreements         |
| Future employees (potential participants) | Future beneficiaries     | Pool size, evergreen, award types                      | Medium                          | Pool adequacy assessment        |
| Company (plan sponsor)                    | Administrator and issuer | All — compliance, dilution, tax deductions             | High — legal, tax, securities   | Counsel review                  |
| Compensation committee                    | Fiduciaries              | Administration, governance, clawback                   | High                            | Independence compliance         |
| Investors/stockholders                    | Dilution impact          | Pool size, evergreen, acceleration                     | Medium-High                     | Dilution modeling               |
| Acquirer (potential)                      | Future obligation        | Change-of-control, acceleration, assumption            | High at exit                    | Diligence and 280G analysis     |
| IRS/HMRC                                  | Regulator                | § 409A, ISO, CSOP/EMI compliance                       | Compliance                      | Regular verification            |
| SEC/exchange                              | Regulator                | Clawback, Form S-8, Rule 701                           | Compliance (listed companies)   | Filing compliance               |
| Participants' tax advisors                | Advisors                 | ISO, 83(b), withholding, AMT                           | Indirect — participant guidance | Participant education materials |

---

## Localization Notes

### US State-Specific Considerations

[JURISDICTION-SPECIFIC] Beyond federal IRC requirements, state laws affect equity plan design:

- **California**: Section 25110 securities exemption; any limitation on transferability or
  repurchase rights must comply with Corporations Code requirements; enhanced participant
  protections under Cal. Corp. Code §§ 408–409 for shareholder agreements
- **Delaware**: DGCL § 157 is the primary authority for option grants; § 161 for share
  issuance; director compensation plans subject to entire fairness or business judgment review
  depending on structure
- **New York**: No specific equity plan statute; general corporation law applies

### UK-Specific Considerations

[JURISDICTION-SPECIFIC] For UK plans or plans with UK participants:

- **EMI annual ERS return**: Must be filed by 6 July each year with HMRC for all EMI grants,
  exercises, and lapses in the prior tax year. Missing deadline can disqualify the scheme.
- **Disqualifying events for EMI**: If the company ceases to meet EMI qualifying conditions
  (e.g., control acquired by another company; company's trade becomes non-qualifying), EMI
  options must be exercised within 90 days to preserve income tax advantages [VERIFY]
- **CSOP shares**: Must be ordinary shares that are not subject to restrictions beyond limited
  pre-emption provisions; post-April 2023 rules also allow employee-controlled trusts [VERIFY]
- **BADR (Business Asset Disposal Relief)**: Formerly Entrepreneurs' Relief; EMI options held
  for at least 2 years benefit from 10% CGT rate on disposal [VERIFY — check current limit]
- **Pre-emption rights**: CA 2006 §§ 560–577 require existing shareholders to be offered
  new shares in proportion to their existing holdings; equity plans typically rely on
  disapplied pre-emption rights via ordinary resolution at each AGM [VERIFY]

### International Sub-Plans

[JURISDICTION-SPECIFIC] For each jurisdiction where participants will receive awards:

- Confirm securities law registration exemption (not all countries have Rule 701 equivalents)
- Confirm income recognition event (grant, vest, or exercise — varies by country)
- Confirm withholding obligation and social charge treatment
- Confirm whether foreign exchange approvals are required (India: FEMA; China: SAFE)
- Consider whether local employment law affects vesting on termination (EU works council
  rights, statutory notice periods, local "good reason" equivalents)

---

## Output Format Template

Structure the final deliverable as:

````markdown
## Equity Incentive Plan Review

**Document**: [Plan name, version, adoption date]
**Plan Sponsor**: [Company name, jurisdiction of incorporation]
**Plan Type**: [Stock Option Plan / RSU Plan / Equity Incentive Plan / LTIP / Other]
**Your Perspective**: [Company / Participant / Acquirer / Counsel]
**Company Stage**: [Seed / Series A / Pre-IPO / Public / Post-Acquisition]
**Review Basis**: [Organizational playbook / Market standards for [stage]]
**Date of Review**: [date]
**Governing Law**: [US (Delaware) / UK (England & Wales) / Other]

---

## Executive Summary

[3–5 bullet points summarizing the most important findings with severity flags]

| Finding     | Severity | Priority |
| ----------- | -------- | -------- |
| [Finding 1] | RED      | Tier 1   |
| [Finding 2] | YELLOW   | Tier 2   |
| [Finding 3] | GREEN    | —        |

---

## Plan Architecture Overview

[Complete the Plan Architecture Overview table from Step 5]

---

## Missing Clauses

[List absent clause categories with severity: RED / YELLOW / GREEN]

---

## Clause-by-Clause Analysis

### [Clause Category] — [GREEN / YELLOW / RED] | Confidence: [level]

**Plan provision**: [summary]
**Standard / legal requirement**: [market standard or specific rule]
**Deviation**: [description of the gap]
**Business / tax impact**: [practical consequence]

**Redline** (if YELLOW or RED):

> **Clause**: [section reference]
> **Current language**: "[exact quote]"
> **Proposed redline**: "[specific replacement language]"
> **Legal basis**: [IRC section / SEC rule / market standard]
> **Priority**: [Must-have / Should-have / Nice-to-have]
> **Fallback**: [alternative if primary is rejected]
> **Tax consequence**: [if applicable]
> **Confidence**: [Definite / High / Probable / Possible]

[Repeat for each clause category]

---

## Dilution & Equity Impact

[Complete the dilution table from Step 10]

**Pool adequacy**: [Assessment of whether the pool is sufficient for 12–18 months of
planned grants at the company's current hiring rate]

**Burn rate**: [Annual burn rate assessment vs. market norm]

---

## Exit Scenario Analysis

### Scenario A — Assumption by Acquirer

[Analysis per Step 11]

### Scenario B — Cash-Out Acquisition

[Analysis per Step 11]

### Scenario C — IPO

[Analysis per Step 11]

---

## Prioritized Recommendations

**Tier 1 (Must-Have — address immediately):**

1. [Issue and specific action required]

**Tier 2 (Should-Have — address within 30–60 days):**

1. [Issue and specific action required]

**Tier 3 (Nice-to-Have — address at next plan refresh):**

1. [Issue and specific action required]

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill: "legalcode-equity-incentive-plan-review"
  plan: "[Plan name, adoption date]"
  plan_type: "[Stock Option Plan / RSU Plan / ESOP / Performance Stock / LTIP]"
  plan_sponsor: "[Company name]"
  reviewer_perspective: "[Company / Participant / Acquirer / Counsel]"
  company_stage: "[Seed / Series A–C / Pre-IPO / Public]"
  governing_law: "[US (Delaware) / UK (England & Wales) / Other]"
  review_basis: "[Organizational playbook / Market standards — [stage]]"
  clauses_reviewed: 12
  clauses_present: "[number] — [list]"
  clauses_missing: "[number] — [list missing, with severity]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-equity-plan-authority.md or 'Not created']"
  statutes_consulted:
    - "IRC § 409A — VERIFIED (legalcode-mcp) / [VERIFY]"
    - "IRC § 422 (ISO) — VERIFIED / [VERIFY]"
    - "IRC § 83 (83(b) election) — VERIFIED / [VERIFY]"
    - "IRC § 280G (golden parachute) — VERIFIED / [VERIFY]"
    - "Exchange Act Rule 10D-1 (clawback) — VERIFIED / [VERIFY]"
    - "DGCL § 157 / § 161 — VERIFIED / [VERIFY]"
    - "ITEPA 2003 Sch. 5 (EMI) — VERIFIED / [VERIFY]" # UK only
    - "ITEPA 2003 Sch. 4 (CSOP) — VERIFIED / [VERIFY]" # UK only
  citations_verified: "[N VERIFIED] / [N UNVERIFIED]"
  dilution_modeled: "Yes / No — [% FDC from full pool, burn rate]"
  exit_scenarios_modeled: "Yes / No"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Scope limitations: documents reviewed vs. not reviewed]"
    - "[Tax analysis requires verification by qualified tax counsel in the governing jurisdiction]"
    - "[This review does not constitute a 409A valuation — a qualified independent appraisal is required]"
  reviewer: "AI-assisted — requires review by qualified legal and tax counsel before reliance"
```
````

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis covering the full lifecycle of equity
incentive plan review: stock options (ISO/NSO), RSUs, RSAs, SARs, phantom equity, UK EMI/CSOP,
and international sub-plans. Research grounded in IRC §§ 83, 409A, 422, 280G; Exchange Act
Rule 10D-1; DGCL; ITEPA 2003; Companies Act 2006; and current market practice data (Radford/AON,
Carta, Compensia). No pre-existing skill merged — this is a Legalcode original skill.
