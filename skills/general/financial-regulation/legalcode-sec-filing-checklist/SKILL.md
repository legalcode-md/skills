---
name: legalcode-sec-filing-checklist
description: Generates comprehensive SEC filing compliance checklists for US public companies.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Generates comprehensive SEC filing compliance checklists for US public companies. Covers periodic reports (Form 10-K, Form 10-Q), current reports (Form 8-K), proxy statements (DEF 14A), and Section 16 insider ownership reports (Forms 3, 4, 5). Assesses filing deadlines by filer category (Large Accelerated, Accelerated, Non-Accelerated, Smaller Reporting Company, Emerging Growth Company, Foreign Private Issuer), required disclosure items under Regulation S-K and Regulation S-X, SOX certifications (Sections 302 and 906), Inline XBRL tagging requirements, EDGAR filing mechanics, non-GAAP financial measure compliance, cybersecurity disclosure obligations (SEC Final Rule Release No. 33-11216), Pay vs. Performance requirements (Item 402(v)), executive compensation clawback policies, and common SEC comment letter deficiencies. Use this skill when a company needs to prepare, review, or remediate an SEC filing; when assessing IPO-readiness; when evaluating disclosure controls and procedures; when preparing CEO/CFO SOX certifications; or when responding to an SEC comment letter. Triggers on: "10-K checklist", "10-Q review", "8-K compliance", "proxy statement", "SEC filing", "EDGAR submission", "XBRL tagging", "SOX 302 certification", "disclosure controls", "material event reporting", "Form 4", "Section 16", "DEF 14A", "executive compensation disclosure", "SEC comment letter", "periodic report", "annual report compliance".


# SEC Filing Compliance Checklist

> ⚠️ **Disclaimer**: This skill provides a framework for AI-assisted SEC filing review and
> compliance assessment. It does not constitute legal advice, accounting advice, or audit
> services, and does not constitute a compliance certification or legal opinion. All outputs
> must be reviewed by qualified securities counsel, a certified public accountant, and other
> relevant professionals licensed and practicing in the United States before reliance. SEC
> rules change; verify the currency of every provision before relying on it. Nothing in this
> skill constitutes an offer or solicitation to purchase or sell any security. This skill
> does not substitute for a registered public accounting firm's audit or PCAOB-compliant
> attestation procedures. AI-assisted analysis carries inherent risk of error; never use
> output to support a CEO/CFO Section 906 certification without independent counsel review.

---

## Purpose and Scope

This skill enables systematic, comprehensive compliance assessment of SEC filings by US
public companies subject to the Securities Exchange Act of 1934 ("Exchange Act") and/or
the Securities Act of 1933 ("Securities Act"). It generates checklists, gap analyses, and
remediation plans covering:

**In scope:**

- Periodic reports: Form 10-K (annual), Form 10-Q (quarterly)
- Current reports: Form 8-K (material events)
- Proxy and information statements: DEF 14A, PRE 14A, Schedule 14C
- Section 16 insider ownership reports: Forms 3, 4, and 5
- Registration statements: Forms S-1, S-3, S-11 (structural review only)
- EDGAR submission mechanics and Inline XBRL tagging
- SOX Sections 302 and 906 certifications
- Non-GAAP financial measure compliance (Regulation G; S-K Item 10(e))
- Material event assessment (8-K triggering event analysis)
- SEC comment letter response framework

**Not in scope:**

- PCAOB audit procedures or attestation on ICFR (SOX § 404(b))
- Actual preparation of financial statements (refer to accounting professionals)
- Securities offering exemption selection (use `legalcode-securities-regulation-compliance`)
- SOX internal controls deep assessment (use `legalcode-sox-compliance-assessment`)
- Non-US reporting regimes (IFRS, UK DTR, EU Transparency Directive — use jurisdiction-specific skills)

**Related skills:**

- `legalcode-sox-compliance-assessment` — deep COSO/ICFR/ITGC assessment
- `legalcode-securities-regulation-compliance` — offering exemptions, Reg D, Reg A+
- `legalcode-us-fcpa-compliance` — FCPA compliance for reporting company disclosures
- `legalcode-non-compete-analysis` — SEC disclosure of restrictive covenant obligations

---

## Jurisdiction and Governing Law

This skill is **US federal law specific**. All analysis is governed by:

| Authority                                                                   | Coverage                                        |
| --------------------------------------------------------------------------- | ----------------------------------------------- |
| Securities Exchange Act of 1934 (15 U.S.C. § 78a et seq.)                   | Periodic reporting, Section 16, proxy rules     |
| Securities Act of 1933 (15 U.S.C. § 77a et seq.)                            | Registration statements, offering disclosures   |
| Sarbanes-Oxley Act of 2002 (Pub. L. 107-204)                                | Certifications, ICFR, audit committee           |
| Dodd-Frank Wall Street Reform and Consumer Protection Act (Pub. L. 111-203) | Whistleblower, clawback, say-on-pay, pay ratio  |
| Regulation S-K (17 CFR Part 229)                                            | Non-financial disclosure requirements           |
| Regulation S-X (17 CFR Part 210)                                            | Financial statement requirements                |
| Regulation S-T (17 CFR Part 232)                                            | Electronic filing (EDGAR) requirements          |
| Exchange Act Rules 12b-2, 13a-1, 13a-11, 13a-13, 13a-14, 13a-15             | Definitions, filing obligations, certifications |
| EDGAR Filer Manual (current version)                                        | Submission mechanics, XBRL tagging              |

**Filer categories determine filing deadlines, accommodation of reduced disclosure, and
exemptions from certain requirements.** The applicability gate in Step 4 must be completed
before any form-specific analysis.

**No state securities law (Blue Sky) analysis is included** in this skill. Blue Sky
compliance for offerings should be assessed using `legalcode-securities-regulation-compliance`.

---

## Interactive Clarification

This skill uses **⟁ CLARIFY** at key decision points. The rule: ask only when the answer
changes the direction of the analysis. When context is already provided, skip the question
and state the assumption.

Each CLARIFY point includes:

- **Options** to choose from (numbered for quick response)
- **Why this matters** — the specific downstream impact on the analysis
- **Batch default** — the assumption used in automated/non-interactive runs

---

## Workflow

### Step 1: Receive and Read the Filing

Accept input in any of these forms:

- Full text of a draft or filed document (pasted or via file path)
- Filing identification (company name, form type, period)
- Scope description for a prospective filing (pre-filing checklist)
- Partial filing (specific Items or sections for targeted review)

**Read the complete filing before flagging any issues.** Disclosure items interact:

- A risk factor in Item 1A may contextualize (or conflict with) an MD&A disclosure in Item 7
- A related-party transaction in Item 13 may trigger ICFR disclosure implications in Item 9A
- An 8-K Item 2.02 earnings disclosure may affect proxy say-on-pay disclosure timing

**If the document is very long (> 100 pages):** Confirm with the user which Items to
prioritize for deep analysis and which to assess at checklist depth only.

---

### Step 2: Gather Context

**⟁ CLARIFY** — Before analysis, gather the following (skip questions already answered):

**2a. Assessment mode:**

1. **Full review** — Complete assessment of all applicable form items
2. **Pre-filing checklist** — Forward-looking checklist before a filing is drafted
3. **Comment letter response** — Assess specific SEC staff comments and draft responses
4. **IPO readiness** — Assess readiness for first S-1 filing and Exchange Act reporting
5. **Targeted item review** — Focus on one or more specific Items or disclosure areas
6. **Amendment assessment** — Determine whether a filed document requires amendment

_Why this matters_: Mode shapes step sequencing; Comment Letter mode activates Step 9;
IPO Readiness triggers a different filer category path.

_Batch default_: Full review.

**2b. Which form(s) are in scope?** (select all that apply):

1. Form 10-K (annual report)
2. Form 10-Q (quarterly report)
3. Form 8-K (current report / material event)
4. DEF 14A (proxy statement)
5. Forms 3 / 4 / 5 (Section 16 insider ownership)
6. Registration statement (S-1, S-3, S-11)
7. Multiple / all of the above

_Batch default_: Form 10-K (most comprehensive — covers the widest range of disclosure
obligations; other forms are subsets).

**2c. Company characteristics:**

- Fiscal year end date (or anticipated period)
- Approximate public float as of most recent June 30 (or IPO pricing)
- Annual revenues (most recent full fiscal year)
- Exchange listing (NYSE, Nasdaq, other) — relevant for listing standard compliance
- Any prior SEC comment letters received (flag unresolved comments)
- Foreign private issuer status? (triggers Form 20-F analysis instead of 10-K)

_Why this matters_: Determines filer category, which in turn determines filing deadlines,
Section 404(b) applicability, EGC accommodation availability, and SRC reduced disclosure
elections.

