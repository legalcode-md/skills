---
name: legalcode-arbitration-demand-drafter
description: Drafts and reviews arbitration demands (Requests for Arbitration, Notices of Arbitration),
  Statements of Claim, Answers/Responses, and Counterclaims for international and domestic commercial
  arbitration proceedings under ICC (2021 Rules), LCIA (2020 Rules), AAA Commercial Arbitration Rules,
  ICDR International Arbitration Rules, SIAC (2016/2025 Rules), and HKIAC (2018 Rules). Use when commencing
  arbitration proceedings, responding to an arbitration demand, seeking emergency relief in arbitration,
  or preparing any notice, request, or demand document for filing with an international or domestic arbitral
  institution.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Drafts and reviews arbitration demands (Requests for Arbitration, Notices of Arbitration), Statements of Claim, Answers/Responses, and Counterclaims for international and domestic commercial arbitration proceedings under ICC (2021 Rules), LCIA (2020 Rules), AAA Commercial Arbitration Rules, ICDR International Arbitration Rules, SIAC (2016/2025 Rules), and HKIAC (2018 Rules). Also supports UNCITRAL ad hoc arbitration and UNCITRAL Model Law jurisdictions. Covers jurisdictional analysis (arbitration agreement validity, scope, seat selection, governing law), statement of claim drafting (factual narrative, legal basis, quantified relief, interest), provisional measures and emergency arbitrator applications (ICC Article 29, LCIA Article 9B, SIAC Rule 30), arbitrator nomination strategy (IBA Guidelines compliance, independence declarations, nationality requirements), procedural timetable proposals, filing fee calculations, service and commencement date verification, multi-party arbitration (consolidation, joinder), and respondent's Answer drafting with jurisdictional objections and counterclaims. Use when commencing arbitration proceedings, responding to an arbitration demand, seeking emergency relief in arbitration, or preparing any notice, request, or demand document for filing with an international or domestic arbitral institution. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers for seat-of-arbitration law. Supports investor-state arbitration background but optimized for international commercial disputes.


# Legalcode Arbitration Demand Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted arbitration demand drafting
> and review. It does not constitute legal advice. All outputs must be reviewed and approved
> by qualified legal counsel admitted in the relevant jurisdiction before filing. Arbitration
> demands have legal and procedural consequences — they commence formal proceedings, may toll
> statutes of limitations, and establish the scope of claims that may be arbitrated. Errors
> in service, commencement requirements, or arbitration agreement compliance can result in
> jurisdictional defeats or unenforceable awards. Laws and institutional rules change
> frequently; verify all authority before relying on any provision described here. Any cited
> authority marked `[VERIFY]` has not been independently validated and must be confirmed
> before reliance. Statutory, case law, and institutional rule references cited from memory
> carry hallucination risk — verify against current institutional rules and authoritative
> sources before filing.

---

## Purpose and Scope

This skill drafts, reviews, and quality-checks arbitration demands and related pleadings for
international and domestic commercial arbitration proceedings. It operates in two primary
modes and one secondary mode:

**Mode 1 — Demand / Request for Arbitration Drafting**: Generates a complete, procedurally
compliant Notice or Request for Arbitration and accompanying Statement of Claim — including
institution-specific mandatory elements, arbitration agreement analysis, statement of facts,
legal basis with citations, quantified relief, arbitrator nomination, and a procedural
timetable proposal.

**Mode 2 — Answer / Response Drafting**: Drafts a compliant Answer or Response to an
incoming arbitration demand — including jurisdictional objections, denial or admission of
claims, counterclaims, arbitrator nomination, and procedural proposals.

**Mode 3 — Emergency / Provisional Measures**: Drafts an Emergency Arbitrator Application
or Provisional Measures Request alongside or separate from the main demand.

**Covers:**

- All major international arbitration institutions: ICC, LCIA, AAA/ICDR, SIAC, HKIAC
- UNCITRAL Arbitration Rules (ad hoc) and UNCITRAL Model Law jurisdictions
- Institution-specific mandatory content requirements (Article-by-Article compliance)
- Arbitration agreement analysis: validity, scope, pathological clauses, multi-contract disputes
- Seat of arbitration selection and implications under lex arbitri
- Statement of Claim structure: facts, legal basis, causation, damages, interest, costs
- Provisional measures framework: emergency arbitrators, court-ordered interim relief
- Arbitrator nomination strategy: IBA Guidelines, independence, conflicts, nationality
- Procedural timetable proposals and expedited procedure eligibility
- Statute of limitations analysis by jurisdiction and institution
- Multi-party arbitration: consolidation, joinder, third-party funding disclosure
- Service requirements and commencement date documentation
- Filing fees and advance on costs calculation guidance
- Answer/Response drafting: jurisdictional objections, counterclaims, procedural proposals

**Does not:**

- File documents with any arbitral institution or court (drafting only)
- Provide legal advice or replace qualified international arbitration counsel
- Guarantee enforceability of any award under the New York Convention or otherwise
- Conduct independent factual investigation — it relies on information provided by the user
- Cover investor-state arbitration under ICSID Convention or investment treaties in depth

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill covering international commercial arbitration across
all major institutional frameworks. Two distinct laws govern every arbitration:

1. **Lex Arbitri (Law of the Seat)**: The procedural law of the arbitration — determined by
   the seat of arbitration, not the parties' governing law choice. Governs tribunal
   constitution, challenge procedures, interim measures from courts, and award annulment.
   This is the jurisdiction that matters most for procedural integrity.

2. **Substantive Governing Law**: The law applied to the merits of the dispute — typically
   chosen by the parties in their contract.

[JURISDICTION-SPECIFIC] When localizing for a specific seat, research and apply:

- National arbitration legislation (e.g., English Arbitration Act 1996; French CPC Arts.
  1442-1527; Singapore International Arbitration Act 1994 (cap. 143A); Hong Kong Arbitration
  Ordinance Cap. 609; US FAA 9 U.S.C. §§1-16; German ZPO §§1025-1066; Swiss PIL Art. 176-194)
- Local court assistance powers for interim measures and evidence
- Mandatory provisions of the lex arbitri that the parties cannot contract out of
- Enforcement framework under the New York Convention 1958 and any bilateral treaties

All New York Convention states (170+ as of 2026) recognize commercial arbitration awards
from other contracting states. [VERIFY current accession status for the relevant jurisdictions.]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The applicable institutional rules or mode of operation are unclear
- The arbitration agreement has ambiguities affecting jurisdiction or scope
- The seat of arbitration or governing law must be confirmed before analysis
- Damages, interest, or relief calculations depend on user-supplied data
- Emergency or provisional measures are needed (affecting the drafting sequence)
- Multi-party or multi-contract issues create structural choices

Use the **⟁ CLARIFY** pattern (structured options with descriptions) at the marked points.
If the user has already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:

- **Dispute summary**: Bullet-point or narrative summary of the dispute, parties, claims, and amounts
- **Contract document**: The underlying contract containing the arbitration agreement
- **Arbitration agreement only**: Standalone arbitration clause or submission agreement
- **Incoming demand**: A received Notice/Request for Arbitration (for Answer drafting)
- **Prior pleadings or correspondence**: For context on the dispute and parties' positions

If no arbitration agreement is provided, ask the user to supply it — the entire demand depends
on the scope and validity of that clause.

---

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask these questions. Present as structured options where
possible. Skip any question already answered in the input.

1. **Mode**: What are you drafting?
   - Options: (A) Notice/Request for Arbitration + Statement of Claim, (B) Answer/Response
     to incoming demand, (C) Emergency Arbitrator Application / Provisional Measures only,
     (D) Full demand package (A + C)
   - _Why this matters_: Determines the entire drafting sequence and required elements.

2. **Institution**: Which arbitral institution or rules apply?
   - Options: ICC (2021 Rules), LCIA (2020 Rules), AAA Commercial (2022 Rules), ICDR
     International (2021 Rules), SIAC (2025 or 2016 Rules), HKIAC (2018 Rules), UNCITRAL
     Rules (ad hoc), Other (specify)
   - _Why this matters_: Each institution has different mandatory content requirements,
     commencement procedures, and fee structures.

3. **Parties**: Who are the claimant(s) and respondent(s)?
   - Prompt: Full legal name, entity type, registered address, and representative details for
     each party. Flag if there are multiple claimants or respondents (multi-party issues).
   - _Why this matters_: Party identification is a mandatory requirement of every institution.

