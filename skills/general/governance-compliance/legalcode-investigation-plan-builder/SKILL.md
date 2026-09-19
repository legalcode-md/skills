---
name: legalcode-investigation-plan-builder
description: Build structured investigation plans for workplace complaints and compliance matters — from
  intake triage through investigation design, investigator assignment, interview guide generation, timeline
  construction, and regulatory deadline mapping. Use when a complaint has been received (harassment, discrimination,
  retaliation, hostile work environment, wage and hour violation, OSHA safety complaint, code-of-conduct
  violation, whistleblower allegation, workplace misconduct) and a structured investigation framework
  is needed before or alongside formal investigation execution.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Build structured investigation plans for workplace complaints and compliance matters — from intake triage through investigation design, investigator assignment, interview guide generation, timeline construction, and regulatory deadline mapping. Use when a complaint has been received (harassment, discrimination, retaliation, hostile work environment, wage and hour violation, OSHA safety complaint, code-of-conduct violation, whistleblower allegation, workplace misconduct) and a structured investigation framework is needed before or alongside formal investigation execution. Also use when an HR or compliance officer asks "how do we investigate this complaint," "who should investigate," "what questions should we ask," or "what documents do we need." Produces: investigation complexity tier (PRELIMINARY / STANDARD / COMPLEX / CRISIS); scoped investigation plan with milestone timeline; investigator assignment and conflict-of-interest analysis; tailored interview guides for complainant, respondent, and corroborating witnesses; document and evidence collection checklists; interim protective measures recommendations; complainant and respondent communication templates; regulatory deadline maps (EEOC, OSHA, NLRB, EU Whistleblowing Directive 2019/1937, UK ACAS, AU Fair Work Commission); and Glass Box audit trail. Jurisdiction-agnostic core with US/UK/AU [JURISDICTION-SPECIFIC] markers. Complements legalcode-internal-investigation for full-lifecycle execution.


# Legalcode Investigation Plan Builder

> **Disclaimer**: This skill provides a framework for AI-assisted workplace
> investigation planning. It does not constitute legal advice and does not
> create an attorney-client relationship. All outputs must be reviewed by
> qualified employment counsel — and, for regulated entities, by appropriately
> licensed professionals — before being used in an actual investigation or
> disciplinary proceeding. Employment law is highly jurisdiction-specific and
> fact-specific; AI cannot verify current EEOC guidance, NLRB General Counsel
> memos, or local employment statutes. Investigation plans must be reviewed by
> qualified employment counsel before use. Privilege analysis is especially
> sensitive: conducting an investigation without proper privilege counsel
> guidance can waive attorney-client privilege. All statutory, regulatory, and
> case law references cited carry hallucination risk — verify against
> authoritative sources (EEOC.gov, ACAS.org.uk, FairWork.gov.au, court
> records) before relying on them in live matters.

---

## Purpose and Scope

This skill builds structured investigation plans for workplace complaints and
compliance matters. It operates as a **pre-investigation planning tool** —
designing the investigation architecture before execution begins. It is the
blueprint stage; `legalcode-internal-investigation` is the execution stage.

**Covers:**

- Complaint intake triage and investigation complexity tier classification
  (PRELIMINARY / STANDARD / COMPLEX / CRISIS)
- Investigator assignment with conflict-of-interest screening and independence
  analysis
- Investigation scope charter (allegation-specific mandate, in/out scope,
  authorization basis)
- Regulatory deadline mapping (EEOC, OSHA, NLRB, EU Whistleblowing Directive,
  UK ACAS, AU Fair Work Commission)
- Interim protective measures assessment and proportionality analysis
- Witness identification and interview sequencing (with rationale)
- Ready-to-use interview guides for complainant, respondent, corroborating
  witnesses, and management/process witnesses
- Document and evidence collection checklists by complaint type
- Complaint type deep analysis (harassment, discrimination, retaliation,
  wage-hour, safety, code-of-conduct, whistleblower)
- Communication protocols for complainant, respondent, and workforce
- Investigation timeline with milestone tracking
- Handoff package to `legalcode-internal-investigation` for execution

**Does not:**

- Draft the final investigation findings report (that is
  `legalcode-internal-investigation`)
- Classify findings as SUBSTANTIATED / UNSUBSTANTIATED / INCONCLUSIVE (that
  is `legalcode-internal-investigation` — which handles findings classification
  after interviews are complete)
- Cover corporate financial crime, FCPA, antitrust, or securities fraud
  investigations (refer to `legalcode-internal-investigation`)
- Manage parallel government criminal investigations (refer to
  `legalcode-internal-investigation`)
- Draft voluntary self-disclosure letters (refer to
  `legalcode-internal-investigation`)
- Provide legal advice or replace qualified employment counsel

**Related skills:**

- `legalcode-internal-investigation` — execution complement: legal hold,
  document collection, interview execution, findings, remediation
- `legalcode-wage-hour-compliance-audit` — for wage-and-hour complaint type
  background analysis
- `legalcode-employee-handbook-review` — for policy gap identification after
  investigation findings
- `legalcode-termination-risk-assessment` — for assessing dismissal risk after
  substantiated findings
- `legalcode-severance-agreement-review` — if resolution involves separation

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic, with [JURISDICTION-SPECIFIC] markers for
US, UK, and AU requirements. The employment jurisdiction(s) of the parties
determine which legal framework applies.

**United States (US):**

- Title VII of the Civil Rights Act of 1964, 42 U.S.C. § 2000e et seq.
  (harassment, discrimination, retaliation)
- ADA, 42 U.S.C. § 12101; ADEA, 29 U.S.C. § 623; FMLA, 29 U.S.C. § 2601;
  NLRA, 29 U.S.C. § 151; FLSA, 29 U.S.C. § 201; OSHA, 29 U.S.C. § 651
- SOX § 806 (18 U.S.C. § 1514A) and Dodd-Frank § 922 (whistleblower)
- _Faragher v. City of Boca Raton_, 524 U.S. 775 (1998); _Burlington
  Industries v. Ellerth_, 524 U.S. 742 (1998) — employer liability and
  affirmative defense framework
- _Upjohn Co. v. United States_, 449 U.S. 383 (1981) — attorney-client
  privilege scope
- FRCP Rule 37(e) — ESI spoliation sanctions
- EEOC guidance documents — **[CHECK CURRENCY: portions of the April 29, 2024
  Harassment Enforcement Guidance were vacated by a federal court on May 15,
  2025; verify current standing before relying on specific provisions]**

**United Kingdom (UK):**

- Employment Rights Act 1996 (ERA 1996) — unfair dismissal framework (s.98)
- Equality Act 2010 — nine protected characteristics; vicarious liability
  (s.109); reasonable steps defence (s.109(4))
- Worker Protection (Amendment of Equality Act 2010) Act 2023 — positive
  duty to prevent sexual harassment (in force October 26, 2024)
- Employment Relations Act 1999, s.10 — right to be accompanied
- Public Interest Disclosure Act 1998 (PIDA) — whistleblower protection
- ACAS Code of Practice on Disciplinary and Grievance Procedures (statutory
  — non-compliance allows Tribunal to adjust awards up to 25%)
- _British Home Stores Ltd v. Burchell_ [1978] IRLR 379 [VERIFY current
  authority] — genuine belief, reasonable grounds, reasonable investigation
- _Three Rivers District Council v. Bank of England (No. 5)_ [2003] EWCA Civ
  474 — legal advice privilege scope (narrower than US)
- UK GDPR / Data Protection Act 2018 — employee data handling in investigations

**Australia (AU):**

- Fair Work Act 2009 (Cth) — s.387 unfair dismissal criteria; ss.340-345
  general protections / adverse action; anti-retaliation reverse onus
- Sex Discrimination Act 1984; Racial Discrimination Act 1975; Disability
  Discrimination Act 1992 (Cth)
- Work Health and Safety Act 2011 (Cth) and state equivalents — psychological
  safety obligations [VERIFY current state/territory WHS regulations]
- Evidence Act 1995 (Cth), ss.118-119 — dominant purpose test for LPP
- _Esso Australia Resources Ltd v. Commissioner of Taxation_ (1999) 201 CLR 49
  (HCA) — dominant purpose test
- _Crafti v. Cohealth Limited_ [2025] FWC 3285 — external investigation
  reports do not automatically attract privilege; privilege waived by conduct
- Fair Work Commission procedural fairness requirements — notice of specific
  allegations in writing before response required

**Jurisdiction-agnostic principles (all three systems):**

- Duty to investigate once a complaint is received (inaction is itself a risk)
- Proportionality — investigation must be commensurate with complaint seriousness
- Procedural fairness (_audi alteram partem_) — both parties must be heard
- Anti-retaliation — protected activity from the moment a complaint is received
- Documentation standards — contemporaneous, specific, evidence-cited records

[JURISDICTION-SPECIFIC] When adapting to additional jurisdictions:

- EU: GDPR Art. 88 employment-context derogations; EU Whistleblowing Directive
  2019/1937; works council consultation requirements (Germany: BetrVG §§ 87,
  94-95; France: Code du travail Art. L.2312-8; Netherlands: Works Councils
  Act)
- Canada: Provincial human rights codes; OHS legislation; _Doré v. Barreau du
  Québec_ [2012] SCC 12 procedural fairness
- India: POSH Act 2013 (mandatory ICC-led investigations for sexual harassment)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather
than assuming complaint facts, jurisdiction, or organizational context, the
workflow pauses and asks when:

- The answer would change the investigation design (tier, investigator, scope)
- Multiple valid approaches exist and the user's preference or constraints
  govern the choice
- A regulatory deadline or privilege decision must be made before proceeding
- Organizational context (union status, executive involvement) changes the
  required plan structure

Use the **⟁ CLARIFY** pattern (structured options with **Why this matters**
explanations) at each marked point. If the user has already provided the
information, skip the question and proceed. For batch/non-interactive runs,
state all assumptions explicitly and flag open items in the Glass Box audit
trail.

