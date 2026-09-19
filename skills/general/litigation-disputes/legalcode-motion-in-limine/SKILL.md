---
name: legalcode-motion-in-limine
description: Draft and analyze motions in limine for US federal court proceedings. Use when filing or
  opposing pretrial motions to exclude or limit evidence, preparing argument outlines for evidentiary
  hearings, anticipating opposition responses, or advising on evidentiary strategy before trial.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Draft and analyze motions in limine for US federal court proceedings. Use when filing or opposing pretrial motions to exclude or limit evidence, preparing argument outlines for evidentiary hearings, anticipating opposition responses, or advising on evidentiary strategy before trial. Covers FRE 401-403 relevance and unfair prejudice balancing (Old Chief, Sprint/United Management), FRE 404(b) prior acts and crimes (Huddleston conditional relevance, 2020 notice amendment, inextricably intertwined doctrine), FRE 407-411 policy exclusions (subsequent remedial measures, compromise negotiations, medical payments, plea statements, liability insurance), FRE 501-502 privilege and inadvertent waiver (clawback orders, 502(d) federal-court orders), FRE 702 expert testimony and Daubert gatekeeping (2023 amendment, Joiner analytical-gap, Kumho Tire non-scientific experts), FRE 801-807 hearsay and exceptions (Crawford Confrontation Clause testimonial overlay, Davis primary-purpose test), and FRE 609 prior convictions for impeachment (crimen falsi mandatory admission, 10-year balancing). Includes standard opposition and response arguments, limiting instruction strategy under FRE 105, conditional relevance under FRE 104(b), door-opening doctrine, and offer-of-proof requirements. Generates argument outlines with confidence-scored authority, anticipated opposition arguments, and reply strategy with Glass Box audit trail.


# Legalcode Motion in Limine

> **Disclaimer**: This skill provides a framework for AI-assisted motion in limine drafting
> and analysis. It does not constitute legal advice. All outputs must be reviewed, verified,
> and signed by qualified legal counsel licensed in the relevant jurisdiction before filing
> with any court. Evidentiary rules, procedural requirements, and governing case law change
> frequently; verify all authority before relying on any conclusion or citation. AI-generated
> motion arguments may contain errors in legal analysis, citation accuracy, or strategic
> assessment — all arguments must be verified against current authority and the specific
> facts of the case. Any cited authority marked `[VERIFY]` has not been independently
> validated and must be confirmed before reliance. Filing a motion in limine constitutes
> a Rule 11 certification that arguments are well-grounded in fact and law; counsel bears
> independent professional responsibility for that certification.

---

## Purpose and Scope

This skill drafts and analyzes motions in limine in US federal courts — pretrial motions
requesting advance rulings on the admissibility of specific evidence before trial. It
operates in two primary modes:

1. **Drafting Mode**: Generates argument blocks, outlines, and supporting authority for a
   motion to exclude or limit specific evidence based on the FRE grounds selected. Produces
   a structured argument framework for attorney review and refinement into a final motion.

2. **Analysis Mode**: Evaluates a motion in limine the user has received — identifying the
   moving party's strongest and weakest arguments, assessing opposition viability, and
   developing response strategy including limiting instructions and alternative admissibility
   theories.

**Covers:**

- **FRE 401-403**: Relevance threshold, character evidence context, unfair prejudice
  balancing — including Old Chief stipulation doctrine, sprint/context-dependency rule,
  and 403 as "last resort" not "first resort"
- **FRE 404(b)**: Other crimes, wrongs, or acts — propensity prohibition, permitted
  non-propensity purposes, 2020 notice amendment, Huddleston conditional-relevance
  standard, inextricably intertwined / direct evidence doctrine, Beechum two-step test
- **FRE 407**: Subsequent remedial measures — admissibility carve-outs for ownership,
  control, feasibility, and impeachment; products liability nuances
- **FRE 408**: Compromise negotiations — what is and is not protected, the bias/undue
  delay/obstruction exceptions, the "in connection with" scope limit
- **FRE 409**: Payment of medical expenses — narrow exclusion scope, surrounding
  statements not protected
- **FRE 410**: Plea statements — withdrawn guilty pleas, nolo contendere, statements in
  plea discussions; perjury exception
- **FRE 411**: Liability insurance — agency, ownership, control, bias exceptions
- **FRE 501-502**: Federal common law privilege in federal-question cases, state law in
  diversity; attorney-client, work product, marital communications, psychotherapist-patient;
  inadvertent disclosure, 502(d) court orders, clawback agreements
- **FRE 702 / Daubert**: Expert qualification, methodology reliability, and fit to facts;
  2023 amendment clarifications on preponderance standard and gatekeeping; Joiner
  analytical-gap exclusion; Kumho Tire extension to all expert testimony
- **FRE 801-807**: Hearsay definition, non-hearsay uses, 801(d) admissions and prior
  statements, 803 exceptions (present sense impression, excited utterance, business
  records, public records), 804 exceptions (former testimony, dying declarations),
  807 residual exception; Crawford / Davis Confrontation Clause overlay for criminal cases
- **FRE 609**: Prior convictions impeachment — crimen falsi mandatory admission,
  felony balancing, 10-year bar and heightened balancing, juvenile adjudications
- **Response arguments**: Limiting instruction (FRE 105), conditional relevance (FRE
  104(b)), offer of proof, door-opening doctrine, curative instruction alternatives
- **Procedural posture**: Pretrial conference timing, FRCP Rule 16 authority, local rule
  compliance, briefing schedule, standard of review on appeal (abuse of discretion),
  running objections and renewed trial objections

**Does not:**

- Replace counsel's professional judgment on evidentiary strategy or judicial temperament
- Certify Rule 11 compliance (only filing counsel may certify)
- Draft the full motion (produces structured argument outlines for counsel to develop)
- Address state court evidentiary motion standards (state rules may differ materially
  from federal FRE; flag for local counsel review)
- Conduct independent factual investigation or verify client representations
- Cover motions to suppress under the Fourth Amendment / exclusionary rule (different
  constitutional framework; see separate suppression skills)
- Address in-depth Confrontation Clause analysis in criminal cases beyond the Crawford
  testimonial-hearsay framework

**Related skills:**

- `legalcode-evidence-admissibility-analysis` — Analyze admissibility of specific items
  of evidence pre-filing (upstream analysis that feeds into this skill)
- `legalcode-motion-to-dismiss-drafter` — Rule 12(b) dispositive motions (pre-answer
  stage; distinct procedural vehicle)
- `legalcode-summary-judgment-analysis` — Rule 56 motions after discovery (evidence
  admissibility issues surface in Rule 56 briefing)
- `legalcode-expert-witness-preparation` — Prepare experts for Daubert challenges and
  deposition (defensive counterpart to Daubert motions in limine)
- `legalcode-opposition-brief-drafter` — Draft full opposition briefs to any motion type
- `legalcode-deposition-preparation` — Prepare witnesses; deposition testimony may
  become the subject of hearsay or prior-inconsistent-statement motions

---

## Jurisdiction and Governing Law

This skill applies to US federal courts operating under the Federal Rules of Evidence
(FRE), as amended through December 1, 2023 (FRE 702 amendment effective). It is not
designed for state court practice, where evidentiary rules may differ materially (some
states still apply Frye general-acceptance rather than Daubert for expert testimony).

[JURISDICTION-SPECIFIC] When adapting for state practice, research and apply:

- Whether the state has adopted the FRE or uses an independent code
- The state's expert testimony standard (Daubert, Frye, or hybrid)
- State-specific privileges not recognized in federal common law
- State constitutional provisions affecting admissibility (beyond the federal
  Confrontation Clause and Fifth Amendment)
- Local court rules on motion in limine filing deadlines, page limits, and
  hearing requirements — these vary significantly across districts and divisions
- Circuit-specific doctrinal variations within the federal system (noted where
  material throughout this skill)

[JURISDICTION-SPECIFIC — CIRCUIT SPLITS] Several FRE doctrines have active circuit
conflicts. This skill identifies the majority rule and flags circuit splits with
`[CIRCUIT-SPLIT]`. Always confirm the applicable circuit's rule before filing.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would change the theory of admissibility or exclusion
- The case is civil vs. criminal (different standards for FRE 404, 609, privilege)
- Multiple valid FRE grounds exist for the same evidence and the user must choose
- Strategic considerations (jury instruction alternatives, door-opening risk) require
  client input

Use the **CLARIFY** pattern (structured options with descriptions) wherever marked below.
If the user has already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:

- **Motion to file**: A description of the evidence the user wants excluded, plus case facts
- **Motion received**: An existing motion in limine to analyze and oppose
- **Evidence item + context**: A specific exhibit, testimony, or statement with case background
- **File**: Document containing prior deposition testimony, exhibit list, or motion brief

If no specific evidence or motion is provided, prompt the user to identify the specific
evidence at issue, the ground for exclusion, and the case context.

### Step 2: Gather Context

**CLARIFY** — Before beginning, ask the user these questions. Present as structured options:

**2.1 Mode:**

- **Draft (Offense)** — Generate arguments to exclude or limit specific evidence
- **Analyze (Defense)** — Evaluate a motion received and develop opposition arguments
- **Both** — Draft moving arguments and anticipate how to oppose if the motion is denied

_Why this matters_: The entire analytical frame inverts depending on whether the user is
seeking exclusion or fighting to admit evidence.

**2.2 Civil or Criminal Case:**

- **Civil** — Different FRE 404 and 609 standards; privilege governed partly by state law
  in diversity; no Confrontation Clause issues
- **Criminal (defendant)** — Heightened 609(a)(1) protection; Crawford overlay; Fifth
  Amendment privilege; constitutional dimension to most FRE rulings
- **Criminal (government)** — 404(b) notice obligations; heightened scrutiny on character
  evidence; Confrontation Clause applies against government

_Why this matters_: Several FRE rules have distinct civil/criminal tracks (404, 609, 410,
501). Misidentifying the case posture produces wrong arguments.

**2.3 Evidentiary Ground(s) at Issue:**
Select all that apply:

- FRE 401-403: Relevance / unfair prejudice
- FRE 404(b): Prior acts or crimes
- FRE 407: Subsequent remedial measures
- FRE 408: Settlement / compromise communications
- FRE 409: Medical expense payments
- FRE 410: Plea statements
- FRE 411: Liability insurance
- FRE 501-502: Privilege
- FRE 702: Expert testimony / Daubert
- FRE 801-807: Hearsay
- FRE 609: Prior convictions
- Other / Not sure — survey all applicable grounds

_Why this matters_: The skill generates targeted argument blocks only for grounds selected.
If "Not sure," it surveys all grounds and recommends which are viable.

