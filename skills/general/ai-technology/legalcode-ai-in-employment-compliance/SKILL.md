---
name: legalcode-ai-in-employment-compliance
description: Assess and remediate compliance with laws governing AI and automated decision-making in employment
  and hiring contexts. Use when deploying, auditing, or advising on AI systems used for candidate screening,
  interviewing, hiring, promotion, compensation, workforce monitoring, or employee evaluation.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Assess and remediate compliance with laws governing AI and automated decision-making in employment and hiring contexts. Use when deploying, auditing, or advising on AI systems used for candidate screening, interviewing, hiring, promotion, compensation, workforce monitoring, or employee evaluation. Covers NYC Local Law 144 (automated employment decision tool (AEDT) bias audit by independent auditor, impact ratio calculation against EEO-1 categories, annual audit frequency, pre-use candidate and employee notice at least 10 business days before use, opt-out accommodation obligation, DCWP civil penalties up to $1,500 per day per violation); Colorado AI Act SB 24-205 (effective February 1, 2026 — high-risk AI consequential decision deployer obligations, impact assessment before deployment and annually thereafter, consumer interaction notice, appeal and human review rights on adverse consequential decisions, annual AG disclosure, $20,000 per affected consumer penalty, reasonable-care developer-reliance safe harbour); Illinois Artificial Intelligence Video Interview Act 225 ILCS 47 / 820 ILCS 42 (informed consent before video capture, AI function explanation before interview, data destruction within 30 days of request or 3 months after final hiring decision, third-party sharing prohibition, annual race-and-ethnicity demographic reporting to DCEO); Illinois HB 3773 effective January 1, 2026 (employer notice whenever AI influences any covered employment decision — hiring, promotion, discipline, termination — annual notice plus 30-day notice of new or substantially updated AI systems, IDHR enforcement under IHRA); California Civil Rights Council FEHA AI Regulations effective October 1, 2025 (anti-bias testing plan for all automated decision systems (ADS) used in employment decisions, mandatory documentation of testing process criteria and results, post-use notice obligations, 4-year record retention, applies to all FEHA-covered employers with 5+ California employees); California CPRA Automated Decisionmaking Technology Regulations 11 CCR 7200-7222 effective January 1, 2026 (pre-use notice content requirements for employment ADMT, opt-out from significant employment decisions, access rights, human review alternative, risk assessment under 11 CCR 7150-7157 with CPPA submission by April 1, 2028); Maryland § 3-717 employer facial recognition written consent waiver requirement before employment interviews (effective October 1, 2020); EU AI Act Regulation 2024/1689 Article 26 deployer obligations for Annex III Category 4 employment AI systems, Article 50 transparency to workers and applicants, prohibited practices under Article 5 including emotion recognition in employment contexts and prohibited biometric categorisation. Integrates EEOC May 2023 technical assistance on algorithmic hiring, Title VII disparate impact four-fifths rule applied to algorithmic selection rates, adverse impact documentation requirements, less-discriminatory-alternative analysis, ADA disability-screening risk in AI tools, ADEA age discrimination in algorithmic ranking, OFCCP obligations for federal contractors, and FCRA pre-adverse-action notice when AI tools process consumer report data. Produces multi-jurisdiction compliance matrix, employment-AI bias audit framework with fairness metric specifications, pre-use notice and disclosure templates for each applicable jurisdiction, opt-out and appeal procedure specifications, remediation roadmap prioritised by severity and regulatory deadline, and Glass Box audit trail suitable for legal counsel review, regulatory response, and board-level AI governance reporting.


# Legalcode AI-in-Employment Compliance

> **Disclaimer**: This skill provides a framework for AI-assisted compliance assessment of
> laws governing the use of AI in employment contexts. It does not constitute legal advice,
> regulatory compliance certification, or authorisation to deploy an AI system. All outputs
> require review by qualified employment law counsel and, where applicable, AI governance
> specialists before implementation. The laws covered — NYC Local Law 144, Colorado AI Act
> SB 24-205, the Illinois Artificial Intelligence Video Interview Act, the California CPRA
> ADMT Regulations, EU AI Act — are recent, actively evolving, and subject to ongoing
> regulatory interpretation and enforcement development. Effective dates, penalty amounts,
> and specific requirements may have been amended; verify current status before relying on
> any provision described here. EEOC guidance on AI tools is non-binding but represents
> agency enforcement position and carries significant risk weight. Statutory, regulatory,
> and guidance references cited from training-data knowledge carry hallucination risk —
> verify against authoritative primary sources before relying on them. Mark all
> unverified references **[VERIFY]**.

---

## Purpose and Scope

This skill assesses an organisation's compliance obligations when deploying, procuring, or
advising on AI systems that make or substantially assist employment decisions. It maps the
applicable legal framework by jurisdiction, identifies specific obligations for each law,
classifies compliance status, and produces actionable remediation guidance.

**Covers:**

- Jurisdictional applicability screening across all major AI-in-employment laws (US and EU)
- NYC Local Law 144 AEDT bias audit requirements (independent auditor, impact ratio, notice, publication)
- Colorado AI Act SB 24-205 deployer obligations for consequential AI employment decisions
- Illinois Artificial Intelligence Video Interview Act consent, destruction, and reporting requirements
- California CPRA Automated Decisionmaking Technology Regulations employment-context obligations
- Maryland employer facial recognition consent requirements
- EU AI Act Annex III Category 4 high-risk employment AI deployer obligations
- EEOC guidance on algorithmic hiring: Title VII disparate impact, four-fifths rule, adverse impact documentation
- Federal overlays: ADA, ADEA, FCRA, and OFCCP obligations triggered by AI employment tools
- Bias audit framework design: fairness metric specification, data requirements, audit frequency
- Pre-use notice and disclosure templates for each applicable jurisdiction
- Opt-out and appeal procedure design specifications
- Remediation roadmap prioritised by severity and regulatory deadline

**Does not:**

- Conduct the technical bias audit itself (see `legalcode-algorithmic-impact-assessment` for fairness
  metric methodology and quantitative analysis)
- Draft employment contracts or policies (see `legalcode-employment-agreement-review`)
- Build AI governance frameworks from scratch (see `legalcode-ai-governance-framework-builder`)
- Assess GDPR or general data protection obligations for AI systems (see `legalcode-dpia-generator`,
  `legalcode-cross-border-transfer-assessment`)
- Assess AI systems outside the employment context (see `legalcode-algorithmic-impact-assessment`
  for credit, housing, healthcare, and criminal justice AI)
- Provide legal advice or replace qualified employment law counsel

**Complementary skills:** Use this skill alongside:

- `legalcode-algorithmic-impact-assessment` — for technical fairness metric analysis when you have
  deployment data or model performance records
- `legalcode-ai-governance-framework-builder` — to build the broader AI governance programme of which
  employment-AI compliance is one pillar
- `legalcode-ccpa-admt-compliance` — for California ADMT compliance in non-employment consumer contexts
- `legalcode-ai-fundamental-rights-impact-assessment` — for EU AI Act Article 27 FRIA obligations

---

## Key Definitions

Understanding statutory definitions is essential because applicability turns on whether a system
qualifies under each jurisdiction's operative terms.

| Term                                           | Jurisdiction                 | Statutory Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Includes                                                                                                        | Excludes                                                                                                                                                            |
| ---------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Automated Employment Decision Tool (AEDT)**  | NYC Local Law 144            | Any "computational process, derived from machine learning, statistical modeling, data analytics, or artificial intelligence, that issues simplified output, including a score, classification, or recommendation, that is used to substantially assist or replace discretionary decision-making processes" in hiring or promotion                                                                                                                                                                                  | Scoring tools, ranking algorithms, personality/skills assessors, AI résumé screeners                            | Human-only decisions; tools that process input and display it unaltered without generating scores/classifications                                                   |
| **High-Risk AI System**                        | EU AI Act Annex III          | AI systems listed in Annex III, Category 4: "AI systems intended to be used for recruitment or selection of natural persons, notably for advertising vacancies, screening or filtering applications, evaluating candidates in the course of interviews or tests" and "AI systems intended to be used for making decisions on promotion and termination of work-related contractual relationships, for task allocation and for monitoring and evaluating performance and behavior of persons in such relationships" | AI hiring screeners, AI video interview analysis, AI performance monitoring, AI task allocation tools           | General-purpose AI tools not specifically designed for employment decisions; human HR decisions with no AI input                                                    |
| **Automated Decisionmaking Technology (ADMT)** | CA CPRA Regs 11 CCR 7200     | "Technology that processes personal information and uses computation as a substantial factor in making a decision or facilitating human decisionmaking that has a legal or similarly significant effect on a consumer"                                                                                                                                                                                                                                                                                             | Algorithmic scoring, profiling tools, automated ranking, AI recommendation systems                              | Human decisions that happen to use software to organise data without scoring or recommending; aggregated statistical analysis not used to make individual decisions |
| **Consequential Decision**                     | Colorado SB 24-205           | Decision that "has a material legal or similarly significant effect on a consumer" including employment, hiring, termination, compensation, and promotion decisions [VERIFY current statutory text]                                                                                                                                                                                                                                                                                                                | Hiring decisions, performance reviews affecting compensation, termination triggers, promotion assessments       | Aggregate analytics; decisions affecting only internal process efficiency without individual impact                                                                 |
| **Artificial Intelligence System**             | Illinois AIVIA (225 ILCS 47) | An automated system that "uses machine learning, statistical modeling, data analytics, or artificial intelligence to evaluate job applicants or employees" from video interview recordings [VERIFY current statutory text]                                                                                                                                                                                                                                                                                         | AI video interview analysis tools that evaluate facial expressions, tone, word choice, or biographical language | Non-AI video recording that does not evaluate candidates; human-reviewed video interviews                                                                           |

---

## Jurisdiction and Governing Law

This skill is jurisdiction-aware. Different employment-AI laws operate on different legal theories,
cover different tool types, impose different obligations, and carry different enforcement mechanisms.
Apply the Regulatory Stack Determination in Step 4 to identify which laws apply before proceeding.

