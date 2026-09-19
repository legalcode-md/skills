---
name: legalcode-faq-generator
description: Generates internal legal FAQ documents for corporate legal departments covering contract
  authority matrices (CAM/DAM), NDA self-service programs, vendor onboarding legal flows, employment law
  questions, IP basics, expense policy legal dimensions, and data handling (GDPR/CCPA/privacy). Use when
  building or refreshing a legal self-service portal, creating employee-facing legal guidance, reducing
  legal department ticket volume, enabling self-service deflection, building a legal knowledge base, onboarding
  employees to legal policies, or drafting FAQ content for HR, procurement, finance, product, or engineering
  business units.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Generates internal legal FAQ documents for corporate legal departments covering contract authority matrices (CAM/DAM), NDA self-service programs, vendor onboarding legal flows, employment law questions, IP basics, expense policy legal dimensions, and data handling (GDPR/CCPA/privacy). Use when building or refreshing a legal self-service portal, creating employee-facing legal guidance, reducing legal department ticket volume, enabling self-service deflection, building a legal knowledge base, onboarding employees to legal policies, or drafting FAQ content for HR, procurement, finance, product, or engineering business units. Also triggers on: contract signing authority, who can sign, NDA approval, do I need legal, legal self-service, can I use open source, expense reimbursement legal, data sharing with vendors, employee data GDPR, working time rules, overtime classification, hiring contractor vs employee. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers; supports US federal, US state, EU/GDPR, UK, and multi-jurisdictional FAQ sets.


# Legalcode FAQ Generator

> **Disclaimer**: This skill produces AI-assisted draft FAQ content for internal legal
> self-service programs. It does not constitute legal advice. All FAQ content generated
> by this skill must be reviewed and approved by a qualified legal professional licensed
> in the relevant jurisdiction(s) before publication. Laws change frequently — verify
> current applicability before relying on any provision described here. Statutory and
> regulatory references cited from memory carry hallucination risk; verify against
> authoritative sources before publishing. This skill is a drafting and structuring tool,
> not a substitute for legal counsel.

---

## Purpose and Scope

This skill generates production-ready draft internal legal FAQ documents for corporate
legal departments. It creates structured, employee-facing guidance across seven high-volume
topic domains that together account for the majority of routine legal questions in most
organizations.

**Covers:**

- Contract authority matrices (CAM/DAM) — who can sign, at what thresholds
- NDA self-service programs — qualification gates, tiered templates, pre-approved redlines
- Vendor onboarding legal workflows — due diligence tiers, DPA triggers, insurance minimums
- Employment law FAQs — FLSA, FMLA, ADA, Title VII, leave management (US); Working Time
  Directive, works council consultation (EU/UK); plus jurisdiction flags for other markets
- IP basics — trade secrets, invention assignment, open source policy, copyright ownership
- Expense policy legal dimensions — accountable plan rules, state reimbursement mandates,
  gifts/entertainment FCPA/anti-bribery limits
- Data handling — GDPR, CCPA/CPRA, employee data, vendor data sharing, breach notification

**Produces:**

- Audience-segmented FAQ modules (by business function: HR, Procurement, Engineering, All)
- Decision trees and routing logic for escalation gating
- Jurisdiction-tagged content with explicit scope statements
- Review metadata (last-reviewed placeholder, DRI field, change triggers)
- Self-service deflection quality assessment per module
- Content maintenance calendar recommendations

**Does not:**

- Provide legal advice or replace qualified counsel
- Produce jurisdiction-specific statutory analysis (use legalcode-mcp for that)
- Generate contract templates (see legalcode-nda-triage, legalcode-contract-review)
- Replace an organization's legal review and approval process
- Apply universally — all output requires attorney review before employee publication

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. Employment law, data protection, tax treatment of
expenses, and IP ownership rules all vary significantly by jurisdiction. The skill produces
a base layer of globally applicable guidance, then layers on jurisdiction-specific content
with explicit tagging.

**Jurisdiction markers used throughout this skill:**

- `[US-FEDERAL]` — Applies to US federal law (FLSA, FMLA, ADA, FCPA, DTSA)
- `[US-STATE: CA/NY/etc.]` — Applies to specific US state(s)
- `[EU-GDPR]` — Applies under the EU General Data Protection Regulation
- `[UK]` — Applies under UK GDPR / Employment Rights Act / Working Time Regulations
- `[JURISDICTION-SPECIFIC]` — Varies; research and replace with jurisdiction-applicable content
- `[VERIFY]` — Legal reference requires independent verification before publication
- `[ATTORNEY-REVIEW]` — This answer carries higher risk; mandatory qualified review before publishing

**Supported jurisdiction combinations (out of the box):**

- US federal baseline + state supplements (CA, NY, WA flagged throughout)
- EU GDPR overlay on data topics
- UK Working Time Regulations on employment topics
- Multi-jurisdictional flag ("If you are based outside the US, contact legal")

**For other jurisdictions:** Research local employment, data, and IP law using legalcode-mcp
and replace [JURISDICTION-SPECIFIC] markers before publishing.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
one-size-fits-all FAQ scope, the workflow pauses and asks when:

- The organization's jurisdiction mix would materially change the content
- Company size triggers different regulatory thresholds (ADA: 15+ employees; FMLA: 50+)
- Audience segmentation choices affect which modules to prioritize
- The organization already has templates or policies to reference in the FAQ output

Use the **⟁ CLARIFY** pattern wherever marked below. If context has already been provided,
skip the question and proceed.

---

## Workflow

### Step 1: Accept the Request

Accept input in any of these formats:

- **Topic request**: "Generate a legal FAQ for vendor onboarding" or "Draft an NDA self-service guide"
- **Module list**: Explicit list of FAQ topics to cover
- **Business unit brief**: "Create legal FAQ for our procurement team" or "Build a legal FAQ for employee onboarding"
- **Full program brief**: Company size, jurisdictions, business units, existing templates, target audience

If the request is a full program, proceed to Step 2. If the request targets a specific
module, jump directly to that module in Step 5 and skip irrelevant context gathering.

### Step 2: Gather Organizational Context

**⟁ CLARIFY** — Ask the user these questions (skip any already answered by the input):

1. **Company size and structure**
   - Options: Under 50 employees, 50–250 employees, 251–1,000 employees, 1,001–5,000 employees, 5,000+ employees, Global enterprise
   - _Why this matters_: FMLA applies at 50+ employees. FMLA/ADA thresholds affect which employment FAQs are relevant. CAM tier structures differ by size.

2. **Primary jurisdictions** (select all that apply)
   - Options: United States — Federal only, United States — specific states (list), European Union (specify countries), United Kingdom, Canada, Australia, Other (specify), Multi-jurisdictional / Global
   - _Why this matters_: Employment law, data protection, and expense reimbursement rules are fundamentally jurisdiction-specific. A US-only FAQ is dangerous for a company with EU employees.

3. **Target audience(s)** (select all that apply)
   - Options: All employees (general), HR / People Operations, Procurement / Finance, Engineering / Product, Sales / Business Development, Executive / Leadership, Legal team only
   - _Why this matters_: HR has a different top-question profile than Procurement. Audience segmentation makes self-service more effective.

4. **Topics to cover** (select all or prioritize)
   - Options: Contract Authority Matrix (CAM/DAM), NDA Self-Service, Vendor Onboarding, Employment Law, IP Basics, Expense Policy, Data Handling/Privacy, All topics
   - _Why this matters_: Full programs require full delivery. Single-topic requests can be handled faster and deeper.

5. **Existing resources** (optional)
   - "Do you have existing NDAs, contract templates, or policies I should reference?"
   - Free text or file input. Reference these in the FAQ output rather than creating conflicts.

6. **Publication format**
   - Options: Confluence/wiki pages, SharePoint, Google Sites, Notion, Standalone markdown, Other
   - _Why this matters_: Affects formatting choices (collapsible sections, header levels, table styles).

**Defaults if not provided:**

- Size: Assume 250–1,000 employees (mid-market)
- Jurisdiction: US Federal baseline + GDPR overlay + UK flag
- Audience: All employees (with function-specific notes)
- Topics: All seven modules
- Format: Markdown (compatible with all platforms)

### Step 3: Assess Legal Landscape and Cite Authority

Before generating content, identify the relevant legal framework for the requested topics.
Use **legalcode-mcp** if connected to verify current statutory requirements.

**For each active topic module, identify:**

- The primary governing statute(s) and their current thresholds
- Any recent changes (rule changes, effective dates) that affect FAQ content
- Jurisdiction-specific variations that require flagging
- Known enforcement trends that affect advice risk level

**Key legal authority reference by module:**

