---
name: legalcode-conflict-check
description: Conduct comprehensive conflict of interest checks for law firms before accepting new client
  representations. Use when screening prospective clients, lateral hires, new matters for existing clients,
  related party transactions, or any engagement requiring professional responsibility clearance. Covers
  ABA Model Rules 1.7-1.10 (US), SRA Code of Conduct (UK), and common law/civil law jurisdiction frameworks.
  Identifies direct, imputed, positional, and corporate family conflicts. Produces auditable conflict
  clearance documentation with waiver recommendations and ethical wall protocols. Integrates with legalcode-client-intake-workflow
  for full intake process.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Conflict Check

> **Disclaimer**: This skill provides a framework for AI-assisted conflict of interest
> screening. It does not constitute legal advice. All conflict determinations should be
> reviewed by qualified conflicts counsel or a licensed attorney in the relevant
> jurisdiction before accepting or declining representations. Professional responsibility
> rules change; verify current applicability before relying on any provision described
> here. Statutory and regulatory references cited from memory carry hallucination risk —
> verify against authoritative sources before relying on them.

## Purpose and Scope

This skill conducts comprehensive conflict of interest checks for law firms, identifying
potential ethical barriers to representation and producing auditable clearance
documentation. It supports both preliminary screening (before receiving confidential
information) and comprehensive checking (after full intake).

**Covers:**

- Identification and classification of conflict types (direct, imputed, positional,
  corporate family, related party, prospective client, former client)
- Multi-party and corporate family relationship mapping
- Conflict waiver analysis (consentable vs. non-consentable)
- Ethical wall/screening protocol recommendations
- Lateral hire conflict assessment
- Auditable conflict clearance documentation
- Integration with conflict management systems

**Does not:**

- Make final accept/decline decisions (human judgment required)
- Provide legal advice on specific conflict scenarios
- Replace conflicts counsel or ethics committee review
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers

**Related skills:**

- `legalcode-client-intake-workflow` — full client onboarding process
- `legalcode-matter-triage-workflow` — matter prioritization and routing
- `legalcode-engagement-letter` — engagement letter drafting (if available)

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic. The firm's home jurisdiction and applicable bar
rules determine which specific conflict rules apply. The workflow identifies the relevant
regulatory framework early and adapts accordingly.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- **US (ABA Model Rules)**: Rules 1.7 (concurrent), 1.8 (specific transactions), 1.9
  (former clients), 1.10 (imputation), 1.11 (government lawyers), 1.18 (prospective
  clients). State variations may apply.
- **UK (SRA)**: Code of Conduct paragraphs 6.1 (own interest), 6.2 (client conflicts),
  "substantially common interest" and "competing for same objective" exceptions
- **EU/Civil Law**: National bar rules varying by jurisdiction; often stricter own-interest
  prohibitions
- **Canada**: Provincial law society rules (e.g., LSO Rules of Professional Conduct)
- **Australia**: State-based legal profession acts and professional conduct rules

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming the firm's policies or the conflict scenario, the workflow pauses and asks
when:

- The conflict type is ambiguous and classification affects the analysis
- Multiple resolution paths exist (waiver, screening, decline)
- Corporate family or related party relationships need clarification
- Risk tolerance or firm policy would change the recommendation

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

### Step 1: Accept Conflict Check Request

Accept the conflict check request in any of these formats:

- **New client/matter**: Prospective client name, adverse parties, matter description
- **Lateral hire**: Incoming attorney name, prior firm(s), client lists, matter history
- **New matter for existing client**: Client name, new matter description, new parties
- **Related party transaction**: Transaction parties, relationships, roles
- **Batch check**: Multiple parties or matters for simultaneous screening

**Minimum information required before proceeding:**

| Element                        | Required      | Purpose                               |
| ------------------------------ | ------------- | ------------------------------------- |
| Primary party name(s)          | Yes           | Core search target                    |
| All known adverse parties      | Yes           | Direct conflict detection             |
| Matter/transaction description | Yes           | Substantial relationship analysis     |
| Party relationships            | If applicable | Corporate family, affiliate detection |
| Check type                     | Yes           | Preliminary vs. comprehensive         |
| Requesting attorney            | Yes           | Personal conflict screening           |

If information is incomplete, prompt for the missing elements. Incomplete party lists
are a leading cause of missed conflicts.

### Step 2: Gather Context

**CLARIFY** — Before running the conflict check, confirm the following. Present as
structured options where possible:

1. **Check type**: What stage is this conflict check?
   - Options: **Preliminary** (before substantive discussion — protect against Rule 1.18
     prospective client issues), **Comprehensive** (full intake with all parties known),
     **Lateral hire** (attorney joining firm), **Matter expansion** (new scope for existing
     client), **Re-check** (triggered by new party or changed circumstances)
   - _Why this matters_: Preliminary checks use limited information to avoid receiving
     disqualifying confidential information. Comprehensive checks require full party lists.

2. **Firm conflict system access**: Do you have access to the firm's conflict database?
   - Options: Yes (provide system name or describe), No (manual check), N/A (solo
     practitioner)
   - _Why this matters_: Determines search methodology and documentation requirements.

3. **Regulatory framework**: Which jurisdiction's conflict rules apply?
   - Options: US (ABA Model Rules + state), UK (SRA Code), Canada (provincial), EU
     (specify country), Australia (specify state), Other (specify)
   - _Why this matters_: Determines applicable conflict rules, waiver requirements, and
     screening procedures.

4. **Firm conflict policy**: Does the firm have a conflicts policy or manual?
   - Options: Yes (describe key policies), No (use general standards), Unknown
   - _Why this matters_: Firm policies may be stricter than bar minimum requirements.

If the user provides partial context, proceed with reasonable defaults and state
assumptions explicitly.

### Step 3: Identify All Parties for Screening

Before searching, compile the complete party list. Conflicts are often missed due to
incomplete party identification.

**CLARIFY** — For each primary party, gather:

1. **Individual clients**:
   - Full legal name and aliases/former names
   - Spouse/partner (for family matters, estate planning)
   - Business affiliations
   - Known agents, representatives, or fiduciaries

2. **Entity clients**:
   - Legal entity name and all DBAs/trade names
   - Parent company and ultimate parent
   - Subsidiaries and affiliates (material ones)
   - Officers, directors, and key shareholders (10%+)
   - Related entities under common control

3. **Adverse parties** (same depth as above)

4. **Related parties**:
   - Co-parties (co-defendants, co-plaintiffs, joint venturers)
   - Insurers and their counsel
   - Lenders, investors, acquirers
   - Key witnesses and their counsel
   - Expert witnesses and consultants
   - Mediators, arbitrators (if known)

5. **For lateral hires**:
   - Prior firm(s) and dates
   - All clients represented (matters and dates)
   - All adverse parties faced
   - Any clients with "portable" expectations
   - Any ethical walls already in place

**Corporate family mapping:**

For entity clients, construct the corporate family tree to identify related party
conflicts:

```
[Ultimate Parent]
  |-- [Parent Company] <-- Client or Adverse?
  |     |-- [Subsidiary A] <-- Consider as related
  |     |-- [Subsidiary B] <-- Consider as related
  |     |-- [JV Entity (50%)] <-- May be related depending on control
  |
  |-- [Affiliate Entity] <-- Under common control
```

Apply the "unity of interest" test: Do the entities share officers, directors, legal
representation, finances, or operations such that adversity to one is effectively
adversity to the other?

### Step 4: Search Conflict Database

Execute the conflict search using all identified parties and variations.

**Search parameters:**

| Search Type             | What to Search                 | Why                            |
| ----------------------- | ------------------------------ | ------------------------------ |
| **Exact match**         | Full legal names               | Primary identification         |
| **Phonetic/fuzzy**      | Soundex, Metaphone variants    | Catch spelling variations      |
| **Partial match**       | Name fragments, initials       | Catch abbreviated entries      |
| **DBA/trade names**     | All known aliases              | Entity name variations         |
| **Corporate family**    | Parent, sub, affiliate names   | Related party conflicts        |
| **Address**             | Business/residential addresses | Catch unreported relationships |
| **Tax ID/registration** | EIN, company numbers           | Definitive entity matching     |

**Database scope:**

- [ ] Current client database (active matters)
- [ ] Former client database (closed matters, per retention policy)
- [ ] Prospective client records (declined/not-engaged)
- [ ] Lateral hire records (imported client lists)
- [ ] Adverse party records
- [ ] Business development contacts (if separate)
- [ ] Personal contacts of requesting attorney

**Document the search:**

```yaml
conflict_search:
  date: "[date]"
  searcher: "[name or AI-assisted]"
  parties_searched: "[count]"
  databases_searched:
    - "[database 1]"
    - "[database 2]"
  search_methods:
    - "Exact match"
    - "Phonetic (Soundex)"
    - "Fuzzy matching"
  results:
    exact_matches: "[count]"
    potential_matches: "[count]"
    no_match: "[count]"
```

### Step 5: Analyze Search Results