---

## Workflow

### Step 1: Accept the Complaint Input

Accept the complaint in any format: written complaint, verbal description
transcribed by HR, hotline report summary, anonymous tip, email forwarded to
HR, or regulatory agency charge (EEOC charge, OSHA complaint, NLRB charge,
ET claim). If input is sparse, prompt for the minimum four elements:
(1) who complained; (2) what they alleged; (3) against whom; and (4) when.

**Output:** Raw complaint → structured Intake Record (complainant identity
or anonymity status, allegation summary, respondent identity, date(s) of
alleged conduct, and complaint channel).

**⟁ CLARIFY:** If the complaint is entirely anonymous and neither the
complainant nor respondent can be identified from available context, ask:
"Should I design a modified investigation plan that accounts for anonymity
limitations, or should I proceed with the standard framework assuming limited
identification?"

---

### Step 2: Complaint Intake Triage

Classify the complaint across three axes before designing the plan:

**Axis 1 — Subject matter type:** Identify the primary complaint category
from the Complaint Type Taxonomy below. If the complaint spans multiple types,
identify the primary type and note secondary types.

**Axis 2 — Urgency signal:** Assess whether any of the following urgency
factors are present:

- Ongoing physical safety risk (threat of or actual violence)
- Active retaliation occurring or credibly threatened
- Regulatory filing already made (EEOC charge received, OSHA inspection
  scheduled, NLRB charge filed, ET claim issued)
- Mandatory reporting obligation with an imminent deadline
- Executive-level respondent with public company disclosure implications
- Evidence destruction risk (employee departing, system access to be lost)

**Axis 3 — Preliminary plausibility signal:** Assess whether the allegation is:

- **Specific** (named parties, approximate dates, described conduct, possible
  witnesses) — proceed with standard plan design
- **Vague or anonymous** (no specific conduct described, no identifiable
  parties) — note limitations; may require preliminary fact-gathering before
  plan can be fully scoped

**Output:** Intake Classification Card with complaint type, urgency flags, and
plausibility assessment.

**⟁ CLARIFY:** If the complaint type is ambiguous (e.g., harassment allegation
that also contains a retaliation component following a prior complaint), ask:
"The complaint contains both [type A] and [type B] elements. Which should
govern the primary investigation design? I can design parallel tracks if
needed."

---

### Step 3: Gather Investigation Context

Gather all information needed to design the investigation. This is the primary
interactive clarification step.

**⟁ CLARIFY (structured question block):** For each item not already provided,
ask before proceeding to Step 4:

1. **Complainant status** — Current employee / former employee / contractor /
   vendor / intern / other.
   _Why this matters:_ Former employees may have limited cooperation; third
   parties may lack standing under some internal processes; status affects
   which legal frameworks apply.

2. **Respondent status and seniority** — Peer / direct supervisor / skip-level
   / VP or above / third party / executive officer.
   _Why this matters:_ Executive respondents trigger COMPLEX tier; external
   investigators may be legally or politically required; board notification
   may be needed.

3. **Complaint channel** — Internal (HR, manager, ethics hotline) / external
   regulatory (EEOC charge, OSHA complaint, NLRB charge, AU FWC application)
   / attorney demand letter / media inquiry.
   _Why this matters:_ External regulatory filing creates hard deadlines and
   changes investigation priority and scope.

4. **Prior complaints** — Has this respondent been the subject of prior
   complaints? Formally investigated? Informally resolved? Has this
   complainant filed prior complaints?
   _Why this matters:_ Prior complaints about the respondent are pattern
   evidence. Prior complaints by the complainant are relevant to motive.

5. **Union / works council / CBA coverage** — Is the complainant or respondent
   covered by a collective bargaining agreement, union, or works council?
   _Why this matters:_ CBA just-cause standards govern discipline. Union reps
   may have attendance rights (Weingarten rights, US; ERA 1999 s.10, UK).
   Works council consultation may be required before disciplinary action (DE,
   FR, NL).

6. **Witness availability** — Are corroborating witnesses known? Are any likely
   to be uncooperative, anonymous, or outside the organization?
   _Why this matters:_ Uncooperative or unavailable witnesses may require
   written questionnaires, voluntary outreach, or modified sequencing.

7. **Jurisdiction(s)** — Where are the complainant and respondent employed
   and located? Is this cross-border?
   _Why this matters:_ Cross-border matters require multi-jurisdiction legal
   analysis; EU GDPR Art. 88 may constrain evidence transfers.

8. **Counsel status** — Has the complainant retained outside counsel? Has the
   respondent? Is in-house employment counsel engaged?
   _Why this matters:_ Retained counsel changes communication protocols;
   privilege framework and Upjohn warning applicability depend on whether
   investigation is attorney-led.

9. **Ongoing harm concern** — Is there a credible risk of ongoing harm,
   retaliation, witness interference, or continued misconduct during the
   investigation period?
   _Why this matters:_ Determines whether interim protective measures are
   required immediately (Step 11).

10. **External deadline** — Is there an externally imposed deadline (EEOC
    response, OSHA inspection, AU FWC conciliation)? If yes, what is the
    filing date and charge/application number?
    _Why this matters:_ Investigation timeline must be built backward from
    the external deadline; missing regulatory deadlines carries independent
    legal consequences.

---

### Step 4: Classify Investigation Complexity Tier

Based on Steps 2 and 3, classify the investigation using the four-tier
framework (see **Investigation Complexity Tiers** below). State explicitly
which criteria triggered the tier.

**Output:** Complexity tier classification with rationale sentence explaining
which criteria were determinative.

**⟁ CLARIFY:** If the complaint sits on a tier boundary, ask: "Based on
[specific factor], this may warrant [higher tier] treatment, which would
require [specific resource/process implication]. Should I design at
[STANDARD / COMPLEX] tier?"

---

### Step 5: Investigator Assignment and Conflict Screening

Recommend the investigator structure appropriate to the tier. Screen
explicitly for conflicts using the Dual-Hat Risk framework below.

**Independence screen — ask these questions:**

- [ ] Does the proposed investigator have a prior supervisory relationship with
      the respondent or complainant?
- [ ] Did the proposed investigator have any prior involvement in the events
      at issue?
- [ ] Is the proposed investigator a potential witness (e.g., received a prior
      complaint about the respondent)?
- [ ] Is the proposed investigator in the reporting chain for either party?
- [ ] Has the proposed investigator expressed a prior opinion about the
      complainant, respondent, or allegation?

If any box is checked, a conflict exists and the investigator must be recused.

**Tier-specific investigator recommendations:**

- **PRELIMINARY:** HR generalist or trained HR manager
- **STANDARD:** Trained HR professional or compliance officer; employment
  counsel engagement optional but recommended if privilege protection is wanted
- **COMPLEX:** Employment counsel leadership recommended; outside counsel if
  respondent is VP or above, or if CBA/union is involved
- **CRISIS:** Outside employment counsel required; GC direct involvement;
  board notification assessment

**Output:** Investigator recommendation with conflict-of-interest screen result
and a recusal flag where applicable.

**⟁ CLARIFY:** If a conflict is identified or if the respondent is an
executive, ask: "Should I recommend outside employment counsel lead this
investigation to protect independence and establish privilege?"

---

### Step 6: Draft the Investigation Scope and Charter

Draft the investigation scope statement — the planning-stage mandate.

**The scope charter must specify:**

1. Each allegation as a discrete factual question (not conclusions)
2. The decision the investigator is asked to make
3. Time period covered (not open-ended)
4. Named parties under investigation
5. What is explicitly **out of scope**
6. Applicable policies and burden of proof standard
7. Authorization basis (HR Director / GC / Board resolution)
8. Confidentiality framework
9. Privilege election (attorney-led or HR-led — **this decision is
   irreversible and must be made before the first interview**)

**Burden of proof standards:**

- **US:** Preponderance of the evidence (more likely than not)
- **UK [JURISDICTION-SPECIFIC]:** Reasonable belief on reasonable grounds
  (_British Home Stores v. Burchell_ [1978] IRLR 379 [VERIFY]) — the employer
  need not prove the conduct occurred but must have a genuine belief based on
  reasonable investigation
- **AU [JURISDICTION-SPECIFIC]:** Balance of probabilities, but with
  procedural fairness requirements; specific allegations must be put to the
  respondent in writing before any findings are made

**Output:** Investigation Charter draft (template-ready for review by
employment counsel).

**⟁ CLARIFY:** If new information surfaced during intake suggests scope broader
than the original complaint, ask: "The complaint describes [allegation X], but
available context suggests [potential pattern Y]. Should the scope be limited
to the specific incident, or expanded to cover [the broader pattern]? A
broader scope requires more resources but may produce more durable findings
and better address systemic risk."

---

### Step 7: Map Regulatory Deadlines and Immediate Legal Obligations

Based on complaint type and jurisdiction, identify all regulatory deadlines
and immediate legal obligations. These constraints are non-negotiable and must
override the investigation timeline if necessary.

**Key US deadlines [VERIFY before relying on — regulatory timelines change]:**

| Trigger                                            | Obligation                       | Deadline                                                            |
| -------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------- |
| EEOC charge received                               | Position statement and records   | Per EEOC charge letter (typically 20-40 days) [VERIFY]              |
| OSHA severe injury (hospitalization or amputation) | Reporting to OSHA                | 24 hours (hospitalization); 8 hours (fatality)                      |
| OSHA complaint filed                               | Response to OSHA                 | Per OSHA notification letter                                        |
| NLRB charge filed                                  | Response to NLRB Regional Office | Per NLRB charge (typically 7-14 days for initial response) [VERIFY] |
| Data breach discovered during investigation        | State breach notification laws   | Varies by state (24 hours to 30+ days depending on state)           |
| SAR obligation (if financial crime element)        | FinCEN SAR filing                | 30 days from detection (60 with extension)                          |
| Federal contractor complaint (FAR § 52.209-5)      | Self-disclosure                  | "Timely" (interpreted ~30 days of credible evidence) [VERIFY]       |

