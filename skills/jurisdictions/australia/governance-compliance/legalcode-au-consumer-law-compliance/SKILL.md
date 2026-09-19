---
name: legalcode-au-consumer-law-compliance
description: 'Assess compliance with the Australian Consumer Law (ACL) — Schedule 2 of the Competition
  and Consumer Act 2010 (Cth). Covers misleading or deceptive conduct (s 18), false representations (s
  29), unconscionable conduct (ss 20–22), consumer guarantees (ss 51–64A), unfair contract terms (ss 23–28)
  including the expanded civil penalty regime effective 9 November 2023 (up to $50 million per contravention),
  product safety obligations (ss 104–140), and ACCC enforcement risk profiling. Generates COMPLIANT /
  PARTIAL / NON-COMPLIANT findings with CRITICAL / HIGH / MEDIUM / LOW risk tiers, clause-level remediation
  language, and a compliance roadmap. Use when auditing terms and conditions, returns/refund policies,
  marketing and advertising materials, subscription contracts, warranty documentation, standard form agreements,
  or any consumer-facing practice for ACL compliance. Jurisdiction: Australia (national — all states and
  territories). Enforced by ACCC and state/territory consumer protection agencies.'
metadata:
  jurisdiction: Australia
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode — Australian Consumer Law Compliance Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted Australian Consumer Law
> compliance assessment. It does not constitute legal advice. All outputs require review by
> an Australian-qualified lawyer before reliance, particularly in relation to enforcement
> risk, specific penalty exposure, and remediation strategies. The ACL is administered by
> the ACCC and state/territory consumer protection agencies; enforcement priorities and
> guidance evolve continuously. Verify current applicability of all statutory provisions,
> penalty thresholds, and case law against authoritative sources (Federal Register of
> Legislation, Federal Court of Australia, ACCC publications) before acting. Statutory and
> case law references cited from memory carry hallucination risk — mark all citations with
> [VERIFY] unless independently confirmed against authoritative sources.

---

## Purpose and Scope

This skill assesses business practices, contracts, and consumer-facing materials for
compliance with the Australian Consumer Law (ACL). The ACL is Schedule 2 of the
Competition and Consumer Act 2010 (Cth) — a single national consumer protection law
that applies in all Australian states and territories.

**Covers:**

- Misleading or deceptive conduct (ACL s 18) and specific false representations (s 29)
- Unconscionable conduct — statutory (ACL ss 20–22) and the 12-factor test
- Consumer guarantees — 9 guarantees for goods (ss 51–60), 4 for services (ss 61–63)
- Returns/refund policy compliance and major vs. minor failure classification
- Unfair contract terms — standard form contract screening (ss 23–28) including the
  9 November 2023 civil penalty expansion (up to $50M per contravention)
- Product safety obligations — standards, bans, and recall duties (ss 104–140)
- ACCC enforcement risk profiling — enforcement priorities 2024–2026
- COMPLIANT / PARTIAL / NON-COMPLIANT classification with CRITICAL / HIGH / MEDIUM / LOW
  risk tiers
- Clause-level remediation with revised draft language
- Compliance program gap assessment

**Does not:**

- Provide legal advice or replace qualified Australian consumer law counsel
- Cover competition law provisions of the Competition and Consumer Act 2010 (Part IV)
- Cover the Australian Privacy Act 1988 (Cth) or Notifiable Data Breach scheme
  (see `australia-privacy-act-ndb-breach-notification-operations`)
- Cover the Franchising Code of Conduct 2025
  (see `legalcode-franchise-agreement-review-au`)
- Cover ASIC-regulated financial products (overlap with AFSL obligations and ASIC Act)
- Cover state-specific retail, real estate, or tenancy legislation beyond ACL scope
- Cover the Oil Code of Conduct or other industry-specific mandatory codes

**Related skills:**

- `legalcode-franchise-agreement-review-au` — Franchising Code + ACL for franchise agreements
- `australia-privacy-act-ndb-breach-notification-operations` — Privacy Act + NDB scheme
- `legalcode-contract-review` — General commercial contract review

---

## Jurisdiction and Governing Law

### Why the ACL Requires a Dedicated Compliance Skill

The Australian Consumer Law has several features that distinguish it from general
commercial contract law and from other consumer protection regimes:

1. **National statute**: The ACL applies uniformly in all states and territories as
   Schedule 2 of the Competition and Consumer Act 2010 (Cth). State-based consumer
   protection laws largely mirror the ACL. All references are to the Commonwealth Act
   unless stated otherwise.

2. **No-fault misleading conduct**: ACL s 18 is strict liability — no mental element is
   required. A business can be found liable for misleading conduct regardless of intent.

3. **Non-excludable guarantees**: Consumer guarantees cannot be contracted out of, modified,
   or excluded. Any clause attempting to do so is void (ACL s 64). This renders a large
   class of standard warranty disclaimers legally ineffective in Australia.

4. **Unfair contract terms penalties since November 2023**: The Treasury Laws Amendment
   (More Competition, Better Prices) Act 2022 expanded UCT coverage and, from 9 November
   2023, made unfair terms in standard form contracts a civil penalty provision for the
   first time — penalties up to $50 million per contravention for body corporates.

5. **Active regulator**: The ACCC has a demonstrated enforcement track record —
   Mazda Australia ($11.5M, 2024), Clorox ($8.25M, 2025), Coles/Woolworths (ongoing,
   2024–2026). In FY2024, total consumer/codes enforcement penalties exceeded $500M.

6. **Consumer threshold**: The ACL applies to goods/services acquired primarily for
   personal, domestic, or household use, or goods/services valued at $100,000 or less
   [VERIFY current threshold — proposals to raise]. Small business contracts (≤20
   employees [VERIFY current definition]) are covered by the UCT regime.

### State/Territory Overlay

The ACL is uniform nationally. Some state/territory variations apply:

- **Cooling-off periods**: Some states provide additional cooling-off periods beyond
  ACL minimums for door-to-door sales and certain services [JURISDICTION-SPECIFIC]
- **Real estate and motor vehicles**: State-based licensing regimes overlay ACL standards
- **Tenancy**: Residential tenancy is primarily state-regulated, though ACL UCT regime
  applies to standard form residential tenancy agreements

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer would change the scope or depth of the assessment
- Multiple valid compliance approaches exist
- Business context is needed to classify risk correctly
- The assessment scope is ambiguous (contract terms vs. advertising vs. operational practices)

Use the **⟁ CLARIFY** pattern wherever marked below. If the user has already provided the
information, skip the question and proceed.

---

## Workflow

### Step 1: Accept the Input

Accept any of the following:

- **Documents**: Terms and conditions, return/refund policy, warranty document,
  subscription agreement, standard form contract, marketing materials, product labels
- **File uploads**: PDF, DOCX, plain text, or other formats
- **Pasted text**: Content pasted directly into the conversation
- **URL**: Link to a live webpage or document (if permitted by the user's tool permissions)
- **Description**: A verbal description of a business practice, policy, or contract term

If no input is provided, prompt the user to supply one.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the assessment, ask the user:

1. **Assessment scope**: What needs to be assessed?
   - Options: Full ACL audit (all six pillars), Targeted review (specific ACL area),
     Specific document review (T&Cs / returns policy / warranty / marketing / contract),
     Pre-launch compliance check, Post-ACCC inquiry response
   - _Why this matters_: Determines which of the six ACL pillars to prioritise.

2. **Business type and sector**: What kind of business?
   - Options: Online retail / e-commerce, Bricks-and-mortar retail, SaaS / digital services,
     Manufacturing / consumer products, Professional services, Food and beverage,
     Financial services (note: ASIC overlap), Automotive, Other (specify)
   - _Why this matters_: Different sectors face different ACL enforcement priorities and
     have different exposure patterns under each pillar.

3. **Consumer vs. B2B**: Who are the customers?
   - Options: Primarily consumers (B2C), Primarily businesses (B2B), Both
   - _Why this matters_: Consumer guarantees (ss 51–64A) apply to consumer acquisitions.
     UCT (ss 23–28) applies to both consumer and small business contracts. Misleading
     conduct (s 18) applies to all trade or commerce.

4. **Standard form contracts**: Does the business use standard form contracts
   (contracts presented on a take-it-or-leave-it basis)?
   - Options: Yes, No, Unsure
   - _Why this matters_: Activates the unfair contract terms pillar with November 2023
     civil penalties.

5. **Known concerns**: Are there specific ACCC concerns or known compliance gaps?
   - Free text. Examples: recent ACCC inquiry, complaint pattern, product recall,
     upcoming contract renewal, new marketing campaign, post-merger compliance review.
   - _Why this matters_: Focuses the assessment on the highest-risk areas first.

If the user provides partial context, proceed with reasonable assumptions and state them
explicitly. Do not silently assume.

### Step 3: Gather Legal Authority

Use **legalcode-mcp** to build a working reference file for this assessment.

**Search for:**

- Current ACL statutory text (Competition and Consumer Act 2010, Schedule 2)
- Penalty amounts (current — indexed annually under CCA s 314ZJ [VERIFY])
- ACCC enforcement actions in the relevant sector (last 3 years)
- Consumer guarantee guidance documents published by the ACCC
- UCT guidance — ACCC's unfair contract terms compliance guide
- Product safety standards applicable to the business's product categories
- Relevant Federal Court decisions on s 18, UCT, or consumer guarantees

**Save results** to `/tmp/legalcode-au-acl-authority.md`.

**If legalcode-mcp is not connected:**

- Mark all statutory provisions [VERIFY]
- Mark all case citations [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed using the legal framework in this skill, flagging all references for independent
  verification

**⟁ CLARIFY** — If the business sector is regulated by ASIC (financial services, credit,
insurance), ask the user whether the assessment should also flag ASIC Act s 12DA
(misleading conduct in financial services) and AFSL-specific compliance obligations, or
whether the scope should be limited to ACL only.

### Step 4: Misleading or Deceptive Conduct Assessment (ACL ss 18, 29)

Assess the business's consumer-facing representations, advertising, product descriptions,
pricing displays, and contract terms against the ACL s 18 standard.

**Core test** (ACL s 18): Conduct is prohibited if, judged objectively from the perspective
of the hypothetical reasonable consumer in the target market, it is misleading or deceptive
or is _likely_ to mislead or deceive. No fault is required.

**Apply this test to each representation identified:**

| Category                             | What to Review                                                  | Common Failures                                                                    |
| ------------------------------------ | --------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Pricing and discounts**            | "Was/now" claims, percentage discounts, "from" prices, specials | Artificial price inflation before discount; "from" price unavailable; drip pricing |
| **Product quality and description**  | Features, materials, origin, condition                          | Overstating specifications; "new" for refurbished; false country of origin         |
| **Service capabilities**             | Uptime claims, delivery timelines, performance guarantees       | Unsubstantiated performance claims; misleading delivery timeframes                 |
| **Environmental and sustainability** | "Natural," "eco-friendly," "recycled," "carbon neutral"         | Unsubstantiated claims; misleading percentages (Clorox $8.25M, 2025)               |
| **Warranties and guarantees**        | Warranty scope, exclusions, comparison with ACL                 | Implying warranty replaces ACL rights; misrepresenting guarantee scope             |
| **Testimonials and endorsements**    | Authenticity, disclosure of commercial relationships            | Fake reviews; paid endorsements without disclosure                                 |
| **Digital practices**                | Privacy disclosures, data collection, subscription terms        | Misleading tracking disclosures (Google LLC v ACCC [2023] HCA 1 [VERIFY])          |
| **ACL rights**                       | Representations about consumer rights and remedies              | Stating "no refunds" or "refunds at our discretion" as absolute                    |

**⟁ CLARIFY** — For pricing claims ("was/now", discounts, "save X%"), ask:

- What was the actual previous selling price and for how long was it offered?
- Is there substantiation (sales records, pricing logs) for the claimed "original" price?
  A key ACCC enforcement focus is discount claims unsupported by genuine prior pricing
  (Coles & Woolworths proceedings, commenced September 2024 [VERIFY final outcome]).

**For ACL s 29 false representations**, check specifically for representations about:

- Standard, quality, value, grade, composition, style, model of goods (s 29(1)(a))
- Whether goods are new (s 29(1)(b)) — "new" cannot describe refurbished or used goods
- Sponsorship, approval, or affiliation (s 29(1)(h)) — endorsements and certifications
- Price including savings claims (s 29(1)(i)) — must reflect genuine prior price
- Availability of repair facilities or spare parts (s 29(1)(j))
- Place of origin (s 29(1)(k)) — "Australian Made" claims require substantiation
- The existence, exclusion, or effect of any ACL guarantee, right, or remedy (s 29(1)(m))

Classify each representation identified:

- **COMPLIANT**: Accurate, not likely to mislead a reasonable consumer
- **PARTIAL**: Some elements accurate but qualifications inadequate, or minor misleading
  component present
- **NON-COMPLIANT**: Likely to mislead or deceive a reasonable consumer, or false per s 29

### Step 5: Consumer Guarantees Audit (ACL ss 51–64A)

Assess the business's warranty documentation, returns/refund policy, and complaint
handling practices against the non-excludable consumer guarantees.

#### 5a. Guarantees Applicability Check

Confirm whether consumer guarantees apply:

- Does the business supply goods or services to "consumers" (personal/household use, or
  value ≤ $100,000 [VERIFY current threshold])?
- For UCT-covered B2B contracts: are small business customers (≤ 20 employees [VERIFY])
  covered by guarantees in the relevant context?

#### 5b. Guarantees for Goods (ACL ss 51–60)

Check that the business's warranty documents, website policies, and sales practices
accurately reflect (and do not contradict) these non-excludable guarantees:

| #   | Guarantee                     | ACL Section | Key Standard                                                                                                        | Common Violation                                                                                                                |
| --- | ----------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Acceptable quality            | s 54        | Safe, durable, free from defects, fit for purpose, acceptable appearance — judged against nature and price of goods | Implying only manufacturer's defect period applies; denying defect claims for goods failing within reasonable durability period |
| 2   | Fitness for disclosed purpose | s 55        | Fit for any purpose made known to the supplier                                                                      | Disclaiming fitness warranty where purpose was explicitly stated                                                                |
| 3   | Match description             | s 56        | Goods correspond to description in contract or advertising                                                          | Goods materially differ from online listing description                                                                         |
| 4   | Match sample or demonstration | s 57        | Goods match sample shown and are free from defects                                                                  | Display model differs materially from supplied goods                                                                            |
| 5   | Express warranties            | s 59        | Goods comply with all express representations made                                                                  | Written warranty terms stricter than representations made in advertising                                                        |
| 6   | Title                         | s 51        | Supplier has right to sell and transfers good title                                                                 | Second-hand goods supplied with undisclosed encumbrances                                                                        |
| 7   | Undisturbed possession        | s 52        | Consumer's possession not disturbed by third party                                                                  |                                                                                                                                 |
| 8   | No undisclosed security       | s 53        | No security, charge, or encumbrance undisclosed                                                                     |                                                                                                                                 |
| 9   | Repair and spare parts        | s 58        | Repairs and spare parts reasonably available for reasonable period                                                  | Stating parts availability cannot be guaranteed; post-model-discontinuation duties                                              |

#### 5c. Guarantees for Services (ACL ss 61–63)

| #   | Guarantee                     | ACL Section | Key Standard                                            |
| --- | ----------------------------- | ----------- | ------------------------------------------------------- |
| 1   | Due care and skill            | s 61        | Services performed with reasonable care and skill       |
| 2   | Fitness for disclosed purpose | s 62        | Services fit for any purpose made known to the supplier |
| 3   | Reasonable time               | s 63        | Completed within a reasonable time if no time agreed    |

#### 5d. Returns and Refund Policy Review

Assess the business's returns/refund policy against ACL requirements:

**Required elements:**

- [ ] Statement that ACL guarantees cannot be excluded or modified
- [ ] No artificial time limits presented as cutting off ACL rights
- [ ] Major failure = consumer's choice of refund OR replacement
- [ ] Minor failure = supplier's choice of repair, replacement, or refund (supplier may
      choose repair for minor failures; consumer cannot demand refund for minor failure
      if repair is offered in reasonable time)
- [ ] No restocking fees, return shipping fees, or administrative charges for defective goods
- [ ] No exclusion for sale items, opened items, or made-to-order goods
- [ ] Refund must be monetary (not store credit only) where consumer elects refund
- [ ] Contact details for complaints clearly provided
- [ ] Mandatory warranty text included if warranty document supplied:
      _"Our goods come with guarantees that cannot be excluded under the Australian Consumer
      Law. You are entitled to a replacement or refund for a major failure and compensation
      for any other reasonably foreseeable loss or damage. You are also entitled to have the
      goods repaired or replaced if the goods fail to be of acceptable quality and the failure
      does not amount to a major failure."_ [VERIFY current mandatory text — check ACCC guidance]

**⟁ CLARIFY** — For consumer electronics, appliances, or goods with known durability
expectations, ask: What is the typical advertised product life or warranty period offered?
This directly affects when a failure constitutes a "major failure" under acceptable
quality (ACL s 54).

#### 5e. Major vs. Minor Failure Classification

A **major failure** exists where goods:

- Would not have been acquired by a reasonable consumer who knew of the problem
- Are substantially unfit for their normal purpose and cannot be rectified in a reasonable
  time
- Are unsafe (ACCC v Mazda Australia — Mazda's repeated failed repairs constituted major
  failure obligating refund/replacement, not merely further repair [VERIFY full holding])
- Do not match a description or sample in a fundamental respect

A **minor failure** exists where the issue is capable of being rectified in reasonable time
and does not render the goods substantially unfit for purpose.

Apply classification for each complaint handling scenario reviewed.

### Step 6: Unfair Contract Terms Screening (ACL ss 23–28)

Screen standard form contracts, subscription agreements, and online terms for unfair
terms under the post-9 November 2023 regime.

**⟁ CLARIFY** — Before proceeding, confirm:

1. Are these contracts presented on a standard form basis (take-it-or-leave-it)?
   Note: ACL s 23(2A) creates a rebuttable presumption of standard form if one party
   drafted the contract and the other had no genuine opportunity to negotiate.
2. Are the customers consumers or small businesses (< $10M turnover or < 100 employees
   in wholesale trade [VERIFY current thresholds])?
3. Have these contracts been reviewed since 9 November 2023?

**The three-limb unfairness test** (ACL s 24):
A term is unfair if **all three** apply:

1. It would cause a significant imbalance in the parties' rights and obligations
2. It is not reasonably necessary to protect the legitimate interests of the party who
   would benefit from the term
3. It would cause detriment (financial or otherwise) to the other party if applied

**Safe harbours — terms exempt from UCT regime** (ACL s 26):

- Terms that define the main subject matter of the contract (what is being bought)
- Terms that set the upfront price payable (but NOT fees triggered during the contract,
  early termination fees, or add-on charges)
- Terms required or expressly permitted by a Commonwealth, State, or Territory law

**Screen for these categories of potentially unfair terms** (s 25 examples):

| Category                          | Potentially Unfair Term Pattern                                                        | Risk Level |
| --------------------------------- | -------------------------------------------------------------------------------------- | ---------- |
| **Unilateral variation**          | Supplier can vary price, scope, or terms without consent or notice                     | CRITICAL   |
| **Automatic renewal traps**       | Auto-renewal without prior reminder; cancellation by phone-only when signup was online | CRITICAL   |
| **Excessive cancellation fees**   | Early termination fees not linked to genuine pre-estimate of loss                      | HIGH       |
| **Asymmetric termination rights** | Supplier can terminate for convenience; consumer cannot                                | HIGH       |
| **Broad liability exclusions**    | Excluding liability for negligence or breach of essential obligations                  | HIGH       |
| **Unilateral dispute resolution** | Mandatory arbitration for consumer; supplier may litigate                              | HIGH       |
| **One-sided indemnities**         | Consumer indemnifies supplier for supplier's own acts                                  | HIGH       |
| **Forfeiture on breach**          | All payments forfeited for minor breach                                                | HIGH       |
| **Automatic waiver of rights**    | Upfront waiver of all statutory rights including ACL guarantees (void under s 64)      | CRITICAL   |
| **Irrevocable consent**           | Blanket consent to all future data uses                                                | MEDIUM     |

**⟁ CLARIFY** — For cancellation fees and early termination charges, ask:
What is the commercial basis for the fee? Is there documentation showing how the fee was
calculated (genuine pre-estimate of loss basis)? The distinction between a legitimate
fee and a penalty/unfair term turns on proportionality and genuine loss basis.

For each term identified, determine:

- Which limb(s) of the three-limb test it may satisfy
- Whether any safe harbour applies
- Civil penalty exposure: up to $50M per contravention (body corporate); $2.5M (individual)
- Remediation: draft compliant alternative term

### Step 7: Unconscionable Conduct Review (ACL ss 20–22)

Assess whether any business practices, sales conduct, or exercise of contractual rights
constitutes unconscionable conduct.

**Two-tier structure:**

- **ACL s 20**: General unconscionability — applying to all persons in trade or commerce
- **ACL s 21**: Consumer or small business unconscionability — lower threshold for
  establishing the conduct was unconscionable

**The 12-factor test** (ACL s 22) — consider (non-exhaustive):

1. Relative bargaining strength of the parties
2. Whether conditions were imposed that were not reasonably necessary to protect
   the legitimate interests of the advantaged party
3. Whether the disadvantaged party could understand documents relevant to the transaction
4. Whether independent advice was available to the disadvantaged party
5. Whether the terms were reasonably disclosed before or at the time of execution
6. Whether the advantaged party used undue influence, pressure, or unfair tactics
7. The amount paid for the goods or services relative to the market
8. Whether the contract was offered on a non-negotiable basis
9. The extent to which the parties acted in good faith
10. Whether the conduct exploited a known special vulnerability of the other party
11. The conduct of the parties after the agreement was reached
12. Any industry code or regulator guidance applicable to the conduct

**Focus areas for business review:**

- Sales practices targeting vulnerable consumers (elderly, non-English-speaking, urgent need)
- Warranty denial practices post-ACL guarantee entitlement (Mazda case pattern)
- Terms exercise against parties in severe financial hardship or distress
- High-pressure sales tactics in home or door-to-door context
- Franchise or supply relationship power imbalances

Apply classification:

- **COMPLIANT**: No indicators of unconscionable conduct in reviewed practices
- **PARTIAL**: Some practices raise concern under one or more s 22 factors; monitoring
  recommended
- **NON-COMPLIANT**: Practice is likely to satisfy the unconscionability test; remediation required

### Step 8: Product Safety Compliance (ACL ss 104–140)

_Apply this step only if the business supplies physical goods to consumers._

**⟁ CLARIFY** — Ask: Does the business supply physical goods to consumers? If yes, are any
products imported, manufactured, or in regulated product categories (electrical, toys,
children's products, flammable garments, sunglasses, motorcycles, helmets)?

**Product safety obligations checklist:**

| Obligation                  | ACL Section   | Requirement                                                                                                       | Check |
| --------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------- | ----- |
| General safety provision    | s 104         | Must not supply goods that create a significant risk of death, serious injury/illness, or property damage         | [ ]   |
| Safety standards compliance | ss 118–119    | Goods must comply with mandatory AS/NZS safety standards applicable to the product category                       | [ ]   |
| Safety bans compliance      | ss 120–121    | Goods must not be subject to an ACCC safety ban                                                                   | [ ]   |
| Product safety reporting    | s 131         | Must notify the ACCC as soon as practicable if aware goods have caused or may cause death, serious injury/illness | [ ]   |
| Recall cooperation          | ss 126–139    | Must cooperate with ACCC recall directions; must notify consumers and provide remedy                              | [ ]   |
| Importer obligations        | [CCA general] | Importers are treated as suppliers for safety purposes; responsible for imported goods' compliance                | [ ]   |

**For each regulated product category, verify:**

- Applicable mandatory standard (check ACCC Product Safety website [VERIFY current standards])
- Certification and testing documentation
- Labelling requirements
- ACCC product recalls register — check whether any similar product is recalled

Classify:

- **COMPLIANT**: All applicable standards met; notification and recall procedures in place
- **PARTIAL**: Some standards met; gaps in documentation or procedures
- **NON-COMPLIANT**: Material non-compliance with applicable safety standard or ban

### Step 9: ACCC Enforcement Risk Assessment

Synthesise the findings from Steps 4–8 into an overall ACCC enforcement risk profile.

**ACCC enforcement priorities 2025–2026** (for risk weighting):

| Priority Area                                       | Risk Weighting                                                  |
| --------------------------------------------------- | --------------------------------------------------------------- |
| Consumer guarantees — misrepresentation and denial  | HIGH — active enforcement (Mazda $11.5M, 2024)                  |
| Pricing misrepresentations ("was/now", discounts)   | HIGH — active enforcement (Coles/Woolworths, 2024)              |
| Unfair contract terms (post-November 2023)          | HIGH — grace period ended; enforcement ramping                  |
| Subscription traps and harmful cancellation clauses | HIGH — stated 2025–2026 priority                                |
| Greenwashing and environmental claims               | HIGH — active enforcement (Clorox $8.25M, 2025)                 |
| Misleading surcharging                              | HIGH — stated 2025–2026 priority                                |
| Digital dark patterns                               | MEDIUM-HIGH — stated priority, enforcement developing           |
| Product safety                                      | MEDIUM — sector-dependent                                       |
| Unconscionable conduct                              | MEDIUM — case-by-case; high when targeting vulnerable consumers |

**Enforcement risk factors that aggravate exposure:**

- Conduct targeting vulnerable consumers (elderly, financial hardship, non-English-speaking)
- Prior ACCC warnings or undertakings in the same category
- Sector-wide investigation already underway
- High volume of affected consumers
- Ongoing conduct (not isolated incident)
- Profit obtained from the conduct
- Failure to cooperate or remedy promptly when issue identified

**Enforcement risk factors that mitigate exposure:**

- Proactive identification and cessation of non-compliant conduct
- Consumer remediation program implemented
- Enforceable undertaking offered (ACL s 87B)
- Compliance program demonstrably improved
- Small number of affected consumers; low loss per consumer

**⟁ CLARIFY** — If any findings are CRITICAL or HIGH, ask the user:

- Is this conduct ongoing or has it already been remediated?
- Has the ACCC contacted the business about this issue (inquiry, information notice,
  or correspondence)?
- What is the estimated number of affected consumers and approximate value of potential
  benefit gained from the non-compliant conduct?
  The answers directly affect penalty exposure calculation and urgency of remediation.

### Step 10: Quality Verification

Before delivering the assessment:

1. Run the 5 Citation Quality Gates (see Quality Assurance Framework below). Revise any
   failures before delivering.
2. For every NON-COMPLIANT or CRITICAL finding, run the 3-pass Self-Interrogation. Revise
   if any pass reveals a weakness.
3. Assign a Confidence Score to each material finding.
4. Confirm all six ACL pillars have been addressed (or explicitly scoped out).
5. Generate the Glass Box Audit Trail and append it to the output.

---

## ACL Compliance Analysis Reference

### Pillar 1: Misleading Conduct (ACL ss 18, 29)

**Standard**: Would the conduct, assessed objectively, likely mislead or deceive a
hypothetical reasonable consumer in the target market? No fault required.

**Key cases:**

- _ACCC v TPG Internet Pty Ltd_ [2013] HCA 54 [VERIFY]: "Up to" speed claims misleading
  where typical consumer could not achieve them — qualifiers do not neutralise misleading
  overall impression.
- _Google LLC v ACCC_ [2023] HCA 1 [VERIFY]: Misleading location data disclosures — the
  test is not whether a sophisticated user can work out the truth, but whether the ordinary
  consumer would be misled.

**Compliance standard**: Every material representation must accurately reflect what the
reasonable consumer in the target market would experience. Qualifiers ("up to," "from,"
"approximately") do not protect a false overall impression. Omissions of material
information can be as misleading as false statements.

**Remediation format for s 18 findings:**

```
Finding: [Description of potentially misleading representation]
Location: [Where it appears — website / T&Cs / advertising / packaging]
Risk: NON-COMPLIANT / PARTIAL
Confidence: [level]
Risk tier: CRITICAL / HIGH / MEDIUM / LOW
Basis: ACL s 18; [case authority if applicable]
Remediation: [Specific corrective action — revised wording or removal]
Revised language: "[Draft replacement text]"
```

### Pillar 2: Consumer Guarantees (ACL ss 51–64A)

**Non-excludability rule (ACL s 64)**: No contract term can exclude, restrict, or modify
a consumer guarantee. Any such clause is void. The guarantee continues regardless.

**Permitted limitation (ACL s 64A)**: For supplies of goods/services NOT ordinarily
acquired for personal use, where the price exceeds [VERIFY current threshold — previously
$100,000], the supplier may limit liability to: (a) resupply of goods/services, or
(b) payment of the cost of resupply.

**Key enforcement pattern (Mazda)**: Representing warranty-only remedies when ACL
guarantees entitle the consumer to refund/replacement is a s 29(1)(m) false representation
and potentially unconscionable under s 21. Mazda paid $11.5M in penalties (2024) [VERIFY].

**LG Electronics precedent**: Representing that "manufacturer's warranty is your only
remedy" violates ACL guarantee obligations — $160,000 penalty (2019) [VERIFY].

**Mandatory warranty text**: Since 8 June 2019, warranty documents for consumer goods must
contain prescribed text recognising ACL guarantee rights [VERIFY current requirements via
ACCC guidance].

### Pillar 3: Unfair Contract Terms (ACL ss 23–28)

**Standard form presumption (ACL s 23(2A))**: Contracts are presumed to be standard form
contracts if drafted by one party and the other had no genuine opportunity to negotiate.
The burden shifts to the drafting party to prove negotiation occurred.

**Penalty exposure (post-9 November 2023)**:

- Body corporates: up to the greater of $50M, 3× the benefit obtained, or 30% of
  turnover during the contravention period [VERIFY current penalty formula — CCA s 224]
- Individuals: up to $2.5M per contravention

**Court declaration required**: Unfair terms are not automatically void in Australia. A
court must declare a term unfair before the penalty consequences arise. However, using an
unfair term exposes the business to penalty proceedings.

**ACCC 2023 enforcement finding**: In its 2023 targeted review, the ACCC found that
**100% of franchise agreements reviewed** contained potentially unfair terms. This signals
the ACCC's view that most standard form contracts in commercial use contain at least
some problematic terms.

**Safe harbour reminder**: Upfront price terms and main subject matter definitions are
NOT subject to the UCT regime. Fees triggered during the contract term (late fees,
cancellation fees, add-ons) ARE subject.

### Pillar 4: Unconscionable Conduct (ACL ss 20–22)

**Threshold**: Higher than mere hardship or unfairness — the conduct must be so
unreasonable that a reasonable person in the position of the advantaged party would not
have engaged in it. However, the statutory threshold (s 21) is lower than equitable
unconscionability: no "special disadvantage" need be proved.

**Key principle**: Technically lawful conduct (exercising a contractual right) can be
unconscionable if exercised in a manner that exploits a vulnerable party without adequate
justification (_Kobelt_ [VERIFY]).

### Pillar 5: Product Safety (ACL ss 104–140)

**General safety provision (s 104)**: Catch-all for goods creating significant injury/
death risk even when no specific standard exists.

**Mandatory reporting (s 131 [VERIFY section])**:
Notification to the ACCC required as soon as practicable after a supplier becomes aware
that goods have caused or may cause death, serious injury, or serious illness. Failure
to report is a civil penalty offence.

**Recall risk**: Non-compliance with an ACCC recall direction is a contempt-equivalent
offence. Voluntary recall cooperation is a strong mitigating factor.

### Pillar 6: ACCC Enforcement Risk

**Penalty calculation factors (CCA s 224)**:

1. Nature, extent, and duration of the contravening conduct
2. Loss or damage caused
3. Benefit derived from the conduct
4. Whether the person has previously been found to have contravened the ACL
5. Whether the person cooperated with ACCC investigation
6. Such other matters as the court considers relevant

**Infringement notices**: The ACCC may issue infringement notices for minor, clear
contraventions. Payment (within 28 days) settles the matter without court proceedings
and is not an admission of liability. Useful for businesses seeking to resolve clear
minor breaches efficiently.

---

## Compliance Status Classification

### Finding Classifications

| Classification    | Meaning                                                  | Action Required                                          |
| ----------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| **COMPLIANT**     | No ACL issue identified for this element                 | Document for audit record; no remediation needed         |
| **PARTIAL**       | Some ACL requirements met; gaps or improvements needed   | Remediation recommended; timeline to be set              |
| **NON-COMPLIANT** | Clear breach of ACL or high likelihood of breach finding | Immediate remediation required; legal advice recommended |

### Risk Tiers

| Tier         | Meaning                                                                                                        | ACCC Enforcement Likelihood                           | Response Timeline                               |
| ------------ | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------- |
| **CRITICAL** | Conduct that would likely constitute a civil penalty contravention; ACCC enforcement priorities directly match | High — ACCC has brought comparable cases              | Immediate — cease within days; legal advice now |
| **HIGH**     | Material ACL gap; significant penalty exposure; ACCC enforcement focus area                                    | Moderate-high — within current enforcement priorities | Within 2–4 weeks                                |
| **MEDIUM**   | ACL improvement needed; some risk but not acute enforcement target                                             | Lower — not a current ACCC priority                   | Within 1–3 months                               |
| **LOW**      | Best practice improvement; technical or minor gap                                                              | Low — unlikely to attract enforcement action          | At next review cycle                            |

---

## Remediation Output Format

For each finding, generate a structured remediation block:

```
## Finding [#]: [Short Title]
**ACL Pillar**: [Misleading Conduct / Consumer Guarantees / UCT / Unconscionable /
               Product Safety]
**Classification**: NON-COMPLIANT / PARTIAL / COMPLIANT
**Risk Tier**: CRITICAL / HIGH / MEDIUM / LOW
**Confidence**: [Definite / High / Probable / Possible]

**What was found**: [Description of the non-compliant element — quote or describe]
**Why it's an issue**: [ACL basis — cite specific section and principle]
**ACCC enforcement precedent**: [Relevant case if applicable, with [VERIFY] marker]
**Potential exposure**: [Civil penalty range / ACCC enforcement risk / consumer claims]

**Required action**: [Specific remediation step]
**Revised language** (if applicable):
> [Draft compliant replacement text]

**Fallback position** (if applicable):
> [Alternative that still complies if primary revision is not feasible]

**Dependencies**: [Other changes needed, e.g., staff training, complaint handling update]
```

---

## Remediation Prioritization Framework

Organize findings by remediation priority:

### Priority 1 — Immediate Action (CRITICAL risk)

Issues where existing conduct likely constitutes a civil penalty contravention:

- Active misleading pricing claims without substantiation
- Returns policies that expressly deny statutory guarantee rights
- Standard form contracts with unilateral variation of price or unilateral termination
  without consumer option
- Any void clause attempting to exclude consumer guarantees (ACL s 64)
- Unreported product safety incidents (if goods have caused injury)

### Priority 2 — Urgent Remediation (HIGH risk, within 4 weeks)

Issues with material ACL exposure within current enforcement priorities:

- Warranty documents without mandatory ACL text
- "No refunds on sale items" or similar statements that imply ACL rights do not apply
- Unsubstantiated environmental claims in marketing
- Cancellation fees with no genuine loss basis
- Auto-renewal clauses without reminder mechanisms

### Priority 3 — Scheduled Remediation (MEDIUM risk, within 3 months)

Issues requiring improvement but not immediate enforcement risk:

- Complaint handling procedures that do not document the major/minor failure assessment
- Delivery timeframe representations that are aspirational rather than guaranteed
- Pricing disclosure that could be clearer but is not actively misleading

### Priority 4 — Review Cycle Improvements (LOW risk)

Best practice enhancements:

- Adding explicit ACL rights summary to the returns policy for consumer clarity
- Improving training documentation
- Refining cancellation UX to reduce friction (reducing dark pattern risk proactively)

**Remediation strategy**: Address Priority 1 and 2 issues first. Use Priority 3 and 4
timelines only when Priority 1 and 2 items are fully remediated. Where penalties may
have already accrued, obtain legal advice before voluntary disclosure to the ACCC —
the timing and manner of disclosure affects penalty negotiations.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise any failure before delivering.

| Gate           | Rule                                                                                                                     | Fail Action                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| **Source**     | Every ACL compliance claim cites a specific ACL section, ACCC enforcement precedent, or established principle            | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow Australian legal citation format (e.g., ACL s 18; [YYYY] HCA [n]; $[X]M penalty per [case])         | Fix format                                               |
| **Currency**   | Every cited ACL provision checked for amendments; penalty thresholds subject to indexation                               | Flag "[CHECK CURRENCY — indexed annually]"               |
| **Domain**     | Analysis stays within Australian law. No importing of US, UK, or EU consumer protection concepts as Australian law       | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated. Where ACCC enforcement outcome is uncertain or penalty amount cannot be confirmed, say so | Add confidence qualifier                                 |

### Self-Interrogation for NON-COMPLIANT / CRITICAL Findings

For any finding classified as NON-COMPLIANT or CRITICAL, apply this 3-pass review before
delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the NON-COMPLIANT classification follow logically from the cited ACL provision?
- Would the ACCC, a Federal Court judge, or an independent Australian consumer law
  practitioner reach this conclusion on these facts?
- What is the strongest counter-argument?

**Pass 2 — Completeness**:

- Have all relevant ACL sections been considered?
- Has ACCC enforcement history for this type of conduct been checked?
- Are there regulatory dimensions (ASIC overlap, state law overlay) not yet addressed?

**Pass 3 — Challenge**:

- What is the strongest argument that this conduct COMPLIES with the ACL?
- Under what circumstances might a reasonable Australian consumer law practitioner
  accept this practice as lawful?
- Is the NON-COMPLIANT / CRITICAL classification proportionate?

If any pass reveals a weakness, revise the finding before delivery. Mark the audit trail
with `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                          | Action                                                |
| ------------ | --------- | ------------------------------------------------ | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear ACL text, settled ACCC/court position      | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong authority; minor interpretation questions | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments; reasonable minds could differ    | State with explicit reasoning and contra-indicators   |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing interpretations   | Flag for qualified Australian consumer law counsel    |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                          | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every ACL compliance assessment output MUST include a Glass Box audit section:

```yaml
glass_box:
  skill: "legalcode-au-consumer-law-compliance"
  date: "[Date of assessment]"
  subject: "[Business name or description of materials assessed]"
  sector: "[Retail / SaaS / Manufacturing / Services / Other]"
  consumer_b2b: "[B2C / B2B / Both]"
  scope_assessed:
    - "[e.g., Terms and Conditions, Returns Policy, Marketing Materials]"
  acl_pillars_assessed:
    - "[Misleading Conduct / Consumer Guarantees / UCT / Unconscionable / Product Safety / All]"
  findings_summary:
    critical: "[number]"
    high: "[number]"
    medium: "[number]"
    low: "[number]"
    compliant: "[number]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "Competition and Consumer Act 2010 (Cth), Schedule 2 (ACL) — [VERIFIED / UNVERIFIED]"
    - "Treasury Laws Amendment (More Competition, Better Prices) Act 2022 — [VERIFIED / UNVERIFIED]"
  cases_consulted:
    - "[Case name, citation — VERIFIED / UNVERIFIED]"
  penalty_thresholds:
    body_corporate: "Up to $50M per contravention — [VERIFIED / UNVERIFIED]"
    individual: "Up to $2.5M per contravention — [VERIFIED / UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no NON-COMPLIANT / CRITICAL items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Scope limitations, assumptions, or caveats]"
    - "Penalty thresholds indexed annually — verify current amounts"
    - "ACCC enforcement priorities may have changed — verify current priorities"
  reviewer: "AI-assisted — requires review by qualified Australian consumer law practitioner"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in ACL compliance assessment:

1. **Treating ACL guarantees as optional**: The consumer guarantee regime is mandatory and
   non-excludable. Do not analyse warranty exclusions without first noting that s 64 renders
   them void for consumer goods and services. Void exclusions cannot reduce ACL exposure.

2. **Confusing manufacturer's warranty with statutory guarantee**: These are separate
   legal obligations. The manufacturer's warranty is contractual; the consumer guarantee is
   statutory. A consumer has both rights. Warranty expiry does not end ACL guarantee rights.

3. **Assuming "clear" qualifiers save misleading claims**: "Up to," "from," "approximately,"
   and similar qualifiers do not protect claims that create a false overall impression
   (_ACCC v TPG Internet_). Assess the likely impression on a reasonable consumer, not
   the technical accuracy of the qualified claim.

4. **Applying the pre-November 2023 UCT framework**: Before 9 November 2023, unfair terms
   in standard form contracts were void but did not attract civil penalties. Post-9 November
   2023, unfair terms attract penalties up to $50M. Applying the old analysis understates
   the current risk.

5. **Treating the standard form presumption as rebuttable in practice**: ACL s 23(2A)
   creates a rebuttable presumption. Do not assume this is easily rebutted — the supplier
   must show genuine negotiation occurred, not merely that it sent a contract for signature.

6. **Ignoring the "three limb" requirement**: A term is only unfair under ACL ss 23–24 if
   all three limbs are satisfied (significant imbalance + not reasonably necessary + would
   cause detriment). Terms that are one-sided but clearly necessary to protect legitimate
   interests may not be unfair. Assess each limb explicitly.

7. **Stating "no refunds" is always unlawful**: A "no refunds" policy is not always
   unlawful — it depends on context. For change-of-mind returns (where goods are of
   acceptable quality and fit for purpose), businesses are not required to offer refunds
   under ACL. The prohibition is on policies that suggest ACL rights (major failure refunds)
   do not apply.

8. **Overlooking the sector-specific enforcement context**: ACCC enforcement is not
   uniform — some sectors face active investigations (supermarkets, automotive, digital
   platforms, franchising) while others have lower enforcement pressure. Calibrate risk
   tier assessments to current ACCC priorities.

9. **Applying the s 20 general unconscionability standard to all cases**: Use s 21
   (consumer/small business unconscionability) for the relevant context. Section 21 has
   a lower threshold and the s 22 12-factor test explicitly applies. Do not conflate with
   equitable unconscionability, which requires special disadvantage.

10. **Confusing UCT safe harbour with immunity**: The safe harbour for "upfront price terms"
    and "main subject matter" is narrow. It covers only what the consumer is paying for and
    the core subject matter. Fees triggered during the contract (late fees, cancellation
    charges, add-on costs) are NOT safe-harboured and remain subject to UCT assessment.

11. **Missing the mandatory warranty text obligation**: Since 8 June 2019, warranty
    documents must contain prescribed ACL text. Omission is a separate compliance gap
    from the content of the warranty itself. Always check both.

12. **Classifying ASIC-regulated financial services as purely ACL matters**: Financial
    products and services regulated by ASIC under the Australian Securities and
    Investments Commission Act 2001 (ASIC Act) s 12DA (misleading conduct in financial
    services) overlap with ACL. Flag this dual-regulator exposure where relevant.

13. **Ignoring state/territory enforcement**: The ACCC is the primary enforcer, but state
    and territory consumer protection agencies (Consumer Affairs Victoria, NSW Fair Trading,
    etc.) have concurrent enforcement powers. A complaint to a state agency can trigger
    the same ACL enforcement outcomes.

14. **Treating enforcement actions as one-offs**: The ACCC's practice is to use major
    cases to signal standards across entire sectors. A penalty against one automotive
    manufacturer signals risk for all. Monitor relevant sector enforcement and treat it
    as an ACL compliance signal for the business.

15. **Delivering findings without remediation language**: ACL findings without specific
    draft revised language are not actionable. Every NON-COMPLIANT or PARTIAL finding
    must include concrete revised wording. "This term should be revised to be fairer" is
    insufficient — provide the revised term.

16. **Assuming voluntary disclosure always reduces penalties**: While ACCC enforcement
    practice generally treats cooperation favourably, the timing and manner of voluntary
    disclosure is legally complex. Do not advise voluntary disclosure without noting that
    legal advice is required — poorly timed disclosure can affect privilege and penalty
    negotiations.

---

## Writing Standards

Apply plain-language discipline to all output:

**For remediation advice** (shared with business stakeholders and counsel):

- Plain language. No unnecessary jargon.
- Active voice: "This clause excludes ACL guarantee rights, which is void under s 64"
  not "ACL guarantee rights are excluded by this clause, a result that is voided by s 64"
- Short sentences. One point per sentence.
- Name the specific ACL provision: "ACL s 18" not "the misleading conduct provision"
- Specific proposed language — not vague guidance like "revise this clause"

**For risk tier classification**:

- State the tier (CRITICAL / HIGH / MEDIUM / LOW) before the explanation
- Cite the ACCC enforcement precedent that drives the classification
- Quantify the potential exposure where possible (penalty range, affected consumer volume)

**Quality gates before delivery**:

1. Can a non-legal business manager understand the key findings and required actions?
2. Can the business's lawyer implement each remediation recommendation without further
   clarification?
3. Is every legal claim backed by a specific ACL citation (or flagged [VERIFY])?
4. Are any phrases vague, hedging, or ambiguous? If yes, fix.
5. Could any sentence be shorter without losing meaning? If yes, shorten.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 3, search for current ACL statutory text, ACCC enforcement actions, and
  applicable Federal Court decisions
- Search for product safety standards applicable to the business's product categories
- Save the most relevant results to `/tmp/legalcode-au-acl-authority.md`
- Verify current penalty thresholds (indexed annually; confirm via CCA s 314ZJ [VERIFY])
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Include a prominent notice: penalty thresholds and case law require independent
  verification against the Federal Register of Legislation and ACCC media releases
- Focus the assessment on structural compliance issues and policy gaps where legal
  certainty is less dependent on specific citations

---

## Localization Notes

### Within Australia

While the ACL is national, some transactions require additional state/territory compliance:

| Area                                 | State/Territory Variation                                                                          | Action                                    |
| ------------------------------------ | -------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| Door-to-door and telemarketing sales | Some states provide cooling-off periods and additional disclosure requirements beyond ACL minimums | [JURISDICTION-SPECIFIC] — verify by state |
| Real estate and property services    | State-based licensing, cooling-off periods, and disclosure rules overlay ACL                       | [JURISDICTION-SPECIFIC]                   |
| Motor vehicle sales                  | State-based dealer legislation supplements ACL consumer guarantees                                 | [JURISDICTION-SPECIFIC]                   |
| Second-hand goods                    | State-specific rules on disclosure and consumer rights for second-hand goods                       | [JURISDICTION-SPECIFIC]                   |
| Residential tenancy                  | Primarily state-regulated; ACL UCT regime applies to standard form residential tenancy             | [JURISDICTION-SPECIFIC]                   |

### Financial Services Overlap

Businesses holding an Australian Financial Services Licence (AFSL) are regulated by
ASIC under the Corporations Act 2001 (Cth) and ASIC Act 2001 (Cth), as well as the ACL.
Misleading conduct in connection with financial products is governed by ASIC Act s 12DA
(parallel to ACL s 18). ACCC and ASIC have concurrent jurisdiction in some areas. Dual
compliance assessments may be required.

---

## Output Format Template

Structure the final deliverable as:

```markdown
## ACL Compliance Assessment Report

**Subject**: [Business / document / materials assessed]
**Sector**: [Business sector]
**Date**: [Assessment date]
**Scope**: [ACL pillars assessed]
**Basis**: [legalcode-mcp-verified / General ACL framework — citations require verification]

---

## Executive Summary

**Overall Compliance Profile**: [COMPLIANT / PARTIALLY COMPLIANT / NON-COMPLIANT]

| Risk Tier | Count | Key Issues           |
| --------- | ----- | -------------------- |
| CRITICAL  | [n]   | [Brief descriptions] |
| HIGH      | [n]   | [Brief descriptions] |
| MEDIUM    | [n]   | [Brief descriptions] |
| LOW       | [n]   | [Brief descriptions] |

**Immediate action required**: [Yes / No — list CRITICAL items if Yes]

---

## Findings by ACL Pillar

### Pillar 1: Misleading or Deceptive Conduct (ACL ss 18, 29)

**Status**: COMPLIANT / PARTIAL / NON-COMPLIANT

[Individual finding blocks per Remediation Output Format above]

### Pillar 2: Consumer Guarantees (ACL ss 51–64A)

**Status**: COMPLIANT / PARTIAL / NON-COMPLIANT

[Returns/refund policy checklist results]
[Individual finding blocks]

### Pillar 3: Unfair Contract Terms (ACL ss 23–28)

**Status**: COMPLIANT / PARTIAL / NON-COMPLIANT

[UCT screening results — term by term]
[Civil penalty exposure per term if applicable]

### Pillar 4: Unconscionable Conduct (ACL ss 20–22)

**Status**: COMPLIANT / PARTIAL / NON-COMPLIANT

[s 22 factor analysis if any concerns identified]

### Pillar 5: Product Safety (ACL ss 104–140)

**Status**: COMPLIANT / PARTIAL / NON-COMPLIANT / NOT APPLICABLE

[Safety checklist results]

### Pillar 6: ACCC Enforcement Risk

**Overall Risk Profile**: LOW / MEDIUM / HIGH / CRITICAL

[Priority areas matching current ACCC enforcement focus]
[Aggravating / mitigating factors]

---

## Remediation Roadmap

### Priority 1 — Immediate (CRITICAL findings)

| Finding | Required Action | Revised Language    | Owner | Deadline    |
| ------- | --------------- | ------------------- | ----- | ----------- |
| [#]     | [Action]        | [See finding block] | [TBC] | [Immediate] |

### Priority 2 — Urgent (HIGH findings, within 4 weeks)

[Table as above]

### Priority 3 — Scheduled (MEDIUM findings, within 3 months)

[Table as above]

### Priority 4 — Review Cycle (LOW findings)

[Table as above]

---

## ACL Compliance Program Gaps

[Assessment of underlying compliance program adequacy:

- Policy coverage
- Staff training
- Complaint handling
- Monitoring and audit cadence
- Regulatory intelligence function]

---

## Next Steps

[Specific immediate actions — legal review needed, policy updates, staff training,
ACCC contact (if relevant), timeline]

---

[Glass Box Audit Trail — YAML per template above]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis for Australian Consumer Law
compliance assessment. Research conducted using 2-agent parallel workflow:

- Agent 1 (Structural Analyst): Deep research on ACL statutory framework — ACL ss 18,
  20–22, 23–28, 29, 51–64A, 104–140; Treasury Laws Amendment (More Competition, Better
  Prices) Act 2022; post-9 November 2023 UCT penalty regime; ACCC enforcement actions
  2019–2025 (Mazda $11.5M, Clorox $8.25M, Coles/Woolworths proceedings, Google LLC v
  ACCC [2023] HCA 1, LG Electronics $160K); ACCC enforcement priorities 2024–2026.
- Agent 2 (Prompt Engineering and Quality Analyst): ACL compliance workflow design;
  ACCC anti-pattern research; UCT safe harbour analysis; sector-specific compliance
  frameworks (e-commerce, SaaS, manufacturing, automotive, financial services); returns
  policy compliance; complaint handling best practices; ACCC enforcement intelligence
  including Coles/Woolworths (2024), Mazda (2024), Clorox (2025) penalty cases.
  Repository reference: `skills/jurisdictions/australia/contracts/legalcode-franchise-agreement-review-au/SKILL.md`
  (existing Australian skill — UCT, consumer guarantees, and ACCC enforcement patterns
  reviewed for cross-reference consistency).
