---
name: legalcode-workplace-investigation
description: Guide workplace investigations end-to-end — from complaint intake and scope determination
  through investigator assignment, privilege preservation, document hold, witness interview protocols,
  credibility assessment, findings documentation, remedial action planning, and regulatory reporting.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Guide workplace investigations end-to-end — from complaint intake and scope determination through investigator assignment, privilege preservation, document hold, witness interview protocols, credibility assessment, findings documentation, remedial action planning, and regulatory reporting. Applies to harassment, discrimination, retaliation, hostile work environment, OSHA/safety complaints, code-of-conduct violations, whistleblower allegations, time-and-attendance fraud, workplace violence, and misconduct investigations. Extends to compliance-driven, fraud, and false-claims investigations that arise in employment contexts. Covers: Faragher/Ellerth affirmative defense preservation (Title VII 42 U.S.C. §2000e); EEOC 2024 Harassment Guidance 5-factor credibility framework; NLRA §7 Weingarten rights (420 U.S. 251 (1975)) and NLRB Banner Health System confidentiality limits; SOX §806/Dodd-Frank §922/OSHA §11(c) whistleblower protection matrix; Upjohn warnings and FRE 502 work-product preservation; Stored Communications Act 18 U.S.C. §2701 limits on electronic evidence; FRCP Rule 37(e) spoliation avoidance; UK ACAS Code of Practice 1 (2015) disciplinary and grievance procedural requirements; Employment Rights Act 1996 s.98 fair dismissal and British Home Stores v Burchell [1980] reasonable-belief test; Equality Act 2010 employer liability; PIDA 1998 whistleblower protection; UK GDPR/Data Protection Act 2018 employee monitoring constraints; EU Whistleblowing Directive 2019/1937 reporting-channel and confidentiality obligations; GDPR Art. 9 special-category data in investigations; German BetrVG §87/§102 works council co-determination; French CSE consultation (Code du Travail L.2312-8); Dutch WOR rights. Produces: investigation complexity tier (PRELIMINARY / STANDARD / COMPLEX / CRISIS); scoped mandate; privilege strategy memo; legal hold notices; tailored interview guides; evidence matrices; credibility scorecards; SUBSTANTIATED / PARTIALLY SUBSTANTIATED / UNSUBSTANTIATED / INCONCLUSIVE findings; remedial action plans with disciplinary escalation; regulatory reporting decision matrices; board-ready investigation reports; and Glass Box audit trails. Jurisdiction-agnostic core with US/UK/EU [JURISDICTION-SPECIFIC] markers.


# Legalcode Workplace Investigation

> **Disclaimer**: This skill provides a framework for AI-assisted workplace investigation
> planning and management. It does not constitute legal advice and does not create an
> attorney-client relationship. All outputs must be reviewed by qualified employment
> counsel — and, for regulated entities, by appropriately licensed professionals —
> before being used in any actual investigation, disciplinary proceeding, or regulatory
> response. Employment law and investigation obligations are highly jurisdiction-specific
> and fact-specific; no AI tool can verify current EEOC guidance letters, NLRB General
> Counsel memos, or local employment statutes. Privilege analysis is especially
> sensitive: conducting an investigation without proper privilege counsel guidance can
> inadvertently waive attorney-client privilege and expose investigation materials to
> litigation discovery. All statutory, regulatory, and case law references cited carry
> hallucination risk — verify against authoritative sources (EEOC.gov, NLRB.gov,
> ACAS.org.uk, EUR-Lex, court records) before relying on them in live matters.

---

## Purpose and Scope

This skill guides the complete execution of a workplace investigation — from the moment
a complaint, allegation, or whistleblower report is received through final findings,
remediation, and any required regulatory reporting. It focuses on **employment-law-centric
investigations** where the primary frameworks are labor and employment statutes rather
than securities, fraud, or criminal law.

**Covers:**

- Complaint triage and investigation complexity classification (Preliminary / Standard /
  Complex / Crisis)
- Scope determination and mandate drafting
- Investigator selection and conflict-of-interest screening (in-house HR, in-house
  counsel, external employment counsel, third-party investigators)
- Privilege preservation strategies (attorney-client, work product, joint defense)
- Legal hold and document preservation notice drafting
- ESI collection protocols and chain-of-custody standards
- Witness sequencing, interview guide construction, and Upjohn warning delivery
- Credibility assessment using the EEOC 5-factor methodology
- Evidence-to-allegation mapping and evidence matrix construction
- Findings classification (Substantiated / Partially Substantiated / Unsubstantiated /
  Inconclusive)
- Remedial action planning including disciplinary tiers, training, and process changes
- Regulatory reporting decision trees (EEOC, NLRB, OSHA, SRA, FCA, EU national
  authorities)
- Board and audit committee reporting for significant matters
- Glass Box audit trail for auditability and privilege log completeness

**Does not:**

- Replace the judgment of qualified employment counsel
- Provide legal advice on any specific matter
- Execute forensic collection or digital investigation tooling
- Draft final investigation reports without human review and sign-off
- Apply exclusively to securities fraud, financial crime, or criminal investigations
  (see `legalcode-internal-investigation` for corporate fraud/regulatory matters)
- Build the pre-investigation planning architecture (see `legalcode-investigation-plan-builder`)

**Relationship to sibling skills:**

- `legalcode-investigation-plan-builder` — pre-investigation architecture and intake
  triage (use before this skill for complex matters)
- `legalcode-internal-investigation` — corporate fraud, securities, and criminal
  compliance investigations with DOJ/SFO cooperation credit analysis
- `legalcode-whistleblower-program-builder` — building the whistleblower channel
  infrastructure that feeds complaints into this workflow

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic at its core. The applicable employment law framework
depends on the jurisdiction where the affected employees work — not where the employer
is incorporated.

**Primary jurisdictions covered:**

| Jurisdiction           | Primary Frameworks                                                                           |
| ---------------------- | -------------------------------------------------------------------------------------------- |
| **United States**      | Title VII, ADEA, ADA, EPA, NLRA, FLSA, SOX §806, Dodd-Frank §922, OSHA §11(c), EEOC Guidance |
| **United Kingdom**     | Equality Act 2010, ERA 1996, ACAS Code of Practice 1, PIDA 1998, UK GDPR/DPA 2018            |
| **European Union**     | EU Whistleblowing Directive 2019/1937, GDPR, national codetermination laws                   |
| **Australia** [VERIFY] | Fair Work Act 2009, Anti-Discrimination Acts (state), Public Interest Disclosure Act 2013    |
| **Canada** [VERIFY]    | Canadian Human Rights Act, provincial employment standards, PSECA, OHS Acts                  |

[JURISDICTION-SPECIFIC] Identify the primary work jurisdiction for each affected
employee at Step 2 — the analysis adapts to that jurisdiction's procedural and
substantive requirements throughout.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent or proceeding on incorrect assumptions about the matter's nature, the workflow
pauses and asks when:

- The answer would materially change the investigator selection, privilege strategy, or
  scope of the investigation
- Multiple valid investigation approaches exist (e.g., investigation vs. mediation vs.
  informal resolution)
- Regulatory reporting obligations are triggered but depend on fact-specific thresholds
- Risk tolerance or business urgency requires prioritization across competing needs

Use the ⟁ CLARIFY pattern (structured options with brief descriptions) wherever marked
below. If the user has already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept the Complaint or Referral

Accept the matter in any of these formats:

- **Written complaint**: Formal written complaint, HR intake form, or grievance letter
- **Oral complaint summary**: HR or manager's written record of an oral report
- **Whistleblower report**: Internal hotline report (with or without reporter identity)
- **Regulatory referral**: EEOC charge, NLRB charge, OSHA complaint, EU authority referral
- **Management referral**: Observed conduct, performance-related discovery, audit finding
- **Anonymous tip**: Documented with as much detail as known

Record the **intake date**, **reporter identity** (or "Anonymous"), **allegation summary**,
**named respondent(s)**, **witnesses mentioned**, and **any documents attached**.

If any of the following are present, escalate immediately to legal counsel before
proceeding:

- Potential criminal conduct (physical assault, theft, embezzlement, fraud)
- Regulatory subpoena or government inquiry on the same subject
- Named respondent is a senior executive or board member
- Matter involves potential class or collective exposure
- Reporter has retained outside counsel

