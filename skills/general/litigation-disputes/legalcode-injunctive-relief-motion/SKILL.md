---
name: legalcode-injunctive-relief-motion
description: Drafts preliminary injunction and TRO (temporary restraining order) applications, analyzes
  prospects under the Winter v. NRDC four-factor test (US), and applies UK American Cyanamid principles
  (serious question to be tried / balance of convenience). Use when you need to obtain emergency or interim
  injunctive relief, stop ongoing harm, preserve the status quo, enforce covenants (non-compete, confidentiality,
  non-solicitation), protect IP rights, prevent asset dissipation, or seek a freezing order (Mareva),
  search order (Anton Piller), or anti-suit injunction. Covers FRCP Rule 65 TROs and preliminary injunctions,
  FRCP 65(c) bond requirements, ex parte / without-notice procedures (FRCP 65(b) / CPR Part 25), mandatory
  vs. prohibitory standards, circuit-by-circuit sliding-scale variations, and UK High Court interim injunction
  practice. Generates argument outlines, factor-by-factor prospect assessments, draft declaration and
  brief structures, and bond/undertaking analysis with Glass Box audit trail.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Injunctive Relief Motion

> **Disclaimer**: This skill provides a framework for AI-assisted drafting and analysis
> of injunctive relief applications. It does not constitute legal advice. All outputs
> must be reviewed, verified, and signed by qualified legal counsel licensed in the
> relevant jurisdiction before filing with any court. Procedural rules, case law, and
> equitable standards change frequently; verify all cited authority before relying on
> any conclusion. AI-generated legal arguments may contain errors in analysis, strategic
> assessment, or citation accuracy — all arguments must be verified against current
> authority and the specific facts of the case. Any cited authority marked `[VERIFY]`
> has not been independently validated and must be confirmed before reliance. Filing a
> motion constitutes a certification (Rule 11 in US federal practice) that the arguments
> are well-grounded in fact and law; counsel bears independent professional
> responsibility for that certification. Injunctions are equitable remedies subject to
> the court's discretion — no analytical framework guarantees a particular outcome.

---

## Purpose and Scope

This skill drafts and analyzes applications for preliminary injunctions and temporary
restraining orders (TROs) in US federal and UK High Court proceedings, with adaptable
principles for other common law jurisdictions.

**Covers:**

- **US Preliminary Injunction**: Winter v. NRDC four-factor test, circuit-specific
  variations (sliding scale, strict sequential), Dataphase factors (8th Circuit)
- **US TRO (ex parte)**: FRCP 65(b) requirements, 14-day duration, expedited hearing
  scheduling, notice-and-opportunity-to-be-heard considerations
- **FRCP 65(c) Bond**: Security requirement, amount analysis, waiver criteria
- **UK Interim Injunction**: American Cyanamid [1975] UKHL 1 serious-question-to-be-tried
  standard, balance of convenience, adequacy-of-damages analysis
- **UK Without-Notice Orders**: CPR Part 25 without-notice (ex parte) applications,
  full and frank disclosure obligations, undertaking in damages
- **Mandatory vs. Prohibitory**: Heightened standard for mandatory injunctions
- **Specialized Injunctions**: Freezing orders (Mareva), search orders (Anton Piller /
  CPR 25 search orders), anti-suit injunctions, garden leave enforcement
- **Emergency Procedures**: After-hours filings, expedited briefing schedules, same-day
  TRO hearings
- **Prospect Assessment**: Factor-by-factor strength rating, overall GRANT-LIKELY /
  BORDERLINE / DENY-LIKELY classification
- **Draft Structure**: Argument outlines, supporting declaration structure, proposed
  order elements, bond/undertaking language

**Does not:**

- Replace counsel's judgment on judicial temperament, local practice, or courtroom
  strategy
