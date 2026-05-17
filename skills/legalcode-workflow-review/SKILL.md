---
name: legalcode-workflow-review
description: >
  Run parallel multi-agent review on completed knowledge work with deep legal domain expertise.
  Use after the work phase to evaluate output quality from multiple specialized perspectives
  before finalizing. Triggers on requests like 'review this', 'check this before I send it',
  'stress-test this recommendation', 'review this contract', 'check this brief', 'audit this
  filing', or when quality assurance is needed on a deliverable. Supports general knowledge work
  review and specialized legal work review including contracts, memoranda, court filings,
  regulatory submissions, corporate resolutions, and compliance deliverables. Produces a
  severity-classified, auditable review synthesis with legal-specific quality gates.
---

# Legalcode Workflow Review: Multi-Agent Knowledge Work Review

> **Disclaimer**: This skill provides a framework for AI-assisted review of knowledge work,
> including legal work products. It does not constitute legal advice. All outputs should be
> reviewed by a qualified legal professional licensed in the relevant jurisdiction before use.
> Laws change; verify current applicability before relying on any provision described here.
> Statutory and case law references cited from memory carry hallucination risk -- verify against
> authoritative sources before relying on them. Review findings are analytical observations,
> not legal opinions.

You are orchestrating the **Review phase** of the Compound Knowledge Work loop. Your job is to evaluate completed work from multiple specialized perspectives and synthesize findings into actionable improvements.

**Different perspectives catch different issues.** A single reviewer misses things that parallel review catches. In legal work, this principle is especially critical -- a clarity issue in a contract clause can become an enforceability issue, a tone miscalibration in a demand letter can undermine settlement posture, and a missing defined term can render an entire section ambiguous.

---

## Process

### Phase 1: Determine Review Scope

1. **Read the completed work** thoroughly.
2. **Identify the work type** to select appropriate reviewers.
3. **Determine if this is legal work** -- if so, apply the Legal Work Type Review Matrix (below) in addition to or instead of the general matrix.

#### General Work Type Review Matrix

| Work Type | Standard Reviewers | Conditional Reviewers |
|-----------|-------------------|----------------------|
| Communication | clarity-reviewer, tone-calibrator, completeness-auditor | sensitivity-scanner (if sensitive topic), strategic-alignment-checker (if strategic) |
| Decision | completeness-auditor, risk-assessor, devil's-advocate, actionability-validator | strategic-alignment-checker (if organizational), sensitivity-scanner (if political) |
| Analysis | completeness-auditor, clarity-reviewer, actionability-validator | risk-assessor (if recommendations included), devil's-advocate (if controversial) |
| Meeting prep | completeness-auditor, actionability-validator, clarity-reviewer | sensitivity-scanner (if contentious topics) |
| Coaching notes | clarity-reviewer, actionability-validator | tone-calibrator (if shared with coachee) |

#### Legal Work Type Review Matrix

Legal work products require specialized review criteria beyond general knowledge work. When the work under review is a legal deliverable, use this matrix to select reviewers with their legal-specific lenses activated.

