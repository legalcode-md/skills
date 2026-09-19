---
name: legalcode-supply-chain-contract-review
description: Review supply and procurement agreements covering pricing mechanisms (fixed, index-linked,
  MFC/MFN), tariff and customs risk allocation, delivery terms (Incoterms 2020), quality specifications
  and inspection rights, warranty provisions (UCC Article 2, CISG Art. 35, UK Sale of Goods Act 1979),
  EU Product Liability Directive 2024/2853 (in force Nov 2024), force majeure and commercial impracticability,
  supply continuity and business continuity obligations, sustainability and ESG supply chain due diligence
  (EU CSDDD, UK Modern Slavery Act, US UFLPA, France Devoir de Vigilance, Norway Åpenhetsloven), critical
  minerals and rare earth traceability (EU CRMA, EU Battery Regulation, Dodd-Frank), supply chain finance
  integration, and indemnification.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review supply and procurement agreements covering pricing mechanisms (fixed, index-linked, MFC/MFN), tariff and customs risk allocation, delivery terms (Incoterms 2020), quality specifications and inspection rights, warranty provisions (UCC Article 2, CISG Art. 35, UK Sale of Goods Act 1979), EU Product Liability Directive 2024/2853 (in force Nov 2024), force majeure and commercial impracticability, supply continuity and business continuity obligations, sustainability and ESG supply chain due diligence (EU CSDDD, UK Modern Slavery Act, US UFLPA, France Devoir de Vigilance, Norway Åpenhetsloven), critical minerals and rare earth traceability (EU CRMA, EU Battery Regulation, Dodd-Frank), supply chain finance integration, and indemnification. Covers UCC Article 2, CISG Arts 25/35/71–79, and UK Sale of Goods Act. Use when reviewing supplier contracts, vendor agreements, procurement agreements, manufacturing agreements, purchase orders with general terms, component supply contracts, distribution supply terms, raw material supply agreements, critical mineral offtake agreements, or any contract for the sale or supply of goods. Jurisdiction-agnostic with localization markers for US (UCC), UK (SGA 1979), international sale (CISG), and EU (CSDDD, EU PLD 2024/2853, CRMA). Covers B2B supply relationships from both buyer and supplier perspectives.


# Legalcode Supply Chain Contract Review

> **Disclaimer**: This skill provides a framework for AI-assisted review of supply and
> procurement agreements. It does not constitute legal advice. All outputs should be
> reviewed by a qualified legal professional licensed in the relevant jurisdiction before
> use. Laws change — UCC provisions, ESG statutes, Incoterms editions, and the EU Product
> Liability Directive are updated periodically; verify current applicability before relying
> on any provision described here. Statutory and case law references cited from memory carry
> hallucination risk — verify against authoritative sources before relying on them.

## Purpose and Scope

This skill reviews supply, procurement, and goods purchase agreements against an
organization's negotiation playbook or general commercial standards. It identifies
deviations, classifies their severity, generates actionable redline suggestions, and
produces a confidence-scored, auditable analysis adapted to the unique legal issues in
supply chain contracting.

**Covers:**

- Clause-by-clause analysis across 18 supply chain–specific clause categories
- Pricing structure review (fixed, index-linked, MFC/MFN, volume-tiered, tariff pass-through)
- Tariff and customs risk allocation (Section 301/232, IEEPA tariffs, hardship clauses)
- Incoterms 2020 risk and cost allocation analysis
- Quality specifications, inspection rights, acceptance/rejection procedures (FAI, AQL)
- Warranty analysis under UCC Article 2, CISG Art. 35, and UK Sale of Goods Act 1979
- EU Product Liability Directive 2024/2853 (in force November 25, 2024; transposition Dec 9, 2026)
- Force majeure, commercial impracticability, and tariff-induced hardship
- CISG anticipatory breach (Arts. 71–73) and damages calculation (Arts. 74–77)
- Supply continuity, business continuity plans, and shortage allocation
- ESG/sustainability due diligence (CSDDD 2029, UK Modern Slavery Act, UFLPA, France Vigilance Law, Norway Åpenhetsloven)
- Critical minerals and rare earth traceability (EU CRMA, EU Battery Regulation 2023/1542, Dodd-Frank § 1502)
- Supply chain finance integration (SCF/reverse factoring, assignment of receivables)
- Deviation classification (GREEN / YELLOW / RED)
- Redline generation with fallback positions
- Missing clause detection
- Business impact assessment and negotiation strategy
- Quality-verified output with Glass Box audit trail

**Does not:**

- Draft new supply agreements (see legalcode-master-services-agreement for MSA drafting)
- Provide legal advice or replace qualified procurement or supply chain counsel
- Apply to services-only engagements with no goods component (see legalcode-contract-review)
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic across three major frameworks for goods contracts:

**US (UCC Article 2)**: The Uniform Commercial Code Article 2 governs the sale of goods
in all US states (with Louisiana variations). Key features: implied warranty of
merchantability (§ 2-314), implied warranty of fitness for particular purpose (§ 2-315),
perfect tender rule (§ 2-601), seller cure rights (§ 2-508 — two paths: seasonably notified
of substitution, or time extension), commercial impracticability (§ 2-615), remedy
limitation (§ 2-719), and battle of the forms (§ 2-207).

**UK (Sale of Goods Act 1979 / Sale and Supply of Goods Act 1994)**: Implied terms as to
title (s.12), description (s.13), satisfactory quality (s.14(2)), and fitness for purpose
(s.14(3)). "Satisfactory quality" (post-1994 standard) includes safety, durability,
appearance, and freedom from minor defects. B2B exclusion of implied terms possible if
reasonable under UCTA 1977 s.6. Consumer Rights Act 2015 applies to B2C.

**International (CISG)**: The UN Convention on the International Sale of Goods applies to
international contracts between parties in contracting states (95+ states) unless expressly
excluded. Key features: fundamental breach threshold for avoidance (Art. 25), conformity
obligation (Art. 35), buyer's remedies (Arts. 45–52), seller's remedies (Arts. 61–65),
risk of loss (Arts. 66–70), anticipatory breach / suspension / installment contracts
(Arts. 71–73), damages calculation — full compensation, cover, market price, mitigation
duty (Arts. 74–77), exemption / force majeure (Art. 79). CISG does not use the "warranty"
concept — it imposes a strict "conformity" obligation on the seller under Art. 35.

**EU Product Liability Directive 2024/2853** (in force November 25, 2024; member state
transposition deadline December 9, 2026; applies to products placed on market / put into
service after transposition date): Replaces 85/374/EEC. Extends strict liability to
software, AI systems, digital manufacturing files, and firmware. Expands damage categories
to include data loss and psychological harm. Lengthens long-stop limitation period to 25
years for latent damage claims. Creates rebuttable presumptions of defect and causation
for claimants facing "excessively difficult" proof burdens. Restructures supply chain
liability tiers: manufacturers primary; importers / authorized representatives secondary
for non-EU manufacturers; distributors / platforms fallback.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- Governing code for goods contracts (UCC Article 2 / UK SGA / CISG / civil code equivalent)
- Implied warranty regime and exclusion formalities
- Inspection and rejection timelines (notice requirements under UCC § 2-602, CISG Art. 38)
- Import/export controls, customs classification, and sanctions regimes
- ESG mandatory due diligence laws applicable to your jurisdiction
- Penalty/liquidated damages enforceability rules
- Dispute resolution norms for commercial goods disputes
- EU Product Liability Directive 2024/2853 national implementing legislation (after Dec 9, 2026)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The governing legal framework is unclear (UCC vs. CISG vs. UK SGA vs. civil law)
- The user's side (buyer/supplier) is ambiguous
- ESG screening triggers are unclear
- Risk tolerance or business context is needed to classify severity correctly
- Ambiguity in the contract creates a fork that only the user can resolve

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

Accept the supply or procurement agreement in any of these formats:

- **File**: PDF, DOCX, or other document format
- **URL**: Link to a contract in a CLM, cloud storage, or document system
- **Pasted text**: Contract text pasted directly into the conversation
- **PO with General Terms**: A purchase order incorporating standard terms by reference

If no contract is provided, prompt the user to supply one.