4. **Claims and amounts**: What are the claims and estimated total amount in dispute?
   - Prompt: Primary claims (breach of contract, payment default, IP infringement, etc.),
     estimated monetary amount for each, and any non-monetary relief sought.
   - _Why this matters_: Affects filing fees (ad valorem systems), expedited procedure
     eligibility, and the structure of the Statement of Claim.

5. **Urgency**: Is there an immediate need for provisional measures or an emergency arbitrator?
   - Options: Yes — imminent irreparable harm requiring emergency relief; No — standard
     proceedings; Uncertain — analyze the situation and advise
   - _Why this matters_: Determines whether to prepare an emergency arbitrator application
     alongside or ahead of the main demand.

6. **Third-party funding**: Is any party using litigation or arbitration funding?
   - Options: Yes — provide funder identity; No; Unknown — advise on disclosure requirements
   - _Why this matters_: HKIAC, ICC, and other institutions require disclosure of third-party
     funding agreements. Failure to disclose can be a ground for sanctions.

If the user provides partial information, proceed with what is available and **state all
assumptions explicitly** at the start of the output.

---

### Step 3: Analyze the Arbitration Agreement

Before drafting, thoroughly analyze the arbitration agreement (the clause or submission
agreement that gives the tribunal jurisdiction). This is the most critical step — an
inadequate or pathological clause can be a ground for annulment or non-enforcement.

**3a. Identify and extract the arbitration agreement**

- Locate the arbitration clause in the underlying contract (or standalone submission agreement)
- Record the full text verbatim — this text will be included in the demand
- Identify any related dispute resolution provisions (notice of dispute, escalation, mediation
  pre-condition, expert determination)

**3b. Assess clause validity**

- Is the agreement in writing? (New York Convention Art. II requires a written agreement) [VERIFY]
- Are the parties bound? (signatories, successors, third parties by estoppel or group of companies doctrine)
- Does it cover the claims being asserted? (scope analysis — "arising out of" vs. "in connection with")
- Does it conflict with another dispute resolution clause in the same or related contract?
- Is the clause pathological? Apply the **Eisemann pathological clause framework** [VERIFY]:
  - Missing institution or administering body (agreed to the wrong or non-existent body)
  - Internally contradictory (e.g., "arbitration before the courts of [city]")
  - Requires unanimous consent to arbitrate (rendering the clause illusory)
  - Conflicts with another clause in the same contract
  - Silent on number of arbitrators, seat, or governing law in a way that creates ambiguity

**⟁ CLARIFY** — If the clause appears pathological or defective:

- "The arbitration clause contains [specific defect]. This may create a jurisdictional
  challenge. Options: (A) Proceed with the demand and address the issue in a jurisdiction
  section; (B) Apply to a competent court to determine arbitrability first; (C) Invite the
  respondent to enter a submission agreement clarifying the clause. Which approach do you want?"

**3c. Identify key clause terms**
Extract from the clause:

- Named institution (if any)
- Seat of arbitration (critical — determines lex arbitri)
- Number of arbitrators (1 or 3)
- Language of arbitration
- Substantive governing law (note: often in a separate clause)
- Any procedure modifications (expedited rules opt-in, waiver of certain rights)
- Pre-arbitration conditions (notice of dispute, cooling-off period, mediation)

**3d. Confirm pre-arbitration conditions are satisfied**
Many clauses require: notice of dispute → negotiation period → mediation → then arbitration.
Failure to comply with pre-conditions can render the demand premature and give the respondent
grounds to object.

**⟁ CLARIFY** — If pre-conditions exist and compliance is uncertain:

- "The clause requires [X days] of negotiation before arbitration. Has this period elapsed?
  If not, commencing arbitration now may be premature and expose the demand to a jurisdictional
  challenge. Do you want to: (A) Wait until the period has elapsed, (B) Proceed now and address
  this issue, or (C) Seek legal advice on whether the respondent's conduct waived the pre-condition?"

---

### Step 4: Jurisdiction and Enforceability Analysis

**4a. Seat of arbitration**

- Identify the seat from the arbitration clause or propose a seat if not specified
- Confirm the seat is in a New York Convention contracting state [VERIFY]
- Note the applicable lex arbitri and its mandatory provisions
- Flag if the proposed seat has unusual restrictions on international arbitration

**4b. Statute of limitations / prescription**
Analyze the applicable limitation period for each claim:

- Identify the substantive governing law of the contract
- Research the applicable limitation period for the primary claim type (breach of contract,
  tort, etc.) under that governing law [VERIFY]
- Confirm whether commencing arbitration (filing the demand) tolls the limitation period under
  applicable law — this varies significantly by jurisdiction [VERIFY]
- Flag any claim that appears to be close to or past the limitation period as a CRITICAL DEFECT

[JURISDICTION-SPECIFIC] Key limitation period rules:

- **England & Wales**: Limitation Act 1980 — contract claims 6 years from breach; arbitration
  generally tolls limitation from the date of the written claim under s.34 [VERIFY]
- **United States (FAA)**: No federal limitation period; state law applies (e.g., NY CPLR
  §213(2): 6-year contract; California CCP §337: 4-year written contract) [VERIFY]
- **France**: Commercial claims 5 years (Code de commerce L.110-4); arbitration commencement
  tolls limitation from the date of service [VERIFY]
- **Singapore**: Limitation Act 1959, s.6: 6-year contract; arbitration commenced on notice
  date under IAA s.9A [VERIFY]
- **Hong Kong**: Limitation Ordinance Cap. 347, s.4: 6-year contract; arbitration commenced on
  notice date under Arbitration Ordinance s.13 [VERIFY]

**4c. New York Convention enforcement assessment**

- Confirm both the seat state and the enforcement state are New York Convention contracting states
- Note any reservations the enforcement state has made (commercial/reciprocity reservations)
- Flag any sovereign immunity issues if one party is a state or state-owned enterprise

---

### Step 5: Select Institution and Applicable Rules

Based on the arbitration agreement and user input from Step 2, confirm the applicable
institutional rules. If the agreement is silent on the institution:

**⟁ CLARIFY** — "The arbitration clause does not specify an institution. Options:
(A) ICC — most recognized globally; best for high-value complex disputes (US$5,000 filing fee);
(B) LCIA — strong for UK/European seat; efficient administration;
(C) SIAC — preferred for Asia-Pacific disputes; S$6M expedited threshold;
(D) HKIAC — preferred for China-related disputes; strong Hong Kong lex arbitri;
(E) ICDR — preferred for US parties in international disputes;
(F) UNCITRAL Rules (ad hoc) — maximum flexibility; no institution; parties appoint directly.
Which institution do you want to proceed with?"

Review the **Institution-Specific Requirements Reference** section below for the detailed
mandatory content requirements for the chosen institution. All demands must satisfy those
requirements precisely.

---

### Step 6: Assess Provisional Measures Needs

**6a. Determine whether emergency relief is needed**
Emergency arbitration / provisional measures may be needed when:

- Assets are at risk of dissipation before an award can be enforced
- Respondent is destroying or concealing evidence
- Contractual rights (exclusivity, IP licenses) are being infringed in real time
- Respondent has commenced proceedings in a court that would undermine the arbitration

**6b. If emergency arbitrator application is needed**

**⟁ CLARIFY** — "This situation suggests emergency arbitrator relief may be warranted.
Emergency applications require immediate, irreparable harm that cannot wait for the tribunal
to be constituted. This is a high bar. Should I: (A) Draft an emergency arbitrator application
alongside the main demand, (B) Assess the threshold and advise before drafting, or
(C) Proceed with the main demand only and address interim relief after the tribunal is formed?"

For emergency applications, gather:

- Specific harm that will occur before a tribunal can be constituted (typically 4-8 weeks)
- Evidence of imminent irreparable harm (not speculative or compensable by money)
- Relief specifically requested from the emergency arbitrator
- Jurisdictional basis (confirm emergency procedures apply to the arbitration agreement date)

Note: ICC emergency arbitrator procedure (Article 29) does NOT apply retroactively to
agreements pre-dating the introduction of the 2012 ICC Rules unless opted in. [VERIFY]
Similarly, LCIA emergency arbitrator (Article 9B) applies only to agreements dated on or
after October 1, 2014, unless the parties agreed in writing to opt in. [VERIFY]

**6c. Court-ordered interim measures**
Parallel to or instead of an emergency arbitrator, advise on court-ordered interim measures
at the seat or place of enforcement:

- Most jurisdictions allow courts to grant interim relief in aid of arbitration
- UK: s.44 Arbitration Act 1996; Singapore: s.12A IAA; HK: s.45 Arbitration Ordinance;
  France: juge des référés; US: varies by circuit under FAA §8 [VERIFY]
