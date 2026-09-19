---
name: legalcode-us-ada-accommodation
description: Guides ADA Title I reasonable accommodation analysis — disability determination under ADAAA,
  essential functions analysis, interactive process compliance, accommodation options, undue hardship
  defense, and direct threat defense. Covers intersections with FMLA leave, the Pregnant Workers Fairness
  Act (PWFA), and state disability laws (CA FEHA, NY NYSHRL, NJ LAD, MA Chapter 151B, WA WLAD). Use when
  responding to an accommodation request, evaluating a denial, assessing interactive process compliance,
  auditing HR accommodation practices, advising on return-to-work situations, or analyzing ADA exposure
  in pending or threatened litigation. Triggers on any task involving Americans with Disabilities Act
  Title I, ADAAA, reasonable accommodation, undue hardship, interactive process, disability in the workplace,
  disability leave, return to work, or ADA accommodation request. US-federal-law-specific with state law
  overlay guidance.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode US ADA Reasonable Accommodation

> **Disclaimer**: This skill provides a framework for AI-assisted ADA Title I accommodation
> analysis. It does not constitute legal advice. All outputs should be reviewed by a qualified
> employment attorney licensed in the relevant jurisdiction before use. Laws change; EEOC
> guidance evolves; state law developments are frequent — verify current applicability before
> relying on any provision described here. Statutory and case law references carry hallucination
> risk — verify against authoritative sources before relying on them.

## Purpose and Scope

This skill guides systematic, legally defensible analysis of ADA Title I reasonable
accommodation situations. It walks through disability determination under the ADAAA, essential
functions analysis, interactive process requirements, the full spectrum of accommodation
options, undue hardship and direct threat defenses, and the intersection with FMLA, PWFA,
and state disability laws.

**Covers:**

- Disability determination analysis under the ADAAA three-prong framework
- Essential functions analysis per 29 C.F.R. § 1630.2(n)
- Interactive process good-faith assessment
- Accommodation option identification and hierarchy
- Undue hardship defense analysis under 42 U.S.C. § 12111(10)
- Direct threat defense analysis under 42 U.S.C. § 12113(b)
- FMLA and ADA concurrent/sequential leave coordination
- PWFA (Pregnant Workers Fairness Act) intersection analysis
- State disability law overlay (CA, NY, NJ, MA, WA, and others)
- EEOC charge exposure assessment and litigation risk evaluation
- Accommodation classification with actionable remediation steps

**Does not:**

- Provide legal advice or substitute for qualified employment counsel
- Address ADA Title II (public entities) or Title III (public accommodations)
- Provide definitive medical or functional capacity opinions
- Replace individualized assessment by HR, occupational health, or legal professionals

## Jurisdiction and Governing Law

This skill is US-law-specific. Federal law (ADA Title I, ADAAA) applies to employers
with 15 or more employees. State disability laws frequently expand coverage (lower employee
thresholds, broader disability definitions, greater remedies). The skill analyzes under
federal law first, then flags applicable state law overlays.

**Key statutory authority:**

- Americans with Disabilities Act of 1990: 42 U.S.C. § 12101 et seq.
- ADA Amendments Act of 2008 (ADAAA): Effective January 1, 2009
- EEOC Implementing Regulations: 29 C.F.R. Part 1630
- Pregnant Workers Fairness Act: 42 U.S.C. § 2605 et seq. (effective June 27, 2023)
- EEOC PWFA Regulations: 29 C.F.R. Part 1636

**[JURISDICTION-SPECIFIC] State law overlays require separate analysis:**

- California FEHA (Gov. Code §§ 12940–12951): 5+ employees; "limits" (not "substantially limits")
- New York NYSHRL (Exec. Law § 290 et seq.): 4+ employees; broader coverage
- New Jersey LAD (N.J.S.A. 10:5-1 et seq.): 1+ employees in certain provisions
- Massachusetts Chapter 151B: Covers employers with 6+ employees for disability claims
- Washington WLAD (RCW 49.60): Covers any employer with 8+ employees
- Many states: Lower employee thresholds, broader definitions, uncapped damages

---

## Interactive Clarification Convention

This skill uses **⟁ CLARIFY** at key decision points where the user's input materially
changes the analysis direction. Present options in a structured format with descriptions.
If the user has already provided the relevant information, skip the clarification and proceed.

Do not ask clarifying questions simultaneously — stage them logically through the workflow.

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:

- **Accommodation request document**: Written request from employee or representative
- **Medical documentation**: Physician notes, functional capacity evaluations, treatment records
- **HR case file**: Summary of prior interactions, prior accommodations, communications log
- **Situation narrative**: Description of the accommodation situation and business context
- **Audit scope**: Request to audit existing accommodation practices or policies
- **Litigation context**: Complaint, EEOC charge, or demand letter requiring response analysis

If no input is provided, prompt the user to supply one and identify the type of analysis needed.

---

### Step 2: Gather Organizational Context

**⟁ CLARIFY** — Ask the user these questions before proceeding. Present as structured options:

1. **Employer profile:**
   - Number of employees (determines federal ADA coverage — 15+ required; state law thresholds differ)
   - Industry and sector (healthcare, government contractor, manufacturing, professional services)
   - State(s) of operation (determines applicable state disability law overlays)
   - _Why this matters_: ADA's 15-employee threshold gates coverage entirely; state law may apply below that threshold.

2. **Role in this analysis:**
   - Options: Employer/HR analyzing an inbound request, Employment counsel advising client,
     Employee or employee advocate, Compliance auditor reviewing past practices, Litigator
     assessing ADA exposure, Other
   - _Why this matters_: Determines framing of output (employer-side risk analysis vs. employee
     rights assessment vs. compliance audit).

3. **Type of analysis needed:**
   - Options: Active accommodation request (new request to analyze), Return-to-work situation,
     Denial review (was a denial legally defensible?), Interactive process audit (was process
     followed correctly?), Litigation/EEOC charge defense, General compliance audit, Other
   - _Why this matters_: Determines which workflow steps receive deeper treatment.

4. **State law applicability:**
   - Identify state(s) where employee works and where employer is headquartered
   - _Why this matters_: State laws vary significantly; California FEHA imposes duties far
     beyond ADA; New York City HRL is even broader than state law.

5. **Prior accommodation history:**
   - Has the employer previously provided accommodations to this employee or this job category?
   - _Why this matters_: Prior accommodation attempts create evidentiary record; successful
     remote work (even temporarily) may preclude undue hardship defense for remote work requests.

If the user provides partial context, proceed with stated assumptions and flag them explicitly.

---

