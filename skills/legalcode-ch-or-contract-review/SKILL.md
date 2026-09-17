---
name: legalcode-ch-or-contract-review
description: Review contracts governed by Swiss law under the Code of Obligations (Obligationenrecht/OR/CO,
  SR 220).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review contracts governed by Swiss law under the Code of Obligations (Obligationenrecht/OR/CO, SR 220). Covers formation requirements (OR Art. 1-10), defects of consent — error (Art. 23-24), fraud (Art. 28), duress (Art. 29-30) — penalty clauses and Konventionalstrafe (Art. 160-163), assignment of claims / Abtretung (Art. 164-174), prescription and limitation periods (Art. 127-142, including the 2020 reform), and all five major specific contract types: sales/Kaufvertrag (Art. 184-238, Rügepflicht Art. 201), lease/Mietvertrag (Art. 253-304), work contract/Werkvertrag (Art. 363-379, 2026 warranty reform), mandate/Auftrag (Art. 394-406), and employment/Arbeitsvertrag (Art. 319-362, non-compete OR 340-340c, mass layoffs). Includes international private law / IPRG choice-of-law analysis (Art. 116-121), general standard terms (AGB) control, and Swiss enforcement mechanisms (SchKG/LP). Use for any contract governed by Swiss law: commercial agreements, services contracts, licensing, employment, leases, SaaS, supply chain, and cross-border deals with Swiss parties. Triggers on Swiss law, Swiss OR, Schweizer Recht, droit suisse, diritto svizzero, OR-governed, OR Art., Obligationenrecht, Code des obligations, Codice delle obbligazioni, Kaufvertrag, Werkvertrag, Auftrag, Mietvertrag, Arbeitsvertrag, Konventionalstrafe, Rügepflicht, Abtretung, OR 160, OR 201, OR 319, OR 394.


# Legalcode Swiss OR Contract Review

> **Disclaimer**: This skill provides a framework for AI-assisted legal review of contracts
> governed by Swiss law. It does not constitute legal advice. All outputs should be reviewed
> by a qualified legal professional licensed in Switzerland before use. Laws change; verify
> current applicability — particularly regarding the Werkvertrag warranty reform effective
> 1 January 2026 and the prescription reform effective 1 January 2020 — before relying on any
> provision described here. Statutory and case law references from memory carry hallucination
> risk; verify against authoritative Swiss sources (admin.ch, fedlex.admin.ch, bger.ch) before
> relying on them.

## Purpose and Scope

This skill reviews contracts governed by Swiss law against market standards, mandatory OR
provisions, and the user's negotiation playbook. It identifies deviations, assesses formation
validity, flags mandatory-law violations, generates confidence-scored redlines, and produces
an auditable analysis.

**Covers:**

- Contract formation validity under OR Art. 1-40 (offer/acceptance, essential terms, form)
- Defects of consent analysis (error OR 23-24, fraud OR 28, duress OR 29-30)
- General standard terms (AGB/CG) incorporation and unfair-clause control
- Prescription and limitation period compliance (OR 127-142, 2020 reform)
- Penalty clause (Konventionalstrafe) analysis and judicial-reduction risk (OR 160-163)
- Assignment of claims / Abtretung validity (OR 164-174)
- Contract-type-specific analysis across all five principal OR types
- Cross-cutting commercial clauses: liability, indemnity, IP, data protection, confidentiality
- International private law / IPRG choice-of-law analysis
- Swiss enforcement-mechanism awareness (SchKG/LP, arbitration IPRG Art. 176-194)
- Deviation classification (GREEN / YELLOW / RED) with redlines and fallback positions

**Does not:**

- Draft new contracts from scratch (use a drafting-specific skill)
- Provide legal advice or replace qualified Swiss counsel
- Substitute for cantonal-specific legal requirements (use `legalcode-ch-cantonal-law-navigator`)
- Cover Swiss financial regulatory law (FINMA, FinSA/FinIA) in depth [VERIFY scope with counsel]

## Jurisdiction and Governing Law

**Primary jurisdiction**: Switzerland — Federal Code of Obligations (Obligationenrecht/OR/CO,
SR 220), Swiss Civil Code (ZGB, SR 210), and Federal Act on Private International Law (IPRG,
SR 291).

**Legal system**: Civil law (Romano-Germanic tradition). Contracts are interpreted by seeking
the **true and common intention** of the parties (subjective method); if that cannot be
determined, by objective good-faith interpretation (Art. 18 OR). The OR fills contractual gaps
— shorter Swiss contracts are normal because the code provides default rules.

**Mandatory provisions**: Many OR provisions are mandatory (zwingend) and cannot be derogated
by agreement. Key non-derogable rules include: prescription periods (OR 129), certain employment
protections (OR 361-362), consumer protections (IPRG 120), and penalty clause reduction
(OR 163(3)). Always flag attempted contractual overrides of mandatory provisions as RED.

**Multilingual context**: Switzerland has three official legal languages — German (Deutsch/DE),
French (Français/FR), and Italian (Italiano/IT). Contracts in any of these languages are equally
valid. Where contracts contain divergent versions in multiple languages, a choice-of-language
provision is critical. Absent such a provision, the court will determine the authoritative text.

**[JURISDICTION-SPECIFIC]** When Swiss law governs, the following mandatory frameworks apply
by statute and cannot be excluded:

- Prescription periods and their modification limits (OR 127-142)
- Minimum employment protections (OR 361-362 list of non-derogable provisions)
- Penalty clause judicial-reduction right (OR 163(3))
- AGB unfair-terms control (UWG/LCD Art. 8 and OR good-faith principle)
- Consumer protections (IPRG Art. 120 + CO mandatory provisions)
- Werkvertrag warranty rights from 2026-01-01 (mandatory rectification right)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points (marked **⟁ CLARIFY**).
The workflow pauses when:

- The answer would change the direction of the analysis
- Contract type classification creates a fork in the analysis path
- Mandatory OR provisions apply differently depending on party status (consumer vs. B2B)
- Risk tolerance or business context is needed to classify severity correctly

When the user has already provided the information, skip the question and proceed. For any
unresolved ambiguity, state the assumption explicitly rather than proceeding silently.

---

## Workflow

### Step 1: Accept the Contract

Accept the contract in any of these formats:

- **File**: PDF, DOCX, or other document format
- **Pasted text**: Contract text pasted directly into the conversation
- **URL**: Link to a contract in a document management system

If no contract is provided, prompt the user to supply one.

### Step 2: Gather Context

**⟁ CLARIFY** — Ask before beginning. Skip questions already answered in the initial prompt.

1. **Which side are you on?**
   - Options: Seller/Vendor/Service Provider, Buyer/Customer/Client, Licensor, Licensee,
     Employer, Employee, Landlord/Lessor, Tenant/Lessee, Contractor (Werkvertrag), Principal
     (Auftrag/Mandate), Other
   - _Why this matters_: The entire analysis flips depending on which side you represent.

2. **Governing law confirmed?**
   - Options: Yes — explicit Swiss law clause present, Probably Swiss — no clause but Swiss
     parties/performance, Cross-border — foreign law selected but Swiss mandatory provisions
     may apply, Unclear — need to determine
   - _Why this matters_: Swiss mandatory provisions apply regardless of choice of foreign law in
     consumer contracts (IPRG 120) and some employment contexts (IPRG 121).

3. **Focus areas:**
   - Options: Formation validity / consent defects, Limitation/prescription periods, Penalty
     clauses, Employment protections, Lease rights, Werkvertrag warranty (especially post-2026),
     Sales / Rügepflicht, Liability and indemnity, IP ownership, Data protection, Cross-border
     / IPRG analysis, No specific focus — full review
   - Allow multiple selections.

