---
name: legalcode-is-contract-law-general
description: Review, draft, and analyse contracts governed by Icelandic law. Covers Act No. 7/1936 on
  Contracts, Agency and Void Legal Acts (samningsgerð, umboð og ógilda löggerninga), freedom of contract
  (samningsfrelsi), Section 36 general fairness clause, standard terms (staðlaðir samningsskilmálar),
  consumer protection (neytendavernd), Sale of Goods Act No. 50/2000, limitation periods under Act No.
  150/2007 (4-year general rule), price indexation (verðtrygging) under Act No. 38/2001, GDPR implementation
  (Act No. 90/2018 — Persónuvernd), and the EEA/EU-aligned consumer acquis including Directives 93/13,
  2011/83, and 2019/771. Use for any commercial agreement, service contract, consumer purchase, software
  licence, employment contract, or other legal instrument governed by Icelandic law. Identifies deviations,
  generates confidence-scored redlines, flags mandatory consumer provisions, and produces an auditable
  Glass Box output.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode — Icelandic Contract Law General Review

> **Disclaimer**: This skill provides a framework for AI-assisted review and analysis of
> contracts governed by Icelandic law. It does not constitute legal advice. All outputs
> must be reviewed by a qualified legal professional (lögfræðingur) licensed to practise
> in Iceland before reliance. Laws change; verify current applicability before acting on
> any provision described here. Statutory and case-law references cited from research
> carry hallucination risk — verify against authoritative Icelandic sources (Alþingi
> database at althingi.is, Stjórnartíðindi, and Hæstiréttur decisions) before relying
> on them.

---

## Purpose and Scope

This skill reviews, analyses, and assists in drafting contracts governed by Icelandic law.
It applies the full framework of Icelandic contract legislation — rooted in Act No. 7/1936
but substantially shaped by EEA-derived consumer acquis — and identifies deviations,
mandatory provisions, and red-flag clauses.

**Covers:**

- Clause-by-clause analysis of any contract governed by Icelandic law
- Consumer vs. commercial distinction and its effect on mandatory provisions
- Section 36 (Act No. 7/1936) general fairness and good-faith review
- Consumer protection compliance: Directives 93/13, 2011/83, 2019/771 as implemented
- Standard terms incorporation and contra proferentem analysis
- Limitation periods under Act No. 150/2007
- Price indexation (verðtrygging) provisions under Act No. 38/2001
- GDPR compliance under Act No. 90/2018 (Persónuvernd)
- CISG applicability (including the Nordic inter-Scandinavian reservation)
- Deviation classification (GREEN / YELLOW / RED)
- Confidence-scored redlines with Icelandic-law basis
- Glass Box audit trail

**Does not:**

- Substitute for qualified Icelandic legal counsel (lögfræðingur)
- Cover family law, succession, or constitutional matters
- Apply to contracts governed by a law other than Icelandic law (use
  jurisdiction-agnostic skill for those)
- Provide binding advice on regulatory authorisations or licences from Seðlabanki
  Íslands, FME (Fjármálaeftirlitið), or other regulatory bodies

---

## Jurisdiction and Governing Law

**Jurisdiction**: Iceland (Republic of Iceland)
**Legal tradition**: Nordic legal tradition — Civil law foundation with strong statutory
consumer protection and EEA obligations. Iceland is NOT an EU member state but is a
full EEA Contracting Party; it implements EU consumer acquis through the EEA Agreement
and EFTA Court oversight.

**Foundational statutes:**

| Act                          | Icelandic title                                  | Scope                                       |
| ---------------------------- | ------------------------------------------------ | ------------------------------------------- |
| Act No. 7/1936               | Lög um samningsgerð, umboð og ógilda löggerninga | General contract law, agency, voidable acts |
| Act No. 50/2000              | Lög um lausafjárkaup                             | Commercial sale of goods (CISG-derived)     |
| Act No. 48/2003              | Lög um neytendakaup                              | Consumer sale of goods                      |
| Act No. 42/2000              | Lög um þjónustukaup                              | Consumer service contracts                  |
| Act No. 16/2001              | Lög um fjarverslun og fjarsölu þjónustu          | Distance selling; 14-day withdrawal         |
| Act No. 150/2007             | Lög um fyrningu kröfuréttinda                    | Limitation periods (claims)                 |
| Act No. 38/2001              | Lög um vexti og verðtryggingu                    | Interest and price indexation               |
| Act No. 30/2002              | Lög um rafræn viðskipti og aðra rafræna þjónustu | Electronic commerce and e-signatures        |
| Act No. 90/2018              | Lög um persónuvernd og vinnslu persónuupplýsinga | GDPR implementation                         |
| Act No. 73/1972 (as amended) | Höfundalög                                       | Copyright (IP provisions in contracts)      |

**EEA consumer acquis implemented in Iceland:**

- Directive 93/13/EEC — Unfair Terms in Consumer Contracts (via Act 7/1936 §36 and consumer acts)
- Directive 2011/83/EU — Consumer Rights (14-day withdrawal, pre-contractual information)
- Directive 2019/771/EU — Sale of Goods (5-year warranty for long-lifespan goods in Iceland)
- Directive 2000/31/EC — Electronic Commerce

**Court hierarchy:**

- Héraðsdómar (District Courts) — first instance
- Landsréttur (Court of Appeal) — created 2018; intermediate appellate court
- Hæstiréttur Íslands (Supreme Court) — final appellate court

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- The consumer / commercial classification is ambiguous
- The governing law clause is absent or in conflict
- Risk tolerance is needed to classify severity correctly

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

### Step 1: Accept the Contract

Accept the contract in any of these formats:

- **File**: PDF, DOCX, or other document
- **URL**: Link to a document system or CLM
- **Pasted text**: Contract text copied directly into the conversation

If no contract is provided, prompt the user to supply one or describe what they need drafted.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user:

1. **Which side are you on?**
   - Options: Seller/Supplier/Service Provider, Buyer/Customer/Consumer, Licensor,
     Licensee, Employer, Employee, Other (describe)
   - _Why it matters_: The entire analysis reverses depending on the user's position.

2. **Consumer or commercial?**
   - Options: Consumer contract (individual not acting in trade or profession),
     B2B commercial contract, Employment contract, Mixed / unclear
   - _Why it matters_: Consumer protections under Icelandic law are mandatory and
     cannot be excluded by contract. Commercial contracts have much wider freedom.

3. **Contract type?**
   - Options: Sale of goods (lausafjárkaup), Service contract (þjónustusamningur),
     Software licence / SaaS, Employment (ráðningarsamningur), Distribution / agency,
     Real property related, Other (describe)
   - _Why it matters_: Different statutes and mandatory provisions apply per type.

4. **Goal of the review?**
   - Options: Full clause-by-clause analysis, Compliance check (consumer / GDPR / EEA),
     Redline drafting for negotiation, Quick red-flag scan, Drafting assistance
   - _Why it matters_: Scopes the depth of the output.

5. **Special concerns?** (multi-select)
   - Price indexation (verðtrygging) provisions
   - Data protection / GDPR compliance (Persónuvernd)
   - IP ownership and copyright (Höfundalög)
   - Limitation of liability and indemnification
   - Consumer withdrawal and return rights
   - CISG exclusion / inclusion (cross-border sale of goods)
   - No specific focus — full review

State any assumptions explicitly if the user provides partial context.

### Step 3: Confirm Governing Law

Read the governing law clause in the contract.

**⟁ CLARIFY** — If any of the following, ask before proceeding:

- **No governing law clause**: Flag as RED (missing mandatory risk) and ask which
  jurisdiction the user expects to govern. Default to Icelandic law if the parties
  are Icelandic and the contract has Icelandic connections.
- **Governing law is not Icelandic**: This skill is Iceland-specific. Inform the user
  and offer to use the jurisdiction-agnostic contract review skill instead, or confirm
  whether to proceed with an Iceland-law analysis anyway.
- **Consumer contract with foreign governing law**: Warn that Icelandic mandatory
  consumer provisions apply regardless of choice of law under EEA/EU private
  international law principles (Rome I Regulation equivalent) [VERIFY current
  Icelandic PIL rules].

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** (if connected) to search for:

- Current text of Act No. 7/1936 and any recent amendments
- Applicable consumer act (Act No. 48/2003, 42/2000, or 16/2001 depending on contract type)
- Act No. 150/2007 (limitation periods)
- Act No. 38/2001 (interest and price indexation) — for any payment provisions
- Act No. 90/2018 (GDPR) — for any data processing provisions
- Recent Hæstiréttur decisions on the contract type being reviewed
- EFTA Court decisions on EEA consumer acquis implementation in Iceland

Save results to `/tmp/legalcode-is-contract-review.md`. Mark legalcode-mcp citations as
VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**

- Mark all statutory and case-law references with [VERIFY]
- Note in the audit trail: `legalcode_mcp: "Not connected — manual verification required"`
- Proceed using the research framework in this skill

### Step 5: Classify Contract Type and Applicable Framework

Based on the context gathered, identify the governing statutory framework:

| Contract Type            | Primary Statute              | Consumer Acts           | Key Mandatory Rules                                                               |
| ------------------------ | ---------------------------- | ----------------------- | --------------------------------------------------------------------------------- |
| Consumer sale of goods   | Act 48/2003 (neytendakaup)   | Act 16/2001 (distance)  | 2-year conformity minimum; 5-year for long-lifespan goods; non-derogable remedies |
| Consumer service         | Act 42/2000 (þjónustukaup)   | Act 16/2001 (distance)  | Service must meet statutory quality; consumer cannot waive remedies               |
| Commercial sale of goods | Act 50/2000 (lausafjárkaup)  | None (B2B)              | CISG-derived; Nordic reservation for Scandinavian parties                         |
| Service contract (B2B)   | Act 7/1936 + trade custom    | None                    | Section 36 fairness review; freedom of contract wide                              |
| Software licence / SaaS  | Act 7/1936 + Act 30/2002     | Act 16/2001 if consumer | Digital content rules; potential consumer right of withdrawal                     |
| Employment               | Act 70/1996 (réttarstaða)    | N/A                     | Collective agreements; mandatory notice periods                                   |
| Agency / distribution    | Act 7/1936 (agency chapters) | N/A                     | Agent authority; apparent authority; del credere                                  |

### Step 6: Clause-by-Clause Analysis

Read the entire contract before flagging issues — clauses interact.

**⟁ CLARIFY** — For long contracts (30+ pages):
Ask whether to perform a **full review** of all clause categories or a **priority scan**
focused on the user's stated concerns plus any RED items found.

Analyse all 15 clause categories below. For each, state whether the clause is present,
absent, or unusual. Apply the GREEN / YELLOW / RED classification (see Severity
Classification section).

| #   | Clause Category                    | Depth    | Key Review Points (Icelandic Law)                                                        |
| --- | ---------------------------------- | -------- | ---------------------------------------------------------------------------------------- |
| 1   | Governing Law & Dispute Resolution | Deep     | Icelandic law confirmed; arbitration vs. courts; Landsréttur / Hæstiréttur               |
| 2   | Limitation of Liability            | Deep     | Cap amount; carveouts; Section 36 fairness review; consumer non-derogable remedies       |
| 3   | Indemnification                    | Deep     | Nordic civil law context (no native "indemnity" concept); scope; mutuality               |
| 4   | Intellectual Property              | Deep     | Höfundalög — no work-for-hire; assignment in writing; inalienable moral rights           |
| 5   | Data Protection                    | Deep     | Act 90/2018 (GDPR); Persónuvernd; DPA requirement; transfer mechanisms                   |
| 6   | Term & Termination                 | Deep     | Statutory termination rights; consumer right of withdrawal; cure periods                 |
| 7   | Price, Payment & Indexation        | Deep     | verðtrygging (price indexation) — unique Icelandic feature; Act 38/2001 default interest |
| 8   | Consumer Protection Compliance     | Deep     | Non-derogable rights; unfair terms; 14-day withdrawal; pre-contractual information       |
| 9   | Confidentiality                    | Standard | Scope; term; permitted disclosures; return obligations                                   |
| 10  | Representations & Warranties       | Standard | Scope; disclaimers; conformity obligations (Act 48/2003 or 50/2000)                      |
| 11  | Force Majeure                      | Standard | Enumerate events; notification; Nordic hardship / changed-circumstances doctrine         |
| 12  | Assignment                         | Standard | Consent requirements; change of control; consumer contract restrictions                  |
| 13  | Compliance & Regulatory            | Standard | Anti-bribery; sanctions; AML/KYC; export controls                                        |
| 14  | Insurance                          | Standard | Coverage types and minimums; certificate delivery                                        |
| 15  | Definitions & Boilerplate          | Standard | Entire agreement; severability; notices; amendments; counterparts                        |

