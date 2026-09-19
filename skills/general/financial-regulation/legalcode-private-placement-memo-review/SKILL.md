---
name: legalcode-private-placement-memo-review
description: Review Private Placement Memoranda (PPMs) for disclosure adequacy, securities law compliance,
  and liability exposure. Use when reviewing a PPM, offering memorandum (OM), confidential information
  memorandum (CIM), private offering document, Reg D offering circular, Reg S offshore offering document,
  hedge fund offering memo, real estate fund PPM, startup PPM, or any private securities offering document.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review Private Placement Memoranda (PPMs) for disclosure adequacy, securities law compliance, and liability exposure. Analyzes risk factor quality, use of proceeds specificity, management descriptions, financial statement sufficiency, subscription terms, investor qualification procedures, and Reg D / Reg S compliance. Flags material omissions, boilerplate risk factors, bad actor disqualification issues, integration doctrine traps, and state Blue Sky notice requirements. Use when reviewing a PPM, offering memorandum (OM), confidential information memorandum (CIM), private offering document, Reg D offering circular, Reg S offshore offering document, hedge fund offering memo, real estate fund PPM, startup PPM, or any private securities offering document. Also triggers on: "review this offering document," "check PPM compliance," "flag material omissions," "is our risk factor section adequate," "review our use of proceeds," "check accredited investor procedures," "Reg D compliance review," "Reg S eligibility," "506(b) vs 506(c) analysis," or "private placement liability check." Primarily US-focused (Securities Act of 1933, Reg D, Reg S, Rule 10b-5, §12(a)(2), §17(a)) with markers for international overlay. Produces GREEN/YELLOW/RED classification with Disclosure Quality Score, material-omission flags, and Glass Box audit trail.


# Legalcode Private Placement Memorandum Review

> **Disclaimer**: This skill provides a framework for AI-assisted PPM review. It does not
> constitute legal advice and does not constitute legal counsel in connection with any
> securities offering. All outputs must be reviewed by a qualified securities attorney
> licensed in the relevant jurisdiction before use or reliance. Securities laws change
> frequently and vary by jurisdiction; verify current applicability before relying on any
> provision described here. Statutory and case law references cited from memory carry
> hallucination risk — verify against authoritative sources (SEC.gov, Westlaw, LexisNexis)
> before relying on them. This skill does not evaluate whether any particular offering is
> exempt from registration; that determination requires qualified counsel.

---

## Purpose and Scope

This skill reviews Private Placement Memoranda and similar offering documents used in
unregistered securities offerings. It identifies disclosure gaps, securities law compliance
issues, material omissions, and liability exposure — from the perspective of either the
issuer (preparing or stress-testing the PPM) or a prospective investor (evaluating
completeness and accuracy).

**Covers:**

- Offering structure assessment: exemption claimed, investor eligibility, integration risk
- Risk factor analysis: quality, specificity, currency, material omission detection
- Use of proceeds: specificity, consistency with business description, completeness
- Management disclosures: background completeness, conflicts of interest, compensation
- Financial statement requirements: sufficiency by offering size and exemption type
- Subscription terms and investor qualification procedures
- Reg D / Reg S compliance (Rule 504, 506(b), 506(c); Reg S Category 1/2/3)
- Bad actor disqualification screening (Rule 506(d))
- State Blue Sky notice filing requirements
- Anti-fraud liability exposure (Rule 10b-5, §12(a)(2), §17(a))
- Material omission detection using TSC/Basic materiality standard

**Does not:**

- Determine whether a specific offering qualifies for a specific exemption (requires counsel)
- Draft a PPM from scratch (see drafting-specific skills)
- Provide advice on whether to invest in any offering
- Constitute legal advice or replace qualified securities counsel
- Review registered offerings (S-1, S-11, etc.) — those require different analysis

## Jurisdiction and Governing Law

This skill is primarily US-focused. The US securities law framework is federal (Securities
Act of 1933, Securities Exchange Act of 1934, and the rules thereunder), supplemented by
state Blue Sky laws. The core framework:

- **Federal**: Securities Act of 1933 §§ 4(a)(2), 5, 12; Regulation D (17 C.F.R. §§
  230.500–230.508); Regulation S (17 C.F.R. §§ 230.901–930.905); Rule 10b-5; §17(a)
- **State**: Blue Sky laws — partially preempted by NSMIA (National Securities Markets
  Improvement Act of 1996, codified at 15 U.S.C. § 77r) for "covered securities" under
  Rule 506; notice filing and fee requirements remain even for covered securities

[JURISDICTION-SPECIFIC] When the offering includes non-US investors or issuers:

- **EU/EEA**: Prospectus Regulation (EU) 2017/1129 and its exemptions for private
  placements; MiFID II client classification for investor eligibility [VERIFY]
- **UK**: Financial Services and Markets Act 2000 §§ 19, 21; FCA Handbook COBS; private
  placement exemptions under FSMA Sch. 11A [VERIFY]
- **Cayman Islands**: Not a registered offering context; typical for hedge fund offshore
  feeder structures combined with Reg S [VERIFY]
- **Canada**: National Instrument 45-106 private placement exemptions; accredited investor
  definition differs from US [VERIFY]
- For any non-US jurisdiction, verify local private placement exemption criteria with
  local counsel and mark all citations [VERIFY].

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the direction or depth of the analysis
- The exemption type or offering structure is unclear (materially affects the compliance
  framework)
- The issuer's stage, type, or industry creates special disclosure requirements
- Whether this is an issuer-side review (stress-test) or investor-side review (diligence)
  is ambiguous

Use the **⟁ CLARIFY** pattern (structured options with descriptions) wherever marked
below. If the user has already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept the PPM

Accept the offering document in any of these formats:

- **File**: PDF, DOCX, or other document format
- **URL**: Link to a PPM in a document system or data room
- **Pasted text**: PPM sections pasted directly into the conversation
- **Partial PPM**: One or more sections only (risk factors, use of proceeds, etc.)

If no document is provided, prompt the user to supply one.

If only partial sections are provided, note which sections are absent and adjust the
review scope accordingly. Do not fabricate analysis for sections not reviewed.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask the user these questions. Skip any
already answered by the initial prompt.

1. **Perspective**: Who are you in this transaction?
   - Options: **Issuer / issuer's counsel** (preparing or stress-testing the PPM),
     **Prospective investor** (diligence review), **Investor's counsel**, **Broker-dealer
     reviewing for suitability**, **Other (describe)**
   - _Why this matters_: The analysis focus shifts materially — issuers want to identify
     and cure disclosure gaps before closing; investors want to identify undisclosed risks
     and evaluate completeness.

2. **Exemption claimed**: What securities law exemption is the offering relying on?
   - Options: **Rule 506(b)** (no general solicitation, up to 35 non-accredited),
     **Rule 506(c)** (general solicitation, accredited only, enhanced verification),
     **Rule 504** (up to $10M, possible state compliance required), **Reg S only**
     (offshore offering), **Reg D + Reg S** (combined US/offshore offering), **§4(a)(2)**
     (not relying on Reg D safe harbor), **Unknown / need to assess**
   - _Why this matters_: The applicable exemption determines disclosure obligations,
     investor eligibility rules, financial statement requirements, and state law treatment.

