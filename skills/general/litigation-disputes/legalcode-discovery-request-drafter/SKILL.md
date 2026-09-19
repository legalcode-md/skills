---
name: legalcode-discovery-request-drafter
description: Draft interrogatories, requests for production (RFPs), and requests for admission (RFAs)
  tailored to specific case types. Generate objection responses with proper specific objection bases.
  Analyze proportionality under FRCP 26(b)(1), assert privilege, and advise on document preservation obligations.
  Use when drafting initial discovery packages, responding to discovery requests, building case-type templates
  for commercial, employment, IP, or personal injury litigation, or preparing for meet-and-confer on discovery
  disputes. Covers US federal practice (FRCP 26-37) and state-level variants with [JURISDICTION-SPECIFIC]
  markers. Supports both propounding side (drafting requests) and responding side (drafting objections
  and responses).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Discovery Request Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted civil discovery drafting.
> It does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before use or filing. Procedural rules
> are amended; verify current applicability before relying on any provision described here.
> Statutory, case law, and local-rule references cited from memory carry hallucination risk —
> verify against authoritative sources before relying on them. Discovery requests have
> tactical, strategic, and ethical dimensions that require experienced counsel review.

## Purpose and Scope

This skill drafts and evaluates civil discovery requests across three formal channels —
interrogatories, requests for production (RFPs), and requests for admission (RFAs) — and
generates substantive objection responses. It operates for both propounding parties (those
sending discovery) and responding parties (those answering or objecting).

**Covers:**

- Drafting interrogatories, RFPs, and RFAs calibrated to case type and litigation stage
- Generating objection responses with specific, rule-compliant bases under FRCP 26-37
- Conducting proportionality analysis under FRCP 26(b)(1) (six-factor test)
- Asserting attorney-client privilege, work-product doctrine, and common-interest privilege
- ESI discovery guidance: custodian identification, format specifications, preservation
- Case-type templates: commercial disputes, employment, IP, and personal injury
- Privilege log format and claw-back agreement structure (FRE 502)
- Meet-and-confer script generation for discovery disputes
- Anticipating objections and drafting fallback (narrowed) versions of each request

**Does not:**

- Cover criminal discovery (Brady, Jencks Act, state equivalents)
- Replace experienced litigators' strategic judgment on discovery scope and timing
- Constitute an expert opinion on discoverability in any specific jurisdiction
- Draft depositions or subpoenas (see separate skills)
- Handle international discovery (Hague Evidence Convention, GDPR cross-border constraints)

**Related skills:** `legalcode-privilege-review` (deep privilege analysis), `legalcode-early-case-assessment` (overall discovery budget and risk), `legalcode-case-timeline-builder` (preservation and sequence), `legalcode-brief-analyzer` (motions to compel/protective orders)

---

## Jurisdiction and Governing Law

This is a US federal-primary skill calibrated to the **Federal Rules of Civil Procedure
(FRCP)** as amended through 2015 and subsequent amendments. It applies directly to any
federal district court case and to state courts that follow analogous discovery rules.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- **State procedural rules**: Many states have different interrogatory limits (e.g., California
  CCP 2030.030 allows 35 interrogatories; Texas TRCP Rule 190 uses discovery "levels"; New
  York CPLR 3130 restricts to 25 interrogatories)
- **Local district court rules**: Individual districts set page limits, filing requirements,
  dispute resolution protocols, and specific ESI standards (e.g., N.D. Cal. Patent Local
  Rules; S.D.N.Y. Judge-specific standing orders)
- **Patent litigation**: Local Patent Rules (LPRs) in many districts set mandatory contentions
  timelines and discovery sequencing
- **Administrative proceedings**: EEOC, NLRB, and other agency proceedings use different
  discovery tools with distinct limitations
- **England & Wales**: CPR Part 31 (Standard Disclosure) replaces interrogatories with
  witness statements; disclosure lists replace US-style RFPs
- **Canada**: Each province has distinct rules; federal proceedings follow Federal Courts Rules

[JURISDICTION-SPECIFIC] When operating in a specific jurisdiction, always verify:

- Interrogatory limits and whether subparts count separately
- Whether contention interrogatories are permitted before the close of fact discovery
- Electronic service and filing requirements for discovery requests
- Local meet-and-confer requirements before filing discovery motions

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
case strategy, the workflow pauses and asks when:

- The answer would change which requests to prioritize or omit
- The propounding/responding side distinction is unclear
- Proportionality constraints vary materially based on deal size or case type
- Privilege exposure is case-specific and requires user judgment
- Local rules or judge-specific standing orders may override the general framework

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

- **Case description**: Complaint or answer description, key claims/defenses, case type
- **Prior discovery**: Existing interrogatories, responses, or meet-and-confer correspondence
- **Scheduling order**: Dates, limits, scope orders from the governing court
- **Client instructions**: Target discovery issues, case theory, budget constraints

If only a topic is provided (e.g., "I need discovery for a trade secret case"), proceed
to Step 2 to gather context before drafting.

### Step 2: Gather Context

**⟁ CLARIFY** — Before drafting, ask the user these questions. Present as structured options.
Skip questions already answered by the input:

1. **Propounding or responding?**
   - Options: **Propounding** (drafting requests to serve on opponent), **Responding**
     (drafting objections and responses to requests already received), **Both**
   - _Why this matters_: The entire workflow changes — propounding drafts requests;
     responding drafts objections, answers, and privilege logs.

2. **Case type**:
   - Options: Commercial dispute / Employment / Intellectual property / Personal injury /
     Patent / Antitrust/competition / Real estate / Other (describe)
   - _Why this matters_: Determines which template to activate — interrogatory topics,
     document categories, and RFA subjects differ significantly.

3. **Jurisdiction and governing rules**:
   - Options: US Federal (FRCP 26-37) / US State (which state) / England & Wales /
     Canada / Other
   - _Why this matters_: Interrogatory limits, proportionality standards, ESI protocols,
     and privilege rules are jurisdiction-specific.

4. **Discovery stage**:
   - Options: Initial (first set, opening of discovery), Mid-stream (follow-up, gaps in
     responses), Late (expert-preparation phase, cleanup requests)
   - _Why this matters_: Initial discovery is broader; late-stage discovery is targeted and
     contention-focused.

5. **Opponent profile**:
   - Options: Well-resourced / Equal resources / Resource-constrained / Cooperative /
     Likely obstructive
   - _Why this matters_: Affects proportionality arguments, request volume, anticipated
     objection strategy, and need for motion practice planning.

6. **Estimated case value / proportionality tier**:
   - Options: High value (>$10M) / Mid-size ($1M-$10M) / Small ($100K-$1M) / Very small
     (<$100K or non-monetary)
   - _Why this matters_: Proportionality (FRCP 26(b)(1)) requires the discovery burden
     to be proportional to case value. A $100K case cannot support 200 interrogatories.

7. **Specific topics to prioritize**: Free text.
   - _Why this matters_: Allows the user to direct the analysis to critical issues —
     liability, damages, witnesses, specific document repositories.

