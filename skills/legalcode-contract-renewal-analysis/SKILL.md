---
name: legalcode-contract-renewal-analysis
description: Analyze contracts approaching renewal to detect auto-renewal traps, calculate termination
  window deadlines, identify evergreen clauses, flag price escalation triggers, and produce renewal decision
  checklists with timeline visualization and cost-benefit analysis. Use when reviewing a contract nearing
  expiration, evaluating whether to renew, renegotiate, rebid, or terminate, assessing auto-renewal risk,
  benchmarking renewal pricing, or preparing renewal negotiation strategy. Jurisdiction-agnostic with
  [JURISDICTION-SPECIFIC] markers. Supports playbook-based or general-standard analysis. Covers SaaS subscriptions,
  vendor agreements, services contracts, licenses, MSAs, and any commercial agreement with recurring or
  evergreen terms. Produces a structured renewal decision report with Glass Box audit trail and confidence
  scoring.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Contract Renewal Analysis

> **Disclaimer**: This skill provides a framework for AI-assisted contract renewal analysis.
> It does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before use. Laws change; verify current
> applicability before relying on any provision described here. Auto-renewal provisions,
> termination notice requirements, price escalation enforceability, and renewal rights vary
> materially across jurisdictions — verify jurisdiction-specific requirements against
> authoritative sources before finalizing any renewal decision. Statutory and case law
> references cited from memory carry hallucination risk — verify against authoritative
> sources before relying on them.

## Purpose and Scope

This skill analyzes contracts at or approaching renewal to identify risks, trapped renewal
terms, termination windows, financial exposures, and strategic alternatives — and recommends a
structured go/no-go decision with negotiation priorities.

**Covers:**

- Auto-renewal trap detection and notice period calculation
- Termination window analysis with safe send dates
- Price escalation trigger identification and cost impact modeling
- Evergreen clause detection (obligations surviving termination)
- Renewal condition assessment (performance, compliance, regulatory changes)
- Cost-benefit analysis: renewal vs. renegotiation vs. rebid vs. termination
- Renewal negotiation priorities organized by tier
- Timeline visualization with deadline urgency classification
- Quality-verified output with Glass Box audit trail and confidence scoring

**Does not:**

- Draft new contracts (see `legalcode-contract-review` and drafting-specific skills)
- Perform full clause-by-clause review of non-renewal terms (see `legalcode-contract-review`)
- Provide legal advice or replace qualified counsel
- Apply to one jurisdiction exclusively — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers
- Replace a vendor performance management process — this skill identifies performance gaps from
  contract data but does not conduct vendor audits

**Related skills:**

- `legalcode-contract-review` — full clause-by-clause deviation analysis
- `legalcode-obligation-tracker` — ongoing obligation monitoring and alert management
- `legalcode-contract-risk-scorer` — quantitative contract risk scoring
- `legalcode-contract-playbook-builder` — define renewal standards before contract intake

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. The contract's governing law clause determines which
legal framework applies. The renewal analysis identifies the governing law early and adapts
the analysis accordingly.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- **Auto-renewal notice requirements**: Several jurisdictions impose mandatory pre-renewal
  notice obligations on suppliers (particularly for consumer-facing contracts).
  - _United States (Federal)_: FTC Final Rule on Recurring Subscriptions and Negative Option
    Programs (effective May 14, 2025 [VERIFY]) — applies to negative option features including
    auto-renewal. Requires clear disclosure, affirmative consent, simple cancellation mechanisms,
    and annual reminders [VERIFY].
  - _United States (ROSCA)_: Restore Online Shoppers' Confidence Act (15 U.S.C. § 8403)
    prohibits charging in a subscription unless the charge terms are clearly disclosed, the
    consumer's billing information is obtained with express informed consent, and simple
    cancellation mechanisms are provided [VERIFY].
  - _California_: Business and Professions Code § 17600 et seq. (Automatic Renewal Law, or
    ARL), as amended effective July 1, 2025 by AB 2863 — requires clear and conspicuous
    disclosure, express affirmative consent, annual reminders, and click-to-cancel mechanisms
    for auto-renewing subscriptions (primarily B2C; check applicability to B2B [VERIFY]).
  - _New York_: N.Y. Gen. Oblig. Law § 5-903 — service provider must give 15-30 days' advance
    written notice before the opt-out window closes [VERIFY].
  - _22+ US states_: Have enacted statutory restrictions on automatic renewal provisions [VERIFY].
  - _European Union_: Directive 2005/29/EC on unfair commercial practices may restrict
    auto-renewal without clear disclosure for consumer-facing agreements [VERIFY].
  - _United Kingdom_: Consumer Contracts (Information, Cancellation and Additional Charges)
    Regulations 2013 may apply to consumer auto-renewals [VERIFY].

- **Enforceability of evergreen clauses**: Indefinite obligation survival clauses face scrutiny
  in some jurisdictions, particularly where they conflict with statutory limitation periods.

- **Price escalation enforceability**: Check whether inflation-linked (CPI/PPI) price escalation
  clauses are enforceable and whether price escalation caps are required or customary.

- **Termination rights**: Some jurisdictions impose minimum notice periods or prevent termination
  for convenience entirely in certain contract types (e.g., employment-adjacent contracts,
  exclusive distribution agreements).

[JURISDICTION-SPECIFIC] Always verify:

- Governing law clause in the contract
- Whether any mandatory statutory renewal, notice, or cancellation requirements override the
  contract's own terms
- Whether the contract involves a consumer party (triggering additional statutory protections)
- Whether the jurisdiction requires notice to be in a specific form (written, certified mail,
  registered email, etc.)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming the
user's intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- Multiple valid approaches exist and the user's preference matters
- Ambiguity in the contract creates a decision fork that only the user can resolve
- Renewal strategy requires business context that is not in the contract

Use the **⟁ CLARIFY** pattern (structured options with descriptions) wherever marked below. If
the user has already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept the Contract

Accept the contract in any of these formats:

- **File**: PDF, DOCX, or other document format
- **URL**: Link to a contract in a CLM, cloud storage, or document system
- **Pasted text**: Contract text pasted directly into the conversation
- **Portfolio mode**: Multiple contracts for batch renewal analysis

Also accept any supporting materials if provided:

- Amendments, addenda, or side letters
- Current pricing or invoices
- SLA performance reports or audit outputs
- Vendor correspondence about renewal terms
- Market benchmarking data

If no contract is provided, prompt the user to supply one.

### Step 2: Gather Renewal Context

**⟁ CLARIFY** — Before beginning the analysis, ask the user these questions. Present them as
structured options. Skip questions already answered in the initial prompt.

1. **Which side are you on?**
   - Options: Customer/Buyer (deciding whether to renew), Vendor/Supplier (managing renewal of
     customer relationship), Both (evaluating all perspectives), Neutral (legal/commercial review)
   - _Why this matters_: The analysis flips entirely. A customer wants exit flexibility and price
     protection. A vendor wants renewal commitment and revenue certainty. The same notice clause
     is favorable to one party and adverse to the other.

2. **How urgent is the renewal decision?**
   - Options: Critical — notice deadline is days away, Urgent — deadline is weeks away, Standard —
     1-3 months available, Planning — 3-12 months away, Portfolio review — no immediate deadline
   - _Why this matters_: Urgency determines how much can be renegotiated before the auto-renewal
     triggers. A notice deadline 5 days away may leave no room for negotiation at all.

3. **What is the strategic importance of this relationship?**
   - Options: Mission-critical (sole-source or deeply integrated — cannot be replaced quickly),
     High-value (important but alternatives exist with effort), Standard/commodity (easy to
     replace), New or uncertain relationship (no established trust or performance history)
   - _Why this matters_: Strategic importance determines how aggressively to negotiate. Fighting
     hard over renewal terms is appropriate for commodity vendors. For mission-critical vendors,
     preserving the relationship may outweigh winning every negotiation point.

