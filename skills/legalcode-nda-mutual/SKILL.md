---
name: legalcode-nda-mutual
description: Draft, review, and negotiate mutual non-disclosure agreements (NDAs) for bilateral business
  discussions across jurisdictions. Use when users ask for two-way confidentiality agreements, MNDA templates,
  pre-contract information sharing terms, startup and investor confidentiality clauses, or risk review
  of definition scope, exclusions, term, compelled disclosure, and remedies. Supports playbook-based or
  general-standard review with confidence-scored analysis and auditable output. Jurisdiction-agnostic
  with localization markers for any governing law.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Mutual NDA

> **Disclaimer**: This skill provides a framework for AI-assisted NDA drafting and review.
> It does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before use. Laws change; verify current
> applicability before relying on any provision described here. Statutory and case law
> references cited from memory carry hallucination risk — verify against authoritative
> sources before relying on them.

## Purpose and Scope

This skill drafts, reviews, and negotiates bilateral NDAs where both parties disclose
confidential information during potential commercial, technical, or strategic collaboration.
It identifies deviations from standard positions, classifies their severity, generates
actionable redline suggestions, and produces a confidence-scored, auditable analysis.

**Covers:**

- Standalone mutual NDA agreements
- NDA sections embedded in term sheets or collaboration framework documents
- Pre-diligence and pre-negotiation confidentiality arrangements
- Clause-by-clause analysis with severity classification (GREEN/YELLOW/RED)
- Redline generation with fallback positions
- Missing clause detection and gap analysis
- Quality-verified output with Glass Box audit trail

**Does not:**

- Replace sector-specific legal review for regulated data, trade controls, export
  restrictions, or public procurement confidentiality rules
- Provide legal advice or replace qualified counsel
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The NDA's own governing law clause determines
which legal framework applies. The review identifies the governing law early and adapts
the analysis accordingly.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- Enforceability of injunctive relief language and equitable remedies
- Treatment of residual knowledge clauses under trade secret law
- Limits on confidentiality duration for trade secrets vs. other information
- Public policy restrictions on reverse-engineering bans and non-use restrictions
- Evidentiary and signature formalities for enforcement
- Data protection requirements where personal data is shared under the NDA
- Competition law constraints where information exchange may be sensitive

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- Multiple valid approaches exist and the user's preference matters
- Ambiguity in the NDA creates a fork that only the user can resolve
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

### Step 1: Accept the NDA

Accept the NDA in any of these formats:

- **File**: PDF, DOCX, or other document format
- **URL**: Link to an NDA in a document management system
- **Pasted text**: NDA text pasted directly into the conversation
- **Drafting request**: Request to draft a new mutual NDA from scratch

If no NDA is provided and no drafting request is made, prompt the user to supply one.

### Step 2: Gather Context

**CLARIFY** — Before beginning the review or draft, ask the user these questions.
Present them as a structured set of options where possible:

1. **What is your role?**
   - Options: Disclosing Party (primarily sharing information), Receiving Party (primarily
     receiving information), Mutual (both sides sharing equally), Unsure
   - _Why this matters_: Even in a "mutual" NDA, one party often has more to protect.
     The analysis focuses on protecting the party with more at stake.

2. **What is the purpose of the disclosure?**
   - Options: M&A due diligence, Commercial partnership evaluation, Technology licensing
     discussion, Investment consideration, Employment/consulting negotiation, General
     business discussion, Other (describe)
   - _Why this matters_: The purpose determines scope of permitted use and influences
     which clauses matter most.

3. **What types of information will be shared?**
   - Options: Technical/IP (code, designs, patents), Financial data, Customer lists/data,
     Business strategies, Personal data (triggers data protection), Trade secrets,
     Multiple categories
   - Allow multiple selections.
   - _Why this matters_: Different information types have different protection needs and
     may trigger additional legal requirements (e.g., GDPR for personal data).

4. **Deadline and negotiation posture?**
   - Options: Urgent (days), Standard (1-2 weeks), Flexible (no hard deadline)
   - _Why this matters_: Affects how many issues to surface vs. focus only on critical ones.

5. **Deal context?**
   - Free text. Prompt with examples: deal size, strategic importance, existing relationship,
     whether this is a template or one-off negotiation.
   - _Why this matters_: A pre-acquisition NDA for a $100M deal gets different treatment
     than a standard commercial exploration NDA.

If the user provides partial context, proceed with what you have but **state your
assumptions explicitly** (e.g., "I'm assuming this is for mutual commercial discussions
where both parties will share confidential information equally — let me know if that's
wrong and I'll re-run the analysis"). Do not silently assume.

### Step 3: Load the Playbook

Check for the organization's NDA review playbook in local settings (e.g., `legal.local.md`
or similar configuration files).

The playbook should define:

- **Standard positions**: Preferred terms for each major NDA clause
- **Acceptable ranges**: Terms that can be agreed without escalation
- **Escalation triggers**: Terms that require senior counsel or decision-maker sign-off

**If no playbook is configured:**

**CLARIFY** — Inform the user that no playbook was found, and ask which approach to take:

- **Option A: Set up a playbook now** — Walk through defining the organization's standard
  positions for key NDA clauses (definition scope, term, exclusions, compelled disclosure,
  remedies, residuals). This takes time upfront but makes this and all future reviews
  more precise.
- **Option B: Proceed with general commercial standards** — Use widely-accepted market
  standards as the baseline. Faster, but the review may not reflect the organization's
  specific risk appetite or negotiation history.
- **Option C: I'll provide positions as we go** — Start the review and I'll ask about your
  preferred position when it matters for each clause.

If proceeding without a playbook, clearly label the review: "Based on general commercial
standards — not organizational positions"

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Read the NDA's governing law clause and identify the applicable jurisdiction. Then
use **legalcode-mcp** to build a working legal reference file for this review.

**Research process:**

1. **Identify the governing law** from the NDA (e.g., "laws of the State of California,"
   "English law," "German law").

   **CLARIFY** — If any of the following are true, ask the user before proceeding:
   - **No governing law clause found**: Ask which jurisdiction the user expects to apply,
     and flag the absence as a RED deviation.
   - **Multiple governing law clauses** (e.g., different schedules reference different laws):
     Ask which governs the main body and note the conflict.
   - **Governing law is unusual or unexpected** for the parties (e.g., parties in France
     and Germany choosing Singapore law): Confirm the user is aware and ask whether to
     analyze under the stated law or flag as an issue.

2. **Search legalcode-mcp** for jurisdiction-relevant authority:
   - Trade secret statutes and common law (e.g., DTSA, UTSA in US; Trade Secrets Directive
     in EU; common law duty of confidence in UK)
   - Enforceability of confidentiality duration limits
   - Injunctive relief availability and standards
   - Compelled disclosure procedures and legal privilege rules
   - Residual knowledge clause treatment under trade secret law
   - Reverse engineering restrictions under competition/IP law
   - Personal data processing requirements if personal data is shared

3. **Save the most relevant results** into a local temporary reference file (e.g.,
   `/tmp/legalcode-nda-authority.md`). Structure it as:

   ```markdown
   # Legal Authority Reference — [NDA Name]

   ## Governing Law: [Jurisdiction]

   ## Date Gathered: [date]

   ### Trade Secret Protection

   - [Statute/doctrine, key elements, protection standards]

   ### Confidentiality Duration

   - [Any statutory limits or case law on enforceability]

   ### Injunctive Relief

   - [Standard for obtaining injunctive relief in this jurisdiction]

   ### Compelled Disclosure

   - [Procedures, privilege rules, notification requirements]
   ```

4. **Use this reference file throughout the analysis.** When citing a statute or case in
   your clause analysis, pull from the verified reference file rather than from memory.
   Mark any citation sourced from legalcode-mcp as VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**

- Mark every statutory and case law reference with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with the analysis using general commercial knowledge, but flag that legal
  authority has not been independently verified

### Step 5: Clause-by-Clause Analysis

Analyze the NDA systematically. Read the entire agreement before flagging issues —
clauses interact with each other (e.g., broad definition may be mitigated by robust
exclusions, or vice versa).

**CLARIFY** — For NDAs with unusual structure (e.g., embedded in a term sheet, multiple
schedules, incorporated documents):

- Ask the user whether to perform a **full review** of all 11 clause categories, or a
  **priority review** focused on the user's stated concerns plus any RED items discovered.
- If the NDA incorporates external documents by reference, ask whether those should be
  reviewed as well.

Cover all 11 clause categories below (unless the user opted for a priority review). For
each, assess against the playbook (or general standards) and note whether the clause is
present, absent, or unusual.

| #   | Clause Category                          | Depth    | Key Review Points                                                                                   |
| --- | ---------------------------------------- | -------- | --------------------------------------------------------------------------------------------------- |
| 1   | Definition of Confidential Information   | Deep     | Scope, marking requirements, oral confirmation, catch-all breadth                                   |
| 2   | Exclusions from Confidential Information | Deep     | Public domain, prior possession, independent development, third-party receipt, compelled disclosure |
| 3   | Purpose and Permitted Use                | Deep     | Specificity, limitation to evaluation, scope creep risk                                             |
| 4   | Use Restrictions and Access Controls     | Standard | Need-to-know, affiliate access, advisor carve-outs, flow-down obligations                           |
| 5   | Standard of Care and Security            | Standard | Reasonable care, specific security requirements, incident reporting                                 |
| 6   | Compelled Disclosure                     | Deep     | Notice requirements, cooperation, minimum disclosure, protective order efforts                      |
| 7   | Term and Survival                        | Deep     | Agreement term, confidentiality survival, trade secret perpetual protection                         |
| 8   | Return and Destruction                   | Standard | Timeline, scope, certification, legal retention carve-out                                           |
| 9   | Remedies and Relief                      | Deep     | Injunctive relief, damages, enforceability of remedy language                                       |
| 10  | No License / No Obligation               | Standard | IP reservation, no deal commitment, evaluation rights limits                                        |
| 11  | Governing Law and Disputes               | Standard | Choice of law, forum, arbitration vs. litigation, prevailing party fees                             |

