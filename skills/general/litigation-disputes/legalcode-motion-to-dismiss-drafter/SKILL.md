---
name: legalcode-motion-to-dismiss-drafter
description: Drafts and analyzes motions to dismiss under FRCP Rule 12(b)(1)–12(b)(7) for US federal court
  proceedings. Use when filing or opposing a motion to dismiss, evaluating grounds for dismissal before
  filing an answer, preparing argument outlines with supporting authority, anticipating opposition arguments,
  or developing reply brief strategy.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Drafts and analyzes motions to dismiss under FRCP Rule 12(b)(1)–12(b)(7) for US federal court proceedings. Use when filing or opposing a motion to dismiss, evaluating grounds for dismissal before filing an answer, preparing argument outlines with supporting authority, anticipating opposition arguments, or developing reply brief strategy. Covers subject matter jurisdiction (12(b)(1) facial vs. factual attacks), personal jurisdiction (12(b)(2) minimum contacts, specific vs. general jurisdiction, stream of commerce), improper venue (12(b)(3)), insufficient process (12(b)(4)), insufficient service (12(b)(5)), failure to state a claim (12(b)(6) Twombly/Iqbal plausibility, Rule 9(b) fraud, PSLRA), and failure to join a required party (12(b)(7) Rule 19 analysis). Addresses conversion to summary judgment under Rule 12(d), incorporation of extrinsic documents, waiver under Rule 12(h), local rule compliance, and leave-to-amend analysis. Generates argument outlines, anticipated opposition arguments, and reply brief strategy with confidence-scored authority marshaling and Glass Box audit trail.


# Legalcode Motion to Dismiss Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted motion to dismiss drafting
> and analysis. It does not constitute legal advice. All outputs must be reviewed, verified,
> and signed by qualified legal counsel licensed in the relevant jurisdiction before filing
> with any court. Procedural rules, pleading standards, and case law change frequently;
> verify all authoritative sources before relying on any conclusion or citation. AI-generated
> motion arguments may contain errors in legal analysis, citation accuracy, or strategic
> assessment — all arguments must be verified against current authority and the specific
> facts of the case. Any cited authority marked `[VERIFY]` has not been independently
> validated and must be confirmed before reliance. Filing a motion constitutes a Rule 11
> certification that the arguments are well-grounded in fact and law; counsel bears
> independent professional responsibility for that certification.

---

## Purpose and Scope

This skill drafts and analyzes motions to dismiss in US federal courts under Federal Rules
of Civil Procedure Rule 12(b)(1) through 12(b)(7). It operates in two primary modes:

1. **Drafting Mode**: Generates argument blocks, outlines, and supporting authority for a
   12(b) motion based on the facts of the case and grounds selected. Produces a structured
   argument framework suitable for attorney review and refinement into a final brief.

2. **Analysis Mode**: Evaluates an existing complaint or motion to dismiss — either one the
   user is filing or one they have received — to identify viable grounds, assess argument
   strength, anticipate opposition responses, and develop reply brief strategy.

The skill covers all seven Rule 12(b) grounds individually and in combination, applying
the governing legal standard for each ground, marshaling relevant authority, and flagging
procedural pitfalls including waiver under Rule 12(h) and conversion under Rule 12(d).

**Covers:**

- **12(b)(1)**: Subject matter jurisdiction — facial and factual attacks, Article III
  standing, mootness, ripeness, Rooker-Feldman, Eleventh Amendment sovereign immunity,
  administrative exhaustion
- **12(b)(2)**: Personal jurisdiction — minimum contacts, specific vs. general jurisdiction,
  stream of commerce doctrine (including circuit splits), purposeful availment, consent by
  registration, jurisdictional discovery
- **12(b)(3)**: Improper venue — 28 U.S.C. § 1391 analysis, forum selection clause
  enforcement under Atlantic Marine, forum non conveniens, transfer vs. dismissal
- **12(b)(4)**: Insufficient process — Rule 4 summons defects
- **12(b)(5)**: Insufficient service of process — Rule 4 service requirements, Rule 4(m)
  time limit, state-law alternatives, good cause extensions
- **12(b)(6)**: Failure to state a claim — Twombly/Iqbal two-step plausibility analysis,
  Rule 9(b) heightened pleading for fraud, PSLRA securities fraud, incorporation by
  reference doctrine, materials properly considered, leave to amend (Foman factors)
- **12(b)(7)**: Failure to join a required party — Rule 19(a) required party analysis,
  Rule 19(b) indispensability, jurisdictional implications
- **Conversion**: Rule 12(d) conversion to summary judgment, extrinsic materials doctrine
- **Waiver**: Rule 12(g) consolidation requirement, Rule 12(h) waiver rules by ground type
- **Local rules**: Pre-motion conference letters, word/page limits, briefing schedules
- **Anticipatory opposition**: Counter-argument identification and rebuttal strategy
- **Reply strategy**: Reply brief organization and selective engagement principles

**Does not:**

- Replace counsel's professional judgment on litigation strategy or judicial temperament
- Certify Rule 11 compliance (only filing counsel may certify)
- Conduct independent factual investigation or verify client representations
- Provide final assessments of state court motion to dismiss standards (state standards
  may differ materially from federal Twombly/Iqbal; flag for local counsel review)
- Draft the full brief (produces structured argument outlines suitable for brief development)
- Address post-dismissal appellate standards of review in depth
- Cover Rule 12(c) motions for judgment on the pleadings (separate analysis)

**Related skills:**

- `legalcode-complaint-drafter` — Draft complaints to Twombly/Iqbal standards (the
  adversarial counterpart to this skill)
- `legalcode-summary-judgment-analysis` — Analyze and draft Rule 56 motions at the
  post-discovery stage
- `legalcode-opposition-brief-drafter` — Draft opposition briefs to any motion type
- `legalcode-appellate-brief-analysis` — Analyze briefing for 12(b) appeals
- `legalcode-litigation-risk-assessment` — Broader litigation risk scoring
- `legalcode-early-case-assessment` — Pre-filing case evaluation including dismissal risk

---

## Jurisdiction and Governing Law

This skill is scoped to **US federal courts** governed by the Federal Rules of Civil
Procedure. FRCP Rule 12(b) applies in all federal district courts as the baseline. State
courts operate under separate procedural rules, and state-court motion to dismiss standards
can differ substantially from the federal Twombly/Iqbal standard.

**[JURISDICTION-SPECIFIC]** Localize for every engagement:

- **Circuit authority**: Identify which US Court of Appeals governs the district. Circuit
  precedent controls where the Supreme Court has not spoken definitively (e.g., stream of
  commerce doctrine under 12(b)(2), forum selection clause venue analysis).
- **District local rules**: Many districts require pre-motion conference letters or have
  special word/page limits. Key examples:
  - SDNY/EDNY (Local Rule 3.A): pre-motion conference letter required before filing any
    dispositive motion; typically 3 pages maximum
  - NDCA (Local Rule 7-3): meet-and-confer requirement before filing
  - DDC (Local Rule 7(m)): confer requirement before non-consent motions
  - Many districts: word limits of 6,500–14,000 words or 20–40 pages
- **State-law claims**: Erie doctrine applies — use state substantive law for any
  state-law claims even in federal court; check state pleading standards for state claims
- **Supplemental jurisdiction**: Consider 28 U.S.C. § 1367 implications if federal claims
  are dismissed and only state claims remain
- **Diversity jurisdiction**: Amount-in-controversy ($75,000 threshold) and complete
  diversity requirements under 28 U.S.C. § 1332; check citizenship of all parties
- **Timing**: Rule 12(a) requires answer or 12(b) motion within 21 days of service
  (60 days for government defendants under Rule 12(a)(2)–(3))

**Note on state courts**: If this motion is for a state court, use this skill only for
structural guidance. The applicable standard may be notice pleading under a Conley-type
standard (most states), a state-specific plausibility standard, a demurrer procedure, or
other local variant. Always verify with local counsel.

---

## Interactive Clarification

This skill uses structured clarification at key decision points. Wherever you see a
**CLARIFY** marker in the workflow, the skill pauses and presents structured questions
before proceeding. Each CLARIFY point explains:

