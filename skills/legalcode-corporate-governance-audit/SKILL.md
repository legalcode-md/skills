---
name: legalcode-corporate-governance-audit
description: Audit corporate governance frameworks against US SOX Sections 302 and 404, UK Corporate Governance
  Code 2024, EU Shareholder Rights Directive II (2017/828/EU), and German Corporate Governance Code (DCGK).
  Covers board composition and independence, committee structure (audit, compensation, nomination), executive
  compensation disclosure and clawback, internal controls over financial reporting (ICFR), risk oversight,
  related-party transaction governance, and shareholder engagement. Use when preparing for SEC examination,
  shareholder activism, IPO governance readiness, annual proxy season, post-M&A board integration, or
  routine governance health checks. Applies to listed companies subject to US SEC rules, UK FCA/LSE premium
  listings, EU-listed entities under SRD II, and German AktG companies. Produces compliance-classified
  findings with remediation roadmaps, board mandate templates, and a Glass Box audit trail. Jurisdiction-agnostic
  core with US/UK/EU/DE specific modules.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Corporate Governance Audit

> **Disclaimer**: This skill provides a framework for AI-assisted corporate governance
> assessment. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional licensed in the relevant jurisdiction before use. Laws and
> governance codes change; verify current applicability before relying on any provision
> described here. Statutory references, listing rule provisions, and code provisions cited
> from training data carry hallucination risk — verify against authoritative sources before
> relying on them. Corporate governance assessment requires access to current board
> materials, committee charters, meeting minutes, and disclosure documents not available
> to this skill unless provided by the user.

---

## Purpose and Scope

This skill audits corporate governance structures and practices against applicable
regulatory requirements and leading governance codes. It produces classified findings,
prioritized remediation recommendations, and board-level deliverables.

**Covers:**

- Board composition, independence, and diversity analysis
- Committee structure and effectiveness (audit, compensation, nomination/governance)
- Executive compensation governance (pay structure, say-on-pay compliance, clawback)
- Internal controls over financial reporting (ICFR) — SOX §302 and §404 compliance
- Risk oversight and enterprise risk management governance
- Related-party transaction approval and disclosure controls
- Shareholder engagement, say-on-pay, and proxy governance
- Governance framework applicability matrix (US/UK/EU/DE regimes)
- Board process, information architecture, and evaluation cycles
- Disclosure controls and procedures (SOX §302 certifications)

**Does not:**

- Provide legal advice or replace qualified board counsel
- Substitute for an independent board evaluation or governance advisory engagement
- Apply detailed analysis to micro-cap or private companies (framework is calibrated for
  listed companies subject to SOX, UK CGC, SRD II, or DCGK)
- Assess financial statement accuracy (ICFR structure reviewed; financials not audited)
- Constitute an independent audit of ICFR under PCAOB AS 2201

**Output modes:**

- **Governance Audit** — comprehensive assessment of all governance domains
- **Board Readiness** — executive-facing assessment for investor/proxy season preparation
- **Regulatory Response** — targeted analysis for SEC examination or shareholder challenge
- **Pre-IPO / Post-M&A** — governance structure buildout from scratch
- **Transaction Screening** — governance risk review of specific transaction (director
  appointment, related-party deal, equity grant)

---

## Jurisdiction and Governing Law

This skill is multi-jurisdictional. Each governance regime applies to specific entity types:

| Regime                                  | Applies to                                                  | Mandatory vs. Best Practice                           |
| --------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------- |
| **SOX §302**                            | US-listed public companies (Exchange Act reporting issuers) | Mandatory — SEC Rules 13a-15, 15d-15                  |
| **SOX §404(a)**                         | All Exchange Act reporting issuers                          | Mandatory — management assessment required            |
| **SOX §404(b)**                         | Accelerated and large accelerated filers                    | Mandatory — auditor attestation required; SRCs exempt |
| **NYSE/NASDAQ listing rules**           | Companies listed on NYSE or NASDAQ                          | Mandatory — exchange governance requirements          |
| **UK Corporate Governance Code 2024**   | Premium-listed UK companies (effective Jan 2025)            | Comply-or-explain                                     |
| **UK Companies Act 2006**               | All UK incorporated companies                               | Mandatory (relevant parts)                            |
| **SRD II (2017/828/EU)**                | EU-listed companies; institutional investors/proxy advisors | Mandatory — transposed in member states               |
| **DCGK 2022**                           | German stock-listed companies                               | Comply-or-explain (Entsprechenserklärung — §161 AktG) |
| **AktG (German Stock Corporation Act)** | All German Aktiengesellschaft                               | Mandatory                                             |
| **COSO 2013 / COSO ERM 2017**           | Best practice (referenced by SEC, PCAOB, PCAOB AS 2201)     | Best practice — de facto standard for ICFR            |
| **SEC Climate/Proxy Rules**             | US-listed public companies                                  | [VERIFY — recent rule amendments]                     |

[JURISDICTION-SPECIFIC] When localizing for a specific jurisdiction:

- **US**: Identify accelerated filer vs. SRC/EGC status for SOX §404(b) applicability;
  confirm exchange listing (NYSE vs. NASDAQ listing standards differ); check Delaware
  fiduciary duty baseline