**[JURISDICTION-SPECIFIC — NYC]**: NYC Local Law 144 applies if the employer uses an AEDT for
employment decisions affecting individuals who are employed in New York City, are applicants for
positions based in New York City, or whose applications are evaluated using the tool in connection
with employment in NYC. Enforcement body: NYC Department of Consumer and Worker Protection (DCWP).
Civil penalties: $375 per violation per day for first violation; up to $1,500 per violation per
day for repeat violations. [VERIFY current penalty schedule — may have been amended]

**[JURISDICTION-SPECIFIC — Colorado]**: SB 24-205 applies to deployers of high-risk AI systems that
make consequential decisions affecting Colorado residents, effective February 1, 2026. Enforcement
body: Colorado Attorney General. Private right of action: not provided; AG enforcement only.
[VERIFY effective date and current enforcement guidance]

**[JURISDICTION-SPECIFIC — Illinois]**: Illinois AIVIA (225 ILCS 47) applies to any employer (not
limited by size) that uses AI to analyse video interviews of candidates for positions anywhere the
employer hires — no geographic restriction to Illinois. Annual demographic data reporting required
to Illinois Department of Commerce and Economic Opportunity (DCEO). Civil penalties up to $500 per
violation (first); up to $1,500 per violation (subsequent). [VERIFY current penalty schedule]

**[JURISDICTION-SPECIFIC — California]**: CPRA ADMT Regulations (11 CCR 7200-7222) apply to covered
businesses (CPRA threshold: 100,000+ consumers annually or 50%+ revenue from data) that process
personal information of California residents using ADMT for significant employment-context decisions.
Effective January 1, 2026. CPPA risk assessment submission deadline: April 1, 2028. Enforcement:
California Privacy Protection Agency (CPPA) and California Attorney General.
[VERIFY: AB 331 legislative status — was pending as of early 2025; may have been enacted or
superseded by CPPA ADMT rulemaking]

**[JURISDICTION-SPECIFIC — Maryland]**: HB 1202 (2024 session) addresses employer use of facial
recognition technology in employment. [VERIFY current law — enactment status and specific
requirements as of 2026 require verification against Maryland Code]

**[JURISDICTION-SPECIFIC — EU]**: EU AI Act Regulation 2024/1689 Article 26 obligations for
deployers of high-risk employment AI apply from August 2, 2026 (for Annex III systems). Applicable
when: (a) deployer is established in the EU, or (b) AI system output is used in the EU affecting
EU-based individuals. Enforcement: national market surveillance authorities (e.g., German BNetzA,
French CNIL/ANSSI, Italian AGCM). Administrative fines: up to €15 million or 3% of global annual
turnover for deployer obligations violations. [VERIFY current EU AI Act guidance from EU AI Office]

**Federal (US)**: EEOC guidance applies to all US employers covered by Title VII (15+ employees),
ADA (15+ employees), ADEA (20+ employees). OFCCP applies to federal contractors and subcontractors.
FCRA applies when AI tools use consumer-report-derived data (background checks, credit checks).
These are not specifically AI laws but create liability when AI tools produce discriminatory outcomes.

---

## Interactive Clarification

This skill uses **interactive clarification** (⟁ CLARIFY) at key decision points. Rather than
proceeding with incorrect assumptions, the workflow pauses and asks when:

- Jurisdictional scope is unclear (which employees/applicants are affected and where)
- The employment decision type affects which obligations apply
- Tool characteristics (biometric data, video analysis, full automation vs. human-assisted) trigger
  different regulatory regimes
- Organisational risk tolerance affects how to classify borderline findings

Present clarification points as structured options with a brief explanation of why the answer
matters. If the user has already provided the information, skip the question and proceed.

For **non-interactive batch runs**, apply these defaults and state assumptions explicitly:

- Scope: The AI system affects US employees or candidates in NYC and California, and optionally EU
- Decision type: Hiring/candidate screening (most stringent obligations)
- Tool includes automated scoring or ranking: YES
- Biometric data: UNKNOWN (flag all biometric provisions as requiring verification)
- Playbook: None provided; use regulatory minimums as baseline

---

## Workflow

### Step 1: Accept Input

Accept the employment AI system description in any format:

- **System documentation**: Product spec, vendor documentation, model card, RFP, or contract
- **Procurement documents**: Vendor agreements, SOWs, or evaluation criteria
- **Pasted description**: Free-text description of what the AI system does, what data it uses, and
  what output it produces
- **Deployment record**: Existing deployment information, prior audit findings, or compliance gap analysis

At minimum, the assessment requires:

1. What the AI system does (what employment decision it supports)
2. What input data it uses (résumés, video, assessments, social data, work-history data)
3. What output it produces (score, ranking, classification, recommendation, rejection flag)
4. Which geographic markets are affected (US states and/or EU)

If insufficient information is provided, prompt the user for the minimum required inputs before
proceeding.

---

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user (skip questions already answered by the input):

1. **What is the decision type?**
   - Options: Candidate screening/hiring selection, Video interview analysis, Employee promotion
     or performance evaluation, Compensation or task allocation, Employee monitoring or productivity
     scoring, Multiple/combined, Other
   - _Why this matters_: Illinois AIVIA is triggered only by video interview AI. EEOC four-fifths
     rule thresholds vary by selection stage. EU AI Act Annex III Category 4 covers different
     sub-categories. The decision type determines which regulatory framework components apply.

2. **Does the tool use biometric data?**
   - Options: Yes — facial recognition or facial analysis, Yes — voice/audio analysis, Yes —
     behavioural biometrics (typing patterns, gaze tracking), No biometric data, Unknown/check vendor
   - _Why this matters_: Illinois AIVIA and Maryland law are triggered specifically by biometric/video AI.
     EU AI Act Article 5 contains specific prohibitions on biometric categorisation.

3. **Which geographic markets are in scope?**
   - Options: US only (specify states), EU only, US and EU, Global/multi-jurisdiction, Not yet determined
   - _Why this matters_: NYC LL 144 applies only to NYC employment. Illinois AIVIA applies wherever
     Illinois candidates are screened. Colorado SB 24-205 applies to Colorado residents from
     February 1, 2026. EU AI Act applies from August 2, 2026 for Annex III systems.

4. **Is the decision fully automated or human-assisted?**
   - Options: Fully automated (AI decision final, no human review), Human-assisted (AI scores; human
     decides), Human-in-the-loop (AI recommends; human must confirm), Human oversight (AI flags;
     human reviews flagged items only)
   - _Why this matters_: Colorado SB 24-205 and California CPRA ADMT both require opt-out from
     **solely automated** consequential decisions. EU AI Act Article 26 requires human oversight
     mechanisms. The automation level affects what remediation controls are required.

5. **Does the organisation have an AI employment compliance playbook?**
   - Options: Yes — provide path or paste it, No — use regulatory minimums as baseline, In development
   - _Why this matters_: A playbook defines the organisation's risk tolerance, internal bias
     thresholds, vendor qualification criteria, and escalation paths. Without one, this assessment
     uses regulatory minimums.

---

### Step 3: Load Organisational Playbook

Attempt to load the organisation's AI employment compliance playbook. If available, extract:

