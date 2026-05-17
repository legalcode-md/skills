---
name: legalcode-workflow-research
description: >
  Research and plan legal and knowledge work tasks thoroughly before execution. Use when
  starting any significant legal matter — contract review, regulatory compliance analysis,
  litigation preparation, corporate governance review, IP/patent analysis, M&A due diligence,
  employment law matters, data privacy assessments (GDPR/CCPA/LGPD), or any high-stakes
  knowledge work requiring structured research. Triggers on requests like 'help me prepare for',
  'I need to draft', 'plan out', 'research this legal question', 'analyze this contract',
  'assess regulatory risk', or any compound legal or knowledge work. Jurisdiction-agnostic
  with localization markers for any governing law. Produces confidence-scored, auditable
  research plans with Glass Box reasoning trail.
---

# Legalcode Research: Legal & Knowledge Work Research Workflow

> **Disclaimer**: This skill provides a framework for AI-assisted legal research and work
> planning. It does not constitute legal advice. All outputs should be reviewed by a qualified
> legal professional licensed in the relevant jurisdiction before use. Laws change; verify
> current applicability before relying on any provision described here. Statutory and case law
> references cited from memory carry hallucination risk — verify against authoritative sources
> before relying on them. Research plans are analytical frameworks, not legal opinions — they
> require professional judgment for application to specific matters.

You are orchestrating the **Research phase** of the Compound Knowledge Work loop. Your job is to thoroughly research a task and transform it into an actionable plan that makes execution straightforward.

**80% of compound knowledge work is in research and review.** Do not rush this phase.

**In legal work, incomplete research creates liability.** Every gap in research is a potential exposure. Every unchecked assumption is a risk to the client, the firm, and the matter outcome.

## Legal Research Categories

This workflow supports structured research across the following legal domains. Identify which categories apply to the current matter and weight research accordingly:

| Category | Description | Key Sources | Typical Stakes |
|----------|-------------|-------------|----------------|
| **Contract Review** | Drafting, reviewing, negotiating agreements | Templates, playbooks, precedent agreements, market standards | Medium-High |
| **Regulatory Compliance** | Ensuring adherence to applicable regulations | Regulatory texts, agency guidance, enforcement actions, compliance frameworks | High |
| **Litigation Preparation** | Preparing for dispute resolution or trial | Case law, procedural rules, discovery obligations, expert requirements | Very High |
| **Corporate Governance** | Board matters, entity formation, fiduciary duties | Corporate statutes, bylaws, board resolutions, fiduciary duty case law | High |
| **IP/Patent Analysis** | Intellectual property strategy and protection | Patent databases, trademark registries, trade secret law, licensing frameworks | High |
| **M&A Due Diligence** | Transaction investigation and risk assessment | Financial records, material contracts, regulatory filings, litigation history | Very High |
| **Employment Law** | Workforce matters, policies, disputes | Employment statutes, agency regulations, handbook policies, arbitration clauses | Medium-High |
| **Data Privacy (GDPR/CCPA/LGPD)** | Privacy compliance and data protection | Privacy regulations, DPA guidance, enforcement decisions, transfer mechanisms | High |

## Jurisdiction Awareness

Legal research is jurisdiction-dependent. Every research task must establish jurisdictional scope early and maintain awareness throughout.

### Jurisdiction Classification

| System | Characteristics | Research Approach |
|--------|----------------|-------------------|
| **Common Law** (US, UK, Australia, Canada, India) | Precedent-driven, case law binding, stare decisis | Case law research primary; statutory interpretation guided by judicial decisions |
| **Civil Law** (EU continental, Latin America, East Asia) | Code-driven, legislative text primary, doctrine secondary | Statutory text primary; scholarly commentary (doctrine) guides interpretation |
| **Mixed Systems** (South Africa, Scotland, Louisiana, Quebec, Philippines) | Blend of common and civil law traditions | Dual-track research: both statutory and case law analysis required |
| **Religious/Customary Law** (parts of Middle East, Africa, South Asia) | Sharia, customary, or traditional law components | Specialized knowledge required; identify applicable personal law regimes |

### Multi-Jurisdiction Considerations

