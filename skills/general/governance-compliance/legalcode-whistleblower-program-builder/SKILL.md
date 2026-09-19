---
name: legalcode-whistleblower-program-builder
description: Build, audit, or optimize a whistleblower program compliant with EU Whistleblower Directive
  2019/1937, US Sarbanes-Oxley (SOX) Section 806, Dodd-Frank Act Section 922 (SEC Whistleblower Program),
  France Sapin II / Loi Waserman (LOI n° 2022-401), and UK Public Interest Disclosure Act 1998 (PIDA /
  ERA 1996 Part IVA). Use when building a new whistleblower program from scratch, auditing an existing
  program for compliance gaps, optimizing procedures for a specific jurisdiction or M&A integration, preparing
  a board readiness assessment, or reviewing employment agreements for confidentiality language that impedes
  protected reporting.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Build, audit, or optimize a whistleblower program compliant with EU Whistleblower Directive 2019/1937, US Sarbanes-Oxley (SOX) Section 806, Dodd-Frank Act Section 922 (SEC Whistleblower Program), France Sapin II / Loi Waserman (LOI n° 2022-401), and UK Public Interest Disclosure Act 1998 (PIDA / ERA 1996 Part IVA). Covers reporting channel design (internal and external), intake triage, investigation procedures, confidentiality obligations, anti-retaliation protections, program governance, regulatory deadline mapping, and board reporting. Use when building a new whistleblower program from scratch, auditing an existing program for compliance gaps, optimizing procedures for a specific jurisdiction or M&A integration, preparing a board readiness assessment, or reviewing employment agreements for confidentiality language that impedes protected reporting. Jurisdiction-agnostic framework with deep EU, US, FR, and UK specific analysis. Also applicable to CFTC, NLRB, OSHA, FCA, and sector-specific whistleblower regimes.


# Legalcode Whistleblower Program Builder

> **Disclaimer**: This skill provides a framework for AI-assisted whistleblower program
> design and compliance review. It does not constitute legal advice. All outputs must be
> reviewed by a qualified legal professional licensed in the relevant jurisdiction before
> use or implementation. Laws change; verify current applicability of all statutory
> references before relying on them. Regulatory guidance, enforcement priorities, and case
> law interpretations cited from training data carry hallucination risk — verify against
> authoritative sources. Whistleblower program design involves sensitive employment law,
> investigative procedure, and regulatory compliance obligations that require experienced
> counsel.

## Purpose and Scope

This skill designs, audits, and optimizes whistleblower programs across the four primary
regulatory regimes: EU Directive 2019/1937, US SOX §806 / Dodd-Frank §922, France Sapin II
/ Loi Waserman, and UK PIDA 1998. It covers every phase of program lifecycle — from channel
design through intake triage, investigation planning, anti-retaliation enforcement, and board
reporting.

**Covers:**

- Four-jurisdiction statutory compliance assessment (EU / US / FR / UK)
- Reporting channel architecture (internal, external, anonymous, multi-language)
- Intake triage and complaint routing procedures
- Investigation protocol design and investigator independence framework
- Confidentiality obligations and identity protection procedures
- Anti-retaliation framework design with burden-of-proof analysis
- Protected activity catalogue across all four regimes
- Regulatory deadline mapping and escalation triggers
- Board and audit committee governance and reporting
- Employment agreement audit for prohibited impediment language (Dodd-Frank Rule 21F-17)
- Program maturity assessment against COMPLIANT / PARTIAL / NON-COMPLIANT framework
- Glass Box audit trail for traceability and regulatory examination

**Does not:**

- Conduct live investigations (see `legalcode-investigation-plan-builder` for that workflow)
- Provide legal advice or substitute for qualified employment or regulatory counsel
- Apply exclusively to one jurisdiction — jurisdiction-agnostic scaffold with
  [JURISDICTION-SPECIFIC] markers for EU, US, FR, and UK deep content

---

## Jurisdiction and Governing Law

This skill is multi-jurisdiction by design. The four primary regimes operate in parallel
for multinational organizations, and the most protective standard across them defines the
minimum program floor.

[JURISDICTION-SPECIFIC EU] **EU Directive 2019/1937**: Applies to organizations with 50+
employees in EU Member States (phase-in to December 2023 for 50-249 employees). Requires
simultaneous internal AND external reporting channels. No mandatory internal escalation
hierarchy. 7-day acknowledgment, 3-month feedback obligation. Covers all workers including
contractors, trainees, volunteers, shareholders. Anonymous reporting optional per Member
State implementation but must be handled equally if accepted. Transposed but deficiencies
reported by Commission in July 2024; infringement procedures threatened.

[JURISDICTION-SPECIFIC US] **SOX Section 806** (18 U.S.C. § 1514A): Applies to all
publicly traded companies registered under Securities Exchange Act §12 or filing under
§15(d), including subsidiaries and contractors. No employee size threshold. Audit committee
must establish confidential and anonymous complaint procedures. 180-day OSHA filing deadline
for retaliation claims. DOL/OSHA enforcement.

[JURISDICTION-SPECIFIC US] **Dodd-Frank Section 922** (15 U.S.C. § 78u-6; Rule 21F-17):
Applies to all SEC-regulated entities. Direct external SEC reporting permitted without
internal escalation. No employment agreement may impede SEC communications (Rule 21F-17 safe
harbor). SEC FY 2024: 45,130 tips received; $255 million in awards. $18 million penalty
against J.P. Morgan Chase (2024) for settlement agreements impeding whistleblower
communications. Two Sigma Investments enforcement action (January 2025).

[JURISDICTION-SPECIFIC FR] **Sapin II / Loi Waserman** (LOI n° 2016-1691; LOI n° 2022-401):
Applies to organizations with 50+ employees (Waserman; previously 500+ under Sapin II). No
mandatory reporting hierarchy (Waserman innovation). Criminal penalties: up to €30,000 and
2 years imprisonment for revealing whistleblower identity; up to €15,000 and 1 year for
obstructing reports. Administrative fines up to €1,000,000 for legal entities failing to
maintain procedures.

[JURISDICTION-SPECIFIC UK] **PIDA 1998** (Employment Rights Act 1996, Part IVA): No
organizational size threshold — universal application. Applies to all workers (employees,
contractors, agency workers, trainees). Unlimited tribunal compensation for retaliation.
Six categories of protected wrongdoing. No statutory confidentiality requirement but best
practice essential. 2024 key cases: Sullivan v Isle of Wight Council (EAT — external
applicants except NHS); "collective memory" doctrine emerging (distributed organizational
knowledge may establish retaliation knowledge).

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
organizational context, the workflow pauses and asks when:

- The answer materially changes the regulatory framework that applies
- Multiple valid program design approaches exist and business context determines the choice
- Jurisdiction coverage or organizational structure is ambiguous
- Risk tolerance or compliance maturity level is needed to calibrate recommendations

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

### Step 1: Accept Input

Accept the engagement in any of these forms:

- **New build**: Organization description + jurisdiction(s) + employee count + regulatory
  drivers
- **Audit request**: Existing program documentation, policies, procedures, or description
  of current state
- **Agreement review**: Employment, separation, consulting, or NDA agreements for
  prohibited impediment language
- **M&A integration**: Description of acquiring and target company programs to harmonize
- **Board readiness**: Request for executive-facing assessment and investment case

If insufficient context is provided, proceed to Step 2 immediately.

---

### Step 2: Gather Context

**⟁ CLARIFY** — Ask the following before proceeding. Skip questions the user has already
answered:

**1. Operating mode** — What should this engagement produce?

- **Build new program** — Full program design, policies, procedures, governance, rollout
  roadmap
- **Audit existing program** — Gap assessment against applicable regulatory requirements
- **Channel design only** — Intake and routing architecture
- **Employment agreement review** — Audit for Rule 21F-17 / Loi Waserman impediment
  language
- **Board readiness** — Executive summary, maturity score, investment case
- _Why this matters_: Each mode produces different outputs and engages different sections
  of the workflow.