- What is being asked
- Why the answer changes the analysis direction
- Options with explanatory context

For batch/automated runs, proceed with the assumptions stated in each CLARIFY block.
For interactive sessions, wait for user response before continuing.

---

## Workflow

### Step 1: Accept Input

Accept input in any of the following forms:

- **Complaint + instruction**: Paste or attach the complaint to be attacked, with
  instruction to identify viable 12(b) grounds
- **Grounds specification**: User identifies the specific 12(b) ground(s) to argue,
  with case facts
- **Draft motion + feedback**: An existing 12(b) motion draft for review and strengthening
- **Opposition posture**: A 12(b) motion already filed by opposing counsel, for opposition
  analysis and reply strategy

Also accept supplemental documents that may be relevant:

- Exhibits incorporated by reference in the complaint
- Prior court filings (prior case history, related actions)
- Applicable local rules or standing orders
- Playbook or litigation strategy memo from supervising counsel

### Step 2: Gather Context

**CLARIFY** — Before proceeding, confirm the following (skip questions already answered):

**2.1 Mode**

- Drafting a 12(b) motion to dismiss (offense — identifying and arguing grounds)
- Opposing a 12(b) motion (defense — identifying weaknesses and developing responses)
- Both (assess the viability of grounds AND prepare for opposition)
- _Why this matters_: Determines analysis perspective, argument framing, and output format

**2.2 Federal District and Circuit**

- Which district court? (e.g., S.D.N.Y., N.D. Cal., D. Del., N.D. Tex.)
- Which circuit? (1st–11th + D.C. + Fed. Cir.)
- _Why this matters_: Circuit precedent controls most 12(b) issues. Stream of commerce,
  consent-by-registration, and Iqbal application all have circuit-specific rules.

**2.3 Grounds to Analyze**

- All seven 12(b)(1)–(7) grounds (full survey)
- Specific ground(s) only: specify which
- _Why this matters_: A full survey is comprehensive but time-consuming; focused analysis
  delivers faster results if grounds are already identified

**2.4 Complaint Posture**

- Is the complaint the initial complaint, or has it been amended previously?
- Have any prior motions to dismiss been filed or ruled on?
- _Why this matters_: Prior unsuccessful motions inform the futility-of-amendment argument;
  prior rulings bind the court on waived/decided issues

**2.5 Nature of Claims**

- Federal question, diversity, or both?
- Types of claims: contract, tort, civil rights, securities, antitrust, IP, other?
- Any fraud-based claims (triggers Rule 9(b))?
- Any securities fraud claims (triggers PSLRA)?
- _Why this matters_: Claim type determines pleading standard, available grounds, and
  applicable heightened pleading rules

**Default assumptions (for non-interactive runs):**

- Mode: Drafting (offense perspective)
- All grounds surveyed
- Federal question jurisdiction
- General civil claims (not fraud or securities specific)
- First-filed complaint; no prior motions

---

### Step 3: Conduct Preliminary Procedural Screen

Before analyzing substantive grounds, run the procedural screen. These issues can affect
the viability or timing of any 12(b) motion.

#### 3.1 Waiver Check (Rule 12(h))

Apply the Rule 12(h) waiver matrix to determine which grounds are still available:

| Ground                                 | Waiver Rule                                                                   | Consequence of Missing     |
| -------------------------------------- | ----------------------------------------------------------------------------- | -------------------------- |
| 12(b)(1) — Subject matter jurisdiction | Never waived; may be raised at any time, including on appeal                  | Court may raise sua sponte |
| 12(b)(2) — Personal jurisdiction       | Waived if not included in first Rule 12 motion/response or raised in answer   | Cannot raise later         |
| 12(b)(3) — Improper venue              | Waived if not included in first Rule 12 motion/response or raised in answer   | Cannot raise later         |
| 12(b)(4) — Insufficient process        | Waived if not included in first Rule 12 motion/response or raised in answer   | Cannot raise later         |
| 12(b)(5) — Insufficient service        | Waived if not included in first Rule 12 motion/response or raised in answer   | Cannot raise later         |
| 12(b)(6) — Failure to state a claim    | May be raised in any pleading under Rule 7(a), Rule 12(c) motion, or at trial | Persistent through trial   |
| 12(b)(7) — Failure to join             | May be raised in any pleading under Rule 7(a), Rule 12(c) motion, or at trial | Persistent through trial   |

**Flag**: If the defendant has already filed an answer or a prior Rule 12 motion, check
whether 12(b)(2)–(5) grounds have been waived under Rule 12(g)(2) and 12(h)(1).

#### 3.2 Local Rule Compliance Screen

**[JURISDICTION-SPECIFIC]** Check and flag any of the following before drafting:

- Pre-motion conference letter requirement (SDNY, EDNY, NDCA, others)
- Meet-and-confer requirement (DDC, NDCA, and others)
- Word or page limits for opening brief
- Required formatting (font, margins, line spacing, certificate of compliance)
- Filing deadline relative to service date (Rule 12(a)(1)(A): 21 days)
- Briefing schedule and opposition/reply deadlines
- Standing orders of the assigned judge (critical — judges often have specific preferences)

#### 3.3 Rule 12(g) Consolidation Requirement

Remind: Under Rule 12(g)(2), a party that has made a Rule 12 motion must consolidate all
available Rule 12 defenses into that motion. Failure to include available 12(b)(2)–(5)
defenses in an initial Rule 12 motion constitutes waiver. Plan for a consolidated filing
that captures all viable grounds simultaneously.

---

### Step 4: Analyze Each 12(b) Ground

For each ground identified in Step 2.3 (or all grounds in full-survey mode), conduct the
following element-by-element analysis. Apply the **Ground Strength Classification** at the
end of each ground analysis.

#### Ground Strength Classification

| Classification | Criteria                                                                                                                                    | Recommended Action                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **STRONG**     | Legal standard clearly met; complaint contains fatal, uncureable defects; authority squarely on point; amendment would be futile            | File; request dismissal with prejudice                                          |
| **VIABLE**     | Legal standard plausibly met; argument is well-grounded but opposition has non-frivolous counter-arguments; outcome depends on facts/court  | File; request dismissal; anticipate opposition                                  |
| **MARGINAL**   | Argument has some basis but significant counter-arguments exist; risk of Rule 11 challenge if overstated; depends on circuit-specific rules | Consider filing if combined with stronger grounds; calibrate argument carefully |
| **WEAK**       | Standard not met on the pleadings; opposition would likely succeed; risk of Rule 11 sanctions                                               | Do not file on this ground alone; document analysis in file                     |

---

#### 4.1 — Rule 12(b)(1): Subject Matter Jurisdiction

**Legal Standard**

Subject matter jurisdiction cannot be waived. It may be challenged at any time, including
on appeal or sua sponte by the court. The plaintiff bears the burden of establishing
subject matter jurisdiction. _Kokkonen v. Guardian Life Ins. Co. of Am._, 511 U.S. 375
(1994) [VERIFY].

**Type of Attack — Identify First**

| Attack Type        | Description                                                             | Evidence Allowed                                                                                       | Burden                                                                                      |
| ------------------ | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| **Facial attack**  | Defendant argues the complaint itself, on its face, fails to allege SMJ | Only pleadings; accept all well-pleaded factual allegations as true                                    | Plaintiff must show SMJ is facially plausible on pleadings                                  |
| **Factual attack** | Defendant challenges the factual basis for SMJ with extrinsic evidence  | Court may consider affidavits, declarations, documents outside pleadings without converting to Rule 56 | Plaintiff must prove SMJ by preponderance; no presumption of truth for jurisdictional facts |

_Note_: Factual attacks are powerful because the court steps outside the pleadings to
evaluate actual jurisdictional facts. This is the one 12(b) ground where extrinsic
evidence is always proper without triggering Rule 12(d) conversion.

**Analysis Checklist — 12(b)(1)**

**A. Federal Question Jurisdiction (28 U.S.C. § 1331)**

- [ ] Do the claims arise under the Constitution, laws, or treaties of the United States?
- [ ] Apply the well-pleaded complaint rule: federal question must appear on the face of the
      complaint, not as an anticipated defense