When a matter spans jurisdictions:
1. **Identify governing law** for each obligation or claim
2. **Map conflict-of-law rules** that determine which jurisdiction's law applies
3. **Note choice-of-law and choice-of-forum clauses** in any governing agreements
4. **Assess enforcement** — where would a judgment need to be enforced?
5. **Flag treaty obligations** — bilateral investment treaties, Hague conventions, EU regulations
6. **Check for mandatory local law** that overrides choice-of-law clauses (e.g., consumer protection, employment, data privacy)

### US Federal/State Interplay

For US matters, always clarify:
- **Federal vs. state law**: Which governs the specific issue?
- **State-specific variations**: Which state(s)? Law varies significantly (e.g., Delaware corporate law vs. California, New York contract law vs. Texas)
- **Preemption**: Does federal law preempt state law on this issue?
- **Erie doctrine**: In federal court, which state's law applies?
- **Uniform laws**: Is a uniform act adopted (UCC, UETA, UFTA/UVTA) and what are local variations?

### EU/UK Considerations

- **EU Regulations** apply directly; **EU Directives** require national transposition (check local implementation)
- **Post-Brexit divergence**: UK law is diverging from EU law — check current UK position separately
- **CJEU and national court hierarchy**: EU court decisions bind national courts on EU law questions
- **Brussels/Lugano regime**: Jurisdiction and enforcement rules for cross-border disputes

## Process

### Phase 0: Discover Available Tools

Before starting research, check what MCP tools and CLIs are available in the environment. For legal research, particularly look for:

**Legal-specific tools:**
- Case law databases (Westlaw, LexisNexis, Casetext, CourtListener)
- Statutory/regulatory databases (government portals, legislative tracking)
- Patent/trademark search tools (USPTO, EPO, WIPO)
- Corporate registry tools (SEC EDGAR, Companies House, state SOS databases)
- Regulatory filing databases (FDA, FCC, EPA, state AG offices)
- Treaty databases (UN Treaty Collection, EUR-Lex)
- Legal analytics tools (Lex Machina, Docket Alarm, PACER)

**General knowledge work tools:**
- Email, calendar, meeting notes, CRM, company intel
- Project trackers, document management systems
- Web search for market/industry context

Note which are available and pass this to all agents so they can use them proactively.

### Phase 1: Understand the Task

1. **Read the task description carefully.** If the user provided a document, file, or URL, read it thoroughly.

2. **Classify the work type:**
   - Communication (email, memo, announcement, presentation)
   - Decision (strategic choice, vendor selection, resource allocation)
   - Analysis (market research, financial analysis, competitive review)
   - Meeting (preparation, facilitation, follow-up)
   - Coaching (leadership challenge, personal effectiveness)
   - Operations (process design, project planning, documentation)
   - **Contract Review** (drafting, reviewing, negotiating agreements)
   - **Regulatory Compliance** (assessing regulatory obligations, designing compliance programs)
   - **Litigation Preparation** (case assessment, discovery planning, motion practice, trial prep)
   - **Corporate Governance** (board matters, entity management, fiduciary analysis)
   - **IP/Patent Analysis** (patent landscape, freedom-to-operate, trademark clearance, trade secrets)
   - **M&A Due Diligence** (target assessment, risk identification, deal structuring)
   - **Employment Law** (policy review, dispute assessment, workforce restructuring)
   - **Data Privacy** (GDPR/CCPA/LGPD compliance, DPIA, data transfer mechanisms)
   - **General Legal Research** (legal question research, memorandum preparation, opinion drafting)

3. **Determine stakes and complexity:**
   - **Low stakes**: Internal notes, routine updates, low-value contract amendments -> lighter planning
   - **Medium stakes**: Team communications, standard decisions, routine contract reviews, standard compliance checks -> moderate planning
   - **High stakes**: Board communications, strategic decisions, sensitive topics, high-value transactions, regulatory enforcement actions, litigation with material exposure, cross-border matters -> full planning
   - **Critical/Privilege-sensitive**: Matters involving attorney-client privilege, work product doctrine, pending litigation, regulatory investigations -> full planning with privilege safeguards

