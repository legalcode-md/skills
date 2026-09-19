---
name: legalcode-board-resolution-drafter
description: 'Drafts board resolutions and unanimous written consents (UWCs) for common corporate actions:
  officer appointments and removals, equity issuances, stock option and warrant grants (ISO/NSO), equity
  incentive plan adoptions, financing approvals (debt facilities, convertible notes, SAFEs, preferred
  rounds), contract authorizations, dividend declarations, bank account authorizations, annual compliance
  resolutions, IP assignments, subsidiary formations, M&A preliminary approvals, and indemnification agreements.
  Use when a company needs a board resolution or written consent for any corporate governance action.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Drafts board resolutions and unanimous written consents (UWCs) for common corporate actions: officer appointments and removals, equity issuances, stock option and warrant grants (ISO/NSO), equity incentive plan adoptions, financing approvals (debt facilities, convertible notes, SAFEs, preferred rounds), contract authorizations, dividend declarations, bank account authorizations, annual compliance resolutions, IP assignments, subsidiary formations, M&A preliminary approvals, and indemnification agreements. Covers recital/WHEREAS and RESOLVED structure, quorum, unanimous consent mechanics, Secretary certification, and corporate formality requirements under Delaware DGCL §141, UK Companies Act 2006, and MBCA. Deep coverage of IRC §409A FMV requirements for equity grants, Rule 701 securities law compliance, and §280G golden parachute analysis triggers. Jurisdiction-agnostic with deep DE/UK/general treatment. Use when a company needs a board resolution or written consent for any corporate governance action. Supports startup, growth-stage, and public company contexts.


# Legalcode Board Resolution Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted drafting of board
> resolutions and unanimous written consents. It does not constitute legal advice. All
> drafts should be reviewed by qualified corporate counsel licensed in the relevant
> jurisdiction before execution or reliance. Corporate governance requirements vary by
> jurisdiction, entity type, charter documents, and bylaws. Statutory and case law
> references cited from memory carry hallucination risk — verify against authoritative
> sources before relying on them.

## Purpose and Scope

This skill drafts board resolutions and unanimous written consents (UWCs) for common
corporate actions. It identifies the correct resolution type, gathers required context,
structures the recital/resolved clauses, and flags corporate authority prerequisites.

**Covers:**

- All common board-authorized corporate actions (see Resolution Type Matrix below)
- Meeting-based board resolutions and unanimous written consents without a meeting
- Quorum and procedural compliance checks
- Secretary certification language
- Corporate authority prerequisite analysis (board-only vs. stockholder approval required)
- Jurisdiction-specific formality requirements (DE / UK / general)
- Tax and securities law triggers for equity and financing actions
- Quality-verified output with Glass Box audit trail

**Does not:**

- Draft stockholder/shareholder resolutions (separate skill)
- Provide legal advice or replace qualified corporate counsel
- File documents with government authorities
- Provide an opinion on the legality of the underlying corporate action

## Jurisdiction and Governing Law

This skill covers three corporate law frameworks in depth:

| Framework          | Statute/Source                                   | Key Resolution Mechanic                                                     |
| ------------------ | ------------------------------------------------ | --------------------------------------------------------------------------- |
| **Delaware**       | DGCL Title 8, Ch. 1                              | Meeting (§141(b) quorum) or UWC (§141(f) — ALL directors must sign)         |
| **UK**             | Companies Act 2006 + Model Articles SI 2008/3229 | Board meeting (Art. 7-8) or written resolution of directors (Model Art. 18) |
| **General / MBCA** | Model Business Corporation Act                   | Meeting with quorum or written consent (MBCA §8.21)                         |

[JURISDICTION-SPECIFIC] When localizing to non-DE/UK jurisdictions, research and apply:

- Local corporate statute requirements for board action without meeting
- Whether UWC requires unanimous or majority director consent
- Quorum reduction rules in the local statute
- Required attachments, notarization, or apostille requirements
- Electronic signature validity (e.g., ESIGN Act / UETA for US; eIDAS for EU)
- Foreign qualification and equivalent resolution requirements

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer changes which type of resolution is required
- Tax or securities law triggers (§409A, Rule 701, §280G) depend on specific facts
- The charter or bylaws may override statutory defaults
- Stockholder approval is required in addition to board approval

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

### Step 1: Accept the Request

Accept the request in any of these formats:

- **Description of the action**: "We need to grant options to three new employees"
- **Specific resolution type**: "Draft a UWC for a Series A financing"
- **List of actions**: Multiple resolutions to be combined in one consent
- **Existing draft for review**: An existing resolution to review and improve

If no specific action is described, prompt the user to identify the corporate action(s)
needing authorization.

### Step 2: Gather Corporate Context

**⟁ CLARIFY** — Before drafting, collect:

1. **Entity and jurisdiction**:
   - Options: Delaware corporation, other US state corporation, UK private limited company
     (Ltd), UK public limited company (Plc), LLC, other
   - _Why this matters_: Different statutes govern UWC mechanics, quorum, and what requires
     stockholder approval. A DE UWC requires ALL directors to sign (§141(f)); an LLC may allow
     manager consent by majority.

2. **Company name and current date**: For the resolution header.

3. **Board composition**: How many directors are on the board? Who is signing?
   - _Why this matters_: A UWC requires ALL current directors to sign under DGCL §141(f).
     If using a meeting format, quorum (majority) is required. A single-director board can
     execute a solo UWC.

4. **Format preference**:
   - Options: **Unanimous Written Consent (UWC)** — action without a meeting, all directors
     must sign; **Board Meeting Minutes** — action at a duly called meeting (special or regular);
     **Written Resolution of Directors** (UK only) — directors' written resolution under
     Model Articles Art. 18
   - _Why this matters_: UWC is faster and most common for startups; meeting minutes are
     required for some investors or when a director will not consent unanimously.

5. **Charter/bylaw authority**: Does the certificate of incorporation or bylaws contain
   special provisions? (e.g., supermajority requirements, reserved matters, board committee
   authority)
   - _Why this matters_: Charter provisions override DGCL defaults. Some actions may require
     supermajority board approval or specific committee sign-off.

### Step 3: Identify the Resolution Type(s)

Classify each requested action using the **Resolution Type Matrix** below. For each action:

- Confirm whether **board approval alone** is sufficient or whether **stockholder/shareholder
  approval is also required**
- Identify any **tax or securities law triggers**
- Note any **prerequisites** (e.g., a current 409A valuation before option grants)

If multiple actions are requested, determine whether they should be combined in a single
consent or separated.