- **UK**: Confirm premium vs. standard listing category; apply FRC UK CGC 2024 (effective
  January 2025); check Companies Act 2006 Part 8 (directors' report) obligations
- **EU/Germany**: Confirm whether DCGK or SRD II (national transposition) applies; identify
  codetermination threshold (≥500 employees: one-third participation; ≥2000: full
  Mitbestimmung); check member state-specific transposition of SRD II

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points marked with **⟁ CLARIFY**.
Rather than assuming the user's context, the workflow pauses and asks when:

- The answer would change which regulatory regime(s) apply
- Operating mode selection affects depth and output format
- Multiple valid governance approaches exist and organizational context is needed
- Business context is needed to classify a governance gap correctly

Present structured options wherever marked with ⟁ CLARIFY. If the user has already provided
the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept Input and Determine Operating Mode

Accept governance materials in any of these formats:

- **Governance documents**: Board charter, committee charters, governance guidelines,
  codes of conduct, annual proxy statement (DEF 14A), annual report, board evaluations,
  compensation plan documents
- **Regulatory filings**: SOX certifications (Forms 10-K, 10-Q certifications), ICFR
  assessment disclosures, management discussion of ICFR effectiveness
- **URL**: Link to publicly available proxy filings, annual report, governance webpage
- **Verbal description**: Description of current governance structure (triggers Board Readiness
  or Pre-IPO mode)

**⟁ CLARIFY** — Operating mode selection:

1. **Operating Mode** — which best describes the engagement?
   - **A. Governance Audit** — comprehensive assessment of all governance domains against
     applicable codes and regulations; produces full compliance matrix and remediation roadmap
   - **B. Board Readiness** — investor-facing assessment; identifies gaps most likely to attract
     proxy advisor (ISS/Glass Lewis) scrutiny or shareholder activist pressure
   - **C. Regulatory Response** — targeted analysis in response to SEC staff comment, PCAOB
     inspection, or shareholder derivative action
   - **D. Pre-IPO or Post-M&A** — build or redesign governance framework from scratch;
     focus on establishing compliant and investor-grade structures
   - **E. Transaction Screening** — assess governance risk of a specific transaction (director
     appointment with potential conflicts, related-party deal, equity compensation grant)
   - _Why this matters_: Mode determines which governance domains to prioritize, level of
     depth per domain, output format, and whether to generate board mandate templates.

### Step 2: Gather Organizational Context

**⟁ CLARIFY** — Ask these questions. Skip any already answered by the input materials:

1. **Jurisdiction(s) in scope**:
   - Options: US (NYSE/NASDAQ listed) / UK (premium listed) / Germany (DCGK / AktG) /
     EU (SRD II member state) / Multi-jurisdiction / Private company (governance best practices only)
   - _Why this matters_: Determines which mandatory regimes apply vs. comply-or-explain.

2. **Entity profile**:
   - Options: Large accelerated filer / Accelerated filer / Smaller reporting company (SRC) /
     Emerging growth company (EGC) / Non-US filer on US exchange / Private / Other
   - _Why this matters_: SOX §404(b) auditor attestation applies only to accelerated and large
     accelerated filers. SRCs and EGCs have scaled disclosure requirements.

3. **Governance baseline**:
   - Options: Provide governance documents for analysis / Describe current governance structure /
     Governance structure unknown — assess based on public filings
   - _Why this matters_: Determines whether analysis is document-based, interview-based, or
     proxy-filing-based.

4. **Specific concerns or focus areas** (multiple selections permitted):
   - Board composition and independence / Audit committee / Compensation structure /
     ICFR / SOX certifications / Risk oversight / Related-party transactions /
     Say-on-pay / ESG governance / Director qualifications / All areas equally
   - _Why this matters_: Allows the analysis to weight the most sensitive governance areas first.

5. **Trigger event** (optional):
   - Options: Annual proxy season preparation / SEC comment letter / Activist investor pressure /
     D&O insurance renewal / M&A integration / IPO preparation / Board refreshment /
     Regulatory examination / Internal governance review / No specific trigger
   - _Why this matters_: Determines urgency tier for remediation roadmap items.

If the user provides partial context, proceed with stated assumptions. State assumptions
explicitly at the top of the analysis.

### Step 3: Map the Regulatory Framework

Determine which governance regimes apply and build the Regulatory Applicability Matrix.

#### Regime Applicability Decision Tree

**US SOX applicability:**

- Is the entity an Exchange Act reporting issuer? → Yes: SOX §302 AND §404(a) apply
- Is it an accelerated or large accelerated filer? → Yes: SOX §404(b) auditor attestation required
- Is it listed on NYSE or NASDAQ? → Yes: Exchange listing standards apply

**UK Corporate Governance Code 2024 applicability:**

- Is the entity premium-listed on the London Stock Exchange? → Yes: UK CGC 2024 applies
  (effective January 2025; replaces 2018 Code)
- Was the entity previously on the 2018 Code? → Transition review required (Provision 29
  new ICFR obligation; remuneration code updates)

**SRD II applicability:**

- Is the entity listed on an EU regulated market? → Yes: SRD II national transposition applies
- Is the entity a German AG? → AktG §§161/93/76 mandatory; DCGK Declaration of Conformity annual
- Institutional investor/proxy advisor operating in EU? → SRD II engagement policy obligations

**DCGK (German Corporate Governance Code) applicability:**

- Is the entity a German stock-listed company (börsennotierte Gesellschaft)? → Comply-or-explain
  Declaration of Conformity required annually (§161 AktG)
- Does the entity have ≥500 employees? → Drittelbeteiligungsgesetz (one-third employee
  representation on Supervisory Board) applies
- Does the entity have ≥2,000 employees? → Mitbestimmungsgesetz 1976 (full codetermination;
  equal employee representation on Supervisory Board) applies

#### Regulatory Applicability Matrix (Template)

| Regime           | Applicable | Mandatory vs. Comply-or-Explain | Highest-Penalty Provision                          | Key Enforcement Focus (2023–2025)               |
| ---------------- | ---------- | ------------------------------- | -------------------------------------------------- | ----------------------------------------------- |
| SOX §302         | [Y/N]      | Mandatory                       | Criminal: $5M / 20 years (§906 willful)            | CEO/CFO cert disclosures; ICFR design gaps      |
| SOX §404(a)      | [Y/N]      | Mandatory                       | Securities fraud overlay                           | ICFR management assessment adequacy             |
| SOX §404(b)      | [Y/N]      | Mandatory (large filers)        | PCAOB inspections → SEC referral                   | Auditor attestation; significant deficiency     |
| NYSE Listing     | [Y/N]      | Mandatory                       | Delisting risk                                     | Board independence; audit committee composition |
| NASDAQ Listing   | [Y/N]      | Mandatory                       | Delisting risk                                     | Board independence; smaller company exemptions  |
| UK CGC 2024      | [Y/N]      | Comply-or-explain               | FCA/FRC investigation; investor opposition         | Provision 29 ICFR; remuneration; independence   |
| SRD II           | [Y/N]      | Mandatory (via national law)    | Member-state civil penalties                       | Related-party transactions; say-on-pay          |
| AktG §161 / DCGK | [Y/N]      | Comply-or-explain               | Supervisory Board liability; shareholder challenge | Declaration of Conformity; two-tier governance  |

**If legalcode-mcp is connected:** Search for the entity's most recent proxy filing, Form
10-K ICFR section, or annual governance statement. Extract current compliance posture.

**If legalcode-mcp is not connected:** Mark all regulatory citations [VERIFY] and proceed
with framework analysis using governance documents provided by the user.

### Step 4: Gather Legal Authority

Use **legalcode-mcp** to build a working governance legal reference for this assessment.

**Search for:**

1. Current SEC rules on ICFR disclosure (Rules 13a-15, 15d-15; Item 308 of Regulation S-K)
2. PCAOB AS 2201 (An Audit of Internal Control Over Financial Reporting Performed in
   Conjunction with an Audit of Financial Statements) — material weakness definition
3. SEC enforcement actions involving ICFR failures, §302 certification inaccuracies,
   or governance failures (last 3 years)
4. FRC guidance on UK CGC 2024 Provision 29 (board ICFR responsibility; effective Jan 2025)
5. SRD II related-party transaction approval requirements and highest-penalty national transpositions
6. DCGK 2022 independence criteria for Supervisory Board and recent Declaration of Conformity disputes
7. ISS and Glass Lewis proxy voting guidelines (current year) — independence, say-on-pay, ICFR

Save results to `/tmp/legalcode-governance-authority.md`.

**If legalcode-mcp is not connected:**

- Proceed with documented governance frameworks below
- Mark all citations [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected — manual verification required"`

### Step 5: Domain-by-Domain Governance Assessment

Assess each of the 12 governance domains below. Apply the severity classification system
(see Section: Severity Classification System) to each domain. Use Self-Interrogation for
any domain rated GOVERNANCE-INADEQUATE or CRITICAL.

For each domain, assess:

1. **Current state** — what governance structures and practices exist?
2. **Applicable standard** — what does the applicable regime require or recommend?
3. **Gap analysis** — where does current state fall short?
4. **Severity classification** — GOVERNANCE-EFFECTIVE / ADEQUATE / DEVELOPING / INADEQUATE
5. **Remediation** — specific, prioritized action required

**⟁ CLARIFY** — For organizations with limited governance documentation:

- Ask whether to proceed with a document-based assessment (if documents provided) or
  a structural assessment (based on organizational description)
- If performing a full audit vs. prioritized spot-check, confirm scope before proceeding

---

#### Domain 1: Board Composition and Independence

**Standard:**

_US (NYSE/NASDAQ):_

- NYSE Listed Company Manual §303A.01: Majority of directors must be independent
- NYSE §303A.02: Independence test — no material relationship with company within 3 years;
  former employees 5-year cooling-off period; immediate family members of executives
- NASDAQ Rule 5605(b)(1): Majority independent; similar independence definition
- [VERIFY: current exchange rule versions]

_UK CGC 2024:_

- Provision 11: At least half of the board (excluding Chair) should be independent
  non-executive directors (INEDs)
- Provision 10: Board Chair must be independent on appointment; should not chair for more
  than 9 years from date of first appointment [VERIFY: 2024 Code provisions]
- Provision 13: Company Secretary should be a named individual responsible to the board

_DCGK 2022:_

- Recommendation C.6: Supervisory Board should have sufficient independent members to form
  the required statutory minimum committees without conflicts
- Recommendation C.7: Supervisory Board should establish independence criteria; threshold
  for "independent" typically <30% remuneration dependency or other material relationship
- [VERIFY: DCGK 2022 Recommendations C.6–C.9 and §100 AktG external criteria]

**Assess:**

- [ ] Count of independent directors (define by applicable exchange/code)
- [ ] Non-executive director majority achieved?
- [ ] Board Chair independence (UK) or lead independent director (US if CEO chairs)
- [ ] Director tenure — any overboarding risks (NYSE: ≤5 public boards; major proxy advisors: stricter)
- [ ] Diversity composition (gender, skill set, sector expertise, nationality)
- [ ] Board size appropriateness (NYSE best practice: 8–12; DCGK: Supervisory Board 6–20 members per articles)
- [ ] German Supervisory Board: codetermination composition correct per Mitbestimmungsgesetz or Drittelbeteiligungsgesetz?
- [ ] Director independence re-affirmation at each annual meeting (NYSE §303A.02(a))

---

#### Domain 2: Board Structure and Process

**Standard:**

- Board charter / terms of reference define: purpose, authority, reserved matters, quorum,
  meeting frequency
- NYSE §303A.03: Non-management directors must meet in executive session (at least annually;
  best practice: each regular meeting)
- UK CGC 2024 Provision 14: Chair should ensure adequate time for discussion; Provision 15:
  NEDs should have access to independent professional advice at company expense
- DCGK Recommendation D.1: Supervisory Board Rules of Procedure; D.2: Chairperson chairs
  Supervisory Board (elected by Supervisory Board) and coordinates with Management Board;
  D.3: Plenum meets minimum 4× per year; D.10: Supervisory Board self-evaluation annually

**Assess:**

- [ ] Written board charter exists and is current?
- [ ] Meeting frequency adequate (minimum quarterly; best practice 6–8× per year)?
- [ ] Executive sessions of non-management or independent directors held (US: required)?
- [ ] Adequate pre-meeting materials distributed (≥5 business days before meeting)?
- [ ] Board access to management and independent advisors without constraint?
- [ ] Clear reserved matters list (matters requiring full board approval, not delegated)?
- [ ] Annual board self-evaluation completed and documented?
- [ ] New director orientation program exists?
- [ ] Continuing education program for directors?
- [ ] Lead Independent Director (US, where CEO is also Chair)?

---

#### Domain 3: Audit Committee Governance

**Standard:**

_US SOX §301 (incorporated into Exchange Act §10A(m)):_

- Audit committee must be composed entirely of independent directors
- Audit committee must include at least one "financial expert" (SEC Item 407(d)(5))
- Audit committee responsible for: appointment/oversight of independent auditor;
  pre-approval of audit and non-audit services; receipt of complaints re accounting/ICFR;
  retention of independent counsel/advisors [VERIFY: 15 U.S.C. §78j-1(m)]

_NYSE §303A.07 / NASDAQ Rule 5605(c):_

- Minimum three members, all independent
- Committee charter must address: purpose, duties/responsibilities, annual self-evaluation
- NYSE: Committee must have authority to engage independent advisors

_UK CGC 2024 Provision 25:_

- Audit committee should comprise independent NEDs; at least one with recent and relevant
  financial experience; collectively competent in the sector

_DCGK Recommendation D.3:_

- Audit Committee required; Chairman cannot have been a member of the Management Board in
  the last 2 years; at least one member with expertise in financial reporting; at least one
  member with expertise in auditing [VERIFY: DCGK D.3–D.7]

**Assess:**

- [ ] All audit committee members independent?
- [ ] At least one financial expert designated (US: required; UK/DCGK: required)?
- [ ] Audit committee charter — scope and authority clearly defined?
- [ ] Auditor appointment, oversight, and rotation — committee authority confirmed?
- [ ] Pre-approval policy for non-audit services?
- [ ] Whistleblower / complaint receipt mechanism (SOX §301)?
- [ ] Regular meetings with independent auditor (without management present)?
- [ ] Regular meetings with internal audit (without management present)?
- [ ] ICFR assessment — audit committee oversight of process?
- [ ] Review of earnings releases, financial statements, MD&A prior to filing?
- [ ] Audit committee meeting frequency adequate (minimum 4× per year)?

---

#### Domain 4: Compensation Committee Governance and Executive Pay

**Standard:**

_NYSE §303A.05:_

- Compensation committee: all members independent
- Committee must have: authority to retain independent compensation consultant; annual
  performance evaluation; compensation philosophy documented
- Dodd-Frank §951: Say-on-pay vote (SOP) required at least every 3 years; say-on-frequency
  vote every 6 years

_SOX §304:_

- CEO/CFO clawback of bonuses and equity compensation upon restatement (improper conduct
  related to financial misconduct) [VERIFY: still operative post-SEC Rule 10D-1]

_SEC Rule 10D-1 / Exchange Listing Requirements (effective October 2023):_

- Listed companies must adopt and enforce clawback policy for incentive-based compensation
  from covered executives if company issues an accounting restatement
- No-fault clawback: applies regardless of executive misconduct
- Clawback period: 3 fiscal years preceding restatement trigger date
- Form 10-K disclosure of policy; filings tagged in XBRL [VERIFY]

_UK CGC 2024 (Remuneration Provisions):_

- Provision 38: Remuneration policy should be underpinned by performance-related pay
- Provision 39: Chair of remuneration committee engages with shareholders
- Provision 40: Policy should not reward excessive risk-taking; malus and clawback provisions
- Say-on-pay: binding vote on remuneration policy (every 3 years minimum) and advisory
  vote on remuneration report (annually) — under Companies Act 2006 ss.439, 439A [VERIFY]

_DCGK Recommendation G:_

- Management Board total compensation must be appropriate to performance and market;
  not exceeding a reasonable cap
- Annual bonus (short-term incentive): performance criteria defined in advance; deferral
  of at least 40% by 2 years
- Long-term incentive: 4-year performance period minimum
- Clawback provisions must be included (Recommendation G.14)
- Supervisory Board sets Management Board compensation; Compensation Report required
  (§162 AktG) — shareholder say-on-pay vote annually [VERIFY: DCGK 2022 G.1–G.16]

**Assess:**

- [ ] Compensation committee fully independent (all members)?
- [ ] Independent compensation consultant engaged? Any conflicts disclosed?
- [ ] Executive compensation philosophy documented and board-approved?
- [ ] Pay-for-performance alignment — short-term and long-term incentive design?
- [ ] Clawback policy adopted and compliant with SEC Rule 10D-1 / exchange requirements?
- [ ] Say-on-pay vote frequency compliant (US: at least every 3 years)?
- [ ] Say-on-pay vote result (most recent): level of support? Response to opposition?
- [ ] CEO pay ratio disclosure (SEC §953(b))?
- [ ] UK/DE: Compensation Report compliant with applicable code?
- [ ] UK: Binding policy vote conducted within required cycle?
- [ ] DE: Management Board compensation caps set and disclosed?
- [ ] Malus and clawback provisions in place for long-term incentives?
- [ ] Peer group used for benchmarking disclosed and appropriate?
- [ ] Perquisites and benefits disclosed?
- [ ] Severance arrangements disclosed and board-approved?

---

#### Domain 5: Disclosure Controls and Procedures (SOX §302)

**Standard:**

_SOX Section 302 / SEC Rules 13a-15(b), 15d-15(b):_

- CEO and CFO must certify quarterly and annually that:
  1. They have reviewed the periodic report
  2. The report contains no material misstatements or omissions
  3. The financial statements and other financial information fairly present condition
  4. They are responsible for establishing and maintaining disclosure controls and procedures
  5. They have disclosed significant deficiencies and material weaknesses in ICFR to the
     audit committee and independent auditors
  6. They have disclosed any fraud involving management or employees with significant ICFR roles
- Criminal penalties (SOX §906): knowing violations: $1M fine / 10 years; willful: $5M / 20 years
- [VERIFY: 18 U.S.C. §1350 — criminal certification requirement]

_SEC Rules 13a-15 / 15d-15:_

- Disclosure controls and procedures must be evaluated by CEO/CFO each quarter
- Evaluation must assess effectiveness of controls for recording, processing, summarizing,
  and reporting material information
- Any changes in ICFR that materially affected or are reasonably likely to affect ICFR
  must be disclosed in each quarterly and annual report

**Assess:**

- [ ] SOX §302 certifications filed with each 10-K and 10-Q?
- [ ] CEO and CFO personally sign (not delegated)?
- [ ] Disclosure controls and procedures policy documented?
- [ ] Disclosure Committee in place (senior management representatives)?
- [ ] Evaluation of disclosure controls completed each quarter?
- [ ] Any material weaknesses or significant deficiencies identified and disclosed?
- [ ] Changes in ICFR disclosed in current period filings?
- [ ] Sub-certifications from business unit leaders obtained for CEO/CFO reliance?

---

#### Domain 6: Internal Controls Over Financial Reporting (SOX §404)

**Standard:**

_SOX §404(a) — Management Assessment (all reporting issuers):_

- Annual report must include management's assessment of ICFR effectiveness
- Must state which ICFR framework used (SEC accepts: COSO 2013, other recognized frameworks)
- Must disclose any material weakness (definition: a reasonable possibility of material
  misstatement in financial statements; more severe than significant deficiency)

_SOX §404(b) — Auditor Attestation (accelerated and large accelerated filers only):_

- Independent auditor must attest to and report on management's ICFR assessment
- Performed under PCAOB AS 2201 (An Audit of ICFR Performed in Conjunction with an Audit
  of Financial Statements)
- Auditor attestation must be included in or accompany management's report
- Smaller reporting companies: exempt from §404(b); §404(a) management assessment required

_COSO 2013 Internal Control — Integrated Framework (de facto standard):_

- Five components: Control Environment, Risk Assessment, Control Activities, Information &
  Communication, Monitoring Activities
- 17 principles across 5 components; each principle must be present and functioning
- Significant deficiency: deficiency, or combination, less severe than material weakness
  but important enough for those responsible for oversight to consider
- Material weakness: significant deficiency (or combination) that results in more than remote
  likelihood of a material misstatement not being prevented or detected

_PCAOB AS 2201 (for §404(b) companies):_

- Top-down, risk-based approach to ICFR audit
- Auditor identifies significant accounts and relevant assertions
- Tests design and operating effectiveness of key controls
- Reports directly to audit committee; any material weakness = adverse opinion on ICFR

**Assess:**

- [ ] ICFR framework adopted (COSO 2013 or equivalent)?
- [ ] Entity-level controls (ELCs) documented and assessed (tone at top, culture, oversight)?
- [ ] Significant accounts and relevant assertions identified?
- [ ] Key controls mapped per significant account?
- [ ] Control design documentation current (walkthroughs updated)?
- [ ] Control operating effectiveness testing completed for current year?
- [ ] Management's ICFR assessment signed and included in 10-K?
- [ ] Any material weaknesses identified? Disclosed in 10-K? Remediation underway?
- [ ] Any significant deficiencies communicated to audit committee and auditor?
- [ ] If §404(b) required: auditor attestation included in 10-K?
- [ ] IT general controls (ITGCs) — access controls, change management, operations assessed?
- [ ] Audit committee oversight of ICFR process (agenda items, management presentations)?
- [ ] For UK CGC 2024 Provision 29: Board statement on ICFR included in annual report?

**UK CGC 2024 Provision 29 Note:**
Effective for financial years beginning on or after 1 January 2025, the UK Corporate
Governance Code requires boards of premium-listed companies to make a declaration in
the annual report that they have carried out a review of the effectiveness of the system
of material controls. This is broader than ICFR and covers financial, operational,
reporting, and compliance controls. [VERIFY: FRC guidance on Provision 29 implementation]

---

#### Domain 7: Risk Oversight Framework

**Standard:**

_NYSE §303A.12 / NASDAQ Rule 5605(b):_

- Full board is responsible for risk oversight; may delegate to committees but cannot
  fully delegate accountability
- Audit committee: oversight of financial reporting risk and compliance risk
- Enterprise risk management (ERM): board-level oversight expected

_UK CGC 2024 (Principle C — Composition, Succession and Evaluation):_

- Board is responsible for determining the nature and extent of significant risks willing
  to take in achieving strategic objectives
- Annual review of risk management and internal controls effectiveness
- Board should review going concern and viability statement

_COSO ERM 2017 Framework:_

- Five components: Governance and Culture, Strategy and Objective-Setting, Performance,
  Review and Revision, Information Communication and Reporting
- Key principle: Risk appetite linked to strategy; board sets and monitors risk appetite

_DCGK Recommendation A.1:_

- Supervisory Board oversees Management Board's risk management and internal control
  systems; monitors compliance and audit
- Management Board is responsible for establishing and maintaining risk management and
  internal controls (§91(2) AktG — Pflicht zur Einrichtung eines Überwachungssystems) [VERIFY]

**Assess:**

- [ ] Board-level risk oversight mandate documented in charter?
- [ ] Risk committee or equivalent established (or full board retains oversight)?
- [ ] Risk appetite statement board-approved and current?
- [ ] Enterprise risk register reviewed by board at least annually?
- [ ] Material risk categories covered: financial, operational, compliance, cyber, ESG, strategic?
- [ ] Risk management function reports directly to board/audit committee?
- [ ] Three Lines of Defense model (or equivalent) operating?
- [ ] Viability / going concern statement (UK: required in annual report)?
- [ ] Crisis management and business continuity plans reviewed by board?
- [ ] Emerging risks process: how does board learn about new/evolving risks?

---

#### Domain 8: Related-Party Transaction Controls

**Standard:**

_US SEC Regulation S-K Item 404:_

- Disclosure of transactions ≥$120,000 involving directors, executive officers, nominees,
  or their immediate family members with the company
- Companies must describe written policies for approving related-party transactions

_NYSE §314A / NASDAQ Rule 5630:_

- Listed company policies must cover: review, approval or ratification of transactions
  with related parties; designate responsibility to audit committee or equivalent body

_SRD II Article 9c:_

- Material related-party transactions require prior approval by shareholders or board
- Transactions >1.5% of total assets (or member-state threshold) require approval before
  conclusion; exemptions for ordinary course at arm's length
- Disclosure required for material related-party transactions [VERIFY: national transpositions]

_DCGK Recommendation E.2:_

- Supervisory Board approval required for transactions between the company and members of
  the Management Board or parties related to them
- Arm's length requirement; disclosure in annual report [VERIFY: DCGK 2022 E.1–E.5 + §113 AktG]

_Companies Act 2006 (UK) ss.177-182:_

- Directors must declare interests in proposed and existing transactions
- Service contracts > 2 years require shareholder approval (s.188)
- Substantial property transactions with directors require shareholder approval (s.190) [VERIFY]

**Assess:**

- [ ] Written related-party transaction policy in place?
- [ ] Approval authority defined (audit committee, full board, shareholders)?
- [ ] Approval process followed for known related-party transactions?
- [ ] Independence screening: conflicted directors recused from approval?
- [ ] Arm's length pricing/terms reviewed by independent party?
- [ ] Related-party transactions disclosed in proxy and annual report?
- [ ] Transaction monitoring for new relationships not captured at formation?
- [ ] SRD II: shareholder approval threshold met where applicable?
- [ ] UK: Companies Act ss.177-182 director interest disclosure in board minutes?
- [ ] DCGK: Supervisory Board approval obtained for Management Board transactions?

---

#### Domain 9: Shareholder Engagement and Proxy Governance

**Standard:**

_SEC Proxy Rules (Regulation 14A):_

- Annual meeting proxy statement (DEF 14A) must disclose: director nominees, executive
  compensation, auditor ratification, shareholder proposals
- Say-on-pay: at least every 3 years for listed companies (Dodd-Frank §951)
- Rule 14a-8: Shareholder proposals — company must include or provide grounds for exclusion
- Universal proxy card: SEC Rule 14a-19 (effective September 2022) [VERIFY]

_ISS / Glass Lewis Proxy Voting Guidelines (current year):_

- ISS: Recommends AGAINST director if: attendance below 75%; serves on > 5 boards; failed
  to implement majority shareholder vote; no gender diversity on board
- Glass Lewis: Recommends AGAINST audit committee chair if material weakness disclosed
  and not remediated; against compensation committee chair if say-on-pay opposition >30%
- [VERIFY: current proxy season guidelines — ISS 2025/2026; Glass Lewis 2025/2026]

_SRD II Arts. 9a–9b:_

- Remuneration policy: binding shareholder vote before implementation; at least every 4 years
- Remuneration report: advisory shareholder vote at annual general meeting (AGM)
- Shareholder identification rights (Art. 3a): right to identify beneficial owners

_UK Companies Act 2006 s.439:_

- Annual advisory vote on remuneration report at AGM
- s.439A: Binding vote on remuneration policy at least every 3 years [VERIFY: current thresholds]

**Assess:**

- [ ] Annual meeting held within required timeframe (US: within 13 months of last meeting)?
- [ ] Proxy statement compliant with applicable SEC/FCA disclosure requirements?
- [ ] Say-on-pay vote conducted with required frequency?
- [ ] Most recent say-on-pay vote: level of support? Response to significant opposition?
- [ ] Shareholder engagement program: ongoing dialogue with institutional investors?
- [ ] ISS/Glass Lewis governance scores reviewed and understood by board?
- [ ] Universal proxy card compliance (US: September 2022 requirement)?
- [ ] Director resignation policy for majority-withheld vote (NYSE: §303A.02)?
- [ ] Responsiveness to shareholder proposals — engagement or stated opposition rationale?
- [ ] SRD II/UK: Remuneration policy binding vote conducted within required cycle?
- [ ] Shareholder identification process (SRD II Art. 3a) implemented?

---

#### Domain 10: Compensation Committee — Say-on-Pay and Clawback Deep Dive

**Standard (US — SEC Rule 10D-1 Clawback):**

Effective October 2, 2023 (listed company policies must be effective by December 1, 2023):

1. **Mandatory clawback policy** must apply to:
   - Current and former "executive officers" (Exchange Act §16 officers)
   - Incentive-based compensation received during the 3-year period before restatement
   - "Incentive-based compensation" = any compensation that is granted, earned, or vested
     based wholly or in part on attainment of a financial reporting measure
2. **Restatement trigger**: Any restatement that corrects a material error (Big R restatement
   or non-reliance restatement "little r" that requires recalculation)
3. **No fault**: Clawback applies even if executive had no misconduct
4. **Calculation**: Excess incentive compensation = received amount minus amount that would
   have been received with restated financials
5. **Exceptions**: Company may choose not to recover if recovery is impracticable (SEC has
   narrow exceptions: direct cost exceeds recovery; violation of home-country law) [VERIFY]
6. **Disclosure**: Clawback policy must be filed as exhibit to Form 10-K; XBRL tagging required

**German DCGK Clawback (Recommendation G.14):**

- Executive contracts must contain clawback provisions for variable compensation
- Supervisory Board may reduce or reclaim bonus/LTIP if: performance targets not met
  with hindsight; material compliance violation; significant personal misconduct
- [VERIFY: DCGK G.14 — 2022 provisions and AktG §93 D&O liability interaction]

**Assess:**

- [ ] Rule 10D-1 compliant clawback policy adopted and filed with Form 10-K?
- [ ] Policy covers all required "executive officers" (§16 officers)?
- [ ] Policy applies to both Big-R and little-r restatements?
- [ ] Policy is no-fault (not limited to misconduct)?
- [ ] Clawback recovery process documented?
- [ ] Most recent fiscal year: any restatements triggering clawback obligation?
- [ ] Policy effective date: compliant with December 1, 2023 deadline?
- [ ] XBRL disclosure of clawback policy included in 10-K?
- [ ] DCGK (if applicable): variable compensation clawback provisions in executive contracts?

---

#### Domain 11: Nomination and Governance Committee

**Standard:**

- NYSE §303A.04 / NASDAQ Rule 5605(e): Nomination committee (or board function) composed
  of independent directors; responsible for director recruitment and governance oversight
- Committee charter: scope, director nomination criteria, evaluation of board composition,
  succession planning, ESG governance (increasingly common)
- Independence criteria for director candidates: committee must review before nomination

**Assess:**

- [ ] Nomination / corporate governance committee established with independent members?
- [ ] Written director nomination criteria established (skills matrix)?
- [ ] Board skills matrix current and disclosed in proxy statement?
- [ ] Director succession planning process documented?
- [ ] CEO succession planning: board involvement in emergency and planned succession?
- [ ] Diversity policy in place (gender, ethnicity, skills)?
- [ ] Director recruitment process independent (not solely management-driven)?
- [ ] New director orientation program?
- [ ] ESG governance oversight responsibility clearly assigned?

---

#### Domain 12: ESG and Sustainability Governance Integration

**Standard:**

- CSRD (EU) requires governance disclosure in sustainability statement (ESRS G1 — Business
  Conduct; ESRS 2 GOV-1 through GOV-5) [VERIFY: ESRS G1 requirements post-Omnibus I]
- UK Companies Act 2006 / Companies (Miscellaneous Reporting) Regulations 2018: strategic
  report must address environmental matters, employee/community concerns
- SEC: Climate-related disclosure rule [VERIFY: current status of SEC climate disclosure rule
  following 2025 legal proceedings]
- DCGK Recommendation A.2: Supervisory Board should address sustainability and long-term
  value creation in its oversight mandate

**Assess:**

- [ ] Board-level ESG/sustainability oversight responsibility assigned (committee or full board)?
- [ ] ESG governance included in board or committee charters?
- [ ] Materiality assessment process established for ESG risks?
- [ ] CSRD (EU/UK): Sustainability statement governance disclosures (ESRS GOV-1 through GOV-5)?
- [ ] Climate risk oversight: board-level review of TCFD or ISSB-aligned disclosures?
- [ ] Director ESG competency development (training, external briefings)?
- [ ] Executive compensation linked to ESG metrics (emerging practice)?
- [ ] Greenwashing risk — governance claims verified against actual practices?

---

### Step 6: Severity Classification System

Classify each governance domain and each individual finding using two parallel systems:

#### Domain-Level Governance Maturity Rating

| Rating                    | Definition                                                                                                       | Proxy Advisor / Regulatory View                                                                         |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **GOVERNANCE-EFFECTIVE**  | Governance structure meets or exceeds applicable standard; controls operating effectively; documented and tested | Low engagement risk; favorable proxy advisor treatment                                                  |
| **GOVERNANCE-ADEQUATE**   | Governance structure meets minimum standard; minor gaps or documentation weaknesses; no material control failure | Passing; some room for improvement; unlikely to draw adverse vote                                       |
| **GOVERNANCE-DEVELOPING** | Governance structure partially meets standard; identified gaps; remediation underway or planned                  | Moderate risk; likely to attract proxy advisor scrutiny; engagement recommended                         |
| **GOVERNANCE-INADEQUATE** | Governance structure fails to meet applicable standard; material control weakness; legal non-compliance risk     | HIGH RISK — adverse proxy advisor recommendation likely; regulatory exposure; board accountability risk |

#### Finding-Level Severity Classification

| Severity        | Definition                                                                                                        | Response Required                               |
| --------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| 🔴 **CRITICAL** | Mandatory requirement violated; regulatory enforcement risk; fiduciary duty breach; imminent proxy opposition     | Immediate remediation before next filing or AGM |
| 🟠 **HIGH**     | Best practice requirement missed; significant deviation from code expectation; likely proxy advisor negative flag | Near-term remediation; engagement plan needed   |
| 🟡 **MEDIUM**   | Code recommendation not followed; documentation gaps; disclosed deviation without adequate explanation            | Planned remediation within 12 months            |
| 🟢 **LOW**      | Minor improvement opportunity; investor-friendly enhancement; no compliance risk                                  | Optional; note for next governance review cycle |

#### Prioritization Framework

| Tier                          | Finding Characteristics                                                                                                  | Action Required                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| **Tier 1 — Must Remediate**   | CRITICAL + HIGH severity; mandatory legal/listing requirements; material weakness in ICFR; SEC Rule 10D-1 non-compliance | Remediate before next regulatory filing; board resolution required           |
| **Tier 2 — Should Remediate** | MEDIUM severity; code compliance gaps; significant proxy advisor concerns; say-on-pay opposition risk                    | Remediate within current proxy season planning cycle; disclose plan if asked |
| **Tier 3 — Optimize**         | LOW severity; investor relations improvements; emerging governance best practices                                        | Address in next governance refresh cycle; consider for annual disclosure     |

### Step 7: Apply Quality Frameworks

#### Citation Quality Gates

Run these five gates silently before delivering any output. Revise before delivery if any fail.

| Gate           | Rule                                                                                                                            | Fail Action                                    |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **Source**     | Every governance claim cites a specific statute, rule, code provision, or established standard                                  | Add citation or mark [UNVERIFIED]              |
| **Format**     | All US citations follow standard form (e.g., "15 U.S.C. §78j-1"); UK: "s.439 CA 2006"; EU: "Article 9c SRD II"; DE: "§161 AktG" | Fix format                                     |
| **Currency**   | Every cited provision checked for amendments; governance codes are updated periodically                                         | Flag [CHECK CURRENCY — [year] version]         |
| **Domain**     | Analysis stays within the applicable governance regime; no cross-contamination of US SOX rules into UK-only entities            | Remove or flag with [JURISDICTION-SPECIFIC]    |
| **Confidence** | Uncertainty explicitly stated; no false precision in governance maturity ratings                                                | Add confidence qualifier; escalate to [VERIFY] |

#### Self-Interrogation for CRITICAL and HIGH Findings

For any finding classified CRITICAL or HIGH, apply this 3-pass review before finalizing:

**Pass 1 — Governance Chain Integrity**: Does the governance gap follow logically from the
cited standard? Would a securities regulator, exchange, or proxy advisor actually reach
this conclusion? Is the compliance bar being applied correctly to this entity type?

**Pass 2 — Compensating Governance Controls**: Are there governance structures that
partially compensate for the gap? Does the organization's size, ownership structure, or
operating context reduce the practical risk? Is the "effective" result preserved by
alternative means?

**Pass 3 — Challenge**: What is the strongest governance practitioner argument against
this classification? Is this a genuine violation of a mandatory rule, or a departure from
a best-practice recommendation? Would reasonable proxy advisors or regulators disagree?

#### Confidence Scoring

| Level        | Range     | Meaning                                                    | Action                                           |
| ------------ | --------- | ---------------------------------------------------------- | ------------------------------------------------ |
| **Definite** | 0.95–1.0  | Mandatory rule; clear text; no ambiguity                   | State with confidence                            |
| **High**     | 0.80–0.94 | Strong authority; minor interpretive questions             | State with brief caveat                          |
| **Probable** | 0.60–0.79 | Good arguments; code provision open to interpretation      | State with reasoning and contra-indicators       |
| **Possible** | 0.40–0.59 | Genuinely uncertain; jurisdiction-specific analysis needed | Flag for professional review; present both sides |
| **Unlikely** | 0.0–0.39  | Weak basis; not a recognized governance standard           | Do not assert; flag [UNCERTAIN]                  |

### Step 8: Generate Remediation Roadmap

Produce a remediation roadmap organized by urgency tier:

| Timeline Tier                                   | Trigger                                       | Examples                                                                                                   |
| ----------------------------------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **IMMEDIATE** (next 30–60 days)                 | CRITICAL findings; regulatory filing deadline | Adopt Rule 10D-1 clawback policy; disclose material weakness; resolve audit committee financial expert gap |
| **NEAR-TERM** (next proxy season / fiscal year) | HIGH and MEDIUM findings                      | Update board charter; add INED; increase committee meeting frequency; adopt written RPT policy             |
| **BACKGROUND** (next 12–18 months)              | LOW findings; emerging best practices         | Board skills matrix update; ESG governance integration; director education program                         |

For each remediation item, specify:

- **Finding** (brief description)
- **Severity tier** (CRITICAL / HIGH / MEDIUM / LOW)
- **Board action required** (board resolution / committee action / management action)
- **Responsible party** (board chair / committee chair / GC / CFO)
- **Target completion date**
- **Regulatory or code citation**
- **Success metric** (how will completion be verified?)

### Step 9: Produce Board Deliverables

Generate the following board-ready deliverables based on operating mode and identified gaps:

#### 9a. Board Mandate Template (if governance framework buildout or material gaps found)

```
CORPORATE GOVERNANCE MANDATE

RESOLVED, that the Board of Directors of [Company Name] hereby:

1. ADOPTS the Corporate Governance Guidelines attached hereto as Exhibit A;
2. APPROVES the updated [Audit / Compensation / Nomination] Committee Charter attached as Exhibit B;
3. CONFIRMS the independence determination of each Non-Executive Director as set forth in the
   Board's Independence Analysis attached as Exhibit C;
4. AUTHORIZES management to take all actions necessary to implement the Governance Remediation
   Roadmap attached as Exhibit D, to be completed by [date];
5. DIRECTS the [Audit Committee / Compensation Committee] to report on implementation progress
   at the next regular Board meeting.

[Signature block]
[Date]
```

#### 9b. KRI Governance Dashboard (template)

| KRI                                            | Current Status | Target                               | Threshold                     | Trend | Last Reviewed |
| ---------------------------------------------- | -------------- | ------------------------------------ | ----------------------------- | ----- | ------------- |
| Board independence %                           | [X]%           | ≥50% (UK) / majority (US)            | <50% → CRITICAL               | ↑/↓/= | [date]        |
| Audit committee financial experts              | [N]            | ≥1                                   | 0 → CRITICAL                  | ↑/↓/= | [date]        |
| Annual board evaluation completed              | Y/N            | Y                                    | No → HIGH                     |       | [date]        |
| Say-on-pay support %                           | [X]%           | ≥80%                                 | <70% → HIGH                   | ↑/↓/= | [date]        |
| Related-party transactions approved per policy | Y/N            | Y                                    | No → CRITICAL                 |       | [date]        |
| ICFR material weaknesses open                  | [N]            | 0                                    | ≥1 → CRITICAL                 | ↑/↓/= | [date]        |
| SOX §302 certifications filed                  | Y/N            | Y                                    | No → CRITICAL                 |       | [date]        |
| Clawback policy Rule 10D-1 compliant           | Y/N            | Y                                    | No → CRITICAL                 |       | [date]        |
| Board meeting attendance average               | [X]%           | ≥75%                                 | <75% → proxy flag             | ↑/↓/= | [date]        |
| Director tenure >9 years (UK)                  | [N]            | 0 over threshold without explanation | >0 without explanation → HIGH |       | [date]        |

### Step 10: Quality Verification

Before delivering, verify:

#### Completeness Check

| Element                                                     | Present | Quality (1–5) |
| ----------------------------------------------------------- | ------- | ------------- |
| All 12 governance domains assessed                          |         |               |
| Regulatory Applicability Matrix completed                   |         |               |
| Domain-level maturity ratings assigned                      |         |               |
| Finding-level severity classifications applied              |         |               |
| Prioritization framework applied (Tier 1/2/3)               |         |               |
| Citation Quality Gates passed                               |         |               |
| Self-Interrogation applied to CRITICAL/HIGH findings        |         |               |
| Confidence scores assigned                                  |         |               |
| Remediation Roadmap (3-tier timeline) produced              |         |               |
| Board Mandate Template (if required) generated              |         |               |
| KRI Dashboard template populated                            |         |               |
| Glass Box Audit Trail completed                             |         |               |
| Anti-patterns checked (findings compared against catalogue) |         |               |
| Writing Standards applied                                   |         |               |

Rescore any element below 3/5 before delivery.

#### Writing Standards

Apply these standards before finalizing any deliverable:

1. **Active voice, imperative mood** for obligations: "The board must adopt..." not "It
   should be noted that adoption of a policy..."
2. **Cite, don't describe**: "SOX §302 requires CEO/CFO certification quarterly" not
   "There is a certification requirement under Sarbanes-Oxley"
3. **Classify explicitly**: Every finding must carry a CRITICAL/HIGH/MEDIUM/LOW label;
   never deliver an unclassified finding
4. **Plain English for board consumption**: Executive summary must be understandable to
   a non-lawyer director; technical analysis belongs in appendix
5. **No false precision**: Confidence scores must match evidence quality; do not express
   certainty about provisions not independently verified
6. **Jurisdiction discipline**: Every governance claim must be labeled with its applicable
   regime; never present US SOX requirements as universal
7. **Actionable**: Every finding must be paired with a specific remediation action,
   responsible party, and deadline

---

## Anti-Patterns Catalogue

What NOT to do when conducting a corporate governance audit. Avoid these patterns in both
the audit methodology and the governance findings themselves.

### Governance Audit Methodology Anti-Patterns

1. **Treating comply-or-explain as a free pass** — The UK CGC and DCGK allow companies
   to explain departures, but "explanation" must be substantive. A boilerplate disclosure
   that the company has not complied "due to its particular circumstances" without any
   specific reason is itself a governance failure.

2. **Conflating US listing rules with universal standards** — SOX §302/§404 and NYSE/NASDAQ
   listing rules apply only to SEC reporting issuers listed on those exchanges. Do not apply
   SOX requirements to private companies, UK-only entities, or EU companies.

3. **Treating ICFR as accounting, not governance** — ICFR deficiencies are board-level
   governance issues, not just auditor issues. The audit committee is directly accountable
   for ICFR oversight. A material weakness is a board governance failure, not merely a
   technical finding.

4. **Ignoring the two-tier board structure** — For German AG companies, applying US
   unitary-board standards to the Supervisory Board misses codetermination dynamics,
   the distinct roles of the Aufsichtsrat and Vorstand, and the interaction of AktG
   mandatory provisions with DCGK recommendations.

5. **Omitting proxy advisor standards from the governance analysis** — ISS and Glass Lewis
   governance policies drive institutional shareholder voting. A governance gap that passes
   the strict legal test but fails ISS/Glass Lewis criteria represents a real-world risk
   of adverse say-on-pay or director vote results.

6. **Benchmarking against median rather than best practice** — Governance audits that
   assess whether a company is "as good as peers" rather than whether it meets the
   applicable code standard fail the independence test. Peer-median compliance with a
   known deficiency is still a deficiency.

7. **Overlooking management override risk** — In ICFR assessments, management override
   of established controls is a consistent fraud risk factor. The absence of anti-override
   controls (e.g., journal entry review, audit of manual adjustments) is a CRITICAL gap
   regardless of whether other controls are strong.

8. **Assuming the governance framework on paper equals governance in practice** — Charter
   provisions, written policies, and board resolutions must be tested against actual
   meeting minutes, attendance records, and decision documentation. Paper governance
   without operational governance is a material deficiency.

9. **Failing to identify the designated "financial expert" explicitly** — SOX §301 and
   NYSE §303A.07 require the company to disclose whether the audit committee has a
   financial expert (and if not, why not). Absence of this disclosure is itself a SEC
   reporting deficiency, separate from the governance gap.

10. **Missing the Rule 10D-1 clawback "little r" restatement trigger** — Companies often
    focus on Big-R restatements (requiring restatement of previously filed financial
    statements). Rule 10D-1 also applies to "little r" (non-reliance) restatements and
    corrections that affect incentive compensation calculations. Omitting this nuance
    underestimates clawback exposure.

11. **Under-assessing related-party transactions for independent director approval** —
    Common error: a transaction with a director's affiliated entity is routed to the full
    board for approval (including the conflicted director), rather than to a committee of
    independent directors with the conflicted director recused. Board majority approval
    with the conflicted director present does not satisfy arm's length requirements.

12. **Ignoring SRD II national transposition differences** — SRD II Art. 9c establishes
    a minimum framework for related-party transaction governance, but member state
    transpositions differ significantly in threshold levels and approval processes.
    Applying the Dutch or French transposition to a German company (or vice versa) is
    a jurisdiction bleed error.

13. **Treating say-on-pay as a formality** — When say-on-pay opposition exceeds 30%, it is
    a material governance signal. The failure to engage with institutional investors, disclose
    the board's response, and adjust compensation practices in the following year creates
    compounding governance risk and heightened proxy advisor scrutiny.

14. **Omitting the board evaluation from the governance health assessment** — Annual board
    and committee self-evaluations are required or strongly recommended by NYSE, UK CGC,
    and DCGK. Failure to conduct formal, documented evaluations prevents identification
    of governance gaps and signals poor board accountability.

15. **Failing to flag the Board Chair / CEO separation issue** — Combined Chair/CEO
    structure in US companies is a significant governance risk factor for ISS/Glass Lewis.
    Where the roles are combined, the presence of a strong lead independent director and
    robust executive sessions is essential to mitigate the risk — not optional.

16. **Ignoring sub-certifications in the SOX §302 ecosystem** — CEO/CFO certifications
    rely on representations from business unit and functional leaders (sub-certifications).
    The absence of a formal sub-certification process leaves the SOX §302 disclosure
    controls without an evidential foundation, even if the certification itself is signed.

17. **Applying COSO 2013 principles checklist without testing** — ICFR assessment requires
    evidence of both design and operating effectiveness of controls. Confirming that policies
    exist (design documentation) without testing whether controls actually operate as
    designed is a systematic gap that will be found in a PCAOB inspection or external audit.

18. **Discounting ESG governance as not "real" governance** — Institutional investors
    (State Street, BlackRock, Vanguard) routinely vote against directors at companies with
    inadequate ESG governance. ESRS G1 under CSRD and related national laws are creating
    mandatory governance disclosure obligations. ESG governance is increasingly indistinct
    from core corporate governance.

19. **Producing governance recommendations without board ownership** — Governance audits
    that produce gap lists without identifying which board body (full board, audit committee,
    compensation committee, nomination committee) is responsible for remediation fail to
    create accountability. Every finding must be assigned to a board body with authority
    to act.

20. **Using outdated governance benchmarks** — The UK CGC 2024 replaced the 2018 Code and
    introduced Provision 29 ICFR requirements (effective January 2025). ISS/Glass Lewis
    update their guidelines annually. DCGK was most recently updated in 2022 and is
    subject to ongoing review. Governance audits must use the current-version standards.

---

## Localization Notes

### United States

**Mandatory:**

- SOX §302/§404: All SEC reporting issuers (§404(b) auditor attestation for accelerated filers only)
- NYSE/NASDAQ listing standards: Applicable per exchange; both require majority independent boards
- Rule 10D-1 clawback: Effective December 1, 2023 (all listed companies)
- SEC proxy rules (Regulation 14A): Annual meeting, say-on-pay, universal proxy (September 2022)
- Delaware corporate law: Most US public companies incorporated in Delaware; business judgment
  rule and Revlon standards for M&A apply to director fiduciary duties [VERIFY]

**Best Practice / Comply-or-Explain:**

- Lead independent director: NYSE does not require separation of Chair/CEO roles but requires
  lead independent director or independent Chair when roles are combined
- Board skills matrix: SEC encourages but does not require

### United Kingdom

**Mandatory:**

- Companies Act 2006: Directors' duties (ss.171-177); strategic report; remuneration report
  (quoted companies); directors' interests declaration
- FCA Listing Rules: Continuous disclosure obligations; significant transactions
- UK CGC 2024 (effective January 2025): Comply-or-explain for premium-listed companies;
  Provision 29 ICFR responsibility now board-level obligation

**Comply-or-Explain:**

- UK CGC 2024: All substantive provisions (Principles carry broader principles; Provisions
  require specific disclosure or explanation of departure)
- Specific changes from 2018 Code: New Provision 29 (ICFR board responsibility), revised
  independence tenure treatment, remuneration code changes [VERIFY: full list of 2024 changes]

### Germany

**Mandatory:**

- AktG §76: Management Board duty of care; §93: Business judgment rule; §116: Supervisory
  Board duty of care and business judgment
- AktG §161: Annual Declaration of Conformity (Entsprechenserklärung) for listed companies
- AktG §§100-105: Supervisory Board composition; independence; number of mandates
- Mitbestimmungsgesetz 1976 / Drittelbeteiligungsgesetz 2004: Codetermination composition

**Comply-or-Explain:**

- DCGK 2022: All Recommendations (Empfehlungen) require comply-or-explain;
  Suggestions (Anregungen) do not require formal disclosure

**Structural difference — Two-tier board:**

- Management Board (Vorstand): Day-to-day management; collective responsibility; no shareholders
- Supervisory Board (Aufsichtsrat): Oversight, appointment, and compensation of Management Board;
  employees represented under codetermination; cannot manage the company

### European Union (SRD II)

**Mandatory (via national transposition):**

- Art. 9a: Remuneration policy — binding shareholder vote before implementation; at least
  every 4 years; disclosed on company website [VERIFY: national transposition thresholds]
- Art. 9b: Remuneration report — advisory shareholder vote at AGM; available on company
  website free of charge for 10 years
- Art. 9c: Related-party transactions above materiality threshold require prior approval
  by shareholders or board (as transposed); immediate disclosure to market
- Arts. 3a–3c: Shareholder identification rights — right to identify beneficial owners
  through intermediary chain

---

## Glass Box Audit Trail Template

Every governance audit deliverable must include a completed Glass Box audit trail appended
as the final section.

```yaml
glass_box:
  skill_name: "legalcode-corporate-governance-audit"
  assessment_date: "[ISO 8601 date]"
  operating_mode: "[Governance Audit / Board Readiness / Regulatory Response / Pre-IPO / Transaction Screening]"
  entity_type: "[Large accelerated filer / Accelerated filer / SRC / EGC / UK premium listed / German AG / EU listed / Private]"
  jurisdictions_in_scope: "[US/UK/EU/DE — as applicable]"
  regimes_applied:
    - "SOX §302: [Applied / Not Applicable]"
    - "SOX §404(a): [Applied / Not Applicable]"
    - "SOX §404(b): [Applied / Not Applicable — entity not accelerated filer]"
    - "NYSE/NASDAQ listing standards: [Applied / Not Applicable]"
    - "UK CGC 2024: [Applied / Not Applicable]"
    - "SRD II: [Applied / Not Applicable]"
    - "DCGK 2022: [Applied / Not Applicable]"
    - "AktG: [Applied / Not Applicable]"
  governance_documents_reviewed: "[List documents provided or 'Public filings only']"
  legalcode_mcp: "[Connected — citations VERIFIED / Not connected — citations require manual verification]"
  domains_assessed: "[Number of domains assessed out of 12]"
  findings_summary:
    critical: "[Number]"
    high: "[Number]"
    medium: "[Number]"
    low: "[Number]"
  self_interrogation_applied_to: "[List of CRITICAL/HIGH findings reviewed]"
  self_interrogation_outcomes: "[PASS or REVISED — with brief rationale]"
  confidence_distribution:
    verified: "[Number of citations independently verified]"
    likely: "[Number relying on strong primary authority]"
    verify: "[Number marked [VERIFY] — requires independent confirmation]"
    assumed: "[Number based on assumed facts]"
  key_assumptions:
    - "[Any assumptions made about entity type, filing status, or governance structure]"
  limitations:
    - "[Governance domains not assessed and why]"
    - "[Documents not available that would improve assessment quality]"
    - "[Jurisdiction-specific analysis that requires qualified local counsel]"
  reviewer: "AI-assisted — requires review by qualified corporate governance counsel licensed in relevant jurisdiction(s)"
```

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal authority source.

**With legalcode-mcp connected (preferred):**

- Search for the entity's most recent Form 10-K (ICFR section, SOX certifications, clawback
  policy exhibit), proxy statement (director independence, say-on-pay results), and any
  SEC comment letters on governance disclosures
- Retrieve current NYSE/NASDAQ listing rule provisions (Rules 303A, 5605)
- Search for UK CGC 2024 FRC guidance documents (Provision 29 implementation guidance)
- Retrieve current ISS/Glass Lewis governance policy guidelines (current proxy season)
- Search for recent SEC enforcement actions involving ICFR failures or governance violations
- Mark all legalcode-mcp sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory, rule, and code provision citations with [VERIFY]
- Rely on governance documents provided by the user
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Focus analysis on structural governance assessment rather than regulatory citation depth

---

## Output Format Template

Produce the governance audit report in this format:

```markdown
# Corporate Governance Audit Report

## [Company Name] — [Assessment Date]

## Prepared by: Legalcode Corporate Governance Audit Skill

## Mode: [Governance Audit / Board Readiness / Regulatory Response / Pre-IPO / Transaction Screening]

## Jurisdiction(s): [US / UK / EU / DE]

---

## Executive Summary

**Governance Health Overview**
[2–3 sentences: Overall governance posture, highest-priority gaps, strategic recommendations]

**Key Metrics**
| Metric | Status |
|--------|--------|
| Board independence | [X]% — [GOVERNANCE-EFFECTIVE / ADEQUATE / DEVELOPING / INADEQUATE] |
| Audit committee financial expert | [Yes / No — CRITICAL if No] |
| SOX §302 current | [Certified / Not Certified — CRITICAL if Not] |
| SOX §404(a) current | [Assessed / Not Assessed] |
| Rule 10D-1 clawback policy | [Adopted / Not Adopted — CRITICAL if Not] |
| Say-on-pay last vote | [X%] |
| Open material weaknesses | [N] |
| ICFR domain maturity | [GOVERNANCE-EFFECTIVE / ADEQUATE / DEVELOPING / INADEQUATE] |

**Top 5 Priority Findings**

1. [Finding] — CRITICAL — [One-line remediation]
2. [Finding] — HIGH — [One-line remediation]
3. [Finding] — HIGH — [One-line remediation]
4. [Finding] — MEDIUM — [One-line remediation]
5. [Finding] — MEDIUM — [One-line remediation]

---

## Regulatory Applicability Matrix

[Complete the table from Step 3]

---

## Governance Domain Assessment

### Domain 1: Board Composition and Independence

**Rating**: [GOVERNANCE-EFFECTIVE / ADEQUATE / DEVELOPING / INADEQUATE]
**Confidence**: [Definite / High / Probable / Possible]

| Finding   | Severity    | Applicable Standard | Required Action | Priority Tier |
| --------- | ----------- | ------------------- | --------------- | ------------- |
| [Finding] | 🔴 CRITICAL | [Rule]              | [Action]        | Tier 1        |
| [Finding] | 🟠 HIGH     | [Rule]              | [Action]        | Tier 1        |

[Repeat for all 12 domains]

---

## Consolidated Finding Register

| #   | Domain | Finding | Severity    | Standard | Required Action | Responsible Party | Target Date | Priority Tier |
| --- | ------ | ------- | ----------- | -------- | --------------- | ----------------- | ----------- | ------------- |
| 1   |        |         | 🔴 CRITICAL |          |                 |                   |             | Tier 1        |
| 2   |        |         | 🟠 HIGH     |          |                 |                   |             | Tier 1        |
| ... |        |         |             |          |                 |                   |             |               |

---

## Remediation Roadmap

### IMMEDIATE Actions (next 30–60 days)

[For each Tier 1 CRITICAL finding:]

- **Action**: [Specific action]
- **Board body responsible**: [Board / Audit Committee / Compensation Committee / Nomination Committee]
- **Completion metric**: [How to verify completion]
- **Regulatory citation**: [Rule / Code provision]

### NEAR-TERM Actions (this proxy season / next fiscal year)

[For each Tier 1 HIGH and Tier 2 MEDIUM finding]

### BACKGROUND Actions (12–18 months)

[For each Tier 3 LOW finding]

---

## Board Mandate Template

[If required — see Step 9a]

---

## KRI Governance Dashboard

[If required — see Step 9b]

---

## Appendix: Glass Box Audit Trail

[Complete YAML from Step 10 Glass Box template]
```

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis combining deep legal research
on US SOX Sections 302 and 404 (SEC Rules 13a-15/15d-15; PCAOB AS 2201; SEC Rule 10D-1),
UK Corporate Governance Code 2024 (FRC; effective January 2025; Provision 29 ICFR),
EU Shareholder Rights Directive II (2017/828/EU; Arts. 9a–9c related-party transactions
and say-on-pay), and German Corporate Governance Code 2022 (DCGK; AktG §§76/93/116/161;
two-tier board structure; Mitbestimmungsgesetz). Structural patterns derived from the
Legalcode compliance skill series (legalcode-compliance-program-builder,
legalcode-compliance-risk-assessment, legalcode-anti-bribery-compliance,
legalcode-whistleblower-program-builder, legalcode-esg-sustainability-reporting).
Governance best-practice benchmarks sourced from ISS/Glass Lewis proxy voting guidelines,
COSO 2013/ERM 2017, and institutional investor engagement frameworks. All statutory
citations require verification against authoritative sources.