### Step 6: Missing Clause Detection

After analyzing the clauses present, check for important clauses that are entirely absent.
A missing clause can be as significant as a problematic one.

For each of the 11 clause categories:

- If the clause category is entirely absent, flag it
- Assess whether the absence is acceptable or a material gap
- Classify the absence as GREEN (not needed), YELLOW (should be added), or RED (must be added)

Common missing clause issues in NDAs:

- No exclusions from confidential information (RED — unworkable)
- No compelled disclosure procedure (RED — creates impossible compliance situation)
- No term or survival period defined (RED — uncertain obligations)
- No return/destruction obligations (YELLOW — creates post-termination uncertainty)
- No governing law clause (RED — enforcement uncertainty)
- No injunctive relief acknowledgment where beneficial (YELLOW — may affect remedy availability)
- No residual knowledge carve-out where receiving party needs it (YELLOW — operational risk)

**CLARIFY** — When the severity of a missing clause depends on business context:

- "This NDA has no residual knowledge carve-out. Will your personnel be working on similar
  projects after this engagement? If yes, this is a YELLOW gap. If the information is
  highly sensitive and memory-based retention is a concern, the absence may be acceptable."

### Step 7: Flag Deviations

Classify each deviation from the playbook using the three-tier system defined in the
**Deviation Severity Classification** section below. For each deviation:

- **GREEN**: Note for awareness.
- **YELLOW**: Generate specific redline language, provide a fallback position, and estimate
  business impact of accepting vs. negotiating.
- **RED**: Explain the specific risk (citing the legal basis where possible), provide
  market-standard alternative language, estimate exposure, and recommend an escalation path.

**CLARIFY** — For borderline classifications where reasonable minds could differ:

- **YELLOW vs. RED borderline**: "The confidentiality term is 1 year — shorter than the
  typical 2-5 years. For sensitive technical information, this is likely RED (too short
  to provide meaningful protection). For general business information in a short-term
  engagement, this might be YELLOW. Which applies here?"

- **GREEN vs. YELLOW borderline**: "The definition requires marking confidential information
  as 'Confidential' but allows 30 days to confirm oral disclosures. This is more restrictive
  than the typical 'reasonable time' or 'promptly' standard but workable. Is this a concern?"

### Step 8: Generate Redlines

**CLARIFY** — Before generating redlines, ask the user about negotiation posture if not
already clear:

- **Relationship dynamic**: Is this a new counterparty, an existing partner, or a must-have
  deal partner with leverage? This affects tone.
- **Volume of redlines**: If there are many YELLOW items: "I've found [N] items worth
  negotiating. Do you want redlines for all of them, or should I focus on the top [X]
  most impactful ones?"

For each YELLOW and RED deviation, generate a redline using the format in **Redline Format**
below.

### Step 9: Drafting Mode (If Drafting New NDA)

If the user requested a new draft rather than reviewing an existing NDA:

1. **Select template basis**: Use the organization's standard form if available, or generate
   from the clause framework in the **Clause Analysis Reference** section.

2. **Gather specific parameters**:
   - Party names and addresses
   - Effective date
   - Specific purpose of disclosure
   - Desired confidentiality term and survival period
   - Any special provisions (e.g., non-compete, return of materials timeline)

3. **Draft each clause category** following the guidance in the Clause Analysis Reference.
   Mark any choices that require user input with [USER INPUT REQUIRED].

4. **Apply the Quality Verification** before delivering the draft.

### Step 10: Quality Verification

Before delivering the analysis or draft, run the quality checks defined in the **Quality
Assurance Framework** section:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every RED-classified item, run the 3-pass Self-Interrogation. Revise if any pass
   reveals a weakness.
3. Assign a Confidence Score to each material clause analysis.
4. Verify completeness: confirm all 11 clause categories have been addressed (present or
   flagged as missing).
5. Generate the Glass Box Audit Trail and append it to the output.

---

## Clause Analysis Reference

### 1. Definition of Confidential Information

**Key elements to review:**