### Step 7: Icelandic-Law Clause Deep Dives

Apply these jurisdiction-specific analytical lenses to the flagged clauses:

#### 7a. Section 36 — General Fairness Review (Act No. 7/1936)

Section 36 of Act No. 7/1936 is the general equity clause of Icelandic contract law.
A contract or clause may be set aside or modified by a court if enforcement would be
**substantially unreasonable** (óhæfilegt) in light of the circumstances, or contrary
to good business practice (góðar viðskiptavenjur).

Apply this lens to every RED item:

- Would enforcement of this clause be "substantially unreasonable" under Icelandic law?
- Is there disproportionality in bargaining power that colours the analysis?
- For standard terms: is this a surprising or onerous clause the other party had no
  reason to expect?

**Consumer contracts**: Section 36 operates alongside the consumer acts. Courts have
used it to void clauses that technically comply with the Acts but are still unfair.

**B2B contracts**: Section 36 still applies but courts afford more latitude to
commercially sophisticated parties who negotiated at arm's length.

#### 7b. Price Indexation (Verðtrygging) — Act No. 38/2001

**This is a uniquely Icelandic feature.** Many Icelandic contracts — especially for
loans, leases, and long-term services — include price indexation tied to the Consumer
Price Index (CPI) or other indices. The purpose is to preserve real value against
inflation.

Review any payment clause for:

- **Presence of verðtrygging**: Is the contract price or principal sum indexed? If so,
  to which index and on what basis?
- **EFTA Court scrutiny**: Icelandic mortgage indexation has been scrutinised under
  Directive 93/13 (unfair terms). In cross-border or consumer contexts, check whether
  indexation is transparent, clearly explained, and not disproportionate. [VERIFY
  current EFTA Court jurisprudence on mortgage indexation cases]
- **Default interest (dráttarvextir)**: Act No. 38/2001 sets the default interest rate
  for overdue sums (central bank rate + margin; Seðlabanki Íslands announces the rate
  periodically). Contracts may specify a higher rate; consumers cannot be subjected to
  punitive interest beyond statutory norms [VERIFY].
- **RED flag**: Price indexation clause that is opaque, not clearly explained to a
  consumer, or disproportionately one-sided.

#### 7c. Consumer Withdrawal Rights (14-Day Cooling-Off Period)

For any consumer contract concluded at a distance or off-premises:

- Statutory 14-calendar-day right of withdrawal applies (Act No. 16/2001 implementing
  Directive 2011/83/EU) [VERIFY current Act number — may have been updated].
- The withdrawal period starts from delivery (goods) or contract conclusion (services).
- Seller/service provider must provide a model withdrawal form.
- **Exceptions**: Custom-made goods, perishables, digital content with immediate
  performance after consumer's express consent, sealed goods opened after delivery.
- **RED flag**: Any contract purporting to exclude the 14-day withdrawal right for
  distance/off-premises consumer contracts.
- **RED flag**: Failure to provide pre-contractual information required before the
  consumer is bound (identity of trader, price including all taxes, right of withdrawal
  notice, complaints procedure).

#### 7d. Sale of Goods — Conformity and Warranty

**Consumer sales (Act No. 48/2003 implementing Directive 2019/771)**:

- Goods must conform with the contract description, suitable for purpose, and of
  satisfactory quality.
- **Warranty period**: Minimum 2 years; Iceland extended this to **5 years for goods
  with considerably longer lifespans** than 2 years (stronger than EU minimum).
- Remedies hierarchy: repair → replacement → price reduction → contract termination.
- These remedies are **non-derogable** in consumer contracts — any clause attempting
  to exclude or limit them is void.
- **RED flag**: Any limitation of warranty below the statutory minimum in a consumer sale.

**Commercial sales (Act No. 50/2000 — CISG-derived)**:

- CISG applies to international sales between Iceland and other CISG Contracting States.
- **Nordic reservation**: Iceland, Denmark, Finland, Norway, and Sweden declared CISG
  does not apply to inter-Nordic sales. Sales between Icelandic and other Nordic parties
  are governed by Act No. 50/2000 (domestic law) not CISG.
- Conformity period: 2 years from delivery (default); parties may shorten for B2B.
- Buyer must examine goods promptly and notify defects within reasonable time.

#### 7e. Intellectual Property — Copyright and Assignment

Under Höfundalög (Copyright Act No. 73/1972 as amended):

- **No work-for-hire doctrine**: Icelandic copyright law does not have an equivalent
  to the US work-made-for-hire concept. IP created by an independent contractor
  belongs to the creator by default.
- **Assignment must be in writing** and should specify the fields of exploitation
  (exploit rights must be granted explicitly).
- **Moral rights (persónulegar höfundarréttarheimildir) are inalienable** — they
  cannot be assigned or waived, only not exercised in certain contexts [VERIFY scope
  of this principle in Icelandic practice].
