---
name: legalcode-licensing-agreement-review
description: Review IP licensing agreements of all categories — patents, trademarks, copyright, trade
  secrets, know-how, and mixed-IP bundles — against organizational positions or general market standards.
  Use when reviewing any IP license for grant scope, field-of-use or territory restrictions, sublicensing
  chain provisions, royalty structures and audit rights, improvement and grant-back clauses, IP title
  warranties, infringement indemnification, licensor insolvency protections (including §365(n)), and termination
  effects on licensed rights.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review IP licensing agreements of all categories — patents, trademarks, copyright, trade secrets, know-how, and mixed-IP bundles — against organizational positions or general market standards. Identifies deviations, generates confidence-scored redlines, and produces an auditable analysis. Use when reviewing any IP license for grant scope, field-of-use or territory restrictions, sublicensing chain provisions, royalty structures and audit rights, improvement and grant-back clauses, IP title warranties, infringement indemnification, licensor insolvency protections (including §365(n)), and termination effects on licensed rights. Covers pharmaceutical licenses, software licenses, trademark franchise-adjacent licenses, copyright and music licenses, trade secret licenses, know-how licenses, university technology transfer, and mixed-IP bundles. Jurisdiction- agnostic with localization markers for US, EU, and UK frameworks. Triggers on any request to review, analyse, flag, or provide a second opinion on an IP license, licensing agreement, technology transfer agreement, copyright assignment-plus-license arrangement, trademark license, or know-how agreement.


# Legalcode IP Licensing Agreement Review

> **Disclaimer**: This skill provides a framework for AI-assisted review of IP licensing
> agreements. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional — preferably one with IP, licensing, or technology
> transactions experience — licensed in the relevant jurisdiction before use. Laws change;
> verify current applicability before relying on any provision described here. Statutory
> and case law references carry hallucination risk — verify against authoritative sources
> (LII, EUR-Lex, BAILII, national patent/trademark/copyright office publications) before
> relying on them. Competition law compliance (TTBER, Sherman Act, Chapter I Competition
> Act 1998) and bankruptcy/insolvency analysis (§365(n), Insolvency Act 1986) require
> specialist counsel; this skill provides a framework, not a definitive analysis.

---

## Purpose and Scope

This skill reviews IP licensing agreements across all IP categories. It identifies
deviations from organizational positions or market standards, classifies their severity,
generates actionable redlines, and produces a confidence-scored, auditable analysis.

**Covers:**

- Grant scope analysis: exclusivity, field of use, territory, permitted acts, sublicensing
- Royalty structures: running royalties, lump sum, milestones, hybrid, MFN/MFL clauses
- Royalty base analysis: net sales deductions, SSPPU vs. EMVR, post-expiration prohibition
- Sublicensing chains: flow-down requirements, sublicense conversion/survival on termination
- IP title warranties: ownership, quiet enjoyment, non-infringement, authority to license
- Infringement indemnification: remedy waterfall, caps, carve-outs, defense obligations
- Royalty audit rights: scope, frequency, sublicensee reach, underpayment thresholds
- Improvement and grant-back clauses: antitrust screening (TTBER, DOJ/FTC guidelines)
- Termination and wind-down: post-termination IP rights, sublicense survival, sell-off
- Licensor insolvency protections: §365(n), trademark gap, EU/UK contractual alternatives
- Source code / IP embodiment escrow: trigger events, verification levels, SaaS alternatives
- IP-category-specific issues: quality control (trademark), moral rights (copyright), Brulotte
  prohibition (patent), reasonable measures (trade secret), §203 termination (copyright)

**Does not:**

- Draft new licensing agreements from scratch (see `legalcode-technology-license-agreement`)
- Perform competition law / antitrust compliance screening under TTBER or US Sherman Act
  (see `legalcode-technology-license-review` for TTBER safe harbor and SEP/FRAND analysis)
- Perform freedom-to-operate (FTO) or patent validity analysis (see `legalcode-patent-landscape-analysis`)
- Perform copyright infringement assessment (see `legalcode-copyright-infringement-assessment`)
- Perform trade secret program audits (see `legalcode-trade-secret-audit`)
- Replace specialist IP, licensing, bankruptcy, competition law, or export control counsel
- Provide legal advice or create a lawyer-client relationship

**Complementary skills:**

- `legalcode-technology-license-agreement` — draft and structure technology license agreements
- `legalcode-technology-license-review` — TTBER safe harbor, SEP/FRAND, antitrust compliance
- `legalcode-ip-assignment-agreement` — outright assignment of IP rather than licensing
- `legalcode-contract-review` — general commercial contract review against an organizational playbook
- `legalcode-nda-triage` — confidentiality / NDA review before licensing discussions
- `legalcode-patent-landscape-analysis` — FTO, landscape, and validity assessment
- `legalcode-copyright-infringement-assessment` — copyright infringement risk analysis
- `legalcode-trade-secret-audit` — trade secret protection program audit

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The license's governing law clause determines which
legal framework applies. The review identifies the governing law early and adapts the
analysis accordingly.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- Patent exhaustion doctrine (US: _Quanta_, _Impression Products_; EU: EEA-wide exhaustion;
  UK post-Brexit: UK domestic exhaustion — asymmetric with EEA)
- Post-expiration royalty prohibition (US: _Brulotte_/_Kimble_ — per se unlawful; EU/UK:
  know-how royalties may survive if properly structured)
- Copyright formalities (US: written instrument required for exclusive license, 17 U.S.C.
  §204; EU/UK: varies by member state)
- Copyright termination rights (US: §203, 35-year inalienable termination right post-1978)
- Trademark quality control requirements (US: Lanham Act — naked licensing = abandonment;
  EU/UK: similar quality control obligations; international: recordation requirements)
- Insolvency protections for licensees (US: §365(n) — patents, copyright, trade secrets,
  NOT trademarks; EU/UK: no statutory equivalent — contractual protections essential)
- Competition law safe harbors (EU: TTBER Regulation 316/2014, expiring 30 April 2026;
  new TTBER draft published September 2025, covering data licensing; US: DOJ/FTC 2017
  IP Licensing Guidelines — rule of reason for most restrictions)
- Moral rights (EU/UK civil and mixed jurisdictions: often inalienable; US: VARA, limited)
- Trademark license recordation (EU, UK, China, Korea, Brazil, others: recordation required
  for third-party enforceability)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- The IP category determines which category-specific issues apply
- Multiple valid approaches exist and the user's preference matters
- Risk tolerance or business context is needed to classify severity correctly
- Ambiguity in the license creates a fork that only the user can resolve

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

### Step 1: Accept the Agreement

Accept the license agreement in any of these formats:

- **File**: PDF, DOCX, or other document format
- **URL**: Link to an agreement in a CLM system, cloud storage, or document repository
- **Pasted text**: Agreement text pasted directly into the conversation
- **Summary**: User-provided summary of key terms (flag that analysis is limited)

If no agreement is provided, prompt the user to supply one.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask the user these questions. Present them
as structured options where possible:

1. **Which side are you on?**
   - Options: Licensor (granting rights), Licensee (receiving rights), Neutral / Both sides
   - _Why this matters_: The analysis flips depending on the party — what protects a licensor
     harms a licensee and vice versa (e.g., strong quality control benefits licensor/trademark
     owner but burdens licensee).

2. **What type(s) of IP are licensed?** (Select all that apply)
   - Options: Patents, Trademarks/Service marks, Copyright/Works of authorship,
     Trade secrets, Know-how (non-patent technical information), Software (may be copyright
     - trade secret + patents), Mixed-IP bundle, Unclear — help me identify
   - _Why this matters_: Each IP type has category-specific issues (e.g., Brulotte post-
     expiration prohibition for patents; quality control mandatory for trademarks; written
     instrument for exclusive copyright license; Lanham Act abandonment risk).

3. **Exclusivity and deal structure**
   - Options: Exclusive license (licensee only), Sole license (licensor retains own rights),
     Non-exclusive license (multiple licensees permitted), Cross-license / bilateral exchange,
     Sublicense only (licensee is itself a sublicensee), Unknown
   - _Why this matters_: Exclusivity level drives priority of grant-scope, market-share
     analysis, and diligence obligations.

4. **What are the relevant jurisdictions?** (governing law + where business will be conducted)
   - Options: United States (specify state), European Union (specify member states), United
     Kingdom, Multiple / international, Other (specify), Unknown / no governing law clause
   - _Why this matters_: Determines which exhaustion doctrine, competition law framework,
     and insolvency protection applies.

5. **Deal context and focus areas**
   - Free text for deal size, industry, strategic importance, known concerns.
   - Prompt: "Deal size? Industry (pharma, software, consumer goods, entertainment, manufacturing)?
     Known red flags? Any specific clauses you are most concerned about?"
   - _Why this matters_: A university research license gets different treatment than a $500M
     pharma commercialization deal or a global trademark franchise.

6. **Deadline**: When does this need to be finalized?
   - Options: Urgent (days), Standard (1–2 weeks), Flexible (no hard deadline)
   - _Why this matters_: Affects whether to surface all issues vs. focus on critical ones.

If the user provides partial context, proceed with what you have and **state assumptions
explicitly**. Do not silently assume.

### Step 3: Load the Playbook

Check for the organization's IP licensing playbook in local settings.

The playbook should define:

- Standard positions for each clause type (e.g., preferred royalty rate ranges, audit
  frequency, minimum royalty structure, grant-back posture)
- Acceptable ranges (terms that can be agreed without escalation)
- Escalation triggers (terms requiring senior IP counsel or decision-maker sign-off)
- IP-category-specific positions (e.g., no naked trademark licensing, always escrow for
  software, §365(n) reference required for US patent/copyright licenses)

