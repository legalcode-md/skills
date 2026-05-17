---
name: legalcode-limitation-of-liability-review
description: >
  Deep analysis of limitation of liability clauses across contract types — review and
  classify liability caps (aggregate, per-incident, per-claim), excluded damages
  (consequential, indirect, special, incidental, punitive), carve-outs and super-caps
  (IP indemnity, confidentiality breach, data breach, willful misconduct, gross
  negligence, death and personal injury), sole-remedy clauses, and fundamental breach
  enforceability. Evaluates cap adequacy relative to deal value and risk profile. Compares
  against market standards for SaaS, professional services, licensing, and procurement
  agreements. Use when reviewing any commercial agreement with limitation of liability
  language, when a counterparty proposes aggressive cap levels or broad exclusions, when
  assessing whether a vendor's LOL clause creates unacceptable risk exposure, or when
  drafting LOL provisions for any contract type. Produces GREEN/YELLOW/RED classification
  with confidence-scored redline suggestions for rebalancing risk allocation, Glass Box
  audit trail, and jurisdiction-aware enforceability analysis. Jurisdiction-agnostic with
  localization markers for US, UK, EU (Germany, France), and Australia.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode Limitation of Liability Review

> **Disclaimer**: This skill provides a framework for AI-assisted review of limitation of
> liability clauses. It does not constitute legal advice. All outputs should be reviewed by
> a qualified legal professional licensed in the relevant jurisdiction before use. Laws
> change; verify current applicability before relying on any provision described here.
> Limitation of liability enforceability is highly jurisdiction-sensitive — mandatory
> statutory floors (UCTA 1977, German BGB §309, French Code Civil Art. 1170) vary
> materially across governing laws. Statutory and case law references cited from memory
> carry hallucination risk — verify against authoritative sources before relying on them.

---

## Purpose and Scope

This skill provides deep, clause-level analysis of limitation of liability provisions in
commercial contracts. It evaluates cap adequacy, exclusion breadth, carve-out structure,
and enforceability — and produces confidence-scored findings with actionable redline
suggestions for rebalancing risk allocation between the parties.

Limitation of liability is consistently ranked as the **most negotiated clause** in
commercial contracts (World Commerce & Contracting Association). It is also the clause
most often rendered ineffective by poor drafting, statutory unenforceability, or
interaction with other provisions (indemnification, SLA sole-remedy, insurance minimums).
This skill addresses all three failure modes.

**Covers:**
- Aggregate liability caps (fixed, fee-multiple, insurance-linked)
- Per-incident and per-claim caps and their implications
- Exclusion of consequential, indirect, special, incidental, and punitive damages
- Carve-outs from caps (IP indemnity, data breach, confidentiality, fraud, willful misconduct, gross negligence, death/personal injury)
- Super-cap structures for elevated-risk categories
- Sole-remedy clauses and their interaction with caps
- Fundamental breach and clause interaction analysis
- Cap adequacy assessment relative to deal value and risk profile
- Enforceability analysis across US, UK, EU (Germany, France), and Australian law
- Dual-perspective analysis: vendor-favorable vs. customer-favorable positions
- Market-standard benchmarks by contract type (SaaS, professional services, licensing, procurement)
- GREEN / YELLOW / RED classification with confidence scoring
- Redline suggestions with fallback positions

**Does not:**
- Draft full limitation of liability clauses from scratch (see `legalcode-contract-review` or relevant drafting skills)
- Perform comprehensive clause-by-clause review of any commercial agreement (see `legalcode-contract-review`)
- Replace qualified counsel — particularly for high-value deals, regulated-sector contracts, or cross-border transactions where enforceability turns on specific local law
- Apply to consumer contracts exclusively — consumer protection rules add mandatory floors not fully covered here

**Related skills:**
- `legalcode-contract-review` — full clause-by-clause review of any commercial agreement
- `legalcode-saas-agreement-drafter` — drafts liability structures for SaaS agreements
- `legalcode-master-services-agreement` — MSA-specific liability cap frameworks
- `legalcode-nda-triage` — NDA triage including confidentiality and remedies analysis
- `legalcode-contract-risk-scorer` — quantified risk scoring of final contract terms
- `legalcode-redline-generator` — standalone redline generation from analyzed positions

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The contract's governing law clause determines
which legal framework applies. The review identifies the governing law early and flags
jurisdiction-specific enforceability issues throughout.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

**United States:**
- UCC §2-719: permits limitation of consequential damages in goods contracts; subject to
  unconscionability; may be voided for gross negligence or willful misconduct
- California Civil Code §1668: limitations on liability for willful injury to person or
  property of another are void (CA Supreme Court confirmed) [VERIFY current application]
- Delaware, New York, Texas: generally enforce commercial LOL clauses with fewer statutory
  restrictions; gross negligence carve-outs increasingly court-imposed [VERIFY per state]
- HIPAA and CCPA: impose mandatory liability obligations that contractual caps cannot
  override for regulated data categories

**United Kingdom:**
- Unfair Contract Terms Act 1977 (UCTA), as amended: reasonableness test applies to
  B2B exclusion and limitation clauses (s.11; Schedule 2 reasonableness factors); death
  and personal injury liability cannot be excluded (s.2(1)); negligence causing other loss
  subject to reasonableness test (s.2(2))
- Consumer Rights Act 2015: in B2C contracts, unfair terms not binding on consumer;
  consumer cannot waive statutory rights
- Photo Production Ltd v Securicor Transport Ltd [1980] UKHL 2: fundamental breach is
  NOT a rule of law; effectiveness of exclusion clauses is a matter of construction
- Fraud / fraudulent misrepresentation: cannot be excluded as matter of public policy
  [VERIFY: HIH Casualty v Chase Manhattan Bank [2003] UKHL 6]
- Hadley v Baxendale (1854): consequential loss = Limb 2 (foreseeable at time of
  contracting); not an absolute exclusion even without clause [VERIFY current treatment]

**Germany (BGB):**
- §309 No. 7(a): in standard terms (AGBs), liability for death or bodily injury cannot
  be limited — VOID
- §309 No. 7(b): in standard terms, limitation of liability for gross negligence
  (grobe Fahrlässigkeit) is VOID
- §307: general fairness test for standard terms; LOL clauses may be struck down if
  they fundamentally impair contractual purpose
- Individually negotiated contracts: more flexibility than standard terms
- "Folgeschäden" (consequential loss): concept used in insurance law; no uniformly
  accepted definition in BGB contract law [VERIFY German doctrine]

**France (Code Civil):**
- Art. 1170 (2016 reform): any clause that empties a material contractual obligation of
  its meaning (substance) shall be "deemed not written" (réputée non écrite)
- Art. 1231-3: only reasonably foreseeable loss recoverable; LOL clauses must not
  conflict with this principle
- Exclusion of liability for dol (fraud) and faute lourde (gross negligence): void as
  matter of public policy
- Personal injury exclusion: categorically prohibited
- B2C: additional consumer protection under Code de la consommation

**Australia:**
- Australian Consumer Law (ACL): unfair contract terms regime (expanded November 2023
  to include small businesses); civil penalties for unfair terms
- Death and personal injury: cannot be excluded in consumer contracts
- GDPR equivalent: Privacy Act 1988 (Cth) with mandatory breach notification
  obligations that cannot be waived by contract

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent, the workflow pauses and asks when:

- The answer changes the direction of analysis (which side to optimize for)
- Contract-type matters for market-standard benchmarking
- Jurisdiction determines which statutory floors apply
- Deal value matters for cap adequacy assessment

Use the structured clarification pattern (options + "why this matters") wherever marked
with **⟁ CLARIFY** below. If the user has already provided the information, skip the
question and proceed — but **state assumptions explicitly** (e.g., "I'm assuming you are
on the customer side — tell me if that's wrong").

---

## Workflow

### Step 1: Accept Input

Accept the limitation of liability provision in any of these formats:

- **Clause extract**: The LOL clause (or clauses) pasted directly — include surrounding
  clauses if available (indemnification, SLA/service credits, insurance requirements)
- **Full contract**: A complete agreement to be analyzed for LOL provisions
- **File or URL**: A document in PDF, DOCX, or linked format
- **Partial text**: Even a single paragraph or sentence triggers analysis; note what
  context is missing and request it

If no provision is provided, prompt the user to supply the LOL clause.

**Also look for:** Sole-remedy clauses (often in SLA sections), "exclusive remedy"
language, mutual waivers of consequential damages, indemnification provisions
(which may create obligations outside the cap), and insurance requirements (which
interact with cap adequacy).

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask these questions. Skip any already
answered by the user:

1. **Which side are you on?**
   - Options: Customer / Buyer, Vendor / Supplier, Licensor, Licensee, Service Provider,
     Client, Neutral / Both, Other
   - *Why this matters*: The entire analysis flips. A cap that is reasonable for a vendor
     may be catastrophically inadequate from the customer's perspective — and vice versa.

2. **What type of contract is this?**
   - Options: SaaS / cloud services, Professional services / MSA, Software license,
     Procurement / supply chain, Employment / services, Distribution / reseller,
     Construction / EPC, Financial services, Other / mixed
   - *Why this matters*: Market standards for cap amounts, carve-outs, and damages
     exclusions vary substantially by contract type. A 12-month cap is standard for SaaS
     but potentially inadequate for high-risk outsourcing.

3. **What is the approximate deal value / annual contract value?**
   - Options: Under $100K / £100K, $100K–$500K / £100K–£500K, $500K–$5M / £500K–£5M,
     Over $5M / £5M, Not sure / not relevant
   - *Why this matters*: Cap adequacy must be assessed relative to deal value and
     realistic exposure. A $5M cap sounds large until you realize it covers a $100M
     outsourcing program.

4. **What is the governing law / jurisdiction?**
   - Options: English/UK law, US (specify state if known), German law, French law,
     Australian law, Other EU member state, Other / not stated, Multiple jurisdictions
   - *Why this matters*: Mandatory statutory floors differ materially. A clause that
     validly excludes death/PI liability under US common law is void under UCTA s.2(1)
     in England.

5. **Do you have the organization's negotiation playbook positions?**
   - Options: Yes, I'll provide them, Use general market standards (no playbook),
     I'll provide key positions as we go
   - *Why this matters*: Playbook positions define what is "acceptable" for GREEN
     classification. Without them, analysis defaults to market standards — which may not
     reflect your risk appetite.

6. **What is your risk tolerance for this deal?**
   - Options: Conservative (prefer to flag any deviation from standard),
     Pragmatic (flag material deviations only; accept commercially reasonable terms),
     Case-by-case (I'll judge each issue as you raise it)
   - *Why this matters*: Affects YELLOW vs. RED threshold — particularly for borderline
     items where reasonable practitioners could differ.

If the user provides partial context, proceed with what you have and **state assumptions
explicitly** at the start of the analysis.

### Step 3: Load Playbook or Market Standards

Check for the organization's LOL playbook positions in local settings (e.g., `legal.local.md`
or `playbook.md`). The playbook should define:

- **Standard cap position**: Preferred cap formula (e.g., 12 months' fees minimum)
- **Carve-out requirements**: Which categories must always be carved out
- **Acceptable ranges**: Terms that can be agreed without escalation
- **Escalation triggers**: When senior counsel sign-off is required

**If no playbook is configured:**

**⟁ CLARIFY** — Inform the user that no playbook was found. Ask:

- **Option A: Provide positions now** — Walk through 6 key LOL positions: cap formula,
  required carve-outs, acceptable damages exclusions, IP indemnity scope, data breach
  super-cap, willful misconduct treatment. Takes 5 minutes upfront; makes the analysis
  precise and playbook-aligned.
- **Option B: Use market standards** — Use the contract-type-specific market standards
  defined in this skill (SaaS, PS, licensing, procurement). Faster; may not reflect your
  risk appetite.
- **Option C: Positions as we go** — Begin analysis; ask for your position when each
  clause element is reached.

Label the analysis clearly: "Based on [organizational playbook / market standards for
[contract type] / user-provided positions]".

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Identify the governing law from the contract's governing law clause or context.

Use **legalcode-mcp** (if connected) to build a working legal reference file:

```
Search targets:
- "limitation of liability [jurisdiction] commercial contracts"
- "consequential damages exclusion [jurisdiction] enforceability"
- "UCTA 1977" (UK) / "BGB §309" (Germany) / "Code Civil Art. 1170" (France) /
  "UCC 2-719" (US) / "ACL unfair terms" (Australia)
- "gross negligence carve-out [jurisdiction]"
- "[jurisdiction] death personal injury liability exclusion"
```

Save results to: `/tmp/legalcode-lol-authority.md`

**Without legalcode-mcp:** Proceed with jurisdiction-agnostic analysis using the
enforceability framework in this skill. Mark all statutory references with [VERIFY].
Note in the Glass Box: `legalcode_mcp: "Not connected"`.

### Step 5: Read the Provision Holistically

Before clause-by-clause analysis, read the entire limitation of liability structure:

1. **Locate all relevant provisions** — LOL is often spread across multiple sections
   (limitation of liability clause, indemnification clause, SLA/service credits, IP
   indemnification, data protection addendum). Identify all of them.

2. **Map the cap architecture** — Does the contract have:
   - A single aggregate cap on all liability?
   - A general cap plus super-caps for specific categories?
   - Per-incident or per-claim caps in addition to or instead of aggregate caps?
   - Excluded categories (uncapped liability)?

3. **Note the mutual / asymmetric structure** — Does the same cap and exclusion structure
   apply to both parties? Or does one party (typically the supplier) receive broader
   protection? Asymmetric structures warrant scrutiny.

4. **Check interaction with related provisions:**
   - SLA / service credits clause: "Sole remedy" language may prevent damage claims
   - Indemnification clause: Indemnities may sit inside or outside the cap
   - Insurance clause: Cap amount relative to insurance requirements
   - Data protection addendum / DPA: GDPR and CCPA impose liability floors

5. **Flag obvious structural issues** before deep analysis:
   - Cap below deal value (immediate RED candidate)
   - No carve-outs for mandatory categories (immediate RED)
   - "Sole remedy" for data breach (immediate RED)
   - Asymmetric structure where one party bears all risk

### Step 6: Deep Liability Structure Analysis

Analyze the LOL provision against each of the following 10 dimensions. For each
dimension, assign PASS / FLAG, note the specific language, apply a confidence score,
and generate a finding.

---

#### Dimension 1: Aggregate Cap Amount and Formula

**What to assess:**

| Contract Type | Vendor-Favorable (Minimum) | Market Range | Customer-Favorable (Maximum) |
|---------------|---------------------------|--------------|-------------------------------|
| SaaS / Cloud | 3–6 months' fees | 12 months' fees | 24 months' fees (or more for data-critical) |
| Professional Services / MSA | 100% of fees paid | 100–200% of total fees paid | 200%+ of fees, or fixed higher amount |
| Software License (perpetual) | License fees paid | 2–5× license fees | Replacement cost of system |
| Outsourcing (BPO/ITO) | 100% of fees paid | 100–300% of annual fees | Higher; may include regulatory exposure |
| Procurement / Supply Chain | Cost of goods supplied | 100–200% of contract value | Replacement cost + downstream losses |
| Distribution / Reseller | Supplier's wholesale value | 2× gross margin | Full downstream exposure |

**Assessment criteria:**
- [ ] Cap is expressed as a formula (fee multiple) rather than an arbitrary fixed number
- [ ] Formula reflects the **actual** economic relationship (e.g., "fees paid or payable in the 12 months preceding the claim")
- [ ] Cap is proportionate to the realistic exposure from a breach or failure
- [ ] Cap aligns with contract-type market standard (see table above)
- [ ] Cap is mutual (both parties subject to the same cap) OR asymmetry is commercially justified

**Adequacy assessment formula** (apply silently, report if material):

```
Cap adequacy ratio = Cap amount ÷ Maximum realistic loss exposure

<0.25: Severely inadequate (RED)
0.25–0.50: Likely inadequate (RED–YELLOW)
0.50–1.0: Potentially inadequate (YELLOW)
1.0–2.0: Market range (GREEN–YELLOW depending on risk profile)
>2.0: Generous to claiming party (GREEN for claimant; may be RED for respondent)
```

[JURISDICTION-SPECIFIC] UK/EU courts may assess whether cap adequacy satisfies UCTA/ACL
reasonableness. A cap that leaves the claimant without meaningful remedy may be struck
down. Flag if cap amount is significantly below market range for the contract type.

---

#### Dimension 2: Per-Incident and Per-Claim Caps

**What to assess:**

- **Aggregate cap only**: One overall limit on all claims combined. Preferred by
  vendors/suppliers (total exposure is capped). For long-term contracts or recurring
  services, aggregate caps can erode quickly after a single incident.

- **Per-incident cap**: Each individual incident or occurrence has its own limit.
  Preferred by customers (each event generates fresh headroom). Often combined with a
  lower aggregate cap.

- **Per-claim cap**: Each individual legal claim has its own limit. Preferred by
  claimants (maximizes available recovery per claim). Contentious — may enable
  multiple claims from a single incident.

**Interaction risks:**
- An aggregate cap of 12 months' fees that resets annually protects the vendor more
  than a static aggregate cap
- "Per occurrence" language creates litigation risk on whether multiple impacts from
  one root cause are one or multiple occurrences (see Stevens & Bolton ambiguity
  cases [VERIFY]) [JURISDICTION-SPECIFIC]
- For subscription/SaaS contracts, confirm whether the cap resets on renewal or is
  cumulative over the contract term

**Assessment criteria:**
- [ ] Cap type (aggregate / per-incident / per-claim) is unambiguous
- [ ] Temporal scope is clear (annual? per contract term? cumulative lifetime?)
- [ ] Reset mechanism (if any) is explicitly stated
- [ ] "Occurrence" is defined if used as the cap trigger
- [ ] Per-incident cap level is reasonable relative to single-incident exposure

---

#### Dimension 3: Exclusion of Consequential and Indirect Damages

**What to assess:**

**Common excluded categories:**

| Category | Definition | Risk if Excluded |
|----------|-----------|-----------------|
| Consequential damages | Losses not directly caused by breach; Hadley v Baxendale Limb 2 [VERIFY] | May eliminate meaningful recovery for downstream impacts |
| Indirect damages | Synonym for consequential in most jurisdictions; Limb 2 losses | Same as consequential |
| Special damages | Losses known to both parties at time of contracting; Hadley Limb 2 [VERIFY] | Covers foreseeable but non-direct losses |
| Incidental damages | Costs incurred in dealing with a breach | Eliminates cost-of-substitute and mitigation costs |
| Punitive / exemplary damages | Court-awarded punishment above actual loss | Rarely available in commercial contracts anyway (UK/EU); more relevant in US |
| Loss of profit / revenue | Operating profit or gross revenue lost due to breach | Critical carve-out for customers whose revenue depends on the service |
| Loss of data | Cost of reconstruction and downstream loss from data loss | Critical for cloud/SaaS; must NOT be covered by standard consequential exclusion [VERIFY jurisdiction] |
| Loss of goodwill | Brand/reputational damage from breach | Difficult to quantify; exclusion typically acceptable |
| Loss of opportunity | Commercial opportunities foregone due to breach | Difficult to quantify; exclusion often acceptable |
| Wasted expenditure | Costs incurred in reliance on the contract | Customer-side concern; exclusion may be problematic for critical IT contracts |

**Enforceability by jurisdiction (summary):**

| Jurisdiction | General Enforceability | Mandatory Carve-Outs | Notes |
|-------------|----------------------|---------------------|-------|
| **England/Wales** | Generally valid in B2B (UCTA reasonableness test) | Death/PI (UCTA s.2(1)), fraud | "Consequential" ≠ "indirect" in all clauses — depends on contract language [VERIFY] |
| **US (general)** | Generally valid in B2B (UCC §2-719 for goods) | Willful misconduct (CA Cal Civ §1668), gross negligence (varies by state) | Unconscionability doctrine applies; "essential purpose" failure may void clause [VERIFY per state] |
| **Germany** | Limited in standard terms (AGBs) | Death/PI (§309 No. 7(a)), gross negligence (§309 No. 7(b)) | Individually negotiated contracts have more flexibility |
| **France** | Valid if not emptying essential obligation (Art. 1170) | Dol (fraud), faute lourde (gross negligence), personal injury | Direct/indirect distinction used differently than UK/US [VERIFY] |
| **Australia** | ACL unfair terms regime (Nov 2023 expansion) | Death/PI (consumer contracts) | Civil penalties for unfair terms in small business contracts |

**Assessment criteria:**
- [ ] Exclusion categories are specifically named (not just "indirect and consequential")
- [ ] **Data loss** is NOT swept into the consequential damages exclusion without a specific carve-out or super-cap
- [ ] **Loss of profits** exclusion does not eliminate the customer's entire meaningful recovery
- [ ] Exclusion does not conflict with mandatory statutory protections for governing law
- [ ] Exclusion is mutual (both parties excluded equally) — or asymmetry is justified
- [ ] "Sole remedy" language does not appear in a separate section without coordination here

[JURISDICTION-SPECIFIC] In the UK, "indirect and consequential loss" has been interpreted
by courts more narrowly than the full scope of Hadley Limb 2. An exclusion of "indirect
and consequential" may not exclude all Limb 2 losses. Legal advice required for specific
application. [VERIFY: Saint Line Ltd v Richardsons Westgarth & Co Ltd (1940) and
subsequent UK cases].

---

#### Dimension 4: Carve-Outs from the Cap (Standard and Mandatory)

**Required carve-outs by jurisdiction:**

| Carve-Out | US | UK | Germany | France | Australia |
|----------|----|----|---------|--------|-----------|
| Death / personal injury | Recommended | **MANDATORY** (UCTA s.2(1)) | **MANDATORY** (§309 No. 7(a)) | **MANDATORY** | Consumer: mandatory |
| Fraud / fraudulent misrepresentation | Public policy void | **MANDATORY** (public policy) | Void | **MANDATORY** (dol) | Void |
| Gross negligence | State-dependent | Market standard | **MANDATORY** in standard terms (§309 No. 7(b)) | **MANDATORY** (faute lourde) | Market standard |
| Willful misconduct / intentional acts | CA Civil Code §1668 void | Market standard (UCTA s.2(2)) | Mandatory (§276 BGB intentional act) | Mandatory (dol) | Market standard |

**Market-standard carve-outs (expected in any well-drafted commercial contract):**

| Carve-Out | Market Status | Typical Treatment |
|----------|--------------|-------------------|
| IP indemnification (third-party IP claims) | Market standard | Historically uncapped; increasingly capped at 2–5× contract value (super-cap) |
| Data breach / privacy violation | Market standard (emerging) | Carve-out from standard cap; super-cap at 2–3× standard cap; or uncapped for GDPR-covered breaches |
| Confidentiality breach | Market standard | Carve-out from standard cap; often uncapped or super-capped |
| Willful misconduct | Market standard | Uncapped |
| Gross negligence | Market standard | Uncapped (mandatory in some jurisdictions) |
| Fraud | Market standard | Always uncapped |
| Death / personal injury | Market standard | Always uncapped (mandatory in UK/EU) |
| Payment obligations (fees already owed) | Market standard | Uncapped (otherwise vendor could cap its own breach of contract to pay) |

**Super-cap structures:**

A **super-cap** is a higher cap applied to specific high-risk categories. It bridges the
gap between the standard cap (vendor-favorable) and fully uncapped liability
(customer-favorable) for carve-out categories.

| Category | Standard Super-Cap Range | Notes |
|----------|-------------------------|-------|
| IP indemnification | 2–5× annual contract value | Driven by third-party IP claim costs |
| Data breach | 2–3× standard cap; sometimes tied to data protection regulatory fines (e.g., 4% of global turnover for GDPR [VERIFY Art. 83]) | GDPR fines can far exceed standard caps |
| Confidentiality breach | 2–3× standard cap; sometimes uncapped | Damage may be irreversible |
| Regulatory fines | Often separate; links to governing regulation maximum | Cannot contractually limit regulator; can allocate between parties |

**Assessment criteria:**
- [ ] Death / personal injury: carved out (mandatory in UK/EU; market standard elsewhere)
- [ ] Fraud / fraudulent misrepresentation: carved out (mandatory in all reviewed jurisdictions)
- [ ] Willful misconduct: carved out (mandatory or market standard in all reviewed jurisdictions)
- [ ] Gross negligence: carved out or not excluded (mandatory in Germany/France; market standard in UK/US)
- [ ] IP indemnification: carved out from standard cap (with or without super-cap)
- [ ] Data breach: carved out from standard cap with super-cap or uncapped treatment
- [ ] Confidentiality breach: carved out from standard cap (with appropriate super-cap or uncapped)
- [ ] Payment obligations: not subject to limitation
- [ ] Super-cap amounts are reasonable relative to exposure (not token amounts that recreate the same problem)

---

#### Dimension 5: IP Indemnification Carve-Out Scope

**What to assess:**

IP indemnification is one of the most commercially important carve-outs. It typically
covers the vendor's obligation to defend and indemnify the customer for third-party
claims that use of the vendor's product/service infringes a third party's IP rights.

**Key variables:**
- Is the IP indemnity carved out from the general cap? (Should be YES)
- Is there a sub-limit on the IP indemnity (super-cap)? What amount?
- Does the IP indemnity cover: defense costs + damages + settlements?
- Is the indemnity triggered by "any IP claim" or only "finally adjudicated" infringement?
  (Vendor-favorable: "finally adjudicated"; customer-favorable: includes costs of unresolved claims)
- Does the indemnity cover customer's modifications to the product? (Typically excluded)
- Does the indemnity cover third-party open-source components? (Often excluded)
- Is it mutual? (Customer should also indemnify vendor for customer-provided content)

**Assessment criteria:**
- [ ] IP indemnity is present (missing = RED; vendor takes no ownership risk for own product)
- [ ] IP indemnity is carved out from general cap
- [ ] Scope covers defense costs, not just damages (defense is often the largest cost)
- [ ] Carve-outs within the IP indemnity are reasonable (modifications OK; entire product exclusion is not)
- [ ] Super-cap amount (if present) is proportionate to potential IP exposure
- [ ] Trigger standard is clear (not dependent on ambiguous "finally adjudicated" to delay coverage)

---

#### Dimension 6: Data Breach and Privacy Carve-Out Scope

**What to assess:**

Data breach liability is a growing battleground in technology contracts. GDPR, CCPA, and
similar privacy regulations impose fines that can exceed standard liability caps. Contracts
need dedicated treatment for data breach liability.

**Key issues:**

- **Data breach inside or outside the cap?** Customers increasingly demand carve-outs
  given potential for six-figure (or larger) breach costs. Vendors increasingly counter
  with super-caps rather than fully uncapped.
- **Super-cap sizing**: Market emerging at 2–3× standard cap for data breach; some
  contracts link to 4% of global annual turnover (GDPR Art. 83 maximum) [VERIFY]
- **"Sole remedy" problem**: If the SLA provides service credits as "sole remedy," does
  that sweep in data breach remedies? It should not — flag as RED if ambiguous.
- **Privacy violation vs. data breach**: Some contracts narrowly define "data breach"
  and exclude broader privacy violations (e.g., unauthorized processing, GDPR Art. 5
  violations without a "breach") from the carve-out
- **Regulatory fines allocation**: Between processor and controller for GDPR purposes
  [JURISDICTION-SPECIFIC]

**Assessment criteria:**
- [ ] Data breach explicitly carved out from standard cap (not swept in by consequential damages exclusion)
- [ ] Super-cap or uncapped treatment clearly stated
- [ ] Super-cap amount is commercially reasonable relative to potential breach costs
- [ ] "Sole remedy" language (if present) explicitly excludes data breach claims
- [ ] Privacy regulation compliance obligations are not waived by LOL clause
- [ ] Clause addresses allocation of regulatory fines (if applicable)

[JURISDICTION-SPECIFIC] GDPR Art. 82 creates a right to compensation for data subjects;
contractual LOL clauses between controller and processor cannot waive or reduce this
right [VERIFY]. Under UK GDPR, equivalent provisions apply. [VERIFY current UK treatment
post-Brexit].

---

#### Dimension 7: Sole-Remedy Clauses and SLA Interaction

**What to assess:**

"Sole and exclusive remedy" language appears most commonly in SLA and service credit
provisions. It limits the claiming party to service credits only and purports to bar
any other damages claim — effectively creating a de facto liability cap at the service
credit ceiling.

**Key risks:**
- SLA credits are typically 10–30% of monthly fees per downtime incident
  (far below actual business impact)
- "Sole remedy" for service outages — not a problem if outages are minor
- "Sole remedy" for data loss — major problem if data cannot be recovered
- "Sole remedy" for data breach — potential statutory violation in some jurisdictions

**Assessment criteria:**
- [ ] Sole-remedy language, if present, applies only to service-level breaches (uptime, response time), NOT to data loss or data breach
- [ ] Sole-remedy clause does not conflict with mandatory statutory remedies
- [ ] Service credit amounts are reasonable relative to the business impact of downtime
- [ ] Sole-remedy clause does not prevent claims for damages caused by negligence or willful misconduct

---

#### Dimension 8: Mutual vs. Asymmetric Structure

**What to assess:**

A symmetric LOL clause applies identically to both parties. An asymmetric clause protects
one party (typically the vendor) more than the other.

**Asymmetric patterns to flag:**
- Vendor's liability is capped; customer's liability is uncapped (RED)
- Same cap amount but vendor has broader exclusions (YELLOW–RED)
- Vendor has death/PI carve-out but customer does not (RED — mandatory in some jurisdictions)
- Vendor's IP indemnity is carved out; customer's IP obligations (to provide vendor with
  necessary licenses) are capped (YELLOW)
- One party can receive punitive/exemplary damages; the other cannot (jurisdiction-dependent)

**Assessment criteria:**
- [ ] Cap structure is mutual (identical formula applies to both parties) OR
- [ ] Asymmetry is commercially justified (e.g., vendor caps liability for service delivery; customer
  caps liability for use of licensed software) AND
- [ ] Asymmetry is disclosed and transparent, not buried in defined terms
- [ ] Mandatory carve-outs (death/PI, fraud) apply equally to both parties

---

#### Dimension 9: Enforceability and Statutory Floor Analysis

**What to assess:**

Even a perfectly drafted LOL clause may be unenforceable under the governing law. This
dimension identifies enforceability risks and flags provisions that may be void.

**Enforceability analysis matrix:**

| Issue | England/Wales | US | Germany | France |
|-------|--------------|-----|---------|--------|
| Death/PI excluded | **VOID** (UCTA s.2(1)) | Rarely enforceable | **VOID** (BGB §309 No. 7(a)) | **VOID** |
| Gross negligence excluded (standard terms) | Risk of unreasonableness (UCTA s.2(2)) | State-dependent | **VOID** in AGBs (§309 No. 7(b)) | **VOID** (faute lourde) |
| Fraud / willful act excluded | **VOID** (public policy) | **VOID** (public policy) | **VOID** (§276 BGB) | **VOID** (dol) |
| LOL empties essential obligation | UCTA unreasonable | Unconscionable | **VOID** (§307 BGB) | **VOID** (Art. 1170 Code Civil) |
| Consumer LOL | Consumer Rights Act 2015 | State UDAP laws | §310 BGB | Code de la consommation |
| Very low cap (e.g., token amount) | UCTA reasonableness | Unconscionability | §307 BGB | Art. 1170 Code Civil |

**Assessment criteria:**
- [ ] No provision purports to exclude death/PI liability where governing law prohibits it
- [ ] No provision purports to exclude gross negligence in a jurisdiction where it is mandatory
- [ ] No provision purports to exclude fraud liability
- [ ] Cap amount does not reduce the counterparty to meaningless recovery (LOL doesn't "deprive clause of substance")
- [ ] Standard-terms analysis is applied where relevant (Germany/France; and potentially UK for click-through contracts)
- [ ] Mutual waiver of consequential damages does not conflict with mandatory statutory remedies (e.g., GDPR Art. 82)

---

#### Dimension 10: Interaction with Indemnification Obligations

**What to assess:**

Indemnification and limitation of liability are closely linked but often drafted
independently, creating gaps and conflicts.

**Key interactions:**
- Is the indemnification obligation subject to the general cap? (Common: vendor prefers
  NO; customer prefers YES for any indemnity they must pay)
- Does the IP indemnity sit outside the cap? (Should be YES for vendor-given IP indemnity)
- Does the data breach indemnity sit outside the cap? (Should be YES for vendor-given
  data breach indemnity; with or without super-cap)
- Is there an indemnity for regulatory fines? Who pays? Is it capped?
- Does the indemnification clause create uncapped obligations that the LOL clause
  purports to limit? (Conflict — must be harmonized)

**Assessment criteria:**
- [ ] LOL clause explicitly states whether indemnification obligations are inside or outside the cap
- [ ] IP indemnification is stated to be outside the general cap (or subject to a super-cap)
- [ ] Data breach indemnification is stated to be outside the general cap (or subject to a super-cap)
- [ ] No conflicting provisions between indemnification clause and LOL clause
- [ ] Mutual indemnification obligations are subject to consistent cap treatment

---

### Step 7: Classify

After completing all 10 dimensions, assign an overall classification:

#### GREEN — Acceptable

**All** of the following must be true:

- [ ] Cap amount is within market range for the contract type (see Dimension 1 table)
- [ ] Cap is mutual OR asymmetry is commercially justified and transparent
- [ ] Death / personal injury: carved out (or not applicable)
- [ ] Fraud: carved out
- [ ] Willful misconduct: carved out
- [ ] Gross negligence: carved out (or jurisdiction does not require it and neither does playbook)
- [ ] IP indemnification: carved out from general cap
- [ ] Data breach: carved out from general cap (with reasonable super-cap or uncapped)
- [ ] Confidentiality breach: carved out from general cap
- [ ] Sole-remedy language (if present) does not cover data breach or gross negligence
- [ ] No mandatory statutory provision is violated under governing law
- [ ] Consequential damages exclusion does not eliminate all meaningful recovery

**Confidence required**: HIGH (0.80+)

**Routing**: Accept with awareness; no escalation required. Note items to monitor.

#### YELLOW — Negotiate

**One or more** of the following are present, but the LOL structure is not fundamentally unacceptable:

- Cap is below market range but not egregiously so (e.g., 9 months instead of 12 months
  for SaaS)
- Missing one standard carve-out that could be added without difficulty
- Consequential damages exclusion without data loss carve-out (negotiate to add)
- Asymmetric structure with commercial justification but unfavorable to your position
- Sole-remedy language in SLA with ambiguous scope relative to data breach claims
- Jurisdiction-specific enforceability concern that legal advice would resolve
- Super-cap for IP/data breach is present but at token amount
- One party's indemnity obligations are not clearly outside the general cap

**Confidence required**: PROBABLE (0.60+). If confidence below 0.60, escalate to YELLOW
regardless.

**Routing**: Flag specific issues for counsel. Negotiate with proposed redlines and fallback
positions. Target resolution in 1–2 negotiation rounds.

#### RED — Escalate

**One or more** of the following are present:

- Cap below 3 months' fees for SaaS (critically low) or no cap at all (unlimited vendor
  exposure) — or conversely, cap covers only 1 month's fees for high-risk outsourcing
- **No carve-out for fraud** (VOID in most jurisdictions as matter of public policy)
- **No carve-out for willful misconduct** (VOID in California [VERIFY]; against market
  standard everywhere)
- **Death / personal injury liability excluded in UK/EU contract** (VOID under UCTA s.2(1),
  BGB §309 No. 7(a))
- **Gross negligence excluded in German or French law contract** (VOID under BGB §309
  No. 7(b) / French public policy)
- **Sole remedy for data breach is SLA credit** with no ability to claim actual damages
- **No IP indemnification carve-out** — vendor takes no ownership responsibility for own
  product's IP risk
- **Consequential damages exclusion with no data loss carve-out** in a data-processing
  contract (makes full recovery impossible for the most foreseeable loss)
- **LOL clause voids the contract's essential purpose** under governing law (Art. 1170
  France; §307 Germany; UCTA s.11 UK; unconscionability US)