- **Software**: Computer programs are protected as literary works.
- **RED flag**: Blanket IP assignment from contractor to client without specifying
  fields of exploitation; any clause purporting to waive moral rights.
- **YELLOW flag**: Assignment without specifying whether pre-existing IP is carved out.

#### 7f. Data Protection — Act No. 90/2018 (GDPR Implementation)

Iceland implemented GDPR through Act No. 90/2018. Persónuvernd is the supervisory
authority. The same substantive rules as EU GDPR apply:

- Data Processing Agreements (DPAs) required under Art. 28 equivalent.
- 72-hour breach notification to Persónuvernd.
- Cross-border transfers: standard contractual clauses or adequacy decisions.
- Iceland is treated as an EEA country for transfer purposes.
- **RED flag**: No DPA where personal data is processed; breach notification period
  longer than 72 hours; no cross-border transfer mechanism identified.

#### 7g. Limitation Periods — Act No. 150/2007

| Claim Type                                              | Limitation Period                                                 |
| ------------------------------------------------------- | ----------------------------------------------------------------- |
| General contractual claims                              | **4 years** from when the creditor could first exercise the right |
| Claims under debt certificates / negotiable instruments | 10 years                                                          |
| Deposits with financial institutions                    | 20 years                                                          |
| Claims against public funds                             | 20 years                                                          |

Key rules:

- Period starts when the creditor **could first** exercise the right (discovery rule element).
- Interrupted by acknowledgment of the claim by the debtor.
- Suspended by written agreement of the parties.
- Survival clauses in contracts cannot extend limitation periods beyond the statutory
  maximum [VERIFY].
- **YELLOW flag**: Contractual limitation clause shortening the 4-year period for
  breach of contract claims. May be permissible in B2B but scrutinise in consumer.
- **YELLOW flag**: Survival clause that leaves obligations alive but no notice that the
  limitation clock runs from the relevant event.

### Step 8: Missing Clause Detection

After clause-by-clause analysis, check for important absent provisions:

**Consumer contracts — mandatory missing items:**

- [ ] No pre-contractual information sheet → RED
- [ ] No withdrawal notice / model form (distance contracts) → RED
- [ ] No conformity / warranty provisions consistent with Act 48/2003 or 42/2000 → RED
- [ ] No complaints procedure reference → YELLOW

**All contracts — material missing items:**

- [ ] No governing law clause → RED
- [ ] No limitation of liability clause → RED
- [ ] No dispute resolution clause → YELLOW
- [ ] No data protection / DPA clause where personal data processed → RED
- [ ] No limitation period clause (if deviation from statutory 4 years intended) → YELLOW
- [ ] No force majeure clause (long-term contracts) → YELLOW
- [ ] No assignment restrictions → YELLOW
- [ ] No IP ownership clause in creative/technology contracts → RED
- [ ] No price indexation or interest clause in long-term payment contracts → YELLOW

**⟁ CLARIFY** — Where the severity of a missing clause depends on business context
not yet provided:

- "There is no DPA. Will personal data be processed under this agreement? If yes → RED."
- "There is no limitation of liability clause. Is this a high-value or long-term
  engagement where uncapped liability is a concern?"

### Step 9: Flag Deviations and Generate Redlines

Classify each deviation using the three-tier system (see **Severity Classification**
below). For each YELLOW and RED item, generate a redline using the **Redline Format**.

**⟁ CLARIFY** — Before generating redlines:

- **Relationship dynamic**: New counterparty vs. established partner? Redline tone shifts.
- **Volume**: "I've found [N] items worth negotiating. Focus on all or top [X] by impact?"

### Step 10: Quality Verification

Before delivering output:

1. Run the 5 Citation Quality Gates silently. Revise any failures.
2. For every RED item, run the 3-pass Self-Interrogation. Revise if any pass reveals
   a weakness.
3. Assign a Confidence Score to each material clause analysis.
4. Verify all 15 clause categories addressed (present or flagged as absent).
5. Generate the Glass Box Audit Trail and append to output.

---

## Icelandic Contract Law Reference

### Core Principles

**1. Freedom of Contract (Samningsfrelsi)**
Parties have broad freedom to agree terms. The principle is subject to three limits:

- **Section 36, Act 7/1936**: Courts may set aside substantially unreasonable clauses.
- **Mandatory consumer provisions**: Consumer protective rules cannot be contracted out.
- **Public policy and good morals**: Contracts contrary to law or public order are void.

**2. Contract Formation**

- **No consideration required**: Icelandic (Nordic) law is consensus-based. A valid
  contract requires only mutual assent (samþykki) — no exchange of value needed.
- **Freedom of form**: Contracts may be formed verbally, by conduct, or in writing
  unless statute requires a specific form.
- **Writing required for**: Powers of attorney (umboð); real property transfers;
  certain financial instruments; notarial instruments.
- **Electronic contracts**: Valid for most purposes under Act No. 30/2002. Electronic
  signatures of three levels (SES, AES, QES) are recognised; QES is legally equivalent
  to a handwritten signature.

**3. Invalidity Grounds (Ógilding)**
Under Act No. 7/1936, a contract may be void or voidable on these grounds:

| Ground                       | Icelandic term               | Notes                                               |
| ---------------------------- | ---------------------------- | --------------------------------------------------- |
| Duress                       | Þvingun / óhemjulegt þvingun | Threats rendering consent involuntary               |
| Fraud                        | Svik                         | Intentional deception inducing contracting          |
| Undue influence              | Misneytning                  | Exploitation of weakness, incapacity, or dependence |
| Error / mistake              | Villur                       | Significant bilateral or induced error of fact      |
| Lack of capacity             | Ólögræði                     | Minors under 18; mental incapacity                  |
| Substantial unreasonableness | Section 36 — óhæfilegt       | General equity ground; partial set-aside possible   |

**4. Standard Terms (Staðlaðir Samningsskilmálar)**

- Standard terms must be **clearly incorporated** — made available before or at
  contract formation.
