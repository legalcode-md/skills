---
name: legalcode-review-contract
description: Review contracts against your organization's negotiation playbook — flag deviations, generate
  confidence-scored redlines, and produce an auditable analysis with business impact assessment. Invoke
  with /review-contract less than file or textgreater than . Use when reviewing vendor contracts, customer
  agreements, SaaS agreements, professional services contracts, licenses, partnerships, procurement agreements,
  or any commercial agreement requiring clause-by-clause analysis against standard positions. Covers AI-specific
  provisions, ESG/supply chain clauses, and emerging regulatory requirements (EU AI Act, CSDDD). Jurisdiction-agnostic
  with localization markers for any governing law. Supports playbook-based or general-standard review.
  Produces GREEN/YELLOW/RED deviation classification, redline suggestions with fallback positions, negotiation
  strategy, stakeholder mapping, and Glass Box audit trail.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review contracts against your organization's negotiation playbook — flag deviations, generate confidence-scored redlines, and produce an auditable analysis with business impact assessment. Invoke with /review-contract <file or text>. Use when reviewing vendor contracts, customer agreements, SaaS agreements, professional services contracts, licenses, partnerships, procurement agreements, or any commercial agreement requiring clause-by-clause analysis against standard positions. Covers AI-specific provisions, ESG/supply chain clauses, and emerging regulatory requirements (EU AI Act, CSDDD). Jurisdiction-agnostic with localization markers for any governing law. Supports playbook-based or general-standard review. Produces GREEN/YELLOW/RED deviation classification, redline suggestions with fallback positions, negotiation strategy, stakeholder mapping, and Glass Box audit trail.


# Legalcode Review Contract

> **Disclaimer**: This skill provides a framework for AI-assisted contract review. It does
> not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before use. Laws change; verify current
> applicability before relying on any provision described here. Statutory and case law
> references cited from memory carry hallucination risk — verify against authoritative
> sources before relying on them. Stanford research demonstrates that general-purpose AI
> systems hallucinate on legal queries 69-88% of the time; even purpose-built legal AI
> tools have meaningful error rates requiring independent verification.

## Purpose and Scope

This skill reviews existing contracts against an organization's negotiation playbook or
general commercial standards. It identifies deviations, classifies their severity, generates
actionable redline suggestions, and produces a confidence-scored, auditable analysis.

**Covers:**

- Clause-by-clause analysis of any commercial agreement
- Deviation classification (GREEN / YELLOW / RED)
- Redline generation with fallback positions
- Missing clause detection
- Business impact assessment and negotiation strategy
- AI-specific and ESG/supply chain clause analysis
- Quality-verified output with Glass Box audit trail
- Multi-stakeholder impact mapping

**Does not:**

- Draft new contracts from scratch (see drafting-specific skills)
- Provide legal advice or replace qualified counsel
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers
- Perform due diligence beyond the four corners of the contract (see due-diligence skills)

## Invocation

```
/review-contract <contract file or URL>
```

Review the contract: @$1

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The contract's own governing law clause determines
which legal framework applies. The review identifies the governing law early and adapts
the analysis accordingly.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- Mandatory consumer protection rules (if any consumer party is involved)
- Statutory limits on exclusion or limitation of liability
- IP ownership defaults (work-for-hire, employee works, assignment formalities)
- Data protection regime (GDPR, UK GDPR, CCPA/CPRA, LGPD, PIPA, etc.)
- Penalty clause enforceability rules
- Dispute resolution norms (jury availability, class actions, arbitration culture)
- Contract formation requirements (writing, notarization, witnesses)
- Anti-bribery, sanctions, and export control regimes
- AI regulatory frameworks (EU AI Act, state-level AI laws)
- Supply chain due diligence obligations (German LkSG, EU CSDDD)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- Multiple valid approaches exist and the user's preference matters
- Ambiguity in the contract creates a fork that only the user can resolve
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

### Step 1: Accept the Contract

Accept the contract in any of these formats:

- **File**: PDF, DOCX, or other document format
- **URL**: Link to a contract in a CLM, cloud storage, or document system
- **Pasted text**: Contract text pasted directly into the conversation

If no contract is provided, prompt the user to supply one.

If the contract is in a language other than English, note this and ask if the user wants a
translation, a review in the original language, or both.

### Step 2: Gather Context

**CLARIFY** — Before beginning the review, ask the user these questions. Present them
as a structured set of options where possible:

1. **Which side are you on?**
   - Options: Vendor/Supplier, Customer/Buyer, Licensor, Licensee, Partner, Other
   - _Why this matters_: The entire analysis flips depending on which side you represent.
     What protects a vendor harms a customer and vice versa.

2. **Deadline**: When does this need to be finalized?
   - Options: Urgent (days), Standard (1-2 weeks), Flexible (no hard deadline)
   - _Why this matters_: Affects how many issues to surface vs. focus only on critical ones.

3. **Focus areas**: Any specific concerns?
   - Options: Data protection, IP ownership, Liability exposure, Termination flexibility,
     Payment terms, AI provisions, No specific focus — full review
   - Allow multiple selections.
   - _Why this matters_: Lets the analysis lead with what the user cares about most.

4. **Deal context**: Relevant business context?
   - Free text. Prompt with examples: deal size, strategic importance, existing relationship,
     whether this is a template or one-off negotiation.
   - _Why this matters_: A $10K vendor contract gets different treatment than a $10M
     strategic partnership.

If the user provides partial context, proceed with what you have but **state your
assumptions explicitly** (e.g., "I'm assuming you are on the customer side — let me know
if that's wrong and I'll re-run the analysis"). Do not silently assume.

### Step 3: Load the Playbook

Check for the organization's contract review playbook in local settings (e.g.,
`legal.local.md` or similar configuration files).