### Step 3: Gather Legal Authority

Search **legalcode-mcp** for ADA Title I authority relevant to the specific accommodation
situation. Build a working reference file before conducting analysis.

**Research categories:**

1. Core ADAAA disability definition and EEOC final regulations (29 C.F.R. Part 1630)
2. EEOC Enforcement Guidance on Reasonable Accommodation and Undue Hardship (October 2002)
3. EEOC Guidance: Employer-Provided Leave and the ADA
4. EEOC Guidance: Work at Home/Telework as a Reasonable Accommodation
5. Relevant case law for the specific accommodation type at issue
6. Applicable state law authority for states identified in Step 2

**Save results** to `/tmp/legalcode-ada-accommodation-authority.md` with this structure:

```markdown
# ADA Accommodation Legal Authority Reference

## Date: [date]

## Accommodation Situation: [brief description]

### Federal Statutory Authority

- [Statute, section, current text or summary]

### EEOC Regulations

- [29 C.F.R. section, content relevant to this situation]

### EEOC Guidance Documents

- [Document title, date, key guidance points relevant to this case]

### Case Law

- [Case name, citation, key holding]

### State Law Authority

- [State, statute, key differences from federal law]
```

**If legalcode-mcp is not connected:**

- Mark all statutory/case law references in the analysis with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Proceed using the legal framework described in this skill, but flag that authority
  has not been independently verified against current text

---

### Step 4: Disability Determination Analysis

Apply the ADAAA three-prong framework. Assess whether the employee qualifies as having a
"disability" under any of the three prongs.

#### Prong 1: Actual Disability (42 U.S.C. § 12102(1)(A))

Assess whether a physical or mental impairment **substantially limits** one or more **major
life activities**, disregarding ameliorative effects of mitigating measures.

**Substantially limits** (post-ADAAA, lower threshold):

- The impairment need not prevent or severely restrict a major life activity
- Comparison class: most people in the general population
- Assess WITHOUT regard to: medication, medical equipment, assistive technology,
  learned behavioral modifications, reasonable accommodations, or similar measures
  (except ordinary eyeglasses/contact lenses — ADAAA § 4(e)(2))

**Major life activities** (29 C.F.R. § 1630.2(i)):

- Activities: caring for oneself, performing manual tasks, seeing, hearing, eating,
  sleeping, walking, standing, sitting, reaching, lifting, bending, speaking, breathing,
  learning, reading, concentrating, thinking, communicating, interacting with others
- Bodily functions: immune system, cell growth, digestive, bowel, bladder, neurological,
  brain, respiratory, circulatory, cardiovascular, endocrine, hemic, lymphatic,
  musculoskeletal, reproductive, and special sense organs/skin

**Episodic and in-remission conditions** (42 U.S.C. § 12102(4)(D)):

- A condition that is episodic or in remission qualifies if it would substantially limit
  a major life activity when active
- Covers: cancer in remission, epilepsy, bipolar disorder, PTSD, diabetes, migraines,
  asthma, HIV infection

**Assess and document:**

- [ ] Identified impairment and its nature
- [ ] Major life activity or bodily function affected
- [ ] Substantially limiting without mitigating measures
- [ ] Whether episodic/in-remission analysis applies
- [ ] Whether burden of mitigating measures (side effects, compliance demands) is considered

#### Prong 2: Record of Disability (42 U.S.C. § 12102(1)(B))

Assess whether the employee has a **record of** a physical or mental impairment that
substantially limited a major life activity in the past.

- Covers individuals who have fully recovered from a disability
- Covers individuals with a history of a substantially limiting condition
- Same expansions (episodic protection, disregard mitigating measures) apply

**Assess and document:**

- [ ] Prior diagnosis, treatment history, or medical record establishing past disability
- [ ] Whether employer has knowledge of the prior record
- [ ] Whether accommodation is sought based on this prong or Prong 1

#### Prong 3: Regarded As Having a Disability (42 U.S.C. § 12102(1)(C))

Assess whether the employer took an adverse employment action based on **actual or perceived**
impairment, regardless of whether the impairment in fact limits a major life activity.

**Key rules:**

- Impairment need not actually meet the ADA disability test
- No need to show the impairment substantially limits a major life activity
- Exception: impairment must not be "transitory and minor" (expected duration of 6 months
  or less AND objectively minor) — 42 U.S.C. § 12102(3)(B)
- **Accommodation limitation**: Individuals covered solely under "regarded as" are NOT
  entitled to reasonable accommodation — 42 U.S.C. § 12201(h)

**⟁ CLARIFY** — If the covered prong is unclear or disputed:

- "Is the claimed disability based on an actual current impairment, a prior medical history,
  or the employer's perception of the employee? This determines whether accommodation is
  required (Prongs 1 and 2) or only anti-discrimination protection applies (Prong 3)."

**Assess and document:**

- [ ] Whether employer's adverse action was based on actual or perceived impairment
- [ ] Whether the perceived impairment is transitory and minor (6-month exception)
- [ ] Whether accommodation obligation exists (Prongs 1/2 only, not Prong 3 alone)

---

### Step 5: Essential Functions Analysis

Identify the position's essential functions before assessing accommodation feasibility.
Reasonable accommodation enables performance of essential functions — it never requires
elimination of essential functions.

**Definition** (29 C.F.R. § 1630.2(n)):
A job function is **essential** if:

1. The reason the position exists is to perform that function
2. There are limited employees available to perform the function
3. The function is so specialized that the person is hired for their expertise in it

**Evidence factors for essential functions** (29 C.F.R. § 1630.2(n)(3)):

- Employer's judgment about which functions are essential
- Written job descriptions prepared before advertising or interviewing (evidence, not
  determinative)
- Amount of time spent performing the function
- Consequences of not performing the function
- Terms of collective bargaining agreements
- Work experience of current and past incumbents in the position
- Work experience of incumbents in similar positions at other employers

**Analytical principles:**

- Focus on the OUTCOME or RESULT required, not the specific manner of performance
- Reasonable accommodation often enables achievement of the same result differently
- "How" a function is performed can often be accommodated; whether the function must be
  performed at all is the essential question
- Courts scrutinize job descriptions that conflict with actual practice; do not uncritically
  defer to written descriptions
- The inability to perform marginal (non-essential) functions is NOT a basis for denial

**⟁ CLARIFY** — If essential functions are disputed:

- "Is there disagreement about whether [specific function] is essential to this role?
  I'll analyze the factors from 29 C.F.R. § 1630.2(n)(3), but context on actual practice,
  time spent, and consequences of non-performance will determine weight."

**Assess and document for each claimed essential function:**

