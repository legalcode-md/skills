---
name: legalcode-us-whistleblower-program-builder
description: Builds US federal whistleblower reporting and investigation programs covering SOX Section
  806 employee protections (18 U.S.C. § 1514A; 29 C.F.R. Part 1980), SOX Section 301 audit committee complaint
  procedures (15 U.S.C. § 78j-1(m)(4)), Dodd-Frank Section 922 SEC Whistleblower Program (15 U.S.C. §
  78u-6; Rules 21F-1 through 21F-17), CFTC Whistleblower Program (7 U.S.C. § 26), OSHA's 25+ whistleblower
  protection statutes, False Claims Act qui tam (31 U.S.C. § 3730), Anti-Money Laundering Act of 2020
  FinCEN whistleblower (31 U.S.C. § 5323), and IRS whistleblower awards (26 U.S.C. § 7623).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Builds US federal whistleblower reporting and investigation programs covering SOX Section 806 employee protections (18 U.S.C. § 1514A; 29 C.F.R. Part 1980), SOX Section 301 audit committee complaint procedures (15 U.S.C. § 78j-1(m)(4)), Dodd-Frank Section 922 SEC Whistleblower Program (15 U.S.C. § 78u-6; Rules 21F-1 through 21F-17), CFTC Whistleblower Program (7 U.S.C. § 26), OSHA's 25+ whistleblower protection statutes, False Claims Act qui tam (31 U.S.C. § 3730), Anti-Money Laundering Act of 2020 FinCEN whistleblower (31 U.S.C. § 5323), and IRS whistleblower awards (26 U.S.C. § 7623). Covers hotline and intake channel architecture, Rule 21F-17 anti-impediment employment agreement audit, anti-retaliation controls and burden-of-proof analysis (SOX contributing-factor standard; Dodd-Frank heightened standard; Digital Realty Trust v. Somers, 583 U.S. 149 (2018)), Upjohn warning protocols, investigation privilege structure, litigation hold triggers, audit committee reporting lines under NYSE Rule 303A.07 and Nasdaq Rule 5605(c)(3), SEC Rule 10D-1 clawback integration, DOJ ECCP September 2024 adequacy criteria, documentation discipline, SEC examination readiness, and remediation workflows. Use when building a new US whistleblower program from scratch, auditing an existing program for SOX/Dodd-Frank/OSHA compliance gaps, reviewing employment and separation agreements for Rule 21F-17 prohibited provisions, preparing a board or audit committee whistleblower governance assessment, evaluating SEC Whistleblower Office award eligibility, responding to OSHA Whistleblower Protection Program investigations, or integrating whistleblower obligations into a post-acquisition compliance remediation. Jurisdiction: United States federal law.


# Legalcode US Whistleblower Program Builder

> **Disclaimer**: This skill provides a framework for AI-assisted design and assessment of
> whistleblower programs under United States federal law. It does not constitute legal advice.
> All outputs must be reviewed by qualified legal counsel admitted to practice in the United
> States before use or implementation. The statutory, regulatory, and case law landscape
> described here — including SEC enforcement guidance, DOJ policy, OSHA procedures, and
> judicial interpretations — evolves continuously. Citations from training data carry
> hallucination risk; verify all statutory references, penalty amounts, award statistics,
> and case citations against authoritative sources (SEC.gov, DOL.gov, DOJ.gov, US Courts)
> before relying on them. Whistleblower program design involves complex employment law,
> investigative procedure, securities regulation, and regulatory compliance obligations
> that require experienced securities, employment, and compliance counsel.

---

## Purpose and Scope

This skill designs, audits, and optimizes whistleblower programs for organizations subject
to US federal whistleblower statutes. It covers the full program lifecycle — from channel
architecture through intake triage, investigation structuring, anti-retaliation controls,
regulatory deadline management, and board governance — with depth on the SEC and DOJ
compliance standards that determine enforcement exposure.

**Covers:**

- Multi-statute regulatory mapping: SOX §806/§301, Dodd-Frank §922, CFTC §748, OSHA
  (25+ statutes), False Claims Act, AML Act of 2020, IRS §7623
- SEC Whistleblower Office award eligibility analysis (Rule 21F-4 through 21F-16)
- Rule 21F-17 anti-impediment employment agreement audit with specific prohibited clauses
- Anti-retaliation framework: SOX contributing-factor standard; Dodd-Frank heightened
  standard; _Digital Realty Trust v. Somers_ (2018) external-report requirement
- SOX Section 301 audit committee governance (NYSE Rule 303A.07; Nasdaq Rule 5605(c)(3))
- Upjohn warning script and investigation privilege election framework
- Litigation hold trigger analysis for whistleblower complaints
- DOJ ECCP (September 2024) adequacy criteria for whistleblower channels
- SEC Rule 10D-1 clawback policy integration
- SEC examination readiness: documentation standards, access controls, metrics
- Program domain assessment: COMPLIANT / PARTIAL / NON-COMPLIANT classification
- Glass Box audit trail for regulatory examination and board reporting

**Does not:**

- Design programs for EU Directive 2019/1937, UK PIDA, or France Sapin II/Waserman
  (see `legalcode-whistleblower-program-builder` for the multi-jurisdiction version)
- Conduct live investigations (see `legalcode-investigation-plan-builder`)
- Provide legal advice or substitute for qualified US securities, employment, or
  regulatory counsel
- Guarantee SEC/DOJ enforcement outcomes or award eligibility determinations

**Related skills:**

- `legalcode-whistleblower-program-builder` — multi-jurisdiction framework (EU/US/FR/UK)
- `legalcode-investigation-plan-builder` — full investigation planning workflow for
  specific complaints post-triage
- `legalcode-sox-compliance-assessment` — SOX Section 302/404 ICFR compliance; this
  skill covers SOX §806/§301 whistleblower obligations specifically
- `legalcode-workplace-investigation` — HR investigation mechanics and documentation
- `legalcode-compliance-program-builder` — holistic corporate compliance program design

---

## Jurisdiction and Governing Law

**Primary jurisdiction**: United States federal law. State whistleblower protections
(including California Labor Code § 1102.5, New York Labor Law § 740, and equivalents)
are out of scope but should be assessed by employment counsel in parallel.

### Core Statutory Framework

| Statute                | Citation                                         | Key Obligation                                        | Enforcer                      |
| ---------------------- | ------------------------------------------------ | ----------------------------------------------------- | ----------------------------- |
| SOX Section 806        | 18 U.S.C. § 1514A; 29 C.F.R. Part 1980           | Anti-retaliation for securities-fraud reports         | DOL/OSHA; federal courts      |
| SOX Section 301        | 15 U.S.C. § 78j-1(m)(4)                          | Audit committee complaint procedures                  | SEC (Exchange Act)            |
| Dodd-Frank Section 922 | 15 U.S.C. § 78u-6; 17 C.F.R. §§ 240.21F-1 to -17 | SEC award program; anti-impediment                    | SEC Division of Enforcement   |
| CFTC Whistleblower     | 7 U.S.C. § 26; 17 C.F.R. Part 165                | CFTC award program; anti-retaliation                  | CFTC                          |
| False Claims Act       | 31 U.S.C. §§ 3730–3733                           | Qui tam; anti-retaliation for FCA reporters           | DOJ; federal courts           |
| AML Act of 2020        | 31 U.S.C. § 5323                                 | FinCEN award program; anti-retaliation                | FinCEN/DOJ                    |
| IRS Whistleblower      | 26 U.S.C. § 7623                                 | IRS award (15-30% collected proceeds >$2M)            | IRS Whistleblower Office      |
| DOJ Corporate WB Pilot | DOJ Criminal Division (August 2024)              | Criminal misconduct award up to $50M; forfeiture >$1M | DOJ Criminal Division (MLARS) |
| OSH Act Section 11(c)  | 29 U.S.C. § 660(c)                               | Workplace safety reporting anti-retaliation           | OSHA                          |

**OSHA Whistleblower Protection Program administers 25+ federal statutes** including:

- Sarbanes-Oxley Act (SOX §806) — 180-day filing deadline [VERIFY]
- Consumer Financial Protection Act (CFPA) — 180 days [VERIFY]
- Food Safety Modernization Act (FSMA) — 180 days [VERIFY]
- Affordable Care Act (ACA) — 180 days [VERIFY]
- Surface Transportation Assistance Act (STAA) — 180 days [VERIFY]
- Clean Air Act — 30 days [VERIFY]
- Safe Drinking Water Act (SDWA) — 30 days [VERIFY]
- Toxic Substances Control Act (TSCA) — 30 days [VERIFY]
- Energy Reorganization Act (NRC matters) — 180 days [VERIFY]
- _See OSHA's current statute list at dol.gov/agencies/osha/workers/whistleblower for
  complete deadlines — deadlines vary by statute and must be verified against current
  regulatory text._

**Enforcement authorities**:

- **SEC Division of Enforcement** — Dodd-Frank Rule 21F enforcement; Rule 21F-17
  anti-impediment enforcement; SOX §301 audit committee requirements
- **DOL/OSHA Whistleblower Protection Program** — SOX §806; 25+ other statutes;
  civil enforcement; referral to federal courts
- **DOJ Criminal Division** — 18 U.S.C. § 1513 (retaliating against informants/witnesses);
  SOX §1107 (retaliating against informants in federal proceedings); FCA civil/criminal
- **IRS Whistleblower Office** — 26 U.S.C. § 7623 award administration
- **CFTC** — Section 748 award program and anti-retaliation rule
- **Federal courts** — SOX §806 de novo review; Dodd-Frank §922 private right of action;
  FCA qui tam proceedings; 18 U.S.C. § 1513 criminal prosecution

**Key case law** [all citations carry hallucination risk — verify independently]:

- _Digital Realty Trust, Inc. v. Somers_, 583 U.S. 149 (2018) — SEC report required
  for Dodd-Frank §922(h) anti-retaliation protection; internal-only disclosure does not
  qualify; SOX §806 provides separate protection for internal reports [VERIFY]
- _Lawson v. FMR LLC_, 571 U.S. 429 (2014) — SOX §806 protects employees of contractors
  and subcontractors of public companies [VERIFY]
- _Murray v. UBS Securities, LLC_, 601 U.S. \_\_\_ (Feb. 8, 2024) — unanimous 9-0 decision
  (Sotomayor, J.): SOX §806 does not require complainant to prove retaliatory intent;
  contributing-factor standard governs; temporal proximity alone can suffice
  circumstantially; resolves Second/Fifth/Ninth Circuit split [VERIFY citation format]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
organizational context, the workflow pauses and asks when:

- The answer materially changes the regulatory obligations that apply
- The organization's compliance maturity level affects the remediation roadmap
- Risk tolerance or business context is needed to calibrate severity classifications
- Multiple program design approaches exist with different trade-offs

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

- **New build**: Organization description + regulatory drivers + employee profile +
  exchange listing status
- **Audit request**: Existing program documentation, policies, hotline contracts, or
  description of current-state program
- **Agreement review**: Employment, separation, consulting, NDA, or settlement agreements
  for Rule 21F-17 prohibited impediment language
- **OSHA response**: Receipt of OSHA complaint under SOX §806 or other OSHA-administered
  statute requiring investigation and response
- **SEC inquiry**: SEC request for information about whistleblower program; OIG/internal
  audit finding; M&A whistleblower due diligence