The playbook should define:

- **Standard positions**: Preferred terms for each major clause type
- **Acceptable ranges**: Terms that can be agreed without escalation
- **Escalation triggers**: Terms that require senior counsel or decision-maker sign-off

**If no playbook is configured:**

**CLARIFY** — Inform the user that no playbook was found, and ask which approach to take:

- **Option A: Set up a playbook now** — Walk through defining the organization's standard
  positions for key clauses (limitation of liability cap, indemnification approach, IP
  ownership default, data protection requirements, termination preferences). This takes
  time upfront but makes this and all future reviews more precise.
- **Option B: Proceed with general commercial standards** — Use widely-accepted market
  standards as the baseline. Faster, but the review may not reflect the organization's
  specific risk appetite or negotiation history.
- **Option C: I'll provide positions as we go** — Start the review and I'll ask about your
  preferred position when it matters for each clause.

If proceeding without a playbook, clearly label the review:
"Based on general commercial standards — not organizational positions"

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Read the contract's governing law clause and identify the applicable jurisdiction. Then
use **legalcode-mcp** to build a working legal reference file for this review.

**Research process:**

1. **Identify the governing law** from the contract (e.g., "laws of the State of Delaware,"
   "English law," "Polish law under the Kodeks cywilny").

   **CLARIFY** — If any of the following are true, ask the user before proceeding:
   - **No governing law clause found**: Ask which jurisdiction the user expects to apply,
     and flag the absence as a RED deviation.
   - **Multiple governing law clauses** (e.g., different schedules reference different laws):
     Ask which governs the main body and note the conflict.
   - **Governing law is unusual or unexpected** for the deal type (e.g., a US-to-US SaaS
     contract governed by the laws of the Cayman Islands): Confirm the user is aware and
     ask whether to analyze under the stated law or flag as an issue.

2. **Search legalcode-mcp** for jurisdiction-relevant authority across these categories:
   - Statutes governing exclusion and limitation of liability clauses
   - IP ownership defaults and assignment formality requirements
   - The applicable data protection regime and transfer mechanisms
   - Penalty / liquidated damages enforceability rules
   - Anti-bribery and sanctions regime
   - Mandatory contract terms that cannot be excluded by agreement
   - AI regulatory requirements affecting contractual obligations
   - Leading case law on contract interpretation, limitation clauses, and indemnification

3. **Save the most relevant results** into a local temporary reference file (e.g.,
   `/tmp/legalcode-review-authority.md`). Structure it as:

   ```markdown
   # Legal Authority Reference — [Contract Name]

   ## Governing Law: [Jurisdiction]

   ## Date Gathered: [date]

   ### Statutes & Regulations

   - [Statute name, section, current text or summary]

   ### Case Law

   - [Case name, citation, key holding relevant to this contract]

   ### Regulatory Guidance

   - [Regulator, guidance title, relevance]
   ```

4. **Use this reference file throughout the analysis.** When citing a statute or case in
   your clause analysis, pull from the verified reference file rather than from memory.
   Mark any citation sourced from legalcode-mcp as VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**

- Mark every statutory and case law reference with [VERIFY]
- Note in the Glass Box audit trail: `external_tools_used: "None — manual verification required"`
- Proceed with the analysis using general commercial knowledge, but flag that legal
  authority has not been independently verified

[JURISDICTION-SPECIFIC] For each jurisdiction, the research should cover at minimum:

- Statute governing exclusion/limitation clauses
- IP ownership and assignment formalities
- Data protection regime and transfer mechanisms
- Penalty/liquidated damages enforceability rules
- Anti-bribery and sanctions regime
- Mandatory contract terms that cannot be excluded by agreement

### Step 5: Clause-by-Clause Analysis

Analyze the contract systematically. Read the entire contract before flagging issues —
clauses interact with each other (e.g., an uncapped indemnity may be partially mitigated
by a broad limitation of liability).

**CLARIFY** — For long or complex contracts (50+ pages, or with multiple schedules,
exhibits, or incorporated documents):

- Ask the user whether to perform a **full review** of all 16 clause categories, or a
  **priority review** focused on the user's stated focus areas (from Step 2) plus any
  RED items discovered.
