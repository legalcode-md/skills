---
name: legalcode-consulting-agreement
description: Draft, review, and negotiate consulting services agreements for B2B and independent contractor
  relationships across jurisdictions. Use when users ask for consultant contracts, professional services
  agreements, advisory agreements, statement-of-work-linked master service terms, or help negotiating
  scope, fees, IP ownership, confidentiality, and termination risk. Supports playbook-based or general-standard
  review with confidence-scored analysis and auditable output. Jurisdiction-agnostic with localization
  markers for any governing law.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Consulting Agreement

> **Disclaimer**: This skill provides a framework for AI-assisted consulting agreement
> drafting and review. It does not constitute legal advice. All outputs should be reviewed
> by a qualified legal professional licensed in the relevant jurisdiction before use. Laws
> change; verify current applicability before relying on any provision described here.
> Statutory and case law references cited from memory carry hallucination risk — verify
> against authoritative sources before relying on them.

## Purpose and Scope

This skill drafts, reviews, and negotiates consulting agreements where a consultant or
services provider performs defined professional services for a client. It identifies
deviations from standard positions, classifies their severity, generates actionable redline
suggestions, and produces a confidence-scored, auditable analysis.

**Covers:**

- Master consulting agreements with optional statements of work (SOWs)
- Standalone consulting contracts with fixed scope
- Independent contractor arrangements where employment classification risk must be managed
- Advisory agreements and board advisory arrangements
- Clause-by-clause analysis with severity classification (GREEN/YELLOW/RED)
- Redline generation with fallback positions
- Missing clause detection and gap analysis
- Quality-verified output with Glass Box audit trail

**Does not:**

- Replace jurisdiction-specific employment, tax, or sector-regulated legal advice
- Provide legal advice or replace qualified counsel
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers
- Cover employee contracts (see employment-agreement skill)

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The agreement's own governing law clause determines
which legal framework applies. The review identifies the governing law early and adapts
the analysis accordingly.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- Worker classification and labor law constraints (employee vs. independent contractor tests)
- Non-compete and non-solicit enforceability limits
- Mandatory data protection language for personal data processing
- Tax withholding, VAT/GST treatment, and invoicing formalities
- Liability limitation and indemnity boundaries where mandatory law restricts exclusions
- IP ownership defaults and assignment formality requirements
- Work-for-hire doctrine applicability (US) or moral rights requirements (civil law)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- Multiple valid approaches exist and the user's preference matters
- Ambiguity in the agreement creates a fork that only the user can resolve
- Risk tolerance or business context is needed to classify severity correctly

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

Accept the consulting agreement in any of these formats:

- **File**: PDF, DOCX, or other document format
- **URL**: Link to an agreement in a document management system
- **Pasted text**: Agreement text pasted directly into the conversation
- **Drafting request**: Request to draft a new consulting agreement from scratch

If no agreement is provided and no drafting request is made, prompt the user to supply one.

### Step 2: Gather Context

**CLARIFY** — Before beginning the review or draft, ask the user these questions.
Present them as a structured set of options where possible:

1. **Which side are you on?**
   - Options: Client (engaging the consultant), Consultant/Service Provider, Other
   - _Why this matters_: The entire analysis flips depending on which side you represent.
     What protects a client harms a consultant and vice versa.

2. **Engagement structure?**
   - Options: Fixed-scope project (one-off), Ongoing retainer/advisory, Master agreement
     with multiple SOWs, Time-and-materials engagement, Hybrid
   - _Why this matters_: Different structures require different clause emphasis. A fixed-scope
     project needs tight deliverable definitions; a retainer needs clear scope boundaries.

3. **What type of services?**
   - Options: Strategic advisory/consulting, Technical/IT services, Creative/design work,
     Professional services (legal, accounting, etc.), Management consulting, Research/analysis,
     Other (describe)
   - _Why this matters_: Service type affects IP ownership expectations, standard of care,
     and industry-specific requirements.

4. **Will the consultant access or process personal data?**
   - Options: Yes (personal data of employees/customers), No, Unsure
   - _Why this matters_: Personal data processing triggers data protection requirements
     (GDPR, CCPA, etc.) and may require a separate DPA.

5. **Deadline and negotiation posture?**
   - Options: Urgent (days), Standard (1-2 weeks), Flexible (no hard deadline)
   - _Why this matters_: Affects how many issues to surface vs. focus only on critical ones.

6. **Deal context?**
   - Free text. Prompt with examples: deal size, strategic importance, existing relationship,
     whether this is a template or one-off negotiation, consultant's leverage.
   - _Why this matters_: A $10K project gets different treatment than a $1M strategic engagement.

