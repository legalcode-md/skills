---
name: legalcode-ma-due-diligence-checklist
description: Generate comprehensive M&A legal due diligence checklists tailored to transaction type (asset
  purchase, stock/share purchase, merger), target company characteristics, and applicable jurisdictions.
  Use when conducting legal due diligence for mergers, acquisitions, carve-outs, joint ventures, or corporate
  investments. Covers all 12 workstreams (corporate structure, contracts, IP, litigation, employment,
  regulatory, real estate, environmental, tax, data privacy, antitrust/FDI, insurance) with deal-type-specific
  considerations, red flag identification, and jurisdiction-variant requirements. Triggers on "M&A due
  diligence", "legal dd checklist", "acquisition due diligence", "asset purchase diligence", "stock purchase
  diligence", "merger legal review", "target company legal review", "data room checklist", or "deal due
  diligence". Jurisdiction-agnostic with markers for US, UK, EU, India, and Australia variants.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode M&A Due Diligence Checklist

> **Disclaimer**: This skill provides a framework for AI-assisted M&A legal due diligence
> planning and execution. It does not constitute legal advice. All outputs should be
> reviewed by qualified legal counsel licensed in the relevant jurisdiction(s) before use.
> Laws change; verify current applicability before relying on any provision described here.
> Statutory and case law references cited from memory carry hallucination risk — verify
> against authoritative sources before relying on them. Due diligence findings require
> professional judgment to assess materiality and deal impact.

## Purpose and Scope

This skill generates comprehensive legal due diligence checklists for M&A transactions,
tailored to transaction structure, target characteristics, and jurisdictional requirements.
It produces actionable request lists, identifies red flags, tracks diligence status, and
generates findings summaries suitable for transaction documentation.

**Covers:**

- Transaction-type-specific diligence frameworks (asset purchase, stock purchase, merger)
- All 12 legal due diligence workstreams with detailed request items
- Deal-type differentiators (what applies only to stock purchases, what differs in mergers)
- Jurisdiction-specific requirements with [JURISDICTION-SPECIFIC] markers
- Industry-specific additions for regulated sectors
- Red flag identification and severity classification
- Diligence request tracking and status management
- Findings summary generation for transaction documentation
- Quality-verified output with Glass Box audit trail

**Does not:**

- Conduct financial, commercial, or operational due diligence (see related financial skills)
- Draft or negotiate transaction documents (see contract skills)
- Provide legal advice or replace qualified M&A counsel
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with localization markers

**Related skills:**

- `legalcode-contract-review` — clause-level contract analysis for material contracts
- `legalcode-legal-risk-assessment` — enterprise-wide legal risk evaluation
- `legalcode-obligation-tracker` — post-closing obligation tracking
- `imported-*-dd-checklist` — basic financial DD checklists (this skill provides the legal layer)

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill designed for multi-jurisdictional M&A transactions.
The target company's jurisdiction(s) of organization and operation determine which legal
frameworks apply.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

**United States:**

- Delaware General Corporation Law (DGCL) for Delaware entities
- State-specific corporate law requirements for non-Delaware entities
- Hart-Scott-Rodino (HSR) Act filing requirements (2026 threshold: USD 133.9M)
- CFIUS review for national security implications
- SEC reporting requirements for public companies
- State-specific bulk sales laws (where not repealed)
- ERISA requirements for employee benefit plans
- Sarbanes-Oxley compliance for public companies

**United Kingdom:**

- Companies Act 2006 corporate structure requirements
- UK National Security and Investment Act 2021 (NSI Act) screening
- Competition and Markets Authority (CMA) merger review thresholds
- TUPE regulations for employee transfers
- UK GDPR and Data Protection Act 2018
- Financial Conduct Authority (FCA) rules for regulated entities
- Pension Protection Fund (PPF) requirements

**European Union:**

- EU Merger Regulation (EUMR) — turnover thresholds and notification
- EU Foreign Direct Investment Regulation coordination
- Member state corporate law (varies by jurisdiction)
- Works council consultation requirements
- GDPR data protection compliance
- EU AI Act implications for AI-enabled targets
- Sector-specific regulations (MiFID II, PSD2, etc.)

**India:**

- Companies Act 2013 corporate requirements
- Competition Commission of India (CCI) merger notification
- Foreign Exchange Management Act (FEMA) FDI compliance
- Reserve Bank of India (RBI) approvals for certain sectors
- SEBI takeover code for listed companies
- Press Note 3 restrictions for investments from neighboring countries
- Labour law compliance (Industrial Disputes Act, etc.)

**Australia:**

- Corporations Act 2001 requirements
- ACCC merger review and authorization
- Foreign Investment Review Board (FIRB) screening
- Foreign Acquisitions and Takeovers Act 1975
- ASX Listing Rules for listed companies
- Modern Slavery Act 2018 reporting requirements
- Privacy Act 1988 data handling requirements

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the scope or structure of the diligence
- Multiple valid approaches exist based on deal structure
- Industry-specific diligence areas need to be added
- Risk tolerance affects what constitutes a red flag
- Jurisdictional requirements need clarification

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

### Step 1: Accept the Transaction Context

Accept the M&A transaction context in any of these formats:

- **Deal overview**: Brief description of the transaction (who, what, why)
- **Term sheet or LOI**: Letter of intent or term sheet for the transaction
- **Information memorandum**: Confidential information memorandum (CIM) on the target
- **Data room access**: Description of available data room contents
- **Specific question**: "What legal due diligence do we need for X transaction?"

If insufficient context is provided, prompt the user for transaction details.

### Step 2: Gather Transaction Parameters

**CLARIFY** — Before generating the checklist, ask the user these questions. Present them
as structured options:

1. **Transaction Type**: What is the deal structure?
   - Options: Asset Purchase, Stock/Share Purchase, Statutory Merger, Triangular Merger
     (Forward/Reverse), Carve-out/Spin-off, Joint Venture, Minority Investment, Other
   - _Why this matters_: Transaction type fundamentally determines what is acquired, what
     liabilities transfer, and what third-party consents are required. An asset purchase
     allows cherry-picking; a stock purchase acquires the entire entity including unknown
     liabilities.

2. **Target Company Profile**: What are the target's key characteristics?
   - Company name and jurisdiction of organization
   - Public or private company
   - Industry/sector
   - Number of employees (approximate)
   - Geographic footprint (jurisdictions of operation)
   - Revenue range (order of magnitude)
   - _Why this matters_: A regulated financial institution requires different diligence
     than a software startup. Employee count determines labor law complexity. Multi-
     jurisdictional operations multiply regulatory requirements.

3. **Your Role**: Which side are you on?
   - Options: Buyer/Acquirer, Seller/Target, Investor, Joint Venture Partner, Financial
     Advisor, Legal Counsel (for which party?)
   - _Why this matters_: Buyer diligence focuses on risk discovery and valuation protection.
     Seller diligence (reverse due diligence) focuses on disclosure preparation and
     representation support.

4. **Deal Timeline**: What is the target closing timeline?
   - Options: Expedited (< 60 days), Standard (60-120 days), Extended (> 120 days),
     Signed/Closing gap (specify)
   - _Why this matters_: Timeline determines diligence depth. An expedited deal requires
     prioritization of critical workstreams; a standard timeline allows comprehensive review.

5. **Key Concerns**: Any specific issues to prioritize?
   - Options: IP ownership/infringement, Customer contract assignability, Employee retention,
     Litigation exposure, Regulatory approvals, Environmental liabilities, Data privacy
     compliance, Antitrust/FDI clearance, Tax structure, None specified — comprehensive review
   - Allow multiple selections.
   - _Why this matters_: Known red flags or deal-specific concerns should be investigated
     first and most thoroughly.

6. **Materiality Threshold**: What is the materiality threshold for flagging?
   - Provide specific thresholds for: Contract value, Litigation exposure, Liability amounts,
     or say "Use standard 5% of deal value thresholds"
   - _Why this matters_: A USD 50M deal has different materiality than a USD 5B deal.
     Thresholds determine what gets flagged and what is noted but not elevated.

