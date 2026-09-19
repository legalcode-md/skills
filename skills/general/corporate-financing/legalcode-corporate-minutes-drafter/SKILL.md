---
name: legalcode-corporate-minutes-drafter
description: Draft formal meeting minutes for board of directors, shareholder/stockholder, and committee
  meetings. Use when preparing minutes for any corporate meeting — annual, special, organizational, or
  written consent — covering attendance and quorum certification, agenda items, motions and voting outcomes,
  conflict of interest disclosures, committee reports, officer elections, equity and financing approvals,
  M&A and major transactions, action item assignments, and next-meeting scheduling.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Draft formal meeting minutes for board of directors, shareholder/stockholder, and committee meetings. Use when preparing minutes for any corporate meeting — annual, special, organizational, or written consent — covering attendance and quorum certification, agenda items, motions and voting outcomes, conflict of interest disclosures, committee reports, officer elections, equity and financing approvals, M&A and major transactions, action item assignments, and next-meeting scheduling. Supports US (Delaware, MBCA) and UK (Companies Act 2006) corporations with [JURISDICTION-SPECIFIC] markers for other jurisdictions. Also use when reviewing draft minutes for completeness, documenting written consents in lieu of meeting, or producing the secretary's certification block. Triggers on "draft board minutes," "write meeting minutes," "corporate minutes," "annual meeting minutes," "shareholder meeting minutes," "board resolution minutes," "committee minutes," "written consent," "action by written consent," or "minute book."


# Legalcode Corporate Minutes Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted drafting of corporate meeting
> minutes. It does not constitute legal advice. All outputs should be reviewed by a qualified
> legal professional — typically the corporation's legal counsel and company secretary or
> secretary of state — licensed in the relevant jurisdiction before execution or filing. Laws
> governing corporate governance requirements change; verify current applicability before relying
> on any provision described here. Statutory and case law references cited from memory carry
> hallucination risk — verify against authoritative sources before relying on them.

---

## Purpose and Scope

This skill drafts and reviews formal corporate meeting minutes — the contemporaneous written
record of a corporation's governance decisions. It serves two modes:

**Mode A — Draft**: Produce a complete, execution-ready minutes document from meeting details
provided by the user.

**Mode B — Review**: Evaluate an existing draft of minutes for procedural completeness,
legal sufficiency, and compliance with the applicable corporate statute and the entity's
governing documents.

**Covers:**

- Board of directors meetings: regular, special, emergency, annual
- Stockholder / shareholder meetings: annual (AGM), special, organizational
- Committee meetings: audit, compensation, nominating/governance, ad hoc
- Written consents and actions in lieu of meeting (directors and stockholders)
- Meeting-specific analysis: quorum certification, voting tallies, conflict disclosures
- Meeting completeness classification (COMPLETE / DEFICIENT / INVALID)
- Business judgment rule documentation and evidentiary protection

**Does not:**

- Draft the underlying board resolutions or stockholder resolutions (see
  `legalcode-board-resolution-drafter`)
- Provide legal advice or replace qualified counsel or a company secretary
- Apply exclusively to one jurisdiction — jurisdiction-agnostic with deep US/UK coverage
  and [JURISDICTION-SPECIFIC] markers elsewhere

---

## Jurisdiction and Governing Law

This skill provides **deep coverage** for two primary jurisdictions. For all others, use
[JURISDICTION-SPECIFIC] markers and verify local requirements with counsel.

### United States (Delaware / MBCA)

**Delaware** (DGCL, Title 8, Delaware Code):

- Recording obligation: DGCL § 142(a) — the Secretary has a statutory duty to record
  proceedings of all board and stockholder meetings.
- Board quorum: DGCL § 141(b) — majority of total directors unless the certificate or bylaws
  require more; may not be reduced below one-third.
- Board written consent: DGCL § 141(f) — **unanimity required** (all directors must sign).
- Stockholder annual meeting: DGCL § 211 — must be held annually; Court of Chancery may order
  one if not held within 13 months of the prior annual meeting.
- Stockholder quorum: DGCL § 216 — majority of shares entitled to vote; floor of one-third.
- Stockholder notice: DGCL § 222 — not less than 10 nor more than 60 days before the meeting.
- Stockholder record date: DGCL § 213 — not more than 60 nor less than 10 days before meeting.
- Stockholder written consent: DGCL § 228 — minimum vote threshold only (not unanimity);
  signatures within 60 days of first; prompt notice to non-consenting stockholders.
- Conflict of interest safe harbor: DGCL § 144 — transaction not void if approved by
  disinterested directors or stockholders with full disclosure, or if fair to the corporation.
- Stockholder list: DGCL § 219 — complete list available for inspection not less than 10 days
  before any stockholder meeting.

**Model Business Corporation Act (MBCA)** (adopted in approximately 24 states):

- Board quorum: MBCA § 8.24 — majority of directors in office.
- Board written consent: MBCA § 8.21 — unanimous consent of all directors required.
- Stockholder meeting records must be maintained as books and records of the corporation.

### United Kingdom (Companies Act 2006)

- Recording obligation: CA 2006 s. 248 — **mandatory** for all companies to record minutes of
  all directors' meetings; retention: **10 years** minimum; **criminal offense** for failure.
- Minutes as evidence: CA 2006 s. 249 — properly authenticated minutes are prima facie evidence
  that the meeting was duly held, all recorded proceedings occurred, and all appointments are valid.
- Member records: CA 2006 ss. 355–358 — written resolutions and general meeting minutes must be
  kept 10 years; available for inspection by any member without charge.
- Ordinary resolution: CA 2006 s. 282 — simple majority of votes cast.
- Special resolution: CA 2006 s. 283 — 75% majority; notice must include full text.
- Written resolutions (private companies only): CA 2006 ss. 288–300 — ordinary: majority of
  eligible shares; special: 75%; lapses after 28 days; cannot remove a director (s. 168) or
  auditor before term-end.
- AGM: CA 2006 s. 336 — required for public companies (PLCs) only; within 6 months of
  financial year-end; minimum 21 clear days' notice (CA 2006 s. 337).
- General meeting quorum: CA 2006 s. 318 — two qualifying persons (members, proxies,
  corporate representatives) unless the articles specify otherwise.
- Director conflicts: CA 2006 ss. 175–177 — duty to avoid conflicts of interest; duty to
  declare interest in proposed transactions before entry.
- Board quorum: Model Articles (SI 2008/3229, Sch. 1, Art. 11) — two directors, or the
  quorum set by the directors (never less than two where more than one director exists).

[JURISDICTION-SPECIFIC] For all other jurisdictions, apply equivalent local corporate statutes
governing: meeting notice requirements, quorum thresholds, voting standards, written consent
availability, secretary's recording obligations, and retention periods. See Localization Notes.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming the
user's intent, the workflow pauses and asks when:

- The meeting type affects required procedural elements (board vs. stockholder vs. committee)
- Attendees or quorum status cannot be confirmed from the information provided
- A conflict of interest or recusal must be documented but the facts are incomplete
- An agenda item involves a stockholder-approval requirement or tax/securities trigger
- The governing documents (bylaws, articles, committee charter) impose requirements
  not captured by the statutory default

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

### Step 1: Accept the Meeting Request

Accept the meeting request in any of these formats:

- **Free-form description**: "Draft board minutes for our Q1 2026 regular meeting"
- **Meeting agenda**: A list of agenda items provided in advance or as a post-meeting summary
- **Draft minutes to review**: An existing draft that needs completeness evaluation
- **Meeting notes**: Rough notes from the meeting to be formalized into minutes

If the meeting has not yet occurred, offer to produce a **shell minutes template** populated
with the agenda items for the secretary to complete during the meeting.

### Step 2: Gather Meeting Context

**⟁ CLARIFY** — Before drafting, gather the following context. Present as structured options
where possible:

1. **Entity type and jurisdiction**
   - Options: Delaware corporation, MBCA-state corporation, UK private limited company (Ltd),
     UK public limited company (PLC), Other — specify
   - _Why this matters_: Sets the statutory baseline for quorum, notice, voting thresholds,
     and what actions require stockholder approval.

2. **Meeting type**
   - Options: Regular board meeting, Special board meeting, Annual board meeting, Organizational/
     first board meeting, Annual meeting of stockholders/shareholders (AGM), Special meeting of
     stockholders, Committee meeting (specify committee), Action by written consent (in lieu
     of meeting)
   - _Why this matters_: Meeting type controls required procedural elements, notice requirements,
     voting mechanics, and what business may be transacted.

3. **Date, time, location, and format**
   - Date and time of the meeting.
   - Location: physical address, or remote — specify platform (Zoom, Teams, telephonic) and
     whether any directors participated remotely.
   - Format: in-person, virtual only, hybrid.
   - _Why this matters_: Affects the call-to-order statement and whether the remote-participation
     provisions of the bylaws or applicable statute were satisfied.

4. **Meeting purpose (for special meetings)**
   - Free text: state the specific purpose(s) for which the special meeting was called.
   - _Why this matters_: Special meetings may transact only the business stated in the notice.
     Minutes must confirm this limitation was observed.

5. **Governing documents available?**
   - Options: Yes — I can provide bylaws/articles/committee charter, No — proceed with
     statutory defaults, Partially — I will provide what I have
   - _Why this matters_: Bylaws frequently modify statutory defaults for quorum, notice, and
     voting thresholds. Proceed with statutory defaults if unavailable, but flag explicitly.

If the user provides partial context, proceed with what is available and **state all assumptions
explicitly**. Do not silently assume.

### Step 3: Identify Meeting Type and Validate Authority

Match the meeting type to the **Meeting Type Matrix** (below) and confirm:

1. **Statutory authority**: Is the meeting being called and conducted in compliance with the
   applicable statute and the entity's bylaws or articles?
2. **Scope limitation**: For special meetings, confirm that only noticed business is transacted.
3. **Required elements for this meeting type**: From the Meeting Type Matrix, identify all
   required procedural elements that must appear in the minutes.