_Batch default_: Large Accelerated Filer, fiscal year end December 31, NYSE listed,
non-FPI.

**2d. Auditor and ICFR context:**

1. Big Four auditor (PCAOB-registered, full § 404(b) attestation expected)
2. Non-Big Four registered auditor (§ 404(b) required if AF or LAF)
3. No auditor attestation (NAF, SRC, or EGC exempt from § 404(b))
4. First-year reporting (no prior ICFR opinion)

_Batch default_: Big Four auditor, § 404(b) attestation required.

---

### Step 3: Search for Governing Authority (legalcode-mcp)

**With legalcode-mcp connected:**
Search for current versions of:

- The relevant form's SEC instructions (10-K, 10-Q, 8-K, DEF 14A as applicable)
- Any SEC staff guidance, C&DI (Compliance and Disclosure Interpretations), or
  No-Action letters relevant to the company's industry or disclosure questions
- Recent SEC enforcement actions in the same industry that signal staff priorities
- Current EDGAR Filer Manual version and any recent XBRL taxonomy updates

Save results to `/tmp/sec-filing-authority-[date].md`.

**Without legalcode-mcp:**
Proceed using web research and repository knowledge. Mark all statutory and rule
references with [VERIFY] for counsel confirmation. Note in the Glass Box:
`legalcode_mcp: "Not connected"`.

---

### Step 4: Filer Category Determination (Mandatory Gate)

**This step is a mandatory gate.** Filer category determines filing deadlines, § 404(b)
applicability, EGC accommodations, and SRC reduced disclosure elections. Complete this
step before any form-specific analysis.

**⟁ CLARIFY** — Confirm the filer category (or determine it from the financial data provided):

| Category                            | Definition                                                                                                                                                          | Key Thresholds                                                                               |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Large Accelerated Filer (LAF)**   | Exchange Act reporting ≥ 12 months; public float ≥ $700M as of June 30                                                                                              | § 404(b) required; tightest deadlines                                                        |
| **Accelerated Filer (AF)**          | Reporting ≥ 12 months; public float $75M–$699.9M as of June 30; annual revenues < $100M do NOT grant SRC status if float ≥ $75M                                     | § 404(b) required                                                                            |
| **Non-Accelerated Filer (NAF)**     | Does not meet LAF or AF thresholds                                                                                                                                  | § 404(b) exempt                                                                              |
| **Smaller Reporting Company (SRC)** | Public float < $250M, OR float < $700M + revenues < $100M                                                                                                           | Reduced S-K disclosure elections available                                                   |
| **Emerging Growth Company (EGC)**   | First IPO on or after Dec 8, 2011; gross revenues < $1.235B [VERIFY current threshold]; < 5 years from IPO or first sale; < $1B non-convertible debt; < $700M float | Extended transition for new accounting standards; § 404(b) exempt; reduced proxy disclosures |
| **Foreign Private Issuer (FPI)**    | More than 50% of voting securities held by non-US residents AND business/assets primarily outside US or majority of directors/officers are non-US citizens          | Files Form 20-F not 10-K; 4-month deadline; IFRS permitted                                   |

**Reclassification risk check:** Verify whether the company crossed a threshold during the
current fiscal year that would change its filer category for the upcoming filing. The LAF
↔ AF transition requires two consecutive years below the applicable float threshold (the
"sticky" rule). Flag reclassification risk prominently if thresholds are near.

**If the entity is not subject to Exchange Act reporting obligations (not a Section 12
registrant or not subject to Section 15(d) reporting), STOP.** This skill does not apply.
Explain why and suggest `legalcode-securities-regulation-compliance` for offering-only
contexts.

---

### Step 5: Filing Deadline Compliance Assessment

Assess whether all required filings are current, upcoming, or overdue. Apply the deadline
matrix below keyed to the confirmed filer category.

#### 5a. Periodic Report Deadlines

| Form           | LAF                                | AF                         | NAF / SRC                  | Extension Available                                                       |
| -------------- | ---------------------------------- | -------------------------- | -------------------------- | ------------------------------------------------------------------------- |
| **10-K**       | 60 calendar days after FYE         | 75 calendar days after FYE | 90 calendar days after FYE | NT 10-K (Form 12b-25): 15-calendar-day extension if filed before deadline |
| **10-Q**       | 40 calendar days after quarter end | 40 calendar days           | 45 calendar days           | NT 10-Q: 5-calendar-day extension                                         |
| **20-F** (FPI) | 4 months after FYE                 | —                          | —                          | No extension available                                                    |

_Note: Deadlines fall on the next business day if the standard deadline falls on a Saturday,
Sunday, or SEC holiday._

**NT form procedure:** NT 10-K / NT 10-Q must be filed before the original deadline. They
require disclosure of why timely filing is impracticable and a good-faith estimate of when
the filing will be completed. A late filing without a timely NT constitutes a delinquency.
Delinquency triggers loss of Form S-3 eligibility (requires timely filer status for the
preceding 12 months).

#### 5b. Current Report Deadlines (Form 8-K)

**Standard rule:** 4 business days after the triggering event or the day on which the
company becomes aware the triggering event occurred, whichever is later.

**Exceptions and nuances:**

- **Item 2.02 (Results of Operations):** If filed within 4 business days of quarter/year
  end to accompany earnings release, the Item 2.02 exhibit (press release) need not contain
  all Reg G non-GAAP reconciliations if the company simultaneously posts them on its website
- **Item 1.05 (Cybersecurity Incident):** 4-business-day deadline runs from the date the
  company determines the incident is material — not from the date of discovery. Effective
  December 18, 2023 (LAF/AF); June 15, 2024 (smaller filers) [VERIFY]
- **Item 8.01 (Other Events):** Voluntary; no deadline
- **Item 9.01 (Financial Statements and Exhibits):** Pro forma financials for significant
  acquisitions may be filed within 71 calendar days of initial 8-K filing (Form 8-K/A)

#### 5c. Section 16 Insider Report Deadlines

| Form       | Who Files                                                                    | Deadline                                      | Purpose                                                        |
| ---------- | ---------------------------------------------------------------------------- | --------------------------------------------- | -------------------------------------------------------------- |
| **Form 3** | Officers, directors, >10% beneficial owners upon becoming a reporting person | Within 10 days of becoming a reporting person | Initial statement of beneficial ownership                      |
| **Form 4** | All Section 16 persons for changes in beneficial ownership                   | Within 2 business days of transaction         | Changes in beneficial ownership                                |
| **Form 5** | Section 16 persons for transactions not reported on Form 4                   | Within 45 days after fiscal year end          | Annual omnibus report (may omit if no reportable transactions) |

**Section 16 "officer" definition [VERIFY — Rule 16a-1(f)]:** Broader than C-suite; includes
any president, principal financial officer, principal accounting officer, any VP heading a
principal business unit/division/function, any other officer performing a policy-making
function, or any other person who performs similar policy-making functions. Confirm the
company's roster of Section 16 officers is current.

#### 5d. Proxy Statement Deadlines

| Event                                | Preliminary (PRE 14A)                                                        | Definitive (DEF 14A)                                                                     |
| ------------------------------------ | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Annual meeting proxy                 | At least 10 calendar days before DEF 14A filing (if SEC review is triggered) | At least 40 calendar days before meeting date (NYSE/Nasdaq listing requirement [VERIFY]) |
| Information statement (Schedule 14C) | Filed same day as DEF 14C; SEC review period 10 days                         | Distributed at least 20 calendar days before effective date of action                    |

---

### Step 6: Form-Specific Item-Level Analysis

Analyze each applicable form against its required disclosure items. Apply the severity
classification defined in Section 8 to each finding.

---

#### Module A: Form 10-K

Review against the 15 primary Items of Form 10-K. For each Item, identify:
(a) whether disclosure is present, (b) whether it is adequate under SEC rules and
anti-fraud standards, (c) whether it is tailored to the company's specific facts (not
boilerplate), and (d) whether it would likely draw an SEC comment.

**Item 1 — Business (Regulation S-K Item 101):**

- General development of business (three-year history)
- Narrative description of business: principal products/services, distribution methods,
  competitive conditions, number of employees, seasonality, raw material availability
- Human capital disclosures [VERIFY S-K Item 101(c)(2)(ii)]: material aspects of human
  capital resources including measures management uses to oversee human capital
- **Common comment issue:** Inadequate description of competitive position; generic
  human capital disclosures that are not company-specific

**Item 1A — Risk Factors (Regulation S-K Item 105):**

- Each risk factor must be specific and tailored to the company — not generic industry risks
- Risk factor captions must accurately reflect the risk described in the body text
- The risk factor section must include a summary of not more than two pages if risk factors
  span more than 15 pages [VERIFY current rule text]
