---
name: legalcode-ip-assignment-agreement
description: Review and draft intellectual property assignment agreements transferring ownership of patents,
  copyrights, trademarks, trade secrets, and know-how. Use when reviewing or drafting IP assignments in
  employment contexts (invention assignment clauses, employee IP provisions), contractor engagements (consultant
  IP transfer, freelancer work product), M&A transactions (IP due diligence, founder IP transfer, pre-incorporation
  assignment remediation), technology transfers (source code assignment, software IP, algorithm transfer),
  and corporate reorganizations (intra-group IP transfer, spin-off IP allocation).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review and draft intellectual property assignment agreements transferring ownership of patents, copyrights, trademarks, trade secrets, and know-how. Use when reviewing or drafting IP assignments in employment contexts (invention assignment clauses, employee IP provisions), contractor engagements (consultant IP transfer, freelancer work product), M&A transactions (IP due diligence, founder IP transfer, pre-incorporation assignment remediation), technology transfers (source code assignment, software IP, algorithm transfer), and corporate reorganizations (intra-group IP transfer, spin-off IP allocation). Covers assignment vs. license distinction, present vs. future rights assignment language ("hereby assign" vs. "agree to assign"), work-for-hire doctrine (17 USC 101 nine categories, Community for Creative Non-Violence v. Reid 1989), moral rights treatment (VARA in US, CDPA 1988 s.77-89 in UK, French droit moral, German Urheberpersonlichkeitsrecht), assignment formalities by jurisdiction (USPTO/ UKIPO/EUIPO/EPO recordation, writing requirements, signature requirements, witness/ notarization), chain-of-title verification, background IP carve-outs, future improvements/derivatives, consideration requirements, warranty of title and non-infringement, further assurance clauses, confidentiality of transferred IP, state-specific inventor protections (California Labor Code 2870, Illinois EPAA, Washington RCW 49.44.140, Minnesota 181.78). GREEN/YELLOW/RED classification with confidence-scored analysis. Jurisdictions: US (federal copyright/patent/trademark, 50-state employment IP), UK (CDPA 1988, Patents Act 1977), EU (Copyright Directive 2019/790, Trade Secrets Directive 2016/943, EPO/EUIPO practice), common law and civil law moral rights treatment. Usefulness: 9/10.


# Legalcode IP Assignment Agreement

> **Disclaimer**: This skill provides a framework for AI-assisted intellectual property
> assignment agreement review and drafting. It does not constitute legal advice. All
> outputs should be reviewed by a qualified legal professional licensed in the relevant
> jurisdiction before use. Laws change; verify current applicability before relying on
> any provision described here. Statutory and case law references cited from memory
> carry hallucination risk — verify against authoritative sources before relying on them.
> IP assignments involve complex jurisdiction-specific formalities and can have
> significant commercial consequences if executed improperly.

## Purpose and Scope

This skill reviews and drafts intellectual property assignment agreements — contracts
that transfer ownership of patents, copyrights, trademarks, trade secrets, and know-how
from one party (the assignor) to another (the assignee). Unlike licenses, which grant
permission to use IP while the original owner retains title, assignments permanently
transfer all ownership rights.

**Covers:**

- Employee invention assignment agreements and IP clauses in employment contracts
- Contractor/consultant IP assignment provisions
- Founder IP assignments (pre-incorporation and post-formation)
- Technology transfer agreements (software, algorithms, source code)
- M&A transaction IP assignments and due diligence
- Intra-group IP transfers in corporate reorganizations
- Copyright, patent, trademark, trade secret, and know-how assignments
- Moral rights waivers and consents (where permitted)
- Assignment formality compliance (writing, signature, recordation)
- Chain-of-title verification and gap remediation

**Does not:**

- Provide legal advice or replace qualified IP counsel
- Draft patent applications or trademark registrations
- Conduct freedom-to-operate searches
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers
- Cover pure licensing transactions (see licensing-specific skills)

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The agreement's governing law clause determines
which legal framework applies. IP rights are territorial — a US patent must be assigned
under US law, a UK trademark under UK law — so multi-jurisdictional assignments require
compliance with each relevant jurisdiction's formalities.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- Assignment writing requirements (most require signed writing; some require both parties)
- Recordation requirements and timing (USPTO, UKIPO, EUIPO, EPO, WIPO, national offices)
- Work-for-hire doctrine availability (US-specific; does not exist in most jurisdictions)
- Moral rights treatment (inalienable in France/Germany; waivable in US/UK)
- Employee invention ownership defaults and assignment limitations
- Consideration requirements (some jurisdictions require nominal consideration)
- Witness or notarization requirements
- State/provincial inventor protection statutes (California, Illinois, Washington, etc.)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- Multiple valid approaches exist and the user's preference matters
- Ambiguity in the agreement creates a fork that only the user can resolve
- Risk tolerance or business context is needed to classify severity correctly
- Assignment formalities vary significantly by jurisdiction

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

### Step 1: Accept the Input

Accept the input in any of these formats:

**For review mode:**

- **File**: PDF, DOCX, or other document format containing an existing IP assignment
- **URL**: Link to a document in a CLM, cloud storage, or document system
- **Pasted text**: IP assignment text pasted directly into the conversation
- **Employment contract excerpt**: IP assignment clause from a broader agreement