- If the contract incorporates external documents by reference (e.g., "subject to Vendor's
  Standard Terms at [URL]"), ask whether the user wants those incorporated documents
  reviewed as well, or only the main agreement.

Cover all 16 clause categories below (unless the user opted for a priority review). For
each, assess against the playbook (or general standards) and note whether the clause is
present, absent, or unusual.

| #   | Clause Category              | Depth    | Key Review Points                                                                               |
| --- | ---------------------------- | -------- | ----------------------------------------------------------------------------------------------- |
| 1   | Limitation of Liability      | Deep     | Cap amount, carveouts, mutual vs. unilateral, consequential damages                             |
| 2   | Indemnification              | Deep     | Scope, mutual vs. unilateral, cap, IP infringement, data breach, procedure                      |
| 3   | Intellectual Property        | Deep     | Pre-existing IP, developed IP, assignment, license grants, moral rights                         |
| 4   | Data Protection              | Deep     | DPA requirement, processing terms, sub-processors, breach notification, transfers               |
| 5   | Term & Termination           | Deep     | Duration, renewal, convenience termination, cause termination, wind-down                        |
| 6   | Governing Law & Disputes     | Deep     | Jurisdiction, venue, arbitration vs. litigation, escalation                                     |
| 7   | Confidentiality              | Standard | Scope, term, carveouts, return/destruction obligations                                          |
| 8   | Representations & Warranties | Standard | Scope, disclaimers, survival period, remedies for breach                                        |
| 9   | Insurance                    | Standard | Coverage requirements, minimums, evidence of coverage                                           |
| 10  | Assignment                   | Standard | Consent requirements, change of control, exceptions                                             |
| 11  | Force Majeure                | Standard | Scope of events, notification, mitigation, termination rights                                   |
| 12  | Payment Terms                | Standard | Net terms, late fees, taxes, price escalation, disputed invoices                                |
| 13  | Compliance & Regulatory      | Standard | Anti-bribery, sanctions, export control, modern slavery, regulatory approvals                   |
| 14  | Definitions & Boilerplate    | Standard | Entire agreement, severability, waiver, notices, counterparts, amendments                       |
| 15  | AI & Technology Provisions   | Deep     | AI use restrictions, AI-generated output ownership, model training, algorithmic accountability  |
| 16  | ESG & Supply Chain           | Standard | Sustainability commitments, supply chain due diligence, human rights, environmental obligations |

### Step 6: Missing Clause Detection

After analyzing the clauses that are present, check for important clauses that are entirely
absent from the contract. A missing clause can be as significant as a problematic one.

For each of the 16 clause categories:

- If the clause category is entirely absent, flag it
- Assess whether the absence is acceptable (e.g., no force majeure in a short-term contract
  may be fine) or a material gap (e.g., no limitation of liability is always a RED flag)
- Classify the absence as GREEN (not needed for this contract type), YELLOW (should be
  added), or RED (must be added)

Common missing clause issues:

- No DPA when personal data is processed (RED)
- No limitation of liability clause (RED)
- No termination for convenience in a long-term contract (YELLOW)
- No force majeure in a multi-year engagement (YELLOW)
- No anti-bribery provisions in a cross-border contract (YELLOW)
- No change-of-control assignment restriction (YELLOW)
- No AI use provisions when AI tools are used in performance (YELLOW)
- No data return/deletion obligations on termination (YELLOW)

**CLARIFY** — When the severity of a missing clause depends on business context that
hasn't been provided, ask rather than guess:

- "This contract has no data processing addendum. Will personal data be processed under
  this agreement? If yes, this is a RED gap. If no personal data is involved, it's fine."
- "There's no force majeure clause. Given the term length and nature of the engagement,
  is this a concern for your organization?"
- "No insurance requirements are specified. Does your organization require vendors to
  carry specific coverage for this type of engagement?"

### Step 7: Flag Deviations

Classify each deviation from the playbook using the three-tier system defined in the
**Deviation Severity Classification** section below. For each deviation:

- **GREEN**: Note for awareness.
- **YELLOW**: Generate specific redline language, provide a fallback position, and estimate
  business impact of accepting vs. negotiating.
- **RED**: Explain the specific risk (citing the legal basis where possible), provide
  market-standard alternative language, estimate exposure, and recommend an escalation path.

**CLARIFY** — For borderline classifications where reasonable minds could differ, ask
the user rather than assuming:

- **YELLOW vs. RED borderline**: When a clause is aggressive but might be acceptable
  depending on the organization's risk appetite, present both interpretations and ask:
  "This liability cap at 3 months' fees is below market standard. Should I treat this as
  YELLOW (negotiate) or RED (escalate)? It depends on your organization's risk tolerance."
- **GREEN vs. YELLOW borderline**: When a clause is slightly off-standard but might be
  acceptable given the deal context: "The confidentiality term is 1 year — shorter than the
  usual 2-3 years. Is this a concern for this deal, or acceptable given the relationship?"
- **Risk tolerance check**: If the contract has several borderline items trending in the
  same direction (all slightly favoring the counterparty), ask whether the user wants a
  conservative classification (flag more) or pragmatic (flag only material items).

### Step 8: Generate Redlines

**CLARIFY** — Before generating redlines, ask the user about negotiation posture if not
already clear from context:

- **Relationship dynamic**: Is this a new counterparty, an existing partner, or a must-have
  vendor with leverage? This affects tone — redlines for a strategic partner should be
  collaborative; redlines for a commodity vendor can be firmer.
- **Volume of redlines**: If there are many YELLOW items, ask: "I've found [N] items worth
  negotiating. Do you want redlines for all of them, or should I focus on the top [X] most
  impactful ones?" Too many redlines can overwhelm a negotiation.

For each YELLOW and RED deviation, generate a redline using the format in **Redline
Format** below. Follow the **Redline Best Practices** to ensure redlines are specific,
balanced, and professionally rationed.

### Step 9: Business Impact Summary

Provide a summary section covering:

- **Overall risk assessment**: High-level view of the contract's risk profile
- **Top 3 issues**: The most important items to address, with severity and priority
- **Negotiation strategy**: Recommended approach — which issues to lead with, what to
  concede, how to sequence
- **Timeline considerations**: Any urgency factors affecting the negotiation approach

**CLARIFY** — If the deal context is unclear and it would materially affect the
negotiation strategy, ask:

- **Walk-away option**: "Can you walk away from this deal, or is this vendor/partner
  essential?" This determines whether the strategy is assertive or accommodating.
- **Internal approval chain**: "Who needs to sign off on the final terms? Legal only, or
  also business/procurement/executive?" This determines how to frame the escalation
  recommendations.
- **Prior negotiation history**: "Have you negotiated with this counterparty before? Did
  they move on similar issues?" Past behavior predicts which redlines will land.

### Step 10: Quality Verification

Before delivering the analysis, run the quality checks defined in the **Quality Assurance
Framework** section:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every RED-classified item, run the 3-pass Self-Interrogation. Revise if any pass
   reveals a weakness.
3. Assign a Confidence Score to each material clause analysis.
4. Verify completeness: confirm all 16 clause categories have been addressed (present or
   flagged as missing).
5. Generate the Glass Box Audit Trail and append it to the output.

### Step 11: CLM Routing

If a Contract Lifecycle Management system is connected via MCP:

- Recommend the appropriate approval workflow based on contract type and risk level
- Suggest the correct routing path (standard approval, senior counsel, outside counsel)
- Note any required approvals based on contract value or risk flags

If no CLM is connected, skip this step.

---

## Clause Analysis Reference

### 1. Limitation of Liability

**Key elements to review:**

- Cap amount (fixed amount, multiple of fees, or uncapped)
- Whether the cap is mutual or applies differently to each party
- Carveouts from the cap (what liabilities are uncapped)
- Whether consequential, indirect, special, or punitive damages are excluded
- Whether the exclusion is mutual
- Carveouts from the consequential damages exclusion
- Whether the cap applies per-claim, per-year, or aggregate

**Common issues:**

- Cap set at a fraction of fees paid (e.g., "fees paid in the prior 3 months" on a low-value contract)
- Asymmetric carveouts favoring the drafter
- Broad carveouts that effectively eliminate the cap (e.g., "any breach of Section X" where Section X covers most obligations)
- No consequential damages exclusion for one party's breaches

[JURISDICTION-SPECIFIC] Key variations:

- **Common law**: Check whether statutory reasonableness tests apply to exclusion clauses (e.g., UCTA in England, unconscionability in the US) [VERIFY]
- **Civil law**: Check whether liability for intentional fault (dolus/Vorsatz/wina umyslna) can be excluded — many civil codes prohibit this [VERIFY]
- **Consumer contracts**: Additional mandatory protections typically apply [VERIFY]

### 2. Indemnification

**Key elements to review:**

- Whether indemnification is mutual or unilateral
- Scope: what triggers the obligation (IP infringement, data breach, bodily injury, breach of representations)
- Whether indemnification is capped (subject to the overall liability cap, or uncapped)
- Procedure: notice requirements, right to control defense, right to settle
- Whether the indemnitee must mitigate
- Relationship between indemnification and the limitation of liability clause

**Common issues:**

- Unilateral indemnification for IP infringement when both parties contribute IP
- Indemnification for "any breach" (too broad — effectively uncaps liability)
- No right to control defense of claims
- Indemnification obligations that survive termination indefinitely

[JURISDICTION-SPECIFIC] Key variations:

- **Common law**: Indemnity is a primary obligation distinct from damages for breach. Different remoteness rules and limitation periods may apply [VERIFY]
- **Civil law**: Indemnification is not a native concept in many civil law systems. It is used under freedom of contract but may be interpreted differently. Distinguish from suretyship/guarantee [VERIFY]

### 3. Intellectual Property

**Key elements to review:**

- Ownership of pre-existing IP (each party should retain their own)
- Ownership of IP developed during the engagement
- Work-for-hire or assignment provisions and their scope
- License grants: scope, exclusivity, territory, sublicensing rights
- Open source considerations
- Feedback clauses (grants on suggestions or improvements)
- Moral rights waivers (where applicable)
- AI-generated work product ownership

**Common issues:**

- Broad IP assignment that could capture the customer's pre-existing IP
- Work-for-hire provisions extending beyond the deliverables
- Unrestricted feedback clauses granting perpetual, irrevocable licenses
- License scope broader than needed for the business relationship
- Silence on ownership of AI-generated outputs

[JURISDICTION-SPECIFIC] Key variations:

- **US**: Work-for-hire doctrine applies to certain categories of works. Copyright assignment does not require specific formalities beyond a signed writing [VERIFY]
- **England & Wales**: No work-for-hire doctrine. Copyright assignment must be in writing (CDPA s.90(3)). Moral rights can be waived but not assigned [VERIFY]
- **Civil law (EU)**: Many jurisdictions require specifying fields of exploitation for copyright transfers. Moral rights are often inalienable [VERIFY]

### 4. Data Protection

**Key elements to review:**

- Whether a Data Processing Agreement/Addendum (DPA) is required
- Data controller vs. data processor classification
- Sub-processor rights and notification obligations
- Data breach notification timeline
- Cross-border data transfer mechanisms
- Data deletion or return obligations on termination
- Data security requirements and audit rights
- Purpose limitation for data processing

**Common issues:**

- No DPA when personal data is being processed
- Blanket authorization for sub-processors without notification
- Breach notification timeline longer than regulatory requirements
- No cross-border transfer protections when data moves internationally
- Inadequate data deletion provisions

[JURISDICTION-SPECIFIC] Key variations:

- **EU (GDPR)**: 72-hour breach notification to supervisory authority. SCCs or adequacy decisions for transfers. Art. 28 processor requirements [VERIFY]
- **UK**: UK GDPR + DPA 2018. UK IDTA or UK Addendum to EU SCCs for transfers. ICO is the supervisory authority [VERIFY]
- **US**: Patchwork of state laws (CCPA/CPRA, state breach notification). No single federal data protection law [VERIFY]
- **Brazil (LGPD)**: ANPD is the authority. Transfer mechanisms differ from GDPR [VERIFY]

### 5. Term and Termination

**Key elements to review:**

- Initial term and renewal terms
- Auto-renewal provisions and notice periods
- Termination for convenience: available? notice period? early termination fees?
- Termination for cause: cure period? what constitutes cause?
- Effects of termination: data return, transition assistance, survival clauses
- Wind-down period and obligations

**Common issues:**

- Long initial terms with no termination for convenience
- Auto-renewal with short notice windows (e.g., 30-day notice for annual renewal)
- No cure period for termination for cause
- Inadequate transition assistance provisions
- Survival clauses that effectively extend the agreement indefinitely

[JURISDICTION-SPECIFIC] Key variations:

- **Common law**: Termination for breach generally requires a "material" or "repudiatory" breach. Contractual termination clauses supplement common law rights [VERIFY]
- **Civil law**: Termination rights may be governed by specific code provisions. Open-ended obligations often have a statutory right to terminate on notice [VERIFY]
- **Early termination fees**: Check whether the jurisdiction's penalty/liquidated damages doctrine constrains these (e.g., UK penalty doctrine, civil law miarkowanie) [VERIFY]

### 6. Governing Law and Dispute Resolution

**Key elements to review:**

- Choice of law (governing jurisdiction)
- Dispute resolution mechanism (litigation, arbitration, mediation, expert determination)
- Venue and jurisdiction for litigation
- Arbitration institution, rules, and seat (if arbitration)
- Escalation provisions (negotiation, mediation before formal proceedings)
- Costs and fees provisions

**Common issues:**

- Unfavorable jurisdiction (unusual or remote venue)
- Mandatory arbitration with rules favorable to the drafter
- No escalation process before formal dispute resolution
- Unclear or "pathological" arbitration clauses (ICC guidance warns against ambiguity)

[JURISDICTION-SPECIFIC] Key variations:

- **US**: Jury waiver, class action waiver, and prevailing party attorney's fees are common and meaningful provisions [VERIFY]
- **England & Wales**: No jury trials or class actions in commercial disputes. "Loser pays" is the default. Exclusive vs. non-exclusive jurisdiction matters [VERIFY]
- **Civil law**: Many jurisdictions do not have jury trials or US-style class actions. Concepts like "jury waiver" may be meaningless [VERIFY]
- **International**: New York Convention governs enforcement of foreign arbitral awards. Multi-tiered escalation clauses (negotiation → mediation → arbitration) are best practice for cross-border agreements [VERIFY]

### 7–14. Standard Clause Checklist

For the following clause categories, review presence, reasonableness, and alignment with
the playbook. Flag deviations using the same GREEN/YELLOW/RED system.

**7. Confidentiality**

- [ ] Scope of confidential information defined and reasonable
- [ ] Term of confidentiality obligations appropriate (typically 2-5 years, or indefinite for trade secrets)
- [ ] Standard carveouts present (public domain, independent development, required by law)
- [ ] Return or destruction obligations on termination
- [ ] Permitted disclosures (affiliates, advisors, under NDA)

**8. Representations and Warranties**

- [ ] Scope appropriate for the contract type
- [ ] Disclaimers reasonable (e.g., "AS IS" for software)
- [ ] Survival period defined
- [ ] Remedies for breach specified (or deferred to indemnification)
- [ ] Warranty of authority and enforceability included

**9. Insurance**

- [ ] Coverage types and minimums specified
- [ ] Evidence of coverage (certificates) required
- [ ] Additional insured status requested where appropriate
- [ ] Coverage period extends through the engagement and a tail period

**10. Assignment**

- [ ] Consent required for assignment (or "not to be unreasonably withheld")
- [ ] Change of control provisions addressed
- [ ] Exceptions for affiliates or corporate restructuring
- [ ] Anti-assignment clause is mutual

**11. Force Majeure**

- [ ] Events are specifically enumerated (not just "acts of God")
- [ ] Pandemic/epidemic explicitly addressed or excluded
- [ ] Notification and mitigation obligations specified
- [ ] Duration threshold for triggering termination rights
- [ ] Cyber attack / infrastructure failure addressed (post-2020 best practice)

**12. Payment Terms**

- [ ] Net payment terms specified (Net 30, Net 60, etc.)
- [ ] Late payment interest and consequences defined
- [ ] Tax responsibilities clearly allocated
- [ ] Price escalation or adjustment mechanisms (for multi-year contracts)
- [ ] Invoice dispute process defined
- [ ] Currency and payment method specified

**13. Compliance and Regulatory**

- [ ] Anti-bribery and anti-corruption representations and obligations
- [ ] Sanctions and export control compliance
- [ ] Modern slavery / human trafficking statement (where required by law)
- [ ] Regulatory approval requirements identified
- [ ] Audit rights for compliance verification
- [ ] Consequences of compliance breach (typically a termination trigger)

**14. Definitions and Boilerplate**

- [ ] Key terms defined consistently and used throughout
- [ ] Entire agreement / integration clause present
- [ ] Severability clause present
- [ ] Waiver clause (no implied waiver from failure to enforce)
- [ ] Notice provisions (method, addresses, deemed receipt)
- [ ] Amendment provisions (written amendments only)
- [ ] Counterparts clause (if applicable)
- [ ] No third-party beneficiary clause (or appropriate third-party rights)
- [ ] Order of precedence (if multiple documents form the agreement)

### 15. AI and Technology Provisions

**Key elements to review:**

- Whether the contract permits or restricts AI tool use in performance of obligations
- Ownership of AI-generated work product and deliverables
- Restrictions on using contract data or confidential information for AI model training
- Representations about AI use in creating deliverables
- Algorithmic accountability and explainability requirements
- AI-related liability allocation (who bears risk of AI errors or bias)
- Compliance with applicable AI regulations (EU AI Act, state-level laws)

**Common issues:**

- Silence on AI use when vendor clearly uses AI tools in service delivery
- Broad license grants that inadvertently permit AI training on customer data
- No representations about AI-generated content accuracy or bias
- Work-for-hire / IP assignment that does not address AI-generated elements
- No audit rights for algorithmic decisions affecting the customer

[JURISDICTION-SPECIFIC] Key variations:

- **EU**: AI Act (Regulation 2024/1689) imposes obligations on deployers and providers of AI systems. Contracts involving AI should address Art. 4 AI literacy requirements and relevant risk-tier obligations [VERIFY]
- **US**: No comprehensive federal AI law; patchwork of state-level requirements (Colorado AI Act, Illinois BIPA for biometric AI, NYC Local Law 144 for automated employment decisions) [VERIFY]
- **International**: OECD AI Principles provide a non-binding framework. ISO/IEC 42001 (AI Management Systems) is an emerging standard [VERIFY]

### 16. ESG and Supply Chain

**Key elements to review:**

- Environmental sustainability commitments and reporting obligations
- Carbon footprint reduction targets or net-zero commitments
- Human rights and labor standards in the supply chain
- Supply chain due diligence obligations
- ESG audit and monitoring rights
- Consequences for ESG non-compliance (termination, remediation plans)
- Conflict minerals and responsible sourcing
- Diversity, equity, and inclusion commitments

**Common issues:**

- Vague sustainability commitments without measurable targets or deadlines
- Supply chain due diligence obligations that exceed the party's practical ability to monitor
- No remediation pathway before termination for ESG non-compliance
- Missing conflict minerals or responsible sourcing provisions in manufacturing contracts

[JURISDICTION-SPECIFIC] Key variations:

- **EU**: Corporate Sustainability Due Diligence Directive (CSDDD) requires supply chain due diligence. CSRD imposes sustainability reporting obligations [VERIFY]
- **Germany**: Supply Chain Due Diligence Act (LkSG) in force. Requires companies above thresholds to monitor human rights and environmental risks in supply chains [VERIFY]
- **France**: Duty of Vigilance Law (Loi de vigilance) imposes similar supply chain obligations on large companies [VERIFY]
- **UK**: Modern Slavery Act s.54 requires annual statements. No comprehensive supply chain due diligence law yet [VERIFY]

---

## Deviation Severity Classification

### GREEN — Acceptable

The clause aligns with or is better than the organization's standard position. Minor
variations that are commercially reasonable and do not materially increase risk.

**Examples:**

- Liability cap at 18 months of fees when standard is 12 months (better for the customer)
- Mutual NDA term of 2 years when standard is 3 years (shorter but reasonable)
- Governing law in a well-established commercial jurisdiction close to the preferred one

**Action**: Note for awareness. No negotiation needed.

### YELLOW — Negotiate

The clause falls outside the standard position but within a negotiable range. The term is
common in the market but not the organization's preference. Requires attention and likely
negotiation, but not escalation.

**Examples:**

- Liability cap at 6 months of fees when standard is 12 months
- Unilateral indemnification for IP infringement when standard is mutual
- Auto-renewal with 60-day notice when standard is 90 days
- Governing law in an acceptable but not preferred jurisdiction

**Action**: Generate specific redline language. Provide fallback position. Estimate
business impact of accepting vs. negotiating.

### RED — Escalate

The clause falls outside the acceptable range, triggers a defined escalation criterion, or
poses material risk. Requires senior counsel review, outside counsel involvement, or
business decision-maker sign-off.

**Examples:**

- Uncapped liability or no limitation of liability clause
- Unilateral broad indemnification with no cap
- IP assignment of pre-existing IP
- No DPA offered when personal data is processed
- Unreasonable non-compete or exclusivity provisions
- Clauses that are likely void or unenforceable under the governing law
- Governing law in a problematic jurisdiction with mandatory arbitration
- No anti-bribery provisions in a contract with corruption-risk jurisdictions
- Broad AI training rights on customer confidential data without consent

**Action**: Explain the specific risk (with legal basis where possible). Provide
market-standard alternative language. Estimate exposure. Recommend escalation path.

---

## Redline Format

For each redline:

```
**Clause**: [Section reference and clause name]
**Current language**: "[exact quote from the contract]"
**Proposed redline**: "[specific alternative language]"
**Rationale**: [1-2 sentences explaining why, suitable for external sharing]
**Legal basis**: [Relevant statute, regulation, or principle — or "General commercial practice"]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative position if primary redline is rejected]
```

### Redline Best Practices

1. **Be specific**: Provide exact language, not vague guidance. The redline should be ready to insert.
2. **Be balanced**: Propose language that is firm on critical points but commercially reasonable. Overly aggressive redlines slow negotiations.
3. **Explain the rationale**: Include a brief, professional rationale suitable for sharing with the counterparty's counsel.
4. **Provide fallback positions**: For YELLOW items, include a fallback if the primary ask is rejected.
5. **Prioritize**: Not all redlines are equal. Indicate which are must-haves and which are nice-to-haves.
6. **Consider the relationship**: Adjust tone based on whether this is a new vendor, strategic partner, or commodity supplier.
7. **Reference applicable law**: Where the redline addresses a legal risk, cite the relevant statute or principle. If citing from memory, mark with [VERIFY].

---

## Negotiation Priority Framework

When presenting redlines, organize by negotiation priority:

### Tier 1 — Must-Haves (Deal Breakers)

Issues where the organization cannot proceed without resolution:

- Uncapped or materially insufficient liability protections
- Missing data protection requirements for regulated data
- IP provisions that could jeopardize core assets
- Terms that conflict with regulatory obligations
- Clauses void or unenforceable under the governing law
- Absent compliance provisions in regulated or cross-border contexts
- AI-related risks to confidential data or trade secrets

### Tier 2 — Should-Haves (Strong Preferences)

Issues that materially affect risk but have negotiation room:

- Liability cap adjustments within range
- Indemnification scope and mutuality
- Termination flexibility and cure periods
- Audit and compliance rights
- Change-of-control assignment protections
- AI use transparency and accountability provisions

### Tier 3 — Nice-to-Haves (Concession Candidates)

Issues that improve the position but can be conceded strategically:

- Preferred governing law (if alternative is acceptable)
- Notice period preferences
- Minor definitional improvements
- Insurance certificate requirements
- Boilerplate refinements
- ESG reporting frequency and format

**Negotiation strategy**: Lead with Tier 1 items. Trade Tier 3 concessions to secure
Tier 2 wins. Never concede on Tier 1 without escalation.

---

## Quality Assurance Framework

### PDCA Quality Cycle

Apply structured discipline to every contract review:

**PLAN**: Identify contract type, user's side, playbook position. Classify complexity
(standard / bespoke / high-value). Identify which statutes, regulations, and legal
principles are likely to be engaged.

**DO**: Execute the clause-by-clause analysis and missing clause detection. Generate
redlines. Score severity.

**CHECK**: Run the Citation Quality Gates. For any RED item, run the Self-Interrogation.
Verify all statutory references against authoritative sources where possible. Confirm all
16 clause categories addressed.

**ACT**: Record any new patterns discovered (novel clause structure, emerging market
position). Flag heuristics for future reviews. If the review changes your understanding
of a standard position, note it for playbook update.

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                   | Fail Action                                                 |
| -------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established principle                       | Add citation or mark as "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction                            | Fix format                                                  |
| **Currency**   | Every cited provision checked for amendments or repeal against authoritative sources where accessible  | Flag as "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the contract's governing law. No assumptions from other jurisdictions leaking in | Remove or flag jurisdictional bleed                         |
| **Confidence** | Uncertainty explicitly stated, not hidden. If you are not certain of a legal position, say so          | Add confidence qualifier                                    |

### Self-Interrogation for RED Items

For any clause classified as RED, apply this 3-pass self-interrogation before delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the risk assessment follow logically from the statute/principle cited?
- Would a court in this jurisdiction actually reach this conclusion on these facts?
- Is there a counter-argument the counterparty's counsel will make?

**Pass 2 — Completeness**:

- Have all relevant statutes and regulations been considered?
- Have any relevant cases or principles been missed?
- Are there regulatory dimensions not yet considered?

**Pass 3 — Challenge**:

- What is the strongest argument that this clause IS acceptable?
- Under what commercial circumstances might a reasonable lawyer accept this risk?
- Is the RED classification proportionate, or is this actually YELLOW with mitigations?

If any pass reveals a weakness, revise the analysis before delivery. Mark the audit trail
with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material clause analysis, assign a confidence level:

| Level        | Range     | Meaning                                          | Action                                                   |
| ------------ | --------- | ------------------------------------------------ | -------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled law, clear statute, no ambiguity         | State with confidence                                    |
| **High**     | 0.80-0.94 | Strong authority, minor interpretation questions | State with brief caveat                                  |
| **Probable** | 0.60-0.79 | Good arguments but reasonable minds could differ | State with explicit reasoning and contra-indicators      |
| **Possible** | 0.40-0.59 | Genuinely uncertain, competing authorities       | Flag for counsel review with both sides of the argument  |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative                          | Do not assert; flag as "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every contract review output MUST include a Glass Box audit section at the end. This makes
the reasoning traceable and auditable:

```yaml
glass_box:
  contract: "[Contract title and date]"
  contract_type: "[SaaS / Professional Services / License / etc.]"
  user_side: "[Supplier / Customer / Licensor / Licensee]"
  governing_law: "[Jurisdiction identified from the contract]"
  playbook_used: "[Playbook name or 'General commercial standards']"
  review_basis: "[Organizational playbook / General commercial standards]"
  clauses_reviewed: 16
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to temp file or 'Not created']"
  statutes_consulted:
    - "[Statute 1 — VERIFIED (legalcode-mcp) or UNVERIFIED]"
    - "[Statute 2 — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  case_law_consulted:
    - "[Case 1 — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified legal review"
```

---

## Multi-Stakeholder Mapping

For every contract, identify ALL affected stakeholders — not just the two contracting
parties:

| Stakeholder            | Role        | Affected Clauses                | Impact     | Action Required               |
| ---------------------- | ----------- | ------------------------------- | ---------- | ----------------------------- |
| [Party A]              | [Customer]  | [All]                           | Primary    | Sign / Negotiate              |
| [Party B]              | [Supplier]  | [All]                           | Primary    | Sign / Negotiate              |
| [Data subjects]        | Third party | Data protection                 | Indirect   | DPA required                  |
| [Sub-processors]       | Third party | Data protection, liability      | Indirect   | Notification rights           |
| [Regulator]            | Regulator   | Data protection, compliance, AI | Compliance | Breach notification           |
| [Employees]            | Internal    | IP, confidentiality, AI         | Indirect   | Employment contract alignment |
| [End users]            | Third party | Liability, data protection, AI  | Indirect   | Terms of service alignment    |
| [Supply chain workers] | Third party | ESG, compliance                 | Indirect   | Due diligence obligations     |

This prevents the common failure of reviewing a contract as a two-party document when it
affects multiple stakeholders with different interests and regulatory requirements.

---

## Anti-Patterns

Explicit catalogue of what NOT to do in contract review:

1. **Single-pass analysis** — A contract review that reads each clause once, in order, will miss interactions between clauses (e.g., an uncapped indemnity partially mitigated by a limitation clause). Read the whole contract, then analyze.

2. **Citing statutes from memory without verification** — Statutes are amended, repealed, and renumbered. Case citations may not exist. If you cannot verify a citation against an authoritative source, mark it [VERIFY] or "[UNVERIFIED — counsel to confirm]." Never present an unverified citation as settled law.

3. **Applying jurisdiction-specific concepts universally** — Work-for-hire exists in the US but not England or civil law systems. Kary umowne (penalty clauses) are a Polish concept with no direct common law equivalent. UCTA is English law only. Always check whether a concept applies under the contract's governing law.

4. **Treating indemnities as equivalent to damages claims** — In many common law jurisdictions, an indemnity is a primary obligation with different remoteness rules and limitation periods than a damages claim. In civil law jurisdictions, the concept may not be native at all. Analyze accordingly.

5. **Reviewing limitation clauses without checking statutory enforceability** — Many jurisdictions impose statutory limits on what liability can be excluded (UCTA in England, unconscionability in the US, mandatory civil code provisions in civil law). Skipping this check is a material omission.

6. **Accepting "consequential loss" at face value** — The contract may redefine "consequential" or "indirect" differently from the legal default. Always check the definitions clause.

7. **Ignoring the penalty doctrine for termination fees** — Early termination fees and liquidated damages must be assessed against the governing law's penalty doctrine. Don't just flag the amount — assess proportionality.

8. **Redlines without fallback positions** — A redline that says "delete this clause" without offering an alternative is a negotiation dead-end. Always provide a fallback.

9. **Importing terminology from the wrong jurisdiction** — "Attorney's fees," "punitive damages," "class action waiver," and "jury waiver" have no meaning in many jurisdictions. Don't import them into analysis governed by a legal system where they are irrelevant.

10. **Confidence without evidence** — Never state "this clause is unenforceable" without citing the specific statute, regulation, or principle that renders it so. Confident assertions without authority are more dangerous than expressed uncertainty.

11. **Reviewing for one party while assuming the other's interests** — The analysis must be from the user's stated side. What protects a vendor harms a customer and vice versa. Confirm the side before analyzing.

12. **Skipping the holistic view** — Individual clause analysis is necessary but not sufficient. The contract must also be assessed as a whole: is the overall risk allocation balanced? Do the commercial terms make business sense? Are any provisions internally contradictory?

13. **Ignoring what is missing** — Focusing only on clauses that are present and ignoring absent clauses. A contract with no limitation of liability, no DPA, or no termination rights has material gaps that must be flagged.

14. **Treating boilerplate as irrelevant** — Entire agreement clauses, severability, notice provisions, and order of precedence can have significant legal consequences. A missing entire agreement clause may allow parol evidence; an incorrect order of precedence can invert the deal terms.

15. **Assuming instead of asking** — Silently assuming the user's side, risk tolerance, deal context, or preferred outcome when it would change the analysis. A liability cap that is RED for a risk-averse enterprise may be YELLOW for a startup that needs the deal. When in doubt, ask.

16. **Overlooking AI-related risks** — Failing to flag AI use provisions, training data rights, or algorithmic accountability when the contract involves AI-powered services. These are emerging but increasingly material contract risks.

17. **Treating ESG clauses as non-binding aspirations** — ESG commitments in contracts can create legally binding obligations with real consequences. Supply chain due diligence requirements (LkSG, CSDDD) impose obligations that flow through contracts. Analyze ESG provisions with the same rigor as commercial terms.

---

## Writing Standards

Apply plain-language discipline to all output:

**For redline rationales** (shared with counterparty's counsel):

- Plain language. No jargon or filler.
- Active voice: "This clause excludes liability for negligence" not "Liability for negligence is excluded by this clause"
- Short sentences. One point per sentence.
- Name the actor: "The supplier must..." not "It is required that..."
- Specific, not vague: cite the relevant provision rather than saying "this may have enforceability issues"

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
legalcode-mcp is a law, regulatory, and case law database with powerful search across
jurisdictions.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for jurisdiction-relevant statutes, regulations, and case law
- Save the most relevant results to a local temp file (`/tmp/legalcode-review-authority.md`)
- Reference verified authority from the temp file throughout the clause analysis
- For RED items, search for additional case law to support or challenge the classification
- Check statutory currency (amendments, repeal, superseding legislation)
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `external_tools_used: "None — manual verification required"`
- Include a prominent notice that legal citations require independent verification
- Focus the analysis on commercial risk assessment and structural issues rather than legal certainty
- Do not create the local authority reference file

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Contract Review Summary

**Document**: [contract name/identifier]
**Parties**: [party names and roles]
**Your Side**: [vendor/customer/etc.]
**Governing Law**: [jurisdiction]
**Deadline**: [if provided]
**Review Basis**: [Playbook name / General Commercial Standards]
**Date of Review**: [date]

---

## Key Findings

[Top 3-5 issues with severity flags (RED/YELLOW) and one-line summaries]

---

## Missing Clauses

[List any of the 16 clause categories that are absent, with severity assessment]

---

## Clause-by-Clause Analysis

### [Clause Category] — [GREEN / YELLOW / RED] | Confidence: [level]

**Contract says**: [summary of the provision]
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

## Stakeholder Impact Map

[Table per Multi-Stakeholder Mapping section]

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
3. Add jurisdiction-specific clause categories (e.g., penalty clauses for civil law, TUPE for UK employment)
4. Add jurisdiction-specific anti-patterns
5. Update the frontmatter name and description to reference the specific jurisdiction
6. Add relevant case law and statutory framework sections

Existing jurisdiction-specific variants:

- **England & Wales**: `imported-uk-legal-plugins--skills-uk-legal-contract-review/SKILL.md`
- **Poland**: `imported-iura-plugins--iura-pl-skills-contract-review/SKILL.md`

---

## Provenance

Enhanced by Legalcode (2026-02-28). Originally imported from
`anthropics/knowledge-work-plugins/legal/commands/review-contract.md` (2026-02-27).
Enhanced to Legalcode gold standard quality using the legalcode-skill-enhancement workflow
with Agent Team analysis (structural + prompt engineering) and legal topic research. Based
on the `legalcode-contract-review` reference standard with additions: expanded to 16 clause
categories (AI Provisions, ESG/Supply Chain), updated anti-patterns catalogue (17 items),
modern regulatory coverage (EU AI Act, CSDDD, LkSG), and enhanced stakeholder mapping.
