---
name: legalcode-non-compete-analysis-de
description: Deep-analysis skill for German post-employment non-compete clauses (Nachvertragliches Wettbewerbsverbot)
  governed by HGB §§ 74-75a. Use when reviewing, drafting, or advising on a non-compete agreement in Germany
  for any commercial employee (Handlungsgehilfe), whether as employer or employee.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Deep-analysis skill for German post-employment non-compete clauses (Nachvertragliches Wettbewerbsverbot) governed by HGB §§ 74-75a. Use when reviewing, drafting, or advising on a non-compete agreement in Germany for any commercial employee (Handlungsgehilfe), whether as employer or employee. Covers the full HGB §§ 74-75a statutory framework including mandatory Karenzentschädigung calculation (minimum 50% of last contractual remuneration under § 74), validity classification (verbindlich / unverbindlich / nichtig), the critical employee choice right when a clause is unverbindlich, employer waiver mechanics under § 75 (at termination — no compensation) and § 75a (before termination — 12-month compensation obligation), set-off rules under § 74c (110%/125% thresholds), 2-year temporal maximum, geographic and activity scope reasonableness under § 74a, and the GmbH-Geschäftsführer distinction (§ 138 BGB, not § 74 HGB). Produces VERBINDLICH / UNVERBINDLICH / NICHTIG / WAIVED classification with per-deficiency remediation, confidence-scored analysis, and Glass Box audit trail. Routes from the cross-jurisdictional legalcode-non-compete-analysis skill.


# Legalcode — German Non-Compete Analysis (Nachvertragliches Wettbewerbsverbot)

> **Disclaimer**: This skill provides a framework for AI-assisted analysis of German
> post-employment non-compete law under HGB §§ 74-75a and BGB § 138. It does not
> constitute legal advice (Rechtsberatung) and does not substitute for advice from a
> Rechtsanwalt or Fachanwalt für Arbeitsrecht licensed in Germany. German employment law
> is highly fact-specific; the Bundesarbeitsgericht (BAG) issues continuous refinements,
> and individual circumstances always affect outcomes. Statutory citations and case
> references herein carry hallucination risk — verify against gesetze-im-internet.de and
> bundesarbeitsgericht.de before relying on them. Laws change; verify current applicability
> before acting on any provision described here.

---

## Purpose and Scope

This skill performs deep enforceability analysis of German post-employment non-compete
agreements (nachvertragliche Wettbewerbsverbote) under the HGB §§ 74-75a statutory scheme.
It operates as the Germany-specific deep-analysis route from the cross-jurisdictional
`legalcode-non-compete-analysis` router skill.

**Covers:**

- Full HGB §§ 74-75a compliance assessment (written form, Karenzentschädigung, scope)
- Validity classification: VERBINDLICH / UNVERBINDLICH / NICHTIG / WAIVED
- Karenzentschädigung calculation including variable remuneration under § 74b
- Set-off calculation under § 74c (110%/125% thresholds, employee disclosure obligations)
- Employer waiver mechanics: § 75 (termination, no pay) vs. § 75a (before termination, 12-month obligation)
- GmbH-Geschäftsführer distinction and BGB § 138 analysis
- Employee choice rights when clause is unverbindlich
- Scope reasonableness analysis: temporal (2-year max), geographic, activity-based
- Contractual penalty (Vertragsstrafe) clause validity
- Interaction with employment termination type (ordinary/extraordinary, Aufhebungsvertrag)
- BAG leading case law application (RSU exclusion, salvatorische Klausel, rescission)

**Does not:**

- Analyse non-competes in business-sale (Unternehmenskauf) contexts — different standard
  under BGB § 138 applies; note this and advise separate counsel
- Review non-solicitation of customers or employees (standalone covenants) in isolation
  — see `legalcode-employment-agreement-review` for full employment agreement analysis
- Cover non-compete obligations during employment (in-employment restrictions governed
  by BGB duty of loyalty, not HGB §§ 74-75a)
- Substitute for works council consultation where applicable (see
  `legalcode-de-betriebsrat-consultation`)
- Provide individual legal advice or guarantee court outcomes

**Related skills:**

- `legalcode-non-compete-analysis` — Cross-jurisdictional router (entry point)
- `legalcode-de-kuendigungsschutz` — Dismissal protection (KSchG) — interacts with
  termination type that triggers the non-compete period
- `legalcode-de-gmbh-formation` — GmbH formation and Geschäftsführervertrag provisions
- `legalcode-employment-agreement-review` — Full employment agreement clause review
- `arbeitsvertrag-employment-agreement-de` — German employment contract drafting

---

## Jurisdiction and Governing Law

**Germany only.** This skill applies German federal law. HGB §§ 74-75a are mandatory
employment law provisions — they **override any contractual choice of law** when the
employee primarily works in Germany. A clause stating "governed by English law" or "Swiss
law" cannot avoid HGB requirements if the employee is based in Germany.

| Statute                            | Abbreviation | Relevance                                            |
| ---------------------------------- | ------------ | ---------------------------------------------------- |
| Handelsgesetzbuch §§ 74-75d        | HGB          | Core non-compete framework for Handlungsgehilfen     |
| Bürgerliches Gesetzbuch § 138      | BGB          | Applies to GmbH-Geschäftsführer (unconscionability)  |
| Bürgerliches Gesetzbuch §§ 305-310 | BGB          | AGB-Kontrolle (standard terms review)                |
| Bürgerliches Gesetzbuch § 323      | BGB          | Employee right to rescind for employer's non-payment |
| Bürgerliches Gesetzbuch § 126      | BGB          | Schriftform (written form requirement)               |
| Zivilprozessordnung § 935          | ZPO          | Einstweilige Verfügung (injunction) for enforcement  |

**Key court**: Bundesarbeitsgericht (BAG) — decisions at bundesarbeitsgericht.de.
For Geschäftsführer: Bundesgerichtshof (BGH) — decisions at bundesgerichtshof.de.
All statutory text: gesetze-im-internet.de. Mark uncertain interpretations **[VERIFY]**.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer changes which legal framework applies (HGB vs. BGB § 138)
- Perspective (employer vs. employee) produces materially different outputs
- Clause terms are ambiguous and the analysis forks based on resolution
- Remediation options depend on the user's goals (enforce vs. exit vs. draft)

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