- [ ] _Mottley_ limitation: anticipated federal defense does not create federal question
      jurisdiction
- [ ] _Gunn v. Minton_, 568 U.S. 251 (2013): state claim implicates federal issue only if
      the federal issue is (1) necessarily raised, (2) actually disputed, (3) substantial,
      and (4) capable of resolution in federal court without disrupting the federal-state
      balance [VERIFY]

**B. Diversity Jurisdiction (28 U.S.C. § 1332)**

- [ ] Complete diversity: every plaintiff's citizenship differs from every defendant's
      citizenship (_Strawbridge v. Curtiss_ rule; _Owen Equipment v. Kroger_, 437 U.S. 365
      (1978) [VERIFY])
- [ ] Amount in controversy exceeds $75,000 (exclusive of interest and costs)
- [ ] Citizenship of individuals: domicile (not residence) controls — _Mas v. Perry_
      [VERIFY]
- [ ] Citizenship of corporations: state of incorporation AND principal place of business
      (_Hertz Corp. v. Friend_, 559 U.S. 77 (2010): "nerve center" test for PPB) [VERIFY]
- [ ] Citizenship of LLCs/partnerships: citizenship of every member, traced through all
      tiers — _Carden v. Arkoma Assocs._, 494 U.S. 185 (1990) [VERIFY]
- [ ] Class actions: CAFA (28 U.S.C. § 1332(d)) applies different standards — minimal
      diversity, aggregate $5M, 100 class members

**C. Article III Standing**

- [ ] **Injury in fact**: concrete and particularized; actual or imminent, not speculative
      — _Lujan v. Defenders of Wildlife_, 504 U.S. 555 (1992)
- [ ] **Concreteness after TransUnion**: statutory violation alone insufficient; must
      show real-world harm or close historical or common-law analog — _TransUnion LLC v.
      Ramirez_, 594 U.S. 413 (2021); _Spokeo, Inc. v. Robins_, 578 U.S. 330 (2016)
- [ ] **Causation**: injury must be fairly traceable to defendant's challenged conduct
- [ ] **Redressability**: a favorable decision must likely redress the injury
- [ ] **Associational/organizational standing**: additional requirements apply
- [ ] **Standing in class actions**: each class member must have standing for each form
      of relief sought — _TransUnion_, 594 U.S. at 431

**D. Other Jurisdictional Bars**

- [ ] **Mootness**: case no longer presents a live controversy (exception: voluntary
      cessation doctrine; capable of repetition yet evading review)
- [ ] **Ripeness**: claim not yet ready for adjudication; no injury yet occurred
- [ ] **Political question doctrine**: _Baker v. Carr_ factors — non-justiciable
- [ ] **Rooker-Feldman doctrine**: federal courts lack jurisdiction over state court
      judgments; applies narrowly to losing parties in state court who seek federal
      review of state judgment — _Exxon Mobil Corp. v. Saudi Basic Indus. Corp._,
      544 U.S. 280 (2005) [VERIFY]
- [ ] **Eleventh Amendment sovereign immunity**: state and state-agency defendants;
      _Ex parte Young_ exception for prospective injunctive relief against state officers;
      check whether state has waived immunity
- [ ] **Administrative exhaustion**: whether plaintiff must exhaust administrative
      remedies before filing — varies by statute

**Argument Block Template — 12(b)(1)**

```
I. THE COURT LACKS SUBJECT MATTER JURISDICTION

A. Standard of Review
   [State the governing standard — facial vs. factual attack; burden on plaintiff]

B. [Specific Basis — e.g., Plaintiff Lacks Article III Standing]
   1. Plaintiff Has Not Alleged a Concrete Injury in Fact
      [TransUnion / Spokeo analysis applied to complaint allegations]
   2. Plaintiff Has Not Established Causation / Redressability
      [If applicable]

C. This Defect Cannot Be Cured by Amendment
   [If the defect is jurisdictional and incurable]
```

---

#### 4.2 — Rule 12(b)(2): Personal Jurisdiction

**Legal Standard**

Plaintiff bears the burden of proving personal jurisdiction. In considering a 12(b)(2)
motion, the court accepts the plaintiff's well-pleaded jurisdictional allegations as true
and resolves factual disputes in plaintiff's favor — but only if the motion is decided on
the pleadings without an evidentiary hearing. _See Daimler AG v. Bauman_, 571 U.S. 117
(2014).

**Two Forms of Personal Jurisdiction**

| Form         | Test                                                                                                                                                                                         | Key Cases                                                                                                                                                                                     |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **General**  | Defendant "at home" in the forum — for individuals, domicile; for corporations, state of incorporation or principal place of business                                                        | _Goodyear Dunlop Tires v. Brown_, 564 U.S. 915 (2011); _Daimler AG v. Bauman_, 571 U.S. 117 (2014)                                                                                            |
| **Specific** | Claim arises from or relates to defendant's forum contacts; three-part test: (1) purposeful availment, (2) claim arises from/relates to contacts, (3) exercise of jurisdiction is reasonable | _International Shoe Co. v. Washington_, 326 U.S. 310 (1945); _Burger King Corp. v. Rudzewicz_, 471 U.S. 462 (1985); _Ford Motor Co. v. Montana Eighth Judicial District_, 592 U.S. 351 (2021) |

**Analysis Checklist — 12(b)(2)**

**A. General Jurisdiction**

- [ ] Is defendant a corporation? If so, is forum the state of incorporation or PPB?
      Post-_Daimler_, "essentially at home" is extraordinarily limited to these two forums
      in typical cases; "exceptional case" exception is very narrow
- [ ] For individuals: is forum defendant's domicile?
- [ ] **Consent by registration**: Does state require foreign corporations to appoint
      agent for service, and does registration constitute consent to general jurisdiction?
      **[JURISDICTION-SPECIFIC] — Active circuit split**: Some circuits hold registration
      equals consent (_Mallory v. Norfolk S. Ry. Co._, 600 U.S. 122 (2023) permitted
      state to require consent by registration); others limit consent jurisdiction —
      check circuit precedent carefully

**B. Specific Jurisdiction**

- [ ] **Purposeful availment**: Did defendant deliberately direct activity toward the
      forum? Must be defendant's own contacts — not unilateral acts of plaintiff or
      third parties (_Walden v. Fiore_, 571 U.S. 277 (2014))
- [ ] **Arises from or relates to**: Does plaintiff's claim arise from or relate to
      defendant's forum contacts? Post-_Ford Motor_: "relates to" is broader than
      "but-for causation"; some causal relationship required but not strict causation
- [ ] **Reasonableness**: Consider (1) burden on defendant, (2) forum's interest,
      (3) plaintiff's interest in convenient relief, (4) interstate judicial system's
      interest, (5) shared interest of states — _Burger King_, 471 U.S. at 477
- [ ] **Mass torts and multi-plaintiff cases**: _Bristol-Myers Squibb Co. v. Superior
      Court_, 582 U.S. 255 (2017) — nonresident plaintiffs cannot rely on in-state
      plaintiffs' contacts; each plaintiff must independently satisfy specific jurisdiction
      (critical for consolidated or multi-district litigation)

**C. Stream of Commerce**
**[JURISDICTION-SPECIFIC] — Persistent circuit split; no majority Supreme Court rule:**

