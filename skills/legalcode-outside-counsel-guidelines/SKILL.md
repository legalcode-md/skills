---
name: legalcode-outside-counsel-guidelines
description: Draft, update, or audit outside counsel guidelines (OCGs) — the overarching billing and conduct
  policies governing law firm relationships for corporate legal departments. Use when a legal ops team
  needs an OCG, when an existing OCG needs updating to reflect AFA trends or AI provisions, when a law
  firm needs to understand client billing expectations, or when invoices are under dispute.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Draft, update, or audit outside counsel guidelines (OCGs) — the overarching billing and conduct policies governing law firm relationships for corporate legal departments. Covers billing rates, staffing requirements, block-billing prohibition, expense policies, budget management, LEDES/UTBMS e-billing compliance, alternative fee arrangements (AFAs), diversity and inclusion reporting, performance scorecards, AI and technology provisions, and enforcement mechanisms. Supports two modes: (1) Draft or update an OCG from scratch for a legal department or organization, and (2) Audit existing outside counsel invoices or billing practices against an established OCG. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers for local billing ethics rules. Use when a legal ops team needs an OCG, when an existing OCG needs updating to reflect AFA trends or AI provisions, when a law firm needs to understand client billing expectations, or when invoices are under dispute. Also triggers on: billing guidelines, outside counsel policy, legal billing guidelines, law firm billing rules, LEDES invoice, UTBMS codes, legal spend management, matter budgets, convergence programs, AFA negotiation.


# Legalcode Outside Counsel Guidelines

> **Disclaimer**: This skill provides a framework for AI-assisted drafting and review of
> outside counsel guidelines. It does not constitute legal advice. All outputs should be
> reviewed by a qualified legal professional licensed in the relevant jurisdiction before
> use. Billing ethics rules and professional responsibility standards vary by jurisdiction
> and bar association — verify current applicability before relying on any provision
> described here. Statutory and professional responsibility references cited from memory
> carry hallucination risk — verify against authoritative sources before relying on them.

---

## Purpose and Scope

This skill enables AI-assisted drafting, updating, and auditing of **outside counsel
guidelines (OCGs)** — the foundational policy documents that corporate legal departments
use to govern billing practices, staffing, and conduct for all retained law firms.

**Covers:**

- Drafting a complete OCG from scratch or updating an existing one
- Auditing outside counsel invoices against OCG requirements
- LEDES/UTBMS format compliance analysis
- Alternative fee arrangement (AFA) provision design
- Diversity and inclusion requirement structuring
- Enforcement mechanism design (penalty reductions, rejection procedures, appeals)
- Professional responsibility boundary analysis (MRPC Rules 1.5, 1.6, 1.7, 1.8, 5.4)
- Performance scorecard design

**Does not:**

- Provide legal advice or replace qualified legal counsel or bar ethics opinions
- Draft the underlying engagement letters or matter-specific scopes of work
- Guarantee that OCG provisions are enforceable in every jurisdiction
- Apply to any single jurisdiction exclusively — jurisdiction-agnostic with
  [JURISDICTION-SPECIFIC] markers

**Two operating modes:**

- **Mode A — Draft/Update**: Create a new OCG or revise an existing one to current
  market standards
- **Mode B — Billing Compliance Audit**: Analyze invoices or billing practices against
  an existing OCG and generate a compliance report

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The OCG's own governing law clause determines
which professional responsibility rules apply to outside counsel. Billing ethics rules
are set by bar associations in the jurisdiction where the firm practices — these are
distinct from the OCG's contractual terms.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- Bar association guidance on fee reasonableness (e.g., MRPC Rule 1.5 [US]; SRA
  Transparency Rules [UK]; LSC [AU])
- Mandatory billing disclosure requirements for the jurisdiction
- Currency, tax (VAT/GST), and cross-border invoice requirements
- Data protection rules governing demographic diversity data collection (GDPR/UK GDPR
  restrict collection of individual diversity data — adapt diversity provisions accordingly)
- Local labor and employment rules that affect staffing provisions
- Professional indemnity/malpractice requirements that affect insurance provisions

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming the user's intent, the workflow pauses and asks when:

- The answer would change the direction of drafting or the scope of analysis
- Multiple valid approaches exist and organizational preferences matter
- Business context is needed to calibrate enforcement mechanisms correctly
- Mode selection (Draft vs. Audit) or scope is ambiguous

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

### Step 1: Accept Input and Determine Mode

Accept input in any of these formats:

- **Existing OCG document**: PDF, DOCX, or pasted text of an OCG to update or against
  which to audit invoices
- **Sample invoices**: LEDES files, PDFs, or pasted invoice data for compliance audit
- **Organization description**: Name, industry, spend volume, panel size for new OCG
- **Specification**: List of requirements or gaps to address

**⟁ CLARIFY** — Determine the operating mode:

1. **Mode A — Draft/Update OCG**: Create or substantially revise an OCG
   - Sub-options: Draft from scratch, Update an existing OCG, Create a targeted
     addendum (e.g., AI/technology provisions only)
   - _Why this matters_: Determines whether to generate a complete 14-section OCG or
     a focused amendment.

2. **Mode B — Billing Compliance Audit**: Review invoices or current practices against
   an existing OCG
   - Sub-options: Full invoice audit, Specific violation analysis, OCG gap analysis
     (assess whether the OCG itself meets current market standards)
   - _Why this matters_: Determines whether output is a new OCG document or a
     compliance report with remediation recommendations.

If no input document is provided and the user describes an organization, default to
**Mode A — Draft from scratch**.

---

### Step 2: Gather Organization Context

**⟁ CLARIFY** — Gather the following context before proceeding. Present as structured
options where possible:

1. **Organization type**:
   - Options: Fortune 500 corporate legal department, Financial institution (bank /
     insurer / investment bank), Government agency, University / academic medical
     center, Other (describe)
   - _Why this matters_: Determines regulatory overlay (government agencies have
     special contracting requirements; financial institutions have heightened conflict
     rules; universities may have special public records considerations).

2. **Annual outside counsel spend**:
   - Options: Under $1M, $1M–$10M, $10M–$50M, $50M–$250M, Over $250M
   - _Why this matters_: Determines appropriate penalty structures, AFA sophistication,
     and convergence panel provisions. High-spend departments justify more elaborate
     enforcement mechanisms and volume-based discounts.

3. **Law firm panel size**:
   - Options: Under 10 firms, 10–25 firms, 25–50 firms, Open panel (no limit), Unknown
   - _Why this matters_: Convergence programs require specific OCG provisions; open
     panels need simpler onboarding provisions.

4. **E-billing platform** (if Mode A):
   - Options: Brightflag, LegalTracker (Thomson Reuters), eBillingHub, Tymetrix 360,
     Collaborati (Mitratech), SimpleLegal (Onit), None / manual, Unknown
   - _Why this matters_: LEDES format requirements and automated enforcement provisions
     depend on the platform. Platform-specific submission procedures go in the OCG.

5. **Priority provisions** (select all that apply):
   - Options: Block billing enforcement, Staffing controls, Expense reduction,
     AFA adoption, Diversity requirements, AI/technology provisions, Budget discipline,
     Performance scorecards, Conflict of interest controls, Professional responsibility
     clarifications
   - _Why this matters_: Lets the drafting lead with the client's most pressing concerns.

6. **Existing OCG** (for Mode A — Update):
   - Provide the existing document. If absent, state the approximate age of the current
     OCG and any known gaps.
   - _Why this matters_: Determines extent of revision needed and preserves
     organization-specific provisions.