- **Bias threshold policy**: Acceptable impact ratio / adverse impact threshold (e.g., "flag any
  group below 85% of highest selection rate" vs. the statutory 80%)
- **Protected characteristics scope**: Characteristics assessed beyond legal minimum (e.g., disability
  status, parental status, veteran status, beyond EEO-1 sex/race/ethnicity)
- **Audit frequency**: Annual (statutory minimum), quarterly, per-cohort, or continuous
- **Vendor qualification criteria**: What auditor independence standards apply
- **Escalation matrix**: When does a compliance finding reach legal, CHRO, CEO, or board
- **Risk tolerance**: Conservative / Balanced / Aggressive

If no playbook is provided:

```
⚠️ No organisational playbook provided. This assessment uses regulatory minimums as the
baseline. All thresholds and standards reflect the minimum required by law; they are not
organisational risk positions. Where regulatory requirements are absent or unclear, this
assessment will note the gap and recommend that counsel establish an internal standard.
```

---

### Step 4: Determine Regulatory Stack

For each jurisdiction, evaluate whether the law applies to this deployment:

| Jurisdiction                                | Trigger Conditions                                                                                         | Effective Date                                   | Enforcement Body                         |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ---------------------------------------- |
| **NYC Local Law 144**                       | AEDT used in hiring or promotion of NYC-based employees or candidates                                      | Effective July 5, 2023; enforcement ongoing      | NYC DCWP                                 |
| **Colorado SB 24-205**                      | High-risk AI consequential employment decision affecting Colorado residents                                | February 1, 2026 [VERIFY]                        | Colorado AG                              |
| **Illinois AIVIA** (820 ILCS 42)            | AI used to analyse video interviews of job candidates                                                      | January 1, 2020; amended 2023                    | IDES / state AG                          |
| **Illinois HB 3773**                        | AI influences any hiring, promotion, discipline, or termination decision                                   | January 1, 2026                                  | IDHR (Illinois Human Rights Act)         |
| **California FEHA AI Regulations**          | ADS used in employment decisions affecting California residents; all FEHA-covered employers (5+ employees) | October 1, 2025                                  | California Civil Rights Dept.            |
| **California CPRA ADMT** (11 CCR 7200-7222) | Covered business (100K+ consumers) using ADMT for significant decisions affecting California residents     | January 1, 2026                                  | CPPA / CA AG                             |
| **Maryland § 3-717**                        | Employer using facial recognition during employment interviews                                             | October 1, 2020                                  | Civil litigation / state AG              |
| **EU AI Act Art. 26**                       | Deployer of Annex III Category 4 employment AI established in EU, or affecting EU-based workers/candidates | August 2, 2026 (Annex III high-risk provisions)  | National market surveillance authorities |
| **EEOC / Title VII**                        | US employer with 15+ employees using AI in employment decisions                                            | Always applicable (Title VII enacted 1964)       | EEOC / federal courts                    |
| **ADA**                                     | US employer with 15+ employees; AI system may screen out individuals based on disability-related features  | Always applicable                                | EEOC / federal courts                    |
| **ADEA**                                    | US employer with 20+ employees; AI system may rank/penalise age-correlated features                        | Always applicable                                | EEOC / federal courts                    |
| **OFCCP**                                   | Federal contractor/subcontractor using AI in employment decisions                                          | Always applicable (for covered contractors)      | OFCCP                                    |
| **FCRA + CFPB Circular 2024-06**            | AI tool generates background dossiers, algorithmic scores, or uses consumer report data                    | Always applicable when consumer reports involved | FTC / CFPB / state AGs                   |

**Output**: Produce a Regulatory Stack Table confirming which laws are triggered, with brief
rationale, effective dates, and enforcement bodies. Flag any laws where applicability is uncertain
and requires factual verification.

---

### Step 5: Gather Legal Authority

**With legalcode-mcp connected (preferred):**

Search for current regulatory guidance on each applicable jurisdiction's law. Priority queries:

- "NYC Local Law 144 AEDT bias audit requirements 2025 2026 DCWP enforcement"
- "Colorado SB 24-205 AI Act high-risk AI employment deployer obligations guidance"
- "Illinois Artificial Intelligence Video Interview Act 2023 amendment requirements"
- "California CPRA ADMT regulations employment 11 CCR 7200 2026"
- "EEOC AI algorithmic hiring Title VII four-fifths rule 2023 technical assistance"
- "EU AI Act Article 26 deployer obligations employment Annex III Category 4"

Save most relevant results to `/tmp/employment-ai-compliance-research.md`. Mark each citation
as VERIFIED when drawn from official primary sources via legalcode-mcp.

**Without legalcode-mcp:**

Proceed with training-data knowledge. Mark all statutory and regulatory citations [VERIFY].
Include in the Glass Box audit trail: `legalcode_mcp: "Not connected — citations require
independent verification"`. Provide this verification checklist for the user:

- [ ] NYC DCWP official Local Law 144 page and enforcement updates
- [ ] Colorado AG office SB 24-205 implementation guidance
- [ ] Illinois DCEO AI Video Interview Act guidance and reporting portal
- [ ] California CPPA ADMT Regulations full text (11 CCR 7200-7222) and FAQ
- [ ] EEOC May 2023 Technical Assistance Document on AI employment tools
- [ ] EU AI Office guidance on Annex III deployer obligations

---

### Step 6: NYC Local Law 144 Compliance Assessment

**Applies when:** Tool is an AEDT used for hiring or promotion of NYC-based employees or applicants.

#### 6.1 Applicability Threshold

**⟁ CLARIFY if uncertain**: Does the tool "substantially assist or replace discretionary
decision-making" by issuing a score, classification, or recommendation? Or does it merely
organise/display inputs without scoring candidates? The NYC DCWP has indicated that tools
that simply aggregate résumé data without ranking or scoring do not trigger LL 144; tools
that generate applicant scores or recommended shortlists do.

#### 6.2 Annual Independent Bias Audit Requirements

**Regulatory basis**: NYC Local Law 144 §8-f, NYC Administrative Code [VERIFY current codification]

**Assessment checklist:**

- [ ] Has an independent bias audit been conducted within the past 12 months?
- [ ] Is the auditor genuinely independent? (not employed by the employer, not the tool
      developer, no financial conflict of interest) [VERIFY DCWP independence definition]
- [ ] Does the audit cover all protected categories: **sex** (binary as per EEO-1 categories),
      **race/ethnicity** (EEO-1 7 categories: Hispanic or Latino; White; Black or African American;
      Native Hawaiian or Other Pacific Islander; Asian; American Indian or Alaska Native;
      Two or More Races), and **intersectional categories** (sex × race/ethnicity)?
- [ ] Does the audit calculate the **impact ratio** for each protected category?
      Impact ratio = (selection rate for group) ÷ (selection rate for group with highest rate)
- [ ] Are there at least **2% of the total candidate/employee pool** in each category for which
      impact ratios are reported? (Groups below 2% threshold may be excluded but must be noted)
- [ ] Is the audit methodology documented (data sources, time period, testing approach)?
- [ ] Do all reported impact ratios meet or exceed **0.80** (four-fifths rule threshold)?
      Any ratio below 0.80 should trigger a remediation review.

**Four-fifths rule application:**

```
Impact Ratio = [selection rate of assessed group] ÷ [selection rate of highest group]
Threshold:  ≥ 0.80 = generally acceptable
            0.70–0.79 = monitor; document business justification
            < 0.70 = significant adverse impact; remediation required
```

#### 6.3 Bias Audit Summary Publication Requirements

**Assessment checklist:**

- [ ] Is the bias audit summary published on the employer's website (or clearly linked from it)?
- [ ] Does the published summary include: (a) date of audit, (b) description of the data used,
      (c) impact ratios for each category, (d) overall scoring/classification method of the AEDT?
- [ ] Has the summary been maintained on the website for at least **12 months** from publication?
- [ ] If the most recent audit is over 12 months old, is a new audit scheduled?

#### 6.4 Pre-Use Notice to Candidates and Employees

**Assessment checklist:**

- [ ] Are candidates notified **at least 10 business days** before the AEDT is used to assess them?
- [ ] Does the notice disclose: (a) that an AEDT will be used, (b) the characteristics or
      categories of data the AEDT will use to assess them, (c) the type of role for which the AEDT
      is being used?
- [ ] Is a mechanism available for candidates to **request an accommodation or alternative process**
      and is this prominently communicated in the notice?
- [ ] Is the notice accessible and provided in a format the candidate can retain?

#### 6.5 Opt-Out and Alternative Selection Process

**Assessment checklist:**

- [ ] Is an **alternative selection process** available to candidates who request one?
- [ ] Is the alternative process genuinely comparable (produces a substantive hiring assessment;
      not a dead-end)? [VERIFY DCWP guidance on adequacy of alternative processes]
- [ ] Are requests for alternatives processed without disadvantaging the requestor?

---

### Step 7: Colorado AI Act SB 24-205 Compliance Assessment

**Effective date**: February 1, 2026 [VERIFY]
**Applies when**: Deployer uses a high-risk AI system making consequential employment decisions
affecting Colorado residents.

#### 7.1 Applicability Determination

**⟁ CLARIFY**: Is the organisation a **deployer** (uses a third-party AI developer's system) or a
**developer** (creates the AI system for its own or others' use)? Deployer and developer obligations
differ under SB 24-205. Employers who buy or license AI tools from a vendor are deployers.

#### 7.2 Deployer Obligations Checklist

**Assessment checklist:**

- [ ] Has the deployer conducted a **deployer-side impact assessment** before deployment?
      (Note: SB 24-205 permits deployers to rely on developer's impact assessment documentation
      if the developer provides it — verify whether vendor has provided adequate documentation)
- [ ] Does the deployer have a **risk management policy** aligned with a recognised framework
      (NIST AI RMF 1.0 or similar)? [VERIFY SB 24-205 §6-1-1703(2)(a) requirements]
- [ ] Is there a mechanism to **notify consumers (applicants/employees)** when a high-risk AI
      system makes or substantially contributes to a consequential employment decision about them?
- [ ] Does the notification include: (a) the fact that AI was used, (b) the AI's role in the
      decision, (c) information about how to seek review or appeal?
- [ ] Is an **opt-out mechanism** available for applicants/employees from solely automated
      consequential decisions?
- [ ] Is there a **human review** option available upon request for consequential decisions?
- [ ] Does the deployer make an **annual disclosure** to the Colorado Attorney General summarising:
      high-risk AI systems deployed, types of consequential decisions made, and the impact assessment?
      [VERIFY annual disclosure form and deadline]
- [ ] If the deployer relies on the developer's documentation for the impact assessment, has
      the deployer independently verified that the developer's documentation is adequate and
      current? [VERIFY SB 24-205 developer-reliance safe harbour conditions]

---

### Step 8: Illinois Artificial Intelligence Video Interview Act Compliance Assessment

**Applies when**: Employer uses AI to analyse video interviews of job applicants (regardless of
where the employer is located or where the applicant is based).

#### 8.1 Pre-Interview Consent and Disclosure Requirements

**Regulatory basis**: 225 ILCS 47/10 [VERIFY current codification]

**Assessment checklist:**

- [ ] Does the employer notify the applicant **before the interview** that AI will be used
      to analyse the video and evaluate their fitness for the role?
- [ ] Does the pre-interview notice explain **how the AI works** — i.e., what characteristics
      it evaluates (facial expression, tone, word choice, language patterns)?
- [ ] Does the employer obtain the applicant's **consent** before the interview is conducted?
      (Consent must be explicit; proceeding with the interview is not deemed consent)
- [ ] Can applicants **opt out** of AI analysis? If yes, what is the alternative process and
      is it communicated to applicants?

#### 8.2 Data Destruction Requirements

**Assessment checklist:**

- [ ] Does the employer delete video recordings **within 30 days** of receiving an applicant's
      written deletion request?
- [ ] If no deletion request is received, are videos automatically deleted **no later than
      3 months** after the employer has made its final hiring decision for the position?
- [ ] Are third-party AI vendors contractually prohibited from retaining, using, or sharing
      video recordings beyond the scope of their engagement?

#### 8.3 Third-Party Data Sharing Restrictions

**Assessment checklist:**

- [ ] Are video recordings shared **only** with persons whose expertise is necessary to evaluate
      applicants for the position? (Not shared for general HR, marketing, or other purposes)
- [ ] Are third-party AI vendors contractually restricted from sharing videos with sub-processors
      not necessary for the AI analysis?
- [ ] Does the employer have a current data processing agreement with video AI vendors that
      addresses deletion, third-party restrictions, and data security?

#### 8.4 Annual Demographic Reporting Requirements (2023 Amendment)

**Assessment checklist:**

- [ ] Does the employer **annually report** to the Illinois Department of Commerce and Economic
      Opportunity (DCEO) the race and ethnicity of applicants who were and were not granted an
      interview (i.e., passed or failed the AI video screening)?
- [ ] Is reporting submitted on time to DCEO's designated portal? [VERIFY current reporting
      deadline — typically by [date] each year]
- [ ] Does the employer have a process to collect race/ethnicity data from applicants voluntarily
      before the video screening for reporting purposes?
      [VERIFY whether self-identification is required or whether employer-inferred data is permissible]

---

### Step 8.5: Illinois HB 3773 Compliance Assessment (Effective January 1, 2026)

**Applies when**: Employer uses AI to influence or make any covered employment decision — hiring,
promotion, discipline, demotion, or termination — for any Illinois employee or applicant.

**Note**: Illinois HB 3773 is distinct from and broader than AIVIA. AIVIA covers only video
interview AI; HB 3773 covers **all AI used in covered employment decisions**. Both may apply
simultaneously if the tool includes video interview analysis.

**Regulatory basis**: [VERIFY current codification as enacted — Illinois Human Rights Act amendment;
IDHR enforcement authority] [VERIFY]

#### HB 3773 Notice Requirements

**Assessment checklist:**

- [ ] Are applicants and employees **notified** when AI is used to influence any covered employment
      decision affecting them?
- [ ] Is an **annual notice** provided to all Illinois employees describing AI systems in use
      for employment decisions, their purpose, and their role in decision-making?
- [ ] When a new AI system is adopted or substantially updated, is notice provided within
      **30 days** to affected employees?
- [ ] Does the notice include: (a) that AI is used, (b) the employment decision types affected,
      (c) the characteristics or factors assessed by the AI?
- [ ] Is the notice provided in accessible language and format for the relevant workforce?

#### HB 3773 Anti-Discrimination Requirements

**Assessment checklist:**

- [ ] Does the employer's use of AI in employment decisions comply with the **Illinois Human
      Rights Act** prohibition on discrimination based on race, sex, age, disability, national
      origin, religion, sexual orientation, and other protected characteristics?
- [ ] Has the employer conducted an adverse impact analysis under the Illinois Human Rights Act
      for AI tools used in covered employment decisions?
- [ ] Is the AI tool reviewed for compliance with IHRA before deployment and upon substantial
      modification?

---

### Step 9: California FEHA AI Regulations Compliance Assessment (Effective October 1, 2025)

**Applies when**: Employer uses any automated decision system (ADS) in employment decisions
affecting California residents. Applies to **all FEHA-covered employers** (5+ employees) — note:
this is far broader than CPRA ADMT which requires 100,000+ consumer threshold.

**Regulatory basis**: California Civil Rights Council FEHA AI Regulations, approved June 2025,
effective October 1, 2025 [VERIFY current regulation text and codification — Civil Rights
Council; California Code of Regulations title 2]

#### 9.1 Anti-Bias Testing Plan Requirements

**Assessment checklist:**

- [ ] Does the employer have a documented **anti-bias testing plan** for each ADS used in
      employment decisions?
- [ ] Does the testing plan specify: (a) the frequency of testing, (b) the methodology for
      detecting adverse impact, (c) the protected characteristics tested (at minimum: sex, race,
      national origin, religion, disability, age — FEHA protected characteristics), (d) the
      threshold that triggers remediation?
- [ ] Has anti-bias testing been conducted since the regulations took effect (October 1, 2025)?
- [ ] Are test results documented and retained for at least **4 years**?

#### 9.2 Bias Documentation Requirements

**Assessment checklist:**

- [ ] Are bias testing results documented in writing, including: (a) the testing process, (b)
      criteria applied, (c) results by protected characteristic, (d) remediation steps taken?
- [ ] Are all ADS-related employment decision records (inputs, outputs, decision criteria,
      correspondence) retained for at least **4 years**?
- [ ] Are records available for production in response to an EEOC or CRD investigation
      or administrative proceeding?

#### 9.3 Notice and Opt-Out Obligations

**Assessment checklist:**

- [ ] Are applicants and employees provided **pre-use notice** before ADS is used in employment
      decisions affecting them?
- [ ] Does the notice disclose: (a) that ADS will be used, (b) for what purpose, (c) opt-out
      rights and appeal/human review process?
- [ ] Is there a mechanism for California employees and applicants to **opt out** of ADS for
      employment decisions and to request human review?
- [ ] Are opt-out requests honoured within a reasonable timeframe?
- [ ] Is a genuine human review alternative available (not merely nominal)?

**Penalty exposure**: FEHA remedies apply — compensatory and punitive damages, reinstatement,
back pay, attorney fees. California Civil Rights Department (CRD) enforcement. This is a
significant exposure because FEHA applies to 5+ employee employers with no turnover threshold.

---

### Step 10: California CPRA ADMT Regulations Compliance Assessment

**Effective date**: January 1, 2026 (for notice obligations); risk assessment submission to CPPA
by April 1, 2028 [VERIFY current timeline]
**Applies when**: Covered business (100,000+ consumers annually) using ADMT to make or facilitate
significant employment decisions affecting California residents.

#### 9.1 ADMT Pre-Use Notice Requirements (11 CCR 7220)

**Assessment checklist:**

- [ ] Is a **pre-use notice** provided to California employees and applicants before the ADMT
      is used to make significant decisions about them?
- [ ] Does the notice include:
  - [ ] (a) The name or description of the ADMT system(s) used
  - [ ] (b) The purpose for which the ADMT is used (e.g., candidate screening, performance assessment)
  - [ ] (c) The categories of personal information processed
  - [ ] (d) The logic or criteria used to make inferences or decisions (to the extent disclosable)
  - [ ] (e) The consumer's right to opt out of the ADMT
  - [ ] (f) The consumer's right to access information about the ADMT decision
  - [ ] (g) The consumer's right to a human review alternative
- [ ] Is the notice provided in **plain language** accessible to the individual?
- [ ] Is the notice provided **before** the ADMT first processes the individual's data for a
      significant decision?

#### 9.2 Opt-Out Rights (11 CCR 7221)

**Assessment checklist:**

- [ ] Does the organisation provide a mechanism for California employees and applicants to **opt
      out** of the use of ADMT for significant employment decisions?
- [ ] If an individual opts out, is the organisation prepared to offer a **human review alternative**
      that is equally capable of evaluating the individual?
- [ ] Is the opt-out mechanism easy to exercise (not buried in fine print or requiring multiple steps)?
- [ ] Are opt-out requests honoured within a reasonable timeframe?

#### 9.3 Risk Assessment Requirements (11 CCR 7150-7157)

**Assessment checklist:**

- [ ] Has the organisation conducted an ADMT risk assessment before deploying ADMT for employment
      decisions affecting California residents?
- [ ] Does the risk assessment address: (a) the purpose and context of ADMT use, (b) the benefits
      of the ADMT, (c) the risks to consumers' privacy and autonomy, (d) potential discriminatory
      impact on protected classes, (e) safeguards and mitigations implemented?
- [ ] Is the risk assessment documentation retained and available for CPPA inspection?
- [ ] Is the organisation prepared to submit the risk assessment to CPPA by April 1, 2028?
      [VERIFY current CPPA submission requirements and format]

---

### Step 11: Maryland Employer Facial Recognition Compliance Assessment

**Regulatory basis**: Maryland Code, Labor and Employment § 3-717 (effective October 1, 2020)
[VERIFY current text]. Maryland prohibits employers from using facial recognition technology
during an employment interview without the applicant's prior written consent waiver.

#### 11.1 Facial Recognition Consent Requirements

**Assessment checklist (pending verification of current law):**

- [ ] Does the employer obtain **explicit written consent** from applicants or employees before
      using facial recognition technology to identify or analyse them in employment contexts?
- [ ] Is the purpose of the facial recognition use disclosed to the individual before consent?
- [ ] Are individuals informed of their right to refuse facial recognition and of any alternative
      processes available?
- [ ] Are consent records retained for the duration of employment plus [VERIFY retention period]?

---

### Step 12: EU AI Act Article 26 Deployer Obligations Assessment

**Effective date**: August 2, 2026 (Annex III high-risk system obligations) [VERIFY]
**Applies when**: Deployer is established in the EU, or AI system output is used to make decisions
about persons located in the EU.

#### 11.1 High-Risk System Classification

**Assessment checklist:**

- [ ] Does the employment AI system qualify as Annex III Category 4 (employment/workers management)?
      Annex III Category 4 covers: recruitment and selection; performance and behaviour monitoring;
      task allocation; promotion and termination decisions
- [ ] Has the organisation confirmed whether the developer has registered the system in the EU
      AI database (Art. 71)?
- [ ] Is the developer providing an adequate instructions-for-use document per Article 13?

#### 11.2 Deployer Obligations (Article 26)

**Assessment checklist:**

- [ ] Does the deployer use the AI system **in accordance with the developer's instructions for use**?
- [ ] Are **human oversight measures** implemented: designated staff with authority and competence
      to monitor, interpret, and override AI system outputs?
- [ ] Is there a defined process for **suspending use** if the system performs unexpectedly or
      causes harm?
- [ ] Are **input data quality** controls in place to ensure the data fed to the AI system is
      relevant and sufficiently representative?
- [ ] Does the organisation **monitor the AI system's operation** and log relevant performance data?
- [ ] Is a **Fundamental Rights Impact Assessment (FRIA)** required under Article 27? (Applies to
      public bodies and private entities performing public functions; may extend to large private
      employers in some interpretations — [VERIFY EU AI Office guidance])

#### 11.3 Transparency to Workers and Candidates (Article 26(7))

**Assessment checklist:**

- [ ] Are workers and candidates **notified** when an Annex III high-risk AI system is used in
      processes affecting them?
- [ ] Does the notification disclose that AI is being used and provide the information required
      by Article 13 (name, purpose, human oversight)?
- [ ] Is the notification provided **before** the AI system first processes data about the individual?

#### 11.4 Prohibited Practices Assessment (Article 5)

**Assessment checklist:**

- [ ] Does the system use **real-time remote biometric identification** in publicly accessible
      spaces? (Prohibited except for listed law enforcement exceptions — employment use is not an exception)
- [ ] Does the system perform **AI-enabled biometric categorisation** to infer sensitive
      attributes (race, political opinion, sexual orientation, religion) from biometric data? (Prohibited)
- [ ] Does the system perform **emotion recognition** in **workplace or educational settings**?
      (Prohibited under Article 5(1)(f)) [VERIFY exact scope of prohibition]
- [ ] Does the system engage in **social scoring** of individuals based on their social behaviour
      across unrelated contexts? (Prohibited)

Any YES answer to the Article 5 checklist is a **CRITICAL DEFICIENCY** requiring immediate
escalation: the practice may be categorically prohibited and deployment must cease pending
legal review.

---

### Step 13: EEOC and Federal Overlay Assessment

**Always applies** for US employers with the required employee thresholds.

#### 12.1 Title VII Disparate Impact Analysis (EEOC Framework)

**Regulatory basis**: Title VII of the Civil Rights Act (42 U.S.C. § 2000e); EEOC May 2023
Technical Assistance Document "Navigating Employment Discrimination in AI and Automated Systems"
[VERIFY current EEOC guidance — may have been updated]

**Assessment checklist:**

- [ ] Has the employer analysed whether the AI tool produces **statistically significant differences
      in selection rates** across sex, race, national origin, or religion?
- [ ] Has the **four-fifths (80%) rule** been applied to algorithmic selection rates? (Selection rate
      for any protected group ÷ selection rate for highest group must be ≥ 0.80)
- [ ] Does the employer maintain **adverse impact documentation**: records of selection rates by
      protected class for each AI-assisted selection stage?
- [ ] If adverse impact exists, has the employer assessed whether the tool is **job-related and
      consistent with business necessity** (the employer's burden under disparate impact doctrine)?
- [ ] Has the employer evaluated whether a **less discriminatory alternative** (LDA) is available
      that would achieve the same business objective with lesser adverse impact?
- [ ] Has the employer reviewed vendor contracts to determine whether the vendor will share data
      for adverse impact analysis? (Employer remains responsible for discrimination even if the AI
      tool is vendor-supplied — EEOC position)

#### 12.2 ADA: Disability Discrimination in AI Screening

**Assessment checklist:**

- [ ] Does the AI tool evaluate characteristics that may correlate with disability status
      (cognitive processing speed, speech patterns, typing cadence, vision-related features)?
- [ ] Does the AI tool screen out candidates or employees with disabilities that could perform
      the essential functions of the job with reasonable accommodation?
- [ ] Is there a process for candidates or employees with disabilities to request an accommodation
      in lieu of the AI-assessed component?
- [ ] Does the AEDT or ADMT notice disclose the right to accommodation for disability?

#### 12.3 ADEA: Age Discrimination in Algorithmic Hiring

**Assessment checklist:**

- [ ] Does the AI tool use features that serve as **proxies for age** (graduation year, length of
      experience, references to early-career language, digital proficiency signals)?
- [ ] Has the employer analysed adverse impact on workers aged 40+ under the ADEA four-fifths
      rule (which, strictly, the EEOC has applied by analogy even though ADEA disparate impact doctrine
      is less settled than Title VII — [VERIFY current ADEA disparate impact standard])? [VERIFY]
- [ ] Are age-proxying features removed or adjusted where feasible?

#### 12.4 OFCCP (Federal Contractors Only)

**Assessment checklist (applies if employer is a federal contractor):**

- [ ] Has the contractor analysed adverse impact of AI employment tools as required by OFCCP
      regulations (41 C.F.R. Part 60-3, Uniform Guidelines on Employee Selection Procedures)?
      [VERIFY current OFCCP AI guidance — the OFCCP released guidance in 2023 [VERIFY current status])
- [ ] Are records retained in compliance with OFCCP recordkeeping requirements?

#### 13.5 FCRA + CFPB Circular 2024-06 Overlay (Consumer-Report Data)

**Regulatory basis**: Fair Credit Reporting Act 15 U.S.C. §§ 1681 et seq.; CFPB Circular 2024-06
"Background Dossiers and Algorithmic Scores for Hiring, Promotion, and Other Employment Decisions"
[VERIFY current CFPB guidance — Circular may have been superseded or supplemented]

**Assessment checklist (applies if AI tool uses background checks, credit data, public records,
or generates background dossiers from third-party data):**

- [ ] Has the employer assessed whether AI-generated **background dossiers or algorithmic scores**
      used in employment decisions constitute "consumer reports" under FCRA pursuant to CFPB Circular
      2024-06? (The CFPB has indicated such products may trigger FCRA consumer-reporting obligations)
- [ ] Is pre-employment screening conducted in compliance with FCRA: permissible purpose, written
      disclosure to the consumer, consumer authorisation?
- [ ] If the AI tool's output leads to an adverse employment decision (rejection, rescission of
      offer, demotion), are **pre-adverse-action notice** (with a copy of the consumer report and
      summary of rights) and **adverse-action notice** procedures followed (FCRA §§ 604, 606, 615)?
- [ ] Does the employer provide at least a **5-business-day waiting period** between pre-adverse-
      action notice and the adverse-action decision?
- [ ] Are FCRA-related employment records retained for at least **5 years** (FCRA statute of
      limitations for private actions)?
- [ ] Are AI vendor contracts reviewed to determine whether the vendor qualifies as a consumer
      reporting agency (CRA) under FCRA, creating additional obligations?

---

### Step 14: Severity Classification

Classify each compliance finding using this four-tier scheme, adapted to employment-AI compliance.

| Tier                 | Status                                         | Description                                                                                                                                                                                                   | Required Action                                                                                  |
| -------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| 🔴 **CRITICAL**      | Prohibited Practice / Immediate Legal Exposure | Law requires a specific action that is not being performed, AND enforcement risk is active (e.g., NYC LL 144 audit overdue; Illinois AIVIA consent not obtained; EU AI Act Art. 5 prohibited practice in use) | Stop deployment or immediately implement required control. Escalate to CHRO and General Counsel. |
| 🟠 **NON-COMPLIANT** | Clear Violation / High Remediation Priority    | Law's requirements are clear; the organisation is not meeting them; enforcement exposure present though not necessarily imminent                                                                              | Remediation plan required within 30-90 days. Owner assigned. Progress tracked.                   |
| 🟡 **PARTIAL**       | Conditionally Compliant / Gap Present          | Some requirements met; key element missing; or applicability is uncertain and requires factual/legal verification                                                                                             | Remediation plan required within 90-180 days. Gap documented. Compensating controls considered.  |
| 🟢 **COMPLIANT**     | Full Compliance                                | All statutory and regulatory requirements for this obligation are met, based on available evidence                                                                                                            | Document compliance. Monitor for regulatory updates. Incorporate into annual audit cycle.        |

**Confidence scoring** (apply to each finding):

- **HIGH (0.85–1.0)**: Clear statutory text; no interpretive uncertainty; evidence of compliance/non-compliance is direct
- **PROBABLE (0.65–0.84)**: Good regulatory basis; minor interpretive questions; evidence is strong but not definitive
- **UNCERTAIN (0.40–0.64)**: Regulatory guidance evolving; factual ambiguity; multiple readings possible — flag for counsel
- **UNVERIFIABLE (0.0–0.39)**: Cannot assess without additional data or verified authority — state assumption; mark [VERIFY]

---

### Step 15: Bias Audit Framework Construction

Where NYC Local Law 144 applies (or as a best-practice framework for other jurisdictions), construct
a bias audit programme specification:

#### 14.1 Protected Characteristics to Assess

| Jurisdiction       | Required Minimum                                                                                   | Recommended Additions                                   |
| ------------------ | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| NYC LL 144         | Sex (binary EEO-1), Race/Ethnicity (EEO-1 7 categories), Intersectional (sex × race/ethnicity)     | Disability status (ADA risk), Age group 40+ (ADEA risk) |
| Colorado SB 24-205 | Protected characteristics under Colorado Anti-Discrimination Act [VERIFY]                          | All EEOC-monitored characteristics                      |
| EEOC / Title VII   | Sex, Race, National Origin, Religion                                                               | Colour; pregnancy/maternity (Title VII)                 |
| EU AI Act / FRIA   | Sex, racial or ethnic origin, disability, age, religion or belief, sexual orientation (EU Charter) | Intersectional analysis                                 |

#### 14.2 Fairness Metrics Specification

For each bias audit, specify the metrics to be calculated:

| Metric                                   | Definition                                                    | Formula                             | Threshold                                                  | Regulatory Basis                             |
| ---------------------------------------- | ------------------------------------------------------------- | ----------------------------------- | ---------------------------------------------------------- | -------------------------------------------- |
| **Impact Ratio (Selection Rate Parity)** | Ratio of selection rates across groups                        | SR_group ÷ SR_highest               | ≥ 0.80                                                     | NYC LL 144; EEOC four-fifths rule            |
| **Statistical Significance Test**        | Whether observed difference is beyond chance                  | χ² test or Fisher's exact; p < 0.05 | Reject null if statistically significant disparity present | EEOC Uniform Guidelines                      |
| **False Positive Rate Parity**           | Rate of incorrectly advancing unqualified candidates by group | FPR_group                           | No single threshold; document disparities                  | ADA (bias in screening out protected groups) |
| **False Negative Rate Parity**           | Rate of incorrectly rejecting qualified candidates by group   | FNR_group (= 1 - TPR_group)         | No single threshold; document disparities                  | Title VII; ADA                               |
| **Proxy Feature Correlation**            | Correlation between features and protected characteristics    | ρ(feature, protected_class)         | Flag correlations > 0.30                                   | EEOC guidance on AI features                 |

#### 14.3 Audit Documentation Requirements

The bias audit must produce:

- [ ] Data description: source, time period, number of candidates/employees in each demographic category
- [ ] Methodology description: how impact ratios were calculated; statistical tests used
- [ ] Impact ratio table: value for each category; groups excluded for small-n with explanation
- [ ] Whether any protected group is below the 0.80 threshold and what remediation was applied
- [ ] Auditor independence declaration: auditor's name, employer, and attestation of independence
- [ ] Date of audit and time period covered by data

#### 14.4 Independent Auditor Qualification Criteria

Under NYC LL 144, the auditor must be genuinely independent. Use these criteria:

- [ ] Not employed by the employer or tool developer
- [ ] No direct financial interest in the tool being audited
- [ ] Has relevant expertise: statistics, psychometrics, algorithmic fairness, or employment law
- [ ] Has reviewed and signed an auditor independence declaration
- [ ] Auditor firm is not the tool developer or a closely affiliated entity [VERIFY DCWP guidance
      on specific independence requirements]

---

### Step 16: Notice Template Library

Generate jurisdiction-appropriate notice templates. Customise with organisation-specific details
before use.

#### Template A: NYC Local Law 144 — Pre-Use Candidate Notice

```
NOTICE OF AUTOMATED EMPLOYMENT DECISION TOOL (AEDT) USE

[Organisation Name] uses automated technology to assist in evaluating candidates for
employment. As required by NYC Local Law 144, we are providing you with the following
information at least 10 business days before we use this technology to assess you.

Type of AEDT used: [System name, e.g., AI candidate screening tool]

What the tool evaluates: The tool analyses [describe characteristics: e.g., résumé text,
skills assessment responses, or video interview responses] to generate [a score / a ranking /
a recommendation] about your fit for the role.

Data used: The tool processes the following categories of information you provide:
[list data categories]

Bias audit: An independent bias audit of this tool was conducted on [date]. The audit summary,
including impact ratios by demographic category, is available at [URL].

Alternative process: You have the right to request an alternative selection process that does
not use the AEDT. To request an alternative, contact [HR contact/email/phone] at least 5
business days before your scheduled assessment. We will confirm an alternative process within
[X] business days.

Questions? Contact [HR contact information].
```

#### Template B: Illinois AIVIA — Pre-Interview AI Disclosure and Consent

```
AI VIDEO INTERVIEW ANALYSIS — DISCLOSURE AND CONSENT

Before your video interview with [Organisation Name], we want to inform you about how we
use technology to evaluate candidates.

What we use: We use [Vendor Name / AI Video Interview Tool] to analyse your video interview
responses. This AI technology evaluates [describe: e.g., verbal communication patterns, tone,
language use, and response structure] to provide an assessment of candidate fit for this role.

What the AI does NOT evaluate: [List characteristics the tool does not assess, e.g., physical
appearance, disability status, protected characteristics]

Your consent: By proceeding with the video interview, you consent to AI analysis of your
responses. Proceeding with the interview constitutes your agreement to this analysis.

Alternative: If you do not consent to AI video analysis, you may request an alternative
interview format by contacting [HR contact] before [date/deadline]. We will offer an
alternative that does not use AI video analysis.

Data retention: Your video recording will be deleted within 30 days of your written request
or within 3 months of our final hiring decision for this position, whichever comes first.

Questions? Contact [HR contact information].
```

#### Template B2: Illinois HB 3773 — Annual AI Employment Use Notice

```
ANNUAL NOTICE OF ARTIFICIAL INTELLIGENCE USE IN EMPLOYMENT DECISIONS
[Illinois HB 3773 — Employee Annual Notice]

[Organisation Name] notifies all Illinois employees and applicants that artificial intelligence
(AI) systems are used in connection with the following employment decisions affecting your
employment:

AI systems in use:
1. [System name]: Used for [purpose — e.g., candidate screening, performance evaluation].
   Data assessed: [categories]. Decision types affected: [hiring / promotion / discipline /
   termination].
2. [Additional systems if applicable]

Your rights: Under the Illinois Human Rights Act, you have the right not to be subjected to
employment discrimination through the use of AI. If you believe an AI system was used
discriminatorily in an employment decision affecting you, you may file a charge with the
Illinois Department of Human Rights (IDHR).

For questions about AI systems used in your employment, contact [HR Director / contact
information].

Date: [date] | Next scheduled update: [date + 12 months or when substantially updated]
```

#### Template C: California CPRA ADMT — Employment Pre-Use Notice

```
NOTICE OF AUTOMATED DECISIONMAKING TECHNOLOGY USE
[California Privacy Rights Act — Employee/Applicant Notice]

[Organisation Name] uses automated decisionmaking technology (ADMT) in connection with
employment decisions as follows:

Technology: [System name and brief description]
Purpose: [Employment screening / performance evaluation / promotion assessment]
Personal information processed: [Categories: résumé data, assessment responses, work history]
Decision significance: This technology is used to make or assist in making [describe
decision and its significance to employment status].
Logic: [Brief description of criteria and scoring approach, to the extent disclosable]

Your rights as a California resident:
- Opt-out right: You may opt out of the use of ADMT for this significant decision. To opt
  out, contact [Privacy contact/email] before [deadline].
- Human review: If you opt out, or upon request, you may request human review of your
  assessment. Contact [HR/Privacy contact].
- Access right: You may request information about the ADMT decision that was applied to you,
  including the categories of data processed. Contact [Privacy contact].

For more information, see our Privacy Notice at [URL] or contact [Privacy contact information].
```

#### Template D: EU AI Act Article 26(7) — Worker/Candidate Transparency Notice

```
NOTIFICATION OF HIGH-RISK AI SYSTEM USE
[EU AI Act — Article 26(7) Transparency Notice]

In accordance with the EU AI Act (Regulation 2024/1689), [Organisation Name] notifies you
that a high-risk AI system classified under Annex III, Category 4 (employment and workers
management) is used in the following context:

AI system: [System name, as registered in EU AI database — reference registration number if
available]
Provider: [Developer/vendor name and contact]
Purpose: [Employment screening / interview analysis / performance monitoring]
Human oversight: All AI system outputs are reviewed by [a designated HR professional / the
hiring manager] before any employment decision is made. You have the right to request
information about the human oversight process.
Right to explanation: You have the right to request a meaningful explanation of any
AI-assisted decision that significantly affects you.

Contact: [Data Protection Officer / HR Director contact information for questions about
AI use in employment decisions]
```

---

### Step 17: Remediation Roadmap

Produce a prioritised remediation roadmap organising all non-compliant and partial findings
by urgency:

**Priority tiers:**

| Priority            | Timeframe                          | Criteria                                                                          |
| ------------------- | ---------------------------------- | --------------------------------------------------------------------------------- |
| **IMMEDIATE (P1)**  | Before deployment / within 30 days | CRITICAL findings; active enforcement exposure; prohibited practices              |
| **NEAR-TERM (P2)**  | 30–90 days                         | NON-COMPLIANT findings; regulatory deadline approaching; clear obligation not met |
| **BACKGROUND (P3)** | 90–180 days                        | PARTIAL findings; gap present but risk is lower; best-practice improvements       |

**Remediation roadmap table format:**

| Priority | Jurisdiction | Obligation                        | Finding       | Current State                                 | Required Remediation                                            | Owner                 | Deadline         | Success Criteria                                                        |
| -------- | ------------ | --------------------------------- | ------------- | --------------------------------------------- | --------------------------------------------------------------- | --------------------- | ---------------- | ----------------------------------------------------------------------- |
| P1       | NYC          | LL 144 Bias Audit                 | NON-COMPLIANT | No audit conducted                            | Commission independent auditor; complete audit; publish results | Legal + Data Science  | [date]           | Audit complete; ratios ≥ 0.80 or remediation plan; published on website |
| P1       | Illinois     | AIVIA Consent                     | NON-COMPLIANT | No pre-interview consent process              | Implement consent flow before video interviews commence         | HR / Legal            | [date]           | All future video interviewees receive and acknowledge consent           |
| P2       | Colorado     | SB 24-205 Impact Assessment       | PARTIAL       | No assessment; effective date upcoming        | Conduct deployer impact assessment; verify vendor documentation | AI Governance / Legal | February 1, 2026 | Assessment documented; vendor docs received and reviewed                |
| P2       | California   | CPRA ADMT Pre-Use Notice          | NON-COMPLIANT | No notice provided to CA applicants/employees | Deploy ADMT notice in hiring process before January 1, 2026     | Privacy / HR          | January 1, 2026  | Notice live for all CA-affected processes; records of notice delivery   |
| P3       | Federal      | EEOC Adverse Impact Documentation | PARTIAL       | No systematic adverse impact records          | Implement quarterly adverse impact tracking by protected class  | Data Science / HR     | 90 days          | Quarterly report template live; first report completed                  |

---

### Step 18: Three-Pass Quality Verification

Before delivering output, conduct this adversarial review:

**Pass 1 — Completeness**: Did the assessment address every jurisdiction in the Regulatory Stack?
For each jurisdiction, is every major obligation category covered (notice, audit, opt-out,
destruction, reporting)? Are there employment decision types or data types in the system
description that trigger obligations not yet assessed?

**Pass 2 — Consistency**: Are the same fairness thresholds applied consistently across jurisdictions?
Is the four-fifths rule applied at the same calculation level for NYC LL 144 and EEOC? Are
confidence scores applied uniformly? Are CRITICAL findings consistently escalated?

**Pass 3 — Verifiability and Currency**: Are all statutory citations marked [VERIFY] unless
verified via legalcode-mcp? Have effective dates been flagged as requiring verification
(regulatory timelines in this area shift frequently)? Are all [VERIFY] markers preserved in
the output for the user's legal counsel to confirm?

---

## Citation Quality Gates

Run these five gates silently before delivering any compliance finding. If any gate fails, revise
or flag before delivering output.

| Gate           | Rule                                                                                                                    | Fail Action                                        |
| -------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **Source**     | Every compliance claim cites a specific statute, regulation, or official guidance document                              | Add citation or mark [UNVERIFIED]                  |
| **Format**     | Citations follow recognisable form: statute name, code section, and jurisdiction                                        | Fix format                                         |
| **Currency**   | Every cited provision checked for amendments, sunset clauses, or pending enforcement guidance                           | Flag [CHECK CURRENCY]                              |
| **Domain**     | Analysis stays within employment-AI scope; does not conflate general AI governance with employment-specific obligations | Remove or segregate general AI governance comments |
| **Confidence** | Uncertainty is explicitly stated; interpretive conclusions are labelled as such rather than presented as settled law    | Add confidence qualifier                           |

---

## Self-Interrogation for CRITICAL and NON-COMPLIANT Findings

For any finding classified as CRITICAL or NON-COMPLIANT, apply this three-pass adversarial review:

**Pass 1 — Legal Chain Integrity**: Does the non-compliance conclusion follow logically from the
cited statutory text or regulatory guidance? Has the assessment correctly identified whether the
system falls within the law's definitional scope (e.g., is this system actually an "AEDT" under
NYC LL 144, or merely a software tool that does not score candidates)?

**Pass 2 — Completeness**: Have all relevant aspects of the obligation been considered? For NYC
LL 144, has the notice requirement been assessed alongside the audit requirement alongside the
publication requirement? Has the EEOC overlay been considered alongside the jurisdictional law?

**Pass 3 — Challenge**: What is the strongest argument that this finding should be downgraded from
CRITICAL to NON-COMPLIANT, or from NON-COMPLIANT to PARTIAL? Is the tool's classification as an
AEDT or high-risk system genuinely clear-cut, or are there reasonable definitional arguments?
Flag definitional uncertainty and recommend legal counsel review.

---

## Confidence Scoring

| Level            | Range     | Meaning                                                    | Prescribed Action                                          |
| ---------------- | --------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| **Definite**     | 0.95–1.0  | Clear statutory text; unambiguous application              | State with confidence                                      |
| **High**         | 0.80–0.94 | Strong authority; minor interpretive questions             | State with brief caveat                                    |
| **Probable**     | 0.60–0.79 | Good regulatory basis; reasonable counter-reading possible | State with reasoning + flag for counsel                    |
| **Uncertain**    | 0.40–0.59 | Evolving guidance; genuinely contestable                   | Flag for professional review; present both interpretations |
| **Unverifiable** | 0.0–0.39  | Cannot assess without more data or verified authority      | Do not assert; mark [UNCERTAIN]; state what data is needed |

---

## Anti-Patterns

The following anti-patterns represent common failures in employment-AI compliance. Every
output should be checked against this list before delivery.

1. **Vendor-reliance without independent review** — Accepting a vendor's assurances that their
   AI tool is "bias-audited" without verifying whether the audit meets the independence, methodology,
   and publication requirements of NYC LL 144 or other applicable law. Employer liability for
   discrimination is not transferable to the vendor.

2. **Treating bias audit as a checkbox** — Commissioning a bias audit once, publishing the results,
   and treating compliance as permanent. NYC LL 144 requires annual audits. If the model is
   retrained, the data changes, or the deployment context shifts, the audit must be refreshed.

3. **Conflating impact ratio with overall fairness** — The four-fifths rule is a minimum threshold,
   not a gold standard. An impact ratio of 0.81 is not "fair"; it is merely above the legal
   floor. Missing proxy-feature analysis, FNR parity, and calibration analysis leaves material
   risk unaddressed.

4. **Narrow scope for demographic analysis** — Calculating impact ratios only for race/ethnicity,
   ignoring sex or intersectional categories required by NYC LL 144, or ignoring age under ADEA
   risk. Conversely, collecting race/ethnicity data for reporting (Illinois AIVIA) without
   also using it to monitor bias creates an evidentiary gap.

5. **Boilerplate notice language** — Using generic privacy-policy language to satisfy jurisdiction-
   specific AEDT and ADMT notice requirements. NYC LL 144 notice is separate from a privacy notice
   and must meet its own timing (10 business days) and content requirements. California CPRA ADMT
   notice must disclose logic and opt-out rights specifically.

6. **Inadequate alternative process design** — Offering a nominal "alternative process" (e.g.,
   a one-page paper form) that practically disadvantages candidates who opt out of the AI tool,
   creating an effective deterrent to exercising the opt-out right. The alternative must be a
   genuine evaluation pathway.

7. **AIVIA consent by implication** — Treating completion of the video interview as implied
   consent to AI analysis. Illinois AIVIA requires explicit pre-interview consent, not inferred
   assent from participation.

8. **Late deletion under AIVIA** — Retaining video recordings beyond the 30-day (request) or
   3-month (post-decision) deletion windows. Video data is regulated separately from other
   applicant data; generic HR data retention policies do not override AIVIA's specific timelines.

9. **EU AI Act emotion recognition use** — Deploying AI video interview analysis tools that
   evaluate candidates' emotions (enthusiasm, stress indicators, deceptive signals) in an
   employment context. Article 5(1)(f) of the EU AI Act prohibits real-time emotion recognition
   in workplace and similar settings [VERIFY scope of prohibition in final EU AI Act text].
   This is a categorically prohibited practice, not a compliance gap.

10. **Ignoring federal contractor OFCCP obligations** — Conducting NYC LL 144 bias audits without
    also assessing whether the organisation's federal contractor status triggers Uniform Guidelines
    on Employee Selection Procedures (UGESP) adverse impact analysis obligations under OFCCP
    oversight — with different documentation and recordkeeping standards.

11. **AI tool classification gaming** — Structuring AI hiring tools to avoid LL 144's "AEDT"
    definition by labelling output as "informational" rather than a recommendation or score, even
    when the output effectively determines who advances. DCWP has signalled attention to substance
    over form in enforcement.

12. **Skipping Colorado SB 24-205 on developer reliance** — Assuming that reliance on the
    developer's impact assessment documentation satisfies the deployer's obligations under SB 24-205
    without independently verifying that the documentation is adequate, current, and covers the
    deployer's specific use case. The safe harbour is conditional, not automatic [VERIFY SB 24-205
    conditions].