- Scope of information covered (written, oral, visual, electronic, derivative works)
- Whether marking or designation is required
- Confirmation window for oral disclosures (typically 10-30 days)
- Catch-all language breadth (e.g., "any information that should reasonably be understood
  to be confidential")
- Whether the definition is balanced for both parties

**Common issues:**

- Definition so broad it captures public information or independently known facts
- Marking requirement too strict (all disclosures must be marked at time of disclosure)
- No confirmation mechanism for oral disclosures
- Asymmetric definition favoring one party's information types
- Catch-all that creates uncertainty about what is actually protected

**Standard position (market norm):**

- All information disclosed in connection with the defined purpose, whether written, oral,
  or visual
- Written information should be marked "Confidential" (or similar) at time of disclosure
- Oral information confirmed in writing within 10-30 days
- Reasonable person catch-all for unmarked information that is clearly sensitive

[JURISDICTION-SPECIFIC] Key variations:

- **US (DTSA/UTSA)**: "Trade secret" has specific statutory definition requiring reasonable
  secrecy measures and independent economic value. NDA definition should encompass but is
  broader than trade secrets [VERIFY]
- **EU (Trade Secrets Directive)**: Similar statutory trade secret definition. NDA
  confidential information protection is contractual and can be broader [VERIFY]
- **UK**: Common law duty of confidence applies to information with quality of confidence,
  imparted in circumstances of confidence. Contract can define broader scope [VERIFY]

### 2. Exclusions from Confidential Information

**Key elements to review:**

- Public domain exclusion (information that becomes publicly available without breach)
- Prior possession (information recipient already had before disclosure)
- Independent development (information developed independently without use of disclosed info)
- Third-party receipt (information received from a third party with right to disclose)
- Compelled disclosure (disclosure required by law, regulation, or legal process)

**Common issues:**

- Exclusions drafted too narrowly to be practically usable
- No independent development carve-out (creates operational impossibility)
- Third-party receipt requires proving the third party's source (often impossible)
- Compelled disclosure treated as an exclusion rather than a permitted disclosure with
  conditions
- Burden of proof not clearly allocated (should be on recipient claiming exclusion)

**Standard position (market norm):**
All five exclusions should be present with clear language:

- Public domain: "at the time of disclosure or thereafter becomes publicly available through
  no fault of the Receiving Party"
- Prior possession: "was in Receiving Party's possession prior to disclosure, as demonstrated
  by contemporaneous written records"
- Independent development: "was independently developed by Receiving Party without use of
  or reference to Disclosing Party's Confidential Information"
- Third-party receipt: "was rightfully received from a third party without restriction and
  without breach of any obligation of confidentiality"
- Compelled disclosure: handled as permitted disclosure with conditions, not as exclusion

[JURISDICTION-SPECIFIC] Key variations:

- **Reverse engineering**: Some jurisdictions (EU under Trade Secrets Directive) protect
  the right to reverse engineer lawfully obtained products. NDA restrictions on reverse
  engineering may be unenforceable [VERIFY]
- **Competition law**: Information exchange between competitors may trigger competition
  law concerns regardless of NDA protections [VERIFY]

### 3. Purpose and Permitted Use

**Key elements to review:**

- Specificity of the permitted purpose
- Whether the purpose is limited to evaluation only
- Scope creep risk (e.g., "and any related purposes")
- Alignment between stated purpose and actual business discussions

**Common issues:**

- Purpose so vague it provides no meaningful limitation ("general business discussions")
- Purpose includes operational use, not just evaluation (creates license risk)
- Mismatch between NDA purpose and actual intended use
- No clear prohibition on use for competitive advantage

**Standard position (market norm):**

- Purpose should be specific: "evaluating a potential [commercial partnership / acquisition /
  licensing arrangement / investment] between the parties"
- Use should be expressly limited to the stated purpose
- Explicit prohibition on use for competitive purposes or to gain unfair advantage

### 4. Use Restrictions and Access Controls

**Key elements to review:**

- Need-to-know limitation (only to personnel who need access for the permitted purpose)
- Affiliate access rights (whether affiliates can receive confidential information)
- Advisor carve-outs (lawyers, accountants, investment bankers)
- Flow-down obligations (requiring recipients to be bound by confidentiality)
- Whether the disclosing party can object to specific recipients

**Common issues:**

- No need-to-know limitation (all employees can access)
- Affiliate access without flow-down obligations
- Advisor carve-out without professional duty of confidence requirement
- No accountability for breaches by recipients (disclosing party has no recourse)
- Subcontractor access without written consent

**Standard position (market norm):**

- Access limited to employees, officers, directors, and authorized representatives with
  need to know
- Affiliate access permitted with flow-down obligations
- Advisor access permitted for those under professional duty of confidence
- Receiving party responsible for compliance by all recipients
- Written consent required for any other disclosure

### 5. Standard of Care and Security

**Key elements to review:**

- Care standard (at least the same care as for own confidential information, and not less
  than reasonable care)
- Specific security requirements (encryption, access controls, secure destruction)
- Incident reporting obligations (notification of actual or suspected breach)
- Audit rights (right to verify compliance with security obligations)

**Common issues:**

- Only "reasonable care" with no floor (may be interpreted differently)
- No specific security requirements for highly sensitive information
- No breach notification obligation
- Audit rights that are impractical or overly invasive

**Standard position (market norm):**

- Care standard: "at least the same degree of care as Receiving Party uses to protect its
  own confidential information of similar nature, and in no event less than reasonable care"
- Security requirements appropriate to information sensitivity (may include encryption,
  access logging, secure destruction)
- Breach notification within reasonable period (24-72 hours for suspected breaches)

### 6. Compelled Disclosure

**Key elements to review:**

- Notice requirement (obligation to notify disclosing party before disclosure)
- Timing of notice (as soon as legally permitted, with sufficient time to seek protection)
- Cooperation obligations (assisting with protective orders or confidentiality motions)
- Minimum disclosure (disclose only what is legally required)
- Continuing confidentiality (disclosed information retains confidential status)

**Common issues:**

- No notice requirement (disclosing party has no opportunity to seek protection)
- Notice only "if legally permitted" without effort to seek permission
- No cooperation obligation
- Disclosure of entire category when only specific information is legally required
- Compelled disclosure treated as destroying confidentiality of all related information

