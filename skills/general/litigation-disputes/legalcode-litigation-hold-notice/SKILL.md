---
name: legalcode-litigation-hold-notice
description: Draft, review, and implement litigation hold notices and preservation workflows for anticipated
  or pending disputes. Use when users ask for legal hold implementation, document preservation memos,
  custodian scope planning, suspension of deletion policies, ESI retention instructions, or defensible
  hold release procedures. Supports cross- jurisdictional commercial matters with confidence-scored analysis
  and auditable output. Includes custodian tracking, reminder workflows, and defensible release procedures.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Litigation Hold Notice

> **Disclaimer**: This skill provides a framework for AI-assisted litigation hold drafting
> and implementation. It does not constitute legal advice. All outputs should be reviewed
> by a qualified legal professional licensed in the relevant jurisdiction before use.
> Litigation holds involve significant legal consequences including potential sanctions for
> spoliation. Laws and procedural rules change; verify current applicability before relying
> on any provision described here. Statutory and case law references cited from memory
> carry hallucination risk — verify against authoritative sources.

## Purpose and Scope

This skill creates, reviews, and manages litigation hold notices and preservation workflows
when a dispute is reasonably anticipated or already filed. It produces defensible hold
documentation, custodian tracking systems, and release procedures.

**Covers:**

- Initial hold trigger analysis and preservation duty assessment
- Litigation hold notice drafting for employees and third parties
- Custodian identification and scoping methodology
- ESI and hard-copy preservation controls
- Reminder and compliance tracking workflows
- Defensible hold release procedures
- Gap analysis with severity classification (GREEN/YELLOW/RED for preservation risks)
- Quality-verified output with Glass Box audit trail

**Does not:**

- Replace qualified counsel's judgment on preservation scope
- Constitute legal advice regarding spoliation risk
- Address criminal investigation holds (different standards apply)
- Cover government agency preservation obligations (specialized rules)
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic framework. The applicable procedural rules and substantive
law determine the specific preservation duty. The skill identifies the forum and governing
law early and adapts the analysis accordingly.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- Trigger standard for preservation duty ("reasonable anticipation" thresholds)
- Spoliation sanctions standards and burden-shifting rules
- Privilege and work-product protections for hold communications
- Data protection conflicts (employee privacy, cross-border transfers, retention limits)
- Proportionality standards for preservation scope
- E-discovery rules and ESI protocols
- Local court rules on preservation orders and sanctions motions

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The preservation scope could materially change based on additional information
- Multiple valid approaches exist for custodian or data source identification
- Risk tolerance affects whether to preserve broadly or narrowly
- Business operations impact of preservation requires balancing

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

### Step 1: Assess the Litigation Hold Trigger

Determine whether a preservation duty has been triggered.

**CLARIFY** — Gather the following information:

1. **What is the dispute status?**
   - Options: Litigation filed (complaint served), Litigation threatened (demand letter
     received), Regulatory investigation (subpoena/CID received), Internal investigation
     (potential future litigation), Dispute reasonably anticipated (no formal action yet),
     Precautionary hold (out of abundance of caution)
   - _Why this matters_: The trigger status affects urgency, scope, and defensibility
     requirements.

2. **What is the nature of the dispute?**
   - Options: Contract dispute, Employment matter, IP/trade secret, Product liability,
     Regulatory/compliance, Securities, Antitrust, Personal injury, Other (describe)
   - _Why this matters_: Dispute type determines relevant custodians, data sources, and
     date ranges.

3. **What is the forum (or likely forum)?**
   - Options: US Federal Court (specify district), US State Court (specify state), UK
     courts, EU member state courts (specify), International arbitration (specify
     institution), Multiple forums, Unknown
   - _Why this matters_: Procedural rules and sanctions standards vary significantly
     by forum.

4. **What is the relevant time period?**
   - Provide: Start date, end date (or ongoing), key events timeline
   - _Why this matters_: Time period defines the document preservation scope.

5. **Who are the adverse parties?**
   - Provide: Names of counterparties, their counsel if known
   - _Why this matters_: May affect scope (documents exchanged with counterparty) and
     timing (whether counterparty has made specific preservation demands).