4. **Establish jurisdictional scope** (for legal work types):
   - What jurisdiction(s) govern the matter?
   - Is this common law, civil law, or mixed system?
   - Are there multi-jurisdictional elements?
   - What is the forum (court, arbitration, regulatory body)?
   - Are there mandatory law provisions that override party choice?

### Phase 1.5: Ask Clarifying Questions

Before launching research, identify gaps and ask the user clarifying questions. This prevents wasted research on the wrong problem.

**When to ask questions:**
- Task description is vague or has multiple interpretations
- Success criteria are unclear
- Stakeholders or constraints are not specified
- High-stakes work where misunderstanding would be costly
- User's stated request might differ from their actual need
- **Jurisdiction is not specified** for legal matters
- **Governing law is ambiguous** or multiple laws could apply
- **Privilege implications** are unclear
- **Regulatory landscape** is uncertain or evolving

**Question patterns (from superpowers):**
- **Ask one at a time**, wait for answer before next question
- **Include your hypothesis**: "What does success look like? My hypothesis: [X]"
- **Focus on research-direction questions**: What would change your approach?
- **Catch red flags early**: Political sensitivity, irreversibility, high stakes

**Hard Gate for high-stakes work** - You MUST get answers to:
1. Who is the audience/stakeholder?
2. What does success look like?
3. What constraints exist (political, budget, timing)?
4. What have you tried before that did not work?

**Hard Gate for legal work** - You MUST additionally get answers to:
5. **What jurisdiction(s) apply?** (Governing law, forum, enforcement jurisdiction)
6. **What is the governing law?** (Contractual choice-of-law, statutory regime, regulatory body)
7. **Are there applicable regulations?** (Industry-specific, cross-border, sector regulations)
8. **Are there privilege concerns?** (Attorney-client privilege, work product, litigation hold)
9. **Have conflict checks been completed?** (Parties, related entities, adverse interests)
10. **What is the matter timeline?** (Statutes of limitation, filing deadlines, contractual deadlines, court dates)

**Example questions for legal matters:**
- "What jurisdiction governs this agreement? My hypothesis: [State/Country] based on the choice-of-law clause, but enforcement may be needed in [other jurisdiction]"
- "Is this matter subject to any pending or anticipated litigation? This affects privilege analysis"
- "What regulatory bodies have oversight here? This determines which compliance frameworks apply"
- "Have conflicts been cleared for all parties? I need to know before mapping stakeholders"
- "What is the statute of limitations exposure? This determines research urgency"
- "Is there existing outside counsel involved? This affects how we coordinate research"
- "Are there any regulatory filing deadlines approaching? This determines timeline priority"

**Example questions for general knowledge work:**
- "What does success look like for this communication? My hypothesis: Board approval vs. team buy-in require different approaches"
- "Who is the decision-maker here? This affects stakeholder mapping"
- "What's the timeline? This determines research depth"
- "Are there political sensitivities I should know about?"
- "What have you already tried? What didn't work?"

**When to skip this phase:**
- Low-stakes routine work (internal notes, simple updates)
- User provided comprehensive brief with explicit success criteria
- Task is crystal clear and unambiguous
- **Never skip for legal work classified as High or Critical stakes**

### Phase 2: Search Past Learnings

Before any new research, check what we already know. This is where compounding pays off.

**In Claude Code** (file-based retrieval):
1. **Check the learnings index** at `.context/learnings/INDEX.md` - scan for matching category, type, and tags.
2. **Search by category**: Grep `.context/learnings/[category]/` for the relevant work type (e.g., `communication/`, `decision/`, `meeting/`, `legal/`, `contracts/`, `compliance/`, `litigation/`).
3. **Search by type**: Look specifically for `pattern` and `template` insights that match the current task.
4. **Search by keywords**: Grep across all learnings for topic-specific terms (stakeholder names, project names, framework names, jurisdiction names, statute numbers, case citations).
5. **Search for preferences**: Grep for `type: preference` insights in the relevant category - these capture style, tone, and detail preferences from previous work.
6. **Search for legal precedents**: Look for previous legal research on the same jurisdiction, statute, regulation, or legal issue.
7. **Search for jurisdiction-specific patterns**: Check if we have established approaches for the relevant jurisdiction(s).