**For drafting mode:**

- **Drafting brief**: Description of what needs to be assigned, parties, and context
- **Term sheet**: Summary of agreed business terms for the assignment
- **Template request**: Request for a standard-form assignment for a specific context

If no input is provided, prompt the user to supply one.

### Step 2: Gather Context

**CLARIFY** — Before beginning the review or draft, ask the user these questions.
Present them as a structured set of options where possible:

1. **Mode**: Review or draft?
   - Options: **Review an existing IP assignment agreement**, **Draft a new IP assignment**
   - _Why this matters_: Determines whether to analyze an existing document or create one.

2. **Transaction context**: What is the purpose of this IP assignment?
   - Options:
     - **Employment**: IP assignment clause in employment agreement or invention assignment
     - **Contractor**: IP assignment from independent contractor or consultant
     - **Founder**: Founder assigning pre-incorporation IP to the company
     - **M&A**: IP assignment as part of an acquisition or asset sale
     - **Technology transfer**: Standalone IP sale or technology transfer
     - **Corporate reorganization**: Intra-group transfer or spin-off
     - **Other**: [describe]
   - _Why this matters_: Different contexts trigger different clauses, formalities, and risks.

3. **Which side are you on?**
   - Options: **Assignor** (transferring IP), **Assignee** (receiving IP)
   - _Why this matters_: Analysis and drafting recommendations differ based on perspective.

4. **IP types involved**: What types of intellectual property are being assigned?
   - Options: Patents/patent applications, Copyrights (software, content, designs), Trademarks/
     service marks, Trade secrets/confidential information, Know-how/technical expertise,
     Domain names, All of the above, Other
   - Allow multiple selections.
   - _Why this matters_: Different IP types have different formality requirements and
     considerations.

5. **Jurisdiction(s)**: Where are the IP rights registered or where do they need protection?
   - Options: US only, UK only, EU (multiple member states), Multi-jurisdictional (specify),
     Unclear/worldwide
   - _Why this matters_: Assignment formalities and requirements vary by jurisdiction.

6. **Deal context**: Relevant business context?
   - Free text. Prompt with examples: deal size, strategic importance, existing relationship,
     timeline, whether this is template or one-off, any red flags already identified.
   - _Why this matters_: Context determines depth of review and risk tolerance.

If the user provides partial context, proceed with what you have but **state your
assumptions explicitly**. Do not silently assume.

### Step 3: Load Any Playbook

Check for the organization's IP assignment playbook or standard positions in local
settings (e.g., `legal.local.md` or similar configuration files).

The playbook should define:

- Standard IP assignment language for employees vs. contractors
- Background IP carve-out approach
- Moral rights waiver requirements
- Required warranties and representations
- Formality compliance checklist by jurisdiction

**If no playbook is configured:**

**CLARIFY** — Inform the user that no playbook was found, and ask which approach to take:

- **Option A: Set up positions now** — Walk through defining the organization's standard
  IP assignment requirements. Takes time but makes future reviews consistent.
- **Option B: Proceed with market standards** — Use widely-accepted IP assignment best
  practices as the baseline.
- **Option C: I'll provide positions as we go** — Ask about preferences when they matter.

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Identify the governing law and applicable IP jurisdictions. Then use **legalcode-mcp**
to build a working legal reference file.

**Research process:**

1. **Identify jurisdictions** from the agreement and IP rights involved. Consider:
   - Governing law of the agreement
   - Countries where patents are registered/pending
   - Countries where copyrights need protection
   - Countries where trademarks are registered
   - Employee/contractor location (for employment-related assignments)

2. **Search legalcode-mcp** for jurisdiction-relevant authority across these categories:
   - Assignment writing and formality requirements by jurisdiction
   - Work-for-hire doctrine scope and limitations (US)
   - Moral rights treatment and waiver possibilities
   - Employee invention statutes and protections
   - Recordation requirements and timing (USPTO, UKIPO, EUIPO, EPO)
   - Consideration requirements for valid assignment
   - Leading case law on assignment interpretation and validity

3. **Save the most relevant results** to `/tmp/legalcode-ip-assignment-authority.md`

**If legalcode-mcp is not connected:**

- Mark every statutory and case law reference with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with the analysis using general IP knowledge

### Step 5: Document Analysis (Review Mode)

For review mode, analyze the IP assignment agreement systematically. Read the entire
document before flagging issues — clauses interact with each other.

**CLARIFY** — For complex assignments (multiple IP types, multiple jurisdictions,
part of a larger transaction):

- Ask whether to perform a **full review** of all 15 clause categories, or a **priority
  review** focused on the user's stated concerns plus any RED items discovered.
- If the assignment incorporates schedules or exhibits by reference, ask whether those
  should be reviewed as well.

Cover all 15 clause categories below (unless the user opted for a priority review):