| Test                                                                                                                                                   | Circuits                  | Authority                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------- | ------------------------------------------------------------------------------------ |
| **Mere foreseeability** (broader): jurisdiction proper if defendant places product into stream knowing it may end up in forum                          | Some circuits             | _World-Wide Volkswagen Corp. v. Woodson_, 444 U.S. 286 (1980) dicta                  |
| **Stream of commerce plus** (narrower): must show additional conduct targeting the forum (designing for the forum, advertising, establishing channels) | More restrictive circuits | _Asahi Metal Indus. Co. v. Superior Court_, 480 U.S. 102 (1987) (O'Connor plurality) |
| **Fragmented / no majority rule**                                                                                                                      | All circuits split        | _J. McIntyre Machinery, Ltd. v. Nicastro_, 564 U.S. 873 (2011) (no majority)         |

Apply the specific circuit's rule; if unclear, analyze under both tests.

**D. Jurisdictional Discovery**

- [ ] Is jurisdictional discovery warranted? Courts may allow limited discovery when
      plaintiff makes a colorable showing that jurisdiction exists and specific discovery
      would reveal facts supporting jurisdiction
- [ ] Flag: courts retain discretion to deny jurisdictional discovery where plaintiff
      fails to demonstrate a colorable claim

**Argument Block Template — 12(b)(2)**

```
II. THIS COURT LACKS PERSONAL JURISDICTION OVER DEFENDANT [NAME]

A. Standard of Review
   [Plaintiff's burden; accept allegations as true at pleadings stage]

B. Defendant Is Not Subject to General Jurisdiction in [Forum]
   [Daimler "essentially at home" analysis — not state of incorporation, not PPB;
    address consent-by-registration if applicable]

C. Defendant Is Not Subject to Specific Jurisdiction
   1. Defendant Did Not Purposefully Avail Itself of [Forum]
      [Walden: must be defendant's own forum-directed contacts]
   2. Plaintiff's Claims Do Not Arise From or Relate to Defendant's Contacts
      [Ford Motor "relates to" analysis]
   3. [If applicable] Stream of Commerce Theory Fails Under [Circuit] Standard
      [Apply circuit test — O'Connor plurality vs. broader approach]

D. Jurisdictional Discovery Is Not Warranted
   [If applicable: no colorable showing; discovery would be futile]
```

---

#### 4.3 — Rule 12(b)(3): Improper Venue

**Legal Standard**

On a 12(b)(3) motion, the court accepts the plaintiff's well-pleaded allegations as true
and resolves all factual conflicts in plaintiff's favor. The moving defendant bears the
burden of showing that venue is improper. [VERIFY circuit split on burden allocation]

**Venue Analysis**

**A. General Venue Statute — 28 U.S.C. § 1391**

- [ ] § 1391(b)(1): Any district where any defendant resides, if all defendants are
      residents of the forum state
- [ ] § 1391(b)(2): Any district where a substantial part of the events or omissions
      giving rise to the claim occurred, or a substantial part of property that is the
      subject of the action is situated
- [ ] § 1391(b)(3): Fallback — if no other district qualifies, any district where any
      defendant is subject to personal jurisdiction
- [ ] Residence of corporations (§ 1391(c)): district where subject to personal
      jurisdiction (for companies incorporated/PPB in another state, the specific
      district within that state where contacts are sufficient)

**B. Forum Selection Clause**

- [ ] Does the contract contain a mandatory forum selection clause designating a different
      venue?
- [ ] **Atlantic Marine Construction Co. v. U.S. Dist. Ct. for W.D. Tex.**, 571 U.S. 49
      (2013): When a valid forum selection clause points to another federal court, the
      court enforces the clause through § 1404(a) transfer, NOT 12(b)(3) dismissal; and
      the § 1404(a) analysis is adjusted — plaintiff's choice of forum gets no weight,
      and private-interest factors are deemed to weigh in favor of the pre-selected forum
- [ ] For clauses pointing to foreign or state courts: 12(b)(3) dismissal or § 1406
      transfer may be appropriate — _M/S Bremen v. Zapata Off-Shore Co._, 407 U.S. 1
      (1972) [VERIFY]: forum selection clauses are presumptively valid; overcoming
      requires showing clause is unreasonable, unjust, or product of fraud/overreaching
- [ ] Check whether clause is mandatory ("shall be in") vs. permissive ("may be in")

**C. Forum Non Conveniens**

- [ ] Even if venue is technically proper, the court has discretion to dismiss in favor
      of a significantly more convenient foreign forum — _Piper Aircraft Co. v. Reyno_,
      454 U.S. 235 (1981) [VERIFY]
- [ ] Analysis: (1) adequate alternative forum; (2) balance of private/public interest
      factors; (3) plaintiff's choice of home forum gets substantial deference (less
      deference if foreign plaintiff chose US forum)

**Argument Block Template — 12(b)(3)**

```
III. VENUE IS IMPROPER IN THE [DISTRICT] DISTRICT OF [STATE]

A. Standard of Review
   [Defendant's burden; well-pleaded allegations accepted as true]

B. Venue Is Not Proper Under 28 U.S.C. § 1391
   1. Defendant Does Not Reside in This District
   2. No Substantial Part of the Events Occurred Here
      [Analyze each alleged basis for venue]

C. [If Applicable] The Parties' Forum Selection Clause Requires Litigation in [Other Forum]
   [Atlantic Marine analysis; characterize as § 1404 transfer argument if other federal court]
```

---

#### 4.4 — Rule 12(b)(4): Insufficient Process

**Legal Standard**

Rule 12(b)(4) challenges the form or content of the process (i.e., the summons itself),
not the manner of service. This is a narrow ground — courts rarely grant dismissal for
technical process defects; they typically quash service and allow re-service.

**Analysis Checklist — 12(b)(4)**

- [ ] Does the summons comply with Rule 4(a) requirements: court name, parties, clerk's
      signature and seal, defendant's name and address, plaintiff's attorney info, time
      to appear?
- [ ] Is the summons directed to the correct party?
- [ ] Practical note: 12(b)(4) motions rarely succeed as grounds for dismissal; courts
      prefer quashing and allowing amendment. Best used to preserve the defense while
      buying time for the defendant to respond.

---

#### 4.5 — Rule 12(b)(5): Insufficient Service of Process

**Legal Standard**

Plaintiff bears the burden of proving that service was effected properly. The court has
discretion to dismiss the action or quash service and allow re-service.

**Analysis Checklist — 12(b)(5)**

- [ ] Was service made by the proper person? Rule 4(c)(2): any person who is at least 18
      and not a party
- [ ] Was service made in the manner required by Rule 4?
  - Individuals: Rule 4(e) — personal delivery, leaving at dwelling with suitable person,
    or delivering to authorized agent; or state-law methods
  - Corporations: Rule 4(h) — officer, managing agent, general agent, or authorized agent;
    or state-law methods
  - Waiver of service: Rule 4(d) — defendant may waive formal service; failure to waive
    without good cause may result in costs award
- [ ] Was service made within the 90-day period? Rule 4(m): if service not made within
      90 days, court must dismiss without prejudice or order service extended for good cause
- [ ] Was there good cause for any delay in service? (excusable neglect, evasion by
      defendant, difficulty locating defendant)
- [ ] **Strategy note**: Courts often quash rather than dismiss on 12(b)(5) unless plaintiff
      cannot cure (e.g., statute of limitations has now run, making re-service futile)

---

#### 4.6 — Rule 12(b)(6): Failure to State a Claim

This is the most frequently litigated 12(b) ground. Apply the Twombly/Iqbal two-step
analysis rigorously.

**Legal Standard**

A complaint survives 12(b)(6) only if it contains sufficient factual matter, accepted as
true, to "state a claim to relief that is plausible on its face." _Ashcroft v. Iqbal_,
556 U.S. 662, 678 (2009), quoting _Bell Atl. Corp. v. Twombly_, 550 U.S. 544, 570 (2007).

**The Twombly/Iqbal Two-Step Test**

**Step 1 — Strip Legal Conclusions**: Identify and disregard all statements that are legal
conclusions, formulaic recitations, or threadbare labels. These are not entitled to the
presumption of truth even though cast in factual form. _Iqbal_, 556 U.S. at 678.

Examples of stripped conclusions:

- "Defendant intentionally and willfully violated Plaintiff's rights" (conclusory)
- "Defendant knew or should have known" (without supporting facts)
- "All conditions precedent have been met" (boilerplate)
- "Defendant engaged in a scheme to defraud" (without specific facts)

**Step 2 — Plausibility Assessment**: Taking the remaining well-pleaded factual allegations
as true, determine whether they plausibly give rise to an entitlement to relief. Plausibility
means "more than a sheer possibility" but less than probability. Where complaint alleges
conduct that is equally consistent with innocent conduct as wrongful conduct, without more,
the complaint does not plausibly allege the claim. _Iqbal_, 556 U.S. at 678–679.