**[JURISDICTION-SPECIFIC UK] Key UK deadlines:**

- ET claim issued: acknowledge service and file ET3 within 28 days
- ACAS Early Conciliation certificate: precondition to ET claim; one month
  period before ET claim can be filed [VERIFY]
- ICO data breach reporting (if investigation reveals personal data breach):
  72 hours

**[JURISDICTION-SPECIFIC AU] Key AU deadlines:**

- AU Human Rights Commission conciliation: respond within 60 days of
  notification [VERIFY against current AHRC practice]
- Fair Work Commission unfair dismissal: respond within 7 days of notification
- Safe Work Australia WHS reportable incident: notify regulator immediately
  (within 24 hours for serious incident) [VERIFY state/territory requirements]
- OAIC NDB notification: 72 hours if investigation reveals eligible data
  breach

**Output:** Regulatory Deadline Map with named obligation, applicable
framework, deadline, and action owner. Flag any deadline that falls before
the investigation can reasonably conclude.

**⟁ CLARIFY:** If the complaint was triggered by an external regulatory
filing, ask for the filing date and charge/application number so deadline
calculations are accurate.

---

### Step 8: Design Witness List and Interview Sequence

Produce a prioritized witness list with sequencing rationale.

**Standard witness sequencing principle:** Peripheral and corroborating
witnesses first → complainant → management/process witnesses → respondent
last → return to complainant only if respondent raises new material facts.

**Rationale for this sequence:**

- Corroborating witnesses before complainant: establishes independent
  evidentiary record; prevents complainant's account from anchoring all
  subsequent interviews
- Complainant before respondent: complainant's full account informs the
  specific questions put to the respondent
- Respondent last: all facts gathered before respondent has opportunity to
  respond; respondent can be shown specific evidence; prevents witness coaching
- Return to complainant only if necessary: complainant must have an opportunity
  to address any materially new evidence the respondent introduces

**Witness categories and sequencing priority:**

| Priority | Category                          | Purpose                                                       | Notes                                                       |
| -------- | --------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------- |
| 1        | Corroborating / bystander witness | Establish independent observations                            | Interview separately; do not disclose complainant's account |
| 2        | Complainant                       | Full account; document identification; witness identification | Open-ended; narrative-first approach                        |
| 3        | Management / process witnesses    | Prior knowledge; documentation; supervisory response          | Ask about HR file contents; prior complaints                |
| 4        | Respondent                        | Response; context; exculpatory evidence                       | Put specific allegations in writing before interview        |
| 5        | Return interview (conditional)    | Respond to material new facts from respondent                 | Only if respondent introduces new facts or alibi witnesses  |

**Special considerations:**

- Former employees: voluntary participation only; written questionnaire as
  fallback
- Represented employees (union, personal counsel): consult employment counsel
  before scheduling
- Employees outside the jurisdiction: multi-jurisdiction legal analysis before
  interview
- Potential co-complainants: interview separately to prevent account
  contamination

**Output:** Witness Matrix with priority, category, role, estimated duration,
sequencing rationale, and special access considerations.

**⟁ CLARIFY:** If a key witness is a former employee, out-of-jurisdiction, or
represented by counsel, ask: "Witness [X] is [status]. Should I flag this as a
witness-access risk and recommend [voluntary outreach / written questionnaire /
outside counsel engagement]?"

---

### Step 9: Generate Interview Guides

Generate tailored interview guides for each witness category required by the
tier. Each guide includes: purpose statement, opening script, question set
organized by phase, documents to show, and a post-interview notes template.

**See Interview Guide Templates below for full content.**

**Tier-to-guide matrix:**

| Tier        | Guides Produced                                             |
| ----------- | ----------------------------------------------------------- |
| PRELIMINARY | Manager conversation guide (not a full investigation guide) |
| STANDARD    | 8A (Complainant), 8B (Respondent), 8C (Corroborating)       |
| COMPLEX     | 8A, 8B, 8C, 8D (Management/Process)                         |
| CRISIS      | 8A, 8B, 8C, 8D + special privilege warnings                 |

**Output:** Interview guides, ready to use, with verbatim opening scripts.

**⟁ CLARIFY:** If the investigation is COMPLEX or CRISIS tier and involves
a union-represented respondent, ask: "Should I include specific Weingarten
rights notice language [US] / ERA 1999 s.10 companion rights script [UK] in
the respondent's opening script? This is recommended for represented
employees."

---

### Step 10: Generate Document and Evidence Collection Checklist

Produce a document collection checklist tailored to the primary complaint type.
Map each document category to the allegation elements it can prove or disprove.

**See Document Checklist Templates below by complaint type.**

**Output:** Document Checklist with allegation-element mapping, priority flags,
named custodians, and collection method.

**⟁ CLARIFY:** If the investigation involves electronic communications on
personal devices or third-party platforms (WhatsApp, personal email), ask:
"Does your organization's investigation or BYOD policy permit access to
personal device data? If yes, I'll include preservation instructions. If no,
I'll flag this as an evidence gap."

---

### Step 11: Recommend Interim Protective Measures

Assess whether interim measures are needed before the investigation concludes.
Frame recommendations using the proportionality principle: the least
restrictive effective measure is the appropriate measure.

**⟁ CLARIFY:** If both the complainant and respondent are in the same physical
workspace with no alternative assignment possible, ask: "The parties share
[workspace/shift/location]. Feasible interim options are: [A: administrative
leave for respondent / B: temporary reporting-line change / C: remote work
arrangement]. Which approach fits your operational constraints?"

**See Interim Protective Measures Framework below for the full decision matrix.**

**Output:** Interim Measures Recommendation with proportionality analysis and
implementation steps.

---

### Step 12: Quality Verification and Plan Assembly

Run the Quality Assurance Framework (see below). Assemble the complete
investigation plan using the Output Format Template. Append the Glass Box
audit trail. Flag all open items requiring human decision before the plan
can be executed.

**Pre-delivery quality checklist:**

- [ ] Complaint type identified and deep analysis applied
- [ ] Tier classification made with explicit rationale
- [ ] Investigator recommendation includes conflict screen result
- [ ] Regulatory deadline map covers all applicable obligations
- [ ] Witness sequence follows professional standard with rationale stated
- [ ] Interview guides include verbatim opening scripts
- [ ] Document checklist is complaint-type specific (not generic)
- [ ] Interim measures recommendation addresses proportionality
- [ ] All [JURISDICTION-SPECIFIC] flags are accurately placed
- [ ] No plan language presupposes investigation outcomes
- [ ] Privilege election noted (attorney-led vs. HR-led)
- [ ] Handoff to `legalcode-internal-investigation` noted
- [ ] Glass Box audit trail complete

**Output:** Complete investigation plan document, Glass Box audit trail, and
an Open Items list of unresolved decisions requiring human input.

---

## Complaint Type Taxonomy and Deep Analysis

### Type 1: Harassment and Hostile Work Environment

**Definition:** Unwelcome conduct based on a protected characteristic that is
either severe or pervasive enough to create a hostile work environment, or
that results in a tangible employment action.

**Protected bases [US — 42 U.S.C. § 2000e et seq.]:** Race, color, religion,
sex, national origin, age (ADEA), disability (ADA), pregnancy, genetic
information (GINA).

**[JURISDICTION-SPECIFIC UK]:** Nine protected characteristics under Equality
Act 2010: age, disability, gender reassignment, marriage/civil partnership,
pregnancy/maternity, race, religion or belief, sex, sexual orientation.

**[JURISDICTION-SPECIFIC AU]:** Protected attributes under Sex Discrimination
Act 1984, Racial Discrimination Act 1975, Disability Discrimination Act 1992,
and state/territory anti-discrimination legislation (which varies).

**Key allegation elements to establish:**

1. Complainant is a member of a protected class (or perceived to be)
2. The conduct was unwelcome
3. The conduct was based on the protected characteristic (not just unpleasant
   workplace conduct)
4. The conduct was severe or pervasive (frequency, severity, whether
   physically threatening, whether it interfered with work performance)
5. The employer knew or should have known of the conduct (constructive
   knowledge)
6. The employer failed to take prompt corrective action

**Most relevant documents:**

- HR file for both complainant and respondent (performance reviews, prior
  complaints, prior discipline)
- Email, messaging platform (Slack, Teams), and text communications between
  parties in the relevant period
- Complainant's contemporaneous notes or reports to third parties
- Prior complaints about the respondent (formal and informal)
- Anti-harassment policy and training records (completion dates)
- CCTV or access badge records (for location verification)

**Interview focus areas:**

- Complainant: Exact words and conduct; frequency and dates; impact on work
  and wellbeing; witnesses present; prior reports
- Respondent: Denial or explanation; intent claim; context; alibi witnesses
  and documents; prior relationship with complainant
- Witnesses: Direct observations; conduct patterns; prior complaints heard;
  complainant's reports to them at the time

**Applicable regulatory framework [US]:** EEOC _Enforcement Guidance on
Harassment_ (April 29, 2024) [**CHECK CURRENCY**: portions vacated May 2025
— verify which specific provisions remain in force before relying on them];
_Faragher-Ellerth_ affirmative defense framework.

**Common pitfalls specific to harassment investigations:**

- Failing to document the "welcome/unwelcome" determination separately from
  the "whether it occurred" finding — these are distinct inquiries
- Over-relying on the complainant's delay in reporting as evidence of welcome
  conduct (EEOC guidance explicitly warns against this inference)
- Failing to investigate pattern evidence (other complainants who haven't
  formally complained)

---

### Type 2: Discrimination in Employment Decisions

**Definition:** Adverse employment actions (hiring, firing, promotion,
demotion, pay, job assignments, leave approvals) based on a protected
characteristic rather than legitimate, nondiscriminatory reasons.

**Key allegation elements:**

1. Complainant is a member of a protected class
2. Complainant suffered an adverse employment action
3. Similarly situated comparators outside the protected class were treated more
   favorably
