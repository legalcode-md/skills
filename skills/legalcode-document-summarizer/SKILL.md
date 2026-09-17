---
name: legalcode-document-summarizer
description: 'Produce structured legal document summaries tailored to audience and purpose. Use when summarizing
  any legal document including contracts and commercial agreements, court pleadings and motions, regulatory
  filings (SEC, administrative), corporate governance documents (board resolutions, bylaws, shareholder
  agreements), and legislation or regulations. Outputs include executive summaries, key terms matrices,
  party identification tables, obligation maps, risk registers, and plain-language briefs. Adapts depth
  and language to the target audience: C-suite executives, in-house counsel, business stakeholders, paralegals,
  junior associates, or clients. Flags non-standard provisions, risk items, and missing mandatory elements.
  Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers; operates without legalcode-mcp but uses
  it when connected for verified legal authority.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Document Summarizer

> **Disclaimer**: This skill provides a framework for AI-assisted legal document
> summarization. It does not constitute legal advice. All outputs must be reviewed by a
> qualified legal professional licensed in the relevant jurisdiction before use or
> reliance. Document summaries are factual distillations, not legal opinions — they do not
> replace attorney judgment on interpretation, enforceability, or legal risk. Statutory and
> case law references cited from memory carry hallucination risk — verify against
> authoritative sources before relying on them. Summaries involving privilege should carry
> an attorney-client privilege header where applicable.

---

## Purpose and Scope

This skill produces structured, audience-calibrated summaries of legal documents across
all major document types encountered in legal practice.

**Covers:**

- Contract and commercial agreement summaries (key terms, obligations, risk register)
- Court pleading and motion summaries (caption, issues, relief, controlling authority)
- Regulatory filing summaries (SEC, administrative, compliance filings)
- Corporate governance document summaries (resolutions, bylaws, shareholder agreements)
- Legislation and regulation summaries (scope, obligations, penalties, effective dates)
- Executive summaries (decision-enabling, plain-language, conclusions-first)
- Obligation maps (party → obligation → trigger → deadline → breach consequence)
- Risk registers (severity-rated flags with escalation guidance)
- Multi-document synthesis (pattern identification across contract portfolios)

**Does not:**

- Provide legal advice or replace attorney judgment
- Guarantee privilege protection for any communication
- Classify documents for e-discovery (see `legalcode-document-classifier`)
- Draft new contracts or legal instruments (see drafting-specific skills)
- Substitute for a full legal review on high-stakes matters

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The applicable law depends on the document's own
governing law clause, the forum of the relevant proceeding, or the regulatory jurisdiction
of the filing.

[JURISDICTION-SPECIFIC] When localizing, identify and apply:

- The document's stated governing law and forum for dispute resolution
- Mandatory disclosure requirements for the document type (e.g., GDPR recitals for DPAs)
- Local legal terminology and concepts that differ from English equivalents
- Local professional conduct rules governing AI-assisted document review in that jurisdiction
- Language requirements (some jurisdictions require contracts to be in the local language)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses when:

- The document type changes the required output structure
- The audience determines depth, language register, and citation density
- The purpose (negotiation support vs. compliance monitoring vs. executive briefing) changes
  what the summary must emphasize
- Risk classification requires business context only the user can supply

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

### Step 1: Accept the Document

Accept the document in any of these formats:

- **File**: PDF, DOCX, or other document format — read via the Read tool
- **Pasted text**: Document text pasted directly into the conversation
- **URL**: Link to a document in a CLM, cloud storage, or document system

If no document is provided, prompt the user to supply one before proceeding.

For documents exceeding 100 pages, confirm whether the user needs a full-document summary
or a focused summary covering specific sections, parts, or issues.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user these questions. Present as structured
options where possible. Skip any question already answered by the initial prompt.

1. **Document type**: What kind of legal document is this?
   - Options: Commercial contract / agreement, Court pleading or motion, Regulatory filing
     (SEC, administrative), Corporate governance document (resolution, bylaws, shareholder
     agreement), Legislation or regulation, Other / Mixed
   - _Why this matters_: Determines the mandatory extraction checklist and output sections.
     Each document type has a different set of elements that must appear.

2. **Target audience**: Who will read this summary?
   - Options: C-suite / Executive / Board, In-house counsel, Business stakeholder /
     Contract manager / Operations, Paralegal / Legal analyst, Junior associate,
     External client (non-lawyer), Mixed / Multiple audiences
   - _Why this matters_: Determines language register, citation density, length target,
     and what to include vs. exclude. An executive summary for the CEO looks nothing like
     a clause-by-clause analysis for a junior associate.

3. **Purpose**: What will this summary be used for?
   - Options: Initial triage / quick orientation, Negotiation support (flagging issues and
     positions), Due diligence (portfolio or transaction review), Compliance monitoring
     (obligation tracking post-signature), Litigation preparation, Regulatory response,
     Board or executive briefing, Archive / matter record, Other
   - _Why this matters_: A negotiation-support summary emphasizes red flags and redline
     opportunities; a compliance-monitoring summary emphasizes deadlines and obligation owners.

4. **Depth**: How detailed should the output be?
   - Options: Executive brief (1-3 pages, conclusions-first, plain language), Standard
     summary (5-15 pages, all material provisions, moderate detail), Full analytical
     summary (15+ pages, clause-by-clause with citations), Obligation map only,
     Risk register only
   - _Why this matters_: Determines how much time to spend and how much detail to surface.
     Default to Standard summary if not specified.