### Step 2: Gather Context

**⟁ CLARIFY** — Before scoping the investigation, gather essential context:

1. **Allegation type** — What is the primary allegation?
   - Options: Harassment/hostile work environment, Discrimination (race/sex/age/disability/
     religion/national origin/other), Retaliation (for protected activity), Workplace
     violence or threat, Whistleblower/ethics hotline report, Code-of-conduct violation,
     Wage/hour or benefits violation, OSHA/safety complaint, Other misconduct
   - _Why this matters_: Determines the applicable legal framework, required procedural
     steps, and potential statutory reporting obligations.

2. **Jurisdiction(s)** — Where do the affected parties work?
   - Identify country, state/province, and any multi-jurisdiction complexity
   - Ask if any party works remotely in a different jurisdiction from the employer's HQ
   - _Why this matters_: Dictates which anti-discrimination and whistleblower statutes
     apply, which procedural requirements govern, and which regulatory agencies must be
     reported to.

3. **Complainant status** — What is the complainant's employment status?
   - Options: Current employee, Former employee (< 6 months), Former employee (> 6 months),
     Contractor/vendor, Applicant, Anonymous/unknown
   - _Why this matters_: Some protections (e.g., Dodd-Frank anti-retaliation) extend to
     former employees; contractor status affects the duty to investigate.

4. **Respondent seniority** — What is the respondent's role?
   - Options: Individual contributor, Manager/supervisor, Senior manager/director,
     Vice President or above, C-suite/Executive, Board member, Third party (client,
     vendor, contractor)
   - _Why this matters_: Determines whether Upjohn obligations arise, whether board
     or audit committee notification is needed, and whether standard HR investigation
     procedures apply or outside counsel must lead.

5. **Urgency and interim harm** — Is there ongoing harm?
   - Options: Immediate safety concern (threat/violence), Active ongoing harassment,
     No ongoing contact (parties separated), Reporter no longer at company, No immediate
     safety concern
   - _Why this matters_: Determines whether interim protective measures must be implemented
     before investigation begins.

6. **Regulatory filing status** — Has any external charge been filed?
   - Options: EEOC charge filed, State agency charge filed, NLRB charge filed, OSHA
     complaint filed, UK Employment Tribunal claim filed, EU regulatory report filed,
     No external filing, Unknown
   - _Why this matters_: An external charge creates a response deadline (EEOC: typically
     180 days from charge to agency investigation demand; NLRB: 6-month statute of
     limitations) and affects whether the investigation must be completed before or
     during the external proceeding.

If the user provides partial context, proceed with stated assumptions and flag them
explicitly.

### Step 3: Classify Investigation Complexity and Scope

Using the context from Step 2, classify the investigation into one of four tiers and
define the scope.

#### Investigation Complexity Tiers

| Tier            | Criteria                                                                                                                                                                     | Typical Investigator                                              | Timeline                                       |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------- |
| **PRELIMINARY** | Single complainant; single respondent; no senior leadership involved; no external charge; factual dispute limited; no privilege considerations                               | HR generalist (trained)                                           | 5–10 business days                             |
| **STANDARD**    | Multiple complainants or witnesses; manager-level respondent; possible discrimination/retaliation nexus; limited privilege analysis needed                                   | HR Business Partner or in-house employment counsel                | 15–30 business days                            |
| **COMPLEX**     | Senior/executive respondent; multiple allegations; regulatory charge filed; privilege considerations; potential legal exposure; cross-jurisdiction elements                  | Outside employment counsel or specialist third-party investigator | 30–60 business days                            |
| **CRISIS**      | C-suite or board member respondent; imminent litigation; government investigation; whistleblower to external agency; potential criminal exposure; media risk; class exposure | Outside employment counsel (lead) + forensic specialist           | 60+ business days; board notification required |

**⟁ CLARIFY** — Present the complexity tier assessment to the user and confirm:

- "Based on the intake information, I assess this as a [TIER] investigation. Does that
  align with your assessment, or do you have additional context that would change the tier?"
- If the user assesses differently: "You've characterized this as [DIFFERENT TIER]. Please
  share any additional context so I can align the investigation design accordingly."

#### Scope Determination

Define the scope in three dimensions:

1. **Temporal scope**: The period covered by the investigation (start date to present,
   or a defined look-back period). Default: from the first alleged incident to the present.

2. **Substantive scope**: The specific allegations to be investigated (not all connected
   issues the investigation might uncover — scope creep is an anti-pattern). Document what
   is in scope and what is expressly out of scope.

3. **Personnel scope**: Named respondents + potential witnesses. Note: if new witnesses
   reveal additional respondents during the investigation, a scope expansion memo must
   be drafted and approved before expanding the investigation.

**⟁ CLARIFY** — For matters where scope is ambiguous:

- "The complaint references conduct by both [Person A] and [Person B]. Should both be
  treated as respondents (separate investigations) or investigated as part of a single
  matter?"
- "The complaint covers events spanning 3 years. Should the full period be investigated,
  or would a look-back limited to [statute of limitations / policy effective date] be
  more appropriate given the circumstances?"

### Step 4: Investigator Selection and Mandate Design

Select the investigator using the matrix in the **Investigator Selection Reference**
section, then draft the investigation mandate.

#### Investigator Independence Screen

Run the following conflict-of-interest checks for every proposed investigator:

| Check                  | Question                                                                                | Fail Trigger                                                   |
| ---------------------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Reporting relationship | Does the investigator report to, or have the respondent in their reporting line?        | Any reporting connection — disqualify                          |
| Prior involvement      | Did the investigator previously advise on, or be informed of, the conduct alleged?      | Prior substantive knowledge — disqualify                       |
| Social relationship    | Close personal friendship with complainant or respondent?                               | Material personal connection — consider disclosure and recusal |
| Business interest      | Does the investigator have a business or compensation interest affected by the outcome? | Any material interest — disqualify                             |
| Prior complaints       | Has the investigator been the subject of a complaint involving the respondent?          | Mutual complaint history — disqualify                          |

[JURISDICTION-SPECIFIC: **UK**: ACAS guidance requires investigation by someone with
no prior involvement in the matter. The Employment Tribunal will scrutinize independence
if a dismissal results. **US**: No statutory independence requirement for internal HR
investigations, but loss of independence undermines the Faragher/Ellerth affirmative
defense.]

#### Mandate Document

Draft a written investigation mandate covering:

- Matter reference number
- Date mandate issued
- Investigator identity and role
- Allegation(s) to be investigated (verbatim from intake)
- Scope (temporal, substantive, personnel)
- Confidentiality obligations on the investigator
- Authority to access records, systems, and personnel
- Reporting chain (to whom findings are reported and when)
- Privilege designation (privileged legal investigation vs. HR investigation)
- Expected timeline and interim check-in schedule

### Step 5: Privilege Preservation and Legal Hold

#### Privilege Strategy

Before any investigation activity, determine the privilege designation for the
investigation.

| Mode                          | How to Designate                                                                                               | What Is Protected                                                          | Risks                                                                                                                         |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Attorney-client privilege** | Outside counsel or in-house counsel directs the investigation; communications made for purpose of legal advice | Counsel's communications, legal advice, direction to investigators         | Waived by disclosure to non-privileged parties; document metadata must be controlled                                          |
| **Work product**              | Investigation conducted in anticipation of litigation; documents prepared by or at direction of counsel        | Interview memoranda, draft reports, investigator notes                     | Fact work product less protected; opinion work product (mental impressions of counsel) is stronger; selective disclosure risk |
| **Hybrid**                    | HR business process + legal oversight                                                                          | HR process documents not privileged; legal oversight communications may be | Mixing privileged and non-privileged materials creates waiver risk                                                            |
| **No privilege (HR process)** | Investigation conducted as standard HR process, not at direction of counsel                                    | Nothing — all materials discoverable                                       | Creates evidentiary record for Faragher/Ellerth defense; no waiver risk; more transparent to employees                        |

**⟁ CLARIFY** — Ask the user (or direct them to employment counsel):

- "Should this investigation be designated as privileged (directed by counsel, protected
  from discovery) or as a non-privileged HR process (full documentation available for
  litigation use as an affirmative defense)? This decision should be made with employment
  counsel before any interviews are conducted."