If the contract incorporates terms by reference (e.g., "subject to Supplier's Standard
Purchase Terms at [URL]"), flag this and ask whether the user wants to review the
incorporated terms in addition to the main agreement.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask the user:

1. **Which side are you on?**
   - Options: Buyer/Purchaser, Supplier/Seller, Manufacturer, Distributor, Other
   - _Why this matters_: The entire analysis flips. What protects a buyer (broad
     inspection rights, implied warranty preservation) harms a supplier and vice versa.

2. **Type of goods or supply relationship:**
   - Options: Components/Raw materials, Finished goods for resale, Custom manufactured
     goods, Commodities, Critical minerals/rare earth materials, Technology hardware,
     Medical devices/regulated goods, Pharmaceutical/biologic APIs, Food/perishables, Other
   - _Why this matters_: Medical devices and food have regulatory compliance overlays;
     critical minerals have offtake and traceability requirements; pharma has FDA/EMA
     regulatory requirements.

3. **Deadline and deal context:**
   - Urgency: Urgent (days) / Standard (1-2 weeks) / Flexible
   - Free text: deal size, strategic importance of supplier, alternative suppliers
     available, whether this is a framework agreement or one-off purchase, whether
     supplier has supply chain leverage (sole-source, long-lead, critical).
   - _Why this matters_: A $5K spot purchase gets different treatment than a
     $50M multi-year exclusive supply agreement.

4. **Focus areas** (allow multiple):
   - Options: Pricing/escalation/tariffs, Delivery/Incoterms, Quality/warranty,
     Force majeure/supply continuity, ESG/sustainability compliance, Critical minerals
     traceability, Supply chain finance, Indemnification/liability, Termination flexibility,
     No specific focus — full review
   - _Why this matters_: Leads the analysis with what the user cares about most.

5. **Playbook status:**
   - Options: We have a procurement playbook (provide it or describe key positions),
     Use general market standards, I'll specify positions as we go
   - _Why this matters_: Determines whether deviations are assessed against
     organizational positions or general commercial norms.

If the user provides partial context, state your assumptions explicitly (e.g., "I'm
assuming you are the buyer — let me know if that's wrong").

### Step 3: Identify the Governing Legal Framework

**⟁ CLARIFY** — Identify the governing law and applicable goods-law framework:

1. Read the contract's governing law clause.
2. Determine the applicable framework:
   - **UCC Article 2**: US domestic sale of goods
   - **CISG**: International sale between parties in CISG contracting states (unless excluded)
   - **UK SGA 1979 + SSGSA 1994**: UK-governed contracts
   - **Civil code equivalent**: French Code civil, German BGB, etc.
   - **No governing law clause**: Flag as RED (absent governing law is a material gap).

3. **CISG default-applies screen**: If the contract is international and the parties are
   in CISG contracting states, CISG applies by default even without explicit choice.
   Ask the user: "This appears to be an international sale. Has CISG been expressly
   excluded? If not, CISG may apply alongside or instead of the stated governing law."

4. **Multiple governing law instruments**: Some supply contracts reference Incoterms
   (ICC instrument) alongside UCC or English law. Confirm the hierarchy.

5. **EU Product Liability Directive applicability**: If goods are placed on the EU market
   (or put into service after December 9, 2026 transposition), Directive 2024/2853 applies
   to the manufacturer (or EU importer if manufacturer is non-EU). Flag if the contract
   does not address EU PLD liability allocation.

[JURISDICTION-SPECIFIC] Note which implied warranty regime applies and what formalities
are required to disclaim:

- **UCC § 2-316**: "Merchantability" disclaimer must be conspicuous and mention the word
  "merchantability." Fitness for particular purpose disclaimer must be conspicuous and
  in writing. "As is" or "with all faults" effectively disclaims all implied warranties
  without requiring specific words [VERIFY — state law variations apply].
- **UK SGA s.14 / CRA 2015**: B2B contracts may exclude implied terms if reasonable under
  UCTA 1977 s.6. B2C contracts: implied terms as to quality cannot be excluded [VERIFY].
- **CISG Art. 35**: Strict conformity obligation — not a warranty concept. Parties may
  derogate by agreement (Art. 6); no specific disclaimer formality required for
  international commercial parties [VERIFY].

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Read the contract's governing law clause and use **legalcode-mcp** to build a working
legal reference file.

**Research process:**

1. Search for applicable goods-law statutes: UCC Article 2, UK SGA 1979, CISG text
2. Search for ESG supply chain statutes applicable to the parties' jurisdictions
3. Search for implied warranty disclaimer requirements and enforceability cases
4. Search for force majeure/commercial impracticability case law in the governing
   jurisdiction (post-2020 COVID-era and 2025 tariff-era precedents)
5. Search for relevant Incoterms 2020 guidance and trade usage
6. Search for EU Product Liability Directive 2024/2853 transposition status (if EU market)
7. Search for critical minerals regulations if relevant goods are involved

Save results to `/tmp/legalcode-supply-review-authority.md`:

```markdown
# Legal Authority Reference — [Contract Name]

## Governing Law: [Jurisdiction]

## Applicable Goods Framework: [UCC / CISG / UK SGA / other]

## Date Gathered: [date]

### Goods Law Statutes

- [Statute, section, relevance]

### Implied Warranty Regime

- [Applicable warranty provisions, disclaimer requirements]

### ESG/Sustainability Statutes

- [Applicable laws, covered entities, obligations]

### Product Liability Framework

- [Applicable directive/statute, key provisions, supply chain allocation]

### Case Law

- [Case, citation, key holding]

### Regulatory Guidance

- [Regulator, guidance, relevance]
```

**If legalcode-mcp is not connected:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Focus analysis on commercial risk and structural issues; flag legal citations as
  requiring independent verification

### Step 5: Incoterms Preliminary Screen

Before the full clause review, identify the Incoterms used in the contract and flag
any structural mismatch.

For each delivery term found:

1. Confirm it is a valid **Incoterms 2020** term — specify edition year (not just "FOB"):
   EXW, FCA, CPT, CIP, DAP, DPU, DDP, FAS, FOB, CFR, CIF. Note: DAT (Incoterms 2010)
   was replaced by DPU in Incoterms 2020.
2. Confirm it is appropriate for the mode of transport (sea-only terms used for air
   shipments is a common error; FOB/CFR/CIF only appropriate for non-containerized bulk)
3. Check whether a named place is specified (Incoterms without a named place are
   incomplete and unenforceable as stated)
4. Check alignment between the Incoterm and the insurance obligation:
   - CIP: seller must provide ICC (A) all-risk cover at minimum 110% of contract value
   - CIF: seller must provide only ICC (C) limited perils — insufficient for manufactured goods
5. Check for FCA containerized cargo: confirm whether the Art. A6/B6 on-board B/L
   arrangement has been agreed (important for letter-of-credit transactions)
6. Check whether CISG or domestic law risk-of-loss rules interact with the Incoterm

**⟁ CLARIFY** — If the Incoterm creates an unclear risk allocation:

- "The contract uses FOB [city], but the goods are containerized. FOB is not recommended
  for containerized cargo — FCA would be more appropriate because risk passes when goods
  are handed to the first carrier, not when loaded on the vessel. Should I flag this as
  a YELLOW deviation?"
- "The contract references DPU but does not specify a named destination place. This
  makes the Incoterm incomplete. Should I flag this as YELLOW or RED?"

### Step 6: ESG and Sustainability Compliance Screen

Before the full clause review, run a targeted ESG compliance screen. Supply chain ESG
obligations are now legally mandatory in major markets, not merely aspirational.

**Screening questions:**

1. **EU Corporate Sustainability Due Diligence Directive (CSDDD, Directive 2024/1760)**
   [VERIFY — under "Omnibus I" (Dec 2025), single application date of July 26, 2029
   for all in-scope companies; Member State transposition deadline July 26, 2027]:
   - Does either party have 1,000+ employees AND EUR 450M+ worldwide turnover (EU-based)?
   - For non-EU companies: does either party have EUR 450M+ EU revenue?
   - Does the agreement contain human rights and environmental due diligence flowdown?
   - Does it include audit rights for supply chain due diligence?
   - Penalties: up to 5% of worldwide net annual turnover; civil liability for negligent failure.

2. **German Supply Chain Due Diligence Act (LkSG)**
   [IMPORTANT: As of March 2026, the German coalition government announced intent to
   abolish LkSG [VERIFY — formal repeal legislation may still be pending]. Do not rely
   on LkSG compliance as sufficient without confirming current legislative status.
   Existing LkSG violations still relevant for contracts executed before repeal.]:
   - If LkSG remains in effect: applies to German entities with 1,000+ employees.
   - Requires risk analysis of direct and indirect suppliers; formal complaint mechanisms.

3. **France Devoir de Vigilance (Loi n° 2017-399)** [VERIFY]:
   - Applies to French joint stock companies with 5,000+ French employees OR
     10,000+ global employees.
   - Requires annual vigilance plan covering human rights, health/safety, environment.
   - Active litigation: 30+ formal notices and 13+ lawsuits filed 2017–2025.
   - Does the contract support supplier compliance with vigilance plan requirements?

4. **Norway Transparency Act (Åpenhetsloven, effective July 1, 2022)** [VERIFY]:
   - Applies to large Norwegian enterprises (>NOK 70M revenue OR >NOK 35M balance sheet
     OR >50 employees).
   - Covers ALL supply chain tiers (Tier N), not just direct suppliers.
   - Annual due diligence report required by June 30 each year.
   - Does the contract require supplier to cooperate with due diligence obligations
     and provide information for the buyer's annual report?

5. **UK Modern Slavery Act 2015 (s.54)** [VERIFY]:
   - Does either party have UK turnover ≥ £36M?
   - Does the contract contain modern slavery representations and audit rights?
   - Note: UK "failure to prevent fraud" offence (in force September 1, 2025) creates
     adjacent liability risk for misrepresentations about MSA compliance.

6. **US Uyghur Forced Labor Prevention Act (UFLPA)** [VERIFY — effective June 22, 2022]:
   - Do the goods involve manufacturing, raw materials, or components from Xinjiang, China?
   - Are any suppliers on the UFLPA Entity List?
   - Does the contract include UFLPA compliance representations and supply chain traceability?
   - Are there documentation requirements for CBP rebuttable presumption rebuttal?

7. **EU Conflict Minerals Regulation (Regulation 2017/821)** [VERIFY — effective Jan 1, 2021]:
   - Do the goods contain tin, tantalum, tungsten, or gold (3TG minerals)?
   - Does the agreement require OECD Due Diligence Framework compliance or RMI certification?

8. **EU Battery Regulation (2023/1542)** [VERIFY — phased application 2024–2027]:
   - Do the goods involve batteries containing cobalt, lithium, nickel, or natural graphite?
   - For large producers: supply chain due diligence applies from February 18, 2025.
   - Requires chain-of-custody documentation and traceability from mine to product.

9. **EU Critical Raw Materials Act (CRMA, Regulation 2024/1252)**
   [VERIFY — in force May 23, 2024]:
   - Are the goods in a "strategic" sector (EV batteries, semiconductors, renewable energy)?
   - Does the contract require supplier to provide origin documentation for critical minerals?

Flag any gap where a mandatory ESG obligation applies but is absent from the contract.

**⟁ CLARIFY** — If ESG screening triggers are unclear:

- "The goods appear to involve materials potentially sourced from Xinjiang. Does your
  organization have UFLPA compliance representations in your standard supplier terms?
  If not, I'll flag this as RED."
- "Germany's coalition government announced abolition of LkSG in March 2026. Please
  confirm the current legal status before treating LkSG compliance as a binding
  obligation in this contract."

### Step 7: Clause-by-Clause Analysis

Read the entire contract before flagging issues — supply chain clauses interact
(e.g., a broad force majeure may negate the entire supply continuity obligation;
an uncapped indemnity may be partially mitigated by a limitation clause).

**⟁ CLARIFY** — For long or complex supply agreements (50+ pages, multiple schedules,
incorporating purchase order terms, quality plans, or technical specifications):

- Ask whether to perform a **full review** of all 18 clause categories or a **priority
  review** focused on stated focus areas plus any RED items discovered.
- If the contract incorporates external quality standards by reference (e.g., ISO 9001,
  AS9100, IATF 16949, USP/EP), ask whether the user wants those standards' requirements
  noted in the analysis.

Cover all 18 clause categories below. For each, assess against the playbook (or general
standards) and note whether the clause is present, absent, or unusual.

| #   | Clause Category                            | Depth    | Key Review Points                                                                               |
| --- | ------------------------------------------ | -------- | ----------------------------------------------------------------------------------------------- |
| 1   | Pricing Mechanisms                         | Deep     | Fixed vs. index-linked, escalation formula, MFC/MFN, tariff pass-through, volume discounts      |
| 2   | Delivery Terms (Incoterms)                 | Deep     | Risk transfer, cost allocation, insurance obligations, named place, version                     |
| 3   | Quality Specifications & Inspection        | Deep     | Specs definition, inspection timing, FAI, AQL sampling, acceptance criteria, rejection notice   |
| 4   | Warranty & Product Liability               | Deep     | Implied warranty status, express warranties, disclaimer, EU PLD 2024/2853, product recall       |
| 5   | Force Majeure, Impracticability & Hardship | Deep     | Scope, tariff hardship, supply disruption coverage, notification, duration, termination trigger |
| 6   | Supply Continuity                          | Deep     | BCP requirements, safety stock, dual sourcing, shortage allocation                              |
| 7   | ESG & Sustainability Obligations           | Deep     | Flowdown requirements, audit rights, representations, termination trigger, CSDDD, UFLPA         |
| 8   | Indemnification                            | Deep     | Scope, mutual vs. unilateral, product liability, IP infringement                                |
| 9   | Limitation of Liability                    | Deep     | Cap amount, carveouts, consequential damages, product recall                                    |
| 10  | Intellectual Property                      | Standard | Pre-existing IP, tooling ownership, custom development, feedback                                |
| 11  | Confidentiality                            | Standard | Scope, term, carveouts, data security                                                           |
| 12  | Term & Termination                         | Standard | Duration, renewal, termination for cause, wind-down, transition                                 |
| 13  | Governing Law & Disputes                   | Standard | Jurisdiction, UCC/CISG/SGA framework, arbitration, escalation                                   |
| 14  | Compliance & Regulatory                    | Standard | Trade compliance, sanctions, export control, product safety, recalls                            |
| 15  | Insurance                                  | Standard | Product liability coverage, cargo insurance, property insurance, EU PLD exposure                |
| 16  | Definitions & Boilerplate                  | Standard | Order of precedence, entire agreement, amendment, notices                                       |
| 17  | Tariff & Customs Risk Allocation           | Deep     | Tariff pass-through, hardship, importer of record, rules of origin, HS code disputes            |
| 18  | Supply Chain Finance                       | Standard | SCF/reverse factoring, assignment of receivables, anti-assignment conflicts                     |

### Step 8: Missing Clause Detection

After analyzing present clauses, check for important absent clauses. A missing clause
can be as significant as a problematic one.

Common critical missing clauses in supply agreements:

- No price escalation mechanism in a multi-year agreement (YELLOW)
- No tariff pass-through or hardship clause in a cross-border agreement (YELLOW)
- No inspection or acceptance procedure (RED — creates acceptance-by-default risk)
- No warranty disclaimer when relying on implied warranties (YELLOW or RED depending on side)
- No force majeure clause (YELLOW — commercial impracticability doctrine may substitute)
- No supply continuity/BCP obligation for critical components (RED for strategic supply)
- No ESG representations when goods are at risk of forced labor exposure (RED)
- No CISG exclusion in an international contract where parties prefer domestic law (YELLOW)
- No product recall mechanism or cost allocation (RED for consumer goods)
- No IP ownership clause for custom tooling (YELLOW)
- No governing law clause (RED)
- No EU authorized representative appointment for non-EU goods placed on EU market (RED if goods are sold to EU)
- No tariff/customs risk allocation for international supply of sensitive goods (YELLOW)

**⟁ CLARIFY** — When the severity of a missing clause depends on business context:

- "This contract has no business continuity plan requirement. Is this supplier strategic
  or single-source for a critical component? If yes, this is RED. If this is a commodity
  purchase with alternatives, it may be YELLOW."
- "There is no CISG exclusion. If both parties are in CISG contracting states, CISG may
  govern. Does your organization prefer UCC/UK law to apply exclusively?"
- "There is no tariff pass-through clause. Has your organization modeled the impact of
  a significant tariff increase (>10%) on the economics of this contract?"

### Step 9: Flag Deviations

Classify each deviation using the three-tier system in the **Deviation Severity
Classification** section below. For each deviation:

- **GREEN**: Note for awareness.
- **YELLOW**: Generate specific redline language, provide a fallback position, and
  estimate business impact.
- **RED**: Explain the specific risk (citing legal basis where possible), provide
  market-standard alternative language, estimate exposure, and recommend escalation.

**⟁ CLARIFY** — For borderline classifications:

- When a warranty disclaimer is incomplete but the buyer may have accepted it in
  prior dealings: "The warranty disclaimer does not specifically disclaim the implied
  warranty of merchantability by name (required under UCC § 2-316). This may not
  achieve the intended disclaimer. Should I treat this as YELLOW (negotiate a proper
  disclaimer) or RED (likely unenforceable — escalate)?"
- When an Incoterm creates unusual risk allocation not necessarily wrong but unusual:
  present the trade-off and ask.

### Step 10: Generate Redlines

**⟁ CLARIFY** — Before generating redlines, ask the user about negotiation posture:

- **Supplier relationship**: Is this a strategic supplier, preferred vendor, or commodity
  supplier? Tone adjustments — strategic partner redlines should be collaborative.
- **Volume of redlines**: If many YELLOW items are found, ask: "I've found [N] items
  worth negotiating. Do you want redlines for all of them, or focus on the top [X]?"

For each YELLOW and RED deviation, generate a redline using the format in **Redline
Format** below.

### Step 11: Business Impact Summary

Provide a summary covering:

- **Overall risk assessment**: High-level risk profile of the supply agreement
- **Top 3 issues**: Most important items with severity and priority
- **Supply chain risk snapshot**: Specific supply disruption, ESG, tariff, and pricing risks
- **Negotiation strategy**: Which issues to lead with, what to concede, sequencing

**⟁ CLARIFY** — If deal context would materially affect strategy:

- "Can you walk away from this supplier, or is this the only qualified source?"
- "Has your organization experienced supply disruptions from this supplier or region
  before? Prior disruptions affect how aggressively to push for BCP clauses."
- "Is your organization subject to any ESG reporting obligations (CSRD, SEC, CSDDD)
  that require supply chain data from this supplier?"

### Step 12: Quality Verification

Before delivering the analysis, run the quality checks in the **Quality Assurance
Framework** section:

1. Run 5 Citation Quality Gates silently. Revise any failures.
2. For every RED item, run the 3-pass Self-Interrogation.
3. Assign Confidence Scores to each material clause analysis.
4. Verify all 18 clause categories have been addressed.
5. Generate the Glass Box Audit Trail.

---

## Supply Chain Clause Analysis Reference

### 1. Pricing Mechanisms

**Key elements to review:**

**Fixed pricing:**

- Is the price truly fixed, or subject to reopener triggers (raw material cost changes,
  tariff changes, currency fluctuation)?
- What is the lock-in period? Fixed prices in multi-year agreements without any escalation
  mechanism expose the supplier to margin erosion.
- Are prices inclusive or exclusive of packaging, handling, and freight?

**Index-linked / escalation pricing:**

- Which index is used? (CPI, PPI, sector-specific commodity index)
- Is the index specified precisely (e.g., "US BLS PPI for Industrial Chemicals,
  Commodity Code PCU325—325, not seasonally adjusted") or vaguely ("appropriate
  inflation index")?
- What is the base date for the index calculation?
- What is the adjustment frequency? (quarterly, semi-annually, annually)
- Are there caps and floors? (e.g., "escalation shall not exceed 5% in any 12-month
  period; escalation shall be not less than -2% in any 12-month period")
- Is the calculation methodology explicitly stated?

**Most Favored Customer (MFC/MFN) clauses:**

- Is the MFN narrow (compared only to direct sales channels) or wide (compared to any
  other buyer)?
- What is the "comparable customer" definition? (volume, geography, product mix)
- What is the remediation mechanism if MFN is breached? (retroactive price adjustment,
  termination, damages)
- [JURISDICTION-SPECIFIC] Wide MFN clauses can raise antitrust concerns in both the
  EU (TFEU Art. 101; EC review of Amazon e-book publisher MFNs) and the US (Sherman
  Act § 1, particularly where market power exists) [VERIFY]. Seek competition counsel
  review for broad MFN provisions in markets where either party has market power.
- What is the audit/verification mechanism? (price comparison audits, third-party
  verification, self-certification)

**Volume-tiered pricing:**

- Are the tier thresholds clearly defined?
- Does the pricing apply prospectively to orders above the threshold, or retroactively
  to all volumes once a threshold is crossed?
- What happens if minimum purchase volumes (MPVs) are not met?

**Common issues:**

- Vague escalation index references that invite disputes
- No cap on escalation in volatile markets (3–5% annual cap is market standard)
- No floor protecting sellers in deflationary environments (2% floor is common)
- Wide MFN provisions without antitrust counsel review
- No audit right to verify MFN compliance

**[JURISDICTION-SPECIFIC]:**

- **US**: Price escalation under multi-year fixed-price government contracts may be
  governed by FAR cost accounting standards [VERIFY]
- **EU**: Wide MFN clauses may require VBER Art. 5(1)(d) compliance assessment [VERIFY]
- **UK**: Price variation clauses in long-term supply contracts may be subject to
  UCTA 1977 reasonableness test in B2B contracts [VERIFY]

### 2. Delivery Terms (Incoterms 2020)

**Key elements to review:**

**For all Incoterms:**

- Confirm the Incoterm is from the current 2020 edition — always specify "Incoterms 2020"
- Confirm a specific named place is stated (e.g., "FCA Shanghai Port" not just "FCA")
- Confirm the Incoterm is appropriate for the mode of transport

**Risk and cost allocation by selected term:**

| Incoterm | Risk Transfer Point            | Seller Pays                                          | Buyer Pays                        | Best Use                                                                               |
| -------- | ------------------------------ | ---------------------------------------------------- | --------------------------------- | -------------------------------------------------------------------------------------- |
| **EXW**  | At seller's premises           | Nothing after ready                                  | Everything                        | Seller minimum obligation; problematic for buyer unfamiliar with export customs        |
| **FCA**  | To carrier nominated by buyer  | Export clearance, delivery to carrier                | Main carriage, import clearance   | **Best for containerized cargo**; FCA with Art. A6/B6 on-board B/L for LC transactions |
| **CPT**  | To first carrier               | Export + main carriage                               | Import, transit risk              | Non-maritime multimodal                                                                |
| **CIP**  | To first carrier               | Export + main carriage + insurance (ICC A, min 110%) | Import                            | Non-maritime; high insurance obligation on seller; preferred for manufactured goods    |
| **DAP**  | At named destination           | All except unloading                                 | Unloading + import                | Seller delivers door; buyer clears import                                              |
| **DPU**  | After unloading at destination | All including unloading                              | Import clearance only             | Seller responsible for unloading; replaces DAT (Incoterms 2010)                        |
| **DDP**  | At named destination           | Everything                                           | Nothing                           | Maximum obligation on seller; creates seller import agent issues in EU                 |
| **FAS**  | Alongside ship                 | Export clearance                                     | Loading + freight + insurance     | Bulk cargo alongside vessel only                                                       |
| **FOB**  | On board vessel                | Export + loading                                     | Freight + insurance + import      | **Not recommended for containerized cargo** — use FCA instead                          |
| **CFR**  | On board vessel                | Export + freight                                     | Transit risk + insurance + import | Bulk maritime only                                                                     |
| **CIF**  | On board vessel                | Export + freight + insurance (ICC C min)             | Transit risk + import             | Bulk maritime; note: CIP offers better insurance for manufactured goods                |

**FCA with on-board B/L (Incoterms 2020 Art. A6/B6):**
Parties may agree that the buyer will instruct its carrier to issue an on-board B/L to
the seller after loading, enabling the seller to present a clean on-board B/L to banks
under a letter of credit. If FCA is used with LC payment, confirm the Art. A6/B6
arrangement is expressly agreed in the contract or in the LC terms.

**Common issues:**

- FOB used for containerized cargo (risk passes at ship's rail but containers are
  handed to carrier at terminal — gap period where risk owner is unclear)
- No edition year specified ("Incoterms" without year creates version dispute)
- No named place (incomplete Incoterm)
- CIF used for high-value manufactured goods (only ICC (C) insurance — under-insured)
- DDP used where seller lacks EU importer registration (creates customs clearance failure)
- EXW with buyer in an unfamiliar country who cannot handle export customs

**CISG/Incoterms interaction:**
CISG risk of loss rules (Arts. 66–70) and Incoterms interact: the Incoterm typically
governs risk of loss allocation, but gaps in Incoterms may be filled by CISG. CISG
Art. 68 (risk in transit goods passes on contract formation) can create tension with
Incoterms delivery-point risk allocation — this is an active interpretive issue in
containerized cargo disputes.

**Tariff/Incoterms interaction:**
The Incoterm determines who is the **importer of record** — a first-order question for
tariff liability. EXW places all import duties on the buyer; DDP places all on the seller.
For goods subject to significant tariffs (e.g., Section 301 on Chinese-origin goods), the
importer-of-record designation should be stated explicitly, separate from the Incoterm.

### 3. Quality Specifications and Inspection Rights

**Key elements to review:**

**Quality specifications:**

- Are specifications incorporated by reference (drawing numbers, part numbers, spec
  sheets) or stated in the contract body?
- Are specifications versioned and dated? (Buyer's spec changes should not automatically
  flow into existing orders without agreement)
- Who bears cost for engineering changes / specification changes?
- Are applicable standards cited? (ISO 9001, AS9100, IATF 16949, USP/EP pharmacopeial,
  FDA 21 CFR Part 820 for medical devices)
- Is first article inspection (FAI) required for new parts?

**First Article Inspection (FAI):**
FAI is required for aerospace/defense (AS9102), automotive (PPAP process), and custom
components. Key elements of an FAI clause:

- FAI must be completed and approved before production shipments begin
- FAI documentation: dimensional report, material certification, functional test results
- Who approves FAI: buyer quality engineer sign-off (not just supplier sign-off)
- FAI re-trigger events: design changes, process changes, supplier changes, 12-month
  production gap (aerospace standard)
- FAI failure: supplier must correct and repeat FAI before first production shipment

**Acceptance Quality Level (AQL) Sampling:**

- ANSI/ASQ Z1.4 is the standard reference for attribute sampling (pass/fail inspection)
- AQL level selection by risk:
  - AQL 1.0: High-risk, safety-critical components
  - AQL 2.5: General commercial components (most common)
  - AQL 4.0: Lower-risk, commodity goods
- Automotive: Use AIAG PPAP Level 3 (customer approval) for production part approval
- Aerospace: AMS/AS standards may require 100% inspection for critical characteristics
- Contract must specify: AQL level, sample plan, inspection level (General I/II/III),
  and who performs inspection (buyer, third party, supplier self-certification)

**Inspection rights:**

- Does the buyer have the right to inspect at the supplier's facility during manufacture?
- Does the buyer have the right to audit the supplier's quality system?
- Are source inspection rights (pre-shipment inspection) specified?
- Who bears inspection costs?

**Acceptance procedure:**

- Is there a defined acceptance period after delivery?
- What are the acceptance criteria? (pass/fail vs. AQL sampling)
- What triggers deemed acceptance? (expiration of rejection period, payment, use of goods)
- **UCC § 2-606**: Acceptance occurs when the buyer (a) signifies conformity, (b) fails
  to make effective rejection, or (c) performs acts inconsistent with seller's ownership
  [VERIFY]
- **CISG Art. 38**: Buyer must examine goods within as short a period as is practicable
  in the circumstances [VERIFY]

**Rejection procedure:**

- What is the rejection notice period? (Must be specific and timely)
- **UCC § 2-602**: Rejection must occur within a reasonable time after delivery [VERIFY]
- **CISG Art. 39**: Buyer must give notice specifying non-conformity within reasonable
  time, no later than 2 years after goods received [VERIFY]
- What are the buyer's remedies upon rejection? (return, cover purchase, price reduction)
- What are the seller's cure rights? (UCC § 2-508 two-path cure; CISG Arts. 34, 37, 48)
- Who bears cost of return shipment for rejected goods?

**Latent defect provisions:**

- What is the warranty/defect claim period for latent defects discovered post-acceptance?
- Is there a distinction between patent defects (discoverable on inspection) and latent
  defects (hidden)?

**Common issues:**

- Specifications incorporated by reference to living documents (allows unilateral changes)
- No defined acceptance period (acceptance by default after delivery)
- Rejection notice must specify reasons but contract is silent — creates dispute risk
- No FAI clause for custom-manufactured goods
- Inspection cost allocation unclear
- No AQL sampling plan for production batches

### 4. Warranty Provisions and Product Liability

**Key elements to review:**

**CISG conformity vs. UCC warranty — important conceptual distinction:**
Under CISG Art. 35, the seller is _not_ required to give a "warranty" — it must deliver
goods that conform to the contract in quantity, quality, description, and packaging. This
is a strict conformity obligation, not a warranty. Parties often mistakenly apply UCC
warranty concepts (including disclaimer formalities) to CISG-governed contracts. Under
CISG Art. 6, parties may derogate from Art. 35 by express agreement; but unlike UCC, there
are no specific disclaimer formality requirements for international commercial parties.

**Implied warranties (jurisdiction-dependent):**

_UCC (US):_

- **§ 2-314 Merchantability**: Goods must pass without objection, meet fair average
  quality, be fit for ordinary purposes. Applies only to merchant sellers. To disclaim:
  clause must (a) mention "merchantability" and (b) be conspicuous (bolded heading,
  different font, prominent placement) [VERIFY]. "As is" or "with all faults" also
  disclaims all implied warranties without requiring specific words.
- **§ 2-315 Fitness for Particular Purpose**: Implied when seller knows buyer's purpose
  and buyer relies on seller's judgment. To disclaim: must be conspicuous and in writing.
- **§ 2-316(3)**: Examination disclaimer — if buyer has inspected goods or refused to
  inspect, no implied warranty as to defects examination should have revealed [VERIFY].
- **Conspicuousness test**: Courts apply a "no surprise" standard — would a reasonable
  person in the buyer's position be surprised to find the disclaimer? Physical characteristics
  alone (font size, bold) are not sufficient if the disclaimer is otherwise buried or
  presented post-purchase [VERIFY — active litigation in electronic commerce contexts].

_UK Sale of Goods Act 1979 / SSGSA 1994 (UK):_

- **s.12** (title), **s.13** (description), **s.14(2)** (satisfactory quality),
  **s.14(3)** (fitness for purpose) — all implied as conditions.
- B2B exclusion: possible if reasonable under UCTA 1977 s.6. B2C: cannot be excluded
  under Consumer Rights Act 2015 [VERIFY].

_CISG Art. 35 (conformity):_

- Seller delivers goods fit for ordinary use, fit for particular purpose if seller knew,
  possessing qualities of sample/model, adequately packaged [VERIFY].
- Parties may derogate (Art. 6). No formality for disclaimer in international B2B contracts.

**Express warranties:**

- What is the warranty period? (typical commercial: 12-24 months from delivery or
  first use, whichever is shorter)
- What does the warranty cover? (defects in materials and workmanship; design defects
  if seller designed the goods)
- What are the warranty remedies? (repair, replacement, refund — priority order matters)
- Is there a warranty claim procedure? (written notice, return authorization, time limits)
- Does warranty coverage require proper storage, installation, or use conditions?

**Remedy limitation (UCC § 2-719):**

- Does the contract limit warranty remedies to repair or replacement only?
- **Failure of essential purpose (§ 2-719(2))**: If the repair/replacement remedy fails
  its essential purpose, buyer may pursue any available remedy [VERIFY].
- **Independent vs. dependent approach** — courts are split: (a) "dependent" approach:
  consequential damages exclusion falls when the exclusive remedy fails; (b) "independent"
  approach: consequential damages exclusion stands unless independently unconscionable.
  Commercial contracts (not consumer goods) generally uphold consequential damage exclusions
  even when the exclusive remedy fails, unless the combined effect is unconscionable [VERIFY].
- Best practice: Draft the exclusive remedy and consequential damages exclusion as
  separately enforceable provisions with explicit "independent, severable" language.

**EU Product Liability Directive 2024/2853** (in force November 25, 2024):
[JURISDICTION-SPECIFIC] Applies to products placed on the EU market / put into service
after Member State transposition (deadline December 9, 2026):

- **What is a "product"**: Now includes software (including AI systems), digital
  manufacturing files, and firmware capable of autonomous behavior.
- **Who is liable (supply chain tiers)**:
  - **Primary**: Manufacturers (incl. component manufacturers and substantial modifiers)
  - **Secondary**: Importers and authorized representatives for non-EU manufacturers
  - **Fallback**: Distributors and fulfillment service providers (if primary/secondary
    not identifiable or unresponsive within 45 days)
- **Damage categories**: Now include data loss/corruption and psychological harm
  (in addition to death, personal injury, property damage)
- **Limitation period**: 25 years (extended from 10 years) for latent damage claims
- **Claimant presumptions**: Rebuttable presumption of defect and causation when
  proof is "excessively difficult" due to technical complexity or information asymmetry
- **AI and software**: Manufacturers liable for harm caused by autonomous post-sale
  AI system behavior, including failure to provide necessary safety updates
- **Supply contract implications**: Non-EU manufacturers must confirm EU authorized
  representative appointment; component manufacturers should allocate liability for
  defects attributable to their components; software update obligations must be defined;
  evidence retention period must align to 25-year long-stop

**Product recall:**

- Who can initiate a recall? (buyer's quality team, regulatory agency, internal test result)
- What quantity/percentage of defective units triggers a recall vs. isolated warranty claim?
  (Define "critical defect" threshold)
- **Notification timeline**: Supplier must notify buyer within [24-48 hours] of identifying
  a potential recall-triggering defect
- **Logistics**: Who manages reverse logistics? Who pays return freight?
- **Rework vs. destruction**: Who authorizes rework? Who issues destruction certificate?
- **Batch traceability**: Supplier must maintain MES/traceability data to enable batch
  recall; production date, facility, QC records, component sources
- **Cost allocation by causation**:
  - Supplier-attributable defect (materials, workmanship): supplier bears recall costs
  - Buyer design defect: buyer bears recall costs; supplier provides reasonable cooperation
  - Regulatory change: negotiated; typically buyer for non-defect recalls
- **Expense caps**: Per-event recall cost cap tied to annual contract value or insurance limit
- **Insurance coordination**: Supplier claims product liability insurance before seeking
  buyer reimbursement; provide insurance certificate evidence
- **Post-recall audit**: Buyer right to audit root cause analysis (RCA) and CAPA plan
- **Regulatory interface**: If FDA (21 CFR Part 806), CPSC, or EU enforcement agency
  orders recall, follow regulatory procedure (overrides contract procedure)

**Common issues:**

- UCC merchantability disclaimer does not mention "merchantability" by name
- Disclaimer not conspicuous (buried in standard-sized contract text, no bold/separate heading)
- Warranty period commences on delivery rather than on first use (shortening effective period)
- Repair/replace warranty without a refund or credit fallback if repair is impossible
- No failure-of-essential-purpose savings clause
- Consequential damages exclusion not drafted as independently severable
- Product recall cost allocation absent
- No authorized representative designation for non-EU products placed on EU market
- Software/firmware update obligations undefined (triggers EU PLD 2024/2853 liability)

### 5. Force Majeure, Commercial Impracticability, and Hardship

**Key elements to review:**

**Event definition:**

- Does the force majeure clause list specific triggering events or use a broad catch-all?
  (Specific lists are more predictable; broad catch-alls invite disputes)
- Are supply disruption events expressly included? (supplier insolvency, component
  shortages, raw material unavailability, logistics disruptions, cyber attacks)
- Are pandemic/epidemic events expressly included? (post-COVID drafting standard)
- Are sanctions and export control restrictions covered? (increasingly important)
- Are labor disputes at the supplier's facility covered? (common carve-out in favor of
  the party controlling labor relations)
- Are price increases or market disruptions excluded? (should be — these are commercial
  risks, not force majeure)
- Are tariff changes and trade policy actions excluded or included?
  (This is a critical design choice — see **Tariff Hardship** below)

**Tariff hardship — a separate and distinct mechanism from force majeure:**
Courts in the US (including _Kyocera Corp. v. Hemlock Semiconductor_, 7th Circuit) and
the UK have consistently held that new tariffs do not prevent contractual performance —
they merely make it more expensive. Tariff increases therefore fail the force majeure
impossibility/impracticability threshold unless the contract specifically includes
governmental trade actions as qualifying events.

For tariff risk, recommend a **hardship clause** rather than force majeure:

- **Hardship trigger**: "If a change in law (including executive order, trade remedy
  action, or tariff proclamation) after the contract date results in a documented
  increase in [party's] cost of performance exceeding [5%] of contract value per year,
  the affected party may request renegotiation within [30] days."
- **Renegotiation process**: Good faith negotiation for [30] days; if no agreement,
  either party may terminate on [60] days notice.
- **Termination right**: If renegotiation fails, mutual right to terminate without penalty.
- **Change-in-law definition**: Expressly includes executive orders, proclamations,
  Section 301/232/IEEPA tariff actions, and any governmental trade remedy — not just
  enacted legislation.
- **English law note**: English courts apply frustration only for impossibility (not cost
  increase). English-law contracts require explicit hardship/MAC clauses to address
  tariff-induced imbalance [JURISDICTION-SPECIFIC] [VERIFY].
- **Civil law note**: French Code civil Art. 1195 (imprévision), German BGB §§ 313–314
  (störung der geschäftsgrundlage), and Dutch BW Art. 6:258 codify hardship doctrines
  that may apply to tariff-driven imbalance — research local applicability [VERIFY].

**Notification obligations:**

- What is the notification period? (typically 5-30 days from event onset)
- What information must the notice contain? (nature of event, expected duration, steps to mitigate)
- What is the consequence of late notice? (typically loss of force majeure protection)

**CISG Art. 79 exemption (international contracts):**
[JURISDICTION-SPECIFIC] Under CISG Art. 79, a party is exempt from liability for
failure to perform if it proves the failure was due to an "impediment beyond its control"
that it could not reasonably have foreseen or avoided at contract formation, and that
it could not have overcome the impediment or its consequences [VERIFY].

- Art. 79 requires prompt notification of the impediment (Art. 79(4)) — failure to notify
  makes the party liable for damages that could have been avoided [VERIFY].
- Courts generally require a true impediment, not mere commercial difficulty; hardship
  (economic difficulty) is debated and often not sufficient on its own [VERIFY].
- CISG Art. 79 does not suspend performance — it only exempts the party from liability.
- CISG does not contain a hardship doctrine; parties must draft one expressly (Art. 6).

**Duration and termination:**

- How long must the force majeure event last before a termination right arises?
  (typical range: 30–180 days depending on contract value and supply criticality)
- Is there a mutual termination right or only one party's right?
- What happens to goods in transit or partially manufactured during force majeure?

**Relationship to UCC § 2-615 (commercial impracticability):**
[JURISDICTION-SPECIFIC] Under UCC § 2-615, a seller may be excused from non-delivery
if performance has been made impracticable by the occurrence of a contingency the
non-occurrence of which was a basic assumption on which the contract was made [VERIFY].
Mere increased costs (including tariff increases) do not meet this standard. Partial
impracticability requires pro-rata allocation to buyers (§ 2-615(b)) [VERIFY].

**Common issues:**

- Force majeure clause silent on pandemics (pre-COVID boilerplate)
- No supply disruption language — commodity shortages, logistics failures, component
  shortages not covered
- No tariff hardship clause — force majeure tested and found inapplicable for tariffs
- No notification period specified
- No mitigation obligation — creates moral hazard for affected party
- No termination trigger — force majeure can persist indefinitely
- Change-in-law clause drafted too narrowly (covers only statutes, not executive orders)

### 6. Supply Continuity and Business Continuity

**Key elements to review:**

**Business Continuity Plans (BCPs):**

- Is the supplier required to have and maintain a documented BCP?
- Does the buyer have audit rights over the BCP?
- What must the BCP cover? (identification of critical processes, prevention measures,
  recovery timeframes, succession plans, alternative supplier pre-qualification)
- How frequently must the BCP be updated and tested?
- Must the supplier share the BCP with the buyer? (confidentiality tensions arise here)

**Safety stock:**

- Is the supplier required to maintain a safety stock buffer?
- What quantity? (expressed as days of supply — typically 30-90 days for critical items)
- Where is the safety stock held?
- Who bears the carrying cost of safety stock?
- What triggers the right to draw on safety stock?

**Dual sourcing / alternative sourcing:**

- Does the agreement require the supplier to maintain dual sourcing capability?
- If so, who qualifies the alternative source?
- Is the alternative source pre-approved?
- Note: Courts may not enforce dual sourcing obligations prior to an actual disruption;
  the obligation must be clearly stated as a pre-disruption contractual duty [VERIFY]

**Shortage allocation:**

- Does the contract specify how the supplier allocates goods during supply shortages?
- Is allocation methodology objective and measurable? (e.g., "pro rata based on prior
  12-month purchase volumes" vs. vague "fair and equitable allocation")
- Non-discrimination principle: supplier should not allocate worse than to comparable
  customers in comparable circumstances
- Communication obligations during shortage (timing, content of notification)

**Capacity reservation:**

- Has the buyer reserved production capacity for minimum volumes?
- What is the notice period for capacity changes?
- What are the consequences if the buyer fails to use reserved capacity?

**Last-Time Buy / End-of-Life provisions:**

- How much notice must the supplier give before discontinuing a product or component?
- What minimum inventory must the supplier build for end-of-life orders?

**Common issues:**

- No BCP requirement for single-source strategic components
- Safety stock obligation without cost allocation (creating ambiguity about who pays)
- No shortage allocation methodology — invitation for disputes during scarcity
- No last-time-buy obligation for custom or semi-custom components
- No capacity reservation for high-volume long-term agreements

### 7. ESG and Sustainability Obligations

**Key elements to review:**

**General code of conduct / supplier standards:**

- Does the contract incorporate a supplier code of conduct or sustainability policy?
- Does the code cover: labor standards (ILO conventions), environmental standards,
  anti-bribery, human rights?
- Is the code enforceable? (incorporated by reference and made a contractual obligation)
- Does it apply to sub-suppliers (tier 2+)?

**Human rights and forced labor:**

- Are there express representations against use of forced, compulsory, or child labor?
- For goods with Xinjiang exposure, are UFLPA-specific representations included?
  (e.g., "Supplier represents and warrants that no goods delivered hereunder are
  wholly or partially mined, produced, or manufactured in the Xinjiang Uyghur
  Autonomous Region of China")
- Are there supply chain mapping and traceability requirements?
- What documentation must the supplier maintain for CBP audit purposes?

**Environmental and carbon obligations:**

- Does the contract require compliance with applicable environmental laws?
- Are there specific requirements for regulated materials (REACH, RoHS, PFAS restrictions)?
- Are carbon footprint reporting obligations included?
  - Scope 1 (direct supplier facility emissions)
  - Scope 2 (purchased energy)
  - Scope 3 product-level carbon footprint (kgCO2e per unit)
- Is data format specified? (GHG Protocol, Science-Based Targets initiative)
- What is the reporting frequency and deadline?
- Are decarbonization commitments binding or aspirational?

**Audit rights:**

- Does the buyer have audit rights over the supplier's ESG practices?
- Who can conduct the audit? (buyer directly, third-party auditor, accepted certification)
- How much notice is required for audits?
- What happens if the audit reveals non-compliance? (cure period, termination right)

**ESG-triggered termination:**

- Is ESG breach a termination for cause trigger?
- Is there a cure period before termination? (reasonable for remediable violations)
- What are the consequences of a material ESG violation?

**Reporting obligations:**

- Does the contract require the supplier to provide data for the buyer's own ESG
  reporting (CSDDD, CSRD, UK Modern Slavery Act statements, SEC climate disclosure)?
- What format and frequency?

**Common issues:**

- No forced labor representations despite Xinjiang supply chain exposure
- Audit rights limited to financial audits, not ESG/human rights audits
- ESG obligations apply only to tier 1 supplier, not flowed down to sub-suppliers
- No termination right for material ESG violations
- No supplier data requirements for buyer's own mandatory reporting
- No carbon footprint / Scope 3 data obligations despite CSRD or SEC disclosure requirements
- Code of conduct not incorporated as binding contractual obligation

**[JURISDICTION-SPECIFIC]:**

- **EU CSDDD (Directive 2024/1760)**: Single application date of July 26, 2029 (extended
  under "Omnibus I", Dec 2025). Applies to EU companies ≥ 1,000 employees / EUR 450M+
  global turnover; non-EU companies ≥ EUR 450M+ EU turnover. Requires contractual due
  diligence clauses with business partners. Civil liability for negligent/intentional
  failure to comply. Penalties up to 5% worldwide turnover [VERIFY]
- **Germany LkSG**: Coalition government announced abolition March 2026 [VERIFY —
  formal repeal legislation status uncertain as of this skill's creation date]
- **France Devoir de Vigilance (Loi 2017-399)**: Active enforcement; 30+ formal notices
  filed; civil liability under French law for failure to implement vigilance plan [VERIFY]
- **Norway Åpenhetsloven (effective July 1, 2022)**: Covers ALL supply chain tiers;
  annual due diligence report required [VERIFY]
- **UK Modern Slavery Act 2015 s.54**: Annual statement for entities with UK turnover
  ≥ £36M; contract audit rights support statement accuracy; weak historical enforcement
  but proposed reforms include fines and director disqualification [VERIFY]
- **US UFLPA (effective June 22, 2022)**: Rebuttable presumption imports from Xinjiang
  are prohibited; importers bear burden of proof; UFLPA Entity List applies [VERIFY]

### 8. Indemnification

**Key elements to review:**

- Is indemnification mutual or one-way? (supply contracts often have asymmetric
  indemnities: supplier indemnifies for product defects; buyer indemnifies for
  design specifications)
- **Product liability indemnification**: Does the supplier indemnify for defects
  attributable to the supplier's manufacturing or materials? Does the buyer indemnify
  for defects attributable to the buyer's design or specifications?
- **IP infringement**: Does the supplier indemnify for IP infringement claims arising
  from the goods as manufactured? Does the buyer indemnify for IP infringement arising
  from use of the buyer's design specifications?
- Is indemnification capped (subject to the liability cap) or uncapped?
- Indemnification procedure: notice obligations, right to control defense, right to
  settle, indemnitee's obligation to cooperate
- Relationship between indemnification and limitation of liability clause
- **EU PLD 2024/2853 allocation**: Component manufacturers should allocate liability for
  defects attributable to their components; supply contract should mirror PLD's supply
  chain liability tiers

[JURISDICTION-SPECIFIC]:

- **Common law**: Indemnity is a primary obligation distinct from damages for breach;
  different remoteness and limitation period rules may apply [VERIFY]
- **Civil law (EU)**: Indemnification is used under freedom of contract but may be
  interpreted as guarantee/suretyship; verify local characterization [VERIFY]

**Common issues:**

- No product liability indemnification split (supplier/buyer design responsibility)
- IP infringement indemnification does not carve out buyer-specified designs
- No control-of-defense provision (creates conflict of interest risks)
- Broad "any third party claim" indemnification not limited to specific risk categories
- No coordination with EU PLD liability tier allocation

### 9. Limitation of Liability

**Key elements to review:**

- Cap amount: fixed sum, multiple of fees/price paid in prior period, uncapped?
- Is the cap mutual or asymmetric?
- **Product recall carveout**: Product recall costs are often carved out of liability
  caps in supply agreements given their potentially massive scale
- Consequential damages exclusion: is it mutual? Does it exclude lost profits, loss of
  business, loss of data?
- **Carveouts from consequential damages exclusion**: death/personal injury from
  negligence, fraud, ESG material breach, willful misconduct, IP indemnification,
  product recalls
- Whether UCC § 2-719 unconscionability analysis is needed [JURISDICTION-SPECIFIC]
- **EU PLD carveout**: Directive 2024/2853 creates mandatory liability that cannot be
  excluded by agreement — any limitation clause should carve out Directive-imposed
  strict liability [VERIFY — per national implementing legislation]

[JURISDICTION-SPECIFIC]:

- **UCC § 2-719**: Limitation of consequential damages for commercial loss is not
  prima facie unconscionable. For consumer goods, limitation of consequential damages
  for personal injury is prima facie unconscionable [VERIFY]
- **UK UCTA 1977 s.2**: Cannot exclude liability for death or personal injury caused
  by negligence; other negligence exclusions subject to reasonableness test [VERIFY]

### 10. Intellectual Property

**Key elements to review:**

- **Tooling ownership**: Who owns tooling, dies, molds, and fixtures? (buyer typically
  retains ownership but supplier retains possession — specify return/access rights)
- **Custom development**: If the supplier develops bespoke designs or processes for
  the buyer, who owns the resulting IP?
- **Background IP**: Supplier's pre-existing IP incorporated into goods — buyer should
  receive a license for use but not ownership
- **Feedback/improvement clauses**: Any grant on buyer's process improvements or
  quality suggestions?
- **Trademark license**: If goods are branded with buyer's marks, specify license scope,
  quality control obligations, and termination of license rights

### 11–16. Standard Clause Checklist

For the remaining clause categories, review presence, reasonableness, and playbook
alignment. Flag deviations using the GREEN/YELLOW/RED system.

**11. Confidentiality**

- [ ] Scope of confidential information defined (includes technical specs, pricing, BCP details)
- [ ] Term appropriate (typically 3-5 years, or indefinite for trade secrets)
- [ ] Standard carveouts present (public domain, independent development, required disclosure)
- [ ] Permitted disclosures (affiliates, subcontractors, under NDA, SCF financiers)
- [ ] Return/destruction obligations on termination

**12. Term and Termination**

- [ ] Initial term and renewal terms clear
- [ ] Auto-renewal notice period adequate
- [ ] Termination for convenience right and notice period
- [ ] Termination for cause: cure period, specific trigger events (ESG breach, insolvency,
      quality failure, failure to maintain BCP, UFLPA violation, FEOC designation)
- [ ] Effects of termination: inventory disposition, transition obligations, tooling return,
      safety stock drawdown, wind-down period

**13. Governing Law and Dispute Resolution**

- [ ] Governing law clause present and unambiguous
- [ ] CISG opt-out (if parties prefer domestic law)
- [ ] Dispute resolution mechanism (litigation, arbitration, expert determination)
- [ ] Escalation process (executive negotiation → mediation → formal proceedings)
- [ ] For cross-border disputes: New York Convention enforcement considerations

**14. Compliance and Regulatory**

- [ ] Trade compliance: export controls (EAR, ITAR), sanctions (OFAC, EU, UK OFSI)
- [ ] Import compliance: customs classification (HS codes), origin documentation
- [ ] Rules of origin compliance (USMCA, CPTPP, GSP) and duty drawback eligibility
- [ ] Product safety standards: CE marking, FCC, UL, FDA registration as applicable
- [ ] Anti-bribery: representations under FCPA, UK Bribery Act 2010
- [ ] Audit rights for regulatory compliance

**15. Insurance**

- [ ] Product liability insurance (minimum coverage appropriate to goods risk profile)
- [ ] Cargo insurance (consistency with Incoterm obligations — who is responsible)
- [ ] Property insurance for buyer-owned tooling at supplier's facility
- [ ] Evidence of coverage requirements (certificates, endorsements)
- [ ] Note: EU PLD 2024/2853 expands damage categories — verify insurance covers
      data loss and psychological harm (new covered categories)

**16. Definitions and Boilerplate**

- [ ] Key supply chain terms defined (Goods, Specifications, Delivery, Acceptance,
      Defect, Incoterm, Force Majeure Event, Change in Law)
- [ ] Order of precedence for conflicting documents (Master Agreement, PO, Specifications,
      Quality Plan — state the hierarchy explicitly)
- [ ] Entire agreement clause
- [ ] Amendment provisions (written amendments only; PO supplements/ECNs addressed)
- [ ] Counterparts clause

### 17. Tariff and Customs Risk Allocation

**Key elements to review:**

**Who is the importer of record?**

- The importer of record is responsible for customs classification, duty payment, and
  CBP/HMRC/EU customs compliance. The Incoterm signals but does not definitively determine
  this — specify explicitly.
- For US imports: importer of record = liable for Section 301/232/IEEPA duties, trade
  remedy investigations, and Customs bonds.

**Tariff pass-through clause:**

- If tariffs on goods increase after contract date, does the price adjust?
- Pass-through formula: "If import duties applicable to the Goods increase by more than
  [5%] above the rate in effect on the Contract Date, Seller may increase the Contract
  Price by the documented increase in duty cost, effective [30] days after written notice."
- One-sided vs. mutual: If tariffs decrease, does buyer benefit from a price reduction?
- Timing: Prospective from notice date, or retroactive to the tariff effective date?

**Tariff hardship clause (preferred to reliance on force majeure):**
Courts have consistently held that tariff increases do not meet the force majeure
impossibility threshold. A hardship clause provides a renegotiation right instead:

- **Trigger**: Any change in law (including executive orders, Section 301/232/IEEPA
  actions, trade remedy orders) that materially changes the cost structure of performance
  by more than [X%] of contract value.
- **Mechanism**: Affected party notifies in writing within [30] days of the tariff change.
  Parties negotiate in good faith for [30] days to adjust the terms.
- **Failure**: If renegotiation fails, either party may terminate on [60] days notice
  without liability (other than for goods in process or in transit).
- **Change-in-law definition**: Must expressly include executive orders, presidential
  proclamations, and administrative trade remedy actions — not just statutes.

**Customs classification and HS codes:**

- What HS (Harmonized System) code do the parties agree applies to the goods?
- If the customs authority reclassifies the goods to a higher-duty HS code, who bears
  the additional duties and any penalties?
- Who provides country of origin certification (USMCA Certificate, EUR.1 for EU)?
- Who bears liability for origin misrepresentation (typically the party providing the cert)?

**Duty drawback:**

- If goods are re-exported after import, does the importer of record qualify for duty
  drawback (refund of duties on exported goods)?
- Does the contract require the supplier to provide documentation for drawback claims?

**Rules of origin compliance:**

- For FTA preferential treatment (USMCA, CPTPP, EU FTAs): which party warrants the
  goods meet applicable rules of origin?
- Post-Brexit: UK origin vs. EU origin may trigger cumulation issues in some FTAs.
- China tariff avoidance through third countries: does the contract require the supplier
  to warrant that goods are not subject to anti-circumvention investigations?

**Common issues:**

- FOB terms with no clarification of who pays tariffs on imported goods
- Tariff pass-through formula not indexed to actual tariff rate (disputes on calculation)
- No right to terminate if tariffs exceed threshold (leaves buyer exposed indefinitely)
- Rules of origin unverified at contract execution (USMCA/CPTPP violations create buyer liability)
- No audit right to verify origin documentation
- Change-in-law clause narrowly drafted (covers only statutes, not executive orders)

**[JURISDICTION-SPECIFIC]:**

- **US**: Section 301 duties on Chinese-origin goods (up to 25%); Section 232 national
  security tariffs on steel/aluminum; new IEEPA-authority executive order tariffs (2025)
  [VERIFY current tariff schedules]. Foreign Trade Zones (FTZ) can defer duty payments.
- **EU**: Common External Tariff (CET) applies to imports; duty suspension programs
  available for some sectors. Anti-dumping duties apply in addition to CET for many goods.
- **UK**: UK Global Tariff (UKGT) differs from EU CET post-Brexit; check Tariff Schedule.
- **China**: Export tariffs on certain rare earth and critical minerals (gallium, germanium,
  graphite); China Customs documentation requirements for export [VERIFY].
- **USMCA**: Goods must meet content requirements; rules of origin certification required
  for preferential treatment.

### 18. Supply Chain Finance

**Key elements to review:**

**Supply chain finance (SCF) / reverse factoring mechanics:**
The buyer approves supplier invoices on an SCF platform; the supplier elects early payment
from a bank/financier at a discount based on the buyer's credit rating; the buyer pays the
financier at the original extended maturity. The ICC/BAFT Global Supply Chain Finance
Forum Standard Definitions (2021) is the authoritative terminology framework.

**Anti-assignment clause conflict:**
SCF relies on assignment of receivables from supplier to financier. Supply contracts with
**anti-assignment clauses** can block this mechanism. Check:

- Does the confidentiality or assignment clause prohibit assignment of payment rights?
- Does the contract require buyer consent for receivables assignment?
- [JURISDICTION-SPECIFIC] Under English law, some restrictions on assignment of
  receivables are unenforceable for SME receivables in certain contexts [VERIFY].
- Add a carve-out: "Notwithstanding any anti-assignment provision, Supplier may assign
  receivables arising under this Agreement to financial institutions for supply chain
  finance purposes without Buyer's consent, provided Seller notifies Buyer of the
  assignment."

**Set-off rights:**

- Does the buyer retain contractual set-off rights against the supplier (e.g., for warranty
  claims, price adjustments, or disputes)?
- If receivables are assigned to an SCF financier, set-off rights may follow the receivable
  and be asserted against the financier — creating a risk the financier will not accept.
- Solution: Define which receivables are eligible for SCF (exclude disputed receivables,
  receivables subject to pending warranty claims, or any receivables where set-off has
  been asserted).

**Confidentiality of payment terms:**
SCF programs often feature extended buyer payment terms (120+ days) that suppliers accept
in exchange for early-payment access. Following IASB/IFRS 7 and IAS 7 amendments
(effective January 1, 2024), companies must disclose supplier finance arrangements in
financial statements. [VERIFY — national adoption status varies.]

**Common issues:**

- Anti-assignment clause unintentionally blocks SCF program (defeats program purpose)
- Confidentiality clause blocks SCF provider from accessing order/invoice data
- No carve-out for buyer's audit rights of SCF-related transactions
- Supplier assumes financier liens without explicit acknowledgment
- No definition of "eligible receivables" (disputed receivables create SCF exposure)

---

## Critical Minerals and Rare Earth Supply Provisions

For supply agreements involving critical minerals (lithium, cobalt, nickel, natural
graphite, rare earth elements, gallium, germanium, tin, tantalum, tungsten, gold), apply
this additional analysis layer:

**Price reopener with indexed floor/ceiling:**
Critical mineral prices are highly volatile (lithium fell ~75% in 2023; cobalt and rare
earths subject to significant swings). Market practice for medium/long-term offtake agreements:

- Index reference: LME price, Fastmarkets, S&P Global Commodity Insights (specify exactly)
- Base price date: contract execution date
- Reopener trigger threshold: price change exceeding [X%] within [rolling period]
- Collar: cap and floor on price movement (e.g., not more than 15% above/below base price
  within any 12-month period)
- If collar is breached: automatic trigger of good faith renegotiation; termination right
  if no agreement within [60] days

**Volume commitment / take-or-pay:**

- Minimum annual / quarterly purchase volumes (financial commitment if not met)
- Take-or-pay formula: if buyer fails to purchase minimum, pay [X%] of contract value
  for undelivered quantities
- Shelf-life risk: who bears obsolescence / inventory build risk for buyer forecast errors?

**Traceability and chain of custody:**

- Supplier must maintain audit trail from mine/refinery to product
- Compliance with: EU Battery Regulation 2023/1542 (from Feb 2025), Dodd-Frank § 1502,
  EU Conflict Minerals Regulation 2017/821 (for 3TG)
- Supplier must provide annual conflict minerals audit report (OECD Framework or RMI)
- Chain-of-custody documentation must support EU Battery Regulation passport requirements

**FEOC / Regulatory status warranty:**
For US IRA Clean Vehicle Credit compliance, suppliers must not be a "Foreign Entity of
Concern" (FEOC) under IRS Treasury regulations [VERIFY — annual updates]:

- Ongoing warranty: "Supplier warrants it is not, and will promptly notify Buyer if it
  becomes, a Foreign Entity of Concern under applicable IRA regulations."
- Notification obligation within [5] business days of FEOC designation
- Buyer termination right on FEOC designation without penalty

**Government intervention / export restriction force majeure:**
Expressly covers governmental export licensing requirements, export bans, and nationalization
affecting mineral supply as excusing events (distinct from commercial hardship):

- "Governmental action" force majeure defined to include export licensing failures,
  export bans or restrictions imposed by any government, nationalization, and
  requisitioning of the relevant minerals.
- Notification procedure: within [5] business days of knowledge of the government action
- If force majeure exceeds [90] days: mutual right to terminate

**ESG and responsible sourcing covenant:**

- Compliance with LME responsible sourcing standard (cobalt, tin)
- OECD Due Diligence Guidance for Responsible Supply Chains of Minerals from
  Conflict-Affected and High-Risk Areas
- Third-party audit right (buyer or recognized third-party auditor)
- Annual responsible sourcing report to buyer

---

## CISG Anticipatory Breach and Damages Reference

For supply contracts governed by CISG (Arts. 71–77), apply this additional analysis:

### Arts. 71–73: Anticipatory Breach and Suspension

**Art. 71 — Suspension of Performance:**
A party may suspend its performance if, after the contract's conclusion, it becomes
apparent that the other party will not perform a substantial part of its obligations due
to: (a) serious deficiency in ability to perform or creditworthiness, or (b) conduct
in preparation for or in performance of the contract.

Practical triggers: supplier's solvency warning signs, early-delivery quality failures
on installment contracts, loss of export license, force majeure notice suggesting systemic
inability to supply.

Art. 71 requires the suspending party to notify the other party immediately. If the other
party provides "adequate assurance" of performance, the suspending party must resume.

**Art. 72 — Avoidance Before Performance Date:**
If before the date for performance it is clear that a party will commit a fundamental breach,
the other party may declare the contract avoided. "Clear" is a high threshold — probable
or foreseeable is not enough; the non-performance must appear certain.

The party intending to avoid must notify promptly; the other party may cure by providing
adequate assurance (unless it has declared it will not perform).

**Art. 73 — Installment Contracts:**
For goods delivered in installments over time, a party may avoid the installment if the
other party's failure in respect of that installment constitutes a fundamental breach of
that installment. If the failure creates well-founded grounds that a fundamental breach
will occur in future installments, a party may avoid prospectively.

**Review questions for installment supply contracts:**

- Does the contract define what constitutes a "fundamental breach" for each installment?
- Is there a cure or notice period before avoidance of an installment?
- Does quality failure on one batch automatically trigger avoidance of future deliveries?

### Arts. 74–77: Damages Calculation

**Art. 74 — Full Compensation:**
Damages = actual loss + lost profits, capped at what the breaching party **foresaw or
ought to have foreseen at the time of contract conclusion** as a possible consequence.
Note: unlike UCC § 2-715, no separate "special circumstances" advance notice is required
— the foreseeability standard is embedded in Art. 74 itself. Downstream contract losses
(lost sales to the buyer's customers) are recoverable if foreseeable.

**Art. 75 — Substitute Transaction (Cover Damages):**
If the contract is avoided and the aggrieved party has made a substitute transaction
(cover purchase at higher price, or resale at lower price) in a reasonable manner within
a reasonable time, it may recover: (contract price – substitute transaction price) +
additional damages under Art. 74. Art. 75 takes precedence over Art. 76 when a
substitute transaction exists.

**Art. 76 — Market Price (Abstract Damages):**
If no substitute transaction, and the goods have a current market price, damages =
(contract price – market price at avoidance or possession date) + additional damages.
Art. 76 is used when no cover transaction occurs; it provides an objective benchmark.

**Art. 77 — Duty to Mitigate:**
The aggrieved party must take measures reasonable in the circumstances to mitigate
its loss. Failure to mitigate allows the breaching party to claim a reduction in damages
equal to the loss that should have been mitigated. Art. 77 may require a cover purchase
(rather than relying on abstract Art. 76 calculation) if one was available and reasonable.

**Key differences from UCC:**

- UCC § 2-715(2) consequential damages require advance notice of special circumstances;
  CISG Art. 74 does not require advance notice — foreseeability assessed at contract formation.
- Attorney fees are not recoverable as damages under CISG Art. 74 (Eighth Circuit) [VERIFY].
- UCC § 2-708(2) lost-volume seller damages have no direct CISG equivalent (though Art. 74
  may produce similar recovery in appropriate cases) [VERIFY].
- CISG Art. 77 requires positive mitigation action; the non-defaulting party cannot
  passively wait and claim full market price under Art. 76 if cover was available.

**Contract provisions to address:**

- Expressly cap consequential damages or define the scope of "foreseeable" loss at contract
  formation (to limit the open-ended Art. 74 exposure)
- Define the substitute transaction methodology and timeframe (to anchor Art. 75 calculations)
- Include a CISG opt-out if parties prefer domestic law: "The parties exclude the
  application of the United Nations Convention on Contracts for the International Sale
  of Goods (CISG)."

---

## Deviation Severity Classification

### GREEN — Acceptable

Clause aligns with or is better than the organization's standard position. Minor
variations that are commercially reasonable and do not materially increase risk.

**Supply chain examples:**

- Warranty period of 18 months when standard is 12 months (better for buyer)
- FCA used instead of FOB for containerized cargo (correct use of Incoterms)
- Escalation cap of 3% when market average is 5% (more protective for buyer)
- CISG expressly excluded when parties prefer domestic law
- CIP used instead of CIF for manufactured goods (better insurance standard)

**Action**: Note for awareness. No negotiation needed.

### YELLOW — Negotiate

Clause falls outside standard position but within negotiable range. Common in the
market but not preferred. Requires attention and likely negotiation, but not escalation.

**Supply chain examples:**

- Index-linked escalation without a cap or floor
- FOB term used for containerized cargo (wrong Incoterm choice)
- Warranty disclaimer does not use the word "merchantability" (may be ineffective)
- Force majeure clause silent on pandemics or supply disruptions
- Safety stock obligation without cost allocation
- MFN clause without audit mechanism
- Shortage allocation methodology vague ("fair and equitable" without formula)
- No tariff hardship clause in a cross-border multi-year agreement
- Anti-assignment clause that blocks potential SCF program
- CISG not addressed in an international supply contract

**Action**: Generate specific redline language. Provide fallback position. Estimate
business impact.

### RED — Escalate

Clause falls outside acceptable range, triggers a defined escalation criterion, or poses
material legal or commercial risk.

**Supply chain examples:**

- No inspection or acceptance procedure (acceptance by default risk)
- Warranty disclaimer fails UCC § 2-316 conspicuousness requirement (likely invalid)
- No force majeure clause and no UCC § 2-615 discussion (supply disruption unaddressed)
- No ESG representations for goods with Xinjiang or high-risk supply chain exposure
- Product recall cost allocation entirely on buyer for supplier-attributable defects
- Uncapped indemnification for any third-party claim (not limited to product liability)
- No CISG opt-out in an international contract where parties did not intend CISG to apply
- No governing law clause
- No EU authorized representative for non-EU goods placed on EU market (EU PLD exposure)
- No tariff pass-through or termination right when contract has significant Section 301/232 exposure

**Action**: Explain specific risk (with legal basis where possible). Provide
market-standard alternative language. Estimate exposure. Recommend escalation path.

---

## Redline Format

For each YELLOW and RED deviation:

```
**Clause**: [Section reference and clause name]
**Current language**: "[exact quote from the contract]"
**Proposed redline**: "[specific alternative language]"
**Rationale**: [1-2 sentences suitable for external sharing]
**Legal basis**: [Relevant statute/regulation/principle, or "General commercial practice"]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative position if primary redline is rejected]
```

### Redline Best Practices

1. **Be specific**: Provide exact language. Redlines must be ready to insert.
2. **Adapt to goods context**: Warranty and inspection redlines differ materially from
   service contract redlines. Use supply chain–appropriate terminology.
3. **Lead with the legal basis**: For UCC, CISG, and UK SGA issues, cite the relevant
   section to support the position.
4. **Provide fallback positions**: For YELLOW items, always include a fallback.
5. **Prioritize by deal impact**: Product recall exposure, ESG compliance gaps, and tariff
   exposure rank higher than minor definitional preferences.
6. **Respect the relationship**: If this is a strategic sole-source supplier, maintain
   collaborative tone. If this is a commodity supplier, a firmer tone is appropriate.
7. **Flag unverified citations**: If citing a statute from memory, mark [VERIFY].

---

## Negotiation Priority Framework

Organize redlines by negotiation priority:

### Tier 1 — Must-Haves (Deal Breakers)

Issues where the organization cannot proceed without resolution:

- No governing law clause or CISG not addressed where CISG applies
- No inspection or acceptance procedure (acceptance-by-default risk)
- ESG/forced labor representations absent for high-risk supply chains
- Product recall cost allocation entirely adverse for material recall risk
- Uncapped indemnification for product liability
- No limitation of liability clause
- No EU authorized representative where goods are placed on EU market (EU PLD exposure)
- No UFLPA representations for goods with potential Xinjiang supply chain exposure

### Tier 2 — Should-Haves (Strong Preferences)

Issues that materially affect risk but have negotiation room:

- Tariff hardship clause for cross-border multi-year agreements with significant tariff exposure
- Escalation cap/floor on index-linked pricing
- Force majeure clause updated for supply disruption, pandemic events, and government action
- Supply continuity/BCP requirements for critical components
- Warranty disclaimer formality compliance (conspicuousness under UCC § 2-316)
- Shortage allocation methodology — objective formula vs. vague standard
- Safety stock obligation with cost allocation
- Critical minerals FEOC warranty for IRA-relevant supply contracts

### Tier 3 — Nice-to-Haves (Concession Candidates)

Issues that improve the position but can be conceded strategically:

- Preferred Incoterm when proposed term is acceptable but not ideal
- MFN audit mechanism (where MFN clause itself is acceptable)
- Insurance certificate requirements
- Anti-assignment carve-out for SCF program (unless SCF program is active)
- Minor definitional improvements to technical specifications
- Boilerplate refinements

**Negotiation strategy**: Lead with Tier 1 items. Trade Tier 3 concessions to secure
Tier 2 wins. Never concede on Tier 1 without escalation to senior procurement counsel.

---

## Quality Assurance Framework

### PDCA Quality Cycle

Apply structured discipline to every supply contract review:

**PLAN**: Identify goods type, user's side, governing goods framework (UCC/CISG/SGA),
tariff exposure, ESG exposure, and playbook position. Classify complexity (standard PO
terms / bespoke supply agreement / strategic sole-source / critical minerals offtake).

**DO**: Execute the clause-by-clause analysis. Run ESG screen and Incoterms screen.
Run tariff risk screen. Generate redlines. Score severity.

**CHECK**: Run Citation Quality Gates. For any RED item, run Self-Interrogation. Verify
statutory references (UCC sections, SGA sections, ESG statutes, EU PLD 2024/2853).
Confirm all 18 clause categories addressed.

**ACT**: Note any novel supply chain clause structures or emerging market practices
(e.g., CSDDD Omnibus I developments, new UFLPA Entity List additions, IEEPA tariff
actions). Flag for playbook update.

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                                                | Fail Action                                              |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established principle                                                    | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction                                                         | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments or repeal — UCC, ESG statutes, Incoterms editions, and EU directives evolve frequently | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the contract's governing law. No UCC concepts applied to CISG contracts or vice versa                         | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden                                                                                           | Add confidence qualifier                                 |

### Self-Interrogation for RED Items

For any clause classified as RED, apply this 3-pass self-interrogation:

**Pass 1 — Legal Chain Integrity**:

- Does the risk assessment follow logically from the statute/principle cited?
- Would a court in this jurisdiction actually reach this conclusion on these facts?
- Is there a counter-argument the counterparty's counsel will make?

**Pass 2 — Completeness**:

- Have all relevant goods-law statutes been considered (UCC, CISG, SGA as applicable)?
- Have ESG obligations across all relevant jurisdictions been screened?
- Have tariff and customs risks been assessed?
- Are there regulatory dimensions (product safety, EU PLD, import/export controls) not yet addressed?

**Pass 3 — Challenge**:

- What is the strongest argument that this clause IS acceptable?
- Under what commercial circumstances might a reasonable procurement lawyer accept this risk?
- Is the RED classification proportionate, or is this actually YELLOW with mitigations?

If any pass reveals a weakness, revise before delivery. Mark audit trail with
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material clause analysis, assign a confidence level:

| Level        | Range     | Meaning                                          | Action                                                   |
| ------------ | --------- | ------------------------------------------------ | -------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled law, clear statute, no ambiguity         | State with confidence                                    |
| **High**     | 0.80-0.94 | Strong authority, minor interpretation questions | State with brief caveat                                  |
| **Probable** | 0.60-0.79 | Good arguments but reasonable minds could differ | State with explicit reasoning and contra-indicators      |
| **Possible** | 0.40-0.59 | Genuinely uncertain, competing authorities       | Flag for counsel review with both sides of the argument  |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative                          | Do not assert; flag as "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every supply contract review output MUST include a Glass Box audit section:

```yaml
glass_box:
  contract: "[Contract title and date]"
  contract_type: "[Supply Agreement / PO with General Terms / Manufacturing Agreement / Critical Minerals Offtake / etc.]"
  user_side: "[Buyer / Supplier / Manufacturer]"
  governing_law: "[Jurisdiction]"
  goods_framework: "[UCC Article 2 / CISG / UK SGA 1979 / other]"
  cisg_applies: "[Yes — excluded / Yes — applies / No — domestic parties]"
  incoterm_used: "[Term and named place, or 'None specified']"
  incoterms_version: "[Incoterms 2020 / Incoterms 2010 / Version not specified]"
  esg_flags_triggered: "[CSDDD / UK MSA / UFLPA / France Vigilance / Norway Aapenhetsloven / Conflict Minerals / EU Battery Reg / None]"
  eu_pld_applies: "[Yes — 2024/2853 / Yes — 85/374/EEC (pre-transposition) / No]"
  tariff_risk_screened: "[Yes — Section 301/232/IEEPA / Yes — EU CET / Yes — UK UKGT / No]"
  critical_minerals: "[Yes — [mineral list] / No]"
  playbook_used: "[Playbook name or 'General commercial standards']"
  clauses_reviewed: 18
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to temp file or 'Not created']"
  statutes_consulted:
    - "[Statute 1 — VERIFIED (legalcode-mcp) or UNVERIFIED]"
    - "[Statute 2 — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  case_law_consulted:
    - "[Case 1 — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified legal review"
```

---

## Multi-Stakeholder Mapping

For every supply contract, identify ALL affected stakeholders:

| Stakeholder                      | Role              | Affected Clauses                    | Impact     | Action Required                                                     |
| -------------------------------- | ----------------- | ----------------------------------- | ---------- | ------------------------------------------------------------------- |
| Buyer (procurement)              | Contracting party | All                                 | Primary    | Sign / Negotiate                                                    |
| Supplier                         | Contracting party | All                                 | Primary    | Sign / Negotiate                                                    |
| Sub-suppliers (tier 2+)          | Third party       | ESG, BCP, quality                   | Indirect   | ESG flowdown required                                               |
| End customers                    | Third party       | Warranty, product recall, liability | Indirect   | Product recall protocol                                             |
| Data subjects                    | Third party       | Confidentiality, data protection    | Indirect   | GDPR/data protection overlay if personal data involved              |
| Customs/trade authority          | Regulator         | Incoterms, import/export compliance | Compliance | UFLPA, sanctions, export controls, tariff obligations               |
| ESG regulator                    | Regulator         | ESG, sustainability                 | Compliance | CSDDD, UK MSA, Vigilance Law, Åpenhetsloven reporting               |
| EU market surveillance           | Regulator         | EU PLD 2024/2853, product safety    | Compliance | Authorized representative, safety updates, 25-year record retention |
| Quality/product safety regulator | Regulator         | Warranty, product recall, specs     | Compliance | Product safety law obligations                                      |
| Logistics providers              | Third party       | Delivery, insurance, risk of loss   | Indirect   | Incoterm obligations                                                |
| SCF financier                    | Third party       | Assignment of receivables, set-off  | Indirect   | Anti-assignment carve-out, eligible receivables definition          |
| Insurers                         | Third party       | Insurance, liability                | Indirect   | Certificate requirements, EU PLD expanded damage categories         |

---

## Anti-Patterns

Explicit catalogue of what NOT to do in supply chain contract review:

1. **Ignoring the goods law framework** — Applying general contract law without
   identifying whether UCC Article 2, CISG, or UK SGA 1979 governs. Each has materially
   different implied warranty regimes, inspection timelines, and remedy structures. Always
   identify the applicable goods law first.

2. **Missing the CISG default-applies trap** — Assuming domestic law governs an
   international supply contract without checking whether CISG applies by default. If
   both parties are in CISG contracting states and the contract does not exclude CISG,
   CISG governs even if the contract says "subject to laws of New York State."

3. **Conflating CISG conformity with UCC warranty** — CISG Art. 35 creates a strict
   conformity obligation, not a "warranty" in the UCC sense. Applying UCC warranty
   disclaimer formalities (conspicuousness, mention of "merchantability") to a
   CISG-governed contract is a conceptual error — CISG Art. 35 is derogated by agreement
   (Art. 6), not disclaimed by magic words.

4. **Accepting FOB for containerized cargo** — FOB is designed for bulk goods loaded
   directly onto vessels. For containerized cargo, risk passes when the container is
   handed to the carrier at the terminal, not when it crosses the ship's rail. Use FCA
   for containerized shipments. FOB for containerized cargo creates a gap period where
   risk ownership is ambiguous.

5. **Failing to check warranty disclaimer conspicuousness** — Under UCC § 2-316, a
   disclaimer of the implied warranty of merchantability must (a) mention the word
   "merchantability" and (b) be conspicuous. A disclaimer buried in standard-sized
   contract text, or that uses only general "as is" language without mentioning
   merchantability, may be legally ineffective. Always verify these formalities.

6. **Treating tariff increases as force majeure events** — Courts (including the 7th
   Circuit in _Kyocera Corp. v. Hemlock Semiconductor_) have consistently held that
   tariff-driven cost increases do not prevent performance — they merely make it more
   expensive. Force majeure fails unless the contract specifically lists governmental
   trade actions as qualifying events. Use a separate hardship clause for tariff risk.

7. **Treating force majeure as covering price increases** — Force majeure excuses
   non-performance due to extraordinary events. Market price increases, raw material
   cost escalation, and exchange rate movements are commercial risks — not force majeure
   events — unless the agreement expressly and specifically provides otherwise.

8. **No ESG screening for high-risk supply chains** — Supply chain ESG is legally
   mandatory in major markets (UFLPA since June 2022, UK MSA since 2015, France Vigilance
   Law since 2017, CSDDD from 2029). Reviewing a supply agreement without running an ESG
   screen is a material omission. Identify the origin of goods and applicable mandatory
   due diligence regimes before starting the clause review.

9. **Relying on vague shortage allocation language** — "Fair and equitable allocation"
   clauses invite litigation. A supplier with multiple large customers during a shortage
   will apply its own internal criteria if the contract provides no formula. Always
   push for objective allocation criteria (e.g., "pro rata based on average monthly
   purchases in the prior 12 months").

10. **Accepting acceptance by default without a defined period** — If the contract does
    not specify an inspection period and rejection procedure, the buyer may be deemed
    to have accepted goods after a "reasonable time" — which a court will determine
    after the fact. This is particularly dangerous for latent defects.

11. **No product recall cost allocation** — Product recalls can cost tens or hundreds
    of millions. A supply contract that does not address who pays for a recall — and under
    what circumstances — leaves a major exposure entirely unallocated.

12. **Over-relying on UCC § 2-615 commercial impracticability** — Parties sometimes
    omit a force majeure clause, assuming UCC § 2-615 will cover them. UCC § 2-615
    has a very high bar: increased cost alone is not enough; the contingency must have
    been a basic contractual assumption. Courts have rejected § 2-615 defenses for
    events including COVID-19 in some jurisdictions. Always include an express force
    majeure clause.

13. **Ignoring Incoterm and insurance alignment** — CIP requires ICC (A) all-risk cover
    at minimum 110%; CIF requires only ICC (C) limited perils. For manufactured goods,
    components, or electronic equipment shipped under CIF, the buyer may be significantly
    underinsured during the main carriage leg. Flag the insurance standard whenever
    CIF or CIP terms are used.

14. **Single-source dependency without continuity obligations** — Reviewing a sole-source
    supply agreement without flagging the absence of BCP, safety stock, and shortage
    allocation provisions is a material omission. Single-source supply creates
    concentration risk; the contract must mitigate it.

15. **Tooling ownership ambiguity** — Many supply disputes arise over tooling (dies,
    molds, fixtures) paid for by the buyer but held at the supplier's facility. Without
    a clear ownership clause, the supplier may refuse to release tooling on termination
    or insolvency.

16. **Reviewing the delivery term in isolation** — The Incoterm, the insurance obligation,
    the force majeure clause, and the risk-of-loss provisions interact. Analyze these
    clauses together: an FOB term means risk passes at the vessel; but if the contract
    has a broad force majeure covering "transportation disruptions," the supplier may
    seek force majeure protection for events that occur after risk has already passed.

17. **Missing ESG termination triggers** — A supplier code of conduct that creates
    obligations but has no enforcement mechanism is a paper commitment. Confirm that
    material ESG violations (UFLPA Entity List addition, labor law conviction, child
    labor finding) are expressly listed as termination for cause triggers.

18. **Not flagging the CISG remedy hierarchy** — Under CISG, the buyer's remedy for
    non-conforming goods follows a hierarchy: require repair, require substitute goods
    (only for fundamental breach), reduce price, or avoid the contract (only for
    fundamental breach). This differs significantly from UCC's "perfect tender rule"
    (§ 2-601). Applying UCC remedy logic to a CISG-governed contract overstates
    the buyer's rejection rights.

19. **Assuming price escalation caps are not needed** — In multi-year fixed-price
    agreements, sellers will often accept uncapped CPI or PPI escalation because it
    appears conservative. But in high-inflation environments, an uncapped escalation
    clause can result in significant price increases that were not modeled at signing.
    Always push for a cap (typically 3–5% per year) and a floor.

20. **Ignoring the EU Product Liability Directive 2024/2853 for EU-bound goods** —
    The new directive (in force November 25, 2024; transposition December 9, 2026)
    expands liability to software, AI, and digital products; extends the long-stop
    period to 25 years; and requires non-EU manufacturers to appoint EU authorized
    representatives. Reviewing supply contracts for EU-destined goods without flagging
    the EU PLD supply chain tier allocation is a material omission.

21. **Anti-assignment clause blocking SCF without flagging** — Confidentiality and
    anti-assignment clauses are often drafted broadly enough to inadvertently block
    supply chain finance programs (which require assignment of receivables to financiers).
    If the buyer or supplier has an existing SCF program, always check whether contract
    assignment provisions would block it.

22. **Missing change-in-law clause for IEEPA/executive order tariffs** — Many supply
    contracts include change-in-law provisions that cover only statutes (Acts of
    Congress, SI, Directives). Executive orders and presidential proclamations — the
    vehicle for IEEPA authority tariffs, Section 232, and emergency trade actions —
    are not statutes. A narrowly drafted change-in-law clause will not cover them.
    Always confirm the definition of "Change in Law" expressly includes executive orders,
    presidential proclamations, and administrative agency trade remedy actions.

---

## Writing Standards

Apply plain-language discipline to all output:

**For redline rationales** (shared with counterparty's counsel):

- Plain language. No jargon or filler.
- Active voice: "The seller must disclaim merchantability by name" not "The merchantability
  disclaimer must mention merchantability by name."
- Short sentences. One point per sentence.
- Name the actor: "Supplier must..." not "It shall be required that..."
- Specific and cited: "UCC § 2-316 requires the word 'merchantability' to appear in the
  disclaimer" not "this may have enforceability issues."

**For internal analysis:**

- Same plain-language standards
- More technical legal analysis permitted (UCC section cites, ESG statute references)
- Confidence qualifiers where appropriate
- Glass Box audit trail appended

**Quality gates before delivery:**

1. Can a non-lawyer procurement professional understand the executive summary?
2. Can the counterparty's counsel understand and respond to each redline?
3. Is every legal claim backed by a specific citation (or flagged [VERIFY])?
4. Are any phrases vague, hedging, or ambiguous? If yes, fix.
5. Could any sentence be shorter without losing meaning? If yes, shorten.
6. Are all Incoterms spelled correctly and consistently (Incoterms® 2020, with edition year)?
7. Are ESG statute names accurate (CSDDD, UFLPA, Åpenhetsloven — not paraphrased)?
8. Are EU PLD references accurate (Directive 2024/2853 vs. old 85/374/EEC)?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 4, search for UCC Article 2 text, UK SGA sections, and CISG provisions
- Search for applicable ESG statutes: CSDDD, UK Modern Slavery Act, UFLPA, France Vigilance Law
- Search for EU Product Liability Directive 2024/2853 national implementing legislation (post-Dec 2026)
- Search for implied warranty disclaimer case law in the governing jurisdiction
- Search for force majeure/commercial impracticability post-COVID and post-tariff precedents
- Search for current UFLPA Entity List additions
- Search for critical minerals regulations (EU CRMA, EU Battery Regulation, FEOC rules) if relevant
- Save results to `/tmp/legalcode-supply-review-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Focus analysis on commercial risk assessment and structural issues
- Include a prominent notice that legal citations require independent verification

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Supply Chain Contract Review Summary

**Document**: [contract name/identifier]
**Parties**: [party names and roles]
**Your Side**: [Buyer / Supplier]
**Goods Type**: [description]
**Governing Law**: [jurisdiction]
**Goods Framework**: [UCC / CISG / UK SGA / other]
**Incoterm**: [term, named place, and version, or "Not specified"]
**ESG Flags**: [CSDDD / UK MSA / UFLPA / France Vigilance / Norway Åpenhetsloven / None]
**EU PLD**: [Directive 2024/2853 applicable / 85/374/EEC (pre-transposition) / Not applicable]
**Tariff Exposure**: [High / Medium / Low / None — with basis]
**Critical Minerals**: [Yes — [list] / No]
**Deadline**: [if provided]
**Review Basis**: [Playbook name / General Commercial Standards]
**Date of Review**: [date]

---

## Key Findings

[Top 3-5 issues with severity flags (RED/YELLOW) and one-line summaries]

---

## Missing Clauses

[List absent clause categories with severity assessment]

---

## ESG/Sustainability Screen Results

[Summary of ESG screening: applicable statutes, gaps identified, severity]

---

## Tariff Risk Screen Results

[Applicable tariff regimes, importer-of-record allocation, tariff hardship clause status]

---

## Incoterms Analysis

[Delivery term: correctness, version, risk allocation, insurance alignment, issues]

---

## EU Product Liability Analysis

[Directive 2024/2853 applicability, authorized representative status, supply chain tier
allocation, software/AI obligations, evidence retention requirements]

---

## Clause-by-Clause Analysis

### [Clause Category] — [GREEN / YELLOW / RED] | Confidence: [level]

**Contract says**: [summary]
**Standard position**: [playbook or market standard]
**Deviation**: [description]
**Legal basis**: [cite statute or principle]
**Business impact**: [practical consequence]
**Redline** (if YELLOW or RED):

> [Specific proposed language]

[Repeat for each of 18 clause categories]

---

## Negotiation Strategy

**Tier 1 (Must-Haves)**: [list]
**Tier 2 (Should-Haves)**: [list]
**Tier 3 (Concession Candidates)**: [list]

**Recommended approach**: [sequencing, tone, strategic trades]

---

## Stakeholder Impact Map

[Table per Multi-Stakeholder Mapping section]

---

## Next Steps

[Specific actions with owners and deadlines if applicable]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

This skill is jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers. When
localizing for specific jurisdictions:

**United States (UCC Article 2):**

- Louisiana has significant UCC Article 2 variations rooted in civil law tradition [VERIFY]
- California, New York, and Delaware have developed specific UCC case law — verify
  local interpretations for implied warranty disclaimers, perfect tender rule
  modifications, and commercial impracticability standards [VERIFY]
- Federal Acquisition Regulation (FAR) applies to US government procurement contracts
  and overrides UCC in key areas [VERIFY]
- Section 301 (China tariffs), Section 232 (steel/aluminum), IEEPA (executive order
  tariffs 2025+): verify current tariff schedules before relying on any tariff allocation
  provisions [VERIFY — tariff rates subject to rapid change]

**United Kingdom (Sale of Goods Act 1979):**

- UK GDPR and DPA 2018 apply if personal data is processed under the supply agreement
- The Consumer Rights Act 2015 applies to B2C supply; Sale of Goods Act 1979 applies B2B
- Scotland: different procedural law but same substantive goods law under SGA [VERIFY]
- Post-Brexit: UK Global Tariff (UKGT) differs from EU Common External Tariff (CET);
  verify rules of origin for UKFTA/EUCETA preferential treatment
- English frustration doctrine does not cover hardship — express tariff hardship clause
  is essential for English-law international supply contracts [VERIFY]

**European Union:**

- **EU Product Liability Directive 2024/2853**: In force November 25, 2024; Member State
  transposition deadline December 9, 2026. After transposition, applies to products placed
  on market / put into service. Research national implementing legislation in relevant
  Member States [VERIFY].
- EU Regulation 2022/2065 (Digital Services Act) may apply if digital goods are involved
- REACH (EC 1907/2006): chemical substances in goods; RoHS Directive 2011/65/EU: hazardous
  substances in electrical/electronic equipment — both create supply chain compliance
  obligations [VERIFY]
- EU Battery Regulation (2023/1542): phased application from 2024; due diligence for
  cobalt, lithium, nickel, natural graphite from February 18, 2025 for large producers
  [VERIFY — implementation status]
- CSDDD (Directive 2024/1760): single application date July 26, 2029 (per "Omnibus I"
  Dec 2025); transposition deadline July 26, 2027 [VERIFY — Omnibus I final legislative
  status]

**Germany:**

- LkSG announced for abolition by German coalition government (March 2026) [VERIFY —
  formal repeal legislation status]. Until formally repealed, may still be in effect.
  Until LkSG is repealed, contracts with German suppliers/buyers should still address
  supply chain due diligence obligations as a matter of good commercial practice.
- CSDDD will replace LkSG obligations once in effect.

**France:**

- Devoir de Vigilance (Loi n° 2017-399): applies to large French companies (5,000+ French
  employees or 10,000+ global employees). Active litigation; courts are increasingly
  interpreting obligations broadly. Supply contracts with French-law governed entities
  should include vigilance plan support obligations [VERIFY]

**International (CISG):**

- CISG ratified by 95+ states including US, Germany, France, China, Japan, Australia,
  Canada (most provinces), Italy, Spain — but NOT the UK [VERIFY — UK accession status]
  and NOT Brazil (ratification pending [VERIFY])
- CISG exclusion clause: "The parties exclude the application of the United Nations
  Convention on Contracts for the International Sale of Goods (CISG)"
- Parties in non-contracting states: CISG does not apply by default

**China (key manufacturing jurisdiction):**

- PRC Civil Code Book III (Contract Law, effective January 1, 2021): governs contracts
  for sale of goods in China [VERIFY]
- UFLPA compliance requires supply chain traceability documentation; Chinese suppliers
  may be unwilling to provide documentation exposing supply chain structure
- China export tariffs and licensing on gallium, germanium, graphite, and other critical
  minerals — verify current restrictions before structuring critical minerals supply
  contracts with Chinese suppliers [VERIFY — subject to rapid change]
- China Customs documentation requirements for export [VERIFY]

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis for supply and procurement contract
review using Mode A creation workflow. Research basis: (1) UCC Article 2 key provisions
(§§ 2-201, 2-207, 2-314–2-316, 2-508, 2-509, 2-510, 2-601, 2-602, 2-606, 2-615,
2-711–2-713, 2-719) via Cornell LII and recent case law (Kyocera Corp. v. Hemlock
Semiconductor, 7th Cir.; MSSC Inc. v. Airboss Flexible Products Co., Michigan Supreme
Court 2023); (2) CISG Arts. 6, 25, 34–39, 45–52, 61–65, 66–70, 71–77, 79 via UNCITRAL,
CISG-Online, and CISG Advisory Council Opinions; (3) UK Sale of Goods Act 1979 ss.12–14
and SSGSA 1994 via UK legislation.gov.uk; (4) Incoterms 2020 all 11 terms via ICC,
including FCA Art. A6/B6 on-board B/L arrangement and DPU replacing DAT; (5) EU Product
Liability Directive 2024/2853 (in force November 25, 2024; transposition deadline December
9, 2026) via EUR-Lex and Reed Smith analysis; (6) EU CSDDD Directive 2024/1760 as amended
by Omnibus I (December 2025) — single application date July 26, 2029 — via Fieldfisher,
Wilson Sonsini, and ECOBIOMANAGER; (7) German LkSG abolition announcement March 2026 via
ESGToday and Fieldfisher; (8) France Devoir de Vigilance (Loi 2017-399) case law via
Global Rights Compliance (2025); (9) Norway Åpenhetsloven (effective July 1, 2022) via
Forbrukertilsynet; (10) UK Modern Slavery Act 2015 s.54 reform status via Skadden (2024);
(11) US UFLPA (effective June 22, 2022) via US CBP; (12) EU Conflict Minerals Regulation
2017/821; (13) EU Critical Raw Materials Act (Regulation 2024/1252, in force May 23, 2024)
via EUR-Lex and Reed Smith; (14) EU Battery Regulation 2023/1542 via EU Commission;
(15) Tariff risk allocation and hardship clause analysis via Davis Wright Tremaine (March
2026), Morgan Lewis (July 2025), Foley & Lardner (Feb 2025), K&L Gates (Apr-May 2025),
Torys (Feb 2025), and Quinn Emanuel (2025); (16) CISG Arts. 71–77 anticipatory breach
and damages via CISG-Online, Pace University CISG Database, CISG Advisory Council Opinion
No. 8; (17) Supply chain finance (reverse factoring/SCF) via ICC/GSCFF Standard
Definitions (2021), BAFT Payables Finance Principles, IFRS 7/IAS 7 amendments (January
2024 effective date), Norton Rose Fulbright analysis; (18) Force majeure post-COVID and
tariff-era precedents via Clifford Chance and National Law Review; (19) Supply continuity
and shortage allocation practitioner guidance; (20) MFC/MFN antitrust analysis via ABA
and EU enforcement precedents. Structural patterns adapted from legalcode-contract-review
(reference standard) and legalcode-distribution-agreement-review (supply chain adjacent).
All citations marked [VERIFY] require verification against authoritative sources before
reliance. ~2,100 lines; 12-step workflow; 12 CLARIFY points; 18/18 quality elements
present; 22 anti-patterns; 18 clause categories (16 core + Tariff/Customs + SCF).
