---
name: legalcode-data-room-organizer
description: Organizes and audits Virtual Data Rooms (VDRs) for M&A transactions, debt financing, IPO/capital
  markets, and venture/growth equity. Use when setting up a sell-side or buy-side data room, auditing
  an existing data room for completeness, preparing an information request list, generating a VDR index
  for transaction documentation, or configuring access controls for multi-bidder auction, competitive
  financing, or IPO processes.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Organizes and audits Virtual Data Rooms (VDRs) for M&A transactions, debt financing, IPO/capital markets, and venture/growth equity. Generates standard folder taxonomy tailored to transaction type, classifies and tags documents, identifies gaps against comprehensive diligence checklists, produces a numbered VDR index, and recommends granular access permission tiers. Use when setting up a sell-side or buy-side data room, auditing an existing data room for completeness, preparing an information request list, generating a VDR index for transaction documentation, or configuring access controls for multi-bidder auction, competitive financing, or IPO processes. Triggers on "data room setup", "VDR organization", "virtual data room structure", "data room gap analysis", "information request list", "data room index", "VDR permissions", "data room checklist", "sell-side data room", "buy-side data room", "data room audit", or any mention of Intralinks / Datasite / Merrill Datasite / iDeals / ShareVault / FirmRoom / Ansarada in the context of transaction preparation. Jurisdiction-agnostic with transaction-type and sector-specific markers.


# Legalcode Data Room Organizer

> **Disclaimer**: This skill provides a framework for AI-assisted VDR organization and
> diligence gap analysis. It does not constitute legal advice. All outputs should be
> reviewed by qualified transaction counsel and financial advisors licensed in the relevant
> jurisdiction(s) before use. Data room structure and document completeness requirements
> vary by transaction type, jurisdiction, industry sector, and counterparty expectations.
> Laws and regulatory requirements change; verify current applicability before relying on
> any provision described here. References to document requirements cited from memory
> carry hallucination risk — verify against authoritative sources and deal-specific
> guidance before relying on them.

## Purpose and Scope

This skill organizes, audits, and optimizes Virtual Data Rooms for any transaction type.
It transforms an unstructured document archive into a well-organized, permission-governed,
indexed data room that accelerates due diligence and protects seller/issuer interests.

**Covers:**

- Standard VDR folder taxonomy by transaction type (M&A, debt financing, IPO, venture equity)
- Document classification and tagging (confidentiality tier, status, workstream)
- Gap analysis against comprehensive diligence checklists (per transaction type)
- Numbered VDR index generation (Excel/markdown format)
- Access permission recommendations (admin, advisor, bidder tiers, clean team)
- Q&A process setup guidance
- Anti-patterns and common data room mistakes
- Glass Box audit trail for traceability

**Does not:**

- Conduct legal due diligence (see `legalcode-ma-due-diligence-checklist`)
- Draft or review transaction documents (see contract review skills)
- Provide binding advice on what must be disclosed (requires jurisdiction-specific counsel)
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with markers

**Related skills:**

- `legalcode-ma-due-diligence-checklist` — generates the diligence request list this skill checks against
- `legalcode-due-diligence-report` — converts DD findings into executive-ready reports
- `legalcode-purchase-agreement-review` — clause-level review of the SPA/APA
- `legalcode-letter-of-intent-review` — reviews the LOI/term sheet before data room opens

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The transaction's governing jurisdiction and the
target's operating jurisdictions determine what documents must be included.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

**United States:**

- SEC disclosure requirements for public company targets (Form 10-K, proxy statements)
- HSR/CFIUS filing requirements affecting what documents must be prepared [VERIFY]
- State corporate law records requirements (Delaware vs. non-Delaware entities)
- ERISA documentation for benefit plans [VERIFY]
- Securities Act registration documents for IPO (Form S-1, comfort letters)
- State bulk sales law compliance documentation (where not repealed) [VERIFY]

**European Union / UK:**

- Merger Regulation disclosure requirements (EU MR 139/2004) for FDI-screened deals [VERIFY]
- UK National Security and Investment Act 2021 notification requirements [VERIFY]
- GDPR/UK GDPR: data room itself must comply with data protection requirements; minimize
  personal data in the VDR and use appropriate access controls [VERIFY]
- Companies Act 2006 (UK) — statutory books, company filings at Companies House
- Notarization and apostille requirements for certain document types

**Other jurisdictions:**

- Disclosure obligations under local M&A rules (e.g., Takeover Panel rules in UK for
  public M&A, SEBI Takeover Code in India, foreign investment screening in Germany/France)
- Local language requirements (some jurisdictions require contracts in the local language —
  check whether English translations suffice or originals must be uploaded)
- Registration requirements for notarized documents, land registers, IP registers

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the transaction type, user's role, and scope, the workflow pauses and asks when:

- The transaction type materially changes the folder taxonomy (M&A vs. IPO vs. financing)
- The user's side (sell-side vs. buy-side) affects what to organize vs. what to request
- Industry-specific documentation requirements are not yet established
- Scope decisions need to be made (full taxonomy vs. gap audit vs. index only)

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

### Step 1: Accept Input

Accept the task in any of these formats:

- **Existing data room contents**: A file list, index, or folder tree of an existing VDR
- **Document archive path**: Local path to a folder of uploaded documents
- **Transaction description**: Description of the transaction (type, parties, industry)
- **Gap analysis request**: Request to check an existing data room against a checklist
- **Index generation request**: Request to produce a numbered VDR index from a file list

If no data room contents are provided but a transaction description is given, proceed to
generate the target taxonomy and checklist so the user can populate the data room against it.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user these questions. Present as structured options:

1. **Transaction type**: What kind of transaction is this data room for?
   - Options: M&A — Stock/Share Purchase, M&A — Asset Purchase, M&A — Merger,
     Debt Financing — Syndicated/Term Loan, Debt Financing — High-Yield Bond,
     Debt Financing — Project Finance, IPO / Capital Markets, Venture/Growth Equity
     Fundraising, PE Secondary Transaction, Multi-purpose (specify)
   - _Why this matters_: The folder taxonomy, document requirements, and access permission
     structure differ significantly across transaction types.

2. **User's role**: Which side are you on?
   - Options: Sell-Side (organizing the data room for buyers/investors), Buy-Side
     (conducting diligence; need a request list and gap audit), Financing Party (lender
     or underwriter reviewing the data room)
   - _Why this matters_: Sell-side and buy-side have mirror-image needs. Sell-side sets
     up and controls; buy-side audits and requests.

3. **Industry sector**: What industry is the target/issuer in?
   - Options: Technology/SaaS, Life Sciences/Pharma, Financial Services/Fintech,
     Real Estate, Energy/Resources, Consumer/Retail, Industrials/Manufacturing,
     Healthcare Services, Other (specify)
   - _Why this matters_: Regulated industries require sector-specific document sections
     (e.g., FDA approvals for pharma, banking licenses for fintech, environmental
     permits for energy).