**2. Jurisdictions in scope** — Which regimes apply?

- EU Directive 2019/1937 (and which Member State implementations?)
- US SOX §806 (publicly traded or subsidiary of public company?)
- US Dodd-Frank §922 (SEC-regulated entity?)
- France Sapin II / Loi Waserman (50+ employees in France?)
- UK PIDA 1998 (workers in the UK?)
- Other (CFTC, NLRB, FCA, sector-specific?)
- _Why this matters_: Determines which statutory requirements are active; multiple
  jurisdictions may impose conflicting obligations requiring the highest-standard approach.

**3. Organization profile** — Provide these details:

- Employee count (total globally; per jurisdiction)
- Industry sector (financial services, healthcare, technology, manufacturing, other)
- Publicly traded, private, non-profit, or public authority?
- Existing reporting channels (hotline, web portal, manager escalation, none)?
- _Why this matters_: Organizational thresholds trigger different obligations; sector
  determines which prescribed regulators / external channels are relevant.

**4. Current program state** — For audits and optimization:

- Written policy exists? (yes / partial / no)
- Reporting channel in operation? (yes / partial / no)
- Last program review or external audit date?
- Known compliance gaps or recent incidents?
- _Why this matters_: Determines whether to build from scratch or remediate.

---

### Step 3: Map Regulatory Obligations

Based on Step 2 context, map the active regulatory obligations for each jurisdiction
in scope. Produce a **Regulatory Obligation Matrix** covering:

| Obligation           | EU 2019/1937 | SOX §806         | Dodd-Frank §922  | Sapin II/Waserman | PIDA/ERA      |
| -------------------- | ------------ | ---------------- | ---------------- | ----------------- | ------------- |
| Size threshold       | 50+ EE       | Public cos.      | SEC-regulated    | 50+ EE            | None          |
| Internal channel     | Required     | Required         | Optional         | Required          | Preferred     |
| External channel     | Required     | Implied          | Required (SEC)   | Required          | Regulator     |
| 7-day acknowledgment | Required     | No               | No               | Recommended       | No            |
| 3-month feedback     | Required     | No               | No               | Recommended       | No            |
| Confidentiality      | Mandatory    | Required         | Required         | Mandatory         | Best practice |
| Anonymous support    | Per MS       | Required         | Yes (w/ counsel) | Required          | Optional      |
| Anti-retaliation     | Art. 19      | 18 U.S.C. §1514A | Rule 21F-2       | Waserman Ch. III  | ERA s.47B     |

Identify the **compliance floor** — the most stringent requirement across active
jurisdictions becomes the minimum standard for the program.

---

### Step 4: Assess Existing Program (Audit Mode Only)

For audit or optimization engagements, assess the current program against the six core
domains (see Section: Program Component Framework). Rate each domain:

- **COMPLIANT** — Meets or exceeds all applicable requirements
- **PARTIAL** — Partially meets requirements; specific gaps identified
- **NON-COMPLIANT** — Fails to meet requirements; regulatory exposure exists
- **NOT ASSESSED** — Insufficient information to evaluate

Apply the **Self-Interrogation** framework (see Quality Assurance) to any domain rated
NON-COMPLIANT before finalizing the assessment.

**⟁ CLARIFY** — For any domain rated PARTIAL or NON-COMPLIANT:

- Is there a remediation plan in place? If yes, what is its status?
- Has the organization received any regulatory inquiry or enforcement action in this area?
- What is the deadline for remediation (regulatory, board-imposed, or operational)?

---

### Step 5: Design or Remediate Reporting Channels

Design the **channel architecture** covering:

**Internal Channels (required under EU Directive, SOX, Sapin II/Waserman)**

- Dedicated reporting platform options: hotline (phone), secure web portal, email-to-
  designated officer, physical drop-box
- **Best practice**: Third-party intake service for credibility and independence
- Language requirements: Native language(s) of workforce; EU Directive Art. 9 requires
  accessible procedures [JURISDICTION-SPECIFIC EU]
- Routing map: Who receives reports? (Compliance Officer / GC / Audit Committee /
  Independent Ombudsperson)
- Anonymity capability: Must support anonymous intake if accepted under applicable law
- Documentation: Each channel must generate a receipt confirmation and maintain
  secure records

**External Channels (reference guidance, not operation)**

Document and communicate the applicable external reporting options:

[JURISDICTION-SPECIFIC US]: SEC Office of the Whistleblower (sec.gov/whistleblower);
OSHA Whistleblower Protection Program; DOJ; CFTC (commodity-related matters); FinCEN
(AML/sanctions); NLRB (labor relations); EPA (environmental)

[JURISDICTION-SPECIFIC EU]: National competent authorities per Directive 2019/1937 Art. 11
(list varies by Member State and subject matter; each MS designates one or more authorities)

[JURISDICTION-SPECIFIC FR]: Défenseur des droits (external authority); AFA
(Agence française anticorruption) for Sapin II compliance

[JURISDICTION-SPECIFIC UK]: Prescribed regulators per ERA 1996 s.43F and Schedule
(FCA, FRC, CMA, HMRC, HSE, Environment Agency, and others by sector); Protect charity
(independent whistleblowing advice)

**⟁ CLARIFY** — Channel architecture decision:

- Should the organization operate its own internal channel or engage a third-party
  provider?
- Is anonymous reporting currently supported? If not, must it be? (Mandatory under
  Dodd-Frank for audit committee procedures; supported under EU Directive; required
  under Waserman)
- Are multi-language materials required? Which languages?

---

### Step 6: Draft Intake Triage and Routing Procedures

Design the **intake triage procedure** — the decision logic applied to every incoming
report. Every report must be:

1. **Received and date-stamped** (triggers 7-day acknowledgment clock under EU/FR)
2. **Classified by allegation type** (see Protected Activity Catalogue)
3. **Assigned an Investigation Complexity Tier** (see Complexity Tiers section)
4. **Routed** to the appropriate handler and regulatory channel
5. **Acknowledged** to the reporter within 7 days (EU/FR mandatory; US/UK best practice)

**Routing Logic**

| Allegation Type               | Primary Route                       | Escalation Trigger                                  |
| ----------------------------- | ----------------------------------- | --------------------------------------------------- |
| Securities fraud / accounting | Audit Committee                     | Immediately + outside counsel                       |
| Anti-bribery / corruption     | GC / CCO                            | Board if executive involved                         |
| Workplace harassment / safety | HR + Compliance                     | Compliance if pattern; outside counsel if executive |
| Environmental / public health | CCO + Regulatory Affairs            | Regulator notification if mandatory                 |
| Data protection / privacy     | DPO + GC                            | Supervisory Authority if data breach                |
| Retaliation against reporter  | Audit Committee / Board             | Outside counsel immediately                         |
| Financial misreporting        | CFO is conflicted → Audit Committee | Outside counsel immediately                         |

**Confidentiality Protocol at Intake**

- Reporter identity and content must be accessible **only to designated personnel**
  (not operational line management unless necessary) — EU Art. 16; Waserman; Dodd-Frank
  Rule 21F-17
- Separate investigation file from HR/personnel files where possible
- Coded case reference system to minimize identity exposure
- Written record of any authorized identity disclosure with stated reason

---

### Step 7: Build Investigation Protocol

Design the **investigation protocol** — the standardized procedures for investigating
reports once triaged. For full investigation planning, cross-reference
`legalcode-investigation-plan-builder`.

**Core Protocol Elements**

