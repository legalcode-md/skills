---
name: legalcode-class-certification-analysis
description: Analyze class certification requirements under FRCP Rule 23 for plaintiff and defense counsel.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Analyze class certification requirements under FRCP Rule 23 for plaintiff and defense counsel. Evaluates all Rule 23(a) prerequisites (numerosity, commonality, typicality, adequacy of representation) and Rule 23(b) class types (23(b)(1) prejudice classes, 23(b)(2) injunctive/declaratory relief, 23(b)(3) predominance and superiority). Covers ascertainability doctrine and the circuit split between administrative feasibility and objective identifiability standards. Performs predominance analysis applying Wal-Mart v. Dukes and Comcast v. Behrend rigorous-analysis framework, superiority evaluation against individual litigation and arbitration, Daubert challenges to class certification experts (circuit-split aware), merits-overlap doctrine, settlement class certification under Amchem, cy pres considerations, Article III standing after TransUnion v. Ramirez, CAFA jurisdiction and exceptions, state class action variations (CA CCP § 382, NY CPLR Article 9), subclass strategy, and Rule 23(f) interlocutory appeal criteria. Produces dual-perspective certification strength assessment, element-by- element classification (STRONG/MODERATE/WEAK/FATAL), opposition arguments, expert strategy, and prioritized strategic recommendations for both plaintiff and defense. Use for class certification briefing, opposition preparation, or pre-filing class viability assessment.


# Legalcode Class Certification Analysis

> **Disclaimer**: This skill provides a framework for AI-assisted class certification
> analysis under FRCP Rule 23. It does not constitute legal advice. All outputs should
> be reviewed by a qualified attorney licensed in the relevant jurisdiction before
> relying on them in any litigation. Class action law evolves rapidly through circuit
> court decisions and Supreme Court review; verify current circuit precedent before
> relying on any doctrinal statement. Statutory and case law references cited from
> memory carry hallucination risk — verify against Westlaw, Lexis, or authoritative
> government sources before citing in any brief or filing. This skill covers US federal
> procedure primarily; state class action analysis requires separate jurisdiction-specific
> research.

---

## Purpose and Scope

Use this skill to produce a structured, dual-perspective class certification analysis
supporting class certification motions, oppositions, reply briefs, pre-filing viability
assessments, and settlement class submissions. The analysis evaluates every Rule 23
element with element-by-element strength classification, identifies the strongest and
weakest points for each side, and delivers prioritized strategic recommendations.

**Covers:**

- Rule 23(a) threshold prerequisites: numerosity, commonality, typicality, adequacy of representation
- Rule 23(b)(1)(A): incompatible-standards-of-conduct prejudice class
- Rule 23(b)(1)(B): limited-fund and impairment-of-interests class
- Rule 23(b)(2): injunctive and declaratory relief class (Wal-Mart cohesiveness requirement)
- Rule 23(b)(3): damages class — predominance and superiority analysis
- Rule 23(c)(4): issue certification as an alternative or supplement
- Rule 23(c)(5): subclass strategy and intraclass conflict management
- Ascertainability doctrine — circuit split between administrative feasibility and objective identifiability
- Predominance analysis — common vs. individual questions, Comcast damages model alignment, statistical/representative evidence under Tyson Foods
- Superiority evaluation — four statutory factors, class vs. individual suits, class vs. arbitration
- Daubert challenges to class certification expert testimony — circuit-split aware application
- Merits-overlap doctrine under Wal-Mart and Comcast rigorous-analysis framework
- Settlement class considerations: Amchem heightened scrutiny, cy pres awards, preliminary approval
- Article III standing for class members post-TransUnion v. Ramirez
- CAFA jurisdiction and exceptions: home state, local controversy, discretionary
- State class action variations: California CCP § 382, New York CPLR Article 9
- Rule 23(f) interlocutory appeal — petition criteria and circuit standards
- Named plaintiff selection strategy and adequacy attacks
- Expert retention and Daubert defense strategy

**Does not:**

- Draft the certification motion or opposition brief itself (see `legalcode-motion-to-dismiss-drafter`, `legalcode-brief-analyzer`, `legalcode-opposition-brief-drafter`)
- Analyze the underlying merits of individual class claims beyond what the certification inquiry requires
- Cover securities fraud class actions under the PSLRA (different framework — fraud-on-the-market presumption, loss causation) without noting the distinction
- Cover mass tort class actions involving predominating individual injury questions without noting the Amchem settlement class alternative
- Analyze non-US collective action procedures (EU Directive 2020/1828, UK representative actions, Australian representative proceedings)
- Provide legal advice or substitute for licensed class action counsel

**Related skills:**

- `legalcode-litigation-risk-assessment` — Four-dimensional litigation risk framing; run before this skill to set risk context
- `legalcode-early-case-assessment` — Element-level merits depth; feeds class-wide harm analysis
- `legalcode-summary-judgment-analysis` — Often filed concurrently with or after certification; related strategic timing
- `legalcode-settlement-negotiation` — Post-certification settlement; consumes certification strength assessment
- `legalcode-damages-calculation` — Damages model construction and class-wide damages methodology

---

## Jurisdiction and Governing Law

**Primary framework:** Federal Rules of Civil Procedure Rule 23, as interpreted by the
Supreme Court and the relevant circuit court of appeals. Class certification analysis is
inherently circuit-specific — the applicable circuit's precedent on commonality,
ascertainability, Daubert application, and predominance frequently determines the outcome.

**Identify the circuit at Step 1.** Circuit-split issues are flagged throughout this skill
with `[CIRCUIT-SPLIT]` markers. Resolve every circuit-split issue based on the controlling
circuit precedent, not the majority rule.

**[JURISDICTION-SPECIFIC]** For state court class actions:

- **California**: CCP § 382; courts apply a more liberal standard and resolve close
  questions in favor of certification; no equivalent of 23(b)(1)/(b)(2)/(b)(3)
  rigid categories; community of interest test
- **New York**: CPLR Article 9 (§§ 901-909); no rigid class categories; courts apply a
  flexible standard; notice is discretionary rather than automatic; opt-out rights
  available regardless of relief sought; not updated since 1966 adoption unlike FRCP 23
- **Other states**: Many follow FRCP 23 substantially; check for state-specific
  ascertainability requirements, superiority equivalents, and settlement approval rules

**CAFA jurisdiction:** Where the amount in controversy exceeds $5 million, the proposed
class has 100 or more members, and minimal diversity exists, the action is removable to
federal court (28 U.S.C. § 1332(d)). CAFA exceptions can defeat federal jurisdiction
and return the case to state court — analyzed at Step 4.

---

## Interactive Clarification

This skill uses **interactive clarification** (marked **⟁ CLARIFY**) at key decision
points where the answer materially changes the analysis or strategy recommendation.
The skill pauses and asks when:

- The perspective (plaintiff/defense/neutral), stage, or class type is unclear
- Circuit assignment is uncertain and circuit-specific precedent is outcome-determinative
- The class definition has not been provided and must be supplied before analysis
- Key documents (complaint, class definition, expert reports) are missing
- Settlement vs. litigated class certification changes the analytical framework

For batch or non-interactive runs, proceed with stated defaults and mark assumptions
explicitly at each CLARIFY point.

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:

- **Motion papers**: Plaintiff's motion for class certification with supporting brief and declarations
- **Opposition**: Defense's opposition to class certification with supporting brief
- **Both sides**: Full certification record — motion, opposition, reply, declarations, and expert reports
- **Pre-filing materials**: Draft complaint, proposed class definition, and factual summary
- **Settlement submission**: Motion for preliminary approval with settlement class definition

**Minimum required information:**