**Standard position (market norm):**

- Prompt notice (within 24-48 hours where legally permitted)
- Reasonable cooperation with protective order efforts
- Disclosure limited to the minimum legally required
- Disclosed information retains confidential status to the extent permitted
- Legal fees for protective order efforts may be addressed

[JURISDICTION-SPECIFIC] Key variations:

- **US**: Subpoena and discovery obligations vary by jurisdiction. Notice may be prohibited
  by certain government requests (NSLs, certain warrants) [VERIFY]
- **UK**: Disclosure obligations in litigation. Norwich Pharmacal orders may compel
  disclosure [VERIFY]
- **EU**: GDPR data subject access rights may require disclosure of personal data [VERIFY]

### 7. Term and Survival

**Key elements to review:**

- Agreement term (when the disclosure period ends)
- Confidentiality survival period (how long obligations continue after termination)
- Trade secret carve-out (perpetual protection for trade secrets)
- Termination rights (can either party terminate early?)
- Effect of termination (triggers return/destruction obligations)

**Common issues:**

- No defined term (creates perpetual disclosure right)
- Survival period too short for information type (1 year for trade secrets)
- Survival period too long and potentially unenforceable (10+ years for non-trade secrets)
- No trade secret carve-out (same survival for all information regardless of value)
- No termination right (locked into indefinite agreement)

**Standard position (market norm):**

- Agreement term: 1-2 years for the disclosure period
- Survival period: 2-5 years for ordinary confidential information after termination
- Trade secrets: protected for as long as they qualify as trade secrets under applicable law
- Either party may terminate on 30 days' written notice
- Confidentiality obligations survive termination for the stated survival period

[JURISDICTION-SPECIFIC] Key variations:

- **California**: Perpetual confidentiality obligations may be unenforceable; trade secret
  protection limited to statutory protections [VERIFY]
- **UK**: Reasonable time limits generally required for confidentiality obligations [VERIFY]
- **Civil law**: Some jurisdictions impose statutory limits on confidentiality duration [VERIFY]

### 8. Return and Destruction

**Key elements to review:**

- Trigger (on termination, on request, or both)
- Timeline for compliance (typically 10-30 days)
- Scope (all copies, including electronic backups and derivative works)
- Certification requirement (written confirmation of destruction)
- Legal retention carve-out (retention required by law or professional standards)
- Archival copies (whether backup copies must be destroyed or can be retained subject to
  ongoing confidentiality)

**Common issues:**

- No return/destruction obligation (materials retained indefinitely)
- Timeline too short for practical compliance (especially for backup systems)
- No legal retention carve-out (creates impossible compliance situation)
- Certification requirement without specifying who must certify
- No treatment of derivative works (notes, analyses, summaries)

**Standard position (market norm):**

- Return or destroy at disclosing party's election within 30 days of termination or request
- Scope includes all copies and derivative works
- Legal retention carve-out for materials required to be retained by law or professional
  standards (subject to ongoing confidentiality)
- Written certification of destruction by authorized officer
- Archival copies may be retained in secure backup systems subject to ongoing confidentiality
  (practical necessity given modern IT systems)

### 9. Remedies and Relief

**Key elements to review:**

- Injunctive relief acknowledgment (recognizing that breach may cause irreparable harm)
- Specific performance availability
- Damages (actual, consequential, liquidated)
- Indemnification obligations
- Attorneys' fees and costs
- Limitation of liability

**Common issues:**

