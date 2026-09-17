---
name: legalcode-au-unfair-contract-terms
description: Review contracts for unfair terms under Australia's unfair contract terms (UCT) regime —
  Australian Consumer Law (ACL) ss 23–28 and ASIC Act ss 12BH–12BK. Use when reviewing any standard form
  consumer or small business contract for Australian UCT compliance — including SaaS agreements, subscription
  contracts, financial services terms, insurance contracts (post-5 April 2021), franchise agreements,
  services contracts, platform terms, and any terms and conditions used at scale in Australia.
metadata:
  jurisdiction: Australia
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review contracts for unfair terms under Australia's unfair contract terms (UCT) regime — Australian Consumer Law (ACL) ss 23–28 and ASIC Act ss 12BH–12BK. Covers standard form contract determination (ACL s 27 six-factor test, rebuttable presumption), consumer and small business contract thresholds (post-9 November 2023: ≤100 FTE employees OR <$10M turnover, no ACL price cap), the three-limb unfairness test (significant imbalance, not reasonably necessary, detriment), transparency as an aggravating factor (ACL s 9), s 25 grey list screening (14 illustrative categories), exempt terms (main subject matter, upfront price, legally required terms), civil penalty regime ($50M per contravention, effective 9 November 2023), ACCC 2025–26 enforcement priorities (automatic renewal, cancellation terms, subscription traps), and ASIC's parallel jurisdiction over financial products and services. Generates UNFAIR / BORDERLINE / LIKELY FAIR findings with clause-level redlines, the legitimate business justification defence, remediation language, and ACCC/ASIC enforcement risk scoring. Key cases: Karpik v Carnival plc [2023] HCA 39, ASIC v PayPal Australia [2024] FCA 762, ACCC v Fujifilm [2022] FCA, Tomasso v IG Markets [2025] WASC, ACCC v Mable Technologies (2025 undertaking). Use when reviewing any standard form consumer or small business contract for Australian UCT compliance — including SaaS agreements, subscription contracts, financial services terms, insurance contracts (post-5 April 2021), franchise agreements, services contracts, platform terms, and any terms and conditions used at scale in Australia. Jurisdiction: Australia (national — ACCC and ASIC enforcement).


# Legalcode — Australian Unfair Contract Terms Review

> **Disclaimer**: This skill provides a framework for AI-assisted review of contracts under
> Australia's unfair contract terms (UCT) regime. It does not constitute legal advice. All
> outputs require review by an Australian-qualified lawyer with competition and consumer law
> experience before reliance. The UCT regime is actively enforced by the ACCC and ASIC;
> enforcement priorities and case law evolve continuously. Verify current applicability of all
> statutory provisions, penalty thresholds, and case holdings against authoritative sources
> (Federal Register of Legislation, Federal Court of Australia, ACCC and ASIC publications)
> before acting on any finding. Statutory and case law references cited from memory carry
> hallucination risk — mark all citations with [VERIFY] unless independently confirmed against
> authoritative sources. The 2023 penalty expansion means that a contract with multiple unfair
> terms used at scale carries very large theoretical exposure; do not delay professional review.

---

## Purpose and Scope

This skill reviews standard form consumer and small business contracts for compliance with
Australia's unfair contract terms (UCT) regime under the Australian Consumer Law (ACL),
Schedule 2 to the Competition and Consumer Act 2010 (Cth), and the parallel regime in the
Australian Securities and Investments Commission Act 2001 (Cth) for financial products and
services.

**Covers:**

- Gateway assessment: standard form determination (ACL s 27 six-factor test)
- Consumer and small business threshold analysis (post-9 November 2023 expanded thresholds)
- Grey list screening — 14 categories of potentially unfair terms (ACL s 25)
- Three-limb unfairness analysis per flagged clause:
  - Significant imbalance (ACL s 24(1)(a))
  - Not reasonably necessary to protect legitimate interests (ACL s 24(1)(b), reversed burden)
  - Detriment if applied or relied upon (ACL s 24(1)(c))
- Transparency assessment (ACL s 9) as an aggravating factor
- Exempt terms identification (ACL s 26: main subject matter, upfront price, legally required)
- Clause-level UNFAIR / BORDERLINE / LIKELY FAIR classification with confidence scoring
- Redline generation with remediation language for flagged terms
- Legitimate business justification defence analysis (evidence required to rebut presumption)
- Civil penalty exposure calculation ($50M per contravention, post-9 November 2023)
- ACCC and ASIC enforcement risk profiling
- Industry-sector considerations (financial services, insurance, franchising, technology,
  energy, telecommunications, construction, gig economy)
- Glass Box audit trail for traceability

**Does not:**

- Provide legal advice or replace Australian consumer law counsel
- Cover misleading or deceptive conduct (ACL s 18), false representations (s 29), or
  unconscionable conduct (ss 20–22) beyond incidental overlap — see
  `legalcode-au-consumer-law-compliance`
- Cover the Franchising Code of Conduct 2025 — see `legalcode-franchise-agreement-review-au`
- Cover the Competition and Consumer Act 2010 Part IV (competition law / cartels)
- Cover state-specific consumer legislation beyond national ACL application
- Cover the Australian Privacy Act 1988 — see
  `australia-privacy-act-ndb-breach-notification-operations`
- Guarantee enforceability of any contractual term in Australian courts
- Replace the need for a commercial lawyer in drafting or negotiating

**Related skills:**

- `legalcode-au-consumer-law-compliance` — Full ACL compliance audit including s 18,
  consumer guarantees, product safety
- `legalcode-franchise-agreement-review-au` — Franchising Code + UCT for franchise agreements
- `legalcode-contract-review` — General commercial contract review (jurisdiction-agnostic)

---

## Jurisdiction and Governing Law

### Why Australia's UCT Regime Requires a Dedicated Skill

Australia's UCT regime is among the most powerful in the world following the November 2023
amendments:

1. **National application**: The ACL is a single federal law applying uniformly in all
   Australian states and territories, administered jointly by the ACCC and state/territory
   consumer protection agencies.

2. **Penalty transformation**: Before 9 November 2023, UCT was a declaratory-only regime —
   courts could declare terms void but could not impose fines. From 9 November 2023, including
   an unfair term, relying on it, or attempting to rely on it became _prohibited conduct_
   attracting civil penalties up to $50 million per contravention under the ACL (or $13.75
   million under the ASIC Act for financial services).

3. **Expanded scope**: The 2022 reforms dramatically expanded the small business definition
   from fewer than 20 employees with a $300,000/$1 million price cap to fewer than 100 FTE
   employees OR less than $10 million annual turnover — with no price cap under the ACL. The
   majority of the Australian commercial market now falls within scope.

4. **Reversed burden of proof**: A term is presumed not reasonably necessary to protect the
   advantaged party's legitimate interests (ACL s 24(4)). The advantaged party must adduce
   positive evidence — not assertion — to rebut this presumption.

5. **Rebuttable presumption of standard form**: A contract is presumed to be standard form
   if one party so alleges (ACL s 27(1)). The drafter bears the burden of rebuttal.

6. **Extra-territorial reach**: The UCT regime applies to foreign entities supplying to
   Australian consumers or small businesses. Choice-of-law clauses selecting foreign law do
   not oust the ACL — _Karpik v Carnival plc_ [2023] HCA 39 confirmed this [VERIFY].

### Dual Regulatory Jurisdiction

- **ACCC**: Enforces the ACL UCT regime for consumer and small business contracts generally.
  Current enforcement priorities (2025–26) include automatic renewal terms, cancellation
  terms, subscription traps, digital economy contracts, and disability/aged care platforms.
