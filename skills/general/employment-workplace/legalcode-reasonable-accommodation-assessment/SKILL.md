---
name: legalcode-reasonable-accommodation-assessment
description: 'Guide an employer through the reasonable accommodation / reasonable adjustments interactive
  process for disabled employees. Use when an employee has requested an accommodation, when a manager
  has identified a potential disability-related need, when an organisation wants to audit its accommodation
  practices, or when a specific accommodation request must be evaluated for feasibility and legal defensibility.
  Covers US ADA Title I, UK Equality Act 2010, and EU Employment Equality Directive 2000/78/EC. Topics
  include: disability determination, essential job functions, accommodation options, undue hardship /
  disproportionate burden, medical documentation, confidentiality, leave as accommodation, reassignment,
  anti-retaliation, and Glass Box audit trails. Also use for: "reasonable adjustment," "disability accommodation,"
  "ADA interactive process," "ADAAA accommodation," "Equality Act reasonable adjustments," "EU disability
  directive," "essential functions analysis," or "undue hardship assessment."'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Reasonable Accommodation Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted assessment of the
> reasonable accommodation / reasonable adjustments process. It does not constitute
> legal advice. All outputs must be reviewed by a qualified employment law attorney
> or HR legal counsel licensed in the relevant jurisdiction before being relied upon.
> Laws change; verify current applicability before acting on any provision described
> here. Statutory and case law references cited from memory carry hallucination risk —
> verify against authoritative sources before relying on them.

---

## Purpose and Scope

This skill guides an employer through the full reasonable accommodation / reasonable
adjustments lifecycle for a disabled employee or job applicant. It provides a structured,
jurisdiction-aware assessment that covers every stage from disability determination through
accommodation selection, documentation, and anti-retaliation safeguards.

**Covers:**

- Disability determination under US ADA Title I, UK Equality Act 2010, and EU Directive 2000/78/EC
- Interactive accommodation process (trigger, dialogue, documentation, selection, monitoring)
- Essential job functions / essential requirements analysis
- Accommodation feasibility assessment with COMPLIANT / PARTIAL / NON-COMPLIANT classification
- Undue hardship (US) / disproportionate burden (EU) / reasonableness (UK) analysis
- Medical documentation — what employers may and may not request
- Confidentiality of medical information
- Leave as accommodation and ADA/FMLA interaction (US)
- Reassignment as accommodation of last resort
- Anti-retaliation / victimisation protections
- Compliance gap remediation and prioritisation
- Glass Box audit trail for HR records and legal defensibility

**Does not:**

- Provide legal advice or replace qualified employment counsel
- Constitute an authoritative legal determination on any individual case
- Cover accommodation obligations in areas beyond employment (housing, public accommodations, education) — see jurisdiction-specific skills for those topics
- Apply to discrimination claims unrelated to the accommodation duty

---

## Jurisdiction and Governing Law

This skill covers three overlapping legal frameworks. At Step 2, the user selects which
applies; the analysis adapts accordingly.

| Framework                   | Primary Authority                                                                                                | Applies To                                       |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **US ADA Title I**          | 42 U.S.C. §§ 12111–12117; 29 CFR Part 1630; EEOC Enforcement Guidance EEOC-CVG-2003-1 (2002)                     | Employers with 15+ employees in the US           |
| **UK Equality Act 2010**    | EA 2010 ss. 6, 20–21, 27, 39; Schedules 1 & 8; EHRC Employment Statutory Code (2011); Acas guidance              | All UK employers (no minimum headcount)          |
| **EU Directive 2000/78/EC** | Council Directive 2000/78/EC Arts. 2, 3, 5, 10, 11; CJEU case law; member state implementing legislation; UNCRPD | Employers in EU member states (via national law) |

[JURISDICTION-SPECIFIC] When a jurisdiction not listed above applies, identify the
applicable statute or code, research the disability definition, accommodation standard,
and interactive process requirements, and apply the same analytical framework using the
most analogous of the three frameworks above as a starting scaffold.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming context, the workflow pauses and asks when:

- The answer would change the direction or scope of the analysis
- Multiple valid approaches exist and the user's priorities matter
- Ambiguity in the situation creates a fork only the user can resolve
- The jurisdiction or legal context is unclear

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

### Step 1: Accept the Situation

Accept the accommodation situation in any of these formats:

- **Narrative description**: Written summary of the employee's request, condition, and role
- **HR file excerpt**: Relevant portions of the employee's personnel or medical file
- **Manager report**: Notes from a manager flagging a likely accommodation need
- **Audit request**: "Audit our accommodation process" with or without case-specific details
- **Form or template**: A completed accommodation request form

If no situation is provided, prompt the user to describe: (1) the employee's role and
reported limitations, (2) the accommodation requested or needed, and (3) the applicable
jurisdiction.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the assessment, ask the following. Skip any question
already answered by the input:

1. **Applicable jurisdiction(s)**:
   - Options: US ADA Title I, UK Equality Act 2010, EU Directive 2000/78/EC (specify
     member state), Multiple jurisdictions, Other (specify)
   - _Why this matters_: The disability definition, process requirements, cost allocation,
     and enforcement mechanism differ materially across frameworks.

2. **Stage of the process**:
   - Options: Accommodation request just received, Interactive process underway,
     Accommodation implemented — assessing effectiveness, Considering denial — need
     legal defensibility analysis, Process audit (no pending request), Post-denial
     dispute or complaint filed
   - _Why this matters_: The output format and focus differ depending on whether the
     employer is at the intake, deliberation, or remediation stage.

3. **Employee role**:
   - Free text. Prompt with: job title, whether the role is primarily physical or
     cognitive, key deliverables, whether the employee is remote or on-site.
   - _Why this matters_: Essential functions analysis and accommodation feasibility
     depend on the specific role.