### Step 2: Assess Preservation Duty Trigger

Based on the information gathered, assess whether a preservation duty exists.

**Preservation duty assessment framework:**

| Factor                      | Analysis                                                                                                                                            |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Litigation filed**        | Duty clearly triggered when complaint served. Duty may attach earlier if reasonably anticipated.                                                    |
| **Demand letter received**  | Strong indicator. Assess whether letter makes litigation reasonably foreseeable.                                                                    |
| **Regulatory inquiry**      | Government investigation typically triggers duty. Scope depends on subject matter.                                                                  |
| **Internal investigation**  | If investigation could lead to litigation or regulatory action, duty may attach.                                                                    |
| **Reasonable anticipation** | Objective standard: would a reasonable party in this position anticipate litigation? Consider past disputes, industry patterns, severity of claims. |

**CLARIFY** — If the trigger is uncertain:

- "Based on the information provided, it is [likely/uncertain/unlikely] that a preservation
  duty has been triggered. Here is the analysis: [reasoning]. Do you want to proceed with
  a precautionary hold, or discuss the trigger question further with counsel?"

[JURISDICTION-SPECIFIC] Trigger standards:

- **US Federal**: "Reasonable anticipation of litigation" standard. Zubulake line of cases
  establishes framework. Duty attaches when litigation is reasonably foreseeable [VERIFY]
- **UK**: Pre-action protocols may affect timing. Duty arises when litigation reasonably
  contemplated. CPR 31.11 and Practice Direction 31B govern [VERIFY]
- **EU**: Varies by member state. GDPR retention limits may conflict with preservation
  obligations. Consider proportionality [VERIFY]

### Step 3: Define Preservation Scope

**CLARIFY** — Gather scope parameters:

1. **Key custodians** — Who are the individuals most likely to have relevant information?
   - Options: Executives involved in the matter, Deal team/project team, Legal department,
     Finance/accounting, HR (for employment matters), IT administrators, Customer-facing
     personnel, Other (specify)
   - _Why this matters_: Custodian list defines whose data must be preserved.

2. **Key data sources** — What systems and repositories contain relevant information?
   - Options: Email (specify system), Documents (SharePoint, G Drive, network drives),
     Messaging (Slack, Teams, WhatsApp), CRM/ERP systems, Financial systems, HR systems,
     Mobile devices, Paper files, Backup tapes, Third-party systems (specify)
   - Allow multiple selections.
   - _Why this matters_: Data sources determine technical preservation requirements.

3. **Subject matter** — What topics and keywords define relevance?
   - Provide: Key topics, project names, counterparty names, relevant products/services,
     search terms
   - _Why this matters_: Subject matter scoping prevents over-preservation and guides
     custodian instructions.

4. **Preservation approach** — How broad should the hold be?
   - Options: Broad (all potentially relevant data from all potential custodians),
     Targeted (key custodians and systems based on matter assessment), Phased
     (immediate hold on critical sources, expand as needed)
   - _Why this matters_: Broad preservation is more defensible but more expensive.
     Targeted requires good scoping documentation.

**Proportionality considerations:**

- Value of the dispute vs. cost of preservation
- Accessibility of data sources
- Business impact of freezing deletion/modification
- Likelihood that particular sources contain unique relevant information

### Step 4: Draft the Litigation Hold Notice

Draft the notice using the required components below.

**Required Components of a Defensible Hold Notice:**

#### 4.1 Header and Matter Identification

- Clear identification as a LEGAL HOLD / LITIGATION HOLD
- Matter name and reference number
- Issue date
- Sender (typically General Counsel or outside counsel)
- Confidentiality/privilege legend

#### 4.2 Legal Obligation Statement

- Explanation of legal duty to preserve
- Consequences of non-compliance (sanctions, adverse inference)
- Immediate effectiveness (do not wait)

#### 4.3 Matter Description

- Brief, non-waiving description of the dispute
- Sufficient to identify relevance without disclosing strategy
- Relevant time period
- Adverse party identification (if appropriate)