**What the Court May Consider at 12(b)(6)**

| Materials                                                               | Basis                                                                           |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| The complaint and all exhibits attached to it                           | Rule 10(c)                                                                      |
| Documents incorporated by reference in the complaint                    | _Faulkner v. Beer_, 463 F.3d 130 (2d Cir. 2006) [VERIFY]                        |
| Documents integral to the complaint (plaintiff relied on and used them) | Circuit-specific; distinguish from "mere mention"                               |
| Matters of public record                                                | Courts may take judicial notice                                                 |
| Judicially noticed facts (Rule 201)                                     | Not disputed; not truth of contents of public filings unless judicially noticed |
| Prior court orders and judgments                                        | Matters of public record                                                        |
| **NOT** extrinsic affidavits or declarations                            | Triggers Rule 12(d) conversion                                                  |
| **NOT** facts the court "knows" are true                                | Court's independent knowledge not permissible                                   |

**[JURISDICTION-SPECIFIC]** The scope of "incorporation by reference" and "integral
document" doctrines varies by circuit. Some circuits apply them liberally; others require
the plaintiff to have explicitly relied on the document. Check circuit authority.

**Heightened Pleading Standards**

**Rule 9(b) — Fraud:**

- [ ] Who committed the fraud?
- [ ] What fraudulent statements were made?
- [ ] When were the statements made?
- [ ] Where were the statements made?
- [ ] How did the statements mislead the plaintiff?
- Rule 9(b) applies to any claim that "sounds in fraud" even if not formally pleaded as
  fraud (e.g., RICO predicate acts, fraudulent concealment, certain consumer protection claims)

**PSLRA — Securities Fraud (15 U.S.C. § 78u-4):**

- [ ] Specify each misleading statement and explain why it was misleading
- [ ] State with particularity facts giving rise to a strong inference of scienter
      ("strong inference" standard: at least as compelling as any innocent inference)
      — _Tellabs, Inc. v. Makor Issues & Rights, Ltd._, 551 U.S. 308 (2007)
- [ ] PSLRA stay of discovery during pendency of motion to dismiss

**Analysis Checklist — 12(b)(6) for Each Claim**

For each cause of action in the complaint:

- [ ] What are the required elements of this claim?
- [ ] Which elements are supported by factual allegations (not conclusions)?
- [ ] Which elements are supported only by legal conclusions that must be stripped?
- [ ] After stripping, do remaining facts plausibly (not just possibly) support the claim?
- [ ] Is any element completely unpleaded?
- [ ] If fraud: does the complaint satisfy Rule 9(b) specificity?
- [ ] Is leave to amend futile? (Would additional facts cure the deficiency, or is the
      claim legally impossible as a matter of law?)

**Leave to Amend — Foman Factors**

After a successful 12(b)(6) motion, courts consider leave to amend under Rule 15(a)(2).
Courts deny leave to amend where:

1. **Undue delay**: significant delay without justification
2. **Bad faith or dilatory motive**: pleading in bad faith
3. **Repeated failure to cure**: prior opportunities to amend have failed to cure
4. **Undue prejudice to opposing party**: significant discovery or trial preparation wasted
5. **Futility**: proposed amendment would not survive another 12(b)(6) challenge

**Futility** is the most important ground for seeking dismissal with prejudice. Argue
futility where:

- The legal claim is foreclosed as a matter of law (e.g., statute of limitations has run;
  conduct is absolutely privileged; element that cannot be pleaded does not exist)
- Prior amendments have demonstrated inability to plead necessary facts
- The jurisdictional defect (for 12(b)(1)) cannot be cured by allegation

**Argument Block Template — 12(b)(6)**

```
[COUNT NUMBER]. [CLAIM NAME] FAILS TO STATE A CLAIM

A. Legal Standard
   [Twombly/Iqbal two-step test; note any heightened pleading requirement]

B. Step 1: The Complaint's Conclusory Allegations Are Not Entitled to the Presumption of Truth
   [List and quote each conclusory allegation; explain why it is a legal conclusion,
    not a factual allegation]

C. Step 2: The Remaining Factual Allegations Do Not Plausibly State a Claim
   Element 1 — [Element Name]:
     [Quote factual allegations; explain why they fail to plausibly support the element]
   Element 2 — [Element Name]:
     [Repeat for each required element; identify missing elements]
   [If applicable] Element [N] — [Element Name]: Not Pleaded At All
     [Identify complete element omissions]

D. [If Applicable] The Complaint Also Fails Rule 9(b)'s Heightened Pleading Standard
   [Identify missing who/what/when/where/how specificity]

E. Leave to Amend Should Be Denied as Futile / Dismissed With Prejudice
   [Foman factors analysis; explain why amendment cannot cure the deficiency]
```

---

#### 4.7 — Rule 12(b)(7): Failure to Join a Required Party

**Legal Standard**

Rule 12(b)(7) requires dismissal when the action cannot proceed without a party that the
plaintiff has failed to join under Rule 19. The moving party bears the burden of producing
evidence showing the absent party is required and that joinder would destroy jurisdiction
or is otherwise not feasible.

**Rule 19 Analysis — Two-Step**

**Step 1 — Is the Absent Party a Required Party? (Rule 19(a))**

A party is required if:

- (1) In the party's absence, the court cannot accord complete relief among existing parties
  (_necessary for complete relief_), OR
- (2) The party claims an interest in the action AND either:
  - (a) Proceeding without the party may impair or impede the absent party's ability to
    protect its interest (_impairment_), OR
  - (b) Proceeding without the party may leave existing parties subject to a substantial
    risk of incurring double, multiple, or inconsistent obligations (_inconsistent obligations_)

**Step 2 — Is the Party Indispensable? (Rule 19(b))**

If joinder is not feasible (e.g., would destroy diversity; no personal jurisdiction), can
the action proceed anyway, or must it be dismissed? Factors:

1. Extent to which a judgment rendered in the party's absence would prejudice the absent
   party or existing parties
2. Extent to which prejudice could be lessened by protective provisions in the judgment,
   shaping of relief, or other measures
3. Whether a judgment rendered without the party would be adequate
4. Whether the plaintiff would have an adequate remedy if the action is dismissed for
   non-joinder

**Analysis Checklist — 12(b)(7)**

- [ ] Identify the absent party and its claimed interest in the dispute
- [ ] Can complete relief be accorded between existing parties? (Step 1 — first basis)
- [ ] Does the absent party claim a legally protected interest in the action?
- [ ] Could proceedings impair the absent party's interest? (Step 1 — second basis, prong a)
- [ ] Could proceedings expose existing parties to inconsistent obligations?
      (Step 1 — second basis, prong b)
- [ ] If the absent party is required: is joinder feasible?
  - Would joinder destroy subject matter jurisdiction (diversity)?
  - Does the court have personal jurisdiction over the absent party?
- [ ] If joinder is not feasible: apply Rule 19(b) indispensability factors

**Argument Block Template — 12(b)(7)**

```
[NUMBER]. THIS ACTION MUST BE DISMISSED FOR FAILURE TO JOIN [PARTY NAME]

A. Standard of Review
   [Rule 19 two-step; defendant's burden]

B. [Absent Party] Is a Required Party Under Rule 19(a)
   1. Complete Relief Cannot Be Accorded Without [Absent Party] [if applicable]
   2. [Absent Party] Claims a Protectable Interest in This Action
   3. Proceeding Without [Absent Party] Would [Impair Its Interest / Create Risk of
      Inconsistent Obligations]

C. Joinder Is Not Feasible Because [Diversity Destruction / No Personal Jurisdiction]

D. Under Rule 19(b), This Action Should Be Dismissed
   [Walk through the four Rule 19(b) indispensability factors]
```

---

### Step 5: Conversion and Extrinsic Materials Analysis (Rule 12(d))

Address conversion issues explicitly when extrinsic materials are relevant.

**When Conversion Is Triggered**

If the court considers "matters outside the pleadings" on a 12(b)(6) motion, Rule 12(d)
requires the court to treat the motion as one for summary judgment under Rule 56. The
court must then give all parties "a reasonable opportunity to present all the material
pertinent to the motion."