- **Blatantly asymmetric**: one party's liability capped; other party uncapped (without
  commercial justification)
- **Regulatory liability waived by contract** (GDPR Art. 82; CCPA minimum rights)

**Confidence required**: HIGH (0.80+). If confidence below 0.80, classify as YELLOW and
flag for counsel review. Never escalate speculatively.

**Routing**: Do not execute without legal review. Full counsel assessment required.
Significant negotiation or redraft necessary.

---

### Step 8: Generate Redlines

For each YELLOW and RED finding, generate a redline with fallback position:

**Format for each redline:**

```
Dimension: [Dimension number and name]
Classification: YELLOW / RED
Finding: [What the clause currently says and why it is problematic]
Legal Basis: [Specific statute, case, or market standard — VERIFIED or UNVERIFIED]
Business Impact: [What this means in practical, commercial terms]
Confidence: [Definite / High / Probable / Possible / Unlikely]

Proposed language: [Specific redline — add / delete / replace]
Fallback position: [Compromise language if proposed language is rejected]
Negotiation note: [Why this matters and how to frame the ask to the counterparty]
```

**Standard Redline Library:**

**Cap Amount — Below Market (SaaS):**
```
Proposed: "IN NO EVENT SHALL EITHER PARTY'S AGGREGATE LIABILITY
ARISING OUT OF OR RELATED TO THIS AGREEMENT EXCEED THE AMOUNT
PAID OR PAYABLE BY CUSTOMER TO VENDOR IN THE 12 MONTHS IMMEDIATELY
PRECEDING THE EVENT GIVING RISE TO THE CLAIM."

Fallback: "...12 months..." → "...6 months..." (minimum acceptable for
standard SaaS operations without high data-processing risk)
```