[JURISDICTION-SPECIFIC: **US**: Upjohn Co. v. United States, 449 U.S. 383 (1981)
governs corporate attorney-client privilege; FRE 502 governs work-product protection.
**UK**: Legal professional privilege (advice and litigation privilege) governed by common
law; harder to maintain for HR-directed investigations. **EU/Germany**: Employees have
stronger data protection rights; privileged materials may still be subject to GDPR access
requests from data subjects.]

#### Legal Hold Notice

Issue a litigation hold/legal hold notice immediately upon decision to investigate.
The hold notice must:

1. Identify the case/matter name and reference number
2. Be sent to all custodians likely to have relevant ESI or documents
3. Identify the categories of documents to be preserved
4. Prohibit deletion, modification, or destruction of covered records
5. Suspend automatic deletion policies for relevant document categories
6. Require acknowledgment from each custodian
7. Be reissued if new custodians or document categories are identified

**Required custodians**: Complainant, respondent(s), named witnesses, any supervisor or
HR personnel with prior knowledge, IT/records management.

**Required document categories**: All communications between/about the parties during
the relevant period; HR files; performance reviews and discipline records; timekeeping
and payroll records; electronic communications (email, Slack, Teams, SMS); security and
access logs; CCTV footage (if applicable); calendar and scheduling records; any prior
complaints involving the respondent.

[JURISDICTION-SPECIFIC: **US**: FRCP Rule 37(e) governs spoliation sanctions for failure
to preserve ESI; Zubulake v. UBS Warburg, 220 F.R.D. 212 (S.D.N.Y. 2003) set the
standard for preservation duties. **UK**: Data protection obligations under UK GDPR may
limit how long certain records can be retained even under a legal hold. **EU**: GDPR
Art. 5(1)(e) storage limitation principle applies; document preservation must be justified
against competing data protection obligations.]

### Step 6: Document Preservation and Evidence Collection

#### Evidence Collection Protocol

Collect evidence in this sequence (preserve chain-of-custody at each step):

1. **HR file review**: Collect complainant's and respondent's complete HR files
   (personnel records, performance reviews, discipline history, prior complaints)
2. **Documentary evidence**: Collect all documents identified in the legal hold
3. **ESI collection**: Coordinate with IT for email, messaging, calendar, and access log
   collection; use forensic imaging for devices if misconduct is suspected
4. **Physical evidence**: Photograph, catalog, and secure any physical evidence (notes,
   physical objects, CCTV footage)
5. **Witness statements** (if any prior written statements exist): Collect and catalog

#### Chain-of-Custody Standards

For each piece of evidence:

- Assign a unique exhibit reference number (e.g., WI-2026-001-EX-001)
- Record: date collected, collected by, source/location, condition at collection
- Store in a secure, access-controlled location (physical or digital)
- Do not alter, annotate, or highlight original documents; work from copies
- Log every access to original evidence

[JURISDICTION-SPECIFIC: **UK**: Interception of private communications without consent
may violate RIPA 2000 and the IPA 2016; employer monitoring of employee communications
requires a lawful basis under UK GDPR Art. 6 and compliance with ICO Monitoring at
Work guidance. **EU**: GDPR Art. 6 and 9 require lawful basis and data minimization for
collecting employee personal data; German BDSG §26 imposes strict limits on employee
data processing for investigation purposes. **US**: Electronic monitoring of employee
communications on employer-owned systems is generally permissible with a computer use
policy in place; the Stored Communications Act (18 U.S.C. §2701) restricts accessing
stored communications on third-party servers without authorization.]

### Step 7: Witness Interview Planning and Execution

#### Witness Sequencing

Interview witnesses in this order to minimize contamination:

1. **Complainant first**: Obtain the full narrative of the alleged conduct
2. **Corroborating witnesses** (if any are named): Gather independent accounts
3. **Neutral witnesses**: Persons with potential information who are neither complainant
   nor respondent
4. **Respondent last**: Provide the respondent with a fair opportunity to respond to the
   specific allegations after all other evidence is collected

**Do not** interview the respondent before collecting corroborating evidence — this allows
the respondent to shape the narrative and pressure witnesses.

#### Upjohn Warning Script

If the investigation is designated as attorney-client privileged and conducted by or at
the direction of counsel, deliver an Upjohn warning to every employee interviewed:

> "I am [name], [in-house counsel / outside counsel] for [Company]. I am conducting this
> interview at the direction of [Company]'s legal department to gather facts so that the
> company can obtain legal advice. Our conversation is protected by the attorney-client
> privilege, but that privilege belongs to [Company], not to you personally. That means
> [Company] — not you — may decide to disclose or waive the privilege, including in
> litigation or government proceedings. You are not required to speak with me, but your
> cooperation is requested and expected as part of your employment obligations. Do you
> understand?"

[JURISDICTION-SPECIFIC: **US**: Upjohn Co. v. United States, 449 U.S. 383 (1981);
the warning is standard practice but the elements are not statutorily prescribed.
**UK**: No equivalent; employees should be informed that the investigation is confidential
and that they may be accompanied by a trade union representative or workplace colleague
under ERA 1996 s.10 (right to accompaniment at disciplinary/grievance meetings).
**EU**: Employees have rights under GDPR Art. 13/14 to be informed of how their personal
data will be used in the investigation; consider a data processing notice alongside the
Upjohn-equivalent disclosure.]

#### Union/Works Council Rights

[JURISDICTION-SPECIFIC]

**US — NLRA Weingarten Rights** [42 NLRB decisions since NLRB v. J. Weingarten, Inc.,
420 U.S. 251 (1975)]:

- Represented employees have the right to request union representation at any investigatory
  interview that the employee reasonably believes may result in discipline
- If the employee requests a union representative, the employer must: (a) grant the request
  and postpone the interview; (b) discontinue the interview; or (c) offer the employee the
  choice between proceeding without a representative or ending the interview
- **Weingarten rights do not apply to non-union employees** under current NLRB precedent
  (IBM Corp., 341 NLRB 1288 (2004))
- NLRB confidentiality limitations: Blanket confidentiality instructions to all witnesses
  may violate §8(a)(1); confidentiality instructions are only lawful when justified by a
  particularized need (NLRB v. Banner Health System, 362 NLRB 1108 (2015))

**UK — Right to Accompaniment** [ERA 1996 ss.10–15]:

- Workers have a statutory right to be accompanied by a trade union official or workplace
  colleague at disciplinary and grievance hearings
- The right does not extend to investigatory interviews unless the employer's policy or
  contractual terms confer it
- ACAS guidance recommends allowing a companion at investigatory interviews as best practice
- Failure to allow accompaniment at a disciplinary hearing can result in an 8-week pay award

**EU — Works Council/Co-determination** [JURISDICTION-SPECIFIC]:

- **Germany**: BetrVG §87(1)(1) gives the works council (Betriebsrat) co-determination
  rights over employee monitoring measures; §102 requires consultation before dismissal.
  Investigations involving employee data must be disclosed to the Betriebsrat.
- **France**: The CSE (Comité Social et Économique) must be consulted on significant
  changes to working conditions; Code du Travail L.2312-8 ff. Any new monitoring system
  requires CSE information and, in some cases, consultation.
- **Netherlands**: The Works Council (OR) under the Wet op de Ondernemingsraden (WOR)
  has information rights and in some cases veto rights over employee monitoring measures.

#### Interview Guide Structure

For each interview, prepare a structured guide:

```
INTERVIEW GUIDE — [Complainant / Respondent / Witness Name]
Matter: [Reference Number]
Date: [Date]
Investigator: [Name]
Privilege designation: [Privileged / Non-privileged HR]

OPENING:
- Introduce investigator and role
- Deliver Upjohn warning (if privileged) or right-to-accompaniment notice (UK)
- Explain purpose: fact-finding, not a disciplinary hearing
- Note confidentiality obligations and limitations (NLRB constraints in US)
- Note that notes will be taken and may be reviewed by company counsel
- Ask for consent to record (if recording is used; verify local law)

CORE QUESTIONS (open-ended, non-leading):
1. Tell me in your own words what happened on [date/period].
2. Where did this occur?
3. Who else was present?
4. What was said or done, as precisely as you can recall?
5. What was your reaction at the time?
6. Did you report this to anyone? If so, to whom, when, and what response did you receive?
7. Are there any documents, messages, or other records relevant to what you've described?
8. Is there anyone else who may have relevant information?
9. Is there anything else you believe I should know?

CLOSING:
- Summarize key points and ask for confirmation or correction
- Advise of confidentiality obligations (scope and limits)
- Provide contact information for follow-up
- Advise of non-retaliation policy and remind employee to report any adverse action
```