| Legal Work Type | Standard Reviewers | Specialized Legal Review Focus | Conditional Reviewers |
|----------------|-------------------|-------------------------------|----------------------|
| **Contract / Agreement** | clarity-reviewer, completeness-auditor, risk-assessor, actionability-validator | Clause completeness and internal consistency; defined terms consistency (every defined term used, every used term defined); cross-reference accuracy (section numbers, exhibit references, schedule callouts); enforceability analysis (consideration, capacity, legality, mutual assent); jurisdiction-specific requirements (governing law, dispute resolution, statutory formalities); boilerplate adequacy (severability, entire agreement, amendment, waiver, assignment, notices) | sensitivity-scanner (if confidentiality/privilege concerns), strategic-alignment-checker (if part of broader transaction), devil's-advocate (if novel or aggressive provisions), tone-calibrator (if client-facing or negotiation document) |
| **Legal Memorandum** | clarity-reviewer, completeness-auditor, devil's-advocate, actionability-validator | IRAC/CREAC structure integrity (Issue clearly framed, Rule accurately stated, Application thorough, Conclusion supported); authority currency (are cited cases still good law? has legislation been amended?); counter-argument strength (has the memo addressed the strongest opposing arguments, not just straw men?); practical recommendations (does the conclusion lead to actionable advice, not just academic analysis?); client question coverage (does the memo answer what was actually asked?) | risk-assessor (if litigation or regulatory exposure), strategic-alignment-checker (if part of ongoing matter strategy), tone-calibrator (if client-facing memo) |
| **Court Filing / Brief** | clarity-reviewer, completeness-auditor, tone-calibrator, actionability-validator | Procedural compliance (correct court, correct caption, correct filing method); local rules conformance (page margins, font size, line spacing, cover page requirements); citation format (Bluebook, ALWD, or jurisdiction-specific citation rules); page/word limits (compliance with applicable rules, including footnote counting rules); certificate of service (proper parties, proper method, proper timing); signature block and attorney identification; standing and jurisdiction assertions; prayer for relief specificity | sensitivity-scanner (if sealed or confidential material), risk-assessor (if sanctions risk or Rule 11 concerns), devil's-advocate (always -- opposing counsel will challenge every argument), strategic-alignment-checker (if part of broader litigation strategy) |
| **Regulatory Submission** | completeness-auditor, clarity-reviewer, risk-assessor, sensitivity-scanner | Regulatory format requirements (correct form, correct agency, correct submission portal); completeness per applicable regulations (all required fields, attachments, and certifications); supporting documentation (exhibits, declarations, financial statements as required); deadline compliance (filing deadlines, comment periods, response windows); regulatory tone and cooperation posture; accuracy of factual representations; consistency with prior submissions to same regulator | tone-calibrator (if public comment or hearing testimony), strategic-alignment-checker (if part of ongoing regulatory relationship), devil's-advocate (if novel regulatory interpretation) |
| **Corporate Resolution** | completeness-auditor, clarity-reviewer, strategic-alignment-checker, actionability-validator | Authority verification (does the resolving body have authority for this action under charter, bylaws, operating agreement, or statute?); quorum requirements (was quorum present or will it be for written consent?); proper authorization chain (board authorizes what requires board action, shareholders what requires shareholder action, officers what requires officer action); voting thresholds (simple majority, supermajority, unanimous consent as required); conflict of interest procedures (recusal, independent committee, fairness opinion); corporate formalities (proper notice, proper meeting conduct, proper minutes) | sensitivity-scanner (if fiduciary duty concerns or related-party transaction), risk-assessor (if ultra vires risk or D&O exposure), devil's-advocate (if contested action or potential challenge) |
| **Opinion Letter** | clarity-reviewer, completeness-auditor, risk-assessor, sensitivity-scanner | Customary qualifications and assumptions; knowledge qualifiers ("to our knowledge" scope); reliance letters and third-party addressees; factual certificate review; opinion scope limitations; exception carve-outs; enforceability qualifications (bankruptcy, equitable principles, public policy); golden parachute and fraudulent transfer opinions where applicable | strategic-alignment-checker (if part of transaction closing), devil's-advocate (if aggressive opinion positions), tone-calibrator (if reliance parties include opposing counsel or regulators) |
| **Due Diligence Report** | completeness-auditor, risk-assessor, clarity-reviewer, actionability-validator | Coverage of all material categories (corporate, contracts, litigation, IP, employment, real property, environmental, tax, regulatory); red flag identification and severity classification; document request list completeness; gap analysis (documents requested but not received); materiality thresholds applied consistently; assumptions and limitations stated; follow-up items identified and prioritized | sensitivity-scanner (if MNPI or insider information concerns), strategic-alignment-checker (if informing transaction terms), devil's-advocate (if seller's or target's representations need testing) |
| **Compliance Policy / Manual** | completeness-auditor, clarity-reviewer, actionability-validator, risk-assessor | Regulatory coverage (does the policy address all applicable regulatory requirements?); practical implementability (can employees actually follow these procedures?); training and acknowledgment requirements; escalation procedures and reporting channels; record retention requirements; monitoring and audit provisions; penalty and enforcement provisions; version control and update procedures | sensitivity-scanner (if whistleblower or retaliation concerns), tone-calibrator (if employee-facing communication), strategic-alignment-checker (if part of broader compliance program) |

4. **Check if the plan specified reviewers.** If so, use those as the baseline and layer legal-specific focus areas on top.

### Phase 2: Parallel Agent Review

Launch all selected review agents in parallel using the Task tool.

Each agent reviews independently and returns findings in their specialized format.

**Agent Instructions:**
- Each agent receives the complete work output
- Each agent applies its specialized lens
- Each agent returns findings with severity levels
- **For legal work**: Each agent also applies its legal-specific review criteria as described in its agent file
- **For legal work**: Each agent flags any finding that implicates a Legal Review Quality Gate (see below)