- [ ] How frequently performed and percentage of time
- [ ] Consequence if function not performed (operational, safety, service impact)
- [ ] Whether other employees can perform the function
- [ ] Whether function appears in written job description (and whether description was
      prepared pre-hire)
- [ ] Whether similarly situated employees are required to perform this function
- [ ] Whether prior incumbents performed this function

---

### Step 6: Interactive Process Assessment

The interactive process is the employer's legal obligation to engage in a good-faith,
flexible dialogue with the employee to identify an effective accommodation. Failure to
engage may independently violate the ADA.

**Triggering the interactive process:**

- Employee requests accommodation (need not use magic words; "I need help due to my
  condition" can trigger the obligation)
- Employer becomes aware of employee's disability-related limitations (awareness trigger)
- Employee's disability is obvious and limitations apparent to reasonable employer

**Employer's good-faith obligations:**

1. **Respond promptly** to accommodation requests (EEOC expects expeditious response;
   weeks of delay without explanation may constitute bad faith)
2. **Acknowledge and accept** the request for dialogue
3. **Gather medical information** — request documentation sufficient to identify:
   - The nature of the condition (not diagnosis; functional limitations)
   - How limitations affect the ability to perform essential functions
   - What types of accommodation may be effective
4. **Identify possible accommodations** through collaboration with employee, HR, occupational
   health, JAN (Job Accommodation Network), and the employee's healthcare provider
5. **Assess feasibility** of proposed accommodations (effectiveness + undue hardship)
6. **Communicate decisions** with explanation; do not silently deny or ignore
7. **Revisit if initial accommodation fails**: Interactive process continues until an
   effective accommodation is found or genuine undue hardship proven

**Employee's good-faith obligations:**

- Participate in the process in good faith
- Provide medical documentation sufficient to establish the need
- Describe functional limitations clearly (not required to suggest specific accommodations)
- Consider employer's reasonable alternative suggestions
- Not unreasonably reject feasible alternatives that would be effective

**Conduct that breaks the interactive process:**

- Employer: refusing to engage; demanding employee cure disability; unilateral denial
  without discussion; terminating during process; demanding unnecessary medical information
- Employee: refusing to provide any medical documentation; rejecting all options without
  explanation; abandoning process entirely

**⟁ CLARIFY** — If the interactive process has already occurred and its adequacy is at issue:

- "Has there been any communication between the employer and employee about the
  accommodation request? Please describe what occurred and when, so I can assess whether
  the interactive process met the good-faith standard."

**Assess and document:**

- [ ] Date accommodation request received (or awareness date)
- [ ] Employer's response timeline
- [ ] Whether employer acknowledged request and invited dialogue
- [ ] Whether medical documentation was requested (appropriate scope — not overly broad)
- [ ] Whether possible accommodations were identified and considered
- [ ] Whether employee participated in good faith
- [ ] Whether any accommodation was offered; if denied, reason given
- [ ] Whether process was documented throughout (contemporaneous records)

---

### Step 7: Accommodation Options Analysis

Identify the full spectrum of potentially effective accommodations before assessing
feasibility. Employer may choose among effective options but cannot unilaterally select
the least costly without considering employee preference.

**Categories of reasonable accommodation:**

| Category                           | Examples                                                                                           | Key Considerations                                                                                   |
| ---------------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Schedule modification**          | Flexible start/end times, part-time schedule, compressed work week, leave for medical appointments | FMLA interaction; intermittent leave; shift change                                                   |
| **Location modification**          | Telework (full or part-time), reassignment to different worksite                                   | COVID precedent: prior successful telework may be evidentiary; essential functions analysis critical |
| **Job restructuring**              | Reassigning marginal functions, modifying how essential functions are performed                    | Cannot eliminate essential functions; can redistribute marginal ones                                 |
| **Leave of absence**               | Paid or unpaid leave for treatment, recovery, or episodic flare-ups                                | ADA may require leave beyond FMLA 12 weeks; undue hardship analysis applies                          |
| **Assistive technology**           | Screen readers, voice recognition software, ergonomic equipment, specialized workstation           | JAN database is key resource; employer may select among effective options                            |
| **Personal assistance**            | Sign language interpreter, reader, job coach, note-taker                                           | Frequency and duration affect undue hardship analysis                                                |
| **Accessible facilities**          | Accessible parking, modified workstation, proximity to restroom                                    | Physical plant constraints may affect feasibility                                                    |
| **Modified testing/evaluation**    | Extended time, alternative format for performance evaluations                                      | Required as accommodation for the evaluation process itself                                          |
| **Reassignment**                   | Transfer to vacant position the employee qualifies for                                             | Last resort when no other effective accommodation exists in current position                         |
| **Attendance policy modification** | Excusing disability-related absences from attendance records, no-fault policies                    | Must distinguish disability-caused absences from general attendance management                       |

**Reassignment — the last resort rule:**

- Reassignment required when no other effective accommodation exists in current position
- Must reassign to a **vacant** position — no obligation to create a position or displace another employee
- Employee must be qualified for the vacant position (not require additional training beyond what employer would provide)
- US Airways, Inc. v. Barnett, 535 U.S. 122 (2002): Seniority system ordinarily prevails over reassignment request, but exceptions possible for "special circumstances"
- Best practice: consider reassignment in the interactive process even before it becomes "last resort"

**Indefinite leave — not required:**

- ADA does not require leave with no expected return date
- Leave must be: (a) for a fixed, determinable period, OR (b) tied to a known medical milestone
- "Possibly never returning" = effectively eliminating the essential function = not a reasonable accommodation
- However, "we don't know exactly when but treatment ends in 6–8 weeks" is generally required

**Remote work — post-COVID analysis:**

- Prior successful telework (including during pandemic) is **evidence** that essential functions
  can be performed remotely — EEOC COVID guidance confirms employers cannot simply ignore this
- Bodie-Jernigan v. School Board of Broward County, Fla. (11th Cir. Sept. 2025): Court
  dismissed claim where teacher could not demonstrate classroom management remotely
- Lesson: remote work feasibility turns on careful, function-by-function essential analysis,
  not blanket policy

**⟁ CLARIFY** — For requests involving novel or costly accommodation types:

- "Has this accommodation type been tried in this role or similar roles before? Prior
  successful use significantly strengthens the case for feasibility."
- "Are there alternative accommodations that might achieve the same result at lower cost
  or disruption? I'll identify all options so the employer can choose among effective ones."

**Assess and document:**

- [ ] Full list of accommodation options identified
- [ ] Which options employee prefers (preference must be considered, not binding)
- [ ] Which options employer assessed as effective
- [ ] Which options employer assessed as creating undue hardship (with documented reasoning)
- [ ] Accommodation chosen and implementation timeline
- [ ] Monitoring plan for effectiveness assessment

---

### Step 8: Defenses — Undue Hardship and Direct Threat

Analyze available statutory defenses only after concluding that accommodation would
otherwise be required. These are affirmative defenses — the employer bears the burden.

#### 8A: Undue Hardship Defense (42 U.S.C. § 12111(10))

**Standard**: "Significant difficulty or expense" — not mere inconvenience or minor disruption.

**Four statutory factors** (42 U.S.C. § 12111(10)(B)):

| Factor                                | What to Assess                                                                                                          |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Nature and cost**                   | Direct and indirect cost of accommodation; not measured against employee's pay but against employer's overall resources |
| **Financial resources of facility**   | Revenue, assets, expenses, employee count at the specific worksite                                                      |
| **Financial resources of the entity** | Total organizational resources; number and location of all facilities; overall employee count; gross revenue            |
| **Type of operation**                 | Composition, structure, and functions of workforce; administrative/fiscal structure; geographic separateness            |

**Analytical rules:**

- **Cost alone rarely establishes undue hardship** in a large or mid-size employer
- **Coworker resentment or inconvenience is irrelevant** — cannot establish undue hardship
  based on employee morale or perceived fairness concerns
- **Tax credits must be considered**: Disabled Access Credit (IRC § 44) — up to $5,000 per
  year for eligible small businesses; Work Opportunity Tax Credit (WOTC) for hiring individuals
  with disabilities
- **Employer must provide specific, concrete evidence** — speculation insufficient
- **Operational disruption must be significant**, not speculative; document actual impact

**Burden of proof:**

1. Employee shows accommodation appears reasonable on its face (presumption arises)
2. Employer must demonstrate special circumstances creating undue hardship with specific evidence
3. Employer cannot rely on assumptions or conclusory assertions

**⟁ CLARIFY** — If cost is the basis for an undue hardship claim:

- "What is the estimated cost of the accommodation? What are the employer's annual revenues
  and total employee count? This is necessary to assess whether cost rises to undue hardship —
  small employers have more latitude; large employers bear a heavier burden."

#### 8B: Direct Threat Defense (42 U.S.C. § 12113(b))

**Standard**: Significant risk of substantial harm to the health or safety of the individual
or others that cannot be eliminated or reduced to acceptable levels by reasonable accommodation.

**Four-factor objective assessment** (29 C.F.R. § 1630.2(r)):

1. **Nature of the risk**: What type of harm is threatened?
2. **Duration of risk**: How long would the risk persist?
3. **Severity/probability**: How severe is potential harm; how likely is it to occur?
4. **Imminence**: Is harm imminent or speculative?

**Key case law:**

- Chevron U.S.A. Inc. v. Echazabal, 536 U.S. 73 (2002): Direct threat includes threat to
  employee's own health; employer must conduct individualized assessment based on objective
  medical evidence
- **Blanket exclusions by disability type are per se violations**
- **Employer cannot rely on lay judgments, assumptions, or stereotypes** — must be grounded
  in "most current medical knowledge" or "best available objective evidence"
- If reasonable accommodation would eliminate or reduce risk to acceptable levels,
  direct threat defense is unavailable

**Individualized assessment requirement:**

- Assess the individual's specific medical circumstances, not disability category
- Consider specific job duties and actual exposure
- Consult occupational health professionals or the employee's treating physician
- Document the basis for the threat determination

**Assess and document:**

- [ ] Specific harm identified (not vague safety concern)
- [ ] Objective medical evidence supporting threat assessment
- [ ] Individualized (not categorical) analysis conducted
- [ ] Whether accommodation could reduce risk to acceptable levels
- [ ] Qualified medical or occupational health professional consulted

---

### Step 9: Intersecting Statutory Obligations

#### 9A: FMLA and ADA Coordination

**Framework:**

| Scenario                                                    | Legal Rule                                                                           |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Employee qualifies under both FMLA and ADA                  | Leave runs concurrently; count against both entitlements simultaneously              |
| FMLA 12 weeks exhausted; employee cannot yet return         | ADA may require additional unpaid leave if fixed/determinable and not undue hardship |
| Employee ineligible for FMLA (tenure, hours, worksite size) | ADA accommodation duty continues independently                                       |
| Employee on ADA leave performing no essential functions     | Not a reasonable accommodation if leave is indefinite                                |

**Coordination rules:**

- FMLA compliance does **not** automatically satisfy ADA
- Exhaustion of FMLA leave is **not** automatic grounds for ADA termination
- Employer must separately assess whether additional leave is a reasonable accommodation
  under the ADA before terminating post-FMLA
- EEOC Guidance: "Employer-Provided Leave and the Americans with Disabilities Act" (May 2016)
  is the primary authority

**Documentation requirement:**

- Track FMLA and ADA leave separately
- Communicate both FMLA designation and ADA accommodation status in writing
- Do not assume FMLA designation satisfies ADA interactive process obligation

#### 9B: Pregnant Workers Fairness Act (PWFA) Intersection

**Coverage**: 42 U.S.C. § 2605 et seq. (effective June 27, 2023); 29 C.F.R. Part 1636.
Applies to employers with 15+ employees.

**"Known limitation" standard** — lower threshold than ADA:

- Physical or mental condition related to, affected by, or arising out of pregnancy,
  childbirth, or related medical conditions
- Need NOT substantially limit a major life activity
- Can be modest, minor, or episodic
- Becomes "known" when employee or representative communicates it to employer

**Interactive process and undue hardship**: Same four-factor analysis as ADA (42 U.S.C.
§ 12111(10)); "significant difficulty or expense" standard.

**Key distinctions from ADA:**

- Lower eligibility threshold (no "substantial limitation" required)
- Specific to pregnancy/childbirth/related conditions
- Cannot require employee to take leave if another accommodation would work (29 C.F.R. § 1636.3(l))
- EEOC regulations (June 18, 2024) provide extensive guidance

**When PWFA and ADA both apply:**

- Provide whichever protection is more favorable to the employee
- PWFA's lower threshold may cover pregnancy-related conditions the ADA would not
- Interactive process requirements are similar; use combined workflow

#### 9C: State Disability Law Overlay

Assess applicable state law(s) based on employee's work location and employer's footprint.

| State             | Law                              | Key Expansions vs. ADA                                                                                                                                                           |
| ----------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **California**    | FEHA (Gov. Code §§ 12940–12951)  | 5+ employees; disability "limits" (not "substantially limits"); affirmative accommodation duty without request if employer aware; no cap on emotional distress; DFEH enforcement |
| **New York**      | NYSHRL (Exec. Law § 290 et seq.) | 4+ employees; broad disability definition; temporary/episodic conditions explicitly covered; 2019 amendments expanded protections                                                |
| **New Jersey**    | LAD (N.J.S.A. 10:5-1 et seq.)    | Very broad coverage; strong employee protections; treble damages in some circumstances                                                                                           |
| **Massachusetts** | Chapter 151B                     | 6+ employees for disability; strong interactive process duties; MCAD enforcement                                                                                                 |
| **Washington**    | WLAD (RCW 49.60)                 | 8+ employees; "disability" broadly defined; aggressive AG enforcement                                                                                                            |

**[JURISDICTION-SPECIFIC]** For any state not listed, research whether:

- Employee threshold differs from ADA's 15 (most states are lower)
- "Disability" definition is broader than ADA
- Damages are uncapped or exceed ADA's per-employee statutory caps
- State administrative exhaustion requirements apply before filing suit
- State-specific affirmative accommodation duties exist beyond the federal floor

---

### Step 10: Quality Verification

Before delivering output, run the following checks silently. Revise before delivery if any
check fails.

**Completeness check:**

- [ ] Disability determination analyzed under all three ADAAA prongs
- [ ] Essential functions identified and analyzed
- [ ] Interactive process assessed (both employer and employee conduct)
- [ ] All viable accommodation options identified
- [ ] Undue hardship defense analyzed if raised or relevant
- [ ] Direct threat defense analyzed if raised or relevant
- [ ] FMLA intersection analyzed if leave is involved
- [ ] PWFA applicability assessed if pregnancy-related condition
- [ ] State law overlay assessed for identified state(s)
- [ ] All findings classified using four-tier system
- [ ] Actionable remediation steps provided for each finding
- [ ] Citation Quality Gates run (see below)
- [ ] Self-Interrogation run for CRITICAL DEFICIENCY items (see below)
- [ ] Glass Box audit trail completed

**Citation check:**

- Every legal claim cites specific statutory section, regulation, or EEOC guidance
- No jurisdiction-specific concepts stated as universal
- All references marked [VERIFY] if unverified against current authority

---

## Accommodation Classification System

Apply this four-tier system to each finding. Document the classification with supporting
reasoning.

### COMPLIANT

**Standard**: Interactive process properly conducted; accommodation analysis legally sound;
documentation adequate; risk of successful EEOC charge or litigation is low.

**Indicators:**

- Prompt, good-faith response to accommodation request
- Medical documentation requested appropriately (functional limitations, not diagnosis)
- Multiple accommodation options considered collaboratively
- Accommodation provided or denial supported by documented undue hardship or direct threat
  with objective evidence
- State law compliance verified
- Contemporaneous records maintained throughout
- FMLA/PWFA intersections addressed if applicable

**Action**: Note for awareness; confirm documentation retention schedule; schedule follow-up
to assess accommodation effectiveness.

---

### PARTIAL

**Standard**: Process initiated but with material gaps that create elevated EEOC charge risk
or litigation exposure. Remediation required within 30–90 days.

**Indicators:**

- Interactive process begun but delayed, incomplete, or inadequately documented
- Medical information request too broad (seeking diagnosis rather than functional limitations)
- Limited accommodation options considered without explaining why alternatives were rejected
- Undue hardship asserted without documented cost analysis relative to employer's resources
- State law requirements partially met but gaps exist
- FMLA running concurrently but ADA interactive process not separately documented
- Accommodation provided but no monitoring plan or follow-up scheduled

**Action**: Specific gap-by-gap remediation with responsible owner and deadline (30–90 days).
Flag for HR/legal review before any adverse employment action.

---

### NON-COMPLIANT

**Standard**: Material failure to meet ADA interactive process or accommodation obligations.
Elevated EEOC charge and litigation exposure. Remediation required immediately.

**Indicators:**

- Accommodation request received but no interactive process initiated
- Accommodation summarily denied without dialogue
- Undue hardship asserted without any documented analysis or objective evidence
- Medical documentation demand was overly broad or used for discriminatory purpose
- Accommodation denied based on coworker impact, morale, or other irrelevant factors
- Marginal functions cited as essential to deny accommodation without analysis
- Return-to-work blocked without individualized assessment
- Job description treated as determinative without examining actual practice

**Action**: Immediate remediation before any further adverse action. Engage employment
counsel. Reopen interactive process. Document good-faith corrective efforts.

---

### CRITICAL DEFICIENCY

**Standard**: Credible evidence of per se ADA violation, or accommodation failures so
fundamental that they constitute willful disregard. Maximum litigation exposure. Immediate
escalation required.

**Indicators:**

- Employee terminated during or immediately after accommodation request (temporal proximity
  creates strong inference of ADA violation)
- Retaliation for filing EEOC charge or requesting accommodation
- Blanket policy refusing accommodation for a disability category (per se violation)
- Medical examination or inquiry conducted outside ADA's permitted scope (post-offer/pre-
  employment rules violated)
