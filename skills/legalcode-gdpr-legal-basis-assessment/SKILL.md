---
name: legalcode-gdpr-legal-basis-assessment
description: >
  Systematically assess the appropriate GDPR Article 6 lawful basis for any processing
  activity — covering consent (Art. 6(1)(a)), contract performance (Art. 6(1)(b)), legal
  obligation (Art. 6(1)(c)), vital interests (Art. 6(1)(d)), public task (Art. 6(1)(e)),
  and legitimate interests (Art. 6(1)(f)). Use when selecting a legal basis for new
  processing, auditing an existing legal basis for GDPR/UK GDPR compliance, refreshing
  invalidated consent, evaluating basis changes, or building a legal basis register
  integrated with ROPA requirements. Covers Article 9 special category processing
  conditions, Article 10 criminal conviction and offence data, and children's data under
  Article 8. Evaluates each candidate basis against adequacy criteria, identifies where
  multiple bases apply or conflict, flags basis-switching risks, documents downstream
  data subject rights per basis, and produces a legal basis register ready for ROPA
  population. EU/UK GDPR primary scope; Swiss FADP and multi-regime annotations
  included. Produces ADEQUATE / REQUIRES REVIEW / INADEQUATE per-basis classifications
  and APPROVED / CONDITIONAL / REJECTED overall outcomes with Glass Box audit trail.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-6
context: fork
agent: general-purpose
---

# Legalcode GDPR Legal Basis Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted GDPR lawful basis
> assessment under GDPR Art. 6, Art. 9, Art. 10, and Art. 8. It does not constitute
> legal advice. All outputs must be reviewed by a qualified privacy counsel or Data
> Protection Officer licensed or operating in the relevant jurisdiction before any
> reliance, action, or regulatory submission. Privacy law, EDPB guidelines, and
> supervisory authority guidance evolve — verify currency before treating any provision
> here as current. Statutory, case law, and regulatory references cited from training
> data carry hallucination risk — verify against authoritative primary sources before
> use. Mark any unverified citation **[VERIFY]** before delivery.

---

## Purpose and Scope

This skill determines the correct GDPR lawful basis for any personal data processing
activity, documents the adequacy assessment rationale, and produces a legal basis
register entry ready for integration with the organisation's Records of Processing
Activities (RoPA).

A lawful basis is the legal foundation that makes data processing permissible under
GDPR. Selecting the right basis is not merely a compliance checkbox — it determines
which data subject rights apply, whether processing can continue if circumstances change,
and what documentation must be maintained. Wrong basis selection is the **single most
fined GDPR violation category**, with enforcement actions including Meta €390M (Irish
DPC, January 2023), LinkedIn €310M (Irish DPC, October 2024), and Meta €479M (Spanish
AEPD, 2025) all stemming from improperly applied or switched legal bases.

**Covers:**
- Adequacy assessment of all six Art. 6(1) lawful bases (a through f)
- Screening triage to identify viable candidate bases quickly
- Deep-dive analysis per viable basis: eligibility criteria, necessity test, and
  proportionality/balancing assessment (where applicable)
- Per-basis classification (ADEQUATE / REQUIRES REVIEW / INADEQUATE)
- Overall legal basis determination (APPROVED / CONDITIONAL / REJECTED)
- Article 9 special category data overlay — 10 conditions under Art. 9(2)
- Article 10 criminal conviction and offence data overlay
- Article 8 children's data consent overlay with age threshold analysis
- Downstream data subject rights matrix per selected basis
- Basis-switching prohibition analysis and valid-change conditions
- Multiple-activities / multiple-bases documentation framework
- Consent refresh trigger analysis
- Three-regime jurisdiction parallel track (EU GDPR / UK GDPR / Swiss FADP)
- ROPA-compatible legal basis register output (Art. 30 integration)
- Integration hooks for DPIA, LIA, privacy policy, and DPA skills
- Glass Box audit trail for supervisory authority demonstrability

**Does not:**
- Conduct a full Legitimate Interest Assessment (LIA) — see
  `legalcode-legitimate-interest-assessment` for the complete three-part test
- Generate a DPIA — see `legalcode-dpia-generator`
- Draft Data Processing Agreements — see `legalcode-data-processing-agreement-drafter`
- Draft a privacy policy — see `legalcode-privacy-policy-drafter`
- Assess cross-border transfer mechanisms — see `legalcode-cross-border-transfer-assessment`
- Provide legal advice or replace qualified data protection counsel
- Guarantee against supervisory authority enforcement action

**Complementary skills in the GDPR skill family:**
- `legalcode-legitimate-interest-assessment` — deep Art. 6(1)(f) three-part test
- `legalcode-ropa-generator` — records the output of this skill in the Art. 30 register
- `legalcode-dpia-generator` — triggered by high-risk processing identified here
- `legalcode-data-mapping-workflow` — provides input data for this assessment
- `legalcode-privacy-policy-drafter` — receives basis disclosure language from this skill

---

## Jurisdiction and Governing Law

This skill operates primarily under EU GDPR and UK GDPR, with Swiss FADP annotation.

| Regime | Primary Instrument | Supervisory Authority | Key Guidance |
|--------|-------------------|-----------------------|--------------|
| **EU GDPR** | Regulation (EU) 2016/679 | Lead SA + EDPB | EDPB Guidelines 2/2019 (Art. 6(1)(b)); EDPB Guidelines 1/2024 (Art. 6(1)(f)); EDPB Guidelines 05/2020 (consent) |
| **UK GDPR** | UK GDPR + Data Protection Act 2018 (DPA 2018) | ICO | ICO lawful basis guidance; DPA 2018 Schedule 1 (special categories); DUA Act 2025 |
| **Swiss FADP** | Federal Act on Data Protection (nDSG), eff. 1 Sep 2023 | FDPIC | FDPIC guidance [VERIFY — comprehensive guidance pending as of 2026] |

**Primary legal authority:**
- **Art. 6** — Lawful bases for processing; six conditions enumerated
- **Art. 7** — Consent conditions (withdrawal obligation; burden of proof on controller)
- **Art. 8** — Children's consent for information society services
- **Art. 9** — Prohibition on special category processing + 10 exceptions
- **Art. 10** — Criminal convictions and offences
- **Arts. 5(1)(a)(b)(c)(e)** — Lawfulness, purpose limitation, data minimisation, storage limitation
- **Art. 5(2)** — Accountability: ability to demonstrate compliance
- **Arts. 13(1)(c)/14(2)(c)** — Transparency: must disclose lawful basis in privacy notices
- **Arts. 17/18/20/21** — Data subject rights (apply differently per basis)
- **Art. 30** — ROPA: must record the lawful basis for every processing activity

**Key guidance documents:**
- EDPB Guidelines 2/2019 — Processing of personal data under Art. 6(1)(b) [VERIFY current version]
- EDPB Guidelines 05/2020 — Consent under Regulation 2016/679
- EDPB Guidelines 1/2024 — Processing of personal data based on legitimate interests (Art. 6(1)(f))
- ICO Guide to Lawful Basis — all six bases with decision trees
- WP29 Opinion 06/2014 — Concept of legitimate interests

**Major enforcement precedents (basis selection):**
- Meta €390M (Irish DPC, January 2023) — Art. 6(1)(b) inapplicable for behavioural advertising; processing not necessary for contract performance
- LinkedIn €310M (Irish DPC, October 2024) — Art. 6(1)(f) failed for targeted advertising; data subjects' rights override
- Meta €479M (AEPD, Spain, 2025) — Basis switch from consent to contract not permitted
- CJEU C-621/22 (KNLTB, 2024) — Commercial interests CAN constitute legitimate interest; balancing test remains critical

[JURISDICTION-SPECIFIC] Before final output, localise:
- Mandatory national derogations restricting specific bases in health, employment,
  financial services, and telecommunications sectors (Art. 23 GDPR)
- Member state age of consent thresholds for Art. 8 (13–16; EU default 16; UK 13)
- UK DPA 2018 Schedule 1 special category conditions (27 substantial public interest conditions)
- Supervisory authority published enforcement posture and sectoral guidance
- UK DUA Act 2025 Recognised Legitimate Interests — eliminates balancing test for
  specified purposes (commencement regulations pending [VERIFY date])

---

## Interactive Clarification

This skill uses **CLARIFY** prompts at decision points where the answer materially
changes the direction or outcome of the assessment. When marked **CLARIFY**, pause and
ask the user before proceeding. If the information is already available, skip the
prompt and proceed using stated assumptions.

