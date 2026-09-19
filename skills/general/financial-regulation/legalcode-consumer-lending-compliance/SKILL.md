---
name: legalcode-consumer-lending-compliance
description: Assess consumer lending programs and loan portfolios for regulatory compliance across the
  US, UK, and EU.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Assess consumer lending programs and loan portfolios for regulatory compliance across the US, UK, and EU. Covers Truth in Lending Act (TILA) / Regulation Z (APR disclosure, ATR/QM rule, HOEPA, TRID), Equal Credit Opportunity Act (ECOA) / Regulation B (adverse action notices, anti-discrimination), Fair Lending (Fair Housing Act, disparate treatment, disparate impact, HMDA), Real Estate Settlement Procedures Act (RESPA) (Section 8 kickback prohibitions, mortgage servicing), state usury laws and rate caps (MLA 36% MAPR, SCRA 6%, NBA preemption), CFPB UDAAP, UK FCA Consumer Credit sourcebook (CONC), Consumer Credit Act 1974 (CCA 1974), FCA Consumer Duty (PS22/9), high-cost short-term credit (HCSTC) price cap, EU Consumer Credit Directive (CCD1 / CCD2 — application November 2026), Mortgage Credit Directive (MCD), and GDPR Article 22 automated credit decisions. Produces jurisdiction-specific compliance gap assessments with COMPLIANT / PARTIAL-COMPLIANT / NON-COMPLIANT / CRITICAL severity ratings, APR calculation reviews, adverse action notice analysis, ability-to-repay assessments, fair lending analysis, and prioritized remediation action plans. Use for consumer loan program reviews, regulatory examination preparation, new product launches, fintech compliance due diligence, and ongoing monitoring programs. Triggers on: TILA review, Reg Z compliance, ECOA adverse action, Regulation B, fair lending audit, RESPA Section 8, consumer credit compliance, APR calculation, ability to repay, qualified mortgage, CONC assessment, Consumer Duty, CCA 1974, CCD2 readiness, creditworthiness assessment, responsible lending review.


# Legalcode Consumer Lending Compliance

> **Disclaimer**: This skill provides a framework for AI-assisted consumer lending
> compliance assessment. It does not constitute legal advice. All outputs must be
> reviewed by qualified banking and consumer finance counsel licensed in the relevant
> jurisdiction before use. Consumer lending regulation is highly technical, frequently
> amended, and subject to extensive regulatory guidance — verify all statutory citations,
> thresholds, and regulatory positions against current authoritative sources before
> relying on any analysis here. Statutory citations, thresholds, and regulatory guidance
> cited from memory carry hallucination risk. Compliance failures can result in regulatory
> enforcement, class action liability, restitution, and civil money penalties — do not
> rely on this skill alone to confirm a compliant program.

---

## Purpose and Scope

This skill assesses consumer lending programs, loan products, and individual transactions
for regulatory compliance across the United States, United Kingdom, and European Union.
It identifies compliance gaps, classifies their severity, and generates prioritized
remediation plans with actionable implementation steps.

**Covers:**

- US TILA / Regulation Z: APR calculation accuracy, disclosure timing, right of rescission,
  ability-to-repay / Qualified Mortgage rule, HOEPA high-cost mortgage thresholds, TRID
  integrated disclosures, CARD Act, Military Lending Act, Servicemembers Civil Relief Act
- US ECOA / Regulation B: prohibited discrimination bases, adverse action notice requirements
  (timing, format, specific reasons), spousal signature rules, Special Purpose Credit Programs
- US Fair Lending: Fair Housing Act, disparate treatment and disparate impact analysis,
  redlining, steering and pricing discrimination, HMDA data obligations
- US RESPA: Section 8 kickback and referral fee prohibitions, Affiliated Business
  Arrangement disclosure, mortgage servicing rules, Qualified Written Request procedures,
  loss mitigation obligations
- US rate regulation: National Bank Act / FDIA preemption analysis, state usury laws,
  OCC/FDIC valid-when-made doctrine, Madden v. Midland exposure assessment
- US CFPB UDAAP (Dodd-Frank § 1031): unfair, deceptive, and abusive acts or practices
- UK FCA CONC sourcebook (CONC 2-8): responsible lending, creditworthiness assessment,
  financial promotions, pre-contractual requirements, post-contractual obligations,
  arrears and forbearance, debt advice
- UK Consumer Credit Act 1974: withdrawal rights (s.55C), periodic statements (s.77A),
  default and termination notices (ss.86B-86E), unfair relationships test (ss.140A-D)
- UK FCA Consumer Duty (PS22/9, July 2023): four outcomes framework, annual assessment
- UK High-Cost Short-Term Credit: price cap (0.8% daily / 100% total / £15 default fee),
  Continuous Payment Authority restrictions, rollover limits
- EU CCD1 (Directive 2008/48/EC): SECCI pre-contractual information, right of withdrawal
  (Art. 14), right of early repayment (Art. 16), creditworthiness assessment (Art. 8)
- EU CCD2 (Directive 2023/2225): scope expansions (BNPL, crypto loans, crowdfunding),
  enhanced creditworthiness assessment (Art. 18), digital SECCI2, CPA controls,
  over-indebtedness prevention — application date November 20, 2026
- EU Mortgage Credit Directive (2014/17/EU): ESIS, responsible lending, APRC
- EU GDPR Article 22: automated credit decision-making, right to explanation
- Member state implementations: Germany (BGB §§ 491-505), France (Consumer Code
  Art. L312-1 et seq.), Netherlands (Wft)

**Does not:**

- Provide legal advice or substitute for qualified legal counsel
- Cover commercial or business lending (B2B credit outside consumer definitions)
- Cover securities-based lending, insurance premium financing, or factoring
- Perform live regulatory filings or HMDA data submissions
- Apply exclusively to one jurisdiction — jurisdiction-agnostic with [JURISDICTION-SPECIFIC]
  markers; always verify current rule text before relying on any specific provision

---

## Jurisdiction and Governing Law

This skill covers **three regulatory domains** — US federal/state, UK (FCA/CCA), and
EU / member state — which operate independently. A single lending program may require
compliance with multiple regimes simultaneously.

[JURISDICTION-SPECIFIC] Jurisdiction-specific content is marked throughout. Always:

- Confirm which jurisdiction's consumer protection rules apply to each borrower
- Verify whether a US national bank or federal thrift can invoke NBA/FDIA preemption
- Confirm CCD2 transposition status in the relevant EU member state before applying
  CCD2 obligations (application date November 20, 2026; transposition deadline November
  20, 2025 — status varies by member state as of March 2026)
- Apply UK rules only to FCA-authorised consumer credit lenders

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's context, the workflow pauses and asks when:

- The applicable jurisdiction or regulatory regime is ambiguous
- The product type changes the applicable framework (e.g., HCSTC vs. standard credit)
- The lender type changes available preemption arguments (national bank vs. state bank)
- Risk classification of a gap depends on context not yet provided

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

### Step 1: Accept the Subject Matter

Accept the lending compliance assessment subject in any format:

- **Loan program description**: Narrative description of a credit product, its terms, and
  the lender's operational procedures
- **Document package**: Loan agreement, disclosure forms (Loan Estimate, Closing Disclosure,
  TRID package, SECCI, SECCI2), adverse action notice samples, underwriting guidelines
- **Regulatory examination scope**: List of regulatory requirements to assess
- **New product specification**: Term sheet or product spec for a consumer credit product
  under development

If no subject matter is provided, prompt the user to supply the relevant documents or
describe the program to be assessed.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the assessment, ask the user:

1. **Jurisdiction(s) to assess**:
   - Options: United States (federal + specify state), United Kingdom, European Union
     (specify member state), Multiple jurisdictions (list them), All three domains
   - _Why this matters_: The applicable regulatory framework, thresholds, and filing
     requirements differ fundamentally across jurisdictions.

2. **Loan product type**:
   - Options: Closed-end mortgage (first lien), Closed-end mortgage (subordinate lien),
     Home equity line of credit (HELOC), Closed-end personal/consumer loan, Credit card /
     revolving line of credit, Auto loan, Student loan, Buy Now Pay Later (BNPL),
     High-cost short-term / payday loan, Other (describe)
   - _Why this matters_: Product type determines which disclosure regime applies (TRID
     vs. non-TRID in the US), whether HOEPA / HCSTC rules are triggered, whether the QM
     safe harbor applies, and the EU directive threshold coverage.