13. **FCRA pre-adverse-action failure** — When an AI screening tool draws on consumer-report data
    and outputs a rejection signal, failing to provide the consumer (applicant) with pre-adverse-
    action notice before finalising the adverse employment action. The FCRA requirement survives
    regardless of whether an AI system generated the adverse signal.

14. **Isolated jurisdiction assessment** — Assessing NYC LL 144 compliance without noting that
    the same tool is likely subject to EEOC Title VII disparate impact analysis (which has no
    NYC-specific limitation) and possibly FCRA if consumer data is used. Each jurisdiction layer
    must be assessed independently, and then the combined exposure assessed.

15. **One-time training adequacy** — Conducting HR and recruiter training on AI employment
    obligations once without a recurring cadence. Colorado SB 24-205 and EEOC guidance both
    contemplate ongoing monitoring and governance, not point-in-time compliance.

16. **Demographic data collection without consent pathway** — Collecting race/ethnicity and sex
    data from applicants for Illinois AIVIA annual reporting purposes without a clear, voluntary
    self-identification process that makes collection legally defensible and creates data quality
    adequate for meaningful reporting.

17. **EU deployer obligations on non-EU AI developer** — EU-based employers using US-built AI
    employment tools assuming the US developer's own compliance programmes satisfy EU AI Act
    Article 26 deployer obligations. Deployer obligations are owed by the deployer, not derivable
    from the developer's compliance posture. The EU-based employer must independently implement
    human oversight, monitoring, and transparency obligations.

