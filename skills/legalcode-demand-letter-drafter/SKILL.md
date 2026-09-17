---
name: legalcode-demand-letter-drafter
description: Drafts demand letters and cease and desist letters for common dispute types including breach
  of contract (UCC and common law), personal injury, employment disputes (wrongful termination, wage theft,
  FLSA violations, discrimination), consumer protection violations (CLRA, state UDAP, ACL), intellectual
  property infringement (trademark, copyright, patent cease and desist), debt collection (FDCPA and Regulation
  F compliant), property damage, and professional malpractice. Use when drafting any pre-suit demand,
  cease and desist, or statutory notice before commencing civil litigation.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Drafts demand letters and cease and desist letters for common dispute types including breach of contract (UCC and common law), personal injury, employment disputes (wrongful termination, wage theft, FLSA violations, discrimination), consumer protection violations (CLRA, state UDAP, ACL), intellectual property infringement (trademark, copyright, patent cease and desist), debt collection (FDCPA and Regulation F compliant), property damage, and professional malpractice. Covers proper party identification, factual narrative development, legal basis articulation with specific statutory references, damages calculation and demand amount, response deadlines, consequences of non-compliance, and settlement offer frameworks. Enforces compliance with professional conduct rules on threatening criminal prosecution (California Rule 3.10 and analogues), FDCPA validation notice requirements, UK Pre-Action Protocol obligations, and Australian ACL and unjustified threats statutes. Also drafts pre-litigation preservation notices and statutory cure demands. Supports US (federal + all states), England & Wales (PAP-compliant Letters Before Action), and Australia (ACL-compliant demand letters) jurisdictions. Use when drafting any pre-suit demand, cease and desist, or statutory notice before commencing civil litigation.


# Legalcode Demand Letter Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted demand letter drafting.
> It does not constitute legal advice. All outputs must be reviewed and signed by qualified
> legal counsel licensed in the relevant jurisdiction before sending. Demand letters have
> legal consequences — they may toll statutes of limitations, trigger professional conduct
> obligations, or constitute admissions depending on jurisdiction. Laws and professional
> rules change frequently; verify all authority before relying on any provision described
> here. Any cited authority marked `[VERIFY]` has not been independently validated and must
> be confirmed before reliance. Sending a demand letter on behalf of a client constitutes a
> representation that the claims are well-founded in fact and law.

---

## Purpose and Scope

This skill drafts demand letters, cease and desist letters, cure demands, statutory pre-suit
notices, and pre-litigation preservation notices by systematically mapping client facts to
the legal basis for each claim, structuring a persuasive narrative, calculating and
articulating damages, proposing a settlement offer framework, and formatting the document
for professional delivery.

The skill operates in three primary modes:

1. **Full Draft Mode**: Generates a complete, professionally formatted demand letter from
   client facts, instructions, and legal analysis — including proper party identification,
   factual narrative, legal basis with citations, damages calculation, settlement offer,
   response deadline, and reservation of rights.

2. **Validation Mode**: Reviews an existing draft demand letter for ethical compliance
   (professional conduct rules), statutory compliance (FDCPA, UK PAP, ACL), legal accuracy
   (elements established, damages defensible), and structural completeness (all required
   elements present).

3. **Pre-Litigation Package Mode**: Drafts the demand letter AND a companion preservation
   notice, jurisdiction and pre-suit checklist, and settlement framework memo for counsel.

**Covers:**

- **All major dispute types**: Breach of contract, personal injury, employment, consumer
  protection, IP infringement, debt collection, property damage, and professional malpractice
- **Letter types**: General demand, cease and desist, cure demand, statutory demand,
  FDCPA-compliant validation notice, pre-litigation preservation notice
- **Ethical gates**: Professional conduct compliance on threats, FDCPA compliance,
  UK IP (Unjustified Threats) Act 2017 compliance, Australian unjustified threats compliance
- **Pre-litigation requirements**: CLRA § 1782, PAGA § 2699.3, EEOC exhaustion,
  medical malpractice pre-suit notices, UCC cure rights, UK Pre-Action Protocols,
  Australian civil dispute resolution obligations
- **Settlement offer framework**: Without-prejudice strategy, time-limited offers,
  Calderbank letter mechanics, BATNA/ZOPA corridor framing
- **Damages articulation**: Special damages itemization, general damages, punitive damages,
  attorney's fees (fee-shifting statutes), pre-judgment interest by jurisdiction
- **Multi-jurisdictional coverage**: US federal + all states, England & Wales, Australia

**Does not:**

- File documents with any court or regulatory body
- Conduct independent factual investigation or verify client representations
- Constitute a Rule 11 / professional conduct certification (only qualified counsel may sign)
- Provide final legal opinions on the merits of claims
- Replace counsel's judgment on litigation strategy, claim selection, or risk assessment
- Provide tax or accounting advice on damages quantification
- Make decisions about whether to send the demand letter

**Related skills:**

- `legalcode-complaint-drafter` — File if demand is rejected; structural complement to this skill
- `legalcode-litigation-risk-assessment` — Assess litigation exposure before drafting demand
- `legalcode-settlement-negotiation` — Detailed negotiation strategy once demand is sent
- `legalcode-damages-calculation` — Deep damages modeling for complex multi-head claims
- `legalcode-early-case-assessment` — Strategic evaluation before any pre-litigation action
- `legalcode-litigation-hold-notice` — Companion preservation notice for evidence hold

---

## Jurisdiction and Governing Law

This skill is **jurisdiction-aware** and adapts analysis to the applicable legal framework
based on the governing law identified in Step 3.

**Jurisdiction-agnostic baseline**: Demand letters share common structural elements across
all common law jurisdictions — proper party identification, factual narrative, legal basis,
damages, and a response deadline. These elements appear in every letter regardless of forum.

**[JURISDICTION-SPECIFIC] markers** indicate where analysis must be adapted. Key
jurisdiction-specific areas:

| Element                      | US                                                                                           | England & Wales                                                     | Australia                                                                 |
| ---------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Pre-suit demand requirements | CLRA § 1782 (CA consumer), PAGA § 2699.3 (CA labor), medical malpractice notice statutes     | Pre-Action Protocol (specific PAPs or general PD)                   | ACCC Debt Collection Guideline; Civil Dispute Resolution Act 2011         |
| IP cease and desist          | DMCA § 512 (copyright); no unjustified threats statute at federal level                      | IP (Unjustified Threats) Act 2017 — strict safe harbor requirements | Patents Act s.128; Trade Marks Act s.129 — unjustified threats actionable |
| Debt collection              | FDCPA 15 U.S.C. § 1692 et seq.; Regulation F 12 C.F.R. Part 1006                             | FCA CONC Chapter 7; Consumer Duty (July 2023)                       | ACCC/ASIC Debt Collection Guideline April 2021; ACL s.18                  |
| Ethical rules on threats     | No single ABA rule; multi-rule framework (3.1/4.1/4.4/4.2); CA Rule 3.10 express prohibition | SRA Codes (Solicitors Act); no direct equivalent to CA Rule 3.10    | Law Council model rules; state bar rules                                  |
| Without-prejudice privilege  | FRE 408; state equivalents (CA Evid. Code § 1152)                                            | Rush & Tompkins [1989] AC 1280; "WP save as to costs" (Calderbank)  | Common law; state Calderbank letter rules; UCPR                           |
| Interest                     | Cal. Civ. Code § 3289 (contract: 10%; tort: 7%); 28 U.S.C. § 1961 (federal post-judgment)    | Late Payment of Commercial Debts Act 1998 (8% over BoE base)        | Judiciary Act 1903 s. 51A; state-based provisions [VERIFY current rate]   |
| Employment pre-conditions    | EEOC charge (Title VII/ADA/ADEA); NLRB; state agencies                                       | ACAS Early Conciliation mandatory (ET Act 1996 s.18A)               | FWC 21-day filing deadline; no mandatory pre-filing demand                |

---

## Interactive Clarification

This skill uses **CLARIFY blocks** at key decision points to gather context that materially
changes the analysis. Present each as a structured question with options and a brief
"Why this matters" explanation.

**When to use**: Pause for CLARIFY when the answer would change the letter type, jurisdiction
analysis, ethical risk profile, or settlement strategy. Skip if the information is already
provided.

**Default behavior** when the user does not respond: State assumptions explicitly and
proceed. Do not loop indefinitely; proceed after two clarification rounds maximum.

---

## Workflow

### Step 1: Accept Input and Matter Description

Accept input in any of these formats:

- **Client narrative**: Facts described in plain language
- **Documents**: Contracts, invoices, correspondence, medical records, employment records
- **Prior legal work**: Early case assessment, litigation risk report, ECA memo
- **Combination**: Any combination of the above

**Before proceeding**: Verify the following minimum information is available or can be
inferred:

- Identity of the claimant (or plaintiff/sending party)
- Identity of the respondent (or defendant/receiving party)
- Nature of the dispute (what happened, to whom, when)
- Relief sought (money, injunction, cessation of conduct, or combination)
- Anticipated forum and governing law (or basis to determine this)

If any minimum information is missing, proceed with CLARIFY Block 1 below.

### Step 2: Gather Context

**⟁ CLARIFY Block 1 — Letter Type**

> What type of letter should be drafted?

- **General demand letter** — Assert claims and demand compensation or remedy for a
  civil dispute (breach of contract, personal injury, property damage, malpractice). Most
  common type.
  _Why it matters_: Structure, tone, and content differ from cease and desist. No special
  statutory form required for most disputes.

- **Cease and desist letter** — Demand that the respondent stop specific ongoing conduct
  (IP infringement, tortious interference, defamation, unfair competition, harassment).
  _Why it matters_: C&D letters for IP in the UK and Australia must comply with unjustified
  threats statutes or expose the sender to a counterclaim.