If the user provides partial context, proceed with reasonable defaults but **state
assumptions explicitly** (e.g., "I'm assuming this is a stock purchase of a US private
company — let me know if that differs"). Do not silently assume.

### Step 3: Load the Deal Playbook

Check for organization-specific M&A due diligence standards in local settings (e.g.,
`legal.local.md`, `ma-playbook.md`, or similar configuration files).

The deal playbook should define:

- Standard diligence scope by deal type and size
- Mandatory workstreams and optional workstreams
- Organization-specific red flag criteria
- Materiality thresholds by deal tier
- Required approvals for specific findings
- Preferred outside counsel and advisors by jurisdiction
- Post-closing integration checklists

**If no playbook is configured:**

**CLARIFY** — Inform the user that no playbook was found, and ask:

- **Option A: Set up deal standards now** — Define organization-specific diligence scope,
  materiality thresholds, and red flag criteria. Takes time but enables consistent
  diligence across transactions.
- **Option B: Proceed with market standards** — Use the comprehensive 12-workstream
  framework below with standard materiality thresholds (5% of deal value for contracts,
  1% for litigation exposure). Professional but may not reflect organizational preferences.
- **Option C: Specify priorities as we go** — Generate the comprehensive checklist and
  flag where organizational input would refine the approach.

Clearly label when defaults are being used: "Based on market-standard M&A due diligence
framework — not organization-specific playbook."

### Step 4: Determine Transaction-Type Differentiators

Based on the transaction type identified in Step 2, apply the appropriate diligence
framework. Different transaction types have materially different risk profiles and
diligence requirements.

#### Asset Purchase Differentiators

In an asset purchase, the buyer acquires specific assets and assumes only specifically
identified liabilities. Diligence focus includes:

**Asset-Specific Focus Areas:**

- [ ] **Asset identification**: Complete inventory of assets to be acquired (tangible,
      intangible, contracts, permits, IP, goodwill)
- [ ] **Title verification**: Seller's clear title to each asset; liens, encumbrances,
      security interests (UCC searches in the US, PPSR in Australia, Companies House charges
      in UK)
- [ ] **Assignability**: Third-party consent requirements for contract and permit assignments
- [ ] **Excluded assets**: Clarity on what is NOT being acquired
- [ ] **Excluded liabilities**: Explicit exclusion of unknown and pre-closing liabilities
- [ ] **Bulk sales compliance**: Applicability of bulk sales laws (varies by US state;
      largely repealed but check) [JURISDICTION-SPECIFIC]
- [ ] **Successor liability exceptions**: Exceptions to general non-assumption (de facto
      merger, product liability, environmental, employee claims) [JURISDICTION-SPECIFIC]

**Asset Purchase Advantages for Buyer:**

- Selective acquisition — acquire only desired assets
- Liability limitation — generally no assumption of unknown liabilities
- Stepped-up tax basis in acquired assets (US)
- Fresh start on permits and relationships

**Asset Purchase Risks for Buyer:**

- Requires individual asset transfer (more complex, more consents)
- May not acquire non-transferable permits/licenses
- Employee transfers require rehiring (termination risk under WARN, TUPE)
- Successor liability doctrines may impose liability anyway

#### Stock/Share Purchase Differentiators

In a stock purchase, the buyer acquires the target entity itself, including all assets,
liabilities, contracts, and obligations. Diligence must be comprehensive because the
buyer inherits everything.

**Stock Purchase-Specific Focus Areas:**

- [ ] **Title to shares**: Seller's clear ownership of target stock; restrictions on transfer
- [ ] **Capitalization**: Authorized, issued, and outstanding shares; options, warrants,
      convertible securities; preemptive rights; anti-dilution protections
- [ ] **Stockholder agreements**: Voting agreements, buy-sell agreements, ROFR/ROFO, drag/tag
- [ ] **Stock issuance compliance**: Proper authorization and issuance of all outstanding
      securities; exemption from registration requirements [JURISDICTION-SPECIFIC]
- [ ] **Unknown liability exposure**: All historical and contingent liabilities transfer
      with the entity — diligence must be comprehensive
- [ ] **Contract continuity**: Contracts generally remain in place (no assignment required
      unless change-of-control provisions exist)
- [ ] **Change-of-control provisions**: Identify contracts with acceleration, termination,
      or consent triggers on change of control
- [ ] **Tax attributes**: NOLs, credits, basis — may be limited by Section 382 (US) or
      similar provisions [JURISDICTION-SPECIFIC]

**Stock Purchase Advantages for Buyer:**

- Simplicity — one transaction transfers the entire entity
- Contract continuity (subject to change-of-control provisions)
- Permits and licenses generally remain in place
- Employment relationships continue without interruption

**Stock Purchase Risks for Buyer:**

- Full assumption of all liabilities (known and unknown)
- Comprehensive diligence required
- No stepped-up tax basis without 338(h)(10) election (US)
- All historical compliance issues and litigation travel with the entity

#### Merger Differentiators

In a statutory merger, the target company merges into the acquirer (or a subsidiary),
with the target's separate existence ceasing. Effects combine elements of both asset
and stock acquisitions.

**Merger-Specific Focus Areas:**

- [ ] **Statutory requirements**: Compliance with merger statutes in the target's
      jurisdiction (board approval, stockholder vote, appraisal rights) [JURISDICTION-SPECIFIC]
- [ ] **Appraisal rights**: Dissenter/appraisal rights availability and procedure;
      potential liability for paying fair value to dissenters [JURISDICTION-SPECIFIC]
- [ ] **Triangular merger structure**: Forward vs. reverse triangular — liability
      containment, tax treatment, third-party consent implications
- [ ] **Certificate of merger**: Filing requirements and effective date mechanics
- [ ] **Surviving entity**: Which entity survives; impact on contracts, permits, obligations
- [ ] **Minority stockholders**: Squeeze-out procedures, entire fairness standards for
      controlling stockholder transactions [JURISDICTION-SPECIFIC]

**Forward Triangular Merger:**

- Target merges into acquirer's subsidiary
- Target shareholders receive merger consideration
- Target ceases to exist; subsidiary survives
- Contracts and liabilities transfer to subsidiary (contained)

**Reverse Triangular Merger:**

- Acquirer's subsidiary merges into target
- Subsidiary ceases to exist; target survives
- Target becomes wholly-owned subsidiary of acquirer
- Useful when target has non-assignable contracts or licenses

### Step 5: Gather Jurisdiction-Relevant Legal Authority

Identify the jurisdiction(s) relevant to the transaction and target operations.

**CLARIFY** — If any of the following are true, ask the user:

- **Multiple jurisdictions with conflicting requirements**: Ask how to prioritize or
  whether to address all jurisdictions comprehensively
- **Unclear regulatory applicability**: Ask whether specific regulations apply (e.g., "Is
  the target subject to CFIUS review?" "Does TUPE apply to this asset purchase?")
- **Extraterritorial reach**: Flag where regulations may apply extraterritorially (e.g.,
  FCPA applies to US issuers' conduct worldwide)

**With legalcode-mcp connected (preferred):**

- Search for jurisdiction-relevant corporate statutes, M&A regulations, and regulatory
  requirements
- Search for recent deal-related enforcement actions and regulatory guidance
- Save results to a local temp file (`/tmp/legalcode-ma-dd-authority.md`)
- Reference verified authority throughout the checklist
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark every statutory reference with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with general M&A knowledge, but flag that legal authority has not been
  independently verified

### Step 6: Generate the Due Diligence Checklist

Generate a comprehensive checklist covering all 12 legal due diligence workstreams.
Tailor the checklist to the transaction type and target characteristics identified in
Steps 2-4.

For each workstream:

1. Include all standard request items
2. Add transaction-type-specific items (flagged with deal type)
3. Add industry-specific items (flagged with industry)
4. Add jurisdiction-specific items (flagged with [JURISDICTION-SPECIFIC])
5. Indicate priority (P0 = critical path, P1 = high priority, P2 = standard, P3 = if time permits)
6. Indicate applicability (Asset Purchase / Stock Purchase / Merger / All)

---

## Due Diligence Workstreams

### Workstream 1: Corporate Structure and Organizational Documents

Review the target's corporate structure, governance documents, and organizational history.

| #    | Request Item                                                                       | Priority | Deal Type    | Notes                                  |
| ---- | ---------------------------------------------------------------------------------- | -------- | ------------ | -------------------------------------- |
| 1.1  | Certificate/Articles of Incorporation (as amended and restated)                    | P0       | All          | Original and all amendments            |
| 1.2  | Bylaws (as amended)                                                                | P0       | All          | Current version                        |
| 1.3  | Organizational chart — all subsidiaries, affiliates, and JVs                       | P0       | Stock/Merger | Less critical for asset purchase       |
| 1.4  | Certificate of good standing (each jurisdiction of organization and qualification) | P0       | Stock/Merger | Within 30 days of closing              |
| 1.5  | Board meeting minutes (past 5 years)                                               | P1       | Stock/Merger | Focus on material transactions         |
| 1.6  | Stockholder/member meeting minutes (past 5 years)                                  | P1       | Stock/Merger | Focus on authorizations                |
| 1.7  | Stockholder consents and written actions                                           | P1       | Stock/Merger | All material actions                   |
| 1.8  | List of all jurisdictions where qualified to do business                           | P1       | All          | Compare to where business is conducted |
| 1.9  | List of current officers and directors; appointment records                        | P0       | Stock/Merger | Verify authority                       |
| 1.10 | D&O questionnaires for current management                                          | P1       | Stock/Merger | Conflicts, litigation, bankruptcy      |
| 1.11 | List of authorized signatories; banking resolutions                                | P1       | Stock/Merger | Verify signing authority               |
| 1.12 | Stock ledger and capitalization table                                              | P0       | Stock/Merger | Reconcile to cap table                 |
| 1.13 | Stock certificates (or book-entry records)                                         | P0       | Stock        | Required for stock transfer            |
| 1.14 | Stock option plans and all option/warrant grants                                   | P0       | Stock/Merger | Impact on diluted share count          |
| 1.15 | Convertible securities documentation                                               | P0       | Stock/Merger | SAFEs, notes, warrants                 |
| 1.16 | Stockholder agreements (voting, buy-sell, ROFR, drag/tag)                          | P0       | Stock/Merger | May restrict transfer                  |
| 1.17 | Registration rights agreements                                                     | P1       | Stock/Merger | Post-closing obligations               |
| 1.18 | Stock issuance records and securities law exemption analysis                       | P1       | Stock        | Proper issuance?                       |
| 1.19 | Corporate minute books (physical or electronic)                                    | P1       | Stock/Merger | Completeness check                     |
| 1.20 | Prior M&A transaction documents (acquisitions, dispositions, reorganizations)      | P1       | All          | Historical structure                   |

**Red Flags — Corporate Structure:**

- Missing or incomplete corporate records
- Unauthorized stock issuances or option grants
- Stockholder agreements that block or complicate the transaction
- Unresolved preemptive rights or ROFRs
- Historical corporate actions not properly documented
- Director/officer conflicts of interest not properly handled
- Jurisdictional qualification gaps (doing business without registration)

### Workstream 2: Material Contracts

Review all material contracts to identify liabilities, change-of-control issues, and
third-party consent requirements.

| #    | Request Item                                                  | Priority | Deal Type    | Notes                                                |
| ---- | ------------------------------------------------------------- | -------- | ------------ | ---------------------------------------------------- |
| 2.1  | Customer contracts (all above materiality threshold)          | P0       | All          | Identify change-of-control, termination, exclusivity |
| 2.2  | Customer contracts — top 10 by revenue                        | P0       | All          | Concentration analysis                               |
| 2.3  | Supplier/vendor contracts (all above materiality threshold)   | P0       | All          | Supply continuity, exclusivity                       |
| 2.4  | Supplier contracts — top 10 by spend                          | P0       | All          | Dependency analysis                                  |
| 2.5  | Partnership, joint venture, and strategic alliance agreements | P0       | All          | Change-of-control triggers                           |
| 2.6  | Distribution, reseller, and agency agreements                 | P1       | All          | Territory, exclusivity                               |
| 2.7  | Franchise agreements                                          | P1       | All          | If applicable                                        |
| 2.8  | Service agreements (as provider and as recipient)             | P1       | All          | Ongoing obligations                                  |
| 2.9  | Outsourcing agreements (IT, HR, manufacturing)                | P1       | All          | Transition implications                              |
| 2.10 | Loan agreements, credit facilities, and debt instruments      | P0       | Stock/Merger | Change of control, prepayment                        |
| 2.11 | Security agreements, pledges, and guarantees                  | P0       | Stock/Merger | Liens on assets                                      |
| 2.12 | Indentures and bond documentation                             | P0       | Stock/Merger | If applicable                                        |
| 2.13 | Letters of credit and bank guarantees                         | P1       | All          | Outstanding obligations                              |
| 2.14 | Lease agreements — real property                              | P0       | All          | Assignment consent, change of control                |
| 2.15 | Lease agreements — equipment and vehicles                     | P1       | All          | Transfer mechanics                                   |
| 2.16 | Government contracts and subcontracts                         | P0       | All          | Special assignment rules, novation                   |
| 2.17 | Related-party contracts and intercompany agreements           | P0       | All          | Terms, arm's length                                  |
| 2.18 | Contracts requiring consent to assignment                     | P0       | Asset        | Critical for asset deals                             |
| 2.19 | Contracts with change-of-control provisions                   | P0       | Stock/Merger | Acceleration, termination rights                     |
| 2.20 | Contracts with exclusivity, non-compete, or MFN provisions    | P1       | All          | Post-closing restrictions                            |
| 2.21 | Contracts with uncapped liability or unusual indemnification  | P0       | All          | Risk assessment                                      |
| 2.22 | Contracts in dispute or subject to pending claims             | P0       | All          | Known issues                                         |
| 2.23 | Contracts that have been breached or may be breached          | P0       | All          | Exposure                                             |
| 2.24 | Contracts expiring within 12 months with no renewal           | P1       | All          | Revenue continuity                                   |
| 2.25 | Form agreements (standard customer, vendor, NDA)              | P2       | All          | Understand terms flow                                |

**Red Flags — Contracts:**

- Key customer or supplier contracts with change-of-control termination rights
- Customer concentration (top 5 customers > 50% of revenue)
- Supplier dependency (sole-source critical components)
- Contracts with uncapped indemnification or liability
- Government contracts requiring novation
- Non-assignable contracts critical to the business
- Exclusivity provisions that limit post-closing operations
- Material contracts in default or threatened default
- Related-party contracts not on arm's-length terms
- Contract expirations creating "cliff" risk

### Workstream 3: Intellectual Property

Review IP assets, ownership, protection status, and third-party rights.

| #    | Request Item                                                     | Priority | Deal Type | Notes                          |
| ---- | ---------------------------------------------------------------- | -------- | --------- | ------------------------------ |
| 3.1  | Schedule of all patents (issued and pending)                     | P0       | All       | Jurisdiction, status, expiry   |
| 3.2  | Schedule of all trademarks (registered and pending)              | P0       | All       | Jurisdiction, classes, status  |
| 3.3  | Schedule of all copyrights (registered)                          | P1       | All       | Key software, content          |
| 3.4  | Schedule of all domain names                                     | P1       | All       | Registration, expiry           |
| 3.5  | Schedule of all trade secrets                                    | P0       | All       | Protection measures            |
| 3.6  | IP assignment agreements (from founders, employees, contractors) | P0       | All       | Chain of title                 |
| 3.7  | IP license agreements (inbound — IP licensed from third parties) | P0       | All       | Restrictions, transferability  |
| 3.8  | IP license agreements (outbound — IP licensed to third parties)  | P0       | All       | Exclusivity, royalties         |
| 3.9  | Open-source software inventory and compliance                    | P0       | Tech      | Copyleft, attribution          |
| 3.10 | Software development agreements                                  | P1       | Tech      | Ownership of developed IP      |
| 3.11 | Source code escrow agreements                                    | P2       | Tech      | Customer protection            |
| 3.12 | IP litigation history and threatened claims                      | P0       | All       | Past, pending, threatened      |
| 3.13 | Freedom-to-operate opinions                                      | P0       | Tech      | Critical for tech acquisitions |
| 3.14 | IP due diligence reports from prior transactions                 | P1       | All       | Historical issues              |
| 3.15 | Invention disclosure records                                     | P2       | Tech      | Unfiled patents                |
| 3.16 | Patent prosecution files (for key patents)                       | P1       | Tech      | Prosecution history            |
| 3.17 | Third-party IP claims or cease-and-desist letters                | P0       | All       | Infringement exposure          |
| 3.18 | IP insurance policies                                            | P2       | All       | Coverage for infringement      |
| 3.19 | Confidentiality and non-disclosure agreements                    | P1       | All       | Trade secret protection        |
| 3.20 | Employee invention assignment agreements                         | P0       | All       | Chain of title                 |

**Red Flags — Intellectual Property:**

- Gaps in IP assignment chain (missing founder/contractor assignments)
- Key technology developed without proper assignment agreements
- Open-source components with copyleft licenses (GPL) in proprietary products
- Pending or threatened IP litigation or cease-and-desist letters
- Patents expiring near-term without replacements
- Core trademarks not registered in key markets
- Reliance on licensed IP with questionable transferability
- Inadequate trade secret protection measures
- Freedom-to-operate concerns not addressed
- AI-generated content without clear ownership analysis

### Workstream 4: Litigation and Disputes

Review all litigation, claims, investigations, and dispute exposure.

| #    | Request Item                                                 | Priority | Deal Type     | Notes                             |
| ---- | ------------------------------------------------------------ | -------- | ------------- | --------------------------------- |
| 4.1  | Schedule of all pending litigation                           | P0       | All           | Parties, claims, status, exposure |
| 4.2  | Schedule of all threatened litigation                        | P0       | All           | Demand letters, pre-action        |
| 4.3  | Schedule of all governmental investigations                  | P0       | All           | Agency, status, exposure          |
| 4.4  | Schedule of all arbitrations (pending and threatened)        | P0       | All           | Parties, claims, status           |
| 4.5  | Settlement agreements (past 5 years)                         | P1       | All           | Confidentiality provisions        |
| 4.6  | Consent decrees and regulatory orders                        | P0       | All           | Ongoing obligations               |
| 4.7  | Judgments and liens against the company                      | P0       | All           | Outstanding amounts               |
| 4.8  | Litigation insurance coverage (D&O, E&O, general liability)  | P1       | All           | Coverage adequacy                 |
| 4.9  | Litigation reserve analysis                                  | P1       | All           | Accounting treatment              |
| 4.10 | Legal hold notices                                           | P1       | Stock/Merger  | Preservation obligations          |
| 4.11 | Outside counsel engagement letters                           | P2       | All           | Scope, fees                       |
| 4.12 | Internal investigation reports                               | P1       | All           | If applicable                     |
| 4.13 | Product liability claims history                             | P0       | Manufacturing | If applicable                     |
| 4.14 | Employment litigation history                                | P1       | All           | Discrimination, wage/hour         |
| 4.15 | IP litigation history                                        | P0       | Tech          | Infringement claims               |
| 4.16 | Environmental litigation history                             | P0       | Industrial    | If applicable                     |
| 4.17 | Class action exposure analysis                               | P1       | US            | Consumer, securities, employment  |
| 4.18 | Whistleblower complaints                                     | P0       | All           | Internal and external             |
| 4.19 | Regulatory correspondence (warning letters, CIDs, subpoenas) | P0       | All           | Agency interactions               |
| 4.20 | Attorney-client privilege log (if sharing)                   | P2       | All           | Privilege protection              |

**Red Flags — Litigation:**

- Material pending litigation with significant exposure
- Pattern of similar claims (suggesting systemic issues)
- Government investigations or enforcement actions
- Uninsured or underinsured litigation exposure
- Litigation reserves that appear inadequate
- Class action exposure (especially securities or consumer)
- Outstanding judgments or consent decrees
- Whistleblower complaints (potential for escalation)
- Litigation involving key customers, suppliers, or personnel
- Matters where change of control could affect outcome

### Workstream 5: Employment and Labor

Review employment relationships, compensation, benefits, and labor compliance.

| #    | Request Item                                                          | Priority | Deal Type    | Notes                          |
| ---- | --------------------------------------------------------------------- | -------- | ------------ | ------------------------------ |
| 5.1  | Employee census (name, title, start date, salary, location, status)   | P0       | All          | Current workforce              |
| 5.2  | Organizational chart                                                  | P1       | All          | Reporting structure            |
| 5.3  | Employment agreements (executives and key employees)                  | P0       | All          | Terms, restrictions, severance |
| 5.4  | Offer letter templates (standard form)                                | P2       | All          | Standard terms                 |
| 5.5  | Employee handbook and policies                                        | P1       | All          | Current version                |
| 5.6  | Compensation structures (salary bands, bonus plans)                   | P1       | All          | Retention planning             |
| 5.7  | Commission and incentive plans                                        | P1       | All          | Variable compensation          |
| 5.8  | Equity incentive plans and grants                                     | P0       | Stock/Merger | Dilution, acceleration         |
| 5.9  | Change-of-control and golden parachute agreements                     | P0       | All          | Deal costs                     |
| 5.10 | Severance policies and agreements                                     | P0       | All          | Exposure if workforce changes  |
| 5.11 | Non-compete, non-solicitation, and confidentiality agreements         | P0       | All          | Restrictions, enforceability   |
| 5.12 | Independent contractor agreements                                     | P0       | All          | Classification risk            |
| 5.13 | Independent contractor classification analysis                        | P0       | All          | Misclassification exposure     |
| 5.14 | Collective bargaining agreements (union contracts)                    | P0       | All          | If applicable                  |
| 5.15 | Works council agreements or consultation records                      | P0       | EU           | [JURISDICTION-SPECIFIC]        |
| 5.16 | TUPE information (employees transferring)                             | P0       | Asset (UK)   | [JURISDICTION-SPECIFIC]        |
| 5.17 | WARN Act analysis (plant closing, layoffs)                            | P0       | US           | [JURISDICTION-SPECIFIC]        |
| 5.18 | Employee benefit plans (health, retirement, welfare)                  | P0       | Stock/Merger | Plan documents                 |
| 5.19 | 401(k)/pension plan documents and compliance testing                  | P0       | US Stock     | [JURISDICTION-SPECIFIC]        |
| 5.20 | ERISA compliance (fiduciary, prohibited transactions)                 | P0       | US Stock     | [JURISDICTION-SPECIFIC]        |
| 5.21 | Defined benefit pension plan funding status                           | P0       | Stock/Merger | Unfunded liabilities           |
| 5.22 | Retiree medical obligations                                           | P0       | Stock/Merger | OPEB liabilities               |
| 5.23 | Employment litigation history (discrimination, harassment, wage/hour) | P0       | All          | Claims history                 |
| 5.24 | EEOC charges or similar agency complaints                             | P0       | US           | [JURISDICTION-SPECIFIC]        |
| 5.25 | Workforce immigration compliance (I-9, visas, sponsorships)           | P1       | All          | Visa holders                   |
| 5.26 | Key employee retention risk assessment                                | P1       | All          | Flight risk                    |
| 5.27 | Restrictive covenant enforceability by state/jurisdiction             | P1       | US           | Varies by state                |
| 5.28 | Pay equity audits                                                     | P1       | All          | If conducted                   |
| 5.29 | Remote work policies and arrangements                                 | P2       | All          | Post-COVID workforce           |
| 5.30 | AI in employment (hiring, monitoring, evaluation)                     | P1       | All          | Compliance with emerging laws  |

**Red Flags — Employment:**

- Key executives without enforceable non-competes or non-solicits
- Change-of-control payments that significantly increase deal costs
- Equity acceleration that creates dilution or tax complications
- Unfunded or underfunded pension liabilities
- Wage and hour class action exposure
- Independent contractor misclassification risk
- Unionized workforce with upcoming contract negotiations
- Works council consultation requirements (EU) that could delay closing
- WARN Act exposure if workforce reductions planned
- Key employee retention concerns (flight risk post-announcement)
- Non-compete enforceability gaps in key jurisdictions

### Workstream 6: Regulatory and Compliance

Review regulatory status, permits, licenses, and compliance programs.

| #    | Request Item                                                      | Priority | Deal Type            | Notes                   |
| ---- | ----------------------------------------------------------------- | -------- | -------------------- | ----------------------- |
| 6.1  | List of all permits, licenses, and authorizations                 | P0       | All                  | By jurisdiction         |
| 6.2  | Permit/license renewal dates and requirements                     | P1       | All                  | Expiration risk         |
| 6.3  | Regulatory correspondence (past 3 years)                          | P1       | All                  | Agency interactions     |
| 6.4  | Regulatory inspection reports and findings                        | P0       | All                  | Deficiencies            |
| 6.5  | Consent decrees, enforcement orders, and compliance agreements    | P0       | All                  | Ongoing obligations     |
| 6.6  | FDA 483s, warning letters, and compliance history                 | P0       | Pharma/Med Device    | [JURISDICTION-SPECIFIC] |
| 6.7  | FCC licenses and compliance                                       | P1       | Telecom              | [JURISDICTION-SPECIFIC] |
| 6.8  | Financial services licenses (state and federal)                   | P0       | FinServ              | [JURISDICTION-SPECIFIC] |
| 6.9  | Healthcare licenses and Medicare/Medicaid certifications          | P0       | Healthcare           | [JURISDICTION-SPECIFIC] |
| 6.10 | Professional licenses (if employees require)                      | P1       | Professional Svcs    | By state/jurisdiction   |
| 6.11 | Anti-corruption/anti-bribery compliance program                   | P0       | All                  | FCPA, UK Bribery Act    |
| 6.12 | Anti-money laundering (AML) compliance program                    | P0       | FinServ              | BSA, FinCEN             |
| 6.13 | Sanctions compliance program and screening                        | P0       | All                  | OFAC, EU, UN            |
| 6.14 | Export control compliance (EAR, ITAR)                             | P0       | Tech/Mfg             | [JURISDICTION-SPECIFIC] |
| 6.15 | Trade compliance (tariffs, customs)                               | P1       | Mfg/Import           | Supply chain            |
| 6.16 | Industry-specific compliance certifications (SOC 2, ISO, PCI-DSS) | P1       | Tech                 | Customer requirements   |
| 6.17 | Code of conduct and ethics policy                                 | P1       | All                  | Current version         |
| 6.18 | Compliance training records                                       | P2       | All                  | Documentation           |
| 6.19 | Hotline/whistleblower reports and investigations                  | P0       | All                  | Trends, outcomes        |
| 6.20 | Third-party due diligence program (vendors, agents, distributors) | P1       | All                  | ABC compliance          |
| 6.21 | Lobbying disclosures and political contributions                  | P2       | All                  | If applicable           |
| 6.22 | Advertising and marketing compliance (FTC, ASA)                   | P1       | B2C                  | [JURISDICTION-SPECIFIC] |
| 6.23 | Product safety and recall history                                 | P0       | Consumer Products    | CPSC, EU                |
| 6.24 | AI Act compliance assessment                                      | P1       | AI/Tech (EU)         | [JURISDICTION-SPECIFIC] |
| 6.25 | Sector-specific regulatory approvals required for deal            | P0       | Regulated Industries | HSR, FCC, CFIUS, etc.   |

**Red Flags — Regulatory:**

- Licenses or permits that are non-transferable or require new applications
- Outstanding compliance deficiencies or warning letters
- Pattern of regulatory enforcement actions
- Material consent decrees or ongoing monitoring
- Anti-corruption red flags (high-risk countries, agent arrangements)
- Export control violations or near-violations
- Sector-specific regulatory approval uncertainty for the deal itself
- Pending regulatory investigations
- Inadequate compliance programs for the industry
- AI systems subject to EU AI Act prohibited or high-risk categories

### Workstream 7: Real Estate

Review real property ownership, leases, and use rights.

| #    | Request Item                                                   | Priority | Deal Type     | Notes                    |
| ---- | -------------------------------------------------------------- | -------- | ------------- | ------------------------ |
| 7.1  | Schedule of all owned real property                            | P0       | All           | Address, use, value      |
| 7.2  | Deeds and title insurance for owned properties                 | P0       | All           | Title confirmation       |
| 7.3  | Title reports or abstracts                                     | P0       | All           | Encumbrances             |
| 7.4  | Surveys and plats                                              | P1       | All           | Boundary issues          |
| 7.5  | Schedule of all leased real property                           | P0       | All           | Address, landlord, terms |
| 7.6  | Lease agreements (all locations)                               | P0       | All           | Full documents           |
| 7.7  | Lease amendments and side letters                              | P1       | All           | All modifications        |
| 7.8  | Subleases and sublicenses                                      | P1       | All           | If applicable            |
| 7.9  | Assignment/change-of-control consent requirements              | P0       | Asset/Stock   | Landlord consent         |
| 7.10 | Mortgages, deeds of trust, and security interests              | P0       | All           | Liens on property        |
| 7.11 | Zoning compliance certificates                                 | P1       | All           | Current use permitted    |
| 7.12 | Building permits (recent construction/renovation)              | P2       | All           | Proper permitting        |
| 7.13 | Certificate of occupancy                                       | P1       | All           | Legal occupancy          |
| 7.14 | Phase I environmental site assessments                         | P0       | All           | Environmental baseline   |
| 7.15 | Phase II environmental assessments (if Phase I flagged issues) | P0       | If applicable | Contamination            |
| 7.16 | Environmental remediation records                              | P0       | If applicable | Cleanup history          |
| 7.17 | Easements, rights-of-way, and access agreements                | P1       | All           | Property rights          |
| 7.18 | Condemnation/eminent domain proceedings                        | P1       | All           | If applicable            |
| 7.19 | Property tax records and appeals                               | P2       | All           | Assessed value           |
| 7.20 | Lease defaults or landlord disputes                            | P0       | All           | Current issues           |

**Red Flags — Real Estate:**

- Leases with change-of-control termination or consent requirements
- Environmental contamination requiring remediation
- Title defects or undisclosed liens
- Zoning violations or non-conforming use
- Leases expiring near-term without renewal rights
- Significant deferred maintenance
- Condemnation or eminent domain threats
- Landlord financial distress
- Critical facilities in flood zones or disaster-prone areas
- Lease guarantees from selling stockholders

### Workstream 8: Environmental

Review environmental compliance, liabilities, and sustainability matters.

| #    | Request Item                                            | Priority | Deal Type        | Notes                   |
| ---- | ------------------------------------------------------- | -------- | ---------------- | ----------------------- |
| 8.1  | Environmental permits and compliance records            | P0       | All              | All facilities          |
| 8.2  | Air emissions permits and monitoring                    | P0       | Industrial       | If applicable           |
| 8.3  | Water discharge permits (NPDES, etc.)                   | P0       | Industrial       | If applicable           |
| 8.4  | Hazardous waste manifests and disposal records          | P0       | Industrial       | If applicable           |
| 8.5  | Underground storage tank registrations                  | P0       | All              | UST compliance          |
| 8.6  | Toxic substance handling records (asbestos, PCBs, lead) | P0       | All              | Older facilities        |
| 8.7  | Phase I ESAs for all owned and leased properties        | P0       | All              | Environmental baseline  |
| 8.8  | Phase II ESAs and remediation records                   | P0       | If applicable    | Known contamination     |
| 8.9  | Environmental litigation and claims history             | P0       | All              | Past and pending        |
| 8.10 | Superfund site involvement (PRP status)                 | P0       | US               | [JURISDICTION-SPECIFIC] |
| 8.11 | Environmental insurance policies                        | P1       | All              | Pollution liability     |
| 8.12 | Environmental audits (internal and third-party)         | P1       | All              | Recent assessments      |
| 8.13 | EPA or state agency correspondence and NOVs             | P0       | US               | [JURISDICTION-SPECIFIC] |
| 8.14 | Environmental consent decrees or orders                 | P0       | All              | Ongoing obligations     |
| 8.15 | Climate-related disclosures and commitments             | P1       | All              | ESG/TCFD                |
| 8.16 | Carbon emissions data and reduction targets             | P1       | All              | Net-zero commitments    |
| 8.17 | Sustainability reports                                  | P2       | All              | Public disclosures      |
| 8.18 | Supply chain environmental due diligence                | P2       | All              | Scope 3 emissions       |
| 8.19 | Product environmental compliance (REACH, RoHS)          | P1       | EU Manufacturing | [JURISDICTION-SPECIFIC] |
| 8.20 | Environmental indemnities from prior transactions       | P1       | All              | Coverage                |

**Red Flags — Environmental:**

- Known contamination without remediation plan or funding
- Superfund (CERCLA) involvement or PRP status
- Environmental permit violations or enforcement actions
- Inadequate Phase I/II assessments for industrial properties
- Asbestos, PCBs, or lead in older facilities
- Underground storage tanks (USTs) without proper monitoring
- Environmental consent decrees with ongoing obligations
- Climate commitments that create legal exposure if unmet
- Inadequate environmental insurance for risk profile
- Indemnification gaps from prior acquisitions

### Workstream 9: Tax

Review tax compliance, attributes, and transaction-specific tax issues.

| #    | Request Item                                              | Priority | Deal Type           | Notes                   |
| ---- | --------------------------------------------------------- | -------- | ------------------- | ----------------------- |
| 9.1  | Federal income tax returns (past 5 years)                 | P0       | Stock/Merger        | All filed returns       |
| 9.2  | State/local income tax returns (past 5 years)             | P0       | Stock/Merger        | All jurisdictions       |
| 9.3  | Sales and use tax returns and compliance                  | P0       | All                 | Nexus analysis          |
| 9.4  | Payroll tax returns and compliance                        | P1       | All                 | Employment taxes        |
| 9.5  | Property tax returns and assessments                      | P1       | All                 | All properties          |
| 9.6  | International tax returns (foreign subsidiaries)          | P0       | Stock/Merger        | If applicable           |
| 9.7  | Tax audit history and current audits                      | P0       | All                 | Open issues             |
| 9.8  | IRS and state tax correspondence                          | P1       | All                 | Notices, disputes       |
| 9.9  | Tax reserves and uncertain tax positions (FIN 48/ASC 740) | P0       | Stock/Merger        | Accounting reserves     |
| 9.10 | NOL and credit carryforwards                              | P0       | Stock/Merger        | Available attributes    |
| 9.11 | Section 382 ownership change analysis                     | P0       | US Stock            | [JURISDICTION-SPECIFIC] |
| 9.12 | Transfer pricing studies and documentation                | P0       | Stock/Merger (intl) | Intercompany pricing    |
| 9.13 | Tax sharing agreements (intercompany)                     | P1       | Stock/Merger        | Allocation              |
| 9.14 | Tax indemnities from prior transactions                   | P1       | All                 | Coverage                |
| 9.15 | R&D tax credit documentation                              | P1       | Tech                | Substantiation          |
| 9.16 | QSBS qualification analysis                               | P1       | US Stock            | [JURISDICTION-SPECIFIC] |
| 9.17 | State nexus analysis                                      | P0       | US                  | Unregistered states     |
| 9.18 | Escheat/unclaimed property compliance                     | P1       | US                  | [JURISDICTION-SPECIFIC] |
| 9.19 | Proposed transaction tax structure and opinions           | P0       | All                 | Deal structuring        |
| 9.20 | FIRPTA analysis (if foreign sellers)                      | P0       | US                  | [JURISDICTION-SPECIFIC] |

**Red Flags — Tax:**

- Open tax audits with significant exposure
- Inadequate tax reserves for uncertain positions
- NOL carryforwards subject to Section 382 limitation
- State nexus issues (unregistered states where nexus exists)
- International tax compliance gaps (transfer pricing, GILTI, BEAT)
- Sales tax exposure from Wayfair nexus
- Unclaimed property (escheat) exposure
- Tax attributes that will be limited or lost in the transaction
- Prior transaction tax indemnities that are expiring or inadequate
- Tax structure of proposed transaction creates unexpected liabilities

### Workstream 10: Data Privacy and Cybersecurity

Review data protection compliance, privacy practices, and cybersecurity posture.

| #     | Request Item                                             | Priority | Deal Type            | Notes                   |
| ----- | -------------------------------------------------------- | -------- | -------------------- | ----------------------- |
| 10.1  | Privacy policy (current and historical versions)         | P0       | All                  | Public commitments      |
| 10.2  | Data processing agreements (DPAs) with vendors           | P0       | All                  | Processor compliance    |
| 10.3  | Sub-processor list and notification process              | P1       | All                  | GDPR requirement        |
| 10.4  | Data processing records (Article 30 records under GDPR)  | P0       | EU                   | [JURISDICTION-SPECIFIC] |
| 10.5  | Data protection impact assessments (DPIAs)               | P1       | EU                   | [JURISDICTION-SPECIFIC] |
| 10.6  | Cross-border data transfer mechanisms (SCCs, BCRs)       | P0       | International        | Transfer compliance     |
| 10.7  | Cookie/tracking consent mechanisms                       | P1       | B2C                  | ePrivacy compliance     |
| 10.8  | Data subject request handling procedures                 | P1       | All                  | DSAR compliance         |
| 10.9  | Data retention policies and schedules                    | P1       | All                  | Retention compliance    |
| 10.10 | Data breach history and incident response records        | P0       | All                  | Past incidents          |
| 10.11 | Breach notification records (to regulators, individuals) | P0       | All                  | Compliance history      |
| 10.12 | Information security policies and standards              | P1       | All                  | Written policies        |
| 10.13 | Cybersecurity certifications (SOC 2, ISO 27001, etc.)    | P1       | Tech                 | Compliance evidence     |
| 10.14 | Penetration test reports and vulnerability assessments   | P1       | Tech                 | Security posture        |
| 10.15 | Cybersecurity insurance policies                         | P1       | All                  | Coverage adequacy       |
| 10.16 | Vendor security assessments                              | P2       | All                  | Third-party risk        |
| 10.17 | Employee data handling training records                  | P2       | All                  | Training compliance     |
| 10.18 | Data inventory/mapping (what data, where stored, why)    | P0       | All                  | Data landscape          |
| 10.19 | AI/automated decision-making systems inventory           | P1       | AI/Tech              | GDPR Art. 22, AI Act    |
| 10.20 | CCPA/CPRA compliance (sale/sharing opt-out, SPI)         | P0       | US (CA consumers)    | [JURISDICTION-SPECIFIC] |
| 10.21 | State privacy law compliance (VA, CO, CT, etc.)          | P1       | US (multi-state)     | [JURISDICTION-SPECIFIC] |
| 10.22 | Children's privacy compliance (COPPA, KOSA)              | P0       | US (children's data) | [JURISDICTION-SPECIFIC] |
| 10.23 | Healthcare data compliance (HIPAA)                       | P0       | US Healthcare        | [JURISDICTION-SPECIFIC] |
| 10.24 | Financial data compliance (GLBA, PCI-DSS)                | P0       | FinServ              | [JURISDICTION-SPECIFIC] |
| 10.25 | Biometric data handling (BIPA, CIPA)                     | P0       | US (IL, TX)          | [JURISDICTION-SPECIFIC] |

**Red Flags — Data Privacy:**

- Data breach history without proper notification
- Inadequate data processing agreements with vendors
- Cross-border data transfers without valid mechanisms
- Privacy policy commitments that exceed actual practices
- No data inventory or mapping (don't know what data exists)
- GDPR/CCPA enforcement actions or complaints
- Biometric data collection without compliant consent (BIPA exposure)
- Automated decision-making affecting individuals without required safeguards
- Healthcare data (PHI) handling without HIPAA compliance
- Inadequate cybersecurity for the sensitivity of data held

### Workstream 11: Antitrust, Competition, and Foreign Investment

Review antitrust exposure and transaction-specific filing requirements.

| #     | Request Item                                   | Priority | Deal Type                     | Notes                   |
| ----- | ---------------------------------------------- | -------- | ----------------------------- | ----------------------- |
| 11.1  | HSR filing analysis (US)                       | P0       | All (if thresholds met)       | [JURISDICTION-SPECIFIC] |
| 11.2  | EU Merger Regulation (EUMR) analysis           | P0       | All (if thresholds met)       | [JURISDICTION-SPECIFIC] |
| 11.3  | CMA merger review analysis (UK)                | P0       | All (if thresholds met)       | [JURISDICTION-SPECIFIC] |
| 11.4  | CCI notification analysis (India)              | P0       | All (if thresholds met)       | [JURISDICTION-SPECIFIC] |
| 11.5  | ACCC merger review analysis (Australia)        | P0       | All (if thresholds met)       | [JURISDICTION-SPECIFIC] |
| 11.6  | Other merger control filings (by jurisdiction) | P1       | All                           | Multi-jurisdictional    |
| 11.7  | Market share data (relevant markets)           | P0       | All                           | Overlap analysis        |
| 11.8  | Competitor overlap analysis                    | P0       | All                           | Horizontal issues       |
| 11.9  | Vertical relationship analysis                 | P1       | All                           | Vertical issues         |
| 11.10 | Prior antitrust enforcement history            | P0       | All                           | Past issues             |
| 11.11 | Antitrust compliance program                   | P1       | All                           | Written program         |
| 11.12 | CFIUS analysis (national security)             | P0       | US (foreign acquirer)         | [JURISDICTION-SPECIFIC] |
| 11.13 | NSI Act analysis (UK)                          | P0       | UK (sensitive sectors)        | [JURISDICTION-SPECIFIC] |
| 11.14 | EU FDI Regulation analysis                     | P1       | EU (foreign acquirer)         | [JURISDICTION-SPECIFIC] |
| 11.15 | FIRB analysis (Australia)                      | P0       | AU (foreign acquirer)         | [JURISDICTION-SPECIFIC] |
| 11.16 | Press Note 3 analysis (India)                  | P0       | India (neighboring countries) | [JURISDICTION-SPECIFIC] |
| 11.17 | Sector-specific foreign ownership restrictions | P0       | All                           | Defense, telecom, etc.  |
| 11.18 | Gun-jumping risk analysis                      | P0       | All                           | Pre-closing conduct     |
| 11.19 | Expected timeline for regulatory approvals     | P0       | All                           | Closing condition       |
| 11.20 | Potential remedies or conditions               | P1       | All                           | If concerns identified  |

**Red Flags — Antitrust/FDI:**

- HSR or other merger filing requirements not yet analyzed
- Significant market share overlaps in concentrated markets
- Vertical integration creating foreclosure concerns
- Prior antitrust violations or consent decrees
- CFIUS or other foreign investment review risk
- National security implications (critical technology, infrastructure)
- Potential for extended regulatory review timeline
- Likely requirement for divestitures or behavioral remedies
- Gun-jumping risk from pre-closing integration planning
- Sector-specific foreign ownership restrictions (telecom, defense, media)

### Workstream 12: Insurance

Review insurance coverage and claims history.

| #     | Request Item                                       | Priority | Deal Type             | Notes                    |
| ----- | -------------------------------------------------- | -------- | --------------------- | ------------------------ |
| 12.1  | Schedule of all insurance policies                 | P0       | All                   | All coverage types       |
| 12.2  | Commercial general liability (CGL) policies        | P0       | All                   | Current and tail         |
| 12.3  | Product liability insurance                        | P0       | Manufacturing         | If applicable            |
| 12.4  | Professional liability / E&O insurance             | P0       | Professional Services | If applicable            |
| 12.5  | Directors and officers (D&O) insurance             | P0       | Stock/Merger          | Tail coverage            |
| 12.6  | Employment practices liability (EPL) insurance     | P1       | All                   | Coverage adequacy        |
| 12.7  | Cyber/privacy liability insurance                  | P0       | All                   | Coverage adequacy        |
| 12.8  | Property and casualty insurance                    | P1       | All                   | Asset coverage           |
| 12.9  | Workers' compensation insurance                    | P1       | All                   | Compliance               |
| 12.10 | Business interruption insurance                    | P1       | All                   | Coverage adequacy        |
| 12.11 | Environmental/pollution liability insurance        | P0       | Industrial            | If applicable            |
| 12.12 | Key person insurance                               | P2       | All                   | If applicable            |
| 12.13 | Claims history (past 5 years)                      | P0       | All                   | All policies             |
| 12.14 | Pending insurance claims                           | P0       | All                   | Open claims              |
| 12.15 | Insurance broker contact and relationship          | P2       | All                   | Continuity               |
| 12.16 | Change-of-control provisions in policies           | P0       | All                   | Coverage continuity      |
| 12.17 | Self-insured retentions and deductibles            | P1       | All                   | Exposure                 |
| 12.18 | Rep and warranty insurance (if being obtained)     | P0       | All                   | If applicable            |
| 12.19 | Certificate of insurance requirements in contracts | P2       | All                   | Customer requirements    |
| 12.20 | Loss runs (carrier-issued claims history)          | P1       | All                   | Independent verification |

**Red Flags — Insurance:**

- Inadequate coverage limits for the risk profile
- Material exclusions in key policies
- Claims history suggesting underlying operational issues
- D&O tail coverage issues for selling directors
- Change-of-control provisions that terminate coverage
- Self-insured retentions that create significant exposure
- Lapsed policies or coverage gaps
- Insurance requirements in contracts that are not met
- Prior insurance claims that affect renewability or pricing
- Rep and warranty insurance exclusions that leave gaps

---

## Red Flag Classification

Classify each red flag identified during diligence using this severity framework:

### CRITICAL — Deal Stopper

Issues that may prevent the transaction from proceeding or fundamentally change deal
economics. Require immediate escalation to deal team leadership and client decision-makers.

**Examples:**

- Target does not have clear title to key assets
- Material fraud or financial statement manipulation discovered
- Regulatory approval is unlikely or would require unacceptable remedies
- Unknown liabilities exceed deal value cushion
- Key contracts terminate on change of control with no consent path
- Intellectual property is not owned by the target
- Criminal investigation or serious regulatory enforcement pending

**Action**: Immediate escalation. Deal pause until resolved or decision to walk made.

### HIGH — Material Issue

Issues that significantly affect deal value, require contract protection (indemnity, escrow,
purchase price adjustment), or necessitate pre-closing remediation. Require deal team and
client attention.

**Examples:**

- Material litigation exposure above diligence threshold
- Key customers or suppliers with termination rights
- Regulatory compliance gaps requiring remediation
- Tax exposure requiring reserves or indemnification
- Employment liabilities (misclassification, pension underfunding)
- Environmental remediation obligations
- Data privacy compliance gaps in regulated environment

**Action**: Detailed analysis and recommendation. Include in issues list for transaction
document negotiation. Consider purchase price adjustment, indemnity, or escrow.

### MEDIUM — Notable Issue

Issues that are below materiality thresholds but warrant disclosure, monitoring, or minor
contract protection. May affect integration planning.

**Examples:**

- Minor litigation or claims within normal business operations
- Contracts requiring consent (obtainable) for assignment
- Permit renewals pending
- Policy or procedure gaps requiring post-closing attention
- Ordinary-course regulatory matters
- Insurance coverage gaps (correctable)
- Employment handbook updates needed

**Action**: Document in diligence report. Address in disclosure schedules. May warrant
representation/warranty language but not specific indemnity.

### LOW — Noted Item

Issues identified for completeness that do not affect the transaction. Informational only.

**Examples:**

- Minor administrative gaps in corporate records
- Expired but non-critical contracts
- Standard-course regulatory correspondence
- Immaterial pending matters
- Documentation improvements needed post-closing

**Action**: Note in diligence report. No transaction document action required.

---

## Status Tracking

Track diligence status for each workstream and request item:

### Status Options

| Status          | Definition                             |
| --------------- | -------------------------------------- |
| **Not Started** | Request not yet sent to target         |
| **Requested**   | Request sent, awaiting response        |
| **Partial**     | Some documents received, more expected |
| **Received**    | All requested documents received       |
| **In Review**   | Received and under review              |
| **Complete**    | Review complete, findings documented   |
| **Red Flag**    | Issue identified requiring escalation  |
| **N/A**         | Not applicable to this transaction     |

### Tracking Template

| Workstream   | Item              | Priority | Status    | Owner  | Due Date | Notes            |
| ------------ | ----------------- | -------- | --------- | ------ | -------- | ---------------- |
| 1. Corporate | 1.1 Charter       | P0       | Complete  | [Name] | [Date]   | Clean            |
| 2. Contracts | 2.1 Top customers | P0       | In Review | [Name] | [Date]   | 3 of 10 reviewed |

### Progress Dashboard

Generate summary statistics:

- % complete by workstream
- Outstanding P0 items
- Red flags identified
- Days until expected completion
- Blockers and delays

---

## Findings Summary Format

Structure diligence findings for transaction documentation:

### Executive Summary

```markdown
## Legal Due Diligence Summary

**Transaction**: [Acquirer] acquisition of [Target]
**Transaction Type**: [Asset Purchase / Stock Purchase / Merger]
**Date**: [Report date]
**Prepared by**: [Firm/Counsel name]
**Status**: [Draft / Final]

### Key Statistics

- Workstreams reviewed: 12
- Request items: [count]
- Documents reviewed: [count]
- Red flags: [count] Critical / [count] High / [count] Medium

### Critical Issues (Deal Stoppers)

1. [Issue] — [Brief description and status]

### High-Priority Issues (Material)

1. [Issue] — [Brief description and recommended protection]
2. [Issue] — [Brief description and recommended protection]

### Summary by Workstream

| Workstream          | Status      | Red Flags | Key Finding             |
| ------------------- | ----------- | --------- | ----------------------- |
| Corporate Structure | Complete    | 0         | Clean capitalization    |
| Material Contracts  | In Progress | 2 High    | Customer COC provisions |
| ...                 | ...         | ...       | ...                     |

### Recommended Transaction Protections

1. [Indemnity for X]
2. [Escrow for Y]
3. [Purchase price adjustment for Z]

### Open Items

1. [Item requiring follow-up]

### Glass Box Audit Trail

[YAML block per specification]
```

### Detailed Findings by Workstream

For each workstream, provide:

- Summary of review scope
- List of documents reviewed
- Findings (organized by severity)
- Recommended actions
- Open items

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                             | Fail Action                         |
| -------------- | -------------------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established principle | Add citation or mark "[VERIFY]"     |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction      | Fix format                          |
| **Currency**   | Every cited provision checked for amendments or repeal                           | Flag "[CHECK CURRENCY]"             |
| **Domain**     | Analysis stays within applicable jurisdiction(s)                                 | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated, not hidden                                        | Add confidence qualifier            |

### Self-Interrogation for CRITICAL Items

For any issue classified as CRITICAL, apply this 3-pass review before finalizing:

**Pass 1 — Factual Accuracy**:

- Is this finding supported by documents actually reviewed?
- Have we misread or misinterpreted the document?
- Is there additional context that would change the conclusion?

**Pass 2 — Legal Analysis**:

- Does the legal conclusion follow from the applicable law?
- Have we applied the correct jurisdiction's law?
- Are there counterarguments or mitigating factors?

**Pass 3 — Materiality**:

- Is this truly CRITICAL or could it be HIGH with mitigation?
- What would it take to resolve this issue?
- Is there a path forward if this is addressed?

If any pass reveals a weakness, revise the classification or analysis before delivery.
Mark the audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material finding, assign a confidence level:

| Level        | Range     | Meaning                                      | Action                               |
| ------------ | --------- | -------------------------------------------- | ------------------------------------ |
| **Definite** | 0.95-1.0  | Clear document, unambiguous finding          | State with confidence                |
| **High**     | 0.80-0.94 | Strong basis, minor interpretation questions | State with brief caveat              |
| **Probable** | 0.60-0.79 | Good arguments but some ambiguity            | State with explicit reasoning        |
| **Possible** | 0.40-0.59 | Uncertain, need more information             | Flag for follow-up                   |
| **Unlikely** | 0.0-0.39  | Speculative, limited basis                   | Do not assert; flag as "[UNCERTAIN]" |

---

## Glass Box Audit Trail

Every due diligence output MUST include a Glass Box audit section:

```yaml
glass_box:
  transaction: "[Transaction description]"
  transaction_type: "[Asset Purchase / Stock Purchase / Merger]"
  target_company: "[Target name]"
  target_jurisdiction: "[Primary jurisdiction]"
  acquirer_role: "[Buyer / Seller / Advisor]"
  deal_playbook: "[Playbook name or 'Market standards']"
  workstreams_reviewed: 12
  request_items_total: "[count]"
  documents_reviewed: "[count]"
  red_flags_critical: "[count]"
  red_flags_high: "[count]"
  red_flags_medium: "[count]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  jurisdictions_analyzed:
    - "[Jurisdiction 1]"
    - "[Jurisdiction 2]"
  key_statutes_consulted:
    - "[Statute 1 — VERIFIED / UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations or caveats]"
  reviewer: "AI-assisted — requires qualified M&A counsel review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in M&A due diligence:

1. **One-size-fits-all checklists** — Applying the same checklist to asset and stock
   purchases without adjusting for fundamental structural differences. Asset purchases
   need title verification and assignability; stock purchases need comprehensive liability
   review.

2. **Missing the liability waterfall** — In stock purchases, assuming the purchase
   agreement's representations and warranties are the only liability protection. If
   diligence misses an issue, the rep may be breached but uncollectible (seller insolvency,
   basket/cap limitations, survival period expiration).

3. **Ignoring change-of-control provisions** — Failing to identify contracts with change-
   of-control termination or consent provisions until after signing. Key customers
   disappearing post-closing is a disaster, not a warranty claim.

4. **Superficial IP diligence** — Taking a patent schedule at face value without verifying
   ownership chain, prosecution status, and freedom-to-operate. IP is often the primary
   value driver in tech acquisitions; superficial diligence is malpractice.

5. **Employment as afterthought** — Treating employment diligence as administrative rather
   than material. Change-of-control payments, equity acceleration, WARN obligations, and
   key employee retention are transaction-critical.

6. **Regulatory approval timeline optimism** — Assuming antitrust, CFIUS, or sector-
   specific regulatory approvals will close on the expected timeline without analyzing
   actual deal complexity and agency workload.

7. **Incomplete document review** — Reviewing the form customer contract but not the
   individual customer agreements (which may have negotiated deviations). The devil is
   in the amendments and side letters.

8. **Ignoring data rooms** — Treating the data room as a checkbox rather than a diligence
   tool. Virtual data rooms track what was provided and when; gaps in production are
   themselves red flags.

9. **Failing to cross-reference** — Reviewing workstreams in isolation without cross-
   referencing. A contract issue may reveal litigation risk; an employment matter may
   have tax implications; an IP license may create antitrust concerns.

10. **Missing seller disclosure schedule strategy** — Focusing only on buyer diligence
    without understanding that findings will be used to negotiate disclosure schedules.
    What is disclosed limits (or expands) seller exposure under representations.

11. **Forgetting post-signing obligations** — Treating signing as the end of diligence.
    Between signing and closing, covenants require monitoring, bring-down conditions
    must be tracked, and material adverse changes must be assessed.

12. **No materiality discipline** — Flagging everything without prioritization. A 500-item
    issues list is as useless as no list. Apply materiality thresholds and prioritize
    what matters for the deal.

13. **Cutting jurisdictional corners** — Applying US law assumptions to UK targets, or
    vice versa. TUPE exists in the UK; it does not exist in the US. Works councils
    exist in Germany; they do not exist in Delaware. Jurisdiction matters.

14. **Rep and warranty insurance as substitute** — Treating R&W insurance as a replacement
    for diligence rather than a complement. Insurers rely on quality diligence; undisclosed
    issues may void coverage; exclusions limit protection.

15. **Not documenting what wasn't reviewed** — Failing to note scope limitations and
    documents not provided. If an issue emerges post-closing that was in documents
    withheld from diligence, the record matters.

16. **Single reviewer without quality check** — Having one associate review an entire
    workstream without senior review or cross-check. Diligence is a team sport; quality
    control is essential.

17. **Ignoring the target's own diligence** — In competitive auctions, not considering
    that multiple bidders received the same data room. What you found, others found.
    What you missed, others may have caught.

---

## Writing Standards

Apply plain-language discipline to all diligence output:

**For client reports:**

- Lead with findings, not process
- State conclusions first, then support
- Use severity classifications consistently
- Quantify exposure where possible
- Recommend specific actions
- Keep executive summary to 2 pages maximum

**For internal work product:**

- Document what was reviewed and what was not
- Note open items and follow-ups
- Track responsibility and deadlines
- Cross-reference related issues across workstreams

**Quality gates before delivery:**

1. Can a non-lawyer deal team member understand the executive summary?
2. Is every CRITICAL and HIGH finding actionable?
3. Are severity classifications applied consistently?
4. Are all open items captured with owners and due dates?
5. Is the Glass Box audit trail complete?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- Search for jurisdiction-relevant corporate statutes and M&A regulations
- Verify antitrust thresholds and foreign investment screening requirements
- Research sector-specific regulatory requirements
- Check recent enforcement actions and regulatory guidance
- Save results to `/tmp/legalcode-ma-dd-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED

**Without legalcode-mcp:**

- Mark every statutory reference with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Recommend independent verification of legal requirements
- Focus on structural diligence framework and checklist completeness

---

## Industry-Specific Additions

Add the following workstream items based on target industry:

### Technology / Software / SaaS

- Open-source software inventory and license compliance
- SaaS metrics (ARR, MRR, churn, NRR, CAC, LTV)
- SOC 2 Type II reports
- Customer data handling and cloud infrastructure
- AI/ML model documentation and training data provenance
- API and integration agreements
- SLA compliance and uptime records

### Healthcare / Life Sciences

- FDA product approvals and compliance history
- Clinical trial records and results
- Medicare/Medicaid certifications
- HIPAA compliance program
- Stark Law and Anti-Kickback compliance
- Physician relationship agreements
- Medical device registrations
- Drug pricing compliance (340B, Medicaid rebate)

### Financial Services

- Regulatory licenses by jurisdiction
- Capital adequacy and reserve requirements
- BSA/AML compliance program
- FINRA/SEC examination history
- Consumer financial protection compliance
- Fair lending analysis
- Loan portfolio quality metrics

### Manufacturing / Industrial

- Product certifications and testing
- Supply chain documentation
- Quality management systems (ISO 9001)
- Equipment condition assessments
- Warranty reserve analysis
- Product recall history
- OSHA compliance and safety records

### Consumer / Retail

- Product safety compliance (CPSC, CE marking)
- Advertising and marketing compliance (FTC, ASA)
- E-commerce terms and consumer protection
- Franchise disclosure compliance
- Import/export compliance
- Food safety (if applicable)

### Energy / Utilities

- FERC and state utility commission authorizations
- Environmental permits and compliance
- Power purchase agreements
- Interconnection agreements
- Renewable energy credits and certificates
- Rate case history

---

## Output Format Template

Structure the final checklist deliverable as:

```markdown
## M&A Legal Due Diligence Checklist

**Transaction**: [Acquirer] [acquisition type] of [Target]
**Transaction Type**: [Asset Purchase / Stock Purchase / Merger]
**Target Jurisdiction**: [Primary jurisdiction]
**Deal Timeline**: [Expected signing] / [Expected closing]
**Prepared for**: [Client]
**Prepared by**: [Firm/Counsel]
**Date**: [Date]
**Version**: [Draft / Final]

---

## Executive Summary

[2-3 paragraph summary of transaction context, diligence approach, and key findings]

### Transaction-Type Considerations

[Deal-type-specific focus areas and risk profile]

### Key Findings

| Severity | Count | Summary                          |
| -------- | ----- | -------------------------------- |
| CRITICAL | [N]   | [One-line summary]               |
| HIGH     | [N]   | [One-line summary]               |
| MEDIUM   | [N]   | [Noted for disclosure schedules] |

### Recommended Transaction Protections

1. [Specific protection]
2. [Specific protection]

---

## Due Diligence Checklist

[Full checklist organized by workstream, with status tracking]

---

## Red Flags and Issues

[Detailed findings organized by severity, with recommended actions]

---

## Regulatory Approval Analysis

[Antitrust, FDI, and sector-specific approval requirements and timeline]

---

## Open Items and Follow-Ups

| Item | Workstream | Owner | Due Date | Status |
| ---- | ---------- | ----- | -------- | ------ |

---

## Glass Box Audit Trail

[YAML block per specification]
```

---

## Localization Notes

This skill is jurisdiction-agnostic by design. To create a jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with verified local legal requirements
2. Add jurisdiction-specific workstream items
3. Update antitrust and FDI filing thresholds
4. Add local employment law requirements (TUPE, works councils, etc.)
5. Include local language requirements for documents
6. Update the frontmatter name and description

Target jurisdiction variants (roadmap):

- **United States (Federal + Delaware focus)**
- **United Kingdom (England & Wales)**
- **European Union (multi-member-state)**
- **India**
- **Australia**

---

## Provenance

Created by Legalcode (2026-02-28). Original synthesis combining M&A due diligence best
practices from multiple sources including Bloomberg Law, Wachtell Lipton, Chambers
Corporate M&A guides, and practitioner experience. Informed by existing imported skills
(`imported-*-dd-checklist`) with Legalcode enhancements for transaction-type differentiation,
jurisdiction markers, quality frameworks, and comprehensive legal workstream coverage.

Research sources consulted:

- [Bloomberg Law M&A Due Diligence Checklist](https://pro.bloomberglaw.com/insights/contracts/ma-due-diligence-checklist/)
- [Wachtell Lipton Cross-Border M&A Guide 2024](https://www.wlrk.com/)
- [Chambers Corporate M&A 2025 Practice Guides](https://practiceguides.chambers.com/practice-guides/corporate-ma-2025)
- [FTC 2026 HSR Notification Thresholds](https://www.gibsondunn.com/ftc-publishes-revised-hart-scott-rodino-notification-thresholds-for-2026/)
- [Diligent M&A Due Diligence Checklist](https://www.diligent.com/resources/blog/mergers-acquisitions-due-diligence-checklist)
