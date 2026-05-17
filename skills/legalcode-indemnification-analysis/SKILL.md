---
name: legalcode-indemnification-analysis
description: >
  Deep analysis of indemnification provisions across commercial contract types — review
  indemnification scope (first-party vs. third-party claims), caps and baskets (deductible
  basket vs. tipping basket, mini-basket thresholds), materiality qualifiers and scrapes,
  defense and control-of-claim mechanics (duty to defend, right to control defense, right
  to settle, cooperation obligations, Cumis counsel in US), survival periods by claim type,
  and interaction with limitation of liability provisions. Evaluates indemnification exposure
  across IP infringement, confidentiality breach, data protection violations, and regulatory
  claims. Compares against market standards by contract type (SaaS, M&A, professional
  services, construction). Use when reviewing or drafting indemnification provisions in any
  commercial agreement, when assessing indemnification exposure from a counterparty's draft,
  when negotiating IP or data breach indemnification obligations, or when structuring M&A
  indemnification baskets and caps. Produces GREEN/YELLOW/RED classification with
  risk-adjusted exposure analysis, confidence-scored redline recommendations, Glass Box
  audit trail, and jurisdiction-aware enforceability notes for US, UK, and Australia.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode Indemnification Analysis

> **Disclaimer**: This skill provides a framework for AI-assisted indemnification clause
> analysis. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional licensed in the relevant jurisdiction before use. Laws change;
> verify current applicability before relying on any provision described here. Indemnification
> enforceability, duty-to-defend obligations, and basket mechanics are highly
> jurisdiction-sensitive — mandatory statutory constraints (anti-indemnity statutes, civil
> law equivalents, proportionate liability schemes) vary materially across governing laws.
> Statutory and case law references cited from memory carry hallucination risk — verify
> against authoritative sources before relying on them.

---

## Purpose and Scope

This skill performs deep, clause-level analysis of indemnification provisions in commercial
contracts. It evaluates indemnification scope, basket and cap structures, defense mechanics,
survival periods, and the interaction with the broader liability regime — and produces
confidence-scored findings with actionable redline suggestions.

Indemnification is consistently ranked among the top three most negotiated clauses in
commercial contracts (World Commerce & Contracting Association). It is also the clause most
often rendered commercially irrational by: (1) misaligned scope (too broad or too narrow);
(2) missing defense obligations (indemnify but not defend); (3) inadequate settlement control
provisions; and (4) failure to harmonize with the limitation of liability clause. This skill
addresses all four failure modes.

**Covers:**
- Indemnification scope: first-party claims (between contracting parties) vs. third-party
  claims (from outsiders) — and the critical distinction between the two
- Baskets: deductible (true deductible) vs. tipping (threshold/first dollar) and
  mini-baskets (per-claim de minimis thresholds)
- Caps on indemnification: general caps, super-caps for high-risk categories, uncapped
  carve-outs for fraud and fundamental matters
- Materiality qualifiers in representations and the "scrape" mechanism for M&A contexts
- Defense and control-of-claim mechanics: duty to defend vs. duty to indemnify, right
  to control defense, settlement consent, cooperation obligations, Cumis counsel (US)
- IP infringement indemnification: scope, carve-outs, remedy waterfall
- Data protection and privacy indemnification: regulatory fines vs. private claims,
  GDPR Art. 82 [VERIFY], breach notification costs, super-caps
- Confidentiality breach indemnification
- Regulatory claims and fines: governmental investigation costs, penalty allocation
- Survival periods by claim type: fundamental reps vs. general reps vs. tax vs. fraud
- Interaction with limitation of liability: what sits inside vs. outside the LOL cap
- Knock-for-knock indemnity structures (energy, construction, offshore)
- Cross-indemnification, contribution, and subrogation mechanics
- Anti-indemnity statutes (US construction: Texas, Louisiana, California, others)
  [JURISDICTION-SPECIFIC]
- Proportionate liability schemes (Australia) and their effect on indemnification
- Market standards by contract type: SaaS, M&A, professional services, construction
- GREEN/YELLOW/RED classification with confidence scoring
- Risk-adjusted exposure analysis and negotiation strategy

**Does not:**
- Review limitation of liability caps, consequential damages exclusions, or cap
  adequacy independent of indemnification (see `legalcode-limitation-of-liability-review`)
- Perform comprehensive clause-by-clause review of any commercial agreement
  (see `legalcode-contract-review`)
- Replace qualified counsel — particularly for high-value M&A, complex insurance-linked
  transactions, regulated-sector contracts, or cross-border transactions where enforceability
  turns on specific local law
- Apply to insurance policies or surety bonds (different legal framework)

**Related skills:**
- `legalcode-limitation-of-liability-review` — deep analysis of LOL caps, exclusions,
  and carve-outs; use alongside this skill for complete risk allocation review
- `legalcode-contract-review` — full clause-by-clause review of any commercial agreement
- `legalcode-contract-risk-scorer` — quantified risk scoring of final contract terms
- `legalcode-dpa-review-and-negotiation` — specialized DPA clause analysis for data
  protection indemnification obligations
- `legalcode-master-services-agreement` — MSA-specific indemnification frameworks
- `legalcode-saas-agreement-drafter` — SaaS agreement indemnification structures

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The contract's governing law clause determines which
legal framework applies. The review identifies the governing law early and flags
jurisdiction-specific enforceability issues throughout.

[JURISDICTION-SPECIFIC] When localizing for these primary jurisdictions, research and apply:

**United States**
- **Duty to defend vs. duty to indemnify**: Under US common law, these are distinct obligations.
  The duty to defend is broader — triggered by allegations (not proven liability) — and
  potentially more valuable than the indemnification obligation itself. The duty to defend
  arises when the complaint potentially states a covered claim; the duty to indemnify arises
  on actual adjudicated or settled liability. [VERIFY per applicable state law]
- **Anti-indemnity statutes**: Many US states prohibit or limit indemnification of a party
  for its own negligence in construction contracts:
  - California (Cal. Civ. Code § 2782): prohibits indemnification for sole negligence or
    willful misconduct in construction contracts; allows partial indemnification for concurrent
    negligence [VERIFY current version]
  - Texas (Tex. Ins. Code § 151.102; Tex. Civ. Prac. & Rem. Code § 130.002): Construction
    anti-indemnity statute prohibits indemnification for indemnitee's own negligence in certain
    contracts; insurance provision rules apply [VERIFY current version]
  - Louisiana (La. R.S. 9:2780): Indemnification for own negligence is void in oilfield and
    mineral contracts; broader construction provisions [VERIFY current version]
  - Colorado, Michigan, North Carolina, and ~30 other states: have varying anti-indemnity
    statutes for construction [VERIFY per state]
- **First-party vs. third-party claims**: Whether an indemnity clause covers first-party
  claims (between contracting parties) depends on the specific language. Courts require "clear
  and unequivocal" language to extend indemnity to first-party claims. The New Jersey Supreme
  Court held a clause cannot apply to first-party claims without specific expanding language
  [VERIFY: Kutzin v. Pirnie and subsequent NJ cases]. California courts have held that "any
  claims" language covers both [VERIFY current CA approach].
- **Gross-up obligations**: Indemnification payments may be taxable income to the recipient.
  Tax gross-up provisions ensure the indemnified party is made "whole" after taxes.
  [VERIFY: applicable IRC provisions and IRS guidance on indemnification payments]
- **Cumis counsel**: In California and some other states, where an insurer defends under a
  reservation of rights, the insured may be entitled to independent counsel paid by the
  insurer (Cumis counsel). This principle can inform indemnification agreements with defense
  obligations where conflicts of interest may arise. [VERIFY: San Diego Navy Federal Credit
  Union v. Cumis Insurance Society, Inc. (1984); Cal. Ins. Code § 2860] [JURISDICTION-SPECIFIC]
- **M&A basket and cap market standards** (ABA Deal Points Study [VERIFY most recent edition]):
  - General/specific basket: 0.5%–1.0% of deal value (deductible or tipping)
  - Cap: 10%–15% of deal value for general reps; 100% for fundamental reps; uncapped for fraud
  - Survival periods: 12–24 months for general reps; indefinite for fundamental reps and fraud

**United Kingdom / England & Wales**
- **Indemnity as a primary obligation**: Under English law, an indemnity is a primary obligation
  distinct from a claim for damages for breach of contract. Indemnities may bypass remoteness
  rules (Hadley v Baxendale [VERIFY]) and limitation of actions differences apply. An indemnity
  is potentially wider in scope than equivalent damages at law. [VERIFY: Caledonia North Sea Ltd
  v British Telecommunications plc [2002] UKHL 4 — indemnity vs. damages analysis]
- **Contra proferentem**: Indemnity clauses will be construed strictly against the party relying
  on them. Ambiguous language is construed narrowly. Courts require clear, unequivocal language
  to cover losses beyond the ordinary scope of the obligation.