- **Cure demand / notice of breach** — Demand that the respondent cure a specific breach
  within a defined period before a party exercises contract remedies (termination, cover).
  _Why it matters_: Some statutes and contracts require notice and opportunity to cure
  before a remedy is available (UCC § 2-508 seller's cure; lease cure periods).

- **Statutory demand / pre-suit notice** — Comply with a specific statutory requirement
  before filing suit (CLRA § 1782, PAGA § 2699.3, medical malpractice notice, UK PAP).
  _Why it matters_: Failure to send a compliant statutory notice may bar specific damages
  claims or result in dismissal of the lawsuit entirely.

- **FDCPA validation notice** — First written communication by a third-party debt collector
  to a consumer for a consumer debt (personal, family, or household purpose).
  _Why it matters_: 15 U.S.C. § 1692g mandates specific disclosures within 5 days of
  initial communication; failure is a per se FDCPA violation regardless of debt validity.

- **Pre-litigation preservation notice** — Notify the respondent to preserve all documents,
  electronically stored information, and physical evidence related to the dispute.
  _Why it matters_: Establishes a record for spoliation arguments if evidence is destroyed
  after notice; may be sent with or without a separate demand letter.

**Default if not specified**: General demand letter.

---

**⟁ CLARIFY Block 2 — Jurisdiction and Governing Law**

> What jurisdiction governs this dispute and where will litigation be filed if the demand is
> rejected?

- **United States — Federal Court** (specify district): FRCP rules apply; EEOC exhaustion
  may be required for employment discrimination; diverse parties trigger diversity jurisdiction.
- **United States — State Court** (specify state): State-specific pre-suit requirements;
  state professional conduct rules; state UDAP statutes.
- **England & Wales**: Pre-Action Protocol requirements; CPR costs consequences; IP
  (Unjustified Threats) Act 2017; ACAS early conciliation for employment.
- **Australia — Federal** (Federal Court or FWC): Civil Dispute Resolution Act 2011
  genuine steps requirement; ACL applies nationally.
- **Australia — State/Territory** (specify): State Supreme Court rules; state-specific
  civil liability acts; relevant consumer protection enforcement.
- **Other** (specify): Research applicable framework.

**Default if not specified**: US state court in the state of the respondent's principal
place of business (or residence for individuals).

---

**⟁ CLARIFY Block 3 — Counterparty Profile**

> What is the nature and sophistication of the respondent?

- **Sophisticated commercial entity with in-house or retained counsel**: Permit more
  technical legal citations; shorter factual narrative acceptable; expect strategic response.
- **Small business or individual without known legal representation**: Simpler language;
  more detailed factual narrative; note right to seek counsel.
- **Government entity or agency**: Different procedures (tort claims notices, sovereign
  immunity); contact information differs; response times are longer.
- **Known to have active legal representation**: Note Model Rule 4.2 / professional conduct
  obligation — no direct contact with represented party; send letter only to counsel of record.
- **Unknown**: Assume sophisticated entity; adapt if client provides additional information.

**Default if not specified**: Sophisticated commercial entity with counsel (maximizes
precision and ethical safeguards).

---

**⟁ CLARIFY Block 4 — Settlement Authority and Demand Amount**

> What is the client's settlement authority and demand amount strategy?

- **Demand full damages + fees, willing to negotiate down to $\_\_\_ range**: Standard
  approach; set demand at full compensable damages + fees + interest + cost premium.
- **Demand full damages, no negotiation (maximum leverage / precedent)**: Most aggressive;
  appropriate for IP infringement with injunctive priority; risks litigation.
- **Demand $**_ (specific figure), willing to accept any amount above $_\*\*\*\*: Client has
  specific walk-away; calculate demand as 1.5–3× walk-away depending on strength.
- **Amount to be determined after damages assessment**: Defer until Step 6; typical for
  complex multi-head claims.

**Default if not specified**: Demand full compensable damages plus pre-judgment interest,
attorney's fees (if statute or contract provides), and a reserve above minimum acceptable
settlement; advise counsel to confirm client's walk-away before sending.

---

**⟁ CLARIFY Block 5 — Timing Pressures**

> Are there any statute of limitations or procedural timing pressures?

- **Statute of limitations approaching within 6 months**: Include explicit SOL warning in
  letter; state that suit will be filed by [date] absent adequate response; do not waive
  through misleading extension representations.
- **Statute of limitations more than 6 months away**: Standard response deadline (14–30
  days); allow reasonable time for response and negotiation.
- **Administrative/regulatory deadline** (e.g., EEOC 180/300-day charge window, UK ET 3
  months, AU FWC 21-day unfair dismissal): Identify deadline; note it in letter; time the
  demand to allow administrative steps to proceed in parallel.
- **No known timing pressure**: Standard approach; use 14-day (business) response deadline
  for commercial disputes; 30 days for consumer debt collection matters.
- **Discovery or litigation already commenced**: Demand letter may still be sent; note
  pending proceedings; coordinate with litigation counsel.

**Default if not specified**: Assume no immediate SOL pressure; use 14-business-day response
deadline for commercial matters and 30-calendar-day deadline for consumer matters.

---

### Step 3: Jurisdiction Analysis and Pre-Suit Requirements Check

Before drafting, verify compliance with all applicable pre-litigation requirements. Flag
any **CRITICAL** items — mandatory steps whose omission bars claims or results in dismissal.

**Run the following checks for the identified jurisdiction and dispute type:**

#### 3.1 Statute of Limitations Analysis

| Claim Type                          | US (General)                                                        | California                                                 | England & Wales                    | Australia                    |
| ----------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------- | ---------------------------- |
| Written contract breach             | 4–6 years (varies by state)                                         | 4 years (CCP § 337)                                        | 6 years (Limitation Act 1980)      | 6 years (most states)        |
| Oral contract breach                | 2–4 years (varies by state)                                         | 2 years (CCP § 339)                                        | 6 years                            | 6 years                      |
| Personal injury (general)           | 2–3 years (varies)                                                  | 2 years (CCP § 335.1)                                      | 3 years (Limitation Act 1980 s.11) | 3 years (varies by state)    |
| Sale of goods (UCC)                 | 4 years (UCC § 2-725)                                               | 4 years (UCC adopted)                                      | 6 years                            | Varies                       |
| Employment discrimination (federal) | 300 days for EEOC charge (deferral states); 180 days (non-deferral) | 300 days; DFEH/CCRD 3 years                                | ET claim 3 months                  | FWC unfair dismissal 21 days |
| FLSA wage claim                     | 2 years (general); 3 years (willful)                                | 3 years (CA Labor Code)                                    | ET claim 3 months                  | FWC 21 days                  |
| Medical malpractice                 | Varies; many states 2–3 years                                       | 3 years from injury or 1 year from discovery (CCP § 340.5) | 3 years                            | Varies                       |
| IP infringement (copyright)         | 3 years from discovery (17 U.S.C. § 507)                            | Federal                                                    | 6 years                            | 6 years                      |
| IP infringement (trademark)         | Laches doctrine applies                                             | Federal/state                                              | 6 years                            | 6 years                      |

**Tolling rules**: Note any applicable discovery rule, equitable tolling, fraudulent concealment,
disability tolling, or government entity notice period tolling.

**SOL Warning Protocol**: If the SOL will expire within 90 days of the anticipated send date,
include the following statement in the demand letter:

> "Please be advised that [Claimant] intends to file suit in [forum] no later than [date],
> absent a written response by [response deadline] indicating willingness to resolve this
> matter on reasonable terms."

#### 3.2 Mandatory Pre-Suit Requirements

**CRITICAL** — Failure to satisfy these requirements may bar claims or result in dismissal.

| Requirement                                                       | When Required                                                                        | Jurisdiction        | Consequence of Non-Compliance                                                                |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------- | -------------------------------------------------------------------------------------------- |
| CLRA § 1782 notice                                                | Consumer lawsuit seeking damages under Consumers Legal Remedies Act                  | California          | Bars damages claim entirely; condition precedent                                             |
| PAGA § 2699.3 notice                                              | Civil enforcement of CA Labor Code violations                                        | California          | Bars PAGA claim; notice must be sent to LWDA by online filing AND certified mail to employer |
| Medical malpractice notice (CCP § 364)                            | Medical malpractice lawsuit                                                          | California          | Tolls SOL during 90-day notice period; required before filing                                |
| Medical malpractice pre-suit investigation (Fla. Stat. § 766.106) | Medical malpractice lawsuit                                                          | Florida             | Prohibits filing during 90-day period; expert affidavit required                             |
| State expert affidavit (29 states)                                | Medical and other professional malpractice                                           | Various US states   | Dismissal if not filed with or before complaint                                              |
| EEOC charge                                                       | Federal employment discrimination (Title VII, ADA, ADEA)                             | US federal          | Exhaustion required; 90-day suit window after right-to-sue                                   |
| UK Pre-Action Protocol                                            | Most civil claims (specific PAPs for personal injury, debt, professional negligence) | England & Wales     | Adverse costs orders; court may sanction non-compliance                                      |
| ACAS Early Conciliation                                           | Employment Tribunal claims (all types)                                               | England & Wales     | ET claim rejected without ACAS certificate number                                            |
| UK PAP for Debt Claims (30-day cascade)                           | Business claiming debt from individual                                               | England & Wales     | Adverse costs; court may stay proceedings for non-compliance                                 |
| UCC cure opportunity (§ 2-508)                                    | Sale of goods: buyer rejecting goods before contract time expires                    | All UCC states      | Cure right exists; demand should allow cure period                                           |
| Civil Dispute Resolution Act 2011                                 | All federal civil proceedings                                                        | Australia (federal) | Court may consider non-compliance in costs orders                                            |

#### 3.3 Preservation Notice Assessment

**Determine whether to send a companion preservation notice:**

- Is electronically stored information at risk of routine deletion? → YES: include preservation demand
- Has the respondent been notified of the dispute yet? → NO: send preservation notice simultaneously
- Does the dispute involve surveillance footage, vehicle data, or perishable physical evidence? → YES: urgent preservation notice required

---

### Step 4: Ethical and Professional Conduct Gates

**Apply all gates before drafting.** If any gate FAILS, do not draft the letter until the
issue is resolved with counsel.

#### Gate 1 — No Threat of Criminal Prosecution to Obtain Civil Advantage

**Rule**: Conditioning civil settlement on the withdrawal of criminal charges, or threatening
to file criminal charges to coerce a civil payment, violates professional conduct rules in
California (Rule 3.10 — express prohibition) and approximately eleven other US states, and
is likely tortious (potentially constituting extortion) in all jurisdictions.

**What IS permitted**:

- Stating factually that the respondent's conduct "may constitute [specific crime]" if that
  statement is accurate and made as description, not threat
- Making an independent criminal referral to law enforcement, not contingent on civil outcome
- Noting that conduct will be reported to relevant regulatory authorities as a matter of fact

**What is PROHIBITED**:

- "Pay $\_\_\_ or I will file criminal charges with [agency]"
- "If you do not settle, I will refer this matter to the District Attorney"
- Any language conditioning withdrawal of a criminal complaint on civil payment

**Check**: Review draft for any language that conditions criminal/administrative action on
civil outcome. Replace with factual description or remove.

**[JURISDICTION-SPECIFIC]** — Verify professional conduct rule in the specific state/
jurisdiction before including any reference to criminal or administrative consequences.
In California, apply Rule 3.10 strictly. In other states, apply the multi-rule framework
(Model Rules 3.1/4.1/4.4/4.2). [VERIFY whether your jurisdiction has an express rule.]

#### Gate 2 — No False Representations About Legal Status, Amount, or Available Remedies

**Rule**: ABA Model Rule 4.1 (US); FDCPA § 1692e (for debt collection); ACL s. 18 AU
(misleading/deceptive conduct); UK FCA CONC 7.3.

**Check**: Verify that:

- The claim amount is based on defensible calculation, not inflation
- Any threatened legal action is genuinely available and genuinely intended
- Attorney's fees are only demanded if a fee-shifting statute, contract, or rule applies
- Pre-judgment interest is calculated at the correct statutory rate
- Any reference to "additional damages" is specific and legally grounded

#### Gate 3 — Contact With Represented Parties

**Rule**: If the respondent is known to have active legal representation, send the letter
to the respondent's counsel — not directly to the respondent. Direct contact with a
represented party without counsel's consent violates Model Rule 4.2 (US), SRA Codes (UK),
and equivalent professional rules in Australia.

**Check**: Is the respondent known to be represented? If YES → address to counsel of record.

#### Gate 4 — FDCPA Compliance (Debt Collection Only)

Apply if this is a debt collection demand letter from a third-party collector seeking a
consumer debt (personal, family, or household purpose):

- **§ 1692g Validation Notice**: Must be in or sent within 5 days of initial communication.
  Contains: amount of debt; creditor name; 30-day dispute right; verification right;
  original creditor identification right.
- **§ 1692e(11) Mini-Miranda Warning**: Initial communication must state: "This communication
  is from a debt collector. This is an attempt to collect a debt and any information obtained
  will be used for that purpose."
- **§ 1692g(b) Non-Overshadowing**: No communication during the 30-day dispute window may
  overshadow or be inconsistent with the consumer's right to dispute.
- **Regulation F (12 C.F.R. Part 1006)**: Electronic communications must be private; social
  media contact must include opt-out; validation notice must itemize debt components.

**Check**: Does this letter trigger FDCPA? → If YES, apply debt collection template (Step 7d).

#### Gate 5 — UK and Australian IP Unjustified Threats (IP C&D Letters Only)

**England & Wales — IP (Unjustified Threats) Act 2017**:
A communication threatening IP infringement proceedings may be the subject of a threats
action by any aggrieved party unless it falls within a "permitted purpose" safe harbor.

**Permitted purposes** (safe harbor):

- Notifying that an IP right exists
- Discovering whether and by whom the right has been infringed
- Giving notice of the IP right held by the sender

**NOT a permitted purpose** (i.e., outside safe harbor — triggers threats liability):

- Demanding the recipient cease commercially using the allegedly infringing item
- Demanding delivery up or destruction of infringing goods
- Demanding undertakings regarding future conduct

**Professional adviser exception**: An IP adviser acting on client instructions is protected
from the threats action if they identify their client in the communication.

**Best practice for UK IP C&D**: Frame the letter as notification of rights + request for
information about use, not as an express demand to cease. Keep express demands to private
party settlements (without public "threats").

**Australia — Patents Act 1990 s. 128 / Trade Marks Act 1995 s. 129**:
Unjustified threats of IP infringement proceedings are actionable. Relief includes
declaration, injunction, and damages (s. 128(1A) allows additional damages for blatant
threats). A C&D letter must be based on a genuine, legally and factually supported claim.

#### Gate 6 — Tone Assessment

Demand letters must project professional confidence without emotional charge. Aggressive
language that threatens, demeans, or harasses the recipient:

- Undermines credibility
- May expose the sender to harassment, defamation, or professional discipline claims
- Reduces likelihood of settlement (invites adversarial posture)
- In FDCPA context (§ 1692d), constitutes a per se violation

**Prohibited tone markers**: "outrageous," "egregious," "fraudulent conduct" (without legal
support), "criminal" (unless factually accurate and not a threat), personal attacks,
statements of moral judgment unconnected to legal basis.

**Permitted**: "Material breach," "serious consequences," "substantial damages,"
"compelled to seek judicial relief," "without prejudice to all available remedies."

---

### Step 5: Letter Type Configuration

Apply the appropriate structural template based on the letter type identified in CLARIFY Block 1.

#### 5a. General Demand Letter

Structure: Header → Parties → Purpose Statement → Factual Narrative (numbered) → Legal Basis
(elements + statutory citations) → Damages Calculation (itemized table) → Settlement Offer →
Response Deadline → Consequences → Reservation of Rights → Signature

#### 5b. Cease and Desist Letter

Structure: Header → Parties → [UK: Permitted Purpose Statement per IP (Unjustified Threats)
Act 2017 — "This letter notifies you that..."] → IP Right Identification (registration No.,
first use dates, etc.) → Description of Infringing Conduct (specific and factual) →
Demand to Cease [note: outside safe harbor in UK — use only after Gates 4/5 cleared] →
Damages and Accounting Demand → Response Deadline → Consequences → Signature

#### 5c. Cure Demand

Structure: Header → Parties → Contract Reference (attach or cite) → Specific Breach
Identified (clause violated, conduct constituting breach) → Cure Period (10 business days
standard; check contract; UCC § 2-508 if goods sale) → Consequences of Failure to Cure
(termination, cover, damages) → Reservation of Rights → Signature

#### 5d. FDCPA Validation Notice (Debt Collection)

Structure: Mini-Miranda Warning (§ 1692e(11)) → Amount of Debt (itemized per Reg. F:
principal + interest + fees) → Creditor Identification → Right to Dispute Within 30 Days →
Verification Right → Original Creditor Identification Right → Opt-Out for Electronic
Communications (if applicable) → Collector Identification → Signature
[Note: No standard demand language threatening litigation in initial contact; state only
facts and statutory disclosures. Litigation threats added in subsequent communications
if not resolved.]

#### 5e. UK Letter Before Action (PAP-Compliant)

Structure (per relevant Pre-Action Protocol and Practice Direction):

- Claimant details and solicitor's details
- Clear statement of the nature of the claim and legal basis
- Precise quantification of the financial claim with supporting documents
- Statement of what documentation the claimant relies on
- Reasonable time for response (Debt PAP: 30 days; PI: 21 days; Prof. Neg: 3 months)
- Invitation to respond to included Reply Form (Debt PAP only)
- ADR/mediation reference (CJC November 2024 recommendations)

#### 5f. Pre-Litigation Preservation Notice

Structure: Header → Parties → Nature of Dispute → Legal Authority (litigation hold duty) →
Categories of Evidence to Preserve (documents, ESI, physical evidence, surveillance footage,
communications) → Instructions for Preservation → Consequences of Spoliation → Signature

---

### Step 6: Liability and Damages Assessment

Before drafting the letter, assess the legal merit and damages quantum for each claim.

#### 6.1 Dispute-Type Legal Element Mapping

Map the available facts to the legal elements of each claim type:

**Breach of Contract**

- [ ] Valid and enforceable contract exists (written/oral; statute of frauds issue?)
- [ ] Claimant performed or was excused from performance
- [ ] Respondent breached specific provision(s) — identify clause(s)
- [ ] Breach was material (vs. minor: minor breach = damages only, not termination right)
- [ ] Damages resulted from the breach (causation)
- [ ] Damages are within contemplation of parties (Hadley v Baxendale proximate damages)
- [ ] [JURISDICTION-SPECIFIC] UCC Article 2 cure rights assessed (if sale of goods)

**Personal Injury**

- [ ] Duty of care owed (relationship, foreseeability, proximity)
- [ ] Breach of that duty (standard of care violation)
- [ ] Causation (actual and proximate; "but for" test; no superseding cause)
- [ ] Damages (physical injury, economic loss, non-economic loss)
- [ ] Government entity: Tort claims notice filed within deadline?
- [ ] Medical malpractice: Expert review completed; pre-suit notice satisfied?
- [ ] Insurance subrogation: Identify any known liens or subrogation interests

**Employment — Wrongful Termination**

- [ ] Employment contract or handbook creates legitimate expectation (implied contract)
- [ ] OR public policy exception applies (fired for exercising a statutory right)
- [ ] OR state FEHA/Title VII/ADEA/ADA: Protected class + adverse action + causal link
- [ ] At-will presumption: Does any exception apply in the jurisdiction?
- [ ] EEOC charge filed (if Title VII/ADA/ADEA claim)?
- [ ] Right-to-sue letter obtained?
- [ ] UK: ACAS early conciliation completed?
- [ ] AU: FWC 21-day filing window observed?

**Employment — Wage Theft / FLSA**

- [ ] Hours worked (with documentation: timesheets, records, calculations)
- [ ] Regular rate of pay; overtime rate calculation
- [ ] Shortfall calculation (period by period)
- [ ] Willful violation? (extends SOL to 3 years)
- [ ] Liquidated damages available (equal to unpaid wages, 29 U.S.C. § 216)
- [ ] State wage law: Is state law more protective? (CA, NY often are)

**Consumer Protection**

- [ ] Identify applicable statute: CLRA § 1770; FTC Act § 5; state UDAP; UK CRA 2015; ACL s. 18
- [ ] CLRA: Has the § 1782 certified-mail notice been sent? 30-day cure period satisfied?
- [ ] Identify specific subsection violation (e.g., CLRA § 1770(a)(7) — false origin of goods)
- [ ] Massachusetts Ch. 93A: 30-day pre-suit demand required; willful/knowing triggers treble damages
- [ ] [JURISDICTION-SPECIFIC] State UDAP provides treble damages, attorney's fees, civil penalties?

**IP Infringement — Cease and Desist**

- [ ] IP right confirmed: copyright registration, USPTO trademark registration (or common law use), patent number
- [ ] Ownership verified (chain of title, assignments, work-for-hire)
- [ ] Respondent's use identified specifically (URLs, product names, dates, screenshots)
- [ ] Likelihood of confusion (trademark) or substantial similarity (copyright) assessed
- [ ] DMCA § 512(c)(3) takedown notice sent to platform/host (if copyright, online infringement)?
- [ ] UK Gate 5 / AU unjustified threats analysis completed (Gate 5 above)
- [ ] Damages: lost royalties, profits, statutory damages (17 U.S.C. § 504 — $750–$30,000; willful: up to $150,000)

**Property Damage**

- [ ] Ownership or possessory interest in damaged property established
- [ ] Respondent's conduct (negligence, trespass, conversion, nuisance) identified
- [ ] Damages: repair cost (contractor estimates), replacement cost, diminished value (professional appraisal for vehicles)
- [ ] Betterment deduction: If repair results in improvement over pre-damage condition, deduct value of betterment
- [ ] Insurance: Has claimant's insurer been notified? Subrogation rights of insurer?

**Professional Malpractice**

- [ ] Professional relationship established (attorney-client, doctor-patient, accountant-client)
- [ ] Standard of care identified (expert witness may be required)
- [ ] Breach of standard of care established
- [ ] Causation: "Case within a case" — but for the malpractice, outcome would have been better
- [ ] Damages: additional economic loss, disgorgement of fees, consequential losses
- [ ] Expert affidavit: Has the jurisdiction's certificate-of-merit requirement been satisfied?
  - 29 US states require affidavit for medical malpractice
  - Florida: Expert affidavit must accompany pre-suit notice (Fla. Stat. § 766.106)
  - [VERIFY] requirements in the specific state before sending demand

#### 6.2 Damages Calculation

Itemize all heads of damages in a structured table:

| Head of Damage                      | Category              | Calculation Method          | Amount      | Confidence       | [VERIFY]       |
| ----------------------------------- | --------------------- | --------------------------- | ----------- | ---------------- | -------------- |
| [Special/economic damages - head 1] | Special               | [Description + source]      | $\_\_\_     | HIGH/MED/LOW     | [cite]         |
| [Special/economic damages - head 2] | Special               | [Description + source]      | $\_\_\_     | HIGH/MED/LOW     | [cite]         |
| [Non-economic / general damages]    | General               | Multiplier or per diem      | $\_\_\_     | MED/LOW          | Estimate       |
| Pre-judgment interest               | Statutory             | [Rate × period × principal] | $\_\_\_     | HIGH             | [cite statute] |
| Attorney's fees                     | Statutory/contractual | [Basis for recovery]        | $\_\_\_     | HIGH/MED         | [cite]         |
| Punitive/exemplary damages          | Punitive              | [Legal standard met?]       | $\_\_\_     | LOW (note basis) | [verify]       |
| **Total Demand Amount**             |                       |                             | **$\_\_\_** |                  |                |

**Demand Amount Strategy**:

- Set demand at 1.5–3× the client's minimum acceptable settlement (walk-away)
- Ensure every item is itemized and defensible
- Reserve right to claim additional damages, costs, and fees if litigation proceeds
- For FDCPA matters: Do not demand amounts not authorized by contract or law (§ 1692f(1))

#### 6.3 Confidence Assessment

Rate the overall demand defensibility:

| Level        | Range     | Meaning                                                       | Action                                            |
| ------------ | --------- | ------------------------------------------------------------- | ------------------------------------------------- |
| **Definite** | 0.95-1.0  | Clear legal basis; well-documented damages; no novel elements | State with full confidence                        |
| **High**     | 0.80-0.94 | Strong legal basis; some calculation uncertainty              | State with brief qualification                    |
| **Probable** | 0.60-0.79 | Arguable legal basis; damages require expert support          | Note assumptions; recommend expert consultation   |
| **Possible** | 0.40-0.59 | Novel theory or disputed facts; litigation outcome uncertain  | Flag for counsel review; consider whether to send |
| **Unlikely** | 0.0-0.39  | Weak or unsupported legal basis                               | Do not draft as written; recommend not sending    |

**If demand confidence is Possible or Unlikely**: Notify counsel before drafting. A weak
demand letter may weaken negotiating position and invite a Rule 11 / professional conduct
challenge.

---

### Step 7: Draft the Demand Letter

**Core structure** (adapt for letter type per Step 5):

```
[LETTERHEAD — Sender name, address, phone, email]
[DATE]

VIA [delivery method: certified mail / overnight courier / email / hand delivery]

[Respondent Name]
[Respondent Address]

Re: [Subject: e.g., Demand for Payment — Breach of Contract / Cease and Desist —
    Trademark Infringement / Notice of Claim — Personal Injury of [Client Name] /
    FDCPA Validation Notice — [Creditor Name] Account]

Dear [Mr./Ms./Mx. [Surname] / "To Whom It May Concern" if no named contact]:

I. INTRODUCTION AND AUTHORITY TO ACT
   [Identify sender's capacity: attorney for claimant, or claimant sending directly]
   [If attorney: "I write on behalf of my client, [Name]."]
   [State purpose: "This letter constitutes formal notice of [nature of claim] and a
   demand for [remedy] as set forth herein."]

II. FACTUAL BACKGROUND
   [Numbered paragraphs: concise, chronological, specific (names, dates, amounts, places)]
   [Attach documentary evidence as Exhibit A, B, C, etc.]
   [Every fact stated must be supportable; do not overstate or embellish]

III. LEGAL BASIS
   [Map facts to legal elements of each claim]
   [Cite specific statutes, regulations, or legal principles with jurisdiction]
   [For US: cite both the applicable federal or state statute and common law basis if applicable]
   [For UK: cite PAP compliance, statute, and common law basis]
   [For AU: cite ACL section, relevant state legislation, and common law]

IV. DAMAGES
   [Present itemized damages table from Step 6.2]
   [Include pre-judgment interest calculation]
   [Include attorney's fees if fee-shifting statute or contractual provision applies]
   [Note: This demand does not waive the right to seek additional damages, costs, and
   fees if litigation becomes necessary.]

V. DEMAND
   [SETTLEMENT OFFER — mark if "WITHOUT PREJUDICE" to protect under applicable privilege]
   ["[Claimant] hereby demands payment of $[total amount] / [specific remedy] in full
   satisfaction of the claims described herein."]
   [If settlement offer: "In lieu of commencing litigation, [Claimant] is prepared to
   accept $[settlement offer] in full and final settlement of all claims, provided that
   [Respondent] responds in writing by [DATE — X business/calendar days from date of
   letter]."]

VI. RESPONSE DEADLINE AND CONSEQUENCES
   ["Please respond in writing by [DATE]."]
   ["Failure to respond or to propose an acceptable resolution by this date will leave
   [Claimant] with no alternative but to pursue all available legal remedies, including
   commencing proceedings in [forum], which may result in additional costs, attorneys'
   fees, and pre-judgment interest accruing at [rate]."]
   [SOL Warning if applicable: "Please be advised that the applicable statute of limitations
   requires action by [date], after which [Claimant's] rights may be affected."]

VII. RESERVATION OF RIGHTS
   ["This letter is not intended to, and does not, waive any rights, claims, defenses, or
   remedies available to [Claimant], all of which are expressly reserved."]
   ["Nothing in this letter constitutes an admission of fact or law, or a limitation of
   [Claimant's] claims to the matters described herein."]

[SIGNATURE BLOCK]
[Name, Title, Bar Number if attorney]
[Contact Information]

Enclosures: [List exhibits]
```

**Drafting discipline**:

- Number every factual paragraph
- Use defined terms consistently (e.g., "the Contract," "the Respondent," "the Infringing Mark")
- Do not use inflammatory adjectives; let facts speak
- Use active voice and present tense for current claims; past tense for historical facts
- Set response deadline as a specific calendar date, not a floating period ("by March 16, 2026"
  not "within 14 days of this letter")

---

### Step 8: Settlement Offer and Without-Prejudice Framework

**Determine without-prejudice status of demand:**

| Jurisdiction    | Without-Prejudice Rule                                                                     | Recommendation                                                                                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| United States   | FRE 408; state equivalents (CA Evid. Code § 1152)                                          | Label "WITHOUT PREJUDICE — FOR SETTLEMENT PURPOSES ONLY" if demand includes a compromise offer below full damages; omit label if asserting full legal entitlement |
| England & Wales | Rush & Tompkins [1989] AC 1280 — genuine settlement communications protected without label | Mark "WITHOUT PREJUDICE SAVE AS TO COSTS" if offering a Calderbank offer; standard PAP letters are not typically WP                                               |
| Australia       | Common law WP privilege; Calderbank letters for cost-shifting                              | Mark "WITHOUT PREJUDICE SAVE AS TO COSTS" for formal Calderbank offers; ensure offer represents genuine compromise                                                |

**Settlement offer framing**:

1. **Opening anchor**: Set demand amount above client's minimum acceptable settlement (MAS)
   but below an amount that appears fabricated. Itemization supports credibility.
2. **Settlement offer** (separate from full damages demand): A discounted amount offered
   to avoid litigation, with clear expiry and consequences for non-acceptance.
3. **Calderbank mechanics** (UK/AU): "Without Prejudice Save as to Costs" letter with
   specific offer amount, deadline, and explicit statement that indemnity costs will be
   sought if the offeree fails to beat the offer at trial.
4. **Time-limited offers**: Set a specific calendar deadline. [JURISDICTION-SPECIFIC]
   California CCP § 999 et seq. governs time-limited pre-suit demands in insurance
   contexts (effective January 1, 2023) — ensure statutory compliance if applicable.

**Response scenario planning** (prepare counsel for each):

- **Scenario A — Acceptance**: Client accepts offer; document settlement in writing; release
  needed; consider scope of release (full vs. partial).
- **Scenario B — Counteroffer**: Within client's ZOPA corridor? → Negotiate. Below MAS? →
  Counter or decline.
- **Scenario C — Rejection / Silence**: File complaint in identified forum; review for Rule
  11 compliance; consider whether to request EEOC/ACAS/FWC steps if applicable.

---

### Step 9: Tone and Professionalism Review

Before finalizing, run the following tone checks:

- [ ] **Factual specificity**: Every allegation includes names, dates, amounts, and exhibit
      references. Vague allegations are replaced with specific ones or removed.
- [ ] **Professional register**: No emotional language, personal attacks, or moral judgments
      unconnected to legal basis.
- [ ] **Legal precision**: Statutory citations are accurate (confirmed by citation gates, below).
      No overstatement of available remedies.
- [ ] **Proportionality**: Demands match what a court could realistically award. Punitive
      damages noted only if legal standard (fraud/malice/oppression) is met.
- [ ] **Credibility**: Demand amount is grounded in itemized calculation, not a round number.
      "I will see you in court by [specific date]" is more credible than "we reserve all rights."
- [ ] **Completeness**: All required statutory elements for the letter type are present
      (FDCPA mini-Miranda, PAP Reply Form reference, CLRA § 1782 language, etc.).

---

### Step 10: Output Delivery and Glass Box Audit

Deliver the complete demand letter package with the following components:

**10.1 Demand Letter Document** — Final formatted letter ready for counsel review and signature.

**10.2 Pre-Suit Requirements and Jurisdiction Checklist** — Summary of:

- Statute of limitations (date of expiry, tolling analysis, SOL pressure alert)
- All mandatory pre-suit procedures with status (CRITICAL items flagged)
- Required delivery method (certified mail, personal service, email with confirmation)
- Any statutory language or form requirements included

**10.3 Ethical Compliance Memo (Confidential — Attorney Work Product)**:

- Gate 1: No criminal prosecution threat — [PASS / FAIL: describe]
- Gate 2: No false representations — [PASS / FAIL: describe]
- Gate 3: No contact with represented party — [PASS / N/A]
- Gate 4: FDCPA compliance — [PASS / N/A / FAIL: describe]
- Gate 5: UK/AU IP unjustified threats — [PASS / N/A / FAIL: describe]
- Gate 6: Tone assessment — [PASS / ADVISORY: describe]
- Demand defensibility score: [X.XX / 1.0]
- Overall assessment: [DEFENSIBLE / PROCEED WITH CAUTION / DO NOT SEND]

**10.4 Settlement Framework and Response Scenarios** — Brief memo for counsel:

- Demand amount (opening anchor)
- Client's minimum acceptable settlement (MAS)
- ZOPA corridor estimate (if counterparty position can be inferred)
- Response deadline
- Three response scenarios with recommended next steps

**10.5 Glass Box Audit Trail** (see template below)

---

## Deep Topic Analysis: Dispute-Type Reference Matrix

| Dispute Type                       | Key Statutes                                                   | Pre-Suit Requirements                                                                                                     | Special Considerations                                                                 |
| ---------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Breach of Contract                 | UCC §§ 2-601/2-508 (goods); Hadley v Baxendale (common law)    | Cure period if goods (UCC § 2-508); contractual notice requirements                                                       | Material vs. minor breach; anticipatory repudiation; Statute of Frauds                 |
| Personal Injury                    | State negligence law; govt. entity tort claims acts            | Government entity notice (CA Gov. Code § 911.2; NY GML § 50-e); medical malpractice pre-suit (29 states expert affidavit) | Insurance subrogation/medical liens; spoliation notice; discovery rule for SOL         |
| Employment (Discrimination)        | Title VII; ADA; ADEA; state FEHA/FHRA                          | EEOC charge (300 days deferral/180 days non-deferral); right-to-sue before suit                                           | ACAS (UK); FWC 21-day window (AU); constructive discharge analysis                     |
| Employment (Wages)                 | FLSA §§ 206/207; state wage laws (CA Lab. Code § 1194 et seq.) | None required under FLSA; PAGA notice for CA Labor Code (§ 2699.3)                                                        | Willful violation extends SOL; liquidated damages (doubling); misclassification issues |
| Consumer Protection                | CLRA § 1770 (CA); Mass. Ch. 93A; ACL s. 18 (AU); CRA 2015 (UK) | CLRA § 1782 certified mail 30-day cure; Mass. Ch. 93A 30-day demand                                                       | State UDAP treble damages/attorney's fees; CLRA notice bars damages if omitted         |
| IP (Copyright C&D)                 | 17 U.S.C. §§ 501-513; DMCA § 512                               | DMCA takedown to host; registration required for statutory damages (US)                                                   | Statute of limitations 3 years from discovery; fair use analysis; safe harbor          |
| IP (Trademark C&D)                 | Lanham Act §§ 32/43; 15 U.S.C. § 1114                          | Laches; [VERIFY] demand to infringer; UK IP (Unjustified Threats) Act 2017                                                | Likelihood of confusion analysis; UK/AU unjustified threats exposure                   |
| IP (Patent C&D)                    | 35 U.S.C. §§ 271-287; UK Patents Act 1977; AU Patents Act 1990 | Patent marking for constructive notice (§ 287); UK/AU unjustified threats                                                 | Claim mapping required; willful infringement enhanced damages                          |
| Debt Collection                    | FDCPA 15 U.S.C. § 1692; Regulation F 12 C.F.R. Part 1006       | Validation notice within 5 days (§ 1692g); mini-Miranda (§ 1692e(11))                                                     | Time-barred debts; AU ACCC guideline; UK FCA CONC; Consumer Duty                       |
| Property Damage                    | State negligence/trespass/nuisance law                         | None generally; insurance notice requirements                                                                             | Diminished value (professional appraisal); betterment deduction; subrogation           |
| Professional Malpractice (Legal)   | State malpractice law; professional conduct rules              | Affidavit of merit (some states); [VERIFY]                                                                                | "Case within a case"; discovery rule for SOL; disgorgement of fees                     |
| Professional Malpractice (Medical) | State malpractice law                                          | Pre-suit notice (CCP § 364 CA; Fla. Stat. § 766.106 FL; 29 states expert affidavit)                                       | MICRA damages cap CA [VERIFY post-2023]; expert witness requirement                    |

---

## Severity Classification

Classify each demand letter across two dimensions:

### Dimension 1: Demand Defensibility (Legal Merit)

| Classification   | Criteria                                                                                                                                     | Action                                                                |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **DEFENSIBLE**   | All legal elements mapped; damages calculated and itemized; no ethical gates failed; jurisdiction confirmed; pre-suit requirements satisfied | Proceed; counsel may sign                                             |
| **ARGUABLE**     | Most elements mapped; some factual gaps; damages need supplemental support; no ethics issues                                                 | Proceed with additional notes for counsel; flag gaps                  |
| **MARGINAL**     | Weak factual support for one or more elements; damages speculative; novel legal theory                                                       | Hold pending additional investigation; consult counsel before sending |
| **UNACCEPTABLE** | Ethical gate failure (false representation, improper threat); legal elements not met; demand amount unsupportable                            | Do not send; redesign or decline matter                               |

### Dimension 2: Compliance Risk (Sending the Letter)

| Classification         | Criteria                                                                                                    | Consequence                            |
| ---------------------- | ----------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **COMPLIANT**          | All ethical gates passed; all statutory requirements for letter type met; proper format for jurisdiction    | Send as drafted after counsel review   |
| **ATTENTION REQUIRED** | Minor compliance gap; fixable before sending (e.g., add mini-Miranda; adjust tone; update calculation)      | Fix and re-review before sending       |
| **NON-COMPLIANT**      | FDCPA per se violation; CLRA pre-suit notice omitted; UK PAP materially deficient; unjustified threats risk | Stop; consult counsel; redesign letter |
| **DO NOT SEND**        | Ethical gate failure; demand constitutes extortion risk; false representations                              | Halt; escalate to supervising attorney |

---

## Prioritization Framework

For demand letters covering multiple claims or issues, prioritize:

**Tier 1 — Must Address (Prerequisite)**

- All statutory pre-suit requirements whose omission bars claims
- All FDCPA validation notice elements (per se violations if omitted)
- All UK PAP mandatory elements
- SOL warning if limitation approaching within 90 days

**Tier 2 — Core Legal Basis (Primary Demand)**

- The strongest, best-supported claim (highest confidence rating)
- The primary damages head (largest, most defensible amount)
- The specific relief demanded (injunction, payment, cessation)

**Tier 3 — Supporting and Amplifying Claims**

- Secondary claims that strengthen leverage (fee-shifting statutes)
- Pre-judgment interest
- Punitive or exemplary damages (if supported)
- Alternative remedies (declaratory relief, specific performance)

**Tier 4 — Preservation**

- Reservation of rights clause
- Preservation demand
- Reference to other claims not developed in the letter ("including but not limited to")

---

## Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                      | Fail Action                                                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, case, or established legal principle                              | Add citation or mark [UNVERIFIED]                                   |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction (Bluebook for US; OSCOLA for UK; AGLC for AU) | Fix format; use short-form after first citation                     |
| **Currency**   | Every cited statute confirmed as currently in force; no repealed provisions; FDCPA, PAP, ACL version confirmed current    | Flag [CHECK CURRENCY] for any statute with recent amendment history |
| **Domain**     | Analysis stays within the identified governing law; no jurisdiction bleed (e.g., applying FDCPA to UK debt collection)    | Remove or flag jurisdictional bleed                                 |
| **Confidence** | Uncertainty in legal analysis is explicitly stated, not hidden; [VERIFY] markers used for unconfirmed authority           | Add confidence qualifier; add [VERIFY]                              |

---

## Self-Interrogation for High-Severity Findings

For any item classified as **UNACCEPTABLE** (legal merit) or **DO NOT SEND** (compliance),
apply this three-pass adversarial review:

**Pass 1 — Legal Chain Integrity**: Does the legal analysis follow from the cited authority?
Would a court find the underlying claims well-grounded? Is there a plausible alternative
reading of the facts that supports a different legal conclusion?

**Pass 2 — Completeness**: Have all applicable statutory schemes been considered? Are there
pre-litigation requirements that have not been assessed? Could an FDCPA, ACL, or unjustified
threats issue have been overlooked?

**Pass 3 — Challenge**: What is the strongest argument against sending this demand? Under
what circumstances might a qualified attorney decline to sign this letter? What risk does
sending it create for the client beyond the immediate dispute?

---

## Confidence Scoring

| Level        | Range     | Meaning                                                      | Action                                   |
| ------------ | --------- | ------------------------------------------------------------ | ---------------------------------------- |
| **Definite** | 0.95-1.0  | Clear statutory authority; verified facts; no novel elements | State with full confidence               |
| **High**     | 0.80-0.94 | Strong authority; minor factual gaps                         | State with brief qualification           |
| **Probable** | 0.60-0.79 | Arguable basis; some missing documentation                   | Note gaps; recommend supplementation     |
| **Possible** | 0.40-0.59 | Novel theory or disputed facts                               | Flag for counsel; advise whether to send |
| **Unlikely** | 0.0-0.39  | Speculative basis or facts not established                   | Do not draft demand on this claim        |

---

## Glass Box Audit Trail

Include in the output package. Complete each field:

```yaml
glass_box:
  skill_name: "legalcode-demand-letter-drafter"
  mode: "Full Draft / Validation / Pre-Litigation Package"
  letter_type: "[General demand / Cease and desist / Cure demand / Statutory demand / FDCPA / Preservation notice]"
  dispute_types:
    - "[Primary: e.g., Breach of Contract]"
    - "[Secondary: e.g., Conversion]"
  governing_law: "[Jurisdiction and applicable law]"
  forum: "[Anticipated court or tribunal]"
  counterparty_profile: "[Sophisticated commercial / Individual / Government / Represented]"

  clarify_responses:
    letter_type: "[response]"
    jurisdiction: "[response]"
    counterparty_profile: "[response]"
    settlement_authority: "[response]"
    timing_pressures: "[response]"

  pre_suit_requirements:
    statute_of_limitations:
      expiry_date: "[date or 'more than 6 months']"
      tolling_applicable: "Yes / No — [basis]"
      sol_warning_included: "Yes / No"
    mandatory_pre_suit_steps:
      - "[requirement]: [SATISFIED / PENDING / NOT APPLICABLE / CRITICAL OMISSION]"

  ethical_gates:
    gate_1_criminal_threats: "PASS / FAIL — [notes]"
    gate_2_false_representations: "PASS / FAIL — [notes]"
    gate_3_represented_party: "PASS / N/A"
    gate_4_fdcpa_compliance: "PASS / FAIL / N/A — [notes]"
    gate_5_ip_unjustified_threats: "PASS / FAIL / N/A — [notes]"
    gate_6_tone: "PASS / ADVISORY — [notes]"

  damages_assessment:
    total_demand_amount: "$[amount]"
    damages_confidence: "[0.XX]"
    primary_heads_of_damage: "[list]"
    fee_shifting_statute: "[cite or N/A]"
    prejudgment_interest_rate: "[rate and statute or N/A]"

  settlement_framework:
    demand_anchor: "$[amount]"
    client_mas: "$[amount or 'not provided']"
    response_deadline: "[specific date]"
    without_prejudice_status: "WP labeled / WP save as to costs / Not labeled"
    calderbank_applicable: "Yes / No"

  demand_defensibility: "DEFENSIBLE / ARGUABLE / MARGINAL / UNACCEPTABLE"
  compliance_status: "COMPLIANT / ATTENTION REQUIRED / NON-COMPLIANT / DO NOT SEND"
  overall_confidence: "[0.XX]"

  legalcode_mcp: "Connected / Not connected"
  limitations:
    - "[Any scope limitations, assumptions made, items requiring further investigation]"
  reviewer: "AI-assisted — requires qualified legal review before sending"
```

---

## Anti-Patterns

What NOT to do when drafting or reviewing demand letters:

1. **Conditioning criminal prosecution on civil payment.** Threatening to file criminal
   charges against the respondent unless civil demands are met may constitute extortion under
   criminal law and violates California Rule 3.10 and the professional conduct rules of
   approximately eleven other US states. Even in jurisdictions without an express rule,
   this conduct violates the multi-rule framework (Model Rules 3.1/4.1/4.4). The line
   between describing potential criminal exposure and threatening to leverage it is fact-specific;
   always flag for counsel review.

2. **Omitting the FDCPA mini-Miranda warning.** Every initial written communication from
   a third-party debt collector to a consumer must include the § 1692e(11) disclosure.
   Omission is a per se FDCPA violation regardless of debt validity, exposing the collector
   to statutory damages of up to $1,000 per violation, actual damages, and attorney's fees.

3. **Failing to send the FDCPA § 1692g validation notice within 5 days.** The notice
   may appear in the initial communication or must be sent within five days. It is not
   optional. Collectors who send collection letters without the validation notice are
   strictly liable.

4. **Overshadowing FDCPA dispute rights during the 30-day window.** Any communication
   during the § 1692g 30-day dispute period that contradicts, minimizes, or obscures the
   consumer's right to dispute violates § 1692g(b). A follow-up demand letter sent during
   that window must not create urgency that overrides the dispute right.

5. **Sending a UK IP cease and desist letter without complying with the IP (Unjustified
   Threats) Act 2017.** A letter demanding that a party cease commercially using an
   allegedly infringing item falls outside the "permitted purpose" safe harbor and exposes
   the sender to a threats action — even if the underlying IP right is valid. Structure UK
   IP correspondence to notify of the right and request information, not to demand cessation.

6. **Sending an Australian IP cease and desist letter without a genuine legal basis.**
   Under Patents Act 1990 s. 128(1A), additional damages are available for blatant
   unjustified threats. Do not send unless the IP right is confirmed and the infringement
   analysis is completed by competent IP counsel.

7. **Demanding CLRA damages without first sending the § 1782 certified-mail notice.**
   California Civil Code § 1782 notice is a condition precedent to a CLRA damages claim.
   Filing suit for damages without the 30-day notice bars the damages claim entirely.
   Injunctive relief may still be available, but damages are forfeited.

8. **Filing a UK Employment Tribunal claim without completing ACAS early conciliation.**
   The ET1 form requires an ACAS Early Conciliation Certificate number. Without it, the
   claim is rejected. ACAS conciliation is mandatory regardless of whether a demand letter
   has been sent.

9. **Contacting a represented party directly.** If the respondent is known to have retained
   legal counsel, any demand letter must be sent to counsel of record, not to the respondent.
   Direct contact with a represented party without counsel's consent violates Model Rule 4.2
   (US), SRA Codes (UK), and equivalent Australian rules.

10. **Demanding pre-litigation attorney's fees without a statutory or contractual basis.**
    Under the American Rule, each party bears its own attorney's fees absent a contract,
    statute, or court order. Demanding "all attorney's fees and costs" in a demand letter
    without identifying the basis overstates the legal entitlement and undermines credibility.
    Cite the specific fee-shifting statute (FDCPA, Title VII, CLRA, ACL, etc.) or contract
    clause.

11. **Setting a demand amount that cannot be itemized.** A round-number demand without
    itemized calculation is a credibility red flag. Sophisticated respondents will immediately
    discount a non-itemized demand. Every head of damage should appear in a table with a
    calculation method and a source document or reference.

12. **Including punitive damages speculatively.** Punitive damages require clear and
    convincing evidence of fraud, malice, or oppression (US); the Rookes v. Barnard
    categories (UK); or proof of reprehensible conduct (AU). Asserting punitive damages
    without a factual basis invites dismissal of that claim in subsequent litigation and
    signals to the respondent that the demand is unreliable.

13. **Using inflammatory adjectives in place of legal analysis.** "Outrageous," "egregious,"
    and "fraudulent" without factual and legal support substitute emotion for argument.
    Professional demand letters let facts build the case; emotional language signals a weak
    legal position and invites dismissal.

14. **Failing to account for UCC cure rights before asserting breach.** In a sale-of-goods
    dispute, if the seller's contract time has not expired, the seller may have the right to
    cure non-conforming tender under UCC § 2-508. A demand letter that ignores this right
    may be premature, and a court may find that the buyer waived the breach by accepting
    substitute performance.

15. **Marking every demand letter "without prejudice" regardless of content.** A standard
    demand asserting full legal entitlement (not a compromise offer) does not benefit from
    a "without prejudice" label under FRE 408 or UK/AU common law. The label applies only
    to genuine settlement communications. Misapplication may confuse the privilege analysis
    later and does not provide absolute protection for factual assertions.

16. **Conflating the response deadline with the statute of limitations date.** A demand
    letter asking the respondent to respond within 14 days does not toll the statute of
    limitations. If the SOL is approaching, the letter must explicitly warn of the SOL date
    and note that suit will be filed by that date absent resolution, independently of the
    response deadline.

17. **Sending a demand letter and then allowing extended negotiations to run out the clock.**
    Demand letters do not generally toll the SOL in the US (absent specific statutory provision
    or agreement). If the respondent engages in protracted negotiations in bad faith, the
    claimant may lose their right to sue. File the complaint before the SOL expires, even if
    negotiations are ongoing.

18. **Omitting the reservation of rights clause.** A demand letter that specifies a total
    amount without reserving rights to claim additional damages, costs, and interest may be
    used by the opposing party to argue that all claims are encompassed in an accepted offer.
    Always include express reservation of all rights, claims, defenses, and remedies.

19. **Failing to identify the correct creditor in FDCPA letters.** If the debt has been
    assigned, the validation notice must identify both the current creditor to whom the
    debt is owed and, if different, the original creditor — in the validation notice text
    or upon request. Misidentifying the creditor is a § 1692e(2) violation.

20. **Demanding fees under a consumer protection statute without sending the pre-suit demand.**
    Massachusetts Chapter 93A § 9 requires a 30-day written demand to the respondent before
    filing suit. Failure to send this demand bars recovery of attorney's fees — which are
    otherwise mandatory for willful or knowing violations — even if the plaintiff prevails.

---

## Writing Standards

Apply these standards before delivering any demand letter draft:

1. **Numbered paragraphs**: All factual allegations must be in sequentially numbered
   paragraphs (e.g., ¶1, ¶2). This aids reference in subsequent litigation and demonstrates
   precision.

2. **Defined terms**: Introduce each defined term once (e.g., "XYZ Corp. (the 'Company')"),
   then use consistently throughout. Do not vary usage ("XYZ," "the company," "respondent").

3. **Exhibit references**: Every document referenced in the letter must have a corresponding
   exhibit designation (Exhibit A, B, etc.). The letter must be complete and self-referential
   with its enclosures.

4. **Specific dates and amounts**: Replace "approximately," "around," and "sometime in" with
   specific dates wherever possible. "On or about March 1, 2025" is acceptable only when the
   exact date cannot be determined.

5. **Active voice**: "XYZ failed to deliver the goods" not "The goods were not delivered."
   Active voice identifies the responsible party unambiguously.

6. **Demand letter ≠ complaint**: A demand letter is shorter, more persuasive, and less
   formally pleaded than a complaint. It presents the strongest version of the facts without
   exhaustive pleading of all elements. Save detailed element analysis for the complaint.

7. **Proportionate length**: General demands should be 1–4 pages. Complex multi-head claims
   may extend to 6–8 pages with exhibits. A demand letter that reads like a brief has lost
   its purpose.

8. **Plain-language discipline**: Replace legal jargon with plain language wherever possible
   (especially for letters to unrepresented parties). "You did not deliver the goods by the
   agreed date" is more effective than "Respondent's failure to tender conforming goods
   constituted an anticipatory repudiation of the contractual obligations."

9. **Quality gates before delivery**:
   - [ ] All ethical gates passed (Step 4)
   - [ ] All statutory elements for letter type included (Step 5)
   - [ ] Pre-suit requirements satisfied (Step 3)
   - [ ] Damages itemized and defensible (Step 6)
   - [ ] Response deadline is a specific date
   - [ ] Reservation of rights included
   - [ ] No inflammatory language
   - [ ] Citation quality gates run (above)

---

## External Tool Integration

**With legalcode-mcp connected (preferred)**:

- Search for current jurisdiction-specific statutes, regulations, and case law
- Verify statutory pre-suit notice requirements and current procedural rules
- Confirm FDCPA and Regulation F current version and effective date
- Verify UK PAP current version and practice direction updates
- Verify Australian legislation current consolidated text
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp (graceful degradation)**:

- Proceed using cited statutes and rules identified in this skill document
- Mark all statutory references with [VERIFY] pending confirmation
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Advise counsel to independently verify all cited statutory provisions before sending
- Focus enhancement efforts on structural quality and ethical compliance

**Companion skills to invoke**:

- `legalcode-damages-calculation` → For complex multi-head damages models exceeding 4 heads
- `legalcode-early-case-assessment` → If litigation viability is uncertain before sending demand
- `legalcode-litigation-hold-notice` → For companion preservation notice generation
- `legalcode-complaint-drafter` → After demand rejected; file formal pleading

---

## Localization Notes

This skill is designed to be jurisdiction-aware. When localizing for a specific jurisdiction:

**United States — California Focus**:

- Mandatory: CLRA § 1782 (consumer), PAGA § 2699.3 (labor), CCP § 364 (malpractice)
- Professional conduct: Rule 3.10 (express prohibition on criminal threats)
- Without-prejudice: Evid. Code § 1152; label demand letters for settlement purposes explicitly
- Interest: Cal. Civ. Code § 3289 (contract 10%; tort 7%)
- Time-limited demands: CCP § 999 et seq. (insurance, effective January 1, 2023)

**England & Wales**:

- Mandatory: Comply with applicable Pre-Action Protocol; use PAP forms for debt claims
- IP: Apply IP (Unjustified Threats) Act 2017 safe harbor analysis for all IP C&D letters
- Employment: ACAS early conciliation mandatory; send demand before ACAS certificate issued
- Without-prejudice: Mark Calderbank offers "WITHOUT PREJUDICE SAVE AS TO COSTS"
- Costs: 2024 CJC Phase Two recommendations — reference ADR in all pre-action correspondence
- Interest: Late Payment of Commercial Debts (Interest) Act 1998 (8% over BoE base) for commercial debts

**Australia**:

- Federal civil: Civil Dispute Resolution Act 2011 — genuine steps to resolve required
- IP: Apply Patents Act 1990 s. 128 / Trade Marks Act 1995 s. 129 analysis for all IP C&D
- Debt collection: Apply ACCC/ASIC Debt Collection Guideline April 2021 standards
- Consumer: ACL s. 18 misleading/deceptive conduct analysis for all demand communications
- Calderbank: Mark "WITHOUT PREJUDICE SAVE AS TO COSTS"; genuine compromise required
- Interest: [VERIFY current pre-judgment interest rate in applicable state/territory]

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis from 2-agent research pipeline:

- **Agent 1 (Structural Analyst)**: Analyzed `legalcode-complaint-drafter`,
  `legalcode-litigation-risk-assessment`, `legalcode-settlement-negotiation`, and
  `legalcode-damages-calculation` for structural patterns, workflow design, and quality
  framework elements.

- **Agent 2 (Legal Research)**: Conducted multi-query web research covering FDCPA and
  Regulation F (2021), professional conduct ethical rules on threatening criminal prosecution,
  UK Pre-Action Protocol framework and 2024 CJC recommendations, Australian ACL and ACCC
  Debt Collection Guideline, EEOC exhaustion requirements, CLRA § 1782, PAGA § 2699.3,
  UCC cure rights, IP (Unjustified Threats) Act 2017, Australian Patents Act s. 128 and
  Trade Marks Act s. 129, without-prejudice privilege across all three jurisdictions,
  California time-limited demand statute (CCP § 999 et seq.), and professional malpractice
  pre-suit requirements.

Key legal authority incorporated: 15 U.S.C. § 1692 et seq. (FDCPA); 12 C.F.R. Part 1006
(Regulation F 2021); ABA Model Rules 3.1/4.1/4.2/4.4; California Rule 3.10; Cal. Civ. Code
§ 1782 (CLRA); Cal. Lab. Code § 2699.3 (PAGA); CCP § 364 (medical malpractice); IP
(Unjustified Threats) Act 2017; Patents Act 1990 (Cth) s. 128; Trade Marks Act 1995 (Cth)
s. 129; ACCC/ASIC Debt Collection Guideline April 2021; ACL s. 18 (Cth); CPR Pre-Action
Protocols and Practice Direction (England & Wales); FRE Rule 408; Calderbank v Calderbank
[1975] All ER 333; Rush & Tompkins Ltd v Greater London Council [1989] AC 1280.

Attribution: Legalcode original synthesis. No external skill was imported.
