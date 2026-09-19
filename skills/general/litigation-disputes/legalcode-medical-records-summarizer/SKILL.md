---
name: legalcode-medical-records-summarizer
description: 'Summarize and analyze medical records chronologically for US personal injury (PI) litigation.
  Use when building a medical chronology, analyzing causation, assessing pre-existing conditions, identifying
  treatment gaps, reviewing diagnostic results, or preparing a damages timeline for a PI case. Covers
  all PI record categories: EMS/ED records, treating physician notes, operative reports, imaging, physical
  therapy, pharmacy records, prior workers'' compensation files, IME/DME reports, and billing. Produces
  a structured medical chronology with ICD-10 classification, treatment intensity mapping, gap analysis,
  eggshell/aggravation analysis, causation narrative, and Daubert readiness assessment. Applicable to
  plaintiff and defense counsel, insurance adjusters, and medical-legal consultants. Jurisdiction-agnostic
  within the US; jurisdiction markers for Daubert vs. Frye states.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Medical Records Summarizer

> **Disclaimer**: This skill provides a framework for AI-assisted medical records review
> and summarization in personal injury litigation. It does not constitute legal advice,
> medical advice, or a substitute for qualified medical experts, forensic nurses, or
> licensed legal professionals. All outputs must be reviewed by qualified legal counsel
> and, where applicable, by retained medical experts before use in litigation, settlement
> negotiations, or expert briefings. Medical causation is a contested factual question
> requiring expert testimony — this skill organizes the record; it does not establish
> causation. Laws and evidentiary standards vary by state; verify current applicability
> before relying on any procedure or principle described here. References to ICD-10
> codes, Daubert/Frye standards, and causation doctrine cited from training data carry
> hallucination risk — verify against authoritative sources before relying on them.

---

## Purpose and Scope

This skill organizes, analyzes, and summarizes medical records for US personal injury
litigation. It produces a structured chronology, causation narrative, and damages
timeline suitable for settlement demands, expert briefings, and trial preparation.

**Covers:**

- Chronological organization of all medical records across multiple providers
- ICD-10 diagnosis code classification (traumatic vs. degenerative; injury vs. sequela)
- Treatment intensity mapping (conservative / moderate / aggressive phases)
- Diagnostic testing summary (imaging, electrodiagnostics, labs, functional assessments)
- Treatment gap identification and legal risk classification
- Pre-existing condition analysis (eggshell plaintiff / aggravation / crumbling skull)
- Causation chain documentation and Daubert readiness assessment
- Damages timeline support (past medicals, future care, lost wages, non-economic losses)
- Quality verification with provider credibility assessment
- Expert support recommendations

**Does not:**

- Provide medical diagnoses or clinical opinions
- Replace qualified medical experts or life care planners
- Guarantee admissibility of any causation theory under Daubert or Frye
- Apply outside the US (different medical record systems and evidentiary standards apply)
- Cover workers' compensation benefit calculations (separate framework required)
- Handle criminal restitution medical evidence (different procedural rules)

**Related skills:**

- `legalcode-damages-calculation` — Quantifying economic and non-economic damages
- `legalcode-early-case-assessment` — Overall PI exposure modeling and strategy
- `legalcode-deposition-preparation` — Deposing treating physicians and IME examiners
- `legalcode-expert-witness-preparation` — Preparing medical experts for deposition/trial
- `legalcode-demand-letter-drafter` — Incorporating the chronology into a settlement demand

---

## Jurisdiction and Governing Law

This skill is US-jurisdiction-focused. Medical causation standards, expert admissibility
rules, and damages frameworks vary significantly by state.

**[JURISDICTION-SPECIFIC]** Localize at minimum:

| Issue                      | Federal / Daubert States            | Frye States                                                         | Notes                                             |
| -------------------------- | ----------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------- |
| Expert admissibility       | Daubert/FRE 702 (5-factor)          | Frye (general acceptance)                                           | ~27 states Daubert; ~8 Frye; CA uses Kelly-Frye   |
| Causation standard         | "More likely than not" (>50%)       | Same — varies in articulation                                       | Plaintiff's burden in all states                  |
| Eggshell plaintiff rule    | Available in all states             | Same                                                                | Defendant takes plaintiff as found                |
| Crumbling skull doctrine   | Available in most states            | Same                                                                | Defense: accelerated inevitable decline           |
| Pre-existing aggravation   | Plaintiff burden in most states     | Burden shifts to defense in some (e.g., Maine _Lovely v. Allstate_) | Verify by jurisdiction                            |
| Treatment gap significance | No fixed rule; jury question        | Same                                                                | 30+ day threshold standard in practice            |
| MMI definition             | Workers' comp concept; varies in PI | Same                                                                | Medical stabilization = trigger for final damages |
| Future care admissibility  | Life care plan preferred            | Same                                                                | Lay opinion insufficient for large future awards  |

**[JURISDICTION-SPECIFIC]** For Frye-state cases (New York, Illinois, Pennsylvania,
Washington, New Jersey, and others), expert methodology must be "generally accepted"
in the relevant scientific community. The key difference in PI cases: Frye is typically
more permissive for standard-of-care causation opinions than Daubert's multi-factor test,
but Daubert applies in all federal courts regardless of forum state.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would change the direction or depth of analysis
- Multiple valid approaches exist (plaintiff vs. defense framing)
- Ambiguity in the records creates a fork that only the user can resolve
- Risk posture or litigation strategy must inform how findings are presented

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

### Step 1: Accept Medical Records and Frame the Matter

Accept the medical records in any format:

- **PDF/DOCX files**: Scanned or digital medical records
- **Record packet**: Pre-organized binders, hyperlinked indices, litigation support databases
- **Pasted text**: Excerpts or summaries copied into the conversation
- **File index**: A list of records for which the user will provide excerpts selectively

If no records are provided, prompt the user to supply them. If only a partial record set
is available, proceed but flag gaps in the records inventory.

**Create a records manifest** at intake:

```
Records Manifest
----------------
[Provider Name] — Record Type — Date Range — Pages — Format — Quality
[...]
Total documents: [N]
Date range: [Earliest] to [Latest]
Identified gaps: [Provider / service type / date range not produced]
```

### Step 2: Gather Analysis Context

**⟁ CLARIFY** — Before beginning analysis, ask the user these questions. Present as
structured options where possible:

**Question 1: Analysis Objective**

- Options: **Trial preparation**, **Settlement demand / demand letter support**,
  **Expert briefing / expert report organization**, **Pre-suit causation analysis**,
  **IME rebuttal / defense medical examination response**, **Insurance adjusting /
  coverage evaluation**, **Early case assessment / intake screening**
- _Why this matters_: Trial prep requires full chronology + Daubert readiness assessment;
  demand letter support needs narrative arc + damages timeline; early intake screening
  needs red flag identification only.

**Question 2: User Role and Side**

- Options: **Plaintiff counsel**, **Defense counsel**, **Medical-legal consultant (neutral)**,
  **Insurance adjuster / defense representative**, **Paralegal / case manager**,
  **Expert economist (damages input)**
- _Why this matters_: Plaintiff counsel wants to maximize and explain the medical record;
  defense counsel wants to identify gaps, inconsistencies, and pre-existing conditions.
  The skill adapts emphasis accordingly but always reports both perspectives.

**Question 3: Injury Type and Complexity**

- Options: **Traumatic orthopedic** (fracture, dislocation, ligament tear),
  **Soft tissue** (cervical/lumbar strain, sprain), **Spinal** (disc herniation, cord
  injury, radiculopathy), **Neurological** (TBI, nerve injury, CRPS),
  **Multi-system trauma** (multiple injury areas), **Occupational / repetitive stress**,
  **Other / mixed**
- _Why this matters_: Different injury types have different causation frameworks,
  ICD-10 coding patterns, and Daubert challenges. Soft tissue cases face different
  scrutiny than surgical cases.

**Question 4: Pre-Existing Condition Complexity**

- Options: **No prior treatment for these body regions documented**,
  **Stable pre-existing history** (prior treatment but asymptomatic at incident),
  **Progressive pre-existing condition** (actively deteriorating),
  **Same body region previously injured** (same mechanism or similar diagnosis),
  **Significant comorbidities** (obesity, diabetes, prior surgeries),
  **Unknown / records not yet obtained**
- _Why this matters_: Pre-existing conditions are the primary defense weapon. The
  eggshell plaintiff rule applies when the condition was asymptomatic; aggravation
  doctrine applies when symptomatic. The analysis strategy differs materially.

**Question 5: Data Readiness**

- Options: **Complete records** (organized, all providers, full date range),
  **Fragmented** (multiple providers, records arriving in batches),
  **Sparse** (limited records, early in case),
  **Contradictory** (conflicting diagnoses or provider notes),
  **Incomplete production suspected** (gaps in billing vs. clinical notes)