For each search hit, analyze whether it represents an actual conflict.

**CLARIFY** — For each potential match, determine:

1. **Is this the same party?** (identity confirmation)
   - Same entity/individual, or false positive (different person, common name)?
   - If uncertain, flag for human verification.

2. **What is the relationship?** (role classification)
   - Current client, former client, prospective client, adverse party, related party,
     witness, other?

3. **What is the matter relationship?** (substantial relationship test)
   - Same matter, substantially related matter, or unrelated matter?
   - Would confidential information from the prior matter be material to the current matter?

**Conflict classification:**

| Conflict Type               | Definition                                                                       | Key Test                                          | Rule Reference         |
| --------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------- | ---------------------- |
| **Direct concurrent**       | Representing client A while adverse to A in another matter                       | Any adversity to current client                   | ABA 1.7(a)(1), SRA 6.2 |
| **Material limitation**     | Representation limited by duties to another client, third party, or own interest | Would limitation affect competent representation? | ABA 1.7(a)(2), SRA 6.1 |
| **Former client**           | Matter substantially related to prior representation                             | Confidential information test                     | ABA 1.9                |
| **Prospective client**      | Received disqualifying information from non-engaged prospect                     | Information that could be significantly harmful   | ABA 1.18               |
| **Imputed**                 | Another firm lawyer has a conflict that spreads firm-wide                        | Imputation unless exception applies               | ABA 1.10               |
| **Positional**              | Taking inconsistent legal positions for different clients                        | Material limitation on advocacy                   | ABA 1.7(a)(2)          |
| **Corporate family**        | Adversity to affiliate of current client                                         | Unity of interest test                            | ABA 1.7 Comment [34]   |
| **Own interest**            | Lawyer's personal interest conflicts with client duties                          | Independence compromised                          | ABA 1.7(a)(2), SRA 6.1 |
| **Government/former gov't** | Prior government service creates restrictions                                    | Substantial participation test                    | ABA 1.11               |

### Step 6: Classify Conflict Severity

For each identified conflict, classify severity to determine the appropriate resolution
path.

### CLEAR — No Conflict

No conflict exists. Representation may proceed without restriction.

**Criteria (ALL must be true):**

- No matches found for any party, OR
- All matches confirmed as false positives (different entity/individual), OR
- Matches found but no adversity, no substantial relationship, and no material limitation

**Action**: Document clearance. Proceed with engagement.

### YELLOW — Potential Conflict (Waivable)

A conflict exists but may be waivable with proper informed consent.

**Criteria (ANY):**

- Concurrent conflict but lawyer reasonably believes competent representation is possible
- Former client conflict with no shared confidential information material to current matter
- Positional conflict with minimal risk of adverse impact
- Corporate family conflict where entities have genuinely separate interests
- Imputed conflict where screening may be available (lateral hire)

**Action**: Analyze waiver requirements. Prepare conflict waiver. Implement safeguards.

### RED — Definite Conflict (Non-Waivable or High-Risk)

A conflict exists that cannot be waived or presents unacceptable risk.

**Criteria (ANY):**

- Same-matter direct adversity (client vs. client in same proceeding)
- Lawyer cannot reasonably believe competent representation possible
- Representation prohibited by law
- Former client matter is substantially related with material confidential information
- Prospective client disclosed significantly harmful information
- Own-interest conflict (SRA: absolute bar; ABA: disclosure required but often impractical)

**Action**: Decline representation or implement formal ethical wall with proper screening
protocol. Escalate to conflicts counsel.

---

## Conflict Type Deep Dive

### 1. Direct Concurrent Conflicts (Rule 1.7(a)(1))

**Definition**: Representation of one client is directly adverse to another current client.

**Key analysis points:**

- Is the adverse party a current client of any lawyer in the firm?
- Does the adversity arise in litigation, negotiation, or any other context?
- Even if matters are unrelated, direct adversity to a current client is prohibited
  without consent

**Common scenarios:**

- Suing a current client (even in an unrelated matter)
- Negotiating against a current client for a different client
- Taking a position in regulatory proceedings adverse to a current client

**Waiver requirements** (if consentable):

- Lawyer must reasonably believe they can provide competent, diligent representation
- Not involving assertion of claim by one client against another in same proceeding
- Informed consent from BOTH affected clients, confirmed in writing
- Disclose nature of conflict, risks, and implications of dual representation

[JURISDICTION-SPECIFIC] **SRA (UK)**: Client conflicts under paragraph 6.2 may only be
waived if "substantially common interest" or "competing for same objective" exception
applies. More restrictive than ABA Model Rules. [VERIFY]