- Certify Rule 11 / professional conduct compliance (counsel's responsibility)
- Conduct independent factual investigation or verify client representations
- Draft full state-court injunction papers (state standards may differ materially from
  federal; flag for local counsel review)
- Provide final assessments on permanent injunction standards following full trial
  (separate analysis from interim/preliminary relief)
- Cover NLRA labor injunctions under the Norris-LaGuardia Act (specialized statutory
  regime)

**Related skills:**

- `legalcode-motion-to-dismiss-drafter` — 12(b) grounds at the pleadings stage
- `legalcode-complaint-drafter` — Draft the underlying complaint
- `legalcode-litigation-risk-assessment` — Broader case risk scoring
- `legalcode-early-case-assessment` — Pre-filing evaluation including injunction viability
- `legalcode-settlement-agreement-drafter` — Consent order / consent injunction drafting

---

## Jurisdiction and Governing Law

This skill covers two primary frameworks. Identify the applicable framework before
beginning analysis — the tests are different and the outputs are structured differently.

| Framework                    | Applies when                                       | Governing authority                                                         |
| ---------------------------- | -------------------------------------------------- | --------------------------------------------------------------------------- |
| **US Federal (Winter)**      | Federal court, preliminary injunction or TRO       | Winter v. NRDC, 555 U.S. 7 (2008); FRCP Rule 65                             |
| **US Federal (Dataphase)**   | 8th Circuit cases                                  | Dataphase Systems, Inc. v. C.L. Systems, Inc., 640 F.2d 109 (8th Cir. 1981) |
| **UK High Court (Cyanamid)** | England & Wales High Court interim injunction      | American Cyanamid Co v Ethicon Ltd [1975] AC 396 (HL)                       |
| **UK Without-Notice**        | Without-notice (ex parte) application, CPR Part 25 | CPR 25.3; Practice Direction 25A                                            |

[JURISDICTION-SPECIFIC] For other common law jurisdictions (Australia, Canada, Singapore,
Hong Kong), the American Cyanamid framework typically applies with local modifications —
verify jurisdiction-specific tests before proceeding. Civil law jurisdictions have
entirely different interim measure frameworks (e.g., French référé, German einstweilige
Verfügung) that this skill does not cover.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming user intent, the workflow pauses and asks when:

- The answer would change the applicable legal framework or procedural path
- Multiple approaches exist with meaningfully different strategic implications
- Factual ambiguity prevents confident factor assessment
- Risk tolerance or business context is needed to calibrate the analysis

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

### Step 1: Accept the Engagement

Accept the matter in any of these formats:

- **Fact pattern**: A description of the dispute, the harm occurring, and the relief
  sought — either freeform or structured
- **Draft complaint or existing papers**: Pleadings, declarations, or prior filings
- **Counterparty's motion**: A motion to dissolve or oppose an existing injunction
- **Pasted document**: Relevant contract, court order, or exhibit

If no fact pattern is provided, ask the user to describe the dispute in enough detail
to begin the analysis.

### Step 2: Gather Context

**⟁ CLARIFY** — Before analysis, gather the following. Present as structured options
where possible.

1. **Jurisdiction and court**:
   - Options: US federal court (specify circuit and district), UK High Court (specify
     division: Chancery / Queen's Bench / Commercial Court / IPEC), Other (describe)
   - _Why this matters_: Determines the applicable legal test, bond requirements,
     procedural rules, and motion format.

2. **Type of relief sought**:
   - Options: Ex parte TRO (no notice to opposing party), Noticed TRO (short notice
     to opposing party), Preliminary injunction (full briefing), UK without-notice
     interim injunction, UK on-notice interim injunction, Freezing order (UK Mareva),
     Search order (UK Anton Piller), Anti-suit injunction, Other
   - _Why this matters_: Ex parte relief has heightened procedural requirements; UK
     without-notice applications require full and frank disclosure; different types have
     different duration and procedural paths.

3. **Nature of the injunction** (if applicable):
   - Options: Prohibitory (stop defendant from doing something — standard), Mandatory
     (require defendant to take affirmative action — heightened standard), Status quo
     preservation (maintain current state of affairs)
   - _Why this matters_: Mandatory injunctions face a stricter standard and are harder
     to obtain; this materially changes the analysis.

4. **Urgency and timeline**:
   - Options: Emergency (hours), Urgent (1–3 days), Standard (days to weeks), No
     immediate urgency
   - Current status of the harm: Has it started? Is it ongoing? Is it imminent?
   - _Why this matters_: Affects whether ex parte relief is available and whether
     emergency court procedures apply.

5. **Substantive claim underlying the injunction**:
   - Describe the primary legal claims (e.g., breach of contract, trade secret
     misappropriation, trademark infringement, breach of fiduciary duty, tortious
     interference)
   - Any prior proceedings or related orders
   - _Why this matters_: "Likelihood of success on the merits" (US) or "serious
     question to be tried" (UK) turns on the strength of the underlying claim.

6. **Harm and damages context**:
   - Can the harm be adequately compensated in money damages?
   - Is the harm quantifiable? Ongoing? Irreversible?
   - _Why this matters_: "Irreparable harm" (US) and "adequacy of damages" (UK) are
     central gatekeeping requirements.

If the user provides partial context, proceed with what you have and **state your
assumptions explicitly** (e.g., "Assuming this is a US federal court matter in the 9th
Circuit — let me know if that is wrong and I will re-run the analysis").

### Step 3: Identify the Applicable Framework

Based on the jurisdiction information from Step 2, map to the applicable legal framework:

| If jurisdiction is...               | Apply this framework                                                   |
| ----------------------------------- | ---------------------------------------------------------------------- |
| US federal court                    | Winter four-factor test (or Dataphase if 8th Circuit)                  |
| US federal court, 2d or 9th Circuit | Winter + sliding scale variant where arguable                          |
| US federal court, 4th Circuit       | Winter strict sequential test (no sliding scale)                       |
| UK High Court, England & Wales      | American Cyanamid serious question / balance of convenience            |
| UK, without-notice application      | American Cyanamid + full and frank disclosure + undertaking in damages |
| UK, mandatory injunction            | American Cyanamid with heightened "overwhelming case" threshold        |
| UK, freezing order                  | Six Cyanamid conditions + dissipation risk + cross-undertaking         |
| UK, search order                    | Four Anton Piller conditions + CPR 25 PD                               |
| UK, anti-suit injunction            | Comity analysis + unconscionability / vexatiousness test               |

**⟁ CLARIFY** — If the applicable circuit or division is not clear and it would materially
change the analysis, ask: "Which circuit / division does this matter fall in? The circuit
affects whether a sliding scale approach is available (e.g., 9th Circuit allows it; 4th
Circuit does not)."

### Step 4: Gather Legal Authority

Use **legalcode-mcp** to search for jurisdiction-relevant authority before beginning
the factor analysis.

**For US federal matters, search for:**

- The Winter test and its application in the relevant circuit
- Circuit-specific sliding scale cases or their abandonment
- Cases applying the test to the specific substantive claim type (e.g., trade secret,
  trademark, non-compete)
- Recent district court decisions in the specific district on the issue
- Any statutory presumption of irreparable harm applicable to the claim (e.g., Lanham
  Act § 34(a) rebuttable presumption [VERIFY])

**For UK matters, search for:**

- American Cyanamid [1975] AC 396 and its progeny
- Cases applying the test to the specific subject matter
- Any applicable statutory power to grant interim relief
- CPR Part 25 rules and Practice Direction 25A

Save the most relevant results to a local reference file (`/tmp/injunction-authority.md`).

**If legalcode-mcp is not connected:**

- Proceed with general knowledge and mark all case citations `[VERIFY]`
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Rely on the authorities cited in this skill, but verify each before filing

### Step 5: Factor-by-Factor Analysis

Apply the framework identified in Step 3. Work through each factor systematically
before rendering an overall assessment.

**⟁ CLARIFY** — For any factor where the strength depends critically on facts not
yet provided, ask rather than assume:

- "What evidence exists of [irreparable harm / ongoing violation / dissipation risk]?
  Declarations? Documentary evidence? Expert opinion?"
- "Has the plaintiff delayed in seeking relief? Delay undermines irreparable harm."
- "What is the counterparty's likely response? Is there a competing public interest?"

Apply the **Factor Prospect Rating** system from the **Prospect Classification**
section below. Assign each factor a rating of STRONG, MODERATE, or WEAK, with
supporting reasoning.

See the **Factor Analysis Reference** section for the detailed analytical framework
for each factor under each jurisdiction.

### Step 6: Ex Parte / Without-Notice Assessment

If the user is seeking ex parte or without-notice relief, conduct the additional
analysis required by Step 5. See the **Ex Parte and Without-Notice Procedures**
section.

**⟁ CLARIFY** — Ask these questions before recommending ex parte / without-notice
relief:

- "Has any notice been given to the opposing party? Has any attempt been made?"
- "What would happen if the opposing party received notice? What specific harm would
  result from giving notice?"
- "Is time truly of the essence, or would a brief (24–48 hour) expedited noticed
  hearing be feasible?"

Ex parte / without-notice relief is extraordinary and courts scrutinize it closely.
Do not recommend it unless the facts clearly justify it.

### Step 7: Bond and Security Assessment

Analyze the bond/security requirement. See the **Bond and Security Requirements**
section.

For US matters: Estimate an appropriate FRCP 65(c) bond amount and assess whether
any waiver argument is available.

For UK matters: Assess the cross-undertaking in damages obligation and whether the
applicant can satisfy it.

**⟁ CLARIFY** — If bond exposure would be substantial:

- "What is the defendant's likely financial exposure if wrongly enjoined?
  Lost profits? Business disruption? Reputational harm?"
- "Is the applicant financially able to satisfy a bond in that amount?"
- "Is there a basis to argue for bond waiver (e.g., government plaintiff, de minimis
  harm, public interest)?"

### Step 8: Draft the Motion Papers

Based on the analysis from Steps 5–7, draft the requested papers. See the **Motion
Drafting Standards** and **Output Format Template** sections.

**⟁ CLARIFY** — Before drafting, confirm:

- **Scope**: Full draft argument, argument outline, or specific sections only?
- **Voice**: First person (court filing voice) or third person (analysis/memo voice)?
- **Format**: FRCP / local rule page/word limits? Court-specific formatting?

For a full TRO / preliminary injunction motion package, the output includes:

1. Memorandum of law / supporting brief
2. Supporting declaration framework (facts to include; counsel drafts actual attestation)
3. Proposed order (TRO or preliminary injunction)
4. FRCP 65(b) certification of notice attempts (for ex parte TRO only)

### Step 9: Quality Verification

Before delivering output, run the quality checks in the **Quality Assurance Framework**
section:

1. Run the 5 Citation Quality Gates silently — revise any failures before delivery.
2. For each factor rated WEAK, run the 3-pass Self-Interrogation to ensure the weakness
   assessment is honest and well-reasoned.
3. Assign a Confidence Score to the overall prospect assessment.
4. Verify completeness: confirm all applicable factors/elements have been addressed.
5. Check that the tone calibration is appropriate — injunction papers should be
   urgent but measured; avoid hyperbole that undermines credibility.
6. Generate the Glass Box Audit Trail and append it to the output.

### Step 10: Deliver Output

Structure the output using the **Output Format Template** at the end of this skill.

---

## Factor Analysis Reference

### US Framework: Winter Four-Factor Test

_Winter v. Natural Resources Defense Council, Inc., 555 U.S. 7 (2008)_

The movant must establish **all four factors**:

1. Likelihood of success on the merits
2. Likelihood of irreparable harm in the absence of preliminary relief
3. That the balance of equities tips in the movant's favor
4. That an injunction is in the public interest

The Supreme Court in _Winter_ rejected the "possibility of irreparable harm" standard
and required the movant to show that irreparable harm is **likely**, not merely possible.

#### Factor 1: Likelihood of Success on the Merits

**What courts require:**

- More than a mere possibility of success
- A "clear showing" in most circuits
- Not a full merits determination — courts avoid prejudging the case
- Movant must identify the elements of the underlying claim and demonstrate a
  colorable basis for each

**Strong showing (STRONG):**

- Compelling evidence on each element
- Favorable precedent closely on point
- Counterparty's defenses are weak or unsupported
- Declaratory evidence corroborates the claims

**Moderate showing (MODERATE):**

- Colorable claim with some contested elements
- Genuine dispute about one or more elements
- Legal uncertainty (novel theory, circuit split) not resolved in movant's favor
- Reasonable defenses available to counterparty

**Weak showing (WEAK):**

- Significant factual disputes material to the claim
- Clear precedent runs against the movant
- Elements of the claim are missing or unsupported
- Affirmative defenses (laches, unclean hands, estoppel) substantially undermine claim

**Circuit-specific variations on this factor:**

| Circuit      | Approach                                                                                                                   |
| ------------ | -------------------------------------------------------------------------------------------------------------------------- |
| 9th Circuit  | "Serious questions going to the merits" may suffice if balance of hardships tips sharply in movant's favor (sliding scale) |
| 2d Circuit   | Either likelihood of success OR serious questions + balance of hardships decidedly in movant's favor                       |
| 7th Circuit  | Sliding scale: stronger showing on merits = lesser irreparable harm required                                               |
| 4th Circuit  | Strict Winter test; no sliding scale; all four factors must independently be met                                           |
| 8th Circuit  | Dataphase: "probability that movant will succeed on merits" — probability not certainty                                    |
| 11th Circuit | "Substantial likelihood of success" — slightly higher formulation                                                          |

#### Factor 2: Likelihood of Irreparable Harm

**Core requirement:** Harm that cannot be adequately compensated by monetary damages
awarded at the end of litigation.

**What courts require:**

- Showing that harm is **likely** to occur without relief (not just possible)
- Inadequacy of money damages — harm must be non-compensable or unrecoverable
- The harm must be caused by the defendant's conduct (causal nexus)
- Delay in seeking relief undercuts the "immediacy" of irreparable harm

**Recognized categories of irreparable harm:**

| Category                                  | Notes                                                                                                         |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Trade secret misappropriation             | Widespread disclosure = irreparable; courts recognize difficulty of quantifying trade secret loss [VERIFY]    |
| Loss of goodwill / customer relationships | Difficult to quantify; courts routinely recognize [VERIFY]                                                    |
| Trademark / brand confusion               | Lanham Act § 34(a): rebuttable presumption of irreparable harm upon showing of likelihood of success [VERIFY] |
| Copyright infringement                    | Rebuttable presumption in some circuits [VERIFY]                                                              |
| Loss of competitive market position       | Difficult to quantify; recognized by courts [VERIFY]                                                          |
| Disclosure of confidential information    | Irreversible once disclosed                                                                                   |
| Breach of covenant not to compete         | Customer solicitation / knowledge transfer can be irreversible                                                |
| Constitutional rights deprivation         | First Amendment, due process violations — often presumed irreparable [VERIFY]                                 |
| Environmental harm                        | Difficult to remediate; recognized in NEPA cases                                                              |

**Common attacks on irreparable harm:**

- Prior delay by movant in seeking relief
- Movant accepted money damages in prior similar circumstances
- Harm is quantifiable (expert can calculate lost profits)
- Counterparty is solvent and can pay any judgment
- Harm has already occurred and injunction cannot restore status quo

**⟁ CLARIFY** — Ask the user: "Has the plaintiff previously accepted money compensation
for the same or similar harm? Has there been any delay in bringing this motion? Courts
treat both as undermining irreparable harm."

#### Factor 3: Balance of Equities (Hardships)

**What courts require:**

- Weigh the harm to the movant if relief is denied vs. the burden on the respondent
  if relief is granted
- Consider the relative magnitude of each party's potential harm
- Consider whether harms are reversible

**Factors favoring movant:**

- Respondent is causing ongoing, escalating harm
- Respondent's conduct is willful or in bad faith
- Respondent can mitigate by ceasing the challenged conduct at low cost
- Granting relief preserves reversibility; denial does not

**Factors disfavoring movant:**

- Injunction would shut down respondent's business or operation
- Third parties (employees, customers) would be severely harmed
- Respondent made significant investments in good faith reliance on current practices
- Scope of injunction is broader than necessary

#### Factor 4: Public Interest

**What courts require:**

- Whether granting or denying the injunction serves the public interest
- Particularly salient when injunction affects third parties or public

**Common arguments for public interest in favor of injunction:**

- Protecting trade secrets encourages innovation
- Preventing consumer confusion (trademark / false advertising)
- Environmental protection
- Protecting whistleblowers

**Common arguments against granting on public interest grounds:**

- Injunction would restrict competition in the marketplace
- Employees would be put out of work
- Consumers would lose access to products or services
- Restrains constitutionally-protected speech

**Monsanto Co. v. Geertson Seed Farms, 561 U.S. 139 (2010)** [VERIFY]:
Confirmed that NEPA violations alone do not create a presumption of injunctive relief;
the full four-factor test applies even when a statutory violation is established.

---

### UK Framework: American Cyanamid

_American Cyanamid Co v Ethicon Ltd [1975] AC 396 (HL)_

Lord Diplock's sequential test:

#### Stage 1: Serious Question to Be Tried

**Threshold:** The claim must not be "frivolous or vexatious" — the applicant must
show there is a serious question to be tried. This is a **low threshold**:

- Not a full merits assessment
- The applicant need not show a _strong_ prima facie case
- A properly arguable claim suffices
- Courts avoid expressing views on the merits at this interlocutory stage

**Exceptions to the low threshold** (where higher standard applies):

- **Shut-out cases**: Where granting or refusing the injunction would effectively
  determine the outcome (e.g., mandatory injunction that gives the applicant
  everything sought in the action) — courts require an "overwhelming case" [VERIFY]
- **Cases unlikely to go to trial**: Defamation claims (Bonnard v Perryman [1891]
  defence of justification carries special weight), trade union injunctions
- **Mandatory injunctions**: Higher standard applies — see below

#### Stage 2: Balance of Convenience and Adequacy of Damages

If the serious question threshold is met, the court proceeds to balance of convenience.
This is where most interlocutory injunction applications are won or lost.

**Primary question: Would damages be an adequate remedy for the applicant?**

- If yes, injunction should normally be refused
- The ability to quantify harm in money damages weighs against granting relief
- If damages would be adequate, the applicant has not established a need for
  equitable intervention

**Secondary question (if damages inadequate for applicant): Would damages under the
cross-undertaking be adequate for the respondent?**

- If yes, and damages were inadequate for applicant, injunction should normally be granted
- If also no, proceed to balance of convenience

**Balance of convenience factors:**

- Relative strength / magnitude of harm to each party
- Reversibility — can the harm be undone?
- Status quo: which party bears the burden of preserving the existing state of affairs?
- Where the balance is equal, prefer to maintain the status quo

**Preservation of status quo:**
Lord Diplock: where other factors are evenly balanced, the court should take such
measures as are calculated to preserve the status quo. The _status quo_ is typically
the state of affairs immediately before the application, not at some earlier point.

#### American Cyanamid Exceptions

| Exception                                | Standard                                       | When It Applies                                           |
| ---------------------------------------- | ---------------------------------------------- | --------------------------------------------------------- |
| **Mandatory injunction**                 | "Overwhelming case" required [VERIFY]          | Requiring defendant to take positive action               |
| **Cases with no real prospect of trial** | Court must assess merits more fully            | Defamation, cases where settlement is near-certain        |
| **Shutout relief**                       | Applicant must show strong prima facie case    | Where interim relief would effectively end the litigation |
| **Public interest injunctions**          | Courts may consider public interest separately | Injunctions against public authorities                    |

---

### Mandatory vs. Prohibitory Injunctions

**Prohibitory injunction**: Restrains defendant from doing something (preserves status quo).
Standard: Winter four-factor test (US) / American Cyanamid (UK).

**Mandatory injunction**: Requires defendant to take positive action (disturbs status quo).
Standard: **Heightened** — court requires:

**US approach:**

- Some circuits apply the same four-factor test but weigh the factors more strictly
- Others require "extreme or very serious damage" and that the facts are "clearly
  in movant's favor" [VERIFY]
- The "mandatory" nature is a significant factor in the balance of equities: the
  court must consider the burden on defendant of being required to act affirmatively

**UK approach (Zockoll Group v Mercury Communications [1998])** [VERIFY]:

- Court requires "a high degree of assurance" that the applicant will succeed at trial
- Courts are "less willing" to grant mandatory interlocutory injunctions
- The "clear and urgent need" test — applicant must show that a failure to grant
  mandatory relief would cause irreparable harm that cannot await trial

---

### Specialized Injunctions (UK)

#### Freezing Order (Mareva Injunction)

_Derived from Mareva Compania Naviera SA v International Bulkcarriers SA [1975]_
Now governed by CPR Part 25 and Practice Direction 25A.

**Six essential requirements:**

1. Underlying cause of action within the English jurisdiction
2. Claim with a good arguable case on the merits (higher than mere "serious question")
3. Assets within the jurisdiction (or, for worldwide freezing order, outside)
4. Real risk that the defendant will dissipate assets before judgment
5. Cross-undertaking in damages by the applicant
6. Full and frank disclosure of all material facts (without-notice applications)

**Scope options:**

- Domestic freezing order: assets within England and Wales
- Worldwide freezing order: all assets globally (extraordinary remedy; available
  where domestic order would be inadequate)

**Living expenses and legal costs exceptions**: The respondent is entitled to spend
ordinary living expenses and reasonable legal costs despite a freezing order.

#### Search Order (Anton Piller / CPR Part 25)

_Anton Piller KG v Manufacturing Processes Ltd [1976] Ch 55_
Superseded by Civil Procedure Act 1997; now governed by CPR 25 PD.

**Four pre-conditions:**

1. Extremely strong prima facie case (higher than ordinary serious question)
2. Damage, actual or potential, must be very serious for the applicant
3. Clear evidence that the respondent has in their possession relevant documents or
   things and there is a real possibility they may destroy them before the application
   can be made inter partes
4. Harm from search order must not be disproportionate to legitimate benefit

**Supervisory solicitor**: A search order must name an independent solicitor to
supervise the search; the applicant's solicitors may not supervise.

#### Anti-Suit Injunction

**US approach** (conservative view, most circuits):

- Granted in narrow circumstances: where foreign proceedings threaten the court's
  jurisdiction or would undermine a strong national policy
- International comity weighs heavily against anti-suit injunctions
- Some circuits (5th, 9th) apply a more liberal multi-factor test [VERIFY]

**UK approach:**

- Court enjoins proceedings in foreign courts where it is "unconscionable" for the
  defendant to continue them
- Classic bases: breach of exclusive jurisdiction clause, breach of arbitration
  agreement, vexatious / oppressive parallel proceedings
- Comity requires restraint — anti-suit injunctions issued only where necessary to
  protect a legitimate English jurisdiction

---

## Ex Parte and Without-Notice Procedures

### US: FRCP 65(b) Ex Parte TRO Requirements

A TRO may be issued **without notice** to the adverse party only if:

**(A)** Specific facts in an affidavit or verified complaint clearly show that **immediate
and irreparable injury, loss, or damage** will result to the movant before the adverse
party can be heard in opposition; **AND**

**(B)** The movant's attorney **certifies in writing** any efforts made to give notice and
the reasons why notice should not be required.

**Duration and dissolution:**

- Maximum duration: **14 days** (extendable once for good cause, another 14 days, or by
  consent)
- Must state the date and hour of issuance
- Binds only the parties, their officers, agents, servants, employees, attorneys, and
  those in active concert or participation

**Expedited hearing:**

- Court must set the preliminary injunction hearing at the **earliest possible time**
- Takes precedence over all matters except older matters of the same character
- If movant does not proceed with the preliminary injunction motion, the TRO is dissolved

**Practical emergency procedures:**

- Many federal districts have emergency judge-of-the-day procedures
- After-hours and weekend filings: check local rules and individual judge standing orders
- Some courts require pre-motion conference or chambers call before emergency filing
- Email service: some districts allow emergency email notice to opposing counsel even
  for ex parte applications

**Checklist for FRCP 65(b) ex parte TRO application:**

- [ ] Verified complaint or affidavit with specific facts of irreparable harm
- [ ] FRCP 65(b)(1)(A): imminent harm clearly shown on the face of the papers
- [ ] FRCP 65(b)(1)(B): attorney certification of notice attempts
- [ ] Memorandum of law addressing all four Winter factors
- [ ] Proposed TRO order with specific terms
- [ ] FRCP 65(c): proposed bond amount or argument for waiver
- [ ] Certificate stating date, hour, reason for ex parte issuance
- [ ] Compliance with local rules (page limits, chambers copies, etc.)

### UK: CPR Part 25 Without-Notice Applications

**General rule**: No order should be made without notice unless there is a very good
reason for departing from the general principle that notice must be given.

**When without-notice orders may be made (CPR 25.3(1)):**

- Where giving notice would defeat the purpose of the order (e.g., dissipation of
  assets, destruction of evidence)
- Where there is exceptional urgency — no time to give notice before the threatened
  wrongful act

**Full and frank disclosure obligation:**
The applicant and their solicitors have an absolute obligation to disclose all material
facts to the court, including facts that might weigh against granting the order. Failure
to give full and frank disclosure is grounds for discharge of the order.

**Fortified cross-undertaking in damages:**
The applicant gives an undertaking to pay damages to the respondent if it is later
found that the order ought not to have been granted. For significant orders, the court
may require:

- A fortification payment into court
- A bank guarantee
- Evidence of sufficient assets to meet the undertaking

**Return date:**
All without-notice orders must include a return date — an inter partes hearing within
days — at which the respondent may apply to discharge the order.

---

## Bond and Security Requirements

### US: FRCP 65(c)

**Statutory requirement:**

> The court may issue a preliminary injunction or a temporary restraining order only
> if the movant gives security in an amount that the court considers proper to pay the
> costs and damages sustained by any party found to have been wrongfully enjoined or
> restrained.

**Setting the bond amount:**
The court has broad discretion. Factors:

- The potential harm to the enjoined party during the period of the injunction
- Lost profits or revenue from compliance
- Costs of compliance
- Reasonable worst-case scenario for the respondent

**Waiver of bond:**
Courts may waive the bond requirement in limited circumstances [VERIFY]:

- Government plaintiff (United States, its officers, agencies)
- Nominal or no likelihood of harm to the enjoined party
- De minimis risk to the enjoined party
- Public interest cases (some circuits)
- When the court lacks jurisdiction to issue a bond waiver as a matter of statutory
  interpretation (circuit split)

**Practical bond considerations:**

- A low bond benefits the movant (less security at risk) but weakens the injunction's
  credibility
- A high bond may be unaffordable but demonstrates confidence in the case
- The bond does not limit the enjoined party's actual recovery if the injunction
  is dissolved; in some circuits, the bond caps recovery [VERIFY]

### UK: Cross-Undertaking in Damages

The applicant's **cross-undertaking in damages** is the price of obtaining an interim
injunction in the UK. If the injunction is later shown to have been wrongly granted,
the respondent may apply for an inquiry as to damages on the cross-undertaking.

**Scope of undertaking:**

- Covers losses caused by the injunction, even if applicant wins at trial
- Applies if the action is discontinued, not pursued, or the applicant loses
- May extend to third parties affected by the injunction

**Fortification:**
Where there is doubt about the applicant's ability to pay, the court may order
fortification — typically a payment into court or bank guarantee.

**No undertaking required:**

- Crown (HM Government) is not required to give a cross-undertaking when acting
  in a public capacity [VERIFY]

---

## Prospect Classification System

Classify each factor, then derive an overall assessment.

### Factor Ratings

| Rating       | Meaning                                          | Indicia                                                                  |
| ------------ | ------------------------------------------------ | ------------------------------------------------------------------------ |
| **STRONG**   | Factor clearly favors granting relief            | Compelling evidence, on-point authority, no significant counterarguments |
| **MODERATE** | Factor favors granting relief but not decisively | Colorable showing, genuine disputes, some counterarguments               |
| **WEAK**     | Factor does not clearly support granting relief  | Missing evidence, unfavorable precedent, strong counterarguments         |

### Overall Assessment

| Assessment       | Rating Combination                                                          | Meaning                                                                     |
| ---------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **GRANT-LIKELY** | 3+ STRONG factors, or 4 MODERATE+ factors, with no WEAK on irreparable harm | Motion is strong; counsel should proceed with confidence                    |
| **BORDERLINE**   | Mixed (some STRONG, some MODERATE, some WEAK); no single fatal weakness     | Motion viable but uncertain; outcome depends on judge and specific briefing |
| **DENY-LIKELY**  | Irreparable harm WEAK, or 2+ STRONG WEAKs, or fundamental legal deficiency  | Motion faces a high likelihood of denial; reconsider strategy               |

### Sliding Scale Adjustment (2d, 7th, 9th Circuits)

In circuits permitting the sliding scale approach, MODERATE on the merits may be
offset by STRONG on irreparable harm and balance of equities, and vice versa. Note
which circuit governs and state the applicable standard explicitly.

---

## Prioritization Framework

When resources and time are limited, prioritize these elements of the motion:

| Priority                  | Element                                                                  | Rationale                                                                                              |
| ------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| **Tier 1 — Must address** | Irreparable harm; likelihood of success; declaratory/evidentiary support | Courts most often deny based on inadequate irreparable harm showing; merits must be at least colorable |
| **Tier 1 — Must address** | FRCP 65(b) certification / UK full and frank disclosure                  | Procedural defects can void the order regardless of merits                                             |
| **Tier 2 — Important**    | Balance of equities; public interest; bond analysis                      | Required under the test; weak arguments on these factors can turn a borderline case                    |
| **Tier 2 — Important**    | Scope of proposed order                                                  | Overbroad injunctions are denied or narrowed; propose precise, enforceable relief                      |
| **Tier 3 — Supporting**   | Background narrative; procedural history; choice of court                | Helpful context but secondary to substantive showings                                                  |

---

## Motion Drafting Standards

### Structure of a US Preliminary Injunction Brief

1. **Introduction** (1–2 paragraphs): Crystallize the harm, the relief sought, and why
   the legal standard is met — write this last but place it first.
2. **Factual Background**: The relevant facts, organized chronologically or topically,
   supported by declaration references; keep short — facts belong in declarations.
3. **Legal Standard**: State the Winter test or circuit variant; do not overbrief this.
4. **Argument**:
   - I. Plaintiff Is Likely to Succeed on the Merits
   - II. Plaintiff Will Suffer Irreparable Harm Absent Injunctive Relief
   - III. The Balance of Equities Favors Plaintiff
   - IV. The Public Interest Supports Injunctive Relief
5. **Scope of Relief**: Specify the exact conduct to be enjoined; proposed duration;
   bond amount.
6. **Conclusion**: Recite the relief sought with precision.

### FRCP 65(b) Ex Parte TRO Certificate

```
CERTIFICATE OF COUNSEL PURSUANT TO FED. R. CIV. P. 65(b)

I, [Name], counsel for Plaintiff, certify as follows:

1. On [date/time], I [describe notice efforts: e.g., "attempted to reach counsel for
   Defendant by telephone at [number] and email at [address]"].
2. [Outcome of notice efforts / reason notice was not possible].
3. Immediate and irreparable injury will result to Plaintiff before the adverse party
   can be heard because [specific reason].

Dated: [date]          ______________________
                        [Attorney Name]
```

### Structure of a UK High Court Application

1. **Application Notice** (Form N244 or Chancery Form): States the order sought and
   the legal basis.
2. **Witness Statement / Affidavit**: Sets out the facts; for without-notice
   applications, must contain full and frank disclosure.
3. **Skeleton Argument** (for hearings with time): Concise argument addressing each
   American Cyanamid stage.
4. **Draft Order**: Precise terms of the injunction; return date; service provisions;
   liberty to apply.
5. **Undertaking in Damages**: Stated on the draft order or in the witness statement.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise
before delivery.

| Gate           | Rule                                                                                   | Fail Action                            |
| -------------- | -------------------------------------------------------------------------------------- | -------------------------------------- |
| **Source**     | Every legal proposition cites a case, rule, or statute                                 | Add citation or mark `[UNVERIFIED]`    |
| **Format**     | Citations follow a recognizable format (Bluebook for US, OSCOLA for UK)                | Fix format                             |
| **Currency**   | Cited authority checked for overruling, amendment, or supersession                     | Flag `[CHECK CURRENCY]`                |
| **Domain**     | Analysis stays within the asserted jurisdiction; no bleed between US and UK frameworks | Remove or flag jurisdictional bleed    |
| **Confidence** | Uncertainty is stated, not hidden                                                      | Add confidence qualifier or `[VERIFY]` |

### Self-Interrogation for Factor Assessments

For any factor rated **WEAK** or any overall assessment of **DENY-LIKELY**, apply
this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the weakness assessment follow from the cited
authority? Would a court actually reach the same conclusion given the stated facts?
Is there any favorable authority that has not been considered?

**Pass 2 — Completeness**: Have all relevant arguments been considered? Are there
equitable doctrines, statutory presumptions, or circuit-specific rules that might
strengthen the showing? Have supporting declarations been adequately considered?

**Pass 3 — Challenge**: What is the strongest argument for the movant on this factor?
Under what presentation of the facts might a sympathetic court find in their favor?
Is the weakness truly fatal, or is it manageable with better briefing?

### Confidence Scoring

| Level        | Range     | Meaning                                           | Action                                                                  |
| ------------ | --------- | ------------------------------------------------- | ----------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, strong facts, on-point authority     | State with confidence                                                   |
| **High**     | 0.80–0.94 | Strong authority, minor factual disputes          | State with brief caveat                                                 |
| **Probable** | 0.60–0.79 | Good arguments, genuine disputes or uncertain law | State with reasoning and contra-indicators                              |
| **Possible** | 0.40–0.59 | Genuinely uncertain; outcome dependent on judge   | Flag for counsel judgment; present both sides                           |
| **Unlikely** | 0.0–0.39  | Weak basis, significant adverse authority         | Do not assert without flagging `[UNCERTAIN]`; recommend reconsideration |

---

## Glass Box Audit Trail

Append this YAML block to every output:

```yaml
glass_box:
  skill_name: "legalcode-injunctive-relief-motion"
  matter: "[Brief matter description]"
  relief_type: "[TRO ex parte / TRO noticed / Preliminary injunction / UK without-notice / UK on-notice / Freezing order / Other]"
  framework_applied: "[Winter / Dataphase / American Cyanamid / Cyanamid + freezing order / Other]"
  jurisdiction: "[Court, circuit or division]"
  underlying_claim: "[Nature of the substantive claims]"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[/tmp/injunction-authority.md or 'Not created']"
  factor_ratings:
    factor_1_merits: "[STRONG / MODERATE / WEAK — one-line rationale]"
    factor_2_irreparable_harm: "[STRONG / MODERATE / WEAK — one-line rationale]"
    factor_3_balance_of_equities: "[STRONG / MODERATE / WEAK — one-line rationale]"
    factor_4_public_interest: "[STRONG / MODERATE / WEAK — one-line rationale]"
  overall_assessment: "[GRANT-LIKELY / BORDERLINE / DENY-LIKELY]"
  confidence_score: "[X.XX — level — brief rationale]"
  mandatory_vs_prohibitory: "[Mandatory / Prohibitory / Mixed — heightened standard applied: yes/no]"
  ex_parte_sought: "[Yes / No — FRCP 65(b) cert included: yes/no]"
  bond_analysis: "[Proposed amount / Waiver argument / UK cross-undertaking only]"
  key_weaknesses: "[List the top 1–3 weaknesses identified]"
  citations_verified: "[N VERIFIED via legalcode-mcp / M [VERIFY] tags applied]"
  limitations:
    - "[Any scope limitations, assumptions, or facts assumed without verification]"
  reviewer: "AI-assisted — requires qualified legal counsel review and Rule 11 / professional conduct verification before filing"
```

---

## Anti-Patterns

What NOT to do when drafting or analyzing injunctive relief applications:

1. **Overstating the legal standard**: Arguing "a chance of success" rather than
   "likelihood of success" (Winter). Courts immediately recognize this error and it
   undermines credibility on every other argument.

2. **Conflating TRO and preliminary injunction standards**: They share the same
   four-factor test in US federal courts, but ex parte TROs require the additional
   FRCP 65(b) showing. Don't omit the certification requirement.

3. **Generic irreparable harm recitations**: Using boilerplate "plaintiff will suffer
   irreparable harm" without specific, fact-supported analysis. Post-_Winter_, courts
   require concrete evidence that harm is **likely** — not merely possible.

4. **Ignoring delay**: A plaintiff who knew of the violation for months and then claims
   "emergency" relief has a serious credibility problem. Address delay head-on or the
   court will raise it.

5. **Conflating US and UK frameworks**: The "balance of convenience" in UK law is not
   the same as "balance of equities" in US law. The UK "serious question" threshold is
   lower than US "likelihood of success." Never mix and match.

6. **Missing the mandatory injunction heightened standard**: Treating a request to
   require the defendant to actively do something (mandatory) the same as a request
   to stop them from doing something (prohibitory). Courts apply a stricter standard
   to mandatory injunctions and will deny if the heightened showing is not made.

7. **Overbroad proposed orders**: Drafting a proposed injunction order that covers
   conduct far beyond what the court is being asked to enjoin. Overbroad orders are
   denied or sharply narrowed; they also signal to the court that the movant is
   overreaching.

8. **Ignoring the bond requirement**: Failing to propose a bond amount or argue
   for waiver. Courts may condition the injunction on a substantial bond — if the
   movant cannot pay, the strategy must account for this.

9. **No FRCP 65(b) certificate for ex parte TROs**: Filing an ex parte TRO motion
   without the attorney certification of notice efforts and reasons why notice should
   not be required. This is a mandatory procedural requirement; its absence is grounds
   for denial.

10. **Inadequate full and frank disclosure (UK)**: In UK without-notice applications,
    failing to disclose all material facts — including facts adverse to the applicant.
    Non-disclosure is an independent ground for discharge of the order even if the
    applicant ultimately prevails on the merits.

11. **Ignoring local rules and individual judge practices**: Emergency motion
    procedures vary widely by district, division, and individual judge. Filing without
    checking local rules and standing orders can result in rejection, sanctions, or
    delay that defeats the purpose of emergency relief.

12. **Proposing duration without a hearing**: US TROs expire after 14 days absent
    good cause; failing to schedule the preliminary injunction hearing promptly can
    result in dissolution of the TRO. UK without-notice orders must include a return
    date.

13. **Conflating preliminary injunction with permanent injunction**: The _eBay v.
    MercExchange_ (2006) four-factor test applies to permanent injunctions; _Winter_
    governs preliminary injunctions. The analysis differs at the merits-certainty level.
    In permanent injunction analysis, the court has made a final determination on the
    merits; at the preliminary stage, it has not.

14. **Ignoring the cross-undertaking exposure (UK)**: In UK practice, the applicant's
    cross-undertaking in damages is a real financial obligation. Clients must understand
    that winning the interim injunction may still result in a substantial damages
    inquiry if the case later fails. Factor this into the strategic advice.

15. **Seeking anti-suit injunction without comity analysis**: Anti-suit injunctions
    are extraordinary remedies affecting relations with foreign courts. Seeking one
    without addressing international comity principles, the applicable circuit test,
    and why the case meets the threshold will result in denial and may damage
    credibility with the court.

---

## Writing Standards

Apply these standards before delivering any output:

1. **Precision over rhetoric**: Courts are persuaded by precision, not hyperbole.
   Replace "egregious," "blatant," and "shocking" with specific facts that speak
   for themselves.

2. **Fact-law integration**: Every legal argument must be tied to specific facts.
   Abstract legal arguments without factual application are not persuasive.

3. **Active, declaratory voice**: "Defendant took X on Y date" — not "it is believed
   that Defendant may have taken X."

4. **Concrete harm description**: Quantify harm wherever possible. "Plaintiff will
   lose its only customer relationship with [Company], representing $2.4M in annual
   revenue" is more persuasive than "Plaintiff will lose business."

5. **Proportionality of proposed relief**: The scope of the injunction must match
   the harm. Courts reject overreaching — propose only what is necessary to prevent
   the specific harm identified.

6. **Verified declarations**: The strength of the motion depends heavily on the
   supporting declaration. Flag where declarant testimony is needed and what specific
   facts each declaration must establish.

7. **Tone calibration**: Emergency motions should convey urgency without hysteria.
   Courts are sophisticated readers; measured, factual urgency is more persuasive
   than breathless hyperbole.

8. **Local rule compliance**: Check word/page limits, filing format, chambers copies,
   and any pre-motion conference requirements before finalizing.

---

## External Tool Integration

**With legalcode-mcp connected:**

- Search for circuit-specific cases applying Winter to the subject matter area
  (e.g., "preliminary injunction trade secrets 9th circuit irreparable harm")
- Search for the applicable district's TRO local rules and recent TRO decisions
- For UK matters: search for recent American Cyanamid applications in the relevant
  division and subject matter
- Verify currency of key cases (check for subsequent history, overruling, or
  significant limitations)
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Apply general knowledge of the Winter/Cyanamid frameworks
- Mark all case citations `[VERIFY]` throughout the output
- Recommend that counsel independently verify all cited authority before filing
- Note in Glass Box: `legalcode_mcp: "Not connected"`

---

## Output Format Template

```markdown
# Injunctive Relief Analysis — [Matter Name]

**Date**: [Date]
**Skill**: legalcode-injunctive-relief-motion
**Relief Sought**: [TRO / Preliminary Injunction / UK Interim Injunction / Other]
**Court**: [Court name, circuit / division]
**Framework Applied**: [Winter four-factor / American Cyanamid / Other]

---

## Overall Assessment: [GRANT-LIKELY / BORDERLINE / DENY-LIKELY]

**Confidence**: [X.XX — Probable/High/Definite/Possible/Unlikely]

**Summary**: [2–3 sentences on the overall prospects and key considerations]

---

## Factor Analysis

### [US: Factor 1 / UK: Stage 1] — [Merits / Serious Question to Be Tried]

**Rating**: [STRONG / MODERATE / WEAK]

**Analysis**:
[Detailed analysis of the merits showing, citing evidence and authority]

**Key strengths**:

- [Strength 1]
- [Strength 2]

**Key weaknesses / risks**:

- [Weakness 1]
- [Weakness 2]

---

### [US: Factor 2 / UK: Stage 2a] — [Irreparable Harm / Adequacy of Damages]

**Rating**: [STRONG / MODERATE / WEAK]

**Analysis**:
[Detailed analysis of the irreparable harm showing]

---

### [US: Factor 3 / UK: Stage 2b] — [Balance of Equities / Balance of Convenience]

**Rating**: [STRONG / MODERATE / WEAK]

**Analysis**:
[Detailed analysis of the balance]

---

### [US: Factor 4 / UK: Status Quo] — [Public Interest / Preservation of Status Quo]

**Rating**: [STRONG / MODERATE / WEAK]

**Analysis**:
[Detailed analysis]

---

## Bond / Security Assessment

**Proposed bond amount (US)**: [$X — reasoning]
**Waiver argument (if applicable)**: [Basis for waiver, if any]

**UK cross-undertaking**: [Applicant's ability to satisfy; whether fortification required]

---

## Ex Parte / Without-Notice Assessment

_[Include only if ex parte / without-notice relief is sought]_

**FRCP 65(b) / CPR 25.3 requirements met**: [Yes / No / Partially — explanation]

**Certification language (FRCP 65(b))**: [Draft certification text or note that
counsel must complete based on actual notice attempts]

**UK full and frank disclosure items**: [List any matters adverse to the applicant
that must be disclosed]

---

## Argument Outline

### I. [Plaintiff/Applicant] Demonstrates [Likelihood of Success / A Serious Question

to Be Tried]

[Argument blocks for the merits showing, with authority and fact integration]

### II. [Plaintiff/Applicant] Will Suffer Irreparable Harm / Damages Are Inadequate

[Argument blocks addressing each category of harm]

### III. The Balance of [Equities / Convenience] Favors [Plaintiff/Applicant]

[Comparative harm analysis]

### IV. [The Public Interest Supports Relief / The Status Quo Should Be Preserved]

[Public interest / status quo argument]

### V. The Scope of the Proposed Order Is Appropriate

[Justification for the specific relief requested; response to overbreadth concerns]

---

## Proposed Order Elements

The proposed order should include:

- [ ] Specific identification of enjoined conduct (no vague "related conduct" catch-alls)
- [ ] Identification of who is bound (defendant, officers, agents, etc.)
- [ ] Geographic scope (if relevant)
- [ ] Duration (TRO: 14 days; preliminary injunction: pending trial or further order)
- [ ] Bond/security amount
- [ ] Return date for hearing (TRO without notice only)
- [ ] Service provisions
- [ ] Date and hour of issuance (TRO only)

---

## Supporting Declaration Framework

_The following facts must be established by declaration from a competent declarant:_

| Fact Required                                                                      | Declarant                     | Evidence Type                            |
| ---------------------------------------------------------------------------------- | ----------------------------- | ---------------------------------------- |
| [Fact 1 — e.g., "Plaintiff's description of the proprietary information at issue"] | [e.g., CEO]                   | [e.g., Personal knowledge]               |
| [Fact 2 — e.g., "Defendant's conduct constituting the violation"]                  | [e.g., Employee witness]      | [e.g., Documentary + personal knowledge] |
| [Fact 3 — e.g., "Harm and its non-compensability"]                                 | [e.g., CFO or damages expert] | [e.g., Financial records]                |

---

## Key Weaknesses and Recommended Mitigations

| Weakness     | Severity              | Recommended Mitigation                                      |
| ------------ | --------------------- | ----------------------------------------------------------- |
| [Weakness 1] | [HIGH / MEDIUM / LOW] | [How to address in briefing or through additional evidence] |
| [Weakness 2] | [HIGH / MEDIUM / LOW] | [Mitigation approach]                                       |

---

## Recommended Next Steps

1. [First action — e.g., "Obtain CEO declaration confirming [X] before filing"]
2. [Second action — e.g., "Check [District] local rules for emergency TRO procedures"]
3. [Third action — e.g., "Confirm bond capacity with client before filing"]

---

## Glass Box Audit Trail

[Append the YAML Glass Box block from the Quality Assurance section above]
```

---

## Localization Notes

This skill covers US federal court and UK High Court practice. When adapting for other
jurisdictions:

**Australia**: The American Cyanamid test generally applies; see _ABC v O'Neill_ [2006]
HCA 46 for the Australian formulation (prima facie case as one factor in the balance,
not a threshold). [VERIFY]

**Canada**: Courts apply a modified Cyanamid test from _RJR-MacDonald Inc v Canada_
[1994] 1 SCR 311 — three-stage: (1) serious question to be tried, (2) irreparable
harm, (3) balance of convenience. [VERIFY]

**Singapore**: The American Cyanamid test applies as modified by Singapore courts.
Note the strong practice in Singapore Commercial Court of maintaining status quo in
commercial cases. [VERIFY]

**European Union / Germany**: Injunctive relief is governed by national procedural
law with EU harmonization in some areas (e.g., IP). German einstweilige Verfügung has
a different standard (Glaubhaftmachung — credible showing). French référé is a
different expedited procedure. These are outside the scope of this skill. [VERIFY]

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on:

- _Winter v. Natural Resources Defense Council, Inc._, 555 U.S. 7 (2008)
- _American Cyanamid Co v Ethicon Ltd_ [1975] AC 396 (HL)
- _eBay Inc. v. MercExchange, L.L.C._, 547 U.S. 388 (2006) [permanent injunctions]
- _Monsanto Co. v. Geertson Seed Farms_, 561 U.S. 139 (2010)
- _Dataphase Systems, Inc. v. C.L. Systems, Inc._, 640 F.2d 109 (8th Cir. 1981)
- FRCP Rule 65 (TROs and Preliminary Injunctions)
- UK CPR Part 25 and Practice Direction 25A
- _Mareva Compania Naviera SA v International Bulkcarriers SA_ [1975] (freezing orders)
- _Anton Piller KG v Manufacturing Processes Ltd_ [1976] Ch 55 (search orders)
- Circuit-specific sliding scale variations (2d, 7th, 9th, 4th Circuits)
- Legalcode quality frameworks from `legalcode-contract-review` (Citation Quality Gates,
  Self-Interrogation, Confidence Scoring, Glass Box Audit Trail)
- Repository litigation skill patterns from `legalcode-motion-to-dismiss-drafter`

All statutory and case law references should be verified against current authority
before reliance in any filing.