4. **Accommodation requested or under consideration**:
   - Free text. What has the employee asked for? Or, if employer-initiated, what is
     being considered?
   - _Why this matters_: The analysis is specific to the accommodation proposed.

5. **Employer size and resources**:
   - Options: Micro (1–14 employees), Small (15–100), Mid-size (101–500),
     Large (501–5,000), Enterprise (5,000+)
   - _Why this matters_: Undue hardship / disproportionate burden analysis is calibrated
     to employer resources. Also determines ADA applicability (15-employee threshold).

If the user provides partial context, state assumptions explicitly before proceeding.

### Step 3: Disability Determination

Assess whether the employee's condition qualifies as a disability under the applicable
framework. Apply the jurisdiction-specific test below.

#### 3a. US ADA (Three-Prong Test)

**Prong 1 — Actual Disability** [42 U.S.C. § 12102(1)(A); 29 CFR § 1630.2(g)–(j)]:

- Does the person have a physical or mental impairment?
- Does it substantially limit one or more major life activities?
- "Substantially limits" is construed broadly post-ADAAA 2008 — the standard is lower
  than "prevents" or "severely restricts." Apply liberally. [VERIFY]
- Assess **without regard to mitigating measures** (medication, assistive devices, learned
  behavioural modifications) — exception: ordinary eyeglasses/contact lenses.
- Episodic conditions and those in remission qualify if they would substantially limit
  when active.

**Prong 2 — Record of Disability** [42 U.S.C. § 12102(1)(B)]:

- Does the person have a history or misclassification of having a substantially limiting
  impairment?

**Prong 3 — Regarded As** [42 U.S.C. § 12102(1)(C); 29 CFR § 1630.2(l)]:

- Does the employer perceive the person as having a disqualifying impairment?
- Note: "Regarded as" individuals are **not entitled to reasonable accommodation** — only
  Prongs 1 and 2 trigger the accommodation duty. [VERIFY]

**Qualified Individual** [42 U.S.C. § 12111(8); 29 CFR § 1630.2(m)]:

- Satisfies requisite skill, experience, education, and other job-related requirements
- Able to perform essential functions **with or without reasonable accommodation**

**⟁ CLARIFY** — If disability determination is contested or unclear:

- "Is the employee's medical condition documented and ongoing, or was it recently
  disclosed? The analysis shifts if the condition is newly identified or disputed."
- "Has the employee provided any medical information about functional limitations? If
  not, document the request for clarification and pause the process."

#### 3b. UK Equality Act 2010 (Substantial and Long-Term Test)

**Core test** [EA 2010 s. 6(1); Schedule 1]:

- Physical or mental impairment?
- Substantial adverse effect on ability to carry out normal day-to-day activities?
  ("Substantial" = more than minor or trivial)
- Long-term: lasted or likely to last ≥12 months, or likely to last the rest of the
  person's life?

**Special rules:**

- Assess the condition **as if no corrective treatment were being taken** (Schedule 1,
  para. 5) — exception: vision corrected by spectacles/contact lenses.
- Cancer, HIV infection, and multiple sclerosis are **automatic disabilities** from
  diagnosis — no further assessment required (Schedule 1, para. 6). [VERIFY]
- Progressive conditions: deemed disabled if the condition is likely to result in
  substantial adverse effect in the future (Schedule 1, para. 8). [VERIFY]
- Recurring/fluctuating conditions: treated as continuing if likely to recur.
- Past disabilities: a person with a past disability is protected from present
  discrimination.

**No minimum employer headcount** — all UK employers are covered.

#### 3c. EU Directive 2000/78/EC (Social/Functional Model)

**CJEU definition** (post-UNCRPD; HK Danmark / Ring, C-335/11 [2013]):

- Physical, mental, or psychological impairment
- Long-term in nature
- That in interaction with various barriers hinders full and effective participation
  in professional life on an equal basis with others

Note: Sickness alone does not constitute disability (Chacón Navas, C-13/05 [2006]).
A long-term condition that creates functional limitations in the workplace qualifies
even if the impairment is not severe by clinical standards.

**⟁ CLARIFY** — If the EU member state is specified:

- "Which member state's law applies? Each member state has its own implementing
  legislation. I can provide the general EU Directive framework, but member state
  variations (e.g., Germany's AGG, France's Labour Code, Netherlands' Wet gelijke
  behandeling) may impose additional obligations. Should I flag these?"

### Step 4: Establish the Applicable Accommodation Standard

Once the jurisdiction is confirmed, identify the precise standard the employer must meet.

| Framework         | Standard                                                                                         | Key Distinction                                                                          |
| ----------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **US ADA**        | Reasonable accommodation unless it causes **undue hardship** (significant difficulty or expense) | Separate undue hardship defence; employer has discretion among equally effective options |
| **UK EA 2010**    | Take reasonable steps to avoid substantial disadvantage                                          | Single integrated reasonableness test; no separate "undue hardship" concept              |
| **EU 2000/78/EC** | Appropriate measures unless they would impose a **disproportionate burden**                      | Floor directive; member state law may be more protective                                 |

[JURISDICTION-SPECIFIC] For multi-national employers:

- Identify the highest standard applicable across all relevant jurisdictions
- US employees governed by ADA; UK employees by EA 2010; EU employees by national
  implementing law — parallel obligations must all be met

### Step 5: Essential Functions / Essential Requirements Analysis

**⟁ CLARIFY** — Before conducting this analysis, ask:

- "Is a written job description available for this role, and was it prepared before the
  dispute arose? A pre-existing description carries evidentiary weight."
- "Which job functions is the employee currently unable to perform, or claims they
  need adjustment to perform?"