### 2. Material Limitation Conflicts (Rule 1.7(a)(2))

**Definition**: Representation is materially limited by duties to another client, a
former client, a third person, or the lawyer's own interests.

**Key analysis points:**

- Would the lawyer's judgment or actions be constrained by other obligations?
- Is there a significant risk that representation will be materially limited?
- Consider: other client duties, personal interests, financial interests, prior
  relationships

**Common scenarios:**

- Personal relationship with adverse party (family, close friend)
- Financial interest in transaction outcome
- Lawyer's fear of losing another client affects advice
- Lawyer previously made an error that affects current advice
- Board membership or business relationship with adverse party

**Waiver requirements** (if consentable):

- Full disclosure of the limiting factor
- Lawyer reasonably believes representation will not be adversely affected
- Client provides informed consent in writing

### 3. Former Client Conflicts (Rule 1.9)

**Definition**: Representation adverse to a former client in the same or substantially
related matter, or use of confidential information to the former client's disadvantage.

**Substantial relationship test:**

```
Is the current matter the same as, or substantially related to, the prior matter?
  |
  v
"Substantially related" = matters in which lawyer could have acquired confidential
information that would be material to the current matter
  |
  v
If YES: Presumption that confidential information was shared. Conflict exists.
If NO: No conflict from former representation (but check imputation).
```

**Key analysis points:**

- What matters did the firm handle for the former client?
- What confidential information might the firm possess?
- Would that information be material to the current adverse matter?
- How much time has passed? (relevant but not dispositive)

**Waiver requirements:**

- Informed consent from the former client, confirmed in writing
- May be more difficult to obtain than current client consent

### 4. Prospective Client Conflicts (Rule 1.18)

**Definition**: Duties owed to a prospective client (someone who consulted about
possible representation but was not engaged) that create conflict for current
representation.

**Key issue**: A lawyer who receives information from a prospective client that could
be "significantly harmful" to that person cannot represent an adverse party in the same
or substantially related matter.

**Mitigation strategies:**

- Limit initial consultation to identify conflicts before receiving substantive facts
- Use intake questionnaires that gather party names before confidential details
- Implement prospective client conflict checks BEFORE detailed discussions

**Screening exception**: If the disqualified lawyer is timely screened and receives no
fee from the matter, the firm may be able to proceed (jurisdiction-dependent).

### 5. Imputed Conflicts (Rule 1.10)

**Definition**: One lawyer's conflict is imputed (attributed) to all lawyers in the firm.

**General rule**: If one lawyer in a firm has a conflict, the entire firm is deemed to
have that conflict.

**Exceptions** (vary by jurisdiction):

- Personal interest conflicts that do not present significant risk
- Timely screening of disqualified lateral hires (in jurisdictions permitting screening)
- Former firm conflicts where lawyer did not acquire confidential information
- Nonlawyer conflicts (may be screened in some jurisdictions)

**Lateral hire analysis:**

1. Identify all prior clients and matters of the incoming attorney
2. Check each against the firm's current and former client list
3. For each match, apply the substantial relationship test
4. If conflict exists, determine if screening is permitted under local rules
5. Implement ethical wall if screening is available and appropriate

### 6. Positional (Issue) Conflicts

**Definition**: Taking inconsistent legal positions for different clients in unrelated
matters that could materially limit representation.

**Key analysis points:**

- Are the legal positions directly contradictory?
- Is there a substantial risk that the position in one case will create adverse
  precedent for the other client?
- Are the matters pending in the same jurisdiction/court?
- Would success for one client materially harm the other's position?

**When consentable**:

- Different jurisdictions (precedent impact minimal)
- Different courts or tribunals
- Positions are distinguishable on the facts
- No reasonable probability one outcome will affect the other

**When non-consentable**:

- Same court, same legal issue, direct precedent impact
- Lawyer cannot competently argue both positions

### 7. Corporate Family Conflicts

**Definition**: Conflicts arising from adverse positions against affiliates, subsidiaries,
or related entities of a current client.

**Unity of interest test** — Consider whether the entities:

- Share common officers or directors
- Share legal representation (same outside counsel)
- Have integrated operations or finances
- Treat each other as a single economic unit
- Would view adversity to one as adversity to both

**If unity exists**: Treat as a single client for conflict purposes.
**If genuinely separate**: May be able to proceed, but document analysis and consider
disclosure.

**CLARIFY** — When corporate family relationships are ambiguous:

"The prospective matter involves [Company B], which appears to be [related to/affiliated
with] your current client [Company A]. Please clarify:

- What is the ownership/control relationship?
- Do they share officers, directors, or legal counsel?
- Does [Company A] consider [Company B] part of 'the client'?
- Has [Company A] previously requested that affiliates be included in conflict checks?"

---

## Conflict Waiver Analysis

### Waiver Availability Matrix

| Conflict Type                         | Generally Waivable?      | Key Conditions                                               |
| ------------------------------------- | ------------------------ | ------------------------------------------------------------ |
| Direct concurrent (different matters) | Yes                      | Reasonably competent representation; both clients consent    |
| Direct concurrent (same matter)       | NO                       | Cannot represent directly adverse clients in same proceeding |
| Material limitation                   | Yes                      | Full disclosure; reasonably competent representation         |
| Former client                         | Yes                      | Former client consent; no actual confidential info misuse    |
| Prospective client                    | Screening may substitute | Timely screen; no fee to disqualified lawyer                 |
| Imputed (lateral)                     | Screening may substitute | Jurisdiction permits; timely screen; written notice          |
| Positional                            | Sometimes                | Depends on precedent impact; both clients consent            |
| Corporate family                      | Usually                  | Depends on unity of interest analysis                        |
| Own interest (ABA)                    | Technically yes          | Disclosure + consent, but often impractical                  |
| Own interest (SRA)                    | NO                       | Absolute prohibition under SRA 6.1                           |

### Waiver Requirements Checklist

For each conflict where waiver is sought:

- [ ] **Waivability confirmed**: Conflict is of a type that can be waived
- [ ] **Reasonableness belief**: Lawyer reasonably believes competent representation
      is possible
- [ ] **Not prohibited by law**: No statutory bar to representation
- [ ] **Not same-proceeding adversity**: Clients not directly adverse in same litigation
- [ ] **Full disclosure made**: All material facts and risks disclosed to client(s)
- [ ] **Independent judgment opportunity**: Client had opportunity to consult
      independent counsel
- [ ] **Voluntary consent**: Consent not coerced or pressured
- [ ] **Written confirmation**: Consent confirmed in writing (signed waiver or email
      confirmation)
- [ ] **Mutual consent** (if applicable): All affected clients provided consent
- [ ] **Waiver filed**: Copy retained in conflict clearance file

### Waiver Letter Elements

A conflict waiver should include:

1. **Identification of conflict**: Clear description of the conflict situation
2. **Parties affected**: Who has the conflict and who is affected
3. **Nature of the conflict**: Type and source of the conflict
4. **Potential risks**: How the conflict could adversely affect the client
5. **Safeguards**: What measures will be taken to protect client interests
6. **Scope of waiver**: What specific conflict(s) are being waived
7. **Future conflicts**: Whether waiver extends to future related conflicts (advance
   waiver)
8. **Right to decline**: Client's right to refuse and seek other counsel
9. **Acknowledgment**: Client acknowledges understanding and voluntarily consents
10. **Signature and date**: Client signature confirming consent

---

## Ethical Wall (Screening) Protocols

When screening is permitted as an alternative to firm-wide disqualification, implement
formal ethical wall procedures.

### When Screening May Be Available

| Scenario                       | Screening Permitted?     | Conditions                                                    |
| ------------------------------ | ------------------------ | ------------------------------------------------------------- |
| Lateral hire from adverse firm | Yes (most jurisdictions) | Timely; no fee; written notice to affected clients            |
| Former government lawyer       | Yes (ABA 1.11)           | Timely; no fee; written notice to government agency           |
| Prospective client (1.18)      | Yes                      | Timely; reasonable measures; no confidential info shared      |
| Nonlawyer (paralegal, staff)   | Yes (most jurisdictions) | Timely; supervised; no file access                            |
| Personal interest conflict     | Maybe                    | Depends on nature; consent often still required               |
| Current client conflict        | Generally NO             | Screening alone usually insufficient for concurrent conflicts |

### Screening Protocol Requirements

**Timely implementation** (CRITICAL):

- Screen MUST be implemented as soon as conflict is identified
- Delay in screening can defeat the protection
- Document date/time of screening implementation

**Physical and electronic barriers:**

- [ ] Screened person removed from matter access in document management system
- [ ] Screened person removed from matter billing codes
- [ ] Electronic files locked from screened person's access
- [ ] Physical files (if any) secured away from screened person
- [ ] Calendar entries for matter meetings exclude screened person
- [ ] Email distribution lists exclude screened person

**Communication barriers:**

- [ ] Firm-wide notice issued identifying screened person and matter
- [ ] Instructions not to discuss matter with screened person
- [ ] Screened person acknowledges screen in writing
- [ ] Supervising attorney designated to monitor compliance