- **Common comment issue (most frequently cited):** Generic, industry-wide risk factors
  that could apply to any issuer; risk factors that describe risks already materialized
  without disclosing the current impact; risk factor captions that are vague or inconsistent
  with the body

**Item 2 — Properties:**

- Material physical properties, including approximate square footage, ownership vs. lease,
  and properties material to business operations
- **Threshold:** Significant revenue contribution or operational dependency

**Item 3 — Legal Proceedings:**

- Pending legal proceedings material to the company or that involve a claim exceeding
  10% of current assets [VERIFY S-K Item 103 threshold]
- Environmental proceedings if a governmental authority is a party and potential sanctions
  exceed $1 million [VERIFY current Instruction 5.C threshold, which may have increased]
- Exclusion: Ordinary routine litigation incidental to the business

**Item 4 — Mine Safety Disclosures:**

- Only required if the company operates mines subject to the Federal Mine Safety and Health
  Act; otherwise, check the box "Not applicable"

**Item 5 — Market for Registrant's Common Equity:**

- Information about holders, dividends, and stock repurchases (Rule 10b-18 buyback table)
- Performance graph comparing 5-year cumulative return vs. index and peer group
  (LAF required; SRC optional)

**Item 6 — [Reserved]:**

- Effective for fiscal years beginning after December 15, 2021; Selected Financial Data
  has been eliminated. Verify the company is not including stale Selected Financial Data
  disclosure from a prior form version

**Item 7 — Management's Discussion and Analysis (S-K Item 303):**

This is the highest-risk Item for SEC comment letters. Assess all of the following:

- **Known trends and uncertainties:** Does the MD&A disclose known trends, demands,
  commitments, events, or uncertainties that are reasonably likely to have a material
  effect on results? This is the most-cited comment issue. Generic statements that the
  company "may be affected by macroeconomic conditions" are inadequate.
- **Quantification requirement:** SEC staff expects quantification of material factors
  driving period-over-period changes — not merely identification. "Revenue increased due
  to volume" is inadequate; the disclosure must quantify the volume effect vs. price effect.
- **Liquidity analysis:** Cash and cash equivalents, material cash commitments, short-term
  borrowing capacity, capital resources, and off-balance-sheet arrangements
- **Critical accounting estimates:** For each critical estimate, disclose the nature of
  the estimate, the assumptions underlying it, the sensitivity to changes in assumptions,
  and the effect of a reasonably likely change in the estimate on reported results
- **Common comment issues:** Failure to discuss the causes driving the numbers (not merely
  the numbers themselves); failure to quantify; failure to address trends that appear
  self-evident from the financial statements; boilerplate on liquidity

**Item 7A — Quantitative and Qualitative Disclosures About Market Risk:**

- Required for LAF and AF; SRC may omit
- Interest rate risk, foreign exchange risk, commodity price risk
- Tabular, sensitivity analysis, or VaR methodology disclosure

**Item 8 — Financial Statements and Supplementary Data:**

- Audited balance sheets (2 years), income statements (3 years), cash flow (3 years)
- Notes to financial statements; auditor's report (PCAOB AS 3101)
- Supplementary quarterly financial data (if applicable; SRC may omit)
- **PCAOB AS 2201 reference:** If § 404(b) applies, auditor's report on ICFR appears here
  or in a separate section immediately following the financial statements

**Item 9 — Changes in and Disagreements with Accountants:**

- Required if auditor change occurred; cross-reference to Form 8-K Item 4.01

**Item 9A — Controls and Procedures:**
This Item requires disclosure of both Disclosure Controls and Procedures (DC&P) and
Internal Control Over Financial Reporting (ICFR). These are distinct concepts:

| Control Framework         | Scope                                                                       | CEO/CFO Evaluation Required                                                  |
| ------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **DC&P** (Rule 13a-15(e)) | All information required to be disclosed in SEC reports — broader than ICFR | Yes, quarterly for 10-Q; annually for 10-K                                   |
| **ICFR** (Rule 13a-15(f)) | Financial reporting controls (COSO 2013 framework)                          | Yes, annually in 10-K (management's report); quarterly assessment of changes |

**Management's Report on ICFR (annual 10-K):**

- Statement of management's responsibility for ICFR
- Identification of the framework used (COSO 2013 for US filers)
- Management's assessment of effectiveness as of fiscal year end
- If a material weakness exists: disclosure of the nature, its effect on the financial
  statements, and remediation status
- If § 404(b) applies: auditor's attestation incorporated by reference

**Automatic Material Weakness Triggers:**
Any of the following constitute a material weakness per se — disclose immediately:

- Fraud by senior management (regardless of materiality)
- Prior-period restatement for more than an immaterial error
- Misstatement detected by the auditor (not management) that is material or potentially material
- Ineffective audit committee (independence failure under Exchange Act Rule 10A-3)
- Significant deficiency or material weakness identified by external auditor

**Item 9B — Other Information:**
Any information that would be required on a Form 8-K but was not separately filed

**Item 10 — Directors, Executive Officers, and Corporate Governance (Regulation S-K Items 401, 405, 406, 407):**

- Director biographies (five-year history, relevant qualifications, other directorships)
- Executive officer list (may be omitted and included in proxy)
- Section 16(a) beneficial ownership reporting compliance (delinquencies must be disclosed;
  check whether all Form 3/4/5 filings were timely for the fiscal year)
- Code of Ethics (must be disclosed and posted on website or filed as exhibit; exceptions
  must be disclosed by Form 8-K Item 5.05 within 4 business days)
- Audit committee financial expert disclosure (Rule 10A-3)

**Item 11 — Executive Compensation (Regulation S-K Item 402):**

- Compensation Discussion and Analysis (CD&A) — required for LAF/AF; SRC may use simplified
  disclosure
- Summary Compensation Table (SCT) covering three fiscal years (two for SRC)
- Grants of Plan-Based Awards table
- Outstanding Equity Awards at Fiscal Year-End table
- Option Exercises and Stock Vested table
- Pension Benefits table (if applicable)
- Nonqualified Deferred Compensation table (if applicable)
- Potential payments upon termination or change in control
- Pay ratio disclosure (CEO to median employee — required for all except EGCs)
- **Pay vs. Performance (Item 402(v)):** Required for proxy statements filed after
  January 27, 2023 (not applicable to EGCs, FPIs, or SRCs in their first year [VERIFY]).
  Must include a table showing TSR, net income, Company Selected Measure, and
  "Compensation Actually Paid" (CAP) — a complex calculation requiring equity award
  adjustments differing from the Summary Compensation Table values.
  **Common comment issue:** Errors in CAP calculation (equity award grant-date vs.
  year-end fair value; inclusion of unvested awards incorrectly).

**Item 12 — Security Ownership of Certain Beneficial Owners and Management:**

- Beneficial ownership table (> 5% holders, officers, directors)
- Equity compensation plan information table

**Item 13 — Certain Relationships and Related Transactions, and Director Independence:**

- Related-party transactions exceeding $120,000 in the fiscal year involving any director,
  officer, or > 5% shareholder [VERIFY current threshold under S-K Item 404(a)]
- Director independence determinations under applicable exchange listing standards
- **Common comment issue:** Failure to disclose transactions because they are "ordinary
  course" without applying the S-K threshold test

**Item 14 — Principal Accountant Fees and Services:**

- Audit fees, audit-related fees, tax fees, all other fees (two-year comparison)
- Audit committee pre-approval policy disclosure
- Percentage of services approved pursuant to de minimis exception

**Item 15 — Exhibits and Financial Statement Schedules:**

- Exhibit index with all required exhibits per S-K Item 601
- Key required exhibits:
  - 3.1 / 3.2: Articles of Incorporation, Bylaws
  - 10.\*: Material contracts not made in ordinary course of business
  - 14: Code of Ethics (if newly adopted or amended)
  - 19: Insider Trading Policy [VERIFY — new requirement effective 2024 [VERIFY]]
  - 21: Subsidiaries
  - 23: Auditor consent
  - 31.1 / 31.2: SOX § 302 certifications (CEO and CFO)
  - 32.1 / 32.2: SOX § 906 certifications (CEO and CFO)
  - 97: Clawback policy [VERIFY — new requirement under Rule 10D-1]
  - 101: Inline XBRL interactive data files

---

#### Module B: Form 10-Q

For each quarterly 10-Q, review:

- **Part I, Item 1:** Interim financial statements (condensed; unaudited)
  - Balance sheet (current and prior year-end)
  - Income statement (current quarter and year-to-date; prior period comparative)
  - Cash flow statement (year-to-date; prior period comparative)
  - Notes to financial statements (condensed; focus on material changes since 10-K)
  - Review report by independent auditor (required for LAF and AF; optional for NAF/SRC)
- **Part I, Item 2:** MD&A — same analytical standards as 10-K Item 7, but focused on
  changes since the most recent annual report; material period-over-period changes must be
  quantified
- **Part I, Item 3:** Quantitative and Qualitative Disclosures About Market Risk (LAF/AF)
- **Part I, Item 4:** Controls and Procedures
  - Quarterly evaluation of DC&P effectiveness (CEO/CFO)
  - Disclosure of any material change in ICFR during the quarter that has materially
    affected, or is reasonably likely to materially affect, ICFR
- **Part II, Item 1:** Legal Proceedings (material changes from 10-K disclosure)
- **Part II, Item 1A:** Risk Factors (material changes from 10-K disclosure; SRC may omit)
- **Part II, Item 2:** Unregistered Sales of Equity Securities and Use of Proceeds;
  Issuer Purchases of Equity Securities (10b-18 buyback table)
- **Part II, Item 5:** Other Information (Rule 10b5-1 plan adoptions/terminations [VERIFY
  new disclosure requirement])
- **Part II, Item 6:** Exhibits (31.1, 31.2, 32.1, 32.2 certifications required every quarter)

---

#### Module C: Form 8-K

For each material event triggering Form 8-K, identify the applicable Item, apply the
4-business-day deadline, and assess whether the disclosure is adequate.

**Complete 8-K Triggering Event Matrix:**

| Item          | Event                                                                                     | 4-BD Deadline                                     | Common Materiality Question                                                                                                                                                         |
| ------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1.01**      | Entry into material definitive agreement                                                  | Yes                                               | Is the agreement "material"? Apply Basic Inc. v. Levinson "substantial likelihood" standard                                                                                         |
| **1.02**      | Termination of material definitive agreement                                              | Yes                                               | Is termination company-initiated or counterparty-initiated?                                                                                                                         |
| **1.03**      | Bankruptcy or receivership                                                                | Yes                                               | Includes filing for Chapter 11; voluntary petition triggers the clock                                                                                                               |
| **1.04**      | Mine safety — failure to meet best practices                                              | Yes                                               | Only for companies subject to MSHA                                                                                                                                                  |
| **1.05**      | Material cybersecurity incident [VERIFY effective date]                                   | Yes                                               | Materiality determination must precede the disclosure clock; disclose the nature, scope, timing, and material impact; ongoing investigations may delay but not eliminate disclosure |
| **2.01**      | Completion of acquisition or disposition of significant amount of assets                  | Yes                                               | Significance threshold: 20% or more of total assets under Reg. S-X Rule 1-02(w) [VERIFY]                                                                                            |
| **2.02**      | Results of operations and financial condition                                             | Yes (if separate from earnings release)           | Press release disclosing material non-public financial information triggers the Item                                                                                                |
| **2.03**      | Creation of direct financial obligation or obligation under off-balance-sheet arrangement | Yes                                               | Debt issuances above materiality threshold; guarantees                                                                                                                              |
| **2.04**      | Triggering events accelerating direct financial obligation                                | Yes                                               | Covenant defaults; cross-default triggers                                                                                                                                           |
| **2.05**      | Costs associated with exit or disposal activities                                         | Yes                                               | Restructuring charges; plant closures                                                                                                                                               |
| **2.06**      | Material impairments                                                                      | Yes                                               | Goodwill impairment; asset write-downs                                                                                                                                              |
| **3.01**      | Notice of delisting or transfer of listing                                                | Yes                                               | Exchange notification; rule violation notice                                                                                                                                        |
| **3.02**      | Unregistered sales of equity securities                                                   | Yes                                               | > $1 million in 180 days [VERIFY threshold]                                                                                                                                         |
| **3.03**      | Material modification to rights of security holders                                       | Yes                                               | Charter or bylaw amendment affecting substantive rights                                                                                                                             |
| **4.01**      | Changes in registrant's certifying accountant                                             | Yes                                               | Auditor dismissal or resignation; requires disclosure of disagreements, reportable events                                                                                           |
| **4.02**      | Non-reliance on previously issued financial statements                                    | Yes                                               | Restatement trigger; SEC staff may also trigger this via comment letter                                                                                                             |
| **5.01**      | Changes in control of registrant                                                          | Yes                                               | > 50% transfer of voting power                                                                                                                                                      |
| **5.02**      | Departure or appointment of directors or principal officers                               | Yes                                               | CEO, CFO, COO, CAO, General Counsel, Secretary departures/appointments                                                                                                              |
| **5.03**      | Amendments to articles or bylaws                                                          | Yes                                               | Material changes only                                                                                                                                                               |
| **5.04**      | Temporary suspension of trading under employee benefit plans                              | Yes                                               | Required before blackout period; Reg. BTR obligation                                                                                                                                |
| **5.05**      | Amendments to code of ethics                                                              | Yes                                               | Any waiver for executive officers or directors                                                                                                                                      |
| **5.06**      | Change in shell company status                                                            | Yes                                               | —                                                                                                                                                                                   |
| **5.07**      | Submission of matters to a vote of security holders                                       | Yes                                               | —                                                                                                                                                                                   |
| **5.08**      | Shareholder director nominations                                                          | Yes                                               | —                                                                                                                                                                                   |
| **6.01–6.05** | ABS-related items                                                                         | Yes                                               | Asset-backed securities only                                                                                                                                                        |
| **7.01**      | Regulation FD disclosure                                                                  | Yes (same day or prior to material disclosure)    | Selective disclosure of material non-public information to certain persons                                                                                                          |
| **8.01**      | Other events                                                                              | Voluntary                                         | Material information company elects to disclose                                                                                                                                     |
| **9.01**      | Financial statements and exhibits                                                         | With triggering 8-K or within 71 days (pro forma) | Acquisition financial statements                                                                                                                                                    |

**Cybersecurity incident disclosure (Item 1.05) — additional requirements:**

- Annual 10-K must include: description of processes for assessing/identifying/managing
  material risks from cybersecurity threats; material effect of cybersecurity risks; board
  oversight of cybersecurity risks; management's role and expertise [VERIFY S-K Item 106]
- The determination of materiality for Item 1.05 must be made promptly; indefinite delay
  pending law enforcement input is not permitted (FBI exception exists but is narrow)

---

#### Module D: DEF 14A — Proxy Statement

Assess against the SEC proxy rules (Regulation 14A, Schedule 14A):

**Director Nominees:**

- Five-year biographical information; other public company directorships
- Qualification disclosure: specific experience, attributes, and skills that qualify each
  nominee
- Independence determination under applicable exchange listing standards
- Interlocking directorships (Schedule 13D / 14D overlap)

**Executive Compensation (full Item 402 analysis — see Module A Item 11 above)**

**Say-on-Pay (Dodd-Frank § 951):**

- Annual advisory vote on executive compensation required (LAF/AF/NAF; EGCs exempt
  in certain years [VERIFY])
- Advisory vote on frequency (every 1, 2, or 3 years) required at least every 6 years
- Disclose how prior say-on-pay vote results informed compensation decisions

**Pay vs. Performance (Item 402(v)):**

- Required disclosure table with five years of data (three years for first-time filers)
- "Compensation Actually Paid" must be calculated per SEC formula (not just SCT values)
- CD&A must describe the relationship between CAP and company performance metrics

**Audit Committee Report:**

- Whether the committee reviewed and discussed the audited financial statements with management
- Whether it discussed AS 1301 communications with independent auditor
- Whether it received AS 2610 independence disclosures from the auditor
- Based on the foregoing, the committee's recommendation to the board

**Auditor Ratification:**

- Fee disclosure (same as 10-K Item 14)
- Say-on-auditor proposals (voluntary; not yet required but increasingly common)

**Director Compensation:**

- Director compensation table (prior fiscal year)
- Narrative description of material elements

**Anti-Hedging and Anti-Pledging Disclosure:**

- Required disclosure of any company policies regarding hedging by officers/directors [VERIFY]

**Compensation Clawback Policy (Rule 10D-1):**

- NYSE/Nasdaq listing standards required compliant policies by December 1, 2023 [VERIFY]
- Policy must apply to both "Big R" (restatement filing) and "little r" (restatement not
  requiring an amendment) restatements
- No-fault standard: recovery does not require misconduct finding
- Covers Incentive-Based Compensation received in the three fiscal years preceding the
  restatement trigger date
- Disclose whether any clawback was triggered during the fiscal year

---

#### Module E: Section 16 Forms 3, 4, and 5

**Assess for each Section 16 reporting person:**

**Reporting person identification:**
Who is a "Section 16 person" under Rule 16a-1?

- Every director
- Every "officer" as defined in Rule 16a-1(f) (broader than C-suite; see Step 5c above)
- Every person who beneficially owns more than 10% of any class of equity security
  registered under Section 12

**Form 3 checklist:**

- [ ] Filed within 10 days of becoming a Section 16 reporting person
- [ ] Includes all securities beneficially owned at time of becoming reporting person
      (direct and indirect; all forms of equity compensation)
- [ ] Correctly identifies relationship (director / officer / 10% holder)

**Form 4 checklist:**

- [ ] Filed within 2 business days of transaction execution date (not settlement date)
- [ ] Transaction code correct (P = open market purchase, S = open market sale,
      A = grant, D = disposition to issuer, M = exercise, etc.)
- [ ] Derivative and non-derivative security tables complete (all columns)
- [ ] Rule 10b5-1 plan adoption / modification / termination disclosed [VERIFY new rules]
- [ ] Late Form 4s disclosed in proxy statement (Item 10 of 10-K if applicable)

**Rule 10b5-1 plan compliance (new rules effective 2023):**

- Cooling-off period for directors and officers: the later of (a) 90 days after plan
  adoption or (b) the filing of the next Form 10-K or 10-Q — capped at 120 days [VERIFY]
- Cooling-off for other persons: 30 days
- Single-trade plans: only one per 12-month period
- Written representation in plan: no MNPI at time of adoption
- Company must file its insider trading policy as Exhibit 19 to Form 10-K [VERIFY]

**Short-swing profit recovery (Section 16(b)):**

- Any profit from purchase and sale (or sale and purchase) of issuer's equity securities
  within any six-month period by a Section 16 person is recoverable by the issuer
- Assess whether any transactions create six-month matching pairs that generate § 16(b)
  exposure; flag for counsel review

---

### Step 7: Anti-Fraud Compliance Overlay

Apply this overlay to every material disclosure item in the filing. This step is separate
from the item-level analysis because anti-fraud obligations apply even when an item is
technically completed.

**Legal standard:** Securities Act § 17(a) (offerings); Exchange Act § 10(b) and Rule 10b-5
(secondary market). The anti-fraud standard prohibits any material misstatement or omission
in connection with the purchase or sale of a security in a document filed with the SEC.

**For each material disclosure item, assess:**

1. **Accuracy:** Is every affirmative statement factually correct based on the available
   information?
2. **Completeness:** Is there any material fact whose omission would make the stated facts
   misleading? (The "half-truth" problem — incomplete truths are as actionable as outright
   misstatements)
3. **Consistency:** Is the disclosure consistent with other disclosures in the filing,
   and with other public statements made by the company (press releases, earnings calls,
   investor presentations)?
4. **Timeliness:** Was any material information known to the company at the time of filing
   that should have been disclosed?
5. **Currency:** For risk factors describing hypothetical risks, if any risk has already
   materialized, the risk factor must be updated to describe the actual impact

**PSLRA Safe Harbor for Forward-Looking Statements:**
Assess whether all forward-looking statements in the filing qualify for the Private
Securities Litigation Reform Act safe harbor (15 U.S.C. § 78u-5):

- [ ] Identified as forward-looking (oral or written)
- [ ] Accompanied by meaningful cautionary statements identifying important factors that
      could cause actual results to differ materially
- [ ] Cautionary language is substantive and specific — not boilerplate
- [ ] Made by a natural person (safe harbor does not apply to forward-looking statements
      made in connection with an initial public offering)

**Materiality standard:** Apply the "substantial likelihood" test from Basic Inc. v. Levinson,
485 U.S. 224 (1988) [VERIFY for current application]: information is material if there is
a substantial likelihood that a reasonable investor would consider it important in making an
investment decision. For contingent events, apply the probability × magnitude analysis:
weigh the probability the event will occur against the magnitude of its effect on the company.

---

### Step 8: Non-GAAP Financial Measures Assessment

If the filing or accompanying earnings release includes non-GAAP financial measures, assess
compliance with Regulation G and S-K Item 10(e).

**Required elements for each non-GAAP measure:**

- [ ] **Prominence rule:** The most directly comparable GAAP measure must be presented with
      equal or greater prominence than the non-GAAP measure. "Equal or greater prominence"
      means the GAAP measure appears first, in the same size font, and is not minimized in
      formatting.
- [ ] **Quantitative reconciliation:** A tabular reconciliation of the non-GAAP measure to
      the most directly comparable GAAP measure must be included (or provided by hyperlink
      to website for 8-K Item 2.02 disclosures)
- [ ] **Reason for use:** The company must explain why it presents the non-GAAP measure and
      how management uses it
- [ ] **Prohibited non-GAAP measures:** Net income calculated on a per-share basis using
      a denominator that excludes non-GAAP adjustments; non-GAAP measures that exclude
      charges or liabilities that require cash settlement; non-GAAP revenue measures
      (generally prohibited for registration statements [VERIFY])
- [ ] **Labeling:** Non-GAAP measures may not be labeled with GAAP terms (e.g., "Adjusted
      Revenue" is permissible; "Adjusted Net Revenue (GAAP)" is prohibited)
- [ ] **Consistency:** Non-GAAP adjustments must be applied consistently across periods;
      new exclusions or inclusions require disclosure and explanation

**Common SEC comment issues on non-GAAP:**

- Non-GAAP measure presented more prominently than comparable GAAP measure (most cited)
- Reconciliation that is incomplete or incorrect
- Non-GAAP measure that excludes recurring charges without adequate explanation
- "Adjusted EBITDA" that excludes charges that recur annually without explaining why
  they are excluded as non-recurring

---

### Step 9: EDGAR Filing Mechanics and XBRL Compliance

Assess the technical submission requirements regardless of the substantive disclosure quality.

**EDGAR general requirements:**

- [ ] Correct form type selected (10-K vs. 10-K/A; 8-K vs. 8-K/A; DEF 14A vs. PRE 14A)
- [ ] CIK number and filing agent credentials current
- [ ] All required exhibits filed as separate EDGAR exhibits with correct exhibit codes
      per S-K Item 601
- [ ] Filing date and period of report date correct
- [ ] Confidential treatment requests (CTR) filed for any exhibit redactions (Rule 24b-2;
      note that CTR must be re-filed every three years or the unredacted version must be filed)
- [ ] EDGAR submission is accessible and all documents render correctly

**Inline XBRL requirements:**
Inline XBRL (iXBRL) tagging using the SEC's EDGAR Inline XBRL Viewer is mandatory for:

- LAF and AF: Required for all periodic reports (10-K and 10-Q) and S-1/S-3 registration
  statements containing financial statements
- NAF and SRC: Phased-in requirements — confirm current phase applicable to the filer
  [VERIFY current phase-in schedule; check EDGAR Filer Manual Part IV]
- 8-K Item 2.02 exhibits: XBRL tagging required [VERIFY current requirement]

**XBRL tagging checklist:**

- [ ] All required financial statement elements tagged using current US GAAP taxonomy
      (FASB taxonomy version current as of filing date [VERIFY])
- [ ] Custom taxonomy elements created only when no standard element exists
- [ ] Cover page tags: entity name, CIK, fiscal year end, filer category, SIC code,
      IRS Employer ID, state of incorporation, entity well-known seasoned issuer,
      entity voluntary filers, current reporting status, interactive data current
- [ ] Footnote-level tagging (block tagging for text; detail tagging for numbers)
- [ ] R9000 and similar EDGAR validation errors resolved before filing

---

### Step 10: Enforcement Exposure Assessment

Synthesize all findings from Steps 5–9 into a consolidated enforcement exposure profile.

**Aggregate risk assessment by category:**

| Risk Category                 | Exposure Indicators                                                                                                 | Assessment                      |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **SEC comment risk**          | MD&A inadequacy; non-GAAP prominence; boilerplate risk factors; material weakness not disclosed; non-GAAP errors    | HIGH / MEDIUM / LOW             |
| **Restatement risk**          | Material weakness in ICFR; auditor-detected misstatement; non-GAAP reconciliation error; period errors              | YES / POSSIBLE / NO             |
| **Enforcement risk**          | Anti-fraud overlay findings; material omissions; insider trading policy gaps; cybersecurity disclosure delay        | HIGH / MEDIUM / LOW             |
| **Private action exposure**   | Section 11 (registration statements); Rule 10b-5 (secondary market); Section 12(a)(2) (prospectus)                  | ELEVATED / STANDARD / N/A       |
| **Exchange delisting risk**   | Delinquent filing; material weakness not remediated; audit committee independence failure; SOX certification issues | YES / POSSIBLE / NO             |
| **Amendment filing required** | Material misstatement or omission in filed document; incorrect period; missing required Item                        | YES / COUNSEL TO DETERMINE / NO |

**Civil monetary penalty tiers (Dodd-Frank § 929P) [VERIFY current amounts; adjusted annually]:**

| Tier       | Conduct                                                                            | Per Violation (Individual) | Per Violation (Entity) |
| ---------- | ---------------------------------------------------------------------------------- | -------------------------- | ---------------------- |
| **Tier 1** | Any violation                                                                      | ~$10,000                   | ~$100,000              |
| **Tier 2** | Fraud, deceit, manipulation, or deliberate disregard of rules                      | ~$100,000                  | ~$500,000              |
| **Tier 3** | Tier 2 conduct + substantial losses or significant risk of losses to other persons | ~$200,000                  | ~$1,000,000            |

Maximum penalties may also equal gross pecuniary gain from the violation.

---

### Step 11: SOX Certification Readiness

Assess whether the CEO and CFO have adequate basis for their required certifications.

**Section 302 Certification (Exhibit 31) — required quarterly and annually:**
The certifying officer must certify, to the best of their knowledge:

- [ ] The report does not contain any untrue statement of material fact or omit to state a
      material fact necessary to make the statements made not misleading
- [ ] The financial statements and other financial information fairly present in all material
      respects the financial condition, results of operations, and cash flows
- [ ] The signing officer is responsible for establishing and maintaining DC&P and ICFR
- [ ] The officer has evaluated DC&P effectiveness within 90 days prior to the report
- [ ] All significant deficiencies and material weaknesses in ICFR have been disclosed to
      the audit committee and to the auditors
- [ ] Any fraud involving management or other employees who have a significant role in
      ICFR has been disclosed

**Section 906 Certification (Exhibit 32) — required quarterly and annually:**
Criminal certification under 18 U.S.C. § 1350:

- Certifies the report "fully complies" with § 13(a) or § 15(d) of the Exchange Act
- Certifies the information contained in the report "fairly presents, in all material
  respects, the financial condition and results of operations of the issuer"
- **Willful false certification:** Up to $5 million fine and/or 20 years imprisonment
- **Knowing false certification:** Up to $1 million fine and/or 10 years imprisonment

**Disclosure Committee adequacy:**

- Does the company maintain a disclosure committee with defined responsibilities?
- Does the committee include appropriate cross-functional representation (Legal, Finance,
  IR, Operations)?
- Does the committee have a defined review schedule tied to filing calendars?
- Does the committee document its conclusions in writing?
- Are the committee's conclusions communicated to the CEO/CFO prior to certification?

---

### Step 12: Comment Letter Response Framework

_This step activates only in "Comment letter response" assessment mode (Step 2a, Option 3)._

For each SEC staff comment:

1. **Classify the comment** by category: Substantive inadequacy, Technical deficiency,
   Request for additional information, Accounting question, Legal conclusion request
2. **Assess the staff's legal basis** for the comment: Is it grounded in a specific
   rule, C&DI interpretation, or SEC enforcement precedent? If not, the comment may
   be responsive to a polite decline or request for basis.
3. **Draft a response framework** for each comment:
   - If agreeing to revise: Confirm the specific revision; provide revised language in
     the response or agree to revise in future filings
   - If declining to revise: Cite specific legal authority; explain why existing
     disclosure satisfies the applicable requirement; offer a supplemental explanation
     if the comment is based on a misreading of the filing
   - If requesting clarification: Ask the specific question; do not assume the staff's
     concern without basis
4. **Response letter logistics:**
   - File on EDGAR as a Correspondence (CORRESP) filing
   - Include the CIK and file number in the header
   - Address the response to the specific SEC staff attorney who signed the comment letter
   - Each comment must be quoted in full, followed by the company's response
   - All supplemental information provided to the staff must be treated as confidential
     or filed as a public CORRESP

---

## Section 8: Severity Classification

Apply this four-tier classification to every finding. Use the highest-applicable tier.

| Classification          | Definition                                                                                                                                                                                                                  | Required Action                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **COMPLIANT**           | Disclosure requirement fully met; adequate under applicable SEC rules, staff guidance, and anti-fraud standards                                                                                                             | Document; no change required                                                                                              |
| **PARTIAL**             | Disclosure exists but has identifiable gaps; likely to generate an SEC comment letter; does not yet create enforcement or private action risk if remediated promptly                                                        | Revise before filing, or flag for next filing if already filed                                                            |
| **NON-COMPLIANT**       | Disclosure requirement materially not met; elevated SEC comment letter risk and potential enforcement exposure; amendment filing should be considered                                                                       | Immediate revision; counsel engagement recommended before next filing                                                     |
| **CRITICAL DEFICIENCY** | Material misstatement or omission present; restatement risk; Rule 10b-5 private action exposure; Section 11 strict liability exposure (if offering document); insider trading concerns; SOX certification integrity at risk | Stop; engage qualified securities counsel immediately before any further securities transactions or public communications |

**Automatic CRITICAL DEFICIENCY triggers** — classify immediately without waiting for full
analysis to complete:

- Material weakness in ICFR that was not disclosed in the most recent 10-K or 10-Q
- Auditor resignation or dismissal that was not reported on Form 8-K Item 4.01
- Cybersecurity incident that was material and not reported within 4 business days
- Financial statement fraud by senior management
- CEO/CFO certification of a report known to contain a material misstatement
- Form 8-K Item 4.02 (Non-reliance) triggered but not filed
- Material related-party transaction not disclosed

---

## Section 9: Actionable Output Per Finding

For each finding, produce a structured finding entry:

```
FINDING: [Brief descriptive title]
Form Item: [e.g., Form 10-K, Item 7 / MD&A]
Classification: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]
Regulatory basis: [Specific rule, form instruction, C&DI, or anti-fraud standard]
Finding: [Precise description of the issue or gap]
Risk: [Specific consequence — SEC comment, restatement, enforcement exposure, private action]
Evidence: [Quote or describe the specific passage triggering the finding; if pre-filing,
           describe what is absent]
Remediation: [Specific, actionable revision — include proposed language where possible]
Responsible party: [CFO / General Counsel / Disclosure Committee / Audit Committee / IR]
Deadline: [BEFORE FILING / NEXT QUARTERLY FILING / NEXT ANNUAL FILING / IMMEDIATE]
Escalation: [Audit Committee notification? Board notification? Auditor communication?]
```

---

## Section 10: Prioritization Framework

Tier findings for remediation sequencing:

| Tier       | Label      | Criteria                                                                                                                                                                  | Timeline                                                                              |
| ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Tier 1** | Immediate  | CRITICAL DEFICIENCY findings; findings that affect the integrity of a filed certification; restatement risk; material omissions in filed documents                        | Before any further securities transactions; before next Form 8-K; same-day escalation |
| **Tier 2** | Pre-Filing | NON-COMPLIANT findings in a document not yet filed; PARTIAL findings in a document not yet filed; Item 9A material weakness disclosure; 8-K trigger not yet filed         | Before submission to EDGAR                                                            |
| **Tier 3** | Next Cycle | PARTIAL findings in already-filed documents that do not rise to amendment level; disclosure improvements for next annual or quarterly report; EDGAR technical corrections | Next periodic filing; or within 30–90 days if a comment letter is anticipated         |

---

## Section 11: Citation Quality Gates

Run these five gates **silently** before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                                                                                      | Fail Action                                            |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **Source**     | Every SEC rule or form instruction cited identifies the specific CFR section, form item, or release number                                                                | Add citation or mark [UNVERIFIED — counsel to confirm] |
| **Format**     | All citations follow consistent format: Rule 13a-15(e); S-K Item 303; 17 CFR § 229.303; Release No. 33-11216                                                              | Fix format                                             |
| **Currency**   | Every cited provision checked against most recent SEC rulemaking; thresholds (float, revenue, penalty amounts) carry [VERIFY current threshold]                           | Flag [CHECK CURRENCY]                                  |
| **Domain**     | Analysis stays within US federal securities law; no state law or accounting standards advice presented as SEC compliance                                                  | Remove or flag out-of-scope conclusions                |
| **Confidence** | Uncertainty explicitly stated; no hedge words when describing affirmative SEC obligations ("may be required" is inappropriate when a rule imposes a mandatory obligation) | Add confidence qualifier or restate as mandatory       |

---

## Section 12: Self-Interrogation for CRITICAL DEFICIENCY Items

For any finding classified CRITICAL DEFICIENCY, apply this three-pass adversarial review
before delivering:

**Pass 1 — Legal Chain Integrity:**
Does the risk assessment follow logically from the cited SEC rule or form instruction?
Would the SEC staff, a court, or a qualified securities attorney actually reach this
conclusion on these facts? Is the legal standard correctly stated?

**Pass 2 — Completeness:**
Have all relevant form items, rules, and anti-fraud provisions been considered?
Are there regulatory dimensions (state law Blue Sky, exchange listing standards,
PCAOB standards) that are outside this skill's scope but should be flagged?
Has the most recent SEC staff guidance been applied?

**Pass 3 — Challenge:**
What is the strongest argument that this disclosure is adequate? Under what circumstances
might a reasonable securities attorney advise the company that no change is necessary?
Have alternative interpretations of the disclosure requirement been considered?

If the finding survives all three passes: deliver with CRITICAL DEFICIENCY classification.
If the finding is weakened by the challenge: reclassify to NON-COMPLIANT and note the
basis for the downgrade in the output.

---

## Section 13: Confidence Scoring

| Level        | Range     | Meaning                                                                           | Action                                                                     |
| ------------ | --------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear mandatory rule; settled SEC staff position; form instruction is unambiguous | State as mandatory obligation with specific citation                       |
| **High**     | 0.80–0.94 | Strong regulatory basis; minor interpretive questions; established C&DI guidance  | State with brief caveat; recommend counsel confirmation                    |
| **Probable** | 0.60–0.79 | Reasonable interpretation; some interpretive ambiguity; emerging SEC focus area   | State with reasoning; present alternative interpretation; flag for counsel |
| **Possible** | 0.40–0.59 | Genuinely uncertain; depends on materiality judgment or fact-specific analysis    | Flag for professional review; present both sides with equal weight         |
| **Unlikely** | 0.0–0.39  | Speculative; unsupported by current SEC rules or guidance                         | Do not assert; flag [UNCERTAIN]                                            |

---

## Section 14: Glass Box Audit Trail

Every completed assessment must include this audit trail in the final output.

```yaml
glass_box:
  skill_name: "legalcode-sec-filing-checklist"
  assessment_date: "[YYYY-MM-DD]"
  entity: "[Company name or 'Not specified']"
  filer_category: "[LAF | AF | NAF | SRC | EGC | FPI | WKSI | Not determined]"
  forms_assessed: "[10-K | 10-Q | 8-K | DEF 14A | Forms 3/4/5 | Multiple]"
  fiscal_year_end: "[YYYY-MM-DD or 'Not specified']"
  filing_deadline: "[YYYY-MM-DD — calculated from filer category and form type, or 'Not calculated']"
  assessment_mode: "[Full review | Pre-filing | Comment letter response | IPO readiness | Targeted | Amendment]"
  sec_404b_applicable: "[Yes | No | Exempt (EGC/SRC/NAF)]"
  legalcode_mcp: "[Connected | Not connected]"
  authority_reference_file: "[/tmp/sec-filing-authority-[date].md | Not created]"
  modules_assessed:
    - "[Module A: Form 10-K — Items 1-15 | Not assessed]"
    - "[Module B: Form 10-Q | Not assessed]"
    - "[Module C: Form 8-K | Not assessed]"
    - "[Module D: DEF 14A | Not assessed]"
    - "[Module E: Section 16 Forms 3/4/5 | Not assessed]"
    - "[Step 7: Anti-Fraud Overlay | Not assessed]"
    - "[Step 8: Non-GAAP Compliance | Not assessed]"
    - "[Step 9: EDGAR/XBRL | Not assessed]"
    - "[Step 10: Enforcement Exposure | Not assessed]"
    - "[Step 11: SOX Certification Readiness | Not assessed]"
  findings_summary:
    critical_deficiency: "[count]"
    non_compliant: "[count]"
    partial: "[count]"
    compliant: "[count]"
  restatement_risk: "[Yes | Possible | No]"
  sec_comment_risk: "[High | Medium | Low]"
  amendment_filing_recommended: "[Yes | No | Counsel to determine]"
  self_interrogation_applied: "[Yes — N critical findings reviewed | Not applicable]"
  citations_verified: "[N verified | N unverified — marked [VERIFY]]"
  confidence: "[HIGH | MEDIUM | LOW] — [rationale]"
  sec_enforcement_note: >
    [Any recent SEC enforcement actions, rule amendments, or staff guidance materially
    affecting this assessment. Note date of assessment relative to rule effective dates.
    Highlight: Cybersecurity rule effective Dec 18, 2023 (LAF/AF) / Jun 15, 2024 (smaller);
    Pay vs. Performance effective for proxy statements filed after Jan 27, 2023;
    Clawback policy required by Dec 1, 2023 per exchange listing standards;
    Rule 10b5-1 cooling-off period reforms effective Feb 27, 2023;
    Climate disclosure rule adopted Mar 2024, stayed Apr 2024, rescission proposed
    Feb 2025 — monitor for developments before including in 10-K disclosures [VERIFY].]
  limitations:
    - "[Documents not provided — analysis based on description only; fact verification required]"
    - "[Financial statement analysis is structural only — not a substitute for auditor review]"
    - "[State law, Blue Sky, and exchange listing standards not assessed]"
    - "[PCAOB attestation procedures not assessed — refer to auditors]"
    - "[Materiality determinations are AI-assisted — final determination requires qualified counsel]"
  reviewer: "AI-assisted — requires qualified securities counsel and CPA review before reliance or CEO/CFO certification"
```

---

## Section 15: Anti-Patterns

The following failure modes are the most common causes of SEC comment letters, enforcement
actions, and restatements. Do NOT commit these errors in the output.

1. **Boilerplate risk factors** — Using generic industry-wide risk factors that could apply
   to any public company in the industry (e.g., "We may be adversely affected by economic
   conditions") without company-specific disclosure of how the risk applies to this company
   and what the potential impact is.

2. **Describing risks that have already materialized** — A risk factor that describes a
   hypothetical risk that has already occurred must be updated to disclose the actual
   impact and current status — not left as a hypothetical.

3. **MD&A that identifies factors without quantifying them** — "Revenue increased primarily
   due to higher volume and favorable pricing" is inadequate; SEC staff expects
   quantification of the contribution of each driver.

4. **Non-GAAP prominence inversion** — Presenting Adjusted EBITDA before GAAP net income
   in press releases or earnings presentations; using a larger font or bold formatting for
   the non-GAAP measure; presenting the GAAP reconciliation only in a footnote.

5. **Conflating DC&P and ICFR** — Treating the quarterly DC&P evaluation and the annual
   ICFR assessment as the same thing; applying COSO only to financial reporting controls
   and failing to assess whether all required SEC disclosures are captured in the disclosure
   process.

6. **Treating the 8-K clock as running from discovery** — The 4-business-day clock for
   material events runs from the date the event occurs or the company becomes aware of it
   (for Item 1.05, from the materiality determination date — not the discovery date). Do
   not advise a company to delay filing until it has "all the facts."

7. **Cybersecurity boilerplate** — Annual 10-K cybersecurity governance disclosure that is
   not tailored to the company's actual processes, board oversight mechanisms, or
   management expertise; generic statements about "industry best practices" that cannot be
   substantiated.

8. **Pay vs. Performance calculation errors** — Using SCT grant-date values instead of
   year-end fair values for unvested equity awards in the Compensation Actually Paid
   calculation; failing to subtract forfeitures; applying the wrong measurement date.

9. **Missing exhibit filings** — Filing the 10-K without Exhibit 19 (Insider Trading
   Policy), Exhibit 97 (Clawback Policy), or current SOX certification exhibits; failing
   to re-file exhibits when the underlying documents are amended.

10. **Confidential treatment request expiration** — Allowing CTRs for redacted exhibits
    to expire (three-year limit) without renewal, causing unredacted versions to become
    publicly accessible on EDGAR.

11. **Section 16 officer definition errors** — Limiting Section 16 reporting to C-suite
    executives and failing to include division heads, business unit presidents, or
    other policy-making officers under Rule 16a-1(f); resulting in untimely Form 3/4
    filings that must be disclosed in the proxy.

12. **Form 4 settlement date error** — Filing Form 4 based on the trade settlement date
    (T+2 or T+1) rather than the trade execution date, causing systematic late filings
    for all open-market transactions.

13. **Anti-fraud half-truth violations** — Disclosing favorable facts while omitting
    unfavorable facts that are necessary to make the disclosed facts not misleading;
    this is treated as a material misstatement even if every stated fact is technically
    accurate.

14. **Failing to update disclosure for known post-balance-sheet events** — Material events
    occurring between fiscal year end and the filing date that affect the financial
    statements must be disclosed as subsequent events; material events occurring before
    filing must be reflected in the MD&A's discussion of subsequent developments.

15. **Clawback policy scope errors** — Limiting the clawback policy to cash incentive
    compensation or to "Big R" restatements only; failing to cover equity awards; failing
    to cover the required three-year lookback period; conditioning clawback on a finding
    of misconduct (the standard is no-fault).

16. **PSLRA safe harbor misapplication** — Claiming PSLRA safe harbor protection for
    forward-looking statements made in connection with an IPO (the safe harbor does not
    apply to initial public offerings); using boilerplate cautionary language that does not
    identify specific meaningful factors that could cause actual results to differ.

17. **Stale rule citations** — Citing the version of a rule or threshold that applied in
    a prior year without checking for amendments; this is particularly acute for EGC
    revenue thresholds (adjusted annually), Dodd-Frank penalty amounts (adjusted annually),
    and EDGAR taxonomy versions (updated annually by FASB).

18. **Related-party transaction threshold misapplication** — Applying a $120,000 threshold
    without accounting for aggregated transactions with the same related party across the
    fiscal year; treating transactions as "ordinary course" without applying the S-K Item
    404 analysis.

19. **Director independence self-assessment** — Allowing the board (including the director
    whose independence is at issue) to determine independence without applying the specific
    objective tests of the applicable exchange listing standards and Rule 10A-3.

20. **Treating the climate disclosure rule as effective** — As of early 2025, the SEC's
    climate disclosure rule (Release No. 33-11275) is stayed pending litigation, and
    rescission has been proposed. Advising companies to include climate disclosures under
    this rule in their 10-K is premature; monitor for developments. Voluntary ESG
    disclosures remain permissible but are not required by this rule in its stayed state.
    [VERIFY current status before any filing].

---

## Section 16: Writing Standards

Apply these standards to all output. Run these gates silently before delivery.

**Mandatory obligations must be stated mandatorily:**
Never use hedge words ("may," "could," "might") when describing an affirmative SEC
obligation. "The company may be required to file a Form 8-K" is wrong if a triggering
event has occurred; write "The company must file a Form 8-K within 4 business days."

**Quantify where SEC staff would quantify:**
If describing an MD&A deficiency, provide an example of what adequate disclosure would
look like, including the quantification that is missing.

**Active voice for remediation instructions:**
Not "A revision to Item 7 should be considered" but "Revise Item 7 to quantify the
specific dollar contribution of each factor driving the year-over-year revenue change."

**Distinguish mandatory from recommended:**
Clearly distinguish between violations of SEC rules (mandatory to fix) and disclosure
improvements that would reduce comment letter risk (recommended). Label each finding
in the output accordingly.

**No legal conclusions on contested issues:**
When a disclosure question is genuinely contested (e.g., whether a particular cybersecurity
incident is "material" under the new rules), present both sides with equal weight and
recommend counsel determination. Do not state one side as the correct answer.

**Pre-delivery quality gates:**

- [ ] All form item numbers verified against the applicable form and year
- [ ] All rule numbers verified against 17 CFR
- [ ] All thresholds marked [VERIFY] where amounts adjust annually
- [ ] Findings are specific to the company's facts, not generic
- [ ] Remediation instructions are actionable, not general guidance
- [ ] Output template is complete with all required sections

---

## Section 17: External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 3, search for current form instructions, C&DIs, and staff guidance for all
  applicable forms
- In Step 7, search for relevant SEC enforcement actions involving anti-fraud claims in
  the company's industry
- In Step 10, search for recent SEC comment letter themes by industry (SEC posts sample
  comment letters on its website periodically)
- Save all results to `/tmp/sec-filing-authority-[YYYY-MM-DD].md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Proceed with repository knowledge and web research
- Mark all specific rule thresholds and form instruction references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Focus the assessment on structural gaps and pattern-based analysis rather than
  current-threshold verification
- Always recommend counsel confirmation of specific deadlines, thresholds, and
  effective dates before reliance

**Graceful degradation:**
If neither legalcode-mcp nor web research is available for a particular question, apply
the confidence scoring framework: if confidence drops below Probable (0.60) on a
threshold or deadline, flag [UNCERTAIN — verify with SEC.gov or qualified counsel before
reliance] rather than presenting a potentially stale figure as current.

---

## Section 18: Output Format Template

Deliver findings in the following structured format. Customize section headings for the
specific form(s) assessed.

---

```markdown
# SEC Filing Compliance Assessment

**Entity:** [Company name]
**Form(s) Assessed:** [10-K / 10-Q / 8-K / DEF 14A / Forms 3/4/5]
**Period:** [Fiscal year end / Quarter end / Filing date]
**Filer Category:** [LAF / AF / NAF / SRC / EGC / FPI]
**Assessment Date:** [YYYY-MM-DD]
**Assessment Mode:** [Full Review / Pre-Filing / Comment Letter / IPO Readiness / Targeted / Amendment]

---

## Executive Summary

**Overall Assessment:** [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY — use highest tier found]

**Key Findings:**
| Priority | Finding | Classification | Deadline |
|----------|---------|----------------|----------|
| Tier 1 — Immediate | [Title] | CRITICAL DEFICIENCY | BEFORE FILING |
| Tier 2 — Pre-Filing | [Title] | NON-COMPLIANT | BEFORE SUBMISSION |
| Tier 3 — Next Cycle | [Title] | PARTIAL | NEXT ANNUAL FILING |

**Filing Deadline Compliance:**

- Form 10-K due: [date] — [ON TRACK / AT RISK / OVERDUE]
- Form 10-Q (Q[N]) due: [date] — [ON TRACK / AT RISK / OVERDUE]
- Next Form 8-K trigger: [description] — [FILED / PENDING / OVERDUE]

---

## Filer Category Analysis

[Filer category determination with float/revenue basis; reclassification risk if applicable]

---

## Form-Specific Findings

### [Form 10-K / Form 10-Q / Form 8-K / DEF 14A / Section 16]

#### [Item Number — Item Title]

**Classification:** [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]
**Finding:** [Description]
**Risk:** [Specific consequence]
**Remediation:** [Actionable instruction]
**Responsible Party:** [Role]
**Deadline:** [BEFORE FILING / NEXT QUARTERLY / NEXT ANNUAL / IMMEDIATE]

[Repeat for each Item assessed]

---

## Anti-Fraud Overlay Assessment

[Results of Step 7 analysis — any material misstatement or omission risk]

## Non-GAAP Compliance Assessment

[Results of Step 8 — if applicable]

## EDGAR/XBRL Technical Assessment

[Results of Step 9]

## Enforcement Exposure Summary

[Aggregate risk table from Step 10]

## SOX Certification Readiness

[Results of Step 11 — basis for CEO/CFO 302 and 906 certifications]

---

## Remediation Plan

### Tier 1 — Immediate Actions

[Specific actions required before any further securities transactions or public filings]

### Tier 2 — Pre-Filing Actions

[Specific revisions required before the next EDGAR submission]

### Tier 3 — Next Cycle Improvements

[Disclosure improvements for the next periodic report]

---

## Glass Box Audit Trail

[Insert completed YAML from Section 14]

---

> ⚠️ **Disclaimer**: This assessment is AI-assisted and does not constitute legal advice,
> accounting advice, or a compliance certification. All findings must be reviewed by
> qualified securities counsel and a certified public accountant before reliance.
> This output may not be used as the basis for a CEO or CFO Section 906 certification
> under 18 U.S.C. § 1350.
```

---

## Localization Notes

This skill is **US federal securities law specific** and is not jurisdiction-agnostic. It
does not apply to:

- Companies reporting under UK DTR, EU Transparency Directive, or IFRS-based regimes
- Companies filing Form 20-F (Foreign Private Issuers — use a jurisdiction-specific FPI skill)
- Canadian reporting issuers (use SEDAR+ and NI 51-102 requirements)
- Companies listed on AIM, Euronext, or other non-US exchanges

For multi-jurisdictional reporting companies (e.g., SEC registrant with European operations
subject to CSRD), this skill covers only the SEC/Exchange Act compliance layer. Coordinate
with `legalcode-esg-sustainability-reporting` and `legalcode-eu-csrd-sustainability-reporting`
for the European layer.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

- Deep web research into SEC form instructions, Regulation S-K, Regulation S-X, and EDGAR
  Filer Manual requirements (current as of March 2026)
- SEC Final Rule releases: Release No. 33-11216 (cybersecurity disclosure, Dec. 2023);
  Release No. 33-11313 (Pay vs. Performance, Aug. 2022); SEC Final Rule on clawback
  policies (Oct. 2022); SEC Final Rule amending Rule 10b5-1 (Dec. 2022)
- Structural patterns and quality frameworks drawn from `legalcode-contract-review`,
  `legalcode-us-fcpa-compliance`, `legalcode-securities-regulation-compliance`, and
  `legalcode-sox-compliance-assessment` (all within the Legalcode repository)
- Agent team analysis: Structural Analyst (pattern extraction) + Research Agent (SEC rule
  verification)
- All regulatory thresholds marked [VERIFY] given annual adjustment by the SEC

Attribution: Legalcode original synthesis. Not derived from any third-party skill.