1. **Class definition** (proposed or actual — cannot proceed without this)
2. **Claims asserted** (legal theories and statutory bases)
3. **Factual background** (sufficient to evaluate commonality and typicality)
4. **Perspective** (plaintiff, defense, or neutral analysis)
5. **Circuit** (for circuit-split issues)

If the class definition is not provided, request it before proceeding. A poorly drafted
class definition is one of the most common sources of certification defeat.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask these questions. Skip any already answered by the input:

1. **Perspective**:
   - Options: Plaintiff/Class Counsel (analyze strength of case for certification), Defense Counsel (identify weakest elements and best opposition arguments), Neutral Analysis (balanced assessment for court, mediator, or advisor)
   - _Why this matters_: Determines emphasis, tone, and prioritization of findings.

2. **Certification stage**:
   - Options: Pre-filing viability assessment, Drafting certification motion, Responding to certification motion, Pre-hearing strategy review, Settlement class submission, Post-ruling Rule 23(f) appeal assessment
   - _Why this matters_: Stage determines what evidence is available and what arguments are timely.

3. **Class type sought** (if plaintiff) or **class type to oppose** (if defense):
   - Options: 23(b)(1)(A) mandatory/prejudice, 23(b)(1)(B) limited fund, 23(b)(2) injunctive, 23(b)(3) damages, 23(c)(4) issue certification, Multiple types or unclear
   - _Why this matters_: Different requirements and doctrinal standards apply.

4. **Expert testimony** available or expected:
   - Options: Full expert reports already submitted, Expert declarations submitted (preliminary), Expert strategy TBD, No expert testimony contemplated
   - _Why this matters_: Daubert analysis and predominance analysis are expert-intensive.

5. **Settlement class** or **litigated certification**:
   - Options: Litigated certification motion, Settlement class (seeking preliminary approval), Both (certification motion and conditional settlement discussion)
   - _Why this matters_: Amchem/Ortiz settlement class standards differ from litigated class standards — manageability is suspended but fairness scrutiny intensifies.

6. **Circuit**:
   - Identify the circuit court of appeals that would hear an appeal from the district court. This is essential for ascertainability doctrine, Daubert application, and other circuit-split issues.
   - Options: First, Second, Third, Fourth, Fifth, Sixth, Seventh, Eighth, Ninth, Tenth, Eleventh, D.C. Circuit, Federal Circuit, Unknown/Mixed
   - _Why this matters_: Multiple doctrinal issues turn entirely on which circuit applies.

### Step 3: Load Class Definition and Litigation Record

Before substantive analysis, extract and record:

1. **Class definition** — Exact proposed class language, including:
   - Temporal boundaries (start and end dates)
   - Geographic scope (nationwide, state, district)
   - Product, service, or conduct identifier
   - Exclusions (employees, defendants, named counsel)

2. **Class definition red flags** — Identify immediately:
   - **Fail-safe class**: Class defined by merits outcome (e.g., "all persons who were wrongfully denied"). Such classes fail because membership cannot be determined without resolving the merits. [VERIFY circuit treatment — most reject fail-safe definitions but see _Boundas v. Abercrombie_ for Seventh Circuit nuance]
   - **Overbreadth**: Class so broad it includes persons with no claim or injury
   - **Precise measurement trap**: Class defined by individualized inquiry (e.g., "all persons who suffered actual damages")
   - **Statute of limitations problems**: Class period longer than applicable limitations period without tolling argument

3. **Claims and legal theories** — Map each claim to its elements and identify which elements will present common vs. individual proof

4. **Named plaintiffs** — For each named plaintiff: role, claim type, relationship to class, potential atypicality issues

5. **Key documents** — Complaint, class certification motion, declarations, expert reports, key contracts or policies at issue

### Step 4: CAFA Jurisdiction Screening

Before Rule 23 analysis, screen for CAFA jurisdiction issues. CAFA jurisdiction affects which court's certification standards apply and may be outcome-determinative for forum strategy.

**CAFA basics** (28 U.S.C. § 1332(d)):

- Amount in controversy: $5 million aggregate (sum of all individual claims)
- Minimal diversity: At least one class member diverse from at least one defendant
- Class size: 100 or more class members

**CAFA mandatory exceptions** (court must remand):

- **Home State Exception**: Two-thirds or more of proposed class citizens of the forum state AND primary defendants citizens of the forum state
- **Local Controversy Exception**: Greater than two-thirds of proposed class citizens of forum state, at least one local defendant whose alleged conduct forms significant basis of claims and who faces potential significant relief, principal injuries occurred in forum state, and no similar class action filed against defendants within 3 years

**CAFA discretionary exceptions** (court may decline jurisdiction):

- Between one-third and two-thirds of proposed class citizens of forum state AND primary defendants citizens of forum state

**Strategic CAFA considerations**:

- **Plaintiffs**: State court certification standards may be more favorable (especially California and New York) — analyze whether a CAFA exception applies
- **Defense**: Federal court generally preferred; preserve CAFA removal rights by filing timely notice (30 days from removability becoming apparent per 28 U.S.C. § 1446(b)); CAFA jurisdiction survives certification denial (most circuits)
- **Jurisdictional challenge timing**: Jurisdictional challenges may be raised at any time; CAFA burden of proof on invoking party per most circuits

**⟁ CLARIFY** — If CAFA jurisdiction is contested or unclear, or if a forum-selection strategic analysis is desired, flag this for separate focused analysis before proceeding.

### Step 5: Rule 23(a) Prerequisites Analysis

Analyze all four Rule 23(a) prerequisites. Every prerequisite must be satisfied — failure on any one defeats certification regardless of Rule 23(b) analysis.

**Evaluation framework for each prerequisite:**

| Element      | Classification       | Meaning                                                                         |
| ------------ | -------------------- | ------------------------------------------------------------------------------- |
| **STRONG**   | Clearly satisfied    | Evidence sufficient; typical opposition arguments unlikely to prevail           |
| **MODERATE** | Satisfied with work  | Supportable but vulnerable to attack; needs strengthening arguments or evidence |
| **WEAK**     | Questionable         | Nontrivial risk of defeat on this element; identify specific deficiencies       |
| **FATAL**    | Likely not satisfied | Certification likely denied on this element without redesign                    |

#### 5.1 Numerosity (Rule 23(a)(1))

**Standard**: The class must be so numerous that joinder of all members is impracticable.

**Impracticability (not impossibility)**: Courts do not require impossibility of joinder; impracticability considers class size, geographic dispersion of class members, nature of the action, and practicality of individual member participation.

**Typical thresholds**:

- **40+ members**: Generally sufficient without extensive argument
- **21–40 members**: May be sufficient; geographic dispersion and small individual claim amounts help
- **Fewer than 21 members**: Typically insufficient; requires compelling facts on impracticability
- **No bright line**: Courts examine all circumstances; some courts have certified classes of as few as 14 members in extraordinary circumstances [VERIFY]

**Analysis points**:

- Quantify the proposed class size with specific evidence (company records, government data, statistical estimates)
- Geographic dispersion weighs toward impracticability even with smaller class
- Small individual damages amounts making individual suits economically irrational support impracticability
- Identify class members by objective criteria (avoid requiring individual inquiry to identify members — this also implicates ascertainability)
- Named defendant's records often contain the best class size evidence; request in discovery or address in certification motion

**Common challenges**:

- **Undercounting**: Defense argues plaintiff overstates class size by using overbroad class definition
- **Overcounting**: Defense argues class includes ineligible members reducing true class size
- **Geographically concentrated**: Defense argues joinder is practicable because all class members are local

**Classification drivers**: Class size alone rarely defeats certification if the class is substantial (40+); focus analysis on class definition precision for numerosity.