- Court relief is typically faster but requires separate proceedings

---

### Step 7: Draft the Notice / Request for Arbitration

Using the institution-specific requirements in the **Institution-Specific Requirements
Reference** section, draft the formal Notice or Request for Arbitration.

**Core components required by all institutions:**

1. Identification of all parties (full legal name, entity type, registered address, contacts)
2. Legal representatives for the claimant (name, firm, address, email, phone)
3. Full text of the arbitration agreement invoked (or reference to the contract containing it)
4. Copy of or reference to the underlying contract(s)
5. Description of the nature and circumstances of the dispute
6. Statement of relief sought (monetary claims quantified; non-monetary relief specified)
7. Proposed seat of arbitration (if not specified in the clause)
8. Proposed language of arbitration (if not specified)
9. Proposal on number of arbitrators (1 or 3) and, if 3, nomination of claimant's arbitrator
10. Proposed substantive governing law (if not specified in the contract)
11. Confirmation of simultaneous service on all respondents

**Additional institution-specific requirements**: See the **Institution-Specific Requirements
Reference** section for ICC, LCIA, AAA/ICDR, SIAC, and HKIAC specific additions.

**Drafting principles for the narrative section:**

- Open with one paragraph stating clearly: (a) who the parties are, (b) what the dispute is
  about, (c) the amount at stake, and (d) the relief sought
- Provide a chronological factual narrative — lead the reader through the events giving rise
  to the dispute in logical order
- State the legal basis for each claim with precision (breach of specific contract provisions,
  statutory violations, torts)
- Quantify every monetary claim — provide the basis for each number
- Identify non-monetary relief with particularity — what exactly must the respondent do or
  not do?
- Use the **memorials approach** (narrative) rather than formulaic pleadings for ICC/LCIA
  proceedings; use the **pleadings approach** for AAA/ICDR domestic arbitrations

---

### Step 8: Arbitrator Nomination Strategy

**8a. Number of arbitrators**

- If the clause specifies 1 or 3 arbitrators, follow the clause
- If silent: for disputes below ~US$5M, a sole arbitrator is typically more proportionate;
  above US$5M, a 3-member tribunal is more common for international disputes
- Note: most institutions reserve the right to determine the number regardless of the parties'
  proposal based on complexity

**8b. Selection criteria for arbitrator nomination**
Evaluate potential nominees against:

| Criterion                       | Considerations                                                                                                                                                       |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Subject matter expertise**    | Relevant industry sector, contract type, or legal issues in dispute                                                                                                  |
| **Arbitration expertise**       | Track record as arbitrator vs. advocate; prior awards                                                                                                                |
| **Nationality**                 | Sole arbitrators and presiding arbitrators are often required to be of different nationality from both parties (check institutional rules) [VERIFY]                  |
| **Language**                    | Must be able to conduct proceedings in the language of arbitration                                                                                                   |
| **Independence / impartiality** | Apply IBA Guidelines on Conflicts of Interest in International Arbitration (2014, updated 2024) [VERIFY] — Red List (waivable/non-waivable), Orange List, Green List |
| **Availability**                | Confirm nominee can commit to the likely timeline                                                                                                                    |
| **Track record**                | Known views on applicable law; prior decisions in similar disputes; history of challenges                                                                            |

**8c. Content of nomination in the demand**
Include in the demand:

- Full name, professional title, firm/institution, address, email of nominated arbitrator
- Brief statement of credentials demonstrating fitness for the dispute
- Confirmation that the claimant has notified the nominated arbitrator and received preliminary
  confirmation of availability and absence of known conflicts
- Statement that the nominated arbitrator will provide a declaration of independence per
  institutional rules upon formal appointment

**8d. Siemens/Dutco problem in multi-party arbitration** [VERIFY]
When there are multiple respondents (or claimants), all parties on the same side must jointly
nominate one arbitrator. If they cannot agree, the institution appoints all three. Raise this
issue if multi-party structure creates nomination complications.

---

### Step 9: Draft the Statement of Claim

For ICC and LCIA proceedings, the Statement of Claim is typically a separate, more detailed
document than the initial Notice/Request. For AAA/ICDR, SIAC, and HKIAC, the claim is often
incorporated into the initial Notice.

**9a. Structure of the Statement of Claim**

```
I.   Introduction and Relief Sought (summary)
II.  The Parties
III. Background and Contractual Framework
IV.  Relevant Arbitration Agreement and Jurisdiction
V.   Factual Background (chronological narrative)
VI.  Legal Basis for Each Claim
     A. Claim 1: [Name] — Legal elements + facts satisfying each element
     B. Claim 2: [Name] — Legal elements + facts satisfying each element
     [...]
VII. Damages and Relief
     A. Direct / expectation damages
     B. Consequential / indirect damages (with jurisdictional note)
     C. Interest (pre-award and post-award)
     D. Costs (legal fees, arbitration costs)
     E. Non-monetary relief
VIII.Reservation of Rights
IX.  Relief Requested (verbatim)
```

**9b. Damages analysis**

For each head of damages, apply the applicable measure under the substantive governing law:

| Governing Law System                   | Expectation Damages                                                                                             | Consequential Damages                                                          | Interest                                                                                                                   |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| **Common law (England)**               | Hadley v Baxendale two-limb test: direct loss + loss in reasonable contemplation at contract formation [VERIFY] | Second limb: known/foreseeable special circumstances [VERIFY]                  | Late Payment of Commercial Debts (Interest) Act 1998 (8% over Bank of England base rate for qualifying contracts) [VERIFY] |
| **Common law (US)**                    | Direct (general) damages + consequential (special) damages with foreseeability limit                            | Proportionality and duty to mitigate                                           | Pre-judgment interest varies by state (simple/compound; rate) [VERIFY]                                                     |
| **Civil law (France)**                 | Article 1231-2 Code civil: dommages-intérêts = damnum emergens + lucrum cessans [VERIFY]                        | Prévisibilité at contract formation (Art. 1231-3) [VERIFY]                     | Taux légal + moratory interest from mise en demeure [VERIFY]                                                               |
| **Civil law (Germany)**                | BGB §249: Naturalrestitution or compensation; §252: lost profits [VERIFY]                                       | Adequate causation theory; foreseeability not strictly required [VERIFY]       | BGB §288: 9 percentage points above base rate for commercial claims [VERIFY]                                               |
| **CISG (international sale of goods)** | Article 74: loss foreseeable at conclusion of contract [VERIFY]                                                 | Interest: Article 78 (rate not specified — lex arbitri or lex causae) [VERIFY] | —                                                                                                                          |

[JURISDICTION-SPECIFIC] Always verify the specific interest rate, compounding rules, and
currency of the award under the applicable substantive law and lex arbitri.

**9c. Relief requested**
Draft the relief section with precision:

- State the exact monetary sum requested in the applicable currency (or primary currency with
  conversion methodology)
- State the interest basis, rate, and accrual date
- State legal costs requested (note: many civil law jurisdictions and some arbitration rules
  give the tribunal broad discretion on costs)
- State any non-monetary relief (specific performance, injunction, declaratory relief)
- Include a "catch-all" reservation: "such further or other relief as the Tribunal may deem
  just and appropriate"

---

### Step 10: Procedural Timetable Proposal

Many institutions expect or require the claimant to propose a procedural timetable in the
initial demand or at the first procedural conference. Include a timetable proposal covering:

**Standard commercial arbitration timetable (18-24 months to hearing):**

| Milestone                                                                 | Proposed Timeframe                               |
| ------------------------------------------------------------------------- | ------------------------------------------------ |
| Notice of Arbitration / Request for Arbitration                           | Day 0 (filed today)                              |
| Respondent's Answer / Response                                            | Day 0 + [28-30 days per institution]             |
| Tribunal constitution                                                     | Day 0 + [4-8 weeks]                              |
| First procedural conference (Terms of Reference / Procedural Order No. 1) | Tribunal + [2-4 weeks]                           |
| Statement of Claim (if not included in Notice)                            | [4-6 weeks after PO1]                            |
| Statement of Defence                                                      | [4-6 weeks after SoC]                            |
| Reply on Merits                                                           | [3-4 weeks after SoD]                            |
| Rejoinder                                                                 | [3-4 weeks after Reply]                          |
| Document production (Redfern Schedule)                                    | [Concurrent with pleadings or standalone]        |
| Witness statements                                                        | [2-3 months after pleadings close]               |
| Expert reports                                                            | [Concurrent with or after witness statements]    |
| Pre-hearing conference                                                    | [4-6 weeks before hearing]                       |
| Evidentiary hearing                                                       | [3-6 months after witness/expert submissions]    |
| Post-hearing briefs                                                       | [As ordered after hearing]                       |
| Award                                                                     | [As ordered; typically 3-6 months after hearing] |

