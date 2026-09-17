---
name: legalcode-complaint-drafter-ew
description: Drafts Particulars of Claim, claim forms, and other statements of case for civil proceedings
  in England & Wales under the Civil Procedure Rules (CPR). Maps client facts to the legal elements of
  each cause of action under English law, validates compliance with CPR Part 16 and relevant Practice
  Directions, checks pre-action protocol compliance, and structures jurisdictional allegations, factual
  narratives, causes of action, and prayer for relief. Covers County Court and High Court proceedings
  across all tracks (small claims, fast track, intermediate track, multi-track). Produces court-ready
  Particulars of Claim with numbered paragraphs, statements of truth, schedules of loss, and document
  attachments as required. Includes pre-action protocol compliance checks, SRA professional conduct validation,
  and strategic claim selection guidance. Companion to legalcode-complaint-drafter (US federal/state).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Complaint Drafter — England & Wales

> **Disclaimer**: This skill provides a framework for AI-assisted drafting of
> statements of case under the Civil Procedure Rules. It does not constitute
> legal advice. All outputs must be reviewed, verified, and signed by a
> qualified solicitor or barrister authorised by the SRA or BSB and entitled
> to conduct litigation in England & Wales before filing with any court.
> Procedural rules, practice directions, and case law change frequently;
> verify all authoritative sources before relying on any conclusion. AI-generated
> pleadings may contain errors in element identification, jurisdictional
> analysis, or factual characterisation — all allegations must be verified
> against actual evidence and client instructions. Any cited authority marked
> `[VERIFY]` has not been independently validated and must be confirmed before
> reliance. Filing a statement of case requires a statement of truth certifying
> that the facts stated are believed to be true; a false statement constitutes
> contempt of court punishable by imprisonment.

---

## Purpose and Scope

This skill drafts Particulars of Claim and related statements of case for
civil proceedings in England & Wales. It maps client facts to the legal
elements of each cause of action under English common law and statute,
validates compliance with the Civil Procedure Rules (CPR) and relevant
Practice Directions, and produces court-ready documents.

**Covers:**

- Particulars of Claim for Part 7 proceedings (CPR Part 16)
- Claim forms (Form N1) with statement of value
- Pre-action protocol compliance verification
- Causes of action under English contract, tort, equity, employment, and commercial law
- Track allocation assessment (small claims, fast track, intermediate track, multi-track)
- County Court and High Court proceedings (including specialist courts)
- Statement of truth requirements (CPR Part 22)
- Schedules of loss and damage
- Interim remedy applications (freezing orders, search orders, interim injunctions)
- Part 20 additional claims (counterclaims, contribution, indemnity)

**Does not cover:**

- Part 8 claims (alternative procedure for claims without substantial factual dispute)
- Family proceedings (governed by FPR, not CPR)
- Tribunal proceedings (Employment Tribunal, First-tier Tribunal — separate rules)
- Criminal proceedings
- Arbitration claims (separate regime under Arbitration Act 1996)
- Judicial review (separate pre-action protocol and procedure)
- Scottish or Northern Irish proceedings (separate civil procedure rules)

**Related skills:**

- `legalcode-complaint-drafter` — US federal/state complaint drafting
- `legalcode-brief-analyzer` — Analysis of legal briefs and submissions
- `legalcode-case-timeline-builder` — Chronological fact organisation
- `legalcode-damages-calculation` — Damages quantification framework

---

## Jurisdiction and Governing Law

This skill is **jurisdiction-specific to England & Wales**. All procedural
references are to the Civil Procedure Rules 1998 (CPR) as amended, associated
Practice Directions, and the Pre-Action Conduct Practice Direction. Substantive
law references are to English common law, equity, and statute.

**Key procedural sources:**

- Civil Procedure Rules 1998 (SI 1998/3132) as amended
- Practice Directions supplementing the CPR
- Pre-Action Conduct and Protocols Practice Direction
- Court forms (N series)
- Senior Courts Act 1981
- County Courts Act 1984
- Limitation Act 1980

**Court hierarchy:**