If the user provides partial context, proceed with what you have but **state your
assumptions explicitly**. Do not silently assume.

### Step 3: Load the Playbook

Check for the organization's consulting agreement review playbook in local settings
(e.g., `legal.local.md` or similar configuration files).

The playbook should define:

- **Standard positions**: Preferred terms for each major clause
- **Acceptable ranges**: Terms that can be agreed without escalation
- **Escalation triggers**: Terms that require senior counsel or decision-maker sign-off

**If no playbook is configured:**

**CLARIFY** — Inform the user that no playbook was found, and ask which approach to take:

- **Option A: Set up a playbook now** — Walk through defining the organization's standard
  positions for key clauses (scope definition, IP ownership, liability cap, termination
  rights, payment terms). This takes time upfront but makes this and all future reviews
  more precise.
- **Option B: Proceed with general commercial standards** — Use widely-accepted market
  standards as the baseline. Faster, but the review may not reflect the organization's
  specific risk appetite.
- **Option C: I'll provide positions as we go** — Start the review and I'll ask about your
  preferred position when it matters for each clause.

If proceeding without a playbook, clearly label the review: "Based on general commercial
standards — not organizational positions"

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Read the agreement's governing law clause and identify the applicable jurisdiction. Then
use **legalcode-mcp** to build a working legal reference file for this review.

**Research process:**

1. **Identify the governing law** from the agreement (e.g., "laws of the State of California,"
   "English law," "German law").

   **CLARIFY** — If any of the following are true, ask the user before proceeding:
   - **No governing law clause found**: Ask which jurisdiction the user expects to apply,
     and flag the absence as a RED deviation.
   - **Governing law is unusual** for the parties: Confirm the user is aware.

2. **Search legalcode-mcp** for jurisdiction-relevant authority:
   - Worker classification tests (employee vs. independent contractor)
   - IP ownership defaults (work-for-hire doctrine, moral rights, assignment formalities)
   - Limitation of liability enforceability rules
   - Non-compete and non-solicit enforceability
   - Data protection requirements for service providers
   - Tax withholding and reporting obligations
   - Consumer protection rules if applicable

3. **Save the most relevant results** into a local temporary reference file (e.g.,
   `/tmp/legalcode-consulting-authority.md`).

4. **Use this reference file throughout the analysis.** Mark any citation sourced from
   legalcode-mcp as VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**

- Mark every statutory and case law reference with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with the analysis using general commercial knowledge

### Step 5: Clause-by-Clause Analysis

Analyze the agreement systematically. Read the entire agreement before flagging issues —
clauses interact with each other.

**CLARIFY** — For agreements with multiple SOWs or complex structure:

- Ask the user whether to perform a **full review** of all 14 clause categories, or a
  **priority review** focused on the user's stated concerns plus any RED items discovered.
- If the agreement incorporates SOWs by reference, ask whether to review them as well.

Cover all 14 clause categories below (unless the user opted for a priority review):

| #   | Clause Category               | Depth    | Key Review Points                                                                |
| --- | ----------------------------- | -------- | -------------------------------------------------------------------------------- |
| 1   | Parties and Definitions       | Standard | Entity identification, defined terms consistency                                 |
| 2   | Scope of Services             | Deep     | Deliverables, acceptance criteria, change control, assumptions                   |
| 3   | Fees and Payment              | Deep     | Rate/fixed price, expenses, invoicing, late payment, taxes                       |
| 4   | Term and Termination          | Deep     | Duration, renewal, convenience termination, cause termination, wind-down         |
| 5   | Intellectual Property         | Deep     | Background IP, work product ownership, license grants, moral rights              |
| 6   | Confidentiality               | Standard | Definition, exclusions, term, return/destruction                                 |
| 7   | Data Protection               | Deep     | Controller/processor roles, DPA requirement, sub-processors, breach notification |
| 8   | Warranties                    | Standard | Authority, non-infringement, professional standard, disclaimers                  |
| 9   | Indemnification               | Deep     | Scope, mutual vs. unilateral, cap, IP infringement, procedure                    |
| 10  | Limitation of Liability       | Deep     | Cap amount, carveouts, consequential damages, mutual vs. unilateral              |
| 11  | Independent Contractor Status | Deep     | No employment relationship, tax responsibility, substitution                     |
| 12  | Non-Compete and Non-Solicit   | Standard | Scope, duration, geographic limits, enforceability                               |
| 13  | Governing Law and Disputes    | Standard | Choice of law, forum, arbitration vs. litigation                                 |
| 14  | General Boilerplate           | Standard | Assignment, force majeure, notices, amendments, entire agreement                 |