**Expedited procedure eligibility** — check and flag if applicable:

- ICC Expedited Procedure: claims ≤ US$3 million (automatically applies unless opted out);
  award within 6 months of Case Management Conference [VERIFY]
- SIAC Expedited Procedure: amount in dispute ≤ S$6 million or exceptional urgency or parties
  agree; final award within 6 months [VERIFY]
- LCIA: Expedited formation available for exceptional urgency (Article 5); no formal expedited
  rules track [VERIFY]
- HKIAC: Expedited procedure: amount in dispute ≤ HK$25 million or exceptional urgency [VERIFY]
- AAA: Expedited procedures for claims ≤ US$100,000 (may opt in for larger) [VERIFY]

**⟁ CLARIFY** — If expedited procedure appears applicable: "The amount in dispute
([amount]) falls within the ICC Expedited Procedure threshold of US$3 million. This would
mean a 6-month timeline and a sole arbitrator unless you opt out. Do you want to (A) proceed
under expedited procedures, or (B) opt out and use the standard procedure? Note that opting
out of ICC expedited procedures can only be done before the Request is filed."

---

### Step 11: Filing and Service Checklist

Before finalizing, run through every item in this checklist:

**Filing requirements:**

| Institution        | Submission Method                                                       | Filing Fee                                              | Commencement Date                                   |
| ------------------ | ----------------------------------------------------------------------- | ------------------------------------------------------- | --------------------------------------------------- |
| **ICC**            | Electronic (NetCase portal or email); copies per Article 4(4) [VERIFY]  | US$5,000 (non-refundable, credited to advance) [VERIFY] | Date Secretariat receives the complete Request      |
| **LCIA**           | Electronic only (efile.lcia.org or email) [VERIFY]                      | Registration fee per Schedule of Costs [VERIFY]         | Date Registrar receives the complete Request        |
| **AAA Commercial** | Online (adr.org) or email + administrative filing fee                   | Varies by amount; see AAA fee schedule [VERIFY]         | Date Administrator receives complete Demand + fee   |
| **ICDR**           | Online (icdr.org) or email + administrative filing fee                  | Varies by amount; see ICDR fee schedule [VERIFY]        | Date Administrator receives Notice                  |
| **SIAC**           | Online (siac.org.sg) or email; copy to Respondent simultaneously        | Filing fee per Schedule of Fees [VERIFY]                | Date Registrar receives complete Notice             |
| **HKIAC**          | Email or online portal; Registration Fee must accompany filing [VERIFY] | Registration fee per Schedule 1 [VERIFY]                | Date HKIAC receives initial Notice (if later cured) |

**Service requirements checklist:**

- [ ] Demand delivered to ALL respondents simultaneously with filing — documentary proof retained
- [ ] Service method complies with institutional rules (certified mail, courier, email, or as
      the arbitration agreement specifies)
- [ ] Date and mode of service confirmed in writing to the institution
- [ ] Legal representatives of respondent copied (if known)
- [ ] Any contractually required notice of dispute sent before or simultaneously with the demand

**Document bundle checklist:**

- [ ] Cover letter identifying the institution and reference number (if assigned)
- [ ] Notice / Request for Arbitration (signed by counsel of record or authorized representative)
- [ ] Full text of the arbitration agreement (or relevant contract pages)
- [ ] Copy of underlying contract(s)
- [ ] Supporting documents referenced in the demand (invoices, correspondence, etc.)
- [ ] Power of attorney or authorization for counsel (if required by the institution)
- [ ] Third-party funding disclosure (HKIAC, and any other institution requiring it) [VERIFY]
- [ ] Payment of filing fee (bank transfer, credit card, as accepted by institution)

---

### Step 12: Quality Verification

Before finalizing the demand, run these quality checks:

**12a. Institution compliance check**
For each mandatory element in the applicable institution's rules, confirm it is present:

| Element                               | ICC Art. 4 | LCIA Art. 1 | ICDR Art. 2 | SIAC Art. 3 | HKIAC Art. 4 | Present? |
| ------------------------------------- | ---------- | ----------- | ----------- | ----------- | ------------ | -------- |
| Party names/addresses                 | ✓          | ✓           | ✓           | ✓           | ✓            |          |
| Representative details                | ✓          | ✓           | ✓           | ✓           | ✓            |          |
| Arbitration agreement text            | ✓          | ✓           | ✓           | ✓           | ✓            |          |
| Nature/circumstances of dispute       | ✓          | ✓           | ✓           | ✓           | ✓            |          |
| Relief sought (quantified)            | ✓          | ✓           | ✓           | ✓           | ✓            |          |
| Seat proposal (if not in clause)      | ✓          | ✓           | —           | —           | —            |          |
| Language proposal                     | ✓          | —           | —           | —           | —            |          |
| Number of arbitrators                 | ✓          | —           | —           | ✓           | ✓            |          |
| Arbitrator nomination                 | ✓          | —           | —           | ✓           | ✓            |          |
| Governing law proposal                | ✓          | —           | —           | —           | —            |          |
| Confirmation of service on respondent | ✓          | ✓           | —           | ✓           | ✓            |          |
| Third-party funding disclosure        | —          | —           | —           | —           | ✓            |          |

**12b. Citation Quality Gates** — Run silently before delivery (see Quality Assurance section)

**12c. Limitations check**

- [ ] Confirm each claim falls within the applicable limitation period
- [ ] Confirm the demand is filed in a manner that tolls the limitation period
- [ ] Flag any claim where the limitation analysis is uncertain as requiring verification

**12d. Self-Interrogation for high-severity items** — Apply to any CRITICAL DEFECT identified

**12e. Final completeness review**

- [ ] All claims asserted explicitly — reserve rights to add new claims only with tribunal leave
- [ ] All parties joined who need to be joined — adding parties after constitution is difficult
- [ ] All contracts / agreements in dispute identified — multi-contract disputes may require
      separate analysis of whether the arbitration clause covers all contracts
- [ ] Statement of relief is complete and internally consistent
- [ ] No inadvertent admissions in the factual narrative
- [ ] Arbitration agreement is correctly quoted and the correct version is used

---

## Institution-Specific Requirements Reference

### ICC — 2021 Arbitration Rules (Request for Arbitration, Article 4)

**Mandatory content per Article 4(3):**

1. Full name, description, address, and contact details of each party
2. Full name, address, and contact details of any representative of the claimant
3. Description of the nature and circumstances of the dispute giving rise to the claim(s)
4. Statement of relief sought, including, to the extent possible, an indication of any amounts
   claimed and the relief or remedy sought; if the claims cannot be quantified, a good-faith
   estimate of their monetary value
5. The relevant arbitration agreement(s) and, if applicable, information on claims arising
   under multiple agreements
6. All relevant particulars concerning the number of arbitrators and their choice in
   accordance with Articles 12 and 13
7. Any observations or proposals as to the place of arbitration, the applicable law, and
   the language of the arbitration

**Article 4(4) submission requirements:**

- File by electronic submission (ICC NetCase or email to the Secretariat)
- Provide sufficient copies for all parties, plus one for each arbitrator and one for the Secretariat
- Pay non-refundable filing fee of **US$5,000** (credited against advance on costs)
- No required form — claimants may use any format satisfying Article 4(3) requirements

**Article 5 — Respondent's Answer:**

- 30 days from the date the Secretariat transmits the Request to the Respondent
- Must include: representative details; comments on nature, circumstances, and basis of dispute;
  observations/proposals on arbitrators, seat, applicable law, and language; nomination of
  arbitrator (if applicable); any counterclaims (with same information as an RfA)
- Extension available from Secretariat if respondent includes observations on arbitrator nomination

**Article 6 — Effect of Arbitration Agreement:**

- If respondent challenges the existence, validity, or scope of the arbitration agreement,
  the arbitration proceeds unless it is prima facie manifest that no agreement exists
- The arbitral tribunal ultimately rules on its own jurisdiction (kompetenz-kompetenz)

**Article 29 — Emergency Arbitrator:**

- Must be filed before the commencement of arbitration or with the Request
- Application fee: **US$40,000** (US$10,000 administrative fee + US$30,000 emergency arbitrator
  fee, credited to advance on costs) [VERIFY current amounts]
- Application must state: nature/circumstances giving rise to the application; relief sought;
  grounds for urgency; parties' arbitration agreement; contact details