### Step 8: Credibility Assessment and Evidence Synthesis

#### EEOC 5-Factor Credibility Assessment

Apply the EEOC's 5-factor credibility methodology to each material witness account:

| Factor                             | Assessment Questions                                                                                                                                                                                                           | Weight |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| **1. Plausibility**                | Does the account make sense given the circumstances? Is it internally consistent? Does it align with what is known about the work environment?                                                                                 | High   |
| **2. Corroboration**               | Is the account corroborated by documentary evidence, ESI, or other witnesses? Are corroborating witnesses independent?                                                                                                         | High   |
| **3. Consistency**                 | Is the account consistent across different parts of the interview? Consistent with prior statements to HR or management? Consistent with how the witness behaved at the time (contemporaneous complaints, behavioral changes)? | High   |
| **4. Motive to fabricate or bias** | Does the witness have a reason to lie or exaggerate? Personal conflict with the respondent or complainant? Fear of discipline? Prior discipline by the respondent?                                                             | Medium |
| **5. Demeanor**                    | Was the account delivered calmly and specifically, or evasively and vaguely? (Use cautiously — demeanor evidence is unreliable for cross-cultural assessments)                                                                 | Low    |

**Credibility Scoring (per witness, per allegation):**

- **CREDIBLE**: Plausible account, corroborated, internally consistent, no significant motive to fabricate
- **PARTIALLY CREDIBLE**: Plausible and internally consistent but lacking corroboration, or corroborated but with motive concerns
- **UNCERTAIN**: Material inconsistencies, lack of corroboration, or significant motive to fabricate; requires additional investigation
- **NOT CREDIBLE**: Account contradicted by physical evidence, ESI, or multiple independent credible witnesses

**⟁ CLARIFY** — When credibility is genuinely uncertain between complainant and respondent:

- "Both the complainant's and respondent's accounts have plausible elements but are
  mutually exclusive. The available corroborating evidence does not clearly favor either
  account. Would you like me to: (A) designate the finding as Inconclusive and document
  the evidentiary stalemate; (B) recommend additional investigation steps to seek further
  corroboration; or (C) consult with employment counsel on burden-of-proof standards in
  this jurisdiction for this allegation type?"

#### Evidence Matrix

For each allegation, construct an evidence matrix:

```
ALLEGATION: [Description]

SUPPORTING EVIDENCE:
| Exhibit | Type | Source | Date | Relevance | Credibility |
|---------|------|--------|------|-----------|-------------|
| WI-XX-EX-001 | Email | [Name] Outlook | [Date] | [Description] | VERIFIED |

CONTRADICTING EVIDENCE:
| Exhibit | Type | Source | Date | Relevance | Credibility |
|---------|------|--------|------|-----------|-------------|

NEUTRAL/CONTEXT EVIDENCE:
| Exhibit | Type | Source | Date | Relevance |
|---------|------|--------|------|-----------|

MISSING EVIDENCE:
| Description | Why Missing | Effect on Finding |
|-------------|-------------|-----------------|
```

### Step 9: Findings Documentation and Classification

#### Standard of Proof

Apply the **preponderance of the evidence** standard (more likely than not, i.e., > 50%
probability) unless the applicable jurisdiction, governing policy, or contractual agreement
specifies a different standard.

[JURISDICTION-SPECIFIC: **UK**: Employment Tribunal claims require the Employment
Tribunal to decide on the balance of probabilities. Internal investigations applying a
higher standard than the Employment Tribunal will use may inadvertently preclude remedial
action that would withstand judicial scrutiny. **US**: Workplace investigations do not use
a judicial burden-of-proof standard, but courts assess whether the investigation was
reasonable and impartial under the Faragher/Ellerth framework.]

#### Findings Classification

| Classification              | Meaning                                                                                                                                            | Requirements                                                                                                                        |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **SUBSTANTIATED**           | The preponderance of evidence supports the allegation                                                                                              | Credible complainant account + corroborating evidence + no credible contradicting evidence sufficient to overcome the corroboration |
| **PARTIALLY SUBSTANTIATED** | Some but not all allegations are supported by evidence, or the evidence supports a lesser or different version of the allegation                   | Document which allegations are substantiated and which are not; explain the evidentiary basis for the distinction                   |
| **UNSUBSTANTIATED**         | The preponderance of evidence does not support the allegation                                                                                      | Document specifically what evidence was collected, why it was insufficient, and what standard was applied                           |
| **INCONCLUSIVE**            | Insufficient evidence to reach a finding on the preponderance standard, and additional investigation is not likely to produce dispositive evidence | Document the evidentiary stalemate; recommend interim and protective measures; advise on next steps                                 |

**Do not** use terminology like "unfounded" or "false" — these imply the complainant was
dishonest, which is a higher standard (and a retaliation risk) not required by the
investigation.

#### Self-Interrogation for SUBSTANTIATED or HIGH-EXPOSURE Findings

For any SUBSTANTIATED finding involving potential legal liability, or any finding that
will result in termination, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the finding follow logically from the evidence?
Would an Employment Tribunal / court / regulatory body, applying the relevant legal
standard, reach the same conclusion on this evidence?

**Pass 2 — Completeness**: Has all reasonably available evidence been collected and
considered? Were all material witnesses interviewed? Were all identified documents
reviewed? Is there any corroborating or contradicting evidence not yet collected?

**Pass 3 — Adversarial Challenge**: What is the strongest argument the respondent could
make against this finding? Under what circumstances would a reasonable investigator reach
a different conclusion? Has that argument been tested and rejected in the analysis?

### Step 10: Remedial Action Planning

#### Remediation Framework

Remediation must be: (1) proportionate to the severity of the conduct; (2) reasonably
calculated to end the conduct and prevent recurrence; (3) protective of the complainant;
and (4) consistent with prior discipline for similar conduct (to avoid disparate
treatment claims).

**Disciplinary Tier Matrix:**

| Tier                             | Conduct                                                                                                                                              | Typical Remediation                                                                                                                     |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Tier 1 — Informal**            | Minor policy violation; first occurrence; no harm                                                                                                    | Counseling memo; additional training; supervisory check-in                                                                              |
| **Tier 2 — Formal Warning**      | Repeated minor violations; single moderate violation; inappropriate but not severe conduct                                                           | Written warning in HR file; mandatory training; performance plan; possible temporary suspension                                         |
| **Tier 3 — Suspension/Demotion** | Serious violation; pattern of conduct; conduct creating legal exposure but not egregious                                                             | Unpaid suspension; demotion; removal from supervisory role; mandatory corrective action plan                                            |
| **Tier 4 — Termination**         | Severe violation; criminal conduct; egregious single event; prior formal warnings for similar conduct; conduct making continued employment untenable | Immediate termination; consider garden leave or separation agreement; assess post-employment obligations (non-compete, confidentiality) |

**Structural Remediation** (beyond individual discipline):

- Policy revisions (if the conduct revealed a policy gap)
- Training programs (targeted to identified risk areas)
- Process changes (e.g., approval requirements, reporting lines)
- Monitoring enhancements (e.g., audit triggers for high-risk areas)
- Anti-retaliation plan for complainant (modified reporting line, non-contact directive,
  periodic check-ins)

**Complainant Remediation**:

- Address any adverse action taken against the complainant during the period of alleged
  conduct (pay adjustments, reinstatement of opportunities denied)
- Issue a non-contact or anti-retaliation directive to the respondent
- Provide the complainant with a status update (without sharing the respondent's
  confidential disciplinary action)