| #   | Clause Category                | Depth    | Key Review Points                                                                            |
| --- | ------------------------------ | -------- | -------------------------------------------------------------------------------------------- |
| 1   | Assignment Language            | Deep     | Present vs. future tense, "hereby assign" vs. "agree to assign," scope of rights transferred |
| 2   | IP Identification              | Deep     | Specificity of IP described, registered vs. unregistered, schedules/exhibits                 |
| 3   | Background IP                  | Deep     | Carve-outs, retained licenses, pre-existing IP treatment                                     |
| 4   | Future Improvements            | Deep     | Derivatives, improvements, enhancements, continuation rights                                 |
| 5   | Moral Rights                   | Deep     | Waiver/consent provisions, jurisdiction-specific treatment                                   |
| 6   | Warranties & Representations   | Deep     | Title, non-infringement, no encumbrances, authority                                          |
| 7   | Further Assurance              | Standard | Cooperation obligations, document execution, recordation assistance                          |
| 8   | Consideration                  | Standard | Payment terms, adequacy, timing                                                              |
| 9   | Employee/Contractor Provisions | Standard | Invention assignment scope, state-law compliance, prior inventions                           |
| 10  | Confidentiality                | Standard | Trade secret protection, ongoing obligations                                                 |
| 11  | Recordation                    | Standard | Responsibility, timing, costs, jurisdiction-specific requirements                            |
| 12  | Indemnification                | Standard | IP infringement, breach of warranty, caps                                                    |
| 13  | Governing Law & Disputes       | Standard | Choice of law, venue, arbitration                                                            |
| 14  | Term & Survival                | Standard | Effectiveness, surviving obligations                                                         |
| 15  | Formalities                    | Standard | Signatures, witnesses, notarization, corporate authority                                     |

### Step 6: Draft Structure (Drafting Mode)

For drafting mode, build the IP assignment agreement using the structure below. Gather
all necessary information before drafting.

**Required information for drafting:**

**CLARIFY** — Ask for any missing elements:

1. **Parties**: Full legal names, addresses, corporate form
2. **IP to be assigned**: Detailed description of all IP (patents, copyrights, trademarks,
   trade secrets, know-how), registration numbers if applicable
3. **Background IP**: Any pre-existing IP to be carved out or licensed back
4. **Consideration**: Payment amount, structure, timing
5. **Warranties**: Scope of representations required
6. **Future improvements**: Whether improvements/derivatives are included
7. **Moral rights**: Waiver required? (depends on jurisdiction)
8. **Recordation**: Who is responsible for recording with IP offices?
9. **Special provisions**: Any unusual terms or requirements
10. **Formalities**: Jurisdiction-specific requirements (notarization, witnesses)

**Draft structure:**

```
1. Parties and Recitals
2. Definitions
3. Assignment of Intellectual Property
   - Present assignment language
   - Scope of rights transferred
   - Future improvements/derivatives
4. Scheduled IP (Exhibit A)
5. Background IP Carve-Outs (Exhibit B, if applicable)
6. Moral Rights Waiver/Consent
7. Warranties and Representations
   - Title and ownership
   - Non-infringement
   - No encumbrances
   - Authority to assign
8. Further Assurance
9. Consideration and Payment
10. Confidentiality (if trade secrets involved)
11. Indemnification
12. Recordation
13. Governing Law and Dispute Resolution
14. General Provisions
15. Signature Blocks (with formality compliance)
Exhibits:
   A. Schedule of Assigned IP
   B. Schedule of Background IP (if applicable)
   C. Schedule of Prior Inventions (if employee/contractor context)
```

### Step 7: Clause-by-Clause Analysis

#### 1. Assignment Language

**Critical distinction**: The language used determines whether assignment is immediate
or merely a promise to assign in the future.

**Present assignment (preferred)**:

- "hereby assigns, transfers, and conveys"
- "does hereby grant and assign"
- "hereby sells, assigns, and transfers"

**Future promise (weaker)**:

- "agrees to assign"
- "will assign"
- "shall transfer"

**Common issues:**

- Using future tense creates only an "expectant interest" requiring separate execution
- Ambiguous language that could be interpreted as license rather than assignment
- Failure to assign "all right, title, and interest"
- Omitting specific rights (reproduce, modify, distribute, sublicense, etc.)

**RED flags:**

- No explicit assignment language at all
- Language that could be construed as license ("grants rights to use")
- Assignment conditioned on events that may not occur

[JURISDICTION-SPECIFIC] Key variations:

- **US**: Present assignment language creates immediate transfer upon creation of
  future works (Stanford v. Roche, 563 U.S. 776 (2011)) [VERIFY]
- **UK**: Assignment must be in writing signed by assignor (CDPA 1988 s.90(3)) [VERIFY]
- **Civil law**: Some jurisdictions require identification of specific "fields of
  exploitation" for copyright assignment [VERIFY]

#### 2. IP Identification

The assignment must identify IP with maximum specificity to be enforceable and recordable.

**For registered IP:**

- Patent/application numbers with filing dates and jurisdictions
- Trademark registration numbers with classes and territories
- Copyright registration numbers (where registered)
- Domain name registrations

**For unregistered IP:**

- Detailed descriptions of copyrightable works
- Source code repositories, commit histories
- Trade secret descriptions
- Know-how and technical documentation
- Product names, brand elements, design files

**Common issues:**

- Vague descriptions ("all IP related to the business")
- Missing registration numbers or filing dates
- Failure to include pending applications
- Incomplete territorial scope
- Missing continuation/divisional applications

