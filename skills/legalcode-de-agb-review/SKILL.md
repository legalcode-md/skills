---
name: legalcode-de-agb-review
description: Reviews German General Terms and Conditions (AGB — Allgemeine Geschäftsbedingungen) under
  BGB §§ 305–310. Use when drafting, reviewing, or auditing standard terms for German-law contracts —
  whether B2C, B2B, online, or employment. Covers incorporation requirements (§ 305), surprising clause
  prohibition (§ 305c), transparency (§ 307 Transparenzgebot), conditional prohibitions (§ 308), absolute
  prohibition catalogue (§ 309), B2C vs. B2B distinctions (§ 310), consequences of invalidity and the
  prohibition of Geltungserhaltende Reduktion (§ 306). Also applies to e-commerce AGB, software licensing
  terms, IT procurement, and post-2022 subscription/auto-renewal changes. Triggers on "review our AGB",
  "check German T&Cs", "BGB 305", "AGB Inhaltskontrolle", "German general conditions", "standard terms
  Germany", "AGB enforceable", or any request to draft or validate general terms under German law.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode: German AGB Review (BGB §§ 305–310)

> **Disclaimer**: This skill provides a framework for AI-assisted review of German General
> Terms and Conditions (Allgemeine Geschäftsbedingungen). It does not constitute legal
> advice (Rechtsberatung) and does not create a lawyer–client relationship. All outputs
> must be reviewed by a qualified German-licensed lawyer (Rechtsanwalt) before reliance or
> use. German law changes; verify all statutory and case law references against authoritative
> sources (gesetze-im-internet.de, dejure.org, BGH-Entscheidungen) before acting on them.
> Statutory and case law references cited from memory carry hallucination risk — mark
> unverified citations [VERIFY] and confirm before relying.

---

## Purpose and Scope

This skill reviews AGB — pre-formulated contractual terms (§ 305 Abs. 1 BGB) intended for
use across multiple contracts — against the German statutory framework in BGB §§ 305–310.

**Covers:**

- Incorporation validity (§§ 305, 305a): whether AGB are properly part of the contract
- Priority of individual agreements (§ 305b): Vorrang der Individualabrede
- Surprising clauses and ambiguity (§ 305c): überraschende Klauseln, Unklarheitenregel
- Consequences of invalidity (§ 306): severability, Geltungserhaltende Reduktion prohibition
- General good faith test (§ 307): Inhaltskontrolle, Transparenzgebot
- Conditional prohibition catalogue (§ 308): Klauselverbote mit Wertungsmöglichkeit
- Absolute prohibition catalogue (§ 309): Klauselverbote ohne Wertungsmöglichkeit
- Scope and B2C/B2B distinctions (§ 310): Kaufmann privilege, consumer contract protections
- 2022 amendments: auto-renewal rules, online cancellation button requirement
- Sector-specific frameworks: IT/EVB-IT, employment AGB, e-commerce, banking/insurance

**Does not:**

- Draft AGB from scratch (use a dedicated AGB drafting skill)
- Provide advice on AGB for jurisdictions other than Germany
- Constitute a complete UKlaG (Unterlassungsklagengesetz) risk assessment
- Replace a qualified German Rechtsanwalt for final sign-off

---

## Jurisdiction and Governing Law

**Jurisdiction**: Federal Republic of Germany (Bundesrecht)
**Primary statute**: Bürgerliches Gesetzbuch (BGB) §§ 305–310, in force as amended through
the Fair Consumer Contracts Act (Gesetz zur Regelung des fairen Verbrauchervertrags) of
2021/2022

**Key secondary legislation:**

- UKlaG (Unterlassungsklagengesetz) — injunctive enforcement of invalid AGB by associations
- EU Directive 93/13/EEC — minimum harmonization baseline (German law exceeds the minimum)
- HGB § 362 — merchant silence as acceptance in B2B dealings
- For sector-specific AGB: KWG, VAG (banking/insurance), EVB-IT (public IT procurement),
  VOB/B (construction)

**Geographic scope**: This skill applies to contracts governed by German law (deutsches
Recht). For Austrian or Swiss law, material differences exist — treat this skill as a
starting point only and consult jurisdiction-specific authority [VERIFY].

**Choice-of-law note**: German courts will apply German AGB control rules even where a
contract contains a foreign-law clause, if the contract has a sufficiently close connection
to Germany or involves a German consumer (BGH VIII ZR 7/23, Nov. 2023 [VERIFY]).

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context, the workflow pauses and asks when:

- The B2C / B2B classification is unclear (it changes nearly everything)
- The contracting channel is unknown (online vs. paper affects incorporation analysis)
- The industry or sector is relevant for special rules (IT, banking, employment)
- A clause is borderline between QUESTIONABLE and VOID and the risk appetite matters
- The user's purpose is review only vs. remediation drafting

Use the **⟁ CLARIFY** pattern at every marked point. If the user has already provided
the information in their prompt, skip the question and proceed.

---

## Workflow

### Step 1: Accept the AGB

Accept the AGB in any format:

- **File**: PDF, DOCX, or text document
- **URL**: Link to publicly posted terms
- **Pasted text**: AGB text pasted directly into the conversation
- **Partial draft**: Extract of terms under review

If no AGB text is provided, prompt the user to supply it.

### Step 2: Gather Context

**⟁ CLARIFY** — Ask the user these questions before beginning. Skip any already answered:

1. **Party type (most critical)**
   - Options: **B2C** (Verbrauchervertrag — at least one party is a consumer under § 13 BGB),
     **B2B** (both parties are Unternehmer under § 14 BGB), **Employment** (Arbeitsvertrag —
     special BAG rules apply), **Mixed or unclear**
   - _Why this matters_: §§ 308–309 absolute and conditional prohibitions apply directly only
     in B2C. In B2B, they operate as indicative standards via § 307. Classification changes
     the entire analysis.