**⟁ CLARIFY** — If the action is ambiguous (e.g., "authorize a financing" — debt? equity?
both?), ask before drafting:

- "Is this a debt financing (loan, line of credit, convertible note) or an equity financing
  (preferred stock round)? Or both?"
- "Approximately how much is being raised? (Affects Rule 701 tracking for equity grants.)"

### Step 4: Check Corporate Authority Prerequisites

Before drafting, confirm that all prerequisites for the action are satisfied or explicitly
addressed in the resolution.

**⟁ CLARIFY** — For equity grants (Step 6 below), ask:

1. "Has the company obtained a current independent 409A valuation? Under IRC §409A,
   the exercise price must equal FMV at grant date. If no 409A report is in place, the
   resolution should not set the exercise price — the board must approve the price after
   receiving a 409A."
2. "Has the equity incentive plan already been adopted and approved by stockholders? An
   option grant references the plan. If no plan exists, we need a plan adoption resolution first."

For stock issuances:

- Confirm the company has sufficient **authorized but unissued shares** of the correct class
  in its certificate of incorporation.
- If authorized shares are insufficient, a certificate amendment (board + stockholder approval
  under DGCL §242) is required first.

### Step 5: Gather Action-Specific Details

For each resolution type, collect the action-specific inputs defined in the
**Resolution Type Reference** section below.

**⟁ CLARIFY** — Present a targeted question set for the specific action type. For example,
for an officer appointment:

- "What is the officer's full name and title (e.g., Chief Executive Officer, Chief Financial
  Officer, General Counsel)?"
- "What is the effective date of appointment?"
- "What authorities do you want to grant this officer? (e.g., sign contracts up to $[X],
  open bank accounts, execute financing documents)"
- "Is there an employment agreement being approved simultaneously?"

### Step 6: Draft the Resolution

Draft the resolution following the **Drafting Standards** section. Structure:

1. **Header** — Entity name, resolution type, and date
2. **Preamble** — Who is taking action (full board / quorum / all directors by written consent)
3. **Recitals** (WHEREAS clauses) — Background facts establishing why the action is appropriate
4. **Resolved Clauses** (RESOLVED, THAT...) — The specific authorizations in operative language
5. **Further Resolved Clauses** — Administrative authorizations (signature authority, further action)
6. **Signature Blocks** — All required signatories with title and date
7. **Secretary's Certificate** (if required by the use case)

### Step 7: Check for Missing Elements

After drafting, run the **Resolution Completeness Checklist** against the draft:

- [ ] Entity name correctly stated in header and preamble
- [ ] Correct resolution type (UWC vs. meeting minutes vs. written resolution)
- [ ] Date of consent / meeting correctly stated
- [ ] All required directors listed and will sign (for UWC)
- [ ] Quorum stated (for meeting minutes)
- [ ] Action-specific required elements present (see Resolution Type Reference)
- [ ] Stockholder approval flag addressed (if required)
- [ ] Tax trigger addressed (§409A, §280G as applicable)
- [ ] Securities law compliance noted (Rule 701, Section 4(a)(2), Regulation D as applicable)
- [ ] "Further Resolved" delegating signing authority to officers
- [ ] Counterparts language (if multiple directors signing separately)
- [ ] Revocation language (for UWC: cannot be revoked once delivered under DGCL §141(f))

### Step 8: Quality Verification

Before delivering the draft:

1. Run the 5 **Citation Quality Gates** silently. Revise failures before delivery.
2. For any **INVALID** classification, run the 3-pass **Self-Interrogation**. Revise if needed.
3. Assign **Confidence Scores** to legal authority claims.
4. Generate the **Glass Box Audit Trail** and append it.

### Step 9: Deliver Draft

Present the final resolution draft with:

- The formatted resolution ready for execution
- A brief completeness summary
- Any prerequisite actions required before execution
- Any items flagged for counsel review
- The Glass Box Audit Trail

---

## Resolution Type Matrix