If past learnings exist, incorporate them into the plan:
- **Reuse patterns** (type: `pattern`) that worked before
- **Avoid failures** (type: `failure`) that were documented
- **Apply templates** (type: `template`) if a relevant one exists
- **Honor preferences** (type: `preference`) from previous work in this category
- **Apply legal precedent** (type: `legal-precedent`) from previous research in the same jurisdiction or legal area

Surface what you found: "Based on previous [category] work, we learned [X] and have a template for [Y]."

### Phase 3: Parallel Research

Launch research agents in parallel based on the work type. Use the Task tool with appropriate subagents. **Pass the stakes level and jurisdictional scope to each agent** so they can calibrate depth.

**Scale agents to stakes:**

| Stakes | Agents to Run |
|--------|---------------|
| **Low** | context-gatherer only (brief scan, no web search) |
| **Medium** | context-gatherer + 1-2 agents from the work type table below |
| **High** | Full agent roster from the work type table below |
| **Critical/Privilege-sensitive** | Full agent roster + external legal research + privilege review |

**Agent roster by work type** (for medium/high stakes):

| Work Type | Additional Agents |
|-----------|-------------------|
| Communication | stakeholder-mapper, precedent-researcher |
| Decision | stakeholder-mapper, constraint-analyzer, precedent-researcher |
| Analysis | constraint-analyzer, precedent-researcher |
| Meeting | stakeholder-mapper, precedent-researcher |
| Coaching | stakeholder-mapper |
| Operations | constraint-analyzer, precedent-researcher |
| **Contract Review** | stakeholder-mapper, constraint-analyzer, precedent-researcher |
| **Regulatory Compliance** | constraint-analyzer, precedent-researcher, stakeholder-mapper |
| **Litigation Preparation** | stakeholder-mapper, constraint-analyzer, precedent-researcher |
| **Corporate Governance** | stakeholder-mapper, constraint-analyzer, precedent-researcher |
| **IP/Patent Analysis** | constraint-analyzer, precedent-researcher |
| **M&A Due Diligence** | stakeholder-mapper, constraint-analyzer, precedent-researcher |
| **Employment Law** | stakeholder-mapper, constraint-analyzer, precedent-researcher |
| **Data Privacy** | constraint-analyzer, precedent-researcher, stakeholder-mapper |
| **General Legal Research** | precedent-researcher, constraint-analyzer |

**For high-stakes work, always add:**
- External research via web search for best practices, frameworks, and examples
- **For legal work**: Case law database searches, regulatory guidance reviews, bar association materials, law review articles, practitioner treatises

### Phase 4: Research Decision

After parallel research returns, assess whether you need additional external research.

**Always research externally when:**
- The topic involves legal, compliance, or regulatory considerations
- The decision is irreversible or very high stakes
- The domain is unfamiliar
- Best practices or industry standards exist that should be consulted

**For legal matters, always verify:**
- **Currency of law**: Has the statute/regulation been amended recently? Has the case been overruled or distinguished?
- **Jurisdiction applicability**: Does this authority actually apply in the relevant jurisdiction? Is it binding or merely persuasive?
- **Regulatory updates**: Have enforcement priorities or agency guidance changed?
- **Legislative pipeline**: Is there pending legislation that could change the analysis?

### Legal Research Sources (by priority)

| Priority | Source Type | Examples | Use Case |
|----------|------------|----------|----------|
| **1 - Primary Authority** | Statutes, regulations, constitutions | USC, CFR, state codes, EU regulations | Binding law in the jurisdiction |
| **2 - Binding Case Law** | Court decisions from the controlling jurisdiction | Supreme Court, Circuit Court (US), CJEU (EU), Supreme Court (UK) | Precedent that must be followed |
| **3 - Persuasive Authority** | Decisions from other jurisdictions, lower courts | Sister-state decisions, district court opinions, Restatements | Influential but not binding |
| **4 - Regulatory Guidance** | Agency interpretations, no-action letters, advisory opinions | SEC guidance, FTC enforcement statements, ICO guidance | How regulators interpret the law |
| **5 - Secondary Sources** | Treatises, law review articles, practice guides | Williston on Contracts, Corbin, ABA publications | Academic and practitioner analysis |
| **6 - Bar/Professional** | Bar association materials, ethics opinions, CLE materials | ABA Model Rules, state bar opinions, ILPA guidelines | Professional standards and best practices |
| **7 - Industry Standards** | Market terms, industry playbooks, trade association guidance | ISDA, LSTA, NVCA, market standard positions | What is customary in the industry |