### Step 1: Accept the Clause or Agreement

Accept the non-compete provision in any of these formats:

- **Full agreement**: Employment contract (Arbeitsvertrag), executive service agreement
  (Geschäftsführerdienstvertrag), standalone non-compete agreement, or severance
  agreement (Aufhebungsvertrag) — paste full text or provide file path
- **Clause extract**: The Wettbewerbsverbot provision extracted from a larger document
- **Summary of terms**: Key terms described verbally (duration, geography, activity
  restriction, compensation amount, waiver provisions)

If only a summary is provided, note that the analysis is based on described terms and
full enforceability assessment requires reviewing the actual clause language.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask (skip questions already answered):

1. **Employee status**: What is the employee's role?
   - Options: Handlungsgehilfe (commercial employee — HGB §§ 74-75a applies),
     GmbH-Geschäftsführer (managing director — BGB § 138 applies),
     Other / unclear (help me determine)
   - _Why this matters_: The entire legal framework and mandatory requirements change
     based on status. A Geschäftsführer has no right to mandatory 50% Karenzentschädigung.

2. **Perspective**: Whose interests should the analysis serve?
   - Options: Employer (drafting or enforcement strategy), Employee (challenge or
     exit planning), In-house counsel (balanced risk assessment), HR / People Operations
     (compliance review of existing agreements)
   - _Why this matters_: Employer perspective focuses on enforceability and scope;
     employee perspective focuses on exit rights and compensation claims.

3. **Situation**: What triggered this analysis?
   - Options: Reviewing a new agreement before signing, Reviewing an existing agreement
     before termination, Post-termination dispute (employer seeking to enforce),
     Post-termination dispute (employee seeking to challenge), Drafting a new agreement,
     M&A due diligence (employee population review)
   - _Why this matters_: Pre-signing review focuses on drafting fixes; post-termination
     analysis focuses on enforcement risk and employee rights.

4. **Compensation details** (if not in the document):
   - Last base salary (Grundgehalt) per month
   - Variable components: commissions (Provisionen), bonuses (Boni), profit sharing,
     company car, other benefits
   - Any RSUs or stock options — and whether granted by the employer or a parent/affiliate
   - _Why this matters_: Karenzentschädigung calculation depends on all "vertragsgemäße
     Leistungen" — omitting variable compensation is the most common employer error.

5. **Termination type** (if employment has ended or notice has been given):
   - Options: Employer-initiated ordinary notice (ordentliche Kündigung),
     Employee-initiated resignation (eigene Kündigung), Mutual termination agreement
     (Aufhebungsvertrag), Extraordinary dismissal (außerordentliche Kündigung),
     Still employed (no termination yet)
   - _Why this matters_: Extraordinary termination by the employee for cause may entitle
     the employee to walk away from the non-compete under § 75 HGB.

If the user provides partial context, proceed with what is available and **state
assumptions explicitly** before the analysis.

### Step 3: Identify the Applicable Legal Framework

**3a. Handlungsgehilfe or Geschäftsführer?**

Apply this decision tree:

```
Is the subject a GmbH-Geschäftsführer (organ of the company)?
├── YES → BGB § 138 framework applies (see Step 5-GF below)
│         No mandatory Karenzentschädigung
│         Reasonableness under public policy test
│         BGH, not BAG, is the key court
└── NO  → HGB §§ 74-75a framework applies
          Is the subject a "Handlungsgehilfe" (commercial employee)?
          ├── YES (most salaried employees qualify) → Full §§ 74-75a analysis
          └── UNCLEAR → Check: Does the employee perform commercial/clerical activities
                        in a trade or commercial enterprise? If yes → Handlungsgehilfe.
                        Other employees (factory workers, etc.) → HGB applies by analogy
                        or via contractual incorporation [VERIFY scope of § 75d HGB]
```

**⟁ CLARIFY** — If the subject is a managing director with characteristics of an employee
(strong hierarchical integration, limited personal decision-making authority):

- "This person holds the title of Geschäftsführer but appears to have significant
  employment characteristics. Should I analyse under (a) BGB § 138 only, (b) HGB § 74
  by analogy as an employee-like Geschäftsführer (arbeitnehmerähnliche Stellung), or
  (c) both frameworks for a complete picture?"

**3b. Choice-of-Law Override Check**

If the agreement states a non-German governing law:

- Flag this immediately — German mandatory employment law (HGB §§ 74-75a) applies
  regardless of the choice-of-law clause when the employee is based in Germany
- Note the discrepancy and proceed under German law for the HGB analysis

### Step 4: Gather Legal Authority

Use **legalcode-mcp** if connected to retrieve current statutory text and recent BAG
decisions for this analysis.

**Key searches:**

- HGB § 74, § 74a, § 74b, § 74c, § 75, § 75a, § 75d — current statutory text
- Recent BAG decisions on Karenzentschädigung calculation (especially RSU/equity cases)
- BGB § 138 GmbH-Geschäftsführer non-compete case law (BGH decisions)
- BAG decisions on unverbindlich vs. nichtig line

Save results to `/tmp/legalcode-de-noncompete-authority.md`.

**If legalcode-mcp is not connected:**

- Mark all statutory and case citations with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed using the legal framework documented in this skill, which is based on
  verified research as of March 2026

### Step 5: Enforceability Analysis

#### For Handlungsgehilfen: HGB §§ 74-75a Analysis

Apply the following seven-checkpoint framework. For each checkpoint, determine whether
the clause PASSES, is DEFICIENT, or FAILS. At the end, assign the overall classification.

---

**Checkpoint 1: Written Form (§ 74 Abs. 1 HGB)**

| Requirement                           | Pass                    | Deficient           | Fail                     |
| ------------------------------------- | ----------------------- | ------------------- | ------------------------ |
| Non-compete is in writing             | ✓ Written               | —                   | Not in writing           |
| Employee's signature present          | ✓ Both parties signed   | Signature unclear   | Employee did not sign    |
| Signed original delivered to employee | ✓ Confirmed             | Unclear             | PDF only / not delivered |
| Schriftform under § 126 BGB met       | ✓ Wet-ink or equivalent | Electronic sig only | No physical signature    |