- **Board readiness**: Audit committee governance assessment + investment case for program
  upgrade

If insufficient context is provided, proceed immediately to Step 2.

---

### Step 2: Gather Context

**⟁ CLARIFY** — Ask these questions before proceeding. Skip any the user has already answered.

**1. Operating mode** — What should this engagement produce?

- **Build new program** — Full program design, policies, procedures, governance,
  rollout roadmap, and implementation checklist
- **Audit existing program** — Gap assessment against SOX/Dodd-Frank/OSHA/DOJ ECCP
  requirements
- **Rule 21F-17 agreement review** — Employment/separation/NDA audit for prohibited
  provisions
- **OSHA response** — Responding to an active OSHA Whistleblower Protection Program
  investigation
- **Board readiness** — Audit committee governance assessment and metrics reporting
- **Award analysis** — Evaluating SEC/CFTC/FCA/IRS award eligibility for a potential
  whistleblower
- _Why this matters_: Each mode produces different outputs and activates different workflow
  sections.

**2. Organization profile** — Provide these details:

- **Exchange listing**: NYSE, Nasdaq, OTC, OTCQB, other, or private?
  - _Why this matters_: Exchange listing triggers SOX §301 audit committee obligations and
    NYSE/Nasdaq listing standard requirements. Private companies are not subject to SOX
    §806 unless they are subsidiaries/contractors of public companies.
- **SEC/CFTC registration**: Registered investment adviser, broker-dealer, swap dealer,
  other regulated entity?
- **Employee count**: Total US; total globally; contractor headcount?
- **Industry sector**: Financial services, healthcare, defense, government contracting,
  manufacturing, technology, other?
  - _Why this matters_: Defense/government contractors face FCA qui tam risk; financial
    services face CFTC exposure; healthcare faces FCA/ACA whistleblower overlap.

**3. Current program state** (for audits):

- Written whistleblower policy: yes / partial (outdated) / no
- Dedicated reporting channel operational: third-party hotline / internal email / manager
  escalation only / none
- Anonymous reporting supported: yes / no
- Last program review or external audit date?
- Any active or recent OSHA complaints, SEC inquiries, or known retaliation incidents?
- _Why this matters_: Determines whether to build from scratch or remediate specific gaps.

**4. Agreement audit scope** (for Rule 21F-17 reviews):

- Which agreement types: all templates / specific categories / pending agreements only?
- Volume: estimate of agreements in scope
- Triggered by: routine audit / SEC inquiry / specific employee complaint / M&A diligence?
- _Why this matters_: Determines depth and sampling approach; SEC inquiry context requires
  more aggressive remediation posture.

---

### Step 3: Map Regulatory Obligations

Based on Step 2 context, map the active US federal whistleblower obligations. Produce a
**US Regulatory Obligation Matrix**:

| Obligation                          | SOX §806                                       | SOX §301              | Dodd-Frank §922               | CFTC §748             | OSHA Programs                   | False Claims Act                      |
| ----------------------------------- | ---------------------------------------------- | --------------------- | ----------------------------- | --------------------- | ------------------------------- | ------------------------------------- |
| Trigger                             | Public co. + contractors                       | Exchange-listed       | SEC-regulated entities        | CFTC-regulated        | Statute-specific                | Gov't contractors                     |
| Internal channel required           | No (but recommended)                           | Yes (audit committee) | No (external optional)        | No                    | No                              | No                                    |
| Anonymous reporting                 | No (but SOX §301 requires for audit committee) | **Yes — mandatory**   | Yes (through counsel)         | Yes                   | No                              | No (but relator identity protected)   |
| Anti-retaliation                    | §1514A — contributing factor                   | N/A (procedural)      | Rule 21F-2 — heightened       | Rule 165.20           | Statute-specific                | 31 U.S.C. § 3730(h)                   |
| Award program                       | No                                             | No                    | 10-30% >$1M sanctions         | 10-30% >$1M sanctions | No                              | 15-30% of recovery                    |
| Filing deadline (retaliation claim) | 180 days to OSHA                               | N/A                   | No OSHA filing; federal court | 180 days to CFTC      | 30-180 days (varies by statute) | 3 years after discovery; 10 years max |

**Applicability determination**:

- **SOX §806 applies** if: (a) organization is a publicly traded company registered under
  Exchange Act §12 or filing under §15(d); OR (b) organization is a subsidiary, contractor,
  or agent of such a company (per _Lawson v. FMR_) [VERIFY]
- **SOX §301 applies** if: organization is an Exchange Act reporting company with a listed
  class of securities subject to audit committee requirements (NYSE/Nasdaq rules overlay)
- **Dodd-Frank §922 applies** if: entity is subject to SEC jurisdiction (registered issuers,
  broker-dealers, investment advisers, etc.)
- **CFTC §748 applies** if: entity is a registered futures commission merchant, swap dealer,
  major swap participant, or other CFTC-regulated entity
- **False Claims Act** applies if: entity contracts with or receives funding from US government
- **OSHA programs** apply by specific statute; analyze which statutes cover the organization's
  activities

---

### Step 4: Assess Current Program (Audit Mode)

For audit or optimization engagements, assess the current program against eight core
domains (see Program Domain Framework). Rate each domain:

- **COMPLIANT** — Meets or exceeds all applicable requirements
- **PARTIAL** — Partially meets requirements; specific gaps identified with remediation
  priority
- **NON-COMPLIANT** — Fails to meet requirements; regulatory exposure quantified
- **NOT ASSESSED** — Insufficient information; identify information needed

Apply Self-Interrogation (see Quality Assurance) to any domain rated NON-COMPLIANT before
finalizing.

**⟁ CLARIFY** — For any domain rated PARTIAL or NON-COMPLIANT, ask:

- Is there a remediation plan? If yes, current status and deadline?
- Has there been a regulatory inquiry, OSHA complaint, or SEC request in this area?
- What is the organization's risk tolerance for this gap (low / medium / high)?

---

### Step 5: Design or Audit Reporting Channels

Design or assess the **channel architecture** covering:

#### Internal Channel Requirements

**SOX §301** mandates that audit committees of Exchange Act reporting companies establish
procedures for:

1. **Receipt, retention, and treatment** of complaints regarding accounting, internal
   controls, and auditing matters
2. **Confidential, anonymous submission** by employees of concerns about questionable
   accounting or auditing matters

**Best practice architecture** (aligned with DOJ ECCP September 2024):

- **Third-party hotline provider** (e.g., NAVEX/EthicsPoint, Lighthouse, Convercent):
  independent intake; anonymous capability; 24/7 access; multiple languages
- **Secure web portal**: allows structured intake with optional anonymity
- **Dedicated email address** to Compliance or GC office (not manager escalation)
- **Written reporting procedure**: published in employee handbook, intranet, and onboarding
- **All worker categories covered**: employees, contractors, agents — per _Lawson v. FMR_

**Channel independence requirements**:

- Intake must route to a function independent of the reporter's management chain
- Audit committee must have direct access to reports involving accounting/controls matters
  (SOX §301) — not filtered through GC or CFO
- CCO should have authority to escalate directly to audit committee without GC approval

#### External Channel Guidance

Document and communicate external reporting options to all workers:

- **SEC Office of the Whistleblower**: sec.gov/whistleblower (securities violations; Form
  TCR online; anonymous submission available through counsel)
- **CFTC Whistleblower Office**: whistleblower.cftc.gov (commodity-related violations)
- **OSHA Whistleblower Protection Program**: dol.gov/agencies/osha/workers/whistleblower
  (retaliation complaints; SOX §806 complaints filed here)
- **DOJ**: justice.gov (fraud, FCA matters)
- **IRS Whistleblower Office**: irs.gov/compliance/whistleblower (tax violations >$2M)
- **FinCEN**: Financial Crimes Enforcement Network (AML Act of 2020 reporter program)
- **Sector-specific**: NRC (nuclear), EPA (environmental), FERC (energy), FRB, OCC, FDIC,
  CFPB (financial services)

**Critical Rule 21F-17 requirement**: The organization may not take any action, through
any agreement, policy, or practice, to impede communication with the SEC. Informing workers
of external reporting options is affirmatively required as part of Rule 21F-17 compliance.

**⟁ CLARIFY** — Channel architecture decisions:

- Should the organization engage a third-party hotline provider or build an internal system?
- Is anonymous reporting currently supported for audit committee matters (SOX §301 mandatory)?
- Are reporting channel instructions included in employment agreements or handbooks?

---

### Step 6: Draft Intake Triage and Routing Procedures

Design the **intake triage procedure** applied to every incoming report:

**Mandatory steps for every report**:

1. **Receive and date-stamp**: Triggers regulatory deadline tracking from receipt
2. **Assign case reference**: Coded reference system minimizes identity exposure in
   records
3. **Classify allegation type** (see Protected Activity Catalogue)
4. **Assign Complexity Tier** (see Investigation Complexity Tiers)
5. **Route** to appropriate handler per routing matrix (below)
6. **Acknowledge receipt**: Within 7 days (best practice; EU/FR mandatory if applicable;
   US has no statutory deadline but DOJ ECCP values prompt acknowledgment)
7. **Map regulatory deadlines**: 180-day OSHA clock (SOX §806); any mandatory reporting
   obligations triggered; litigation hold evaluation

**Routing Matrix**

| Allegation Type                            | Primary Route                       | Escalation Trigger                        | Privilege?                               |
| ------------------------------------------ | ----------------------------------- | ----------------------------------------- | ---------------------------------------- |
| Securities fraud / accounting irregularity | Audit Committee + outside counsel   | Immediate                                 | Attorney-directed recommended            |
| Insider trading                            | GC + Compliance + outside counsel   | Immediate; trading halt consideration     | Attorney-directed required               |
| Anti-bribery / FCPA                        | CCO + outside counsel               | Board if executive involved; VSD analysis | Attorney-directed recommended            |
| Financial statement fraud                  | Audit Committee (CFO conflicted)    | Immediate + outside counsel               | Attorney-directed required               |
| Government contract fraud (FCA)            | GC + outside counsel                | Immediate; VSD analysis                   | Attorney-directed required               |
| Workplace safety / OSHA                    | Safety Officer + Compliance         | Immediate if imminent danger              | HR-directed acceptable                   |
| HR / workplace harassment                  | HR + Compliance                     | Outside counsel if executive respondent   | HR-directed; document privilege election |
| Retaliation against a reporter             | Audit Committee / Board             | Outside counsel immediately               | Attorney-directed required               |
| AML / financial crimes                     | CCO + BSA Officer + outside counsel | SAR obligations may arise independently   | Attorney-directed recommended            |
| Environmental violations                   | Regulatory Affairs + GC             | Mandatory reporting if applicable         | Attorney-directed recommended            |

**Confidentiality Protocol at Intake**:

- Reporter identity accessible **only to designated personnel** — not operational management
  unless investigation requires
- Anonymous reports handled with equal rigor to identified reports
- Separate investigation file from HR/personnel records
- Written record of any authorized identity disclosure with justification
- Legal hold evaluation triggered on receipt of any allegation involving potential litigation
  or regulatory proceeding (anticipation-of-litigation standard applies from earliest
  reasonable anticipation)

---

### Step 7: Structure the Investigation Protocol

Design the **investigation framework** for reports post-triage. For full investigation
execution, cross-reference `legalcode-investigation-plan-builder`.

#### Privilege Election (US-Specific)