- County Court → High Court (King's Bench / Chancery / Family Division) → Court of Appeal → Supreme Court
- Specialist courts: Commercial Court, Technology and Construction Court (TCC), Admiralty Court, Patents Court, Intellectual Property Enterprise Court (IPEC), Business and Property Courts

---

## Interactive Clarification

Before drafting, gather context through structured clarification. Use
**CLARIFY** markers to indicate where to pause for user input. Only ask
questions whose answers would change the analysis direction. When the user
provides sufficient context in their initial prompt, proceed without asking.

**CLARIFY 1 — Claim objective**

> What is the primary objective of this claim?
>
> **Options:**
>
> - Damages (monetary compensation)
> - Injunctive relief (requiring defendant to do or stop doing something)
> - Declaration (court ruling on legal rights)
> - Specific performance (enforcing contractual obligation)
> - Account of profits
> - Mixed (multiple remedy types)
>
> **Default:** Damages
>
> **Why this matters:** Determines the structure of the prayer for relief,
> whether interim applications are needed, and affects statement of value
> and track allocation.

**CLARIFY 2 — Claim type and causes of action**

> What type of claim is this? (Select all that apply)
>
> **Options:**
>
> - Breach of contract
> - Professional negligence
> - General negligence / personal injury
> - Fraud / misrepresentation
> - Breach of fiduciary duty
> - Property / land dispute
> - Intellectual property
> - Employment (wrongful dismissal — common law)
> - Commercial tort (conspiracy, inducing breach, unlawful means)
> - Defamation / malicious falsehood
> - Breach of confidence / privacy
> - Other (specify)
>
> **Default:** Infer from facts provided
>
> **Why this matters:** Each cause of action has specific elements that must
> be pleaded, and some (fraud, dishonesty) require heightened specificity
> under PD 16 para 8.2. Determines which pre-action protocol applies.

**CLARIFY 3 — Court and track**

> Which court should this claim be issued in?
>
> **Options:**
>
> - County Court (claims up to £100,000; PI up to £50,000)
> - High Court — King's Bench Division (claims over £100,000; PI over £50,000)
> - High Court — Chancery Division (trusts, land, IP, company)
> - Commercial Court (high-value commercial disputes)
> - Technology and Construction Court (TCC)
> - Intellectual Property Enterprise Court (IPEC) (IP claims up to £500,000)
> - Not sure — advise based on claim value and type
>
> **Default:** Determine from claim value and subject matter
>
> **Why this matters:** Affects claim form requirements, court fees, available
> procedures, and whether the claim will be allocated to small claims, fast
> track, intermediate track, or multi-track.

**CLARIFY 4 — Pre-action protocol status**

> Has pre-action protocol been followed?
>
> **Options:**
>
> - Yes — Letter of Claim sent and Letter of Response received
> - Partially — Letter of Claim sent but no response yet
> - No — not yet commenced (skill will draft Letter of Claim first)
> - Not applicable — urgent interim relief needed
> - Unsure which protocol applies
>
> **Default:** Assume not yet commenced; check applicable protocol
>
> **Why this matters:** Courts impose costs sanctions for non-compliance
> with pre-action protocols. If protocol is incomplete, may need to defer
> issuing proceedings or explain urgency.

**CLARIFY 5 — Parties**

> Who are the parties to this claim?
>
> **Information needed:**
>
> - Claimant(s): Full name, address, status (individual / company / partnership / LLP / trustee)
> - Defendant(s): Full name, address (if known), status, registered company number (if applicable)
> - Any representative or litigation friend issues
> - Multiple defendants: joint liability, several liability, or both
>
> **Default:** Extract from facts provided
>
> **Why this matters:** Party status determines how they are identified in
> the claim form, whether a corporate disclosure is needed, and affects
> jurisdiction and service requirements.

**CLARIFY 6 — Available evidence and documents**

> What evidence and documents are available?
>
> **Options:**
>
> - Contracts / agreements
> - Correspondence (letters, emails)
> - Financial records (invoices, accounts, bank statements)
> - Expert reports (medical, surveyor, forensic accountant)
> - Witness accounts
> - Photographs / video
> - Limited — key documents in opponent's possession
>
> **Default:** Assess from materials provided
>
> **Why this matters:** Determines what documents to attach to the Particulars,
> whether pre-action disclosure is needed, and affects the specificity of
> factual allegations.

**CLARIFY 7 — Limitation**

> When did the cause of action accrue? Are there any limitation concerns?
>
> **Information needed:**
>
> - Date of breach / tort / accrual
> - Whether claimant had knowledge of facts (for latent damage / PI)
> - Any standstill agreements
> - Whether fraud or concealment applies (s.32 Limitation Act 1980)
>
> **Default:** Flag limitation analysis for counsel review
>
> **Why this matters:** If limitation is approaching, may need to issue
> protective proceedings urgently even if pre-action protocol incomplete.
> Different causes of action have different limitation periods.

**CLARIFY 8 — Costs and funding**

> What is the costs and funding position?
>
> **Options:**
>
> - Private funding (client paying)
> - Conditional fee agreement (CFA / "no win no fee")
> - Damages-based agreement (DBA)
> - Legal expenses insurance (BTE or ATE)
> - Legal aid
> - Other
>
> **Default:** Private funding
>
> **Why this matters:** Affects costs budgeting requirements, whether QOCS
> applies (personal injury), and the costs information that must be provided
> to the defendant.

---

## Workflow

### Step 1: Accept client input

Accept the client's matter via any of:

- File path to client instructions, witness statement, or draft documents
- Pasted text with factual narrative and client objectives
- Reference to prior correspondence or pre-action documents
- Combination of the above

Regardless of input format, extract:

- **Parties** (names, roles, relationships, legal status)
- **Key facts** (chronological events, dates, amounts)
- **Causes of action** (explicit or to be identified from facts)
- **Relief sought** (damages, injunction, declaration, specific performance)
- **Limitation position** (dates of accrual, any concerns)
- **Pre-action protocol status** (Letters of Claim / Response exchanged?)
- **Available documents** (contracts, correspondence, reports)

### Step 2: Gather context via interactive clarification

Run through CLARIFY 1-8 above. Skip any question already answered by the
initial input. Present remaining questions as a structured list.

### Step 3: Pre-action protocol compliance check

Identify the applicable pre-action protocol:

| Claim Type                 | Applicable Protocol                                                                                                                             |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Personal injury            | Pre-Action Protocol for Personal Injury Claims                                                                                                  |
| Clinical negligence        | Pre-Action Protocol for the Resolution of Clinical Disputes                                                                                     |
| Professional negligence    | Pre-Action Protocol for Professional Negligence                                                                                                 |
| Construction / engineering | Pre-Action Protocol for Construction and Engineering Disputes                                                                                   |
| Defamation / privacy       | Pre-Action Protocol for Media and Communications Claims                                                                                         |
| Debt recovery              | Pre-Action Protocol for Debt Claims                                                                                                             |
| Housing disrepair          | Pre-Action Protocol for Housing Conditions Claims                                                                                               |
| Judicial review            | Pre-Action Protocol for Judicial Review                                                                                                         |
| Disease / illness          | Pre-Action Protocol for Disease and Illness Claims                                                                                              |
| Package travel             | Pre-Action Protocol for Package Travel Claims                                                                                                   |
| Dilapidations              | Pre-Action Protocol for Claims for Damages in Relation to the Physical State of Commercial Property at Termination of a Tenancy (Dilapidations) |
| All other claims           | Practice Direction — Pre-Action Conduct and Protocols (general)                                                                                 |

**Compliance checklist:**

- [ ] Correct protocol identified
- [ ] Letter of Claim sent in compliant format
- [ ] Reasonable time for response allowed (protocol-specific; typically 14 days to 3 months)
- [ ] Letter of Response received (or time expired)
- [ ] Relevant documents disclosed as required by protocol
- [ ] ADR considered and position documented
- [ ] Expert evidence obtained if required by protocol (e.g., medical report in PI)
- [ ] If protocol not followed: justification documented (urgency, limitation)

**If protocol not yet followed:**

- Draft Letter of Claim in protocol-compliant format
- Advise on timing before proceedings can be issued
- If limitation is imminent: advise on issuing protective proceedings with explanation to court

### Step 4: Identify and select causes of action

Map the facts to available causes of action under English law. For each
potential cause of action:

1. **Element check** — Does the factual matrix support each required element?
2. **Evidence assessment** — Is there evidence (or reasonable prospect of
   obtaining evidence through disclosure) to support each element?
3. **Limitation check** — Is the claim within the applicable limitation period?
4. **Merits assessment** — Would the claim survive a strike-out application
   (CPR 3.4) or summary judgment application (CPR Part 24)?
5. **Costs-benefit analysis** — Given the loser-pays costs regime, is this
   claim worth pursuing?

**Decision matrix for claim inclusion:**

| Factor                                         | Include | Exclude |
| ---------------------------------------------- | ------- | ------- |
| All elements supported by facts                | ✓       |         |
| Strong evidential basis                        | ✓       |         |
| Within limitation                              | ✓       |         |
| Reasonable prospect of success (CPR 24.2 test) | ✓       |         |
| Proportionate to value of claim                | ✓       |         |
| Missing elements without prospect of evidence  |         | ✓       |
| Limitation expired without s.32/s.33 extension |         | ✓       |
| No reasonable grounds (CPR 3.4(2)(a))          |         | ✓       |
| Costs disproportionate to likely recovery      |         | ✓       |

### Step 5: Determine court and track allocation

**Court selection:**

| Criterion                 | County Court   | High Court                                  |
| ------------------------- | -------------- | ------------------------------------------- |
| Claim value               | Up to £100,000 | Over £100,000                               |
| Personal injury value     | Up to £50,000  | Over £50,000                                |
| Specialist subject matter | Limited        | Commercial Court, TCC, Chancery, Patents    |
| Complexity                | Standard       | Complex, multi-party, public importance     |
| Injunctive relief         | Available      | Full range including freezing/search orders |

**Track allocation (CPR Part 26):**

| Track              | Value                    | Trial Length    | Features                                                                 |
| ------------------ | ------------------------ | --------------- | ------------------------------------------------------------------------ |
| Small claims       | ≤ £10,000 (PI: ≤ £1,000) | Usually < 1 day | Limited costs recovery; no disclosure; informal                          |
| Fast track         | £10,000 – £25,000        | ≤ 1 day         | Fixed costs; standard disclosure; strict timetable                       |
| Intermediate track | £25,000 – £100,000       | ≤ 3 days        | Fixed recoverable costs; proportionate procedure [VERIFY current status] |
| Multi-track        | > £100,000 (or complex)  | Variable        | Full costs budgeting; disclosure; case management conferences            |

### Step 6: Draft claim form (Form N1)

```
IN THE [COUNTY COURT AT [LOCATION] / HIGH COURT OF JUSTICE
[KING'S BENCH DIVISION / CHANCERY DIVISION / [SPECIALIST COURT]]]

CLAIM NO: [To be assigned]

BETWEEN:

                    [CLAIMANT NAME]                     Claimant

                         — and —

                    [DEFENDANT NAME]                    Defendant

                    ____________________

                       CLAIM FORM
                    ____________________

Brief details of claim:
[Concise statement of the nature of the claim — 2-3 sentences maximum]

Value:
The Claimant expects to recover [not more than £10,000 / more than £10,000
but not more than £25,000 / more than £25,000 but not more than £100,000 /
more than £100,000].

[For personal injury claims: The Claimant expects to recover general damages
for pain, suffering, and loss of amenity of [not more than £1,000 / more
than £1,000].]

Defendant's name and address:
[Full name and address including postcode]

Amount claimed:        £[amount]
Court fee:             £[fee per EX50]
Legal representative's costs: £[amount]
Total amount:          £[total]

Does your claim include any issues under the Human Rights Act 1998?  [Yes/No]

Particulars of Claim [attached / to follow]
```

### Step 7: Draft Particulars of Claim

Structure the Particulars of Claim as follows:

**Heading:**

```
IN THE [COURT]

CLAIM NO: [number]

BETWEEN:

                    [CLAIMANT NAME]                     Claimant

                         — and —

                    [DEFENDANT NAME]                    Defendant

                    ____________________

                 PARTICULARS OF CLAIM
                    ____________________
```

**Body — numbered paragraphs:**

1. **The Parties** (¶¶ 1-X)
   - Claimant's identity, capacity, and relevant status
   - Defendant's identity, capacity, and relevant status
   - Relationship between parties (if relevant)

2. **Background / Factual Matrix** (¶¶ X-Y)
   - Concise statement of material facts in chronological order
   - Reference to key documents ("the Agreement", "the Email")
   - Only **material facts** — not evidence, not law
   - Each material fact in its own paragraph

3. **The Contract / Duty / Relationship** (¶¶ Y-Z)
   - For contract claims: formation, terms (express and implied)
   - For tort claims: duty of care and its basis
   - For equitable claims: the fiduciary relationship or confidence

4. **Breach / Wrong** (¶¶ Z-A)
   - Specific acts or omissions constituting the breach or wrong
   - Particulars of each breach, numbered and itemised
   - For fraud/dishonesty: full particulars required (PD 16 para 8.2)

5. **Causation and Loss** (¶¶ A-B)
   - How the breach/wrong caused the loss
   - Specific heads of damage
   - Reference to schedule of loss (if separate)

6. **Interest** (¶¶ B-C)
   - Statutory basis (Senior Courts Act 1981 s.35A / County Courts Act 1984 s.69)
   - Or contractual basis
   - Rate claimed and calculation

7. **Prayer for Relief**

   ```
   AND THE CLAIMANT CLAIMS:

   (1) Damages [/ to be assessed];
   (2) Interest pursuant to section 35A of the Senior Courts Act 1981
       [/ section 69 of the County Courts Act 1984] at such rate and
       for such period as the Court thinks fit;
   (3) [Injunctive relief — specify];
   (4) [Specific performance — specify];
   (5) [Declaration — specify];
   (6) Costs;
   (7) Such further or other relief as the Court thinks fit.
   ```

8. **Statement of Truth**

   ```
   STATEMENT OF TRUTH

   [I believe][The Claimant believes] that the facts stated in these
   Particulars of Claim are true. I understand that proceedings for
   contempt of court may be brought against anyone who makes, or
   causes to be made, a false statement in a document verified by a
   statement of truth without an honest belief in its truth.

   Signed: ____________________
   [Claimant / Claimant's Solicitor]
   Full name: [NAME]
   [Position or office held (if signing on behalf of company/firm)]
   Date: [DATE]

   [Claimant's / Claimant's solicitor's address for service]
   ```

### Step 8: Draft schedule of loss (if applicable)

For claims involving quantified losses, prepare a schedule:

**Personal injury schedule format:**

```
SCHEDULE OF PAST AND FUTURE EXPENSES AND LOSSES

PAST LOSSES (to date of schedule)

1. Loss of earnings
   [Details with dates and calculation]                    £[amount]

2. Medical expenses
   [Details]                                               £[amount]

3. Travel expenses
   [Details]                                               £[amount]

4. Care and assistance
   [Details with hours and rates]                          £[amount]

TOTAL PAST LOSSES                                          £[amount]

FUTURE LOSSES

5. Future loss of earnings
   [Details with multiplier/multiplicand]                  £[amount]

6. Future medical treatment
   [Details]                                               £[amount]

7. Future care
   [Details]                                               £[amount]

TOTAL FUTURE LOSSES                                        £[amount]

GENERAL DAMAGES

8. Pain, suffering, and loss of amenity
   [Reference to JC Guidelines bracket]                    £[amount]

TOTAL CLAIM                                                £[amount]
```

**Commercial loss schedule format:**

```
SCHEDULE OF LOSS AND DAMAGE

1. Direct losses
   (a) [Specific head of loss with particulars]            £[amount]
   (b) [Specific head of loss with particulars]            £[amount]

2. Consequential losses
   (a) [Specific head of loss with foreseeability basis]   £[amount]
   (b) [Specific head of loss with foreseeability basis]   £[amount]

3. Wasted expenditure (if claimed in alternative)
   (a) [Specific item]                                     £[amount]

4. Interest
   [Calculation]                                           £[amount]

TOTAL                                                      £[amount]
```

**Construction disputes — Scott Schedule format:**

```
| Item | Claimant's Description | Amount Claimed | Defendant's Response | Amount Admitted |
|------|----------------------|----------------|---------------------|----------------|
| 1 | [Defect/item] | £[amount] | [To be completed by Defendant] | [To be completed] |
```

### Step 9: Compliance review

Before delivering, run a compliance check:

**CPR Part 16 compliance:**

- [ ] Concise statement of facts relied on (CPR 16.4(1)(a))
- [ ] Details of interest claimed (CPR 16.4(2))
- [ ] Aggravated / exemplary damages grounds stated (if claimed) (CPR 16.4(1)(c))
- [ ] Provisional damages grounds stated (if claimed) (CPR 16.4(1)(d))
- [ ] Documents required by PD 16 attached
- [ ] Full particulars of fraud / illegality / misrepresentation (PD 16 para 8.2)
- [ ] Human rights claim details (PD 16 para 15) (if applicable)
- [ ] Statement of value in claim form (CPR 16.3)
- [ ] Personal injury: date of birth, injury details, schedule of loss, medical report (PD 16 para 4)

**Statement of truth compliance (CPR Part 22):**

- [ ] Correct wording used (post-6 April 2020 format)
- [ ] Appropriate signatory identified
- [ ] Full name printed beneath signature line

**Pre-action protocol compliance:**

- [ ] Correct protocol identified and followed
- [ ] Letter of Claim sent in compliant format
- [ ] Adequate time allowed for response
- [ ] ADR considered
- [ ] If non-compliant: justification documented

**Professional conduct (SRA):**

- [ ] Facts supported by client instructions
- [ ] No misleading allegations
- [ ] Reasonable basis for each cause of action
- [ ] No claim included solely for tactical pressure

### Step 10: Deliver statement of case

Output the complete package with:

1. **Particulars of Claim** — Court-ready formatted document
2. **Claim Form (N1) summary** — Key information for form completion
3. **Schedule of Loss** — If applicable
4. **Pre-Action Protocol Status** — Compliance assessment
5. **Element Mapping Table** — Which facts support which elements for each cause of action
6. **Merits Assessment** — Per-cause-of-action analysis of strike-out/summary judgment risk
7. **Track Allocation Assessment** — Recommended court and track
8. **Strategic Notes** — Claims considered but excluded, Part 36 considerations, costs analysis
9. **Glass Box Audit Trail** — Full YAML audit block

---

## Causes of Action Elements Library — English Law

<!-- PLACEHOLDER: Will be enriched with research from causes-of-action agent -->

### Contract Claims

**Breach of Contract**

Elements:

1. **Valid and binding contract** — offer, acceptance, consideration (or deed), intention to create legal relations, capacity
2. **Terms of the contract** — express terms (written / oral), implied terms (by statute, custom, business efficacy, officious bystander test)
3. **Breach by the defendant** — specific acts or omissions constituting breach, with particulars
4. **Causation** — the breach caused the loss (factual causation — "but for" test)
5. **Loss and damage** — specific, quantified losses flowing from the breach
6. **Remoteness** — loss was within the reasonable contemplation of the parties at the time of contracting (Hadley v Baxendale (1854) — two limbs) [VERIFY]

Pleading requirements:

- Identify the contract (date, parties, whether written or oral)
- If written: attach or identify the document
- If oral: plead when, where, between whom, and the words used (or their effect)
- Plead each term relied on and whether express or implied
- If implied by statute: identify the statute and section
- If implied at common law: state the basis (business efficacy / officious bystander / custom)
- Plead each specific breach with full particulars
- Plead causation and each head of loss

**Misrepresentation**

Types and elements:

_Fraudulent misrepresentation (Derry v Peek (1889)):_ [VERIFY]

1. Representation of fact (not opinion, unless speaker has no grounds for opinion)
2. Made by or on behalf of the defendant to the claimant
3. Representation was false
4. Defendant knew it was false, or was reckless as to its truth
5. Intended to induce the claimant to act on it
6. Claimant did act on it (reliance)
7. Claimant suffered loss as a result

_Negligent misrepresentation (Misrepresentation Act 1967 s.2(1)):_ [VERIFY]

1. Representation of fact
2. Made by or on behalf of the defendant
3. Representation was false
4. Induced the claimant to enter a contract
5. Claimant suffered loss
6. Burden shifts to defendant to prove reasonable grounds for believing truth (reversed burden)

_Innocent misrepresentation:_

1. Representation of fact
2. False
3. Induced the contract
4. Defendant had reasonable grounds for belief (defence to s.2(1))

Pleading requirements (PD 16 para 8.2):

- **Full particulars required** — who made the representation, to whom, when, in what terms
- Must distinguish between fraudulent, negligent (statutory), and innocent
- For fraud: must plead facts from which fraud can be inferred (not just allege dishonesty)
- Must plead reliance and the acts induced by the representation
- Must plead loss flowing from the misrepresentation

**Breach of Implied Terms — Consumer and Commercial**

_Sale of Goods Act 1979 (business-to-business):_ [VERIFY]

- s.12: Implied term as to title
- s.13: Goods to correspond with description
- s.14(2): Satisfactory quality
- s.14(3): Fitness for particular purpose
- s.15: Sale by sample

_Consumer Rights Act 2015 (business-to-consumer):_ [VERIFY]

- s.9: Satisfactory quality
- s.10: Fitness for particular purpose
- s.11: Goods to be as described
- s.12: Other pre-contract information included as term
- s.13: Goods to match a model seen or examined
- s.17: Trader to have right to supply the goods

_Supply of Goods and Services Act 1982:_ [VERIFY]

- s.13: Implied term that services carried out with reasonable care and skill
- s.14: Reasonable time for performance (where not specified)
- s.15: Reasonable charge (where not specified)

**Unjust Enrichment / Restitution**

Elements (Banque Financière de la Cité v Parc (Battersea) Ltd [1999]): [VERIFY]

1. Defendant has been enriched
2. The enrichment was at the claimant's expense
3. The enrichment was unjust (recognised "unjust factor" — mistake, failure of consideration, duress, undue influence, etc.)
4. There is no defence available (change of position, estoppel, bona fide purchaser)

**Breach of Fiduciary Duty**

Elements:

1. Fiduciary relationship exists (director, trustee, agent, partner, solicitor-client, or analogous relationship)
2. Scope of the fiduciary duty (loyalty, no-conflict, no-profit, confidentiality)
3. Specific breach — conflict of interest, unauthorised profit, misuse of position, misapplication of property
4. Loss to the claimant or gain to the fiduciary

Pleading requirements:

- Identify the relationship and why it is fiduciary
- Plead the specific duty breached
- Give full particulars of the breach (dates, transactions, amounts)
- For dishonesty allegations: full particulars required (PD 16 para 8.2)

### Tort Claims

**Negligence**

Elements (Caparo Industries plc v Dickman [1990]): [VERIFY]

1. **Duty of care** — established by the three-stage test:
   - (a) Foreseeability of harm
   - (b) Proximity of relationship
   - (c) Fair, just, and reasonable to impose a duty
2. **Breach of duty** — defendant fell below the standard of a reasonable person (or professional — Bolam test)
3. **Causation** — factual ("but for") and legal (not too remote)
4. **Damage** — actual loss (physical injury, property damage, or pure economic loss in limited circumstances)

Pleading requirements:

- Identify the basis of the duty (relationship, assumption of responsibility, statutory)
- Plead the standard of care applicable
- Give particulars of negligence (specific acts/omissions)
- Plead causation — how the negligence caused the specific loss
- Quantify each head of damage

**Professional Negligence**

Additional elements beyond standard negligence:

1. **Retainer / assumption of responsibility** — the professional undertook to provide services
2. **Standard of care** — Bolam v Friern Hospital Management Committee [1957]: standard of a reasonably competent practitioner in the relevant field [VERIFY]
3. **Bolitho qualification** — Bolitho v City and Hackney HA [1998]: the professional practice relied on must withstand logical analysis [VERIFY]
4. **Scope of duty** — what risks the professional assumed responsibility for (SAAMCO / BPE Solicitors v Hughes-Holland [2017] — "scope of duty" principle) [VERIFY]

Pleading requirements:

- Identify the retainer / engagement and its scope
- Identify the relevant professional standards
- Give detailed particulars of each alleged failure
- For solicitors: distinguish between negligent advice and negligent conduct of litigation
- Address scope of duty (what loss falls within the scope of the duty breached)

**Negligent Misstatement**

Elements (Hedley Byrne & Co Ltd v Heller & Partners Ltd [1964]): [VERIFY]

1. Defendant made a statement
2. Defendant assumed responsibility for the accuracy of the statement
3. Claimant reasonably relied on the statement
4. There was sufficient proximity between the parties
5. Statement was inaccurate / negligently made
6. Claimant suffered loss as a result

**Nuisance**

_Private nuisance:_

1. Claimant has an interest in the land affected (owner or occupier with exclusive possession)
2. Defendant's use of their land (or conduct) causes unreasonable interference
3. With the claimant's use or enjoyment of their land
4. The interference is substantial and not merely trivial
5. Foreseeability of the type of harm (Cambridge Water Co v Eastern Counties Leather plc [1994]) [VERIFY]

_Public nuisance (actionable by individual):_

1. Interference with a right common to the public
2. Claimant has suffered particular damage beyond that suffered by the public generally

**Defamation**

Elements (Defamation Act 2013): [VERIFY]

1. **Publication** — defendant published a statement to at least one person other than the claimant
2. **Defamatory meaning** — the statement would tend to lower the claimant in the estimation of right-thinking members of society generally
3. **Reference to the claimant** — the statement refers to the claimant (directly or by inference)
4. **Serious harm** — the publication has caused or is likely to cause serious harm to the reputation of the claimant (s.1(1)); for bodies trading for profit: serious financial loss (s.1(2))

Key defences (must be anticipated in pleading strategy):

- Truth (s.2) — substantial truth of the imputation
- Honest opinion (s.3) — statement of opinion based on fact, honestly held
- Publication on matter of public interest (s.4) — reasonably believed publication was in the public interest
- Absolute privilege — proceedings, judicial etc.
- Qualified privilege — various categories
- Website operator defence (s.5)

**Passing Off**

Elements (Reckitt & Colman Products Ltd v Borden Inc [1990] — the "Jif Lemon" case): [VERIFY]

1. **Goodwill** — claimant has goodwill associated with the goods/services/get-up
2. **Misrepresentation** — defendant's actions amount to a misrepresentation (intentional or unintentional) leading the public to believe the defendant's goods/services are those of the claimant
3. **Damage** — the misrepresentation causes (or is likely to cause) damage to the claimant's goodwill

### Equitable Claims

**Breach of Confidence / Misuse of Private Information**

_Breach of confidence (traditional):_

1. Information has the necessary quality of confidence
2. Information was imparted in circumstances importing an obligation of confidence
3. Unauthorised use of the information to the detriment of the confider

_Misuse of private information (post-Campbell v MGN [2004]):_ [VERIFY]

1. Claimant had a reasonable expectation of privacy in respect of the information
2. Defendant's use/publication of the information was not justified (balancing Article 8 (privacy) against Article 10 (expression))

**Dishonest Assistance / Knowing Receipt**

_Dishonest assistance (Royal Brunei Airlines v Tan [1995]):_ [VERIFY]

1. A trust or fiduciary relationship exists
2. There was a breach of trust/fiduciary duty by the trustee/fiduciary
3. The defendant assisted in the breach
4. The defendant acted dishonestly (objective standard: Ivey v Genting Casinos [2017]) [VERIFY]

_Knowing receipt (BCCI v Akindele [2001]):_ [VERIFY]

1. Disposal of trust assets in breach of trust/fiduciary duty
2. Beneficial receipt by the defendant of assets traceable to the breach
3. Such knowledge that makes it unconscionable for the defendant to retain the benefit

### Employment Claims (Common Law)

**Wrongful Dismissal**

Elements:

1. Contract of employment existed
2. Employer terminated the contract
3. Termination was in breach of contract (e.g., without proper notice, in breach of contractual disciplinary procedure)
4. Claimant suffered loss (limited to notice period — damages generally capped)

Note: Unfair dismissal is a statutory right (Employment Rights Act 1996) pursued in the Employment Tribunal, not the civil courts. This skill covers wrongful dismissal (common law breach of contract) in the civil courts.

### Commercial / Economic Torts

**Conspiracy**

_Lawful means conspiracy (Crofter Hand Woven Harris Tweed Co v Veitch [1942]):_ [VERIFY]

1. Combination or agreement between two or more persons
2. To take action which is lawful in itself
3. With the predominant purpose of injuring the claimant
4. Which does cause the claimant damage

_Unlawful means conspiracy (Total Network SL v HMRC [2008]):_ [VERIFY]

1. Combination or agreement between two or more persons
2. To use unlawful means
3. With the intention of injuring the claimant (need not be predominant purpose)
4. Which does cause the claimant damage

**Inducing Breach of Contract**

Elements (OBG Ltd v Allan [2007]): [VERIFY]

1. A valid and enforceable contract exists between the claimant and a third party
2. The defendant knew of the contract
3. The defendant intended to procure a breach of the contract
4. The defendant did procure the breach (by persuasion, inducement, or procurement)
5. The claimant suffered damage as a result

**Causing Loss by Unlawful Means**

Elements (OBG Ltd v Allan [2007]): [VERIFY]

1. The defendant used unlawful means against a third party
2. The unlawful means interfered with the third party's freedom to deal with the claimant
3. The defendant intended to cause loss to the claimant
4. The claimant suffered loss as a result

---

## Pre-Action Protocol — Detailed Reference

<!-- PLACEHOLDER: Will be enriched with research from pre-action agent -->

### Practice Direction — Pre-Action Conduct and Protocols (General)

**Objectives of pre-action conduct:**

1. Enable parties to settle without litigation
2. Support efficient management of proceedings if litigation is necessary
3. Encourage exchange of early and full information
4. Enable parties to avoid litigation by agreeing a resolution

**General steps required (where no specific protocol applies):**

1. Claimant sends a letter of claim setting out:
   - The basis for the claim (a brief summary of facts)
   - What the claimant wants from the defendant
   - The financial value (if a money claim)
2. Defendant responds within a reasonable period (typically 14 days for acknowledgment, then a full response within a period proportionate to the claim)
3. Both parties consider whether ADR is appropriate and, if so, engage with it
4. Both parties disclose key documents relevant to the issues

### Key Specific Protocols

**Personal Injury Protocol:**

| Step            | Requirement                                                                  | Timeline           |
| --------------- | ---------------------------------------------------------------------------- | ------------------ |
| Letter of Claim | Summary of facts, nature of injuries, rehabilitation needs, financial losses | Before proceedings |
| Acknowledgment  | Insurer acknowledges receipt and gives preliminary response                  | Within 21 days     |
| Full Response   | Accept/deny with reasons, identify disputed facts, any counterclaim          | Within 3 months    |

- If NO reply within 21 days, claimant entitled to issue proceedings
- Medical report required — for soft tissue/whiplash injuries, must be fixed-cost report via MedCo Portal
- Rehabilitation: parties should consider rehabilitation needs at earliest opportunity

**Professional Negligence Protocol:**

| Step                     | Requirement                                                                                    | Timeline                       |
| ------------------------ | ---------------------------------------------------------------------------------------------- | ------------------------------ |
| Preliminary Notice       | Brief notification identifying claimant, professional, outline of grievance, approximate value | As soon as reasonable          |
| Acknowledgment of Notice | Professional acknowledges receipt                                                              | Within 21 days                 |
| Letter of Claim          | Full identities, detailed events/dates, allegations, breakdown of damages, key documents       | After preliminary notice stage |
| Acknowledgment of Claim  | Formal acknowledgment                                                                          | Within 21 days                 |
| Letter of Response       | Written response to EVERY claim/allegation; accept or deny with supporting evidence            | Within 3 months                |

- Extension requests: professional should explain difficulty before deadline and propose reasonable date
- Consider joint expert evidence

**Clinical Disputes Protocol:**

| Step                              | Requirement                                                                     | Timeline                               |
| --------------------------------- | ------------------------------------------------------------------------------- | -------------------------------------- |
| Letter of Notification (optional) | Advises healthcare provider that a Letter of Claim is likely                    | Acknowledge within 14 days             |
| Medical Records Request           | Standard form request for clinical records                                      | Disclosed within 40 days               |
| Letter of Claim                   | Detailed claim; if against NHS Trust, copy must also go to NHSLA/NHS Resolution | As soon as practicable                 |
| Letter of Response                | Full written response                                                           | 14 days (simple) to 4 months (complex) |

- Healthcare providers should involve NHSLA / defence organisations / insurers at early stage

**Construction and Engineering Protocol:**

| Step               | Requirement                                                                                                                                          | Timeline                  |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| Letter of Claim    | Basis of claim, factual background, contractual/statutory provisions, remedy sought, whether Protocol Referee Procedure proposed, identified experts | Before proceedings        |
| Acknowledgment     | Written acknowledgment, insurer notification, agreement to Protocol Referee Procedure                                                                | Within 14 days            |
| Letter of Response | Full response to all allegations                                                                                                                     | Within 28 days            |
| Pre-Action Meeting | **Mandatory** without prejudice meeting before litigation                                                                                            | After exchange of letters |

- **Unique mandatory pre-action meeting** — everything said treated as "without prejudice"
- Scott Schedule may be required for itemised claims/defects (tabular format: item, description, amount, response)

**Debt Claims Protocol:**

| Step            | Requirement                                                                                                                              | Timeline                       |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| Letter of Claim | Amount owed, interest/charges, how to pay, statement of account, contract details, information sheet with free debt advice organisations | Sent before proceedings        |
| Response        | Reply form returned or no response                                                                                                       | 30 days minimum before issuing |

- Must include regulatory information sheet with free debt advice organisations
- Court focuses on **substantive** compliance, not minor/technical breaches

**Media and Communications Protocol (Defamation/Privacy):**

| Step               | Requirement                                                                                                                                  | Timeline           |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Letter of Claim    | Specific publication, statement complained of, copy/transcript, imputation contended, factual inaccuracies, jurisdiction basis (s.9 DA 2013) | Before proceedings |
| Letter of Response | Full response                                                                                                                                | Within 14 days     |

- **1-year limitation** for defamation and malicious falsehood — protocol must be completed quickly
- Must address jurisdiction if any international element (s.9 Defamation Act 2013)

**Judicial Review Protocol:**

| Step                | Requirement                                                                        | Timeline                       |
| ------------------- | ---------------------------------------------------------------------------------- | ------------------------------ |
| Letter Before Claim | Decision/matter challenged, claimant details, grounds of challenge, legal advisers | Promptly, well within 3 months |
| Letter of Response  | Full response from public body                                                     | Within 14 days                 |

- Urgency exception: in very urgent cases, claim should be made immediately without protocol

### ADR Requirements

Courts expect parties to have considered ADR before issuing proceedings.

**Halsey v Milton Keynes General NHS Trust [2004]:** [VERIFY]

- Unreasonable refusal to engage in ADR can result in adverse costs consequences
- Court considers: nature of the dispute, merits of mediation, whether ADR was attempted, costs of mediation relative to litigation costs

**Churchill v Merthyr Tydfil County Borough Council [2023] EWCA Civ 1416:** [VERIFY]

- **Landmark decision** overturning key aspect of Halsey
- Court of Appeal held courts CAN stay proceedings and **order parties to engage in ADR**, even where parties are unwilling
- Lord Justice Dyson's statement in Halsey about compulsion being an "unacceptable obstruction" was **not binding** — obiter dictum
- Power is lawful provided it: (a) does not impair the "very essence" of the right to a judicial hearing, and (b) is proportionate to achieving the legitimate aim of settling disputes fairly, quickly, and at reasonable cost
- Relevant factors: form of ADR, legal representation, urgency, cost of ADR, imbalance between parties
- **Post-Churchill CPR amendments (October 2024):** Emphasise court's power to mandate ADR [VERIFY]

**PGF II SA v OMFS Company 1 Ltd [2013] EWCA Civ 1288:** [VERIFY]

- **Silence** in the face of a proposal to mediate is itself unreasonable
- A party must engage with the ADR proposal, even if to refuse with reasons
- Distinguished from actively refusing with articulated reasons

**Types of ADR to consider:**

- Mediation (most common)
- Early neutral evaluation
- Expert determination
- Ombudsman schemes (where applicable)
- Negotiation (with or without Part 36 offer)

### Part 36 Offers — Pre-Action Strategy

Part 36 offers can be made **before proceedings are issued** and carry significant costs consequences:

- If defendant makes a pre-action Part 36 offer and claimant fails to beat it at trial: claimant pays defendant's costs from expiry of relevant period
- If claimant makes a pre-action Part 36 offer and obtains a judgment at least as advantageous: enhanced interest (up to 10% above base rate), indemnity costs, and additional amount (up to £75,000) [VERIFY]

**Strategic consideration:** Always advise on Part 36 offers before issuing proceedings.

---

## Strike-Out and Survival — CPR 3.4 and Part 24 Reference

<!-- PLACEHOLDER: Will be enriched with research from strike-out agent -->

### Strike-Out (CPR 3.4(2))

The court may strike out a statement of case if it appears that:

**(a) No reasonable grounds for bringing or defending the claim**

- The statement of case discloses no reasonable cause of action
- Applies to both claims and defences
- Test: assuming all facts pleaded are true, does the statement of case disclose a legally recognisable claim?
- Lower bar than US Twombly/Iqbal plausibility — only requires "reasonable grounds"

**(b) Abuse of the court's process or otherwise likely to obstruct the just disposal of the proceedings**

- Frivolous or vexatious claims
- Claims brought for an improper collateral purpose
- Re-litigation of issues already decided (res judicata / Henderson v Henderson [1843] abuse of process) [VERIFY]
- **Henderson v Henderson rule**: A party is expected to raise all matters that could and should have been raised in earlier proceedings. Failure to do so in subsequent proceedings constitutes abuse. The court applies a broad-brush approach balancing private and public interests.
- Duplicative proceedings or "warehousing" claims (deliberately delaying prosecution)

**(c) Failure to comply with a rule, practice direction, or court order**

- Non-compliance with unless orders
- Failure to file/serve documents on time
- Mitchell v News Group Newspapers Ltd [2013] / Denton v TH White Ltd [2014] — relief from sanctions three-stage test: (1) was the breach serious or significant? (2) is there a good reason for it? (3) all the circumstances including need for litigation to be conducted efficiently, compliance with rules/PDs/orders, and enforcement [VERIFY]

**(d) SLAPP claims (from 18 June 2025)** [VERIFY]

- Civil Procedure (Amendment) Rules 2025 added a new SLAPP ground under s.195 of the Economic Crime and Corporate Transparency Act 2023
- Court may strike out if: (1) the claim is a "SLAPP claim" AND (2) the claimant fails to show it is more likely than not the claim would succeed at trial
- **Higher burden on claimant** than standard strike-out — must demonstrate probable success
- Targets claims designed to suppress speech on matters of public interest

### Summary Judgment (CPR Part 24)

**Test (CPR 24.2):** The court may give summary judgment if:

1. The claimant/defendant has **no real prospect of succeeding/successfully defending** the claim or issue; AND
2. There is **no other compelling reason** why the case should be disposed of at a trial

**Key principles (Easyair Ltd v Opal Telecom Ltd [2009], Lewison J):** [VERIFY]

1. Court must consider whether the claim has a **"realistic" as opposed to "fanciful"** prospect of success — "realistic" means carrying some degree of conviction, more than merely arguable
2. Court must **not conduct a "mini-trial"**
3. Court should not take everything a party says at face value without analysis
4. Court should take into account evidence that can reasonably be expected to be available at trial
5. Court should **hesitate** about making a final decision without a trial where reasonable grounds exist for believing a fuller investigation of facts would add to or alter the evidence
6. Where there is a short point of law or construction, court should decide it if confident it has all the evidence necessary

**Swain v Hillman [2001] — foundational authority:** [VERIFY]

- "No real prospect of success" does not need amplification — speaks for itself
- The word "real" distinguishes fanciful prospects of success
- If there is a real prospect, summary judgment **does not arise** merely because success is improbable

### Part 18 Requests for Further Information

- Either party may request clarification or additional information about any matter in a statement of case (CPR 18.1)
- Request must be concise and proportionate
- Court can order a party to provide further information
- Analogous to US Rule 12(e) motion for more definite statement
- If response inadequate: may support strike-out application

### Amendment of Statements of Case (CPR Part 17)

| Timing                                           | Permission Required?                                                                            | Key Rule      |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------- | ------------- |
| Before service                                   | No permission needed                                                                            | CPR 17.1(1)   |
| After service, before case management conference | With consent of all parties or court permission                                                 | CPR 17.1(2)   |
| After limitation expired                         | Court permission; must be a "new claim arising out of the same or substantially the same facts" | CPR 17.4      |
| Adding/substituting parties                      | Court permission under CPR Part 19                                                              | CPR 19.4-19.5 |

**Limitation and amendment:**

- CPR 17.4 implements s.35 Limitation Act 1980 [VERIFY]
- New claim after limitation: only permitted if it arises out of "the same facts or substantially the same facts" as already pleaded
- Adding a new party after limitation: only if the new party is necessary for determination of the original claim and the mistake was genuine
- **Relation-back doctrine**: The amended claim is deemed to have been commenced on the date of the original claim form, so limitation is assessed by reference to that date

### Key Differences from US Pleading

| Feature                        | US Federal (Post-Twombly/Iqbal)                                     | England & Wales (CPR)                                                                |
| ------------------------------ | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Pleading standard**          | "Plausibility" — claims must be plausible on their face             | "Reasonable grounds" — facts assumed true; lower bar                                 |
| **Judicial analysis**          | Court disregards "conclusory" allegations, assesses plausibility    | Court assesses on face; must be **certain** no reasonable grounds                    |
| **Fraud specificity**          | Rule 9(b) — who, what, when, where, how                             | PD 16 para 8.2 — must be "specifically set out" (similar function, different source) |
| **Costs**                      | American Rule — each side bears own costs (absent statute/contract) | Loser-pays — unsuccessful party pays successful party's costs                        |
| **Pre-suit discovery**         | Available in limited circumstances                                  | No right to pre-action disclosure (except CPR 31.16, Norwich Pharmacal)              |
| **Discovery scope**            | Extensive (interrogatories, depositions, document requests)         | Narrower — standard or issues-based disclosure                                       |
| **Pre-suit requirements**      | Limited (EEOC, tort claims acts)                                    | Extensive pre-action protocols; costs sanctions for non-compliance                   |
| **Heightened pleading**        | Rule 9(b) fraud; PSLRA securities                                   | PD 16 para 8.2 fraud/dishonesty; no securities equivalent                            |
| **Amendment after limitation** | Rule 15(c) relation-back; generous                                  | CPR 17.4 — "same or substantially same facts" only                                   |
| **Group litigation**           | Rule 23 class action (opt-out)                                      | GLO (opt-in), representative action (opt-out), CAT collective (competition only)     |

---

## Court Structure and Allocation Reference

<!-- PLACEHOLDER: Will be enriched with research from courts-remedies agent -->

### Business and Property Courts (B&PCs)

Launched July 2017, the B&PCs umbrella encompasses specialist jurisdictions
from both KBD and Chancery. B&PCs sit in London (Rolls Building) and district
registries (Birmingham, Bristol, Cardiff, Leeds, Liverpool, Manchester, Newcastle).

Lists within B&PCs:

- Admiralty Court, Commercial Court, TCC
- Business List, Companies and Insolvency List, Competition List
- Financial List, IP List (Patents Court + IPEC)
- Revenue List, Property/Trusts/Probate List

### Court Selection Guide

| Claim Type                             | Preferred Court                                               |
| -------------------------------------- | ------------------------------------------------------------- |
| Money claims up to £100,000            | County Court                                                  |
| Personal injury up to £50,000          | County Court                                                  |
| Money claims over £100,000             | High Court (KBD)                                              |
| Personal injury over £50,000           | High Court (KBD)                                              |
| Company / partnership / trusts         | High Court (Chancery) or County Court (equity up to £350,000) |
| Intellectual property (up to £500,000) | IPEC (capped costs regime)                                    |
| Intellectual property (high value)     | Patents Court / High Court (Chancery)                         |
| Construction / engineering disputes    | TCC                                                           |
| International commercial disputes      | Commercial Court                                              |
| Shipping / admiralty                   | Admiralty Court                                               |
| Revenue / tax                          | High Court (KBD)                                              |
| Freezing / search orders               | High Court                                                    |
| Financial services / markets           | Financial List                                                |

### Post-Brexit Jurisdiction Position

**Brussels Regulation (Recast):** No longer applies from 1 January 2021. Retained EU law provisions revoked.

**Lugano Convention 2007:** UK applied to accede independently; application **rejected** (EU objected). Not in force for UK. [VERIFY]

**Hague Choice of Court Convention 2005:** UK acceded independently (effective 1 January 2021). Applies to **exclusive** choice of court agreements concluded after 1 October 2015. Provides for mutual recognition and enforcement. [VERIFY]

**Practical effect:**

- Common law rules now govern most international jurisdiction questions
- CPR Part 6 / PD 6B gateways are the primary mechanism for service out of jurisdiction
- Forum non conveniens doctrine (Spiliada) fully revived (was largely displaced under Brussels regime)
- Anti-suit injunctions no longer constrained by EU law (cf. Turner v Grovit) [VERIFY]
- Enforcement of EU member state judgments now requires common law or bilateral treaties

### Limitation Periods Quick Reference

| Claim Type                         | Period                                   | Statute           | Notes                                                                                      |
| ---------------------------------- | ---------------------------------------- | ----------------- | ------------------------------------------------------------------------------------------ |
| Simple contract                    | 6 years                                  | LA 1980 s.5       | From date of breach                                                                        |
| Contract by deed                   | 12 years                                 | LA 1980 s.8       | From date of breach [VERIFY]                                                               |
| Tort (general)                     | 6 years                                  | LA 1980 s.2       | From date damage occurs                                                                    |
| Personal injury                    | 3 years                                  | LA 1980 s.11      | From date of injury or date of knowledge (s.14); court discretion to override (s.33)       |
| Fatal accident                     | 3 years                                  | LA 1980 s.12      | From date of death or personal representative's knowledge                                  |
| Latent damage                      | 3 years from knowledge; 15-year longstop | LA 1980 s.14A-14B | From date claimant knew/should have known of damage [VERIFY]                               |
| Defamation / malicious falsehood   | 1 year                                   | LA 1980 s.4A      | With court discretion to extend (s.32A) [VERIFY]                                           |
| Contribution (between tortfeasors) | 2 years                                  | LA 1980 s.10      | From date of judgment or settlement [VERIFY]                                               |
| Fraud / concealment                | No fixed period                          | LA 1980 s.32      | Time runs from when fraud/concealment could with reasonable diligence have been discovered |
| Consumer protection                | Various                                  | CRA 2015          | Depends on the right exercised [VERIFY]                                                    |

---

## Classification System

Each element assessment is classified:

| Classification | Definition                                                                                                              | Confidence Threshold | Action                                             |
| -------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------- | -------------------------------------------------- |
| **WELL-PLED**  | Element fully supported by specific factual allegations in proper form                                                  | ≥ 0.80               | No changes needed                                  |
| **ADEQUATE**   | Element pled with sufficient facts but could be strengthened                                                            | ≥ 0.60               | Suggest strengthening language                     |
| **VULNERABLE** | Element pled but insufficiently particularised; may not survive strike-out or Part 18 request                           | ≥ 0.80               | Provide rewrite with fuller particulars            |
| **DEFICIENT**  | Element missing, inadequately pleaded, or statement of case contains impermissible content (evidence, law, conclusions) | ≥ 0.90               | Must rewrite or recommend omitting cause of action |

**Classification decision rules:**

- DEFICIENT: Missing element, pleading evidence rather than facts, or clear failure to provide required particulars (e.g., fraud without PD 16 para 8.2 compliance) — confidence ≥ 0.90
- VULNERABLE: Element pled but with insufficient specificity; likely to attract Part 18 request or risk strike-out — confidence ≥ 0.80
- ADEQUATE: Element pled with basic facts but room for improvement — confidence ≥ 0.60
- WELL-PLED: Element fully supported with specific, properly particularised factual allegations — confidence ≥ 0.80

---

## Actionable Output Per Finding

```yaml
finding:
  id: "F-001"
  cause_of_action: "Professional Negligence"
  element: "Standard of care and breach"
  classification: "VULNERABLE"
  confidence: 0.83
  summary: "Particulars of negligence allege the solicitor 'failed to act competently' without specifying what a reasonably competent solicitor would have done differently. Under Bolam, the Particulars must identify the applicable standard and explain how the defendant's conduct fell below it."
  current_text: "The Defendant failed to act with reasonable care and skill in advising the Claimant."
  suggested_fix: |
    The Defendant failed to exercise the care and skill to be expected of a
    reasonably competent solicitor specialising in commercial property
    transactions. In particular, the Defendant:
    (a) failed to advise the Claimant of the existence of restrictive covenants
        affecting the Property, as set out in Entry 3 of the Charges Register
        of Title Number AB12345;
    (b) failed to raise requisitions on title regarding the said restrictive
        covenants before exchange of contracts;
    (c) failed to obtain an indemnity insurance policy to cover the risk of
        enforcement of the said restrictive covenants; and
    (d) failed to advise the Claimant that the intended use of the Property
        for [purpose] would be in breach of the said restrictive covenants.
  priority: "Tier 1 — Must fix before service"
  self_interrogation:
    pass_1: "Professional negligence requires specific particulars of how the standard was breached. Generic 'failed to act competently' will attract a Part 18 request at minimum and risks strike-out."
    pass_2: "Consider whether each particular is supported by evidence or expert opinion. For solicitor negligence, an expert report may not be required (as opposed to medical negligence) but specificity is still essential."
    pass_3: "Scope of duty issue: check whether the alleged failures fall within the scope of the retainer. If the solicitor was only instructed on conveyancing, allegations about investment advice may be outside scope."
```

---

## Prioritisation Framework

### Tier 1 — Must Fix Before Service

- Missing elements for any cause of action
- Particulars failing PD 16 para 8.2 (fraud/dishonesty not fully particularised)
- Missing statement of truth
- Missing statement of value
- Pre-action protocol non-compliance without justification
- Limitation issues (claim out of time without extension argument)
- Pleading evidence or law instead of material facts
- Missing required attachments (medical report in PI, schedule of loss)

### Tier 2 — Should Fix Before Service

- Weak factual support for elements (arguable but thin)
- Inadequate party identification
- Interest calculation incomplete or incorrect
- Formatting non-compliance with practice directions
- Schedule of loss incomplete or inadequately particularised
- Failure to anticipate obvious defences
- Missing heads of damage that should be claimed

### Tier 3 — Consider Improving

- Narrative organisation and clarity
- Strategic claim ordering
- Additional causes of action that could be included
- Strengthening language for merits-strong claims
- Part 36 strategy advice
- Costs implications of claim structure

---

## Citation Quality Gates

| Gate           | Rule                                                                                             | Fail Action                              |
| -------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| **Source**     | Every element assessment cites specific paragraph of Particulars and factual basis               | Add citation or mark `[CITATION NEEDED]` |
| **Format**     | Case and statute citations use correct neutral citation format (e.g., [2023] UKSC 1)             | Normalise format                         |
| **Currency**   | Legal authority is current (not overruled, superseded by statute, or distinguished on the facts) | Add `[VERIFY CURRENCY]`                  |
| **Domain**     | Legal principles are English law, not imported from other jurisdictions                          | Remove jurisdiction bleed                |
| **Confidence** | Confidence score aligns with classification threshold                                            | Downgrade if below threshold             |

---

## Self-Interrogation (For VULNERABLE and DEFICIENT Findings)

**Pass 1 — Element Accuracy**
Is this actually a required element under English law? Has the law been
modified by statute (e.g., Defamation Act 2013 changing the serious harm
threshold)? Are there alternative formulations of the cause of action that
avoid this problematic element?

**Pass 2 — Factual Sufficiency**
Is the allegation truly insufficiently particularised, or would it survive a
strike-out application given the courts' general approach of reading statements
of case generously? Would further and better particulars (Part 18) cure the
deficiency rather than requiring a full amendment?

**Pass 3 — Strategic Alternative**
If this element cannot be adequately pled, is there an alternative cause of
action that captures the same conduct? Would amendment be available later
when more evidence is obtained through disclosure? Should the cause of action
be omitted to avoid adverse costs consequences?

---

## Confidence Scoring

| Level        | Range     | Interpretation                                                   | Action                        |
| ------------ | --------- | ---------------------------------------------------------------- | ----------------------------- |
| **Definite** | 0.95-1.00 | Element clearly and specifically pled with proper particulars    | No action needed              |
| **High**     | 0.80-0.94 | Element well-pled; minor improvements possible                   | Report with brief caveat      |
| **Probable** | 0.60-0.79 | Element pled but some vulnerability; may attract Part 18 request | Note vulnerability            |
| **Possible** | 0.40-0.59 | Element weakly pled; risk of strike-out or summary judgment      | Flag for counsel review       |
| **Unlikely** | 0.00-0.39 | Element not adequately pled; cause of action likely fails        | Recommend rewrite or omission |

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-complaint-drafter-ew"
  skill_version: "1.0"
  topic: "England & Wales statement of case drafting"
  timestamp: "[ISO 8601]"
  jurisdiction: "England & Wales"
  procedural_framework: "Civil Procedure Rules 1998"
  inputs:
    client_instructions: "[summary of instructions received]"
    documents_reviewed:
      - "[document 1 — type and date]"
      - "[document 2 — type and date]"
    pre_action_status: "[protocol compliance status]"
  clarifications:
    - question: "[CLARIFY question]"
      answer: "[user response or default applied]"
      impact: "[how this affected the analysis]"
  court_selection:
    court: "[County Court at X / High Court KBD / etc.]"
    track: "[small claims / fast / intermediate / multi-track]"
    rationale: "[why this court and track were selected]"
  causes_of_action_considered:
    - claim: "[cause of action 1]"
      included: true
      elements_count: X
      elements_satisfied: Y
      classification: "[WELL-PLED / ADEQUATE / VULNERABLE / DEFICIENT]"
      confidence: 0.XX
      notes: "[key observations]"
    - claim: "[cause of action 2]"
      included: false
      exclusion_reason: "[limitation expired / insufficient facts / costs disproportionate]"
  pre_action_protocol:
    applicable_protocol: "[protocol name]"
    compliance_status: "[compliant / partially compliant / non-compliant]"
    deficiencies: "[if any]"
  limitation_analysis:
    - claim: "[cause of action]"
      limitation_period: "[X years under s.Y LA 1980]"
      accrual_date: "[date]"
      expiry_date: "[date]"
      status: "[within time / approaching / expired / extended under s.32/33]"
  findings:
    total: X
    by_classification:
      WELL-PLED: X
      ADEQUATE: X
      VULNERABLE: X
      DEFICIENT: X
    tier_1_issues: X
  costs_analysis:
    estimated_court_fee: "£[amount]"
    track_costs_implications: "[fixed costs / costs budgeting / etc.]"
    part_36_recommendation: "[yes/no and proposed amount]"
  model: "[model identifier]"
  tools_used:
    - "[tool 1]"
    - "[tool 2]"
  caveats:
    - "[caveat 1]"
    - "[caveat 2]"
  verify_flags:
    - item: "[unverified assertion]"
      source_needed: "[what source would verify this]"
```

---

## Remedies and Relief — Detailed Reference

### Damages

**General (non-pecuniary) damages:**

- Pain, suffering, and loss of amenity (PSLA) — assessed by reference to Judicial College Guidelines [VERIFY]
- Loss of congenial employment
- Diminution in quality of life
- For defamation: injury to reputation

**Special (pecuniary) damages:**

- Past and future loss of earnings (multiplier/multiplicand method for future losses — Ogden Tables) [VERIFY]
- Medical and care expenses
- Property damage
- Wasted expenditure (in alternative to loss of bargain for contract claims)

**Aggravated damages:**

- Additional compensation for injury to feelings, dignity, or pride caused by the manner of the defendant's conduct
- Must be specifically pleaded with grounds stated (CPR 16.4(1)(c))
- Available in tort (especially trespass, defamation, false imprisonment)
- Not generally available for breach of contract [VERIFY]

**Exemplary damages:**

Available only in limited categories (Rookes v Barnard [1964]): [VERIFY]

1. Oppressive, arbitrary, or unconstitutional action by government servants
2. Defendant calculated that their conduct would make a profit exceeding any compensation payable
3. Where expressly authorised by statute

Must be specifically pleaded with grounds stated (CPR 16.4(1)(c)).

### Equitable Remedies

**Injunctions:**

- Prohibitory (restraining the defendant from doing something)
- Mandatory (requiring the defendant to take positive action)
- Interim/interlocutory (pending trial — American Cyanamid Co v Ethicon Ltd [1975] test) [VERIFY]:
  1. Is there a serious question to be tried?
  2. Would damages be an adequate remedy for the claimant?
  3. If not, would the cross-undertaking in damages adequately protect the defendant?
  4. Balance of convenience

**Freezing orders (formerly Mareva injunctions):**

- Prevents the defendant from dissipating assets before judgment
- Worldwide freezing orders available
- Requires: good arguable case, risk of dissipation, full and frank disclosure by applicant
- Made without notice (ex parte) — urgency required

**Search orders (formerly Anton Piller orders):**

- Permits entry to defendant's premises to search for and preserve evidence
- Requires: extremely strong prima facie case, very serious actual or potential damage, clear evidence defendant has relevant documents, real risk of destruction

**Specific performance:**

- Discretionary remedy compelling performance of a contractual obligation
- Generally available for land contracts
- Not available where damages are adequate, supervision would be impractical, or contract is for personal services
- Must show damages would not be an adequate remedy

**Rescission:**

- Setting aside a contract (e.g., for misrepresentation)
- Bars: affirmation, lapse of time, third party rights, impossibility of restitutio in integrum

**Account of profits:**

- Alternative to damages in IP and breach of fiduciary duty claims
- Requires the defendant to account for profits made from the wrongful conduct

### Interest

**Statutory basis:**

- Senior Courts Act 1981 s.35A (High Court)
- County Courts Act 1984 s.69 (County Court)
- Discretionary: court can award interest at "such rate as it thinks fit" for "such period as it thinks fit"
- Conventional rate: typically 1-2% above base rate for commercial claims [VERIFY]

**Contractual interest:**

- If contract provides for interest, that rate applies
- Late Payment of Commercial Debts (Interest) Act 1998: 8% above base rate for qualifying commercial debts [VERIFY]

**Late payment interest on damages:**

- From date of accrual of cause of action to date of judgment
- Must be specifically claimed in Particulars (CPR 16.4(2))

### Costs

**General rule (CPR 44.2(2)):** The unsuccessful party pays the successful party's costs.

**Types of costs assessment:**

- Standard basis: reasonable and proportionate
- Indemnity basis: reasonable (proportionality not considered) — awarded for unreasonable conduct or as Part 36 consequence

**Qualified One-Way Costs Shifting (QOCS) — PI claims:**

- Claimant's costs liability limited to the amount of damages and interest awarded
- Does not apply if claim is struck out as having no reasonable grounds or is an abuse of process, or if fundamental dishonesty found

**Part 36 consequences:**

- Claimant fails to beat defendant's offer: defendant's costs from end of relevant period
- Judgment at least as advantageous as claimant's offer: enhanced interest (up to 10% above base), indemnity costs, additional amount (up to £75,000)

---

## Group Litigation Reference

### Group Litigation Orders (GLOs) — CPR Part 19, Section III

- **Opt-in mechanism**: Claimants must individually apply to join a group register
- Court-managed: a managing judge is assigned and gives case management directions
- Common issues identified and tried as lead cases or "generic" issues
- Individual issues (quantum, causation) tried separately
- Common uses: product liability, institutional abuse, environmental, taxation, employment-related PI
- Costs: individual claimants generally liable for share of common costs plus own individual costs

### Representative Actions — CPR 19.8

- **Opt-out mechanism**: Action proceeds on behalf of all in defined class unless they opt out
- Strict "same interest" requirement historically limited use
- Lloyd v Google [2021] UKSC 50: confirmed representative actions can be used for bifurcated proceedings (common issues first, individual issues later) [VERIFY]

### Competition Act Collective Proceedings — s.47B

- Before the Competition Appeal Tribunal (CAT), not ordinary courts
- **Opt-out** for UK-domiciled class members
- Available for infringements of UK competition law
- Requires Collective Proceedings Order (CPO) certification
- Merricks v Mastercard [2025]: first opt-out collective settlement (£200m, 44 million consumers) [VERIFY]

### Comparison with US Class Actions

| Feature       | US Rule 23              | E&W GLO                           | E&W Rep. Action         | CAT Collective      |
| ------------- | ----------------------- | --------------------------------- | ----------------------- | ------------------- |
| Mechanism     | Opt-out                 | Opt-in                            | Opt-out                 | Opt-out             |
| Certification | Class certification     | GLO application                   | No formal certification | CPO required        |
| Damages       | Individual or aggregate | Individual                        | Limited historically    | Aggregate possible  |
| Funding       | Contingency fees        | ATE insurance, litigation funding | Litigation funding      | Third-party funding |
| Scope         | All civil claims        | All civil claims                  | All civil claims        | Competition only    |

---

## Common Weaknesses by Statement of Case Type

### Contract Claims

- **Failing to identify the contract**: Not attaching written agreement or identifying oral contract with sufficient specificity (who, when, where, what words)
- **Vague breach allegations**: "The Defendant breached the contract" without specifying which terms were breached and how
- **Ignoring implied terms**: Not pleading implied terms under SGA 1979, CRA 2015, or SGSA 1982 where they strengthen the claim
- **Remoteness gap**: Claiming consequential losses without pleading that they were within the reasonable contemplation of the parties at the time of contracting (Hadley v Baxendale)
- **Wrong statute for consumer claims**: Citing SGA 1979 for consumer contracts entered after 1 October 2015 (should be CRA 2015)

### Professional Negligence Claims

- **Generic negligence allegation**: "Failed to exercise reasonable care and skill" without particularising what a competent professional would have done
- **Missing Bolam/Bolitho framework**: Not identifying the relevant professional standard or why defendant's conduct fell below it
- **Scope of duty confusion**: Claiming losses outside the scope of the professional's retainer (SAAMCO/BPE Solicitors principle) [VERIFY]
- **Missing expert evidence**: Professional negligence typically requires expert evidence to establish the standard — claim may be struck out without it
- **Loss of chance not pleaded**: Where negligence caused loss of a chance (e.g., solicitor missing limitation), must plead and quantify the lost chance

### Fraud Claims

- **Bare dishonesty allegation**: "The Defendant acted fraudulently" without particularising the primary facts from which fraud is inferred — guaranteed strike-out target
- **Wrong type of misrepresentation**: Pleading fraud (PD 16 para 8.2 specificity required) when negligent misrepresentation under s.2(1) Misrepresentation Act 1967 achieves the same result with reversed burden and without needing to prove dishonesty
- **No inference of dishonesty**: Primary facts pleaded must make dishonesty more likely than innocence or negligence (Three Rivers v Bank of England) [VERIFY]
- **Corporate fraud without attribution**: Not identifying whose state of mind is attributed to the corporate defendant

### Personal Injury Claims

- **Missing medical report**: PD 16 para 4 requires attachment — statement of case defective without it
- **No schedule of loss**: Must attach schedule of past and future expenses and losses
- **Limitation not checked**: 3-year period with date of knowledge complications — must be verified before issuing
- **QOCS assumptions**: Assuming QOCS protection is absolute — can be lost for fundamental dishonesty or abuse of process

### Defamation Claims

- **No serious harm**: Post-Lachaux, must plead specific evidence of serious harm to reputation — mere assertion of defamatory meaning is insufficient [VERIFY]
- **Missing words complained of**: Must set out the exact words verbatim
- **No meaning pleaded**: Must specify the defamatory meaning attributed to the words
- **Limitation exposure**: 1-year period — shortest in English civil law; protocol must be completed quickly

---

## Anti-Patterns

### Drafting Anti-Patterns

1. **Pleading evidence, not facts** — "Mr Smith will say that he saw the accident" vs. "On 15 January 2025, at approximately 2:00 pm, the Defendant's vehicle struck the Claimant's vehicle" — plead facts, not what witnesses will say
2. **Pleading law, not facts** — "The Defendant owed a duty of care pursuant to the principles in Caparo v Dickman" — state the facts from which the duty arises; legal analysis is for skeleton arguments
3. **Excessive prolixity** — English courts expect concise statements of case; lengthy, repetitive pleadings may be struck out or attract costs sanctions
4. **Conclusory allegations without particulars** — "The Defendant acted fraudulently" without specifying the who, what, when, where, and how of the fraud
5. **Missing statement of truth** — Renders the statement of case unenforceable as evidence and risks strike-out
6. **Shotgun pleading** — Incorporating all preceding paragraphs into every cause of action without discrimination
7. **Inflammatory or emotive language** — Undermines credibility; courts expect measured, factual language
8. **Failing to plead specific loss** — "The Claimant suffered loss and damage" without quantification or particularisation

### Procedural Anti-Patterns

9. **Skipping pre-action protocol** — Costs sanctions, possible stay of proceedings; courts take non-compliance seriously
10. **Wrong court or track** — Issuing in the High Court when the claim should be in County Court (or vice versa)
11. **Missing or incorrect statement of value** — Affects track allocation, court fees, and may cause rejection
12. **Service out of time** — Particulars must be served within 14 days of claim form service (or before 4-month claim form deadline)
13. **Wrong claim type** — Using Part 7 when Part 8 is appropriate (or vice versa)

### Strategic Anti-Patterns

14. **Ignoring costs risk** — Loser-pays regime means a weak claim can be catastrophically expensive; every claim should have a costs-benefit analysis
15. **Missing Part 36 opportunity** — Failing to make or advise on Part 36 offers before issuing
16. **Over-claiming** — Claims disproportionate to the evidence, inviting adverse costs orders and damaging credibility
17. **Under-claiming** — Omitting available heads of damage (aggravated damages, interest, specific consequential losses) that need to be claimed to be recovered
18. **Ignoring ADR** — Courts penalise parties who refuse to engage with ADR without good reason
19. **Multiple defendants without attribution** — "The Defendants" without specifying which defendant did what

### Professional Conduct Anti-Patterns

20. **No reasonable basis** — Including causes of action without reasonable basis in law or fact; SRA Code of Conduct violation
21. **Misleading the court** — Allegations contradicted by evidence known to the solicitor
22. **False statement of truth** — Certifying facts that the client has not confirmed or that are known to be untrue — contempt of court
23. **Conflicts of interest** — Acting for multiple claimants with conflicting interests without proper informed consent

---

## Writing Standards

1. **Material facts only**: Plead facts, not evidence and not law. The distinction is fundamental to English pleading.
2. **Numbered paragraphs**: Every allegation in its own numbered paragraph.
3. **Conciseness**: English courts expect brevity. Avoid repetition and verbose language.
4. **Particulars in sub-paragraphs**: Use lettered sub-paragraphs (a), (b), (c) for lists of particulars.
5. **Active voice**: "[The Defendant] failed to advise" not "It was not advised by the Defendant".
6. **Formal register**: Appropriate legal register without being archaic. Avoid unnecessary Latin.
7. **Document references**: Refer to documents by description and date: "the Agreement dated 15 January 2024" not "the contract".
8. **Headings**: Use headings to organise different sections (parties, facts, each cause of action).
9. **Cross-references**: Refer to earlier paragraphs by number: "As set out at paragraph 12 above" or "The matters set out at paragraphs 5-8 above are repeated."
10. **Sterling amounts**: Use the £ symbol and specify amounts clearly: "£250,000" not "250k" or "about a quarter of a million".

---

## External Tool Integration

### legalcode-mcp (Legal Research)

If legalcode-mcp is available, use for:

- Verifying English case law citations and current status
- Checking CPR rule amendments and practice direction updates
- Retrieving limitation period authorities
- Confirming cause of action element formulations

### WebSearch (Live Research)

Use WebSearch to:

- Verify current CPR rules and practice directions (justice.gov.uk)
- Check current court fees (EX50)
- Research pre-action protocol compliance requirements
- Verify case law authority (BAILII, ICLR)
- Check current Judicial College Guidelines brackets for PSLA (PI claims)

### Task Tool (Sub-Agent Delegation)

Use the Task tool for:

- Parallel element research across multiple causes of action
- Pre-action protocol compliance verification
- Limitation period analysis for complex multi-claim cases
- Costs analysis and Part 36 strategy research

### legalcode-damages-calculation (Companion Skill)

Use for structuring the schedule of loss:

- Calculate past and future loss of earnings
- Apply Ogden Tables multipliers/multiplicands
- Assess general damages brackets (JC Guidelines)
- Evaluate interest calculations

### legalcode-complaint-drafter (US Companion)

Cross-reference for:

- Multi-jurisdictional disputes (US and English claims arising from same facts)
- Understanding US procedural requirements where client may need to file in both jurisdictions
- Forum selection analysis

---

## Output Format Template

### Complete Statement of Case Package

The deliverable includes:

1. **Particulars of Claim** — Court-ready formatted document with numbered paragraphs, statement of truth, and required attachments
2. **Claim Form (N1) Information** — Key data for completing Form N1 (parties, statement of value, brief description)
3. **Schedule of Loss and Damage** — Particularised schedule (format depends on claim type)
4. **Pre-Action Protocol Compliance Report** — Assessment of protocol compliance and any deficiencies
5. **Element Mapping Table** — Which facts support which elements for each cause of action
6. **Merits Assessment** — Per-cause-of-action analysis of strike-out and summary judgment risk
7. **Court and Track Allocation Assessment** — Recommended court and anticipated track
8. **Costs Analysis** — Court fees, track costs implications, Part 36 strategy
9. **Strategic Notes** — Claims considered but excluded, anticipated defences, ADR considerations
10. **Glass Box Audit Trail** — Full YAML audit block

### Element Mapping Table

| Cause of Action    | Element         | Factual Basis (¶¶)                            | Classification | Confidence | Notes                                                  |
| ------------------ | --------------- | --------------------------------------------- | -------------- | ---------- | ------------------------------------------------------ |
| Breach of Contract | Valid contract  | ¶¶ 3-5 (Agreement dated 15/01/2024, attached) | WELL-PLED      | 0.95       | Written contract with signatures                       |
| Breach of Contract | Terms relied on | ¶¶ 6-8 (clause 4.1 — delivery obligation)     | WELL-PLED      | 0.92       | Express term, clearly pleaded                          |
| Breach of Contract | Breach          | ¶¶ 9-12 (failure to deliver by 01/03/2024)    | WELL-PLED      | 0.90       | Specific date, specific failure                        |
| Breach of Contract | Loss and damage | ¶¶ 13-14, Schedule                            | ADEQUATE       | 0.72       | Consequential loss needs fuller particularisation      |
| Prof. Negligence   | Breach of duty  | ¶ 20 ("failed to act competently")            | VULNERABLE     | 0.83       | Too generic — needs specific particulars of negligence |

---

## Sub-Agent Architecture (For Complex Multi-Claim Cases)

For Particulars of Claim involving more than 3 causes of action or complex
multi-party disputes, use the Task tool to delegate parallel analysis:

```yaml
sub_agents:
  - agent: "element-checker"
    task: "Verify all elements for [cause of action] are supported by the factual allegations"
    model: "claude-opus-4-5-20251101"

  - agent: "protocol-checker"
    task: "Verify pre-action protocol compliance for [protocol name]"
    model: "claude-sonnet-4-5-20250514"

  - agent: "limitation-checker"
    task: "Run limitation analysis for all causes of action"
    model: "claude-sonnet-4-5-20250514"

  - agent: "costs-analyst"
    task: "Assess costs implications including track allocation, likely costs budget, and Part 36 strategy"
    model: "claude-sonnet-4-5-20250514"

  - agent: "precedent-researcher"
    task: "Research current case law on [specific legal issue]"
    model: "claude-opus-4-5-20251101"
```

**Delegation rules:**

- Delegate when the Particulars involve more than 3 causes of action
- Delegate when multiple pre-action protocols may apply
- Delegate limitation analysis when multiple accrual dates are involved
- Always synthesise sub-agent outputs into a single coherent document
- The orchestrator agent reviews all sub-agent outputs for consistency

---

## Statement of Case Drafting Quick-Start Checklist

Use this checklist for rapid readiness assessment before detailed analysis:

**Phase 1 — Pre-Action Requirements**

- [ ] Applicable pre-action protocol identified
- [ ] Letter of Claim sent in protocol-compliant format
- [ ] Adequate response time allowed (protocol-specific)
- [ ] Letter of Response received (or time expired)
- [ ] Key documents disclosed as required by protocol
- [ ] ADR considered and position documented (Churchill v Merthyr Tydfil)
- [ ] Expert evidence obtained if required by protocol (medical report in PI)
- [ ] Part 36 offer considered

**Phase 2 — Limitation**

- [ ] Limitation period identified for each cause of action
- [ ] Accrual date confirmed
- [ ] If approaching limitation: protective proceedings planned
- [ ] s.32 fraud/concealment extension checked (if applicable)
- [ ] s.33 PI discretionary extension considered (if applicable)
- [ ] s.14A latent damage knowledge date assessed (if applicable)

**Phase 3 — Court and Track**

- [ ] Correct court selected (County Court / High Court / specialist)
- [ ] Anticipated track allocation assessed
- [ ] Court fees calculated (EX50)
- [ ] Statement of value correct for anticipated recovery
- [ ] If High Court: claim exceeds £100,000 (or £50,000 PI)

**Phase 4 — Statement of Case Content**

- [ ] Parties identified with full names, addresses, legal status
- [ ] Factual allegations set out concisely — material facts only
- [ ] No evidence pleaded (what happened, not how you'll prove it)
- [ ] No law pleaded (causes of action identified, not statutes recited)
- [ ] Each cause of action has all elements pled with supporting facts
- [ ] Fraud/dishonesty allegations fully particularised (PD 16 para 8.2)
- [ ] Interest claimed with statutory/contractual basis and calculation
- [ ] Aggravated/exemplary damages specifically pleaded (if claimed)
- [ ] Prayer for relief complete (damages, interest, injunction, costs, further relief)
- [ ] Statement of truth in correct post-2020 wording
- [ ] Appropriate signatory identified

**Phase 5 — Attachments and Schedules**

- [ ] Written contracts/agreements attached (or identified)
- [ ] Medical report attached (PI claims — PD 16 para 4)
- [ ] Schedule of past and future expenses and losses attached (PI claims)
- [ ] Scott Schedule prepared (construction/property disputes)
- [ ] Required documents per PD 16 attached

**Phase 6 — Strategic Review**

- [ ] Costs-benefit analysis performed (loser-pays regime)
- [ ] Each cause of action assessed for strike-out/summary judgment risk
- [ ] Part 36 strategy formulated
- [ ] Anticipated defences considered and addressed where possible
- [ ] Henderson v Henderson check — all related claims included
- [ ] Multiple defendants: conduct attributed to specific defendants
- [ ] Amendment potential preserved (facts support future claims if needed)

---

## Provenance

This skill was created as a Legalcode original synthesis using multi-agent
research methodology, adapted from the England & Wales localization sections
of `legalcode-complaint-drafter` (US-focused).

**Research methodology:**

- 6 parallel research agents (Opus) conducted domain-specific web research
- Research domains: CPR Part 16 and Statements of Case, pre-action protocols and conduct, English causes of action elements, strike-out and summary judgment under CPR, court structure and remedies, strategic pleading and professional conduct
- Findings synthesised into unified skill by orchestrator agent

**Key reference frameworks:**

- Civil Procedure Rules 1998 (SI 1998/3132) as amended [VERIFY]
- Practice Direction 16 — Statements of Case [VERIFY]
- Practice Direction — Pre-Action Conduct and Protocols [VERIFY]
- Limitation Act 1980 [VERIFY]
- Senior Courts Act 1981 [VERIFY]
- County Courts Act 1984 [VERIFY]
- Defamation Act 2013 [VERIFY]
- Consumer Rights Act 2015 [VERIFY]
- Employment Rights Act 1996 [VERIFY]
- Equality Act 2010 [VERIFY]
- SRA Standards and Regulations [VERIFY]
- Caparo Industries plc v Dickman [1990] 2 AC 605 — duty of care test [VERIFY]
- Bolam v Friern Hospital Management Committee [1957] 1 WLR 582 — professional standard [VERIFY]
- Rookes v Barnard [1964] AC 1129 — exemplary damages [VERIFY]
- American Cyanamid Co v Ethicon Ltd [1975] AC 396 — interim injunctions [VERIFY]
- Halsey v Milton Keynes General NHS Trust [2004] EWCA Civ 576 — ADR [VERIFY]
- Churchill v Merthyr Tydfil CBC [2023] EWCA Civ 1416 — compulsory ADR [VERIFY]

**Research artifacts:**

- Research findings from 6 parallel agents available in team workspace
- Web search results cached for verification

**Skill version:** 1.0
**Created:** 2026-03-01
**Created by:** Legalcode multi-agent research pipeline