**⟁ CLARIFY** — If the meeting type is unclear (e.g., the user describes a "quarterly board
meeting" but also mentions stockholder votes), clarify:

- "Is this a board-only meeting, or will stockholders be voting on any matters?"
- "Was this called as a special meeting with specific noticed purposes, or a regular meeting
  following the established calendar?"

### Step 4: Validate Attendance and Quorum

**⟁ CLARIFY — MANDATORY before drafting** — Minutes cannot be completed without confirming
the quorum. Ask:

1. **Directors / members present**
   - Full names of all directors (US) or directors/members (UK) present, including via
     remote communication.
   - Full names of any directors absent (with or without excuse).
   - _Why this matters_: The attendance list establishes quorum — a foundational prerequisite
     for any valid corporate action. Business transacted without quorum is void.

2. **Officers and guests present**
   - Names and roles of officers, legal counsel, financial advisors, auditors, or other guests
     who attended (or who attended for specific agenda items only).
   - Note when guests entered and left if they were present only for part of the meeting.
   - _Why this matters_: Officers' attendance establishes reliance on management reports.
     Advisor attendance is required for business judgment rule documentation.

3. **Recusals for conflict of interest**
   - Did any director/member have a conflict of interest in any agenda item?
   - If yes: name of the interested director, the nature of the conflict, and whether they
     recused from discussion, from the vote, or both.
   - _Why this matters_: Conflict disclosures must be contemporaneously documented. Failure
     to document is a governance failure that can void the transaction or remove the director
     from the protection of DGCL § 144 / CA 2006 ss. 175–177.

4. **Quorum confirmation**
   - Total number of directors on the board (for board meetings), or total shares outstanding
     and shares represented (for stockholder meetings).
   - Calculate and confirm quorum is satisfied before proceeding. If quorum is not confirmed,
     flag INVALID and do not draft the minutes as if valid corporate action occurred.
   - _Why this matters_: Quorum is a statutory requirement. No valid corporate action may be
     taken at a meeting where quorum is not established and maintained.

### Step 5: Gather Agenda Items and Discussion Details

**⟁ CLARIFY** — For each agenda item, gather:

1. The agenda item description and purpose.
2. Materials presented (reports, presentations, financial statements, fairness opinions —
   referenced by title and date).
3. Advisors or officers who presented or opined.
4. Scope of discussion: note that discussion occurred and its general scope (without word-for-word
   attribution); note time devoted to substantive items.
5. The motion, who moved it, and whether it was seconded.
6. The vote: unanimous / non-unanimous (provide counts: X in favor, Y against, Z abstentions,
   W recusals).
7. The outcome: adopted, failed, deferred, referred to committee.
8. Action items: who is authorized to act, by what deadline, subject to what conditions.

**⟁ CLARIFY** — For each agenda item involving a significant corporate action, ask:

- "Did any director make or note a dissent or abstention? If so, who, and on what basis?"
- "Was there a formal presentation by advisors? If so, by whom, and was a report or fairness
  opinion presented in writing?"
- "Were any documents approved, executed, or authorized at the meeting? If so, provide titles."

### Step 6: Check Action-Specific Prerequisites

Before drafting the minutes for high-risk or complex actions, confirm that necessary prerequisites
have been met:

| Action Type                        | Key Prerequisites                                                                                                   | Why It Matters                                                               |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Equity grants (options/RSUs)**   | 409A valuation current (US); equity plan approved by board and stockholders                                         | Options below FMV create IRC § 409A penalty to the recipient                 |
| **Equity plan adoption**           | Stockholder approval within 12 months for ISO eligibility (IRC § 422)                                               | ISOs require stockholder-approved plan                                       |
| **Preferred stock issuance**       | Authorized shares available; certificate of incorporation authorizes the class/series                               | Issuance of unauthorized shares is void                                      |
| **Dividend declaration**           | Surplus exists (DGCL § 170) or UK equivalent (net assets exceed called-up share capital + undistributable reserves) | Unlawful dividend creates director liability                                 |
| **M&A approval**                   | Board recommendation; fairness opinion (if fiduciary duty context); appraisal rights notice                         | Board minutes are critical evidentiary record — Smith v. Van Gorkom [VERIFY] |
| **Officer election**               | Bylaw authority for the specific title; no conflicting provisions                                                   | Confirm all officer appointments are authorized by the bylaws                |
| **Stockholder approval required?** | Check whether the action requires stockholder vote (merger, charter amendment, dissolution, DGCL § 271 asset sale)  | Board-only approval for a stockholder-required action is void                |
| **Written consent validity**       | All directors signed (board, US); private company + 28-day lapse not expired (UK members)                           | Non-unanimous board consent void under DGCL § 141(f); MBCA § 8.21            |

**⟁ CLARIFY** — For any action on the list above:

- "Has the [prerequisite] been confirmed? If not, I will flag this as DEFICIENT in the
  completeness assessment."
- "Should I draft the minutes on the assumption that prerequisites are satisfied, or would
  you like me to include a prerequisite checklist as a drafting note?"

### Step 7: Gather Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** to gather legal authority relevant to the meeting type and actions
being documented before drafting.

**Research targets:**

- Applicable corporate statute provisions governing meeting notice, quorum, and voting
  for the entity's jurisdiction
- Bylaw enforceability rules for any unusual provisions in the entity's governing documents
- Case law relevant to business judgment rule protection (especially for M&A or
  related-party transactions)
- Any recent statutory amendments affecting the meeting type (e.g., electronic meeting rules)

Save results to `/tmp/legalcode-minutes-authority.md` for use in the draft.

**If legalcode-mcp is not connected:**

- Proceed using general corporate law knowledge calibrated to the stated jurisdiction.
- Mark all statutory references in the minutes draft with [VERIFY].
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — manual verification required"`.

### Step 8: Draft the Minutes

Draft the minutes following the **Output Format Template** (below).

**Drafting principles:**

- Write in past tense throughout — minutes record what occurred.
- Use the entity's formal legal name in the header.
- Reference governing documents by their exact title (e.g., "the Amended and Restated Bylaws
  dated [date]" rather than "the bylaws").
- For each action taken: include the exact text of the resolution or the complete description
  of the motion and outcome.
- For discussions: describe scope and substance without verbatim attribution — "The board
  discussed the proposed financing, including the proposed interest rate, covenant structure,
  and dilution impact on existing stockholders" rather than "'Director X said Y.'"
- For privileged discussions with counsel: note only that a privileged discussion occurred;
  do not summarize substance.
- Executive session: note that the session occurred, attendance, presiding director, and any
  formal actions — but do not summarize discussion.

**⟁ CLARIFY** — For minutes length and detail:

- "Should these minutes be comprehensive (detailed discussion summaries for business judgment
  rule documentation) or concise (standard administrative format noting decisions only)?"
  - **Comprehensive**: recommended for M&A, related-party transactions, significant equity
    actions, any matter where fiduciary duty scrutiny is foreseeable.
  - **Concise**: appropriate for routine administrative matters (officer elections, ratification
    of prior actions, scheduling).

### Step 9: Quality Verification

Before delivering the minutes, run the completeness checklist and quality frameworks:

#### 9a. Procedural Completeness Checklist

Run through every item. Flag any unchecked item in the Minutes Completeness Classification.

```
PROCEDURAL ELEMENTS
[ ] Entity legal name and state of incorporation/registration correct
[ ] Meeting type stated correctly (regular board / special / AGM / etc.)
[ ] Date, start time, end (adjournment) time noted
[ ] Location or remote-communication platform specified
[ ] Notice given or waiver of notice attached / referenced
[ ] Record date confirmed (stockholder meetings)
[ ] Stockholder list availability confirmed per DGCL § 219 or equivalent
[ ] Presiding officer identified
[ ] Secretary identified (person recording the minutes)

ATTENDANCE & QUORUM
[ ] Full name of every director/member present (including remote)
[ ] Full name of every director/member absent; reason noted if known
[ ] Quorum calculated and certified (X of Y required; Z present)
[ ] Officers present named and titled
[ ] Guests / advisors named and role stated; entry/exit noted if partial attendance

NOTICE / WAIVER
[ ] Notice was timely given OR waiver of notice executed by all applicable parties
[ ] Method and date of notice stated
[ ] Waiver of notice form appended or referenced if notice was waived

AGENDA & VOTING
[ ] Prior meeting minutes approved (or first organizational meeting noted)
[ ] Each agenda item documented with: motion, mover, second, discussion scope, vote, outcome
[ ] Voting tallies stated (in favor / against / abstentions / recusals) for each action
[ ] Non-unanimous votes: names of dissenters and abstainers recorded
[ ] For stockholder meetings: shares present vs. total outstanding; proxy vote tallies

CONFLICTS & RECUSALS
[ ] All director conflicts identified, disclosed, and documented
[ ] Interested directors noted as recused from discussion and/or vote
[ ] Basis of conflict stated; DGCL § 144 / CA 2006 s. 177 cleanser applied or flagged
[ ] Disinterested director vote count stated separately where required

ACTIONS & AUTHORIZATIONS
[ ] Each resolution adopted is set out in complete, unambiguous language
[ ] Delegated authority specified: who may act, scope, conditions, deadline
[ ] Reference to underlying resolutions or exhibits appended
[ ] Stockholder approval: flagged if required but not yet obtained

ADJOURNMENT & NEXT MEETING
[ ] Time of adjournment stated
[ ] Next meeting date, time, and location noted (or recorded as "to be determined")

CERTIFICATION
[ ] Secretary certification language: "I hereby certify that the foregoing is a true and
    accurate record of the proceedings of the [meeting type] of [Entity Name] held on [date]"
[ ] Signature line for Secretary (and, where required, Chairman confirmation)
[ ] Exhibit list (waiver of notice, consents, materials presented) appended
```

#### 9b. Citation Quality Gates

| Gate           | Rule                                                                                                                  | Fail Action                                         |
| -------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, bylaw provision, or established authority                                 | Add citation or mark "[VERIFY — specify authority]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction (e.g., "DGCL § 141(b)"; "CA 2006 s. 248") | Fix format                                          |
| **Currency**   | Every cited provision checked for amendments or repeal                                                                | Flag "[CHECK CURRENCY]"                             |
| **Domain**     | Analysis stays within the entity's governing jurisdiction — no cross-jurisdictional bleed without flagging            | Remove or flag jurisdictional bleed                 |
| **Confidence** | Uncertainty about bylaw-specific or jurisdiction-specific requirements stated explicitly                              | Add confidence qualifier                            |

#### 9c. Self-Interrogation for Procedurally Risky Items

Apply this 3-pass review to any item classified as DEFICIENT or INVALID, and to any meeting
where a conflict of interest was disclosed or stockholder approval was required:

**Pass 1 — Procedural Integrity**: Do the minutes accurately reflect the actual meeting
process? Are voting mechanics consistent with the applicable statute and bylaws? Could a court
or regulator confirm that procedures were properly followed based solely on these minutes?

**Pass 2 — Completeness**: Are all required disclosures present — quorum calculation, proper
notice, conflict disclosures with recusal records, voting tallies for every action? Are any
statutory prerequisites missing from the record (e.g., missing DGCL § 219 stockholder list
confirmation, no fairness opinion noted for an M&A vote)?

**Pass 3 — Evidentiary Challenge**: What is the strongest argument that a corporate action
documented here is void or voidable? Under what circumstances would a stockholder derivative
plaintiff, a regulator, or opposing counsel successfully challenge the validity of what is
recorded? Address that argument in the minutes or flag it for counsel.

#### 9d. Confidence Scoring

| Level        | Range     | Meaning                                                     | Action                                                         |
| ------------ | --------- | ----------------------------------------------------------- | -------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear statute and bylaws confirm procedural validity        | State with confidence                                          |
| **High**     | 0.80–0.94 | Strong authority; minor bylaw ambiguity possible            | State with brief caveat                                        |
| **Probable** | 0.60–0.79 | Generally valid under statute; verify against actual bylaws | State with explicit reasoning                                  |
| **Possible** | 0.40–0.59 | Genuine uncertainty — bylaw or statutory ambiguity          | Flag for counsel review with both possibilities                |
| **Unlikely** | 0.0–0.39  | Weak procedural basis; likely deficient or invalid          | Do not assert validity; flag "[UNCERTAIN — counsel to advise]" |

### Step 10: Deliver the Minutes

Deliver the complete, execution-ready minutes package:

1. **Minutes document** — ready for secretary to sign
2. **Completeness Assessment** — COMPLETE / DEFICIENT / INVALID with specific flags
3. **Flags for Counsel Review** — numbered list of items requiring legal attention
4. **Glass Box Audit Trail** — YAML block for traceability
5. **Exhibit list** — documents to be appended to the executed minutes

---

## Meeting Type Matrix

[JURISDICTION-SPECIFIC] markers indicate elements that vary by jurisdiction.

| Meeting Type                                 | Quorum Required                                               | Notice Required                                                  | Voting Standard                                                                            | Written Consent Available                   | Unique Required Elements                                                                                                                        |
| -------------------------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Board — Regular**                          | Majority of board [JURISDICTION-SPECIFIC]                     | Per bylaws (typically none for scheduled meetings)               | Majority of directors present                                                              | Yes (unanimous — US)                        | Prior minutes approval; committee reports; officer reports                                                                                      |
| **Board — Special**                          | Majority of board [JURISDICTION-SPECIFIC]                     | Yes — timing per bylaws; describe purpose                        | Majority of directors present                                                              | Yes (unanimous — US)                        | State reason; limit to noticed business                                                                                                         |
| **Board — Organizational / First**           | Majority of board                                             | Waiver of notice typical                                         | Majority of directors present                                                              | Yes (unanimous — US)                        | Ratification of articles; adoption of bylaws; officer elections; stock authorization; bank account authorization; registered agent confirmation |
| **Board — Annual**                           | Majority of board                                             | Per bylaws                                                       | Majority of directors present                                                              | Less common                                 | Annual officer re-election; ratification of prior actions; fiscal year scheduling                                                               |
| **Stockholder — Annual (AGM)**               | Majority of shares (floor: one-third) [JURISDICTION-SPECIFIC] | 10–60 days (US DGCL § 222); 21 days for UK PLCs (CA 2006 s. 337) | Majority of votes cast (default)                                                           | No (physical meeting required)              | Proof of notice; § 219 stockholder list confirmation; inspector of elections (public cos); proxy vote tallies; say-on-pay (US public cos)       |
| **Stockholder — Special**                    | Majority of shares [JURISDICTION-SPECIFIC]                    | Same as annual                                                   | Majority of votes cast; supermajority for charter amendment / dissolution                  | No (physical meeting required)              | State specific purpose; confirm only noticed business transacted                                                                                |
| **Committee Meeting**                        | Per committee charter (majority of members typical)           | Per committee charter                                            | Per committee charter                                                                      | Per charter                                 | Committee charter authority; delegated scope; formal report to full board                                                                       |
| **Written Consent — Directors**              | N/A                                                           | N/A                                                              | Unanimous (US: DGCL § 141(f); MBCA § 8.21)                                                 | Yes — all directors must sign               | Date of last signature = effective date; file with minute book                                                                                  |
| **Written Consent — Stockholders / Members** | N/A                                                           | N/A                                                              | Minimum vote threshold — not unanimity (DGCL § 228); majority/75% (UK CA 2006 ss. 288–300) | Yes — US private; UK private companies only | Signatures within 60 days (US); 28-day lapse (UK); non-unanimous: notice to non-consenters                                                      |

### Organizational Meeting — Standard Agenda Template

The organizational (first) board meeting is the most formulaic meeting type and must cover:

1. Ratification of articles of incorporation / certificate of incorporation
2. Adoption of bylaws
3. Election of initial directors (if incorporators are acting)
4. Election of officers: President/CEO, Secretary, Treasurer/CFO, and any others
5. Establishment of fiscal year
6. Authorization to open bank accounts and designate signatories
7. Ratification of all pre-incorporation contracts and organizational expenses
8. Authorization of stock issuance: class, series, number of shares, price per share,
   form of consideration
9. S-Corporation election authorization (if applicable) — authorize Form 2553 filing
10. Authorization of initial employee agreements, benefit plans, and contracts
11. Appointment of accountants and legal counsel
12. Adoption of corporate seal (if any)
13. Registered agent confirmation
14. Execution of indemnification agreements (if applicable)

Attach as exhibits: certificate of incorporation, bylaws, form of stock certificate, bank
resolution forms, waiver of notice signed by all directors.

### Committee-Specific Requirements

| Committee                   | Unique Minutes Elements                                                                                                                                                                                                  |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Audit**                   | Review of financial statements; executive session with auditors without management; whistleblower matters reviewed; related-party transactions reviewed; internal control assessments; reliance on auditor reports noted |
| **Compensation**            | Compensation consultant engagement and independence confirmed; tally sheets / peer benchmarking materials referenced; specific compensation elements approved; IRC § 280G screening noted for executive changes [VERIFY] |
| **Nominating / Governance** | Director candidate evaluation process documented; independence determinations noted; board skills matrix reviewed; proxy advisor guidelines considered                                                                   |
| **Ad Hoc / Special**        | Authorizing board resolution referenced; scope of delegated authority stated; limitations on authority confirmed                                                                                                         |

---

## Conflict of Interest Disclosure Protocol

When any director has a material interest in an agenda item, apply this protocol before
drafting the relevant minutes section.

### Disclosure Requirements

**US (DGCL § 144):** A transaction is not void or voidable solely because a director is
interested if:

1. The material facts of the conflict are disclosed to the board, and the transaction is
   approved by a majority of disinterested directors; or
2. The material facts are disclosed to stockholders, and they approve; or
3. The transaction is fair to the corporation at the time it is authorized.

**UK (CA 2006 ss. 175–177):**

- Section 175: Directors must avoid conflicts of interest.
- Section 177: Directors must declare the nature and extent of any interest in a proposed
  transaction before the company enters it.
- Articles may authorize conflicts (s. 175(5)); if authorized, the minutes should confirm
  the authorization was invoked.

### What to Document in Minutes

For each conflict situation, include a complete disclosure record:

```
Conflict Disclosure Record — [Agenda Item]

Director Name: [Full name]
Nature of Conflict: [Description — e.g., "Director X is a partner at Firm Y, which is
   a counterparty to the proposed agreement" or "Director X holds a 20% equity interest
   in the target company"]
Disclosure Made: [When disclosed — before discussion, before vote, or previously disclosed
   pursuant to standing conflict disclosure on file]
Recusal Decision: [Recused from discussion only / Recused from vote only / Recused from both /
   Participated — articles authorize conflict (UK s. 175(5))]
Legal Basis: [DGCL § 144(a)(1) — disinterested board approval / CA 2006 s. 177 declaration]
Disinterested Directors Present: [Names and count]
Disinterested Director Vote: [X in favor, Y against, Z abstentions]
Result: [Transaction approved by disinterested directors]
```

### Graduated Conflict Risk Table

| Conflict Severity                       | Example                                                         | Documentation Level                                                                              | Escalation                                                   |
| --------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------ |
| **Administrative**                      | Director is an officer whose salary is under review             | Standard disclosure note; no recusal typically required                                          | None                                                         |
| **Material Financial Interest**         | Director is an equity holder in a counterparty                  | Full disclosure; recusal from vote; disinterested vote count                                     | Counsel review recommended                                   |
| **Controlling Stockholder Transaction** | Transaction with majority stockholder or affiliate              | Full disclosure; special committee formation; fairness opinion; entire fairness standard applies | Mandatory counsel review                                     |
| **Related-Party Transaction (RPT)**     | Loan to director; compensation set by non-independent committee | Full disclosure; audit committee review; RPT disclosure policy compliance                        | Mandatory counsel review; SEC or market disclosure may apply |

---

## Voting Record Framework

For each action taken at the meeting, document a complete voting record:

```
Voting Record — [Agenda Item / Resolution Title]

Motion: [Exact text of the motion as stated]
Moved by: [Director/Member name]
Seconded by: [Director/Member name]
Discussion: [Brief scope — "The board discussed [topic] for approximately [X] minutes,
   during which [Advisor/Officer] presented [materials]" — no attribution of opinions
   to individuals]
Conflict recusals: [Names of recused directors; reason; departed room Y/N]

Vote:
  In favor:    [Names] — Count: [X]
  Against:     [Names] — Count: [Y]
  Abstentions: [Names] — Count: [Z]
  Recused:     [Names] — Count: [W]
  Total voting: [X + Y]
  Quorum present: Confirmed

Outcome: [ADOPTED / FAILED / DEFERRED / REFERRED TO COMMITTEE]
Delegated authority: [Who may execute; conditions; deadline]
Underlying resolution reference: [Cross-reference if applicable]
```

---

## Minutes Completeness Classification

After completing the Procedural Completeness Checklist, classify the minutes as:

### COMPLETE

All required procedural elements are present. The minutes are ready for secretary signature
and filing in the minute book. No material deficiencies.

### DEFICIENT

One or more required elements are missing or incomplete, but the underlying corporate action
is likely valid. The minutes must be corrected or supplemented before execution.

Common deficiencies:

- Quorum stated but calculation not shown
- Voting tallies missing for one or more agenda items
- Conflict of interest disclosed verbally but not documented
- Exhibits referenced but not listed
- Prior minutes approval step omitted
- Secretary certification language absent

**Remediation**: Specify each deficiency with the exact corrective language needed.

### INVALID

A fundamental procedural defect makes the corporate action itself void or potentially void,
not merely the minutes record. Counsel must advise before execution.

**Automatic INVALID triggers:**

- Quorum not met or not confirmed — any corporate action is void
- Directors' written consent is not unanimous (US) — violates DGCL § 141(f) or MBCA § 8.21
- Business transacted at a special meeting outside the noticed purposes
- Interested director participated in a vote where recusal was required and no DGCL § 144
  safe harbor is available
- Action requires stockholder approval (charter amendment, asset sale under DGCL § 271,
  merger requiring stockholder vote) but only board approval is documented
- UK private company used written resolutions to remove a director (void under CA 2006 s. 288(2))

---

## Prioritization Framework

Classify every element in the minutes output by its priority:

### Required — Must Be Present for Validity or Statutory Compliance

- Entity name, meeting type, date, time, location
- Quorum certification with calculation
- Notice or waiver of notice confirmation
- Full attendance list (present, absent, recused)
- Exact text of each resolution adopted
- Voting tallies for each action
- Conflict of interest disclosures and recusal records
- Secretary certification and signature
- Retention in minute book (US: corporate records; UK: 10-year statutory minimum)

### Recommended — Best Practice; Builds Business Judgment Rule Protection

- Discussion scope per agenda item without attribution
- Identification of materials presented and advisors attending
- Time devoted to substantive agenda items
- Explicit approval of prior meeting minutes
- Exhibit list appended to executed minutes
- Presiding officer identified throughout
- Action items with specific delegates and deadlines
- Next meeting date recorded

### Optional — Useful but Not Essential for Validity

- Verbatim resolution language in narrative (acceptable to reference an attached exhibit)
- Detailed officer report summaries
- Background and "whereas" recitals in minutes narrative
- Industry or market context paraphrased in discussion summaries

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise before delivering if any gate fails.

| Gate           | Rule                                                                                                                           | Fail Action                                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, bylaw provision, or established principle                                          | Add citation or mark "[VERIFY — specify authority]" |
| **Format**     | All citations follow a consistent, recognizable format (e.g., "DGCL § 141(b)"; "CA 2006 s. 248"; "MBCA § 8.24")                | Fix format                                          |
| **Currency**   | Every cited provision checked for amendments or repeal                                                                         | Flag "[CHECK CURRENCY]"                             |
| **Domain**     | Analysis stays within the entity's governing jurisdiction — no bleed from Delaware into MBCA states or UK law without flagging | Remove or flag jurisdictional bleed                 |
| **Confidence** | Uncertainty about bylaw-specific or jurisdiction-specific requirements stated explicitly                                       | Add confidence qualifier                            |

---

## Self-Interrogation for High-Risk Items

For any item classified INVALID, or any matter where a conflict of interest was disclosed or
stockholder approval was required, apply this 3-pass review:

**Pass 1 — Procedural Integrity**: Do the minutes accurately reflect the actual meeting process?
Are voting mechanics consistent with the applicable statute and bylaws? Could a court or
regulator confirm proper procedure from these minutes alone?

**Pass 2 — Completeness**: Are all required disclosures present — quorum calculation, proper
notice, conflict disclosures with recusal records, voting tallies for every action? Are any
statutory prerequisites missing from the record?

**Pass 3 — Evidentiary Challenge**: What is the strongest argument that the corporate action
documented here is void or voidable? Under what circumstances would a stockholder derivative
plaintiff, a regulator, or opposing counsel successfully challenge the validity of what is
recorded? Address that argument in the minutes or flag it explicitly for counsel.

---

## Confidence Scoring

| Level        | Range     | Meaning                                                     | Action                                                         |
| ------------ | --------- | ----------------------------------------------------------- | -------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear statute and bylaws confirm procedural validity        | State with confidence                                          |
| **High**     | 0.80–0.94 | Strong authority; minor bylaw ambiguity possible            | State with brief caveat                                        |
| **Probable** | 0.60–0.79 | Generally valid under statute; verify against actual bylaws | State with explicit reasoning                                  |
| **Possible** | 0.40–0.59 | Genuine uncertainty — bylaw or statutory ambiguity          | Flag for counsel review with both possibilities                |
| **Unlikely** | 0.0–0.39  | Weak procedural basis; likely deficient or invalid          | Do not assert validity; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Include this YAML block at the end of every minutes package delivered:

```yaml
glass_box:
  skill_name: "legalcode-corporate-minutes-drafter"
  mode: "[Draft from scratch / Review of existing draft]"
  entity_name: "[Legal name of entity]"
  jurisdiction: "[Delaware / UK Ltd / UK PLC / MBCA-state / Other]"
  meeting_type: "[Board Regular / Board Special / AGM / Stockholder Special / Committee / Written Consent]"
  meeting_date: "[YYYY-MM-DD]"
  board_composition: "[Total directors authorized]"
  directors_present: "[Count]"
  quorum_required: "[Count or % of shares]"
  quorum_confirmed: "[Yes / No / Unconfirmed — flag INVALID if No]"
  actions_taken: "[Count of resolutions adopted]"
  conflicts_disclosed: "[Count; or None]"
  recusals_documented: "[Count; or None]"
  stockholder_approval_required: "[Yes — specify action / No]"
  written_consent: "[Yes — unanimous / Yes — minimum threshold / No]"
  prior_minutes_approved: "[Yes / No / N/A — first meeting]"
  governing_documents_reviewed: "[Bylaws provided / Charter provided / Model articles / Statutory defaults only]"
  legalcode_mcp: "[Connected — citations VERIFIED / Not connected — manual verification required]"
  citations_verified: "[X VERIFIED / Y UNVERIFIED / Z marked CHECK CURRENCY]"
  self_interrogation: "[PASS / REVISED — describe changes made]"
  completeness_classification: "[COMPLETE / DEFICIENT / INVALID]"
  deficiencies: "[List specific items; or None]"
  flags_for_counsel: "[Count; or None]"
  confidence: "[HIGH / MEDIUM / LOW — rationale]"
  limitations:
    - "[e.g., Bylaws not provided — statutory defaults assumed; verify against actual bylaws]"
    - "[e.g., Quorum calculation based on board size stated by user — verify against register]"
    - "[e.g., Conflict characterization requires counsel confirmation]"
  reviewer: "AI-assisted — requires review by qualified legal counsel and company secretary"
```

---

## Anti-Patterns

What NOT to do when drafting or reviewing corporate meeting minutes:

1. **Failing to confirm quorum before drafting** — Drafting minutes as if valid corporate action
   occurred when quorum cannot be confirmed. Any action without confirmed quorum is void. Always
   calculate and certify quorum before proceeding.

2. **Omitting the attendance list** — Recording only "a quorum was present" without naming
   individual directors. Courts require an identifiable record of who was present and who was
   absent. A bare quorum statement fails the evidentiary standard.

3. **Missing voting tallies** — Recording "the motion was adopted unanimously" without specifying
   the actual vote count. If a quorum challenge arises, tallies prove the vote was valid. Always
   state the count (e.g., "by a vote of 5 in favor, 0 against, 0 abstentions").

4. **Undocumented conflicts of interest** — Failing to note that an interested director disclosed
   a conflict, recused, or abstained. The absence of a conflict disclosure is treated by courts
   as evidence of concealment, not evidence that no conflict existed.

5. **Drafting minutes long after the meeting** — Minutes created weeks or months after the
   meeting are viewed by courts as unreliable and potentially fabricated. Smith v. Van Gorkom
   [VERIFY] drew adverse inferences from inadequate contemporaneous documentation. Circulate
   the draft within one week; approve at the next meeting.

6. **Verbatim attribution of director statements** — Recording "Director X said the deal was
   too risky" creates attribution liability, chills future candid discussion, and generates a
   textual record that opposing counsel will exploit in discovery. Document scope of discussion
   without attributing opinions to individuals.

7. **Summarizing privileged legal advice** — Recording the substance of counsel's advice in
   non-privileged minutes waives attorney-client privilege. Note only that a privileged
   discussion occurred and the general subject area; do not describe what counsel advised.

8. **Non-unanimous directors' written consent (US)** — Processing a directors' written consent
   that is not signed by all directors, then treating it as a valid board action. Non-unanimous
   director consent is void under DGCL § 141(f) and MBCA § 8.21. Distinguish carefully from
   stockholder written consent under DGCL § 228, which requires only the minimum vote threshold.

9. **Business outside noticed purposes at special meetings** — Transacting any business at a
   special meeting not described in the notice, then recording it in the minutes. This action
   is void regardless of whether a quorum was present. Minutes must affirmatively confirm the
   limitation was observed.

10. **Treating committee minutes informally** — Committee minutes carry the same evidentiary
    weight as full board minutes and are routinely requested in litigation, regulatory inquiries,
    and audits. Apply the same procedural rigor to audit, compensation, and nominating committee
    minutes as to full board minutes.

11. **Missing the secretary certification** — Delivering minutes without the secretary's
    certification ("I hereby certify that the foregoing is a true and accurate record...") leaves
    the document without the CA 2006 s. 249 evidentiary presumption (UK) or the equivalent US
    standard. Always include a certification block.

12. **Recording audio or video of meetings** — Audio and video recordings create verbatim records
    inconsistent with the summary-style minutes standard, inhibit candid discussion, generate
    complex discovery obligations, and create risk that recordings contradict the written minutes.
    Per CGI guidance, recordings should be deleted once minutes are approved and should not
    substitute for proper written minutes. If a recording exists, flag this for counsel.

13. **Keeping multiple draft versions** — Retaining email chains, annotated drafts, and personal
    notes after the minutes are approved creates discovery risk. Only the final approved minutes
    should be retained. Destroy all interim drafts after approval.

14. **UK: Using written resolutions to remove a director** — Written resolutions cannot be
    used to remove a director under Companies Act 2006 s. 168 or to remove an auditor before
    the end of their term. These actions require a physical general meeting with proper notice
    (special notice of 28 days under CA 2006 s. 312). Flag this immediately if it arises.

15. **Misidentifying the meeting type** — Drafting minutes for a "special board meeting" when
    the action required a stockholder vote (e.g., charter amendment, merger, asset sale under
    DGCL § 271), then recording only board approval. This produces an INVALID document.
    Always verify whether stockholder approval is required before treating board action as
    sufficient.

16. **Selective detail** — Using "extensive discussion" for some items and "brief discussion"
    for others inconsistently. Courts and plaintiffs notice differential treatment and draw
    adverse inferences. Apply consistent detail levels across all agenda items within the
    same meeting.

17. **No reference to materials presented** — Failing to note that advisors presented materials,
    or that directors reviewed reports, fairness opinions, or financial analyses. Business
    judgment rule protection rests on directors being adequately informed. Walt Disney Co.
    Derivative Litigation (Del. Ch. 2005) [VERIFY] confirmed that minutes showing genuine
    engagement with materials support protection; bare minutes without such references do not.

18. **UK: Failing to plan for 10-year retention** — Under CA 2006 s. 248, failure to retain
    minutes for 10 years is a criminal offense. Always confirm where executed minutes will be
    stored, particularly for newly formed companies with no established minute book system.

---

## Writing Standards

Apply these standards before delivering the minutes:

1. **Past tense throughout** — Minutes record completed proceedings: "The board reviewed" not
   "The board will review"; "Ms. Smith was elected" not "Ms. Smith is elected."

2. **Formal entity name** — Use the corporation's full legal name in the header. Use a defined
   short name ("the Company") consistently throughout.

3. **Plain, direct language** — Avoid archaic formulations like "WHEREFORE, IT IS RESOLVED" in
   narrative sections. Use resolution language ("RESOLVED, that...") only in the operative
   resolution texts, not in surrounding narrative.

4. **Defined terms** — Establish and use defined terms consistently: "the Board" for the board
   of directors; "the Company" for the entity; defined terms for counterparties named.

5. **Consistent detail level** — Apply the same level of detail to all agenda items within
   the same meeting. Do not provide extensive discussion summaries for some items and bare
   conclusions for others without reason.

6. **No editorializing** — Do not describe the board's mood, enthusiasm, or disagreement
   qualitatively ("the board vigorously debated"). Factual scope only: "The board discussed
   [topic] for approximately [X] minutes."

7. **Accuracy over completeness** — If information is uncertain, omit rather than guess.
   Flag uncertain information for the secretary to verify rather than including potentially
   inaccurate details.

8. **Objective confirmation test** — Before delivering: read the draft as if you were opposing
   counsel in a derivative lawsuit. Can you confirm quorum, notice, voting, and every action
   taken from the minutes alone? If not, revise.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 7, search for jurisdiction-specific statutes governing the meeting type.
- Verify quorum, notice, and voting threshold requirements against current statutory text.
- Search for recent case law on business judgment rule documentation and minutes evidentiary
  standards.
- Verify currency of any statute referenced (recent DGCL amendments, Companies Act changes).
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail.

**Without legalcode-mcp:**

- Proceed with general corporate law knowledge calibrated to the stated jurisdiction.
- Mark all statutory references with [VERIFY].
- Note in the Glass Box: `legalcode_mcp: "Not connected — manual verification required"`.
- Focus on structural completeness, quorum/conflict documentation, and procedural workflow
  rather than jurisdiction-specific statutory depth.

---

## Output Format Template

```markdown
# [Entity Full Legal Name]

## [Meeting Type] — Meeting Minutes

**Date:** [Full date, e.g., March 20, 2026]
**Time:** Called to order at [time]; adjourned at [time]
**Location:** [Physical address] / [Remote platform and connection details] / [Hybrid — specify]
**Presiding Officer:** [Name and title]
**Recording Secretary:** [Name and title]

---

## Attendance and Quorum

### Directors / Members Present

| Name   | Role                                                   | Attendance                      |
| ------ | ------------------------------------------------------ | ------------------------------- |
| [Name] | [Chair / Lead Independent / Executive Director / etc.] | Present [in person / via video] |

### Directors / Members Absent

| Name   | Role   | Reason (if known)                  |
| ------ | ------ | ---------------------------------- |
| [Name] | [Role] | [Excused / Unexcused / Not stated] |

### Officers and Guests Present

| Name   | Title / Role                                     | Present For                     |
| ------ | ------------------------------------------------ | ------------------------------- |
| [Name] | [CEO / CFO / General Counsel / External Counsel] | [Full meeting / Items X–Y only] |

**Quorum Certification:** The [Chairman / Secretary] confirmed that [X] of [Y] directors
were present, constituting a quorum of the Board pursuant to [Section X of the Amended
and Restated Bylaws dated [date] / DGCL § 141(b) / CA 2006 s. 248 and Model Articles
Art. 11]. A quorum was present throughout the meeting.

---

## Notice

[Select and complete one:]

**Notice given:** Written notice of this [regular / special] meeting was provided to all
directors on [date] by [email / letter / other method], [X] days prior to the meeting,
in accordance with [Section X of the Bylaws].

**Waiver of notice:** All directors signed a written Waiver of Notice for this meeting,
a copy of which is attached hereto as **Exhibit A** and made part of these minutes.

---

## Approval of Prior Meeting Minutes

[Name] moved, and [Name] seconded, a motion to approve the minutes of the [meeting type]
held on [prior date]. The motion was **adopted** by a vote of [X] in favor, [Y] against,
and [Z] abstentions, with no modifications.

---

## Agenda Items

### Item [#]: [Agenda Item Title]

**Presented by:** [Name and role / "The Secretary / Chairman presented"]

**Background:** [One to two sentences describing the purpose and context — no verbatim dialogue]

**Discussion:** The Board discussed [topic], including [key aspects considered without
attribution]. [Name / capacity] answered questions regarding [topic]. The Board devoted
approximately [X] minutes to this item.

**[Conflict disclosure — include if applicable, omit if not:]**
Prior to discussion, [Director Name] disclosed that [nature of conflict — e.g., "Director
Smith disclosed that she is a general partner of [Firm], which is a party to the proposed
agreement"]. [Director Name] recused herself from [the discussion and the vote / the vote
only] on this item and [departed the meeting room / confirmed she would not participate].
The remaining [X] disinterested directors proceeded.

**Motion:**

> RESOLVED, that [exact resolution language, e.g., "the Company is hereby authorized to
> enter into and execute the Software License Agreement with [Counterparty], substantially
> in the form presented to the Board at this meeting, with such changes as the Chief
> Executive Officer may approve, and that the Chief Executive Officer is hereby authorized
> and directed to execute and deliver all documents, instruments, and agreements, and to
> take all such further actions, as may be necessary or appropriate to carry out the
> foregoing"].
>
> [FURTHER RESOLVED, that [additional resolution language].]

**Vote:** [X] in favor, [Y] against, [Z] abstentions[, [W] recused].

**Outcome:** The foregoing resolution was **ADOPTED**.

**Delegated authority:** [Name, title] is authorized to execute the [document/action] on
behalf of the Company, subject to [any conditions], by [deadline if applicable].

---

### Item [#]: [Next Agenda Item Title]

[Repeat Item structure above for each agenda item]

---

## Executive Session

[Include if an executive session occurred:]

At [time], [Name] requested that management and other non-director guests be excused.
Management and guests departed the meeting, and the Board convened an executive session
without management present, presided over by [Name / Lead Independent Director]. The
executive session concluded at [time], at which point management was invited to return.
No formal actions were taken during the executive session. / The following resolution
was adopted during the executive session: [resolution text and vote].

---

## Adjournment

There being no further business to come before the Board, [Name] moved to adjourn the
meeting. The motion was seconded by [Name] and adopted without objection. The meeting
was adjourned at [time].

**Next meeting:** The Board scheduled its next meeting for [date] at [time], [location /
platform]. / The next meeting date will be communicated separately.

---

## Secretary's Certification

I, [Full Name], [Secretary / Assistant Secretary] of [Entity Full Legal Name], a
[Delaware corporation / company incorporated in England and Wales / other], hereby
certify that the foregoing minutes are a true and accurate record of the proceedings
of the [meeting type] of [Entity Full Legal Name], duly held on [date], at which a
quorum of the Board of Directors was present throughout.

**Signed:** \***\*\*\*\*\*\*\***\_\_\_\_\***\*\*\*\*\*\*\***
**Name:** [Name]
**Title:** [Secretary / Assistant Secretary]
**Date:** \***\*\*\*\*\*\*\***\_\_\_\_\***\*\*\*\*\*\*\***

**Confirmed as Chairman:**
**Signed:** \***\*\*\*\*\*\*\***\_\_\_\_\***\*\*\*\*\*\*\***
**Name:** [Chairman Name]
**Date:** \***\*\*\*\*\*\*\***\_\_\_\_\***\*\*\*\*\*\*\***

---

## Exhibit List

| Exhibit | Description                                                                   |
| ------- | ----------------------------------------------------------------------------- |
| A       | [Waiver of Notice signed by all directors / Proof of Notice]                  |
| B       | [Name of materials presented — title and date]                                |
| C       | [Additional documents — e.g., Written Consent form, Fairness Opinion summary] |

---

## Completeness Assessment

**Status: [COMPLETE / DEFICIENT / INVALID]**

[If DEFICIENT or INVALID, list:]

**Deficiencies requiring correction before execution:**

1. [Specific deficiency and exact corrective language]
2. [...]

---

## Flags for Counsel Review

1. [Specific item requiring legal attention before execution — e.g., "Quorum calculation
   assumes [X] is the total board; verify against corporate records and register"]
2. [...]

---

## Glass Box Audit Trail

[YAML block as specified in the Glass Box Audit Trail section above]
```

---

## Localization Notes

This skill provides deep coverage for **Delaware corporations** and **UK companies (Ltd and PLC)**.
For other jurisdictions, apply these localization adjustments:

[JURISDICTION-SPECIFIC] **United States — MBCA States (~24 states):**

- MBCA § 8.24: Board quorum — majority of directors in office.
- MBCA § 8.21: Directors' written consent — unanimity required.
- MBCA § 7.01: Annual meeting required; court may order if not held timely.
- Many MBCA states have adopted electronic meeting provisions; verify current text.

[JURISDICTION-SPECIFIC] **United States — California:**

- Corp. Code § 307(a): Regular meetings require no notice. Special meetings require 4 days'
  notice by mail or 48 hours' notice by telegraph, fax, or electronic means.
- Corp. Code § 307(a)(8): Board may act by written consent with fewer than all directors if
  the articles or bylaws so provide — not unanimity required (differs from DGCL).
- Corp. Code § 601: Annual stockholder meeting must be held within 15 months of the last meeting.

[JURISDICTION-SPECIFIC] **Canada (CBCA and provincial):**

- Canada Business Corporations Act s. 114: Directors may meet by telephone or electronic means.
- Written resolutions (CBCA s. 117): Any number of directors who constitute a quorum may sign;
  need not be unanimous (differs from DGCL and MBCA).
- Province-specific requirements apply for extra-provincially registered companies.

[JURISDICTION-SPECIFIC] **Germany (GmbH / AG):**

- GmbH (Gesellschafterversammlung): Notarial certification required for certain resolutions;
  written resolutions possible with unanimous consent.
- AG (Hauptversammlung): Required annually; notary certification required for structural
  resolutions (merger, dissolution, capital changes).

[JURISDICTION-SPECIFIC] **Australia (Corporations Act 2001):**

- s. 248A: Directors may pass resolutions without a meeting if all directors sign (unanimous).
- s. 251A: Minutes of directors, managers, and member meetings must be retained — 7-year
  retention period [VERIFY against current Act].
- s. 250N: Public companies must hold AGM within 5 months of financial year-end.

**Universal principles across all jurisdictions:**

- All jurisdictions require some form of minutes recording for corporate governance validity.
- Conflict of interest disclosure is a fiduciary duty recognized in every major legal system.
- Written consents in lieu of meeting are available in most common-law jurisdictions but
  restricted or unavailable for certain significant actions.
- Retain local counsel to verify jurisdiction-specific requirements before executing minutes
  for any entity incorporated outside the US or UK.

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis developed using:

- **Structural analysis** of `legalcode-contract-review` (reference standard) and
  `legalcode-board-resolution-drafter` (closest structural ancestor in the same category),
  conducted by the Legalcode two-agent team.
- **Legal research** covering: DGCL §§ 141(b), 141(f), 142(a), 144, 211, 213, 216, 219,
  222, 228 (8 Del. C.); MBCA §§ 8.21, 8.24, 7.01; CA 2006 ss. 175, 177, 248–249, 282–283,
  288–300, 318, 336–337, 355–358; Model Articles for Private Companies (SI 2008/3229).
- **Case law**: Smith v. Van Gorkom (Del. 1985); Walt Disney Co. Derivative Litigation
  (Del. Ch. 2005); Caremark International Inc. Derivative Litigation (Del. Ch. 1996).
  All citations marked [VERIFY] — verify against authoritative sources before relying on them.
- **Professional guidance**: CGI (formerly ICSA) Guidance Note on Minute-Taking (2nd ed.);
  ABA Business Law Today (Jan. 2025); Dorsey & Whitney corporate minutes best practices;
  Robert's Rules of Order (12th ed., 2020); Robert's Rules of Order official FAQs.
- **Attribution**: Legalcode original synthesis. Not imported from any third-party repository.