### Legal Review Quality Gates

Before synthesizing findings for legal work products, verify that the following quality gates have been checked. These are pass/fail gates -- a failure in any gate requires flagging as a Critical issue regardless of which agent discovered it.

| Quality Gate | Description | Applies To |
|-------------|-------------|------------|
| **Citation Verification** | Every case, statute, regulation, and rule cited must be checked for: (a) correct citation format, (b) current validity (not overruled, repealed, or superseded), (c) accurate quotation and parenthetical description, (d) relevance to the proposition cited for. Flag any citation that cannot be verified as [UNVERIFIED -- REQUIRES MANUAL CHECK]. | Memoranda, Briefs, Opinion Letters, Regulatory Submissions |
| **Defined Term Consistency** | Every capitalized term used as a defined term must have a corresponding definition. Every defined term must be used at least once. No defined term should be defined differently in different sections. Cross-check the definitions section against usage throughout the document. | Contracts, Corporate Resolutions, Compliance Policies |
| **Cross-Reference Integrity** | Every internal cross-reference (section numbers, exhibit references, schedule callouts, "as defined in Section X") must point to the correct target. Check for orphaned references (pointing to sections that do not exist) and stale references (pointing to sections that have been renumbered). | All legal documents |
| **Privilege Review** | Scan for content that may inadvertently waive attorney-client privilege or work product protection. Flag: (a) descriptions of legal advice in non-privileged documents, (b) forwarding of privileged communications to non-privileged recipients, (c) inclusion of attorney mental impressions in discoverable documents, (d) failure to mark privileged documents as such. | All legal documents, especially those shared externally |
| **Conflict Check** | Verify that the work product does not contain positions or representations that conflict with positions taken in other matters for the same client, or that create adverse interest conflicts. Flag any apparent conflict for human review. | All legal documents |
| **Ethical Obligations Check** | Verify compliance with applicable rules of professional conduct: (a) no false statements of fact or law, (b) disclosure of directly adverse mandatory authority, (c) no assistance with client fraud or crime, (d) proper identification of the client and authorized representatives, (e) candor to tribunals where applicable. | All legal documents, especially court filings and regulatory submissions |
| **Deadline / Statute of Limitations Verification** | Check for any deadline-sensitive elements: (a) filing deadlines, (b) statutes of limitations, (c) contractual notice periods, (d) regulatory response windows, (e) option exercise periods. Flag any deadline within 30 days as URGENT. Flag any deadline that appears to have passed as CRITICAL. | Court Filings, Regulatory Submissions, Contracts, Corporate Actions |
| **Signature and Execution Requirements** | Verify that the document identifies the correct signatories, includes proper authority representations, and complies with execution formalities (notarization, witnessing, corporate seal) required by the governing law and document type. | Contracts, Corporate Resolutions, Opinion Letters, Regulatory Submissions |

### Phase 3: Synthesize Findings

After all agents return, synthesize their findings.

**For general work**, use the standard output format below.
**For legal work**, use the Legal Review Output Format, which adds legal-specific sections.

#### Standard Output Format

```markdown
## Review Summary

### Overall Assessment
**Quality Score**: [1-10]
[2-3 sentence assessment of overall quality and readiness]

### Critical Issues (Must Fix)
Issues that would cause real problems if not addressed.

#### Issue 1: [Title]
- **Found by**: [Agent name]
- **Location**: [Where in the document]
- **Problem**: [What's wrong]
- **Impact**: [What happens if not fixed]
- **Fix**: [Specific recommendation]

### Important Issues (Should Fix)
Issues that meaningfully improve quality.

#### Issue 1: [Title]
- **Found by**: [Agent name]
- **Location**: [Where in the document]
- **Problem**: [What's wrong]
- **Fix**: [Specific recommendation]

### Minor Issues (Nice to Fix)
Polish and refinement opportunities.

- [Issue]: [Quick fix] _(found by [agent])_
- [Issue]: [Quick fix] _(found by [agent])_

### What's Working Well
- [Strength 1] _(noted by [agent])_
- [Strength 2] _(noted by [agent])_

### Conflicting Feedback
[If agents disagree, note the conflict and recommend resolution]

### Recommended Action
- [ ] Fix critical issues (estimated: [time])
- [ ] Fix important issues (estimated: [time])
- [ ] Fix minor issues (estimated: [time])
- [ ] Ready to finalize after fixes
```