- **ASIC**: Enforces the parallel ASIC Act regime (ss 12BH–12BK) for financial products and
  financial services contracts. ASIC has targeted billing error terms (_PayPal_), manifest
  error clauses (_IG Markets_), and insurance notification terms (_Auto & General_).

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent or context, the workflow pauses and asks when:

- The gateway assessment depends on facts only the user knows (e.g., whether the counterparty
  is a consumer or small business)
- Multiple valid classification approaches exist for a borderline clause
- The legitimate business justification assessment requires commercial context
- Industry-specific regulatory considerations apply

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

Accept the contract in any format:

- **File**: PDF, DOCX, or other document
- **URL**: Link to terms in a CLM or cloud storage system
- **Pasted text**: Contract pasted directly into the conversation

If no contract is provided, prompt the user to supply one.

Identify:

- Contract type (services agreement, SaaS subscription, terms and conditions, franchise
  agreement, insurance policy, financial services agreement, platform terms, etc.)
- Parties to the contract
- Whether there is a governing law clause, and whether it nominates Australian law

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask these questions. Present structured options
where possible:

**1. Which side are you on?**

- Options: **Party offering the contract (drafter/supplier)** — compliance audit to identify
  exposure before use; **Party receiving the contract (customer/small business)** — identify
  unfair terms to negotiate or challenge; **Neutral — compliance advisory**
- _Why this matters_: The review focus differs — drafters want to know what to fix; recipients
  want to know what to push back on.

**2. What is the counterparty profile?**

- Options: **Consumer** (individual acquiring for personal/domestic/household use — no
  monetary threshold); **Small business** (≤100 FTE employees OR <$10M annual turnover —
  confirm both prongs post-9 November 2023); **Both** (the contract is used with both
  consumers and small businesses); **Unsure** — I'll assess the likely threshold
- _Why this matters_: The applicable threshold determines whether the UCT regime applies and
  whether the ACL or ASIC Act governs.

**3. Is this a financial product or financial service?**

- Options: **Yes** — banking, credit, insurance, investment product, financial advice
  (ASIC Act applies, upfront price cap of $5M); **No** — ACL applies, no price cap;
  **Partly** — some elements may be financial services
- _Why this matters_: ASIC Act penalties differ from ACL penalties; certain exemptions differ.

**4. When was this contract last entered into, renewed, or varied?**

- Options: **On or after 9 November 2023** (civil penalties apply); **Before 9 November 2023
  and not yet renewed or varied** (pre-penalty regime — declaratory only); **Unsure**
- _Why this matters_: The civil penalty regime applies only to contracts made, renewed, or
  varied on or after 9 November 2023.

**5. Any specific concerns?**

- Options: Automatic renewal / subscription traps; Unilateral variation rights; Liability
  limitations and indemnities; IP assignment; Exit fees and termination; Dispute resolution;
  Full review (all clauses); Other (describe)
- Allow multiple selections.
- _Why this matters_: Allows the analysis to lead with what matters most to the user.