If partial context is provided, proceed and **state assumptions explicitly**.

---

### Step 3: Research Applicable Billing Ethics and Market Standards

Use **legalcode-mcp** to research jurisdiction-relevant billing ethics rules and
professional responsibility standards that constrain OCG provisions.

**Research process:**

1. **Identify the governing jurisdiction(s)** for outside counsel professional
   responsibility (typically the jurisdiction(s) where retained firms are licensed).

   **⟁ CLARIFY** — If the organization retains firms in multiple jurisdictions:
   - Ask whether to draft a single unified OCG applying to all jurisdictions (with
     [JURISDICTION-SPECIFIC] carve-outs), or
   - Separate OCGs per jurisdiction.
   - For most organizations: a single unified OCG with jurisdiction-specific annexes
     for non-US counsel is the most practical approach.

2. **Search legalcode-mcp** for:
   - Bar ethics opinions on billing practices in the primary jurisdiction
   - Case law on OCG enforceability (treatment as contract vs. unilateral policy)
   - Professional responsibility rules on fee reasonableness (MRPC 1.5 equivalent)
   - Conflict of interest rules relevant to affiliate definitions (MRPC 1.7 Comment 34)
   - Third-party payer rules (MRPC 1.8(f)) where client pays for matters benefiting another
   - [JURISDICTION-SPECIFIC] data protection laws governing diversity data collection

3. **Save relevant results** to `/tmp/legalcode-ocg-authority.md`:

   ```markdown
   # Legal Authority — Outside Counsel Guidelines

   ## Organization: [name]

   ## Date: [date]

   ### Billing Ethics Rules

   - [Bar rule, jurisdiction, relevance to OCG provision]

   ### OCG Enforceability Case Law

   - [Case, citation, holding]

   ### Professional Responsibility Constraints

   - [Rule, jurisdiction, impact on OCG drafting]

   ### Diversity Data Protection Rules

   - [GDPR / local law, restriction on demographic data collection]
   ```

**If legalcode-mcp is not connected:**

- Proceed with analysis using general knowledge of MRPC and market standards
- Mark all professional responsibility references with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected — verify all PR citations"`

---

### Step 4: Draft or Audit Core Rate and Staffing Provisions

#### Mode A — Draft

Draft **Sections 1–3** of the OCG using the **OCG Provision Analysis Framework** below:

- **Section 1 — Scope and Applicability**: Define which matters, entities, and
  personnel are covered; affiliate and subsidiary treatment; acknowledgment mechanism.
- **Section 2 — Billing Rates and Rate Approval**: Pre-approval requirement, rate
  freeze period, annual increase process, most-favored-nation (MFN) clause, first-year
  associate/law clerk policy.
- **Section 3 — Staffing Requirements**: Timekeeper pre-approval, team size caps,
  experience matching, one-lead-partner rule, staffing continuity, daily hour caps.

Apply market data from the research phase. Default to:

- Rate freeze: 24 months between increases
- Annual increase request deadline: November 1 for January 1 effective date
- Team size: Maximum 3 timekeepers without pre-approval
- First-year associates: non-compensable or require written approval

**⟁ CLARIFY** — For high-spend organizations ($50M+ annual spend):

- Should the OCG include a most-favored-nation (MFN) clause requiring the firm to
  charge no more than its lowest rate to any other client for the same work?
- Should the OCG include volume-tier discounts based on annual spend thresholds?
- _Why this matters_: MFN and volume tiers are appropriate for large buyers but may
  chill relationships with specialty boutiques where the organization is not a major client.

#### Mode B — Audit

Analyze the existing OCG's rate and staffing provisions against the **COMPLIANT /
PARTIAL / NON-COMPLIANT** classification (see below). Flag:

- Missing timekeeper pre-approval requirement
- Absence of rate freeze period
- No first-year associate policy
- No daily billing hour cap
- No team size limit

---

### Step 5: Draft or Audit Billing Practice Requirements

#### Mode A — Draft

Draft **Section 4 — Billing Practices**, covering:

1. **Block billing prohibition**: Define block billing (combining multiple tasks in a
   single time entry without per-task allocation); specify the penalty (e.g., 10–15%
   reduction on the affected line item or invoice).

2. **Time increment requirement**: Require billing in 0.1-hour (6-minute) increments
   as the current market standard. Prohibit minimum billing increments greater than 0.1
   hour per task.

3. **Contemporaneous timekeeping**: Require daily time entry; prohibit retroactive
   reconstruction of time entries beyond a defined period (typically 5 business days).

4. **Time entry description quality**: Require sufficiently descriptive entries; prohibit
   vague descriptions ("For services rendered," "Review documents," "Telephone call").

5. **Invoice submission deadlines and late billing penalties**: Specify monthly invoice
   cycle; set penalty tiers for late invoices. Draft market-standard tier structure:
   - 31–60 days late: 10% reduction
   - 61–90 days late: 25% reduction
   - 91–180 days late: 50% reduction
   - 181+ days late: non-compensable

6. **Invoice format**: Require LEDES format (specify version — see LEDES/UTBMS section);
   require UTBMS task, activity, and expense codes.

7. **Internal communications**: Set cap or guidance on billing for internal team meetings,
   supervision, and knowledge transfer.

**⟁ CLARIFY** — On late billing penalties:

- Should the penalty structure be automatic (applied by the e-billing platform without
  discretion) or subject to a waiver process?
- _Why this matters_: Automatic penalties are administratively efficient but may create
  disputes with key firms. A waiver process preserves relationship flexibility but
  requires manual oversight.

#### Mode B — Audit

For each invoice reviewed, check:

- Block billing instances (multiple tasks in one entry, no per-task time)
- Entries billed in increments > 0.1 hour
- Vague or non-descriptive entries
- Invoice submission date vs. service period end date (calculate lateness)
- Missing UTBMS codes on line items
- Apply applicable penalty reductions per the OCG's terms

---

### Step 6: Draft or Audit Expense and Budget Provisions

#### Mode A — Draft

Draft **Section 5 — Expense Policy** and **Section 6 — Budget Management**:

**Expense Policy provisions:**

Classify expenses in three tiers:

_Non-Reimbursable (per se)_: List all charges outside counsel may not pass through.
Standard non-reimbursable list includes:

- Copying, printing, word processing, facsimile, telephone, postage
- File organization, binders, calendaring, docketing, conflict checks
- Opening/closing matters, preparing budgets or accruals
- Basic legal research within the firm's core competency
- Training of junior or replacement staff
- Local travel under [threshold, e.g., 50 miles]
- Support staff overtime and meals (unless traveling on client business)
- Subscriptions, books, treatises, periodicals (without pre-approval)
- AI tool subscription costs and software licensing fees

_Reimbursable with Pre-Approval_: Expenses requiring advance written consent:

- Any single expense or category exceeding the pre-approval threshold (draft:
  $300–$1,000 depending on organization)
- Business/first-class airfare (always require pre-approval; default economy/coach)
- Hotel accommodations exceeding a per-night cap (draft guidance: $250–$350 USD
  mid-range; [JURISDICTION-SPECIFIC] for local market rates)
- Meal expenses exceeding a daily cap (draft guidance: $100–$150 USD/day)
- Expert witnesses, litigation support vendors, local counsel

_Reimbursable as Incurred_: Standard litigation/transaction disbursements:

- Court filing fees, subpoena fees, witness fees
- Deposition and trial transcripts
- Patent/trademark official fees

**Budget Management provisions:**

- Require initial matter budget within 10–15 business days of engagement
- Require phase-by-phase budget breakdown (L100–L600 phases for litigation; P100–P600
  for transactions)