- **UCTA 1977**: In B2B contracts, clauses excluding or restricting liability must satisfy the
  reasonableness test. Indemnity clauses that effectively transfer statutory liability may also
  be subject to UCTA scrutiny. [VERIFY: Regus (UK) Ltd v Epcot Solutions Ltd [2008] EWCA Civ 361]
- **No duty to defend (English law)**: English law does not recognize the US-style "duty to
  defend" (i.e., an obligation to take over and fund the defense of third-party claims). The
  typical English mechanism is an indemnity against costs, losses, and liabilities arising from
  third-party claims — the indemnified party defends and then claims its costs under the
  indemnity. Control-of-claim provisions must be expressly and clearly drafted.
- **Proportionate liability / contributory negligence**: An indemnitee's contributory negligence
  may reduce recovery under the Civil Liability (Contribution) Act 1978 [VERIFY]. Express
  language is needed to make an indemnity absolute regardless of contributory negligence.
- **IP indemnification**: IP infringement indemnities are standard in technology contracts.
  The Technology Law Alliance, Practical Law, and leading UK firms' standard positions require
  uncapped (or super-capped) IP indemnities from service providers for third-party infringement
  claims arising from use of the vendor's product as supplied. [VERIFY current UK market data]

**Australia**
- **Proportionate liability schemes**: All Australian states and territories have enacted
  proportionate liability legislation based on the model Proportionate Liability Act. Under
  these schemes, each "concurrent wrongdoer" is liable only for their proportionate share of
  loss in claims for economic loss or property damage caused by negligence.
  - **Queensland (Civil Liability Act 2003 (Qld))**: Explicitly prohibits contracting out of
    proportionate liability — contractual indemnities that re-apportion loss between concurrent
    wrongdoers may not be enforceable for property damage and economic loss claims [VERIFY
    current Qld position].
  - **New South Wales (Civil Liability Act 2002 (NSW), s.3A)**: Expressly acknowledges that
    contracting parties may provide for their rights and liabilities, potentially permitting
    contractual indemnities to re-apportion proportionate liability [VERIFY current NSW position].
  - **Victoria**: Does not include the NSW-style express acknowledgment; position on contractual
    indemnity re-apportionment is less clear [VERIFY current Vic position].
- **Australian Consumer Law (ACL)**: Unfair contract terms regime (expanded November 2023 to
  include small business contracts with civil penalties). Broad indemnification obligations in
  standard form contracts may be challenged as unfair terms. [VERIFY current ACL enforcement
  positions post-November 2023]
- **Privacy Act 1988 (Cth)**: Indemnification provisions related to data breaches must account
  for obligations under the Notifiable Data Breaches (NDB) scheme. Regulatory liability to the
  OAIC cannot be contractually transferred; indemnification allocates costs between the
  contracting parties only. [VERIFY current NDB enforcement positions]
- **Knock-for-knock and construction**: Australian courts recognize knock-for-knock indemnity
  structures. The enforceability of indemnities against a party's own negligence in construction
  depends on state-specific legislation and the proportionate liability scheme. [VERIFY per state]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming the
user's intent, the workflow pauses and asks when:

- The answer changes which side's position to optimize (indemnitee vs. indemnifying party)
- Contract type determines which market standards and basket structures apply
- Deal value affects exposure calculation and basket adequacy
- Jurisdiction determines which statutory constraints apply

Use the structured clarification pattern (options + "why this matters") wherever marked with
**⟁ CLARIFY** below. If the user has already provided the information, skip the question and
proceed — but **state assumptions explicitly** (e.g., "I'm assuming you are on the indemnitee
side — tell me if that's wrong and I'll re-run the analysis").

---

## Workflow

### Step 1: Accept Input

Accept the indemnification provision in any of these formats:

- **Clause extract**: The indemnification clause (or clauses) pasted directly — include
  the limitation of liability clause and any IP, data breach, or regulatory provisions
  nearby, as these interact materially with the indemnification structure.
- **Full contract**: A complete agreement to be reviewed for indemnification structure.
- **File or URL**: A document in PDF, DOCX, or linked format.
- **Partial text**: Even a single paragraph triggers analysis; note what context is missing
  and request it.

**Also look for:**
- IP indemnification provisions (often separate clauses or schedules)
- Data Processing Addendum / DPA (may contain data breach indemnification)
- M&A representations and warranties sections (survival and indemnification procedures
  often in a separate Article in an SPA or APA)
- Insurance clause (may carve out or require specific indemnification structures)
- Dispute resolution clause (affects control-of-claim mechanics)

If the indemnification clause is absent entirely, flag it as a RED gap and proceed with
the analysis of what an appropriate clause should contain.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask these questions. Skip any already answered
by the user:

1. **Which side are you on?**
   - Options: Indemnitee (receiving indemnification / protected party), Indemnifying party
     (providing indemnification / obligated party), Neutral / reviewing for both sides, Other
   - *Why this matters*: The entire risk analysis inverts. An uncapped indemnity obligation
     is catastrophic for the indemnifying party; a capped indemnity is dangerous for the
     indemnitee. Advice on "acceptable" terms depends entirely on which side bears the risk.

2. **What type of contract is this?**
   - Options: SaaS / technology services, Professional services / MSA, M&A / share purchase
     / asset purchase, Software license, Procurement / supply chain, Construction / EPC,
     Outsourcing (BPO/ITO), Energy / resources, Other / mixed
   - *Why this matters*: Market standards for scope, baskets, caps, and defense mechanics
     vary fundamentally across contract types. M&A indemnification operates on entirely
     different economics from SaaS or construction.

3. **What is the approximate deal value / annual contract value?**
   - Options: Under $100K / £100K / AUD 150K, $100K–$1M, $1M–$10M, Over $10M / M&A
     transaction, Not sure / not relevant
   - *Why this matters*: Basket and cap adequacy must be assessed relative to deal value.
     A $100K basket on a $1M deal is standard; a $100K basket on a $50M deal is token.
     Exposure calculations require an order-of-magnitude estimate.

4. **What is the governing law / jurisdiction?**
   - Options: US (specify state if known — critical for anti-indemnity statutes), English /
     UK law, Australian law (specify state if known — critical for proportionate liability),
     Other / not stated, Multiple jurisdictions
   - *Why this matters*: Anti-indemnity statutes (US construction), proportionate liability
     schemes (Australia), and UCTA constraints (UK) can void or limit indemnification clauses
     that are otherwise valid. The analysis must account for mandatory statutory limits.

5. **Are specific risk categories a priority?**
   - Options (multi-select): IP infringement claims, Data breach / privacy violations,
     Regulatory investigations and fines, Confidentiality breach, Personal injury / property
     damage, General contractual breach, M&A basket and cap structure, All of the above
   - *Why this matters*: The IP and data breach indemnification analysis is different from
     general contractual indemnification. Knowing the priority risk categories lets the
     analysis lead with what matters most.

6. **Do you have the organization's negotiation playbook positions?**
   - Options: Yes, I'll provide them, Use general market standards (no playbook),
     I'll provide key positions as we go
   - *Why this matters*: Playbook positions define what is "acceptable" for GREEN
     classification. Without them, analysis defaults to market standards.

If the user provides partial context, proceed with what you have and **state all assumptions
explicitly** at the start of the analysis.

### Step 3: Load Playbook or Market Standards

Check for the organization's indemnification playbook positions in local settings (e.g.,
`legal.local.md` or `playbook.md`). The playbook should define:

- **Standard positions**: Preferred scope, cap, basket, and defense mechanics by contract type
- **Acceptable ranges**: What can be agreed without escalation
- **Hard limits**: Non-negotiable positions (e.g., always require IP indemnity; never accept
  uncapped first-party indemnification)

**If no playbook is configured:**

**⟁ CLARIFY** — Inform the user that no playbook was found. Ask:

- **Option A: Provide positions now** — Walk through 6 key indemnification positions:
  scope (first-party / third-party / both), uncapped categories, maximum indemnification
  cap, required defense obligation, basket structure (M&A only), and IP indemnification
  requirements. Takes time upfront; makes the analysis precise.
- **Option B: Use market standards** — Use the contract-type-specific market standards
  defined in this skill. Faster; may not reflect your organization's risk appetite.
- **Option C: Positions as we go** — Begin analysis; ask for your position when each
  element is reached.

Label the analysis clearly: "Based on [organizational playbook / market standards for
[contract type] / user-provided positions]".

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Identify the governing law from the contract's governing law clause or context.

Use **legalcode-mcp** (if connected) to build a working legal reference file:

```
Search targets:
- "indemnification [jurisdiction] commercial contracts scope defense"
- "anti-indemnity statute [state] construction" (US)
- "proportionate liability [state] contractual indemnity" (Australia)
- "duty to defend [jurisdiction] commercial indemnification"
- "IP indemnification [jurisdiction] market standard"
- "data breach indemnification [jurisdiction] regulatory fines"
- "indemnification basket cap [jurisdiction] M&A deal terms"
```