#### 4.4 Scope of Preservation

- Types of information to preserve (documents, ESI, hard copy, communications)
- Subject matter parameters
- Time period
- Relevant custodians/departments

#### 4.5 Specific Preservation Instructions

- **Do** instructions:
  - Preserve all potentially relevant documents and ESI
  - Suspend auto-delete and routine destruction
  - Preserve metadata
  - Report relevant information discovered
- **Do NOT** instructions:
  - Do not delete, modify, or destroy potentially relevant materials
  - Do not create new versions to "clean up" documents
  - Do not discuss the hold with unauthorized persons
  - Do not self-select what is "relevant" — preserve broadly

#### 4.6 Data Source-Specific Instructions

- Email: suspend deletion, auto-archive
- Documents: disable version control cleanup
- Messaging: preserve chat history
- Mobile devices: do not wipe, reset, or upgrade
- Paper: do not shred or discard
- Backup systems: suspend tape rotation

#### 4.7 Escalation and Questions

- Contact for questions
- Reporting path for discovered relevant materials
- Privilege handling instructions

#### 4.8 Acknowledgment Requirement

- Deadline for acknowledgment
- Statement to acknowledge
- Return instructions

**CLARIFY** — Customize the notice based on:

- "Will this notice go to employees only, or also to third parties (contractors, vendors)?"
- "Does your organization have a standard hold notice template that should be used as the
  basis?"
- "Are there any specific systems or processes that need special instructions?"

### Step 5: Establish Custodian Tracking

Create a tracking system for hold compliance:

**Custodian Register Template:**

| Field                 | Description                               |
| --------------------- | ----------------------------------------- |
| Custodian Name        | Full name                                 |
| Department/Role       | Organizational position                   |
| Notice Date           | When hold notice sent                     |
| Acknowledgment Status | Received / Pending / Escalated            |
| Acknowledgment Date   | When acknowledgment received              |
| Data Sources          | Relevant systems for this custodian       |
| Special Instructions  | Any custodian-specific preservation needs |
| Follow-up Dates       | Reminder schedule                         |
| Notes                 | Compliance issues, questions raised       |

**CLARIFY** — Ask about tracking requirements:

- "What is your organization's standard for acknowledgment follow-up (e.g., 3 days, 5
  days)?"
- "Who will be responsible for tracking acknowledgments and sending reminders?"
- "Should the tracking system integrate with your matter management system?"

### Step 6: Establish Reminder and Compliance Cadence

Define ongoing compliance monitoring:

**Reminder Schedule:**

- Initial notice: Day 0
- First reminder (non-responders): Day 3-5
- Escalation to supervisor: Day 7-10
- Periodic re-certification: Every 60-90 days (or more frequently for active litigation)
- Update notices: When scope changes or new custodians identified

**Compliance Monitoring:**

- Track acknowledgment rates
- Document follow-up efforts
- Escalate chronic non-compliance
- Audit data source preservation (spot-check that auto-delete is suspended)

### Step 7: Plan for Hold Release

Document the criteria and process for eventual hold release:

**Release Criteria:**

- Litigation resolved (judgment, settlement, dismissal)
- Statute of limitations expired
- Regulatory investigation closed
- Matter abandoned (document reasoning)
- Superseded by new hold with different scope

**Release Process:**

1. Legal sign-off confirming release criteria met
2. Written release notice to all custodians
3. Documentation of release decision and reasoning
4. Restart of normal retention schedules
5. Update of matter management records

**Release Notice Components:**

- Identification of original hold being released
- Confirmation that preservation obligation for this matter has ended
- Instruction to resume normal retention policies
- Contact for questions
- Acknowledgment requirement (recommended)

### Step 8: Quality Verification

Before delivering the hold package:

1. Run the **Preservation Risk Assessment** (see below) to identify gaps
2. For any RED-classified gaps, run the 3-pass Self-Interrogation
3. Assign Confidence Scores to scope and trigger assessments
4. Verify all required notice components are present
5. Generate the Glass Box Audit Trail

---

## Preservation Risk Assessment

