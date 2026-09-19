---
name: legalcode-expert-witness-preparation
description: Prepare expert witnesses and manage expert evidence strategy across all phases of litigation.
  Use when retaining, qualifying, preparing, or challenging expert witnesses in civil litigation; when
  reviewing expert reports for Daubert or CPR 35 compliance; when building cross-examination plans for
  opposing experts; or when deciding whether to retain a rebuttal expert.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Prepare expert witnesses and manage expert evidence strategy across all phases of litigation. Covers Daubert/Frye qualification screening, FRE 702 (2023 amendment) admissibility gating, FRCP 26(a)(2)(B) written report compliance, FRCP 26(b)(4) work-product protections, cross-examination vulnerability mapping, deposition preparation, rebuttal expert strategy, and conflicts identification for US federal and state court. Also covers UK CPR Part 35 expert duties, Practice Direction 35 report requirements, Single Joint Expert procedures, and hot-tubbing / concurrent evidence protocols. Use when retaining, qualifying, preparing, or challenging expert witnesses in civil litigation; when reviewing expert reports for Daubert or CPR 35 compliance; when building cross-examination plans for opposing experts; or when deciding whether to retain a rebuttal expert. Triggers on phrases like "expert witness", "Daubert motion", "Frye standard", "FRE 702", "FRCP 26(a)(2)", "CPR 35", "expert report review", "expert deposition prep", "single joint expert", "cross-examination expert", "rebuttal expert", "expert conflicts", or any task requiring qualification, preparation, or challenge of expert testimony.


# Legalcode Expert Witness Preparation

> **Disclaimer**: This skill provides a framework for AI-assisted expert witness strategy
> and preparation. It does not constitute legal advice. All outputs must be reviewed by
> qualified litigation counsel licensed in the relevant jurisdiction before use.
> Procedural rules, local rules, and standing orders vary by court and judge; verify
> applicable rules before relying on any guidance here. Statutory, regulatory, and
> case-law references cited from memory carry hallucination risk — verify against
> authoritative sources before relying on them. Expert witness strategy has tactical,
> ethical, and professional-responsibility dimensions that require experienced litigation
> counsel judgment.

## Purpose and Scope

This skill covers the full lifecycle of expert evidence in civil litigation — from initial
expert screening through qualification, report preparation, deposition readiness,
cross-examination vulnerability analysis, and rebuttal strategy. It applies to both sides:
the **retaining party** (qualifying, preparing, and protecting your expert) and the
**challenging party** (identifying weaknesses in the opposing expert and mounting Daubert
or CPR 35 exclusion arguments).

**Covers:**

- Expert qualification screening against Daubert, Frye, and Kumho Tire standards (US)
- FRE 702 (as amended December 1, 2023) admissibility gating
- FRCP 26(a)(2)(A)–(D) disclosure requirements and timing
- FRCP 26(a)(2)(B) written report content compliance (all 6 required elements)
- Distinction between retained experts (26(a)(2)(B) reports) and non-retained experts
  (26(a)(2)(C) disclosure only)
- FRCP 26(b)(4) work-product protections for draft reports and expert–attorney
  communications (with the three statutory exceptions)
- Cross-examination vulnerability mapping across 8 attack categories
- Deposition preparation: direct examination outline, anticipated cross sequences,
  learned treatise exposure, and "hired gun" attack preparation
- Rebuttal expert strategy: disclosure timing (FRCP 26(a)(2)(D)), scope constraints,
  and tactical deployment
- Conflicts of interest identification: financial, testimonial, and relational conflicts
- UK CPR Part 35 and Practice Direction 35: overriding duty to court, report content
  requirements, questions to experts
- Single Joint Expert (SJE) procedures under CPR 35.7–35.8
- Concurrent evidence / hot-tubbing under CPR 35.12

**Does not:**

- Provide expert testimony or substantive opinions in any technical field
- Cover criminal cases, grand jury proceedings, or post-conviction expert challenges
- Draft expert reports (the expert drafts; this skill structures the preparation process)
- Cover international arbitration expert procedures in full depth (ICSID, IBA Rules on
  the Taking of Evidence) — use the arbitration skills for those contexts
- Replace experienced litigators' strategic judgment on whether to retain, challenge,
  or defer on expert evidence

**Related skills:** `legalcode-deposition-preparation` (fact witness and full deposition
preparation), `legalcode-evidence-admissibility-analysis` (FRE admissibility screening),
`legalcode-early-case-assessment` (case strategy and exposure modeling),
`legalcode-brief-analyzer` (Daubert exclusion motions and oppositions),
`legalcode-litigation-risk-assessment` (overall case risk framework)

---

## Jurisdiction and Governing Law

This skill covers two primary jurisdictions:

**US Federal (Primary)**: Calibrated to the Federal Rules of Civil Procedure (FRCP) and
Federal Rules of Evidence (FRE) as amended through 2023. Applies directly to US district
court practice and to federal agency adjudications with analogous expert rules. State
court coverage uses [JURISDICTION-SPECIFIC] markers.

**England and Wales (Secondary)**: Calibrated to CPR Part 35 and Practice Direction 35,
with the Ikarian Reefer principles and Kennedy v Cordia [2016] UKSC 6. References to
"UK" in this skill mean England and Wales unless stated otherwise.

[JURISDICTION-SPECIFIC] **State court variations (US)**: Many states have adopted
Daubert, but a significant minority still apply Frye. Verify the applicable standard
before advising on qualification strategy:

- **Daubert states**: Most federal circuits and the majority of states (including TX, FL
  since _DeLisle v. Crane Co._ (2018), OH, CO, MI) [VERIFY]