- Direct threat assessment based entirely on stereotypes or without individualized analysis
- Disability-motivated termination during interactive process without undue hardship
  justification
- Prior EEOC charge or consent decree addressing same conduct (potential for enhanced remedies)

**Action**: Engage employment counsel immediately. Preserve all communications and records.
Assess litigation reserve. Evaluate voluntary accommodation/settlement options before
escalation. Self-Interrogation required (see below).

---

## Actionable Output Per Finding

For each classified finding, provide:

```
**Finding #[N]**
Domain: [Disability Determination | Essential Functions | Interactive Process |
         Accommodation Options | Undue Hardship | Direct Threat | FMLA/PWFA | State Law]
Classification: [COMPLIANT | PARTIAL | NON-COMPLIANT | CRITICAL DEFICIENCY]
Finding: [One-sentence description of what was found]
Risk: [Specific ADA exposure — statute/regulation/EEOC guidance violated; EEOC
      charge probability and litigation exposure if not remediated]
Evidence: [Specific facts, documents, or conduct supporting classification]
Remediation: [Specific corrective action required]
Owner: [HR Manager | Employment Counsel | CHRO | C-Suite | Legal/Compliance]
Deadline: [IMMEDIATE (48 hours) | URGENT (7 days) | 30 DAYS | 90 DAYS]
State Law Note: [Any heightened obligation under applicable state law]
Confidence: [Definite | High | Probable | Possible | Unlikely]
```