If the user provides partial context, proceed with stated assumptions and flag them explicitly
(e.g., "Assuming US federal court, FRCP 26-37 governs — let me know if that is wrong").

### Step 3: Load Legal Authority for Jurisdiction

Read the governing court's procedural rules and identify applicable constraints. Use
**legalcode-mcp** to build a working legal reference for this matter.

**Research process:**

1. **Identify governing rules** from the matter frame (e.g., FRCP, state CCP, local rules).

   **⟁ CLARIFY** — If any of the following apply, ask before proceeding:
   - **No scheduling order provided**: Ask whether discovery is open, what the cutoff date
     is, and whether any orders limit the number or scope of requests.
   - **State vs. federal**: If it is unclear whether FRCP or state rules apply (e.g., state
     court case or diversity jurisdiction), ask the user to confirm.
   - **Local patent rules**: If a patent case, ask whether Local Patent Rules (LPRs) apply
     and what contention disclosure obligations have been set.

2. **Search legalcode-mcp** for:
   - Applicable proportionality precedent in the governing district
   - Recent case law on privilege scope and waiver in this jurisdiction
   - Any standing orders from the assigned judge
   - ESI protocols specific to the court (e.g., Sedona Principles adoption)

3. **Save results** to `/tmp/legalcode-discovery-authority.md`:

   ```markdown
   # Discovery Legal Authority — [Matter Name]

   ## Governing Rules: [FRCP 26-37 / State rules / Local rules]

   ## Date Gathered: [date]

   ### Proportionality Precedent

   - [Case, citation, key holding on FRCP 26(b)(1)]

   ### Privilege Precedent

   - [Case, citation, key holding on attorney-client / work product]

   ### ESI Standards

   - [Standing order or case on ESI format, preservation, metadata]

   ### Local Rule Notes

   - [Anything court-specific about discovery disputes, meet-and-confer, motions]
   ```

**If legalcode-mcp is not connected:**

- Mark all case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with FRCP 26-37 general knowledge but flag that local precedent is unverified

### Step 4: Conduct Proportionality Analysis

Before drafting any requests, assess proportionality under **FRCP 26(b)(1)**. The 2015
amendments made proportionality a gatekeeping requirement, not an affirmative defense.

**The six proportionality factors** (FRCP 26(b)(1)):

| Factor                                              | Questions to Answer                                                                                            |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **1. Importance to issues at stake**                | How central is this information to liability, damages, or defenses? Is it outcome-determinative or peripheral? |
| **2. Amount in controversy**                        | What is the case value? Does the discovery cost justify the potential recovery?                                |
| **3. Parties' relative resources**                  | Do both sides have comparable resources? Is cost-shifting appropriate?                                         |
| **4. Parties' relative access to information**      | Does the responding party uniquely control this information? Can the propounding party get it elsewhere?       |
| **5. Importance of discovery in resolving issues**  | Is this category necessary to adjudicate the claim or defense, or duplicative of other discovery?              |
| **6. Burden or expense relative to likely benefit** | What is the estimated cost to collect, review, and produce? Is that cost proportional to the expected benefit? |

**Classify each request category using the three-tier system:**

| Classification | Meaning                                                          | Action                                                                                                    |
| -------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **GREEN**      | All six proportionality factors favor discovery                  | Draft request with confidence; minimal objection risk                                                     |
| **YELLOW**     | Mixed proportionality — some factors support, others cut against | Draft with narrowing options; anticipate scope or burden objection; provide fallback                      |
| **RED**        | Disproportionate — expected objection likely to succeed          | Either narrow to a defensible scope before serving, or flag for meet-and-confer discussion before serving |

**⟁ CLARIFY** — For RED-tier categories, present the user with two paths:

- **Option A**: Narrow the request to GREEN or YELLOW before serving (recommended)
- **Option B**: Serve as drafted and use the objection counter-argument as the opening
  position in meet-and-confer (higher risk but potentially needed for case strategy)

### Step 5: Map Issue Elements to Request Categories

Build the discovery architecture before drafting individual requests. For each claim/defense
element in the case, identify the corresponding interrogatory topic, RFP category, and RFA
target.

**Issue-to-discovery mapping:**

| Claim/Defense Element | Interrogatory Topic            | RFP Category           |              RFA Target |
| --------------------- | ------------------------------ | ---------------------- | ----------------------: |
| [Element 1]           | [Factual interrogatory]        | [Document category]    |   [Admission to narrow] |
| [Element 2]           | [Identification interrogatory] | [Custodian/repository] | [Authenticate document] |
| [Damages element]     | [Computation interrogatory]    | [Financial records]    |       [Admit causation] |

This mapping ensures that every element of every claim has at least one corresponding
interrogatory, RFP, and RFA — and prevents over-serving on well-covered issues.

**⟁ CLARIFY** — If the claim/defense elements are unclear (e.g., complaint not provided,
or elements depend on jurisdiction-specific law), ask:

- "What are the key claims/defenses you are building discovery around?"
- "Which elements do you expect to contest most heavily?"

### Step 6: Draft Interrogatories

Draft interrogatories under **FRCP 33** (or equivalent state rule).

#### Key Rules and Limits (FRCP 33)

- **Default limit**: 25 interrogatories per party, including subparts [FRCP 33(a)(1)]
- **Timing**: Served any time after Rule 26(f) conference; responses due within 30 days
- **Subparts**: Each discrete subpart counts as a separate interrogatory — use defined terms
  to avoid splitting the count
- **Scope**: Must be within FRCP 26(b)(1) (relevant, proportional, non-privileged)
- **Contention interrogatories**: Permitted under FRCP 33(a)(2), but courts may allow
  deferral until end of fact discovery if served early

**⟁ CLARIFY** — Before drafting, ask:

- "Have interrogatories already been served in this case? If so, what is the remaining
  allotment?" (Each prior interrogatory counts against the 25-question limit.)
- "Are there court orders modifying the interrogatory limit?"

#### Interrogatory Types and When to Use Each

| Type                        | Purpose                                          | Example                                                         | Drafting Notes                                       |
| --------------------------- | ------------------------------------------------ | --------------------------------------------------------------- | ---------------------------------------------------- |
| **Identification**          | Identify persons, entities, documents            | "Identify all persons with knowledge of the alleged breach"     | Use for witnesses, experts, custodians               |
| **Factual narrative**       | Describe events, circumstances                   | "Describe in detail the circumstances of [event]"               | Narrow by date, subject, actors                      |
| **Contention**              | Force adversary to crystallize legal position    | "State all facts supporting your [defense]"                     | Best served mid-to-late discovery                    |
| **Damages computation**     | Establish damages theory and methodology         | "Describe your method for calculating lost profits"             | Require identification of all inputs and assumptions |
| **Document identification** | Identify documents that exist (precursor to RFP) | "Identify all documents reflecting communications with [party]" | Useful when document volume is unclear               |

#### Interrogatory Drafting Checklist

Before serving, apply this checklist to each interrogatory:

- [ ] Is the interrogatory within the 25-question limit (counting subparts)?
- [ ] Is scope defined by date range, actor, subject matter — not unlimited?
- [ ] Does it ask for facts, not legal conclusions?
- [ ] Are all undefined terms defined in the definitions section?
- [ ] Is it phrased as a single question (not compound)?
- [ ] Is it proportional to the case value?
- [ ] Has the anticipated objection been pre-assessed?
- [ ] Is there a fallback (narrower) version if the original is objected to?

#### Interrogatory Format

```
INTERROGATORY NO. [X]: [Full question text]

**Purpose**: [What this interrogatory establishes for your case theory]
**Proportionality**: [GREEN / YELLOW / RED] — [one-sentence justification]
**Anticipated Objection(s)**:
  - [Objection type]: [Why opponent will raise it and counter-argument]
**Fallback version**: [Narrower version if primary is objected to as overbroad]
**Confidence Score**: [Definite / High / Probable / Possible / Unlikely]
**Notes**: [Synergy with RFP #X / RFA #X / deposition topic]
```

### Step 7: Draft Requests for Production (RFPs)

Draft RFPs under **FRCP 34** (or equivalent state rule).

#### Key Rules and Limits (FRCP 34)

- **No numerical limit** under FRCP 34 — but proportionality applies to each request
- **Timing**: Served any time after Rule 26(f) conference; responses due within 30 days;
  responses must state objections and whether production will be withheld
- **Scope**: Documents, electronically stored information (ESI), and tangible things
- **Specificity requirement**: Requests must describe items "with reasonable particularity"
  [FRCP 34(b)(1)(A)]
- **ESI format**: If format is not specified, respondent may produce in form ordinarily
  maintained or in a reasonably usable form [FRCP 34(b)(2)(E)]
- **Objections**: Must be stated with specificity; general objections without explanation
  are prohibited under post-2015 amendments

**Key drafting principle**: Define terms broadly in the definitions section (e.g.,
"Documents" includes ESI, metadata, text messages, chat logs, audio recordings) to avoid
loopholes created by technical readings of undefined terms.

#### ESI-Specific Guidance

For any case involving electronically stored information:

1. **Identify custodians**: Key individuals whose email, files, and devices hold relevant
   information. List in RFP definitions or accompanying ESI protocol.

2. **Specify repositories**: Email servers, shared drives, collaboration tools (Slack,
   Teams), CRMs, project management systems, mobile devices, cloud storage.

3. **Define search terms**: Propose search terms in the definitions section or in a
   separate ESI protocol agreed during the Rule 26(f) conference.

4. **Specify format**: Request native format with metadata preserved (preferred for ESI),
   or TIFF/PDF images if that is the court/opponent norm. Never leave format unspecified.

5. **Address claw-back**: Reference an agreed-upon FRE 502(d) non-waiver order or propose
   one — this protects against inadvertent privilege waiver during production.

6. **Preservation**: State that the opponent must preserve all potentially relevant ESI
   and physical documents from the litigation hold trigger date. [See legalcode-privilege-review
   for litigation hold analysis.]

[JURISDICTION-SPECIFIC] Some courts have adopted the **Sedona Principles** or their own
ESI standing orders. Research the assigned judge's standing order before finalizing ESI
requests.

#### RFP Format

```
REQUEST FOR PRODUCTION NO. [X]: [Full request text]

**Document Category**: [Type of document or ESI]
**Purpose**: [What this document category proves or disproves]
**Proportionality**: [GREEN / YELLOW / RED] — [one-sentence justification]
**Privilege Screening**: [Low / Medium / High — what privilege risk this request carries]
**ESI Considerations**: [Custodians, repositories, format requirements for this category]
**Anticipated Objection(s)**:
  - [Objection type]: [Why opponent will raise it and counter-argument]
**Fallback version**: [Narrower version if primary is objected to as overbroad]
**Confidence Score**: [Definite / High / Probable / Possible / Unlikely]
**Notes**: [Synergy with interrogatory #X / RFA #X / deposition topic]
```

### Step 8: Draft Requests for Admission (RFAs)

Draft RFAs under **FRCP 36** (or equivalent state rule).

#### Key Rules (FRCP 36)