| #   | Action Type                                     | Board-Only Sufficient?                                                 | Key Prerequisites                                               | Tax/Securities Triggers            |
| --- | ----------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------- |
| 1   | Officer appointment                             | ✅ Yes (DE §142 / CA 2006 s.160 by board)                              | Employment agreement                                            | N/A                                |
| 2   | Officer removal                                 | ✅ Yes                                                                 | Check employment contract severance                             | §280G (if M&A context)             |
| 3   | Common stock issuance                           | ✅ Yes (if authorized shares available)                                | Authorized shares in cert                                       | Section 4(a)(2) / Reg D / Rule 701 |
| 4   | Preferred stock issuance                        | ✅ Board + possibly stockholders for new series                        | Cert of Designation or cert amendment                           | Reg D; accredited investor checks  |
| 5   | Option/warrant grants                           | ✅ Yes (plan must exist; 409A required)                                | Board-approved plan, 409A valuation                             | IRC §409A; Rule 701 aggregate      |
| 6   | Equity incentive plan adoption                  | ✅ Board + stockholder approval (for ISO treatment)                    | N/A                                                             | IRC §422 (ISOs); Rule 701          |
| 7   | Convertible note / SAFE issuance                | ✅ Yes                                                                 | Cap table analysis                                              | Section 4(a)(2) / Reg D            |
| 8   | Debt facility / credit agreement                | ✅ Yes (with lien authority)                                           | UCC-1 authorization                                             | N/A                                |
| 9   | Contract authorization                          | ✅ Yes (within board's authority)                                      | Check dollar threshold vs. bylaws                               | N/A                                |
| 10  | Dividend declaration                            | ✅ Yes                                                                 | Sufficient surplus (DE §170) / distributable profits (UK s.830) | Applicable withholding taxes       |
| 11  | Bank account authorization                      | ✅ Yes                                                                 | N/A                                                             | N/A                                |
| 12  | Annual compliance / organizational              | ✅ Yes                                                                 | N/A                                                             | N/A                                |
| 13  | IP assignment approval                          | ✅ Yes                                                                 | Ownership confirmed                                             | N/A                                |
| 14  | Real estate lease                               | ✅ Yes (unless >X value per bylaws)                                    | Check bylaw thresholds                                          | N/A                                |
| 15  | Subsidiary formation                            | ✅ Yes                                                                 | N/A                                                             | N/A                                |
| 16  | Indemnification agreements                      | ✅ Yes                                                                 | DGCL §145 authority confirmed                                   | N/A                                |
| 17  | M&A — preliminary / LOI                         | ✅ Yes for LOI                                                         | Fiduciary duty analysis                                         | §280G preliminary screen           |
| 18  | M&A — merger/acquisition agreement              | ✅ Board + **stockholder approval required** (DE §251 / CA 2006 s.907) | Fairness opinion; fiduciary duties                              | §280G analysis; HSR filing         |
| 19  | Sale of substantially all assets                | ✅ Board + **stockholder approval required** (DE §271)                 | Fairness consideration                                          | N/A                                |
| 20  | Certificate amendment (authorized shares, etc.) | ❌ Board + **stockholder approval required** (DE §242)                 | N/A                                                             | N/A                                |
| 21  | Dissolution                                     | ❌ Board + **stockholder approval required** (DE §275)                 | N/A                                                             | N/A                                |

> **DE Note**: Under DGCL §228(a), stockholder action may also be taken by written consent
> of stockholders holding a majority of shares, unless the certificate of incorporation
> restricts this. Always check the cert.

> **UK Note**: UK private limited companies may pass written resolutions of shareholders
> (ordinary: >50%; special: ≥75%) under CA 2006 ss.288-295. Written resolutions are NOT
> available to public limited companies (CA 2006 s.288(1)).

---

## Resolution Type Reference

### 1. Officer Appointments and Removals

**Required inputs:**

- Full legal name of the officer
- Title (e.g., Chief Executive Officer, President, Chief Financial Officer, Secretary,
  Treasurer, General Counsel, Chief Operating Officer)
- Effective date
- Authority scope (signing limits, banking, regulatory filings)
- Reference to any related employment agreement (include approval of the agreement itself)
- Removal: reason (if stated), effective date, severance treatment reference

**Statutory basis:**

- DE: DGCL §142(b) — officers appointed by board or as bylaws provide; serve at board's pleasure
  unless term specified; officers may hold multiple titles unless charter/bylaws prohibit
- UK: CA 2006 s.160 — directors appointed at general meeting or by board between meetings;
  company secretary appointed by directors (s.271); managing director under Model Articles Art. 5
- MBCA: §8.40 — corporation has officers described in bylaws or appointed by board

**Drafting notes:**

- Include "serves at the pleasure of the Board of Directors, subject to any applicable
  employment agreement" for flexibility
- For CEO, include authority to bind the company in ordinary course; execute agreements
  up to $[threshold]; open/operate bank accounts
- Secretary appointment: include authority to certify resolutions and corporate records

**Standard resolved clause (officer appointment):**

```
RESOLVED, THAT [Full Name] is hereby appointed to serve as [Title] of the Company,
effective [Date], to hold such office until [his/her/their] successor is duly appointed
and qualified or until [his/her/their] earlier resignation, removal, or death, and to
receive such compensation as shall be determined by the Board of Directors from time
to time.

RESOLVED FURTHER, THAT the [Title] is hereby authorized and directed, on behalf of
and in the name of the Company, to execute and deliver any and all documents,
instruments, and agreements, and to take any and all actions, as [he/she/they] may
deem necessary or advisable to carry out the purposes of the foregoing resolution.
```

---

### 2. Equity Issuances

**Required inputs:**

- Class of stock (Common / Preferred — specify series)
- Number of shares to be issued
- Purchase price per share (must be at or above par value; DE §153)
- Purchaser name(s) and accredited investor status
- Closing date
- Reference to stock purchase agreement / subscription agreement

**Statutory basis:**

- DE: DGCL §152 — consideration for shares fixed by board; DGCL §153 — payment may be in
  cash, property, or past services; par value is minimum (DGCL §154)
- UK: CA 2006 s.549 — directors require authorization to allot shares; s.561 — pre-emption
  rights on allotment (may be disapplied under s.570-571); s.580 — prohibition on issuing
  at a discount to par value
- Securities law: Section 4(a)(2) (private offering) or Regulation D (Rule 506(b)/506(c))
  exemption required; blue sky compliance per state

**Tax / securities triggers:**

- [JURISDICTION-SPECIFIC] Securities: Regulation D Form D must be filed within 15 days of
  first sale under Rule 503 (US). Blue sky filings may be required in each state where
  purchasers reside.
- Rule 701: If issuing equity as compensation (not investment), track aggregate Rule 701
  issuances. Issuances exceeding $10M in any 12-month period trigger enhanced disclosure
  obligations under SEC Rule 701(e). [VERIFY current threshold]
- QSBS: Confirm QSBS eligibility criteria under IRC §1202 if applicable (C-corporation,
  active business, <$50M gross assets at issuance, 5-year holding requirement)

**Drafting notes:**

- Reference the investors' subscription agreement or stock purchase agreement
- Include representations from investors (accredited investor, investment intent)
- For preferred stock new series: reference the Certificate of Designation or amended cert
- Confirm authorized shares in the current certificate of incorporation

---

### 3. Stock Option and Warrant Grants

**⟁ CLARIFY — MANDATORY before drafting option grants**:

"Before drafting an option grant resolution, I need to confirm two prerequisites:

1. **409A Valuation**: Under IRC §409A, the exercise price of any nonqualified stock option
   (NSO) must equal the fair market value (FMV) of the underlying stock on the grant date.
   For ISOs, the same requirement applies under IRC §422(b)(4). Granting options at below-FMV
   creates severe tax consequences for optionees: immediate income inclusion, 20% excise tax,
   and interest charges under IRC §409A(a)(1)(B).
   - Has the company obtained an independent 409A valuation from a qualified appraiser?
   - When was the most recent 409A valuation completed? (A valuation is typically good for
     12 months, or until a material event such as a financing round.)

2. **Equity Incentive Plan**: Are these grants under an existing Board/stockholder-approved
   equity incentive plan? (e.g., '2024 Equity Incentive Plan'). If no plan exists, we need
   a plan adoption resolution first."

**Required inputs (per grantee):**

- Grantee full legal name and title
- Number of option shares
- Type: ISO (Incentive Stock Option) or NSO (Non-Qualified / Non-Statutory Stock Option)
- Exercise price per share (must equal FMV from 409A valuation)
- Grant date (date of board approval)
- Vesting schedule (e.g., 4-year with 1-year cliff and monthly thereafter)
- Post-termination exercise period (typically 90 days for NSO; ISO-specific rules apply)
- Option expiration (maximum 10 years; ISO from grant date)
- Reference to equity incentive plan
- Reference to stock option agreement

**Statutory / regulatory basis:**

- DE: DGCL §157 — board may create and issue options/warrants; grant terms set by board
  resolution or a committee thereof
- IRC §422: ISO requirements: (i) employee of issuer, parent, or subsidiary; (ii) exercise
  price ≥ FMV at grant; (iii) $100,000 annual exercisability limit (per ISO Agreement);
  (iv) plan adopted and approved by stockholders within 12 months; (v) 10-year maximum term;
  (vi) 90-day post-termination exercise window (1 year for disability; no limit for death) [VERIFY]
- IRC §409A: Applies to NSOs and deferred compensation generally; exercise price at or above
  FMV at grant is the safe harbor to avoid §409A application to options
- Rule 701: Compensatory equity issued under Rule 701 exemption from Securities Act registration;
  annual aggregate issuances capped at the greatest of: (i) $1 million; (ii) 15% of the
  issuer's total assets; or (iii) 15% of all outstanding securities of the class being offered,
  in each case measured over the prior 12 months; when aggregate sales in any 12-month period
  exceed **$10 million**, enhanced disclosure obligations are triggered under Rule 701(e),
  including delivery of financial statements and a risk factors summary to all option holders
  before their securities are offered for sale [VERIFY current threshold]

**ISO-specific drafting requirement:**

```
RESOLVED, THAT the grant of an Incentive Stock Option to [Name] is hereby approved,
subject to the terms of the Company's [Plan Name], with the following terms:
  - Number of Shares: [X]
  - Exercise Price: $[X.XX] per share, representing the Fair Market Value of the
    Company's Common Stock as of the Grant Date, as determined by the Board of
    Directors in good faith based on [the independent 409A appraisal dated [Date]
    prepared by [Appraiser Name]]
  - Vesting: [X]% on [Date] (cliff), then [X]% per month/quarter thereafter over [X]
    months, subject to continued service
  - Term: 10 years from the Grant Date, subject to earlier expiration
  - Grant Date: [Date of this resolution]
```

**10% Stockholder rule (ISOs):** For optionees owning >10% of voting stock, the exercise
price must be ≥110% of FMV and the term is capped at 5 years (IRC §422(c)(5)). [VERIFY]

---

### 4. Equity Incentive Plan Adoption

**Required inputs:**

- Plan name and total share reserve
- Types of awards permitted (ISOs, NSOs, RSAs, RSUs, SARs, Performance Awards)
- Plan administrator (Board or Compensation Committee)
- ISO annual limit per employee
- Evergreen provision (automatic annual share reserve increase), if any

**Statutory basis:**

- ISOs require stockholder approval of the plan within 12 months before or after board
  adoption (IRC §422(b)(1)) [VERIFY]
- DE: DGCL §157 authorizes the board to create option plans; §228 allows stockholder
  approval by written consent
- UK: CA 2006 s.701 — options must be granted within authority granted by shareholders
  under s.549(1); EMI options require HMRC notification within 92 days [JURISDICTION-SPECIFIC]

**Two-resolution approach** (recommended):

1. Board resolution adopting the plan
2. Stockholder written consent or meeting resolution approving the plan (for ISO eligibility)

---

### 5. Financing Approvals

#### 5a. Convertible Note / SAFE

**Required inputs:**

- Principal amount (note) or investment amount (SAFE)
- Investor name(s)
- Key economic terms: interest rate (note), discount rate, valuation cap, maturity date (note)
- Reference to the form of note / SAFE agreement
- Authorized signatories

**Securities law:** Section 4(a)(2) or Regulation D exemption; Form D filing within 15 days
of first sale under Rule 503; accredited investor verification [VERIFY for Rule 506(c)]

#### 5b. Preferred Stock Round (Priced Round)

**Required inputs:**

- Series designation (e.g., Series A, Series Seed)
- Number of shares to be authorized and issued
- Price per share
- Lead investor and all participants
- Key terms: liquidation preference, dividend, conversion ratio, voting rights
- Reference to: Stock Purchase Agreement, Restated Certificate, Investor Rights Agreement,
  ROFR/Co-Sale Agreement, Voting Agreement

**Additional approvals needed:**

- Stockholder approval of Restated Certificate of Incorporation (DGCL §242 — board
  recommends, stockholders approve by written consent or meeting)
- Stockholder approval of Voting Agreement provisions binding all stockholders

#### 5c. Debt / Credit Facility

**Required inputs:**

- Lender name
- Facility type and amount
- Collateral (if secured — personal property UCC; real property mortgage)
- Reference to loan agreement / promissory note / security agreement
- UCC-1 financing statement authorization (if granting security interest)
- Authorized signatories

---

### 6. Contract Authorizations

**Use case:** Authorize a specific material agreement or establish officer signing authority.

**Required inputs:**

- Contract name and counterparty
- Material terms summary (for specific authorization)
- Dollar threshold for officer authority (if establishing general authority)
- Designated officers authorized to sign

**Drafting note:** For large or strategic contracts, name the specific agreement and attach
as an exhibit. For routine contracts, establish a dollar threshold framework:

```
RESOLVED, THAT the Officers of the Company are hereby authorized to execute, deliver,
and perform any contract, agreement, or instrument with a value not exceeding $[X] in the
ordinary course of business, without further action of the Board.
```

---

### 7. Dividend Declarations

**Required inputs:**

- Dividend amount per share
- Class of stock receiving the dividend
- Record date (stockholders of record as of this date receive the dividend)
- Payment date

**Statutory prerequisites:**

- DE: DGCL §170(a) — dividends payable only out of "surplus" (excess of net assets over
  capital account) or, if no surplus, out of net profits for the current or preceding fiscal
  year. Dividends that impair capital are prohibited. [VERIFY against current Delaware case law]
- UK: CA 2006 s.830 — dividends payable only out of "distributable profits" (accumulated
  realized profits less accumulated realized losses). Directors must prepare interim accounts
  to justify interim dividends. Unlawful dividends create personal liability for directors
  and must be repaid by knowing shareholders. [VERIFY]
- MBCA: §6.40 — distributions permitted unless after distribution company cannot pay its
  debts or its total assets would be less than total liabilities plus preferential liquidation
  rights [VERIFY]

**Solvency confirmation required:** Always include a solvency/surplus confirmation in the
recitals:

```
WHEREAS, based on the most recently available financial statements of the Company and
the Board's review thereof, the Company has sufficient surplus within the meaning of
Section 170 of the DGCL [or: distributable profits within the meaning of Section 830 of
the Companies Act 2006] to make the foregoing distribution without impairing the
Company's capital;
```

---

### 8. Annual Compliance / Organizational Resolutions

**Typical actions in annual consent or organizational meeting:**

1. **Ratification of prior acts**: Ratify all acts of officers and directors since the last
   consent/meeting (protects against inadvertent defects in prior authorizations)
2. **Officer reappointments**: Re-confirm current officers in their roles
3. **Fiscal year**: Confirm or change the fiscal year
4. **Bank accounts**: Confirm authorized banks and signing officers
5. **Accountants/auditors**: Appoint or reappoint the company's accountants or auditors
6. **D&O insurance**: Authorize D&O, E&O, and other insurance
7. **Equity plan share increase** (if applicable): Approve annual evergreen increase
8. **Reaffirm indemnification**: Reaffirm indemnification agreements and policy
9. **Code of conduct**: Reaffirm business ethics and code of conduct
10. **Annual report / financial statements**: Receive and acknowledge financial statements

---

### 9. Bank Account Authorization

**Required inputs:**

- Bank name and branch
- Account type (checking, savings, money market)
- Authorized signatories: name, title, signature alone or jointly
- Any dollar threshold for single vs. dual signature

**Standard form:**

```
RESOLVED, THAT the Company is hereby authorized to maintain bank account(s) at [Bank
Name], and that the following officers are hereby authorized to open, maintain, and close
accounts at such bank, and to sign checks, drafts, withdrawal orders, and other instruments
on behalf of the Company with respect to such accounts:
  [Name], [Title] — [Sole/Joint] signatory up to $[X]
  [Name], [Title] — [Sole/Joint] signatory up to $[X]
```

---

### 10. M&A Preliminary and Full Approvals

#### 10a. LOI / Term Sheet Authorization

- Authorize negotiation and execution of a non-binding LOI
- Typically board-only; note non-binding nature in recitals
- Include exclusivity authorization if applicable

#### 10b. Merger / Acquisition Agreement Approval (Full)

**Requires stockholder approval (DE §251 / MBCA §11.04 / CA 2006 s.907)**

**Exception — DGCL §251(f) small-share-issuance merger**: No stockholder vote is required
if (i) the merger agreement does not amend the certificate, (ii) each share of the surviving
corporation is identical to the pre-merger shares, AND (iii) the surviving corporation issues
common stock representing ≤20% of its pre-merger outstanding shares. If all three conditions
are met, board approval alone is sufficient. Confirm applicability with counsel before
omitting the stockholder vote. [VERIFY]

Board resolution must:

- Approve the merger agreement
- Declare advisability of the merger [DGCL §251(b) requirement — the word "advisable" is
  mandatory; using only "approved" is insufficient]
- Direct that the merger agreement be submitted to stockholders for approval (unless the
  §251(f) exception applies)
- Include §280G screening (golden parachute analysis): If any payment to a disqualified
  individual equals or exceeds 3x their base amount, golden parachute excise tax applies
  (IRC §280G / §4999). Board must be aware; stockholder approval of parachute payments in
  certain contexts can avoid excise tax. [VERIFY with tax counsel]
- Authorize officers to file any required regulatory submissions (HSR, CFIUS if applicable)

#### 10c. Sale of Substantially All Assets (DE §271)

- Board resolution + stockholder majority approval required
- Board must recommend the sale (or note its recommendation)

---

### 11. Subsidiary Formation

**Required inputs:**

- Subsidiary name, state/country of formation
- Authorized shares or membership interests
- Initial officers/directors of subsidiary
- Capital contribution amount
- Reference to operating agreement (if LLC) or subsidiary bylaws

**Standard resolved clauses:**

```
RESOLVED, THAT the Company hereby approves the formation of [Subsidiary Name], a
[Delaware] [corporation/limited liability company], and that the Officers of the Company
are authorized to take all steps necessary to effect such formation, including filing
applicable organizational documents, paying all required fees, and contributing [$X]
as initial capital.
```

---

### 12. Indemnification Agreements

**Statutory basis:**

- DE: DGCL §145 — corporation may (and in many cases must, under §145(c)) indemnify
  current and former directors and officers for expenses, judgments, fines, and settlements
  incurred in proceedings by reason of their status as director/officer, provided they acted
  in good faith and in a manner reasonably believed to be in or not opposed to the best
  interests of the corporation
- UK: CA 2006 s.232-238 — restrictions on provisions protecting directors from liability;
  qualifying third-party indemnity provisions (QTPIs) and qualifying pension scheme
  indemnity provisions (QPSIs) are permitted; directors' indemnity insurance permitted

**Drafting note:** Board approves the form of indemnification agreement and authorizes the
company to enter into individual agreements with each director and officer.

---

## Drafting Standards

### Recital / Resolved Structure

Every board resolution uses a consistent structure:

**Header (UWC format):**

```
UNANIMOUS WRITTEN CONSENT OF THE BOARD OF DIRECTORS
OF [COMPANY NAME]
[A DELAWARE CORPORATION / A COMPANY LIMITED BY SHARES INCORPORATED IN ENGLAND AND WALES]

Dated: [DATE]
```

**Header (Meeting Minutes format):**

```
MINUTES OF A SPECIAL MEETING OF THE BOARD OF DIRECTORS
OF [COMPANY NAME]

Held on [DATE] at [TIME] via [video conference / telephone / in person at: ADDRESS]
```

**Preamble (UWC):**

```
The undersigned, constituting all of the members of the Board of Directors (the "Board")
of [Company Name] (the "Company"), a [Delaware corporation / company incorporated in
England and Wales], acting pursuant to [Section 141(f) of the Delaware General Corporation
Law / Article 18 of the Company's Articles of Association], hereby unanimously adopt the
following resolutions by written consent without a meeting:
```

**Preamble (Meeting):**

```
Present: [List all directors present], constituting a quorum of the Board.
Also present: [List non-directors, e.g., counsel, officers]
The [Chair/President/Secretary] called the meeting to order and noted that a quorum was
present. Notice of the meeting was [waived by all directors / provided on [date]].
```

**Recitals (WHEREAS clauses):**

- State the background facts, not the authorizations
- Use WHEREAS for factual predicate: "WHEREAS, the Company desires to..."
- Keep concise — one WHEREAS per material fact
- End with "NOW, THEREFORE, BE IT RESOLVED AS FOLLOWS:" or similar
- Not always required for simple/administrative resolutions

**Resolved clauses:**

- Start each operative paragraph with "RESOLVED, THAT..."
- Additional authorizations: "RESOLVED FURTHER, THAT..."
- Administrative catchall: "RESOLVED FURTHER, THAT the Officers of the Company are
  authorized to take such further actions... as may be necessary or appropriate to
  carry out the intent of the foregoing resolutions."
- Use active, present-tense language: "is hereby authorized" not "shall be authorized"

**Standard administrative "Further Resolved" clauses** (include in nearly every consent):

```
RESOLVED FURTHER, THAT the Secretary of the Company is authorized and directed to
file this Consent in the corporate records of the Company.

RESOLVED FURTHER, THAT the Officers of the Company are authorized and directed to
execute and deliver any documents, instruments, certificates, or agreements and to
take all actions that they deem necessary or advisable to carry out and give full
effect to the foregoing resolutions and the transactions contemplated thereby.

RESOLVED FURTHER, THAT any actions previously taken by the Officers of the Company
consistent with the purposes and intent of the foregoing resolutions are hereby
ratified, confirmed, and approved.
```

**Counterparts language (for UWC with multiple directors signing separately):**

```
This Consent may be executed in one or more counterparts, each of which shall be
deemed an original, and all of which together shall constitute one and the same
instrument. Electronic signatures shall be deemed valid and binding to the same
extent as original signatures.
```

**Signature block:**

```
[SIGNATURE PAGE TO UNANIMOUS WRITTEN CONSENT OF THE BOARD OF DIRECTORS
OF [COMPANY NAME]]

______________________________    ______________________________
[Director Name]                    [Director Name]
Director                           Director

Date: ____________________         Date: ____________________
```

### Plain-Language Discipline

- Use "is hereby authorized" not "shall be authorized to be empowered to"
- Name the actor explicitly: "the Chief Executive Officer is authorized" not "it is authorized"
- One action per RESOLVED clause
- Define terms once ("the Company"), then use consistently
- Avoid redundant qualifiers: "necessary and appropriate" (use one or the other unless
  both have distinct meaning in context)
- Dates: spell out months (e.g., "March 20, 2026" not "3/20/26")

### Exhibit / Attachment Practice

For material documents approved by the board (e.g., form of option agreement, stock purchase
agreement, loan agreement):

- Reference as "Exhibit A" or "attached hereto as Exhibit A and incorporated herein"
- Note in the resolution: "substantially in the form attached hereto, with such changes
  as the Officers may approve"
- The "substantially in the form" language gives officers flexibility for minor revisions

---

## Resolution Status Classification

After drafting, classify each resolution's completeness:

### COMPLETE — Ready for Execution

All required elements are present. The resolution:

- Correctly identifies the corporate action and authority
- Contains all action-specific required elements
- Addresses any tax/securities law prerequisites
- Has proper signature blocks for all required parties

**Action**: Present for execution.

### DEFICIENT — Revision Required

One or more elements are incomplete, ambiguous, or missing. The resolution may be
ineffective or expose the company to challenge.

**Examples:**

- Exercise price for options stated without reference to 409A valuation
- Dividend declared without surplus/distributable-profits recital
- UWC signed by only some directors (not all)
- Stock issuance approved without confirming authorized shares

**Action**: Identify and remedy each deficiency before presenting for execution.

### INVALID — Void or Unenforceable Without Remediation

A fundamental defect makes the resolution void or unable to authorize the intended action.

**Examples:**

- UWC executed when the company's articles require a meeting for this action
- Board approves a merger without providing for stockholder vote (when required by statute)
- Options granted below FMV with knowledge of 409A exposure and no corrective plan
- Director with material conflict of interest not disclosed or recused for a vote requiring
  disinterestedness (DGCL §144 cleansing procedure not followed) [VERIFY]
- Action taken by a committee that lacks authority for that action under the committee's charter

**Action**: Do not execute. Identify the root defect and the remediation path. Apply
3-pass Self-Interrogation before classifying as INVALID.

---

## Prioritization Framework

### Required Elements (must be present for validity)

- Correct entity name and jurisdiction
- Proper preamble identifying authority under statute / charter
- Operative RESOLVED language that clearly states the authorization
- Grant date / effective date of the action
- All required directors' signatures (for UWC) or quorum present (for meeting)
- Action-specific mandatory elements (see Resolution Type Reference)

### Recommended Elements (best practice; protects against future challenge)

- WHEREAS recitals for context and factual support
- Reference to supporting documents (agreements, appraisals, valuation reports)
- Explicit confirmation of prerequisites (sufficient authorized shares, surplus, 409A compliance)
- "Further Resolved" catch-all delegation of authority to officers
- Ratification of prior acts
- Counterparts clause (for UWC)
- Exhibit attachments for forms of documents

### Optional Elements (useful but not essential)

- Whereas clauses for administrative / simple resolutions
- Extensive narrative recitals for routine actions
- Signatures of non-director officers on the resolution itself (officers implement, board signs)

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                             | Fail Action                                              |
| -------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established principle | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent format (DGCL §; CA 2006 s.; IRC §)             | Fix format                                               |
| **Currency**   | Cited provisions checked for amendments or repeal                                | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the applicable corporate law jurisdiction                  | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated; do not assert a legal rule without a basis        | Add confidence qualifier                                 |

### Self-Interrogation for INVALID Classifications

For any element classified as INVALID, apply this 3-pass review before delivery:

**Pass 1 — Legal Chain Integrity:**

- Does the invalidity follow logically from the cited statute or provision?
- Would a Delaware court of chancery (or English High Court) actually hold this void on
  these facts?
- Has the corporation adopted any charter/bylaw provision that modifies the statutory default?

**Pass 2 — Completeness:**

- Have all relevant statutes, code provisions, and case law been considered?
- Could the defect be cured by a ratifying resolution or shareholder approval?
- Does DGCL §204 (ratification of defective corporate acts) provide a cure path? [VERIFY]

**Pass 3 — Challenge:**

- What is the strongest argument that this resolution IS valid despite the apparent defect?
- Under what circumstances would a reasonable corporate lawyer advise proceeding?
- Is INVALID proportionate, or is this actually DEFICIENT with a clear remedy?

If any pass reveals a weakness, revise before delivery. Mark the Glass Box with
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                          | Action                                                |
| ------------ | --------- | ------------------------------------------------ | ----------------------------------------------------- |
| **Definite** | 0.95-1.0  | Clear statutory text, settled practice           | State with confidence                                 |
| **High**     | 0.80-0.94 | Strong authority, minor interpretation questions | State with brief caveat                               |
| **Probable** | 0.60-0.79 | Good practice, could vary by charter/bylaw       | State with reasoning and qualifiers                   |
| **Possible** | 0.40-0.59 | Genuinely uncertain, charter-dependent           | Flag for counsel review with both interpretations     |
| **Unlikely** | 0.0-0.39  | Weak or speculative basis                        | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every output MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-board-resolution-drafter"
  entity: "[Company name]"
  entity_type: "[Delaware corporation / UK Ltd / UK Plc / LLC / other]"
  resolution_format: "[UWC / Meeting Minutes / Written Resolution of Directors (UK)]"
  actions_covered:
    - "[Action type 1 — COMPLETE / DEFICIENT / INVALID]"
    - "[Action type 2 — COMPLETE / DEFICIENT / INVALID]"
  stockholder_approval_required: "[Yes — [action(s)] / No]"
  tax_triggers_flagged:
    - "[IRC §409A — [addressed/not applicable]]"
    - "[IRC §280G — [addressed/not applicable]]"
    - "[Rule 701 aggregate — [addressed/not applicable]]"
  prerequisites_confirmed:
    - "[Authorized shares sufficient — [Yes/No/Unconfirmed]]"
    - "[409A valuation current — [Yes/No/Unconfirmed]]"
    - "[Equity plan adopted and stockholder-approved — [Yes/No/Unconfirmed]]"
    - "[Dividend surplus/distributable profits confirmed — [Yes/No/N/A]]"
  legalcode_mcp: "Connected / Not connected"
  statutes_consulted:
    - "[DGCL §141(f) — VERIFIED (legalcode-mcp) or UNVERIFIED]"
    - "[IRC §409A — VERIFIED or UNVERIFIED]"
    - "[CA 2006 s.288 — VERIFIED or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no INVALID items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations — e.g., 'charter and bylaws not reviewed']"
    - "[Any items requiring counsel verification]"
  reviewer: "AI-assisted — requires qualified corporate counsel review before execution"
```

---

## Anti-Patterns

Corporate resolution drafting failure modes — explicit catalogue of what NOT to do:

1. **Non-unanimous UWC under Delaware law** — Under DGCL §141(f), action by written consent
   without a meeting requires the consent of _all_ members of the board, not just a majority.
   A written consent signed by fewer than all directors is a nullity under Delaware law.
   If unanimous consent is not achievable, call a meeting instead.

2. **Granting options without a current 409A valuation** — Options granted at below-FMV
   are not "options" for §409A purposes — they are deferred compensation. The optionee faces
   income tax, 20% excise tax, and interest on the _unvested spread_ in the year of vesting.
   No resolution should set an option exercise price without referencing a current independent
   409A appraisal.

3. **Backdating option grants** — Recording a grant date earlier than the actual board
   approval date to achieve a lower exercise price (lower 409A). This is securities fraud and
   exposes officers, directors, and optionees to criminal and civil liability. The grant date
   is the date of board approval.

4. **Issuing more shares than are authorized** — A stock issuance is void if the company does
   not have sufficient authorized but unissued shares of the applicable class in its certificate
   of incorporation. Always verify authorized share counts before approving an issuance.

5. **Declaring dividends without surplus** — Under DGCL §170(a), dividends may only be
   declared out of surplus. Directors who authorize an illegal dividend face personal liability
   to the corporation and creditors. Always include a surplus/solvency recital based on
   reviewed financials.

6. **Board approving a merger without recommending it to stockholders** — DGCL §251(b) requires
   the board to adopt a resolution approving the agreement and declaring its advisability _before_
   submitting to stockholders. A merger agreement approved but not declared advisable by the
   board may create defects in the merger approval process.

7. **Forgetting that written resolutions are not available for UK PLCs** — CA 2006 s.288(1)
   limits written resolutions to private companies. A public company's directors cannot act
   by written resolution of shareholders; they must call a general meeting.

8. **Interested director transactions without DGCL §144 cleansing** — A contract or transaction
   in which a director has a material financial interest is voidable unless: (i) the material
   facts are disclosed and the disinterested directors approve by majority, (ii) the material
   facts are disclosed and stockholders approve, or (iii) the transaction was fair to the
   corporation. Resolutions for interested-party transactions must reflect the §144 cleansing
   procedure (DGCL §144). [VERIFY]

9. **Missing the ISO employee requirement** — ISOs under IRC §422 can only be granted to
   employees of the issuing corporation or its parent or subsidiary. Granting ISOs to
   contractors, advisors, or consultants renders them NSOs by operation of law — but with
   potential documentation and administrative issues.

10. **Granting ISOs that exceed the $100K annual vesting limit** — Under IRC §422(d), ISOs
    first exercisable in any calendar year with FMV (at grant) exceeding $100,000 are treated
    as NSOs to the extent of the excess. Large grants to senior executives must be modeled
    to ensure the $100K cap is not exceeded. [VERIFY]

11. **Using a committee resolution for actions reserved to the full board** — Board committees
    have only the authority delegated to them. Under DGCL §141(c)(2), committees cannot
    approve mergers, recommend asset sales to stockholders, amend bylaws, or declare dividends
    unless the certificate expressly permits. Confirm committee authority before using a
    committee consent.

12. **Action in a jurisdictions where board must physically meet** — Some jurisdictions
    or company articles require directors to convene in person for certain actions. Verify
    the articles and applicable law before relying on a telephonic or video meeting.

13. **No "further resolved" delegation to officers** — A board resolution that grants an
    authorization but does not delegate signing authority to specific officers leaves the
    company unable to execute the authorized transaction without coming back to the board.
    Always include an officer delegation clause.

14. **Failing to attach or reference supporting documents** — A resolution authorizing
    a stock purchase agreement that does not identify the agreement (by name, date, or
    as an exhibit) leaves room for dispute about what was authorized. Attach material forms
    as exhibits or describe them with sufficient specificity.

15. **Storing electronic consents without signatures on file** — A UWC exists only when
    signed by all directors and delivered to the company per DGCL §116. Delivery may be
    electronic, but signatures must be collected and retained. A partially signed consent
    not yet delivered to the company has no legal effect until fully signed and delivered.

16. **Missing quorum for board meeting** — Minutes should affirmatively state quorum was
    present. Minutes that don't confirm quorum are deficient and may be challenged. Under
    DGCL §141(b), a majority of the total number of directors (as of the date of the meeting,
    not just those present) constitutes a quorum unless the bylaws specify otherwise.

17. **Omitting 280G analysis in M&A resolutions** — If the company is being acquired and
    any payments to officers, directors, or employees could constitute "excess parachute
    payments" under IRC §280G, the board resolution should document that this was considered.
    A board that fails to evaluate 280G creates potential liability. Consider whether stockholder
    approval of parachute payments is available to avoid the excise tax. [VERIFY tax counsel required]

18. **Approving a charter amendment without separately recommending it to stockholders** —
    A board resolution that "amends the certificate of incorporation" (rather than "approves
    the amendment and recommends it to stockholders for approval") misunderstands that the
    board cannot amend the charter unilaterally. The board recommends; the stockholders approve.

19. **UK: Allotting shares without shareholder authority under s.551** — In the UK, directors
    of a company cannot allot shares unless authorized by the shareholders under CA 2006 s.549-551,
    or the allotment falls within an exemption (e.g., employees' share scheme under s.549(2)).
    Any allotment without s.551 authority is a criminal offence. [VERIFY current penalties]

20. **Confusing ratification with original authorization** — A "catch-all ratification" of
    prior acts does not cure acts that were fundamentally void (e.g., an issuance of shares
    beyond authorized limits). DGCL §204 provides a procedure for ratifying "defective
    corporate acts," but it has specific procedural requirements and limits. [VERIFY scope]

---

## Writing Standards

Apply plain-language discipline to all resolution drafts:

**For operative language (RESOLVED clauses):**

- Verb-first, active voice: "the Company is hereby authorized" not "authorization is hereby granted to the Company"
- Use "hereby" to signal present effect of the resolution
- Specify the actor: "the Chief Executive Officer is authorized" not "an officer is authorized"
- Be specific about amounts, dates, and document references
- Use capitalized defined terms consistently after first definition

**For recitals (WHEREAS clauses):**

- State facts, not conclusions: "WHEREAS, the Board has reviewed the terms of the Merger Agreement" not "WHEREAS, the Merger Agreement is advisable"
- Keep each WHEREAS to one factual point
- Chronological order: present facts in sequence

**Quality gates before delivery:**

1. Can a corporate secretary execute this resolution without ambiguity?
2. Does every defined term match its first definition?
3. Is every dollar amount, date, and name specific?
4. Has every statutory cross-reference been stated correctly?
5. Are all required directors' names spelled correctly?
6. Could any clause be shortened without losing precision? If yes, shorten.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- Search for jurisdiction-relevant corporate statutes and recent amendments before drafting
- Verify specific DGCL, CA 2006, or IRC section text and current version
- Search for recent Delaware Court of Chancery opinions on corporate governance actions
- For equity grant resolutions: verify current 409A regulatory guidance and any recent
  IRS notices affecting FMV valuation methodology
- For M&A resolutions: verify current §280G thresholds and stockholder approval procedures
- Save verified authority to `/tmp/legalcode-board-resolution-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Mark all statutory and regulatory references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed with general corporate law knowledge but flag all legal authority for counsel
  verification before execution

---

## Output Format Template

Structure every deliverable as:

```markdown
## Board Resolution Summary

**Entity**: [Company name and jurisdiction]
**Action(s)**: [List of authorized actions]
**Format**: [UWC / Board Meeting Minutes / Written Resolution of Directors]
**Date**: [Date of consent or meeting]
**Prepared**: [Date of this draft]

---

## Prerequisites Status

| Prerequisite                 | Status                                          | Notes    |
| ---------------------------- | ----------------------------------------------- | -------- |
| Authorized shares sufficient | ✅ Confirmed / ⚠️ Unconfirmed / ❌ Insufficient | [detail] |
| 409A valuation current       | ✅ / ⚠️ / ❌ / N/A                              | [detail] |
| Equity plan adopted          | ✅ / ⚠️ / ❌ / N/A                              | [detail] |
| Stockholder approval needed  | ✅ Obtained / ⚠️ Still required / N/A           | [detail] |
| Dividend surplus confirmed   | ✅ / ⚠️ / N/A                                   | [detail] |

---

## Flags for Counsel Review

[List any items requiring legal counsel attention before execution, numbered and specific]

---

## Resolution Draft

[FULL FORMATTED RESOLUTION READY FOR EXECUTION — see Drafting Standards for structure]

---

## Completeness Assessment

**Resolution Status**: COMPLETE / DEFICIENT / INVALID

[If DEFICIENT or INVALID: identify each deficiency with specific remediation steps]

---

## Glass Box Audit Trail

[YAML per Glass Box template above]
```

---

## Localization Notes

This skill provides deep coverage for Delaware and UK corporate law. When used for
other jurisdictions, apply these localization steps:

| Jurisdiction         | Key Differences                                                                                                                                                                                         |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Other US states**  | Check state corporation statute for UWC requirements (unanimous vs. majority); some states require notarization for certain filings; foreign qualification resolutions may need state-specific language |
| **Canada (federal)** | CBCA s.117 permits written resolutions signed by all directors; directors' liability for unauthorized dividends under CBCA s.118 [JURISDICTION-SPECIFIC]                                                |
| **Germany**          | GmbH board (Geschäftsführer) vs. supervisory board (Aufsichtsrat) distinction; shareholder approval thresholds differ for GmbH vs. AG [JURISDICTION-SPECIFIC]                                           |
| **France**           | SAS vs. SA vs. SARL structure affects resolution mechanics; statutory auditor (commissaire aux comptes) involvement for certain actions [JURISDICTION-SPECIFIC]                                         |
| **Cayman Islands**   | Common for offshore holding companies of US-backed startups; Companies Act 2023 (Cayman) governs; written resolutions of directors permitted; generally very flexible [JURISDICTION-SPECIFIC]           |
| **Singapore**        | Companies Act (Cap. 50) s.179 written resolutions of directors; s.184E electronic general meetings [JURISDICTION-SPECIFIC]                                                                              |

For any non-covered jurisdiction, always verify:

1. Whether action by written consent without a meeting is permitted and the consent threshold
2. Whether any specific actions require shareholder/member approval
3. Electronic signature validity for corporate records
4. Filing or registration requirements for corporate actions

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis based on:

- Delaware General Corporation Law Title 8, Chapter 1 (DGCL §§141, 142, 145, 152, 157,
  170, 228, 242, 251, 271, 275, 204)
- UK Companies Act 2006 (ss.160, 168, 248, 288-300, 549-551, 561, 580, 830) and Model
  Articles of Association SI 2008/3229
- IRC §§409A, 422, 280G, 1202; Securities Act Rule 701; Section 4(a)(2); Regulation D
- Model Business Corporation Act (MBCA §§8.21, 8.40, 11.04)
- NVCA model documents and startup corporate governance best practices
- Legalcode original synthesis using 2-agent research pipeline (legal research agent +
  structural analysis agent) + reference standard patterns from legalcode-contract-review