1. **Investigator Independence**: Screen for conflicts (respondent's manager, HR business
   partner for respondent, anyone in respondent's reporting line)
2. **Privilege Election**: Decide at outset whether investigation is attorney-directed
   (privilege protection applies) or HR-directed (potentially discoverable). Document
   the decision and rationale.
3. **Upjohn Warnings** [JURISDICTION-SPECIFIC US]: Script required interview opening;
   applies to corporate employees only; document compliance
4. **Investigator Assignment Matrix**:

| Complexity Tier | Investigator                                           | Counsel Requirement                         |
| --------------- | ------------------------------------------------------ | ------------------------------------------- |
| PRELIMINARY     | HR officer / CCO designee                              | Optional                                    |
| STANDARD        | Compliance professional                                | Optional; recommended if executive-adjacent |
| COMPLEX         | CCO + outside employment counsel                       | Required                                    |
| CRISIS          | Outside counsel lead; board committee direct oversight | Required; GC and CEO involved               |

5. **Timeline Standards** (See Complexity Tiers for detail)
6. **Evidence Preservation**: Litigation hold obligation triggers on first reasonable
   anticipation of litigation or regulatory proceeding — apply early
7. **Feedback to Reporter**: Acknowledge within 7 days; substantive update within 3 months
   (EU/FR mandatory; US/UK best practice)

---

### Step 8: Design Anti-Retaliation Framework

The anti-retaliation framework is the core protective mechanism of any whistleblower
program. Design it in three layers:

#### Layer 1 — Prohibited Conduct Definition

Define explicitly prohibited retaliatory actions per applicable statute:

**All Jurisdictions**: Discharge, demotion, suspension, harassment, discrimination in
compensation or terms of employment, threats, exclusion from activities.

[JURISDICTION-SPECIFIC US] **Additional Dodd-Frank prohibitions**: Any action to impede
communication with SEC; enforcement of confidentiality agreements against SEC reporting;
requiring waiver of right to SEC report (Rule 21F-17(a) — $18M JP Morgan penalty 2024).

[JURISDICTION-SPECIFIC EU] **Art. 19 Directive 2019/1937**: Prohibition extends to
facilitators and associated persons (colleagues, family members, legal representatives).

[JURISDICTION-SPECIFIC FR] **Loi Waserman**: Criminal penalties for revealing identity
(up to €30,000 / 2 years imprisonment); criminal penalties for obstructing report
(up to €15,000 / 1 year imprisonment).

[JURISDICTION-SPECIFIC UK] **ERA 1996 s.47B**: Detriment prohibited from any act or
deliberate failure to act by employer or co-worker. Worker Protection Act 2023 (effective
October 2024): Positive duty on employers to prevent workplace harassment (impacts
retaliation culture).

#### Layer 2 — Burden of Proof Analysis

Understanding the burden of proof determines how organizations must document
employment actions involving known or suspected whistleblowers:

| Jurisdiction      | Initial Burden                                                | Burden Shift                                                                 | Standard                                          |
| ----------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------- |
| US (SOX)          | Complainant shows protected activity + adverse action + nexus | Employer must show same action without whistleblowing                        | Contributing factor standard (lower than but-for) |
| US (Dodd-Frank)   | Complainant shows protected activity + adverse action         | Employer must show clear and convincing non-retaliatory reason               | Heightened employer burden                        |
| EU                | Complainant shows protected activity + adverse action         | Presumption of retaliation if adverse action within defined period of report | Employer must disprove                            |
| France (Waserman) | Good faith report + adverse action                            | Reverse onus (employer proves action unrelated)                              | Employer bears burden                             |
| UK (PIDA)         | Worker shows protected disclosure + detriment                 | Employer must show reason for detriment unrelated to disclosure              | Balance of probabilities after burden shifts      |

**Implication**: Any employment action taken within a defined window after a protected
disclosure requires careful documentation of independent business justification. Advise
HR and managers to route proposed adverse actions involving known reporters through legal
review before execution.

#### Layer 3 — Interim Protective Measures

Implement protective measures during investigation, before findings are made:

- Do NOT automatically suspend or place on administrative leave the reporter
  (creates retaliation presumption risk)
- Consider separating reporter and respondent (neutral transfer, remote work) without
  penalizing reporter
- Provide written assurance to reporter that status is not affected by report
- If reporter faces ongoing safety risk from continued exposure to respondent, treat
  as emergency and escalate immediately
- Apply interim measures proportionately; document decision-making

---

### Step 9: Design Governance and Board Reporting

Build the **governance architecture** for ongoing program oversight:

**Board / Audit Committee Roles**

[JURISDICTION-SPECIFIC US] **SOX §301 Audit Committee**: Must establish complaint receipt
and anonymous submission procedures; must review whistleblower matters quarterly (minimum);
must receive immediate escalation of material accounting / control issues.

**All Jurisdictions**: Board/Audit Committee should receive:

- Quarterly summary of reports received, classification, and status
- Immediate escalation of: CRISIS-tier matters, regulatory inquiries involving
  whistleblower allegations, allegations against C-suite or board members
- Annual program effectiveness review (aligned with DOJ ECCP 2024 "works in practice"
  assessment question)

**Chief Compliance Officer (CCO) Obligations**

- Functional independence from business units; direct reporting line to board or audit
  committee (not solely through GC or CEO) [JURISDICTION-SPECIFIC US — DOJ ECCP preference]
- Written investigation procedures maintained and updated
- Access controls on complaint database reviewed annually
- Annual report to board on program metrics, trends, and gaps

**Program Metrics Dashboard** (recommended minimum)

| Metric                         | Frequency  | Purpose                                |
| ------------------------------ | ---------- | -------------------------------------- |
| Reports received (by channel)  | Monthly    | Channel utilization                    |
| Reports by allegation category | Quarterly  | Risk area identification               |
| Time-to-acknowledgment         | Per report | Regulatory compliance                  |
| Time-to-close                  | Per report | Operational efficiency                 |
| Substantiation rate            | Quarterly  | Program credibility                    |
| Retaliation claims filed       | Quarterly  | Anti-retaliation program effectiveness |
| External regulatory referrals  | Quarterly  | Cooperation tracking                   |

---

### Step 10: Employment Agreement Audit (Dodd-Frank / Waserman)

For Dodd-Frank and Loi Waserman compliance, audit all standard employment agreements,
separation agreements, consulting agreements, and NDAs for language that may impede
protected reporting.

**Prohibited Language Patterns**

[JURISDICTION-SPECIFIC US — Dodd-Frank Rule 21F-17]:

- "You agree not to disclose any information about this company to any third party,
  including regulatory authorities" ← **RED: Impedes SEC/OSHA/DOJ reporting**
- "You release all claims and agree not to assist any government investigation" ← **RED**
- "Confidentiality obligations apply to all financial information" with no government
  carve-out ← **YELLOW: May impede**
- Non-disparagement clause with no government agency carve-out ← **YELLOW**

**Required Safe Harbor Language** [JURISDICTION-SPECIFIC US]:

```
Nothing in this agreement prohibits you from reporting possible violations of law or
regulation to any governmental agency or entity, including the SEC, CFTC, NLRB, or
OSHA, or from making other disclosures that are protected under whistleblower provisions
of applicable law. You do not need prior authorization to make any such report or
disclosure, and you are not required to notify the company that you have made such a
report or disclosure.
```

[JURISDICTION-SPECIFIC FR — Loi Waserman]:

- Any clause preventing disclosure to external authorities (AFA, Défenseur des droits,
  judicial authorities) is unenforceable
- Anonymous reporting cannot be waived by contractual clause
- Criminal liability for identity revelation applies even to contractually bound employees

**⟁ CLARIFY** — Agreement audit scope:

- Which agreement types should be reviewed? (All standard templates / specific agreements
  / pending agreements before signing)
- Are there legacy agreements (pre-2011 for SOX; pre-2010 for Dodd-Frank) that should
  be retroactively assessed?
- Is this triggered by an SEC inquiry, routine audit, or M&A due diligence?

---

### Step 11: Run Quality Verification

Before delivering program design, audit findings, or recommendations, run the complete
quality assurance framework (see Quality Assurance section).

**Completeness Check**:

- [ ] All six program domains assessed
- [ ] All active jurisdictions mapped in Regulatory Obligation Matrix
- [ ] All CLARIFY points answered or documented as assumed defaults
- [ ] Glass Box audit trail populated
- [ ] All legal citations marked VERIFIED or [VERIFY]
- [ ] Anti-retaliation burden-of-proof analysis completed for each active jurisdiction
- [ ] Employment agreement audit complete if operating mode requires it

---

### Step 12: Deliver Output

Deliver the output following the Output Format Template (see final section). Append the
Glass Box audit trail to every output.

---

## Four-Jurisdiction Statutory Framework

### EU Whistleblower Directive 2019/1937

**Full citation**: Directive (EU) 2019/1937 of the European Parliament and of the Council
of 23 October 2019 on the protection of persons who report breaches of Union law

**Key Articles**:

- Art. 4 — Qualifying whistleblowers (workers, contractors, trainees, volunteers,
  shareholders, facilitators, associated persons)
- Art. 7 — Internal reporting channels (50+ employees)
- Art. 8 — Obligations for legal entities in private sector (50+ employees)
- Art. 9 — Procedures for internal reporting and follow-up
- Art. 10 — External reporting to competent authorities
- Art. 16 — Confidentiality obligations (identity protection mandatory)
- Art. 19 — Prohibited retaliation (broad list including damage to reputation, blacklisting,
  psychiatric referral, negative performance assessment)
- Art. 21 — Measures of support (legal aid access for whistleblowers)
- Art. 23 — Penalties for retaliation and for hindering reporting

**Transposition status (as of 2025)**: All Member States have transposed, but Commission
July 2024 report identified persistent deficiencies in Poland, Hungary, Italy, Bulgaria.
Infringement procedures possible. [VERIFY current status for specific Member States]

**Organizations with 50-249 employees**: Extended transposition deadline to December 2023;
may share internal reporting channel resources but must maintain compliance individually.

---

### US Sarbanes-Oxley Section 806

**Full citation**: 18 U.S.C. § 1514A (Sarbanes-Oxley Act of 2002, §806); implementing
regulations at 29 C.F.R. Part 1980

**Scope**: Employees of publicly traded companies, including subsidiaries, contractors,
subcontractors, agents

**Protected activities**: Reports of mail/wire/bank/securities fraud; violations of SEC
rules; violations of federal law relating to fraud against shareholders

**Filing requirement**: Complainant must file retaliation complaint with OSHA within
**180 days** of retaliatory action

**Enforcement**: DOL/OSHA (Whistleblower Protection Program); right to de novo review in
federal district court if OSHA does not act within 180 days of filing

**Remedies**: Reinstatement, back pay (with interest), compensation for litigation costs,
special damages

**Audit Committee obligation (SOX §301)**: Must establish procedures for receiving,
retaining, and treating complaints; must include confidential and anonymous submission
mechanisms for employees regarding accounting, internal controls, or auditing matters

---

### US Dodd-Frank Section 922

**Full citation**: 15 U.S.C. § 78u-6 (Securities Exchange Act §21F); SEC Rules 21F-1
through 21F-17 (17 C.F.R. §§ 240.21F-1 to 240.21F-17)

**Scope**: All entities subject to SEC jurisdiction; employees, contractors,
subcontractors, agents; non-US nationals protected if violation affects US securities
markets

**Protected activities**: Reports to SEC of reasonable belief of federal securities law
violations; participation in SEC investigation or judicial/administrative proceeding

**Safe harbor**: Rule 21F-17(a) — No person may take action to impede an individual
from communicating directly with the SEC; no confidentiality agreement may restrict such
communications; no waivers of right to report to SEC permitted

**Award program**: 10-30% of sanctions exceeding $1 million; complete anonymity available
if reporting through counsel; record FY 2024 tips (45,130) and awards ($255 million)

**Critical 2024 enforcement**: J.P. Morgan Chase ($18M) — settlement agreements impeded
SEC reporting; September 2024 seven-company enforcement ($3M+ combined); Two Sigma
Investments (January 2025). Pattern: agreement language impeding government reporting
continues to be primary enforcement target.

**Remedies for retaliation**: Reinstatement; double back pay plus interest; attorney's
fees; expert witness fees; available in federal district court

---

### France Sapin II / Loi Waserman

**Citations**:

- Loi Sapin 2: Loi n° 2016-1691 du 9 décembre 2016 relative à la transparence, à la lutte
  contre la corruption et à la modernisation de la vie économique
- Loi Waserman: LOI n° 2022-401 du 21 mars 2022 visant à améliorer la protection des
  lanceurs d'alerte (implemented EU Directive 2019/1937)

**Thresholds**: 50+ employees (Waserman, since September 2022); previous Sapin II threshold
of 500+ employees replaced

**Key Waserman innovations**:

- Removed mandatory internal-before-external hierarchy: reporters may go directly to
  external authorities (AFA, Défenseur des droits, judicial authorities) without internal
  escalation
- Extended protection to facilitators and associated persons
- Explicit anonymous reporting support required
- Increased criminal penalties for obstruction and identity revelation

**Article 8 (reporting obligation)**: Organizations with 50+ employees must maintain
documented whistleblowing systems integrated into internal compliance framework;
designated receiving officer or service required

**Penalties**:

- Administrative (AFA Sanctions Commission): up to €1,000,000 for legal entities; up to
  €200,000 for natural persons failing to maintain Article 8 procedures
- Criminal: up to €15,000 and 1 year imprisonment for obstructing reports; up to €30,000
  and 2 years imprisonment for revealing whistleblower identity
- Corruption penalties: up to €5,000,000 or double the derived benefit

---

### UK Public Interest Disclosure Act 1998 (PIDA)

**Citation**: Public Interest Disclosure Act 1998 (c.23), inserting Part IVA into
Employment Rights Act 1996 (ERA 1996) as amended; Worker Protection (Amendment of
Equality Act 2010) Act 2023 (effective October 2024)

**Scope**: All workers (employees, contractors, agency workers, trainees, volunteers);
no size threshold; all sectors; universal application

**Three elements of protected disclosure** (all required):

1. **Qualifying disclosure**: Information the worker reasonably believes shows one of six
   categories of wrongdoing
2. **Reasonable belief**: Worker need not be correct; reasonable but mistaken belief
   is protected
3. **Public interest**: Worker reasonably believes disclosure is in the public interest
   (added by Enterprise and Regulatory Reform Act 2013)

**Six categories of qualifying wrongdoing** (ERA 1996 s.43B):

1. Criminal offence
2. Failure to comply with a legal obligation
3. Miscarriage of justice
4. Danger to health and safety of any individual
5. Damage to the environment
6. Deliberate concealment of information about any of the above

**Disclosure hierarchy**:

- **s.43C** — Internal: to employer (protected automatically)
- **s.43F** — External: to prescribed regulators (protected automatically if reasonable
  belief substantially true)
- **s.43G/43H** — Public: highly restricted conditions; good faith and public interest
  both required; previous internal/external reports attempted or objectively pointless

**Day-one rights**: Protection applies from first day of engagement; no minimum service
requirement

**Unlimited compensation**: No statutory cap; tribunal may award compensation for
loss of earnings, future loss, and injury to feelings

**2024 developments**: Sullivan v Isle of Wight Council (EAT Feb 2024) — external
applicants (non-NHS) cannot bring detriment claims against prospective employers;
"collective memory" doctrine — organization can be liable even if individual decision-
maker lacked personal knowledge of protected disclosure

---

## Program Component Framework

Assess or design the program against these six core domains. Each domain should be rated
COMPLIANT / PARTIAL / NON-COMPLIANT.

### Domain 1 — Governance and Oversight

**Minimum requirements**:

- Written whistleblower policy approved by board or audit committee
- Designated receiving officer or function (Compliance, GC, Internal Audit, or
  third-party ombudsperson) — must be independent from operational management
- Direct audit committee access for escalated matters [JURISDICTION-SPECIFIC US — SOX §301]
- Annual board review of program effectiveness
- CCO or equivalent has authority to investigate without business unit interference

**COMPLIANT**: Written policy; designated officer; board oversight; documented escalation
path; CCO independence established

**PARTIAL**: Policy exists but outdated; officer designated but lacks independence; no
documented board oversight

**NON-COMPLIANT**: No written policy; no designated officer; no board oversight; reporting
function embedded in operational management with no independent path

---

### Domain 2 — Reporting Channels

**Minimum requirements**:

- At least one internal channel operational and accessible (mandatory: EU, SOX, Sapin II)
- External channel guidance documented and communicated to workers
- Channel supports anonymous reports where required (SOX, EU per MS implementation,
  Waserman)
- Accessible in applicable language(s) of workforce
- Multiple modalities offered (phone, web, in-person option, email)
- Third-party provider used or equivalent independence demonstrated

**COMPLIANT**: Multiple channels; anonymous capability; multi-language; accessible to all
worker categories; third-party provider or equivalent

**PARTIAL**: Single channel; no anonymous option; single language only; only employees
covered (contractors excluded in breach of EU/US/FR requirements)

**NON-COMPLIANT**: No dedicated channel; only manager escalation path; known reports
suppressed or discouraged

---

### Domain 3 — Intake Triage and Routing

**Minimum requirements**:

- Acknowledgment within 7 days (mandatory: EU, FR; best practice: US, UK)
- Documented triage procedure classifying allegation type and urgency
- Routing to independent handler (not respondent's management chain)
- Regulatory deadline mapping triggered on receipt
- Substantive feedback to reporter within 3 months (mandatory: EU, FR; best practice
  US, UK)
- Records maintained securely, separate from personnel files

**COMPLIANT**: Written triage procedure; 7-day acknowledgment; 3-month feedback; secure
records; independent routing; regulatory deadline tracking

**PARTIAL**: Acknowledgment inconsistent; no triage procedure; routing through management
(potential conflict); no feedback cycle

**NON-COMPLIANT**: No acknowledgment; no triage; reports routed to respondent's chain;
no records; no follow-up to reporter

---

### Domain 4 — Confidentiality and Identity Protection

**Minimum requirements**:

- Identity accessible only to personnel necessary for investigation
- Anonymous reports accepted and handled with equal rigor
- Documented confidentiality procedures with access controls
- Reporter informed before identity disclosed (except where disclosure would jeopardize
  investigation) [EU Art. 16 / FR Waserman]
- Written explanation provided if identity must be disclosed
- Employment agreements contain no prohibited impediment language [JURISDICTION-SPECIFIC
  US — Dodd-Frank Rule 21F-17]

**COMPLIANT**: Strict access controls; documented procedures; anonymous handling equal to
identified; no prohibited agreement language; written disclosure notification process

**PARTIAL**: Confidentiality intended but undocumented; identity disclosed without
notification; some agreements contain impediment language

**NON-COMPLIANT**: Reporter identity disclosed without justification; identity used to
facilitate retaliation; active use of NDA / confidentiality agreements to prevent
external reporting

---

### Domain 5 — Anti-Retaliation

**Minimum requirements**:

- Written anti-retaliation policy defining prohibited conduct with reference to
  applicable statutes
- Interim protective measures procedure (pre-finding protection during investigation)
- Legal review required before adverse employment action affecting known reporters
- Training for managers and HR on prohibited retaliation (annual)
- Documented monitoring: track whether adverse actions follow protected disclosures
- Remediation for confirmed retaliation: reinstatement, back pay, and appropriate
  discipline of retaliating manager

**COMPLIANT**: Written policy; interim measures; legal review gate for adverse actions;
manager training; monitoring; documented response to confirmed retaliation

**PARTIAL**: Policy exists but not enforced; no interim measures; adverse actions not
reviewed; no training

**NON-COMPLIANT**: No policy; known retaliatory actions against reporters; use of
agreements to suppress reporting (Rule 21F-17 exposure)

---

### Domain 6 — Investigation Protocol

**Minimum requirements**:

- Written investigation procedures covering scope, timeline, and documentation standards
- Investigator conflict screening process
- Privilege election decision at investigation opening
- Standard investigation timeline by complexity tier
- Findings documented as: Substantiated / Partially Substantiated / Unsubstantiated
- Remediation triggered on substantiated findings
- Cross-referencing with `legalcode-investigation-plan-builder` for full execution

**COMPLIANT**: Written procedures; conflict screening; privilege decision; findings
documented; remediation tracked; board escalation path documented

**PARTIAL**: Informal procedures only; no conflict screening; inconsistent documentation

**NON-COMPLIANT**: No procedures; investigations conducted by conflicted parties;
no documentation; findings not acted upon

---

## Investigation Complexity Tiers

Classify every incoming report into one of four tiers at intake:

| Tier            | Characteristics                                                                                                              | Investigator                                           | Counsel                                  | Timeline                                          |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------- | ------------------------------------------------- |
| **PRELIMINARY** | Anonymous tip; vague allegation; no identifiable respondent; low credibility indicators                                      | HR or CCO designee                                     | Optional                                 | 1-2 weeks (fact-gathering; may close or escalate) |
| **STANDARD**    | Named reporter; identifiable respondent; workplace-level allegation; no regulatory filing; no executive respondent           | Compliance officer + HR                                | Recommended                              | 4-8 weeks                                         |
| **COMPLEX**     | Multiple allegations; executive or board respondent; parallel regulatory inquiry; financial materiality; privilege-sensitive | CCO + outside employment counsel                       | Required                                 | 8-16 weeks                                        |
| **CRISIS**      | Active government investigation; criminal allegations; material financial or reputational risk; board-level respondent       | Outside counsel lead; board committee direct oversight | Required; GC and board directly involved | Variable (paced by regulatory timeline)           |

**Automatic CRISIS triggers** — Escalate immediately regardless of initial assessment:

- Receipt of government subpoena, CID, or investigative demand referencing the
  disclosed subject matter
- Allegation that CEO, CFO, General Counsel, or board member is a respondent
- Allegation involving financial statement fraud, material misstatement, or insider
  trading
- Whistleblower reports receiving or anticipating press inquiry
- Retaliation incident occurs during open investigation

---

## Protected Activity Catalogue

Document the scope of protected activities per jurisdiction for use in triage and policy:

### United States (SOX §806 + Dodd-Frank §922)

**Protected activities include**:

- Reporting mail fraud, wire fraud, bank fraud, or securities fraud to any federal agency
  or supervisor
- Reporting violations of SEC rules and regulations
- Reporting violations of federal laws relating to fraud against shareholders
- Providing information to the SEC about possible securities law violations (Dodd-Frank)
- Initiating, testifying in, or otherwise participating in SEC proceedings
- Reporting to CFTC (commodity-related violations)
- Internal reporting to a supervisor, compliance officer, or audit committee

**NOT protected** (common misconceptions):

- Reports about labor law violations unrelated to securities fraud (different statute)
- Reports made in bad faith or solely for personal gain
- Reports that do not meet the "reasonable belief" standard

### EU Directive 2019/1937

**Protected breach categories**:

- Public procurement violations
- Financial services, banking, insurance regulations
- Anti-money laundering and counter-terrorism financing
- Product safety and compliance
- Transport safety
- Environmental protection
- Nuclear safety
- Food and feed safety, animal health and welfare
- Public health
- Consumer protection
- Privacy, data protection, and network/information security
- Competition and state aid rules
- Corporate tax violations

**Protected persons**: Workers, contractors, trainees, volunteers, shareholders,
self-employed, directors, persons in supply chain, facilitators, associated persons

### France (Sapin II / Loi Waserman)

**Protected disclosures**:

- Crimes or misdemeanors (délits ou crimes)
- Violations of international obligations (treaties, conventions)
- Unilateral acts of international organizations
- Laws and regulations
- Threats or serious harm to general interest (public health, environment, democratic
  institutions, financial security of state)
- Good faith reasonable belief standard applies; motive irrelevant

### UK PIDA 1998

**Six categories** (ERA 1996 s.43B) — see Statutory Framework section above

---

## Regulatory Deadline Matrix

Map the critical deadlines that a report may trigger:

| Jurisdiction    | Deadline                               | Trigger                                    | Consequence of Miss                   |
| --------------- | -------------------------------------- | ------------------------------------------ | ------------------------------------- |
| EU (Directive)  | 7 days                                 | Receipt of report                          | Non-compliance; Art. 23 penalties     |
| EU (Directive)  | 3 months                               | Acknowledgment of report                   | Non-compliance; Art. 23 penalties     |
| US (SOX §806)   | 180 days                               | Retaliatory action against reporter        | OSHA claim time-barred                |
| US (Dodd-Frank) | No hard deadline                       | Ongoing — Rule 21F-17 applies continuously | Enforcement risk continuous           |
| FR (Waserman)   | 7 days (best practice aligned with EU) | Receipt of report                          | Regulatory scrutiny                   |
| FR (Waserman)   | 3 months (best practice)               | Acknowledgment                             | Regulatory scrutiny                   |
| UK (PIDA)       | 3 months (tribunal claim)              | Detriment or dismissal                     | Tribunal claim time-barred for worker |
| UK (PIDA)       | No acknowledgment requirement          | Receipt of report                          | Best practice only                    |

**Additional regulatory triggers** (jurisdiction-specific):

[JURISDICTION-SPECIFIC US] OSHA investigation notification to respondent: within 10 days
of receiving complaint; employer has 20 days to respond with position statement

[JURISDICTION-SPECIFIC EU] National competent authority acknowledgment: Art. 11 requires
authorities to acknowledge within 7 days and provide feedback within 3 months of receipt

[JURISDICTION-SPECIFIC FR] AFA referral: No mandatory timeline but AFA may initiate
own-motion investigation of Sapin II compliance; cooperation expected

---

## Severity Classification

### Domain-Level Severity (Program Assessment)

| Rating            | Definition                                             | Action Required                                            |
| ----------------- | ------------------------------------------------------ | ---------------------------------------------------------- |
| **COMPLIANT**     | Fully meets all applicable requirements                | Maintain; continue periodic review                         |
| **PARTIAL**       | Partially meets requirements; specific identified gaps | Remediation plan required; timeline for completion         |
| **NON-COMPLIANT** | Fails to meet requirements; regulatory exposure exists | Immediate remediation; legal counsel; notify CCO and board |

### Finding-Level Severity (Employment Agreement Audit / Clause Review)

| Rating                | Definition                                                        | Example                                                                                |
| --------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **RED — Prohibited**  | Language directly violates a statutory prohibition                | NDA preventing SEC reporting; agreement requiring waiver of right to government report |
| **YELLOW — Risk**     | Language creates impediment risk or may chill protected reporting | Non-disparagement without government carve-out; overbroad confidentiality              |
| **GREEN — Compliant** | Contains required safe harbor language or is otherwise compliant  | Explicit government agency carve-out; written anti-retaliation statement               |

---

## Prioritization Framework

Prioritize program gaps and recommendations in three tiers:

### Tier 1 — Must Remediate (Regulatory Exposure)

- Internal reporting channel does not exist (EU, SOX, Sapin II statutory requirement)
- No confidentiality protection for reporter identity (EU, FR mandatory; US best practice)
- Employment agreements contain prohibited impediment language (Dodd-Frank Rule 21F-17)
- No anti-retaliation policy (all jurisdictions)
- Retaliation has occurred against a known reporter (active regulatory and litigation risk)
- No audit committee oversight procedure (SOX §301 mandatory for public companies)
- Anonymous reporting not supported where required (SOX §301 mandatory)

### Tier 2 — Should Remediate (Compliance Gap)

- Acknowledgment not within 7 days (EU/FR mandatory; US/UK gap creates credibility risk)
- No independent third-party channel (reliance on manager escalation only)
- Investigation procedures undocumented
- Manager training on anti-retaliation absent or more than 24 months old
- No complexity tier classification at intake
- Board receives no regular program reporting
- Anonymous reports handled differently than identified reports

### Tier 3 — Should Consider (Best Practice)

- Third-party ombudsperson engaged for additional independence
- Program metrics dashboard maintained and reviewed monthly
- Multi-language materials (required for EU/FR if multilingual workforce)
- Reporter feedback more frequent than 3-month statutory minimum
- Cross-reference with `legalcode-investigation-plan-builder` for full investigation
  procedure standardization
- Annual external audit of program effectiveness
- Sector-specific prescribed regulator list maintained and communicated

---

## Quality Assurance Framework

### Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                         | Fail Action                                              |
| -------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every statutory obligation cites specific article, section, or regulation    | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow consistent, recognizable format for the jurisdiction    | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments, repeal, or regulatory update   | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within program's governing law scope; no jurisdictional bleed | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden                                    | Add confidence qualifier                                 |

### Self-Interrogation for NON-COMPLIANT Domains

For any domain rated NON-COMPLIANT, apply this three-pass review before finalizing:

**Pass 1 — Legal Chain Integrity**: Does the non-compliance finding follow logically from
the cited statutory authority? Would a regulator or enforcement authority actually reach
this conclusion? Counter-arguments?

**Pass 2 — Completeness**: Have all relevant statutes, regulations, regulatory guidance,
and safe harbor provisions been considered? Is the most current version of the statute
applied? Are there transitional provisions or phase-in timelines that soften the finding?

**Pass 3 — Challenge**: What is the strongest argument that the current practice is
compliant or defensible? Under what circumstances would a regulator exercise enforcement
discretion? Is the finding proportionate?

Mark outcome: `self_interrogation: PASS` (finding confirmed) or `self_interrogation: REVISED`
(finding adjusted with explanation).

### Confidence Scoring

| Level        | Range     | Meaning                                                       | Action                                                |
| ------------ | --------- | ------------------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled statutory text; no ambiguity                          | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong statutory authority; minor interpretation questions    | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments; reasonable interpretations differ             | State with reasoning and contra-indicators            |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing authorities or interpretations | Flag for counsel review with both sides presented     |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                                       | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Append this YAML block to every output. Complete all fields.

```yaml
glass_box:
  skill_name: "legalcode-whistleblower-program-builder"
  engagement_date: "[YYYY-MM-DD]"
  operating_mode: "[Build New / Audit / Channel Design / Agreement Review / Board Readiness]"
  organization_profile:
    employee_count: "[number or range]"
    sector: "[sector]"
    organization_type: "[public / private / non-profit / public authority]"
  jurisdictions_in_scope: "[EU / US-SOX / US-Dodd-Frank / FR / UK / other]"
  regulatory_drivers:
    eu_directive: "[applicable / not applicable / unknown]"
    sox_806: "[applicable / not applicable / unknown]"
    dodd_frank_922: "[applicable / not applicable / unknown]"
    sapin_waserman: "[applicable / not applicable / unknown]"
    pida_uk: "[applicable / not applicable / unknown]"
  domains_assessed:
    governance: "[COMPLIANT / PARTIAL / NON-COMPLIANT / NOT ASSESSED]"
    reporting_channels: "[COMPLIANT / PARTIAL / NON-COMPLIANT / NOT ASSESSED]"
    intake_triage: "[COMPLIANT / PARTIAL / NON-COMPLIANT / NOT ASSESSED]"
    confidentiality: "[COMPLIANT / PARTIAL / NON-COMPLIANT / NOT ASSESSED]"
    anti_retaliation: "[COMPLIANT / PARTIAL / NON-COMPLIANT / NOT ASSESSED]"
    investigation_protocol: "[COMPLIANT / PARTIAL / NON-COMPLIANT / NOT ASSESSED]"
  tier1_gaps_identified: "[number] — [brief list]"
  agreement_audit_performed: "[yes / no / partial]"
  prohibited_language_found: "[yes / no / N/A]"
  legalcode_mcp: "[Connected / Not connected]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "[PASS / REVISED / NOT APPLICABLE (no NON-COMPLIANT domains)]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified legal and employment counsel review"
```

---

## Anti-Patterns

What NOT to do when designing, auditing, or operating a whistleblower program:

### Governance Anti-Patterns

1. **Reporting to GC without board path**: CCO or whistleblower function reports only to
   General Counsel, with no independent path to audit committee. GC may be conflicted in
   matters involving legal liability.

2. **Policy not reviewed by board**: Written policy approved by HR or management only.
   SOX §301 and DOJ ECCP expect board or audit committee ownership; regulatory examiners
   will look for board approval.

3. **No written escalation procedure**: Escalation to board/audit committee is ad hoc and
   undocumented. When a crisis arises, absence of documented procedure suggests program
   exists on paper only.

4. **Compliance officer lacks authority to investigate executives**: Program effectively
   covers only non-management employees; senior management investigations routed through
   HR controlled by respondent's colleagues. Independent path to board or external counsel
   is essential.

5. **No program effectiveness review**: Program last reviewed at implementation.
   DOJ ECCP 2024 "works in practice" assessment question specifically targets programs
   that are documented but not functioning. Annual review is minimum standard.

### Channel Design Anti-Patterns

6. **Anonymous reporting disabled**: Anonymity disabled because of "cultural fit" or
   investigation difficulty concerns. SOX §301 explicitly requires anonymous submission
   capability. EU Directive requires equal treatment of anonymous reports if accepted.
   Disabling anonymity chills reporting and may breach statutory requirements.

7. **Manager-only escalation path**: Internal channel routes reports through the reporter's
   direct management chain. Guarantees suppression of reports about immediate superiors.
   Independent routing is fundamental.

8. **Single-channel program**: Only one intake method (e.g., phone hotline only). Reduces
   accessibility. EU Directive Art. 9 requires accessible procedures; multiple modalities
   are best practice across all jurisdictions.

9. **No external channel guidance**: Organization provides internal channel but does not
   communicate the existence or contact information for external regulators (SEC, AFA,
   FCA, etc.). Workers have a right to external reporting — withholding this information
   may constitute obstruction.

10. **Channel not accessible to contractors**: Internal channel (and program materials)
    available only to employees. EU Directive, Dodd-Frank, PIDA, and Waserman all cover
    contractors, subcontractors, and agents. Excluding them creates statutory compliance
    gaps.

### Confidentiality and Identity Anti-Patterns

11. **Identity disclosed without notification**: Reporter's identity shared with
    investigation team or management without notifying the reporter and obtaining
    justification. Violates EU Art. 16; triggers Waserman criminal liability risk;
    destroys program credibility.

12. **Report routed directly to respondent's HR business partner**: HRBP for the
    respondent's business unit receives the complaint. Structural conflict; creates
    retaliation risk even without intent.

13. **Confidentiality agreements restrict government reporting**: NDA, separation
    agreement, or consulting agreement contains language preventing disclosure to SEC,
    OSHA, AFA, or other regulators. Violates Dodd-Frank Rule 21F-17 (enforcement risk
    in 2024-2025); unenforceable under Waserman. $18M JP Morgan Chase penalty (2024).

14. **Anonymous reports treated with lower priority**: Organization investigates identified
    reports promptly but places anonymous reports on a slow track or closes them without
    investigation for "insufficient information." Equal treatment obligation under EU Art. 9
    and Waserman; chills anonymous reporting.

15. **Investigation details shared with respondent's colleagues before findings**: Sharing
    allegation details with respondent's manager or colleagues before investigation
    completes. Creates retaliation risk and may constitute prohibited adverse action.

### Anti-Retaliation Anti-Patterns

16. **Automatic suspension of reporter during investigation**: Reporter suspended
    "pending investigation" of their own complaint. Creates presumption of retaliation
    under burden-of-proof frameworks; exactly what interim protective measures are
    designed to prevent.

17. **Adverse employment action taken before investigation completes**: Reporter denied
    promotion, given poor performance review, or demoted while investigation is open.
    Under SOX contributing-factor standard, proximity in time is sufficient to survive
    summary judgment. Requires independent business justification documented before action.

18. **No legal review gate for actions affecting reporters**: HR can proceed with adverse
    employment actions for known reporters without legal sign-off. Eliminates the key
    control that prevents inadvertent retaliation.

19. **Manager training skipped or more than two years old**: Managers lack knowledge of
    what constitutes retaliation; retaliatory acts occur through ignorance, not malice.
    Annual training on prohibited actions is minimum standard.

20. **Retaliating manager remains in place after substantiated retaliation**: Post-
    investigation, retaliating manager receives no discipline. Sends organizational
    message that retaliation is tolerated; DOJ ECCP requires incentive and discipline
    alignment with compliance objectives.

### Intake and Triage Anti-Patterns

21. **No urgency classification at intake**: All reports treated with equal priority
    regardless of severity. Securities fraud and health/safety emergencies lose critical
    response time. CRISIS-tier triggers must be acted upon immediately.

22. **Regulatory deadline not tracked from receipt**: 7-day acknowledgment (EU/FR
    mandatory), 180-day OSHA filing window (US SOX), and 3-month feedback obligation
    (EU/FR mandatory) are not tracked. Deadline management failure converts a substantive
    compliance failure into a procedural one as well.

23. **Report closed as vague without triage**: Anonymous or vague reports closed
    immediately as "insufficient information" without basic triage. Many actionable
    allegations begin as vague tips. Triage requires minimum documented assessment
    before close.

24. **No record of reports received**: Organization has no log of reports, dates, triage
    decisions, or outcomes. In a regulatory examination, absence of records creates
    inference that program does not operate in practice.

### Investigation Anti-Patterns

25. **Investigator conflict not screened**: Investigation assigned to HR business partner
    who supports the respondent's department, or to a colleague with a social relationship
    with the respondent. Conflict of interest invalidates investigation integrity.

26. **Privilege election not documented**: Investigation begins without determining whether
    it is attorney-directed (privilege-protected) or HR-directed (discoverable). Post-hoc
    privilege claims are difficult to sustain; decision must be made at outset.

27. **Upjohn warning omitted in US investigations**: US corporate employee interviewed
    without Upjohn warning. Employee may believe they are represented by company's counsel;
    subsequent use of their statements may create legal complications and ethical issues.
    [JURISDICTION-SPECIFIC US]

28. **Findings not documented in writing**: Investigation concludes with verbal
    communications only. "Substantiated / Partially Substantiated / Unsubstantiated"
    finding must be written, dated, and retained. Without documentation, remediation
    cannot be tracked and regulatory defense is impossible.

29. **Remediation not connected to findings**: Substantiated findings produce no
    disciplinary action or corrective measures. DOJ ECCP explicitly requires discipline
    proportional to misconduct; inconsistent or absent discipline is a program failure
    indicator.

### Program Design Anti-Patterns

30. **Single jurisdiction design applied globally**: Program designed for US requirements
    only, deployed globally. EU Directive, PIDA, and Waserman impose different and in
    some respects stricter requirements (7-day acknowledgment, identity protection
    procedures, no mandatory internal-before-external hierarchy). One-size program
    without jurisdiction adaptation creates non-compliance in EU, FR, and UK.

31. **No board reporting on program metrics**: Board receives annual policy confirmation
    but no metrics. Cannot assess whether program is functioning. DOJ ECCP "adequately
    resourced and empowered to function effectively" standard requires demonstrable
    board engagement.

32. **Program not accessible in workforce languages**: Program materials, reporting channel
    instructions, and anti-retaliation policy available only in English for a multi-lingual
    workforce. EU Art. 9 requires accessible procedures; French Waserman compliance may
    require French-language materials.

---

## Writing Standards

Apply these standards to all program deliverables, policies, and communications:

**For Program Policies and Procedures**:

- Write in plain language accessible to all employees, not legal terminology
- Use active voice: "Submit your report to..." not "Reports should be submitted to..."
- Short sentences; one instruction per sentence
- Define terms at first use; avoid undefined acronyms
- Numbered steps for procedural instructions
- Headers and sub-headers for navigation

**For Board and Audit Committee Reports**:

- Lead with the key finding and its regulatory or business consequence
- Use tables for program metrics; narrative for significant findings
- Quantify where possible: number of reports, time-to-acknowledgment statistics,
  substantiation rates
- Flag Tier 1 gaps explicitly and separately from Tier 2/3 gaps
- Include a "no action required" confirmation if applicable

**Quality Gates Before Delivery**:

1. Non-specialist employee can understand the policy without legal interpretation
2. Every regulatory requirement cited includes the specific provision (not just
   "applicable law")
3. Every legal claim backed by citation or flagged [VERIFY]
4. No conditional or hedging language used where statutory text is clear
5. Sentences are as short as possible without losing meaning
6. Glass Box audit trail appended and complete

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool
and cross-references two related skills for handoff.

**With legalcode-mcp connected (preferred)**:

- Search for current transposition status of EU Directive 2019/1937 in specific Member
  States (transposition quality varies; July 2024 Commission report identifies deficiencies)
- Verify current enforcement actions and penalty levels by jurisdiction
- Research sector-specific whistleblower regimes (FCA, NRC, EPA, CFTC) beyond the four
  primary frameworks
- Search for recent OSHA whistleblower program statistics and case outcomes
- Verify current Waserman implementing guidance from AFA (Agence française anticorruption)
- Mark legalcode-mcp sourced citations as VERIFIED in Glass Box

**Without legalcode-mcp**:

- Proceed with statutory framework research from training data
- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Focus on structural program design and framework completeness rather than
  current-state enforcement developments

**Cross-skill handoffs**:

- **`legalcode-investigation-plan-builder`**: When a specific report has been triaged and
  an investigation must be planned. Provides full 12-step investigation planning workflow,
  complaint type taxonomy, complexity tiers, interview guide templates, and privilege
  framework.
- **`legalcode-compliance-program-builder`**: When integrating the whistleblower program
  into a broader compliance program structure. Provides governance design, risk assessment,
  training curriculum, and third-party due diligence frameworks.

---

## Output Format Template

Every engagement produces output following this structure (adapt sections to operating mode):

```markdown
# Whistleblower Program [Assessment / Design / Agreement Review] Report

**Organization**: [name or description]
**Date**: [YYYY-MM-DD]
**Engagement Mode**: [Build New / Audit / Channel Design / Agreement Review / Board Readiness]
**Jurisdictions in Scope**: [list]
**Prepared by**: Legalcode Whistleblower Program Builder (AI-assisted — qualified counsel
review required)

---

## Executive Summary

[2-4 sentence overview: what was assessed, the headline finding, and the primary recommended
action. Suitable for board/audit committee briefing.]

---

## Regulatory Obligation Matrix

[Table from Step 3 — active obligations per jurisdiction]

---

## Program Domain Assessment

| Domain                     | Rating                            | Key Gaps  | Priority |
| -------------------------- | --------------------------------- | --------- | -------- |
| Governance & Oversight     | [COMPLIANT/PARTIAL/NON-COMPLIANT] | [top gap] | [Tier]   |
| Reporting Channels         | …                                 | …         | …        |
| Intake Triage & Routing    | …                                 | …         | …        |
| Confidentiality & Identity | …                                 | …         | …        |
| Anti-Retaliation           | …                                 | …         | …        |
| Investigation Protocol     | …                                 | …         | …        |

**Overall Program Maturity**: [EFFECTIVE / ADEQUATE / DEVELOPING / INADEQUATE]
[One-sentence rationale]

---

## Tier 1 Gaps — Immediate Remediation Required

[For each Tier 1 gap:]

### [Gap Name]

**Domain**: [Domain 1-6]
**Jurisdictions implicated**: [list]
**Statutory basis**: [specific provision]
**Finding**: [description of gap]
**Regulatory exposure**: [consequence if not remediated]
**Confidence**: [Definite / High / Probable / Possible / Unlikely]
**Recommended action**: [specific, actionable step]
**Suggested timeline**: [immediate / 30 days / 90 days]

---

## Tier 2 Gaps — Remediation Recommended

[Summary table: Gap | Domain | Jurisdiction | Recommended Action | Timeline]

---

## Tier 3 — Best Practice Enhancements

[Bulleted list of optional improvements with brief rationale]

---

## Employment Agreement Audit (if applicable)

| Agreement Type | Finding   | Severity         | Required Change                 |
| -------------- | --------- | ---------------- | ------------------------------- |
| [type]         | [summary] | RED/YELLOW/GREEN | [specific language or deletion] |

---

## Remediation Roadmap

| Action   | Owner            | Deadline | Dependencies   |
| -------- | ---------------- | -------- | -------------- |
| [action] | CCO / HR / Legal | [date]   | [prerequisite] |

---

## Next Steps

- [ ] [Specific action 1 — owner — deadline]
- [ ] [Specific action 2 — owner — deadline]
- [ ] [Legal counsel review of this report before distribution]

---

[Glass Box Audit Trail — YAML block]
```

---

## Localization Notes

When adapting this skill for a specific jurisdiction or Member State implementation:

**EU Member States**: EU Directive 2019/1937 sets the minimum floor; Member State
implementations vary. Germany (HinSchG 2023), France (Waserman), Netherlands (Wet
bescherming klokkenluiders) each have specific nuances. Review national transposition
for: (a) whether anonymous reporting is mandatory or optional; (b) competent authority
designation; (c) penalty levels for non-compliance; (d) any stricter worker protections
beyond Directive minimum. [VERIFY against current national legislation before use]

**US sector-specific overlays**: FCA-regulated institutions (OFR), nuclear industry (NRC),
environmental violations (EPA), transportation (DOT), commodity derivatives (CFTC),
consumer finance (CFPB) all have sector-specific whistleblower programs. Layer these on
top of SOX/Dodd-Frank for regulated entities. [VERIFY applicable programs with sector counsel]

**UK financial services**: FCA SYSC 18 Whistleblowing Rules apply to banks, building
societies, credit unions, and insurers with annual revenue >£250M and/or assets >£50B.
Requirements beyond PIDA: designated whistleblowers' champion; annual report to board;
FCA-specific protected disclosure guidance. [VERIFY current FCA SYSC 18 application thresholds]

**Australia** (outside primary scope but common request): Fair Work Act 2009 (general
protections); Corporations Act 2001 Part 9.4AAA (public companies and large proprietary
companies); Treasury Laws Amendment (Enhancing Whistleblower Protections) Act 2019.
Reverse onus on employer to disprove retaliation. ASIC external reporting channel.

**Non-English language requirements**: France (French required for workforce materials);
Germany (German required for HinSchG compliance procedures); multilingual EU workforce
(accessible procedures in workers' languages — EU Directive Art. 9). Translation of
program materials into local language(s) is recommended for all EU Member State
deployments.

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis from primary statutory research
across four jurisdictions: EU Directive 2019/1937 (full text analysis), US SOX §806 and
Dodd-Frank §922 (statutory text, 29 C.F.R. Part 1980, SEC Rules 21F-1 through 21F-17,
SEC FY 2024 Annual Report to Congress), France Sapin II / Loi Waserman (LOI n° 2016-1691;
LOI n° 2022-401), UK PIDA 1998 (ERA 1996 Part IVA, 2024 EAT case law). Quality frameworks,
Glass Box audit trail structure, Citation Quality Gates, Self-Interrogation, and Confidence
Scoring adapted from `legalcode-contract-review` (benchmark standard). Program domain
framework and maturity model adapted from `legalcode-compliance-program-builder`. For
investigation planning cross-reference, see `legalcode-investigation-plan-builder`. 2024
enforcement benchmarks: J.P. Morgan Chase $18M SEC penalty; Two Sigma Investments (January
2025); EU Commission July 2024 implementation deficiency report. Research conducted via
multi-agent pipeline with parallel structural and legal framework analysis.
