---
name: legalcode-evidence-admissibility-analysis
description: Analyze evidence admissibility under the Federal Rules of Evidence with rule-by-rule assessment
  for trial preparation, motions in limine, and evidentiary objection strategy. Use when evaluating whether
  specific evidence items can be admitted at trial, preparing motions in limine to exclude opposing evidence,
  anticipating evidentiary objections and building responses, assessing privilege claims before disclosure,
  analyzing hearsay and identifying applicable exceptions, evaluating expert witness qualification under
  Daubert or Frye, building foundation requirements checklists for any evidence type, or challenging expert
  methodology under the post-2023 FRE 702 preponderance standard.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Analyze evidence admissibility under the Federal Rules of Evidence with rule-by-rule assessment for trial preparation, motions in limine, and evidentiary objection strategy. Use when evaluating whether specific evidence items can be admitted at trial, preparing motions in limine to exclude opposing evidence, anticipating evidentiary objections and building responses, assessing privilege claims before disclosure, analyzing hearsay and identifying applicable exceptions, evaluating expert witness qualification under Daubert or Frye, building foundation requirements checklists for any evidence type, or challenging expert methodology under the post-2023 FRE 702 preponderance standard. Covers FRE Articles I–XI: judicial notice (FRE 201); relevance and FRE 403 balancing (FRE 401–403); character evidence and prior bad acts (FRE 404–406); subsequent remedial measures, settlement offers, medical payments, pleas, and insurance (FRE 407–411); privilege including attorney-client, work product, spousal, and executive privilege with FRE 502 inadvertent-waiver clawback (FRE 501–502); competency and impeachment including prior convictions (FRE 601–609); lay and expert opinion testimony including full Daubert four-factor test, Joiner, Kumho Tire, and post-2023 preponderance standard (FRE 701–706); hearsay definition, non-hearsay admissions under 801(d), all 23 Rule 803 exceptions, Rule 804 unavailability exceptions, and Rule 807 residual exception (FRE 801–807); authentication and identification including digital and electronic evidence, self- authenticating documents, and 2017 FRE 902(13)–(14) electronic certification (FRE 901–903); and best evidence rule for originals, duplicates, and summaries (FRE 1001–1008). Incorporates the December 1, 2020 FRE 404(b) criminal notice amendment and December 1, 2023 FRE 702 preponderance clarification amendment. Produces ADMISSIBLE / LIKELY ADMISSIBLE / CONTESTED / LIKELY INADMISSIBLE / INADMISSIBLE per-item classification with objection/response pairs, motion in limine recommendations, foundation requirement checklists, alternative admissibility theories, and confidence- scored Glass Box audit trail.


# Legalcode Evidence Admissibility Analysis

> **Disclaimer**: This skill provides a framework for AI-assisted evidence admissibility
> analysis under the Federal Rules of Evidence. It does not constitute legal advice. All
> outputs must be reviewed, verified, and acted upon only by qualified legal counsel
> licensed in the relevant jurisdiction. Evidentiary rulings are highly fact-sensitive and
> court-specific; the analysis produced here is a structured starting point for attorney
> review, not a substitute for it. Statutory and case law citations carry hallucination
> risk — every case name, citation, and rule interpretation must be verified against
> authoritative sources before reliance. Filing a motion in limine based on AI-generated
> analysis without independent verification violates counsel's professional responsibility
> and may constitute a Rule 11 breach.

---

## Purpose and Scope

This skill performs systematic, rule-by-rule evidence admissibility analysis under the
Federal Rules of Evidence (FRE). It operates in two modes:

1. **Proponent Mode**: Build the admissibility case for evidence the user wants to admit
   — identify foundation requirements, anticipate objections, and prepare responses.

2. **Opponent Mode**: Challenge admissibility of evidence the opposing party seeks to
   admit — identify viable objection grounds, assess motion in limine strategy, and
   predict judicial discretion outcomes.

**Covers:**

- Full FRE Article analysis: FRE 201 (judicial notice); FRE 401–403 (relevance); FRE
  404–406 (character/prior acts); FRE 407–411 (policy exclusions); FRE 501–502
  (privilege); FRE 601–609 (competency and impeachment); FRE 701–706 (opinion
  testimony); FRE 801–807 (hearsay); FRE 901–903 (authentication); FRE 1001–1008
  (best evidence)
- Per-item admissibility classification (five-tier scale)
- Objection/response pairs for each applicable rule
- Motion in limine recommendations with timing and strategy
- Foundation requirement checklists per evidence type
- Alternative admissibility theories when primary theory fails
- Expert testimony qualification under Daubert/Joiner/Kumho Tire and post-2023 FRE 702
- Hearsay exception identification across all 37 FRE provisions
- Privilege analysis including FRE 502 inadvertent-waiver protection
- Digital/electronic evidence authentication under FRE 902(13)–(14)

**Does not:**

- Analyze state evidence rules (California Evidence Code, New York CPLR, etc.) — though
  it notes where federal rules diverge from common state approaches
- Address constitutional admissibility issues (Confrontation Clause under Crawford v.
  Washington, 541 U.S. 36 (2004); Fourth Amendment suppression; Fifth Amendment
  compelled production) — flag these separately for constitutional analysis
- Replace qualified counsel's independent professional judgment
- Constitute a Rule 11 certification of any argument

**Related skills:**

- `legalcode-privilege-review` — deeper privilege log workflow and TAR integration
- `legalcode-deposition-digest` — preparing impeachment evidence from depositions
- `legalcode-discovery-request-drafter` — FRE 901/902 authentication planning at
  discovery stage

---

## Jurisdiction and Governing Law

This skill analyzes evidence under the **Federal Rules of Evidence**, which apply in all
United States federal courts. The FRE was enacted by Congress in 1975 and is administered
by the Judicial Conference of the United States. Amendments are promulgated by the Supreme
Court under the Rules Enabling Act (28 U.S.C. § 2072) and take effect December 1 each
year unless Congress acts.

**Critical jurisdiction limitation**: Many states follow the FRE closely (adopting
"identical," "amended," or "similar" codifications) but many diverge on key rules:

[JURISDICTION-SPECIFIC] When the case is in state court, always verify:

- Whether the state follows the federal hearsay exceptions or has its own (e.g., New
  York's patchwork common-law rules differ significantly from FRE 803)
- Whether Daubert or Frye applies — approximately 30 states still use Frye general
  acceptance test; check current state approach [VERIFY per state]
- Whether the state has adopted FRE 502 analog for privilege waiver or still uses older
  common-law inadvertent disclosure standards
- Whether the state has its own character evidence rules (particularly for sexual assault
  cases — FRE 412–415 has no universal state analog)
- Whether state privilege law applies (in federal diversity cases, FRE 501 requires
  applying state privilege law for state-law claims)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. The evidentiary
analysis changes fundamentally based on:

- Whether the case is civil or criminal (different character evidence rules, beyond
  reasonable doubt vs. preponderance standard, prosecutorial special obligations)
- Which side is requesting the analysis (proponent vs. opponent mode)
- Procedural posture (pre-trial motion in limine, trial objection, appellate issue
  preservation)
- Whether privilege applies (if privileged, further analysis is moot)

Use the **⟁ CLARIFY** pattern (structured options with descriptions) wherever marked
below. If the user has already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept Evidence Input

Accept evidence descriptions in any format:

- **Evidence list**: Numbered list of evidence items with brief descriptions
- **Trial exhibit log**: Exhibit numbers, descriptions, and anticipated use
- **Discovery materials**: Documents, ESI, depositions, physical evidence
- **Expert witness description**: Expert's name, field, opinion, and methodology
- **Free text**: Description of one or more evidence items with context

For each evidence item, capture:

- What the item is (document, testimony, object, photograph, recording, ESI, etc.)
- Who created or generated it, and when
- Its anticipated use at trial (what fact it tends to prove)
- Whether it is offered for the truth of the matter asserted (hearsay trigger)

If an item's description is ambiguous, note the ambiguity and apply the analysis to the
most plausible interpretation, stating assumptions explicitly.

### Step 2: Gather Litigation Context

**⟁ CLARIFY** — Before analyzing, ask the user these questions (skip any already answered):

1. **Case type**: Civil or criminal?
   - Options: **Federal civil** (FRCP rules apply), **Federal criminal** (different
     character evidence rules apply to defendant and alleged victim; Crawford implicates
     hearsay), **Mixed/unclear**
   - _Why this matters_: Character evidence rules (FRE 404–405), the hearsay exception
     for dying declarations, and the prosecution's FRE 404(b) notice obligation all differ
     between civil and criminal. Crawford v. Washington, 541 U.S. 36 (2004) [VERIFY]
     restricts testimonial hearsay in criminal cases regardless of FRE exceptions.

2. **Your side**: Proponent or opponent of the evidence?
   - Options: **Proponent** (seeking admission — build foundation, answer objections),
     **Opponent** (seeking exclusion — identify objection grounds, draft MIL), **Both**
     (assess from both sides for settlement or stipulation purposes)
   - _Why this matters_: The entire analytical frame flips. Proponent mode builds the
     case for admissibility; opponent mode finds exclusion grounds.

3. **Procedural posture**: When does this analysis need to support action?
   - Options: **Pre-trial motion in limine**, **Trial objection prep** (anticipate
     in-the-moment objections), **Mid-trial objection** (specific ruling pending),
     **Appellate issue** (was error preserved and was it prejudicial?), **Discovery
     planning** (authentication strategy for documents before production)
   - _Why this matters_: Motion in limine analysis requires different output than a
     trial objection list. Appellate analysis requires assessing harmless error and
     whether objection was properly preserved.

4. **Number of evidence items**: How many items need analysis?
   - Options: **Single item** (deep analysis), **Small set (2–10)** (per-item analysis),
     **Large set (11+)** (prioritize most contested, categorical treatment for remainder)
   - _Why this matters_: For large evidence sets, full per-item analysis is impractical.
     Offer categorical analysis for obviously admissible items, deep analysis for contested ones.

5. **Expert testimony involved?**
   - Options: **Yes — need Daubert/702 analysis**, **No expert issues**, **Uncertain**
   - _Why this matters_: FRE 702 analysis requires separate Daubert gatekeeping
     framework distinct from general admissibility analysis.

### Step 3: Privilege Screen (Always First)

**Before any other analysis**, run a privilege screen for each evidence item. Privilege
is an absolute bar — if privilege applies and has not been waived, the item is inadmissible
regardless of relevance or any other FRE provision.

For each item, assess:

**Attorney-Client Privilege** (FRE 501; federal common law)

- Is it a confidential communication?
- Between attorney and client (or their agents)?
- Made for the purpose of seeking or giving legal advice?
- Was confidentiality maintained? (no unnecessary third-party disclosure)
- Has there been waiver? (express, implied, or by FRE 502(b) inadvertent disclosure analysis)

**Work Product Protection** (FRCP 26(b)(3); Hickman v. Taylor, 329 U.S. 495 (1947) [VERIFY])

- Prepared in anticipation of litigation or for trial?
- By or for a party or its representative?
- Opinion work product (mental impressions, conclusions, strategies) — near-absolute protection
- Ordinary work product — overcome by substantial need and undue hardship

**Spousal Privilege** (FRE 501; federal common law)

- Adverse spousal testimony privilege: criminal cases; holder is defendant-spouse
- Marital communications privilege: civil and criminal; communication must be confidential;
  either spouse holds in most federal jurisdictions [JURISDICTION-SPECIFIC][VERIFY]

**Other Recognized Privileges** (FRE 501 — federal common law)

- Psychotherapist-patient privilege (Jaffee v. Redmond, 518 U.S. 1 (1996) [VERIFY])
- Fifth Amendment — self-incrimination (constitutional, not FRE)
- Executive/governmental privilege — qualified [VERIFY in applicable circuit]
- Priest-penitent, journalist shield (recognized in many circuits, not universally) [VERIFY]

**FRE 502 Inadvertent Disclosure Analysis** (if item was produced in discovery)

- Did the holder take reasonable steps to prevent disclosure?
- Did the holder take prompt reasonable steps to rectify the error?
- Is there a FRE 502(d) court order protecting against waiver?
- Lubrizol v. IBM (2024) [VERIFY] — ongoing question of whether 502(d) orders cover
  intentional disclosures

**⟁ CLARIFY** — If a privilege issue is identified:

- "I've identified a potential attorney-client privilege claim over [item]. Has this
  privilege been formally asserted? Was there a FRE 502(d) protective order in place
  during discovery? Was the document voluntarily produced or produced inadvertently?"

If privilege applies and is not waived → classify as **INADMISSIBLE (PRIVILEGE)** and
stop further analysis for that item. Note what would be needed to assert or waive the
privilege.

### Step 4: Relevance Gate (FRE 401–402)

For each non-privileged item, apply the relevance threshold:

**FRE 401 Test**: Does the evidence have **any tendency** to make a fact of consequence
in determining the action more or less probable than it would be without the evidence?

- This is a **low bar** — courts apply FRE 401 permissively
- The fact must be "of consequence" — connected to a claim or defense actually in dispute
- Both direct and circumstantial evidence can be relevant
- Relevance is assessed from the evidence's **anticipated use**, not the item in isolation

**FRE 402**: Relevant evidence is generally admissible; irrelevant evidence is not.

If FRE 401 is not satisfied → classify as **INADMISSIBLE (IRRELEVANT)** and flag whether
the item might become relevant if additional foundation is established.

### Step 5: FRE 403 Balancing

Even if relevant, evidence may be excluded if:

> The probative value is **substantially outweighed** by the danger of:
>
> - Unfair prejudice
> - Confusing the issues
> - Misleading the jury
> - Undue delay
> - Wasting time
> - Needlessly presenting cumulative evidence

**Key FRE 403 principles:**

- The "substantially outweighed" standard favors admission — the opponent bears a
  significant burden to exclude under FRE 403
- _Old Chief v. United States_, 519 U.S. 172 (1997) [VERIFY]: Courts may consider
  alternative means of proving the same fact when assessing probative value
- "Unfair prejudice" means prejudice that is _undue_ — evidence that is merely
  damaging to the opponent does not meet the standard
- Jury limiting instructions can reduce, but not eliminate, prejudice

**⟁ CLARIFY** — FRE 403 is inherently discretionary:

- "This evidence may trigger a FRE 403 objection. Do you want me to assess the strength
  of a FRE 403 motion to exclude, or focus on strengthening the probative value argument
  to defeat the objection?"

### Step 6: Specific Categorical Rules (FRE 404–415; FRE 407–411)

Apply applicable categorical exclusions after the relevance screen:

#### Character Evidence (FRE 404–406)

**FRE 404(a) — General Prohibition**
Character evidence is generally inadmissible to prove conduct in conformity therewith.

**FRE 404(a) Exceptions (Criminal):**

- Defendant may offer evidence of defendant's own pertinent trait; prosecution may rebut
- Defendant may offer evidence of alleged victim's pertinent trait; prosecution may
  rebut and may offer same trait of defendant
- FRE 608–609 govern character evidence of witnesses

**FRE 404(b) — Other Crimes, Wrongs, or Acts**

- Not admissible to prove propensity
- Admissible for other purposes: MIIMOKAP (Motive, Intent, Identity, Mistake/accident
  (absence of), Opportunity, Knowledge, Absence of mistake/accident, Plan/preparation)
- **December 1, 2020 Amendment (Criminal)**: Prosecution must provide reasonable written
  notice before trial identifying (1) the specific 404(b) evidence, (2) the permitted
  purpose, and (3) the reasoning supporting that purpose. Notice is required without
  a defense request. Defense need not request it.
- In civil cases: No equivalent mandatory notice requirement

**FRE 405 — Methods of Proving Character**

- When character evidence is admissible: reputation or opinion evidence
- When character is "in issue" (an essential element of a claim or defense): also specific
  instances of conduct

**FRE 406 — Habit Evidence**

- Evidence of habit or routine practice is admissible to prove conduct on a specific
  occasion was in conformity with the habit
- Admissible regardless of eyewitness corroboration; does not require foundation of
  more than one instance (unlike 404(a) character)

#### Policy-Based Exclusions (FRE 407–411)

**FRE 407 — Subsequent Remedial Measures**

- Not admissible to prove negligence, culpable conduct, defect, or need for warning
- Admissible for: impeachment (if opponent claims no feasible precaution existed),
  proving ownership or control, proving feasibility of precautionary measures if disputed
- Manufacturer's post-accident redesign is the paradigm exclusion

**FRE 408 — Compromise Offers and Negotiations**

- Not admissible to prove or disprove validity or amount of a disputed claim
- Covers: settlement offers, settlement agreements, and statements made during
  compromise negotiations
- Admissible for: proving bias or prejudice of a witness, negating contention of
  undue delay, proving obstruction of criminal investigation or prosecution
- Note: FRE 408 applies only when there is a disputed claim — not every negotiation

**FRE 409 — Offers to Pay Medical Expenses**

- Not admissible to prove liability
- Does NOT protect accompanying admissions from other inadmissible-admission rules;
  narrower protection than FRE 408

**FRE 410 — Pleas, Plea Discussions, and Related Statements**

- Not admissible against a defendant: withdrawn guilty plea, nolo contendere plea,
  statement made during federal Rule 11 plea proceedings, statement made during plea
  discussions with prosecution resulting in no guilty plea or in withdrawn guilty plea
- Exception: when defendant introduces part of the statement and fairness requires
  completing it, or in perjury/false statement prosecution where defendant made
  the statement under oath, on the record, and counsel was present

**FRE 411 — Insurance Coverage**

- Existence or absence of liability insurance not admissible to prove negligence or
  wrongful conduct
- Admissible for: bias or prejudice, agency, ownership, control

**FRE 412 — Sex Offense Cases; Victim's Sexual Behavior or Predisposition**

- In civil and criminal sex offense cases: evidence offered to prove victim's sexual
  predisposition is generally inadmissible
- Criminal exceptions: specific instances admissible to prove another person was the
  source of physical evidence, or to prove consent (with pretrial hearing requirement)
- Civil cases: additional balancing test required — probative value must substantially
  outweigh harm to victim [JURISDICTION-SPECIFIC in some states]

**FRE 413–415 — Prior Sexual Assault and Child Molestation Acts**

- Defendant's commission of prior similar offense is admissible in sexual assault (413),
  child molestation (414), and civil sex cases (415)
- These are significant exceptions to FRE 404(b)'s propensity bar
- Notice requirement: disclose at least 15 days before trial

### Step 7: Hearsay Analysis (FRE 801–807)

Hearsay analysis involves three sequential questions:

**Question 1: Is the statement hearsay?**

- A **statement** is an oral or written assertion, or nonverbal conduct intended as
  an assertion (FRE 801(a))
- **Hearsay** = an out-of-court statement offered to prove the truth of the matter
  asserted (FRE 801(c))
- If offered for a non-truth purpose, it is not hearsay: effect on listener, verbal
  act (operative words of defamation, contract formation, etc.), circumstantial
  evidence of declarant's state of mind, legally operative words

**Question 2: Does a non-hearsay exemption apply?**
FRE 801(d) treats certain statements as not hearsay:

_Prior statements of witnesses_ (FRE 801(d)(1)):

- (A) Prior inconsistent statement: made under oath at prior proceeding, offered to
  prove the truth of the matter asserted
- (B) Prior consistent statement: offered to rebut charge of fabrication/improper
  influence or motive (must have been made before the alleged motive arose)
- (C) Prior identification: identification of a person after perceiving them

_Opposing party's statements_ (FRE 801(d)(2)):

- (A) The party's own statement (classic admission)
- (B) Adoptive admission: party manifested adoption or belief in the statement
- (C) Authorized admission: statement by person authorized to make such statement
- (D) Agent/employee admission: statement on matter within scope of agency/employment
  during relationship
- (E) Co-conspirator statement: made during and in furtherance of the conspiracy
  (Bourjaily v. United States, 483 U.S. 171 (1987) [VERIFY])

**Question 3: Does a hearsay exception apply?**

_FRE 803 — Exceptions (Declarant's availability immaterial):_
| # | Exception | Key Requirements |
|---|-----------|-----------------|
| 803(1) | Present sense impression | Statement while or immediately after perceiving event |
| 803(2) | Excited utterance | Startling event; made while under stress of excitement |
| 803(3) | Then-existing mental/emotional/physical condition | State of mind (not memory/belief to prove fact) |
| 803(4) | Medical diagnosis/treatment | Made for purpose of diagnosis; pertinent to treatment |
| 803(5) | Recorded recollection | Witness once knew, now can't recall; made when fresh |
| 803(6) | Business records | Regular activity; made near time by person with knowledge; kept in ordinary course; foundation via custodian or qualified witness (or FRE 902(11)–(12) certification) |
| 803(7) | Absence of business record | Matters not regularly recorded show nonoccurrence |
| 803(8) | Public records | Government office; matters in scope of duty; not police reports for criminal defendants [VERIFY circuit law on scope] |
| 803(9) | Vital statistics | Births, deaths, marriages in official records |
| 803(10) | Absence of public record | Cert. that diligent search failed to disclose |
| 803(11) | Religious organization records | Personal/family history |
| 803(12) | Marriage/baptism certificates | Made by officiating clergy |
| 803(13) | Family records | Bibles, genealogies, engravings on urns |
| 803(14) | Documents affecting property interest | Recitals in deeds, etc. |
| 803(15) | Statements in property documents | Part of document affecting an interest |
| 803(16) | Ancient documents | Authenticated document at least 20 years old [Note: 2017 amendment requires document created before Jan. 1, 1998, to preserve exception for ESI] |
| 803(17) | Market reports/commercial publications | Market quotations, tabulations, etc. |
| 803(18) | Learned treatises | Established as reliable; relied on by expert or called to attention on cross |
| 803(19) | Reputation: personal/family history | Among family members or in community |
| 803(20) | Reputation: land boundaries/community history | Before controversy arose |
| 803(21) | Reputation: character | In community |
| 803(22) | Judgment: prior conviction | Felony conviction offered to prove fact essential to judgment; not against criminal defendant if prosecution's evidence [VERIFY] |
| 803(23) | Judgment: personal/family history | Judgment as proof of matters necessarily decided therein |

_FRE 804 — Exceptions (Declarant must be unavailable):_

Unavailability (FRE 804(a)) includes: claim of privilege, refusal to testify despite
court order, lack of memory (genuinely), death or physical/mental illness, and absence
from hearing when proponent could not procure attendance through reasonable means.

| #         | Exception                            | Key Requirements                                                                                                                                                             |
| --------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 804(b)(1) | Former testimony                     | Testimony at prior hearing/deposition; party against whom offered (or predecessor in interest) had opportunity and similar motive to develop                                 |
| 804(b)(2) | Dying declaration                    | Statement under belief of imminent death; only in civil and homicide cases in federal courts [Note: more limited than state analogs]                                         |
| 804(b)(3) | Statement against interest           | Against declarant's pecuniary, proprietary, civil, or penal interest when made; corroborating circumstances required for statements exposing declarant to criminal liability |
| 804(b)(4) | Statement of personal/family history | Declarant's own birth, adoption, legitimacy, etc.                                                                                                                            |
| 804(b)(6) | Forfeiture by wrongdoing             | Party engaged in or acquiesced in wrongdoing to make declarant unavailable                                                                                                   |

_FRE 807 — Residual Exception:_

- Statement not specifically covered by 803 or 804
- Supported by sufficient guarantees of trustworthiness (totality of circumstances +
  corroborating evidence considered)
- More probative on the point than other evidence the proponent can obtain through
  reasonable efforts
- Proponent must give adverse party reasonable notice before trial (including substance
  and declarant's name/address if known)
- Use sparingly — courts construe narrowly

**Double hearsay (FRE 805)**

- Each level of hearsay must independently satisfy an exception
- Example: Business record (803(6)) containing statement of employee's recollection
  of customer's statement requires an exception for the customer's statement too

**Crawford and the Confrontation Clause (Criminal Cases)**
[JURISDICTION-SPECIFIC — Constitutional overlay]:
Even if a hearsay exception applies, admission of **testimonial** hearsay against a
criminal defendant without opportunity for cross-examination may violate the Sixth
Amendment Confrontation Clause under _Crawford v. Washington_, 541 U.S. 36 (2004) [VERIFY].
Testimonial statements include: formal police interrogations, affidavits, and statements
to police when the primary purpose is to establish or prove past events for prosecution.
Non-testimonial statements (e.g., 911 calls during ongoing emergency) are not barred.
Flag Crawford issues separately — they require constitutional analysis beyond the FRE.

### Step 8: Authentication and Best Evidence (FRE 901–903; FRE 1001–1008)

#### Authentication (FRE 901–902)

Every item of evidence must be authenticated — the proponent must produce evidence
sufficient to support a finding that the item is what the proponent claims it is.

**FRE 901(b) Authentication Methods:**
| Method | How |
|--------|-----|
| Testimony of witness with knowledge | Witness testifies item is what it's claimed to be |
| Nonexpert handwriting opinion | Familiarity acquired before litigation |
| Expert comparison | Comparison with authenticated specimen |
| Distinctive characteristics | Appearance, contents, internal patterns, circumstances |
| Opinion about voice | Familiarity, telephone circumstances |
| Telephone evidence | Calls placed, voice recognized, or self-identification |
| Public records | Filed or recorded in public office as authorized by law |
| Ancient documents | At least 20 years old, in expected custody, no suspicious alterations |
| Process or system | Computer/process produces accurate result (explain the process) |
| Statute or rule | Any method provided by federal statute or other FRE |

**FRE 902 Self-Authenticating Documents** (no extrinsic evidence required):

- Domestic public documents under seal (902(1))
- Domestic public documents signed by officer, no seal required (902(2))
- Foreign public documents with certification (902(3))
- Certified copies of public records (902(4))
- Official publications of government (902(5))
- Newspapers and periodicals (902(6))
- Trade inscriptions (902(7))
- Acknowledged instruments (902(8))
- Commercial paper (902(9))
- Certified domestic records of regularly conducted activity (902(11))
- Certified foreign records (902(12))
- **Certified electronic records (902(13))**: Record generated by electronic process or
  system that produces accurate result (added December 1, 2017)
- **Certified data from electronic device/storage (902(14))**: Data copied from electronic
  device, storage medium, or file (added December 1, 2017)

**Digital and Social Media Evidence — Foundation Requirements:**
Social media posts, text messages, emails, and website content require authentication showing
the purported author actually created them. Circumstantial foundation methods include:

- Metadata (sender's email address, phone number, IP address)
- Content of the communication (references to private facts known only to the sender)
- Other messages in the same thread
- Distinctive writing style or idiosyncrasies
- Witness testimony about the account

[VERIFY current circuit law on social media authentication standards — courts have
developed case-specific approaches]

#### Best Evidence Rule (FRE 1001–1008)

**FRE 1002**: To prove the content of a writing, recording, or photograph, the
original must be offered.

**FRE 1003**: A duplicate (exact copy by any means) is admissible to the same extent
as the original unless there is a genuine question about the original's authenticity or
it would be unfair to admit the duplicate.

**FRE 1004**: Admissibility of other evidence of content (secondary evidence) when:

- Original is lost or destroyed (not due to proponent's bad faith)
- Original cannot be obtained by judicial process
- Original in the opponent's possession and opponent was put on notice but did not produce it
- The writing, recording, or photograph is not closely related to a controlling issue

**Practical note on ESI**: Courts increasingly recognize that electronically stored
information is frequently available only in duplicate form (copies, backups). The best
evidence rule applies to ESI but is usually satisfied by certified copies under FRE 902(13)–(14).

### Step 9: Opinion Testimony Analysis (FRE 701–706)

#### Lay Opinion (FRE 701)

Lay witness opinion is admissible only if:

- (a) Rationally based on the witness's perception
- (b) Helpful to clearly understanding the witness's testimony or determining a fact in issue
- (c) **Not based on scientific, technical, or other specialized knowledge** within the
  scope of FRE 702

Common lay opinion examples: speed of a vehicle, sobriety, emotional state, identity
of handwriting, value of the witness's own property, similarity of voice. Courts have
held that "skilled lay witness" opinions (e.g., business owner on lost profits) may be
admitted under FRE 701 in some circuits but FRE 702 in others. [VERIFY circuit law]

#### Expert Testimony (FRE 702 — as amended December 1, 2023)

The 2023 amendment clarified that the court must **actually determine** (not merely find
plausible) that the admissibility requirements are met by a **preponderance of evidence**:

A witness qualified as an expert may testify if:

1. The expert's scientific, technical, or other specialized knowledge will help the trier
   of fact understand evidence or determine a fact in issue
2. The testimony is **based on sufficient facts or data**
3. The testimony is **the product of reliable principles and methods**
4. The expert's opinion **reflects a reliable application** of the principles and methods
   to the facts of the case

**The proponent must demonstrate each element by a preponderance of the evidence.**
The 2023 amendment was intended to overturn cases that applied an overly permissive
standard of "plausibility" for expert admissibility.

**Daubert Gatekeeping Framework** (_Daubert v. Merrell Dow Pharmaceuticals, Inc._,
509 U.S. 579 (1993) [VERIFY]):

The trial court acts as gatekeeper. Factors for assessing reliability (non-exhaustive):

1. **Testability**: Whether the theory or technique can be (and has been) tested
2. **Peer review and publication**: Whether the theory has been subjected to peer review
3. **Known error rate**: The known or potential rate of error; standards controlling operation
4. **General acceptance**: Whether the methodology is generally accepted in the relevant
   scientific community (_Frye_ standard, now one factor among several)

Additional _Daubert_ principles:

- **General Electric Co. v. Joiner**, 522 U.S. 136 (1997) [VERIFY]: Appellate review
  is abuse of discretion; conclusions must flow from methodology ("analytical gap" doctrine)
- **Kumho Tire Co. v. Carmichael**, 526 U.S. 137 (1999) [VERIFY]: Daubert gatekeeping
  extends to technical and other specialized knowledge, not just science

**Common Daubert Challenge Bases:**

- Expert failed to test the specific hypothesis relevant to the case
- Methodology not used outside litigation context
- Conclusion not supported by cited studies (analytical gap)
- Expert cherry-picked data or ignored contrary evidence
- Error rate unknown or unacceptably high
- Opinion inconsistent with expert's own prior publications

**Expert Qualification** under FRE 702 — knowledge, skill, experience, training,
or education. Deficiencies in formal credentials may be compensated by practical experience;
courts rarely exclude on qualifications alone if some basis exists.

**Court-Appointed Experts** (FRE 706): Court may appoint neutral expert on its own
or on motion; appointed expert must advise parties of opinion in writing and may be
deposed; compensation determined by court.

### Step 10: Judicial Notice and Additional Rules (FRE 201; FRE 601–609)

#### Judicial Notice (FRE 201)

- Applies to **adjudicative facts** only (not legislative facts used in rulemaking)
- A fact must be: (1) generally known within the trial court's jurisdiction, or (2)
  accurately and readily determined by resort to sources whose accuracy cannot reasonably
  be questioned
- Court **must** take judicial notice if a party requests and supplies necessary information
- Court **may** take notice on its own
- **Criminal cases**: Jury may, but is not required to, accept noticed fact as conclusive
- **Civil cases**: Jury must accept noticed fact as conclusive
- Common examples: calendar dates, geographic facts, court records, government publications

#### Competency (FRE 601–606)

- FRE 601: Every person presumed competent to be a witness
- **In federal diversity cases**: state law governs competency for state-law claims
- FRE 602: Witness must have personal knowledge (unless expert)
- FRE 605: Presiding judge incompetent to testify
- FRE 606: Juror incompetent to testify about deliberations (with narrow exceptions for
  extraneous information or outside influence affecting the verdict)

#### Impeachment (FRE 607–609)

- FRE 607: Any party, including party calling witness, may attack credibility
- FRE 608: Character for truthfulness — reputation/opinion evidence; specific instances
  on cross-exam only (no extrinsic evidence of prior lies)
- FRE 609: Prior convictions for impeachment:
  - Crime punishable by death or imprisonment > 1 year: admissible if probative value
    outweighs prejudicial effect (FRE 403 standard generally; more protective standard
    for defendant-witnesses)
  - Crime involving dishonesty/false statement (crimen falsi): always admissible, no
    balancing
  - Time limit: generally 10 years from conviction or release from confinement
  - Annulled or pardoned convictions: may affect admissibility [VERIFY]

### Step 11: Quality Verification

Before delivering the analysis, run the quality checks in the **Quality Assurance Framework**
section:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every INADMISSIBLE or LIKELY INADMISSIBLE classification, run the 3-pass
   Self-Interrogation. Revise if any pass reveals a weakness.
3. Assign a Confidence Score to each material admissibility determination.
4. For each evidence item, confirm all applicable FRE articles have been checked.
5. Verify that privilege screen was performed before relevance analysis.
6. Generate the Glass Box Audit Trail and append it to the output.

---

## Admissibility Classification System

Classify each evidence item on a five-tier scale:

### ADMISSIBLE

Evidence meets all applicable FRE requirements and is likely to be admitted without
significant contest. Foundation requirements are clear and can be met. No viable
exclusion grounds identified.

**Action**: Identify foundation requirements checklist for trial. Brief note on any
non-meritorious objections opposing party may raise and standard responses.

**Examples:**

- Business record with proper custodian foundation (FRE 803(6); FRE 902(11) cert.)
- Party's own statement in recorded deposition (FRE 801(d)(2)(A))
- Photograph authenticated by photographer witness (FRE 901(b)(1))

### LIKELY ADMISSIBLE

Evidence has minor authenticity, foundation, or technical issues that can likely be cured
with additional foundation or that courts typically overlook. Any FRE 403 risk is low.

**Action**: Identify cure steps (additional foundation, stipulation, certification).
Brief opposing argument note.

**Examples:**

- Eyewitness testimony with slight memory inconsistency
- Email with metadata authentication that could be strengthened
- Expert opinion with one weak Daubert factor but strong overall methodology

### CONTESTED

Colorable arguments exist on both sides. Outcome depends on judicial discretion, disputed
facts, or unresolved circuit splits. Reasonable judges could rule either way.

**Action**: Present full objection/response analysis. Recommend motion in limine to
obtain advance ruling. Identify alternative admissibility theory. Assess FRE 403 risk.

**Examples:**

- Prior bad act offered under FRE 404(b) with plausible purpose but high prejudice risk
- Hearsay statement where exception application is contested (e.g., scope of FRE 803(6))
- Expert with contested methodology in emerging scientific field
- Social media post with authentication gaps that are arguable

### LIKELY INADMISSIBLE

Material deficiencies exist that are likely to prevail before a careful judge. The item
fails one or more FRE requirements without an obvious cure. Risk is high that exclusion
motion would succeed.

**Action**: Recommend motion in limine if opponent; if proponent, identify alternative
evidence or curable defect. Assess whether the deficiency can be remedied before trial.

**Examples:**

- Hearsay with no applicable exception and no non-hearsay purpose
- Prior act evidence where propensity purpose is obvious and FRE 404(b) alternative
  purposes are pretextual
- Expert opinion not connected to reliable methodology (analytical gap)
- Unauthenticated document with no available witness to cure

### INADMISSIBLE

Per se exclusion by rule with no viable alternative theory. Includes:

- Privileged communications not waived
- Evidence excluded by absolute rule (FRE 407, FRE 408, FRE 410)
- Irrelevant evidence with no alternative use
- Evidence that fails the privilege screen

**Action**: If opponent, document exclusion grounds and file motion in limine.
If proponent, accept inadmissibility and seek alternative evidence source.

---

## Objection/Response Pairs

Standard objection language and responses by rule cluster:

### Relevance (FRE 401–403)

| Objection                                                                | Response                                                                                                                                   |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| "Objection, relevance — no tendency to prove any fact of consequence"    | "Your Honor, this evidence tends to prove [specific fact at issue] by showing [logical connection]"                                        |
| "Objection, more prejudicial than probative under FRE 403"               | "The probative value is [describe]; the prejudice claimed is speculative/overstated; a limiting instruction would cure any residual risk"  |
| "Objection, cumulative — already established by multiple other exhibits" | "This exhibit corroborates [key fact], is distinctly probative because [unique aspect], and courts generally admit corroborating evidence" |

### Character Evidence (FRE 404)

| Objection                                                         | Response                                                                                                                                                      |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "Objection, improper character evidence under FRE 404(a)"         | "Not offered for character/propensity. Offered under 404(a) exception for [defendant's pertinent trait/alleged victim's pertinent trait]"                     |
| "Objection — FRE 404(b) prior acts, improper propensity purpose"  | "Offered for [specific non-propensity purpose: motive/intent/knowledge/identity/plan]. The permitted purpose is distinct from propensity because [reasoning]" |
| "Objection — no timely 404(b) notice per December 2020 amendment" | [Criminal defense]: "Prosecution failed to provide required written notice identifying specific evidence, permitted purpose, and supporting reasoning"        |

### Policy Exclusions (FRE 407–411)

| Objection                                                | Response                                                                                                                                                                        |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "Objection — subsequent remedial measure under FRE 407"  | "Not offered to prove negligence. Offered for [impeachment/feasibility of precaution/ownership — specify which]"                                                                |
| "Objection — settlement offer/negotiation under FRE 408" | "Not offered to prove liability. Offered to show [bias/undue delay — specify]"                                                                                                  |
| "Objection — FRE 410, plea discussion statement"         | "The statement was not made during formal plea discussions with the prosecutor / the exception applies because [prior statement introduced by defendant / perjury prosecution]" |

### Privilege (FRE 501–502)

| Objection                                                        | Response                                                                                                                                       |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| "Objection — attorney-client privilege"                          | "Privilege was waived by [voluntary disclosure to third party/at-issue waiver/subject-matter waiver through intentional selective disclosure]" |
| "Objection — work product protection"                            | "Proponent has substantial need for the materials and cannot obtain the substantial equivalent without undue hardship"                         |
| "Objection — FRE 502, inadvertent disclosure, clawback demanded" | "Holder did not take reasonable steps to prevent disclosure / did not promptly seek rectification / FRE 502(d) order was not in place"         |

### Hearsay (FRE 801–807)

| Objection                                           | Response                                                                                                       |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| "Objection, hearsay"                                | "Not hearsay — offered not for truth but to show [effect on listener/verbal act/circumstantial state of mind]" |
| "Objection, hearsay"                                | "Admissible as opposing party's statement under FRE 801(d)(2)([A/B/C/D/E])"                                    |
| "Objection, hearsay"                                | "Falls within [FRE 803(_)/804(_)/807] exception because [specific requirements met]"                           |
| "Hearsay within hearsay — both levels inadmissible" | "Both levels satisfy exceptions: outer level [FRE ___]; inner level [FRE ___]"                                 |

### Authentication (FRE 901–903)

| Objection                                                  | Response                                                                                                                              |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| "Objection — lack of authentication"                       | "Authenticated by [witness testimony/distinctive characteristics/FRE 902 self-authentication/FRE 902(13)–(14) certification]"         |
| "Objection — digital evidence authentication insufficient" | "Authentication supported by [metadata/content/context/witness testimony — specify]; FRE 901(b)(4) distinctive characteristics apply" |

### Expert Testimony (FRE 702; Daubert)

| Objection                                                              | Response                                                                                                                                                        |
| ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "Objection — no foundation for expert testimony; fails Daubert"        | "Methodology is [tested/peer reviewed/accepted]; meets each Daubert factor; 2023 FRE 702 amendment satisfied by preponderance because [each element addressed]" |
| "Objection — analytical gap; conclusions not supported by methodology" | "Methodology directly supports conclusion; any gap is a weight-not-admissibility issue for cross-examination"                                                   |
| "Objection — expert not qualified"                                     | "Expert qualified by [knowledge/skill/experience/training/education — specify]; formal credentials not required; practical experience sufficient"               |

### Best Evidence (FRE 1001–1008)

| Objection                                           | Response                                                                                                    |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| "Objection — original required; best evidence rule" | "Duplicate admissible under FRE 1003; no genuine question of authenticity; no unfairness in admission"      |
| "Best evidence rule — where is the original?"       | "Original lost/destroyed without bad faith (FRE 1004(a)) / original in opponent's possession (FRE 1004(c))" |

---

## Motion in Limine Framework

A motion in limine is a pretrial motion asking the court to rule on admissibility before
trial, preventing opposing counsel from referring to the evidence in the jury's presence
even if an objection would be sustained.

### When to File

| Timing Recommendation                | Situation                                                                                                                                                                       |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **File immediately**                 | Highly prejudicial evidence that could contaminate the jury even if later excluded; Crawford Confrontation Clause issues; privilege issues that should be resolved definitively |
| **File with standard MIL deadline**  | FRE 404(b) prior acts; challenged expert testimony (Daubert motion); hearsay with disputed exceptions                                                                           |
| **Defer — preserve trial objection** | Issues where context matters (FRE 403 depends on how the evidence is presented); minor foundation issues better addressed at trial                                              |

### MIL Drafting Framework

Each motion in limine should include:

1. **Statement of the evidence**: Specifically identify what evidence the motion targets
2. **Governing legal standard**: The specific FRE provision and applicable test
3. **Why the evidence fails the standard**: Specific analysis of each element
4. **Prejudice argument**: Why exclusion is important and trial instruction would be inadequate
5. **Relief requested**: Precise scope of exclusion (specific exhibit, category, or topic)
6. **Alternative relief**: If full exclusion denied, alternative limiting instruction

### Common Federal Court MIL Practice

- File with the final pretrial order or pursuant to court's scheduling order
- Many courts require meet-and-confer before filing
- Courts may grant/deny/defer ruling to trial context
- Deferred rulings require renewed objection at trial to preserve issue for appeal
- **Limine orders are not final** — courts retain discretion to revisit at trial

---

## Foundation Requirements Matrix

| Evidence Type                 | Foundation Requirements                                                                                                                                                | Common Failures                                                                 | Cure Strategy                                                                                    |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Witness Testimony**         | Personal knowledge (FRE 602); competency (FRE 601)                                                                                                                     | No personal knowledge established; witness incompetent                          | Lay personal knowledge foundation first; voir dire witness                                       |
| **Documents**                 | Authentication (FRE 901/902); best evidence (FRE 1002); hearsay exception if offered for truth                                                                         | No authentication witness; original not produced; hearsay not addressed         | Custodian of records; FRE 902(11) certification; business records foundation                     |
| **Photographs**               | Identification by witness with knowledge; depicts what it purports to show                                                                                             | No witness to identify; photograph altered                                      | Testimony of photographer or person who viewed scene; metadata                                   |
| **Video/Audio Recordings**    | Accurate portrayal; authentication; chain of custody where relevant                                                                                                    | Gaps in chain; no authenticating witness                                        | System logs; witness to recording; FRE 901(b)(9) process foundation                              |
| **Digital/ESI**               | FRE 901 foundation or FRE 902(13)–(14) certification; metadata review                                                                                                  | No metadata; self-authentication not prepared; social media attribution unclear | FRE 902(13)–(14) certification; witness with knowledge of electronic system                      |
| **Social Media Posts**        | Content attribution to specific person (FRE 901(b)(4)/(1))                                                                                                             | Attribution gap — anyone could have posted                                      | Distinctive content; account data; witness; compare across messages                              |
| **Text Messages**             | Authentication of sender; accurate record of communication                                                                                                             | No witness to identify sender; screenshot not original                          | Phone records; witness testimony; metadata; FRE 902(14) certification                            |
| **Physical Objects**          | FRE 901 identification; chain of custody where integrity matters (drugs, DNA)                                                                                          | Chain of custody gap                                                            | Testimony of each custodian; laboratory protocols; stipulation                                   |
| **Business Records**          | Regular business activity; made at or near time; by person with knowledge; regular practice to keep; custodian or qualified witness (FRE 803(6)); or FRE 902(11) cert. | Missing custodian; gaps in when made; not a business activity                   | Certification under FRE 902(11); deposition of records custodian                                 |
| **Expert Opinion**            | Qualification (FRE 702); sufficient facts/data; reliable methodology; reliable application (Daubert); preponderance showing (2023 amendment)                           | Qualification dispute; methodology not established; analytical gap              | Daubert hearing; curriculum vitae; expert's prior publications; methodology description          |
| **Demonstrative Exhibits**    | Accurate representation of underlying evidence; no independent truth claim                                                                                             | Misleading portrayal; contains inadmissible information                         | Stipulation; limiting instruction that demonstrative is not evidence                             |
| **Summaries (FRE 1006)**      | Underlying materials too voluminous to be conveniently examined; underlying materials available to opponent                                                            | Underlying materials available to opponent; summary not accurate                | Make originals available; verify accuracy; proffer underlying records                            |
| **Prior Statements**          | Witness on stand (for 801(d)(1)); prior statement under oath (for 801(d)(1)(A)); prior proceeding and opportunity to cross (for 804(b)(1))                             | Witness not on stand; statement not under oath                                  | Call witness; lay oath and prior proceeding foundation                                           |
| **Co-conspirator Statements** | Conspiracy existed; declarant and defendant were members; statement made during and in furtherance (FRE 801(d)(2)(E)); Bourjaily foundation                            | No independent evidence of conspiracy; statement not in furtherance             | Proffer; independent evidence of conspiracy; court may provisionally admit subject to connection |

---

## Recent FRE Amendments (2020–2023)

### December 1, 2020 — FRE 404(b) Criminal Notice Amendment

**What changed**: In criminal cases, the prosecutor must now provide notice of FRE 404(b)
evidence:

- **Without defense request** (notice is automatic)
- In **writing**
- Within a **reasonable time before trial**
- The notice must: (1) identify the specific 404(b) evidence, (2) articulate the
  permitted non-propensity purpose, and (3) explain the reasoning supporting that purpose

**Strategic implications**:

- Defense can seek suppression of 404(b) evidence for failure to comply with notice
- Prosecutors must think earlier about 404(b) theory and articulate it specifically
- Generic notice statements ("prior acts including [crime]") are no longer sufficient
- Civil cases: no change — no equivalent notice requirement

### December 1, 2023 — FRE 702 Preponderance Clarification Amendment

**What changed**: The amendment added clarifying language that:

- The proponent must demonstrate that the admissibility requirements are met by a
  **preponderance of evidence**
- The court must **actually determine** reliability — not merely find the evidence
  plausible

**Background**: Many circuits had applied an overly permissive standard, admitting
expert testimony if the methodology was "plausible" rather than actually determined
to meet the reliability standard by a preponderance. The amendment overrules that
approach.

**Strategic implications**:

- Daubert motions now have a stronger textual hook for demanding full gatekeeping
- Proponents must be prepared to actually prove methodology meets FRE 702 elements
- Courts can no longer simply defer reliability questions to the jury as weight issues
  without making an independent determination

### December 1, 2017 — FRE 902(13)–(14) Electronic Evidence Certification

**What changed**: Two new self-authentication categories added:

- FRE 902(13): Certified records generated by an electronic process or system
- FRE 902(14): Certified data copied from an electronic device, storage medium, or file

**Strategic implications**: Parties can authenticate ESI without calling a sponsoring
witness if they have a proper declaration from a qualified person familiar with the
electronic process. Dramatically simplifies authentication of emails, server logs, and
digital forensic copies.

---

## Daubert Hearing Preparation Framework

When a Daubert challenge is anticipated, prepare for the evidentiary hearing:

### Proponent's Preparation Checklist

- [ ] Curriculum vitae establishing qualifications (knowledge, skill, experience, training, education)
- [ ] Expert's written report identifying: opinions, basis, facts/data relied on, methodology
- [ ] Publications establishing peer review and general acceptance of methodology
- [ ] Description of testing or validation of the methodology
- [ ] Error rate documentation if quantitative methodology
- [ ] Prior cases where methodology was admitted (or explain absence)
- [ ] Prepare expert for voir dire on qualifications and methodology
- [ ] Prepare expert to explain how methodology was applied to the specific facts (avoid analytical gap)

### Opponent's Daubert Challenge Checklist

- [ ] Identify which Daubert factor(s) fail and why
- [ ] Research expert's prior publications for inconsistencies with current opinions
- [ ] Identify studies expert did not consider or that contradict conclusions
- [ ] Assess whether methodology is used outside litigation context
- [ ] Analyze whether conclusions follow from methodology (Joiner analytical gap)
- [ ] File Daubert motion with supporting materials
- [ ] Request evidentiary hearing (courts may deny for minor issues)
- [ ] Prepare cross-examination on methodology failures if admission is granted despite challenge

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                      | Fail Action                                                      |
| -------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Source**     | Every admissibility determination cites the specific FRE provision and any key case                       | Add rule citation or mark "[UNVERIFIED — counsel to confirm]"    |
| **Format**     | All citations follow consistent FRE and case law format                                                   | Fix format (e.g., "FRE 803(6)" not "Rule 803.6")                 |
| **Currency**   | Every rule reference checked for 2020/2023 amendments; Daubert/Joiner/Kumho analysis reflects current law | Flag "[CHECK CURRENCY — rule may have been amended]"             |
| **Domain**     | Analysis stays within FRE; no state evidence rules applied as if federal                                  | Remove or flag state-law intrusion; mark [JURISDICTION-SPECIFIC] |
| **Confidence** | Uncertainty explicitly stated; no definitive conclusions on discretionary matters without caveat          | Add confidence qualifier; flag judicial discretion               |

### Self-Interrogation for INADMISSIBLE / LIKELY INADMISSIBLE Items

For any item classified at the two lowest tiers, apply this 3-pass review:

**Pass 1 — Exclusion Chain Integrity**:

- Does the exclusion ground follow logically from the cited rule?
- Is there a plausible non-hearsay purpose, alternative FRE provision, or cure that
  wasn't considered?
- Would a judge applying the correct standard actually grant the motion to exclude?

**Pass 2 — Alternative Admissibility Theories**:

- Have all 37 FRE hearsay provisions been considered?
- Is there a non-hearsay purpose for the statement?
- Could the authentication deficiency be cured with additional foundation?
- Could the FRE 403 risk be mitigated by a limiting instruction?

**Pass 3 — Challenge**:

- What is the opposing party's strongest argument for admissibility?
- Under what circumstances would a reasonable judge admit this evidence?
- Is the exclusion recommendation proportionate, or is this actually CONTESTED?

If any pass reveals a weakness, revise the classification before delivery. Mark the
audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                                        | Action                                                |
| ------------ | --------- | -------------------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled rule, clear application, per se exclusion or admission | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong rule application, minor discretion question             | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Likely outcome, but judicial discretion may vary               | State with explicit reasoning and contra-indicator    |
| **Possible** | 0.40–0.59 | Genuinely contested; reasonable judges disagree                | Flag for counsel judgment with both sides             |
| **Unlikely** | 0.00–0.39 | Weak basis for the proposed classification                     | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every evidence admissibility analysis MUST include this audit section:

```yaml
glass_box:
  skill_name: "legalcode-evidence-admissibility-analysis"
  analysis_date: "[date]"
  case_type: "[Civil / Criminal / Unknown]"
  mode: "[Proponent / Opponent / Both]"
  procedural_posture: "[Pre-trial MIL / Trial objection prep / Appellate / Discovery]"
  evidence_items_analyzed: "[number]"
  items_by_classification:
    admissible: "[number]"
    likely_admissible: "[number]"
    contested: "[number]"
    likely_inadmissible: "[number]"
    inadmissible: "[number]"
  privilege_screen: "COMPLETED — [number] items flagged / No privilege issues identified"
  fre_articles_engaged: "[list: 201 / 401-403 / 404-406 / 407-411 / 501-502 / 601-609 / 701-706 / 801-807 / 901-903 / 1001-1008]"
  daubert_analysis: "YES — [number] experts analyzed / NO"
  legalcode_mcp: "Connected / Not connected"
  amendments_applied:
    - "FRE 404(b) Dec. 1, 2020 criminal notice — APPLIED / NOT APPLICABLE"
    - "FRE 702 Dec. 1, 2023 preponderance standard — APPLIED / NOT APPLICABLE"
    - "FRE 902(13)-(14) Dec. 1, 2017 electronic certification — APPLIED / NOT APPLICABLE"
  crawford_flagged: "YES — [number] testimonial hearsay items require constitutional analysis / NO"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED (marked [VERIFY])]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "State evidence rules not analyzed — verify if case is in state court"
    - "Constitutional admissibility (Confrontation Clause, Fourth Amendment suppression) not addressed"
    - "Case-specific judicial temperament and local rules not assessed"
    - "[Any other scope limitations]"
  reviewer: "AI-assisted — requires qualified legal review and independent citation verification"
```

---

## Prioritization Framework

When analyzing multiple evidence items, prioritize analysis effort:

### Tier 1 — Must Resolve Before Trial

Issues where in-court surprise would be highly prejudicial or strategic damage irreversible:

- Highly prejudicial 404(b) prior acts evidence (jury contamination even if excluded)
- Challenged expert testimony (Daubert motions require full briefing and often hearings)
- Privileged communications inadvertently produced (FRE 502 clawback)
- Crawford-implicating testimonial hearsay in criminal cases
- Confessions or statements subject to Miranda/voluntariness challenge
- Evidence central to core claims or defenses

### Tier 2 — Strong Preference — File MIL

Issues with colorable challenge where pretrial ruling clarifies evidence presentation:

- FRE 404(b) prior acts with contested 404(b) purpose
- Hearsay where exception application is genuinely disputed
- Expert opinions with targeted Daubert weaknesses
- Social media or ESI with authentication gaps
- FRE 407–411 policy exclusions where opponent may attempt to introduce

### Tier 3 — Preserve at Trial

Issues better addressed in trial context or where MIL would be premature:

- FRE 403 challenges where balance depends on trial context
- Minor foundation issues likely to be cured at trial
- Cumulative evidence that may become less cumulative as trial develops
- Impeachment evidence that depends on direct testimony elicited

---

## Anti-Patterns

What NOT to do in evidence admissibility analysis:

1. **Skipping the privilege screen** — Analyzing relevance and hearsay before checking
   privilege. Privilege is an absolute bar; if it applies, all other analysis is moot.
   Always run the privilege screen first.

2. **Conflating hearsay purpose with admissibility** — Stating "this is inadmissible
   hearsay" without identifying whether the statement is offered for truth, whether any
   801(d) exemption applies, and whether any of the 37 FRE provisions might except it.
   There are 37 ways hearsay might be admissible; check all applicable ones.

3. **Misapplying FRE 404(b) in civil cases** — Treating civil cases as having the same
   404(b) notice requirement as criminal cases. The December 2020 amendment applies only
   to the prosecution in criminal cases; civil litigants have no equivalent mandatory
   notice duty.

4. **Ignoring the 2023 FRE 702 amendment** — Applying the pre-amendment "plausibility"
   standard instead of the correct "preponderance" standard for expert admissibility.
   Courts must now actually determine reliability, not merely find it plausible.

5. **Treating FRE 403 as a presumption against admission** — The standard is that
   probative value must be "substantially outweighed" by the danger of unfair prejudice.
   FRE 403 favors admission; the party seeking exclusion bears a significant burden.

6. **Applying Crawford to civil cases** — The Sixth Amendment Confrontation Clause applies
   only in criminal prosecutions. It does not bar hearsay in civil cases. Don't recommend
   Crawford challenges in civil litigation.

7. **Confusing FRE 408 and FRE 409 scope** — FRE 408 covers settlement negotiations for
   disputed claims (broad protection); FRE 409 covers only offers to pay medical expenses
   (narrower, does not protect accompanying statements the way FRE 408 does).

8. **Analyzing business records without checking FRE 902(11) self-authentication** —
   Business records certified under FRE 902(11) do not require a live custodian at trial.
   Failing to advise clients of this option leads to unnecessary trial preparation.

9. **Forgetting double hearsay** — When a document contains a statement that contains
   another statement (e.g., police report containing witness statement), each level needs
   its own exception. Many practitioners analyze only one level.

10. **Misidentifying habit evidence** — Distinguishing FRE 406 habit (specific repeated
    behavior in specific circumstances, near-automatic response) from FRE 404 character
    (general disposition) is often contested. Habit requires regularity and specificity
    beyond general character traits. Don't label general character as habit.

11. **Ignoring dying declaration limitations** — Under FRE 804(b)(2), dying declarations
    are admissible in federal court only in civil cases and **homicide** prosecutions.
    Unlike many state rules, there is no federal dying declaration exception for non-homicide
    criminal cases. [VERIFY — state analogs often broader]

12. **Failing to consider FRE 807 residual exception** — After exhausting all specific
    hearsay exceptions, always consider FRE 807. Courts apply it narrowly, but for critical
    evidence with strong trustworthiness indicia (corroboration, contemporaneous creation,
    no motive to fabricate), it may succeed.

13. **Recommending FRE 901 authentication without preparing the witness** — Telling a
    client their document is authenticated "by a witness with knowledge" without preparing
    the specific witness to testify to the specific attributes. Authentication witnesses
    must be prepped on exactly what foundation is being laid and why.

14. **Treating Daubert as just a qualifications challenge** — Most Daubert exclusions
    rest on methodology, not credentials. Courts rarely exclude experts on credentials
    alone. The Joiner analytical gap doctrine (conclusions must flow from methodology)
    and Kumho Tire (applies to technical and specialized knowledge, not just science) are
    the stronger challenge bases for many expert opinions.

15. **Failing to preserve objections for appeal** — An MIL ruling, even if denied, does
    not automatically preserve the issue for appeal. Counsel must renew the objection when
    the evidence is actually offered at trial. Failing to do so waives the appellate issue.
    Note this risk whenever a court defers MIL ruling or rules "without prejudice."

16. **Asserting privilege without analyzing waiver** — Opposing a privilege claim requires
    analyzing all waiver theories: at-issue waiver (party's defense places privileged
    communications directly at issue), subject-matter waiver (selective intentional
    disclosure), and crime-fraud exception (communication in furtherance of future crime
    or fraud). Generic privilege assertions without waiver analysis are incomplete.

17. **Ignoring FRE 412 in civil sex cases** — Rule 412 applies to civil cases involving
    alleged sexual misconduct or sexual harassment, not just criminal sexual assault
    prosecutions. Evidence of an alleged victim's sexual predisposition is generally
    inadmissible in civil cases with a different (but similarly protective) standard.

---

## Writing Standards

Apply plain-language discipline to all output:

**For admissibility assessments** (may be shared with supervising attorney):

- State the classification first, then the analysis (bottom-line up front)
- Name the specific FRE provision: "FRE 803(6) business records exception" not
  "a hearsay exception"
- Active voice: "The document fails FRE 901 authentication" not "Authentication of the
  document has not been established"
- One objection/response pair per FRE issue — don't bundle multiple objections

**For motion in limine language** (submitted to court):

- Precise rule citations
- Specific description of the evidence targeted
- Specific relief requested (including scope)
- Courts prefer concise, focused MILs to omnibus motions

**Quality gates before delivery:**

- [ ] Every FRE citation is to a specific rule and subsection
- [ ] Privilege screen is documented before relevance/hearsay analysis
- [ ] Each admissibility classification is supported by specific reasoning
- [ ] CONTESTED items include full objection/response analysis
- [ ] Alternative admissibility theories addressed for LIKELY INADMISSIBLE items
- [ ] Confidence scores assigned to all material determinations
- [ ] Glass Box audit trail included

---

## External Tool Integration

### With legalcode-mcp Connected (Preferred)

In Step 4 (privilege screen), use legalcode-mcp to retrieve:

- Circuit-specific privilege doctrine (split on psychotherapist privilege, journalist privilege, and scope of spousal privilege)
- Current Daubert standard in the applicable circuit (some circuits apply more stringent gatekeeping)
- Recent circuit court decisions on FRE 404(b) after the 2020 amendment
- Any district court local rules affecting MIL practice or Daubert hearing requirements

Save relevant results to `/tmp/legalcode-evidence-research.md`.

Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail.

### Without legalcode-mcp

- Proceed with analysis using general FRE knowledge
- Mark all case citations with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Advise user to verify circuit-specific law for all contested issues

---

## Output Format Template

```markdown
# Evidence Admissibility Analysis

**Case**: [Case name or description]
**Analysis Date**: [date]
**Mode**: [Proponent / Opponent / Both]
**Case Type**: [Civil / Criminal]
**Procedural Posture**: [Pre-trial MIL / Trial prep / etc.]

---

## Executive Summary

**[N] items analyzed: [X] ADMISSIBLE | [X] LIKELY ADMISSIBLE | [X] CONTESTED |
[X] LIKELY INADMISSIBLE | [X] INADMISSIBLE**

**Critical issues requiring immediate attention:**

1. [Highest priority item and action needed]
2. [Second priority]
3. [Third priority]

---

## Privilege Screen Results

[Summary of privilege screen. If no issues: "No privilege issues identified across all
[N] evidence items." If issues: detail each.]

---

## Per-Item Analysis

### Exhibit [#] / [Item Name]

**Description**: [What the item is and its anticipated use]

**Classification**: [ADMISSIBLE / LIKELY ADMISSIBLE / CONTESTED / LIKELY INADMISSIBLE / INADMISSIBLE]

**Confidence**: [Definite / High / Probable / Possible / Unlikely] ([0.XX])

**Applicable FRE Provisions**: [List rules analyzed]

**Admissibility Analysis**:
[Step-by-step analysis of each applicable FRE provision]

**Objection (if opponent)**:

> "[Specific objection language]" — basis: FRE [___]

**Response (if proponent)**:

> "[Specific response]" — basis: FRE [___]

**Foundation Requirements** (if proponent):

- [ ] [Specific foundation requirement 1]
- [ ] [Specific foundation requirement 2]
- [ ] [...]

**Motion in Limine Recommendation**:
[File immediately / File with MIL deadline / Defer / Not recommended]
[Brief strategy note]

**Alternative Admissibility Theory** (if primary theory fails):
[Describe alternative theory, if any]

**Self-Interrogation** (if LIKELY INADMISSIBLE or INADMISSIBLE):

- Pass 1: [Exclusion chain integrity assessment]
- Pass 2: [Alternative theories checked]
- Pass 3: [Strongest counter-argument]
- Result: [PASS — classification confirmed / REVISED — classification changed to ___]

---

[Repeat for each evidence item]

---

## Motion in Limine Recommendations Summary

| Priority | Item   | Grounds   | Recommendation         | Filing Deadline |
| -------- | ------ | --------- | ---------------------- | --------------- |
| Tier 1   | [Item] | FRE [___] | File immediately       | [date]          |
| Tier 2   | [Item] | FRE [___] | File with MIL deadline | [date]          |

---

## Daubert Analysis (if applicable)

[For each expert: qualification assessment, methodology reliability assessment, analytical
gap review, hearing recommendation]

---

## Glass Box Audit Trail

[YAML audit block as specified above]
```

---

## Localization Notes

This skill analyzes evidence under the **Federal Rules of Evidence only**. When the case
is in state court or involves state-law claims in federal court:

1. **Privilege (FRE 501)**: In federal diversity cases, state law governs privilege for
   state-law claims. Federal common law governs privilege for federal claims.

2. **Expert witnesses**: Approximately 30 states still apply the Frye general acceptance
   test rather than Daubert. Always verify which standard applies in the applicable
   forum. [VERIFY current state law]

3. **Hearsay exceptions**: Many states have their own hearsay exception lists that differ
   from FRE 803–807 — notably, many state dying declaration rules are broader than the
   federal rule (which limits it to homicide and civil cases).

4. **Character evidence**: FRE 413–415 (prior sexual assault admissibility) has no
   universal state analog — many states follow traditional FRE 404 rules for sexual
   assault cases.

5. **Electronic evidence**: FRE 902(13)–(14) electronic certification has been adopted
   in varying forms in many states but not universally. Verify state authentication rules.

---

## Provenance

Created by Legalcode (2026-03-02). Legalcode original synthesis. Incorporates the
December 1, 2020 FRE 404(b) criminal notice amendment, the December 1, 2023 FRE 702
preponderance standard clarification amendment, and the December 1, 2017 FRE 902(13)–(14)
electronic evidence self-authentication provisions. Research informed by web-backed
research on current FRE doctrine, Daubert framework, motion in limine practice, and
privilege law. Legal citations throughout marked [VERIFY] where not independently
confirmed — verify all authority before reliance.

```

```