- **Surprising or onerous clauses** (óvænt ákvæði) may not be incorporated even if
  technically available, if a reasonable party would not have expected them.
- **Contra proferentem**: Ambiguous standard terms are construed against the drafter.
- **Battle of forms**: When both parties use standard terms, Icelandic courts apply
  a "last shot" or "knock-out" approach depending on circumstances [VERIFY].

**5. Interpretation (Túlkun Samninga)**

- Objective interpretation: courts seek the reasonable meaning of the contract language.
- Parties' mutual intent controls where discernible from negotiations and course of
  dealing.
- Trade custom and usage (viðskiptavenjur) fills gaps.
- Good faith (góð trú) is a pervasive implied obligation.
- Parol evidence rule: No direct equivalent — courts in civil law tradition can look
  beyond written text to establish intent.

**6. Remedies for Breach (Vanefndir)**
| Remedy | Icelandic term | Availability |
|--------|---------------|-------------|
| Damages — actual loss | Skaðabætur | Always; causation + foreseeability required |
| Damages — lost profit | Mist hagnaður | Foreseeable at contract formation |
| Specific performance | Efndakrafa | When monetary relief inadequate |
| Price reduction | Afsláttur | Sale and service non-conformity |
| Termination / rescission | Riftun | Material breach; statutory consumer rights |
| Interest on overdue sums | Dráttarvextir | Act No. 38/2001 default rate |

**Duty to mitigate**: Claimant must take reasonable steps to reduce loss. Failure
reduces recoverable damages.

**Limitation clauses**: Permissible in B2B under freedom of contract but subject to
Section 36. Cannot completely exclude liability for **intentional misconduct or
gross negligence** (stórkostlegt gáleysi) [VERIFY precise Icelandic rule]. Consumer
contracts cannot exclude statutory remedies.

---

## Severity Classification

### GREEN — Acceptable

Clause aligns with or is better than the standard commercial position. Minor variations
that are commercially reasonable under Icelandic law.

**Examples:**

- Mutual limitation of liability at an appropriate multiple of contract value
- Warranty period at or above the statutory minimum (2 years / 5 years for long-lifespan)
- Governing law in Iceland with dispute resolution at District Court or Landsréttur

**Action**: Note for awareness. No negotiation needed.

### YELLOW — Negotiate

Clause falls outside the standard position but within a negotiable range. Common in the
market but not optimal. Requires attention and likely negotiation.

**Examples:**

- Limitation of liability cap well below the annual contract value
- Warranty period shortened in B2B to 1 year (permissible but below customary)
- Price indexation clause that is valid but to an unfavourable index
- Default interest rate set below Act No. 38/2001 statutory rate
- Assignment permitted on notice rather than consent

**Action**: Generate specific redline language. Provide fallback position. Estimate
business impact.

### RED — Escalate / Unacceptable

Clause poses material legal risk, may be void or unenforceable under Icelandic law,
or triggers a mandatory consumer protection violation.

**Examples:**

- Complete exclusion of liability in a consumer contract (void — non-derogable)
- Exclusion of the 14-day withdrawal right for a distance consumer contract (void)
- Warranty shorter than the statutory minimum in a consumer sale (void)
- No DPA when personal data is processed (GDPR / Act 90/2018 violation)
- Blank IP assignment capturing pre-existing IP without carveout
- Price indexation clause in a consumer contract that is opaque or unfair (Directive
  93/13 / Section 36 risk)
- No governing law clause (creates uncertainty and litigation risk)
- Limitation period contractually cut to less than 4 years in consumer contexts

**Action**: Explain specific risk with Icelandic legal basis. Provide market-standard
alternative language. Estimate exposure. Recommend escalation to qualified Icelandic
counsel.

---

## Redline Format

For each YELLOW and RED deviation:

```
**Clause**: [Section reference and clause name]
**Classification**: RED / YELLOW
**Current language**: "[exact quote from the contract]"
**Proposed redline**: "[specific alternative language]"
**Rationale**: [1-2 sentences, suitable for external sharing with counterparty]
**Legal basis**: [Specific Icelandic statute/principle — or "General commercial practice (Iceland)"]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative position if primary redline is rejected]
**Confidence**: [Definite / High / Probable / Possible — see Confidence Scoring]
```

### Redline Best Practices

1. **Provide exact language**: Redlines should be ready to insert, not vague guidance.
2. **Cite Icelandic law basis**: Reference the specific Act and section where possible.
3. **Distinguish consumer from commercial**: A clause acceptable in B2B may be void in
   consumer context; make this explicit.
4. **Mark memory-sourced citations**: If citing from research rather than legalcode-mcp,
   mark with [VERIFY].
5. **Prioritise**: Not all redlines are equal. Indicate must-haves vs. concession items.
6. **Provide fallback positions**: For YELLOW items, include an alternative if the
   primary redline is rejected.
7. **Respect the Nordic style**: Icelandic commercial contracts tend toward directness
   and concision. Redlines should not add unnecessary boilerplate.

---

## Negotiation Priority Framework

### Tier 1 — Must-Haves (Mandatory / Deal-Breakers)

Issues where the user cannot proceed without resolution — either because the clause is
void under Icelandic law, violates consumer protection, or creates unacceptable legal risk:

- Any clause void under mandatory consumer protection acts
- Missing DPA where personal data is processed (Act 90/2018 violation)
- Missing or conflicting governing law clause
- IP assignment capturing pre-existing IP without carveout
- Complete exclusion of liability / non-derogable consumer remedies excluded
- Absence of mandatory pre-contractual information for distance consumer contracts

### Tier 2 — Should-Haves (Strong Preferences)

Issues that materially affect risk but have negotiation room under Icelandic law:

- Liability cap adjustments within commercially acceptable ranges
- Price indexation (verðtrygging) terms — index selection and transparency
- Default interest rate alignment with Act No. 38/2001
- Warranty period adjustments (B2B — customary 2 years even if parties could agree less)
- Termination notice periods and cure rights
- Assignment consent vs. notice