4. **Deal context:**
   - Free text: deal size, strategic importance, B2B vs. B2C, consumer involved?,
     number of employees involved (for employment contracts), cross-border elements
   - _Why this matters_: Mandatory consumer and employment protections apply at different
     thresholds; deal size affects proportionality of redline effort.

5. **Deadline:**
   - Options: Urgent (days), Standard (1-2 weeks), Flexible

State any unresolved assumptions explicitly before proceeding.

### Step 3: Identify Contract Type Under OR

Determine the primary contract type and any mixed-contract elements. Swiss law categorizes
contracts into specific types (Nominalkontrakte) with dedicated statutory regimes, plus
innominate/atypical contracts (Innominatkontrakte) governed by general OR principles and analogy.

**⟁ CLARIFY** — If the contract type is ambiguous (e.g., a services agreement that could be
Auftrag OR Werkvertrag, or a SaaS agreement), ask:

- "This agreement could qualify as either a **Werkvertrag** (work contract — specific result
  owed) or an **Auftrag** (mandate — best efforts in principal's interest). The distinction
  affects warranty obligations, defect liability, and revocability. Which best describes the
  primary obligation?"
- "This appears to be an **Innominatkontrakt** — a contract type not specifically regulated in
  the OR. Swiss courts analyze these by analogy to the closest OR type. Which type seems
  closest: [suggest based on contract content]?"

**Primary contract type decision tree:**

| Contract                                   | OR Articles     | Key Indicator                   | Key Mandatory Provisions                           |
| ------------------------------------------ | --------------- | ------------------------------- | -------------------------------------------------- |
| **Kaufvertrag** (Sale)                     | 184-238         | Transfer of ownership for price | Rügepflicht (201), warranty for defects            |
| **Mietvertrag** (Lease)                    | 253-304         | Use and enjoyment for rent      | Notice periods, residential rent protection        |
| **Werkvertrag** (Work/Services for Result) | 363-379         | Specific result owed            | Warranty rights (2026 reform), defect notification |
| **Auftrag** (Mandate/Services for Efforts) | 394-406         | Best-efforts service            | Revocability (404), fiduciary duties               |
| **Arbeitsvertrag** (Employment)            | 319-362         | Subordinate work for salary     | OR 361-362 mandatory provisions list               |
| **Innominatkontrakt** (Atypical)           | 1-183 + analogy | Does not fit above types        | General OR principles; analogy to closest type     |
| **Mixed Contract** (Gemischter Vertrag)    | Multiple        | Elements of multiple types      | Apply each type's rules to the relevant elements   |

**SaaS/Technology contracts**: Swiss courts typically analyze SaaS as a mix of Auftrag (ongoing
service), Mietvertrag (use of software), and possibly Werkvertrag (implementation/customization).
Identify and apply the dominant type's rules. [VERIFY with Swiss IT law practitioners]

### Step 4: Verify Formation Validity

Before analyzing substantive provisions, check contract formation under OR Art. 1-40.

**4a. Essential terms (Essentialia negotii):**

- Identify the objectively essential elements for the identified contract type
- **Kaufvertrag**: object (Kaufsache) + price (Art. 184) — both must be sufficiently determined
  or determinable
- **Mietvertrag**: object + rent (Art. 253)
- **Werkvertrag**: work to be performed + remuneration (Art. 363; remuneration need not be
  agreed if customary rate applies under Art. 374)
- **Auftrag**: mandate description (remuneration not essential; gratuitous if not agreed, Art. 394(3))
- **Arbeitsvertrag**: work + salary + subordination (Art. 319; no formal requirement unless
  fixed-term or for school-leavers)
- Flag as RED any contract missing objectively essential terms

**4b. Form requirements:**

- General principle: no form required (Art. 11) unless statute prescribes otherwise
- Written form (Schriftform, Art. 13): required for certain contracts — check governing
  statutory provision
- Authenticated/notarized form (öffentliche Beurkundung): required for real estate transactions
  (ZGB 657), marriage contracts (ZGB 184), guarantee/surety in some cantons [VERIFY per canton]
- Non-compete clauses in employment: **must be in writing** (OR 340)
- Fixed-term employment beyond 3 months: best practice to confirm in writing
- Flag as RED any form deficiency for contracts requiring specific form

**4c. Defects of consent — screen for indicators:**

| Defect                              | OR Article | Trigger Indicator                                                                          | Consequence                                                               |
| ----------------------------------- | ---------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| Error / Fundamental Mistake         | 23-24      | Party misunderstood essential element; material discrepancy between intent and declaration | Voidable — must give notice within 1 year of discovery                    |
| Fraud / Deception (Täuschung)       | 28         | Party induced by deliberate misrepresentation                                              | Voidable regardless of whether error is fundamental; 1-year notice period |
| Duress (Drohung)                    | 29-30      | Party threatened with credible imminent harm                                               | Voidable — must act within 1 year                                         |
| Undue Exploitation (Übervorteilung) | 21         | Gross disproportion + exploitation of weakness                                             | Voidable within 1 year                                                    |

Flag any contract clause that purports to waive the right to rescind for defects of consent —
such waivers are ineffective under Swiss law for fundamental defects.

**4d. AGB / General Standard Terms incorporation:**

Screen all contracts containing boilerplate or general terms:

- Were the AGB brought to the counterparty's attention before or at contract conclusion?
- Did the counterparty have a reasonable opportunity to read them?
- **Unusual clause rule (Ungewöhnlichkeitsregel)**: Under BGE 4A_372/2022 (July 11, 2023),
  unusual or surprising clauses hidden in AGB are not incorporated — this applies in **B2B
  relationships** and is not limited to unequal bargaining power
- UWG Art. 8 / LCD Art. 8: AGB clauses creating a significant and unjustified imbalance to
  the detriment of consumers are unfair and unenforceable
- Flag as YELLOW any AGB that may not have been validly incorporated; flag as RED any clause
  that likely qualifies as unusual or unfair

### Step 5: Load Swiss Market Standards or Playbook

Check for the organization's contract review playbook.

**If no playbook is configured:**

**⟁ CLARIFY** — Inform the user and offer:

- **Option A: Set up a Swiss-specific playbook now** — Define standard positions for liability,
  indemnity, Konventionalstrafe caps, non-compete terms, data protection, and dispute resolution
  under Swiss law.
- **Option B: Proceed with Swiss market standards** — Use Swiss commercial practice and
  mandatory OR rules as the baseline. Label the review: "Based on Swiss market standards and
  mandatory OR provisions — not organizational playbook positions."
- **Option C: I'll provide positions as we go** — Ask during the review at each key clause.

### Step 6: Gather Swiss Legal Authority

Use **legalcode-mcp** to gather jurisdiction-relevant authority for this review.

**Research process:**

1. Confirm the governing law clause — note the exact formulation (e.g., "Swiss law" /
   "Schweizer Recht" / "droit suisse"). Flag absence of governing law clause as RED.

2. **Search legalcode-mcp** for:
   - Current text of relevant OR articles for the identified contract type
   - Recent Federal Supreme Court (BGer/TF) decisions on key issues in the contract
   - IPRG provisions if cross-border elements are present
   - ZGB provisions if property, succession, or family law elements arise
   - SchKG/LP enforcement framework if debt collection provisions are present

3. **Save results** to `/tmp/legalcode-ch-or-review.md`:

   ```markdown
   # Swiss OR Legal Authority — [Contract Name]

   ## Governing Law: Swiss Law (OR SR 220)

   ## Date Gathered: [date]

   ### Statutory Provisions

   - [OR Article — current text or summary — VERIFIED/UNVERIFIED]

   ### Federal Supreme Court Case Law (BGer/TF)

   - [Decision reference (e.g., BGE 4A_372/2022), key holding]

   ### IPRG (if cross-border)

   - [IPRG article, relevance]
   ```

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Focus the analysis on commercial risk and structural issues; flag legal-certainty gaps

### Step 7: Clause-by-Clause Analysis

Read the entire contract before flagging issues — clauses interact. Analyze against all
clause categories below. For long contracts (50+ pages):

**⟁ CLARIFY** — Ask: "This is a long contract. Should I perform a **full review** of all
clause categories, or a **priority review** focused on [user's stated focus areas] plus RED
items?"

Cover all clause categories applicable to the identified contract type:

#### General Commercial Clauses (All Contract Types)

| #   | Clause Category                          | Depth    | Key Swiss OR Review Points                                                   |
| --- | ---------------------------------------- | -------- | ---------------------------------------------------------------------------- |
| 1   | **Formation & Essential Terms**          | Deep     | Essentialia complete? Form requirement met?                                  |
| 2   | **Prescription / Limitation**            | Deep     | OR 127/128 periods; override attempts; 2020 reform applied?                  |
| 3   | **Penalty Clauses (Konventionalstrafe)** | Deep     | OR 160-163; judicial reduction risk; relationship to damages                 |
| 4   | **Assignment / Abtretung**               | Standard | OR 164: written form; debtor notification; assignment-exclusion validity     |
| 5   | **Limitation of Liability**              | Deep     | OR mandatory limits; intentional fault exclusion (OR 100); AGB control       |
| 6   | **Confidentiality**                      | Standard | Scope, duration, carveouts, return obligations                               |
| 7   | **Governing Law & Dispute Resolution**   | Deep     | Swiss law confirmed; arbitration seat; IPRG Art. 176 compliance              |
| 8   | **Data Protection**                      | Standard | nDSG (DSG SR 235.1, revised 2023); GDPR if EU data subjects; DPA requirement |
| 9   | **Assignment of Contract**               | Standard | OR 164ff. for claims; agreement transfer requires counterparty consent       |
| 10  | **Force Majeure**                        | Standard | OR gap: no statutory force majeure — contract clause critical                |
| 11  | **Term & Termination**                   | Standard | Mutual termination rights; cure period; effects of termination               |
| 12  | **Compliance & Regulatory**              | Standard | Anti-bribery (GwG SR 955.0); sanctions (EmbG SR 946.231); ESG (OR 964a-c)    |
| 13  | **Intellectual Property**                | Standard | Swiss IP statute ownership rules; moral rights (URG SR 231.1)                |
| 14  | **Definitions & Boilerplate**            | Standard | Entire agreement; severability; notices; amendment                           |

#### Contract-Type-Specific Clauses

**Apply the appropriate sub-section based on Step 3 classification.**

---

### Step 7a: Kaufvertrag (Sale) — OR Art. 184-238

**Key elements to review:**

**Rügepflicht (Duty to Notify Defects, OR 201) — Priority RED trigger:**

- The buyer must inspect goods upon receipt and notify the seller of defects **promptly** (unverzüglich)
  — typically interpreted as 3-7 days for discoverable defects, immediately upon discovery for
  hidden defects
- **Failure to notify on time forfeits all warranty rights** (Art. 201(3)) — this is among the
  most commercially significant mandatory rules in Swiss sales law
- Review: Is there a contractual notification period? Is it longer than immediately? A
  contractual extension beyond the statutory default is valid in B2B (Art. 201 is non-mandatory
  in commercial sales) [VERIFY]; shorter is generally not favorable to the buyer
- Flag as RED any provision that purports to eliminate the notification requirement entirely

**Risk transfer (OR 185):**

- Risk passes to buyer upon contract conclusion (not delivery) by default
- Flag as YELLOW any missing risk-transfer provision in contracts for specific goods
- For cross-border sales: check whether CISG applies (Switzerland is a Contracting State;
  parties may opt out under CISG Art. 6)

**Warranty for defects (Sachgewährleistung):**

- Seller warrants against physical and legal defects existing at time of risk transfer
- Buyer's remedies: Wandelung (withdrawal) or Minderung (price reduction); replacement for
  fungible goods
- Commercial warranty period: 2 years from delivery (Art. 210(1)); 5 years for works
  incorporated into immovables
- Warranty exclusion: valid in B2B if defect not fraudulently concealed; invalid in B2C for
  mandatory provisions [VERIFY]

**Title warranty (Rechtsmängelgewährleistung, OR 192-198):**

- Seller must ensure buyer receives clear title
- Screen for IP licenses sold: ensure seller has right to transfer

---

### Step 7b: Mietvertrag (Lease) — OR Art. 253-304

**Key elements to review:**

**Commercial vs. residential classification:**

- Residential (Wohn- und Geschäftsräume used for housing): stringent tenant protections apply
- Commercial (business premises only): more contractual flexibility; still subject to
  basic protections and good-faith termination rules

**Notice periods:**

- **Residential**: minimum 3 months to local term (Art. 266c/266d); many cantons have
  fixed local terms (Ortsgebrauch)
- **Commercial**: minimum 6 months to local term (Art. 266e); can be contractually extended
  but not shortened
- Flag as RED any notice period shorter than the statutory minimum for the lease type

**Termination for defects (OR 259a-259i):**

- Tenant may terminate, withhold rent (into escantonal deposit — Art. 259g), or demand repair
  for material defects
- Flag as YELLOW any provision that purports to waive defect-related remedies

**Rent adjustment and indexation:**

- Rent increases must follow the legally prescribed procedure (reference interest rate
  mechanism, Referenzzinssatz)
- Flat indexation clauses in residential leases are restricted [VERIFY current Referenzzinssatz
  mechanism applicability]

**Deposit:**

- Maximum 3 months' net rent for residential (Art. 257e); must be held in blocked bank
  account in tenant's name

---

### Step 7c: Werkvertrag (Work Contract) — OR Art. 363-379

> ⚠️ **2026 REFORM**: The Werkvertrag warranty rules were amended effective 1 January 2026
> for contracts involving **immovable works** (construction, renovation). Apply the new rules
> to any Werkvertrag executed or performed after this date.

**Key elements to review:**

**Result obligation (Erfolgsverpflichtung):**

- The contractor (Unternehmer) owes the specific agreed result — not just best efforts
- If the scope of work is ambiguous, determine whether this is really Werkvertrag or Auftrag
  (best-efforts mandate) — the distinction is critical for warranty liability

**Defect notification — 2026 Reform (immovable works):**

- **Pre-2026**: Buyer must notify defects immediately (unverzüglich) upon discovery
- **Post-2026 (from 1 January 2026)**: 60-day notification period for both visible defects
  (after acceptance) and hidden defects (after discovery) in contracts for immovable works
- Flag as RED any contract for immovable works that purports to shorten the 60-day period
  below the statutory minimum

**Mandatory rectification right — 2026 Reform:**

- **From 1 January 2026**: The employer/principal has a mandatory right to demand rectification
  of defects in immovable works — this right **cannot be contractually excluded**
- Flag as RED any clause in a post-2026 immovable Werkvertrag that purports to exclude or
  limit the rectification right

**Limitation period — 2026 Reform:**

- **Pre-2026**: 5 years for immovable works, 2 years for movable works
- **Post-2026**: 5-year limitation period confirmed and clarified for immovable works; ensure
  contracts do not purport to shorten this period

**Acceptance (Abnahme, OR 367):**

- Formal acceptance triggers the start of the defect-notification period
- Review: Is there an explicit acceptance procedure? Are defects noted at acceptance treated as
  notified? Is there a provisional/final acceptance distinction (common in construction)?

**Price (OR 373-374):**

- Fixed price (Pauschalpreis): contractor bears cost overrun risk; employer bears design-change risk
- Open price (Regie): employer bears cost-escalation risk
- Flag as YELLOW any price structure without a clear change-order/Nachtragsmanagement mechanism

**SIA norm integration:**

- In Swiss construction, the SIA 118 general conditions are commonly incorporated by reference
- If incorporated: flag any derogations from SIA 118 that disadvantage the client [VERIFY
  incorporation language]

---

### Step 7d: Auftrag (Mandate/Services for Efforts) — OR Art. 394-406

**Key elements to review:**

**Best-efforts obligation (Sorgfaltspflicht):**

- The agent (Beauftragter) owes diligent performance in the principal's interest — not a
  guaranteed result
- Review: Does the contract correctly characterize the obligation? Mischaracterizing an
  Auftrag as Werkvertrag creates implied result-warranties the parties may not intend

**Revocability (OR 404):**

- **Either party may revoke/terminate the mandate at any time** — this is a mandatory rule
  (zwingend) and cannot be contractually excluded
- Compensation may be owed for poorly-timed revocation (OR 404(2))
- Flag as RED any clause purporting to make the mandate irrevocable

**Fiduciary duty and conflicts of interest:**

- Agent must disclose conflicts of interest and not pursue self-interest to the principal's
  detriment (OR 398)
- Review: Are conflict-of-interest disclosure obligations present? Are agency fee / commission
  arrangements transparently disclosed?

**Remuneration:**

- If no fee is agreed, customary fees apply (OR 394(3) — Auftrag is not presumed gratuitous
  in commercial contexts)
- Review: Is fee structure clear? Is it contingent-fee / pactum de quota litis? [VERIFY
  enforceability in Switzerland — restrictions apply for certain professional mandates]

**Sub-mandate:**

- Agent may delegate only if authorized or if delegation is customary (OR 398(3))
- Review: Is sub-contracting/sub-mandate expressly authorized? Are flow-down obligations
  required?

---

### Step 7e: Arbeitsvertrag (Employment) — OR Art. 319-362

> Note: Swiss employment law has a **two-tier mandatory structure**: OR Art. 361-362 lists
> provisions that are non-derogable in any direction (Art. 361) and provisions derogable only
> in favor of the employee or by collective agreement (Art. 362). Any contractual deviation from
> Art. 361 provisions is automatically void; Art. 362 deviations are void only if to the
> employee's detriment.

**Key elements to review:**

**Notice periods (OR 335a-335c) — AUTO-RED if violated:**

- Statutory minimum notice periods:
  - Year 1 (probation excluded): **1 month** at end of any month
  - Years 2-9: **2 months** at end of any month
  - Year 10+: **3 months** at end of any month
- Contractual periods may only be **equal** or **longer** for both parties — asymmetric periods
  favor the employer and require scrutiny
- Flag as RED any contractual notice period shorter than the statutory minimum for the
  applicable service year

**Probation period:**

- Statutory default: 1 month (OR 335b(1))
- Contractual extension permitted up to **3 months maximum** (OR 335b(2))
- Flag as RED any probation period exceeding 3 months

**Protection from dismissal during incapacity (OR 336c) — AUTO-RED if violated:**

- Dismissal given during statutory protection periods is void (nichtig) — key periods:
  - Illness/accident: 30 days (year 1), 90 days (years 2-5), 180 days (year 6+)
  - Military service / civil protection / civil service
  - Pregnancy and 16 weeks after delivery (Art. 336c(1)(c))
  - Swiss Federal BGer 1C_595/2023 (2024): job-related incapacity may not trigger full blocking
    period [VERIFY]
- Flag as RED any termination during these periods without proper legal advice

**Abusive termination (Missbräuchliche Kündigung, OR 336):**

- Non-exhaustive catalogue of abusive grounds (OR 336(1)(a)-(f)): personality characteristics,
  exercising legal rights, discriminatory motivation, retaliation
- Remedy: up to **6 months' salary** compensation (OR 336a) — not reinstatement
- Review: Does the employment agreement contain provisions that, if enforced, would qualify as
  abusive termination triggers? Are there dispute resolution provisions for wrongful dismissal?

**Non-compete clause (Konkurrenzverbot, OR 340-340c):**

- Valid only if **all three** conditions are met:
  1. Employee had access to customer circles, manufacturing secrets, or business secrets
  2. Restriction is in **written form** (OR 340)
  3. Restriction is **limited in time** (maximum 3 years), **geographic scope**, and
     **subject matter** to what is reasonably necessary
- **Automatic lapse**: Non-compete lapses if employer terminates without just cause, or if
  employee leaves for just cause attributable to employer (OR 340c(2))
- Penalty/Konventionalstrafe in non-compete: common but subject to OR 163(3) judicial reduction
- Flag as RED any non-compete exceeding 3 years or lacking geographic/subject-matter limitation
- Flag as YELLOW any non-compete without a clear Konventionalstrafe or compensation clause

**Mass layoffs (Massenentlassung, OR 335d-335g):**

- Definition (OR 335d): employer with 20+ employees terminating within 30 days for economic
  reasons — 10-29 employees: 10+ terminations; 30-99 employees: 10% or more; 100+ employees: 30+
- Process requirements (OR 335f):
  1. Consult with employees / employee representatives in good faith
  2. Notify cantonal labour office (KAST) in writing
  3. Mandatory 30-day waiting period from KAST notification before dismissals take effect
- Social plan (Sozialplan): mandatory for companies with 250+ employees terminating 30+ within
  30 days (OR 335h)
- Non-compliance: dismissals during waiting period may be challenged as abusive
- Flag as RED any mass-layoff provisions that purport to waive or shorten statutory consultation
  and waiting periods

**Mandatory benefits (non-derogable, OR 361):**

- Minimum vacation: 4 weeks per year (OR 329a); 5 weeks for employees under 20
- Continued pay during incapacity to work (OR 324a): employer must pay during illness/accident
  for a period scaled to years of service (1 month year 1, 2 months years 2-5, etc.) unless
  adequate insurance coverage is maintained
- Protection from garnishment of wage beyond minimum living amount (SchKG 93)

---

### Step 8: Missing Clause Detection

After analyzing present clauses, check for critical absent clauses:

| Missing Clause                       | Contract Types                | Severity | Note                                          |
| ------------------------------------ | ----------------------------- | -------- | --------------------------------------------- |
| No governing law clause              | All                           | RED      | Swiss courts will apply IPRG to determine law |
| No force majeure (OR has no default) | Long-term contracts           | YELLOW   | Swiss OR has no statutory force majeure       |
| No Konventionalstrafe                | Employment, services          | YELLOW   | Parties lose a powerful enforcement tool      |
| No defect notification procedure     | Kaufvertrag, Werkvertrag      | RED      | Rügepflicht / notification deadline crucial   |
| No acceptance procedure              | Werkvertrag                   | YELLOW   | Ambiguous acceptance triggers prescription    |
| No data processing agreement         | Any — personal data processed | RED      | Revised DSG (nDSG) requires DPA               |
| No limitation of liability           | All B2B                       | YELLOW   | Unlimited exposure under OR                   |
| No change-of-control provision       | Strategic contracts           | YELLOW   | Assignment of contract requires consent       |
| No non-compete (employment)          | Senior employees              | YELLOW   | Assess whether exposure requires protection   |
| No social plan provision             | Potential mass layoff         | YELLOW   | May become mandatory                          |
| No language / translation provision  | Multilingual contracts        | YELLOW   | Dispute-risk if versions diverge              |

**⟁ CLARIFY** — For missing clauses where severity depends on context, ask:

- "This contract has no force majeure clause. Given the term length and nature of performance,
  is this a concern? Swiss OR has no default force majeure provision."
- "There is no Konventionalstrafe for breach of the [non-compete / delivery obligation / exclusivity].
  Would the organization like one added? This is the primary Swiss mechanism for liquidated damages."

### Step 9: Generate Redlines

**⟁ CLARIFY** — Before generating redlines, confirm negotiation posture:

- **Relationship dynamic**: new counterparty / existing partner / must-have vendor?
- **Volume**: "I've found [N] items. Focus on top RED items only, or generate all YELLOW too?"

For each YELLOW and RED deviation, generate a redline using the **Redline Format** below,
applying **Swiss-specific legal drafting standards** (plain German/French/Italian as appropriate).

---

## Swiss OR Clause Analysis Reference

### 1. Prescription / Limitation Periods (OR 127-142)

**2020 reform — check applicability:**

- General period (OR 127): **10 years** for all claims not subject to shorter period
- Short periods (OR 128): **5 years** for:
  - Periodic payments (rent, interest, maintenance)
  - Retail goods and work performed (craftsmen, retailers, innkeepers)
  - Medical/legal/professional services
  - Wages and salaries
- Personal injury tort/unjust enrichment (OR 128a, added 2020):
  - **3 years** relative (from knowledge of damage and obligor)
  - **20 years** absolute (from the date of the harmful act/event)
  - Pre-2020 contracts may still carry the old 1-year relative period for personal injury [VERIFY]
- **Non-derogation rule (OR 129)**: Prescription periods cannot be modified by agreement
  — any contractual reduction is void. Parties may not agree to a shorter period. [NOTE: Some
  academic views allow consensual extension; extension clauses warrant [VERIFY]]

**Common issues:**

- Purported contractual reduction of prescription periods (void under OR 129)
- Missing prescription waiver / standstill provisions in settlement negotiations
- Short 5-year period not accounted for in service contracts billed periodically
- Cross-border contracts not checking whether CISG's 4-year CISG-limitation (UN Limitation
  Convention, not ratified by Switzerland) or local law governs

### 2. Penalty Clauses / Konventionalstrafe (OR 160-163)

**Core framework:**

- OR 160: Penalty clause valid without restriction on amount agreed by parties
- OR 160(2): If penalty stipulated for non-performance, creditor cannot claim both penalty AND
  performance (must choose) — unless parties expressly agreed otherwise
- OR 161: Penalty accrues when performance is not rendered; default notice (Mahnung) required
  if the penalty is for delay (not for non-performance)
- OR 163(3): **Court may reduce penalties considered excessive** — this is a non-waivable right.
  Criteria include: severity of breach, economic circumstances, proportionality to harm suffered

**Key issues:**

- Penalty combined with damages: parties may agree that the penalty is in lieu of damages
  OR that it is a minimum and further damages may be claimed — check which approach
- Relationship to limitation clauses: does the limitation clause cap Konventionalstrafe recovery?
- Employment non-compete Konventionalstrafe: subject to judicial reduction; courts look at
  remuneration level and nature of breach (BGer 4A_202/2024, 4A_212/2024 — Sep 2024 confirmed
  reduction in SPA non-compete context)

**Classification:**

- Penalty amount proportionate to protected interest and likely harm: GREEN
- Penalty potentially excessive but not manifestly disproportionate: YELLOW (flag OR 163(3) risk)
- Penalty manifestly disproportionate / intended as punitive: RED (high judicial-reduction risk)

### 3. Assignment of Claims / Abtretung (OR 164-174)

**Core requirements:**

- Assignment valid only if **in writing** (OR 165(1)) — oral assignment is void
- Assignment-exclusion clauses (Abtretungsverbote) in B2B: valid but debtor must have
  interest and clause must be in writing; cannot prevent assignment based on written debt
  acknowledgment without express prohibition
- Debtor must be notified — until notification, debtor may discharge by paying original creditor
  (OR 167)
- Partial assignment (Teilabtretung): valid for divisible claims

**Common issues:**

- Assignment clauses in SaaS / service contracts that prohibit assignment without consent —
  determine whether this covers entire contract (consent required) vs. individual claims only
- Security assignment (Sicherungszession): valid under Swiss law; no registration requirement
  (unlike pledge); but may be recharacterized [VERIFY in financial services context]
- Cross-border assignment: IPRG Art. 145 — assignment governed by law agreed by parties or
  law of assignor's habitual residence

### 4. Limitation of Liability (Swiss OR Application)

**Intentional fault exclusion (OR 100):**

- **Mandatory rule**: Liability for intentional misconduct (Absicht, dolus) **cannot be excluded
  by agreement** — any such clause is void
- Liability for gross negligence (grobe Fahrlässigkeit) can be excluded only in commercial B2B
  contexts and even then with limits [VERIFY — some academic divergence; courts narrow]
- Liability for simple negligence: freely excludable in B2B

**AGB / standard terms:**

- Limitation clauses in AGB are subject to the unusual-clause rule (Ungewöhnlichkeitsregel)
  — extremely broad or one-sided limitations may be deemed not incorporated (BGer 4A_372/2022)
- Consumer contracts: consumer protection rules limit exclusions (IPRG 120 + CO provisions)

**Key issues:**

- Limitation clause that purports to exclude liability for intentional fault: RED (void under OR 100)
- Asymmetric limitation favoring only one party: YELLOW
- Cap amount far below reasonably anticipated loss: YELLOW
- No exclusion of consequential damages (indirekte Schäden): no statutory prohibition, but
  must be expressly agreed — implied exclusions may be challenged

### 5. Governing Law and Dispute Resolution

**Swiss law selection:**

- Parties may select Swiss law under IPRG Art. 116 — this is a valid, recognized choice
- Swiss law applies to the merits; procedural law is determined by the seat of proceedings

**IPRG Art. 120 — Consumer contracts:**

- If the contract is with a consumer and the supplier directed activities to the consumer's
  country, the mandatory provisions of the consumer's domicile apply regardless of choice of
  Swiss law — flag for consumer-facing contracts

**IPRG Art. 121 — Employment contracts:**

- Mandatory provisions of the law of the employee's usual place of work (or place of business
  if no fixed place) apply regardless of governing law choice