**If no playbook is configured:**

**⟁ CLARIFY** — Inform the user that no playbook was found, and ask:

- **Option A: Set up a playbook now** — Walk through defining standard positions for key
  IP licensing clauses (exclusivity scope, royalty structure, audit rights, grant-back posture,
  insolvency protection requirements, quality control standards). Takes time upfront but
  makes this and all future reviews more precise.
- **Option B: Proceed with general IP licensing market standards** — Use widely-accepted
  market standards as the baseline. Faster, but the review may not reflect the organization's
  specific risk profile or negotiation history.
- **Option C: Provide positions as we go** — Start the review and ask about preferred
  positions when they become material for each clause.

Label the review clearly: "Based on general IP licensing market standards — not organizational positions."

### Step 4: Run the IP Category Pre-Screen

Before clause-by-clause analysis, identify IP-category-specific issues that must be
checked regardless of the party's position. These checks are non-negotiable; missing any
one can render the license legally defective or commercially unenforceable.

#### 4a. Patent Licenses — Mandatory Pre-Screen

| Check                     | Issue                                                                     | Severity if Failed                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Post-expiration royalties | Are royalties payable on sales after patent expiry?                       | CRITICAL — _Brulotte_/_Kimble_ per se unlawful in US                                                                         |
| Patent schedule           | Are licensed patents identified by number, family, and national variants? | RED — vague grant creates scope disputes                                                                                     |
| Patent prosecution clause | Who controls prosecution/maintenance? What if licensor abandons?          | RED — licensor abandonment can eliminate licensed rights                                                                     |
| Non-challenge clause      | Can licensee challenge patent validity? What is the consequence?          | YELLOW — EU TTBER Art. 5 excludes termination-on-challenge from block exemption                                              |
| Patent exhaustion         | Are "no-exhaustion" clauses included?                                     | RED — unenforceable through patent law post-_Impression Products_ [VERIFY jurisdiction]                                      |
| Joint ownership           | Is the licensed IP jointly owned?                                         | YELLOW — joint owners in US may each license independently without consent (35 U.S.C. §262); EU/UK require unanimous consent |

#### 4b. Trademark Licenses — Mandatory Pre-Screen

| Check                         | Issue                                                                                  | Severity if Failed                                                                          |
| ----------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Quality control provisions    | Are detailed quality control provisions included AND actually exercised?               | CRITICAL — naked licensing = trademark abandonment (Lanham Act §1127)                       |
| Registered user / recordation | Has the license been (or will it be) recorded with relevant trademark registries?      | RED — many jurisdictions (EU, UK, China) require recordation for third-party enforceability |
| Goodwill inurement            | Does all goodwill from licensee's use inure to licensor's benefit?                     | RED — absent clause risks trademark abandonment argument                                    |
| Assignment in gross           | Is the trademark being assigned without associated goodwill?                           | CRITICAL — assignment in gross = abandonment                                                |
| Geographic scope              | Does the license scope match trademark registration coverage?                          | RED — unlicensed territory use is infringement                                              |
| Bankruptcy / §365(n) gap      | Trademark licenses are NOT protected by §365(n) — what contractual alternatives exist? | RED — trademark licensees need express contractual protection                               |

#### 4c. Copyright Licenses — Mandatory Pre-Screen

| Check                          | Issue                                                                          | Severity if Failed                                                                               |
| ------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| Written instrument (exclusive) | Is an exclusive copyright license in a signed writing?                         | CRITICAL — 17 U.S.C. §204 requirement; unenforceable if missing                                  |
| §203 termination exposure      | Is the license a post-1978 grant that could be terminated in 35 years?         | RED — non-waivable statutory right; affects copyright licenses for music, literary works, film   |
| Moral rights waiver            | Are moral rights addressed in the license?                                     | YELLOW/RED — moral rights inalienable in many EU/UK jurisdictions; US VARA applies to visual art |
| AI training data               | Does the license address AI training use of copyrighted works?                 | YELLOW — significant legal uncertainty 2024–2025; opt-in/opt-out language recommended            |
| Termination of transfer        | For music/entertainment: does the license address §203 reversion risk?         | RED — particularly material for pre-2013 grants                                                  |
| Works for hire boundary        | Has a contractor incorrectly been labelled as creating a "work made for hire"? | RED — work for hire must fit §101 categories; otherwise author retains termination rights        |

#### 4d. Trade Secret Licenses — Mandatory Pre-Screen

| Check                           | Issue                                                                                                            | Severity if Failed                                                        |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Confidentiality as the license  | Is the confidentiality provision strong enough to maintain trade secret status?                                  | CRITICAL — inadequate confidentiality destroys trade secret protection    |
| Post-termination survival       | Do trade secret obligations survive termination of the license?                                                  | RED — termination of license ≠ disclosure right                           |
| Reasonable measures obligations | Is licensee required to maintain reasonable measures to protect secrecy?                                         | RED — DTSA/UTSA protection requires owner to maintain reasonable measures |
| Public domain risk              | What happens if the trade secret enters the public domain?                                                       | YELLOW — license should address whether royalties survive loss of secrecy |
| DTSA whistleblower notice       | Does the license include required DTSA §1833(b) whistleblower immunity notice in any employment-related context? | YELLOW — failure forfeits exemplary damages and attorney's fees           |

#### 4e. Know-How Licenses — Mandatory Pre-Screen

| Check                        | Issue                                                                          | Severity if Failed                                                                                         |
| ---------------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| Brulotte bundling risk       | Is know-how bundled with patents in a way that extends effective royalty term? | RED — royalties for mixed patent/know-how licenses must be apportioned to avoid _Brulotte_ violation in US |
| Post-public-domain royalties | Are know-how royalties payable after the know-how enters the public domain?    | YELLOW — reduces leverage; may be unenforceable depending on jurisdiction                                  |
| Duration and TTBER           | Does a know-how license extend beyond the period of secrecy?                   | YELLOW — EU TTBER: know-how license must not extend beyond period when information remains secret          |

### Step 5: Gather Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** to build a working legal reference file for this review. Research:

1. **Governing law jurisdiction**: Identify the applicable jurisdiction from the governing
   law clause.

   **⟁ CLARIFY** — If any of the following are true, ask before proceeding:
   - **No governing law clause found**: Ask which jurisdiction the user expects to apply,
     and flag the absence as a RED deviation.
   - **Multiple governing laws** (e.g., different schedules reference different laws): Ask
     which governs the main license body and note the conflict.
   - **Unusual governing law** for the IP or business relationship: Confirm the user is
     aware and ask whether to analyze under the stated law or flag as an issue.

2. **Search legalcode-mcp** for jurisdiction-relevant authority:
   - Patent exhaustion statutes and leading cases (US: _Quanta_, _Impression Products_;
     EU: _Merck v. Primecrown_; UK post-Brexit regime)
   - Post-expiration royalty prohibition (US: _Brulotte v. Thys_, _Kimble v. Marvel_)
   - Copyright exclusive license formalities (17 U.S.C. §204; CDPA s.90; equivalent)
   - Copyright termination rights (17 U.S.C. §203)
   - Trademark quality control requirements (Lanham Act §1055, §1127; equivalent)
   - TTBER safe harbor thresholds and hardcore restrictions (if EU is relevant jurisdiction)
   - Licensor insolvency protections (11 U.S.C. §365(n) and trademark gap; Insolvency Act
     1986 for UK; EU Restructuring Directive 2019/1023)
   - Competition law for grant-back and territory restrictions (DOJ/FTC 2017 Guidelines;
     TTBER Art. 4 hardcore restrictions, Art. 5 excluded restrictions)

3. **Save results** to a local temporary reference file at `/tmp/legalcode-license-review-authority.md`.

**If legalcode-mcp is not connected:**

- Mark every statutory and case law reference with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with general knowledge but flag that legal authority has not been verified

### Step 6: Clause-by-Clause Analysis

Analyze the agreement systematically. **Read the entire agreement before flagging any
issues** — licensing clauses interact heavily (e.g., a broad sublicensing grant interacts
with royalty audit rights; field-of-use limits interact with improvement grant-back scope;
royalty caps interact with indemnity caps).

**⟁ CLARIFY** — For long or complex agreements (50+ pages, or with multiple schedules,
exhibits, or side letters):

- Ask whether to perform a **full review** of all 14 clause categories, or a **priority
  review** focused on the categories the user is most concerned about.