---

## Prioritization Framework

**Tier 1 — Immediate/Critical (CRITICAL DEFICIENCY)**
Act before any further adverse employment action. Engage employment counsel.

- Employee termination during interactive process without completion
- Retaliation for accommodation request or EEOC charge
- Blanket categorical denial without individualized assessment
- Direct threat claim based on stereotypes, not objective medical evidence
- Any situation with pending or threatened litigation or EEOC charge

**Tier 2 — Urgent/Material (NON-COMPLIANT)**
Remediate within 7–30 days. HR and legal review required before further action.

- Interactive process never initiated for clear accommodation request
- Accommodation denied without documented analysis
- Undue hardship asserted without factual foundation
- FMLA exhaustion used as automatic ADA termination basis

**Tier 3 — Important/Ongoing (PARTIAL)**
Remediate within 30–90 days. Process improvement and documentation cleanup.

- Interactive process documentation incomplete
- Accommodation options not fully explored
- State law compliance gaps
- FMLA/ADA concurrent tracking not established
- No monitoring plan for accommodation effectiveness

**Tier 4 — Best Practice (COMPLIANT with improvements)**
Recommended enhancements without immediate legal risk.

- Accommodation effectiveness review schedule
- Updated written accommodation procedure
- Supervisor training on recognizing accommodation requests
- Job description review to ensure accuracy of essential functions