[JURISDICTION-SPECIFIC: **UK**: ACAS Code of Practice requires proportionality between
offence and sanction; dismissal for a first offence is only appropriate for gross
misconduct. Employment Tribunals apply the band-of-reasonable-responses test (Iceland
Frozen Foods v Jones [1982] IRLR 439). **US**: "At-will" employment generally allows
termination without cause, but consistency with prior discipline for similar conduct is
critical to avoiding disparate treatment claims. **EU**: Many member states require cause
for dismissal and prior warnings; German KSchG requires social justification (soziale
Rechtfertigung) for dismissals at employers with 10+ employees.]

### Step 11: Regulatory Reporting Decision

#### Reporting Obligation Matrix

| Trigger                            | Jurisdiction       | Agency                                        | Deadline                                                                                                                | Notes                                                                                                              |
| ---------------------------------- | ------------------ | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| EEOC charge filed                  | US (federal)       | EEOC                                          | Position statement typically due 30 days from charge notice; investigation not required to be completed                 | Faragher/Ellerth defense requires prompt, thorough investigation                                                   |
| NLRB charge filed                  | US (federal)       | NLRB                                          | 6-month statute of limitations on underlying unfair labor practice                                                      | Confidentiality instructions issued pre-charge may be scrutinized                                                  |
| OSHA §11(c) complaint              | US (federal)       | OSHA                                          | No mandated internal investigation timeline; OSHA has 90-day investigation period                                       | Employer must demonstrate legitimate, non-retaliatory reason for adverse action                                    |
| SOX §806 whistleblower             | US (federal)       | OSHA (primary); de novo in federal court      | OSHA must complete investigation within 180 days of complaint                                                           | SOX §806 (18 U.S.C. §1514A) covers companies with registered securities; includes contractors of covered companies |
| Dodd-Frank §922 whistleblower      | US (federal)       | SEC                                           | No mandated investigation timeline                                                                                      | 15 U.S.C. §78u-6; covers disclosures to SEC directly; employer anti-retaliation applies                            |
| OSHA safety complaint              | US (federal/state) | OSHA / State-plan agency                      | OSHA has 6-month investigation window                                                                                   | Employer must preserve safety records and cooperate                                                                |
| Employment Tribunal claim          | UK                 | Employment Tribunal / ACAS early conciliation | ACAS early conciliation: 1 month + 2-week extension; ET Response: 28 days from receipt                                  | ACAS early conciliation is mandatory before ET claim                                                               |
| Grievance (unfiled)                | UK                 | Internal HR / ACAS                            | ACAS Code: no set deadline but prompt investigation required                                                            | Failure to follow ACAS Code allows ET to uplift any award by up to 25%                                             |
| Equality Act complaint             | UK                 | EHRC (systemic only) / ET                     | Same as ET above                                                                                                        | Individual claims via ET; EHRC enforcement for systemic issues                                                     |
| PIDA whistleblower                 | UK                 | Various (ET, regulatory bodies)               | ET claim limitation: 3 months less one day from detriment or dismissal                                                  | Protected disclosure must be to prescribed person or employer                                                      |
| EU Whistleblowing Directive report | EU Member States   | National competent authority                  | Directive 2019/1937: internal report → external report timeline; acknowledgment within 7 days; feedback within 3 months | National implementations vary; some MS require internal reporting channel acknowledgment within 7 days             |
| GDPR data breach                   | EU/UK              | DPA (e.g., ICO, BfDI)                         | 72 hours (GDPR Art. 33); [VERIFY national implementations]                                                              | If investigation evidence includes personal data breach, GDPR reporting may be triggered independently             |

**⟁ CLARIFY** — If a regulatory charge or external investigation is already underway:

- "A [EEOC/NLRB/ET/other] charge has been filed. This affects the timeline, privilege
  strategy, and whether the internal investigation findings can be used in the external
  proceeding. I recommend the following coordination steps — please confirm with employment
  counsel before proceeding."

#### Voluntary Self-Disclosure Considerations

If the investigation reveals potential violations of law (not just internal policy):

- Consult with employment counsel and (where relevant) regulatory counsel on whether
  voluntary disclosure to the relevant agency would be appropriate
- Consider cooperation credit (DOJ Monaco Memo Sep. 2022 / CEP Nov. 2024 for criminal
  matters; EEOC conciliation incentives for civil matters)
- Document the disclosure decision and its rationale in the privileged investigation record

### Step 12: Final Investigation Report and Delivery

Produce the investigation report using the **Output Format Template** below. Before
delivering the final report:

1. Run the **Citation Quality Gates** (see Quality Frameworks section)
2. Apply the **Self-Interrogation** protocol to all SUBSTANTIATED or HIGH-EXPOSURE findings
3. Confirm the **Confidence Score** for each material finding
4. Complete the **Glass Box Audit Trail**
5. Have the report reviewed by employment counsel before disclosure to any party

---

## Investigation Complexity Tier Reference

### PRELIMINARY Tier Indicators

- Single complainant, single respondent
- Allegation is factually limited (single incident or short time period)
- No seniority differential (peers or non-supervisory context)
- No prior complaints involving either party
- No regulatory charge filed or expected
- No privilege considerations (standard HR process)
- No union representation or works council notification required

### STANDARD Tier Indicators

- 2–5 witnesses needed
- Manager-level respondent (not senior leadership)
- Pattern of conduct over months (not years)
- Possible discrimination or retaliation nexus requiring legal analysis
- Some privilege analysis helpful but not complex
- Potential ET/EEOC/agency claim (not yet filed)

### COMPLEX Tier Indicators

- Senior or executive-level respondent
- Multiple allegations across multiple complainants
- External charge already filed
- Works council or union notification required
- Cross-jurisdiction elements (employees in multiple countries)
- Privilege strategy materially affects how the investigation is conducted
- Potential class or collective exposure
- Significant documentary and ESI evidence requiring forensic analysis

### CRISIS Tier Indicators

- C-suite, board member, or founding team respondent
- Government investigation (grand jury, regulatory inquiry, SEC CID)
- Whistleblower has reported externally (to SEC, DOL, OSHA, Eurojust)
- Potential criminal exposure for the company or individual
- Media attention or material reputational risk
- Imminent or pending litigation
- Potential class or collective action

---

## Investigator Selection Reference

| Investigator Type                           | Best For                                                                                                 | Key Advantage                                                     | Key Risk                                                                     |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **HR Generalist (trained)**                 | PRELIMINARY tier; policy violations; straightforward factual disputes                                    | Speed; employee familiarity; cost-effective                       | May lack legal expertise; harder to defend independence                      |
| **HR Business Partner (senior)**            | STANDARD tier; manager-level respondents; pattern allegations                                            | HR law knowledge; organizational awareness                        | Conflicts if they manage the relevant business unit                          |
| **In-House Employment Counsel**             | STANDARD–COMPLEX; matters requiring legal analysis; privilege preferred                                  | Privilege available; legal expertise; institutional knowledge     | Conflicts from prior business advice role; privilege may chill documentation |
| **Outside Employment Counsel**              | COMPLEX–CRISIS; senior/executive respondents; external charges; high legal exposure                      | Strong privilege protection; independence; regulatory credibility | Cost; potential unfamiliarity with company culture                           |
| **Third-Party Investigator** (non-attorney) | STANDARD–COMPLEX; matters where attorney privilege is not needed; matters requiring investigative skills | Perceived independence; investigative expertise                   | No attorney-client privilege; legal analysis capability limited              |
| **Forensic Specialist**                     | COMPLEX–CRISIS; ESI-heavy matters; criminal conduct suspected; digital evidence                          | Chain-of-custody expertise; court-admissible evidence             | Cost; may alarm employees and escalate matter                                |

---

## Privilege Framework Reference

### Attorney-Client Privilege (US)

**Requirements** (Upjohn Co. v. United States, 449 U.S. 383 (1981)):

1. Communication must be between an attorney (in-house or outside) and a client (corporate employees)
2. Communication must be made for the purpose of obtaining legal advice
3. Communication must be confidential (not shared outside the privilege group)
4. Client must be the corporation (not the individual employee)

**Investigation privilege requires:**

- Counsel must direct the investigation — not merely be copied on it
- Interview memoranda must reflect counsel's legal analysis, not just factual summaries
- All communications within the privilege group must be marked "Privileged and Confidential — Attorney-Client Communication"
- No disclosure to board members, HR personnel, or business leaders outside the need-to-know group without careful privilege analysis

**Work Product Doctrine** (FRE 502; FRCP Rule 26(b)(3)):