### Step 6: Missing Clause Detection

After analyzing the clauses present, check for important clauses that are entirely absent.

Common missing clause issues in consulting agreements:

- No scope definition or SOW mechanism (RED — undefined obligations)
- No IP ownership clause (RED — default rules may be unfavorable)
- No limitation of liability (RED — unlimited exposure)
- No termination for convenience (YELLOW — locked into engagement)
- No independent contractor language (YELLOW — classification risk)
- No confidentiality provisions (YELLOW — no protection for shared information)
- No DPA when personal data is processed (RED — regulatory violation risk)

**CLARIFY** — When the severity of a missing clause depends on context:

- "This agreement has no data processing terms. Will the consultant access any personal
  data? If yes, this is a RED gap requiring a DPA. If no personal data is involved, it's
  acceptable."

### Step 7: Flag Deviations

Classify each deviation using the three-tier system (GREEN/YELLOW/RED). For each deviation:

- **GREEN**: Note for awareness.
- **YELLOW**: Generate specific redline language, provide a fallback position, and estimate
  business impact.
- **RED**: Explain the specific risk (citing the legal basis where possible), provide
  market-standard alternative language, estimate exposure, and recommend escalation.

**CLARIFY** — For borderline classifications:

- "The liability cap is set at one month's fees. For a $5,000/month engagement, this is a
  $5,000 cap. Is this proportionate to the risk, or should I treat it as RED (too low)?"

### Step 8: Generate Redlines

**CLARIFY** — Before generating redlines, ask about negotiation posture if not clear:

- **Relationship dynamic**: Is this a preferred consultant, a commodity provider, or a
  strategic partner?
- **Volume of redlines**: "I've found [N] items worth negotiating. Do you want redlines for
  all of them, or should I focus on the top [X]?"

For each YELLOW and RED deviation, generate a redline using the format in **Redline Format**
below.

### Step 9: Drafting Mode (If Drafting New Agreement)

If the user requested a new draft:

1. **Select structure**: Master agreement + SOW template, or standalone integrated agreement.

2. **Gather specific parameters**:
   - Party names and addresses
   - Service description and deliverables
   - Fee structure and payment terms
   - Term and termination preferences
   - IP ownership model (client owns all, consultant retains tools, license back)
   - Any special provisions (exclusivity, non-compete, security requirements)

3. **Draft each clause category** following the guidance in the Clause Analysis Reference.

4. **Apply Quality Verification** before delivering the draft.

### Step 10: Quality Verification

Before delivering the analysis or draft:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every RED-classified item, run the 3-pass Self-Interrogation.
3. Assign a Confidence Score to each material clause analysis.
4. Verify completeness: confirm all 14 clause categories have been addressed.
5. Generate the Glass Box Audit Trail and append it to the output.

---

## Clause Analysis Reference

### 1. Parties and Definitions

**Key elements to review:**

- Legal entity names, addresses, and registration identifiers
- Effective date and document version control
- Defined terms used consistently throughout
- Whether affiliates are covered

**Common issues:**

- Incorrect or incomplete party names
- Defined terms inconsistent between master agreement and SOW
- Affiliate coverage without corresponding obligations

### 2. Scope of Services and Deliverables

**Key elements to review:**

- Specific description of services and deliverables
- Acceptance criteria and testing procedures
- Assumptions and dependencies
- Change control mechanism
- Client responsibilities and cooperation requirements

**Common issues:**

- Vague scope ("provide consulting services as requested")
- No acceptance criteria for deliverables
- No change control (scope creep risk)
- Client responsibilities undefined (delays blamed on consultant)
- Mismatch between scope and fees

**Standard position (market norm):**

- Services specifically defined in SOW with measurable deliverables
- Acceptance criteria and testing period defined (typically 5-15 business days)
- Change control requiring written change orders with pricing
- Client responsibilities explicitly stated with timeline impact for delays

[JURISDICTION-SPECIFIC] Key variations:

- **Common law**: Contract interpretation focuses on objective meaning; parol evidence may
  be excluded [VERIFY]
- **Civil law**: Good faith obligations may fill gaps in scope definition [VERIFY]

### 3. Fees, Invoicing, and Payment

**Key elements to review:**

- Fee structure (fixed price, time and materials, retainer, milestone)
- Expense reimbursement and approval requirements
- Invoice timing and payment terms (Net 30, Net 45, etc.)
- Late payment interest and consequences
- Tax treatment (who bears VAT/GST, withholding)
- Currency and payment method
- Price escalation for multi-year engagements
- Invoice dispute mechanism