**Arbitration (IPRG Art. 176-194):**

- International arbitration with seat in Switzerland and at least one non-Swiss party governed
  by IPRG Chapter 12 (Art. 176-194), reformed effective 1 January 2021
- Swiss Rules (Swiss Arbitration Centre): well-established institutional rules
- Arbitrability: all disputes with pecuniary value are arbitrable under Swiss law (Art. 177(1))
- Domestic arbitration: ZPO Art. 353-399

**Common issues:**

- No governing law clause in cross-border contract (RED — costly to resolve)
- Foreign law selected without considering Swiss mandatory provisions for employees/consumers
- "Pathological" arbitration clause with ambiguous seat, institution, or rules
- Dispute resolution clause not covering all disputes arising under the contract

---

## Deviation Severity Classification

### GREEN — Compliant / Acceptable

The clause complies with mandatory OR requirements and aligns with or exceeds Swiss market
standards. Minor variations that do not increase legal or commercial risk.

**Examples:**

- Notice period longer than statutory minimum (better for employee)
- Warranty period extended beyond statutory 2 years (better for buyer)
- Liability cap set at 12 months' fees in standard B2B services contract
- Swiss law / Swiss arbitration clause properly drafted

**Action**: Note for awareness. No negotiation needed.

### YELLOW — Non-Compliant with Market Standard / Negotiate

