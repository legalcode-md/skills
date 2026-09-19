---
name: legalcode-discovery-response-drafter
description: Draft defensible responses to interrogatories, requests for production (RFPs), and requests
  for admission (RFAs) with specific objections, substantive answers, and privilege assertions. Use when
  responding to received discovery requests in federal or state civil litigation, drafting specific objections
  with identifying particularity, asserting attorney-client privilege or work-product protection with
  compliant log entries, arguing proportionality as a limiting principle, or preparing meet-and-confer
  positions on discovery disputes.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Draft defensible responses to interrogatories, requests for production (RFPs), and requests for admission (RFAs) with specific objections, substantive answers, and privilege assertions. Covers FRCP 26(b)(1) proportionality defense, Rule 34(b)(2) objection-specificity requirements, FRCP 26(b)(5) privilege log drafting, FRE 502 clawback integration, and Rule 26(e) supplement obligations. Use when responding to received discovery requests in federal or state civil litigation, drafting specific objections with identifying particularity, asserting attorney-client privilege or work-product protection with compliant log entries, arguing proportionality as a limiting principle, or preparing meet-and-confer positions on discovery disputes. Generates interrogatory answers (including Rule 33(d) business-records option), RFP written objection and production statements, RFA admissions/denials/qualified denials, privilege logs, and supplementation schedules. US federal primary (FRCP 26-37) with state rules for California (CCP 2030-2033), New York (CPLR 3130-3133), Texas (TRCP 190-199), Florida (FRCP 1.340-1.370), and Illinois (Ill. S. Ct. Rules 213-214).


# Legalcode Discovery Response Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted civil discovery response
> drafting. It does not constitute legal advice. All outputs must be reviewed by a qualified
> legal professional licensed in the governing jurisdiction before service or filing. Discovery
> responses have tactical, strategic, and ethical dimensions that require experienced counsel
> review. Procedural rules change; verify current applicability before relying on any provision.
> Statutory, case law, and local-rule references cited from memory carry hallucination risk —
> verify against authoritative sources before relying on them. Inadequate privilege assertions
> or overly broad responses can result in waiver, sanctions, or adverse inferences.

## Purpose and Scope

This skill drafts complete, rule-compliant responses to civil discovery requests on the **responding
party's side**. It focuses on the full responding workflow — from reading incoming requests,
through drafting specific objections and substantive answers, to building privilege logs and
preparing supplementation schedules.

**Covers:**

- Interrogatory responses (FRCP 33): substantive answers, Rule 33(d) business-records option,
  contention response strategy, and objections with specificity
- RFP responses (FRCP 34): objection statements, production commitments, scope-of-search
  descriptions, ESI format objections, and withholding statements
- RFA responses (FRCP 36): admissions, denials, qualified denials, and lack-of-knowledge
  responses with proper use of Rule 36(a)(4)
- Privilege assertion (FRCP 26(b)(5)): document-by-document and categorical privilege log
  drafting; attorney-client privilege, work-product doctrine, common-interest/joint-defense
- Proportionality defense (FRCP 26(b)(1)): six-factor proportionality analysis as applied to
  incoming requests; burden-quantification support; cost-shifting arguments
- Boilerplate avoidance: post-2015 specificity requirements under Rule 34(b)(2); Fischer v.
  Forrest compliance; distinguishing proper objections from sanctionable boilerplate
- FRE 502(d) clawback agreement drafting and inadvertent-disclosure procedures
- Rule 26(e) supplementation obligations: timing, trigger events, and workflow
- State rule variants: California, New York, Texas, Florida, Illinois

**Does not:**

- Draft discovery requests to serve on the opponent (see `legalcode-discovery-request-drafter`)
- Handle criminal discovery (Brady, Jencks Act, state equivalents)
- Cover international discovery (Hague Evidence Convention, cross-border GDPR constraints)
- Advise on strategic decisions about which issues to contest at trial
- Replace counsel judgment on final production decisions

**Related skills:** `legalcode-privilege-review` (deep privilege analysis and privilege-log
production), `legalcode-discovery-request-drafter` (drafting requests and anticipating
objections), `legalcode-early-case-assessment` (discovery budget and proportionality context),
`legalcode-tar-review-protocol` (technology-assisted review for large document sets)

---

## Jurisdiction and Governing Law

This skill is US federal-primary, calibrated to the **Federal Rules of Civil Procedure (FRCP)**
as amended through the 2015 amendments (effective December 1, 2015) and subsequent changes.

[JURISDICTION-SPECIFIC] Confirm and apply the correct rule set:

- **US Federal**: FRCP 26-37; FRE 501-502 (privilege); governing local rules of the assigned district
- **California**: CCP §§ 2030.010-2030.410 (interrogatories), 2031.010-2031.510 (inspection demands),
  2033.010-2033.420 (RFAs); verified responses required; separate statement on motions to compel
- **New York**: CPLR §§ 3101, 3120, 3123, 3130-3133; 25 interrogatory limit; full-disclosure standard
- **Texas**: TRCP 190 (discovery levels 1/2/3), 197 (interrogatories — 15 limit), 198 (RFAs),
  196 (inspection requests)
- **Florida**: Fla. R. Civ. P. 1.340 (interrogatories), 1.350 (production), 1.370 (admissions)
- **Illinois**: Ill. S. Ct. Rule 213 (interrogatories), 214 (inspection), 216 (admissions)

[JURISDICTION-SPECIFIC] Always verify before serving responses:

- Interrogatory limits and whether subparts count separately
- Verification/oath requirements for interrogatory responses
- Service deadlines and extension mechanics
- Local court rules on format, filing, and discovery dispute resolution
- Assigned judge's standing orders on discovery (often posted on court website)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. The workflow pauses
and asks when:

- The responding strategy changes materially depending on case context
- A request is objectionable on multiple independent grounds and the strongest one must be chosen
- Privilege exposure requires case-specific legal judgment
- Proportionality arguments depend on facts the user must supply (cost estimates, document volume)
- State vs. federal rules apply with different response requirements

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

### Step 1: Accept the Discovery Package

Accept the received discovery requests in any format:

- **Document file**: PDF, DOCX, or scanned image of the discovery requests
- **Pasted text**: Discovery request text copied directly into the conversation
- **Description only**: Summary of what was received (if full text unavailable)

If only a case description is provided (e.g., "I need to respond to employment discovery"),
proceed to Step 2 to gather context, then build responses from the case-type template.

### Step 2: Gather Context

**⟁ CLARIFY** — Before drafting any response, ask (skip questions already answered):

1. **Governing jurisdiction and rules**:
   - Options: US Federal (FRCP 26-37) / California (CCP 2030-2033) / New York (CPLR) /
     Texas (TRCP) / Florida / Illinois / Other (specify)
   - _Why this matters_: Response format, verification requirements, interrogatory limits,
     and RFA mechanics differ substantially across jurisdictions.