| Module                  | Primary Authority (US)                  | Primary Authority (EU/UK)           |
| ----------------------- | --------------------------------------- | ----------------------------------- |
| Employment — Overtime   | FLSA 29 U.S.C. §§ 201–219               | WTD 2003/88/EC; UK WTR 1998         |
| Employment — Leave      | FMLA 29 U.S.C. §§ 2601–2654             | Parental Leave Directive 2019/1158  |
| Employment — Disability | ADA 42 U.S.C. §§ 12101–12213            | EU Framework Directive 2000/78/EC   |
| Data Protection         | CCPA Cal. Civ. Code §§ 1798.100 et seq. | GDPR Regulation (EU) 2016/679       |
| Trade Secrets           | DTSA 18 U.S.C. §§ 1831–1839             | EU Trade Secrets Directive 2016/943 |
| Expense — Tax           | IRC § 62(a)(2)(A); IRC § 132(d)         | Varies by member state              |
| Anti-Bribery (Expenses) | FCPA 15 U.S.C. §§ 78dd-1 et seq.        | UK Bribery Act 2010                 |
| NDA / Contracts         | State contract law; UTSA                | Civil code frameworks by country    |

**If legalcode-mcp is not connected:**

- Proceed with knowledge-based drafting
- Mark all specific statutory thresholds with `[VERIFY — confirm current threshold]`
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`

### Step 4: Plan the FAQ Program Structure

Before writing individual modules, present the user with a structural plan:

**⟁ CLARIFY** — For full-program requests, confirm the program structure:

1. **Segmentation model**: Single FAQ per topic (one page per topic, audience notes inline) vs. Separate pages per business function (HR page, Procurement page, etc.)
   - Recommend: Start with topic-based pages (easier to maintain), add audience shortcuts later

2. **Escalation model**: How should employees contact legal when self-service doesn't cover their situation?
   - Options: Email address, intake form, CLM self-service, Slack channel, Other
   - _Why this matters_: Every FAQ answer must end with an escalation path

3. **Template library**: Does the organization want links to templates (e.g., standard NDA, vendor agreement) embedded in the FAQ, or FAQ-only?
   - _Why this matters_: Embeds with templates are higher-value but require template to already exist

4. **Maintenance model**: How will the FAQ be kept current?
   - Options: Quarterly legal review cycle, Annual review, Event-triggered (law changes), Combination
   - Recommend: Quarterly for employment/data topics; annual for structural topics like CAM

### Step 5: Generate FAQ Modules

For each active topic module, generate content following the **FAQ Module Structure** defined
in the Topic Analysis Reference section. Apply jurisdiction-appropriate content, escalation
logic, and maintenance metadata.

**⟁ CLARIFY** — For each module, confirm depth:

- **Standard**: 8–12 Q&As covering the most common questions
- **Deep**: 12–20 Q&As including edge cases and sub-topic nuance
- **Executive summary only**: 3–5 key rules, decision tree, escalation contact

Default: Standard depth unless user requests otherwise.

Generate modules in this order (highest deflection value first):

1. Contract Authority Matrix (Module A)
2. NDA Self-Service (Module B)
3. Vendor Onboarding (Module C)
4. Data Handling (Module D)
5. Employment Law — Exempt/Non-Exempt & Leave (Module E)
6. IP Basics (Module F)
7. Expense Policy (Module G)

### Step 6: Apply Quality Classification

Assess each generated FAQ entry against the three-tier quality classification:

- **READY-TO-PUBLISH**: Factually accurate, jurisdiction-appropriate, clear escalation path, no high-risk content
- **NEEDS-REVIEW**: Contains jurisdiction-specific claims, specific statutory thresholds, or advice on high-risk topics; mandatory attorney review before publishing
- **INCOMPLETE**: Requires organizational input (e.g., "Insert your standard NDA template link here") or additional research

For each **NEEDS-REVIEW** item, run the Self-Interrogation before delivery.

### Step 7: Deflection Quality Assessment

For each module, assess the expected deflection impact:

| Module            | Typical Deflection Rate | Key Dependency                      | Expected Annual Time Saved         |
| ----------------- | ----------------------- | ----------------------------------- | ---------------------------------- |
| CAM/DAM           | HIGH (70-85%)           | CAM must be pre-configured by org   | 2–5 hrs/week for 100-employee orgs |
| NDA Self-Service  | HIGH (60-80%)           | Standard NDA template must exist    | 3–8 hrs/week                       |
| Vendor Onboarding | MEDIUM-HIGH (50-70%)    | Tiered template library helpful     | 2–4 hrs/week                       |
| Data Handling     | MEDIUM (40-60%)         | Complex questions still need legal  | 1–3 hrs/week                       |
| Employment Law    | MEDIUM (35-55%)         | High-risk questions require legal   | 2–5 hrs/week                       |
| IP Basics         | MEDIUM (40-65%)         | Side project/OSS questions escalate | 1–3 hrs/week                       |
| Expense Policy    | HIGH (65-80%)           | Clear policy must exist             | 1–2 hrs/week                       |

Present the deflection assessment alongside each module so the user can prioritize
publication sequence and set realistic expectations.

### Step 8: Generate Maintenance Calendar

For each module, specify:

- **Review frequency**: How often this module should be reviewed
- **Review triggers**: Specific events that require an immediate re-review
- **DRI field**: Placeholder for the Directly Responsible Individual
- **Last reviewed date**: Placeholder (`[Date]`) for publication date tracking

### Step 9: Quality Verification

Before delivering the FAQ program:

1. Run the 5 Citation Quality Gates silently
2. For every NEEDS-REVIEW item, run the 3-pass Self-Interrogation
3. Confirm every answer has a clear escalation path
4. Verify no answer gives legal advice without qualification
5. Check that all jurisdiction-specific claims are correctly tagged
6. Generate the Glass Box Audit Trail

### Step 10: Deliver and Structure Output

Deliver the FAQ program using the **Output Format Template** defined below. Structure for
direct publication to the target platform.

**⟁ CLARIFY** — Before final delivery, confirm:

- "Should I include a program launch checklist (steps to publish, communicate, and track adoption)?"
- "Should I include a gap analysis of what this FAQ program does NOT cover?"

---

## Topic Analysis Reference

### Module A: Contract Authority Matrix (CAM/DAM)

**Purpose**: Define who has authority to sign and approve contracts, at what thresholds, and
under what conditions. Eliminates ambiguity, prevents unauthorized commitments, and enables
faster deal execution by routing routine approvals without legal involvement.

**Standard Q&A Set (adapt to organizational structure):**

---

**Q: Who can sign a contract on behalf of the company?**

Contracts bind the company only when signed by someone with actual authority. Authority is
granted through the Contract Authority Matrix (CAM), not by seniority or job title alone.

The CAM defines approval authority by:

- Contract type (vendor, customer, NDA, employment, real estate, settlement, IP license)
- Contract value or annual commitment
- Whether the contract uses the company's standard template or non-standard terms

_Classification: NEEDS-REVIEW — [attorney to confirm CAM tiers before publishing]_

---

**Q: What if I need to sign something urgently and cannot reach the right approver?**

Contact your manager and the Legal team immediately. Do not sign without authorization —
an unauthorized signature can still bind the company under apparent authority principles,
even if you lacked actual authority. [ATTORNEY-REVIEW]

Urgency does not create authority. If the approver is unreachable, escalate to their
manager. Legal can advise on an emergency approval path for time-sensitive matters.

---

**Q: Does a purchase order (PO) count as a contract?**

Yes. A purchase order is a binding contract once accepted by the vendor (usually by
performing the services or delivering goods). PO authority follows the same thresholds
as the CAM. Never issue a PO above your authorization threshold without the required approvals.

---

**Q: I'm not sure if I need a contract. When do I need one?**

Use a contract whenever:

- The company is paying or receiving payment for goods or services
- You are disclosing or receiving confidential information (NDA required)
- A vendor will have access to company systems, data, or facilities
- You are engaging a consultant, contractor, or staffing agency
- You are granting or receiving a license to intellectual property

If you are unsure, contact legal before proceeding. The cost of reviewing a question is
far lower than the cost of an unprotected or unauthorized arrangement.

---

**Q: What is the CAM approval threshold for my contract?**

[Insert organization's current CAM table here. Example structure below — replace with your organization's actual tiers.]

| Contract Value | Contract Type                                              | Required Approvals                        |
| -------------- | ---------------------------------------------------------- | ----------------------------------------- |
| Under $[X]     | Standard vendor, company template                          | Department Director                       |
| $[X]–$[Y]      | Standard vendor, company template                          | VP + Finance                              |
| Above $[Y]     | Any contract                                               | C-suite + Legal review                    |
| Any value      | Non-standard terms, settlement, IP assignment, real estate | Legal review required regardless of value |
| Any value      | Government contracts                                       | Legal + Compliance required               |

_[PLACEHOLDER — Legal team to insert your organization's actual CAM before publishing]_

---

**Q: When does Legal need to review a contract?**

Legal review is required when:

- The contract value exceeds the Legal Review Threshold in the CAM
- The contract uses the counterparty's paper (non-standard terms)
- The contract involves IP assignment, settlement, government, or real estate
- The contract includes non-standard indemnification or unusual liability provisions
- The counterparty is in a high-risk jurisdiction [VERIFY applicable list with Compliance]
- You are uncertain whether the template applies

When in doubt, ask Legal. An email asking "does this need legal review?" takes minutes.

---

**CAM Escalation Gate:**

> Use the CAM self-service path if: (a) the contract value falls within your authorization tier, (b) you are using the company's approved standard template, and (c) no red flags apply.
>
> Contact legal if: (a) the value exceeds your tier, (b) the counterparty insists on their paper, (c) any of the mandatory escalation triggers apply, or (d) you are unsure.

_Escalation contact: [Legal team email / intake form URL]_
_Last reviewed: [Date] | Reviewed by: [Employment/Commercial Counsel] | Review frequency: Annual_

---

### Module B: NDA Self-Service Program

**Purpose**: Enable business stakeholders to execute routine NDAs without attorney review,
while preserving legal oversight for higher-risk situations. Typically the highest-ROI
self-service initiative — NDAs represent 20–40% of legal requests at many companies.

**Qualification Decision Tree:**

To determine whether your NDA can proceed on the self-service path, answer these questions:

```
1. Is the counterparty a domestic entity (same country as company HQ)?
   → No: ESCALATE to Legal (international NDA template or review required)
   → Yes: Continue