The clause deviates from Swiss market standards or best practice, but does not violate
mandatory OR provisions. Requires attention and likely negotiation.

**Examples:**

- Limitation clause excluding gross negligence without adequate countervailing terms
- Konventionalstrafe amount potentially disproportionate (judicial reduction risk)
- Non-compete clause geographically broad but within the 3-year maximum
- Force majeure clause omitted in a multi-year agreement
- Auftrag with limited revocability provisions (not invalid — irrevocability is RED)
- Assignment clause with no change-of-control carveout

**Action**: Generate specific redline language. Provide fallback position. Assess judicial
reduction risk for Konventionalstrafe. Note market-standard comparison.

### RED — Violates Mandatory OR / Escalate

The clause violates a mandatory OR provision, is void or voidable, creates unacceptable
legal exposure, or conflicts with non-derogable Swiss law.

**Examples:**

- Notice period shorter than statutory minimum (Art. 335c — void)
- Exclusion of liability for intentional fault (OR 100 — void)
- Non-compete exceeding 3 years (OR 340(3) — void; court will reduce but uncertainty remains)
- Purported elimination of Konventionalstrafe judicial-reduction right (OR 163(3) — void)
- Assignment without written form (OR 165(1) — invalid)
- Werkvertrag (post-2026) excluding mandatory rectification right (void)
- Auftrag purporting to be irrevocable (OR 404 — void)
- Missing Rügepflicht provision where rapid notification is required
- No DPA where personal data is processed (nDSG requirement)
- Employment dismissal during statutory protection period (OR 336c — void)
- Mass layoff without mandatory consultation and waiting period