**Common issues:**

- Ambiguous fee structure (is it fixed or T&M?)
- Expense approval process undefined
- No late payment consequences (creates cash flow risk for consultant)
- Tax allocation unclear (especially for cross-border engagements)
- No price adjustment for long-term engagements
- Right to set-off without limit (client withholds payment for disputed amounts)

**Standard position (market norm):**

- Clear fee structure with rates or fixed prices documented in SOW
- Expenses reimbursed at cost with reasonable pre-approval thresholds
- Net 30 payment terms with interest at 1-1.5% per month for late payment
- Consultant not responsible for client's withholding obligations
- Set-off limited to undisputed amounts; disputed amounts handled separately

### 4. Term and Termination

**Key elements to review:**

- Initial term and renewal mechanism
- Termination for convenience (available? notice period? payment for work done?)
- Termination for cause (what constitutes cause? cure period?)
- Effect of termination on work product, payment, and ongoing obligations
- Transition assistance and knowledge transfer
- Survival clauses

**Common issues:**

- No termination for convenience (client locked in)
- Termination for convenience without payment for work in progress
- Cause termination without cure period
- Immediate termination right for minor breaches
- No transition assistance obligations
- Survival clauses that effectively extend the agreement indefinitely

**Standard position (market norm):**

- Either party may terminate for convenience on 30 days' notice
- On termination for convenience, consultant paid for work performed through termination date
- Cause termination after material breach and 30-day cure period
- Defined transition period with knowledge transfer obligations
- Survival limited to provisions that logically must survive (confidentiality, IP, indemnity,
  limitation of liability)

### 5. Intellectual Property

**Key elements to review:**

- Ownership of pre-existing IP (background IP)
- Ownership of IP developed during the engagement (work product / foreground IP)
- License grants (if ownership is not transferred)
- Work-for-hire provisions (US-specific)
- Moral rights treatment
- Consultant tools, templates, and methodologies
- Feedback clauses
- Third-party IP and open source

**Common issues:**