Assess each claimed essential function using the framework below:

#### 5a. Evidence of Essential Functions (US ADA)

The following evidence is relevant [29 CFR § 1630.2(n)(3)]:

1. Employer's judgment (not conclusive alone)
2. Written job description prepared before advertising or interviewing
3. Amount of time spent on the function
4. Consequences of not requiring performance of that function
5. Terms of any applicable collective bargaining agreement
6. Work experience of past and current holders of the position

**Key rule**: A function is essential if the position exists _specifically_ to perform it,
if only a limited number of employees can share the function, or if the person was hired
for that expertise.

**Marginal functions must be reallocated** as an accommodation even if the employer
prefers the current arrangement.

#### 5b. Essential Requirements (UK EA 2010)

The UK framework does not use the term "essential functions" but applies comparable logic:

- The employer is **not required** to change the fundamental or basic nature of the job
- Redistributing tasks that are not central to the role may be a required adjustment
- In _Archibald v Fife Council_ [2004] UKHL 32, the House of Lords confirmed the duty
  can require **transferring the employee to a vacant post without competitive selection** [VERIFY]

#### 5c. Genuine and Determining Occupational Requirements (EU)

Article 4(1) Directive 2000/78/EC: A difference in treatment is permissible only where
the requirement is a genuine and determining occupational requirement and the objective
is legitimate and proportionate. This is a narrow exception — the accommodation duty
must be exhausted before relying on it.

### Step 6: Accommodation Feasibility Assessment

Assess each proposed or potential accommodation across four dimensions. Classify each as:

- **COMPLIANT** — accommodation is provided or would be effective, proportionate, and
  legally defensible
- **PARTIAL** — accommodation is underway but incomplete, or provided with conditions
  that may not be legally permissible
- **NON-COMPLIANT** — accommodation has been denied or is absent where required, or
  the process has a material legal gap

#### Accommodation Dimensions

**6a. Effectiveness** — Does the accommodation address the specific limitations caused
by the disability?

- Must enable the employee to perform essential functions, not merely improve comfort
- Multiple accommodations may be combined
- The employer may choose among equally effective options — but must offer _something_
  effective [VERIFY]

**6b. Process integrity** — Has the interactive process been conducted in good faith?

- Was the employee's request acknowledged promptly?
- Was a genuine dialogue held to explore options?
- Were alternatives considered when the requested accommodation was infeasible?
- Are all steps documented?

**6c. Cost / burden** — Is the accommodation financially proportionate?

Apply the jurisdiction-specific standard:

| Factor                     | US Undue Hardship [42 U.S.C. § 12111(10)] | UK Reasonableness [EA 2010 Sch. 8] | EU Disproportionate Burden [Recital 21] |
| -------------------------- | ----------------------------------------- | ---------------------------------- | --------------------------------------- |
| Net cost                   | After tax credits and grants              | Absolute and relative cost         | After available public subsidies        |
| Employer resources         | Facility + enterprise level               | Employer's overall resources       | Organisation size and scale             |
| Operational disruption     | Degree of disruption to operations        | Practicality and disruption        | Practicability                          |
| Available external funding | ADA tax credit (small employers)          | Access to Work grants              | Member state disability schemes         |
| Type of operation          | Structure and workforce composition       | Nature of employer's activities    | Type and degree of impairment           |

**⟁ CLARIFY** — For a cost-based denial:

- "Has the employer documented an actual cost estimate for the accommodation? Courts
  require objective evidence, not speculation."
- "Has the employer explored available government assistance? In the US, the ADA small
  business tax credit covers 50% of costs between $250–$10,250. In the UK, Access to
  Work can fund adjustments. EU member states have national disability employment
  schemes. These must be considered before claiming undue hardship / disproportionate
  burden."

**6d. Legal permissibility** — Does the proposed accommodation comply with legal constraints?

- Does it eliminate an essential function? (Impermissible)
- Does it lower production standards? (Impermissible)
- Does it bump another employee from their position? (Impermissible under ADA;
  differs under UK law — see Archibald)
- Does it create a new position not previously existing? (Not required)

### Step 7: Medical Documentation Review

Assess whether the employer's documentation requests comply with applicable law.

**US ADA — Permissible scope** [EEOC Enforcement Guidance EEOC-CVG-2003-1]:

- Nature, severity, and duration of the impairment
- Which major life activities are substantially limited
- Why the specific accommodation requested is needed
- Professional source: licensed physician, psychologist, PT, OT, vocational rehabilitation
  specialist, or licensed mental health professional

**US ADA — Impermissible requests**:

- Complete medical records
- Information about conditions unrelated to the accommodation need
- Demanding a specific form or format
- Requiring examination by employer's own physician as a first step (may occur only if
  employee-provided documentation is inadequate and employer identifies specific
  deficiencies)

**UK EA 2010 — Documentation approach**:

- Employer may request an occupational health report but cannot compel disclosure of
  the underlying clinical record
- The Access to Medical Reports Act 1988 gives employees the right to see reports
  prepared by their own treating physician before transmission to the employer [VERIFY]
- A formal diagnosis is **not required** — functional limitations are the relevant inquiry
- Medical evidence is not a prerequisite to the duty arising; the employer's knowledge
  triggers the duty

**EU GDPR overlay** [Regulation 2016/679, Art. 9]:

- Health / disability data is **special category data** requiring explicit consent or
  another Article 9(2) basis (typically processing necessary for employment law obligations
  under Art. 9(2)(b))
- Strict data minimisation applies — collect only what is necessary for the accommodation
- Purpose limitation — information collected for accommodation cannot be used for other
  HR purposes without a separate legal basis

**⟁ CLARIFY** — If documentation is disputed:

- "Has the employer clearly communicated to the employee what specific information is
  needed and why the documentation provided was insufficient? An unexplained request for
  more information may itself be a process violation."

### Step 8: Confidentiality and Information Handling

Assess whether medical and disability-related information is being handled lawfully.

**US ADA [29 CFR § 1630.14(c)]**:

- Medical information must be kept in a **separate, confidential file** — not in the
  general personnel file
- Permissible disclosures limited to:
  - Supervisors/managers — **only** to inform them of restrictions and required
    accommodations (not the diagnosis or medical details)
  - First aid and safety personnel — if emergency treatment may be needed
  - Government compliance investigators
- HIPAA does not generally govern employer-held employment records but governs
  healthcare provider disclosures to employers [VERIFY]

**UK — UK GDPR and DPA 2018**:

- Disability-related medical information is special category data
- Must be processed under Article 9(2) GDPR (explicit consent or employment law necessity)
- Strong data minimisation — share only with those with a need to know
- Managers may be informed of adjustments required but not of underlying medical details
  without the employee's consent

**EU GDPR** [Regulation 2016/679]:

- Same special category rules apply across all EU member states
- Processing basis must be documented
- Data subject rights (access, rectification, erasure) apply

**Confidentiality breach classification**: Sharing a diagnosis with an employee's team
members or including medical details in a general personnel file is classified as
**NON-COMPLIANT** and triggers separate legal exposure under privacy / data protection law.

### Step 9: Leave and Reassignment Assessment

#### 9a. Leave as Accommodation (US ADA / FMLA Interaction)

**Key ADA rule**: Leave is a reasonable accommodation even when:

- The employer has no leave policy
- The employee has exhausted FMLA or short-term disability
- The leave required extends beyond FMLA's 12-week entitlement [VERIFY]

**Critical distinction from FMLA**:

| Issue              | FMLA                                 | ADA                                        |
| ------------------ | ------------------------------------ | ------------------------------------------ |
| Maximum duration   | 12 weeks (or 26, military caregiver) | No fixed ceiling — individualized analysis |
| Return-to-position | Equivalent position                  | Original position (absent undue hardship)  |
| Eligibility        | 50+ employees; 12-month tenure       | 15+ employees; no tenure requirement       |
| Covered conditions | Serious health condition             | ADA-qualifying disability                  |

**Indefinite leave**: Courts consistently hold that leave with no foreseeable return date
is generally not a reasonable accommodation because it prevents workforce planning.
However, a definite but extended period may qualify; each situation requires individual
analysis. [VERIFY]

**Counting disability-related absences against attendance policies**: Applying a "no
fault" attendance policy to absences caused by disability without ADA individualized
analysis is a material compliance risk. Classify as **NON-COMPLIANT** if disability-related
absences are treated identically to other absences without accommodation analysis.

#### 9b. Reassignment (Accommodation of Last Resort)

**Trigger**: Reassignment is required only when:

1. No effective accommodation exists for the current position, OR
2. All other effective accommodations constitute undue hardship / are not reasonable

**US ADA rules** [29 CFR § 1630.2(o)(2)(ii); EEOC Guidance]:

- Must reassign to a **vacant equivalent position** (pay, status, benefits, location)
- If no equivalent vacancy, must consider lower-level positions
- Employee need only meet basic qualifications — not be the best candidate
- Employer must inform employee of vacancies; need not create a new position or bump an
  existing employee
- "Vacant" includes positions likely to become available within a reasonable time [VERIFY]

**UK EA 2010 — Archibald duty**:

- _Archibald v Fife Council_ [2004] UKHL 32: the duty may require transferring the
  employee to a vacant post **without competitive selection**, even if the employee would
  not have succeeded in open competition [VERIFY]
- This goes materially further than the US ADA standard

**EU — HR Rail duty**:

- _HR Rail SA v Juliën Matzak_, C-485/20 [2022]: the employer must consider
  redeployment to another post before dismissing a disabled employee. The accommodation
  duty is not exhausted without this step [VERIFY]

### Step 10: Anti-Retaliation / Victimisation Assessment

Assess whether the employer's actions could constitute unlawful retaliation or victimisation.

**US ADA — Protected activities** [42 U.S.C. § 12203]:

- Making an accommodation request
- Filing an EEOC charge or internal complaint
- Participating in an EEOC investigation or proceeding
- Opposing a practice believed to violate the ADA
- Assisting another person in asserting ADA rights

**US ADA — Prohibited employer conduct**:

- Termination, demotion, pay cut, or schedule change following a request
- Negative performance evaluations tied to accommodation use or requests
- Increased scrutiny following a charge or complaint
- "Interference" — coercive tactics that discourage exercise of ADA rights
- Applying disciplinary action for disability-related absences that were approved as
  ADA accommodation

**UK EA 2010 — Victimisation** [EA 2010 s. 27]:

- Subjecting a person to a detriment because they have done (or are believed likely to
  do) a **"protected act"**
- Protected acts include: bringing EA 2010 proceedings, giving evidence, doing anything
  in connection with the EA 2010, making a good-faith allegation of a breach
- Bad faith (deliberately false allegations) removes protection; honest but mistaken
  beliefs retain protection

**EU — Victimisation** [Directive 2000/78/EC Art. 11]:

- Employees must be protected against dismissal or other adverse treatment as a reaction
  to an internal complaint or legal proceedings aimed at enforcing equal treatment
- Burden shift [Art. 10]: once a prima facie case of discrimination or failure to
  accommodate is established, the burden shifts to the employer to prove no breach

**⟁ CLARIFY** — If any adverse action occurred after an accommodation request:

- "When did the adverse action (termination, demotion, poor review) occur relative to
  the accommodation request or complaint? Temporal proximity is significant evidence of
  retaliation even if the employer claims an independent reason."

