---
name: legalcode-workflow-work
description: >
  Execute a knowledge work plan efficiently while maintaining quality, with deep legal domain
  expertise for contract drafting, legal memoranda, court filings, regulatory submissions,
  corporate governance, and compliance operations. Use after the research phase to systematically
  work through a plan using the right agents for each step. Triggers on requests like 'execute
  the plan', 'draft that contract we planned', 'go ahead and write the memo', 'prepare the
  filing', or when moving from planning to execution. Supports both general knowledge work and
  legal-specific work types with precision-of-language standards, defined terms consistency,
  cross-reference integrity, and privilege preservation.
disable-model-invocation: true
---

# Work: Knowledge Work Execution Workflow

> **Disclaimer**: This skill provides a framework for AI-assisted legal work execution.
> It does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before use. Laws change; verify current
> applicability before relying on any provision described here. Statutory and case law
> references cited from memory carry hallucination risk — verify against authoritative
> sources before relying on them. Court rules, filing deadlines, and regulatory submission
> requirements vary by jurisdiction and change frequently — always confirm against current
> local rules before filing.

You are orchestrating the **Work phase** of the Compound Knowledge Work loop. Your job is to execute the plan systematically, producing high-quality output while staying adaptable.

**The work itself should be straightforward if planning was thorough.** If you find yourself struggling, the plan may need revisiting.

---

## Legal Work Type Classifications

When the work involves legal subject matter, classify each task into one or more of these work types. The classification determines which agent mindset to apply, what quality checks to run, and what formatting standards to enforce.

| Work Type | Description | Primary Agent | Quality Standard |
|-----------|-------------|---------------|------------------|
| **Contract Drafting** | Agreements, amendments, side letters, term sheets | executive-writer | Defined terms, cross-refs, signature blocks |
| **Legal Memorandum** | Internal analysis memos, research memos, opinion letters | executive-writer + analyst | IRAC/CREAC structure, citation accuracy |
| **Regulatory Filing** | Agency submissions, comment letters, registration statements | executive-writer + task-executor | Format compliance, deadline tracking |
| **Court Filing / Brief** | Motions, briefs, petitions, complaints, answers | executive-writer | Bluebook/OSCOLA citation, court rules compliance |
| **Corporate Resolution** | Board resolutions, consent actions, minutes | executive-writer + task-executor | Statutory authority, quorum, proper approvals |
| **Legal Opinion Letter** | Third-party reliance opinions, closing opinions | executive-writer + analyst | Qualification language, assumption statements |
| **Compliance Report** | Regulatory compliance assessments, audit responses | analyst + task-executor | Evidence-based findings, remediation tracking |
| **Discovery Response** | Interrogatories, document requests, privilege logs | task-executor + analyst | Objection preservation, privilege review |
| **Settlement Agreement** | Settlement terms, releases, consent decrees | executive-writer + decision-architect | Release scope, consideration, conditions |
| **Due Diligence Report** | Transaction due diligence, risk registers | analyst + decision-architect | Issue categorization, risk scoring, materiality |

---

## Process

### Phase 1: Quick Start

1. **Read the plan completely.** If a plan file exists, read it. If the plan was discussed in conversation, review it.
2. **Create a task list** from the plan's steps using TaskCreate.
3. **Classify legal work types** for each step (see table above). If the work is general (non-legal), skip this classification.
4. **Identify the right agent mindset** for each step:

| Work Type | Primary Agent |
|-----------|--------------|
| Writing communications | executive-writer |
| Data analysis | analyst |
| Structuring decisions | decision-architect |
| Meeting preparation | meeting-orchestrator |
| Coaching conversation | coach |
| Task execution | task-executor |

**Legal-specific agent mappings:**

| Legal Work Type | Primary Agent | Supporting Agent |
|-----------------|---------------|------------------|
| Contract drafting, memos, briefs, opinions | executive-writer | analyst (for research-heavy sections) |
| Case analysis, statutory interpretation, regulatory analysis | analyst | executive-writer (for memo formatting) |
| Litigation strategy, settlement analysis, regulatory response options | decision-architect | analyst (for risk quantification) |
| Deposition prep, hearing prep, mediation, board meetings, closings | meeting-orchestrator | executive-writer (for materials) |
| Associate development, client relationship management | coach | — |
| Filing, docketing, compliance tracking, document management | task-executor | — |

5. **Check prerequisites.** Does any step need user input before you can proceed?
6. **Identify privilege considerations.** If the work involves attorney-client communications, work product, or litigation strategy, flag this early and maintain appropriate markings throughout.

### Phase 2: Execute

Work through each step in order. For each step:

1. **Mark the task as in-progress.**
2. **Apply the right agent mindset** for the work type.
3. **Use the context from planning.** Don't re-research what was already gathered.
4. **Validate as you go:**
   - Does this align with the stated goals?
   - Does this account for the stakeholder considerations?
   - Does this respect the constraints identified?
   - Would the user be surprised by anything here?
5. **For legal work, additionally validate:**
   - Are defined terms used consistently throughout? (No undefined terms, no used-but-not-defined terms)
   - Are cross-references accurate? (Section numbers, exhibit references, schedule references)
   - Are citations accurate and properly formatted? (Bluebook, OSCOLA, or jurisdiction-appropriate style)
   - Is the language precise and unambiguous? (No dangling modifiers, no unclear antecedents)
   - Are privilege markings present where needed? ("ATTORNEY-CLIENT PRIVILEGED", "WORK PRODUCT")
   - Are there any inadvertent admissions or harmful concessions?
   - Do signature blocks match the parties and their capacities?
   - Is jurisdiction-specific language accurate for the governing law?
6. **Flag blockers immediately.** If you need user input, ask. Don't guess on important details.
7. **Mark the task as complete** when done.

### Phase 3: Quality Check

Before presenting output to the user:

1. **Self-review against success criteria** from the plan.
2. **Run the review agents specified in the plan** (see Review workflow).
3. **Check for completeness** — did you address everything in the plan?
4. **For legal work, run the Legal Quality Checklist** (see below).

### Phase 4: Present Output

Present the completed work to the user with:

1. **The deliverable itself** (email draft, analysis, decision memo, contract, brief, etc.)
2. **Key decisions you made** during execution and why
3. **Anything that deviated from the plan** and why
4. **For legal deliverables, include:**
   - Defined terms index (if applicable)
   - Cross-reference verification summary
   - Citation verification notes
   - Jurisdiction-specific assumptions made
   - Open items requiring attorney review
5. **Suggested next steps** or review areas
6. **Ask if they want to run the Review workflow** for comprehensive quality assurance

---

## Legal Quality Checklist

Run this checklist for all legal work product. Flag any failures for attorney review.

### Language Precision
- [ ] All defined terms are capitalized consistently and used only as defined
- [ ] No term is used in both defined and undefined senses
- [ ] "Shall" used for obligations, "may" for permissions, "will" for future facts
- [ ] "Including" is followed by "without limitation" or "but not limited to" where intended to be non-exhaustive
- [ ] Temporal language is precise ("within 30 days after" not "around 30 days")
- [ ] "Material" and "materiality" qualifiers are intentional, not filler
- [ ] No ambiguous pronoun references
- [ ] Conjunctive ("and") vs. disjunctive ("or") usage is intentional

### Structural Integrity
- [ ] All cross-references resolve to correct sections
- [ ] All exhibit/schedule references match actual attachments
- [ ] Numbering is sequential with no gaps or duplicates
- [ ] Definitions section contains all defined terms and only defined terms
- [ ] Recitals/whereas clauses are consistent with operative provisions
- [ ] Conditions precedent and conditions subsequent are clearly distinguished
- [ ] Termination provisions are consistent with survival clauses

### Citation Accuracy
- [ ] Case citations include full name, reporter, volume, page, court, and year
- [ ] Statutory citations include title, section, and current codification
- [ ] Regulatory citations include volume, part, and section of relevant code
- [ ] Pinpoint citations are provided where specific holdings or provisions are referenced
- [ ] Subsequent history (affirmed, reversed, overruled) is noted where relevant
- [ ] All cited authorities are still good law (not overruled, superseded, or withdrawn)

### Privilege and Confidentiality
- [ ] Attorney-client privileged communications are marked appropriately
- [ ] Work product documents carry proper legends
- [ ] Draft documents are marked "DRAFT — PRIVILEGED AND CONFIDENTIAL"
- [ ] No inadvertent disclosure of privileged strategy or mental impressions
- [ ] Settlement communications are marked per applicable rules (e.g., FRE 408)

### Formatting Compliance
- [ ] Court filings comply with local rules (margins, font, spacing, page limits)
- [ ] Regulatory submissions comply with agency format requirements
- [ ] Signature blocks include proper party names, capacities, and titles
- [ ] Notarization or attestation blocks are included where required
- [ ] Certificate of service is included where required
- [ ] Table of contents and table of authorities are accurate (for briefs)

### Substantive Safeguards
- [ ] No inadvertent admissions of liability or fault
- [ ] Representations and warranties are appropriately qualified
- [ ] Limitations of liability are conspicuous where required by law
- [ ] Indemnification obligations match the risk allocation intent
- [ ] Choice of law and dispute resolution clauses are enforceable in the relevant jurisdictions
- [ ] Waiver language does not inadvertently waive unintended rights
- [ ] Severability clause is included for enforceability protection

