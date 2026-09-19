---
name: legalcode-anti-bribery-compliance
description: 'Assess, build, or remediate an organization''s anti-bribery and anti-corruption (ABAC) compliance
  program against the major international regimes: US Foreign Corrupt Practices Act (FCPA) anti-bribery
  provisions, books-and-records, and internal controls requirements; UK Bribery Act 2010 including the
  Section 7 corporate offence and adequate procedures defense; France Sapin II (Law No. 2016-1691) mandatory
  compliance program obligations and Agence Française Anticorruption (AFA) guidelines; and Brazil Clean
  Company Act (Lei 12.846/2013). Use when reviewing an existing ABAC program for gaps, building a new
  program from scratch, preparing for regulatory examination or enforcement response, conducting third-party
  due diligence, drafting or reviewing gifts-and-entertainment policies, designing government-official
  interaction protocols, or evaluating a specific transaction or red flag for corruption risk.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Assess, build, or remediate an organization's anti-bribery and anti-corruption (ABAC) compliance program against the major international regimes: US Foreign Corrupt Practices Act (FCPA) anti-bribery provisions, books-and-records, and internal controls requirements; UK Bribery Act 2010 including the Section 7 corporate offence and adequate procedures defense; France Sapin II (Law No. 2016-1691) mandatory compliance program obligations and Agence Française Anticorruption (AFA) guidelines; and Brazil Clean Company Act (Lei 12.846/2013). Use when reviewing an existing ABAC program for gaps, building a new program from scratch, preparing for regulatory examination or enforcement response, conducting third-party due diligence, drafting or reviewing gifts-and-entertainment policies, designing government-official interaction protocols, or evaluating a specific transaction or red flag for corruption risk. Triggers on: "FCPA compliance," "UK Bribery Act," "Sapin II program," "anti-bribery," "anti-corruption," "adequate procedures," "third-party due diligence," "gifts and entertainment policy," "facilitation payments," "DOJ FCPA guidance," "SFO prosecution," "AFA audit," "government official interaction."


# Legalcode Anti-Bribery & Anti-Corruption Compliance

> **Disclaimer**: This skill provides a framework for AI-assisted anti-bribery compliance
> assessment. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional or compliance specialist licensed in the relevant jurisdiction
> before use. Laws, regulations, and enforcement guidance change; verify current applicability
> before relying on any provision described here. Statutory and regulatory references cited
> from training data carry hallucination risk — verify against authoritative sources including
> the DOJ, SEC, SFO, AFA, and CGU official publications before relying on them.

---

## Purpose and Scope

This skill assesses organizations' anti-bribery and anti-corruption (ABAC) compliance
programs, identifies gaps against four major regulatory regimes, and produces a
prioritized remediation roadmap.

**Covers:**

- Full ABAC program assessment across FCPA, UK Bribery Act 2010, Sapin II, and Brazil CCA
- Multi-regime gap analysis with jurisdiction-specific classification
- Third-party due diligence program review
- Gifts, entertainment, and hospitality policy assessment
- Government-official interaction protocol review
- Books, records, and internal controls assessment (FCPA)
- Adequate procedures analysis (UK Bribery Act)
- Mandatory program components audit (Sapin II / Brazil CCA)
- Transaction-specific corruption risk assessment
- Confidence-scored findings with Glass Box audit trail

**Does not:**

- Provide legal advice or replace qualified anti-corruption counsel
- Substitute for external forensic investigation or privilege-protected internal review
- Assess sanctions, export controls, or AML compliance (see dedicated skills)
- Apply exclusively to one jurisdiction — multi-regime with [JURISDICTION-SPECIFIC] markers

---

## Jurisdiction and Governing Law

This is a multi-jurisdiction skill covering four primary regimes with global extraterritorial
reach. Unlike contract-review skills, governing law is not determined by a single clause —
multiple regimes may apply simultaneously.

### Extraterritorial Reach Matrix

| Regime                | Territorial Scope                                                                                      | Key Trigger                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| **FCPA** (US)         | US persons and issuers everywhere; foreign companies with US nexus                                     | Use of US mail, bank, or territory; US person involvement; SEC registrant status |
| **UK Bribery Act**    | UK persons and companies everywhere; any company with UK business presence                             | Section 7: any commercial organisation doing business in the UK                  |
| **Sapin II** (France) | French companies ≥500 employees and €100M+ revenue worldwide; groups meeting thresholds at group level | AFA audit jurisdiction; group consolidation rule                                 |
| **Brazil CCA**        | Companies operating in Brazil; Brazilian companies globally                                            | Acts against Brazilian public administration                                     |

[JURISDICTION-SPECIFIC] For organizations operating in additional jurisdictions, supplement
this assessment with local counsel review of: OECD Working Group on Bribery member
country implementing legislation; EU Member State implementing legislation of the OECD
Convention; UN Convention Against Corruption (UNCAC) implementing laws; industry-specific
anti-corruption requirements (e.g., pharmaceutical, defense, natural resources).

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's context, the workflow pauses and asks when:

- The answer determines which regime(s) to apply or prioritize
- The organization's size or structure affects mandatory program requirements
- Risk tolerance or business context is needed to classify a finding correctly
- The mode of operation (build vs. assess vs. remediate) changes the deliverable

Use the **⟁ CLARIFY** pattern (structured options with descriptions) wherever marked below.
If the user has already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:

- **Existing program materials**: Policy documents, procedure manuals, training records,
  due diligence reports, board minutes, risk assessments, prior audit reports
- **Specific document or transaction**: A contract with a third-party intermediary, a
  proposed gift or hospitality request, a government tender, a red-flag notification
- **Verbal description**: Organization type, industry, jurisdictions, employee count,
  revenue, current program state
- **Investigation context**: A suspected bribery incident, a whistleblower report, a
  government inquiry or dawn raid

If no materials are provided, the workflow can still produce a gap assessment based on
the user's responses to the clarification questions below.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the assessment, ask these questions. Present structured
options where possible:

1. **Operating mode**: What is the primary objective?
   - **Build**: Draft a new ABAC program from scratch (produces a program blueprint and
     template policies)
   - **Assess**: Evaluate an existing program against regulatory requirements (produces a
     gap assessment and remediation roadmap)
   - **Remediate**: Focus on specific identified gaps or a recent incident/investigation
     (produces targeted remediation plan)
   - **Transaction screen**: Assess corruption risk for a specific transaction, acquisition,
     or third-party engagement (produces transaction-level red-flag analysis)
   - _Why this matters_: The workflow, deliverable format, and level of regulatory detail
     differ materially between these modes.

2. **Organization profile**: Which of these best describes the organization?
   - Large publicly traded company (US issuer or US person rule applies; SEC and DOJ FCPA
     jurisdiction likely; Sapin II may apply if French or French group)
   - Large private company (UK Bribery Act Section 7 and/or Brazil CCA may apply; Sapin II
     if French thresholds met)
   - Mid-size company (≥500 employees, ≥€100M revenue — Sapin II threshold; assess UK nexus)
   - SME / startup (UK Bribery Act applies but lighter-touch; FCPA applies if US person or
     US nexus; formal Sapin II not triggered but good-practice elements advisable)
   - Financial institution or professional services firm (additional sector-specific
     anti-corruption obligations may apply)
   - _Why this matters_: Determines which regimes create mandatory obligations vs.
     recommended best practices.

3. **Industry and risk profile**: What best describes the industry and operating environment?
   - High-risk sectors: natural resources, extractives, construction, infrastructure,
     defense/aerospace, pharmaceuticals, financial services, telecoms
   - Medium-risk sectors: manufacturing, technology, professional services, retail
   - Lower-risk sectors: domestic consumer goods, education, non-profit
   - Government contracting (primary)
   - Mixed (government and private sector)
   - _Why this matters_: Risk profile drives due diligence depth requirements and the
     adequacy of controls assessments.

4. **Jurisdictions of operation**: Which regions present the highest corruption exposure?
   - High-risk regions per FCPA/Transparency International: Sub-Saharan Africa, Southeast
     Asia, Central Asia, Eastern Europe, Middle East, Latin America (excluding Brazil/Chile/Uruguay)
   - Specific countries of concern (list)
   - Primarily domestic/low-risk jurisdictions only
   - _Why this matters_: Determines third-party due diligence depth, enhanced monitoring
     requirements, and specific red-flag protocols.