**Fee isolation:**

- [ ] Screened person receives no fee, bonus, or compensation tied to the matter
- [ ] This must be documented and verifiable

**Notice to affected parties:**

- [ ] Written notice to affected client(s) explaining screening
- [ ] Notice to former client/adverse party (if required by rule)
- [ ] Notice includes opportunity to challenge or seek disqualification

**Ongoing monitoring:**

- [ ] Periodic compliance checks documented
- [ ] Immediate reporting of any breach
- [ ] Remediation procedures if breach occurs

### Screen Documentation Template

```yaml
ethical_screen:
  matter: "[matter name/number]"
  screened_person: "[name]"
  reason_for_screen: "[conflict type and description]"
  date_implemented: "[date]"
  implemented_by: "[conflicts counsel or responsible attorney]"
  measures:
    electronic_access_removed: true/false
    physical_files_secured: true/false
    billing_access_removed: true/false
    calendar_exclusion: true/false
    firm_notice_issued: true/false
    acknowledgment_signed: true/false
  fee_isolation:
    no_fee_participation: true/false
    documented: true/false
  notices_sent:
    - recipient: "[client/former client]"
      date: "[date]"
      method: "[email/letter]"
  monitoring:
    compliance_checks: "[frequency]"
    responsible_person: "[name]"
  status: "Active / Lifted / Breached"
```

---

## Lateral Hire Conflict Analysis

Special workflow for screening conflicts when attorneys join the firm.

### Step L1: Gather Prior Representation Information

**From the incoming attorney:**

- [ ] Complete list of all clients represented at prior firm(s)
- [ ] All matters worked on (with dates)
- [ ] All adverse parties faced
- [ ] Any clients with expectations of ongoing representation
- [ ] Any ethical walls already in place at prior firm
- [ ] Any advance waivers or consent agreements

**From the prior firm** (if available):

- Client lists may be provided subject to confidentiality
- Some firms provide "clean lists" that exclude confidential matter details

### Step L2: Cross-Reference Against Firm Conflicts Database

For EACH client and matter from the incoming attorney:

1. Search firm's current client list — is this party now adverse to the firm?
2. Search firm's former client list — substantially related matters?
3. Search firm's adverse party list — would incoming attorney be conflicted?
4. Search firm's prospective client list — any unconsummated representations?

### Step L3: Analyze Each Conflict

For each hit:

| Question                                                              | If YES                                         | If NO                           |
| --------------------------------------------------------------------- | ---------------------------------------------- | ------------------------------- |
| Did incoming attorney personally work on the matter?                  | Conflict analysis required                     | May be imputed only             |
| Did incoming attorney acquire material confidential information?      | Presumed if substantially related              | May proceed with caution        |
| Is the current firm matter substantially related to the prior matter? | Screening or consent required                  | May proceed                     |
| Is the prior client now a current client of this firm?                | Special attention — may need consent from both | Standard former client analysis |

### Step L4: Determine Resolution

| Scenario                                                 | Resolution                                           |
| -------------------------------------------------------- | ---------------------------------------------------- |
| No substantial relationship, no confidential information | Clear to proceed                                     |
| Substantially related but screening permitted            | Implement ethical wall                               |
| Substantially related and screening not sufficient       | Obtain former client consent OR decline matter       |
| Current adversity to firm client                         | May be non-waivable; evaluate carefully              |
| Prior client is now firm client                          | Dual analysis: former client + current client duties |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any conflict analysis. If any gate fails,
revise before delivering.

| Gate           | Rule                                                                | Fail Action                         |
| -------------- | ------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every rule reference cites a specific professional conduct rule     | Add citation or mark "[UNVERIFIED]" |
| **Format**     | All citations follow proper format (e.g., ABA Model Rule 1.7(a)(1)) | Fix format                          |
| **Currency**   | Cited rules checked for recent amendments                           | Flag "[CHECK CURRENCY]"             |
| **Domain**     | Analysis applies rules from the correct jurisdiction                | Remove inapplicable rules           |
| **Confidence** | Uncertainty explicitly stated                                       | Add confidence qualifier            |

### Self-Interrogation for RED Conflicts

For any conflict classified as RED (non-waivable or high-risk), apply this 3-pass
review:

**Pass 1 — Rule Application**:

- Is the conflict classification correct under the applicable rules?
- Has the right test been applied (substantial relationship, material limitation, etc.)?
- Could a reasonable conflicts counsel reach a different conclusion?

**Pass 2 — Completeness**:

- Have all affected parties been identified?
- Have all relevant matters been checked?
- Are there screening or consent options not yet considered?

**Pass 3 — Challenge**:

- What is the strongest argument that this conflict IS waivable or manageable?
- Are there factual distinctions that would change the analysis?
- Would the affected client(s) likely consent if asked?

If any pass reveals a weakness, revise the analysis before delivery.

### Confidence Scoring

For each conflict determination, assign a confidence level:

| Level        | Range     | Meaning                            | Action                                   |
| ------------ | --------- | ---------------------------------- | ---------------------------------------- |
| **Definite** | 0.95-1.0  | Clear conflict or clear clearance  | State with confidence                    |
| **High**     | 0.80-0.94 | Strong conclusion, minor questions | Proceed with brief caveat                |
| **Probable** | 0.60-0.79 | Good analysis but facts uncertain  | Document reasoning; escalate if material |
| **Possible** | 0.40-0.59 | Genuinely uncertain                | Require conflicts counsel review         |
| **Unlikely** | 0.0-0.39  | Insufficient information           | Do not proceed; gather more information  |

---

## Glass Box Audit Trail

Every conflict check output MUST include a Glass Box audit section for traceability:

```yaml
glass_box:
  conflict_check_id: "[reference number]"
  check_type: "Preliminary / Comprehensive / Lateral / Re-check"
  date: "[date]"
  requesting_attorney: "[name]"
  prospective_client: "[name]"
  matter_type: "[description]"
  jurisdiction: "[regulatory framework applied]"
  parties_searched: "[count]"
  databases_searched:
    - "[database 1]"
    - "[database 2]"
  matches_found: "[count]"
  conflicts_identified: "[count]"
  conflict_classifications:
    clear: "[count]"
    yellow_waivable: "[count]"
    red_non_waivable: "[count]"
  resolutions:
    - conflict: "[description]"
      classification: "CLEAR / YELLOW / RED"
      resolution: "Cleared / Waiver obtained / Screen implemented / Declined"
  waivers_required: "[count]"
  waivers_obtained: "[count]"
  screens_implemented: "[count]"
  legalcode_mcp: "Connected / Not connected"
  rules_consulted:
    - "[Rule 1.7 — VERIFIED / UNVERIFIED]"
    - "[Rule 1.9 — VERIFIED / UNVERIFIED]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified conflicts counsel review"
  final_status: "CLEARED / CONDITIONAL (waivers pending) / BLOCKED (decline required)"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in conflict checking:

1. **Incomplete party lists** — Checking only the named client and adverse party without
   expanding to corporate family, related parties, witnesses, and insurers. This is the
   leading cause of missed conflicts.

2. **Skipping preliminary checks** — Receiving confidential information from a
   prospective client before running a conflict check. This can disqualify the entire
   firm under Rule 1.18.

3. **Single-database reliance** — Checking only the current client database and missing
   former clients, adverse parties, or imported lateral hire conflicts.

4. **Phonetic/fuzzy match skipping** — Relying only on exact name matches and missing
   spelling variations, name changes, or data entry errors.

5. **Corporate family blindness** — Failing to analyze whether related entities should
   be treated as a single client for conflict purposes.

6. **Premature waiver assumption** — Assuming all conflicts are waivable without
   analyzing whether the specific conflict type permits consent.

7. **Stale clearance reliance** — Using an old conflict clearance when new parties have
   been added, the matter scope has changed, or new lawyers have joined the firm.

8. **Undocumented clearances** — Clearing a conflict verbally or informally without
   creating an auditable record. If it is not documented, it did not happen.

9. **Ignoring positional conflicts** — Focusing only on party-based conflicts and
   missing issue conflicts where the firm takes inconsistent legal positions.

10. **Delayed screening** — Implementing an ethical wall after the disqualified lawyer
    has already accessed matter files or discussions. Late screens may not protect
    against disqualification.

11. **Fee participation in screened matters** — Allowing a screened lawyer to share in
    fees from the screened matter, which defeats the screening protection.

12. **Informal waiver acceptance** — Accepting oral consent or an ambiguous email as a
    conflict waiver without proper written confirmation and required disclosures.

13. **Assuming former client consent** — Proceeding against a former client without
    analyzing whether the matter is substantially related and whether consent is needed.

14. **Ignoring government lawyer rules** — Failing to apply the special conflict rules
    (Rule 1.11) for former government attorneys, which have different screening
    requirements.

15. **Lateral hire delay** — Waiting until after a lateral hire starts to run conflict
    checks. Conflicts should be identified during the hiring process.

---

## Writing Standards

Apply plain-language discipline to all conflict documentation:

**For conflict clearance memos**:

- State the conclusion first (CLEARED / CONDITIONAL / BLOCKED)
- Plain language, active voice
- Identify all parties and their roles
- Cite specific rules with precision
- Document the search and analysis
- State assumptions and limitations

**For conflict waiver letters** (client-facing):

- Plain language accessible to non-lawyers
- Clear identification of the conflict
- Honest disclosure of risks
- Client-friendly explanation of safeguards
- Clear consent language

**Quality gates before delivery**:

1. Can conflicts counsel understand and act on this memo?
2. Is every conflict classification supported by the applicable rule?
3. Are all parties accounted for and correctly identified?
4. Is the audit trail complete?
5. Would this memo survive bar disciplinary review?

---

## External Tool Integration

This skill integrates with **legalcode-mcp** for regulatory research and verification.

**With legalcode-mcp connected:**

- Search for jurisdiction-specific conflict of interest rules
- Verify current professional conduct rules and amendments
- Research ethics opinions on novel conflict scenarios
- Check for recent disciplinary actions involving conflicts
- Mark all legalcode-mcp-sourced references as VERIFIED

**Without legalcode-mcp:**

- Mark all rule references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Use general knowledge of ABA Model Rules and SRA Code
- Recommend verification against current bar rules before relying on analysis

---

## Output Format Template

Structure the completed conflict check documentation as:

```markdown
## Conflict Check Report