- Protects documents prepared in anticipation of litigation
- Fact work product: can be overcome by substantial need
- Opinion work product: near absolute protection for mental impressions of counsel
- Selective disclosure to one party can destroy protection against others

### Legal Professional Privilege (UK)

**Advice privilege**: Confidential communications between lawyer and client seeking/giving legal advice
**Litigation privilege**: Communications made for the dominant purpose of pending or reasonably anticipated litigation

**Key differences from US privilege:**

- Communications with third parties (e.g., investigators, forensic specialists) are covered by litigation privilege only if litigation is reasonably contemplated and the dominant purpose is obtaining evidence for that litigation
- In-house lawyers: advice privilege applies to genuine legal advice; business advice is not protected
- PIDA disclosures: privilege may be overridden if the investigation concerns a public interest matter

### EU/GDPR Intersection

Under GDPR, employees have the right to access their personal data (Art. 15) — including
personal data collected during the investigation. Privilege does not automatically override
GDPR subject access rights in EU jurisdictions. Consider:

- Data minimization: collect only personal data necessary for the investigation
- Purpose limitation: investigation data should not be repurposed for other HR decisions
- Retention: establish a clear retention period for investigation records
- [JURISDICTION-SPECIFIC: Germany: BDSG §26 permits processing employee data for
  investigation purposes only where there is concrete suspicion of a criminal offence or
  serious policy violation; proportionality assessment required]

---

## Severity Classification

Every finding in the investigation report receives one of these classifications:

| Classification              | Icon | Meaning                                        | Required Action                                                                                                               |
| --------------------------- | ---- | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **SUBSTANTIATED**           | 🔴   | Preponderance supports the allegation          | Immediate remediation; document disciplinary decision; escalate to senior leadership if COMPLEX/CRISIS tier                   |
| **PARTIALLY SUBSTANTIATED** | 🟠   | Evidence supports some but not all allegations | Proportionate remediation for substantiated elements; document distinction between substantiated and unsubstantiated elements |
| **UNSUBSTANTIATED**         | 🟡   | Evidence does not support the allegation       | No discipline of respondent; confirm no retaliation against complainant; consider whether complainant acted in good faith     |
| **INCONCLUSIVE**            | ⚪   | Insufficient evidence to reach finding         | Implement protective measures; consider further investigation options; document the evidentiary stalemate                     |

Each finding also receives a **Confidence Score** (0.0–1.0):

- 0.95–1.0: Strong corroboration; clear credibility assessment; no significant contrary evidence
- 0.80–0.94: Good corroboration; credibility favors one side; minor uncertainty remains
- 0.60–0.79: Credibility assessment favors one side but corroboration is limited
- 0.40–0.59: Genuine evidentiary uncertainty; finding may warrant escalation to counsel
- Below 0.40: Insufficient basis for finding; classify as INCONCLUSIVE

---

## Prioritization Framework

Prioritize remediation actions using this tier structure:

**IMMEDIATE (within 2 business days of substantiated finding)**

- Any conduct posing ongoing safety or harm risk
- Any retaliation risk against complainant
- Removal of respondent from supervisory role pending final discipline determination
- Notification to board or audit committee (CRISIS tier only)
- Mandatory regulatory reporting obligations

**NEAR-TERM (within 5–10 business days of final report)**

- Final discipline decision and implementation
- Anti-retaliation directive to respondent
- Complainant status update and remedial measures
- Policy revision or gap closure identified during investigation
- Non-contact directives between parties

**BACKGROUND (within 30–60 days of final report)**

- Mandatory training for respondent (if not terminated) and work unit
- Process improvements and monitoring enhancements
- Manager/supervisor training on recognition and reporting
- Investigation lessons-learned memo for legal files
- Annual review trigger for policy revision

---

## Quality Frameworks

### Citation Quality Gates

Run these 5 gates silently before delivering the final investigation report. If any gate
fails, revise before delivering.

| Gate           | Rule                                                                                                                                     | Fail Action                                                                           |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Source**     | Every legal claim (statutory, regulatory, or case law) cites a specific provision or authority                                           | Add citation or mark "[UNVERIFIED — counsel to confirm]"                              |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction (EEOC Guidance note, ACAS Code §, EUR-Lex Regulation number) | Fix format                                                                            |
| **Currency**   | Every cited provision has been checked for amendments or repeal since the last known version                                             | Flag "[CHECK CURRENCY — may have been amended]"                                       |
| **Domain**     | Analysis stays within the employment-law scope of the applicable jurisdiction; no bleed of concepts from other jurisdictions             | Remove or flag jurisdictional assumptions                                             |
| **Confidence** | Uncertainty is explicitly stated, not hidden; all findings include a confidence score                                                    | Add confidence qualifier; do not present uncertain findings as definitive conclusions |

### Self-Interrogation for SUBSTANTIATED or HIGH-EXPOSURE Findings

For any finding classified as SUBSTANTIATED where the likely outcome is termination or
significant legal exposure, apply this 3-pass review before finalizing the report:

**Pass 1 — Legal Chain Integrity**: Does the finding follow logically from the evidence?
Would an Employment Tribunal, EEOC, or court applying the relevant legal standard reach
the same conclusion?

**Pass 2 — Completeness**: Has all reasonably available evidence been collected and
considered? Were all material witnesses interviewed? Are there documents, systems, or
access logs not yet reviewed that might affect the finding?

**Pass 3 — Adversarial Challenge**: What is the strongest argument the respondent's
counsel could make against this finding? Under what circumstances would a reasonable
investigator reach a different conclusion? Has that argument been considered and rejected?

Record the outcome as: `self_interrogation: PASS` (no revision) or `self_interrogation:
REVISED` (finding or confidence score adjusted).

### Confidence Scoring

| Level        | Range     | Meaning                                                                          | Action                                                      |
| ------------ | --------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Multiple independent corroborating sources; no credible contrary evidence        | State finding with full confidence                          |
| **High**     | 0.80–0.94 | Credible account + documentary corroboration; minor credibility questions remain | State finding with brief caveat                             |
| **Probable** | 0.60–0.79 | Credible account; corroboration limited or indirect; some contrary evidence      | State finding with explicit reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing credible accounts; corroboration absent           | Classify as INCONCLUSIVE; escalate to counsel               |
| **Unlikely** | 0.0–0.39  | Account lacks plausibility or directly contradicted                              | Do not substantiate; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Include a completed Glass Box audit trail in every final investigation report:

```yaml
glass_box:
  skill_name: "legalcode-workplace-investigation"
  matter_reference: "[Matter reference number]"
  allegation_type: "[Harassment / Discrimination / Retaliation / Misconduct / Whistleblower / Other]"
  complexity_tier: "[PRELIMINARY / STANDARD / COMPLEX / CRISIS]"

  # Parties and jurisdiction
  complainant_status: "[Current employee / Former / Contractor / Anonymous]"
  respondent_seniority: "[IC / Manager / Senior Manager / VP+ / C-suite / Board]"
  primary_jurisdiction: "[Country / State]"
  secondary_jurisdictions: "[If any]"
  governing_employment_law: "[Title VII + EEOC / ERA 1996 + Equality Act / EU Directive / Other]"

  # Investigator
  investigator_type: "[HR / In-house counsel / Outside counsel / Third-party]"
  privilege_designation: "[Attorney-client + work product / Non-privileged HR process / Hybrid]"
  upjohn_warning_delivered: "[Yes / No / Not applicable]"
  union_weingarten_rights_noted: "[Yes / No / Not applicable — jurisdiction]"
  works_council_notified: "[Yes / No / Not required]"

  # Process integrity
  legal_hold_issued: "[Date / Not required]"
  legal_hold_custodians: "[Number of custodians]"
  interviews_conducted: "[Number]"
  witnesses_interviewed: "[List of roles — not names in report]"
  documents_reviewed: "[Approximate volume]"
  esи_collected: "[Yes / No / Not required]"

  # Quality frameworks
  legalcode_mcp: "[Connected / Not connected]"
  citation_quality_gates: "[PASS / FAIL — specify gate if failed]"
  self_interrogation: "[PASS / REVISED / Not triggered]"
  confidence_distribution:
    substantiated_findings: "[Confidence scores]"
    unsubstantiated_findings: "[Confidence scores]"
    inconclusive_findings: "[Confidence scores]"

  # Regulatory
  external_charge_filed: "[Yes — agency / No]"
  regulatory_reporting_triggered: "[List if any]"
  voluntary_disclosure_considered: "[Yes / No / Not applicable]"
  cooperation_credit_assessed: "[Yes / No / Not applicable]"

  # Findings and outcomes
  findings_summary:
    - allegation: "[Description]"
      classification: "[SUBSTANTIATED / PARTIALLY / UNSUBSTANTIATED / INCONCLUSIVE]"
      confidence: "[Score]"
  remediation_tier: "[IMMEDIATE / NEAR-TERM / BACKGROUND]"

  # Limitations
  limitations:
    - "[Any scope limitations — what was not investigated and why]"
    - "[Any evidence not collected and why]"
    - "[Any jurisdiction-specific advice not provided due to legalcode-mcp not connected]"
  assumptions:
    - "[Key assumptions made during the investigation]"

  reviewer: "AI-assisted — all findings must be reviewed by qualified employment counsel before use"
```