4. **Scope of this task**: What do you need?
   - Options: Full taxonomy setup (generate the target folder structure), Gap audit
     (compare existing data room against checklist), Index generation (produce a numbered
     document index), Access permissions design (configure user groups and tiers),
     All of the above
   - _Why this matters_: Determines which workflow modules to activate.

5. **Process stage**: Where are you in the transaction?
   - Options: Pre-launch (building the data room before first-round bids), First-round
     access (management presentations stage), Second-round/final diligence, Post-LOI/pre-
     signing, Regulatory approval period, Post-closing
   - _Why this matters_: Data room completeness expectations and access permissions vary
     materially by stage.

If the user provides partial context, proceed with what you have and state assumptions
explicitly (e.g., "I'm assuming this is a sell-side M&A data room for a tech company —
let me know if that's wrong").

### Step 3: Load Transaction-Specific Framework

Based on the transaction type confirmed in Step 2, load the appropriate folder taxonomy
and document checklist from the **VDR Taxonomy Reference** section below.

**⟁ CLARIFY** — If the transaction has unusual features, confirm before proceeding:

- Cross-border targets in multiple jurisdictions (need multi-jurisdiction document sections)
- Public company target (requires SEC/regulatory filing sections and public document handling)
- Highly regulated sector (life sciences, banking, insurance — need regulatory section expansion)
- Carve-out transaction (requires separation documentation, TSA exhibits, shared services)
- Distressed transaction (may have limited documentation availability; note gaps differently)

### Step 4: Audit Existing Data Room (if provided)

If the user has provided an existing data room file list, folder tree, or index:

1. **Map to the standard taxonomy**: Categorize each existing document against the standard
   folder structure for the transaction type. Identify which folders are populated and which
   are empty or sparse.

2. **Apply the Document Status Classification** to each identified document category:
   - **POPULATED** — Category has sufficient documents; no immediate action required
   - **PARTIAL** — Some documents present but key items are missing; remediation needed
   - **MISSING** — No documents in this category; escalate to preparation team

3. **Generate gap report**: List every PARTIAL and MISSING category with:
   - What is expected (specific document list)
   - What is present (if anything)
   - Gap severity (CRITICAL / IMPORTANT / STANDARD — see Classification section below)
   - Recommended action

4. **Check naming conventions**: Flag documents with:
   - Multiple version suffixes (v1, v2, final, final-final) — standardize to one current version
   - Special characters, spaces in filenames — replace with underscores/hyphens
   - Missing dates on time-sensitive documents
   - Inconsistent casing or abbreviations across folders

### Step 5: Generate VDR Taxonomy

Produce the target folder structure for the transaction type. Use the detailed hierarchies
from the **VDR Taxonomy Reference** section. For each folder, specify:

- **Folder number and name** (1.0 Corporate, 1.1 Formation Documents, etc.)
- **What belongs here** (specific document types)
- **Minimum completeness expectation** (for gap analysis)
- **Confidentiality tier** (Standard / Confidential / Restricted)
- **Access tier** (who can see this folder — see Access Permissions section)

**⟁ CLARIFY** — For sector-specific expansions, confirm with the user which additional
sections to add:

- Life Sciences: FDA filings, clinical trial data, regulatory approvals, CMC documentation
- Financial Services: Banking licenses, capital adequacy, regulatory exam reports, AML/KYC
- Real Estate: Title reports, surveys, zoning, environmental assessments, rent rolls
- Energy: Environmental permits, FERC/offtake agreements, resource reports, lease rights

### Step 6: Configure Access Permissions

Design the user group structure and permission matrix for the data room. Apply the
**Access Permission Framework** from the dedicated section below.

**⟁ CLARIFY** — Ask about specific permission requirements:

- Is this a competitive multi-bidder process? (requires bidder group isolation)
- Are any bidders competitors to the target? (requires clean team configuration)
- Are there management-exclusion documents (comp plans, board materials sensitive to mgmt)?
- Does the process include multiple rounds with expanding access?

### Step 7: Generate VDR Index

Produce a numbered document index for all items in the data room. Structure as:

```
[Section #].[Subsection #].[Document #]  [Document Name]  [Date]  [Status]  [Notes]
```

Example:

```
1.1.001  Certificate of Incorporation (Delaware)  2019-03-15  Final
1.1.002  Certificate of Amendment (Series A)       2021-06-01  Final
1.2.001  Bylaws (as amended)                       2023-11-30  Final
1.2.002  Second Amended and Restated Bylaws        2024-08-14  Draft — pending board approval
```

Generate the index in markdown table format (for easy copy-paste into Excel or VDR export).

### Step 8: Produce Gap Report

Present the gap report in the format defined in the **Output Format Template** below.
Organize findings by:

- CRITICAL gaps (must be resolved before data room launch or first-round access)
- IMPORTANT gaps (should be resolved before management presentations)
- STANDARD gaps (should be resolved before final due diligence)

For each gap, provide a specific remediation action, not just a label.

### Step 9: Q&A Process Recommendations

Provide setup guidance for the data room Q&A module:

- How to assign Q&A routing (who receives which question types)
- Process for ensuring consistent answers to all bidder groups
- Template for Q&A response format
- Policy on unilateral disclosures (answers that benefit all parties, shared simultaneously)
- Lockdown periods for Q&A (when question submission closes relative to bid deadlines)

### Step 10: Quality Verification

Before delivering the output, run the quality checks in the **Quality Assurance Framework**:

1. Run Citation Quality Gates for any legal or regulatory claims in the output.
2. For any CRITICAL gap, run the Self-Interrogation to verify the classification.
3. Confirm completeness: all relevant checklist categories addressed.
4. Generate the Glass Box audit trail.

---

## VDR Taxonomy Reference

### Transaction Type 1: M&A — Stock/Share Purchase

**Priority folders**: Corporate (cap table critical), Contracts (key customer/vendor),
Financial, IP (ownership chain), Tax (multi-year), Litigation, Employment (key people).

```
1.0  CORPORATE STRUCTURE & GOVERNANCE
  1.1  Formation Documents
       Certificate/Articles of Incorporation (all amendments)
       Bylaws (all amendments)
       Good Standing Certificates (all jurisdictions)
       Foreign Qualification Documents
       Registered Agent Documentation
  1.2  Capitalization
       Capitalization Table (fully diluted, as of close date)
       Stock Ledger / Register of Members
       Stock Certificates (all issued shares)
       Option / Warrant Ledger
       Rights of First Refusal / Co-Sale Agreements
  1.3  Governance Documents
       Board Minutes (all meetings, 3–5 years)
       Committee Minutes (Audit, Compensation, Nominating)
       Stockholder / Shareholder Meeting Minutes (3–5 years)
       Unanimous Written Consents (all)
       Organizational Chart (current)
  1.4  Stockholder / Shareholder Agreements
       Investors' Rights Agreement
       Voting Agreement
       Co-Sale Agreement / Tag-Along
       Drag-Along Agreement
       Right of First Refusal Agreements
       Lock-Up Agreements

2.0  FINANCIAL INFORMATION
  2.1  Historical Financial Statements
       Audited Financial Statements (3 fiscal years)
       Auditor's Reports and Management Letters
       Unaudited Interim Financial Statements (current year)
  2.2  Projections and Forecasts
       Management Projections (most recent board-approved)
       Budget vs. Actuals (current year)
       Long-Range Financial Plan
  2.3  Working Capital
       Working Capital Analysis and Methodology
       Accounts Receivable Aging
       Accounts Payable Aging
       Inventory Schedules
  2.4  Debt and Banking
       Bank Account Statements (12 months)
       Credit Agreements and Term Loans
       Letters of Credit
       Lines of Credit Documentation
       Debt Schedules (principal, interest, maturity)
  2.5  Management Accounts
       Monthly Management Accounts (12–24 months)
       Key Financial Metrics / KPIs

3.0  TAX
  3.1  Returns
       Federal/National Tax Returns (3–5 years)
       State / Provincial Tax Returns (3–5 years)
       Foreign Tax Returns (if applicable)
  3.2  Tax Compliance
       Tax Payment Records and Confirmations
       Sales and Use Tax Returns
       Payroll Tax Records
  3.3  Tax Due Diligence
       Tax Opinions
       Transfer Pricing Documentation and Studies
       Tax Audit Correspondence and Notices
       Net Operating Loss (NOL) Schedules
       Research and Development (R&D) Tax Credit Documentation
  3.4  Tax Structuring
       Section 382 Studies (US NOL limitation) [JURISDICTION-SPECIFIC]
       IRC § 280G Golden Parachute Analysis [JURISDICTION-SPECIFIC]
       VAT / GST Compliance Records [JURISDICTION-SPECIFIC]

4.0  INTELLECTUAL PROPERTY
  4.1  Patents
       Patent Portfolio Summary
       Issued Patent Certificates (all jurisdictions)
       Pending Patent Applications
       Patent Assignment Agreements (all inventors)
       Patent License Agreements (in-bound and out-bound)
       Freedom-to-Operate Opinions [RESTRICT — attorney-client privilege]
  4.2  Trademarks and Branding
       Trademark Registration Certificates (all jurisdictions)
       Trademark Applications (pending)
       Trade Name / Domain Name Registrations
       Brand Licensing Agreements
  4.3  Copyrights and Software
       Copyright Registrations
       Software Development Agreements
       Open Source License Inventory and Compliance Policy
       Software Escrow Agreements
       Source Code Ownership Documentation
  4.4  Trade Secrets and Know-How
       Trade Secret Identification and Protection Policy
       NDA Register (key third-party NDAs)
  4.5  IP Ownership Chain
       Employee IP Assignment and Confidentiality Agreements (all employees)
       Contractor / Consultant IP Assignment Agreements (all)
       Founder IP Assignment Agreements
       Work-Made-for-Hire Agreements

5.0  MATERIAL CONTRACTS
  5.1  Customer Contracts
       Top 25 Customer Agreements (by revenue)
       Standard Customer Terms of Service / MSA
       Customer Concentration Analysis
       Deferred Revenue Schedule
  5.2  Supplier and Vendor Contracts
       Top 20 Supplier/Vendor Agreements (by spend)
       Standard Vendor / Procurement Terms
       Critical Single-Source Supplier Agreements
  5.3  Partnership and Distribution
       Partnership Agreements
       Reseller / Distribution Agreements
       Strategic Alliance Agreements
       Referral Agreements
  5.4  License Agreements (In-bound)
       Technology License Agreements (inbound)
       Data License Agreements
       Content License Agreements
  5.5  License Agreements (Out-bound)
       Technology License Agreements (outbound)
       SaaS / Platform Agreements
       API Agreements
  5.6  Other Material Contracts
       Joint Venture Agreements
       Non-Compete Agreements (third-party)
       Revenue Share Agreements
       Government Contracts and Grants
       Consent-to-Assignment Analysis (for change of control)

6.0  EMPLOYMENT AND HUMAN RESOURCES
  6.1  Executive Employment
       Executive Employment Agreements (C-suite, VP level)
       Executive Offer Letters
       Executive Confidentiality and IP Assignment Agreements
       Executive Non-Compete and Non-Solicitation Agreements
  6.2  Workforce Overview
       Employee Headcount Summary (by department, location)
       Employee Classification Summary (employee vs. contractor)
       Key Employee Retention Risk Assessment
  6.3  Compensation and Benefits
       Equity Incentive Plans (all active plans)
       Outstanding Equity Award Summary (by employee)
       Employee Benefit Plans (health, dental, vision, life insurance)
       401(k) / Pension Plan Documentation [JURISDICTION-SPECIFIC]
       Deferred Compensation Plans
       Bonus and Commission Plans
  6.4  Employment Compliance
       Employment Handbook / Policy Manual
       Equal Employment Opportunity (EEO) Records [JURISDICTION-SPECIFIC]
       WARN Act Compliance Records [JURISDICTION-SPECIFIC]
       OSHA / Workplace Safety Records [JURISDICTION-SPECIFIC]
       I-9 / Right to Work Compliance Summary [JURISDICTION-SPECIFIC]
       Workers' Compensation Records

7.0  LITIGATION AND REGULATORY
  7.1  Litigation
       Pending and Threatened Litigation Summary
       Complaint Files (all pending cases)
       Settlement Agreements (past 5 years)
       Arbitration and Mediation Records
       Legal Hold Notices (active)
  7.2  Regulatory and Compliance
       Regulatory Licenses and Permits (all jurisdictions)
       Regulatory Correspondence (past 3 years)
       Government Investigation Materials
       Consent Orders and Settlement Agreements with Regulators
       Compliance Policies (Anti-Bribery, AML/KYC, Export Control, Data Protection)
       Compliance Audit Reports

8.0  REAL ESTATE AND ASSETS
  8.1  Real Property
       Leases (all office, warehouse, production locations)
       Lease Abstracts
       Subleases
       Real Property Ownership Documents (if owned)
       Title Reports
  8.2  Personal Property and Equipment
       Asset Schedule / Fixed Asset Register
       Equipment Leases and Financing Agreements
       Material Equipment Purchase Agreements
  8.3  Insurance
       Insurance Policies (all lines: GL, D&O, E&O, Workers' Comp, Property, Cyber)
       Insurance Certificates
       Claims History (past 5 years)
       Coverage Gap Analysis

9.0  ENVIRONMENTAL, HEALTH & SAFETY
  9.1  Environmental
       Phase I and Phase II Environmental Assessments
       Environmental Permits
       Environmental Compliance Certifications
       Remediation Plans and Status Reports
       Hazardous Material Inventories
  9.2  Health & Safety
       OSHA / HSE Compliance Records [JURISDICTION-SPECIFIC]
       Workplace Accident / Incident Reports
       Safety Audit Reports

10.0  DATA PRIVACY AND CYBERSECURITY
  10.1  Data Privacy
        Privacy Policy and Terms of Service (current versions)
        Data Processing Agreements (with key processors and customers)
        Data Protection Impact Assessments (DPIAs)
        Personal Data Inventory / Record of Processing Activities (ROPA)
        Cross-Border Transfer Mechanisms (SCCs, adequacy decisions, BCRs)
        Regulatory Correspondence (DPAs, FTC, state AGs)
        Data Breach Incident Log
  10.2  Cybersecurity
        Cybersecurity Policy and Incident Response Plan
        Penetration Testing Reports (past 2 years)
        SOC 2 / ISO 27001 / ISO 27701 Certification Reports
        Cyber Insurance Policy

11.0  CORPORATE DEVELOPMENT AND PRIOR TRANSACTIONS
  11.1  Prior Acquisitions
        Prior Acquisition Agreements (past 5 years)
        Post-Closing Integration Reports
        Earn-Out Status Reports
  11.2  Prior Financing
        Prior Investment Documents (term sheets, financing docs — all rounds)
        SAFE / Convertible Note Documentation
        Series A–[current] Financing Documents
  11.3  Strategic Alternatives
        Board Materials Related to Strategic Alternatives (if any)
        Prior Sale Process Materials (redacted where required)
```

---

### Transaction Type 2: M&A — Asset Purchase

Use the Stock Purchase taxonomy above with these modifications:

**Add to Section 1:**

- Asset Schedule (all assets to be transferred)
- Excluded Assets List
- Assumed Liabilities Schedule
- Retained Liabilities Schedule

**Add to Section 5:**

- Consent-to-Assignment Analysis for each material contract (asset sales require
  counterparty consent to assign; document which require consent and status of requests)
- Bulk Sales Law Compliance Analysis [JURISDICTION-SPECIFIC]

**Modify Section 1.2:** Cap table less critical; replace with a clean Asset title analysis

**Add Section 12:**

```
12.0  ASSET-SPECIFIC DOCUMENTATION
  12.1  Title and Ownership
        Title Reports for Transferred Real Property
        UCC Lien Search Results (for tangible assets)
        Warranty Documentation for Equipment
  12.2  Transition Service Agreements
        Draft Transition Services Agreement (TSA)
        Shared Services Inventory
        IT Systems Separation Plan
        Employee Transfer Plan
```

---

### Transaction Type 3: Debt Financing (Syndicated Loan / Term Loan)

**Priority folders**: Financial capacity, collateral, covenant compliance, existing debt.

```
1.0  BORROWER CORPORATE
  1.1  Entity Documentation (Formation, Good Standing, Authorization)
  1.2  Organizational Chart
  1.3  Board Resolutions Authorizing Financing

2.0  FINANCIAL INFORMATION
  2.1  Audited Financial Statements (3 years)
  2.2  Interim Unaudited Financials (most recent quarter)
  2.3  Financial Projections and Forecasts
  2.4  Management Accounts (12 months)
  2.5  Working Capital Analysis

3.0  EXISTING DEBT STRUCTURE
  3.1  Existing Credit Agreements (all active facilities, all amendments)
  3.2  Existing Note Indentures and Supplements
  3.3  Guaranty Documentation
  3.4  Subordination Agreements
  3.5  Intercreditor Agreements
  3.6  Debt Repayment Schedule

4.0  COLLATERAL
  4.1  Collateral Descriptions and Valuations
  4.2  UCC / PPSA / Charge Search Results [JURISDICTION-SPECIFIC]
  4.3  UCC-1 / Security Filings (current) [JURISDICTION-SPECIFIC]
  4.4  Mortgage / Debenture Documentation
  4.5  Insurance on Collateral Assets
  4.6  Appraisals (real estate, equipment, IP)

5.0  COVENANT COMPLIANCE
  5.1  Historical Covenant Compliance Certificates (2 years)
  5.2  Pro Forma Covenant Compliance Analysis (for new facility)
  5.3  EBITDA Addback / Adjustment Schedule
  5.4  Material Event Certificates (waivers, amendments, defaults)

6.0  MATERIAL CONTRACTS
  6.1  Key Customer Contracts (top revenue sources)
  6.2  Material Supplier Contracts
  6.3  IP Licenses (in-bound and out-bound)

7.0  LITIGATION AND REGULATORY
  7.1  Pending Litigation Summary
  7.2  Material Regulatory Matters

8.0  INSURANCE
  8.1  Business Insurance Policies (GL, Property, Business Interruption)
  8.2  D&O Insurance

9.0  TAX
  9.1  Federal / National Returns (3 years)
  9.2  Tax Audit Correspondence
  9.3  VAT / GST Returns [JURISDICTION-SPECIFIC]

10.0  ENVIRONMENTAL AND COMPLIANCE
  10.1  Environmental Compliance Status
  10.2  Regulatory Licenses and Permits
```

---

### Transaction Type 4: IPO / Capital Markets

**Priority folders**: SEC registration drafts, audited financials, governance, exec comp.

```
1.0  REGISTRATION AND REGULATORY FILINGS
  1.1  Draft Registration Statement (Form S-1 / F-1 or equivalent)
  1.2  Registration Statement Amendments (all filed versions)
  1.3  Prospectus Drafts (preliminary and final)
  1.4  SEC Correspondence and Comment Letters
  1.5  EDGAR Filing Materials

2.0  CORPORATE GOVERNANCE
  2.1  Restated Certificate / Articles of Incorporation (IPO form)
  2.2  Amended and Restated Bylaws (IPO form)
  2.3  Board Committee Charters (Audit, Compensation, Nominating/Governance)
  2.4  Board Composition and Independence Analysis
  2.5  Director Questionnaires
  2.6  Insider Trading Policy (IPO form)
  2.7  Related Party Transactions Policy
  2.8  Compensation Recovery (Clawback) Policy [JURISDICTION-SPECIFIC]

3.0  FINANCIAL STATEMENTS
  3.1  Audited Financial Statements (2–3 years per applicable rules)
  3.2  Interim Reviewed Financial Statements
  3.3  Auditor Comfort Letters (drafts)
  3.4  Internal Controls / SOX 404 Documentation [JURISDICTION-SPECIFIC]
  3.5  Management's Discussion and Analysis (MD&A) Drafts
  3.6  Financial Statement Restatement Records (if any)

4.0  EXECUTIVE COMPENSATION
  4.1  Compensation Discussion and Analysis (CD&A) Drafts
  4.2  Executive Compensation Tables
  4.3  Pay-Versus-Performance Tables [JURISDICTION-SPECIFIC]
  4.4  Equity Award Agreements (IPO form)
  4.5  Director Compensation Schedules
  4.6  Section 280G / Golden Parachute Analysis [JURISDICTION-SPECIFIC]

5.0  CAPITAL STRUCTURE
  5.1  Pre-IPO Capitalization Table (fully diluted)
  5.2  Post-IPO Pro Forma Capitalization
  5.3  Underwriting Agreement (drafts)
  5.4  Lock-Up Agreements (all insiders, major stockholders)
  5.5  Recapitalization / Reclassification Documents

6.0  LEGAL AND REGULATORY
  6.1  Legal Opinions (corporate, disclosure, tax)
  6.2  Regulatory Compliance Summary
  6.3  Material Contracts (key commercial agreements)
  6.4  IP Portfolio Summary
  6.5  Litigation Summary

7.0  ENVIRONMENTAL, SOCIAL AND GOVERNANCE (ESG)
  7.1  Environmental Compliance Status
  7.2  Cybersecurity Risk Disclosure Documentation
  7.3  Climate / Sustainability Disclosures [JURISDICTION-SPECIFIC — evolving]
  7.4  Human Capital Metrics

8.0  UNDERWRITING AND ROADSHOW
  8.1  Roadshow Presentation (drafts)
  8.2  Analyst Presentation Materials
  8.3  Due Diligence Session Transcripts
  8.4  Testing-the-Waters Communications (if applicable)
```

---

### Transaction Type 5: Venture/Growth Equity Financing

```
1.0  LEGAL AND COMPLIANCE
  1.1  Corporate Formation Documents
  1.2  Cap Table (current, fully diluted)
  1.3  Existing Investor Agreements (all rounds)
  1.4  Certificate of Incorporation (current)
  1.5  Board and Stockholder Consents (key actions)
  1.6  SAFE / Convertible Note Documentation (all outstanding)
  1.7  409A Valuation Report (most recent) [JURISDICTION-SPECIFIC]
  1.8  Export Control / CFIUS Analysis (if applicable) [JURISDICTION-SPECIFIC]

2.0  FINANCIAL INFORMATION
  2.1  Audited / Reviewed Financial Statements (if available)
  2.2  Management Accounts (current year)
  2.3  Revenue and ARR/MRR Breakdown
  2.4  Financial Model and Projections

3.0  PORTFOLIO / PRODUCT
  3.1  Product Roadmap
  3.2  Customer Summary and Cohort Analysis
  3.3  NPS / Customer Retention Data

4.0  INTELLECTUAL PROPERTY
  4.1  IP Portfolio Summary
  4.2  Employee IP Assignments (all current and former employees)
  4.3  Open Source Compliance

5.0  TEAM AND EMPLOYMENT
  5.1  Executive Employment Agreements
  5.2  Equity Grant Schedules
  5.3  Key Employee Retention Documentation
  5.4  Reference-Accessible CVs / Biographies (key team)

6.0  PRESENTATION MATERIALS
  6.1  Investor Pitch Deck (current)
  6.2  Investment Thesis Summary
  6.3  Competitive Landscape Analysis

7.0  REGULATORY AND COMPLIANCE
  7.1  Regulatory Licenses (if regulated sector)
  7.2  Material Contracts Summary
  7.3  Privacy / Data Compliance (if applicable)
```

---

## Document Classification System

### Confidentiality Tier Labels

Apply one of four tiers to every folder and document:

| Tier | Label            | Description                                            | Typical Documents                                                                                                       |
| ---- | ---------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| 1    | **Public**       | No restriction; may be shared before NDA               | Publicly filed documents, press releases                                                                                |
| 2    | **Standard**     | NDA required; standard diligence access                | Financial statements, most contracts, corporate docs                                                                    |
| 3    | **Confidential** | Restricted to named individuals                        | Customer lists, pricing, trade secrets, board minutes                                                                   |
| 4    | **Restricted**   | Severely restricted — legal counsel or clean team only | Attorney-client privileged materials, regulatory investigation files, management compensation, employee-identified data |

### Document Status Tags

Apply status tags to every document in the index:

| Tag          | Meaning                                                    |
| ------------ | ---------------------------------------------------------- |
| `Final`      | Executed, signed, and current                              |
| `Draft`      | Not yet executed — note version date                       |
| `Redacted`   | Sensitive information removed; note what was redacted      |
| `Superseded` | Replaced by a later version — retain for historical record |
| `Privileged` | Attorney-client or work-product privilege claimed          |
| `Missing`    | Category placeholder — document not yet uploaded           |

### Workstream Tags

Tag each document by the diligence workstream it supports:

`Corporate` | `Financial` | `Tax` | `IP` | `Contracts` | `Employment` | `Litigation` |
`Regulatory` | `Real Estate` | `Environmental` | `Insurance` | `Privacy` | `Cybersecurity`

---

## Access Permission Framework

### User Group Hierarchy

Design user groups before sending access invitations. Use this 5-tier model:

| Tier | Group Name            | Who                                                             | Default Access                                                  |
| ---- | --------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| 0    | **Admin**             | Data room operator (usually counsel or banker)                  | Full control: upload, delete, permission management, audit logs |
| 1    | **Sell-Side Full**    | Seller's legal counsel, financial advisors, transaction team    | All folders including Restricted; manages the room              |
| 2    | **Advisor Standard**  | Buyer's/investor's advisors (legal, financial, accounting)      | Tiers 1–3 (Standard and Confidential); excludes Restricted      |
| 3    | **Bidder Management** | C-suite executives of the buyer (limited personal data visible) | Tiers 1–2 (Standard); excludes Confidential and Restricted      |
| 4    | **Clean Team**        | Competitor bidders or conflict-of-interest parties              | Curated subfolder only; isolated from other bidder groups       |

### Folder-Level Permission Matrix

| Folder               | Admin | Sell-Side Full | Advisor Standard | Bidder Mgmt | Clean Team |
| -------------------- | ----- | -------------- | ---------------- | ----------- | ---------- |
| 1.0 Corporate        | ✅    | ✅             | ✅               | ✅          | ⬜         |
| 1.2 Cap Table        | ✅    | ✅             | ✅               | ❌          | ⬜         |
| 2.0 Financial        | ✅    | ✅             | ✅               | ✅          | ⬜         |
| 3.0 Tax              | ✅    | ✅             | ✅               | ❌          | ⬜         |
| 4.0 IP               | ✅    | ✅             | ✅               | ✅          | ⬜         |
| 5.0 Contracts        | ✅    | ✅             | ✅               | ✅          | ⬜         |
| 6.0 Employment       | ✅    | ✅             | ✅               | ❌          | ⬜         |
| 6.3 Executive Comp   | ✅    | ✅             | ✅               | ❌          | ⬜         |
| 7.0 Litigation       | ✅    | ✅             | ✅               | ❌          | ⬜         |
| 7.1 Privileged Legal | ✅    | ✅             | ❌               | ❌          | ❌         |
| 10.0 Privacy/Cyber   | ✅    | ✅             | ✅               | ❌          | ⬜         |

Legend: ✅ = Full access, ❌ = No access, ⬜ = Clean team custom folder (separate instance)

### Multi-Bidder Isolation Rules

In competitive multi-bidder M&A auctions:

1. Each bidder group must be fully isolated — no bidder can see another's identity, questions, or VDR access activity.
2. Create separate permission groups per bidder (e.g., Bidder A, Bidder B, Bidder C).
3. Q&A answers given to any bidder must be simultaneously distributed to all bidders (unless competitively sensitive and addressed to one bidder's specific situation).
4. Monitor access analytics by bidder group without cross-bidder visibility.

### Document-Level Restrictions

Apply these controls by document sensitivity:

| Control                      | When to Apply                                                              |
| ---------------------------- | -------------------------------------------------------------------------- |
| **Watermarking**             | All Confidential and Restricted documents (shows viewer name + timestamp)  |
| **Download disabled**        | Restricted folder documents; attorney-client privileged materials          |
| **Print disabled**           | Restricted folder documents                                                |
| **Fence view** (screen-only) | Source code, detailed pricing models, key personnel comp                   |
| **Time-limited access**      | Post-bid deadline; pre-regulatory approval                                 |
| **IP restriction**           | Restrict access to specific IP address ranges (for known-location bidders) |

---

## Gap Analysis Classification

### Document Gap Severity Tiers

Classify each gap finding using this three-tier system:

#### CRITICAL — Must Resolve Before Data Room Launch

The document or category is essential for any bidder to proceed. Its absence signals
preparation failure and will trigger immediate information requests, bid delay, or
withdrawal.

**Triggers:**

- Cap table or capitalization documentation missing
- Audited financial statements absent or more than 18 months old
- Material contracts (top 5 by revenue/risk) absent
- Litigation summary missing (any current pending matter)
- IP ownership chain broken (no inventor assignments or founder IP assignment)
- No organizational chart

**Action**: Escalate to preparation team immediately. Do not launch data room with
CRITICAL gaps unresolved.

#### IMPORTANT — Resolve Before Management Presentations

The document or category is expected by sophisticated diligence teams. Absence signals
organizational risk and will increase Q&A volume and buyer doubt.

**Triggers:**

- Tax returns absent (1–2 years) or only one year available
- Regulatory licenses and permits absent for licensed activities
- Key executive employment agreements absent
- Environmental assessments absent for real-property-owning targets
- Insurance policies absent or certificates only (no full policies)
- Data protection agreements missing for data-heavy businesses
- Board minutes sparse (< 1 year) or absent

**Action**: Target resolution before second-round access or management presentations.

#### STANDARD — Resolve Before Final Diligence

The document or category is part of completeness but less urgent. Absence will be noted
in buyer's legal report but will not typically derail the process at this stage.

**Triggers:**

- Minor contracts (individual contract value < 5% of total revenue)
- Historical documents beyond the standard look-back period
- Insurance certificates already available even if full policies not yet uploaded
- Supplementary compliance records

**Action**: Prioritize as bandwidth allows; resolve before signing and closing conditions.

---

## Actionable Output per Gap Finding

For each gap identified, produce this structured finding card:

```
📁 SECTION: [Section number and name]
🔍 GAP: [Specific document or subcategory missing]
⚠️  SEVERITY: CRITICAL / IMPORTANT / STANDARD
📋 EXPECTED: [Specific list of documents expected in this section]
📄 FOUND: [What was found, if anything; "None" if empty]
🔧 ACTION: [Specific step to take to resolve — name the person/team responsible where possible]
📅 DEADLINE: [By which stage this must be resolved]
📝 NOTE: [Any contextual information — e.g., "May not exist if company is < 3 years old"]
```

Example:

```
📁 SECTION: 3.0 Tax
🔍 GAP: Federal Income Tax Returns — only 2 years available; third year missing
⚠️  SEVERITY: IMPORTANT
📋 EXPECTED: Federal returns for fiscal years 2023, 2024, 2025
📄 FOUND: FY2024 and FY2025 returns uploaded; FY2023 missing
🔧 ACTION: Request FY2023 return from accounting team or tax advisor (Jones Day LLP);
           if under audit, upload audit correspondence and notify buyers
📅 DEADLINE: Before management presentations
📝 NOTE: If FY2023 return was on extension, upload filed extension request
```

---

## Prioritization Framework

When presenting gap findings, organize by priority tier:

### Tier 1 — Showstoppers (Data Room Must Not Open Without These)

- Cap table (fully diluted)
- Audited financial statements (minimum 2 years)
- Material customer contracts (top 25 by revenue)
- IP ownership assignments (all employees and founders)
- Organizational chart and formation documents
- Litigation summary

### Tier 2 — First-Round Essentials (Resolve Before LOI / First-Round Bids)

- Tax returns (3 years)
- Executive employment agreements
- Regulatory licenses and permits
- Insurance policies
- Board minutes (2–3 years)
- Environmental assessments (if target owns real property or operates in regulated sector)
- Data processing agreements (if business processes significant personal data)

### Tier 3 — Final Diligence Completeness (Resolve Before Signing)

- All remaining contracts not in Tier 1
- Ancillary employee documentation
- Supplementary corporate records
- Full insurance claims history
- Background compliance documentation

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                       | Fail Action                                              |
| -------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every regulatory or legal requirement cited references a specific statute, rule, or authoritative guidance | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction                                | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments or updates                                                    | Flag "[CHECK CURRENCY — requirements may have changed]"  |
| **Domain**     | Analysis stays within the transaction's applicable jurisdictions                                           | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty about what documents are required explicitly stated                                            | Add confidence qualifier                                 |

### Self-Interrogation for CRITICAL Gaps

For any gap classified as CRITICAL, apply this 3-pass review before delivering:

**Pass 1 — Necessity Check**: Is this document truly essential, or is there an alternative
that satisfies the same diligence need? Would a sophisticated buyer proceed without it,
or is this genuinely a showstopper?

**Pass 2 — Availability Check**: Is the gap a preparation failure (document exists but
was not uploaded), a documentation gap (document was never created), or a disclosure issue
(document cannot be shared for legal reasons)? The remediation action differs for each.

**Pass 3 — Challenge**: What is the strongest argument that this gap is not CRITICAL for
this specific transaction? Under what circumstances (transaction type, company age,
industry) might a competent advisor accept this gap?

If any pass reveals a misclassification, revise before delivery. Mark audit trail with
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each gap finding and access permission recommendation, assign a confidence level:

| Level        | Range     | Meaning                                            | Action                        |
| ------------ | --------- | -------------------------------------------------- | ----------------------------- |
| **Definite** | 0.95–1.0  | Standard market practice; universally expected     | State with confidence         |
| **High**     | 0.80–0.94 | Strong consensus; minor transaction-type variation | State with brief caveat       |
| **Probable** | 0.60–0.79 | Common but deal-specific variation possible        | State with reasoning          |
| **Possible** | 0.40–0.59 | Depends heavily on transaction specifics           | Flag for advisor confirmation |
| **Unlikely** | 0.0–0.39  | Speculative; apply only with expert confirmation   | Flag "[VERIFY with counsel]"  |

---

## Glass Box Audit Trail

Every data room organization output MUST include this audit section:

```yaml
glass_box:
  skill_name: "legalcode-data-room-organizer"
  transaction_type: "[M&A Stock Purchase / Asset Purchase / Debt Financing / IPO / Venture]"
  user_role: "[Sell-Side / Buy-Side / Financing Party]"
  industry_sector: "[Sector identified from user context]"
  process_stage: "[Pre-launch / First-round / Second-round / Post-LOI / Regulatory / Post-closing]"
  taxonomy_version: "[Transaction Type Folder Taxonomy used]"
  documents_inventoried: "[number, or 'Not provided — taxonomy generated only']"
  gaps_identified:
    critical: "[number]"
    important: "[number]"
    standard: "[number]"
  access_groups_designed: "[number]"
  index_generated: "Yes / No"
  legalcode_mcp: "Connected / Not connected"
  jurisdiction_markers_applied: "[List of [JURISDICTION-SPECIFIC] markers applied]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL gaps)"
  limitations:
    - "[Sector-specific documentation requirements not validated — review with industry counsel]"
    - "[Document availability varies by company age and jurisdictions]"
    - "[Access permission design requires review by VDR platform administrator]"
  reviewer: "AI-assisted — requires qualified transaction counsel and financial advisor review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do when organizing or auditing a data room:

1. **Launching an incomplete data room**: Opening the data room to buyers before CRITICAL
   documents are uploaded signals organizational weakness and raises due diligence red flags
   before diligence begins. Buyers notice what is missing. Never launch with CRITICAL gaps
   unresolved.

2. **Version chaos**: Uploading multiple versions of the same document (v1, v2, final,
   final_final, final_REVISED) without removing superseded versions. Buyers cannot
   determine which version is operative. Maintain one current version per document; archive
   superseded versions in a separate subfolder labeled "Superseded — Do Not Rely."

3. **Unstructured document dump**: Uploading files in their original archive structure
   (e.g., `Accounting/Backup/2023/Q4/FS_final.xlsx`) rather than mapping to the standard
   taxonomy. Buyers waste hours searching. Always map documents to the standard folder
   structure before inviting users.

4. **Over-nesting**: Creating a folder hierarchy more than 4 levels deep. Deep nesting
   makes navigation slow and document discovery unreliable. Documents should be reachable
   in 2–3 clicks from the top-level folder.

5. **Missing the cap table**: The cap table is the single most important document in an
   M&A data room. Uploading it late, in draft form, or with an incorrect date is a CRITICAL
   failure. Upload the most current, board-certified cap table before any buyer access.

6. **Granting top-level admin access to external users**: Buyers or their advisors with
   admin rights can see all access logs, all bidder identities, and all permissions.
   Reserve admin access for the seller's transaction team and counsel only.

7. **No bidder group isolation in competitive auctions**: In multi-bidder processes,
   failing to create separate permission groups per bidder allows one bidder to see
   another's Q&A questions, access patterns, or identity. This is a process-integrity
   failure that can expose the seller to claims of preferential treatment.

8. **Uploading privileged documents without restriction**: Attorney-client privileged
   materials, work-product, and legal opinions must be either excluded from the data room
   or placed in a Restricted folder with download disabled. Unrestricted access can waive
   privilege. Always consult counsel before uploading any privileged document.

9. **Missing IP ownership chain**: A data room without employee and founder IP assignment
   agreements leaves the most valuable M&A asset unverifiable. Buyers will classify IP
   ownership as a CRITICAL risk and price it accordingly (or kill the deal). Every employee
   and contractor who touched the technology must have a signed IP assignment on file.

10. **Uploading unsigned or draft contracts as final**: Buyers discover unsigned "final"
    contracts during diligence and correctly flag them as unexecuted. Upload only fully
    executed agreements in the main folder; clearly label drafts as such in a designated
    Drafts subfolder.

11. **Ignoring consent-to-assignment requirements**: Many customer and vendor contracts
    require counterparty consent to assignment on a change of control. Failing to flag and
    track these in the data room means the M&A team will discover consent requirements at
    closing, not before. Prepare a consent tracker and upload it to the Contracts section.

12. **Failing to redact personal data**: Uploading employee files, customer lists, or HR
    records that contain personal data without considering GDPR / data protection implications.
    The data room must itself comply with applicable data protection law. Minimize personal
    data and apply appropriate access restrictions. [VERIFY with data protection counsel]

13. **No access analytics monitoring**: Modern VDR platforms provide analytics showing which
    bidders access which folders and how frequently. Failing to monitor these analytics means
    losing intelligence on buyer engagement, serious interest, and areas of concern. Monitor
    analytics actively throughout the process.

14. **Publishing Q&A answers to only one bidder**: In a competitive auction, if one bidder
    asks a question that reveals new information about the target, the answer must be
    distributed to all bidders simultaneously to avoid creating an information asymmetry.
    Sellers that fail to do this risk process challenges and, in some jurisdictions, potential
    liability. [VERIFY for regulated public M&A processes]

15. **Treating the data room as final disclosure**: The data room is not a substitute for
    the schedules and disclosure letter to the SPA/APA. Material exceptions to representations
    and warranties must be included in the formal disclosure schedules, not just uploaded to
    the data room. The two processes are complementary, not interchangeable.

16. **Not preparing a VDR index**: Failing to generate a numbered document index forces
    buyers to refer to documents by filename or folder path, making correspondence
    ambiguous and diligence reports hard to cross-reference. Generate a numbered index
    before first-round access and maintain it throughout the process.

17. **Starting data room preparation too late**: Beginning document collection after the LOI
    is signed places the transaction team under time pressure, increases preparation errors,
    and signals disorganization to buyers. Best practice is to begin 2–3 months before
    the process launch. Companies that start late consistently see longer diligence timelines
    and more disruptive buyer Q&A.

18. **Uploading management compensation details to the wrong access tier**: Executive
    compensation plans and individual employee salary data should be in a Restricted subfolder
    accessible only to advisors, not to general bidder management access. Disclosing
    compensation prematurely can create retention risk and disrupt the target's operations.

---

## Writing Standards

Apply plain-language discipline to all outputs:

**For gap findings** (shared with transaction teams):

- Lead with the severity: CRITICAL / IMPORTANT / STANDARD
- One specific action per gap card — not "address this" but "upload the FY2023 Federal
  Income Tax Return to Section 3.1 by [date]"
- Name the responsible party where known
- Short sentences; one point per sentence

**For the VDR index**:

- Consistent formatting: `[Section].[Subsection].[Doc#]  [Document Name]  [Date]  [Status]`
- Dates in YYYY-MM-DD format
- No version numbers in document names — use Status tags instead

**Quality gates before delivery**:

1. Can a senior banker or M&A partner scan the gap report and immediately understand
   what is missing and what action is needed?
2. Is every gap card actionable (specific action, owner, deadline) rather than a vague label?
3. Are access permissions specific (named groups, named folders) rather than generic descriptions?
4. Are all jurisdiction-dependent requirements clearly marked [JURISDICTION-SPECIFIC]?
5. Are all unverified regulatory requirements marked [VERIFY]?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 3, search for jurisdiction-specific document disclosure requirements for the
  transaction type (e.g., HSR filing requirements, SEC registration requirements, GDPR
  data room compliance obligations)
- Search for regulatory filing requirements in the target's operating jurisdictions
- Verify consent-to-assignment requirements under applicable contract law
- Save the most relevant results to `/tmp/legalcode-data-room-research.md`
- Mark all legalcode-mcp-sourced requirements as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all regulatory and legal requirements with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus the output on organizational structure and gap analysis rather than legal
  compliance requirements
- Recommend the user verify specific regulatory disclosure obligations with deal counsel

---

## Localization Notes

VDR content requirements vary significantly by the target's operating jurisdictions:

**United States:**

- Delaware entities: Confirm all director and stockholder consents are in "written consent"
  or meeting-minutes form compliant with DGCL § 141 and § 228 [VERIFY]
- HSR: If transaction exceeds HSR threshold, include FTC/DOJ filing preparation materials
  in a separate Regulatory section
- CFIUS: If buyer is or may be foreign, document CFIUS notification materials [VERIFY]
- SOX: Public company targets require SOX 404 documentation in the Financial section

**European Union and UK:**

- GDPR/UK GDPR: Data room must comply with applicable data protection law. Minimize
  personal data; ensure adequate access restrictions; document the legal basis for
  processing personal data in the VDR context [VERIFY]
- Companies House (UK): Confirm statutory books are current and consistent with filed
  accounts at Companies House
- EU Foreign Subsidies Regulation (FSR): Large transactions may require FSR notification;
  document accordingly [VERIFY — FSR thresholds applicable from 2023]
- FDI screening: Germany, France, Italy, UK all have FDI screening regimes; document
  regulatory pre-clearance materials in the Regulatory section [VERIFY per jurisdiction]

**India:**

- FEMA compliance for cross-border transactions; pricing guidelines documentation
- Competition Commission of India (CCI) filing materials if applicable [VERIFY]
- Stamp duty and registration requirements for certain documents

**Multi-jurisdiction targets:**

- Create jurisdiction-specific subsections within the Regulatory and Employment sections
- Flag documents that require local-language originals alongside English translations
- Note local notarization or apostille requirements for executed documents

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Data Room Organization Report

**Transaction**: [Company Name — Transaction Type]
**User Role**: [Sell-Side / Buy-Side / Financing Party]
**Industry**: [Sector]
**Process Stage**: [Stage]
**Taxonomy Applied**: [Transaction type folder taxonomy version]
**Date**: [date]

---

## 1. VDR FOLDER TAXONOMY

[Numbered folder hierarchy for the transaction type, formatted as:]

1.0 CORPORATE STRUCTURE & GOVERNANCE
1.1 Formation Documents
[Specific documents expected]
1.2 Capitalization
...

[Continue for all sections relevant to transaction type]

---

## 2. DOCUMENT CLASSIFICATION MATRIX

| Folder                     | Confidentiality Tier | Default Access      | Download |
| -------------------------- | -------------------- | ------------------- | -------- |
| 1.0 Corporate              | Standard             | Advisor Standard+   | Enabled  |
| 1.4 Stockholder Agreements | Confidential         | Advisor Standard+   | Enabled  |
| 7.1 Privileged Legal       | Restricted           | Sell-Side Full only | Disabled |

...

---

## 3. GAP ANALYSIS REPORT

**CRITICAL GAPS — Resolve Before Data Room Launch**

[Gap cards using the structured format]

**IMPORTANT GAPS — Resolve Before Management Presentations**

[Gap cards using the structured format]

**STANDARD GAPS — Resolve Before Final Diligence**

[Gap cards using the structured format]

**Summary**:

- Total gaps identified: [N]
- CRITICAL: [N] | IMPORTANT: [N] | STANDARD: [N]
- Estimated preparation effort: [High / Medium / Low]

---

## 4. VDR INDEX

| Doc #   | Document Name                       | Date       | Status | Confidentiality | Notes           |
| ------- | ----------------------------------- | ---------- | ------ | --------------- | --------------- |
| 1.1.001 | Certificate of Incorporation        | 2019-03-15 | Final  | Standard        |                 |
| 1.1.002 | Certificate of Amendment (Series A) | 2021-06-01 | Final  | Standard        |                 |
| 1.2.001 | Cap Table — Fully Diluted           | 2026-03-15 | Final  | Confidential    | Board-certified |

...

---

## 5. ACCESS PERMISSION DESIGN

**User Groups:**

| Group                             | Members       | Folders Accessible                                  | Restrictions             |
| --------------------------------- | ------------- | --------------------------------------------------- | ------------------------ |
| Admin                             | [Names/roles] | All                                                 | None                     |
| Sell-Side Full                    | [Names/roles] | All                                                 | None                     |
| Advisor Standard (Buyer A)        | [Names/roles] | 1–10 (excl. 4.1 Freedom-to-Operate, 7.1 Privileged) | Download disabled for §7 |
| Management Access (Buyer A)       | [Names/roles] | 1–5, excl. cap table detail                         | Download disabled for §6 |
| Clean Team (Buyer B — Competitor) | [Names/roles] | Custom clean room folder                            | Full isolation           |

**Permission Configuration Instructions:**
[Platform-specific permission setup guidance]

---

## 6. Q&A PROCESS RECOMMENDATIONS

**Q&A Routing Matrix:**
| Question Topic | Routes To | Target Response Time |
|----------------|-----------|---------------------|
| Legal / Contracts | Outside Counsel | 3 business days |
| Financial | CFO / Finance Team | 2 business days |
| Tax | Tax Counsel | 3 business days |
| IP | IP Counsel | 3 business days |
| Regulatory | Regulatory Counsel | 5 business days |

**Q&A Policy:**

- All responses distributed simultaneously to all bidder groups in the same round
- Q&A rounds close [X] business days before bid deadlines
- Unilateral questions (answers that reveal non-public information) trigger simultaneous distribution

---

[Glass Box Audit Trail — YAML block]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on:

- Industry VDR best practices research (Datasite, Intralinks, iDeals, FirmRoom, ShareVault documentation)
- M&A advisory guidance from leading investment banks and transaction counsel
- Legalcode repository patterns from `legalcode-ma-due-diligence-checklist` (12-workstream framework)
- Legalcode quality framework from `legalcode-contract-review` (Citation Gates, Self-Interrogation, Glass Box, Anti-patterns)
- SEC IPO registration documentation requirements [VERIFY for current SEC rules]
- Syndicated lending VDR standards (Intralinks DealVault, Debtdomain)
- GDPR/UK GDPR data room compliance principles [VERIFY with data protection counsel]

All legal and regulatory references should be verified against current authoritative sources
before relying on them in any transaction.