2. **Contracting channel**
   - Options: Online (e-commerce / click-wrap), Paper / signed agreement, B2B framework
     agreement, Hybrid (online order + paper terms), Unknown
   - _Why this matters_: Online contracting has specific § 305 incorporation requirements
     and, for consumer subscriptions since July 2022, a mandatory cancellation button.

3. **Sector or industry**
   - Options: IT / software / SaaS, Retail / e-commerce, Financial services / banking,
     Insurance, Construction, Employment / HR, General commercial, Other (specify)
   - _Why this matters_: Special regimes apply (EVB-IT for IT procurement, VOB for
     construction, BaFin rules for banking/insurance, BAG jurisprudence for employment).

4. **Review purpose**
   - Options: **Audit only** — identify invalid/risky clauses; **Remediation** — identify
     issues and provide corrected draft language; **Pre-publication check** — validate AGB
     before releasing to counterparties; **Dispute / litigation context** — assess specific
     clause enforceability
   - _Why this matters_: Determines whether to provide redline alternatives or analysis only.

5. **Governing law confirmed?**
   - Confirm whether the AGB or the main agreement specifies German law. If not, flag the
     absence and proceed on the assumption German law applies.

### Step 3: Gather Legal Authority

Use **legalcode-mcp** to gather verified BGB authority before analysis.

**Search priorities:**

1. Current text of BGB §§ 305–310 (verify no post-2022 amendments)
2. Recent BGH decisions on § 307 transparency (Transparenzgebot) violations
3. BGH decisions on § 309 No. 7 liability exclusion clauses
4. BGH XI ZR 26/20 (2021) — deemed consent / fictitious consent invalidity [VERIFY]
5. Industry-specific case law if sector was identified in Step 2

Save results to `/tmp/legalcode-agb-authority.md`:

```markdown
# AGB Legal Authority — [Date]

## BGB §§ 305–310 Currency Check

## Key BGH Decisions

## Sector-Specific Rules
```

**Without legalcode-mcp**: Mark all case law citations [VERIFY]. Note in Glass Box:
`legalcode_mcp: "Not connected — manual verification required"`. Proceed with analysis
but flag every statutory claim that is not plain text of BGB.

### Step 4: Structural Pre-Analysis

Before clause-by-clause review, map the AGB structure:

- **Count** distinct clause categories present
- **Identify** any clauses that appear to be individually negotiated (Individualabreden)
  rather than pre-formulated — these are not AGB and fall outside §§ 305–310 scope
- **Flag** the party types identified in the AGB (consumer vs. merchant indicators)
- **Note** whether the AGB are properly labeled and referenced in the main contract

**⟁ CLARIFY** — If a clause might be Individualabrede (genuinely negotiated, not
pre-formulated), ask the user:

- "Clause [X] appears to be individually negotiated rather than pre-formulated. Should I
  analyze it under AGB control (§§ 305–310) or as a negotiated term outside that
  framework?"

### Step 5: Incorporation Analysis (§§ 305–305a)

Assess whether the AGB have been validly incorporated into the contract.

For each incorporation requirement, assign: **MET / UNMET / UNCLEAR**

Apply the full analysis from the **Incorporation Requirements** reference section below.

**⟁ CLARIFY** — If the AGB text was provided without the main contract, ask:

- "Were these AGB accompanied by a main contract that references them? I need to check
  whether the incorporation formalities (§ 305 Abs. 2) were satisfied."

### Step 6: Clause-by-Clause AGB Control Analysis

Analyze each clause across four control layers, in this order:

| Layer                            | Provision     | Question                                                     |
| -------------------------------- | ------------- | ------------------------------------------------------------ |
| 1. Individual agreement priority | § 305b        | Does an Individualabrede override this clause?               |
| 2. Surprising clause             | § 305c Abs. 1 | Is this clause so unusual it cannot have been expected?      |
| 3. Prohibited catalogue          | §§ 308–309    | Does this clause match a listed prohibition?                 |
| 4. General good faith            | § 307         | Does this clause unreasonably disadvantage the counterparty? |

For each clause, complete the analysis from the **AGB Control Reference** section below.
Assign a classification: **VALID / QUESTIONABLE / VOID**.

**⟁ CLARIFY** — For borderline QUESTIONABLE vs. VOID classifications where B2B commercial
context matters, ask:

- "This clause [X] would be automatically void in a B2C context (§ 309 No. [Y]). For your
  B2B contract, the issue is whether it fails the § 307 good faith test given commercial
  norms in your industry. What is the standard practice in your sector for this type of
  clause?"

### Step 7: Flag Deviations and Generate Corrections

For each clause classified QUESTIONABLE or VOID:

**QUESTIONABLE**: Provide analysis of the risk, a corrected draft clause, and the
fallback position if the correction is rejected.

**VOID**: State the specific provision that voids the clause (§ 309 No. X, or § 307
with reasoning), explain the consequence under § 306 (which statutory default fills the
gap), and provide corrected language that achieves the drafter's legitimate purpose
within the law.

**⟁ CLARIFY** — Before generating corrected drafts, confirm:

- "Should I provide (A) corrected draft language for each invalid clause, or (B) analysis
  and identification only, with your team drafting the corrections?"

### Step 8: Assess Consequences of Invalidity (§ 306)

For each VOID clause, apply the § 306 consequence analysis:

1. **Single clause void**: Contract remains valid; statutory default fills the gap.
   Identify the specific statutory default that applies (e.g., § 307 + implied term,
   § 433 et seq. for sale of goods warranty).

2. **Cumulative invalidity**: If multiple clauses are void, assess whether the
   accumulated gaps create "unzumutbaren Nachteil" (unreasonable hardship) for one
   party — the threshold for voiding the entire contract under § 306 Abs. 3. This
   is rare; flag only if the cumulative effect is severe.