### Phase 5: Synthesize the Plan

Use the **plan-synthesizer** agent mindset to create the final plan.

**Plan Output Format:**

```markdown
# Plan: [Task Name]

## Task Summary
[2-3 sentences: What we're doing, why it matters, what success looks like]

## Jurisdictional Analysis
[Applicable jurisdiction(s), governing law, forum, enforcement considerations.
For multi-jurisdiction matters: conflict-of-law analysis, mandatory local law overrides,
treaty obligations. Classify as common law / civil law / mixed system.
Note any pending legislative or regulatory changes that could affect the analysis.]

## Regulatory Landscape
[Applicable regulations and regulatory bodies. Current enforcement posture and priorities.
Recent enforcement actions or guidance relevant to the matter. Compliance framework requirements.
For cross-border matters: each jurisdiction's regulatory requirements mapped separately.]

## Context Brief
[Key context gathered - what we know, what matters, what is sensitive]

## Prior Learnings Applied
[What we found from past compound phases, organized by type:
- **Patterns**: [approaches that worked before]
- **Failures**: [mistakes to avoid]
- **Templates**: [reusable structures available]
- **Preferences**: [style/tone/detail preferences for this category]
- **Legal Precedents**: [prior research on same jurisdiction/issue]
If none found, state "No prior learnings found for this work type."]

## Stakeholder Considerations
[Who is affected, their interests, anticipated reactions.
For legal matters: parties, counsel, regulators, courts/tribunals, affected third parties,
guarantors, insurers, beneficiaries. Note any adverse interests or conflicts.]

## Privilege Considerations
[Attorney-client privilege scope and preservation requirements.
Work product doctrine applicability. Common interest / joint defense arrangements.
Privilege log requirements. Communication protocols to maintain privilege.
If no privilege concerns apply, state "No privilege considerations identified."]

## Conflict Check Notes
[Status of conflict checks. Parties and related entities checked.
Any potential conflicts identified and their resolution.
If not applicable, state "Conflict check not applicable to this matter type."]

## Constraints
[Time, political, resource, or other constraints identified.
For legal matters: statutes of limitations, filing deadlines, regulatory timelines,
court schedules, contractual notice periods, discovery deadlines, cooling-off periods,
regulatory approval timelines.]

## Relevant Precedents
[What has been done before in similar situations, what worked/didn't.
For legal matters: binding case law, persuasive authority, statutory interpretation,
regulatory guidance, legislative history, treaty obligations.
Note authority hierarchy: binding vs. persuasive, majority vs. minority positions.]

## Approach
[Step-by-step plan for execution]

### Step 1: [Action]
- **What**: [Specific action]
- **Why**: [Rationale]
- **Agent**: [Which work-phase agent to use]
- **Inputs needed**: [What information is required]
- **Legal considerations**: [Jurisdiction-specific requirements, privilege implications, regulatory constraints]

### Step 2: [Action]
[Same structure]

## Review Plan
[Which review agents should evaluate the output, and why]

| Reviewer | Why Needed | Legal Focus |
|----------|------------|-------------|
| [Agent] | [What they will catch] | [Jurisdiction/regulatory/privilege check] |

## Legal Risk Matrix
[For legal matters: structured risk assessment of identified legal exposures]

| Risk | Category | Jurisdiction | Probability | Impact | Severity | Mitigation |
|------|----------|--------------|-------------|--------|----------|------------|
| [Risk description] | [Contract/Regulatory/Litigation/IP/Employment/Privacy] | [Jurisdiction] | [H/M/L] | [H/M/L] | [CRITICAL/HIGH/MEDIUM/LOW] | [Mitigation strategy] |

## Regulatory Compliance Checklist
[For matters with regulatory dimensions: specific compliance requirements mapped to actions]

- [ ] [Regulatory requirement 1] - [Applicable regulation] - [Compliance action]
- [ ] [Regulatory requirement 2] - [Applicable regulation] - [Compliance action]

## Success Criteria
- [ ] [Measurable outcome 1]
- [ ] [Measurable outcome 2]
- [ ] [Measurable outcome 3]

## Risks & Mitigations
| Risk | Likelihood | Mitigation |
|------|------------|------------|
| [Risk] | [H/M/L] | [How to address] |

## Timeline
[Suggested sequencing and any time constraints.
For legal matters: include filing deadlines, statutes of limitations, regulatory timelines,
court dates, contractual notice periods, discovery cut-offs, and any cooling-off or
waiting periods. Flag immovable deadlines in **bold**.]

## Confidence Assessment
[Rate confidence in the research completeness and plan quality]

| Dimension | Score | Notes |
|-----------|-------|-------|
| Research completeness | [1-5] | [What gaps remain] |
| Jurisdictional coverage | [1-5] | [Jurisdictions fully/partially/not covered] |
| Authority currency | [1-5] | [How current are the legal sources] |
| Stakeholder identification | [1-5] | [Completeness of stakeholder map] |
| Risk identification | [1-5] | [Completeness of risk assessment] |
```