2. Is this related to an acquisition, joint venture, or strategic partnership?
   → Yes: ESCALATE to Legal
   → No: Continue

3. Will we be receiving the counterparty's source code, proprietary technology, or
   formula-level trade secrets?
   → Yes: ESCALATE to Legal
   → No: Continue

4. Is the proposed term longer than 3 years?
   → Yes: ESCALATE to Legal
   → No: Continue

5. Does the counterparty want to use their own NDA paper?
   → Yes: ESCALATE to Legal
   → No: Continue

6. Is the counterparty a direct competitor?
   → Yes: ESCALATE to Legal
   → No: Self-service path — proceed with Standard NDA Template
```

**Standard Q&A Set:**

---

**Q: When do I need an NDA?**

You need an NDA (also called a Confidentiality Agreement, or CA) before:

- Sharing confidential business information with a third party (pricing, strategy, roadmap, customer data)
- Receiving confidential information from a third party under an obligation of secrecy
- Beginning discussions with a vendor, partner, or potential hire about sensitive matters
- Any situation where either party needs to share something not yet public

You do not need an NDA for:

- Publicly available information only
- Routine vendor interactions where no confidential information changes hands

When in doubt, execute an NDA. It is easier and faster than remedying a disclosure.

---

**Q: Do I need a mutual or one-way NDA?**

- **Mutual NDA**: Both parties will share confidential information with each other. Use for partnerships, joint ventures, vendor negotiations, due diligence.
- **One-way (unilateral) NDA**: Only one party shares. Use when we are receiving a vendor pitch, evaluating a candidate's prior work, or sharing our product roadmap without expecting confidential information in return.

The standard company template covers both. Select the correct variant in the template.

---

**Q: Does the NDA need to be notarized or witnessed?**

No, for standard commercial NDAs in [applicable jurisdiction]. A signed NDA is effective
upon execution by both parties; no notarization or witnesses are required. [JURISDICTION-SPECIFIC:
Some jurisdictions require formalities for certain contract types — verify if operating outside
primary jurisdiction.]

---

**Q: Who can sign the NDA?**

Follow the CAM. For standard NDAs using the company template, typically a Director-level or
VP-level employee is authorized to sign. Check the CAM for your organization's specific
authority level.

---

**Q: The counterparty sent us their own NDA. Can I just sign it?**

No. Always try to use your company's standard NDA first. If the counterparty insists on
their paper, route to Legal for review. Counterparty NDAs often favor the drafter and may
include unfavorable provisions (broad scope of confidential information, asymmetric obligations,
unusual governing law, IP grant-backs).

---

**Q: How long should the NDA last?**

Standard mutual NDAs typically have:

- Agreement term: 1–3 years (auto-expires or renews)
- Confidentiality obligation term: 3–5 years after disclosure (or indefinitely for trade secrets)

The company standard template uses [insert your organization's standard term]. Do not agree
to terms shorter than [X years] without legal review. [PLACEHOLDER — Legal team to specify]

---

**Q: Can the counterparty request redlines to our standard NDA?**

Certain pre-approved redlines can be accepted without Legal review. Examples of typically
pre-approved changes:

- Changing governing law from [company default state] to another US state
- Reducing the term from 3 years to 2 years
- Adding standard Residuals carve-out

Redlines outside the pre-approved list require Legal review. If unsure, forward to Legal.

_[PLACEHOLDER — Legal team to define and publish the pre-approved redline list before activating self-service]_

---

**NDA Self-Service Escalation Gate:**

> Proceed without Legal if: (a) you passed all 6 qualification questions, (b) you are using the company's standard NDA template, (c) any requested redlines are on the pre-approved list.
>
> Contact Legal if: any qualification question triggers escalation, counterparty is on their own paper, or redlines fall outside the pre-approved list.

_Standard NDA Template: [Insert template link]_
_Escalation contact: [Legal team email / intake form]_
_Last reviewed: [Date] | Reviewed by: [Commercial Counsel] | Review frequency: Annual or upon change to template_

---

### Module C: Vendor Onboarding Legal FAQ

**Purpose**: Help procurement and finance teams understand when legal review is required
for new vendors, what documents must be in place, and what the standard requirements are.

**Vendor Legal Due Diligence Tiers:**

| Tier                 | Description                                              | Annual Spend | Data Access               | Legal Review                      |
| -------------------- | -------------------------------------------------------- | ------------ | ------------------------- | --------------------------------- |
| Tier 1 — Standard    | Commodity goods/services, PO terms, no data              | Under $[X]   | None                      | Not required                      |
| Tier 2 — Enhanced    | Moderate value, professional services, system access     | $[X]–$[Y]    | Non-sensitive             | Standard template; Finance review |
| Tier 3 — Full Review | High value, personal data processing, non-standard terms | Above $[Y]   | Customer or employee data | Legal review required             |
| Tier 4 — Compliance  | High-risk jurisdiction, regulated industry, sensitive IP | Any          | Any                       | Legal + Compliance required       |

_[PLACEHOLDER — Legal team to set dollar thresholds before publishing]_

---

**Q: Do I need an NDA before talking to a new vendor?**

Yes, if you will be sharing company confidential information (e.g., requirements documents,
technical specifications, pricing information, business strategy) during the evaluation.
Use the NDA self-service path for standard vendor NDAs. See Module B.

You do not need an NDA if the conversation involves only publicly available information or
general capability discussions.

---

**Q: Can I use the vendor's standard contract?**

Generally no — always try to use the company's standard vendor agreement first. The company
template is balanced and protects the organization's interests in IP, data, liability, and
termination. Vendor-drafted contracts typically favor the vendor.

If the vendor insists on their paper, route to Legal. This is a Tier 3 situation regardless
of spend amount.

---

**Q: Does this vendor need a Data Processing Agreement (DPA)?**

A DPA is required whenever a vendor processes personal data on behalf of the company.
"Processing" includes storing, accessing, analyzing, transmitting, or deleting personal data
belonging to employees, customers, or other individuals.

Common examples that require a DPA:

- Cloud storage vendor that holds employee HR files
- Marketing platform with customer contact data
- Payroll processor
- Background check vendor
- Analytics tool with access to user behavioral data
- Customer support platform with access to customer data

[EU-GDPR] The DPA is a legal requirement under GDPR Art. 28. It must be in place **before**
any personal data is transferred to the vendor. Failure to have a DPA is an enforcement risk.

[US-FEDERAL] While a formal DPA is not universally mandated by federal law, a data processing
contract is required under CCPA for California-regulated businesses and is best practice
universally. [VERIFY current CCPA/CPRA contractual requirements]

---

**Q: What insurance does the vendor need to carry?**

Standard insurance requirements for vendors depend on the engagement type:

[PLACEHOLDER — Legal/Risk to insert organization's standard minimums. Common baselines:]

- General Liability: $1M per occurrence / $2M aggregate (minimum for most vendors)
- Professional Liability / E&O: $1M per claim (for professional services, software, consulting)
- Cyber Liability: $1M minimum (for any vendor with access to company data or systems)
- Workers' Compensation: Per statutory requirements
- Umbrella/Excess: $5M+ for high-risk engagements

Request a Certificate of Insurance (COI) from the vendor before work begins on any Tier 3+ engagement.

---

**Q: Who can approve a vendor for use?**

Vendor approvals follow the CAM. For vendors at or below the Tier 1/2 threshold using
company standard terms, a Director-level approval is typically sufficient. For Tier 3+ vendors,
legal and potentially compliance sign-off is required in addition to business approval.

---

**Q: Do we need to run sanctions and export control checks on vendors?**

[US-FEDERAL] OFAC (Office of Foreign Assets Control) sanctions apply to transactions with
certain individuals, entities, and jurisdictions. You should verify that any vendor is not
on the OFAC SDN (Specially Designated Nationals) list. [VERIFY your organization's OFAC
screening process with Compliance]

[JURISDICTION-SPECIFIC] Export control regulations (EAR, ITAR in the US; UK Export Control
Order; EU Dual-Use Regulation) may apply to vendors receiving technical data or software
with potential dual-use applications. [ATTORNEY-REVIEW — route to Legal/Compliance if unsure]

---

**Vendor Onboarding Escalation Gate:**

> Self-service path: Tier 1 vendor, standard PO terms, no data access, spend under threshold.
>
> Contact Legal if: Tier 3+ vendor, any personal data processing, non-standard terms, high-risk jurisdiction, regulated industry, IP assignment or licensing, unusual liability structures.

_Vendor Onboarding Intake Form: [Insert URL]_
_DPA Template: [Insert link if available]_
_Escalation contact: [Legal / Procurement Counsel email]_
_Last reviewed: [Date] | Reviewed by: [Commercial / Privacy Counsel] | Review frequency: Annual_

---

### Module D: Data Handling FAQ

**Purpose**: Help employees across all functions understand their data protection obligations,
particularly around GDPR, CCPA, and internal data governance. High self-service value because
many questions have clear rule-based answers.

---

**Q: What is "personal data" / "personal information"?**

Personal data (GDPR terminology) or personal information (CCPA terminology) is any information
that identifies or can reasonably identify a living individual. This includes:

- Names, email addresses, phone numbers, physical addresses
- Employee IDs, job titles, salary, performance ratings
- Health information, biometric data, location data
- IP addresses, device identifiers, cookie data
- Photos and video footage where individuals are identifiable

[EU-GDPR] The EU definition is broad — even a combination of data points that together
identify someone constitutes personal data, even if each piece alone would not.

[JURISDICTION-SPECIFIC] Definitions vary by jurisdiction. When in doubt, treat data as
personal data and apply the highest applicable standard of protection.

---

**Q: Can we share employee data with our parent company / US headquarters?**

[EU-GDPR / UK] Transferring personal data outside the EEA (or UK) requires a transfer
mechanism. Common options:

- **Standard Contractual Clauses (SCCs)**: EU-approved contract terms for data transfers.
  Most US-to-EU and EU-to-US transfers rely on these. [VERIFY that your SCCs are the
  current 2021 EU version]
- **Adequacy decision**: EU Commission has recognized certain countries as providing
  adequate protection (check current list — it changes) [VERIFY current adequacy decisions]
- **Binding Corporate Rules (BCRs)**: For intra-group transfers; requires DPA approval;
  high setup cost but provides long-term flexibility

Contact Legal before establishing any new cross-border data transfer arrangement. [ATTORNEY-REVIEW]

[US-FEDERAL / US-STATE] No single US federal law restricts domestic data transfers. State
laws (CCPA/CPRA in California) impose restrictions on "sharing" with affiliates for
cross-context behavioral advertising. [VERIFY current CCPA/CPRA restrictions]

---

**Q: When do we need to notify individuals of a data breach?**

[EU-GDPR] A personal data breach that is likely to result in a risk to individuals' rights
must be reported to the relevant supervisory authority within **72 hours** of becoming aware.
Breaches with **high risk** to individuals require direct individual notification without
undue delay. Notify the Data Protection Officer (DPO) or Legal immediately upon suspecting
a breach. [VERIFY current DPA breach notification procedures]

[US-FEDERAL/STATE] Breach notification requirements vary by state. Most states require
notification to affected individuals and in some cases state regulators, within timeframes
ranging from 30 to 90 days. California requires notification "in the most expedient time
possible." [VERIFY state-specific requirements for each jurisdiction where you operate]

**Any suspected data breach must be reported to Legal / the DPO within 24 hours of discovery.
Do not investigate or remediate without Legal involvement.**

---

**Q: Can we use employee data for AI model training?**

[EU-GDPR] Using personal data for AI training purposes likely requires a separate legal
basis from the original processing purpose (purpose limitation principle). Consent is the
most commonly used basis, but it must be freely given — which is problematic in an
employment context where consent may not be truly voluntary. [ATTORNEY-REVIEW]

[US-FEDERAL] No single US federal law prohibits this, but state laws and employment
contracts may limit it. Collective bargaining agreements may restrict it further.
[ATTORNEY-REVIEW — consult Legal before using any employee data for AI training]

---

**Q: Can we monitor employee email, Slack, or computer activity?**

[JURISDICTION-SPECIFIC] Employee monitoring laws vary significantly. In general:

- [US-FEDERAL] US employers have broader monitoring rights than EU/UK employers. Employees
  should have no expectation of privacy on company systems, but policy must disclose this.
- [EU] Employee monitoring requires a legitimate interest justification, proportionality
  assessment, and typically consultation with the works council. Individual consent is
  not a valid basis in most employment contexts. [VERIFY country-specific requirements]
- [UK] Data Protection Act 2018 / UK GDPR applies. Employment Practices Code (ICO)
  guidance requires transparency and proportionality. [VERIFY current ICO guidance]

Before implementing any monitoring program, contact Legal and, where required, HR. [ATTORNEY-REVIEW]

---

**Q: How long do we keep employee records?**

Retention periods vary by record type and jurisdiction. General guidance:

| Record Type             | US Retention (Federal minimum)               | EU Retention                 |
| ----------------------- | -------------------------------------------- | ---------------------------- |
| Payroll / tax records   | 4 years (IRS); some states require more      | 10 years (varies by country) |
| Personnel files         | 3 years post-termination (EEOC)              | Varies; 3–7 years typical    |
| I-9 forms               | 3 years from hire or 1 year post-termination | N/A                          |
| Workers' comp records   | Per state law                                | Varies                       |
| Litigation-hold records | Until litigation concludes + standard period | Until litigation concludes   |

[ATTORNEY-REVIEW — retention schedules require Legal approval before implementation;
failure to retain mandatory records or premature deletion of litigation-hold records
carries significant legal risk]

---

**Q: Can we share customer data with a third-party analytics vendor?**

Only if you have appropriate contractual protections in place:

- A Data Processing Agreement (DPA) or Service Provider Agreement must be signed before sharing
- The vendor must agree to process data only for the specified purpose (purpose limitation)
- The data shared must be limited to what is necessary (data minimization)
- The vendor must implement appropriate security measures
- [EU-GDPR] Ensure cross-border transfer mechanisms are in place if the vendor is outside the EEA

Contact the Privacy team or Legal before engaging any new analytics vendor with customer data. [ATTORNEY-REVIEW]

---

**Data Handling Escalation Gate:**

> Handle yourself: General data hygiene questions, understanding what personal data is, identifying whether your activity involves personal data.
>
> Contact Legal/DPO: Any breach or suspected breach (within 24 hours), new vendor access to personal data, cross-border data transfers, monitoring programs, AI training on personal data, any data subject access request received.

_Data breach reporting: [DPO or Legal emergency contact]_
_Privacy intake form: [URL]_
_Escalation contact: [Privacy Counsel / DPO email]_
_Last reviewed: [Date] | Reviewed by: [Privacy Counsel / DPO] | Review frequency: Quarterly_

---

### Module E: Employment Law FAQ

**Purpose**: Answer the most frequent employment law questions from HR, managers, and
employees. High-volume but also high-risk — these answers require careful jurisdiction
flagging and mandatory attorney review on sensitive topics.

**Audience**: Primarily HR / People Operations, Managers; secondary: All employees

---

#### E1: Exempt vs. Non-Exempt / Overtime

**Q: What is the difference between an exempt and non-exempt employee?**

[US-FEDERAL — FLSA] Under the Fair Labor Standards Act (FLSA):

- **Non-exempt employees** are entitled to overtime pay (1.5x regular rate) for all hours
  worked over 40 in a workweek.
- **Exempt employees** are excluded from FLSA overtime requirements if they meet both the
  salary test (currently a minimum salary threshold [VERIFY current DOL threshold, adjusted
  periodically]) AND one of the duties tests (Executive, Administrative, Professional,
  Computer Professional, Outside Sales, or Highly Compensated).

Common misclassification pitfall: Job title alone does not determine exempt status. An
employee titled "Manager" who lacks genuine supervisory duties and decision-making authority
may be non-exempt. [ATTORNEY-REVIEW — misclassification is a top source of FLSA liability]

[EU / UK] The "exempt vs. non-exempt" framework does not apply. Instead, the EU Working
Time Directive (2003/88/EC) and UK Working Time Regulations 1998 set maximum working hours
for most workers. See "Working Time" Q&A below. [JURISDICTION-SPECIFIC]

---

**Q: How many hours per week can employees work?**

[US-FEDERAL] No federal law caps hours for adult employees in most industries. Non-exempt
employees can work unlimited hours but must receive overtime pay for hours over 40/week.
[VERIFY applicable state restrictions — some states have industry-specific caps]

[EU — Working Time Directive] The EU Working Time Directive limits average working time to
**48 hours per week** (averaged over a 17-week reference period), including overtime. Employees
may opt out of the 48-hour limit in some member states (including, post-Brexit, the UK) but
the opt-out must be voluntary and in writing. [VERIFY country-specific implementation]

[UK — Working Time Regulations 1998] Same 48-hour average limit as EU, with individual
opt-out available. Mandatory minimum: 11 consecutive hours daily rest; 24 hours weekly rest;
rest break after 6 hours; 5.6 weeks paid annual leave (28 days for full-time). [VERIFY
current UK WTR provisions for any post-Brexit amendments]

---

**Q: What records do we need to keep for non-exempt employees?**

[US-FEDERAL — FLSA] Employers must retain payroll records including: hours worked each day
and week, regular and overtime pay rates, total daily and weekly straight-time pay, total
overtime pay, total wages, applicable pay period dates. Retention period: 3 years for payroll
records; 2 years for records used to compute wages. [VERIFY]

---

#### E2: Family and Medical Leave

**Q: Who qualifies for FMLA leave?**

[US-FEDERAL — FMLA] To be eligible for FMLA leave, an employee must:

- Work for an employer with **50 or more employees** within 75 miles of the worksite
- Have worked for the employer for at least **12 months**
- Have worked at least **1,250 hours** in the 12-month period immediately before the leave

Qualifying reasons: Serious health condition of the employee or immediate family member;
birth, adoption, or foster placement of a child; qualifying military exigency; care for a
covered servicemember (26 weeks).

[JURISDICTION-SPECIFIC] Many US states have more generous leave laws. Some cover smaller
employers; some provide paid leave; some expand the definition of qualifying family members.
[VERIFY applicable state leave laws for all states where you have employees]

[EU / UK] EU Parental Leave Directive 2019/1158 provides at least 4 months' parental leave,
with at least 2 months non-transferable. UK provides up to 52 weeks' maternity leave and
18 weeks' (unpaid) parental leave per child. [VERIFY current entitlements for each
country where you have employees]

---

**Q: Can we require employees to use PTO concurrently with FMLA leave?**

[US-FEDERAL — FMLA] Yes. Employers may (and many do) require employees to use any accrued
paid leave concurrently with unpaid FMLA leave. The employer must notify employees of this
requirement in the FMLA designation notice. [VERIFY current DOL regulations]

---

**Q: What happens if an employee cannot return from FMLA leave?**

[US-FEDERAL — FMLA] Generally, the employee must be restored to the same or an equivalent
position upon return from FMLA leave. If the employee is unable to return at the end of
FMLA, the employer has limited options but must still consider whether an ADA accommodation
(e.g., extended unpaid leave) is required. [ATTORNEY-REVIEW — FMLA/ADA intersection is
high-litigation-risk; consult Employment Counsel before making any adverse employment decision
for an employee on or recently returned from leave]

---

#### E3: Reasonable Accommodation (ADA / Disability)

**Q: When does the company have to provide a reasonable accommodation?**

[US-FEDERAL — ADA] The Americans with Disabilities Act (applies to employers with **15 or
more employees**) requires reasonable accommodation for a qualified individual with a
disability unless doing so would cause undue hardship.

A "disability" is a physical or mental impairment that substantially limits a major life
activity. Common examples: mobility impairments, chronic health conditions, mental health
conditions, sensory impairments.

A "reasonable accommodation" might include: modified work schedule, remote work, ergonomic
equipment, reassignment to a vacant position, leave of absence, modified duties.

The employer must engage in an **interactive process** — good-faith dialogue with the employee
to identify an effective accommodation. Refusing to engage is itself a violation. [ATTORNEY-REVIEW]

[EU] The EU Framework Directive 2000/78/EC and national implementing legislation require
reasonable accommodation for disabled workers. Definitions and obligations vary by member
state. [JURISDICTION-SPECIFIC — consult local employment counsel]

---

**Q: What is the "interactive process" and when must we start it?**

[US-FEDERAL — ADA] The interactive process is a good-faith dialogue between employer and
employee (or applicant) to identify and implement an effective reasonable accommodation. It
should start promptly — as soon as the employee requests an accommodation or the employer
reasonably believes one may be needed, even without a formal request.

Required steps: (1) Identify the functional limitation. (2) Determine what accommodation
the employee is requesting. (3) Consider alternatives. (4) Implement or explain why undue
hardship applies.

**Do not deny accommodation requests without HR and Legal review. Refusal to engage in the
interactive process is one of the most common ADA violations.** [ATTORNEY-REVIEW]

---

#### E4: Worker Classification (Employee vs. Contractor)

**Q: What is the risk of misclassifying a contractor as an employee (or vice versa)?**

[US-FEDERAL] Worker misclassification is a major source of legal liability. Consequences:

- Back taxes and penalties (employer portion of FICA, failure-to-withhold penalties)
- Retroactive benefit obligations (health insurance, 401(k), paid leave, workers' comp)
- Wage and hour claims (unpaid overtime if the worker was non-exempt)
- State agency audits (most states have aggressive misclassification enforcement)

[US-STATE: CA] California's ABC test (Labor Code § 2750.3 / Dynamex) is the most restrictive:
a worker is presumed an employee unless the hiring entity can prove all three prongs: (A) free
from control and direction, (B) performs work outside the usual course of the hiring entity's
business, and (C) has an independently established business. [VERIFY current CA law status
— subject to ballot initiative changes]

**All new contractor engagements should be reviewed by HR and Legal before proceeding.** [ATTORNEY-REVIEW]

---

**Employment Law Escalation Gate:**

> Handle through FAQ: General understanding of leave entitlements, overtime rules, accommodation obligations, classification criteria.
>
> Contact HR immediately: Any individual accommodation request, leave request, performance/termination decision for employee on leave, contractor classification decision.
>
> Contact Legal: Adverse employment action for employee on or recently returned from leave; denial of accommodation; investigation of harassment or discrimination; any situation involving litigation risk.

_HR intake: [HR contact or HRIS self-service link]_
_Employment Counsel: [Legal team email]_
_Last reviewed: [Date] | Reviewed by: [Employment Counsel] | Review frequency: Quarterly_

---

### Module F: IP Basics FAQ

**Purpose**: Help employees understand what intellectual property belongs to the company,
what they can use, and when to involve Legal. Particularly critical for engineers (open source),
salespeople (customer-provided materials), and employees considering side projects.

---

**Q: Who owns the work I create as an employee?**

[US-FEDERAL] Generally, work created within the scope of employment belongs to the employer.
Under the **work-made-for-hire** doctrine (17 U.S.C. § 101) [VERIFY current provision],
works created by employees within the scope of their employment are owned by the employer.

Your **Proprietary Information and Invention Assignment (PIIA)** agreement (signed at hire)
formalizes this — it typically assigns to the company all inventions, developments, and
works created: (a) using company time, resources, or equipment; (b) relating to the company's
current or reasonably anticipated business; or (c) resulting from work performed for the
company.

[US-STATE: CA] California Labor Code § 2870 [VERIFY current provision] requires employers
to exclude from assignment inventions made entirely on employee's own time, using no company
resources, that neither relate to the company's business nor result from company work. Other
states have similar carve-outs. [VERIFY applicable state law]

[EU] "Work made for hire" as a US doctrine does not exist in most EU jurisdictions. The
employer typically owns works created by employees within their duties, but the mechanism
differs by country (employment contract, statutory provision). Moral rights may not be
waivable. [JURISDICTION-SPECIFIC]

---

**Q: I built something on the weekends. Does the company own it?**

It depends. Apply these questions:

1. Did you use any company equipment, systems, or software? → If yes, likely company IP
2. Did you use any company confidential information (code, data, customer info, strategy)? → If yes, likely company IP
3. Does the project relate to the company's current or reasonably anticipated business? → If yes, potentially company IP

If none of the above apply and you are not in California (or equivalent jurisdiction with
statutory carve-outs), the company may still have a contractual claim if your PIIA is
broadly worded.

**Best practice: Disclose to Legal/HR before the side project goes further.** If it
qualifies as employee-owned, Legal can issue a written confirmation. If it doesn't, better
to know now. [ATTORNEY-REVIEW]

---

**Q: Can I use open source software in our product?**

It depends on the open source license:

| License Type     | Examples                        | Use in Product                  | Distribution Obligation                                                |
| ---------------- | ------------------------------- | ------------------------------- | ---------------------------------------------------------------------- |
| Permissive       | MIT, Apache 2.0, BSD 2/3-clause | Generally yes, with attribution | Attribution required; no source disclosure                             |
| Weak Copyleft    | LGPL v2.1, MPL 2.0              | Generally yes with care         | Modified LGPL/MPL files may need disclosure                            |
| Strong Copyleft  | GPL v2/v3                       | Requires legal review           | Distribution of GPL-linked software may require source code disclosure |
| Network Copyleft | AGPL v3                         | Requires legal review           | Serving software over a network triggers disclosure obligation         |
| Proprietary      | Commercial software             | Confirm license terms           | N/A                                                                    |

[ATTORNEY-REVIEW] GPL and AGPL are particularly significant risks for SaaS and distributed
software. Consult Legal before incorporating any copyleft-licensed library into production code.

**Check the company's approved open source license list before adding any new dependency.**
If the license isn't on the approved list, open a Legal request before using it.

---

**Q: What is a trade secret and how do I protect it?**

[US-FEDERAL — DTSA] A trade secret is any business information (formula, method, code,
customer list, pricing, algorithm, strategy) that: (a) derives independent economic value
from not being generally known; and (b) is subject to reasonable measures to maintain its
secrecy. The Defend Trade Secrets Act (18 U.S.C. § 1836 et seq.) [VERIFY] provides federal
civil and criminal protection.

**Reasonable measures the company takes (and you must follow):**

- Mark confidential documents as "CONFIDENTIAL" or "PROPRIETARY"
- Use NDAs before sharing with external parties
- Restrict access to sensitive systems on a need-to-know basis
- Do not send confidential information to personal email accounts
- Do not use cloud storage outside approved company tools

**What you must do when leaving the company:**

- Return all company information and equipment
- Delete any company data from personal devices
- Do not take customer lists, source code, pricing, or strategy documents
- Former employer trade secrets cannot be used in new employment — even if memorized

---

**Q: Can I contribute to an open source project using company resources or code?**

Personal open source contributions on personal time, using no company resources: Generally
allowed, but check your PIIA and any open source contribution policy.

Contributions using company code, during working hours, or to a project related to company
business: Require prior written approval from Legal. Contributing company code to an open
source project could inadvertently disclose trade secrets or trigger copyleft license obligations.

**Consult Legal before any contribution of company-related code to open source.** [ATTORNEY-REVIEW]

---

**IP Escalation Gate:**

> Handle through FAQ: General understanding of IP ownership rules, open source license categories, trade secret concepts.
>
> Contact Legal: Side projects with any connection to company business or resources; any open source use outside the approved list; open source contributions using company code; potential trade secret misuse (yours or a third party's); IP ownership disputes.

_Open source approved license list: [Insert link if available]_
_IP/Legal intake: [Legal team email / intake form]_
_Last reviewed: [Date] | Reviewed by: [IP Counsel] | Review frequency: Annual_

---

### Module G: Expense Policy FAQ

**Purpose**: Answer common questions about expense reimbursement, gifts/entertainment,
and the legal dimensions of travel and expense policy. Typically high deflection value
because most answers are rule-based.

---

**Q: What expenses can I claim for reimbursement?**

The company reimburses necessary and reasonable business expenses incurred while performing
your job duties. General categories:

- Business travel (airfare, hotel, ground transportation)
- Business meals (with client, prospect, or internal team — must document business purpose)
- Client entertainment (within policy limits)
- Home office expenses (where applicable — see jurisdiction note below)
- Professional development (conferences, courses — with manager approval)

All expenses must have: (a) a clear business purpose, (b) adequate documentation (receipt),
and (c) manager approval. The company's expense policy is the definitive guide — this FAQ
covers the legal dimensions only.

[US-FEDERAL — IRS Accountable Plan] For reimbursements to be tax-free to you and deductible
to the company, they must meet IRS accountable plan requirements: business connection,
adequate accounting, and return of excess amounts. Reimbursements that fail these criteria
are treated as taxable wages. [VERIFY]

---

**Q: Are meal expenses 100% deductible?**

[US-FEDERAL] No. Business meals are **50% deductible** for the company (reduced from 100%
under the Tax Cuts and Jobs Act of 2017). [VERIFY current deductibility rules — subject
to legislative change] The temporary 100% deduction for restaurant meals (2021-2022) has
expired.

Employee meals while traveling overnight remain 50% deductible. Meals that are de minimis
fringe benefits (e.g., occasional company-wide catered lunches) may qualify for full deduction.

This affects the company's books, not your reimbursement — you are still reimbursed 100%
of allowable meal expenses subject to the policy per diem.

---

**Q: Do I get reimbursed for using my personal phone for work?**

[US-STATE: CA] Yes. California Labor Code § 2802 requires employers to reimburse employees
for all necessary expenditures, including a reasonable percentage of personal phone costs
when the phone is required for work. [VERIFY current interpretation]

[US-FEDERAL / Other States] No federal requirement. State law varies. [VERIFY your applicable
state law] Company policy governs in the absence of a statutory requirement.

[EU] Some EU member states require reimbursement for work-related use of personal devices.
[JURISDICTION-SPECIFIC — consult local employment counsel or HR]

---

**Q: What are the rules for giving gifts to clients or government officials?**

**Private-sector clients:** The company's expense policy sets the per-person limit for
gifts and entertainment. Typical range: $[X] per person per occasion for gifts; higher
limits for entertainment with prior approval. [PLACEHOLDER — Legal/Finance to insert limits]

**Government officials (US):**
[US-FEDERAL — FCPA] The Foreign Corrupt Practices Act prohibits giving anything of value
to a foreign government official to obtain or retain business. "Reasonable and bona fide"
business entertainment is a limited exception but must be modest, transparent, and properly
documented. [VERIFY current DOJ/SEC FCPA guidance]

US federal employees are subject to strict gift rules — generally $20 per gift, $50 per
year from any single source. [VERIFY]

State and local government employees have varying rules. Contact Legal before providing
anything of value to a government employee. [ATTORNEY-REVIEW]

**UK / Global:** [UK — Bribery Act 2010] The UK Bribery Act is stricter than the FCPA —
it covers private-sector bribery as well, and does not have a facilitation payment
exception. Maximum penalty: 10 years' imprisonment and unlimited fine. [ATTORNEY-REVIEW]

**When in doubt about gifts or entertainment for government officials: do not proceed without
Legal clearance.** [ATTORNEY-REVIEW]

---

**Q: I lost a receipt. Can I still claim the expense?**

[US-FEDERAL — IRS] For expenses under $75, the IRS does not require receipts if you have
other adequate records documenting the business purpose, amount, time, and place. For
expenses $75 and above, receipts are required. [VERIFY current IRS threshold — subject to
adjustment]

The company expense policy may be stricter than IRS minimums. Submit a lost receipt
explanation via your expense platform and obtain manager sign-off. For high-value expenses,
contact Finance.

---

**Q: Can my spouse/family accompany me on a business trip?**

Travel costs for personal guests accompanying you on a business trip are your personal
expense — the company does not reimburse non-business travel.

If your guest participates in business activities (e.g., attends a client dinner with a
clear business purpose), that portion may be reimbursable. Contact Finance for guidance on
mixed-purpose trips. [ATTORNEY-REVIEW for any significant amounts]

[US-FEDERAL — IRS] Travel costs for a spouse/companion who has no bona fide business role
are not deductible. [VERIFY]

---

**Expense Policy Escalation Gate:**

> Handle through FAQ: General reimbursability questions, standard meals/travel/home office, lost receipt process.
>
> Contact Finance: Questions about specific expense categories, policy exceptions, large or unusual expenses.
>
> Contact Legal: Any gift or entertainment for government officials; expenses in high-risk jurisdictions; potential FCPA / Bribery Act questions; large entertainment expenses above policy limits.

_Expense policy: [Link to company expense policy]_
_Finance contact: [Finance team email]_
_Legal/Compliance: [Legal team email]_
_Last reviewed: [Date] | Reviewed by: [Employment/Compliance Counsel + Finance] | Review frequency: Annual_

---

## Quality Assurance Framework

### PDCA Quality Cycle for FAQ Generation

**PLAN**: Identify topic module, target audience, and jurisdiction. Classify each Q&A as
READY-TO-PUBLISH, NEEDS-REVIEW, or INCOMPLETE. Identify which answers carry litigation risk.

**DO**: Generate Q&A content with jurisdiction flags, escalation paths, and maintenance
metadata. Apply Self-Interrogation to all NEEDS-REVIEW items.

**CHECK**: Run Citation Quality Gates. Verify escalation gates are clear. Confirm no
answer gives unqualified legal advice. Verify all [JURISDICTION-SPECIFIC] markers are
placed correctly.

**ACT**: Flag INCOMPLETE items for organizational input. Note change triggers for
maintenance calendar. Update deflection assessment based on content depth achieved.

---

### Citation Quality Gates

Run these 5 gates silently before delivering any FAQ module. If any gate fails, revise.

| Gate           | Rule                                                                                                    | Fail Action                                                 |
| -------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Source**     | Every statutory threshold or legal claim cites a specific statute or regulation                         | Add citation or mark `[VERIFY — confirm current threshold]` |
| **Format**     | All citations follow a consistent format for the jurisdiction (e.g., FLSA § 207, GDPR Art. 28)          | Fix format                                                  |
| **Currency**   | Every cited provision checked for recent amendments (thresholds change; new regulations enacted)        | Flag `[VERIFY — may have been amended]`                     |
| **Domain**     | FAQ content stays within the jurisdiction tagged. No US concepts bleeding into EU answers or vice versa | Remove or re-tag with correct jurisdiction                  |
| **Confidence** | Uncertainty is explicitly stated, not hidden. High-risk answers are flagged [ATTORNEY-REVIEW]           | Add confidence qualifier or ATTORNEY-REVIEW tag             |

---

### Self-Interrogation for NEEDS-REVIEW Items

For any FAQ answer classified as NEEDS-REVIEW, apply this 3-pass review before delivery:

**Pass 1 — Legal Chain Integrity:**

- Does the answer follow logically from the cited statute or regulation?
- Would a qualified employment/privacy/IP attorney in this jurisdiction confirm this answer?
- Is there a significant counterargument or exception the answer omits?

**Pass 2 — Completeness:**

- Are all relevant statutory authorities reflected?
- Are there notable state/local supplements to the federal rule that employees need to know?
- Are there enforcement trends or recent regulatory guidance that affect the answer?

**Pass 3 — Challenge:**

- What is the most likely way this answer harms an employee who relies on it?
- What scenario would make this answer wrong or misleading?
- Should this question be removed from self-service and routed to Legal instead?

If any pass reveals weakness, revise the answer or reclassify as [ATTORNEY-REVIEW] before delivery.

---

### Confidence Scoring

For each FAQ module, assign an overall confidence level:

| Level        | Range     | Meaning                                               | Action                                                                  |
| ------------ | --------- | ----------------------------------------------------- | ----------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled rule, clear statute, no significant variation | Publish with standard disclaimer                                        |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions      | Publish with specific caveat; attorney review recommended               |
| **Probable** | 0.60–0.79 | Good guidance but jurisdictionally sensitive          | Flag for attorney review before publishing; add [JURISDICTION-SPECIFIC] |
| **Possible** | 0.40–0.59 | Genuinely uncertain, competing authorities            | Do not publish as FAQ; route to Legal intake instead                    |
| **Unlikely** | 0.0–0.39  | Weak basis, highly variable, or speculative           | Do not publish; remove from FAQ scope                                   |

Apply this scoring per answer where stakes are high. Lower-risk answers (definitional,
procedural) can be published at High confidence. Higher-risk answers (adverse employment
action, data transfer, trade secret protection) require Probable or higher.

---

## Glass Box Audit Trail

Every FAQ program delivery MUST include this audit section:

```yaml
glass_box:
  skill_name: "legalcode-faq-generator"
  mode: "Created from scratch"
  topic: "Internal Legal FAQ — Self-Service Program"
  jurisdiction: "Jurisdiction-agnostic with US-federal, EU-GDPR, and UK markers"
  source_skills_analyzed: 0
  enhancement_type: "Create"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "[path or 'Not created']"
  modules_generated: "[list of modules generated]"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  needs_review_count: "[number of NEEDS-REVIEW answers]"
  incomplete_count: "[number of INCOMPLETE placeholders]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  attorney_review_required: "Yes — all NEEDS-REVIEW items must be cleared by qualified counsel before publication"
  limitations:
    - "All content is a starting draft — requires attorney review before employee publication"
    - "Thresholds and statutory references must be verified against current law"
    - "Jurisdiction-specific content requires research and replacement of [JURISDICTION-SPECIFIC] markers"
    - "CAM tiers, insurance minimums, and dollar thresholds are placeholders requiring organizational input"
    - "[INCOMPLETE] items require organizational input to finalize"
  reviewer: "AI-assisted — requires qualified legal review before publication"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do when generating or publishing internal legal FAQs:

1. **Publishing without attorney review** — AI-generated FAQ content contains hallucination
   risk and cannot reflect organization-specific policies, recent law changes, or nuanced
   legal judgment. Never publish to employees without a qualified attorney reviewing and
   approving each answer.

2. **Disclaimers that destroy utility** — Adding "this is not legal advice, consult counsel,
   your situation may differ" to every single answer renders the FAQ useless. Use targeted
   disclaimers only where the legal risk genuinely requires it. The point of a self-service
   FAQ is to answer routine questions definitively.

3. **Stale content syndrome** — A FAQ published and never updated becomes a liability.
   Employment law thresholds (FLSA salary threshold, FMLA coverage) change by regulation.
   GDPR enforcement evolves. State laws have staggered effective dates. Every answer must
   have a review frequency and DRI attached.

4. **No escalation guidance** — Every FAQ answer must tell the employee when NOT to use
   the self-service path. A FAQ without escalation triggers creates both under-escalation
   (employees handling legal matters they shouldn't) and over-escalation (employees
   contacting Legal for everything). Escalation gates are as important as the answers.

5. **Jurisdiction-agnostic answers for jurisdiction-specific law** — Stating "the law
   requires X" without specifying which jurisdiction's law creates dangerous over-reliance.
   Employment law in Germany, California, and New York differs dramatically from US federal
   baseline. Always tag jurisdiction and flag where it varies.