**When Conversion Is NOT Triggered — Incorporation Exceptions**

| Exception                             | Rule              | Notes                                                                                       |
| ------------------------------------- | ----------------- | ------------------------------------------------------------------------------------------- |
| Exhibits attached to complaint        | Rule 10(c)        | Always permissible                                                                          |
| Documents incorporated by reference   | Judicial doctrine | Document must be explicitly referred to in complaint                                        |
| Documents "integral" to the complaint | Judicial doctrine | Plaintiff actually relied on the document in drafting the complaint — not just mentioned it |
| Judicially noticed facts              | FRE 201           | Courts may take judicial notice of facts "not subject to reasonable dispute"                |
| Matters of public record              | Judicial doctrine | Court records, public filings; but truth of contents may not be judicially noticed          |

**[JURISDICTION-SPECIFIC]** The scope of the incorporation-by-reference and integral
document doctrines varies materially by circuit:

- 2d Circuit: considers documents "integral" to the complaint even without formal incorporation
- 9th Circuit: documents may be incorporated if plaintiff refers to them and their authenticity
  is not questioned
- Other circuits: may require explicit quotation or incorporation
  Verify the applicable circuit rule before relying on extrinsic documents.

**Drafting Strategy**

If you want the court to consider specific extrinsic documents:

1. Attach them as exhibits to the motion with proper authentication
2. Argue they are incorporated by reference or integral to the complaint
3. Alert the court that if it declines to consider them, the 12(b)(6) motion still succeeds
   on the pleadings; in the alternative, request conversion to Rule 56

---

### Step 6: Anticipatory Opposition Analysis

For each ground filed, map the opposition's strongest counter-arguments and develop
pre-emptive rebuttals.

#### Standard Opposition Moves by Ground

| Ground                               | Typical Opposition Arguments                                                               | Pre-Emptive Rebuttal Strategy                                                                 |
| ------------------------------------ | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| **12(b)(1) — Standing**              | Concrete injury alleged; analogous common-law harm; statutory standing created by Congress | TransUnion nexus: no real-world harm; congressional creation of legal right ≠ concrete injury |
| **12(b)(1) — SMJ generally**         | Factual allegations sufficient; jurisdictional facts need not be proved at pleading stage  | For factual attacks: submit affidavits challenging jurisdictional facts                       |
| **12(b)(2) — Personal jurisdiction** | Defendant purposefully availed itself; claim relates to contacts; stream of commerce       | Walden: plaintiff's contacts not defendant's; Bristol-Myers Squibb: nonresidents' claims      |
| **12(b)(3) — Venue**                 | Events occurred here; defendant resides here                                               | Analyze § 1391 elements precisely; for forum selection clauses, show clause is mandatory      |
| **12(b)(6) — Plausibility**          | Factual allegations create plausible inference of wrongdoing                               | Iqbal Step 1: strip conclusions; Step 2: remaining facts equally consistent with innocence    |
| **12(b)(6) — Leave to amend**        | Plaintiff should be allowed to amend                                                       | Foman futility: amendment cannot cure the legal deficiency                                    |
| **12(b)(7) — Joinder**               | Complete relief available without absent party; no prejudice                               | Rule 19(b): dismissal is required; inconsistent obligations risk                              |

#### Cross-Cutting Opposition Strategies

- **Bell Pleading Standard**: Plaintiff may argue that notice pleading under Rule 8(a) is
  satisfied. Rebuttal: _Twombly_ and _Iqbal_ superseded Conley's "no set of facts" standard;
  Rule 8 requires a "plausible" claim, not just notice.
- **Factual Dispute Argument**: Plaintiff may assert there are factual issues precluding
  dismissal. Rebuttal: on 12(b)(6), the court accepts plaintiff's allegations as true — the
  question is whether those accepted facts, if true, plausibly state a claim.
- **Amendment as of Right**: Under Rule 15(a)(1), plaintiff may amend once as of right within
  21 days of service of a 12(b) motion. Consider: if amendment would cure the defects, should
  you file the motion now to precipitate the amendment (and then re-evaluate), or wait?

---

### Step 7: Reply Brief Strategy

Structure the reply brief to maximize persuasive impact:

1. **Lead with the ground most likely to succeed** — do not bury the strongest argument
2. **Do not repeat the opening brief** — assume the court read it; use the reply to rebut
   opposition, not rehearse arguments
3. **Cite new authority** (if any emerged since the opening brief was filed)
4. **Selective engagement**: Do not answer every opposition argument; answer only the
   arguments that:
   - Directly attack your strongest ground
   - Introduce new authority not addressed in the opening brief
   - Misrepresent the record or the law
5. **Clarify any concessions**: If the opposition identified a narrow issue where the
   motion overstates the case, concede narrowly and refocus on the viable grounds
6. **Reinforce futility of amendment** (for 12(b)(6)): If plaintiff proposed an amendment
   in the opposition, analyze why the proposed amendment still fails
7. **Address incorporation-by-reference disputes**: If plaintiff argued the court cannot
   consider specific extrinsic materials, respond with circuit-specific doctrine

**Reply Brief Length**: Typically one-half to two-thirds the length of the opening brief.
Check local rules for reply word/page limits.

---

### Step 8: Apply Quality Frameworks

Before delivering any analysis or argument outline, run the following frameworks.

#### Citation Quality Gates

Run these 5 gates silently. If any gate fails, revise before delivering.

| Gate           | Rule                                                                                                   | Fail Action                             |
| -------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------- |
| **Source**     | Every legal claim cites a specific Supreme Court or circuit case, statute, or rule                     | Add citation or mark `[UNVERIFIED]`     |
| **Format**     | Citations follow consistent format: _Case Name_, volume U.S./F.3d/F.Supp.3d page (year)                | Fix format                              |
| **Currency**   | Cited cases have not been overruled or limited by subsequent authority                                 | Flag `[CHECK CURRENCY]`                 |
| **Domain**     | Analysis correctly identifies whether the rule is circuit-wide, circuit-specific, or subject to splits | Flag `[CIRCUIT-SPLIT]` where applicable |
| **Confidence** | Any uncertainty about the precise holding is explicitly stated                                         | Add confidence qualifier or `[VERIFY]`  |

#### Self-Interrogation for STRONG-Classified Grounds

For any ground classified STRONG (Step 4), apply this 3-pass review before recommending filing:

**Pass 1 — Legal Chain Integrity**: Does the dismissal argument follow logically from
the cited authority? Would a federal district judge in this circuit actually grant
the motion on this argument?

**Pass 2 — Completeness**: Have all potential curative arguments by the plaintiff been
considered? Is there a reasonable theory by which the complaint could survive even if
the argument is accepted?

**Pass 3 — Challenge**: What is the strongest argument plaintiff will make in opposition?
Does the motion adequately pre-empt that argument? Under what circumstances might the
court allow amendment rather than dismissing with prejudice?

#### Confidence Scoring

| Level        | Range     | Meaning                                                                     | Action                                     |
| ------------ | --------- | --------------------------------------------------------------------------- | ------------------------------------------ |
| **Definite** | 0.95–1.0  | Settled law; Supreme Court or unanimous circuit authority directly on point | State with confidence                      |
| **High**     | 0.80–0.94 | Strong circuit authority; minor questions on application to specific facts  | State with brief caveat                    |
| **Probable** | 0.60–0.79 | Good arguments; circuit split or analogical reasoning required              | State with reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuinely uncertain; novel application; outcome depends on judge's approach | Flag for counsel review with both sides    |
| **Unlikely** | 0.0–0.39  | Weak basis; current circuit authority against the position                  | Do not assert; flag `[UNCERTAIN]`          |

---

## Prioritization Framework

When the motion raises multiple grounds, prioritize argument blocks in the following order:

### Tier 1 — Must Lead (Threshold Arguments)

Arguments that, if successful, end the action and cannot be waived later:

- 12(b)(1): Subject matter jurisdiction (court has no power to hear the case)
- 12(b)(2): Personal jurisdiction (leads if defendant has no connections to forum)
- 12(b)(6): Failure to state a claim — complete failure on all counts