**Action**: Explain specific mandatory rule violated. Identify void/voidable consequence.
Provide compliant alternative language. Recommend qualified Swiss counsel review.

---

## Redline Format

For each redline:

```
**Clause**: [Section reference and clause name, original language if in German/French/Italian]
**Current language**: "[exact quote]"
**Proposed redline**: "[specific alternative language]"
**Rationale**: [1-2 sentences in plain language suitable for external sharing]
**Legal basis**: [Relevant OR article / BGer decision — or "Swiss market practice"]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative position if primary redline is rejected]
**Swiss-specific note**: [Any mandatory-law limits or judicial-reduction risk]
```

### Redline Best Practices (Swiss Context)

1. **Draft in the contract's language** — Swiss contracts are often in German, French, or Italian.
   Provide redlines in the language of the agreement, with an English translation if helpful.
2. **Cite the OR article** — Swiss counterparties respond well to specific statutory citations.
   Mark unverified citations [VERIFY].
3. **Distinguish mandatory from default rules** — When a clause violates a mandatory provision,
   say so explicitly ("This clause is void under OR Art. [X]"). When it deviates from a default
   rule, flag as market practice.
4. **Provide fallback positions** — Always offer an alternative, especially for Konventionalstrafe
   and non-compete clauses where judicial adjustment is likely anyway.