Assess the litigation hold package against these risk categories:

| #   | Risk Category            | Key Assessment Points                                                |
| --- | ------------------------ | -------------------------------------------------------------------- |
| 1   | Trigger Documentation    | Is the trigger clearly documented? Is timing defensible?             |
| 2   | Custodian Scope          | Are all likely custodians identified? Is the methodology documented? |
| 3   | Data Source Coverage     | Are all relevant systems covered? Are any known gaps documented?     |
| 4   | Notice Clarity           | Are preservation instructions clear and actionable?                  |
| 5   | Acknowledgment Tracking  | Is there a system to track compliance?                               |
| 6   | Auto-Delete Suspension   | Have routine deletion processes been suspended?                      |
| 7   | Third-Party Preservation | Have third parties with relevant data been notified?                 |
| 8   | Cross-Border Issues      | Are there data protection or privacy conflicts?                      |
| 9   | Mobile/BYOD Coverage     | Are personal devices addressed?                                      |
| 10  | Release Criteria         | Are release criteria and process documented?                         |

### Severity Classification for Preservation Risks

#### GREEN — Adequate

The preservation element is present, documented, and defensible. Minor improvements
possible but no material gap.

**Examples:**

- Custodian list is comprehensive and methodology is documented
- All major data sources identified with preservation instructions
- Acknowledgment tracking system in place
- Reminder schedule defined

**Action**: Note for awareness. No remediation needed.

#### YELLOW — Gap Requiring Attention

A gap exists that could create challenges if challenged but is not an immediate
spoliation risk. Should be addressed promptly.

**Examples:**

- Some custodians have not acknowledged after first reminder
- One data source preservation is pending IT implementation
- Third-party preservation notice drafted but not yet sent
- Mobile device policy unclear but devices not yet wiped
- Release criteria not yet documented

**Action**: Document the gap. Assign owner and deadline for remediation. Monitor.

#### RED — Critical Risk

A gap that creates immediate spoliation risk or would be difficult to defend in a
sanctions motion.

**Examples:**

- Preservation duty triggered but no hold issued
- Key custodians not notified
- Auto-delete processes still running on relevant systems
- Known relevant data destroyed after duty triggered
- No documentation of hold scope or trigger analysis
- Employee reported deleting documents after hold issued

**Action**: Escalate immediately. Implement emergency preservation measures. Document
remediation. Consider disclosure obligations. Consult outside counsel.

---

## Spoliation Risk Factors

Assess these factors to calibrate preservation rigor:

| Factor                   | Higher Risk                                     | Lower Risk                    |
| ------------------------ | ----------------------------------------------- | ----------------------------- |
| **Adverse party**        | Sophisticated, will examine preservation        | Unlikely to challenge         |
| **Forum**                | Jurisdiction with strong sanctions (US federal) | Lenient or unclear standards  |
| **Data value**           | "Smoking gun" documents likely                  | Mostly cumulative evidence    |
| **Dispute size**         | Large damages/stakes                            | Small matter                  |
| **Counterparty demands** | Specific preservation demands made              | No specific requests          |
| **Prior conduct**        | History of preservation issues                  | Clean track record            |
| **Data accessibility**   | Easy to preserve                                | Expensive/complex to preserve |

---

## Quality Assurance Framework

### Citation Quality Gates

| Gate           | Rule                                                     | Fail Action                         |
| -------------- | -------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every legal claim cites specific procedural rule or case | Add citation or mark "[UNVERIFIED]" |
| **Format**     | All citations follow consistent format                   | Fix format                          |
| **Currency**   | Procedural rules checked for recent amendments           | Flag "[CHECK CURRENCY]"             |
| **Domain**     | Analysis stays within the applicable forum's rules       | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated                            | Add confidence qualifier            |

### Self-Interrogation for RED Items

For any preservation gap classified as RED:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the
cited authority? Would a court actually impose sanctions for this gap?

**Pass 2 — Completeness**: Have all relevant rules and standards been considered? Are
there defenses or mitigating factors?