**Data Breach Super-Cap (add where missing):**
```
Proposed: "Notwithstanding the foregoing, the aggregate liability of
[Vendor] arising out of or related to a Data Breach (as defined in
the Data Processing Addendum) shall not exceed [2× / 3×] the amount
paid or payable by Customer in the 12 months preceding the event."

Fallback: Super-cap at 1.5× standard cap (minimum meaningful elevation)
```

**Missing Carve-Outs — Add:**
```
Proposed: "The limitations in this Section shall not apply to:
(a) either party's indemnification obligations under Section [X];
(b) breaches of either party's confidentiality obligations;
(c) claims arising from a party's fraud, gross negligence, or willful
    misconduct;
(d) death or bodily injury caused by a party's negligence;
(e) either party's IP indemnification obligations under Section [Y];
(f) a party's obligations to pay amounts due under this Agreement."
```

**Sole Remedy — Limit Scope:**
```
Proposed: "The remedies set forth in Section [X] are [Vendor's] sole
and exclusive liability, and Customer's sole and exclusive remedy,
for [Vendor's] failure to meet the Service Levels set forth in
Exhibit [Z]. The foregoing shall not limit Customer's right to seek
damages arising from (i) any Data Breach, (ii) [Vendor's] fraud,
gross negligence, or willful misconduct, or (iii) any breach of the
confidentiality obligations under this Agreement."
```

