---
name: legalcode-settlement-agreement-drafter
description: Draft and review settlement agreements covering mutual releases, payment terms and schedules,
  confidentiality and non-disparagement, representations and warranties, tax indemnification, enforcement
  mechanisms, court approval requirements, and dismissal stipulations. Handles employment (ADEA/OWBPA
  over-40 waiver, FLSA court approval, NLRA-compliant non-disparagement), commercial, and class action
  settlements. Supports both US and UK frameworks. Use when settling employment discrimination claims,
  wage-and-hour disputes, commercial contract disputes, personal injury claims, class actions, or any
  civil matter requiring a written settlement agreement, release of claims, or dismissal stipulation.
  Jurisdiction-agnostic core with [JURISDICTION-SPECIFIC] markers for US federal, US state, and UK practice.
  Integrates with legalcode-settlement-negotiation for pre-drafting BATNA/ZOPA analysis and legalcode-early-case-assessment
  for merits input.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Settlement Agreement Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted drafting and review of
> settlement agreements. It does not constitute legal advice. All outputs must be reviewed
> by a qualified legal professional licensed in the relevant jurisdiction before use or
> execution. Settlement agreements have complex tax, employment, and regulatory dimensions
> that vary significantly by jurisdiction and dispute type. Laws change; verify current
> applicability before relying on any provision described here. Statutory and case law
> references cited from memory carry hallucination risk — verify against authoritative
> sources before relying on them.

---

## Purpose and Scope

Use this skill to draft, review, or analyze settlement agreements for civil disputes. The
skill operationalizes the statutory and case law requirements governing settlement
enforceability across dispute types into a structured drafting workflow.

**Covers:**

- Full settlement agreement drafting (employment, commercial, personal injury, class action)
- ADEA/OWBPA-compliant waiver provisions (21-day / 45-day review, 7-day revocation)
- FLSA settlement approval pathway (Cheeks doctrine compliance)
- Rule 23(e) class action court approval requirements and fairness hearing preparation
- NLRA-compliant confidentiality and non-disparagement provisions (post-McLaren Macomb 2023)
- Mutual release drafting with California § 1542 carveout analysis
- Payment term structures including structured settlements and tax allocation
- UK settlement agreement requirements (s.203 ERA 1996, ACAS COT3 alternative)
- Enforcement mechanisms: confession of judgment, consent judgment, stipulated dismissal
- Rule 41 FRCP dismissal stipulations (with/without prejudice)
- Representations, warranties, and indemnification for settlement context
- Multi-party and multi-claim settlement structures
- Minor settlements and court approval requirements

**Does not:**

- Replace qualified legal counsel or binding legal advice
- Conduct merits analysis of the underlying claims (see `legalcode-early-case-assessment`)
- Calculate damages ranges or probability-weighted outcomes (see `legalcode-damages-calculation`)
- Build negotiation strategy or BATNA analysis (see `legalcode-settlement-negotiation`)
- Apply to criminal plea agreements, consent orders in regulatory proceedings, or
  sentencing (different frameworks apply)
- Provide tax advice; tax allocation analysis is indicative only and requires qualified
  tax counsel

---

## Jurisdiction and Governing Law

This is a **US/UK dual-framework skill** with jurisdiction-agnostic core provisions. The
governing law of the underlying dispute and the location of the parties determine which
framework applies.

| Framework          | Triggers                                                             | Key Authority                                                          |
| ------------------ | -------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **US Federal**     | Federal claims (ADEA, FLSA, Title VII, FLSA, ADA, § 1983, etc.)      | 29 U.S.C. § 626(f); Fed. R. Civ. P. 23, 41; 29 U.S.C. § 216            |
| **US State**       | State law employment, commercial, or tort claims                     | State-specific (identify governing law clause)                         |
| **UK**             | Employment claims, commercial disputes governed by English/Welsh law | ERA 1996 s.203; Employment Tribunals Act 1996; ACAS Code of Practice   |
| **Universal core** | Any civil settlement                                                 | Mutual release doctrine; contract formation; tax allocation principles |

[JURISDICTION-SPECIFIC] The following elements require jurisdiction-by-jurisdiction analysis:

- Review period and revocation rights (US: ADEA 21/45-day rule; UK: 10-day ACAS guidance)
- Mandatory independent legal advice requirement (UK s.203 only; US ADEA requires written
  notice to consult, not mandatory advice)
- Claim-specific language (NLRA § 8(a)(1) non-disparagement constraints; UK s.203 specific
  claims requirement)
- Tax treatment of each payment component (IRC § 104, § 3402; UK ITEPA 2003, HMRC guidance)
- Court approval requirements (FLSA: Cheeks doctrine; class action: Rule 23(e))
- Enforcement mechanisms (confessions of judgment: prohibited in several US states [VERIFY])

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points, marked with **⟁ CLARIFY**
below. Rather than assuming intent, the workflow pauses and asks when:

- The settlement type determines statutory compliance requirements (ADEA vs. commercial vs.
  class action — each has different mandatory provisions)
- Jurisdiction choices affect which court approval pathway applies
- Tax allocation decisions carry material financial consequences
- The user's role (drafter for plaintiff/claimant vs. defendant/respondent) changes the
  structure of releases and protections

If the user has already provided the information, skip the question and proceed. For
batch/automated runs, state your assumed defaults explicitly.

---

## Workflow

### Step 1: Intake — Characterize the Settlement

Accept the request in any format:

- **Summary of the dispute**: Parties, claim types, jurisdiction, settlement amount range
- **Existing draft**: A settlement agreement to review and improve
- **Term sheet or bullet points**: Key economic and non-economic terms
- **Prior pleadings or demand letters**: For context on claims being released

**⟁ CLARIFY** — Before drafting, ask the user these foundational questions. Present as
structured options:

1. **Settlement type** — Which best describes this dispute?
   - Employment (discrimination, harassment, retaliation, wrongful termination)
   - Employment (wage-and-hour / FLSA / state wage claims)
   - Employment (age discrimination — triggers ADEA/OWBPA requirements)
   - Commercial (contract dispute, business tort, IP, real estate)
   - Personal injury / tort (requires IRC § 104 physical injury analysis)
   - Class action or collective action
   - Mixed (multiple claim types — specify each)
   - _Why this matters_: Determines mandatory statutory requirements and court approval pathway.

2. **Jurisdiction** — Which framework applies?
   - US federal court (specify circuit)
   - US state court (specify state)
   - UK / England and Wales (specify tribunal or court)
   - Multiple jurisdictions (specify each)
   - _Why this matters_: Determines review period, independent advice requirements, and
     court approval obligations.

3. **Your client's role**
   - Plaintiff / Claimant (receiving payment, releasing claims)
   - Defendant / Respondent (making payment, being released)
   - Joint drafting (both sides involved)
   - _Why this matters_: The structure of releases, indemnification, and
     representations depends on which party you represent.

4. **Settlement consideration structure**
   - Lump sum cash payment
   - Structured / installment payments
   - Non-cash consideration only (reinstatement, reference letter, equity, etc.)
   - Mixed cash and non-cash
   - _Why this matters_: Drives payment terms, confession of judgment, and tax allocation.

5. **Claims being resolved** — List all claims being released:
   - Federal statutory claims (ADEA, Title VII, ADA, FLSA, § 1983, FMLA, etc.)
   - State statutory claims (specify)
   - Common law claims (breach of contract, fraud, defamation, etc.)
   - UK statutory claims (unfair dismissal, discrimination, whistleblowing, etc.)
   - _Why this matters_: Determines release scope, statutory waiver requirements, and
     whether any claims cannot be waived by private agreement.

### Step 2: Flag Mandatory Compliance Requirements

Before drafting any substantive provisions, identify all mandatory statutory requirements
that apply. These are non-negotiable — failure to meet them renders the settlement
unenforceable in whole or in part.

**Run this compliance screen silently and present results to the user:**