### Step 11: Quality Verification

Before delivering the assessment, run all quality checks in the **Quality Assurance
Framework** section:

1. Run the 5 Citation Quality Gates silently. Revise failures before delivering.
2. For every NON-COMPLIANT finding, run the 3-pass Self-Interrogation. Revise if any
   pass reveals a weakness in the classification.
3. Assign a Confidence Score to each material finding.
4. Verify all jurisdiction-specific [VERIFY] flags are resolved or clearly marked.
5. Generate the Glass Box Audit Trail and append to the output.

---

## Legal Framework Reference

### Disability Definition Quick Reference

| Issue                   | US ADA (post-ADAAA)                                                     | UK Equality Act 2010                                                                                  | EU / CJEU (Ring)                                                                                                                 |
| ----------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Core test               | Physical/mental impairment substantially limiting a major life activity | Physical/mental impairment with substantial, long-term adverse effect on normal day-to-day activities | Long-term physical/mental/psychological impairment interacting with barriers to hinder professional participation on equal basis |
| Standard                | Broadly construed post-2008                                             | "Substantial" = more than minor/trivial                                                               | Social/functional model (UNCRPD-aligned)                                                                                         |
| Mitigating measures     | Assessed without (except spectacles)                                    | Assessed without corrective treatment (except spectacles)                                             | Not explicitly addressed by Directive; varies by member state                                                                    |
| Automatic conditions    | None — all impairments assessed                                         | Cancer, HIV, MS automatic from diagnosis                                                              | None specified in Directive                                                                                                      |
| Temporary illness       | Does not qualify unless long-term                                       | Does not qualify unless substantial/long-term                                                         | Sickness ≠ disability (Chacón Navas)                                                                                             |
| Employer size threshold | 15+ employees                                                           | None                                                                                                  | Varies by member state                                                                                                           |

### Interactive Process Steps

| Phase         | US ADA                                             | UK EA 2010                                                 | EU Directive                                  |
| ------------- | -------------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------- |
| Trigger       | Employee request or employer knowledge of need     | Employer knowledge (anticipatory element)                  | Employee need; employer awareness             |
| Initiation    | Employer acknowledges request                      | Employer engages upon knowledge                            | Varies; CJEU implies case-by-case assessment  |
| Dialogue      | Good faith interactive process (EEOC Guidance)     | Genuine consultation (EHRC Code para. 6.19; Acas guidance) | Implied; member state law varies              |
| Selection     | Employer chooses among equally effective options   | Employer selects reasonable adjustment                     | Employer selects appropriate measure          |
| Monitoring    | Ongoing duty if circumstances change               | Ongoing duty to review                                     | Ongoing duty                                  |
| Documentation | Critical — absence of records treated as bad faith | Important — Tribunals draw adverse inferences              | Good practice; member state requirements vary |

### Accommodation Types Reference

| Category                             | Examples                                                          | Notes                                                            |
| ------------------------------------ | ----------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Schedule modification**            | Flexible hours, reduced hours, intermittent leave, rest breaks    | Required even if no equivalent policy exists for others          |
| **Telework / remote work**           | Full or partial remote; hybrid arrangements                       | Effective only if essential functions can be performed remotely  |
| **Assistive / ergonomic equipment**  | Screen readers, voice-to-text, ergonomic chairs, amplified phones | Often low cost; JAN database is key resource                     |
| **Job restructuring**                | Reallocating marginal (non-essential) tasks                       | Essential functions need NOT be eliminated                       |
| **Physical workspace modifications** | Accessible workstations, ramps, signage, lighting adjustments     | May involve physical features limb under UK EA 2010              |
| **Policy modifications**             | Adjusting attendance policies, conduct rules, grooming policies   | Must be considered before denying due to policy conflict         |
| **Modified training**                | Alternative formats, additional time, captioning, interpreters    | Required for training and development as well as daily work      |
| **Reassignment**                     | Transfer to vacant equivalent or lower-level position             | Last resort — only when current role cannot be accommodated      |
| **Auxiliary aids / services**        | Job coaches, note-takers, BSL interpreters                        | Expressly listed in UK EA 2010 Schedule 8                        |
| **Leave**                            | Paid (if accrued), unpaid beyond FMLA (ADA); phased return (UK)   | Individualized analysis; indefinite leave generally not required |

**Explicitly NOT required** (US ADA):

- Eliminating an essential function
- Lowering production standards (qualitative or quantitative)
- Creating a new position
- Bumping another employee
- Providing personal use items (hearing aids, prosthetics, wheelchairs — though workplace
  equipment modifications are required)
- Changing the employee's supervisor

---

## Compliance Classification

Classify each assessed element using a three-tier system:

### COMPLIANT — Requirement Met

The employer's current practice or response satisfies the applicable legal standard.
The accommodation process is legally defensible at this element.

**Examples:**

- Accommodation request acknowledged within 5 business days with a meeting scheduled
- Medical documentation request limited to functional limitations and accommodation need
- Medical information stored in a separate, locked confidential file
- Alternative effective accommodations offered when the requested one was infeasible

**Action**: Document for the Glass Box audit trail. No immediate remediation needed.
Continue to monitor for changed circumstances.

### PARTIAL — Requirement Partially Met

The employer has made efforts that partially satisfy the legal standard but there is a
gap that creates compliance risk. Remediation is needed but the situation is not yet
a clear legal violation.

**Examples:**

- Interactive process initiated but documentation of dialogue is incomplete
- Medical documentation request was appropriate in scope but the form also asked for
  diagnosis details not necessary for the accommodation decision
- Accommodation was approved but effectiveness review has not been scheduled
- Leave granted as accommodation but the return-to-position guarantee was not documented