### Tier 3 — Nice-to-Haves (Concession Candidates)

Issues that improve the position but can be conceded strategically:

- Preferred arbitration vs. court litigation (both are valid in Iceland)
- Insurance certificate requirements
- Notice method preferences
- Minor definitional refinements
- Boilerplate style preferences

**Strategy**: Lead with Tier 1. Trade Tier 3 concessions to secure Tier 2 wins. Never
concede on Tier 1 without escalation to qualified Icelandic counsel.

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Identify contract type, user's side, consumer/commercial classification.
Confirm governing law is Icelandic. Identify which Acts apply.

**DO**: Execute clause-by-clause analysis. Apply Icelandic-specific deep dives (Steps 7a–7g).
Generate redlines.

**CHECK**: Run Citation Quality Gates. For any RED item, run Self-Interrogation. Verify
statutory references. Confirm all 15 categories addressed.

**ACT**: Record new patterns. Flag any emerging Icelandic/EEA law developments for
future reference.

### Citation Quality Gates

Run these 5 gates silently before delivering output:

| Gate           | Rule                                                                                                                               | Fail Action                                                   |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific Icelandic Act, EEA directive, or established Icelandic principle                                | Add citation or mark "[UNVERIFIED — lögfræðingur to confirm]" |
| **Format**     | All Icelandic Act citations follow the format "Act No. [number]/[year] (Icelandic title)"                                          | Fix format                                                    |
| **Currency**   | Every cited provision checked for amendments — Icelandic Acts are amended frequently through EEA alignment                         | Flag "[CHECK CURRENCY — may have been amended]"               |
| **Domain**     | Analysis stays within Icelandic law. No EU law applied as directly applicable (it is not — only EEA-implemented equivalents apply) | Remove or flag jurisdictional bleed                           |
| **Confidence** | Uncertainty explicitly stated; never hidden                                                                                        | Add confidence qualifier                                      |

### Self-Interrogation for RED Items

For any clause classified as RED, apply this 3-pass self-interrogation:

**Pass 1 — Legal Chain Integrity**:

- Does the risk assessment follow logically from the cited Icelandic statute?
- Would an Icelandic district court (héraðsdómur) actually reach this conclusion?
- What is the counterparty's likely argument against this classification?

**Pass 2 — Completeness**:

- Have all relevant Icelandic Acts been considered?
- Is there applicable EEA/EFTA Court jurisprudence that could shift the analysis?
- Are there regulatory dimensions (Persónuvernd, Neytendastofa, FME) not yet addressed?

**Pass 3 — Challenge**:

- What is the strongest argument that this clause is acceptable under Icelandic law?
- Is the Section 36 fairness concern present, or is this simply below-standard commercially?
- Is the RED classification proportionate, or is this actually YELLOW with mitigations?

Mark audit trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material clause analysis, assign a confidence level:

| Level        | Range     | Meaning                                                     | Action                                                      |
| ------------ | --------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled Icelandic statute, clearly applicable               | State with confidence                                       |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions            | State with brief caveat                                     |
| **Probable** | 0.60–0.79 | Good arguments; Icelandic courts could differ               | State with explicit reasoning and contra-indicators         |
| **Possible** | 0.40–0.59 | Genuinely uncertain; EFTA Court or Hæstiréttur input needed | Flag for qualified Icelandic counsel review with both sides |
| **Unlikely** | 0.0–0.39  | Weak basis or speculative                                   | Do not assert; flag "[UNCERTAIN — lögfræðingur to advise]"  |

---

## Glass Box Audit Trail

Every review output MUST include this audit section at the end:

```yaml
glass_box:
  skill_name: "legalcode-is-contract-law-general"
  contract: "[Contract title and date]"
  contract_type: "[Consumer sale / B2B service / Software licence / etc.]"
  user_side: "[Supplier / Customer / Licensor / etc.]"
  consumer_or_commercial: "[Consumer / Commercial / Mixed]"
  governing_law: "Icelandic law (confirmed from governing law clause / assumed)"
  applicable_acts:
    - "[Act No. X/YYYY — reason it applies]"
  eea_directives_relevant:
    - "[Directive XX/YY/EEC — as implemented in Iceland]"
  clauses_reviewed: 15
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "[Act — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  case_law_consulted:
    - "[Case — Hæstiréttur / Landsréttur / EFTA Court — VERIFIED or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified Icelandic legal review (lögfræðingur)"
```

---

## Multi-Stakeholder Mapping

For every Icelandic-law contract, identify all affected stakeholders:

| Stakeholder              | Role                                   | Affected Clauses    | Impact        | Action Required                               |
| ------------------------ | -------------------------------------- | ------------------- | ------------- | --------------------------------------------- |
| Party A                  | [Seller / Service Provider / Licensor] | All                 | Primary       | Sign / Negotiate                              |
| Party B                  | [Buyer / Consumer / Licensee]          | All                 | Primary       | Sign / Negotiate                              |
| Data subjects            | Third parties                          | Data protection     | Indirect      | DPA required if personal data processed       |
| Neytendastofa            | Regulator                              | Consumer clauses    | Enforcement   | Consumer rights non-derogable                 |
| Persónuvernd             | Regulator                              | Data protection     | Enforcement   | Act 90/2018 / GDPR compliance                 |
| FME (Fjármálaeftirlitið) | Regulator                              | Financial services  | If applicable | Regulated activities require authorisation    |
| Employees / contractors  | Internal                               | IP, confidentiality | Indirect      | Höfundalög — IP belongs to creator by default |

---

## Anti-Patterns

What NOT to do when reviewing or drafting contracts under Icelandic law:

1. **Treating Iceland as an EU member state** — Iceland is an EEA Contracting Party,
   not an EU member. EU Regulations do not directly apply; only EEA-implemented
   equivalents do. GDPR applies via Act No. 90/2018, not directly. Cite the Icelandic
   implementing act, not the EU regulation.