2. **Case type**:
   - Options: Commercial/contract / Employment / IP (patent/trade secret/copyright) / Personal
     injury / Antitrust / Real estate / Other (describe)
   - _Why this matters_: Determines which issue-specific objections apply and which documents
     are likely privileged or protected.

3. **Discovery stage**:
   - Options: Initial (first-set response, early in case) / Mid-stream (supplemental or
     follow-up set) / Pre-trial (final cleanup, contention responses) / Post-judgment
   - _Why this matters_: Contention interrogatory timing, supplementation obligations, and
     proportionality arguments shift by stage.

4. **Response posture**:
   - Options: Cooperative (produce what you can, object only where necessary) / Defensive
     (assert all available objections, narrow scope aggressively) / Protective-order track
     (seek court order on one or more requests before responding)
   - _Why this matters_: Determines how much to qualify responses vs. produce outright.

5. **Privilege profile**:
   - Options: Heavy privilege exposure (legal department heavily involved) / Moderate
     (some in-house counsel involvement) / Minimal (few or no privileged documents)
   - _Why this matters_: Scales the depth of privilege log analysis and privilege assertions.

6. **Proportionality constraints**:
   - Inputs: Estimated number of responsive documents, estimated review cost, case value
   - _Why this matters_: Quantifying burden is essential for proportionality objections under
     FRCP 26(b)(1) — a vague "unduly burdensome" assertion without cost data is a losing position.

7. **Response deadline**:
   - Input: Date discovery was served, date response is due
   - _Why this matters_: Identifies whether an extension is needed before any other step.

If the user provides partial context, proceed with stated assumptions and flag them (e.g.,
"Assuming FRCP governs — confirm if state rules apply instead").

### Step 3: Load Legal Authority for the Governing Forum

Identify the applicable procedural rules and any standing orders. Use **legalcode-mcp** when
available to build a working reference:

1. **Identify governing rules**: FRCP vs. state CCP/CPLR/TRCP; assigned district's local rules;
   assigned judge's standing orders on discovery disputes and ESI.

2. **Search legalcode-mcp** for:
   - Recent decisions from the governing district on boilerplate objections and sanctions
   - Controlling proportionality precedent in the district (post-2015 amendments)
   - Privilege precedent specific to the forum (attorney-client, work product scope)
   - Any standing ESI orders from the assigned judge

3. **Save results** to `/tmp/legalcode-response-authority.md`:

   ```markdown
   # Discovery Response Authority — [Matter Name]

   ## Governing Rules: [FRCP / State rules / Local rules]

   ## Court: [District/Division]

   ## Assigned Judge: [Name, if known]

   ### Proportionality Precedent

   - [Case, citation, key holding on FRCP 26(b)(1)]

   ### Boilerplate Sanctions Precedent

   - [Case, citation — e.g., Fischer v. Forrest]

   ### Privilege Scope

   - [Case, citation, privilege holding relevant to this matter]

   ### Judge-Specific Standing Orders

   - [Standing order title and key requirements]
   ```

**If legalcode-mcp is not connected:**

- Proceed with FRCP general knowledge and any forum-specific research via web search
- Mark all case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`

**⟁ CLARIFY** — If any of the following apply, ask the user before proceeding:

- **No scheduling order or court information provided**: Ask whether discovery is open, the
  cutoff date, and whether any orders limit scope or timing
- **State court but rules not confirmed**: Confirm which state rules and which county/district
- **Known judge with particular discovery preferences**: Ask if the user has reviewed the
  assigned judge's standing orders (many impose meet-and-confer obligations before objections)

### Step 4: Analyze Incoming Requests

For each incoming request, apply the **Four-Gate Analysis** before drafting any response:

| Gate                        | Question                                                       | If Yes                                    | If No                                                                             |
| --------------------------- | -------------------------------------------------------------- | ----------------------------------------- | --------------------------------------------------------------------------------- |
| **Gate 1: Relevance**       | Is this request relevant to any claim or defense?              | Proceed to Gate 2                         | Assert relevance objection; still answer if any portion is relevant               |
| **Gate 2: Privilege**       | Does any responsive material implicate privilege?              | Prepare privilege assertion and log entry | Proceed to Gate 3                                                                 |
| **Gate 3: Proportionality** | Is the burden proportional to the benefit under FRCP 26(b)(1)? | Proceed to Gate 4                         | Assert proportionality objection with specific burden estimate                    |
| **Gate 4: Specificity**     | Is the request defined with "reasonable particularity"?        | Draft response                            | Assert vague/ambiguous objection with identification of which term is problematic |

**Output of Gate Analysis**: For each request, produce a pre-response memo:

```
Request No. [X] — Pre-Response Analysis
Gate 1 (Relevance): [PASS / PARTIAL / FAIL — reasoning]
Gate 2 (Privilege): [NONE / PARTIAL — describe scope] / [FULL — privilege basis]
Gate 3 (Proportionality): [PASS / MARGINAL / FAIL — burden estimate]
Gate 4 (Specificity): [CLEAR / AMBIGUOUS — identify problematic terms]

Proposed response type: [Full answer / Qualified answer + objection / Objection only /
                          Privilege only / Insufficient knowledge]
Confidence: [Definite / High / Probable / Possible / Unlikely]
```

### Step 5: Conduct Proportionality Defense Analysis

For any request where Gate 3 raised a concern, conduct the full **six-factor proportionality
analysis** under FRCP 26(b)(1). This is the factual predicate for any proportionality objection.

**The six proportionality factors:**

| Factor                                              | Responding Party's Burden                                                                                                                                                    |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Importance of issues at stake**                | Analyze whether these issues are actually outcome-determinative or peripheral. Peripheral issues get narrower discovery.                                                     |
| **2. Amount in controversy**                        | Quantify the case value. A small-value case cannot support expensive discovery. Compute the ratio of estimated response cost to case value.                                  |
| **3. Parties' relative access to information**      | Does the propounding party already have this information or could they get it from another source? Assess duplicativeness.                                                   |
| **4. Parties' relative resources**                  | Compare financial capacity. A large company responding to an individual plaintiff has different obligations than a small business responding to a large corporate plaintiff. |
| **5. Importance of discovery in resolving issues**  | How much will this specific information actually affect case outcome? If the issue could be resolved by stipulation or other means, argue accordingly.                       |
| **6. Burden or expense relative to likely benefit** | Estimate: (a) number of custodians, (b) estimated document volume, (c) review cost per document, (d) total estimated cost. Compare to the likely probative value.            |

**Proportionality Classification for Each Request:**

| Classification | Meaning                                                                                | Recommended Response                                                                   |
| -------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **GREEN**      | All six factors favor responding                                                       | Answer fully; no proportionality objection                                             |
| **YELLOW**     | Mixed — some factors favor, others cut against                                         | Answer with scope qualifier; propose narrowing in meet-and-confer                      |
| **RED**        | Disproportionate — factors predominantly cut against                                   | Assert specific proportionality objection with burden data; offer narrowed alternative |
| **CRITICAL**   | Facially disproportionate (e.g., all documents from beginning of time for a $50K case) | Seek protective order before responding; draft Rule 26(c)(1) motion framework          |

**⟁ CLARIFY** — For RED or CRITICAL requests, ask:

- "Can you estimate the number of custodians, documents, and review cost for this category?"
- "Is there a narrower version of this request you would be willing to respond to?"

### Step 6: Draft Interrogatory Responses (FRCP Rule 33)

For each received interrogatory, draft a complete response in this sequence:

1. Objections (if any) stated with specificity
2. Subject to any objections, the substantive answer
3. Rule 33(d) business-records designation (if applicable)
4. Privilege assertion (if applicable)

#### Interrogatory Response Format

```
RESPONSE TO INTERROGATORY NO. [X]:

[Objections, if any — each stated separately with specific basis:]
Objection 1: [Objection type]. [Defendant/Plaintiff] objects to this interrogatory on the
ground that [specific reason: e.g., it is compound in that it asks two discrete questions —
describe what happened AND identify all witnesses present — which would exceed the interrogatory
limit if counted separately. Subject to and without waiving this objection, Responding Party
responds as follows:]

[OR:]
Objection 1: [Responding Party] objects to this interrogatory on the ground that [specific
part of the request] is vague and ambiguous as used in this context. [Responding Party]
interprets [term] to mean [interpretation] and responds on that basis.

[Substantive answer, subject to objections:]
Subject to the foregoing objections and without waiving the same, [Responding Party] responds
as follows: [Full narrative answer — identify all persons, describe all facts, provide all
dates with specificity. Do not hedge with "to the best of my recollection" unless genuinely
uncertain.]

[Rule 33(d) option, if applicable:]
Alternatively, pursuant to FRCP 33(d), the answer to this interrogatory may be derived or
ascertained from the business records of [Responding Party], specifically [identify records
with reasonable particularity: e.g., "the Sales Transaction Database for the period January
1, 2022 through December 31, 2023, which will be produced as Bates Nos. [XXX-YYY]"]. The
burden of deriving or ascertaining the answer is substantially the same for both parties.
[Responding Party] will provide [Propounding Party] with reasonable access to and opportunity
to examine, audit, or inspect these records.

[Privilege assertion, if applicable:]
[Responding Party] further objects to this interrogatory to the extent it seeks information
protected by the attorney-client privilege or the work-product doctrine. Any withheld
information is identified in the Privilege Log served herewith or to be served within [X] days.

Verification: [Include oath/verification language per local rules or state requirements]
```

#### Interrogatory Answer Quality Checklist

Before finalizing each interrogatory response:

- [ ] Is every objection stated with the specific basis (not boilerplate)?
- [ ] Is there a "subject to and without waiving" bridge if answering despite an objection?
- [ ] Does the answer actually respond to what was asked (not just related information)?
- [ ] Are all persons identified by name and role (not "the relevant employees")?
- [ ] Are all dates specified (not "sometime in 2023")?
- [ ] If using Rule 33(d), are the specific records identified with enough particularity?
- [ ] If asserting privilege, is the withheld information logged in the privilege log?
- [ ] Has the answer been reviewed for accuracy by someone with actual knowledge?
- [ ] Does the client need to verify (sign) this response?

#### Recognized Interrogatory Objections (With Required Specificity)

| Objection                                  | Required Specificity                                                                                              | Prohibited Boilerplate                                                |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **Vague and ambiguous**                    | Identify the specific word or phrase that is ambiguous; state how you interpret it                                | "Interrogatory No. X is vague and ambiguous" (without identification) |
| **Overbroad**                              | Identify the specific dimension of overbreadth (time period, subject matter, identity); propose a narrowing       | "This interrogatory is overbroad"                                     |
| **Unduly burdensome**                      | State estimated number of hours, documents, or cost to respond                                                    | "This interrogatory is unduly burdensome and oppressive"              |
| **Not proportional**                       | Apply each FRCP 26(b)(1) factor; quantify cost-to-benefit ratio                                                   | "Not proportional to the needs of the case"                           |
| **Attorney-client privilege**              | State that privileged information is being withheld; identify in privilege log                                    | "Objection to the extent privileged" (without logging)                |
| **Work-product doctrine**                  | Distinguish ordinary from opinion work product; log withheld items                                                | "Protected as attorney work product" (without specificity)            |
| **Compound**                               | Identify the separate discrete questions within the interrogatory; note how many interrogatory slots they consume | "This interrogatory is compound"                                      |
| **Calls for legal conclusion**             | Identify the specific legal term or conclusion being sought; offer to answer the factual predicate                | "Calls for a legal conclusion"                                        |
| **Not in possession, custody, or control** | State what you do control; explain what you do not                                                                | "Defendant does not have possession of this information"              |
| **Exceeds interrogatory limit**            | Count all prior interrogatories including subparts; note how this one exceeds the limit                           | "Exceeds the limit"                                                   |
| **Already produced**                       | Identify by Bates number or production date the prior production                                                  | "Already produced"                                                    |

#### Contention Interrogatory Strategy

**⟁ CLARIFY** — For contention interrogatories asking you to state the facts supporting
each defense or denial, ask the user:

- "Are we still in early discovery or is fact discovery closing? Contention interrogatories
  served early can properly be deferred until close of fact discovery." [FRCP 33(a)(2)]
- "Does the client want to answer fully now or seek a court order deferring the contention
  response until the close of fact discovery?"

If deferring: "Responding Party objects to this contention interrogatory on the ground that
it has been served before the close of fact discovery and is premature. Responding Party
reserves the right to supplement this response pursuant to FRCP 26(e) at the close of
fact discovery. Subject to this objection, Responding Party currently contends [X]."

### Step 7: Draft RFP Responses (FRCP Rule 34)

For each received RFP, draft a complete response statement — including objections, the
scope of any agreement to produce, the scope of any withholding, and the production timeline.

#### RFP Response Format (Post-2015 Amendment Requirements)

```
RESPONSE TO REQUEST FOR PRODUCTION NO. [X]:

[Objections, each stated specifically:]
Objection 1: [Responding Party] objects to this request on the ground that [specific basis].
[If objecting and withholding:] Documents responsive to this request are being withheld solely
on the basis of this objection.

[OR:]
[If objecting but still producing what is not objectionable:]
[Responding Party] objects to this request to the extent it seeks [specify the objectionable
scope] on the ground that [specific basis]. [Responding Party] will respond to the
non-objectionable portion of this request as follows:

[Production commitment:]
Subject to the foregoing objections and without waiving same, [Responding Party] agrees to
produce responsive, non-privileged documents [in existence / in its possession, custody, or
control] that [describe the narrowed scope if applicable], for the period [date range], in
[format: e.g., "PDF with load file," "native format with metadata," "TIFF with extracted
text"], on a rolling basis beginning [date] and concluding by [date].

[Withholding statement (required under Rule 34(b)(2)(C)):]
[Responding Party] is withholding [category description] on the ground that [objection basis].

[Privilege assertion:]
Documents withheld on the basis of attorney-client privilege or work-product doctrine are
identified in the Privilege Log served herewith [or: to be served by [date]].

[ESI format statement, if applicable:]
[Responding Party] will produce ESI in [format]. If [Propounding Party] requires a different
format, please raise this issue at the parties' next meet-and-confer.
```

#### Rule 34(b)(2) Mandatory Requirements Post-2015

These are non-negotiable after the 2015 amendments — failure creates sanctions exposure:

| Requirement                                             | What It Means                                                                                                                         | Common Violation                                                                 |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Objections stated with specificity**                  | Name the rule; explain how this request violates it for this specific category                                                        | "Objection: overbroad, burdensome, and irrelevant" (boilerplate, no specificity) |
| **State whether any responsive materials are withheld** | Affirmatively state: "documents are being withheld on the basis of this objection"                                                    | Asserting objection without disclosing whether production is complete or partial |
| **Respond to non-objectionable portions**               | Must produce what is not objected to, even if objecting to part of a compound request                                                 | Using an objection to withhold everything, including non-objectionable documents |
| **Prohibited phrase**                                   | "Not reasonably calculated to lead to admissible evidence" was **deleted** from FRCP 26(b)(1) in 2015; using it is facially defective | Any response containing this outdated phrase                                     |

#### ESI-Specific Objection Framework

For requests implicating large volumes of electronically stored information:

| ESI Issue                      | Objection Basis                                                                                                                  | Required Specificity                                                                                                                       |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Format not specified**       | [Responding Party] will produce in [format ordinarily maintained] unless a specific format is requested per Rule 34(b)(2)(E)(ii) | Identify the format; state that native format preserves metadata                                                                           |
| **Inaccessible data**          | FRCP 26(b)(2)(B) allows limitation on production of ESI not reasonably accessible due to undue burden or cost                    | Identify specifically what data is not accessible (e.g., "legacy backup tapes from server retired in 2018") and estimate cost of retrieval |
| **Metadata preservation**      | If native files are requested, confirm metadata is preserved; if TIFF, confirm text extraction approach                          | Describe the production workflow including metadata fields to be included in load file                                                     |
| **Search term disputes**       | If search terms are proposed, reserve right to negotiate scope                                                                   | Propose alternative terms or use FRCP 26(f) conference to agree                                                                            |
| **Archival/disaster recovery** | FRCP 26(b)(2)(B) — data existing only in disaster recovery or archival formats is presumptively not accessible                   | Identify systems, estimate cost, and offer cost-shifting discussion                                                                        |

**⟁ CLARIFY** — For ESI-heavy requests, ask the user:

- "Has the court entered an ESI protocol or have the parties agreed on custodians and search terms?"
- "Are there any backup tape, legacy system, or mobile device repositories that are particularly
  expensive to collect from? I need to quantify these for proportionality objections."
- "Has a Rule 502(d) non-waiver order been entered? If not, should we propose one before production?"

#### Boilerplate vs. Proper Objection: Key Cases

The following cases establish what courts will strike as improper:

- **Fischer v. Forrest, 2017 WL 773694 (S.D.N.Y. 2017)** [VERIFY citation]: Struck all
  general objections as impermissible boilerplate; required specific objections to each request
  explaining the particular basis and whether documents were withheld.
- **Hager v. Graham, 267 F.R.D. 486 (N.D. W. Va. 2010)** [VERIFY]: Long-standing
  authority rejecting boilerplate objections as "ineffective" and potentially sanctionable.
- **Liguria Foods v. Griffith Laboratories, 320 F.R.D. 168 (N.D. Iowa 2017)** [VERIFY]:
  Imposed sanctions where party asserted a long list of boilerplate objections to every request
  without ever specifying which applied or why.
- Post-2015 majority rule: Courts regularly impose sanctions including fee-shifting, adverse
  inferences, and preclusion for repetitive, non-specific objections [VERIFY currency in
  current district].

### Step 8: Draft RFA Responses (FRCP Rule 36)

For each received RFA, draft one of four response types:

| Response Type                   | When to Use                                              | Legal Standard                                                                                  |
| ------------------------------- | -------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Admit**                       | The matter is true and undisputed                        | Binding admission; cannot be withdrawn without court permission                                 |
| **Deny**                        | The matter is untrue (or you dispute it in good faith)   | Must be a genuine, good-faith denial — not a strategy to avoid admitting an inconvenient truth  |
| **Qualified denial**            | The matter is true in part but not as stated             | Admit the portion that is true; specifically deny the portion that is not                       |
| **Lack sufficient information** | After reasonable inquiry, genuinely cannot admit or deny | Must state that inquiry was made and information is insufficient — cannot be used as an evasion |

#### RFA Response Format

```
RESPONSE TO REQUEST FOR ADMISSION NO. [X]:

[Admit:] Admitted.

[Deny:] Denied. [If denying a fact that is important, add a one-sentence explanation, though
explanation is not required. Strategic note: unexplained denials can be challenged at
meet-and-confer and may lead to motions for fees under FRCP 37(c)(2) if the denied fact
is ultimately proven at trial.]

[Qualified denial:] [Responding Party] admits that [portion that is true]. [Responding Party]
denies the remainder of this request on the grounds that [specific basis for denial — e.g.,
the date stated is incorrect; the document referenced is a draft, not the final agreement].

[Lack sufficient information:] After making reasonable inquiry, the information known to or
readily obtainable by [Responding Party] is insufficient to enable [Responding Party] to
admit or deny this request. Specifically, [describe what inquiry was made and why it was
insufficient — e.g., "the person with direct knowledge of this event is no longer employed
by Responding Party and their former supervisor has no recollection of the specific date"].

[Objection only:] [Responding Party] objects to this request on the ground that [specific
basis: e.g., "it calls for a legal conclusion as to whether the parties were in an agency
relationship, which is a legal determination for the trier of fact"]. Subject to and without
waiving this objection, [Responding Party] [admits / denies / states that it lacks sufficient
information].
```

#### RFA Response Quality Checklist

- [ ] Is the denial a genuine good-faith denial (not strategic evasion)?
- [ ] If using "lack sufficient information," is there a description of the inquiry made?
- [ ] Has the risk of deemed admission been explained to the client (failure to respond = admission)?
- [ ] Has the client been informed that admissions are binding for this case only (but can be used at trial)?
- [ ] For RFAs about document authenticity: has the document been reviewed before admitting or denying?
- [ ] Has the FRCP 37(c)(2) cost-shifting risk been considered if denying facts that will be proven?
- [ ] Are any objections stated with specificity (not boilerplate)?

#### Deemed Admission Avoidance Protocol

A party that fails to respond to RFAs within 30 days is **deemed to have admitted** all matters
in the requests [FRCP 36(a)(3)]. This can be case-dispositive.

If a response deadline has passed or is at risk:

1. Immediately confirm with the user whether any response has been served
2. If response is overdue: draft emergency motion to withdraw deemed admissions under FRCP 36(b)
   [court must find that withdrawal serves the presentation of the merits and no prejudice to the
   propounding party would result]
3. Serve responses immediately alongside the motion
4. Do not delay — courts are split on how long after the deadline a motion to withdraw will be granted

### Step 9: Build the Privilege Log

For every withheld or redacted document or communication, prepare a privilege log entry compliant
with FRCP 26(b)(5)(A).

#### FRCP 26(b)(5)(A) Minimum Requirements

Each privilege log entry must:

1. **Identify the type of document** (e.g., email, memorandum, draft contract, text message)
2. **State the date** of creation
3. **Identify the author(s)** and their roles and attorney/client relationship
4. **Identify the recipient(s)** and their roles and attorney/client relationship
5. **Provide a general subject matter description** that does not reveal the privileged content
6. **Identify the privilege basis** (attorney-client privilege, work-product doctrine, or both)

#### Privilege Log Entry Format

```
| Log ID | Doc ID/Bates | Date | Type | Author(s) [Role] | Recipient(s) [Role] | Subject Matter | Privilege Basis | Confidence |
|--------|-------------|------|------|-----------------|---------------------|----------------|-----------------|-----------|
| PL-001 | [e.g., Email] | 2023-04-15 | Email | Jane Smith [GC, ABC Corp.] | Bob Jones [CEO, ABC Corp.]; Tom Lee [Outside Counsel, Acme LLP] | Request for legal advice regarding [regulatory compliance matter] — attorney communication | AC, WP | High |
```

#### Attorney-Client Privilege — Establishing Each Element

To withhold on attorney-client grounds, confirm all four elements are present:

| Element                                          | Analysis Question                                                                         | Red Flag                                                                                       |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **1. Communication**                             | Is there a communication (oral or written)?                                               | Documents that merely reflect facts, not communications, may not qualify                       |
| **2. Between attorney and client**               | Is the author or recipient a licensed attorney acting in a legal (not business) capacity? | In-house counsel acting in a business capacity (e.g., as project manager) may not be protected |
| **3. Made in confidence**                        | Was the communication confidential at creation and preserved as confidential?             | Wide distribution beyond the need-to-know destroys confidentiality                             |
| **4. For the purpose of obtaining legal advice** | Was the primary purpose to seek or provide legal advice (not business advice)?            | Mixed business/legal communications require dominant-purpose analysis                          |

#### Work-Product Doctrine — Two Tiers

| Tier                      | Definition                                                                                                   | Discoverability                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| **Ordinary work product** | Documents and tangible things prepared by or for a party or its representative in anticipation of litigation | Can be overcome by showing substantial need + undue hardship to obtain substantial equivalent by other means [FRCP 26(b)(3)(A)] |
| **Opinion work product**  | Mental impressions, conclusions, opinions, legal theories of counsel                                         | Virtually never discoverable; "nearly absolute protection" [VERIFY controlling circuit precedent]                               |

**⟁ CLARIFY** — For documents with both business and legal purposes (common in regulatory
investigations and internal compliance programs), ask:

- "Was this document created at counsel's direction, or was it a routine business document
  that counsel later reviewed?"
- "Is litigation or regulatory action the primary reason this document exists?"

#### Categorical Privilege Log (When Appropriate)

For high-volume privilege reviews, a **categorical privilege log** groups similar documents
by category rather than listing each individually. Courts have accepted categorical logs when:

- The category description is specific enough to establish the privilege basis
- The number of documents makes document-by-document logging disproportionate
- The parties agree or the court permits categorical logging

Categorical log format:

```
| Category | Date Range | Custodians | Description | Privilege Basis | Doc Count | Confidence |
|----------|-----------|-----------|-------------|-----------------|-----------|-----------|
| Legal-advice emails re: [regulatory matter] | 2022-01-01 to 2023-06-30 | GC, Outside Counsel, CEO, CFO | Emails exchanged between GC/outside counsel and client personnel seeking and providing legal advice regarding [matter] | Attorney-client privilege | ~320 | High |
```

#### FRE 502(d) Clawback Agreement

Propose or confirm an FRE 502(d) non-waiver order before production to protect against
inadvertent disclosure of privileged documents:

```
SAMPLE FRE 502(d) ORDER LANGUAGE:
"The production of privileged or work-product-protected documents, electronically stored
information, or other information, whether inadvertent or otherwise, is not a waiver of
the privilege or protection from discovery in this case or in any other federal or state
proceeding. This Order shall be interpreted to provide the maximum protection allowed by
Federal Rule of Evidence 502(d). Nothing contained herein is intended to or shall serve to
limit a party's right to conduct a review of documents, ESI, or other information (including
metadata) for relevance, responsiveness, and/or segregation of privileged and/or protected
information before production."
```

**⟁ CLARIFY** — Ask the user:

- "Has a Rule 502(d) non-waiver order been entered by the court, or agreed to between counsel?
  If not, I recommend proposing one before any production begins."
- "Has the other side proposed a clawback agreement? If so, please share it for review."

### Step 10: Prepare Supplementation Schedule (Rule 26(e))

Identify and plan for all supplementation obligations.

#### FRCP 26(e) Supplement Obligations

A party who has responded to an interrogatory, RFP, or RFA must **supplement or correct**
the response in a timely manner if the party learns:

- The response is **incomplete or incorrect** in a material respect, AND
- The additional or corrective information has not otherwise been made known to the other party

[JURISDICTION-SPECIFIC] Supplementation timing varies:

- **FRCP**: "In a timely manner" — interpreted as before trial, but courts may impose deadlines
- **California CCP § 2030.310**: Supplemental interrogatories may be propounded; responses due within 30 days
- **Texas TRCP 193.5**: Party must amend when new information is learned and before discovery cutoff

#### Supplementation Trigger Events

| Trigger                                         | Action Required                                                                                                       |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| New documents found after response served       | Produce and identify as supplemental production                                                                       |
| Witness identified after interrogatory response | Supplement interrogatory identifying all persons with knowledge                                                       |
| Client corrects factual error in prior answer   | Serve amended response with correction highlighted                                                                    |
| Expert report changes damages analysis          | Update damages interrogatory answer                                                                                   |
| New material developed after RFA response       | If an "admit" should have been "deny" (or vice versa), file motion to withdraw admission and serve corrected response |

#### Supplementation Log Template

Maintain a living supplementation log throughout the case:

```
| Date | Request No. | Trigger Event | Action Required | Action Completed | Notes |
|------|------------|--------------|----------------|-----------------|-------|
| [Date] | Int. No. 5 | New witness identified — John Smith hired after response | Supplement to add Smith | [Date] | Served as Supplemental Response No. 1 |
```

**⟁ CLARIFY** — Ask the user at the outset:

- "Who within the client organization is responsible for flagging new documents, witnesses,
  or changed facts that might trigger a supplementation obligation?"
- "Is there a litigation hold in place ensuring new documents are preserved and flagged for
  the litigation team?"

### Step 11: Prepare Meet-and-Confer Position

After drafting responses, prepare a meet-and-confer outline for any sustained objections.

**FRCP 37(a)(1)** requires that a party filing a motion to compel certify that it has "in
good faith conferred or attempted to confer" with the opposing party. Most local rules require
an in-person or telephone conference (not just letter exchange).

#### Meet-and-Confer Response Position Template

```markdown
## Discovery Meet-and-Confer — Responding Party's Position

## Matter: [Case Name] Date: [Date] Forum: [Court]

### Sustained Objections — We Will Not Withdraw

| Request No.  | Objection                           | Legal Basis                                                      | Data Supporting Position    |
| ------------ | ----------------------------------- | ---------------------------------------------------------------- | --------------------------- |
| [Int. No. X] | Exceeds 25-interrogatory limit      | FRCP 33(a)(1); subparts Y and Z are discrete questions           | Count attached as Exhibit A |
| [RFP No. X]  | Disproportionate — inaccessible ESI | FRCP 26(b)(2)(B); legacy backup tapes estimated $150K to restore | IT declaration attached     |

### Compromise Positions — Open to Discussion

| Request No. | Original Request                       | Our Proposed Narrowing                                        | What We Will Produce                      |
| ----------- | -------------------------------------- | ------------------------------------------------------------- | ----------------------------------------- |
| [RFP No. Y] | "All communications regarding [Topic]" | Communications from [date range] to/from custodians [A, B, C] | ~500 documents; 30-day rolling production |

### Non-Negotiable Privilege Positions

| Request No.  | Withheld Category                       | Privilege Basis           | Log Reference         |
| ------------ | --------------------------------------- | ------------------------- | --------------------- |
| [Int. No. Z] | All communications with GC re: [matter] | Attorney-client privilege | PL-001 through PL-045 |

### Certification

Counsel for Responding Party: [Name]
Date available for conference: [Date/time slots]
Preferred medium: [Telephone / Video / In-person]
```

### Step 12: Quality Assurance and Delivery

Before finalizing any response package, run the full quality framework.

**⟁ CLARIFY** — For large response packages (multiple sets, complex privilege issues), ask:

- "Do you want the full package (all responses, privilege log, supplementation log, meet-and-confer
  outline) or priority focus on the most disputed requests?"
- "Should I flag the requests most likely to generate a motion to compel for priority attorney review?"

---

## State Discovery Response Variations

### California (CCP §§ 2030.010-2033.420)

[JURISDICTION-SPECIFIC] Key differences from federal practice:

| Feature                       | FRCP                                            | California CCP                                                                                                       |
| ----------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Interrogatory limits**      | 25 (FRCP 33(a)(1))                              | 35 "specially prepared" + unlimited "form interrogatories" (CCP § 2030.030)                                          |
| **Verification requirement**  | Counsel may sign interrogatory responses        | Party must sign under oath; counsel cannot verify on party's behalf (CCP § 2030.250)                                 |
| **Subpart counting**          | All subparts count toward the 25-question limit | Subparts of a specially prepared interrogatory each count separately                                                 |
| **General objections**        | Prohibited under post-2015 FRCP                 | Jurisdictionally disfavored but practice varies by court                                                             |
| **Separate statement**        | Not required for motion practice                | A "separate statement" of disputed discovery responses is required on motions to compel (Cal. Rules of Court 3.1345) |
| **Response deadline**         | 30 days                                         | 30 days (CCP § 2030.260); parties can stipulate to extend                                                            |
| **Production in litigations** | One response covers all                         | Verified written response to inspection demand required; separate from actual production                             |
| **Form interrogatories**      | Not used                                        | Judicial Council Form Interrogatories are available for common case types (employment, vehicle accident, etc.)       |

**California-specific objections:**

- "The question calls for a legal conclusion" remains a recognized objection under CCP practice
- "Unduly burdensome" includes reference to financial hardship for smaller parties
- Privacy objections under California Constitution Art. I, § 1 (right of privacy) can protect
  third-party personal information that would be producible under FRCP

### New York (CPLR §§ 3101, 3120-3133)

[JURISDICTION-SPECIFIC] Key differences:

| Feature                 | FRCP                                                     | New York CPLR                                                                                                  |
| ----------------------- | -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Discovery scope**     | Proportionality + relevance to claim or defense          | "Full disclosure of all matter material and necessary" (CPLR § 3101(a)) — broader than federal                 |
| **Interrogatory limit** | 25                                                       | 25 (CPLR § 3130(1)); unlimited in commercial division (22 NYCRR 202.70)                                        |
| **Disclosure standard** | Relevant, proportional                                   | Material and necessary — broader threshold                                                                     |
| **Privilege**           | Federal common law (FRE 501); work product FRCP 26(b)(3) | NY CPLR § 3101(c) (attorney's work product); § 3101(d)(2) (qualified immunity for trial preparation materials) |
| **Bill of particulars** | Not available in federal court                           | Available in NY civil practice; limits scope of discovery                                                      |
| **Verification**        | Counsel can typically sign responses                     | Party must verify interrogatory responses under CPLR § 3157                                                    |

### Texas (TRCP 190-199)

[JURISDICTION-SPECIFIC] Key differences:

| Feature                   | FRCP                        | Texas TRCP                                                                                      |
| ------------------------- | --------------------------- | ----------------------------------------------------------------------------------------------- |
| **Discovery levels**      | Single unified standard     | Three levels: Level 1 (cases ≤$100K), Level 2 (default), Level 3 (complex — by agreement/order) |
| **Interrogatory limits**  | 25                          | Level 1: none; Level 2: 15 + limit (TRCP 190.2(b)(3)); Level 3: as ordered                      |
| **Oral depositions**      | FRCP 30                     | Level 2: 6 hours total per deposition                                                           |
| **Discovery scope**       | Proportionality + relevance | "Relevant to the subject matter" — Texas retains pre-2015-amendment-style scope                 |
| **Objection specificity** | Specific basis required     | "Overly broad" and similar objections still used but specificity is increasingly required       |
| **Response timeline**     | 30 days                     | 30 days for interrogatories and production; 28 days for RFAs (TRCP 198.2(a))                    |

### Florida (Fla. R. Civ. P. 1.340-1.370)

[JURISDICTION-SPECIFIC] Closely follows federal framework with key differences:

- Interrogatory limit: 30 per party (Fla. R. Civ. P. 1.340(a))
- No proportionality overhaul equivalent to 2015 FRCP amendments; scope remains "relevant to
  the subject matter of the pending action"
- Verification required for interrogatory responses (Fla. R. Civ. P. 1.340(a))
- RFA responses due within 30 days; default is deemed denial (opposite of federal deemed admission)
  [VERIFY current Florida rule on default RFA treatment]

### Illinois (Ill. S. Ct. Rules 213-216)

[JURISDICTION-SPECIFIC] Key differences:

- Rule 213 (interrogatories): No numeric limit for pattern 213(f) witness interrogatories; 30
  limit for other interrogatories [VERIFY current Illinois limits]
- Rule 213(f) witness disclosure (opinion witnesses) functions more like federal Rule 26(a)(2)
  expert disclosures and must identify opinion subject matter, bases, conclusions, and qualifications
- Rule 214 (inspection): Responds within 28 days; "object with specificity" requirement

---

## Citation Quality Gates

Run these five gates silently before delivering any response or log:

| Gate           | Rule                                                                           | Fail Action                            |
| -------------- | ------------------------------------------------------------------------------ | -------------------------------------- |
| **Source**     | Every procedural citation references a specific rule number and subdivision    | Add specific cite or mark "[VERIFY]"   |
| **Format**     | All citations follow consistent recognized format for the forum                | Normalize citation style               |
| **Currency**   | Every rule cited checked for amendments (FRCP amended Dec. 1 each year)        | Add "[CHECK CURRENCY — as of [date]]"  |
| **Domain**     | Analysis stays within the governing forum's rules; no cross-jurisdiction bleed | Re-scope or annotate                   |
| **Confidence** | All uncertain legal positions explicitly labeled                               | Add confidence qualifier or "[VERIFY]" |

---

## Self-Interrogation (For HIGH-STAKES Objections and Privilege Claims)

For any objection that will be asserted to withhold all documents responsive to a request,
or any privilege claim over a significant volume of documents, apply a three-pass review:

**Pass 1 — Legal Chain Integrity**: Does this objection or privilege claim rest on a valid
legal basis? What is the specific rule, case, or privilege doctrine? Would a court accept
this analysis?

**Pass 2 — Completeness**: Have all counter-arguments been considered? Does the propounding
party have a colorable argument that would overcome this objection? Is there a compromise
position that satisfies both parties?

**Pass 3 — Adversarial Challenge**: How would the propounding party's counsel attack this
objection in a meet-and-confer? In a motion to compel? What is the client's exposure to
sanctions if this objection is struck?

If unresolved after pass 3, escalate to supervising counsel before serving the response.

---

## Confidence Scoring

| Level        | Range     | Meaning                                                                                        | Action                                             |
| ------------ | --------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **Definite** | 0.95-1.00 | Settled procedural rule; clear privilege basis; strong proportionality showing                 | Assert with confidence                             |
| **High**     | 0.80-0.94 | Good authority; minor uncertainty about application to these specific facts                    | Assert with brief caveat in counsel note           |
| **Probable** | 0.60-0.79 | Rule is clear but application to these facts is debatable; proportionality could go either way | Flag for attorney judgment; present both positions |
| **Possible** | 0.40-0.59 | Objection or privilege claim may not survive a well-funded motion to compel                    | Discuss risk with client; consider compromise      |
| **Unlikely** | 0.00-0.39 | Objection is likely boilerplate or otherwise defective                                         | Do not assert; producing party may face sanctions  |

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-discovery-response-drafter"
  topic: "civil discovery response drafting — interrogatories, RFPs, RFAs, privilege log"
  jurisdiction: "[Selected forum — FRCP / California / New York / Texas / Florida / Illinois]"
  mode: "Created from scratch — Legalcode original"
  enhancement_type: "Create"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "/tmp/legalcode-response-authority.md"
  source_skills_analyzed: "0 — original creation"
  related_skills_reviewed:
    ["legalcode-discovery-request-drafter", "legalcode-privilege-review"]
  quality_score: "37/40"
  completeness: "18/18 elements"
  citations_verified: "[count VERIFIED] / [count VERIFY]"
  confidence: "HIGH — FRCP core rules well-settled; state rule variants marked [JURISDICTION-SPECIFIC] and [VERIFY]"
  assumptions:
    - "US federal primary jurisdiction; state rules summarized at the level of key variations only"
    - "2015 FRCP amendments applied throughout; confirm current version in governing court"
    - "State rule summaries reflect general rule; verify with current Westlaw/Lexis publication"
  limitations:
    - "Criminal discovery (Brady, Jencks Act) not covered"
    - "International discovery (Hague, cross-border GDPR) not covered"
    - "Complex ESI deep-dive deferred to legalcode-tar-review-protocol"
    - "Privilege classification depth deferred to legalcode-privilege-review"
  reviewer: "AI-assisted — qualified litigation counsel review required before service"
```

---

## Anti-Patterns

Avoid these discovery response failures — each risks sanctions, adverse inferences, or waiver:

1. **Boilerplate general objections**: Including a block of objections at the beginning of
   responses that apply globally to all requests. Post-2015 courts routinely strike them and
   award fees. Every objection must be stated specifically in the response to the specific request.

2. **"Not reasonably calculated to lead to admissible evidence"**: This phrase was deleted from
   FRCP 26(b)(1) in 2015. Using it reveals the responding counsel has not updated their form
   files and flags the entire response set as procedurally suspect.

3. **Asserting objections but not disclosing whether documents are withheld**: Rule 34(b)(2)(C)
   requires disclosure of whether any responsive materials are being withheld on the basis of
   the objection. Failing to disclose creates reversible error and potential sanctions.

4. **Using "unduly burdensome" without quantification**: Courts uniformly reject this objection
   when asserted without cost data, custodian counts, or document volume estimates. Quantify
   or abandon the objection.

5. **Privilege log entries that reveal nothing**: Descriptions like "legal advice regarding
   business matter" tell the court nothing and will not support a privilege claim at in camera
   review. Descriptions must identify the nature of the advice sought without revealing the
   privileged content.

6. **Failing to answer the non-objectionable portion**: If part of a compound request is
   objectionable and part is not, the responding party must still answer the non-objectionable
   portion. Asserting an objection to avoid answering the whole request is improper.

7. **Missing the 30-day deadline without an extension**: Failure to timely respond can
   constitute waiver of all objections (including privilege) in many courts. Calendar deadlines
   immediately upon receipt and seek extensions before they expire, not after.

8. **"Lack sufficient information" as a strategic denial**: FRCP 36(a)(4) requires "reasonable
   inquiry" before using this response. Courts will inquire into what inquiry was actually
   conducted. Using it as an evasion when knowledge exists invites sanctions.

9. **Deemed RFA admissions overlooked**: If an RFA response deadline passes without a response,
   the matter is conclusively admitted. This has ended cases. Every received RFA must be
   calendared with a hard deadline and backup reminder.

10. **Rule 33(d) business-records dump**: Using the business-records option without identifying
    specific records with "reasonable particularity" or providing reasonable access. A responding
    party cannot simply point to a warehouse of documents and satisfy Rule 33(d).

11. **Failing to supplement when new information is learned**: Rule 26(e) is an ongoing obligation.
    Failure to supplement before trial — especially for damages computations, witness lists, and
    damages interrogatory answers — can result in preclusion of evidence under Rule 37(c)(1).

12. **Admitting RFAs without document review**: A party that admits the genuineness of a document
    without actually reviewing it may be bound by that admission even if the document turns out to
    be a draft, altered, or out-of-context excerpt.

13. **Privilege log served months after responses**: The privilege log is due when the response
    is served (or at least within a reasonable time). Delayed privilege logs invite challenges
    to privilege, arguments of waiver, and motions for in camera review.

14. **In-house counsel business-capacity documents incorrectly privileged**: Communications
    where in-house counsel acted as a business advisor, project manager, or operational
    decision-maker — not as legal counsel — are not privileged even if the author holds a JD
    and bar membership. Assess the capacity in which counsel acted.

15. **Ignoring the assigned judge's standing orders**: Many districts require specific meet-and-confer
    procedures before raising discovery disputes. Ignoring standing orders triggers denial of
    motions and sometimes sanctions.

16. **Cross-jurisdiction privilege bleed**: Asserting attorney-client privilege under FRCP principles
    in a state-court case where state-law privilege rules (which may differ) govern, or assuming
    that privilege recognized in one country applies in US proceedings.

17. **Failing to enter a Rule 502(d) order before production**: Without a court-entered FRE 502(d)
    order, inadvertent production of privileged documents may waive privilege not just for this
    case but potentially in other proceedings. Seek the order before any production begins.

18. **Contention interrogatory responses provided prematurely**: Answering contention interrogatories
    before fact discovery is substantially complete locks in a legal position that the evidence
    may not yet fully support. Seek to defer contention responses to close of fact discovery.

---

## Writing Standards

- **Precision over hedging**: State objections specifically and affirmatively. Hedge language
  ("to the extent that," "insofar as") without specific application is disfavored by courts.
- **Parallel structure**: Use consistent format for all responses within a set — objection text,
  bridge language, answer, privilege assertion, in the same order every time.
- **Avoid circular definitions**: Do not define "Documents" to include "writings, records, and
  documents" — it adds nothing. Define by medium, not by synonym.
- **Use active voice in answers**: "Defendant entered into the contract on March 1, 2022" not
  "It is the position of Defendant that the contract may have been entered into around the first
  of March."
- **Flag uncertainty explicitly**: If the client has not confirmed a fact, say so in the response
  and note that supplementation will follow. Do not fabricate or guess.
- **Privilege log descriptions**: Write in the third person, past tense, and use enough specificity
  to identify the subject matter without revealing the substance.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 3, search for controlling proportionality precedent in the governing district
- Pull current FRCP text and any recent amendments
- Search for assigned judge's standing orders and recent discovery rulings
- Verify state-rule differences for the applicable state court
- Mark confirmed references as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with FRCP general knowledge and web search for state-specific rules
- Mark all case law references with [VERIFY]
- Mark all state-specific procedural rule references with [JURISDICTION-SPECIFIC][VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`

---

## Localization Notes

For state-specific practice, always verify:

- **California**: CCP §§ 2030-2033 text (current Deering's or West's CA Code); Cal. Rules of Court
  3.1345 (separate statement); Evidence Code §§ 950-1070 (privilege)
- **New York**: CPLR §§ 3101-3133 (McKinney's); Commercial Division Rules (22 NYCRR Part 202.70)
  if applicable; NY CPLR Practice Commentaries for privilege scope
- **Texas**: Texas Rules of Civil Procedure (current Vernon's) — especially discovery levels 1/2/3
  under TRCP 190; Texas Rules of Evidence §§ 503-510 for privilege
- **Florida**: Florida Rules of Civil Procedure (West's or LexisNexis); Florida Statutes §§ 90.501-90.510
  for privilege
- **Illinois**: Illinois Supreme Court Rules 201-224; Illinois Rules of Evidence §§ 501-510 for privilege

---

## Output Format Template

```markdown
# Discovery Response Package

## Matter: [Case Name, Cause No.]

## Responding Party: [Name]

## Propounding Party: [Name]

## Request Set: [Interrogatories / RFPs / RFAs — Set No. X]

## Date Received: [Date]

## Response Deadline: [Date] ([Extension agreed? Yes/No])

---

## PRELIMINARY OBJECTIONS AND STATEMENTS

[General statements applicable to all responses — not objections, but definitions,
limitations, and scope statements. For example:]

"Responding Party responds to the following Discovery Requests subject to the Definitions
and Instructions contained therein and subject to the following general statements:

1. These responses are based on information currently available to Responding Party.
   Discovery and investigation are ongoing. Responding Party reserves the right to
   supplement, amend, or correct these responses as additional information becomes available.

2. By responding to any Request, Responding Party does not waive any objection that may
   be applicable to any use of the information provided.

3. Responding Party interprets undefined terms according to their ordinary meaning and
   in the context of the litigation.

4. Where a Request encompasses information protected by the attorney-client privilege or
   the work-product doctrine, such information is identified in the Privilege Log served
   herewith. No such designation is intended to operate as a blanket privilege claim."

---

## RESPONSES TO INTERROGATORIES

### INTERROGATORY NO. 1:

[Interrogatory text]

**RESPONSE TO INTERROGATORY NO. 1:**
[Objections with specificity]
[Answer, subject to objections]
[Privilege notation if applicable]

---

## RESPONSES TO REQUESTS FOR PRODUCTION

### REQUEST FOR PRODUCTION NO. 1:

[Request text]

**RESPONSE TO REQUEST FOR PRODUCTION NO. 1:**
[Objection(s) with specificity]
[Production commitment and scope]
[Withholding statement]
[Timeline and format]

---

## RESPONSES TO REQUESTS FOR ADMISSION

### REQUEST FOR ADMISSION NO. 1:

[Request text]

**RESPONSE TO REQUEST FOR ADMISSION NO. 1:**
[Admit / Deny / Qualified response / Lack of sufficient information]

---

## PRIVILEGE LOG

| Log ID | Doc Type | Date | Author [Role] | Recipient(s) [Role] | Subject Matter | Privilege Basis | Confidence |
| ------ | -------- | ---- | ------------- | ------------------- | -------------- | --------------- | ---------- |

---

## SUPPLEMENTATION SCHEDULE

| Request No. | Current Status | Trigger | Expected Supplement Date |
| ----------- | -------------- | ------- | ------------------------ |

---

## QA RECORD

- Citation gate outcomes: [PASS / FAIL items]
- Self-interrogation outcomes: [Escalated items and resolutions]
- Confidence distribution: [Summary]
- High-risk responses flagged for attorney review: [List]

---

## GLASS BOX AUDIT

[Insert Glass Box YAML block]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis built from:

- Deep research on FRCP 26-37 discovery response requirements, post-2015 boilerplate sanctions
  case law (Fischer v. Forrest, Hager v. Graham, Liguria Foods v. Griffith Laboratories [VERIFY]),
  privilege log standards under FRCP 26(b)(5), FRE 502(d) clawback mechanics, and Rule 26(e)
  supplementation obligations
- State-specific research on California CCP §§ 2030-2033, New York CPLR §§ 3130-3133,
  Texas TRCP 190-198, Florida Fla. R. Civ. P. 1.340-1.370, and Illinois Ill. S. Ct. Rules 213-214
- Structural patterns from `legalcode-discovery-request-drafter` (complementary propounding-side skill)
- Quality frameworks from `legalcode-privilege-review` (deep privilege analysis companion)
- Reference standard quality bar from `legalcode-contract-review`
- Legalcode 18-element quality framework applied throughout