**Action**: Identify specific gap. Provide remediation steps. Classify urgency using the
Priority Framework. Implement before the compliance gap becomes a legal violation.

### NON-COMPLIANT — Requirement Not Met

The employer's current practice or response falls below the applicable legal standard.
This element creates material legal exposure.

**Examples:**

- Accommodation request denied with no interactive process conducted
- Undue hardship claimed with no documented cost analysis
- Disability-related absences counted against attendance policy without ADA / EA 2010
  accommodation analysis
- Employee's diagnosis shared with their team or included in the general personnel file
- Adverse employment action taken within weeks of accommodation request with no
  documented independent reason
- Accommodation denied because the employer concluded the position can be held by a
  non-disabled person (this is irrelevant to the ADA accommodation analysis)

**Action**: Apply 3-pass Self-Interrogation. Explain the specific legal basis for
non-compliance. Provide market-standard remediation language. Classify urgency as
Critical or High. Recommend escalation to employment counsel.

---

## Remediation Framework

For each PARTIAL or NON-COMPLIANT finding, provide a remediation entry in this format:

```
Finding: [brief description of the compliance gap]
Classification: [PARTIAL / NON-COMPLIANT]
Jurisdiction: [US ADA / UK EA 2010 / EU 2000/78/EC / All]
Legal basis: [specific statute, regulation, or principle — or mark [UNVERIFIED]]
Risk level: [Critical / High / Medium / Low]
Remediation steps:
  1. [First action — who does what by when]
  2. [Second action — who does what by when]
  3. [Third action if needed]
Confidence: [level from scoring framework]
```

---

## Prioritisation Framework

When presenting findings, organise by priority:

### Critical — Immediate Legal Exposure

Issues where the employer faces imminent legal liability unless remediated immediately:

- Accommodation request denied with no interactive process
- Retaliation / victimisation occurring now
- Disability-related dismissal without accommodation analysis (HR Rail rule — EU)
- Medical information disclosed to unauthorised persons
- Complete absence of documentation for a contested accommodation decision

**Recommended response**: Escalate to employment counsel within 24–48 hours.
Suspend adverse actions pending legal review.

### High — Material Legal Risk

Issues that create serious legal exposure if not remediated soon:

- Interactive process initiated but stalled for more than a few weeks without justification
- Undue hardship claimed without documented objective analysis
- Reassignment not considered before concluding no accommodation is possible
- Attendance policy applied to disability-related absences without individual analysis
- Documentation requests that exceeded permissible scope

**Recommended response**: Remediate within 1–2 weeks. Brief HR leadership and
employment counsel.

### Medium — Compliance Gap Requiring Attention

Issues that fall below best practice and create partial legal risk:

- Accommodation approved but effectiveness monitoring not scheduled
- Incomplete documentation of the interactive process (some steps not recorded)
- Medical information in the general personnel file rather than a confidential separate file
- Leave accommodation granted but return-to-position guarantee not documented

**Recommended response**: Remediate within 30 days. Implement systemic process
improvements to prevent recurrence.

### Low — Best Practice Gap

Issues that do not yet constitute a legal violation but represent departures from best
practice that could escalate:

- Job descriptions not reviewed to identify essential vs. marginal functions before a
  request arises
- Accommodation policy not in place or not communicated to employees
- Managers not trained on accommodation request recognition and referral

**Recommended response**: Address within 90 days as part of ongoing HR compliance
programme.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                                          | Fail Action                                              |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, case, or established principle                                        | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction (e.g., 42 U.S.C. § 12111; EA 2010 s. 6; C-335/11) | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments or repeal; ADAAA-era changes incorporated for US law                             | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the identified jurisdiction; no cross-jurisdictional assumptions imported without explicit flags        | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden. If not certain of a legal position, say so                                         | Add confidence qualifier                                 |

### Self-Interrogation for NON-COMPLIANT Findings

For any element classified as NON-COMPLIANT, apply this 3-pass self-interrogation before
delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the non-compliance classification follow logically from the statute, regulation,
  or case cited?
- Would an Employment Tribunal, EEOC investigator, or court actually reach this
  conclusion on these facts?
- What counter-argument would the employer's counsel make?

**Pass 2 — Completeness**:

- Have all relevant statutes, regulations, and principles been considered?
- Has recent guidance (EEOC 2023 mental health guidance, EHRC 2024 neurodiversity
  updates) been accounted for?
- Are there procedural dimensions not yet addressed (e.g., burden of proof, limitation
  periods)?

**Pass 3 — Challenge**:

- What is the strongest argument that the employer's conduct IS compliant?
- Under what circumstances might a reasonable employment lawyer accept this approach?
- Is the NON-COMPLIANT classification proportionate, or should this be PARTIAL with
  conditions?

If any pass reveals a weakness, revise the classification and rationale before delivery.
Mark the audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material finding, assign a confidence level:

| Level        | Range     | Meaning                                                      | Action                                                |
| ------------ | --------- | ------------------------------------------------------------ | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, clear statute, unambiguous application          | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong authority, minor factual questions remain             | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments but circumstances are disputed                | State with explicit reasoning and contra-indicators   |
| **Possible** | 0.40–0.59 | Genuinely uncertain — competing authorities or unusual facts | Flag for counsel review with both sides of argument   |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                                      | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every assessment output MUST include a Glass Box audit section. This makes the reasoning
traceable and supports legal defensibility of HR decisions.