18. **Missing intersectional analysis** — Calculating impact ratios only at the single-axis level
    (e.g., only by race, only by sex) when NYC LL 144 requires intersectional analysis (e.g.,
    Black women as a distinct category from Black men and White women). Intersectional disparities
    can exist even where single-axis ratios appear acceptable.

19. **Adverse action without documentation** — Taking adverse employment actions informed by AI
    tools (rejecting applications, reducing performance scores, terminating) without contemporaneous
    documentation of the human decision-maker's role in reviewing and approving the AI-assisted
    output. This documentation is critical for both EEOC defence and Colorado/California review-
    right compliance.

20. **Compliance programme not updated for regulatory amendments** — Building compliance around the
    initial version of NYC LL 144 or Illinois AIVIA without a process to track amendments. Both
    laws have been amended since initial enactment. Colorado SB 24-205 and California CPRA ADMT
    are still early in their implementation cycles and will see guidance and amendment.

---

## Writing Standards

Before delivering any output:

- [ ] Every claim is grounded in a specific law, regulation, or official guidance — not general
      AI ethics or industry best practice (unless clearly labelled as such)
- [ ] All [VERIFY] markers are preserved and visible to the recipient; do not remove them to
      make the output look cleaner
- [ ] CRITICAL findings are stated as CRITICAL and escalation guidance is explicit; do not soften
      regulatory non-compliance into vague "recommendations"