The most consequential decision in any US internal investigation is made at the outset:

**Attorney-directed investigation (privilege-protected)**:

- Outside or in-house counsel directs the investigation
- All communications made for the purpose of giving legal advice
- Work product doctrine protects investigation memoranda
- Selective waiver risks: disclosing to government may waive privilege broadly [VERIFY
  circuit-specific law on selective waiver]
- Upjohn warnings required for employee interviews (see below)

**HR-directed investigation (not privilege-protected)**:

- Appropriate for lower-complexity workplace matters
- Investigation file potentially discoverable in litigation
- More appropriate where transparency to employees is important
- Document privilege election decision at investigation opening regardless of choice

**Document privilege election**: Create a written record at investigation opening stating:

- Who is directing the investigation and in what capacity
- Whether the investigation is attorney-directed for purposes of legal advice
- Who has authorized the investigation
- Scope of investigation

#### Upjohn Warnings (US-Required for Corporate Investigations)

Deliver Upjohn warnings at the opening of every interview of a corporate employee in an
attorney-directed investigation. Use this script (adapt as needed; have counsel review):

```
Before we begin, I need to explain a few things. I am [name], and I represent
[Company Name], not you individually. The company has asked me to investigate
[general subject matter]. The purpose of this interview is to gather information
to assist the company in obtaining legal advice.

This conversation is protected by the attorney-client privilege — but that privilege
belongs to the company, not to you personally. The company may decide, in its sole
discretion, to disclose the contents of this interview to third parties, including
government agencies, without your consent and over your objection.

You are not required to speak with me. However, if you choose not to cooperate
with the company's investigation, that refusal itself may have employment
consequences. Do you understand what I have explained? Do you have any questions?
```

Document compliance: Date, time, interviewer name, interviewee name, and written
confirmation that the warning was delivered. Have the employee sign a written
acknowledgment at the conclusion confirming receipt and understanding of the warning.
Document the exact warning language given and the employee's acknowledgment verbatim
in interview notes. If the investigation may place the employee at personal legal risk
(e.g., potential criminal exposure, SEC/DOJ referral), proactively advise the employee
to seek personal counsel before proceeding with the interview — failure to do so risks
suppression of statements and adverse Sixth Amendment implications in parallel criminal
proceedings.

#### Investigator Independence Requirements

Screen for conflicts before assigning every investigation:

| Conflict Category      | Disqualifying Relationship                                                |
| ---------------------- | ------------------------------------------------------------------------- |
| Reporting relationship | Investigator is in respondent's reporting chain (any level)               |
| HR partnership         | HR business partner who supports respondent's business unit               |
| Social/personal        | Close personal relationship with respondent or complainant                |
| Business interest      | Financial interest in outcome (compensation tied to respondent's results) |
| Prior involvement      | Previously advised on or approved the subject conduct                     |

If all internal personnel are conflicted, engage outside counsel to lead.

#### Litigation Hold Trigger Analysis

A litigation hold obligation arises when the organization has **reasonable anticipation**
of litigation or regulatory proceeding — which in the whistleblower context arises when:

- A complaint is received that contains specific, credible allegations of legal violations
- An OSHA complaint is filed under SOX §806 or other statute
- An SEC/CFTC/DOJ inquiry references the alleged conduct
- A reporter's attorney sends a preservation demand letter
- Adverse employment action has been taken against a known reporter

On trigger: issue written legal hold immediately (within 24-72 hours); suspend normal
document retention schedules for all in-scope custodians; document issuance with
timestamp and recipient list.

**Personal devices and personal messaging applications** are now in scope: SEC Enforcement
Manual updates (2026) direct staff to request preservation of communications on personal
devices and personal messaging applications (WhatsApp, Signal, iMessage) used for business.
Legal holds must affirmatively reach personal devices — a hold limited to corporate systems
is insufficient where employees regularly use personal channels for business. [VERIFY
current SEC Enforcement Manual section reference]

**Retention periods for investigation files**: 7 years minimum (SOX floor); 10 years
for matters with government inquiry involvement; up to limitations period + buffer for
securities fraud matters (10-year maximum under 28 U.S.C. § 1658 for some claims). [VERIFY]

---

### Step 8: Design Anti-Retaliation Framework

The anti-retaliation framework is the most legally sensitive element of any US whistleblower
program. Design it in four layers.

#### Layer 1 — Prohibited Conduct Definition

Define explicitly prohibited retaliatory actions under each applicable statute:

**All Applicable Statutes**: Discharge, demotion, suspension, threats, harassment,
reassignment, discrimination in compensation or terms of employment, exclusion from
professional activities.

**SOX §806 specific** (18 U.S.C. § 1514A): Any adverse employment action affecting the
terms and conditions of employment. Includes constructive discharge. Covers:

- Employees of publicly traded companies
- Employees of subsidiaries, contractors, subcontractors, agents (_Lawson v. FMR_)

**Dodd-Frank Rule 21F-2 specific**: Broader than SOX — applies to all who report to SEC
regardless of employer type. Also covers actions that impede future reporting. Note:
per _Digital Realty Trust v. Somers_ (2018), Dodd-Frank anti-retaliation protection
requires an actual report to the SEC — internal-only disclosure does not qualify.
SOX §806 separately protects internal reports to supervisors or regulatory bodies.

**18 U.S.C. § 1513** (federal criminal retaliation): Retaliating against an informant
or witness in a federal proceeding. DOJ Criminal Division enforcement.

**31 U.S.C. § 3730(h)** (False Claims Act): Protects any action in furtherance of an
FCA claim, including internal investigations and disclosures to supervisors.

#### Layer 2 — Burden-of-Proof Analysis

Understanding the burden framework determines how organizations must document any
employment action involving a known or suspected whistleblower:

| Statute                       | Initial Burden (Employee)                                                           | Burden Shift              | Employer's Standard                                                                                                                           |
| ----------------------------- | ----------------------------------------------------------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **SOX §806**                  | Protected activity + adverse action + contributing factor                           | Burden shifts to employer | Clear and convincing evidence of same action without the protected activity (_Murray v. UBS_ (2024): no retaliatory intent required) [VERIFY] |
| **Dodd-Frank §922**           | Protected activity (SEC report required per _Digital Realty_) + adverse action      | Burden shifts to employer | Clear and convincing non-retaliatory reason (heightened standard vs. SOX)                                                                     |
| **False Claims Act §3730(h)** | Protected activity + adverse action + causal connection                             | After prima facie showing | Employer must show legitimate, non-retaliatory reason; burden then shifts back                                                                |
| **OSHA statutes**             | Protected activity + adverse action + nexus (contributing factor for most statutes) | Burden shifts             | Clear and convincing evidence action would have been taken absent protected activity                                                          |

**Practical implication**: Any adverse employment action within a temporal window following
a protected disclosure must be:

1. Documented with an independent business justification pre-dating the complaint
2. Reviewed by employment counsel before execution
3. Approved by a decision-maker who was not aware of the protected disclosure, if possible

**Legal review gate**: Implement a process requiring legal sign-off before any adverse
employment action affecting a known or suspected whistleblower.

#### Layer 3 — Interim Protective Measures During Investigation

- Do **NOT** automatically suspend, place on leave, or transfer the reporter
  (creates contributing-factor presumption)
- If separation of reporter and respondent is necessary, move the respondent where possible
- Provide written assurance to reporter that their employment status is unaffected by
  their report (without prejudging the investigation)
- If reporter faces ongoing risk from continued proximity to respondent, treat as CRISIS
  tier and escalate
- Document all protective measure decisions with rationale

#### Layer 4 — Post-Retaliation Remediation (Confirmed Cases)

When investigation substantiates retaliation:

1. Reinstatement or equivalent relief for the reporter
2. Back pay calculation (SOX §806: back pay with interest; Dodd-Frank: double back pay)
3. Discipline of retaliating manager proportional to severity (DOJ ECCP requires
   "disciplinary procedures" to be "consistent and fairly applied")
4. Root cause analysis: Was this an individual failure or systemic gap?
5. Notify OSHA if SOX §806 complaint is pending — demonstrate remediation in response
6. Legal hold on all documents related to the retaliation incident

---

### Step 9: Conduct Rule 21F-17 Employment Agreement Audit

Audit all standard employment agreements, separation agreements, consulting agreements,
NDAs, arbitration agreements, and settlement agreements for Rule 21F-17 prohibited
provisions.

#### Prohibited Language Patterns (RED — Requires Immediate Remediation)

| Prohibited Pattern                                                                                | Why Prohibited                                                | Enforcement Example                                                                      |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| "You agree not to disclose company information to any third party, including regulatory agencies" | Directly impedes SEC/OSHA/CFTC reporting                      | J.P. Morgan Securities ($18M, Jan 17 2024): passive-only carve-out insufficient [VERIFY] |
| "You release all claims and agree not to assist any government investigation"                     | Waives right to government cooperation                        | Multiple SEC enforcement actions 2024 [VERIFY]                                           |
| "Confidentiality obligations apply to all financial and operational information" (no carve-out)   | Potential to impede securities violation reporting            | SEC 2024 enforcement wave [VERIFY]                                                       |
| "All disputes must be reported internally before engaging any external party"                     | Mandatory pre-reporting requirement prohibited by Rule 21F-17 | Rule 21F-17(a) explicit prohibition                                                      |
| Non-disparagement clause with no government agency carve-out                                      | Chills SEC/DOJ cooperation                                    | Two Sigma Investments enforcement (Jan 2025) [VERIFY]                                    |
| "You agree to keep this settlement confidential from all parties" (no government exception)       | May impede testimony in SEC proceedings                       | SEC enforcement guidance 2024                                                            |
| "By accepting this separation package, you waive any claim under securities laws"                 | Cannot waive right to SEC report; award cannot be waived      | Rule 21F-17(a); 15 U.S.C. § 78u-6(h)(1)(A)(i)                                            |

#### YELLOW — Risk Language (Review and Remediate)

- Non-disparagement with no explicit government agency carve-out
- Broad confidentiality covering "all company matters" without carve-out for regulatory
  disclosures
- Arbitration clause that could be read to cover whistleblower retaliation claims
- Internal escalation requirements not accompanied by notice of right to go directly
  to SEC
- Trade secret provisions that could chill disclosure of evidence of securities fraud

#### Required Safe Harbor Language (GREEN — Insert in All Agreements)

```
Nothing in this agreement prohibits you from reporting possible violations of
law or regulation to any governmental agency or entity, including the Securities
and Exchange Commission, Commodity Futures Trading Commission, Department of
Labor, Department of Justice, National Labor Relations Board, or any other
federal, state, or local governmental agency or authority, or from making other
disclosures that are protected under the whistleblower provisions of applicable
law. You do not need the company's prior authorization to make any such report
or disclosure, and you are not required to notify the company that you have
done so. You may not waive your right to receive an award for information
provided to a government agency.
```

**Additional required disclosure** (Rule 21F-17): New employees should receive a
written description of the SEC Whistleblower Program at or near hiring, explaining:

- Right to report directly to SEC without internal escalation
- SEC award program availability
- Anti-retaliation protections

**⟁ CLARIFY** — Agreement audit priorities:

- Are there legacy agreements (pre-2011, before Dodd-Frank) that should also be reviewed?
- Has the organization received any SEC inquiry related to agreement language?
- Should remediated agreements be distributed proactively to all current employees?

---

### Step 10: Build SEC Whistleblower Award Analysis (If Applicable)

For engagements where a specific individual may be considering SEC or CFTC whistleblower
reporting, or where the organization is assessing the likelihood that current or former
employees may pursue awards:

#### SEC Award Eligibility Framework (Rule 21F-4 through 21F-16)

**Required elements for award eligibility**:

1. **Original information**: Independent knowledge or analysis not already known to SEC
   and not derived solely from public sources
2. **Voluntary submission**: Not compelled by subpoena, judicial order, or contractual
   obligation
3. **Reasonable belief**: Reasonably believes information relates to possible violation
   of federal securities laws
4. **>$1M sanctions**: SEC action or related action resulting in sanctions exceeding
   $1 million
5. **Award range**: 10-30% of collected monetary sanctions (17 C.F.R. § 240.21F-16)

**Internal reporting credit** (Rule 21F-4(b)(7)): An individual who reports internally
first may still be treated as a whistleblower for award purposes if the SEC receives
the information within 120 days of the internal report **AND** the company discloses
to the SEC. [VERIFY current rule text]

**Award-increasing factors** (Rule 21F-16):

- Significance of information to enforcement
- Degree of assistance provided throughout proceeding
- Law enforcement interest in effective enforcement
- Whether reporter acted promptly
- Whether reporter reported internally first

**Award-decreasing factors** (Rule 21F-16):

- Unreasonable delay in reporting
- Interference with internal compliance systems
- Culpability in the underlying violation
- False information provided

**Anonymous submission**: Available if reporting through counsel; attorney must certify
whistleblower status at award collection

**FY2024 statistics** [VERIFY]: Per SEC Office of the Whistleblower FY2024 Annual Report
to Congress (November 2024): approximately 24,980 tips received (record high); 47
individual award recipients; total awards exceeding $255 million; cumulative program
awards over $2.2 billion to 444 individuals since 2011. Largest single FY2024 award:
~$98 million (split two whistleblowers). [VERIFY against current SEC Annual Report]

#### CFTC Award Program (7 U.S.C. § 26; 17 C.F.R. Part 165)

- Same 10-30% of sanctions >$1M structure as SEC program
- Covers commodity futures, derivatives, and spot market violations
- Anti-retaliation rule (CFTC Rule 165.19; 7 U.S.C. § 26(h)) covers all employees;
  2-3 year statute of limitations for retaliation claims; direct federal court access [VERIFY]
- **FY2024 statistics** [VERIFY]: 1,744 tips received (record high); 12 award orders;
  15 recipients; approximately $42 million in awards; cumulative ~$390-395 million to
  53 recipients since 2014. Notable: first-ever compliance officer award ($1.25 million);
  digital assets/crypto award. [VERIFY against CFTC FY2024 Annual Report]
- **Eligibility note**: Ineligibility for award does not preclude anti-retaliation
  protection — Rule 165.19 coverage is broader than award eligibility

#### False Claims Act Qui Tam (31 U.S.C. § 3730)

- **Qui tam**: Private relator files under seal on behalf of US government
- **Award**: 15-25% if government intervenes; 25-30% if relator proceeds alone
- **Protected activity**: Any act in furtherance of an FCA claim, including investigation
  and disclosure to supervisor
- **Filing deadline**: 6 years after violation or 3 years after government knows/should
  know; not more than 10 years
- **Jurisdictional requirement**: Government must have funds at issue

#### IRS Whistleblower (26 U.S.C. § 7623)

- **Threshold**: Tax underpayment >$2 million; individual taxpayer income >$200K
- **Award**: 15-30% of collected proceeds (including penalties and interest)
- **Waiting period**: Significant delays common (3-10+ years); award paid after collection

#### DOJ Corporate Whistleblower Awards Pilot Program (August 1, 2024)

A three-year Criminal Division pilot program administered by the Money Laundering and
Asset Recovery Section (MLARS):

- **Award trigger**: Net proceeds of forfeiture exceeding **$1 million**
- **Award ceiling**: Up to **$50 million** per case
- **Focused gap areas** (not covered by SEC/CFTC/IRS programs):
  1. Financial institution crimes
  2. Foreign corruption not covered by FCPA whistleblowers
  3. Domestic public corruption
  4. Health care fraud against private insurers (outside False Claims Act scope)
- **Eligibility**: Original, truthful information about corporate criminal misconduct
  not already known to DOJ
- **Interaction with 120-day VSD window**: DOJ Corporate Enforcement Policy (CEP, August 2024) creates a 120-day self-disclosure window tied to internal whistleblower reports —
  organizations that receive internal reports and voluntarily disclose to DOJ within 120
  days of the internal report (before DOJ contact) may qualify for a presumption of
  declination. Organizations that retaliate against whistleblowers lose CEP credit and
  face separate criminal referrals. [VERIFY current CEP text — August 2024 version]
- **Program operates alongside** (not instead of) SEC, CFTC, IRS, and FCA programs —
  assess overlap and sequence of submissions with counsel

---

### Step 11: Design Governance and Audit Committee Reporting

Build the **governance architecture** for ongoing program oversight.

#### SOX Section 301 Audit Committee Requirements (Exchange-Listed Companies)

SOX §301 (15 U.S.C. § 78j-1(m)(4)) requires audit committees to establish procedures for:

1. **Receipt, retention, and treatment** of complaints regarding accounting, internal
   controls, or auditing matters
2. **Confidential, anonymous submission** by employees of concerns about questionable
   accounting or auditing matters

**NYSE Rule 303A.07** (Listed Company Manual): Audit committee must have written charter
specifying procedures for receiving, retaining, and treating complaints. [VERIFY current
rule text]

**Nasdaq Rule 5605(c)(3)**: Audit committee must have procedures for handling such
complaints. [VERIFY current rule text]

**Audit Committee Reporting Cadence**:

| Report Type                  | Frequency                       | Content                                                                     |
| ---------------------------- | ------------------------------- | --------------------------------------------------------------------------- |
| Complaint summary            | Quarterly                       | Reports received by category, status, and resolution                        |
| Material accounting matters  | Immediate                       | Any allegation involving financial statement fraud or material ICFR failure |
| Active OSHA investigations   | Immediately on receipt          | Filing date, allegation summary, status                                     |
| SEC/DOJ inquiries            | Immediately                     | Nature of inquiry, subject matter                                           |
| Program effectiveness review | Annual                          | Metrics trend analysis, gap remediation status, benchmark comparison        |
| Retaliation incidents        | Immediately upon substantiation | Facts, remediation, disciplinary action                                     |

**Industry Benchmarks** (NAVEX 2025 Whistleblowing Benchmark Report — 4,000+ orgs,
69 million employees, 2.15 million reports): US median = **1.78 reports per 100 employees**
(global median: 1.57). Below 1.0 per 100 employees may indicate a speak-up culture gap or
trust deficit. For the first time in 2025, web/digital form submissions surpassed phone as
the most common intake channel. Anonymous reports continue to account for the majority of
disclosures. [VERIFY against most current NAVEX annual report]

**Program Metrics Dashboard** (minimum for DOJ ECCP / SEC examination readiness):

| Metric                                  | Reporting Frequency | Purpose                                |
| --------------------------------------- | ------------------- | -------------------------------------- |
| Reports received by channel             | Monthly             | Channel utilization and accessibility  |
| Reports by allegation category          | Quarterly           | Risk area identification               |
| Anonymous vs. identified reports        | Quarterly           | Anonymity chilling effect monitoring   |
| Time to acknowledgment (days)           | Per report          | Responsiveness benchmark               |
| Time to close (days by complexity tier) | Per report          | Operational efficiency                 |
| Substantiation rate                     | Quarterly           | Program credibility signal             |
| Retaliation claims filed internally     | Quarterly           | Anti-retaliation program effectiveness |
| External regulatory referrals           | Quarterly           | Cooperation tracking                   |
| Active OSHA/SEC investigations          | Monthly             | Current legal exposure                 |
| Rule 21F-17 agreement remediation       | Annual              | Compliance with anti-impediment rule   |

#### CCO Independence Requirements (DOJ ECCP September 2024)

DOJ's Evaluation of Corporate Compliance Programs (September 2024) asks:

- Does the CCO have direct reporting access to the board or audit committee?
- Is the CCO's compensation independent from business unit performance?
- Does the CCO have sufficient resources and authority to investigate without business
  unit interference?
- Are compliance functions adequately resourced relative to the organization's risk profile?

Program design should reflect these requirements: CCO whistleblower function should have:

- Direct access to audit committee chair on any matter without GC intermediation
- Written authority to retain outside counsel independently for investigations
- Budget authority for investigation costs not subject to GC or business-line approval
- Protection from retaliation for escalating matters to the board

---

### Step 12: SEC Rule 10D-1 Clawback Integration

For Exchange Act reporting companies, integrate the whistleblower program with the SEC
Rule 10D-1 clawback policy (effective November 28, 2023 for most NYSE/Nasdaq issuers).
[VERIFY current effective date and rule text]

**Interaction with whistleblower program**:

- Whistleblower reports of accounting errors or financial misreporting may trigger
  mandatory clawback analysis
- Investigation findings of financial restatement require Rule 10D-1 analysis of whether
  incentive compensation must be clawed back
- Clawback determinations must be made by the compensation committee; cannot be delegated
  to management (conflict of interest)
- Investigation protocol should include: "Does this finding implicate financial results
  that would trigger Rule 10D-1 analysis?" as a mandatory escalation question

**Documentation requirement**: Board/compensation committee minutes must reflect clawback
analysis whenever a financial restatement or correction occurs, even if recovery is not
pursued (with documented justification).

---

### Step 13: Run Quality Verification

Before delivering program design, audit findings, or recommendations, run the complete
Quality Assurance framework (see Quality Assurance section).

**Completeness Check**:

- [ ] All applicable US statutes mapped to organization's specific profile
- [ ] SOX §806 vs. §301 obligations distinguished and both addressed
- [ ] _Digital Realty Trust_ implication addressed (internal vs. SEC external report)
- [ ] All CLARIFY points answered or documented as assumed defaults
- [ ] Rule 21F-17 agreement audit complete if operating mode requires
- [ ] Upjohn warning script included for attorney-directed investigations
- [ ] Litigation hold trigger analysis complete
- [ ] Privilege election framework addressed
- [ ] DOJ ECCP adequacy criteria mapped
- [ ] Glass Box audit trail populated
- [ ] All citations marked VERIFIED or [VERIFY]

---

### Step 14: Deliver Output

Deliver output following the Output Format Template (see final section). Append the Glass
Box audit trail to every output.

---

## US Statutory Framework Deep Reference

### SOX Section 806 (18 U.S.C. § 1514A)

**Full citation**: Sarbanes-Oxley Act of 2002, §806; codified at 18 U.S.C. § 1514A;
implementing regulations at 29 C.F.R. Part 1980

**Covered employers**: Publicly traded companies registered under Exchange Act §12 or
filing under §15(d); subsidiaries, contractors, subcontractors, agents (_Lawson v. FMR_)

**Covered employees**: Employees of covered employers; no minimum service requirement

**Protected activities** (reporting to federal agency, supervisor, or Congress):

- Mail fraud (18 U.S.C. § 1341)
- Wire fraud (18 U.S.C. § 1343)
- Bank fraud (18 U.S.C. § 1344)
- Securities fraud (18 U.S.C. § 1348)
- Violations of SEC rules and regulations
- Federal laws relating to fraud against shareholders

**Filing deadline**: Complainant must file with OSHA within **180 days** of the
retaliatory action (or 180 days from when complainant knew or should have known of the
retaliatory action). [VERIFY current deadline — statutes of limitation can change]

**OSHA investigation process** (29 C.F.R. Part 1980):

1. Complaint filed with OSHA within 180 days
2. OSHA notifies employer within 10 days; employer has 20 days to submit position
   statement
3. OSHA investigation; preliminary order if reasonable cause found
4. Hearing before ALJ if objection filed
5. ARB review available
6. Federal court de novo review if OSHA has not issued final order within 180 days

**Remedies**: Reinstatement; back pay with interest; compensation for litigation costs,
expert witness fees, attorney's fees; special damages including compensatory damages

**Burden of proof**: _Murray v. UBS_ (Feb. 8, 2024, unanimous 9-0) — "contributing
factor" standard; no retaliatory intent required; temporal proximity alone suffices
circumstantially; employer must rebut by clear and convincing evidence.

**Preliminary reinstatement note**: OSHA may order preliminary reinstatement during the
administrative phase. Per Third Circuit 2024 decision, after complainant exercises the
§ 1514A(b)(1)(B) federal court kick-out right, the OSHA preliminary reinstatement order
is not enforceable — it terminates on election of federal forum. Plan accordingly.
[VERIFY Third Circuit decision citation]

---

### SOX Section 301 (15 U.S.C. § 78j-1(m)(4))

**Audit committee complaint procedures** — mandatory for Exchange Act §13(a)/§15(d) filers:

1. **Receipt procedures**: Formal process for receiving complaints about accounting,
   internal controls, and auditing matters
2. **Retention procedures**: Secure record-keeping separate from general personnel/HR files
3. **Treatment procedures**: Investigation response; escalation criteria
4. **Anonymous submission**: Must accept anonymous submissions from employees about
   questionable accounting or auditing matters; anonymous submissions must be handled
   with equal rigor

**NYSE/Nasdaq implementation**: Exchange listing rules require audit committee charter to
specify these procedures; charter must be publicly available on company's website

---

### Dodd-Frank Section 922 (15 U.S.C. § 78u-6)

**Award program** (17 C.F.R. §§ 240.21F-1 to 21F-17):

- Voluntary submission of original information to SEC
- Information must lead to successful enforcement action with sanctions >$1M
- Award: 10-30% of collected sanctions
- Anonymous submission available through counsel

**Anti-retaliation** (Rule 21F-2):

- Covers employees who report to SEC or engage in protected activity
- Per _Digital Realty_ (2018): internal-only report insufficient; must report to SEC for
  Dodd-Frank anti-retaliation protection [VERIFY — confirm post-Digital Realty developments]
- Remedies: reinstatement + double back pay + attorney's fees + expert fees
- Private right of action in federal district court

**Anti-impediment rule** (Rule 21F-17):

- No person may take action to impede an individual from communicating directly with SEC
- Applies to any agreement, policy, or practice
- Covers pre-dispute arbitration agreements, NDAs, separation agreements, employment
  agreements, settlement agreements, and company policies
- No waiver of right to receive SEC award permitted

**2023-2025 enforcement pattern**: Chronology of notable Rule 21F-17 actions:

- **September 2023 — D.E. Shaw & Co. ($10 million)**: Investment adviser required departing
  employees to represent in separation agreements they had not made any complaints with any
  government agency — conditioning benefits on a representation that chilled future reporting.
  [VERIFY]
- **January 17, 2024 — J.P. Morgan Securities ($18 million)**: Retail client settlement
  releases restricted clients from affirmatively reporting to SEC; passive-only carve-out
  (permitted responding to government inquiries) held insufficient. [VERIFY]
- **September 9, 2024 — Seven-company sweep ($3M+ combined)**: Acadia Healthcare, AppFolio,
  IDEX Corporation, LSB Industries, Smart for Life, TransUnion, and others; separation
  agreement confidentiality provisions without adequate carve-outs. [VERIFY]
- **January 16, 2025 — Two Sigma Investments ($90M combined / $45M each)**: Identification-trap
  (state-as-fact no government complaint filed) + financial disincentive provisions. [VERIFY]

**Enforcement posture note (2025)**: After SEC Chair Paul Atkins's appointment in 2025,
the SEC brought significantly fewer Rule 21F-17 enforcement actions — a marked reduction
from the Biden-era pace. However: (a) the legal obligations under Rule 21F-17 have not
changed; (b) DOJ and OSHA issued a joint statement (January 14, 2025) targeting NDAs
that undermine whistleblower protection laws under antitrust statutes — signaling parallel
enforcement even during SEC restraint; (c) private litigation under Rule 21F-2 continues
independent of SEC enforcement pace. Do not treat enforcement pause as regulatory permission
to use restrictive agreements. [VERIFY current enforcement posture with securities counsel]

[VERIFY all enforcement citations against SEC press releases before relying on them]

---

## Program Domain Framework

Assess or design the program against these eight core domains. Each domain rated:
COMPLIANT / PARTIAL / NON-COMPLIANT / NOT ASSESSED.

### Domain 1 — Governance and Oversight

**Requirements**:

- Written whistleblower policy approved by board or audit committee (not management only)
- SOX §301 procedures established and documented for audit committee
- Designated receiving officer independent of operational management
- CCO has direct access to audit committee without GC intermediation on material matters
- Written escalation procedure from intake to audit committee
- Annual board review of program effectiveness metrics
- CCO independence from business unit performance metrics

**COMPLIANT**: Written policy; §301 procedures; audit committee charter updated;
independent routing; documented escalation; annual board review

**PARTIAL**: Policy exists but predates Dodd-Frank; §301 procedures informal; audit
committee receives reports only through GC; no annual review

**NON-COMPLIANT**: No written policy; no §301 procedures; no audit committee oversight;
complaint function embedded in operational management

---

### Domain 2 — Reporting Channels

**Requirements**:

- SOX §301: Anonymous submission capability mandatory for accounting/controls/audit matters
- At least one internal channel accessible to all workers (employees + contractors)
- Third-party provider or equivalent independence
- Multiple intake modalities (phone, web, email, in-person)
- 24/7 availability for time-sensitive reports
- External channel guidance documented and communicated (Rule 21F-17 compliance)

**COMPLIANT**: Third-party hotline; web portal; anonymous capability; accessible to all
worker categories; external channel guidance in policy and onboarding

**PARTIAL**: Phone hotline only; no web portal; employees covered but contractors excluded;
no external channel guidance provided

**NON-COMPLIANT**: Manager-only escalation; no anonymous capability; §301 anonymous
requirement unmet; contractors excluded from coverage

---

### Domain 3 — Intake Triage and Routing

**Requirements**:

- Documented triage procedure with written decision criteria
- CRISIS-tier triggers acted upon immediately (no triage delay)
- Routing independent of reporter's management chain and respondent
- Regulatory deadline tracking from receipt (OSHA 180-day clock; litigation hold analysis)
- Privilege election decision documented at investigation opening
- Case log maintained securely: date received, triage classification, routing, status

**COMPLIANT**: Written triage procedure; CRISIS-tier protocol; independent routing; deadline
tracking; privilege election documented; secure case log

**PARTIAL**: Informal triage; no CRISIS triggers; routing through line management; no
deadline tracking

**NON-COMPLIANT**: No triage; reports routed to respondent's management; no records;
no deadline tracking

---

### Domain 4 — Confidentiality and Identity Protection

**Requirements**:

- Identity accessible only to designated investigation personnel
- Anonymous reports accepted and handled with equal rigor (§301 requires this for
  accounting/controls reports)
- Coded case reference system throughout investigation
- Written documentation of any authorized identity disclosure
- Employment agreements contain Rule 21F-17 safe harbor language — no prohibited
  impediment provisions
- Agreement audit completed for all standard templates

**COMPLIANT**: Access controls documented; anonymous handling equal to identified;
safe harbor language in all agreements; no prohibited provisions

**PARTIAL**: Confidentiality intended but undocumented; some agreements lack carve-out
language; anonymous reports handled informally

**NON-COMPLIANT**: Identity disclosed without justification; active enforcement of
confidentiality agreements against regulatory reporting; agreements contain prohibited
provisions without safe harbor

---

### Domain 5 — Anti-Retaliation

**Requirements**:

- Written anti-retaliation policy citing 18 U.S.C. § 1514A, Rule 21F-2, and other
  applicable statutes
- Interim protective measures procedure for open investigations
- Legal review gate: no adverse employment action affecting known reporter without
  employment counsel approval
- Annual manager training on prohibited retaliation (what it is; how to avoid it)
- Monitoring: track adverse actions following known disclosures; flag temporal proximity
- Confirmed retaliation: reinstatement, back pay, discipline of retaliating manager
- SOX §806 OSHA response procedure if complaint is filed

**COMPLIANT**: Written policy with statutory citations; interim measures; legal review
gate; annual training; monitoring; documented response protocol

**PARTIAL**: Policy exists but unpublished; no interim measures; adverse actions not
reviewed before execution; training more than 24 months old

**NON-COMPLIANT**: No policy; known retaliation not addressed; reporter adversely affected
during open investigation; no training

---

### Domain 6 — Investigation Protocol

**Requirements**:

- Written investigation procedures: scope, timeline, documentation standards
- Investigator conflict screening for every case
- Privilege election decision documented at investigation opening
- Upjohn warnings script ready for attorney-directed investigations
- Complexity tier assignment at intake (PRELIMINARY / STANDARD / COMPLEX / CRISIS)
- Findings documented: Substantiated / Partially Substantiated / Unsubstantiated
- Litigation hold triggers mapped and enforced from earliest anticipation
- Remediation connected to substantiated findings

**COMPLIANT**: Written procedures; conflict screening; privilege election; Upjohn script;
tier assignment; written findings; litigation hold; remediation tracking

**PARTIAL**: Informal procedures; no conflict screening; privilege election ad hoc; no
Upjohn script; findings verbal only

**NON-COMPLIANT**: No procedures; conflicted investigators; no privilege framework; no
written findings; no remediation

---

### Domain 7 — DOJ ECCP Adequacy (if DOJ exposure or government contracting)

For organizations at risk of DOJ enforcement (government contractors, FCA exposure,
criminal regulatory matters), assess adequacy under the DOJ Evaluation of Corporate
Compliance Programs (September 2024):

**DOJ ECCP September 2024 — Dedicated Whistleblower Section** ("Commitment to
Whistleblower Protection and Anti-Retaliation"): Prosecutors are directed to evaluate
all seven of these specific criteria:

1. **Anonymous reporting mechanism exists**: Dedicated hotline/portal — necessary but
   not sufficient alone.
2. **Company actively encourages and incentivizes reporting**: Passive existence of a
   hotline is inadequate; active promotion through training, leadership messaging, and
   regular communication is required.
3. **Company practices do not chill reporting**: NDAs, separation agreements, management
   behavior that discourages speaking up are red flags. Rule 21F-17 compliance is
   embedded in this criterion.
4. **Differential treatment of reporters vs. non-reporters**: How employees who report
   are treated compared to those who do not — promotions, reviews, assignments after
   reporting are scrutinized.
5. **Anti-retaliation policies and training cover external whistleblower programs**:
   Training covering only the internal hotline is insufficient; training must address
   SEC, DOJ, OSHA, and other external reporting rights.
6. **Company assesses employees' willingness to report**: Culture surveys, exit interview
   data, focus groups — this makes culture measurement an adequacy requirement, not
   just best practice.
7. **No penalization or impediment of reporting**: This is now a specific enforcement
   trigger; any documented act to discourage reporting eliminates ECCP credit.

_Note: These criteria apply broadly — not only to formal DOJ enforcement targets. Any
company seeking to demonstrate compliance program adequacy (e.g., in SEC proceedings,
OSHA responses, or civil litigation) should assess all seven._

**COMPLIANT**: Program documented; metrics show active use; training records current;
discipline records show consistent application; CCO has independent board access

**PARTIAL**: Documentation exists but metrics show low utilization; inconsistent discipline;
CCO must route through GC for all board communication

**NON-COMPLIANT**: Program on paper only; no usage; no training; no discipline of retaliators

---

### Domain 8 — SEC Examination Readiness

For registered entities (broker-dealers, investment advisers, registered funds), assess
readiness for SEC examination of whistleblower program:

**What examiners request**:

- Whistleblower policy and procedures
- Complaint log for the examination period (typically 2-3 years)
- Sample investigation files (redacted for privilege)
- Training records and materials
- Employment agreement templates (Rule 21F-17 review)
- Separation agreement and NDA templates
- Evidence of audit committee complaint procedures

**Common examination findings** [VERIFY against current OCIE/EXAMS priorities]:

- Incomplete or missing Rule 21F-17 safe harbor language
- No complaint log or incomplete records
- Hotline inaccessible to contractors
- §301 procedures not reflected in audit committee charter
- Training records not maintained

---

## Investigation Complexity Tiers

Assign every report to one of four tiers at intake:

| Tier            | Characteristics                                                                                                               | Investigator                                           | Counsel                                  | Timeline                                  |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------- | ----------------------------------------- |
| **PRELIMINARY** | Anonymous; vague; no identifiable respondent; no specific allegation of legal violation                                       | HR designee or CCO                                     | Optional                                 | 1-2 weeks; fact-gather; close or escalate |
| **STANDARD**    | Named parties; workplace-level; no executive respondent; no regulatory parallel                                               | Compliance + HR                                        | Recommended                              | 4-8 weeks                                 |
| **COMPLEX**     | Executive or board respondent; financial materiality; parallel regulatory inquiry; privilege-sensitive; multiple allegations  | CCO + outside employment/securities counsel            | Required                                 | 8-16 weeks                                |
| **CRISIS**      | Active government investigation; material financial fraud allegation; criminal conduct; board-level respondent; press inquiry | Outside counsel lead; board committee direct oversight | Required; CEO/GC/Board directly involved | Variable; paced by regulatory timeline    |

**Automatic CRISIS triggers — escalate immediately**:

- Receipt of OSHA complaint, SEC subpoena, or government CID referencing the subject matter
- Allegation that CEO, CFO, GC, or board member is a respondent
- Allegation of financial statement fraud, material misstatement, or insider trading
- Report triggers mandatory regulatory notification (SAR, mandatory disclosure, etc.)
- Retaliation incident during open investigation
- Reporter's counsel sends litigation preservation letter
- Press inquiry references the alleged conduct

---

## Protected Activity Catalogue (US Federal)

### SOX Section 806 Protected Activities

**Protected against retaliation**:

- Internal reports to supervisor, Compliance, GC, or audit committee about reasonably
  believed violations of: mail fraud (§1341), wire fraud (§1343), bank fraud (§1344),
  securities fraud (§1348), SEC rules, or federal laws relating to fraud against shareholders
- External reports to federal regulatory/law enforcement agencies (SEC, DOJ, OSHA, FBI)
- Reports to members of Congress or their staff
- Assisting in any investigation or proceeding related to the above
- Filing, testifying, or participating in proceedings about the above

**NOT protected under SOX §806** (but may be protected under other statutes):

- Reports of labor law violations unrelated to securities fraud
- Reports in bad faith or solely for personal gain
- Reports that do not meet the "reasonable belief" standard
- Reports only to media or public (must be to appropriate government body or internally)

### Dodd-Frank Section 922 Protected Activities

**Protected**: Providing information to SEC about reasonably believed federal securities
law violations; assisting in SEC investigation or enforcement action

**Critical distinction**: Per _Digital Realty Trust v. Somers_ (2018), Dodd-Frank
anti-retaliation protection under §21F(h) requires an actual report to the SEC —
internal-only reporting does not qualify for Dodd-Frank protection (SOX §806 separately
protects internal reports)

**Exception**: Rule 21F-4(b)(7) internal reporting credit — individual who reports
internally first and SEC receives information within 120 days may still be treated as
a whistleblower for award purposes [VERIFY]

### OSHA-Administered Statutes

**Coverage varies by statute**: OSHA administers 25+ whistleblower protection statutes
covering reports of: workplace safety violations (OSH Act §11(c)); financial fraud (SOX
§806); food safety (FSMA); consumer product safety; environmental violations (Clean Air
Act, SDWA, TSCA); nuclear safety (ERA); surface transportation safety (STAA); consumer
financial protection (CFPA); and others.

**Filing deadline is statute-specific**: Ranges from 30 days (Clean Air Act, SDWA) to
180 days (SOX, FSMA, CFPA, STAA). **The applicable deadline must be identified on the
day a report is received** — missing the OSHA deadline bars the claim permanently.

### False Claims Act Protected Activities

- Investigating, initiating, testifying in, or assisting in any FCA action
- Reporting internally to supervisors about potential FCA violations
- Any good-faith effort to stop violations of the FCA
- Does NOT require filing a qui tam lawsuit — internal investigation suffices

---

## Regulatory Deadline Matrix (US)

Track these critical deadlines from the date any report is received or adverse action occurs:

| Deadline                              | Trigger                                                  | Statute                    | Consequence of Miss                                         |
| ------------------------------------- | -------------------------------------------------------- | -------------------------- | ----------------------------------------------------------- |
| **OSHA filing — 180 days**            | Retaliatory action against reporter                      | SOX §806                   | Retaliation claim time-barred; employer may move to dismiss |
| **OSHA filing — 180 days**            | Retaliatory action                                       | CFPA, FSMA, STAA, ACA, ERA | Claim time-barred                                           |
| **OSHA filing — 30 days**             | Retaliatory action                                       | Clean Air Act, SDWA        | Claim time-barred                                           |
| **OSHA filing — 30-60 days**          | Retaliatory action                                       | AHERA, certain others      | Claim time-barred                                           |
| **Litigation hold**                   | Reasonable anticipation of litigation/proceeding         | General civil procedure    | Spoliation sanctions; adverse inference instruction         |
| **120-day internal window**           | Internal report made; Dodd-Frank award consideration     | Rule 21F-4(b)(7)           | Loss of potential award attribution credit                  |
| **OSHA response — 20 days**           | Employer notified of SOX §806 complaint                  | 29 C.F.R. § 1980.105       | Default preliminary order possible                          |
| **FCA qui tam — 6 years**             | Date of violation (or 3 years from government knowledge) | 31 U.S.C. § 3731           | Claim time-barred; max 10 years from violation              |
| **Dodd-Frank civil action — 6 years** | Retaliatory action                                       | 15 U.S.C. § 78u-6(h)       | Federal court claim time-barred [VERIFY]                    |

**Operational requirement**: Intake log must automatically flag OSHA deadline on receipt
of any report that may constitute a protected disclosure, even before classification is
complete. A missed OSHA deadline cannot be cured.

---

## Severity Classification

### Program Domain Level

| Rating            | Definition                                             | Required Response                                                          |
| ----------------- | ------------------------------------------------------ | -------------------------------------------------------------------------- |
| **COMPLIANT**     | Meets all applicable US federal requirements           | Maintain; conduct periodic review                                          |
| **PARTIAL**       | Partially meets requirements; specific gaps identified | Remediation plan required with timeline; prioritize by regulatory exposure |
| **NON-COMPLIANT** | Fails requirements; enforcement exposure exists        | Immediate remediation; outside counsel; board notification                 |

### Employment Agreement Finding Level

| Rating                | Definition                                                                  | Response                                                                    |
| --------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **RED — Prohibited**  | Language directly violates Rule 21F-17 or waives right to government report | Amend immediately; assess whether historical agreements create SEC exposure |
| **YELLOW — Risk**     | Language may chill protected reporting or creates arguable impediment       | Remediate in next revision cycle; notify legal                              |
| **GREEN — Compliant** | Contains required safe harbor; no prohibited provisions                     | Document and maintain                                                       |

### Retaliation Incident Level

| Rating       | Definition                                                                    | Response                                                                         |
| ------------ | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **CRITICAL** | Confirmed or highly probable retaliation against known reporter               | Outside counsel immediately; interim protective measures; OSHA deadline tracking |
| **HIGH**     | Adverse action temporally proximate to disclosure; causal connection possible | Legal review before action; document independent business justification          |
| **MEDIUM**   | Employment action involving known reporter; temporal proximity moderate       | Legal review before action; document rationale                                   |
| **LOW**      | Employment action; reporter's disclosure is remote or unrelated               | Standard HR process; document that review occurred                               |

---

## Prioritization Framework

### Tier 1 — Must Remediate (Immediate Regulatory Exposure)

- No SOX §301 audit committee complaint procedures (Exchange-listed companies: exchange
  listing standard violation; SEC enforcement risk)
- Anonymous submission capability absent for accounting/controls matters (§301 requires this)
- Employment agreements contain Rule 21F-17 prohibited provisions (active SEC enforcement
  risk; J.P. Morgan Chase $18M penalty example)
- No anti-retaliation policy with statutory citations
- Confirmed retaliation against a known reporter (active litigation and OSHA exposure)
- Known reporter's OSHA deadline within 30 days and complaint not yet filed (litigation
  risk exposure)
- Investigation conducted by conflicted investigator on material matter
- Upjohn warnings not given in attorney-directed investigations (ethical rules risk)
- No litigation hold in place when anticipation of proceeding has arisen

### Tier 2 — Should Remediate (Compliance Gap; Near-Term Risk)

- Third-party hotline not in use (reliance on manager-only escalation)
- Contractors not covered by internal channel (statutory coverage gaps)
- No formal triage procedure or CRISIS-tier escalation protocol
- Annual manager anti-retaliation training absent or more than 24 months old
- OSHA regulatory deadline not tracked from intake
- No privilege election documentation at investigation opening
- Board receives no program metrics (DOJ ECCP adequacy gap)
- SEC Rule 10D-1 clawback policy not integrated with investigation protocol
- No external channel guidance provided to workers (Rule 21F-17 interpretive risk)
- CCO lacks direct board/audit committee access

### Tier 3 — Should Consider (Best Practice; DOJ ECCP Credit)

- Third-party ombudsperson engaged for additional independence
- Program benchmarked against NAVEX or ECI industry data (reports per 1,000 employees)
- Reporter feedback beyond acknowledgment (update on investigation status)
- Annual external audit of program effectiveness
- Annual SEC/CFTC award program communication to all employees
- Proactive distribution of safe harbor language amendment to legacy agreement holders
- Monthly program metrics dashboard reviewed by CCO; quarterly by audit committee

---

## Quality Assurance Framework

### Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                       | Fail Action                                                      |
| -------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Source**     | Every US regulatory obligation cites specific statute, section, or CFR provision                           | Add citation or mark "[UNVERIFIED — counsel to confirm statute]" |
| **Format**     | All citations use consistent US legal citation format (U.S.C., C.F.R., Pub. L.)                            | Fix format                                                       |
| **Currency**   | Every cited provision checked: SOX/Dodd-Frank amended? SEC rules revised? OSHA deadlines current?          | Flag "[CHECK CURRENCY — rule may have been amended]"             |
| **Domain**     | Analysis stays within US federal law scope; state whistleblower protections explicitly flagged as separate | Flag state law overlap and direct to employment counsel          |
| **Confidence** | Uncertainty explicitly stated, not hidden; case law citations include docket [VERIFY] tag                  | Add confidence qualifier; apply [VERIFY] tag                     |

### Self-Interrogation for NON-COMPLIANT Domains

For any domain rated NON-COMPLIANT, apply before finalizing:

**Pass 1 — Legal Chain Integrity**: Does the non-compliance finding follow logically from
the cited statutory provision or regulatory guidance? Would SEC, DOJ, or OSHA actually
reach this conclusion? What is the strongest counter-argument?

**Pass 2 — Completeness**: Has the most current version of the statute/rule been considered?
Have SEC/DOJ guidance documents, no-action letters, or enforcement releases been considered?
Are there phase-in timelines or safe harbors that soften the finding?

**Pass 3 — Challenge**: What is the best argument that current practice is compliant or
defensible? Under what circumstances would the regulator exercise discretion not to enforce?
Is the finding proportionate to actual risk?

Mark outcome: `self_interrogation: PASS` (finding confirmed) or `self_interrogation: REVISED`
(finding adjusted with explanation).

### Confidence Scoring

| Level        | Range     | Meaning                                                                    | Action                                                |
| ------------ | --------- | -------------------------------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear statutory text; unambiguous rule language; binding SCOTUS            | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong statutory authority; consistent SEC/DOJ guidance; circuit precedent | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good authority; reasonable interpretations differ; circuit split           | State with reasoning and contra-indicators            |
| **Possible** | 0.40–0.59 | Genuine uncertainty; limited precedent; evolving regulatory guidance       | Flag for qualified counsel with both sides            |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative; contrary authority predominates                   | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Append this YAML block to every output:

```yaml
glass_box:
  skill_name: "legalcode-us-whistleblower-program-builder"
  engagement_date: "[YYYY-MM-DD]"
  operating_mode: "[Build New / Audit / Agreement Review / OSHA Response / Board Readiness / Award Analysis]"
  organization_profile:
    exchange_listing: "[NYSE / Nasdaq / OTC / Private / Other]"
    sec_registrant: "[yes / no / unknown]"
    cftc_regulated: "[yes / no / unknown]"
    government_contractor: "[yes / no / unknown]"
    employee_count_us: "[number]"
    sector: "[sector]"
  statutes_in_scope:
    sox_806: "[applicable / not applicable / unknown]"
    sox_301: "[applicable / not applicable / unknown]"
    dodd_frank_922: "[applicable / not applicable / unknown]"
    cftc_748: "[applicable / not applicable / unknown]"
    osha_programs: "[applicable / not applicable — statutes: list]"
    false_claims_act: "[applicable / not applicable / unknown]"
    aml_act_2020: "[applicable / not applicable / unknown]"
    irs_7623: "[applicable / not applicable / unknown]"
  domains_assessed:
    governance_oversight: "[COMPLIANT / PARTIAL / NON-COMPLIANT / NOT ASSESSED]"
    reporting_channels: "[COMPLIANT / PARTIAL / NON-COMPLIANT / NOT ASSESSED]"
    intake_triage: "[COMPLIANT / PARTIAL / NON-COMPLIANT / NOT ASSESSED]"
    confidentiality_identity: "[COMPLIANT / PARTIAL / NON-COMPLIANT / NOT ASSESSED]"
    anti_retaliation: "[COMPLIANT / PARTIAL / NON-COMPLIANT / NOT ASSESSED]"
    investigation_protocol: "[COMPLIANT / PARTIAL / NON-COMPLIANT / NOT ASSESSED]"
    doj_eccp_adequacy: "[COMPLIANT / PARTIAL / NON-COMPLIANT / NOT ASSESSED]"
    sec_examination_readiness: "[COMPLIANT / PARTIAL / NON-COMPLIANT / NOT ASSESSED]"
  tier1_gaps_identified: "[number] — [brief list]"
  agreement_audit_performed: "[yes / no / partial]"
  prohibited_language_found: "[yes / no / N/A]"
  osha_deadline_tracked: "[yes / no / N/A]"
  upjohn_warning_addressed: "[yes / no / N/A]"
  privilege_election_addressed: "[yes / no / N/A]"
  legalcode_mcp: "[Connected / Not connected]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED — marked [VERIFY]]"
  self_interrogation: "[PASS / REVISED / NOT APPLICABLE]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  digital_realty_implication_addressed: "[yes / no / N/A]"
  rule_21f17_audit_complete: "[yes / no / partial / N/A]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
    - "State whistleblower protections not in scope — refer to employment counsel"
    - "Award eligibility analysis is framework only — not a legal opinion on award qualification"
  reviewer: "AI-assisted — requires qualified US securities, employment, and regulatory counsel review"
```

---

## Anti-Patterns

What NOT to do when designing, auditing, or operating a US whistleblower program:

### Governance Anti-Patterns

1. **Routing all complaints through GC**: CCO whistleblower function reports only to
   General Counsel, with no independent path to audit committee. GC may be conflicted
   when the subject matter creates legal liability. SOX §301 and DOJ ECCP expect
   independent audit committee access; examiners specifically look for this.

2. **Audit committee procedures not in charter**: SOX §301 complaint procedures exist
   informally but are not reflected in the audit committee charter. NYSE/Nasdaq listing
   rules require the charter to specify these procedures; SEC examination will request the
   charter.

3. **CCO compensation tied to business unit performance**: Compliance officer's bonus
   is based on the profitability of the business line they oversee. DOJ ECCP September 2024
   specifically asks whether compliance officer compensation creates conflicts of interest.

4. **Policy approved by HR management only**: Board or audit committee never formally
   adopted the whistleblower policy. DOJ ECCP requires evidence of board-level commitment;
   HR-approved policy does not satisfy this.

5. **No annual program effectiveness review**: Program was designed at implementation;
   no metrics reviewed since. DOJ ECCP "works in practice" test is specific: regulators
   want to see that programs actually receive and investigate reports, not just that
   policies exist on paper.

### Channel Design Anti-Patterns

6. **Anonymous submission disabled for SOX §301 matters**: Audit committee complaint
   procedures do not accept anonymous submissions. This directly violates SOX §301 which
   explicitly requires procedures for "confidential, anonymous submission." A single
   Exchange Act enforcement inquiry could identify this gap immediately.

7. **Manager-only escalation path**: Internal reporting route requires employees to report
   to their direct manager first. Reports about the manager or manager's supervisor are
   structurally guaranteed to be suppressed. Routing must bypass the management chain.

8. **Contractors excluded from reporting channel**: Internal channel (and all program
   materials) are available only to employees. _Lawson v. FMR_ extended SOX §806 to
   contractor employees. OSHA statutes vary. Excluding contractors creates statutory
   coverage gaps and operational blind spots.

9. **No external channel guidance**: Organization does not communicate the SEC
   Whistleblower Office, OSHA Whistleblower Protection Program, or other external
   reporting options to workers. Withholding this information, combined with any
   impeding agreement language, creates Rule 21F-17 exposure.

10. **Single channel program**: Only one intake method offered (e.g., phone hotline).
    Technology failures, language barriers, or fear of call recording deter reports.
    SEC examination readiness requires demonstrable accessibility.

### Rule 21F-17 and Agreement Anti-Patterns

11. **Broad confidentiality in separation agreements**: Standard severance template
    requires employees to keep all company information confidential without a government
    agency carve-out. This is the most common SEC enforcement target in the 2024 wave.
    Every separation agreement must be reviewed.

12. **Non-disparagement without government carve-out**: Non-disparagement clauses
    covering "statements about the company or its operations" without explicitly exempting
    government communications. SEC has taken enforcement action against this pattern.

13. **Mandatory internal reporting requirement**: Policy or agreement requires employees
    to report violations internally first before contacting any external party. Rule 21F-17
    explicitly prohibits mandatory internal-first requirements that impede SEC communications.

14. **Not remediating historical agreements**: Organization amends new agreements but
    does not address legacy agreements currently held by active employees. SEC has
    required issuers to reach out to current employees covered by legacy impeding agreements.
    In _Two Sigma_ (January 16, 2025, $90M combined / $45M each), departing employees
    were required to (i) state as fact they had not filed any government complaint
    (identifying potential whistleblowers) and (ii) accept financial forfeiture provisions
    that created a disincentive to concurrent regulatory reporting. Both mechanisms
    independently violated Rule 21F-17 — the identification trap and the financial
    disincentive are each standalone violations. [VERIFY]

15. **Assuming award waiver is enforceable**: Separation agreement includes language
    stating employee "waives any right to any award program." 15 U.S.C. § 78u-6(h)(1)(A)(i)
    explicitly voids such waivers — they are legally unenforceable and their presence is
    itself a Rule 21F-17 violation.

### Anti-Retaliation Anti-Patterns

16. **Adverse action taken before investigation completes**: Reporter denied promotion
    or given negative performance review while investigation of their complaint is open.
    Under the SOX §806 contributing-factor standard, temporal proximity alone is sufficient
    to create a triable retaliation claim (_Murray v. UBS_, 2024). Legal review gate is
    non-negotiable.

17. **Suspension of reporter during their own complaint investigation**: Reporter placed
    on administrative leave "pending investigation" of the complaint they made. This creates
    a presumption of retaliation under virtually every applicable burden-of-proof framework.

18. **Retaliating manager remains in role after substantiated retaliation**: Post-finding,
    retaliating manager receives no discipline. DOJ ECCP explicitly evaluates whether
    discipline is "consistent and fairly applied" — a manager who retaliates without
    consequence signals that retaliation is permitted.

19. **No legal review gate for employment actions involving reporters**: HR can execute
    adverse actions affecting known whistleblowers without employment counsel sign-off.
    This eliminates the primary operational control for preventing inadvertent retaliation
    liability.

20. **Manager training not refreshed after enforcement actions**: Anti-retaliation training
    was delivered at onboarding only. DOJ ECCP requires training to be current and adapted
    to recent enforcement developments; annual refresh is minimum.

### Investigation Anti-Patterns

21. **Privilege election not made at investigation opening**: Investigation begins without
    determining whether it is attorney-directed or HR-directed. After the investigation
    concludes, a post-hoc privilege claim is difficult to sustain and creates regulatory
    credibility risk.

22. **Upjohn warning omitted**: Corporate employees interviewed in an attorney-directed
    investigation without Upjohn warning. Creates ethical complications and may expose the
    organization to professional responsibility issues if the employee later claims they
    believed company counsel represented them personally.

23. **Selective waiver to SEC without privilege analysis**: Organization discloses
    investigation report to SEC as part of cooperation and then asserts privilege against
    private plaintiffs. Selective waiver doctrine varies by circuit; this decision requires
    outside counsel analysis before any disclosure.

24. **Litigation hold issued too late**: Organization issues litigation hold after receiving
    OSHA complaint but not upon receiving the initial whistleblower report. Anticipation
    of litigation arises at the earliest reasonable point — often the original complaint.
    Late hold may result in spoliation sanctions.

25. **Investigator is respondent's HR business partner**: HRBP for the respondent's
    department assigned as investigator. Structural conflict that may invalidate investigation
    integrity regardless of the investigator's good faith. Conflict screening must be
    completed before assignment.

### Reporting and Documentation Anti-Patterns

26. **No complaint log maintained**: Organization has no written record of complaints
    received, triage decisions, routing, status, or closure. In SEC examination, DOJ
    investigation, or OSHA proceeding, absence of records creates an inference that the
    program does not function. Every report must be logged from receipt.

27. **OSHA deadline not tracked from intake**: OSHA complaint deadline (180 days for SOX
    §806; 30 days for some environmental statutes) is not tracked from the date of the
    retaliatory action. The deadline is not from the date of the internal complaint —
    it runs from the retaliatory action. A missed deadline cannot be cured.

28. **Findings communicated verbally only**: Investigation closes with verbal summary
    only. The written closing memorandum ("Substantiated / Partially Substantiated /
    Unsubstantiated" + rationale + recommended action) is essential for OSHA response,
    DOJ cooperation credit, and litigation defense.

29. **Clawback analysis not triggered by substantiated financial misconduct**: Investigation
    substantiates financial statement irregularity. No one runs Rule 10D-1 clawback analysis.
    Compensation committee is not notified. The failure to conduct and document this
    analysis is itself an SEC disclosure and governance issue.

30. **Audit committee reports are metrics-free**: Board receives narrative updates about
    "the program continues to operate" without usage statistics, substantiation rates,
    or trend analysis. DOJ ECCP and NYSE/Nasdaq governance standards require the audit
    committee to actively oversee program effectiveness — not just receive confirmation
    of its existence.

### Digital Realty and Award Program Anti-Patterns

31. **Assuming internal report qualifies for Dodd-Frank anti-retaliation**: After _Digital
    Realty Trust v. Somers_ (2018), employees who report only internally — not to the SEC
    — do not have Dodd-Frank §922(h) anti-retaliation protection. SOX §806 separately
    protects internal reports, but the remedies differ. Failing to analyze which statute
    applies to a specific retaliation claim may result in wrong procedural path and missed
    deadlines.

32. **Discouraging SEC reporting to protect internal processes**: Program or managers
    (formally or informally) discourage employees from "going to the SEC" and request
    internal escalation first. Rule 21F-17 prohibits any action to impede direct SEC
    communication. Even a well-intentioned internal-first culture, if implemented through
    any agreement or policy, creates enforcement exposure.

---

## Writing Standards

Apply these standards to all program deliverables, policies, and regulatory responses:

**For Whistleblower Policies and Procedures**:

- Write in plain language that a non-lawyer employee can understand without interpretation
- Active voice: "Submit your report to the hotline at [number]" not "Reports should be
  submitted"
- Numbered steps for procedural instructions; one instruction per step
- Define terms at first use; spell out acronyms
- Short sentences; one idea per sentence
- Include contact information, not just role titles

**For OSHA Responses and Government Correspondence**:

- Lead with the dispositive fact; do not bury it in procedural narrative
- Every factual assertion supported by a document reference (Bates number or exhibit)
- Legal argument separated from factual narrative
- Timeline presented in table format where complex
- Consistent characterization of the reporter as "complainant" or by name — not
  pejoratively or dismissively

**For Board and Audit Committee Reports**:

- Lead with the key finding and its regulatory or business consequence
- Use tables for metrics; narrative only for significant anomalies
- Quantify: number of reports, substantiation rates, time-to-close averages
- Tier 1 gaps flagged explicitly and separately
- "No action required" or "for information only" clearly stated for routine reports

**Quality Gates Before Delivery**:

1. Every regulatory obligation cites the specific provision (not just "applicable law")
2. Every legal claim is backed by citation or flagged [VERIFY]
3. No conditional or hedged language where statutory text is clear
4. Glass Box audit trail appended and complete
5. _Digital Realty_ implication addressed wherever internal vs. external reporting is discussed
6. OSHA deadline mapped wherever retaliatory action is identified

---

## External Tool Integration

**With legalcode-mcp connected (preferred)**:

- Search for current SEC Whistleblower Office annual report statistics (tips, awards, amounts)
- Verify most recent SEC enforcement actions under Rule 21F-17 (agreement language precedents)
- Confirm current OSHA filing deadlines for specific statutes
- Verify current state of _Digital Realty_ developments in circuit courts post-2018
- Search for most recent DOJ ECCP guidance and whistleblower-specific criteria
- Confirm current NYSE/Nasdaq listing standard rule text for audit committee requirements
- Search for CFTC whistleblower program annual statistics
- Mark all legalcode-mcp-sourced citations as VERIFIED in Glass Box audit trail

**Without legalcode-mcp**:

- Proceed with statutory framework from training data
- Mark all case citations and penalty amounts with [VERIFY]
- Note: `legalcode_mcp: "Not connected"` in Glass Box
- Focus on structural program design and framework completeness
- Direct user to SEC.gov/whistleblower, DOL.gov/osha/whistleblower, and DOJ.gov for
  current statistics and enforcement guidance

**Cross-skill handoffs**:

- **`legalcode-investigation-plan-builder`**: When a specific report has been triaged
  at STANDARD, COMPLEX, or CRISIS tier and investigation planning is required. Provides
  full 12-step investigation workflow, interview guide templates, and evidence handling.
- **`legalcode-sox-compliance-assessment`**: When whistleblower program assessment reveals
  broader SOX §302/§404 ICFR implications — coordinate findings across both skills.
- **`legalcode-workplace-investigation`**: For PRELIMINARY and STANDARD tier matters that
  are workplace-conduct issues without securities law dimensions.
- **`legalcode-whistleblower-program-builder`**: When organization has multinational
  operations requiring EU Directive, UK PIDA, or France Sapin II/Waserman compliance
  alongside US requirements.

---

## Output Format Template

Every engagement produces output following this structure (adapt sections to operating mode):

```markdown
# US Whistleblower Program [Assessment / Design / Agreement Review / Board Report]

**Organization**: [name or description]
**Date**: [YYYY-MM-DD]
**Engagement Mode**: [Build New / Audit / Agreement Review / OSHA Response / Board Readiness / Award Analysis]
**Statutes In Scope**: [SOX §806 / SOX §301 / Dodd-Frank §922 / CFTC §748 / OSHA statutes / False Claims Act / Other]
**Prepared by**: Legalcode US Whistleblower Program Builder (AI-assisted — qualified US
legal counsel review required before use or reliance)

---

## Executive Summary

[2-4 sentences: What was assessed? What is the overall compliance posture? What is the
most urgent action required?]

**Overall Program Status**: [COMPLIANT / PARTIAL — [N] Tier 1 gaps / NON-COMPLIANT]

---

## Statutory Applicability Matrix

[Table mapping each US federal statute to the organization's profile: applicable / not
applicable / requires further assessment]

---

## Domain Assessment

### Domain 1 — Governance and Oversight: [COMPLIANT / PARTIAL / NON-COMPLIANT]

**Findings**: [Specific gaps identified]
**Tier 1 gaps**: [If any]
**Recommended actions**: [Specific remediation steps with priority]

[Repeat for Domains 2-8]

---

## Priority Gap Register

### Tier 1 — Must Remediate (Immediate)

| Gap | Statute/Rule | Regulatory Exposure | Recommended Action | Owner | Deadline |
| --- | ------------ | ------------------- | ------------------ | ----- | -------- |

### Tier 2 — Should Remediate (Near-Term)

| Gap | Risk Level | Recommended Action | Owner | Deadline |
| --- | ---------- | ------------------ | ----- | -------- |

### Tier 3 — Should Consider (Best Practice)

[List of best-practice enhancements]

---

## Rule 21F-17 Agreement Audit Results

[If applicable]

**Agreements Reviewed**: [number and types]
**RED — Prohibited provisions found**: [list with agreement type and specific language]
**YELLOW — Risk language found**: [list with agreement type]
**GREEN — Compliant**: [percentage compliant]
**Recommended remediation**: [steps, priority, distribution plan]

---

## OSHA Deadline Tracker

[If applicable]

| Reporter | Protected Activity Date | Adverse Action Date | OSHA Deadline | Status |
| -------- | ----------------------- | ------------------- | ------------- | ------ |

---

## Investigation Protocol Assessment

[If applicable]

**Privilege election framework**: [COMPLIANT / PARTIAL / NON-COMPLIANT]
**Upjohn warning script**: [Available / Not available]
**Investigator independence**: [COMPLIANT / PARTIAL / NON-COMPLIANT]
**Litigation hold protocol**: [COMPLIANT / PARTIAL / NON-COMPLIANT]

---

## Board / Audit Committee Reporting

**SOX §301 procedures**: [COMPLIANT / PARTIAL / NON-COMPLIANT]
**Reporting cadence**: [Current / Insufficient / Not established]
**Program metrics provided**: [Yes — summary / No / Not tracked]

---

## Recommended Implementation Roadmap

| Phase                  | Timeframe | Key Actions                         | Responsible |
| ---------------------- | --------- | ----------------------------------- | ----------- |
| Immediate (0-30 days)  |           | Tier 1 gap remediation              |             |
| Near-term (30-90 days) |           | Tier 2 gap remediation              |             |
| Ongoing                |           | Monitoring; training; annual review |             |

---

[Glass Box YAML block]
```

---

## Localization Notes

This skill covers **US federal whistleblower law only**. Additional analysis is required for:

- **State whistleblower laws**: California (Labor Code § 1102.5), New York (Labor Law § 740,
  § 741), New Jersey (Conscientious Employee Protection Act), Illinois (Whistleblower Act),
  and equivalents in all states where the organization has employees. State protections
  often extend beyond federal law. Employment counsel in each relevant state must assess.
- **Industry-specific federal programs**: Banking regulators (OCC, FRB, FDIC, CFPB),
  nuclear (NRC), energy (FERC), healthcare (HHS/OIG) all have sector-specific whistleblower
  dimensions that overlay the statutes described here.
- **US government contractors**: Subject to False Claims Act qui tam as primary exposure;
  also subject to Department of Defense contractor whistleblower protections (10 U.S.C.
  § 4701) and related federal procurement whistleblower provisions. [VERIFY]
- **Multinational operations**: Organizations with EU, UK, or French operations must also
  comply with EU Directive 2019/1937, UK PIDA, and France Sapin II/Waserman. See
  `legalcode-whistleblower-program-builder` for multi-jurisdiction analysis.

---

## Provenance

Created by Legalcode as a US-federal-specific variant of the multi-jurisdiction
`legalcode-whistleblower-program-builder`, developed 2026-03-22. Based on deep synthesis
of US statutory framework (SOX, Dodd-Frank, CFTC §748, OSHA statutes, False Claims Act,
AML Act of 2020, IRS §7623), SEC Office of the Whistleblower annual reports, DOJ ECCP
September 2024, SEC Rule 21F enforcement wave 2024-2025, NYSE/Nasdaq listing standards,
and _Digital Realty Trust v. Somers_ (2018) jurisprudential framework. Legalcode original
synthesis — not imported from external repository.
