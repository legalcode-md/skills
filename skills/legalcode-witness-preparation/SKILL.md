---
name: legalcode-witness-preparation
description: Prepare lay witnesses and corporate designees for deposition and trial testimony in US civil
  litigation. Use when you need to prepare any non-expert witness for deposition, trial, arbitration,
  or administrative proceeding; when reviewing prior testimony for inconsistencies before cross-examination
  exposure; when assessing a witness's readiness across credibility dimensions; or when building a multi-session
  preparation timeline.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Prepare lay witnesses and corporate designees for deposition and trial testimony in US civil litigation. Generates structured preparation packages covering anticipated direct and cross-examination questions, exhibit familiarity sessions, prior statement reconciliation, rules-of-the-road orientation, demeanor and conduct coaching, objection protocol instructions, deposition-vs-trial distinctions, and redirect rehabilitation planning. Covers all witness types: first-time lay witnesses, fact witnesses with prior testimony history, corporate Rule 30(b)(6) designees, former employees, and hostile/reluctant witnesses. Produces per-topic preparation cards, a witness readiness score, a mock examination plan, and a logistics checklist. Use when you need to prepare any non-expert witness for deposition, trial, arbitration, or administrative proceeding; when reviewing prior testimony for inconsistencies before cross-examination exposure; when assessing a witness's readiness across credibility dimensions; or when building a multi-session preparation timeline. Calibrated to US federal practice (FRCP 30/32, FRE 612/613/801) with [JURISDICTION-SPECIFIC] markers for state-court variants. Triggers on: "witness prep", "prepare witness", "witness preparation", "depose our witness", "30(b)(6) prep", "corporate designee preparation", "trial witness prep", "witness coaching", "prep for deposition", "prepare for cross-examination", "prior statement review", "witness demeanor", "redirect rehabilitation", or any task involving preparing a non-expert witness to testify.


# Legalcode Witness Preparation

> **Disclaimer**: This skill provides a framework for AI-assisted witness preparation. It
> does not constitute legal advice. All outputs must be reviewed by qualified litigation
> counsel licensed in the relevant jurisdiction before use. Federal rules, local rules,
> and standing orders vary by court and judge; verify current applicability before relying
> on any guidance here. Statutory, case law, and ethics-rule references cited from memory
> carry hallucination risk — verify against authoritative sources before relying on them.
> Witness preparation has significant ethical, strategic, and professional-responsibility
> dimensions that require experienced litigation counsel judgment. No document generated
> by this skill should be shared with the witness without attorney review.

---

## Purpose and Scope

This skill prepares lay and corporate witnesses for testimony in US civil litigation. It
spans the full preparation arc: initial assessment, document review, prior statement
reconciliation, mock examination, demeanor coaching, and final logistics preparation.

**Covers:**

- Witness type assessment and preparation strategy tailoring (lay, 30(b)(6), former
  employee, hostile)
- Initial witness interview protocol and baseline recollection capture
- Document and exhibit familiarity sessions — systematic review of expected exhibits
- Prior statement reconciliation — depositions, interrogatory answers, declarations,
  affidavits, social media, and informal writings
- Rules-of-the-road orientation — foundational session content for witnesses approaching
  testimony for the first time
- Anticipated direct examination question mapping and coaching
- Anticipated cross-examination question mapping with Three-C reverse engineering
  (Commit / Credit / Confront)
- Demeanor guidance and courtroom/deposition conduct coaching
- Objection protocol instruction — what witnesses must do when objections are raised
- Deposition-vs-trial distinction module — how each proceeding differs in scope, pace,
  and consequences
- Redirect rehabilitation planning — identifying and preparing explanatory content for
  anticipated cross-examination damage
- Mock examination session design and debrief protocol
- Session planning and pacing across the full preparation timeline
- Corporate Rule 30(b)(6) designee preparation — affirmative corporate preparation duty,
  topic mastery, and sanctions exposure

**Does not:**

- Prepare expert witnesses (see `legalcode-expert-witness-preparation` — covers Daubert,
  FRE 702, FRCP 26(a)(2), report compliance, and methodology attack preparation)
- Prepare witnesses for criminal proceedings, grand jury testimony, or post-conviction
  hearings
- Draft declarations, affidavits, or interrogatory answers
- Cover international deposition procedures in full depth (Hague Evidence Convention,
  letters rogatory, GDPR transcript transfer constraints)
- Constitute an opinion on any ethics question specific to the preparer's bar membership
- Replace the strategic judgment of experienced trial counsel

**Related skills:** `legalcode-deposition-preparation` (attorney-side deposition outlines,
question sequences, impeachment mapping), `legalcode-expert-witness-preparation` (expert
qualification, Daubert, FRE 702, FRCP 26 compliance), `legalcode-evidence-admissibility-analysis`
(FRE admissibility screening), `legalcode-early-case-assessment` (overall case strategy),
`legalcode-litigation-risk-assessment` (case risk framework), `legalcode-deposition-digest`
(summarizing prior testimony transcripts)

---

## Jurisdiction and Governing Law

This is a **US federal-primary skill** calibrated to the **Federal Rules of Civil
Procedure (FRCP)** and the **Federal Rules of Evidence (FRE)**. It applies directly to
federal district court proceedings and to state courts that follow substantially similar
rules.

**Key federal authorities:**

- FRCP Rule 30 — depositions by oral examination; Rule 30(b)(6) corporate designee
  obligations and preparation duties
- FRCP Rule 26(b)(3) — work-product doctrine; preparation sessions and attorney notes are
  generally protected, but the existence and number of sessions may be discoverable