- Emergency arbitrator appointed within 2 business days
- Does not apply unless specifically incorporated: for agreements pre-dating 1 January 2012 [VERIFY]

**ICC Costs (ad valorem) — indicative only:**

- ICC administrative fee + arbitrators' fees calculated as a percentage of amount in dispute
  on a regressive scale; use the ICC cost calculator for current amounts [VERIFY]
- Advance on costs typically demanded from both parties; failure to pay leads to dismissal

---

### LCIA — 2020 Arbitration Rules (Request for Arbitration, Article 1)

**Mandatory content per Article 1.1:**

1. Full names, nationalities, and all contact details for all parties
2. Full names, nationalities, positions, and all contact details for all known legal representatives
3. Full terms of the written arbitration agreement(s) being invoked
4. Copy of the relevant contractual documentation and arbitration agreement
5. A brief statement summarizing the nature and circumstances of the dispute and the relief claimed,
   including a good-faith estimate of any monetary claims
6. A statement of any procedural matters already agreed in writing between the parties, or
   any procedural matters proposed by the claimant
7. Confirmation (with supporting documentary proof) that copies of the Request and all
   attachments have been delivered to all other parties

**LCIA submission requirements:**

- Electronic submission only (e-filing portal at efile.lcia.org or email to the Registrar)
- 2 hard copies for a sole arbitrator, 4 for a panel of 3 arbitrators [VERIFY post-2020 updates]
- Commencement date = the date the complete Request is received by the Registrar
- Registration fee per LCIA Schedule of Costs (hourly-rate based, not ad valorem) [VERIFY]

**Article 2.1 — Respondent's Response:**

- 28 days from the Commencement Date (extendable by the LCIA Court on application)
- Must include: full names/contacts of respondent and representatives; confirmation or denial
  of claims; any counterclaims (with same information as a Request); comments on procedural
  matters; confirmation of delivery to all parties
- Failure to file a Response does not preclude respondent from asserting objections later

**Article 5 — Expedited Formation of the Tribunal:**

- Available on grounds of **exceptional urgency** only (not merely commercial urgency)
- Written application to the Registrar; set out specific grounds; notify all parties
- LCIA Court determines application expeditiously without reasons
- Distinguished from emergency arbitrator (Article 9B): expedited formation accelerates
  constitution of the full tribunal (within days instead of weeks)

**Article 9B — Emergency Arbitrator:**

- Available for exceptional urgency before tribunal is constituted
- Written application to Registrar; specify grounds for urgency, specific claim, reasons for
  emergency; must deliver/notify all parties
- Special fee required; application dismissed without payment [VERIFY current fee]
- Applies only to arbitration agreements dated on or after 1 October 2014, unless written
  opt-in for earlier agreements

---

### AAA Commercial Arbitration Rules (2022 Revision) and ICDR International Arbitration Rules (2021 Revision)

**AAA Commercial Rules — Demand for Arbitration:**

- Submit: Demand for Arbitration + copy of applicable arbitration agreement + administrative
  filing fee (payable before matter is properly filed)
- Serve respondent simultaneously: copy of demand + all supporting documents
- Less prescriptive than international institutions — no mandatory detailed content template
  but best practice requires: full party identification; description of dispute; amount claimed;
  copy of arbitration clause; requested relief; proposed arbitration location

**ICDR International Arbitration Rules — Notice of Arbitration (Article 2):**

**Mandatory content:**

1. Demand that the dispute be referred to arbitration
2. Names, addresses, telephone numbers, fax numbers, and email addresses of each party and
   their known representatives
3. Copy of the entire arbitration clause or agreement being invoked
4. If claims arise under multiple agreements: separate copy of the agreement for each claim
5. Commencement date = date the Administrator receives the Notice

**ICDR filing requirements:**

- Submit online at icdr.org or by email
- Administrative filing fee due with filing (amount in dispute-based scale) [VERIFY current fee]
- No institutional fee for witnesses or evidence — more streamlined than ICC
- Apply separate fee schedule for ICDR domestic-international track

**Key domestic AAA vs. international ICDR differences:**

| Feature              | AAA Commercial               | ICDR International                               |
| -------------------- | ---------------------------- | ------------------------------------------------ |
| Governing Rules      | AAA Commercial Rules 2022    | ICDR International Rules 2021                    |
| Primary Users        | US domestic disputes         | Cross-border disputes; non-US parties            |
| Pleading formality   | Flexible — less prescriptive | Structured mandatory content (Art. 2)            |
| Arbitrator roster    | Domestic US arbitrators      | International arbitrators; ICDR maintained panel |
| Language             | English default              | Multi-language; translation at discretion        |
| Discovery            | Broad by default             | Narrower; IBA Rules on Evidence common           |
| Emergency Arbitrator | Article 38 — available       | Article 7 — available                            |

---

### SIAC — 2025 Arbitration Rules (formerly 2016 Rules) (Notice of Arbitration, Article 3)

**Mandatory content per Rule 3.1:**

1. A request that the dispute be referred to arbitration under the SIAC Rules
2. Full names, nationality, addresses, and contact details of all parties and known representatives
3. A copy of the arbitration agreement(s) being invoked
4. A description of the general nature of the dispute and the circumstances giving rise to it
5. A statement of the relief sought, and where possible, an indication of the amounts claimed
6. A proposal for the number of arbitrators (Rule 9.1) if not already agreed
7. If the claimant nominates an arbitrator: the arbitrator's name, address, and contact details

**SIAC submission requirements:**

- File Notice with the Registrar AND simultaneously deliver a copy to the Respondent
- Notify the Registrar of the date and mode of service on the Respondent
- Commencement date = date of receipt of complete Notice by Registrar (Rule 3.2)
- Notice is "complete" when Rule 3.1 and Rule 6.1(b) (filing fee) requirements are satisfied,
  or when SIAC has accepted substantial compliance

**SIAC filing fee and costs:**

- Filing fee based on amount in dispute — see SIAC Schedule of Fees [VERIFY current amounts]
- Arbitrators' fees: SIAC scales per Schedule of Fees [VERIFY]

**Rule 30.3 — Emergency Arbitrator:**

- Application filed to the Registrar (before or together with Notice of Arbitration)
- Must include: claimant's full name/address; description of dispute; arbitration agreement;
  emergency relief sought; grounds for the urgency; reason the emergency arbitrator is necessary;
  confirmation that all parties have been notified or explain why notice was not possible
- Emergency arbitrator appointed within 1 business day [VERIFY]
- Fees: filing fee + emergency arbitrator fee per Schedule [VERIFY]

**Expedited Procedure (Rule 5) — SIAC 2025:**

- Applies when amount in dispute ≤ S$6,000,000 (approximately US$4.5M) [VERIFY current threshold]
- Or when the parties agree in writing; or when exceptional urgency exists
- Final award within 6 months of constitution of the tribunal
- Sole arbitrator (even if 3-arbitrator panel was agreed)
- Opt out must be in writing before appointment of the tribunal

**Rule 7 — Respondent's Response:**

- 14 days from receipt of Notice of Arbitration
- Must include: confirmation/denial of claims; any counterclaims; proposal on arbitrators

---

### HKIAC — 2018 Administered Arbitration Rules (Notice of Arbitration, Article 4)

**Mandatory content per Article 4.3:**

1. A request that the dispute be referred to arbitration under the HKIAC Rules
2. Full names, known addresses, fax numbers, and email addresses of all parties and known representatives
3. A copy of the arbitration agreement invoked
4. A copy of the contract(s) or legal instrument(s) giving rise to the dispute, or reference thereto
5. A description of the general nature of the claim and the amount involved, if any
6. The relief or remedy sought
7. If the claimant proposes a sole arbitrator: contact details of proposed arbitrator nominee
8. If the arbitration agreement provides for 3 arbitrators: the claimant's proposed arbitrator's contact details
9. A proposal as to the number of arbitrators (1 or 3) if not already agreed
10. If a party is using third-party funding (Article 44): confirmation of existence of funding
    agreement and identity (but not terms) of the third-party funder

**HKIAC submission requirements:**

- Notice must be accompanied by the Registration Fee per HKIAC Schedule 1 [VERIFY current fee]
- If the Notice is non-compliant or fee is not paid: HKIAC requests remedy within a prescribed time
- If claimant complies: arbitration deemed commenced on date of the initial (non-compliant) Notice
- Must notify HKIAC of the date of Respondent's receipt and method of service
- Claimant must send all materials to all Respondents simultaneously

**Respondent's Answer (Article 5):**

- 30 days from receipt of Notice
- Respond to claims; assert defenses; file counterclaims (with same information as a Notice)
- Nominate arbitrator or make proposals on tribunal composition