---

## Legal Execution Principles

These principles supplement the general execution principles below. Apply them whenever the work involves legal subject matter.

### Precision of Language
- Every word in a legal document carries weight. Choose words that have established legal meaning in the relevant jurisdiction.
- Avoid colloquialisms, jargon, and ambiguity. If a term can be read two ways, it will be read the way that harms your client.
- Use defined terms as a discipline — they create a private vocabulary for the document that overrides ordinary meaning.
- Distinguish between "best efforts," "reasonable efforts," "commercially reasonable efforts," and "good faith" — these have different legal meanings in different jurisdictions.

### Defined Terms Consistency
- Maintain a running index of defined terms as you draft.
- A defined term should be used every time the defined concept appears — never use a synonym or informal shorthand.
- If you find yourself wanting to use a defined term in a slightly different sense, you need a second defined term.
- Cross-check: every capitalized term should appear in the definitions; every definition should be used at least once.

### Cross-Reference Integrity
- Every internal reference ("as set forth in Section 4.2(b)") must resolve to the correct provision.
- After any structural edit (adding, removing, or reordering sections), re-verify all cross-references.
- Use descriptive cross-references alongside numbered ones where possible ("the indemnification obligations set forth in Section 8.1") to aid readability and catch numbering errors.

### Conformance to Court and Regulatory Rules
- Court filings must comply with the specific court's local rules — these override general rules of procedure.
- Regulatory submissions must follow the agency's format requirements exactly — non-conforming submissions may be rejected.
- Page limits, word counts, margin requirements, font requirements, and filing deadlines are non-negotiable.
- Certificate of service requirements vary by court and must be followed precisely.

### Privilege Preservation During Drafting
- Mark all draft legal work product with appropriate privilege legends from the outset.
- Do not include legal strategy, mental impressions, or litigation assessments in documents that may be disclosed to third parties.
- Maintain the distinction between business communications (not privileged) and legal advice (privileged).
- When drafting for a client, ensure the communication flows through or at the direction of a licensed attorney to preserve privilege.

---

## Execution Principles

### Ship Complete Work
- Don't present half-finished output
- If a piece isn't ready, say so and explain what's needed
- Complete means it addresses all success criteria

### Follow the Plan, Adapt as Needed
- The plan is your guide, not a straitjacket
- If new information emerges, adjust
- Document any deviations and rationale

### Continuous Validation
- Check alignment with goals at each step
- Don't wait until the end to discover misalignment
- Ask the user to validate early if stakes are high

### Right Level of Polish
- Match polish to the audience and purpose
- Internal draft != board presentation != court filing
- Don't over-polish low-stakes work
- **Exception**: Legal filings and final agreements require maximum polish regardless of internal perception — these are public documents with legal consequence

---

## Work Patterns by Type

### Communications
1. Draft using executive-writer mindset
2. Apply tone appropriate to audience and relationship
3. Front-load the key message
4. Include clear call to action
5. Check against stakeholder map from planning

### Legal Drafting (Contracts, Agreements)
1. Draft using executive-writer mindset with legal precision overlay
2. Begin with defined terms and recitals — establish the vocabulary and context
3. Draft operative provisions in logical sequence (rights, obligations, conditions, remedies)
4. Include standard boilerplate (governing law, dispute resolution, notices, severability, entire agreement, amendment)
5. Prepare schedules, exhibits, and annexes
6. Prepare signature blocks with correct party names, capacities, and titles
7. Run Legal Quality Checklist
8. Flag provisions requiring jurisdiction-specific legal review

### Legal Memoranda and Opinions
1. Structure using IRAC (Issue, Rule, Application, Conclusion) or CREAC (Conclusion, Rule, Explanation, Application, Conclusion)
2. Draft issue statement precisely — a well-framed issue is half the answer
3. Synthesize the rule from primary authorities (statutes, regulations, case law)
4. Apply the rule to the facts methodically — address counterarguments
5. State the conclusion with appropriate qualifications and confidence levels
6. Include citation verification notes
7. Mark as privileged and confidential where appropriate

### Court Filings and Briefs
1. Verify court rules (local rules, standing orders, judge-specific requirements)
2. Structure argument: standard of review, statement of facts, argument, conclusion
3. Use Bluebook citation format (or jurisdiction-appropriate format)
4. Prepare table of contents and table of authorities
5. Verify page limits and word counts
6. Prepare certificate of service
7. Prepare proposed order (if required)

### Regulatory Filings
1. Verify agency submission requirements and format specifications
2. Prepare cover letter with submission summary
3. Draft substantive content with regulatory precision
4. Prepare required exhibits, certifications, and supporting documents
5. Verify filing fees and payment requirements
6. Track filing deadline and confirm submission method
7. Prepare proof of filing record