---

## Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                    | Fail Action                                              |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statutory section, EEOC regulation, or established guidance document                                 | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow consistent, recognizable format (e.g., 42 U.S.C. § 12102; 29 C.F.R. § 1630.2(n))                                   | Fix format                                               |
| **Currency**   | EEOC guidance, state law statutes, and employee thresholds checked for recent amendments; PWFA regulations effective June 2024          | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within ADA Title I scope; no Title II/III concepts bleed in; state law differences clearly labeled as state-specific     | Remove or flag domain bleed                              |
| **Confidence** | Uncertainty explicitly stated, not hidden; developing areas (e.g., remote work case law, PWFA enforcement patterns) flagged as evolving | Add confidence qualifier                                 |

---

## Self-Interrogation for CRITICAL DEFICIENCY Items

For any finding classified as CRITICAL DEFICIENCY, apply this 3-pass review before delivery:

**Pass 1 — Legal Chain Integrity**

- Does the CRITICAL DEFICIENCY classification follow logically from the cited statutory
  or regulatory authority?
- Would an EEOC investigator or federal judge actually reach this conclusion on these facts?
- What is the employer's strongest counter-argument?

**Pass 2 — Completeness**

- Have all relevant EEOC guidance documents been considered?
- Is there applicable case law in the controlling circuit that affects the analysis?
- Are there PWFA or state law dimensions not yet addressed?
- Has the direct threat defense been evaluated if safety is at issue?

**Pass 3 — Challenge**

- What is the strongest argument that employer conduct was compliant?
- Under what circumstances might a court find the employer's actions reasonable?
- Is the CRITICAL DEFICIENCY classification proportionate, or is this actually NON-COMPLIANT
  with mitigating circumstances?

If any pass reveals a weakness, revise the analysis before delivery. Record result in
Glass Box: `self_interrogation: PASS` or `self_interrogation: REVISED`.

---

## Confidence Scoring

Assign a confidence level to each material finding.

| Level        | Range     | Meaning                                                             | Action                                                |
| ------------ | --------- | ------------------------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled EEOC guidance, clear statutory text, unambiguous regulation | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong authority; minor interpretation questions or circuit splits  | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments; developing case law (e.g., remote work post-COVID)  | State with reasoning and contra-indicators            |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing authorities; novel fact pattern      | Flag for employment counsel review with both sides    |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative; no clear precedent                         | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

**Areas currently at Probable or lower confidence (as of 2026-03-21):**

- Remote work as reasonable accommodation: actively developing case law; circuit-by-circuit variation
- PWFA enforcement patterns: regulations effective June 2024; limited EEOC enforcement precedent
- AI/algorithmic accommodations: no settled ADA guidance on AI tool accommodations
- Long COVID as disability: EEOC guidance exists (July 2021) but case law still developing

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-us-ada-accommodation"
  situation: "[Brief description of accommodation situation analyzed]"
  analysis_type: "[Active request | Denial review | Interactive process audit | EEOC defense | Compliance audit]"
  employee_role: "[Position title]"
  employer_size: "[Number of employees — determines ADA threshold and state law applicability]"
  applicable_law:
    federal: "ADA Title I, ADAAA, 29 C.F.R. Part 1630"
    pwfa_applicable: "[Yes / No — pregnancy-related condition?]"
    fmla_applicable: "[Yes / No — leave involved?]"
    state_law: "[State and applicable statute, or 'None identified']"
  disability_prong_analyzed: "[Prong 1 (Actual) | Prong 2 (Record) | Prong 3 (Regarded As) | Multiple]"
  essential_functions_contested: "[Yes / No]"
  interactive_process_status: "[Not initiated | In progress | Complete | Broken by employer | Broken by employee]"
  accommodations_considered: "[List of options evaluated]"
  defenses_raised: "[Undue hardship | Direct threat | Both | None]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "42 U.S.C. § 12102 (disability definition) — [VERIFIED/UNVERIFIED]"
    - "42 U.S.C. § 12111(9) (reasonable accommodation) — [VERIFIED/UNVERIFIED]"
    - "42 U.S.C. § 12111(10) (undue hardship) — [VERIFIED/UNVERIFIED]"
    - "42 U.S.C. § 12113(b) (direct threat) — [VERIFIED/UNVERIFIED]"
    - "29 C.F.R. § 1630.2(n) (essential functions) — [VERIFIED/UNVERIFIED]"
    - "[Additional statutes as applicable]"
  eeoc_guidance_consulted:
    - "Enforcement Guidance on Reasonable Accommodation and Undue Hardship (Oct. 2002) — [VERIFIED/UNVERIFIED]"
    - "[Additional EEOC guidance as applicable]"
  case_law_consulted:
    - "[Case name, citation, key holding — VERIFIED/UNVERIFIED]"
  findings_summary:
    critical_deficiency: "[number]"
    non_compliant: "[number]"
    partial: "[number]"
    compliant: "[number]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL DEFICIENCY items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats about the analysis]"
  reviewer: "AI-assisted — requires review by qualified employment attorney before reliance"