4. **What is your primary concern about this renewal?**
   - Options: Auto-renewal trap (fear of being locked in without action), Price escalation (cost
     creep), Service gaps or SLA failures (poor performance), Evergreen obligations (undefined
     long-term exposure), Termination penalties (expensive to exit), Regulatory changes
     (compliance risk at renewal), Market shift (better alternatives now available), No specific
     concern — full analysis
   - Allow multiple selections.
   - _Why this matters_: Guides where to spend analysis depth. A time-pressed review should lead
     with the user's biggest concern.

5. **Do you have performance data?**
   - Options: Yes (full SLA reports, invoices, incident logs), Partial (some data available),
     No (relying on contract terms only), Ask at renewal (will gather data separately)
   - _Why this matters_: Cost-benefit analysis without performance data relies on assumptions.
     The analysis will mark all performance assessments with [DATA NEEDED] if performance data
     is absent.

6. **Renewal intent going in?**
   - Options: Leaning toward renewing (want confirmation and priorities), Undecided (need
     cost-benefit analysis), Leaning toward not renewing (want exit analysis), Have decided
     (just need to execute correctly)
   - _Why this matters_: Shapes whether the output emphasizes renewal negotiation or exit
     sequencing.

If the user provides partial context, proceed with reasonable assumptions and **state them
explicitly** (e.g., "Assuming you are on the customer side, leaning toward renewal, with
moderate urgency — let me know if that's wrong and I'll re-run the analysis"). Do not silently
assume.

### Step 3: Load the Renewal Playbook

Check for an organizational renewal playbook in local configuration (e.g., `legal.local.md`
or similar settings files).

A renewal playbook typically defines:

- **Notice window minimums**: How many days of non-renewal notice the organization requires before
  sending (e.g., "always allow 14 days for internal approval before the latest send date")
- **Price escalation limits**: Maximum acceptable annual price increase without escalation
  (e.g., "accept up to CPI + 2% without senior approval")
- **Renewal term limits**: Maximum acceptable auto-renewal term (e.g., "no auto-renewals for
  periods > 12 months")
- **Escalation triggers**: What constitutes a RED renewal issue requiring business decision-maker
  sign-off
- **Renewal decision timeline**: Lead time required for competitive alternatives assessment

**If no playbook is configured:**

**⟁ CLARIFY** — Inform the user that no playbook was found, and ask which approach to take:

- **Option A: Set up a renewal playbook now** — Walk through defining the organization's standard
  positions for renewal terms: acceptable price escalation ranges, maximum auto-renewal periods,
  minimum notice window requirements, renewal approval thresholds. Improves all future renewal
  analyses. Takes 10-15 minutes.
- **Option B: Proceed with general commercial standards** — Use widely-accepted market standards
  as the baseline (e.g., notice windows of 60-90 days, price escalation caps of CPI + 3%,
  auto-renewal periods of 12 months or less). Faster but the analysis may not reflect your
  organization's specific risk appetite.
- **Option C: Provide positions as we go** — Proceed with the analysis and the skill will ask
  when a playbook position matters for a specific clause.

Label the analysis accordingly: "Based on [playbook name] / General commercial standards —
not organizational positions."

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Read the contract's governing law clause. Then use **legalcode-mcp** (if connected) to build
a working legal reference file.

**Research priorities for renewal analysis:**

1. **Auto-renewal statutory requirements**: Does the governing jurisdiction impose mandatory
   disclosure, consent, or cancellation requirements on auto-renewal provisions?

2. **Notice enforceability rules**: Are there statutory minimum notice periods? Are certain
   notice methods (e.g., registered mail) required for effective notice?

3. **Evergreen clause enforceability**: Does the jurisdiction impose any limitations on
   indefinite obligation survival clauses?

4. **Price escalation rules**: Are there any price regulation or unfair terms doctrines that
   cap contractual price escalation?

5. **Termination rules**: Are there mandatory notice periods for termination that may exceed
   the contractual notice period? Are termination for convenience rights restricted for any
   contract type?

**⟁ CLARIFY** — If any of the following are true, ask before proceeding:

- **No governing law clause found**: Ask which jurisdiction the user expects to apply, and flag
  the absence as a governance gap.
- **Governing law differs from where contract is performed**: Note the potential conflict between
  governing law and mandatory local law at place of performance.
- **Multiple governing law provisions** (e.g., different schedules governed by different laws):
  Confirm which governs the renewal provisions.

Save the most relevant legal research results to a local temporary reference file
(`/tmp/legalcode-renewal-authority.md`). Reference this file throughout the analysis.

**If legalcode-mcp is not connected:**

- Mark all statutory references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus the analysis on commercial and contractual risk assessment rather than legal certainty
- Flag jurisdiction-specific auto-renewal laws for manual verification

### Step 5: Extract Renewal Metadata and Detect Auto-Renewal

Before analyzing individual clauses, extract the core renewal mechanics from the contract.
Read the entire contract — renewal provisions often appear in different sections (term in
Section 2, notice in Section 12, price adjustment in Schedule A, survival in the general
conditions).

**Extract the following for every contract:**

| Metadata Element             | Source Clause | Value                  | Confidence |
| ---------------------------- | ------------- | ---------------------- | ---------- |
| Effective Date               | [section]     | [date]                 | [level]    |
| Initial Term                 | [section]     | [duration or date]     | [level]    |
| Renewal Date (calculated)    | [formula]     | [YYYY-MM-DD]           | [level]    |
| Renewal Type                 | [section]     | [auto/manual/optional] | [level]    |
| Notice Window Opens          | [formula]     | [YYYY-MM-DD]           | [level]    |
| Latest Notice Send Date      | [formula]     | [YYYY-MM-DD]           | [level]    |
| Safe Send Date (with buffer) | [formula]     | [YYYY-MM-DD]           | [level]    |
| Days Until Safe Send Date    | [calculation] | [n]                    | —          |
| Renewal Term Duration        | [section]     | [duration]             | [level]    |
| Price Escalation Trigger     | [section]     | [mechanism]            | [level]    |
| Evergreen Clauses Found      | [sections]    | [count]                | [level]    |
| Termination for Convenience  | [section]     | [yes/no/conditions]    | [level]    |
| Governing Law                | [section]     | [jurisdiction]         | [level]    |

**Date Calculation Formulas:**

```
Renewal_Date = Effective_Date + Initial_Term
  (or the specific fixed date stated in the contract)

Notice_Window_Opens = Renewal_Date - Earliest_Notice_Days
  (where Earliest_Notice_Days is the maximum advance notice allowed, if stated)

Notice_Window_Closes = Renewal_Date - Latest_Notice_Days
  (where Latest_Notice_Days is the minimum advance notice required)

Safe_Send_Date = Notice_Window_Closes - Internal_Approval_Buffer
  (default Internal_Approval_Buffer = 10 business days unless playbook specifies otherwise)

Days_Until_Safe_Send = Today - Safe_Send_Date
  (negative = past deadline; 0-7 = CRITICAL; 7-14 = RED; 14-30 = YELLOW; >30 = GREEN)
```

**Auto-Renewal Detection Checklist:**

Scan the contract for these language patterns. Each triggers specific analysis:

| Language Pattern                                                      | Meaning                                   | Risk Level                               |
| --------------------------------------------------------------------- | ----------------------------------------- | ---------------------------------------- |
| "automatically renews unless notice given"                            | Classic auto-renewal                      | Moderate — check notice window           |
| "continues for successive periods of [X] unless terminated"           | Evergreen rollover                        | Moderate-High — check period length      |
| "shall be renewed for [X] period upon [Y] days notice of non-renewal" | Auto-renewal with notice requirement      | Moderate — notice window is key          |
| "renews at Vendor's then-current list price"                          | Auto-renewal at market rate               | High — price unpredictability            |
| "renews by mutual written agreement"                                  | No auto-renewal — active consent required | Low — but track deadline                 |
| "continues in full force and effect" without termination trigger      | Evergreen — no automatic renewal term     | CRITICAL — must trace termination rights |
| "either party may terminate upon [X] days notice"                     | Termination right (not renewal clause)    | Low — but counts as renewal flexibility  |
| "subject to renewal at mutually agreed terms"                         | Open renewal negotiation                  | Moderate — "to be agreed" risk           |
| "renews for additional [X] year period"                               | Fixed-term rollover                       | Moderate-High if term is long            |

**⟁ CLARIFY** — If auto-renewal status is ambiguous (e.g., contract is silent on what happens
at expiration, or multiple clauses conflict), ask the user:

- "The contract is unclear about what happens at expiration — can you confirm the intended
  renewal mechanism? Options: (a) I believe it auto-renews, (b) I believe it terminates, (c)
  I'm not sure — analyze both scenarios."

### Step 6: Perform Termination Window and Timeline Analysis

Calculate all renewal-related deadlines and present them as a timeline visualization.

**Critical Timeline Table:**

```
CONTRACT RENEWAL TIMELINE — [Contract Name]
─────────────────────────────────────────────────────────────────
Date           Event                          Status      Action
─────────────────────────────────────────────────────────────────
[YYYY-MM-DD]   Contract Effective Date        Historical  —
[YYYY-MM-DD]   Notice Window Opens            [status]    [action]
[YYYY-MM-DD]   Safe Send Date (internal)      [status]    [action]
[YYYY-MM-DD]   Latest Notice Send Date        [status]    [action]
[YYYY-MM-DD]   Renewal / Termination Date     [status]    [action]
[YYYY-MM-DD]   Post-Renewal Period Begins     [status]    [action]
─────────────────────────────────────────────────────────────────
TODAY IS: [today's date]   DAYS TO SAFE SEND DATE: [n] [STATUS]
─────────────────────────────────────────────────────────────────
```

**Deadline Urgency Classification:**

| Status                   | Days to Safe Send Date     | Required Action                                                                      |
| ------------------------ | -------------------------- | ------------------------------------------------------------------------------------ |
| **GREEN — Plan**         | > 60 days                  | Calendar reminder set; begin renewal analysis                                        |
| **YELLOW — Monitor**     | 30-60 days                 | Begin renewal analysis; prepare decision brief                                       |
| **ORANGE — Act**         | 14-30 days                 | Complete analysis immediately; escalate to decision-maker                            |
| **RED — Urgent**         | 7-14 days                  | Emergency review; expedite internal approval; brief senior stakeholder               |
| **CRITICAL — Emergency** | 0-7 days                   | Immediate action required; brief executive; send notice or waiver immediately        |
| **PAST DEADLINE**        | Negative (deadline missed) | Assess whether auto-renewal has triggered; explore cure options; escalate to counsel |

**Notice Effectiveness Requirements:**

Extract and verify from the contract:

- [ ] Required form of notice (email, certified mail, in-person delivery, CLM platform)
- [ ] Required recipient (specific person, role, address, email)
- [ ] Required content elements (e.g., contract number, effective date, party name)
- [ ] Deemed receipt rules (e.g., "notice effective 2 days after certified mail dispatch")
- [ ] Whether electronic notice is valid

[JURISDICTION-SPECIFIC] In some jurisdictions, notice requirements are stricter than the
contract states. For example, New York law may require notices sent to specific addresses per
N.Y. Gen. Oblig. Law § 5-903 [VERIFY]. Verify that the contract's notice mechanism is
sufficient under applicable law.

**⟁ CLARIFY** — If the notice recipient address appears stale (e.g., references a person who
has left, or an address that has changed), ask the user whether they have current contact
information for the counterparty's notice recipient. A notice sent to an incorrect address
may be legally ineffective.

### Step 7: Analyze Price Escalation and Financial Impact

Identify all price escalation mechanisms in the contract and model their financial impact
over the renewal term.

**Price Escalation Catalog:**

For each escalation mechanism found, document:

```
Escalation Trigger: [Section X — exact clause quote]
Type: [CPI-linked / PPI-linked / Fixed % / Vendor discretion / "to be agreed" / None]
Index Referenced: [CPI-U / CPI-W / All-items / Core / PPI-specific index]
Cap Applied: [Yes — X% maximum / No cap / "Whichever is lower: CPI or X%"]
Floor Applied: [Yes — X% minimum / No floor]
Calculation Period: [Annual / On renewal / On X anniversary]
Applies To: [All fees / License fees only / Support fees only / [specific fee types]]
```

**Financial Impact Modeling:**

For each active escalation mechanism, calculate:

| Year                | Current Rate | Escalation Formula | Projected Rate | YoY Change | Cumulative Change |
| ------------------- | ------------ | ------------------ | -------------- | ---------- | ----------------- |
| Year 1 (current)    | $[X]         | Baseline           | $[X]           | —          | —                 |
| Year 2 (renewal Y1) | $[X]         | +[formula]         | $[Y]           | +[%]       | +[%]              |
| Year 3 (renewal Y2) | $[X]         | +[formula]         | $[Z]           | +[%]       | +[%]              |
| [etc.]              |              |                    |                |            |                   |

**Note on compound escalation**: A 3% annual escalation is NOT a 15% total increase over 5
years. It is 15.93%. Always calculate compound interest, not simple interest.

**Price Escalation Severity Classification:**

| Annual Escalation                              | Classification | Action                                     |
| ---------------------------------------------- | -------------- | ------------------------------------------ |
| 0-CPI                                          | GREEN          | Acceptable — below inflation               |
| CPI to CPI+2%                                  | GREEN          | Acceptable — market standard               |
| CPI+2% to CPI+5%                               | YELLOW         | Negotiate cap or index change              |
| > CPI+5% or no cap                             | RED            | Escalate — negotiate cap or consider rebid |
| "Vendor's then-current list price" (unlimited) | RED            | Escalate — high unpredictability           |
| "To be agreed" (open-ended)                    | RED            | Escalate — renewal pricing is not defined  |

**Benchmarking:**

[JURISDICTION-SPECIFIC] Market rate benchmarking data varies by industry, contract type, and
region. Where market data is available:

- Compare current renewal rate to market average for comparable services
- Identify whether renewal pricing is competitive, at market, or above market
- Use benchmarking to support negotiation redlines (e.g., "comparable providers offer this
  at 12% below your quoted renewal rate — market standard is CPI + 2%")

If no benchmarking data is available, flag as: `[BENCHMARKING DATA NEEDED — obtain market
comparables before finalizing renewal decision]`

### Step 8: Identify and Assess Evergreen Clauses

Scan the contract for obligations that survive termination or renewal and create ongoing
exposure.

**Evergreen Clause Categories:**

| Clause Type               | Common Survival Language                                         | Typical Duration       | Risk Level                       |
| ------------------------- | ---------------------------------------------------------------- | ---------------------- | -------------------------------- |
| **IP ownership**          | "IP ownership survives termination"                              | Perpetual              | MEDIUM — standard if defined     |
| **Confidentiality**       | "Confidentiality obligations survive for X years / indefinitely" | 2-5 years or perpetual | MEDIUM — check duration          |
| **Indemnification**       | "Indemnification obligations survive expiration"                 | Perpetual typically    | MEDIUM-HIGH — check scope        |
| **Warranty claims**       | "Warranty claims survive for X years after delivery"             | Typically 1-3 years    | LOW-MEDIUM                       |
| **Governing law/dispute** | "Dispute resolution survives"                                    | Perpetual              | LOW                              |
| **Non-solicitation**      | "Non-solicitation survives for X period"                         | 6-24 months            | YELLOW if broad                  |
| **Non-compete**           | "Non-compete survives for X period"                              | Varies                 | RED if broad; check jurisdiction |
| **Data return/deletion**  | "Vendor must return/delete data within X days of termination"    | Time-bound obligation  | HIGH — must track and enforce    |
| **Payment obligations**   | "All outstanding payments survive termination"                   | Until settled          | MEDIUM                           |
| **Reporting obligations** | "Annual reporting survives for X years"                          | X years                | LOW                              |
| **Audit rights**          | "Audit rights survive for X years"                               | X years                | MEDIUM — track and exercise      |

**Evergreen Clause Output:**

For each evergreen clause identified:

```
**Evergreen Clause**: [Section X — clause type]
**Contract says**: "[exact quote]"
**Duration**: [perpetual / X years / until [event]]
**Scope**: [what obligations are covered]
**Risk**: [GREEN / YELLOW / RED] — [brief rationale]
**Action**: [track deadline / negotiate reduction / negotiate sunset / no action needed]
```

**Dangerous Evergreen Patterns (flag as RED):**

1. **Uncapped perpetual indemnity** surviving termination — exposure may increase post-renewal
2. **No data return/deletion obligation** — data continues to be held by vendor with no
   contractual requirement for secure disposal
3. **Non-compete with no geographic or temporal limit** — may prevent post-termination
   competition with no clear scope
4. **"All terms survive termination" boilerplate** — this is often overreaching; check whether
   confidentiality, IP, or liability terms are effectively made perpetual by this catch-all

### Step 9: Perform Renewal Decision Analysis

Synthesize all findings from Steps 5-8 into a structured renewal decision framework.

**⟁ CLARIFY** — Before finalizing the renewal recommendation, ask if needed:

- "Based on the analysis so far, the renewal looks [favorable / unfavorable / mixed]. Would
  you like me to weight the cost-benefit analysis toward (a) pure financial comparison, (b)
  strategic continuity, or (c) risk minimization? Or let me present all three and you decide."

**Renewal Decision Options:**

| Option                                               | Description                                                                                                              | When Appropriate                                                     |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| **PROCEED** — Renew at current or similar terms      | Contract is performing well, pricing is market-rate, terms are acceptable, relationship is strategic                     | Good performance + competitive pricing + acceptable terms            |
| **RENEGOTIATE** — Renew with material changes        | Relationship is valuable but terms or pricing require adjustment                                                         | Good performance + above-market pricing or problematic terms         |
| **REBID** — Competitive alternatives assessment      | Market alternatives are likely better; performance is acceptable but pricing is above market                             | Commodity vendor + above-market pricing + adequate alternatives      |
| **TERMINATE** — Do not renew                         | Performance has materially failed, pricing is non-competitive, relationship is adversarial, or better alternatives exist | Material breach history + above-market pricing + viable alternatives |
| **CONVERT** — Month-to-month or short-term extension | Strategic uncertainty; not ready to commit to full renewal; need time to assess alternatives                             | Transition period needed; no urgency to lock in long-term            |

**Renewal Decision Scoring Model:**

Apply this weighted scoring to generate a structured recommendation:

```
RenewalScore = (0.35 × CostBenefitScore)
             + (0.25 × VendorPerformanceScore)
             + (0.20 × StrategicImportanceScore)
             + (0.10 × NegotiationFeasibilityScore)
             + (0.10 × ContractRiskScore)

CostBenefitScore (0-100):
  Start at 50 (neutral)
  + 20 if renewal pricing is at or below market benchmark
  + 15 if single-year term (flexibility premium)
  - 20 if renewal pricing is > 15% above market
  - 15 if multi-year commitment required (lock-in penalty)
  + 10 if price escalation cap ≤ CPI+2%
  - 10 if no price escalation cap (or "then-current list price")

VendorPerformanceScore (0-100):
  Start at 50 (neutral / no data)
  + 40 if all SLAs met with no material breaches
  + 20 if most SLAs met with only minor issues
  0 if performance data unavailable (stay at 50 with [DATA NEEDED] flag)
  - 20 if material SLA failures documented
  - 40 if repeated material SLA failures or breach history

StrategicImportanceScore (0-100):
  Mission-critical (sole source): 90
  High-value (alternatives exist with significant effort): 70
  Standard/commodity: 40
  Easy to replace: 20

NegotiationFeasibilityScore (0-100):
  Strong buyer leverage (many alternatives): 80
  Moderate leverage: 55
  Vendor has leverage (sole source / unique product): 30
  + 20 if > 45 days remain in notice window
  - 20 if < 14 days remain in notice window

ContractRiskScore (0-100):
  Start at 50 (neutral)
  - 30 if uncapped indemnity or liability exposures
  - 20 if evergreen clauses with unlimited duration found
  - 15 if no termination for convenience post-renewal
  + 20 if favorable risk allocation confirmed
  + 10 if strong exit protections (T4C, data return, transition assistance)
```

**RenewalScore → Recommendation Mapping:**

| Score  | Recommendation  | Rationale                                                            |
| ------ | --------------- | -------------------------------------------------------------------- |
| 70-100 | **PROCEED**     | Strong case for renewal — cost, performance, and risk all acceptable |
| 50-69  | **RENEGOTIATE** | Renewal advisable but significant improvements needed                |
| 30-49  | **REBID**       | Competitive alternatives assessment required before committing       |
| 0-29   | **TERMINATE**   | Do not renew — strategic, financial, or performance basis for exit   |

**⟁ CLARIFY** — If the score falls in the RENEGOTIATE or REBID range (30-69), present the
borderline factors to the user and ask:

- "The scoring suggests [RENEGOTIATE / REBID]. Key drivers: [list top factors]. Would you like
  to explore (a) the renegotiation approach in detail, (b) the rebid process and timeline, or
  (c) both options side-by-side?"

### Step 10: Generate Renewal Negotiation Priorities

If the decision is PROCEED or RENEGOTIATE, generate a prioritized negotiation package.

**Negotiation Priority Framework:**

#### Tier 1 — Must-Haves (Deal Breakers)

Issues where the organization cannot proceed without resolution:

- Auto-renewal term exceeds acceptable maximum (e.g., 3-year lock-in when playbook maximum is 1 year)
- Price escalation is uncapped or "then-current list price" (unlimited price risk)
- No termination for convenience in the new renewal term
- Evergreen clauses impose perpetual obligations beyond reasonable scope
- Notice period for next renewal is insufficient for internal decision-making
- Data return and deletion obligations are absent or inadequate

**Negotiation strategy**: Lead with Tier 1 items. These are non-negotiable. If counterparty
refuses all Tier 1 asks, escalate to business decision-maker for walk-away analysis.

#### Tier 2 — Should-Haves (Strong Preferences)

Issues that materially affect risk but have room for negotiation:

- Price escalation cap reduction (negotiate down from current CPI+5% to CPI+2%)
- Notice window extension (negotiate from 30 days to 60 days for next renewal cycle)
- Renewal term reduction (from 3-year to 1-year automatic renewal periods)
- Audit rights strengthened or added for next renewal term
- SLA improvement or service credit enhancement
- Performance milestones tied to renewal commitment

#### Tier 3 — Nice-to-Haves (Concession Candidates)

Issues that improve the position but can be conceded strategically:

- Preferred governing law (if current is acceptable)
- Minor definitional improvements
- Additional report types or frequencies
- Cosmetic notice mechanism improvements
- Minor insurance requirement adjustments

**Negotiation sequence**: Lead with Tier 1. Trade Tier 3 concessions to secure Tier 2 wins.
Never concede Tier 1 without escalation.

**Redline Format for Renewal Negotiations:**

```
**Clause**: [Section reference and clause name]
**Current language**: "[exact quote from the contract]"
**Proposed redline**: "[specific alternative language]"
**Rationale**: [1-2 sentences suitable for external sharing]
**Legal basis**: [Relevant statute, principle, or market standard — or "General commercial practice"]
**Priority**: [Tier 1 (Must-Have) / Tier 2 (Should-Have) / Tier 3 (Nice-to-Have)]
**Fallback**: [Alternative position if primary redline is rejected]
**Timeline impact**: [Does this change the notice window or renewal term calculation?]
```

**Example Redline — Auto-Renewal Term Reduction:**

```
**Clause**: Section 5.2 — Renewal
**Current language**: "This Agreement shall automatically renew for successive three (3)-year
  periods unless either party provides written notice of non-renewal no less than ninety (90)
  days prior to expiration."
**Proposed redline**: "This Agreement shall automatically renew for successive one (1)-year
  periods unless either party provides written notice of non-renewal no less than sixty (60)
  days prior to expiration. Notwithstanding the foregoing, either party may terminate for
  convenience upon ninety (90) days' written notice."
**Rationale**: Market standard for SaaS agreements is 1-year auto-renewal with 60-day notice.
  A 3-year lock-in period is materially above market and removes budget flexibility.
**Priority**: Tier 2 (Should-Have)
**Fallback**: Accept 2-year auto-renewal periods with 90-day notice if 1-year is refused.
```

### Step 11: Quality Verification

Before delivering the renewal analysis, run the quality checks.

#### 11a. Citation Quality Gates

Run these 7 gates silently. Revise before delivering if any gate fails.

| Gate                    | Rule                                                                                                              | Fail Action                                              |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**              | Every legal claim cites a specific statute, regulation, or contract section                                       | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**              | All dates in ISO 8601 (YYYY-MM-DD), all durations as "[N] days/months/years"                                      | Normalize format                                         |
| **Currency**            | Every statutory reference checked for amendments or repeal                                                        | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**              | Analysis stays within the contract's governing law — no jurisdiction bleed                                        | Remove or flag as [JURISDICTION-SPECIFIC]                |
| **Confidence**          | Uncertainty explicitly stated, not hidden                                                                         | Add confidence qualifier                                 |
| **Timeline Integrity**  | Notice window open date < safe send date < notice deadline < renewal date                                         | Flag logical impossibilities and recalculate             |
| **Renewal Specificity** | Every deadline has: (a) source clause citation, (b) computation formula, (c) anchor date, (d) days until deadline | Flag any incomplete deadline calculations                |

#### 11b. Self-Interrogation for CRITICAL/RED Items

For any deadline classified as CRITICAL or clause classified as RED, apply this 3-pass review:

**Pass 1 — Calculation Chain Integrity:**

- Does the deadline calculation follow directly from the contract language?
- Could a court in this jurisdiction interpret the notice clause differently, giving more time?
- Is the anchor date (effective date, anniversary date, renewal date) unambiguously established?

**Pass 2 — Completeness:**

- Have all amendments and side letters that could affect the renewal clause been reviewed?
- Is there a statutory override of the contractual notice period in the governing jurisdiction?
- Are there any conditions precedent to renewal that might invalidate the auto-renewal trigger?

**Pass 3 — Challenge:**

- What is the strongest argument that this deadline is not actually critical?
- Under what circumstances might the counterparty agree to extend the notice window retroactively?
- Could this issue be resolved by a waiver-and-reaffirmation strategy rather than emergency action?

If any pass reveals a weakness, revise before delivery. Mark the audit trail:
`self_interrogation: PASS` or `self_interrogation: REVISED`

#### 11c. Completeness Verification

Confirm all required elements are addressed:

- [ ] All 10 metadata elements extracted (Step 5)
- [ ] Timeline visualization produced (Step 6)
- [ ] Price escalation mechanisms catalogued (Step 7)
- [ ] Evergreen clauses assessed (Step 8)
- [ ] Renewal decision scored and recommendation provided (Step 9)
- [ ] Negotiation priorities tiered (Step 10, if PROCEED or RENEGOTIATE)
- [ ] Glass Box audit trail populated (below)
- [ ] Writing standards applied (below)

### Step 12: Deliver Renewal Analysis Package

Deliver the complete output using the template in the **Output Format Template** section.

---

## Renewal Clause Deep Analysis

### Auto-Renewal Provision Analysis (Deep)

For the main renewal clause, analyze at depth:

**1. Renewal Trigger**

- Is renewal affirmative (notice required TO renew) or passive (auto-renews unless notice to CANCEL)?
- What event triggers renewal — contract anniversary, fixed date, project completion?
- Is renewal conditional on anything (regulatory approval, performance threshold, mutual consent)?

**2. Notice Requirements**

- Form: written / electronic / certified mail / delivery to a specific system
- Timing: X days before contract expiration vs. X days before renewal date (these differ if
  the contract has multiple auto-renewal periods)
- Recipient: named individual / role / legal department / any officer of the party
- Content: must specify contract reference, renewal decision, next term, pricing?

**3. Consequences of Missing Notice**

- Does the contract auto-renew for the full term if notice is missed?
- Are there any cure rights after missed notice?
- Can the counterparty waive the notice requirement and accept late notice?

[JURISDICTION-SPECIFIC] Check:

- Whether mandatory statutory notice periods override the contract's notice clause in the
  governing jurisdiction
- Whether certain B2C auto-renewal laws impose additional requirements (FTC Final Rule [VERIFY],
  California ARL [VERIFY], New York Gen. Oblig. Law § 5-903 [VERIFY])
- Whether B2B auto-renewal rules apply if one party is a small business or consumer-equivalent

**4. Renewal Terms**

- Does the contract renew on the SAME terms, or are terms renegotiated at renewal?
- If terms change at renewal (e.g., price escalates automatically), what is the mechanism?
- Does the renewed contract have a different governing law, notice structure, or liability regime?

**5. Termination for Convenience**

- Is there a termination for convenience right during the renewal term?
- What notice is required for T4C? (Note: if T4C requires 90 days notice but renewal auto-occurs
  on 60 days notice, the effective decision window is 150 days before renewal — not 60.)
- Does T4C require payment of outstanding fees, early termination fees, or winding-down costs?

---

## Price Escalation Analysis (Deep)

### CPI-Linked Escalation

The most common mechanism. Key analysis points:

- **Which CPI?** U.S. Bureau of Labor Statistics publishes multiple indexes: CPI-U (all urban
  consumers), CPI-W (urban wage earners), CPI-All-Items, Core CPI (excluding food and energy).
  Contracts should specify the exact index — ambiguity favors the vendor [VERIFY].
- **Base period**: When does the CPI measurement begin? Contracts tied to "the CPI at the time
  of renewal" without specifying a base period create uncertainty.
- **Cap and floor**: Best practice is "whichever is lower: CPI-U or [N]%" (caps upside) or
  "not less than [X]%" (floor protects vendor). Negotiate for caps, resist floors.
- **Compounding**: Compound escalation grows faster than simple escalation — model 5-year
  cumulative impact before agreeing to any annual escalation formula.

### Vendor-Discretion Pricing ("Then-Current List Price")

Highest-risk escalation mechanism. Analysis points:

- The vendor controls the index by setting their own list price — unlimited escalation potential
- Check whether the contract defines "list price" or references a published price list
- Negotiate a price protection schedule: "Renewal pricing shall not exceed the pricing in
  effect at the time of execution plus [CPI + X%] annually"
- If vendor insists on list pricing, negotiate a "most-favored customer" or "market rate"
  benchmark clause

### "To Be Agreed" Pricing

Critical risk: renewal pricing is undefined, creating negotiation uncertainty at the worst
possible time (when auto-renewal has already triggered or is imminent). Analysis points:

- This is effectively "no renewal pricing term" — a material gap
- The parties may have different expectations of what "agreed" means (past pricing? market rate?)
- Recommend fixing: insert a pricing formula or mechanism in the renewal term, with fallback
  if agreement is not reached (e.g., "if parties cannot agree on renewal pricing within 30 days
  of renewal date, the Agreement shall terminate at the end of the current term")

---

## Stakeholder Impact Map

For every renewal analysis, identify ALL affected stakeholders:

| Stakeholder                      | Role               | Renewal Interest                | Impact      | Action Required               |
| -------------------------------- | ------------------ | ------------------------------- | ----------- | ----------------------------- |
| Business Owner                   | Decision-maker     | Service continuity              | Primary     | Approve renewal decision      |
| Finance / Procurement            | Budget authority   | Cost control                    | Primary     | Approve pricing changes       |
| Legal                            | Risk management    | Term and risk review            | Primary     | Review redlines and notice    |
| Operations / IT                  | Service dependency | Service continuity              | High        | Confirm operational impact    |
| Compliance                       | Regulatory         | Data handling / regulatory risk | Medium      | Confirm compliance impact     |
| Data subjects (if DPA)           | Third party        | Data protection                 | Indirect    | Ensure DPA is renewed         |
| Sub-processors (if any)          | Third party        | Flow-down obligations           | Indirect    | Confirm sub-processor renewal |
| Senior Counsel / Outside Counsel | Escalation         | Material risk                   | Conditional | Engage if RED issues found    |

---

## Deviation Severity Classification

### GREEN — No Renewal Concern

The renewal provision is clear, enforceable, and favorable (or at market standard). No
negotiation needed on this point.

**Examples:**

- Auto-renewal for 12-month periods with 60-day notice — market standard
- CPI-linked pricing with cap at CPI+3% — reasonable and predictable
- Clear written notice requirement with a well-identified recipient
- Termination for convenience available at renewal with 30-day notice

**Action**: Note for awareness. No negotiation needed.

### YELLOW — Monitor or Negotiate

The renewal provision is not favorable but is within a negotiable range. Requires attention
before the auto-renewal triggers.

**Examples:**

- Auto-renewal for 24-month periods when playbook maximum is 12 months
- CPI-linked pricing without a cap (escalation is predictable but uncapped)
- Notice requirement of 90 days with only 91 days remaining — borderline safe
- Termination for convenience requires 6-month notice — long but manageable

**Action**: Generate specific redline language. Provide fallback position. Assess business
impact of accepting vs. negotiating.

### RED — Escalate or Do Not Renew

The renewal provision poses material risk. Requires senior stakeholder review or immediate
action before the deadline triggers.

**Examples:**

- Auto-renewal for 5 years with 30-day notice — excessive lock-in
- Pricing at "then-current list price" — uncapped escalation risk
- Notice deadline has passed — auto-renewal has triggered without intent
- No termination for convenience in the renewal term — locked in with no exit
- Notice clause is ambiguous — legal effectiveness of notice is uncertain
- Evergreen indemnity clause with no scope limit — indefinite exposure

**Action**: Explain specific risk. Provide market-standard alternative language. Recommend
escalation path. Set immediate deadline for action.

---

## Quality Assurance Framework

### PDCA Quality Cycle

**PLAN**: Identify contract type, renewal type (auto vs. manual), governing law, user's side
and intent. Confirm notice window status. Determine whether emergency action is needed before
full analysis.

**DO**: Execute Steps 5-10. Extract metadata, calculate deadlines, analyze price escalation,
assess evergreen clauses, score renewal decision, generate negotiation priorities.

**CHECK**: Run the 7 Citation Quality Gates. For any CRITICAL or RED item, run the
Self-Interrogation 3-pass review. Verify timeline arithmetic is internally consistent.
Confirm all metadata elements are populated or explicitly marked as unknown.

**ACT**: Note any new renewal clause patterns discovered for future playbook updates. If this
renewal reveals a gap in the organization's standard contract template (e.g., missing price
cap), flag for template review. Update the renewal decision once additional data becomes
available.

### Citation Quality Gates

See Step 11a for the complete 7-gate checklist.

### Self-Interrogation for CRITICAL/RED Items

See Step 11b for the complete 3-pass structure.

### Confidence Scoring

For each material finding, assign a confidence level:

| Level        | Range     | Meaning                                          | Action                                                |
| ------------ | --------- | ------------------------------------------------ | ----------------------------------------------------- |
| **Definite** | 0.95-1.0  | Clear contract language, no ambiguity            | State with confidence                                 |
| **High**     | 0.80-0.94 | Strong basis, minor interpretation questions     | State with brief caveat                               |
| **Probable** | 0.60-0.79 | Good arguments but reasonable minds could differ | State with reasoning and contra-indicators            |
| **Possible** | 0.40-0.59 | Genuinely uncertain, competing interpretations   | Flag for counsel review with both sides               |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative                          | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

Apply confidence scoring to:

- Each deadline calculation (affected by notice clause clarity)
- Each evergreen clause classification (affected by "survival" language clarity)
- Cost-benefit analysis (affected by availability of performance and pricing data)
- Negotiation priority ranking (affected by market data availability)

Items rated below 0.60 (Possible or Unlikely) should be flagged for qualified legal review
before the organization acts on them.

---

## Glass Box Audit Trail

Every renewal analysis output MUST include a Glass Box audit section at the end:

```yaml
glass_box:
  skill_name: "legalcode-contract-renewal-analysis"
  contract: "[Contract title, parties, execution date]"
  contract_type: "[SaaS / Professional Services / License / Vendor Agreement / etc.]"
  user_side: "[Customer / Vendor / Licensor / Licensee / Neutral]"
  governing_law: "[Jurisdiction identified from the contract]"
  renewal_analysis:
    renewal_type: "[Auto-renewal / Manual extension / Fixed-term with option / Unknown]"
    renewal_date: "[YYYY-MM-DD or UNKNOWN]"
    notice_deadline: "[YYYY-MM-DD or UNKNOWN]"
    safe_send_date: "[YYYY-MM-DD or UNKNOWN]"
    days_until_safe_send: "[n or UNKNOWN or PAST]"
    deadline_status: "[GREEN / YELLOW / ORANGE / RED / CRITICAL / PAST DEADLINE]"
    evergreen_clauses_found: "[count]"
    price_escalation_mechanisms: "[count]"
    termination_for_convenience: "[yes / no / conditional]"
  renewal_decision:
    recommendation: "[PROCEED / RENEGOTIATE / REBID / TERMINATE / CONVERT]"
    renewal_score: "[0-100]"
    confidence: "[HIGH / MEDIUM / LOW — rationale]"
  playbook_used: "[Playbook name or 'General commercial standards']"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to temp file or 'Not created']"
  statutes_consulted:
    - "[Statute 1 — VERIFIED (legalcode-mcp) or UNVERIFIED]"
    - "[Statute 2 — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL/RED items)"
  confidence_distribution:
    definite: 0
    high: 0
    probable: 0
    possible: 0
    unlikely: 0
  assumptions:
    - "[Assumption 1 — e.g., effective date assumed from contract header; not independently verified]"
    - "[Assumption 2 — e.g., no amendments found; if amendments exist, renewal terms may differ]"
  limitations:
    - "[Limitation 1 — e.g., performance data not provided; vendor performance scored as neutral]"
    - "[Limitation 2 — e.g., benchmarking data not available; pricing comparison marked as UNKNOWN]"
  reviewer: "AI-assisted — requires qualified legal review before action"
```

---

## Anti-Patterns

What NOT to do in contract renewal analysis:

1. **Calculating the renewal deadline from the wrong anchor** — "90 days before renewal date"
   means 90 days before the CONTRACT RENEWAL DATE, not 90 days before the calendar year end,
   the notice date, or when you first started thinking about renewal. Verify the anchor date.

2. **Treating the notice deadline as the decision deadline** — The legal deadline to send
   notice and the internal deadline to make the renewal decision differ by at least the internal
   approval buffer (typically 10 business days minimum). Planning to decide on Day 0 of the
   notice window is too late.

3. **Missing the auto-renewal clause entirely** — Auto-renewal language is often buried in
   Section 12 ("Term") boilerplate, not highlighted in the commercial terms. Read the entire
   contract, not just the cover page and commercial schedule.

4. **Assuming "automatically continues" means perpetual** — Some contracts state the service
   "continues" on the same terms without specifying a renewal period or whether it has a fixed
   end date. This creates genuine ambiguity — escalate to counsel rather than assuming.

5. **Trusting a CLM system's renewal date without verifying the source clause** — CLM systems
   extract renewal dates automatically but can misinterpret anniversary clauses, fixed-date
   renewals, and conditional renewals. Always verify the CLM's date against the actual contract
   language.

6. **Treating price escalation as "not my department"** — A price escalation clause that goes
   unanalyzed at renewal can result in a 15-20% total cost increase over a 5-year term. Always
   model the cumulative financial impact, not just the year-one change.

7. **Confusing simple and compound escalation** — A 3% annual increase over 5 years is NOT
   15% total. It is (1.03^5 - 1) = 15.93%. Always use compound calculation for multi-year
   escalation impact modeling.

8. **Accepting "then-current list price" without negotiating a price cap** — This is effectively
   unlimited escalation. Vendors can raise list prices at any time. This clause must always be
   flagged as RED and negotiated.

9. **Missing the termination-for-convenience notice period as a constraint on renewal** — If
   the contract has a termination-for-convenience right requiring 90 days notice, and the
   auto-renewal triggers on 60 days notice, the effective decision horizon is actually 150
   days before renewal — not 60. Model both notice periods together.

10. **Ignoring survival clauses** — A contract that terminates does not necessarily end all
    obligations. Indemnity, IP, confidentiality, and data return obligations may survive
    termination for years or indefinitely. Failure to track these creates ongoing exposure.

11. **Recommending renewal without performance data** — Renewing a vendor contract without
    objective SLA performance review is a governance failure. Always request performance data
    and state clearly when it is absent: "[Performance data not available — renewal analysis
    based on contract terms only]".

12. **Missing the amendment effect on renewal terms** — An amendment may have changed the
    notice period, renewal term, or price escalation mechanism after the original contract was
    signed. Never analyze the original contract without checking for amendments.

13. **Analyzing only the main contract body** — Renewal mechanics may be spread across the
    main agreement AND the schedule (pricing), AND the order form, AND the service description.
    All incorporated documents must be reviewed together.

14. **Treating the notice address as current when it names a specific person** — If the notice
    clause requires delivery to "the CFO of [Company]" and the CFO has changed, notice to the
    old CFO's email may not be legally effective. Verify recipient currency before sending.

15. **Assuming the counterparty will cooperate if notice is missed** — In adversarial
    relationships, a missed notice window locks you into an unwanted renewal. The counterparty
    has no legal obligation to waive the notice requirement. Act before the deadline, not after.

16. **Confusing "renewal" with "extension"** — A renewal typically involves signing a new
    agreement (potentially with new terms); an extension continues the existing agreement beyond
    its original end date on the same terms. These have different implications for renegotiation
    leverage, SLA resets, and regulatory compliance.

17. **Ignoring evergreen clauses that create ongoing post-termination liability** — The worst
    evergreen clauses are those that impose perpetual financial obligations after termination
    (e.g., perpetual indemnity for IP infringement arising from services delivered under the
    agreement). These must be negotiated down to a reasonable survival period.

18. **Delivering renewal analysis without a timeline visualization** — Abstract descriptions
    like "you have approximately 60 days" are insufficient. Stakeholders need to see a timeline
    table with specific dates, urgency status, and required actions. Always include the Critical
    Timeline Table (Step 6 format).

19. **Not modeling vendor switching costs in the rebid scenario** — A rebid may appear cheaper
    based on quoted price but fails to account for transition costs: data migration, staff
    retraining, system integration, operational disruption, and productivity loss during
    switchover. Cost-benefit analysis must include switching costs to be meaningful.

20. **Treating the renewal decision as solely legal** — Contract renewal is a business decision
    with legal constraints, not a legal decision with business consequences. Legal provides
    the compliance framework (notice, terms, risk), but the business (Finance, Operations,
    Procurement) makes the renewal call. Ensure the right stakeholders are in the decision.

21. **Analyzing the renewal in isolation from the broader vendor portfolio** — If an
    organization has multiple contracts with the same vendor (e.g., a master agreement plus
    several work orders), renewing or terminating one may affect the others. Look for cross-
    contract dependencies before recommending a standalone renewal decision.

22. **Ignoring recently enacted auto-renewal legislation** — The legal landscape for auto-renewal
    clauses has changed materially in 2024-2025, with the FTC Final Rule (May 2025 [VERIFY]),
    California AB 2863 (July 2025 [VERIFY]), and similar state laws. Always check for recent
    statutory changes before advising on auto-renewal enforceability.

---

## Writing Standards

Apply plain-language discipline to all output:

**For renewal decision summaries** (shared with business stakeholders):

- Lead with the critical deadline: "Notice deadline is [date] — [N] days remaining — [status]"
- Use tables for timelines and cost-benefit comparisons (easier to scan than prose)
- Every deadline must cite the specific contract clause and formula used
- Separate timeline facts (objective) from analysis opinions (judgment-based)
- Name the required owner and escalation path for every action item
- Plain language: no legal jargon; if a legal term is required, define it in the same sentence

**For renewal negotiation memos** (shared with procurement or vendor management):

- Lead with Tier (Must-Have / Should-Have / Nice-to-Have) for each priority
- Every redline must include: specific language, fallback position, business rationale
- Include market benchmarking to justify each redline position
- Separate what is non-negotiable (Tier 1) from what can be traded (Tier 2/3)
- Keep redlines commercially reasonable — aggressive redlines that the counterparty will reject
  serve no one

**For internal legal analysis:**

- Same plain-language standards
- May include technical legal analysis of notice enforceability, evergreen clause scope
- Mark all unverified legal propositions as [VERIFY]
- Include confidence levels for all deadline calculations
- Preserve source documentation: clause citations, calculation formulas, assumptions

**Quality gates before delivery:**

1. Can a non-lawyer CFO or operations director understand the executive summary and the
   recommended action in under 60 seconds?
2. Can the counterparty's procurement team understand and respond to each redline?
3. Does every deadline have a source clause citation, computation formula, and urgency status?
4. Are cost-benefit assumptions stated explicitly, with [DATA NEEDED] flags for missing inputs?
5. Is the safe send date clearly marked with internal approval buffer shown?
6. Are all RED/CRITICAL flags accompanied by specific remediation steps?
7. Could any sentence be shorter without losing essential meaning? If yes, shorten it.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for jurisdiction-relevant statutes on auto-renewal, notice requirements,
  and price escalation enforceability
- Save results to a local temp file (`/tmp/legalcode-renewal-authority.md`)
- Reference verified authority throughout the clause analysis
- For RED items, search for case law on missed notice consequences and evergreen enforceability
- Verify statutory currency (e.g., whether recent auto-renewal legislation amendments are in force)
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus analysis on contractual risk and commercial decision rather than legal enforceability
- Flag that jurisdiction-specific auto-renewal laws require manual verification before acting

---

## Output Format Template

Structure the final deliverable as:

```markdown
# Contract Renewal Analysis

**Document**: [contract name/identifier]
**Parties**: [party names and roles]
**Your Side**: [customer/vendor/etc.]
**Governing Law**: [jurisdiction]
**Analysis Date**: [date]
**Review Basis**: [Playbook name / General Commercial Standards]

---

## RENEWAL STATUS — [GREEN / YELLOW / ORANGE / RED / CRITICAL]

**Recommendation**: [PROCEED / RENEGOTIATE / REBID / TERMINATE / CONVERT]
**Renewal Score**: [0-100]
**Confidence**: [level]

**Action Required**: [One sentence: what needs to happen, by when, by whom]

---

## Critical Timeline

CONTRACT RENEWAL TIMELINE — [Contract Name]
─────────────────────────────────────────────────────────────────
Date Event Status Action
─────────────────────────────────────────────────────────────────
[YYYY-MM-DD] Contract Effective Date Historical —
[YYYY-MM-DD] Notice Window Opens [status] [action]
[YYYY-MM-DD] Safe Send Date (internal) [status] [action]
[YYYY-MM-DD] Latest Notice Send Date [status] [action]
[YYYY-MM-DD] Renewal / Termination Date [status] [action]
─────────────────────────────────────────────────────────────────
TODAY IS: [date] DAYS TO SAFE SEND DATE: [n] [STATUS]
─────────────────────────────────────────────────────────────────

---

## Key Findings

[Top 3-5 renewal issues with severity flags (RED/YELLOW/GREEN) and one-line summaries]

1. [RED] [Finding] — [one-line explanation]
2. [YELLOW] [Finding] — [one-line explanation]
3. [GREEN] [Finding] — [one-line explanation]

---

## Renewal Clause Analysis

### Auto-Renewal Provision — [GREEN / YELLOW / RED] | Confidence: [level]

**Contract says**: [summary]
**Analysis**: [findings]
**Risk**: [explanation]
**Redline** (if needed): > [proposed language]

### Price Escalation — [GREEN / YELLOW / RED] | Confidence: [level]

**Mechanism**: [type — CPI / PPI / fixed % / list price / to be agreed]
**Current rate**: $[X]
**Renewal rate (calculated)**: $[Y] — [+/- Z%]
**5-year cumulative impact**: $[amount] ([%] increase)
**Redline** (if needed): > [proposed language]

### Evergreen Clauses — [count found]

| Clause | Duration   | Risk    | Action   |
| ------ | ---------- | ------- | -------- |
| [type] | [duration] | [level] | [action] |

### Termination for Convenience — [Present / Absent]

**Details**: [notice period, conditions, cost implications]
**Risk**: [explanation if YELLOW or RED]

---

## Cost-Benefit Analysis

| Factor                        | Renew             | Rebid      | Difference        |
| ----------------------------- | ----------------- | ---------- | ----------------- |
| Annual fees                   | $[X]              | $[Y]       | +/-$[Z]           |
| Implementation/switching cost | $0                | $[Y]       | $[Y]              |
| Transition risk               | Low               | [estimate] | —                 |
| Total 1-year cost             | $[X]              | $[Y+Z]     | +/-$[Z]           |
| Total 3-year cost             | $[X×3+escalation] | $[Y×3+Z]   | +/-$[Z]           |
| **Winner**                    |                   |            | **[Renew/Rebid]** |

**Performance Summary**:

- SLA 1: [target vs. actual] — [status]
- SLA 2: [target vs. actual] — [status]

**Benchmarking**: [current rate vs. market: above/below/at market — by [%]]

---

## Negotiation Priorities

**Tier 1 — Must-Haves (Deal Breakers)**:

- [Issue 1]: [current clause] → [proposed redline] — [rationale]

**Tier 2 — Should-Haves (Strong Preferences)**:

- [Issue 1]: [current clause] → [proposed redline] — [rationale]

**Tier 3 — Concession Candidates**:

- [Issue 1]: [can be conceded for Tier 2 win]

**Recommended approach**: [sequencing, tone, strategic trades]

---

## Renewal Decision Framework

| Option                    | Feasibility          | Cost            | Risk    | Timeline   | Recommended |
| ------------------------- | -------------------- | --------------- | ------- | ---------- | ----------- |
| Renew at current terms    | [yes/no/conditional] | $[X]            | [level] | [timeline] | [yes/no]    |
| Renegotiate and renew     | [yes/no/conditional] | $[X]            | [level] | [timeline] | [yes/no]    |
| Rebid (competitive)       | [yes/no/conditional] | $[X+transition] | [level] | [timeline] | [yes/no]    |
| Do not renew / terminate  | [yes/no/conditional] | $[exit cost]    | [level] | [timeline] | [yes/no]    |
| Convert to month-to-month | [yes/no/conditional] | $[X]            | [level] | [timeline] | [yes/no]    |

**Recommended decision**: [OPTION] — [2-sentence rationale]

---

## Stakeholder Impact Map

| Stakeholder      | Role             | Impact   | Action   |
| ---------------- | ---------------- | -------- | -------- |
| [Business Owner] | Decision-maker   | [impact] | [action] |
| [Finance]        | Budget authority | [impact] | [action] |
| [Legal]          | Risk             | [impact] | [action] |
| [Operations]     | Continuity       | [impact] | [action] |

---

## Next Steps

- [ ] [Action 1] — Owner: [role] — Deadline: [date]
- [ ] [Action 2] — Owner: [role] — Deadline: [date]
- [ ] [Action 3] — Owner: [role] — Deadline: [date]

If renewing: Send non-renewal / renewal notice to [recipient] at [address] by [safe send date]
If rebidding: Initiate vendor evaluation by [date]; communicate non-renewal by [notice deadline]
If escalating: Brief [decision-maker role] by [date] with cost-benefit analysis and Tier 1 asks

---

## Glass Box Audit Trail

[YAML block per Glass Box section above]
```

---

## Localization Notes

This skill is jurisdiction-agnostic by design. To create a jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with verified local legal content
2. Replace [VERIFY] tags with verified statutory references
3. Add jurisdiction-specific auto-renewal statutory requirements (see Jurisdiction and
   Governing Law section above for known jurisdiction patterns)
4. Add jurisdiction-specific anti-patterns (e.g., California ARL compliance issues for B2C,
   ROSCA compliance for US online subscriptions)
5. Update frontmatter name and description to reference the specific jurisdiction
6. Add relevant case law on notice enforceability, auto-renewal, and evergreen clauses

**Priority jurisdictions for localization (based on auto-renewal regulatory activity 2024-2025):**

- United States (federal FTC Final Rule, effective May 2025) [VERIFY]
- California (ARL amendments, effective July 2025) [VERIFY]
- New York (Gen. Oblig. Law § 5-903) [VERIFY]
- European Union (Unfair Commercial Practices Directive, consumer-facing) [VERIFY]
- United Kingdom (Consumer Contracts Regulations 2013) [VERIFY]

---

## Provenance

Created by Legalcode (2026-03-01). Original synthesis combining:

- Contract renewal management best practices (CLM industry, procurement standards)
- Legal research on auto-renewal statutory requirements across US federal, California, New York,
  EU, and UK jurisdictions (2024-2025 legislative developments)
- Structural patterns from `legalcode-contract-review` (gold standard QA frameworks,
  Citation Quality Gates, Self-Interrogation, Confidence Scoring, Glass Box audit trail)
- Deadline tracking patterns from `legalcode-obligation-tracker` (renewal notice logic,
  trigger normalization, severity classification)
- Scoring framework from `legalcode-contract-risk-scorer` (weighted decision model,
  cross-factor adjustment logic)
- 2-agent parallel research pipeline (Structural Analyst + Prompt Engineering Analyst)
  analyzing reference skills and extracting quality patterns
- Legal research via WebSearch on price escalation mechanics (CPI/PPI indexing, caps and
  floors), auto-renewal enforceability across jurisdictions, FTC regulatory developments,
  and CLM renewal management best practices