_Why lead_: Courts expect threshold arguments first; they determine whether the court has
power to proceed. Winning on 12(b)(1) or 12(b)(2) is more powerful than 12(b)(6) because
it forecloses the whole forum, not just the current pleading.

### Tier 2 — Strong Merits Arguments

Arguments that defeat specific claims even if others survive:

- 12(b)(6): Failure to state specific causes of action (where not all claims fail)
- 12(b)(3): Venue (dismissal sends case elsewhere, not necessarily ends it)
- 12(b)(7): Failure to join (often leads to dismissal without prejudice)

_Why second_: Procedurally strong but do not end the litigation as decisively as Tier 1.

### Tier 3 — Technical / Supplemental Arguments

Arguments that rarely result in full dismissal but may buy time or protect rights:

- 12(b)(4): Insufficient process (usually results in quash + re-service, not dismissal)
- 12(b)(5): Insufficient service (usually quash + re-service opportunity)

_Why third_: Preserve the defense and include in consolidated motion per Rule 12(g)(2),
but do not lead the brief with these unless they are the strongest available ground.

---

## Anti-Patterns in Motion to Dismiss Practice

The following are specific, recurring errors in 12(b) motion practice. Avoid each.

1. **Arguing the merits on 12(b)(6)**: Submitting extrinsic evidence of what actually
   happened, rather than focusing on whether the complaint's own allegations state a
   plausible claim. Merits evidence triggers Rule 12(d) conversion and undermines the
   motion.

2. **Waiving 12(b)(2)–(5) defenses by delay**: Filing an answer or a prior Rule 12
   motion without including all available 12(b)(2)–(5) grounds. Rule 12(g)(2) requires
   consolidation; failure to include waives the defense.

3. **Failing to address the plausibility standard correctly**: Arguing the facts are
   false (a merits issue) rather than arguing the facts as alleged do not plausibly state
   the elements of the claim (the correct standard).

4. **Confusing the two Twombly/Iqbal steps**: Skipping Step 1 (stripping legal conclusions)
   and jumping to Step 2, which leaves the court with inflated "facts" to evaluate. Always
   strip conclusions first, then assess plausibility of the residue.

5. **Ignoring Rule 12(b)(1) in cases with standing issues**: Filing only on 12(b)(6) when
   the complaint has standing or mootness defects. Subject matter jurisdiction is paramount
   and can be raised at any time — missing it in the initial motion is a strategic error.

6. **Relying on stream of commerce arguments without identifying circuit**: The stream of
   commerce doctrine for 12(b)(2) has no Supreme Court majority. The applicable test
   depends entirely on circuit precedent. Filing a 12(b)(2) motion without identifying the
   circuit rule is professionally inadequate.

7. **Requesting dismissal with prejudice without arguing futility**: Courts default to
   granting leave to amend after a first 12(b)(6) dismissal unless the defendant argues
   and demonstrates that amendment would be futile. Always address futility expressly.

8. **Filing without checking pre-motion conference requirements**: SDNY/EDNY and other
   districts require pre-motion letters before filing any dispositive motion. Filing the
   motion directly can result in it being stricken or the judge imposing sanctions.

9. **Overloading the brief with weak grounds**: Including marginal or weak 12(b) grounds
   to "cover all bases" dilutes the brief and reduces credibility for the strong grounds.
   If a ground is WEAK under the classification in Step 4, do not file it — document it
   in the file instead.

10. **Misusing Rule 12(b)(3) for forum selection clause enforcement**: Post-_Atlantic
    Marine_, when a forum selection clause points to another federal court, the proper
    vehicle is § 1404(a) transfer, not Rule 12(b)(3) dismissal. Filing a 12(b)(3) motion
    in this scenario is inconsistent with governing Supreme Court authority.

11. **Ignoring the consent-by-registration circuit split in 12(b)(2) motions**: After
    _Mallory v. Norfolk Southern_, filing a 12(b)(2) motion without addressing whether
    the defendant registered as a foreign corporation in the forum state is incomplete in
    circuits that treat registration as consent to general jurisdiction.

12. **Failing to segregate grounds when arguing leave to amend**: After a 12(b)(6) grant,
    arguing futility without differentiating between grounds that can be cured (add more
    facts) and grounds that cannot be cured (legal impossibility). Blanket "amendment is
    futile" arguments are disfavored; specify why each claim cannot be cured.

13. **Not addressing the Spokeo/TransUnion concreteness requirement for statutory claims**:
    In cases involving statutory violations (data privacy, consumer protection, financial
    regulations), the 12(b)(1) standing challenge to concrete injury is often more powerful
    than the 12(b)(6) merits challenge. Many practitioners default to 12(b)(6) and miss
    the stronger 12(b)(1) ground.

14. **Treating 12(b)(4) and 12(b)(5) as equivalent**: They are distinct defenses. 12(b)(4)
    attacks the form of the process (the summons); 12(b)(5) attacks the manner of service.
    Conflating them in the brief signals a lack of procedural precision to the court.

15. **Failing to brief the extrinsic-materials doctrine before citing extrinsic documents**:
    When the motion relies on documents outside the complaint, the brief must affirmatively
    argue that the court may consider those documents (incorporation by reference; integral
    document; judicial notice). Courts may ignore extrinsic materials that are not properly
    argued into the record.

16. **Omitting local rule compliance certification**: Many courts require a certificate of
    compliance (word count, font, format) appended to motions. Missing the certification
    can result in the motion being stricken without review.

17. **Anchoring on the weakest claim in the complaint**: Spending disproportionate brief
    space on the most easily defeated claim while inadequately briefing the claims that
    present stronger opposition arguments. Opposition will highlight the claims where your
    brief is weakest.

18. **Failing to anticipate the amendment-as-of-right maneuver**: Under Rule 15(a)(1),
    plaintiff may amend once as of right within 21 days of service of a 12(b) motion.
    If the plaintiff amends quickly to cure an obvious defect, your motion is mooted.
    Consider whether the motion is timed appropriately or whether plaintiff's likely
    amendment would produce a stronger complaint.

---

## Writing Standards

Apply these standards before delivering any argument outline or analysis:

**Precision over length**: Every sentence should earn its place. Delete throat-clearing
introductions ("It is well-established that...") and repetition of points already made.

**Standard of review first**: Every argument section must open with the governing legal
standard, stated precisely and with citation. The standard frames the entire analysis.

**Active voice**: "The court lacks jurisdiction" not "Jurisdiction is lacking."
"Plaintiff failed to allege" not "The allegations are insufficient."

**Quote selectively, accurately**: When quoting cases, use accurate quotations with
pinpoint citations. Do not paraphrase key doctrinal language; courts and opposing counsel
will check exact language.

**Cite primary sources**: Rely on Supreme Court and circuit court authority. District
court decisions are persuasive at best; do not lead arguments with them.

**Avoid loaded rhetoric**: "Frivolous," "meritless," "absurd" — these characterizations
inflame without persuading and invite counter-characterization. State the deficiency
precisely: "The complaint alleges no facts from which a court could infer..."

**Plain language for courts**: Avoid unnecessary legalese. Write for a federal district
judge who reads hundreds of briefs per year. Clarity and organization create credibility.

**Self-cite internally**: When argument sections cross-reference each other (e.g., the
12(b)(1) section references the same factual deficiency analyzed in 12(b)(6)), use
internal cross-references rather than repeating the analysis.

**Quality gate before delivery**: Before returning any output, verify:

- [ ] Each cited case has a year, volume, and page number (or is marked `[VERIFY]`)
- [ ] Circuit splits are identified as such, not presented as universal rules
- [ ] All STRONG classifications have passed the Self-Interrogation 3-pass review
- [ ] Leave-to-amend analysis addresses futility expressly for 12(b)(6) recommendations
- [ ] Local rules compliance flags are included for the identified district

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for current circuit authority on the applicable 12(b) ground
- Verify that cited Supreme Court and circuit precedents remain good law
- Search for recent district court decisions in the specific forum applying relevant doctrine
- Check for recent amendments to FRCP rules or local rules affecting procedure

**Without legalcode-mcp:**

