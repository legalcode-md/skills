---
name: legalcode-deposition-preparation
description: Prepare comprehensive deposition outlines with question sequences organized by topic and
  chronology, exhibit lists with foundation requirements, impeachment areas mapped to prior testimony
  and documents, objection anticipation guides, and witness demeanor assessment frameworks. Use when preparing
  Rule 30(b)(6) corporate designee depositions, expert witness depositions, adverse party depositions,
  or fact witness depositions in federal or state civil litigation. Covers deposition outline design,
  exhibit strategy, impeachment preparation, Daubert foundation mapping for experts, real-time note-taking
  templates, and post-deposition summary workflows. Calibrated to US federal practice (FRCP 30–32) with
  [JURISDICTION-SPECIFIC] markers for state variants and international deposition contexts.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Deposition Preparation

> **Disclaimer**: This skill provides a framework for AI-assisted deposition preparation.
> It does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before use. Federal and state
> procedural rules are amended regularly; verify current applicability before relying on
> any provision described here. Statutory, case law, local-rule, and ethics-rule references
> cited from memory carry hallucination risk — verify against authoritative sources before
> relying on them. Depositions have tactical, strategic, and ethical dimensions that require
> experienced counsel judgment.

## Purpose and Scope

This skill prepares comprehensive deposition packages for civil litigation. It covers the
full arc from pre-deposition strategy through question outline, exhibit preparation,
impeachment mapping, and post-deposition summary. It supports both the **propounding side**
(preparing to take a deposition) and the **defending side** (preparing a client or witness
to testify).

**Covers:**

- Deposition outlines organized by legal issue and chronology, with question sequences and
  cross-references to documentary evidence
- Exhibit lists with foundation requirements, authentication plans, and admissibility risk
  analysis per exhibit
- Impeachment area mapping tied to prior deposition testimony, interrogatory answers,
  affidavits, documents, learned treatises, and bias/motive evidence
- Objection anticipation guides: form, foundation, privilege, hearsay, and relevance
  objections with response scripts and fallback question sequences
- Witness demeanor and credibility assessment across 10 dimensions
- Rule 30(b)(6) corporate designee notice adequacy analysis and preparation checklists
- Expert witness deposition preparation, including Daubert foundation mapping and
  prior-publication impeachment strategies
- Real-time note-taking templates for in-deposition documentation and flag capture
- Post-deposition summary workflows: key admissions extraction, follow-up needs
  assessment, motion support mapping, and errata sheet strategy

**Does not:**

- Prepare criminal depositions, grand jury examinations, or post-conviction proceedings
- Cover international deposition procedures (Hague Evidence Convention, letters rogatory,
  GDPR cross-border transcript constraints) in full depth
- Replace experienced litigators' strategic judgment on deposition scope and sequencing
- Draft deposition notices or subpoenas (scope and service are separate tasks)
- Constitute an expert opinion on any specific evidentiary or ethical question

**Related skills:** `legalcode-discovery-request-drafter` (document and interrogatory
discovery), `legalcode-privilege-review` (privilege screening and log design),
`legalcode-early-case-assessment` (overall case strategy and exposure modeling),
`legalcode-brief-analyzer` (motions to compel, exclude, or limit), `legalcode-case-timeline-builder`
(chronology reconstruction and preservation)

---

## Jurisdiction and Governing Law

This is a US federal-primary skill calibrated to the **Federal Rules of Civil Procedure
(FRCP) Rules 30–32** and the **Federal Rules of Evidence (FRE)**. It applies directly to
federal district court proceedings and to state courts that follow substantially similar
rules.

[JURISDICTION-SPECIFIC] When operating in a specific state or jurisdiction, verify:

- **Deposition limit per side**: FRCP 30(a)(2) allows 10 depositions without leave; many
  states differ — California: 35 (CCP § 2025.610) [VERIFY]; New York: subject to court
  order (CPLR 3106) [VERIFY]; Texas: no per-side limit but subject to court control (TRCP
  Rule 199) [VERIFY]
- **Seven-hour limit**: FRCP 30(d)(1) limits each deposition to one day of seven hours;
  many states allow longer; courts may expand by stipulation or order
- **Rule 30(b)(6) meet-and-confer**: Required since the December 1, 2020 amendment; state
  equivalents may not impose this obligation [VERIFY]
- **Expert deposition timing**: FRCP 26(b)(4)(A) limits expert depositions to after the
  written report; state sequencing rules vary
- **Speaking objection prohibition**: FRCP 30(c)(2) restricts objections to concise,
  nonargumentative statements; state enforcement varies
- **Transcript review period**: FRCP 30(e) allows 30 days for review and errata; states
  vary; circuit split exists on permissible substantive changes [VERIFY]
- **Witness-preparation privilege**: Attorney-witness preparation sessions are generally
  privileged in the US; some civil law jurisdictions restrict witness preparation ethically
- **England & Wales**: Depositions (CPR Part 34) are rare — witness statements serve as
  the functional equivalent; cross-examination occurs at trial [VERIFY]
- **Canada**: Examinations for discovery follow provincial rules; duration limits, topic
  restrictions, and undertaking obligations vary by province [VERIFY]

[JURISDICTION-SPECIFIC] Always verify applicable local court rules and judge-specific
standing orders before serving any deposition notice.

---

## Ethical Boundaries Framework

> **Internalize these constraints before preparing any deposition. Violating them exposes
> counsel to disciplinary proceedings, sanctions, and civil liability.**

Deposition preparation operates within strict ethical guardrails. The line between
legitimate preparation and improper coaching is a core professional responsibility issue.

### What You MAY Do (Proper Preparation)

- Review prior sworn testimony (depositions, trial transcripts) with the witness
- Review the witness's prior written statements (interrogatory answers, affidavits)
- Explain applicable procedural rules and how depositions work
- Prepare the witness to understand the claims and defenses in the case
- Discuss potential questions and how to think about answering them truthfully
- Counsel the witness to listen carefully and ask for clarification of unclear questions
- Advise the witness about their right to consult with counsel during breaks
- Instruct the witness to answer only what is asked, without volunteering information
- Discuss the witness's memory and help them identify documents that refresh recollection
- Conduct mock deposition sessions to build comfort and identify vulnerabilities

### What You MAY NOT Do (Improper Coaching)

- Instruct the witness to provide false, misleading, or evasive testimony
- Suggest specific answers to questions the witness cannot truthfully remember
- Advise the witness to destroy, conceal, or fail to disclose relevant documents
- Instruct the witness to claim privilege over non-privileged communications
- Prepare a Rule 30(b)(6) witness on topics beyond the scope of the deposition notice
- Interpose speaking objections designed to signal how the witness should answer
- Discuss ongoing deposition testimony with the witness during breaks (except to
  determine privilege claims) [VERIFY: circuit-level rules vary on mid-deposition consultations]
- Use improperly obtained privileged documents of the opposing party as impeachment
- Prepare the witness to deny recollection of matters the witness actually recalls

**Governing ethics rules (US):** ABA Model Rule 3.4(b) (assisting false testimony),
Model Rule 8.4(c) (dishonesty, deceit), Model Rule 3.3 (candor toward the tribunal).
[JURISDICTION-SPECIFIC] Verify against applicable state bar rules, which may be stricter
than the ABA Model Rules.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
deposition strategy, the workflow pauses and asks when:

- The answer would change which outline structure or question sequences to generate
- The deposition type (corporate designee, expert, adverse, friendly) is unclear
- The strategic objective (evidentiary pinning, impeachment building, settlement leverage)
  determines which topics to emphasize
- Scope constraints arising from the scheduling order or witness profile require adjustment
- Prior materials available will shape the impeachment strategy significantly

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

### Step 1: Accept the Matter Frame

Accept input in any of these formats:

- **Case description**: Complaint, answer, key claims/defenses, case type
- **Deposition notice or subpoena**: The formal document served
- **Witness profile**: What is known about the witness (role, involvement, knowledge base)
- **Prior transcripts**: Prior deposition or trial testimony of this witness
- **Expert report**: The expert's written report under FRCP 26(a)(2)
- **Scheduling order**: Discovery dates, limits, and scope orders from the governing court

If only a case type and witness name are provided, proceed to Step 2.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user these questions. Present as structured
options. Skip questions already answered by the input.

1. **Which side are you on?**
   - Options: **Propounding** (taking the deposition), **Defending** (preparing a witness),
     **Both**
   - _Why this matters_: The entire workflow changes — propounding generates an attack
     outline; defending generates a preparation guide and anticipated-question map.

2. **Deposition type?**
   - Options: **Rule 30(b)(6) corporate designee**, **Expert witness (friendly — direct)**,
     **Expert witness (opposing — cross-examination)**, **Adverse fact witness**,
     **Friendly/neutral fact witness**, **Adverse party deponent**
   - _Why this matters_: Each type requires a fundamentally different outline structure,
     preparation depth, and legal framework. Corporate designee requires notice adequacy
     analysis; opposing expert requires Daubert mapping; friendly witnesses need walk-through
     structure.

3. **Strategic objective?**
   - Options: **Pin down facts for summary judgment**, **Create trial impeachment
     opportunities**, **Support or undercut settlement valuation**, **Limit scope and
     damage (defensive)**, **Comprehensive — all of the above**
   - _Why this matters_: Summary judgment depositions focus on undisputed facts; trial
     impeachment depositions target credibility inconsistencies; settlement depositions
     surface exposure early.

4. **Case type?**
   - Options: Commercial dispute / Employment / Intellectual property / Personal injury /
     Contract / Securities / Real estate / Patent / Antitrust / Other (describe)
   - _Why this matters_: Determines which case-type template to activate and which legal
     elements the deposition must support.

5. **Jurisdiction and governing rules?**
   - Options: US Federal (FRCP 30-32) / US State — which state / Other
   - _Why this matters_: Deposition limits, time limits, transcript review periods, and
     expert deposition sequencing rules vary materially by jurisdiction.

6. **Available materials?** (multi-select)
   - Options: Prior deposition transcript, Prior interrogatory answers / written statements,
     Expert report (FRCP 26(a)(2)), Documents and exhibits, No prior materials — cold prep
   - _Why this matters_: Determines how deep impeachment mapping can go and what exhibit
     preparation is possible.

7. **Witness profile** (free text):
   - Prompt: What do you know about this witness's role, knowledge base, and likely
     demeanor? Any known vulnerabilities — prior inconsistent statements, bias indicators,
     subject-matter gaps?
   - _Why this matters_: Shapes question sequencing, credibility assessment depth, and
     objection anticipation.