5. **Flag judicial-reduction risk** — For Konventionalstrafe clauses, note OR 163(3) judicial
   reduction risk so the client can make an informed decision.

---

## Negotiation Priority Framework (Swiss Context)

### Tier 1 — Must-Haves (OR Mandatory Compliance)

Issues where the clause violates mandatory OR provisions or creates void/voidable terms:

- Clauses void under OR 100 (intentional fault exclusion)
- Employment notice periods below OR 335c minimums
- Non-compete clauses exceeding 3-year maximum or lacking written form
- Auftrag irrevocability clauses (void under OR 404)
- Post-2026 Werkvertrag clauses excluding mandatory rectification
- Assignment clauses without written form (OR 165)
- Mass-layoff procedures bypassing statutory consultation requirements
- No governing law clause in cross-border contract
- Absence of DPA for personal data processing

### Tier 2 — Should-Haves (Material Risk / Market Deviation)

Issues outside mandatory law but material to risk or market standard:

- Limitation of liability cap and carveouts
- Konventionalstrafe proportionality (judicial-reduction risk)
- Force majeure clause (OR has no statutory default)
- Non-compete geographic and temporal reasonableness
- Warranty period and defect notification procedure
- Assignment / change-of-control protections
- Data protection terms and processor obligations

### Tier 3 — Nice-to-Haves (Concession Candidates)

Issues that improve position but may be conceded strategically:

- Preferred arbitration institution (if any recognized Swiss institution is acceptable)
- Notice period preferences beyond statutory minimums
- Governing language choice (where all versions are adequate)
- Minor definitional improvements
- Boilerplate refinements

**Negotiation strategy**: Lead with Tier 1 mandatory-law items — these are non-negotiable by
definition. Trade Tier 3 concessions to secure Tier 2 wins. Never concede on Tier 1 without
qualified Swiss counsel sign-off.

---

## Quality Assurance Framework

### PDCA Quality Cycle (Swiss Adaptation)

**PLAN**: Identify contract type under OR. Confirm governing law. Note applicable mandatory
provisions for the contract type. Identify IPRG cross-border considerations.

**DO**: Execute the clause-by-clause analysis. Classify deviations. Generate redlines.
Apply Swiss-law-specific analysis for each contract type.

**CHECK**: Run Citation Quality Gates. For RED items, run Self-Interrogation. Verify all OR
articles cited. Confirm mandatory vs. default rule classification.

**ACT**: Flag any novel clause structure or emerging Swiss market position for playbook update.
Note Werkvertrag/employment reform applicability.

### Citation Quality Gates (Swiss OR Adapted)

Run these 5 gates silently before delivering output. Revise any failures before delivering.

| Gate           | Rule                                                                                                                       | Fail Action                                                    |
| -------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific OR article, BGer decision, or established Swiss principle                               | Add citation or mark "[UNVERIFIED — Swiss counsel to confirm]" |
| **Format**     | Citations follow Swiss legal citation format: "OR Art. [X]", "BGE [volume] [number]", "BGer [date/case number]"            | Fix format                                                     |
| **Currency**   | Each provision checked for amendments — particularly 2020 prescription reform and 2026 Werkvertrag reform                  | Flag "[CHECK CURRENCY — verify at fedlex.admin.ch]"            |
| **Domain**     | Analysis stays within Swiss OR and applicable Swiss law — no leakage of foreign law concepts unless IPRG analysis warrants | Remove or flag jurisdictional bleed                            |
| **Confidence** | Uncertainty explicitly stated — especially for mandatory vs. default rule classification                                   | Add confidence qualifier                                       |

### Self-Interrogation for RED Items

For any clause classified RED, apply this 3-pass self-interrogation before delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the void/voidable classification follow directly from the cited OR article?
- Which specific provision of OR 361, OR 100, OR 163(3), OR 404, etc. applies?
- Would the Federal Supreme Court actually reach this conclusion? Check BGer precedent.

**Pass 2 — Completeness**:

- Have all relevant mandatory OR provisions been considered?
- Are there cantonal variations or collective agreement provisions that modify the OR default?
- Does the IPRG analysis change the outcome for cross-border elements?

**Pass 3 — Challenge**:

- What is the strongest argument that this clause is enforceable despite the mandatory OR provision?
- Is there BGer case law creating exceptions or safe harbors?
- Is the RED classification proportionate, or is this actually YELLOW with a [VERIFY] flag?