**Result of failure**: Clause is **NICHTIG** (void). Electronic signatures (DocuSign, PDF,
email) do **not** satisfy § 126 BGB Schriftform for non-compete agreements. A non-compete
that was never signed by the employee or delivered as a signed original does not exist.

---

**Checkpoint 2: Karenzentschädigung — Existence (§ 74 Abs. 2 HGB)**

| Requirement                                          | Pass                  | Deficient       | Fail             |
| ---------------------------------------------------- | --------------------- | --------------- | ---------------- |
| Compensation clause present                          | ✓ Explicitly promised | Unclear / vague | Entirely absent  |
| Amount at least 50% of last contractual remuneration | ✓ ≥ 50% stated        | Below 50%       | No amount stated |
| Not left to employer's sole discretion               | ✓ Fixed amount        | Discretionary   | Left to employer |

**Result of failure**:

- **No compensation clause at all** → Clause is **NICHTIG** (BAG 10 AZR 448/15: a
  salvatorische Klausel cannot cure a missing compensation commitment)
- **Compensation stated but below 50%** → Clause is **UNVERBINDLICH** (employee may
  choose to comply and demand statutory 50% minimum, or ignore the clause entirely)

---

**Checkpoint 3: Karenzentschädigung — Calculation Accuracy (§§ 74 Abs. 2, 74b HGB)**

Calculate whether the stated Karenzentschädigung amount actually meets the 50% minimum:

**Step 3a: Identify all "vertragsgemäße Leistungen" (contractual remuneration)**

| Included                                            | Excluded (BAG case law)                                       |
| --------------------------------------------------- | ------------------------------------------------------------- |
| Base salary (Grundgehalt)                           | RSUs / stock options from parent/affiliate (BAG 8 AZR 453/21) |
| Contractually agreed commissions (Provisionen)      | Benefits granted by third parties                             |
| Regular bonuses and gratuities                      | Conditional future payments not yet earned                    |
| Profit participation (Gewinnbeteiligung)            | Statutory public benefits                                     |
| Monetary value of company car (private use portion) | Expense reimbursements                                        |
| Meal allowances (if contractually agreed)           |                                                               |
| Housing benefits (if contractually agreed)          |                                                               |

**Step 3b: Calculate base for variable compensation (§ 74b HGB)**

If remuneration includes commissions or other variable elements:

- Use the **3-year average** (36 months immediately before termination)
- If variable element existed less than 3 years, average only the period of existence
- This average becomes the "last contractual remuneration" for 50% calculation

**Karenzentschädigung minimum formula:**

```
Monthly minimum = (Annual contractual remuneration × 50%) ÷ 12
Annual contractual remuneration = Base salary + 3-year average of variable components
                                  + monetary value of non-cash benefits
```

**⟁ CLARIFY** — If variable compensation is material (>10% of total package), ask:

- "What were the employee's annual earnings including all variable components for the
  last 3 years? This is needed to calculate the accurate Karenzentschädigung minimum."
- "Did the employee receive RSUs or stock options from a parent company or affiliate?
  If so, were they contractually guaranteed by the employing entity itself?"

---

**Checkpoint 4: Temporal Scope (§ 74a Abs. 1 HGB)**

| Requirement                                          | Pass              | Deficient | Fail             |
| ---------------------------------------------------- | ----------------- | --------- | ---------------- |
| Duration ≤ 2 years                                   | ✓ ≤ 24 months     | —         | > 24 months      |
| Duration measured from end of employment, not notice | ✓ Correct trigger | Unclear   | From notice date |

**Result of failure**: A duration exceeding 2 years renders the clause **UNVERBINDLICH**
as to the excess period. German courts generally treat the entire clause as unverbindlich
when the temporal scope makes the overall restriction unreasonable in context — they do
not automatically reduce the period to 2 years. The employee may choose to ignore the
restriction entirely or comply for up to 2 years and demand compensation.

---

**Checkpoint 5: Geographic and Activity Scope (§ 74a Abs. 1 HGB)**

Assess whether the scope is **reasonable and proportionate** to protect a **legitimate
business interest** of the employer (berechtigtes geschäftliches Interesse).

**Geographic scope analysis:**

| Scope                                         | Likely PASS                                      | Likely UNVERBINDLICH       |
| --------------------------------------------- | ------------------------------------------------ | -------------------------- |
| Limited to employee's actual territory        | ✓ Tailored                                       | —                          |
| Nationwide (Germany) for senior national role | ✓ Possible                                       | Regional role → overreach  |
| EU-wide                                       | Only if employee operated EU-wide                | Narrow scope employee      |
| Global                                        | Only for C-suite with true global responsibility | Most employees             |
| "Worldwide" with no carve-outs                | Rarely justified                                 | Presumptively overreaching |

**Activity scope analysis:**

| Scope                                                               | Likely PASS     | Likely UNVERBINDLICH          |
| ------------------------------------------------------------------- | --------------- | ----------------------------- |
| Restricted to direct competitors in employee's product area         | ✓ Proportionate | —                             |
| Restricted to the employer's industry segment where employee worked | ✓ Possible      |                               |
| Any work "for a competitor" (undefined)                             | —               | Overbroad unless well-defined |
| Any work in the employer's broader sector                           | —               | Usually overreaching          |
| Any work that might harm the employer's interests                   | —               | Far too broad                 |

**Legitimate business interest (berechtigtes Interesse) checklist:**

- [ ] Employee had access to trade secrets, customer lists, or confidential pricing
- [ ] Employee had direct customer/supplier relationships the employer seeks to protect
- [ ] Employee had specialized knowledge that would give a competitor material advantage
- [ ] The restriction is tailored to the specific competitive threat from this employee

**Result of failure**: Geographic or activity overreach renders the clause **UNVERBINDLICH**.
There is no partial enforcement for overreaching scope — the clause becomes unverbindlich
as a whole. [VERIFY: some lower courts have taken a more nuanced view on partial scope
reduction in specific circumstances.]

---

**Checkpoint 6: Employer Waiver Status (§§ 75, 75a HGB)**

Check whether the employer has waived the right to enforce the non-compete:

| Scenario                                          | Legal Effect                                                                                                                                       |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| § 75: Waiver declared **at or after** termination | Non-compete ceases immediately; no Karenzentschädigung owed for post-employment period → **WAIVED**                                                |
| § 75a: Waiver declared **before** employment ends | Non-compete will cease; employer must pay Karenzentschädigung for 12 months from date of waiver declaration → **WAIVED (pending 12-month period)** |
| No waiver declared                                | Non-compete remains as-is; continue with other checkpoints                                                                                         |

**⟁ CLARIFY** — If any waiver language appears in the agreement, termination letter,
or communications:

- "I found language that may constitute a waiver of the non-compete. Can you confirm
  whether this was a § 75 waiver (at termination) or § 75a waiver (before termination)?
  This determines whether the employer owes 12 months of compensation."

---

**Checkpoint 7: Payment Compliance and Employee Rights to Rescind (§§ 74c, 323 BGB)**

If the non-compete period has already started:

**7a. Set-off calculation under § 74c HGB:**

```
If: Karenzentschädigung + Other monthly earnings > 110% of last monthly gross salary
Then: Deduct the excess from Karenzentschädigung
Else: Employee receives full Karenzentschädigung

Exception (relocation): If employee had to relocate due to non-compete:
  Threshold increases from 110% to 125%
```

**"Other earnings" subject to set-off:**

- All employment income from any new employer
- Self-employment income
- Consulting fees and freelance income
- Variable compensation (commissions, bonuses) accrued during the period

**Not subject to set-off:**

- Unemployment insurance (Arbeitslosengeld) [VERIFY current BAG position]
- Social welfare payments
- Passive investment income (interest, dividends) in most interpretations

**Employee disclosure obligation**: Employee must disclose other earnings on request.
Failure to disclose permits employer to suspend Karenzentschädigung payments.

**7b. Employer non-payment consequences:**

If employer has not paid Karenzentschädigung as promised:

- Employee has the right to **rescind the non-compete agreement** (BGB § 323, confirmed
  in BAG 10 AZR 392/17)
- Rescission is retroactive — the employee is freed from the restriction from the date
  of the breach
- Employee may also claim damages for the period of non-payment
- **Critical**: An employer cannot seek damages for breach of non-compete if the employer
  itself has not paid the promised Karenzentschädigung

---

#### For GmbH-Geschäftsführer: BGB § 138 Analysis

HGB §§ 74-75a do **not** apply to GmbH managing directors (Organs). The applicable
framework is BGB § 138 Abs. 1 (unconscionability / public policy).

**BGB § 138 Non-Compete Validity Test for Geschäftsführer:**

A non-compete with a Geschäftsführer is **void (nichtig)** if it:

1. **Does not serve a legitimate business interest** of the GmbH:
   - Protectable interest must be genuine — trade secrets, customer relationships,
     specialized market knowledge
   - A Geschäftsführer who is essentially an executor of others' decisions has fewer
     protectable interests associated with their position

2. **Unreasonably impairs the Geschäftsführer's professional freedom** in terms of:
   - **Place (Ort)**: Is the geographic restriction proportionate to the GmbH's actual market?
   - **Time (Zeit)**: Duration must be proportionate — up to 2 years is typically acceptable
     [VERIFY: BGH has not set a hard statutory maximum unlike § 74a HGB for employees];
     some BGH decisions have accepted longer periods in Unternehmenskauf contexts
   - **Subject matter (Gegenstand)**: Must be limited to activities the Geschäftsführer
     was actually involved in

**Key distinctions from HGB § 74 framework:**

| Aspect                           | Handlungsgehilfe (§ 74 HGB)            | GmbH-Geschäftsführer (§ 138 BGB)                             |
| -------------------------------- | -------------------------------------- | ------------------------------------------------------------ |
| Mandatory compensation           | Yes — 50% minimum                      | No — compensation is not required for validity               |
| Written form                     | Strictly required — NICHTIG without it | Strongly recommended but not formally mandatory for validity |
| 2-year maximum                   | Yes — § 74a hard cap                   | No hard statutory cap; reasonableness test                   |
| Validity outcome if overreaching | UNVERBINDLICH (employee can choose)    | NICHTIG (entirely void)                                      |
| Key court                        | Bundesarbeitsgericht (BAG)             | Bundesgerichtshof (BGH)                                      |

**Employee-like Geschäftsführer (arbeitnehmerähnliche Stellung):**

If the Geschäftsführer demonstrates strong employee characteristics:

- Significant hierarchical subordination (e.g., reporting to a supervisory board or
  parent company management)
- Limited personal decision-making authority
- De facto integration into the company's organizational structure as an employee

→ Courts may apply HGB § 74 requirements **by analogy**, including mandatory
Karenzentschädigung. This is a fact-specific assessment.

**⟁ CLARIFY** — If the subject is a Fremdgeschäftsführer (non-shareholder managing
director):

- "Is there any indication that this person operated with employee-like characteristics
  (strong hierarchical subordination, limited personal discretion)? If yes, I can analyse
  whether an analogous application of § 74 HGB is arguable."

---

### Step 6: Overall Enforceability Classification

After completing the applicable checkpoints, assign the overall classification:

| Classification    | Definition                                                                                                  | Legal Consequence                                                                                                                                             |
| ----------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **VERBINDLICH**   | All HGB §§ 74-75a requirements met; clause is binding                                                       | Employee must comply; employer must pay Karenzentschädigung monthly; breach by employee → damages; breach by employer → employee can rescind                  |
| **UNVERBINDLICH** | Deficiency in compensation level, scope, or reasonableness — but not a fundamental form or existence defect | Employee can (a) ignore clause and compete freely, or (b) comply and demand statutory 50% minimum Karenzentschädigung — employee's choice                     |
| **NICHTIG**       | No written form, no compensation clause at all, or fundamental statutory defect                             | Clause does not legally exist; no obligations on either side; no compensation owed; employer cannot enforce; employee cannot claim compensation for complying |
| **WAIVED**        | Employer has declared § 75 or § 75a waiver                                                                  | Non-compete no longer applies; compensation obligations depend on timing (§ 75 = none; § 75a = 12 months from waiver date)                                    |
| **GF-VOID**       | Geschäftsführer non-compete fails BGB § 138 test                                                            | Clause void under public policy; employer cannot enforce; no compensation required                                                                            |
| **GF-VALID**      | Geschäftsführer non-compete meets BGB § 138 reasonableness                                                  | Clause enforceable; compensation not mandatory but recommended for proportionality                                                                            |