**Asymmetric Cap — Restore Mutuality:**
```
Proposed: "The limitations set forth in this Section [X] apply
equally to both parties and to all causes of action in the aggregate."
```

---

### Step 9: Prioritize Findings

Assign each finding a negotiation tier:

**Tier 1 — Non-Negotiable (hold the line):**
- Statutory violations (death/PI, fraud, gross negligence in mandatory jurisdictions)
- Complete absence of IP indemnity carve-out
- Sole remedy for data breach
- Cap below critical floor for contract type and risk level

**Tier 2 — Material (strong preference; trade for equivalent):**
- Cap below market range by >25%
- Missing data breach super-cap
- Missing confidentiality carve-out
- Sole-remedy ambiguity relative to data breach
- Asymmetric cap without commercial justification

**Tier 3 — Preferred (can concede with appropriate trade):**
- Cap below preferred range but above market floor
- Super-cap at token level (prefer higher but not blocking)
- Missing wasted-expenditure carveout
- Ambiguous "occurrence" definition

---

### Step 10: Deliver Analysis with Glass Box Audit Trail

Present the output in the format specified in the Output Format Template below. Include
the Glass Box YAML block at the end of every analysis.

---

## Citation Quality Gates

Run these 5 gates **silently** before delivering any output. If any gate fails, revise
before delivering.

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every legal claim cites a specific statute, regulation, or established case | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format** | All citations follow a consistent, recognizable format for the jurisdiction | Fix format |
| **Currency** | Every cited provision checked for amendments or repeal | Flag "[CHECK CURRENCY — may have been amended]" |
| **Domain** | Analysis stays within the contract's governing law; no jurisdictional bleed | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated, not hidden | Add confidence qualifier |