- [ ] Confidence scores are assigned and disclosed for every compliance finding
- [ ] Notice templates are labelled as templates requiring legal review before use, not as
      ready-to-deploy documents
- [ ] Effective dates are stated explicitly for each jurisdiction; do not rely on the reader
      inferring currency
- [ ] The compliance matrix is complete — every jurisdiction in the Regulatory Stack has a row;
      no jurisdiction is omitted because the finding is unclear
- [ ] Output is in plain language that a CHRO or CFO can read and act on without translating
      legal jargon

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

Use legalcode-mcp to:

1. Retrieve current text of NYC Local Law 144 and any DCWP enforcement rules or FAQ
2. Search for recent DCWP enforcement actions under LL 144 (civil penalties, consent decrees)
3. Retrieve Colorado SB 24-205 current text and AG guidance [VERIFY current AG rulemaking status]
4. Retrieve Illinois 225 ILCS 47 current text and DCEO reporting guidance
5. Search for California 11 CCR 7200-7222 ADMT Regulations current text and CPPA enforcement
6. Retrieve EEOC May 2023 Technical Assistance Document
7. Search EU AI Act Regulation 2024/1689 Article 26 and Annex III current text

Save verified citations to `/tmp/employment-ai-compliance-research.md`. Mark each citation VERIFIED
when sourced from primary law via legalcode-mcp. Update the Glass Box audit trail with
`legalcode_mcp: "Connected — [N] citations verified on [date]"`.