5. **Focus areas**: Any specific provisions or issues to prioritize?
   - Options: No specific focus — full review, Liability / indemnification, IP ownership,
     Data protection / privacy, Termination and exit, Financial terms, Obligations and
     deadlines, Regulatory compliance, Other (specify)
   - Allow multiple selections.
   - _Why this matters_: Lets the summary lead with what the user cares about most.

State assumptions explicitly if the user provides partial context (e.g., "I'm assuming
this is a contract summary for in-house counsel — let me know if that's wrong").

### Step 3: Classify the Document

Before extracting content, identify:

1. **Document type** (from Step 2, or by reading the document if not provided)
2. **Parties**: All parties named, with preliminary role identification
3. **Governing law and jurisdiction** (if stated)
4. **Effective or filing date**
5. **Document length and structure**: number of pages, sections, schedules, exhibits

**⟁ CLARIFY** — If the document type is ambiguous (e.g., a "Master Agreement" that could
be an MSA, a partnership agreement, or a framework agreement), ask the user to confirm
before proceeding with extraction.

Use the classification to select the applicable extraction checklist from the
**Document-Type Analysis Reference** section below.

### Step 4: Gather Jurisdiction-Relevant Legal Authority

For documents where risk flagging requires legal context (contracts, pleadings, regulatory
filings), use **legalcode-mcp** to gather verified legal authority before analyzing.

**Research process:**

1. Identify the governing law from the document.
2. Search legalcode-mcp for jurisdiction-relevant authority across:
   - Mandatory clauses or provisions that must appear in this document type [VERIFY]
   - Statutory limits on exclusion or limitation of liability [VERIFY]
   - Data protection regime requirements [VERIFY]
   - Penalty enforceability rules [VERIFY]
   - Any regulatory deadline or threshold relevant to the document type [VERIFY]
3. Save results to `/tmp/legalcode-summarizer-authority.md`.
4. Reference this file when assigning risk classifications to flagged provisions.

**If legalcode-mcp is not connected:**

- Mark all statutory references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed using general legal knowledge, but flag that authority is unverified

[JURISDICTION-SPECIFIC] Adjust research scope to the document's governing law.

### Step 5: Extract Content by Document Type

Apply the applicable extraction checklist from the **Document-Type Analysis Reference**
section below. For each checklist item:

- Mark as **COMPLETE** if fully addressed in the document
- Mark as **PARTIAL** if present but incomplete, ambiguous, or unusual
- Mark as **MISSING** if entirely absent and expected for this document type

**⟁ CLARIFY** — For long or complex documents (50+ pages, multiple schedules, or
incorporated-by-reference documents):

- Ask whether to perform a full extraction of all checklist items, or a priority extraction
  focused on the user's stated focus areas.
- If the document incorporates external documents by reference (e.g., terms at a URL, a
  standard form, or a schedule not provided), ask whether to flag those as unreviewed or
  proceed as if they exist.

Read the entire document before extracting. Clauses interact — what appears to grant a
right in one section may be limited by an exception in another. Never summarize a clause
in isolation without checking cross-references.

### Step 6: Build the Obligation Map

For contracts, agreements, and regulatory filings, build an obligation map using the
framework in the **Obligation Mapping Framework** section below.

For each obligation identified:

1. Identify the obligated party (exact legal name and defined term)
2. Classify: Affirmative obligation / Negative covenant / Conditional obligation
3. Identify the triggering event or condition
4. State the performance standard
5. State the deadline (specific date or relative trigger)
6. State the consequence of breach (remedy, penalty, termination right)
7. Assign a risk rating: CRITICAL / HIGH / MEDIUM / LOW
8. Cite the clause and page number

For pleadings and motions, map the procedural obligations instead: response deadlines,
hearing dates, production deadlines, and briefing schedules.

**⟁ CLARIFY** — For complex obligation maps with many owners, ask whether the user wants:

- A full obligation table (all obligations by all parties)
- A party-specific view (obligations of one party only — specify which)
- A deadline-sorted calendar view (obligations ordered by deadline)

### Step 7: Risk Flagging

Identify and classify all material risk items using the **Risk Classification System**
below. For each risk item:

- Assign a severity tier: CRITICAL / HIGH / MEDIUM / LOW / INFORMATIONAL
- Describe the specific risk and its source
- Cite the provision (or note the absence that creates the risk)
- State the recommended action

**⟁ CLARIFY** — For borderline severity classifications where business context matters:

- "This indemnification obligation has no cap. Depending on deal value and counterparty
  creditworthiness, I'd classify this CRITICAL or HIGH. What is the approximate deal size?"
- "This auto-renewal provision requires [X]-day notice. Is this a concern for your
  organization's contract management process?"

### Step 8: Draft the Summary

Produce the summary using the applicable output template from the **Output Format
Template** section. Apply the audience adaptation rules from the **Audience Adaptation
Framework** section.

**⟁ CLARIFY** — Before delivering, confirm any open scope decisions:

- "I found [N] CRITICAL and [M] HIGH risk items. Should I draft the full summary first
  and include all of them, or deliver a quick triage memo on the critical items now?"
- "The document is [X] pages. The full summary will be approximately [Y] pages. Is that
  the depth you need, or would a shorter executive brief serve better?"

### Step 9: Quality Verification

Before delivering, run the quality checks in the **Quality Assurance Framework** section:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every CRITICAL-rated risk item, run the 3-pass Self-Interrogation. Revise if
   any pass reveals a weakness.
3. Assign a Confidence Score to each material extraction claim.
4. Verify completeness: confirm all checklist items for the document type have been
   addressed (COMPLETE, PARTIAL, or MISSING — not silently skipped).
5. Verify audience calibration: check that language register, citation density, and length
   match the stated audience.
6. Generate the Glass Box Audit Trail and append it to the output.

### Step 10: Deliver

Deliver the summary in the output format for the document type and audience. Lead with the
most important findings — never bury critical risk flags in footnotes or appendices.

If the summary is for multiple audiences, deliver the executive brief first, followed by
the detailed analysis, clearly separated and labeled.

---

## Document-Type Analysis Reference

### 1. Contracts and Commercial Agreements

**Mandatory extraction fields:**

| #   | Field                                | Notes                                                                                              |
| --- | ------------------------------------ | -------------------------------------------------------------------------------------------------- |
| 1   | Party table                          | Full legal name, entity type, jurisdiction of formation, address, role, defined term, signatory    |
| 2   | Contract type and classification     | MSA, SOW, NDA, SaaS Agreement, Employment Agreement, License, etc.                                 |
| 3   | Effective date and term              | Initial term, renewal mechanics, auto-renewal flag                                                 |
| 4   | Scope of goods / services / license  | What is being provided; field-of-use restrictions if any                                           |
| 5   | Financial terms                      | Price, payment schedule, milestones, late payment, price escalation                                |
| 6   | Performance obligations              | By party, with deadlines, acceptance criteria, SLAs                                                |
| 7   | Intellectual property                | Ownership, background IP, developed IP, assignment, license grants, work-for-hire characterization |
| 8   | Confidentiality                      | Scope, duration, carve-outs, return / destruction obligations                                      |
| 9   | Indemnification                      | Scope, mutual vs. unilateral, cap, procedure triggers                                              |
| 10  | Limitation of liability              | Cap amount, excluded damages, carve-outs, mutual vs. asymmetric                                    |
| 11  | Representations and warranties       | Scope, by whom, survival period, disclaimer                                                        |
| 12  | Conditions precedent                 | Triggers to effectiveness or performance                                                           |
| 13  | Termination                          | Grounds, notice, cure period, effects, wind-down                                                   |
| 14  | Governing law and dispute resolution | Governing law, venue, arbitration vs. litigation, escalation steps                                 |
| 15  | Assignment and change of control     | Consent requirements, permitted transfers, CoC provisions                                          |
| 16  | Force majeure                        | Scope, notification, mitigation, duration trigger for termination                                  |
| 17  | Data protection                      | DPA requirement, processor / controller classification, breach notification, transfer mechanisms   |
| 18  | Compliance and regulatory            | Anti-bribery, sanctions, modern slavery, audit rights                                              |

**Non-standard provision flags:** Prominently flag any deviation from market standard:

- Asymmetric termination rights
- Uncapped or unclarified indemnification scope
- Overly broad IP assignment (capturing pre-existing IP)
- Auto-renewal with insufficient notice window
- Limitation of liability at or below a single month of fees
- Unilateral amendment rights
- No governing law or dispute resolution clause

**Severity classification for contracts:**

| Status | Meaning                                                                       |
| ------ | ----------------------------------------------------------------------------- |
| GREEN  | Market-standard or better than standard; note for awareness                   |
| YELLOW | Below standard but negotiable; flag with recommended alternative language     |
| RED    | Outside acceptable range; requires negotiation or escalation before execution |

### 2. Court Pleadings and Motions

**Mandatory extraction fields:**

| #   | Field                                 | Notes                                                                                                      |
| --- | ------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| 1   | Caption                               | Court, case number, judge / magistrate, parties (plaintiff, defendant, appellant, appellee), docket number |
| 2   | Document type                         | Complaint, Answer, Motion for Summary Judgment, Motion to Dismiss, Brief, etc.                             |
| 3   | Filing date and deadline implications | Any response deadline triggered by the filing                                                              |
| 4   | Moving party and relief sought        | One-paragraph summary of what the filer is asking for                                                      |
| 5   | Legal standard                        | Applicable standard (e.g., Rule 12(b)(6) plausibility, Rule 56 no genuine dispute)                         |
| 6   | Undisputed material facts             | Numbered summary with record citations                                                                     |
| 7   | Disputed material facts               | Issues of fact that must go to a finder of fact                                                            |
| 8   | Legal issues presented                | Issue-by-issue breakdown in the order argued                                                               |
| 9   | Controlling authority                 | Key cases and statutes cited, with holdings                                                                |
| 10  | Key admissions / damaging statements  | Favorable statements by opposing party in the record                                                       |
| 11  | Requested relief                      | Exact language of the relief requested                                                                     |
| 12  | Outcome scenarios                     | What happens procedurally if the motion is granted vs. denied                                              |

**Format note for pleading summaries:** Organize by issue. For each issue: (1) applicable
legal standard, (2) key supporting facts with record citations, (3) controlling authority
and its holding, (4) application to this case, (5) conclusion. Do not re-argue; distill.

### 3. Regulatory Filings

**For SEC periodic reports (10-K, 10-Q, 20-F):**

| #   | Field                        | Notes                                                                                      |
| --- | ---------------------------- | ------------------------------------------------------------------------------------------ |
| 1   | Company and period           | Registrant, fiscal year / quarter, filing date                                             |
| 2   | Business description         | Segments, industry, primary markets                                                        |
| 3   | Material risk factors        | Top 5-10 by category: strategic, operational, financial, legal / regulatory, cybersecurity |
| 4   | Legal proceedings            | Pending material litigation, regulatory investigations, settlements                        |
| 5   | MD&A highlights              | Revenue trends, operating performance, liquidity, capital resources, known trends          |
| 6   | Financial highlights         | Key line items: revenue, EBITDA, net income, debt levels                                   |
| 7   | Critical accounting policies | Estimates with material uncertainty                                                        |
| 8   | Governance notes             | Executive compensation structure, related-party transactions                               |
| 9   | Auditor opinion              | Qualified or unqualified; going-concern language if present                                |
| 10  | Subsequent events            | Material events after period end                                                           |

**For comment letters and administrative filings:**

| #   | Field                       | Notes                                                      |
| --- | --------------------------- | ---------------------------------------------------------- |
| 1   | Rulemaking identification   | Rule / docket number, agency, comment period               |
| 2   | Statutory authority         | Enabling statute cited                                     |
| 3   | Proposed rule summary       | Plain-language description of what is proposed             |
| 4   | Compliance obligation dates | Effective date, phase-in periods, transition rules         |
| 5   | Industry impact             | Who is covered, who is exempt, estimated compliance burden |
| 6   | Open interpretive questions | Ambiguities in the proposal requiring clarification        |

### 4. Corporate Governance Documents

**Board Resolutions:**

| #   | Field                | Notes                                               |
| --- | -------------------- | --------------------------------------------------- |
| 1   | Resolution type      | Routine vs. material transaction                    |
| 2   | Action authorized    | Exactly what is approved                            |
| 3   | Authorized officers  | Names, titles, and authority scope                  |
| 4   | Vote record          | Unanimous vs. majority; any dissents or abstentions |
| 5   | Effective date       | Conditions to effectiveness                         |
| 6   | Related transactions | Any agreements or transactions referenced           |

**Bylaws:**

| #   | Field                | Notes                                                    |
| --- | -------------------- | -------------------------------------------------------- |
| 1   | Board composition    | Director count, term, qualification requirements         |
| 2   | Meeting requirements | Quorum, notice period, frequency, written consent        |
| 3   | Voting mechanics     | Majority vs. supermajority thresholds by action type     |
| 4   | Officer authority    | Roles and scope of authority                             |
| 5   | Amendment process    | Required approvals, notice requirements                  |
| 6   | Shareholder rights   | Meeting procedures, inspection rights, demand procedures |

**Shareholder / Stockholder Agreements:**

| #   | Field                                | Notes                                                     |
| --- | ------------------------------------ | --------------------------------------------------------- |
| 1   | Party table                          | Shareholders, ownership percentages, share classes        |
| 2   | Transfer restrictions                | ROFR, drag-along, tag-along mechanics                     |
| 3   | Governance rights                    | Board appointment rights by shareholder class             |
| 4   | Reserved matters                     | Actions requiring supermajority or minority consent       |
| 5   | Anti-dilution and pre-emptive rights | Structure, triggers, waivers                              |
| 6   | Dividend policy                      | Declared, committed, or discretionary                     |
| 7   | Exit provisions                      | Drag-along mechanics, IPO obligations, put / call options |
| 8   | Non-compete / non-solicitation       | Scope, geography, duration                                |
| 9   | Dispute resolution                   | Mechanism, governing law                                  |

### 5. Legislation and Regulations

**Mandatory extraction fields:**

| #   | Field                       | Notes                                                       |
| --- | --------------------------- | ----------------------------------------------------------- |
| 1   | Citation                    | Statute, regulation, or directive citation and jurisdiction |
| 2   | Effective date              | Enactment date, entry into force, and any phase-in periods  |
| 3   | Scope                       | Who is covered; who is expressly exempted                   |
| 4   | Prohibited conduct          | What the statute / regulation prohibits                     |
| 5   | Affirmative obligations     | What covered entities must do                               |
| 6   | Enforcement mechanism       | Enforcing agency, powers, penalty structure                 |
| 7   | Private right of action     | Whether private parties may sue; standing requirements      |
| 8   | Safe harbors and exceptions | Enumerated defenses or exclusions                           |
| 9   | Preemption                  | Whether federal / national law preempts state / local law   |
| 10  | Key defined terms           | Definitions that determine scope of application             |
| 11  | Transition provisions       | Grandfather clauses, compliance deadlines, interim rules    |

---

## Audience Adaptation Framework

Adapt every output along these five dimensions based on the stated audience:

| Dimension         | Executive / Board               | In-House Counsel                                                     | Business Stakeholder                     | Associate / Analyst                        | Client (non-lawyer)                      |
| ----------------- | ------------------------------- | -------------------------------------------------------------------- | ---------------------------------------- | ------------------------------------------ | ---------------------------------------- |
| **Language**      | Plain English; no jargon        | Legal terminology acceptable; plain-language bottom line per section | Plain English throughout                 | Full legal vocabulary                      | Plain English; all legal terms explained |
| **Depth**         | 1-3 pages; conclusions-first    | 3-10 pages; material provisions only                                 | Obligation tables and deadline calendars | Full clause-by-clause analysis             | FAQ or narrative                         |
| **Citations**     | None (unless requested)         | Section references at key claims                                     | None                                     | Section + page for every claim             | None                                     |
| **Risk framing**  | Binary: act / no action         | Severity-tiered with legal basis                                     | Operational impact only                  | Full analysis including minority arguments | Plain-language impact                    |
| **Structure**     | Narrative prose, minimal tables | Headers + sections + issue list                                      | Tables and calendars                     | Mirrors document structure                 | Simple bullets or Q&A                    |
| **Length target** | 5-10% of source                 | 15-30% of source                                                     | 10-20% of source                         | Up to 50% of source                        | 5-10% of source                          |

**Invariant rules regardless of audience:**

- Never assign an obligation to the wrong party
- Never characterize a unilateral obligation as mutual, or vice versa
- Never omit CRITICAL or HIGH risk flags from any audience level — frame them differently,
  but never suppress them
- Never state a legal conclusion without a basis (cite the clause or note uncertainty)

---

## Obligation Mapping Framework

Use this framework for all contracts, agreements, and regulatory filing summaries.

### The Three Obligation Dimensions

Analyze every provision from each contracting party's perspective separately:

1. **Obligations** — What the party MUST do (affirmative duties)
2. **Entitlements** — What the party MAY do or is entitled to receive
3. **Prohibitions** — What the party MUST NOT do

### Obligation Table Format

For each obligation identified, populate these fields:

| Field                 | Content                                                              |
| --------------------- | -------------------------------------------------------------------- |
| Party                 | Exact legal entity name and defined term                             |
| Obligation type       | Affirmative / Negative / Conditional                                 |
| Description           | Plain-language statement of the obligation                           |
| Triggering event      | What must occur to activate the obligation                           |
| Performance standard  | How the obligation must be performed                                 |
| Deadline              | Specific date or relative trigger (e.g., "within 10 days of notice") |
| Consequence of breach | Remedy, penalty, termination right, or other consequence             |
| Risk rating           | CRITICAL / HIGH / MEDIUM / LOW                                       |
| Clause reference      | Section number and page                                              |

### Obligation Lifecycle Stages

Track obligations across four stages in the summary:

1. **Pre-execution** — Conditions precedent to effectiveness
2. **Ongoing** — Continuing obligations during the term
3. **Triggered** — Obligations activated by specific events (breach, change of control, etc.)
4. **Post-termination** — Obligations that survive expiration or termination

### Deadlines Calendar

For compliance-monitoring summaries, produce a separate deadlines calendar:

```
UPCOMING DEADLINES — [Contract / Matter Name]

[Date]    [Party]    [Obligation]    [Consequence if Missed]    [Clause Ref]
[Date]    [Party]    [Obligation]    [Consequence if Missed]    [Clause Ref]
```

---

## Risk Classification System

### Severity Tiers

| Tier              | Definition                                                                                                               | Required Action                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| **CRITICAL**      | Immediate legal, financial, or regulatory exposure; deal-breaker level; requires resolution before execution or reliance | Escalate immediately to senior counsel; do not execute or rely on the document without resolution |
| **HIGH**          | Material risk beyond acceptable threshold; significant exposure if unaddressed                                           | Negotiate change; senior counsel review required before proceeding                                |
| **MEDIUM**        | Below-standard or unusual term within a negotiable range; moderate exposure                                              | Flag for discussion; document acceptance rationale if not negotiated                              |
| **LOW**           | Minor deviation; commercially reasonable alternatives exist; minimal exposure                                            | Note for awareness; no escalation needed                                                          |
| **INFORMATIONAL** | Non-standard or noteworthy but not adverse; worth flagging for completeness                                              | Note in summary; no action required                                                               |

### Risk Categories

Classify each risk item by category:

| Category                      | Covers                                                                                                    |
| ----------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Legal / Compliance**        | Non-compliant provisions, missing mandatory clauses, jurisdiction conflicts, regulatory exposure          |
| **Financial**                 | Uncapped liability, unfavorable payment terms, penalty exposure, price adjustment mechanisms              |
| **Operational**               | Unclear responsibility allocation, vague deliverables, onerous SLAs, unrealistic timelines                |
| **Strategic**                 | Overly restrictive exclusivity, inflexible duration, change-of-control exposure, competitive restrictions |
| **Reputational / Regulatory** | Counterparty conduct risk, sanctions exposure, non-compliant data handling                                |

### Automatic CRITICAL Triggers

The following provisions always warrant CRITICAL classification pending context:

- Unlimited or uncapped indemnification obligation
- Governing law or venue that is unusual or clearly unfavorable for the deal type
- IP assignment clause that captures pre-existing IP
- No limitation of liability in a high-value agreement
- Auto-renewal with notice period shorter than the organization's standard review cycle
- Change-of-control without consent right on a strategic agreement
- Data breach notification timeline exceeding applicable regulatory requirement
- Material adverse change definition so narrow it is effectively unavailable [VERIFY]
- Conditions precedent to the other party's obligations that are within their sole control

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                  | Fail Action                         |
| -------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every material extraction claim cites a specific section, article, or page number in the source document              | Add citation or mark "[UNVERIFIED]" |
| **Format**     | All citations follow a consistent format for the document type (section numbers, docket citations, statute citations) | Fix format                          |
| **Currency**   | For regulatory filings and legislation: verify the cited version is current and in force                              | Flag "[CHECK CURRENCY]"             |
| **Domain**     | Analysis stays within the document's governing law and document type                                                  | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty in interpretation or risk classification explicitly stated, not hidden                                    | Add confidence qualifier            |

### Self-Interrogation for CRITICAL Items

For every item classified CRITICAL, apply this 3-pass review:

**Pass 1 — Factual accuracy**: Does the extraction accurately state what the document
says? Read the actual clause text. Does the summary characterize it correctly, including
all conditions, exceptions, and cross-references?

**Pass 2 — Risk chain integrity**: Does the CRITICAL classification follow logically from
the clause? What specific harm arises? Is the harm actual or theoretical? Would a
reasonable practitioner agree with this classification?

**Pass 3 — Challenge**: What is the strongest argument that this item is not CRITICAL?
Under what circumstances would a reasonable professional accept the risk as stated? If
there is a plausible counter-argument, lower the severity or add a confidence qualifier.

### Confidence Scoring

Assign a Confidence Score to each material extraction claim:

| Level         | Range     | Meaning                                                        | Action                                             |
| ------------- | --------- | -------------------------------------------------------------- | -------------------------------------------------- |
| **Definite**  | 0.95-1.0  | Clear, unambiguous clause text; direct extraction              | State with confidence                              |
| **High**      | 0.80-0.94 | Clause text is clear but requires cross-reference confirmation | State with brief caveat                            |
| **Probable**  | 0.60-0.79 | Clause is ambiguous or incomplete; interpretation required     | State with reasoning and note alternative reading  |
| **Possible**  | 0.40-0.59 | Genuine ambiguity; multiple plausible readings                 | Flag for attorney review with both interpretations |
| **Uncertain** | 0.0-0.39  | Insufficient basis for confident extraction                    | Mark "[UNCERTAIN — requires attorney review]"      |

---

## Glass Box Audit Trail

Append this audit trail to every delivered summary:

```yaml
glass_box:
  skill_name: "legalcode-document-summarizer"
  document_type: "[Contract / Pleading / Regulatory Filing / Corporate / Legislation]"
  document_name: "[Name or description of document summarized]"
  audience: "[Executive / In-House Counsel / Business Stakeholder / Associate / Client]"
  purpose: "[Triage / Negotiation / Due Diligence / Compliance / Litigation / Board Briefing]"
  depth_requested: "[Executive Brief / Standard / Full Analytical / Obligation Map / Risk Register]"
  jurisdiction: "[Governing law identified, or 'Not stated']"
  legalcode_mcp: "[Connected — citations verified] / [Not connected — manual verification required]"
  checklist_items_assessed: "[Number of checklist items evaluated]"
  items_complete: "[Number marked COMPLETE]"
  items_partial: "[Number marked PARTIAL]"
  items_missing: "[Number marked MISSING]"
  obligations_mapped: "[Number of obligations identified]"
  risk_items_flagged: "[Number flagged, by tier: CRITICAL: N, HIGH: N, MEDIUM: N, LOW: N]"
  citations_verified: "[Number VERIFIED via legalcode-mcp] / [Number marked VERIFY]"
  confidence_notes: "[Any material confidence qualifiers applied]"
  limitations:
    - "[Document sections not provided or reviewed]"
    - "[Incorporated-by-reference documents not reviewed]"
    - "[Jurisdiction-specific law not independently verified]"
  reviewer: "AI-assisted — requires qualified legal review before reliance"
```

---

## Anti-Patterns

What NOT to do when producing legal document summaries:

1. **Copying clause text verbatim** — A summary that reproduces clauses at length is not
   a summary; it is a second copy. Extract, synthesize, and paraphrase with citation. The
   only exception is exact quotation of critical language where precision matters (e.g.,
   the exact wording of a liability cap or an indemnification trigger).

2. **Summarizing in isolation** — Analyzing a clause without reading the entire document
   first. Clauses interact. An uncapped indemnification obligation may be partially
   mitigated by a limitation of liability carve-out. A termination right may be
   conditioned on a prior cure period buried elsewhere.

3. **Omitting exceptions and carve-outs** — The most dangerous extraction failure. A
   summary that states a general rule without its exceptions (e.g., "the cap does not
   apply to IP indemnification") creates false confidence that the general rule applies
   universally.

4. **Losing conditional logic** — Summarizing "Party A must pay" when the clause says
   "Party A must pay unless X, provided that Y, subject to Z." Every if-then chain and
   materiality qualifier must be preserved.

5. **Misidentifying the obligated party** — Assigning an obligation to the wrong party.
   This failure is catastrophic in compliance contexts. Always verify party identity
   against the defined-term section and signature block.

6. **Characterizing unilateral obligations as mutual** — Stating that both parties bear
   a right or obligation that the document assigns to only one. Common with indemnification,
   termination rights, and audit rights.

7. **Using a generic template regardless of document type** — Applying a contract template
   to a court filing, or a corporate governance template to a regulatory filing. Each
   document type has a different mandatory checklist. Using the wrong checklist produces
   false completeness signals.

8. **Suppressing risk flags for the audience** — Omitting CRITICAL or HIGH risk items
   from executive summaries because they seem too technical or alarming. Frame them
   differently for non-lawyers, but never suppress material risk. The attorney advising
   the executive is responsible; the summary is the attorney's tool.

9. **Jargon in executive-facing summaries** — Using legal terms without explanation in
   summaries intended for non-lawyers. Every legal concept in an executive or client
   summary must be translated into plain language.

10. **No call to action in executive summaries** — Delivering an executive summary that
    describes what the document says but does not state what the decision-maker should do.
    Every executive summary must end with a clear recommended action or authority request.

11. **Inconsistent defined-term usage** — Alternating between a party's full legal name
    and its defined term within the summary. Pick one and use it consistently throughout.
    Inconsistency signals lack of care and makes the summary harder to read.

12. **Missing cross-references to schedules and exhibits** — Summarizing the main body
    without noting that key terms (pricing, scope, SLAs, data processing requirements) are
    defined in schedules or exhibits. If those schedules are not reviewed, the summary must
    explicitly flag the gap.

13. **Fabricating missing fields** — If a mandatory field is absent from the document (e.g.,
    no governing law clause), flagging it as MISSING is correct. Do not infer or assume the
    field's content. Never populate an extraction field with a guess.

14. **Confidence laundering** — Expressing low-confidence extractions with the same certainty
    as high-confidence ones. Every uncertain interpretation must carry a confidence qualifier.
    Uniform confidence expression across the entire summary signals that no quality review
    occurred.

15. **Single-audience format for multi-audience delivery** — When delivering to multiple
    audiences, producing a single document that compromises between formats. Deliver the
    executive brief and the detailed analysis as clearly separated sections, not blended.

16. **Omitting the Glass Box audit trail** — Delivering a summary without the structured
    audit trail. The audit trail records what was and was not reviewed, enabling downstream
    reviewers to assess the summary's scope and limitations.

17. **Skipping the completeness check** — Producing the output in a single pass without
    verifying that all mandatory checklist items for the document type have been addressed.
    Use the document-type checklist explicitly, not from memory.

---

## Writing Standards

Apply these standards before delivering any summary output:

**Lead with what matters most.** For executive summaries: risk flags and recommended
actions first, background second. For analytical summaries: each section leads with the
key finding, then supporting detail.

**Plain language for all audiences.** Even in associate-level summaries, prefer concrete
over abstract, active voice over passive, and short sentences over compound structures.
Every sentence should carry exactly one idea.

**Defined terms, used consistently.** Once a party or concept is identified with a defined
term (e.g., "the Vendor"), use that term throughout. Never alternate between "the Vendor,"
"ABC Corp.," and "it" to refer to the same party.

**Precision over brevity when it matters.** In obligation and risk analysis, precision
is more important than brevity. If the exact wording of a clause determines the scope of a
liability cap, quote it and cite it rather than paraphrasing.

**No advocacy.** A legal document summary is a factual distillation, not a brief. Do not
argue for an interpretation; present the most natural reading and flag alternatives where
they exist.

**Quality gates before delivery:**

- [ ] Every material claim cites a specific section or page
- [ ] No obligation is assigned to the wrong party
- [ ] No unilateral provision is characterized as mutual
- [ ] All CRITICAL and HIGH risks are present regardless of audience
- [ ] Defined terms are used consistently throughout
- [ ] Language register matches the stated audience
- [ ] Glass Box audit trail is complete and appended

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.
legalcode-mcp provides a law, regulatory, and case law database with search across
jurisdictions.

**With legalcode-mcp connected (preferred):**

- Use in Step 4 to verify jurisdiction-specific legal requirements for risk flagging
- Verify whether a flagged provision violates a mandatory statutory requirement
- Confirm whether a missing clause (e.g., data processing addendum) is legally required
  under the applicable law
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory references with [VERIFY]
- Proceed with general legal knowledge for risk classification
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Advise the user that risk classifications related to mandatory legal requirements have
  not been independently verified against current law

---

## Output Format Template

### Template A: Executive Brief

```markdown
# [Document Name] — Executive Summary

**Document type**: [Type]
**Parties**: [Party A] and [Party B]
**Date**: [Effective date / Filing date]
**Prepared for**: [Audience]
**Privilege**: [Attorney-Client Privileged / Not Privileged / Mark as appropriate]

---

## Bottom Line

[2-3 sentences: What is this document, what does it do, and what is the most important
thing the reader needs to know or decide?]

## Key Financial Commitments

| Commitment | Amount   | Due              | Party Responsible |
| ---------- | -------- | ---------------- | ----------------- |
| [Item]     | [Amount] | [Date / Trigger] | [Party]           |

## Critical Issues — Requiring Decision

| #   | Issue                                 | Severity | Recommended Action |
| --- | ------------------------------------- | -------- | ------------------ |
| 1   | [Issue description in plain language] | CRITICAL | [Action]           |
| 2   | [Issue description]                   | HIGH     | [Action]           |

## Key Obligations

[3-5 bullet points covering the most important things each party must do, by when]

## Recommended Action

[Specific decision requested from the reader — approve, escalate, negotiate X before
signing, etc. Never leave an executive summary without a clear call to action.]
```

---

### Template B: Standard Summary

```markdown
# [Document Name] — Summary

**Document type**: [Type]
**Governing law**: [Jurisdiction]
**Effective date**: [Date]
**Term**: [Duration and renewal mechanics]
**Prepared for**: [Audience / Purpose]

---

## 1. Party Identification

| Party | Full Legal Name | Entity Type     | Jurisdiction    | Role                | Defined Term | Signatory     |
| ----- | --------------- | --------------- | --------------- | ------------------- | ------------ | ------------- |
| [A]   | [Full name]     | [LLC/Corp/etc.] | [State/Country] | [Buyer/Seller/etc.] | ["Company"]  | [Name, Title] |

## 2. Key Terms Matrix

| Provision        | Summary   | Clause Ref | Status                       | Risk                           |
| ---------------- | --------- | ---------- | ---------------------------- | ------------------------------ |
| [Provision name] | [Summary] | § [X]      | COMPLETE / PARTIAL / MISSING | CRITICAL / HIGH / MEDIUM / LOW |

## 3. Obligation Map

| Party   | Obligation   | Type        | Trigger   | Deadline | Breach Consequence     | Risk   | Clause |
| ------- | ------------ | ----------- | --------- | -------- | ---------------------- | ------ | ------ |
| [Party] | [Obligation] | Affirmative | [Trigger] | [Date]   | [Remedy / termination] | [Tier] | § [X]  |

## 4. Risk Register

| #   | Risk Item | Category   | Severity | Source | Recommended Action |
| --- | --------- | ---------- | -------- | ------ | ------------------ |
| 1   | [Risk]    | [Category] | CRITICAL | § [X]  | [Action]           |

## 5. Non-Standard Provisions

[Provisions that deviate from market standard — note the deviation and recommend position]

## 6. Missing Mandatory Elements

[Any checklist items classified MISSING — explain why they matter and what to do]

## 7. Summary Assessment

[2-3 paragraph overall assessment suitable for the audience: overall risk level, main
negotiation priorities, recommended next steps]

---

_Glass Box Audit Trail: [Append YAML block here]_
```

---

### Template C: Obligation Map Only

```markdown
# [Document Name] — Obligation Map

**Parties**: [List all parties]
**Effective date**: [Date]
**Source**: [Document reference]

---

## Pre-Execution Obligations

| Party | Obligation | Deadline | Consequence | Clause |
| ----- | ---------- | -------- | ----------- | ------ |

## Ongoing Obligations

| Party | Obligation | Frequency / Duration | Performance Standard | Consequence | Clause |
| ----- | ---------- | -------------------- | -------------------- | ----------- | ------ |

## Triggered Obligations

| Party | Obligation | Triggering Event | Deadline from Trigger | Consequence | Clause |
| ----- | ---------- | ---------------- | --------------------- | ----------- | ------ |

## Post-Termination Obligations

| Party | Obligation | Duration | Consequence | Clause |
| ----- | ---------- | -------- | ----------- | ------ |

## Deadlines Calendar

| Date | Party | Obligation | Consequence if Missed | Clause |
| ---- | ----- | ---------- | --------------------- | ------ |

---

_Glass Box Audit Trail: [Append YAML block here]_
```

---

### Template D: Risk Register Only

```markdown
# [Document Name] — Risk Register

**Parties**: [List]
**Date**: [Effective date / Filing date]
**Prepared for**: [Audience]

---

## Critical Risks — Immediate Escalation Required

| #   | Risk Description | Category | Source | Recommended Action |
| --- | ---------------- | -------- | ------ | ------------------ |

## High Risks — Negotiate Before Execution

| #   | Risk Description | Category | Source | Recommended Action |
| --- | ---------------- | -------- | ------ | ------------------ |

## Medium Risks — Document and Monitor

| #   | Risk Description | Category | Source | Notes |
| --- | ---------------- | -------- | ------ | ----- |

## Low Risks / Informational

| #   | Provision | Category | Notes |
| --- | --------- | -------- | ----- |

## Missing Mandatory Elements

| #   | Missing Element | Severity | Why It Matters | Recommended Action |
| --- | --------------- | -------- | -------------- | ------------------ |

---

_Glass Box Audit Trail: [Append YAML block here]_
```

---

## Localization Notes

When summarizing documents governed by non-English-law systems, apply these adjustments:

- **Use local legal terminology** alongside English equivalents in parentheses (e.g.,
  "mise en demeure (formal demand letter)" for French law documents)
- **Note civil law vs. common law differences** where they affect the summary (e.g.,
  civil law systems fill contractual gaps with statutory defaults that common law systems
  leave to the parties to address)
- **Flag language requirements**: In some jurisdictions, documents must be in the local
  language to be enforceable; if the document reviewed is in English but governs a
  jurisdiction with language requirements, flag this [VERIFY]
- **Note notarization, registration, or apostille requirements** where applicable to the
  document type and jurisdiction [VERIFY]

[JURISDICTION-SPECIFIC] For each jurisdiction, verify current mandatory disclosure and
formality requirements for the document type before finalizing risk classifications.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on:

- Research into AI-assisted legal document summarization best practices (Harvey, Kira,
  ContractPodAi, Luminance platforms and their published workflows)
- The CONTRASUM party-specific obligation mapping framework (EMNLP 2023 research)
- ABA Formal Opinion 2024 and state bar guidance on AI use in legal practice (Texas
  Opinion 705 / California guidance)
- Stanford Law School empirical research on legal AI hallucination rates (2025)
- The Legalcode reference standard: `legalcode-contract-review`
- Repository quality frameworks: Citation Quality Gates, Self-Interrogation, Confidence
  Scoring, and Glass Box Audit Trail patterns adapted from `legalcode-contract-review`

This skill is a Legalcode original synthesis. No external skill files were merged.