3. **Geltungserhaltende Reduktion**: Confirm that no attempt was made in the AGB to
   rely on "savings clauses" (e.g., "to the extent permitted by law" modifiers).
   Under established BGH case law, such clauses themselves violate the
   Transparenzgebot and do not save invalid provisions. Flag any such clause as VOID
   independently.

### Step 9: Business Impact Summary

Provide a summary covering:

- **Overall AGB risk rating**: LOW / MEDIUM / HIGH based on count and nature of void clauses
- **Top issues**: Three most critical findings with severity and legal basis
- **Enforcement risk**: Assessment of UKlaG exposure — whether a consumer or trade
  association could seek an injunction against use of identified invalid clauses
- **Recommended action**: Immediate (fix before publication/use), Near-term (fix in next
  revision), Monitor (low-risk clauses to track)

### Step 10: Quality Verification

Before delivering, run the quality checks from the **Quality Assurance Framework** section:

1. Run the 5 Citation Quality Gates silently.
2. For every VOID classification, run the 3-pass Self-Interrogation.
3. Assign a Confidence Score to each material finding.
4. Verify B2C/B2B classification is consistent throughout the analysis.
5. Check that the § 306 consequence analysis covers every VOID clause.
6. Generate the Glass Box Audit Trail and append it to the output.

---

## AGB Control Reference

### 1. Incorporation Requirements (§§ 305, 305a)

**§ 305 Abs. 2 Requirements (B2C and most B2B):**

| Requirement                                                 | Standard                                                                       | Common Failure Mode                                                                           |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| Express reference (ausdrücklicher Hinweis)                  | Clear statement that AGB apply, referencing where to find them                 | AGB printed only on the reverse of a document without front-page reference                    |
| Reasonable opportunity to take note (zumutbare Möglichkeit) | Counterparty can read, understand, and consider AGB before contract conclusion | AGB sent post-conclusion in confirmation email; terms behind paywall; print too small to read |
| Agreement of the other party                                | Affirmative acceptance (signature, checkbox, verbal confirmation)              | Silence treated as acceptance without prior course of dealing; browse-wrap only               |

**§ 310 Abs. 1 relaxation for B2B:**
Enhanced incorporation requirements of § 305 Abs. 2–3 do NOT apply to AGB used against
entrepreneurs (Unternehmer). However, some form of reference is still required — complete
surprise incorporation is not permitted even in B2B. Course of dealing and industry custom
(Handelsbrauch) can substitute for express reference in established B2B relationships.

**Online contracting specifics:**

- Click-wrap: Checkbox "I agree to the [linked] AGB" immediately before contract conclusion
  is sufficient if AGB are accessible and readable before the click
- Browse-wrap: Hyperlink in page footer without explicit notice is insufficient for B2C
  (§ 305 Abs. 2 not met); very high risk in B2B unless supplemented by notice
- Cancellation button (Kündigungsbutton, since July 1, 2022): For consumer contracts with
  continuing payment obligations concluded online, a clearly labeled, permanently available
  cancellation button is mandatory (§ 312k BGB [VERIFY]). Absence = consumer can cancel
  at any time without notice

**§ 305a special incorporation:**
For utilities, transport, telecoms, and financial services, sector-specific statutory
regimes may provide alternative incorporation pathways. Verify applicable sector regulation.

**§ 305b — Priority of Individual Agreements:**
Any individually negotiated term takes absolute priority over AGB, regardless of whether
the deviation from standard terms is recognized by the parties. "Individual agreement"
requires genuine joint decision-making on the content — offering multiple pre-written
variants is not individual negotiation. Document Individualabreden separately with
counterparty initials or a signed addendum.

---

### 2. Surprising Clause Analysis (§ 305c Abs. 1)

**Test**: Is the clause so unusual, given the objective circumstances of the transaction,
that the counterparty could not reasonably have anticipated it?

**Four-factor analysis:**

| Factor                                     | Assessment Questions                                                                                                                  |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Unusualness (Ungewöhnlichkeit)**         | Is this clause standard in the relevant industry and contract type? Does it deviate radically from statutory defaults?                |
| **Surprise element (Überraschungsmoment)** | Is the clause buried in small print, an appendix, or an unexpected location? Is it visually de-emphasized relative to its importance? |
| **Burden of the clause**                   | How significant is the restriction imposed? Heavier burdens require more prominence.                                                  |
| **Counterparty sophistication**            | Consumer: low threshold for surprise. Merchant with industry experience: higher threshold.                                            |

**High-risk clause types for § 305c:**

- Arbitration clauses not prominently displayed
- Complete liability exclusions in consumer services contracts
- Automatic renewal clauses without prominent disclosure (heightened risk post-2022 amendments)
- Unilateral right to assign contract to a third party
- Price escalation clauses buried in appendices for ostensibly fixed-price arrangements
- Jurisdiction clauses selecting remote or unusual forums for consumer disputes

**Ambiguity Rule (§ 305c Abs. 2 — Unklarheitenregel):**
When AGB language is genuinely ambiguous after applying all standard interpretation rules,
the ambiguity is resolved against the drafter (in dubio contra proferentem). This rule:

- Applies to both B2C and B2B
- Does not apply to Individualabreden
- Is applied after attempting interpretation under §§ 133, 157 BGB (normal interpretation)
- Means ambiguous limitation clauses are read narrowly against the party who drafted them

---

### 3. Absolute Prohibition Catalogue (§ 309)

§ 309 lists clauses that are void in B2C contracts without any justification. In B2B
contexts, these provisions serve as indicative standards (Leitbildfunktion) under § 307.