2. **Ignoring Section 36 (Act 7/1936) fairness review** — Section 36 gives courts
   broad power to set aside or modify unreasonable clauses in any contract. A clause
   that is technically lawful may still be struck down if it is substantially
   unreasonable. Always ask: "Would a Section 36 challenge succeed here?"

3. **Missing the consumer/commercial distinction** — Icelandic consumer protection
   provisions are mandatory and non-derogable. A clause valid in a B2B context may be
   void in a consumer contract. Never assume the same analysis applies to both without
   checking each relevant consumer act.

4. **Ignoring verðtrygging (price indexation)** — Price indexation is a distinctive
   feature of the Icelandic economy. Long-term payment clauses without indexation
   provisions may not reflect the parties' actual intent. At the same time, opaque
   indexation in consumer contracts carries Directive 93/13 unfair-terms risk. Always
   address the indexation question explicitly.

5. **Applying the CISG to Nordic inter-Scandinavian sales** — Iceland, Denmark, Finland,
   Norway, and Sweden all reserved that CISG does not apply between Nordic parties.
   A sale of goods between an Icelandic and a Danish company is governed by domestic
   sales law, not CISG. Missing this leads to wrong legal analysis.

6. **Assuming work-for-hire applies** — Icelandic copyright law (Höfundalög) has no
   work-for-hire doctrine. IP created by an independent contractor belongs to the
   contractor by default, not the commissioning party. Explicit written assignment
   is required, specifying fields of exploitation.

7. **Drafting a limitation of liability exclusion in a consumer contract** — Consumer
   statutes create non-derogable minimum remedies. Limiting liability below the
   statutory minimum in a consumer sale or service contract is void. Redline every
   attempt to do this.

8. **Forgetting the 4-year limitation period** — The general contractual claims
   limitation under Act No. 150/2007 is 4 years — shorter than the 5-year period
   in many comparable European jurisdictions. Survival clauses and indemnification
   obligations should be reviewed against this background.

9. **Missing Landsréttur as the intermediate appellate court** — Iceland created the
   Landsréttur (Court of Appeal) in 2018. Pre-2018 guidance on court hierarchy is
   outdated. Dispute resolution clauses should reflect the current three-tier structure.

10. **Conflating Act 48/2003 and Act 50/2000** — Act 50/2000 governs commercial sale
    of goods; Act 48/2003 governs consumer sale of goods. They have different conformity
    periods, remedy hierarchies, and derogability rules. Always confirm which applies.

11. **Citing EU law directly as binding in Iceland** — EU directives and regulations
    are not directly applicable in Iceland. The binding authority is the Icelandic
    implementing act. Cite "Act No. 90/2018 (GDPR implementation)" not "GDPR Art. 28"
    as the primary legal basis, though cross-referencing the directive for context is
    helpful.

12. **Missing dráttarvextir (default interest) compliance** — Act No. 38/2001 sets the
    statutory default interest rate. Contracts that fail to address overdue payment
    interest will attract this rate by default. In consumer contracts, the rate cannot
    be set punitively above statutory norms [VERIFY].

13. **Ignoring moral rights in IP clauses** — Icelandic copyright includes inalienable
    moral rights (persónulegar höfundarréttarheimildir). No clause can permanently strip
    a creator's right to attribution (right to be identified as author) or integrity
    (right to object to derogatory treatment of the work). Clauses purporting to do so
    are void.

14. **Overlooking Persónuvernd's enforcement posture** — Iceland's data protection
    authority (Persónuvernd) is active and exercises GDPR-equivalent enforcement powers.
    Any data processing provision that is compliant under old Icelandic rules but not
    under Act No. 90/2018 / GDPR is a live enforcement risk.

15. **Skipping the EEA/EFTA Court jurisprudence layer** — EFTA Court decisions on
    Directive 93/13 (including landmark Icelandic mortgage indexation cases) are binding
    interpretive authority in Iceland. For consumer contracts, search EFTA Court decisions
    before concluding that a clause is valid under Icelandic law.

---

## Writing Standards

Apply these standards to all contract analysis and drafting outputs:

1. **Be precise about jurisdiction**: Always say "under Icelandic law" not "under
   Scandinavian law" or "under Nordic law." Iceland has its own legal system.

2. **Use bilingual terminology for important concepts**: Give the Icelandic term in
   parentheses on first use (e.g., "limitation periods (fyrningarfrestur)"). This helps
   Icelandic-speaking parties and counsel verify the analysis.

3. **Distinguish consumer from commercial throughout**: Every finding should state
   whether it applies in consumer context, commercial context, or both.

4. **Never hide uncertainty**: If you are not certain of an Icelandic rule, say so
   explicitly. Mark it [VERIFY] and recommend qualified Icelandic counsel confirm.

5. **Avoid over-reliance on EU equivalents**: EEA-implemented Icelandic law may diverge
   from the EU equivalent. Iceland sometimes provides greater protection (e.g., 5-year
   warranty period). Always check the Icelandic implementing act.

6. **Write in plain language**: Icelandic commercial contracts are typically concise
   and direct. Avoid over-engineered boilerplate. If an analysis point can be stated
   in one sentence, use one sentence.

7. **Quality gate before delivery**: Before presenting any output, confirm:
   - [ ] Every RED item has a Tier 1 / Tier 2 priority designation
   - [ ] Every statutory citation is marked VERIFIED or [VERIFY]
   - [ ] Consumer provisions are flagged as non-derogable where relevant
   - [ ] Glass Box audit trail is complete and appended
   - [ ] Confidence scores are assigned to all material clause analyses

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for current text of all Icelandic Acts listed in the statute table above
- Search Hæstiréttur decisions on the specific contract type
- Search EFTA Court decisions relevant to Directive 93/13, 2019/771, and 2011/83
  in Iceland