```

---

## Anti-Patterns

What NOT to do in ADA accommodation analysis and HR practice. These represent the most
common errors that generate EEOC charges and adverse judgments.

1. **Treating the written job description as gospel.** Job descriptions are evidence of
   essential functions, not determinative. Courts look at actual practice, time spent,
   and consequences of non-performance. Descriptions written to exclude accommodations
   after the fact are particularly suspect.

2. **Demanding a diagnosis rather than functional limitations.** The ADA permits employers
   to request information about how the condition limits the employee's ability to perform
   essential functions — not the specific diagnosis, prognosis, or medical details beyond
   what is necessary. Overly broad medical inquiries violate the ADA's medical confidentiality
   provisions.

3. **Terminating an employee during the interactive process.** Termination while the
   interactive process is open — even for legitimate performance reasons — creates a strong
   inference of ADA violation (temporal proximity). Complete the process or pause the
   disciplinary action until accommodation analysis is complete.

4. **Asserting undue hardship based on coworker resentment.** Employee morale,
   perceptions of unfairness, or resentment from colleagues who are not disabled is
   legally irrelevant to the undue hardship analysis. Courts have uniformly rejected this
   rationale.

5. **Using FMLA exhaustion as automatic ADA termination authority.** Exhausting 12 weeks
   of FMLA leave does not end the ADA accommodation obligation. The employer must separately
   assess whether additional leave is a reasonable accommodation before terminating.

6. **Demanding cure or full recovery as a condition of return.** Requiring an employee to
   be "100% healed" before returning is a per se violation. The ADA protects the right to
   work with disability and with reasonable accommodation.

7. **Blanket "no telework" policies after COVID.** Prior successful telework — including
   temporary pandemic-era arrangements — is probative evidence that essential functions
   can be performed remotely. Blanket refusal of post-pandemic remote work accommodation
   requests without individualized analysis creates significant exposure.

8. **Conflating direct threat with mere risk.** Direct threat requires a significant risk
   of substantial harm based on objective, individualized, medical evidence. A general
   concern about safety or a categorical assumption about a disability is not a direct
   threat defense — it is a per se violation.

9. **Ignoring the "regarded as" prong's accommodation limitation.** Employees who are
   solely "regarded as" having a disability (Prong 3) are NOT entitled to reasonable
   accommodation — but ARE protected from discrimination. Confusing these is a common
   analytical error that cuts both ways.

10. **Stopping the interactive process after one failed accommodation.** The interactive
    process continues until an effective accommodation is found or genuine undue hardship
    is proven. Abandoning the process because the first attempt did not work constitutes
    a process failure.

11. **Not separately tracking ADA and FMLA leave.** Running leave concurrently without
    separately documenting ADA accommodation analysis creates ambiguity about whether the
    employer met its independent ADA obligations.

12. **Ignoring state law when the employer has fewer than 15 employees.** ADA Title I
    does not apply below 15 employees — but California FEHA applies at 5, New York NYSHRL
    at 4, and New Jersey LAD covers even smaller employers. Federal ADA non-coverage does
    not mean state law non-coverage.

13. **Requesting medical documentation for obvious conditions.** When a disability is
    obvious (e.g., employee uses a wheelchair), requesting medical documentation to
    confirm the disability condition is unnecessary and may itself be an ADA violation.
    Only request documentation for limitations that are not obvious or already documented.

14. **Assuming an accommodation is unreasonable without analysis.** Dismissing an
    accommodation request as "unreasonable" without exploring the option, consulting
    resources like the Job Accommodation Network (JAN), or conducting an individualized
    assessment is independent grounds for ADA liability.

15. **Failing to document the interactive process contemporaneously.** Reconstruction
    of the interactive process after an EEOC charge is filed is far less credible than
    contemporaneous records. Every step — request received, meetings held, medical
    documentation requested and received, options discussed, decisions made — should be
    documented in real time.

16. **Applying PWFA's higher ADA threshold to pregnancy-related conditions.** The PWFA
    requires accommodation for "known limitations" — a much lower threshold than ADA's
    "substantially limits." Analyzing a pregnant worker's accommodation request under the
    ADA standard alone, when PWFA applies, will result in denial of legally required
    accommodations.

17. **Failing to provide accommodations during the interactive process itself.** While
    the interactive process is ongoing, the employer should consider providing temporary
    accommodations. Denying all support during the process — particularly when the process
    is extended — can itself constitute an ADA violation.

---

## Writing Standards

Apply these standards to all output:

**For HR/management communications** (accommodation decision letters, interactive process
documentation):

- Plain language; avoid legal jargon in communications directed at employees
- Active voice: "We have reviewed your request" not "Your request has been reviewed"
- Specific: name the accommodation requested, the analysis conducted, the decision reached,
  and the reason (if denying)
- Do not disclose specific medical information to supervisors — communicate the nature
  of the accommodation needed, not the diagnosis

**For legal analysis and internal memoranda:**

- Precise statutory and regulatory citations
- Confidence qualifiers where legal certainty is less than High
- Distinguish established EEOC guidance from developing case law
- Glass Box audit trail appended

**Quality gates before delivery:**

1. Can an HR manager who is not an employment attorney understand the key findings?
2. Is every ADA violation or risk claim backed by a specific statutory/regulatory/
   guidance citation, or flagged [VERIFY]?
3. Are any findings vague or conclusory? If yes, revise with specific evidence and analysis.
4. Does any finding bleed state law concepts into federal analysis without clearly labeling
   them as state-specific?
5. Would a plaintiff's employment attorney find obvious gaps in this analysis?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 3, search for current text of ADA Title I provisions, EEOC regulations (29 C.F.R.
  Part 1630), PWFA regulations (29 C.F.R. Part 1636), and applicable state statutes
- Search for EEOC enforcement guidance documents (October 2002 accommodation guidance;
  May 2016 leave guidance; COVID-related guidance)
- Search for controlling circuit case law on the specific accommodation type at issue
- Mark all legalcode-mcp-verified citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Proceed using the legal framework in this skill
- Mark all statutory, regulatory, and case law citations with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Strongly recommend independent verification before relying on any specific citation
  for decision-making or litigation purposes

**Job Accommodation Network (JAN):**

- JAN (askjan.org) is the premier free resource for identifying specific accommodation
  options by disability type and job category
- Reference JAN's accommodation ideas database when exploring options in Step 7
- JAN guidance is not legally binding but is persuasive evidence of accommodation feasibility
  in EEOC proceedings

**Related skills for cross-referencing:**

- `legalcode-us-state-non-compete-analysis`: For CA FEHA non-compete intersection
- `legalcode-workplace-investigation`: If ADA retaliation claim involves investigation
- For ERISA/benefits intersection with disability: benefits-specific compliance skills

---

## Output Format Template

```markdown
## ADA Accommodation Analysis