**Article 44 — Third-Party Funding:**

- Parties must promptly disclose to HKIAC and all other parties: (a) existence of a funding
  agreement; (b) identity of the third-party funder. Terms need not be disclosed.
- Disclosure obligation is ongoing — must notify if funding commences during proceedings
- This is one of the most explicit funding disclosure obligations in international arbitration [VERIFY]

---

## Response / Answer Drafting (Mode 2)

When drafting a Response or Answer to an incoming demand:

**Step R1 — Assess the incoming demand**

- Verify that the demand meets the institutional mandatory content requirements (use the
  Institution-Specific Requirements Reference section above)
- Check whether the demand was properly served — note any service defects (reserve but do not
  waive the objection by participating)
- Verify the commencement date — statute of limitations assessment for any counterclaims
- Identify any jurisdictional defects that must be raised as objections in the Response

**Step R2 — Jurisdictional objections**
If any of the following apply, raise the objection in the Response — failure to raise
jurisdictional objections promptly may constitute a waiver under most institutional rules:

- The arbitration agreement is invalid, void, or non-binding (e.g., unsigned, unsigned by
  authorized signatory, consumer/employment claims in some jurisdictions)
- The claims are outside the scope of the arbitration agreement
- Pre-arbitration conditions have not been satisfied
- The demand was defectively served (note service defect but may need to participate)
- The arbitration agreement has expired or the claims are time-barred

**⟁ CLARIFY** — "Are there any grounds to challenge the tribunal's jurisdiction? Raising a
jurisdictional objection in the Response does not necessarily end the arbitration, but failing
to raise it may constitute a waiver. Do you want to: (A) Raise jurisdictional objections in
the Response while reserving rights, (B) Proceed on the merits without objecting, or
(C) Apply to the seat court to restrain the arbitration? Note: participating in the arbitration
without objecting may amount to a waiver of any prior court proceedings contrary to the
arbitration agreement."

**Step R3 — Draft the Response**

Include per institutional requirements:

1. Full name, nationality, and contact details of respondent and representatives
2. Confirmation or denial of each claim — admit what can be admitted, deny what is disputed,
   and provide a brief statement of the respondent's position on each issue