3. **Lender type (US only)**:
   - Options: National bank (OCC-chartered), Federal savings association (OTS/OCC),
     State-chartered bank (FDIC member), State-chartered bank (Federal Reserve member),
     Nonbank / fintech lender, Credit union, Other
   - _Why this matters_: National banks and federal savings associations may invoke NBA /
     FDIA preemption to override state usury laws; nonbank lenders generally cannot.

4. **Assessment scope**:
   - Options: Full regulatory stack (all applicable laws), Specific regulation (name it),
     Pre-examination readiness, New product launch review, Fair lending only, APR and
     disclosure accuracy only, Servicing and post-origination only
   - _Why this matters_: Scoping the assessment focuses the analysis on what the user
     most needs.

5. **Outcome format**:
   - Options: Executive compliance gap summary, Detailed regulatory analysis with
     citations, Remediation action plan with owners and deadlines, Examination response
     preparation, All of the above
   - _Why this matters_: Determines the level of detail and output format.

If the user provides partial context, state your assumptions explicitly and proceed.

### Step 3: Identify Applicable Regulatory Framework

Based on jurisdiction and product type, identify the complete regulatory stack that applies.
Use the **Regulatory Framework Reference** section below to map the applicable rules.

**⟁ CLARIFY** — If the product is at a jurisdictional or product boundary, confirm:

- "This appears to be a BNPL product. Under EU CCD2 (applicable November 2026), BNPL
  products with more than 3 installments or a repayment period over 3 months are now
  in scope. Should I assess CCD1 compliance (current), CCD2 readiness, or both?"
- "This mortgage product may be above the HOEPA threshold. I'll need to verify the
  current APR and fee tests. Can you confirm the APR and total points/fees?"
- "This lender appears to be a nonbank. State usury law preemption is unavailable — should
  I assess state rate caps for the relevant state(s)?"

### Step 4: Gather Regulatory Authority

Use **legalcode-mcp** to build a working regulatory reference file for the applicable
jurisdiction(s).

Search for:

- Current text of applicable regulations (Regulation Z, ECOA/Reg B, CONC provisions, etc.)
- Recent CFPB/FCA/EBA guidance and interpretations
- Relevant enforcement actions and consent orders from the past 3 years
- Any proposed or finalized rule changes affecting the assessed product type
- Current regulatory thresholds (which are updated annually)

Save results to `/tmp/legalcode-lending-authority.md`. Structure as:

```markdown
# Regulatory Authority Reference — Consumer Lending Compliance

## Jurisdiction: [jurisdiction]

## Date: [date]

### Applicable Statutes and Regulations

- [Statute/Regulation, section, current text or summary]

### Regulatory Thresholds (verify annually)

- [Threshold name, current value, effective date]

### Recent Guidance and Enforcement

- [Regulator, action/guidance, date, key holding]
```

**If legalcode-mcp is not connected:**

- Proceed using the regulatory framework reference in this skill
- Mark all specific thresholds with [VERIFY — thresholds update annually]
- Mark all enforcement citations with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — verify all citations and thresholds"`

### Step 5: Conduct Compliance Assessment

Assess the lending program systematically against each applicable regulatory domain.
Use the **Regulatory Framework Reference** section below for the detailed analysis criteria.

Cover all applicable domains from the table below. For each requirement, determine whether
the program is **COMPLIANT**, **PARTIAL-COMPLIANT**, **NON-COMPLIANT**, or **CRITICAL**
(see Severity Classification).

| #   | Assessment Domain                         | Applicable To                                                             |
| --- | ----------------------------------------- | ------------------------------------------------------------------------- |
| 1   | APR Calculation Accuracy                  | US TILA/Reg Z; UK Total Charge for Credit Regs; EU CCD1/CCD2              |
| 2   | Disclosure Timing and Format              | US TILA/Reg Z (TRID for mortgages); UK CONC 4/CCA 1974; EU SECCI/SECCI2   |
| 3   | Creditworthiness / Ability-to-Repay       | US ATR/QM Rule (§1026.43); UK CONC 5; EU CCD Art. 8 / CCD2 Art. 18        |
| 4   | Adverse Action Notices                    | US ECOA/Reg B (§1002.9); US FCRA                                          |
| 5   | Fair Lending Compliance                   | US Fair Housing Act; ECOA; HMDA; disparate impact/treatment               |
| 6   | Rate and Fee Compliance                   | US state usury; MLA 36% MAPR; SCRA 6%; UK HCSTC cap; EU member state caps |
| 7   | RESPA Section 8 Compliance (US)           | US RESPA / Regulation X                                                   |
| 8   | Mortgage Servicing                        | US Reg X loss mitigation; UK CONC 6-7; EU CCD2 Art. 27-29                 |
| 9   | Right of Withdrawal / Rescission          | US TILA §1026.23; UK CCA s.55C; EU CCD Art. 14                            |
| 10  | UDAAP / Unfair and Abusive Practices      | US Dodd-Frank § 1031; UK Consumer Duty / FCA Principles                   |
| 11  | Automated Decision-Making                 | EU GDPR Art. 22; UK FCA Consumer Duty; US CFPB fair lending               |
| 12  | Military / Servicemember Protections (US) | MLA (32 CFR Part 232); SCRA (50 U.S.C. §§ 3901-4043)                      |
| 13  | High-Cost Credit Rules                    | US HOEPA (§1026.32); UK HCSTC; EU CCD2 over-indebtedness                  |
| 14  | Consumer Duty / Vulnerable Customer       | UK FCA Consumer Duty (PS22/9); UK CONC 7.2                                |

**⟁ CLARIFY** — For complex programs involving multiple products or channels:

- Ask whether to assess all products in scope or focus on the highest-risk product first
- Ask whether automated underwriting systems are used — if yes, fair lending and GDPR
  Article 22 assessments require additional information about the model

### Step 6: APR Calculation Review

For any loan product, review the APR/APRC/APR calculation methodology against the
applicable regime. See **APR Calculation Framework** section below.

Flag any APR deviation exceeding the applicable tolerance as NON-COMPLIANT.
[JURISDICTION-SPECIFIC] Applicable tolerances:

- US: 1/8% overstatement; 1/4% understatement (regular transactions); 1/4%/1/8%
  for irregular transactions (12 CFR §1026.22 and commentary) [VERIFY]
- UK: APR must be calculated per SI 2010/1011 methodology; no explicit tolerance
  for pre-contractual disclosure — CONC 3.1.2R requires accurate representative APR
- EU CCD1/CCD2: APR calculated per Annex I formula; methodology must be exactly as
  prescribed; no tolerance for pre-contractual SECCI disclosure

### Step 7: Adverse Action Notice Review (US) / Refusal Notice Review (UK/EU)

Assess adverse action or refusal notices against applicable requirements. See the
**Adverse Action Notice Requirements** section below.

**⟁ CLARIFY** — Ask: "Do you have sample adverse action notices to review, or should
I assess the program's stated procedure for generating notices?"

### Step 8: Fair Lending Analysis (US) / Non-Discrimination Assessment (UK/EU)

Assess fair lending risk using the **Fair Lending Analysis Framework** section below.
This domain carries the highest reputational and enforcement risk in US consumer lending.

**⟁ CLARIFY** — Ask:

- "Is HMDA data available for this lending program? HMDA analysis is the primary
  fair lending evidence base."
- "Are there any pending or prior fair lending examinations, investigations, or
  enforcement actions?"
- "Does the underwriting model use any proxy features (geographic, behavioral, or
  alternative data) that could correlate with protected class status?"

### Step 9: Classify Severities and Generate Findings

Classify each identified gap using the **Severity Classification** system below. For
each NON-COMPLIANT or CRITICAL finding, generate an actionable remediation recommendation
using the format in **Actionable Output per Finding**.

Run the **Citation Quality Gates** silently before delivering findings. For every CRITICAL
finding, run the 3-pass **Self-Interrogation** and assign a **Confidence Score**.

### Step 10: Quality Verification and Delivery

Before delivering the assessment:

1. Run the 5 Citation Quality Gates. Revise any failures.
2. For every CRITICAL finding, run the 3-pass Self-Interrogation.
3. Assign Confidence Scores to all material findings.
4. Verify all 14 assessment domains have been addressed or explicitly scoped out.
5. Generate the Glass Box Audit Trail.
6. Deliver using the **Output Format Template** below.

---

## Regulatory Framework Reference

### US Framework