5. **Current program maturity**: Which best describes the existing ABAC program?
   - **None**: No formal ABAC program exists
   - **Nascent**: Basic code of conduct or policy exists but not operationalized
   - **Developing**: Policies exist, some training, limited monitoring
   - **Established**: Full program in place; seeking to assess against regulatory standards
   - **Mature**: Well-established program; targeted gap-fill or pre-examination review
   - _Why this matters_: The Build mode is appropriate for None/Nascent; Assess/Remediate
     for Developing through Mature.

6. **Trigger event** (if applicable): Is this assessment triggered by any of the following?
   - Regulatory inquiry, subpoena, or government investigation
   - M&A due diligence (pre-acquisition or post-acquisition integration)
   - Whistleblower report or internal hotline allegation
   - Voluntary disclosure consideration
   - Board or audit committee directive
   - Routine periodic assessment
   - No specific trigger
   - _Why this matters_: Regulatory inquiry or voluntary disclosure triggers counsel
     involvement and potentially privilege considerations before proceeding.

If partial context is provided, proceed with reasonable defaults and state assumptions
explicitly. Do not silently assume.

**⟁ CLARIFY** — If the trigger event includes a regulatory inquiry, government investigation,
or voluntary disclosure consideration, pause and advise:

> "Before proceeding with an AI-assisted assessment in the context of a regulatory inquiry
> or voluntary disclosure, consult with experienced anti-corruption counsel regarding
> privilege protections. Work product doctrine may not protect AI-assisted analyses from
> government disclosure. Retaining qualified counsel to direct this assessment may be
> advisable before generating written findings."

### Step 3: Determine Applicable Regimes

Based on the context gathered in Step 2, determine which regimes apply and their relative
priority for this organization.

#### Regime Applicability Decision Tree

**US FCPA applies if ANY of the following:**

- The organization is incorporated or has principal offices in the US
- The organization is an "issuer" (SEC registrant, including foreign private issuers)
- Any employee, officer, director, agent, or contractor is a US person (citizen, permanent
  resident, or entity incorporated under US law)
- The transaction used the US banking system, mail, or any means of US interstate commerce
- The organization has otherwise established a sufficient US nexus

**UK Bribery Act 2010 applies if:**

- The organization is incorporated in the UK or UK territory
- The organization carries on a business or part of a business in the UK (broad test —
  even a UK client or UK sales office may suffice under Section 7)
- Any individual bribery offence involves a UK person or UK territory

**Sapin II applies if:**

- The organization is a company (SA, SAS, SCA, SNC, SE, GIE) or a public establishment
- The organization (or its group on a consolidated basis) employs ≥500 persons AND has
  turnover ≥€100 million
- Note: The threshold assessment is at the group level — subsidiaries of large groups may
  be in scope even if individually below threshold

**Brazil Clean Company Act applies if:**

- The organization is incorporated under Brazilian law or operates in Brazil
- The acts targeted Brazilian government officials, agencies, or interests
- Note: Parent companies of Brazilian subsidiaries may face liability