#### Legal Review Output Format

For legal work products, use this enhanced format that includes legal-specific sections.

```markdown
## Legal Work Review Summary

### Document Profile
- **Document Type**: [Contract / Memorandum / Brief / Filing / Resolution / etc.]
- **Jurisdiction**: [Governing law or forum]
- **Matter**: [Matter name or reference if known]
- **Date of Review**: [Date]
- **Privilege Status**: [Privileged / Non-privileged / Mixed -- handle accordingly]

### Overall Assessment
**Quality Score**: [1-10]
**Legal Readiness**: [Ready for filing/execution / Needs revision / Significant rework required]
[2-3 sentence assessment of overall quality, legal soundness, and readiness]

### Quality Gate Results

| Quality Gate | Status | Notes |
|-------------|--------|-------|
| Citation Verification | PASS / FAIL / N/A | [Details] |
| Defined Term Consistency | PASS / FAIL / N/A | [Details] |
| Cross-Reference Integrity | PASS / FAIL / N/A | [Details] |
| Privilege Review | PASS / FAIL / N/A | [Details] |
| Conflict Check | PASS / FAIL / N/A | [Details] |
| Ethical Obligations | PASS / FAIL / N/A | [Details] |
| Deadline Verification | PASS / FAIL / N/A | [Details] |
| Signature/Execution Requirements | PASS / FAIL / N/A | [Details] |

### Critical Issues (Must Fix Before Filing/Execution)
Issues that create legal risk, procedural deficiency, or enforceability problems.

#### Issue 1: [Title]
- **Found by**: [Agent name]
- **Category**: [Enforceability / Procedural / Substantive / Ethical / Privilege]
- **Location**: [Section, page, or clause reference]
- **Problem**: [What's wrong and why it matters legally]
- **Legal Risk**: [What happens if not fixed -- exposure, challenge, invalidity, sanctions]
- **Fix**: [Specific recommendation with draft language where appropriate]
- **Authority**: [Relevant rule, statute, or case if applicable]
- **Urgency**: [Immediate / Before filing / Before execution / Before distribution]

### Important Issues (Should Fix)
Issues that meaningfully improve legal quality, reduce risk, or strengthen the position.

#### Issue 1: [Title]
- **Found by**: [Agent name]
- **Category**: [Drafting / Analytical / Strategic / Procedural]
- **Location**: [Section, page, or clause reference]
- **Problem**: [What's wrong]
- **Fix**: [Specific recommendation]

### Minor Issues (Nice to Fix)
Polish, formatting, citation style, and refinement opportunities.

- [Issue]: [Quick fix] _(found by [agent])_
- [Issue]: [Quick fix] _(found by [agent])_

### What's Working Well
- [Strength 1] _(noted by [agent])_
- [Strength 2] _(noted by [agent])_

### Conflicting Feedback
[If agents disagree, note the conflict and recommend resolution.
In legal work, conflicting feedback often reflects genuine tensions -- e.g.,
aggressive advocacy vs. candor to tribunal, comprehensive disclosure vs. privilege
protection. Present both positions and the legal framework for resolving the tension.]

### Confidence Assessment
| Aspect | Confidence | Basis |
|--------|-----------|-------|
| Factual accuracy | [High/Medium/Low] | [How verified] |
| Legal analysis soundness | [High/Medium/Low] | [Basis for assessment] |
| Citation currency | [High/Medium/Low] | [Verification method] |
| Jurisdictional applicability | [High/Medium/Low] | [Governing law confirmed?] |

### Recommended Action
- [ ] Fix critical issues (estimated: [time])
- [ ] Fix important issues (estimated: [time])
- [ ] Fix minor issues (estimated: [time])
- [ ] Human attorney review of [specific issues requiring professional judgment]
- [ ] Citation verification against authoritative sources for [unverified citations]
- [ ] Ready to finalize after fixes and attorney sign-off
```

### Phase 4: Apply Fixes

If the user approves:

1. **Fix critical issues first.** For legal work, prioritize quality gate failures and enforceability issues.
2. **Fix important issues.**
3. **Fix minor issues if time permits.**
4. **Present the revised version** with a summary of changes made.
5. **For legal work**: Flag any changes that require attorney review before the document can be considered final. AI review is a quality tool, not a substitute for professional legal judgment.