- No injunctive relief language (may make it harder to obtain emergency relief)
- Injunctive relief "acknowledgment" that overreaches (e.g., "shall be entitled to
  injunctive relief without bond")
- Liquidated damages that may be unenforceable as penalties
- Broad indemnification for any breach (disproportionate to typical NDA risk)
- No limitation of liability (unlimited exposure for breach)

**Standard position (market norm):**

- Acknowledgment that breach may cause irreparable harm and that injunctive relief may be
  appropriate (without guaranteeing it will be granted)
- Actual damages recoverable
- No liquidated damages (difficult to calculate and may be challenged as penalty)
- No broad indemnification (unnecessary for typical NDA)
- Limitation of liability may be included for high-value deals

[JURISDICTION-SPECIFIC] Key variations:

- **US**: Injunctive relief standards vary by jurisdiction. "Irreparable harm" acknowledgment
  may or may not affect actual standard applied [VERIFY]
- **UK**: Injunctions are discretionary equitable remedies. Contractual acknowledgments do
  not bind the court [VERIFY]
- **Civil law**: Specific performance may be more readily available than in common law
  jurisdictions. Penalty clauses may be enforceable (and adjustable by court) [VERIFY]

### 10. No License / No Obligation

**Key elements to review:**

- IP reservation (no implied license to patents, copyrights, trade secrets, or other IP)
- No deal obligation (disclosure does not commit either party to proceed with transaction)
- Warranty disclaimers (no warranty as to accuracy or completeness of disclosed information)
- Non-reliance language (receiving party should not rely solely on disclosed information)

**Common issues:**

- Missing IP reservation (could create implied license arguments)
- Ambiguous language suggesting commitment to proceed
- No warranty disclaimer (could create liability for inaccurate information)
- Evaluation rights language that goes beyond the stated purpose

**Standard position (market norm):**

- Express statement that no license is granted under any IP rights
- Express statement that neither party is obligated to proceed with any transaction
- Disclaimer of warranties as to accuracy, completeness, or fitness for purpose
- Each party responsible for own evaluation and due diligence decisions

### 11. Governing Law and Disputes

**Key elements to review:**

- Choice of law (which jurisdiction's law governs)
- Forum selection (which courts have jurisdiction, exclusive or non-exclusive)
- Arbitration clause (if disputes go to arbitration instead of litigation)
- Prevailing party fees (who pays legal costs if dispute arises)
- Injunctive relief exception (courts retain jurisdiction for injunctive relief even if
  arbitration applies)

**Common issues:**

- No governing law clause (creates uncertainty)
- Governing law disconnected from parties or transaction (e.g., Delaware law for two
  European parties with no US connection)
- Exclusive jurisdiction in inconvenient forum
- Arbitration without injunctive relief carve-out (may delay emergency relief)
- Prevailing party clause that creates asymmetric risk

**Standard position (market norm):**

- Governing law of jurisdiction with connection to at least one party or the transaction
- Non-exclusive jurisdiction (allows flexibility while establishing a default)
- If arbitration, carve-out for injunctive relief in courts
- No prevailing party clause for typical NDAs (cost not worth the exposure)

[JURISDICTION-SPECIFIC] Key variations:

- **US**: State law choice matters (e.g., California vs. Delaware). Federal courts have
  concurrent jurisdiction over trade secret claims under DTSA [VERIFY]
- **UK**: English courts comfortable with exclusive jurisdiction clauses. Arbitration Act
  provides framework for injunctive relief [VERIFY]
- **EU**: Brussels Regulation governs jurisdiction in EU cross-border matters [VERIFY]

---

## Deviation Severity Classification

### GREEN — Acceptable

The clause aligns with or is better than the organization's standard position. Minor
variations that are commercially reasonable and do not materially increase risk.

**NDA Examples:**

- Confidentiality survival of 3 years when standard is 5 years (shorter but reasonable for
  non-trade-secret information)
- Confirmation period for oral disclosures is 14 days when standard is 30 days (stricter
  but workable)
- Governing law in a well-established commercial jurisdiction close to the preferred one

**Action**: Note for awareness. No negotiation needed.

### YELLOW — Negotiate

The clause falls outside the standard position but within a negotiable range. The term is
common in the market but not the organization's preference. Requires attention and likely
negotiation, but not escalation.

**NDA Examples:**

- Confidentiality survival of 1 year when standard is 3-5 years (too short, but negotiable)
- Marking requirement for all information including oral (stricter than standard)
- No residual knowledge carve-out when receiving party employs personnel who will work on
  similar projects
- Limited compelled disclosure notice (only "if legally permitted" without effort requirement)
- Governing law in an acceptable but not preferred jurisdiction

**Action**: Generate specific redline language. Provide fallback position. Estimate
business impact of accepting vs. negotiating.

### RED — Escalate

The clause falls outside the acceptable range, triggers a defined escalation criterion, or
poses material risk. Requires senior counsel review, outside counsel involvement, or
business decision-maker sign-off.

**NDA Examples:**

- No exclusions from confidential information definition (unworkable)
- No compelled disclosure carve-out (creates impossible compliance situation)
- Perpetual confidentiality without trade secret carve-out (may be unenforceable)
- Unrestricted right to use residual information without limitation
- Assignment of IP rights in information disclosed (transforms NDA into license agreement)
- No governing law clause in cross-border NDA (enforcement uncertainty)
- Excessive liquidated damages that may constitute unenforceable penalty
- Broad indemnification for any breach of NDA (disproportionate risk)

**Action**: Explain the specific risk (with legal basis where possible). Provide
market-standard alternative language. Estimate exposure. Recommend escalation path.

---

## Redline Format

For each redline:

```
**Clause**: [Section reference and clause name]
**Current language**: "[exact quote from the NDA]"
**Proposed redline**: "[specific alternative language]"
**Rationale**: [1-2 sentences explaining why, suitable for external sharing]
**Legal basis**: [Relevant statute, regulation, or principle — or "General commercial practice"]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative position if primary redline is rejected]
```

### Redline Best Practices

1. **Be specific**: Provide exact language, not vague guidance. The redline should be ready
   to insert into the document.
2. **Be balanced**: Propose language that is firm on critical points but commercially
   reasonable. Overly aggressive redlines slow negotiations and signal distrust.
3. **Explain the rationale**: Include a brief, professional rationale suitable for sharing
   with the counterparty's counsel.
4. **Provide fallback positions**: For YELLOW items, include a fallback if the primary ask
   is rejected.
5. **Prioritize**: Not all redlines are equal. Indicate which are must-haves and which are
   nice-to-haves.
6. **Consider the relationship**: Adjust tone based on whether this is a new counterparty,
   existing partner, or strategic relationship.
7. **Reference applicable law**: Where the redline addresses a legal risk, cite the relevant
   statute or principle. If citing from memory, mark with [VERIFY].

---

## Negotiation Priority Framework

When presenting redlines, organize by negotiation priority:

### Tier 1 — Must-Haves (Deal Breakers)

Issues where the organization cannot proceed without resolution:

- Missing exclusions (particularly prior possession, independent development)
- No compelled disclosure procedure
- Perpetual confidentiality for all information (likely unenforceable)
- Missing or unworkable return/destruction mechanism
- No governing law clause
- Assignment of IP rights beyond the agreed scope

### Tier 2 — Should-Haves (Strong Preferences)

Issues that materially affect risk but have negotiation room:

- Confidentiality survival period adjustments
- Marking and confirmation requirements for oral disclosures
- Residual knowledge carve-out (if needed for operations)
- Compelled disclosure notice and cooperation mechanics
- Security and breach notification obligations

### Tier 3 — Nice-to-Haves (Concession Candidates)

Issues that improve the position but can be conceded strategically:

- Preferred governing law (if alternative is acceptable)
- Specific security requirements (if baseline is reasonable)
- Audit rights
- Prevailing party attorney's fees
- Minor definitional improvements

**Negotiation strategy**: Lead with Tier 1 items. Trade Tier 3 concessions to secure
Tier 2 wins. Never concede on Tier 1 without escalation.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                  | Fail Action                                              |
| -------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established principle                      | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction                           | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments or repeal against authoritative sources where accessible | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the NDA's governing law. No assumptions from other jurisdictions leaking in     | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden. If you are not certain of a legal position, say so         | Add confidence qualifier                                 |

### Self-Interrogation for RED Items

For any clause classified as RED, apply this 3-pass self-interrogation before delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the risk assessment follow logically from the statute/principle cited?
- Would a court in this jurisdiction actually reach this conclusion?
- Is there a counter-argument the counterparty's counsel will make?

**Pass 2 — Completeness**:

- Have all relevant statutes and regulations been considered?
- Have any relevant cases or principles been missed?
- Are there regulatory dimensions not yet considered?

**Pass 3 — Challenge**:

- What is the strongest argument that this clause IS acceptable?
- Under what commercial circumstances might a reasonable lawyer accept this risk?
- Is the RED classification proportionate, or is this actually YELLOW with mitigations?

If any pass reveals a weakness, revise the analysis before delivery.

### Confidence Scoring

For each material clause analysis, assign a confidence level:

| Level        | Range     | Meaning                                          | Action                                                |
| ------------ | --------- | ------------------------------------------------ | ----------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled law, clear statute, no ambiguity         | State with confidence                                 |
| **High**     | 0.80-0.94 | Strong authority, minor interpretation questions | State with brief caveat                               |
| **Probable** | 0.60-0.79 | Good arguments but reasonable minds could differ | State with explicit reasoning and contra-indicators   |
| **Possible** | 0.40-0.59 | Genuinely uncertain, competing authorities       | Flag for counsel review with both sides               |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative                          | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every NDA review output MUST include a Glass Box audit section at the end:

```yaml
glass_box:
  document: "[NDA title and date]"
  document_type: "Mutual NDA"
  user_role: "[Disclosing Party / Receiving Party / Mutual]"
  governing_law: "[Jurisdiction identified from the NDA]"
  playbook_used: "[Playbook name or 'General commercial standards']"
  review_basis: "[Organizational playbook / General commercial standards]"
  clauses_reviewed: 11
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to temp file or 'Not created']"
  statutes_consulted:
    - "[Statute 1 — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified legal review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in NDA drafting and review:

1. **Treating all NDAs as fungible** — An M&A due diligence NDA, a commercial partnership
   NDA, and an employment negotiation NDA have different risk profiles and different
   standard positions. Do not apply a one-size-fits-all approach.

2. **Accepting overbroad definitions without pushback** — A definition of "Confidential
   Information" that captures "all information disclosed" without exclusions is unworkable.
   Standard exclusions exist for good reason.

3. **Ignoring the purpose clause** — The purpose clause limits permitted use. An overly
   broad purpose ("any business purpose") effectively grants unlimited use rights. An
   overly narrow purpose may not cover the actual intended use.

4. **Perpetual confidentiality for all information** — Perpetual confidentiality is
   appropriate for trade secrets but may be unenforceable for ordinary confidential
   information. Most jurisdictions expect time limits on contractual confidentiality.

5. **No compelled disclosure procedure** — Treating compelled disclosure as an exclusion
   rather than a permitted disclosure with conditions creates an impossible compliance
   situation and may destroy the protective order opportunity.

6. **Confusing NDAs with licenses** — An NDA protects information; it does not grant rights
   to use it. If the NDA includes IP assignment, unlimited evaluation rights, or broad
   residual knowledge clauses, it may be transforming into a license agreement.

7. **Overlooking data protection requirements** — If personal data will be shared under
   the NDA, data protection requirements may apply. A standard NDA confidentiality clause
   does not satisfy GDPR or equivalent obligations.

8. **Applying US trade secret concepts universally** — The DTSA/UTSA definition of "trade
   secret" is US law. Other jurisdictions have different definitions and different
   protection regimes. Do not assume US concepts apply under foreign governing law.

9. **Ignoring the residual knowledge problem** — Employees who receive confidential
   information will remember some of it. A strict NDA without residual knowledge carve-out
   may create impossible compliance situations for the receiving party. Consider whether
   a carve-out is needed based on the nature of the information and the receiving party's
   operations.

10. **Accepting injunctive relief overreach** — Language stating that the disclosing party
    "shall be entitled to injunctive relief without posting bond and without proving
    irreparable harm" may not be enforceable. Courts apply their own standards for
    injunctive relief.

11. **Missing the return/destruction practical reality** — Modern IT systems make complete
    destruction of all copies impractical. Backup systems, email archives, and disaster
    recovery copies cannot realistically be purged. Insisting on certification of complete
    destruction creates a compliance trap.

12. **Single-pass review** — Reading an NDA once, clause by clause, misses interactions.
    A broad definition may be acceptable if exclusions are robust. A short survival period
    may be acceptable if trade secrets are carved out. Read the whole document before
    concluding on any clause.

13. **Importing jurisdiction-specific concepts** — "Work-for-hire" is a US copyright
    concept. "Kary umowne" is a Polish penalty clause concept. "Unilateral undertaking"
    has specific meaning in English law. Do not apply concepts from one jurisdiction to
    an NDA governed by another.

14. **Confidence without evidence** — Never state "this clause is unenforceable" without
    citing the specific statute, regulation, or principle that renders it so. Confident
    assertions without authority are more dangerous than expressed uncertainty.

15. **Reviewing without knowing the purpose** — An NDA review without knowing the
    transaction context, information types, and party roles cannot properly assess risk.
    A clause that is RED for one purpose may be GREEN for another.

---

## Writing Standards

Apply plain-language discipline to all output:

**For redline rationales** (shared with counterparty's counsel):

- Plain language. No jargon or filler.
- Active voice: "This clause requires marking all disclosures" not "All disclosures are
  required to be marked by this clause"
- Short sentences. One point per sentence.
- Name the actor: "The Disclosing Party must..." not "It is required that..."
- Specific, not vague: cite the relevant provision rather than saying "this may have
  enforceability issues"

**For internal analysis**:

- Same plain-language standards
- May include more technical legal analysis
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

- In Step 4, search for jurisdiction-relevant trade secret statutes, confidentiality case
  law, and enforcement standards
- Save the most relevant results to a local temp file (`/tmp/legalcode-nda-authority.md`)
- Reference verified authority from the temp file throughout the clause analysis
- For RED items, search for additional case law to support or challenge the classification
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Include a prominent notice that legal citations require independent verification
- Focus the analysis on commercial risk assessment rather than legal certainty

---

## Output Format Template

Structure the final deliverable as:

```markdown
## NDA Review Summary

**Document**: [NDA name/identifier]
**Parties**: [party names and roles]
**Your Role**: [Disclosing Party / Receiving Party / Mutual]
**Governing Law**: [jurisdiction]
**Purpose**: [stated purpose of disclosure]
**Deadline**: [if provided]
**Review Basis**: [Playbook name / General Commercial Standards]
**Date of Review**: [date]

---

## Key Findings

[Top 3-5 issues with severity flags (RED/YELLOW) and one-line summaries]

---

## Missing Clauses

[List any of the 11 clause categories that are absent, with severity assessment]

---

## Clause-by-Clause Analysis

### [Clause Category] — [GREEN / YELLOW / RED] | Confidence: [level]

**NDA says**: [summary of the provision]
**Standard position**: [playbook or market standard]
**Deviation**: [description of gap]
**Business impact**: [what this means practically]
**Redline** (if YELLOW or RED):

> [Specific proposed language]

[Repeat for each clause category]

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

---

## Localization Notes

This skill is jurisdiction-agnostic by design. To create a jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with jurisdiction-specific legal content
2. Replace [VERIFY] tags with verified statutory references
3. Add jurisdiction-specific clause considerations (e.g., German AGB rules for standard
   terms, California limits on non-compete scope)
4. Add jurisdiction-specific anti-patterns
5. Update the frontmatter name and description to reference the specific jurisdiction
6. Add relevant case law and statutory framework sections

Existing jurisdiction-specific NDA variants:

- **UK**: `imported-uk-legal-plugins--skills-uk-legal-nda-triage/SKILL.md`
- **Poland**: `imported-iura-plugins--iura-pl-skills-nda-triage/SKILL.md`

---

## Provenance

Enhanced by Legalcode (2026-03-01). Original skill created 2026-02-27 as jurisdiction-
agnostic baseline. This version upgraded to Legalcode quality standard with:

- Multi-step interactive workflow with CLARIFY points
- Deep clause analysis with severity classification
- Citation Quality Gates, Self-Interrogation, and Confidence Scoring
- Glass Box audit trail for traceability
- 15-item anti-patterns catalogue
- Writing standards and output format template
- External tool integration with graceful degradation