If the user provides partial context, proceed with reasonable defaults and state assumptions
explicitly (e.g., "I'm assuming the contract is used with Australian consumers — flag if
that's wrong and I'll re-run the gateway").

### Step 3: Gateway Assessment — Does the UCT Regime Apply?

Before reviewing individual clauses, determine whether the UCT regime applies at all.
A negative gateway answer means the regime does not apply; a positive gateway answer
triggers the clause-by-clause analysis.

#### 3a. Standard Form Contract Determination (ACL s 27)

Under ACL s 27(1), a contract is presumed to be a **standard form contract** if one party
so alleges. The drafter bears the burden of rebuttal. A court must consider these six factors
(s 27(2)) when assessing whether the contract is standard form:

| Factor                                | Assessment Question                                                                                              |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **(a) Bargaining power**              | Did one party have all or most of the bargaining power in the transaction?                                       |
| **(b) Prepared in advance**           | Was the contract prepared by one party before any discussion?                                                    |
| **(c) Take-it-or-leave-it**           | Was the other party effectively required to accept or reject terms as presented?                                 |
| **(d) Real opportunity to negotiate** | Did the other party have a genuine, effective opportunity to negotiate the terms?                                |
| **(e) Specific characteristics**      | Do the terms account for the specific characteristics of the other party or the transaction?                     |
| **(f) Volume of contracts**           | Has the drafter entered into the same or substantially similar contracts with other parties (added by 2022 Act)? |

**Key principles:**

- A contract does not become non-standard merely because minor modifications were permitted
  or alternative pre-packaged options existed, if core terms remained take-it-or-leave-it.
- The "volume of contracts" factor means businesses using identical or near-identical clauses
  at scale face heightened exposure to standard form classification.
- If in doubt, treat the contract as standard form — the presumption applies.

**Gateway finding options:**

- **Standard form confirmed**: Proceed to Step 3b.
- **Standard form arguable — rebuttal possible**: Note the factors supporting rebuttal; flag
  as a risk; proceed to Step 3b as a precaution.
- **Genuinely negotiated**: Document the basis; note that UCT does not apply; close the review.

**⟁ CLARIFY** — If the standard form assessment is borderline (e.g., the user says "we
allow customers to negotiate some terms"), ask:

- "Which terms can customers genuinely negotiate, and how often does that occur in practice?
  If core terms like price, liability limits, and auto-renewal are non-negotiable, the
  contract likely remains standard form for UCT purposes even if some peripheral terms
  can be adjusted."

#### 3b. Consumer or Small Business Contract Threshold (ACL ss 23, 27)

Confirm the applicable regime:

| Contract Type                        | Threshold (Post-9 November 2023 — ACL)                                                                                       | Threshold (ASIC Act)                             |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **Consumer**                         | Individual acquiring wholly/predominantly for personal, domestic, or household use. No monetary cap.                         | Same definition                                  |
| **Small business**                   | At least one party has fewer than 100 FTE employees **OR** had annual turnover <$10M in prior income year. No ACL price cap. | Same headcount/turnover test; upfront price ≤$5M |
| **Pre-November 2023 small business** | Fewer than 20 employees AND upfront price ≤$300,000 (or ≤$1M for >12 months)                                                 | Same                                             |

**⟁ CLARIFY** — If the counterparty's size is unknown or if the contract is used with a
mixed customer base (some consumers, some small businesses, some larger businesses):

- "Can you confirm the typical counterparty profile? A consumer qualification is based on
  the individual's purpose (personal/domestic/household use). A small business qualification
  is based on employee count OR annual turnover at the time of contracting. If the contract
  is used with both consumers and small businesses, the UCT regime applies to both, and I
  will review it on that basis."

#### 3c. Identify Exempt Terms (ACL s 26)

Before flagging terms as potentially unfair, identify and set aside terms that cannot be
found unfair under ACL s 26:

| Exempt Category                | What It Covers                                                                                         | What It Does NOT Cover                                                                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **(a) Main subject matter**    | Terms defining the primary goods or services being supplied (e.g., "this is an ADSL internet service") | Not the terms governing _how_ the services are provided or the conditions of supply                                                         |
| **(b) Upfront price**          | Terms setting the disclosed upfront price at contract formation                                        | Contingent fees (exit fees, default fees, late payment fees triggered by events during the contract) — these remain subject to UCT scrutiny |
| **(c) Legally required terms** | Terms required or expressly permitted by Commonwealth or State/Territory law                           | Terms merely not prohibited by law — this exemption is narrow                                                                               |

Document the exempt terms and their basis. Do not include them in the UCT analysis.

### Step 4: Grey List Screening (ACL s 25)

Screen the contract for clauses matching the 14 illustrative categories in ACL s 25 —
the "grey list" of potentially unfair terms. Grey list inclusion does not create a
presumption of unfairness, but it flags clauses for priority three-limb analysis in Step 5.

For each grey list category, identify matching clauses in the contract:

| #   | Grey List Category (ACL s 25)                                                                                  | Clause Identified | Priority |
| --- | -------------------------------------------------------------------------------------------------------------- | ----------------- | -------- |
| 1   | Permits one party (but not the other) to avoid or limit performance                                            |                   |          |
| 2   | Permits one party (but not the other) to terminate                                                             |                   |          |
| 3   | Penalises one party (but not the other) for breach or termination                                              |                   |          |
| 4   | Permits one party (but not the other) to vary the contract terms                                               |                   |          |
| 5   | Permits one party (but not the other) to renew or not renew                                                    |                   |          |
| 6   | Permits one party to vary the upfront price without the other's right to exit                                  |                   |          |
| 7   | Permits one party to unilaterally determine whether a breach has occurred                                      |                   |          |
| 8   | Limits one party's vicarious liability for its agents                                                          |                   |          |
| 9   | Limits one party's right to sue                                                                                |                   |          |
| 10  | Imposes an evidential burden on the other party                                                                |                   |          |
| 11  | Is not transparent (ACL s 9: not in plain language, not legible, not clearly presented, not readily available) |                   |          |
| 12  | Requires the other party to pay exit fees unilaterally set by the advantaged party                             |                   |          |
| 13  | Purports to exclude statutory rights the other party holds (e.g., ACL consumer guarantees)                     |                   |          |
| 14  | Assigns the burden of remedying a problem to one party only                                                    |                   |          |

**Also screen specifically for ACCC/ASIC enforcement priority clause types:**

- Automatic renewal without adequate notice before renewal
- Short objection windows or deemed acceptance clauses
- Broad indemnities covering losses the indemnified party caused or contributed to
- Unilateral IP assignment extending beyond contracted deliverables
- One-sided liability exclusions or caps without preserving ACL non-excludable rights
- Dispute resolution terms with prohibitive cost (arbitration for low-value claims)
- Class action waivers (_Karpik v Carnival_ [2023] HCA 39) [VERIFY]
- Non-compete or restraint-of-trade clauses on platform workers/contractors

### Step 5: Three-Limb Analysis

For each clause flagged in Step 4, apply the three-limb unfairness test under ACL s 24(1).
A term is unfair only if **all three** limbs are satisfied. Run the analysis holistically —
assess each clause in the context of the whole contract, not in isolation.

#### Limb 1 — Significant Imbalance (ACL s 24(1)(a))

Does the term cause a significant imbalance in the parties' rights and obligations?

**Indicators of significant imbalance:**

- The right or power is held only by one party (asymmetry)
- The clause constrains the other party while imposing no reciprocal obligation on the drafter
- The clause shifts financial or legal risk from the drafter to the other party without
  corresponding benefit
- The other party has no practical ability to protect themselves if the power is exercised

**Key case principles:**

- A term disproportionately advantaging one party while constraining the other creates
  imbalance: _Karpik v Carnival plc_ [2023] HCA 39 — class action waiver solely benefited
  the carrier without restricting its own litigation options [VERIFY]
- Confusion or complexity alone does not establish imbalance: _ASIC v HCF Life_ [2024] —
  consumer confusion about a term does not itself demonstrate significant imbalance [VERIFY]
- The clause is assessed as it operates in practice, not merely as written

**Limb 1 finding**: SATISFIED / NOT SATISFIED / BORDERLINE

#### Limb 2 — Not Reasonably Necessary to Protect Legitimate Interests (ACL s 24(1)(b))

Is the term reasonably necessary to protect the legitimate interests of the advantaged party?

**Critical: Reversed burden of proof (ACL s 24(4))** — The advantaged party must prove the
term is reasonably necessary. A term is **presumed not to be** reasonably necessary. The
drafter must adduce positive evidence, not mere assertion.

**What courts require as evidence:**

- Detailed financial data, cost structures, and risk exposure demonstrating the commercial
  rationale for the term in its current form
- A reasoned link between each element of the term's scope and the identified legitimate risk
- Demonstration that a less restrictive formulation could not adequately address the risk
- Expert evidence where technical risk assessment is involved (e.g., actuarial evidence for
  insurance pre-existing condition terms)

**Legitimate interests that have survived challenge:**

- Anti-selection risk management in insurance (accepted in _ASIC v Auto & General_ [2025]
  FCAFC — change-notification clause upheld; aligned with statutory policyholder duties) [VERIFY]
- Regulatory compliance obligations expressly required by law (ACL s 26(1)(c))
- Genuine financial risk from counterparty default, where the term scope is proportionate

**Legitimate interests that have failed:**

- Avoiding pressure to settle questionable claims by preventing class actions: _Karpik_
  (_Carnival_) — not a legitimate interest [VERIFY]
- No evidence adduced at all: _ASIC v PayPal_ [2024] FCA 762 — PayPal presented no evidence
  to rebut the presumption; fee error notification clause found not reasonably necessary [VERIFY]
- General commercial preference without evidence: broad manifest error clause in _Tomasso v
  IG Markets_ [2025] WASC — proportionate alternatives existed [VERIFY]

**Limb 2 finding**: SATISFIED (not reasonably necessary) / NOT SATISFIED (reasonably necessary) / BORDERLINE

**⟁ CLARIFY** — If the drafter/adviser provides a business rationale for a challenged term,
ask: "Can you provide specific evidence to support this justification — for example, financial
data showing the cost exposure the term addresses, or evidence that a narrower version
would not adequately protect the business? Courts require concrete evidence, not assertion,
to rebut the statutory presumption that the term is not reasonably necessary."

#### Limb 3 — Detriment (ACL s 24(1)(c))

Would the term cause detriment (financial or otherwise) to the other party if applied or
relied upon?

**Key principles:**

- Detriment need not have _actually occurred_ — potential detriment suffices
- _ASIC v PayPal_: enforcement proceeded even though PayPal had not retained any erroneous
  fees; the risk of financial loss and the operational burden of constant monitoring
  constituted detriment [VERIFY]
- Detriment includes: financial loss risk, restriction of legal rights, operational burden,
  denial of practical access to justice (_Karpik_ — class actions denied), exit costs
- The detriment is assessed if the term is _applied or relied upon_, not merely included

**Limb 3 finding**: SATISFIED / NOT SATISFIED / BORDERLINE

#### Transparency Assessment (ACL s 9)

Transparency is not a separate standalone test — it is a factor in the unfairness
assessment (ACL s 24(2)(a)). Lack of transparency aggravates unfairness; transparency
alone cannot cure substantive unfairness (_Anderson v Kincumber Nautical Village_ [2025]
NSWCAT) [VERIFY].

A term is **transparent** under ACL s 9 if it is:

- Expressed in **reasonably plain language**
- **Legible**
- **Presented clearly** (not buried in fine print, complex schedules, or long linked documents)
- **Readily available** to any party affected by it at the time of contracting

**Transparency assessment:**

- TRANSPARENT: Plain language, prominently placed, clearly headed
- PARTIALLY TRANSPARENT: Reasonably clear but buried or poorly accessible
- NOT TRANSPARENT: Complex legalese, buried in fine print, not available at contracting,
  or hidden in linked external documents not provided to the other party

### Step 6: Classify Each Finding

Assign each flagged clause an overall UCT classification:

#### Classification System

| Classification   | Meaning                                                                                                                                                 | Action Required                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **UNFAIR**       | All three limbs satisfied on the analysis; material enforcement risk                                                                                    | Remove or substantially revise immediately; do not use or rely on this term                     |
| **BORDERLINE**   | Two of three limbs appear satisfied, or one limb is a close call; arguable enforcement risk                                                             | Prioritise revision; document business justification; seek legal advice                         |
| **LIKELY FAIR**  | Analysis indicates the term can survive the three-limb test, particularly where the advantaged party can demonstrate reasonably necessary justification | Monitor and document; maintain evidence of the legitimate business justification                |
| **EXEMPT**       | Term qualifies as main subject matter, upfront price, or legally required under ACL s 26                                                                | No UCT analysis required; document the basis for exemption                                      |
| **NOT IN SCOPE** | UCT regime does not apply to this term or contract                                                                                                      | Document the basis (e.g., not a standard form contract, not a consumer/small business contract) |

#### Severity Tier for UNFAIR and BORDERLINE Findings

| Tier                  | Label                                   | Penalty Exposure                                                                                                                  | Priority                                                   |
| --------------------- | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Tier 1 — Critical** | UNFAIR — ACCC/ASIC enforcement priority | High penalty exposure; clause type matches current enforcement priorities (auto-renewal, cancellation terms, one-sided liability) | Fix immediately; do not use                                |
| **Tier 2 — High**     | UNFAIR — Material enforcement risk      | Clearly unfair under three-limb test; not current enforcement priority but significant exposure                                   | Fix before any new contract made, renewed, or varied       |
| **Tier 3 — Medium**   | BORDERLINE — Arguable enforcement risk  | Close call on one or more limbs; enforcement possible but less certain                                                            | Revise to strengthen defensibility; document justification |
| **Tier 4 — Low**      | BORDERLINE — Monitor                    | Term raises UCT considerations but has good prospects of surviving three-limb test with documented justification                  | Maintain justification file; monitor case law developments |

### Step 7: Generate Remediation Recommendations

For each UNFAIR and BORDERLINE finding, generate:

**1. Original clause extract** (the problematic term, verbatim)

**2. UCT analysis summary** (one paragraph: which limbs are satisfied, why, key case analogy)

**3. Revised clause** (redlined alternative that addresses the unfairness)

**4. Business justification documentation guidance** (what evidence the drafter should
prepare and file to support the "reasonably necessary" argument, even after revision)

**5. Civil penalty exposure estimate** (post-9 November 2023 contracts only):

- Identify number of potentially affected contracts (if known)
- Apply per-contravention penalty: greater of $50M / 3× benefit / 30% adjusted turnover
- Note: each unfair term = a separate contravention; maximum exposure is cumulative

#### Redline Best Practices

- **Add counterbalancing protections**: Almost any unilateral right becomes more defensible
  with adequate notice and a penalty-free exit right for the other party.
- **Limit scope to legitimate risk**: Replace broad powers with specific, objective triggers
  (e.g., "price variation limited to changes in CPI or documented supplier cost increases"
  rather than "we may vary the price at any time").
- **Preserve ACL non-excludable rights**: Ensure liability limitations and exclusions contain
  a carve-out preserving rights under the ACL that cannot be excluded by contract (ss 64, 64A).
- **Mutual where possible**: Convert one-sided rights into mutual rights or add equivalent
  protections for the disadvantaged party.
- **Plain language**: Revise transparent versions of remaining terms to plain language and
  clear presentation, reducing the transparency aggravating factor.
- **Proportionate exit fees**: If exit fees are maintained, link them to a genuine
  pre-estimate of loss (not a unilaterally set penalty amount).

### Step 8: Industry-Sector Considerations

Apply the following industry-specific analysis where relevant. Check the contract type
identified in Step 1 and apply the relevant sector overlay.

#### Financial Services (ASIC Act Jurisdiction)

- ASIC Act ss 12BH–12BK applies the same unfairness test to financial products and services.
- Key ASIC information sheets: INFO 210 (consumer UCT protections) and INFO 211 (small
  business UCT protections) [VERIFY current versions at asic.gov.au].
- Sector-specific enforcement history:
  - **Fee error notification terms**: Short objection windows where the advantaged party
    has superior information access — _ASIC v PayPal_ [2024] FCA 762 [VERIFY]
  - **Manifest error / error correction clauses**: One-sided unilateral powers to void or
    amend transactions — _Tomasso v IG Markets_ [2025] WASC [VERIFY]
  - **Insurance notification clauses**: Survive if clearly worded, contextualised with
    examples, and aligned with statutory policyholder duties — _ASIC v Auto & General_
    [2025] FCAFC [VERIFY]
- ASIC penalty cap: greater of $13.75M (50,000 penalty units) / 3× benefit / 10% annual
  turnover (capped at approximately $555M as at 2025) [VERIFY current penalty unit values].

#### Insurance (Post-5 April 2021)

- UCT applies to general insurance and life insurance contracts via Insurance Contracts Act
  1984 (Cth) s 15(2) amendment effective 5 April 2021 [VERIFY].
- **Excluded**: Medical indemnity insurance, private health insurance, workers' compensation
  insurance, compulsory third-party motor insurance.
- High-risk terms in insurance: pre-existing condition exclusions that misrepresent statutory
  rights under ICA s 47 (_HCF Life_ — $750,000 penalty for misleading term [2025]) [VERIFY];
  coverage variation terms; broad cancellation/non-renewal provisions; "catch-all" duty of
  disclosure terms broader than statutory requirements.
- ASIC has signalled review of "wear and tear" and maintenance exclusions in home insurance.

#### Franchising

- ACCC has conducted comprehensive UCT reviews of franchise agreements and found that every
  agreement reviewed contained potentially unfair terms.
- Highest-risk terms in franchise agreements:
  - Unilateral variation of system requirements, fees, or marketing fund levies without
    franchisee consent or exit rights
  - Withholding and set-off clauses without limitation or dispute mechanism
  - Broad audit power clauses (unlimited scope, frequency, costs borne by franchisee)
  - Restraint of trade clauses broader than necessary (geographic or temporal)
  - Termination for minor breaches without cure opportunity
  - Unilateral determination-of-breach clauses
- Note: Franchising also has the Franchising Code of Conduct 2025 overlay — see
  `legalcode-franchise-agreement-review-au` for full franchise coverage.

#### Technology / SaaS / Platform

- High-risk clause combinations: uncapped customer indemnities for third-party claims
  paired with vendor liability cap at monthly fees; unilateral service feature variation
  without notice or compensation; automatic annual price escalation at renewal without
  clear advance disclosure; broad IP assignment of all work product including pre-existing
  background IP; platform terms requiring workers to forfeit client relationships.
- _ACCC v Mable Technologies_ (2025 undertaking — first enforcement under expanded regime):
  $5,000 minimum penalty for support workers maintaining client relationships within
  12 months; auto-approval of timesheets within 24 hours; unilateral fee changes without
  reasonable notice [VERIFY].
- ACCC 2025–26 priority: subscription traps and automatic renewal in digital/online services.

#### Energy and Telecommunications

- Historical ACCC industry reviews found problematic terms in energy and telco sectors.
- Energy: unilateral price variation in supply contracts without exit rights; exclusion of
  liability for service interruptions; penalty fees for usage outside contracted bands;
  automatic rollover without adequate notice.
- Telecommunications: early termination fees structured as penalties (not genuine
  pre-estimates of loss); unilateral plan changes; data throttling provisions inadequately
  disclosed; auto-contract extension terms.

#### Construction

- UCT now applies to construction contracts following the small business threshold expansion.
- High-risk terms: unilateral time extension determinations; termination for convenience
  without cost reimbursement for committed expenditure; unilateral scope variation;
  one-sided delay damage caps; conclusive evidence clauses regarding payment calculations.

### Step 9: Enforcement Risk Assessment

Provide an overall ACCC/ASIC enforcement risk profile:

| Risk Level   | Description                | Indicators                                                                                                                           |
| ------------ | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **CRITICAL** | Immediate enforcement risk | Contract type matches current ACCC/ASIC priority; clearly unfair terms used at scale; recent analogous enforcement action            |
| **HIGH**     | Material enforcement risk  | Multiple UNFAIR-classified terms; large volume of contracts affected; non-compliance with prior ACCC/ASIC guidance in the sector     |
| **MEDIUM**   | Potential enforcement risk | BORDERLINE terms; moderate contract volume; sector not currently an enforcement priority                                             |
| **LOW**      | Low enforcement risk       | LIKELY FAIR terms or BORDERLINE with strong documented justifications; small contract volume; proactive compliance measures in place |

**Factors the ACCC/ASIC weigh in enforcement decisions (ACL s 224A):**

- Severity and extent of the conduct
- Loss or damage caused or likely to be caused
- Size and financial resources of the business
- Whether the conduct was deliberate or reckless
- Whether the business has prior contraventions
- Whether the business cooperated with regulators
- Whether the business took remedial action

### Step 10: Quality Verification

Before delivering the analysis, run the quality checks in the Quality Assurance Framework
section:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every UNFAIR (Tier 1 and Tier 2) classification, run the 3-pass Self-Interrogation.
3. Assign a Confidence Score to each material clause finding.
4. Verify all three limbs have been addressed for each flagged clause.
5. Verify the gateway assessment supports application of the UCT regime.
6. Generate the Glass Box Audit Trail and append it to the output.

---

## UCT Clause Analysis Reference

### A. Unilateral Variation Clauses

**Statutory basis**: ACL s 25(1)(d) — grey list item

**Why high risk**: Broad unilateral variation rights — allowing one party to change prices,
service features, specifications, or contract terms for any reason or without notice — are
the most consistently targeted clause type by both the ACCC and ASIC.

**Three-limb analysis:**

- _Significant imbalance_: Asymmetric power — only one party can alter the bargain. The
  other party committed on the basis of original terms but bears the risk of future changes.
- _Not reasonably necessary_: Drafter must show evidence that the scope of the variation
  right is proportionate to a specific, identified legitimate risk. A broad "any reason"
  variation clause fails this test. A variation right limited to CPI, regulatory cost
  changes, or verified third-party cost increases has better prospects.
- _Detriment_: Financial impact of unexpected price increases; inability to plan; risk of
  being locked into a materially changed service.

**Legitimate justification evidence**: Documented cost structures showing exposure to
variable input costs; regulatory change obligations; financial modelling demonstrating that
the current scope is the minimum necessary.

**Remediation**:

- Limit variation triggers to objectively defined events (CPI, regulatory change, documented
  cost increases)
- Require minimum notice of 30 days before variation takes effect
- Grant the other party a penalty-free exit right if they disagree with material variations
- _Anderson v Kincumber_ [2025]: even CPI + composite formula found unfair when components
  were unsubstantiated — transparency alone insufficient [VERIFY]

### B. Automatic Renewal / Rollover Clauses

**Statutory basis**: ACL s 25(1)(e) — grey list item; ACCC 2025–26 enforcement priority

**Why high risk**: Automatic renewal without adequate pre-renewal notice is an explicit
ACCC 2025–26 enforcement priority. The regime targets "harmful cancellation terms" and
"subscription traps."

**Three-limb analysis:**

- _Significant imbalance_: The drafter benefits from continued revenue without active
  re-consent; the other party bears the risk of being locked in to another term.
- _Not reasonably necessary_: Renewal processes can be managed with adequate notice
  mechanisms — the automatic feature serves primarily the drafter's revenue continuity.
- _Detriment_: Financial commitment without genuine opportunity to review; exit fees
  if cancellation missed; compounding over successive renewal periods.

\*_ACCC v JJ Richards_ [2017] FCA: auto-renewal unless cancelled within 30 days before term
end declared unfair [VERIFY].
_ACCC v Fujifilm_ [2022] FCA: automatic renewal was one of six declared-unfair term
categories [VERIFY].

**Remediation**:

- Provide clear, prominent written notice **at least 30 days before** the renewal date
- Notice must specify: the renewal date, the renewal period, the renewal price (especially
  if escalated), and the precise mechanism for cancelling (not just "contact us")
- Make the opt-out process accessible, simple, and not more burdensome than the original
  sign-up
- If renewal includes price escalation, disclose the new price at notice stage; grant an
  exit right at the pre-escalation price

### C. Limitation of Liability and One-Sided Indemnity

**Statutory basis**: ACL ss 25(1)(a), (c) — grey list items; ACL ss 64, 64A (non-excludable
consumer guarantee rights)

**Why high risk**: Completely excluding the supplier's liability while imposing full
liability or indemnity obligations on the other party is a recurring target. The ByteCard
(2013) and Fujifilm (2022) enforcement actions both included one-sided liability terms
[VERIFY].

**Three-limb analysis:**

- _Significant imbalance_: Asymmetric risk allocation — the supplier is fully protected;
  the customer bears all loss regardless of the supplier's conduct.
- _Not reasonably necessary_: Proportionate liability caps are legitimate (e.g., cap at
  12 months' fees); complete exclusion for the drafter's own acts or negligence is not.
- _Detriment_: Financial loss with no remedy; operational disruption with no compensation.

**Consumer guarantee interaction**: Liability limitations that purport to exclude or limit
statutory consumer guarantee rights are void under ACL s 64. Even a limitation clause that
is not independently unfair under UCT may be void under s 64 if it attempts to exclude
non-excludable rights.

**Remediation**:

- Use a proportionate cap (e.g., higher of 12 months' fees or a stated dollar amount)
- Apply the cap mutually (same cap on both parties' aggregate liability)
- Carve out from the cap: fraud, wilful misconduct, death or personal injury, data breach
  obligations, indemnification obligations
- Expressly preserve rights under the ACL that cannot be excluded (ss 64, 64A)
- For indemnities: limit to losses _in the indemnitor's control_; exclude losses the
  indemnified party caused or contributed to; make genuinely mutual where possible

### D. Exit Fees and Early Termination Charges

**Statutory basis**: ACL s 25(1)(f) — fee variation unilaterally set; ACL s 25(1)(b) —
termination rights

**Why high risk**: Exit fees unilaterally set by the advantaged party fail the three-limb
test. _ACCC v Fujifilm_ [2022] FCA declared unilateral exit fee determination unfair [VERIFY].

**Three-limb analysis:**

- _Significant imbalance_: The drafter alone determines the fee quantum — no objective
  basis or cap protects the other party.
- _Not reasonably necessary_: A genuine pre-estimate of loss is legitimate; a fee whose
  quantum is solely at the drafter's discretion is not.
- _Detriment_: Financial; practical lock-in preventing exit even from a relationship that
  has broken down.

**Remediation**:

- Pre-specify the exit fee formula at contract inception (e.g., remaining monthly fees for
  the unexpired term, or a declining schedule)
- Tie the formula to actual loss (unamortised setup costs, committed third-party costs)
- Do not reserve the right to vary the fee formula unilaterally
- Include a zero-cost exit right following material variation of the contract by the drafter

### E. Dispute Resolution Clauses

**Statutory basis**: ACL s 25(1)(i) — limits right to sue

**Why high risk**: Dispute resolution clauses that effectively deny access to justice by
imposing prohibitive costs are unfair. _AghaeiRad v Plus500AU_ [2025] FCA: arbitration
clause requiring tiered dispute resolution found unfair due to disproportionate cost
relative to potential claim value [VERIFY].

**Three-limb analysis:**

- _Significant imbalance_: One party (typically the drafter) has the resources to sustain
  complex arbitration; the other party (consumer/small business) effectively cannot pursue
  claims due to cost asymmetry.
- _Not reasonably necessary_: Efficient dispute resolution can be achieved through less
  restrictive mechanisms (e.g., small claims tribunal access, ODR platforms, low-cost
  mediation).
- _Detriment_: Practical denial of access to justice; class action waivers prevent pooling
  of claims where individual claim value is below practical litigation threshold (_Karpik_).

**Remediation**:

- Ensure dispute resolution mechanism is accessible and proportionate to the likely claim
  value (consumer and small business disputes are often low-value)
- Do not include class action waivers (_Karpik v Carnival_ — found unfair by High Court)
- Provide clear, simple escalation paths (internal complaint, external dispute resolution
  scheme, tribunal or court of appropriate jurisdiction)
- For financial services: reference the Australian Financial Complaints Authority (AFCA)
  free external dispute resolution scheme

### F. Conclusive Evidence and Deemed Acceptance Clauses

**Statutory basis**: ACL ss 25(1)(g), (j) — unilateral breach determination; evidential
burden

**Why high risk**: Deemed acceptance clauses (e.g., "if you do not object within 24 hours,
you accept this") combined with the drafter holding superior information create significant
imbalance. _ACCC v Mable Technologies_ (2025): auto-approval of timesheets within 24 hours
without opt-out right — found unfair [VERIFY].

**Three-limb analysis:**

- _Significant imbalance_: The drafter, holding full information, sets short deadlines the
  other party may realistically miss.
- _Not reasonably necessary_: Business efficiency goals can be met with longer, more
  reasonable windows or by requiring affirmative confirmation rather than silence.
- _Detriment_: Financial loss from being treated as having accepted disputed amounts or
  terms; operational burden of monitoring all drafter communications.

**Remediation**:

- Avoid deemed acceptance clauses; require affirmative consent for material changes
- Where objection windows are operationally necessary, provide reasonable timeframes
  (not less than 30 days for financial matters; longer for complex review)
- Give the other party meaningful access to the information they need to assess the matter
  before the window expires

### G. IP Assignment Clauses

**Why high risk**: Broad IP assignment clauses requiring assignment of all IP (including
pre-existing background IP) or granting unlimited sub-licensing rights beyond the scope
of contracted deliverables create significant imbalance, particularly in technology,
creative services, and platform agreements.

**Three-limb analysis:**

- _Significant imbalance_: Transfer of IP rights far exceeding what is needed for the
  contracted service; the other party's broader business is constrained.
- _Not reasonably necessary_: For most engagements, a license to use deliverables is
  sufficient — assignment of background IP is not necessary to achieve the drafter's
  legitimate commercial purpose.
- _Detriment_: Loss of proprietary IP, inability to reuse work product in other engagements,
  exposure in subsequent dealings with third parties.

**Remediation**:

- Assign only specifically described _commissioned_ deliverables under the contract
- License (rather than assign) any pre-existing or background IP needed for the other
  party's use of the deliverables
- Narrow scope to specifically described works; avoid "all IP relating to the project"
  formulations
- Include compensation or credit if significant IP transfers are commercially justified

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates **silently** before delivering any output. If any gate fails, revise
before delivery.

| Gate           | Rule                                                                                                                                                   | Fail Action                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| **Source**     | Every statutory reference cites specific ACL or ASIC Act section numbers; every case reference includes parties, year, and court                       | Add citation or mark "[UNVERIFIED]" |
| **Format**     | All citations follow Australian legal citation conventions: _Case Name_ [Year] Court Code; ACL s XX(X)                                                 | Fix format                          |
| **Currency**   | Every cited provision checked for amendments or repeal, particularly post-9 November 2023 penalty regime commencement                                  | Flag "[CHECK CURRENCY]"             |
| **Domain**     | Analysis stays within the UCT scope — does not stray into unconscionable conduct, misleading conduct, or general contract law unless directly relevant | Remove or flag scope bleed          |
| **Confidence** | Uncertainty explicitly stated, not hidden; all case law references from memory marked [VERIFY]                                                         | Add confidence qualifier            |

### Self-Interrogation for UNFAIR (Tier 1 and Tier 2) Findings

For any clause classified UNFAIR at Tier 1 or Tier 2, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the three-limb analysis follow logically? Could
the advantaged party adduce evidence to rebut the "reasonably necessary" presumption?
Is there any case law supporting the term's validity? Would the ACCC/ASIC actually
prioritise this for enforcement?

**Pass 2 — Completeness**: Have all three limbs been independently assessed? Has the
transparency factor been considered? Have exempt term categories been checked? Has the
whole contract been read for counterbalancing terms that might reduce the imbalance?

**Pass 3 — Challenge**: What is the strongest argument for this clause being LIKELY FAIR
or BORDERLINE? Is there a defensible legitimate business justification? Under what
circumstances might a regulator exercise prosecutorial discretion and not pursue this?

### Confidence Scoring

| Level        | Range     | Meaning                                                                                      | Action                                       |
| ------------ | --------- | -------------------------------------------------------------------------------------------- | -------------------------------------------- |
| **Definite** | 0.95–1.0  | Well-settled by High Court or Full Federal Court authority on substantially identical clause | State classification with confidence         |
| **High**     | 0.80–0.94 | Strong Federal Court authority; clause closely matches decided cases                         | State classification with brief caveat       |
| **Probable** | 0.60–0.79 | Good arguments; analogous enforcement action; some uncertainty                               | State with reasoning and contra-indicators   |
| **Possible** | 0.40–0.59 | Genuinely uncertain — reasonable arguments both ways                                         | Flag for professional review with both sides |
| **Unlikely** | 0.0–0.39  | Weak basis for the classification; speculative                                               | Do not assert; flag "[UNCERTAIN]"            |

Apply confidence scores to each clause-level finding in the output. Where confidence is
below Probable, note the specific uncertainty.

### Glass Box Audit Trail

Append this YAML block to every review output:

```yaml
glass_box:
  skill_name: "legalcode-au-unfair-contract-terms"
  review_date: "[YYYY-MM-DD]"
  contract_name: "[Contract name or description]"
  contract_type: "[e.g., SaaS subscription terms, services agreement]"
  standard_form: "[Confirmed / Arguable / Rebuttable / Not assessed]"
  counterparty_profile: "[Consumer / Small business / Both / Unknown]"
  financial_product: "[Yes — ASIC Act applies / No — ACL applies / Partial]"
  regime_applicable: "[ACL ss 23-28 / ASIC Act ss 12BH-12BK / Both]"
  penalty_regime_applies: "[Yes — on or after 9 Nov 2023 / No — pre-penalty / Unknown]"
  clauses_reviewed: "[total number]"
  clauses_exempt: "[number exempt under s 26]"
  grey_list_matches: "[number matching s 25 categories]"
  findings:
    unfair_tier1: "[number]"
    unfair_tier2: "[number]"
    borderline_tier3: "[number]"
    borderline_tier4: "[number]"
    likely_fair: "[number]"
  enforcement_risk: "[CRITICAL / HIGH / MEDIUM / LOW]"
  legalcode_mcp: "[Connected / Not connected]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED — marked [VERIFY]]"
  confidence: "[HIGH / MEDIUM / LOW — rationale]"
  limitations:
    - "All case law citations from memory — mark [VERIFY] before relying"
    - "Penalty amounts subject to penalty unit adjustments — verify current amounts"
    - "[Any other scope limitations or assumptions]"
  reviewer: "AI-assisted — requires review by Australian-qualified consumer law lawyer"
```

---

## Prioritization Framework

After completing the clause-level analysis, present findings in priority order:

### Tier 1 — Must Fix (Before Any New Contract Is Made, Renewed, or Varied)

These findings pose the highest civil penalty exposure and/or match current ACCC/ASIC
enforcement priorities. Do not use contracts containing Tier 1 clauses until they are
revised. Each unfair term is a separate contravention — exposure is cumulative.

_Action_: Remove or substantially revise immediately. Seek legal advice. Document remediation.

### Tier 2 — Must Fix (High Priority)

These findings are clearly UNFAIR under the three-limb test but not current enforcement
priority. High exposure if the ACCC/ASIC enforcement priorities shift or a third-party
complaint is lodged.

_Action_: Revise in next contract update cycle. Document the planned fix timeline.

### Tier 3 — Should Fix (BORDERLINE — Arguable Enforcement Risk)

These findings are close calls — one or more limbs are arguable. Enforcement is possible
but less certain. The drafter can reduce risk by documenting the legitimate business
justification and narrowing the clause.

_Action_: Revise to improve defensibility. Prepare and file business justification evidence.

### Tier 4 — Monitor (BORDERLINE — Low Enforcement Priority)

These findings raise UCT considerations but have reasonable prospects of surviving challenge
with documented justification. Case law developments could shift the classification.

_Action_: Monitor case law. Maintain justification file. Review annually.

---

## Anti-Patterns

What NOT to do when using or applying the UCT regime or this skill:

1. **Relying on the absence of past enforcement** — The pre-November 2023 declaratory-only
   regime created a false sense of security. The 2023 amendments transformed UCT into a
   penalty regime. Past non-enforcement is not a guide to future enforcement.

2. **Treating "industry standard" as a defence** — The ACCC has explicitly stated that
   industry norm is not a defence to unfairness. Every franchise agreement reviewed was
   found to contain potentially unfair terms — the entire industry was equally exposed.

3. **Failing to rebut the statutory presumption with evidence** — The burden is on the
   advantaged party to prove the term is reasonably necessary. Courts have repeatedly found
   against parties that asserted necessity without adducing financial data, risk analysis,
   or expert evidence. Prepare the evidence file before, not after, a challenge arises.

4. **Treating transparency as a complete cure** — A clearly worded, prominently placed
   unfair term is still unfair. _Anderson v Kincumber_ confirmed this: detailed transparency
   did not cure substantive unfairness in a fee escalation formula. Transparency reduces
   risk at the margin — it is not an independent defence.

5. **Confusing "upfront price" exemption with contingent fee exemption** — The upfront
   price exemption (ACL s 26(1)(b)) covers only disclosed fixed prices set at contracting.
   Exit fees, default fees, late payment charges, and other event-triggered charges are not
   exempt and remain subject to the full UCT analysis.

6. **Assuming a "negotiated" contract is non-standard** — Minor modifications to peripheral
   terms do not make a contract non-standard if the core terms remain take-it-or-leave-it.
   The ACCC applies the s 27 six-factor test holistically; selective negotiation rights do
   not save a fundamentally non-negotiable contract structure.

7. **Relying on a foreign governing law clause** — A choice-of-law clause selecting a
   foreign jurisdiction does not oust the ACL. _Karpik v Carnival plc_ [2023] HCA 39
   confirmed that the ACL UCT regime applies to foreign entities operating in Australia
   regardless of contractual choice-of-law [VERIFY]. This is a high-stakes misunderstanding
   in cross-border contracts.

8. **Analyzing terms in isolation** — The three-limb test requires holistic assessment.
   A term that appears imbalanced may be counterbalanced by another provision (e.g., an
   unconditional exit right that accompanies a unilateral variation power may reduce the
   imbalance and detriment). Read the whole contract before classifying individual clauses.

9. **Ignoring the reversed burden on "reasonably necessary"** — The ACL places the burden
   on the advantaged party to prove necessity. This is not the plaintiff's burden to
   disprove — drafters must prepare and be ready to produce evidence of legitimate necessity,
   not merely assert it at the time of challenge.

10. **Classifying all asymmetric terms as unfair** — Not every one-sided term is unfair.
    The test requires _significant_ imbalance, _not_ reasonably necessary, _and_ detriment.
    Some asymmetry serves legitimate commercial purposes (e.g., an insurance notification
    obligation aligned with statutory policyholder duties — _Auto & General_ [2025] FCAFC).
    Over-classifying increases false positives and reduces the practical utility of the
    review.

11. **Missing the ASIC Act parallel regime** — Financial services and products are governed
    by the ASIC Act, not the ACL. The penalties differ (ASIC Act: $13.75M per contravention
    rather than $50M); the upfront price cap differs ($5M under the ASIC Act, none under the
    ACL). Misidentifying the applicable statute affects the penalty exposure calculation.

12. **Not accounting for insurance-specific UCT commencement date** — UCT applied to
    general insurance and life insurance contracts only from 5 April 2021 via the ICA s 15(2)
    amendment. Pre-2021 insurance contracts are not subject to UCT review even if used at
    scale.

13. **Forgetting that each term is a separate contravention** — When a contract contains
    five unfair terms and is used with 500,000 customers, the theoretical maximum exposure
    is five separate penalty calculations, each potentially up to $50M. The cumulative
    exposure from a high-volume standard form contract with multiple unfair terms can reach
    hundreds of millions of dollars. Always quantify exposure term by term.

14. **Drafting remediation as broad as the original problem** — Redlines that simply add
    "reasonable" or "material" to an otherwise unfair term often fail to address the
    underlying imbalance. Genuine remediation narrows the trigger, adds notice requirements,
    and provides the disadvantaged party with real protective rights (exit right, objection
    window, dispute mechanism).

15. **Forgetting to update internal enforcement and training** — A revised contract is only
    effective if staff responsible for applying and enforcing contracts know what changed and
    why. Training staff not to rely on removed terms is as important as revising the contract
    itself. Reliance on a declared-void term is itself prohibited conduct under the amended
    regime.

16. **Assuming compliance once reviewed** — UCT case law evolves rapidly. Findings that
    were LIKELY FAIR in 2023 may be BORDERLINE or UNFAIR by 2026 as courts, the ACCC, and
    ASIC continue to develop the regime. Build UCT review into the annual contract maintenance
    cycle, not just as a one-off exercise.

---

## Writing Standards

Before delivering any output, verify:

1. **Plain language**: Use plain English in all analysis and redlines. Avoid legalese in
   explanations to non-lawyers. Spell out acronyms on first use (ACL, ACCC, ASIC, UCT).

2. **Precision**: Name specific statutory provisions (e.g., "ACL s 24(1)(b)" not "the
   reasonably necessary test") and case names (e.g., "_ASIC v PayPal Australia_ [2024]
   FCA 762" not "the PayPal case").

3. **Active voice**: Use active constructions ("The term gives the supplier the right to...")
   rather than passive ("The right to... is given to the supplier...").

4. **No hedging on clear findings**: If a clause is plainly UNFAIR on the three-limb test,
   say so clearly. Do not soften clear findings to avoid conflict. Flag uncertainty where
   it genuinely exists; do not create false uncertainty.

5. **No false certainty**: Mark all case law from memory with [VERIFY]. Do not state penalty
   amounts without noting that penalty units are indexed and the amounts should be confirmed.

6. **Audience calibration**: Adjust the technical depth of the output to the user's context.
   An in-house legal team needs technical precision; a small business owner needs clear,
   jargon-free guidance on what to do.

7. **Completeness check before delivery**: Confirm all three limbs are addressed for every
   UNFAIR or BORDERLINE finding. Confirm the glass box audit trail is complete. Confirm
   the enforcement risk assessment is provided.

---

## External Tool Integration

### legalcode-mcp (Primary Legal Research Tool)

**With legalcode-mcp connected (preferred):**

- In Step 3, search for the current text of ACL ss 23–28 and any recent amendments
- Search for recent Federal Court and Full Federal Court UCT decisions
- Search for current ACCC and ASIC enforcement actions and guidance publications
- Verify penalty unit values (currently $313 per penalty unit as at January 2025 [VERIFY])
- Save relevant results to `/tmp/legalcode-uct-authority.md` for reference throughout review
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Direct the user to verify critical provisions at:
  - Federal Register of Legislation: legislation.gov.au
  - Federal Court decisions: fedcourt.gov.au or austlii.edu.au
  - ACCC guidance: accc.gov.au/business/selling-products-and-services/contracts
  - ASIC guidance: asic.gov.au/about-asic/what-we-do/our-role/laws-we-administer/unfair-contract-terms-law/

### ASIC Regulatory Reference

When ASIC Act jurisdiction applies, reference:

- **ASIC INFO 210**: Unfair contract term protections for consumers [VERIFY current URL]
- **ASIC INFO 211**: Unfair contract term protections for small businesses [VERIFY current URL]
- **ASIC REG 167C**: Class no-action position for institutional market contracts [VERIFY]

---

## Output Format Template

Structure the final output as follows:

---

```markdown
# Unfair Contract Terms Review

## [Contract Name]

### Jurisdiction: Australia (ACL / ASIC Act UCT Regime)

### Review Date: [DATE]

### Prepared for: [Client/User]

---

## Executive Summary

**Contract**: [Name and type]
**Standard form assessment**: [Confirmed / Arguable — basis stated]
**Counterparty profile**: [Consumer / Small business / Both]
**Applicable regime**: [ACL / ASIC Act / Both]
**Civil penalty regime applies**: [Yes — contracts on or after 9 Nov 2023 / No]
**Overall enforcement risk**: [CRITICAL / HIGH / MEDIUM / LOW]

**Findings summary**:

- UNFAIR — Tier 1 (Critical): [N] clauses
- UNFAIR — Tier 2 (High): [N] clauses
- BORDERLINE — Tier 3 (Medium): [N] clauses
- BORDERLINE — Tier 4 (Low): [N] clauses
- LIKELY FAIR: [N] clauses
- EXEMPT: [N] clauses

**Key messages**:

1. [Most important finding in one sentence]
2. [Second most important]
3. [Third most important]
4. [Recommended immediate actions]

---

## Gateway Assessment

### Standard Form Determination (ACL s 27)

[Six-factor analysis with finding]

### Counterparty Threshold (ACL ss 23–27)

[Consumer / Small business threshold analysis]

### Exempt Terms (ACL s 26)

[List exempt terms and basis]

---

## Clause Findings

### [Clause X] — [Clause heading from contract]

**Classification**: UNFAIR — Tier 1 | UNFAIR — Tier 2 | BORDERLINE — Tier 3 | BORDERLINE — Tier 4 | LIKELY FAIR | EXEMPT
**Confidence**: [Definite / High / Probable / Possible / Unlikely] ([score])
**Grey list match**: ACL s 25(1)([X]) — [description]

**Original clause**:

> [Verbatim extract]

**UCT Analysis**:

- _Limb 1 — Significant imbalance_: [SATISFIED / NOT SATISFIED] — [reasoning]
- _Limb 2 — Not reasonably necessary_: [SATISFIED / NOT SATISFIED] — [reasoning; reversed burden noted]
- _Limb 3 — Detriment_: [SATISFIED / NOT SATISFIED] — [reasoning]
- _Transparency_: [TRANSPARENT / PARTIAL / NOT TRANSPARENT] — [impact on finding]

**Civil penalty exposure** (if applicable):

- Per-contravention maximum: $50M / 3× benefit / 30% adjusted turnover (greater of)
- Estimated contracts affected: [if known]

**Recommended revision**:
```

[Revised clause text]

```

**Business justification evidence to prepare**:
[Guidance on what evidence to compile]

---

[Repeat for each finding]

---

## Industry Sector Considerations
[Applicable sector-specific analysis]

---

## Enforcement Risk Assessment
[CRITICAL / HIGH / MEDIUM / LOW with specific factors]

---

## Prioritized Action Plan

| Priority | Clause | Classification | Action | Timeline |
|---------|--------|---------------|--------|---------|
| 1 | [Clause] | UNFAIR — Tier 1 | [Remove / Revise] | Immediately |
| 2 | [Clause] | UNFAIR — Tier 2 | [Revise] | Before next renewal |
| ... | | | | |

---

## Compliance Program Recommendations
1. [Recommendation 1 — e.g., establish annual UCT contract review cycle]
2. [Recommendation 2 — e.g., train commercial and sales teams on prohibited conduct]
3. [Recommendation 3 — e.g., document business justification file for retained clauses]
4. [Recommendation 4 — e.g., implement proactive renewal notification system]

---

[Glass Box Audit Trail — YAML block]
```

---

## Localization Notes

The ACL applies uniformly in all Australian states and territories — there is no
state-by-state variation in the UCT regime. However, note:

- **State enforcement agencies**: The ACCC enforces the ACL nationally; state/territory
  consumer protection agencies (e.g., NSW Fair Trading, Consumer Affairs Victoria,
  Queensland Office of Fair Trading) have concurrent enforcement jurisdiction and may
  initiate their own actions.
- **Industry-specific codes**: Some sectors have mandatory industry codes (franchising,
  energy, telecommunications) under the Competition and Consumer Act 2010 that interact
  with the UCT regime. These codes may impose additional obligations beyond the UCT.
- **Financial services**: ASIC Act jurisdiction is federal — no state variation.
- **Insurance**: The Insurance Contracts Act 1984 (Cth) is a federal statute — UCT applies
  uniformly to in-scope insurance contracts nationally.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on:

**Primary legal authority** (all [VERIFY] unless independently confirmed):

- _Competition and Consumer Act 2010_ (Cth), Schedule 2 (ACL), ss 9, 23–28
- _Australian Securities and Investments Commission Act 2001_ (Cth), ss 12BH–12BK
- _Treasury Laws Amendment (More Competition, Better Prices) Act 2022_ (Cth)
- _Insurance Contracts Act 1984_ (Cth), s 15(2) (amended 5 April 2021)

**Key cases** (all [VERIFY] against authoritative sources):

- _Karpik v Carnival plc_ [2023] HCA 39 (Ruby Princess — High Court UCT)
- _ASIC v PayPal Australia Pty Ltd_ [2024] FCA 762
- _ASIC v Auto & General Insurance Company Limited_ [2025] FCAFC 76
- _Tomasso v IG Markets Ltd_ [2025] WASC 338
- _ACCC v Mable Technologies Pty Ltd_ (2025 undertaking — first expanded regime enforcement)
- _ACCC v Fujifilm Business Innovation Australia Pty Ltd_ [2022] FCA
- _ACCC v JJ Richards & Sons Pty Ltd_ [2017] FCA
- _ACCC v ByteCard Pty Ltd_ [2013] FCA
- _ACCC v Chrisco Hampers Australia Ltd_ [2015] FCA 1204
- _Anderson v Kincumber Nautical Village Pty Ltd_ [2025] NSWCAT
- _AghaeiRad v Plus500AU Pty Ltd_ [2025] FCA

**Regulatory guidance** (verify current versions at accc.gov.au and asic.gov.au):

- ACCC 2025–26 Compliance and Enforcement Priorities
- ACCC industry UCT reviews (franchising, energy, telecommunications, waste management)
- ASIC INFO 210 (consumer UCT protections) and INFO 211 (small business UCT protections)

**Quality standard**: Calibrated to the Legalcode gold standard (legalcode-contract-review).
Synthesized with the structural and prompt engineering quality frameworks of the Legalcode
skill library. Related Australian skills: `legalcode-au-consumer-law-compliance`,
`legalcode-franchise-agreement-review-au`.