- Require proactive budget alerts at 70% and 90% consumed
- Require revised budget estimate before exceeding budget
- Require monthly accrual submissions by [first business day of each month]
- Late accrual penalty: [5%] reduction on next invoice if submitted late more than
  twice in a calendar year

**⟁ CLARIFY** — On budget management:

- Does the organization want to require **phase-by-phase** budgets (more granular
  control) or **matter-level** budgets (less administrative burden)?
- Should the OCG include a **budget overrun approval process** (no work exceeding
  budget without written approval) or a **notification-only process** (flag but don't
  stop work)?
- _Why this matters_: Budget overrun approval gives maximum cost control but risks
  creating conflicts during critical matter phases (trials, closings) if approvals are slow.

#### Mode B — Audit

Check each invoice for:

- Non-reimbursable expense codes (E101–E108 per UTBMS) billed without pre-approval
- Expenses exceeding the pre-approval threshold without prior written consent
- Business/first-class airfare (E110)
- AI tool charges or software subscription pass-throughs

---

### Step 7: Draft or Audit LEDES/UTBMS and E-Billing Requirements

#### Mode A — Draft

Draft **Section 7 — LEDES and E-Billing Requirements**:

**LEDES Format Requirement**:

Specify the required LEDES format version. Most large corporate clients use:

- **LEDES 1998B**: ASCII pipe-delimited, 24 fields; most widely adopted U.S. standard;
  recommended default for domestic matters
- **LEDES 1998BI**: 52-field international version; use when retaining non-U.S. counsel
  requiring multi-currency or tax support
- **LEDES XML 2.2**: Current XML standard, 206 fields; use when the organization
  requires more granular data or the e-billing platform requires it

**UTBMS Code Requirements**:

Require UTBMS codes on all invoice line items. Draft guidance:

| Code Series                   | Applicable Matters       | Key Categories                                                                             |
| ----------------------------- | ------------------------ | ------------------------------------------------------------------------------------------ |
| **L-Series** (L100–L690)      | Litigation               | L100 Assessment, L200 Pleadings, L300 Discovery, L400 Trial, L500 Appeal, L600 E-Discovery |
| **B-Series** (B100–B400)      | Bankruptcy               | B100 Administration, B200 Operations, B300 Claims                                          |
| **C-Series** (C100–C400)      | General Counseling       | C100 Fact Gathering, C200 Research, C300 Advice                                            |
| **P-Series** (P100–P800)      | Transactions             | P200 Due Diligence, P400 Document Prep, P500 Negotiation, P600 Closing                     |
| **PA-Series** (PA100–PA740)   | Patent Prosecution       | PA300 Domestic Prosecution, PA500 International                                            |
| **I-Series** (I110–I990)      | IP (Trademark/Copyright) | I310 Prosecution, I410 Opposition, I510 Post-Issuance                                      |
| **A-Series** (Activity Codes) | All                      | A103 Draft/Revise, A104 Review/Analyze, A106 Client Communication                          |
| **E-Series** (Expense Codes)  | All                      | E110 Travel, E112 Court Fees, E118 Litigation Support, E122 Expert Fees                    |

Require task codes (L/B/C/P/PA/I), activity codes (A101–A112), and expense codes
(E101–E131) on all applicable line items. Invoices without required codes may be
rejected or subject to penalty.

**E-Billing Platform Onboarding**:

Specify the organization's e-billing platform and onboarding procedure:

- Firm must complete platform onboarding before submitting first invoice
- Contact: [Legal Operations / Billing Analyst contact]
- Onboarding timeline: [10 business days from engagement confirmation]
- Technical support: [platform support contact]

**Shadow Billing Requirement (for AFA matters)**:

Even under fixed-fee or other alternative fee arrangements, require firms to submit
hourly shadow invoices for tracking and benchmark purposes unless the AFA agreement
explicitly waives this requirement.

**⟁ CLARIFY** — For Mode A:

- Which specific LEDES version does the e-billing platform require? (If platform is
  known, specify the version required by that platform.)
- Should shadow billing be mandatory for all AFAs, or optional for true fixed-fee matters
  where the scope is clearly defined and closed?

#### Mode B — Audit

For each LEDES invoice, check:

- Correct format version (1998B field count = 24 fields; pipe-delimited; correct line format)
- All line items have a UTBMS task code
- All line items have an activity code (where applicable)
- Expense items use E-series codes
- No L600 e-discovery codes without prior e-discovery protocol agreement

---

### Step 8: Draft or Audit Alternative Fee Arrangement Provisions

#### Mode A — Draft

Draft **Section 8 — Alternative Fee Arrangements**:

**AFA Types Recognized**:

| AFA Type                        | Description                               | Best Use Case                                          |
| ------------------------------- | ----------------------------------------- | ------------------------------------------------------ |
| **Fixed/Flat Fee**              | Predetermined amount for defined scope    | Routine matters with predictable scope                 |
| **Capped Fee**                  | Maximum cost, savings if under cap        | Matters with variable but bounded scope                |
| **Blended Rate**                | Single uniform rate for all timekeepers   | Portfolio of similar matters                           |
| **Success Fee / Success Bonus** | Payment tied to measurable outcome        | Litigation, transactions with clear victory conditions |
| **Holdback with Success Bonus** | Base guarantee + contingent balance       | Complex litigation; aligns firm incentives             |
| **Collared Fee**                | Floor-and-ceiling hybrid                  | Matters with reasonable scope predictability           |
| **Portfolio Pricing**           | Fixed fee for bundle of related matters   | High-volume, repeat-matter type                        |
| **Subscription / Retainer**     | Monthly fixed amount for ongoing services | General counsel support, compliance monitoring         |
| **Contingency**                 | Outcome-based only                        | Plaintiff-side recovery matters only                   |

**Standard AFA Provisions**:

1. Any AFA requires a written AFA agreement signed by [General Counsel / VP Legal Ops]
2. AFA agreement must specify: scope definition, change-order process, shadow billing
   requirement, and exclusions
3. All non-billable, non-reimbursable provisions of this OCG apply to AFA matters
   unless explicitly modified in the written AFA agreement
4. Staffing approval requirements remain in force under all AFA types
5. Budget submission requirements apply to AFA matters; submit a phase-by-phase
   estimate of the work and its equivalent hourly value
6. **Scope creep**: Any work outside the defined AFA scope requires a signed change order
   before work commences; retroactive change orders will not be approved

**AFA Invoice Requirements**:

- AFA invoices must still be submitted in LEDES format where available
- Shadow billing (hourly detail) required unless expressly waived in the AFA agreement
- Milestone-based fee releases must be tied to defined, verifiable deliverables

---

### Step 9: Draft or Audit Diversity, AI, and Performance Provisions

#### Mode A — Draft

Draft **Sections 9–11**:

**Section 9 — Diversity and Inclusion**:

[JURISDICTION-SPECIFIC] Note: Collection of individual demographic data by name or
identifier from law firm timekeepers may be restricted under GDPR (EU/UK), PIPEDA
(Canada), and analogous privacy laws. For non-US counsel, adapt to request firm-level
statistical data only, not individual-level demographic data.

Draft a diversity provision calibrated to the organization's risk tolerance and the
current legal landscape (note 2025 U.S. executive order environment):

_Approach A — Incentive-based (lower legal exposure)_:

- Request voluntary diversity reporting on team staffing for U.S. matters
- Recognize firms with strong diversity performance in annual outside counsel
  designation decisions
- No mandatory percentages or financial penalties