#### 1. Truth in Lending Act (TILA) / Regulation Z

**Statutory authority**: 15 U.S.C. §§ 1601-1667f (TILA); 12 CFR Part 1026 (Regulation Z)
**Regulator**: CFPB (primary consumer protection authority post-Dodd-Frank); prudential
regulators for supervised entities

**Core scope**: Credit offered to a natural person primarily for personal, family, or
household purposes where the creditor regularly extends credit and either the credit is
payable in more than 4 installments or subject to a finance charge (15 U.S.C. § 1602).

**Key exemptions**: Business/agricultural/commercial credit; credit exceeding $66,400
threshold (2024 figure — [VERIFY annually]) unless secured by real property or a
dwelling; public utility credit; broker securities credit.

**Closed-end credit disclosures** (§§ 1026.17-1026.24):

- Amount financed, finance charge, APR, total of payments, payment schedule, total sale
  price (for credit sales)
- Disclosures must be given before consummation
- APR tolerance: 1/8% overstatement; 1/4% understatement [VERIFY]

**TRID (TILA-RESPA Integrated Disclosure)** for residential mortgage transactions
(§ 1026.19(e)-(f)):

- Loan Estimate (LE): provided within 3 business days of application receipt; must
  reflect good faith estimates; contain 7 required fields
- Closing Disclosure (CD): provided no later than 3 business days before consummation
- Changed circumstance triggers allow revised LE
- Tolerances: zero tolerance (origination charges, transfer taxes, unaffiliated third-party
  services with provider list); 10% tolerance (recording fees, affiliated services, seller
  required services); unlimited tolerance (prepaid interest, insurance premiums, escrow)

**Ability-to-Repay (ATR) / Qualified Mortgage (QM)** (§ 1026.43):

- For covered transactions (closed-end mortgages on a dwelling), creditors must make a
  reasonable, good-faith determination of repayment ability considering 8 underwriting factors
- QM safe harbor: General QM (debt-to-income ≤ 43%, points/fees ≤ 3% of loan amount for
  loans ≥ $130,461 [VERIFY threshold annually], no risky loan features)
- QM conclusive safe harbor: APR ≤ APOR + 1.5% (for first lien conforming loans);
  rebuttable presumption: APR > APOR + 1.5% but ≤ APOR + 2.25% [VERIFY]
- GSE Patch: expired October 2022

**HOEPA / High-Cost Mortgage** (§ 1026.32):

- Triggered by: APR exceeding APOR by 6.5% (first lien) / 8.5% (subordinate lien);
  OR points/fees exceeding 5% of loan amount (or dollar threshold for small loans)
- Prohibited terms: balloon payments (with exceptions), prepayment penalties (with
  exceptions), negative amortization, advance payments from proceeds, increased rates
  after default, split loan structures
- Enhanced pre-loan counseling required

**Right of Rescission** (§ 1026.23):

- 3 business-day right to rescind for non-purchase money transactions secured by the
  consumer's principal dwelling
- Extended 3-year rescission right for material disclosure violations
- Notice must be on separate documents; creditor must provide 2 copies per consumer

**Adjustable-Rate Mortgage (ARM) disclosures** (§ 1026.19(b), §§ 1026.20(c)-(d)):

- Initial ARM disclosure (CHARM Booklet) at application or within 3 business days
- Adjustment notices: 210-240 days before first payment change; 60-120 days for
  subsequent changes

**Open-end credit / Credit cards** (§§ 1026.5-1026.16):

- CARD Act 2009 amendments: penalty rate triggers require 60+ days delinquency;
  45-day advance notice of rate increases; prohibit rate increases in first year;
  minimum payment disclosure; over-limit opt-in requirement

**Military Lending Act (MLA)** [JURISDICTION-SPECIFIC — US only]:

- 32 CFR Part 232; 10 U.S.C. § 987
- 36% Military Annual Percentage Rate (MAPR) cap for consumer credit to covered borrowers
  (active duty servicemembers, spouses, and certain dependents)
- MAPR includes all charges that would be excluded from APR (e.g., credit insurance,
  application fees, participation fees)
- Prohibits mandatory arbitration, prepayment penalties, and allotment conditions
- MLA statement and Regulation Z disclosure required
- Creditor must check MLA database or use safe harbor consumer report method [VERIFY]

**Servicemembers Civil Relief Act (SCRA)** [JURISDICTION-SPECIFIC — US only]:

- 50 U.S.C. §§ 3901-4043
- 6% annual interest rate cap on pre-service obligations during active duty
- Mortgage foreclosure protections (stay during active duty + 1 year post-termination)
- Applies to obligations incurred before entry into active duty

#### 2. Equal Credit Opportunity Act (ECOA) / Regulation B

**Statutory authority**: 15 U.S.C. § 1691 et seq.; 12 CFR Part 1002 (Regulation B)
**Regulator**: CFPB (primary); DOJ (enforcement authority for pattern or practice)

**Prohibited bases** (§ 1002.4): race, color, religion, national origin, sex, marital
status, age (provided applicant has legal capacity), receipt of public assistance, exercise
of rights under the Consumer Credit Protection Act.

**Adverse action requirements** (§ 1002.9):

- Must provide notification within 30 days of receiving a completed application
- Notification must: identify the creditor; state action taken; include Statement of
  Specific Reasons OR disclose right to request reasons within 60 days
- At minimum 4 specific reasons (if reasons given); reasons cannot be "discriminatory"
- CFPB Model Form C-1 through C-5 provide safe harbors
- Counteroffers: if applicant does not accept within 90 days, treat as adverse action

**Specific reasons requirement** (§ 1002.9(b)(2)):

- Statement of reasons or disclosure of right to request must be given
- "Insufficient credit experience" is not sufficient without specificity
- Creditors using credit scoring: statement that credit scoring was used; score obtained;
  range; key factors (no more than 4) adversely affecting the score
- Artificial intelligence / algorithmic denials: CFPB Circular 2022-03 requires specific
  reasons even from black-box models [VERIFY current guidance]

**Spousal signature rules** (§ 1002.7(d)):

- Creditor cannot require signature of applicant's spouse unless spouse is a joint
  applicant or the state is a community property state and the spouse's signature is
  necessary to create a valid security interest [JURISDICTION-SPECIFIC — state law]

**Special Purpose Credit Programs (SPCP)** (§ 1002.8):

- Programs designed to benefit economically disadvantaged borrowers may deviate from
  general ECOA anti-discrimination rules under certain conditions
- CFPB issued guidance October 2022 on SPCPs for homeownership programs [VERIFY currency]

**Income consideration** (§ 1002.6(b)(5)):

- Must consider income from part-time employment, alimony, child support if applicant
  chooses to disclose; cannot discount solely on the basis of source

#### 3. Fair Lending

**Primary laws**: Fair Housing Act (FHA) 42 U.S.C. §§ 3601-3619; ECOA 15 U.S.C. § 1691
et seq.; 42 U.S.C. § 1981 (equal rights under the law)

**Discrimination theories**:

- **Disparate treatment**: intentional discrimination; treating similarly-situated
  applicants differently based on a protected class — requires comparator evidence
  or direct evidence of discriminatory intent