Save results to: `/tmp/legalcode-indemnification-authority.md`

**Without legalcode-mcp:** Proceed with jurisdiction-agnostic analysis using the
enforceability framework in this skill. Mark all statutory references with [VERIFY].
Note in the Glass Box: `legalcode_mcp: "Not connected"`.

### Step 5: Read the Indemnification Ecosystem Holistically

Before dimension-by-dimension analysis, read the entire indemnification structure:

1. **Locate all indemnification-related provisions** — indemnification is often spread
   across: the main indemnification clause, IP indemnification, data breach provisions,
   regulatory compliance clauses, the limitation of liability clause (carve-outs for
   indemnification), insurance clause, and any DPA or BAA.

2. **Map the obligation structure** — Does the contract have:
   - A general indemnification clause?
   - Specific carve-out indemnifications (IP, data breach, regulatory)?
   - Defense obligations (duty to defend) alongside indemnification?
   - Basket and cap structures (M&A context)?

3. **Note mutual vs. unilateral structure** — Is indemnification mutual? Or does only one
   party provide indemnification? Unilateral structures warrant scrutiny.

4. **Check the LOL interaction** — Is the indemnification obligation:
   - Inside the general limitation of liability cap?
   - Carved out from the cap (uncapped)?
   - Subject to a super-cap?
   - Silent on this question (creates ambiguity — flag immediately)?

5. **Flag obvious structural issues** before deep analysis:
   - No indemnification clause at all (RED gap for any commercial contract)
   - First-party indemnification without clear triggering language (litigation risk)
   - Defense obligation missing from indemnification (major gap — most costly omission)
   - Uncapped indemnification with no corresponding insurance requirement
   - Indemnification that purports to cover the indemnifying party's own gross negligence
     or fraud (may be void and creates adversarial dynamic)

### Step 6: Deep Indemnification Analysis

Analyze the indemnification structure against each of the following 10 dimensions. For each
dimension, assign PASS / FLAG, note the specific language, apply a confidence score, and
generate a finding.

---

#### Dimension 1: Scope — First-Party vs. Third-Party Claims

**What to assess:**

Indemnification provisions traditionally cover two distinct categories:

| Scope | Definition | Risk Profile |
|-------|-----------|-------------|
| **Third-party claims** | Claims brought by persons not party to the contract (customers, regulators, competitors, injured parties) — the indemnifying party defends and pays | Standard; expected in commercial contracts; typically the narrower scope |
| **First-party claims** | Direct claims between the contracting parties (e.g., Party A indemnifies Party B for losses Party B itself suffers from Party A's breach) | High risk for indemnifying party — expands beyond what "damages for breach" provides; may bypass limitation periods and remoteness rules |
| **Both** | Language covering "any loss, claim, or damage" without qualification | Broadest scope; most litigation-prone; requires explicit language in most jurisdictions |

**Why first-party scope matters:** An indemnity that covers first-party claims can provide
a claimant with more advantageous recovery than a pure damages claim — potentially bypassing
Hadley v Baxendale remoteness [VERIFY], limitation of actions constraints, and damages
mitigation obligations. Courts in most jurisdictions require "clear and unequivocal" language
to read first-party claims into an indemnity provision.

[JURISDICTION-SPECIFIC] Under English law, the contra proferentem principle requires
unambiguous language to extend an indemnity to first-party losses. Under New Jersey law,
a general indemnity clause does not cover first-party claims without specific language
[VERIFY: Kutzin v. Pirnie]. Under California law, "any claims" language may cover both
[VERIFY current CA approach].

**Assessment criteria:**
- [ ] Scope (third-party only, first-party only, or both) is unambiguous
- [ ] If first-party scope is intended, express language reflects this clearly
- [ ] "Losses" definition, if present, clearly delineates what is covered (costs, damages,
  judgments, settlement amounts, attorneys' fees, regulatory fines)
- [ ] Scope does not inadvertently override the limitation of liability clause
- [ ] Cross-party indemnification (where Party A indemnifies Party B's own losses from Party
  A's acts) is clearly limited to "arising from Party A's breach" not "any loss suffered by
  Party B"

---

#### Dimension 2: Caps and Baskets (M&A and Commercial Contexts)

**What to assess:**

In M&A transactions, indemnification caps and baskets are the central economic negotiation.
In commercial contracts, caps and baskets are less common but increasingly used for specific
risk categories.

**Basket structures:**

| Structure | Mechanics | Effect |
|-----------|-----------|--------|
| **Deductible basket (true deductible)** | Indemnification applies only to losses EXCEEDING the basket; the buyer absorbs the basket amount | Like an insurance deductible — lower recovery for claimant; preferred by seller/indemnifying party |
| **Tipping basket (threshold / first-dollar)** | Once cumulative losses exceed the basket threshold, ALL losses from the first dollar are recoverable | Much more favorable to claimant; standard in US M&A; disputed in UK M&A |
| **Mini-basket (per-claim threshold)** | Individual claims below the mini-basket threshold are excluded regardless of aggregate losses | Prevents de minimis claims; does not reduce maximum recovery once threshold crossed |

**Market standards by contract type (US M&A — ABA Deal Points Study [VERIFY most recent]):**

| Metric | Range | Median |
|--------|-------|--------|
| General basket | 0.5%–1.5% of deal value | 0.75% |
| Basket type | ~50% tipping, ~30% deductible, ~20% hybrid [VERIFY] | Tipping basket more common in US |
| General cap | 10%–20% of deal value | 10%–15% |
| Fundamental rep cap | 100% of deal value | 100% |
| Fraud: uncapped | Standard | Uncapped (contractual fraud is not capped in any jurisdiction) |

**Commercial contract baskets (technology/services):**
- Baskets are less common in pure services contracts but increasingly seen for specific
  risk categories (e.g., data breach indemnification may have a mini-basket to exclude
  de minimis incidents)
- Some commercial agreements use "thresholds" on IP indemnification (e.g., claims below
  $50K are excluded from the defense obligation)

**Assessment criteria:**
- [ ] Basket type (deductible vs. tipping) is unambiguously stated
- [ ] Basket amount is proportionate to deal value and realistic loss expectations
- [ ] Mini-basket amount (if present) excludes only genuinely de minimis claims
- [ ] Exclusions from the basket (items counted against the basket vs. excluded entirely)
  are clearly stated
- [ ] Aggregate cap on indemnification is stated (unlimited indemnification is commercially
  irrational for the indemnifying party)
- [ ] Cap on fundamental representations is separate from and higher than the general cap
- [ ] Fraud is excluded from any cap (fraud caps are unenforceable as a matter of public
  policy in US/UK/AU)
- [ ] Super-caps for specific categories (IP, data breach) are appropriate

---

#### Dimension 3: Materiality Qualifiers and Scrapes

**What to assess (primarily relevant for M&A indemnification):**

In M&A transactions, representations and warranties often contain materiality qualifiers
("material adverse effect," "in all material respects," "materially"). When a rep is
breached and the indemnification obligation is triggered, the question arises: does
materiality continue to apply when calculating the indemnification amount?

**The "scrape" mechanic:** A materiality scrape removes (or "scrapes out") the materiality
qualifiers from the representations for purposes of determining (a) whether a breach occurred
and/or (b) the amount of losses recoverable. Without a scrape, the party seeking
indemnification must prove a "material" breach — which may effectively preclude recovery
for real but small breaches. With a scrape, every breach triggers indemnification (subject
to the basket).

**Types of scrapes:**
- **Single scrape**: Materiality qualifiers removed only for calculating the amount of
  losses (not for determining whether a breach occurred). The claimant must still prove
  a material breach to trigger the obligation.
- **Double scrape**: Materiality qualifiers removed for both breach determination and loss
  calculation. Most favorable to the claimant; allows recovery for any breach regardless
  of materiality.
- **No scrape**: Materiality qualifiers retained for all purposes — most favorable to the
  indemnifying party.

**Market standard**: In US M&A, double scrapes are increasingly common (approximately
60%–70% of deals per ABA Deal Points Study [VERIFY]). Single scrapes and no scrapes remain
in seller-favorable deals.

**Assessment criteria:**
- [ ] Presence/absence of materiality scrape is clearly stated (or absence is recognized)
- [ ] Scrape type (single / double / none) is clear from the language
- [ ] Knowledge qualifiers (e.g., "to Seller's knowledge") are addressed separately —
  knowledge qualifiers are typically NOT scraped even when materiality is
- [ ] Scrape interaction with the basket is addressed (double scrape + tipping basket is
  the most buyer-favorable combination)

---

#### Dimension 4: Defense and Control-of-Claim Mechanics

**What to assess:**

This dimension covers the most operationally critical indemnification provisions — what
actually happens when a third-party claim is made. A structurally correct indemnification
clause with no defense mechanics is commercially incomplete.

**Key elements:**

| Element | What It Provides | Risk if Missing |
|---------|-----------------|-----------------|
| **Duty to defend** | Indemnifying party takes over and funds the defense of third-party claims (US concept; not applicable under English law as a legal obligation) | Indemnitee must fund defense then recover via indemnity — cashflow risk; may be impractical for SMEs |
| **Right to control defense** | Indemnifying party has the right to select counsel and control strategy for covered claims | Without this right, the indemnifying party bears cost but has no control — perverse incentive |
| **Notification obligation** | Indemnitee must promptly notify the indemnifying party of a claim | Without prompt notice, indemnifying party may lose the ability to defend — courts may reduce recovery for late notice in some jurisdictions |
| **Right to settle** | Indemnifying party may settle covered claims; indemnitee's consent may be required | Without consent protection, indemnitee can be forced into unfavorable settlement terms |
| **Consent standard for settlement** | Indemnitee's consent "not to be unreasonably withheld" (standard) or "sole discretion" (aggressive) | Unreasonable withholding of consent may expose the indemnitee to excess damages above the settlement amount |
| **Cooperation obligations** | Indemnitee must cooperate with defense: provide documents, witnesses, access | Without cooperation, defense may be compromised — indemnifying party may argue this as a defense |
| **Cumis counsel (US)** | Where a conflict of interest exists between the insurer/indemnifying party and indemnitee, the indemnitee may be entitled to select independent counsel at the indemnifying party's expense | Applies primarily in insurance contexts; can be relevant where indemnification is paired with a duty to defend [JURISDICTION-SPECIFIC: California and some other US states] |

**Defense obligation structure by jurisdiction:**

| Jurisdiction | "Duty to Defend" Concept | Typical Commercial Mechanism |
|-------------|------------------------|------------------------------|
| **US (general)** | Recognized; typically broader than indemnity (triggered by allegations) | Explicit "defend, indemnify, and hold harmless" language creates defense obligation |
| **England/Wales** | Not recognized as a primary legal obligation | Indemnity against "costs, claims, losses, and liabilities" — indemnitee defends and recovers costs |
| **Australia** | Similar to England — no automatic duty to defend | Express control-of-claim language required; recovery mechanism differs from US |

**Notice requirements by jurisdiction:**

[JURISDICTION-SPECIFIC] Late notice may affect recovery under an indemnification provision:
- **US**: Courts are split on whether late notice is a defense to indemnification; some
  states require prejudice from late notice before reducing recovery [VERIFY per state]
- **England/Wales**: Failure to give prompt notice may be a breach of condition or
  warranty depending on drafting; courts assess prejudice from delay [VERIFY current
  English case law]
- **Australia**: Notice requirements are interpreted strictly; late notice may defeat
  a claim if the indemnifying party can show prejudice [VERIFY per state]

**Assessment criteria:**
- [ ] Defense obligation (duty to defend or its equivalent mechanism) is expressly stated
- [ ] Control of defense right is allocated (to indemnifying party, with clear exceptions)
- [ ] Notice obligation is present and the notice period is specified (typically "prompt" or
  within a specific number of days of receiving the claim)
- [ ] Settlement consent is required from the indemnitee (standard position)
- [ ] Consent standard is "not to be unreasonably withheld, conditioned, or delayed"
  (rather than sole discretion)
- [ ] "No admission" protection is included (indemnitee cannot admit liability or make
  statements that prejudice the defense without indemnifying party's consent)
- [ ] Cooperation obligations are present but not unduly burdensome
- [ ] Consequence of late notice is specified (or, absent language, flag as ambiguous)
- [ ] Conflict of interest provisions address what happens when indemnitee's and indemnifying
  party's interests diverge in defending the claim

---

#### Dimension 5: IP Infringement Indemnification

**What to assess:**

IP indemnification is typically the most significant single indemnification obligation in
technology, SaaS, and software agreements. The vendor/licensor indemnifies the customer
for third-party claims that use of the vendor's product infringes a third party's
intellectual property rights.

**Scope variables:**

| Element | Vendor-Favorable | Customer-Favorable |
|---------|-----------------|-------------------|
| **Coverage trigger** | "Finally adjudicated infringement" only (no coverage during litigation) | Any claim of infringement (including pending claims) |
| **Remedy coverage** | Damages and settlements only | Damages, settlements, defense costs, and related expenses |
| **Infringing use carve-outs** | Customer modifications, combination with unauthorized third-party products, continued use after notice to cease — all excluded | Narrow carve-outs: only customer's own modifications to the infringing element; not combination claims |
| **Geographic scope** | Limited to specific jurisdictions | Global / worldwide |
| **Open source** | Open-source components excluded from IP indemnity | Vendor must manage OSS IP risk; no blanket exclusion |
| **Super-cap / uncapped** | Capped at 1–2× contract value | Uncapped (historically market standard; shifting to super-cap) |

**Remedy waterfall (standard market structure):** When a third-party IP claim arises:
1. Vendor obtains a license for the customer to continue using the product
2. Vendor modifies the product to remove the infringing element
3. Vendor substitutes equivalent non-infringing product
4. Vendor terminates the license and refunds pre-paid fees

**IP indemnification and the LOL interaction (critical):**
IP indemnification is the most common carve-out from the general limitation of liability cap.
However, even "uncapped" IP indemnities are increasingly subject to super-caps in technology
contracts. The trend (per Norton Rose Fulbright Liability 101 Guide [VERIFY]) shows:
- Service providers limiting uncapped IP indemnities to third-party claims amounts (not system
  replacement costs)
- Super-caps for IP indemnification at 2–5× annual contract value becoming standard
- Cloud/SaaS providers accepting cap at 12 months' fees maximum for general liability;
  IP indemnity at higher levels

**Assessment criteria:**
- [ ] IP indemnification obligation is present (missing = RED for technology contracts)
- [ ] Scope covers third-party claims of infringement (not limited to "finally adjudicated"
  without interim defense coverage)
- [ ] Defense costs are covered (not just ultimate judgment or settlement)
- [ ] Carve-outs within IP indemnity are reasonable:
  - Customer modifications: narrowly scoped (only where modification is the cause)
  - Combination: only where combination not authorized/anticipated by vendor
  - Continued use: only after notice and reasonable cure opportunity
  - Open source: vendor manages OSS; not blanket exclusion
- [ ] Remedy waterfall is present (license → modify → substitute → refund)
- [ ] Super-cap or uncapped status is clearly stated (and amount is proportionate to risk)
- [ ] IP indemnity is carved out from the general LOL cap (or explicitly inside it — flag
  if inside the cap as YELLOW or RED depending on cap level)

---

#### Dimension 6: Data Protection and Privacy Indemnification

**What to assess:**

Data protection indemnification covers two distinct risk categories that must be analyzed
separately:

| Category | What It Covers | Key Issues |
|----------|---------------|------------|
| **Regulatory fines and penalties** | Governmental/regulatory fines for data protection violations (GDPR Art. 83, US state penalties, OAIC fines) | Contractual indemnification between parties doesn't reduce regulatory liability to the regulator; it allocates payment responsibility between the contracting parties |
| **Third-party claims** | Private claims from data subjects (GDPR Art. 82, CCPA private rights of action [VERIFY scope], class actions) | These are indemnifiable; critical question is who pays when a joint controller/processor breach leads to data subject claims |
| **Breach response costs** | Notification costs, forensic investigation, credit monitoring, remediation | Often contractually allocated; frequently excluded from standard indemnification caps |
| **Business interruption** | Revenue lost due to a data breach incident | More difficult to indemnify; typically excluded or subject to consequential damages exclusions |

**Regulatory fine allocation between contracting parties:**

[JURISDICTION-SPECIFIC] Under GDPR (EU/UK), the regulatory fine is imposed on the controller
or processor by the supervisory authority. The fine itself cannot be allocated by contract —
the regulator will collect it from the entity found responsible. However, the contractual
indemnification allocates who ultimately bears the economic burden between the parties:
- Controller-to-processor indemnification: If the processor's breach caused the fine against
  the controller, the controller may seek indemnification from the processor
- Processor's GDPR obligations: Under Art. 82, both controllers and processors can be
  liable to data subjects. The party that pays compensation may seek contribution from the
  other [VERIFY: GDPR Art. 82(5) right of recourse]

**Assessment criteria:**
- [ ] Data breach / privacy violation is carved out from the general LOL cap (or clearly
  inside it with an appropriate super-cap)
- [ ] Scope distinguishes between regulatory fines and third-party claims (different risk
  profiles and allocation logics)
- [ ] Breach response costs (forensic, notification, remediation) are explicitly covered
- [ ] Super-cap or uncapped treatment is stated; amount is proportionate (market range:
  100%–500% of contract fees for data/security breaches per Norton Rose Fulbright [VERIFY])
- [ ] GDPR / UK GDPR / Privacy Act controller-processor responsibility allocation is
  addressed (who bears regulatory investigation costs? who pays if a supervisory authority
  opens a formal investigation following an incident?)
- [ ] Data breach indemnification is not swept in by a "sole remedy" SLA provision
- [ ] Cross-border indemnification for multi-regime data protection obligations is addressed
  where the contract involves international data flows

---

#### Dimension 7: Confidentiality Breach Indemnification

**What to assess:**

Confidentiality breach indemnification is distinct from the confidentiality clause itself.
The confidentiality clause defines the obligation; indemnification (or a separate damages
regime) determines the remedy.

**Key variables:**
- Is breach of confidentiality covered by the general indemnification clause? Or does the
  confidentiality clause have its own dedicated remedy (often injunctive relief + damages)?
- Is confidentiality breach carved out from the general LOL cap?
- What losses are covered? Direct losses only, or also third-party claims arising from
  the other party's disclosure of trade secrets, personal data, or proprietary information?
- Is the indemnification mutual for confidentiality breach? (Should be YES — both parties
  owe confidentiality obligations)

**Assessment criteria:**
- [ ] Confidentiality breach is either: (a) covered by the general indemnification clause,
  or (b) has a separate express remedy
- [ ] Confidentiality breach is carved out from the general LOL cap (market standard for
  high-value or data-sensitive contracts)
- [ ] Losses covered include: direct losses from disclosure AND third-party claims arising
  from the breach
- [ ] Trade secret misappropriation is addressed (particularly in US jurisdictions where
  DTSA provides federal overlay) [VERIFY: Defend Trade Secrets Act 18 U.S.C. § 1836]
- [ ] Confidentiality breach indemnification is mutual

---

#### Dimension 8: Regulatory Claims and Fines Indemnification

**What to assess:**

Beyond data protection, contracts may involve indemnification for regulatory violations,
governmental investigations, or compliance failures. Key contexts:

| Context | Regulatory Category | Indemnification Considerations |
|---------|-------------------|-------------------------------|
| **Financial services** | SEC/FCA investigations, AML penalties, sanctions violations | Who pays investigation costs? Who bears penalty if conduct is attributable to counterparty? |
| **Healthcare / life sciences** | FDA, TGA, MHRA enforcement; HIPAA penalties (US) | Regulatory allocation particularly important for contract research, manufacturing |
| **Construction / infrastructure** | Building code violations, environmental fines, WHS penalties | Proportionate liability (AU); anti-indemnity statutes (US) |
| **Employment / labor** | Workers' compensation, OSHA fines, unfair dismissal claims | Typically allocated to employing party; indemnification for contractor-related workforce claims |
| **Anti-bribery / corruption** | FCPA (US), Bribery Act (UK), Criminal Code Act (AU) | Supply chain due diligence; who bears fine if third-party supplier is found in breach? |

**Assessment criteria:**
- [ ] Regulatory claims covered by indemnification are specifically identified (not left
  to inference from "any claims")
- [ ] Allocation of regulatory investigation costs is stated
- [ ] Allocation of resulting fines or penalties between the parties is stated
- [ ] Anti-bribery / sanctions compliance obligations are cross-referenced
- [ ] FCPA / Bribery Act / local equivalents are appropriately addressed for cross-border
  contracts [JURISDICTION-SPECIFIC]
- [ ] Indemnification for regulatory fines does not purport to excuse the indemnifying
  party from its own regulatory compliance obligations (indemnification allocates costs
  between parties; it does not transfer regulatory responsibility to the regulator)

---

#### Dimension 9: Survival Periods

**What to assess:**

Survival provisions determine how long indemnification obligations survive the termination
or expiration of the contract. Without survival language, indemnification obligations may
expire when the contract ends — before claims are discovered or filed.

**Survival framework by claim type:**

| Claim Type | Typical Survival Period | Rationale |
|-----------|------------------------|-----------|
| **General reps and warranties (M&A)** | 12–24 months post-closing | Discovery period for ordinary business representations |
| **Fundamental reps (M&A)** | Indefinite / statute of limitations | Organization existence, authority, title, capitalization — no reason to cut off |
| **Tax representations (M&A)** | Statute of limitations + 60–90 days | Tax authority assessment periods |
| **IP infringement claims** | Term of the license / service agreement | IP claims arise during use |
| **Data protection claims** | 3–5 years (or applicable regulatory limitation period) | GDPR limitation periods; regulatory investigation timelines |
| **Fraud / intentional misconduct** | Indefinite (no cut-off) | Public policy prevents a party from contracting out of fraud liability with time limits |
| **General indemnification (commercial contracts)** | 12–36 months post-termination | Aligned with limitation of actions in applicable jurisdiction |
| **Environmental / property damage** | Long survival (10+ years) | Latent damage discovery |

[JURISDICTION-SPECIFIC] Survival periods interact with statutes of limitations:
- **US**: Limitation periods vary by state and claim type (contract: 4–6 years in most
  states; warranty: UCC 4 years for goods; longer for fraud) [VERIFY per state]
- **England/Wales**: 6 years for simple contract claims; 12 years for claims under deed;
  fraud: time runs from discovery (Limitation Act 1980) [VERIFY current application]
- **Australia**: 6 years in most states for contract claims; may be extended for latent
  damage [VERIFY: Limitation Act per state]

**Assessment criteria:**
- [ ] Survival provision expressly states which obligations survive and for how long
- [ ] General indemnification obligations have a stated survival period
- [ ] IP indemnification survives at least for the term of the agreement
- [ ] Data protection indemnification survives for the regulatory investigation period
- [ ] Fraud and intentional misconduct indemnification survive indefinitely (or for the
  statutory limitation period with discovery-based extension)
- [ ] Fundamental representations (M&A) survive indefinitely
- [ ] Survival clause is not shorter than the applicable statute of limitations for the
  most material claim types

---

#### Dimension 10: Interaction with Limitation of Liability

**What to assess:**

This dimension examines the relationship between the indemnification clause and the
limitation of liability clause — the most common source of contractual conflict and
litigation in commercial disputes.

**Key interaction patterns:**

| Pattern | Description | Risk |
|---------|-------------|------|
| **Indemnification inside the cap** | LOL clause applies to indemnification obligations; total recovery capped | Indemnitee may be left with uncovered losses if cap is inadequate |
| **Indemnification outside the cap** | "Notwithstanding any other provision" language carves out indemnification from LOL cap | Indemnifying party faces potentially unlimited liability |
| **Super-cap for indemnification** | Indemnification subject to a separate higher cap | Balances the two extremes; increasingly standard |
| **Silent on interaction** | Neither clause addresses the other | Highest litigation risk — courts must interpret which governs; outcome varies by jurisdiction |
| **LOL clause governs "any liability"** | Broad LOL cap language may inadvertently capture indemnification obligations | The "notwithstanding" carve-out for indemnification may be needed in the LOL clause |

**Critical language patterns:**

- **"Notwithstanding the foregoing"** in LOL clause: carves out indemnification from cap
- **"Subject to Section X" (LOL clause)** in indemnification clause: puts indemnification
  inside the LOL cap
- **Silent**: Both clauses exist without cross-reference — ambiguous and litigation-prone
- **"For the avoidance of doubt, the indemnification obligations...are subject to the
  limitation of liability in Section X"**: explicit inclusion inside cap

**Assessment criteria:**
- [ ] The relationship between indemnification and the LOL cap is expressly stated
- [ ] IP indemnification is clearly stated to be outside the general LOL cap (or inside
  with a super-cap)
- [ ] Data breach indemnification is clearly stated to be outside the general LOL cap
  (or inside with a super-cap)
- [ ] The LOL clause expressly carves out fraud and willful misconduct indemnification
  from any cap (or these are never subject to a cap)
- [ ] There are no directly conflicting provisions between the indemnification clause
  and the LOL clause
- [ ] The LOL's consequential damages exclusion does not inadvertently sweep in
  legitimate indemnification recoveries

---

### Step 7: Classify

After completing all 10 dimensions, assign an overall classification:

#### GREEN — Acceptable

**All** of the following must be true:

- [ ] Indemnification scope (first-party / third-party) is clear and appropriate for the
  contract type
- [ ] Defense obligation (or equivalent English/AU mechanism) is expressly stated
- [ ] Settlement consent protection is present at reasonable standard ("not unreasonably
  withheld")
- [ ] IP indemnification is present (for technology contracts) and carved out from the cap
- [ ] Data protection indemnification is present and carved out from the cap (or subject
  to appropriate super-cap)
- [ ] Confidentiality breach is covered by indemnification or express remedy
- [ ] Fraud indemnification is uncapped (or no cap purports to apply to fraud)
- [ ] Survival periods are appropriate for the claim types covered
- [ ] LOL interaction is expressly stated (indemnification inside or outside the cap)
- [ ] No mandatory statutory provision is violated (anti-indemnity statutes, proportionate
  liability schemes)
- [ ] Indemnification structure is mutual OR asymmetry is commercially justified

**Confidence required**: HIGH (0.80+)

**Routing**: Accept with awareness; no escalation required.

#### YELLOW — Negotiate

**One or more** of the following are present, but the indemnification structure is not
fundamentally unacceptable:

- Defense obligation is present but ambiguous (indemnify but defense mechanics incomplete)
- IP indemnification is present but carve-outs are overly broad (e.g., any combination
  with any third-party product — not just unauthorized combinations)
- Data breach indemnification is inside the general cap without a super-cap
- Survival periods are shorter than recommended but not critically inadequate
- LOL interaction is unclear (silent rather than conflicting)
- Basket/cap in M&A context is unfavorable but within negotiable range
- Materiality scrape is absent or only a single scrape (no double scrape) in M&A context
- Settlement consent is "sole discretion" rather than "not unreasonably withheld"
- Regulatory claims indemnification is present but scope is ambiguous
- One category of required indemnification (e.g., confidentiality breach) is missing but
  covered indirectly through another clause

**Confidence required**: PROBABLE (0.60+). If confidence below 0.60, escalate to YELLOW
regardless.

**Routing**: Negotiate with proposed redlines. Flag specific issues. Target resolution in
1–2 negotiation rounds.

#### RED — Escalate

**One or more** of the following are present:

- **No indemnification clause at all** in a commercial agreement where third-party claims
  are a realistic risk (technology, services, data processing, construction)
- **No defense obligation** and no mechanism for the indemnifying party to participate in
  defending claims — the indemnitee bears all defense costs with no right of recovery
- **Scope purports to cover indemnifying party's own fraud or gross negligence without
  limitation** (may be void in some jurisdictions; creates perverse incentive)
- **IP indemnification is absent** from a technology or SaaS agreement (vendor takes no
  responsibility for its own product's IP risk)
- **IP indemnification is inside the general LOL cap** at a level that is inadequate to
  cover realistic IP litigation costs (e.g., 1 month's fees for a $5M software deployment)
- **Anti-indemnity statute violation** — the clause purports to indemnify a party for its
  own sole negligence in a construction contract governed by a state with an anti-indemnity
  statute [JURISDICTION-SPECIFIC: verify applicable state]
- **Proportionate liability conflict** — the clause purports to make one party liable for
  the full loss in a jurisdiction where proportionate liability cannot be contracted out
  (e.g., Queensland) [JURISDICTION-SPECIFIC]
- **No survival provision** and the contract term is short (indemnification obligations
  may expire before claims are discovered or filed)
- **Uncapped first-party indemnification** for broad categories (e.g., "any losses"
  without qualification) — the indemnifying party faces unlimited exposure for losses
  the other party suffers from its own business operations
- **Fraud indemnification is expressly capped** — this is unenforceable as a matter of
  public policy in US/UK/AU and signals a fundamentally unacceptable approach
- **Settlement consent requires sole discretion** with no "prejudice" or "admission"
  protection for the indemnitee — the indemnitee can be forced into settlements it cannot
  dispute regardless of how harmful the terms

**Confidence required**: HIGH (0.80+). If confidence below 0.80, classify as YELLOW and
flag for counsel review. Never escalate speculatively.

**Routing**: Do not execute without legal review. Full counsel assessment required.
Significant negotiation or redraft necessary. Escalate to senior counsel.

---

### Step 8: Generate Redlines

For each YELLOW and RED finding, generate a redline with fallback position.

**Format for each redline:**

```
Dimension: [Dimension number and name]
Classification: YELLOW / RED
Finding: [What the clause currently says and why it is problematic]
Legal Basis: [Specific statute, case, or market standard — VERIFIED or UNVERIFIED]
Business Impact: [What this means in practical, commercial terms]
Exposure Estimate: [Quantify where possible — e.g., "IP litigation defense costs average
  $1M–$3M per case [VERIFY]; the current cap of $50K covers <5% of realistic exposure"]
Confidence: [Definite / High / Probable / Possible / Unlikely]

Proposed language: [Specific redline — add / delete / replace]
Fallback position: [Compromise language if proposed language is rejected]
Negotiation note: [Why this matters; how to frame the ask to the counterparty]
```

**Standard Redline Library:**

**Defense Obligation — Missing (Add):**
```
Proposed: "Indemnifying Party shall, at its own expense, defend Indemnitee against any
Third-Party Claim covered by the indemnification obligations in this Section, using counsel
reasonably acceptable to Indemnitee. Indemnifying Party shall pay all costs, fees, and
expenses of such defense. Indemnitee shall: (a) promptly notify Indemnifying Party in
writing of any such claim (provided that failure to provide timely notice shall not relieve
Indemnifying Party of its obligations except to the extent Indemnifying Party is materially
prejudiced by such failure); (b) grant Indemnifying Party sole control of the defense and
settlement of the claim; and (c) provide reasonable cooperation and assistance. Indemnifying
Party shall not settle any claim without Indemnitee's prior written consent (not to be
unreasonably withheld, conditioned, or delayed), provided that Indemnitee's consent shall
not be required for any settlement that does not impose any obligation, restriction, or
liability on Indemnitee."

Fallback: Maintain defense obligation with sole discretion consent — at minimum, require
that no admission of liability is made and no obligation imposed on Indemnitee without consent.
```

**IP Indemnification — Carve-Out from LOL Cap (Add "Notwithstanding"):**
```
Proposed: "Notwithstanding any other provision of this Agreement, including any limitation
of liability provisions, the Indemnifying Party's obligations under this Section [IP
Indemnification] shall not be subject to any limitation of liability cap set forth in this
Agreement. [Alternative: shall be subject to a separate aggregate cap of [2× / 3×] the
amount paid or payable by Customer in the 12 months preceding the event.]"

Fallback: Super-cap at 2× annual contract value (minimum meaningful elevation above
the standard cap).
```

**IP Indemnification Remedy Waterfall — Add:**
```
Proposed: "If any Product or Service is, or in Vendor's reasonable opinion is likely to
become, the subject of an infringement claim, Vendor shall, at its own expense and sole
option: (a) procure for Customer the right to continue using such Product or Service;
(b) modify the Product or Service so that it no longer infringes; (c) replace the Product
or Service with a non-infringing equivalent; or (d) if none of the foregoing is commercially
practicable, terminate the relevant license or service and refund any prepaid fees for
periods after the termination date."

Fallback: Retain remedy waterfall; remove option (d) as a self-executing right and require
mutual agreement on termination as last resort.
```

**Survival Period — Extend to Cover Regulatory Investigation Period:**
```
Proposed: "The indemnification obligations in this Section shall survive termination or
expiration of this Agreement for a period of [3 / 5] years, except that obligations relating
to (a) fraud or willful misconduct shall survive indefinitely, (b) data protection violations
shall survive for 5 years following the incident giving rise to the obligation [or for the
applicable regulatory limitation period, whichever is longer], and (c) intellectual property
claims shall survive for the term of the applicable intellectual property rights."

Fallback: 2-year general survival + indefinite survival for fraud.
```

**Tipping Basket — Clarify Mechanism (M&A):**
```
Proposed: "Indemnitor shall not be required to make any payment pursuant to this Article [X]
until the aggregate amount of all Losses for which indemnification is claimed under this
Agreement exceeds [__] (the 'Basket Amount'). Once such aggregate Losses exceed the Basket
Amount, Indemnitor shall be liable for all such Losses from the first dollar, including the
Basket Amount. The Basket Amount shall not apply to Losses arising from [fraud / Fundamental
Representations / Tax matters]."

Fallback: Convert tipping basket to deductible basket if tipping basket is not achievable
(reduces total recovery but avoids the "cliff" risk at the basket threshold).
```

---

### Step 9: Prioritize Findings

Assign each finding a negotiation tier:

**Tier 1 — Non-Negotiable (hold the line):**
- Missing defense obligation in a contract with material third-party claim exposure
- IP indemnification absent from technology contract
- Anti-indemnity statute violation (regulatory void risk)
- Proportionate liability scheme conflict (AU)
- Fraud indemnification capped
- Uncapped first-party indemnification for undefined "any losses"
- No survival provision on a contract covering data protection or IP obligations

**Tier 2 — Material (strong preference; trade for equivalent):**
- Defense obligation present but incomplete (no settlement consent protection)
- IP indemnification inside general cap at inadequate level
- Data breach indemnification inside general cap without super-cap
- Survival period shorter than applicable regulatory investigation period
- LOL interaction silent (not expressly stated)
- M&A basket type unfavorable (deductible vs. tipping) — depending on deal dynamics

**Tier 3 — Preferred (can concede with appropriate trade):**
- IP remedy waterfall absent (indemnity present but no mitigation mechanism)
- Minor basket amount optimization in M&A
- Settlement consent at "sole discretion" where deal allows for it
- Regulatory claims indemnification scope ambiguous but not completely absent
- Materiality scrape single rather than double (M&A)

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
considered? Are there other provisions in the contract that mitigate this risk? Does the
insurance clause, DPA, or another provision partially address the issue?

**Pass 3 — Challenge**: What is the strongest argument that this indemnification structure
IS acceptable? Under what deal dynamics might a reasonable practitioner accept this risk?
Is RED classification proportionate, or is this actually YELLOW with targeted redlines?

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

**Critical rule**: If overall confidence is below 0.60, escalate to counsel review regardless
of GREEN/YELLOW classification. Never GREEN-classify with sub-0.60 confidence.

---

## Glass Box Audit Trail

Every output MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-indemnification-analysis"
  contract_title: "[Contract title or 'Untitled']"
  contract_type: "[SaaS / M&A / Professional Services / Construction / Other]"
  user_side: "[Indemnitee / Indemnifying Party / Neutral]"
  governing_law: "[Jurisdiction identified from the contract or 'Not stated']"
  playbook_used: "[Playbook name / 'Market standards' / 'User-provided positions']"
  indemnification_structure: "[Mutual / Unilateral / Mixed]"
  defense_obligation: "[Present / Absent / Partial]"
  basket_type: "[Deductible / Tipping / Mini-basket / N/A]"
  basket_amount: "[Amount or 'Not applicable']"
  cap_structure: "[General cap / Super-cap / Uncapped / Mixed]"
  review_date: "[Date of review]"
  dimensions_assessed: 10
  dimension_summary:
    scope: "PASS / FLAG — [first-party / third-party / ambiguous]"
    baskets_caps: "PASS / FLAG — [brief note]"
    materiality_scrapes: "PASS / FLAG — [N/A for commercial / double / single / none for M&A]"
    defense_mechanics: "PASS / FLAG — [missing duty to defend / incomplete settlement control]"
    ip_indemnification: "PASS / FLAG — [absent / inside cap at inadequate level / appropriate]"
    data_protection: "PASS / FLAG — [inside cap without super-cap / appropriate]"
    confidentiality: "PASS / FLAG — [brief note]"
    regulatory_claims: "PASS / FLAG — [brief note]"
    survival_periods: "PASS / FLAG — [too short / appropriate for claim types]"
    lol_interaction: "PASS / FLAG — [silent / express inside cap / express outside cap]"
  overall_classification: "GREEN / YELLOW / RED"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "[Anti-indemnity statute — VERIFIED / UNVERIFIED]"
    - "[Proportionate liability scheme — VERIFIED / UNVERIFIED]"
    - "[UCTA 1977 — VERIFIED / UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  tier_1_issues: "[count]"
  tier_2_issues: "[count]"
  tier_3_issues: "[count]"
  anti_indemnity_statute_risk: "[Yes — statute identified / No / VERIFY]"
  proportionate_liability_risk: "[Yes — state identified / No / VERIFY]"
  limitations:
    - "[Scope limitations, missing provisions, assumptions]"
  reviewer: "AI-assisted — requires qualified legal review"
```

---

## Anti-Patterns

What NOT to do when reviewing or drafting indemnification clauses:

1. **Treating indemnification and damages for breach as equivalent** — An indemnity is a
   primary obligation under English law, potentially bypassing remoteness rules (Hadley v
   Baxendale [VERIFY]) and providing different limitations periods. Never advise that
   "indemnification is just a damages claim" — it may be considerably more powerful (or
   less, depending on drafting).

2. **Reviewing the indemnification clause in isolation from the LOL clause** — The most
   dangerous failure mode. If the LOL clause says "in no event shall either party be liable
   for more than $100K" and the indemnification clause says "Party A shall indemnify Party B
   for all losses," these provisions conflict. Always read them together. Failing to do so
   is the single most common reason indemnification provisions fail in practice.

3. **Ignoring the absence of a defense obligation** — "Indemnify" does not automatically
   mean "defend" under English or Australian law. A clause that indemnifies against losses
   but provides no defense mechanism leaves the indemnitee funding its own defense and
   seeking reimbursement later — if the indemnifying party is solvent when the claim
   resolves. This is materially worse than a true duty to defend.

4. **Accepting "sole negligence" exclusions without checking the governing jurisdiction** —
   In California, Texas, and other US states with anti-indemnity statutes, indemnification
   for the indemnitee's sole negligence is void as a matter of law in construction contracts.
   Advising that a clause is "market standard" without checking anti-indemnity exposure is
   a fundamental error.

5. **Failing to distinguish first-party from third-party scope** — An indemnity clause
   covering "any losses" without qualification may be read to cover first-party claims between
   the parties. This dramatically expands exposure for the indemnifying party and may bypass
   the limitation of liability clause entirely. Always flag ambiguous scope language.

6. **Missing the basket type distinction in M&A** — A tipping basket and a deductible basket
   are not interchangeable. On a $10M deal with a $75K basket, the tipping basket is worth
   up to $75K more to the buyer than a deductible basket (the basket amount itself is
   recoverable under a tipping structure). This is not a drafting nicety — it is a
   material economic point that lawyers sometimes overlook.

7. **Recommending uncapped IP indemnification without quantifying the exposure** —
   "Uncapped" IP indemnification is the historically market-standard recommendation, but
   IP litigation defense costs average $1M–$3M per claim [VERIFY]. For a small-value
   contract, recommending uncapped IP indemnity to a vendor can be commercially devastating
   if the customer's downstream use creates large IP exposure. Always size the exposure
   before recommending uncapped treatment.

8. **Ignoring Cumis counsel risk (US)** — Where an indemnifying party also provides
   (or funds) the defense and has a potential conflict of interest with the indemnitee in
   the underlying claim, independent counsel obligations may arise in California and some
   other states. This is particularly relevant where the indemnifying party's conduct is
   partly at issue and it has an interest in minimizing its own exposure in the third-party
   proceeding. [JURISDICTION-SPECIFIC]

9. **Treating proportionate liability as overridable everywhere in Australia** — Queensland's
   Civil Liability Act 2003 (Qld) may prevent parties from contracting out of proportionate
   liability for property damage and economic loss claims. An indemnification clause that
   allocates 100% of loss to one party may not be enforceable for these claim types in
   Queensland. Do not advise that Australian indemnification clauses automatically override
   proportionate liability without checking the applicable state scheme. [VERIFY current Qld
   and state-by-state positions]

10. **Using "including" in an indemnification trigger without "but not limited to"** —
    Courts have held that "including" without "but not limited to" may be read as exhaustive
    of the categories listed. Where the parties intend the list to be illustrative, not
    exhaustive, add "including without limitation" or "including but not limited to."

11. **Allowing the surviving party (post-termination) to trigger new indemnification claims
    indefinitely** — If the indemnification clause does not have a survival cut-off, the
    indemnitee can theoretically claim indemnification years after the contract ends. Unlimited
    survival is commercially irrational for the indemnifying party (and often not the
    actual intent of either party). Always include express survival periods.

12. **Missing the "no settlement without consent" protection** — An indemnification clause
    that grants the indemnifying party full control of defense and settlement without
    requiring the indemnitee's consent can result in the indemnitee being bound by an
    adverse settlement (admissions of liability, injunctions against future business conduct)
    that the indemnifying party agreed to because it minimized the indemnifying party's
    cost. Always require consent for settlement terms that impose obligations on the
    indemnitee.

13. **Failing to address subrogation** — When an insurer pays an indemnification claim, it
    may be subrogated to the indemnitee's right to recover from the indemnifying party.
    This can create unexpected triple-sided disputes. Where the contract involves insurance
    requirements, address subrogation and waiver of subrogation rights.

14. **Accepting "promptly notify" without specifying a time period** — "Promptly" is
    litigated constantly. Specify a number of days (e.g., 10 business days) for the notice
    obligation. Failure to give timely notice in some jurisdictions may reduce or eliminate
    indemnification recovery if the indemnifying party can show prejudice.

15. **Reading "defend, indemnify, and hold harmless" as redundant** — Each word has distinct
    meaning under US common law: "defend" creates the immediate defense obligation; "indemnify"
    creates the ultimate obligation to pay; "hold harmless" is sometimes interpreted as a
    waiver of any contribution claim the indemnifying party might have against the indemnitee
    for the underlying loss. Do not advise that these are interchangeable or that one can be
    omitted without consequence.

16. **Ignoring the insurance clause interaction** — The indemnification obligation and the
    insurance clause are the two sides of the risk transfer mechanism. If the contract requires
    the indemnifying party to maintain $5M of professional indemnity insurance but the
    indemnification obligation is uncapped, the first $5M may be covered but the excess is
    bare exposure. Always cross-check indemnification scope against insurance requirements.

17. **Overlooking contribution and contribution bar provisions** — In multi-party transactions,
    a "contribution bar" prevents a settling party from being subject to contribution claims
    from non-settling parties. If the indemnification clause does not address this, a party
    who settles one claim may still face contribution actions from others for the same
    underlying event.

18. **Missing the regulatory vs. contractual distinction in data protection** — GDPR
    regulatory fines are imposed by supervisory authorities and cannot be contractually
    redirected. The indemnification clause allocates the economic burden between the
    contracting parties AFTER the regulator collects the fine from the responsible entity.
    Advising that "the indemnification clause means the processor pays the fine" is incorrect —
    the regulator collects from whoever it finds responsible; the indemnification clause
    determines who reimburses whom between the commercial parties. [VERIFY current GDPR
    Art. 82 case law]

19. **Accepting a "reasonable" legal fees standard without defining it** — Where the
    indemnification covers legal fees and costs, "reasonable" is contestable. Consider
    specifying: the rate basis (e.g., standard rate billing, not premium rates), the
    approval process for incurring significant legal costs, and whether fees include
    counsel for the indemnitee's own advisors or only external defense counsel.

20. **Drafting indemnification without considering the full risk allocation ecosystem** —
    Indemnification is one component of a risk transfer system that includes limitation of
    liability, insurance, representations and warranties, force majeure, and termination
    rights. A perfectly drafted indemnification clause can still create irrational overall
    risk allocation when considered with the rest of the contract. Always close the analysis
    with a holistic assessment of the complete risk allocation picture.

---

## Writing Standards

### For Redline Rationales (shared with counterparty)

- **Plain language.** "This clause requires you to fund the defense of any claim — even
  frivolous ones — before the court has made any finding" — not "this provision imposes an
  obligation to defend all covered proceedings irrespective of adjudication."
- **Active voice.** "Vendor must defend Customer against any IP claim" — not "Customer shall
  be defended against IP claims."
- **Name the actor.** "Vendor's defense obligation applies when..." — not "the defense
  obligation applies when..."
- **Quantify the exposure.** "IP litigation defense costs average $1M–$3M per case; the
  current indemnification cap of $50K provides less than 5% coverage" — not "the cap is
  insufficient."
- **Specific, not vague.** Reference the clause number and the specific language that is
  problematic. Do not reference the "general indemnification structure."

### For Internal Analysis

- Same plain-language standards; may include more legal detail
- Confidence qualifiers wherever appropriate
- [VERIFY] and [UNVERIFIED] markers on all statutory/case law references not confirmed
- Glass Box audit trail appended before delivery

### Quality Gates Before Delivery

1. Can a non-lawyer business stakeholder understand the executive summary?
2. Is every identified gap accompanied by a specific proposed resolution?
3. Is every legal claim backed by a specific citation or flagged [VERIFY]?
4. Is the overall classification supported by HIGH (0.80+) confidence?
5. Are RED items supported by the self-interrogation 3-pass review?
6. Has the LOL clause been reviewed alongside the indemnification clause? (If not, flag
   this as a limitation in the Glass Box.)

---

## External Tool Integration

### With legalcode-mcp (preferred)

Use legalcode-mcp in Step 4 to:
- Retrieve current anti-indemnity statute text per applicable US state
- Retrieve current proportionate liability scheme provisions per applicable Australian state
- Retrieve current UCTA 1977 / Consumer Rights Act 2015 indemnification case law (UK)
- Retrieve current ABA Deal Points Study data on M&A basket and cap market standards
- Retrieve current GDPR Art. 82 case law on data protection indemnification
- Retrieve recent IP infringement litigation cost benchmarks for exposure sizing

Mark citations from legalcode-mcp searches as VERIFIED in the Glass Box.
Save research to: `/tmp/legalcode-indemnification-authority.md`

### Without legalcode-mcp

Proceed with jurisdiction-agnostic analysis using the enforceability framework in this
skill. Mark all statutory and case law references with [VERIFY].
Note in the Glass Box: `legalcode_mcp: "Not connected"`.
Focus the analysis on structural quality, defense mechanics, scope clarity, and survival
period adequacy rather than specific legal citation depth.

---

## Output Format Template

```markdown
# Indemnification Analysis — [Contract Title / Counterparty]

## Classification

**Overall: [GREEN / YELLOW / RED]** | Confidence: [level] | Basis: [playbook / market standards]

[1–2 sentence risk summary for non-legal stakeholders.]

## Route

[Approval authority / Counsel review / Senior escalation required]
[Expected action: accept / negotiate redlines / full redraft]

---

## Executive Summary

[3–5 bullet points covering the most important findings in priority order.
Plain language. Business-focused. Include exposure estimates where quantifiable.]

---

## Tier 1 Findings — Non-Negotiable

[For each Tier 1 finding:]

### [Dimension Name] — RED | Confidence: [level]

**Contract says**: [Exact or summarized language]
**Problem**: [Why this is unacceptable]
**Legal basis**: [Statute / case — VERIFIED or UNVERIFIED]
**Business impact**: [Practical consequence]
**Exposure estimate**: [Quantified where possible]
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

[Assessment of how the indemnification structure interacts with:
- Limitation of liability clause (inside / outside / super-cap)
- Insurance requirements
- Data protection addendum / DPA
- IP ownership provisions
- Regulatory compliance obligations
- Overall risk allocation balance between the parties]

---

## Jurisdiction-Specific Enforceability Notes

[For the identified governing law: flag any provisions that may be void or
subject to challenge — particularly anti-indemnity statutes (US), proportionate
liability (AU), UCTA (UK). Reference specific statutes and confidence level.]

---

## Negotiation Strategy

[Tier 1 must-haves, Tier 2 priorities, Tier 3 preferences. Sequencing guidance.
How to frame the ask to the counterparty. Trade-link suggestions.]

---

## Glass Box Audit Trail

[YAML block — see template above]
```

---

## Localization Notes

When applying this skill to a specific jurisdiction, replace [JURISDICTION-SPECIFIC] markers
with verified local content:

| Jurisdiction | Key Constraint | Critical Issue | Primary Authority |
|-------------|---------------|---------------|-------------------|
| US (general) | No anti-indemnity statute outside construction | First-party vs. third-party scope; Cumis counsel | State-by-state — verify |
| US (construction) | Anti-indemnity statutes in ~30 states | Sole negligence / partial negligence carve-outs | Cal. Civ. Code § 2782; Tex. Ins. Code § 151.102 [VERIFY] |
| England/Wales | No duty to defend; UCTA 1977 reasonableness | Contra proferentem; proportionate liability adjustment | Caledonia North Sea [2002] UKHL 4; UCTA 1977 [VERIFY] |
| Australia (Qld) | Civil Liability Act 2003 (Qld) — no contracting out | Proportionate liability cannot be re-apportioned by contract | Civil Liability Act 2003 (Qld) [VERIFY] |
| Australia (NSW) | Civil Liability Act 2002 (NSW) s.3A — contracting permitted | Parties may provide for their own rights | Civil Liability Act 2002 (NSW) [VERIFY] |
| Australia (Vic) | Position less clear | VERIFY current Victorian position | [VERIFY Victorian legislation] |
| EU / UK (GDPR) | Art. 82 — data subject compensation rights; Art. 82(5) recourse | Cannot limit data subject rights; allocation between parties permitted | GDPR Arts. 82, 83 [VERIFY current EDPB guidance] |

---

## Provenance

Created by Legalcode (2026-03-01). Original synthesis based on:
- Deep legal research on indemnification enforceability across US, UK, and Australian law
- Analysis of structural patterns from `legalcode-limitation-of-liability-review`,
  `legalcode-contract-review`, and `legalcode-master-services-agreement` reference skills
- Market standards from Norton Rose Fulbright Liability 101 guide (technology and
  outsourcing contracts), ABA Deal Points Study (M&A baskets and caps), SRS Acquiom
  Annual MA Deal Terms Study [VERIFY most recent editions], WorldCC / IACCM benchmarks
- Key legal authority: Caledonia North Sea [2002] UKHL 4; UCTA 1977; Civil Liability
  Act 2003 (Qld); Civil Liability Act 2002 (NSW); Cal. Civ. Code § 2782 (CA anti-indemnity);
  GDPR Art. 82; Hadley v Baxendale (1854)
- Legal topic research: knock-for-knock indemnity structures (energy/construction);
  proportionate liability schemes (Australia); Cumis counsel doctrine (California);
  M&A basket mechanics (deductible vs. tipping); IP indemnification remedy waterfalls
- Legalcode original synthesis — no imported third-party skill content

All statutory and case law references should be verified against authoritative sources
before use in legal advice contexts. Laws change; this skill reflects the state of
knowledge as of 2026-03-01.