| § 309 No.  | Prohibited Clause Type                                                                                          | Common Examples                                                               | B2B Status                                                                          |
| ---------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **No. 1**  | Short-term price increases (within 4 months of contract) without objective justification                        | Price increase clause for goods with delivery within 4 months                 | Indicative — may still be invalid if unreasonable                                   |
| **No. 2**  | Restriction or exclusion of right to withhold performance or set off (Aufrechnungs- und Zurückbehaltungsrechte) | "No set-off of counterclaims" without limitation to undisputed claims         | Often invalid in B2B too                                                            |
| **No. 3**  | Precluding objections to assigned claims                                                                        | Clause preventing counterparty raising defenses against assignee              | Indicative                                                                          |
| **No. 4**  | Advance assignment of counterclaims                                                                             | Requiring counterparty to assign claims in advance                            | Indicative                                                                          |
| **No. 5**  | Contractual penalties (Vertragsstrafe) for non-acceptance, late payment, or withdrawal                          | Liquidated damages for breach without proportionality                         | Indicative; B2B penalties valid if proportionate                                    |
| **No. 6**  | Forfeiture of deposit or prepayment (Verfallklausel)                                                            | "Deposit is forfeited upon cancellation"                                      | Indicative                                                                          |
| **No. 7a** | Exclusion of liability for death or personal injury                                                             | "No liability for any personal injury whatsoever"                             | Directly void — § 309 No. 7a reflects mandatory law applicable to B2B too           |
| **No. 7b** | Exclusion of liability for gross negligence (grobe Fahrlässigkeit) for material obligations                     | "No liability for damages of any kind"                                        | Void in both B2C and B2B for intentional/gross negligence on material duties        |
| **No. 8a** | Warranty exclusion for new goods (Gewährleistungsausschluss)                                                    | "Seller gives no warranty for this product"                                   | Indicative; B2B warranty limitation possible but must not eliminate Nacherfüllung   |
| **No. 8b** | Limitation of cure rights (Nacherfüllung) or notice periods below one year                                      | "Customer must report defects within 14 days or warranty is void"             | Indicative; limitation periods below 1 year risky in B2B                            |
| **No. 9**  | Auto-renewal exceeding 1 year without right to cancel with 1 month notice                                       | "Contract renews for 12 months unless 3 months' notice given" (pre-2022 form) | Void per 2022 amendments (see below)                                                |
| **No. 10** | Unilateral right to substitute third party as contracting party                                                 | "Provider may transfer this agreement to any group company"                   | Indicative                                                                          |
| **No. 11** | Restrictions on customer's right to withdraw or cancel orders                                                   | "Orders are binding and cannot be cancelled" without qualification            | Indicative                                                                          |
| **No. 12** | Burden of proof shifting to counterparty where statute allocates it to drafter                                  | "Customer must prove product was defective on delivery"                       | Generally void in B2B too                                                           |
| **No. 13** | Formal notice requirements for defect claims (Mängelrüge) as condition precedent                                | "Warranty void unless customer inspects within 3 days of delivery" (consumer) | In B2C: void. In B2B: HGB § 377 allows shorter inspection periods between merchants |
| **No. 14** | Subscription contracts entered into by minors                                                                   | Subscription signed by anyone under 18                                        | Void                                                                                |

**2022 Auto-Renewal Amendments (§ 309 No. 9):**
Effective March 1, 2022 (Fair Consumer Contracts Act):

- Maximum initial/renewal term: 2 years (contracts cannot lock consumers in longer)
- Tacit renewal: valid only if contract becomes terminable at any time with 1 month's notice
  (reduced from 3 months under previous law)
- Any auto-renewal clause that still references a 3-month notice period is now void in B2C
- For B2B: the 2022 amendments have indicative effect; courts may find 3-month notice
  periods disproportionate in B2B depending on contract value and sector norms

---

### 4. Conditional Prohibition Catalogue (§ 308)

§ 308 lists clauses that are presumptively void but may be valid if objectively justified
in the specific context. Apply full force in B2C; use as indicative standard in B2B.

| § 308 No. | Prohibited Clause Type                                                                                                           | Justification Required                                                                                   | Common Issues                                                                                  |
| --------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **No. 1** | Unreasonably long acceptance or performance periods (Annahme- und Leistungsfristen)                                              | Must be objectively justified by production, logistics, or service complexity                            | "Delivery within 12 weeks" for off-the-shelf goods                                             |
| **No. 2** | Right to supplementary performance or inspection (Nacherfüllung) that is unreasonably restricted                                 | Must leave reasonable rights intact                                                                      | Restricting cure to "one attempt only" for complex technical goods                             |
| **No. 3** | Unilateral withdrawal/cancellation right (Rücktritts-/Kündigungsrecht) for the drafter without equivalent right for counterparty | Must be objectively justified; must provide compensation                                                 | One-sided termination for convenience with no cure period                                      |
| **No. 4** | Right to change the agreed service (Änderungsvorbehalt)                                                                          | Must have objectively justified reasons; must not be arbitrary; counterparty must have termination right | "We may modify services at any time at our discretion"                                         |
| **No. 5** | Fictitious declarations — silence or inaction treated as acceptance (fingierte Erklärungen)                                      | Clause must specifically draw attention to the significance of silence                                   | "If no objection within 10 days, customer accepts proposed contract modifications"             |
| **No. 6** | Fictitious receipt (fingierter Zugang) — deemed delivery of notices                                                              | Must match reality; cannot create unreasonably early deemed receipt                                      | "Notice sent by first-class post deemed received next business day" where postal delays common |
| **No. 7** | Individual contract clauses presented as if they were general terms                                                              | Cannot use AGB to convert individually negotiated terms back into standardized ones                      |                                                                                                |
| **No. 8** | Obligation to pay despite non-performance                                                                                        | Must have objective justification; must not impose payment where services not rendered                   | "Payment due regardless of whether services are delivered"                                     |

---

### 5. General Good Faith Test (§ 307)

**Application**: Applies to all AGB clauses not covered by §§ 308–309 (and as a backstop
to catch clauses not explicitly listed). Applies to both B2C and B2B, with higher
tolerance in B2B commercial contexts.