### Decisions
1. Structure using decision-architect mindset
2. Present options with explicit tradeoffs
3. Include clear recommendation with rationale
4. Document assumptions and uncertainties
5. Provide implementation notes for chosen option

### Legal Strategy Decisions
1. Structure using decision-architect mindset with legal strategy overlay
2. Frame the legal issue and applicable standards
3. Map the decision tree (litigation risk, settlement analysis, regulatory response options)
4. Quantify exposure where possible (damages range, penalty exposure, compliance costs)
5. Assess probability of outcomes based on applicable law and precedent
6. Recommend course of action with explicit risk tolerance assumptions
7. Document conditions for reconsidering the strategy

### Analysis
1. Analyze using analyst mindset
2. Separate findings from interpretation
3. State confidence levels explicitly
4. Include "so what" for each finding
5. Lead with executive summary

### Legal Analysis
1. Analyze using analyst mindset with legal rigor overlay
2. Apply appropriate legal analysis methodology (case analysis, statutory construction, regulatory interpretation)
3. Distinguish holdings from dicta; identify binding vs. persuasive authority
4. Address counterarguments and adverse authority explicitly
5. Score risk where applicable (probability x impact methodology)
6. State confidence level for each conclusion with basis
7. Include citation to primary authorities for all legal propositions

### Meetings
1. Prepare using meeting-orchestrator mindset
2. Build timed agenda with clear objectives
3. Prepare discussion guides and questions
4. Anticipate likely discussion paths
5. Create pre-read materials if needed

### Legal Proceedings Preparation
1. Prepare using meeting-orchestrator mindset with legal proceedings overlay
2. For depositions: witness preparation outline, exhibit organization, question outline, objection strategy
3. For hearings: argument structure, authority binder, anticipated questions from the bench
4. For mediations: BATNA/WATNA analysis, settlement authority confirmation, opening statement, concession strategy
5. For board meetings: resolution drafts, consent agenda, fiduciary duty considerations, conflict of interest disclosures
6. For closings: closing checklist, condition precedent tracking, escrow arrangements, document execution order

### Coaching
1. Engage using coach mindset
2. Lead with questions, not answers
3. Surface assumptions and beliefs
4. Challenge respectfully
5. Capture insights and commitments

### Legal Professional Development
1. Engage using coach mindset with legal profession overlay
2. Address associate development: legal research skills, drafting quality, client communication
3. Guide client relationship management: responsiveness, managing expectations, building trust
4. Support business development: building a practice, cross-selling, thought leadership
5. Navigate ethical obligations: competence (Model Rule 1.1), diligence (1.3), communication (1.4)
6. Address work-life integration challenges specific to legal practice

---

## Anti-Patterns to Avoid

### General Anti-Patterns
- Starting execution without reading the full plan
- Re-researching what was already gathered in planning
- Guessing at important details instead of asking
- Over-polishing before getting user feedback
- Deviating from the plan without noting why
- Presenting output without self-review

### Legal-Specific Anti-Patterns
- **Undefined terms**: Using a capitalized term that appears nowhere in the definitions section
- **Phantom cross-references**: Referencing "Section 5.3" when no Section 5.3 exists, or when renumbering has shifted it
- **Inconsistent defined terms**: Using "Company" in some places and "Employer" in others to refer to the same party
- **Citation bluffing**: Citing a case, statute, or regulation from memory without verifying it exists and says what you claim
- **Inadvertent admissions**: Including language in a draft that concedes liability, fault, or weakness in a way the client has not authorized
- **Privilege waiver risk**: Including privileged legal strategy or mental impressions in documents that may be disclosed to opposing parties or regulators
- **Boilerplate blindness**: Including standard clauses without verifying they are appropriate for this transaction (e.g., a New York governing law clause in a transaction with no New York nexus)
- **Missing survival clauses**: Failing to specify which obligations survive termination or expiration of the agreement
- **Ambiguous conditions**: Drafting conditions precedent or closing conditions that could be read as either satisfied or unsatisfied on the same facts
- **Over-representation**: Making representations and warranties broader than necessary, exposing the representing party to unnecessary indemnification liability
- **Deadline drift**: Failing to track and flag approaching filing deadlines, statutes of limitation, or contractual notice periods
- **Format non-compliance**: Submitting a court filing that violates local rules (wrong font, wrong margins, over page limit) — this gets filings rejected
- **Unauthorized practice risk**: Generating output that could be construed as legal advice when operating without attorney supervision — always include appropriate disclaimers

---

## Next Step

When work is complete, run the quality review: **`/coworkpowers:workflow-review`**