CLARIFY topics in this skill (all in Step 2):
1. Jurisdiction(s) — EU / UK / Swiss / multi-regime
2. Data subject categories — employees, consumers, children, patients, vulnerable groups
3. Data categories — ordinary personal data, special category (Art. 9), criminal (Art. 10), children's
4. Processing type and purpose — what the organisation is trying to achieve
5. Entity type — private controller, public authority, or processor
6. Risk tolerance — conservative / pragmatic / strict escalation threshold
7. ROPA integration context — new activity vs. existing ROPA audit
8. Prior assessments — whether consent, DPIA, or LIA has already been conducted

---

## Workflow

### Step 1: Accept Input

Accept the processing activity in any of these formats:
- **Free text description**: "We want to process [data categories] for [purpose] by [means]"
- **ROPA extract**: An existing or draft record of processing activities entry
- **Project brief or technical specification**: Product documentation, system design doc
- **Data mapping output**: Output from `legalcode-data-mapping-workflow`
- **Multiple activities**: A list of processing activities for batch legal basis review

If no description is provided, prompt the user to supply one. At minimum, collect:
- Processing **purpose** — what the organisation is trying to achieve
- **Data categories** — what personal data is involved
- **Data subjects** — who the data relates to (employees, customers, public, children)
- **Processing means** — how data is collected, used, shared, stored
- **Retention period** — how long data will be kept
- **Controller identity** — whether a public authority or private organisation

For batch reviews of multiple processing activities, complete Steps 2–9 for each
activity separately, then produce a combined legal basis register in Step 10.

---

### Step 2: Gather Context

**CLARIFY** — Before beginning the assessment, ask the user the following. Present as
structured options. Skip any question already answered by the input material.

**1. Which jurisdiction(s) apply?**
- Options: EU GDPR only, UK GDPR only, Swiss FADP only, EU + UK, EU + UK + Swiss, Other
- *Why this matters*: Regime differences affect which Art. 9(2) conditions apply, the
  children's age threshold (EU: 16; UK: 13), and whether UK DUA Act 2025 Recognised
  Legitimate Interests are available.

**2. Who are the data subjects?**
- Options: Employees/staff, Consumers/customers, General public, Children (under 18),
  Patients/health service users, People in financial difficulty, Multiple groups
- *Why this matters*: Vulnerable data subjects attract heightened protection and may
  restrict which bases are viable (e.g., consent is rarely freely given by employees
  due to power imbalance).

**3. What categories of data are involved?**
- Multi-select: Ordinary personal data, Special-category data under Art. 9 (health,
  biometric, genetic, racial/ethnic origin, political opinions, religious beliefs, trade
  union membership, sex life, sexual orientation), Criminal conviction/offence data
  under Art. 10, Children's data, Financial data, Location data
- *Why this matters*: Special-category and criminal data require a separate legal
  condition (Art. 9(2) or Art. 10) in addition to an Art. 6 basis. Children's data
  triggers Art. 8 age/parental consent requirements.

**4. What type of processing is this?**
- Options: Marketing/advertising, Fraud prevention/security, Contract performance,
  Employment management, Legal/regulatory compliance, Research/analytics, Profiling,
  Intra-group transfers, Public service delivery, Medical treatment, Other
- *Why this matters*: Processing type directly signals which bases are viable (e.g.,
  contract performance is strongly linked to Art. 6(1)(b); legal compliance is strongly
  linked to Art. 6(1)(c)) and which EDPB guidance applies.

**5. Is the controller a public authority?**
- Options: Yes — public authority acting in official capacity, Yes — public body but
  acting outside official functions, No — private controller
- *Why this matters*: Public authorities acting in official capacity **cannot** rely on
  Art. 6(1)(f) (legitimate interests) for official functions per Art. 6(1) final clause.

**6. Risk tolerance / escalation approach?**
- Options: Conservative (flag CONDITIONAL outcomes, require explicit mitigations before
  proceeding), Pragmatic (accept CONDITIONAL with documented mitigations), Strict (any
  REQUIRES REVIEW triggers escalation to legal counsel)
- *Why this matters*: Affects how borderline basis assessments are classified and whether
  REQUIRES REVIEW findings trigger immediate remediation or documented acceptance.

**7. ROPA integration context?**
- Options: Assessing a new processing activity (no ROPA entry exists), Auditing an
  existing ROPA entry (current basis needs validation), Batch audit of multiple ROPA
  activities
- *Why this matters*: Determines the output format — standalone assessment report vs.
  ROPA field update vs. bulk assessment spreadsheet.

**8. Prior assessments completed?**
- Options: Consent already obtained (provide details), LIA already conducted (provide
  file), DPIA already conducted (provide file), No prior assessments
- *Why this matters*: If consent was previously obtained, assess whether it remains
  valid. If LIA was conducted, incorporate its conclusions into the Art. 6(1)(f) analysis
  rather than repeating the full three-part test.

---

### Step 3: Threshold Screening

Before assessing individual bases, run threshold checks that constrain which bases are
eligible.

**3a. Entity type constraint (public authority exclusion)**

If the controller is a public authority acting in official capacity:
- **ELIMINATE** Art. 6(1)(f) (legitimate interests) from viable candidates
- Add note: "Public authority acting in official capacity — Art. 6(1)(f) not available
  per final clause of Art. 6(1) GDPR"

**3b. Data category screening**

| Trigger | Art. overlay required | Action |
|---------|----------------------|--------|
| Health, biometric, genetic, racial/ethnic origin, political opinion, religious/philosophical belief, trade union membership, sex life, or sexual orientation data | Art. 9 overlay | Flag for Step 7 |
| Criminal conviction, offence, or related security measure data | Art. 10 overlay | Flag for Step 8 |
| Data relating to individuals under 18 in an Information Society Service context | Art. 8 overlay | Flag for Step 9 |
| None of the above | No overlay | Proceed to Step 4 |

Note: Art. 6 basis and Art. 9/10 conditions are **separate requirements**. Both must be
satisfied for special-category or criminal data processing. A valid Art. 6 basis alone
does not authorise special-category processing.

**3c. Preliminary scope note**

If multiple processing activities were submitted in Step 1, assign each a unique
Activity ID (A-001, A-002, etc.) and complete Steps 3–9 per activity before proceeding
to the batch legal basis register in Step 10.

---

### Step 4: Candidate Basis Triage

Screen all six Art. 6 bases with a quick pass/fail filter to identify viable candidates
for deep-dive analysis in Step 5. Assign each a preliminary triage status.

| Basis | Triage question | Preliminary status |
|-------|----------------|-------------------|
| **Art. 6(1)(a) — Consent** | Is genuine, freely given, informed, specific, unambiguous consent obtainable? Is the processing one where consent is practical (not employment context, not required for core service)? | VIABLE / UNCERTAIN / NOT VIABLE |
| **Art. 6(1)(b) — Contract** | Is the controller itself a party to the contract? Is the processing objectively necessary — not merely convenient — for contract performance? Does the data subject have a pre-existing or pending contractual relationship with this controller? | VIABLE / UNCERTAIN / NOT VIABLE |
| **Art. 6(1)(c) — Legal Obligation** | Can a specific EU or member state law obligation (not a contractual obligation, not foreign law) be identified that requires this exact processing? | VIABLE / UNCERTAIN / NOT VIABLE |
| **Art. 6(1)(d) — Vital Interests** | Does the processing protect someone's physical life (as a last resort, when consent is unobtainable)? Note: this basis is narrow and rarely applies in commercial processing. | VIABLE / UNCERTAIN / NOT VIABLE |
| **Art. 6(1)(e) — Public Task** | Is the controller a public authority or body acting in the public interest under clear member state law authority? Is processing necessary for that specific public function? | VIABLE / UNCERTAIN / NOT VIABLE |
| **Art. 6(1)(f) — Legitimate Interests** | Does a genuine, specific, real and present legitimate interest exist? Is the controller NOT a public authority acting in official capacity? | VIABLE / UNCERTAIN / NOT VIABLE |

For each VIABLE or UNCERTAIN candidate: proceed to deep-dive in Step 5.
For NOT VIABLE candidates: record reason and exclude from further analysis.