If issues conflict, present the tradeoff to the user and let them decide. In legal work, conflicts often involve genuine policy tensions (e.g., aggressive position vs. sanctions risk, comprehensive disclosure vs. privilege protection, plain language vs. legal precision). Frame these as the legal tradeoffs they are.

---

## Review Principles

### Severity Calibration

#### General Work

- **Critical**: Would cause real damage -- wrong tone in sensitive email, missing key stakeholder concern, factual error in analysis, flawed logic in decision
- **Important**: Meaningful quality improvement -- unclear structure, missing context, weak evidence, incomplete consideration
- **Minor**: Polish -- word choice, formatting, small redundancies

#### Legal Work -- Severity Calibration with Examples

**Critical** -- Creates legal risk, procedural deficiency, or enforceability failure. Must be fixed before the document can be used.

| Example | Why Critical |
|---------|-------------|
| Defined term "Confidential Information" used throughout but never defined | Entire confidentiality obligation is unenforceable -- core term is void for vagueness |
| Brief cites *Lochner v. New York* for economic substantive due process without noting it has been effectively overruled | Opposing counsel will attack credibility; court may impose sanctions for citing discredited authority |
| Contract cross-references "Section 8.3" but document only has 7 sections | Orphaned reference creates ambiguity about what obligation was intended; may void the provision |
| Merger agreement lacks required shareholder approval provision for a transaction exceeding statutory threshold | Transaction may be voidable; directors face breach of fiduciary duty claims |
| Regulatory filing misses statutory deadline by referencing wrong effective date | Filing may be rejected; client may lose rights or face enforcement action |
| Court brief exceeds word limit by 2,000 words | Filing will be rejected or stricken; potential sanctions |
| Opinion letter fails to include standard bankruptcy qualification | Drafter liability exposure; reliance party may have claims |
| Corporate resolution authorizes action ultra vires the company's charter | Resolution is void; officers acting on it face personal liability |

**Important** -- Meaningfully improves legal quality, reduces risk, or strengthens the position. Should be fixed before finalization.

| Example | Why Important |
|---------|-------------|
| Contract uses "best efforts" where "commercially reasonable efforts" would be more appropriate | "Best efforts" may impose a higher standard than intended; could require actions adverse to the obligor's own interests |
| Memo analyzes majority rule but doesn't address minority view adopted in the forum jurisdiction | Analysis is incomplete for the jurisdiction where it matters most; advice may be wrong |
| Indemnification clause lacks a cap or basket | Unlimited liability exposure; standard market practice includes caps |
| Force majeure clause doesn't include pandemic/epidemic | Post-COVID, this is a known gap that sophisticated counterparties will flag |
| Brief argument section doesn't address opposing party's strongest case | Court may view the omission as concession; weakens persuasive force |
| Regulatory submission uses inconsistent terminology for the same concept | Regulator may interpret inconsistency as describing different things; creates confusion |
| Corporate minutes don't reflect that conflicted director recused from vote | Failure to document conflict procedures undermines business judgment rule protection |

**Minor** -- Polish and refinement. Nice to fix but not blocking.

| Example | Why Minor |
|---------|----------|
| Inconsistent use of "herein" vs. "in this Agreement" | Style inconsistency; no legal effect but looks unprofessional |
| Bluebook citation uses "Id." where "id." (lowercase) is correct under current edition | Technical citation format; court is unlikely to care but perfectionism matters |
| Recitals use "WHEREAS" in some clauses and "Whereas" in others | Formatting inconsistency; no legal significance |
| Memo uses both "Section" and "s." to refer to statutory provisions | Style inconsistency; recommend standardizing |
| Contract has minor numbering gap (Section 4.1, 4.2, 4.4 -- missing 4.3) | Numbering error; no substantive issue if cross-references are correct |

### Independence Matters
- Each agent reviews independently
- Don't let one agent's findings influence another
- Conflicts between agents are valuable signal
- **In legal review, independent review is especially important** because different legal concerns genuinely pull in different directions (e.g., comprehensive disclosure vs. privilege protection, aggressive advocacy vs. sanctions risk)

