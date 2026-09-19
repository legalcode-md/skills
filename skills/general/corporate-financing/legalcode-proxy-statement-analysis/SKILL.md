---
name: legalcode-proxy-statement-analysis
description: Deep analysis of SEC Form DEF 14A proxy statements for US public companies. Use when conducting
  proxy statement disclosure review for institutional investors, activist shareholders, proxy advisory
  firms, SEC compliance teams, governance counselors, or in-house legal teams preparing for annual meeting
  season.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Deep analysis of SEC Form DEF 14A proxy statements for US public companies. Covers director nominations and board composition (independence standards, tenure, skills matrix, overboarding, conflicts of interest), executive compensation (CD&A narrative quality, Summary Compensation Table, Grants of Plan-Based Awards, pay-versus-performance table and CAP calculations, clawback policy, say-on-pay responsiveness, CEO pay ratio, perquisites), related party transactions (Item 404 compliance, $120K threshold, written review policies), shareholder proposals (Rule 14a-8 eligibility, ESG themes, board opposition rationale), audit committee (composition, financial expert designation, auditor fees by category, pre-approval policies), and voting standards (majority vs. plurality, broker non-votes, universal proxy, virtual meeting disclosure). Flags disclosure deficiencies against SEC Regulation S-K Items 401, 402, 404, 407, Schedule 14A, Rules 14a-8, 14a-19, 14a-21, and NYSE/Nasdaq listing standards. Classifies findings by type (OMISSION, INCOMPLETE, MISCHARACTERIZED, QUANTIFICATION GAP, COMPARATIVE GAP, TRANSPARENCY GAP) and severity (DEFICIENT / PARTIAL / COMPLIANT). Models pay-versus-performance across target, peer-50th-percentile, and peer-75th-percentile scenarios. Applies dual-perspective framing (investor / management view) to every material finding. Produces a confidence-scored, auditable analysis with Glass Box trail and remediation roadmap. Use when conducting proxy statement disclosure review for institutional investors, activist shareholders, proxy advisory firms, SEC compliance teams, governance counselors, or in-house legal teams preparing for annual meeting season. Jurisdiction: United States — domestic public company issuers filing with the SEC. Not applicable to foreign private issuers filing Form 20-F without modification.


# Legalcode Proxy Statement Analysis

> **Disclaimer**: This skill provides a framework for AI-assisted analysis of SEC proxy
> statement disclosures. It does not constitute legal advice or securities law advice.
> All outputs should be reviewed by a qualified securities attorney or governance
> professional before use. SEC rules, Regulation S-K requirements, and proxy advisory
> guidelines change annually — verify currency of all cited requirements before relying
> on them. AI-generated analysis may contain errors in regulatory interpretation,
> financial modeling, or benchmark comparisons — verify all material conclusions
> independently. Statutory and regulatory references carry hallucination risk; verify
> against current SEC.gov source text and exchange listing standards before acting.

---

## Purpose and Scope

This skill analyzes SEC Form DEF 14A proxy statements for US public companies. It
evaluates disclosure completeness against SEC Regulation S-K requirements, exchange
listing standards, and proxy advisory voting guidelines, then identifies deficiencies
and produces an actionable remediation roadmap.

**Covers:**

- Director nominations, board composition, independence, and governance structure
- Executive compensation: CD&A, Summary Compensation Table, PvP table, clawback,
  say-on-pay, CEO pay ratio, perquisites
- Related party transactions: Item 404 compliance and written policy review
- Shareholder proposals: Rule 14a-8 eligibility and board opposition rationale
- Audit committee: composition, financial expert, fee disclosure, pre-approval policies
- Voting standards: majority/plurality mechanics, broker non-votes, virtual meetings
- Missing disclosure detection across all Schedule 14A items
- Pay-versus-performance scenario modeling (target / peer-50th / peer-75th)
- Dual-perspective framing: investor/governance advocate view vs. management view
- Confidence-scored findings with Glass Box audit trail

**Does not:**

- Provide legal advice or replace qualified securities counsel
- Analyze foreign private issuers filing Form 20-F without material adaptation
- Review definitives (merger agreements, transaction proxies) — see
  `legalcode-purchase-agreement-review` or `legalcode-ma-due-diligence-checklist`
- Conduct fund-return or IRR analysis from the investor's portfolio perspective
- Draft proxy statement sections from scratch — this skill reviews, does not draft

---

## Jurisdiction and Governing Law

**Jurisdiction**: United States federal securities law.

**Primary authority**: Securities Exchange Act of 1934, Section 14(a); Regulation 14A
(17 CFR Part 240, Rules 14a-1 through 14b-2); Schedule 14A (Rule 14a-101); SEC
Regulation S-K (17 CFR Part 229).

**Exchange listing standards**: NYSE Listed Company Manual (Rule 303A) and Nasdaq
Listing Rule 5600 series govern director independence, board composition, and committee
requirements. The skill identifies which exchange the company is listed on and applies
the relevant standards.

**Proxy advisory guidelines**: ISS US Benchmark Policy and Glass Lewis US Benchmark
Policy are referenced as market expectations but do not carry the force of law. Both
update annually; always confirm the guidelines edition applicable to the filing year
before relying on them.

**Scope limitations**:

- Smaller reporting companies (SRCs) and emerging growth companies (EGCs) are exempt
  from certain disclosures (CD&A, PvP table, CEO pay ratio). Confirm filer status at
  the outset.
- Foreign private issuers (FPIs) file Form 20-F with materially different compensation
  and governance disclosure requirements. Do not apply this skill to FPIs without
  confirming applicability of each item.
- State law governs meeting mechanics (quorum, voting, virtual meetings); the skill
  flags issues but does not provide state-specific legal analysis.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming context, the workflow pauses with **⟁ CLARIFY** wherever:

- The answer would change the scope or direction of the analysis
- Multiple valid analytical approaches exist and the user's priority matters
- Ambiguity in the proxy creates a classification fork requiring user judgment
- Business context (activist posture, SEC response timeline) affects recommended
  remediation urgency

Present structured options with descriptions wherever marked **⟁ CLARIFY**. If the
user has already provided the information, skip the question and proceed. Never assume
silently — state all assumptions explicitly when proceeding without full context.

---

## Workflow

### Step 1: Accept the Proxy Statement

Accept the DEF 14A in any of these formats:

- **File**: PDF or DOCX of the filed proxy statement
- **EDGAR URL**: Link to the filing on SEC EDGAR (fetch the filing directly)
- **Company reference**: Ticker symbol or CIK number — retrieve from EDGAR
- **Prior + current year**: Both proxies for year-over-year delta analysis

If no proxy statement is provided, ask the user to supply one before proceeding.

Identify immediately:

1. **Filer type**: Accelerated filer, large accelerated filer, SRC, EGC, or non-
   accelerated filer — this determines which disclosure items apply.
2. **Exchange listing**: NYSE vs. Nasdaq — this determines which listing standards apply.
3. **Filing date** and **annual meeting date**.
4. **Fiscal year end** covered by the proxy.