- Search Persónuvernd decisions for data protection compliance
- Search Neytendastofa guidance for consumer contract compliance
- Save results to `/tmp/legalcode-is-contract-review.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the audit trail

**Without legalcode-mcp:**

- Mark all statutory and case-law references with [VERIFY]
- Note in audit trail: `legalcode_mcp: "Not connected — manual verification required"`
- Recommend the user verify citations at althingi.is, haestirettur.is, and
  efta.int/court before relying on any legal analysis
- Focus the review on structural quality, obvious RED flags, and framework application
  rather than specific case-law citations

**Primary Icelandic legal databases:**

- **althingi.is** — Official parliamentary database of all Acts in current force
- **haestirettur.is** — Supreme Court decisions
- **landsrettur.is** — Court of Appeal decisions
- **efta.int/court** — EFTA Court decisions (binding on Iceland)
- **neytendastofa.is** — Consumer Agency guidance and decisions
- **personuvernd.is** — Data Protection Authority guidance
- **island.is** — Government portal with consumer rights guides

---

## Localization Notes

This skill is Iceland-specific. When using it alongside other Nordic jurisdiction skills:

| Aspect                  | Iceland                                     | Denmark/Sweden/Norway/Finland                      |
| ----------------------- | ------------------------------------------- | -------------------------------------------------- |
| Contract law foundation | Act 7/1936 (own Act)                        | Own national contract acts (same Nordic tradition) |
| CISG applicability      | Ratified; Nordic reservation                | Same Nordic reservation                            |
| Consumer acquis         | EEA, not EU member                          | EU member; directly applicable                     |
| GDPR                    | Via Act 90/2018 (EEA)                       | Directly applicable + national implementation      |
| Currency & indexation   | ISK; verðtrygging common                    | EUR/DKK/SEK/NOK; indexation less common            |
| Court structure         | District → Landsréttur (2018) → Hæstiréttur | Country-specific                                   |

**Language requirements**: Icelandic law does not generally mandate that contracts be
in Icelandic, but consumer-facing pre-contractual information and withdrawal notices
should be in a language the consumer understands (typically Icelandic for domestic
transactions). Government contracts and regulatory submissions are typically in
Icelandic [VERIFY].

---

## Output Format Template

Deliver every contract review using this format:

---

## Contract Review — [Contract Name]

**Governing law**: Icelandic law (Act No. 7/1936 and applicable sector Acts)
**Review date**: [date]
**User's position**: [Party role]
**Contract type**: [Consumer / Commercial — specific type]
**Review basis**: [Organisational playbook / General Icelandic commercial standards]

---

### Executive Summary

**Overall risk level**: HIGH / MEDIUM / LOW

[2-3 sentence summary of the contract's risk profile and the most important issues.]

**Top 3 issues:**

1. [Issue] — [RED/YELLOW] — [one-line impact statement]
2. [Issue] — [RED/YELLOW] — [one-line impact statement]
3. [Issue] — [RED/YELLOW] — [one-line impact statement]

---

### Consumer Protection Compliance (if consumer contract)

| Provision                                   | Status       | Notes |
| ------------------------------------------- | ------------ | ----- |
| Pre-contractual information                 | ✅ / ⚠️ / ❌ |       |
| 14-day withdrawal right                     | ✅ / ⚠️ / ❌ |       |
| Conformity / warranty minimum               | ✅ / ⚠️ / ❌ |       |
| Complaints procedure                        | ✅ / ⚠️ / ❌ |       |
| Unfair terms (Section 36 / Directive 93/13) | ✅ / ⚠️ / ❌ |       |

---

### Clause-by-Clause Analysis

#### [Clause Category Name] — [GREEN / YELLOW / RED]

**Current position**: [What the contract says]
**Issue**: [What the problem is, if any]
**Legal basis**: [Act No. X/YYYY, Section Y — or "General commercial standard (Iceland)" — VERIFIED or [VERIFY]]
**Confidence**: [Definite / High / Probable / Possible / Unlikely] ([0.XX])

[Repeat for each clause category]

---

### Missing Clauses

| Missing Item             | Severity | Recommendation                                                   |
| ------------------------ | -------- | ---------------------------------------------------------------- |
| [e.g., No DPA]           | RED      | Add a GDPR-compliant Data Processing Agreement (Act No. 90/2018) |
| [e.g., No force majeure] | YELLOW   | Add standard force majeure provision with Nordic hardship carve  |
| ...                      |          |                                                                  |

---

### Redlines

[Use Redline Format for each YELLOW and RED item]

---

### Negotiation Strategy

**Tier 1 — Must resolve before signing:**

- [List of Tier 1 items]

**Tier 2 — Strongly prefer to resolve:**

- [List of Tier 2 items]

**Tier 3 — Concession candidates:**

- [List of Tier 3 items]

**Recommended sequencing**: [1-2 sentences on negotiation order and approach]

---

### Glass Box Audit Trail

```yaml
[Complete Glass Box YAML — see template above]
```

---

_Review produced by legalcode-is-contract-law-general. Requires qualified Icelandic
legal review (lögfræðingur) before reliance._

---

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis from:

- Comprehensive web research on Act No. 7/1936, Act No. 50/2000, Act No. 48/2003,
  Act No. 42/2000, Act No. 16/2001, Act No. 150/2007, Act No. 38/2001, Act No. 30/2002,
  Act No. 90/2018, and Höfundalög (Act No. 73/1972)
- Research on EEA consumer acquis implementation in Iceland: Directives 93/13, 2011/83,
  1999/44 (replaced by 2019/771), 2000/31
- EFTA Court jurisprudence on Icelandic consumer protection cases
- Structure and quality frameworks adapted from `legalcode-contract-review`
  (general jurisdiction-agnostic gold standard)
- Existing Iceland skills in the repository: `legalcode-iceland-real-estate-contracts`,
  `legalcode-non-compete-analysis-is`
- NYU Law GlobalEx guide to Icelandic law research
- Neytendastofa (Consumer Agency Iceland) public guidance
- DocuSign / Adobe e-signature legality guides for Iceland

**Attribution**: Legalcode original synthesis. No third-party skill imported.