- **Frye states**: California (Kelly/Frye, Cal. Evid. Code precedent), Illinois
  (_Donaldson v. Central Illinois_), New York (Frye applies to "novel scientific
  evidence"), Pennsylvania, Minnesota, Maryland (_Reed v. State_), Washington [VERIFY]
- **Hybrid/modified**: New York applies Daubert to non-novel science but Frye for novel
  techniques; New Jersey applies a modified Frye/Daubert hybrid (_State v. Harvey_)
  [VERIFY]; verify current state law before advising — approximately 27 states have
  adopted some form of Daubert but only about 9 without modification [VERIFY]
- **Practical significance**: In Frye states, admission of a novel scientific technique
  requires demonstration of community-wide professional acceptance, typically through
  testimony from multiple field experts. In Daubert states, the proponent instead
  demonstrates reliability through the flexible multi-factor analysis, which may allow
  admission of a methodology not yet achieving general acceptance if otherwise reliable.

[JURISDICTION-SPECIFIC] **Scotland, Northern Ireland, Australia, Canada**: Expert witness
obligations differ. This skill does not cover those jurisdictions in depth. Use
[VERIFY] markers when applying principles outside England & Wales or US federal practice.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming context, the workflow pauses with **⟁ CLARIFY** prompts when:

- The answer would change the direction of the analysis
- Multiple valid strategic approaches exist
- Jurisdiction-specific rules require confirmation before proceeding
- The tactical context (retaining vs. challenging side) determines which analysis applies

Use the structured-options format at each CLARIFY point. If the user has already
provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept the Input

Accept the engagement in any of these forms:

- **Expert CV / curriculum vitae**: For qualification screening and conflict checking
- **Draft expert report**: For 26(a)(2)(B) / CPR 35 compliance review
- **Opposing expert report**: For cross-examination vulnerability mapping
- **Case summary or complaint**: For identifying expert needs and strategy
- **Deposition transcript (prior testimony)**: For impeachment analysis

If the user provides none of these but describes a case or expert situation, proceed to
Step 2 to gather context.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user these questions (skip any already answered):

1. **Which side are you on?**
   - Options: Retaining party (preparing your own expert), Challenging party (opposing
     their expert), Both (dual analysis — you have your expert and need to anticipate
     opposing attack), Neutral (court-appointed or SJE context)
   - _Why this matters_: The entire analysis flips. Retaining side maximizes qualification
     and report strength; challenging side identifies exclusion arguments.

2. **Jurisdiction and court?**
   - Options: US federal court (specify district/circuit), US state court (specify state),
     England and Wales (CPR 35), Other (describe)
   - _Why this matters_: Determines whether Daubert, Frye, or CPR 35 applies, and which
     procedural timeline governs.

3. **Expert type?**
   - Options: Scientific/medical (pathology, toxicology, pharmacology), Engineering /
     technical (accident reconstruction, product design, structural), Financial / economic
     (lost profits, valuation, damages), Industry practice (standard of care, customs),
     Other (describe)
   - _Why this matters_: Daubert analysis differs for scientific vs. non-scientific
     experts (post-Kumho Tire); CPR 35 applies uniformly but the admissibility risk
     profile differs by field.

4. **Phase of the engagement?**
   - Options: Pre-retention screening, Report review / preparation, Deposition preparation,
     Motion practice (Daubert or CPR 35 challenge), Trial preparation, Post-deposition
     assessment
   - _Why this matters_: Determines which workflow modules to activate and what deliverables
     to produce.

5. **Litigation context?**
   - Free text. Prompt with examples: case type, claims at issue, key factual disputes,
     trial date, existing expert disclosures from the other side.
   - _Why this matters_: Expert strategy is case-specific. A damages expert in a patent
     case faces different Daubert exposure than a causation expert in a pharmaceutical
     mass tort.

If the user provides partial context, proceed with stated assumptions and flag them
explicitly.

### Step 3: Load Legal Authority

Identify the applicable rules and gather legal authority for the specific court and judge.

**Use legalcode-mcp** to research:

- The specific judge's Daubert / FRE 702 jurisprudence (judge-level pattern analysis)
- Circuit-level FRE 702 interpretive trends (some circuits are notably stricter post-2023)
- State-specific Frye / Daubert case law if in state court
- CPR Part 35 recent practice directions or Chancery/TCC practice notes if in UK court
- Recent exclusion decisions in the same expert's field

**Save results** to `/tmp/legalcode-expert-research.md` with structure:

```markdown
# Expert Witness Legal Authority Reference

## Court: [court name]

## Judge: [if known]

## Date: [date]

### Applicable Standard

- [Daubert / Frye / CPR 35 / other]

### FRE 702 / Rule Interpretation

- [Key holdings in this circuit or court]

### Judge-Level Patterns

- [Known Daubert rulings, preferences on expert scope, hot-button issues]

### Recent Field-Specific Exclusions

- [Cases excluding experts in this field, with grounds]
```

**If legalcode-mcp is not connected:**

- Proceed using the rule framework below
- Mark all case citations with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — manual verification required"`

**⟁ CLARIFY** — If the judge or district is provided, ask: "Do you want me to include a
judge-specific Daubert pattern analysis as part of this preparation? This requires
legalcode-mcp access and may take additional time, but is especially valuable for courts
with a well-documented track record of excluding experts in this field."

### Step 4: Expert Qualification Screening

Screen the expert's qualifications against the applicable admissibility standard.

**⟁ CLARIFY** — For this step, ask if not already provided:

- "Do you have the expert's CV / résumé? Please provide it for qualification analysis."
- "Has this expert been previously challenged or excluded in any case? If known, provide
  case names or details."

Run the **Qualification Screening Matrix** (see Qualification Framework below) and
produce a qualification risk score (STRONG / QUALIFIED / AT-RISK / EXCLUDABLE) for each
of the four Daubert prongs and the overall FRE 702 / CPR 35 standard.

Flag any red-flag factors requiring remediation before disclosure:

- Credentialing gaps (lacks degree, board certification, or field recognition)
- Prior exclusion rulings (check the expert's "prior cases testified" list)
- Financial conflicts (see Conflicts Framework below)
- Publication record issues (thin record, retracted publications, prior inconsistent
  published opinions)
- Methodology mismatches (expertise is in adjacent but distinct field)

### Step 5: Report Compliance Review

Review the draft expert report (if available) or prepare the report requirements
checklist for the expert.

**⟁ CLARIFY** — If a draft report is provided: "Should I review this report for
[FRCP 26(a)(2)(B)] compliance only, or also for cross-examination vulnerability? The
latter produces a more complete picture of how opposing counsel may attack the report,
but adds time."

Apply the **FRCP 26(a)(2)(B) Report Compliance Checklist** or the **CPR 35 / PD 35
Report Requirements Checklist** as applicable (see Report Requirements section below).

Classify each compliance element as:

- **COMPLIANT**: Element is present and adequate
- **PARTIAL**: Element is present but deficient (needs cure before disclosure)
- **NON-COMPLIANT**: Element is missing (must be added or sanctions risk arises)

For any NON-COMPLIANT item involving compensation, prior testimony, or the completeness
of opinions, flag as **CRITICAL** — these are the most-litigated exclusion grounds.

### Step 6: Cross-Examination Vulnerability Mapping

Map the opposing expert's report (or your own expert's draft) against the 8 standard
attack vectors (see Cross-Examination Vulnerability section below).

**⟁ CLARIFY** — "Is this analysis for your own expert (to prepare defenses) or for an
opposing expert (to develop the cross-examination)? The deliverable differs: for your
expert, I produce a preparation memo; for an opposing expert, I produce a
cross-examination outline."

For each attack vector, assign a **STRENGTH** score for the attack:

- **HIGH**: Clear basis for challenge; likely to succeed in part
- **MEDIUM**: Arguable challenge; outcome depends on judge and supporting evidence
- **LOW**: Weak basis; unlikely to move the court

Prioritize HIGH-strength attacks for Daubert briefing or extended deposition sequences.
De-prioritize LOW-strength attacks to avoid diluting the cross.

### Step 7: Deposition Preparation

Prepare the expert for deposition testimony (retaining side) or prepare the
cross-examination outline (challenging side).

**For the retaining side** — prepare the expert on:

1. The three unprotected disclosure areas under FRCP 26(b)(4)(C): compensation paid,
   facts/data provided by counsel that the expert considered, and assumptions provided
   by counsel that the expert relied upon
2. "Hired gun" attacks and how to defuse them (prior work ratio, compensation size)
3. Learned treatise attacks under FRE 803(18): identify every treatise likely to be used
   against the expert's methodology
4. Scope discipline: experts must stay within the disclosed opinions; surprise opinions
   at trial risk exclusion under FRCP 37(c)(1)
5. Common cross-examination sequences in the expert's field

**For the challenging side** — produce:

1. Daubert foundation sequence: questions to establish or undermine the four Daubert
   prongs at deposition
2. Compensation and bias sequence: prior work for same retaining firm, hourly rate,
   proportion of income from litigation
3. Learned treatise sequence: establish the treatise as authoritative (or have the
   expert deny it), then deploy the inconsistency
4. Methodology challenge sequence: expose steps that deviate from the expert's published
   methodology or the field's accepted protocols
5. Prior testimony / prior publications inconsistency map

**⟁ CLARIFY** — "For deposition prep, what is the deposition format? Single-day / 7-hour
limit (FRCP 30(d)(1) default), extended by stipulation, or a CPR 35.6 written-questions
procedure? This affects the outline structure."

### Step 8: Rebuttal Expert Strategy

Evaluate whether to retain a rebuttal expert and, if so, define the scope.

Apply the **Rebuttal Decision Framework** (see Rebuttal Strategy section below):

- Is the opposing expert's testimony case-dispositive on any issue?
- Can the opposing expert be cross-examined to sufficient effect without a rebuttal expert?
- What is the FRCP 26(a)(2)(D) deadline for rebuttal disclosure (default: 30 days after
  initial disclosure unless modified by court order)?
- Does the proposed rebuttal expert's scope stay within "intended solely to contradict or
  rebut" the initial expert (the scope limitation courts enforce strictly)?

**⟁ CLARIFY** — "Has the court set specific rebuttal expert disclosure deadlines in the
scheduling order? If so, provide the date, as this constrains the decision timeline."

### Step 9: Conflicts Identification

Screen the expert for conflicts of interest that could damage credibility at trial or
require disclosure / disqualification.

Apply the **Conflicts Screening Matrix** (see Conflicts Framework below) across:

- Prior adverse testimony for the opposing party or same law firm
- Financial interest in the outcome (contingency arrangements, equity in plaintiff/
  defendant, prior consulting for opposing party)
- Prior published opinions inconsistent with the expert's retained opinions in this case
- Ethical rule violations (state bar rules on expert conduct; ABA Model Rule 3.4(b)
  on compensating experts beyond reasonable fee [VERIFY current jurisdiction])

Flag **DISQUALIFYING** conflicts (require withdrawal or renegotiation) separately from
**CREDIBILITY** conflicts (are disclosable and should be pre-empted in direct examination).

### Step 10: Quality Verification

Before delivering any output, run the quality checks defined in the Quality Assurance
Framework:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every EXCLUDABLE or CRITICAL classification, run the 3-pass Self-Interrogation.
3. Verify that all jurisdiction-specific rules are correctly flagged with
   [JURISDICTION-SPECIFIC] markers.
4. Confirm all procedural deadlines cited are keyed to the actual scheduling order or
   default rule (not assumed).
5. Generate the Glass Box Audit Trail and append it to the output.

---

## Qualification Framework

### Daubert Screening Matrix (US Federal / Daubert States)

Apply the four primary Daubert prongs from _Daubert v. Merrell Dow Pharmaceuticals, Inc._,
509 U.S. 579 (1993) [VERIFY], supplemented by _Kumho Tire Co. v. Carmichael_, 526 U.S.
137 (1999) [VERIFY] (extending gatekeeping to all expert testimony, not just scientific)
and _General Electric Co. v. Joiner_, 522 U.S. 136 (1997) [VERIFY] (abuse of discretion
review; fit between methodology and conclusions).

**FRE 702 (Amended December 1, 2023)** — as amended, the rule requires that the
**proponent demonstrates to the court that it is more likely than not** that:
(a) The expert's scientific, technical, or other specialized knowledge will help the trier
of fact to understand the evidence or determine a fact in issue;
(b) The testimony is based on sufficient facts or data;
(c) The testimony is the product of reliable principles and methods; and
(d) **The expert's opinion reflects a reliable application of the principles and methods
to the facts of the case.** [VERIFY]

**Two critical changes from the 2023 amendment:**

1. **Preponderance standard explicitly imposed.** The phrase "the proponent demonstrates
   to the court that it is more likely than not" was added. Many courts had incorrectly
   treated sufficiency of basis and application of methodology as "questions of weight and
   not admissibility." The 2023 amendment corrects this: under FRE 104(a), the court —
   not the jury — must find by a preponderance that all four elements are satisfied before
   the testimony is admitted. After admission, the jury weighs persuasive value. A trial
   court that admits expert testimony without making the preponderance finding commits legal
   error. When challenging expert testimony, explicitly invoke the preponderance standard
   and request express findings.

2. **Expert overstatement now expressly prohibited.** The Advisory Committee Notes
   specifically address forensic testimony: experts "should avoid assertions of absolute
   or one hundred percent certainty — or to a reasonable degree of scientific certainty —
   if the methodology is subjective and thus potentially subject to error." This directly
   targets documented problems with forensic disciplines (bite mark analysis, hair
   comparison, firearms toolmark analysis) where experts routinely claimed certainties
   their methods could not support. Post-amendment, an expert whose report asserts
   certainty beyond what the methodology supports faces exclusion on those grounds alone.

| Prong                         | Question                                                                                      | Strong (5)                                                   | At-Risk (2-3)                                            | Excludable (1)                                               |
| ----------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | -------------------------------------------------------- | ------------------------------------------------------------ |
| **Testing / Falsifiability**  | Can the theory/technique be tested? Has it been tested?                                       | Theory is testable; testing confirms reliability             | Theory testable but tested with mixed results            | Theory is inherently untestable ("ipse dixit")               |
| **Peer Review / Publication** | Has the theory/technique been subjected to peer review and publication?                       | Published in peer-reviewed journals; methodology transparent | Limited publication; practitioner-oriented sources       | Unpublished; published in non-peer-reviewed venues only      |
| **Error Rate**                | What is the known or potential rate of error? Are there standards controlling the technique?  | Known, low error rate; established standards in field        | Partial error rate data; some standards exist            | Unknown error rate; no standards; error acknowledged as high |
| **General Acceptance**        | Is the theory/technique generally accepted in the relevant scientific or technical community? | Widely accepted; no credible dissent                         | Accepted by majority but contested by recognized experts | Minority view; rejected or marginalized in the field         |

Additional FRE 702(a) gatekeeping factors:

- **Fit**: Does the expert's testimony "fit" the facts of the case? Methodology may be
  sound in the abstract but misapplied here. _Joiner_.
- **Sufficient facts or data**: Post-2023 amendment courts scrutinize this more actively
  — a thin data set supporting a sweeping opinion is a vulnerability.
- **Qualifications**: Expert must be qualified by knowledge, skill, experience, training,
  or education. Generalist offering specialized opinion is excludable.
- **Analytical gap**: _Joiner_ requires that the connection between data and conclusion be
  explicitly reasoned, not assumed. A "too great an analytical leap" between the data and
  the expert's conclusions is independent grounds for exclusion. [VERIFY]

**Standard of review**: Appellate review of Daubert rulings is for **abuse of discretion**,
not de novo (_General Electric Co. v. Joiner_, 522 U.S. 136 (1997)) [VERIFY]. This highly
deferential standard means the trial court's gatekeeping decisions are effectively
unreviewable unless clearly unreasonable. The practical implication: the trial court
Daubert hearing is the critical battleground. Losing at Daubert is very difficult to
reverse on appeal.

**Qualification Risk Score:**

- **STRONG (18-20/20)**: Expert likely survives Daubert; minimal challenge risk
- **QUALIFIED (14-17/20)**: Expert survives with preparation; some prong requires
  strengthening before disclosure
- **AT-RISK (9-13/20)**: Expert faces significant Daubert exposure; consider supplement
  with stronger expert or additional methodology documentation
- **EXCLUDABLE (below 9/20)**: Expert likely to be excluded; strongly consider replacement

### Frye Screening Framework (Frye States)

The _Frye v. United States_, 293 F. 1013 (D.C. Cir. 1923) [VERIFY] "general acceptance"
standard is narrower than Daubert but applies strictly to **novel scientific evidence**.
For non-novel methods, Frye states generally apply a relevance and qualifications screen only.

**Frye analysis steps:**

1. **Identify whether the methodology is "novel"**: Novel means not yet established in the
   scientific community as generally accepted. Established methodologies (e.g., standard
   blood-alcohol testing) are not subject to Frye scrutiny.
2. **Survey the relevant scientific community**: Identify the community (may be narrow).
   Majority acceptance is required; near-universal acceptance is not.
3. **Distinguish "general acceptance of the principle" from "application"**: Frye only
   tests the general scientific principle; the specific application to facts is for the
   jury to evaluate.

[JURISDICTION-SPECIFIC] Frye states each have specific case law refining the general
acceptance test. California's Kelly/Frye standard (_People v. Kelly_, 17 Cal. 3d 24
(1976) [VERIFY]) is particularly well-developed. New York's Frye analysis (_People v.
Wesley_, 83 N.Y.2d 417 (1994) [VERIFY]) applies to novel evidence only. Verify the
specific state standard before relying on general Frye analysis.