**CLARIFY** — If fewer than two bases appear viable after triage:
- If only one basis appears viable: confirm with the user before proceeding ("Based on
  the processing description, only Art. 6(1)(c) [legal obligation] appears viable. Is
  there additional context about the purpose or relationship that might open other bases?")
- If zero bases appear viable after triage: alert the user that the processing as
  described may lack a lawful basis, and ask whether to (a) reassess the processing
  purpose or scope, (b) consult specialist counsel, or (c) proceed with a documentation
  of no viable basis found.

---

### Step 5: Per-Basis Adequacy Analysis

For each VIABLE or UNCERTAIN basis identified in Step 4, conduct a structured adequacy
analysis. Use the framework below for each basis. Produce a three-part verdict per basis:
**ADEQUATE** (basis fully met), **REQUIRES REVIEW** (basis met with conditions or gaps),
or **INADEQUATE** (basis conditions not met).

---

#### 5a. Art. 6(1)(a) — Consent

**Eligibility criteria checklist:**

| Criterion | GDPR requirement | Assessment question | Status |
|-----------|-----------------|---------------------|--------|
| **Freely given** | Art. 4(11); Recitals 42-43 | Is consent genuinely voluntary? No negative consequence for refusal? No power imbalance (employment, state, financial dependency)? Not bundled with unrelated processing? | PASS / FAIL / PARTIAL |
| **Specific** | Art. 4(11); Art. 7(2) | Is consent requested separately for each distinct processing purpose? Not a blanket or generic consent? | PASS / FAIL / PARTIAL |
| **Informed** | Art. 7(2); Arts. 13/14 | Is the controller identified? Is the processing purpose disclosed? Is the right to withdraw explained? Is the right to object or erasure explained? | PASS / FAIL / PARTIAL |
| **Unambiguous affirmative action** | Art. 4(11); Recital 32 | Does consent require a positive act (ticking a box, clicking "Accept")? No pre-ticked boxes, no silence, no inactivity treated as consent? | PASS / FAIL / PARTIAL |
| **Withdrawable** | Art. 7(3) | Can withdrawal be exercised at any time, easily, without detriment? Is withdrawal as easy as giving consent? | PASS / FAIL / PARTIAL |
| **Documented** | Art. 7(1) | Can the controller demonstrate that consent was given (date, mechanism, version of notice)? | PASS / FAIL / PARTIAL |
| **Not conditional** | Recital 43 | Is consent not a condition for accessing a service unless the processing is strictly necessary for that service? | PASS / FAIL / PARTIAL |
| **Not exploiting imbalance** | Art. 7(4) | For employment context: is genuine freedom of choice demonstrated despite the employer-employee power imbalance? (Note: EDPB considers this rarely possible.) | PASS / FAIL / N/A |

**Necessity assessment (consent-specific):**

Art. 6(1)(a) does not have a necessity test in the same sense as other bases — the
consent itself provides the lawful basis. However, assess:
- Is consent the most appropriate and robust basis for this processing, or would another
  basis provide greater certainty (e.g., Art. 6(1)(b) for contract, Art. 6(1)(c) for
  legal obligation)?
- Risk flag: Consent is **revocable at any time** (Art. 7(3)). Processing must cease
  immediately on withdrawal unless another basis applies. If no fallback basis exists,
  consent creates ongoing operational risk.

**Special issues for Art. 6(1)(a):**

- **Art. 9 special categories**: Explicit consent (heightened standard — clear affirmative
  statement; not merely unambiguous) required under Art. 9(2)(a); verbal or implied
  consent insufficient
- **Children (Art. 8)**: For information society services, parental consent required for
  children below the applicable age threshold (EU: 16; UK: 13; member state may lower to
  minimum 13 for EU)
- **Research and archiving**: Special considerations for consent in research contexts
  (Art. 89 — consent may be waived for compatible research)

**Classification:**
- **ADEQUATE**: All eligibility criteria PASS; withdrawal mechanism operational; documented
- **REQUIRES REVIEW**: One or more criteria PARTIAL; power imbalance risk; documentation gaps
- **INADEQUATE**: Pre-ticked boxes; bundled consent; no withdrawal mechanism; employment context without demonstrated freedom; not documented

---

#### 5b. Art. 6(1)(b) — Performance of a Contract

**Eligibility criteria checklist:**

| Criterion | GDPR requirement | Assessment question | Status |
|-----------|-----------------|---------------------|--------|
| **Controller is party** | Art. 6(1)(b) | Is the controller itself a party to the contract? (Not a third party's contract.) | PASS / FAIL |
| **Data subject is the contracting party** | Art. 6(1)(b) | Is the data subject the other party to the contract? Processing for a third party's benefit does not satisfy this basis. | PASS / FAIL |
| **Necessity for performance** | Art. 6(1)(b) | Is the processing **objectively necessary** to perform the contract — not just required because the controller included it in the terms? Apply EDPB Guidelines 2/2019 [VERIFY] "inextricably linked" test. | PASS / FAIL / PARTIAL |
| **Pre-contractual steps** | Art. 6(1)(b) | If relying on pre-contractual steps: were these steps taken **at the request of the data subject**? Not at the controller's initiative. | PASS / FAIL / N/A |
| **Purpose limitation** | Art. 5(1)(b) | Is the processing purpose limited to what is necessary for contract performance? Does it extend to purposes that benefit the controller rather than being necessary for the data subject's contract? | PASS / FAIL / PARTIAL |

**EDPB Guidelines 2/2019 necessity test for Art. 6(1)(b):**

Processing is necessary for contract performance only when:
1. The contract **cannot be performed** without the processing; AND
2. The data subject **cannot reasonably be expected** to receive the contracted service
   without the processing.

**Common FAILS:**

| Processing | Common misapplication | Why it fails |
|-----------|----------------------|-------------|
| Fraud analytics on purchase transactions | "Necessary for contract" | Fraud prevention is NOT necessary for delivery of the purchased goods; Art. 6(1)(f) is the appropriate basis |
| Behavioural advertising to platform users | "Necessary for free service contract" | LinkedIn €310M; Meta €390M — advertising at scale is not necessary to provide the platform service |
| Location tracking beyond delivery purposes | "Part of the service" | Only location data strictly necessary for the specific delivery is covered |
| Pre-service prospecting data | "Pre-contractual steps" | Pre-contractual steps must be at the data subject's request; outbound prospecting fails |

**Classification:**
- **ADEQUATE**: Processing inextricably linked to contract performance; would not be possible without it; pre-contractual steps at subject's request
- **REQUIRES REVIEW**: Processing partially necessary; some elements may exceed necessity; pre-contractual steps ambiguous
- **INADEQUATE**: Processing for controller's convenience; advertising or analytics beyond service necessity; no contract exists or controller is not a party

---

#### 5c. Art. 6(1)(c) — Legal Obligation

**Eligibility criteria checklist:**

| Criterion | GDPR requirement | Assessment question | Status |
|-----------|-----------------|---------------------|--------|
| **EU/member state law** | Art. 6(1)(c); Art. 6(3) | Can a specific EU regulation or member state law be identified that imposes the obligation? (Not foreign law. Not guidance, soft law, or best practice.) | PASS / FAIL |
| **Specific and foreseeable** | Recital 45 | Is the obligation sufficiently clear and foreseeable? Vague or implied obligations do not qualify. | PASS / FAIL / PARTIAL |
| **Necessity** | Art. 6(1)(c) | Is the processing necessary to comply with the obligation — not broader than what the law requires? | PASS / FAIL / PARTIAL |
| **No excess beyond obligation** | Art. 5(1)(c) | Does the processing go beyond what the specific legal obligation requires? | PASS / FAIL |
| **Processing serves the public interest** | Art. 6(3) | For EU law obligations: does the processing pursue a legitimate aim of general interest proportionate to the aim? | PASS / FAIL / PARTIAL |

**Identify the specific obligation:**

Record the specific legal obligation in full citation format:
```
Legal obligation: [Name of statute/regulation], [Jurisdiction], [Section/Article],
[Obligation text or summary], [Processing required by the obligation]
```

Examples of valid legal obligations:
- AML/CTF: UK Proceeds of Crime Act 2002 ss. 327-333 / EU AMLD6
- Tax: UK HMRC payroll reporting (PAYE) / EU VAT Directive
- Employment: UK Statutory sick pay reporting / Working Time Regulations 1998
- Financial services: FCA regulatory reporting obligations
- Health and safety: RIDDOR reporting requirements (UK)

[JURISDICTION-SPECIFIC] Always verify the specific national implementing legislation.
GDPR itself can be a legal obligation basis for DPA compliance requirements (e.g., Art.
33 breach reporting to supervisory authority).

**Classification:**
- **ADEQUATE**: Specific, identified EU/member state law obligation; processing is strictly necessary to comply; no excess
- **REQUIRES REVIEW**: Obligation identified but scope of necessary processing is ambiguous; legal analysis required to determine minimum necessary scope
- **INADEQUATE**: No specific legal obligation identified; obligation is contractual not statutory; foreign law obligation; guidance/soft law; processing exceeds minimum required

---

#### 5d. Art. 6(1)(d) — Vital Interests

**Eligibility criteria checklist:**

| Criterion | GDPR requirement | Assessment question | Status |
|-----------|-----------------|---------------------|--------|
| **Life-threatening situation** | Art. 6(1)(d); Recital 46 | Is the processing necessary to protect the life of the data subject or another person? Not financial interests, contractual interests, or reputational interests. | PASS / FAIL |
| **Last resort** | Recital 46 | Could another basis (consent, legal obligation, legitimate interest) have been relied upon instead? Vital interests apply only where other bases are unavailable. | PASS / FAIL |
| **Consent unobtainable** | Recital 46 | If the processing involves the data subject's own vital interests: is it impossible or unreasonable to obtain consent (e.g., data subject is incapacitated)? | PASS / FAIL |
| **Necessity** | Art. 6(1)(d) | Is the specific processing activity necessary for the life-protection purpose, or would less intrusive means suffice? | PASS / FAIL |

**Scope note:** Vital interests is an extremely narrow basis applying almost exclusively
to medical emergencies, disaster response, and similar life-safety contexts. It is
very rarely the correct basis for commercial processing activities.

**Classification:**
- **ADEQUATE**: Clear life-threatening situation; other bases unavailable; processing strictly necessary
- **REQUIRES REVIEW**: Life risk plausible but other bases not fully assessed; necessity of specific processing unclear
- **INADEQUATE**: No imminent life risk; financial/contractual interests; other bases available; deployed as fallback convenience basis

---

#### 5e. Art. 6(1)(e) — Public Task

**Eligibility criteria checklist:**

| Criterion | GDPR requirement | Assessment question | Status |
|-----------|-----------------|---------------------|--------|
| **Public authority or public function** | Art. 6(1)(e); Recital 45 | Is the controller a public authority, OR is the controller performing a task in the public interest or exercising official authority? | PASS / FAIL |
| **Clear legal basis for the task** | Art. 6(3); Recital 45 | Is the public task/official authority grounded in a clear, specific EU or member state law provision? | PASS / FAIL |
| **Necessity for the task** | Art. 6(1)(e) | Is the specific processing necessary to carry out the identified public task — not merely convenient or useful? | PASS / FAIL / PARTIAL |
| **Not private commercial processing** | Art. 6(1) final clause | Is the processing in the exercise of official authority or public interest, rather than commercial activity? | PASS / FAIL |

[JURISDICTION-SPECIFIC] In the UK, this basis applies to public authorities under
DPA 2018 and to private bodies exercising statutory functions (e.g., regulatory bodies,
licensed broadcasters, qualifying professional bodies). The specific statutory function
must be identified.

**Classification:**
- **ADEQUATE**: Public authority/function clearly identified; specific legal basis for task; processing necessary for that task
- **REQUIRES REVIEW**: Public task plausible but scope of processing exceeds what the specific task requires; legal basis for task needs clarification
- **INADEQUATE**: Controller is a private entity with no public function; no identified statutory basis for the task; processing serves commercial rather than public interest

---

#### 5f. Art. 6(1)(f) — Legitimate Interests

**Scope note:** Art. 6(1)(f) requires a full three-part Legitimate Interest Assessment
(LIA). This section provides a summary adequacy check. For a complete, auditable LIA
following EDPB Guidelines 1/2024 with all four balancing factors, use
`legalcode-legitimate-interest-assessment`.

**Not available to:** Public authorities acting in their official capacity (final clause
of Art. 6(1)).

**Three-part adequacy summary:**

| Part | Test | EDPB authority | Assessment |
|------|------|----------------|------------|
| **Stage 1 — Purpose** | Is there a lawful, clearly and precisely articulated, real and present legitimate interest? | EDPB Guidelines 1/2024, paras. 18-47 | ADEQUATE / REQUIRES REVIEW / INADEQUATE |
| **Stage 2 — Necessity** | Is processing strictly necessary (not merely useful) to achieve the interest? Are there less intrusive alternatives? | EDPB Guidelines 1/2024, paras. 48-64 | ADEQUATE / REQUIRES REVIEW / INADEQUATE |
| **Stage 3 — Balancing** | Does the controller's interest outweigh the data subjects' interests, rights, and freedoms? (EDPB four-factor test: nature of data, likely impact, reasonable expectations, safeguards) | EDPB Guidelines 1/2024, paras. 65-115 | ADEQUATE / REQUIRES REVIEW / INADEQUATE |

**CLARIFY** — If the preliminary Stage 1 purpose assessment is REQUIRES REVIEW: ask the
user to articulate the specific interest more precisely before proceeding. A vague
purpose ("business improvement," "analytics," "security") cannot pass the balancing test.
EDPB Guidelines 1/2024 require the interest to be stated in a single, concrete sentence.

**Recognised legitimate interests (reduced scrutiny — Recitals 47-50):**
- Direct marketing to existing customers (Recital 47)
- Intra-group administrative transfers (Recital 48)
- Network and information security (Recital 49)
- Prevention of fraud and criminal acts threatening public security (Recital 50)

**UK DUA Act 2025 — Recognised Legitimate Interests:**
Under Schedule 4 of the UK Data (Use and Access) Act 2025, certain processing
categories are designated as Recognised Legitimate Interests (RLIs) with no balancing
test required. These include national security purposes, crime prevention/detection,
safeguarding, democratic engagement, and others. [VERIFY commencement date and
specific Schedule 4 list.]

**Classification:**
- **ADEQUATE**: All three stages pass; purpose specific; necessity demonstrated; balancing favours controller or safeguards implemented; LIA documented
- **REQUIRES REVIEW**: One or more stages borderline; safeguards can tip the balance but must be documented; full LIA recommended via `legalcode-legitimate-interest-assessment`
- **INADEQUATE**: Purpose fails (vague, unlawful, speculative); necessity fails (less intrusive alternatives not considered); balancing test fails (data subjects' rights clearly override)

---

### Step 6: Basis Recommendation and Ranking

After completing Step 5 for all viable bases, rank the candidates:

**Basis selection principles:**
1. **Precision first**: Choose the basis that best fits the processing purpose and provides
   the clearest legal grounding. Do not choose a weaker basis to avoid a harder test.
2. **No hierarchy**: GDPR does not rank the six bases — they are all equally legitimate
   when properly applied. Do not default to consent as "safest" when another basis fits better.
3. **Single basis per purpose**: Select one primary basis per processing purpose. Multiple
   bases may apply to different processing steps within an activity (e.g., contract for
   account creation, legal obligation for tax reporting, legitimate interest for fraud
   detection).
4. **Document before processing begins**: The basis must be identified and documented
   before processing starts. Retroactive justification is not permitted.
5. **No retrospective basis switching**: Once processing begins on a documented basis,
   switching to a different basis for the same purpose is prohibited by the EDPB. A change
   requires (a) stopping the original processing, (b) reassessing with the new basis, and
   (c) updating privacy notices before recommencing.

**Recommended ranking for common scenarios:**

| Scenario | Primary recommendation | Rationale |
|----------|----------------------|-----------|
| Payroll, tax reporting, PAYE | Art. 6(1)(c) | Specific legal obligation |
| Delivery of goods/services agreed in contract | Art. 6(1)(b) | Contractually necessary |
| Marketing to existing customers | Art. 6(1)(f) + Recital 47 | Recognised LI; Recital 47 baseline |
| Marketing to prospective customers | Art. 6(1)(a) or (f) | Consent or LI; depends on relationship |
| Emergency medical treatment | Art. 6(1)(d) + Art. 9(2)(c) | Vital interests (last resort) |
| Government statistical reporting | Art. 6(1)(e) | Public task/official authority |
| Fraud detection for financial services | Art. 6(1)(f) + Recital 50 | Recognised LI; Recital 50 baseline |
| Background checks (employment) | Art. 6(1)(b) or (c) | Contract or legal obligation; Art. 10 overlay required |
| Research analytics | Art. 6(1)(f) or (a) | LI (public interest) or consent; depends on context |

---

### Step 7: Article 9 Special Category Overlay

*Complete only if Step 3 flagged special-category data.*

Art. 9(1) prohibits processing of special-category data **unless** one of Art. 9(2)'s
ten conditions is met. A valid Art. 6 basis is necessary but **not sufficient** for
special-category processing — both Art. 6 and Art. 9(2) conditions must be satisfied.

**Art. 9(2) conditions — complete assessment table:**

| Condition | Art. 9(2) | Requirements | Common use cases | EU/UK note |
|-----------|----------|-------------|-----------------|------------|
| **(a) Explicit consent** | Art. 9(2)(a) | Higher standard than Art. 6 consent: clear affirmative statement to the specific special-category processing; cannot be implied | Biobank, clinical research, genetic screening | UK: explicit consent also sufficient in DPA 2018 |
| **(b) Employment/social security law** | Art. 9(2)(b) | Processing for rights/obligations in employment, social security law under EU/member state law; appropriate safeguards | Occupational health, disability accommodation, sick leave | UK: DPA 2018 Schedule 1, para. 1 (employment) |
| **(c) Vital interests** | Art. 9(2)(c) | Protection of vital interests where data subject physically or legally unable to give consent | Emergency medical; unconscious patient | Mirrors Art. 6(1)(d) — narrow scope |
| **(d) Not-for-profit bodies** | Art. 9(2)(d) | Processing by foundation/association for political, philosophical, religious, or trade union purposes; for members/former members; no disclosure outside body without consent | Trade union membership records; religious organisations | Must be membership-based; strict limits |
| **(e) Manifestly public data** | Art. 9(2)(e) | Data subject has manifestly made the data public themselves | Data subject discussed health publicly; openly disclosed political affiliation | Narrow: must be manifestly, deliberately made public |
| **(f) Legal claims** | Art. 9(2)(f) | Necessary for establishment, exercise, or defence of legal claims, or court acting in judicial capacity | Litigation support; insurance claims; HR investigations | Must be genuinely necessary; not precautionary |
| **(g) Substantial public interest** | Art. 9(2)(g) | Member state law; substantial public interest; proportionate; appropriate safeguards | Public health monitoring; equality monitoring; prevention of fraud | UK: DPA 2018 Schedule 1 Part 2 (27 specific conditions) [VERIFY] |
| **(h) Healthcare** | Art. 9(2)(h) | Medical/dental diagnosis, treatment, social medicine; EU/member state law or professional obligations; confidentiality obligation | Patient records; occupational medicine; prescription records | [JURISDICTION-SPECIFIC] — healthcare professional confidentiality obligations vary |
| **(i) Public health** | Art. 9(2)(i) | Necessary for public health in public interest (epidemic, cross-border health threats); EU/member state law; appropriate safeguards | Public health surveillance; COVID-19 contact tracing; pandemic response | Narrow public health scope; not general health research |
| **(j) Research/statistics/archiving** | Art. 9(2)(j) | EU/member state law; scientific, historical, or statistical purposes; public interest; proportionate; Art. 89 safeguards | Academic research; national statistics; historical archives | Must satisfy Art. 89 safeguards (anonymisation where possible) |

**UK DPA 2018 Schedule 1 Part 2 — Substantial Public Interest Conditions:**
DPA 2018 provides 27 additional substantial public interest conditions [VERIFY full
list] including: preventing unlawful acts, safeguarding children, regulatory purposes,
journalism, equality monitoring, anti-doping, occupational pensions, and more. Each
condition has specific requirements for documented policy compliance.

**Art. 9 overlay classification per viable Art. 6 basis:**

For each Art. 6 basis identified as ADEQUATE or REQUIRES REVIEW in Step 5, assess
whether an Art. 9(2) condition is also met:

| Art. 6 basis | Compatible Art. 9(2) conditions | Incompatible/Restricted |
|-------------|--------------------------------|-------------------------|
| Art. 6(1)(a) consent | Art. 9(2)(a) explicit consent (must pair) | Cannot use regular consent for Art. 9 — explicit required |
| Art. 6(1)(b) contract | Art. 9(2)(b) employment law; (f) legal claims | No direct Art. 9 counterpart for pure contract basis; check if (b) or (h) fits |
| Art. 6(1)(c) legal obligation | Art. 9(2)(b) employment/SS law; (g) substantial public interest; (h) healthcare; (i) public health | Usually (b) or (g) will align |
| Art. 6(1)(d) vital interests | Art. 9(2)(c) vital interests | Direct alignment |
| Art. 6(1)(e) public task | Art. 9(2)(g) substantial public interest; (h) healthcare; (i) public health; (j) research | Depends on public function type |
| Art. 6(1)(f) legitimate interests | Art. 9(2)(g) (if member state law exists); (j) research; (e) manifestly public | Note: Art. 6(1)(f) + Art. 9(2)(g) requires specific member state law |

---

### Step 8: Article 10 Criminal Data Overlay

*Complete only if Step 3 flagged criminal conviction or offence data.*

Art. 10 GDPR provides that processing of personal data relating to criminal convictions,
offences, or related security measures may only be carried out:
- Under the control of official authority; OR
- When authorised by EU or member state law providing appropriate safeguards.

**Criminal data scope:**
- Criminal convictions (including spent/pardoned)
- Criminal offences (alleged or charged, not only convicted)
- Security measures associated with criminal proceedings

**Authorization assessment:**

| Path | Requirements | Status |
|------|-------------|--------|
| **Official authority** | Processing under the control of an official authority (courts, law enforcement, prosecutorial bodies) acting within their statutory function | AUTHORISED / NOT APPLICABLE |
| **Member state law authorization** | Specific EU or member state law provision that authorises processing of criminal data; with appropriate safeguards | AUTHORISED [cite law] / NOT AUTHORISED |

**UK DPA 2018 — Criminal offences conditions:**
DPA 2018 Schedule 1, Part 1, para. 36 — Criminal conviction data
May be processed for substantial public interest purposes listed in Schedule 1 Part 2;
same policy document requirements apply. [VERIFY current DPA 2018 Schedule 1 para. references]

**Common authorised contexts:**
- Background screening under sector-specific legislation (financial services, childcare)
- CRB/DBS checks (UK) under Police Act 1997 / Protection of Children Act 1999
- AML/KYC obligations (criminal proceeds identification) under money laundering regulations
- Employment law contexts where spent convictions can be disclosed
- Insurance claims involving criminal allegations

**Art. 10 overlay classification:**
- **COMPATIBLE**: Specific authorization or official authority identified; appropriate safeguards in place
- **REQUIRES REVIEW**: Processing involves criminal data but authorization is indirect or unclear; legal analysis needed
- **NOT COMPATIBLE**: No official authority; no member state law authorization; criminal data being processed without authorisation

---

### Step 9: Article 8 Children's Data Overlay

*Complete only if Step 3 flagged children's data in an information society service (ISS) context.*

**Art. 8 scope:** Art. 8 applies when:
1. Processing is for the offer of **information society services** (ISS — online services offered directly to children); AND
2. The lawful basis relied upon is **consent** (Art. 6(1)(a))

Note: Art. 8 does NOT apply when the lawful basis is not consent (e.g., contract,
legal obligation). If relying on a non-consent basis for children's data, Art. 8 does
not impose additional conditions beyond the standard basis analysis — though child-
specific data protection considerations (heightened protection, best interests of the
child) still apply under Art. 5(1)(a) and EDPB guidance.

**Age threshold assessment:**

| Regime | Age of consent | Below threshold requirement |
|--------|---------------|---------------------------|
| **EU GDPR** | 16 years (Art. 8(1)) | Parental consent required |
| **EU GDPR — member state lower limit** | 13–15 years (member state may lower to minimum 13) | Parental consent required for those below member state's chosen threshold |
| **UK GDPR** | 13 years (DPA 2018 s.9) | Parental consent required for under-13s |
| **Swiss FADP** | No specific ISS age threshold; general consent capacity rules apply | [VERIFY FDPIC guidance on children] |

**Parental consent verification:**

| Requirement | GDPR | Assessment |
|-------------|------|-----------|
| Reasonable efforts to verify age | Art. 8(2) | Does the ISS implement age verification? What method? (Attribute-based — yes/no over threshold — preferred over ID collection) |
| Verification of parental responsibility | Art. 8(2) | For under-threshold users: is there a mechanism to obtain and verify parental/guardian consent? |
| Avoid excessive data collection for verification | Art. 5(1)(c) | Age verification mechanism must be proportionate; avoid collecting more personal data than necessary |

**ICO Children's Code (Age Appropriate Design Code):**
UK controllers offering services likely accessed by children must also comply with the
ICO Age Appropriate Design Code (s.123 DPA 2018). The Code's 15 standards apply
regardless of which lawful basis is used. [JURISDICTION-SPECIFIC — applies to UK only]

**Art. 8 overlay classification:**
- **COMPLIANT**: Correct age threshold applied; parental consent mechanism operational; reasonable verification
- **REQUIRES REVIEW**: Age threshold unclear; verification mechanism not implemented; design may be accessible to children without age check
- **NON-COMPLIANT**: No age check; under-threshold children using service with no parental consent; no verification efforts

---

### Step 10: Final Legal Basis Determination

Synthesise the per-basis analysis from Steps 5–9 into a final determination.

**10a. Select primary basis**

Identify the strongest single basis for each processing purpose based on:
- All three adequacy criteria met (ADEQUATE in Step 5)
- Compatible Art. 9(2) condition (if applicable)
- Art. 10 authorization (if applicable)
- Art. 8 compliance (if applicable)
- Downstream rights implications (see Rights Matrix in the Frameworks section)

**10b. Identify fallback bases (optional but recommended)**

Document whether any secondary bases could apply if the primary basis fails. Note: this
is not basis-switching — it is advance planning for scenarios where circumstances change
(e.g., if consent is withdrawn, does legitimate interest provide a fallback?).

**10c. Flag basis-change risks**

If the processing currently relies on a documented basis and a change is being
considered, apply the basis-change rules:

- Changing basis **before processing begins**: PERMITTED — update privacy notice and ROPA
- Changing basis **after processing has begun on a different documented basis**: GENERALLY
  PROHIBITED per EDPB guidance. Exceptions:
  1. The original basis has become inapplicable due to changed circumstances (e.g., contract
     terminated → Art. 6(1)(b) no longer valid → may switch to consent or LI if conditions met)
  2. The change is to correct an erroneous original basis selection (remediation)
  3. A new, separate processing purpose is being added (this is NOT basis-switching — it
     is adding a new activity requiring its own basis)

**10d. Consent refresh analysis**

If the assessment involves existing consent, evaluate whether consent remains valid:

| Trigger | Reassessment required? |
|---------|----------------------|
| Processing purpose has changed since consent was obtained | YES — new consent required for the new purpose |
| Privacy notice has materially changed | YES — re-inform; may require fresh consent |
| Change in controller identity (acquisition, merger) | YES — new controller must re-obtain or confirm consent |
| Consent was not freely given (power imbalance identified) | YES — remediate or change basis |
| Consent was obtained without adequate disclosure | YES — retroactively invalid; immediate remediation |
| Time elapsed / relationship changed (consent is "stale") | ASSESS — no fixed expiry; factor in nature of processing and reasonable expectations |

**10e. Assign overall classification**

| Classification | Conditions |
|----------------|-----------|
| **APPROVED** | Primary basis ADEQUATE; any required Art. 9/10/8 overlays satisfied; no remediation required before processing |
| **CONDITIONAL** | Primary basis REQUIRES REVIEW or one overlay REQUIRES REVIEW; specified remediations must be completed before relying on this basis |
| **REJECTED** | No viable basis found; or primary basis INADEQUATE; or Art. 9/10/8 overlay conditions unmet; processing must not proceed without fundamental redesign |

---

## Data Subject Rights Matrix

The selected lawful basis determines which data subject rights apply:

| Right | Art. | Consent (a) | Contract (b) | Legal obligation (c) | Vital interests (d) | Public task (e) | Legitimate interests (f) |
|-------|------|-------------|-------------|---------------------|--------------------|-----------------|-----------------------|
| **Erasure** | 17 | YES — on withdrawal or purpose achieved | YES — when no longer necessary | LIMITED — unless processing exceeds obligation | LIMITED | LIMITED — public interest override possible | YES — if interests do not override |
| **Portability** | 20 | YES — automated processing | YES — automated processing | NO | NO | NO | NO |
| **Object** | 21 | Not applicable (withdrawal covers this) | Not applicable | Not applicable | YES | YES — unless compelling grounds | YES — unless compelling grounds; absolute for direct marketing |
| **Restriction** | 18 | YES — pending withdrawal | YES — accuracy contested; erasure dispute | YES — accuracy contested | YES | YES | YES |
| **Rectification** | 16 | YES | YES | YES | YES | YES | YES |
| **Not be subject to automated decision** | 22 | Only with explicit consent | If necessary for contract | If authorised by EU/member state law | N/A | If authorised by EU/member state law | Cannot ground Art. 22 solely automated decisions |

---

## Basis Change and Multiple Bases

**Core rule — one basis per purpose:** Each processing purpose requires exactly one
identified lawful basis. Document the basis before processing commences.

**Multiple purposes → multiple bases:** A single processing activity may serve multiple
purposes, each with its own basis:
- Example: Customer purchase data — Art. 6(1)(b) for order fulfilment, Art. 6(1)(c)
  for VAT records, Art. 6(1)(f) for fraud detection. Each purpose is documented separately.

**Prohibition on basis switching (post-commencement):**
EDPB position (EDPB Guidelines 2/2019; confirmed in enforcement decisions): Once
processing has commenced under a documented basis, swapping to a different basis for
the same purpose is not permitted. The accountability principle (Art. 5(2)) and
transparency principle (Art. 5(1)(a)) require that the basis be fixed at the outset so
data subjects can rely on the basis stated in privacy notices.

**When basis change is permitted:**
1. Before processing commences — update draft privacy notice and ROPA
2. Original basis genuinely no longer applies (contract terminated; legal obligation
   repealed) AND the change is disclosed to data subjects under Art. 13/14
3. The "change" is actually a new processing purpose requiring a new assessment

**Documentation requirements for any basis change:**
- Date of original basis and date of change
- Reason for change (changed circumstances or original error)
- Updated ROPA entry
- Updated privacy notice with notification to data subjects where required
- DPO/legal sign-off record

---

## Severity Classification

Apply to each basis adequacy finding and each overlay check:

**Per-basis classification:**

| Classification | Criteria |
|----------------|---------|
| **ADEQUATE** | ALL eligibility criteria for the basis are PASS; necessity confirmed; no significant gaps; documented and ready for ROPA recording |
| **REQUIRES REVIEW** | One or more eligibility criteria are PARTIAL; necessity plausible but not fully documented; safeguards or conditions should be implemented before reliance; LIA, expert review, or additional documentation required |
| **INADEQUATE** | One or more core eligibility criteria FAIL; basis not available for this processing purpose; do not rely on this basis |

**Overall determination:**

| Classification | Criteria |
|----------------|---------|
| **APPROVED** | Primary basis ADEQUATE; all required overlays (Art. 9/10/8) satisfied; ROPA ready |
| **CONDITIONAL** | Primary basis REQUIRES REVIEW; specified actions must be completed within documented timeline; document conditions and implement before relying |
| **REJECTED** | No viable basis found; primary basis INADEQUATE; Art. 9/10/8 overlay unresolvable; processing must not proceed as described |

---

## Prioritization Framework

Triage findings by urgency:

| Priority | Classification | Action |
|----------|---------------|--------|
| **Immediate** | REJECTED — no viable basis; Art. 9 processing without condition; Art. 10 processing without authorisation | Stop processing; escalate to DPO/counsel immediately |
| **Near-term (14 days)** | CONDITIONAL — primary basis REQUIRES REVIEW; critical overlay gap (Art. 8 age check missing) | Implement required conditions; update ROPA/privacy notice |
| **Planned (30–90 days)** | REQUIRES REVIEW — documentation gaps; consent refresh needed; basis-change documentation required | Document, assign ownership, set review date |
| **Ongoing** | APPROVED — periodic reassessment due date | Set reassessment calendar (annually or on material change) |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise.

| Gate | Rule | Fail action |
|------|------|-------------|
| **Source** | Every legal claim cites Art. 6, GDPR recital, EDPB guideline, case law, or DPA enforcement decision | Add citation or mark **[UNVERIFIED]** |
| **Format** | All citations follow consistent format: `Art. 6(1)(f) GDPR`, `Recital 47 GDPR`, `EDPB Guidelines 1/2024`, `CJEU C-621/22` | Fix format |
| **Currency** | Every cited provision and guideline checked for amendments (EDPB guidance updates; DUA Act 2025 UK; EU Omnibus package) | Flag **[CHECK CURRENCY]** |
| **Domain** | Analysis stays within GDPR/UK GDPR framework; no CCPA/LGPD/PDPA concepts introduced unless explicitly flagged as other regime | Remove or flag cross-regime bleed |
| **Confidence** | All uncertainties explicitly stated; no hidden gaps or assumed positions | Add confidence qualifier |

### Self-Interrogation for REJECTED or INADEQUATE Findings

For any REJECTED overall outcome or INADEQUATE per-basis finding, apply this three-pass
review before delivering:

**Pass 1 — Legal Chain Integrity:** Does the INADEQUATE finding follow logically from
the stated eligibility criteria and GDPR text? Would the DPA/EDPB reach the same
conclusion on these facts?

**Pass 2 — Completeness:** Have all viable bases been genuinely considered? Have the
most recent enforcement precedents (Meta, LinkedIn, etc.) been applied? Are there
Art. 9(2) conditions not yet considered?

**Pass 3 — Challenge:** What is the strongest argument that this processing DOES have a
valid basis? Under what circumstances might the INADEQUATE finding be reversed (e.g.,
if additional information were available or safeguards were implemented)?

### Confidence Scoring

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95–1.0 | GDPR text unambiguous; EDPB guidance directly on point | State with confidence |
| **High** | 0.80–0.94 | Strong authority; minor interpretive questions | State with brief caveat |
| **Probable** | 0.60–0.79 | Good arguments; enforcement could differ; guidance general | State with reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuinely uncertain; depends on unreported facts or value judgments | Flag for professional review; present both sides |
| **Unlikely** | 0.0–0.39 | Weak evidentiary basis; speculative; major information gaps | Do not assert; flag **[UNCERTAIN]**; recommend counsel |

---

## Anti-Patterns

What NOT to do when assessing or documenting a GDPR lawful basis:

1. **Defaulting to consent** — Treating Art. 6(1)(a) as the "safe" default when another
   basis (contract, legal obligation, legitimate interest) would be more appropriate and
   more robust. Consent is the weakest basis because it is revocable.

2. **Confusing basis with purpose** — The basis is the legal ground (Art. 6(1)(f)); the
   purpose is what processing achieves (fraud prevention). These are not interchangeable.
   Recording "fraud prevention" as the lawful basis is incorrect.

3. **Art. 6 without Art. 9 for special category data** — Believing a valid Art. 6 basis
   is sufficient for special-category processing. Art. 9(1) imposes a separate prohibition
   that requires its own condition under Art. 9(2). Both must be satisfied independently.

4. **Necessity inflation for Art. 6(1)(b)** — Designing a contract that includes processing
   terms and then claiming the processing is "necessary for the contract." EDPB: necessity
   is assessed against the underlying purpose of the contract, not the contractual terms
   the controller drafted.

5. **Behavioural advertising as contract necessity** — The most-fined misapplication.
   Advertising, analytics, and profiling are not necessary to perform the core service
   contract. Meta €390M and LinkedIn €310M both stemmed from this error.

6. **Post-commencement basis switching** — Attempting to change from consent to legitimate
   interests after consent was withdrawn (or vice versa) for the same processing purpose.
   The EDPB has confirmed this is not permitted. Meta €479M (Spain, 2025) is the leading
   enforcement case.

7. **Foreign law as legal obligation** — Claiming Art. 6(1)(c) when the obligation arises
   from foreign law (e.g., US FISA, Chinese data security law). The obligation must be
   under EU or member state law. Foreign law obligations may sometimes be pursued under
   Art. 6(1)(f) but require a full LIA.

8. **Guidance and best practice as legal obligation** — Treating regulatory guidance, sector
   codes of practice, or voluntary standards as "legal obligations." Art. 6(1)(c) requires
   binding law, not recommended practice.

9. **Consent as fallback when LI fails** — Attempting to "fall back" to consent when the
   LIA reveals a weak balancing outcome. If consent is the basis, data subjects must be
   genuinely free to refuse without consequences — which may not be achievable if the
   processing is commercially important.

10. **Employment consent as freely given** — Assuming employees can freely consent to
    processing. EDPB guidance is clear: due to the power imbalance in the employment
    relationship, employee consent is generally not freely given. Art. 6(1)(b) or (c)
    are typically more appropriate bases for employee data processing.

11. **No consent withdrawal mechanism** — Documenting Art. 6(1)(a) as the basis without
    operational infrastructure to process consent withdrawals immediately and trace their
    downstream effect on processing.

12. **Stale consent** — Relying on consent obtained years earlier without reassessing
    whether the scope, purpose, or technology has materially changed since consent was
    given.

13. **Bundled consent** — Embedding consent for optional processing into acceptance of
    general terms and conditions. Art. 7(2) and EDPB Guidelines 05/2020 prohibit this.
    Consent must be granular per purpose.

14. **Art. 6(1)(d) as operational fallback** — Using vital interests as a convenient
    basis when consent is difficult to obtain. Vital interests requires a genuinely
    life-threatening situation where other bases are unavailable.

15. **Ignoring the rights matrix** — Selecting a basis without considering the downstream
    data subject rights consequences. Choosing Art. 6(1)(b) over (f) removes the right
    to object; choosing (a) over (b) adds a right to portability.

16. **Not recording the basis before processing** — Starting processing and retroactively
    documenting a basis after a data subject request or regulatory inquiry. The
    accountability principle (Art. 5(2)) requires advance documentation.

17. **Treating ROPA lawful basis field as a formality** — Recording generic descriptions
    ("legitimate interest" or "consent") without specifying the concrete interest or the
    specific consent mechanism. ROPA entries should be specific enough for supervisory
    authority scrutiny.

18. **Art. 9(2)(g) without member state law** — Claiming substantial public interest as
    a special-category condition without identifying the specific member state law provision
    that authorises the processing and the specific safeguards required.

19. **Children's services without age check** — Offering a digital service that may be
    used by children without implementing age verification and parental consent mechanisms
    before collecting personal data.

20. **Multiple purposes, single basis** — Recording one basis for a processing activity
    that actually serves multiple distinct purposes with different appropriate bases. Each
    purpose needs its own basis documented in the ROPA.

21. **Ignoring basis change notification** — Changing the basis for ongoing processing
    without updating the privacy notice and notifying data subjects under Arts. 13/14.

22. **Claiming Art. 6(1)(e) without identifying the statutory function** — Public task
    basis requires a specific, identifiable statutory function. Vague "public interest"
    without a legal basis fails the Art. 6(3) requirement.

---

## Writing Standards

Before delivering any output, verify:

- [ ] Every lawful basis cited using the precise GDPR article reference (e.g.,
  "Art. 6(1)(f) GDPR" not "legitimate interests" alone)
- [ ] Special-category conditions cited as "Art. 9(2)(x) GDPR" + member state law where applicable
- [ ] Every EDPB guideline cited with version and date (e.g., "EDPB Guidelines 1/2024
  on legitimate interests, adopted 8 October 2024")
- [ ] All unverified legal claims marked [VERIFY]
- [ ] All jurisdiction-specific content marked [JURISDICTION-SPECIFIC]
- [ ] Plain language used in recommended ROPA field entries (not legal jargon)
- [ ] Specific, concrete legitimate interest stated (not "business purposes")
- [ ] Specific legal obligation identified by statute name, section, and jurisdiction
- [ ] Confidence scores applied to assessments with non-obvious outcomes
- [ ] Glass Box audit trail completed

---

## External Tool Integration

### legalcode-mcp (if connected)

Use legalcode-mcp to verify and enrich the assessment before delivery:
- Search for the specific national implementing legislation for Art. 6(1)(c) legal
  obligations in the applicable member state(s)
- Search for recent EDPB binding decisions and consistency mechanism opinions on the
  specific processing type
- Search for supervisory authority enforcement decisions involving the same or similar
  basis claims
- Search for Art. 9(2) condition requirements in the specific member state

Mark all legalcode-mcp sourced citations as VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**
- Mark statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed on the basis of known GDPR text and EDPB guidance

### Skill family integration

| Trigger | Action |
|---------|--------|
| Art. 6(1)(f) selected as primary or fallback basis | Launch `legalcode-legitimate-interest-assessment` for full three-part LIA |
| Step 10 classification is APPROVED but processing involves large-scale, systematic, or novel data use | Recommend `legalcode-dpia-generator` for DPIA trigger assessment |
| Assessment produces ROPA-ready legal basis assignment | Pass output to `legalcode-ropa-generator` for ROPA population |
| Privacy notice update required | Pass basis disclosure language to `legalcode-privacy-policy-drafter` |
| Processing involves cross-border data transfers | Flag for `legalcode-cross-border-transfer-assessment` |

---

## Glass Box Audit Trail

Every legal basis assessment output must include this YAML block:

```yaml
glass_box:
  skill: "legalcode-gdpr-legal-basis-assessment"
  assessment_date: "[YYYY-MM-DD]"
  activity: "[Processing activity name or ID]"
  organisation: "[Name or 'Not specified']"
  jurisdiction: "[EU GDPR / UK GDPR / Swiss FADP / Multi]"
  entity_type: "[Private controller / Public authority / Processor]"
  data_categories:
    ordinary: true/false
    special_category: true/false
    art9_condition: "[Art. 9(2)(?) or 'Not applicable']"
    criminal_data: true/false
    art10_authorization: "[Authorization citation or 'Not applicable']"
    children_data: true/false
    art8_compliant: "true/false/Not applicable"
  bases_screened: 6
  bases_viable: "[List of viable bases]"
  bases_inadequate: "[List of inadequate bases with reason]"
  primary_basis: "[Art. 6(1)(?) — [name]]"
  fallback_basis: "[Art. 6(1)(?) or 'None identified']"
  overall_classification: "APPROVED / CONDITIONAL / REJECTED"
  confidence: "DEFINITE / HIGH / PROBABLE / POSSIBLE / UNLIKELY"
  basis_change_risk: "[None / Low / Medium / High — reasoning]"
  consent_refresh_required: "true/false/Not applicable"
  dpia_recommended: "true/false — [reason if true]"
  lia_required: "true/false — [if Art. 6(1)(f) selected]"
  ropa_update_required: "true/false"
  privacy_notice_update_required: "true/false"
  legalcode_mcp: "Connected / Not connected"
  citations_verified: "[N] VERIFIED / [N] UNVERIFIED"
  self_interrogation: "PASS / REVISED — [note if revised]"
  limitations:
    - "[Any scope limitations, missing information, or assumptions]"
  reviewer: "AI-assisted — requires qualified legal review before reliance"
```

---

## Output Format Template

Every legal basis assessment output must follow this structure:

```markdown
# GDPR Legal Basis Assessment — [Processing Activity Name]

**Organisation**: [Name or "Not specified"]
**Assessment date**: [YYYY-MM-DD]
**Assessor**: [Name/role]
**Jurisdiction(s)**: [EU GDPR / UK GDPR / Swiss FADP]
**Processing activity**: [One-sentence description]
**Activity ID**: [ROPA activity ID if available]
**Next reassessment due**: [Date or trigger condition]

---

## Executive Summary

**Recommended lawful basis**: Art. 6(1)(?) — [Name]
**Art. 9(2) condition** (if applicable): Art. 9(2)(?) — [Name]
**Art. 10 authorization** (if applicable): [Authorization or N/A]
**Art. 8 children's data** (if applicable): [COMPLIANT / REQUIRES REVIEW / N/A]
**Overall classification**: APPROVED / CONDITIONAL / REJECTED

| Basis | Viability | Art. 9 | Art. 10 | Art. 8 | Overall |
|-------|-----------|--------|---------|--------|---------|
| Art. 6(1)(a) Consent | ADEQUATE/REQ. REVIEW/INADEQUATE | Compatible/Conflict/N/A | N/A | COMPLIANT/REQ/N/A | VIABLE/NOT |
| Art. 6(1)(b) Contract | ADEQUATE/REQ. REVIEW/INADEQUATE | — | N/A | — | VIABLE/NOT |
| Art. 6(1)(c) Legal Obligation | ADEQUATE/REQ. REVIEW/INADEQUATE | — | — | — | VIABLE/NOT |
| Art. 6(1)(d) Vital Interests | ADEQUATE/REQ. REVIEW/INADEQUATE | — | — | — | VIABLE/NOT |
| Art. 6(1)(e) Public Task | ADEQUATE/REQ. REVIEW/INADEQUATE | — | — | — | VIABLE/NOT |
| Art. 6(1)(f) Legitimate Interests | ADEQUATE/REQ. REVIEW/INADEQUATE | — | — | — | VIABLE/NOT |

**Key finding**: [One sentence — why the recommended basis is the strongest; why alternatives fail]
**Recommended action**: [One sentence — what to do next]

---

## Basis Assessment — [Art. 6(1)(?) Name]

**Why selected as primary**: [Rationale]

**Eligibility criteria assessment**:

| Criterion | Requirement | Assessment | Status |
|-----------|------------|------------|--------|
| [Criterion 1] | [GDPR requirement] | [Analysis] | PASS/FAIL/PARTIAL |
| ... | ... | ... | ... |

**Necessity assessment**: [Analysis]

**Special issues**: [Any consent withdrawal, employment imbalance, or other flags]

**Classification**: ADEQUATE / REQUIRES REVIEW / INADEQUATE
**Confidence**: [Level and rationale — cite EDPB/case law where applicable]

---

## Basis Assessment — [Alternative Bases]

[Repeat block above for each assessed basis, even if INADEQUATE — document why]

---

## Special Category / Criminal Data / Children's Data Overlays

[Include only the applicable sections]

### Art. 9 Special Category Overlay

**Art. 9(2) condition identified**: [Art. 9(2)(?) — name]
**Assessment**: [How the condition applies; member state law if Art. 9(2)(g)]
**Classification**: ADEQUATE / REQUIRES REVIEW / INADEQUATE

### Art. 10 Criminal Data Overlay

**Authorization identified**: [Art. 10 path — official authority or member state law]
**Classification**: COMPATIBLE / REQUIRES REVIEW / NOT COMPATIBLE

### Art. 8 Children's Data Overlay

**Age threshold applicable**: [EU 16 / UK 13 / Member state threshold]
**Parental consent required for**: [Age range]
**Verification mechanism**: [In place / Planned / Missing]
**Classification**: COMPLIANT / REQUIRES REVIEW / NON-COMPLIANT

---

## Downstream Data Subject Rights

| Right | Applies under this basis? | Notes |
|-------|--------------------------|-------|
| Erasure (Art. 17) | YES / LIMITED / NO | [Conditions] |
| Portability (Art. 20) | YES / NO | [Automated processing requirement] |
| Object (Art. 21) | YES / NO | [Override conditions] |
| Restriction (Art. 18) | YES | [Circumstances] |
| Rectification (Art. 16) | YES | [Always applies] |
| Not subject to automated decisions (Art. 22) | YES / LIMITED / NO | [Conditions] |

---

## Basis-Change and Consent Refresh

**Current documented basis** (if auditing existing activity): [Art. 6(1)(?)]
**Basis-change risk**: [None / Low / Medium / High — reasoning]
**Consent refresh required**: [Yes — trigger conditions / No / N/A]

---

## Findings and Remediation Plan

| Finding ID | Basis/Overlay | Severity | Finding | Required Action | Owner | Due |
|-----------|---------------|---------|---------|----------------|-------|-----|
| LBA-001 | [Basis] | [IMMEDIATE/NEAR-TERM/PLANNED] | [Description] | [Specific action] | [Role] | [Date] |

---

## ROPA and Privacy Notice Integration

**ROPA field update — lawful basis**:
```
Art. 6(1)(?) — [specific purpose or interest statement]
[Art. 9(2)(?) — [condition] — if special category data]
```

**Privacy notice update required?** [Yes / No]
**Required disclosure language** (Arts. 13/14):
```
Lawful basis: We process your [data type] on the basis of [Art. 6(1)(?) description]
[for special categories: We process your [special category] data on the additional
basis of [Art. 9(2)(?) description]]
```

**DPIA recommended?** [Yes — trigger legalcode-dpia-generator / No]
**LIA required?** [Yes — trigger legalcode-legitimate-interest-assessment / No]

---

## Overall Classification and Recommendation

**Classification**: APPROVED / CONDITIONAL / REJECTED

**Recommendation**: [Full recommendation covering:
- Primary basis and why it is the strongest available
- Why alternative bases are inadequate (specifically)
- If CONDITIONAL: exact remediations required, owner, deadline
- If REJECTED: what would need to change for processing to be lawful
- Next steps: ROPA update, privacy notice, DPA update, DPIA, consent refresh]

---

## Glass Box Audit Trail

[YAML block per Glass Box Audit Trail section above]
```

---

## Localization Notes

To apply this skill to a specific member state or UK/Swiss context:

1. Research the competent supervisory authority's published guidance on lawful basis —
   most EU SAs have issued sector-specific guidance supplementing the EDPB guidelines
2. Identify national derogations enacted under Art. 23 GDPR that restrict specific bases
   in your sector (employment, health, financial services, telecommunications, journalism)
3. For UK: Verify DPA 2018 Schedule 1 current list of substantial public interest
   conditions and any updates from the Data (Use and Access) Act 2025
4. For Art. 8 age threshold: confirm the member state's chosen threshold (if lower than 16)
5. Replace [JURISDICTION-SPECIFIC] markers with verified local legal content
6. Add jurisdiction-specific enforcement examples to the anti-patterns section

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis for the Legalcode skill library.
Informed by:
- GDPR Regulation (EU) 2016/679, Articles 6–10
- EDPB Guidelines 05/2020 on consent
- EDPB Guidelines 2/2019 on processing under Art. 6(1)(b)
- EDPB Guidelines 1/2024 on legitimate interests under Art. 6(1)(f)
- ICO Guide to Lawful Basis (ico.org.uk)
- UK DPA 2018 and Data (Use and Access) Act 2025
- Meta €390M (Irish DPC, January 2023), LinkedIn €310M (Irish DPC, October 2024),
  Meta €479M (AEPD Spain, 2025), CJEU C-621/22 (KNLTB, 2024)
- Repository structural patterns from `legalcode-legitimate-interest-assessment` and
  `legalcode-contract-review` (gold standard reference)