**Without legalcode-mcp:**

Proceed with training-data knowledge. Apply all [VERIFY] markers. Include in the Glass Box audit
trail: `legalcode_mcp: "Not connected — all citations require independent verification"`. Provide
the user with the verification checklist in Step 5.

---

## Glass Box Audit Trail Template

Populate this template for every assessment to create an auditable record of inputs, assumptions,
and confidence levels:

```yaml
glass_box:
  skill_name: "legalcode-ai-in-employment-compliance"
  assessment_date: "[date]"
  mode: "Created from scratch — Legalcode original"

  # System assessed
  system_description: "[name and brief description of AI tool assessed]"
  employment_decision_type: "[hiring / promotion / performance / monitoring / compensation]"
  uses_biometric_data: "[yes/no/unknown]"
  fully_automated: "[yes/no — specify level]"

  # Regulatory stack
  jurisdictions_assessed:
    - "NYC Local Law 144: [applicable / not applicable / uncertain]"
    - "Colorado SB 24-205: [applicable / not applicable / not yet effective]"
    - "Illinois AIVIA: [applicable / not applicable / uncertain]"
    - "California CPRA ADMT: [applicable / not applicable / below coverage threshold]"
    - "Maryland HB 1202: [applicable / not applicable / verify current law]"
    - "EU AI Act Art. 26: [applicable / not applicable / uncertain]"
    - "EEOC / Title VII: [applicable / not applicable]"
    - "ADA: [applicable / not applicable]"
    - "ADEA: [applicable / not applicable]"
    - "OFCCP: [applicable — federal contractor / not applicable]"
    - "FCRA: [applicable — consumer report data used / not applicable]"

  # Organisational context
  playbook_loaded: "[yes / no — using regulatory minimums]"
  risk_tolerance: "[conservative / balanced / aggressive / not specified]"

  # Research and verification
  legalcode_mcp: "[Connected — [N] citations verified / Not connected — all citations require independent verification]"
  research_file: "[/tmp/employment-ai-compliance-research.md / Not created]"
  verify_markers_count: "[N]"

  # Findings summary
  critical_findings: "[N]"
  non_compliant_findings: "[N]"
  partial_findings: "[N]"
  compliant_findings: "[N]"
  overall_confidence: "[HIGH / PROBABLE / UNCERTAIN — rationale]"

  # Quality assurance
  three_pass_review_completed: "[yes / partial / no]"
  citation_quality_gates_passed: "[yes / partial with exceptions noted]"
  notice_templates_included: "[yes / no]"
  remediation_roadmap_included: "[yes / no]"

  limitations:
    - "[Any scope limitations: jurisdictions not assessed; data not available; effective dates not verified]"
    - "[Any effective dates that require verification before relying on compliance status]"
    - "[Any definitional questions about whether the assessed system falls within statutory scope]"
  reviewer: "AI-assisted — requires review by qualified employment law counsel before implementation"
```