_Approach B — Accountability-based (stronger enforcement)_:

- Require U.S. firms to report annually on: (a) diverse timekeepers on client matters
  by hours percentage, and (b) firm-wide diversity statistics
- Define diversity to include gender identity, race/ethnicity, disability, and
  LGBTQ+ status (consistent with HP/Microsoft precedent)
- Require at least one diverse timekeeper performing a minimum percentage of billable
  hours (draft: 10%) on matters exceeding a spend threshold (draft: $50,000 annually)
- Tie non-compliance to performance scorecard score, not automatic financial penalty,
  to reduce legal exposure

**⟁ CLARIFY** — On diversity provisions:

- Which approach does the organization want: incentive-based, accountability-based, or
  a hybrid?
- Has the organization's legal team reviewed the 2025 executive orders on DEI for
  federal contractor implications?
- _Why this matters_: Organizations with federal contracts face heightened scrutiny;
  mandatory quota-based diversity provisions may expose the organization to legal
  challenge in the current environment.

**Section 10 — AI and Technology Provisions**:

Draft provisions addressing AI tool usage by outside counsel (now standard in all
modern OCGs):

1. **Permitted AI use**: Outside counsel may use AI tools to improve efficiency and
   reduce costs, provided they comply with all confidentiality obligations below.
2. **Confidentiality protection**: Outside counsel must not upload, submit, or expose
   any client confidential information to any AI system not governed by an enterprise
   agreement with adequate confidentiality protections equivalent to attorney-client
   privilege. All AI tools must meet the firm's ethical obligations under [MRPC 1.6 /
   [JURISDICTION-SPECIFIC] equivalent].
3. **Training data prohibition**: Outside counsel must not use any client data,
   documents, communications, or work product to train or improve any AI model.
4. **Human review requirement**: All AI-generated work product must be reviewed and
   validated by a licensed attorney before delivery to the client.
5. **Non-billable AI tools**: Subscription costs, per-query fees, and other costs for
   AI tools are non-reimbursable overhead. Efficiency gains realized through AI use
   should benefit the client, not generate additional billings.
6. **Disclosure obligation**: Outside counsel must disclose to [General Counsel] any
   use of AI tools for client matters upon request.

**Section 11 — Performance Metrics and Scorecards**:

Define the performance scorecard dimensions used for annual outside counsel review:

| Dimension             | Weight | Measurement Basis                                            |
| --------------------- | ------ | ------------------------------------------------------------ |
| Billing Compliance    | 20%    | Invoice bounce-back rate, penalty frequency, LEDES accuracy  |
| Budget Performance    | 20%    | Actual spend vs. budget; accrual accuracy and timeliness     |
| Matter Outcomes       | 25%    | Case/transaction outcomes vs. objectives and cost efficiency |
| Communication Quality | 15%    | Response times, proactive updates, issue escalation          |
| Diversity Reporting   | 10%    | Completion and accuracy of diversity submissions             |
| Value Innovation      | 10%    | AFA proposals, process improvements, cost reduction ideas    |

Conduct annual performance reviews; distribute scorecard results to firm relationship
partners. Scorecards inform annual panel review and matter allocation decisions.

#### Mode B — Audit

Check the existing OCG's diversity and AI provisions:

- Is there a diversity reporting requirement?
- Does the AI provision prohibit training on client data?
- Are AI tool costs designated as non-reimbursable?
- Does the AI provision require human review of AI output?
- Is there a performance scorecard defined?

---

### Step 10: Draft or Audit Enforcement and Professional Responsibility Provisions

#### Mode A — Draft

Draft **Sections 12–14**:

**Section 12 — Conflict of Interest and Professional Responsibility**:

1. **Affiliate treatment**: Specify which entities are treated as the client for
   conflict purposes. [JURISDICTION-SPECIFIC: Under MRPC Rule 1.7 Comment 34, mere
   corporate affiliation does not automatically create a conflict. Maintain a current
   affiliate list; do not make it the firm's responsibility to identify all affiliates.]
2. **Competitive work**: Outside counsel may not represent a party adverse to the
   organization or its listed affiliates without prior written consent.
3. **Professional independence**: Nothing in this OCG shall be construed to interfere
   with outside counsel's independent professional judgment. If any OCG provision
   conflicts with outside counsel's professional responsibility obligations, those
   obligations control. Outside counsel must promptly notify [General Counsel] of any
   such conflict.
4. **Mandatory notification**: Outside counsel must notify the organization within
   [5 business days] of becoming aware of any actual or potential conflict of interest
   affecting any pending or active matter.

**Section 13 — Audit Rights and Compliance Certification**:

1. **Invoice audit**: The organization reserves the right to audit all fees,
   disbursements, and expense reimbursements billed under this OCG, either internally
   or through a third-party legal bill review firm.
2. **Audit frequency**: At minimum annually; more frequently for matters with billing
   irregularities.
3. **Cooperation requirement**: Outside counsel must provide, upon request and within
   [30 business days], all time records, expense receipts, and supporting documentation.
4. **Annual compliance certification**: Each year by [January 31], outside counsel
   must execute a written certification that it has read, understands, and complied
   with this OCG during the prior calendar year.
5. **Reimbursement of overbilled amounts**: Outside counsel must reimburse, within
   [30 days of written notice], any amounts determined to have been billed in violation
   of this OCG.

**Section 14 — Enforcement, Remediation, and Dispute Resolution**:

Draft a tiered enforcement structure:

_Tier 1 — Automatic Adjustments_: Applied by the e-billing platform without prior notice:

- Block billing violation: [10%] reduction on affected invoice
- Late invoice submission per the penalty tier in Section 4
- Missing UTBMS codes: invoice returned for correction

_Tier 2 — Discretionary Adjustments_: Applied by Legal Operations after review:

- Unapproved timekeepers billed: reduction equal to the amount billed by unapproved
  timekeeper(s)
- Unauthorized expenses: charge-back of the specific expense
- Unapproved rate application: reduction to the approved rate

_Tier 3 — Dispute Resolution_:

- Outside counsel may dispute any adjustment within [30 calendar days] of the
  adjustment notice
- Disputes escalated to [General Counsel / Deputy General Counsel] for final determination
- Unresolved disputes subject to [mediation / binding arbitration] under [JAMS / AAA
  Commercial Rules] [JURISDICTION-SPECIFIC]

_Tier 4 — Relationship Consequences_:

- Pattern of non-compliance (3 or more violations in a 12-month period) may result in
  removal from the approved panel or reduction in matter allocations
- The organization reserves the right to terminate any engagement for material
  non-compliance with this OCG upon [30 days'] written notice

**Section 15 — General Terms** (boilerplate):

- Entire agreement (with engagement letter)
- Amendment: OCG may be updated by the organization with [30 days'] notice to all firms
- Severability: If any provision is void or unenforceable, the remainder continues
- Governing law: [JURISDICTION-SPECIFIC]
- Effective date and acknowledgment

**⟁ CLARIFY** — On enforcement:

- Should the OCG require firms to countersign the OCG, or is an acknowledgment email
  or engagement letter reference sufficient?
- _Why this matters_: A countersigned OCG provides clearer contractual enforceability,
  but many large organizations use engagement letter incorporation by reference as a
  practical alternative.

---

### Step 11: Quality Verification

Before delivering the OCG or compliance report, run the following checks:

#### 11a. Completeness Check (Mode A)

Verify all 15 OCG sections are present and complete:

| Section                            | Present | Quality | Notes |
| ---------------------------------- | ------- | ------- | ----- |
| 1. Scope and Applicability         |         |         |       |
| 2. Billing Rates and Rate Approval |         |         |       |
| 3. Staffing Requirements           |         |         |       |
| 4. Billing Practices               |         |         |       |
| 5. Expense Policy                  |         |         |       |
| 6. Budget Management               |         |         |       |
| 7. LEDES/UTBMS E-Billing           |         |         |       |
| 8. Alternative Fee Arrangements    |         |         |       |
| 9. Diversity and Inclusion         |         |         |       |
| 10. AI and Technology              |         |         |       |
| 11. Performance Metrics            |         |         |       |
| 12. Conflict of Interest / PR      |         |         |       |
| 13. Audit Rights                   |         |         |       |
| 14. Enforcement                    |         |         |       |
| 15. General Terms                  |         |         |       |

#### 11b. Professional Responsibility Spot-Check

- [ ] No provision requires outside counsel to violate MRPC 1.5 (fee reasonableness)
- [ ] No provision requires disclosure of confidential client information in violation of
      MRPC 1.6
- [ ] Affiliate/conflict provisions are bounded by a named list, not unbounded
- [ ] Professional independence preservation clause is present (Section 12)
- [ ] No provision could be construed as fee-sharing with a non-lawyer (MRPC 5.4)
- [ ] AI provisions do not conflict with confidentiality obligations

#### 11c. Jurisdiction Accuracy

- [ ] [JURISDICTION-SPECIFIC] markers placed on all provisions that vary by jurisdiction
- [ ] Diversity data collection provisions adapted for GDPR / non-US counsel
- [ ] Dispute resolution clause specifies governing law
- [ ] Currency and tax provisions present for international matters

---

### Step 12: Deliver OCG with Implementation Guidance

Deliver the final OCG (Mode A) or compliance report (Mode B) using the **Output
Format Template** below.

For Mode A, include an **Implementation Checklist**:

- [ ] Legal review by outside counsel (preferably a law firm NOT on the panel)
- [ ] Review for MRPC / bar ethics consistency in primary jurisdiction
- [ ] E-billing platform configuration for automated enforcement rules
- [ ] Distribution to all panel firms with acknowledgment mechanism
- [ ] Internal training for Legal Operations billing analysts
- [ ] Calendar: Annual compliance certification deadline; annual OCG review date
- [ ] Integration reference in all new engagement letters

---

## OCG Provision Analysis Framework

This is the core analytical reference for both Mode A drafting and Mode B auditing.
For each of the 15 OCG sections, the framework defines: what a best-practice provision
covers, the current market standard, common deficiencies, and professional responsibility
constraints.

---

### 1. Scope and Applicability

**Best-practice provision covers:**

- Which matters and retentions are covered (all matters unless explicitly excluded)
- Which entities within the organization are covered (named affiliates and subsidiaries)
- How the OCG is incorporated into the engagement relationship (countersignature,
  engagement letter reference, or online acknowledgment)
- What constitutes acceptance (commencing work = acceptance is common)

**Current market standard:**

- Most large organizations: engagement letter reference + annual compliance certification
- Government agencies and banks: countersignature required
- Annual update notice: 30 days advance notice to all firms

**Common deficiencies:**

- Affiliate list not maintained or updated — creates gaps and conflict rule tensions
- No acknowledgment mechanism — makes OCG harder to enforce as a contract

---

### 2. Billing Rates and Rate Approval

**Best-practice provision covers:**

- Pre-approval of all rates before any work commences
- Rate freeze period (market standard: 24 months minimum between increases)
- Annual rate increase request deadline (market: November 1 for January 1 effective)
- Most-favored-nation clause for high-spend clients
- First-year associate and summer associate billing policy (market: non-compensable)
- Law clerk and paralegal rate tiers

**Current market standard:**

- 15–25% discount off standard rates common for $10M+ relationships
- CPI cap on increases after 24-month freeze period (Yahoo model)
- Fixed rates for life of matter (MongoDB, Yahoo)

**Common deficiencies:**

- No rate freeze period — allows unlimited annual increases
- First-year associates billed at associate rates without client awareness
- No MFN clause — client unaware it is paying more than peers

[JURISDICTION-SPECIFIC] MRPC 1.5 requires fees to be reasonable — OCG rate provisions
must not, in context, produce unreasonable fee outcomes. [VERIFY in relevant jurisdiction]

---

### 3. Staffing Requirements

**Best-practice provision covers:**

- Pre-approval of all timekeepers before billing
- Team size cap (3 timekeepers without approval is current market standard)
- Experience matching (no partners billing for associate-level work)
- Lead counsel continuity (no unilateral staffing changes)
- Prohibition on billing to bring replacement counsel up to speed
- Daily hour cap per timekeeper (8 hours/day with carve-outs for trials, closings)

**Current market standard:**

- MongoDB, Zscaler: 3-person team limit; daily 8-hour cap
- Carve-outs: trials, depositions, M&A signings, securities offerings

---

### 4. Billing Practices

**Best-practice provision covers:**

- Block billing: defined and prohibited with automatic penalty
- Time increment: 0.1-hour (6-minute) minimum; no rounding up
- Contemporaneous billing: daily entry; 5-business-day maximum lag
- Descriptive time entries: task, document name, purpose — not generic labels
- Invoice submission: monthly; aligned with LEDES format
- Late penalty tiers: 31–60 days (10%), 61–90 days (25%), 91–180 days (50%),
  181+ days (non-compensable) — calibrate to organization's preferences

**Current market standard:**

- 0.1-hour increments: universal in Fortune 500 OCGs
- Block billing penalty: 10–15% on affected invoice

---

### 5. Expense Policy

**Best-practice provision covers:**

- Comprehensive non-reimbursable list (copies, admin, basic research, AI tools)
- Pre-approval threshold for discretionary expenses ($300–$1,000 range)
- Travel policy: economy/coach only; business class requires pre-approval with
  documented business necessity; per-day meal cap; hotel pre-approval above threshold
- Receipt requirement above threshold amount ($25–$50 typical)
- Litigation disbursements: court fees, transcripts, expert fees reimbursable

**Common deficiencies:**

- No AI tool non-reimbursable provision (critical omission in post-2023 OCGs)
- No hotel nightly cap — allows luxury hotel charges
- No receipt threshold — creates audit burden

---

### 6. Budget Management

**Best-practice provision covers:**

- Initial budget due within 10–15 business days of engagement
- Phase-by-phase breakdown (UTBMS task phases L100–L600 or P100–P700)
- Budget alert at 70% and 90% consumed
- Revised budget submission required before exceeding budget
- Monthly accrual submission deadline (first business day)
- Late accrual penalty (5% reduction on next invoice after 2 violations)

**Common deficiencies:**

- No phased budget requirement — lump-sum budgets hide cost overruns until late
- No automatic alert requirement — client only discovers overrun on invoice receipt
- No accrual obligation — prevents monthly financial close accuracy

---

### 7. LEDES/UTBMS Compliance

**Best-practice provision covers:**

- Specific LEDES version required (1998B for domestic; 1998BI for international)
- All line items must carry UTBMS task, activity, and expense codes
- E-billing platform name and onboarding procedure
- Shadow billing requirement for AFA matters
- Rejection mechanism for non-compliant invoices

**LEDES Versions Quick Reference:**

| Version       | Format               | Fields | Best For                                     |
| ------------- | -------------------- | ------ | -------------------------------------------- |
| LEDES 1998B   | ASCII pipe-delimited | 24     | U.S. domestic; most widely supported         |
| LEDES 1998BI  | ASCII pipe-delimited | 52     | International; single tax support            |
| LEDES XML 2.2 | XML                  | 206    | Complex matters; multi-tax; modern platforms |

**UTBMS Activity Codes (A-Series) — Reference:**

| Code | Description                                     |
| ---- | ----------------------------------------------- |
| A101 | Plan and prepare for                            |
| A102 | Research                                        |
| A103 | Draft/Revise                                    |
| A104 | Review/Analyze                                  |
| A105 | Internal communication (within firm)            |
| A106 | Client communication                            |
| A107 | Outside counsel communication                   |
| A108 | External communication (non-client/non-counsel) |
| A109 | Appearance/Attendance                           |
| A110 | Data/File management                            |
| A112 | Travel                                          |

**UTBMS Expense Codes (E-Series) — Key Codes:**

| Code      | Description                                                                                                                 |
| --------- | --------------------------------------------------------------------------------------------------------------------------- |
| E101–E108 | Administrative (Copying, Printing, Word Processing, Fax, Phone, Online Research, Delivery, Postage)                         |
| E109–E111 | Travel & Meals (Local Travel, Out-of-Town Travel, Meals)                                                                    |
| E112–E117 | Court & Litigation (Court Fees, Subpoena, Witness, Deposition Transcripts, Trial Transcripts, Trial Exhibits)               |
| E118–E123 | Vendors & Experts (Litigation Support, Private Investigators, Arbitrators, Local Counsel, Expert Fees, Other Professionals) |
| E125–E131 | IP Matters (Translation, Drawings, Patent/Trademark Records/Searches/Monitoring/Official Fees/Post-Issuance)                |

---

### 8. Alternative Fee Arrangements

_(See Step 8 above for complete draft guidance)_

**Key provision requirement**: OCG explicitly states all non-billing provisions
(staffing, expense, conflict) apply to AFA matters unless modified in writing.

**Common deficiency**: No change-order process for AFA scope creep — creates disputes
when scope expands beyond fixed-fee definition.

---

### 9. Diversity and Inclusion

**Best-practice provision covers:**

- Annual reporting requirement for U.S. firms (hours percentage by diverse category)
- Firm-level statistical data for international firms (GDPR-compatible)
- Accountability mechanism (scorecard weight or conditional financial incentive)
- Scope of "diversity" defined to include gender, race/ethnicity, LGBTQ+, disability
- GDPR-compatible alternative for non-U.S. timekeepers

**Current market environment (2025–2026):**

- HP model (mandatory 10% fee holdback for non-compliance) under legal review post-2025
  executive orders affecting federal contractors
- Preferred approach: Tie to scorecard/panel decisions rather than automatic fee reduction

---

### 10. AI and Technology Provisions

**Best-practice provision covers:**

- Conditional permission to use AI (must protect confidentiality)
- Explicit prohibition on using client data to train AI models
- Human attorney review requirement for all AI-generated work product
- Non-billable status of AI tool costs
- Disclosure obligation for AI tool use on matters

**This is a critical gap in OCGs drafted before 2023.** Every OCG update should
include AI provisions.

---

### 11. Conflict of Interest and Professional Responsibility

**Best-practice provision covers:**

- Named affiliate list (not open-ended affiliate definition)
- Competitive representation prohibition with consent mechanism
- Professional independence preservation clause
- Mandatory conflict notification timeline
- Outside counsel's professional obligations control over OCG if conflict arises

[JURISDICTION-SPECIFIC] MRPC 1.7 Comment 34 [VERIFY]: representing a corporation does
not automatically mean representing affiliates. Maintain a bounded affiliate list to
avoid unintentionally expanding conflict obligations beyond what MRPC requires.

---

## Provision Classification System

Classify each OCG provision in both Mode A (drafting completeness) and Mode B (billing
compliance) using this three-tier system:

### COMPLIANT — Best Practice

The provision aligns with or exceeds current market standards. No changes needed.

**Examples:**

- 0.1-hour billing increment requirement with explicit prohibition on minimum charges
  greater than 0.1 hour
- Tiered late invoice penalty up to 100% reduction at 181+ days
- Complete non-reimbursable expense list including AI tool costs
- Human review requirement for AI-generated work product

**Action**: Note as a strength; no change needed.

---

### PARTIAL — Present but Deficient

The provision exists but is missing material elements or uses outdated standards.
Should be updated.

**Examples:**

- Block billing prohibition without a defined penalty
- Diversity reporting requirement without GDPR-compatible variant for international firms
- LEDES requirement without specifying the version
- Budget management provision without phased breakdown or alert thresholds
- Expense policy without an AI/technology non-reimbursable clause

**Action**: Identify the specific gap. Draft the missing element. Provide before/after
comparison.

---

### NON-COMPLIANT — Absent or Directly Problematic

A material provision is entirely absent, or an existing provision conflicts with
professional responsibility rules or current market expectations.

**Examples:**

- No block billing prohibition
- No LEDES format requirement
- No AI and technology provision (in any OCG updated before 2023)
- Affiliate definition so broad it conflicts with MRPC 1.7
- Provision requiring disclosure of other clients in violation of MRPC 1.6
- No enforcement mechanism of any kind
- No professional independence preservation clause

**Action**: Draft the missing provision. Flag any professional responsibility conflicts
for bar ethics review. Classify as Priority Tier 1 (see below).

---

## Prioritization Framework

Organize findings by priority for Mode A (update urgency) and Mode B (remediation
urgency):

### Tier 1 — Critical (Address Immediately)

Issues that create direct legal, financial, or ethical exposure:

- Absence of AI/technology provisions (any OCG in use today without them)
- Professional responsibility conflicts (overbroad affiliate definition, confidentiality
  breach requirements)
- No block billing prohibition (primary driver of billing abuse and fee inflation)
- No enforcement mechanism (OCG without teeth has no deterrent value)
- No LEDES/UTBMS requirement (prevents automated invoice auditing)
- No professional independence preservation clause

### Tier 2 — Important (Address in Next Update Cycle)

Issues that materially affect cost control and relationship management:

- Missing or outdated AFA provisions
- Outdated time increment standard (still using 0.25 hours instead of 0.1)
- No budget management provisions or no phased budget requirement
- Diversity provisions incompatible with current legal environment or GDPR
- No performance scorecard defined

### Tier 3 — Enhancement (Consider for Following Update)

Issues that improve the OCG but are not material gaps:

- Shadow billing provision for AFA matters not explicitly stated
- Late accrual penalty provision absent but not causing immediate problems
- Annual compliance certification requirement not formalized
- Convergence panel provisions for organizations with panel programs

**Strategy**: Address Tier 1 items in an immediate OCG amendment. Incorporate Tier 2
and Tier 3 items in the next annual OCG review cycle. Never defer Tier 1 items.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                                | Fail Action                                                  |
| -------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Source**     | Every professional responsibility claim cites a specific Model Rule, bar opinion, or established legal principle    | Add citation or mark "[UNVERIFIED — bar counsel to confirm]" |
| **Format**     | All citations follow a consistent format for the jurisdiction (MRPC rule number, bar opinion number, case citation) | Fix format                                                   |
| **Currency**   | Every cited provision checked for amendments — bar rules and professional responsibility opinions change            | Flag "[CHECK CURRENCY — may have been amended]"              |
| **Domain**     | Analysis stays within scope; no assumptions from unrelated practice areas                                           | Remove or flag out-of-scope analysis                         |
| **Confidence** | Uncertainty about enforceability or bar ethics explicitly stated, not hidden                                        | Add confidence qualifier                                     |

---

### Self-Interrogation for NON-COMPLIANT Items

For any provision classified as NON-COMPLIANT, apply this 3-pass review before
delivering:

**Pass 1 — Legal Chain Integrity**: Does the gap or conflict follow logically from the
cited rule or authority? Is the professional responsibility concern real, or would a
bar authority actually reach this conclusion on these specific OCG terms?

**Pass 2 — Completeness**: Have all relevant Model Rules, bar opinions, and market
standards been considered? Are there jurisdictions where the provision would be
enforceable even if problematic elsewhere?

**Pass 3 — Challenge**: What is the strongest argument that this provision is acceptable
or unproblematic? Under what circumstances might a reasonable general counsel accept
this risk? Is the NON-COMPLIANT classification proportionate, or is this actually
PARTIAL with mitigations?

If any pass reveals a weakness, revise the analysis before delivery. Mark the audit
trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

---

### Confidence Scoring

For each material OCG provision assessment, assign a confidence level:

| Level        | Range     | Meaning                                                              | Action                                                       |
| ------------ | --------- | -------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Definite** | 0.95–1.0  | Clear bar rule, settled market standard, unambiguous OCG requirement | State with confidence                                        |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions                     | State with brief caveat                                      |
| **Probable** | 0.60–0.79 | Good arguments; enforcement varies by jurisdiction                   | State with explicit reasoning and contra-indicators          |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing approaches                            | Flag for general counsel review with both sides              |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative enforceability                               | Do not assert; flag "[UNCERTAIN — ethics counsel to advise]" |

---

## Glass Box Audit Trail

Every OCG deliverable must include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-outside-counsel-guidelines"
  mode: "Draft/Update OCG | Billing Compliance Audit"
  organization: "[Organization name or 'Not disclosed']"
  organization_type: "[Corporate / Financial Institution / Government / Other]"
  annual_spend_tier: "[Under $1M / $1M–$10M / $10M–$50M / $50M–$250M / Over $250M]"
  ocg_sections_analyzed: "[number or 'All 15']"
  sections_compliant: "[number]"
  sections_partial: "[number]"
  sections_non_compliant: "[number — list]"
  legalcode_mcp: "Connected | Not connected — verify all PR citations"
  authority_reference_file: "[path to temp file or 'Not created']"
  pr_rules_consulted:
    - "[MRPC Rule / Bar opinion — VERIFIED or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS | REVISED | NOT APPLICABLE (no NON-COMPLIANT items)"
  tier_1_items: "[number of critical items identified]"
  tier_2_items: "[number of important items identified]"
  tier_3_items: "[number of enhancement items]"
  ai_provisions_present: "Yes | No | Partial"
  ledes_version_specified: "1998B | 1998BI | XML 2.2 | Not specified"
  confidence: "HIGH | MEDIUM | LOW — [rationale]"
  limitations:
    - "[Scope limitations, jurisdiction-specific caveats, assumptions]"
  reviewer: "AI-assisted — requires qualified legal review and bar ethics clearance"
```

---

## Anti-Patterns

What NOT to do when drafting, reviewing, or applying outside counsel guidelines:

1. **Drafting an open-ended affiliate list** — Requiring outside counsel to treat all
   "affiliates and subsidiaries worldwide" as conflicts clients without providing a
   maintained, named list creates unworkable conflict obligations and conflicts with
   MRPC 1.7 Comment 34. Always attach a named affiliate list and update it annually.

2. **Block billing prohibition without a penalty** — A prohibition that has no
   enforcement mechanism is a suggestion, not a rule. Block billing is the most common
   billing abuse; the prohibition must carry an automatic penalty to deter it.

3. **Using 0.25-hour billing increments in 2024+** — The market shifted to 0.1-hour
   (6-minute) increments as the standard for large corporate clients. Permitting
   15-minute increments allows systematic rounding that inflates invoices.

4. **No AI and technology provision** — Any OCG that does not address AI tool usage is
   dangerously incomplete in the current environment. Firms are using AI on client
   matters today; the prohibition on training AI with client data is a minimum
   acceptable provision.

5. **Diversity provisions that conflict with current law** — Following the 2025
   executive orders, mandatory racial quota-based diversity fee penalties carry
   heightened legal exposure for federal contractors. Do not draft provisions that look
   like quota-based incentives without legal review; pivot to scorecard-based or
   incentive-based approaches.

6. **LEDES requirement without specifying the version** — Requiring "LEDES format" without
   specifying 1998B, 1998BI, or XML 2.2 creates invoice submission ambiguity and
   prevents automated e-billing platform configuration.

7. **No shadow billing requirement under AFAs** — Without shadow billing, an organization
   loses visibility into how fixed-fee matters are actually staffed and whether they
   represent good value. This eliminates the data needed for future AFA negotiations.

8. **Omitting the professional independence preservation clause** — An OCG without this
   clause is exposed to challenge as improperly interfering with outside counsel's
   professional judgment. The clause costs nothing to include and is a professional
   responsibility requirement.

9. **Budget notifications only at 100% consumed** — Many OCGs require outside counsel to
   notify only when budget is exceeded. A 70% and 90% alert system gives the
   organization time to adjust strategy, consider settlement, or increase the budget
   proactively — preventing surprise cost overruns.

10. **Treating expense thresholds as absolute without a pre-approval path** — An OCG
    that says "expenses over $300 are non-reimbursable" without providing a pre-approval
    path creates perverse incentives: outside counsel either avoids necessary expenditures
    (like expert witnesses) or ignores the policy. Always pair a threshold with a
    pre-approval mechanism.

11. **Annual OCG updates without advance notice** — Changing billing rules mid-year
    without notice creates disputes over which version applies to existing engagements.
    Always give 30 days advance written notice of OCG changes and specify the effective
    date and whether changes apply to existing or new matters only.

12. **Making the OCG too punitive for boutique or specialty firms** — OCG penalty
    structures designed for large full-service firms can be disproportionate for small
    boutiques handling specialized work. Consider tiering enforcement mechanisms by
    firm size or annual spend level, or allowing a waiver process for high-value
    specialty relationships.

13. **No GDPR carve-out for diversity data on international timekeepers** — Collecting
    individual-level diversity data (name + demographic identifiers) from EU/UK
    timekeepers violates GDPR without specific legal basis. International OCGs must
    request firm-level aggregate statistics only, not individual demographic data.

14. **Enforcement without a dispute process** — An OCG that allows automatic invoice
    reductions without any appeal mechanism may be challenged as fundamentally unfair.
    A 30-day appeal period to the General Counsel is a minimum due process requirement
    and protects the relationship with key firms.

15. **Drafting OCG provisions that require confidentiality disclosures** — Provisions
    requiring law firms to disclose the names of clients in related practice areas or
    competing representations may force firms to violate MRPC 1.6 confidentiality
    obligations. Frame conflict provisions around firm certification, not disclosure,
    to avoid this trap.

16. **Ignoring the OCG-engagement letter integration** — If the engagement letter does
    not reference the OCG (or vice versa), a court may not treat OCG terms as
    contractually binding. Every engagement letter should contain an explicit OCG
    incorporation clause.

17. **No annual review cycle** — OCG provisions become stale quickly (LEDES versions
    change; AI tools evolve; legal environment shifts). ACC/CLOC best practice is to
    review and update OCGs every 18 months. An OCG last updated before 2022 almost
    certainly lacks AI provisions and current LEDES version specifications.

---

## Writing Standards

Apply plain-language discipline to all OCG drafting and compliance analysis:

**For OCG provisions:**

- Use imperative/mandatory language: "Outside counsel must..." not "Outside counsel
  should consider..." — ambiguity in billing policies invites non-compliance
- Be specific about thresholds, deadlines, and penalty amounts — vague rules are
  unenforceable
- Define all key terms in a definitions section (block billing, timekeeper, affiliate,
  matter, diverse attorney)
- Use consistent terminology throughout — do not use "firm" in some places and
  "outside counsel" in others
- Active voice: "Outside counsel must submit invoices by the last day of the month"
  not "Invoices must be submitted by the last day of the month by outside counsel"

**For compliance analysis reports:**

- Plain language accessible to both lawyers and legal operations professionals
- Short sentences; one point per sentence
- Tables for structured comparisons (compliant / partial / non-compliant)
- Specific citations to OCG section numbers when referencing provisions
- Distinguish clearly between factual findings ("Invoice #123 contains block billing
  in 5 line items") and legal assessments ("This violates Section 4(a) of the OCG")

**Quality gates before delivery:**

1. Can a legal operations professional (non-lawyer) understand every provision in
   the OCG?
2. Is every threshold, deadline, and penalty amount specific — no ranges left for the
   reader to fill in?
3. Is every professional responsibility reference either verified or marked [VERIFY]?
4. Are there any vague words like "reasonable," "appropriate," or "timely" that have
   not been defined or quantified?
5. Could any sentence be shorter without losing meaning? If yes, shorten.

---

## External Tool Integration

### legalcode-mcp

Use **legalcode-mcp** as the primary research tool for billing ethics rules and
professional responsibility authority.

**With legalcode-mcp connected (preferred):**

- Search for bar ethics opinions on billing practices in the primary jurisdiction
- Search for case law on OCG enforceability and treatment as contract
- Verify MRPC rule currency and any jurisdiction-specific modifications
- Check for recent bar opinions on AI tool use and billing ethics
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail
- Save results to `/tmp/legalcode-ocg-authority.md`

**Without legalcode-mcp:**

- Proceed with analysis using general MRPC knowledge and market data
- Mark all professional responsibility and bar ethics references with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected — verify all PR citations"`
- Focus on structural completeness and market-standard provisions rather than
  jurisdiction-specific ethics depth

---

## Localization Notes

When adapting this skill to specific jurisdictions:

**United States (federal/state):**

- Primary bar ethics reference: ABA Model Rules of Professional Conduct
- Most states have adopted MRPC substantially; verify state-specific variations
- 2025 executive orders affect federal contractor DEI provisions — consult employment
  counsel for federal contractor clients
- LEDES 1998B is the universal domestic standard

**United Kingdom:**

- Solicitors Regulation Authority (SRA) Transparency Rules govern fee disclosure
- SRA Code of Conduct replaces MRPC; different structure but comparable billing
  ethics principles
- LEDES 1998BI common; XML 2.2 growing
- Diversity data collection: UK GDPR and Equality Act 2010 apply

**European Union:**

- GDPR governs collection of diversity demographic data — individual-level collection
  of racial/ethnic, sexual orientation, and other sensitive data prohibited without
  specific legal basis
- Adapt diversity provisions to request firm-level aggregate data only for EU firms
- National bar association rules apply per member state (CCBE principles provide
  overarching framework)

**Australia:**

- Legal profession uniform law framework (NSW/VIC); state variations elsewhere
- LEDES formats supported; UTBMS adoption growing but not universal
- ACL provisions: OCG terms must not be "unfair contract terms" under ACL consumer
  protection framework

---

## Output Format Template

### Mode A — OCG Deliverable

```markdown
# Outside Counsel Guidelines

## [Organization Name]

**Version**: [X.Y] | **Effective Date**: [date] | **Replaces**: [prior version or "N/A"]

---

## Table of Contents

1. Scope and Applicability
2. Billing Rates and Rate Approval
3. Staffing Requirements
4. Billing Practices
5. Expense Policy
6. Budget Management
7. LEDES and E-Billing Requirements
8. Alternative Fee Arrangements
9. Diversity and Inclusion
10. AI and Technology Provisions
11. Performance Metrics and Scorecards
12. Conflict of Interest and Professional Responsibility
13. Audit Rights and Compliance Certification
14. Enforcement and Remediation
15. General Terms

---

## 1. Scope and Applicability

[Provision text]

## 2. Billing Rates and Rate Approval

[Provision text]

[...continue for all 15 sections...]

---

## Acknowledgment

By commencing work on any matter for [Organization Name], outside counsel acknowledges
receipt of and agreement to comply with these Outside Counsel Guidelines.

[Or: Please execute and return the acknowledgment page by [date].]

---

## Exhibit A — Approved Timekeeper List

[To be completed per matter]

## Exhibit B — Affiliate List (For Conflicts Purposes)

[Maintained by [Legal Operations]; current as of [date]]
```

---

### Mode B — Billing Compliance Audit Report

```markdown
## OCG Compliance Audit Report

**Organization**: [name]
**Outside Counsel Firm**: [firm name]
**Matter(s)**: [matter ID(s) or description]
**Invoices Reviewed**: [number; date range]
**OCG Version Applied**: [version and effective date]
**Audit Date**: [date]

---

## Executive Summary

[2–4 sentences: total invoiced amount, total amount at issue, top 3 violations,
recommended adjustment amount]

---

## Compliance Findings

| #   | Violation Type        | Invoice # | Line Items | Amount at Issue | OCG Section | Classification |
| --- | --------------------- | --------- | ---------- | --------------- | ----------- | -------------- |
| 1   | Block billing         | INV-001   | 5 entries  | $2,340          | §4(a)       | NON-COMPLIANT  |
| 2   | Unapproved timekeeper | INV-002   | 12 entries | $8,400          | §3(b)       | NON-COMPLIANT  |
| ... |                       |           |            |                 |             |                |

**Total amount at issue**: $[X]
**Recommended adjustment**: $[Y] ([X]% of total invoiced amount)

---

## Detailed Findings

### Finding 1 — Block Billing (NON-COMPLIANT) | Confidence: [level]

**OCG provision**: Section 4(a) prohibits block billing and imposes a [10%] penalty
on affected invoices.
**Finding**: [N] time entries in Invoice #[X] combine multiple tasks without per-task
time allocation.
**Examples**:

- "[Entry text]" — [time billed] — tasks: [list]
  **Amount at issue**: $[Y]
  **Recommended adjustment**: $[Z] ([10%] reduction per OCG §4(a))
  **Remediation**: Require firm to resubmit with task-by-task time allocation.

[Repeat for each finding]

---

## OCG Gap Analysis (if requested)

[COMPLIANT / PARTIAL / NON-COMPLIANT assessment of the OCG itself against market
standards, with specific recommendations for Tier 1/2/3 improvements]

---

## Recommended Next Steps

1. [Specific action, owner, deadline]
2. ...

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis built from comprehensive research
on Fortune 500 outside counsel guidelines (MongoDB, Yahoo/Verizon Media, Zscaler,
HP, Microsoft, Google OCG programs), LEDES Oversight Committee format specifications,
UTBMS code registry (utbms.com), ACC guidance on outside counsel management, CLOC
core competency framework, Harbor 2025 Law Department Survey, LegalBillReview.com
2025 legal spend survey, and ABA professional responsibility analysis of OCG-MRPC
interactions. All market data sourced from publicly available research; all professional
responsibility analysis based on ABA Model Rules of Professional Conduct with [VERIFY]
markers on jurisdiction-specific variations. No prior Legalcode skill in this area
— created from scratch via 2-agent research pipeline.