3. **Issuer type and stage**: What type of issuer?
   - Options: **Operating company (startup/early stage)**, **Operating company (growth
     stage / revenue-generating)**, **Reporting company (SEC registrant)**, **Real estate /
     REIT / fund**, **Hedge fund / private equity fund**, **Special purpose vehicle**,
     **Other (describe)**
   - _Why this matters_: Real estate funds, hedge funds, and operating companies have
     different standard disclosure frameworks. Reporting companies have different financial
     statement obligations.

4. **Deal context**: Any specific concerns or focus areas?
   - Options: **Risk factor adequacy**, **Use of proceeds**, **Management disclosures /
     conflicts**, **Financial statement sufficiency**, **Investor qualification procedures**,
     **Reg D compliance mechanics**, **Bad actor screening**, **State Blue Sky compliance**,
     **Full review (all sections)**, **Other**
   - Allow multiple selections.
   - _Why this matters_: Focuses the analysis on what the user needs most. A "full review"
     triggers all 8 analysis modules below.

5. **Offering size and timeline**: Deal size and closing timeline?
   - Free text. Prompt: "Offering size affects financial statement requirements and the
     depth of SEC scrutiny. Timeline affects urgency prioritization."

If the user provides partial context, proceed with reasonable defaults and state assumptions
explicitly (e.g., "I am assuming this is a Rule 506(b) offering from an operating company's
perspective — let me know if that's wrong").

### Step 3: Securities Law Exemption Assessment

Before beginning substantive analysis, assess the offering's claimed exemption(s) and
flag any structural compliance issues.

#### 3a. Identify and Validate the Exemption

| Exemption        | Dollar Limit     | Investor Limit                               | General Solicitation        | NSMIA Covered Security    | Financial Stmt Required                            |
| ---------------- | ---------------- | -------------------------------------------- | --------------------------- | ------------------------- | -------------------------------------------------- |
| **Rule 504**     | $10M / 12 months | None                                         | Generally no (exceptions)   | No                        | None mandated                                      |
| **Rule 506(b)**  | None             | Unlimited accredited + max 35 non-accredited | Prohibited                  | Yes                       | Rule 502(b) if non-accredited present              |
| **Rule 506(c)**  | None             | Accredited only                              | Permitted                   | Yes                       | None mandated (but investor verification required) |
| **§4(a)(2)**     | None             | No safe harbor limit                         | Prohibited                  | No (unless also Rule 506) | Facts and circumstances                            |
| **Reg S Cat. 1** | None             | Offshore only                                | No directed selling efforts | N/A                       | Offshore regime                                    |
| **Reg S Cat. 2** | None             | Offshore, 40-day hold                        | No directed selling efforts | N/A                       | Offshore regime                                    |
| **Reg S Cat. 3** | None             | Offshore, 1-year hold (equity)               | No directed selling efforts | N/A                       | Offshore regime                                    |

**⟁ CLARIFY** — If the PPM does not clearly state the exemption being claimed, or if the
exemption statement appears inconsistent with offering terms:

- "I cannot identify which exemption this offering is relying on. The PPM should clearly
  state the exemption. Can you confirm whether this is Rule 506(b), 506(c), or another
  exemption? The compliance requirements differ substantially."

#### 3b. Check Integration Risk

Assess whether prior or concurrent offerings could integrate with this offering and blow
the exemption. Under SEC integration doctrine (Regulation D Rule 502(a) and the
general integration analysis under _SEC v. Murphy_, _Continental Information Systems_):

- Offerings within 6 months before or after may integrate if they are part of the same
  plan of financing
- Integration can destroy a Reg D exemption by converting an exempt offering into an
  unregistered public offering
- Flag if the PPM discloses other recent or contemporaneous offerings without an
  integration analysis

#### 3c. Bad Actor Disqualification Check (Rule 506(d))

For any Rule 506 offering, the following "covered persons" must not be subject to
disqualification:

- The issuer and any predecessors or affiliated issuers
- Directors, general partners, managing members, and executive officers of the issuer
- Any person owning 20%+ of the issuer's voting equity
- Promoters connected with the issuer
- Investment managers and their principals (for pooled investment funds)
- Any underwriter, broker-dealer, or solicitor participating in the offering

Disqualifying events include: SEC orders, criminal convictions for securities violations,
final orders from banking regulators, certain regulatory orders. Bad actor events after
September 23, 2013 automatically disqualify; pre-2013 events require disclosure.

**Red flag triggers:**

- PPM does not include a bad actor representation or certificate
- Disclosure section on "certain legal proceedings" is absent or vague about disqualifying events
- Issuer relies on blank exception (Rule 506(d)(2)(iv)) without required disclosure

#### 3d. Form D Filing Assessment

For all Reg D offerings, issuers must file Form D with the SEC within 15 days of the
first sale of securities (17 C.F.R. § 230.503).

- Assess whether the PPM contains a Form D filing reminder or acknowledgment
- Note that many states require parallel notice filings (Form D or state-specific forms)
  and fees — Rule 506 preemption does not excuse notice filing requirements

[JURISDICTION-SPECIFIC] Key states with additional requirements beyond basic notice filing:

- **New York**: Form 99 and filing fee (varies by aggregate offering size) [VERIFY]
- **California**: Form D notice filing within 15 days of first sale to CA investor [VERIFY]
- **Texas**: Form D + filing fee with Texas State Securities Board [VERIFY]
- **Florida**: Form D notice within 120 days [VERIFY]

### Step 4: Gather Legal Authority (legalcode-mcp)

Use **legalcode-mcp** to build a working legal reference file before analyzing sections.

**Research process:**

1. Identify the exemption(s) and governing state law from the PPM.
2. Search legalcode-mcp for:
   - Current text of Regulation D rules 501–506 (17 C.F.R. §§ 230.501–230.506)
   - Regulation S rules 901–905 (if Reg S is claimed)
   - Rule 10b-5 and §17(a) anti-fraud provisions
   - Materiality standard cases: _TSC Industries v. Northway_, 426 U.S. 438 (1976);
     _Basic Inc. v. Levinson_, 485 U.S. 224 (1988)
   - Recent SEC enforcement actions involving PPM disclosure failures
   - Applicable state Blue Sky statutes (if specific state compliance is at issue)

3. Save results to `/tmp/legalcode-ppm-review-authority.md`:

   ```markdown
   # Legal Authority Reference — PPM Review

   ## Offering: [Issuer name / offering title]

   ## Exemption: [Rule 506(b) / 506(c) / 504 / Reg S / combined]

   ## Date Gathered: [date]

   ### Federal Securities Laws

   - [Statute or Rule, current text or summary]

   ### Materiality Case Law

   - [Case, citation, key holding]

   ### Recent SEC Enforcement

   - [Action name, date, key facts relevant to review]

   ### State Blue Sky

   - [Applicable state statute or requirement — VERIFIED or UNVERIFIED]
   ```

4. Use this reference throughout the analysis. Mark legalcode-mcp-sourced citations as
   VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**

- Mark all statutory and case law references [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed using general securities law knowledge, with appropriate caveats

### Step 5: PPM Structural Assessment

Read the entire PPM before section-by-section analysis to identify:

1. **Document completeness**: What standard sections are present and absent?
2. **Internal consistency**: Do representations in one section contradict another?
   (e.g., "experienced management team" in executive summary vs. thin backgrounds in
   management section; "proven business model" vs. startup-stage financials)
3. **Cross-section coherence**: Does use of proceeds align with business description?
   Do risk factors reflect the actual risks disclosed in the business description?
4. **Document currency**: What date is the PPM? If older than 12 months, staleness is a
   material concern for fast-moving businesses.
5. **Missing sections**: Identify which of the 8 standard sections below are entirely absent.

**⟁ CLARIFY** — For very long PPMs (100+ pages) or fund documents with multiple exhibits:

- "This is a complex offering document. Should I perform a **full review** of all 8
  disclosure modules, or a **priority review** focused on [user's stated concerns]?"
- "The PPM incorporates [exhibit/appendix] by reference. Should those documents be
  reviewed as part of this analysis?"

### Step 6: Section-by-Section Disclosure Analysis

Analyze each of the 8 standard PPM sections. Classify each finding as GREEN, YELLOW, RED,
or MATERIAL-OMISSION (see Severity Classification below).

**Coverage depth:**

| #   | Section                                     | Depth    | Key Issues                                                         |
| --- | ------------------------------------------- | -------- | ------------------------------------------------------------------ |
| 1   | Risk Factors                                | Deep     | Specificity, currency, boilerplate, material omissions             |
| 2   | Use of Proceeds                             | Deep     | Specificity, allocation detail, contingency disclosures            |
| 3   | Management & Compensation                   | Deep     | Background completeness, conflicts, compensation disclosure        |
| 4   | Financial Statements                        | Deep     | Sufficiency for exemption type, audit status, currency             |
| 5   | Offering Structure / Securities             | Deep     | Securities description, pricing, liquidation rights, anti-dilution |
| 6   | Subscription Terms / Investor Qualification | Standard | Accredited investor verification, subscription agreement terms     |
| 7   | Business Description                        | Standard | Fair presentation, material business risks, competitive landscape  |
| 8   | Capitalization                              | Standard | Pre/post-offering cap table, dilution disclosure                   |

---

## Section Analysis Reference

### 1. Risk Factors

Risk factors are the primary defense against anti-fraud liability. A PPM's risk factor
section must disclose all material risks with enough specificity that investors can
meaningfully evaluate them. The SEC, in enforcement actions and guidance, has consistently
held that generic, boilerplate risk factors provide little protection.

**Key elements to analyze:**

- **Specificity**: Are risk factors specific to this issuer and offering, or are they
  generic "could affect" language applicable to any company? Under _SEC v. Lucent_,
  _SEC v. Syntax-Brillian_, and SEC guidance, risk factors must describe the specific
  manner in which the risk could affect the issuer — not merely that a risk "may" exist.
- **Completeness**: Do the risk factors cover:
  - [ ] Risks related to the industry and competitive environment
  - [ ] Risks specific to the issuer's business model and stage
  - [ ] Risks related to the securities being offered (dilution, liquidation preferences,
        limited transferability, lack of public market)
  - [ ] Risks related to the offering and use of proceeds
  - [ ] Management / key person risk
  - [ ] Regulatory and legal risks specific to the industry
  - [ ] Macro/economic risks that are material to this specific business
  - [ ] For technology companies: IP risk, cybersecurity risk, data privacy risk
  - [ ] For real estate: property-specific risks, market concentration, leverage risks
  - [ ] For funds: strategy risks, counterparty risks, leverage risks, redemption risks
- **Currency**: Do risk factors reflect the current business and market environment?
  Outdated risk factors (referencing prior-year market conditions as current) are a
  liability exposure.
- **Material omissions**: Would a reasonable investor consider any known, undisclosed
  risk material under the _TSC Industries / Basic_ standard? Under _Basic Inc. v.
  Levinson_, 485 U.S. 224 (1988), information is material if there is a "substantial
  likelihood that the disclosure would have been viewed by the reasonable investor as
  having significantly altered the total mix of information available."
- **Boilerplate flag**: Flag risk factors that use language applicable to virtually any
  company ("we may face competition," "we may be unable to attract key personnel") without
  specificity about why these risks are material to this particular issuer.

**Common issues:**

- Risk factors present but entirely generic (provides minimal 10b-5 defense)
- Known, specific adverse events buried in risk factors rather than prominently disclosed
  in the executive summary or a special notice
- No risk factor addressing limited transferability and lack of liquidity for investors
- No risk factor disclosing that the securities have not been registered and resale is
  restricted
- For Rule 506(c): no risk factor disclosing that investor self-certification alone does
  not guarantee enhanced verification compliance

[JURISDICTION-SPECIFIC] For international offerings under Reg S, risk factors should
also address: currency/exchange rate risk, political and regulatory risk in the issuer's
operating jurisdictions, and foreign legal system risk. [VERIFY]

### 2. Use of Proceeds

The use of proceeds section must specifically identify how offering proceeds will be
deployed. Vague "general working capital" allocations are a common SEC enforcement focus.

**Key elements to analyze:**

- **Specificity**: Does the section itemize how proceeds will be used with dollar amounts
  or percentages? Minimum specificity includes approximate allocation percentages to each
  use category.
- **Prioritization**: If the offering has a minimum/maximum structure, are there different
  use-of-proceeds scenarios for minimum vs. maximum raising?
- **Completeness**: Does the section disclose:
  - [ ] Offering costs and commissions (must disclose aggregate compensation to placement
        agents, finders, and broker-dealers)
  - [ ] Debt repayment (if proceeds will repay insider loans or related-party debt, this is
        a RED flag requiring prominent disclosure)
  - [ ] Officer/director compensation from proceeds (a MATERIAL-OMISSION if not disclosed)
  - [ ] Timeframe for deployment of proceeds
  - [ ] What happens if the full offering amount is not raised
- **Consistency**: Do use-of-proceeds allocations align with the business description's
  stated strategy? Inconsistencies suggest document drafting errors or, in worse cases,
  potential fraud.
- **Related-party payments**: Any proceeds flowing to insiders, affiliates, or related
  parties must be disclosed prominently with the relationship, amount, and basis for the
  payment.

**Common issues:**

- "General working capital" as the only stated use of proceeds (provides minimal
  anti-fraud defense)
- Offering costs understated or omitted
- Related-party repayments disclosed only in footnotes to financials, not in use of proceeds
- No disclosure of what happens if the offering is not fully subscribed

### 3. Management and Compensation

Management disclosures are among the most scrutinized areas in SEC enforcement actions.
Omissions about criminal history, prior business failures, and conflicts of interest are
leading causes of PPM-related liability.

**Key elements to analyze:**

- **Background completeness**: For each director, executive officer, and key person, does
  the PPM disclose:
  - [ ] Full name
  - [ ] Title and role with the issuer
  - [ ] All professional experience and positions (typically 5 years minimum, though
        longer for material prior roles)
  - [ ] Prior business failures, bankruptcies, and formal SEC or regulatory proceedings
        (required under Rule 10b-5 / §12(a)(2) materiality)
  - [ ] Relevant educational background
  - [ ] Current time commitment to the issuer (important for part-time management)
- **Compensation disclosure**: For operating companies, the PPM should disclose:
  - [ ] Current salary or compensation arrangements
  - [ ] Equity holdings and option grants
  - [ ] Related-party transactions and self-dealing arrangements
  - [ ] Deferred compensation and earn-out arrangements
- **Conflicts of interest**: Does the PPM disclose:
  - [ ] Outside business interests that compete with or could divert opportunities from
        the issuer
  - [ ] Related-party transactions and their arms-length (or not) nature
  - [ ] Side letter arrangements with certain investors (if material)
  - [ ] Investment advisor registration status (critical for fund managers)
- **Investment advisor status** (for funds): Does the fund manager disclose:
  - [ ] Whether it is registered with the SEC under the Investment Advisers Act of 1940
  - [ ] If exempt (e.g., venture capital fund adviser exemption, private fund adviser
        exemption under §203(l) or §203(m)), on what basis

**Common issues:**

- Biographies limited to current role — omit prior roles, especially prior failures
- Prior SEC enforcement actions, civil judgments, or criminal proceedings omitted
  (this is a MATERIAL-OMISSION and a potential disqualifying event under Rule 506(d))
- Related-party transactions disclosed in financial statement footnotes only, not in
  the PPM's conflicts section
- Time commitment not disclosed for managers running multiple funds or businesses
- Fund manager not disclosing adviser registration status or exempt status

### 4. Financial Statements

Financial statement sufficiency is one of the most technically complex areas of PPM review.
Requirements vary by exemption type and offering size.

**Rule 506(b) with non-accredited investors — Rule 502(b) disclosure requirements:**

When non-accredited (but sophisticated) investors participate in a Rule 506(b) offering,
issuers must provide the financial information specified in Rule 502(b)(2)(i)–(vi), which
mirrors registration statement requirements for comparable offering sizes:

| Offering Size  | Financial Statement Requirement                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| ≤ $2M          | Balance sheet (90 days old max) + statements of operations, changes in stockholders' equity, and cash flows for the most recent fiscal year |
| > $2M to $7.5M | 2 years of audited financial statements + unaudited interim statements                                                                      |
| > $7.5M        | Audited statements as required by SEC Regulation S-X (2 years of income statements; 3 years for reporting companies)                        |

**Rule 506(b) or 506(c) with accredited investors only:**

- No mandated financial statement format under Regulation D
- However, anti-fraud liability requires disclosure of material financial information
- Market standard: 2 years of audited (or at minimum reviewed) financial statements + most recent interim period

**Rule 504:**

- No financial statement requirements under the rule
- Anti-fraud liability still applies; material financial information must be disclosed

**Key elements to analyze:**

- **Audit status**: Are financial statements audited by an independent registered public
  accounting firm (PCAOB-registered for public companies; AICPA-standards for private)?
  If unaudited, are they clearly labeled as such?
- **Currency**: Are financial statements within acceptable staleness limits? Audited annual
  financials should be accompanied by unaudited interim statements if the audit is more
  than 135 days old (tracking registration statement staleness rules as a practical
  standard [VERIFY]).
- **GAAP compliance**: Do financial statements state that they are prepared in accordance
  with US GAAP (or IFRS with reconciliation for foreign private issuers)?
- **Going concern**: If the auditor's report contains a going concern qualification, is it
  prominently disclosed in the PPM (not just buried in the financials)?
- **Consistency with business description**: Do the financial statements support the
  business description's characterizations (e.g., is the company described as "growing
  rapidly" consistent with revenue trends)?
- **Related-party transactions**: Are related-party transactions disclosed in financial
  statement footnotes? Are they consistent with the PPM's conflicts disclosure?

**Common issues:**

- Unaudited financials in an offering where audits are market standard or required
- Financial statements older than 12 months with no interim update
- Going concern qualification not highlighted in the PPM cover page or executive summary
- Pro forma financial statements presented without being clearly labeled as pro forma
- No financial statements at all (a MATERIAL-OMISSION for any material offering)

### 5. Offering Structure and Securities Description

The PPM must clearly describe the securities being offered so investors can evaluate what
they are buying.

**Key elements to analyze:**

- **Securities type and terms**: For equity (common stock, preferred stock, LLC interests,
  limited partnership interests):
  - [ ] Voting rights, or absence thereof
  - [ ] Liquidation preference and priority (for preferred)
  - [ ] Anti-dilution protections (for preferred): full ratchet vs. weighted average
  - [ ] Conversion rights, conversion price, and conversion triggers
  - [ ] Dividend rights and cumulative dividend provisions
  - [ ] Drag-along and tag-along rights
  - [ ] Registration rights (if any)
  - [ ] Redemption rights, if any
  - [ ] Pre-emptive rights in future rounds
- **Securities type and terms**: For debt instruments (convertible notes, SAFEs, revenue
  share, promissory notes):
  - [ ] Principal amount, maturity date, interest rate
  - [ ] Conversion mechanics, valuation cap, discount rate (for convertible instruments)
  - [ ] Security interest (if secured) or subordination position (if unsecured)
  - [ ] Default and acceleration provisions
  - [ ] Most Favored Nation (MFN) rights in later similar instruments
- **Offering terms**:
  - [ ] Offering price and maximum offering amount
  - [ ] Minimum investment amount
  - [ ] Minimum offering amount (if applicable) — if there is a minimum, what happens to
        escrowed funds if it is not met?
  - [ ] Offering period and any extension rights
  - [ ] Placement agent compensation (aggregate fees, success fee percentages, warrants)
- **Dilution disclosure**: The PPM should quantify expected dilution from the offering,
  including impact of outstanding options, warrants, convertible instruments, and the
  current offering on existing shareholders.

**Common issues:**

- No description of anti-dilution provisions — critical for preferred stock investors
- Placement agent warrants or compensation not disclosed or understated
- No disclosure of pay-to-play provisions that could affect existing investors
- Liquidation preference terms described inconsistently with the actual charter documents
- No disclosure of the capitalization table pre- and post-offering

### 6. Subscription Terms and Investor Qualification

**Key elements to analyze:**

- **Accredited investor representations**: The subscription agreement should require investors
  to represent that they qualify as accredited investors under Rule 501(a). Categories include:
  - Natural persons with net worth > $1M (excluding primary residence) individually or
    jointly with spouse [amended 2020]
  - Natural persons with income > $200K (or $300K joint) in each of the past 2 years with
    reasonable expectation of same in current year
  - Natural persons holding Series 7, 65, or 82 licenses in good standing [added 2020]
  - "Knowledgeable employees" of the fund for fund offerings [added 2020]
  - Entities (corporations, partnerships, LLCs, trusts, etc.) with assets > $5M
  - Entities all of whose equity owners are accredited investors ("all owners" test)
  - Registered investment advisers and broker-dealers
  - Family offices with > $5M in AUM [added 2020]
  - SEC- and state-registered investment companies (including SBIC)
  - Defined employee benefit plans with plan assets > $5M

- **Rule 506(c) enhanced verification**: If the offering claims Rule 506(c) (general
  solicitation), the issuer must take "reasonable steps" to verify accredited investor
  status. Self-certification alone is insufficient for Rule 506(c). Reasonable steps include:
  - [ ] Tax returns (IRS Form 1040) for income-based accreditation
  - [ ] Written confirmation from CPA, attorney, broker-dealer, or registered investment
        adviser that the investor is accredited
  - [ ] Net worth verification: bank/brokerage statements within 90 days + credit report
        (for net worth ≥ $1M excluding residence)
  - [ ] Verification platform certificates (Parallel Markets, VerifyInvestor, etc.) [VERIFY]
  - Document the verification procedures and retain records

- **Sophistication requirement** (Rule 506(b) non-accredited investors): Non-accredited
  investors must, either alone or with a purchaser representative, have sufficient
  financial and business sophistication to evaluate the investment. The PPM and
  subscription documents must assess and record this finding.

- **Subscription agreement completeness**: Does the subscription agreement include:
  - [ ] Accredited investor status representations and attestations
  - [ ] Investment intent representation (acquiring for own account, not for distribution)
  - [ ] Transfer restriction acknowledgment (restricted securities under Rule 144)
  - [ ] Lock-up period acknowledgment (for Reg S investors)
  - [ ] Legends requirement acknowledgment
  - [ ] Representation of receipt and review of the PPM
  - [ ] Anti-money laundering representations (for institutional investors and funds)
  - [ ] Suitability representations (risk tolerance, investment objectives consistent
        with the offering)

**Common issues:**

- Subscription agreement does not distinguish between Rule 506(b) and 506(c) investor
  qualification requirements
- Rule 506(c) offering with self-certification only (insufficient verification)
- No anti-money laundering (AML) representations — risk for institutional investors and
  international offerings
- Investor qualification procedures described in PPM but subscription agreement not included
  in the review (a gap that should be flagged)
- No assessment of sophistication for non-accredited investors in a Rule 506(b) offering

### 7. Business Description

The business description must fairly represent the issuer's current business, strategy,
competitive position, and prospects.

**Key elements to analyze:**

- **Accuracy**: Does the business description accurately reflect the current state of the
  business (not aspirational without disclosure of current stage)?
- **Stage-appropriate language**: Are forward-looking statements (projections, forecasts)
  clearly identified as forward-looking and accompanied by meaningful cautionary language?
- **Competition**: Is the competitive landscape fairly described? Omitting well-known
  major competitors may be a material omission.
- **Material contracts**: Are material customer, supplier, or license agreements
  disclosed? A significant customer concentration (e.g., one customer = 50% of revenue)
  must be disclosed.
- **Legal proceedings**: Are material pending or threatened legal proceedings disclosed?
  (Also links to bad actor screening — certain proceedings are disqualifying events.)
- **Intellectual property**: For technology/IP-dependent businesses, are IP ownership
  and protection status accurately described? Unresolved IP disputes must be disclosed.
- **Regulatory status**: For regulated industries (healthcare, financial services,
  cannabis, fintech), is regulatory status accurately described, including any pending
  enforcement actions or license/permit issues?

### 8. Capitalization

The capitalization section must provide a clear picture of ownership before and after the
offering.

**Key elements to analyze:**

- **Pre-offering cap table**: Number and type of shares outstanding by class
- **Post-offering cap table**: Assuming full subscription (and, if applicable, minimum
  subscription)
- **Fully diluted capitalization**: Including outstanding options, warrants, convertible
  instruments, promised but unissued shares, and the current offering on an as-converted
  basis
- **Dilution disclosure**: The percentage reduction in existing investor ownership if the
  full offering is completed
- **Option pool**: Size of existing employee option pool; whether option pool is being
  increased in connection with the offering (option pool shuffle effect)

**Common issues:**

- Cap table does not show fully diluted capitalization (options and warrants missing)
- No dilution analysis for existing investors
- Inconsistency between cap table and financial statements' equity section

---

## Deviation Severity Classification

### GREEN — Adequate

The disclosure meets applicable standards and market expectations. The section is present,
specific, and reasonably complete for this offering type and stage.

**Action**: Note for awareness. No revision needed unless minor improvements are suggested.

### YELLOW — Revise

The disclosure is present but inadequate, vague, or below market standard. The deficiency
creates some anti-fraud exposure and should be corrected before closing. Does not rise to
the level of a material omission requiring an offering halt.

**Examples:**

- Risk factor exists but is generic and could apply to any company
- Use of proceeds section present but lacks percentage allocations
- Management bio present but omits prior positions more than 5 years ago
- Financial statements within acceptable staleness but no interim update

**Action**: Provide specific revision language. Explain the specific risk created by the
deficiency. Recommend revision before closing.

### RED — Cure Before Closing

The disclosure gap or deficiency creates material anti-fraud exposure. A reasonable
investor would likely consider the missing or inadequate disclosure material to their
investment decision. The offering should not close without addressing the issue.

**Examples:**

- Risk factor section contains only boilerplate language with no issuer-specific risks
- Use of proceeds fails to disclose related-party payments from offering proceeds
- Key management bio omits a prior SEC enforcement action
- Financial statements more than 12 months old with no update in a fast-moving business
- No description of investors' limited transferability and lack of liquidity

**Action**: Explain the specific anti-fraud exposure (citing Rule 10b-5, §12(a)(2), or
§17(a) as applicable). Provide market-standard alternative disclosure. Recommend
escalation to securities counsel before closing.

### MATERIAL-OMISSION — Halt and Cure

The deficiency involves a material fact that has been entirely omitted from the PPM and
whose omission, under the _TSC Industries / Basic Inc._ standard, creates a "substantial
likelihood" that a reasonable investor would consider it important. Distribution of a PPM
with a material omission exposes the issuer to securities fraud liability.

**Examples:**

- Prior criminal conviction or SEC enforcement action of a principal — entirely omitted
- Bad actor disqualification event — not disclosed despite Rule 506(d)(1) applicability
- No offering exemption stated or claimed exemption is plainly inapplicable
- Material pending litigation (e.g., lawsuit seeking damages > 25% of offering amount)
  entirely absent from the PPM
- Going concern qualification in auditor's report — disclosed in financials but not in
  PPM body or cover page
- No use of proceeds section at all (for any offering > $500K)
- No risk factors section at all

**Action**: Halt distribution. Advise immediate consultation with securities counsel.
Identify the specific information that must be added. Flag the anti-fraud provisions
violated (Rule 10b-5, §17(a), or §12(a)(2) as applicable). Identify potential rescission
exposure if securities have already been sold.

---

## Redline / Revision Format

For each YELLOW, RED, or MATERIAL-OMISSION finding:

```
**Section**: [Section name and subsection]
**Issue**: [Specific problem]
**Current disclosure**: "[Exact quote or paraphrase from PPM]" OR "Absent"
**Proposed revision**: "[Specific suggested language or disclosure]"
**Rationale**: [1-2 sentences explaining why, suitable for discussion with counsel]
**Legal basis**: [Relevant provision — Rule 10b-5 / §12(a)(2) / §17(a) / Rule 506(d) / etc. — or [VERIFY]]
**Priority**: [Must-cure (MATERIAL-OMISSION/RED) / Should-cure (YELLOW)]
**Exposure if not cured**: [Brief description of the specific liability or enforcement risk]
```

---

## Disclosure Adequacy Prioritization Framework

When presenting findings, organize by priority:

### Tier 1 — Cure Before Any Sale (MATERIAL-OMISSION)

Issues whose uncured presence exposes every sale of securities to securities fraud
liability. Closing even one subscription without curing these items is not advisable.

- Material information entirely omitted (criminal history, disqualifying events, etc.)
- Exemption not claimed or plainly inapplicable
- Bad actor event not disclosed
- Going concern qualification not disclosed in PPM body

### Tier 2 — Cure Before Closing (RED)

Issues that create material anti-fraud exposure but where the securities have not yet
been sold. Cure before the first closing.

- Boilerplate-only risk factor section
- Use of proceeds inadequately specific, omitting related-party payments
- Financial statements materially stale or missing required audit
- Subscription terms lacking required accredited investor verification for Rule 506(c)

### Tier 3 — Revise at Next Opportunity (YELLOW)

Issues that reduce (but do not eliminate) the PPM's anti-fraud defense. Revise before
additional closings or at the next practical opportunity.

- Generic risk factors that should be made more specific
- Management bios that could be more complete
- Cap table that omits fully diluted calculation
- Minor inconsistencies between sections

---

## Disclosure Quality Score

After completing all 8 section analyses, compute the Disclosure Quality Score:

| Section                                     | Weight | Score (1-5) | Weighted Score |
| ------------------------------------------- | ------ | ----------- | -------------- |
| Risk Factors                                | 25%    |             |                |
| Use of Proceeds                             | 15%    |             |                |
| Management & Compensation                   | 20%    |             |                |
| Financial Statements                        | 15%    |             |                |
| Offering Structure / Securities             | 10%    |             |                |
| Subscription Terms / Investor Qualification | 10%    |             |                |
| Business Description                        | 3%     |             |                |
| Capitalization                              | 2%     |             |                |
| **Total**                                   | 100%   |             | **/5.0**       |

**Score interpretation:**

- **4.5–5.0**: Excellent disclosure — minimal liability exposure
- **3.5–4.4**: Good disclosure — minor improvements recommended
- **2.5–3.4**: Adequate disclosure — several YELLOW items require revision
- **1.5–2.4**: Inadequate disclosure — RED items require cure before closing
- **< 1.5**: Deficient disclosure — MATERIAL-OMISSION items; halt distribution

Score each section:

- **5**: Specific, complete, current, and consistent with all other sections
- **4**: Substantially complete with minor gaps only
- **3**: Present but contains significant vagueness or minor omissions
- **2**: Present but materially inadequate (boilerplate, outdated, or inconsistent)
- **1**: Absent or wholly deficient

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise any failures before
delivering.

| Gate           | Rule                                                                                                                                     | Fail Action                                              |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, rule, or established principle                                                               | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format (e.g., "17 C.F.R. § 230.506(b)")                                                  | Fix format                                               |
| **Currency**   | Every cited rule checked for amendments or repeal — Regulation D has been amended multiple times                                         | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the applicable exemption's framework. Do not apply Reg S requirements to a pure Rule 506(b) offering or vice versa | Remove or flag framework bleed                           |
| **Confidence** | Uncertainty about a legal position explicitly stated, not hidden                                                                         | Add confidence qualifier                                 |

### Self-Interrogation for MATERIAL-OMISSION and RED Items

For any item classified as MATERIAL-OMISSION or RED, apply this 3-pass review before
delivering:

**Pass 1 — Legal Chain Integrity**

- Does the materiality assessment follow logically from the _TSC Industries / Basic_
  standard? Would a reasonable investor actually consider this information important?
- Is there a plausible argument that the information is already disclosed elsewhere in the
  document (potentially curing the omission)?
- Would the SEC staff, in a comment letter or enforcement action, actually cite this as a
  deficiency?

**Pass 2 — Completeness**

- Have all related sections of the PPM been checked for this issue? (e.g., is a prior
  enforcement action disclosed in the legal proceedings section even if absent from the
  biography section?)
- Are there regulatory dimensions not yet considered? (e.g., FinCEN AML requirements for
  certain fund types, FINRA rules for broker-dealer-involved offerings)
- Have the subscription agreement and exhibits been considered, not just the PPM body?

**Pass 3 — Challenge**

- What is the strongest argument that the classified item is actually adequate (GREEN)?
- Under what circumstances might the existing disclosure be sufficient for a specific
  investor profile or offering type?
- Is the MATERIAL-OMISSION or RED classification proportionate, or is this actually a
  YELLOW item with reasonable mitigation?

If any pass reveals a weakness, revise the analysis before delivery. Mark the audit
trail: `self_interrogation: "PASS"` or `self_interrogation: "REVISED"`.

### Confidence Scoring

For each material section analysis, assign a confidence level:

| Level        | Range     | Meaning                                          | Action                                                |
| ------------ | --------- | ------------------------------------------------ | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, clear rule, no ambiguity            | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments but reasonable minds could differ | State with reasoning and contra-indicators            |
| **Possible** | 0.40–0.59 | Genuinely uncertain, competing interpretations   | Flag for securities counsel with both sides           |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                          | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

**Calibration note**: Given securities fraud exposure and the potential for investor
rescission claims, err toward flagging uncertainty rather than concealing it. A "Probable"
finding presented as "Definite" can cause an issuer to proceed with a materially deficient
PPM. When in doubt, escalate to counsel.

---

## Step 11: Quality Verification

Before delivering the analysis, run the quality checks:

1. Run the 5 Citation Quality Gates silently. Revise any failures.
2. For every MATERIAL-OMISSION and RED item, run the 3-pass Self-Interrogation. Revise
   if any pass reveals a weakness.
3. Assign a Confidence Score to each material section analysis.
4. Verify all 8 sections have been addressed (present or flagged as absent).
5. Compute the Disclosure Quality Score.
6. Verify internal consistency: do all findings in the Glass Box audit trail match the
   output body?
7. Generate the Glass Box Audit Trail and append to output.

---

## Anti-Patterns

What NOT to do when reviewing a Private Placement Memorandum:

1. **Clearing generic risk factors as adequate** — Risk factors that say "we may face
   competition" or "we may be unable to retain key personnel" without issuer-specific
   context provide minimal anti-fraud protection. Do not classify generic boilerplate risk
   factors as GREEN. The adequacy test is specificity and materiality, not mere presence.

2. **Ignoring the subscriber's perspective** — A PPM reviewed from the issuer's perspective
   only misses the investor's ability to bring rescission claims. Always consider whether
   a reasonable investor reading this document would feel adequately informed — because
   that is the standard courts apply.

3. **Treating "no financial statements" as YELLOW for large offerings** — The absence of
   financial statements in a material private offering is a MATERIAL-OMISSION, not a minor
   deficiency. Anti-fraud liability applies regardless of exemption type.

4. **Missing the management biography completeness test** — Biographies that list only
   current roles without prior positions, especially prior business failures, bankruptcies,
   or regulatory proceedings, are a leading cause of PPM-related enforcement. Check
   completeness against all prior roles for at least the past 5 years (longer for material
   prior positions).

5. **Skipping bad actor screening** — Rule 506(d) disqualification is an automatic issue —
   it does not require intent or knowledge. Overlooking a covered person's disqualifying
   event invalidates the entire Rule 506 exemption. Always flag when the PPM lacks a bad
   actor representation or when covered persons are identified without a clear negative
   history statement.

6. **Confusing Rule 506(b) and 506(c) investor qualification standards** — Self-certification
   of accredited investor status is sufficient for Rule 506(b). It is not sufficient for
   Rule 506(c), which requires "reasonable steps" to verify. Recommending self-certification
   alone for a 506(c) offering is incorrect and potentially exposes the issuer to a failed
   exemption.

7. **Ignoring integration risk** — Multiple offerings within a 12-month window from the
   same issuer can be integrated, potentially blowing the exemption and converting the
   offering into an unregistered public offering. Do not ignore recent or concurrent
   offerings disclosed in the PPM without assessing integration risk.

8. **Treating related-party payments as a footnote issue** — If offering proceeds are used
   to repay insider loans, compensate affiliates, or pay related-party vendors, this must
   be disclosed prominently in the PPM body — not only in financial statement footnotes.
   Failure to highlight related-party payments from proceeds is a common SEC enforcement
   focus.

9. **Assuming Reg S and Reg D are fully compatible without analysis** — Combined Reg D /
   Reg S offerings require meeting the requirements of both exemptions simultaneously,
   including directed selling efforts prohibitions, restricted period requirements, and
   the applicable Reg S category conditions. Do not assume compatibility — analyze each
   exemption's requirements independently and then assess the combined offering. [VERIFY]

10. **Overlooking going concern qualifications** — An auditor's going concern qualification
    buried in financial statement footnotes but not disclosed in the PPM's risk factors or
    executive summary is a paradigmatic material omission. Always check the audit opinion
    for going concern language and verify it is prominently disclosed if present.

11. **Conflating "no legal requirement" with "no disclosure needed"** — For Rule 506(b)
    and 506(c) offerings to all accredited investors, Regulation D does not mandate specific
    financial statements. But anti-fraud liability under Rule 10b-5, §12(a)(2), and §17(a)
    still requires disclosure of material financial information. The absence of a regulatory
    mandate is not a defense to securities fraud.

12. **Assessing only the PPM without the subscription agreement** — The PPM and the
    subscription agreement together constitute the offering documents. Investor qualification
    representations, transfer restriction acknowledgments, and investment intent representations
    are typically in the subscription agreement. A PPM review that ignores the subscription
    agreement is incomplete.

13. **Treating forward-looking statements as automatically protected** — The Private
    Securities Litigation Reform Act (PSLRA) safe harbor for forward-looking statements
    applies to certain claims by reporting companies. It does not apply to private placements
    or to companies that are not SEC reporting issuers. Do not suggest that projections in a
    PPM are "protected" by the PSLRA — for most private issuers, they are not. [VERIFY]

14. **Ignoring state Blue Sky compliance for Rule 504 offerings** — Rule 504 offerings are
    not "covered securities" under NSMIA. State Blue Sky registration or qualification may
    be required in each state where securities are sold. Do not treat Rule 504 offerings as
    having the same state preemption as Rule 506 offerings.

15. **Presenting findings without liability quantification** — "Material omissions" mean
    more in securities law than in contract law — they trigger rescission rights and civil
    liability under §12(a)(2). When flagging a MATERIAL-OMISSION, always specify the
    exposure: the investor may have the right to rescind their investment and recover the
    purchase price plus interest. This framing conveys appropriate urgency to the issuer.

16. **Skipping the internal consistency check** — A PPM that says one thing in the
    executive summary and another in the financial statements, or whose risk factors do not
    reflect risks disclosed in the business description, signals a document assembled from
    prior templates without careful review. Inconsistencies are a red flag for both
    inadequate disclosure and potential misrepresentation claims.

17. **Assuming crypto/digital asset offerings are outside this framework** — If the
    offering involves tokens or digital assets that may constitute securities (applying the
    _Howey_ test: investment of money in a common enterprise with expectation of profits
    from others' efforts), securities law analysis applies. Do not skip this analysis for
    technology offerings involving digital assets, governance tokens, or revenue-sharing
    tokens. [VERIFY current SEC guidance on digital assets]

18. **Delivering findings without prioritization** — A review that lists 25 issues without
    differentiating MATERIAL-OMISSION from YELLOW items forces the reader to decide
    priority. Always organize findings by severity tier (Tier 1/Tier 2/Tier 3) so the
    issuer knows immediately what must be cured before the first closing.

---

## Writing Standards

Before delivering the PPM review output, apply these standards:

1. **Active voice**: Write "This clause omits the material conflict" not "The conflict is
   omitted by this clause." Write "The issuer failed to disclose" not "Disclosure of X was
   not made."
2. **Quantify exposure**: State dollar amounts and percentages, not vague descriptions.
   "The omitted conflict involves a $500K consulting arrangement" is more useful than
   "a significant related-party arrangement is not disclosed."
3. **One finding per block**: Do not bundle multiple issues in a single finding. Separate
   each material issue into its own entry with its own severity classification.
4. **Source every benchmark claim**: State "[X]% of Reg D offerings in [year] included
   [feature], per SEC DERA data" rather than "market standard requires." [VERIFY all
   statistical claims]
5. **Confidence qualifiers**: State uncertainty explicitly. Never present a borderline
   materiality assessment as settled. "Probably material under _TSC Industries_, but
   reasonable minds could differ" is more accurate than "material."
6. **Revision language is proposed**: Preface suggested disclosure with "Suggested language
   (for counsel review):" — not as finalized legal text.
7. **No legal advice**: State findings as legal analysis frameworks for counsel consideration,
   not as definitive legal conclusions. "This omission appears inconsistent with Rule 10b-5's
   anti-fraud requirements — securities counsel should confirm" is appropriate.
8. **Plain-language summaries**: Each RED and MATERIAL-OMISSION item should include a
   plain-language summary of the issue and its consequence, followed by the technical
   legal analysis. Lead with what matters, then explain why.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** for legal authority verification.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for current text of Regulation D, Regulation S, and anti-fraud rules
- Verify the materiality standard cases (_TSC Industries_, _Basic Inc. v. Levinson_)
- Search for recent SEC enforcement actions involving PPM disclosure failures
- For state Blue Sky issues, verify current state notice filing requirements
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed using general securities law knowledge with appropriate qualifications
- Specifically flag for external verification: accredited investor definition categories
  (amended 2020), bad actor disqualification events (amended 2013), and any recent
  Regulation D amendments

---

## Localization Notes

### Combined Reg D / Reg S Offerings

For offerings combining Regulation D (US) and Regulation S (offshore):

**Reg S Category Analysis:**

| Category       | Issuer Type                                                                                          | Directed Selling Efforts | Restricted Period               | Resale Restrictions                                                                       |
| -------------- | ---------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------------- | ----------------------------------------------------------------------------------------- |
| **Category 1** | Foreign private issuer; domestic reporting with no SUSMI; offshore transactions in non-SUSMI markets | Prohibited               | None                            | None                                                                                      |
| **Category 2** | Reporting domestic issuer; equity of non-reporting domestic issuer                                   | Prohibited               | 40 days                         | Purchaser not US person; no directed selling; resale restrictions during 40 days          |
| **Category 3** | All others (non-reporting domestic issuer equity)                                                    | Prohibited               | 1 year (equity); 40 days (debt) | Purchaser not US person; prohibited from reselling to US persons during restricted period |

**Checklist for combined offerings:**

- [ ] All sales to non-US persons comply with Reg S offshore transaction requirements
- [ ] No directed selling efforts in the US for the Reg S tranche
- [ ] Reg S investors receive legends noting restricted period and resale restrictions
- [ ] The Reg D and Reg S tranches are clearly delineated in the subscription process
- [ ] Integration between the Reg D and Reg S tranches does not destroy either exemption

### International Issuer PPMs (Offshore Funds)

For offshore fund PPMs (Cayman Islands, BVI, Luxembourg feeder funds):

- Reg S analysis for US investor restriction vs. eligibility
- IA Act investment adviser exemption analysis (§203(l) venture capital fund, §203(m)
  private fund adviser with AUM < $150M)
- Check whether any US persons are investing — if so, full Reg D analysis required for
  US investor tranche
- [JURISDICTION-SPECIFIC] Cayman Islands: Mutual Funds Act (as amended), Securities
  Investment Business Act for adviser registration [VERIFY]
- [JURISDICTION-SPECIFIC] BVI: Financial Services Commission requirements for private
  fund PPMs [VERIFY]
- [JURISDICTION-SPECIFIC] Luxembourg: CSSF approval for AIF/UCITS vs. private placement
  exemption under AIFMD [VERIFY]

---

## Output Format Template

````markdown
# Private Placement Memorandum Review

**Document**: [PPM title, issuer name, date]
**Offering**: [Type of securities, amount sought]
**Exemption Claimed**: [Rule 506(b) / 506(c) / 504 / Reg S / combined]
**Review Perspective**: [Issuer / Investor / Issuer's counsel / Investor's counsel]
**Governing Law**: [State of organization; federal securities law]
**Date of Review**: [date]

---

## Disclosure Quality Score: [X.X / 5.0]

**Overall Assessment**: [Excellent / Good / Adequate / Inadequate / Deficient]
**Confidence**: [High / Probable] — [1-2 sentence rationale]

| Section                               | Score | Key Issues |
| ------------------------------------- | ----- | ---------- |
| Risk Factors (25%)                    | [1-5] | [brief]    |
| Use of Proceeds (15%)                 | [1-5] | [brief]    |
| Management & Compensation (20%)       | [1-5] | [brief]    |
| Financial Statements (15%)            | [1-5] | [brief]    |
| Offering Structure / Securities (10%) | [1-5] | [brief]    |
| Subscription Terms (10%)              | [1-5] | [brief]    |
| Business Description (3%)             | [1-5] | [brief]    |
| Capitalization (2%)                   | [1-5] | [brief]    |

---

## Tier 1 — Cure Before Any Sale (MATERIAL-OMISSION)

[If none: "No Tier 1 issues identified."]

### [1.1] [Issue Name] | MATERIAL-OMISSION | Confidence: [level]

**Plain-language summary**: [1-2 sentences in plain English]
**Section affected**: [Section name]
**Issue**: [Specific problem]
**Current disclosure**: "[Exact quote or 'Absent']"
**Suggested language (for counsel review)**:

> [Specific proposed disclosure]
> **Legal basis**: [Rule 10b-5 / §12(a)(2) / §17(a) / Rule 506(d) — [VERIFY if uncertain]]
> **Exposure if uncured**: [Rescission exposure, SEC enforcement risk, etc.]

---

## Tier 2 — Cure Before Closing (RED)

[RED items in priority order]

### [2.1] [Issue Name] | RED | Confidence: [level]

**Section**: [Section name]
**Issue**: [Specific problem]
**Current disclosure**: "[Quote or paraphrase]"
**Proposed revision**:

> [Suggested language]
> **Rationale**: [1-2 sentences for discussion with counsel]
> **Legal basis**: [Applicable rule or principle — [VERIFY if uncertain]]
> **Priority**: Must-cure before closing

---

## Tier 3 — Revise at Next Opportunity (YELLOW)

[YELLOW items]

### [3.1] [Issue Name] | YELLOW | Confidence: [level]

**Section**: [Section name]
**Issue**: [Specific problem]
**Current disclosure**: "[Quote or paraphrase]"
**Proposed revision**:

> [Suggested revision language]
> **Priority**: Should-revise before additional closings

---

## Securities Law Compliance Assessment

### Exemption Compliance

| Requirement           | Rule 506(b) / 506(c) / 504                        | Assessment                  |
| --------------------- | ------------------------------------------------- | --------------------------- |
| Offering size limit   | [N/A / $10M]                                      | [Compliant / Flag]          |
| Investor eligibility  | [All accredited / Accredited + 35 non-accredited] | [Compliant / Flag]          |
| General solicitation  | [Prohibited / Permitted]                          | [Compliant / Flag]          |
| Investor verification | [Self-cert / Enhanced verification]               | [Compliant / Flag]          |
| Bad actor check       | Required                                          | [Addressed / Not addressed] |
| Form D reminder       | Required                                          | [Present / Absent]          |
| Financial statements  | [Not required / Rule 502(b)]                      | [Adequate / Deficient]      |

### Reg S Assessment (if applicable)

| Requirement                  | Category [1/2/3]         | Assessment                  |
| ---------------------------- | ------------------------ | --------------------------- |
| Offshore transaction         | Required                 | [Addressed / Not addressed] |
| No directed selling efforts  | Required                 | [Addressed / Not addressed] |
| Restricted period disclosure | [N/A / 40 days / 1 year] | [Present / Absent]          |
| Resale restriction legends   | Required                 | [Present / Absent]          |

---

## Green Items (for Awareness)

[GREEN items noted for completeness — no action required]

---

## Jurisdiction-Specific Actions

[List of state Blue Sky notice filings required, international law matters requiring
local counsel verification, etc.]

---

## Recommended Next Steps

1. [Numbered action items with suggested owner and timing — Immediate / Before first
   closing / Before additional closings / Ongoing]

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill: "legalcode-private-placement-memo-review"
  ppm_document: "[PPM title, issuer, date]"
  offering_type: "[Operating company / Fund / Real estate / Other]"
  exemption_reviewed: "[Rule 506(b) / 506(c) / 504 / Reg S / Combined]"
  review_perspective: "[Issuer / Investor / Counsel]"
  governing_law: "[State of organization] + Federal securities law"
  sections_reviewed: "[list of sections present and reviewed]"
  sections_absent: "[list of sections entirely absent from PPM]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-ppm-review-authority.md or 'Not created']"
  statutes_consulted:
    - "Securities Act of 1933 §§4(a)(2), 5, 12, 17 — [VERIFIED / UNVERIFIED]"
    - "17 C.F.R. §§230.501-230.506 (Reg D) — [VERIFIED / UNVERIFIED]"
    - "17 C.F.R. §§230.901-230.905 (Reg S) — [VERIFIED / UNVERIFIED]"
    - "17 C.F.R. §240.10b-5 (Rule 10b-5) — [VERIFIED / UNVERIFIED]"
  case_law_consulted:
    - "TSC Industries v. Northway, 426 U.S. 438 (1976) — [VERIFIED / UNVERIFIED]"
    - "Basic Inc. v. Levinson, 485 U.S. 224 (1988) — [VERIFIED / UNVERIFIED]"
    - "SEC v. Ralston Purina Co., 346 U.S. 119 (1953) — [VERIFIED / UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  disclosure_quality_score: "[X.X]/5.0"
  findings_count:
    material_omissions: "[number]"
    red: "[number]"
    yellow: "[number]"
    green: "[number]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no Tier 1/RED items)"
  bad_actor_screening: "Addressed in PPM / Not addressed / Flagged as deficiency"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "This review does not constitute legal advice or a legal opinion on exemption availability."
    - "Subscription agreement and exhibits reviewed: [Yes / No — specify what was missing]"
    - "State Blue Sky compliance verified: [Yes / Partial / No]"
    - "[Other scope limitations]"
  reviewer: "AI-assisted — requires qualified securities counsel review before reliance"
```
````

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis based on:

- Securities Act of 1933 §§ 4(a)(2), 5, 12(a)(2), 17(a); Regulation D (17 C.F.R. §§
  230.500–230.508); Regulation S (17 C.F.R. §§ 230.901–930.905); Rule 10b-5 (17 C.F.R.
  § 240.10b-5)
- Materiality standards: _TSC Industries, Inc. v. Northway, Inc._, 426 U.S. 438 (1976);
  _Basic Inc. v. Levinson_, 485 U.S. 224 (1988)
- Section 4(a)(2) doctrine: _SEC v. Ralston Purina Co._, 346 U.S. 119 (1953)
- 2020 SEC amendments to accredited investor definition and qualified purchaser definition
- SEC Rule 506(d) bad actor disqualification rule (effective September 23, 2013)
- NSMIA preemption framework, 15 U.S.C. § 77r
- SEC Division of Enforcement reports on private offering fraud (2021–2025)
- Repository best practices from legalcode-contract-review, legalcode-term-sheet-analysis,
  and legalcode-shareholders-agreement-review quality frameworks
- All statutory and case law references should be verified against authoritative sources
  before reliance — cite as [VERIFY] in outputs where legalcode-mcp is not connected