**Pass 3 — Challenge**: What is the strongest argument that this gap is defensible?
Under what circumstances might a court decline to impose sanctions?

### Confidence Scoring

| Level        | Range     | Meaning                                          | Action                            |
| ------------ | --------- | ------------------------------------------------ | --------------------------------- |
| **Definite** | 0.95-1.0  | Clear rule, straightforward application          | State with confidence             |
| **High**     | 0.80-0.94 | Strong authority, minor interpretation questions | State with brief caveat           |
| **Probable** | 0.60-0.79 | Good arguments but reasonable minds could differ | State with explicit reasoning     |
| **Possible** | 0.40-0.59 | Genuinely uncertain, fact-dependent              | Flag for counsel review           |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative                          | Do not assert; flag "[UNCERTAIN]" |

---

## Glass Box Audit Trail

```yaml
glass_box:
  matter: "[Matter name and reference]"
  document_type: "Litigation Hold Package"
  forum: "[Court/tribunal/arbitration]"
  governing_procedural_rules: "[FRCP / CPR / etc.]"
  trigger_status: "[Litigation filed / Anticipated / Regulatory / etc.]"
  trigger_date: "[Date duty triggered or assessed]"
  custodian_count: "[Number of custodians on hold]"
  data_sources_covered: "[Number of systems/repositories]"
  risk_assessment_completed: "Yes / No"
  red_gaps_identified: "[Number]"
  yellow_gaps_identified: "[Number]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  procedural_rules_consulted:
    - "[Rule — VERIFIED or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations or caveats]"
  reviewer: "AI-assisted — requires qualified legal review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in litigation hold implementation:

1. **Waiting for the complaint to issue the hold** — The preservation duty attaches when
   litigation is reasonably anticipated, not when it is filed. Waiting for the complaint
   may mean relevant evidence has already been destroyed.

2. **Vague hold notices** — A notice that says "preserve all relevant documents" without
   defining what is relevant is unactionable. Custodians need specific subject matter,
   time periods, and system instructions.

3. **One-and-done notices** — Sending a hold notice once and never following up is
   insufficient. Regular reminders and re-certifications are necessary to demonstrate
   good faith compliance.

4. **No acknowledgment tracking** — If you cannot prove who received the notice and when,
   you cannot defend the hold in a sanctions motion. Track every acknowledgment.

5. **Ignoring auto-delete** — Sending a hold notice while auto-delete policies continue to
   run defeats the purpose. IT must suspend automated deletion on covered systems.

6. **Over-reliance on custodian self-collection** — Allowing custodians to decide what is
   relevant and collect their own documents creates gaps. Collections should be supervised
   or performed by professionals.

7. **Forgetting third parties** — If relevant documents are held by third parties (vendors,
   cloud providers, former employees), they must be notified and appropriate preservation
   steps taken.

8. **Ignoring mobile and personal devices** — If employees use personal devices for work
   (BYOD), those devices may contain relevant ESI. The hold must address them.

9. **No documentation of scope decisions** — If you cannot explain why certain custodians
   or data sources were excluded from the hold, you cannot defend a proportionality
   argument. Document the methodology.

10. **Failing to update the hold** — As litigation develops, new custodians and issues may
    emerge. The hold must be updated to reflect new information.

11. **Releasing holds informally** — Lifting a hold without documentation and formal
    release notice creates risk. If litigation resurfaces, you need to show the release
    was proper.

12. **Treating all holds the same** — A $100M commercial dispute requires different rigor
    than a small employment matter. Calibrate preservation to the risk.

13. **Ignoring cross-border data issues** — In international matters, GDPR and other data
    protection laws may conflict with preservation obligations. Address transfer mechanisms
    and retention limits proactively.

14. **Privilege waiver through hold communications** — Hold notices that disclose litigation
    strategy or legal analysis may waive privilege. Keep hold communications factual and
    mark them as privileged.

15. **Spoliation after the hold** — Issuing a hold does not prevent spoliation if employees
    ignore it. Monitor compliance and escalate violations immediately.

---

## Writing Standards

Apply plain-language discipline to all output:

**For hold notices** (distributed to employees):

- Plain language. No legal jargon.
- Active voice: "You must preserve" not "Preservation is required"
- Clear instructions: "Do X. Do not do Y."
- Accessible to non-lawyers

**For legal documentation** (trigger analysis, scope memos):

- Same plain-language standards
- May include legal analysis
- Cite procedural rules and case law
- Confidence qualifiers where appropriate

**Quality gates before delivery**:

1. Can a non-lawyer employee understand and follow the hold notice?
2. Are all instructions actionable (not vague)?
3. Is every legal assertion backed by citation (or flagged [VERIFY])?
4. Could any sentence be clearer or shorter?

---

## External Tool Integration

**With legalcode-mcp connected:**

- Search for jurisdiction-relevant spoliation standards, sanctions cases, and e-discovery
  rules
- Verify procedural rule citations
- Research recent sanctions decisions in the forum
- Mark all legalcode-mcp citations as VERIFIED in Glass Box

**Without legalcode-mcp:**

- Mark all procedural and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Include notice that legal citations require independent verification

---

## Output Format Template

### For Hold Notice Package:

```markdown
## Litigation Hold Package

