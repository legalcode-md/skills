---
name: legalcode-uk-corporate-governance-code
description: Reviews UK Corporate Governance Code 2024 (FRC) compliance for companies listed on the London
  Stock Exchange commercial companies and closed-ended investment funds categories. Use when preparing
  annual report governance disclosures, conducting internal governance reviews, advising listed companies
  on FRC monitoring readiness, assessing board composition against independence criteria, or reviewing
  remuneration structure for Code alignment.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Reviews UK Corporate Governance Code 2024 (FRC) compliance for companies listed on the London Stock Exchange commercial companies and closed-ended investment funds categories. Covers all five Code sections: Board Leadership and Company Purpose (Principles A-E, Provisions 1-5), Division of Responsibilities (Principles F-H, Provisions 6-13), Composition, Succession and Evaluation (Principles I-L, Provisions 14-23), Audit, Risk and Internal Control (Principles M-O, Provisions 24-31), and Remuneration (Principles P-R, Provisions 32-41). Assesses compliance against all 18 Principles and 41 Provisions, generates comply-or-explain analysis, identifies material control gaps, evaluates malus and clawback provisions, assesses board independence and diversity disclosures, and produces a governance compliance roadmap. Use when preparing annual report governance disclosures, conducting internal governance reviews, advising listed companies on FRC monitoring readiness, assessing board composition against independence criteria, or reviewing remuneration structure for Code alignment. Applies to financial years beginning on or after 1 January 2025 (Provision 29 internal controls declaration: 1 January 2026). UK (England and Wales) jurisdiction.


# Legalcode — UK Corporate Governance Code 2024 Compliance Review

> **Disclaimer**: This skill provides a framework for AI-assisted corporate governance
> compliance review. It does not constitute legal advice or professional governance
> advisory services. All outputs should be reviewed by a qualified solicitor, governance
> counsel, or company secretary licensed in England and Wales before use in annual reports,
> regulatory submissions, or board communications. The UK Corporate Governance Code is
> updated periodically; verify the current version from the FRC at frc.org.uk. Statutory
> and regulatory references cited carry hallucination risk — verify against authoritative
> sources before relying on them.

---

## Purpose and Scope

This skill reviews corporate governance practices and disclosures against the UK Corporate
Governance Code 2024, published by the Financial Reporting Council (FRC) on 22 January 2024.

**Covers:**

- Provision-by-provision compliance assessment across all 41 Code Provisions
- Principles application review across all 18 Code Principles
- Comply-or-explain analysis with quality assessment of departure explanations
- Board independence assessment against the nine independence criteria
- Audit committee composition and internal controls framework review
- Remuneration structure review including malus/clawback contractual compliance
- Board composition, diversity reporting, and succession planning assessment
- Risk management and internal control framework evaluation (including Provision 29 preparation)
- Stakeholder and shareholder engagement quality assessment
- FRC annual monitoring readiness check

**Does not:**

- Constitute legal advice or replace qualified governance counsel
- Cover the QCA Corporate Governance Code (for AIM-listed companies)
- Cover the Wates Principles (for large private companies)
- Assess compliance with the UK Stewardship Code (for institutional investors)
- Provide an audit opinion on financial statements or internal controls effectiveness
- Cover compliance with listing rules beyond their interaction with the Code

**Code structure:**

The 2024 Code comprises **18 Principles** (lettered A–R) and **41 Provisions** (numbered
1–41) across five sections. Companies must **apply all Principles** and either **comply
with Provisions or explain any departure** in their annual report.

---

## Jurisdiction and Governing Law

This skill applies UK law and the FRC's UK Corporate Governance Code 2024. It is
jurisdiction-specific to England and Wales (and by extension, Scotland and Northern Ireland
for GB-listed companies incorporated elsewhere in the UK).

**Mandatory scope:**

Companies listed in the **commercial companies category** or the **closed-ended investment
funds category** on the UK Official List (London Stock Exchange) are required to apply
the Code under the UK Listing Rules (UKLR).

**Voluntary adoption:**

Standard-listed companies, AIM-listed companies, and large private companies may choose
to apply the Code, but are not mandated to do so.

**Governing legal framework:**

| Instrument                                                           | Relevance to Code Review                                                           |
| -------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Companies Act 2006 (CA 2006) ss.171–177                              | Directors' duties; s.172 promote company success; s.172(1) stakeholder statement   |
| UK Listing Rules (UKLR)                                              | Mandate comply-or-explain reporting against the Code                               |
| Disclosure Guidance & Transparency Rules (DTR)                       | Financial reporting obligations; going concern disclosures                         |
| Large and Medium-sized Companies Regulations 2008 (as amended)       | Directors' remuneration reporting; CEO pay ratio (250+ UK employees)               |
| Companies (Miscellaneous Reporting) Regulations 2018                 | s.172(1) statement; workforce engagement reporting for large companies             |
| FRC Minimum Standard: Audit Committees and External Audit (May 2023) | Referenced in Provisions 25–26; key audit committee standards                      |
| Market Abuse Regulation (MAR)                                        | Price-sensitive information; insider dealing controls                              |
| UK Stewardship Code 2020                                             | Complementary code for institutional investors; context for shareholder engagement |
| Audit Reform and Corporate Governance Bill (draft)                   | Proposed ARGA replacement for FRC; expanded enforcement powers                     |

**Effective dates:**

- All Provisions except Provision 29: financial years beginning on or after **1 January 2025**
- Provision 29 (internal controls effectiveness declaration): financial years beginning
  on or after **1 January 2026** (the 2018 Code Provision 29 continues until then)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would change the scope or direction of the review
- The company's circumstances affect how a Provision should be assessed
- Whether a Code departure is intentional (comply-or-explain) or inadvertent
- Materiality judgements require business context only the user can supply

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

### Step 1: Accept Input Materials

Accept governance materials in any of these formats:

- **Annual report (draft or published)**: PDF, DOCX, or pasted text of the corporate
  governance report section
- **Board governance policy documents**: Chair/board committee terms of reference,
  board composition register, remuneration policy
- **Questionnaire responses**: Answers to a governance assessment questionnaire
- **Prior year annual report + known changes**: Last year's report plus a summary of
  changes made since publication

If no input is provided, prompt the user to supply at least the corporate governance
section of the annual report.

### Step 2: Gather Company Context

**⟁ CLARIFY** — Before beginning the review, ask the user:

1. **Company size and index membership?**
   - Options: FTSE 100, FTSE 250, FTSE 350, FTSE Small Cap, Other listed (commercial
     companies category), Closed-ended investment fund
   - _Why this matters_: Some Provisions allow lighter requirements for companies below
     FTSE 350 (e.g., two independent NEDs on audit/remuneration committees instead of
     three; two independent NEDs sufficient for Provision 11).

2. **Financial year end?**
   - Free text (e.g., 31 December 2025, 31 March 2026)
   - _Why this matters_: Determines which Code version applies and whether Provision 29
     (internal controls declaration) is in scope for this reporting year.