**Multiple deficiencies**: When more than one deficiency is present, apply the most
severe classification. NICHTIG > UNVERBINDLICH > VERBINDLICH.

---

### Step 7: Remediation and Actionable Output

For each deficiency identified in Step 5, provide:

1. **What is wrong** (specific statutory basis)
2. **The legal consequence** (NICHTIG / UNVERBINDLICH)
3. **Remediation options** (employer vs. employee perspective)
4. **Draft language** (for fixing the deficiency if pre-signature, or for correspondence if post-termination)

#### Remediation Guidance by Deficiency Type

**Missing or inadequate Karenzentschädigung (→ NICHTIG if absent; UNVERBINDLICH if below 50%)**

_Employer perspective (pre-signature):_

- Calculate the correct minimum based on all vertragsgemäße Leistungen
- Add explicit monthly payment clause: "The Employer shall pay Karenzentschädigung of
  €X per month during the restriction period, payable on the last business day of each
  calendar month."
- Specify the variable compensation averaging methodology for § 74b compliance
- Do NOT rely on a salvatorische Klausel to cure a missing compensation commitment

_Employee perspective (post-termination, clause is UNVERBINDLICH):_

- Employee may send written notice: "The non-compete agreement is unverbindlich due to
  insufficient Karenzentschädigung. I hereby elect to comply with the restrictions and
  demand payment of the statutory minimum of €X per month from [termination date]. Absent
  written confirmation of payment by [date], I will exercise my right to treat the clause
  as non-binding and engage in unrestricted competitive activity."

**Temporal scope exceeding 2 years (→ UNVERBINDLICH)**

_Employer perspective:_

- Reduce period to a maximum of 24 months
- Specify the trigger: "beginning on the date the employment relationship ends"

_Employee perspective:_

- Assert unverbindlich status and exercise election (comply + demand compensation, or
  compete freely)

**Geographic or activity overreach (→ UNVERBINDLICH)**

_Employer perspective:_

- Narrow geographic scope to territories where employee actually worked or had
  customer relationships
- Narrow activity scope to direct competitors in the specific product/service area
  the employee was responsible for
- Document the legitimate business interest being protected

_Employee perspective:_

- Assert unverbindlich status based on overreach
- Be prepared to identify the legitimate scope an employer might argue for (courts
  will assess reasonableness based on the actual employment context)

**Written form deficiency (→ NICHTIG)**

_Employer perspective (pre-signing):_

- Execute a new non-compete agreement with wet-ink signatures on a physical document
- Ensure the employee receives an original signed copy
- Do NOT use DocuSign or PDF signature for HGB § 74 non-compete agreements
- Consider executing as a separate standalone document for clarity

_Post-termination (clause already NICHTIG):_

- If employment continues, execute a new compliant agreement (adequate consideration
  required — a standalone promise or pay increase may be needed)
- If employment has ended, a new post-termination non-compete can only be agreed if
  the employee accepts it (requires fresh consideration/Karenzentschädigung)

---

### Step 8: Apply Quality Frameworks

#### Citation Quality Gates

Run all five gates silently before delivering output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                            | Fail Action                         |
| -------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Source**     | Every legal claim cites a specific HGB section, BAG decision, or BGB provision                  | Add citation or mark "[UNVERIFIED]" |
| **Format**     | All citations follow German legal citation format (e.g., "BAG 10 AZR 448/15")                   | Fix format                          |
| **Currency**   | Every cited provision checked for amendments; BAG decisions verified at bundesarbeitsgericht.de | Flag "[CHECK CURRENCY]"             |
| **Domain**     | Analysis stays within German law; no Common Law or non-German concepts stated as applicable     | Remove or flag                      |
| **Confidence** | Uncertainty explicitly stated; no overconfident assertions about contested points               | Add confidence qualifier            |

#### Self-Interrogation for NICHTIG and Highly Adverse Findings

For any item classified as **NICHTIG** or any finding with Confidence below 0.70, apply
this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the NICHTIG classification follow directly from
the cited HGB provision? Is the statutory text clear, or is there room for interpretation?
For example: is the lack of written form an absolute defect, or could a court find
substantial compliance?

**Pass 2 — Completeness**: Have all relevant BAG decisions been considered? Has the
unverbindlich vs. nichtig distinction been correctly applied? Is there any argument that
a deficiency makes the clause merely unverbindlich rather than nichtig?

**Pass 3 — Challenge**: What is the strongest argument the opposing party would make?
For example: would the employer argue a different calculation of vertragsgemäße Leistungen?
Would the employee argue that the scope is reasonable given their actual duties?

#### Confidence Scoring

| Level        | Range     | Meaning                               | Action                                         |
| ------------ | --------- | ------------------------------------- | ---------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled BAG law, clear statute        | State with confidence                          |
| **High**     | 0.80-0.94 | Strong authority, minor edge cases    | State with brief caveat                        |
| **Probable** | 0.60-0.79 | Good arguments but court could differ | State with reasoning and contra-indicators     |
| **Possible** | 0.40-0.59 | Genuinely contested legal point       | Flag for Fachanwalt review; present both sides |
| **Unlikely** | 0.0-0.39  | Weak basis, speculation               | Do not assert; flag "[UNCERTAIN]"              |

---

## Enforceability Classification Reference

| Outcome            | German Term        | Trigger                                                     | Employee Rights                                                                   | Employer Rights                                                               |
| ------------------ | ------------------ | ----------------------------------------------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **VERBINDLICH**    | Bindend            | All §§ 74-75a requirements met                              | Receive Karenzentschädigung monthly; rescind if employer doesn't pay              | Enforce restriction; claim damages for breach                                 |
| **UNVERBINDLICH**  | Nicht bindend      | Compensation below 50%; scope overreach; excess duration    | Choose: (a) compete freely, no compensation; OR (b) comply and demand 50% minimum | Cannot enforce if employee ignores; must pay 50% if employee elects to comply |
| **NICHTIG**        | Nichtig            | No written form; no compensation clause; fundamental defect | Compete freely; cannot claim compensation for compliance                          | Cannot enforce; no damages claim                                              |
| **WAIVED (§ 75)**  | Verzichtet (§ 75)  | Employer waives at/after termination                        | Immediately free to compete                                                       | No Karenzentschädigung owed for post-employment period                        |
| **WAIVED (§ 75a)** | Verzichtet (§ 75a) | Employer waives before employment ends                      | Free to compete; receives 12 months' Karenzentschädigung from waiver date         | Owes 12 months Karenzentschädigung from waiver date; then released            |