---

## Localization Notes

This skill is jurisdiction-aware rather than jurisdiction-agnostic: different laws apply in different
states and regions. When delivering output:

- Apply only the laws in the Regulatory Stack to the specific deployment; do not pad the output with
  inapplicable laws
- For EU deployments, note that EU member states may impose additional requirements beyond the EU AI
  Act (e.g., works council consultation requirements in Germany under Betriebsverfassungsgesetz;
  CNIL or ICO guidance overlays on employment AI) [JURISDICTION-SPECIFIC — verify local labour law]
- For global deployments, note that Canada (AIDA — died January 2025 [VERIFY]; Quebec Law 25 applies
  to private sector AI), Singapore (MAS and PDPC guidance on AI in employment), and Australia
  (Fair Work Act protections, Australian Privacy Principles) may impose additional requirements —
  these are not covered in detail by this skill and require jurisdiction-specific analysis

---

## Output Format Template

Deliver the final assessment using this template:

---

# AI-in-Employment Compliance Assessment

**AI System**: [system name]
**Organisation**: [name]
**Assessment Date**: [date]
**Prepared by**: AI-assisted — requires review by qualified employment law counsel

---

## Executive Summary

[3–5 sentence overview: which jurisdictions apply, number of CRITICAL/NON-COMPLIANT/PARTIAL/
COMPLIANT findings, most urgent remediation actions, overall compliance readiness posture]

---

## Regulatory Stack

| Jurisdiction | Law                               | Applicable? | Key Obligations                                              | Effective Date         | Enforcement Body |
| ------------ | --------------------------------- | ----------- | ------------------------------------------------------------ | ---------------------- | ---------------- |
| NYC          | Local Law 144                     | [Yes/No]    | Bias audit, notice, publication, opt-out                     | Jul 2023               | DCWP             |
| Colorado     | SB 24-205                         | [Yes/No]    | Impact assessment, notice, opt-out, AG disclosure            | Feb 1, 2026 [VERIFY]   | CO AG            |
| Illinois     | AIVIA (225 ILCS 47)               | [Yes/No]    | Consent, AI disclosure, data destruction, demographic report | Jan 2020, amended 2023 | DCEO / AG        |
| California   | CPRA ADMT 11 CCR 7200             | [Yes/No]    | Pre-use notice, opt-out, access, risk assessment             | Jan 1, 2026            | CPPA / CA AG     |
| Maryland     | HB 1202 [VERIFY]                  | [Yes/No]    | Facial recognition consent                                   | [VERIFY]               | [VERIFY]         |
| EU           | AI Act Art. 26 + Annex III Cat. 4 | [Yes/No]    | Human oversight, instructions, transparency, FRIA            | Aug 2, 2026 [VERIFY]   | National MSA     |
| Federal      | EEOC Title VII + ADA + ADEA       | [Yes/No]    | Disparate impact analysis, adverse impact docs, LDA          | Always                 | EEOC             |
| Federal      | OFCCP (if contractor)             | [Yes/No]    | UGESP adverse impact analysis                                | Always                 | OFCCP            |
| Federal      | FCRA (if consumer data)           | [Yes/No]    | Pre-adverse-action notice                                    | Always                 | FTC              |

---

## Compliance Findings — By Jurisdiction

### NYC Local Law 144

| Obligation               | Compliance Status | Confidence | Finding   | Remediation |
| ------------------------ | ----------------- | ---------- | --------- | ----------- |
| Annual bias audit        | 🔴 CRITICAL       | HIGH       | [finding] | [action]    |
| Audit publication        | 🔴 CRITICAL       | HIGH       | [finding] | [action]    |
| Pre-use notice (10 days) | 🟠 NON-COMPLIANT  | HIGH       | [finding] | [action]    |
| Alternative process      | 🟡 PARTIAL        | PROBABLE   | [finding] | [action]    |

### Colorado SB 24-205 [Effective Feb 1, 2026 — VERIFY]

[table format as above]

### Illinois AIVIA

[table format as above]

### California CPRA ADMT

[table format as above]

### EEOC / Federal Overlay

[table format as above]

---

## Bias Audit Framework

[Populated per Step 14: protected characteristics, fairness metrics, auditor qualifications,
documentation requirements, audit frequency]

---

## Pre-Use Notice Templates

[Populated per Step 15: notice template(s) for applicable jurisdictions]

---

## Remediation Roadmap

| Priority | Jurisdiction | Obligation | Current State | Remediation Required | Owner | Deadline | Success Criteria |
| -------- | ------------ | ---------- | ------------- | -------------------- | ----- | -------- | ---------------- |
| P1       |              |            |               |                      |       |          |                  |
| P2       |              |            |               |                      |       |          |                  |
| P3       |              |            |               |                      |       |          |                  |

---

## Glass Box Audit Trail

[YAML block populated per Glass Box Audit Trail Template above]

---

_This assessment was produced by the Legalcode `legalcode-ai-in-employment-compliance` skill.
It does not constitute legal advice. All findings, notice templates, and remediation recommendations
require review by qualified employment law counsel before implementation. Laws cited are subject
to amendment; verify current status before relying on any provision._

---

## Provenance

Created by Legalcode (2026-03-02). Legalcode original synthesis. Research-informed by 2-agent
pipeline (structural analysis of legalcode-algorithmic-impact-assessment, legalcode-ccpa-admt-
compliance, and legalcode-ai-governance-framework-builder reference skills; plus deep web research
across primary sources via background research agent). Covers NYC Local Law 144 (AEDT bias audit +
notice + opt-out + DCWP enforcement), Colorado AI Act SB 24-205 effective February 1, 2026
(deployer impact assessment + consumer notice + appeal rights + AG disclosure + $20K/consumer
penalty), Illinois AIVIA 820 ILCS 42 (consent + AI disclosure + data destruction + DCEO demographic
reporting), Illinois HB 3773 effective January 1, 2026 (annual and 30-day notice of AI in covered
employment decisions + IHRA anti-discrimination), California CRC FEHA AI Regulations effective
October 1, 2025 (anti-bias testing plan + documentation + 4-year retention; applies to 5+ employee
FEHA-covered employers), California CPRA ADMT Regulations 11 CCR 7200-7222 effective January 1,
2026 (pre-use notice + opt-out + risk assessment), Maryland § 3-717 facial recognition written
consent (effective October 1, 2020), EU AI Act Reg. 2024/1689 Article 26 + Annex III Category 4
(deployer obligations including human oversight + worker notice + prohibited emotion recognition in
employment, effective August 2, 2026), EEOC May 2023 technical assistance (Title VII disparate
impact four-fifths rule + LDA analysis), ADA disability screening risk, ADEA age proxy analysis,
OFCCP UGESP federal contractor obligations, and FCRA + CFPB Circular 2024-06 (AI background
dossiers as consumer reports + pre-adverse-action notice). Features 18-step workflow, 13-law
regulatory stack with applicability trigger table, 11-step jurisdictional assessment with detailed
checklists, bias audit framework (impact ratio calculation + protected characteristics matrix +
fairness metrics specification), 5 notice/disclosure templates (NYC LL 144, Illinois AIVIA,
Illinois HB 3773, California FEHA/CPRA, EU AI Act), remediation roadmap with P1/P2/P3 priority
tiers, 4-tier CRITICAL/NON-COMPLIANT/PARTIAL/COMPLIANT severity classification with confidence
scoring, 20 anti-patterns, Citation Quality Gates, Self-Interrogation three-pass review, Confidence
Scoring, Glass Box audit trail, and complete output format template.