---

## Self-Interrogation for RED Items

For any item classified as RED, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the
cited authority? Would a court or tribunal in the governing jurisdiction actually reach
this conclusion on these facts? What is the strongest counter-argument the counterparty's
counsel will make?

**Pass 2 — Completeness**: Have all relevant statutes, regulations, and principles been
considered? Are there regulatory dimensions not yet addressed? Could the clause interact
with another provision to mitigate or worsen the risk?

**Pass 3 — Challenge**: What is the strongest argument that this clause IS acceptable?
Under what circumstances might a reasonable commercial practitioner accept this risk?
Is RED classification proportionate, or is this actually YELLOW with redlines? Would a
solicitor at a leading firm send this back, or mark it up and proceed?

If any pass reveals a weakness in the analysis, revise before delivery. Mark the audit
trail with `self_interrogation: PASS` or `self_interrogation: REVISED`.

---

## Confidence Scoring

For the overall classification and each material finding, assign a confidence level:

| Level | Range | Meaning | Action |
|-------|-------|---------|--------|
| **Definite** | 0.95–1.0 | Settled law, clear contractual provision, no ambiguity | State with confidence |
| **High** | 0.80–0.94 | Strong basis, minor interpretation questions | State with brief caveat |
| **Probable** | 0.60–0.79 | Good arguments but reasonable minds could differ | State with reasoning and contra-indicators |
| **Possible** | 0.40–0.59 | Genuinely uncertain, competing interpretations | Flag for counsel review with both sides |
| **Unlikely** | 0.0–0.39 | Weak basis, speculative | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

**Critical rule**: If overall confidence is below 0.60, escalate to counsel review
regardless of GREEN/YELLOW classification. Never GREEN-classify with sub-0.60 confidence.

---