**Two-step test:**

**Step 1 — Deviation from statutory model (Leitbildfunktion):**
Does the clause deviate from essential principles of the statutory model that would
otherwise govern? If no deviation, § 307 generally does not apply.

**Step 2 — Unreasonable disadvantage (unangemessene Benachteiligung):**
Does the deviation unreasonably disadvantage the counterparty contrary to good faith
(Treu und Glauben, § 242 BGB)?

Presumption of unreasonableness (§ 307 Abs. 2) arises if:

- Clause deviates from essential statutory principles (Abs. 2 No. 1), OR
- Clause restricts essential contractual rights/obligations so as to endanger the contract
  purpose (Abs. 2 No. 2)

**Transparency requirement (Transparenzgebot, § 307 Abs. 1 S. 2):**
AGB must be clear and comprehensible. Transparency violations independently constitute
unreasonable disadvantage. A clause is non-transparent if it:

- Uses unclear, ambiguous, or contradictory language
- Obscures the counterparty's rights or obligations
- Contains hidden economic burdens not apparent from the clause's face
- Relies on technical jargon without definition
- Presents key limitations in visually subordinate positions (small font, appendices)

**Main performance carve-out (§ 307 Abs. 3):**
Price and main performance obligations (Hauptleistungspflichten) themselves are not subject
to Inhaltskontrolle — parties are free to agree on the price and core service. However,
how those obligations are described and modified by AGB remains subject to § 307.

**B2B good faith test:**
Courts apply § 307 in B2B with "appropriate account of customs and practices in commercial
dealings" (§ 310 Abs. 1 S. 2). Industry custom can justify harsh terms; however,
egregiously one-sided B2B provisions will still fail the § 307 test.

---

### 6. Scope and B2C/B2B Matrix (§ 310)

| Rule                                       | B2C Consumer | B2B Merchant                                                     | Employment                 |
| ------------------------------------------ | ------------ | ---------------------------------------------------------------- | -------------------------- |
| § 305 Abs. 1 (AGB definition)              | ✅ Full      | ✅ Full                                                          | ✅ Full                    |
| § 305 Abs. 2–3 (incorporation formalities) | ✅ Full      | ❌ Does not apply                                                | ✅ Full                    |
| § 305b (Individualabrede priority)         | ✅ Full      | ✅ Full                                                          | ✅ Full                    |
| § 305c (surprising clauses)                | ✅ Full      | ✅ Applies (higher threshold)                                    | ✅ Full                    |
| § 306 (invalidity consequences)            | ✅ Full      | ✅ Full                                                          | ✅ Full                    |
| § 307 (general good faith)                 | ✅ Full      | ✅ Full (with commercial adjustment)                             | ✅ BAG applies analogously |
| § 308 (conditional prohibitions)           | ✅ Full      | ❌ Indicative via § 307                                          | ❌ Indicative via § 307    |
| § 309 (absolute prohibitions)              | ✅ Full      | ❌ Indicative via § 307                                          | ❌ Indicative via § 307    |
| § 309 No. 7a (death/injury)                | ✅ Void      | ✅ Also void (mandatory law)                                     | ✅ Also void               |
| § 309 No. 7b (gross negligence)            | ✅ Void      | ✅ Also void for intentional/gross negligence on material duties | ✅ Also void               |

**Employment AGB (§ 310 Abs. 4):**
Employment contracts are largely exempt from §§ 305 Abs. 2–3, § 308, § 309, but the BAG
applies § 307 analogously to assess unreasonable employee disadvantage. Key employment AGB
issues: excessive confidentiality, disproportionate non-compete, penalty clauses for
resignation, post-contractual restriction enforceability.

---

### 7. Consequences of Invalidity (§ 306)

**Rule**: A void clause is simply void — it is not modified, reduced, or rewritten by
the court.

| Scenario                       | § 306 Consequence                                                                   | Statutory Gap-Fill                                                                             |
| ------------------------------ | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Single clause void             | Contract remains valid; void clause is eliminated                                   | Statutory default law fills the gap (e.g., §§ 433 ff. for sale, §§ 631 ff. for work contracts) |
| Multiple clauses void          | Contract remains valid unless § 306 Abs. 3 applies                                  | Each void clause filled by its relevant statutory default                                      |
| § 306 Abs. 3 threshold reached | Contract may be void in its entirety if retention would cause unzumutbaren Nachteil | Rare; only when cumulative invalidity fundamentally distorts the bargain                       |

**Prohibition of Geltungserhaltende Reduktion:**
German courts **cannot** save an invalid clause by trimming it to a valid kernel. There is
no "blue pencil" rule equivalent. If a clause is void, the court does not, e.g.:

- Reduce a 3-month notice period to the maximum permitted 1 month
- Reduce a disproportionate penalty to a proportionate one
- Narrow a blanket liability exclusion to the permissible scope

**Consequence for drafters**: Draft defensively and precisely. "Savings" clauses (e.g.,
"to the extent permitted by law," "insofar as legally permissible") do not cure invalid
provisions and may themselves violate the Transparenzgebot. See BGH warranty disclaimer
case law (VIII ZR 26/14 [VERIFY]).

**UKlaG enforcement**: If AGB contain void clauses, qualified associations (consumer
groups, chambers of commerce, trade associations) may seek injunctions under UKlaG §§ 1–3
preventing future use. An injunction does not affect already-concluded contracts but
requires immediate removal from future use and can trigger significant reputational and
procedural costs.

---

## Severity Classification

Classify each AGB provision as:

### VALID — Compliant

The clause satisfies all requirements of §§ 305–310. For B2C, it passes the § 309 / § 308
tests. For both B2C and B2B, it passes § 307 and the Transparenzgebot.

**Action**: Note for awareness. No changes required.

### QUESTIONABLE — Risk Identified