**Date**: [date]
**Situation**: [Brief description]
**Employee Role**: [Position]
**Employer Size**: [Employee count and ADA coverage determination]
**Applicable Law**: [Federal ADA Title I + ADAAA] [+ PWFA if applicable] [+ State law if applicable]
**Analysis Basis**: [Active request | Denial review | Audit | EEOC defense]
**Prepared by**: AI-assisted — requires qualified employment attorney review

---

## Executive Summary

[2–4 sentence summary of key findings, highest-severity classification, and priority action]

---

## Key Findings Table

| #   | Domain   | Classification                                              | Finding            | Deadline                     |
| --- | -------- | ----------------------------------------------------------- | ------------------ | ---------------------------- |
| 1   | [Domain] | [CRITICAL DEFICIENCY / NON-COMPLIANT / PARTIAL / COMPLIANT] | [One-line finding] | [IMMEDIATE / 7d / 30d / 90d] |
| ... |          |                                                             |                    |                              |

---

## Disability Determination Analysis

**Prong 1 (Actual Disability)**: [Analysis — impairment, major life activity, substantially
limits without mitigating measures, episodic/in-remission if applicable]
**Classification**: [COMPLIANT | PARTIAL | NON-COMPLIANT | CRITICAL DEFICIENCY]

**Prong 2 (Record of Disability)**: [Analysis — prior diagnosis or history if at issue]
**Classification**: [as applicable]

**Prong 3 (Regarded As)**: [Analysis — employer's perception and adverse action if at issue;
note accommodation limitation]
**Classification**: [as applicable]

---

## Essential Functions Analysis

**Essential functions identified**: [List]
**Contested functions**: [List with analysis of whether essential or marginal]
**Accommodation impact**: [Which functions at issue; how accommodation would affect performance]
**Classification**: [COMPLIANT | PARTIAL | NON-COMPLIANT | CRITICAL DEFICIENCY]

---

## Interactive Process Assessment

**Timeline**: [Key dates — request, response, meetings, documentation]
**Employer conduct**: [Specific findings on good-faith engagement]
**Employee conduct**: [Specific findings on participation]
**Process status**: [Complete / Incomplete / Broken]
**Classification**: [COMPLIANT | PARTIAL | NON-COMPLIANT | CRITICAL DEFICIENCY]

---

## Accommodation Options Analysis

**Options considered**: [List with description]
**Preferred by employee**: [Employee's stated preference]
**Employer's assessment**: [Effective / Undue hardship / Other]
**Accommodation provided/proposed**: [Description]
**Monitoring plan**: [Follow-up schedule for effectiveness assessment]
**Classification**: [COMPLIANT | PARTIAL | NON-COMPLIANT | CRITICAL DEFICIENCY]

---

## Defense Analysis

### Undue Hardship

**Raised**: [Yes / No]
**Four-factor analysis**: [Cost, facility resources, entity resources, operation type]
**Tax credits available**: [Disabled Access Credit, WOTC if applicable]
**Conclusion**: [Supported by objective evidence / Not supported]
**Classification**: [COMPLIANT | NON-COMPLIANT | CRITICAL DEFICIENCY | N/A]

### Direct Threat

**Raised**: [Yes / No]
**Four-factor objective assessment**: [Nature, duration, severity/probability, imminence]
**Medical evidence basis**: [Objective and individualized / Stereotype-based]
**Accommodation eliminating risk**: [Available / Not available]
**Classification**: [COMPLIANT | NON-COMPLIANT | CRITICAL DEFICIENCY | N/A]

---

## Intersecting Obligations

### FMLA

[Leave tracking, concurrent designation, post-exhaustion ADA obligations]

### PWFA

[Applicable / Not applicable; known limitation analysis if applicable]

### State Law ([State])

[Applicable differences from federal ADA; heightened obligations; remedies]

---

## Priority Remediation Roadmap

**Tier 1 — Immediate (CRITICAL DEFICIENCY):**

- [Action] — Owner: [Role] — Deadline: IMMEDIATE

**Tier 2 — Urgent (NON-COMPLIANT):**

- [Action] — Owner: [Role] — Deadline: [7 / 30 days]

**Tier 3 — Important (PARTIAL):**

- [Action] — Owner: [Role] — Deadline: [30 / 90 days]

**Tier 4 — Best Practice (COMPLIANT enhancements):**

- [Action] — Owner: [Role] — Deadline: [Ongoing / Next review cycle]

---

## Glass Box Audit Trail

[Complete YAML block per Glass Box section]
```

---

## Localization Notes

**Using this skill for state-law-only analysis (employer below 15-employee ADA threshold):**

Apply this skill's framework but substitute the applicable state statute and definitions:

- California FEHA: Use "limits" (not "substantially limits") for disability determination;
  apply 5-employee threshold; note affirmative accommodation duty
- New York NYSHRL: 4-employee threshold; broad coverage including temporary/episodic conditions;
  New York City HRL (4 or fewer employees) provides even broader protection
- For any state law analysis: mark state-specific conclusions distinctly from federal analysis
  and verify current state statute text

**Multi-state employers:**

- Apply the law of the state where the employee works (lex loci principle)
- If employee works remotely across multiple states, analyze the state with the strongest
  connection to the employment relationship
- Note that some state laws apply extraterritorially (e.g., California FEHA can apply to
  California-based employees working remotely)

---

## Provenance

Legalcode original synthesis (2026-03-21). Created using the Legalcode 2-agent research
pipeline: structural analysis of `legalcode-contract-review` and `legalcode-us-fcpa-compliance`
reference standards combined with deep legal research on ADA Title I (42 U.S.C. § 12101
et seq.), ADAAA (effective 2009), 29 C.F.R. Part 1630, EEOC Enforcement Guidance on
Reasonable Accommodation (Oct. 2002), PWFA (42 U.S.C. § 2605, effective June 27, 2023),
FMLA intersection guidance, Chevron U.S.A. v. Echazabal 536 U.S. 73 (2002), US Airways
v. Barnett 535 U.S. 122 (2002), Bodie-Jernigan v. School Board of Broward County (11th
Cir. Sept. 2025), and state law overlay research covering CA FEHA, NY NYSHRL, NJ LAD,
MA Chapter 151B, and WA WLAD. Quality frameworks (Citation Quality Gates, Self-Interrogation,
Confidence Scoring, Glass Box Audit Trail) adapted from `legalcode-contract-review` gold
standard. Classification system (COMPLIANT/PARTIAL/NON-COMPLIANT/CRITICAL DEFICIENCY)
adapted from `legalcode-us-fcpa-compliance` compliance-domain pattern.