- **Disparate impact**: facially neutral policy with statistically significant
  disproportionate adverse effect on a protected class; defendant must show business
  necessity; plaintiff can rebut with less discriminatory alternative
  (Texas Dep't of Housing v. Inclusive Communities, 576 U.S. 519 (2015)) [VERIFY]
- **Redlining**: failure to lend in, or discouraging applications from, geographic areas
  with high minority population — DOJ and CFPB enforcement via Combating Redlining Initiative
- **Reverse redlining / predatory lending**: targeting protected-class communities with
  high-cost or unfavorable loan products

**HMDA reporting** (12 U.S.C. § 2801 et seq.; 12 CFR Part 1003):

- Covered institutions must collect, report, and disclose HMDA data annually
- Data fields: race, ethnicity, sex, age, income, loan amount, action taken, denial
  reasons, pricing data, property location (census tract)
- Threshold triggers: banks/credit unions 25+ closed-end mortgages in each of two
  preceding years; nonbanks 100+ closed-end mortgages [VERIFY thresholds]
- HMDA data is the primary tool for fair lending statistical analysis and examination

**Key enforcement actions** (for calibration):

- DOJ / CFPB Townstone Mortgage consent order (2022): redlining via marketing exclusion
- DOJ Lakeland Bank consent order (2023): $13M community reinvestment fund [VERIFY]
- CFPB / DOJ fair lending enforcement: ongoing Combating Redlining Initiative [VERIFY]

#### 4. Real Estate Settlement Procedures Act (RESPA) / Regulation X

**Statutory authority**: 12 U.S.C. § 2601 et seq.; 12 CFR Part 1024 (Regulation X)

**Section 8 prohibitions** (12 U.S.C. § 2607; 12 CFR § 1024.14):

- No person shall give or accept any fee, kickback, or thing of value for referral of
  business incident to a real estate settlement service
- No fee splitting (splitting of unearned fees) even without referral
- Exceptions: services actually performed; payment for goods, facilities, or services
  actually furnished; controlled business arrangement (AfBA) with disclosure; employer/
  employee relationships

**Affiliated Business Arrangement (AfBA)** (§ 1024.15):

- Must disclose the arrangement at or before referral
- Use CFPB Affiliated Business Arrangement Disclosure Statement
- Consumer must not be required to use the affiliated provider
- Referral fees cannot be based on use of the affiliated provider

**Mortgage servicing** (§§ 1024.17, 1024.30-1024.41):

- Escrow account management: annual escrow account analysis; 2-month cushion cap
- Error resolution (§ 1024.35): respond to Notice of Error within 5 business days
  (acknowledgment) and 30 business days (resolution); extended 45 days for certain errors
- Information requests (§ 1024.36): 5 business days (acknowledgment); 30 business days
  (response); extended 45 days for certain requests [VERIFY current timelines]
- Loss mitigation (§ 1024.41): upon receipt of complete loss mitigation application,
  evaluate for all options within 30 business days; dual tracking prohibition (cannot
  proceed with foreclosure while evaluating complete loss mitigation application)

**Qualified Written Request (QWR)** (12 U.S.C. § 2605(e)):

- Written correspondence from borrower identifying loan and describing problem or
  requesting information
- Servicer must acknowledge within 5 business days; provide response within 30 business
  days (extendable 15 days); no adverse credit reporting during response period [VERIFY]

#### 5. Rate Regulation and Usury

**National Bank Act (NBA) preemption** [JURISDICTION-SPECIFIC — US, national banks only]:

- 12 U.S.C. § 85: national banks may charge interest at the rate allowed by the state
  where the bank is located
- NBA preemption allows a national bank to "export" its home state's interest rate to
  borrowers in other states with lower usury caps
- 12 C.F.R. Part 7 (OCC rules); OCC valid-when-made rule (2020) [VERIFY current status]

**Federal Deposit Insurance Act (FDIA) preemption** [JURISDICTION-SPECIFIC — US, FDIC-insured state banks]:

- 12 U.S.C. § 1831d: parallel to NBA for state-chartered, FDIC-insured banks
- FDIC valid-when-made rule (2020) [VERIFY current status]

**Madden v. Midland Funding** (786 F.3d 246, 2d Cir. 2015) [VERIFY — second-hand exposure]:

- In the Second Circuit (New York, Connecticut, Vermont): assignment of a national bank
  loan to a nonbank may eliminate NBA interest rate preemption
- OCC/FDIC valid-when-made rules aimed to address — but their current legal status
  and geographic scope requires independent verification [VERIFY]
- Nonbank lenders, fintech platforms, and bank-model (rent-a-bank) partnerships in
  affected states should assess ongoing litigation risk

**State rate caps** [JURISDICTION-SPECIFIC — verify per state]:

- New York: criminal usury 25% p.a. (Penal Law § 190.40); civil usury 16% p.a.
  (GOL § 5-501); exceptions for national banks [VERIFY]
- California: no general usury cap for licensed lenders; CFL licensees exempt;
  rate cap history (SB 1235/AB 539) for loans $2,500-$10,000: max 36% + FFIR [VERIFY]
- Illinois: 36% APR cap on consumer loans ≤$40,000 (PLPA, effective 2021) [VERIFY]
- Many other states: verify applicable cap, exemptions, and charter type impact

**Military Lending Act / SCRA**: See TILA section above.

#### 6. CFPB UDAAP

**Authority**: Dodd-Frank Wall Street Reform and Consumer Protection Act § 1031;
12 U.S.C. § 5531

**Unfair**: substantial injury to consumers; injury not reasonably avoidable; injury
not outweighed by countervailing benefits

**Deceptive**: material representation or omission likely to mislead a reasonable consumer

**Abusive** (unique to Dodd-Frank — not in FTC Act):

- Materially interferes with consumer's ability to understand a term or condition, OR
- Takes unreasonable advantage of: (a) consumer's lack of understanding; (b) consumer's
  inability to protect their interests; (c) consumer's reasonable reliance on a covered
  person

Key UDAAP risk areas in lending: hidden fees, confusing repayment terms, misleading
APR advertising, aggressive collection practices, ineffective loss mitigation [VERIFY
current CFPB guidance on UDAAP examination procedures].

---

### UK Framework

#### 7. FCA Consumer Credit (CONC) Sourcebook

**Regulatory authority**: Financial Conduct Authority (FCA); authorisation required under
FSMA 2000 and Part 4A permission for consumer credit activities

**CONC 2: Conduct of Business**

- CONC 2.2R: creditworthiness assessment must be undertaken before credit is agreed;
  assessment must be appropriate and proportionate to the type and amount of credit
- Cannot rely solely on CRA data; must consider income, committed expenditure, and
  other relevant factors

**CONC 3: Financial Promotions**

- CONC 3.1.2R: representative APR must be shown in credit promotions where a rate of
  interest, fee, or charge is included; representative APR must apply to at least 51%
  of consumers who enter into a credit agreement in response to the promotion
- Financial promotions must be clear, fair, and not misleading (FCA Principle 7)

**CONC 4: Pre-Contractual Requirements**

- Pre-contract information in prescribed form; SECCI-equivalent for UK [VERIFY current
  required form post-Brexit]
- Distance contract information requirements (FCA COBS overlap for regulated activities)
- Adequate explanations: lender must provide an adequate explanation of product features
  to allow consumer to make an informed decision (CONC 4.2G)

**CONC 5: Responsible Lending**

- CONC 5.1.2R: creditworthiness assessment required for all consumer credit, including
  secured credit
- Assessment must consider sustainability of repayment over the full term
- For HCSTC: additional assessment required before each rollover

**CONC 6: Post-Contractual Requirements**

- Account information and statements at least annually (or more frequently for revolving)
- Interest rate variation notice required before change takes effect
- Statements must include: outstanding balance, interest rate, minimum payment, next
  payment date

**CONC 7: Arrears, Default, and Recovery**

- Firms must treat customers in financial difficulty fairly (CONC 7.2.1R)
- Must signpost to free debt advice (MoneyHelper/StepChange/Citizens Advice) when
  consumer is in arrears 36+ days (CONC 7.3.4R) [VERIFY current rule reference]
- Forbearance: firms must give adequate consideration to forbearance and arrangement to
  pay options before taking enforcement action
- Recovery actions must not be oppressive or disproportionate

**CONC 8: Debt Advice**

- Requirements for firms carrying on regulated debt counselling / debt adjusting activities

#### 8. Consumer Credit Act 1974 (CCA 1974)

**Section 55C**: Right to withdraw from a credit agreement within 14 days of conclusion,
without penalty (except interest accrued on amounts drawn). Consumer must notify lender
and repay any drawn amounts within 30 days. Applies to most personal credit agreements
(exceptions: mortgages and overdrafts on demand).

**Section 77A**: Creditor must provide periodic statements for fixed-sum credit at
least annually, free of charge. Must include outstanding balance, interest rate, minimum
payment, and next payment date.

**Sections 86B-86E**: Default and termination notices must be in prescribed form (SI
1983/1561 as amended) [VERIFY current SI reference]; minimum 14-day cure period before
action; notice must specify breach and remedy options.

**Sections 140A-140D**: Unfair relationships test — courts can set aside or vary any
credit agreement if the relationship between creditor and debtor is unfair to the debtor.
No time limit; wide remedial powers. High litigation risk for lenders with aggressive
terms.

**Sections 77-78**: Consumer right to request a copy of the credit agreement and
statement of account within prescribed timeframes and fee limits.

#### 9. FCA Consumer Duty (PS22/9)

**Effective date**: July 31, 2023 (new products/services); July 31, 2024 (closed book)

**Four outcomes** — firms must demonstrate achievement of:

1. **Products and Services**: designed and targeted to meet the needs of the intended
   consumer group; not marketed to consumers outside the target market
2. **Price and Value**: price reflects fair value; no disproportionate exit fees;
   value testing processes documented; intermediary chains assessed for fair value
3. **Consumer Understanding**: communications enable informed decisions; consumer
   testing documented; clear, fair, and not misleading standard exceeded
4. **Consumer Support**: support responsive to consumer needs; particular protections
   for vulnerable consumers; complaints handling effective

**Annual assessment**: firms must annually assess and confirm compliance with Consumer
Duty obligations; board (or equivalent) must review and approve assessment.

**Vulnerable customers** (FG21/1): lenders must have processes to identify consumers
with characteristics of vulnerability (health, life events, resilience, capability);
must ensure vulnerable consumers can access and benefit from products and services.

#### 10. High-Cost Short-Term Credit (HCSTC)

**Definition**: Consumer credit agreement where the APR equals or exceeds 100% p.a.,
where the credit is due within 12 months, and which is not a home credit loan, bill of
sale loan, or overdraft [VERIFY current CONC 2 Annex 1R definition].

**Price cap** (CONC 2 Annex 1R):

- Interest: max 0.8% per day
- Total cost cap: consumer must never repay more than 100% of the amount borrowed
- Default fee cap: max £15 (or 2% of the payment due if that is lower) [VERIFY]

**Continuous Payment Authority (CPA)**:

- CONC 6.7.25R: after 2 failed CPA collection attempts on one loan, firm cannot attempt
  further CPA collection unless consumer agrees; applies to total amount (not part-payments)
- Part-payment CPA use restricted

**Rollover limits**: CONC 6.7.23R — HCSTC agreement cannot be refinanced/rolled over
more than twice; lender must offer alternative repayment arrangement after second rollover.

#### 11. Mortgage Market Review (MMR) and FCA Mortgage Rules

**Responsible lending**: MCOB 11 — mortgage lender must assess affordability; stress
testing at interest rates above offered rate (typically +2% or stressed floor rate);
cannot assume house price appreciation.

**Regulated mortgage contract**: defined in FSMA 2000 (Regulated Activities) Order 2001
Art. 61; covers first-charge mortgages on UK residential property.

---

### EU Framework

#### 12. Consumer Credit Directive 2008/48/EC (CCD1) — Current

**Scope**: Consumer credit agreements €200-€75,000 [VERIFY for CCD2 updates]; consumer =
natural person acting outside trade/business/profession.

**Key exemptions**: Mortgages (covered by MCD); overdrafts repayable on demand within
3 months; employer loans to employees at below-market rates.

**Standard European Consumer Credit Information (SECCI)**:

- Mandatory pre-contract form (Annex II of CCD1)
- Must be provided in good time before consumer is bound
- Must include: lender details, credit amount, duration, APR, total amount payable,
  repayment schedule, charges, right of withdrawal, early repayment terms

**Right of withdrawal** (Art. 14): 14-day withdrawal period; no penalty; consumer must
repay drawn amounts + interest within 30 days; no compensation to creditor except
necessary administrative costs.

**Right of early repayment** (Art. 16): consumer may repay early at any time; compensation
for creditor limited to max 1% of outstanding amount if period remaining > 1 year;
max 0.5% if period remaining ≤ 1 year; no compensation for variable-rate credit.

**Creditworthiness assessment** (Art. 8): lender must assess on basis of sufficient
information about consumer's financial situation; may consult credit database; if
assessment shows high risk of non-performance, lender should not grant credit.

#### 13. Consumer Credit Directive 2023/2225 (CCD2) — Application November 20, 2026

**Transposition deadline**: November 20, 2025 — member states at varying implementation
stages; verify national transposition status before relying on CCD2 obligations [VERIFY]

**Scope expansions** (key changes from CCD1):

- BNPL: now in scope if repayment in more than 3 installments or period > 3 months
- Crypto-asset backed loans: explicitly included
- Crowdfunding consumer loans: €200-€100,000 threshold
- Medical/dental treatment loans
- Car leasing with purchase option

**Enhanced creditworthiness assessment** (Art. 18 CCD2):

- Lender must assess based on: sufficient and appropriate information about consumer;
  financial circumstances; ability to meet obligations under proposed agreement
- Cannot extend credit if assessment shows inability to sustain repayment
- Over-indebtedness prevention: must consider total debt obligations

**Digital SECCI2**:

- Digital format is the default; interactive tools permissible
- Accessible to consumers with disabilities
- Consumer must be able to store/print

**CPA controls** (Art. 34 CCD2):

- Annual consent renewal required for ongoing CPAs
- Tighter frequency restrictions; strengthened termination rights

**Forbearance requirements** (Arts. 27-29 CCD2):

- Lender must contact consumer before enforcement action
- Must offer forbearance measures where feasible
- Must explore debt restructuring options
- Provides consumers in arrears with stronger protections than CCD1

**Over-indebtedness prevention** (Art. 23 CCD2):

- Lenders must consider total debt obligations
- Credit reference bureau information mandatory consideration

#### 14. Mortgage Credit Directive 2014/17/EU (MCD)

**European Standardised Information Sheet (ESIS)**: prescribed format; must be provided
before consumer is bound; includes APRC, monthly payment, total payable, early repayment
terms, valuation requirements.

**Responsible lending** (Art. 18): lender must assess creditworthiness; cannot approve
if consumer clearly unable to repay; cannot assume property value appreciation.

**Annual Percentage Rate of Charge (APRC)**: EU APRC equivalent of APR; calculated per
Annex I formula; includes all mandatory costs.

#### 15. GDPR Article 22 and Automated Credit Decisions

**Article 22 (GDPR)**: Subject to exceptions, individuals have the right not to be
subject to a decision based solely on automated processing which produces legal effects
or similarly significant effects. Credit decisions are typically "similarly significant."

**Exception for contract necessity** (Art. 22(2)(a)): automated decision-making permitted
if necessary for contract; but lender must implement suitable safeguards including:

- Right to obtain human intervention
- Right to express point of view
- Right to contest the decision

**Right to explanation**: Recital 71; CJEU C-203/22 (2024) — consumer has right to
meaningful explanation of automated credit decision logic [VERIFY — recent CJEU case]

**Proxy discrimination risk**: ML/AI models using geographic, behavioral, or third-party
data features may constitute indirect discrimination on protected characteristics
(Art. 22 + GDPR anti-discrimination overlay + national fair lending laws)

---

## APR Calculation Framework

| Regime                 | Method                                            | Key Inclusions                                                                 | Key Exclusions                                                                     | Tolerance                                    | Verify Annually                                     |
| ---------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| US TILA/Reg Z          | Actuarial method per § 1026.22 and Appendix J     | Interest, origination fees, PMI (if required), mandatory products              | Optional insurance, late charges, taxes                                            | ±1/8% to ±1/4% depending on transaction type | Annual exemption thresholds                         |
| UK CONC / SI 2010/1011 | Iterative present value equation per SI 2010/1011 | Interest, mandatory fees, mandatory insurance, credit intermediary commissions | Optional insurance, penalty charges, valuation fees (mortgages), enforcement costs | No explicit tolerance — must be accurate     | Representative APR must apply to 51%+ of applicants |
| EU CCD1/CCD2 Annex I   | Annex I iterative formula                         | Same categories as UK (implementing same EU standard)                          | Same as UK                                                                         | No tolerance for pre-contract SECCI          | Annual verification against Annex I [VERIFY]        |

**Common APR calculation errors to detect:**

- Excluding mandatory credit insurance from finance charge (US) or total charge for
  credit (UK/EU)
- Using nominal instead of effective rate basis
- Incorrect handling of irregular payment schedules
- Not annualizing fees correctly for short-term products
- HCSTC: applying 0.8% daily as equivalent to APR without cross-checking total cap

---

## Adverse Action Notice Requirements

| Requirement             | US ECOA/Reg B                                                            | US FCRA                                                     | UK (Refusal Explanation)                                                     |
| ----------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Timing                  | 30 days from complete application                                        | Within 5 business days of adverse action (if CRA data used) | Before or at time of refusal; no prescribed statutory period [VERIFY CONC 4] |
| Format                  | Written (electronic with E-SIGN consent); oral for certain notifications | Written; oral if applicant asked for reasons                | Not prescribed by CCA 1974 [VERIFY CONC 4.2G]                                |
| Specific reasons        | 4+ specific reasons OR right to request within 60 days                   | Principal reason(s) for adverse action                      | Explanation must enable informed decision (Consumer Duty, CONC 4)            |
| Credit score disclosure | If score used: score, range, key factors (≤4), date obtained             | Score, range, key factors (≤4), lender contact info         | Not required under UK rules; GDPR Art. 22 explanation may be required        |
| Model form safe harbor  | CFPB Model Forms C-1 to C-5                                              | CFPB FCRA Model Form                                        | None [VERIFY]                                                                |

**Common adverse action failures:**

- Providing "general" reasons rather than specific reasons (e.g., "Credit history" without
  specifying what about credit history)
- Not providing notice when counter-offer is declined within 90 days (US)
- Failing to provide credit score disclosure when a score was used in the decision
- AI/ML model denial: using unexplainable model output; CFPB Circular 2022-03 [VERIFY]

---

## Ability-to-Repay / Creditworthiness Assessment Requirements

### US: ATR / QM Rule

**8 underwriting factors** (§ 1026.43(c)(2)) — creditor must consider and verify:

1. Current or reasonably expected income or assets
2. Current employment status
3. Monthly payment on the covered transaction
4. Monthly payment on simultaneous loan
5. Monthly payment for mortgage-related obligations
6. Current debt obligations, alimony, child support
7. Monthly debt-to-income ratio or residual income
8. Credit history

**QM safe harbor elements** (General QM as of 2021 revision) [VERIFY current thresholds]:

- Points and fees ≤ 3% of loan amount (for loans ≥ threshold; higher percentage for
  smaller loans — see § 1026.43(e)(3))
- No risky loan features (interest-only, negative amortization, balloon, term > 30 years)
- APR ≤ APOR + 1.5% for strong safe harbor (first lien conforming); ≤ APOR + 3.5% for
  small creditor portfolio loans [VERIFY]

### UK: CONC 5 Responsible Lending Assessment

- Assessment proportionate to type of credit, amount, duration
- Must consider income and expenditure (essential living costs + committed expenditure)
- Cannot rely solely on credit reference data (CONC 5.3.7AG)
- For HCSTC: enhanced assessment; sustainability of repayment on each rollover
- Consumer Duty overlay: assessment must produce good outcome; must be sustainable

### EU: CCD1 Art. 8 / CCD2 Art. 18

- Based on sufficient and appropriate information about consumer's financial situation
- Must consult relevant credit databases if national law requires
- CCD2: enhanced — must assess sustainability; consider over-indebtedness risk; document
  assessment

**Common creditworthiness failures:**

- Relying solely on stated income without verification in required contexts
- Not considering existing debt obligations
- For HCSTC/payday: extending rollover without fresh assessment
- Credit model not calibrated to product risk (short-term vs. mortgage)

---

## Fair Lending Analysis Framework

**Step 1 — Population analysis**: Identify the geographic market served; compare
application, approval, denial, and pricing distributions across protected classes
using HMDA data (if available) or proprietary data.

**Step 2 — Comparative file review**: For denial rate disparities exceeding 2:1 (black
box standard) or adverse action rates above industry norms, review a sample of denied
and approved files for comparably qualified applicants of different protected classes.

**Step 3 — Pricing disparity analysis**: Compare pricing (APR, fees, points) across
protected classes after controlling for objective risk factors (credit score, LTV, DTI,
loan purpose). Any unexplained pricing gap requires further analysis.

**Step 4 — Redlining screen**: Map application density by census tract against
demographic composition; identify CRA assessment areas with statistically low application
rates in minority-majority tracts vs. similar majority-White tracts.

**Step 5 — Policy review**: Identify any underwriting overlays, exception policies, or
discretionary pricing policies that could create disparate impact. Document business
necessity for each.

**Step 6 — Model review**: For AI/ML-based underwriting, assess for:

- Use of proxy features that correlate with protected class (zip code, surname, spending
  patterns)
- Disproportionate denial rates for protected class applicants after removing proxy features
- Absence of adverse impact testing and bias monitoring
- CFPB / DOJ fair lending expectations for explainability of automated decisions

**Red flags requiring immediate escalation**:

- Denial rate ratio Black:White or Hispanic:White > 2.0 without explainable credit factors
- Pricing disparities > 50 bps on APR by race/ethnicity after risk factor control
- Absence of any applications from minority-majority census tracts in the CRA assessment area
- Underwriting exception policy that approves higher proportions of majority-class applicants
- AI model with no documented adverse impact testing

---

## Severity Classification

Classify each finding using the four-tier system:

| Tier | Label                 | Definition                                                                                                                                                                                                                                                                                                                                    | Response Required                                                                              |
| ---- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 🔴   | **CRITICAL**          | Violation with high probability of regulatory enforcement action, individual consumer harm, or class action liability. Immediate remediation required. Examples: systematic APR understatement; failure to provide right of rescission; MLA violations; unlawful denial of mortgage on discriminatory basis; HCSTC price cap breach.          | Halt or suspend product/practice; immediate legal counsel; regulatory self-disclosure analysis |
| 🟠   | **NON-COMPLIANT**     | Clear regulatory violation without immediate CRITICAL risk. Remediation required within defined timeframe. Examples: adverse action notice missing required specific reasons; SECCI missing mandatory elements; CPA consent procedure non-compliant; loss mitigation dual-tracking violation.                                                 | Remediation within 30-60 days; document root cause; implement corrective controls              |
| 🟡   | **PARTIAL-COMPLIANT** | Requirements partially met; gaps exist but core obligation substantially satisfied. Remediation recommended. Examples: creditworthiness assessment process documented but not calibrated to product risk; Consumer Duty assessment performed but lacks vulnerability considerations; HMDA data collected but with gaps in demographic fields. | Remediation within 90 days; enhanced monitoring                                                |
| 🟢   | **COMPLIANT**         | Requirement met; no material gaps identified.                                                                                                                                                                                                                                                                                                 | Continue monitoring; note in compliance calendar                                               |

**Automatic CRITICAL triggers** (do not downgrade without qualified legal review):

- Any pricing above applicable cap (MLA 36% MAPR, SCRA 6%, HCSTC 0.8%/day, state usury)
- Failure to provide right of rescission on rescission-eligible transaction
- Systematic adverse action notices missing required specific reasons for protected-class applicants
- Redlining pattern with statistical significance and no legitimate business justification
- Failure to perform ATR assessment on QM-eligible transactions
- Using prohibited loan features in HOEPA high-cost mortgage
- HCSTC total charge cap exceeded
- GDPR Art. 22 violation (automated credit denial with no human review safeguard)

---

## Actionable Output per Finding

For each NON-COMPLIANT or CRITICAL finding, produce:

```
Finding ID: [JDXXX-NNN]
Regulation: [Statute/rule reference]
Severity: [CRITICAL / NON-COMPLIANT / PARTIAL-COMPLIANT]
Confidence: [Level — see Confidence Scoring]

Description:
[1-3 sentence description of the gap or violation. What is non-compliant and why.]

Current State:
[What the program currently does / doesn't do]

Required State:
[What the regulation requires, with specific citation]

Remediation Steps:
1. [Immediate action required — assign owner and deadline]
2. [System/process change required]
3. [Policy/procedure update required]
4. [Testing / monitoring required]
5. [Evidence to retain for examination]

Business Impact:
[Estimated enforcement risk, consumer harm exposure, class action risk, regulatory penalty range]

Priority: [Critical/High/Medium/Low — see Prioritization Framework]
```

---

## Prioritization Framework

| Priority     | Criteria                                                                                                          | Timeframe                                 | Examples                                                                                                          |
| ------------ | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Critical** | Active legal violation with imminent enforcement or consumer harm risk; automatic CRITICAL trigger conditions     | Immediate — halt practice, engage counsel | Rate cap violation; rescission right failure; systematic discriminatory denial                                    |
| **High**     | Clear regulatory non-compliance; high probability of examination finding; significant remediation effort required | 30-60 days                                | Adverse action notice deficiencies; SECCI missing elements; TRID tolerance breach; CPA non-compliance             |
| **Medium**   | Partial compliance gap; examination risk moderate; straightforward remediation                                    | 60-90 days                                | Creditworthiness assessment process gaps; Consumer Duty documentation deficiencies; HMDA data quality gaps        |
| **Low**      | Best-practice gaps or technical deficiencies with low examination priority; monitoring enhancements               | 90-180 days                               | Policy updates not reflecting recent guidance; enhanced HMDA field completion; annual compliance training updates |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any finding. Revise before delivery if any gate fails.

| Gate           | Rule                                                                                                                     | Fail Action                       |
| -------------- | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------- |
| **Source**     | Every compliance finding cites a specific statute, regulation section, or authoritative guidance                         | Add citation or mark [UNVERIFIED] |
| **Format**     | Citations follow consistent format: statute name, statutory/CFR/SI cite, specific section                                | Fix format                        |
| **Currency**   | Every cited threshold (APR cap, dollar amount, percentage) flagged as [VERIFY — thresholds update annually]              | Add verification flag             |
| **Domain**     | Analysis stays within identified regulatory scope; no cross-contamination (e.g., applying TRID to non-mortgage products) | Remove or re-scope                |
| **Confidence** | Uncertainty about regulatory interpretation explicitly stated                                                            | Add confidence qualifier          |

### Self-Interrogation for CRITICAL Findings

For any CRITICAL-classified finding, apply this 3-pass review before delivery:

**Pass 1 — Regulatory Chain Integrity**: Does the violation follow clearly from the cited
regulatory provision? Would a regulatory examiner (CFPB, FCA, national competent authority)
actually make this finding? Is the statute/rule currently in effect and not superseded?

**Pass 2 — Completeness**: Have all relevant regulatory provisions been considered?
Are there safe harbors, exemptions, or regulatory guidance that could cure or mitigate
the violation? Is there a more recent CFPB circular, FCA Dear CEO letter, or EBA guideline
that changes the analysis?

**Pass 3 — Challenge**: What is the strongest argument that this is not a violation?
Are there business justification defenses? Is this a good-faith compliance failure
with voluntary disclosure pathway? Would a court/tribunal likely uphold enforcement?

### Confidence Scoring

| Level        | Range     | Meaning                                                                            | Action                                                       |
| ------------ | --------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Definite** | 0.95-1.0  | Settled regulatory requirement; clear rule text; confirmed by examination guidance | State with full confidence                                   |
| **High**     | 0.80-0.94 | Strong regulatory basis; minor interpretive questions                              | State with brief caveat                                      |
| **Probable** | 0.60-0.79 | Good regulatory basis; some interpretive uncertainty; jurisdiction may vary        | State reasoning and contra-indicators; flag for legal review |
| **Possible** | 0.40-0.59 | Genuinely uncertain; competing regulatory interpretations or evolving guidance     | Flag for expert review; present both positions               |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative; threshold not yet verified                                | Do not assert as finding; flag [UNCERTAIN — verify]          |

---

## Glass Box Audit Trail

Append this YAML block to every assessment output for traceability:

```yaml
glass_box:
  skill_name: "legalcode-consumer-lending-compliance"
  version: "1.0 (2026-03-21)"
  mode: "Compliance assessment"
  jurisdictions_assessed: [] # list: US-Federal, US-[State], UK, EU-[MemberState]
  product_types_assessed: [] # list: closed-end mortgage, HELOC, personal loan, etc.
  lender_type: "" # national bank, nonbank, FCA-authorised, etc.
  assessment_date: ""
  regulatory_frameworks_applied: [] # list of statutes/directives assessed
  legalcode_mcp: "" # "Connected — [N] searches" or "Not connected"
  external_authority_file: "" # path to /tmp/legalcode-lending-authority.md or "Not created"
  findings_summary:
    critical: 0
    non_compliant: 0
    partial_compliant: 0
    compliant: 0
  key_thresholds_verified: false # true only if thresholds independently verified
  auto_triggers_checked: true # mandatory CRITICAL trigger table reviewed
  citation_quality_gates_passed: false
  self_interrogation_performed: false # for CRITICAL findings
  confidence_scores_assigned: false
  limitations:
    - "All threshold figures require annual verification — regulatory thresholds change"
    - "CCD2 transposition status varies by EU member state — verify before applying CCD2 obligations"
    - "Madden / valid-when-made preemption analysis requires jurisdiction-specific legal advice"
    - "Fair lending statistical analysis requires access to proprietary or HMDA data not assessed here"
    - "[VERIFY] markers throughout require verification against current authoritative sources"
  reviewer: "AI-assisted — requires qualified consumer finance counsel review before reliance"
```

---

## Anti-Patterns

Consumer lending compliance-specific patterns that produce unreliable or harmful outputs.
Do not do any of the following:

1. **Stating APR thresholds without verification flags**: APR-related thresholds (HOEPA,
   QM points/fees, MLA MAPR, state usury caps) update frequently. Never state a specific
   threshold figure without adding [VERIFY — updates annually].

2. **Applying TRID to non-mortgage products**: TRID (Loan Estimate / Closing Disclosure)
   applies only to closed-end credit secured by real property (with exceptions for reverse
   mortgages and HELOCs). Do not apply TRID disclosure requirements to personal loans,
   auto loans, or credit cards.

3. **Assuming NBA preemption for nonbanks**: National Bank Act interest rate preemption
   is available to national banks and federal savings associations. Nonbank lenders,
   fintech platforms, and bank-partner lending programs do not automatically inherit
   preemption. Madden exposure varies by circuit and requires independent legal analysis.

4. **Treating adverse action as a formality**: Adverse action notice non-compliance is a
   high-examination-priority CFPB and DOJ enforcement area, particularly where AI/ML
   models generate denials without explainable specific reasons. Do not classify adverse
   action notice deficiencies as Low priority.

5. **Conflating CCD1 and CCD2 obligations**: CCD2 does not apply until November 20, 2026.
   Applying CCD2 obligations to a current program assessment creates false compliance gaps.
   Assess CCD1 (current); assess CCD2 readiness separately as a forward-looking gap analysis.

6. **Ignoring the unfair relationships test (UK s.140A CCA 1974)**: This is a broad,
   open-ended judicial power with no time limit. Do not treat standard commercial terms
   as automatically compliant — assess whether pricing, terms, or practices could be
   challenged as creating an unfair relationship.

7. **Underweighting UDAAP / Consumer Duty risks**: Unfairness (UDAAP) and Consumer Duty
   (FCA) violations are inherently fact-dependent and not defined by bright-line rules.
   Do not classify UDAAP exposure as Low without affirmatively assessing whether fee
   structures, communications, or sales practices create substantial injury.

8. **Applying MLA without checking covered borrower status**: The Military Lending Act
   applies only to "covered borrowers" (active duty servicemembers, dependents). Creditors
   must use the DMDC database or a consumer report from a CRA using the DMDC database as
   a safe harbor [VERIFY current method]. Do not apply MLA to all consumers.

9. **Fair lending analysis without data**: Fair lending disparate impact requires statistical
   evidence. Do not assert a disparate impact violation without HMDA data, application data,
   or other statistical evidence. Identify the data gap and flag it as a preliminary risk
   indicator requiring quantitative analysis.

10. **Omitting state law analysis for US programs**: Federal law (TILA, ECOA, RESPA) provides
    a floor, not a ceiling. State laws frequently impose additional requirements (state-specific
    mortgage disclosures, right of rescission extensions, usury caps, state UDAP laws). Do not
    certify US compliance without confirming applicable state law obligations.

11. **Assuming HCSTC rules apply only to payday lenders**: The UK HCSTC price cap applies
    to any consumer credit agreement where the APR is ≥ 100%, regardless of lender type or
    product name. Installment loans, rent-to-own arrangements, or other products with high
    APRs may be caught. Screen APR, not product label.

12. **Treating Consumer Duty as an overlay on CONC only**: Consumer Duty is an independent
    FCA obligation with its own annual board assessment, governance, and documentation
    requirements. It does not simply require existing CONC compliance — it requires affirmative
    demonstration of good outcomes for consumers. Do not treat Consumer Duty as automatically
    satisfied by CONC compliance.

13. **Ignoring the 51% representative APR rule**: In UK and EU advertising, the "representative
    APR" must be a rate that at least 51% of consumers who enter credit agreements in response
    to the promotion actually receive. Using the best possible rate for advertising with most
    consumers receiving higher rates is non-compliant. Do not assess advertising compliance
    without checking the 51% basis.

14. **Applying Section 8 RESPA analysis to affiliate arrangements without AfBA analysis**:
    The RESPA affiliated business arrangement disclosure provides a safe harbor from
    Section 8 — but only if the three conditions are met (disclosure, no required use,
    return is from services actually performed). Do not treat affiliated arrangements as
    automatically compliant with Section 8 without assessing AfBA conditions.

15. **Failing to assess GDPR Article 22 for EU automated credit decisions**: Any EU consumer
    credit decision made by automated means (including credit scoring models) without meaningful
    human intervention may require Article 22 safeguards. This obligation exists regardless of
    CCD compliance. AI/ML underwriting must have human review pathway and right-to-explanation
    infrastructure.

16. **Stating that QM provides absolute protection from ATR liability**: General QM provides
    a conclusive safe harbor for APR ≤ APOR + 1.5% (for conforming first-lien loans), and a
    rebuttable presumption for higher-APR QM. Small creditor portfolio QM has different
    thresholds. Do not state that any QM loan is completely immune from ATR claims without
    verifying the specific QM subtype and APR relative to APOR [VERIFY current thresholds].

17. **Missing SCRA analysis for servicer clients**: SCRA imposes obligations not only on
    original lenders but on mortgage servicers (foreclosure restrictions, interest rate
    reduction on request). Servicer compliance assessments must include SCRA as a separate
    checklist item, not fold it into origination compliance only.

---

## Writing Standards

Apply these standards before delivering any output:

1. **Cite specifically**: "§ 1026.43(c)(2)" not "Regulation Z"; "CONC 5.1.2R" not
   "CONC responsible lending rules"
2. **Distinguish jurisdictions**: Do not write "the APR rule requires" — write "Under
   US TILA/Regulation Z..." or "Under FCA CONC..."
3. **Flag thresholds as current-year**: Any dollar amount, percentage cap, or de minimis
   threshold should be followed by "[VERIFY — thresholds update annually]"
4. **Write in active voice**: "The lender must provide..." not "The disclosure is
   required to be provided by..."
5. **Remediation in imperative form**: "Update adverse action notice template to include
   the four specific reasons..." not "The adverse action notice template should consider..."
6. **Avoid regulatory jargon without definition on first use**: Define MLA, MAPR, ATR,
   QM, TRID, SECCI, CONC, HCSTC on first use for non-specialist audiences
7. **Do not assert conclusions without citing authority**: Every compliance classification
   must cite the specific rule that is violated or satisfied
8. **Confidence qualifiers are not disclaimers**: Confidence scoring describes analytical
   confidence in the finding; it does not substitute for the overall disclaimer — both
   must appear

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

Use legalcode-mcp in Step 4 to retrieve:

- Current text of 12 CFR Part 1026 (Regulation Z), 12 CFR Part 1002 (Regulation B),
  12 CFR Part 1024 (Regulation X), and any relevant CFPB examination procedures
- Current HOEPA, QM, MLA, and annual threshold figures [these update annually]
- FCA Handbook CONC provisions at current version
- CCD2 transposition status in the relevant EU member state
- Recent CFPB, FCA, and national competent authority enforcement actions and guidance
  from the prior 24 months
- Current HMDA reporting thresholds and field requirements

Save to `/tmp/legalcode-lending-authority.md` and use throughout the assessment for
citation accuracy.

**Without legalcode-mcp:**

- Proceed using the regulatory framework reference in this skill
- Mark all specific thresholds and quantitative figures with [VERIFY — thresholds update annually]
- Mark all enforcement action references with [VERIFY — verify currency and relevance]
- Note in Glass Box: `legalcode_mcp: "Not connected — all thresholds and citations require independent verification"`
- Recommend the user independently verify all findings against current CFPB/FCA/EBA sources

---

## Output Format Template

```markdown
# Consumer Lending Compliance Assessment

**Program / Product**: [name]
**Assessment Date**: [date]
**Jurisdictions**: [US-Federal | US-[State] | UK | EU-[Member State]]
**Product Type**: [closed-end mortgage | personal loan | BNPL | credit card | etc.]
**Lender Type**: [national bank | nonbank | FCA-authorised | etc.]
**Prepared by**: Legalcode Consumer Lending Compliance Skill (AI-assisted)
**Status**: DRAFT — requires qualified legal counsel review before reliance

---

## Executive Summary

| Metric                     | Value                            |
| -------------------------- | -------------------------------- |
| Critical findings          | [N]                              |
| Non-Compliant findings     | [N]                              |
| Partial-Compliant findings | [N]                              |
| Compliant domains          | [N]                              |
| Overall risk rating        | [CRITICAL / HIGH / MEDIUM / LOW] |
| Key action required        | [top 1-2 sentences]              |

---

## Finding Index

| ID   | Domain   | Finding Summary  | Severity | Priority   | Owner             |
| ---- | -------- | ---------------- | -------- | ---------- | ----------------- |
| [ID] | [Domain] | [1-line summary] | [tier]   | [priority] | [TBD / suggested] |

---

## Detailed Findings

### [Finding ID]: [Finding Title]

**Regulation**: [Cite]
**Severity**: [🔴 CRITICAL / 🟠 NON-COMPLIANT / 🟡 PARTIAL-COMPLIANT]
**Confidence**: [Level — range]

**Description**: [2-4 sentences]

**Current State**: [What exists today]

**Required State**: [What the regulation requires — specific cite]

**Remediation Steps**:

1. ...
2. ...
3. ...

**Business Impact**: [Enforcement risk, consumer harm potential, penalty range]

**Priority**: [Critical / High / Medium / Low]

---

## Compliant Domains

| Domain   | Regulatory Basis | Notes                                  |
| -------- | ---------------- | -------------------------------------- |
| [Domain] | [Cite]           | [Brief note on evidence of compliance] |

---

## Prioritized Remediation Action Plan

| Priority | Finding      | Deadline      | Owner   | Status |
| -------- | ------------ | ------------- | ------- | ------ |
| Critical | [Finding ID] | Immediate     | [Owner] | Open   |
| High     | [Finding ID] | [30-60 days]  | [Owner] | Open   |
| Medium   | [Finding ID] | [60-90 days]  | [Owner] | Open   |
| Low      | [Finding ID] | [90-180 days] | [Owner] | Open   |

---

## Compliance Calendar — Key Dates and Thresholds

| Item                                  | Current Value                     | Next Verification         |
| ------------------------------------- | --------------------------------- | ------------------------- |
| Regulation Z exemption threshold      | $[amount] [VERIFY]                | January annually          |
| QM points/fees threshold              | $[amount] [VERIFY]                | January annually          |
| HOEPA APR trigger (first lien)        | APOR + [X]% [VERIFY]              | Annually                  |
| EU CCD2 application date              | November 20, 2026                 | Pre-implementation review |
| UK Consumer Duty closed book deadline | July 31, 2024                     | Completed                 |
| HMDA reporting threshold              | [X] closed-end mortgages [VERIFY] | Annually                  |

---

## Glass Box Audit Trail

[Insert YAML block from Glass Box Audit Trail section]
```

---

## Localization Notes

This skill covers three major regulatory domains. Key localization considerations:

- **US state law**: This skill covers federal law in detail. State law (state UDAP, state
  mortgage lending laws, state usury, state foreclosure procedures) requires separate state-by-state
  analysis. Do not certify US compliance without adding a state law assessment.
- **EU member state transposition**: CCD1 has been transposed differently across member states;
  national provisions add detail beyond the directive minimum. CCD2 transposition is ongoing
  (deadline November 2025; application November 2026). Always check national transposition law,
  not only the directive.
- **UK post-Brexit**: UK consumer credit regulation is independent of EU law post-January 31, 2020. The UK retained CCD1-equivalent rules in CONC and CCA 1974, but will diverge further
  as EU implements CCD2 without UK equivalent reform.
- **Crypto-asset and BNPL products**: Both are subject to rapidly evolving regulation across
  all three jurisdictions. Treat any BNPL or crypto-lending assessment as requiring enhanced
  current-state regulatory verification.

---

## Provenance

Created by Legalcode (2026-03-21). Legalcode original synthesis. Research basis:
2-agent research pipeline covering US consumer lending law (TILA/Reg Z, ECOA/Reg B,
Fair Lending, RESPA, usury regulation, CFPB UDAAP), UK FCA CONC sourcebook / CCA 1974 /
Consumer Duty / HCSTC rules, EU CCD1/CCD2/MCD regulatory framework, GDPR Article 22,
and member state implementations (Germany BGB §§491-505, France Consumer Code Art.
L312-1 et seq., Netherlands Wft). No prior skills on this topic in the repository.
All statutory citations carry [VERIFY] obligation given frequent threshold amendments.