---

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the analysis, ask (skip any already answered by the
user's prompt):

1. **Primary stakeholder perspective:**
   - **Institutional Investor**: Assess disclosure quality for fiduciary voting decisions
   - **Activist / Governance Advocate**: Expose gaps for engagement or campaign support
   - **Management / In-House Counsel**: Identify compliance gaps before filing or SEC review
   - **Proxy Advisory Firm**: Build voting recommendation analysis
   - **Securities Counsel**: SEC comment letter response preparation
   - _Why this matters_: Dual-perspective framing is always applied, but the primary
     audience determines which findings lead the report and how remediation is framed.

2. **Scope of review:**
   - **Full disclosure review**: All Schedule 14A items (director, compensation, related
     party, audit, shareholder proposals, voting)
   - **Executive compensation focus**: CD&A, PvP, say-on-pay, clawback, perquisites
   - **Board governance focus**: Director independence, composition, conflicts, skills
   - **Related party transactions**: Item 404 compliance and written policy
   - **Shareholder proposal analysis**: ESG, governance, social proposals
   - **Multiple focus areas** (specify)
   - _Why this matters_: Full review requires comprehensive analysis across 7 sections;
     focused reviews can prioritize depth on selected areas.

3. **Benchmarking approach for pay-versus-performance (if compensation is in scope):**
   - **Use the disclosed peer group** (CD&A specifies comparables)
   - **Provide a custom peer group** (user specifies alternative comparables)
   - **Use industry median only** (no specific peers — limit analysis accordingly)
   - **Skip benchmarking** (flag peer disclosure adequacy only)
   - _Why this matters_: PvP scenario modeling requires a reference peer group.

4. **Prior year comparison:**
   - **First-time review** (baseline analysis only)
   - **Annual update** (prior year proxy available — flag year-over-year changes)
   - **Post-incident** (following activist campaign, <50% say-on-pay, or SEC comment)
   - **Pre-filing review** (draft proxy — identify gaps before filing)
   - _Why this matters_: Prior year comparison enables delta analysis of compensation
     structure changes, board composition shifts, and disclosure evolution.

If the user provides partial context, proceed with what is available and **state all
assumptions explicitly** (e.g., "Proceeding as institutional investor perspective,
full disclosure review — revise me if different").

---

### Step 3: Load Disclosure Standards

Check for an organization-specific proxy review framework or governance standards
document (e.g., `governance-standards.md`, `proxy-review-playbook.md`) in local settings.

**If no framework is found:**

**⟁ CLARIFY** — Inform the user and ask which baseline to apply:

- **Option A: SEC Regulation S-K baseline** — Apply the full SEC disclosure requirement
  checklist: Schedule 14A Items 1–21, Regulation S-K Items 401, 402, 404, 407, Rules
  14a-8, 14a-19, 14a-21, and applicable exchange listing standards. This is the
  enforcement standard. Label findings: "Based on SEC Regulation S-K requirements."
- **Option B: ISS/Glass Lewis alignment** — Apply proxy advisory voting guidelines
  as the primary standard, flagging where the filing may trigger negative voting
  recommendations. More conservative than SEC minimum requirements.
- **Option C: Organization-specific standards** — The user provides their organization's
  preferred positions on director tenure, pay structure, ESG disclosure, etc.

Proceed with Option A by default if no clarification is provided. State this assumption.

---

### Step 4: Gather Legal Authority

Use **legalcode-mcp** (if connected) to retrieve current text of:

- SEC Regulation S-K Items 401, 402 (all sub-items), 404, 407
- Schedule 14A Items 1–21 (specifically Items 7–10 for compensation, Item 9 for audit)
- Rules 14a-8, 14a-19, 14a-21
- NYSE Rule 303A series / Nasdaq Rule 5600 series (as applicable)
- Recent SEC staff comment letter summaries on proxy statement deficiencies
- Current ISS and Glass Lewis US Benchmark Policy editions (if accessible)

Save verified authority to `/tmp/proxy-statement-authority.md`:

```markdown
# Legal Authority Reference — DEF 14A Analysis

## Company: [Name] | Ticker: [X] | Fiscal Year: [YYYY]

## Date Gathered: [YYYY-MM-DD]

### SEC Regulations Applied

- Reg S-K Item 402(v) — Pay Versus Performance [VERIFIED / UNVERIFIED]
- Reg S-K Item 404(a) — Related Party Transactions [VERIFIED / UNVERIFIED]
- [...]

### Exchange Standards Applied

- NYSE Rule 303A.01 — Director independence [VERIFIED / UNVERIFIED]
- [...]

### Proxy Advisory Guidelines

- ISS US Benchmark Policy [Edition year] [VERIFIED / UNVERIFIED]
- Glass Lewis US Benchmark Policy [Edition year] [VERIFIED / UNVERIFIED]

### Recent SEC Comment Patterns

- [Summary of recent staff focus areas]
```

**If legalcode-mcp is not connected:**

- Mark every statutory citation with [VERIFY]
- Proceed using the framework below with general SEC Reg S-K knowledge
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Cross-reference all regulatory citations against SEC.gov before acting on findings

---

### Step 5: Map the Proxy's Disclosure Landscape

Before clause-by-clause analysis, extract and document from the filing:

| Item                            | Finding                                                                    |
| ------------------------------- | -------------------------------------------------------------------------- | ----------------- | --------------- |
| Filer type                      | [Large accelerated / Accelerated / Non-accelerated / SRC / EGC]            |
| Exchange                        | [NYSE / Nasdaq / Other]                                                    |
| Fiscal year end                 | [Date]                                                                     |
| Filing / meeting dates          | [Proxy filed: X                                                            | Meeting date: Y]  |
| Named executive officers        | [N] NEOs — CEO: [name]                                                     | CFO: [name]       | Others: [names] |
| Board composition               | [N] directors                                                              | [N] independent   | [N] committees  |
| Prior say-on-pay outcome        | [% For / % Against / Abstentions]                                          |
| Auditor                         | [Firm name]                                                                | [Tenure: N years] |
| Shareholder proposals           | [N] proposals filed                                                        | [N] included      | [N] excluded    |
| Material year-over-year changes | [New CEO / New comp structure / Board refresh / Activist pressure / Other] |

Flag immediately if any of the following are absent (RED without further analysis):

- No CD&A for an accelerated filer that is not an SRC or EGC
- No PvP table for a fiscal year ending after December 16, 2022 (non-SRC, non-EGC,
  non-FPI accelerated filer)
- No clawback policy disclosure (Exhibit 97 / Item 402(w)) for a listed company post
  December 1, 2023
- No audit committee report
- No auditor fee table

---

### Step 6: Section-by-Section Disclosure Analysis

Analyze each major proxy section using the classification system in the **Disclosure
Deficiency Framework** section below. Read the entire proxy before classifying
individual findings — sections interact (e.g., an independence issue in the board
section may interact with a related-party transaction in Item 404).

**⟁ CLARIFY** — For proxies exceeding 80 pages or with complex compensation structures
(multiple equity plans, international pay components, multiple NEO changes mid-year):

- Ask whether to perform a **full analysis** of all seven sections or a **priority
  analysis** limited to the user's stated focus areas plus any immediately apparent
  DEFICIENT items.
- If the proxy incorporates by reference any documents (e.g., "See our Corporate
  Governance Guidelines at [URL]"), ask whether the user wants those incorporated
  documents reviewed as part of this analysis.

Cover all seven sections below (unless a priority review was agreed):

---

#### Section A: Director Nominations and Board Composition

**Governing authority**: Reg S-K Items 401(e), 407(a)–(c); NYSE Rule 303A /
Nasdaq Rule 5605; Exchange Act Rule 10A-3 (audit committee); Rule 10C-1
(compensation committee).

**Checklist — classify each item as DEFICIENT / PARTIAL / COMPLIANT:**

| #   | Disclosure Item                                                                 | Authority              | Depth    |
| --- | ------------------------------------------------------------------------------- | ---------------------- | -------- |
| A1  | Each nominee's specific qualifications, attributes, and skills explained        | Reg S-K Item 401(e)    | Deep     |
| A2  | Independence status identified for each director; standard applied named        | Reg S-K Item 407(a)    | Deep     |
| A3  | Committee-level independence confirmed (audit: Rule 10A-3; comp: Rule 10C-1)    | Reg S-K Item 407(b)    | Deep     |
| A4  | Audit committee financial expert named; independence confirmed                  | Reg S-K Item 407(d)(5) | Deep     |
| A5  | Nominating committee's diversity consideration process described                | Reg S-K Item 407(c)    | Standard |
| A6  | Chair/CEO separation explained; lead independent director disclosed if combined | NYSE 303A.03           | Standard |
| A7  | Board oversight of risk management described with specificity                   | Schedule 14A           | Standard |
| A8  | Director tenure, age, and overboarding status assessable from disclosure        | Best practice          | Standard |
| A9  | Skills/competency matrix or equivalent board composition disclosure             | Best practice          | Standard |
| A10 | Cybersecurity governance disclosure at board level (post-Dec 2023)              | Reg S-K Item 106       | Deep     |

**Deep analysis for DEFICIENT items:**

For each DEFICIENT finding, apply the dual-perspective frame:

_Investor/Governance Advocate View_: Explain the governance risk and how ISS/Glass
Lewis would likely respond (e.g., "ISS will recommend against all members of the
nominating committee if the board lacks a sufficient independence majority").

_Management View_: Explain why management may view the disclosure as adequate and what
competitive or confidentiality arguments apply.

**Key red flags to escalate immediately:**

- Director described as "independent" despite a disclosed related-party relationship,
  consulting fee, or family-member employment within the three-year look-back period
- No audit committee financial expert identified
- Audit committee member who is also an executive officer or who fails Rule 10A-3
- Board with fewer than three independent directors (NYSE/Nasdaq non-compliance risk)
- Any nominee with five or more concurrent public company board seats (CEO: four or more)
- Qualifications section using boilerplate language that does not tie to specific
  oversight responsibilities

---

#### Section B: Executive Compensation (CD&A and Compensation Tables)

**Governing authority**: Reg S-K Items 402(a)–(w); Rule 14a-21 (say-on-pay/frequency).

This is the deepest analytical section. Work through each sub-item:

**B1 — CD&A Narrative Quality (Item 402(b))**

| Requirement                                                                         | Compliant? | Notes |
| ----------------------------------------------------------------------------------- | ---------- | ----- |
| Objectives of the compensation program stated                                       |            |       |
| Behaviors/outcomes the program is designed to reward described                      |            |       |
| Each compensation element identified (salary, bonus, equity, benefits, perquisites) |            |       |
| Rationale for choosing each element explained                                       |            |       |
| Amount/level determination process described                                        |            |       |
| Performance metrics and targets disclosed (or withheld with adequate explanation)   |            |       |
| How most recent say-on-pay vote influenced current compensation decisions           |            |       |

**Critical CD&A deficiency patterns:**

- Boilerplate "pay for performance" statement without substantive analysis of the link
- Performance targets entirely omitted with only a generic "competitively sensitive"
  claim and no discussion of target difficulty — SEC Staff has flagged this repeatedly
- No responsiveness discussion after say-on-pay support below 80% (below 70%:
  substantive engagement disclosure expected; below 50%: highest degree of scrutiny)
- Peer group selection criteria unexplained or peers materially different in size/sector

**B2 — Summary Compensation Table (Item 402(c))**

Verify:

- Three fiscal years of data for all NEOs who served during the most recent year
- All SCT columns present: salary, bonus, stock awards (ASC 718 grant date FV), option
  awards, non-equity incentive plan compensation, change in pension value, all other
  compensation
- "All Other Compensation" column: perquisites itemized if any single item exceeds the
  greater of $25,000 or 10% of total perquisites; totaling >$10,000 triggers disclosure
- Consistent NEO identification across all three years (departures noted)

**B3 — Pay Versus Performance Table (Item 402(v)) [Non-SRC, Non-EGC, Non-FPI only]**

The PvP table is among the most technically complex disclosures. Verify each element:

| PvP Element                                                                                   | Required? | Present? | Complete? |
| --------------------------------------------------------------------------------------------- | --------- | -------- | --------- |
| Five years of PEO SCT total / CAP (three for first-year filers)                               | Yes       |          |           |
| Average non-PEO NEO SCT total / average CAP                                                   | Yes       |          |           |
| Company TSR (cumulative, $100 base)                                                           | Yes       |          |           |
| Peer group TSR (same peers as Form 10-K Item 201(e) performance graph, or explain difference) | Yes       |          |           |
| Net income                                                                                    | Yes       |          |           |
| Company-selected measure (CSM) — exactly one                                                  | Yes       |          |           |
| CAP footnote with all six equity adjustment components                                        | Yes       |          |           |
| Non-PEO NEO names identified for each year in footnote                                        | Yes       |          |           |
| Relationship disclosure (CAP vs. each performance measure)                                    | Yes       |          |           |
| Tabular list of 3–7 most important financial performance measures                             | Yes       |          |           |
| Inline XBRL tagging                                                                           | Yes       |          |           |

**CAP Footnote — The Six Required Equity Adjustment Components** [VERIFY against current SEC guidance]:

1. Year-end fair value of awards granted and outstanding/unvested at year-end
2. Change in year-end fair value of awards granted in prior years and outstanding/unvested
3. Fair value at vesting date of awards that vested during the year (granted in prior years)
4. Change in fair value from end of prior year to vesting date for awards vesting during year
5. Negative: fair value at end of prior year for awards forfeited/failed to vest during year
6. Dividends or earnings not otherwise reflected in the above amounts

Missing or incomplete CAP footnotes are the most common SEC comment letter deficiency.

**B4 — Clawback Policy Disclosure (Item 402(w) + Rule 10D-1)**

Verify:

- Exhibit 97 (clawback policy) filed with the Form 10-K (required by December 1, 2023)
- Policy covers all current and former executive officers
- Policy applies to excess incentive compensation without fault requirement
- Three-fiscal-year look-back period is present
- Only the four permitted exceptions are used (legal enforcement action impractical;
  home country law prohibits; de minimis amount; accounting restatement did not result
  in excess)
- Form 10-K cover page checkboxes correct (Item 402(w) interaction)
- If restatement occurred: recovery analysis disclosed or explain why no recovery required

**B5 — Say-on-Pay Disclosure (Rule 14a-21)**

Verify:

- Advisory vote on NEO compensation proposed (Rule 14a-21(a))
- Say-on-frequency vote proposed where required (Rule 14a-21(b) — every six years)
- Prior year say-on-pay vote result disclosed with specificity (% for, against, abstain)
- CD&A responsiveness discussion present (required if support below threshold)

**B6 — CEO Pay Ratio (Item 402(u)) [Non-SRC, Non-EGC only]**

Verify: Median annual total compensation of all employees identified; ratio calculation
methodology disclosed; any exemptions used (non-US employees, statistical sampling) explained.

**B7 — Perquisites and All Other Compensation**

Perquisites that in aggregate exceed $10,000 must be disclosed by category. Any single
perquisite exceeding the greater of $25,000 or 10% of aggregate perquisites must be
identified by type and amount.

High-scrutiny perquisite items: personal aircraft usage (valued at incremental cost,
not charter rate), personal security, housing/relocation, spousal travel, club
memberships, financial planning/tax preparation.

**⟁ CLARIFY** — For complex compensation structures (sign-on awards, mid-year CEO
transition, international pay components, pension plan with significant change in
actuarial value): Ask whether to model the full multi-component compensation waterfall
or focus on the most material items only.

---

#### Section C: Say-on-Pay and Compensation Governance

**Governing authority**: Rule 14a-21; Reg S-K Item 402(b)(2)(xv) (responsiveness).

**Checklist:**

| Item                                                                            | Required      | Present | Notes |
| ------------------------------------------------------------------------------- | ------------- | ------- | ----- |
| Prior year say-on-pay vote result disclosed (% for / against / abstain)         | Yes           |         |       |
| If <70% support: substantive engagement disclosure                              | Yes           |         |       |
| If <50% support: full responsiveness package (engagement, changes made)         | Yes           |         |       |
| Compensation changes made in response to low support disclosed                  | If <70%       |         |       |
| Golden parachute advisory vote (Rule 14a-21(c)) where required (merger proxies) | If applicable |         |       |

**Classification guide:**

- **DEFICIENT**: Prior year say-on-pay result not disclosed; no responsiveness discussion
  after <50% support
- **PARTIAL**: Result disclosed but management response vague or generic
- **COMPLIANT**: Full disclosure with specific engagement actions and compensation changes

---

#### Section D: Related Party Transactions

**Governing authority**: Reg S-K Items 404(a)–(b).

**Threshold**: Any transaction since beginning of last fiscal year where a "related
person" (director, nominee, executive officer, 5%+ shareholder, or immediate family
member of any of the foregoing) had a direct or indirect material interest, and the
aggregate amount exceeds **$120,000**.

**Checklist:**

| Item                                                                                                           | Authority   | Compliant? |
| -------------------------------------------------------------------------------------------------------------- | ----------- | ---------- |
| All transactions >$120K disclosed with: related person name, relationship, interest description, dollar amount | Item 404(a) |            |
| Written review/approval policy described or Form 8-K explanation for absence                                   | Item 404(b) |            |
| Any director independence determination that conflicts with a disclosed Item 404 transaction flagged           | Item 407(a) |            |
| Loans to executive officers confirmed absent (Sarbanes-Oxley Section 402 prohibits)                            | SOX §402    |            |
| Family member employment arrangements disclosed (beyond $120K threshold)                                       | Item 404(a) |            |

**Common SEC enforcement patterns** (Skechers 2024; Express 2024):

- Family member employment: spouse, child, sibling, in-law employed by the company or
  subsidiary — payments in aggregate often exceed $120K but are not disclosed
- Personal aircraft and other perquisites with related-party characteristics
- Consulting arrangements with director-affiliated entities

**⟁ CLARIFY** — If the proxy states "no related party transactions" but director bios
reveal family-member employment, vendor relationships, or consulting arrangements,
ask the user whether to escalate this to RED (potential omission) or flag for counsel
review with a PARTIAL classification.

---

#### Section E: Shareholder Proposals

**Governing authority**: Exchange Act Rule 14a-8.

**For each proposal in the proxy:**

| Item                                                                  | Compliant? |
| --------------------------------------------------------------------- | ---------- |
| Proposal text included without omission                               |            |
| Proponent eligibility criteria met (ownership threshold and duration) |            |
| Board recommendation (for/against/abstain) stated                     |            |
| Board rationale substantively explained (not boilerplate)             |            |
| Excluded proposals: basis for exclusion clear and legally supported   |            |

**Critical 2025–2026 season note**: As of November 2025, the SEC Division of Corporation
Finance will not respond to Rule 14a-8 no-action requests except under Rule 14a-8(i)(1)
(improper under state law). Companies bear full legal risk for exclusion decisions made
without SEC staff concurrence. [VERIFY current SEC guidance at time of analysis.]

**Staff Legal Bulletin 14M (February 2025)**: Rescinded SLB 14L and reinstated broader
grounds for excluding ESG/social proposals under Rule 14a-8(i)(5) (economic significance)
and Rule 14a-8(i)(7) (ordinary business). [VERIFY current SLB at time of analysis.]

**Classification guide:**

- **DEFICIENT**: Properly submitted proposal excluded without adequate basis; board
  statement mischaracterizes the proposal; proponent identity omitted
- **PARTIAL**: Proposal included but board rationale is boilerplate
- **COMPLIANT**: Full proposal disclosure with substantive board analysis

---

#### Section F: Audit Committee and Auditor Disclosures

**Governing authority**: Schedule 14A Items 9(e)(1)–(e)(4); Reg S-K Item 407(d);
SOX Section 407; Exchange Act Rule 10A-3.

**Audit Committee Report checklist:**

| Requirement                                                                       | Present? |
| --------------------------------------------------------------------------------- | -------- |
| Committee reviewed and discussed audited financial statements with management     |          |
| Committee discussed with auditor matters required by PCAOB AS 1301                |          |
| Committee received PCAOB Rule 3526 independence letter and discussed with auditor |          |
| Committee recommended board include audited statements in Form 10-K               |          |

**Auditor fee disclosure (four mandatory categories):**

| Category           | Amount Disclosed | Pre-Approval Status |
| ------------------ | ---------------- | ------------------- |
| Audit Fees         |                  |                     |
| Audit-Related Fees |                  |                     |
| Tax Fees           |                  |                     |
| All Other Fees     |                  |                     |

**Key flags:**

- Non-audit fees (Tax + All Other) approaching or exceeding audit fees — triggers ISS
  scrutiny and potential negative auditor ratification recommendation
- Tax planning fees (as opposed to tax compliance) — potential independence concern [VERIFY]
- No pre-approval policy described or de minimis exception invoked without explanation
- Auditor tenure exceeding 20 years without rotation discussion
- Audit committee member who does not meet Rule 10A-3 independence standards

---

#### Section G: Voting Standards and Meeting Mechanics

**Governing authority**: Regulation 14A generally; Rule 14a-19 (universal proxy);
state corporate law (meeting mechanics).

**Checklist:**

| Item                                                                                  | Present? | Classification |
| ------------------------------------------------------------------------------------- | -------- | -------------- |
| Voting standard for each matter clearly stated (majority vs. plurality for directors) |          |                |
| Director resignation policy disclosed alongside majority voting standard              |          |                |
| Broker non-vote treatment explained for each proposal                                 |          |                |
| Quorum requirements stated                                                            |          |                |
| Virtual meeting: access/participation/Q&A procedures disclosed                        |          |                |
| Universal proxy compliance disclosed (if contested election)                          |          |                |
| Record date and share count as of record date disclosed                               |          |                |

**Governance concern flags:**

- Plurality voting in uncontested director elections at large-cap company (best practice
  is majority voting with resignation policy)
- Voting standard description internally inconsistent (proxy says "majority" but describes
  a plurality mechanism)
- Virtual meeting disclosure absent or vague (no Q&A procedures, no technical support info)
- Advance notice bylaw requirements materially more restrictive than Rule 14a-19 or
  Rule 14a-8 standard timelines

---

### Step 7: Pay-Versus-Performance Scenario Modeling

**[Applicable when compensation review is in scope and sufficient data is available]**

Model three scenarios to contextualize CEO/PEO compensation against performance:

**Scenario 1 — Target Achievement**

- Assume 100% attainment of annual bonus targets + target LTI vesting
- Calculate: Total target compensation = base salary + target bonus + target LTI grant value
- Identify pay mix: % fixed (salary) vs. % variable (bonus + LTI)
- Compare to prior year total target compensation (year-over-year change %)

**Scenario 2 — Peer-50th-Percentile Benchmark**

- Using the disclosed peer group (or user-provided alternative):
  - Identify 50th percentile total direct compensation
  - Calculate: CEO pay vs. peer 50th percentile ($X above/below, as % of peer median)
  - Identify whether CEO pay is positioned above, at, or below market median
  - Note: a pay positioning above 75th percentile without commensurate performance
    warrants heightened disclosure scrutiny

**Scenario 3 — Peer-75th-Percentile Benchmark**

- Calculate: CEO pay vs. peer 75th percentile
- What performance level would be required to justify top-quartile pay?
- Does disclosed performance (TSR, net income, CSM) support top-quartile positioning?

**PvP Table Cross-Check**:

- Does disclosed Compensation Actually Paid (CAP) align directionally with TSR and
  company-selected measure (CSM) performance?
- Material misalignment between CAP and performance without narrative explanation
  is a DEFICIENT finding (Reg S-K Item 402(v)(5) relationship disclosure gap)

---

### Step 8: Self-Interrogation on DEFICIENT Findings

For every finding classified as **DEFICIENT**, apply this 3-pass self-interrogation
before finalizing. The goal is to prevent over-classification and ensure every DEFICIENT
label is defensible to a securities attorney or SEC staff reviewer.

**Pass 1 — Disclosure Requirement Chain Integrity**

- Does the DEFICIENT classification follow logically from a specific, current SEC
  Regulation S-K Item, Schedule 14A requirement, or exchange listing standard?
- Would SEC staff in a comment letter actually flag this omission?
- Is there a safe harbor, exemption, or smaller reporting company carve-out that
  applies to this filer?

**Pass 2 — Completeness**

- Have all relevant SEC Items and listing standards been considered?
- Have recent SEC Staff comment letter patterns, CDIs, and proxy advisory guidelines
  been incorporated?
- Are there rule amendments or new guidance (PvP, clawback, cybersecurity) that change
  the applicability of this requirement for this fiscal year?

**Pass 3 — Challenge**

- What is the strongest argument that this disclosure level is actually adequate?
- Under what regulatory interpretation or market standard could a company reasonably
  omit this disclosure?
- Is the DEFICIENT classification proportionate, or should this be PARTIAL with a
  recommendation to enhance?

**If any pass reveals a weakness**: revise classification before delivery. Mark in audit
trail: `self_interrogation: PASS` or `self_interrogation: REVISED`.

---

### Step 9: Dual-Perspective Summary

For every DEFICIENT or PARTIAL finding in the report, apply dual-perspective framing:

**Investor / Governance Advocate View:**

- Why does this disclosure gap matter for fiduciary decision-making?
- How would ISS or Glass Lewis view this gap when making director election or say-on-pay
  vote recommendations?
- Does it trigger a negative recommendation or simply reduce confidence?
- What governance risk (misalignment, entrenchment, conflicts) does the gap signal?

**Management / Compliance View:**

- Why might management view the current disclosure as adequate?
- What competitive sensitivity, legal privilege, or confidentiality argument applies?
- What is the market standard — are peer companies providing similar or more detailed
  disclosure?
- Is there a cost-benefit argument for limiting disclosure specificity?

---

### Step 10: Quality Verification

Before delivering the output, run all quality checks silently:

1. **Citation Quality Gates** (5 gates — see Quality Frameworks section)
2. **Self-Interrogation** on all DEFICIENT findings (3-pass — see Step 8)
3. **Confidence Scoring** for every material finding
4. **Completeness check**: Confirm all seven sections (A–G) have been analyzed or
   the scope limitation explicitly noted
5. **Glass Box Audit Trail**: Populate all fields before delivery (see template below)

---

## Disclosure Deficiency Framework

### Deficiency Type Classification

Classify every finding by its disclosure gap _type_ before assigning severity:

| Type                   | Definition                                                          | Example                                                                         |
| ---------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **OMISSION**           | Disclosure required by SEC rule but entirely absent                 | No PvP table for an accelerated filer for fiscal year ending after Dec 16, 2022 |
| **INCOMPLETE**         | Disclosure present but lacks required specificity or data points    | CAP footnote present but missing three of the six equity adjustment components  |
| **MISCHARACTERIZED**   | Disclosure present but materially misleading or factually incorrect | Director with consulting agreement described as "independent"                   |
| **QUANTIFICATION GAP** | Disclosure present but key amounts or metrics absent                | CD&A describes bonus but omits target amounts or payout thresholds              |
| **COMPARATIVE GAP**    | Disclosure present but lacks required comparisons or benchmarks     | PvP table present but does not describe relationship between CAP and net income |
| **TRANSPARENCY GAP**   | Disclosure present but rationale or methodology unexplained         | Peer group listed but no explanation of selection criteria                      |

### Severity Classification

| Severity      | Definition                                                                                                                                                                                                         | Investor Impact                            | Typical Action                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------ | ------------------------------------------------------------------------- |
| **DEFICIENT** | Disclosure required by SEC rule or listing standard is materially absent, incomplete, or misleading. Investor cannot form a fully informed decision. May constitute a Rule 14a-9 violation or trigger SEC comment. | High: vote decision impaired               | Flag immediately; recommend counsel review; include in remediation Tier 1 |
| **PARTIAL**   | Disclosure is present but has material gaps reducing quality below SEC guidance or proxy advisory expectations. Investor can form a decision but with reduced confidence.                                          | Moderate: decision possible but incomplete | Recommend enhancement before next filing; include in remediation Tier 2   |
| **COMPLIANT** | Disclosure meets SEC requirements and proxy advisory expectations. No material gaps identified.                                                                                                                    | Low: no action required                    | Note as strength; no remediation required                                 |

### Confidence Scoring

Assign a confidence level to every DEFICIENT or PARTIAL finding:

| Level        | Range     | Meaning                                                       | Output Format                                       |
| ------------ | --------- | ------------------------------------------------------------- | --------------------------------------------------- |
| **DEFINITE** | 0.95–1.0  | Explicit SEC rule requirement; clear, unambiguous omission    | State without qualification                         |
| **HIGH**     | 0.80–0.94 | Strong regulatory basis; minor interpretive questions remain  | State with brief caveat                             |
| **PROBABLE** | 0.60–0.79 | Solid basis but reasonable alternative interpretation exists  | State with explicit reasoning and contra-indicators |
| **POSSIBLE** | 0.40–0.59 | Deficiency claim is debatable; strong counter-argument exists | Flag for counsel review; present both sides         |
| **UNLIKELY** | 0.0–0.39  | Deficiency claim is weak; likely a permissible approach       | Do not assert; note for completeness only           |

---

## Prioritization Framework

Organize all findings into three remediation tiers:

### Tier 1 — Must Address (Governance and Legal Risk)

Criteria: DEFICIENT classification + DEFINITE or HIGH confidence. These are items where:

- A specific SEC rule or listing standard is materially violated
- SEC staff would likely comment in a review
- ISS or Glass Lewis may issue a negative vote recommendation as a result
- A Rule 14a-9 (anti-fraud) argument is plausible

Examples: Missing PvP table; no clawback policy; undisclosed related-party transaction
exceeding $120K; director independence misrepresented; no audit committee financial
expert.

### Tier 2 — Should Address (Investor Confidence and Engagement Risk)

Criteria: PARTIAL classification + DEFINITE or HIGH confidence, OR DEFICIENT + PROBABLE
confidence. These are items where:

- Disclosure exists but is materially below SEC guidance expectations or market practice
- ISS/Glass Lewis may view the disclosure unfavorably in a say-on-pay or director election
  context without triggering an automatic negative recommendation
- Institutional investor engagement is likely if the gap persists

Examples: CD&A without responsiveness discussion after 75% say-on-pay; peer group
unexplained; perquisites disclosed in aggregate without itemization; PvP relationship
narrative is boilerplate.

### Tier 3 — Nice to Have (Transparency Enhancement)

Criteria: PARTIAL + PROBABLE or lower confidence, or best-practice gaps not required by
rule. These are items where:

- Current disclosure is legally adequate but below leading practice
- Enhancement would improve investor confidence and reduce engagement friction
- Proxy advisory firms may note the gap in their analysis without a voting impact

Examples: No board skills matrix (not SEC-required); audit committee financial expert
bio lacks depth; diversity disclosure absent after Nasdaq rule vacatur (now voluntary);
shareholder proposal board rationale is thin but not misleading.

---

## Quality Frameworks

### Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise
before delivery:

| Gate           | Rule                                                                                                                                   | Fail Action                                              |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every DEFICIENT/PARTIAL claim cites a specific SEC Item, Rule, or listing standard                                                     | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations use consistent format (e.g., "Reg S-K Item 402(v)" not "Item 402" or "the PvP rule")                                     | Fix format                                               |
| **Currency**   | Every cited requirement checked for amendments, CDIs, or rule changes effective for the filing year                                    | Flag "[CHECK CURRENCY — rule may have been amended]"     |
| **Domain**     | Analysis stays within US federal securities law and exchange standards; no assumptions from non-authoritative sources without flagging | Remove or attribute non-authoritative source clearly     |
| **Confidence** | Uncertainty explicitly stated; no finding presented with more certainty than the evidence supports                                     | Add confidence qualifier                                 |

### Self-Interrogation for DEFICIENT Findings

See Step 8 — applies to every DEFICIENT classification. Do not deliver a DEFICIENT
finding that has not passed all three self-interrogation passes.

### Confidence Scoring

See Disclosure Deficiency Framework above. Every material finding must carry a
confidence score. Do not omit confidence scoring from the output template.

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

Use legalcode-mcp in Step 4 to verify:

- Current text of Reg S-K Items 401, 402, 404, 407 (including any amendments)
- Current Schedule 14A Items 1–21 text
- Rules 14a-8, 14a-19, 14a-21 current text
- PCAOB AS 1301 and Rule 3526 (audit committee communication requirements)
- Recent SEC staff comment letter summaries on proxy disclosures

Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail. This
is the highest reliability source for regulatory text; prefer it over memory for any
citation appearing in a DEFICIENT finding.

### Without legalcode-mcp (Graceful Degradation)

Proceed using the framework in this skill with general SEC Reg S-K knowledge. Mandatory
degradation steps:

1. Mark every regulatory citation with [VERIFY]
2. Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
3. Recommend the user or counsel verify all Tier 1 regulatory citations against
   current SEC.gov source text before acting on findings
4. For PvP analysis specifically: confirm the current CAP calculation methodology
   against the most recent SEC releases and CDIs, as this area has seen active
   staff interpretation [VERIFY]

---

## Glass Box Audit Trail

Every proxy statement analysis output must conclude with a fully populated Glass Box
YAML block. Do not deliver the output without this section.

```yaml
glass_box:
  skill_name: "legalcode-proxy-statement-analysis"
  topic: "DEF 14A Proxy Statement Disclosure Analysis"

  # Company and filing context
  company_name: "[Company name]"
  company_ticker: "[Ticker]"
  cik: "[SEC CIK number]"
  fiscal_year_end: "[YYYY-MM-DD]"
  proxy_filed: "[YYYY-MM-DD]"
  annual_meeting_date: "[YYYY-MM-DD]"
  proxy_type: "[DEF 14A / DEF 14A/A amendment]"
  stock_exchange: "[NYSE / Nasdaq / Other]"

  # Filer classification
  filer_type: "[Large accelerated / Accelerated / Non-accelerated / SRC / EGC]"
  cd_a_required: "[Yes / No — SRC/EGC exempt]"
  pvp_table_required: "[Yes / No — SRC/EGC/FPI exempt; fiscal year end check]"
  clawback_required: "[Yes / No — listed company, post Dec 1 2023]"
  ceo_pay_ratio_required: "[Yes / No — SRC/EGC exempt]"

  # Board and NEO landscape
  named_executive_officers: "[N] NEOs — [CEO name] | [CFO name] | [others]"
  board_size: "[N] directors | [N] independent | committees: [list]"
  auditor: "[Firm name] | Tenure: [N] years"
  shareholder_proposals: "[N] included | [N] excluded"

  # Analysis parameters
  analysis_date: "[YYYY-MM-DD]"
  primary_perspective: "[Institutional Investor / Activist / Management / Proxy Advisory / Counsel]"
  scope: "[Full / Compensation focus / Board governance / Related party / Shareholder proposals]"
  prior_year_comparison: "[Yes — delta analysis performed / No — baseline only]"
  prior_say_on_pay_outcome: "[% For | % Against | Abstentions]"

  # Standards applied
  baseline_applied: "SEC Regulation S-K [Items 401, 402, 404, 407] + Schedule 14A"
  exchange_standards: "[NYSE Rule 303A / Nasdaq Rule 5605 series]"
  proxy_advisory_guidelines: "[ISS US Benchmark Policy YYYY / Glass Lewis US Benchmark Policy YYYY]"
  legalcode_mcp: "[Connected — citations marked VERIFIED / Not connected — citations marked VERIFY]"
  research_reference_file: "[/tmp/proxy-statement-authority.md / Not created]"

  # Finding summary
  total_findings: "[N]"
  deficient_count: "[N] DEFICIENT findings"
  partial_count: "[N] PARTIAL findings"
  compliant_count: "[N] COMPLIANT items"

  # Deficiency type breakdown
  omissions: "[N]"
  incomplete_disclosures: "[N]"
  mischaracterized: "[N]"
  quantification_gaps: "[N]"
  comparative_gaps: "[N]"
  transparency_gaps: "[N]"

  # Tier breakdown
  tier_1_must_address: "[N] findings"
  tier_2_should_address: "[N] findings"
  tier_3_nice_to_have: "[N] findings"

  # Top material findings
  most_material_findings:
    - "[Finding 1 — Type — Severity — Investor impact summary]"
    - "[Finding 2]"
    - "[Finding 3]"

  # Compensation analysis (if in scope)
  pvp_table_reviewed: "[Yes / No / Not applicable]"
  cap_footnote_complete: "[Yes / No / Partially — [missing components]]"
  say_on_pay_risk: "[LOW / MODERATE / HIGH] — [rationale]"
  clawback_policy_filed: "[Yes — Exhibit 97 filed / No — flag for Tier 1]"
  pay_scenario_modeling: "[Performed — 3 scenarios / Not applicable]"

  # Quality frameworks applied
  citation_quality_gates: "[All 5 PASSED / Gate [X] flagged and revised]"
  self_interrogation_applied: "[Applied to [N] DEFICIENT findings / Not required]"
  self_interrogation_revisions: "[N] findings revised from DEFICIENT to PARTIAL after Pass 3]"
  dual_perspective_applied: "[Comprehensively / To key findings only]"
  confidence_scoring: "[All material findings scored]"

  # Limitations
  scope_limitations:
    - "Analysis based on proxy statement as filed on [date] — later amendments not reviewed"
    - "Proxy advisory guidelines current as of [date] — verify annual updates before relying"
    - "State law meeting mechanics flagged but not fully analyzed — state counsel review recommended"
    - "[Any other scope limitations relevant to this filing]"
  jurisdictional_note: "US domestic issuer analysis — not applicable to FPIs without modification"
  data_cutoff: "[YYYY-MM-DD]"

  # Reviewer guidance
  reviewer: "AI-assisted — requires review by qualified securities attorney and governance professional"
  priority_review_items: "[List any Tier 1 findings that require immediate counsel attention]"
```

---

## Anti-Patterns

What NOT to do when conducting proxy statement disclosure analysis:

1. **Applying accelerated-filer requirements to SRCs or EGCs without first confirming
   filer status.** CD&A, PvP table, and CEO pay ratio are not required for smaller
   reporting companies and emerging growth companies. Flagging their absence as a
   DEFICIENT finding creates false positives and destroys analytical credibility.

2. **Treating the independence checklist as complete without reviewing the related-party
   transaction section.** A director may pass the independence checklist in the board
   section while a disclosed $250K consulting arrangement appears in Item 404 — creating
   a direct contradiction that constitutes a MISCHARACTERIZED finding more serious than
   either gap alone.

3. **Accepting "competitively sensitive" as a sufficient explanation for withholding
   all performance targets.** SEC Staff has repeatedly flagged this. The CD&A must
   explain, with specificity, how difficult it would be to achieve withheld targets.
   A statement that goals are "challenging" or "stretch" is insufficient without
   qualitative context (e.g., industry growth rates, macro headwinds, historical
   achievement frequency).

4. **Using the PvP peer group interchangeably with the CD&A compensation peer group
   without checking for consistency.** The PvP table requires TSR comparison to the
   same peer group used in the Form 10-K Item 201(e) performance graph (or disclose
   and explain the difference). Silently assuming they are the same when they differ
   is one of the most common SEC comment triggers.

5. **Classifying a missing diversity matrix as DEFICIENT after December 11, 2024.**
   The Fifth Circuit vacated Nasdaq's board diversity matrix requirement. Companies
   are no longer required to publish the Nasdaq-format diversity matrix. Classify
   absence of voluntary diversity disclosure as PARTIAL (best practice gap) at most,
   not DEFICIENT. [VERIFY current status at time of analysis.]

6. **Over-relying on prior year say-on-pay support as the primary compensation quality
   indicator.** A company with 85% say-on-pay support may have material disclosure
   deficiencies that institutional shareholders have not yet focused on. Use say-on-pay
   history as one data point, not the primary indicator of disclosure quality.

7. **Missing the compounding perquisite problem.** Each individual perquisite may fall
   below the itemization threshold in a given year, but a pattern of executive benefits
   (security, housing, aircraft, financial planning, spouse travel) that together
   approach $100K+ may indicate systematic underdisclosure. Always calculate aggregate
   perquisite value and confirm the total triggers proper disclosure.

8. **Treating the clawback policy as adequate based on its existence alone without
   reviewing Exhibit 97 substance.** Clawback policies that exclude time-vesting equity
   awards, apply only to current officers (not former), or contain improper carve-outs
   beyond the four permitted exceptions violate Rule 10D-1. The checkbox on the Form
   10-K cover page does not confirm policy adequacy.

9. **Classifying a shareholder proposal exclusion as COMPLIANT without reviewing the
   exclusion basis.** Post-November 2025, companies excluding proposals without SEC
   no-action concurrence bear the full legal risk of that decision. A company that
   excluded a proposal on Rule 14a-8(i)(7) (ordinary business) grounds relying on
   pre-SLB 14M interpretations may have excluded a valid proposal. Review the stated
   basis against current SLB and CDI guidance.

10. **Accepting "board oversight of risk" boilerplate without checking for cybersecurity
    governance disclosure.** Following the December 2023 cybersecurity disclosure rule
    (Reg S-K Item 106), proxy statements (via Form 10-K) must include board-level
    cybersecurity governance disclosure. Generic "the board oversees all risks"
    language without cybersecurity specificity is now a PARTIAL finding at minimum.

11. **Presenting say-on-pay risk assessment without checking the actual PvP relationship
    disclosure.** A company with strong TSR but CAP that significantly lags TSR (due
    to underwater equity) may appear to have misaligned pay without the relationship
    disclosure. Always read the CAP relationship narrative before concluding on pay
    alignment.

12. **Missing the universal proxy compliance check for any election involving a dissident
    slate.** Rule 14a-19 (effective August 31, 2022) requires universal proxy cards for
    all contested director elections. Failure to comply with notice timelines (50-day
    advance notice of nominees) or to include all nominees from all parties on a single
    card is a serious procedural deficiency.

13. **Modeling pay-versus-performance using SCT totals rather than CAP.** The PvP table
    specifically defines Compensation Actually Paid as an adjusted figure that marks
    equity to market value — it is structurally different from SCT totals, which use
    grant-date fair value. Using SCT totals in PvP analysis produces a materially
    different (and incorrect) picture of realized pay alignment.

14. **Not tracing the audit fee pattern over multiple years.** A single year where
    non-audit fees approach audit fees may be explainable (major acquisition, one-time
    tax restructuring). A multi-year pattern where Tax Fees consistently exceed 50% of
    Audit Fees is a systematic auditor independence concern that a single-year analysis
    misses.

15. **Treating the Item 404(b) written policy as a box-check without reviewing whether
    it covers all required relationships.** Written review policies that apply only to
    "director and officer" transactions may miss 5%-shareholder transactions or
    immediate family member relationships. Review the policy scope against the full
    Item 404(a) definition of "related persons."

16. **Applying ISS or Glass Lewis voting guidelines as mandatory legal requirements.**
    Proxy advisory guidelines create investor expectations and voting risk — they do
    not have the force of law. A compensation structure that triggers an ISS negative
    recommendation is not automatically legally deficient. Distinguish between
    regulatory DEFICIENT findings and market/governance PARTIAL findings in the output.

17. **Skipping the say-on-frequency analysis for companies in their sixth annual
    meeting cycle.** Rule 14a-21(b) requires a say-on-frequency vote every six years.
    Companies that omit this vote when required create a serious proxy deficiency.
    Check whether the company last held a say-on-frequency vote and whether one is
    required at the current meeting.

18. **Ignoring the interaction between golden parachute disclosures and merger proxy
    requirements.** Rule 14a-21(c) requires an advisory vote on golden parachute
    arrangements in connection with certain acquisitions. If the proxy relates to a
    merger or acquisition, confirm whether a separate golden parachute advisory vote
    is required alongside the say-on-pay vote.

19. **Presenting dual-perspective framing as a perfunctory add-on rather than a
    genuine analytical lens.** The investor view and management view must contain
    substantive, distinct arguments — not paraphrases of each other. If the management
    view cannot articulate a legitimate defense of the disclosure level, that itself
    is a signal that the DEFICIENT classification is correct.

20. **Omitting the remediation roadmap under time pressure.** The remediation roadmap
    is the most actionable deliverable for management teams preparing next year's proxy.
    A deficiency finding without a specific recommended disclosure addition or
    structural change is incomplete analysis. Every DEFICIENT and PARTIAL finding
    must map to a specific Tier 1, 2, or 3 remediation action.

---

## Writing Standards

Apply these standards before delivering any output:

1. **Lead with the finding, not the methodology.** Write: "The CD&A omits any
   discussion of how the board responded to the 2024 say-on-pay vote (64% support)
   — this is a DEFICIENT finding under Reg S-K Item 402(b)(2)(xv)." Not: "In
   reviewing Item B5 of our checklist, we noted that..."

2. **Cite the rule, not a paraphrase.** Name the specific Regulation S-K Item, Rule,
   or Schedule 14A requirement for every DEFICIENT finding. Generic references
   to "SEC requirements" without a specific citation reduce the analytical value.

3. **Quantify wherever possible.** "Non-audit fees ($2.1M) exceeded audit fees ($1.8M)
   by 17%" is stronger than "non-audit fees were high." "CEO pay is at the 87th
   percentile of disclosed peers" is stronger than "CEO pay appears above market."

4. **Calibrate hedging to confidence.** DEFINITE findings use indicative language
   ("this is DEFICIENT"). PROBABLE findings use hedged language ("this appears
   PARTIAL"). POSSIBLE findings use conditional language ("this may be a concern —
   counsel review recommended").

5. **Avoid jargon without definition.** Define CD&A, CAP, CSM, NEO, PvP, SRC, EGC,
   and FPI on first use if the report audience is not exclusively securities lawyers.

6. **Separate regulatory requirements from best practice.** A finding that is DEFICIENT
   under SEC rule reads differently from a finding that is PARTIAL because it departs
   from ISS voting guidelines or leading governance practice. Keep these lanes clear.

7. **Gate the output.** Do not deliver the report until all five Citation Quality Gates
   pass and all DEFICIENT findings have passed self-interrogation. If time pressure
   prevents full review, state the limitation explicitly in the Glass Box.

---

## Output Format Template

Use this template for every proxy statement analysis deliverable:

---

```markdown
# Proxy Statement Disclosure Analysis

## [Company Name] | [Ticker] | DEF 14A Filed [Date] | Fiscal Year [YYYY]

## Analysis Date: [YYYY-MM-DD] | Perspective: [Institutional Investor / Management / etc.]

---

## Executive Summary

**Overall Disclosure Quality**: [DEFICIENT / PARTIAL / COMPLIANT — 1–2 sentences]
**Say-on-Pay Risk**: [LOW / MODERATE / HIGH]
**Filer Type**: [Large accelerated / Accelerated / SRC / EGC]
**Exchange**: [NYSE / Nasdaq]

### Top 3 Material Deficiencies

| #   | Finding         | Type              | Severity  | Tier |
| --- | --------------- | ----------------- | --------- | ---- |
| 1   | [Finding title] | [OMISSION/etc.]   | DEFICIENT | 1    |
| 2   | [Finding title] | [INCOMPLETE/etc.] | DEFICIENT | 1    |
| 3   | [Finding title] | [COMPARATIVE GAP] | PARTIAL   | 2    |

---

## Section A: Director Nominations and Board Composition

### Item A[N] — [Finding Title]

**Type**: [OMISSION / INCOMPLETE / etc.] | **Severity**: [DEFICIENT / PARTIAL / COMPLIANT]
**Confidence**: [DEFINITE / HIGH / PROBABLE / POSSIBLE]
**Authority**: [Reg S-K Item 407(a) / NYSE Rule 303A.01 / etc.]

[Detailed finding narrative — 2–4 sentences describing the gap and its regulatory basis]

**Investor / Governance Advocate View:**
[Why this matters for voting decisions; ISS/Glass Lewis impact]

**Management View:**
[Legitimate defense or competitive rationale; market standard comparison]

**Remediation (Tier [1/2/3]):**
[Specific language to add or structural change to make]

---

[Repeat for each section: B (Compensation), C (Say-on-Pay), D (Related Party),
E (Shareholder Proposals), F (Audit Committee), G (Voting Standards)]

---

## Pay-Versus-Performance Analysis

[If in scope]

### Target Scenario

- Base salary: $[X]
- Target annual bonus: $[X] ([Y]% of salary / [Z] metric thresholds)
- Target LTI grant value (ASC 718): $[X]
- **Total target direct compensation**: $[X]M
- Pay mix: [%] fixed / [%] variable

### Peer-50th-Percentile Benchmark

- Peer group: [N] companies (disclosed in CD&A, or user-provided)
- Peer 50th percentile total direct compensation: $[X]M
- CEO positioning: [above / at / below] median by $[X]M ([Y]%)

### Peer-75th-Percentile Benchmark

- Peer 75th percentile: $[X]M
- CEO positioning: [above / at / below] 75th percentile

### PvP Alignment Assessment

- CAP vs. TSR direction: [Aligned / Misaligned — explain]
- CAP vs. [CSM name]: [Aligned / Misaligned — explain]
- Overall pay-performance alignment: [Strong / Moderate / Weak]

---

## Say-on-Pay Risk Assessment

**Risk Level: [LOW / MODERATE / HIGH]**

| Factor                    | Assessment                                        | Notes                                   |
| ------------------------- | ------------------------------------------------- | --------------------------------------- |
| Prior say-on-pay support  | [%] for / [%] against                             | [Trend: improving / declining / stable] |
| CD&A disclosure quality   | [DEFICIENT / PARTIAL / COMPLIANT]                 |                                         |
| Pay-performance alignment | [Strong / Moderate / Weak]                        |                                         |
| Problematic pay practices | [None / Single-trigger CIC / Tax gross-up / etc.] |                                         |
| ISS quantitative PfP      | [Pass / Concern / Elevated concern]               | [Estimate only — verify with ISS]       |

**Rationale**: [3–5 sentences explaining the risk level]

**Mitigation recommendations for management:**

1. [Specific action 1]
2. [Specific action 2]

---

## Remediation Roadmap

### Tier 1 — Must Address Before Next Filing (Governance and Legal Risk)

| #   | Finding | Disclosure to Add          | Responsible Party                                  |
| --- | ------- | -------------------------- | -------------------------------------------------- |
| 1   | [Title] | [Specific language / data] | [Compensation Committee / Audit Committee / Board] |
| 2   |         |                            |                                                    |

### Tier 2 — Should Address (Investor Confidence)

| #   | Finding | Disclosure to Add          | Recommended Timing                          |
| --- | ------- | -------------------------- | ------------------------------------------- |
| 1   | [Title] | [Specific language / data] | [Next proxy / Mid-year 8-K / Annual report] |

### Tier 3 — Nice to Have (Transparency Enhancement)

| #   | Finding | Suggested Enhancement |
| --- | ------- | --------------------- |
| 1   | [Title] | [Specific suggestion] |

---

## Glass Box Audit Trail

[Fully populated YAML block — see Glass Box template above]
```

---

## Localization Notes

This skill is US-specific. For companies with international operations, note:

- **Foreign private issuers (FPIs)**: File Form 20-F; exempt from most compensation
  disclosure requirements (no CD&A, no PvP, no CEO pay ratio in the US sense). Do not
  apply this skill to FPIs without a jurisdiction-specific adaptation.
- **Multi-national pay elements**: US NEOs with international assignments may have
  foreign retirement benefits, tax equalization payments, and housing allowances that
  affect SCT "All Other Compensation" presentation. Verify incremental cost calculation
  methodology for non-US benefits.
- **Non-US employees in CEO pay ratio**: Item 402(u) permits companies to exclude
  non-US employees from the pay ratio denominator up to 5% of the workforce (de minimis
  exemption) — but must disclose the number of excluded employees.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on deep research across:
SEC Regulation 14A (Rules 14a-1 through 14b-2), Schedule 14A, SEC Regulation S-K Items
401, 402, 404, 407 (current as of March 2026), SEC enforcement actions (Skechers 2024,
Express 2024), ISS 2025 US Benchmark Policy, Glass Lewis 2025 US Benchmark Policy,
White & Case 2025 proxy season guidance, Harvard Law School Forum on Corporate
Governance, Pay Versus Performance SEC final rule (August 2022), Rule 10D-1 clawback
final rule (November 2022), Rule 14a-19 universal proxy (effective August 2022), Staff
Legal Bulletin 14M (February 2025), and SEC Division no-action suspension announcement
(November 2025). All regulatory citations should be verified against current SEC.gov
source text before relying on them. Structural patterns adapted from
`legalcode-contract-review` (Legalcode gold standard) and `legalcode-term-sheet-analysis`.