- **No numerical limit** under FRCP 36, but proportionality governs
- **Timing**: May be served at any time after the Rule 26(f) conference; responses due
  within 30 days (or 45 days if served before defendant's answer deadline)
- **Scope**: Facts, application of law to fact, opinions about either, and genuineness
  of described documents [FRCP 36(a)(1)]
- **Deemed admitted**: Failure to respond timely = conclusive admission [FRCP 36(a)(3)]
- **Withdrawal**: An admission may be withdrawn only with court permission [FRCP 36(b)]
- **Effect**: Admissions are binding only in the case in which they are made; not usable
  in other proceedings

**Critical distinction**: RFAs are NOT discovery devices in the same sense as interrogatories
or RFPs. They are narrowing tools — designed to eliminate uncontested issues from trial.
A request for admission is most powerful when it asks about something the opponent either
cannot deny or will suffer consequences if they deny falsely.

#### Strategic Uses of RFAs

| Strategic Goal                               | RFA Example                                                                                                                               |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Authenticate documents**                   | "Admit that Exhibit 1 is a true and correct copy of the contract between the parties dated [date]"                                        |
| **Establish undisputed facts**               | "Admit that [Defendant] did not provide written notice before the cure period expired"                                                    |
| **Narrow damages theories**                  | "Admit that [Plaintiff]'s claimed damages do not include lost profits from any product other than [Product X]"                            |
| **Lock in legal admissions**                 | "Admit that [Defendant] owed a duty of care to [Plaintiff]"                                                                               |
| **Set up cost-shifting under FRCP 37(c)(2)** | Serve RFAs on facts the opponent will deny but ultimately be unable to contest; if they deny and lose, move for costs of proving the fact |

#### RFA Drafting Checklist

- [ ] Does the RFA ask about a single, discrete fact (not compound)?
- [ ] Is the RFA phrased so the natural answer is "Admit" or "Deny" (not evasive)?
- [ ] Does an admission actually help your case (do not ask what you do not want admitted)?
- [ ] Have you planned the follow-up interrogatory or deposition question if denied?
- [ ] Is the RFA drafted narrowly enough to avoid "lacks sufficient information to admit
      or deny" as a legitimate response?
- [ ] Is the subject matter appropriate (facts, law-to-fact, genuineness — not pure
      legal conclusions)?

#### RFA Format

```
REQUEST FOR ADMISSION NO. [X]: [Full request text]

**Purpose**: [What admission would establish]
**Strategic Value**: [High / Moderate / Low]
**Anticipated Response**: [Admit / Deny / Qualify / "Lack sufficient information"]
**If Denied**: [Follow-up interrogatory / deposition topic / documentary proof strategy]
**Anticipated Objection(s)**:
  - [Objection type]: [Counter-argument]
**FRCP 37(c)(2) cost-shifting potential**: [Yes / No — is this a fact opponent should
  know if they deny and then lose at trial?]
**Confidence Score**: [Definite / High / Probable / Possible / Unlikely]
```

### Step 9: Privilege and Confidentiality Screening

After drafting, screen every request for privilege and confidentiality exposure.

#### Attorney-Client Privilege Screening

Interrogatories and RFPs that may invite privileged responses or require a privilege log:

- Requests for "any and all communications" without excluding privileged communications
- Requests for "all documents relating to legal advice regarding [topic]"
- Interrogatories asking "what did you learn from counsel" or "what was your counsel's
  recommendation"

**Mitigation options:**

1. Exclude privileged materials in the request text: "...excluding any documents protected
   by the attorney-client privilege or work-product doctrine, which shall be identified
   in a privilege log."
2. Request a privilege log compliant with FRCP 26(b)(5)(A) for any withheld documents.
3. Enter an FRE 502(d) non-waiver order to protect against inadvertent disclosure.

#### Work-Product Doctrine Screening

[JURISDICTION-SPECIFIC] Work product under **FRCP 26(b)(3)** protects materials prepared
in anticipation of litigation. Two tiers:

- **Ordinary work product**: Documents and things prepared by or for a party's attorney —
  can be overcome by showing substantial need and undue hardship
- **Opinion work product**: Mental impressions, conclusions, opinions of an attorney —
  almost never discoverable; not subject to the substantial-need exception

Requests that carry work-product risk:

- Communications or notes from after the litigation hold trigger date
- Internal investigation documents prepared at counsel's direction
- Expert-related communications if the expert is retained specially for litigation

#### Privilege Log Requirements (FRCP 26(b)(5))

When asserting privilege, provide a privilege log that identifies:

1. Type of document (email, memo, letter, etc.)
2. Date
3. Author(s) and recipient(s) with their roles and relationship
4. Subject matter (general description without disclosing privileged content)
5. Privilege asserted (attorney-client / work product / common interest)

**⟁ CLARIFY** — Ask the user whether a privilege log format template is needed for
production alongside the requests (for Responding mode), or whether they need a protective
order requesting that the opponent's privilege log meet FRCP 26(b)(5) requirements.

#### Common-Interest Privilege and Joint Defense

[JURISDICTION-SPECIFIC] If multiple defendants share an attorney or coordinate defense:

- The **common-interest doctrine** may protect communications shared between co-parties
  with aligned legal interests
- A written **joint defense agreement (JDA)** is strongly recommended to memorialize
  the shared legal interest and preserve the privilege

Note: The common-interest doctrine protects only communications made _in furtherance of_
the shared legal interest — not business or commercial communications between the parties.
Courts scrutinize JDAs for true legal (not commercial) alignment.

### Step 10: Generate Objection Responses (Responding Mode)

When operating in Responding mode (drafting objections and answers to received requests):

#### The Specificity Requirement (Post-2015 Amendments)

The 2015 amendments to FRCP 34(b)(2) require that:

- Objections must be stated **with specificity** — not general or boilerplate
- Objecting party must **state whether any responsive materials are being withheld** on
  the basis of the objection
- An objection that a request "is not reasonably calculated to lead to admissible evidence"
  **is no longer valid** — that phrase was deleted in 2015 [VERIFY currency]

Prohibited objection language (court-sanctioned as improper):

- "Defendant objects to this request as vague, ambiguous, overbroad, and unduly burdensome"
  (without specificity)
- "Plaintiff objects to the extent the request seeks information protected by the attorney-
  client privilege" (without logging the withheld items)
- "Objection — not reasonably calculated to lead to admissible evidence" (2015 amendment
  deleted this standard from FRCP 26(b)(1))

#### Objection Framework

For each incoming request, apply this framework:

| Step                                         | Action                                                                          |
| -------------------------------------------- | ------------------------------------------------------------------------------- |
| **1. Identify valid objection basis**        | Is there a specific, articulable reason to object?                              |
| **2. State the objection specifically**      | Name the rule, explain how this request violates it                             |
| **3. State whether production is withheld**  | FRCP 34 requires statement of what is or is not being produced                  |
| **4. Respond to non-objectionable portions** | Produce what is not objected to; do not use an objection to withhold everything |
| **5. Meet and confer**                       | Objection is not a refusal — conferral required before motion to compel         |

#### Objection Reference Table

| Objection                           | Legal Basis                   | Required Specificity                               | Counter to Expect                                |
| ----------------------------------- | ----------------------------- | -------------------------------------------------- | ------------------------------------------------ |
| **Overbroad**                       | FRCP 26(b)(1) proportionality | Explain which specific aspect is overbroad and how | Narrowing offer in meet-and-confer               |
| **Unduly burdensome**               | FRCP 26(c)(1)(B)              | State estimated cost, hours, custodians, documents | Cost-shifting or phased production offered       |
| **Not proportional**                | FRCP 26(b)(1) six factors     | Apply each proportionality factor to this request  | Motion to compel with proportionality argument   |
| **Vague or ambiguous**              | FRCP 33(a)(2)                 | Identify which term or phrase is ambiguous         | Clarification in meet-and-confer                 |
| **Compound**                        | FRCP 33(a)(2)                 | Identify the multiple discrete questions bundled   | Agreement to split into separate interrogatories |
| **Calls for legal conclusion**      | FRCP 33(a)(2)                 | Explain what legal conclusion is sought            | Reformulation to factual predicate               |
| **Attorney-client privilege**       | FRE 501; FRCP 26(b)(5)        | Log withheld items; identify scope of privilege    | Challenge to privilege log completeness          |
| **Work-product doctrine**           | FRCP 26(b)(3)                 | Log withheld items; identify ordinary vs. opinion  | Substantial-need and undue-hardship showing      |
| **Seeks confidential/trade secret** | FRCP 26(c)(1)(G)              | Identify nature of the confidentiality             | Protective order negotiation                     |
| **Already in possession**           | FRCP 33(a)(3)                 | Reference specific prior production                | Verification of prior production completeness    |

#### Meet-and-Confer Script Template

Generate a meet-and-confer outline addressing anticipated objections:

```markdown
## Meet-and-Confer Agenda — [Matter Name]

**Date**: [date]
**Parties' counsel**: [names]
**Purpose**: Discovery dispute resolution re: [Interrogatory Set 1 / RFP Set 1 / etc.]

### Opening Position

[Propounding party statement of what is sought and why it is proportional]

### Response to Objections

For each sustained objection:

1. **Objection**: [Specific objection raised]
2. **Counter**: [Your counter-argument and cited authority]
3. **Compromise offer**: [Narrowing, phased production, format change, or other accommodation]
4. **Fallback**: [Minimum acceptable resolution before filing motion to compel]

### ESI-Specific Discussions

- Custodians agreed: [list]
- Search terms proposed: [list]
- Format agreement: [native / TIFF / other]
- Claw-back order: [FRE 502(d) — proposed or agreed]

### Resolution Items

For each request in dispute:
| Request | Opponent's Objection | Your Position | Resolution or Next Step |
|---------|--------------------|----|---|
| Int. No. X | [objection] | [your position] | [agreed / unresolved → motion to compel] |

### Certification

FRCP 37(a)(1) requires certification that parties have in good faith conferred before
filing a motion to compel. Document the date, participants, and substance of this conference.
```

**⟁ CLARIFY** — If operating in Responding mode, ask:

- "Have you received the discovery requests already? If yes, please share them so I can
  draft specific objections and responses."
- "Are there any requests you are unwilling to respond to under any circumstances, or
  are you open to producing some version of the requested information?"

### Step 11: Quality Assurance and Delivery

Before delivering any discovery request set or response package, run the full quality
assurance framework.

**⟁ CLARIFY** — For large or complex discovery packages (100+ requests, multiple case
types, or complex privilege issues), ask whether the user wants:

- **Full package**: All interrogatories, RFPs, RFAs, objection guidance, privilege analysis,
  meet-and-confer script, and Glass Box audit trail
- **Priority focus**: Only the most important categories (user specifies priority topics)
- **Responding-only**: Focus on drafting specific objections to a received request set

---

## Case-Type Discovery Templates

Activate the appropriate template based on the case type identified in Step 2.

### Template A: Commercial Dispute (Contract Breach / Trade Dispute)

**Discovery architecture:**

**Core liability interrogatories (15-20):**

1. Identify all persons with knowledge of contract formation, performance, or breach
2. Describe all communications regarding performance obligations (by date range and subject)
3. Identify all documents reflecting the alleged breach of [specific provision]
4. Describe the timeline of events from contract execution through breach
5. Identify all prior disputes between the parties under this or related agreements
6. Describe the basis for any claimed excuse or force majeure defense
7. Identify all persons involved in the decision to [breach/repudiate/terminate]
8. Describe your [plaintiff's/defendant's] damages computation methodology
9. Identify all attempts to mitigate damages, including the steps taken and outcome
10. Describe all representations made regarding [subject of contract] before execution
11. Identify all third parties whose performance affected the contract
12. Describe any course-of-dealing or course-of-performance affecting interpretation
13. Identify all expert witnesses and the subjects on which they will testify
14. Describe the relationship between the parties before the agreement was executed
15. Identify all similar agreements between [defendant] and other parties in the past
    [X] years

**Core RFP categories (20-30):**

- The contract, all amendments, schedules, exhibits, and incorporated documents
- All drafts of the contract and negotiation correspondence
- All communications (email, text, chat) regarding performance and alleged breach
- Invoices, payment records, and accounts receivable/payable records
- Remediation or cure attempt records
- Comparable agreements with third parties
- Internal communications about the decision to [breach/terminate]
- Expert witness files and materials
- Financial statements and P&L records for the damages period
- Insurance claims related to the dispute

**Core RFAs (10-15):**

- Admit that the contract is authentic and was executed by the parties
- Admit that [specific provision] was included in the final agreement
- Admit that [defendant] received notice of breach on [date]
- Admit that [plaintiff] performed its material obligations under the contract
- Admit that no written amendment modified [specific provision]
- Admit that damages commenced on [date]

---

### Template B: Employment Dispute (Discrimination / Retaliation / Wrongful Termination)

**Discovery architecture:**

**Core liability interrogatories (15-25):**

1. Identify all persons involved in the decision to [terminate / demote / not promote] plaintiff
2. Describe all reasons for the adverse employment action, in order of importance
3. Identify all comparator employees who engaged in similar conduct and were treated differently
4. Describe all prior complaints of [discrimination / harassment / retaliation] made by any
   employee in the past [X] years and the outcome of each
5. Identify all persons present at [incident / meeting / review] and describe their roles
6. Describe all performance documentation for plaintiff from the date of hire to termination
7. Identify all policies regarding [discrimination / retaliation / termination] and whether
   they were followed in plaintiff's case
8. Describe the timeline of events from plaintiff's protected activity to the adverse action
9. Identify all communications between decision-makers regarding plaintiff
10. Describe the legitimate non-discriminatory reasons for the adverse action in detail
11. Identify all witnesses to [the discriminatory act / retaliatory conduct / harassment]
12. Describe how similarly situated employees outside plaintiff's protected class were treated
13. Identify all prior EEOC charges or civil rights complaints filed against defendant
14. Describe the decision-making process for [terminations / promotions] generally
15. Identify all communications between defendant and any state/federal agency regarding
    plaintiff's charge

**Core RFP categories (15-25):**

- Plaintiff's complete personnel file
- All performance evaluations for plaintiff and comparator employees
- All communications (email, messaging) referring to plaintiff
- HR investigation files related to any complaint involving plaintiff
- Comparator employees' personnel files (subject to proportionality/privacy limitations)
- All policies on discrimination, harassment, and retaliation (all versions)
- EEOC position statement and supporting documentation
- Payroll records and compensation comparisons
- Supervisor notes, meeting minutes, and decision memos

**Core RFAs (8-12):**

- Admit that plaintiff engaged in protected activity on [date]
- Admit that defendant was aware of plaintiff's protected activity before the adverse action
- Admit that plaintiff's job performance was satisfactory through [date]
- Admit that the adverse action occurred within [X] days of plaintiff's protected activity
- Admit that comparator employee [name/role] was not subject to the same adverse action
- Admit that defendant's written policy requires [X] before termination

[JURISDICTION-SPECIFIC] Employment discovery: In California, employees have heightened
privacy rights; personnel file requests may be subject to the California Personnel Records
Act (Labor Code §1198.5). Federal EEOC files may require separate FOIA requests.

---

### Template C: Intellectual Property (Patent / Trade Secret / Copyright / Trademark)

**Discovery architecture:**

**Patent-specific interrogatories (20-30):**

_For Plaintiff (patent owner to accused infringer):_

1. Describe in detail all products and processes that practice the asserted patent claims,
   element by element
2. Identify all persons who designed, developed, tested, or manufactured [accused product]
3. Describe all prior art you contend renders the asserted claims invalid
4. Describe your claim construction position for each disputed claim term
5. Identify all communications with any person regarding knowledge of the patent prior
   to the filing of this lawsuit
6. Describe all revenues, costs, and profits attributable to [accused product] for the
   damages period
7. Identify all licenses entered into regarding [accused product] or comparable technology
8. Describe all design-around efforts made or considered regarding the asserted claims
9. Identify all expert witnesses and their expected testimony
10. Describe all secondary considerations of non-obviousness (if relevant to invalidity)

_For Defendant (accused infringer to patent owner):_

1. Describe the conception and reduction to practice of the claimed invention, including
   all persons involved and all documents
2. Identify all prior art known to the inventors during prosecution
3. Describe all prior art you contend renders the asserted claims invalid, element by
   element with chart
4. Describe all statements made to the USPTO during prosecution affecting claim scope
5. Identify all persons with knowledge of the earliest date of public disclosure
6. Describe all reasonable royalty components and the comparable license agreements
7. Identify all persons and entities that have licensed the asserted patents
8. Describe all products or processes you contend are non-infringing alternatives

**Trade secret interrogatories (15-20):**

1. Identify each alleged trade secret with sufficient particularity [JURISDICTION-SPECIFIC:
   California DTSA and state equivalents require early identification before discovery]
2. Describe the reasonable measures taken to maintain secrecy of each alleged trade secret
3. Identify all persons who had access to the alleged trade secrets
4. Describe the economic value of each alleged trade secret and how that value is derived
5. Identify all documents reflecting independent development of the allegedly misappropriated
   information
6. Describe all communications between defendant and former employees of plaintiff

**Core IP RFP categories (20-40):**

- Patent prosecution file and all USPTO correspondence
- Design and development documents for [accused/claimed invention]
- Prior art searches, freedom-to-operate opinions, and competitor analyses
- All licenses and royalty agreements for the patent or comparable technology
- Revenue and financial records for the damages period
- Source code and technical documentation (subject to source code protocol)
- Communications with inventors regarding conception and reduction to practice
- Expert files and materials

**Core RFAs (10-20):**

- Admit that [exhibit] is a true and correct copy of the asserted patent
- Admit that [product feature] is present in [accused product]
- Admit that no license was obtained before the date of first infringement
- Admit that the patent was in force and effect during the damages period

[JURISDICTION-SPECIFIC] In patent cases, **Local Patent Rules (LPRs)** in the N.D. Cal.,
E.D. Tex., D. Del., and other districts impose mandatory disclosure deadlines for
infringement contentions, invalidity contentions, and claim construction positions. Verify
local rules before relying on standard FRCP timing.

---

### Template D: Personal Injury / Products Liability

**Discovery architecture:**

**Core liability interrogatories (15-20):**

1. Describe in detail the circumstances of the incident, including all actors, locations,
   and sequence of events
2. Identify all witnesses to the incident or who have knowledge of the circumstances
3. Describe all prior incidents, claims, or complaints involving [same product / location /
   conduct] in the past [X] years
4. Identify all safety standards, codes, or regulations applicable to [product / premises]
5. Describe all inspections, maintenance, and repair of [product / premises] in the [X]
   years before the incident
6. Identify all warnings or instructions provided to [plaintiff / user] regarding [product /
   condition]
7. Describe all remedial measures taken after the incident
8. Identify all insurance policies that may provide coverage for this claim
9. Describe plaintiff's medical history relevant to the claimed injuries, including all
   prior treatment for similar conditions [FRCP 35 medical examination may also be sought]
10. Identify all health care providers who treated plaintiff for claimed injuries
11. Describe all claimed economic damages, including lost wages and medical expenses
12. Identify all expert witnesses, their qualifications, and the subject of their opinions

**Core RFP categories (15-25):**

- Incident or accident reports
- Photos, videos, and diagrams of the scene and product
- Maintenance and inspection records for [product / premises]
- Prior complaint and claim files regarding similar incidents
- Medical records and bills (via authorization or subpoena)
- Employment and wage records (lost income claims)
- Insurance declarations pages and claims files
- Expert files and materials
- Product design and warnings documents

**Core RFAs (8-12):**

- Admit that defendant had a duty of care to plaintiff on the date of the incident
- Admit that the incident occurred at [location] on [date]
- Admit that [specific condition] was present at the time of the incident
- Admit that defendant had prior notice of [condition / defect]
- Admit that plaintiff has not fully recovered from the injuries claimed

---

## Proportionality Classification System

Every request category in the output must receive a proportionality classification:

### GREEN — Proportional Discovery

**Definition**: Expected benefit of the information clearly outweighs the burden of
production. All or most FRCP 26(b)(1) factors favor discovery.

**Characteristics:**

- Directly relevant to core liability or damages element
- Information likely uniquely within responding party's control
- Production cost is manageable relative to case value
- No significant privilege risk
- Narrowly scoped (specific custodians, date ranges, document types)

**Action**: Draft the request as-is. Anticipate minimal objection.

### YELLOW — Borderline Proportionality

**Definition**: Some FRCP 26(b)(1) factors favor discovery, but others cut against. An
objection is plausible and may succeed without a narrowing offer.

**Characteristics:**

- Relevant but not outcome-determinative
- Broad scope or large anticipated document volume
- Production cost may be significant relative to case value
- Some privilege risk

**Action**: Draft both the primary request AND a fallback (narrower) version. Use the
meet-and-confer script to lead with the primary and offer the fallback as a compromise.

### RED — Disproportionate

**Definition**: FRCP 26(b)(1) factors do not support discovery as drafted. An objection
is likely to be sustained unless the request is narrowed.

**Characteristics:**

- Tangential relevance
- Very large document volume relative to case value or importance
- High production cost
- Broad scope covering many custodians, long time periods, or marginally relevant topics

**Action**: Narrow the request before serving OR flag for strategic meet-and-confer
discussion. Never serve a RED-tier request without a plan for the anticipated objection.

---

## Prioritization Framework

Organize the final discovery package by tier:

### Tier 1 — Must-Serve (Case-Critical)

Requests that directly establish or defeat core liability elements; requests for documents
that only the opponent possesses; interrogatories that lock in the opponent's factual
theory before depositions.

### Tier 2 — Should-Serve (Material Requests)

Requests that materially strengthen the case but where some information may be available
from other sources; damages-focused interrogatories; document requests for corroborative
evidence.

### Tier 3 — Optional (Strategic Enhancement)

Requests that are useful but where the cost-benefit analysis is close; deposition
preparation requests that are not essential to the core theory; requests designed to
narrow the issues for trial rather than establish liability.

**Sequencing strategy**: Serve Tier 1 and Tier 2 in the initial request set. Defer
Tier 3 unless discovery is productive and budget allows. Reserve follow-up interrogatory
slots for contention interrogatories at close of fact discovery.

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                             | Fail Action                                              |
| -------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every procedural objection cites FRCP 26-37, local rules, or a case              | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a recognizable format: "FRCP 26(b)(1)" not "Rule 26"        | Fix citation format                                      |
| **Currency**   | Verify that cited provisions reflect 2015 and subsequent amendments              | Flag "[CHECK CURRENCY — post-2015 amendment may apply]"  |
| **Domain**     | Analysis stays within governing jurisdiction; no FRCP bleed into UK CPR analysis | Remove or flag cross-jurisdiction error                  |
| **Confidence** | Uncertainty explicitly stated; "courts have held" only where authority is cited  | Add confidence qualifier or mark [VERIFY]                |

---

## Self-Interrogation for RED-Tier Requests

For any request classified as RED (disproportionate), apply this 3-pass self-interrogation
before including it in the output:

**Pass 1 — Proportionality Chain Integrity**:

- Do all six FRCP 26(b)(1) factors actually support this objection risk?
- Would a federal magistrate sustain an objection to this request as served?
- Is there a narrowing that would make this GREEN or YELLOW?

**Pass 2 — Completeness**:

- Have alternative discovery tools been considered (interrogatory instead of broad RFP,
  for example)?
- Is there a less burdensome way to get equivalent information?
- Would phased production resolve the burden concern?

**Pass 3 — Adversarial Challenge**:

- What is the strongest argument that this request IS proportional?
- Under what circumstances would the requesting party prevail on a motion to compel?
- Is the RED classification proportionate, or is this actually YELLOW with a reasonable
  narrowing offer?

If any pass reveals a weakness in the classification, revise before delivery. Mark the
audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

---

## Confidence Scoring

For each material interrogatory, RFP, and RFA, assign a confidence level:

| Level        | Range     | Meaning                                           | Action                                                   |
| ------------ | --------- | ------------------------------------------------- | -------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled rule, controlling case, no ambiguity      | State with confidence                                    |
| **High**     | 0.80-0.94 | Strong authority, minor interpretation questions  | State with brief caveat                                  |
| **Probable** | 0.60-0.79 | Good arguments but proportionality is contestable | State with explicit reasoning and counter-indicators     |
| **Possible** | 0.40-0.59 | Genuinely uncertain — could go either way         | Flag for counsel review with both sides                  |
| **Unlikely** | 0.0-0.39  | Weak basis for the request or objection           | Do not assert; flag as "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every discovery package output MUST include a Glass Box audit section at the end:

```yaml
glass_box:
  matter_name: "[Case name / matter identifier]"
  case_type: "[Commercial / IP / Employment / Personal Injury / Patent / Antitrust / Other]"
  mode: "[Propounding / Responding / Both]"
  jurisdiction: "[US Federal / US [State] / UK / AU / Other]"
  governing_rules: "[FRCP 26-37 / State CCP / CPR Part 31 / etc.]"
  discovery_stage: "[Initial / Mid-stream / Late]"
  case_estimated_value: "[$ range or 'Non-monetary']"
  opponent_resources: "[Well-resourced / Equal / Resource-constrained]"
  template_used: "[Commercial / Employment / IP / Personal Injury / Custom]"
  proportionality_test_applied: "YES / NO"
  proportionality_distribution:
    green: "[N] requests"
    yellow: "[N] requests"
    red: "[N] requests"
  requests_total:
    interrogatories: "[N]"
    rfps: "[N]"
    rfas: "[N]"
  objections_anticipated: "[N]"
  privilege_screening_performed: "YES / NO"
  esi_guidance_included: "YES / NO"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-discovery-authority.md or 'Not created']"
  citations_verified: "[N VERIFIED] / [N VERIFY]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified legal review before serving or filing"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in discovery drafting and response:

1. **Proportionality-blind drafting** — Writing requests without assessing FRCP 26(b)(1)
   proportionality factors. Courts regularly sustain objections to requests that fail the
   proportionality test; drafting without this analysis produces requests that invite
   sanctions and successful protective orders.

2. **Boilerplate objections** — Responding to every request with "Defendant objects to
   this request as vague, ambiguous, overbroad, and unduly burdensome" without specificity.
   Federal courts have imposed sanctions for boilerplate objections, which are per se
   improper under the 2015 amendments. State the specific ground with specificity.

3. **Citing the old discovery standard** — Using "not reasonably calculated to lead to
   admissible evidence" as an objection. This language was deleted from FRCP 26(b)(1) in
   the 2015 amendments. Using it signals ignorance of current rules and undermines
   credibility with the court.

4. **Fishing-expedition requests** — Drafting unlimited "any and all documents relating
   to any aspect of this dispute" without narrowing by date, custodian, or subject. These
   requests invite objection and impose unnecessary burden; narrow before serving.

5. **Compound interrogatories** — Bundling multiple discrete questions into one ("Did you
   perform the contract AND did you suffer damages AND did you mitigate?") rather than
   separating into individual interrogatories. Each discrete sub-part counts against the
   25-question limit and can be objected to as compound.

6. **Interrogatories calling for legal conclusions** — Asking "Did defendant breach the
   contract?" instead of "Describe all actions taken by defendant regarding [obligation]."
   FRCP 33(a)(2) permits questions on law-to-fact application only when they can be
   answered by factual explanation, not pure legal assertion.

7. **No fallback strategy** — Serving requests with no narrowed alternative in reserve.
   Every borderline request should have a narrowed fallback ready for the meet-and-confer
   so you can offer a reasonable compromise rather than litigating every request.

8. **Unverified case law citations in objections** — Citing decisions from memory to
   support or oppose proportionality without verifying citation accuracy. Discovery
   correspondence is read by opposing counsel who will verify; a fabricated or miscited
   case destroys credibility and risks Rule 11 sanctions.

9. **Ignoring privilege risk in RFPs** — Requesting "all communications regarding [topic]"
   without acknowledging that some will be privileged and requiring a privilege log. This
   creates disputes and delays production of the non-privileged materials.

10. **Vague ESI requests** — Not specifying custodians, search terms, date ranges, or
    production format for electronically stored information. Vague ESI requests invite
    disputes and inadequate productions; the Sedona Principles and local ESI standing
    orders require specificity.

11. **No meet-and-confer certification plan** — Filing a motion to compel without first
    conferring in good faith as required by FRCP 37(a)(1). Courts deny motions to compel
    that lack an adequate meet-and-confer certification, imposing delay and costs.

12. **Treating RFAs as discovery devices** — Using requests for admission to seek factual
    narrative the opponent must explain (that is an interrogatory's role). RFAs should
    state a single discrete fact or ask about a document's genuineness — not require
    narrative explanation.

13. **Over-serving in small cases** — Serving 100 interrogatories and 200 RFPs in a case
    worth $100,000. Courts view discovery volume in proportion to case value; overburdening
    a small case will generate protective orders and sanction risk.

14. **No follow-up strategy** — Asking interrogatory #5 but not planning the RFP that
    will follow if the answer identifies key custodians, or the deposition that will test
    the interrogatory answer. Discovery is strategic and sequential; each phase informs
    the next.

15. **Importing template language verbatim** — Using a form discovery request without
    adapting to the specific case, parties, and claims. Form requests include irrelevant
    topics, omit case-specific needs, and signal to opposing counsel that the requests
    are not well thought out.

16. **Responding incompletely under objection** — Objecting to a request and then
    producing nothing — including the non-objectionable portions. Post-2015 FRCP 34 requires
    the responding party to state whether production is being withheld and what non-
    objectionable materials will be produced.

17. **Missed ESI preservation obligations** — Failing to issue a litigation hold before
    serving or responding to discovery, or failing to instruct custodians to preserve
    relevant materials. Spoliation sanctions (adverse inference instructions, case
    dispositive sanctions) are the most dangerous litigation risk in discovery.

18. **Assuming good-faith compliance** — Drafting requests without a verification mechanism
    and accepting incomplete responses without follow-up. Every discovery response should
    be cross-referenced against known documents (from initial disclosures, privilege log,
    etc.) to identify gaps.

19. **No privilege log format in requests** — Not specifying what format the privilege
    log must take when requesting production. An underspecified privilege log creates
    challenges and does not meet FRCP 26(b)(5)(A); specify required fields in the
    definitions section.

20. **Single-pass drafting** — Writing the discovery package in a single pass without
    reviewing the case file holistically. Interrogatory #12 may answer interrogatory #5,
    making #5 redundant; RFP #8 may seek the same documents as RFP #15 from a different
    angle, wasting the interrogatory count or creating inconsistencies.

---

## Writing Standards

Apply plain-language discipline to all discovery output:

**For requests (served on opposing party):**

- Plain language. Avoid unnecessary legal jargon.
- Define all terms in a definitions section — "Document," "Communication," "ESI," and
  key proper names
- Each request: one instruction per request sentence. No compound requests.
- Active voice: "Describe all steps taken by Defendant" not "All steps taken by Defendant
  shall be described"
- Specific scope: "from January 1, 2022 through the date of this Request" not "at all
  relevant times"

**For objections and responses (served on opponent):**

- Each objection: name the specific rule, explain how the request violates it
- State explicitly whether production is being withheld and, if so, on what grounds
- Reserve rights to supplement without committing to indefinite supplementation
- Do not include the prohibited phrase "not reasonably calculated to lead to admissible
  evidence" in objections

**Quality gates before delivery:**

1. Has each request been checked against the 25-interrogatory limit (counting subparts)?
2. Is every claim backed by a cited rule or authority (or marked [VERIFY])?
3. Have boilerplate objections been replaced with specific, articulable grounds?
4. Is the ESI request specific enough to avoid a "format not specified" dispute?
5. Is every privileged withholding logged in a privilege log?
6. Could any request be narrowed to reduce proportionality objection risk without
   sacrificing essential information?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 3, search for proportionality precedent in the governing district
- Search for privilege and work-product precedent for the relevant circuit
- Verify ESI standing orders from the assigned judge
- Search for sanctions decisions involving boilerplate objections in this court
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with FRCP 26-37 general knowledge but flag that local precedent is unverified
- Focus the discovery package on structural completeness and proportionality analysis
  rather than jurisdiction-specific case law support

---

## Output Format Template

Structure the final deliverable as:

```markdown
# Discovery Package — [Matter Name]

**Case Type**: [Commercial / Employment / IP / Personal Injury / Patent / Other]
**Mode**: [Propounding / Responding / Both]
**Governing Rules**: [FRCP 26-37 / State rules / Local rules]
**Discovery Stage**: [Initial / Mid-stream / Late]
**Date Prepared**: [date]
**Review Basis**: [Case-type template / Custom]

---

## Proportionality Overview

**Case value tier**: [High / Mid-size / Small / Very small]
**Proportionality assessment**:

- GREEN (proportional): [N] request categories
- YELLOW (borderline): [N] request categories — fallbacks prepared for each
- RED (disproportionate — narrowed before serving): [N] request categories — see fallbacks

---

## Definitions

All defined terms used in the requests below:

- **"Document"** means any writing, recording, or graphic matter, whether in paper or
  electronic form, including emails, text messages, chat logs, voicemails, audio/video
  recordings, and metadata.
- **"Communication"** means any oral or written exchange of information, in any medium.
- **"ESI"** means electronically stored information as defined in FRCP 34(a)(1).
- **"You" / "Your"** means [Responding Party] and all officers, directors, employees,
  agents, and persons acting on its behalf.
- **"[Key Term 1]"** means [definition relevant to the case].
- [Additional case-specific definitions]

---

## Interrogatories

[Set organized by category per the case-type template]

### Category 1: [e.g., Liability — Timeline and Actors]

**Purpose**: Establish who knew what and when — foundational to liability
**Proportionality**: GREEN

**INTERROGATORY NO. 1**: [Full question text]
**Proportionality**: GREEN
**Anticipated Objection**: None anticipated / [specific objection and counter-argument]
**Confidence**: High

[Repeat for each interrogatory]

---

## Requests for Production (RFPs)

[Set organized by document category per the case-type template]

### Document Category 1: [e.g., Contract and Negotiation Documents]

**Purpose**: Obtain foundational contract documents and negotiate-down history
**Proportionality**: GREEN
**Privilege Screening**: Low (pre-contract negotiation communications generally not privileged)

**REQUEST FOR PRODUCTION NO. 1**: [Full request text]
**ESI Considerations**: [Custodians, repositories, format]
**Anticipated Objection**: None anticipated / [specific objection and counter-argument]
**Confidence**: High

[Repeat for each RFP]

---

## Requests for Admission (RFAs)

[Set organized by legal element per the case-type template]

### Element: [e.g., Contract Authenticity]

**Purpose**: Authenticate foundational documents; narrow facts for trial
**Strategic Value**: High

**REQUEST FOR ADMISSION NO. 1**: [Full request text]
**Anticipated Response**: Admit
**If Denied**: [Follow-up interrogatory or deposition topic]
**FRCP 37(c)(2) potential**: [Yes / No]
**Confidence**: Definite

[Repeat for each RFA]

---

## Objection & Response Guidance

[For Responding mode — objection analysis per request received]

---

## Privilege Log Template

| Doc No. | Type    | Date   | Author          | Recipients         | Subject (No Privilege Content)   | Privilege Asserted |
| ------- | ------- | ------ | --------------- | ------------------ | -------------------------------- | ------------------ |
| [1]     | [Email] | [date] | [Author, Title] | [Recipient, Title] | [General subject — no substance] | [AC / WP / CI]     |

---

## Meet-and-Confer Script

[Template per Step 10]

---

## Next Steps

[Specific actions, owners, and deadlines]

- [ ] Finalize definitions section with case-specific terms
- [ ] Confirm interrogatory count against prior sets (25-limit)
- [ ] Verify jurisdiction-specific rules (interrogatory limits, local ESI order)
- [ ] Have experienced litigation counsel review before serving
- [ ] Calendar response deadline (30 days from service) [FRCP 33, 34, 36]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

This skill is US federal primary. To create a jurisdiction-specific variant:

1. **State court variant**: Replace FRCP rule references with state equivalents; adjust
   interrogatory limits (California 35, Texas "Level" system, New York 25); verify
   proportionality standards under state rules

2. **England & Wales variant**: Replace interrogatories with witness statements (CPR Part
   35); replace RFPs with CPR Part 31 standard disclosure lists; preserve specific
   disclosure requests for supplemental requests

3. **Canada variant**: Apply Federal Courts Rules or provincial rules as applicable;
   no direct interrogatory equivalent in some provinces (discovery is deposition-based);
   Ontario Rules of Civil Procedure Rr. 30-31 govern document discovery

4. **Patent litigation overlay**: Add Local Patent Rules (LPRs) for the governing district;
   incorporate mandatory infringement/invalidity contention timelines; adjust claim
   construction discovery to Markman hearing schedule

When creating a jurisdiction-specific variant, replace all [JURISDICTION-SPECIFIC] markers
with verified local content and update the frontmatter name.

---

## Provenance

Created by Legalcode (2026-03-01). Legalcode original synthesis. Calibrated against the
`legalcode-contract-review` gold standard and informed by structural analysis of
`legalcode-privilege-review`, `legalcode-early-case-assessment`, and `legalcode-brief-analyzer`.
Legal framework based on FRCP 26-37 (2015 amendments), proportionality doctrine, work-product
doctrine, attorney-client privilege, and FRE 502. Case-type templates informed by federal
civil discovery practice in commercial, employment, IP, and personal injury litigation.
Research sources: US federal rules (law.cornell.edu FRCP); federal court ESI standing orders;
Sedona Principles (3d ed.); Fischer v. Forrest (SDNY 2017) on boilerplate objections; EDRM
discovery standards. All legal authority cited with [VERIFY] except settled black-letter FRCP text.