## Glass Box Audit Trail

Every output MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-limitation-of-liability-review"
  contract_title: "[Contract title or 'Untitled']"
  contract_type: "[SaaS / Professional Services / License / Procurement / Other]"
  user_side: "[Customer / Vendor / Licensor / Licensee / Neutral]"
  governing_law: "[Jurisdiction identified from the contract or 'Not stated']"
  playbook_used: "[Playbook name / 'Market standards' / 'User-provided positions']"
  cap_amount: "[Stated cap formula or fixed amount]"
  cap_type: "[Aggregate / Per-incident / Per-claim / Hybrid]"
  review_date: "[Date of review]"
  dimensions_assessed: 10
  dimension_summary:
    aggregate_cap: "PASS / FLAG — [brief note]"
    per_incident_cap: "PASS / FLAG — [brief note]"
    consequential_exclusions: "PASS / FLAG — [brief note]"
    carve_outs: "PASS / FLAG — [missing: data breach, gross negligence]"
    ip_indemnity: "PASS / FLAG — [brief note]"
    data_breach: "PASS / FLAG — [brief note]"
    sole_remedy: "PASS / FLAG — [brief note]"
    mutual_structure: "PASS / FLAG — [asymmetric: vendor-only cap]"
    enforceability: "PASS / FLAG — [jurisdiction-specific issue]"
    indemnification_interaction: "PASS / FLAG — [brief note]"
  overall_classification: "GREEN / YELLOW / RED"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "[UCTA 1977 s.2(1) — VERIFIED / UNVERIFIED]"
    - "[BGB §309 No. 7(b) — VERIFIED / UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  tier_1_issues: "[count]"
  tier_2_issues: "[count]"
  tier_3_issues: "[count]"
  limitations:
    - "[Scope limitations, missing provisions, assumptions]"
  reviewer: "AI-assisted — requires qualified legal review"
```

---

## Anti-Patterns

What NOT to do when reviewing limitation of liability clauses:

1. **Treating all damages exclusions as equivalent** — An exclusion of "indirect and
   consequential loss" does not automatically exclude loss of data, loss of profits, or
   wasted expenditure. These may be direct losses in some fact patterns. Read the clause
   against the specific breach scenario, not abstractly.

2. **Ignoring the interaction between cap, SLA credits, and indemnification** — A "sole
   remedy" clause in the SLA section can silently decimate the benefit of a well-drafted
   LOL provision. Always read all three provisions together. Failing to do so is the most
   common reason LOL clauses fail in practice.

3. **Assuming enforceability without checking the governing law** — A clause that
   validly excludes gross negligence under English law may be VOID in a German-law
   contract. Never assume enforceability. Run the statutory floor analysis (Dimension 9)
   for every review.

4. **Treating "fundamental breach" as a live doctrine** — In England, Photo Production
   v Securicor [1980] UKHL 2 settled that fundamental breach is NOT a rule of law.
   Clause effectiveness is a matter of construction. Do not advise that a limitation
   clause will automatically be unenforceable because of a "fundamental breach." Apply
   UCTA reasonableness instead.

5. **Conflating "consequential" with "indirect"** — These are sometimes treated as
   synonyms, sometimes as distinct categories. Under Hadley v Baxendale, both Limbs 1
   and 2 may be recoverable absent an exclusion clause. Whether an exclusion covers "all"
   consequential loss depends on the specific language and jurisdiction.

6. **Missing the data loss problem in consequential damages exclusions** — Loss of data
   in a cloud/SaaS context may be characterized as direct (because the very service being
   contracted is data storage/processing) or consequential (in a broader commercial
   context). If the contract processes critical data and has no data loss carve-out, flag
   it regardless of the theoretical argument — this is where enforcement risk is highest.

7. **Accepting IP indemnity caps at face value without assessing exposure** — A super-cap
   at 1× annual contract value for an IP indemnity may be inadequate if the vendor's
   product is central to the customer's business and IP exposure is real. Assess whether
   the super-cap amount reflects realistic IP litigation exposure, not just a number that
   exceeds the standard cap.

8. **Reviewing from only one side's perspective without considering the counterparty's
   position** — A vendor's counsel will push back on every carve-out request. Understand
   which carve-outs are truly non-negotiable (statutory floors) vs. market standard
   (negotiable with justification) vs. aspirational (likely conceded). Overshooting all
   carve-outs in a single negotiation round risks losing credibility.

9. **Assuming "mutual" means "fair"** — A mutual cap at 1 month's fees is equally
   inadequate for both parties. Mutuality is necessary but not sufficient for fairness.
   Assess cap adequacy independently of symmetry.

10. **Ignoring GDPR and data protection regulatory floors** — GDPR Art. 82 creates a
    right of compensation for data subjects that cannot be waived or limited by contract.
    A LOL clause between controller and processor does not affect data subject rights. But
    it does affect who pays — and allocation provisions between commercial parties must be
    assessed separately. [VERIFY current UK GDPR treatment post-Brexit].

11. **Treating token super-caps as meaningful carve-outs** — A "super-cap" for data
    breach set at 1.01× the standard cap is not a meaningful protection. Assess whether
    the super-cap amount reflects realistic exposure, not just the appearance of a carve-out.

12. **Failing to identify "deemed acceptance" risks** — Some contracts deem acceptance of
    services (or failure to reject within a period) as a waiver of liability claims. These
    provisions interact with the LOL clause. Always check for deemed-acceptance language.

13. **Not verifying whether the cap resets** — An aggregate cap that resets annually is
    materially more favorable to the capped party than a cumulative lifetime cap. An
    aggregate cap that does not reset for a 5-year contract may be far more limiting than
    the stated amount implies. Always check the temporal scope.

14. **Recommending "uncapped" carve-outs without sizing the exposure** — Recommending
    uncapped IP indemnity or uncapped data breach liability without flagging the commercial
    implications for the capped party (usually the vendor) is not balanced legal advice.
    Recommend super-caps with reasonable amounts as the default.

15. **Overlooking the penalty / liquidated damages interaction** — Some LOL clauses
    expressly carve out "liquidated damages" obligations. Check whether liquidated
    damages provisions appear elsewhere in the contract and whether they are subject to
    the cap or carved out.

16. **Citing jurisdiction-specific doctrine without verifying application** — "Fundamental
    breach" is rejected in England but may be applied differently in other common law
    jurisdictions (Canada has had a more complex history). Do not universalize jurisdiction-
    specific doctrines.

17. **Ignoring insurance requirements as a cap adequacy check** — A cap at 2× annual
    fees means nothing if the party's professional indemnity insurance covers $10M. And
    a cap that exceeds available insurance coverage imposes uninsurable risk. Always
    cross-check against the insurance clause where present.

18. **Presenting all carve-outs in a single list without prioritization** — Not all
    carve-outs have equal urgency. Death/PI and fraud carve-outs are non-negotiable in
    most jurisdictions. Data breach carve-outs are Tier 1 or Tier 2 depending on the
    contract. Goodwill exclusions are Tier 3 at best. Present findings in priority order.

19. **Assuming the governing law clause reflects the actual governing law** — In cross-
    border contracts, there may be mandatory rules of one party's home jurisdiction that
    apply regardless of the chosen governing law (e.g., GDPR applies to EU data subjects
    regardless of chosen law; Australian ACL may apply to Australian consumers). Flag
    jurisdictional overlay risks.

20. **Drafting without considering the full risk allocation ecosystem** — The LOL clause
    is one part of a risk allocation system that includes indemnification, insurance,
    warranties, representations, force majeure, and termination. A legally correct LOL
    clause can still create an irrational overall risk allocation when considered with
    the rest of the contract. Always close the analysis with a holistic assessment.

---

## Writing Standards

### For Redline Rationales (shared with counterparty)

- **Plain language.** No legal jargon without explanation. "This clause excludes your
  right to recover the cost of data recovery" — not "this provision bars recovery of
  mitigation costs incurred pursuant to a service failure event."
- **Active voice.** "The vendor must indemnify" — not "indemnification obligations shall
  be assumed by the vendor."
- **Name the actor.** "Vendor's aggregate liability..." — not "aggregate liability of
  either party..."
- **Short sentences.** One idea per sentence.
- **Specific, not vague.** Reference the clause number and the specific language that is
  problematic; do not reference the "general structure."

### For Internal Analysis

- Same plain-language standards; may include more legal detail
- Confidence qualifiers wherever appropriate
- [VERIFY] and [UNVERIFIED] markers on all statutory/case law references not confirmed
  against an authoritative source
- Glass Box audit trail appended before delivery

### Quality Gates Before Delivery

1. Can a non-lawyer business stakeholder understand the executive summary?
2. Can the counterparty's counsel understand and respond to each proposed redline?
3. Is every legal claim backed by a specific citation or flagged [VERIFY]?
4. Is the overall classification supported by HIGH (0.80+) confidence?
5. Are RED items supported by the self-interrogation 3-pass review?

---

## External Tool Integration

### With legalcode-mcp (preferred)

Use legalcode-mcp in Step 4 to:
- Retrieve current UCTA 1977 / Consumer Rights Act 2015 case law (UK)
- Retrieve current BGB §307-309 enforcement positions (Germany)
- Retrieve current Code Civil Art. 1170 case law (France)
- Retrieve current state-specific UCC §2-719 / unconscionability cases (US)
- Retrieve GDPR Art. 82 / UK GDPR enforcement guidance (EU/UK)
- Retrieve Australian Consumer Law unfair terms enforcement decisions (November 2023 expansion)
- Search for recent significant enforcement decisions or legislative updates

Mark citations from legalcode-mcp searches as VERIFIED in the Glass Box.
Save research to: `/tmp/legalcode-lol-authority.md`

### Without legalcode-mcp

Proceed with jurisdiction-agnostic analysis using the enforceability framework in this
skill. Mark all statutory and case law references with [VERIFY].
Note in the Glass Box: `legalcode_mcp: "Not connected"`.
Focus the analysis on structural quality, market standard assessment, and carve-out
completeness rather than specific legal citation depth.

---

## Output Format Template

```markdown
# Limitation of Liability Review — [Contract Title / Counterparty]