State assumptions explicitly if proceeding with partial context (e.g., "Assuming you are
the propounding side — correct me if wrong and I will re-run the analysis").

### Step 3: Gather Jurisdiction-Relevant Legal Authority

Identify the applicable procedural and evidentiary rules before analyzing the matter.

Use **legalcode-mcp** if connected to:

- Pull current text of FRCP 30, 30(b)(6), 30(c), 30(d), 30(e), 31, 32
- Pull FRE 611 (control of examination), 613 (prior statements), 701–705 (expert
  testimony), 608–609 (character and credibility), 801–807 (hearsay and exceptions),
  901–902 (authentication)
- Pull key cases on: speaking objection sanctions, 30(b)(6) preparation obligations,
  Daubert methodology standards [509 U.S. 579 (1993)] [VERIFY], errata sheet circuit split
- Pull applicable state bar ethics opinions on witness preparation boundaries

Save results to `/tmp/legalcode-deposition-authority.md`:

```markdown
# Legal Authority — [Witness Name / Matter]

## Jurisdiction: [FRCP / State]

## Date: [date]

### Procedural Rules

- [Rule, current text, deposition-specific notes]

### Evidence Rules

- [Rule, text, application to this deposition]

### Case Law

- [Case, citation, key holding]

### Ethics Opinions

- [Citation, holding, application]
```

**Without legalcode-mcp**: Proceed with best-practice guidance and mark all specific
citations [VERIFY] before relying on them. Note in the Glass Box:
`legalcode_mcp: "Not connected"`.

### Step 4: Rule 30(b)(6) Notice Adequacy Analysis

**Skip this step if the deposition is not a Rule 30(b)(6) corporate designee deposition.**

Analyze the deposition notice for adequacy before proceeding:

#### Notice Adequacy Checklist

| Element                | Adequacy Assessment                                                                                                                              | Risk Level |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **Topic specificity**  | Are topics stated with "reasonable particularity" as required? Vague catch-all topics (e.g., "all matters related to the dispute") are deficient | HIGH       |
| **Topic scope**        | Are topics limited to matters the organization can reasonably prepare for? Overly broad topics invite protective orders                          | MEDIUM     |
| **Time periods**       | Is a relevant time period specified for each topic?                                                                                              | MEDIUM     |
| **Document request**   | Does the notice include a subpoena duces tecum? Are document categories specific and bounded?                                                    | HIGH       |
| **Meet-and-confer**    | Has the 2020-amended FRCP 30(b)(6) meet-and-confer requirement been satisfied? [VERIFY: effective December 1, 2020]                              | CRITICAL   |
| **Notice period**      | Is there adequate lead time for the organization to designate and prepare witnesses?                                                             | MEDIUM     |
| **Designation format** | Has the noticing party requested that the organization identify the designee(s) by name in advance?                                              | LOW        |

**If propounding side**: Evaluate whether your notice adequately covers the topics you
need. Flag deficiencies in your own notice before the deposition.

**If defending side**: Identify topics that are deficient or objectionable; prepare a
meet-and-confer agenda and draft an objection letter template.

**Rule 30(b)(6) preparation obligations (defending side)**:

- Designate one or more witnesses able to speak for the organization on each noticed topic
- Prepare designated witnesses on all "reasonably available" information, including
  information held by former employees and agents [VERIFY under applicable circuit law]
- If no current employee has personal knowledge, the organization must investigate and
  prepare a witness with the gathered information — the obligation does not disappear
- Failure to adequately prepare a designee can result in FRCP 37 sanctions [VERIFY]

### Step 5: Map Issues to Deposition Topics

Organize material case issues into a deposition topic map before drafting questions.

#### Issue-to-Topic Matrix

| Legal Element   | Proof Required                          | Witness's Likely Knowledge | Key Documents           | Deposition Goal         | Priority |
| --------------- | --------------------------------------- | -------------------------- | ----------------------- | ----------------------- | -------- |
| [e.g., Breach]  | [Acts / omissions violating obligation] | [Role in relevant events]  | [Contract, emails]      | [Pin down timeline]     | GREEN    |
| [e.g., Damages] | [Causation + quantum]                   | [Financial records access] | [Invoices, projections] | [Lock in floor/ceiling] | GREEN    |
| [e.g., Notice]  | [Receipt + timing of notice]            | [Mail / email access]      | [Correspondence]        | [Establish or undercut] | YELLOW   |

#### Topic Prioritization

Classify each topic using the three-tier framework:

| Classification | Definition                                                                  | Action                                                  |
| -------------- | --------------------------------------------------------------------------- | ------------------------------------------------------- |
| **GREEN**      | Core liability or damages element; unique witness knowledge; time-efficient | Lead with this; full outline depth; detailed follow-ups |
| **YELLOW**     | Important but duplicated in other discovery, or time-constrained            | Include but narrower; fewer follow-up levels            |
| **RED**        | Peripheral, duplicative, or high-objection risk without strategic return    | Defer or omit; consider alternative discovery tools     |

Apply these six factors when classifying:

1. Importance to claims or defenses — is this outcome-determinative?
2. Witness's unique knowledge — can only this witness answer?
3. Prior discovery coverage — already addressed by interrogatory or document production?
4. Impeachment opportunity — is there a prior statement or document to contrast?
5. Objection risk — privilege, relevance, or proportionality risk?
6. Time efficiency — how many deposition hours does this topic justify?

### Step 6: Build the Deposition Outline

Design the outline using the structure appropriate to the deposition type.

#### 6a. Outline Architecture by Deposition Type

**Rule 30(b)(6) Corporate Designee Outline:**

1. Witness identity — name, title, tenure, supervisory chain
2. Corporate structure relevant to noticed topics — organizational chart, decision-makers
3. Document retention and custodian identification
4. Topic-by-topic examination in notice order — link each to documents
5. Scope confirmation — ask whether any persons with additional relevant knowledge have not been identified
6. Completeness certification — confirm nothing was withheld from preparation

**Expert Witness — Opposing (Cross-Examination):**

1. Qualifications framing — surface gaps, limitations, academic vs. industry experience
2. Retention and prior work — frequency, side, compensation structure, prior engagements
3. Materials reviewed — identify what was NOT requested, reviewed, or considered
4. Opinion scope — extract admissions limiting opinions to the disclosed report
5. Methodology stress-test — commit to methodology; expose flaws (error rate, peer review,
   testability, general acceptance per Daubert) [VERIFY]
6. Prior inconsistent opinions — mine prior reports, transcripts, and publications
7. Compensation and bias — total fees, percentage of income from litigation, financial
   interest in outcome

**Expert Witness — Friendly (Direct Examination Preparation):**

1. Qualifications walk-through — build a compelling credentials narrative
2. Retention and materials review — demonstrate thoroughness of preparation
3. Opinion elicitation — FRE 702-705 foundation for each opinion [VERIFY]
4. Methodology validation — explain reliability and applicability to this case
5. Opinion-scope limitation — clearly bound opinions to the disclosed report
6. Anticipate cross-examination attacks — prepare for bias, methodology, and prior
   publications challenges

**Adverse Party or Fact Witness Outline:**

1. Background and role in the relevant events
2. Chronological walk-through — establish the timeline
3. Document-by-document examination — show, authenticate, extract testimony
4. Knowledge and intent — what did you know; when did you know it; what did you do
5. Damages or harm — extent, causation, mitigation steps
6. Impeachment sequences — prior interrogatory answers, affidavits, prior testimony

**Friendly Fact Witness Preparation (Defending Side):**

1. Explain the deposition process, the oath, and the obligation to answer truthfully
2. Map what the witness knows, how they know it, and which documents they reviewed
3. Walk through anticipated questions from opposing counsel based on case theory
4. Coach listening discipline — answer only what is asked; ask for clarification of
   unclear questions; do not speculate
5. Review prior statements — surface any inconsistencies and explain them before deposition

#### 6b. Question Design Principles

| Principle                     | Rule                                                                          | Example                                                              |
| ----------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Leading for cross**         | Use leading questions to control adverse witnesses                            | "Isn't it true that you never reviewed the contract before signing?" |
| **Open for direct**           | Use open questions to elicit full narrative from friendly witnesses           | "Please describe what happened at the June 15 meeting."              |
| **One fact per question**     | Never compound: one discrete fact per question                                | Wrong: "Did you attend and were you aware of the policy?"            |
| **Commit before challenging** | Lock the witness into a position before showing the contradictory document    | Get: "You never received notice" THEN: "Let me show you Exhibit 12." |
| **Know the answer**           | Never ask a propounding question to which you do not know the expected answer | Research and document expected answers before the deposition         |
| **Sequence tactically**       | Build momentum with comfortable topics; reserve impeachment for later         | Don't reveal credibility attacks before establishing baseline        |
| **Leave doors open**          | Elicit a clean commitment on each impeachment target                          | "That is your complete answer, correct?"                             |
| **Confirm knowledge scope**   | At each topic, confirm what the witness knows — and does not know             | "Who else in the organization has knowledge about this topic?"       |

### Step 7: Build the Exhibit List with Foundation Requirements

For each exhibit to be used in the deposition, prepare a foundation plan.

#### Exhibit Foundation Matrix

| #   | Exhibit         | Bates/Doc ID | Foundation Required                    | Who Establishes        | Auth Method        | Admissibility Risk | Q Sequence                                                |
| --- | --------------- | ------------ | -------------------------------------- | ---------------------- | ------------------ | ------------------ | --------------------------------------------------------- |
| 1   | [Contract]      | [P0001-25]   | Authentication + execution authority   | Signatory or custodian | Witness testimony  | LOW                | "Is this your signature? Did you negotiate these terms?"  |
| 2   | [Email chain]   | [D0100-15]   | Author identification, account control | Sender or recipient    | Witness testimony  | MEDIUM             | "Is this your email address? Did you write this message?" |
| 3   | [Expert report] | N/A          | FRCP 26(a)(2) disclosure               | Expert witness         | Direct examination | LOW                | "Is this the report you submitted in this case?"          |

#### Foundation Requirements by Document Type

| Document Type               | Foundation Requirements                                                   | Governing Rule                  |
| --------------------------- | ------------------------------------------------------------------------- | ------------------------------- |
| Email                       | Author identity, account control, no material alteration                  | FRE 901(b)(4), (b)(11) [VERIFY] |
| Business record             | Regular course of business, contemporaneous creation, qualified witness   | FRE 803(6) [VERIFY]             |
| Contract or signed document | Signatory identity, authority to sign                                     | FRE 901(b)(1) [VERIFY]          |
| Photograph or video         | Accurate depiction of relevant scene                                      | FRE 901(b)(1), (b)(9) [VERIFY]  |
| Prior deposition transcript | Certified transcript, available or unavailable witness                    | FRCP 32, FRE 804 [VERIFY]       |
| Opposing party statement    | Identity as party or authorized agent                                     | FRE 801(d)(2) [VERIFY]          |
| Expert publication          | Acknowledged by expert or established by reputation as reliable authority | FRE 803(18) [VERIFY]            |
| Database or ESI             | System reliability, extraction accuracy, chain of custody                 | FRE 901(b)(9) [VERIFY]          |

**Contingency planning**: If foundation cannot be established through the deponent, identify
the alternative foundation witness, stipulation request, or request for judicial notice.

### Step 8: Map the Impeachment Areas

Systematically identify all available impeachment material before the deposition.

#### Impeachment Source Inventory

| Source Type                 | Specific Material                       | Topic Area       | Prior Statement          | Expected Position              | Strength                                | Sequence                                         |
| --------------------------- | --------------------------------------- | ---------------- | ------------------------ | ------------------------------ | --------------------------------------- | ------------------------------------------------ |
| Prior deposition transcript | [Trans., date, page:line]               | [Topic]          | [Prior statement]        | [Current likely position]      | DISPOSITIVE/SIGNIFICANT/MODERATE        | Commit → Credit → Confront                       |
| Interrogatory answer        | [Interrogatory #, verbatim answer]      | [Topic]          | [Prior answer]           | [Current claim]                | HIGH/MED/LOW                            | Show, confirm under oath, elicit contradiction   |
| Prior affidavit             | [Affidavit, date]                       | [Topic]          | [Sworn statement]        | [Expected deposition position] | HIGH                                    |                                                  |
| Document                    | [Document reference]                    | [Topic]          | [Document content]       | [Expected testimony]           | HIGH/MED/LOW                            |                                                  |
| Learned treatise            | [Publication, author, page]             | [Expert topic]   | [Published passage]      | [Expert's opinion]             | HIGH (if expert acknowledges authority) | Establish authority → Read contradicting passage |
| Prior expert report         | [Report, case, date]                    | [Expert opinion] | [Prior opinion text]     | [Current opinion]              | HIGH                                    |                                                  |
| Bias / financial interest   | [Compensation, employment relationship] | [Credibility]    | [Financial relationship] | [Claimed neutrality]           | HIGH                                    |                                                  |

#### Impeachment Execution: The Three-C Sequence

For each impeachment area, follow this sequence:

1. **Commit** — Lock the witness into the current position you intend to challenge:
   - "Your testimony is that you never received notice of the breach?"
   - "And you are certain of that?"
   - "Is that your complete testimony on this point?"

2. **Credit** — Establish the authority and credibility of the prior inconsistent source:
   - "You gave a deposition in the Smith matter in June 2024, correct?"
   - "Your attorney represented you at that time?"
   - "You swore under oath to tell the truth?"
   - "And a certified court reporter transcribed your testimony?"

3. **Confront** — Present the prior inconsistent statement clearly and specifically:
   - "I am showing you page 47, lines 12 through 18 of that transcript. Please read it."
   - "Does that refresh your recollection?"
   - "And today you are telling us [contradictory position]. Is that your testimony?"

**For expert witnesses — learned treatise impeachment (FRE 803(18))**:

- Establish that the publication is "a reliable authority in the field" [VERIFY]
- If expert declines to acknowledge, establish reliability through reputation or other experts
- Read the contradicting passage and ask the expert to reconcile the inconsistency

### Step 9: Build the Objection Anticipation Guide

For each key question or topic, predict likely objections and prepare response scripts.

#### Objection Classification Framework

| Objection Type                            | Rule Basis          | When Used                                                  | Proper Form                                                         | Waived if Not Made?              | Counter-Position                                                            |
| ----------------------------------------- | ------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------- |
| **Form — Vague/Ambiguous**                | FRCP 30(c)(2)       | Question is unclear                                        | "Objection. Form."                                                  | YES                              | Rephrase with specificity; note if objection is itself a speaking objection |
| **Form — Compound**                       | FRCP 30(c)(2)       | Question contains multiple discrete questions              | "Objection. Form."                                                  | YES                              | Separate into individual questions                                          |
| **Form — Leading (on direct)**            | FRE 611(c)          | Leading question to own witness                            | "Objection. Leading."                                               | NO                               | Rephrase as open question                                                   |
| **Foundation — Lacks Personal Knowledge** | FRE 602             | Witness lacks direct knowledge                             | "Objection. Foundation."                                            | YES                              | Lay foundation: "How do you know? Were you present?"                        |
| **Privilege — Attorney-Client**           | FRE 501, common law | Question calls for privileged communication                | "Objection. Privilege. I am instructing the witness not to answer." | NO                               | Confirm privilege basis on record; mark for potential motion to compel      |
| **Privilege — Work Product**              | FRCP 26(b)(3)       | Question calls for attorney mental impressions             | "Objection. Work product."                                          | NO                               | Distinguish factual from opinion work product                               |
| **Hearsay**                               | FRE 801-807         | Question asks for out-of-court statement offered for truth | "Objection. Hearsay."                                               | NO (goes to trial admissibility) | Identify applicable exception (FRE 803, 804, 807) or non-hearsay purpose    |
| **Speculation**                           | FRE 701, 602        | Witness asked to speculate beyond personal knowledge       | "Objection. Calls for speculation."                                 | NO                               | Reframe: "Based on your direct knowledge and observation…"                  |
| **Relevance**                             | FRE 401             | Question exceeds case scope                                | "Objection. Relevance."                                             | NO                               | Note proper scope under FRCP 26(b)(1) and deposition notice                 |

#### Speaking Objection Detection and Response

A **speaking objection** coaches the witness rather than stating a legal ground. Examples:

- "Objection — she wasn't at that meeting so she can't answer that" (signals the answer)
- "Objection, vague — do you mean the first meeting or the second one?" (suggests the answer)
- "Objection, foundation — she didn't have personal knowledge of the agreement" (tells the
  witness what to say about her knowledge)

**Response protocol to speaking objections**:

1. State calmly on the record: "I would ask counsel to limit objections to stating the
   legal ground without coaching the witness, as required by FRCP 30(c)(2)."
2. If the pattern continues: "I am noting for the record that counsel is making repeated
   speaking objections in violation of FRCP 30(c)(2). The witness may answer."
3. If egregious or persistent: Consider a FRCP 30(d)(3) motion to terminate or limit the
   deposition.

**Managing instruction-not-to-answer directives**:

- Confirm the privilege basis on the record: "What privilege are you asserting?"
- Note the refusal and move on; mark the question for a potential FRCP 37 motion to compel
- Improper instruction-not-to-answer grounds (e.g., relevance alone) should be challenged
  on the record

### Step 10: Witness Credibility Assessment Framework

Assess the witness across 10 dimensions before the deposition. For each dimension, assign
a status and confidence level.

#### Classification Scale

| Status         | Definition                                                                   | Action                                                                              |
| -------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **STRONG**     | Favorable to the witness's credibility on this dimension                     | Propounding: target to undermine; Defending: reinforce                              |
| **NEEDS WORK** | Manageable but requires preparation or follow-up                             | Propounding: probe for weakness; Defending: additional prep sessions                |
| **VULNERABLE** | Exploitable weakness; opposing counsel will target                           | Propounding: develop full question sequence; Defending: remediate before deposition |
| **CRITICAL**   | Fundamental credibility problem; case-altering if exploited or not addressed | Propounding: lead with this at trial; Defending: strategic decision required        |

#### Ten-Dimension Credibility Assessment

| #   | Dimension                     | STRONG                                                                          | NEEDS WORK                                                            | VULNERABLE                                                        | CRITICAL                                                         |
| --- | ----------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------- |
| 1   | **Internal Consistency**      | No known prior inconsistent statements; all testimony consistent with documents | Minor inconsistencies with ready explanations                         | Multiple inconsistencies across sworn statements                  | Contradiction of central facts in prior sworn testimony          |
| 2   | **Subject-Matter Knowledge**  | Deep personal knowledge directly from experience and role                       | Adequate knowledge with some gaps on secondary topics                 | Significant gaps in knowledge of key topics claimed               | Witness claims knowledge they demonstrably lack                  |
| 3   | **Memory Quality**            | Clear, specific recollection with documentary support                           | General recollection; some uncertainty on peripheral details          | Selective or conveniently poor memory on key events               | Blanket "I don't recall" on core, document-supported topics      |
| 4   | **Bias Indicators**           | No financial interest; neutral relationship to outcome                          | Explained relationship to party; bias acknowledged and contextualized | Clear financial or employment interest undisclosed                | Compensation or employment directly tied to case outcome         |
| 5   | **Motive to Lie**             | No discernible motive to shade testimony                                        | Minor professional interest that does not create strong incentive     | Strong personal or financial motive to shade testimony            | Criminal liability or major financial interest in outcome        |
| 6   | **Demeanor (Anticipated)**    | Professional, credible, measured based on prior testimony or profile            | Likely nervous but recoverable with preparation                       | Prior evasion, aggression, or poor deposition history             | Prior sanctions for witness conduct; known combative deponent    |
| 7   | **Perception Reliability**    | Was present; directly observed key events; no reported impairment               | Partially observed key events with explainable gaps                   | Knowledge reconstructed from others; largely secondhand           | No direct observation; all knowledge from hearsay or documents   |
| 8   | **Expert Opinion Foundation** | Fully documented methodology; peer-reviewed; tested; within expertise           | Adequate methodology with minor gaps                                  | Methodology contestable or extrapolated beyond expertise          | Methodology unreliable under Daubert/Frye standard [VERIFY]      |
| 9   | **Prior Testimony Record**    | Clean prior deposition or trial record on similar topics                        | Prior testimony with minor explainable inconsistencies                | Prior testimony directly contradicts expected deposition position | Prior sworn statement is a case-dispositive contradiction        |
| 10  | **Impeachment Exposure**      | No available impeachment material                                               | Limited impeachment available on peripheral issues                    | Multiple impeachment vectors on core issues                       | Smoking-gun prior statement directly contradicting key testimony |

---

## Classification Systems

### Objection Predictability Classification

| Level        | Range     | Definition                                              | Prescribed Action                                                             |
| ------------ | --------- | ------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **DEFINITE** | 0.95-1.0  | Objection is certain to be raised; rule clearly applies | Prepare counter-position and fallback question sequence before the deposition |
| **HIGH**     | 0.80-0.94 | Objection very likely; strong rule basis                | Prepare counter-position; consider preemptive reframe                         |
| **PROBABLE** | 0.60-0.79 | Objection likely if opposing counsel is prepared        | Prepare response; have foundation question ready                              |
| **POSSIBLE** | 0.40-0.59 | Objection may be raised; uncertain basis                | Note; have response available if raised                                       |
| **UNLIKELY** | 0.0-0.39  | Objection unlikely; weak or no rule basis               | No specific preparation needed                                                |

### Preparation Readiness Classification (Defending Side)

| Status                    | Definition                                                                        | Action                                                    |
| ------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **READY**                 | Witness is prepared on topic; testimony will be credible and consistent           | Light review only                                         |
| **NEEDS WORK**            | Witness has knowledge gaps, inconsistencies, or anxiety on the topic              | Additional preparation sessions required                  |
| **NOT READY**             | Witness is substantially unprepared; testimony risk is high                       | Deep remediation required; consider seeking a continuance |
| **VULNERABILITY MANAGED** | Known vulnerability has been addressed; witness understands the response strategy | Monitor during deposition; execute contingency if needed  |

### Impeachment Strength Classification

| Level           | Definition                                                            | Strategic Use                                                     |
| --------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **DISPOSITIVE** | Contradiction goes to a central fact; could change case outcome       | Lead with this at trial; use at deposition to create the record   |
| **SIGNIFICANT** | Contradiction materially undermines credibility on an important issue | Develop full commit-credit-confront sequence; prioritize          |
| **MODERATE**    | Contradiction undermines a secondary issue                            | Include if deposition time permits; useful for closing argument   |
| **MINOR**       | Peripheral inconsistency unlikely to affect outcome                   | Low priority; consider whether it distracts from stronger attacks |

---

## Actionable Output Per Finding

For each identified issue in the deposition preparation package, structure as:

```
**Issue/Topic**: [Name of deposition topic or credibility dimension]
**Classification**: [Objection predictability / Preparation readiness / Impeachment strength]
**Description**: [What the issue is and why it matters to the deposition]
**Evidence/Authority**: [Document cite, rule reference, prior testimony page:line]
**Deposition Strategy**: [Specific question sequence or preparation approach]
**Contingency**: [If primary strategy fails, what is the fallback?]
**Confidence**: [Definite / High / Probable / Possible / Unlikely]
```

---

## Prioritization Framework

### Tier 1 — Must Address (Deposition Prerequisites)

Issues that must be resolved before the deposition proceeds:

- Rule 30(b)(6) notice deficiencies that would make the deposition futile
- Pending protective order motions that could limit scope
- Ethical boundary violations identified in the proposed preparation plan
- Missing foundational documents needed to authenticate key exhibits
- Scheduling order conflicts or deposition limit exhaustion issues

### Tier 2 — Critical Preparation (High Strategic Value)

Issues that materially affect deposition effectiveness:

- DISPOSITIVE and SIGNIFICANT impeachment areas requiring full commit-credit-confront sequences
- Expert credibility dimensions rated VULNERABLE or CRITICAL (Daubert attack preparation)
- Rule 30(b)(6) topics where witness preparation is NOT READY
- Key exhibits where foundation is uncertain and alternative plans are needed
- Anticipated speaking objection patterns requiring pre-deposition strategy
- Credibility dimensions scoring CRITICAL across multiple dimensions

### Tier 3 — Enhance Preparation (Tactical Improvements)

Issues that improve the deposition without being essential:

- MODERATE impeachment areas worth developing if time permits
- Supplemental question sequences for peripheral topics
- Additional exhibit lists for contingency scenarios
- Demeanor coaching on secondary topics
- Nice-to-have admissions for closing argument or mediation use

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Identify deposition type, side, strategic objective. Classify topics (GREEN /
YELLOW / RED). Identify which rules, prior statements, and documents are engaged.

**DO**: Execute the outline design, exhibit foundation plan, impeachment mapping, and
objection anticipation guide. Score witness credibility across all 10 dimensions.

**CHECK**: Run the Citation Quality Gates. For any Tier 1 issue, run the Self-Interrogation.
Verify all FRCP and FRE citations against authoritative sources where possible. Confirm the
time allocation is realistic.

**ACT**: Note any new impeachment patterns discovered. Update case timeline with facts
established. Flag heuristics for future depositions of this witness type.

### Citation Quality Gates

Run these five gates silently before delivering any output:

| Gate           | Rule                                                                                               | Fail Action                         |
| -------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every procedural or evidentiary claim cites a specific rule number                                 | Add citation or mark [VERIFY]       |
| **Format**     | Transcript citations include witness name, date, page, and line number                             | Fix format                          |
| **Currency**   | Rules checked for amendments (e.g., FRCP 30(b)(6) 2020 amendment, 2015 proportionality amendments) | Flag [CHECK CURRENCY]               |
| **Domain**     | Analysis stays within the applicable jurisdiction; no cross-jurisdiction procedural bleed          | Remove or flag jurisdictional bleed |
| **Confidence** | Objection predictions and credibility assessments carry explicit confidence levels                 | Add confidence qualifier            |

### Self-Interrogation for Tier 1 Issues

For any issue classified as Tier 1, apply this 3-pass self-interrogation:

**Pass 1 — Legal Chain Integrity**:

- Does the legal risk follow directly from the specific rule or ethical obligation cited?
- Would a court or disciplinary body actually reach this conclusion on these facts?
- Is there a counter-argument opposing counsel or the regulator would make?

**Pass 2 — Completeness**:

- Have all relevant FRCP, FRE, and state-rule provisions been considered?
- Have applicable local court rules and judge standing orders been verified?
- Are there ethics opinions that directly address this preparation scenario?

**Pass 3 — Challenge**:

- What is the strongest argument that the proposed approach is proper?
- Under what circumstances would a reasonable practitioner take a different position?
- Is this really Tier 1, or is it actually Tier 2 with a manageable contingency?

Mark audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                          | Action                                                |
| ------------ | --------- | ------------------------------------------------ | ----------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled rule, clear precedent, no ambiguity      | State with confidence                                 |
| **High**     | 0.80-0.94 | Strong authority, minor interpretation questions | State with brief caveat                               |
| **Probable** | 0.60-0.79 | Good arguments but reasonable minds could differ | State with explicit reasoning and contra-indicators   |
| **Possible** | 0.40-0.59 | Genuinely uncertain — rule application contested | Flag for counsel review with both sides presented     |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative                          | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every deposition preparation output MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-deposition-preparation"
  matter: "[Case name / matter identifier]"
  witness: "[Witness name, title, and organizational role]"
  side: "[Propounding / Defending / Both]"
  deposition_type: "[30(b)(6) / Expert-opposing / Expert-friendly / Adverse / Friendly]"
  strategic_objective: "[Summary judgment / Trial impeachment / Settlement / Comprehensive]"
  jurisdiction: "[US Federal FRCP / US [State name] / Other]"
  case_type: "[Commercial / Employment / IP / Personal Injury / Patent / Other]"
  materials_reviewed:
    - "[Prior deposition transcript dated — AVAILABLE / NOT AVAILABLE]"
    - "[Expert report dated — AVAILABLE / NOT AVAILABLE]"
    - "[Interrogatory answers — AVAILABLE / NOT AVAILABLE]"
  topics_total: "[N]"
  topics_green: "[N]"
  topics_yellow: "[N]"
  topics_red: "[N — deferred or omitted]"
  total_questions_drafted: "[N]"
  estimated_deposition_hours: "[X]"
  exhibits_prepared: "[N]"
  impeachment_vectors_identified: "[N]"
  objections_anticipated: "[N]"
  30b6_notice_analyzed: "YES / NO / NOT APPLICABLE"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-deposition-authority.md or 'Not created']"
  rules_consulted:
    - "[FRCP 30 — VERIFIED (legalcode-mcp) or [VERIFY]]"
    - "[FRE 613 — VERIFIED (legalcode-mcp) or [VERIFY]]"
  citations_verified: "[N VERIFIED] / [N [VERIFY]]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no Tier 1 issues)"
  ethical_boundaries_reviewed: "YES"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified legal review before deposition"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in deposition preparation:

1. **Asking questions without knowing the answer (propounding side)** — Never ask an
   adverse witness a question to which you do not know the expected answer. Depositions pin
   down known facts; they are not exploration tools. Asking open questions of hostile
   witnesses invites damaging narratives you cannot control.

2. **Failing to complete the Rule 30(b)(6) meet-and-confer** — Proceeding with a corporate
   designee deposition without satisfying the December 2020 amendment's meet-and-confer
   requirement. Courts have sanctioned both sides for this omission. [VERIFY: FRCP 30(b)(6)
   as amended December 1, 2020]

3. **Coaching through speaking objections** — Interposing objections that signal the answer
   rather than stating the legal ground. "Objection — she wasn't in that meeting" violates
   FRCP 30(c)(2) and is sanctionable. One legal ground. Nothing more.

4. **Preparing a 30(b)(6) designee on topics not in the notice** — Allowing testimony
   beyond noticed topics without formally expanding scope. The organization is bound by
   designee testimony on noticed topics; exceeding scope creates inconsistencies.

5. **Over-preparing witnesses to the point of artificial responses** — Scripting answers
   so completely that the witness sounds rehearsed. Over-coached witnesses speak like
   lawyers; jurors and judges notice and discount them accordingly.

6. **Missing impeachment from prior expert reports and publications** — Failing to mine the
   opposing expert's prior reports, trial transcripts, and publications before the
   deposition. For experienced experts, prior testimony is the richest source of
   contradiction material.

7. **Using exhibits before committing the witness to a position** — Showing the
   contradictory document before locking in the testimony you intend to contradict.
   Once the witness sees the document, they can pivot. Follow commit → credit → confront
   without exception.

8. **No time management plan** — Failing to map estimated time per topic against the
   seven-hour FRCP 30(d)(1) limit. Running out of time before covering key topics is a
   preparation failure, not a surprise.

9. **Exhibits without authentication plans** — Assuming exhibits will be authenticated
   without advance planning. Identify the foundation witness for each exhibit at the
   deposition stage; authentication failures at trial are preventable at this step.

10. **Ignoring the Rule 30(e) errata sheet** — Failing to develop a strategy for the
    30-day errata sheet review window. Material substantive changes (not merely
    typographical corrections) can and should be challenged; courts are split on scope
    of permissible changes [VERIFY: circuit split on FRCP 30(e)].

11. **No real-time follow-up system** — Taking depositions without a structured note-taking
    system that flags evasions, new facts, and follow-up opportunities in the room. The
    most valuable follow-up questions come from deposition answers, not from pre-prepared
    outlines.

12. **Inadequate 30(b)(6) designee preparation** — Presenting a designee who has not
    reviewed all reasonably available information on noticed topics. If no current employee
    knows the answer, the obligation to prepare does not disappear — the organization must
    gather information from former employees, agents, and documents.

13. **No post-deposition summary workflow** — Allowing the transcript to sit without
    systematic extraction of key admissions, follow-up needs, and motion support. Deposition
    value degrades rapidly without structured post-deposition analysis within 72 hours.

14. **Shallow bias cross-examination for experts** — Asking total fees only, rather than
    developing the full financial picture: percentage of income from litigation work,
    frequency of testifying for the same side, history with retaining counsel, and prior
    employment relationships.

15. **Accepting "I don't recall" without follow-up** — Moving past memory gaps without
    testing them. Ask: What DO you recall about that topic? Would reviewing documents help?
    Who else would know? Is this a genuine gap or a deliberate evasion?

16. **Not tying deposition questions to the summary judgment theory** — Deposing witnesses
    without a clear map of which questions support which elements of the dispositive
    motion. Every question should serve case strategy; unfocused questions waste deposition
    time and signal case theory to opposing counsel.

17. **Violating privilege through over-disclosure in preparation** — Discussing substantive
    legal theories and litigation strategy in preparation sessions in ways that make the
    session content arguably discoverable. The session itself is privileged; the facts
    discussed within it are not.

18. **Deposing the wrong witness** — Spending deposition budget on witnesses with peripheral
    knowledge rather than decision-makers, document custodians, or key experts. Prioritize
    deposition targets based on unique knowledge, not organizational hierarchy or convenience.

19. **Compound questions that generate ambiguous records** — Asking questions that bundle
    multiple facts and receive a single "yes" or "no" — creating an ambiguous transcript
    that is hard to use at trial or on a summary judgment motion.

20. **Single-pass outline design** — Writing the outline in one pass without cross-checking
    for: topic coverage against the issue map, time allocation against the deposition limit,
    exhibit foundation against the question sequence, and impeachment material against the
    topics covered. Single-pass drafting produces outlines with structural gaps.

---

## Writing Standards

Apply plain-language discipline to all deposition preparation output:

**For deposition outlines (used in the deposition room)**:

- Concise question text — one idea per line
- Trigger cues in brackets: `[If witness says X, go to Q14]`
- Transcript citations at point of use: `[Prior Dep. 47:12-18]`
- Exhibit numbers at point of use: `[Show Exhibit 12]`
- Time estimates per topic: `[~15 min]`

**For witness preparation guides (shared with the witness)**:

- Plain language — no legal jargon
- Active voice: "Answer only what is asked" not "Only the asked question should be answered"
- Numbered steps the witness can follow sequentially
- Clear explanation of why each instruction exists

**Quality gates before delivery**:

1. Does every exhibit have a foundation plan and a contingency if the witness cannot authenticate?
2. Does every impeachment sequence follow commit → credit → confront?
3. Are time allocations realistic within the applicable deposition time limit?
4. Have all citations been checked or marked [VERIFY]?
5. Has the Ethical Boundaries Framework been reviewed against the preparation approach?
6. Are speaking objection risks identified in the Objection Anticipation Guide?

---

## Real-Time Deposition Note-Taking Template

Use this three-column format during the deposition:

```
| Q # | Answer Summary | Follow-Up / Flags |
|-----|---------------|------------------|
| [#] | [Key phrases verbatim or close paraphrase] | ⚑ EVADE | ⚑ CONTRA @P14:L6 | ⚑ NEW FACT | ⚑ SJ | ⚑ TRIAL | ⚑ SETTLE | ⚑ OBJ |
```

**Flag codes for real-time use**:

- `⚑ EVADE` — Witness appeared to evade or redirect; follow up immediately or mark for later
- `⚑ CONTRA` — Answer contradicts a prior statement; note cite for commit-credit-confront
- `⚑ NEW` — New fact, document, or witness identified; note for follow-up investigation
- `⚑ SJ` — Admission supports a summary judgment motion; extract for brief
- `⚑ TRIAL` — Answer valuable for trial testimony or impeachment
- `⚑ SETTLE` — Admission affects settlement valuation
- `⚑ OBJ` — Objection raised by opponent; note for motion practice assessment

**Deposition timeline tracker** (update every 30 minutes):

```
Topic 1: [Name]  Start: ____  End: ____  Status: COMPLETE / PARTIAL / CARRY OVER
Topic 2: [Name]  Start: ____  End: ____  Status: COMPLETE / PARTIAL / CARRY OVER
[...]
Remaining time: ____   Remaining topics: ____   Adjustment needed: YES / NO
```

---

## Post-Deposition Summary Workflow

Complete this workflow within 72 hours of the deposition.

### Step 1: Key Admissions Extraction

```markdown
# Key Admissions — [Witness Name] — [Date]

## Element: [Legal element supported]

- **Admission**: [Exact quote or close paraphrase]
- **Transcript cite**: [Page:Line]
- **Strategic value**: [Summary judgment support / Trial impeachment / Settlement leverage]

[Repeat for each material admission]
```

### Step 2: Impeachment Opportunities Documented

```markdown
# Impeachment Record — [Witness Name]

| Topic   | Prior Statement + Cite       | Deposition Testimony + Cite | Inconsistency Level                  | Trial Use              |
| ------- | ---------------------------- | --------------------------- | ------------------------------------ | ---------------------- |
| [Topic] | [Prior statement and source] | [Dep. testimony and cite]   | DISPOSITIVE / SIGNIFICANT / MODERATE | YES / NO / CONDITIONAL |
```

### Step 3: Follow-Up Needs Assessment

**⟁ CLARIFY** — After reviewing the transcript, assess:

- Are there topics the witness was unprepared or evasive on that warrant a second deposition session?
- Did the witness identify new documents or custodians requiring additional investigation?
- Do any admissions suggest follow-up discovery would improve the motion record?
- Do any errata sheet changes require challenge?

### Step 4: Errata Sheet Strategy (FRCP 30(e))

If the witness makes corrections to the transcript:

- Review all corrections for substantive vs. typographical character
- Note the applicable circuit's rule on permissible errata sheet changes [VERIFY: circuit split exists]
- If substantive changes contradict deposition testimony, consider motion to strike or to reopen deposition
- At trial, use the original transcript alongside the errata sheet to highlight the change

### Step 5: Motion Integration Map

| Admission        | Transcript Cite | Target Motion                    | Element Supported                    |
| ---------------- | --------------- | -------------------------------- | ------------------------------------ |
| [Admission text] | [Page:Line]     | [SJ motion, Daubert motion, MIL] | [Legal element or evidentiary basis] |

### Step 6: Case Timeline Update

Update the case timeline with dates, facts, and witness identifications established at the
deposition. Flag any timeline contradictions created by the testimony that require follow-up.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred)**:

- In Step 3, pull current text of FRCP 30–32, FRE 608–609, 613, 701–705, 801–807, 901–902
- Search for key cases: speaking objection sanctions, 30(b)(6) preparation obligations,
  Daubert methodology standards, errata sheet circuit split, mid-deposition consultation rules
- Verify ethics opinions on witness preparation boundaries
- Save results to `/tmp/legalcode-deposition-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp**:

- Mark all FRCP, FRE, and case law references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Focus preparation on structural quality (outline design, impeachment sequencing, objection
  classification) rather than verified legal citation depth
- Include a prominent notice that all procedural and evidentiary rules require independent
  verification before reliance

---

## Output Format Template

Structure the final deposition preparation package as:

```markdown
# Deposition Preparation Package — [Witness Name / Matter]

**Witness**: [Full name, title, organizational role]
**Deposition Type**: [Rule 30(b)(6) / Expert-Opposing / Expert-Friendly / Adverse / Friendly]
**Side**: [Propounding / Defending]
**Case**: [Matter name and docket number]
**Governing Rules**: [FRCP 30-32 / State rules]
**Date Prepared**: [date]
**Prepared by**: AI-assisted (legalcode-deposition-preparation) — requires counsel review

---

## Executive Strategy

**Primary objective**: [Summary judgment support / Trial impeachment / Settlement leverage / Other]
**Top 3 deposition topics**: [List with GREEN/YELLOW classification]
**Critical constraints**: [Seven-hour limit, deposition count, outstanding privilege disputes]
**Top impeachment opportunities**: [2-3 strongest areas by name]
**Overall witness credibility risk**: [STRONG / NEEDS WORK / VULNERABLE / CRITICAL]

---

## Rule 30(b)(6) Notice Analysis (if applicable)

**Notice adequacy**: [ADEQUATE / DEFICIENT — explain]
**Meet-and-confer status**: [Completed / Scheduled / Not yet completed — required]
**Recommended topic modifications**: [If any]

---

## Topic Prioritization Matrix

| Topic     | Classification | Legal Element | Unique Witness Knowledge | Est. Time | Impeachment Available |
| --------- | -------------- | ------------- | ------------------------ | --------- | --------------------- |
| [Topic 1] | GREEN          | [Element]     | YES / NO                 | [X min]   | YES / NO              |
| [Topic 2] | YELLOW         | [Element]     | YES / NO                 | [X min]   | YES / NO              |
| [Topic 3] | RED — deferred | [Element]     | NO                       | —         | NO                    |

---

## Deposition Outline by Topic

### Topic 1: [Name] — GREEN — Est. [X] min

**Objective**: [What to establish or pin down]
**Legal element**: [Which claim or defense this supports]

**Q1**: [Question text]

- Expected answer: [Expected response]
- If evasive: [Follow-up question]
- Exhibit: [Exhibit # if applicable]
- Confidence: [High / Probable / Possible]
- Objection risk: [PROBABLE — Form: Vague] — Counter: [Rephrase as: ...]

[Repeat for each question]

[Repeat for each topic]

---

## Exhibit List with Foundation Matrix

| #   | Exhibit | Bates/ID | Foundation Required | Foundation Witness | Auth Method | Risk         | Q # |
| --- | ------- | -------- | ------------------- | ------------------ | ----------- | ------------ | --- |
| 1   | [Doc]   | [ID]     | [Foundation]        | [Witness]          | [Method]    | LOW/MED/HIGH | Q#  |

---

## Impeachment Map

| #   | Source           | Topic   | Prior Statement   | Expected Position  | Strength    | Commit → Credit → Confront |
| --- | ---------------- | ------- | ----------------- | ------------------ | ----------- | -------------------------- |
| 1   | [Trans. P47:L12] | [Topic] | [Prior statement] | [Current position] | DISPOSITIVE | [Step sequence]            |

---

## Objection Anticipation Guide

| Topic / Q # | Objection Type | Confidence | Counter-Position  | Fallback Question  |
| ----------- | -------------- | ---------- | ----------------- | ------------------ |
| [Q5]        | Form — Vague   | HIGH       | [Reframe as: ...] | [Narrower version] |

---

## Witness Credibility Assessment

| Dimension                 | Status                                  | Confidence | Notes            |
| ------------------------- | --------------------------------------- | ---------- | ---------------- |
| Internal Consistency      | [STRONG/NEEDS WORK/VULNERABLE/CRITICAL] | [Level]    | [Specific basis] |
| Subject-Matter Knowledge  |                                         |            |                  |
| Memory Quality            |                                         |            |                  |
| Bias Indicators           |                                         |            |                  |
| Motive to Lie             |                                         |            |                  |
| Demeanor (Anticipated)    |                                         |            |                  |
| Perception Reliability    |                                         |            |                  |
| Expert Opinion Foundation |                                         |            |                  |
| Prior Testimony Record    |                                         |            |                  |
| Impeachment Exposure      |                                         |            |                  |

**Overall witness risk**: [Summary assessment]

---

## Real-Time Note-Taking Template

[Attach blank three-column template per Real-Time Deposition Note-Taking Template section]

---

## Post-Deposition Workflow Checklist

- [ ] Key admissions extracted within 72 hours
- [ ] Impeachment record documented
- [ ] Follow-up needs assessed
- [ ] Errata sheet strategy prepared (if witness reviews transcript)
- [ ] Motion integration map completed
- [ ] Case timeline updated with facts and identifications established

---

## Glass Box Audit Trail

[YAML block per Glass Box Audit Trail section]
```

---

## Localization Notes

When adapting this skill for a specific jurisdiction or state:

### US State Court Variants

[JURISDICTION-SPECIFIC] **California (CCP § 2025)**:

- Depositions are subject to a one-per-witness-per-case rule absent stipulation or court
  order [VERIFY: CCP § 2025.610]
- No independent meet-and-confer requirement before the 30(b)(6) equivalent under CCP §
  2025.230 [VERIFY]
- Seven-hour federal limit does not automatically apply; courts may impose limits [VERIFY]
- Errata sheet: California permits substantive changes under CCP § 2025.520 [VERIFY]

[JURISDICTION-SPECIFIC] **New York (CPLR Part 31)**:

- No numerical deposition limit per party without court order
- No explicit time limit per deposition session; court may impose
- Note-of-issue timing affects deposition scheduling [VERIFY]

[JURISDICTION-SPECIFIC] **Texas (TRCP 199)**:

- Depositions by oral examination require "reasonable" notice
- No per-session time limit in civil cases without court order [VERIFY: TRCP 199.5(c)]
- Expert depositions must be taken before the discovery deadline [VERIFY]

### International Context

[JURISDICTION-SPECIFIC] For depositions involving witnesses located abroad:

- Hague Evidence Convention procedures may be required for compelled depositions
- GDPR and UK GDPR constrain cross-border transfer of deposition transcripts containing
  personal data [VERIFY applicable transfer mechanism]
- Voluntary depositions abroad may proceed under the laws of the host country without
  Hague Convention procedures — this is jurisdiction-specific [VERIFY]
- UK: Depositions under CPR Part 34 are rare; witness statements are the functional
  equivalent; examine separately if needed [VERIFY]

### Localization Checklist

When creating a jurisdiction-specific variant:

- [ ] Replace [JURISDICTION-SPECIFIC] markers with verified local procedural rules
- [ ] Replace [VERIFY] tags with confirmed citations from authoritative sources
- [ ] Add state-specific deposition limits, time limits, and sequencing rules
- [ ] Add applicable local court rules and judge standing orders
- [ ] Update the frontmatter name to reference the specific jurisdiction
- [ ] Add jurisdiction-specific anti-patterns (e.g., California's unique expert deposition rules)

---

## Provenance

Created by Legalcode (2026-03-01). Original synthesis drawing on US federal civil procedure
(FRCP 30–32), Federal Rules of Evidence (FRE 608–609, 613, 701–705, 801–807, 901–902),
ABA Model Rules of Professional Conduct (3.3, 3.4, 8.4), _Daubert v. Merrell Dow
Pharmaceuticals, Inc._, 509 U.S. 579 (1993) [VERIFY], and litigation practice resources.
Structurally informed by the patterns of `legalcode-discovery-request-drafter` (topic
prioritization and objection anticipation), `legalcode-brief-analyzer` (dimension-based
quality assessment and priority matrices), and `legalcode-privilege-review` (categorical
classification frameworks). All rule and case law citations require verification against
current authoritative sources before reliance.