---

## Prioritization Framework

After completing the analysis, prioritize findings for action:

### Tier 1 — Immediate Action (Critical)

_These issues create the highest legal risk or most immediate harm:_

- NICHTIG classification (no enforceable agreement exists — employer must decide whether
  to attempt a new agreement, if possible)
- Employer failure to pay Karenzentschädigung (employee can rescind — time-sensitive)
- Misclassification of Geschäftsführer as subject to HGB § 74 (wrong legal standard applied)
- Written form deficiency discovered before termination (fixable with a new agreement)
- Compensation calculation using wrong base (risk of unverbindlich or employee election)

### Tier 2 — Material (Address Before Finalizing or Before Termination)

_These issues create enforceability risk that should be resolved:_

- UNVERBINDLICH classification due to inadequate compensation amount
- Geographic scope overreach (employee can ignore the clause)
- Activity scope overreach (especially if it covers the employee's primary career path)
- Duration at or near the 2-year maximum (consider whether shorter is more defensible)
- Missing § 74c set-off clause (employer may be paying more than required)
- Ambiguous waiver provisions that could be misread as § 75 or § 75a waivers

### Tier 3 — Advisory (Good Practice, Not Legally Required)

_These issues are good practice but do not affect immediate enforceability:_

- Variable compensation calculation methodology not spelled out (§ 74b compliance unclear)
- No Vertragsstrafe (contractual penalty) clause for breach
- No employee acknowledgment of receipt of the signed original
- Unclear trigger date for the non-compete period
- No provision addressing employer bankruptcy or change of control
- No mechanism for mutual agreement to reduce the non-compete period post-termination

---

## Karenzentschädigung Calculation Reference

### Step-by-Step Calculation

**1. Identify all vertragsgemäße Leistungen (last 12 months):**

| Component                                        | Amount       | Include?                       |
| ------------------------------------------------ | ------------ | ------------------------------ |
| Monthly base salary                              | €**\_** × 12 | ✓ Yes                          |
| Annual bonus (contractually guaranteed)          | €**\_**      | ✓ Yes                          |
| Commissions (3-year average under § 74b)         | €**\_**      | ✓ Yes                          |
| Company car (private use value, e.g., 1% rule)   | €**\_** × 12 | ✓ Yes                          |
| Meal or housing allowance (contractually agreed) | €**\_**      | ✓ Yes                          |
| RSUs from parent/affiliate company               | €**\_**      | ✗ No (BAG 8 AZR 453/21)        |
| Expense reimbursements                           | €**\_**      | ✗ No                           |
| Employer pension contributions                   | €**\_**      | [VERIFY — case law developing] |

**2. Annual contractual remuneration base:** €**\_** per year

**3. Monthly minimum Karenzentschädigung:** (Annual base × 50%) ÷ 12 = €**\_** per month

**4. Set-off check (§ 74c) — apply monthly during non-compete period:**

- Employee's new monthly income: €**\_**
- Karenzentschädigung before set-off: €**\_**
- Sum: €**\_**
- 110% of last gross monthly salary: €**\_**
- Excess (if any): €**\_** → deduct from Karenzentschädigung
- Actual monthly payment to employee: €**\_**

---

## Glass Box Audit Trail

Every analysis should produce or reference this YAML template:

```yaml
glass_box:
  skill_name: "legalcode-non-compete-analysis-de"
  jurisdiction: "Germany — HGB §§ 74-75a / BGB § 138"
  framework_applied: "HGB §§ 74-75a (Handlungsgehilfe) | BGB § 138 (Geschäftsführer)"
  analysis_date: "[ISO date]"
  perspective: "[employer | employee | neutral]"
  situation: "[pre-signing | pre-termination | post-termination | due-diligence]"
  legalcode_mcp: "[Connected — X results retrieved | Not connected]"
  research_reference_file: "[/tmp/legalcode-de-noncompete-authority.md | Not created]"

  subject_status: "[Handlungsgehilfe | GmbH-Geschäftsführer | Employee-like Geschäftsführer | Unknown]"
  governing_law_stated: "[Law stated in contract | None stated]"
  german_mandatory_law_override: "[Yes — HGB applies regardless | N/A]"

  checkpoints_applied:
    cp1_written_form: "[PASS | FAIL → NICHTIG]"
    cp2_karenz_existence: "[PASS | DEFICIENT → UNVERBINDLICH | FAIL → NICHTIG]"
    cp3_karenz_calculation: "[PASS | DEFICIENT → UNVERBINDLICH | Unable to assess]"
    cp4_temporal_scope: "[PASS | FAIL → UNVERBINDLICH]"
    cp5_geographic_scope: "[PASS | FAIL → UNVERBINDLICH]"
    cp5_activity_scope: "[PASS | FAIL → UNVERBINDLICH]"
    cp6_waiver_status: "[No waiver | WAIVED (§ 75) | WAIVED (§ 75a)]"
    cp7_payment_compliance: "[N/A — pre-termination | COMPLIANT | BREACH → rescission right]"

  overall_classification: "[VERBINDLICH | UNVERBINDLICH | NICHTIG | WAIVED | GF-VOID | GF-VALID]"
  deficiencies_identified: "[number]"
  tier_1_issues: "[number]"
  tier_2_issues: "[number]"
  tier_3_issues: "[number]"

  citations_verified: "[number VERIFIED] / [number UNVERIFIED with [VERIFY] flags]"
  key_bag_cases_applied: "[e.g., BAG 10 AZR 448/15; BAG 8 AZR 453/21; BAG 10 AZR 392/17]"

  confidence: "[HIGH | MEDIUM | LOW] — [rationale]"
  limitations:
    - "[Any assumptions made about undisclosed terms]"
    - "[Any elements that require Fachanwalt für Arbeitsrecht review]"
    - "[Any developments post-March 2026 not captured in this analysis]"
  reviewer: "AI-assisted — requires qualified Fachanwalt für Arbeitsrecht review before acting"
```

---

## Anti-Patterns

The following are the most common errors in German non-compete practice. Do not replicate
any of these when drafting or advising.

1. **Using DocuSign or PDF signatures** — § 126 BGB Schriftform requires wet-ink signature
   on a physical document delivered to the employee. Electronic signatures do not satisfy
   this requirement. This is the most operationally easy defect to avoid and the most
   commonly seen in practice.

2. **Omitting the Karenzentschädigung clause entirely** — "We'll figure it out later" or
   relying on a salvatorische Klausel renders the non-compete NICHTIG (BAG 10 AZR 448/15).
   No compensation commitment at all = void, not unverbindlich.

3. **Calculating Karenzentschädigung on base salary only** — All vertragsgemäße Leistungen
   must be included: commissions, bonuses, car value. Employers underestimate compensation
   by ignoring variable components and benefits, rendering the stated amount below 50%.

4. **Including RSUs from parent companies in the Karenzentschädigung base** — Since BAG
   8 AZR 453/21, RSUs granted by parent or affiliate companies are NOT included. Employees
   cannot demand that these be counted; employers cannot claim them as Karenzentschädigung.

5. **Copying a US- or UK-style non-compete into a German employment contract** — Common
   law "reasonable restraint" language, "garden leave" structures without HGB compliance,
   and missing compensation commitments all produce NICHTIG or UNVERBINDLICH results in
   Germany. Each jurisdiction's non-compete must be drafted from its own legal framework.

6. **Setting a 5-year or perpetual non-compete** — The 2-year cap under § 74a Abs. 1 HGB
   is absolute for Handlungsgehilfen. Any duration above 24 months is unverbindlich.

7. **Applying a Germany-wide non-compete to a regional employee** — An employee who worked
   only in Bavaria and had only Bavarian customer relationships cannot be restricted
   nationwide. Geographic overreach makes the clause unverbindlich.

8. **Prohibiting the employee from working "for any competitor"** — This sweeping activity
   restriction covers far more than necessary and is typically unverbindlich. The restriction
   must be specific to the employee's actual activities and the employer's protectable interests.

9. **Assuming HGB § 74 applies to the GmbH-Geschäftsführer** — It does not. The applicable
   standard is BGB § 138 — no mandatory compensation requirement. Drafting a Geschäftsführer
   non-compete using the HGB § 74 framework wastes mandatory compensation payments that the
   employer is not legally required to make.

10. **Failing to distinguish § 75 from § 75a waivers** — Both are employer waivers but with
    radically different cost implications. § 75 waiver at termination: no compensation owed.
    § 75a waiver before termination: 12 months' Karenzentschädigung still owed. Drafting
    waiver provisions without clarity on timing can create unintended 12-month obligations.

11. **Believing a salvatorische Klausel can save any defective non-compete** — Expressly
    rejected by the BAG (10 AZR 448/15). A severability clause can help in other contract
    contexts, but it cannot create a compensation obligation that was never agreed.

12. **Failing to pay Karenzentschädigung monthly** — § 74c requires monthly payment at the
    end of each calendar month. Paying quarterly, annually, or "when convenient" is a breach
    that gives the employee the right to rescind the non-compete entirely.

13. **Ignoring the employee's § 74c disclosure obligation** — Employers often do not know
    to request disclosure of new earnings, then overpay Karenzentschädigung for years without
    applying the § 74c set-off. Add an explicit obligation for the employee to disclose and
    a mechanism for the employer to adjust payments.

14. **Assuming the employee has no option when the clause is unverbindlich** — The employee's
    choice right is the single most misunderstood aspect of German non-compete law. An
    unverbindlich clause is not void — the employee can elect to comply and extract
    adequate compensation, even if the original agreed amount was inadequate.

15. **Not re-executing a compliant non-compete after the original was found NICHTIG** —
    Once an employment relationship is ongoing, it is still possible to enter a new,
    compliant non-compete agreement with adequate consideration. After termination, a
    post-termination non-compete requires the employee's agreement (cannot be imposed
    unilaterally). Employers who discover a defective non-compete during employment have
    a window to fix it.