- If the agreement incorporates external documents (e.g., "Subject to Licensor's Standard
  Licensing Terms at [URL]"), ask whether to review those incorporated documents as well.

Cover all 14 clause categories below. For each, assess against the playbook (or general
market standards) and note whether the clause is present, absent, or unusual.

| #   | Clause Category                          | Depth    | IP-Specific Key Review Points                                                                          |
| --- | ---------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------ |
| 1   | Grant Scope and Field of Use             | Deep     | Exclusivity, FOU definition, territory, permitted acts, sublicensing right, future IP inclusion        |
| 2   | Royalty Structure and Financial Terms    | Deep     | Royalty base, deductions, Brulotte risk, SSPPU/EMVR, MFN/MFL, minimum royalties, milestones            |
| 3   | Sublicensing Rights and Flow-Down        | Deep     | Permission scope, mandatory flow-downs, sublicensee audit, sublicense survival on termination          |
| 4   | IP Indemnification and Warranties        | Deep     | Ownership warranties, FTO/quiet enjoyment, remedy waterfall, caps, carve-outs, defense obligations     |
| 5   | Royalty Audit Rights                     | Deep     | Frequency, auditor qualifications, sublicensee reach, records retention, underpayment threshold        |
| 6   | Improvement and Grant-Back Provisions    | Deep     | Type (assignment/exclusive/non-exclusive), antitrust screening, "Improvement" definition, compensation |
| 7   | Termination and Wind-Down                | Deep     | Termination triggers, cure periods, post-termination rights, sell-off period, survival obligations     |
| 8   | Licensor Insolvency Protections          | Deep     | §365(n) reference, trademark gap, IP escrow, direct covenant, EU/UK contractual alternatives           |
| 9   | IP Embodiment / Source Code Escrow       | Deep     | Trigger events, verification level, release license scope, SaaS/RaaS alternatives                      |
| 10  | Confidentiality and Trade Secrets        | Standard | Scope, duration (indefinite for TS), licensee obligations, sublicensee flow-down                       |
| 11  | Representations, Warranties, Disclaimers | Standard | IP ownership, authority, non-infringement, disclaimer scope, survival period                           |
| 12  | Assignment and Change of Control         | Standard | Consent requirements, change-of-control, affiliate exceptions, competitor acquisition                  |
| 13  | Governing Law and Dispute Resolution     | Standard | Jurisdiction, arbitration vs. litigation, escalation, IP-specific dispute resolution                   |
| 14  | Compliance, Regulatory, and Boilerplate  | Standard | Export controls (ITAR/EAR), anti-bribery, data protection, entire agreement, order of precedence       |

### Step 7: Missing Clause Detection

After analyzing clauses that are present, check for important clauses that are entirely
absent. In IP licensing, a missing clause can be more dangerous than a problematic one.

For each of the 14 categories:

- If absent, flag it with the appropriate severity
- Assess whether the absence is acceptable (e.g., no escrow for a short-term know-how
  license may be fine) or material

Common missing clause issues specific to IP licensing:

- No royalty audit rights (RED — common in early-stage deals by unsophisticated licensors)
- No sublicense survival clause (RED — sublicensees unprotected if head license terminates)
- No §365(n) reference in US patent/copyright license (RED — reduces insolvency protection)
- No quality control provisions in trademark license (CRITICAL — naked licensing risk)
- No IP escrow for software license from single-source vendor (RED)
- No cure period before termination for breach (RED — immediate termination is disproportionate)
- No post-termination sell-off period for physical goods (YELLOW)
- No definition of "Improvement" (YELLOW — grant-back scope is undefined)
- No diligence/commercialization obligation in exclusive license (RED — licensee can "shelf" the IP)
- Missing §203 risk allocation clause in copyright license (YELLOW — for post-1978 grants)

**⟁ CLARIFY** — When severity of a missing clause depends on business context:

- "This license has no royalty audit rights. Is royalty tracking a material issue for
  this deal? Absent audit rights, underpayment cannot be verified."
- "There is no §365(n) reference clause. Is the licensor a startup or financially
  distressed company? If so, this is a RED gap for a US patent or copyright license."
- "There is no diligence obligation on the exclusive licensee. Does the licensor care
  whether the IP is actively commercialized, or is the revenue stream alone sufficient?"

### Step 8: Flag Deviations

Classify each deviation from the playbook using the four-tier system defined in the
**Deviation Severity Classification** section below. For each deviation:

- **GREEN**: Note for awareness.
- **YELLOW**: Generate specific redline language, provide fallback position, and estimate
  business impact of accepting vs. negotiating.
- **RED**: Explain the specific risk (citing the legal basis where possible), provide
  market-standard alternative language, estimate exposure, and recommend escalation.
- **CRITICAL**: Flag immediately. These are legally defective or antitrust-violating
  provisions requiring immediate attention regardless of the organization's risk appetite.

**⟁ CLARIFY** — For borderline classifications, ask rather than assume:

- **YELLOW vs. RED**: "This grant-back provision requires the licensee to assign all
  improvements — which is typically RED from a licensee perspective. Is your organization
  willing to accept this, or should I treat it as a must-fix?"
- **YELLOW vs. CRITICAL**: "This trademark license contains no quality control provisions.
  This is a CRITICAL issue under US Lanham Act (naked licensing = abandonment), but may
  have less immediate consequence in jurisdictions where quality control obligations are
  implied. Should I treat it as CRITICAL?"

### Step 9: Generate Redlines

**⟁ CLARIFY** — Before generating redlines, ask about negotiation posture if not clear:

- **Relationship dynamic**: New counterparty vs. established partner vs. must-have licensor?
  Tone of redlines should match the commercial relationship.
- **Volume of redlines**: If many YELLOW items exist, ask: "I found [N] issues worth
  negotiating. Do you want redlines for all, or focus on the top [X] most impactful?"

For each YELLOW and RED deviation, generate a redline using the **Redline Format** below.

### Step 10: Licensing Clause Interaction Analysis

After individual clause analysis, assess material clause interactions. These compound risks
can be worse than any single clause in isolation.

**Key interaction pairs to assess:**

| Interaction                                   | Risk                                                                                                                                 |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Royalty cap + IP indemnity cap                | If indemnity is subject to the general liability cap, the licensor's IP warranty is effectively hollow for large infringement claims |
| Field of use + sublicensing rights            | Licensee sublicenses within FOU but sublicensee uses outside FOU — who is liable?                                                    |
| Exclusivity + diligence obligation            | No diligence obligation in exclusive license = licensor locked out while licensee "shelves" IP                                       |
| Grant-back + FOU                              | Is the grant-back limited to the licensed FOU? Or does licensor get improvements across all fields?                                  |
| Termination + sublicense survival             | Head license terminates → sublicenses terminate → downstream partners lose rights                                                    |
| Post-expiration royalties + know-how bundling | Patent/know-how bundle without apportionment = _Brulotte_ violation for the patent component                                         |
| §365(n) scope + trademark                     | Licensor's IP includes both patents and trademark → licensee has §365(n) protection for patents but NOT trademark                    |
| Audit rights + sublicensee reach              | Licensor has audit rights over licensee but not sublicensees → royalty accuracy unverifiable                                         |
| MFN + exclusivity                             | MFN requires licensor to match all future licensees' terms → may prevent licensor from granting exclusive license at all             |

### Step 11: Business Impact Summary

Provide a summary covering:

- **Overall risk assessment**: High-level view of the license's risk profile
- **CRITICAL / RED items**: Issues that must be addressed before signing
- **Top 5 issues**: Most important items to address, with severity and priority
- **Negotiation strategy**: Which issues to lead with, what to concede, how to sequence
- **IP category-specific alerts**: Category-specific risks identified in the Pre-Screen (Step 4)
- **Clause interaction alerts**: Material compound risks identified in Step 10

**⟁ CLARIFY** — If deal context is unclear and it would materially affect negotiation strategy:

- **Walk-away option**: Is this an essential licensor/technology with no alternatives?
- **IP criticality**: Is the licensed IP core to the licensee's business or peripheral?
- **Exclusivity importance**: Would losing exclusivity materially harm the licensee's
  competitive position?

### Step 12: Quality Verification

Before delivering the analysis:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every CRITICAL or RED item, run the 3-pass Self-Interrogation.
3. Assign a Confidence Score to each material clause analysis.
4. Verify completeness: confirm all 14 clause categories have been addressed.
5. Verify the IP Category Pre-Screen findings have been integrated.
6. Verify clause interactions have been assessed (Step 10).
7. Generate the Glass Box Audit Trail and append to the output.

---

## Clause Analysis Reference

### 1. Grant Scope and Field of Use

**Key elements to review:**

- Is the IP bundle precisely identified? (Patents by number and national filing; copyright by
  specific works or by category with future works provision; trademarks by registration
  number; trade secrets by reference to Schedule)
- Exclusivity level: exclusive, sole, or non-exclusive? Is it defined clearly?
  - **Exclusive**: Only licensee may exercise rights in the FOU/territory
  - **Sole**: Licensee and licensor may both exercise rights; no further licensees
  - **Non-exclusive**: Multiple licensees permitted
- Field of use: specifically defined? Objective and binary (not open to interpretation)?
  Industry-standard terminology used?
- Territory: by country, by region, worldwide? Are any countries excluded?
- Permitted acts: what specifically may the licensee do? (Make, use, sell, import, offer
  for sale, reproduce, distribute, publicly perform, display, sublicense, have made)
- "Have made" rights: Licensee can instruct third-party manufacturers to make product
  embodying the licensed IP — significant right; present? Appropriately scoped?
- Future IP: Does the license automatically capture future improvements, continuation
  patents, or registered trademark variants? Should it?
- Background IP vs. Foreground IP: Is pre-existing IP clearly delineated from IP
  developed under the license?

**Common issues:**

- Grant clause so vague that its scope is disputed ("use the technology")
- FOU defined in subjective terms ("as licensor deems appropriate")
- Automatic inclusion of future IP without narrowing to related patents or improvements
- Licensed patents identified only by patent family head — national filings may differ
- "Have made" rights granted when licensor is a sole-source manufacturer

[JURISDICTION-SPECIFIC] Key variations:

- **US**: Joint ownership — either co-owner may license independently without the other's
  consent and without accounting (35 U.S.C. §262); very different from EU/UK [VERIFY]
- **EU/UK**: Joint IP ownership requires unanimous consent to license; co-owner cannot
  grant licenses unilaterally (unless agreed otherwise) [VERIFY]
- **EU TTBER**: Exclusive license between competitors in the same FOU/territory is a
  TTBER-sensitive arrangement requiring market share analysis [VERIFY]

**Severity indicators:**
| Finding | Severity |
|---------|----------|
| Grant clause does not identify licensed IP by reference to a Schedule | RED |
| "Have made" rights granted to a competitor of the licensor | RED |
| FOU defined in subjective terms open to licensor's unilateral reinterpretation | RED |
| Future improvements automatically captured without termination right | YELLOW |
| Exclusivity scope broader than the licensee's actual business | YELLOW |
| Parallel import restrictions inconsistent with exhaustion doctrine | RED [VERIFY jurisdiction] |

---

### 2. Royalty Structure and Financial Terms

**Key elements to review:**

**Running royalties:**

- Royalty base: Is "Net Sales" defined? What deductions are permitted?
  Standard permissible deductions: actual trade discounts, freight, taxes, returns/allowances
  Non-permissible deductions: internal transfer pricing, R&D cost offsets, management charges
- SSPPU vs. EMVR: For patent licenses, is the royalty base the smallest saleable unit
  practicing the licensed patent, or the entire product value?
  - EMVR only justified where the licensed feature drives demand for the entire product
  - _Cornell v. Hewlett-Packard_, _Ericsson v. D-Link_ establish SSPPU preference [VERIFY]
- Tiered royalties: escalating or de-escalating at volume breakpoints?
- Post-expiration royalties: do royalties cease on patent expiration? _Brulotte v. Thys_ (1964),
  _Kimble v. Marvel_ (2015) — per se unlawful in US to require royalties on post-expiration sales
- Mixed patent/know-how bundle: are royalties apportioned between patent and non-patent
  components to avoid _Brulotte_ violation?

**Milestone payments:**

- Are milestones objectively and binary defined? (IND filing, Phase II completion, first
  commercial sale — not "satisfactory completion" or "licensor approval")
- Is payment timing specified after milestone achievement?
- What happens if a milestone is delayed through no licensee fault?

**Minimum royalties (MARs):**

- Is a minimum annual royalty included? (Critical for licensor in exclusive licenses)
- What is the consequence of failure to meet minimums: conversion to non-exclusive or
  termination right?
- Is the MAR structure a step-up schedule (increasing over time)?

**Most-Favored-Nation / Most-Favored-Licensee (MFN/MFL):**

- If MFN is included: what is its scope? All terms? Royalty rate only?
- What carve-outs exist? Standard carve-outs: settlement licenses, government/compulsory
  licenses, cross-licenses, licenses with materially different scope/FOU/territory,
  licenses pre-dating the MFN clause
- Does the MFN have an expiration date?
- Is adjustment automatic or triggered by notice?

**Royalty stacking:**

- Is the licensed IP a component of a product that requires multiple licenses from
  different parties?
- Is a royalty stacking relief clause included?

**Common issues:**

- Royalty base includes gross revenue without itemized permitted deductions
- No SSPPU analysis — EMVR applied to a patent covering one minor product feature
- No minimum royalties in an exclusive license (licensee can "shelf" the IP)
- Post-expiration patent royalty obligation (US: per se unlawful)
- MFN without scope limitation — licensor locked out of any flexibility in future deals
- Milestone definitions with subjective triggers ("to licensor's satisfaction")

**Severity indicators:**
| Finding | Severity |
|---------|----------|
| Royalties payable on sales after all licensed patents expire (US) | CRITICAL |
| Mixed patent/know-how license with no royalty apportionment | RED |
| No minimum royalties in exclusive license with no diligence obligation | RED |
| Royalty base broader than net sales from licensed products | RED |
| MFN with no carve-outs and no expiration | YELLOW |
| Milestone definitions with subjective triggers | YELLOW |
| No royalty stacking clause in high-SEP-exposure technology area | YELLOW |

---

### 3. Sublicensing Rights and Flow-Down

**Key elements to review:**

- Is sublicensing permitted? (No implied sublicensing right — requires express authorization)
- Scope of sublicensing permission:
  - Blanket approval for any sublicensee?
  - Approval required (written consent, not to be unreasonably withheld)?
  - Permitted only for specified affiliates?
  - Negative consent (licensor has right to object within defined period)?

**Mandatory flow-down provisions:**
The following must flow down to all sublicenses:

- FOU and territorial restrictions (sublicensee cannot exceed head license scope)
- Licensor's reserved rights
- Audit rights (direct licensor audit of sublicensee OR flow-down obligation requiring
  licensee to audit sublicensees and share results with licensor)
- Confidentiality obligations (at least as restrictive as head license)
- IP ownership and non-challenge of licensor's IP
- Trademark quality control requirements (if applicable)
- Prohibition on further sublicensing (unless specifically permitted)
- Diligence/reporting obligations
- Governing law and dispute resolution (or consistent alternative)

**Sublicense survival on termination:**

- Default rule: sublicenses terminate automatically when head license terminates
- Express exception: head license can provide that sublicenses survive termination and
  become direct licenses between licensor and sublicensee (_Speedplay v. Bebop_ doctrine)
- Without a survival clause, sublicensees lose rights if licensor-licensee dispute
  terminates the head license — even through no fault of the sublicensee

**Sublicense royalty pass-through:**

- Is licensee accountable to licensor for sublicensee royalties?
- What percentage of sublicensee-paid royalties passes through to licensor?
- Is there a minimum sublicense royalty rate (preventing licensee from granting sweetheart
  sublicenses to affiliates)?

**Severity indicators:**
| Finding | Severity |
|---------|----------|
| No sublicense survival clause — downstream partners lose rights on licensor-licensee dispute | RED |
| Sublicensing permitted with no flow-down of audit rights | RED |
| No minimum sublicense royalty — licensee can grant zero-royalty sublicenses to affiliates | RED |
| Sublicensee not bound by FOU/territory limits of head license | RED |
| Sublicensing broadly permitted with no licensor consent or notification | YELLOW (licensor perspective) |
| No prohibition on further sub-sublicensing | YELLOW |

---

### 4. IP Indemnification and Warranties

**Key elements to review:**

**Licensor representations and warranties (review completeness):**

- **Ownership / chain of title**: Licensor solely and exclusively owns (or has right to
  sublicense) all licensed IP; no liens, encumbrances, or adverse claims
- **Validity**: Licensed patents are valid and enforceable (often knowledge-qualified:
  "to licensor's knowledge, no pending invalidity proceedings")
- **Non-infringement / FTO**: Licensed IP does not, to licensor's knowledge, infringe
  any third-party IP rights
- **Quiet enjoyment**: Licensee's exercise of licensed rights within scope will not be
  disturbed by licensor or any party claiming through licensor
- **Authority**: Licensor has full corporate authority to enter and perform
- **No conflicting licenses**: No existing licenses inconsistent with the exclusivity granted
- **No encumbrances**: Licensed IP is free of liens, security interests, and encumbrances

**Infringement indemnification — remedy waterfall:**
When a third-party infringement claim is asserted against the licensee:

1. Licensor **defends** the claim at licensor's expense
2. Licensor **modifies** the licensed IP to make it non-infringing (maintaining substantially
   equivalent functionality)
3. Licensor **replaces** the licensed IP with a non-infringing equivalent
4. Licensor **obtains** a license from the third party on licensee's behalf
5. Licensor **refunds** fees paid and **terminates** if none of the above is feasible
   (Note: Steps 2–4 may be in any order; Step 5 should be a last resort only)

**Standard indemnification carve-outs (licensor exclusions):**
Infringement claims arising from:

- Licensee's modifications to the licensed IP (not authorized by licensor)
- Combination of licensed IP with third-party products/services not recommended by licensor
  (where the infringement arises from the combination, not the licensed IP alone)
- Licensee's use outside the licensed FOU, territory, or permitted scope
- Failure to use licensor-provided updates/corrections that would have resolved the infringement
- Use in compliance with licensee's own specifications or instructions

**Liability caps:**

- Is IP indemnification subject to the general liability cap?
- If yes: a cap at 12 months of fees may be grossly inadequate for a $100M infringement claim
- Preferred structure: IP indemnification either uncapped or subject to a separate, higher "super-cap"
- Is the consequential damages exclusion carved out for IP indemnification?

**Common issues:**

- IP indemnification capped at general liability cap (inadequate for core IP obligation)
- Missing remedy waterfall — only obligation is to "notify" licensor (no defense duty)
- Combination carve-out drafted so broadly it excludes virtually all real-world integration
- No mutual indemnification — licensor only indemnifies, licensee has no reciprocal obligation
- No right to control defense (licensor might accept unfavorable settlement binding licensee)

**Severity indicators:**
| Finding | Severity |
|---------|----------|
| No IP indemnification in license of commercial IP | RED |
| IP indemnification capped at 3 months of fees or less | RED |
| Combination carve-out excludes standard integrations reasonably anticipated by licensor | RED |
| No duty to defend — only indemnification for losses after the fact | YELLOW |
| No sole remedy clause — licensee can pursue both indemnification and breach of warranty claims | GREEN (licensee perspective) |
| Licensor IP warranty knowledge-qualified ("to licensor's best knowledge only") | YELLOW |

---

### 5. Royalty Audit Rights

**Key elements to review:**

- **Scope**: What records are auditable? (Net sales calculations, permitted deductions,
  sublicensee royalty reports, cost deductions, currency conversion)
- **Frequency**: Maximum once per year? Twice if significant underpayment found?
- **Notice period**: Typically 30 days' advance written notice
- **Qualified auditor**: Independent CPA or chartered accountant, bound by confidentiality
- **Business hours and location**: At licensee's principal place of business during normal hours
- **Records retention**: Minimum period licensee must retain royalty records (typically 3–5 years
  after the relevant royalty period; not shorter than applicable limitations period)
- **Underpayment threshold**: If underpayment exceeds X% (typically 5–10%), licensee pays
  audit costs; below threshold, licensor pays
- **Overpayment**: Credited against future royalties or refunded within 30 days
- **Underpayment interest**: Defined interest rate on underpaid royalties (e.g., prime + 2%,
  or SOFR + defined spread)
- **Dispute resolution for audit findings**: Management escalation → independent accountant
  determination → arbitration

**Sublicensee audit rights:**

- Does licensor have direct audit rights over sublicensees? OR
- Is licensee required to flow down equivalent audit rights to sublicensees and enforce/
  share results with licensor? (Flow-down audit is the minimum; direct audit rights are preferable)

**Common issues:**

- No audit rights at all (common in early-stage deals)
- Audit rights that cover net sales but not gross-to-net deductions
- No sublicensee audit rights — royalty accuracy of sublicensees unverifiable
- Records retention period shorter than applicable statute of limitations
- No underpayment interest clause — no disincentive for delayed payment
- No dispute resolution process for disagreements over audit findings

**Severity indicators:**
| Finding | Severity |
|---------|----------|
| No audit rights in a running royalty license | RED |
| Audit rights do not reach sublicensees (no direct or flow-down rights) | RED |
| Records retention period shorter than 3 years | RED |
| Audit frequency limited to once every 3+ years | YELLOW |
| No underpayment interest rate defined | YELLOW |
| Audit costs always paid by licensor regardless of underpayment | YELLOW |

---

### 6. Improvement and Grant-Back Provisions

**Key elements to review:**

**Type of grant-back:**
| Type | Description | Antitrust Risk |
|------|-------------|----------------|
| Non-exclusive grant-back | Licensee grants licensor non-exclusive license to improvements; licensee retains all rights | LOW — generally permissible (US rule of reason; EU TTBER safe harbor if non-exclusive) |
| Exclusive grant-back | Licensee must exclusively license improvements to licensor | HIGH — EU TTBER Art. 5(1)(b): excluded restriction for severable improvements; US: heightened rule of reason scrutiny |
| Assignment of improvements | Licensee must transfer full ownership of improvements | CRITICAL — treated same as exclusive grant-back; very high antitrust risk; destroys licensee's innovation incentive |
| Reach-through royalties | Licensor receives royalties on products derived from improvements | HIGH — NIH discourages for research tools; problematic in US and EU |

**Definition of "Improvement":**

- Is "Improvement" defined precisely? (Overly broad definition can capture the licensee's
  independent innovations having no real relation to the licensed IP)
- Does it capture only modifications that require a license to the original licensed patents
  to practice? (Preferred definition — avoids over-capture)
- Are jointly developed improvements addressed separately?

**Compensation for exclusive or assignment grant-backs:**

- Is there compensation to the licensee for the value surrendered (exclusive grant-back or
  assignment)?
- Cross-license: does licensor grant back equivalent rights to the improvement?

**EU TTBER analysis (if applicable):**

- TTBER Art. 5(1)(b): Exclusive grant-back of **severable** improvements is an excluded
  restriction — cannot benefit from block exemption regardless of market shares [VERIFY currency]
- Non-exclusive grant-back of severable improvements: generally within TTBER safe harbor
- "Severable" = independently exploitable without the licensed technology

**Common issues:**

- Mandatory assignment of all improvements to licensor (destroys licensee innovation incentive)
- "Improvement" defined so broadly it captures unrelated independent R&D
- No compensation for exclusive or assignment grant-backs
- No licensor obligation to cross-license improvements back to licensee
- Exclusive grant-back in EU-governed license (TTBER excluded restriction)

**Severity indicators:**
| Finding | Severity |
|---------|----------|
| Mandatory assignment of all improvements to licensor | CRITICAL (licensee) / RED |
| Exclusive grant-back of severable improvements in EU-governed license | CRITICAL — TTBER Art. 5(1)(b) excluded restriction |
| "Improvement" defined to capture licensee's independent R&D | RED |
| No compensation for exclusive grant-back | RED |
| Non-exclusive grant-back with no cross-license to licensee | YELLOW |
| No definition of "Improvement" — scope undefined | YELLOW |

---

### 7. Termination and Wind-Down

**Key elements to review:**

- **Term**: Initial term, renewal terms, auto-renewal notice periods
- **Termination for cause**: What events trigger termination? Is there a cure period?
  - Material breach with [30–60 day] cure period: standard
  - Immediate termination for: insolvency, IP invalidity, IP challenge (check antitrust
    implications — EU TTBER excludes termination-on-challenge from block exemption)
- **Termination for convenience**: Available to either party? Notice period?
- **Post-termination rights**:
  - Licensed rights cease immediately (or after sell-off period)?
  - Sell-off period for physical goods: typically 30–90 days, with royalty accounting
  - Return or destruction of licensed materials, tangible embodiments, and confidential information
  - Which clauses survive termination? (Confidentiality, accrued royalties, audit rights for
    pre-termination period, indemnification)
- **Sublicense survival on termination**: Do sublicenses survive head license termination and
  convert to direct licenses with licensor? (See Clause 3 analysis)
- **Conversion rights on MAR failure**: If licensee fails to meet minimum annual royalties, does
  licensor have a right to convert exclusive to non-exclusive (preferred over termination)?

**Termination for IP invalidity:**

- If the licensed patents are declared invalid, does the license terminate automatically?
- Should royalties already paid be refunded?
- If the license covers multiple patents, what happens if only some are invalidated?

**Common issues:**

- Immediate termination for minor/technical breach without cure period
- No sell-off period — licensee cannot clear existing inventory bearing licensor's trademark
- Survival clause vaguely drafted — unclear which obligations continue
- No post-termination audit right for pre-termination royalty period
- Termination for IP challenge — may be antitrust-problematic (EU TTBER)

**Severity indicators:**
| Finding | Severity |
|---------|----------|
| Immediate termination for any breach without cure period | RED |
| No sublicense survival clause | RED — downstream sublicensees lose rights |
| No sell-off period for goods bearing licensed trademark | RED |
| Termination-on-challenge clause in EU-governed license (TTBER Art. 5) | RED — antitrust risk |
| Auto-renewal with notice window shorter than reasonable business planning period | YELLOW |
| Survival clause does not specifically identify surviving obligations | YELLOW |

---

### 8. Licensor Insolvency Protections

**Key elements to review:**

**US — §365(n) protection:**

- Does the license expressly reference 11 U.S.C. §365(n) and the licensee's right to elect
  to retain rights under the license in licensor bankruptcy?
- Are IP license fees clearly separated from fees for ancillary services? (If bundled, the
  licensee may lose IP rights when the service component is rejected)
- Is the licensed IP explicitly characterized as "intellectual property" within the meaning
  of 11 U.S.C. §101(35A)?
- Is a source code escrow in place as a "tangible embodiment" of the licensed IP?

**Trademark — §365(n) gap:**

- §365(n) does NOT cover trademarks (legislative gap; Congress deferred pending quality
  control study that was never completed)
- _Mission Products v. Tempnology_ (2019): Trademark license rejection = breach of contract,
  not rescission. Licensee retains whatever rights it had unless the license provides otherwise.
- Contractual protection: Express clause that licensor's obligations survive any insolvency
  proceeding; delegation of quality control to licensee in licensor's absence;
  step-in rights for licensee to maintain trademark quality post-rejection

**EU/UK — no statutory equivalent to §365(n):**

- No harmonized EU equivalent to §365(n)
- UK: Insolvency Act 1986 / CIGA 2020 — IP licenses treated as general executory contracts;
  administrator/liquidator has broad flexibility; no guaranteed licensee protection
- **Contractual alternatives** for EU/UK licensees:
  - Grant of usufruct rather than license (stronger property right in civil law jurisdictions)
  - Contractual option to purchase licensed IP if licensor enters insolvency
  - Right of first refusal on IP sale in insolvency
  - IP escrow arrangement
  - Step-in rights / direct license from parent IP-holding entity
  - Solvent parent guarantee of IP license obligations

**Common issues:**

- No §365(n) reference in US patent/copyright license from financially stressed licensor
- Trademark license with no contractual insolvency protection (no §365(n), no contractual alternative)
- IP fees and service fees bundled — licensee may lose IP rights when services are rejected
- No IP escrow for critical single-source software or other IP embodiments

**Severity indicators:**
| Finding | Severity |
|---------|----------|
| No §365(n) reference in US patent or copyright license (startup/distressed licensor) | RED |
| Trademark license with no insolvency protection (no §365(n), no contractual alternative) | RED |
| IP fees and service fees bundled without separation | RED |
| No IP escrow for critical single-source software | RED |
| No bankruptcy-remote IP holding entity structure for high-value exclusive license | YELLOW |

---

### 9. IP Embodiment / Source Code Escrow

**Key elements to review:**

- Is an escrow arrangement in place for software or other IP embodiments?
- **Trigger events**: What events release the escrow? Standard triggers:
  - Licensor voluntary insolvency filing
  - Involuntary insolvency filing not dismissed within 60–90 days
  - Licensor's cessation of active support obligations
  - Material breach of support/maintenance obligations uncured after notice period
  - Licensor's failure to deliver updates as required
- **Verification level**:
  - Level 1: Deposit existence only (no verification of content)
  - Level 2: Technical verification (materials compile and run basic tests)
  - Level 3: Full functional verification (materials produce the licensed functionality)
- **Escrow agent**: Reputable third-party escrow agent (e.g., NCC Group/Escode, IronMountain)
- **Content**: Source code, build instructions, third-party libraries and licenses, technical
  documentation, development environment specifications
- **Release license scope**: On release, is the licensee permitted to modify the source code?
  Sublicense for maintenance? Or only use for internal purposes?
- **SaaS alternatives**: For SaaS products, traditional escrow is insufficient (code alone
  does not produce the service). Alternatives:
  - Recovery-as-a-Service (RaaS): Licensor and licensee test a recovery scenario regularly
  - Operational runbooks in escrow
  - Cloud provider direct agreements (AWS/Azure/GCP step-in rights)
  - Data portability provisions: licensee's data exportable in standard format
- **Update obligations**: Is licensor required to update the escrow with each new release?
  How frequently?

**Severity indicators:**
| Finding | Severity |
|---------|----------|
| No escrow for critical single-source software license | RED |
| Trigger events exclude licensor voluntary insolvency | RED |
| Level 1 verification only (no testing of deposited materials) | YELLOW |
| Release license does not permit licensee to modify code for emergency use | YELLOW |
| SaaS license with no data portability or RaaS provisions | YELLOW |
| No update obligation — escrow may contain outdated version | YELLOW |

---

### 10–14. Standard Clause Checklist

For the following clause categories, review presence, reasonableness, and alignment with
the playbook. Flag deviations using the same four-tier system.

**10. Confidentiality and Trade Secrets**

- [ ] Scope of confidential information defined and reasonable
- [ ] Duration appropriate: trade secrets — indefinite; other confidential information —
      typically 5–7 years in IP licensing context (longer than general commercial contracts)
- [ ] Standard carveouts present (public domain, independent development, required by law)
- [ ] Licensee required to use measures at least as protective as its own confidential information,
      but no less than reasonable care
- [ ] Flow-down to sublicensees required (at least as restrictive as head license)
- [ ] Return or destruction obligations on termination

**11. Representations, Warranties, and Disclaimers**

- [ ] Licensor warrants corporate authority and enforceability of license
- [ ] IP ownership warranty: does licensor solely own or have authority to sublicense?
- [ ] Non-infringement warranty (or knowledge-qualified version: "to licensor's knowledge")
- [ ] Quiet enjoyment covenant: licensee's use within scope will not be disturbed
- [ ] No conflicting licenses warranty (especially critical for exclusive licenses)
- [ ] Disclaimer of implied warranties (e.g., merchantability, fitness for purpose) — scope
      appropriate for IP category and jurisdiction
- [ ] Warranty survival period defined (typically 2–3 years post-execution, or post-delivery)
- [ ] Remedies for breach of warranty: limited to replacement/correction or indemnification?

**12. Assignment and Change of Control**

- [ ] Assignment requires prior written consent
- [ ] Change of control triggers assignment provisions (to prevent competitor acquisition
      of license)
- [ ] Affiliate assignment exceptions: permitted without consent?
- [ ] Anti-assignment clause is mutual (or, if only one-directional, is it appropriate
      for the party's position?)
- [ ] What happens to sublicenses on assignment?
- [ ] Assignment to successor by merger/acquisition: what representations must the
      assignee provide to licensor?

**13. Governing Law and Dispute Resolution**

- [ ] Choice of law specified
- [ ] Jurisdiction for IP validity disputes (consider UPC for EU patent disputes [VERIFY])
- [ ] Dispute resolution mechanism (litigation, arbitration, expert determination for
      royalty disputes, escalation)
- [ ] Escalation provisions before formal proceedings (management escalation → mediation)
- [ ] For international licenses: consider WIPO Arbitration Center for IP-specific disputes
- [ ] IP-specific considerations: some jurisdictions will not permit arbitration of certain
      IP validity questions [VERIFY jurisdiction]

**14. Compliance, Regulatory, and Boilerplate**

- [ ] Export controls: ITAR/EAR compliance (US); UK Strategic Export Controls; EU Dual-Use
      Regulation — critical for technology licenses involving controlled technologies
- [ ] Anti-bribery and anti-corruption representations
- [ ] Sanctions compliance (OFAC, EU, UK OFSI)
- [ ] Data protection: if licensed technology processes personal data, GDPR/UK DPA/CCPA
      compliance and DPA/BAA requirement
- [ ] Entire agreement / integration clause: parol evidence implications
- [ ] Order of precedence: when multiple documents (license, schedule, SOW) form the agreement
- [ ] Severability: what happens if a clause (e.g., field-of-use restriction) is struck?
- [ ] Amendment provisions: written amendments only; who is authorized to sign?
- [ ] No third-party beneficiary (or express rights for sublicensees where appropriate)

---

## Deviation Severity Classification

### GREEN — Acceptable

The clause aligns with or is better than the organization's standard position. Minor
variations that are commercially reasonable and do not materially increase risk.

**Examples for IP licensing:**

- Non-exclusive grant-back (licensor perspective — acceptable, not ideal)
- Audit rights once per year with 30-day notice (market standard)
- Governing law in an established commercial jurisdiction close to preferred one
- Knowledge-qualified IP ownership warranty from established licensor with strong IP portfolio

**Action**: Note for awareness. No negotiation needed.

### YELLOW — Negotiate

The clause falls outside the standard position but within a negotiable range. Requires
attention and likely negotiation, but not escalation.

**Examples for IP licensing:**

- Royalty base includes some non-standard deductions
- Sublicensing permitted without prior written consent but with notification requirement
- Grant-back is non-exclusive but "Improvement" definition is overbroad
- Audit frequency limited to once every 18 months
- §365(n) reference absent but licensor is financially stable with strong IP position

**Action**: Generate specific redline language, fallback position, and business impact
estimate.

### RED — Escalate

The clause falls outside the acceptable range, creates material legal or financial risk,
or triggers a defined escalation criterion. Requires senior IP counsel or decision-maker
review before proceeding.

**Examples for IP licensing:**

- No royalty audit rights in a running royalty license
- IP indemnification capped at 3 months of fees
- Mandatory exclusive grant-back of improvements
- No sublicense survival clause
- §365(n) absent for critical single-source technology from a startup licensor

**Action**: Explain the specific risk (with legal basis), provide market-standard
alternative language, estimate exposure, recommend escalation path.

### CRITICAL — Immediate Attention Required

The provision is legally defective, potentially illegal, or creates an existential risk
to the organization regardless of risk appetite. These are not negotiation items — they
require immediate resolution before the license can be executed.

**CRITICAL triggers in IP licensing:**

- Royalties on sales after patent expiration (US: _Brulotte_ — per se unlawful)
- Exclusive copyright license without written instrument (17 U.S.C. §204 — unenforceable)
- Trademark license with no quality control provisions (naked licensing = abandonment)
- Assignment of trademark without goodwill (assignment in gross = abandonment)
- Exclusive grant-back of severable improvements in EU-governed license (TTBER Art. 5(1)(b))
- Patent license containing an unenforceable "no-exhaustion" clause in US [VERIFY]
- Copyright license purporting to grant rights for the full copyright term when §203
  creates a non-waivable 35-year termination right

**Action**: Flag immediately. Do not proceed to signature. Engage specialist IP counsel.

---

## Redline Format

Use this format for every YELLOW and RED deviation redline:

```
**Clause**: [Section reference and clause name]
**Current language**: "[exact quote from the agreement, or summary if too long]"
**Proposed redline**: "[specific alternative language]"
**Rationale**: [1–2 sentences explaining why, suitable for sharing with counterparty's counsel]
**Legal basis**: [Relevant statute, regulation, case, or general market practice]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative position if primary redline is rejected]
**Confidence**: [Definite / High / Probable / Possible]
```

**Redline Best Practices:**

- Never propose a deletion without a replacement — offer an alternative
- Redlines should balance the licensee's and licensor's legitimate interests
- Do not over-redline: every redline asks the counterparty to give something up; ration them
- Lead with must-haves; be willing to trade nice-to-haves
- Frame rationales in terms of market standards ("this is typically structured as..."),
  not demands ("you must change this")

---

## Negotiation Priority Framework

Use this framework to triage findings into negotiation priority tiers.

### Tier 1 — Must-Have (Non-Negotiable)

Items in Tier 1 are deal-critical. If the counterparty does not move, consider whether
to walk away.

**Licensor perspective:**

- Quality control provisions in trademark license (CRITICAL — abandonment risk)
- Royalty audit rights with records retention ≥ 3 years
- No post-expiration patent royalty obligation (US: illegal)
- Anti-assignment clause prohibiting transfer to competitors
- Change-of-control provisions with licensor consent right
- Grant-back limited to non-exclusive license of improvements (not assignment)

**Licensee perspective:**

- IP indemnification with remedy waterfall and adequate cap (or no cap)
- §365(n) reference for US patent/copyright licenses from startup/distressed licensor
- Sublicense survival clause (if sublicensing is part of licensee's business model)
- Cure period before termination for breach
- Royalty base limited to net sales from licensed products (not entire business revenue)
- Written instrument for any exclusive copyright license (§204 compliance)

### Tier 2 — Should-Have (Negotiate Hard)

Items in Tier 2 are important but not deal-breaking.

**Licensor:**

- Minimum annual royalties in exclusive licenses
- Diligence/commercialization obligations with milestone conversion rights
- IP escrow for licensee's confidential information
- Narrowly defined "Improvement" in grant-back clause
- Audit rights reaching sublicensees

**Licensee:**

- Source code / IP embodiment escrow with Level 2+ verification
- Most-favored-nation clause with appropriate carve-outs
- Post-termination sell-off period (30–90 days)
- IP ownership warranty (not just knowledge-qualified)
- Cross-license back to licensee's improvements under non-exclusive grant-back

### Tier 3 — Nice-to-Have (Concession Candidates)

Items in Tier 3 are preferable but concedable to reach agreement.

- Audit frequency (twice vs. once per year)
- Underpayment threshold for cost-shifting (5% vs. 10%)
- Notice period for audit (30 vs. 60 days)
- MFN clause expiration date
- Escrow update frequency
- Dispute resolution mechanism for audit disagreements

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                             | Fail Action                                              |
| -------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established principle | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction      | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments or repeal                           | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the agreement's governing law; no jurisdiction bleed       | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden                                        | Add confidence qualifier                                 |

**IP licensing-specific currency checks:**

- EU TTBER Regulation 316/2014: expires 30 April 2026 — verify whether new TTBER is in
  force before citing specific TTBER provisions
- 17 U.S.C. §203 termination rights: check whether any pending legislation has modified
  the 35-year rule
- _Mission Products v. Tempnology_ (2019) trademark bankruptcy: check for subsequent
  circuit court decisions interpreting the holding

### Self-Interrogation for CRITICAL and RED Items

For any item classified as CRITICAL or RED, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the
statute/case/principle cited? Would a court or regulator in this jurisdiction actually reach
this conclusion on these facts? Is there a counter-argument the counterparty's counsel will make?

**Pass 2 — Completeness**: Have all relevant statutes and regulations been considered? Are
there jurisdiction-specific defenses or safe harbors that might mitigate the risk? Are
there regulatory dimensions (competition law, insolvency, export controls) not yet addressed?

**Pass 3 — Challenge**: What is the strongest argument that this clause IS acceptable?
Under what commercial circumstances might a reasonable IP lawyer accept this risk? Is the
RED/CRITICAL classification proportionate, or is this actually YELLOW with appropriate
mitigations?

### Confidence Scoring

| Level        | Range     | Meaning                                          | Action                                                |
| ------------ | --------- | ------------------------------------------------ | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, clear statute, no ambiguity         | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments but reasonable minds could differ | State with reasoning and contra-indicators            |
| **Possible** | 0.40–0.59 | Genuinely uncertain, competing authorities       | Flag for counsel review with both sides               |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                          | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Append the following YAML block to every review output:

```yaml
glass_box:
  skill: "legalcode-licensing-agreement-review"
  agreement: "[License title and date, or 'Untitled agreement — [date reviewed]']"
  ip_categories:
    - "[Patent / Trademark / Copyright / Trade Secret / Know-How / Software / Mixed-IP]"
  user_side: "[Licensor / Licensee / Neutral]"
  exclusivity: "[Exclusive / Sole / Non-Exclusive / Cross-License / Unknown]"
  governing_law: "[Jurisdiction identified from the agreement]"
  playbook_used: "[Playbook name or 'General IP licensing market standards']"
  clauses_reviewed: "[number of the 14 categories reviewed]"
  clauses_present: "[number]"
  clauses_missing: "[number — list missing categories]"
  ip_pre_screen:
    patent_checks: "[PASS / FLAG / N/A]"
    trademark_checks: "[PASS / FLAG / N/A]"
    copyright_checks: "[PASS / FLAG / N/A]"
    trade_secret_checks: "[PASS / FLAG / N/A]"
    know_how_checks: "[PASS / FLAG / N/A]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to temp file or 'Not created']"
  statutes_consulted:
    - "[Statute 1 — VERIFIED (legalcode-mcp) or [VERIFY]]"
    - "[Statute 2 — VERIFIED (legalcode-mcp) or [VERIFY]]"
  case_law_consulted:
    - "[Case 1 — VERIFIED (legalcode-mcp) or [VERIFY]]"
  citations_verified: "[number VERIFIED] / [number total]"
  clause_interactions_assessed: "[number of material interactions flagged]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL or RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
    - "legalcode_mcp: [Connected/Not connected] — [impact on legal authority verification]"
  reviewer: "AI-assisted — requires qualified IP legal review before reliance"
```

---

## Anti-Patterns

What NOT to do when reviewing IP licensing agreements:

1. **Failing to identify the IP category first** — A trademark license without quality control
   is CRITICAL; the same clause in a patent license is irrelevant. Identify IP types before
   reviewing any clause.

2. **Accepting "AS IS" without probing the IP warranty package** — Disclaimer of all IP
   warranties is standard for software but not for a commercialization license. "AS IS" in
   a patent license covering a licensee's core product is a RED flag, not a boilerplate
   acceptance.

3. **Ignoring post-expiration royalty risk in mixed-IP bundles** — When a license covers
   both patents and know-how, failing to check whether royalties are apportioned invites
   a _Brulotte_ challenge in US courts for the patent component.

4. **Treating grant scope as "usually fine"** — The grant clause is the most litigated
   provision in IP licensing. Vague grants create expensive scope disputes. Review every
   word: exclusivity, FOU, territory, permitted acts, sublicensing.

5. **Missing the sublicense survival gap** — If the head license terminates, sublicenses
   terminate automatically unless a survival clause exists. Downstream sublicensees —
   often an entire distribution network — lose their rights through no fault of their own.
   This gap is common and catastrophic.

6. **Confusing exclusive and sole licenses** — An exclusive license (only licensee can
   exploit) is very different from a sole license (licensee and licensor can exploit;
   no further licenses). Misclassifying exclusivity leads to wrong analysis.

7. **Overlooking the §365(n) trademark exclusion** — §365(n) protects patent, copyright,
   and trade secret licenses — NOT trademark licenses. A mixed-IP bundle license gives
   partial §365(n) protection. Trademark-only licensees need express contractual protection.

8. **Approving "commercially reasonable efforts" diligence clauses without analysis** —
   "Best efforts," "commercially reasonable efforts," "reasonable efforts," and "good faith
   efforts" have materially different meanings across US jurisdictions and in EU/UK. Never
   treat these as equivalent.

9. **Redlining royalty rate without analyzing royalty base** — A 3% royalty on gross global
   revenue is far more expensive than a 7% royalty on net sales from products practicing the
   licensed patents. Always analyze base and rate together.

10. **Skipping the clause interaction analysis** — Individual clauses can each appear
    acceptable but create compound risk. A royalty cap of 12 months' fees and an IP
    indemnification cap of 12 months' fees can together fail to cover a $50M patent claim
    against a licensee paying $100K/year.

11. **Accepting "improvement" grant-back without antitrust screening** — Exclusive grant-back
    of severable improvements is an EU TTBER excluded restriction regardless of market share.
    Mandatory assignment of improvements is a RED item that destroys licensee innovation
    incentive.

12. **Failing to verify quality control is actually exercised** — For trademark licenses,
    contractual quality control provisions alone are insufficient to avoid naked licensing
    risk. Licensor must actually exercise supervision. Flag whether the agreement includes
    mechanisms for actual oversight (inspection rights, sample approval, customer complaint
    reporting).

13. **Treating IP indemnification as equivalent to general indemnification** — IP infringement
    indemnification is the licensor's core obligation. If it is subject to the general liability
    cap (often 12 months' fees), a $100M patent infringement claim against a SaaS customer
    paying $50K/year is effectively uncovered. Analyze the cap structure specifically.

14. **Ignoring the §203 copyright termination right** — For post-1978 copyright grants, the
    35-year termination right under 17 U.S.C. §203 is non-waivable. Long-term copyright
    licenses in music, publishing, and entertainment should always address §203 risk
    allocation even though the right cannot be contractually waived.

15. **Assuming the law review is complete after reviewing the main agreement** — IP licenses
    often incorporate external documents: standard licensing terms, patent schedules, quality
    control manuals, data protection addenda, and side letters. Each can modify the main
    license in material ways. Always ask whether incorporated documents exist.

16. **Neglecting trademark recordation requirements** — In many jurisdictions (EU, UK, China,
    Korea, Brazil, and others), a trademark license must be recorded with the relevant
    trademark registry to be enforceable against third parties. Absence of a recordation
    obligation in the license is a RED gap in cross-border trademark licensing.

17. **Skipping the TTBER currency check** — EU TTBER Regulation 316/2014 expires 30 April 2026. A new TTBER is expected by 1 May 2026. Any EU technology license under a TTBER
    safe harbor must be reviewed against the new TTBER's framework once published. Always
    flag this transition risk.

18. **Accepting "no audit rights" from an established counterparty** — In running royalty
    licenses, no audit rights means royalty accuracy can never be verified. Even trusted
    counterparties make accounting errors; audit rights are a fundamental protection, not
    an accusation of dishonesty.

19. **Ignoring the AI training data dimension** — As of 2024–2025, AI training data licensing
    is an active area of legal development. If the licensed IP includes copyrighted works
    (text, images, music, software) and the licensee or licensor is an AI company, explicit
    AI training use provisions are now commercially expected. Failure to address this creates
    ambiguity in a high-stakes area.

20. **Forgetting the graceful degradation check** — Every external tool dependency (legalcode-mcp,
    CLM system) must have a fallback. If legalcode-mcp is not connected, flag that legal
    authority has not been verified and mark all statutory/case references with [VERIFY].

---

## Writing Standards

**For redline rationales** (shared with counterparty's counsel):

- Plain language. No jargon or filler.
- Active voice: "This clause excludes IP indemnification for combination infringement" not
  "Liability for combination infringement is excluded by this clause"
- Short sentences. One point per sentence.
- Name the actor: "Licensor must..." not "It is required that..."
- Specific, not vague: cite the relevant provision rather than saying "this may have issues"

**For internal analysis:**

- Same plain-language standards
- Technical legal analysis permitted where it adds precision
- Confidence qualifiers where appropriate
- Glass Box audit trail appended at the end

**Quality gates before delivery:**

1. Can a non-lawyer business stakeholder understand the executive summary?
2. Can the counterparty's IP counsel understand and respond to each redline?
3. Is every legal claim backed by a specific citation (or flagged [VERIFY])?
4. Are any phrases vague, hedging, or ambiguous? If yes, fix.
5. Could any sentence be shorter without losing meaning? If yes, shorten.
6. Have IP category-specific CRITICAL issues been surfaced prominently?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 5, search for patent exhaustion, post-expiration royalty, trademark quality
  control, copyright termination, §365(n) protection, and TTBER safe harbor authority
  relevant to the governing law
- Save results to `/tmp/legalcode-license-review-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail
- Cross-check TTBER currency: confirm whether Regulation 316/2014 is still in force or
  whether a new TTBER has been published (critical transition: April 2026)

**Without legalcode-mcp:**

- Proceed with general knowledge but mark all statutory and case law references [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Focus on structural quality, workflow design, and clause-category coverage; flag that
  legal substance depth requires independent verification

---

## Localization Notes

### United States

- **Brulotte/Kimble** (_Brulotte v. Thys_, 379 U.S. 29 (1964); _Kimble v. Marvel_, 576 U.S. 446
  (2015)): Post-expiration patent royalty obligation is per se unlawful — mixed-IP licenses
  must apportion royalties to avoid violation [VERIFY]
- **§365(n)** (11 U.S.C. §365(n)): Applies to patents, copyright, trade secrets — NOT
  trademarks; trademark licensees require contractual protection
- **§203 copyright termination**: Non-waivable 35-year termination right for all post-1978
  copyright grants; affects music, literary works, film, and software licenses [VERIFY]
- **§204 writing requirement**: Exclusive copyright license requires signed writing;
  non-exclusive licenses may be granted orally (though this is inadvisable)
- **Lanham Act naked licensing**: Quality control mandatory for trademark licenses or mark
  is abandoned (15 U.S.C. §1055, §1127)
- **Patent exhaustion**: _Quanta_ and _Impression Products_ — "no-exhaustion" clauses
  unenforceable through patent law; use contract law instead [VERIFY]
- **Joint ownership (35 U.S.C. §262)**: Co-owner may license without co-owner consent
  and without accounting — unlike EU/UK
- **State choice of law**: Delaware and New York are most common; different standards for
  "commercially reasonable efforts" and "best efforts"

### European Union

- **TTBER Regulation 316/2014**: Expires 30 April 2026 — review all EU technology licenses
  for compliance with new TTBER framework once published (draft: September 2025)
- **TTBER hardcore restrictions** (Art. 4): Absolute prohibitions including price fixing
  between competing undertakings, absolute territorial protection, output restrictions
- **TTBER excluded restrictions** (Art. 5): Cannot benefit from block exemption regardless
  of market share — includes exclusive grant-back of severable improvements,
  non-challenge termination clauses
- **Moral rights**: Often inalienable in EU member states (e.g., France, Germany); cannot
  be waived even in "work for hire" agreements; tailor accordingly
- **EU patent exhaustion**: EEA-wide exhaustion — placing goods on market in any EEA
  country with consent exhausts rights throughout EEA [VERIFY]
- **Joint ownership**: Unanimous consent required to license; co-owner cannot license
  without the other's agreement (unlike US)
- **SEP/FRAND**: EU SEP Regulation proposed but withdrawn from 2025 Work Programme;
  UPC developing EU FRAND jurisprudence — monitor developments

### United Kingdom (Post-Brexit)

- **Post-Brexit exhaustion**: UK domestic exhaustion — goods placed on UK market are
  exhausted in UK; NOT in EEA; EEA-placed goods are exhausted in UK (asymmetric) [VERIFY]
- **CDPA s.90(3)**: Exclusive copyright license must be in writing — same as US §204
- **TMA s.28(4)**: Sublicenses only as permitted in head license — express sublicense
  authorization required
- **No §365(n) equivalent**: Insolvency Act 1986 and CIGA 2020; IP licenses treated as
  general executory contracts; administrator/liquidator has broad discretion; contractual
  protection essential
- **FRAND/SEP jurisdiction**: UK courts (post-_Unwired Planet_, _Optis v Apple_) actively
  setting global FRAND rates; risk of anti-suit injunctions from unwilling licensees

### Cross-Border Issues

- **Trademark recordation**: EU, UK, China, Korea, Brazil, and many others require
  recordation of trademark license for third-party enforceability; include contractual
  obligation for licensee to cooperate with recordation
- **Moral rights in EU-authored works**: Cannot be waived in France, Germany, and most
  EU jurisdictions — even if US work-for-hire contract attempts to extinguish them
- **Compulsory licensing**: Some jurisdictions have compulsory license regimes (UK design
  rights last 5 years; pharmaceutical patent systems in developing countries); address
  in cross-border licenses
- **Export controls**: ITAR, EAR (US); UK Strategic Export Controls; EU Dual-Use
  Regulation — technology licenses involving controlled items require compliance provisions

---

## Output Format Template

```markdown
## IP Licensing Agreement Review

**Agreement**: [Name/identifier of the license]
**IP Categories**: [Patent / Trademark / Copyright / Trade Secret / Know-How / Mixed-IP]
**Parties**: [Licensor name] (Licensor) → [Licensee name] (Licensee)
**Your Side**: [Licensor / Licensee / Neutral]
**Exclusivity**: [Exclusive / Sole / Non-Exclusive / Unknown]
**Governing Law**: [Jurisdiction]
**Review Basis**: [Playbook name / General IP licensing market standards]
**Date of Review**: [date]

---

## IP Category Pre-Screen Results

| Category       | Checks Run | Issues Found       | Severity                   |
| -------------- | ---------- | ------------------ | -------------------------- |
| [Patent]       | [N checks] | [issues or "None"] | [CRITICAL/RED/YELLOW/PASS] |
| [Trademark]    | [N checks] | [issues or "None"] | [CRITICAL/RED/YELLOW/PASS] |
| [Copyright]    | [N checks] | [issues or "None"] | [CRITICAL/RED/YELLOW/PASS] |
| [Trade Secret] | [N checks] | [issues or "None"] | [CRITICAL/RED/YELLOW/PASS] |

---

## Key Findings

| #   | Issue               | Severity       | Clause    |
| --- | ------------------- | -------------- | --------- |
| 1   | [Top issue summary] | CRITICAL / RED | [Section] |
| 2   | [Second issue]      | RED            | [Section] |
| 3   | [Third issue]       | RED / YELLOW   | [Section] |

[Add rows as needed]

---

## Clause Interaction Alerts

[Table of material clause interactions identified in Step 10]

---

## Missing Clauses

| Missing Clause | Why It Matters | Severity   |
| -------------- | -------------- | ---------- |
| [Clause type]  | [Impact]       | [severity] |

---

## Clause-by-Clause Analysis

### 1. Grant Scope and Field of Use — [GREEN / YELLOW / RED / CRITICAL] | Confidence: [level]

**Agreement says**: [summary of the grant provision]
**Standard position**: [playbook or market standard for licensor/licensee]
**Deviation**: [description of the gap]
**IP-specific issue**: [any category-specific concern, e.g., "Have-made rights granted in a
sole-source manufacturing context"]
**Business impact**: [what this means practically]
**Redline** (if YELLOW or RED):

> [Specific proposed language]

[Repeat for all 14 clause categories]

---

## Negotiation Strategy

**Tier 1 — Must-Have (Non-Negotiable)**:

- [list with brief rationale for each]

**Tier 2 — Should-Have (Negotiate Hard)**:

- [list]

**Tier 3 — Nice-to-Have (Concession Candidates)**:

- [list]

**Recommended approach**: [sequencing, tone, strategic trades]

---

## Next Steps

1. [Specific action with owner and deadline if applicable]
2. [...]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis based on deep research across US,
EU, and UK IP licensing legal frameworks including: 35 U.S.C. §§ 154/261/262/271/365(n)
(cross-reference); 17 U.S.C. §§ 101/106/201/203/204 (copyright termination and exclusive
license formalities); 15 U.S.C. §§ 1055/1127 (Lanham Act quality control/naked licensing);
18 U.S.C. §§ 1831–1839 (DTSA); 11 U.S.C. § 365(n) (licensor insolvency); EU TTBER
Regulation 316/2014 (expiring April 2026) and EC Draft Revised TTBER September 2025;
DOJ/FTC 2017 IP Licensing Antitrust Guidelines; UK Patents Act 1977; CDPA 1988 ss. 90–92;
Trade Marks Act 1994 s.28; Insolvency Act 1986 / CIGA 2020; _Brulotte v. Thys_, 379 U.S.
29 (1964); _Kimble v. Marvel_, 576 U.S. 446 (2015); _Quanta Computer v. LG Electronics_,
553 U.S. 617 (2008); _Impression Products v. Lexmark_, 137 S.Ct. 1523 (2017); _Mission
Products Holdings v. Tempnology_, 139 S.Ct. 1652 (2019); _Speedplay v. Bebop_ sublicense
survival doctrine; Barcamerica International v. Tyfield Importers (9th Cir. 2002) (naked
licensing); 2 Live Crew §203 termination litigation; _Thomson Reuters v. ROSS_ (2025) (AI
training data copyright); _Bartz v. Anthropic_ (June 2025) (AI training fair use); WIPO
Trademark Licensing Guide; WIPO Secrets Guide; NIH Research Tools Policy (reach-through
royalties); NCC Group/Escode Level 1/2/3 escrow verification standards.
Repository best-practice patterns adopted from `legalcode-contract-review` (quality
frameworks, Glass Box audit trail, anti-patterns architecture, redline format) and
`legalcode-technology-license-agreement` (grant scope analysis, royalty structure, §365(n)
coverage, sublicense chain mechanics, IP indemnification remedy waterfall). Complements
the technology-license skills by extending coverage to trademark, copyright, trade secret,
and know-how licensing categories, adding the IP Category Pre-Screen framework, the Clause
Interaction Analysis matrix, and the four-tier (GREEN/YELLOW/RED/CRITICAL) severity system
with IP-licensing-specific CRITICAL triggers.