3. Any jurisdictional objections (clearly labeled as without waiver of rights to object)
4. Proposals on arbitrators, seat, language, and governing law (if different from claimant's)
5. Nomination of respondent's arbitrator (if 3-member tribunal)
6. Statement of any counterclaims — must include same level of detail as a demand

**Step R4 — Counterclaim assessment**

- Do any counterclaims arise out of the same transaction or relationship? These should be
  asserted now — failing to assert related counterclaims in the Response may limit the ability
  to introduce them later without tribunal leave
- Quantify counterclaims to the extent possible — affects ad valorem fees and expedited
  procedure eligibility
- For ICC, LCIA, and HKIAC: counterclaim triggers a new advance on costs contribution from
  the claimant in respect of the counterclaim

---

## Defect Classification System

Classify findings from a demand review using this three-tier system:

### CRITICAL DEFECT — Potentially Voids the Demand or Creates Jurisdictional Risk

The defect could result in: (a) rejection of the demand by the institution, (b) a successful
jurisdictional challenge by the respondent, (c) an unenforceable award due to procedural
defects, or (d) claims being time-barred.

**Examples:**

- Missing or incorrect arbitration agreement citation
- Failure to serve all respondents simultaneously and documented
- Commencement without paying the required filing fee (where the fee is a condition of commencement)
- Claims that appear to be outside the limitation period without analysis of tolling
- Demand filed under the wrong institution's rules (not matching the arbitration clause)
- No arbitration agreement covering the dispute asserted
- Emergency arbitrator application with no genuine urgency (risks sanctions and damages reputation)

**Action**: Correct before filing. Do not file a demand with a CRITICAL DEFECT without express
legal advice on whether the defect can be cured or waived.

### MATERIAL DEFICIENCY — Weakens the Demand or Creates Strategic Vulnerability

The deficiency does not necessarily void the demand but creates a risk or opportunity for the
respondent to exploit, creates procedural delays, or weakens the claimant's case on the merits.

**Examples:**

- Quantification of claims is vague or unsupported (respondent can challenge as speculative)
- Arbitrator nomination lacks CV or independence statement (delays constitution)
- Seat is not proposed (institution must resolve; causes delay)
- Pre-arbitration conditions may not have been fully complied with (respondent can object)
- Third-party funding not disclosed in jurisdictions requiring disclosure
- Factual narrative omits key documents (creates discovery pressure)
- Statement of claim omits a colorable legal theory (may be barred from adding later)

**Action**: Address before filing where possible. Flag in the output with recommended remedy.

### RECOMMENDED ADDITION — Strengthens the Demand or Improves Procedural Position

The addition is not mandatory under institutional rules but would improve the demand's
effectiveness, clarify the claimant's position, or reduce procedural friction.

**Examples:**

- A proposed procedural timetable (signals preparedness and frames expectations)
- A brief statement of available evidence (foreshadows the strengths of the claimant's case)
- A mediation proposal (demonstrates good faith; may accelerate settlement)
- A request for bifurcation of jurisdiction and merits (for complex jurisdictional issues)
- A proposed list of issues (if agreed ICC/SIAC Terms of Reference approach)

**Action**: Consider including; flag the strategic benefit.

---

## Prioritization Framework

When there are multiple issues to address, prioritize in this order:

**Tier 1 — File-or-Not-File (address before any filing)**

1. Statute of limitations / prescription (a time-barred claim is fatal)
2. Arbitration agreement validity (no clause = no jurisdiction)
3. Scope of the arbitration agreement (claims outside scope cannot proceed)
4. Filing fee and commencement date (institutional requirements for valid commencement)
5. Service on all respondents (documentary proof essential)

**Tier 2 — Must-Fix Before Filing (institutional compliance)**

1. Mandatory content completeness per applicable institutional rules
2. Simultaneous service on respondents with documentary proof
3. Pre-arbitration conditions compliance
4. Third-party funding disclosure (where required)
5. Arbitrator nomination (where required at commencement)

**Tier 3 — Material Enhancements (address if time permits)**

1. Full quantification of all claims with backup calculations
2. Complete factual narrative with key documents annexed
3. Arbitrator nomination with full CV and preliminary independence confirmation
4. Proposed procedural timetable
5. Emergency / provisional measures application (if needed)

**Tier 4 — Strategic Additions (include if available)**

1. Settlement posture and reservation of without-prejudice discussions
2. Proposed list of issues or Terms of Reference framework
3. Evidence inventory and disclosure framework proposal
4. Expert witness identification (for complex technical disputes)
5. Proposed document production protocol

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                     | Fail Action                                       |
| -------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **Source**     | Every procedural requirement cites the specific rule/article (e.g., "ICC Rules 2021, Art. 4(3)")         | Add citation or mark "[UNVERIFIED]"               |
| **Format**     | All rule citations follow the institutional naming convention consistently                               | Fix format                                        |
| **Currency**   | Every cited rule confirmed to be the current version in force                                            | Flag "[CHECK CURRENCY — rules update frequently]" |
| **Domain**     | Analysis stays within the applicable institutional rules; no bleed from other institutions' requirements | Remove or flag institutional bleed                |
| **Confidence** | Uncertainty explicitly stated, not hidden (especially for non-English jurisdiction rules)                | Add confidence qualifier                          |

### Self-Interrogation for CRITICAL DEFECTS

For any item classified as a CRITICAL DEFECT, apply this 3-pass review before delivering:

**Pass 1 — Procedural Chain Integrity**: Does the defect classification follow logically from
the institutional rule cited? Would the institution actually reject the demand for this reason,
or would it request a cure? Would the respondent's jurisdictional challenge succeed on this basis?

**Pass 2 — Completeness**: Have all relevant institutional rules, lex arbitri provisions, and
potential curing mechanisms been considered? Has the specific version of the institutional
rules that applies to this arbitration agreement been confirmed?

**Pass 3 — Challenge**: What is the strongest argument that the defect is not fatal? Under what
circumstances might a tribunal or institution overlook this defect? Is there a curing step
available before the limitation period expires?

### Confidence Scoring

| Level        | Range     | Meaning                                                               | Action                                                            |
| ------------ | --------- | --------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled institutional rule, clear article                             | State with confidence                                             |
| **High**     | 0.80-0.94 | Well-established rule, minor version uncertainty                      | State with brief caveat                                           |
| **Probable** | 0.60-0.79 | General practice, institution-specific nuance possible                | State with reasoning and verification recommendation              |
| **Possible** | 0.40-0.59 | Genuinely uncertain (e.g., recent rule changes, unusual jurisdiction) | Flag for counsel verification with both interpretations           |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative                                               | Do not assert; flag "[UNCERTAIN — counsel verification required]" |

### Glass Box Audit Trail

Append this section to all demand drafts and reviews:

```yaml
glass_box:
  skill_name: "legalcode-arbitration-demand-drafter"
  mode: "[Demand Draft / Answer Draft / Emergency Application / Review]"
  institution: "[ICC 2021 / LCIA 2020 / AAA 2022 / ICDR 2021 / SIAC 2025 / HKIAC 2018 / UNCITRAL / Other]"
  seat_of_arbitration: "[City, Country]"
  lex_arbitri: "[Applicable procedural law]"
  substantive_governing_law: "[Applicable substantive law]"
  amount_in_dispute: "[Currency and amount, or estimated range]"
  expedited_procedure_eligible: "[Yes / No / Unknown]"
  emergency_application_included: "[Yes / No]"
  legalcode_mcp: "[Connected / Not connected]"
  statute_of_limitations_verified: "[Yes / No — [verification status and flagged claims if any]]"
  service_documented: "[Yes / No / N/A — filing not yet made]"
  third_party_funding_disclosed: "[Yes / Not applicable / Required but not yet disclosed]"
  critical_defects_found: "[Number] — [Brief summary]"
  material_deficiencies_found: "[Number] — [Brief summary]"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  citations_verified: "[Number] VERIFIED / [Number] UNVERIFIED"
  confidence: "[HIGH / MEDIUM / LOW] — [Rationale]"
  limitations:
    - "Institutional rules verified as of [date] — verify current version before filing"
    - "Filing fees stated as approximate — verify current schedule before filing"
    - "Limitation period analysis requires counsel verification under applicable law"
    - "[Any other limitations]"
  reviewer: "AI-assisted — requires qualified international arbitration counsel review before filing"
```

---

## Anti-Patterns

These are the most common and consequential mistakes in arbitration demand drafting. Do not
repeat them.

1. **Filing without verifying the limitation period.** The most catastrophic error. A
   time-barred claim results in defeat on the merits even if the underlying legal claim is
   sound. Always verify the applicable limitation period, whether and how commencement of
   arbitration tolls it, and whether any claim is close to or past the period. If uncertain,
   file before the deadline and sort out the details later.

2. **Using the wrong institutional rules.** Filing under ICC rules when the clause specifies
   LCIA, or vice versa. The demand will be rejected or the respondent will have a jurisdictional
   defense. Read the arbitration clause carefully — if the institution is misspelled or refers
   to a defunct institution, research whether the clause can be saved by interpretation.

3. **Inadequate proof of service.** Filing the demand without obtaining and retaining
   documentary proof that the respondent received it simultaneously. Without proof of service,
   the commencement date is disputed and the respondent can challenge jurisdiction on the basis
   of inadequate notice. Use multiple delivery methods (courier + email) and retain delivery
   receipts.

4. **Vague or unquantified claims.** Stating "damages in an amount to be determined" without
   providing at least a good-faith estimate. In ad valorem systems (ICC, LCIA), this affects
   fee calculation. For the tribunal, it signals a weak damages case and gives the respondent
   room to argue the claim is speculative. Quantify every head of damages with supporting
   calculations as best as the evidence allows.

5. **Failing to include all claims arising from the same transaction.** Claims not included
   in the initial demand may require tribunal leave to add later — and leave may be denied if
   the respondent would be prejudiced. Apply issue-spotting discipline to ensure all contract
   breaches, all damages heads, and all relevant time periods are included.

6. **Omitting or incorrectly quoting the arbitration agreement.** Every institution requires
   the full text (or at minimum a clear reference to) the arbitration agreement. Quote it
   verbatim from the signed document. Do not paraphrase. An incorrect quote may suggest the
   clause does not cover the asserted claims.

7. **Ignoring pre-arbitration conditions.** Many contracts require a notice of dispute,
   cooling-off period, negotiation, or mediation before arbitration can commence. Failure to
   comply gives the respondent a procedural objection (though it usually does not permanently
   bar arbitration). Document compliance with all pre-conditions or analyze whether they have
   been waived by the respondent's conduct.

8. **Nominating an arbitrator with undisclosed conflicts.** The nominated arbitrator will be
   required to disclose all relationships with the parties, counsel, and the dispute. Failing
   to conduct a pre-nomination conflict check leads to delays (the nomination is challenged),
   embarrassment, and potential award annulment if the conflict is serious enough. Always
   conduct an IBA Guidelines conflict analysis before nominating.

9. **Applying for an emergency arbitrator without genuine urgency.** Emergency arbitration
   has a high threshold: imminent, irreparable harm that cannot wait for the full tribunal
   to be constituted. Using the emergency procedure for tactical reasons (to get an early
   hearing) or without meeting the threshold wastes the emergency arbitration fee and damages
   credibility with the institution and eventual tribunal.

10. **Failing to disclose third-party funding.** HKIAC (Article 44) and increasingly other
    institutions require disclosure of third-party funding arrangements. Non-disclosure can
    lead to sanctions, adverse costs orders, and in some jurisdictions, challenges to the
    award. Disclose promptly and update the disclosure if funding is obtained during proceedings.

11. **Confusing the seat and the venue.** The **seat** of arbitration is a legal concept that
    determines the lex arbitri — it need not be where the hearings physically take place. The
    **venue** is where the parties actually hold hearings. Hearings can take place anywhere
    (even if the seat is London); the seat determines which national courts supervise the
    arbitration and which annulment regime applies. Never use "seat" and "venue" interchangeably.

12. **Submitting pathological clauses without analysis.** If the arbitration agreement is
    defective (names a defunct institution, has internally contradictory terms, requires
    unanimous consent), filing a demand under it will provoke a jurisdictional challenge.
    Analyze the clause first; consider whether a submission agreement with the respondent
    would resolve the problem; or seek a declaratory ruling from the supervisory court.

13. **Asserting claims in the wrong currency or without interest.** International awards
    often include substantial interest. Failing to claim pre-award interest (from the date of
    breach or the date of demand) may result in losing years of interest. Identify the
    applicable interest rate and compounding rules early and include a specific interest claim
    in the demand.

14. **Single-party perspective in a multi-party dispute.** When the dispute involves three
    or more parties (e.g., employer, contractor, subcontractor in a construction dispute),
    consolidation and joinder rules become critical. Filing demands in parallel arbitrations
    against different respondents wastes resources and risks inconsistent awards. Analyze
    whether consolidation is available under the applicable institutional rules.

15. **Ignoring the Siemens/Dutco problem.** In a 3-member panel with multiple respondents
    who cannot agree on a joint nominee, the institution appoints all three arbitrators (to
    preserve the principle of equal treatment). This is often tactically disadvantageous for
    the respondents. Plan for this if the claimant is the one with multiple respondents who
    may struggle to agree.

16. **Over-relying on AI-generated drafts without counsel review.** Arbitration demands have
    legal consequences from the moment of filing. The demand establishes the scope of the
    claims, the commencement date, the applicable rules, and the tribunal's jurisdiction. An
    AI-generated draft is a starting point, not a final product. Always have qualified
    international arbitration counsel review and approve before filing.

---

## Writing Standards

Apply these standards before delivering any demand draft:

**1. Precision over prolixity.** International arbitration tribunals are experienced
professionals. Long, argumentative demands are not more persuasive — they are harder to
read and dilute the key points. Write the shortest demand that includes every mandatory
element and makes the case clearly.

**2. Chronological factual narrative.** The facts section should read like a well-organized
timeline. Start at the beginning of the parties' relationship, trace the key events, and
end with the breach or event giving rise to the dispute. Use dates for every event.

**3. Specific legal claims.** Each claim should identify: (a) the legal theory, (b) the
specific contract provision or legal rule violated, (c) the facts satisfying each element
of the legal theory, and (d) the resulting damages. Do not assert "breach of contract"
without specifying which contract provision was breached and how.

**4. Quantify every damage.** Even early-stage estimates are better than none. Use formulas
or tables to break down complex damage calculations. Identify what additional information
or expert evidence is needed to finalize the calculation.

**5. Active voice.** "Respondent failed to deliver the goods" is stronger and clearer than
"The goods were not delivered." Write in active voice throughout the factual narrative.

**6. Define terms consistently.** If the claimant is a company named "Acme Corporation
Ltd.," refer to it as "Acme" or "Claimant" consistently — not alternating between the two.
Define terms in the Parties section and use them throughout.

**7. No inadvertent admissions.** Review every statement in the factual narrative for
whether it could be used against the claimant in the arbitration or in court. Counsel should
review the demand for privileged communications that should not be disclosed.

**8. Plain English in the procedural section.** Institutional compliance sections (service,
commencement, arbitrator nomination) should be written in plain, direct language — not
legalese. The tribunal administrator and institution staff are the primary audience for
these sections.

**Quality gates before delivery:**

- [ ] Every mandatory element from the institutional rules checklist is present and verified
- [ ] All monetary claims are quantified (or a good-faith estimate is provided with basis)
- [ ] The arbitration agreement is quoted verbatim and correctly
- [ ] The relief section is complete, specific, and internally consistent
- [ ] All [VERIFY] tags are either resolved or explicitly flagged for counsel
- [ ] The Glass Box audit trail is complete

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.
legalcode-mcp provides access to statutes, case law, and regulatory materials across jurisdictions.

**With legalcode-mcp connected (preferred):**

- Search for jurisdiction-specific limitation period statutes for the applicable governing law
- Verify current versions of institutional arbitration rules
- Research the arbitration law at the seat (lex arbitri) for mandatory provisions
- Search for leading case law on arbitration agreement scope and enforceability in the jurisdiction
- Research damages law under the applicable substantive law
- Verify New York Convention status of the seat and enforcement states
- Save research results to `/tmp/legalcode-arbitration-research.md`

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Rely on the institution-specific requirements in this skill document as the baseline
- Explicitly instruct the user to verify all rule citations, limitation periods, and legal
  authority with counsel or authoritative sources before filing

---

## Localization Notes

**English-language seat jurisdictions (London, New York, Singapore, Hong Kong)**:
These seats have the most developed international arbitration jurisprudence. The institutional
rules operate within well-established arbitration law frameworks. Demands for disputes with
these seats are most likely to produce predictable, enforceable awards.

**French seat (Paris)**:
French arbitration law (CPC Arts. 1442-1527) is extremely supportive of international
arbitration. The Paris Court of Appeal is the supervisory court. French law takes a liberal
approach to arbitrability and provides a supportive interim measures regime. [VERIFY]

**Swiss seat (Geneva, Zurich, Lugano)**:
Switzerland's PIL Chapter 12 (Arts. 176-194) governs international arbitration. The Federal
Supreme Court is the supervisory court. Switzerland is known for its strict confidentiality
protections and sovereign immunity waiver approach. [VERIFY]

**Civil law jurisdictions generally:**
Demands in civil law tradition proceedings often take a more "memorials" style — detailed
written submissions with all evidence annexed from the start. The IBA Rules on the Taking of
Evidence in International Arbitration are commonly used to bridge common law / civil law
document production expectations.

**Non-English language requirements:**
If the arbitration agreement specifies a non-English language, the demand must be in that
language (or translated). Many institutions accept English for the initial filing if translation
is provided later. [VERIFY per institution]

---

## Output Format Template

Deliver the arbitration demand output using this structure:

```markdown
# [INSTITUTION] Arbitration Demand

## [Claimant Full Legal Name] v. [Respondent Full Legal Name]

---

## NOTICE OF ARBITRATION / REQUEST FOR ARBITRATION

**To:** [Institution Name and Secretariat Address]
**Date:** [Filing Date]
**Reference:** [Leave blank — to be assigned by institution]

---

### I. Parties

**Claimant:**
[Full legal name]
[Entity type and jurisdiction of incorporation]
[Registered address]
[Contact: email, phone]

**Claimant's Legal Representatives:**
[Counsel name, firm, address, email, phone]

**Respondent:**
[Full legal name]
[Entity type and jurisdiction of incorporation]
[Last known registered address]
[Contact: email, phone if known]

---

### II. Arbitration Agreement

The Claimant commences this arbitration pursuant to the arbitration agreement contained in:

[Full citation of the contract: name, date, parties]

The relevant arbitration clause provides as follows:

> "[Verbatim text of the arbitration clause]"

---

### III. The Dispute

#### A. Background

[2-3 paragraph background on the parties' relationship and the underlying contract(s)]

#### B. Nature and Circumstances of the Dispute

[Narrative of the facts giving rise to the dispute — chronological, specific, with dates]

#### C. Claimant's Claims

[Summary of each claim with the legal basis]

---

### IV. Relief Sought

The Claimant respectfully requests that the Arbitral Tribunal:

1. **Award monetary damages** of [currency amount], representing:
   a. [Head of damages 1]: [Amount] — [Basis]
   b. [Head of damages 2]: [Amount] — [Basis]
   [...]

2. **Award pre-award interest** on the above amounts at [rate] from [date] to the date of the award.

3. **Award post-award interest** on all sums due at [rate] from the date of the award until payment.

4. **Award the costs** of this arbitration, including the Claimant's legal costs, in full.

5. **[Any non-monetary relief]**: [Specific description of what the Respondent must do or refrain from doing.]

6. Such further or other relief as the Tribunal may deem just and appropriate.

---

### V. Arbitral Tribunal

**Proposed number of arbitrators:** [1 or 3]

**Claimant's Nominated Arbitrator (if 3-member panel):**
[Name, title, firm, address, email]
[Brief statement of credentials]

**Observations on sole arbitrator selection (if applicable):**
[Proposed criteria or candidate(s)]

---

### VI. Proposed Seat, Language, and Governing Law

**Seat of Arbitration:** [City, Country]
**Language of Arbitration:** [Language]
**Substantive Governing Law:** [Jurisdiction]

---

### VII. Proposed Procedural Timetable

[Table from Step 10 above, adapted to the specific dispute]

---

### VIII. Service Confirmation

The Claimant confirms that a copy of this Request for Arbitration, together with all accompanying
documents, has been delivered to the Respondent simultaneously with filing, by [method] on [date],
to the following address: [address].

[Supporting delivery documentation to be attached as Exhibit [X]]

---

### IX. Certification

The undersigned, duly authorized to act on behalf of the Claimant, hereby certifies that the
information contained in this Notice is complete and accurate to the best of [their] knowledge.

Signed: \***\*\*\*\*\***\_\_\_\***\*\*\*\*\***
Name: [Counsel name]
Title: [Counsel of record / Authorized representative]
Firm: [Firm name]
Date: [Date]
Email: [Email]
Phone: [Phone]

---

### EXHIBITS

- Exhibit 1: [Contract name] dated [date]
- Exhibit 2: [Arbitration agreement, if standalone]
- Exhibit 3: [Key correspondence supporting the dispute]
- Exhibit 4: [Damages calculation or financial summary]
- Exhibit 5: [Proof of service on Respondent]
  [...]

---

## STATEMENT OF CLAIM

[See Step 9 structure — I. through IX.]

---

## DEFECT AND QUALITY REVIEW

### CRITICAL DEFECTS

[List with specific rule citations, risk description, and recommended remedy]

### MATERIAL DEFICIENCIES

[List with specific rule citations, risk description, and recommended remedy]

### RECOMMENDED ADDITIONS

[List with strategic rationale]

---

## GLASS BOX AUDIT TRAIL

[YAML block per the Glass Box Audit Trail template above]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis from scratch (Mode A) using a 2-agent
research pipeline covering: ICC Arbitration Rules 2021 (Articles 4, 5, 6, 29); LCIA Arbitration
Rules 2020 (Articles 1, 2, 5, 9B); ICDR International Arbitration Rules 2021 (Article 2); AAA
Commercial Arbitration Rules 2022; SIAC Arbitration Rules 2025/2016 (Rules 3, 5, 7, 30); HKIAC
Administered Arbitration Rules 2018 (Articles 4, 5, 44); UNCITRAL Model Law on International
Commercial Arbitration (1985, with 2006 amendments); New York Convention on the Recognition and
Enforcement of Foreign Arbitral Awards 1958; IBA Guidelines on Conflicts of Interest in
International Arbitration (2014/2024); IBA Rules on the Taking of Evidence in International
Arbitration (2020); Eisemann pathological clause framework; jurisdiction-specific limitation
period and lex arbitri analysis for English, US, French, Singapore, Hong Kong, German, and
Swiss law; emergency arbitrator practice; provisional measures framework; arbitrator nomination
strategy; multi-party arbitration (Siemens/Dutco problem); third-party funding disclosure
obligations; Hadley v Baxendale damages framework; civil law damages (BGB, Code Civil); CISG
Articles 74-78; and best practices from Norton Rose Fulbright, Travers Smith, and international
arbitration scholarship. References should be verified against current institutional rules before
filing.