**⟁ CLARIFY** — If the applicability of one or more regimes is unclear from the context
provided, ask the user specific questions (e.g., "Does the organization have any employees
who are US citizens or green-card holders?" or "Does the organization have any UK clients,
offices, or registered entities?") rather than making a blanket applicability determination.

### Step 4: Gather Legal Authority

Use **legalcode-mcp** to gather current regulatory authority for the applicable regimes.

**Research priorities:**

1. **FCPA** (if applicable):
   - DOJ/SEC FCPA Resource Guide (current edition) [VERIFY current version]
   - DOJ Corporate Enforcement and Voluntary Self-Disclosure Policy (current) [VERIFY]
   - SEC FCPA Unit guidance and recent enforcement releases
   - DOJ ECCP (Evaluation of Corporate Compliance Programs) — current version [VERIFY]
   - Recent FCPA enforcement actions in the organization's industry

2. **UK Bribery Act** (if applicable):
   - MoJ Six Principles Guidance on Adequate Procedures [VERIFY current]
   - SFO prosecution decisions and DPA reports
   - Current SFO corporate cooperation guidance
   - Recent SFO/CPS enforcement actions

3. **Sapin II** (if applicable):
   - AFA Recommendations (Recommandations de l'AFA) — current version [VERIFY]
   - AFA audit methodology and inspection reports
   - Judicial Convention d'Intérêt Public (CJIP) — recent examples
   - AFA annual report for enforcement trends [VERIFY year]

4. **Brazil CCA** (if applicable):
   - CGU Compliance Programme Integrity Guidelines (current) [VERIFY]
   - CADE cooperation agreements
   - Recent CGU/AGU enforcement decisions and leniency agreements

**Save research results** to `/tmp/legalcode-abac-authority.md` structured as:

```markdown
# ABAC Legal Authority Reference

## Date: [date]

## Regimes: [applicable regimes]

### FCPA Authority

- [Statute/guidance, key provision, relevance]

### UK Bribery Act Authority

- [Statute/guidance, key provision, relevance]

### Sapin II Authority

- [Statute/guidance, key provision, relevance]

### Brazil CCA Authority

- [Statute/guidance, key provision, relevance]

### Enforcement Trends

- [Recent actions, trends, industry focus areas]
```

**If legalcode-mcp is not connected:**

- Mark all regulatory citations with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with assessment using training-data knowledge; flag that all regulatory
  authority requires independent verification against current official sources

### Step 5: Program Gap Assessment

Assess the organization's ABAC program across the **Eight Core Pillars**. For each pillar,
evaluate against the compliance standards defined in the **Program Assessment Framework**
section below. Classify each element using the four-tier system in the **Compliance Status
Classification** section.

**⟁ CLARIFY** — For organizations in Build mode (no existing program), skip the gap
assessment and proceed to Step 6 (Program Blueprint). For Assess and Remediate modes,
continue through all eight pillars.

**⟁ CLARIFY** — For transaction-specific screens (Transaction Screen mode), skip to
Step 7 (Transaction Risk Analysis) directly.

Cover all Eight Pillars unless the user has specified a focused assessment:

| #   | Pillar                                    | Core Elements                                                                                                                         |
| --- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Risk Assessment**                       | Enterprise-wide corruption risk assessment; third-party risk profiling; geographic and industry risk mapping                          |
| 2   | **Policies and Procedures**               | ABAC policy; gifts/entertainment policy; government official interaction protocol; third-party policy; political contributions policy |
| 3   | **Leadership, Tone, and Governance**      | Board and C-suite commitment; Chief Compliance Officer (CCO) authority; ABAC oversight committee; board reporting                     |
| 4   | **Third-Party Due Diligence**             | Screening process; tiered due diligence; contractual protections; ongoing monitoring; termination procedures                          |
| 5   | **Training and Communication**            | Risk-based training curriculum; government-facing employee training; third-party training; attestation records; culture surveys       |
| 6   | **Internal Controls and Books & Records** | Payment controls; expense approval controls; invoice verification; accounting controls; no off-books accounts                         |
| 7   | **Monitoring, Auditing, and Testing**     | Compliance monitoring; internal audit coverage; transaction testing; whistleblower/hotline system; investigation protocol             |
| 8   | **Response and Remediation**              | Incident response; root cause analysis; disciplinary procedures; voluntary disclosure protocols; government cooperation framework     |

### Step 6: Program Blueprint (Build Mode Only)

For organizations in Build mode, produce a program blueprint based on the DOJ ECCP,
UK MoJ Six Principles, AFA Recommendations, and CGU Integrity Guidelines.

**⟁ CLARIFY** — Before drafting, confirm:

1. **Priority regime**: Which regime(s) should the blueprint prioritize?
   - FCPA-first (US focus)
   - UK Bribery Act-first (UK/global focus)
   - Sapin II-first (French legal obligation)
   - Multi-regime balanced design
   - _Why this matters_: While programs should be multi-regime where possible, mandatory
     Sapin II structures differ materially from FCPA "adequate procedures" design.

2. **Resource level**: What resources are available for program implementation?
   - Full team (CCO + compliance staff)
   - Lean team (compliance function shared with legal or HR)
   - Single-person function
   - External counsel + internal designee only
   - _Why this matters_: Blueprint complexity should match implementation capacity.

Produce a **Program Blueprint** covering all Eight Pillars with:

- What each element must contain at minimum
- DOJ ECCP / MoJ / AFA / CGU reference for each requirement
- Template policy language or structure (where applicable)
- Implementation sequencing (Phase 1 / Phase 2 / Phase 3)
- Resource and ownership recommendations

### Step 7: Transaction Risk Analysis (Transaction Screen Mode)

For transaction-specific screens, assess corruption risk using the **Red Flag Matrix** in
the Program Assessment Framework section.

**⟁ CLARIFY** — Gather transaction context:

1. **Transaction type**: What is the nature of the transaction or engagement?
   - Third-party intermediary engagement (agent, distributor, consultant, JV partner)
   - Government tender or procurement
   - M&A due diligence target
   - Acquisition of a government license, permit, or approval
   - Government contract performance
   - Other high-risk transaction

2. **Counterparty**: Who is the other party?
   - Company name, jurisdiction of incorporation, operating jurisdiction
   - Is any party a state-owned enterprise or government entity?
   - Does any beneficial owner hold a government position?
   - Is any introduction made through a government official contact?

3. **Red flags present**: Are any of the following present?
   - Unusual payment requests (cash, third-country account, nominee)
   - Excessive commission rates relative to services
   - No legitimate business rationale for the engagement
   - Counterparty lacks resources to perform the contracted services
   - Request for retroactive payments or "success fees" for government approvals
   - Government official facilitation of the contract award
   - Jurisdiction with endemic corruption risk (Transparency International CPI ≤40)

Assess against the **Red Flag Matrix** and produce a transaction-level risk classification:

- **LOW RISK**: Proceed with standard controls
- **ELEVATED RISK**: Enhanced due diligence required before proceeding
- **HIGH RISK**: Senior compliance or legal approval required; consider enhanced monitoring
- **PROHIBITED**: Transaction should not proceed without comprehensive legal review and
  potential voluntary disclosure consideration

### Step 8: Classify Findings

Classify each finding using the **Compliance Status Classification** (four-tier system
below). For CRITICAL DEFICIENCY findings, apply the **Self-Interrogation** framework
before finalizing classification.

For multi-regime organizations, classify each finding against each applicable regime
separately if the standards differ materially.

### Step 9: Generate Remediation Roadmap

For each NON-COMPLIANT and CRITICAL DEFICIENCY finding:

- Provide a specific, actionable remediation step
- Assign a timeline: IMMEDIATE / NEAR-TERM / BACKGROUND (per Prioritization Framework)
- Identify the responsible function (Legal/Compliance, HR, Finance/Accounting, IT, Business)
- Note any regulatory citation that informs the priority or specific action

For PARTIAL findings, provide enhancement recommendations with NEAR-TERM or BACKGROUND timelines.

**⟁ CLARIFY** — If the organization faces a regulatory inquiry or investigation, ask before
producing the roadmap whether to:

- **Include** voluntary disclosure considerations in the remediation steps
- **Exclude** voluntary disclosure content pending counsel guidance
- **Flag** areas where law-enforcement cooperation implications should be assessed

### Step 10: Quality Verification

Before delivering the assessment, run the **Quality Assurance Framework** checks:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every CRITICAL DEFICIENCY classification, run the 3-pass Self-Interrogation. Revise
   if any pass reveals a weakness.
3. Assign a Confidence Score to each significant finding.
4. Verify no JURISDICTION-SPECIFIC content has bled into the regime where it does not apply
   (e.g., do not state FCPA's facilitation payment exception applies under the UK Bribery Act).
5. Confirm that every policy or program element citation references the correct regime.

### Step 11: Deliver the Assessment

Produce output using the **Output Format Template** section. Append the Glass Box Audit
Trail to every deliverable.

---

## Program Assessment Framework

### Eight Pillars — Detailed Standards

#### Pillar 1: Risk Assessment

**COMPLIANT standard:**

- Enterprise-wide corruption risk assessment conducted within the past 2 years
- Assessment covers all geographies, business lines, and third-party relationships
- Risk factors documented: country risk (TI CPI), sector risk, transaction type risk,
  third-party risk, government interaction risk
- Assessment formally approved by senior management or board
- Risk assessment drives the rest of the program (risk-based approach documented)
- Updated when material changes occur (new market entry, acquisition, product change)

**FCPA standard (DOJ ECCP)**: Risk assessment should be "current," "thoughtful," and
reflect the organization's "business model and operations" [VERIFY current ECCP language].

**UK Bribery Act standard (MoJ Principle 3)**: "Due diligence" — the organisation assesses
the nature and extent of its exposure to potential external and internal risks of bribery.

**Sapin II standard (AFA)**: Cartographie des risques — mandatory for in-scope companies;
must be regularly updated; must identify, analyse, and prioritise corruption risks.

**Brazil CCA (CGU)**: Análise de perfil e riscos — risk assessment required for full
program credit in enforcement mitigation.

**Common gaps:**

- Assessment is generic ("we operate globally") rather than specific to actual business
- Assessment not updated after M&A, new market entry, or product change
- Assessment not formally approved or linked to actual program design
- Geographic risk assessment relies on perception indices only (no incident data)

---

#### Pillar 2: Policies and Procedures

**COMPLIANT standard — Core policies:**

| Policy                                       | Minimum Content                                                                                                                                                                                                        | FCPA        | UK BA       | Sapin II                                  | Brazil CCA |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------- | ----------------------------------------- | ---------- |
| **ABAC Policy**                              | Prohibition on bribery and corruption; coverage of all forms of benefit; third-party coverage; consequences; reporting channel                                                                                         | Required    | Required    | Required (Code of Conduct)                | Required   |
| **Gifts & Entertainment Policy**             | Per-person and per-year thresholds; pre-approval triggers; government official prohibition or enhanced rules; records requirement                                                                                      | Required    | Required    | Required                                  | Required   |
| **Government Official Interaction Protocol** | Definition of "government official" covering SOE employees; pre-approval for engagement; prohibition on facilitation payments [JURISDICTION-SPECIFIC: FCPA facilitation payment exception vs. UK absolute prohibition] | Required    | Required    | Required                                  | Required   |
| **Third-Party ABAC Policy**                  | Mandatory ABAC representations; due diligence requirements; right to audit; termination for breach                                                                                                                     | Required    | Required    | Required                                  | Required   |
| **Political Contributions Policy**           | Prohibition or strict limitation; pre-approval; no corporate funds for government official campaigns                                                                                                                   | Recommended | Recommended | Required (Sapin II lists as element)      | Required   |
| **Whistleblower/Speak-Up Policy**            | Anonymous reporting channel; no retaliation commitment; investigation protocol                                                                                                                                         | Recommended | Recommended | Required (Sapin II — dispositif d'alerte) | Required   |

[JURISDICTION-SPECIFIC — Facilitation payments]: Under the **FCPA**, narrow exceptions exist
for "facilitating payments" or "grease payments" to expedite routine governmental actions
(15 U.S.C. § 78dd-1(b)). This exception does NOT exist under the **UK Bribery Act 2010**,
**Sapin II**, or **Brazil CCA**. Organizations subject to UK or French law should have a
zero-tolerance facilitation payment policy. FCPA-only organizations may choose to include
or exclude the exception — but DOJ/SEC have signaled that companies claiming the exception
are increasingly scrutinized. Best practice is zero tolerance across all regimes.

**Common policy gaps:**

- Policy covers bribery only in one direction (paying bribes) but not receiving
- Gifts thresholds set too high relative to industry norms or regulator expectations
- Government official definition does not cover state-owned enterprise employees
- No specific government hospitality rules distinct from private-sector hospitality
- Facilitation payment policy inconsistent across regimes (FCPA exception stated globally)
- No record-keeping requirement for gifts/entertainment below the pre-approval threshold
- Third-party policy does not include right to audit or ABAC training obligation

---

#### Pillar 3: Leadership, Tone, and Governance

**COMPLIANT standard:**

- CEO/Board has made clear, public, documented commitment to anti-corruption
- CCO or equivalent ABAC function with direct board/audit committee access
- ABAC not solely delegated to a junior compliance officer without resources
- Board or audit committee receives ABAC-specific reporting (at least annually)
- Consequences for ABAC violations applied consistently, including to senior personnel
- Compliance officer compensation not tied to business revenue (independence)

**DOJ ECCP emphasis**: "Tone from the Top" AND "Middle Management Buy-In" — senior
management must communicate through conduct, not just policy [VERIFY current ECCP].

**UK MoJ Principle 2**: Top-level commitment — senior management is committed to
preventing bribery by associated persons and fosters a culture of integrity.

**Sapin II (AFA)**: Engagement de la direction — AFA has cited lack of documented board
commitment as a deficiency. CCO (or équivalent) must have resources and autonomy.

**Common governance failures:**

- Compliance function lacks budget to implement the program
- Board reports contain only positive metrics (no escalation of serious issues)
- Investigations into senior personnel are not handled independently
- "Tone from the top" exists in policy but is contradicted by business pressure

---

#### Pillar 4: Third-Party Due Diligence

**COMPLIANT standard:**

This is the **highest-risk area** for FCPA and UK Bribery Act enforcement — approximately
80-90% of FCPA enforcement actions involve third-party intermediaries.

**Tiered due diligence model:**

| Tier                  | Trigger                                                                                                                          | Minimum Due Diligence                                                                                                                        |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tier 1 — Baseline** | All third parties                                                                                                                | Sanctions/watch-list screening; ownership verification; ABAC certification/questionnaire                                                     |
| **Tier 2 — Enhanced** | Third parties with government interaction; high-risk jurisdictions; high-risk sectors; significant commission or fee structures  | All Tier 1 plus: business rationale documentation; compensation benchmarking; reference checks; ABAC clause in contract                      |
| **Tier 3 — Deep**     | Government intermediaries in high-risk countries; acquisition targets; joint-venture partners; politically exposed third parties | All Tier 2 plus: media and adverse information search; UBO verification; independent report; senior compliance approval; enhanced monitoring |

**Contractual protections required (Tiers 2 and 3):**

- ABAC representations and warranties
- Right to audit/inspect records
- Right to terminate for ABAC breach
- Flow-down obligation to sub-agents
- Certification of compliance

**Red flags requiring enhanced diligence or prohibition:**

- Third party introduced by or related to a government official
- Third party requests payments to offshore accounts or nominees
- Third party lacks apparent business capability for contracted services
- Commission rate significantly exceeds market norms for the services
- Engagement purpose is to "open doors" with a specific government agency
- Third party declines to certify ABAC compliance or provide ownership information
- Third party or beneficial owner is a current or former government official

**DOJ ECCP**: "Companies should undertake some form of risk-based due diligence to better
understand the qualifications and associations of those with whom the company does business"
[VERIFY current ECCP language].

**UK MoJ Principle 4**: Due diligence — the commercial organisation applies due diligence
procedures, taking a proportionate and risk-based approach, in respect of persons who
perform or will perform services for or on behalf of the organisation.

**Common third-party due diligence failures:**

- Screening only at onboarding; no periodic re-screening
- Tier 1 screening only (sanctions) for all third parties regardless of risk
- Absence of compensation benchmarking for government-facing intermediaries
- No review of sub-agent relationships used by primary intermediaries
- Contractual ABAC clause absent or generic (no specific right to audit)
- No defined process for terminating a third party on ABAC grounds

---

#### Pillar 5: Training and Communication

**COMPLIANT standard:**

- All employees receive initial ABAC training at onboarding and periodic refreshers
  (at least every 2 years for general population; annually for high-risk roles)
- High-risk employees (government-facing, procurement, finance, senior management,
  third-party relationship managers) receive enhanced, role-specific training
- Training addresses all applicable regimes, not just one
- Attestation of completion documented and retained
- Content is current (updated when law, policy, or risk profile changes)
- Third parties in Tier 2+ receive training or are required to certify their own ABAC training

**Sapin II (AFA)**: Dispositif de formation — required annual training for "exposed personnel"
(personnels les plus exposés aux risques de corruption); AFA has cited inadequate training
documentation as a recurring deficiency.

**Brazil CCA (CGU)**: Training and communication is a required element of an integrity
program for maximum credit in enforcement mitigation.

**Common training failures:**

- Training is generic (covers all compliance topics without ABAC specificity)
- High-risk employees receive the same training as general population
- Training delivered in wrong language for a local operating entity
- Completion records are not retained or are unverifiable
- Training content has not been updated to reflect new regulatory guidance
- Third-party training requirement exists in policy but is not verified or enforced

---

#### Pillar 6: Internal Controls and Books & Records

**FCPA-specific standards (15 U.S.C. § 78m(b)(2)(B)):**
The FCPA's internal controls provisions apply to issuers and require:

- Controls that provide reasonable assurance that transactions are authorized by management
- All transactions accurately and fairly reflected in books and records
- Access to company assets permitted only with management authorization
- Recorded accountability for assets compared with existing assets at reasonable intervals

**COMPLIANT standard — Anti-corruption controls:**

- No off-books accounts, slush funds, or unrecorded payments
- Expense reports supported by documentation and subject to supervisor approval
- Gifts and entertainment expense pre-approval for amounts above threshold
- Invoice verification — no payment without verified deliverables
- Cash payment controls — limits on cash disbursements; cash payments to government
  officials require senior approval
- Petty cash subject to ABAC controls
- Bank account controls — no accounts controlled solely by third parties
- Charitable donation controls — pre-approval for donations in jurisdictions where
  donations could be government-linked

**Common internal controls failures:**

- Expense management system does not flag government official entertainment separately
- Procurement controls do not require ABAC screening before vendor onboarding
- No reconciliation between approved payments and actual disbursements
- Petty cash is exempt from anti-corruption controls
- "Business development" expense category is poorly controlled
- Bonuses or commissions payable to third parties are not subject to ABAC review

---

#### Pillar 7: Monitoring, Auditing, and Testing

**COMPLIANT standard:**

- Regular compliance monitoring (not solely external audit)
- Internal audit covers ABAC program elements as part of annual audit plan
- Transaction testing: sample-based review of high-risk expense categories (gifts,
  entertainment, travel, consulting fees, third-party payments) in high-risk geographies
- Whistleblower/hotline system is operational, accessible, and anonymous
- All ABAC hotline reports are properly investigated and resolved
- Investigation protocol defines scope, investigator qualifications, documentation, and
  escalation triggers

**Sapin II (AFA)**: Dispositif de contrôle et d'évaluation interne — mandatory; AFA has
cited absence of internal controls testing as a recurring deficiency in inspection reports.

**DOJ ECCP on testing**: "The company should devote adequate staffing and resources to the
compliance function. The company should also assess whether its compliance resources match
its risk profile and whether a lack of compliance resources has resulted in compliance
gaps" [VERIFY current ECCP].

**Common monitoring failures:**

- Hotline is present but investigations are poorly documented
- Internal audit does not include ABAC-specific transaction testing
- Monitoring is reactive (responds to complaints) rather than proactive
- Monitoring program does not cover third-party payments or government-facing expenses
- No look-back review after new market entry or acquisition integration

---

#### Pillar 8: Response and Remediation

**COMPLIANT standard:**

- Investigation protocol with defined scope, trigger thresholds, investigator qualifications,
  documentation standards, and privilege considerations
- Root cause analysis conducted for every substantiated ABAC violation
- Disciplinary policy specifies that ABAC violations may result in termination, regardless
  of seniority
- Evidence that discipline has been applied consistently, including to senior personnel
- Voluntary disclosure framework: decision criteria, escalation path, legal/board review
- Post-incident program enhancements documented and tracked
- Government cooperation policy if applicable (deferred prosecution agreements, leniency)

**DOJ ECCP**: Incentivizes prompt reporting, full cooperation, and remediation; considers
whether the company has "taken remedial action, including disciplining wrongdoers" [VERIFY].

**Brazil CCA**: Leniency agreements (acordos de leniência) require full cooperation and
program remediation; CGU and AGU have authority to negotiate leniency.

**Sapin II**: CJIP (Judicial Convention d'Intérêt Public) — available for serious corruption
cases; requires AFA-monitored compliance program as a condition.

---

### Red Flag Matrix (Transaction Screen)

| Category                                    | Red Flag                                                                                          | Risk Level                                         | Action Required                                                    |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------ |
| **Third-party introduction**                | Third party introduced by government official or SOE employee                                     | HIGH                                               | Independent due diligence; legal review of compensation structure  |
| **Payment structure**                       | Payment to offshore account, nominee, or third-country beneficiary                                | HIGH                                               | Require explanation; default to prohibition unless justified       |
| **Compensation level**                      | Commission rate >5% for government procurement; >20% for any contract without clear justification | ELEVATED                                           | Benchmark against market; document justification; escalate         |
| **Business capability**                     | Third party lacks staff, office, or apparent ability to perform contracted services               | HIGH                                               | Require capability evidence; consider prohibition                  |
| **Timing**                                  | Payment requested immediately before or after government approval or contract award               | HIGH                                               | Pause transaction; conduct investigation                           |
| **Cash request**                            | Any request for cash payment, especially to a government official                                 | PROHIBITED                                         | Do not proceed; mandatory escalation to Legal/Compliance           |
| **Retroactive payments**                    | "Success fee" requested after government approval already obtained                                | HIGH                                               | Legal review required; presumptively prohibited                    |
| **Government official as beneficial owner** | Ultimate beneficial owner holds or recently held government position                              | ELEVATED-HIGH                                      | Enhanced due diligence; specific waiver process                    |
| **Unusual secrecy**                         | Counterparty declines to provide ownership information or sign ABAC certification                 | HIGH                                               | Do not proceed until resolved                                      |
| **Jurisdiction**                            | Transaction primarily in country with TI CPI ≤35                                                  | ELEVATED                                           | Enhanced due diligence; monitoring                                 |
| **Facilitation payment request**            | Any request to expedite routine government action through payment                                 | PROHIBITED (UK/FR/BR) / [VERIFY - restricted] (US) | Do not pay; escalate; consider reporting obligation                |
| **Charitable "donation" request**           | Charitable donation requested by government official in connection with deal                      | PROHIBITED                                         | Treat as potential bribe; do not proceed                           |
| **Political contribution request**          | Contribution requested by government official or in connection with government contract           | PROHIBITED                                         | Do not proceed; legal review                                       |
| **Lavish hospitality**                      | Hospitality exceeding policy limits offered to or requested by government official                | HIGH                                               | Pre-approval required; default to refusal for government officials |

---

## Compliance Status Classification

### Four-Tier System

Apply this classification to every program element assessed. The tiers are adapted from
the DOJ ECCP evaluation methodology and Sapin II AFA inspection framework.

#### COMPLIANT ✅

- Program element meets or exceeds the applicable regulatory standard
- Element is documented, current (updated within required cycle), and operationalized
  (not just written but practiced)
- Evidence of effectiveness: training records, due diligence files, monitoring reports
- Regulatory risk: **LOW** — element would not generate a finding in a standard government
  examination
- **Required action**: Maintain; document for use in regulatory examination or defense

#### PARTIAL ⚠️

- Program element exists but has identifiable, material gaps
- May be: outdated (beyond required refresh cycle); incomplete (missing required elements);
  not operationalized (written but not practiced); not tailored to actual risk profile
- Partial credit available in DOJ ECCP assessment and Brazil CGU integrity program
  evaluation; limited credit in AFA inspection
- Regulatory risk: **MODERATE** — would likely generate a recommendation or low-priority
  finding in examination; cited as deficiency if a violation occurs
- **Required action**: Near-term remediation with specific gap-fill plan

#### NON-COMPLIANT ❌

- Required program element is materially deficient; likely would not meet the minimum
  standard required by applicable law or regulatory guidance
- May be: significantly outdated; substantially incomplete; fundamentally not operationalized;
  not tailored to any meaningful degree; contradicted by actual conduct
- No credit available in enforcement proceedings absent substantial remediation
- Regulatory risk: **HIGH** — likely to generate a significant finding in examination;
  cited as aggravating factor in enforcement proceedings
- **Required action**: Immediate or near-term remediation; escalate to senior compliance
  or legal; consider whether a violation is ongoing

#### CRITICAL DEFICIENCY 🚨

- Required element is absent, completely non-functional, or actively undermined by
  organizational conduct
- For FCPA-covered issuers: may constitute a books-and-records or internal controls
  violation independent of any bribery (15 U.S.C. § 78m)
- For UK Bribery Act Section 7: absence of "adequate procedures" element undermines
  corporate defense
- For Sapin II in-scope companies: mandatory element completely absent; AFA inspection
  finding; potential referral to PNF (Parquet National Financier)
- Regulatory risk: **IMMEDIATE** — basis for enforcement action; potential personal
  liability for CCO or responsible officer
- **Required action**: Escalate immediately to CCO and General Counsel; halt problematic
  activity pending remediation; consider voluntary disclosure; brief board

---

## Regime-Specific Assessment Standards

### FCPA Books, Records, and Internal Controls (15 U.S.C. § 78m)

**Applicable to**: All SEC issuers (US and foreign private issuers); effectively extends
to all subsidiaries through the "issuer" definition.

**Core requirements** [VERIFY against current SEC enforcement guidance]:

1. **Books and Records**: The issuer shall make and keep books, records, and accounts
   that, in reasonable detail, accurately and fairly reflect the transactions and
   dispositions of the assets of the issuer.
   - "Reasonable detail" standard — not perfect accuracy but proportionate to the
     transaction
   - Record-keeping failures can constitute independent FCPA violations even without
     evidence of actual bribery

2. **Internal Controls**: The issuer shall devise and maintain a system of internal
   accounting controls sufficient to provide reasonable assurance that:
   - Transactions are executed only with management authorization
   - Transactions are recorded to permit preparation of GAAP financial statements
   - Access to assets only with management authorization
   - Recorded accountability for assets compared with actual assets at reasonable intervals

**DOJ ECCP assessment factors** [VERIFY current edition]:

- Is the compliance function "adequately resourced and empowered to function effectively"?
- "Has the company taken steps to ensure that the compliance and ethics function has the
  appropriate authority within the organization?"
- Are compliance personnel "compensated and promoted in ways that encourage the compliance
  function"?

---

### UK Bribery Act 2010 — Adequate Procedures

**Applicable to**: Any commercial organisation (formed in the UK or carrying on business
in the UK) under Section 7 (failure to prevent bribery).

**Six Principles (MoJ Guidance)** — each must be evidenced:

| Principle                       | Key Requirement                                                                    | Common Failures                                                      |
| ------------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **1. Proportionate Procedures** | Procedures proportionate to bribery risks faced                                    | Procedures not tailored to actual risk; one-size generic policy      |
| **2. Top-Level Commitment**     | Senior management committed to preventing bribery; culture of integrity            | Policy exists but senior management behavior contradicts it          |
| **3. Risk Assessment**          | Regular and thorough assessment of exposure to bribery risks                       | Assessment not updated; not tied to program design                   |
| **4. Due Diligence**            | Proportionate risk-based due diligence on persons associated with the organisation | Screening only; no enhanced diligence for high-risk third parties    |
| **5. Communication**            | Policies communicated and embedded across the organisation                         | Training completed but not role-specific; not reaching third parties |
| **6. Monitoring and Review**    | Monitoring and review of procedures; improvements where necessary                  | Monitoring is reactive only; no proactive testing                    |

**Section 7 corporate offence elements** [VERIFY]:

- A "person associated" with the commercial organisation bribes another person
- The bribery is intended to obtain or retain business or a business advantage for the
  commercial organisation
- Defence: organisation had "adequate procedures" in place to prevent bribery

---

### Sapin II — Mandatory Program Components

**Applicable to**: Companies (and groups on consolidated basis) ≥500 employees and
≥€100M annual revenue.

**Eight mandatory components (AFA Recommendations)** [VERIFY current AFA recommendations]:

| Component                                          | AFA Requirement                                                          | Key Points                                                                            |
| -------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| **1. Code of Conduct (Code de conduite)**          | Document defining prohibited behaviours; aligned with legal obligations  | Must be updated and integrated into internal regulations                              |
| **2. Internal Alert System (Dispositif d'alerte)** | Employees can report breaches; whistleblower protection                  | Must comply with Waserman Law (loi Waserman, 2022) whistleblower protections [VERIFY] |
| **3. Risk Mapping (Cartographie des risques)**     | Regular identification, analysis, and prioritisation of corruption risks | Must reflect actual business activities; updated regularly                            |
| **4. Third-Party Evaluation Procedures**           | Assessment of major clients, first-tier suppliers, intermediaries        | Proportionate to identified risks; documented                                         |
| **5. Accounting Controls**                         | Designed to detect and prevent corruption risks in accounting            | Specific to corruption risks, not general financial controls                          |
| **6. Training (Formation)**                        | For "exposed personnel" (personnels les plus exposés)                    | Annual; role-specific; documented completion                                          |
| **7. Disciplinary Regime**                         | Internal sanctions for ABAC breaches                                     | Must be documented and consistently enforced                                          |
| **8. Internal Controls and Evaluation**            | Controls to assess and evaluate corruption risk management measures      | Regular assessment; documented results; continuous improvement                        |

**AFA enforcement**: AFA can impose financial sanctions: up to €200,000 for natural persons,
€1,000,000 for legal persons; sanctions published on AFA website [VERIFY current limits].

**CJIP (Convention Judiciaire d'Intérêt Public)**: French equivalent of DPA — available for
corruption, influence peddling, and related offences. Requires AFA-monitored compliance
program as standard condition [VERIFY].

---

### Brazil Clean Company Act — Integrity Program Elements

**Applicable to**: Legal entities (national or foreign) incorporated under Brazilian law
or operating in Brazil for acts against Brazilian public administration.

**CGU Integrity Program Pillars** [VERIFY current CGU guidelines]:

| Pillar                                   | Core Elements                                                               | Mitigation Credit                               |
| ---------------------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------- |
| **Commitment and Support of Leadership** | Formal board resolution; executive compliance champion; resources allocated | Foundation — no credit without this             |
| **Policies and Code of Conduct**         | Anti-corruption policy; code of ethics; gifts/hospitality policy            | Required                                        |
| **Risk Assessment**                      | Documented corruption risk analysis; updated periodically                   | Required for substantial credit                 |
| **Training and Communication**           | Anti-corruption training for employees; communication campaigns             | Required                                        |
| **Internal Controls**                    | Financial controls; payment procedures; anti-circumvention                  | Required                                        |
| **Third-Party Due Diligence**            | Screening and evaluation of business partners                               | Required for sectors with high third-party risk |
| **Monitoring and Auditing**              | Internal audit; independent verification; testing                           | Required                                        |
| **Incident Response**                    | Investigation protocol; whistleblower protections; disciplinary process     | Required                                        |

**Leniency Agreement (Acordo de Leniência)**: Available through CGU/AGU; requires full
cooperation, disgorgement, and implementation of an integrity program; can reduce fines
by up to 2/3 and eliminate certain reputational sanctions [VERIFY].

---

## Gifts and Entertainment Policy Assessment Framework

### Policy Element Checklist

| Element                                  | COMPLIANT Standard                                                                                                                | Common Deficiency                                                           |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Government official definition**       | Covers foreign and domestic officials; SOE employees; employees of international organizations; family members acting as nominees | Does not cover SOE employees; does not cover foreign officials              |
| **Government official per-gift limit**   | Zero or near-zero (many FCPA consent agreements use $0 or de minimis); UK SFO expects very low limits for government officials    | No separate lower limit for government officials vs. private sector         |
| **Private sector per-gift limit**        | Proportionate; common range $50-$250 per gift; annual limit per recipient                                                         | No annual limit; per-gift limit only                                        |
| **Entertainment limits**                 | Pre-approval above threshold; business purpose requirement; no "quid pro quo" conditioning                                        | No distinction between government official entertainment and private sector |
| **Prohibited items**                     | Cash; cash equivalents (gift cards); excessive hospitality; anything with "expectation of return"                                 | Cash equivalents not explicitly prohibited                                  |
| **Pre-approval trigger**                 | Defined monetary threshold; all government official hospitality; overseas travel for counterparties                               | Threshold not defined; self-approval allowed                                |
| **Record-keeping**                       | Records for all gifts/entertainment above de minimis; government official records for all amounts                                 | No records below pre-approval threshold                                     |
| **Facilitation payment prohibition**     | Zero tolerance (best practice) or FCPA exception with explicit limitation [JURISDICTION-SPECIFIC]                                 | No policy on facilitation payments; FCPA exception stated broadly           |
| **Third-party giving on company behalf** | Third parties prohibited from giving on company behalf without pre-approval                                                       | Third-party giving not addressed                                            |

### Industry-Specific Hospitality Considerations

[JURISDICTION-SPECIFIC] Certain industries face heightened scrutiny of hospitality practices:

- **Pharmaceuticals / Healthcare**: [JURISDICTION-SPECIFIC] May be subject to additional
  transfer-of-value reporting (e.g., Sunshine Act in US [VERIFY]; EFPIA Code in EU [VERIFY]).
  Sponsorship of medical education, conference funding, and physician hospitality face
  specific DOJ/SEC scrutiny in FCPA enforcement.
- **Defense**: Government procurement hospitality faces specific restrictions in many
  jurisdictions. US procurement integrity rules (FAR) impose limitations on gifts to
  procurement officials [VERIFY].
- **Natural Resources / Extractives**: Government interaction in extractive industries
  (mining, oil/gas, forestry) faces FCPA heightened scrutiny; community benefit payments
  and local content requirements must be structured to avoid "disguised bribery" risk.
- **Financial Services**: "Relationship banking" entertainment norms are inconsistent with
  FCPA/UK Bribery Act government official standards; differentiate clearly between
  private banking and government entity clients.

---

## Prioritization Framework

Prioritize remediation by regulatory exposure, legal risk, and operational urgency.

| Priority                     | Criteria                                                                                                                                                                                                                                    | Typical Timeline                                                                                                                         | Action |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **IMMEDIATE** (0-30 days)    | CRITICAL DEFICIENCY; any element creating ongoing FCPA anti-bribery criminal exposure; active facilitation payment; government investigation triggered; voluntary disclosure window; Sapin II mandatory element absent in inspected company | Halt activity; escalate to GC/Board; engage external counsel; consider voluntary disclosure; notify auditors if public company           |        |
| **NEAR-TERM** (30-90 days)   | NON-COMPLIANT element; multiple PARTIAL findings in same pillar creating combined risk; third-party due diligence gaps in active high-risk markets; adequate procedures defense significantly weakened                                      | Assign named remediation owner; document corrective action plan with milestones; report to Board/Audit Committee; brief external counsel |
| **BACKGROUND** (90-180 days) | PARTIAL findings with no immediate enforcement risk; program enhancements beyond minimum compliance requirements; additional training rollouts; policy refresh cycles                                                                       | Include in annual program roadmap; assign ownership; set measurable targets                                                              |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise failures before delivery.

| Gate           | Rule                                                                                                                                                                                   | Fail Action                                              |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established guidance document                                                                                               | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction (e.g., US Code citation; UK Act section; French law number; Brazilian lei number)                          | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments, updates, or new guidance; FCPA Resource Guide, DOJ ECCP, and AFA Recommendations are updated periodically                                | Flag "[CHECK CURRENCY — may have been updated]"          |
| **Domain**     | Regime-specific rules are not stated as universal; FCPA facilitation payment exception not stated as applying under UK/FR/BR law; jurisdiction-specific standards correctly attributed | Remove or flag regime bleed                              |
| **Confidence** | Uncertainty explicitly stated; interpretive FCPA/UK Bribery Act/Sapin II positions qualified with confidence level                                                                     | Add confidence qualifier                                 |

### Self-Interrogation for Critical Deficiencies

For any element classified as CRITICAL DEFICIENCY, apply this 3-pass review before
delivering the assessment:

**Pass 1 — Regulatory Chain Integrity:**

- Does the CRITICAL DEFICIENCY classification follow logically from the cited regulatory
  requirement?
- Would an actual DOJ FCPA examiner, SFO investigator, AFA inspector, or CGU auditor
  make this finding on these specific facts?
- What specific statutory or guidance provision has been violated?
- Is there a compensating control that could reduce the severity to NON-COMPLIANT?

**Pass 2 — Completeness:**

- Have all relevant regulatory authorities been considered (not just one regime)?
- Is there a safe harbor, affirmative defense, or alternative compliance mechanism that
  could address the gap?
- Has the DOJ ECCP "credit for compliance" framework been applied to evaluate any
  partial mitigation?
- Are there facts not yet gathered that could change the classification?

**Pass 3 — Challenge:**

- What is the strongest argument that this element is actually NON-COMPLIANT or PARTIAL
  rather than CRITICAL DEFICIENCY?
- Under what circumstances would a regulator accept the current state?
- Is there compensating control evidence (monitoring results, audit findings, board minutes)
  that could reduce severity?
- Is this classification proportionate to the actual enforcement risk?

If any pass reveals a weakness, revise the classification before delivery. Mark the audit
trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

Assign a confidence score to every significant finding before delivery.

| Level        | Range     | Meaning                                                                                                           | Action                                                                     |
| ------------ | --------- | ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled regulatory requirement; specific statute or guidance provision confirmed; consistent enforcement practice | State with confidence                                                      |
| **High**     | 0.80-0.94 | Strong regulatory authority; minor interpretive questions; consistent with enforcement trends                     | State with brief caveat                                                    |
| **Probable** | 0.60-0.79 | Good regulatory authority but reasonable interpretations differ; FCPA/UK BA interpretive grey area                | State with explicit reasoning and identify counter-arguments               |
| **Possible** | 0.40-0.59 | Reasonable interpretation but significant uncertainty; no clear enforcement precedent                             | Flag for counsel review with both sides documented                         |
| **Unlikely** | 0.0-0.39  | Speculative; weak regulatory basis                                                                                | Do not assert; flag as "[UNCERTAIN — verify with anti-corruption counsel]" |

---

## Anti-Patterns Catalogue

What NOT to do in anti-bribery compliance program design, assessment, and enforcement response:

1. **Checkbox compliance, not risk-based design** — Building a program to satisfy a list
   of required elements without tailoring each element to the organization's actual risk
   profile. DOJ ECCP specifically asks whether the program is "designed to detect the
   particular types of misconduct most likely to occur in the company's line of business"
   [VERIFY]. An extractives company's program should look nothing like a domestic retail
   company's program.

2. **The facilitation payment blindspot** — Relying on the FCPA's facilitating payments
   exception without recognizing that (a) the exception does not apply under the UK
   Bribery Act, Sapin II, or Brazil CCA; (b) DOJ/SEC have significantly narrowed the
   practical scope of the exception in recent enforcement; (c) even within FCPA, the
   exception applies only to "routine governmental actions" and has never been affirmatively
   applied by DOJ/SEC to defeat an enforcement action. Best practice is zero tolerance.

3. **Ignoring state-owned enterprises** — Treating employees of state-owned enterprises
   (SOEs) as private sector counterparties. Under the FCPA, an SOE employee is a "foreign
   official" if the SOE is an "instrumentality" of a foreign government — a fact-intensive
   test but one courts have applied broadly. This is a recurring enforcement gap. Gifts,
   hospitality, and payments to SOE employees require government-official-level scrutiny.

4. **Third-party due diligence theater** — Conducting perfunctory database checks and
   calling it "due diligence." DOJ ECCP asks whether due diligence is "commensurate with
   the risks presented." A 5-minute OFAC search for a government-connected intermediary
   in a high-corruption country is not adequate procedures — and would not support the
   UK Bribery Act Section 7 defense.

5. **Ignoring sub-agents and sub-contractors** — Performing due diligence on the primary
   third party but ignoring sub-agents retained by that third party. FCPA enforcement has
   reached companies through multi-tiered agency relationships. The primary contract should
   require disclosure and flow-down of ABAC obligations to all sub-agents.

6. **Training completeness vs. training effectiveness** — Treating completion records as
   proof of training effectiveness. DOJ ECCP asks whether training is "effective" — not
   merely completed. Culture surveys, post-training assessments, and behavioral data
   (e.g., gifts/entertainment pre-approval rates) are evidence of effectiveness.

7. **Policy-practice divergence** — Having strong written policies that are not reflected
   in actual practice (e.g., a gifts policy with a €50 threshold, but expense reports
   showing regular entertainment at €300-500 per person with no pre-approval). This is
   evidence of deliberate non-compliance rather than mere gap — and is an aggravating
   factor in DOJ/SEC enforcement.

8. **Voluntary disclosure under-preparation** — Considering voluntary disclosure without
   first conducting a thorough internal investigation to understand full scope, isolating
   privilege-protected work product, and briefing Board and external counsel. Incomplete
   voluntary disclosure can be worse than no disclosure.

9. **Applying FCPA standards universally and forgetting UK/FR/BR obligations** — Many
   US-focused compliance teams assess compliance only under the FCPA and miss the more
   stringent requirements of the UK Bribery Act (no facilitation payment exception, broader
   "associated person" definition) and Sapin II (mandatory program components with AFA
   inspection authority, regardless of bribery having occurred).

10. **The "new management" defense** — Assuming that a change in leadership eliminates
    successor liability for prior ABAC violations. For M&A transactions, FCPA successor
    liability can extend to the acquirer for pre-acquisition conduct of the target. Robust
    pre-acquisition due diligence and post-acquisition integration are essential.

11. **Confusing anti-bribery with AML** — These are related but distinct regimes with
    different legal bases, regulators, and compliance requirements. Anti-bribery focuses
    on the act of paying; AML focuses on proceeds of crime. A company can have a strong
    AML program but a deficient ABAC program, and vice versa.

12. **Ignoring the "books and records" exposure** — Under the FCPA, a books-and-records
    or internal controls violation can be charged independently of any bribery. A company
    that "should have known" its third-party payments were improper may face books-and-records
    liability even without proof of actual bribery. Internal controls failures are frequently
    charged as standalone FCPA violations.

13. **Treating ABAC as a one-time implementation** — A compliance program is a living
    system. DOJ ECCP asks whether the company's program "has evolved" in response to
    lessons learned. Programs that have not been updated in 3+ years are inherently suspect,
    even if they were strong when originally built.

14. **Compliance without consequence** — Having an ABAC policy that is not enforced. DOJ
    specifically considers whether sanctions are applied consistently and without regard
    to seniority. A senior executive who violates the gifts policy and is not disciplined
    is evidence that the program is not effective.

15. **Inadequate investigation of red flags** — Receiving a hotline report or audit finding
    suggesting potential ABAC misconduct and failing to investigate promptly and thoroughly.
    Failure to investigate a known red flag is an aggravating factor in DOJ enforcement
    and may indicate willful blindness.

16. **Over-relying on reps and warranties** — Treating contractual ABAC representations
    from a third party as a substitute for due diligence. Reps and warranties shift
    contractual risk; they do not satisfy the FCPA's "knew or should have known" standard
    or the UK Bribery Act's adequate procedures test.

17. **Ignoring political contribution risks** — Political contributions to government
    officials or parties in connection with a business relationship can constitute bribery
    under FCPA, UK Bribery Act, and Sapin II. Many organizations lack specific controls
    on political contributions in foreign jurisdictions.

18. **Inadequate post-merger integration** — Acquiring a company with ABAC deficiencies
    and failing to integrate it into the acquirer's program promptly. DOJ has provided
    a safe harbor for voluntary disclosure and remediation of acquired-company violations
    within 1 year of acquisition [VERIFY current DOJ policy]. Failure to integrate
    is not eligible for this safe harbor.

19. **No independent channel for government official concerns** — Relying on normal
    management escalation for concerns involving government officials. Management may have
    conflicting business interests. An independent channel to Legal/Compliance (bypassing
    management) is essential for government-official-related concerns.

20. **Conflating "local norms" with legal permission** — "Everyone does it here" is not
    a defense to FCPA, UK Bribery Act, or Sapin II violations. Local cultural norms around
    gift-giving, hospitality, and relationship-building do not create a legal exception.
    Multi-national organizations must apply their program standards regardless of local
    custom.

---

## Localization Notes

This skill is jurisdiction-agnostic in structure but covers four specific regimes. When
adapting for additional jurisdictions:

1. **OECD member states implementing legislation**: Research the national implementing
   legislation for the OECD Anti-Bribery Convention in any jurisdiction where the
   organization operates. Most OECD members have criminalized bribery of foreign public
   officials under similar standards.

2. **EU Directive overlap**: The EU Anti-Money Laundering framework (AMLA) and related
   directives intersect with anti-corruption compliance in financial services contexts.
   Sapin II compliance does not substitute for AML compliance [VERIFY].

3. **Domestic bribery**: This skill focuses on foreign bribery (cross-border). Most
   jurisdictions also criminalize domestic bribery (bribery of domestic officials and
   commercial bribery). [JURISDICTION-SPECIFIC] Supplement with local counsel review for
   domestic bribery requirements, which may differ significantly from the four regimes covered.

4. **Chinese Anti-Corruption Law**: China's Criminal Law (Articles 389-393), NDRC
   regulations, and CPC anti-corruption rules apply to operations in China. These are
   not covered by this skill — engage specialist China counsel for PRC compliance [VERIFY].

5. **Industry-specific overlays**: Healthcare, defense, extractives, financial services,
   and telecommunications face sector-specific anti-corruption requirements in many
   jurisdictions. [JURISDICTION-SPECIFIC] These overlays must be assessed separately.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal authority source.

**With legalcode-mcp connected (preferred):**

- Search for current DOJ FCPA Resource Guide, ECCP guidance, and recent enforcement
  releases relevant to the organization's industry
- Retrieve current SFO prosecution guidance and UK Bribery Act case law
- Search for current AFA Recommendations (French language; current edition) and CJIP
  precedents
- Verify current CGU Integrity Program guidelines and Brazilian leniency precedents
- Search for Transparency International CPI data and OECD Working Group reports for
  relevant jurisdictions
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all regulatory citations with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus assessment on structural program gaps rather than regulatory citation depth
- Recommend that the user independently verify all statutory and guidance citations against
  current DOJ, SEC, SFO, AFA, and CGU official publications before relying on findings

---

## Writing Standards

Apply these standards to all ABAC compliance assessment deliverables:

1. **Precision over generality**: Write "The organization's third-party due diligence
   procedure does not require compensation benchmarking for government-facing intermediaries"
   rather than "third-party due diligence may need improvement."

2. **Regime attribution**: Every finding must specify which regime's standard it is
   assessed against. Do not conflate FCPA standards with UK Bribery Act standards
   — they differ materially in several areas.

3. **Regulatory citation**: Every CRITICAL DEFICIENCY and NON-COMPLIANT finding must cite
   the specific statutory provision, guidance document, or enforcement precedent it is
   assessed against.

4. **Severity language alignment**: CRITICAL DEFICIENCY findings must use urgent language.
   PARTIAL findings must not be overstated as NON-COMPLIANT. Proportionality matters
   — overstated findings erode credibility; understated findings create legal risk.

5. **Actionable remediation**: Every finding must include a specific remediation action
   with a suggested timeline (IMMEDIATE / NEAR-TERM / BACKGROUND). "Improve the program"
   is not actionable — "draft and implement a tiered third-party due diligence procedure
   within 60 days" is.

6. **Confidence qualification**: Any regulatory interpretation that is not settled law
   must be qualified with the applicable confidence level and a recommendation to verify
   with qualified anti-corruption counsel.

7. **[VERIFY] discipline**: Mark every statutory or regulatory citation that has not been
   independently verified against current authoritative sources. The DOJ ECCP, AFA
   Recommendations, and CGU guidelines are updated periodically.

8. **Tone**: Findings should be factual and professional — neither alarmist nor dismissive.
   The goal is to help the organization understand and remediate its risk, not to create
   unnecessary alarm or false reassurance.

9. **Plain language for executive summaries**: The executive summary must be understandable
   to a CEO or board member without legal training. Reserve technical language for the
   detailed findings sections.

---

## Output Format Template

### Cover Page

```
ANTI-BRIBERY & ANTI-CORRUPTION COMPLIANCE ASSESSMENT

Organization: [Name and jurisdiction]
Assessment Date: [Date]
Prepared by: AI-assisted — requires review by qualified anti-corruption counsel
Operating Mode: [Build / Assess / Remediate / Transaction Screen]
Regimes Assessed: [FCPA / UK Bribery Act / Sapin II / Brazil CCA — tick applicable]
Assessment Scope: [Full program / Targeted gaps / Transaction-specific]

PRIVILEGED AND CONFIDENTIAL — ATTORNEY-CLIENT COMMUNICATION [IF APPLICABLE]
[Include if directed by counsel; confirm with legal before adding this header]
```

---

### Executive Summary

```markdown
## Executive Summary

**Overall Program Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]
**Critical Deficiencies**: [N] findings requiring immediate action
**Non-Compliant Elements**: [N] findings requiring near-term remediation
**Partial Compliance**: [N] findings requiring enhancement
**Compliant Elements**: [N] elements meeting applicable standards

### Top 3 Priority Actions

1. [Most urgent finding — specific action, responsible function, and deadline]
2. [Second priority]
3. [Third priority]

### Regime Summary

| Regime                         | Overall Status | Key Gap            |
| ------------------------------ | -------------- | ------------------ |
| FCPA (if applicable)           | [status]       | [one-line summary] |
| UK Bribery Act (if applicable) | [status]       | [one-line summary] |
| Sapin II (if applicable)       | [status]       | [one-line summary] |
| Brazil CCA (if applicable)     | [status]       | [one-line summary] |
```

---

### Program Assessment — Eight Pillars

```markdown
## Program Assessment

### Pillar [N]: [Pillar Name]

**Overall Classification**: [COMPLIANT ✅ / PARTIAL ⚠️ / NON-COMPLIANT ❌ / CRITICAL DEFICIENCY 🚨]
**Confidence**: [0.X] — [one-line rationale]

| Element        | Status        | Regime(s)                | Finding            | Remediation       |
| -------------- | ------------- | ------------------------ | ------------------ | ----------------- |
| [Element name] | [✅/⚠️/❌/🚨] | [FCPA/UK BA/Sapin II/BR] | [Specific finding] | [Specific action] |

**Summary**: [2-3 sentences on overall pillar status and most significant finding]

[Repeat for each pillar assessed]
```

---

### Transaction Risk Analysis (if Transaction Screen mode)

```markdown
## Transaction Risk Analysis

**Transaction**: [Brief description]
**Counterparty**: [Name, jurisdiction]
**Transaction type**: [Third-party intermediary / Government procurement / M&A / Other]

### Red Flag Assessment

| Red Flag            | Present?             | Risk Level          | Detail                 |
| ------------------- | -------------------- | ------------------- | ---------------------- |
| [Red flag category] | [Yes / No / Unclear] | [HIGH/ELEVATED/LOW] | [Specific observation] |

### Overall Transaction Classification

**Risk Level**: [PROHIBITED / HIGH RISK / ELEVATED RISK / LOW RISK]
**Recommendation**: [Specific action — proceed / enhanced DD required / legal review / do not proceed]
**Conditions for proceeding** (if applicable): [List specific conditions]
```

---

### Remediation Roadmap

```markdown
## Remediation Roadmap

### IMMEDIATE (0-30 days)

| Finding   | Action            | Owner                                          | Regime(s) |
| --------- | ----------------- | ---------------------------------------------- | --------- |
| [Finding] | [Specific action] | [Legal / Compliance / Finance / HR / Business] | [Regime]  |

### NEAR-TERM (30-90 days)

| Finding | Action | Owner | Regime(s) |
| ------- | ------ | ----- | --------- |

### BACKGROUND (90-180 days)

| Finding | Action | Owner | Regime(s) |
| ------- | ------ | ----- | --------- |
```

---

### Glass Box Audit Trail

```yaml
glass_box:
  skill: "legalcode-anti-bribery-compliance"
  assessment_date: "[Date]"
  operating_mode: "[Build / Assess / Remediate / Transaction Screen]"
  organization_type: "[Public company / Private company / SME]"
  regimes_assessed:
    - FCPA: "[Applicable / Not applicable / Unclear]"
    - UK_Bribery_Act: "[Applicable / Not applicable / Unclear]"
    - Sapin_II: "[Applicable / Not applicable / Unclear]"
    - Brazil_CCA: "[Applicable / Not applicable / Unclear]"
  pillars_assessed: "[N of 8]"
  critical_deficiencies: "[N]"
  non_compliant: "[N]"
  partial: "[N]"
  compliant: "[N]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  external_tools_used: "[VERIFIED citations from legalcode-mcp / manual verification required]"
  quality_gates_status: "PASS / REVISED (specify which gates)"
  self_interrogation: "[PASS / REVISED] for each CRITICAL DEFICIENCY"
  confidence_qualifiers: "[Any findings marked POSSIBLE or UNLIKELY with caveats]"
  regime_bleed_check: "[Passed / Corrected — describe]"
  assumptions: "[Any explicit assumptions about organizational context]"
  limitations:
    - "Sapin II threshold applicability requires verification of consolidated headcount and revenue figures"
    - "FCPA applicability for non-issuer private companies may require specific nexus analysis by counsel"
    - "Transaction-specific assessments require full fact development before legal conclusions are drawn"
    - "All regulatory citations require verification against current official sources"
  generated_by: "AI-assisted assessment — requires review by qualified anti-corruption counsel"
  date_generated: "[Date]"
```

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis drawing on:

- US DOJ/SEC FCPA Resource Guide and Evaluation of Corporate Compliance Programs (ECCP)
- UK Ministry of Justice Guidance on Adequate Procedures (Bribery Act 2010)
- French AFA Recommendations (Recommandations de l'Agence Française Anticorruption)
- Brazilian CGU Integrity Programme Guidelines (Diretrizes sobre Programas de Integridade)
- Transparency International Corruption Perceptions Index methodology
- OECD Good Practice Guidance on Internal Controls, Ethics and Compliance
- Structural and quality frameworks adapted from `legalcode-contract-review` and
  `legalcode-aml-kyc-compliance` reference standards in the Legalcode repository

Attribution: Legalcode original synthesis. Not derived from any single third-party source.
All statutory and regulatory citations require verification against current authoritative
sources.