```yaml
glass_box:
  skill: legalcode-reasonable-accommodation-assessment
  employee_role: "[Job title — or 'Not provided']"
  accommodation_requested: "[Description — or 'General audit']"
  jurisdiction: "[US ADA / UK EA 2010 / EU 2000/78/EC (member state) / Multiple]"
  employer_size: "[Micro / Small / Mid-size / Large / Enterprise]"
  process_stage: "[Intake / Interactive process / Denial analysis / Audit / Post-dispute]"
  disability_determination: "[COMPLIANT / PARTIAL / NON-COMPLIANT / Not assessed]"
  interactive_process: "[COMPLIANT / PARTIAL / NON-COMPLIANT / Not assessed]"
  accommodation_analysis: "[COMPLIANT / PARTIAL / NON-COMPLIANT / Not assessed]"
  documentation_review: "[COMPLIANT / PARTIAL / NON-COMPLIANT / Not assessed]"
  confidentiality: "[COMPLIANT / PARTIAL / NON-COMPLIANT / Not assessed]"
  leave_analysis: "[COMPLIANT / PARTIAL / NON-COMPLIANT / Applicable / Not applicable]"
  reassignment_analysis: "[COMPLIANT / PARTIAL / NON-COMPLIANT / Applicable / Not applicable]"
  anti_retaliation: "[COMPLIANT / PARTIAL / NON-COMPLIANT / Not assessed]"
  legalcode_mcp: "Connected / Not connected"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no NON-COMPLIANT items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Scope limitations — e.g., 'Assessment based on employer's account only; employee's medical documentation not reviewed']"
    - "[Any caveats about jurisdiction-specific member state law variations]"
  reviewer: "AI-assisted — requires review by qualified employment law counsel"
```

---

## Anti-Patterns

What NOT to do in the reasonable accommodation process:

1. **Waiting for a formal request before engaging** — Under UK law, the duty is triggered
   by employer knowledge, not a formal request. Under the ADA, courts treat failure to
   proactively engage as bad faith when the need was obvious. Always act on notice.

2. **Requiring a specific diagnosis** — The legal inquiry is functional (what limitations
   does the impairment create?) not diagnostic (what is the medical label?). Demanding a
   specific diagnosis exceeds permissible documentation and may deter employees from
   disclosing needs.

3. **Treating the employee's preferred accommodation as mandatory** — The employer has
   discretion to choose among equally effective options. But discretion to choose among
   effective options is not discretion to offer nothing.

4. **Denying accommodation because the job can be done by a non-disabled person** — The
   ADA requires accommodation for the specific employee's limitations; the existence of
   non-disabled applicants is irrelevant.

5. **Conflating FMLA exhaustion with the end of accommodation obligations** — Telling an
   employee their rights are exhausted when 12 weeks of FMLA ends, without separately
   analysing ADA leave obligations, is one of the most common and costly employer errors.

6. **Claiming undue hardship without a documented cost analysis** — Gut feeling is not
   a legal defence. Courts require objective, specific evidence of significant difficulty
   or expense. A documented analysis that fails is more defensible than none at all.

7. **Sharing medical diagnoses with supervisors or teams** — Managers may be told what
   accommodations and restrictions apply, but not the underlying diagnosis or medical
   details. Breaching this rule creates independent legal exposure under ADA, UK GDPR,
   and EU GDPR.

8. **Including medical information in the general personnel file** — The ADA requires
   a separate, confidential medical file. Including disability-related documentation in
   the general HR file is a standalone ADA violation.

9. **Rigid application of attendance or performance policies** — Applying a "no fault"
   attendance policy to disability-related absences without individualized accommodation
   analysis is a material compliance risk. The policy must be evaluated as a potential
   PCP (UK) or practice subject to reasonable accommodation (US/EU).

10. **Relying on co-worker resentment as undue hardship** — Co-workers may resent
    accommodations. This is legally irrelevant unless the accommodation actually imposes
    a documented material work burden on specific co-workers. Courts have consistently
    rejected resentment alone as a basis for undue hardship.

11. **Closing the process after one denial** — Circumstances change. If the employee's
    condition evolves, a new request is made, or vacancies arise, the duty re-triggers.
    A single denial does not permanently exhaust the employer's obligation.

12. **Failing to consider reassignment** — Before concluding no accommodation is possible
    in the current role and moving toward dismissal, the employer must genuinely canvass
    available vacancies. This step is mandatory under ADA, required by Archibald (UK),
    and confirmed by HR Rail (EU). Omitting it is a material process failure.

13. **Taking adverse action shortly after an accommodation request without documentation
    of an independent reason** — Temporal proximity is highly probative evidence of
    retaliation. If adverse action was planned before the request for legitimate reasons,
    document those reasons contemporaneously before the action is taken.

14. **Assuming small employer status eliminates obligations** — US ADA applies to employers
    with 15+ employees; UK EA 2010 has no threshold at all. "Small business" often
    reduces the weight of financial factors in the burden analysis but rarely eliminates
    the duty entirely.

15. **Requiring the employee to accept leave when other accommodations would work** — A
    policy that automatically routes accommodation requests to leave of absence, without
    exploring less disruptive alternatives, has been challenged successfully in EEOC
    litigation. Leave is an accommodation of last resort, not first resort.

---

## Writing Standards

Apply plain-language discipline to all output:

**For remediation instructions** (shared with HR and line managers):

- Plain language. No legal jargon without definition.
- Active voice: "The employer must document the cost analysis" not "A cost analysis
  is required to be documented by the employer."
- Short sentences. One point per sentence.
- Name the actor: "HR must schedule a dialogue meeting" not "A meeting should be held."
- Specific, not vague: cite the legal provision rather than "this may be a problem."

**For legal analysis sections** (shared with employment counsel):

- Same plain-language standards
- Technical analysis may be more detailed
- Confidence qualifiers where appropriate
- Glass Box audit trail appended

**Quality gates before delivery**:

1. Can an HR business partner act on the remediation steps without a law degree?
2. Can employment counsel understand and rely on the legal analysis in an EEOC response
   or Tribunal submission?