4. Causal nexus between protected characteristic and adverse action

**Most relevant documents:**

- Decision-maker's communications before and after the adverse action
- Performance records for the complainant and comparator employees
- HR approval and documentation chain for the decision
- Pay records and compensation decisions (especially for pay equity claims)
- Promotion and succession records
- Prior EEOC or HR complaints about the decision-maker

**Interview focus areas:**

- Decision-maker: documented rationale; consideration given to comparators;
  timeline of decision
- HR approvers: review process; any concerns raised
- Comparators (carefully): treatment in similar circumstances; awareness of
  complainant's protected status

---

### Type 3: Retaliation

**Definition:** An adverse employment action against an employee for engaging
in protected activity (filing a complaint, participating in an investigation,
reporting to a regulator, opposing discriminatory practices).

**Protected activity trigger:** The protected activity may be the current
complaint — or a prior complaint, EEOC charge, or regulator contact that the
investigation must identify.

**Key allegation elements:**

1. Employee engaged in protected activity
2. Employer was aware of the protected activity
3. Adverse employment action followed
4. Causal nexus (timing proximity, pattern of conduct, decision-maker
   awareness)

**Temporal proximity doctrine [VERIFY case law currency]:** Courts have found
that adverse actions taken within days to weeks of a protected activity can
establish a prima facie case of retaliation; some circuits set a 3-month
outer boundary. Identify the date of the protected activity and map all
subsequent employment decisions.

**Most relevant documents:**

- Timeline of protected activity and subsequent employment decisions
- Decision-maker's communications (especially those referencing the complaint)
- Performance records before and after protected activity
- Comparator employees' treatment in similar circumstances

---

### Type 4: Wage and Hour Violations

**Definition:** Allegations of off-the-clock work, minimum wage violations,
overtime violations, tip theft, misclassification, or pay equity violations.

**Key allegation elements:**

1. Employer-employee (or misclassification) relationship established
2. Hours worked (documented or estimated)
3. Compensation paid vs. compensation required by law
4. Gap between required and actual pay

**Most relevant documents:**

- Time records (paper and electronic) — especially where discrepancies are
  alleged
- Pay stubs and payroll records
- Manager communications about time recording, off-the-clock work
- Classification records (employee vs. contractor)
- Tip pool records and distribution
- FLSA exemption basis documentation (if exempt status is challenged)

**[JURISDICTION-SPECIFIC AU]:** Fair Work Ombudsman has broad investigation
and enforcement powers; employers have record-keeping obligations under Fair
Work Regulations 2009, regs. 3.31-3.46 [VERIFY current regulations].
Underpayment remediation obligations (three-year statute of limitations under
FWA s.545 [VERIFY]) are significant.

---

### Type 5: Workplace Safety Complaints

**Definition:** Allegations of hazardous workplace conditions, unsafe
practices, failure to provide required safety equipment, or retaliation for
raising safety concerns.

**Key allegation elements:**

1. Specific hazard or unsafe condition identified
2. Employer knew or should have known of the hazard
3. Employer failed to correct the hazard
4. Harm or risk of harm resulted

**Immediate action before plan is executed:** If any physical safety risk is
ongoing, implement immediate controls before proceeding with investigation
design. The investigation plan is secondary to immediate harm prevention.

**Most relevant documents:**

- Incident reports and OSHA logs (OSHA 300, 300A, 301 for US employers [VERIFY])
- Safety inspections and prior citations
- Equipment maintenance records
- Training records for relevant safety procedures
- Prior reports of the same or similar hazard

**US mandatory reporting triggers [VERIFY deadlines and thresholds]:**

- Fatality: report to OSHA within 8 hours
- Amputation, loss of eye, in-patient hospitalization: report within 24 hours
- OSHA 300 log recording: within 7 days of incident

---

### Type 6: Code of Conduct and Policy Violations

**Definition:** Alleged violations of organizational policy that do not
necessarily involve legal violations — conflicts of interest, misuse of
company resources, expense fraud, confidentiality breaches, outside
employment conflicts.

**Note:** If the alleged conduct crosses into potential criminal territory
(theft above a threshold, financial fraud), escalate to COMPLEX or CRISIS
tier and involve legal counsel; the investigation may intersect with
criminal or regulatory proceedings.

**Key allegation elements:**

1. Applicable policy existed and was communicated to the respondent
2. The respondent was aware of (or should have been aware of) the policy
3. The specific conduct alleged occurred
4. The conduct violated the applicable policy

**Most relevant documents:**

- The policy alleged to have been violated (version in effect at time of
  alleged conduct)
- Training records confirming the respondent received the policy
- Evidence of the alleged conduct (expense reports, emails, access logs)
- Prior discipline or counseling related to the same type of conduct

---

### Type 7: Whistleblower / Protected Disclosure Allegations

**Definition:** Allegations that an employee suffered adverse action for
disclosing illegal activity, regulatory violations, or conduct posing a risk
to public health or safety to a supervisor, HR, compliance, or external
regulator or law enforcement.

**Key allegation elements:**

1. Employee made or was about to make a protected disclosure
2. The disclosure was of a covered subject matter under applicable law
3. Employer took adverse action against the employee
4. Causal nexus between disclosure and adverse action

**Anti-retaliation obligations activate immediately:** The moment a complaint
is identified as potentially involving a whistleblower allegation, flag the
complainant's identity to HR for "at-risk" monitoring. Any adverse employment
action from this point carries heightened legal risk.

**Applicable frameworks [VERIFY current status of each]:**

- **US:** SOX § 806 (18 U.S.C. § 1514A); Dodd-Frank § 922 (15 U.S.C. § 78u-6);
  OSHA whistleblower program statutes (23 separate statutes); state
  whistleblower protection acts
- **[JURISDICTION-SPECIFIC UK]:** PIDA 1998; ERA 1996 Part IVA; detriment
  and dismissal protections; uncapped compensation
- **[JURISDICTION-SPECIFIC EU]:** EU Whistleblowing Directive 2019/1937 (50+
  employee organizations must have internal reporting channel; 2-year data
  retention; 3-month response obligation; confidentiality of reporter identity
  — member state implementation status varies [VERIFY])
- **[JURISDICTION-SPECIFIC AU]:** Fair Work Act 2009 general protections
  (reverse onus of proof on employer to disprove adverse action); Corporations
  Act 2001 Part 9.4AAA (whistleblower protection for financial disclosures)

---

## Investigation Complexity Tiers

### PRELIMINARY — Informal or Pre-Investigation Track

**Definition:** The complaint does not yet meet the threshold for a formal
investigation, or the appropriate resolution is an informal intervention.

**Criteria (ALL of the following must be true):**

- Single incident, single complainant, single respondent
- No physical harm; no ongoing pattern alleged
- No regulatory filing has been made (no EEOC charge, no OSHA complaint, no
  FWC application)
- Respondent is a peer (not a supervisor or management)
- No protected-class dimension that creates legal exposure if not formally
  investigated
- No prior complaints involving the same respondent

**Plan elements at PRELIMINARY tier:**

- Informal intake record (complaint summary, date received, intake person)
- Manager conversation guide with structured documentation template
- Anti-retaliation instructions to relevant managers
- Monitoring and follow-up schedule
- Escalation triggers: specific conditions that will elevate to STANDARD
  (recurrence, additional complainants, escalation by complainant, regulatory
  filing)

> **Important:** PRELIMINARY is not "no investigation." It is a structured
> informal track with documentation. Undocumented informal resolutions are a
> recognized anti-pattern — they cannot be cited in defense of a later claim.

---

### STANDARD — Routine Formal Investigation

**Definition:** The complaint warrants a formal internal investigation with
documented process, witness interviews, document review, and written findings.

**Criteria (any one of the following triggers STANDARD):**

- Allegation involves a supervisor-subordinate relationship
- Protected-class dimension present (Title VII, Equality Act 2010, AU
  anti-discrimination legislation)
- Two or more complainants reporting the same conduct
- Prior complaint(s) about the respondent that were informally resolved
- Retaliation allegation arising from a prior complaint

**Plan elements at STANDARD tier:**

- Full Investigation Plan (all 11 plan sections)
- Investigator: trained HR professional or compliance officer; employment
  counsel engagement recommended for privilege protection
- Interview guides: 8A (Complainant), 8B (Respondent), 8C (Corroborating)
- Standard document checklist by complaint type
- 30–60 day timeline
- Regulatory deadline map (all applicable)

---

### COMPLEX — High-Stakes or Multi-Dimensional Investigation

**Definition:** The investigation involves senior respondents, multiple
complainants, significant legal exposure, or regulatory involvement requiring
employment counsel leadership.

**Criteria (any one of the following triggers COMPLEX):**

- Respondent is VP-level or above
- Three or more complainants
- Allegation of systemic pattern (not isolated incident)
- Parallel regulatory proceeding active (EEOC charge filed, OSHA inspection
  underway, NLRB charge, FWC application, ET claim issued)
- Allegation involves potential criminal conduct (assault, sexual assault,
  theft, financial fraud below the regulatory disclosure threshold)
- Union grievance filed in connection with the same events
- Media inquiry or public disclosure risk
- Cross-border jurisdiction (parties in different countries)
- Prior unresolved complaints about the same respondent (pattern suggests
  systemic failure)

**Plan elements at COMPLEX tier** (all STANDARD elements plus):

- Employment counsel leadership or co-leadership recommended
- Interview guide 8D (Management/Process Witness) added
- Enhanced document checklist with ESI preservation instruction
- Extended 60–90 day timeline with milestone gates
- Board or audit committee notification assessment
- Communications strategy note for workforce (when and how to address)
- Privilege election explicitly documented and counsel engaged before first
  interview

---

### CRISIS — Emergency or Potentially Criminal Matter

**Definition:** The complaint involves an immediate safety risk, mandatory
reporting obligations, potential criminal conduct, or facts that could
escalate to a government investigation.

**Criteria (any one of the following triggers CRISIS):**