**Check ID**: [reference number]
**Date**: [date]
**Check Type**: [Preliminary / Comprehensive / Lateral / Re-check]
**Requesting Attorney**: [name]
**Regulatory Framework**: [jurisdiction]

---

## Summary: [CLEARED / CONDITIONAL / BLOCKED]

[One-paragraph summary of outcome and any required actions]

---

## Parties Searched

### Primary Parties

| Party  | Role                         | Variations Searched |
| ------ | ---------------------------- | ------------------- |
| [Name] | [Client / Adverse / Related] | [Aliases, DBAs]     |

### Corporate Family

[Corporate family tree if applicable]

---

## Search Results

**Databases searched**: [list]
**Total parties searched**: [count]
**Matches found**: [count]
**Conflicts identified**: [count]

---

## Conflict Analysis

### [Conflict 1] — [CLEAR / YELLOW / RED]

**Parties involved**: [names]
**Conflict type**: [direct / former client / imputed / etc.]
**Applicable rule**: [Rule 1.7(a)(1), etc.]
**Analysis**: [substantive analysis]
**Resolution**: [cleared / waiver required / screen implemented / decline]
**Confidence**: [level]

[Repeat for each conflict]

---

## Required Actions

### Waivers Needed

| Affected Client | Conflict Type | Status                          |
| --------------- | ------------- | ------------------------------- |
| [Name]          | [Type]        | [Pending / Obtained / Declined] |

### Screens Required

| Screened Person | Matter   | Implementation Date |
| --------------- | -------- | ------------------- |
| [Name]          | [Matter] | [Date]              |

---

## Clearance Determination

**Final Status**: [CLEARED / CONDITIONAL / BLOCKED]
**Conditions** (if any): [list any conditions such as pending waivers]
**Approved by**: [conflicts counsel name / pending review]
**Expiration**: [date, if re-check required for matter changes]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

This skill is jurisdiction-agnostic. To create a jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with specific bar rules
2. Replace [VERIFY] tags with verified rule citations
3. Add jurisdiction-specific conflict types or exceptions
4. Add jurisdiction-specific screening rules and limitations
5. Include jurisdiction-specific waiver requirements
6. Add jurisdiction-specific anti-patterns
7. Update frontmatter to reference the specific jurisdiction

**Key jurisdiction variations to address:**

- **US (by state)**: ABA Model Rules adopted with state variations; screening rules
  differ significantly by state
- **UK (England & Wales)**: SRA Code; stricter "own interest" bar; different exceptions
  for client conflicts
- **Canada**: Provincial law societies; varies by province
- **Australia**: State-based; some states stricter on screening
- **EU**: National bar rules vary significantly; some prohibit any concurrent conflicts

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis combining ABA Model Rules 1.7-1.10,
SRA Code of Conduct conflict provisions, conflict management system best practices, and
law firm intake procedures into a comprehensive jurisdiction-agnostic conflict checking
skill. Research sources include ABA Model Rules and Comments, SRA Code of Conduct
(2024-2025), FATF conflict of interest guidance, and legal ethics literature on conflict
management.