The clause may be invalid depending on context (counterparty type, industry practice,
B2B commercial norms) or is ambiguous in its application. The clause may survive a § 307
good faith test in B2B but would fail in B2C, or the outcome depends on facts not
apparent from the AGB text.

**Action**: Flag the risk, explain the relevant test and context-dependent factors, and
provide a compliant alternative. If context is unclear, ask the user (⟁ CLARIFY).

### VOID — Non-Compliant

The clause violates a specific provision of §§ 305–310 and is void under German law. This
includes:

- Clauses that fail § 309 (B2C) or are clearly outside § 307 tolerance (B2C and B2B)
- Clauses that violate the Transparenzgebot under § 307 Abs. 1 S. 2
- Clauses not incorporated into the contract under § 305 Abs. 2
- Savings clauses that attempt to cure other void provisions

**Action**: Identify the specific provision voiding the clause, state the § 306 consequence
(which statutory default fills the gap), and provide corrected language that achieves the
drafter's legitimate purpose within the law.

---

## Actionable Output per Finding

For each QUESTIONABLE or VOID finding, use this format:

```
**Clause**: [Section/number and title]
**Current language**: "[Exact quote]"
**Classification**: [QUESTIONABLE / VOID]
**Applicable provision**: [§ 309 No. X / § 308 No. X / § 307 Abs. Y — reason]
**B2C/B2B relevance**: [Void directly in B2C / Indicative risk in B2B / Applies to both]
**Legal basis**: [Specific BGB provision and rationale — or "[VERIFY]" if from memory]
**Gap-fill if void**: [Which statutory default applies under § 306 Abs. 2]
**Corrected draft**:
> [Specific replacement clause language]
**Fallback** (if primary correction is rejected or impractical):
> [Alternative that reduces but does not eliminate the risk]
**Confidence**: [Level — reasoning]
```

---

## Prioritization Framework

Organize findings by remediation priority:

### Priority 1 — Immediate Fix (Sofortmaßnahme)

Clauses that are void without question and that expose the drafter to UKlaG injunction
risk or material liability:

- § 309 No. 7a/b violations (liability for death, injury, gross negligence)
- § 307 Transparenzgebot violations in consumer-facing AGB published online
- Auto-renewal clauses that still use pre-2022 3-month notice periods (B2C)
- Cancellation button absence in consumer subscription services
- Complete warranty exclusions in sales of new consumer goods (§ 309 No. 8a)
- Savings clauses ("to the extent permitted by law") masking void provisions

### Priority 2 — Fix Before Next Revision (Nächste Revision)

Clauses that carry significant QUESTIONABLE or VOID risk in the primary use context
(B2C), or that are demonstrably void in B2B under § 307:

- Fictitious consent clauses (§ 308 No. 5) — deemed acceptance by silence
- Disproportionate Vertragsstrafe provisions (§ 309 No. 5)
- Broad set-off exclusions (§ 309 No. 2)
- Unreasonably short notice periods for termination
- Burden of proof shifts (§ 309 No. 12)

### Priority 3 — Monitor and Review (Beobachten)

Clauses that are borderline QUESTIONABLE, context-dependent, or carry lower overall risk:

- B2B provisions that may pass § 307 depending on industry custom
- Clauses that are VALID now but may become void after regulatory change
- Mängelrüge formality requirements (§ 309 No. 13) in pure B2B contexts governed by
  HGB § 377 (merchant inspection duties)

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise failures before delivering.

| Gate           | Rule                                                                                                          | Fail Action                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific BGB provision, BGH decision, or established principle                      | Add citation or mark "[UNVERIFIED — Rechtsanwalt to confirm]" |
| **Format**     | BGB citations use "§ [number] Abs. [paragraph] [code name]" format consistently                               | Fix format                                                    |
| **Currency**   | BGB §§ 305–310 provisions checked against post-2022 amendments; BGH decisions checked for overruling          | Flag "[CHECK CURRENCY — may have been amended post-2022]"     |
| **Domain**     | Analysis stays within German law. No assumptions from Austrian, Swiss, or common law systems without flagging | Remove or flag cross-jurisdictional bleed                     |
| **Confidence** | Uncertainty explicitly stated. B2B/B2C borderlines flagged. BGH-unsettled questions noted                     | Add confidence qualifier                                      |

### Self-Interrogation for VOID Findings

For any VOID classification, apply this 3-pass self-interrogation before delivering:

**Pass 1 — Legal Chain Integrity:**

- Does the void classification follow logically from the cited BGB provision?
- Would a German court (LG / OLG / BGH) actually reach this conclusion on these facts?
- Is there a plausible argument that the clause is Individualabrede, not AGB?
- What is the strongest counterargument (e.g., industry custom justifying the provision)?

**Pass 2 — Completeness:**

- Have §§ 307, 308, and 309 all been considered in sequence?
- Has the B2C/B2B classification been applied correctly to determine which provisions apply?
- Has the Transparenzgebot been checked independently?
- Are the § 306 consequences fully analyzed (which statutory default fills the gap)?

**Pass 3 — Challenge:**

- What is the strongest argument that this clause IS valid?
- Under B2B norms in this industry, would a German court apply a higher tolerance?
- Is the VOID classification proportionate, or is this actually QUESTIONABLE with
  mitigations available?

If any pass reveals a weakness, revise the analysis. Mark the audit trail with
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                                                        | Action                                                     |
| ------------ | --------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled BGH case law, clear BGB text, no ambiguity                             | State with confidence                                      |
| **High**     | 0.80–0.94 | Strong authority, minor interpretation questions                               | State with brief caveat                                    |
| **Probable** | 0.60–0.79 | Good arguments but B2B/B2C context-dependent or BGH has not squarely addressed | State with explicit reasoning and contra-indicators        |
| **Possible** | 0.40–0.59 | Genuinely uncertain, competing OLG decisions or unsettled industry practice    | Flag for Rechtsanwalt with both sides                      |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                                                        | Do not assert; flag "[UNCERTAIN — Rechtsanwalt to advise]" |