3. Is every legal claim backed by a specific citation (or flagged [VERIFY])?
4. Are any phrases vague or hedging where precision is possible? If yes, fix.
5. Could any sentence be shorter without losing meaning? If yes, shorten.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred)**:

- In Step 3, search for jurisdiction-specific disability definitions and case law
- In Step 6, search for undue hardship / disproportionate burden case law from the
  relevant jurisdiction
- In Step 9, verify current state of EEOC guidance on leave and reassignment
- In Step 10, search for recent anti-retaliation / victimisation case law
- Save the most relevant results to `/tmp/legalcode-accommodation-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp**:

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus the assessment on process integrity and structural compliance rather than
  jurisdiction-specific legal certainty
- Include a prominent notice that legal citations require independent verification
  before reliance

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Reasonable Accommodation Assessment

**Employee Role**: [job title]
**Accommodation Requested**: [description]
**Jurisdiction**: [US ADA / UK EA 2010 / EU (member state) / Multiple]
**Employer Size**: [size category]
**Assessment Date**: [date]
**Process Stage**: [stage]

---

## Disability Determination

**Status**: COMPLIANT / PARTIAL / NON-COMPLIANT
**Analysis**: [1–3 sentences applying the jurisdiction-specific test]
**Confidence**: [level]

---

## Interactive Process Assessment

**Status**: COMPLIANT / PARTIAL / NON-COMPLIANT
**Steps completed**: [list]
**Gaps identified**: [list or "None identified"]

---

## Accommodation Feasibility

**Accommodation reviewed**: [description]
**Status**: COMPLIANT / PARTIAL / NON-COMPLIANT
**Effectiveness**: [analysis]
**Cost / Burden analysis**: [analysis]
**Legal permissibility**: [analysis]

---

## Medical Documentation Review

**Status**: COMPLIANT / PARTIAL / NON-COMPLIANT
**Analysis**: [what was requested vs. what is permissible]

---

## Confidentiality Assessment

**Status**: COMPLIANT / PARTIAL / NON-COMPLIANT
**Analysis**: [how medical information is handled]

---

## Leave / Reassignment Assessment

**Leave status**: [COMPLIANT / PARTIAL / NON-COMPLIANT / Not applicable]
**Reassignment status**: [COMPLIANT / PARTIAL / NON-COMPLIANT / Not applicable]
**Analysis**: [summary]

---

## Anti-Retaliation Assessment

**Status**: COMPLIANT / PARTIAL / NON-COMPLIANT
**Risk indicators**: [list or "None identified"]

---

## Priority Findings

| Priority | Finding       | Status        | Action Required |
| -------- | ------------- | ------------- | --------------- |
| Critical | [description] | NON-COMPLIANT | [action]        |
| High     | [description] | NON-COMPLIANT | [action]        |
| Medium   | [description] | PARTIAL       | [action]        |
| Low      | [description] | PARTIAL       | [action]        |

---

## Remediation Plan

[Remediation entry for each PARTIAL or NON-COMPLIANT finding using the Remediation
Framework format]

---

## Next Steps

[Specific actions, owners, and deadlines]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

This skill covers US ADA Title I, UK Equality Act 2010, and EU Directive 2000/78/EC as
its primary frameworks. For jurisdictions not covered here:

1. **Canada**: Canadian Human Rights Act (federal) and provincial human rights codes (e.g.,
   Ontario Human Rights Code) impose a duty to accommodate to the point of "undue
   hardship." The Canadian standard is broadly comparable to the ADA but with some
   differences in process. [JURISDICTION-SPECIFIC — verify current provincial requirements]

2. **Australia**: Disability Discrimination Act 1992 (Cth) and the Australian Human Rights
   Commission enforce a duty to provide reasonable adjustments. Standards are broadly
   analogous to the UK EA 2010 model. [JURISDICTION-SPECIFIC — verify current guidance]

3. **Germany**: AGG (Allgemeines Gleichbehandlungsgesetz) § 5 requires positive measures
   including reasonable accommodation (angemessene Vorkehrungen), informed by the Directive.
   Additional obligations exist under SGB IX (Sozialgesetzbuch IX) for severely disabled
   employees (GdB ≥ 50), including co-determination with the integration committee
   (Schwerbehindertenvertretung / SBV). [JURISDICTION-SPECIFIC — verify current AGG requirements]

4. **France**: Labour Code (Code du travail) L.5213-6 requires reasonable adjustments for
   disabled workers. RQTH (Reconnaissance de la Qualité de Travailleur Handicapé) is an
   official recognition status that triggers specific employer obligations including AGEFIPH
   contribution obligations. [JURISDICTION-SPECIFIC — verify current Labour Code provisions]

5. **Nordic jurisdictions**: Norway's Discrimination and Accessibility Act (Likestillings-
   og diskrimineringsloven), Sweden's Discrimination Act (Diskrimineringslag 2008:567),
   Denmark's Act on Prohibition of Discrimination in the Labour Market all impose
   accommodation duties. [JURISDICTION-SPECIFIC — verify per-country requirements]

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on deep research of US ADA
Title I (42 U.S.C. §§ 12111–12117), UK Equality Act 2010 (ss. 6, 20–21, 27, 39;
Schedules 1 & 8), and EU Directive 2000/78/EC and CJEU case law including HK Danmark
(C-335/11), Chacón Navas (C-13/05), and HR Rail SA (C-485/20). Informed by EEOC
Enforcement Guidance EEOC-CVG-2003-1, the EHRC Employment Statutory Code of Practice
(2011), Acas reasonable adjustments guidance, and the Job Accommodation Network (JAN)
practitioner database. All statutory and case law references marked [VERIFY] should be
independently verified against authoritative sources before reliance.