### Review Should Be Proportional
- Quick internal note: clarity-reviewer only
- Important email: clarity + tone + completeness
- Board presentation: all standard + conditional reviewers
- Strategic decision: all reviewers including devil's-advocate
- **Contract for execution**: all standard + legal quality gates
- **Court filing**: all standard + procedural compliance + citation verification + opposing counsel simulation (devil's-advocate)
- **Regulatory submission**: all standard + regulatory format + deadline verification + sensitivity scan
- **Corporate resolution**: all standard + authority verification + conflict check + governance alignment

### The Devil's Advocate is Special
- Always include for decisions and recommendations
- Its job is to find the strongest counterargument
- Don't dismiss its findings just because you disagree
- If the devil's advocate can't find a good counterargument, that's strong validation
- **In legal work**: The devil's advocate simulates opposing counsel, the regulator, or the most hostile reader. This is not optional for adversarial legal work -- it is essential.

---

## Legal Anti-Patterns to Avoid

These are common failure modes in legal work review. Watch for them and flag when they occur.

### Drafting Anti-Patterns

| Anti-Pattern | Description | Risk |
|-------------|-------------|------|
| **Defined Term Proliferation** | Defining terms that are used only once, or defining terms that have their ordinary meaning | Clutters the document; creates ambiguity about whether undefined terms have special meaning |
| **Circular Definitions** | Term A is defined by reference to Term B, which is defined by reference to Term A | Definition provides no actual meaning; provision may be unenforceable |
| **Belt and Suspenders Overload** | Including every conceivable protective clause regardless of relevance | Makes the document harder to negotiate, slower to execute, and may invite challenges to provisions that weren't carefully tailored |
| **Copy-Paste Jurisdiction Mismatch** | Using provisions drafted for one jurisdiction in a document governed by another without adaptation | Provisions may be unenforceable, unnecessary, or missing jurisdiction-specific requirements |
| **Ambiguous Antecedents** | Pronoun references that could refer to multiple parties or concepts | Creates genuine ambiguity about obligations; may be construed against the drafter (contra proferentem) |
| **Dangling Cross-References** | References to sections, exhibits, or schedules that don't exist or have been renumbered | Creates gaps in the document; may void referenced obligations |
| **Inconsistent Defined Terms** | Same concept referred to by different defined terms in different sections, or same defined term used with subtly different meanings | Courts may interpret inconsistency as intentional distinction; creates unintended obligations or gaps |

### Analysis Anti-Patterns

| Anti-Pattern | Description | Risk |
|-------------|-------------|------|
| **Straw Man Counter-Arguments** | Addressing only weak opposing arguments while ignoring the strong ones | Analysis provides false confidence; actual opposing arguments will be stronger |
| **Jurisdiction Shopping in Authority** | Citing favorable authority from non-binding jurisdictions while ignoring unfavorable authority from the binding jurisdiction | Misleading analysis; may violate ethical obligations of candor |
| **Outdated Authority Reliance** | Relying on cases or statutes without checking for subsequent history | Analysis may be based on overruled or repealed authority; advice may be wrong |
| **Conclusory Analysis** | Stating conclusions without showing the analytical path from rule to application | Reader cannot evaluate the quality of the analysis; undermines credibility |
| **Academic Abstraction** | Providing thorough legal analysis but no practical recommendation for what the client should do | Analysis is useless to the client; fails to answer the question asked |
| **Single-Jurisdiction Blinders** | Analyzing under one jurisdiction when the matter has multi-jurisdictional implications | Missing risks from other applicable jurisdictions |

### Review Process Anti-Patterns

| Anti-Pattern | Description | Risk |
|-------------|-------------|------|
| **Running review on low-stakes work** | Applying full multi-agent review to routine, low-risk documents | Wastes time and resources; creates review fatigue |
| **Ignoring conflicting feedback** | Dismissing conflicts between agents instead of resolving them | Conflicts often signal genuine legal tensions that need resolution |
| **Treating all findings as equal severity** | Failing to triage -- spending equal time on citation format as on enforceability issues | Critical issues may not get fixed before deadline |
| **Over-revising based on minor feedback** | Making extensive changes based on stylistic preferences that don't affect legal substance | Introduces new errors; delays finalization without meaningful improvement |
| **Not running devil's advocate on adversarial work** | Skipping opposing counsel simulation on briefs, motions, or contested contracts | Missing the arguments that will actually be made against you |
| **Applying fixes without attorney review** | Making substantive legal changes based on AI review without human attorney oversight | AI may introduce errors; changes may not reflect the attorney's judgment or the client's instructions |
| **Privilege-blind review** | Sharing privileged work product with non-privileged review channels or failing to mark privileged output | May waive attorney-client privilege or work product protection |

---

## Next Step

When the work is finalized, capture what you learned: **`/coworkpowers:workflow-compound`**