6. **US-centric FAQ for global companies** — Treating US law as the universal standard
   harms employees in EU, UK, APAC, and LatAm offices. Add [EU-GDPR], [UK], and
   [JURISDICTION-SPECIFIC] flags liberally. When in doubt, add: "If you are based outside
   [primary jurisdiction], contact Legal — local law may differ."

7. **Using placeholders as final content** — Template gaps like "[Insert CAM tiers here]"
   or "[Insert NDA template link]" must be filled before publication. Publishing a FAQ
   with visible placeholders destroys credibility and creates legal risk if employees
   interpret blank fields incorrectly.

8. **Wrong scope for self-service** — Not all legal questions are FAQ-appropriate. Questions
   involving an active performance/termination situation, an ongoing investigation, a
   specific individual's accommodation request, or a potential lawsuit must be routed to
   Legal, not answered by FAQ. The FAQ should identify these categories explicitly and
   exclude them from self-service scope.

9. **Ignoring enforcement trends** — Legal FAQs based only on statutory text miss the
   practical picture. FLSA enforcement of employee-vs-contractor misclassification has
   intensified in certain sectors. GDPR enforcement is more aggressive in some EU member
   states. FAQ advice that is technically legal but practically risky should be flagged.

10. **Building portal before content strategy** — Investing in a self-service portal platform
    before having high-quality FAQ content results in an empty, low-trust system. Build
    content quality first; scale platform second.