16. **Applying German non-compete rules to Austrian or Swiss employees** — Austria and
    Switzerland have their own non-compete frameworks that differ from HGB §§ 74-75a.
    Do not extrapolate German rules to these jurisdictions without separate legal review.

17. **Overlooking interaction with extraordinary dismissal** — If the employee resigns
    for good cause (außerordentlich wichtiger Grund) due to the employer's breach, the
    employee may be released from the non-compete under § 75 HGB analogously. This is
    a complex analysis requiring Fachanwalt review.

18. **Missing the interaction between non-compete and Aufhebungsvertrag** — A termination
    by mutual agreement (Aufhebungsvertrag) can include specific non-compete provisions,
    waivers, or modifications. The parties have more flexibility in an Aufhebungsvertrag
    than in a standard termination. Failing to address the non-compete in the Aufhebungsvertrag
    leaves the existing agreement in full force.

19. **Accepting a clause that provides "voluntary" waiver of Karenzentschädigung** — Per
    § 75d HGB, agreements by the employee to waive the right to Karenzentschädigung are
    void and non-derogable. Any such "waiver" provision inserted by the employer is
    unenforceable — the employee is always entitled to the statutory minimum.

20. **Thinking an industry-specific collective agreement (Tarifvertrag) cannot affect the
    non-compete** — Some Tarifverträge contain specific provisions about post-employment
    restrictions that may supplement or restrict HGB §§ 74-75a rights. Check whether a
    Tarifvertrag applies to the employment relationship.

---

## Writing Standards

Before delivering any output:

**Plain-language discipline:**

- [ ] Use both the German legal term and its English gloss on first reference:
      e.g., "Karenzentschädigung (mandatory non-compete compensation)"
- [ ] Define all technical terms before using them as shorthand
- [ ] Avoid vague risk language ("may cause issues") — state the specific legal consequence
- [ ] Where the law is clear, say so clearly; where it is contested, say so explicitly
- [ ] Active voice throughout: "The employer must pay" not "Payment must be made"

**Structure gates:**