## Classification

**Overall: [GREEN / YELLOW / RED]** | Confidence: [level] | Basis: [playbook / market standards]

[1–2 sentence risk summary for non-legal stakeholders.]

## Route

[Approval authority / Counsel review / Senior escalation required]
[Expected action: accept / negotiate redlines / full redraft]

---

## Executive Summary

[3–5 bullet points covering the most important findings in priority order.
Plain language. Business-focused.]

---

## Tier 1 Findings — Non-Negotiable

[For each Tier 1 finding:]

### [Dimension Name] — RED | Confidence: [level]

**Contract says**: [Exact or summarized language]
**Problem**: [Why this is unacceptable]
**Legal basis**: [Statute / case — VERIFIED or UNVERIFIED]
**Business impact**: [Practical consequence]
**Proposed redline**: [Exact replacement or addition language]
**Fallback position**: [Minimum acceptable compromise]

---

## Tier 2 Findings — Material

[Same format as Tier 1; YELLOW classification]

---

## Tier 3 Findings — Preferred

[Same format; YELLOW or borderline classification]

---

## Holistic Risk Assessment

[Assessment of how the LOL clause interacts with:
- Indemnification obligations
- SLA / service credit / sole-remedy clauses
- Insurance requirements
- Data protection addendum / DPA
- Overall risk allocation balance between the parties]

[Note: Even if individual provisions are GREEN, a holistic structure can create
irrational overall risk allocation.]

---

## Jurisdiction-Specific Enforceability Notes

[For the identified governing law: flag any provisions that may be void or
subject to challenge. Reference specific statutes and confidence level.]

---

## Negotiation Strategy

[Tier 1 must-haves, Tier 2 priorities, Tier 3 preferences. Trade-link suggestions.
How to sequence the negotiation for best results.]

---

## Glass Box Audit Trail

[YAML block — see template above]
```

---

## Localization Notes

When applying this skill to a specific jurisdiction, replace [JURISDICTION-SPECIFIC]
markers with verified local content:

| Jurisdiction | Key Statute | Critical Mandatory Floor | Primary Case |
|-------------|-------------|--------------------------|-------------|
| England/Wales | UCTA 1977; Consumer Rights Act 2015 | Death/PI; fraud; UCTA reasonableness | Photo Production v Securicor [1980] UKHL 2 [VERIFY] |
| Scotland | UCTA 1977 (separate provisions); CRA 2015 | Same as England; judicial approach may differ | [VERIFY Scottish authority] |
| United States | UCC §2-719; state-specific | Willful misconduct (CA); unconscionability | [VERIFY per state] |
| Germany | BGB §307–309 | Death/PI; gross negligence in AGBs | [VERIFY German case law] |
| France | Code Civil Arts. 1170, 1231-3 | Dol; faute lourde; personal injury | [VERIFY French Court of Cassation authority] |
| Australia | ACL (Competition and Consumer Act 2010, Sch 2) | Consumer contracts: death/PI; unfair terms | [VERIFY ACL Nov 2023 amendments] |
| EU cross-border | GDPR Art. 82 (data subjects) | Cannot limit data subject compensation rights | [VERIFY current EDPB guidance] |

For EU member states not listed, apply the relevant national implementation of EU
consumer rights directives and identify local court interpretation of "unfair terms"
under Directive 93/13/EEC. [VERIFY]

---

## Provenance

Created by Legalcode (2026-03-01). Original synthesis based on:
- Deep legal research on limitation of liability enforceability across US, UK, EU
  (Germany, France), and Australian law
- Analysis of structural patterns from `legalcode-contract-review`, `legalcode-nda-triage`,
  and `legalcode-saas-agreement-drafter` reference skills
- Market standards from Norton Rose Fulbright Liability 101 guide, JDSupra Morgan Lewis
  LOL carve-out analysis, IAPP data privacy liability coverage, ACC resources, and
  Contract Nerds practitioner guides
- Key legal authority: Photo Production v Securicor [1980] UKHL 2; UCTA 1977; BGB
  §307–309; Code Civil Art. 1170 (2016 reform); UCC §2-719; Hadley v Baxendale (1854)
- Legalcode original synthesis — no imported third-party skill content

All statutory and case law references should be verified against authoritative sources
before use in legal advice contexts. Laws change; this skill reflects the state of
knowledge as of March 2026.