- All IP automatically transfers to client (captures consultant's pre-existing tools)
- No carve-out for consultant's general knowledge and reusable methodologies
- Work-for-hire provisions for work that does not qualify under US copyright law
- No moral rights waiver (civil law jurisdictions)
- Broad feedback clauses granting perpetual licenses to suggestions
- No treatment of third-party or open source components

**Standard position (market norm):**

- Background IP: each party retains ownership of their pre-existing IP
- Work product: client owns deliverables specifically created for the engagement
- Consultant tools: consultant retains ownership of pre-existing tools, templates, and
  methodologies, with perpetual license to client to use them as part of deliverables
- License back: consultant receives limited license to use deliverables for portfolio/
  reference purposes (where appropriate)
- Moral rights: waived or not asserted to extent permitted by law

[JURISDICTION-SPECIFIC] Key variations:

- **US**: Work-for-hire applies only to specified categories of works (collective works,
  part of motion pictures, etc.) or requires employee relationship. For other works,
  assignment must be explicit [VERIFY]
- **UK**: No work-for-hire doctrine. Copyright must be assigned in writing (CDPA s.90(3)).
  Moral rights can be waived but not assigned [VERIFY]
- **EU/Civil law**: Moral rights are often inalienable. Copyright transfers may require
  specifying fields of exploitation. Employee works have different rules [VERIFY]
- **Germany**: Copyright (Urheberrecht) cannot be transferred, only licensed. Moral rights
  (Urheberpersonlichkeitsrecht) are inalienable [VERIFY]

### 6. Confidentiality and Data Security

**Key elements to review:**

- Definition of confidential information
- Exclusions (public domain, prior possession, independent development)
- Use restrictions and need-to-know access
- Term of confidentiality obligations
- Return/destruction requirements
- Security measures and breach notification

**Common issues:**

- Overbroad definition without workable exclusions
- Asymmetric obligations (only consultant bound)
- Perpetual confidentiality for all information
- No security requirements despite sensitive data access
- No breach notification obligation

**Standard position (market norm):**

- Mutual confidentiality with standard exclusions
- Confidentiality survives termination for 2-5 years (perpetual for trade secrets)
- Security measures appropriate to information sensitivity
- Prompt breach notification (24-72 hours)

### 7. Data Protection

**Key elements to review:**

- Whether personal data will be processed
- Controller vs. processor classification
- DPA requirement and incorporation
- Sub-processor rights and notification
- Data breach notification timeline
- Cross-border transfer mechanisms
- Data deletion on termination

**Common issues:**

- No DPA when personal data is processed (GDPR violation)
- Controller/processor roles misallocated
- Blanket sub-processor authorization without notification
- Breach notification timeline longer than regulatory requirements
- No cross-border transfer protections

**Standard position (market norm):**

- If personal data processed, DPA required as schedule or incorporated document
- Clear controller/processor designation
- Sub-processor changes with notification and objection right
- Breach notification within 48-72 hours
- SCCs or equivalent for international transfers

[JURISDICTION-SPECIFIC] Key variations:

- **EU (GDPR)**: 72-hour breach notification to authority. Art. 28 processor requirements.
  SCCs required for transfers outside adequacy countries [VERIFY]
- **UK**: UK GDPR + DPA 2018. UK IDTA for transfers [VERIFY]
- **US**: State-level laws (CCPA/CPRA, state breach notification). No federal data
  protection law [VERIFY]

### 8. Warranties and Disclaimers

**Key elements to review:**

- Warranty of authority and enforceability
- Professional standard of care warranty
- Non-infringement warranty
- Compliance with law warranty
- Warranty disclaimers (AS IS, implied warranties)
- Warranty remedies and survival

**Common issues:**

- Absolute warranties disconnected from practical service context
- No professional standard of care (creates negligence issues)
- Broad non-infringement warranty without carve-outs for client materials
- No disclaimers for deliverables incorporating client input
- No remedy structure (jump straight to termination)

**Standard position (market norm):**

- Warranty that services performed in professional and workmanlike manner
- Non-infringement warranty excluding client-provided materials and specifications
- Compliance with applicable law warranty
- Reasonable disclaimers of implied warranties (merchantability, fitness for purpose)
- Warranty claim procedure with cure opportunity

### 9. Indemnification

**Key elements to review:**

- Whether indemnification is mutual or unilateral
- Indemnification triggers (IP infringement, breach, negligence, third-party claims)
- Cap on indemnification liability
- Procedure (notice, control of defense, settlement consent)
- Carve-outs (client-provided materials, specifications, modifications)
- Relationship to limitation of liability clause

**Common issues:**

- One-sided indemnification with no reciprocity
- Indemnification for "any breach" (effectively uncaps liability)
- No carve-out for claims arising from client materials
- No right to control defense
- Indemnification uncapped when liability cap applies to other claims

**Standard position (market norm):**

- Mutual indemnification for each party's IP infringement and negligence
- Consultant indemnifies for IP infringement in deliverables (excluding client materials)
- Client indemnifies for claims arising from client-provided materials and specifications
- Standard procedure (prompt notice, right to control defense, settlement consent)
- Indemnification subject to overall liability cap (or separate super-cap)

[JURISDICTION-SPECIFIC] Key variations:

- **Common law**: Indemnity is primary obligation with different remoteness rules than
  damages for breach [VERIFY]
- **Civil law**: Indemnification is not a native concept in many systems; may be interpreted
  as guarantee or penalty clause [VERIFY]

### 10. Limitation of Liability

**Key elements to review:**

- Cap amount (fixed amount, multiple of fees, or uncapped)
- Whether cap is mutual or asymmetric
- Carveouts from the cap (what liabilities are uncapped)
- Consequential damages exclusion
- Carveouts from consequential damages exclusion
- Per-claim vs. aggregate cap

**Common issues:**

- No liability cap (unlimited exposure)
- Cap at a fraction of fees (too low relative to risk)
- Asymmetric carveouts favoring one party
- Broad carveouts that effectively eliminate the cap
- No consequential damages exclusion
- Consequential damages exclusion without carveouts for key risks

**Standard position (market norm):**

- Mutual liability cap at 12-24 months of fees paid or payable under the agreement
- Carveouts for: fraud/willful misconduct, indemnification obligations, breach of
  confidentiality, breach of IP provisions, death/personal injury from negligence
- Mutual exclusion of consequential, indirect, special, and punitive damages
- Carveouts from exclusion for confidentiality breach, IP infringement, and willful misconduct

[JURISDICTION-SPECIFIC] Key variations:

- **UK (UCTA)**: Exclusion clauses must be reasonable. Cannot exclude liability for death/
  personal injury from negligence [VERIFY]
- **Civil law**: Cannot exclude liability for gross negligence (grobe Fahrlassigkeit) or
  intentional misconduct (Vorsatz) in many jurisdictions [VERIFY]
- **Consumer contracts**: Additional mandatory protections typically apply [VERIFY]

### 11. Independent Contractor Status

**Key elements to review:**

- Express statement that relationship is independent contractor, not employment
- Control over work methods and schedule
- Tax and benefits responsibility
- No authority to bind the other party
- Substitution rights
- Non-exclusivity

**Common issues:**

- Language suggesting employer-like supervision and control
- No tax responsibility allocation
- Exclusive engagement without independent contractor carve-out
- No substitution right (suggests employment relationship)
- Benefits expectations language

**Standard position (market norm):**

- Clear independent contractor statement
- Consultant controls own work methods, schedule, and place of work
- Consultant responsible for own taxes, benefits, and insurance
- No authority to bind client without written authorization
- Right to substitute personnel (subject to qualifications and client approval)
- Non-exclusive (consultant may provide services to others, subject to confidentiality)

[JURISDICTION-SPECIFIC] Key variations:

- **US**: Multi-factor tests vary by state and purpose (IRS, DOL, state labor law). ABC test
  in California (AB5) presumes employment [VERIFY]
- **UK**: Employment status tests focus on mutuality of obligation, control, and personal
  service. IR35 rules for tax purposes [VERIFY]
- **EU**: Each member state has different classification tests. Increasing regulatory
  attention to gig economy classification [VERIFY]

### 12. Non-Compete and Non-Solicit

**Key elements to review:**

- Non-compete scope (competing services, competing clients)
- Non-solicit of employees
- Non-solicit of clients
- Geographic scope
- Duration
- Consideration (especially for post-termination restrictions)

**Common issues:**

- Overbroad non-compete preventing consultant from practicing profession
- Non-compete without compensation (unenforceable in many jurisdictions)
- Non-solicit of employees that captures general hiring
- Geographic scope exceeding business necessity
- Duration exceeding what is enforceable

**Standard position (market norm):**

- Non-compete: limited to specific competing clients during engagement and for 6-12 months
  after (if enforceable in jurisdiction)
- Non-solicit of employees: mutual, 12-24 months, limited to active solicitation
- Non-solicit of clients: consultant may not solicit client's customers for competing
  services during engagement
- Compensation for post-termination non-compete where required by law

[JURISDICTION-SPECIFIC] Key variations:

- **California**: Non-competes generally unenforceable (except for business sale) [VERIFY]
- **UK**: Post-termination restraints require consideration and must be reasonable in scope
  and duration to protect legitimate business interests [VERIFY]
- **Germany**: Post-termination non-competes require compensation (at least 50% of most
  recent compensation) [VERIFY]
- **Many US states**: Garden leave provisions and blue pencil rules vary significantly [VERIFY]

### 13. Governing Law and Disputes

**Key elements to review:**

- Choice of law
- Forum selection (exclusive or non-exclusive)
- Arbitration clause (if disputes go to arbitration)
- Arbitration institution and rules
- Injunctive relief exception
- Prevailing party fees

**Common issues:**

- No governing law clause
- Governing law disconnected from parties or services
- Exclusive jurisdiction in inconvenient forum
- Arbitration without injunctive relief carve-out
- Unclear arbitration clause

**Standard position (market norm):**

- Governing law of jurisdiction with connection to at least one party
- Non-exclusive jurisdiction (allows flexibility)
- If arbitration, carve-out for injunctive relief in courts
- Standard arbitration institution (AAA, JAMS, ICC, LCIA)

### 14. General Boilerplate

**Key elements to review:**

- Assignment restrictions
- Subcontracting rights
- Force majeure
- Notices provisions
- Amendment requirements
- Entire agreement/integration
- Severability
- Waiver
- Counterparts and electronic signatures
- Order of precedence (if multiple documents)

**Common issues:**

- Assignment permitted without consent (allows change of counterparty)
- Subcontracting without accountability
- Force majeure that excuses all performance indefinitely
- Notice provisions with incorrect addresses
- No entire agreement clause (allows parol evidence)
- Conflicting terms across documents with no order of precedence

---

## Deviation Severity Classification

### GREEN — Acceptable

The clause aligns with or is better than the standard position. Minor variations that are
commercially reasonable and do not materially increase risk.

**Consulting Agreement Examples:**

- Liability cap at 18 months fees when standard is 12 months (better)
- Net 45 payment when standard is Net 30 (slightly worse but acceptable)
- Confidentiality survival of 3 years when standard is 5 years (shorter but reasonable)

**Action**: Note for awareness. No negotiation needed.

### YELLOW — Negotiate

The clause falls outside the standard position but within a negotiable range.

**Consulting Agreement Examples:**

- Liability cap at 6 months fees when standard is 12 months
- All IP automatically assigned to client without tools carve-out
- No termination for convenience (locked in)
- Non-compete broader than necessary but with reasonable duration
- No change control mechanism in SOW

**Action**: Generate specific redline language. Provide fallback position. Estimate
business impact.

### RED — Escalate

The clause falls outside the acceptable range or poses material risk.

**Consulting Agreement Examples:**

- No liability cap (unlimited exposure)
- Unilateral broad indemnification with no cap
- IP assignment of consultant's pre-existing tools and methodologies
- No independent contractor language (classification risk)
- No payment for work on termination for convenience
- Overbroad non-compete that prevents consultant from practicing
- No governing law clause
- Processing personal data without DPA

**Action**: Explain the specific risk. Provide market-standard alternative language.
Recommend escalation path.

---

## Redline Format

For each redline:

```
**Clause**: [Section reference and clause name]
**Current language**: "[exact quote from the agreement]"
**Proposed redline**: "[specific alternative language]"
**Rationale**: [1-2 sentences explaining why, suitable for external sharing]
**Legal basis**: [Relevant statute, regulation, or principle — or "General commercial practice"]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative position if primary redline is rejected]
```

---

## Negotiation Priority Framework

### Tier 1 — Must-Haves (Deal Breakers)

- Limitation of liability clause (with reasonable cap)
- Clear scope definition with change control
- IP ownership clarity (consultant retains pre-existing tools)
- Independent contractor status language
- Payment for work performed through termination
- Data protection terms if personal data processed

### Tier 2 — Should-Haves (Strong Preferences)

- Termination for convenience (with reasonable notice)
- Liability cap at 12+ months fees
- Mutual confidentiality
- Reasonable non-compete scope
- Cure period for termination for cause
- Change control mechanism

### Tier 3 — Nice-to-Haves (Concession Candidates)

- Preferred governing law
- License back for portfolio use
- Expense approval thresholds
- Specific payment terms
- Notice period preferences

---

## Quality Assurance Framework

### Citation Quality Gates

| Gate           | Rule                                                    | Fail Action                         |
| -------------- | ------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every legal claim cites a specific statute or principle | Add citation or mark "[UNVERIFIED]" |
| **Format**     | All citations follow consistent format                  | Fix format                          |
| **Currency**   | Every cited provision checked for amendments            | Flag "[CHECK CURRENCY]"             |
| **Domain**     | Analysis stays within the agreement's governing law     | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated                           | Add confidence qualifier            |

### Self-Interrogation for RED Items

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the
cited authority?

**Pass 2 — Completeness**: Have all relevant statutes been considered?

**Pass 3 — Challenge**: What is the strongest argument that this clause IS acceptable?

### Confidence Scoring

| Level        | Range     | Meaning                           | Action                            |
| ------------ | --------- | --------------------------------- | --------------------------------- |
| **Definite** | 0.95-1.0  | Settled law, clear statute        | State with confidence             |
| **High**     | 0.80-0.94 | Strong authority, minor questions | State with brief caveat           |
| **Probable** | 0.60-0.79 | Good arguments but could differ   | State with reasoning              |
| **Possible** | 0.40-0.59 | Genuinely uncertain               | Flag for counsel review           |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative           | Do not assert; flag "[UNCERTAIN]" |

---

## Glass Box Audit Trail

```yaml
glass_box:
  document: "[Agreement title and date]"
  document_type: "Consulting Agreement"
  user_side: "[Client / Consultant]"
  governing_law: "[Jurisdiction]"
  playbook_used: "[Playbook name or 'General commercial standards']"
  clauses_reviewed: 14
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations or caveats]"
  reviewer: "AI-assisted — requires qualified legal review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in consulting agreement drafting and review:

1. **Treating scope as "we'll figure it out"** — A consulting agreement without clear scope
   definition creates disputes about what was promised and what is additional. Always define
   deliverables, acceptance criteria, and change control.

2. **Ignoring classification risk** — In jurisdictions with strict worker classification
   tests, a consulting agreement that looks like employment creates liability for both
   parties. Include proper independent contractor language and structure the relationship
   accordingly.

3. **All-or-nothing IP assignment** — Automatically assigning all IP to the client captures
   the consultant's pre-existing tools, templates, and methodologies. Always carve out
   background IP and general know-how.

4. **Work-for-hire overreach** — Using work-for-hire language for works that do not qualify
   under US copyright law creates false comfort. If the work does not fit a statutory
   category and there is no employee relationship, you need an explicit assignment.

5. **No liability cap** — A consulting engagement with no liability cap exposes the
   consultant to unlimited risk for a limited fee. Always include a cap proportionate
   to the engagement value.

6. **Liability cap at one month's fees** — While a cap exists, it may be too low to provide
   meaningful protection for the client if something goes wrong. Standard is 12-24 months.

7. **Termination for convenience without payment** — If the client can terminate at will
   without paying for work in progress, the consultant bears all downside risk. Payment for
   work performed should survive termination for convenience.

8. **Perpetual non-compete** — A non-compete with no time limit, or one that prevents the
   consultant from practicing their profession, is likely unenforceable and signals bad faith.

9. **Ignoring data protection** — If the consultant will access personal data, data
   protection requirements apply regardless of whether the agreement addresses them.
   The absence of a DPA does not eliminate GDPR obligations.

10. **Applying US concepts globally** — Work-for-hire is a US doctrine. California non-compete
    rules are California law. Do not assume US concepts apply under foreign governing law.

11. **SOW without master agreement alignment** — If the SOW has different terms than the
    master agreement, conflicts arise. Always include clear order of precedence.

12. **Expenses without controls** — Unlimited expense reimbursement or expense reimbursement
    without approval thresholds creates cost overrun risk. Define what is reimbursable and
    approval requirements.

13. **One-sided indemnification** — Requiring the consultant to indemnify for "any claim"
    including those arising from client materials or specifications is unreasonable. Mutual
    indemnification with appropriate carve-outs is standard.

14. **Reviewing without knowing the engagement type** — A fixed-scope project has different
    risk profile than an ongoing advisory retainer. Confirm the engagement structure before
    assessing clause adequacy.

15. **Ignoring tax implications** — Cross-border consulting engagements have complex tax
    implications (permanent establishment, withholding, VAT). The agreement should address
    tax responsibility clearly.

---

## Writing Standards

Apply plain-language discipline to all output:

**For redline rationales** (shared with counterparty):

- Plain language, no jargon
- Active voice
- Short sentences, one point per sentence
- Specific, not vague

**Quality gates before delivery**:

1. Can a business stakeholder understand the executive summary?
2. Can counterparty's counsel respond to each redline?
3. Is every legal claim backed by citation (or flagged [VERIFY])?
4. Could any sentence be shorter without losing meaning?

---

## External Tool Integration

**With legalcode-mcp connected:**

- Search for jurisdiction-relevant worker classification tests, IP ownership rules,
  limitation of liability enforceability, and non-compete standards
- Mark all legalcode-mcp citations as VERIFIED in Glass Box

**Without legalcode-mcp:**

- Mark all statutory references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Focus on commercial risk assessment

---

## Output Format Template

```markdown
## Consulting Agreement Review Summary

**Document**: [agreement name/identifier]
**Parties**: [party names and roles]
**Your Side**: [Client / Consultant]
**Governing Law**: [jurisdiction]
**Engagement Type**: [fixed-scope / retainer / MSA+SOW]
**Review Basis**: [Playbook / General Standards]
**Date of Review**: [date]

---

## Key Findings

[Top 3-5 issues with severity flags and summaries]

---

## Missing Clauses

[List missing clause categories with severity]

---

## Clause-by-Clause Analysis

### [Clause Category] — [GREEN / YELLOW / RED] | Confidence: [level]

**Agreement says**: [summary]
**Standard position**: [market standard]
**Deviation**: [gap description]
**Business impact**: [practical impact]
**Redline** (if YELLOW or RED):

> [Proposed language]

[Repeat for each clause]

---

## Negotiation Strategy

**Tier 1 (Must-Haves)**: [list]
**Tier 2 (Should-Haves)**: [list]
**Tier 3 (Concession Candidates)**: [list]

**Recommended approach**: [strategy]

---

## Next Steps

[Specific actions]

---

## Glass Box Audit Trail

[YAML block]
```

---

## Localization Notes

To create a jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with local legal content
2. Replace [VERIFY] tags with verified statutory references
3. Add jurisdiction-specific clause considerations (e.g., IR35 for UK, AB5 for California)
4. Add jurisdiction-specific anti-patterns
5. Update frontmatter to reference the specific jurisdiction

---

## Provenance

Enhanced by Legalcode (2026-03-01). Original skill created 2026-02-27 as jurisdiction-
agnostic baseline. This version upgraded to Legalcode quality standard with:

- Multi-step interactive workflow with CLARIFY points
- Deep clause analysis for 14 categories with severity classification
- Citation Quality Gates, Self-Interrogation, and Confidence Scoring
- Glass Box audit trail for traceability
- 15-item anti-patterns catalogue
- Writing standards and output format template
- External tool integration with graceful degradation