---

## Glass Box Audit Trail

Every AGB review output MUST include a Glass Box audit section at the end:

```yaml
glass_box:
  skill: "legalcode-de-agb-review"
  governing_law: "BGB §§ 305–310 (German law)"
  party_type: "[B2C / B2B / Employment / Mixed]"
  contracting_channel: "[Online / Paper / Framework / Unknown]"
  sector: "[IT / Retail / Financial / Employment / General / Other]"
  review_purpose: "[Audit / Remediation / Pre-publication / Dispute]"
  clauses_analyzed: "[number]"
  valid_clauses: "[number]"
  questionable_clauses: "[number]"
  void_clauses: "[number — list]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  bgb_provisions_cited:
    - "§ 305 Abs. 2 — [VERIFIED / UNVERIFIED]"
    - "§ 307 Abs. 1 S. 2 (Transparenzgebot) — [VERIFIED / UNVERIFIED]"
    - "§ 309 No. [X] — [VERIFIED / UNVERIFIED]"
  bgb_currency_checked: "[Yes — post-2022 amendments verified / No — manual check required]"
  bgh_decisions_cited:
    - "[Case — VERIFIED / UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no VOID findings)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  uklag_exposure: "LOW / MEDIUM / HIGH — [summary]"
  limitations:
    - "B2B findings are context-dependent on industry custom — verify with sector specialist"
    - "Employment AGB require BAG jurisprudence analysis not fully covered in this review"
    - "UKlaG risk assessment is indicative only — not a substitute for enforcement counsel"
  reviewer: "AI-assisted — requires qualified Rechtsanwalt review before reliance"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in AGB review:

1. **Conflating B2C and B2B rules** — §§ 308–309 apply directly only in B2C. Applying them
   directly to a B2B contract overstates the case; failing to apply them indicatively
   understates it. Always state the B2C/B2B classification and its effect on the analysis.

2. **Using savings clauses to cure invalid provisions** — "To the extent permitted by law"
   does not validate an otherwise void clause. Under BGH case law, such phrases may
   independently violate the Transparenzgebot (§ 307 Abs. 1 S. 2). Flag them as VOID,
   not as a mitigant.

3. **Attempting Geltungserhaltende Reduktion** — Never suggest trimming an invalid clause
   to a permissible range. The court cannot do it; do not imply the drafter can either.
   Provide a fully rewritten compliant clause instead.

4. **Treating HGB § 377 inspection duties as AGB** — In pure B2B sale-of-goods contracts
   between merchants, HGB § 377 (immediate inspection and complaint duty) imposes
   Mängelrüge obligations by statute. These are not AGB provisions; they apply regardless
   of whether they appear in the contract.

5. **Overlooking the 2022 auto-renewal amendments** — Many AGB still contain pre-2022
   3-month notice periods for tacit renewal (§ 309 No. 9). These are now void in B2C.
   Check auto-renewal clauses first — this is a common, immediately actionable issue.

6. **Applying § 305 Abs. 2 incorporation formalities to B2B** — The enhanced incorporation
   requirements of § 305 Abs. 2–3 are disapplied in B2B by § 310 Abs. 1. Flagging them
   as failures in B2B contracts is incorrect. Instead, assess whether any notice at all
   was given.

7. **Ignoring § 305c in B2B** — The surprising clause prohibition (§ 305c) applies to B2B
   contracts, though at a higher threshold. Do not skip this analysis for B2B — arbitration
   clauses, complete liability exclusions, and one-sided assignment rights remain
   potentially surprising even for merchants.

8. **Confusing Vertragsstrafe (§ 309 No. 5) with liquidated damages** — German law treats
   penalty clauses (Vertragsstrafe) differently from liquidated damages clauses. A
   Vertragsstrafe must be proportionate (§ 343 BGB allows reduction by court in B2B
   [VERIFY]). The prohibition in § 309 No. 5 is B2C-direct; in B2B, disproportionate
   penalties still fail the § 307 test.

9. **Relying on § 306 Abs. 3 (whole contract void) too readily** — The threshold for
   voiding an entire contract under § 306 Abs. 3 is very high. Individual void clauses
   are replaced by statutory defaults; only extreme cumulative invalidity that
   fundamentally distorts the deal warrants § 306 Abs. 3 analysis.

10. **Skipping the Transparenzgebot analysis** — The transparency requirement under § 307
    Abs. 1 S. 2 is an independent ground for invalidity, separate from § 309 and § 308.
    A clause that is substantively valid can still be void if it is unclear, ambiguous,
    hides economic burdens, or uses technical jargon without definition. Always run this
    check on every clause, not just when substance fails.

11. **Treating the ambiguity rule (§ 305c Abs. 2) as a last resort** — Contra proferentem
    applies after all normal interpretation methods are exhausted, not before. Do not
    jump to "interpreted against the drafter" without first applying §§ 133, 157 BGB
    interpretation standards.

12. **Ignoring UKlaG exposure** — An invalid AGB clause is not merely an academic issue.
    Qualified associations can seek injunctions under UKlaG § 1. In B2C online contexts,
    public-facing AGB with void clauses represent actionable enforcement targets. Always
    assess and communicate this risk.

13. **Missing sector-specific special rules** — Employment AGB (BAG jurisprudence differs
    materially from general BGB AGB control), public IT procurement (EVB-IT), banking
    (BaFin / AGB-Banken / AGB-Sparkassen), and construction (VOB/B) each have additional
    layers that override or supplement §§ 305–310. Never analyze sector-specific AGB
    without checking for these overlays.

14. **Conflating Austrian or Swiss AGB law with German law** — Austrian UGB/KSchG and
    Swiss OR have AGB control frameworks that differ from BGB §§ 305–310. When a contract
    involves Austrian or Swiss parties, note the jurisdictional limitation explicitly and
    recommend jurisdiction-specific review.

15. **Generating redlines without understanding the drafter's legitimate purpose** — Every
    void clause usually exists because the drafter had a legitimate commercial interest
    they tried (and failed) to protect. Corrected language must satisfy that interest
    within the law. "Delete clause" without an alternative is not useful guidance.

---

## Writing Standards

Apply these discipline standards to all output from this skill:

**For correction drafts (shared with legal team or counterparties):**

- Precise German legal terminology with English translation in brackets on first use
- Active voice: "Der Verwender haftet nicht..." not "Haftung wird ausgeschlossen..."
- One obligation or right per sentence
- Define technical terms on first use; use consistently thereafter
- Name the specific BGB provision authorizing each corrected clause where relevant

**For analysis narrative:**

- Plain language alongside legal terms
- State the specific provision (e.g., "§ 309 No. 7b BGB") not just a general reference
- Distinguish between "void in B2C" and "indicative risk in B2B" explicitly
- Confidence qualifiers on every contested legal claim
- Short paragraphs; use tables for structured comparisons

**Quality gates before delivery:**

1. Does every VOID classification cite a specific BGB provision?
2. Is the B2C/B2B distinction applied correctly and consistently throughout?
3. Does every corrected clause achieve the drafter's legitimate purpose while complying
   with §§ 305–310?
4. Are all BGH citations verified or marked [VERIFY]?
5. Is the Glass Box audit trail complete and filled in?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- Search for the current text of BGB §§ 305–310 (verify 2022 amendments incorporated)
- Search for BGH decisions on § 307 Transparenzgebot, § 309 No. 7, and § 309 No. 9
- Search for relevant OLG decisions on sector-specific AGB issues
- Search for UKlaG enforcement actions in the relevant industry
- Save results to `/tmp/legalcode-agb-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with analysis using BGB provisions from memory
- Mark all BGH and OLG case citations [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Include prominent notice that case law has not been independently verified
- Focus on structural issues and clear statutory violations rather than nuanced case law

---

## Localization Notes

**Austrian law (ABGB / KSchG / UGB):**
Austria has its own AGB control framework under the Konsumentenschutzgesetz (KSchG) for
B2C and UGB for B2B. While concepts are similar (unfair terms, transparency, prohibition
lists), specific rules, list provisions, and case law differ. This skill is not for
Austrian-law contracts. [VERIFY with Austrian-qualified counsel]

**Swiss law (OR Art. 8):**
Switzerland's AGB control under OR Art. 8 is significantly less prescriptive than German
law. No equivalent of § 309 absolute prohibition list exists. German AGB standards cannot
be mapped directly onto Swiss contracts. [VERIFY with Swiss-qualified counsel]

**EU cross-border context:**
For German consumers, EU Directive 93/13/EEC is the minimum floor; German law provides
stronger protection. For B2B contracts in Germany with EU counterparties, German law
applies if German law governs (Rome I Regulation choice-of-law). For non-EU counterparties,
note that German AGB control may apply even if a foreign law is chosen, where the
connection to Germany is substantial (BGH VIII ZR 7/23 [VERIFY]).

---

## Output Format Template

Structure the final AGB review as:

```markdown
## AGB Review Summary

**AGB title/document**: [name or description]
**Party type**: [B2C / B2B / Employment / Mixed]
**Contracting channel**: [Online / Paper / Framework]
**Sector**: [if relevant]
**Review purpose**: [Audit / Remediation / Pre-publication / Dispute]
**Date of review**: [date]
**Governing law confirmed**: [Yes — German law / Assumed — German law]

---

## Key Findings

[Top 3–5 issues with VOID/QUESTIONABLE flags and one-line summaries]

---

## Incorporation Assessment (§ 305)

| Requirement              | Status                | Issue             |
| ------------------------ | --------------------- | ----------------- |
| Express reference        | MET / UNMET / UNCLEAR | [detail if unmet] |
| Opportunity to take note | MET / UNMET / UNCLEAR | [detail]          |
| Counterparty agreement   | MET / UNMET / UNCLEAR | [detail]          |

---

## Clause-by-Clause Analysis

### [Clause Title] — [VALID / QUESTIONABLE / VOID] | Confidence: [level]

**Current language**: "[quote]"
**Applicable provision**: [§ X No. Y BGB / § 307 reason]
**Analysis**: [explanation of the issue]
**B2C/B2B note**: [how context affects the classification]
**§ 306 consequence** (if VOID): [which statutory default applies]
**Corrected draft**:

> [replacement clause]
> **Fallback**: [alternative if primary correction is rejected]

[Repeat for each clause]

---

## Overall Assessment

**AGB risk rating**: [LOW / MEDIUM / HIGH]
**Void clauses**: [count and list]
**Questionable clauses**: [count]
**UKlaG exposure**: [LOW / MEDIUM / HIGH — brief reasoning]

## Recommended Actions

### Priority 1 — Immediate Fix

- [clause] — [one-line reason]

### Priority 2 — Fix Before Next Revision

- [clause] — [one-line reason]

### Priority 3 — Monitor

- [clause] — [one-line reason]

---

## Glass Box Audit Trail

[YAML block as defined in Glass Box Audit Trail section]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

- BGB §§ 305–310 as amended through the Fair Consumer Contracts Act (2021/2022)
- BGH jurisprudence on AGB validity, Transparenzgebot, and § 309 prohibitions
- EU Directive 93/13/EEC (minimum harmonization baseline)
- Taylor Wessing, Noerr, and dejure.org commentary on German AGB law
- Legalcode gold standard quality framework modeled on `legalcode-contract-review`

All statutory and BGH citations should be verified against authoritative sources
(gesetze-im-internet.de, dejure.org, juris.bundesgerichtshof.de) before reliance.