11. **No attribution or authority signal** — FAQs without "Prepared by [Legal team]" and
    "Last reviewed: [date]" are distrusted by employees. Attribution signals authority and
    currency. Anonymous undated FAQs are treated as unofficial and frequently ignored.

12. **Conflating FAQ content with legal opinions** — A FAQ answer saying "you are not
    required to sign a non-compete" is very different from a legal opinion advising a
    specific employee on a specific non-compete. FAQ answers describe general rules; they
    cannot and do not constitute advice about a specific legal situation.

13. **No feedback loop** — A FAQ program with no mechanism to learn what questions aren't
    answered, what answers employees found unhelpful, or what search terms returned no
    results cannot improve. Minimally: "Was this helpful? Yes/No" per article; monthly
    review of unanswered searches.

14. **Treating every question as self-service appropriate** — Some questions appear simple
    but are actually high-variance (e.g., "Can I use this open source library?" depends
    entirely on which library). These should trigger a decision tool or routing question,
    not a static FAQ answer. Resist the pressure to put everything in the FAQ.

15. **Forgetting litigation hold** — FAQ programs focused on routine questions often neglect
    to include: "When do I need to preserve documents for potential litigation?" Employees
    who delete emails or files after a preservation obligation has attached face personal
    liability. This topic should be in every FAQ program under "Data Handling" or as a
    standalone module.