- FRCP Rule 37 — sanctions for failure to comply with discovery, including inadequate
  30(b)(6) preparation (adverse inferences, compelled redesignation, attorney's fees)
- FRE 612 — writings used to refresh recollection; documents shown to a witness during
  preparation may be subject to production demands by opposing counsel [VERIFY]
- FRE 613 — prior inconsistent statements; mechanism for impeaching witnesses at trial
  with prior deposition testimony or interrogatory answers
- FRE 801(d)(1)(A) — prior inconsistent statements as substantive evidence when made
  under oath at a prior proceeding
- FRE 803(5) — recorded recollection; relevance to limitations on document use during
  live testimony
- ABA Model Rule 3.4(b) — prohibition on assisting or suborning false testimony; the
  ethics floor for all witness preparation
- ABA Formal Opinion 508 (2023) — definitive guidance on the ethics of witness
  preparation, including remote proceeding constraints

[JURISDICTION-SPECIFIC] When operating in a specific state, verify:

- State rules of civil procedure governing depositions (many track FRCP 30 but differ on
  time limits, objection protocol, and party attendance rights)
- State ethics rules on witness preparation (most adopt Model Rule 3.4(b) substantially
  verbatim; some jurisdictions have supplementary bar opinions — consult applicable state
  bar authority) [VERIFY]
- State-specific 30(b)(6) equivalents (most states have substantially equivalent corporate
  designee rules) [VERIFY]
- Local rules and standing orders governing remote depositions and counsel conduct during
  proceedings [VERIFY]
- FRE 612 production obligations — state evidentiary equivalents vary [VERIFY]

---

## Ethics and Preparation Boundaries

**This section must be reviewed and understood before any preparation session begins.**

Witness preparation is affirmatively required by the duty of competence (ABA Model Rule
1.1). Failure to adequately prepare a witness can itself constitute a competence violation.
The question is not _whether_ to prepare witnesses, but _how far_ preparation may go.

**ABA Formal Opinion 508 (2023)** — the governing guidance — draws the operative line:

### Permitted

- Explaining the purpose, procedure, and setting of a deposition or trial
- Advising the witness they are under oath and must testify truthfully
- Advising that "I do not recall" is an acceptable and complete answer where genuinely true
- Reviewing documents, exhibits, and prior statements with the witness
- Refreshing recollection (with awareness of FRE 612 production risk)
- Discussing probable and anticipated lines of examination
- Advising on attire, demeanor, composure, and communication style
- Suggesting clearer word choices for accuracy and clarity — not to replace recollection
- Conducting mock examinations using anticipated questions
- Instructing the witness on how objections work and how to respond to them

### Prohibited

- Scripting testimony so thoroughly that it supplants the witness's own recollection
- Instructing or suggesting that "the less you recall the better"
- Directing witnesses to minimize or downplay the number of preparation sessions with
  counsel if asked in examination [VERIFY against applicable jurisdiction]
- Using suggestive objections ("Objection, counsel is leading, and of course she never
  said that") to signal witnesses during proceedings — violates FRCP 30(c)(2) and ABA
  Model Rule 3.4(c)
- Texting, messaging, or otherwise communicating with a witness mid-proceeding, including
  during remote depositions — explicitly addressed in ABA Formal Opinion 508 as prohibited
- Directing omission of material facts
- Counseling a witness to testify falsely, including by omission

**Core principle — extract, don't inject:** Begin every preparation session with a
narrative-first approach. Let the witness recount events in their own words without
prompting, before document review or directed questioning begins. This preserves the
authenticity of the witness's recollection and documents that the attorney elicited rather
than installed the narrative.

**⟁ CLARIFY** — If this is a preparation session for a witness who has already been
deposed, inform the attorney that the prior deposition transcript must be reviewed before
any preparation session begins, to avoid inadvertently reinforcing inconsistencies. Ask
whether the prior transcript has been collected and reviewed.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would change the preparation strategy or the topics to emphasize
- The witness type determines which preparation module to activate
- Missing documents or prior statements create a material gap in preparation
- Risk tolerance or case strategy affects how aggressively to prepare certain topics

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

Accept case and witness materials in any of these formats:

- **Witness name and role** (minimum required input)
- **Case summary or complaint** — the factual allegations and claims at issue
- **Prior testimony transcripts** — deposition transcripts, prior trial testimony
- **Interrogatory answers** — the party's responses to interrogatories
- **Declarations and affidavits** — prior sworn statements
- **Document set** — exhibits likely to be shown; produced documents the witness authored
  or received
- **30(b)(6) notice** — if preparing a corporate designee, the notice of topics is the
  preparation roadmap
- **Case theory memo** — counsel's theory of the case for the client
- **Opposing party's pleadings or expert reports** — signals anticipated cross themes

If no case context is provided, prompt the user to supply at minimum: witness name, role
in the case (plaintiff, defendant, third party), and the general subject matter of the
litigation.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user these questions. Skip questions already
answered by the input materials:

1. **Witness type:**
   - Options: Lay fact witness (party), Lay fact witness (non-party), Corporate Rule
     30(b)(6) designee, Former employee, Hostile/adverse witness (compelled to testify),
     Treating professional (non-expert opinion)
   - _Why this matters_: Each witness type requires a fundamentally different preparation
     architecture. A 30(b)(6) designee must master topics beyond personal knowledge; a
     hostile witness requires different pacing and trust-building.

2. **Proceeding type:**
   - Options: Deposition only, Trial only, Both (deposition first, then trial), Arbitration
     hearing, Administrative proceeding
   - _Why this matters_: Deposition prep emphasizes brevity and avoiding commitment; trial
     prep emphasizes persuasion and narrative. The preparation session design differs
     materially.

3. **Available preparation time:**
   - Options: Single session (1–2 hours, emergency), Two or three sessions (standard),
     Full preparation timeline (1 week or more)
   - _Why this matters_: Session depth and topic prioritization change substantially with
     available time.

4. **Prior testimony history:**
   - Options: No prior testimony (first-time witness), Prior deposition in this matter,
     Prior deposition in a related matter, Prior trial testimony, Prior testimony in an
     unrelated matter that may surface on cross
   - _Why this matters_: Prior testimony creates impeachment exposure and must be
     reconciled before any mock examination.

5. **Key themes of anticipated cross-examination:**
   - Free text. Examples: bias/motive, prior inconsistent statements, knowledge gaps,
     document-specific attacks, credibility impeachment (FRE 608–609 [VERIFY]).
   - _Why this matters_: Informs which preparation topics to treat as CORE vs. TARGET vs.
     FLEXIBLE.

If the user provides partial context, proceed with what is available but state assumptions
explicitly before delivering output.

### Step 3: Load Legal Authority

Use **legalcode-mcp** to gather the jurisdiction-relevant legal authority for this witness
and proceeding.

**Search for:**

- The court's local rules governing deposition conduct, objection protocol, and remote
  deposition requirements
- Any standing orders from the assigned judge that affect witness examination
- Current state-court witness preparation ethics authority if the proceeding is in state
  court [JURISDICTION-SPECIFIC]
- FRE 612 production obligation current application in the circuit [VERIFY]
- Any recent amendments to FRCP Rule 30 affecting the specific deposition context [VERIFY]

**If legalcode-mcp is not connected:**

- Mark all rule and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed using general federal authority but flag that local rules and standing orders
  have not been verified

### Step 4: Assess Witness Type and Activate Modules

Based on the context gathered in Step 2, activate the preparation modules applicable to
this witness. Not every module applies to every witness.

| Module                           |   Lay Fact Witness   | 30(b)(6) Designee | Former Employee | Hostile Witness |
| -------------------------------- | :------------------: | :---------------: | :-------------: | :-------------: |
| Rules-of-the-road orientation    |       Required       |     Required      |    Required     |    Required     |
| Personal recollection capture    |       Required       |     Required      |    Required     |     Limited     |
| Document and exhibit review      |       Standard       |     Enhanced      |    Standard     |    Targeted     |
| Prior statement reconciliation   | If prior stmts exist |     Required      |    Required     |    Required     |
| 30(b)(6) topic mastery module    |          —           |     Required      |        —        |        —        |
| Direct examination prep          |       Required       |     Required      |    Required     |        —        |
| Cross-examination prep           |       Required       |     Required      |    Required     |     Limited     |
| Redirect rehabilitation planning |       Standard       |     Standard      |    Standard     |    Standard     |
| Demeanor coaching                |       Required       |     Required      |    Required     |    Adaptive     |
| Logistics prep                   |       Required       |     Required      |    Required     |    Required     |

**⟁ CLARIFY** — For a 30(b)(6) designee, ask:

- Has the 30(b)(6) notice been received? If yes, provide it — the noticed topics define
  the preparation roadmap.
- Has the organization determined which designee(s) will cover which topics? If multiple
  designees are planned, this skill produces separate preparation packages per designee.
- Has the organization begun document collection on the noticed topics?

### Step 5: Initial Witness Assessment and Recollection Capture

Begin every preparation engagement with a **narrative-first session** before any document
review or directed questioning.

**Purpose:** Establish the witness's unprimed recollection as a baseline before introducing
documents. This both protects against claims that the attorney installed a narrative and
provides a map of memory gaps that preparation must address.

**Protocol:**

1. Open with an unstructured prompt: "Tell me, in your own words, what you know about
   [the relevant events/subject matter]. Start wherever feels right and don't worry about
   order."
2. Do not interrupt. Take notes without asking clarifying questions during the narrative.
3. After the narrative completes, ask only clarifying questions: "You mentioned X — can
   you tell me more about that?" Avoid leading questions at this stage.
4. Document what the witness does and does not remember before document review begins.
5. Note the witness's baseline: vocabulary, comfort under questioning, response length
   tendencies, and stress responses (hedging, fidgeting, speed changes).

**Witness Baseline Assessment — score each dimension:**

| Dimension                  | STRONG                        | NEEDS WORK                                | VULNERABLE                        | CRITICAL                                  |
| -------------------------- | ----------------------------- | ----------------------------------------- | --------------------------------- | ----------------------------------------- |
| Memory specificity         | Clear, detailed, consistent   | Some gaps, but coherent                   | Key gaps on central events        | Contradicts documents or prior statements |
| Response length discipline | Concise, answers the question | Mildly over-explains                      | Frequently volunteers information | Narrates extensively, repeats             |
| Composure under pressure   | Calm and measured             | Mild stress signals                       | Visible anxiety or defensiveness  | Combative or collapses under challenge    |
| Credibility markers        | Specific, corroborated recall | Generally credible, minor inconsistencies | Notable inconsistencies surfaced  | Material inconsistencies with record      |
| Vocabulary and clarity     | Clear, precise language       | Some jargon or confusion                  | Communication gaps                | Easily misunderstood or mischaracterized  |
| Document familiarity       | Comfortable with exhibits     | Recognizes key docs                       | Limited document recall           | Does not recognize key authored documents |

**Score each dimension** (STRONG = 3, NEEDS WORK = 2, VULNERABLE = 1, CRITICAL = 0).
**Aggregate score (0–18):**

- **15–18**: READY — proceed to mock examination with moderate prep time
- **10–14**: NEEDS WORK — focused remediation on VULNERABLE/CRITICAL dimensions required
- **5–9**: SIGNIFICANT WORK — multiple sessions needed; prioritize CRITICAL items first
- **0–4**: NOT READY — fundamental preparation deficits; escalate preparation timeline

### Step 6: Document and Exhibit Review

After the narrative-first session, conduct a systematic exhibit review.

**Organization:** Sort documents into three categories before the session:

| Category                             | Contents                                                                                                                 | Purpose                                                           |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| **A — Key exhibits**                 | Documents the witness authored, received, or signed; documents central to the case theory                                | Ensure witness can identify, authenticate, and contextualize each |
| **B — Cross-examination ammunition** | Documents opposing counsel will likely use for impeachment; documents inconsistent with the witness's expected testimony | Prepare the witness to handle each without being ambushed         |
| **C — Corroborating materials**      | Documents that support the witness's testimony; documents helpful to the client's theory                                 | Strengthen the witness's recall and confidence                    |

**Review process per document:**

1. Show the witness the document without labeling it. Ask: "Have you seen this before?"
2. Let the witness review independently before asking any questions.
3. Ask: "What is this document? What does it mean? What was happening at the time?"
4. For Category B documents: "Opposing counsel may show you this. What would you say
   about it?" — Prepare the witness to respond honestly and contextually, not defensively.

**FRE 612 warning:** [VERIFY] Documents shown to a witness to refresh recollection during
preparation may be subject to opposing counsel's demand for production at deposition or
trial. Consult the applicable circuit's interpretation of FRE 612 before selecting
preparation documents. The risk is most acute for documents not otherwise produced.

**⟁ CLARIFY** — If the document set is incomplete (e.g., no exhibit list has been shared,
or the witness authored documents not yet collected), ask the user to identify the
documents most likely to be used on cross-examination before proceeding to mock
examination. An ambush at mock examination is manageable; an ambush at deposition is not.

### Step 7: Prior Statement Reconciliation

Collect every prior sworn or documented statement the witness has made that is potentially
discoverable or usable at the proceedings. Review these before any mock examination.

**Prior statement inventory:**

| Source                                | Significance                                                                      | Impeachment Use |
| ------------------------------------- | --------------------------------------------------------------------------------- | --------------- |
| Prior deposition in this matter       | Binding record; any inconsistency usable at trial under FRE 801(d)(1)(A) [VERIFY] | HIGH            |
| Prior deposition in a related matter  | May be admissible; signals established positions                                  | HIGH            |
| Interrogatory answers (party witness) | Binding on the party; witness should not casually contradict                      | HIGH            |
| Declarations and affidavits           | Sworn statements; FRE 801(d)(1)(A) if under oath; FRE 613 otherwise [VERIFY]      | HIGH            |
| Prior trial testimony                 | Permanent sworn record                                                            | HIGH            |
| Informal written statements           | Emails, letters, reports authored by the witness                                  | MEDIUM          |
| Social media posts                    | Public statements; no privilege; may be authenticated through metadata            | MEDIUM          |
| Text messages and chat logs           | Informal; may contain admissions                                                  | MEDIUM          |
| Prior testimony in unrelated matters  | If related to credibility, bias, or relevant facts                                | VARIES          |

**Reconciliation protocol:**

1. Read each prior statement against the witness's current expected testimony.
2. Identify every material inconsistency. Classify each:
   - **Explainable inconsistency**: Memory change with an honest explanation (time elapsed,
     different context of questioning). Prepare the witness to acknowledge and explain.
   - **Apparent inconsistency**: The statements are not actually inconsistent but can be
     made to appear so through selective quotation. Prepare the witness to provide
     context and expose the false implication.
   - **True inconsistency**: The prior statement is incorrect or the current position has
     changed. Prepare the witness to acknowledge the prior statement, explain the
     discrepancy, and affirm the current accurate position. Do NOT prepare the witness
     to deny or minimize the prior statement.
3. Walk the witness through each identified inconsistency explicitly before mock
   examination. An unplanned encounter with a damaging prior statement at deposition
   is one of the highest-risk preparation failures.

**⟁ CLARIFY** — If any true inconsistency involves a prior sworn statement that the
witness now believes was inaccurate, alert counsel immediately. The attorney has ethical
obligations (ABA Model Rule 3.3) regarding known false testimony. This requires legal
judgment beyond this skill's scope.

### Step 8: Rules-of-the-Road Orientation

Every witness — regardless of experience level — must receive a foundational orientation
before any examination practice begins. This session establishes the basic rules that
govern all testimony.

**Core rules to deliver to every witness:**

**On answering questions:**

1. Listen to the complete question before answering. Do not anticipate where the question
   is going and answer before it finishes.
2. Answer the question that was asked — not the question you wish had been asked.
3. Answer briefly. A complete, honest, brief answer is always better than a complete,
   honest, long answer. Long answers provide follow-up ammunition.
4. If you do not understand a question, say so: "I don't understand the question — could
   you rephrase it?" You are entitled to understand what you are being asked.
5. If you do not know the answer, say "I don't know." This is a complete answer.
6. If you do not recall, say "I don't recall" or "I don't remember." This is a complete
   answer. Never guess or speculate to fill a memory gap.
7. Do not volunteer information beyond the specific question asked. Wait for the next
   question.
8. Silence after you have finished answering is not your problem. Stop talking when you
   have answered.

**On documents:** 9. When you are shown a document, take time to read it completely before responding to
any question about it. You are entitled to read the full document. 10. Confirm that you have read it: "I've read it." 11. If you do not recognize a document, say so: "I don't recognize this document." You
are not required to identify every document placed in front of you.

**On objections:** 12. When your attorney objects, stop speaking immediately. Wait. 13. If the judge says "overruled" — answer the question that was asked, and only that question. 14. If the judge says "sustained" — do not answer. Wait for the next question. 15. At depositions: most objections do not prevent you from answering. After your attorney
objects and states the basis, you will typically still be asked to answer unless
privilege is invoked. Wait for the attorney to finish objecting and then answer
unless instructed otherwise. 16. Do not ask your attorney whether to answer a question. Do not look to them for cues.

**On demeanor:** 17. Tell the truth. Always. Your attorney can deal with difficult truths. They cannot deal
with a witness who lies. 18. Do not argue with examining counsel. Do not be sarcastic, combative, or dismissive. 19. Maintain composure regardless of the tone of questioning. An aggressive questioner is
trying to provoke a reaction — deny them one.

**Deposition-specific rules:** 20. Every word you say is being recorded. The transcript is permanent. What you say today
can and will be used at trial. 21. Breaks: you may request a break at any time. You may not request a break while a
question is pending — answer the question first, then request the break. 22. Conferring with counsel during breaks: you may confer with your attorney during breaks
unless a question is pending. Do not confer during pending questions.
[JURISDICTION-SPECIFIC] Some courts limit counsel-witness conferences during
depositions; verify applicable local rules [VERIFY]. 23. Remote depositions: do not communicate with anyone — by text, chat, email, or any
other channel — while the deposition is ongoing. ABA Formal Opinion 508 (2023)
addresses this explicitly. Unauthorized communications are sanctionable.

### Step 9: Direct Examination Preparation

Prepare the witness for expected questions on direct examination.

**Structure the direct as a narrative arc:**

1. Identify the 3–5 core factual points the witness must convey. These are non-negotiable
   anchor points that every preparation session must reinforce.
2. Organize anticipated direct questions chronologically or topically — whichever presents
   the witness's account most clearly.
3. Conduct at least one full mock direct examination. Debrief: Did the witness convey the
   core points? Were there gaps? Was the narrative coherent?
4. Coach the witness to use their own language, not counsel's. Scripted answers sound
   scripted. The goal is that the witness can tell the story naturally because they have
   thought it through, not because they have memorized a script.

**Direct examination preparation cards — one per topic area:**

```
Topic Area: [subject]
Readiness Level: STRONG / NEEDS WORK / VULNERABLE / CRITICAL
Core Point: [the essential fact this topic must establish]
Anticipated Question: [representative question]
Prepared Answer Framework: [key points the answer should address, in the witness's own words]
Supporting Exhibits: [key documents that corroborate this testimony]
Risk: [what opposing counsel will try to do with this topic on cross]
Redirect Opportunity: [if cross attacks this, the witness can reclaim the narrative by ___]
```

### Step 10: Cross-Examination Preparation

Prepare the witness to handle hostile, leading, and impeachment-driven questioning.

**The Three-C Cross-Examination Sequence (Commit / Credit / Confront):**

Opposing counsel will frequently run this sequence against cooperative-seeming facts:

1. **Commit**: Get the witness to commit to a favorable-to-the-examiner version of a fact
   ("You would agree that [X] is true, wouldn't you?")
2. **Credit**: Get the witness to agree that a document or prior statement is accurate
   ("And you wrote this email yourself, didn't you?")
3. **Confront**: Use the committed-to statement and the credited document to establish
   the impeaching conclusion ("So when you wrote [X], you understood [damaging
   conclusion], isn't that right?")

**Preparation objective:** Teach witnesses to recognize this sequence in real time and
respond with discipline. The weapon against the Three-C sequence is not argument —
it is refusing to over-commit in Step 1. A witness who gives accurate, appropriately
qualified answers on Step 1 gives opposing counsel nothing to exploit in Step 3.

**Cross-examination coaching principles:**

- Brevity is protection. A short accurate answer cannot be expanded into a damaging
  admission. A long answer almost always can.
- "Isn't it true that..." questions often embed assumptions or mischaracterizations. The
  witness's job is to answer the accurate part and correct the embedded error — not simply
  say yes because part of the compound is true.
- "Yes or no" demands on questions that require nuance: the witness may say "I can't
  answer that accurately with just yes or no."
- Silence after a complete answer is the examiner's problem, not the witness's. Teach
  witnesses to stop talking when they have answered.
- Do not anticipate where a line of questioning is going and try to get ahead of it.
  Answer each question individually.

**Mock cross-examination protocol:**

1. Build a mock cross outline based on opposing counsel's known case theory, identified
   impeachment areas, and anticipated document confrontations.
2. Conduct the mock cross without warning — simulate the surprise of real examination.
3. Use genuine adversarial pressure and tone (after warning the witness this will be
   the difficult part of preparation). Witnesses who have never been pressed collapse
   more severely under real cross than witnesses who have experienced simulated hostility.
4. Debrief immediately after: note VULNERABLE and CRITICAL dimension responses.
5. Conduct a second, shorter mock cross on the problem areas before the proceeding.

**⟁ CLARIFY** — For witnesses with extensive prior statement exposure (prior depos,
interrogatory answers, prior trial testimony), ask whether to run a targeted
impeachment-simulation session focused exclusively on the most damaging prior statements.
This is separate from the general mock cross and may require additional session time.

### Step 11: Redirect Rehabilitation Planning

Anticipate which cross-examination attacks are repairable on redirect and plan the
rehabilitative testimony in advance.

**Rehabilitation categories:**

| Cross Attack Type                                                  | Redirect Opportunity                                                                             | Witness Preparation                                                                                 |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| Prior inconsistent statement (true inconsistency with explanation) | Explain circumstances; if relevant, introduce explaining context under FRE 801(d)(1)(B) [VERIFY] | Prepare the witness to give the completing account when asked on redirect                           |
| Apparent inconsistency (context stripped by selective quotation)   | Read the full document or full statement                                                         | Coach the witness to offer to explain if not given the opportunity                                  |
| Bias / motive attack                                               | Counter-evidence of lack of bias; prior consistent statements                                    | Prepare the witness to acknowledge the relationship and explain why it does not affect truthfulness |
| Memory gap exploitation                                            | Explain why memory gap is genuine; prior consistent contemporaneous record                       | Walk the witness through why the gap is honest                                                      |
| Document-specific impeachment (interpretation dispute)             | Provide full context for the document; surrounding circumstances                                 | Ensure the witness understands the full documentary context before the proceeding                   |

**Anticipatory redirect technique:** Where repair is highly predictable, embed the
rehabilitative answer into direct examination before cross happens. A witness who
proactively acknowledges a limitation or prior statement on direct ("I will say that
at the time I wrote this email, I believed X, though I later learned Y") takes the
cross-examination weapon away by using it first.

### Step 12: Deposition vs. Trial Distinction Module

Every witness preparing for both deposition and trial must understand how the two
proceedings differ. Witnesses who treat depositions like trial testimony — by attempting
to persuade — create discovery problems and lock themselves into positions they may
regret at trial.

| Dimension                   | Deposition                                                                                                                   | Trial                                                                           |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Purpose**                 | Discovery for opposing party — you are helping them understand the facts                                                     | Presentation to factfinder — you are communicating your account persuasively    |
| **Audience**                | Opposing counsel; no judge or jury present (typically)                                                                       | Judge and/or jury; credibility is being evaluated at every moment               |
| **Answer goal**             | Accuracy and brevity — give the truth, no more                                                                               | Accuracy and narrative — give the truth with appropriate context                |
| **Volunteering**            | Do not volunteer — answer the specific question and stop                                                                     | May provide context within answers where it helps the factfinder understand     |
| **Real-time coaching**      | Breaks allowed; counsel may confer during breaks (not mid-question)                                                          | Counsel cannot coach during examination                                         |
| **Correction window**       | Errata sheet available within 30 days under FRCP 30(e) [VERIFY] — narrow corrections only                                    | No errata mechanism; testimony is final                                         |
| **Scope of questions**      | Broad discovery scope — questions need not be admissible, only reasonably calculated to lead to admissible evidence [VERIFY] | Relevant and admissible evidence only                                           |
| **Primacy/recency effects** | Less important — no factfinder evaluating performance                                                                        | Critical — jurors remember opening and closing most vividly                     |
| **Stakes**                  | Record creation — this transcript will be used at trial                                                                      | Outcome determination — this is the live testimony on which the verdict depends |
| **Redirect**                | Limited redirect opportunity during deposition session                                                                       | Full redirect examination available; counsel may rehabilitate                   |

**FRCP 30(e) errata sheet [VERIFY]:** A deponent may review and sign the deposition
transcript within 30 days of notification that it is ready. Changes must include a
statement of the reason for each change. Courts are divided on whether substantive
changes are permissible; some circuits severely limit the scope of errata.

### Step 13: Corporate Rule 30(b)(6) Designee Module

**Activate this module only for corporate designee witnesses.**

The 30(b)(6) designee is not an individual witness — the designee speaks for the
corporation. Testimony is binding on the entity, not merely on the individual.

**The corporate preparation obligation:**

- The corporation has an affirmative duty to prepare the designee on **all topics
  noticed in the 30(b)(6) notice** — including matters outside the designee's personal
  knowledge. The corporation must investigate and educate the designee. [VERIFY]
- Inadequate preparation is equivalent to failure to appear — courts have imposed
  sanctions including adverse inference instructions, compelled redesignation, and
  attorney's fees. [VERIFY] _Black Horse Lane Assoc. v. Dow Chemical Corp._, 228 F.3d 275
  (3d Cir. 2000) [VERIFY].
- "I don't know" is not an acceptable answer on a noticed topic. The corporation is
  expected to know. The designee must say what the corporation's position is, based on
  its investigation.

**30(b)(6) preparation workflow:**

1. **Notice analysis:** Immediately upon receipt of the 30(b)(6) notice, analyze each
   noticed topic. Map to the designee(s) most knowledgeable on each topic.
2. **Document collection:** Collect all corporate records responsive to each noticed
   topic. This is not optional — it is the evidentiary foundation for the designation.
3. **Multi-designee strategy:** Consider whether multiple designees should cover different
   topic clusters. Each designee is prepared only on their designated topics.
4. **Topic mastery sessions:** Walk through each noticed topic systematically. For each:
   - What does the corporation know? (Based on documents and investigation)
   - What is the corporation's official position?
   - What are the key documents supporting that position?
   - What are the gaps in the record on this topic?
5. **Mock examination by topic:** Conduct mock 30(b)(6) examination using the actual
   noticed topics as the examination framework. Do not compress — each topic area
   deserves its own mock session.

**30(b)(6) readiness check per topic:**

```
Topic: [noticed topic verbatim]
Designee: [name]
Documents Reviewed: [list or count]
Readiness: READY / BORDERLINE / NOT READY
Key Corporate Position: [what the corporation will say on this topic]
Residual Gaps: [what the corporation does not know and why]
Risk if Inadequate: [sanctions exposure; adverse inference risk]
```

---

## Topic Coverage Framework

Organize the preparation package around **topic areas** rather than individual questions.
Each topic area maps to a cross-examination risk level and a readiness tier.

**Topic Area Classification:**

| Tier     | Label       | Meaning                                                  | Preparation Depth                                                            |
| -------- | ----------- | -------------------------------------------------------- | ---------------------------------------------------------------------------- |
| CORE     | Must Master | Central to the case theory; heavy cross expected         | Multiple mock sessions; all prior statements reviewed; full Three-C analysis |
| TARGET   | Important   | Significant exposure; likely cross-examination focus     | One to two mock sessions; key documents reviewed                             |
| FLEXIBLE | Cover       | Background or supporting matters; lighter cross expected | Single review pass; documents confirmed                                      |

**Topic inventory template:**

```
Topic: [subject area]
Tier: CORE / TARGET / FLEXIBLE
Prior Statement Exposure: [yes/no; sources]
Document Exposure: [key exhibits on this topic]
Opposing Theory: [what opposing counsel will argue on this topic]
Readiness Level: STRONG / NEEDS WORK / VULNERABLE / CRITICAL
Readiness Score: [0–3]
Preparation Actions: [specific actions before the proceeding]
```

---

## Demeanor and Logistics Preparation

### Demeanor Coaching

Credibility is assessed on both content and delivery. Demeanor coaching is appropriate,
ethical, and necessary preparation. It is not deception — it is helping the witness
present authentically under conditions of significant stress.

**Core demeanor guidance:**

| Dimension                  | Guidance                                                                                                                      |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Eye contact**            | Make eye contact with the questioner during deposition; with the jury/judge during trial testimony                            |
| **Posture**                | Upright, facing forward; avoid crossing arms or slouching                                                                     |
| **Pause before answering** | A brief pause before answering prevents blurting, allows objections, and signals thoughtfulness — not evasion                 |
| **Pace of speech**         | Speak at a moderate, measured pace; stress accelerates speech                                                                 |
| **Tone**                   | Conversational and matter-of-fact; avoid defensive, sarcastic, or overly formal register                                      |
| **Response to aggression** | Maintain the same calm tone regardless of the examiner's intensity                                                            |
| **Physical tells**         | Identify any stress-specific behaviors (fidgeting, eye-contact avoidance, covering mouth) during mock examination and address |
| **Looking to counsel**     | Never look to counsel for answers or cues during examination — it signals evasion                                             |

**Attire:** Professional conservative attire. Attire communicates respect for the
proceeding and the factfinder. [JURISDICTION-SPECIFIC] Cultural context may affect
guidance. Defer to counsel.

### Logistics Preparation

**Day-before checklist:**

- [ ] Review the rules of the road one more time
- [ ] Review the 3–5 CORE topic area cards
- [ ] Get adequate rest — cognitive performance under pressure degrades with fatigue
- [ ] Know the location, parking, and check-in procedure
- [ ] Know who to report to on arrival; bring a contact number for counsel

**Day-of checklist:**

- [ ] Arrive 15–30 minutes early — unexpected logistics consume preparation buffer
- [ ] Do not discuss the case with anyone in the waiting area, hallways, or restrooms —
      opposing parties, counsel, or observers may be present
- [ ] Turn off or silence mobile device; do not text or communicate during any proceeding
- [ ] Water or non-caffeinated beverage is appropriate on the table
- [ ] If anxious: take a breath before answering each question — this is a physical anchor
      to the "pause before answering" rule

**Remote deposition checklist:**

- [ ] Confirm the video platform and test connection the day before
- [ ] Plain, uncluttered background; professional lighting
- [ ] No one else in the room — no visible or audible presence of others
- [ ] Phone off or in another room — no communications during the session by any channel
- [ ] Printed copy of key exhibits permitted if agreed in advance [VERIFY applicable rules]
- [ ] Advise counsel if any technical issues arise — request a break rather than proceeding
      through connection problems

---

## Readiness Assessment and Prioritization

### Overall Witness Readiness Score

After completing preparation, score the witness across all active topic areas:

| Topic Area | Tier   | Readiness                               | Score (0–3) |
| ---------- | ------ | --------------------------------------- | ----------- |
| [Topic 1]  | CORE   | [STRONG/NEEDS WORK/VULNERABLE/CRITICAL] | [0–3]       |
| [Topic 2]  | CORE   |                                         |             |
| [Topic 3]  | TARGET |                                         |             |
| ...        |        |                                         |             |
| **Total**  |        |                                         | /[max]      |

**Overall readiness:**

- All CORE topics STRONG or NEEDS WORK, no CRITICAL items → **READY**
- Any CORE topic VULNERABLE, or any CRITICAL item on any tier → **NEEDS WORK** — additional session required
- Two or more CRITICAL items → **NOT READY** — preparation timeline must be extended

### Session Prioritization

If preparation time is constrained, prioritize in this order:

1. CRITICAL items on any topic — address these first regardless of tier
2. CORE topics not yet at STRONG or NEEDS WORK
3. Prior statement reconciliation for any HIGH-risk inconsistencies
4. TARGET topics at VULNERABLE
5. Mock cross-examination on CORE topics
6. Logistics and demeanor coaching
7. FLEXIBLE topics and final logistics review

---

## Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise
before delivery.

| Gate           | Rule                                                                                                                                        | Fail Action                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every legal claim cites a specific rule, statute, ABA opinion, or established principle                                                     | Add citation or mark "[UNVERIFIED]" |
| **Format**     | All citations follow a consistent, recognizable format (FRCP rule number, FRE rule number, case citation with court and year)               | Fix format                          |
| **Currency**   | Every cited provision checked for amendments or repeal — particularly FRCP and FRE, which are amended annually                              | Flag "[CHECK CURRENCY]"             |
| **Domain**     | Analysis stays within US civil litigation scope; ethics guidance stays within ABA Model Rules unless state bar authority specifically noted | Remove or flag out-of-scope content |
| **Confidence** | Uncertainty explicitly stated; do not assert contested procedural rules as settled                                                          | Add confidence qualifier            |

---

## Self-Interrogation for CRITICAL Findings

For any topic area or witness dimension classified as CRITICAL, apply this three-pass
review before delivering the preparation package:

**Pass 1 — Accuracy:** Is the readiness classification accurate? Does the specific
evidence (prior statement, document, behavioral observation) actually establish a CRITICAL
risk — or is it VULNERABLE on closer examination?

**Pass 2 — Completeness:** Have all potential sources of impeachment on this topic been
considered? Are there documents, prior statements, or lines of examination not yet
identified that could compound the risk?

**Pass 3 — Rehabilitation:** Is this CRITICAL finding truly unrepairable, or is there a
preparation approach — document context, explanation of inconsistency, anticipatory direct
testimony — that could realistically move it to VULNERABLE or NEEDS WORK before the
proceeding?

---

## Confidence Scoring

| Level        | Range     | Meaning                                                  | Action                                                  |
| ------------ | --------- | -------------------------------------------------------- | ------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled rule or procedure; universally applied           | State with confidence                                   |
| **High**     | 0.80–0.94 | Strong authority; minor circuit/state variation possible | State with brief caveat                                 |
| **Probable** | 0.60–0.79 | Good authority; circuit split or state variation likely  | State with reasoning and note variation                 |
| **Possible** | 0.40–0.59 | Genuinely uncertain; court-by-court or judge-by-judge    | Flag for attorney review; present both sides            |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                                  | Do not assert; flag "[UNCERTAIN — verify with counsel]" |

---

## Anti-Patterns

What NOT to do in witness preparation:

1. **Starting with documents, not narrative** — Showing documents before capturing the
   witness's unprimed recollection destroys the "extract, don't inject" discipline and
   creates risk that the attorney's narrative is in the transcript rather than the
   witness's own.

2. **Single-session preparation** — One session the day before the deposition is
   inadequate for any witness with meaningful exposure. The first session surfaces
   problems; subsequent sessions address them. A single-session witness has unidentified
   CRITICAL issues the attorney has not discovered.

3. **Skipping prior statement reconciliation** — The most avoidable impeachment in civil
   litigation is by prior statements the attorney already possesses but never reviewed
   with the witness. Encountering a damaging prior deposition answer for the first time
   during cross-examination is a preparation failure, not a strategy.

4. **Over-scripting** — So thoroughly rehearsing exact answers that the witness sounds
   robotic. Opposing counsel will vary the question minimally and the witness, unable to
   deviate from the script, will pause visibly or give an answer that fits the rehearsed
   question rather than the actual one. Authenticity is destroyed.

5. **Injecting testimony** — Telling the witness what happened or what to say, rather
   than eliciting what the witness actually recalls. This is the ethics line that separates
   preparation from coaching. ABA Formal Opinion 508 (2023) addresses this directly.

6. **Coaching the witness to minimize preparation time** — Directing a witness to
   understate the number of preparation sessions with counsel is explicitly prohibited
   by ABA Formal Opinion 508 (2023). Witnesses may be asked about preparation and should
   answer honestly.

7. **Using suggestive objections as witness signals** — Speaking objections ("Objection,
   counsel is putting words in the witness's mouth — you never said that, did you?") are
   prohibited coaching signals under FRCP 30(c)(2) and ABA Model Rule 3.4(c).

8. **Omitting mock cross-examination** — Witnesses who have never been pressed under
   simulated adversarial conditions are far more likely to collapse under real cross.
   Even one practice round with genuine pressure produces materially better performance
   than none.

9. **Inadequate 30(b)(6) preparation** — Designating a witness with superficial knowledge
   of the noticed topics, providing minimal preparation, and hoping for the best. Courts
   have held inadequate 30(b)(6) preparation equivalent to failure to appear, with
   corresponding sanctions exposure. _Black Horse Lane_, 228 F.3d 275 [VERIFY].

10. **Failing to instruct on objection protocol** — Witnesses who answer over their
    attorney's objections, argue with opposing counsel about the objections, or look to
    counsel for cues after objections undermine both the attorney's professionalism and
    the witness's credibility.

11. **Remote deposition hygiene failures** — Not instructing the witness that texting,
    chat, email, or any other channel communication during the proceeding is prohibited.
    ABA Formal Opinion 508 (2023) specifically addresses real-time coaching via remote
    channels as impermissible. Sanctions have been imposed.

12. **Treating the deposition as a trial** — Instructing a witness to "tell their story"
    at a deposition produces verbose, volunteering testimony that locks the witness into
    expansive positions that are difficult to qualify at trial and provide opposing counsel
    with significant material.

13. **Demeanor-free preparation** — Focusing exclusively on factual content while
    ignoring how the witness presents physically and emotionally. Credibility assessments
    are simultaneous evaluations of content and delivery. A factually accurate witness
    who appears evasive, combative, or nervous is less credible than one who does not.

14. **Forgetting the logistics** — Witnesses who arrive at depositions uncertain of the
    location, anxious about the setting, or unclear on basic procedures underperform
    regardless of factual preparation quality. Logistics preparation is not optional.

15. **No redirect rehabilitation planning** — Conducting full mock cross-examination but
    not working through which anticipated cross-examination damage is repairable on
    redirect. Redirect is the attorney's recovery mechanism; preparing for it in advance
    is a skill.

16. **Allowing undisclosed third parties in the room during remote depositions** — The
    witness must be alone in the physical space during a remote deposition. Undisclosed
    third-party presence is a sanctionable ethics violation.

---

## Writing Standards

Apply these standards before delivering any preparation package:

- **Witness-facing content** (rules of the road, topic cards): Write in plain language the
  witness will understand without legal training. Avoid defined terms, procedural jargon,
  and citation-heavy explanations. Test each instruction: could a layperson follow it?
- **Attorney-facing content** (readiness assessment, Glass Box, CRITICAL findings):
  Write with precision. Cite specific rules, prior statements by document and date,
  and topic areas by name. Use legal terminology accurately.
- **Never mix audiences** in a single document. The preparation package has two
  components: (1) the witness's materials, and (2) the attorney's assessment. Produce
  them separately.
- Verb-first instructions in witness materials: "Listen to the complete question before
  answering" — not "The witness should ensure that..."
- Active voice throughout: "Stop talking when you have answered" — not "Talking should
  be stopped after answering."
- No hedging language in rules-of-the-road content: the witness needs clear rules, not
  probability assessments.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for local rules and standing orders for the assigned judge and court
- Verify current FRCP Rule 30 and applicable local rule text
- Search for circuit-specific FRE 612 authority governing documents used in preparation
- Search for applicable state ethics authority on witness preparation if proceeding is
  in state court [JURISDICTION-SPECIFIC]
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all rule, case law, and ethics references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Focus the preparation package on structural quality and coaching content rather than
  jurisdiction-specific legal substance
- Advise the user to independently verify all cited rules and local requirements

---

## Glass Box Audit Trail

Include this YAML block at the end of every preparation package:

```yaml
glass_box:
  skill_name: "legalcode-witness-preparation"
  witness_name: "[name — use initials or role if confidentiality required]"
  witness_type: "[Lay fact / 30(b)(6) designee / Former employee / Other]"
  proceeding_type: "[Deposition / Trial / Both / Arbitration]"
  case_summary: "[Brief description of the matter]"
  prior_statements_reviewed:
    - "[Statement type, date, source]"
    - "[...]"
  modules_activated:
    - "[list active modules]"
  topic_areas_assessed: "[number]"
  core_topics_count: "[number]"
  critical_items_found: "[number]"
  overall_readiness: "READY / NEEDS WORK / NOT READY"
  readiness_score: "[total] / [maximum]"
  legalcode_mcp: "Connected / Not connected"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  fre_612_risk_flagged: "Yes / No / N/A"
  ethics_bounds_reviewed: "Yes"
  aba_formal_opinion_508_applied: "Yes"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any materials not reviewed — missing prior transcripts, incomplete document set, etc.]"
    - "[Any preparation constraints — single session, limited time, etc.]"
  reviewer: "AI-assisted — requires qualified litigation counsel review before use"
  date: "[preparation date]"
```

---

## Output Format Template

Deliver the preparation package in two separate documents:

---

### Document 1: Witness Preparation Package (Witness Copy)

**PRIVILEGED AND CONFIDENTIAL — ATTORNEY-CLIENT COMMUNICATION / ATTORNEY WORK PRODUCT**
**For: [Witness Name]**
**Matter: [Matter Name]**
**Proceeding: [Deposition / Trial date and location]**
**Prepared by: [Attorney name]**
**Date: [Date]**

---

#### Your Preparation Summary

- **Proceeding**: [What is happening, when, and where]
- **Your role**: [What you are being asked to testify about]
- **Sessions completed**: [Number and dates]
- **Key message**: [1–2 sentence plain-language summary of what you are there to do]

---

#### Rules of the Road

[Insert rules-of-the-road content from Step 8, formatted as numbered rules in plain
language. Remove all citations and procedural complexity from this copy.]

---

#### Your Core Topics

For each CORE topic area, include a plain-language preparation card:

**Topic: [Subject]**

- What this is about: [plain-language explanation]
- What you should say: [key points in the witness's own language — not scripted, but
  framework]
- Documents to remember: [key exhibits by brief description]
- Watch out for: [anticipated cross-examination attack on this topic, described simply]

---

#### Logistics

[Day-before and day-of checklists, tailored to deposition or trial]

---

### Document 2: Attorney Assessment (Counsel Only — Not for Witness)

**PRIVILEGED AND CONFIDENTIAL — ATTORNEY WORK PRODUCT**
**Do not share with the witness**
**Matter: [Matter Name]**
**Witness: [Name / Role]**
**Date: [Date]**

---

#### Readiness Assessment

| Topic Area  | Tier | Readiness                        | Score  | Actions Required |
| ----------- | ---- | -------------------------------- | ------ | ---------------- |
| [Topic 1]   | CORE |                                  |        |                  |
| ...         |      |                                  |        |                  |
| **Overall** |      | [READY / NEEDS WORK / NOT READY] | /[max] |                  |

---

#### Prior Statement Inconsistencies

| Statement | Date | Inconsistency Type              | Risk Level   | Preparation Status        |
| --------- | ---- | ------------------------------- | ------------ | ------------------------- |
| [Source]  |      | [Explainable / Apparent / True] | HIGH/MED/LOW | [Addressed / Outstanding] |

---

#### CRITICAL Items

[For each CRITICAL item: full description, evidence basis, Three-C attack vector,
rehabilitation potential, and recommended action]

---

#### Cross-Examination Roadmap

[List anticipated cross-examination themes, attack vectors, and likely documents per
topic area. This is for counsel's use in monitoring the examination in real time.]

---

#### Redirect Rehabilitation Plan

| Cross Attack | Redirect Opportunity | Witness Preparation Status                   |
| ------------ | -------------------- | -------------------------------------------- |
| [Attack]     | [Redirect approach]  | [Prepared / In progress / Not yet addressed] |

---

#### Glass Box Audit Trail

[YAML block from Glass Box section above]

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis built from deep research into ABA
Formal Opinion 508 (2023), ABA Model Rules 1.1, 1.3, 3.3, 3.4, FRCP Rules 26/30/37,
FRE Rules 612/613/801, and practitioner guidance from Marks & Harrison, McGuireWoods,
Dentons, Holland & Knight, and the American Bar Association's litigation resources.
Structural frameworks adapted from `legalcode-deposition-preparation` (Ten-Dimension
Credibility Assessment, Three-C impeachment sequence, per-finding card structure) and
`legalcode-mediation-preparation` (CORE/TARGET/FLEXIBLE topic prioritization,
assumption-disclosure pattern, client orientation session structure). Distinct from
`legalcode-deposition-preparation` (attorney-side deposition outlines) and
`legalcode-expert-witness-preparation` (Daubert, FRE 702, FRCP 26 expert compliance):
this skill is witness-facing preparation, not attorney-facing deposition strategy.