Revise if any pass reveals a weakness. Mark audit trail: `self_interrogation: PASS` or
`self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                                  | Action                                                                 |
| ------------ | --------- | -------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Clear mandatory OR provision, settled BGer jurisprudence | State with confidence                                                  |
| **High**     | 0.80-0.94 | Strong OR authority, minor interpretation questions      | State with brief caveat                                                |
| **Probable** | 0.60-0.79 | Good arguments; reasonable Swiss lawyers might differ    | State with reasoning and contra-indicators                             |
| **Possible** | 0.40-0.59 | Genuinely uncertain; competing BGer lines                | Flag for qualified Swiss counsel with both sides                       |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative                                  | Do not assert — flag "[UNCERTAIN — qualified Swiss counsel to advise]" |

---

## Glass Box Audit Trail

Every output MUST include this Glass Box audit section:

```yaml
glass_box:
  contract: "[Contract title and date]"
  contract_type: "[Kaufvertrag / Werkvertrag / Auftrag / Mietvertrag / Arbeitsvertrag / Mixed / Innominatkontrakt]"
  user_side: "[Seller/Buyer/Employer/Employee/Contractor/Principal/Landlord/Tenant/Other]"
  governing_law: "Swiss Law (OR SR 220)"
  playbook_used: "[Playbook name or 'Swiss market standards']"
  werkvertrag_reform_applied: "[Yes — 2026 reform applied / No — pre-2026 rules / N/A]"
  prescription_reform_applied: "[Yes — 2020 reform applied / N/A]"
  clauses_reviewed: "[number]"
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to /tmp/legalcode-ch-or-review.md or 'Not created']"
  statutes_consulted:
    - "[OR Art. X — VERIFIED (legalcode-mcp) / UNVERIFIED]"
    - "[IPRG Art. X — VERIFIED / UNVERIFIED]"
    - "[ZGB Art. X — VERIFIED / UNVERIFIED]"
  bger_decisions_cited:
    - "[BGer decision reference — VERIFIED / UNVERIFIED]"
  mandatory_provisions_flagged: "[list of OR mandatory provisions triggered]"
  citations_verified: "[N VERIFIED] / [N UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  iprg_analysis: "[Yes — cross-border elements / No — purely domestic]"
  limitations:
    - "[Scope limitations, cantonal variations requiring separate analysis, etc.]"
  reviewer: "AI-assisted — requires qualified Swiss legal review"
```

---

## Multi-Stakeholder Mapping

For every contract, identify all affected stakeholders beyond the two contracting parties:

| Stakeholder            | Role                          | Affected Clauses                        | Impact     | Action Required     |
| ---------------------- | ----------------------------- | --------------------------------------- | ---------- | ------------------- |
| [Party A]              | [Buyer/Employer]              | All                                     | Primary    | Sign / Negotiate    |
| [Party B]              | [Seller/Employee]             | All                                     | Primary    | Sign / Negotiate    |
| [Data subjects]        | Third party                   | nDSG/GDPR provisions                    | Indirect   | DPA required        |
| [Cantonal authorities] | Regulator                     | Employment (KAST), land registry        | Compliance | Notifications       |
| [Creditors/lenders]    | Third party                   | Assignment, change of control           | Indirect   | Consent required?   |
| [Employees]            | Internal (employment context) | OR 335d mass layoff                     | Direct     | Consultation rights |
| [Tax authorities]      | Regulator                     | ESG reporting, cross-border structuring | Compliance | Verify              |

---

## Anti-Patterns

Swiss OR contract review: what NOT to do.

1. **Treating OR as a common-law contract** — Swiss contracts are shorter because the OR fills
   gaps by statute. Do not flag absent boilerplate as missing when the OR default adequately
   covers the situation. Focus on derogating mandatory rules, not importing common-law clauses.

2. **Confusing Auftrag and Werkvertrag** — The distinction determines warranty liability, defect
   notification obligations, and revocability. A services contract labeled "Werkvertrag" that is
   substantively an Auftrag creates unintended warranty exposure. Always characterize before
   analyzing specific remedies.

3. **Ignoring the Rügepflicht (OR 201)** — Failure to notice the absence or inadequacy of a
   defect-notification procedure in a Kaufvertrag or Werkvertrag is a material omission. Late
   notification forfeits all warranty rights.

4. **Missing the 2026 Werkvertrag reform** — Not applying the new 60-day notification period,
   mandatory rectification right, and amended limitation period to post-2026 contracts for
   immovable works. This reform significantly changes the client's contractual position.

5. **Accepting liability exclusions for intentional fault** — Any clause purporting to exclude
   liability for intentional misconduct is void under OR 100. Do not analyze it as a negotiating
   point — it is unenforceable by statute.

6. **Missing the Konventionalstrafe judicial-reduction risk** — OR 163(3) gives courts the
   discretion to reduce excessive penalties. A Konventionalstrafe should be sized to survive
   judicial scrutiny — flagging this risk is part of the review, not optional.

7. **Not assessing AGB for the unusual clause rule** — Under BGer 4A_372/2022, surprising or
   unusual clauses in general terms are not incorporated even in B2B contracts. Reviewing AGB
   without applying this doctrine risks approving terms that may not form part of the contract.

8. **Importing common-law indemnity concepts** — "Indemnification" as a primary obligation
   distinct from damages is not a native Swiss law concept. Under OR, the equivalent analysis
   flows through Schadenersatz (OR 97/41) and contractual Garantie/Gewährleistung. Using
   common-law indemnity framing in a Swiss law analysis misleads.

9. **Missing IPRG consumer and employment mandatory-provision analysis** — Where a Swiss-law
   contract involves a consumer or employee in a foreign jurisdiction, or where a foreign-law
   contract involves a Swiss consumer or employee, IPRG Art. 120/121 mandatory provisions may
   override the choice of law. This is a common miss in cross-border transaction reviews.

10. **Applying old prescription periods without checking the 2020 reform** — The 2020 reform
    extended the relative personal-injury limitation period from 1 year to 3 years and introduced
    a new 20-year absolute period. Contracts and claims arising before 2020 may still be subject
    to the old rules. Check which version applies.

11. **Approving an irrevocable Auftrag** — OR 404 is mandatory. Any clause making a mandate
    irrevocable is void. Parties can agree on compensation for untimely revocation, but cannot
    eliminate the revocation right itself.

12. **Missing the multilingual contract problem** — Swiss contracts are often in German, French,
    or Italian, sometimes in multiple versions. Failing to identify which version is authoritative
    creates interpretation risk when versions diverge.

13. **Skipping the employment mandatory-provisions checklist** — The two-tier structure of OR 361
    (absolutely mandatory) and OR 362 (mandatory in favor of employee) is a trap for non-Swiss
    practitioners. Any employment agreement review must cross-check against both lists.

14. **Assuming cantonal law does not matter** — The OR is federal, but cantonal procedural rules,
    court structures, and in some areas substantive rules (notarization requirements, land law,
    tax) affect enforceability. Flag cantonal-specific issues for the `legalcode-ch-cantonal-law-navigator`.

15. **No analysis of SchKG enforcement** — Swiss enforcement of contract claims goes through the
    formal Betreibung procedure. A contract without clear monetary claims, interest provisions,
    or debt acknowledgment may be harder to enforce. Flag the absence of debt acknowledgment
    (Schuldanerkennung) where relevant.

16. **Treating the penalty clause as unlimited protection** — The Konventionalstrafe accrues
    automatically only for non-performance; for delay, a Mahnung (notice of default) is required
    unless agreed otherwise (OR 161(2)). A penalty clause with no activation-notice provision
    may leave the creditor in an unexpected gap.

17. **Assuming CISG does not apply** — Switzerland is a party to the CISG. For international
    B2B sales contracts with counterparties in other CISG states, CISG applies by default unless
    expressly excluded (CISG Art. 6). Not flagging a missing CISG opt-out in a Swiss sales
    contract is a material gap.

---

## Writing Standards

Apply plain-language discipline to all output:

**For redlines and rationales** (shared with counterparty's counsel):

- Draft in the contract language (German/French/Italian) with English translation
- Active voice: "This clause excludes liability for intentional fault, which is void under
  OR Art. 100" — not "Liability for intentional fault is excluded, which may have implications"
- Short sentences. One legal point per sentence.
- Name the actor: "The employer must provide..." not "It is required that..."
- Reference the specific OR article: "OR Art. 335c requires a minimum 1-month notice period"

**For internal analysis**:

- Same plain-language standards
- Distinguish mandatory from default provisions explicitly: "This is a mandatory rule
  (zwingend) under OR X — it cannot be modified by agreement"
- Use confidence qualifiers: "This classification is Probable (0.70) — the BGer has not
  ruled definitively on this specific factual pattern"
- Glass Box audit trail appended

**Quality gates before delivery:**

1. Can a business stakeholder understand the executive summary without legal training?
2. Can Swiss opposing counsel understand and respond to each redline?
3. Is every OR article citation specific and correctly referenced?
4. Are mandatory vs. default rules correctly distinguished throughout?
5. Has the Werkvertrag 2026 reform applicability been addressed for any Werkvertrag element?
6. Has the 2020 prescription reform been applied to any limitation period analysis?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 6, search for the current text of relevant OR articles and recent BGer decisions
- Save results to `/tmp/legalcode-ch-or-review.md`
- Verify OR article currency at fedlex.admin.ch (authoritative Swiss law database)
- For RED items, search for BGer decisions applying the mandatory provision in similar contexts
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Mark all OR article and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — verify at fedlex.admin.ch"`
- Focus analysis on structural risk assessment and clear mandatory-rule violations
- Do not create the authority reference file