- [ ] Overall classification appears in the first section, not buried at the end
- [ ] Each deficiency is self-contained: what is wrong → why it matters → what to do
- [ ] Confidence scores accompany every contested legal assertion
- [ ] [VERIFY] tags accompany every unverified statutory or case law citation

**German legal conventions:**

- [ ] Use the nominative form for statute names (§ 74 HGB, not "Section 74")
- [ ] BAG case citations follow the format: "BAG [Datum] — [Aktenzeichen]" (e.g., BAG 22.03.2017 — 10 AZR 448/15)
- [ ] Reference gesetze-im-internet.de for statutory verification, bundesarbeitsgericht.de for BAG decisions

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for: "§ 74 HGB Wettbewerbsverbot", "Karenzentschädigung BAG", "nachvertragliches
  Wettbewerbsverbot", "GmbH Geschäftsführer Wettbewerbsverbot § 138 BGB"
- Retrieve current statutory text and verify no recent amendments
- Look for BAG decisions from 2024-2026 that may update the RSU calculation or
  unverbindlich/nichtig line
- Save results to `/tmp/legalcode-de-noncompete-authority.md`
- Mark all retrieved citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case citations in the output with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Direct the user to verify at:
  - gesetze-im-internet.de (statutes)
  - bundesarbeitsgericht.de (BAG decisions)
  - dejure.org (linked case law with HGB commentary)
  - hensche.de/Rechtsanwalt_Arbeitsrecht_Handbuch_Wettbewerbsverbot.html (practitioner reference)

---

## Output Format Template

Produce the analysis in this format:

```markdown
# German Non-Compete Analysis (Nachvertragliches Wettbewerbsverbot)

**Agreement / Clause**: [Name or description of the document]
**Subject**: [Name/role of employee or Geschäftsführer]
**Analysis Date**: [Date]
**Perspective**: [Employer | Employee | Neutral]
**Legal Framework Applied**: [HGB §§ 74-75a | BGB § 138 | Both]

---

## Overall Classification: [VERBINDLICH | UNVERBINDLICH | NICHTIG | WAIVED | GF-VOID | GF-VALID]

> **[One-sentence plain-language summary of the finding and its most important consequence]**

**Confidence**: [Level] ([X.XX]) — [Brief rationale]

---

## Summary of Findings

| #   | Checkpoint                                    | Result                     | Classification Impact            | Priority |
| --- | --------------------------------------------- | -------------------------- | -------------------------------- | -------- |
| 1   | Written Form (§ 74 Abs. 1)                    | [PASS / FAIL]              | [None / NICHTIG]                 | [Tier]   |
| 2   | Karenzentschädigung — Existence (§ 74 Abs. 2) | [PASS / DEFICIENT / FAIL]  | [None / UNVERBINDLICH / NICHTIG] | [Tier]   |
| 3   | Karenzentschädigung — Calculation             | [PASS / DEFICIENT]         | [None / UNVERBINDLICH]           | [Tier]   |
| 4   | Temporal Scope ≤ 2 years (§ 74a Abs. 1)       | [PASS / FAIL]              | [None / UNVERBINDLICH]           | [Tier]   |
| 5   | Geographic Scope — Reasonableness             | [PASS / FAIL]              | [None / UNVERBINDLICH]           | [Tier]   |
| 5b  | Activity Scope — Reasonableness               | [PASS / FAIL]              | [None / UNVERBINDLICH]           | [Tier]   |
| 6   | Employer Waiver Status (§§ 75/75a)            | [No waiver / WAIVED]       | [As applicable]                  | [Tier]   |
| 7   | Payment Compliance / Rescission Risk          | [N/A / COMPLIANT / BREACH] | [As applicable]                  | [Tier]   |

---

## Karenzentschädigung Calculation

**Annual contractual remuneration base**: €[X]
**Components included**: [list]
**Components excluded**: [list with reason]
**Monthly minimum under § 74 Abs. 2**: €[X]
**Stated amount in agreement**: €[X] per month
**Assessment**: [Meets minimum / Below minimum by €X / Cannot assess without further information]

---

## Detailed Findings

### Finding 1: [Checkpoint Name]

**Status**: [PASS | DEFICIENT | FAIL]
**Statutory basis**: [HGB § / BGB §]
**Finding**: [Specific description of what was found in the clause]
**Legal consequence**: [VERBINDLICH | UNVERBINDLICH | NICHTIG — with explanation]
**Confidence**: [Level] ([X.XX])

**Employer remediation**:
[Specific steps; draft language if applicable]

**Employee options**:
[What the employee can do given this finding]

---

[Repeat for each finding]

---

## Priority Action Plan

### Tier 1 — Immediate

- [Action item → Responsible party → Deadline or timing]

### Tier 2 — Material

- [Action item → Responsible party]

### Tier 3 — Advisory

- [Action item]

---

## Glass Box Audit Trail

[Paste the completed YAML from the template above]
```

---

## Localization Notes

This skill covers **German federal law only**. Note these jurisdiction-adjacent points:

- **Austria (Österreich)**: Similar but distinct non-compete framework under AngG
  (Angestelltengesetz); separate analysis required
- **Switzerland (Schweiz)**: OR Art. 340 ff.; different compensation threshold and
  remedies; separate analysis required
- **German-speaking employees in multinational groups**: The mandatory rules of HGB
  §§ 74-75a apply to employees based in Germany regardless of the parent company's
  home jurisdiction or the contract's choice-of-law clause
- **Posted workers**: If an employee is temporarily posted to Germany under the Posted
  Workers Directive, German mandatory employment law may apply during the posting period
  [VERIFY applicable scope for non-compete matters]

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

- HGB §§ 74-75d statutory text (gesetze-im-internet.de)
- BAG leading decisions: 10 AZR 448/15 (salvatorische Klausel); 8 AZR 453/21 (RSU
  exclusion); 10 AZR 392/17 (employee rescission for non-payment)
- BGB § 138 framework for GmbH-Geschäftsführer (BGH and BAG case law)
- Practitioner references: hensche.de, HENSCHE Rechtsanwälte Arbeitsrecht
- 2-agent research pipeline (structural + prompt engineering analysis, March 2026)
- Reference standard: `legalcode-contract-review`, `legalcode-de-kuendigungsschutz`
- Related skill: `legalcode-non-compete-analysis` (cross-jurisdictional router)