16. **Skipping the CAM as foundation** — The contract authority matrix is the single highest-
    leverage FAQ item for reducing legal team workload. Organizations that build FAQ programs
    without first establishing a clear CAM will see disproportionate legal inbox volume on
    contract approval questions. Always build CAM content first.

---

## Writing Standards

Apply these plain-language standards to all FAQ content:

**For FAQ answers:**

- Lead with the rule, not the exception: State the general rule first, then flag the exceptions
- One concept per answer: If an answer covers three sub-topics, split it into three Q&As
- Active voice: "The employer must pay overtime" not "Overtime must be paid by the employer"
- Define jargon: Use plain language; define legal terms when first used ("exempt" → "employees not entitled to overtime")
- Short sentences: Maximum 25 words per sentence for legal rules
- Use tables and lists: Threshold tables, tier matrices, and bulleted requirements are more
  readable than prose paragraphs for rule-based content
- Be specific: "72 hours" not "promptly"; "$1,250 hours" not "substantial hours"
- Avoid false confidence: Where the law is unsettled or varies, say so

**Jurisdiction flags:**

- Always tag jurisdiction before jurisdiction-specific content: `[US-FEDERAL — FLSA]` before the overtime rule
- Never assume the reader's jurisdiction
- When genuinely global (e.g., basic trade secret concepts), state explicitly: "This guidance applies broadly; specific rules vary by jurisdiction"

**Quality gates before delivery:**

1. Can an HR manager understand and apply this answer without legal training?
2. Does every answer include an escalation trigger?
3. Is every specific threshold or statutory reference either verified or marked [VERIFY]?
4. Are there any phrases that could be misread as legal advice rather than general guidance?
5. Is every [PLACEHOLDER] item clearly identified so the publishing attorney knows what to fill in?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 3, search for current statutory thresholds (FLSA salary threshold, FMLA coverage requirements, GDPR fines)
- Verify currency of cited statutes before including in FAQ content
- Search for recent enforcement actions or regulatory guidance changes that affect FAQ accuracy
- Search for jurisdiction-specific employment and data protection requirements for any jurisdiction the user requests
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with knowledge-based drafting
- Mark all specific thresholds with `[VERIFY — confirm current threshold]`
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Advise the user to have their attorney verify all statutory thresholds against current authoritative sources (DOL website, EEOC.gov, EUR-Lex, ICO, etc.) before publishing
- Focus the FAQ generation on structural quality, escalation design, and content organization rather than legal authority depth