**RED flags:**

- No schedule or exhibit identifying the IP
- Generic description without specifics
- IP described does not match registration records

#### 3. Background IP

Background IP (or "background technology") is pre-existing IP that should not be
assigned. Proper handling is critical for both parties.

**From assignor's perspective:**

- Carve out all pre-existing IP from the assignment
- Retain ownership of general tools, methodologies, frameworks
- Grant limited license to assignee for use with assigned IP

**From assignee's perspective:**

- Ensure carve-outs are not so broad as to undermine the assignment
- Obtain necessary licenses to use background IP with assigned IP
- Verify background IP is clearly distinguished from assigned IP

**Common issues:**

- No background IP carve-out (assignor loses more than intended)
- Overly broad carve-out (assignee receives less than expected)
- No license granted for background IP needed with assigned IP
- Ambiguity about what constitutes background vs. foreground IP

**For employee/contractor contexts:**
Prior inventions should be listed in a schedule and expressly excluded. See state-law
compliance section below.

#### 4. Future Improvements and Derivatives

**Scope considerations:**

- Does the assignment include improvements made after execution?
- Does it cover derivative works?
- What about continuations, divisionals, reissues of patents?
- Who owns improvements made jointly?

**Common issues:**

- Silent on future improvements (creates uncertainty)
- Overly broad improvement language (captures unrelated work)
- No mechanism for identifying and assigning future IP
- Perpetual improvement assignment obligations on individuals

**RED flags:**

- Unlimited future improvement assignment without consideration
- Assignment of improvements unrelated to the assigned IP
- No termination of future assignment obligations

#### 5. Moral Rights

Moral rights protect authors' personal interests in their works — primarily the right
of attribution (paternity) and the right to object to derogatory treatment (integrity).
Treatment varies significantly by jurisdiction.

| Jurisdiction | Inalienable?                           | Waivable?            | Assignable?  | Key Statute                |
| ------------ | -------------------------------------- | -------------------- | ------------ | -------------------------- |
| US           | No (limited to visual arts under VARA) | Yes                  | No           | 17 USC 106A [VERIFY]       |
| UK           | No                                     | Yes (written waiver) | No           | CDPA 1988 s.77-89 [VERIFY] |
| France       | Yes (perpetual, imprescriptible)       | No                   | No           | CPI Art. L121-1 [VERIFY]   |
| Germany      | Yes (personality rights)               | Limited              | No           | UrhG s.12-14 [VERIFY]      |
| EU generally | Often yes                              | Varies               | Generally no | National law               |

**Common issues:**

- No moral rights waiver in jurisdictions where waiver is required
- Attempting to assign moral rights (not possible in any jurisdiction)
- Waiver language that is not compliant with local requirements
- Silent on moral rights (leaves assignee exposed)

**RED flags:**

- No moral rights provisions in copyright assignment
- Purported assignment of moral rights (void)
- Non-compliant waiver in jurisdictions with formality requirements

[JURISDICTION-SPECIFIC] Key considerations:

- **UK**: Moral rights must be asserted to be effective; waiver should be in writing,
  identify works, and be signed by waiving party (CDPA 1988 s.78, 87) [VERIFY]
- **France**: Any waiver agreement is invalid; obtain consent to specific uses instead
- **Germany**: Waiver of exercise (not the right itself) possible if not "unconscionable"

#### 6. Warranties and Representations

Standard warranties in IP assignments:

**Title and Ownership:**

- Assignor is the sole and exclusive owner
- No co-owners unless disclosed
- Assignment is not subject to any prior transfers

**Non-Infringement:**

- Assigned IP does not infringe third-party rights
- No pending claims or threats
- No known infringement issues

**No Encumbrances:**

- IP is free of liens, security interests, and encumbrances
- No exclusive licenses outstanding
- No restrictions on transfer

**Authority:**

- Assignor has full authority to assign
- Corporate authorizations obtained
- No consents required (or all consents obtained)

**Common issues:**

- Missing or incomplete warranties
- Warranties qualified to point of meaninglessness
- No survival period specified
- No indemnification backing warranties

**RED flags:**

- No title warranty (assignee has no recourse if IP is defective)
- Broad "as is" disclaimer with no warranties
- Disclaimer of knowledge that should be obtainable through diligence

#### 7. Further Assurance

The assignor should commit to executing additional documents needed to:

- Perfect the assignment
- Record ownership changes with IP offices
- Enforce IP rights against infringers
- Obtain registrations in additional jurisdictions

**Common issues:**

- No further assurance clause
- Time-limited cooperation obligations
- No mechanism for assignee to execute documents on assignor's behalf
- Assignor required to bear costs (should typically be assignee)

**Power of attorney**: Consider including a limited power of attorney allowing the
assignee to execute documents on the assignor's behalf if the assignor becomes
unavailable or uncooperative.

#### 8. Consideration

[JURISDICTION-SPECIFIC] Requirements vary:

- **Common law**: Consideration required but can be nominal ("$10 and other good and
  valuable consideration")
- **Some jurisdictions**: Require adequate/fair consideration
- **Employment context**: Employment itself often sufficient consideration for
  invention assignment

**Common issues:**

- No consideration stated (creates validity risk in some jurisdictions)
- Consideration contingent on conditions that may not be met
- Unclear payment timing
- No mechanism for calculating royalties (if applicable)

#### 9. Employee/Contractor Provisions

**Employee invention assignment:**

[JURISDICTION-SPECIFIC] State-law limitations on employee invention assignment:

| State          | Statute            | Protection Scope                                                                   |
| -------------- | ------------------ | ---------------------------------------------------------------------------------- |
| California     | Labor Code 2870    | Inventions on own time, without employer resources, unrelated to business [VERIFY] |
| Illinois       | EPAA 765 ILCS 1060 | Similar to California [VERIFY]                                                     |
| Washington     | RCW 49.44.140      | Inventions on own time, without employer resources [VERIFY]                        |
| Minnesota      | 181.78             | Inventions on own time, without employer resources [VERIFY]                        |
| Delaware       | DUTA               | Inventions on own time if unrelated to business [VERIFY]                           |
| North Carolina | NCGS 66-57.1       | Similar protections [VERIFY]                                                       |

**Required provisions:**

- Notice to employee of state-law protections
- Schedule of prior inventions (Exhibit C)
- Disclosure procedure for new inventions
- Determination process for ownership disputes

**Contractor IP assignment:**

Contractors retain default IP ownership unless expressly assigned. Work-for-hire
doctrine has limited application to contractors.

**Common issues:**

- Missing state-law compliance notice
- No prior inventions schedule
- Overly broad invention assignment (capturing unrelated work)
- No invention disclosure procedure
- Unclear treatment of inventions made on personal time

**RED flags:**

- Employment agreement silent on IP (creates ambiguity)
- Assignment purporting to capture inventions protected by state law
- No prior inventions disclosure procedure

#### 10. Confidentiality

Critical for trade secret assignments:

- Define confidential information to include the assigned trade secrets
- Maintain confidentiality obligations even after assignment
- Require assignee to maintain reasonable security measures
- Address employee/contractor awareness and acknowledgment

**Common issues:**

- No confidentiality provisions for trade secret assignment
- Confidentiality obligations that terminate at assignment
- No security requirements for assignee
- Trade secrets disclosed without appropriate protections

#### 11. Recordation

Recording assignments with IP offices establishes public notice and protects against
subsequent transferees. Requirements vary by jurisdiction and IP type.

| IP Office           | Requirement               | Timing                                         | Fee                      |
| ------------------- | ------------------------- | ---------------------------------------------- | ------------------------ |
| USPTO (Patents)     | Form PTO-1595 or AIA      | Within 3 months to avoid subsequent BFP issues | $50-100 [VERIFY]         |
| USPTO (Trademarks)  | Electronic recordation    | Promptly; no statutory deadline                | $25-50 per mark [VERIFY] |
| US Copyright Office | Form DCS or online        | No deadline but affects remedies               | $125+ [VERIFY]           |
| UKIPO (Patents)     | Form 21 with evidence     | Within 6 months to preserve remedies           | Free [VERIFY]            |
| UKIPO (Trademarks)  | Form TM16                 | No deadline but advisable promptly             | GBP 50 [VERIFY]          |
| EUIPO (EUTM)        | Application with evidence | Promptly for third-party effect                | EUR 200 [VERIFY]         |
| EPO                 | Form 5050 or equivalent   | During prosecution; national phase varies      | Varies [VERIFY]          |

**Common issues:**

- Silent on who is responsible for recordation
- No timing requirements
- Costs not allocated
- Missing documents needed for recordation

#### 12. Indemnification

**Typical indemnification provisions:**

**From assignor:**

- Breach of title warranty (IP was not owned)
- Infringement claims based on pre-assignment use
- Third-party claims arising from assignor's conduct

**From assignee:**

- Infringement claims based on post-assignment use
- Third-party claims arising from assignee's modifications

**Common issues:**

- No indemnification provisions
- Uncapped indemnification
- No notice and cooperation requirements
- No right to control defense

#### 13. Governing Law and Dispute Resolution

**Key considerations:**

- Governing law should be consistent with IP jurisdictions
- Consider arbitration for confidentiality
- Venue selection for enforcement practicality
- Multi-jurisdictional enforcement considerations

#### 14. Term and Survival

**Effectiveness:**

- When does the assignment take effect?
- Conditions precedent (payment, regulatory approval)

**Survival:**

- Warranties typically survive for a defined period
- Indemnification survives termination
- Confidentiality obligations for trade secrets
- Further assurance obligations

#### 15. Formalities Compliance

**Signature requirements:**

- Written document required for all IP assignments
- Assignor signature required in all jurisdictions
- Both parties' signatures required for some EU jurisdictions
- Witness or notarization in some cases

**Corporate authority:**

- Board resolution or authorization
- Certificate of incumbency
- Secretary's certification

**Additional requirements:**

- Patent assignments may require specific forms
- Trademark assignments should include goodwill
- Copyright assignments should identify specific works

---

## Deviation Severity Classification

### GREEN — Acceptable

The clause aligns with or exceeds standard market practice. Minor variations that are
commercially reasonable and do not create material risk.

**Examples:**

- Assignment language uses "hereby assigns" (present tense)
- All registered IP specifically identified with registration numbers
- Comprehensive title warranty with reasonable survival period
- Appropriate moral rights waiver for the jurisdiction
- Clear background IP carve-out with necessary license

**Action**: Note for awareness. No changes needed.

### YELLOW — Negotiate

The clause falls outside standard practice but within a negotiable range. Requires
attention and likely negotiation.

**Examples:**

- Future tense assignment language ("agrees to assign") — fixable but weaker
- IP identification lacks some specifics but generally adequate
- Warranty scope narrower than standard but acceptable
- Moral rights waiver missing but obtainable
- Background IP carve-out broader than expected
- Further assurance limited to defined period
- Consideration unclear but parties can clarify

**Action**: Generate specific redline language. Provide fallback position. Estimate
risk of accepting vs. negotiating.

### RED — Escalate

The clause falls outside acceptable range, triggers escalation, or poses material risk.
Requires senior counsel review or decision-maker sign-off.

**Examples:**

- No assignment language at all (document may be a license)
- IP description so vague as to be unrecordable
- No title warranty (assignee has no recourse)
- Purported assignment of moral rights (void in all jurisdictions)
- Assignment of pre-existing IP beyond intended scope
- Missing state-law compliance for employee invention assignment
- No consideration in jurisdiction requiring it
- Assignment conditioned on events that may not occur
- Chain-of-title gap with no remediation
- Formality defects that could invalidate the assignment

**Action**: Explain the specific risk with legal basis. Provide market-standard
alternative language. Estimate exposure. Recommend escalation path.

---

## Redline Format

For each redline:

```
**Clause**: [Section reference and clause name]
**Current language**: "[exact quote from the agreement]"
**Proposed redline**: "[specific alternative language]"
**Rationale**: [1-2 sentences suitable for external sharing]
**Legal basis**: [Relevant statute, principle, or "Market standard practice"]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative position if primary redline is rejected]
```

### Redline Best Practices

1. **Be specific**: Provide exact language ready to insert
2. **Be balanced**: Firm on critical points, commercially reasonable otherwise
3. **Explain the rationale**: Professional explanation suitable for counterparty
4. **Provide fallback positions**: Alternatives if primary ask is rejected
5. **Prioritize**: Indicate must-haves vs. nice-to-haves
6. **Reference applicable law**: Cite relevant statutes or principles

---

## Negotiation Priority Framework

### Tier 1 — Must-Haves (Deal Breakers)

Issues where the transaction cannot proceed without resolution:

- Present-tense assignment language ("hereby assign")
- Specific identification of all material IP
- Title warranty covering ownership and non-infringement
- Moral rights waiver/consent (where applicable)
- State-law compliance for employee/contractor assignments
- Consideration (where required by law)
- Formality compliance (signatures, writing)
- Chain-of-title integrity

### Tier 2 — Should-Haves (Strong Preferences)

Issues that materially affect value but have negotiation room:

- Comprehensive warranty scope
- Further assurance obligations
- Background IP carve-out clarity
- Future improvements treatment
- Indemnification provisions
- Recordation responsibilities
- Confidentiality for trade secrets

### Tier 3 — Nice-to-Haves (Concession Candidates)

Issues that improve position but can be traded strategically:

- Preferred governing law
- Specific dispute resolution venue
- Enhanced cooperation periods
- Additional insurance requirements
- Audit rights

**Negotiation strategy**: Lead with Tier 1 items — these are non-negotiable for a valid
assignment. Trade Tier 3 concessions to secure Tier 2 wins.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise.

| Gate           | Rule                                                                 | Fail Action                         |
| -------------- | -------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or principle | Add citation or mark "[UNVERIFIED]" |
| **Format**     | All citations follow consistent format for the jurisdiction          | Fix format                          |
| **Currency**   | Provisions checked for amendments or repeal                          | Flag "[CHECK CURRENCY]"             |
| **Domain**     | Analysis stays within relevant IP law scope                          | Remove jurisdictional bleed         |
| **Confidence** | Uncertainty explicitly stated                                        | Add confidence qualifier            |

### Self-Interrogation for RED Items

For any clause classified as RED, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**:

- Does the risk assessment follow logically from the statute/principle cited?
- Would a court in this jurisdiction reach this conclusion on these facts?
- Is there a counter-argument the counterparty's counsel will make?

**Pass 2 — Completeness**:

- Have all relevant IP-specific statutes been considered?
- Have any relevant cases or principles been missed?
- Are there formality requirements not yet considered?

**Pass 3 — Challenge**:

- What is the strongest argument that this clause IS acceptable?
- Under what circumstances might a reasonable IP lawyer accept this risk?
- Is the RED classification proportionate, or is this actually YELLOW with mitigations?

### Confidence Scoring

| Level        | Range     | Meaning                           | Action                                     |
| ------------ | --------- | --------------------------------- | ------------------------------------------ |
| **Definite** | 0.95-1.0  | Settled law, clear statute        | State with confidence                      |
| **High**     | 0.80-0.94 | Strong authority, minor questions | State with brief caveat                    |
| **Probable** | 0.60-0.79 | Good arguments but could differ   | State with reasoning and contra-indicators |
| **Possible** | 0.40-0.59 | Genuinely uncertain               | Flag for counsel review with both sides    |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative           | Do not assert; flag "[UNCERTAIN]"          |

---

## Glass Box Audit Trail

Every IP assignment review/draft MUST include a Glass Box audit section:

```yaml
glass_box:
  document: "[Agreement title and date]"
  mode: "[Review / Draft]"
  transaction_context: "[Employment / Contractor / Founder / M&A / Tech transfer]"
  user_side: "[Assignor / Assignee]"
  ip_types: "[Patents, Copyrights, Trademarks, Trade secrets, Know-how]"
  jurisdictions: "[List of relevant jurisdictions]"
  governing_law: "[Governing law clause]"
  playbook_used: "[Playbook name or 'Market standards']"
  clauses_reviewed: 15
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  formalities_verified:
    - "[Jurisdiction 1 — Compliant / Non-compliant / Needs review]"
    - "[Jurisdiction 2 — ...]"
  statutes_consulted:
    - "[Statute 1 — VERIFIED or UNVERIFIED]"
  case_law_consulted:
    - "[Case 1 — VERIFIED or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  chain_of_title: "VERIFIED / GAPS IDENTIFIED / NOT REVIEWED"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified IP counsel review"
```

---

## Multi-Stakeholder Mapping

For every IP assignment, identify ALL affected stakeholders:

| Stakeholder           | Role               | Affected Provisions            | Impact                   | Action Required      |
| --------------------- | ------------------ | ------------------------------ | ------------------------ | -------------------- |
| Assignor              | Transferring party | All                            | Primary                  | Execute, cooperate   |
| Assignee              | Receiving party    | All                            | Primary                  | Pay, record          |
| Co-inventors          | Third party        | Assignment, warranties         | May need consent         | Verify assignments   |
| Prior licensees       | Third party        | Scope of assignment            | May have superior rights | Verify no conflicts  |
| Employees/contractors | Third party        | Background IP, confidentiality | Awareness needed         | Obtain assignments   |
| IP offices            | Government         | Recordation                    | Administrative           | File timely          |
| Acquirers (M&A)       | Future party       | Chain of title                 | Diligence target         | Clean chain          |
| Infringers            | Adverse party      | Enforcement rights             | Standing to sue          | Assignment effective |

---

## Anti-Patterns

Explicit catalogue of what NOT to do in IP assignment review/drafting:

1. **Using "agrees to assign" language** — Future tense creates only an expectant
   interest. Courts may not enforce automatic transfer. Always use present-tense
   "hereby assigns" language for immediate effect.

2. **Generic IP descriptions** — "All IP related to the business" is not specific
   enough for recordation or enforcement. List specific registration numbers, works,
   and detailed descriptions for unregistered IP.

3. **Ignoring moral rights** — Every copyright assignment in common law jurisdictions
   should address moral rights. In civil law jurisdictions, understand that waiver may
   be invalid and plan accordingly.

4. **Assuming work-for-hire applies** — Work-for-hire is a US-specific doctrine with
   limited categories. It does not exist in the UK, EU, or most other jurisdictions.
   Do not rely on it for contractors or non-US employees.

5. **Missing state-law compliance** — California, Illinois, Washington, and other
   states protect employee inventions made on personal time. Failing to include
   required notices makes assignment provisions void for protected inventions.

6. **No background IP carve-out** — Assignors should retain their pre-existing IP.
   Without a carve-out, they may inadvertently assign tools, methodologies, or
   frameworks they use across engagements.

7. **Skipping chain-of-title verification** — In M&A, verify that all IP actually
   belongs to the target. Missing founder assignments, contractor agreements, or
   employee invention assignments create gaps that derail transactions.

8. **No further assurance clause** — Assignors become uncooperative or unavailable.
   A further assurance clause with limited power of attorney ensures the assignee can
   complete recordation and enforcement.

9. **Inadequate warranty scope** — "As is" assignments leave assignees with no recourse
   if IP turns out to be defective, encumbered, or infringing. Require title, non-
   infringement, and authority warranties.

10. **No consideration in common law jurisdictions** — While nominal consideration is
    sufficient, complete absence may create validity issues. Include "$10 and other
    good and valuable consideration" or similar.

11. **Ignoring formality requirements** — Different jurisdictions have different
    signature, witness, and notarization requirements. Failing to comply can
    invalidate the assignment.

12. **Not recording promptly** — Delay in recording with IP offices can result in
    losing priority to subsequent bona fide purchasers. Record within 3-6 months.

13. **Conflating assignment with license** — An assignment transfers ownership; a
    license grants permission to use. Using "license" language in an assignment
    creates ambiguity about what was actually transferred.

14. **No trade secret protection provisions** — Trade secrets lose protection if not
    kept confidential. Assignment agreements for trade secrets must include
    confidentiality provisions that survive the assignment.

15. **Over-broad future assignment obligations** — Perpetual obligations to assign
    all future inventions are often unenforceable, especially for individuals after
    employment ends. Limit scope and duration appropriately.

---

## Writing Standards

Apply plain-language discipline to all output:

**For redlines** (shared with counterparty's counsel):

- Plain language. No jargon or filler.
- Active voice: "The Assignor hereby assigns" not "Assignment is hereby made"
- Short sentences. One point per sentence.
- Name the actor explicitly.
- Specific, not vague: cite the relevant IP, provision, or principle.

**For internal analysis**:

- Same plain-language standards
- May include more technical IP analysis
- Confidence qualifiers where appropriate
- Glass Box audit trail appended

**Quality gates before delivery**:

1. Can a non-lawyer business stakeholder understand the executive summary?
2. Can the counterparty's counsel understand and respond to each redline?
3. Is every legal claim backed by a specific citation (or flagged [VERIFY])?
4. Are any phrases vague, hedging, or ambiguous? If yes, fix.
5. Could any sentence be shorter without losing meaning? If yes, shorten.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- Search for jurisdiction-specific IP assignment formalities
- Verify state-law employee invention protections
- Research moral rights treatment by jurisdiction
- Check recordation requirements and timing
- Verify case law on assignment interpretation
- Mark all legalcode-mcp-sourced citations as VERIFIED

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus on structural quality and standard market practices

---

## Output Format Template

### For Review Mode:

```markdown
## IP Assignment Agreement Review Summary

**Document**: [Agreement title and date]
**Parties**: [Assignor] (Assignor) / [Assignee] (Assignee)
**Your Side**: [Assignor/Assignee]
**Transaction Context**: [Employment/Contractor/Founder/M&A/Tech transfer]
**IP Types**: [Patents, Copyrights, Trademarks, Trade secrets, Know-how]
**Jurisdictions**: [List]
**Governing Law**: [Jurisdiction]
**Review Basis**: [Playbook name / Market Standards]
**Date of Review**: [date]

---

## Key Findings

[Top 3-5 issues with severity flags (RED/YELLOW) and one-line summaries]

---

## Missing Elements

[List any critical elements absent from the agreement]

---

## Clause-by-Clause Analysis

### [Clause Category] — [GREEN / YELLOW / RED] | Confidence: [level]

**Agreement says**: [summary]
**Standard position**: [market standard or playbook]
**Deviation**: [description of gap]
**Impact**: [practical consequences]
**Redline** (if YELLOW or RED):

> [Specific proposed language]

[Repeat for each clause category]

---

## Formality Compliance Check

| Jurisdiction   | Requirement   | Status                  | Action Needed |
| -------------- | ------------- | ----------------------- | ------------- |
| [Jurisdiction] | [Requirement] | [Compliant/Gap/Unknown] | [Action]      |

---

## Chain of Title Assessment

[Assessment of IP ownership chain, any gaps identified]

---

## Negotiation Strategy

**Tier 1 (Must-Haves)**: [list]
**Tier 2 (Should-Haves)**: [list]
**Tier 3 (Concession Candidates)**: [list]

**Recommended approach**: [sequencing, tone, strategic trades]

---

## Next Steps

[Specific actions to take, with owners and deadlines if applicable]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

### For Drafting Mode:

```markdown
## IP Assignment Agreement Draft

**Prepared for**: [Client name]
**Transaction Context**: [Employment/Contractor/Founder/M&A/Tech transfer]
**Parties**: [Assignor] / [Assignee]
**IP Types**: [Patents, Copyrights, Trademarks, Trade secrets, Know-how]
**Jurisdictions**: [List]
**Draft Date**: [date]

---

## Draft Agreement

[Full drafted agreement text]

---

## Drafting Notes

[Explanation of key drafting decisions and alternatives considered]

---

## Formality Checklist

| Jurisdiction   | Requirement   | Included | Notes   |
| -------------- | ------------- | -------- | ------- |
| [Jurisdiction] | [Requirement] | [Yes/No] | [Notes] |

---

## Exhibits Required

- Exhibit A: Schedule of Assigned IP
- Exhibit B: Schedule of Background IP (if applicable)
- Exhibit C: Schedule of Prior Inventions (if applicable)

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

This skill is jurisdiction-agnostic by design. To create a jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with verified local law
2. Add jurisdiction-specific formality requirements
3. Include local language versions of key provisions if required
4. Add relevant case law and regulatory guidance
5. Update the frontmatter to reference the specific jurisdiction
6. Add jurisdiction-specific anti-patterns

**Key localization areas:**

- Moral rights treatment (inalienable vs. waivable)
- Work-for-hire doctrine availability
- Employee invention protection statutes
- Recordation requirements and timing
- Signature and formality requirements
- Consideration requirements

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis combining IP assignment best
practices from US, UK, and EU jurisdictions, work-for-hire and moral rights frameworks,
employee invention protection compliance, M&A IP due diligence requirements, and
formality checklists into a comprehensive IP assignment review and drafting skill.

Research sources: Perplexity-search queries on IP assignment best practices (2025-2026),
assignment formalities across jurisdictions, moral rights treatment, work-for-hire
doctrine, employee/contractor IP assignment requirements, M&A IP due diligence issues,
software and trade secret assignment considerations. Repository reference skills:
legalcode-contract-review (structural framework), legalcode-employment-agreement-review
(employee IP patterns).