**2.4 Evidence Description:**
Free text. Prompt with examples: _What is the specific evidence?_ (e.g., "prior DUI conviction
from 2019," "plaintiff's post-incident safety audit," "defendant's statement during
settlement talks," "plaintiff's expert on causation"). Include: _who is the witness or
custodian?_, _how was it obtained or will it be offered?_, _what purpose does opposing
counsel say it serves?_

_Why this matters_: Evidence-specific facts determine whether the legal standard is met
and which argument template applies.

**2.5 Filing Deadline and Procedural Posture:**

- **Pretrial conference scheduled**: Motions due before FRCP Rule 16(c) pretrial conference
- **Trial approaching**: Days/weeks to filing; prioritize strongest grounds
- **Responding to motion received**: Deadline for opposition brief
- **No immediate deadline**: Strategic planning exercise

**Default assumptions (for non-interactive runs):**

- Mode: Drafting (offense perspective)
- All applicable grounds surveyed
- Federal district court, civil case
- Jurisdiction: Federal Rules of Evidence
- Output: Argument outlines, not full brief text

### Step 3: Conduct Preliminary Procedural Screen

Before analyzing the merits, check for threshold procedural issues:

**3.1 Timing and Local Rules**

Motions in limine are not expressly addressed in the FRCP but arise from the court's
inherent authority and FRCP Rule 16(c)(2)(C)-(D). Procedure is governed by:

| Source                | Rule                                                                | What It Controls                            |
| --------------------- | ------------------------------------------------------------------- | ------------------------------------------- |
| FRCP Rule 16(c)(2)(C) | Court may "consider and take appropriate action" on controlling law | Authorizes advance evidentiary rulings      |
| FRCP Rule 16(c)(2)(D) | Limits on expert testimony under FRE 702-706                        | Specific Daubert scheduling authority       |
| Local Rules           | Filing deadlines, page limits, hearing requirements                 | Vary by district — **[VERIFY local rules]** |
| Scheduling Order      | Often sets in limine deadline at pretrial conference                | Control document for the case               |

[JURISDICTION-SPECIFIC] Local rule compliance is non-negotiable. Many districts require
motions to be filed 14-21 days before trial and limit briefing to 10-15 pages. Flag
local-rule deadline and page-limit issues before drafting.

**3.2 Scope of In Limine Relief**

Identify whether the motion seeks:

- **Complete exclusion**: All evidence on a topic excluded from trial
- **Limitation**: Evidence admissible for limited purpose only; limiting instruction under
  FRE 105 to accompany admission
- **Procedural sequencing**: Require opposing counsel to obtain advance ruling before
  referencing evidence in opening or examination
- **Precautionary relief**: Prohibit reference to a topic absent side-bar ruling

The broader the relief sought, the harder the standard. Courts generally grant in limine
motions to exclude only when the inadmissibility is clear; conditional or limiting
alternatives are common compromises.

**3.3 Effect of In Limine Ruling at Trial**

An in limine ruling is interlocutory — not final for appeal purposes. Key practical rules:

- An in limine ruling granting exclusion does NOT relieve opposing counsel of the obligation
  to make a renewed objection at trial if the excluded evidence is offered. _Luce v. United
  States_, 469 U.S. 38 (1984) [VERIFY].
- A ruling denying exclusion preserves the issue for appeal only if the proponent actually
  offers the evidence at trial and the opponent renews the objection. _Ohler v. United
  States_, 529 U.S. 753 (2000) [VERIFY] — _but note_: courts split on whether the defendant
  who preemptively introduces evidence waives appellate review. [CIRCUIT-SPLIT]
- Courts retain discretion to revisit in limine rulings as trial develops. An in limine
  order is not an irrevocable commitment.

### Step 4: Analyze Each Evidentiary Ground

For each ground identified in Step 2.3, apply the relevant legal standard and generate
an argument block. Use the **Ground Strength Classification** defined in Step 4 preamble.

---

**Ground Strength Classification**

Before analyzing any specific ground, apply this four-tier classification to each
argument:

| Classification | Criteria                                                                                                                                                                     | Recommended Action                                                               |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **STRONG**     | Legal standard clearly met; inadmissibility plain on the face of the evidence; controlling authority squarely on point; no viable counter-argument under current circuit law | File; argue strongly for full exclusion                                          |
| **VIABLE**     | Argument well-grounded in law and facts; opposition has non-frivolous counter-arguments; outcome depends on record development or judicial discretion                        | File; anticipate opposition; prepare limiting-instruction alternative            |
| **MARGINAL**   | Some legal basis but significant counter-arguments; standard not clearly met; risk of educating opposition on weaknesses                                                     | Consider filing only if combined with stronger grounds; calibrate tone carefully |
| **WEAK**       | Standard not met under current authority; filing risks Rule 11 sanction and damages credibility with court                                                                   | Do not file; document in file; address through trial objections                  |

---

#### 4.1 FRE 401-403: Relevance and Unfair Prejudice

**Legal Standard:**

FRE 401 sets a very low relevance bar: evidence is relevant if it has "any tendency" to
make a fact of consequence to the determination of the action more or less probable.
FRE 402 makes relevant evidence generally admissible. FRE 403 is the counterweight:
evidence may be excluded if its probative value is _substantially outweighed_ by danger of:
unfair prejudice, confusion of the issues, misleading the jury, undue delay, wasting time,
or needless presentation of cumulative evidence.

**Key Authority:**

- _Old Chief v. United States_, 519 U.S. 172 (1997): Government may not reject a defendant's
  offered stipulation on prior-felony element to preserve the full "narrative" at the
  cost of unfair prejudice from the conviction's nature. Probative value of the name of the
  prior offense is substantially outweighed by prejudice when the defendant offers to
  stipulate to the status element.
- _Sprint/United Management Co. v. Mendelsohn_, 552 U.S. 379 (2008): FRE 403 rulings are
  inherently context-specific; circuit courts of appeal may not adopt categorical rules of
  admissibility or exclusion — each case requires case-by-case balancing.
- Standard: "substantially outweighed" is a high bar — courts favor admissibility and
  use 403 as a last resort, not a first resort.

**Argument Block Template (Motion to Exclude — FRE 403):**

```
The [evidence at issue] should be excluded under FRE 403 because its minimal probative
value is substantially outweighed by the danger of unfair prejudice to [party].

The evidence has limited probative value: [state specifically why the evidence adds little
to a fact actually in dispute]. [Identify the contested fact of consequence under FRE 401.]
[Party] is prepared to stipulate to [the fact the evidence is offered to prove], which
eliminates any need for [the evidence]. See Old Chief v. United States, 519 U.S. 172,
184-85 (1997) [VERIFY].

The prejudice is severe: [describe specifically how jurors will misuse the evidence —
draw impermissible inferences, assess damages on improper bases, etc.]. FRE 403's danger
of "unfair prejudice" means evidence that has "an undue tendency to suggest decision on an
improper basis, commonly, though not necessarily, an emotional one." Advisory Committee
Notes to FRE 403. No curative instruction can prevent the jury from [describe the specific
harm that cannot be undone by instruction].
```

**Standard Response Arguments:**

- The "substantially outweighed" standard is stringent; marginal prejudice does not suffice
- Curative/limiting instruction under FRE 105 adequately addresses prejudice concern
- The stipulation alternative does not preserve the government's or plaintiff's right to
  present its narrative with context (_Old Chief_ applies narrowly to status-element cases)
- Evidence is highly probative because the fact in dispute is genuinely contested

---

#### 4.2 FRE 404(b): Prior Acts, Crimes, or Wrongs

**Legal Standard:**

FRE 404(b)(1) prohibits evidence of prior crimes, wrongs, or other acts to prove a person
acted in conformity therewith (propensity). FRE 404(b)(2) permits such evidence for
_non-propensity purposes_: proving motive, opportunity, intent, preparation, plan,
knowledge, identity, absence of mistake, or absence of accident.

**2020 Notice Amendment**: The amended rule requires that, in criminal cases, the
prosecution provide reasonable advance written notice of 404(b) evidence describing the
act, the permitted purpose(s), and the evidence supporting each act. [VERIFY exact
notice-deadline requirements in the applicable district's local rules.]

**Conditional Relevance Standard**: _Huddleston v. United States_, 485 U.S. 681 (1988)
held that 404(b) evidence is admitted under FRE 104(b) conditional relevance — the judge
need only find that sufficient evidence has been introduced from which the jury could find
by a preponderance that the defendant committed the prior act. No preliminary ruling by
the judge under the higher FRE 104(a) standard is required.

**Inextricably Intertwined Doctrine** [CIRCUIT-SPLIT]: Many circuits recognize a "direct
evidence" or "inextricably intertwined" exception — prior acts that form part of the
same transaction or are necessary context to explain the charged conduct are not "other
acts" under 404(b) at all, and require no 404(b) analysis. Circuits disagree on the
breadth of this doctrine.

**Argument Block Template (Motion to Exclude — FRE 404(b)):**

```
The government's [or plaintiff's] evidence of [describe the prior act] should be excluded
under FRE 404(b)(1) because it is offered solely to prove [defendant's/party's] propensity
to act in the manner alleged, not for any legitimate non-propensity purpose.

[Moving party] cannot identify a genuine non-propensity purpose: [address each claimed
purpose in FRE 404(b)(2) and explain why it does not apply given the actual facts in
dispute]. Where the prior-act evidence is offered for [claimed purpose], the evidence adds
nothing beyond the forbidden inference that [party] "acted in conformity" with a prior bad
act. See, e.g., [circuit precedent].

Even if a non-propensity purpose existed, the evidence should be excluded under FRE 403
because [prior act] is [significantly more inflammatory / less probative] than the charged
conduct. The jury cannot be expected to limit its use of [evidence] to the limited
permissible purpose — no curative instruction will prevent the prejudicial spillover.

Notice requirements: [If applicable] The prosecution has not provided timely advance notice
in compliance with FRE 404(b)(3), which independently warrants exclusion.
```

**Standard Response Arguments:**

- Articulate the specific non-propensity purpose and tie it to a genuinely disputed issue
- The evidence is "inextricably intertwined" with the charged conduct and is direct evidence,
  not a "prior act" within the rule's scope (use sparingly; flagged circuit split)
- _Huddleston_ standard is met: sufficient evidence exists to support the jury's finding
  by preponderance that the prior act occurred
- A limiting instruction under FRE 105 adequately addresses the propensity risk

---

#### 4.3 FRE 407: Subsequent Remedial Measures

**Legal Standard:**

When measures are taken after an event that, if taken before, would have made the event
less likely, those subsequent measures are not admissible to prove negligence, culpable
conduct, product defect, or failure to warn. _Admissible_ to prove ownership, control,
feasibility of precautionary measures (if controverted), or for impeachment.

**Key Issues:**

- "Subsequent" means after the harm-causing event, not after the filing of litigation
- The rule applies to the party that took the measure; not limited to the defendant
- Products liability: circuits split on whether the rule applies to manufacturing defect
  claims. [CIRCUIT-SPLIT]
- Feasibility carve-out: if the defendant claims it was infeasible to take the precaution,
  evidence of the subsequent measure becomes admissible to controvert that claim

**Argument Block Template:**

```
Plaintiff's evidence of [describe remedial measure] taken after [date of incident] should
be excluded under FRE 407 as a subsequent remedial measure. The measure was taken on [date]
— after the [accident/injury/event] that is the subject of this action — and Plaintiff
offers it to prove [negligence / product defect / failure to warn].

FRE 407 squarely prohibits this use. The policy rationale — encouraging remediation
without fear that evidence of improvements will be used as an admission of prior fault —
applies in full here: [defendant] should not be penalized for promptly correcting [the
condition]. See Advisory Committee Notes to FRE 407.

None of the rule's exceptions apply: [defendant] does not dispute ownership or control;
[defendant] has never claimed the remedial measure was infeasible; and Plaintiff does not
offer the evidence for impeachment of any specific prior statement.
```

**Standard Response Arguments:**

- The measure was taken _before_ the harm-causing event (the rule requires "subsequent")
- Feasibility is controverted: defendant has argued or implied that precautions were not
  practicable, making the subsequent measure admissible to show feasibility
- Ownership or control is at issue: defendant denies ownership; the measure is offered
  to show control over the instrumentality
- Impeachment: a specific prior inconsistent statement by a witness opens the door

---

#### 4.4 FRE 408: Compromise Negotiations

**Legal Standard:**

FRE 408 bars admission of offers to compromise, completed compromises, and statements
made during compromise negotiations when offered to prove or disprove the validity or
amount of a disputed claim or to impeach through prior inconsistent statement or
contradiction. Admissible for other purposes: proving bias or prejudice of a witness,
negating a contention of undue delay, or proving an effort to obstruct criminal
investigation or prosecution.

**Scope Limits:**

- Requires a _claim_ — a dispute must exist or be anticipated; FRE 408 does not protect
  pre-dispute business negotiations
- Applies only to offers and statements made _in connection with_ compromise negotiations —
  independent facts or documents do not become protected merely because they are mentioned
  in a settlement communication
- Rule 408(a)(2) covers "conduct or statement" made in compromise negotiations; this
  includes attorneys' statements as well as parties' statements

**Argument Block Template:**

```
[Party]'s statement that "[quote]," made in [describe the negotiation context], is
inadmissible under FRE 408(a)(2) as a statement made "in connection with" compromise
negotiations of [describe the disputed claim]. [Moving party] made this statement during
[describe the settlement discussion] in a clear attempt to resolve [the dispute] — the
statement cannot be introduced to prove [validity of claim / amount / to impeach the witness].

The "in connection with" requirement is satisfied: [describe how the statement was made
in a negotiation context, not as a separate operative admission].

None of the FRE 408(b) exceptions apply: [party] does not assert undue delay; no criminal
investigation is involved; the statement is not offered to prove bias through a separate
witness's prior statement.
```

**Standard Response Arguments:**

- No "claim" existed at the time — the communication was ordinary business negotiation,
  not compromise of a disputed legal claim
- The statement is offered for an independent purpose under FRE 408(b): [identify the
  specific non-prohibited purpose — bias, undue delay, obstruction]
- The underlying fact existed independently and would have been discoverable outside the
  negotiation; FRE 408 does not make independently provable facts inadmissible

---

#### 4.5 FRE 409: Payment of Medical Expenses

**Legal Standard:**

Evidence of paying or offering to pay medical, hospital, or similar expenses caused by
an injury is not admissible to prove liability. The rule is narrow: it excludes only the
offer or payment itself, _not_ accompanying statements made in connection with the offer
or payment. A defendant who says "I'll pay your hospital bill — I'm so sorry, this was
all my fault" loses the apology but keeps the liability exclusion only for the payment
offer itself.

**Argument Block Template:**

```
Evidence that [defendant] [paid / offered to pay] [plaintiff]'s medical expenses of
[$amount] is inadmissible under FRE 409 to prove liability. Such payments are expressly
excluded because their admission would deter humanitarian aid to injured persons.
FRE 409 applies to the offer or payment and [moving party] limits the motion to that
discrete item. [If applicable: Any accompanying statements are addressed separately
under FRE 401-403.]
```

**Standard Response Arguments:**

- FRE 409 is narrow; any statements made alongside the payment offer are not protected
  and remain admissible
- The payment was made pursuant to a contractual obligation, not as a humanitarian gesture,
  distinguishing the policy rationale

---

#### 4.6 FRE 410: Plea Statements

**Legal Standard:**

In civil and criminal cases, the following are inadmissible against the defendant who
made the plea or statement: (1) a guilty plea that was later withdrawn; (2) a nolo
contendere plea; (3) a statement made during a Rule 11 proceeding concerning either
plea (if the plea was later withdrawn); (4) a statement made during plea-bargain
discussions with a prosecuting attorney that did not result in a guilty plea, or that
resulted in a later-withdrawn guilty plea.

**Exceptions**: Admissible in a criminal proceeding for perjury or false statement if
the statement was made under oath, on the record, and with counsel present; or when
another statement made in the same plea discussion has been introduced and fairness
requires consideration of both.

**Argument Block Template:**

```
[Defendant]'s statement that "[quote]" was made during [describe the plea discussion /
Rule 11 proceeding] and is inadmissible under FRE 410(a)(4). The statement was made
during discussions with [prosecuting attorney] concerning [the charged offense], and [the
discussions did not result in a guilty plea / the resulting guilty plea was withdrawn].

FRE 410 is categorical: the statement may not be used against [defendant] in this
proceeding. No exception applies: this is not a perjury proceeding; the statement was
[not made under oath in a formal proceeding / does not require consideration for fairness
as a companion to another statement introduced].
```

**Standard Response Arguments:**

- The statement was made to law enforcement before any formal plea discussions with a
  prosecuting attorney; FRE 410 does not cover general statements to agents
- The perjury exception applies: the statement was under oath, on the record, with counsel
- The defendant introduced a related statement during the same plea discussion, making this
  statement admissible for completeness under FRE 410(b)(2)

---

#### 4.7 FRE 411: Liability Insurance

**Legal Standard:**

Evidence that a person was or was not insured against liability is not admissible to
prove whether the person acted negligently or otherwise wrongfully. Admissible to prove:
agency, ownership, or control; bias or prejudice of a witness.

**Argument Block Template:**

```
Evidence that [defendant] carried liability insurance in the amount of [$amount] with
[insurer] is inadmissible under FRE 411 to prove that [defendant] acted negligently or
otherwise wrongfully. The rule bars this inference categorically.

[If opposing counsel intends to use it for another purpose]: If [party] intends to offer
the insurance evidence for [stated purpose], a limiting instruction does not adequately
prevent the jury from drawing the forbidden inference. [Moving party] requests that the
evidence be excluded in its entirety or that the court require proponent to establish an
admissible purpose outside the jury's presence before introduction.
```

**Standard Response Arguments:**

- Evidence is offered for a permitted purpose — agency, ownership, or control is at issue
- Bias of a witness who has a financial interest in the outcome is a recognized exception
- Insurance coverage establishes an agency relationship between the insured and the insurer
  relevant to a claim of apparent authority

---

#### 4.8 FRE 501-502: Privilege

**Legal Standard:**

FRE 501: In federal-question cases, privilege is governed by federal common law. In
diversity or supplemental-jurisdiction cases where state law governs an element of a
claim or defense, state privilege law applies. Federal common law recognizes: attorney-client
privilege, work product doctrine (_Hickman v. Taylor_, 329 U.S. 495 (1947) [VERIFY]),
marital communications privilege, and psychotherapist-patient privilege (_Jaffee v.
Redmond_, 518 U.S. 1 (1996) [VERIFY]).

FRE 502: Governs inadvertent waiver — disclosure of privileged attorney-client
communications or work product does not waive privilege as to undisclosed material if:
the disclosure was inadvertent, the holder took reasonable steps to prevent it, and the
holder promptly took reasonable steps to rectify the error. A 502(d) federal-court order
protects against waiver in all federal and state proceedings.

**Work Product Doctrine:** Two tiers — ordinary work product (fact work product, protected
but discoverable on showing of substantial need and inability to obtain without undue
hardship) and opinion work product (attorney's mental impressions, conclusions, opinions,
legal theories — near-absolute protection).

**Argument Block Template (Attorney-Client Privilege):**

```
[Document / communication] is protected from disclosure by the attorney-client privilege.
The communication was made by [client / agent] to [attorney / agent of attorney], in
confidence (no third parties), for the purpose of obtaining legal advice concerning
[subject matter]. All elements of the privilege are satisfied.

[Moving party] did not waive the privilege: [no prior disclosure / any disclosure was
inadvertent and promptly remedied under FRE 502(b) / a court order under FRE 502(d)
entered on [date] governs non-waiver]. The privilege is not vitiated by any crime-fraud
exception because [opposing party has not made a prima facie showing that the communication
was made in furtherance of a crime or fraud].
```

**Standard Response Arguments:**

- The communication was not made in confidence — a third party was present who was not an
  agent of either the attorney or client
- The communication was not for the purpose of legal advice; it was ordinary business advice
  from an in-house attorney acting in a business role
- Privilege was waived by voluntary disclosure to [third party / opposing counsel / public]
- Crime-fraud exception applies: show probable cause that the communication was made to
  further a crime or fraud
- Work product: show substantial need and inability to obtain equivalent material without
  undue hardship (ordinary work product only; opinion work product remains near-absolutely
  protected)

---

#### 4.9 FRE 702: Expert Testimony and Daubert Gatekeeping

**Legal Standard:**

FRE 702 (as amended December 1, 2023) requires that:

1. The expert's scientific, technical, or other specialized knowledge will **help** the
   trier of fact to understand the evidence or determine a fact in issue
2. The testimony is **based on sufficient facts or data**
3. The testimony is the product of **reliable principles and methods**
4. The expert's opinion **reflects a reliable application** of the principles and methods
   to the facts of the case

**2023 Amendment key clarification**: The proponent must **demonstrate** to the court by
a **preponderance of the evidence** that all requirements are met. The court must "carefully"
exercise its gatekeeping function. The amendment was intended to combat courts deferring to
experts too readily — if the expert's opinion does not reliably follow from the data and
the methodology, it should be excluded.

**Daubert Trilogy:**

- _Daubert v. Merrell Dow Pharmaceuticals, Inc._, 509 U.S. 579 (1993): The four factors
  (testing, peer review, error rates, general acceptance) are illustrative, not exclusive
- _General Electric Co. v. Joiner_, 522 U.S. 136 (1997): Abuse of discretion on appeal;
  a "too great an analytical gap between the data and the opinion" is a sufficient basis
  for exclusion
- _Kumho Tire Co. v. Carmichael_, 526 U.S. 137 (1999): Daubert applies to all expert
  testimony, not just scientific testimony; "technical and other specialized knowledge"
  experts are subject to the same gatekeeping

**Three Attacks on Expert Testimony:**

1. **Qualification**: Does the expert have the specific knowledge, skill, experience,
   training, or education for the opinion offered? (General expertise in a field is
   insufficient if the specific opinion requires specialized sub-field expertise)
2. **Methodology**: Is the expert's method reliable? (Apply the Daubert factors; check
   for analytical gaps under _Joiner_)
3. **Fit**: Does the expert's opinion actually address a fact in issue? Is it sufficiently
   tied to the specific facts of the case? (The fit requirement excludes speculative
   or unhelpful opinions)

**Argument Block Template (Daubert Motion to Exclude Expert):**

```
[Defendant / Plaintiff] moves to exclude the expert testimony of [Name], [credentials],
designated by [opposing party] to testify regarding [opinion topic].

I. [Expert] Lacks Qualification for the Specific Opinion Offered.
[Expert]'s general expertise in [field] does not qualify [Expert] to opine on [the
specific sub-topic]. The opinions require [specific sub-field expertise, experience,
or credentials], which [Expert] does not possess. [Cite specific credential gaps from
Expert's CV and deposition testimony.]

II. [Expert]'s Methodology Is Unreliable.
[Expert]'s opinion that [state the conclusion] rests on methodology that fails Daubert
scrutiny:
- Testing: [Expert]'s method has not been tested / cannot be tested
- Peer review: [Expert]'s method has not been subject to peer review or publication
- Error rate: [Expert] has not identified or considered the known error rate of the method
- General acceptance: [Expert]'s methodology is not generally accepted in [field]
- Analytical gap: [Expert] leaps from [data] to [conclusion] without adequate
  explanation — "too great an analytical gap" under Joiner, 522 U.S. at 146 [VERIFY]

III. [Expert]'s Opinion Does Not Fit the Facts of This Case.
[Expert]'s opinion was formed [in a different context / based on different data /
addressing a different question] from that at issue here. The opinion requires the jury
to bridge a gap between [the data Expert relied on] and [the contested issue in this
case] that FRE 702's "fit" requirement bars.

Under the 2023 amendment to FRE 702, [opposing party] bears the burden to demonstrate
by a preponderance of the evidence that each element of Rule 702 is satisfied. [Opposing
party] cannot meet that burden for the reasons set forth above.
```

**Standard Response Arguments:**

- Qualification: General expertise in the field is sufficient; "[Expert]'s experience
  across [related areas] equips [Expert] to address [the specific sub-topic]"
- Methodology: Courts should not exclude expert testimony merely because they disagree
  with the expert's conclusions; _Daubert_ tests the process, not the outcome
- Fit: Any gap between the data and the opinion goes to weight, not admissibility, under
  _Joiner_ — the "too great an analytical gap" standard does not require every inferential
  step to be spelled out
- Cross-examination and competing expert testimony are the appropriate tools for
  challenging reliability, not exclusion

---

#### 4.10 FRE 801-807: Hearsay

**Legal Standard:**

FRE 801 defines hearsay as an out-of-court statement by a declarant offered for the
truth of the matter asserted. Key concepts:

**Non-Hearsay Uses (Not Offered for Truth):**

- Verbal acts: statements whose utterance itself creates legal consequences (operative words)
- Effect on listener: offered to show what the recipient knew or believed, not to prove
  the truth of the statement's content
- Prior inconsistent statements offered solely for impeachment (not substantive use)
- Legally operative words (contract formation, defamation, notice)

**FRE 801(d) — Defined as Not Hearsay:**

- 801(d)(1)(A): Prior inconsistent statement made under oath — admissible substantively
- 801(d)(1)(B): Prior consistent statement — admissible to rehabilitate after charge of
  recent fabrication or improper influence (timing requirement: must predate the motive
  to fabricate)
- 801(d)(1)(C): Prior statement of identification
- 801(d)(2): Admission by party-opponent — own statement, adoptive admission, authorized
  statement, agent/employee admission within scope, co-conspirator statement

**Key FRE 803 Exceptions (Declarant Availability Immaterial):**

| Exception                                | Requirement                                                                             | Common Attack                                             |
| ---------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Present sense impression (803(1))        | Made while perceiving or immediately after                                              | Timing; declarant must be the perceiver                   |
| Excited utterance (803(2))               | Made while under stress of startling event                                              | Staleness of excitement; coaching                         |
| Then-existing state of mind (803(3))     | Shows declarant's then-existing intent, plan, motive                                    | Backwards-looking statements excluded                     |
| Statement for medical diagnosis (803(4)) | Made for diagnosis or treatment; reasonably pertinent                                   | Non-medical portions; motive to fabricate                 |
| Business records (803(6))                | Regular business activity; made at or near the time; qualified witness; trustworthiness | Prepared in anticipation of litigation; untrustworthiness |
| Public records (803(8))                  | Public office's activities; matters observed or investigated                            | Law enforcement reports in criminal cases (803(8)(A)(ii)) |

**Key FRE 804 Exceptions (Declarant Must Be Unavailable):**

- Former testimony (804(b)(1)): Prior testimony at hearing/trial/deposition with predecessor
  in interest having opportunity and motive to develop testimony
- Dying declaration (804(b)(2)): Belief of imminent death; criminal homicide or civil case
- Statement against interest (804(b)(3)): Against declarant's pecuniary, proprietary, or
  penal interest
- Forfeiture by wrongdoing (804(b)(6)): Party procured declarant's unavailability

**FRE 807 Residual Exception**: Requires equivalent circumstantial guarantees of
trustworthiness; offered as evidence of a material fact; more probative than other
reasonably obtainable evidence; admission serves the interests of justice; notice required.

**Crawford / Confrontation Clause Overlay (Criminal Cases Only):**
_Crawford v. Washington_, 541 U.S. 36 (2004): The Confrontation Clause bars admission of
_testimonial_ hearsay statements against a criminal defendant unless the declarant is
unavailable AND the defendant had a prior opportunity to cross-examine.

_Davis v. Washington_, 547 U.S. 813 (2006) — Primary Purpose Test: A statement is
**testimonial** if its primary purpose is to establish or prove past events relevant to
prosecution. A statement is **non-testimonial** if its primary purpose is to enable
police to respond to an ongoing emergency.

_Michigan v. Bryant_, 562 U.S. 344 (2011): Ongoing emergency extends non-testimonial
characterization when an objective observer would conclude the primary purpose is
addressing the emergency.

**Argument Block Template (Motion to Exclude Hearsay):**

```
[Party]'s exhibit [X] / testimony of [Witness] regarding the statement "[quote]" is
inadmissible hearsay under FRE 802. The statement is an out-of-court statement by
[Declarant], offered for the truth of the matter asserted — specifically, to prove that
[state what proponent claims the statement proves].

No exception or exemption applies:
- FRE 801(d)(2) admission by party-opponent: [Declarant] is not [party] and was not [party]'s
  authorized agent / employee acting within the scope of employment / co-conspirator during
  the course and furtherance of the conspiracy at the time of the statement.
- FRE 803(6) business records: The document was not prepared in the ordinary course of
  regularly conducted business activity — it was prepared in anticipation of litigation
  by [identify who prepared it and why], which defeats the reliability rationale for
  the exception. See Palmer v. Hoffman, 318 U.S. 109 (1943) [VERIFY].
- FRE 803(2) excited utterance: The statement was made [time period] after the event —
  sufficient time had elapsed that [Declarant] was no longer "under the stress of
  excitement" caused by the startling event.
[Address any other exception raised or anticipated.]
```

**Standard Response Arguments:**

- Non-hearsay use: the statement is not offered for the truth; it is offered to show
  [effect on listener / verbal act / notice to party]
- 801(d)(2) admission: [Declarant] was [party's] authorized agent / acting within the
  scope of employment / co-conspirator; establish agency or conspiracy at the FRE 104(a)
  preponderance level
- 803(6) business records: The document was made and kept in the course of regularly
  conducted activity; the litigation-preparation exception requires more than mere
  awareness that litigation might occur
- Crawford does not apply in civil cases; and in criminal cases the statement is
  non-testimonial because its primary purpose was [responding to emergency / not to
  establish past events for prosecution]

---

#### 4.11 FRE 609: Prior Convictions for Impeachment

**Legal Standard:**

FRE 609 governs impeachment of a witness's credibility by evidence of prior criminal
convictions:

**609(a)(1) — Felony (Offense Punishable by More Than One Year):**

- Witness _other_ than accused in criminal case: admissible if probative value **outweighs**
  prejudicial effect to the party (low bar — probative value need only outweigh, not
  substantially outweigh)
- **Accused** in criminal case: admissible only if probative value **substantially outweighs**
  prejudicial effect (higher bar; mirrors FRE 403 but reversed — prejudice must be the
  starting point)

**609(a)(2) — Crimes of Dishonesty (Crimen Falsi):**
Convictions for crimes involving **dishonest act or false statement** must be admitted
regardless of any balancing — the court has no discretion. Examples: perjury, false
statement, fraud, embezzlement, theft involving deceit. Examples of crimes that do NOT
qualify: simple assault, drug possession, robbery without fraud element [VERIFY circuit-
specific tests for robbery and theft offenses — circuits split on whether "dishonesty"
requires a specific element of deceit]. [CIRCUIT-SPLIT]

**609(b) — Convictions More Than 10 Years Old:**
Admissible only if: (1) probative value **substantially outweighs** prejudicial effect
**and** (2) advance written notice is provided and the court finds admission is in the
interests of justice.

**609(c)**: Annulled, pardoned, or rehabilitated — generally not admissible.
**609(d)**: Juvenile adjudications — not admissible in civil cases; in criminal cases,
admissible only if court finds it would be admitted under 609(a) for an adult and admission
is necessary for a fair determination.
**609(e)**: Pendency of appeal does not make conviction inadmissible (goes to weight).

**Argument Block Template (Motion to Exclude Prior Conviction — 609(b) / 10-Year Bar):**

```
[Opposing party] should be precluded from using [witness]'s [describe conviction, year]
conviction under FRE 609(b). The conviction is more than ten years old, measured from
the date of conviction or release from confinement (whichever is later). See FRE 609(b).

Under FRE 609(b), a conviction beyond the ten-year limit is admissible only if its
probative value substantially outweighs its prejudicial effect — a demanding standard
that the Ninth Circuit has [describe circuit-specific approach] [VERIFY circuit law].
[Opposing party] cannot make this showing because:
(1) The conviction — [describe] — bears [minimal / no] relationship to truthfulness or
    accuracy of the witness's testimony in this case;
(2) The passage of [N] years makes the conviction stale and its probative value attenuated;
(3) The prejudice to [moving party] from introducing a [N]-year-old conviction is
    substantial — it risks [describe specific harm: distraction, undue sympathy against
    the defendant, confusion with the charged conduct];
(4) [Opposing party] has not provided the advance written notice required by FRE 609(b).
```

**Standard Response Arguments:**

- The conviction is within the ten-year window; the 609(b) heightened standard does not apply
- The conviction involves dishonesty under 609(a)(2) — mandatory admission with no
  balancing regardless of age (if within 10 years; 609(b) still applies beyond 10 years)
- For convictions close to the 10-year line: probative value substantially outweighs
  prejudice because the witness is testifying about recent events; conviction demonstrates
  ongoing character for dishonesty
- Circuit precedent in [circuit] applies a broader definition of "dishonest act" to include
  [robbery / theft] convictions

---

### Step 5: Assess Standard Response and Opposition Arguments

For each ground analyzed in Step 4, synthesize the available response arguments. Apply
the following universal response toolkit in addition to ground-specific arguments:

**Universal Response Arsenal:**

| Tool                  | Rule                    | When to Deploy                                                                              |
| --------------------- | ----------------------- | ------------------------------------------------------------------------------------------- |
| Limiting instruction  | FRE 105                 | Evidence admitted for one purpose but not another; request a tailored instruction           |
| Conditional relevance | FRE 104(b)              | Admissibility depends on a preliminary fact; ask court to admit subject to later connection |
| Offer of proof        | FRE 103(b)              | Preserve excluded evidence for appeal; prevent forfeiture of the objection                  |
| Door-opening doctrine | Common law / discretion | Moving party's opening statement or prior evidence opens the door to the excluded evidence  |
| Curative instruction  | Discretion              | Jury instruction can address the prejudice risk without total exclusion                     |
| Completeness          | FRE 106                 | When opponent introduces part of a writing or recording, admit the remainder as necessary   |

**Limiting Instruction Strategy (FRE 105):**

Where the moving party seeks total exclusion but the court is inclined to admit for a
limited purpose, propose a specific limiting instruction that: (1) names the permissible
purpose, (2) names the forbidden use, and (3) directs the jury specifically. Weak limiting
instructions ("consider this only for [vague purpose]") are rarely effective — a precise
instruction tailored to the specific evidence and issue is more persuasive to courts
evaluating whether exclusion is necessary.

**Door-Opening Doctrine:**

If the moving party's own opening statement, examination, or introduced evidence opens
the subject matter that the court previously excluded, the opponent may seek permission
to introduce the previously excluded evidence. Anticipate the door-opening risk when
crafting the scope of the motion — a motion that is too broad may be undercut if the
moving party's trial conduct opens the door.

### Step 6: Anticipatory Opposition Analysis

For each ground classified VIABLE or STRONG, identify the three most likely opposition
arguments and develop pre-emptive rebuttals:

**Format for each ground:**

```
Ground: FRE [rule number] — [brief description]
Classification: [STRONG / VIABLE / MARGINAL / WEAK]
Confidence: [0.XX]

Opposition Arg 1: [State the argument opposing counsel will make]
→ Rebuttal: [State the specific answer]

Opposition Arg 2: [State the argument]
→ Rebuttal: [State the specific answer]

Opposition Arg 3: [State the argument]
→ Rebuttal: [State the specific answer]

Reply Focus: [What the reply brief should emphasize — the strongest rebuttal, the
authority the opposition will not have a good answer for]
```

### Step 7: Draft Argument Blocks

For each STRONG or VIABLE ground, produce a complete argument block using the templates
from Step 4. Argument blocks should:

1. Open with the legal standard, precisely stated with citation
2. Apply the standard to the specific facts of the case
3. Address each element of the ground in sequence
4. Anticipate and pre-empt the one or two strongest opposition arguments
5. Close with a prayer for relief that is calibrated to the classification (total exclusion
   for STRONG; exclusion or, alternatively, limiting instruction for VIABLE)

**Argument Ordering — Prioritization Framework:**

| Tier       | Criteria                                                                                                                                                                  | Placement                                      |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **Tier 1** | STRONG classification; constitutional dimension (Confrontation Clause, Due Process); most prejudicial evidence if admitted; outcome-determinative on liability or damages | Lead argument; separate section heading        |
| **Tier 2** | VIABLE classification; significant prejudice risk; clear statutory bar with well-settled exceptions                                                                       | Second; middle sections                        |
| **Tier 3** | MARGINAL classification; cumulative or alternative grounds; preserving issues for appeal                                                                                  | Last; clearly labeled as alternative arguments |

MARGINAL grounds should be filed, if at all, in the alternative: "Even if the Court
finds [Evidence] admissible on [Tier 1 ground], the Court should nonetheless exclude
it under FRE [403 / 404(b) / etc.] for the following independent reasons."

Do not list WEAK grounds in the motion. Filing WEAK arguments dilutes the credibility
of STRONG ones and invites Rule 11 scrutiny.

### Step 8: Apply Quality Frameworks

**Run all three frameworks silently before delivering any output. If any gate fails, revise before delivering.**

---

## Citation Quality Gates

Run these 5 gates before delivering:

| Gate           | Rule                                                                                            | Fail Action                            |
| -------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------- |
| **Source**     | Every legal claim cites a specific FRE rule, SCOTUS or circuit case, or Advisory Committee Note | Add citation or mark `[UNVERIFIED]`    |
| **Format**     | Citations follow consistent format: _Case Name_, volume F.R.D./F.2d/F.3d/U.S. page (Year)       | Fix format                             |
| **Currency**   | Cited cases and rules checked for amendment or overruling — especially FRE 702 (2023 amendment) | Flag `[CHECK CURRENCY]`                |
| **Domain**     | Analysis correctly identifies circuit-wide vs. circuit-specific vs. split rules                 | Flag `[CIRCUIT-SPLIT]`                 |
| **Confidence** | Uncertainty explicitly stated; no overconfident predictions on discretionary rulings            | Add confidence qualifier or `[VERIFY]` |

---

## Self-Interrogation for STRONG-Classified Grounds

For any ground classified STRONG, apply this 3-pass review before including it in output:

**Pass 1 — Legal Chain Integrity**: Does the exclusion argument follow logically from the
cited authority? Would a federal district judge actually grant a motion to exclude on this
basis given the specific facts? Are there limiting principles from _Sprint/United Management_
(context-dependency of 403 rulings) or similar cases that apply?

**Pass 2 — Completeness**: Have all potential carve-outs, exceptions, and counter-theories
been considered? Is there a realistic theory of admissibility for a non-propensity purpose
(404(b)), a non-hearsay use (801-807), a legitimate purpose exception (408, 409, 411)?

**Pass 3 — Challenge**: What is the strongest argument opposing counsel will make? Does
the argument block adequately pre-empt it? Under what circumstances might the court admit
the evidence in a limited form with a FRE 105 limiting instruction instead of excluding it?

If STRONG classification cannot survive all three passes, downgrade to VIABLE and revise
the argument tone accordingly.

---

## Confidence Scoring

| Level        | Range     | Meaning                                                                                           | Action                                            |
| ------------ | --------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law; SCOTUS authority directly on point; clear statutory bar with no recognized exception | State with confidence                             |
| **High**     | 0.80–0.94 | Strong circuit authority; well-settled doctrine; minor questions on application to specific facts | State with brief caveat                           |
| **Probable** | 0.60–0.79 | Good arguments; circuit split or analogical reasoning required; outcome depends on record         | State with reasoning and contra-indicators        |
| **Possible** | 0.40–0.59 | Genuinely uncertain; novel application; result depends heavily on judicial discretion             | Flag for counsel review with both sides presented |
| **Unlikely** | 0.0–0.39  | Weak basis; current circuit authority against the position; filing risks Rule 11                  | Do not assert; flag `[UNCERTAIN]`                 |

---

## Anti-Patterns

The following are specific, recurring errors in motion in limine practice. Avoid each.

1. **Filing a 403 motion as a first resort.** FRE 403 is a last resort — courts disfavor
   excluding evidence solely on unfair prejudice grounds because almost all damaging
   evidence is "prejudicial." Reserve 403 arguments for evidence whose prejudice is
   demonstrably severe and whose probative value is genuinely minimal.

2. **Conflating "prejudicial" with "unfairly prejudicial."** All evidence against a party
   is prejudicial in the colloquial sense. FRE 403 requires that the prejudice be _unfair_
   — that it operates through an illegitimate route (e.g., emotional appeal, propensity
   inference, confusion of issues). Failing to articulate the _unfairness_ of the prejudice
   is the most common 403 argument failure.

3. **Overstating the Old Chief stipulation doctrine.** _Old Chief_ applies narrowly when
   a defendant offers to stipulate to a status element (e.g., prior felony for § 922(g))
   and the government seeks to admit the conviction to prove that element. It does not
   entitle any party to substitute a stipulation for any evidence at any time.

4. **Ignoring the 2020 FRE 404(b) notice amendment in criminal cases.** The 2020
   amendment requires prosecutors to provide advance written notice specifying the act,
   the permitted purpose, and the supporting evidence. Failure to move to exclude on notice
   grounds waives the argument. Always check whether proper notice was given in criminal
   cases.

5. **Filing a 404(b) motion without identifying what the actual permissible purpose is.**
   Courts do not grant 404(b) motions that merely argue "propensity." The movant must
   demonstrate that no genuine non-propensity purpose exists — which requires engaging
   with the specific purpose(s) the proponent claims. Failure to engage with claimed
   purposes is a losing motion.

6. **Misreading FRE 408's scope in business disputes.** FRE 408 protects statements made
   _in connection with_ compromise of a _disputed claim_. Many inter-party communications
   before litigation is threatened are ordinary business negotiations, not protected
   compromise discussions. Seeking exclusion of pre-dispute business communications under
   FRE 408 is a common and losing argument.

7. **Treating FRE 409 as a broad mediation privilege.** FRE 409 protects only the offer
   or payment of medical expenses — not accompanying statements, admissions, or apologies.
   Moving to exclude an accompanying apology under FRE 409 (rather than 408 or 403) will
   fail.

8. **Failing to address Daubert fit separately from methodology.** Many Daubert motions
   attack only the expert's methodology. _Fit_ — whether the expert's opinion actually
   addresses the specific factual issue in the case — is an independent ground and often
   the stronger one. Identify both.

9. **Failing to use the 2023 FRE 702 amendment's burden-shifting language.** The 2023
   amendment explicitly places the burden on the _proponent_ to demonstrate admissibility
   by a preponderance. Failing to invoke this language in a Daubert motion concedes the
   burden-framing to the proponent.

10. **Filing a Daubert motion before a full deposition record.** Daubert motions succeed
    when they are grounded in specific deposition testimony, report admissions, and
    identified methodological failures. A pre-deposition Daubert motion based solely on
    the expert report lacks the evidentiary foundation to prevail and wastes the motion.

11. **Misidentifying hearsay vs. non-hearsay uses.** The most common hearsay error is
    arguing that a statement is hearsay when it is offered for its effect on the listener,
    as a verbal act, or for notice. Conversely, accepting a proponent's "effect on
    listener" or "verbal act" characterization without scrutinizing whether the statement's
    truth is actually relevant to the claimed non-hearsay purpose.

12. **Missing the FRE 803(6) litigation-preparation exception.** A document prepared in
    anticipation of litigation — even if created by a company's regular department — loses
    the business records exception's trustworthiness rationale. Documents created after
    the incident that triggered litigation (incident reports, root-cause analyses prepared
    at counsel's direction) are frequently excluded. The litigation-preparation attack is
    underused.

13. **Overlooking the FRE 609(a)(2) crimen falsi mandatory admission rule.** If the
    prior conviction is for a crime involving dishonest act or false statement, there is
    no balancing and no discretion — the conviction _must_ be admitted. Filing a motion
    in limine to exclude a crimen falsi conviction is frivolous. Know your circuits'
    definition of which crimes qualify.

14. **Failing to provide written notice for FRE 609(b) convictions.** For convictions
    more than 10 years old, FRE 609(b) requires advance written notice in addition to
    satisfying the heightened balancing test. Proponents who fail to give notice will
    have the conviction excluded regardless of its probative value.

15. **Seeking exclusion of criminal conviction evidence in civil cases under the wrong
    standard.** In civil cases, a non-party witness's prior conviction is subject to the
    lower FRE 609(a)(1) standard (probative value need only outweigh, not substantially
    outweigh, prejudicial effect). Movants who argue the more demanding "substantially
    outweighs" standard set for criminal defendants will be applying the wrong rule.

16. **Failing to renew the trial objection after a denied in limine motion.** A ruling
    denying a motion in limine does not automatically preserve the issue for appeal. When
    the evidence is offered at trial, a timely renewed objection is required. Failure to
    renew forfeits the issue. Counsel must instruct trial teams on renewal obligations.

17. **Moving in limine to exclude entire categories of evidence rather than specific items.**
    Motions to exclude "all evidence of prior accidents" or "any mention of [topic]" are
    facially overbroad and invite denial. Courts prefer and grant narrowly tailored motions
    that identify specific exhibits, witnesses, or statements. Overbroad motions create
    adverse-credibility risk with the court.

18. **Ignoring the Crawford / Davis framework in criminal cases involving police reports
    and 911 calls.** Not all out-of-court statements are hearsay issues — some are
    Confrontation Clause issues. Police reports prepared for investigative purposes are
    generally testimonial under _Crawford_ and inadmissible against a criminal defendant
    absent unavailability plus prior cross-examination opportunity, regardless of whether
    any hearsay exception applies. Litigating this as a hearsay issue rather than a
    Confrontation Clause issue results in the wrong analysis and potentially lost arguments.

---

## Writing Standards

1. **Legal standard first.** Every argument section opens with the governing standard,
   precisely stated with citation. Courts must be able to identify the applicable rule
   and standard within the first two sentences of each argument.

2. **Precision over length.** Delete throat-clearing. "The Court should exclude the
   statement because..." not "As set forth more fully below and as will be demonstrated
   throughout this memorandum, the Court should exclude the statement because..."

3. **Active voice.** "The probative value does not substantially outweigh the unfair
   prejudice" not "Exclusion is warranted because the probative value is not substantially
   outweighed."

4. **Quote the rule accurately with pinpoint citation.** FRE exclusion motions succeed
   when the court can see the exact language of the rule and the exact facts that violate
   it. Quote the operative rule text; do not paraphrase.

5. **Do not overstate the classification.** Avoid language like "clearly," "obviously,"
   and "plainly" for VIABLE arguments. Reserve strong language for STRONG-classified
   grounds that have passed the 3-pass Self-Interrogation.

6. **Calibrate the prayer for relief to the classification.** STRONG: request exclusion
   with prejudice. VIABLE: request exclusion, or alternatively a limiting instruction and
   offer of proof. MARGINAL: request limiting instruction or sequenced ruling before trial.

7. **One argument per rule; cross-references for compound grounds.** A motion to exclude
   evidence on both FRE 404(b) and FRE 403 grounds should have separate argument sections
   with a cross-reference: "Even if the evidence were admissible under FRE 404(b), it
   should be excluded under FRE 403 for the independent reasons set forth in Argument II."

8. **Avoid loaded rhetoric.** "The evidence is irrelevant," not "this transparent attempt
   to inflame the jury." State the legal deficiency precisely; courts are unpersuaded by
   advocacy about opposing counsel's motives.

**Quality gate before delivery:**

- [ ] Each cited case has year, volume, and reporter page number (or marked `[VERIFY]`)
- [ ] Circuit splits are identified as such and not presented as universal rules
- [ ] All STRONG-classified grounds have passed the Self-Interrogation 3-pass review
- [ ] The prayer for relief is calibrated to the classification tier for each ground
- [ ] Local rule compliance flags (filing deadline, page limit) are included

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for the specific FRE rule's current text and Advisory Committee Notes
- Search for circuit-specific case law on the doctrine at issue
- Verify that key anchor cases (Daubert, Crawford, Old Chief, Huddleston) have not been
  limited or overruled in the applicable circuit
- Search for district-specific local rules on motion in limine procedure and page limits
- Save research results to `/tmp/legalcode-motion-in-limine-research.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed using the authority embedded in this skill
- Mark all statutory and case law references with `[VERIFY]`
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Focus on structural quality, argument framework, and identifying grounds — counsel must
  independently verify all authority before filing

---

## Glass Box Audit Trail

Every output should include a completed audit trail in the following format:

```yaml
glass_box:
  skill_name: "legalcode-motion-in-limine"
  mode: "Drafting | Analysis | Both"
  case_caption: "[Plaintiff v. Defendant, No. ___]"
  court: "[e.g., S.D.N.Y., N.D. Cal.]"
  circuit: "[e.g., Second Circuit, Ninth Circuit]"
  case_type: "Civil | Criminal (defendant) | Criminal (government)"
  grounds_analyzed:
    - "FRE 401-403: [brief description of evidence at issue]"
    - "FRE 404(b): [brief description]"
    - "FRE 702: [expert name and opinion topic]"
    - "[one entry per ground actually analyzed]"
  grounds_classification:
    "FRE 401-403": "STRONG | VIABLE | MARGINAL | WEAK | Not Analyzed"
    "FRE 404(b)": "STRONG | VIABLE | MARGINAL | WEAK | Not Analyzed"
    "FRE 407": "STRONG | VIABLE | MARGINAL | WEAK | Not Analyzed"
    "FRE 408": "STRONG | VIABLE | MARGINAL | WEAK | Not Analyzed"
    "FRE 409": "STRONG | VIABLE | MARGINAL | WEAK | Not Analyzed"
    "FRE 410": "STRONG | VIABLE | MARGINAL | WEAK | Not Analyzed"
    "FRE 411": "STRONG | VIABLE | MARGINAL | WEAK | Not Analyzed"
    "FRE 501-502": "STRONG | VIABLE | MARGINAL | WEAK | Not Analyzed"
    "FRE 702": "STRONG | VIABLE | MARGINAL | WEAK | Not Analyzed"
    "FRE 801-807": "STRONG | VIABLE | MARGINAL | WEAK | Not Analyzed"
    "FRE 609": "STRONG | VIABLE | MARGINAL | WEAK | Not Analyzed"
  self_interrogation_applied: "Yes — [grounds] | N/A"
  local_rules_checked: "[District local rules reviewed; specific rules applied or 'Not checked — flag for counsel']"
  filing_deadline: "[Date or 'Unknown — verify scheduling order']"
  legalcode_mcp: "Connected | Not connected"
  citations_verified: "[N VERIFIED / N UNVERIFIED — flag all UNVERIFIED for attorney review]"
  overall_confidence: "HIGH | MEDIUM | LOW"
  confidence_rationale: "[Brief explanation of overall confidence assessment]"
  limitations:
    - "[Scope limitations, factual assumptions, or caveats]"
    - "All cited authority marked [VERIFY] requires independent verification before filing"
  attorney_review_required: true
  reviewer: "AI-assisted — requires qualified legal review before filing"
```

---

## Output Format Template

Deliver analysis in the following structure. Omit sections that do not apply.

```markdown
# Motion in Limine Analysis

**Case**: [Caption]
**Court / Circuit**: [Court and Circuit]
**Date**: [Date]
**Skill Version**: legalcode-motion-in-limine

---

## Executive Summary

**Overall Assessment**: [1-2 sentences on the evidentiary landscape and strongest grounds]
**Recommended Filing**: [File / File with caveats / Oppose with [strategy] / Do not file]
**Strongest Ground(s)**: [FRE rule(s)]

| Ground      | Classification                    | Confidence | Notes        |
| ----------- | --------------------------------- | ---------- | ------------ |
| FRE 401-403 | [STRONG/VIABLE/MARGINAL/WEAK/N/A] | [0.XX]     | [Brief note] |
| FRE 404(b)  | [STRONG/VIABLE/MARGINAL/WEAK/N/A] | [0.XX]     | [Brief note] |
| FRE 702     | [STRONG/VIABLE/MARGINAL/WEAK/N/A] | [0.XX]     | [Brief note] |
| FRE 801-807 | [STRONG/VIABLE/MARGINAL/WEAK/N/A] | [0.XX]     | [Brief note] |
| FRE 609     | [STRONG/VIABLE/MARGINAL/WEAK/N/A] | [0.XX]     | [Brief note] |

[one row per ground analyzed]

---

## Procedural Screen

**Local Rule Compliance**: [Filing deadline, page limit, hearing requirement — or flag for verification]
**Pretrial Conference**: [Date or 'unknown — check scheduling order']
**Effect of Ruling Note**: [Reminder on renewing objections at trial; Luce v. United States note if applicable]

---

## Argument Outlines

### Argument I — [FRE Rule]: [Title of Argument]

**Classification**: [STRONG / VIABLE / MARGINAL]
**Confidence**: [0.XX]

**Legal Standard**: [Precisely stated standard with citation]

**Key Authority**:

- _[Case Name]_, [citation] — [key holding]
- _[Case Name]_, [citation] — [key holding]

**Argument Outline**:

1. [Step 1 of argument — legal standard applied to facts]
2. [Step 2 — address each element]
3. [Step 3 — address anticipated counter-argument]
4. Prayer for Relief: [Exclude entirely / Exclude or, alternatively, limit with instruction]

**Anticipated Opposition**:
→ [Opposition argument 1] → [Rebuttal]
→ [Opposition argument 2] → [Rebuttal]

**Reply Focus**: [What reply brief should emphasize]

---

[Repeat for each STRONG or VIABLE ground in Tier 1 → Tier 2 → Tier 3 order]

---

## Alternative / Preserving Arguments

[Tier 3 / MARGINAL arguments, labeled "In the alternative..."]

---

## Response Toolkit

**Available If Motion Is Denied**:

- FRE 105 Limiting Instruction: [Proposed text of specific instruction]
- FRE 104(b) Conditional Relevance: [If facts supporting admissibility are disputed]
- FRE 103(b) Offer of Proof: [What the record requires to preserve the issue]
- Door-Opening Risk: [Identify what moving party's own trial conduct could re-open]

---

## Glass Box Audit Trail

[Paste completed YAML template from the Glass Box section above]
```

---

## Localization Notes

**For state court adaptation**: This skill is designed for federal courts under the FRE.
State adaptations require:

- Determining whether the state has adopted the FRE (most have) or a distinct code
- Identifying the state's expert testimony standard (Frye states include California, New
  York, Illinois, Pennsylvania — though some have shifted to Daubert; [VERIFY current
  state standard])
- Replacing federal privilege analysis (FRE 501) with state privilege rules
- Applying state-specific in limine motion deadlines and briefing requirements
- Removing or modifying Crawford / Confrontation Clause analysis, which is a federal
  constitutional doctrine applicable in state criminal cases via the Fourteenth Amendment
  but whose procedural application varies

**For criminal vs. civil adjustments within federal practice**: The skill flags civil/
criminal distinctions throughout (FRE 404, 609, 410, privilege). In criminal cases, also
consider: (1) FRE 413-415 (prior sexual assault / child molestation acts — specific
authorization for character evidence that overrides 404(b)); (2) FRE 412 (rape shield
protections); (3) constitutional dimensions of character evidence exclusion under the
Due Process and Confrontation Clauses.

---

## Provenance

Created by Legalcode (2026-03-21). Legalcode original synthesis. Research basis: Federal
Rules of Evidence as amended through December 1, 2023; _Daubert v. Merrell Dow Pharmaceuticals,
Inc._, 509 U.S. 579 (1993); _General Electric Co. v. Joiner_, 522 U.S. 136 (1997);
_Kumho Tire Co. v. Carmichael_, 526 U.S. 137 (1999); _Old Chief v. United States_, 519
U.S. 172 (1997); _Crawford v. Washington_, 541 U.S. 36 (2004); _Davis v. Washington_,
547 U.S. 813 (2006); _Huddleston v. United States_, 485 U.S. 681 (1988); _Hickman v.
Taylor_, 329 U.S. 495 (1947); _Jaffee v. Redmond_, 518 U.S. 1 (1996); _Luce v. United
States_, 469 U.S. 38 (1984); Advisory Committee Notes to FRE 401-403, 404, 407-411,
501-502, 702, 801-807, 609. Structural patterns adapted from `legalcode-motion-to-dismiss-
drafter` and the `legalcode-contract-review` reference standard. All cited authority
marked [VERIFY] requires independent verification.