### UK Expert Admissibility Framework (CPR Part 35)

Under CPR 35.3(2), the expert's **overriding duty is to the court**, not to the party
instructing them. This is not merely aspirational — courts have excluded or heavily
discounted partisan experts who appeared to advocate rather than advise.

**Ikarian Reefer Principles** (_National Justice Compania Naviera SA v Prudential
Assurance Co Ltd_ [1993] 2 Lloyd's Rep 68 [VERIFY]):

1. Expert evidence must be the product of the expert's independent judgment, uninfluenced
   by the exigencies of litigation or by the party instructing them.
2. An expert witness should not assume the role of an advocate.
3. Expert must state the facts and assumptions on which their opinion is based; must not
   omit to consider material facts that could detract from the concluded opinion.
4. Expert must make clear when a particular question falls outside their expertise.
5. If the expert's opinion is not properly researched because insufficient data is
   available, that must be stated with an indication that the opinion is provisional.
6. If the expert changes their view after exchange of reports, they must promptly
   communicate this to the other side through legal representatives.
7. Facts relied on by the expert must clearly be distinguished from the expert's opinion.

**CPR 35.4** — Expert evidence requires the court's permission. Courts may limit expert
evidence to a single joint expert under CPR 35.7 where proportionality so requires.

**Permission triggers**: The court grants permission to rely on expert evidence at the
case management conference (CMC). Courts increasingly refuse permission where:

- The issue is within the competence of the court itself (legal interpretation, common
  sense inferences)
- The costs are disproportionate to the sums at issue (Form H costs budget implications)
- A single joint expert would suffice

---

## FRCP 26(a)(2) Report Requirements

### Retained / Specially Employed Experts — FRCP 26(a)(2)(B) [VERIFY]

A party must disclose a **written report** prepared and signed by the expert for any
witness who is **retained or specially employed** to provide expert testimony. The
report must contain:

| #   | Required Element                                                                                                                  | Common Deficiencies                                                                                                               | Severity |
| --- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------- |
| 1   | **A complete statement of all opinions** the witness will express and **the basis and reasons for them**                          | Vague opinions ("within reasonable degree of scientific certainty") without specific factual basis; opinions that expand at trial | CRITICAL |
| 2   | **The facts or data considered** by the witness in forming the opinions                                                           | Failing to list all materials reviewed, including unfavorable data; listing "documents provided by counsel" without specifics     | HIGH     |
| 3   | **Any exhibits** that will be used to summarize or support the opinions                                                           | Exhibits listed at a level of generality that does not allow fair notice                                                          | MEDIUM   |
| 4   | **The witness's qualifications**, including a list of all publications authored or co-authored in the previous 10 years           | Missing publications; inaccurate dates; omitted co-authorship; omitted retracted papers                                           | HIGH     |
| 5   | **A list of all other cases** in which, during the previous 4 years, the witness testified as an expert at trial or by deposition | Incomplete list; cases listed without caption or docket number sufficient to permit research                                      | HIGH     |
| 6   | **A statement of the compensation** to be paid for the study and testimony in the case                                            | Failure to include; range vs. specific rate; failing to distinguish study from testimony                                          | CRITICAL |

**Timing** (FRCP 26(a)(2)(D)): Initial expert disclosures are due at least 90 days
before the date set for trial, or as directed by the court. Rebuttal disclosures are
due within 30 days after the initial disclosure. Verify the scheduling order — most
courts modify these defaults.

**Sanctions**: Failure to comply with FRCP 26(a)(2)(B) can result in exclusion of the
expert's testimony under FRCP 37(c)(1) unless the failure was substantially justified or
harmless. Courts apply a 5-factor test from _Meyers v. Pennypack Woods Home Ownership
Ass'n_ (3d Cir.) [VERIFY] or circuit-equivalent to assess harmlessness.

### Non-Retained Experts — FRCP 26(a)(2)(C) [VERIFY]

For experts **not retained or specially employed** (e.g., treating physicians, supervisors
who formed opinions in the ordinary course), the party must disclose:
(i) The subject matter on which the witness is expected to present expert opinion; and
(ii) A summary of the facts and opinions to which the witness is expected to testify.

**No written report is required.** However, courts draw the line carefully between a
treating physician testifying about treatment (non-retained) and one who was asked to
form a causation opinion (retained).

**The treating physician "catch-22"**: If a treating physician bases causation opinions
on information supplied by counsel — rather than from their own treatment of the patient
— courts in the majority of circuits treat that physician as a retained expert subject to
the full 26(a)(2)(B) report requirement, including the four-year prior testimony
disclosure. The disclosure of how the opinion was formed (information from counsel vs.
clinical treatment) is itself discoverable. Counsel must be deliberate about whether to
engage a treating physician as a percipient witness or as a retained causation expert —
the line determines the entire disclosure obligation. Misclassifying a retained expert
as non-retained to avoid a written report is a sanctionable discovery abuse.

### FRCP 26(b)(4) Work-Product Protections [VERIFY]

Drafts of expert reports and **communications between the party's attorney and the expert
witness** are protected from discovery under FRCP 26(b)(4)(B) and (C), **except** for:
(i) **Compensation** paid or to be paid the expert for the study or testimony;
(ii) **Facts or data** provided by counsel that the expert considered in forming the
opinions; and
(iii) **Assumptions** provided by counsel that the expert relied on in forming the
opinions.

**Practice implications**:

- Do not produce draft reports voluntarily in discovery
- Do not waive the protection by providing drafts to non-privileged parties
- Be prepared to disclose (a) the compensation structure, (b) any factual materials
  counsel provided the expert, and (c) any assumptions counsel directed the expert to use
- Communications that are purely legal strategy (without conveying new facts or
  assumptions) retain protection
- The protection attaches only to **testifying** experts; consulting experts retain
  broader work-product protection under FRCP 26(b)(4)(D)

---

## CPR Part 35 and Practice Direction 35 Requirements

### Report Content Requirements (PD 35, Paras. 2–3) [VERIFY]

An expert's report under CPR Part 35 must:

| #   | Required Element                                                                                                                                         | Notes                                                                                                                                                              |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | Give details of the expert's **qualifications**                                                                                                          | Include any relevant limitations                                                                                                                                   |
| 2   | Give details of any **literature or other material** which the expert has relied on in making the report                                                 | Cannot cherry-pick; must include adverse material                                                                                                                  |
| 3   | Contain a **statement setting out the substance of all facts and instructions** given to the expert that are material to the opinions expressed          | Instructions to the expert are not automatically privileged — courts may order disclosure                                                                          |
| 4   | Make clear which of the facts stated in the report are within the expert's own **knowledge**                                                             | Clearly distinguish fact from opinion                                                                                                                              |
| 5   | Say who **carried out any examination, measurement, test, or experiment** that the expert has used                                                       | Delegation to assistants must be disclosed                                                                                                                         |
| 6   | Where there is a range of opinion on the matters dealt with in the report, **summarise the range of opinion and give reasons** for the expert's own view | Failure to acknowledge competing views is an Ikarian Reefer violation                                                                                              |
| 7   | Contain a **summary of the conclusions** reached                                                                                                         | Avoid unexplained U-turns from earlier expert discussions                                                                                                          |
| 8   | Contain a **declaration that the expert understands their duty to the court** under CPR 35.3 and has complied                                            | Mandatory — report without this declaration is deficient                                                                                                           |
| 9   | Contain a **statement of truth** in the prescribed form (see below)                                                                                      | Failure to include is a technical deficiency but can be cured; the contempt warning creates real criminal exposure for experts who knowingly verify false opinions |

### Single Joint Expert (SJE) — CPR 35.7–35.8 [VERIFY]

Where the parties cannot agree to instruct a single joint expert, the court may
direct one be appointed. SJE practice is most common in:

- Small claims and fast-track cases (where costs of competing experts are disproportionate)
- Cases where the expert question has a "right answer" rather than a range of defensible views
- Building disputes, boundary disputes, some clinical negligence cases
- Financial cases where a single valuation can be obtained

**⟁ CLARIFY** — "Has the court directed or indicated it may direct a single joint expert?
If so, the preparation framework shifts from adversarial to neutral — I can produce
instructions for a SJE and a framework for written questions under CPR 35.6."

**SJE instruction requirements (PD 35, Para. 7)** [VERIFY]:

- Joint instructions where parties can agree; separate instructions where they cannot
  (attached in chronological order)
- Instructions must set out the questions the expert is asked to address
- Must include any background documents the expert needs
- Must not include partisan advocacy or direction on conclusions

**Prescribed statement of truth for UK expert reports** [VERIFY current PD 35 text]:

> _"I confirm that I have made clear which facts and matters referred to in this report
> are within my own knowledge and which are not. Those that are within my own knowledge
> I confirm to be true. The opinions I have expressed represent my true and complete
> professional opinions on the matters to which they refer. I understand that proceedings
> for contempt of court may be brought against anyone who makes, or causes to be made,
> a false statement in a document verified by a statement of truth without an honest
> belief in its truth."_

The contempt warning creates real criminal exposure. Experts must verify the statement
personally and not merely on the basis of counsel's assurances about the facts.

**Written Questions (CPR 35.6)**: Any party may put written questions to an expert
(including SJE) within **28 days** of service of the report. Questions may only be put
**once** and must be for **clarification** only — they may not amount to cross-examination
or attempt to change the opinion. If an expert fails without good reason to answer,
the court may direct that the instructing party may not rely on the report, or may not
recover the costs of the report.

### Hot-Tubbing / Concurrent Evidence (CPR 35.12) [VERIFY]

Courts may (and TCC, ChD, and specialist courts increasingly do) direct that experts
give evidence concurrently rather than sequentially. The typical format:

1. Experts are sworn together
2. Judge leads examination on agreed agenda
3. Each expert gives their view; other experts may comment
4. Parties' counsel then ask questions

**Preparation for hot-tubbing**:

- Identify areas of genuine disagreement vs. areas where positions can be refined
- Prepare the expert to listen carefully and respond proportionately — advocacy in
  hot-tubbing is particularly visible and damaging
- Anticipate the judge's questions based on the joint statement of issues
- Note: CPR 35.12 expert discussions are **without prejudice** (unless parties otherwise
  agree). The joint statement of what is agreed and what remains in dispute is not
  without prejudice — it is served on the parties and filed with the court.

**Expert Discussions Without Prejudice**: Counsel may not instruct an expert to withhold
agreement where agreement is genuinely appropriate, or to agree where genuine disagreement
exists. Such instructions are improper and a potential disciplinary matter.

**Recent UK Developments** [VERIFY for current status]:

- _Chaptre Finance_ [2024]: CPR Part 35 requirements apply to valuation reports in
  restructuring plan proceedings — demonstrating that Part 35 applies beyond conventional
  civil litigation
- _Worcester v Hopley_ [2024] EWHC 2181 (KB): Costs sanctions for unrealistic Precedent H
  expert costs budgets — Master Thornett held claimant's budget was unreasonable and
  disproportionate
- Kings Bench Masters CMH Guidance (September 2024): Updated guidance on costs management
  hearings, including expert evidence phases
- CJC Pre-Action Protocol Review Phase Two (November 2024): Recommended reform of the
  expert nomination process, finding it "wholly unsuited to claims outside the fast track"
- CPR 35.4(3A)–(3B): Specific restrictions in soft tissue injury claims arising from road
  accidents — fixed-cost accredited medical reports required; parties may not adduce
  expert evidence from a non-accredited source [VERIFY current rule text]

---

## Cross-Examination Vulnerability Analysis

Map the expert's testimony across 8 standard attack categories. For each, assess
STRENGTH (HIGH / MEDIUM / LOW) and the specific evidence needed to mount the attack.

### Attack Category 1: Methodology Deficiency

**Core question**: Is the expert's methodology accepted in the field, and was it
correctly applied here?

| Attack Type                                       | Evidence Required                                                                 | Daubert Prong Engaged                |
| ------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------ |
| Untested or non-replicable methodology            | Expert's publications; field treatises                                            | Testing/falsifiability               |
| Deviation from expert's own published methodology | Expert's prior publications                                                       | Peer review; general acceptance      |
| Data cherry-picking (exclusion of adverse data)   | Internal case documents; depositions                                              | Sufficient facts / data (FRE 702(b)) |
| Conclusion-driven analysis ("working backwards")  | Expert's prior report drafts (if discoverable); deposition about sequence of work | Fit (Joiner)                         |
| Deviation from field consensus methodology        | Learned treatises; competing expert                                               | General acceptance                   |

**Sample deposition sequence**: Establish the standard methodology from the expert's own
prior publications → elicit that the expert knows the field's standard protocols →
expose the specific deviations in this case → have expert characterize the deviations.

### Attack Category 2: Qualifications Mismatch

**Core question**: Does the expert actually have the expertise they claim for the opinion
offered in this case?

- Degree in adjacent field, not the specific field of opinion
- License/certification lapsed or in different jurisdiction
- Prior exclusion based on qualifications (research the expert's prior cases)
- Experience is theoretical (academic) but the opinion addresses practical field matters
- Expert's publications are in a different sub-specialty than the opinion offered

[JURISDICTION-SPECIFIC] **UK**: Under CPR 35.3, the expert must make clear when a
question falls outside their expertise. Failure to do so is itself an Ikarian Reefer
violation and can be used to undermine the expert's credibility on the opined-to matters.

### Attack Category 3: Financial Bias / "Hired Gun"

**Core question**: Is the expert financially dependent on a particular outcome or on
advocacy-oriented testimony?

Key metrics to develop in deposition (from FRCP 26(a)(2)(B)(vi) prior case list and
compensation disclosure) [VERIFY]:

- **Retaining-side ratio**: Percentage of cases testified for plaintiff vs. defense
- **Retaining-firm ratio**: Cases for the same law firm (high frequency suggests
  captive relationship)
- **Annual income from litigation testimony**: Expert's litigation work as a proportion
  of total professional income
- **Contingency or outcome-related compensation**: Prohibited by ABA Model Rule 3.4(b)
  and analogous state rules [VERIFY]; if present, this is disqualifying

**UK**: CPR 35.3 overriding duty expressly negates partisan loyalty. Evidence that the
expert communicated privately with the instructing solicitors about desired conclusions
(exposed via the PD 35 Para. 3 instruction disclosure) is highly damaging.

### Attack Category 4: Learned Treatise Attack (FRE 803(18)) [VERIFY]

FRE 803(18) provides a hearsay exception for **learned treatises** when:
(A) the statement is called to the attention of the expert on cross-examination or is
relied on by the expert on direct; AND
(B) the publication is **established as a reliable authority** by the expert's admission,
other expert testimony, or judicial notice.

**Preparation steps (challenging side)**:

1. Identify every major treatise, textbook, or peer-reviewed article in the expert's field
2. Research whether the expert has cited any in prior publications or prior testimony
   (prior testimony list from 26(a)(2)(B)(v) is invaluable)
3. Identify statements in those treatises that contradict the expert's opinions in this case
4. At deposition: confirm the treatise is authoritative in the field BEFORE showing the
   inconsistency — note that FRE 803(18) does **not** require the witness to acknowledge
   the treatise as authoritative; it only requires the treatise to be "called to the
   attention" of the expert. If the expert denies authoritativeness, establish it through
   your own expert, judicial notice, or other means [VERIFY]
5. Once established as authoritative, the passage is read into evidence at trial as
   **substantive evidence** (not merely impeachment) — the jury hears the authoritative
   source directly contradicting the expert; the treatise may not be received as a
   physical exhibit but the passage read aloud is admissible

**Preparation steps (retaining side)**: Identify every treatise that may be used against
the expert and prepare the expert to distinguish or explain apparent inconsistencies.

[JURISDICTION-SPECIFIC] **UK**: CPR 35 does not have a direct FRE 803(18) equivalent.
Learned treatises may be put to an expert in cross-examination. The expert must
acknowledge material they relied upon. PD 35 Para. 2.2 requires disclosure of literature
relied upon — inconsistency between the disclosed materials and the expert's conclusions
is a direct attack vector.

### Attack Category 5: Prior Inconsistent Opinions

**Core question**: Has the expert published, testified, or opined to a position
inconsistent with the current opinions in this case?

Sources of prior inconsistent opinions:

- Prior expert reports in disclosed prior cases (26(a)(2)(B)(v))
- Published academic articles, book chapters, conference papers
- Prior deposition testimony (from the 4-year case list)
- Prior consulting or academic reports not previously published
- Regulatory submissions, FDA/EPA comments, agency testimony

**Impeachment sequencing**: Establish the prior opinion first ("you wrote/testified/
published X") → confirm it represents the expert's genuine view ("you believed that
was correct?") → elicit that the factual predicates here are materially similar →
confront with the inconsistency.

### Attack Category 6: Cherry-Picked or Incomplete Analysis

**Core question**: Did the expert consider all material evidence, or only evidence
that supports the retained opinion?

Indicators of incomplete analysis:

- Internal documents the expert did not review but opposing counsel produced
- Test results that undermine the expert's theory, not addressed in the report
- Studies inconsistent with the expert's methodology, not acknowledged
- Alternative hypotheses that a reasonable expert in the field would have considered

[JURISDICTION-SPECIFIC] **UK**: Under Ikarian Reefer principle 3, an expert must not
omit to consider material facts which could detract from the concluded opinion. Failure
to address adverse evidence is a disciplinary-grade breach of the expert's court duty.

### Attack Category 7: Improper Ultimate Issue Opinion

**Core question**: Has the expert improperly testified to legal conclusions rather than
factual or technical matters?

Under FRE 704(a), an expert may testify as to an ultimate issue of fact [VERIFY].
However, experts may NOT offer legal conclusions dressed as fact (e.g., "the defendant
was negligent," "the contract was breached"). The line between ultimate issue of fact
(permissible) and legal conclusion (impermissible) is contested.

[JURISDICTION-SPECIFIC] **FRE 704(b)**: In criminal cases, mental health experts may
NOT state an opinion on whether the defendant had the requisite mental state [VERIFY].

[JURISDICTION-SPECIFIC] **UK**: The Ikarian Reefer makes clear the expert must not
assume the role of an advocate. Opining to legal liability (as opposed to factual
causation, standard of care, or technical matters) is excluded.

### Attack Category 8: Insufficient Basis / Speculation

**Core question**: Is the expert's opinion based on sufficient facts or data, or is it
speculation extrapolated from thin evidence?

Post-2023 FRE 702(b) amendment makes this prong more actively enforced. Courts no longer
treat data sufficiency as purely a weight/credibility issue for the jury — insufficient
data is grounds for exclusion.

Key questions:

- What were the actual sample sizes, data sets, or experimental conditions?
- Did the expert assume facts not in evidence?
- Did the expert extrapolate from animal studies or lab conditions to human or field
  outcomes without validating the extrapolation?
- Did the expert apply standard methodologies to non-standard data?

---

## Severity / Admissibility Classification

### Classification System

Apply the four-tier classification to all qualification findings, report deficiencies,
and cross-examination vulnerabilities:

| Tier | Label          | Definition                                                                                                  | Required Action                                                                            |
| ---- | -------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| 🟢   | **ADMISSIBLE** | Expert meets all applicable standards; no material vulnerabilities                                          | Note for awareness; proceed to trial preparation                                           |
| 🟡   | **QUALIFIED**  | Expert likely admissible with specific cures; one or more issues require remediation before disclosure      | Remediate identified issues; re-screen after cure                                          |
| 🔴   | **AT-RISK**    | Expert faces significant exclusion exposure; Daubert or CPR 35 challenge has reasonable prospect of success | Consider supplementing with stronger expert; prepare robust opposition brief if proceeding |
| ⛔   | **EXCLUDABLE** | Expert will likely be excluded on current record; one or more fundamental deficiencies cannot be cured      | Strong recommendation to replace; if proceeding, prepare exclusion defense strategy        |

---

## Rebuttal Expert Strategy

### Rebuttal Decision Framework

Apply this four-factor test to decide whether to retain a rebuttal expert:

| Factor                         | Retain Rebuttal                                                                      | No Rebuttal Needed                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| **Case impact**                | Opposing expert is case-dispositive on a core issue                                  | Issue is peripheral or can be neutralized on cross                                          |
| **Cross-examination efficacy** | Methodology is too complex for cross alone; jury may defer to uncontested expert     | Expert is vulnerable to learned treatise / prior opinion attacks that make cross sufficient |
| **Scope fit**                  | A qualified expert exists whose opinions will directly contradict the initial expert | Rebuttal expert would not directly contradict — risk of exceeding rebuttal scope            |
| **Cost-benefit**               | Value of exclusion or discrediting of opposing expert justifies cost                 | Proportionality concerns; SJE may be preferable                                             |

### Rebuttal Scope Constraints

Under FRCP 26(a)(2)(D), rebuttal experts are permitted only for opinions "intended
solely to contradict or rebut evidence on the same subject matter identified by another
party" [VERIFY]. Courts enforce this strictly. Rebuttal experts who offer new affirmative
opinions risk exclusion of the new opinions.

**Rebuttal scope discipline**:

- Map every proposed rebuttal opinion to a specific statement in the initial expert's report
- Do not include new affirmative opinions not triggered by the initial expert's report
- Distinguish "contradicting" (permissible) from "adding to the case" (not permissible)
- If an opinion is both rebuttal AND affirmative, disclose it as an initial expert opinion
  (with appropriate timing under 26(a)(2)(D))

[JURISDICTION-SPECIFIC] **UK**: There is no direct CPR equivalent of the FRCP rebuttal
expert framework. Under CPR 35.4, the court controls the number and scope of experts. A
party seeking to rely on more expert evidence than initially permitted requires further
court permission. The expert discussion framework under CPR 35.12 often narrows
disagreements before trial without requiring a separate "rebuttal" expert.

---

## Conflicts Identification Framework

### Conflicts Screening Matrix

| Category        | Type                                | Screening Question                                                                                                   | Severity                                                 |
| --------------- | ----------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Financial**   | Contingency fee arrangement         | Is expert's compensation in any way contingent on the outcome of the case?                                           | DISQUALIFYING — violates ABA Rule 3.4(b) analog [VERIFY] |
| **Financial**   | Equity/ownership interest           | Does expert hold equity in the plaintiff or defendant entity?                                                        | DISQUALIFYING                                            |
| **Relational**  | Prior adverse retention             | Has expert previously been retained by or testified for the opposing party in this case or a closely related matter? | DISQUALIFYING (may be waivable with disclosure)          |
| **Relational**  | Retained by opposing counsel's firm | Has expert testified repeatedly for the opposing law firm?                                                           | CREDIBILITY — must be disclosed and pre-empted           |
| **Testimonial** | Prior inconsistent opinions         | Has expert publicly or in prior testimony opined to positions inconsistent with retained opinion?                    | CREDIBILITY — assess severity case by case               |
| **Testimonial** | Prior exclusion rulings             | Has expert been excluded in prior cases?                                                                             | HIGH CREDIBILITY — must be disclosed and addressed       |
| **Testimonial** | Retracted publications              | Has expert published work that was later retracted or subject to editorial concern?                                  | HIGH CREDIBILITY                                         |
| **Relational**  | Personal relationship               | Does expert have a personal relationship with a party, attorney, or witness?                                         | CREDIBILITY — must be disclosed                          |
| **Regulatory**  | Disciplinary history                | Has expert been subject to professional disciplinary proceedings?                                                    | HIGH CREDIBILITY to DISQUALIFYING depending on nature    |
| **Testimonial** | Excessive prior-side ratio          | Expert has testified >80% for one side over a meaningful sample                                                      | CREDIBILITY — anticipate "hired gun" attack              |

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Identify the applicable qualification standard, report type (26(a)(2)(B) vs.
(C)), and jurisdiction. Classify the engagement phase. Identify which attack categories
are most likely based on the expert's field and prior testimony record.

**DO**: Execute the qualification screening, report compliance review, vulnerability
mapping, and deposition preparation. Apply the conflicts matrix. Assess rebuttal need.

**CHECK**: Run the Citation Quality Gates. For every EXCLUDABLE or CRITICAL classification,
run the Self-Interrogation. Verify all deadlines against the actual scheduling order.

**ACT**: Record expert-specific patterns for future depositions (e.g., known learned
treatises the expert has cited previously; known cross-examination vulnerabilities from
prior depositions). Note any new case law on admissibility for this expert type.

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                       | Fail Action                                                            |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| **Source**     | Every procedural rule citation identifies the specific rule number and sub-provision                                                       | Add specific citation or mark "[RULE UNVERIFIED — counsel to confirm]" |
| **Format**     | Case citations follow a consistent Bluebook-equivalent format (US) or OSCOLA-equivalent (UK)                                               | Fix format                                                             |
| **Currency**   | Every rule and statutory reference verified for current version (FRCP / FRE are amended annually; CPR is amended by statutory instruments) | Flag "[CHECK CURRENCY — rule may have been amended]"                   |
| **Domain**     | Analysis applies the law of the specific court / jurisdiction; no bleed from other jurisdictions                                           | Remove or flag jurisdictional bleed                                    |
| **Confidence** | Uncertainty explicitly stated; all memory-sourced citations marked [VERIFY]                                                                | Add confidence qualifier                                               |

### Self-Interrogation for EXCLUDABLE / CRITICAL Classifications

For any item classified EXCLUDABLE (qualification) or CRITICAL (report compliance), apply
this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the exclusion risk follow logically from the rule or case cited?
- Would the specific court or judge actually exclude on this basis, given the local
  Daubert jurisprudence and circuit precedent?
- Is there a response or cure the retaining party could mount?

**Pass 2 — Completeness**:

- Have all relevant rules (local rules, standing orders, scheduling order) been considered?
- Are there circuit-level cases that cut in favor of admissibility that have not been
  addressed?
- Have the most recent post-2023 FRE 702 amendment cases been considered?

**Pass 3 — Challenge**:

- What is the strongest argument that this expert should be admitted despite the identified
  deficiency?
- Under what circumstances would a trial court exercise its gatekeeping discretion to
  admit?
- Is the EXCLUDABLE classification proportionate, or is this actually AT-RISK with
  adequate curative preparation?

If any pass reveals a weakness, revise before delivery. Mark: `self_interrogation: PASS`
or `self_interrogation: REVISED`.

### Confidence Scoring

For each material qualification finding or vulnerability, assign a confidence level:

| Level        | Range     | Meaning                                        | Action                                                   |
| ------------ | --------- | ---------------------------------------------- | -------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Clear rule, unambiguous application            | State with confidence                                    |
| **High**     | 0.80-0.94 | Strong authority; minor interpretation issues  | State with brief caveat                                  |
| **Probable** | 0.60-0.79 | Good arguments; outcome depends on judge       | State with reasoning and contra-indicators               |
| **Possible** | 0.40-0.59 | Genuinely uncertain; judge could go either way | Flag for counsel review with both sides                  |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative                        | Do not assert; flag as "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every expert witness preparation output MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-expert-witness-preparation"
  engagement_type: "[Qualification screening / Report review / Vulnerability mapping / Deposition prep / Rebuttal strategy / Full preparation package]"
  expert_field: "[Expert's field of testimony]"
  expert_name: "[Expert's name or 'Not provided']"
  side: "[Retaining / Challenging / Neutral]"
  jurisdiction: "[US federal — district/circuit / State: [state] / England and Wales / Other]"
  applicable_standard: "[Daubert (FRE 702 as amended 2023) / Frye / CPR Part 35]"
  qualification_risk_score: "[STRONG / QUALIFIED / AT-RISK / EXCLUDABLE]"
  report_compliance: "[COMPLIANT / PARTIAL / NON-COMPLIANT elements: list]"
  critical_vulnerabilities:
    - "[Most material cross-examination attack vector and strength]"
  rebuttal_recommended: "[Yes / No / Assess after deposition]"
  disqualifying_conflicts: "[None identified / List]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  rules_consulted:
    - "FRCP 26(a)(2)(B) — [VERIFIED / UNVERIFIED]"
    - "FRE 702 (Dec. 1, 2023 amendment) — [VERIFIED / UNVERIFIED]"
    - "CPR Part 35 — [VERIFIED / UNVERIFIED if applicable]"
  case_law_consulted:
    - "Daubert v. Merrell Dow, 509 U.S. 579 (1993) — [VERIFIED / UNVERIFIED]"
    - "Kumho Tire Co. v. Carmichael, 526 U.S. 137 (1999) — [VERIFIED / UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no EXCLUDABLE classifications)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Scheduling order not reviewed — all deadline references are default rules only]"
    - "[Expert's prior testimony list not available — prior exclusion analysis incomplete]"
  reviewer: "AI-assisted — requires qualified litigation counsel review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in expert witness preparation:

1. **Assuming Daubert applies without checking the governing standard** — Daubert is the
   federal standard and the majority state standard, but Frye states remain and some have
   hybrid tests. Never assume; always verify the applicable standard for the specific court.

2. **Treating FRE 702 as unchanged since Daubert** — The 2023 amendment to FRE 702
   materially strengthened the gatekeeping language. Cases decided before December 1, 2023
   on the old text are not fully reliable guides to current analysis. Always flag the
   amendment and check post-amendment circuit decisions. [VERIFY current case law]

3. **Ignoring the six FRCP 26(a)(2)(B) elements** — Treating disclosure as a formality
   rather than a substantive obligation. Incomplete prior testimony lists and under-
   disclosed compensation are among the most litigated exclusion grounds. Audit all six
   elements before disclosure.

4. **Conflating retained and non-retained expert obligations** — A treating physician
   retained specifically to form a causation opinion (retained) requires a 26(a)(2)(B)
   report. A treating physician testifying about their own course of treatment (non-
   retained) does not. Misclassifying the second as the first (or vice versa) invites
   sanctions or exclusion.

5. **Disclosing draft reports in discovery** — FRCP 26(b)(4)(B) protects expert draft
   reports. Voluntarily producing drafts (e.g., in a clawback dispute or compelled
   production) waives the protection and exposes the attorney–expert dialogue. Always
   assert and document the work-product protection.

6. **Preparing the expert to deny the three 26(b)(4)(C) exceptions** — The three
   exceptions (compensation, facts/data provided by counsel, assumptions provided by
   counsel) are mandatory disclosures. Coaching an expert to obscure these violates FRCP
   and can constitute witness tampering.

7. **Neglecting the scheduling order in favor of default timelines** — Default disclosure
   timelines (90/30 days) are routinely modified. Proceeding on default timelines without
   checking the scheduling order is a recipe for missed deadlines and exclusion under
   FRCP 37(c)(1).

8. **Building a Daubert motion without a deposition record** — A Daubert motion without
   deposition testimony is difficult to support because the expert has not been tested on
   methodology. Most successful Daubert motions are built on deposition admissions.
   Sequence: depose first, then move.

9. **Learned treatise attacks without establishing authority** — FRE 803(18) requires that
   the treatise be established as a reliable authority first. If the expert denies the
   treatise is authoritative and you have no other foundation, the attack fails.
   Pre-identify foundational sources before the deposition.

10. **Rebuttal experts who offer new affirmative opinions** — A rebuttal expert who
    introduces new theories not directly responding to the initial expert's report is
    offering out-of-scope opinion. Courts regularly exclude such opinions or hold they
    should have been disclosed in the initial round. Map every rebuttal opinion to a
    specific initial expert statement before disclosure.

11. **Ignoring the UK "overriding duty to court" in expert preparation** — UK experts must
    act independently and not as advocates. Preparing a UK expert the way a US advocate-
    style expert is prepared (coaching toward conclusions, emphasizing the client's
    position) will produce an expert who appears partisan and whose evidence is discounted.
    Prepare UK experts to present the full range of opinion and to acknowledge adverse
    points before they are put in cross-examination.

12. **Treating SJE instructions as a formality** — Instructions to a Single Joint Expert
    must be balanced and must not advocate for a particular outcome. Partisan instructions
    to an SJE can lead to the court disregarding the expert entirely or directing new
    instructions at costs expense.

13. **Missing financial conflicts in the screening** — Experts who have served as
    consultants to, hold equity in, or have an ongoing business relationship with an adverse
    party's law firm create conflicts that may require disqualification. Run a full conflict
    check before engagement, not after the report is produced.

14. **Relying on an excluded expert's prior opinions to impeach** — Prior exclusion on
    Daubert grounds means the expert's testimony on the excluded matter was found
    unreliable. However, it does not automatically disqualify the expert in new proceedings.
    Courts analyze admissibility de novo. Use prior exclusions as a credibility tool, not
    as automatic disqualification.

15. **Over-preparing the expert to give scripted answers** — Deposition preparation should
    make the expert comfortable and knowledgeable, not robotic. Overcoached witnesses are
    easily exposed. Prepare the expert to listen carefully, answer only what is asked, and
    say "I don't know" or "I don't recall" when accurate.

16. **Producing a report that expands at trial** — Trial testimony that materially expands
    or changes the disclosed opinions risks exclusion under FRCP 37(c)(1). All anticipated
    opinions must be in the 26(a)(2)(B) report. If additional opinions become necessary,
    supplement in advance under FRCP 26(e).

17. **Ignoring hot-tubbing preparation in UK proceedings** — Concurrent evidence is
    increasingly used in specialist UK courts (TCC, ChD, Commercial Court). An expert
    unprepared for hot-tubbing — where their opinions are directly tested against competing
    experts in real time with the judge actively participating — is at a severe disadvantage.

---

## Writing Standards

Apply plain-language discipline to all expert witness preparation outputs:

**For qualification memos and Daubert analysis** (shared with supervising counsel):

- Lead with the risk score (STRONG / QUALIFIED / AT-RISK / EXCLUDABLE)
- State each vulnerability in one sentence
- Cite the specific rule or case that creates the risk; mark [VERIFY] if citing from memory
- Use active voice: "The expert lacks peer-reviewed publications supporting this methodology"
  not "It is noted that publications may be lacking"
- Include proposed cures for each QUALIFIED or AT-RISK item

**For deposition preparation memos** (shared with the expert):

- Plain, non-legal language where possible — the expert is not a lawyer
- One rule or concept per sentence
- Concrete examples of good and bad answers for each anticipated question
- Do not advise on legal strategy — advise on honest, precise communication

**Quality gates before delivery**:

1. Can a supervising partner understand the risk score and top issues in 60 seconds?
2. Is every rule citation specific and keyed to the correct sub-provision?
3. Are all case citations marked [VERIFY] if not confirmed against authoritative sources?
4. Is every conclusion backed by a specific rule, case, or principle?
5. Are strategic recommendations (e.g., replace the expert, retain a rebuttal expert)
   clearly labeled as recommendations, not conclusions?

---

## External Tool Integration

This skill uses **legalcode-mcp** as its primary legal research tool for case-specific
expert admissibility authority.

**With legalcode-mcp connected:**

- In Step 3, search for judge-specific Daubert rulings and circuit-level FRE 702 trends
- Search for prior exclusion decisions involving the specific expert (by name)
- Verify current text of FRCP 26(a)(2), FRE 702-705, CPR Part 35, PD 35
- Search for post-2023 amendment FRE 702 cases establishing how courts interpret the
  revised "reflects a reliable application" language
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all case citations with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Focus analysis on structural qualification issues and rule-based report compliance
  rather than judge-specific Daubert pattern analysis
- Advise counsel to research the specific judge's prior expert exclusion decisions
  independently

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Expert Witness Preparation: [Expert Name / "Opposing Expert"] — [Engagement Phase]

**Expert**: [Name, title, institution]
**Field**: [Expert's field of testimony]
**Case**: [Case caption or description]
**Court**: [Court / jurisdiction]
**Applicable Standard**: [Daubert (FRE 702 as amended 2023) / Frye / CPR Part 35]
**Your Side**: [Retaining / Challenging]
**Date**: [date]

---

## Summary Finding

**Qualification Risk Score**: [STRONG 🟢 / QUALIFIED 🟡 / AT-RISK 🔴 / EXCLUDABLE ⛔]

**Top 3 Issues**:

1. [Most critical issue — severity — one-line summary]
2. [Second issue — severity]
3. [Third issue — severity]

---

## Qualification Screening (Daubert / FRE 702)

### Prong 1: Testing / Falsifiability — [Score / Risk Level]

[Analysis]

### Prong 2: Peer Review / Publication — [Score / Risk Level]

[Analysis]

### Prong 3: Error Rate / Standards — [Score / Risk Level]

[Analysis]

### Prong 4: General Acceptance — [Score / Risk Level]

[Analysis]

### Overall FRE 702 Fitness — [STRONG / QUALIFIED / AT-RISK / EXCLUDABLE]

[Summary with confidence score]

---

## Report Compliance Review (FRCP 26(a)(2)(B) / CPR 35 PD)

| Element                          | Status                                | Issue         | Cure   |
| -------------------------------- | ------------------------------------- | ------------- | ------ |
| 1. Complete opinions and basis   | [COMPLIANT / PARTIAL / NON-COMPLIANT] | [description] | [cure] |
| 2. Facts or data considered      | …                                     | …             | …      |
| 3. Exhibits                      | …                                     | …             | …      |
| 4. Qualifications / publications | …                                     | …             | …      |
| 5. Prior cases (4 years)         | …                                     | …             | …      |
| 6. Compensation                  | …                                     | …             | …      |

---

## Cross-Examination Vulnerability Map

| Attack Category                | Strength              | Evidence Needed     | Recommended Action            |
| ------------------------------ | --------------------- | ------------------- | ----------------------------- |
| 1. Methodology deficiency      | [HIGH / MEDIUM / LOW] | [specific evidence] | [depose / Daubert / pre-empt] |
| 2. Qualifications mismatch     | …                     | …                   | …                             |
| 3. Financial bias / hired gun  | …                     | …                   | …                             |
| 4. Learned treatise            | …                     | …                   | …                             |
| 5. Prior inconsistent opinions | …                     | …                   | …                             |
| 6. Cherry-picked analysis      | …                     | …                   | …                             |
| 7. Improper ultimate issue     | …                     | …                   | …                             |
| 8. Insufficient basis          | …                     | …                   | …                             |

---

## Deposition Preparation Outline / Cross-Examination Outline

[Section heading: "Preparation Memo for [Expert Name]" (retaining side) OR "Cross-
Examination Outline — [Expert Name]" (challenging side)]

### Sequence 1: [Topic]

[Questions / preparation points]

### Sequence 2: [Topic]

[Questions / preparation points]

---

## Rebuttal Expert Assessment

**Recommendation**: [Retain rebuttal expert / No rebuttal needed / Assess after deposition]
**Rationale**: [2-3 sentences applying the 4-factor rebuttal decision framework]
**Scope constraint**: [Specific initial expert opinions the rebuttal must address]
**Disclosure deadline**: [FRCP 26(a)(2)(D) default or scheduling order date]

---

## Conflicts Screening

| Conflict Category            | Finding   | Severity                             |
| ---------------------------- | --------- | ------------------------------------ |
| Financial conflicts          | [finding] | [DISQUALIFYING / CREDIBILITY / None] |
| Prior adverse retention      | …         | …                                    |
| Prior inconsistent testimony | …         | …                                    |
| Prior exclusions             | …         | …                                    |
| Excessive one-side ratio     | …         | …                                    |

---

## Recommended Next Steps

[Specific actions, owners, and deadlines]

---

## Glass Box Audit Trail

[YAML block per Glass Box section above]
```

---

## Localization Notes

### US State Variations

[JURISDICTION-SPECIFIC] When operating in a specific US state, verify:

1. Whether the state applies Daubert, Frye, or a hybrid standard for the specific type
   of expert at issue
2. State-specific procedural rules for expert disclosure timing and format
3. Local court rules and standing orders on expert depositions, Daubert briefing schedules,
   and page limits for exclusion motions
4. State bar ethics rules on expert compensation (some states have more specific rules
   than ABA Model Rule 3.4(b))

### UK Variations Beyond England and Wales

[JURISDICTION-SPECIFIC] Scotland applies different civil procedure rules (the Court of
Session Rules and Sheriff Court Rules). Expert evidence in Scotland is governed by different
principles. Do not apply CPR Part 35 analysis to Scottish proceedings without verification.
Northern Ireland follows broadly similar principles to England and Wales but verify under
the Rules of the Court of Judicature (Northern Ireland).

### International Arbitration

[JURISDICTION-SPECIFIC] Expert witnesses in international commercial arbitration are
governed by the arbitral rules (ICC, LCIA, AAA/ICDR, SIAC, HKIAC) and, where adopted,
the IBA Rules on the Taking of Evidence in International Arbitration (2020). The IBA
Rules Art. 5 (party-appointed experts) and Art. 6 (tribunal-appointed experts) provide
a different framework from both FRCP and CPR. Use the Legalcode arbitration skills for
international arbitration expert strategy.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis combining US federal expert witness
law (FRCP 26(a)(2), FRE 702 as amended 2023, Daubert / Kumho Tire / Joiner trilogy,
FRCP 26(b)(4) work-product protections), state Frye practice, UK CPR Part 35 and
Practice Direction 35 (Ikarian Reefer principles), and expert deposition best practices
from the litigation practitioner community. Calibrated against the Legalcode quality
standard using the legalcode-contract-review and legalcode-deposition-preparation
reference skills. All rule and case citations carry [VERIFY] markers pending verification
against authoritative legal sources.