**Graceful degradation**: The skill is fully functional without legalcode-mcp. The loss is
primarily legal authority verification. The structural content, workflow guidance, escalation
logic, and quality frameworks all remain valuable and deliverable without the tool.

---

## Localization Notes

For organizations with employees in non-English speaking jurisdictions:

1. **Translation**: Legal FAQ content should be translated to the local language by or in
   coordination with local counsel. Do not rely on machine translation for legal content.

2. **Local counsel review**: Employment law, data protection, and expense tax rules are
   fundamentally national law. Use local employment or privacy counsel to review and
   supplement jurisdiction-specific modules.

3. **Works council consultation**: `[EU]` In Germany, France, the Netherlands, and other
   EU jurisdictions with co-determination, major changes to employment policies (including
   the creation of monitoring programs or significant data collection) may require works
   council consultation before implementation. Consult local counsel before publishing
   FAQ content on monitoring or data handling that could affect works council rights.
   [ATTORNEY-REVIEW]

4. **Language requirements**: Some jurisdictions require employment contracts, privacy
   notices, and certain policies to be provided in the local language. Check whether
   the FAQ itself requires translation by law. [JURISDICTION-SPECIFIC]

5. **Multi-jurisdiction display**: For global companies, best practice is to display
   jurisdiction tags prominently and consider a jurisdiction selector ("I am based in:
   US / EU / UK / Other") that surfaces the most relevant content.

---

## Output Format Template

Structure the final FAQ program delivery as follows:

```markdown
# [Organization Name] Legal FAQ — Internal Self-Service Guide

> **Important**: This FAQ provides general legal information for employees. It is not legal
> advice and does not address every possible situation. For your specific circumstances,
> contact the Legal team at [legal@company.com / intake form link].
>
> Last reviewed: [Date] | Legal team

---

## Quick Navigation

- [A. Contract Authority Matrix (Who Can Sign)](#A)
- [B. NDA Self-Service Program](#B)
- [C. Vendor Onboarding Legal Guide](#C)
- [D. Data Handling and Privacy](#D)
- [E. Employment Law Basics](#E)
- [F. Intellectual Property Basics](#F)
- [G. Expense Policy — Legal Dimensions](#G)
- [When to Contact Legal](#escalation)

---

## A. Contract Authority Matrix {#A}

**Audience:** All employees who sign, approve, or negotiate contracts
**Jurisdiction:** [Applicable jurisdictions]
**Reviewed by:** [Commercial/Contracts Counsel] | [Date]

[Generated CAM content — see Module A above]

---

## B. NDA Self-Service {#B}

**Audience:** All employees (primary: Sales, BD, Procurement, HR)
**Jurisdiction:** [Applicable jurisdictions]
**Reviewed by:** [Commercial Counsel] | [Date]

[Generated NDA self-service content — see Module B above]

---

## C. Vendor Onboarding Legal Guide {#C}

**Audience:** Procurement, Finance, Engineering (for software vendors)
**Jurisdiction:** [Applicable jurisdictions]
**Reviewed by:** [Commercial/Privacy Counsel] | [Date]

[Generated vendor onboarding content — see Module C above]

---

## D. Data Handling and Privacy {#D}

**Audience:** All employees; primary: Engineering, Marketing, HR, Operations
**Jurisdiction:** EU GDPR, UK GDPR, CCPA/CPRA, [other applicable]
**Reviewed by:** [Privacy Counsel / DPO] | [Date]

[Generated data handling content — see Module D above]

---

## E. Employment Law Basics {#E}

**Audience:** HR/People Operations, Managers; All employees
**Jurisdiction:** [Applicable US states + EU/UK flags]
**Reviewed by:** [Employment Counsel] | [Date]

[Generated employment law content — see Module E above]

---

## F. Intellectual Property Basics {#F}

**Audience:** Engineering, Product, Design, Research; All employees
**Jurisdiction:** US federal (DTSA, FLSA IP provisions), [EU/UK flags as applicable]
**Reviewed by:** [IP Counsel] | [Date]

[Generated IP basics content — see Module F above]

---

## G. Expense Policy — Legal Dimensions {#G}

**Audience:** All employees who submit expenses; Finance/Accounting
**Jurisdiction:** US federal (IRS rules), [state supplements], [UK/EU as applicable]
**Reviewed by:** [Employment/Compliance Counsel + Finance] | [Date]

[Generated expense policy content — see Module G above]

---

## When to Contact Legal {#escalation}

Contact the Legal team for situations that fall outside this FAQ's self-service scope:

| Situation                                                     | Contact                                                 |
| ------------------------------------------------------------- | ------------------------------------------------------- |
| Contracts above authorization threshold or non-standard terms | [legal@company.com / intake form]                       |
| Any NDA with a non-domestic party or non-standard terms       | [legal@company.com]                                     |
| Vendor with access to personal data (DPA required)            | [privacy@company.com / legal@company.com]               |
| Any data breach or suspected breach                           | [dpo@company.com / legal@company.com — within 24 hours] |
| Employee accommodation, leave dispute, or adverse action      | [hr@company.com + legal@company.com]                    |
| Worker classification decision                                | [hr@company.com + legal@company.com]                    |
| Trade secret concerns (yours or a third party's)              | [legal@company.com]                                     |
| Open source use outside the approved list                     | [legal@company.com]                                     |
| Gifts or entertainment for government officials               | [legal@company.com]                                     |
| Any active or threatened litigation                           | [legal@company.com — immediately]                       |

**When in doubt, ask.** A 5-minute email to Legal is far less costly than a problem you
handle alone.

---

## Maintenance Schedule

| Module               | Review Frequency | Review Trigger Events                                                                 | DRI                                       |
| -------------------- | ---------------- | ------------------------------------------------------------------------------------- | ----------------------------------------- |
| A. CAM               | Annual           | Org restructure, new deal types, board resolution                                     | [Commercial Counsel]                      |
| B. NDA Self-Service  | Annual           | New template, new jurisdictions, major counterparty type change                       | [Commercial Counsel]                      |
| C. Vendor Onboarding | Annual           | New vendor risk tier, DPA template update, procurement policy change                  | [Commercial/Privacy Counsel]              |
| D. Data Handling     | Quarterly        | New data regulation, supervisory authority enforcement action, GDPR threshold changes | [Privacy Counsel / DPO]                   |
| E. Employment Law    | Quarterly        | DOL rule change, FLSA threshold update, new state leave laws, FMLA/ADA guidance       | [Employment Counsel]                      |
| F. IP Basics         | Annual           | New open source policy, new PIIA terms, DTSA developments                             | [IP Counsel]                              |
| G. Expense Policy    | Annual           | IRS rate updates, FCPA guidance changes, new state reimbursement laws                 | [Employment/Compliance Counsel + Finance] |

---

## Program Launch Checklist

Before publishing this FAQ program:

- [ ] **Attorney review complete**: All NEEDS-REVIEW items reviewed and approved by qualified counsel
- [ ] **Placeholders filled**: All [PLACEHOLDER] items replaced with organizational content
- [ ] **CAM verified**: Contract authority matrix tiers confirmed current and Board/leadership approved
- [ ] **Templates linked**: NDA, vendor agreement, and other template links active and pointing to current versions
- [ ] **Escalation paths tested**: All legal@ / intake form / Slack channel links verified working
- [ ] **Jurisdiction review complete**: [JURISDICTION-SPECIFIC] markers addressed for all operating jurisdictions
- [ ] **Works council consultation**: (If EU) Any required consultation completed before publishing employment or monitoring FAQ content
- [ ] **Publication platform configured**: Content formatted and accessible to target audience
- [ ] **Communication plan executed**: Employees notified of self-service resource availability
- [ ] **Feedback mechanism active**: "Was this helpful?" mechanism enabled
- [ ] **Maintenance calendar set**: DRI assignments confirmed and calendar invites scheduled
- [ ] **Analytics baseline**: Page view / deflection tracking enabled

---

_Legal FAQ Program — Version [1.0] | [Date] | Prepared by [Legal Team]_
_This document is intended for internal use only and does not constitute legal advice._
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on:

- ACC (Association of Corporate Counsel) Legal Operations resources and Quick Counsel format
- CLOC (Corporate Legal Operations Consortium) Core 12 framework and knowledge management guidance
- DOL FLSA enforcement guidance and WHD regulations
- EU Working Time Directive (2003/88/EC) and national implementing legislation
- GDPR Regulation (EU) 2016/679 and Art. 29 Working Party / EDPB guidance
- UK Working Time Regulations 1998 and ICO Employment Practices Code
- IRS accountable plan regulations (26 C.F.R. § 1.62-2) and Publication 463
- FCPA Resource Guide (DOJ/SEC, 2020 edition)
- UK Bribery Act 2010 Guidance (Ministry of Justice)
- Defend Trade Secrets Act (18 U.S.C. §§ 1831–1839)
- California Labor Code §§ 2750.3, 2802, 2870
- Web research on legal ops self-service programs, deflection rate benchmarks, and corporate
  FAQ program design patterns (ACC, CLOC, Brightflag, Ironclad, Harvey AI publications)
- Legalcode repository reference standard: `legalcode-contract-review` skill structure and
  quality framework patterns