| Trigger                                     | Statutory Requirement                                                                                                                                                                                                                                           | Consequence of Non-Compliance                                                 |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Employee age 40+ AND ADEA claims released   | 29 U.S.C. § 626(f): 21-day review (individual) or 45-day review (group layoff/incentive program) + 7-day irrevocable revocation + plain language + written advice to consult attorney + specific ADEA reference + consideration exceeding existing entitlements | Waiver void and unenforceable                                                 |
| Group layoff (2+ employees, ADEA)           | 29 CFR § 1625.22(f): Attach decisional unit disclosure (job titles, individual ages of all decisional unit members — NOT age bands — selection criteria)                                                                                                        | Waiver void and unenforceable [VERIFY per circuit]                            |
| FLSA claims in litigation (Cheeks doctrine) | 2d Cir.: Cheeks v. Freeport Pancake House, 796 F.3d 199 (2d Cir. 2015): Court or DOL approval required                                                                                                                                                          | Settlement unenforceable without approval; other circuits may differ [VERIFY] |
| Class action settlement                     | Fed. R. Civ. P. 23(e): Court approval, fairness hearing, class notice, adequacy of representation finding                                                                                                                                                       | Settlement void without court approval                                        |
| UK employment statutory claims              | ERA 1996 s.203: Written, specific claims, independent legal advice from named adviser with professional indemnity insurance                                                                                                                                     | Waiver of statutory claims unenforceable                                      |
| Minor party (under 18)                      | Court approval required in all US jurisdictions [VERIFY threshold by state]; guardian ad litem typically required                                                                                                                                               | Settlement voidable; funds may require restricted account                     |
| EEOC charges                                | 42 U.S.C. § 2000e: Cannot waive right to file EEOC charge or participate in EEOC investigation                                                                                                                                                                  | Waiver of administrative charge filing rights void                            |
| Section 7 NLRA rights                       | 29 U.S.C. § 157; NLRB McLaren Macomb, 372 NLRB No. 58 (Feb. 21, 2023): Cannot waive future Section 7 rights; cannot include confidentiality/non-disparagement that chills concerted activity                                                                    | Provision void; potential ULP charge                                          |

**⟁ CLARIFY** — After running the compliance screen, if any mandatory requirement is triggered:

- Present the triggered requirement to the user
- Ask whether they have already satisfied it (e.g., "Has the employee already been given
  the 45-day consideration period? If not, the agreement cannot be executed until this
  period runs")
- Flag any requirements that cannot be waived by the parties

### Step 3: Gather Drafting Parameters

**⟁ CLARIFY** — Collect all parameters needed to produce accurate draft language. Skip
any that were already provided in Step 1.

**Party details:**

- Full legal names of all settling parties
- Party roles in the underlying dispute (plaintiff, defendant, employer, employee, etc.)
- Corporate status if any party is an entity (state of formation, authorized signatory)

**Economic terms:**

- Total settlement amount (gross)
- Payment allocation: back pay/wages, compensatory damages, emotional distress, attorney
  fees (each line item affects tax treatment)
- Payment method: wire transfer, check, direct deposit
- Payment timing: on execution, on court approval, by specific date
- Installment schedule if applicable
- Consequences of non-payment (liquidated damages, acceleration, confession of judgment)

**Non-economic terms:**

- Employment reference scope and language (neutral reference, title/dates only, etc.)
- Rehire eligibility (eligible, ineligible, or silent)
- Reinstatement (if applicable)
- Equity treatment (vesting, options, repurchase)
- Non-compete and non-solicitation (scope, duration, geography)
- Return of company property
- Any affirmative obligations post-execution

**Release structure:**

- Mutual release (both sides release each other) vs. unilateral release
- Known and unknown claims (California § 1542 waiver if CA law applies)
- Carveouts from the release (workers' compensation, vested retirement benefits,
  claims arising after execution, pending EEOC investigation participation rights)
- Time period for released claims (all claims arising before execution date)

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Read the governing law designation and use **legalcode-mcp** to gather relevant authority.

**Research process:**

1. **Identify the governing law** — pull from the underlying dispute's pleadings,
   the employment agreement or dispute resolution clause, or ask the user.

   **⟁ CLARIFY** — If no governing law is established:
   - For employment: default to the state where the employee principally worked
   - For commercial: default to the contract's stated governing law
   - For class action: typically the court's jurisdiction
   - Ask the user to confirm or correct before proceeding

2. **Search legalcode-mcp** for:
   - ADEA/OWBPA waiver validity requirements in the relevant circuit [VERIFY]
   - FLSA settlement approval requirements (Cheeks applicability in the relevant circuit) [VERIFY]
   - State-specific non-compete enforceability rules at the applicable governing law
   - State-specific confession of judgment enforceability [VERIFY — prohibited in CA, NY residential, others]
   - Applicable tax treatment for settlement payment components
   - UK-specific: ERA 1996 s.203 case law; ACAS COT3 guidance

3. **Save research findings** to `/tmp/legalcode-settlement-authority.md`.

**If legalcode-mcp is not connected:**

- Proceed with the analysis but mark all statutory and case law references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — all citations require verification"`
- Emphasize to the user that jurisdiction-specific compliance requirements must be
  independently verified by qualified counsel before execution

### Step 5: Draft the Settlement Agreement

Draft the complete settlement agreement using the **15-Provision Architecture** below.
For each provision, classify it as REQUIRED / RECOMMENDED / OPTIONAL / JURISDICTION-SPECIFIC
per the **Provision Classification System**.

Draft all provisions before presenting. Do not output a partial draft — the interaction
between provisions (e.g., the release scope must align with the dismissal stipulation)
requires the complete document to be internally consistent.

**⟁ CLARIFY** — For long or complex multi-party settlements:

- Ask whether the user wants a **full draft** of all applicable provisions or a
  **focused draft** of specific provisions (e.g., only the release and payment terms)
- For class action settlements, ask whether the user needs the **Settlement Agreement**,
  the **Notice to Class Members**, and the **Motion for Preliminary Approval** separately

### Step 6: Self-Review for Statutory Compliance

Before delivering the draft, run the statutory compliance verification silently:

1. **ADEA/OWBPA check** (if applicable): Confirm 21/45-day review language, 7-day
   revocation, plain-language waiver, specific ADEA reference, consideration adequacy,
   decisional unit disclosure (group layoff only)
2. **FLSA check** (if applicable): Confirm that the agreement contemplates court or
   DOL approval before becoming effective if claims arose in litigation
3. **NLRA check**: Confirm confidentiality and non-disparagement provisions are
   narrowly tailored to trade secrets and defamation-only respectively; confirm no
   waiver of future Section 7 rights
4. **UK s.203 check** (if applicable): Confirm written form, specific claims identified,
   independent adviser named with professional indemnity confirmation, statutory
   conditions statement
5. **Release scope check**: Confirm the release clause covers all claims in the
   compliance screen from Step 2; confirm carveouts are present for non-waivable rights
6. **Internal consistency check**: Payment amounts in recitals match payment clause;
   dismissal timing matches payment condition; release scope matches claim list

### Step 7: Quality Verification

Run the Citation Quality Gates, Self-Interrogation for CRITICAL provisions, and
Confidence Scoring per the **Quality Assurance Framework**. Append the Glass Box
Audit Trail.

### Step 8: Deliver Draft with Instruction Memo

Present the draft with:

- A brief cover memo flagging any provisions where the user must take an action before
  execution (e.g., run the 45-day clock, obtain court approval)
- A checklist of execution requirements (signing formalities, witnesses, notarization)
- Post-execution timeline (payment deadlines, filing deadlines, retention obligations)
- Filing and court submission instructions (if court approval required)

---

## 15-Provision Architecture

### Provision Classification System

| Classification            | Meaning                                                                    | Action if Absent                                                            |
| ------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **REQUIRED**              | Provision is legally mandatory or essential for enforceability             | Flag immediately; do not deliver draft without it                           |
| **RECOMMENDED**           | Provision is market standard and strongly advisable for protection         | Include unless user specifically opts out with awareness of risk            |
| **OPTIONAL**              | Provision is available but not universally used; depends on facts          | Include if applicable facts are present; discuss with user                  |
| **JURISDICTION-SPECIFIC** | Provision is mandatory or significantly different in certain jurisdictions | Flag with [JURISDICTION-SPECIFIC] and ask user to verify with local counsel |

### Provision 1: Caption, Parties, and Recitals

**Classification**: REQUIRED

**Purpose**: Identify all parties with precision, establish the context of the dispute,
and anchor the consideration for the release.

**Key elements:**

- Full legal names, addresses, and roles of all parties (and released parties/releasees)
- Corporate parties: state of incorporation, authorized signatory title
- Effective date (consider whether date of last signature or a specific future date)
- Recitals: brief statement of the underlying dispute, claims asserted, and that the
  parties desire to resolve the matter without admission of liability
- **No Admission of Liability** clause in recitals or immediately following:

  > _"Settlement constitutes compromise and settlement of disputed claims only. Nothing
  > herein constitutes or shall be construed as an admission of liability, fault, or
  > wrongdoing by any party. Each party expressly denies any and all liability."_

**Drafting notes:**

- Name all releasees explicitly (corporate affiliates, parents, subsidiaries, officers,
  directors, agents) — failure to name a party means they are not released
- If the employer is a corporate entity, name both the entity and the individual
  supervisors if they are separately named defendants
- Include party-defined terms at the outset (e.g., "Employee," "Company," "the Parties")

---

### Provision 2: Settlement Payment and Consideration

**Classification**: REQUIRED

**Purpose**: Define the exact amount, timing, method, and conditions for payment of
settlement consideration.

**Key elements:**

- Gross settlement amount in numerals and words
- Payment schedule: single payment or installment schedule with precise dates
- Payment method: wire transfer with routing/account number, corporate check, or other
- Conditions precedent to payment: execution by all parties, court approval (FLSA/class
  action), expiration of ADEA revocation period, delivery of signed W-9 or equivalent
- Withholding: specify whether any amount is subject to income tax withholding and FICA
  (see Provision 9 for tax allocation)
- Non-payment consequences (see Provision 14)

**⟁ CLARIFY** — If installment payments are contemplated:

- Is there to be a confession of judgment held in escrow? (Powerful enforcement tool
  but prohibited in several US states — California, New York for residential debts —
  and void in others [VERIFY per state])
- What are the cure rights for late payment (e.g., 10-day cure before acceleration)?
- Does the full unpaid balance accelerate on default?

**Market practice:**

- Employment: Payment typically due within 5–10 business days of the later of execution
  or expiration of the ADEA revocation period (if applicable)
- FLSA: Payment due within 5–10 business days of court approval
- Class action: Distribution plan following court approval; class administrator typically
  handles disbursement
- Commercial: Conditions and timing negotiated; interest on late payment recommended

---

### Provision 3: ADEA/OWBPA Waiver (Age Discrimination)

**Classification**: JURISDICTION-SPECIFIC — REQUIRED when employee is age 40+ and any
ADEA claim is being released

**Statutory basis**: 29 U.S.C. § 626(f); 29 CFR § 1625.22 [VERIFY]

**Mandatory elements (all must be present; omission voids the waiver):**

1. **Plain language acknowledgment**:

   > _"This Agreement is written in plain language that [Employee] understands."_

2. **Specific ADEA reference** — Must name the statute:

   > _"[Employee] knowingly and voluntarily waives and releases any rights or claims
   > under the Age Discrimination in Employment Act of 1967, as amended, 29 U.S.C.
   > § 621 et seq. ('ADEA')."_

3. **Not waiving future claims**:

   > _"This waiver does not extend to rights or claims that may arise after the date
   > this Agreement is executed."_

4. **Additional consideration**:

   > _"In exchange for this waiver, [Employee] is receiving consideration in addition to
   > anything of value to which [Employee] is already entitled."_

5. **Written advice to consult attorney**:

   > _"[Employee] is advised in writing to consult with an attorney prior to executing
   > this Agreement."_

6. **Individual separation — 21-day review period**:

   > _"[Employee] acknowledges having been given a period of at least twenty-one (21)
   > calendar days within which to consider this Agreement before signing. [Employee]
   > may sign before the 21-day period expires but does so voluntarily."_

   **OR for group layoff/incentive program — 45-day review period:**

   > _"[Employee] acknowledges having been given a period of at least forty-five (45)
   > calendar days within which to consider this Agreement before signing. Attached as
   > Exhibit [A] is the required disclosure of the job titles and ages of all employees
   > in the decisional unit and the selection criteria used."_

7. **Seven-day revocation right (mandatory; cannot be shortened)**:
   > _"[Employee] may revoke this Agreement within seven (7) calendar days after
   > signing by delivering written notice of revocation to [Company contact/address]
   > before the close of the seventh day. This Agreement shall not become effective
   > or enforceable until the revocation period has expired without revocation. If
   > revoked, this Agreement shall be null and void and Company shall have no payment
   > obligation hereunder."_

**Decisional Unit Disclosure (group layoff only — 29 CFR § 1625.22(f)(1)(iii)(B)):**

Attach as Exhibit A a table with:

- Job titles of all employees in the decisional unit (all who were considered for the
  program — not just those selected)
- Individual ages (not age bands) of all such employees
- Selection criteria applied

> _DRAFTING WARNING: Providing only age ranges (e.g., "40–49") rather than individual
> ages invalidates the group-layoff waiver under EEOC guidance [VERIFY]. Provide
> individual ages or the waiver will not satisfy OWBPA._

**Non-waivable EEOC rights:**

> _"Nothing in this Agreement prevents [Employee] from filing a charge with or
> participating in an investigation by the Equal Employment Opportunity Commission
> ('EEOC') or any state or local fair employment agency. However, [Employee] waives
> the right to recover any monetary relief in connection with any such charge or
> proceeding."_

---

### Provision 4: General Release of Claims

**Classification**: REQUIRED

**Purpose**: Effect the full and final settlement of all claims between the parties.

**⟁ CLARIFY** — Before drafting the release:

- **Unilateral vs. mutual**: Does the defendant/company also release the employee/plaintiff,
  or is this a one-directional release?
  - _Why this matters_: Courts may imply a mutual release even if parties intended
    one-directional; express the direction to avoid ambiguity
- **Known and unknown claims** (California § 1542 applicability):
  - If California law governs or a California employee is involved, a release of unknown
    claims must include an express § 1542 waiver (see below)

**Core release language:**

> \_"In consideration of the payments and other obligations set forth in this Agreement,
> and subject to the exclusions in Section [X], [Releasor] hereby releases, acquits, and
> forever discharges [Releasees, including their predecessors, successors, assigns,
>
> > parents, subsidiaries, affiliates, officers, directors, members, managers, employees,
> > agents, and attorneys] ('Released Parties') from any and all claims, charges, demands,
> > actions, causes of action, suits, debts, liabilities, damages, costs, expenses,
> > attorneys' fees, and obligations of any kind, whether known or unknown, suspected or
> > unsuspected, fixed or contingent, in law or equity, which [Releasor] now has, ever had,
> > or may have had against any Released Party, arising from or related to [Releasor's]
> > employment with Company / the subject matter of the Action, up to and including the
> > date of this Agreement."\_

**California Civil Code § 1542 waiver (REQUIRED if California law applies or
California employee is party):**

> _"[Releasor] expressly waives and relinquishes all rights and benefits afforded by
> California Civil Code § 1542, which states: 'A general release does not extend to
> claims that the creditor or releasing party does not know or suspect to exist in his
> or her favor at the time of executing the release and that, if known by him or her,
> would have materially affected his or her settlement with the debtor or released party.'
> [Releasor] acknowledges that it understands the significance of this waiver."_
> [JURISDICTION-SPECIFIC]

**Required carveouts from the release (REQUIRED):**

- Claims arising after the date of execution
- Vested pension/retirement benefits
- Workers' compensation rights (state law typically prohibits waiver [VERIFY])
- Unemployment compensation rights (where non-waivable [VERIFY by state])
- Right to file an administrative charge (EEOC, NLRB, NLRB) — may waive monetary recovery
- Pending workers' compensation claims (separately addressed)
- Any claims explicitly listed as not being released
- Indemnification rights under company D&O or applicable law (for employee-releasors
  who are also officers/directors)

**Mutual release language (add when both sides release):**

> _"In consideration of [Employee's] releases and covenants herein, Company hereby
> releases [Employee] from any and all claims... [mirror language]."_

---

### Provision 5: Confidentiality

**Classification**: RECOMMENDED — but subject to NLRA constraints for employment settlements

**⟁ CLARIFY** — For employment settlements:

- **NLRB McLaren Macomb impact**: Broad confidentiality clauses prohibiting disclosure of
  the settlement's "existence, terms, or conditions" or all information about employment
  violate NLRA § 8(a)(1) for employees exercising Section 7 rights. Present the user with:
  - Option A: **Trade-secret-only confidentiality** (NLRA-compliant) — restrict disclosure
    of proprietary or trade secret information only, with legitimate business justification
  - Option B: **No confidentiality provision** — avoid the NLRA risk entirely
  - Option C: **Limited settlement amount confidentiality** — some employers request
    confidentiality of the monetary amount only; enforceability under McLaren Macomb
    is uncertain [VERIFY — NLRB GC Memo 23-05 issued March 2023]

**NLRA-compliant confidentiality draft:**

> _"The Parties agree to maintain the confidentiality of [Company's] proprietary
> business information, trade secrets, and confidential customer and business data that
> [Employee] obtained during employment, consistent with [Employee's] obligations under
> the Confidentiality Agreement dated [date] and applicable law. Nothing in this
> provision restricts [Employee's] right to discuss wages, hours, working conditions,
> or terms of employment with co-workers or others, to file charges with or cooperate
> with any government agency, or to exercise rights protected by the NLRA or any other
> applicable law."_

**Commercial settlement confidentiality draft:**

> _"The Parties agree to keep the existence of this Agreement and the terms hereof
> strictly confidential and shall not disclose such information to any person or entity
> without the prior written consent of the other Party, except: (a) to each Party's
> legal counsel, accountants, financial advisors, or tax advisers under obligations of
> confidentiality; (b) to members of each Party's immediate family (if an individual);
> (c) as required by applicable law, court order, or regulatory requirement; or (d) as
> reasonably necessary to enforce this Agreement."_

[JURISDICTION-SPECIFIC] **UK note**: Post-#MeToo reforms increased scrutiny of
non-disclosure agreements in harassment and discrimination settlements. UK NDAs cannot
prevent a victim from reporting to the police, a regulated professional, or prescribed
person under PIDA 1998. Solicitors' conduct rules (SRA Code of Conduct 2019) prohibit
using NDAs to impede legitimate reporting. [VERIFY current guidance]

---

### Provision 6: Non-Disparagement

**Classification**: OPTIONAL — frequently requested; must be NLRA-compliant for employment

**NLRA constraints post-McLaren Macomb:**

- Prohibition on any truthful statements about employment violates Section 7
- Only **defamation-only** non-disparagement is permissible: prohibiting statements that
  are provably false and made with knowledge of falsity or reckless disregard for truth/falsity

**NLRA-compliant non-disparagement draft (employment):**

> _"Each Party agrees not to make defamatory statements about the other Party or, in
> the case of Company, about Company's officers, directors, or employees. For purposes
> of this provision, 'defamatory' means statements that are (a) false, (b) made with
> knowledge of their falsity or with reckless disregard for their truth or falsity, and
> (c) harmful to the reputation of the subject. Nothing in this provision restricts
> [Employee's] right to make truthful statements about workplace experiences, conditions
> of employment, or alleged unlawful conduct, or to exercise rights protected under the
> National Labor Relations Act or any other applicable law."_

**Broader commercial non-disparagement draft (non-employment context):**

> _"Each Party agrees not to make any public or private statements, in writing or
> orally, that disparage or negatively characterize the other Party, its products,
> services, business practices, or personnel. This restriction does not apply to
> truthful statements made in legal proceedings or to government agencies, or to
> statements required by applicable law."_

---

### Provision 7: Restrictive Covenants (Non-Compete and Non-Solicitation)

**Classification**: OPTIONAL — include only when expressly requested and where enforceable

**⟁ CLARIFY** — Restrictive covenants in settlement agreements require careful
jurisdiction-specific analysis:

- **California**: Non-competes and non-solicits preventing work in chosen profession are
  per se void under Cal. Bus. & Prof. Code § 16600, as amended by AB 1076 (SB 699 effective
  Jan 1, 2024) [VERIFY current status]
- **FTC Non-Compete Rule**: The FTC's final rule (Aug 2024) was vacated by Ryan LLC v.
  FTC (N.D. Tex. Aug 20, 2024); the non-compete legal landscape is in flux [VERIFY]
- **General test**: Enforceable only if (i) necessary to protect legitimate business
  interests (trade secrets, customer relationships), (ii) limited in duration and
  geography, (iii) not unduly burdensome, and (iv) not against public policy

**Settlement-context non-compete draft:**

> \_"In consideration of the settlement consideration provided herein, [Employee/Counterparty]
> agrees not to directly or indirectly engage in [defined competitive activity] within
> [defined geographic area] for a period of [duration] from the date of this Agreement.
> This restriction applies only to activities substantially competitive with [specific
>
> > business lines]. Nothing herein prevents [Employee] from working in [Employee's]
> > professional field in a non-competitive capacity."\_

**⚠ Drafting warning**: Overly broad restrictive covenants may render the entire
settlement agreement subject to challenge. Narrowly tailor to the specific legitimate
interest being protected.

---

### Provision 8: Representations and Warranties

**Classification**: REQUIRED

**Purpose**: Ensure each party has the authority and capacity to enter the agreement,
has read and understands it, and has not relied on extraneous representations.

**Standard representations:**

> _"Each Party represents and warrants that: (a) it has the full right, power, and
> authority to enter into this Agreement and perform its obligations hereunder; (b) this
> Agreement has been duly authorized and constitutes a legal, valid, and binding obligation
> enforceable against each Party; (c) no consent or approval not already obtained is
> required for the execution or performance of this Agreement; (d) the Party has read
> and fully understands this Agreement; (e) the Party has had the opportunity to consult
> with legal counsel of its choosing; (f) the Party is not acting under duress or undue
> influence; (g) the Party has not relied on any representation, promise, or inducement
> not expressly set forth herein; and (h) the Party has not assigned, pledged, or
> transferred any of the claims released herein to any third party."_

**Employee-specific additional warranty:**

> _"[Employee] further warrants that there are no pending or threatened claims, lawsuits,
> or arbitration proceedings arising from [Employee's] employment with Company other than
> those expressly identified herein, and that [Employee] has not filed any complaints or
> charges arising from employment with Company that are not referenced herein, except
> for any pending EEOC charge which [Employee] agrees to withdraw upon receipt of
> settlement payment."_

**No-assignment warranty (CRITICAL — prevents third-party enforcement problems):**

> _"[Releasor] represents and warrants that [Releasor] has not assigned, pledged, or
> otherwise transferred any interest in any claim released herein to any third party,
> and that [Releasor] has the full authority to grant the releases set forth in this
> Agreement."_

---

### Provision 9: Tax Indemnification and Payment Allocation

**Classification**: REQUIRED — omission creates tax and indemnification gaps

**⚠ Disclaimer**: Tax treatment of settlement payments is complex and depends on the
specific facts of each case and applicable law. The allocation guidance below is
indicative only. Users must obtain qualified tax advice before finalizing allocations.

**General tax characterization principles (US):**
| Payment Component | Tax Treatment | Withholding |
|------------------|---------------|-------------|
| Back pay / lost wages | Ordinary income; subject to income tax and FICA | W-2; employer withholds |
| Compensatory damages for personal physical injury (IRC § 104(a)(2)) | Excludable from gross income | No withholding if properly documented |
| Emotional distress damages (not arising from physical injury) | Taxable ordinary income | Form 1099-MISC (box 3) |
| Punitive damages | Always taxable regardless of claim type | Form 1099-MISC |
| Attorney fees (contingency fee cases) | Taxable to plaintiff under Banks; deduction may be available | Form 1099-MISC |
| ADEA/Title VII/ADA damages (non-physical) | Taxable ordinary income | Form 1099-MISC |
| Payment in lieu of notice (UK/PILON) | Taxable income in the UK under ITEPA 2003 regardless of contractual basis [VERIFY current HMRC guidance] | PAYE |
| UK compensatory/general damages | First £30,000 of termination payments may be exempt under ITEPA 2003 s.403 [VERIFY] | |

**Allocation clause draft:**

> \_"The Parties agree to allocate the Settlement Amount as follows for tax reporting
> purposes: (a) $[X] as wages/back pay, subject to applicable withholding and reported
> on a Form W-2; (b) $[Y] as compensatory damages for [emotional distress / personal
>
> > injury / other non-wage harm], reported on Form 1099-MISC; (c) $[Z] as attorney fees
> > payable directly to Plaintiff's counsel, reported on Form 1099-NEC. The Parties shall
> > file all applicable tax returns and reports consistently with this allocation. [Employee]
> > shall be responsible for [Employee's] own tax obligations on amounts received under
> > this Agreement and shall indemnify and hold Company harmless from any taxes, penalties,
> > or interest assessed against Company arising from [Employee's] failure to pay taxes
> > on amounts allocated as non-wage consideration."\_

**Tax indemnification (mutual; recommended):**

> _"Each Party shall be solely responsible for any taxes, interest, or penalties
> assessed on consideration received by such Party under this Agreement. Each Party
> shall indemnify and hold the other harmless from any tax liability, penalty, or
> interest assessed against the indemnified Party arising from the indemnifying Party's
> failure to pay applicable taxes on amounts received."_

[JURISDICTION-SPECIFIC] **UK note**: HMRC requires consistent tax reporting between
parties to a settlement. Seek agreement on allocation before execution. Employer
National Insurance contributions implications must also be considered.

---

### Provision 10: Court Approval Provisions

**Classification**: JURISDICTION-SPECIFIC — REQUIRED for FLSA and class action settlements

#### 10a. FLSA Court Approval (Cheeks Doctrine)

**Applicable when**: FLSA wage-and-hour claims being settled in litigation

**Statutory basis**: 29 U.S.C. § 216(b); Cheeks v. Freeport Pancake House, 796 F.3d 199
(2d Cir. 2015) [VERIFY applicability in your circuit — circuits may differ]

> _"The Parties acknowledge that this Agreement is conditioned upon approval by the
> [Court name and docket] as a fair and reasonable resolution of a bona fide dispute
> under the FLSA, pursuant to Cheeks v. Freeport Pancake House. The Parties agree to
> file a joint motion for approval promptly following execution of this Agreement. This
> Agreement shall not become effective, and Company shall have no obligation to make any
> payment hereunder, until the Court enters an order approving this Agreement."_

> \_"The Parties agree that the Settlement Amount represents a reasonable compromise of
> a bona fide dispute over FLSA liability including [disputed hours / overtime
>
> > calculation / tip credit / exemption classification]. The Parties will submit to the
> > Court a joint motion demonstrating: (a) the nature of the bona fide dispute; (b) the
> > reasonableness of the settlement amount; and (c) the reasonableness of any attorney
> > fee allocation."\_

**⚠ Note on prelitigation FLSA settlements**: Courts and commentators distinguish
pre-litigation FLSA settlements, which may not require court approval under Cheeks.
[VERIFY per circuit and specific facts.]

#### 10b. Class Action Fairness Hearing (Rule 23(e))

**Applicable when**: Settlement of a certified or uncertified class action or collective
action

**Statutory basis**: Fed. R. Civ. P. 23(e)

> _"This Agreement is contingent upon entry by the [Court] of a Final Approval Order
> following a fairness hearing pursuant to Federal Rule of Civil Procedure 23(e). The
> Agreement shall not be effective and no settlement funds shall be distributed until
> the Court has: (a) issued a Preliminary Approval Order; (b) caused adequate notice to
> be provided to the Class; (c) conducted a fairness hearing; and (d) issued a Final
> Approval Order finding this settlement to be fair, reasonable, and adequate under Rule
> 23(e)(2). If the Court denies final approval or if an appeal of a final approval order
> results in the settlement not receiving final approval, this Agreement shall be null
> and void and neither Party shall have any obligation to the other hereunder."_

**Class member opt-out and objection rights:**

> _"Class Members shall have the right to opt out of or object to this Agreement as
> provided in the Class Notice approved by the Court. No payment to an objector or
> their counsel connected to withdrawal of an objection shall be made without Court
> approval pursuant to Rule 23(e)(5)."_

---

### Provision 11: Dismissal Stipulations

**Classification**: REQUIRED (for litigated settlements); RECOMMENDED (for pre-litigation settlements with pending filings)

**Statutory basis**: Fed. R. Civ. P. 41; comparable UK CPR provisions [JURISDICTION-SPECIFIC]

**⟁ CLARIFY** — Specify the dismissal effect:

- **With prejudice** (RECOMMENDED for finality): Bars re-filing of the same claims; the
  normal choice for a final settlement
- **Without prejudice**: Default under Rule 41 absent explicit language; allows re-filing
  (almost never appropriate for a final settlement)

**Standard stipulation of dismissal with prejudice:**

> _"Plaintiff agrees to file or cause to be filed a Stipulation of Dismissal With
> Prejudice as to all claims against Defendant in [Action name and docket number]
> within [5] business days of the later of: (a) receipt of the Settlement Payment, or
> (b) expiration of the ADEA revocation period (if applicable). The Parties shall bear
> their own costs and attorneys' fees except as otherwise provided in this Agreement."_

**Condition on court approval (FLSA/class action):**

> _"Following entry of the Court's Final Approval Order [or FLSA approval order],
> Plaintiff's counsel shall file a Stipulation of Dismissal With Prejudice within [5]
> business days."_

**Administrative proceedings dismissal:**

> _"Concurrent with or immediately following execution of this Agreement, [Employee]
> shall withdraw or move to dismiss with prejudice any pending administrative
> complaints, charges, or proceedings before [EEOC / NLRB / applicable agency] arising
> from or related to [Employee's] employment, except that [Employee] retains the right
> to participate in any EEOC investigation or proceeding in which [Employee] did not
> initiate the charge."_

[JURISDICTION-SPECIFIC] **UK note**: Employment Tribunal proceedings are withdrawn via
a COT3 (ACAS conciliation) or by consent order. Ensure the Tribunal claim number and
applicable ET claim form reference are stated. Withdrawal must be filed with the
Tribunal; parties cannot privately settle a pending ET claim without notifying the
Tribunal. [VERIFY current ET procedural requirements]

---

### Provision 12: Enforcement Mechanisms

**Classification**: OPTIONAL — but strongly recommended when installment payments are used

**⟁ CLARIFY** — Which enforcement mechanism does the user prefer?

- **Confession of Judgment** (fastest enforcement on default; prohibited in some states —
  see below)
- **Consent Judgment** (court enters judgment; enforceable by contempt; requires filing
  with court)
- **Acceleration + Interest** (simpler; balance due immediately on default plus interest)
- **Combined** (confession of judgment held in escrow as backstop to installment schedule)

**Confession of Judgment (where permitted):**

> _"In the event of [Employee's / Counterparty's] breach of the payment obligations
> herein, and upon expiration of the [10]-day cure period without cure, Company /
> [Creditor] shall have the right to enter judgment against [Debtor] by confession
> in the amount of the outstanding unpaid balance, plus interest at the rate of [X%]
> per annum from the date of default. [Debtor] hereby irrevocably appoints [Creditor]
> or its counsel as [Debtor's] attorney-in-fact for the purpose of confessing judgment
> in any court of competent jurisdiction. This authorization shall survive any revocation
> or attempted revocation by [Debtor]."_

> _[JURISDICTION-SPECIFIC] DRAFTING WARNING: Confessions of judgment are prohibited or
> significantly restricted in several US states: California (Code Civ. Proc. § 1132;
> void if entered against consumers), New York (CPLR § 3218 — only on default; consumer
> restrictions apply), and other states. Verify enforceability in the applicable
> jurisdiction before including. [VERIFY]_

**Consent Judgment (court-approved enforcement):**

> _"Contemporaneously with execution of this Agreement, [Debtor] shall execute a
> Consent Judgment in the form attached hereto as Exhibit [B]. [Creditor] agrees to
> hold the Consent Judgment and not file it with any court unless and until [Debtor]
> fails to make a payment when due and fails to cure such default within [10] business
> days of written notice. Upon a non-cured default, [Creditor] may file the Consent
> Judgment and seek enforcement thereof."_

**Acceleration clause:**

> _"In the event [Debtor] fails to make any installment payment when due, and such
> failure continues for [10] business days after written notice, the entire unpaid
> balance of the Settlement Amount shall become immediately due and payable, together
> with interest at the rate of [X%] per annum from the date of the original default."_

---

### Provision 13: UK-Specific Requirements (s.203 ERA 1996)

**Classification**: JURISDICTION-SPECIFIC — REQUIRED for UK employment statutory claims

**Statutory basis**: Employment Rights Act 1996 s.203; Employment Tribunals Act 1996;
ACAS Code of Practice on Settlement Agreements (4th ed.) [VERIFY current edition]

**Mandatory elements for s.203 validity (all must be present):**

1. **Written form**: Agreement must be in writing.

2. **Specific claims identification** (s.203(3)(b)) — must name each statutory claim:

   > \_"This Agreement relates to and settles the following particular complaints: (a)
   > [Employee's] complaint of unfair dismissal under the Employment Rights Act 1996;
   > (b) [Employee's] complaint of [direct race discrimination / sex discrimination /
   >
   > > disability discrimination] under the Equality Act 2010; (c) [list each claim
   > >
   > > > > individually by statutory reference]."\_

   > **⚠ Drafting warning**: A blanket waiver of "all statutory employment claims" is
   > insufficient — each claim must be specifically identified. [VERIFY current case law]

3. **Named independent adviser** — must be identified with specifics:

   > \_"[Employee] has received advice from [Name of Adviser], a [qualified solicitor /
   >
   > > certified trade union official / advice centre worker with written authorisation]
   > > ('Independent Adviser'), regarding the terms and effect of this Agreement, in
   > > particular its effect on [Employee's] ability to pursue the Particular Complaints
   > > before an Employment Tribunal."\_

4. **Professional indemnity insurance confirmation**:

   > _"At the time the Independent Adviser gave the advice, there was in force a contract
   > of insurance, or an indemnity provided for members of a profession or professional
   > body, covering the risk of a claim by [Employee] in respect of loss arising in
   > consequence of that advice."_

5. **Statutory conditions statement**:

   > _"The conditions regulating settlement agreements under section 203 of the
   > Employment Rights Act 1996 and section 49 of the National Minimum Wage Act 1998
   > and section 288(2B) of the Trade Union and Labour Relations (Consolidation) Act
   > 1992 [and any other applicable statutory provision] are satisfied."_

6. **10-day consideration period** (ACAS guidance; not statutory minimum but strongly
   recommended to establish voluntariness and good faith):
   > _"Company acknowledges that [Employee] has been given a minimum of 10 calendar
   > days to consider the terms of this Agreement and to obtain independent legal advice
   > before signing."_

**ACAS COT3 as alternative to s.203:**
Where claims are settled through ACAS conciliation, the resulting COT3 agreement does not
require independent legal advice but should still identify claims settled by ACAS claim
reference. COT3 agreements are broader in potential scope than s.203 agreements and can
settle claims outside the Employment Tribunal remit within the ACAS mandate. [VERIFY
with ACAS]

---

### Provision 14: Miscellaneous / Boilerplate

**Classification**: REQUIRED (integration, governing law, severability); RECOMMENDED (others)

**14a. Integration / Entire Agreement Clause (REQUIRED):**

> _"This Agreement constitutes the entire agreement between the Parties with respect to
> its subject matter and supersedes all prior negotiations, discussions, representations,
> warranties, undertakings, or agreements, whether oral or written, between the Parties
> relating to such subject matter."_

**14b. Disclaimer of Reliance (RECOMMENDED — prevents fraud claims where merger clause alone is insufficient):**

> _"Each Party acknowledges and agrees that it has not relied on any representation,
> promise, inducement, or statement of intention by any other Party or their counsel that
> is not expressly set forth in this Agreement and that no such representation, promise,
> inducement, or statement has been made."_

> [PRACTICE NOTE: An integration clause alone does not prevent a fraud claim based on
>
> > pre-contractual representations. The disclaimer of reliance is required to prevent later
> > fraudulent inducement claims. Include both.]

**14c. Governing Law and Forum (REQUIRED):**

> _"This Agreement shall be governed by and construed in accordance with the laws of
> [State / jurisdiction], without regard to conflicts of law provisions. Any dispute
> arising out of or relating to this Agreement shall be brought exclusively in the
> [courts / arbitration forum] of [jurisdiction]."_

**14d. Severability (REQUIRED):**

> _"If any provision of this Agreement is held to be invalid, unenforceable, or
> contrary to applicable law, such provision shall be modified to the minimum extent
> necessary to make it enforceable, or if not susceptible to modification, shall be
> severed, and the remaining provisions shall continue in full force and effect. The
> invalidity of any provision of this Agreement shall not affect the enforceability of
> the releases or the payment obligations."_

**14e. No Waiver:**

> _"No waiver of any breach of this Agreement shall be construed as a continuing waiver
> or a waiver of any other breach of this Agreement."_

**14f. Amendment:**

> _"This Agreement may be amended only by a written instrument signed by all Parties."_

**14g. Counterparts:**

> _"This Agreement may be executed in counterparts, each of which shall be an original
> and all of which together shall constitute one instrument. Electronic signatures
> (including PDF or DocuSign) shall be deemed original signatures."_

**14h. Notices:**

> _"All notices required or permitted under this Agreement shall be in writing and
> delivered by hand, overnight courier, certified mail (return receipt requested), or
> email with delivery confirmation to the addresses and email addresses set forth below
> or such other addresses as a Party may designate in writing."_

**14i. Headings:** Headings are for convenience only and do not affect interpretation.

**14j. Construction / No Drafter Presumption:**

> _"This Agreement shall not be construed more strictly against one Party than the other
> by reason of either Party having drafted the Agreement or any portion thereof."_

---

### Provision 15: Signatures and Execution

**Classification**: REQUIRED

**Elements:**

- Signature lines for all parties (individual and authorized corporate signatory)
- Printed name and title for corporate signatories
- Date of execution (each party signs separately; use the later date for "effective date")
- Witness or notary (OPTIONAL in most US commercial/employment settlements; may be
  required for real property releases or in certain states [VERIFY])
- Independent adviser's countersignature (UK s.203 REQUIRED)

**UK independent adviser countersignature block:**

> _"I confirm that I have given independent legal advice to [Employee] about the terms
> and effect of this Agreement and, in particular, its effect on [Employee's] ability
> to pursue the claims set out in [clause X] before an Employment Tribunal._
>
> _Name of Adviser: \***\*\*\*\*\***\_\_\***\*\*\*\*\***_
> _Firm / Organisation: **\*\*\*\***\_\_\_**\*\*\*\***_
> _Address: **\*\***\*\***\*\***\_\_\_\_**\*\***\*\***\*\***_
> _Professional qualification: **\*\***\_**\*\***_
> _Signature: **\*\***\*\***\*\***\_**\*\***\*\***\*\***_
> _Date: **\*\***\*\*\*\***\*\***\_\_**\*\***\*\*\*\***\*\***"_

---

## Severity / Status Classification System

### Classification Tiers for Settlement Agreement Provisions

| Status                    | Meaning                                                                                                           | Action                                                                                |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **REQUIRED**              | Legally mandatory or essential for enforceability (e.g., ADEA review period, s.203 conditions, Rule 41 dismissal) | Cannot deliver draft without this provision; flag immediately                         |
| **RECOMMENDED**           | Market standard; provides essential protection; should be included absent specific reason to omit                 | Include by default; flag if user requests omission                                    |
| **OPTIONAL**              | Available but depends on specific facts or mutual agreement (e.g., non-compete, confession of judgment)           | Include when applicable; confirm with user                                            |
| **JURISDICTION-SPECIFIC** | Mandatory or significantly different in certain jurisdictions; requires local counsel verification                | Flag with [JURISDICTION-SPECIFIC] and [VERIFY]; do not assert universal applicability |
| **PROHIBITED / CAUTION**  | Provision is invalid, unenforceable, or creates regulatory risk in the stated jurisdiction                        | Flag prominently; propose compliant alternative                                       |

---

## Prioritization Framework

### Tier 1 — Enforceability Anchors (Non-Negotiable)

Issues where omission makes the settlement void or voidable:

- ADEA/OWBPA: Missing 21/45-day review, 7-day revocation, or decisional unit disclosure
- UK s.203: Missing written form, specific claims, or independent adviser provisions
- FLSA: Missing court/DOL approval mechanism for litigated FLSA claims
- Class action: Missing Rule 23(e) conditional effectiveness clause
- Release: No-assignment warranty absent (creates third-party enforcement risk)
- Consideration: Settlement amount not specified or consideration is pre-existing entitlement only (ADEA additional consideration requirement)

### Tier 2 — Protection Priorities (Should-Haves)

Issues that materially affect protection but have negotiating room:

- Tax allocation and indemnification
- Disclaimer of reliance (beyond merger clause alone)
- Carveouts from release (vested benefits, EEOC charge rights)
- Enforcement mechanism for installment payments
- Integration clause and governing law
- UK: 10-day consideration period; employer legal fee contribution
- NLRA-compliant confidentiality/non-disparagement scope

### Tier 3 — Enhancements (Concession Candidates)

Issues that improve position but can be adjusted:

- Specific neutral reference language
- Rehire eligibility carve-in or exclusion
- Restrictive covenant duration and scope
- Specific notice provisions
- Minor boilerplate variations
- Administrative proceedings withdrawal timing

**Strategy**: Deliver Tier 1 elements as non-negotiable. Negotiate Tier 2 within ranges.
Treat Tier 3 as concession inventory for the negotiation.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                   | Fail Action                                                  |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Source**     | Every statutory claim cites a specific statute, section, and enacted date                                                              | Add citation or mark "[UNVERIFIED — counsel to confirm]"     |
| **Format**     | All US citations use standard legal format (29 U.S.C. § X; Fed. R. Civ. P. X; X F.3d X); UK citations use standard Law Report format   | Fix format                                                   |
| **Currency**   | Every cited statute checked for subsequent amendment, repeal, or judicial narrowing                                                    | Flag "[CHECK CURRENCY — may have been amended or overruled]" |
| **Domain**     | Analysis stays within the identified governing law. No US ADEA analysis in a pure UK matter; no s.203 requirements stated as universal | Remove or flag with [JURISDICTION-SPECIFIC]                  |
| **Confidence** | Uncertainty explicitly stated; no "the settlement will be unenforceable" without citing authority                                      | Add confidence qualifier or flag [VERIFY]                    |

### Self-Interrogation for REQUIRED Provisions

For any provision classified REQUIRED and any statutory compliance checkpoint, apply this
3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the drafted language actually satisfy the statutory requirement cited?
- Would a court reviewing this agreement for ADEA/OWBPA compliance, FLSA approval, or
  s.203 compliance find all mandatory elements present?
- Is there a ground on which the opposing party or a reviewing court might challenge the
  provision?

**Pass 2 — Completeness**:

- Have all statutes and regulations relevant to the settlement type been considered?
- Are there state law requirements (non-compete, confession of judgment, minor settlements)
  that have not been addressed?
- Have all carveouts from the release been included?

**Pass 3 — Challenge**:

- What is the strongest argument that a required provision is missing or deficient?
- Could the employee/claimant void the release by challenging this provision?
- Are there any recent statutory amendments or cases that affect the stated requirements?

Mark audit trail: `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                                                                | Action                                                                    |
| ------------ | --------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled statute; black-letter requirement (ADEA 7-day revocation; Rule 23(e) approval) | State with confidence                                                     |
| **High**     | 0.80-0.94 | Strong authority; minor circuit or jurisdiction questions                              | State with brief caveat                                                   |
| **Probable** | 0.60-0.79 | Good authority but circuit or state splits exist                                       | State with reasoning and contra-indicators; flag [VERIFY in your circuit] |
| **Possible** | 0.40-0.59 | Genuinely uncertain; evolving law (McLaren Macomb scope; Cheeks circuit split)         | Flag for counsel review with both sides                                   |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative                                                                | Do not assert; mark "[UNCERTAIN — counsel to advise]"                     |

---

## Glass Box Audit Trail

Every settlement agreement draft MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-settlement-agreement-drafter"
  settlement_type: "[Employment-ADEA / Employment-FLSA / Commercial / Class Action / Personal Injury / Mixed]"
  governing_law: "[Jurisdiction / 'Jurisdiction-agnostic']"
  frameworks_applied:
    - "[ADEA/OWBPA 29 U.S.C. § 626(f) — Applied / Not applicable]"
    - "[FLSA Cheeks doctrine — Applied / Not applicable]"
    - "[Rule 23(e) class action approval — Applied / Not applicable]"
    - "[NLRA § 8(a)(1) McLaren Macomb — Applied / Not applicable]"
    - "[ERA 1996 s.203 — Applied / Not applicable]"
    - "[California § 1542 waiver — Applied / Not applicable]"
  party_role: "[Plaintiff/Claimant / Defendant/Respondent / Joint]"
  provisions_drafted: "[count]"
  required_provisions_present: "[count] of [count required]"
  compliance_flags: "[List any open compliance items requiring user action]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED or UNVERIFIED]"
  case_law_consulted:
    - "[Case — VERIFIED or UNVERIFIED]"
  citations_verified: "[X VERIFIED] / [Y UNVERIFIED]"
  open_actions_before_execution:
    - "[e.g., 'Run 45-day ADEA consideration period before Employee can sign']"
    - "[e.g., 'File joint motion for FLSA approval before payment obligation arises']"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  tax_advice_required: "YES — settlement payment allocation must be reviewed by qualified tax counsel"
  reviewer: "AI-assisted — requires qualified legal review before execution"
```

---

## Anti-Patterns

Catalogue of what NOT to do when drafting settlement agreements:

1. **Omitting the specific ADEA/OWBPA statutory name**: Releasing "all federal claims"
   without naming the Age Discrimination in Employment Act by name and citation violates
   the OWBPA knowing-and-voluntary waiver requirement. A court will void the ADEA waiver
   even if the employee received 21 days and independent advice.

2. **Using age bands in the decisional unit disclosure**: EEOC guidance requires disclosure
   of individual ages (e.g., "39, 42, 51") not age ranges (e.g., "40–49"). Providing age
   ranges instead of individual ages renders the group-waiver disclosure non-compliant and
   voids the ADEA waiver. [VERIFY current EEOC enforcement position]

3. **Shortening the 7-day ADEA revocation period**: No provision, no waiver, and no
   mutual agreement can validly shorten the 7-day post-execution ADEA revocation period.
   Including language like "Employee agrees the revocation period is 3 days" has no legal
   effect and signals non-compliance.

4. **Broad NLRA non-disparagement/confidentiality**: Post-McLaren Macomb (2023), including
   a clause prohibiting employees from discussing employment terms, working conditions, or
   the settlement with anyone violates NLRA § 8(a)(1). This is not a minor drafting issue —
   the NLRB treats even offering such a clause as an unfair labor practice.

5. **Using age bands in decisional unit disclosures instead of individual ages**: Covered
   under #2 but deserves repetition — this is the single most common OWBPA compliance
   error in group-layoff situations.

6. **Relying on a merger clause alone to prevent fraud claims**: Courts consistently hold
   that an integration/merger clause alone does not prevent a claim for fraudulent
   inducement. Always add a "disclaimer of reliance" clause separately.

7. **Settling FLSA claims without court or DOL approval** (in litigation): In circuits
   that follow Cheeks, a Rule 41 stipulation of dismissal without court or DOL approval
   is not effective to settle FLSA overtime claims. The agreement will be unenforceable.
   Do not draft a FLSA settlement in a litigated case without the court approval mechanism.

8. **Blanket waiver of "all claims" in UK s.203 agreements**: UK law requires each
   statutory claim to be specifically identified by name and statutory reference. A clause
   releasing "all claims arising from employment" does not satisfy s.203 for any specific
   statutory claim and leaves all statutory rights intact.

9. **Omitting the no-assignment warranty**: A release by a party who has previously
   assigned the claim to a litigation funder or other third party is worthless. The
   no-assignment warranty catches this; omitting it creates an enforcement gap.

10. **Including confessions of judgment without checking state law**: Confessions of
    judgment are prohibited or severely restricted in California, New York (for consumer
    debts), and other states. Including them in a settlement governed by such states
    creates an unenforceable provision and may invalidate the enforcement mechanism entirely.

11. **Allocating 100% of a mixed employment settlement to "compensatory damages"**: Tax
    authorities scrutinize allocation. An employment settlement that allocates no amount
    to back pay defies economic reality and will be challenged by the IRS. All allocations
    must be economically defensible and consistently reported by both parties.

12. **Drafting a release without carving out vested benefits**: A release that inadvertently
    releases vested pension or 401(k) benefits creates significant exposure. ERISA rights
    may not be waivable; failing to carve them out creates ambiguity and possible ERISA
    preemption arguments.

13. **Settling EEOC administrative charges privately without withdrawing them**: If the
    employee has a pending EEOC charge and the parties settle privately, the EEOC charge
    remains pending until the employee formally withdraws it. The agreement should include
    an obligation to withdraw the charge and specify timing.

14. **Omitting the dismissal timing as a condition on payment**: Paying settlement funds
    before the dismissal is filed (or before FLSA court approval) means the payor has
    performed without receiving the benefit of the release. Always make payment conditional
    on (or concurrent with) dismissal and satisfaction of all conditions.

15. **Using mutual release language when only a unilateral release was negotiated**: If the
    deal contemplated only the employee releasing the employer, and the draft inadvertently
    includes a mutual release, the employer may be releasing claims it did not intend to
    release — including potential claims for misappropriation, trade secrets, or other
    misconduct discovered post-execution.

16. **Drafting a class action settlement without addressing side agreements**: Rule 23(e)(3)
    requires the parties to disclose any agreement made in connection with a proposed class
    settlement. Undisclosed side agreements are grounds for denial of final approval.

17. **Failing to address the tax impact on structured settlement annuity payments**: For
    personal injury settlements, structured settlement payments from a properly designed
    annuity are income-tax-free. But failure to comply with IRC §§ 104(a)(2) and 130
    (including qualified assignment) means the annuity payments lose their tax-free
    character. Get structured settlement tax advice before finalizing.

18. **Including an arbitration clause for disputes about the settlement agreement in a
    FLSA matter requiring court approval**: Cheeks-approval courts retain jurisdiction
    to enforce the approved settlement. An arbitration clause for disputes about the
    settlement may conflict with this retained jurisdiction. [VERIFY in your court/circuit]

19. **Signing a UK settlement agreement before the employee has had independent legal
    advice**: An agreement executed by the employee before the adviser has given advice
    (or before the adviser has countersigned) is not a valid s.203 settlement agreement.
    The signing sequence matters.

20. **Settling a minor's claim without court approval**: Every US jurisdiction requires
    court approval for minor's settlements, usually with appointment of a guardian ad
    litem. Proceeding without approval gives the minor the right to void the settlement
    upon reaching majority.

---

## Writing Standards

Apply plain-language discipline to all drafted settlement agreement provisions and
analysis output:

**For settlement agreement text (shared with opposing counsel and parties):**

- Active voice: "Company shall pay Employee" not "Payment shall be made by Company to Employee"
- Define terms on first use; use consistently throughout
- Numerals and words for monetary amounts: "$150,000 (One Hundred Fifty Thousand Dollars)"
- Specific dates, not relative references: "March 15, 2026" not "within 10 days of execution"
  where the execution date is known
- No double negatives: "Employee releases all claims" not "Employee does not retain any claim"
- One sentence per obligation where possible
- Parallel structure for list items

**For analysis and flagging output (for the drafting attorney):**

- Lead with the issue and classification (REQUIRED/OPTIONAL), then the reasoning
- Active voice throughout
- Name the specific statute or case, not just "applicable law"
- Confidence qualifiers where appropriate (see Confidence Scoring)
- Specific, not vague: "This provision violates NLRA § 8(a)(1) as interpreted by
  McLaren Macomb (2023) because it prohibits all discussion of employment terms" not
  "this may have NLRA issues"

**Quality gates before delivery:**

1. Can a non-lawyer client understand the plain meaning of each provision?
2. Has each REQUIRED provision been verified against its statutory requirements?
3. Is every statutory citation in a consistent format (US or UK as applicable)?
4. Are all monetary amounts stated in numerals and words?
5. Is the release scope aligned with the list of claims identified in Step 1?
6. Does the dismissal mechanism align with the payment condition?
7. Have all open compliance requirements been presented to the user in the cover memo?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for circuit-specific ADEA/OWBPA case law, state-specific non-compete
  enforceability, and applicable tax authority
- Verify current statutory text for ADEA, FLSA, NLRA, and applicable state law provisions
- Check currency of cited cases (McLaren Macomb; Cheeks applicability by circuit)
- For UK matters: verify current ERA 1996 s.203 requirements and ACAS Code of Practice
  edition
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Focus the analysis on structural quality and standard drafting patterns
- Add a prominent notice: "All statutory citations require independent verification by
  qualified counsel before relying on them in an executed agreement"

**Integration with other Legalcode skills:**

- **`legalcode-settlement-negotiation`**: Use before this skill for BATNA/ZOPA analysis
  and negotiation playbook; use the agreed economic and non-economic terms as input to
  this skill's Step 1
- **`legalcode-early-case-assessment`**: Use for merits assessment and probability of
  success; feed into settlement amount adequacy analysis
- **`legalcode-damages-calculation`**: Use to model exposure range; supports adequacy
  of consideration analysis (especially FLSA Cheeks "reasonable compromise" standard)

---

## Localization Notes

### United States — Jurisdiction-by-Jurisdiction Alerts

| Issue                      | Jurisdiction      | Rule                                                    | Reference                                                               |
| -------------------------- | ----------------- | ------------------------------------------------------- | ----------------------------------------------------------------------- |
| Non-compete enforceability | California        | Per se void                                             | Cal. Bus. & Prof. Code § 16600 (as amended by AB 1076, SB 699) [VERIFY] |
| Non-compete enforceability | New York          | "Reasonableness" test; limited to protectable interests | NY Ins. Law; common law [VERIFY]                                        |
| Non-compete enforceability | Minnesota         | Broadly unenforceable                                   | Minn. Stat. § 181.988 (effective July 2023) [VERIFY]                    |
| Confession of judgment     | California        | Prohibited for most consumers                           | Cal. Code Civ. Proc. § 1132 [VERIFY]                                    |
| Confession of judgment     | New York          | Restricted for consumers                                | CPLR § 3218 [VERIFY current scope]                                      |
| § 1542 waiver              | California        | Required for release of unknown claims                  | Cal. Civ. Code § 1542 [VERIFY]                                          |
| Minor settlement approval  | All US states     | Court approval required                                 | Varies by state [VERIFY threshold]                                      |
| FLSA Cheeks doctrine       | 2d, 11th Circuits | Court/DOL approval required in litigation               | 796 F.3d 199; [VERIFY in other circuits]                                |
| Workers' comp release      | Most US states    | Cannot privately waive; separate process required       | State workers' comp laws [VERIFY by state]                              |

### United Kingdom — Key Alerts

| Issue                                        | Rule                                                           | Reference                                                         |
| -------------------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------- |
| s.203 settlement — independent advice        | Mandatory for statutory claims waiver                          | ERA 1996 s.203 [VERIFY]                                           |
| s.203 — specific claims naming               | Each claim must be identified individually                     | ERA 1996 s.203(3)(b) [VERIFY]                                     |
| NDA restrictions (harassment/discrimination) | Cannot prevent police/regulatory reporting                     | SRA Code of Conduct 2019; PIDA 1998 [VERIFY current SRA guidance] |
| PILON taxation                               | Taxable from day one regardless of contractual basis           | ITEPA 2003 Part 6 Chapter 3 [VERIFY]                              |
| Settlement payment tax-free threshold        | First £30,000 of termination payment may be exempt             | ITEPA 2003 s.403 [VERIFY current guidance and applicable caps]    |
| Employment Tribunal withdrawal               | Must notify Tribunal; cannot privately settle pending ET claim | ET Rules of Procedure [VERIFY current Rules]                      |

---

## Output Format Template

Structure the deliverable as:

```markdown
# Settlement Agreement

**Parties**: [Names and roles]
**Settlement Type**: [Employment-ADEA / Employment-FLSA / Commercial / Class Action / etc.]
**Governing Law**: [Jurisdiction]
**Effective Date**: [Date]

---

## DRAFTING ATTORNEY COVER MEMO

**Compliance Actions Required Before Execution:**
[ ] [e.g., Run 45-day ADEA consideration period — agreement cannot be executed until [date]]
[ ] [e.g., File joint motion for FLSA court approval before payment obligation arises]
[ ] [e.g., Obtain independent legal advice for Employee — UK s.203 requirement]

**Open Items / User Decisions Needed:**
[ ] [e.g., Confirm whether mutual release or unilateral release]
[ ] [e.g., Confirm payment allocation for tax purposes with tax counsel]
[ ] [e.g., Confirm whether confession of judgment is enforceable in [state]]

**Post-Execution Checklist:**
[ ] Payment due: [date/condition]
[ ] Dismissal to be filed: [date/condition]
[ ] Administrative charge withdrawal: [date/condition]
[ ] UK: Adviser countersignature required before Employee signs

---

## SETTLEMENT AGREEMENT AND MUTUAL RELEASE

[Full draft agreement follows, organized by Provision 1-15]

---

## GLASS BOX AUDIT TRAIL

[YAML block per template above]
```

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis based on deep research into US
federal and UK statutory settlement agreement requirements (ADEA/OWBPA 29 U.S.C. § 626(f);
FLSA 29 U.S.C. § 216(b); Cheeks v. Freeport Pancake House, 796 F.3d 199 (2d Cir. 2015);
Fed. R. Civ. P. 23(e) and 41; NLRA 29 U.S.C. § 157; NLRB McLaren Macomb 372 NLRB No. 58
(2023); ERA 1996 s.203; ACAS Code of Practice on Settlement Agreements) and repository
best practices from the `legalcode-contract-review` quality framework and
`legalcode-settlement-negotiation` workflow patterns. Covers employment (ADEA/OWBPA,
FLSA, NLRA-compliant non-disparagement), commercial, and class action settlement types
for US and UK practice. All statutory citations require independent verification.

All citations in this skill carry hallucination risk. Verify against primary sources
before relying on them in an executed settlement agreement.