### Phase 6: Legal Research Quality Gates

Before presenting the plan to the user, run through these quality gates. Every legal research plan must pass ALL applicable gates.

#### Gate 1: Citation Verification
- [ ] All case citations include full citation (case name, reporter, year, jurisdiction)
- [ ] No citations to overruled, vacated, or superseded decisions without noting current status
- [ ] Statutory references include section numbers, version/year, and jurisdiction
- [ ] Regulatory references specify the agency, rule number, and effective date
- [ ] Secondary sources are identified by author, title, and edition/year

#### Gate 2: Currency of Law
- [ ] Check whether cited statutes have been amended since the last known version
- [ ] Check whether cited cases remain good law (not overruled, distinguished, or limited)
- [ ] Check for pending legislation or rulemaking that could change the analysis
- [ ] Note the "as of" date for all legal research conclusions
- [ ] Flag any areas where the law is unsettled or in flux

#### Gate 3: Jurisdiction Applicability
- [ ] Confirm that each cited authority is from the correct jurisdiction
- [ ] Distinguish binding authority from persuasive authority
- [ ] Note where federal vs. state law applies (for US matters)
- [ ] Confirm that EU regulations vs. directives are correctly classified (for EU matters)
- [ ] Verify that foreign law citations are from the governing jurisdiction, not an analogous one

#### Gate 4: Cross-Reference Secondary Sources
- [ ] Verify primary authority interpretations against at least one secondary source
- [ ] Check for minority/majority positions on contested points
- [ ] Note circuit splits, conflicting state approaches, or unsettled law
- [ ] Identify trending directions in legal development (are courts moving toward a position?)

#### Gate 5: Privilege and Confidentiality
- [ ] Confirm that research output does not inadvertently waive privilege
- [ ] Verify that no confidential client information is exposed in research queries
- [ ] Check that work product protections are maintained
- [ ] Note any common interest or joint defense implications

#### Gate 6: Completeness Check
- [ ] All identified legal issues have been researched (no known gaps without explanation)
- [ ] All relevant jurisdictions have been covered
- [ ] Both favorable and unfavorable authority have been identified (no cherry-picking)
- [ ] Practical/business considerations are addressed alongside legal analysis
- [ ] Risk assessment covers all identified exposures

### Phase 7: User Approval

Present the plan to the user. Ask if they want to:
1. **Approve and proceed** to the Work phase
2. **Modify** specific sections
3. **Add context** you may have missed
4. **Adjust scope** (more or less thorough)
5. **Flag privilege concerns** about any research direction
6. **Confirm jurisdictional scope** before proceeding

## Important Principles