- Physical threat or recent physical harm to any party
- Credible allegation of sexual assault or serious physical assault
- Mandatory reporting obligation triggered (OSHA severe injury; DCFS child
  abuse; SAR if financial crime element)
- Parallel criminal investigation underway or reasonably anticipated
- Executive-level respondent in a public company context (SEC implications,
  proxy disclosure, SOX § 302/906 certification integrity)
- Evidence of tampering with evidence or anticipated document destruction

**Plan elements at CRISIS tier** (all COMPLEX elements plus):

- Outside employment counsel engagement required immediately — not optional
- Immediate interim measures assessment (physical separation, system access
  revocation) before investigation plan is otherwise complete
- Mandatory reporting obligation checklist with specific deadlines
- Board notification protocol (not just "assess")
- External communications holding statement
- 30-day accelerated timeline with daily milestone tracking
- Parallel handoff to `legalcode-internal-investigation` for immediate
  execution of legal hold and evidence preservation

---

## Investigator Independence and Dual-Hat Risk

**Independence requirements (all jurisdictions):**

- The investigator must have no prior supervisory relationship with either party
- The investigator must not be a potential witness to the events
- The investigator must not have expressed a prior opinion about the parties
  or allegation
- The investigator must be sufficiently senior to conduct the investigation
  credibly (ACAS; EEOC)

**Dual-hat risk analysis:**
The most common independence failure in workplace investigations is the
"dual-hat" HR Business Partner: the HR professional who manages the
respondent's team is also assigned to investigate the complaint against the
respondent. This creates:

- An actual or perceived conflict of interest (the HR partner has an
  organizational stake in the respondent's continued performance)
- A potential witness conflict (the HR partner may have prior knowledge)
- A credibility gap in subsequent proceedings

**Separation of functions rule:** Where possible, separate these roles:

1. Intake officer (receives and triages complaint)
2. Investigator (gathers evidence and prepares findings)
3. Decision-maker (makes discipline decision based on findings)
4. Appellate officer (reviews discipline decision if appealed)

None of these roles should be held by the same person in the same matter.

**When to recommend external investigators:**

- Senior management or executive respondents
- The organization is too small for internal neutrality
- HR has a prior relationship with either party
- The allegation is serious (sexual assault, systemic harassment, financial
  misconduct)
- Prior internal investigations have been criticized or overturned

---

## Interview Guide Templates

### 8A: Complainant Interview Guide

**Purpose:** Gather the complainant's full account; establish timeline;
identify documents and witnesses; assess impact; identify comparators.

**Timing:** After any preliminary corroborating witnesses (if known);
before the respondent interview.

**Opening Script:**

> "Thank you for coming in. I want to explain how this process works before
> we begin. [Organization] takes all workplace concerns seriously. The purpose
> of this meeting is to understand your experience and gather information.
> This conversation is confidential within the investigation team — the details
> will not be shared outside the team except as required by the investigation
> or by law. I may need to share some information with [respondent] to give
> them a fair opportunity to respond, and I will let you know if that occurs.
> You can take notes if you wish. If you need to stop at any point, please
> let me know. Do you have any questions before we begin?"

**[JURISDICTION-SPECIFIC UK]:** If disciplinary action against the
complainant is possible as a result of conduct disclosed in this interview,
the right to be accompanied under ERA 1999 s.10 must be offered before
proceeding.

**[JURISDICTION-SPECIFIC US — attorney-led investigation]:** Deliver the
Upjohn warning before proceeding. See Privilege Protection below.

**Phase 1 — Background:**

1. How long have you worked at [Organization] and in what role?
2. Describe your working relationship with [Respondent] — how long, what
   is the nature of your professional contact?

**Phase 2 — Narrative (open-ended; do not interrupt):** 3. Tell me in your own words what happened. Start from the beginning and
take as much time as you need. 4. [Allow full narrative before asking specific follow-up questions.] 5. When did this first happen? Walk me through each incident chronologically.

**Phase 3 — Specific Inquiry:** 6. Were there any witnesses present during [incident]? 7. Do you have documents, messages, emails, or other records related to
what you have described? 8. Did you report this to anyone before today? To whom, when, and what
happened? 9. How has this affected your work, health, or wellbeing? 10. Are you aware of other employees who have had similar experiences?

**Phase 4 — Comparators (if discrimination allegation):** 11. Can you identify specific colleagues in a similar role who you believe
were treated more favorably in [specific decision]? 12. Are you aware of any reason [decision-maker] would treat you differently
from [comparator]?

**Phase 5 — Close:** 13. Is there anything else you want me to know that you have not already
told me? 14. Are there other witnesses I should speak with? 15. What outcome are you hoping for from this process? 16. Confidentiality instruction: "Please keep the content of this interview
confidential to the extent possible. Do not discuss the specifics of what
we have covered with colleagues. If someone asks, it is appropriate to say
you met with HR."

**[US caution on confidentiality instructions]:** Do not instruct employees
"do not discuss this with anyone." Broad confidentiality instructions may
violate NLRA Section 7 rights. The correct framing asks employees to maintain
confidentiality "to the extent possible" without prohibiting discussion with
union representatives or outside counsel.

**Post-Interview Notes Template:**

- Date, time, location, attendees (interviewer, note-taker, support person):
- Summary of account (narrative, not interpretation):
- Documents identified:
- Witnesses named:
- Follow-up items:
- Credibility assessment: [HIGH / MEDIUM / LOW / INCONCLUSIVE]
  - Plausibility: [Assessment with specific observations]
  - Consistency (internal): [Assessment]
  - Corroboration available: [Assessment]
  - Motive to fabricate: [Specific evidence if present; "None identified" if not]
  - Prior inconsistencies: [Yes — describe / No]

---

### 8B: Respondent Interview Guide

**Purpose:** Provide the respondent a full and fair opportunity to respond
to specific allegations; gather their account; identify exculpatory evidence;
assess credibility.

**Timing:** After corroborating witnesses and complainant interview. After
putting specific written allegations to the respondent in advance where
required (AU: procedural fairness — specific allegations must be provided in
writing before the response interview; UK ACAS: employee must know the case
against them).

**[JURISDICTION-SPECIFIC UK]:** Respondent has the right to be accompanied by
a trade union representative or colleague under ERA 1999 s.10 if this
interview could lead to disciplinary action. This right must be offered and
documented before the interview begins.

**[JURISDICTION-SPECIFIC AU]:** Specific allegations must be provided to the
respondent in writing with reasonable time to respond before the interview.
Failure to do so is a procedural fairness failure that can independently
render a subsequent dismissal unfair (FWA s.387(b)-(c)).

**[JURISDICTION-SPECIFIC US — attorney-led investigation]:** Deliver the
Upjohn warning before proceeding.

**Opening Script:**

> "Thank you for meeting with me. I am conducting a confidential internal
> investigation into a workplace matter. I want to be clear about a few
> things. First, this is a fact-gathering process — it is not a disciplinary
> hearing. Second, this conversation is confidential within the investigation
> team. Third, I want to give you a full opportunity to respond to the
> information we will discuss. I have prepared specific questions about
> concerns that have been raised, and I will ask you each one individually.
> [If applicable: you have the right to have a [union representative /
>
> > colleague / personal counsel] present.] Do you have any questions before
> > we begin?"

**Phase 1 — Background:**

1. Describe your role, reporting relationships, and how your work
   intersects with [complainant's team/role].
2. Describe your general professional relationship with [complainant or
   general description if identity not yet disclosed].

**Phase 2 — Specific Allegations (put each allegation specifically):**
For each discrete allegation identified in the scope charter: 3. "I want to ask you about [specific incident / conduct / statement]. What
can you tell me about that?" 4. "On [approximate date], were you [at location / in this meeting]? What
happened?" 5. "Did you [specific alleged conduct]? If so, what did you intend by that?
If not, what is your account?"

**Phase 3 — Response and Context:** 6. Are there witnesses who can speak to your account of these events? 7. Are there documents — emails, calendar entries, messages — that support
what you have told me? 8. Is there any context I should understand about your working relationship
with [complainant] or about the events described?

**Phase 4 — Pattern and Prior:** 9. Have you ever had a prior complaint made against you regarding [this
type of conduct] at this organization or elsewhere? 10. Have you ever received training on [anti-harassment policy / relevant
code of conduct]?

**Phase 5 — Close:** 11. Is there anything you want to add that you have not had the opportunity
to tell me? 12. Are there witnesses or documents you want me to consider that I have
not asked about? 13. Confidentiality instruction (same framing as complainant; same NLRA
caution applies [US]).

---

### 8C: Corroborating / Bystander Witness Guide

**Purpose:** Gather independent observations without leading the witness or
telegraphing the investigation's direction.

**Opening Script:**

> "Thank you for making time to speak with me. I am conducting a
> confidential internal review of a workplace matter. I want to ask you
> some questions about your observations at work. This conversation is
> confidential — please keep the content of our discussion private and do
> not discuss it with colleagues, to the extent possible."

**Question Set:**

1. How long have you worked at [Organization] and in what role?
2. Describe your working relationship with [team/department].
3. Have you observed any interactions between [general description, not
   naming parties initially] in the team that concerned you?
4. [If witness was specifically named:] Were you present at [general context
   of alleged incident]? What did you observe?
5. Have any colleagues spoken to you about concerns with [general conduct
   area] in your team?
6. Do you have any documents or communications relevant to what we have
   discussed?
7. Is there anything else you believe is relevant that I have not asked about?

---

### 8D: Management / Process Witness Guide (COMPLEX and CRISIS tiers)

**Purpose:** Understand organizational context, prior knowledge, and
supervisory response relevant to the allegations.

**Question Set:**

1. Describe your management responsibilities and reporting relationships.
2. Describe your knowledge of [respondent's] performance and conduct — any
   prior concerns?
3. Have you received any prior complaints or informal expressions of concern
   about conduct in your team?
4. What documentation exists in [respondent's] HR file regarding performance
   or conduct?
5. Were you aware of any of the events described in [general terms]? If yes,
   what action did you take?
6. What policies govern [relevant conduct type] in this organization, and
   how are they communicated?
7. Could you describe the approval or escalation process for [relevant HR
   decision — promotion, pay, termination]?

---

## Privilege Protection Framework

### US: Upjohn Warning

The Upjohn warning is required whenever a corporate attorney (in-house or
external) interviews an employee as part of an investigation. It is NOT
appropriate in HR-led (non-attorney) investigations.

**Upjohn Warning — Five Required Elements:**

> "1. I am [name], an attorney. I represent [Company Name]. I do not
> represent you personally.
>
> 2. I am interviewing you as part of an internal investigation into a
>    workplace matter. The information you provide will assist [Company] in
>    obtaining legal advice.
> 3. This conversation is protected by the attorney-client privilege.
>    However, the privilege belongs to [Company], not to you. [Company] controls
>    whether the privilege is waived.
> 4. [Company] may, at its discretion, choose to disclose the contents of
>    this interview to third parties, including government authorities, without
>    your consent.
> 5. Because I represent [Company] and not you, you may wish to consult
>    your own attorney before or after this interview. You are not required to
>    speak with me, although [Company] expects its employees to cooperate with
>    internal investigations."

**Deliver orally AND in writing. Document delivery and acknowledgment in
the interview memorandum.**

**Privilege election — make this decision before the first interview:**

- Attorney-led (in-house or outside counsel): Upjohn warning appropriate;
  privilege may attach if properly established
- HR-led (non-attorney): No Upjohn warning; no attorney-client privilege;
  work product doctrine may apply if litigation was reasonably anticipated

**Dual-hat risk:** If the same attorney leads the investigation and is also
expected to provide legal advice or appear as counsel in litigation, privilege
may be waived if the attorney becomes a witness. Separate "investigation
counsel" from "litigation counsel" roles.

### [JURISDICTION-SPECIFIC UK]: Three Rivers Limitation

Under _Three Rivers (No. 5)_ [2003], legal advice privilege extends only to
communications with the client group authorized to seek and receive legal
advice — not to all employee interview notes even if conducted by lawyers.
Litigation privilege requires: (a) litigation reasonably contemplated or
pending; AND (b) dominant purpose of interview was to prepare for litigation.

**Practical approach:** Engage investigation law firm separate from ongoing
legal advisers. Document litigation anticipation rationale early. Restrict
dissemination of interview notes. Obtain privileged legal advice framing the
dominant purpose clearly.

### [JURISDICTION-SPECIFIC AU]: Dominant Purpose Test

Under _Esso Australia_ (1999) and _Crafti v. Cohealth_ [2025] FWC 3285,
investigation reports do not automatically attract privilege. The dominant
purpose must be legal advice or litigation preparation — not compliance
investigation or HR function.

**Practical approach:** Engagement letter with external investigator must
explicitly establish dominant purpose. Frame communications from investigating
law firm as legal advice. Maintain strict access controls on investigation
documents.

---

## Interim Protective Measures Framework

**Core principle:** The least restrictive effective measure is the appropriate
measure. Measures protect parties and investigation integrity — they are not
punitive.

**Anti-retaliation constraint:** Measures must not be punitive toward the
complainant. Any measure that moves the complainant (rather than the
respondent) — without the complainant's informed, documented consent — is a
recognized retaliation risk.

**Decision matrix:**

| Risk Factor                                                   | Recommended Measure                                                |
| ------------------------------------------------------------- | ------------------------------------------------------------------ |
| Ongoing physical safety risk (threat, violence)               | Immediate physical separation; administrative leave for respondent |
| Evidence destruction risk (departing employee; system access) | System access restriction; accelerated document preservation       |
| Continued misconduct during investigation                     | Administrative leave for respondent or workspace separation        |
| Witness interference / intimidation risk                      | Administrative leave; no-contact directive; document all contacts  |
| Complainant feels unsafe continuing in shared workspace       | Consent-based workspace change or remote work arrangement          |
| No immediate safety or interference risk                      | No interim measure; enhance anti-retaliation monitoring            |

**Escalating restrictiveness:**

1. Anti-retaliation monitoring and management communication only
2. Remote work (with consent of affected party; operational feasibility check)
3. Reporting-line change (respondent moved to different manager; no consent required)
4. Workspace separation (respondent relocated; document as precautionary not punitive)
5. Restricted duties (remove supervisory authority over complainant specifically)
6. Paid administrative leave for respondent (standard where leave is required;
   unpaid leave before findings triggers independent wage and discrimination claims)

**[JURISDICTION-SPECIFIC US]:** Paid administrative leave is generally safest.
Unpaid leave before findings may be treated as an adverse employment action.
Involuntary transfer of complainant without consent is a potential retaliation
claim under EEOC Retaliation Guidance.

**[JURISDICTION-SPECIFIC UK]:** ACAS guidance: suspension should not be used
as punishment before investigation concludes. Suspension should be on full pay.
Suspension decision must be reviewed regularly — indefinite suspension can
constitute breach of the implied duty of trust and confidence (constructive
dismissal trigger).

**[JURISDICTION-SPECIFIC AU]:** Paid stand-down pending investigation is
generally permissible under Fair Work Act 2009 where there is a valid reason.
Must be on full pay. Prolonged stand-down without findings may become a
general protections claim. [VERIFY current FWC guidance on stand-down vs.
suspension]

---

## Credibility Assessment Framework

Apply this structured framework to each witness after their interview.
Document specific observations for each factor — never record only the
conclusion. Credibility must be evidence-anchored, not impression-based.

**EEOC Five-Factor Framework (adapted for all three jurisdictions):**

| Factor                    | Assessment                                                                                                                                                       | Notes                                                                                                                            |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Inherent Plausibility** | Is the account internally coherent? Does the sequence make sense given context? Do specific details (words, location, timing) add up?                            | Caution: "implausible" is susceptible to implicit bias — document why plausibility is in question                                |
| **Demeanor**              | Specific behavioral observations (forthcoming, evasive, consistent, inconsistent)                                                                                | Weight minimally; demeanor is the least reliable indicator and is cross-culturally variable; do not draw character conclusions   |
| **Motive to Fabricate**   | Specific, evidenced reason why witness would lie (not speculative) — prior adverse action by respondent against complainant; personal conflict; financial motive | The mere existence of a prior relationship is not motive to fabricate                                                            |
| **Corroboration**         | Witness testimony, documentary evidence, or absence of contradicting evidence consistent with the account                                                        | Note type of corroboration: contemporaneous report; medical/counseling record; email evidence; prior complaints about respondent |
| **Consistency**           | Internal consistency across interview; cross-account consistency with other witnesses on verifiable facts; documentary consistency                               | Distinguish minor peripheral inconsistencies (normal) from material inconsistencies on core facts                                |

**Credibility Classification:**

- **HIGH** — Account consistent, corroborated, plausible, no apparent motive
  to fabricate; demeanor forthcoming and consistent
- **MEDIUM** — Account generally consistent with some gaps; limited
  corroboration; or minor inconsistencies on peripheral facts
- **LOW** — Material inconsistencies; contradicted by documents; implausible
  account; or apparent strong, specific motive to fabricate
- **INCONCLUSIVE** — Insufficient basis to assess (limited interaction;
  witness declined to answer material questions)

**Anti-bias requirement:** Apply all five factors consistently across all
witnesses regardless of their protected characteristics. Structured credibility
worksheets (one per witness) ensure consistent application.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these six gates silently before delivering any plan output. If any gate
fails, revise before delivery.

| Gate                | Rule for Investigation Plans                                                                                                                                                           | Fail Action                                                           |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **Source**          | Every legal claim (mandatory reporting obligation, employee right, privilege basis) cites a specific statute, regulation, or established framework                                     | Add citation or mark "[UNVERIFIED — employment counsel to confirm]"   |
| **Format**          | All citations follow consistent format for the jurisdiction                                                                                                                            | Fix format                                                            |
| **Currency**        | Employment law changes frequently — EEOC guidance, NLRB GC memos, ACAS updates, AU WHS regulations. Flag authority where currency is doubtful                                          | Mark "[CHECK CURRENCY — verify current guidance]"                     |
| **Domain**          | Plan stays within the complaint's governing jurisdiction. Do not import US at-will doctrine into EU/AU investigation, or EU collective consultation requirements into US investigation | Remove or flag jurisdictional bleed                                   |
| **Proportionality** | Every investigation element (scope, timeline, intrusion) must be proportionate to complaint seriousness                                                                                | Flag and justify any element that exceeds what the complaint warrants |
| **Neutrality**      | Every statement about complainant, respondent, or alleged conduct must be neutral and factual — no conclusions, no characterizations, no outcome-presupposing language                 | Replace any prejudging language with neutral description              |

### Self-Interrogation

For COMPLEX and CRISIS tier classifications, and for any recommended interim
measure that restricts a party's activities, apply this 3-pass review:

**Pass 1 — Necessity:**

- Is every element of this plan actually required for this complaint?
- Does the investigation scope match the complaint scope, or has it drifted?
- Would a reasonable investigator design the plan this way?

**Pass 2 — Fairness:**

- Does the plan give the respondent a full and fair opportunity to respond?
- Are interim measures proportionate and non-punitive toward either party?
- Could the witness sequence be characterized as building a case before the
  respondent is heard?

**Pass 3 — Legal Exposure:**

- Does the plan itself create legal risk? (Does the complainant notification
  script inadvertently discourage seeking counsel? Does respondent notification
  reveal complainant's identity in a jurisdiction where that triggers additional
  liability?)
- Would this plan survive scrutiny in an employment tribunal or arbitration?
- Can any recommended interim measure be characterized as retaliatory or
  discriminatory on its face?

Mark the Glass Box audit trail: `self_interrogation: PASS` or
`self_interrogation: REVISED [describe what was revised]`

### Confidence Scoring

| Level        | Range     | Meaning in Investigation Plan Context                                                                                                           | Action                                                           |
| ------------ | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Mandatory obligation with clear statutory basis; no ambiguity (e.g., OSHA 8-hour fatality reporting)                                            | State as obligation                                              |
| **High**     | 0.80–0.94 | Strong authority; minor interpretation questions (e.g., EEOC position statement deadline in most circumstances)                                 | State with brief caveat                                          |
| **Probable** | 0.60–0.79 | Good practice supported by guidance but not black-letter law (e.g., recommended interview sequence)                                             | State as recommended practice with explicit reasoning            |
| **Possible** | 0.40–0.59 | Genuinely uncertain — jurisdictional variation or competing guidance (e.g., privilege applicability in a given state for HR-led investigations) | Present both positions; flag for employment counsel              |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                                                                                                                         | Do not assert; mark "[UNCERTAIN — employment counsel to advise]" |

### Glass Box Audit Trail

Append this YAML block to every plan output:

```yaml
glass_box:
  matter_name: "[Descriptive, non-prejudicial identifier]"
  complaint_type: "[Category from taxonomy]"
  tier_classification: "[PRELIMINARY / STANDARD / COMPLEX / CRISIS]"
  tier_rationale: "[Criteria that triggered this tier]"
  jurisdiction(s): "[Employment jurisdiction(s)]"
  investigator_recommendation: "[HR / Compliance / Employment counsel / Outside counsel]"
  conflict_screen: "[No conflict / Conflict identified — describe / Recusal recommended]"
  privilege_election: "[Attorney-led / HR-led / Undecided — requires employment counsel]"
  regulatory_deadlines_identified: "[Number and list]"
  interim_measures_recommended: "[Yes / No / Under consideration — describe]"
  interview_guides_produced: "[Number and categories — e.g., 8A, 8B, 8C]"
  document_checklist_produced: "Yes / No"
  legalcode_mcp: "Connected / Not connected"
  statutes_consulted:
    - "[Statute — VERIFIED or UNVERIFIED]"
  regulatory_guidance_consulted:
    - "[Guidance name — VERIFIED or UNVERIFIED; CHECK CURRENCY if applicable]"
  citations_verified: "[N VERIFIED] / [N UNVERIFIED]"
  self_interrogation: "PASS / REVISED — [describe revision] / NOT APPLICABLE (PRELIMINARY tier)"
  neutrality_gate: "PASS / REVISED"
  proportionality_gate: "PASS / REVISED"
  confidence_overall: "HIGH / MEDIUM / LOW — [rationale]"
  assumptions:
    - "[List all assumptions made due to incomplete input context]"
  limitations:
    - "[Scope limitations, jurisdiction gaps, unresolved CLARIFY items]"
  handoff_to_internal_investigation: "Yes — [specify which sections] / No / Partial"
  reviewer: "AI-assisted — requires review by qualified employment counsel before use"
```

---

## Anti-Patterns

Catalogue of what NOT to do in workplace investigation planning. Each
anti-pattern represents a recognized failure mode in the professional and
legal literature.

1. **Starting without a written mandate.** Launching witness interviews before
   the scope and mandate are documented. The investigator cannot answer "what
   were you asked to find?" in subsequent proceedings. Evidence gathered without
   a defined mandate is vulnerable to admissibility challenges.

2. **The mushy mandate.** Writing a scope document using vague language
   ("investigate concerns regarding the workplace environment") without
   allegation-specific questions. A mandate must specify each allegation as a
   discrete factual question the investigator must resolve.

3. **Delayed initiation.** Waiting days or weeks to begin after a complaint is
   received. Evidence degrades; memories fade; electronic records may be
   overwritten; the delay itself weakens the Faragher-Ellerth affirmative
   defense (US) and the "all reasonable steps" defence (UK); retaliation is
   more likely during the unmonitored gap.

4. **Conflicted investigator appointment.** Assigning an investigator who has
   a prior supervisory relationship with the respondent, a personal friendship
   with either party, or prior involvement in the events. This is the most
   common ground for findings of procedural unfairness in UK Employment
   Tribunal and AU Fair Work Commission proceedings.

5. **Failing to issue a legal hold.** Not issuing a legal hold notice upon
   receipt of a complaint that could lead to litigation. Auto-deletion policies
   will continue running absent explicit hold instructions. Courts impose
   adverse inference instructions or monetary sanctions under FRCP Rule 37(e)
   for ESI lost due to failure to preserve.

6. **Interviewing the respondent first.** Alerting the respondent to the
   allegations before independent corroborating evidence is gathered enables
   witness coordination, deprives the investigator of the evidentiary base
   needed to challenge the respondent's account, and is recognized as a common
   structural error in investigation literature.

7. **Leading questions.** Questions that suggest the answer ("you knew this
   was inappropriate, didn't you?") contaminate witness accounts, undermine
   investigation integrity, and expose the investigation to challenge in
   subsequent proceedings.

8. **Failing to put specific allegations to the respondent.** Interviewing the
   respondent on vague or general accusations without providing specific written
   notice of each allegation before the interview. This violates ACAS Code
   requirements (UK), procedural fairness requirements under FWA s.387 (AU),
   and EEOC best practices (US).

9. **Broad confidentiality instructions to witnesses [US].** Instructing
   employees "do not discuss this investigation with anyone" may violate NLRA
   Section 7 rights. The correct instruction is to maintain confidentiality
   "to the extent possible" without prohibiting contact with union
   representatives or personal counsel.

10. **The dual-hat HR investigator.** Using the HR Business Partner who manages
    the respondent's team as the investigator. This creates an actual or
    perceived conflict of interest, makes the HR professional a potential
    witness in litigation, and undermines impartiality.

11. **Over-reliance on demeanor evidence.** Concluding a witness is not
    credible primarily because of their interview demeanor (nervous, stoic,
    emotional). Demeanor is the least reliable credibility indicator and is
    susceptible to bias based on cultural norms, neurodiversity, and trauma
    response.

12. **Failing to protect the complainant from retaliation during the
    investigation.** Not implementing anti-retaliation communications and
    monitoring after a complaint is received. Retaliation is the most common
    EEOC charge category and independently actionable.

13. **Undocumented scope expansion.** Expanding the investigation when new
    allegations surface mid-interview without documenting the decision and
    obtaining mandate authority. This creates due process risks for the
    respondent and creates a "fishing expedition" appearance in litigation.

14. **Confirmation bias — reaching conclusions before evidence is complete.**
    Forming a conclusion after the complainant interview and conducting
    subsequent interviews to confirm rather than test it. This is a
    well-documented cognitive failure mode in investigations.

15. **Investigation reports that make legal conclusions.** Writing findings
    reports that state "the respondent violated Title VII" or "the conduct was
    unlawful." Investigators make factual findings; legal determinations belong
    to counsel. Legal conclusions in investigation reports may waive privilege
    and may be used against the employer in litigation as admissions.

16. **Using a one-size-fits-all intake form.** Applying generic complaint
    intake forms to all complaint types regardless of allegation nature.
    Harassment, retaliation, wage-hour, and safety complaints require different
    preliminary questions and evidence preservation steps.

17. **Not confirming the privilege framework before commencing.** Beginning
    interviews without deciding whether the investigation is attorney-led
    (Upjohn warning required, potential privilege protection) or HR-led (no
    Upjohn warning, no privilege). This is an irreversible decision.

18. **Indefinite administrative leave without review.** Placing the respondent
    on paid leave and allowing the investigation to drag without a defined
    timeline and regular review. Extended leave may constitute an adverse
    employment action or, in some circumstances, a constructive dismissal
    trigger (UK) or general protections concern (AU).

19. **Interim measures that burden the complainant.** Requiring the complainant
    to transfer to a different shift, team, or location as an interim measure.
    This is a recognized form of constructive retaliation — the respondent
    bears the burden of any operational adjustment.

20. **Failure to monitor for retaliation post-resolution.** Completing the
    investigation and implementing discipline without establishing an explicit
    anti-retaliation monitoring plan. Retaliation that occurs after the
    investigation closes is separately actionable and may trigger new charges.

21. **Failing to consider cross-border dimensions.** When complainant and
    respondent are in different countries, the investigation plan must address
    which law governs, what local counsel must be engaged, and whether GDPR
    or other data protection law constrains transfers of investigation materials
    across borders. [JURISDICTION-SPECIFIC: EU GDPR Art. 88; German BetrVG;
    French Code du travail consultation requirements]

22. **Delivering a plan without flagging open items.** Producing an
    investigation plan that appears complete but contains hidden assumptions
    about jurisdiction, employment status, union coverage, or regulatory
    applicability without flagging them as open items. A plan with explicit
    open items is actionable; a plan with hidden assumptions is dangerous.

---

## Writing Standards

Apply plain-language discipline and neutrality to all plan output.

**Neutrality discipline:**

- Use "complainant" and "respondent" — not "victim" and "accused"
- Use "alleged conduct" — not "misconduct" before findings are made
- Use "the events described" — not "the harassment" or "the discrimination"
- Document what parties said they observed; do not characterize it in
  legal terms
- Plans and interview guides must not presuppose the outcome of the
  investigation

**Plain language requirements:**

- Active voice: "Interview the complainant" not "The complainant should
  be interviewed"
- Specific, not generic: "Collect Slack messages between [Party A] and
  [Party B] from [date range]" not "Collect relevant electronic communications"
- Opening scripts must be verbatim-ready (quoted blocks) so a non-lawyer
  HR professional can read them aloud without confusion
- Interview questions must be open-ended by default; specific only after
  narrative is established

**Quality gates before delivery:**

1. Can a trained HR professional (non-lawyer) understand and use each
   interview guide without additional instruction?
2. Would this investigation plan survive scrutiny in an employment tribunal
   or arbitration proceeding?
3. Is every regulatory obligation backed by a specific citation (or marked
   [VERIFY])?
4. Does any language presuppose the outcome of the investigation? If yes,
   revise.
5. Are all interim measures phrased in a way that cannot be characterized
   as retaliatory toward either party?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal
research tool.

**With legalcode-mcp connected (preferred):**

- In Step 7, search for current regulatory deadlines: EEOC procedural rules
  (29 C.F.R. Part 1601); OSHA incident reporting rules (29 C.F.R. Part 1904);
  NLRB charge rules (29 C.F.R. Part 102); EU Whistleblowing Directive
  transposition status in the relevant member state; AU Fair Work Commission
  procedural rules
- In Steps 5 and 9, search for jurisdiction-specific employee rights during
  investigations (UK right to be accompanied ERA 1999 s.10; German BetrVG
  works council requirements; French Code du travail CSSCT consultation)
- Save the most relevant results to a local temporary reference file
  (e.g., `/tmp/legalcode-investigation-plan-authority.md`)
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box
  audit trail

**Without legalcode-mcp:**

- Mark all regulatory deadline and statutory citations with [VERIFY]
- Note in the Glass Box audit trail:
  `external_tools_used: "None — manual verification required"`
- Focus the plan on structural design and process architecture; flag all
  specific regulatory claims for counsel verification before use in a live
  matter

**Handoff to legalcode-internal-investigation:**
The investigation charter draft (Step 6 output) is directly usable as input
to `legalcode-internal-investigation`. Step 12 must produce a structured
handoff note specifying which plan elements are ready for execution by
`legalcode-internal-investigation`, including: legal hold distribution list,
privilege framework election, ESI preservation steps, and the witness matrix.

---

## Output Format Template

Structure the assembled investigation plan as follows:

```markdown
## Workplace Investigation Plan

**Matter Name**: [Descriptive but non-prejudicial identifier]
**Date of Plan**: [Date]
**Complaint Received**: [Date]
**Tier Classification**: [PRELIMINARY / STANDARD / COMPLEX / CRISIS]
**Tier Rationale**: [One-sentence explanation of criteria]
**Plan Prepared by**: [AI-assisted — requires employment counsel review before use]

---

## 1. Complaint Summary

**Complainant**: [Name or "Anonymous" / Status: current employee / former employee / contractor]
**Respondent**: [Name / Title / Relationship to complainant]
**Complaint Type**: [Primary type from taxonomy]
**Date(s) of Alleged Conduct**: [Range]
**Complaint Channel**: [Internal / Hotline / EEOC charge / OSHA / FWC / Other]
**Summary of Allegations**: [Neutral factual summary — not conclusions]
**Urgency Flags**: [List: ongoing harm / safety risk / retaliation risk / regulatory deadline / none]

---

## 2. Investigation Scope and Charter

**In Scope**: [Specific conduct, time period, named parties]
**Out of Scope**: [Explicitly excluded — prevents scope creep]
**Investigative Questions**: [Discrete factual questions the investigator must resolve — one per allegation]
**Authorization Basis**: [HR Director / General Counsel / Board resolution]
**Burden of Proof Standard**: [Preponderance / Reasonable belief / Balance of probabilities]
**Applicable Policies**: [Named policies in effect at the time of alleged conduct]
**Confidentiality Framework**: [To whom disclosed; how maintained]
**Privilege Election**: [Attorney-led — Upjohn warning required / HR-led — work product only / TBD — consult employment counsel]

---

## 3. Investigator Assignment

**Lead Investigator**: [Name / Title / Function]
**Supporting Investigator(s)**: [If any]
**Conflict-of-Interest Screen**: [No conflict / Conflict identified — describe / Recusal required]
**Independence Assessment**: [Neutral party analysis rationale]
**Outside Counsel Engaged**: [Yes / No / Recommended — consult GC]

---

## 4. Regulatory Deadline Map

| Obligation   | Framework                     | Deadline | Action Owner | Status  |
| ------------ | ----------------------------- | -------- | ------------ | ------- |
| [Obligation] | [Statute/regulation — VERIFY] | [Date]   | [HR / Legal] | Pending |

[Mark N/A for inapplicable obligations]

---

## 5. Interim Protective Measures

**Assessment**: [Immediate action required / Under consideration / Not currently warranted]
**Recommended Measures**: [Specific options with proportionality rationale]
**Implementation Steps**: [Who takes what action by when]
**Anti-Retaliation Note**: [Measures are precautionary; confirm no measures burden the complainant without their consent]

---

## 6. Communication Plan

**Complainant notification**: [Content; timing; communicator]
**Respondent notification**: [When notified; content; approach to allegation disclosure]
**Manager/supervisor in chain**: [What they are told; anti-retaliation instructions]
**Workforce communication**: [None recommended unless CRISIS tier; placeholder language if required]

---

## 7. Witness List and Interview Sequence

| Priority | Witness | Category        | Role      | Est. Duration | Special Considerations       |
| -------- | ------- | --------------- | --------- | ------------- | ---------------------------- |
| 1        | [Name]  | Corroborating   | [Explain] | 45 min        | [Union rep / support person] |
| 2        | [Name]  | Complainant     | Primary   | 90 min        | [Counsel retained?]          |
| 3        | [Name]  | Process witness | [Manager] | 30 min        | [Potential dual interest]    |
| 4        | [Name]  | Respondent      | Primary   | 90 min        | [Written allegations prior?] |

**Sequencing Rationale**: [Why this order — protective logic]

---

## 8. Interview Guides

[Attach 8A, 8B, 8C and, for COMPLEX/CRISIS tiers, 8D — see Interview Guide Templates]

---

## 9. Document and Evidence Collection Checklist

| Document Category | Allegation Element | Priority            | Custodian | Collection Method | Status  |
| ----------------- | ------------------ | ------------------- | --------- | ----------------- | ------- |
| [Category]        | [Element]          | HIGH / MEDIUM / LOW | [Named]   | [Method]          | Pending |

---

## 10. Investigation Timeline

| Milestone                        | Target Date  | Owner                   | Status |
| -------------------------------- | ------------ | ----------------------- | ------ |
| Plan approved and distributed    | [Date]       | HR / Legal              |        |
| Legal hold / preservation issued | [Date]       | Legal / IT              |        |
| Interim measures implemented     | [Date]       | HR                      |        |
| Corroborating witness interviews | [Date range] | Investigator            |        |
| Complainant interview            | [Date]       | Investigator            |        |
| Document review                  | [Date range] | Investigator            |        |
| Respondent interview             | [Date]       | Investigator            |        |
| Preliminary findings review      | [Date]       | Investigator + Legal    |        |
| Report draft                     | [Date]       | Investigator            |        |
| Final report                     | [Date]       | Investigator            |        |
| Remediation decisions            | [Date]       | HR + Management + Legal |        |

---

## 11. Handoff to Full Investigation Execution

**Handoff to legalcode-internal-investigation**: [Yes / No / Partial]
**Elements ready for handoff**: [Legal hold distribution list / ESI preservation steps / Privilege framework / Witness matrix]
**Open Items before handoff**: [List of unresolved decisions or missing information]

---

## Glass Box Audit Trail

[YAML block per Glass Box Audit Trail template above]
```

---

## Localization Notes

To create a jurisdiction-specific variant of this skill:

1. Replace [JURISDICTION-SPECIFIC] markers with verified local statutory
   and regulatory content for the target jurisdiction
2. Replace [VERIFY] tags with confirmed current authority citations
3. Add jurisdiction-specific mandatory process requirements (e.g., POSH
   Act 2013 ICC composition requirements for India; EU works council
   consultation rights; PIDA prescribed persons for UK external disclosures)
4. Update the Regulatory Deadline Map with jurisdiction-specific timelines
5. Update interview guide scripts with jurisdiction-specific rights notices
   (right to be accompanied scripts for UK; union representative rights
   notices for US)
6. Add local language requirements if investigation documents must be
   provided in the local official language

**Existing related skills by jurisdiction:**

- US employment law dimensions: `legalcode-non-compete-enforceability`,
  `legalcode-wage-hour-compliance-audit`
- EU data protection constraints on investigation materials: `legalcode-dpa-review-and-negotiation`

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis using a 2-agent
research pipeline. Agent 1 (Structural Analyst and Legal Researcher):
researched EEOC guidance and Quality Practices framework; ACAS Code of
Practice on Disciplinary and Grievance Procedures; Fair Work Act 2009 s.387
procedural fairness requirements; _Upjohn Co. v. United States_ 449 U.S. 383
(1981) and Upjohn warning structure; _Three Rivers District Council v. Bank
of England (No. 5)_ [2003] EWCA Civ 474 (UK privilege); _Esso Australia
Resources Ltd v. Commissioner of Taxation_ (1999) 201 CLR 49 and _Crafti v.
Cohealth Limited_ [2025] FWC 3285 (AU privilege); _Faragher v. City of Boca
Raton_ 524 U.S. 775 (1998) and _Burlington Industries v. Ellerth_ 524 U.S.
742 (1998); EU Whistleblowing Directive 2019/1937; Worker Protection
(Amendment of Equality Act 2010) Act 2023; EEOC credibility assessment
five-factor framework; professional investigation literature from DLA Piper,
Ogletree, Mayer Brown, Fisher Phillips, HR Acuity, Case IQ, Rubin Thomlinson,
and Clyde & Co; witness sequencing standards; interim protective measures
proportionality frameworks; findings classification standards; anti-pattern
catalogue from SafetyCulture, Case IQ, Ogletree, and Nolo. Agent 2 (Prompt
Engineering and Quality Analyst): analyzed legalcode-contract-review (gold
standard), legalcode-internal-investigation, and legalcode-aml-kyc-compliance
to calibrate CLARIFY point design, tier classification framework, Glass Box
YAML structure, six-gate Citation Quality Gates (including Neutrality and
Proportionality gates specific to investigation planning), three-pass
Self-Interrogation framework adapted for fairness assessment, output template
architecture, and 22-item anti-patterns catalogue. Jurisdiction-agnostic core
with US/UK/AU markers. Designed as the planning complement to
legalcode-internal-investigation.