3. **Review purpose?**
   - Options:
     - Prepare annual report corporate governance disclosures
     - Internal governance gap analysis before external review
     - FRC monitoring readiness assessment
     - Board evaluation supplement
     - M&A target due diligence
     - New listing governance readiness
   - _Why this matters_: Affects tone, depth, and output format.

4. **Known departures from Code Provisions?**
   - Free text: List any Provisions the company intentionally does not comply with, and
     the general reason (e.g., "NED has served 10 years — not re-classified as non-
     independent," "no internal audit function").
   - _Why this matters_: Distinguishes intentional comply-or-explain from inadvertent
     non-compliance. Intentional departures need quality explanation analysis; inadvertent
     gaps need remediation guidance.

5. **Specific focus areas?**
   - Options (multiple allowed): Board composition and independence, Audit committee and
     internal controls, Remuneration (including malus/clawback), Board diversity and
     succession, Shareholder and stakeholder engagement, Provision 29 preparation,
     All sections (full review)
   - _Why this matters_: Allows a priority review for time-constrained situations.

If the user provides partial context, proceed with reasonable defaults and state
assumptions explicitly.

### Step 3: Identify the Applicable Code Version

Confirm the exact Code version and effective provisions:

1. **2024 Code** (FRC, 22 January 2024): Applies to financial years beginning on or
   after 1 January 2025. All Provisions except Provision 29 (internal controls
   declaration).

2. **Provision 29 (2024 Code version)**: Applies to financial years beginning on or
   after 1 January 2026. Companies whose year begins before that date still apply the
   2018 Code Provision 29.

3. **2018 Code (residual)**: For financial years beginning before 1 January 2025 only.
   Flag if the user appears to be reviewing against the wrong Code version.

**⟁ CLARIFY** — If the company's financial year end and the applicable Code version are
inconsistent with what the user describes (e.g., a December 2024 year-end being reviewed
against the 2024 Code), flag the discrepancy and ask the user to confirm which Code
applies.

### Step 4: Gather Legal Authority

Use **legalcode-mcp** to verify current regulatory requirements:

Search for:

- Current UK Listing Rules provisions on comply-or-explain obligations
- FRC Minimum Standard for Audit Committees and External Audit (May 2023)
- FRC Annual Review of Corporate Governance Reporting (latest edition)
- Relevant FCA diversity listing rules (LR 9.8.6R gender and ethnicity targets)
- Companies Act 2006 sections on directors' duties, s.172 statement requirements,
  remuneration reporting
- Large and Medium-sized Companies Regulations 2008 (as amended 2019) for CEO pay ratio

Save results to `/tmp/legalcode-uk-cgc-authority.md`.

**If legalcode-mcp is not connected:**

- Mark all statutory and regulatory references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed using the research embedded in this skill, with [VERIFY] tags on citations

### Step 5: Section-by-Section Compliance Assessment

Assess each of the five Code sections systematically. For each Provision:

- Identify the **current position** from the materials provided
- Classify as **COMPLIANT**, **PARTIAL**, **NON-COMPLIANT**, or **EXPLAIN**
  (see Compliance Classification Framework below)
- Identify any **quality gaps** in the disclosure or explanation
- Generate **actionable remediation steps** for PARTIAL and NON-COMPLIANT findings
- Assess the **quality of comply-or-explain explanations** for EXPLAIN findings

**⟁ CLARIFY** — For a full review with 41 Provisions across 5 sections, ask the user
whether to produce:

- **Full provision-level analysis**: All 41 Provisions assessed individually
- **Section-level summary**: Material findings per section with the most significant
  issues highlighted
- **Priority gaps only**: Focus on NON-COMPLIANT and PARTIAL findings, skip COMPLIANT
  confirmations

Cover all five Code sections using the Provision Analysis Framework below.

### Step 6: Comply-or-Explain Quality Assessment

For every EXPLAIN-classified finding (where the company has intentionally departed from
a Provision), assess the quality of the explanation against the FRC's five-element test:

| Element             | Description                                                                  | Quality (1–3)                                 |
| ------------------- | ---------------------------------------------------------------------------- | --------------------------------------------- |
| **Background**      | Explanation sets out why the departure is necessary for this company         | 1=absent, 2=generic, 3=company-specific       |
| **Rationale**       | Clear explanation of why the alternative still achieves effective governance | 1=absent, 2=vague, 3=detailed                 |
| **Impact**          | Describes what effect the departure has had or will have                     | 1=absent, 2=acknowledged, 3=quantified        |
| **Risk mitigation** | Addresses governance risks created by the departure and mitigating actions   | 1=absent, 2=noted, 3=specific mitigations     |
| **Time-frame**      | If temporary, indicates when the company expects to comply                   | 1=absent (if applicable), 2=vague, 3=specific |

A quality explanation scores **12–15** out of 15. An explanation scoring below 9 should
be flagged for revision before annual report publication.

**⟁ CLARIFY** — When an explanation appears generic or boilerplate (e.g., "The company
considers this arrangement to be in the best interests of shareholders"), ask the user:
"This explanation appears generic. Can you provide the company-specific background that
explains why this departure is appropriate for the company's particular circumstances?"

### Step 7: Internal Controls and Provision 29 Assessment

Assess readiness for Provision 29 (effective 1 January 2026) separately, even if not
yet mandatory:

**Current position assessment:**

1. Has the company identified its **principal risks** in the annual report?
2. Has the company mapped **material controls** to each principal risk?
3. What monitoring processes are in place (management self-assessment, internal audit,
   risk/compliance function, external assurance)?
4. Is there an **internal audit function**? If not, has the audit committee reviewed
   the need annually (Provision 28)?
5. Has the board reviewed the **effectiveness** of the risk management and internal
   control framework in the reporting period?

**Provision 29 readiness score (if not yet effective):**

| Readiness Step                                      | Status | Gap |
| --------------------------------------------------- | ------ | --- |
| Principal risks identified                          |        |     |
| Material controls mapped to risks                   |        |     |
| Monitoring processes documented                     |        |     |
| Internal audit coverage adequate                    |        |     |
| External assurance scope assessed                   |        |     |
| Board has reviewed framework effectiveness          |        |     |
| ESG/sustainability controls in scope                |        |     |
| Interim financial statements updated (Provision 30) |        |     |

**⟁ CLARIFY** — If the company's financial year means Provision 29 (2024 Code version)
is already in scope (year beginning on or after 1 January 2026), ask for the board's
declaration and any material controls identified as not operating effectively.

### Step 8: Remuneration and Malus/Clawback Assessment

Assess Provisions 32–41 with particular focus on the 2024 Code changes:

**Malus/clawback contractual compliance (Provision 37 — KEY 2024 CHANGE):**

Verify that malus and clawback provisions are contained in:

- Executive directors' **service contracts** (not just remuneration policy)
- **Share plan rules** to which the director is legally bound
- **Award documentation** the director has agreed to be bound by

Verify the annual report (Provision 38) discloses:

- The circumstances in which provisions can be invoked
- The period for malus/clawback and rationale for the chosen period
- Whether provisions were used in the reporting period (even if the answer is "no")

**Vesting and holding periods (Provision 36):**

Verify that long-term share awards have:

- A total vesting and holding period of **five years or more**
- **Phased release** (shares released progressively, not all at once)

**Remuneration committee independence (Provision 32):**

Verify:

- Committee comprises independent NEDs only
- Minimum three members (two for below FTSE 350)
- No executive director involved in own remuneration decisions

### Step 9: Missing Disclosure Detection

After provision-level analysis, check for disclosures that should be present but are
absent from the materials provided:

| Required Disclosure                                        | Basis          | Present? | Severity if Absent |
| ---------------------------------------------------------- | -------------- | -------- | ------------------ |
| Statement that Principles have been applied                | UKLR           |          | RED                |
| Explanation of any Provision departure                     | UKLR           |          | RED                |
| List of independent NEDs with basis for independence       | Provision 10   |          | RED                |
| Board performance review description                       | Provision 21   |          | RED                |
| Nomination committee work description                      | Provision 18   |          | YELLOW             |
| Audit committee work description (incl. FRC Min. Standard) | Provision 26   |          | RED                |
| Remuneration committee work description                    | Provision 34   |          | YELLOW             |
| Malus/clawback circumstances and period                    | Provision 38   |          | RED                |
| Whether malus/clawback used                                | Provision 38   |          | RED                |
| Internal audit function or explanation of absence          | Provision 28   |          | RED                |
| Going concern statement in interim statements              | Provision 30   |          | RED                |
| Viability statement                                        | Provision 31   |          | YELLOW             |
| Diversity policy and progress                              | Provision 23   |          | YELLOW             |
| s.172(1) stakeholder statement                             | CA 2006        |          | YELLOW             |
| CEO pay ratio (if 250+ UK employees)                       | Regs 2008/2019 |          | YELLOW             |

### Step 10: Generate Remediation Roadmap

For each PARTIAL and NON-COMPLIANT finding, generate a specific remediation action:

- **Immediate (before annual report filing)**: Disclosure gaps that can be addressed
  through additional text in the current annual report
- **Short-term (within 12 months)**: Policy or practice changes requiring board/committee
  decision but achievable within the year
- **Medium-term (12–36 months)**: Structural governance changes (board composition
  changes, succession pipeline, committee restructuring)

Classify each action by:

- Owner (Board, Audit Committee, Remuneration Committee, Nomination Committee, Company
  Secretary, External Counsel)
- Priority (P1: before filing / P2: before next AGM / P3: within 12 months)

### Step 11: Quality Verification

Before delivering the analysis, run the quality checks in the Quality Assurance Framework:

1. Run the 5 Citation Quality Gates silently. Revise failures before delivery.
2. For every RED finding, run the 3-pass Self-Interrogation.
3. Verify that no jurisdiction-specific concepts have been stated as universal.
4. Verify that Provision 29 effective date is correctly applied (1 January 2026).
5. Verify FTSE 350 vs. smaller company thresholds are correctly applied.
6. Verify that the comply-or-explain quality scores are calibrated (not systematically
   over- or under-scored).

### Step 12: Deliver Report

Produce the output using the Output Format Template defined below.

---

## Compliance Classification Framework

Apply this four-tier system to every Principle and Provision:

### COMPLIANT

The company's current policies, practices, and disclosures fully address the Code
requirement. No action required.

_Evidence threshold_: The annual report (or governance documents provided) contains
specific, company-tailored disclosure that demonstrates compliance with the letter and
spirit of the requirement.

### PARTIAL

The company addresses the Code requirement but with gaps, omissions, or
insufficient disclosure. Action required to reach full compliance.

_Common partial patterns_:

- Practice exists but disclosure is absent or generic
- Some elements of a Provision are met but others are not
- Policy exists on paper but no evidence of implementation
- Comply-or-explain explanation quality is insufficient (scores below 9/15)

### NON-COMPLIANT

The company does not comply with the Code Provision and has not provided an explanation.
Immediate action required.

_Evidence threshold_: No policy, practice, or disclosure found addressing the Provision,
or a clear breach of a specific requirement (e.g., chair also serving as CEO).

### EXPLAIN

The company has intentionally departed from a Provision and provides or should provide
a comply-or-explain explanation in the annual report. Assess explanation quality using
the five-element test.

_Note_: EXPLAIN is not a negative classification — the comply-or-explain mechanism is a
legitimate part of the Code. A well-drafted EXPLAIN finding with a score of 12–15/15
represents good governance practice.

---

## Provision Analysis Framework

### Section 1: Board Leadership and Company Purpose (Principles A–E, Provisions 1–5)

**Provision 1 — Culture assessment and monitoring**

_Requirement_: The board must assess and monitor culture and how the desired culture
has been embedded throughout the organisation (not just at board level).

_Assessment criteria_:

- Is there a defined set of company values and culture standards?
- Does the board have specific mechanisms to assess culture (surveys, whistleblowing
  data, exit interviews, ethics hotline metrics, site visits)?
- Does disclosure describe **how** culture has been embedded (operational implementation)
  not just what culture aspired to?
- Are there measurable culture metrics reported? (FRC 2024: only ~20% of sampled
  companies disclosed clear culture metrics)
- Is feedback from operational levels evidenced and acted upon?

_Common failures_: Generic aspirational statements; culture described as "tone from the
top" only; no metrics; no operational-level culture assurance evidence.

---

**Provision 2 — Strategy, values, and principal decisions**

_Requirement_: The board should understand and promote the company's purpose, values,
and strategy. Governance reporting (Principle C) should focus on board decisions and
their outcomes, not process description.

_Assessment criteria_:

- Does the annual report describe **specific board decisions** made in the year (not
  just processes)?
- Are decisions linked to strategy and long-term objectives?
- Does outcome-based reporting demonstrate the board's contribution to long-term
  sustainable success?

---

**Provision 3 — Stakeholder engagement and s.172 statement**

_Requirement_: The board must understand views of key stakeholders and describe how
s.172 CA 2006 matters have been considered in board discussions and decision-making.

_Assessment criteria_:

- Are key stakeholders (workforce, customers, suppliers, investors, communities) identified?
- Does the s.172(1) statement describe how stakeholder interests influenced specific decisions?
- Is the engagement outcomes-based (what was learned and what changed) not process-based?

_Common failures_: Generic stakeholder lists without engagement evidence; s.172 statement
describes who stakeholders are without demonstrating influence on decisions.

---

**Provision 4 — AGM and shareholder vote action**

_Requirement_: All resolutions at general meetings decided on a poll. Chair must act on
significant votes against resolutions (typically ≥20% against). Results must be acted
upon meaningfully.

_Assessment criteria_:

- Are all AGM resolutions decided on a poll?
- Were any resolutions in the prior year opposed by 20% or more of votes cast?
- If yes, has the company disclosed follow-up engagement with shareholders and outcomes?

---

**Provision 5 — Major shareholder meetings**

_Requirement_: The chair should hold meetings with major shareholders without executive
management present, at least annually. The SID should attend sufficient of these meetings
to develop a balanced understanding of shareholders' views.

_Assessment criteria_:

- Does the disclosure confirm the chair met major shareholders without management present?
- Does the SID attend sufficient of these meetings?

---

### Section 2: Division of Responsibilities (Principles F–H, Provisions 6–13)

_Note_: Section 2 was **unchanged from the 2018 Code**.

**Provision 6 — Chair/CEO separation**

_Requirement_: Chair and CEO roles must not be combined. If combined (extremely rare),
the board must provide a full explanation.

_RED flag_: Chair also serving as CEO, or no disclosure addressing this requirement.

---

**Provision 7 — Chair independence and former CEO ban**

_Requirement_: The chair must be independent on appointment. A former CEO of the same
company should not become chair.

_Assessment criteria_:

- Was the chair independent on appointment?
- Was the chair previously CEO of this company?

_RED flag_: Former CEO of same company appointed as chair.

---

**Provision 8 — Senior Independent Director (SID)**

_Requirement_: The board must appoint one independent NED as SID. The SID serves as
sounding board for the chair and intermediary for directors and shareholders.

---

**Provision 9 — NED meetings without chair**

_Requirement_: The SID and other NEDs must meet without the chair present at least annually.

---

**Provision 10 — Independence assessment**

_Requirement_: The board must identify in the annual report each NED it considers
independent. Nine circumstances may indicate lack of independence (any triggers scrutiny):

| Criterion                                                       | Independence Risk                                |
| --------------------------------------------------------------- | ------------------------------------------------ |
| Employee in past five years                                     | Likely non-independent                           |
| Material business relationship in past three years              | Likely non-independent                           |
| Additional remuneration beyond director's fee                   | Likely non-independent                           |
| Close family ties with adviser/director/senior employee         | Likely non-independent                           |
| Cross-directorship or significant links through other companies | Likely non-independent                           |
| Represents a significant shareholder                            | Likely non-independent                           |
| Board service exceeding **nine years**                          | [VERIFY] Likely non-independent unless justified |

_Note_: The nine criteria are indicators, not automatic disqualifiers. The board may
conclude a NED is independent notwithstanding one or more criteria with adequate explanation.

---

**Provision 11 — Board independence composition**

_Requirement_: At least half the board (excluding the chair) must be independent NEDs.
Companies below FTSE 350: at least two independent NEDs is sufficient.

_Assessment_: Count independent NEDs (per Provision 10) vs. executive directors.

---

**Provision 12 — Chair committee non-membership**

_Requirement_: The chair should not sit on the audit, remuneration, or nomination
committees (unless the specific Provision permits attendance at nomination committee
when not dealing with chair succession).

---

**Provision 13 — NED time commitments**

_Requirement_: The annual report should describe time commitments of each NED and confirm
directors do not have excessive commitments.

---

### Section 3: Composition, Succession and Evaluation (Principles I–L, Provisions 14–23)

**Provision 14 — Nomination committee establishment**

_Requirement_: The board must establish a nomination committee to lead appointments and
develop a diverse succession pipeline.

---

**Provision 15 — Nomination committee composition**

_Requirement_: Majority of members must be independent NEDs. The board chair may chair
the committee but must not chair it when dealing with the appointment of a successor
to the chair.

---

**Provision 16 — Skills and capabilities assessment**

_Requirement_: The nomination committee must evaluate the balance of skills, experience,
independence, and knowledge, and prepare capability descriptions for appointments.

---

**Provision 17 — NED terms and tenure**

_Requirement_:

- NEDs appointed for specified terms (usually three years), renewable
- Terms beyond **six years** subject to particularly rigorous review
- Terms beyond **nine years** require specific justification; independence must be considered

---

**Provision 18 — Nomination committee disclosure**

_Requirement_: A separate section of the annual report must describe the work of the
nomination committee.

---

**Provision 19 — Chair tenure limit**

_Requirement_: The chair should not remain in post beyond **nine years** from the date
of first appointment to the board (including prior NED service). Extension requires
specific justification.

_RED flag_: Chair exceeding nine years without disclosure and justification.

---

**Provision 20 — Independence override disclosure**

_Requirement_: If the board concludes a director is independent despite one or more
independence indicators, the board must state its reasons.

---

**Provision 21 — External board performance review**

_Requirement_: The board must undertake an externally-facilitated board **performance
review** at least every three years. The external facilitator must be identified in
the annual report with a statement of whether they have any other connection to the company.

_Assessment criteria_:

- When was the last external board performance review?
- Is the external facilitator named in the annual report?
- Is a statement provided on whether the facilitator has other connections to the company?

---

**Provision 22 — Board performance review scope**

_Requirement_: The board performance review must consider composition, diversity,
effectiveness of members working together, and individual director performance.

---

**Provision 23 — Diversity reporting**

_Requirement_: The annual report must describe:

- The board's diversity policy and any initiatives
- Objectives and link to company strategy
- How the policy has been implemented
- Progress on achieving objectives

_Note_: The 2024 Code removes specific references to gender, ethnic background, cognitive
and personal strengths, replacing with broader "diversity, inclusion and equal opportunity."
However, the FCA Listing Rules (LR 9.8.6R) separately require: [VERIFY]

- Women occupying at least 40% of board positions
- At least one senior board position held by a woman
- At least one board member from a non-white ethnic minority background

---

### Section 4: Audit, Risk and Internal Control (Principles M–O, Provisions 24–31)

This section contains the **most significant 2024 Code changes**, particularly around
internal controls.

**Provision 24 — Audit committee composition**

_Requirement_: Audit committee of independent NEDs with minimum **three members**
(two for below FTSE 350). Committee chair and at least one member must have relevant
financial experience; committee as a whole must have competence relevant to the sector.

---

**Provision 25 — Audit committee responsibilities (aligned to FRC Minimum Standard)**

_Requirement_: The audit committee must carry out its roles as set out in the FRC
Minimum Standard: Audit Committees and External Audit (May 2023). Key responsibilities:

- Monitor the integrity of financial statements
- Review significant financial reporting judgements
- Monitor and review effectiveness of the internal audit function
- Oversee the external auditor relationship (appointment, independence, non-audit services)
- Review the audit and assurance policy (or provide equivalent disclosure)

---

**Provision 26 — Audit committee disclosure**

_Requirement_: The annual report must describe the work of the audit committee including
matters set out in the FRC Minimum Standard.

---

**Provision 27 — Ongoing risk and internal control monitoring**

_Requirement_: The board must monitor the company's risk management and internal control
framework on an ongoing basis (not just annually).

---

**Provision 28 — Internal audit function**

_Requirement_: Companies should have an internal audit function. If none exists, the
audit committee must review the need annually and the reasons for absence must be
explained in the annual report.

_RED flag_: No internal audit function AND no annual review and explanation.

---

**Provision 29 — Internal controls effectiveness declaration**

_MAJOR 2024 CODE CHANGE — effective financial years beginning on or after 1 January 2026_

_Requirement_: The board must:

1. Monitor and annually review the effectiveness of the risk management and internal
   control framework (covering ALL material controls: financial, operational, reporting,
   and compliance controls)
2. Disclose in the annual report:
   - How the board has monitored and reviewed effectiveness
   - A **declaration of effectiveness** of material controls as of the balance sheet date
   - Description of any material controls not operating effectively, actions taken, and
     steps addressing previously reported issues

_Material controls categories_:

- **Financial**: Financial statement preparation, reconciliations, financial forecasting
- **Operational**: Supply chain, cybersecurity, health and safety, M&A process controls
- **Reporting**: ESG/sustainability reporting, narrative reporting, annual report controls
- **Compliance**: GDPR, Bribery Act, Economic Crime Act, sanctions controls

_Assurance approach_: External assurance is NOT mandatory. Boards must decide what level
is appropriate. Common frameworks: COSO, ISO 31000, three-lines-of-defence model.

_Readiness assessment_: Even before the 2026 effective date, the FRC expects companies
to be preparing. Absence of preparatory disclosure in 2025 annual reports is noted.

---

**Provision 30 — Going concern (expanded in 2024 Code)**

_Requirement_: The board must state in the annual report **and all interim financial
statements** (expanded from half-yearly only in the 2018 Code) that it considers it
appropriate to adopt the going concern basis, identifying any material uncertainties
over at least 12 months from the date of approval.

_RED flag_: Going concern statement absent from interim financial statements.

---

**Provision 31 — Viability statement**

_Requirement_: The board must explain how it has assessed prospects over a period longer
than 12 months, stating the period and assumptions. The statement should use quantitative
and qualitative information and be subject to robust challenge.

_Common failures_: Viability statements covering only 12 months; boilerplate language;
no explanation of stress testing or scenario analysis.

---

### Section 5: Remuneration (Principles P–R, Provisions 32–41)

**Provision 32 — Remuneration committee composition**

_Requirement_: Remuneration committee of independent NEDs with minimum **three members**
(two for below FTSE 350). No executive director involved in deciding own remuneration.

---

**Provision 33 — Remuneration authority**

_Requirement_: Committee has delegated authority for chair, executive directors, and
senior management remuneration. Committee chair (not the board chair) responsible
for committee work.

---

**Provision 34 — Remuneration committee disclosure**

_Requirement_: Annual report must describe the committee's work including engagement
with the workforce on how executive remuneration aligns with wider company pay policy.

---

**Provision 35 — Remuneration consultant**

_Requirement_: If a remuneration consultant is appointed, they must be identified in
the annual report with a statement of whether they have any other connection to the company.

---

**Provision 36 — Long-term share awards**

_Requirement_: Share awards should normally:

- Be subject to a total vesting and holding period of **five years or more**
- Be released on a **phased basis** (not all at once)

---

**Provision 37 — Malus and clawback (KEY 2024 CHANGE)**

_Requirement_: Directors' contracts **and/or other agreements or documents** (including
plan rules and award documentation the director has agreed to be bound by) must include
malus and clawback provisions enabling the company to:

- **Clawback**: Recover sums or share awards already delivered
- **Malus**: Withhold sums or share awards not yet delivered
- The provision must specify circumstances in which it would be appropriate

_Key 2024 change_: Provisions must be in **legally binding contracts/agreements** — not
merely in non-binding remuneration policy documents. [VERIFY current legal enforceability
of plan rules under applicable law]

_Common triggering circumstances_: Material misstatement of financial results; serious
misconduct; material reputational damage; material failure of risk management; serious
breach of regulatory requirements.

---

**Provision 38 — Malus/clawback annual disclosure (KEY 2024 CHANGE)**

_Requirement_: The annual report on remuneration must disclose:

- The **circumstances** in which malus and clawback provisions could be used
- The **period** for malus/clawback and **why the selected period** is best suited to
  the organisation
- Whether the provisions **were used** in the last reporting period and, if so, why

_Note_: A "provisions were not used" statement is required. Silence is not compliance.

---

**Provision 39 — Workforce pay consideration**

_Requirement_: Remuneration committees must consider pay and conditions of the workforce
when setting executive remuneration policy.

---

**Provision 40 — Pay conditions in annual report**

_Requirement_: The remuneration committee's annual report must describe how pay conditions
elsewhere in the company were taken into account when determining executive remuneration.

---

**Provision 41 — Shareholder vote engagement**

_Requirement_: Where a significant percentage of shareholders vote against a remuneration
report or policy (typically ≥20%), the committee must explain what actions it intends to
take to consult with shareholders.

---

## Prioritization Framework

### Priority 1 — Immediate Action Required (before annual report filing)

Findings that constitute a clear breach of the Code with no comply-or-explain explanation
available, or disclosure gaps that can be remedied by adding text to the current annual
report:

- Chair/CEO role combination without explanation (Provision 6) — **structural breach**
- Former CEO appointed as chair of same company (Provision 7) — **structural breach**
- Fewer than half the board (excluding chair) independent (Provision 11) — **structural breach**
- Chair in post beyond nine years without disclosure/justification (Provision 19)
- Malus/clawback not in legally binding contracts (Provision 37)
- No disclosure of whether malus/clawback was used in reporting period (Provision 38)
- No going concern statement in interim financial statements (Provision 30)
- No internal audit function AND no annual review and explanation (Provision 28)
- Significant AGM vote against (≥20%) with no follow-up engagement disclosed (Provision 4)
- No statement that Principles have been applied (UKLR obligation)

### Priority 2 — Address Before Next AGM (within 6 months)

Material governance gaps that require board or committee decision but can be resolved
within the reporting cycle:

- Insufficient explanation quality for existing Code departures (below 9/15 on the
  five-element test)
- Audit committee without required financial expertise (Provision 24)
- Nomination committee chair is board chair during CEO succession (Provision 15)
- Chair who is an executive director or former executive (Provision 7)
- No external board performance review in past three years (Provision 21)
- External facilitator not named or no other-connection statement (Provision 21)
- Vesting periods shorter than five years (Provision 36)
- All shares vesting simultaneously with no phased release (Provision 36)
- Remuneration consultant with undisclosed connections to company (Provision 35)

### Priority 3 — Address Within 12–36 Months (structural improvements)

Longer-term governance improvements requiring succession planning, structural change,
or multi-year programmes:

- Board composition changes to achieve independent majority (Provision 11)
- Internal audit function establishment if currently absent (Provision 28)
- Provision 29 (internal controls) preparation and maturity programme (Provision 29)
- Board diversity targets and pipeline development (Principle J; FCA LR)
- Culture metrics programme with measurable KPIs (Provision 1)
- Succession plan development for CEO, CFO, and chair (Principle I)
- Outcome-based governance reporting transformation (Principle C)

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise failures before delivering.

| Gate           | Rule                                                                                          | Fail Action                                             |
| -------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **Source**     | Every reference to a Code Provision cites the specific Provision number and 2024 Code         | Add reference or mark [UNVERIFIED — counsel to confirm] |
| **Format**     | All citations follow consistent format: "Provision [N], UK Corporate Governance Code 2024"    | Fix format                                              |
| **Currency**   | Every regulatory reference checked against the applicable effective date                      | Flag [CHECK CURRENCY — may not yet be effective]        |
| **Domain**     | Analysis stays within UK listed company governance; no US/EU governance requirements imported | Remove or flag cross-jurisdictional bleed               |
| **Confidence** | Uncertainty about a requirement's application explicitly stated                               | Add confidence qualifier                                |

### Self-Interrogation for RED (Priority 1) Findings

For any finding classified Priority 1 (immediate action required), apply this 3-pass
review before delivery:

**Pass 1 — Compliance Chain Integrity**: Does the Priority 1 classification follow
logically from the Code Provision cited? Would the FRC or a governance-informed investor
reach the same conclusion on these facts?

**Pass 2 — Completeness**: Have all relevant Code Provisions been considered? Is the
finding isolated or part of a pattern of governance weakness? Are there any statutory
law obligations (CA 2006, UKLR) that reinforce or modify the Code requirement?

**Pass 3 — Challenge**: What is the strongest argument that the company's position is
actually acceptable? Is there a comply-or-explain basis that the company may not have
articulated? Would the finding survive challenge by the company's governance counsel?

### Confidence Scoring

| Level        | Range     | Meaning                                               | Action                                                         |
| ------------ | --------- | ----------------------------------------------------- | -------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear Code language, no ambiguity                     | State with confidence                                          |
| **High**     | 0.80–0.94 | Strong Code basis, minor interpretation questions     | State with brief caveat                                        |
| **Probable** | 0.60–0.79 | Good arguments; Code could be interpreted differently | State with explicit reasoning and alternative interpretation   |
| **Possible** | 0.40–0.59 | Genuinely uncertain application to company's facts    | Flag for governance counsel review with both positions         |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative application                   | Do not assert; flag [UNCERTAIN — governance counsel to advise] |

---

## Anti-Patterns

What NOT to do when reviewing UK Corporate Governance Code compliance:

1. **Treating comply-or-explain as automatic non-compliance** — The comply-or-explain
   mechanism is a legitimate feature of the Code, not a failure. A company with a
   thoughtful, company-specific explanation for a Provision departure may have better
   governance than a company with boilerplate "compliant" ticking. Never classify EXPLAIN
   as worse than PARTIAL without assessing explanation quality.

2. **Applying FTSE 350 thresholds to smaller companies** — Provisions 11, 24, and 32
   allow smaller companies (below FTSE 350) to have two independent NEDs on audit and
   remuneration committees rather than three. Applying the FTSE 350 standard to a smaller
   company produces false positive NON-COMPLIANT findings.

3. **Confusing the 2018 and 2024 Code versions** — The 2024 Code applies to financial
   years beginning on or after 1 January 2025. Provision 29 (internal controls declaration)
   applies from 1 January 2026. Reviewing a 2024 year-end company against the wrong
   Code version produces incorrect compliance assessments.

4. **Importing US SOX concepts** — The UK internal controls regime under Provision 29
   is materially different from US SOX Section 302/404. External auditor attestation is
   NOT required. Controls are material to the company's facts, not SOX-prescribed. Do not
   describe Provision 29 as "mandatory external assurance" — it is not.

5. **Treating nine years as an automatic independence bar** — Nine years of board service
   is a circumstance that may indicate lack of independence (Provision 10). It is not
   an automatic disqualifier. The board may conclude the NED remains independent if it
   provides a specific, reasoned explanation. Do not classify nine-year NEDs as
   NON-COMPLIANT without first checking whether the company has addressed this in the
   annual report.

6. **Overlooking interim financial statements for going concern** — The 2024 Code
   (Provision 30) extends the going concern statement obligation to all interim financial
   statements (beyond the half-yearly requirement in the 2018 Code). This is a common
   missed finding when reviewers focus on the annual report only.

7. **Checking for malus/clawback in the remuneration policy only** — The 2024 Code
   (Provision 37) requires malus and clawback in legally binding **contracts and/or
   other legally binding agreements**. A policy document that is not contractually
   binding does not satisfy the Provision. Always check the service contract and share
   plan rules.

8. **Skipping the Provision 38 "were provisions used" requirement** — The 2024 Code
   requires disclosure of whether malus/clawback provisions were used in the reporting
   period, even if the answer is "no." Silence is not compliance. This is a frequent
   finding in FRC annual monitoring reviews.

9. **Accepting outcome-language as outcome-based reporting** — Principle C requires
   reporting that focuses on decisions and their outcomes. Using words like "outcome"
   and "decision" in a governance report is not the same as genuinely outcomes-based
   reporting. Look for: (a) identification of the specific decision, (b) the context
   (strategy/objective the decision relates to), and (c) what happened as a result.

10. **Ignoring culture metrics** — FRC monitoring consistently finds that fewer than
    30% of sampled companies disclose clear culture metrics. A culture section describing
    aspirational values without measurable indicators should be flagged as PARTIAL,
    not COMPLIANT.

11. **Missing ESG/sustainability controls in Provision 29 scope** — Material controls
    should cover all four categories: financial, operational, reporting, AND compliance.
    Sustainability/ESG reporting controls are reporting controls. A Provision 29 framework
    that excludes ESG reporting controls is likely to be considered inadequate by the FRC.

12. **Accepting generic s.172 statements** — A s.172(1) statement that lists stakeholders
    and describes engagement processes (surveys, town halls) without demonstrating how
    stakeholder interests influenced specific board decisions does not meet the requirement.
    Stakeholder influence must be evidenced against actual decisions.

13. **Failing to assess explanation quality for EXPLAIN findings** — Classifying a finding
    as EXPLAIN and moving on is incomplete. Every EXPLAIN finding requires quality
    assessment against the FRC's five-element test. A departure with a weak explanation
    (score below 9/15) creates reputational and regulatory risk that needs to be flagged.

14. **Treating the chair as subject to no independence requirement** — The chair must
    be independent on appointment (Provision 7). Once appointed, the chair is excluded
    from the independent majority count (Provision 11). These are different requirements
    and both must be assessed separately.

15. **Assuming Audit Reform and Corporate Governance Bill is current law** — The proposed
    ARGA legislation is a draft bill as of the skill's creation date. It would significantly
    expand enforcement powers if enacted. Do not treat the bill's proposals as current
    law; flag as [PENDING LEGISLATION] and note the direction of travel.

16. **Conflating the UK Corporate Governance Code with the QCA Code** — AIM-listed
    companies are not required to follow the FRC Code; they may follow the QCA Corporate
    Governance Code instead. Do not apply this skill to AIM-listed company governance
    without confirming the company has voluntarily adopted the FRC Code.

17. **Ignoring the FCA diversity listing rule obligations** — The 2024 Code removed
    specific diversity metrics, but the FCA Listing Rules (LR 9.8.6R) impose separate
    gender and ethnicity requirements on listed companies. [VERIFY current FCA rules]
    A company may COMPLY with the Code's diversity Provisions while failing to meet
    the separate FCA listing rule requirements. Both must be assessed.

---

## Writing Standards

### For governance compliance reports shared with the board:

- Plain language, no unexplained legal jargon
- Active voice: "The board has not disclosed..." not "It has not been disclosed..."
- Reference specific Provisions by number: "Provision 38 requires..."
- Specific, not vague: cite the disclosure gap or breach explicitly, not in general terms
- No hedging on Priority 1 (RED) findings — these require immediate action, say so clearly

### For comply-or-explain drafting (supporting the company's annual report):

- Company-specific language tailored to the company's precise circumstances
- Forward-looking where appropriate: "The board expects to comply by [date] when..."
- Avoids generic justifications ("in the best interests of shareholders" without specifics)
- Demonstrates why the underlying Principle is met despite the Provision departure

### Quality gates before delivery (5 checks):

1. Does the report distinguish between Priority 1 (immediate), Priority 2, and Priority 3
   findings clearly?
2. Is every EXPLAIN finding supported by a five-element quality score?
3. Are all Provision references accurate (correct number, correct Code version)?
4. Is the Provision 29 effective date correctly applied?
5. Are FTSE 350 thresholds correctly applied to the company's size?

---

## External Tool Integration

### With legalcode-mcp connected (preferred):

- In Step 4, search for: current FRC Code text, FRC Minimum Standard, FCA Listing Rules
  LR 9.8.6R, Companies Act 2006 s.172, Large and Medium-sized Companies Regulations 2008
- Save results to `/tmp/legalcode-uk-cgc-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail
- Search for the most recent FRC Annual Review of Corporate Governance Reporting to
  calibrate findings against current FRC monitoring priorities

### Without legalcode-mcp:

- Mark all Code Provision references with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed using the Provision analysis embedded in this skill
- Flag that all citations require independent verification against current FRC publications

### FRC monitoring resources:

- FRC Annual Review of Corporate Governance Reporting (published annually, November)
- FRC Corporate Governance Code 2024 and Guidance (frc.org.uk)
- FRC Minimum Standard: Audit Committees and External Audit (May 2023)
- Investment Association Shareholder Priorities (published annually)

---

## Output Format Template

````markdown
# UK Corporate Governance Code 2024 — Compliance Review

## [Company Name] | Annual Report [Year] / Financial Year [dates]

**Review date**: [date]
**Code version**: UK Corporate Governance Code 2024 (FRC, 22 January 2024)
**Provision 29 status**: [In scope / Preparatory year / Not yet effective]
**Review purpose**: [e.g., Annual report preparation / Gap analysis / FRC readiness]
**Review basis**: Materials provided: [list materials reviewed]

---

## Executive Summary

**Compliance overview**: [X Provisions COMPLIANT | Y PARTIAL | Z NON-COMPLIANT | W EXPLAIN]

**Priority 1 findings** (immediate action required):

- [Provision N — brief description — action required]
- [...]

**Key strengths**:

- [What the company does well]

**Most significant gaps**:

- [Top 3 gaps with business context]

---

## Section-by-Section Compliance Assessment

### Section 1: Board Leadership and Company Purpose

| Provision | Requirement (Summary)                | Status                                    | Confidence | Key Finding        |
| --------- | ------------------------------------ | ----------------------------------------- | ---------- | ------------------ |
| 1         | Culture assessment and embedding     | [COMPLIANT/PARTIAL/NON-COMPLIANT/EXPLAIN] | [level]    | [one-line finding] |
| 2         | Outcome-based governance reporting   |                                           |            |                    |
| 3         | Stakeholder engagement / s.172       |                                           |            |                    |
| 4         | AGM poll; significant vote follow-up |                                           |            |                    |
| 5         | Chair meets major shareholders alone |                                           |            |                    |

### Section 2: Division of Responsibilities

| Provision | Requirement (Summary)                    | Status | Confidence | Key Finding |
| --------- | ---------------------------------------- | ------ | ---------- | ----------- |
| 6         | Chair/CEO separation                     |        |            |             |
| 7         | Chair independence; no former CEO        |        |            |             |
| 8         | Senior Independent Director appointed    |        |            |             |
| 9         | NEDs meet without chair annually         |        |            |             |
| 10        | Independence of each NED stated          |        |            |             |
| 11        | Majority of board (ex-chair) independent |        |            |             |
| 12        | Chair not on audit/rem/nom committees    |        |            |             |
| 13        | NED time commitments disclosed           |        |            |             |

### Section 3: Composition, Succession and Evaluation

| Provision | Requirement (Summary)                             | Status | Confidence | Key Finding |
| --------- | ------------------------------------------------- | ------ | ---------- | ----------- |
| 14        | Nomination committee established                  |        |            |             |
| 15        | Nom com majority independent; chair rule          |        |            |             |
| 16        | Skills and capability assessment                  |        |            |             |
| 17        | NED terms; six-year and nine-year reviews         |        |            |             |
| 18        | Nomination committee work described               |        |            |             |
| 19        | Chair tenure ≤ nine years                         |        |            |             |
| 20        | Independence override explained                   |        |            |             |
| 21        | External performance review ≤ every 3 years       |        |            |             |
| 22        | Performance review scope (diversity, composition) |        |            |             |
| 23        | Diversity policy, objectives, progress            |        |            |             |

### Section 4: Audit, Risk and Internal Control

| Provision | Requirement (Summary)                            | Status | Confidence | Key Finding |
| --------- | ------------------------------------------------ | ------ | ---------- | ----------- |
| 24        | Audit committee composition                      |        |            |             |
| 25        | Audit committee responsibilities (FRC Min. Std.) |        |            |             |
| 26        | Audit committee work described                   |        |            |             |
| 27        | Ongoing risk/internal control monitoring         |        |            |             |
| 28        | Internal audit function or annual review         |        |            |             |
| 29        | Internal controls declaration [if in scope]      |        |            |             |
| 30        | Going concern in all interim statements          |        |            |             |
| 31        | Viability statement                              |        |            |             |

### Section 5: Remuneration

| Provision | Requirement (Summary)                                  | Status | Confidence | Key Finding |
| --------- | ------------------------------------------------------ | ------ | ---------- | ----------- |
| 32        | Remuneration committee composition                     |        |            |             |
| 33        | Delegated authority for exec pay                       |        |            |             |
| 34        | Remuneration committee work described                  |        |            |             |
| 35        | Remuneration consultant identified                     |        |            |             |
| 36        | Share awards: 5-year vesting; phased release           |        |            |             |
| 37        | Malus/clawback in binding contracts                    |        |            |             |
| 38        | Malus/clawback disclosure (circumstances, period, use) |        |            |             |
| 39        | Workforce pay considered in exec pay                   |        |            |             |
| 40        | Workforce pay conditions in annual report              |        |            |             |
| 41        | Significant vote against: shareholder engagement plan  |        |            |             |

---

## Detailed Findings — Priority 1 (Immediate Action)

### Provision [N] — [Status] — [Priority]

**Code requirement**: [Exact or paraphrased Provision text]
**Current position**: [What the materials show / do not show]
**Gap**: [Specific deviation]
**Risk**: [What happens if not addressed: FRC scrutiny / investor pressure / regulatory action]
**Recommended action**: [Specific, actionable step]
**Owner**: [Board / Audit Committee / Remuneration Committee / Company Secretary / External Counsel]
**Deadline**: [Before annual report filing / Before next AGM]
**Confidence**: [Level] — [Basis]

[Repeat for each Priority 1 finding]

---

## Detailed Findings — Priority 2 and Priority 3

[Same format as Priority 1 findings, grouped by priority]

---

## Comply-or-Explain Quality Assessment

### Provision [N] — EXPLAIN — Quality Score: [X]/15

| Element         | Score (1–3) | Assessment                                             |
| --------------- | ----------- | ------------------------------------------------------ |
| Background      |             |                                                        |
| Rationale       |             |                                                        |
| Impact          |             |                                                        |
| Risk mitigation |             |                                                        |
| Time-frame      |             |                                                        |
| **Total**       | **/15**     | [ADEQUATE ≥ 12 / NEEDS REVISION 9–11 / INADEQUATE < 9] |

**Recommended revision**: [Specific guidance on how to improve the explanation]

---

## Internal Controls Readiness Assessment (Provision 29)

**Effective from**: [Financial year beginning 1 January 2026]
**Company status**: [Year beginning [date] — [in scope / preparatory year]]

| Readiness Step                                      | Status          | Gap / Recommendation |
| --------------------------------------------------- | --------------- | -------------------- |
| Principal risks identified                          | ✓ / ✗ / Partial |                      |
| Material controls mapped to risks                   |                 |                      |
| Monitoring processes documented                     |                 |                      |
| Internal audit coverage adequate                    |                 |                      |
| External assurance scope assessed                   |                 |                      |
| Board has reviewed framework effectiveness          |                 |                      |
| ESG/sustainability controls in scope                |                 |                      |
| Interim financial statements updated (Provision 30) |                 |                      |

**Overall readiness**: [Early stage / In progress / Advanced / Compliant (if in scope)]

---

## Governance Compliance Roadmap

### Priority 1 — Before Annual Report Filing

| Action | Owner | Provision | Effort |
| ------ | ----- | --------- | ------ |
|        |       |           |        |

### Priority 2 — Before Next AGM

| Action | Owner | Provision | Effort |
| ------ | ----- | --------- | ------ |
|        |       |           |        |

### Priority 3 — Within 12–36 Months

| Action | Owner | Provision | Effort |
| ------ | ----- | --------- | ------ |
|        |       |           |        |

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-uk-corporate-governance-code"
  code_version: "UK Corporate Governance Code 2024 (FRC, 22 January 2024)"
  company: "[company name or 'Confidential']"
  financial_year: "[start date — end date]"
  provision_29_in_scope: "[Yes / No / Preparatory — effective [date]]"
  company_size: "[FTSE 100 / FTSE 250 / FTSE 350 / Smaller listed / Investment fund]"
  review_purpose: "[Annual report / Gap analysis / FRC readiness / Other]"
  materials_reviewed:
    - "[Annual report year X]"
    - "[Board committee terms of reference]"
    - "[Other documents]"
  provisions_assessed: "[number out of 41]"
  compliance_summary:
    compliant: "[number]"
    partial: "[number]"
    non_compliant: "[number]"
    explain: "[number]"
  priority_1_findings: "[number]"
  legalcode_mcp: "[Connected / Not connected]"
  authority_reference_file: "[/tmp/legalcode-uk-cgc-authority.md / Not created]"
  statutes_consulted:
    - "UK Corporate Governance Code 2024 — [VERIFIED / UNVERIFIED]"
    - "Companies Act 2006 s.172 — [VERIFIED / UNVERIFIED]"
    - "FRC Minimum Standard: Audit Committees and External Audit (May 2023) — [VERIFIED / UNVERIFIED]"
  self_interrogation: "[PASS / REVISED / NOT APPLICABLE (no Priority 1 findings)]"
  comply_or_explain_quality: "[number] explanations assessed; [number] adequate (≥12/15)"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "Review based on materials provided — board practices not independently verified"
    - "Provision 29 preparatory assessment only — declaration not yet required"
    - "[Other scope limitations]"
  reviewer: "AI-assisted — requires qualified governance counsel review before use"
```
````

---

## Localization Notes

This skill applies specifically to the UK (England and Wales). Key localization points:

- **Scotland**: The CA 2006 and the Code apply equally to companies incorporated in
  Scotland and listed on the UK Official List. Scottish law concepts (e.g., CREST
  settlement) are not materially relevant to Code compliance.
- **Channel Islands / BVI / Cayman Islands incorporation**: Many London-listed companies
  are incorporated offshore. The Code applies based on listing status, not incorporation
  jurisdiction. The Companies Act 2006 obligations (s.172, strategic report) apply
  only to UK-incorporated entities — verify applicable statutory obligations for
  offshore-incorporated companies separately.
- **AIM-listed companies**: The FRC Code does not apply. AIM Rule 26 requires AIM
  companies to disclose their chosen corporate governance code (typically QCA Code).
  Do not apply this skill to AIM companies without confirming voluntary FRC Code adoption.
- **Closed-ended investment funds**: The 2024 Code scope expanded to include this
  category. Investment trusts and other closed-ended funds should apply the Code in
  the context of their typically externally managed structure. Some Provisions (e.g.,
  remuneration) require adaptation for externally managed funds where the fund's board
  does not employ executives directly.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on:

- UK Corporate Governance Code 2024 (FRC, 22 January 2024)
- Corporate Governance Code Guidance (FRC, January 2024, updated March 2026)
- FRC Minimum Standard: Audit Committees and External Audit (May 2023)
- FRC Annual Review of Corporate Governance Reporting 2024 (November 2024)
- FCA Listing Rules LR 9.8.6R diversity requirements
- Companies Act 2006 (ss.171–177, s.172)
- Large and Medium-sized Companies Regulations 2008 (as amended 2019)
- Companies (Miscellaneous Reporting) Regulations 2018
- Law firm analysis: Norton Rose Fulbright, Ashurst, EY, PwC, DLA Piper, KPMG,
  Skadden, Freshfields, White & Case, Davis Polk, Reed Smith

Assembled using the Legalcode 2-agent research pipeline: structural analysis of the
legalcode-contract-review reference standard + deep web research on UK CGC 2024.
Attribution: Legalcode original synthesis.