- Proceed using the authority in this skill, repository research, and available web sources
- Mark all case citations with `[VERIFY]` if not independently verified
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus on structural quality and argument organization rather than comprehensive
  case-law marshaling; flag for attorney research completion before filing

---

## Glass Box Audit Trail

Every output generated by this skill should include the following audit record. Complete
each field based on the engagement.

```yaml
glass_box:
  skill_name: "legalcode-motion-to-dismiss-drafter"
  mode: "Drafting | Analysis | Both"
  case_caption: "[Plaintiff v. Defendant, No. ___]"
  district: "[e.g., S.D.N.Y.]"
  circuit: "[e.g., Second Circuit]"
  complaint_version: "[Initial / First Amended / Second Amended]"
  grounds_analyzed:
    - "12(b)(1): [specify basis — standing / SMJ / other]"
    - "12(b)(2): [general / specific / stream of commerce]"
    - "12(b)(3): [general venue / forum selection clause]"
    - "12(b)(4): [if applicable]"
    - "12(b)(5): [if applicable]"
    - "12(b)(6): [all claims / specific claims — list]"
    - "12(b)(7): [if applicable]"
  waiver_check_completed: true | false
  local_rules_checked: "[District local rules reviewed; specific rules applied]"
  extrinsic_materials_considered: "[List or 'None']"
  conversion_risk: "Yes — [materials identified] | No"
  pre_motion_conference_required: "Yes — [local rule] | No | Unknown — verify"
  legalcode_mcp: "Connected | Not connected"
  grounds_classification:
    "12(b)(1)": "STRONG | VIABLE | MARGINAL | WEAK | Not Analyzed"
    "12(b)(2)": "STRONG | VIABLE | MARGINAL | WEAK | Not Analyzed"
    "12(b)(3)": "STRONG | VIABLE | MARGINAL | WEAK | Not Analyzed"
    "12(b)(4)": "STRONG | VIABLE | MARGINAL | WEAK | Not Analyzed"
    "12(b)(5)": "STRONG | VIABLE | MARGINAL | WEAK | Not Analyzed"
    "12(b)(6)": "STRONG | VIABLE | MARGINAL | WEAK | Not Analyzed"
    "12(b)(7)": "STRONG | VIABLE | MARGINAL | WEAK | Not Analyzed"
  overall_confidence: "HIGH | MEDIUM | LOW"
  confidence_rationale: "[Brief explanation of overall confidence assessment]"
  citations_verified: "[N VERIFIED / N UNVERIFIED — flag all UNVERIFIED for attorney review]"
  self_interrogation_applied: "Yes — [grounds] | N/A"
  limitations:
    - "[Any scope limitations, factual assumptions, or caveats specific to this engagement]"
  attorney_review_required: true
  reviewer: "AI-assisted — requires qualified legal review before filing"
```

---

## Output Format Template

Deliver analysis in the following structure. Omit sections that do not apply.

---

```markdown
# Motion to Dismiss Analysis — [Case Caption]

**District**: [Court Name]
**Circuit**: [Circuit]
**Date**: [Date]
**Skill Version**: legalcode-motion-to-dismiss-drafter

---

## Executive Summary

**Overall Assessment**: [1–2 sentences on the strength of available grounds]
**Recommended Filing**: [Yes / Yes with caveats / No — explain briefly]
**Lead Ground(s)**: [Strongest ground(s) for the motion]
**Grounds by Classification**:
| Ground | Classification | Confidence | Notes |
|--------|---------------|------------|-------|
| 12(b)(1) | STRONG / VIABLE / MARGINAL / WEAK | 0.XX | [Brief rationale] |
| 12(b)(2) | — | — | [If not analyzed] |
| 12(b)(3) | — | — | |
| 12(b)(6) | STRONG / VIABLE / MARGINAL / WEAK | 0.XX | [Brief rationale per claim] |
| [Other grounds] | | | |

---

## Procedural Screen

**Waiver Status**:

- 12(b)(2)–(5): [Available / WAIVED — explain]
- 12(b)(6)–(7): Available (non-waivable)

**Local Rule Requirements**:

- Pre-motion conference letter: [Required (Local Rule ___) / Not required / Verify]
- Word/page limit: [X words / X pages per Local Rule ___]
- Filing deadline: [21 days from service = date; adjust for government defendants]

**Rule 12(g) Consolidation**: [List all grounds to be included in single motion]

---

## Argument Outlines

### Argument I: [Ground — e.g., This Court Lacks Subject Matter Jurisdiction]

[See Argument Block Template for the applicable ground from Step 4]

**Classification**: [STRONG / VIABLE / MARGINAL]
**Confidence**: [0.XX]
**Key Authority**:

- [Case 1, citation, key holding]
- [Case 2, citation, key holding]

**Argument Outline**:
[Numbered outline following the argument block template]

**Anticipated Opposition**:

- [Opposition argument 1] → [Rebuttal]
- [Opposition argument 2] → [Rebuttal]

**Reply Focus**:
[What to address in reply brief; what to ignore]

---

### Argument II: [Next Ground]

[Repeat format]

---

## Leave-to-Amend Analysis (12(b)(6) only)

**Recommendation**: Dismiss with prejudice / Dismiss without prejudice / Oppose leave to amend

**Futility Analysis by Claim**:
| Claim | Defect | Can Amendment Cure? | Reasoning |
|-------|--------|---------------------|-----------|
| [Claim 1] | [Element missing / Legally foreclosed] | No / Yes | [Foman analysis] |
| [Claim 2] | [Defect description] | No / Yes | |

---

## Extrinsic Materials Analysis

**Documents Considered**:
| Document | Basis for Consideration | Circuit Authority |
|----------|------------------------|-------------------|
| [Exhibit A] | Attached to complaint (Rule 10(c)) | Permissible |
| [Contract] | Incorporated by reference (complaint ¶ \_\_\_) | [Circuit rule] |

**Conversion Risk**: [None / Yes — identify materials and proposed handling]

---

## Glass Box Audit Trail

[Paste completed YAML template from the Glass Box section above]
```

---

## Localization Notes

**State Courts**: Do not use this skill for state court motions to dismiss without
substantial verification. State procedural rules vary widely:

- Many states use notice pleading under a Conley-type standard (rejected in federal courts)
- Some states have adopted Twombly/Iqbal (California: _Doe v. City of Los Angeles_, 2007
  pre-Iqbal; others have adopted plausibility post-2009 — [VERIFY state-specific status])
- Demurrer practice (California, some other states) is functionally equivalent to 12(b)(6)
  but with distinct procedural rules
- State court standing requirements may differ from Article III federal standing

**International Arbitration Context**: If the case involves a motion to dismiss in favor
of arbitration under the Federal Arbitration Act (9 U.S.C. § 1 et seq.), the analysis
differs from 12(b) practice — see the `legalcode-arbitration-clause-review` skill.

**Patent Cases**: Patent cases in federal court have heightened pleading requirements for
claim construction and infringement. Consult Federal Circuit authority, which controls
patent-specific procedural questions.

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis based on:

- FRCP Rules 8, 9, 12, 15, 19, 56 (current text)
- Supreme Court authority: _International Shoe_ (1945), _Bell Atl. Corp. v. Twombly_ (2007),
  _Ashcroft v. Iqbal_ (2009), _Daimler AG v. Bauman_ (2014), _Goodyear Dunlop_ (2011),
  _Bristol-Myers Squibb_ (2017), _Ford Motor Co. v. Montana Eighth Judicial District_ (2021),
  _Walden v. Fiore_ (2014), _TransUnion LLC v. Ramirez_ (2021), _Mallory v. Norfolk S. Ry._
  (2023), _Atlantic Marine Construction_ (2013), _Tellabs v. Makor_ (2007)
- Repository patterns from `legalcode-summary-judgment-analysis`,
  `legalcode-complaint-drafter`, `legalcode-opposition-brief-drafter`
- 2-agent research team (structural analysis + legal research)
- Jurisdiction-agnostic with US federal FRCP scope; [JURISDICTION-SPECIFIC] markers for
  circuit-specific rules and local rule compliance
- All citations marked `[VERIFY]` require attorney verification before reliance