- _Why this matters_: Drives confidence scoring and identifies what additional record
  requests must be made before the chronology is reliable.

If the user provides partial context, proceed with what you have and state assumptions
explicitly (e.g., "I'm assuming this is plaintiff-side analysis — advise if you need
defense framing and I'll re-run the emphasis").

### Step 3: Build the Medical Chronology

Read the full record set before flagging individual findings — records interact across
providers, and a finding at one provider often contradicts or contextualizes a finding
at another.

**3a. Extract all treatment encounters** in date order:

- Date of encounter
- Provider name, specialty, and practice type
- Type of encounter (office visit, ER, surgery, PT session, imaging, etc.)
- Chief complaint and mechanism of injury as reported in the record
- Examination findings (objective: ROM measurements, neurological findings, palpation)
- Diagnosis or assessment (with ICD-10 code if coded)
- Treatment plan or intervention
- Follow-up instructions or referrals made

**3b. Organize into treatment phases**:

| Phase                 | Typical Timeframe                 | Characteristics                                                                               |
| --------------------- | --------------------------------- | --------------------------------------------------------------------------------------------- |
| **Acute**             | Incident through first 6–8 weeks  | Emergency/urgent care, initial specialist eval, baseline imaging, acute-phase treatment       |
| **Subacute**          | 6 weeks to 6 months post-incident | PT/OT, specialist follow-up, diagnostic testing, medication management, functional assessment |
| **Chronic / Ongoing** | 6+ months post-incident           | Ongoing management, surgical consideration, IME, MMI assessment, life care planning           |
| **Post-MMI**          | After maximum medical improvement | Maintenance care, permanent restrictions, future care needs                                   |

**3c. Flag structural gaps** in the chronology (dates without documented treatment in
the record set) for later analysis in Step 7.

**Output**: `Medical Chronology Table` — see Output Format Template, Part A.

### Step 4: Extract and Classify Diagnoses

For each unique diagnosis appearing in the records:

**4a. Extract the ICD-10 code** and verify its clinical description:

| Code Series                          | Injury Type                               | Key Distinctions                                                                                                                            |
| ------------------------------------ | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| S00–S99 (with 7th character "A/D/S") | Acute traumatic injuries                  | **A** = initial encounter (active treatment); **D** = subsequent encounter (routine follow-up); **S** = sequela (late effect of old injury) |
| M00–M99                              | Musculoskeletal / degenerative conditions | Indicates pre-existing or degenerative pathology — defense-favorable                                                                        |
| V00–Y99 (External cause codes)       | Mechanism / cause of injury               | Documents that the injury is causally linked to the incident — absence is a causation red flag                                              |
| G00–G99                              | Neurological conditions                   | Neuropathy, radiculopathy, myelopathy — may follow traumatic injury or be pre-existing                                                      |
| F00–F99                              | Mental/behavioral health                  | PTSD, anxiety, depression — may be post-traumatic; often challenged                                                                         |

**4b. Classify each diagnosis**:

- **PRIMARY**: Direct anatomical injury from the incident (e.g., L4-5 disc herniation
  coded S33.0XXA from MVA)
- **SECONDARY**: A condition developing as a consequence of the primary injury
  (e.g., lumbar radiculopathy G54.1 following disc herniation)
- **COMORBID / PRE-EXISTING**: Condition present before the incident; relevance depends
  on eggshell/aggravation analysis

**4c. Flag ICD-10 red flags** (see Anti-patterns section for full list):

- Provider using M-codes (degenerative) instead of S-codes (traumatic) for injuries
  claimed as incident-caused
- Missing or incorrect 7th character — especially "S" (sequela) where "A" (initial
  encounter) is expected
- Absence of external cause codes (V/W/X/Y) for injury-related records
- Inconsistent coding of the same diagnosis across providers

**Output**: `Diagnosis Inventory` — see Output Format Template, Part B.

### Step 5: Map Treatment Progression and Intensity

For each treatment phase identified in Step 3, classify treatment intensity and document
clinical rationale:

**Treatment Intensity Classification:**

| Level            | Examples                                                                                                          | PI Significance                                                          |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **CONSERVATIVE** | OTC medication, rest, ice/heat, self-care, observation                                                            | Minimal injury signal; defense argues no objective need for treatment    |
| **MODERATE**     | Physician visits, PT/OT/chiropractic, oral Rx, injections (ESI, trigger points), imaging                          | Documented injury needing professional care; standard for soft tissue PI |
| **AGGRESSIVE**   | Surgery, hospitalization, specialist referral, EMG/nerve testing, pain management program, spinal cord stimulator | Strong severity signal; most defense-resistant treatment category        |

**5a. Document escalation triggers**: When treatment advances from conservative to
moderate, or moderate to aggressive, identify the clinical finding or lack of response
that drove the decision. Unsupported escalation is a credibility risk; well-documented
escalation is a causation anchor.

**5b. Track medication progression** as a severity proxy:

- OTC NSAIDs / analgesics → minimal injury
- Prescription NSAIDs, muscle relaxants → moderate acute injury
- Opioids / gabapentinoids → significant pain or nerve involvement
- Opioid escalation or long-term maintenance → high severity signal
- **Inconsistency flag**: If the plaintiff claims severe disabling pain but the
  medication record shows only OTC or no medications, note this as a potential
  credibility issue for cross-examination.

**5c. Document treatment response** at each phase:

- **RESPONDING**: Objective improvement in ROM, pain scores, functional capacity
- **PLATEAU**: Stable condition without significant further improvement (MMI approaching)
- **WORSENING**: Deterioration despite treatment (supports higher damages)
- **INCONSISTENT**: Reported improvements in records contradict functional claims

**Output**: `Treatment Timeline` — see Output Format Template, Part C.

### Step 6: Examine Diagnostic Testing and Objective Evidence

For each diagnostic test in the records (imaging, electrodiagnostics, functional
assessments, lab work):

**6a. Extract key findings**:

- Date ordered and date performed
- Modality (X-ray, CT, MRI, EMG/NCS, bone scan, ultrasound, FCE, etc.)
- Ordering provider and interpreting radiologist / specialist
- Key findings in the report impression section (not just the ordering physician's summary)
- Severity designation used in the report ("mild," "moderate," "severe," "acute," etc.)
- High-value objective findings that support acute trauma:
  - **Bone marrow edema** (MRI): Strong indicator of acute bone injury
  - **High Intensity Zone / HIZ** (MRI): Annular fissure — acute disc trauma
  - **Acute hematoma** (any modality): Post-traumatic hemorrhage
  - **Avulsion fracture**: Acute tendon/ligament avulsion from bone
  - **Ligamentous laxity / instability**: Acute ligamentous disruption
  - **EMG denervation potentials**: Nerve injury (acute or subacute)

**6b. Compare baseline to follow-up imaging** where available:

- If pre-incident imaging exists: document what was abnormal before the incident vs.
  what is new or worsened post-incident. This is the strongest defense against the
  "pre-existing condition" challenge.
- If only post-incident imaging: note the absence of a baseline comparison and flag
  the need for aging analysis testimony (to establish imaging findings are not age-related
  degeneration).

**6c. Assess radiologist report vs. treating physician characterization**:

- If the radiologist's impression describes "moderate disc herniation" but the treating
  physician documents "severe disc herniation," note the discrepancy.
- The radiologist's contemporaneous report controls for evidentiary purposes.

**⟁ CLARIFY** — If imaging shows significant degenerative changes alongside acute injury
findings, ask:

- "The [imaging report] shows both [acute finding] and [degenerative finding] at the same
  level. How do you want me to present the pre-existing component — as part of the
  eggshell analysis, or do you have prior imaging for comparison?"

**Output**: `Diagnostic Testing Summary` — see Output Format Template, Part D.

### Step 7: Assess Treatment Gaps and Compliance

**7a. Identify all treatment gaps** (periods of 30+ days without documented medical care
for the claimed injuries):

For each gap:

- Identify the gap period (start and end dates, duration)
- Note what treatment was ongoing (or not) before and after the gap
- Identify whether the reason for the gap is documented in the records
- Classify the gap using the framework below:

| Classification    | Description                                                                                                                                                                               | Legal Signal                                                                                         |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **EXPECTED GAP**  | Post-surgical healing period; medical advice to return only if needed; documented recovery phase                                                                                          | Neutral to plaintiff-favorable; part of normal recovery trajectory                                   |
| **EXPLAINED GAP** | Financial barrier, insurance denial, transportation, scheduling delay — documented in the records                                                                                         | Potentially neutralized if well-documented; must appear in medical records not just client statement |
| **CONCERN GAP**   | Extended treatment cessation without clear explanation; inconsistent with claimed severity                                                                                                | Weakens damages narrative; defense will argue condition resolved                                     |
| **RED FLAG GAP**  | Gap followed by a new first-time complaint; gap coincides with period of high physical activity (social media / surveillance evidence); gap longer than 90 days without documented reason | Causation break risk; defense will argue new injury or non-injury period                             |

**7b. Assess compliance with treatment recommendations**:

| Compliance Issue             | Examples                                | Defense Argument                                      |
| ---------------------------- | --------------------------------------- | ----------------------------------------------------- |
| Missed appointments          | Multiple no-shows or late cancellations | Plaintiff not actually suffering; failure to mitigate |
| Unmet referrals              | Surgeon referred; plaintiff never went  | Damages from unmet referral are speculative           |
| Medication non-adherence     | Prescription filled but not refilled    | Pain not as severe as claimed                         |
| Home exercise non-compliance | PT notes "non-compliant with HEP"       | Contribution to non-recovery                          |

**⟁ CLARIFY** — For gaps > 60 days, ask:

- "There is a [N]-day gap between [Date A] and [Date B]. Do you have a client explanation
  or supplemental documentation for this period? This gap will be highlighted by defense
  counsel and should be addressed proactively."

**Output**: `Gaps and Compliance Analysis` — see Output Format Template, Part E.

### Step 8: Analyze Pre-Existing Conditions and Causation

This is the highest-stakes analytical step. Pre-existing conditions are the primary
defense weapon in PI litigation.

**8a. Establish the pre-incident baseline** for each body region at issue:

- Review all records pre-dating the incident for the relevant body regions
- Document the last known status of each region: asymptomatic, symptomatic, treated,
  stabilized, deteriorating
- Note any prior PI suits, workers' compensation claims, or disability applications
  for the same body regions (search records for references; flag for discovery follow-up)

**8b. Classify each pre-existing condition** using the three-doctrine framework:

| Doctrine               | Applies When                                                                                     | Analysis Required                                                                                            | Recovery                                                               |
| ---------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| **Eggshell Plaintiff** | Pre-existing condition was asymptomatic before incident; incident activated or worsened it       | Document last pre-incident records showing no complaints; document first post-incident complaints            | Full recovery — defendant takes plaintiff as found                     |
| **Aggravation**        | Pre-existing condition was symptomatic; incident materially worsened it                          | Quantify the pre-incident vs. post-incident delta (visits, medications, functional limits, severity ratings) | Recovery for the aggravation only — the delta, not the whole condition |
| **Crumbling Skull**    | Pre-existing condition was already deteriorating; incident merely accelerated inevitable decline | Defense must prove deterioration was inevitable and quantify the acceleration                                | Limited recovery — acceleration only, not the full deterioration       |

**8c. Apply the aggravation delta analysis** for each pre-existing condition:

```
Pre-Incident Baseline:
  Treatment frequency: [visits/month]
  Medications: [list]
  Work restrictions: [none / specific restrictions]
  Pain level documented: [0-10 scale from records]
  Functional capacity: [documented limitations, if any]

Post-Incident Status:
  Treatment frequency: [visits/month — increase over baseline]
  Medications: [list — additions over baseline]
  Work restrictions: [new or increased restrictions]
  Pain level documented: [0-10 scale — increase over baseline]
  Functional capacity: [new documented limitations beyond baseline]

Aggravation Assessment:
  Classification: DISTINCT / AGGRAVATED / CONFOUNDING / PROBLEMATIC
  Delta magnitude: [Quantified increase in treatment, medications, limitations]
  Causation confidence: [Level — see Confidence Scoring section]
```

**8d. Identify ICD-10 code consistency issues** between pre- and post-incident records:

- If pre-incident records for the same body region use M-codes (degenerative) and
  post-incident records use both M-codes and S-codes, the S-code pathology is the
  causation anchor
- If providers are using M-codes post-incident for what the plaintiff claims is a new
  traumatic injury, a treating physician narrative report (or retained expert opinion)
  is needed to reconcile

**Output**: `Pre-Existing Conditions Analysis` — see Output Format Template, Part F.

### Step 9: Build the Causation Narrative

Synthesize the chronology, diagnoses, treatment, and pre-existing analysis into a
four-element causation chain:

**Element 1 — Incident Mechanism**: Does the described mechanism support the alleged
injuries? Is the mechanism description consistent across all medical records and the
incident report / police report / plaintiff statements?

**Element 2 — Injury Symptomatology**: Are the onset and nature of symptoms consistent
with the described mechanism? Temporal proximity (symptoms within 24–72 hours) is the
gold standard. Delayed onset requires explanation (adrenaline, delayed inflammation).

**Element 3 — Objective Evidence**: Do imaging, examination findings, and diagnostic
tests confirm structural injury consistent with the claimed mechanism? This is the
strongest causation pillar.

**Element 4 — Alternative Explanations**: Have plausible alternative explanations been
identified and addressed? Pre-existing degeneration, concurrent conditions, non-incident
activities, age-related changes — each must be considered.

**9a. Assign a causation confidence rating** for each primary injury claim (see
Confidence Scoring section).

**9b. Assess Daubert readiness** for each causation opinion:

| Requirement                                        | Assessment                | Flag                                            |
| -------------------------------------------------- | ------------------------- | ----------------------------------------------- |
| Treating physician causation opinion in the record | Present / Absent          | RED if absent for primary injuries              |
| Expert methodology testable and peer-reviewed      | Yes / Needs confirmation  | FLAG if only clinical experience, no literature |
| Temporal proximity documented                      | Strong / Adequate / Weak  | FLAG if >72 hours to initial care               |
| Objective evidence supporting causation            | Strong / Moderate / Weak  | RED if purely subjective                        |
| Alternative causes addressed                       | Addressed / Not addressed | FLAG if significant alternatives unexplored     |
| Plaintiff-consistent presentation across providers | Consistent / Inconsistent | RED if significant inconsistency                |

**⟁ CLARIFY** — If causation is disputed and there is no treating physician causation
opinion in the records, ask:

- "No treating physician has documented a causation opinion linking the injury to the
  incident. Do you want me to flag this for supplemental narrative report from the
  treating physician, or is a retained expert already being used for causation?"

**Output**: `Causation Narrative` — see Output Format Template, Part G.

### Step 10: Quality Verification and Deliverables

Before delivering the analysis, run all quality checks defined in the Quality Assurance
Framework section.

1. Run the 5 Medical Records Citation Quality Gates silently. Revise failures before
   delivery.
2. For any CATASTROPHIC-classified injuries or disputed causation elements, run the
   3-pass Self-Interrogation.
3. Assign Confidence Scores to each major causation claim.
4. Complete the Glass Box audit trail YAML.
5. Generate expert support recommendations.

**⟁ CLARIFY** — Confirm output format before delivery:

- "Do you want: (a) Full chronology package (all Parts A–K), (b) Executive Summary +
  Causation Brief only, (c) Damages Timeline only, or (d) Custom — specify which parts?"

Deliver the output using the template in the Output Format Template section.

---

## Deep Topic Analysis

### 10 Essential Medical Record Categories

For complete PI record coverage, obtain and analyze all applicable categories:

| #   | Category                                    | Key Content                                                                                                                                                  | Collection Priority                                                           |
| --- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| 1   | **EMS / Emergency Department**              | First-reported symptoms, mechanism, baseline severity before attorney involvement; contains the most legally pristine observations                           | **CRITICAL** — obtain first; pre-dates litigation posture                     |
| 2   | **Treating Physician Office Notes**         | All primary care and specialist office visit notes (orthopedics, neurology, physiatry, neurosurgery, pain management) — full notes, not just assessment/plan | **CRITICAL** — longitudinal narrative                                         |
| 3   | **Operative Reports**                       | Intraoperative observations under direct visualization; strongest objective causation evidence when surgery occurred                                         | **CRITICAL** if surgery performed                                             |
| 4   | **Diagnostic Imaging Reports**              | Actual radiology reports (not ordering physician's summary); baseline vs. post-incident comparison where available                                           | **CRITICAL** — objective anatomical evidence                                  |
| 5   | **PT / OT / Chiropractic Records**          | Functional progress, ROM measurements, pain scores over time, MMI notation, HEP compliance                                                                   | **HIGH** — documents functional limitation and treatment duration             |
| 6   | **Pharmacy Records**                        | Full medication history; reveals undisclosed prior conditions; opioid history; medication progression as severity proxy                                      | **HIGH** — primary defense research tool for pre-existing conditions          |
| 7   | **Health Insurance Claim Histories / EOBs** | Searchable index of all prior treatment; "Detailed Claims Listing" reveals undisclosed prior treatment for same body regions                                 | **HIGH** — often overlooked; contains pre-existing condition evidence         |
| 8   | **IME / DME Reports**                       | Defense medical examination reports; require critical analysis for examiner bias, financial relationship, examination duration vs. report detail             | **MEDIUM-HIGH** — critical to rebut; examiner's credibility is primary target |
| 9   | **Prior WC / SSDI / Military Records**      | Prior injury documentation, disability ratings, prior physician statements for same body parts                                                               | **HIGH if prior claims exist** — binding prior characterizations              |
| 10  | **Billing Records**                         | Itemized bills cross-referenced to clinical notes; identifies undocumented treatment; establishes economic damages                                           | **HIGH** — cross-reference to clinical notes                                  |

### ICD-10 Analysis Methodology for PI Cases

**The 7th Character — Most Legally Significant ICD-10 Element:**

The 7th character on injury codes (S00–T88) is the single most important coding element
for PI causation arguments:

| 7th Character                | Meaning                                           | PI Significance                                                                                                                                       |
| ---------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A** — Initial encounter    | Patient receiving active treatment for the injury | **Plaintiff-favorable**: establishes ongoing acute injury requiring active treatment                                                                  |
| **D** — Subsequent encounter | Routine care after active treatment               | Neutral to defense-favorable: defense argues treatment is in maintenance phase                                                                        |
| **S** — Sequela              | Late effect or complication of old injury         | **Defense-favorable**: provider has characterized condition as a long-term consequence, not a fresh acute injury — devastating to causation narrative |

**ICD-10 Causation Battleground — Traumatic vs. Degenerative Coding:**

| Scenario                              | ICD-10 Pattern                                                  | Causation Implication                                   |
| ------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------- |
| Traumatic disc herniation             | S33.0XXA (traumatic rupture, initial encounter)                 | Strong plaintiff causation anchor                       |
| Degenerative disc disease             | M51.16 (degeneration of disc, lumbar)                           | Defense: pre-existing degeneration, not incident-caused |
| Cervical radiculopathy — acute        | S14.3XXA (injury of brachial plexus, initial encounter)         | Traumatic nerve injury — plaintiff-favorable            |
| Cervical radiculopathy — degenerative | M54.12 (radiculopathy, cervical)                                | Defense: age-related, not incident-caused               |
| External cause coding present         | V43.52XA (car occupant injured in collision, initial encounter) | Links injury to incident — critical for causation       |
| External cause coding absent          | —                                                               | Defense: provider did not link condition to incident    |

**ICD-10 Review Protocol:**

1. Cross-check all injury codes against the claimed incident mechanism — do the codes
   describe the type of trauma that would result from the incident?
2. Verify external cause codes (V/W/X/Y) are present on all injury-related records
3. Track 7th character consistency — premature switch to "D" or "S" codes undermines
   ongoing severity
4. Flag M-code dominance where S-codes are expected for acute traumatic injury
5. Identify coding inconsistencies across providers and plan reconciliation strategy
6. Assess code specificity — vague codes reduce causation narrative strength

### Gap Analysis Framework

**Legal significance threshold**: 30+ days between medical visits for claimed injuries.
Research indicates ~17% of PI cases contain at least one such gap.

**The Four Defense Gap Arguments:**

1. **Not Serious**: Consistent care is required to support severity claims
2. **Causation Break**: Gap allows defense to argue subsequent treatment is for unrelated condition
3. **Failure to Mitigate**: Plaintiff has duty to seek reasonable treatment
4. **Credibility**: Inconsistent care patterns suggest exaggeration

**Pre-Treatment Gap** (delay from incident to first medical contact): The most
legally damaging gap type. Every 24 hours of delay post-incident without documented
cause weakens causation. Standard defense benchmark: no care within 72 hours = vulnerable.

**Neutralizing Gaps — Required Documentation:**
Each gap explanation must appear in the **medical records themselves**, not merely in
a client statement that can be challenged at deposition. Recognized explanations:

- Financial barriers / lack of insurance (document with records, not just assertion)
- Transportation limitations
- Provider scheduling delays (obtain confirmation from provider records)
- Medical advice to return only "if needed" (confirm in treating physician notes)
- Post-surgical healing period (document activity restrictions in operative notes)
- Geographic access limitations

### Medical Terminology Reference for Attorneys

**Degenerative Terms (Defense-Favorable — Signals Pre-Existing):**

| Term                        | Meaning                                                   | Defense Use                                  |
| --------------------------- | --------------------------------------------------------- | -------------------------------------------- |
| Osteophytes / bone spurs    | Bony overgrowths from chronic degeneration                | "These took years to develop — pre-existing" |
| Spondylosis                 | Degenerative spinal changes                               | "Age-related, not incident-caused"           |
| Spondylolisthesis           | Vertebral slippage (congenital, isthmic, or degenerative) | Depends on type; isthmic = often congenital  |
| Chondromalacia              | Cartilage softening and breakdown                         | "Pre-existing wear and tear"                 |
| "Degenerative disc disease" | Misnomer for normal aging of discs                        | "Normal aging process; everyone has this"    |

**Acute Traumatic Terms (Plaintiff-Favorable — Signals New Injury):**

| Term                             | Meaning                                       | Plaintiff Use                                      |
| -------------------------------- | --------------------------------------------- | -------------------------------------------------- |
| Bone marrow edema                | Acute bone injury signal on MRI               | "This only appears immediately after trauma"       |
| High Intensity Zone (HIZ)        | Annular fissure — acute disc trauma on MRI    | "Indicates acute disc injury at this level"        |
| Avulsion fracture                | Bone fragment pulled away by ligament/tendon  | "Classic acute traumatic event"                    |
| Edema / hematoma                 | Acute tissue inflammation or blood collection | "Present only in acute post-traumatic state"       |
| Ligamentous laxity / instability | Suggests acute ligamentous disruption         | "Indicates fresh injury to stabilizing structures" |
| EMG denervation potentials       | Nerve injury (acute or subacute)              | "Consistent with acute or subacute nerve injury"   |

**Key Functional and Impairment Terms:**

| Term                                  | Meaning                                                        | PI Significance                                                               |
| ------------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| MMI (Maximum Medical Improvement)     | Condition stabilized; no further significant recovery expected | Trigger for final damages assessment; never settle before MMI is reached      |
| FCE (Functional Capacity Evaluation)  | Objective physical work capacity assessment                    | Strongest objective evidence of functional limitation / permanent restriction |
| AMA Impairment Rating                 | % whole-person impairment (AMA Guides 6th Ed.)                 | Informs permanent impairment damages                                          |
| Radiculopathy                         | Nerve root dysfunction (dermatomal pain / weakness)            | Common post-disc injury; objective EMG confirmation preferred                 |
| Myelopathy                            | Spinal cord dysfunction                                        | More severe; permanent injury risk higher; larger damages                     |
| CRPS (Complex Regional Pain Syndrome) | Chronic post-traumatic pain syndrome                           | High damages; aggressively contested by defense                               |

---

## Injury Severity and Status Classification

### Injury Severity Tiers

Classify the overall injury severity at the outset to frame the entire analysis:

| Tier             | Classification                                                                    | Indicators                                                                                                      | PI Damages Signal                                                                                |
| ---------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **CATASTROPHIC** | Permanent disability, major functional loss, lifelong care                        | Death, paralysis, severe TBI, amputation, CRPS requiring spinal cord stimulator, permanent cognitive impairment | Maximum non-economic damages; future care required; pain multiplier 4–5x+                        |
| **SERIOUS**      | Significant injury, substantial treatment, temporary to semi-permanent impairment | Multiple surgeries, prolonged hospitalization, 6+ months recovery, significant functional limitation            | Multiplier 3–4x; strong economic damages; expert life care plan advisable                        |
| **MODERATE**     | Treatable injury requiring professional care, temporary functional impact         | Single surgery OR 3+ months professional treatment, documented return to work with restrictions                 | Multiplier 2–3x; objective evidence critical; treatment gaps most damaging                       |
| **MINOR**        | Mild injury, self-limited recovery, brief treatment                               | Soft-tissue injury, <8 weeks treatment, return to full function                                                 | Multiplier 1.5–2x; most vulnerable to pre-existing condition defense; must prove injury occurred |

### Diagnosis Severity Grading (Per-Diagnosis)

| Grade       | Label        | Characteristics                                                                   |
| ----------- | ------------ | --------------------------------------------------------------------------------- |
| **GRADE 4** | CATASTROPHIC | Permanent impairment, ongoing care required, major life impact                    |
| **GRADE 3** | SEVERE       | Major functional impairment, intensive treatment required, uncertain recovery     |
| **GRADE 2** | MODERATE     | Significant functional impact, professional treatment required, recovery expected |
| **GRADE 1** | MILD         | Minimal functional impact, conservative treatment, expected full recovery         |

### Treatment Response Status

| Status           | Description                               | Damages Implication                                                  |
| ---------------- | ----------------------------------------- | -------------------------------------------------------------------- |
| **RESPONDING**   | Objective improvement, functional gains   | Supports recovery narrative; damages may reduce over time            |
| **PLATEAU**      | Stable but not improving; MMI approaching | Supports ongoing damages and future care needs                       |
| **WORSENING**    | Deterioration despite treatment           | Strongest damages support; largest future care exposure              |
| **INCONSISTENT** | Atypical treatment response               | Requires expert explanation; vulnerability to malingering allegation |

### Pre-Existing Condition Impact

| Classification      | Doctrine                                               | Recovery                                                              |
| ------------------- | ------------------------------------------------------ | --------------------------------------------------------------------- |
| **DISTINCT**        | No relevant pre-existing condition                     | Full recovery for all incident-caused losses                          |
| **EGGSHELL**        | Pre-existing asymptomatic vulnerability activated      | Full recovery — defendant takes plaintiff as found                    |
| **AGGRAVATED**      | Pre-existing symptomatic condition materially worsened | Recovery limited to the aggravation delta                             |
| **CONFOUNDING**     | Pre-existing complicates but does not bar causation    | Partial recovery; apportionment evidence needed                       |
| **CRUMBLING SKULL** | Pre-existing inevitable deterioration accelerated      | Recovery limited to acceleration; defense bears burden in some states |

---

## Actionable Output Per Finding

For each material finding in the medical record analysis, produce:

**For CATASTROPHIC / SERIOUS findings:**

- Full clinical summary with ICD-10 codes and severity grading
- Causation chain documentation (all four elements)
- Defense challenge prediction and rebuttal strategy
- Expert support requirements (type of expert, key opinions needed, Daubert roadmap)
- Damages contribution estimate

**For MODERATE findings:**

- Clinical summary with ICD-10 code and severity grade
- Causation confidence rating with supporting evidence
- Key vulnerabilities and recommended documentation fixes
- Expert support recommendation (if needed)

**For MINOR / COMORBID findings:**

- Flag for awareness
- Note whether it creates a pre-existing condition risk
- Recommend proactive treatment in demand letter / direct examination

**For RED FLAG findings** (gaps, inconsistencies, pre-existing conditions, adverse coding):

- Identify the specific record and page reference
- Explain the defense argument it supports
- Provide plaintiff-side rebuttal options
- Recommend corrective action (supplemental physician narrative, additional discovery,
  expert opinion)

---

## Prioritization Framework

Prioritize findings for counsel attention in three tiers:

| Tier       | Priority                              | Criteria                                                                                                                                                              | Action Required                                                                        |
| ---------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **TIER 1** | Must address before demand / trial    | Causation-dispositive issues; RED FLAG gaps; undisclosed pre-existing conditions; missing treating physician causation opinion; Daubert-vulnerable expert methodology | Immediate — obtain supplemental records, narrative reports, or retained expert opinion |
| **TIER 2** | Should address for maximum case value | Diagnosis severity optimization; imaging report vs. physician characterization reconciliation; treatment escalation documentation; compliance issues                  | Near-term — resolve before demand letter or case development cutoff                    |
| **TIER 3** | Enhances case quality                 | ICD-10 code optimization; provider credibility documentation; comprehensive damages timeline; life care plan baseline                                                 | Background — address as resources allow                                                |

---

## Quality Assurance Framework

### Medical Records Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate                   | Rule                                                                                                                        | Fail Action                                                                 |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Clinical Support**   | Every diagnosis cited is supported by documented clinical findings, not diagnosis codes alone                               | Add specific clinical reference or flag "[DIAGNOSIS UNSUPPORTED IN RECORD]" |
| **Source Consistency** | Cross-provider characterizations of the same injury are consistent, or inconsistencies are explicitly flagged               | Note inconsistency; recommend reconciliation                                |
| **Contemporaneity**    | Key causation opinions appear in contemporaneous treating physician notes (not just retrospective affidavits)               | Flag as "[CAUSATION OPINION ABSENT FROM CONTEMPORANEOUS RECORDS]"           |
| **Coding Accuracy**    | ICD-10 codes cited are correct and support the claimed injury type (S-codes for traumatic; no premature S = sequela coding) | Flag coding issue with specific correction recommendation                   |
| **Completeness**       | No obvious record category gaps (per the 10-category checklist) that would undermine the causation narrative                | Flag "[RECORD CATEGORY NOT PRODUCED: TYPE]" with priority recommendation    |

### Self-Interrogation for CATASTROPHIC and Disputed Causation Items

For any injury classified as CATASTROPHIC or any causation element where confidence
is below PROBABLE, apply this 3-pass review:

**Pass 1 — Causation Chain Integrity**

- Does each link in the four-element causation chain (mechanism → injury → treatment →
  damages) follow logically from the prior link?
- Would a treating physician — or a retained defense expert — reach the same causation
  conclusion from this record?
- Is there an unbroken temporal and clinical narrative from incident to current status?

**Pass 2 — Completeness**

- Have all 10 record categories been obtained or confirmed as non-existent for this
  plaintiff?
- Is the pre-existing condition baseline fully documented (or confirmed absent)?
- Have pharmacy records been obtained to rule out undisclosed prior opioid use or
  treatment for similar conditions?
- Are all treatment gaps explained and documented?

**Pass 3 — Challenge Resistance**

- What is the strongest Daubert challenge to the primary causation opinion?
- How would a skilled defense IME physician attack this medical chronology?
- Are there inconsistencies in ICD-10 coding across providers that defense will exploit?
- Could any combination of gaps, pre-existing conditions, and M-code diagnoses allow
  defense to construct a plausible alternative causation theory?

### Confidence Scoring

Apply to each major causation claim:

| Level        | Range     | Meaning                                                                                                      | Action                                                                                    |
| ------------ | --------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| **DEFINITE** | 0.90–1.0  | Objective findings + treating physician causation opinion + consistent coding + temporal proximity           | State with full confidence in demand and briefs                                           |
| **HIGH**     | 0.75–0.89 | Strong objective evidence, minor gaps or coding issues, no treating physician causation opinion (obtainable) | Obtain supplemental narrative report before demand                                        |
| **PROBABLE** | 0.55–0.74 | Good support, debatable pre-existing condition, some coding inconsistencies                                  | Retain causation expert; address gaps in demand narrative                                 |
| **POSSIBLE** | 0.35–0.54 | Genuine causation uncertainty; significant pre-existing condition; sparse objective findings                 | Expert required; consider additional diagnostics; assess settlement posture realistically |
| **WEAK**     | 0.0–0.34  | Sparse objective evidence; major causation gaps; pre-existing condition dominates; IME adverse               | Flag for counsel: settlement-only posture likely; aggressive defense expected             |

---

## Glass Box Audit Trail

Include this YAML block at the end of every medical records summary deliverable:

```yaml
glass_box:
  skill_name: "legalcode-medical-records-summarizer"
  matter: "[Matter identifier — do not include PII]"
  analysis_date: "[YYYY-MM-DD]"
  analysis_purpose: "[Trial prep / Settlement demand / Expert briefing / IME rebuttal / Other]"
  user_role: "[Plaintiff counsel / Defense counsel / Neutral / Adjuster]"
  injury_classification: "[CATASTROPHIC / SERIOUS / MODERATE / MINOR]"
  injury_type: "[Orthopedic / Spinal / Neurological / TBI / Soft tissue / Multi-system / Other]"
  jurisdiction: "[State]"
  daubert_or_frye: "[Daubert / Frye / Federal (Daubert)]"
  records_analyzed:
    total_documents: "[N]"
    date_range: "[Start to End]"
    providers_covered: "[Count and types]"
    record_categories_present: "[List categories from 10-category checklist]"
    record_categories_missing: "[Categories not produced / confirmed non-existent]"
  diagnoses_mapped: "[N diagnoses across N injury categories]"
  treatment_phases_identified: "[N phases]"
  treatment_gaps_identified: "[Count — [dates/durations]]"
  pre_existing_conditions_identified: "[Y/N — [classification: DISTINCT/EGGSHELL/AGGRAVATED/CONFOUNDING/CRUMBLING SKULL]]"
  aggravation_analysis_completed: "[Y/N]"
  causation_confidence:
    primary_injury: "[Level — X.XX]"
    secondary_injuries: "[Level — X.XX]"
    pre_existing_aggravation: "[Level — X.XX if applicable]"
  daubert_readiness:
    treating_physician_causation_opinion: "[Present / Absent — [action required]]"
    objective_evidence_present: "[Strong / Moderate / Weak]"
    temporal_proximity: "[Strong (<72hr) / Adequate (72hr-7d) / Weak (>7d) — [reason if weak]]"
    alternative_causes_addressed: "[Addressed / Not addressed — [specifics]]"
  red_flags_identified: "[Count — [brief descriptions]]"
  expert_support_recommended:
    treating_physician_narrative: "[Yes / No / Already exists]"
    retained_causation_expert: "[Yes / No — specialty needed]"
    life_care_planner: "[Yes / No]"
    vocational_expert: "[Yes / No]"
    other: "[Type if applicable]"
  citation_quality_gates_passed: "[N/5 — [any failures noted]]"
  self_interrogation_applied: "[Y/N — applied to: [items]]"
  legalcode_mcp: "[Connected / Not connected]"
  confidence: "[HIGH / MEDIUM / LOW — rationale]"
  limitations:
    - "[Scope limitations or missing record categories]"
    - "[Unverified legal references marked [VERIFY]]"
    - "[Medical causation requires expert confirmation]"
  reviewer: "AI-assisted — requires qualified legal and medical review before use"
```

---

## Anti-Patterns

What NOT to do when reviewing and summarizing medical records for PI litigation:

1. **Reviewing summaries instead of source records**: Accepting a nurse consultant's
   summary or prior medical chronology without spot-checking 10–20% of entries against
   the original records. Errors in summaries propagate to expert opinions and briefs
   with devastating consequences at trial.

2. **Collecting only the obvious providers**: Failing to subpoena pharmacy records,
   prior insurance claim histories, workers' compensation files, SSDI applications,
   and correctional health records. Defense obtains these in discovery; plaintiff must
   review them first to anticipate attacks.

3. **Building causation on temporal proximity alone**: Assuming the timeline proves
   causation ("patient sought care after the accident, therefore the accident caused the
   injury"). Temporal proximity is necessary but not sufficient. Courts routinely exclude
   "post hoc ergo propter hoc" causation opinions as Daubert failures.

4. **Ignoring the 7th ICD-10 character**: Failing to recognize that a treating provider
   switched from "A" (initial encounter) to "S" (sequela) coding signals the provider
   characterized the condition as a late effect of an old injury — not an ongoing acute
   injury. This coding switch is frequently missed and is catastrophic to causation.

5. **Treating all medical records as unbiased**: Assuming all treating provider notes
   are accurate, complete, and unbiased. Providers document defensively, incompletely,
   or with referral incentives. IME physicians often have financial relationships with
   defense insurers generating 50–100% of their income. Credibility assessment is required.

6. **Settling before MMI**: Accepting a settlement offer before maximum medical
   improvement is reached means the full extent of future care needs, permanent
   impairment, and wage loss is unknown. This is the single most common cause of
   systematic PI case under-valuation.

7. **Not reconciling ICD-10 codes across providers**: Two providers treating the same
   injury using different codes — one using S-codes (traumatic) and another using M-codes
   (degenerative) — create an irreconcilable inconsistency unless addressed with a
   treating physician narrative report before demand or trial.

8. **Explaining gaps with client statements only**: The explanation for a treatment gap
   must appear in the medical records themselves — not just in a client deposition or
   declaration that can be attacked for credibility. Work backwards: if the gap was
   caused by financial barriers, the treating physician's next note should reference the
   patient returning after the break due to financial constraints.

9. **Over-relying on subjective complaints without objective corroboration**: Building
   causation entirely on pain complaints and functional limitations without imaging,
   examination findings, or objective indicators. Defense medical experts will destroy
   a purely subjective causation case under Daubert cross-examination.

10. **Missing the pre-incident pharmacy record**: Pharmacy fill histories are the single
    best source for discovering undisclosed prior conditions. A plaintiff with years of
    opioid prescriptions, muscle relaxants, or anti-inflammatories for spinal conditions
    in the pharmacy records — but denying prior treatment — faces catastrophic impeachment.

11. **Not addressing the crumbling skull doctrine**: In cases with significant pre-existing
    degenerative disease, failing to retain an expert who can quantify the acceleration
    of the plaintiff's condition versus its natural progression. Without this analysis,
    defense successfully limits recovery to minimal acceleration damages.

12. **Confusing the radiologist's report with the ordering physician's summary**: The
    controlling objective evidence is the radiologist's own impression section — not the
    ordering physician's characterization of what the radiologist said. These often differ,
    and defense will use the actual radiology report to contradict the treating physician.

13. **Using a generic pain-and-suffering multiplier without record support**: Applying
    a 3x or 4x multiplier in a demand letter without medical record documentation of the
    corresponding severity level, functional limitation, treatment intensity, and
    chronicity. Insurance adjusters are trained to reduce multipliers for unsupported
    severity claims.

14. **Presenting unitemized medical bills**: Total medical expenses without itemization
    allow defense to argue that a portion of the bills are unrelated to the incident.
    Itemized billing records, correlated to ICD-10-coded visit records, are required for
    maximum claim credibility.

15. **Not preparing for the defense IME before trial**: Failing to depose the defense
    IME physician on: their qualifications; financial bias (percentage of income from
    defense IMEs); the duration of the examination versus the detail of the report; and
    the specific records they reviewed versus those not provided. An undeposed IME
    physician testifies unchallenged at trial.

16. **Retaining causation experts who only reviewed summaries**: Expert witnesses who
    render causation opinions based on record summaries (not complete records) are
    vulnerable to catastrophic Daubert cross-examination: "You didn't review the original
    records, did you?" Provide complete records to every expert.

17. **Accepting incomplete record productions without follow-up**: Billing records
    referencing visits not in the clinical record, or treatment notes referencing imaging
    that was never produced, signal an incomplete record production. These gaps must be
    pursued aggressively before discovery cutoffs — records that surface at trial were
    not "newly discovered."

18. **Not documenting the eggshell baseline proactively**: Assuming the absence of prior
    records means the plaintiff had no pre-existing conditions. Absence of records is not
    the same as absence of conditions. The correct approach: obtain a 5-year (minimum)
    pre-incident records sweep and affirmatively document the asymptomatic baseline for
    each body region at issue.

---

## Writing Standards

Apply these standards before delivering any medical records analysis:

**Precision over vagueness**: Write "The January 15 MRI report states 'moderate L4-5
disc herniation with right-sided foraminal narrowing'" — not "the imaging showed disc
problems." Specific findings survive cross-examination; general characterizations do not.

**Objective evidence first**: Lead with objective findings (imaging, exam, surgical) before
subjective complaints. If a section has only subjective evidence, say so explicitly.

**Separate observation from inference**: The medical record says what it says; causation
inferences are the attorney's or expert's analytical overlay. Keep these clearly
distinguished in the output.

**Flag uncertainty with precision**: Use these specific markers:

- `[VERIFY]`: Legal or medical claim that requires independent verification
- `[RECORD GAP]`: A record category or time period not in the produced records
- `[CODING ISSUE]`: ICD-10 code concern requiring treating physician reconciliation
- `[EXPERT REQUIRED]`: A causation element that requires retained expert testimony
- `[DEFENSE RISK: HIGH/MEDIUM/LOW]`: A finding that will be exploited by opposing counsel

**Avoid clinical diagnosis language**: Write "the records document a diagnosis of
cervical radiculopathy" — not "the plaintiff has cervical radiculopathy." The skill
describes what the records contain; the records state what the physician diagnosed.

**Active voice, verb-first**: "The March 3 MRI shows bone marrow edema at T12" — not
"Bone marrow edema at T12 was shown by the March 3 MRI." Active construction is faster
to read and harder to misconstrue under cross-examination.

**Quality gate before delivery**: Before delivering the final output, verify:

- [ ] Every diagnosis cites a specific record, date, and provider
- [ ] Every causation claim identifies its evidentiary basis
- [ ] Every gap has been classified and addressed
- [ ] Every pre-existing condition has been analyzed under the applicable doctrine
- [ ] All confidence scores are calibrated against the evidence actually present
- [ ] The Glass Box audit trail is complete

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

Use legalcode-mcp in Step 9 to verify:

- State-specific Daubert or Frye standard for the identified forum state
- ICD-10 code accuracy for the diagnosed conditions
- State-specific jury instructions on causation, pre-existing conditions, and eggshell
  plaintiff rule for the identified jurisdiction
- Recent case law on admissibility of medical causation testimony in the forum state
- Applicable statutes of limitations for PI claims in the jurisdiction
- State-specific comparative fault / contributory negligence framework

Save results to `/tmp/legalcode-medical-research-[matter-id].md` and mark citations
as VERIFIED in the Glass Box audit trail.

**Without legalcode-mcp:**

- Mark all jurisdiction-specific legal standards with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Rely on the workflow's built-in Daubert/Frye matrix (jurisdiction-agnostic)
- Flag that forum-specific jury instruction research is needed before trial preparation

---

## Localization Notes

This skill is US-focused but adaptable:

**By Daubert / Frye Status:**

- Daubert states (~27): Federal standard applies; 5-factor test; analytical gap
  exclusion most common failure mode
- Frye states (~8): General acceptance standard; typically more permissive for
  standard-of-care causation; standard medical literature usually sufficient
- California (Kelly-Frye): Applies Frye to novel scientific evidence; standard
  causation opinions generally admissible without Daubert-level scrutiny
- Florida (adopted Daubert 2019): Full Daubert analysis required since 2019

**By Eggshell / Aggravation / Crumbling Skull:**

- All states recognize the eggshell plaintiff rule for unforeseeable consequences
- Burden of apportionment proof: plaintiff bears burden in most states; defense bears
  burden in Maine (_Lovely v. Allstate_) and some other states — [VERIFY by jurisdiction]
- Crumbling skull doctrine: recognized in most states; requires defense to prove and
  quantify the inevitability of deterioration — not just assert it

**Non-US Applications (limited):**
The chronology, gap analysis, and pre-existing condition frameworks are applicable in
most common-law PI systems (UK, Canada, Australia). However, ICD-10 analysis, Daubert
criteria, and damages multipliers are US-specific. Replace with jurisdiction-appropriate
causation standards and evidentiary rules.

---

## Output Format Template

Use the following format for all medical records analysis deliverables. Include all
applicable Parts; omit only Parts where no relevant records or findings exist.

---

```markdown
# MEDICAL RECORDS SUMMARY AND CAUSATION ANALYSIS

**Matter**: [Matter Name / File Number — do not include PII in public filings]
**Claimant**: [Name]
**Date of Incident**: [Date]
**Date of Analysis**: [Date]
**Prepared by**: AI-assisted analysis — requires qualified legal and medical review
**Analysis Purpose**: [Trial prep / Settlement demand / Expert briefing / IME rebuttal]
**User Role**: [Plaintiff counsel / Defense counsel / Neutral]

---

## EXECUTIVE SUMMARY

**Overall Injury Classification**: CATASTROPHIC / SERIOUS / MODERATE / MINOR
**Causation Confidence (Primary Injuries)**: DEFINITE / HIGH / PROBABLE / POSSIBLE / WEAK
**Key Findings**:

1. [Finding 1 — one sentence, most important]
2. [Finding 2]
3. [Finding 3]

**Immediate Action Items**:

- [ ] [Tier 1 action — most urgent]
- [ ] [Tier 1 action]

---

## PART A: MEDICAL CHRONOLOGY

### Records Manifest

| Provider   | Specialty   | Record Type                          | Date Range  | Pages | Completeness           |
| ---------- | ----------- | ------------------------------------ | ----------- | ----- | ---------------------- |
| [Provider] | [Specialty] | [Office notes / Imaging / PT / etc.] | [Start–End] | [N]   | Complete / [Gap noted] |

**Record Categories NOT Produced / Confirmed Non-Existent:**

- [Category]: [Status — not requested / requested but not produced / confirmed non-existent]

### Chronological Timeline

| Date   | Provider   | Specialty   | Encounter Type                         | Chief Complaint | Diagnosis (ICD-10) | Treatment   | Key Findings         |
| ------ | ---------- | ----------- | -------------------------------------- | --------------- | ------------------ | ----------- | -------------------- |
| [Date] | [Provider] | [Specialty] | [Office / ER / PT / Imaging / Surgery] | [Complaint]     | [Diagnosis (Code)] | [Treatment] | [Objective findings] |

### Treatment Phase Summary

| Phase    | Date Range     | Treatment Type | Intensity                            | Response                         |
| -------- | -------------- | -------------- | ------------------------------------ | -------------------------------- |
| Acute    | [Dates]        | [Summary]      | CONSERVATIVE / MODERATE / AGGRESSIVE | RESPONDING / PLATEAU / WORSENING |
| Subacute | [Dates]        | [Summary]      | [Level]                              | [Response]                       |
| Chronic  | [Dates]        | [Summary]      | [Level]                              | [Response]                       |
| Post-MMI | [Date forward] | [Summary]      | [Level]                              | [Response]                       |

---

## PART B: DIAGNOSES AND INJURY CLASSIFICATION

### Primary Injuries (Direct Result of Incident)

| Diagnosis   | ICD-10 | 7th Character | Severity Grade | Objective Evidence               | Provider   | Date First Documented | Status                               |
| ----------- | ------ | ------------- | -------------- | -------------------------------- | ---------- | --------------------- | ------------------------------------ |
| [Diagnosis] | [Code] | A/D/S         | GRADE 1–4      | [Imaging finding / Exam finding] | [Provider] | [Date]                | Acute / Chronic / Resolved / Ongoing |

### Secondary Injuries (Cascading from Primary)

| Diagnosis   | ICD-10 | Causal Link to Primary | Severity  | Status   |
| ----------- | ------ | ---------------------- | --------- | -------- |
| [Diagnosis] | [Code] | [Mechanism]            | GRADE 1–4 | [Status] |

### ICD-10 Code Analysis

**External Cause Codes Present**: Yes / No
**Traumatic vs. Degenerative Code Assessment**: [Overall assessment — S-code dominance / M-code concerns / mixed]
**7th Character Issues**: [Any premature D or S coding — specify]
**Cross-Provider Coding Consistency**: CONSISTENT / INCONSISTENT — [details if inconsistent]

---

## PART C: TREATMENT INTENSITY AND PROGRESSION

### Treatment Intensity by Phase

| Phase   | Dates   | Key Treatments | Intensity Level                      | Escalation Trigger                    | Response                                        |
| ------- | ------- | -------------- | ------------------------------------ | ------------------------------------- | ----------------------------------------------- |
| [Phase] | [Dates] | [List]         | CONSERVATIVE / MODERATE / AGGRESSIVE | [Clinical finding driving escalation] | RESPONDING / PLATEAU / WORSENING / INCONSISTENT |

### Medication Progression

| Date Range | Medications     | Class                               | Severity Signal           | Notes                               |
| ---------- | --------------- | ----------------------------------- | ------------------------- | ----------------------------------- |
| [Dates]    | [Medication(s)] | OTC / Prescription / Opioid / Other | Minimal / Moderate / High | [Consistency with claimed severity] |

### Treatment Escalation Assessment

**Escalation Well-Documented**: Yes / No / Partially
**Key Escalation Points**: [List each major treatment escalation with clinical justification from records]
**Inconsistencies**: [Any inconsistency between claimed severity and actual medication / treatment level]

---

## PART D: DIAGNOSTIC TESTING SUMMARY

### Imaging Studies

| Date   | Modality                 | Body Region | Radiologist | Key Findings         | Severity Grade | Baseline Comparison              | Objective Trauma Markers        |
| ------ | ------------------------ | ----------- | ----------- | -------------------- | -------------- | -------------------------------- | ------------------------------- |
| [Date] | MRI / CT / X-ray / Other | [Region]    | [Name]      | [Impression summary] | GRADE 1–4      | [N/A / vs. [date] prior imaging] | [HIZ / Edema / Hematoma / None] |

### Electrodiagnostic Studies

| Date   | Study   | Performing Physician | Key Findings | Interpretation                                      | Severity   |
| ------ | ------- | -------------------- | ------------ | --------------------------------------------------- | ---------- |
| [Date] | EMG/NCS | [Physician]          | [Findings]   | [Normal / Denervation / Radiculopathy / Myelopathy] | [Severity] |

### Functional Assessments

| Date   | Assessment        | Evaluator | Key Findings | Work Capacity           | Permanent Restrictions |
| ------ | ----------------- | --------- | ------------ | ----------------------- | ---------------------- |
| [Date] | FCE / IME / Other | [Name]    | [Summary]    | [Full / Partial / None] | [If any]               |

### Imaging Assessment

**Pre-Incident Baseline Available**: Yes / No
**Acute Trauma Markers Present**: Yes / No — [List: HIZ / Bone marrow edema / Hematoma / Avulsion]
**Degenerative Findings**: Yes / No — [Details if present — defense challenge assessment]
**Radiologist vs. Treating Physician Consistency**: Consistent / Inconsistent — [Specify if inconsistent]

---

## PART E: TREATMENT GAPS AND COMPLIANCE

### Treatment Gaps

| Gap Period  | Duration | Before Gap       | After Gap        | Reason Documented in Record       | Classification                            | Defense Risk        |
| ----------- | -------- | ---------------- | ---------------- | --------------------------------- | ----------------------------------------- | ------------------- |
| [Start–End] | [Days]   | [Last treatment] | [Next treatment] | Yes / No — [Reason if documented] | EXPECTED / EXPLAINED / CONCERN / RED FLAG | LOW / MEDIUM / HIGH |

### Compliance Issues

| Issue        | Date(s)   | Details     | Defense Argument | Rebuttal Option  |
| ------------ | --------- | ----------- | ---------------- | ---------------- |
| [Issue type] | [Date(s)] | [Specifics] | [Defense use]    | [How to address] |

### Gap Assessment Summary

**Total gaps identified**: [N]
**Longest gap**: [Duration] — [Classification]
**Unexplained gaps requiring documentation**: [Count] — [Specifics]
**Recommended action**: [What records or client documentation needed]

---

## PART F: PRE-EXISTING CONDITIONS ANALYSIS

### Pre-Incident Baseline

| Body Region | Last Pre-Incident Record | Status at Incident                                | Notes                      |
| ----------- | ------------------------ | ------------------------------------------------- | -------------------------- |
| [Region]    | [Date / Provider]        | Asymptomatic / Stable / Symptomatic / Progressive | [Specific findings if any] |

### Pre-Existing Condition Analysis

| Condition   | ICD-10 | Pre-Incident Status                   | Post-Incident Status | Doctrine                                                         | Aggravation Delta                               | Causation Confidence                         |
| ----------- | ------ | ------------------------------------- | -------------------- | ---------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------- |
| [Condition] | [Code] | [Asymptomatic / Stable / Progressive] | [New severity level] | DISTINCT / EGGSHELL / AGGRAVATED / CONFOUNDING / CRUMBLING SKULL | [Quantified increase: visits / meds / function] | DEFINITE / HIGH / PROBABLE / POSSIBLE / WEAK |

### Aggravation Delta Summary
```

Pre-Incident Baseline — [Condition]:
Treatment frequency: [visits/month]
Medications: [list]
Functional restrictions: [none / specific]
Pain level: [documented level]

Post-Incident Status:
Treatment frequency: [increase]
Medications: [additions]
Functional restrictions: [new / increased]
Pain level: [increase]

Aggravation Assessment:
Doctrine: [EGGSHELL / AGGRAVATED / CONFOUNDING / CRUMBLING SKULL]
Delta magnitude: [Quantified]
Defendant's liability: [Full / Aggravation delta only / Acceleration only]

```

---

## PART G: CAUSATION NARRATIVE

### Four-Element Causation Chain Assessment
| Element | Evidence | Strength | Vulnerability |
|---------|---------|---------|--------------|
| 1. Incident Mechanism | [Description consistent with injuries?] | STRONG / MODERATE / WEAK | [Any inconsistency] |
| 2. Injury Symptomatology | [Temporal onset and clinical presentation] | STRONG / MODERATE / WEAK | [Any delay / inconsistency] |
| 3. Objective Evidence | [Imaging / exam / surgical findings supporting injury] | STRONG / MODERATE / WEAK | [Defense challenges] |
| 4. Alternative Causes Addressed | [Pre-existing / concurrent / unrelated conditions] | STRONG / MODERATE / WEAK | [Alternative theories not yet rebutted] |

### Causation Confidence Assessment
| Injury | Confidence Level | Score | Basis | Key Vulnerability |
|--------|----------------|-------|-------|------------------|
| [Primary injury] | DEFINITE / HIGH / PROBABLE / POSSIBLE / WEAK | [0.XX] | [Objective evidence + treating opinion + temporal proximity] | [Main defense challenge] |

### Daubert Readiness Assessment
| Requirement | Status | Action Required |
|-------------|--------|----------------|
| Treating physician causation opinion | Present / Absent | [Obtain narrative report if absent] |
| Objective evidence supporting causation | Strong / Moderate / Weak | [Additional diagnostics if weak] |
| Temporal proximity | Strong / Adequate / Weak | [Address delay if weak] |
| Alternative causes addressed | Addressed / Partially / Not addressed | [Expert opinion if significant alternatives] |
| Expert methodology peer-reviewed | Yes / Needs confirmation | [Confirm with expert if unclear] |
| State standard (Daubert / Frye) | [State standard] | [Confirm specific requirements] |

---

## PART H: DAMAGES TIMELINE SUPPORT

### Past Medical Expenses
| Date Range | Provider | Service | Diagnosis Basis | Amount | Related to Incident |
|------------|----------|---------|-----------------|--------|-------------------|
| [Dates] | [Provider] | [Service type] | [ICD-10 code] | $[Amount] | Yes / No / Partially |

**Past Medical Total (Incident-Related)**: $[Amount]
**Disputed Amount**: $[Amount] — [Basis for dispute]

### Lost Wages / Earning Capacity
| Period | Employer Documentation | Basis | Amount |
|--------|----------------------|-------|--------|
| [Dates] | [Employer records / Tax returns / Other] | [Hourly rate × hours / Salary] | $[Amount] |

**Lost Wage Total**: $[Amount]

### Future Medical Care
| Treatment | Frequency | Annual Cost | Duration | Present Value |
|-----------|-----------|-------------|----------|--------------|
| [Treatment] | [Frequency] | $[Annual] | [Years / Life] | $[PV] |

**Future Care Total (Estimated)**: $[Amount]
**Life Care Plan**: Required / Not yet obtained / [Planner name if obtained]

### Non-Economic Damages
| Category | Documentation | Multiplier Range | Estimated Range |
|----------|--------------|-----------------|-----------------|
| Pain and suffering | [Severity grade + functional documentation basis] | [Low–High] | $[Range] |
| Loss of enjoyment | [Documented activity limitations] | [Low–High] | $[Range] |
| Loss of consortium | [Documented impact on relationship] | [Low–High] | $[Range] |

---

## PART I: EXPERT SUPPORT RECOMMENDATIONS

| Expert Type | Need | Key Opinions Required | Priority |
|-------------|------|-----------------------|---------|
| Treating physician narrative report | [Yes / No / Already exists] | Causation opinion + permanency + future care | TIER 1 if absent |
| Retained causation expert ([Specialty]) | [Yes / No] | [Specific opinions needed] | [Tier] |
| Life care planner | [Yes / No] | Future medical costs + permanent care needs | TIER 1 for CATASTROPHIC/SERIOUS |
| Vocational expert | [Yes / No] | Earning capacity loss + vocational limitations | TIER 1 if permanent work restrictions |
| Forensic economist | [Yes / No] | Present value of future losses + lost wages | TIER 2 for significant economic damages |
| IME rebuttal expert | [Yes / No — if adverse IME obtained] | Rebut specific IME opinions | TIER 1 if IME adverse |

### Key Questions for Primary Causation Expert
1. Within a reasonable degree of medical certainty, did the [incident date] incident
   cause the [primary diagnosis]?
2. Are the treatment intensity and progression documented in the records consistent with
   the diagnosed injuries?
3. Was any pre-existing condition for [body region] materially aggravated by the incident?
4. What further medical treatment is reasonably necessary and causally related to the
   incident?
5. Is there any plausible alternative explanation for the [primary diagnosis] that is
   more likely than the incident?

---

## PART J: RED FLAGS AND ACTION ITEMS

### Red Flags Identified
| Flag | Record / Date | Defense Argument | Risk Level | Recommended Action |
|------|--------------|-----------------|-----------|-------------------|
| [Flag type] | [Record ref] | [How defense uses it] | HIGH / MEDIUM / LOW | [Action] |

### Tier 1 Action Items (Must address)
- [ ] [Action] — [Deadline / Priority]

### Tier 2 Action Items (Should address)
- [ ] [Action]

### Tier 3 Action Items (Enhances case quality)
- [ ] [Action]

---

## PART K: GLASS BOX AUDIT TRAIL

[Insert completed Glass Box YAML from audit trail section]

---

## APPENDIX A: Provider Credibility Matrix
| Provider | Specialty | Note Quality | Potential Bias | Contemporaneity | Causation Opinion | Assessment |
|----------|-----------|-------------|---------------|-----------------|------------------|-----------|
| [Name] | [Specialty] | Detailed / Sparse / Incomplete | None / Defense IME / Referral incentive | Timely / Retrospective | Present / Absent | Strong / Moderate / Weak / Compromised |

## APPENDIX B: Complete Detailed Chronology
[Full date-by-date record of every encounter with full clinical notes summary]

## APPENDIX C: ICD-10 Code Reference
[Complete list of all ICD-10 codes present in the records with descriptions and classifications]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis via Mode A creation workflow.
Research pipeline: 2-agent parallel research (structural analysis agent examining
`legalcode-damages-calculation` and `legalcode-early-case-assessment` reference skills;
legal research agent conducting 8 targeted web searches across medical records
summarization practice, ICD-10 PI methodology, gap analysis doctrine, pre-existing
condition doctrines, Daubert/Frye standards, and settlement value research). Key
sources: EvenUp Law (medical chronology methodology), PAXTON AI (AI-enhanced medical
records best practices), Paralegal Boot Camp (summarization techniques), CasePeer
(records management), Expert Institute (Daubert vs. Frye standards), PMC/NCBI (Daubert
and medical expert witnesses), Plaintiff Magazine (eggshell plaintiff doctrine), Berman
& Simmons (2025 eggshell plaintiff guide), Robinson & Kole (treatment gaps), EvenUp
Law (gap mitigation), PubMed (ICD-10 external cause framework), Grundy MD Consulting
(attorney guide to medical record review), AllLaw (settlement calculator methodology).
Skill scope: US personal injury; general medical records review methodology;
jurisdiction markers for Daubert/Frye; ICD-10 analysis; eggshell/aggravation/crumbling
skull doctrine framework; 10-category record checklist; 18-element Legalcode quality
standard. Quality: 18/18 elements present; prompt engineering score: 37/40.