#### 5.2 Commonality (Rule 23(a)(2)) — Wal-Mart Framework

**Standard**: There must be questions of law or fact common to the class.

**Wal-Mart heightened standard** (_Wal-Mart Stores, Inc. v. Dukes_, 564 U.S. 338 (2011)):
The commonality requirement demands more than questions "common" in the sense that every class member suffered the same type of wrong. Plaintiffs must demonstrate that "the class members have suffered the same injury" and that determination of the common question will "generate common answers apt to drive the resolution of the litigation." The "common answer" requirement — not merely common questions — is the critical test.

The Court requires a "common contention" whose truth or falsity resolves an issue central to the validity of each class member's claim in one stroke. The alleged common contention must be capable of classwide resolution.

**The "glue" test**: What is the "glue holding the alleged reasons for [the defendant's action] together"? This is the central question after Wal-Mart. If each class member's claim requires individualized proof of the common question's resolution, the question does not truly bind the class.

**Merits overlap**: Wal-Mart confirmed that the "rigorous analysis" required for Rule 23 "will frequently entail some overlap with the merits of the plaintiff's underlying claim." The court can and must examine evidence bearing on the common question even if that evidence also goes to the merits.

**Analysis points**:

1. **Identify the specific common contention**: State precisely the common question and how its resolution drives the litigation. Avoid generic common questions (e.g., "whether defendant was negligent") that could be answered differently for each class member.
2. **Articulate the common answer mechanism**: How does resolution of the common question resolve liability/entitlement for all class members simultaneously?
3. **Evidence supporting the common question**: Identify the classwide evidence (company-wide policies, systematic conduct, statistical proof) that answers the common question without individualized inquiry.
4. **Distinguish Wal-Mart's discretionary-policy problem**: Where defendant gave managers discretion to make individualized decisions, commonality fails because there is no company-wide "glue." Plaintiff must show a common policy or systematic practice driving the alleged wrong.

**Common evidence types supporting commonality**:

- Uniform company-wide policy or practice applied to all class members
- Standard form contract applied identically
- Algorithm or automated system generating alleged wrong
- Laboratory or scientific evidence applicable to all class members (e.g., product defect)
- Statistical analysis demonstrating classwide pattern

**Defense attacks on commonality**:

- Individualized decision-making: Each class member's experience was different
- Manager/agent discretion: No uniform policy existed; each decision was individual
- Varied exposure: Class members experienced the common policy in different ways, producing different outcomes

**⟁ CLARIFY** — If the factual record is insufficient to identify the specific common contention and the evidence that would answer it, request additional information before classifying this element.

#### 5.3 Typicality (Rule 23(a)(3))

**Standard**: The claims or defenses of the representative parties must be typical of the claims or defenses of the class.

**What typicality requires**: The named plaintiff's claims must arise from the same event, practice, or course of conduct giving rise to class claims, and be based on the same legal or remedial theory. Claims need not be factually identical — "typical" does not mean "identical."

_Hanon v. Dataproducts Corp._, 976 F.2d 497 (9th Cir. 1992): Typicality is satisfied when the named plaintiff's claim "arises from the same course of events and each class member makes similar legal arguments to prove the defendant's liability." [VERIFY]

**Merge with commonality**: The Supreme Court noted that "the commonality and typicality requirements of Rule 23(a) tend to merge." Both serve to ensure the named plaintiff's and class members' interests are sufficiently aligned.

**Atypicality defects — most dangerous:**

- **Unique defenses**: If defendant has a defense specific to the named plaintiff not applicable to the class (e.g., statute of limitations expired for named plaintiff but not class; contractual release; comparative fault specific to named plaintiff), typicality fails.
- **Factual distinctions**: Named plaintiff's factual circumstances differ materially from typical class member (different product version, different transaction terms, different damages theory)
- **Credibility problems**: Significant credibility issues with named plaintiff may support an atypicality argument, though courts are divided on whether credibility alone defeats typicality

**Defense tactics on typicality**:

- Identify unique defenses applicable only to the named plaintiff
- Attack the named plaintiff's standing or injury
- Argue named plaintiff's damages are atypical (e.g., named plaintiff has no damages while class does, or vice versa)
- Depose named plaintiff aggressively before certification briefing to develop atypicality evidence

**Named plaintiff selection (plaintiff strategy)**:

- Select named plaintiffs whose claims are most representative of typical class members
- Avoid named plaintiffs with contractual releases, statute of limitations problems, or unique factual circumstances
- Multiple named plaintiffs reduce the risk of typicality defeat — if one is disqualified, others may survive
- Consider whether named plaintiff's transaction, exposure, or injury type matches the majority of class members

#### 5.4 Adequacy of Representation (Rule 23(a)(4))

**Standard**: The representative parties must fairly and adequately protect the interests of the class.

**Two-part adequacy inquiry**:

1. **Named plaintiff adequacy**: Are there conflicts of interest between the named plaintiff and class members? Does the named plaintiff have sufficient interest in the outcome to advocate vigorously?
2. **Class counsel adequacy**: Do proposed class counsel have the competence and resources to conduct the litigation vigorously? (FRCP 23(g) separately governs class counsel appointment)

**Conflict of interest analysis**:

- **Intraclass conflicts**: Named plaintiff has interests that conflict with the interests of absent class members (e.g., named plaintiff's settlement preference differs from class members'; named plaintiff benefits from subclass treatment others don't)
- **Entrepreneurial plaintiff problem**: Named plaintiff has minimal stake in the outcome; may be controlled by class counsel
- **Competing interests**: Named plaintiff has business relationship with defendant creating conflicting interests

**Class counsel adequacy** (FRCP 23(g) factors):

- Work done in identifying or investigating potential claims
- Experience in handling class actions and other complex litigation
- Knowledge of applicable law
- Resources committed to representing the class

**Defense attacks on adequacy**:

- Expose named plaintiff's lack of involvement in litigation decisions
- Identify potential intraclass conflicts (particularly in 23(b)(3) classes seeking damages)
- Challenge class counsel's expertise or resources
- Identify prior class action settlements with inadequate results by same counsel
- Demonstrate that named plaintiff lacks basic understanding of claims
- Show that named plaintiff's interests favor early settlement over maximum recovery

### Step 6: Rule 23(b) Class Type Analysis

After establishing all four 23(a) prerequisites, analyze the applicable Rule 23(b) class type(s). The plaintiff must satisfy at least one 23(b) category.

#### 6.1 Rule 23(b)(1)(A): Incompatible Standards Class

**Standard**: Prosecuting separate actions would create a risk of inconsistent or varying adjudications that would establish incompatible standards of conduct for the party opposing the class.

**Application**: Less commonly used for plaintiff class actions; primarily applies where a defendant's conduct toward non-class members depends on uniform legal treatment (e.g., challenging a single legal standard applied across the class). The defendant — not class members — would face incompatible conduct standards.

**Examples**: Challenges to a government benefit determination scheme; challenges to a pension plan administrator's uniform policy; antitrust injunctive relief cases.

**Note**: (b)(1)(A) classes are mandatory — no opt-out right.

#### 6.2 Rule 23(b)(1)(B): Limited Fund Class

**Standard**: Prosecuting separate actions would create a risk that adjudications with respect to individual class members would be dispositive of the interests of other members not party to the individual adjudications, or substantially impair or impede their ability to protect their interests.

**Limited fund theory** (_Ortiz v. Fibreboard Corp._, 527 U.S. 815 (1999)): A mandatory class may be certified where a genuine limited fund exists — the aggregate assets available are insufficient to satisfy all potential claims. The _Ortiz_ Court imposed three requirements: (1) the fund's totality must be identified, (2) the whole fund must be devoted to the limited class, and (3) the claimants to the fund must be treated equitably among themselves.

**Application**: Insurance policy limits; corporate assets in insolvency-adjacent situations; environmental cleanup cost pools. _Ortiz_ significantly limited the (b)(1)(B) limited fund theory; courts post-_Ortiz_ apply it narrowly.

**Note**: (b)(1)(B) classes are mandatory — no opt-out right.

#### 6.3 Rule 23(b)(2): Injunctive/Declaratory Relief Class

**Standard**: The party opposing the class has acted or refused to act on grounds that apply generally to the class, so that final injunctive relief or corresponding declaratory relief is appropriate respecting the class as a whole.

**Wal-Mart's (b)(2) limitation**: The Supreme Court in _Wal-Mart_ held that Rule 23(b)(2) does not apply when class members would be entitled to individualized monetary relief. The "cohesiveness" of the class around the injunctive remedy is required — the injunction or declaration must be equally applicable to each class member.

**Key analysis points**:

- The class must be "cohesive" around the injunctive remedy
- Individual damages claims may destroy (b)(2) certification if they predominate over the injunctive relief sought
- Mixed cases (injunction + individualized damages): Generally cannot certify the entire case as (b)(2); may need to bifurcate liability/injunctive phase certified under (b)(2) from individualized damages determined later
- **Civil rights / employment discrimination**: Traditional home of 23(b)(2) classes; _Wal-Mart_ narrowed this for back-pay claims
- **No opt-out right**: (b)(2) classes are mandatory; this limits class member autonomy and is a strategic consideration
- **No individualized damages**: If class seeks monetary relief beyond incidental to injunctive relief, (b)(2) is inappropriate

**Note**: (b)(2) classes are mandatory — no opt-out right.

#### 6.4 Rule 23(b)(3): Predominance and Superiority — The Core Analysis

**Standard**: Questions of law or fact common to class members predominate over any questions affecting only individual members, AND a class action is superior to other available methods for fairly and efficiently adjudicating the controversy.

##### Predominance Analysis

**Higher bar than commonality**: Predominance asks more than whether common questions exist — it asks whether common questions dominate the litigation compared to individual issues. _Amchem Products, Inc. v. Windsor_, 521 U.S. 591 (1997).

**The Comcast requirement** (_Comcast Corp. v. Behrend_, 569 U.S. 27 (2013)):

- Damages methodology must match the theory of liability
- Plaintiffs must submit a damages model that measures only those damages attributable to the specific theory of liability that survives certification
- A damages model that calculates aggregate damages across multiple theories — only some of which survive — fails Comcast
- The model must be capable of class-wide administration using common proof
- Plaintiffs must demonstrate the model with more than boilerplate expert testimony — case-specific evidence of workability is required

**Applying the Comcast framework**:

1. Identify the specific liability theory (or theories) for which certification is sought
2. Map each theory to a damages calculation methodology
3. Verify the damages methodology is cabined to the surviving theory
4. Verify the methodology can be applied using common proof across the class
5. Identify what individualized calculations, if any, are required and whether they destroy predominance

**Individual damages calculations and predominance**:

- Individual damages calculations alone do not necessarily defeat predominance
- Courts have certified classes where liability is common and damages are individualized, reserving damages calculations for a subsequent phase
- _[CIRCUIT-SPLIT]_: Courts vary on how much individualized damages inquiry defeats predominance; Seventh Circuit is generally more permissive; Second Circuit provides frameworks for bifurcation

**Statistical/representative evidence** (_Tyson Foods, Inc. v. Bouaphakeo_, 577 U.S. 442 (2016)):

- Representative or statistical evidence may be used at class certification and trial where use of such evidence is permissible under the substantive law governing the claim
- _Tyson Foods_ limited _Wal-Mart_'s implication that statistical evidence is categorically impermissible
- Key question: Could individual plaintiffs have introduced the statistical evidence in their own individual suits? If yes, class use is permissible
- Defense strategy: Challenge the statistical methodology and demonstrate that the evidence cannot substitute for individualized proof

**Common questions that support predominance** (examples):

- Whether a product is defective (if a single defect affects all products)
- Whether a disclosure was materially false or misleading (securities fraud, subject to PSLRA)
- Whether a uniform contract provision is enforceable
- Whether a uniform company policy violated the law
- Whether an algorithm or automated system generated a uniform wrong

**Individual questions that undermine predominance** (examples):

- Causation varying by class member exposure, transaction, or circumstances
- Reliance required on an individualized basis (but see fraud-on-the-market presumption in securities fraud)
- Injury varying substantially across class members
- Damages requiring individualized assessment of harm
- Affirmative defenses individualized to particular class members

**TransUnion standing overlay** (_TransUnion LLC v. Ramirez_, 141 S. Ct. 2190 (2021)):

- Every class member must have Article III standing to recover individual damages
- Post-_TransUnion_, classes containing members who suffered no concrete injury fail standing requirements
- Plaintiff strategy: Define class to include only persons who suffered concrete injury-in-fact
- Defense strategy: Challenge whether all class members suffered actual (not merely risk of) harm; attack class definition breadth; argue typicality, adequacy, and predominance are undermined where standing varies across class

##### Superiority Analysis

**Four statutory superiority factors** (Rule 23(b)(3)(A)-(D)):

1. **Class member interest in individual suits**: The interest of class members in individually controlling the prosecution or defense of separate actions — weighs against class if individual claims are large enough to incentivize individual suits
2. **Pending litigation**: The extent and nature of any litigation concerning the controversy already begun by or against class members — prior individual suits may undermine superiority
3. **Desirability of concentration**: The desirability or undesirability of concentrating litigation in the particular forum — weighs in favor where all parties and evidence are in or near the forum
4. **Manageability**: The likely difficulties in managing a class action — complex individualized issues create manageability problems; trial plan required

**Class action vs. individual suits**:

- Small individual damages make individual suits economically irrational → strongly supports superiority
- Large individual damages undermine superiority because individual suits are viable
- Named plaintiff's counsel fees in individual cases vs. class action recovery — courts scrutinize incentive alignment

**Class action vs. arbitration** (_[JURISDICTION-SPECIFIC]_):

- Where class members' claims are subject to arbitration agreements with class action waivers, courts must determine arbitrability before certification
- _AT&T Mobility LLC v. Concepcion_, 563 U.S. 333 (2011): Class action waivers in consumer arbitration agreements are generally enforceable under the FAA
- _Epic Systems Corp. v. Lewis_, 584 U.S. 497 (2018): Class/collective action waivers in employment arbitration agreements are enforceable under the FAA
- **Ending Forced Arbitration of Sexual Assault and Sexual Harassment Act of 2022** (Pub. L. 117-90): Sexual assault and sexual harassment claims cannot be compelled to individual arbitration, enabling class treatment [VERIFY scope]
- Defense strategy: Move to compel arbitration before certification; class action waiver in applicable agreements
- Plaintiff strategy: Challenge arbitration agreement enforceability (unconscionability, notice defects, delegation clause enforceability)

**Manageability and trial plan**:

- Courts may require a trial plan demonstrating how the class action would actually be tried
- A class action that is unmanageable at trial may not satisfy superiority
- Issue certification under 23(c)(4) can separate manageable common issues from unmanageable individual issues
- **For settlement classes**: Manageability concerns are suspended — the Amchem/Ortiz test focuses on fairness, not manageability

### Step 7: Ascertainability Assessment

**⟁ CLARIFY**: Before applying ascertainability standards, identify the controlling circuit. The ascertainability doctrine is deeply circuit-split and the applicable standard is entirely circuit-dependent.

**[CIRCUIT-SPLIT] Ascertainability circuit alignment:**

| Circuit      | Standard                                                                 | Key Cases                                                                                       |
| ------------ | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| **First**    | Administrative feasibility required                                      | _In re Asacol Antitrust Litig._ (2018) [VERIFY]                                                 |
| **Third**    | Strict: administrative feasibility of identifying class members required | _Byrd v. Aaron's Inc._ (3d Cir. 2016); _In re Niaspan Antitrust Litig._ (3d Cir. 2023) [VERIFY] |
| **Fourth**   | Administrative feasibility required                                      | _EQT Production Co. v. Adair_ (4th Cir.) [VERIFY]                                               |
| **Second**   | Objective criteria only; no administrative feasibility requirement       | _Brecher v. Republic of Argentina_ (2d Cir. 2015) [VERIFY]                                      |
| **Sixth**    | No standalone administrative feasibility requirement                     | Joined majority [VERIFY]                                                                        |
| **Seventh**  | No standalone administrative feasibility requirement                     | _Mullins v. Direct Digital, LLC_ (7th Cir. 2015) [VERIFY]                                       |
| **Eighth**   | No strict ascertainability requirement                                   | Joined majority [VERIFY]                                                                        |
| **Ninth**    | No standalone administrative feasibility requirement                     | _Briseno v. ConAgra Foods, Inc._ (9th Cir. 2017) [VERIFY]                                       |
| **Eleventh** | No standalone administrative feasibility requirement                     | Joined majority [VERIFY]                                                                        |

**Administrative feasibility standard (minority: 1st, 3rd, 4th)**:

- Class definition must provide an administratively feasible mechanism for identifying class members without extensive individual inquiry
- Cannot rely on self-identification by class members (affidavits) alone
- Defendant's records must enable identification
- **Plaintiff strategy**: Identify objective, verifiable data sources for class member identification
- **Defense strategy**: Demonstrate that class member identification requires individualized inquiry into each claimant's circumstances

**Objective criteria standard (majority: 2nd, 6th, 7th, 8th, 9th, 11th)**:

- Class must be defined by objective criteria that make class membership determinable without reference to the merits
- No separate administrative feasibility inquiry
- Self-identification/affidavits may be permissible
- Rule 23(b)(3)(D)'s "likely difficulties in managing a class action" factor addresses administrative concerns within the superiority analysis

**[CIRCUIT-SPLIT] Fail-safe class doctrine:**
Most circuits reject class definitions that make membership turn on a merits determination (fail-safe classes). A class defined as "all persons who were wrongfully denied benefits" cannot be identified without resolving the merits. Courts generally require class definitions to use objective, non-merits-dependent criteria.

### Step 8: Daubert and Expert Evidence Analysis

Expert testimony is typically required in 23(b)(3) damages class actions to support:

- Common injury or impact theory (antitrust, securities, consumer fraud cases)
- Damages methodology and class-wide measurement
- Statistical or regression analysis supporting commonality and predominance
- Scientific or technical evidence on product defect, disease causation, etc.

**[CIRCUIT-SPLIT] Daubert standard at class certification:**

| Standard                          | Circuits                                 | Description                                                                                                                       |
| --------------------------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Full Daubert** (majority trend) | 2nd, 3rd, 5th, 7th, 9th (emerging), 11th | Full Daubert reliability analysis required at certification stage; inadmissible expert opinion cannot support certification       |
| **Tailored/limited Daubert**      | 6th (historically), 8th                  | Daubert analysis limited to evaluating reliability for purposes of certification; full trial-admissibility standards not required |

**Recent development**: The Sixth Circuit signaled in 2024 that full Daubert review applies at class certification. [VERIFY current Sixth Circuit position]

**Expert testimony strategy — Plaintiff**:

1. Retain qualified experts with class action experience before certification briefing
2. Submit declarations (or full reports) supporting: (a) common impact/injury, (b) damages methodology aligned with liability theory (_Comcast_ compliance), (c) statistical methodology supporting commonality and predominance
3. Anticipate defense Daubert challenges; build in alternative methodologies
4. Demonstrate with specific data that the damages model is workable for this specific case — not just theoretically capable

**Expert testimony strategy — Defense**:

1. Retain rebuttal experts to challenge plaintiff's common impact and damages models
2. File Daubert challenges to plaintiff's experts before or with opposition brief
3. Challenge: (a) reliability of methodology, (b) whether model measures damages attributable only to the surviving liability theory, (c) data quality, (d) expert's qualifications for this specific analysis
4. Demonstrate that implementation of plaintiff's model requires individualized inquiry that defeats predominance

**Merits-overlap in expert analysis**:

- Courts must evaluate whether plaintiff's expert testimony is reliable for purposes of certification, even where that evaluation requires merits engagement
- Defense may not shield merits-based arguments from certification scrutiny by labeling them "merits issues"
- Plaintiff may not avoid substantive examination of expert methodology by labeling challenges "merits questions"

### Step 9: Settlement Class Considerations

**⟁ CLARIFY**: If this is a settlement class submission (preliminary or final approval), the analysis shifts to the Amchem framework.

**Settlement class framework** (_Amchem Products, Inc. v. Windsor_, 521 U.S. 591 (1997)):

- All Rule 23 requirements except manageability must be satisfied for a settlement class
- Courts apply **heightened scrutiny** to settlement classes because the adversarial process that normally tests certification arguments is absent
- The court acts as a "guardian" of absent class members' interests

**Rule 23(e) fairness review for settlement class**:
Courts evaluate whether the settlement is "fair, reasonable, and adequate" considering:

1. **Adequacy of representation**: Were class counsel and named plaintiffs adequate advocates?
2. **Arm's length negotiation**: Was the settlement reached through genuine arm's-length negotiation or a collusive process?
3. **Relief adequacy**: Does the settlement provide adequate relief given the risks, expenses, and complexity of continued litigation?
4. **Equitable treatment**: Is each class member treated equitably relative to other class members?

**Red flags for collusive settlement**:

- Disproportionately large attorneys' fees relative to class recovery
- Incentive payments to named plaintiffs far exceeding typical class recovery
- Cy pres-only settlement with no direct class member benefit
- "Reversionary" clauses returning unclaimed funds to defendant
- Quick settlement shortly after filing with no adversarial proceedings

**Cy pres awards** (_Frank v. Gaos_, 586 U.S. \_\_\_ (2019)):

- _Frank v. Gaos_ was remanded on Article III standing grounds without reaching the cy pres merits; the cy pres doctrine remains contested
- Courts continue to scrutinize cy pres awards; key concerns: nexus between cy pres recipients and class claims; conflicts of interest between cy pres recipients and class counsel/defendant
- Post-_Frank v. Gaos_, best practice: include at least some direct class member distribution alongside cy pres; select neutral cy pres recipients with clear nexus to claims [VERIFY current circuit treatment]

**Article III standing in settlement classes** (_TransUnion_ overlay):

- Settlement class cannot include members who lacked Article III standing, even in settlement context
- Defense strategy in opposing inadequate settlement: challenge whether class definition includes uninjured members who lack standing, defeating class certification

**Preliminary approval standard** (FRCP 23(e)(1)):
Courts send notice and schedule a final approval hearing where the proposed settlement "would likely be approved" and the proposed class "would likely be certified." Courts apply less scrutiny at preliminary approval than final approval.

### Step 10: Synthesize and Prioritize

After completing all element analyses, synthesize findings into a certification strength assessment.

**Overall certification prospect rating**:

| Rating       | Meaning                                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------------------ |
| **HIGH**     | All Rule 23 elements supported by strong evidence; no fatal weaknesses; realistic path to certification            |
| **MODERATE** | Most elements satisfied; one or more moderate weaknesses addressable with additional evidence or argument          |
| **LOW**      | One or more elements present significant risk; certification possible but requires redesign or additional evidence |
| **VERY LOW** | One or more elements likely cannot be satisfied; class definition redesign or theory change necessary              |

**⟁ CLARIFY**: If the analysis reveals a VERY LOW prospect on any single element, ask whether the user wants to pivot to: (a) an alternative class definition, (b) an alternative class type (e.g., 23(c)(4) issue certification, 23(b)(2) injunctive class), or (c) strategic alternatives to class certification.

---

## Classification Framework

### Element-Level Classification

For each Rule 23(a)/(b) element, assign:

| Code  | Label    | Standard                                                                          |
| ----- | -------- | --------------------------------------------------------------------------------- |
| **S** | STRONG   | Evidence clearly supports; typical opposition unlikely to prevail                 |
| **M** | MODERATE | Supportable; vulnerable to specific attack; needs targeted argument               |
| **W** | WEAK     | Nontrivial defeat risk; specific deficiencies identified                          |
| **F** | FATAL    | Likely cannot be satisfied without class definition change or additional evidence |

### Opposition Vulnerability Classification

For defense analysis, classify each element:

| Code         | Label                     | Standard                                                      |
| ------------ | ------------------------- | ------------------------------------------------------------- |
| **OPP-HIGH** | High opposition value     | Strong arguments; realistic chance to defeat on this element  |
| **OPP-MOD**  | Moderate opposition value | Arguable; better used in combination with other arguments     |
| **OPP-LOW**  | Low opposition value      | Weak argument; plaintiff's evidence strongly supports element |

### Circuit-Split Risk Flag

| Code              | Meaning                                                                  |
| ----------------- | ------------------------------------------------------------------------ |
| `[CIRCUIT-SPLIT]` | Outcome depends on which circuit applies; identify controlling precedent |
| `[VERIFY]`        | Legal proposition unverified; confirm against authoritative source       |

---

## Actionable Output Per Finding

For each element or issue identified, provide:

```
ELEMENT: [Rule 23(a)/(b) element or doctrine]
CLASSIFICATION: [S/M/W/F for plaintiff; OPP-HIGH/MOD/LOW for defense]
CONFIDENCE: [Definite/High/Probable/Possible/Unlikely — see Confidence Scoring]

ANALYSIS SUMMARY:
[1-2 paragraph substantive analysis applying the applicable standard to the specific facts]

EVIDENCE ASSESSMENT:
- Evidence supporting: [List specific evidence and its weight]
- Evidence undermining: [List specific evidence and its weight]
- Evidence gaps: [What additional evidence would strengthen/weaken this element]

BEST ARGUMENT (Plaintiff):
[The strongest argument plaintiff can make on this element]

BEST ARGUMENT (Defense):
[The strongest argument defense can make on this element]

STRATEGIC RECOMMENDATION:
- Plaintiff: [Specific action to take]
- Defense: [Specific action to take]

AUTHORITY: [Most relevant circuit/Supreme Court authority for this element]
```

---

## Prioritization Framework

### For Plaintiff Certification Motion

| Tier       | Label                       | Criteria                                                   | Action                                                                                    |
| ---------- | --------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Tier 1** | Certification-determinative | Elements rated W or F; without fixing, certification fails | Address first; redesign class definition or theory if needed                              |
| **Tier 2** | Significant but not fatal   | Elements rated M; opposition will attack these             | Build targeted evidence and arguments; consider preemptive concessions (e.g., subclasses) |
| **Tier 3** | Supporting arguments        | Elements rated S; already strong                           | Maintain; use to anchor brief structure; don't over-brief strengths at cost of weaknesses |

### For Defense Opposition

| Tier       | Label                 | Criteria                                                                     | Action                                                                  |
| ---------- | --------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Tier 1** | Most likely to defeat | Elements rated OPP-HIGH; realistic argument to defeat certification outright | Lead the opposition; invest expert and evidentiary resources here       |
| **Tier 2** | Combination arguments | Elements rated OPP-MOD; alone not sufficient but in combination may persuade | Brief thoroughly; support Tier 1 arguments                              |
| **Tier 3** | Record preservation   | Elements rated OPP-LOW; unlikely to succeed but worth preserving for 23(f)   | Brief proportionally; don't dilute opposition brief with weak arguments |

### Issue Certification Alternative (Rule 23(c)(4))

If a Rule 23(b)(3) class fails predominance due to individualized damages or causation, consider issue certification:

- Certify common questions only (e.g., liability determination; defect existence; uniform policy unlawfulness)
- Reserve individualized questions (damages, causation, reliance) for separate proceedings
- Issue certification may be certified as part of a proposed 23(b)(3) class even if the overall class could not be certified
- [CIRCUIT-SPLIT] Circuits differ on whether 23(c)(4) can be used where predominance fails for the case as a whole or only where predominance fails for particular issues within an otherwise certifiable case [VERIFY circuit alignment]

---

## Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate                | Rule                                                                                                      | Fail Action                                                |
| ------------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Source Gate**     | Every legal proposition cites specific case, statute, or rule                                             | Add citation or mark [UNVERIFIED]                          |
| **Format Gate**     | Case citations follow _Name_, Volume U.S./F.2d/F.3d Page (Year) format                                    | Fix format; use proper reporter abbreviations              |
| **Currency Gate**   | Check for post-2020 circuit developments on circuit-split issues                                          | Flag [CHECK CURRENCY] for volatile doctrine areas          |
| **Domain Gate**     | Analysis stays within FRCP 23 and the controlling circuit; state class action analysis labeled separately | Remove or flag cross-jurisdictional bleed                  |
| **Confidence Gate** | Uncertainty in circuit-split or evolving doctrine is explicitly stated                                    | Add confidence qualifier; flag [CIRCUIT-SPLIT] or [VERIFY] |

---

## Self-Interrogation for High-Severity Items

For any finding classified FATAL (for plaintiff) or OPP-HIGH (for defense), apply this
three-pass review before finalizing:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the
cited authority? Would the controlling circuit actually reach this conclusion on these
facts? Is there distinguishing precedent that weakens the conclusion?

**Pass 2 — Completeness**: Have all relevant Rule 23 doctrines, circuit precedents, and
strategic alternatives been considered? Have both the plaintiff's and defense's best
responses to this finding been fully developed?

**Pass 3 — Challenge**: What is the strongest counterargument against this classification?
Under what circumstances might a court certify the class despite this weakness (for
plaintiff) or deny certification despite this strength (for defense)?

---

## Confidence Scoring

| Level        | Range     | Meaning                                                            | Action                                     |
| ------------ | --------- | ------------------------------------------------------------------ | ------------------------------------------ |
| **Definite** | 0.95–1.0  | Settled Supreme Court or clear circuit precedent directly on point | State with full confidence                 |
| **High**     | 0.80–0.94 | Strong circuit precedent; minor factual distinctions possible      | State with brief qualification             |
| **Probable** | 0.60–0.79 | Good arguments; circuit precedent somewhat distinguishable         | State with reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuinely contested; circuit is unsettled or facts are borderline  | Flag for attorney review with both sides   |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative; circuit precedent against                 | Do not assert; flag [UNCERTAIN]            |

---

## Glass Box Audit Trail

Include this YAML audit template in every output:

```yaml
glass_box:
  skill_name: "legalcode-class-certification-analysis"
  mode: "Dual-perspective / Plaintiff-focused / Defense-focused"
  topic: "FRCP Rule 23 class certification analysis"
  jurisdiction: "US federal — [Circuit]th Circuit"
  class_definition_reviewed: "yes / no — [if no, state assumption]"
  class_type_analyzed: "[23(b)(1)(A) / (b)(1)(B) / (b)(2) / (b)(3) / (c)(4) / multiple]"
  settlement_class: "yes / no"
  cafa_jurisdiction_screened: "yes / no"
  expert_testimony_evaluated: "yes / no"
  circuit_split_issues: "[List of doctrine areas where circuit split applies]"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "[path] / Not created"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  citations_verified: "[N] VERIFIED / [N] [VERIFY]-tagged / [N] [CIRCUIT-SPLIT]-tagged"
  overall_certification_prospect: "HIGH / MODERATE / LOW / VERY LOW"
  element_summary:
    numerosity: "[S/M/W/F]"
    commonality: "[S/M/W/F]"
    typicality: "[S/M/W/F]"
    adequacy: "[S/M/W/F]"
    class_type_23b: "[S/M/W/F] — [applicable type]"
    ascertainability: "[S/M/W/F] — [circuit standard applied]"
    predominance: "[S/M/W/F] — [if 23(b)(3)]"
    superiority: "[S/M/W/F] — [if 23(b)(3)]"
    daubert: "[N/A / evaluated]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "Analysis based on [available record]; full certification record review recommended"
    - "Circuit-split issues resolved based on [circuit]; verify controlling precedent"
    - "[Any other scope limitations or assumptions]"
  reviewer: "AI-assisted — requires review by class action attorney licensed in the relevant jurisdiction"
```

---

## Anti-Patterns

Avoid these class certification analysis anti-patterns:

1. **Skipping the class definition review**: The class definition is not just preliminary context — it is the foundation of every Rule 23 analysis. A poorly drafted fail-safe class, an overbroad class, or a class with statute of limitations problems can be fatal before the first prerequisite is examined.

2. **Conflating commonality and predominance**: Commonality (23(a)(2)) requires any common question capable of a common answer. Predominance (23(b)(3)) requires those common questions to _dominate_ the litigation. Satisfying commonality does not mean satisfying predominance; many analyses incorrectly treat them as equivalent.

3. **Applying the wrong circuit's ascertainability standard**: Ascertainability doctrine is circuit-dependent. Applying the Third Circuit's strict administrative feasibility standard in a Ninth Circuit case (or vice versa) produces incorrect analysis. Always identify the circuit first.

4. **Ignoring the Comcast damages model requirement**: Treating predominance as satisfied once common liability questions are identified, without ensuring the damages methodology matches the specific surviving liability theory, produces analysis that will fail the Comcast test.

5. **Missing TransUnion's standing overlay**: Building a predominance argument that assumes all class members suffered uniform injury without addressing whether each member suffered concrete injury-in-fact under Article III. Post-_TransUnion_, this is a standing-based class-definition problem.

6. **Applying the wrong Daubert standard**: In circuits applying full Daubert at certification (Second, Third, Fifth, Seventh, Eleventh), failing to prepare for rigorous reliability review of class certification experts is a significant strategic error. In circuits applying tailored Daubert (Eighth), applying the full trial standard is unnecessary.

7. **Underestimating the Wal-Mart "common answer" requirement**: Identifying that class members have common questions (e.g., "were all denied the same benefit?") without demonstrating that resolution of the question will generate a common _answer_ applicable across the class. Wal-Mart demands the common question's answer actually drives the litigation.

8. **Proposing a (b)(2) class for individualized damages relief**: Seeking Rule 23(b)(2) certification for a class seeking primarily individualized monetary damages, when _Wal-Mart_ prohibits (b)(2) where monetary relief would require individualized determinations. This results in certain defeat.

9. **Failing to select named plaintiffs strategically**: Using named plaintiffs without fully vetting them for unique defenses, atypical facts, statute of limitations issues, prior releases, or credibility problems. Defense counsel exploit named plaintiff vulnerabilities through focused deposition before certification briefing.

10. **Not preparing for the merits overlap**: Treating the "we can't look at the merits" doctrine as a shield to avoid presenting a substantive common proof theory. Post-Wal-Mart courts recognize that rigorous analysis requires some merits engagement at certification.

11. **Filing a settlement class without Amchem compliance**: Submitting a settlement class that satisfies manageability (suspended in the settlement context) but fails adequacy, commonality, or typicality requirements — which are _not_ suspended. Courts apply heightened scrutiny to settlement classes.

12. **Ignoring CAFA jurisdiction strategy**: For state court class actions, failing to analyze whether CAFA enables federal court removal (defense strategy) or whether a CAFA exception could defeat federal jurisdiction (plaintiff strategy). CAFA is a threshold issue that shapes the entire litigation forum.

13. **Missing the Rule 23(f) window**: Failing to petition for interlocutory review within 14 days of a certification order (or denial). The 14-day deadline is jurisdictional in most circuits; missing it forfeits the right to interlocutory review. [VERIFY jurisdictional vs. claim-processing characterization in current circuits]

14. **Underdeveloping the trial plan**: Submitting a certification motion in a complex 23(b)(3) case without a credible trial plan demonstrating manageability. Courts increasingly require trial plans; failure to provide one — or providing a generic one — undermines the superiority showing.

15. **Treating intraclass conflicts as minor**: Failing to identify and address conflicts between class members (e.g., different class members prefer different remedies; named plaintiff's interests diverge from absent class members). Intraclass conflicts can destroy adequacy and, if they create fundamental class member antagonism, may preclude certification entirely.

16. **Conflating Rule 23 and state class action standards**: Applying FRCP 23 doctrine to a state court class action (or vice versa) without accounting for material differences. California CCP § 382 is more liberal; New York CPLR Article 9 lacks rigid class categories; many state courts resolve close certification questions in favor of certification.

17. **Omitting the opt-out analysis**: For 23(b)(3) classes, failing to consider the strategic implications of the opt-out right — including the ability of significant opt-outs to undermine settlement value or superiority arguments. For 23(b)(1) and (b)(2) mandatory classes, failing to note the absence of opt-out rights and its implications for class member autonomy.

18. **Over-relying on general damages evidence at certification**: Presenting a damages expert who describes generally applicable methodologies without demonstrating with case-specific data that the methodology works for this class. Courts post-_Comcast_ reject theoretical adequacy and require concrete demonstration.

---

## Writing Standards

Apply these quality standards before delivering any output:

1. **Precision**: Every doctrinal statement includes the specific rule, case, or circuit that establishes it. No generic "courts have held" without identifying which courts.

2. **Circuit specificity**: All circuit-split issues expressly identify which circuits support which position and which position the controlling circuit has adopted.

3. **[VERIFY] discipline**: Legal propositions from memory that have not been independently verified are tagged [VERIFY]. Do not assert unverified circuit precedent as established law.

4. **[CIRCUIT-SPLIT] transparency**: Where circuits disagree and the controlling circuit's position has not been confirmed, flag explicitly with [CIRCUIT-SPLIT] and present both positions.

5. **Dual perspective**: Unless the user has specified a single perspective, analysis addresses both plaintiff and defense implications for every major finding.

6. **Actionability**: Every classification (STRONG, MODERATE, WEAK, FATAL, OPP-HIGH) includes a specific recommended action — not just an assessment.

7. **No merits substitution**: Rule 23 analysis is not a substitute for merits analysis. Where the certification inquiry requires engagement with merits evidence, clearly distinguish between the certification-stage inquiry and any merits conclusions.

8. **Length calibration**: Match analysis depth to the element's importance to the specific case. Do not over-brief STRONG elements; focus depth on WEAK and FATAL elements.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for controlling circuit precedent on the specific elements and doctrine areas at issue
- Verify currency of circuit precedent on volatile doctrine areas (ascertainability, Daubert at certification, cy pres)
- Research recent district court decisions on certification in analogous cases within the controlling circuit
- Identify recent Supreme Court decisions or cert grants affecting class certification doctrine
- Save verified authority to `/tmp/legalcode-class-cert-authority.md` structured as:

```markdown
# Class Certification Legal Authority

## Circuit: [X]th Circuit

## Date: [date]

### Rule 23(a) Authority

- Commonality: [cases]
- Typicality: [cases]
- Adequacy: [cases]

### Rule 23(b)(3) Authority

- Predominance: [cases]
- Superiority: [cases]
- Comcast application in this circuit: [cases]

### Ascertainability: [applicable standard + cases]

### Daubert at Certification: [applicable standard + cases]

### CAFA: [relevant decisions]
```

**Without legalcode-mcp:**

- Proceed with the analysis using the research embedded in this skill
- Mark all circuit-specific authority with [VERIFY] and note the need for independent verification
- Flag in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Recommend that attorney verify all circuit citations against Westlaw or Lexis before filing

---

## Output Format Template

Structure the final deliverable as follows:

````markdown
# Class Certification Analysis — [Case Name / Matter Description]

**Prepared for**: [Plaintiff's counsel / Defense counsel / Neutral]
**Class definition**: [Exact proposed class language]
**Date**: [Date of analysis]
**Circuit**: [X]th Circuit
**Class type(s) analyzed**: [23(b)(1)/(b)(2)/(b)(3)/other]

---

## Executive Summary

**Overall certification prospect**: [HIGH / MODERATE / LOW / VERY LOW]

[2-3 paragraph summary of the overall certification prospect, the most important
strength or weakness, and the highest-priority strategic recommendation]

---

## CAFA Jurisdiction Screening

[Results of CAFA screening; state whether CAFA applies, exceptions analysis,
and strategic implications for forum selection]

---

## Rule 23(a) Prerequisite Analysis

### Numerosity — [S/M/W/F]

[Analysis]

### Commonality — [S/M/W/F]

[Analysis applying Wal-Mart "common answer" framework]

### Typicality — [S/M/W/F]

[Analysis; named plaintiff assessment; unique defenses identified]

### Adequacy of Representation — [S/M/W/F]

[Named plaintiff and class counsel adequacy analysis]

---

## Rule 23(b) Class Type Analysis

### [Applicable 23(b) type] — [S/M/W/F]

[Analysis of class type requirements]

#### Predominance Analysis (if 23(b)(3)) — [S/M/W/F]

[Common vs. individual questions; Comcast damages model assessment; Tyson Foods
statistical evidence analysis; TransUnion standing overlay]

#### Superiority Analysis (if 23(b)(3)) — [S/M/W/F]

[Four statutory factors; class vs. individual suits; class vs. arbitration;
manageability and trial plan]

---

## Ascertainability Assessment — [S/M/W/F]

**Controlling circuit standard**: [Administrative feasibility / Objective criteria only]
[Analysis]

---

## Expert Evidence and Daubert Analysis

**Circuit Daubert standard**: [Full / Tailored]
[Expert strategy and Daubert challenge analysis]

---

## Settlement Class Considerations (if applicable)

[Amchem analysis; fairness factors; cy pres review; Article III standing]

---

## Prioritized Strategic Recommendations

### Tier 1: Certification-Determinative Issues

| Issue   | Plaintiff Action | Defense Action | Urgency   |
| ------- | ---------------- | -------------- | --------- |
| [Issue] | [Action]         | [Action]       | IMMEDIATE |

### Tier 2: Significant Issues

| Issue   | Plaintiff Action | Defense Action | Urgency   |
| ------- | ---------------- | -------------- | --------- |
| [Issue] | [Action]         | [Action]       | NEAR-TERM |

### Tier 3: Supporting Arguments

| Issue   | Plaintiff Action | Defense Action | Urgency    |
| ------- | ---------------- | -------------- | ---------- |
| [Issue] | [Action]         | [Action]       | BACKGROUND |

---

## Rule 23(f) Interlocutory Appeal Assessment

**Applicable**: [Yes / No]
**Petition deadline**: [14 calendar days from order date]
[Analysis of whether Rule 23(f) petition criteria are satisfied]

---

## Alternative Strategies

[If certification prospects are LOW or VERY LOW, analyze alternatives:]

- Alternative class definition
- Issue certification under 23(c)(4)
- Alternative 23(b) class type
- Settlement class submission
- Individual/coordinated litigation alternative

---

## Quality Assurance

**Citation Quality Gates**: [All passed / Issues identified: ...]
**Self-Interrogation**: [Performed for FATAL/OPP-HIGH items — summary]
**Confidence calibration**: [Overall confidence level and key uncertainties]

---

## Glass Box Audit Trail

```yaml
glass_box: [full audit trail as specified above]
```
````

```

---

## Localization Notes

This skill is US federal procedure-centric. When adapting for state court class actions:

1. **California (CCP § 382)**: Remove 23(b) categorical structure; apply "community of interest" test (numerosity; common questions; representative plaintiff typical of the class); courts resolve close questions in favor of certification; statute of limitations analysis under California law differs from federal law
2. **New York (CPLR Article 9)**: No rigid class categories; apply flexible test; notice after certification is discretionary; opt-out rights available regardless of relief type; Desrosiers v. Perry Ellis requires court approval even for pre-certification settlements
3. **Other states**: Most states follow FRCP 23 substantially but verify local court rules, local certification standards, and notice requirements before advising

**Potential jurisdiction-specific variants:**
- `legalcode-class-certification-analysis-ca` — California CCP § 382 focused analysis
- `legalcode-class-certification-analysis-ny` — New York CPLR Article 9 focused analysis
- `legalcode-class-certification-analysis-securities` — PSLRA securities fraud class certification with fraud-on-the-market presumption (*Basic Inc. v. Levinson*; *Halliburton Co. v. Erica P. John Fund*)

---

## Provenance

Legalcode original skill created 2026-03-02. Created using the 2-agent research pipeline
with supplementary WebSearch research. Legal research grounded in:

- FRCP Rule 23 (2024 text via federalrulesofcivilprocedure.org)
- *Wal-Mart Stores, Inc. v. Dukes*, 564 U.S. 338 (2011)
- *Comcast Corp. v. Behrend*, 569 U.S. 27 (2013)
- *Tyson Foods, Inc. v. Bouaphakeo*, 577 U.S. 442 (2016)
- *TransUnion LLC v. Ramirez*, 141 S. Ct. 2190 (2021)
- *Amchem Products, Inc. v. Windsor*, 521 U.S. 591 (1997)
- *Ortiz v. Fibreboard Corp.*, 527 U.S. 815 (1999)
- *Frank v. Gaos*, 586 U.S. ___ (2019)
- Circuit ascertainability precedent: Third Circuit (*In re Niaspan*, 2023), Ninth Circuit (*Briseno v. ConAgra*, 2017), Seventh Circuit (*Mullins v. Direct Digital*, 2015) [VERIFY]
- Circuit Daubert-at-certification precedent: Fifth, Seventh, Eleventh (full Daubert); Eighth (tailored) [VERIFY currency]
- Gibson Dunn 2024 Class Action Update — circuit trends analysis
- American Antitrust Institute Fall 2024 Class Action Update
- Skadden "Litigating Expert Testimony at the Class Certification Stage" (2019)
- Structural patterns from: `legalcode-summary-judgment-analysis`, `legalcode-litigation-risk-assessment`, `legalcode-early-case-assessment` (Legalcode repository)

All statutory and case citations carry [VERIFY] status — verify against authoritative
sources before relying on them in any filing. This skill requires review by qualified
class action counsel before use in any litigation.
```