**Swiss law primary sources (for manual verification):**

- **fedlex.admin.ch** — Official consolidated Swiss federal law database (DE/FR/IT)
- **bger.ch** — Federal Supreme Court decisions (BGer/TF)
- **ch.ch** — Official Swiss portal for practical legal information
- **SR 220** — Obligationenrecht/Code des Obligations (current consolidated text)

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Swiss OR Contract Review

**Document**: [contract name/identifier]
**Parties**: [party names and roles]
**Your Side**: [seller/buyer/employer/employee/contractor/principal/landlord/tenant]
**Contract Type (OR)**: [Kaufvertrag / Werkvertrag / Auftrag / Mietvertrag / Arbeitsvertrag / Mixed]
**Governing Law**: Swiss Law (OR SR 220)
**Cross-Border Elements**: [Yes — IPRG analysis included / No — purely domestic]
**Werkvertrag Reform (2026)**: [Applicable / Not applicable / N/A]
**Prescription Reform (2020)**: [Applicable / N/A]
**Review Basis**: [Playbook name / Swiss market standards]
**Date of Review**: [date]

---

## Key Findings

[Top 3-5 issues with severity flags (RED/YELLOW) and one-line summaries,
including which OR provision is violated or at risk]

---

## Mandatory OR Violations

[Any RED items representing void or voidable provisions under mandatory OR law,
with the specific OR article violated and the consequence — void / voidable / enforceable risk]

---

## Missing Clauses

[List any absent clauses that are material under Swiss OR for this contract type,
with severity assessment]

---

## Clause-by-Clause Analysis

### [Clause Category] — [GREEN / YELLOW / RED] | Confidence: [level]

**Contract says**: [summary of the provision]
**OR standard**: [mandatory rule or market standard]
**Deviation**: [description of gap or violation]
**Legal basis**: [OR Art. X / BGer decision / Swiss market practice]
**Business impact**: [what this means practically]
**Redline** (if YELLOW or RED):

> [Specific proposed language, in contract language where possible]

[Repeat for each clause category]

---

## Contract-Type-Specific Analysis

### [Kaufvertrag / Werkvertrag / Auftrag / Mietvertrag / Arbeitsvertrag]

[Type-specific issues: Rügepflicht (Kaufvertrag), 2026 warranty reform (Werkvertrag),
OR 404 revocability (Auftrag), notice periods (Mietvertrag/Arbeitsvertrag), etc.]

---

## Negotiation Strategy

**Tier 1 (Must-Haves — Mandatory OR Compliance)**: [list]
**Tier 2 (Should-Haves — Material Risk / Market Deviation)**: [list]
**Tier 3 (Concession Candidates)**: [list]

**Recommended approach**: [sequencing, tone, Swiss market practice context]

---

## Stakeholder Impact Map

[Table per Multi-Stakeholder Mapping section]

---

## Next Steps

[Specific actions: qualified Swiss counsel review for RED items, cantonal law analysis
if cantonal issues arise, IPRG analysis for cross-border elements, etc.]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

Switzerland operates under three official legal languages (German/French/Italian) and
26 cantons, each with separate procedural and some substantive variations.

**Language-region considerations:**

| Region                                  | Primary OR Language | Court Language | Key Terminology                                                |
| --------------------------------------- | ------------------- | -------------- | -------------------------------------------------------------- |
| German Switzerland (Deutschschweiz)     | Deutsch             | Deutsch        | Obligationenrecht (OR), Werkvertrag, Kaufvertrag, Auftrag      |
| French Switzerland (Suisse romande)     | Français            | Français       | Code des obligations (CO), contrat d'entreprise, vente, mandat |
| Italian Switzerland (Svizzera italiana) | Italiano            | Italiano       | Codice delle obbligazioni (CO), appalto, vendita, mandato      |

**Cross-language contracts:**

- Where a contract is executed in multiple language versions, identify the authoritative version
- Absent a governing-language clause, Swiss courts determine the authoritative version based on
  the surrounding circumstances and the parties' common intent

**Cantonal differences:**

- Notarization requirements, court structures, and cantonal taxes vary significantly by canton
- For real estate, inheritance, matrimonial property, and corporate registration, engage
  `legalcode-ch-cantonal-law-navigator` for canton-specific analysis
- Labour courts (Arbeitsgericht / Tribunal des prud'hommes) exist only in certain cantons
  (ZH, BE, GE, VD) — other cantons use ordinary courts for employment disputes

**IPRG cross-border signals:**
Flag the following for IPRG analysis:

- Any party not domiciled in Switzerland
- Performance outside Switzerland
- Foreign governing law selected despite Swiss parties
- Employee or consumer domiciled outside Switzerland

---

## Provenance

Created by Legalcode (2026-03-21). Legalcode original synthesis. Research basis: Federal Code
of Obligations (OR SR 220), Swiss Civil Code (ZGB SR 210), Federal Act on Private International
Law (IPRG SR 291), Debt Collection and Bankruptcy Act (SchKG SR 281.1), Unfair Competition Act
(UWG SR 241), Revised Federal Data Protection Act (nDSG SR 235.1, effective 1 September 2023).
Key BGer decisions incorporated: BGer 4A_372/2022 (unusual clause rule B2B), BGer 4A_202/2024 /
4A_212/2024 (non-compete penalty reduction), BGer 4A_666/2024 (licensing exclusivity burden of
proof), BGer 1C_595/2023 (job-related incapacity dismissal). Prescription reform: effective
1 January 2020. Werkvertrag warranty reform: effective 1 January 2026. Research conducted via
agent-team web research pipeline (March 2026). All statutory and case law references marked
[VERIFY] where not independently confirmed against fedlex.admin.ch or bger.ch.