- **Plans are living documents.** They will be updated during execution.
- **Front-load the thinking.** Every minute spent planning saves ten in execution.
- **Be explicit about assumptions.** If you are guessing, say so.
- **Match rigor to stakes.** A routine email does not need a 20-step plan.
- **Include review in the plan.** Every plan should specify which reviewers will check the output.
- **Jurisdiction matters in every legal analysis.** Never assume the law is the same across jurisdictions.
- **Privilege is fragile.** Once waived, it cannot be restored. Err on the side of protection.
- **Currency of law is non-negotiable.** Outdated legal research is worse than no research.
- **Both sides of the argument.** Identify unfavorable authority before your adversary does.
- **Confidence scoring is mandatory for legal work.** Always rate your confidence and explain gaps.
- **Glass Box reasoning.** Show your analytical chain so the supervising attorney can verify the logic.

## Next Step

When the plan is approved, move to execution: **`/coworkpowers:workflow-work`**

## Anti-Patterns to Avoid

### General Anti-Patterns
- Planning so long that urgency passes
- Over-planning low-stakes work
- Skipping stakeholder analysis on communications
- Assuming context instead of gathering it
- Creating plans that are too abstract to execute

### Legal Anti-Patterns

| Anti-Pattern | Risk | Prevention |
|-------------|------|------------|
| **Citing overruled cases** | Incorrect legal advice; malpractice risk | Always check case status (Shepardize / KeyCite equivalent) |
| **Missing jurisdiction-specific nuances** | Advice that does not apply in the relevant jurisdiction | Confirm jurisdiction for every cited authority |
| **Ignoring regulatory changes** | Compliance gaps; enforcement exposure | Check regulatory update feeds; note "as of" dates |
| **Privilege waiver risks** | Loss of attorney-client privilege; exposure of work product | Review all outputs for privilege implications before sharing |
| **Cherry-picking favorable authority** | Incomplete analysis; client surprise when adverse authority surfaces | Affirmatively research and disclose unfavorable authority |
| **Assuming uniform law across states/countries** | Material legal errors | Research each jurisdiction independently; note variations |
| **Conflating binding and persuasive authority** | Overstatement of legal position; credibility loss | Always classify authority hierarchy |
| **Ignoring legislative pipeline** | Advice overtaken by new legislation | Check pending bills, proposed rules, and regulatory agendas |
| **Treating secondary sources as law** | Overstating legal certainty | Distinguish treatises/articles from primary authority |
| **Missing statutes of limitations** | Waived claims; malpractice exposure | Always check limitation periods early in research |
| **Ignoring choice-of-law issues** | Wrong law applied to the analysis | Identify governing law before substantive research |
| **Failing to consider both parties' positions** | Incomplete negotiation preparation; surprise arguments | Research opposing position as thoroughly as your own |
| **Not noting unsettled law** | False confidence in legal position | Flag circuit splits, evolving doctrine, pending cases |
| **Skipping conflict checks** | Ethical violations; disqualification risk | Verify conflict clearance before substantive engagement |
| **Over-relying on AI-generated citations** | Hallucinated cases; sanctions risk | Verify every citation against primary sources |

## Legal Research Methodology Notes

### Hierarchy of Authority (Common Law Jurisdictions)

```
Constitutional provisions (supreme)
    |
Statutes / Codes (legislative enactments)
    |
Administrative regulations (agency rulemaking)
    |
Case law - same jurisdiction, highest court (binding)
    |
Case law - same jurisdiction, lower courts (binding in that court)
    |
Case law - other jurisdictions (persuasive only)
    |
Agency guidance / advisory opinions (persuasive, shows enforcement posture)
    |
Restatements, treatises, law review articles (persuasive secondary sources)
    |
Practice guides, bar materials, CLE materials (professional guidance)
```

### Hierarchy of Authority (Civil Law Jurisdictions)

```
Constitution / Basic Law (supreme)
    |
Codes (Civil Code, Commercial Code, etc.)
    |
Statutes / Legislative Acts
    |
Administrative regulations / Decrees
    |
Doctrine (scholarly commentary - more weight than in common law)
    |
Jurisprudence (court decisions - less weight than in common law, but increasingly cited)
    |
Custom and practice
```

### EU Legal Order

```
EU Treaties (TEU, TFEU) (primary law)
    |
Charter of Fundamental Rights
    |
EU Regulations (directly applicable in all Member States)
    |
EU Directives (require national transposition)
    |
CJEU decisions (binding interpretation of EU law)
    |
National implementing legislation
    |
National court decisions interpreting EU-derived law
```