**Matter**: [Matter name]
**Matter Reference**: [Reference number]
**Date**: [Date]
**Prepared By**: [Name/Role]

---

## 1. Executive Summary

**Trigger Status**: [Litigation filed / Anticipated / Regulatory]
**Trigger Date**: [Date duty triggered]
**Forum**: [Court/jurisdiction]
**Adverse Party**: [Name]
**Relevant Period**: [Date range]
**Custodian Count**: [Number]
**Data Sources**: [Number of systems]

---

## 2. Trigger Analysis

[Analysis of when and why preservation duty was triggered]

**Confidence**: [Level]

---

## 3. Scope Determination

### Custodians

[List of custodians with roles and relevant data sources]

### Data Sources

[List of systems and repositories covered]

### Subject Matter

[Topics, keywords, and parameters defining relevance]

### Methodology

[Documentation of how scope was determined]

---

## 4. Hold Notice

[Full text of the litigation hold notice]

---

## 5. Custodian Tracking

[Custodian register template or populated register]

---

## 6. Preservation Risk Assessment

| Risk Category | Status             | Notes        |
| ------------- | ------------------ | ------------ |
| [Category]    | [GREEN/YELLOW/RED] | [Assessment] |

---

## 7. Open Items and Remediation Plan

[YELLOW and RED gaps with assigned owners and deadlines]

---

## 8. Release Criteria

[Documented criteria for eventual hold release]

---

## 9. Glass Box Audit Trail

[YAML block]
```

---

## Localization Notes

To create a jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with jurisdiction-specific procedural rules
2. Add specific sanctions standards and case law for the forum
3. Address jurisdiction-specific e-discovery protocols
4. Add data protection/privacy requirements (GDPR, etc.)
5. Update frontmatter to reference the specific jurisdiction

**Key jurisdictional differences:**

| Jurisdiction                  | Key Considerations                                                |
| ----------------------------- | ----------------------------------------------------------------- |
| **US Federal**                | Zubulake standards, FRCP 37(e) sanctions, proportionality factors |
| **US State (varies)**         | State-specific e-discovery rules, sanctions standards             |
| **UK**                        | CPR 31 and Practice Direction 31B, disclosure obligations         |
| **EU**                        | GDPR conflicts, retention limits, cross-border transfer issues    |
| **International Arbitration** | Institution-specific discovery rules, limited sanctions           |

---

## Provenance

Enhanced by Legalcode (2026-03-01). Original skill created 2026-02-27 as jurisdiction-
agnostic framework. This version upgraded to Legalcode quality standard with:

- Multi-step interactive workflow with CLARIFY points
- Comprehensive trigger and scope assessment methodology
- Preservation risk assessment with severity classification
- Citation Quality Gates, Self-Interrogation, and Confidence Scoring
- Glass Box audit trail for traceability
- 15-item anti-patterns catalogue specific to litigation holds
- Writing standards and comprehensive output format template
- External tool integration with graceful degradation