---

## Anti-Patterns

What NOT to do when conducting a workplace investigation:

1. **Starting interviews before legal hold is issued** — Alerting respondents or witnesses
   before issuing a document hold risks spoliation of evidence; failure to preserve ESI
   can result in sanctions under FRCP Rule 37(e) and adverse inference instructions.

2. **Interviewing the respondent first** — Interviewing the respondent before gathering
   corroborating evidence allows the respondent to shape the narrative, pressure witnesses,
   and destroy or explain away evidence before it is collected.

3. **Promising absolute confidentiality** — Telling witnesses "this conversation will be
   completely confidential" is both untrue (the company may be required to disclose the
   investigation in litigation or regulatory proceedings) and potentially an NLRA violation
   if it constitutes a blanket confidentiality instruction without particularized need.

4. **Conflating investigation with discipline** — The investigator must remain neutral and
   should not be the person who makes the discipline decision; a single investigator-discipliner
   is an anti-pattern that undermines the procedural fairness of the process and is specifically
   criticized in ACAS guidance.

5. **Documenting credibility conclusions without evidence basis** — Conclusions like
   "the respondent seemed sincere" without supporting evidence basis are not credibility
   assessments; they are impressionistic guesses that cannot withstand legal scrutiny.

6. **Using "unfounded" or "false" as a finding classification** — These classifications
   imply the complainant fabricated the allegation, which requires a higher evidentiary
   standard than the investigation typically achieves and creates significant retaliation risk.

7. **Applying the same investigation template to all allegation types** — A harassment
   investigation requires different expertise, different questions, and different legal
   framework analysis than a financial fraud investigation; one-size templates produce
   inadequate analyses.

8. **Ignoring the complainant after intake** — Failing to provide status updates (without
   sharing confidential disciplinary information) creates a perception of indifference
   and increases the risk of retaliation claims and external escalation.

9. **Failing to address the Weingarten or accompaniment right** — Overlooking an
   employee's right to union representation (US) or the right to accompaniment (UK) at an
   investigatory interview that may result in discipline is an unfair labor practice and
   can render subsequent disciplinary action procedurally unfair.

10. **Scope creep without a scope expansion memo** — Expanding the investigation to cover
    new allegations or additional respondents discovered mid-investigation without formally
    amending the scope creates confusion, privilege gaps, and inconsistent treatment.

11. **Failing to distinguish between attorney-client and work-product protection** —
    These are separate doctrines with separate requirements; designating all investigation
    documents as "privileged" without understanding whether they meet the elements of each
    protection leads to privilege waiver.

12. **Overlooking works council or union notification obligations** — In Germany (BetrVG §102),
    dismissal without works council consultation is void; in France, CSE consultation
    obligations for significant changes are mandatory; failing to consult results in
    procedurally defective terminations.

13. **Treating past disciplinary history inconsistently** — Imposing more severe discipline
    on a protected-class respondent for the same conduct as a non-protected-class respondent
    who received lesser discipline is disparate treatment under Title VII / Equality Act;
    always check prior discipline for comparable conduct before setting the disciplinary tier.

14. **Disclosing the investigation's findings or conclusions to the respondent in the presence
    of the complainant** — Creating a confrontational disclosure setting is not a mediation;
    it re-traumatizes complainants, undermines investigation confidentiality, and may
    constitute harassment itself.

15. **Interviewing witnesses in groups** — Group interviews allow witnesses to synchronize
    accounts; each witness must be interviewed separately and should be advised not to
    discuss the investigation with other employees (subject to NLRB limitations).

16. **Applying US employment law standards to UK or EU employees** — At-will employment,
    the EEOC's credibility framework, and Faragher/Ellerth do not translate to UK or EU
    law; the investigation framework must be adapted to the applicable jurisdiction's
    procedural and substantive standards.

17. **Failing to assess the EU Whistleblowing Directive's reporting channel requirements** —
    Since December 2023, all EU member states' implementations require employers with 50+
    employees to maintain internal reporting channels with specific acknowledgment (7 days)
    and feedback (3 months) obligations; conducting an investigation without checking these
    obligations creates regulatory exposure.

18. **Closing the investigation without an anti-retaliation check-in** — The investigation
    closes the fact-finding phase, but the compliance obligation continues; failing to
    schedule follow-up contact with the complainant to check for retaliation within 30–60
    days of the investigation's close is the most common post-investigation failure.

19. **Using the investigation report as a termination letter** — The investigation report
    documents facts and findings; the employment decision and rationale should be in a
    separate document, reviewed by employment counsel, that addresses the applicable
    legal standard for termination in the relevant jurisdiction.

20. **Failing to update the legal hold when new evidence or custodians are identified** —
    A legal hold is not a single document; it must be updated as the investigation scope
    expands; failure to issue supplemental holds to newly identified custodians can result
    in spoliation sanctions even if the original hold was timely.

---

## Writing Standards

Apply these standards before delivering any investigation output:

1. **Evidence first, conclusion second**: State the evidence before the conclusion it
   supports (e.g., "Email chain (EX-007) shows [description] — this supports a finding
   that..." not "The respondent behaved inappropriately, as shown by email EX-007").

2. **Active voice throughout**: Write "The complainant reported that [Name] said..." not
   "It was reported that statements were allegedly made...".

3. **Specific facts, not characterizations**: "On [date], [Name] sent the following message:
   [exact text]" not "inappropriate messages were sent."

4. **Legal conclusions require legal authority**: Do not write "This conduct constitutes
   sexual harassment" without citing the applicable statutory or regulatory standard.

5. **Tense discipline**: Use past tense for facts ("the respondent said"); use present
   tense for legal standards ("Title VII prohibits").

6. **No double negatives in findings**: "The evidence does not support the allegation"
   not "The allegation is not unsupported."

7. **Plain language for non-attorney readers**: Investigation reports are often read by HR
   leaders, business executives, and complainants; avoid legal jargon without explanation.

8. **Separate facts from findings**: Use clearly labeled sections — "Factual Findings" and
   "Legal/Policy Analysis" must be distinct so that attorneys can assess the factual record
   independently of the investigator's conclusions.

9. **Date-stamp and version-control every draft**: Investigation reports go through multiple
   drafts; number each draft and record the date and drafter to maintain privilege log integrity.

10. **Quality gate before delivery**: Confirm all [VERIFY] tags have been resolved or escalated
    to counsel; confirm all confidence scores are stated; run Citation Quality Gates.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- At Step 4 (privilege framework) and Step 11 (regulatory reporting), search for current
  statutory text and regulatory guidance for the applicable jurisdiction
- Search for recent case law on: Faragher/Ellerth affirmative defense, NLRB confidentiality
  instructions, EU Whistleblowing Directive national implementations, UK Employment Tribunal
  procedural fairness
- Search for current EEOC, NLRB, or ICO enforcement guidance relevant to the allegation type
- Save verified authorities to `/tmp/legalcode-wi-authority-[matter-ref].md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp (graceful degradation):**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Direct the user to verify citations against: EEOC.gov, NLRB.gov, ACAS.org.uk, EUR-Lex,
  relevant national court databases before relying on any cited authority in live matters
- Focus analysis on procedural quality, evidence framework, and investigator guidance
  rather than jurisdiction-specific legal substance

---

## Output Format Template

````markdown
# Workplace Investigation Report

> CONFIDENTIAL — ATTORNEY-CLIENT PRIVILEGED / ATTORNEY WORK PRODUCT
> [OR: CONFIDENTIAL — HR PROCESS — NOT SUBJECT TO ATTORNEY-CLIENT PRIVILEGE]
> This report contains sensitive employment information. Distribution is restricted to:
> [list recipients]

## 1. Executive Summary

**Matter Reference**: [WI-YYYY-NNN]
**Investigation Type**: [Harassment / Discrimination / Retaliation / Misconduct / Whistleblower]
**Investigation Tier**: [PRELIMINARY / STANDARD / COMPLEX / CRISIS]
**Date Complaint Received**: [Date]
**Date Investigation Opened**: [Date]
**Date Report Finalized**: [Date]
**Investigator**: [Name / Role / Designation — in-house or outside counsel]
**Privilege Designation**: [Attorney-client + work product / Non-privileged HR process]
**Primary Jurisdiction**: [Country / State]

**Overall Finding**: [SUBSTANTIATED / PARTIALLY SUBSTANTIATED / UNSUBSTANTIATED / INCONCLUSIVE]
**Recommended Remediation Tier**: [IMMEDIATE / NEAR-TERM / BACKGROUND]

[2–3 sentence executive summary of the allegation, investigation process, and key finding]

---

## 2. Allegation Summary

**Complainant**: [Role/Department — do not use name in widely distributed reports]
**Respondent**: [Role/Department]
**Allegation(s)**:

| #   | Allegation    | Dates     | Persons Involved |
| --- | ------------- | --------- | ---------------- |
| 1   | [Description] | [From–To] | [Roles]          |
| 2   | [Description] | [From–To] | [Roles]          |

---

## 3. Investigation Process

**Investigation scope**: [Description of temporal, substantive, and personnel scope]
**Legal hold issued**: [Date / Custodians covered]
**Documents reviewed**: [Volume / types]
**ESI reviewed**: [Yes / No / Systems accessed]
**Interviews conducted**: [Number and roles — not names]

| Interview # | Witness Role | Date   | Duration | Upjohn Warning?  |
| ----------- | ------------ | ------ | -------- | ---------------- |
| 1           | [Role]       | [Date] | [mins]   | [Yes / No / N/A] |

---

## 4. Factual Findings

### Allegation 1: [Description]

**Evidence reviewed**:
| Exhibit | Type | Source | Date | Summary of Relevance |
|---------|------|--------|------|---------------------|
| WI-EX-001 | Email | [System] | [Date] | [Description] |

**Witness credibility assessments**:
| Witness Role | Account Summary | Credibility Rating | Basis |
|-------------|----------------|-------------------|-------|
| Complainant | [Summary] | [CREDIBLE / PARTIALLY / UNCERTAIN] | [Brief basis] |
| Respondent | [Summary] | [CREDIBLE / PARTIALLY / UNCERTAIN] | [Brief basis] |
| Witness 1 | [Summary] | [CREDIBLE / PARTIALLY / UNCERTAIN] | [Brief basis] |

**Factual finding**: [What the evidence establishes on the preponderance standard]

---

## 5. Policy/Legal Analysis

### Applicable Standards

- [Statute/regulation/policy] — [How it applies to this allegation]

### Analysis

[Evidence-to-standard mapping; identify where evidence meets or does not meet the
applicable standard; cite legal authority with [VERIFY] tag if unverified]

---

## 6. Findings and Confidence Scores

| Allegation | Classification                                               | Confidence | Basis Summary |
| ---------- | ------------------------------------------------------------ | ---------- | ------------- |
| 1          | [SUBSTANTIATED / PARTIALLY / UNSUBSTANTIATED / INCONCLUSIVE] | [0.0–1.0]  | [Brief]       |
| 2          | [SUBSTANTIATED / PARTIALLY / UNSUBSTANTIATED / INCONCLUSIVE] | [0.0–1.0]  | [Brief]       |

---

## 7. Remedial Action Recommendations

### Immediate (within 2 business days)

- [Action item] — Owner: [Role] — Deadline: [Date]

### Near-Term (within 5–10 business days of final report)

- [Action item] — Owner: [Role] — Deadline: [Date]

### Background (within 30–60 days)

- [Action item] — Owner: [Role] — Deadline: [Date]

### Complainant Remediation

- [Anti-retaliation measures; status update protocol; remediation for any adverse action]

---

## 8. Regulatory Reporting Analysis

| Agency                             | Trigger   | Status                      | Deadline | Action            |
| ---------------------------------- | --------- | --------------------------- | -------- | ----------------- |
| [EEOC / NLRB / OSHA / ICO / Other] | [Trigger] | [Triggered / Not triggered] | [Date]   | [Required action] |

---

## 9. Quality Assurance

**Citation Quality Gates**: [PASS / FAIL — specify gate]
**Self-Interrogation** (SUBSTANTIATED findings): [PASS / REVISED / Not triggered]
**Confidence distribution**: [Summary of confidence scores across findings]
**[VERIFY] tags remaining**: [Number — 0 = all resolved]

---

## 10. Glass Box Audit Trail

```yaml
[Insert completed Glass Box YAML block]
```
````

---

## 11. Appendices

**Appendix A**: Evidence Index (all exhibits)
**Appendix B**: Interview memoranda (privileged — restricted distribution)
**Appendix C**: Legal hold notices
**Appendix D**: Relevant policy provisions
**Appendix E**: Regulatory citation index with [VERIFY] status

```

---

## Localization Notes

When adapting this skill for a specific jurisdiction, replace [JURISDICTION-SPECIFIC] markers
as follows:

| Marker Location | US Adaptation | UK Adaptation | EU Adaptation |
|----------------|--------------|--------------|--------------|
| Investigation procedure | EEOC guidance; NLRB rules; state FEPA | ACAS Code of Practice 1; ET procedural rules | EU WB Directive + national implementation |
| Privilege | FRE 502; Upjohn (449 U.S. 383) | LPP (advice + litigation); IBA Rule 2.4 | National privilege law; GDPR Art. 15 tension |
| Right to accompaniment | Weingarten (NLRA §7; 420 U.S. 251) | ERA 1996 ss.10–15 | National works council / trade union law |
| Termination standard | At-will (most US states) with disparate treatment screen | Equity Act + ERA 1996 s.98; Band of reasonable responses (Iceland Frozen Foods v Jones) | National labor law (cause required in most EU states) |
| Data protection | SCA (18 U.S.C. §2701); state wiretapping | UK GDPR/DPA 2018; ICO Monitoring at Work | GDPR Arts. 5/6/9; national adaptations (BDSG §26) |
| Whistleblower protection | SOX §806; Dodd-Frank §922; OSHA §11(c) | PIDA 1998; ERA 1996 s.47B | EU WB Directive 2019/1937; national acts |
| Regulatory reporting | EEOC; NLRB; OSHA; DOJ | ET; ACAS; EHRC | National DPA; Eurojust; national labor authorities |

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis covering US/UK/EU workplace
investigation law and best practices. Legal research sources: EEOC Enforcement Guidance
on Harassment in the Workplace (2024); NLRB v. J. Weingarten, Inc., 420 U.S. 251 (1975);
NLRB v. Banner Health System, 362 NLRB 1108 (2015); Faragher v. City of Boca Raton,
524 U.S. 775 (1998); Burlington Industries v. Ellerth, 524 U.S. 742 (1998); Upjohn Co.
v. United States, 449 U.S. 383 (1981); British Home Stores v Burchell [1980] ICR 303;
Iceland Frozen Foods v Jones [1982] IRLR 439; ACAS Code of Practice 1 (2015); EU
Whistleblowing Directive 2019/1937; GDPR; German BetrVG; Legalcode agent-team research
(structural analysis + multi-jurisdiction legal research pipeline). Complements:
`legalcode-investigation-plan-builder` (pre-investigation planning),
`legalcode-internal-investigation` (corporate fraud/regulatory matters),
`legalcode-whistleblower-program-builder` (channel infrastructure).

All legal authorities marked [VERIFY] should be confirmed against current sources before
use in live matters.
```
