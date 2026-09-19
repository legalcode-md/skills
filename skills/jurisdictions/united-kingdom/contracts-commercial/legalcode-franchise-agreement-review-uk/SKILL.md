---
name: legalcode-franchise-agreement-review-uk
description: Review franchise agreements for UK operations under the self-regulatory and common law framework
  — analyse against BFA Code of Ethics disclosure and fair dealing standards, screen for unfair contract
  terms under UCTA 1977 (s 3 reasonableness test for standard terms), evaluate post-termination restraint
  of trade enforceability using the *Dwyer v Fredbar* [2022] EWCA Civ 889 framework (legitimate interest
  + proportionality + inequality of bargaining power), assess good faith obligations in relational contracts
  per *Yam Seng* [2013] and the Braganza duty of rational decision-making, review misrepresentation exposure
  under the Misrepresentation Act 1967 (s 3 reasonableness for non-reliance clauses), analyse competition
  law compliance under the UK VABEO (SI 2022/516) including RPM hardcore restrictions and online sales
  channel rules, evaluate IP licence structure under Trade Marks Act 1994 (s 28), and assess penalty clause
  enforceability under *Cavendish Square v Makdessi* [2015].
metadata:
  jurisdiction: United Kingdom
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review franchise agreements for UK operations under the self-regulatory and common law framework — analyse against BFA Code of Ethics disclosure and fair dealing standards, screen for unfair contract terms under UCTA 1977 (s 3 reasonableness test for standard terms), evaluate post-termination restraint of trade enforceability using the *Dwyer v Fredbar* [2022] EWCA Civ 889 framework (legitimate interest + proportionality + inequality of bargaining power), assess good faith obligations in relational contracts per *Yam Seng* [2013] and the Braganza duty of rational decision-making, review misrepresentation exposure under the Misrepresentation Act 1967 (s 3 reasonableness for non-reliance clauses), analyse competition law compliance under the UK VABEO (SI 2022/516) including RPM hardcore restrictions and online sales channel rules, evaluate IP licence structure under Trade Marks Act 1994 (s 28), and assess penalty clause enforceability under *Cavendish Square v Makdessi* [2015]. GREEN/YELLOW/RED classification with confidence scoring and Glass Box audit trail. Use when reviewing franchise agreements governed by English or Scots law, or where the franchise will operate in the UK. Jurisdiction-specific variant of legalcode-franchise-agreement-review.


# Legalcode Franchise Agreement Review — United Kingdom

> **Disclaimer**: This skill provides a framework for AI-assisted franchise agreement review
> under UK law. It does not constitute legal advice. All outputs require review by a UK-
> qualified solicitor experienced in franchise law before reliance. The UK has **no franchise-
> specific statute** — franchise agreements are governed by general contract law, competition
> law, and IP law. The legal landscape is shaped primarily by case law, which evolves
> continuously. The Vodafone franchise dispute has prompted government review of franchise
> legislation — potential reforms may be forthcoming. Statutory and case law references cited
> from memory carry hallucination risk — verify against authoritative sources (UK legislation,
> court records, CMA/IPO guidance) before relying on them.

---

## Purpose and Scope

This skill reviews franchise agreements for UK compliance, navigating a regime that is
fundamentally different from the US registration model or the Australian mandatory code.
The UK relies on self-regulation through the BFA Code of Ethics and general principles of
contract, competition, and IP law. This makes franchise agreement review in the UK more
nuanced — there is no statutory checklist, but there are powerful common law doctrines and
competition law constraints.

**Covers:**

- BFA Code of Ethics compliance (for BFA member franchisors) and best practice standards
- UCTA 1977 unfair terms screening (s 3 reasonableness test for standard form contracts)
- Restraint of trade analysis under common law, calibrated by _Dwyer v Fredbar_ [2022]
- Good faith / Braganza duty analysis for relational contracts (_Yam Seng_ [2013])
- Misrepresentation Act 1967 exposure and non-reliance clause enforceability
- Competition Act 1998 / UK VABEO (SI 2022/516) compliance
- Trade Marks Act 1994 IP licence structure review
- Penalty clause enforceability under _Cavendish Square v Makdessi_ [2015]
- Trading Schemes Act 1996 applicability (multi-tier franchise structures)
- GREEN / YELLOW / RED deviation classification with confidence scoring
- Glass Box audit trail

**Does not:**

- Draft new franchise agreements from scratch
- Provide legal advice or replace qualified UK franchise counsel
- Cover non-UK franchise law (see `legalcode-franchise-agreement-review` for general;
  jurisdiction-specific variants for US-CA, AU, EU-FR, Nordics)
- Provide employment law advice beyond franchise-specific provisions
- Cover Scots law variations in detail (note material differences where relevant)

**Related skills:**

- `legalcode-franchise-agreement-review` — General multi-jurisdictional franchise review
- `legalcode-franchise-agreement-review-us-ca` — California focus
- `legalcode-franchise-agreement-review-au` — Australia focus
- `legalcode-contract-review` — General commercial contract review
- `legalcode-nda-triage` — NDA review

---

## Jurisdiction and Governing Law

### Why the UK Requires a Dedicated Skill

The UK franchise landscape is fundamentally different from jurisdictions with statutory
franchise regulation:

1. **No franchise-specific statute**: No registration, no mandatory disclosure period, no
   statutory relationship protections. Franchisors are free to structure agreements as they
   choose, subject only to general law.
2. **Self-regulatory model**: The BFA Code of Ethics provides voluntary standards, but only
   approximately a minority of UK franchise systems are BFA members.
3. **Common law dominance**: Franchise disputes are resolved under general contract law
   principles — good faith, restraint of trade, misrepresentation — which require case law
   analysis rather than statutory compliance.
4. **Post-_Dwyer v Fredbar_ landscape**: The 2022 Court of Appeal decision fundamentally
   reshaped the enforceability analysis for franchise non-competes, introducing inequality
   of bargaining power as a key factor.
5. **UK VABEO divergences**: Post-Brexit, the UK's competition law treatment of vertical
   agreements diverges from the EU VBER in material ways (retail parity, shared exclusivity).
6. **Potential reform**: The Vodafone franchise scandal has prompted government review of
   franchise legislation — PM Starmer pledged review in January 2026.

### England & Wales vs. Scotland vs. Northern Ireland

This skill primarily addresses **English law** (which also applies in Wales). Key
differences in other UK jurisdictions:

- **Scotland**: Separate legal system. Restraint of trade doctrine is similar but not
  identical. Scottish courts have their own precedent. UCTA 1977 applies with modifications.
  Contract law follows common law principles but with distinct traditions.
- **Northern Ireland**: Generally follows English common law but with own court system.

Where material differences exist, they are noted. For franchise agreements governed by Scots
law, consider supplementing this analysis with Scots law-specific advice.

### No Registration Requirement

Unlike the US (state registration), France (Loi Doubin), or Australia (Franchising Code),
the UK has **no requirement to register franchise offerings** or provide pre-contractual
disclosure as a matter of law. This means:

- There is no government body overseeing franchise sales
- There is no mandatory waiting period before signing
- There is no mandatory cooling-off period (except under Trading Schemes Act for multi-tier
  structures)
- Pre-contractual disclosure is a matter of good practice, not legal obligation
- The absence of statutory protection places greater importance on common law doctrines

---

## Regulatory Framework

### BFA Code of Ethics

The BFA Code is based on the European Code of Ethics for Franchising (EFF). BFA membership
is voluntary — approximately 1,009 franchise systems operate in the UK (2024 survey), with
BFA members representing a significant but not majority share.

**Key BFA Code provisions:**

**Disclosure:**

- Full and accurate written disclosure of all information material to the franchise
  relationship
- Must be provided "within a reasonable time" prior to execution of any binding document
- Must include: up-to-date financials, operations manual details, franchise offer specifics,
  franchisor's history
- Prospective franchisees must receive a copy of the Code itself

**Fair dealing:**

- "Fairness shall characterise all dealings between a franchisor and its franchisees"
- Written notice of contractual breach required
- Reasonable time to remedy breach (where appropriate)

**Recruitment:**

- Advertising must be "free of ambiguity and misleading statements"
- Franchisors must recruit only franchisees who possess "basic skills, education, personal
  qualities and adequate capital to succeed"

**Franchisor obligations:**

- Must have operated business concept successfully for a reasonable time in at least one
  pilot unit before franchising
- Must be the owner (or have legitimate rights) of a trade name, trademark, or other
  distinguishing identification
- Must provide initial training and continuing assistance for the duration of the agreement

**REVIEW CHECKLIST — BFA Compliance:**

- [ ] Is the franchisor a BFA member? → If yes, Code is binding; if no, use as best practice
      benchmark
- [ ] Was disclosure provided? How much time before signing? → "Reasonable time" is vague;
      best practice is 14+ days
- [ ] Does disclosure include financials, operational details, franchise offer specifics?
- [ ] Was the BFA Code provided to the prospective franchisee?
- [ ] Does the agreement reflect BFA fair dealing standards?

### Trading Schemes Act 1996 / Trading Schemes Regulations 2017

Applies only to **multi-tier franchise structures** where franchisees are encouraged to
appoint sub-franchisees. Where applicable:

- Specified information must be provided when marketing the franchise
- **14-day cooling-off period** after signing (or 90 days for sub-franchise agreements)
- Restrictions on timing of certain payments
- Exemption applies if all network members are VAT-registered

**REVIEW CHECKLIST:**

- [ ] Is this a multi-tier franchise model? → If yes, Trading Schemes Act may apply
- [ ] Are franchisees encouraged/incentivised to recruit sub-franchisees?
- [ ] If applicable, is a 14-day cooling-off period provided?
- [ ] Are all network members VAT-registered? (Exemption condition)

---

## Unfair Contract Terms Act 1977 (UCTA)

### Application to Franchise Agreements

UCTA applies to franchise agreements as **business-to-business standard form contracts**.

**Key provisions:**

| Section    | Rule                                                                                                          | Franchise Application                                                |
| ---------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **s 2(1)** | Cannot exclude liability for death or personal injury from negligence                                         | Absolute — any such exclusion is void                                |
| **s 2(2)** | Cannot exclude liability for other loss from negligence unless "reasonable"                                   | Reasonableness test applies                                          |
| **s 3**    | Where contracting on written standard terms, cannot exclude/restrict liability for breach unless "reasonable" | **Critical for franchise agreements** — almost all are standard form |
| **s 11**   | Reasonableness test: "fair and reasonable to be included having regard to the circumstances"                  | Case-by-case analysis                                                |

**s 11 Reasonableness factors:**

- Equality of bargaining powers between the parties
- How practical it was to obtain independent legal advice
- Clarity and preciseness of the clause
- Whether the term was individually negotiated or standard boilerplate
- Burden of proof falls on the party seeking to rely on the exclusion

**REVIEW CHECKLIST — UCTA Screening:**

- [ ] Is the franchise agreement a **standard form** (not individually negotiated)? → If yes,
      s 3 applies to all exclusion and limitation clauses
- [ ] Does the agreement exclude liability for franchisor's breach of contract? → Must pass
      s 11 reasonableness test
- [ ] Does the agreement contain a non-reliance clause? → Must pass s 11 (see
      Misrepresentation Act s 3 below)
- [ ] Does the agreement contain a cap on franchisor's liability? → Assess reasonableness
- [ ] Does the agreement exclude consequential or indirect damages? → Common but must be
      reasonable
- [ ] Was the franchisee given opportunity to take independent legal advice? → Key
      reasonableness factor

---

## Good Faith and the Braganza Duty

### Good Faith in Franchise Agreements

English law does not recognise a **general** implied duty of good faith in all contracts.
However, franchise agreements are strong candidates for implied good faith obligations
because they are "relational contracts."

**_Yam Seng Pte Ltd v ITC Ltd_ [2013] EWHC 111 (QB):**

- Leggatt J held that good faith can be implied into a "relational contract"
- **Franchise agreements were explicitly cited** as examples of relational contracts
- Standard: conduct would be regarded as **"commercially unacceptable by reasonable and
  honest people"**
- Implied duties include: duty of honest dealing, duty not to act in a way that would
  destroy the contract's purpose

### The Braganza Duty

**_Braganza v BP Shipping Ltd_ [2015] UKSC 17:**

- When one party makes decisions affecting both parties with differing interests, the
  decision-maker must not take into account **irrelevant considerations** or fail to take
  into account **relevant ones**
- This is a duty of **rationality**, not a general duty of good faith

**Application to franchising:**

| Decision                         | Braganza Duty Applies?    | Basis                                             |
| -------------------------------- | ------------------------- | ------------------------------------------------- |
| Termination for breach           | Yes — must be rational    | _Hunters v Brybond_ [2022]                        |
| Refusal to approve transfer      | Likely yes                | Discretionary power affecting franchisee          |
| Refusal to renew                 | Depends on contract terms | _Winkworth v Goble_ [2023] — clear terms enforced |
| Territory modification           | Likely yes                | Affects franchisee's commercial position          |
| Operations manual changes        | Likely yes                | Discretionary power with material impact          |
| Fee increases (if discretionary) | Likely yes                | Unilateral power affecting both parties           |

**Key case law:**

- **_Hunters Franchising Ltd v Brybond Ltd_ [2022] EWHC 3195:** Braganza duty recognised in
  master franchise context. Franchisor acted consistently with policy of not approving
  franchises that would adversely affect existing franchisees — duty not breached. [VERIFY]
- **_Winkworth Franchising Ltd v Goble_ [2023] EWHC 2883:** Franchisor entitled to refuse
  renewal where franchisee failed to comply with clear contractual requirements (annual
  accounts). No additional requirement of "materiality" implied. [VERIFY]

**REVIEW CHECKLIST — Good Faith / Braganza:**

- [ ] Does the agreement contain discretionary powers for the franchisor? → Each should be
      assessed against Braganza duty
- [ ] Does the agreement exclude or limit good faith obligations? → YELLOW (may be valid
      but risky; contractual exclusion may face UCTA challenge)
- [ ] Does the agreement give franchisor sole discretion on material matters (termination,
      transfer, territory)? → YELLOW to RED (Braganza duty likely applies regardless)
- [ ] Are franchisor decisions subject to reasonableness or rationality standards? → GREEN
      if present

---

## Restraint of Trade — _Dwyer v Fredbar_ Framework

### The Post-_Dwyer_ Landscape

**_Dwyer v Fredbar Ltd_ [2022] EWCA Civ 889** is the leading modern UK franchise non-compete
case and fundamentally reshaped the enforceability analysis.

**Facts:** Dwyer (Drain Doctor franchisor) granted a 10-year franchise to Fredbar (Mr
Bartlett). The franchise agreement contained a 12-month post-termination non-compete within
the franchise territory and a 5-mile radius. Bartlett invested his life savings; the
franchise was unprofitable from year one; COVID-19 further disrupted operations.

**Court of Appeal held:**

1. The **12-month restriction was unreasonable** because:
   - **Inequality of bargaining power**: Franchisee had no negotiating leverage
   - **No proportionality to goodwill**: Same covenant whether franchise ran 1 year or 10
     years; little goodwill had accumulated because franchise terminated early
   - **Franchisee's vulnerability**: Dwyer knew Bartlett was investing all savings and risked
     losing the family home
   - **Not specifically discussed**: The non-compete had not been brought to the franchisee's
     attention or negotiated

2. **Severance (blue-pencil) was not available**: The unreasonable part could not be severed
   from the rest of the covenant. The court refused to rewrite the covenant.

3. The **Braganza duty applied** to the termination decision.

### Restraint of Trade Analysis Framework

**Step 1: Is there a legitimate interest to protect?**

| Interest                            | Protectable? | Franchise Context                                            |
| ----------------------------------- | ------------ | ------------------------------------------------------------ |
| Goodwill                            | Yes          | Goodwill built by franchisee using franchisor's brand/system |
| Know-how / confidential information | Yes          | Franchisor's operating methods, customer data                |
| Customer connections                | Yes          | Relationships built under franchise brand                    |
| Network integrity                   | Arguable     | Protecting other franchisees and the system                  |
| Investment in training              | Weak         | Unlikely to justify restraint alone                          |

**Step 2: Is the restraint proportionate?**

Post-_Dwyer_ proportionality factors:

| Factor                                 | Analysis                                                                                                                                                                                                              |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Duration**                           | 6-12 months typical range; 12 months at outer limit; beyond requires strong justification. Duration should be proportionate to goodwill actually built — same covenant for 1-year and 10-year franchise is vulnerable |
| **Geographic scope**                   | Must correspond to franchise territory. A local territory restriction is easier to justify than a national ban                                                                                                        |
| **Activity scope**                     | Must be limited to genuinely competing activities. "Any business" is vulnerable; "business of the same or similar nature" is standard                                                                                 |
| **Bargaining power**                   | Post-_Dwyer_: inequality of bargaining power is a significant factor even in commercial franchise agreements. First-time franchisees investing life savings are in a position more analogous to employees             |
| **Attention drawn to covenant**        | Was the restraint specifically discussed and explained? If buried in boilerplate → greater vulnerability                                                                                                              |
| **Proportionality to actual goodwill** | Did the franchisee build goodwill warranting the restraint? Early termination = less goodwill = less justification                                                                                                    |

**Step 3: Severance available?**

_Dwyer_ confirmed that courts will **not** rewrite unreasonable covenants. Severance (blue-
pencil) is only available if:

- The unreasonable part is **clearly severable** from the reasonable part
- Severance does not change the fundamental character of the covenant
- The remaining covenant makes sense as a standalone restriction

**REVIEW CHECKLIST — Restraint of Trade:**

- [ ] Is there a post-termination non-compete? → Analyse under framework above
- [ ] What is the duration? → >12 months → RED; 12 months → YELLOW (vulnerable per _Dwyer_);
      6 months → GREEN to YELLOW
- [ ] Is scope geographically proportionate to territory? → National ban for local franchise
      → RED
- [ ] Does activity scope match franchise business specifically? → Overly broad → YELLOW
- [ ] Was the covenant specifically discussed and negotiated? → If not → vulnerability factor
- [ ] Does covenant vary with franchise duration (sliding scale)? → If not → vulnerability
      factor per _Dwyer_
- [ ] Is severance possible if broadest restraint fails? → Assess blue-pencil eligibility
- [ ] Is there a non-solicitation of customers clause? → More likely enforceable than
      non-compete
- [ ] Is there a confidentiality obligation? → Generally enforceable (not subject to restraint
      of trade doctrine)

### Recommended Post-_Dwyer_ Non-Compete Structure

Based on _Dwyer v Fredbar_, a robust UK franchise non-compete should:

1. **Vary duration with franchise length**: e.g., 3 months if franchise operated <2 years,
   6 months if 2-5 years, 12 months if 5+ years
2. **Limit geography to franchise territory** (plus reasonable buffer)
3. **Limit activity to specifically defined competing business** (not "any business")
4. **Be specifically drawn to franchisee's attention** and discussed
5. **Include cascading provisions** (if 12 months is unreasonable, 6 months applies; if
   20km is unreasonable, 10km applies)
6. **Separate non-solicitation** from non-compete (non-solicitation is more likely enforceable)

---

## Misrepresentation Act 1967

### Application to Franchise Sales

Franchise sales involve extensive pre-contractual representations about profitability,
support, territory, and brand strength. The Misrepresentation Act 1967 provides the
franchisee's primary remedy for false pre-contractual statements.

### Types of Misrepresentation

| Type           | Mental State                                            | Remedies                                                                                               |
| -------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Fraudulent** | Knowingly false, without belief in truth, or recklessly | Rescission + damages (all foreseeable losses). Cannot be excluded.                                     |
| **Negligent**  | No reasonable grounds for belief                        | Rescission + damages (same measure as fraud unless s 2(2) discretion). Excludable if reasonable (s 3). |
| **Innocent**   | Honest and reasonable belief                            | Rescission or damages in lieu (s 2(2)). Excludable if reasonable (s 3).                                |

### Non-Reliance and Entire Agreement Clauses (s 3)

**Section 3** (as substituted by UCTA s 8): Any clause limiting or excluding liability for
misrepresentation or excluding any remedy is enforceable **only if it satisfies the UCTA
reasonableness test**.

**Key cases:**

- **_Papa Johns v Doyley_**: Non-reliance clause **failed** reasonableness test because of
  inequality of bargaining power, non-negotiable agreement, and boilerplate not specifically
  drawn to franchisee's attention. [VERIFY]
- **_FoodCo UK LP v Henry Boot Developments Ltd_ [2010] EWHC 358**: Non-reliance clause
  **upheld** as reasonable in a commercial context; it excluded liability for innocent and
  negligent misrepresentation, confining claims to fraud. [VERIFY]
- **_Peart Stevenson Associates Ltd v Holland_**: Franchisor awarded £20,000 for breach;
  franchisee counterclaimed £170,000 for misleading representations about projected
  turnover/profit — significantly exceeding the franchisor's recovery. [VERIFY]

**Critical principle**: Non-reliance clauses **cannot** exclude liability for **fraudulent**
misrepresentation — any such exclusion is void as a matter of public policy.

**REVIEW CHECKLIST — Misrepresentation:**

- [ ] Does agreement contain a non-reliance clause? → Must satisfy UCTA s 11 reasonableness
- [ ] Does agreement contain an entire agreement clause? → Assess whether it limits
      misrepresentation remedies
- [ ] Does either clause purport to exclude liability for fraud? → **RED** (unenforceable)
- [ ] Was the non-reliance clause specifically drawn to franchisee's attention? → Key
      reasonableness factor
- [ ] Were financial projections or earnings representations made pre-contract? → Document
      and assess misrepresentation risk
- [ ] Does the FDD/disclosure document make representations about earnings? → Compare to
      actual franchise performance data

---

## Competition Law — UK VABEO

### Competition Act 1998

**Chapter I Prohibition (s 2)**: Prohibits agreements that may affect UK trade and prevent,
restrict, or distort competition.

**Chapter II Prohibition (s 18)**: Prohibits abuse of dominant position.

### UK VABEO (SI 2022/516) — Safe Harbour

The Vertical Agreements Block Exemption Order provides a safe harbour for franchise
agreements from the Chapter I prohibition. Effective 1 June 2022, expires 31 May 2028.

**Conditions for exemption:**

- Both parties have market shares of **less than 30%** on their respective markets
- No "hardcore" restrictions

**Hardcore restrictions (franchise-relevant):**

| Restriction                                               | Status                   | Consequence                                                                                                           |
| --------------------------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| **Resale price maintenance (RPM)**                        | Hardcore — prohibited    | Recommended/maximum prices OK; minimum/fixed prices prohibited                                                        |
| **Active sales restrictions** outside allocated territory | Generally permissible    | Can restrict franchisee from actively soliciting in other territories                                                 |
| **Passive sales restrictions**                            | Hardcore — prohibited    | Cannot prevent franchisee from fulfilling unsolicited orders from outside territory                                   |
| **Online sales channel ban**                              | Hardcore — prohibited    | Cannot prevent effective use of internet as sales channel                                                             |
| **Wide retail parity obligations**                        | Hardcore (UK divergence) | Cannot require franchisee to offer same/better prices through all channels                                            |
| **Trademark bidding restrictions**                        | May be hardcore          | Banning franchisee from bidding on franchisor trademarks in search engines may be treated as online sales restriction |

**Key UK-EU post-Brexit divergences:**

| Issue                  | UK VABEO                                | EU VBER                                   |
| ---------------------- | --------------------------------------- | ----------------------------------------- |
| Wide retail parity     | **Hardcore**                            | Only across-platform parity is non-exempt |
| Shared exclusivity     | No prescribed max; proportionality test | Max 5 exclusive distributors              |
| Duration               | Expires 31 May 2028                     | Expires 31 May 2034                       |
| CMA information powers | Specific 10-day response power          | No equivalent                             |

**REVIEW CHECKLIST — Competition Law:**

- [ ] Does agreement impose minimum or fixed resale prices? → **RED** (RPM — hardcore)
- [ ] Does agreement restrict passive sales outside territory? → **RED** (hardcore)
- [ ] Does agreement restrict online sales? → **RED** (hardcore unless narrowly tailored)
- [ ] Does agreement require wide retail parity? → **RED** (UK-specific hardcore)
- [ ] Does agreement restrict trademark bidding on search engines? → YELLOW to RED
- [ ] Are both parties below 30% market share? → If above, VABEO safe harbour not available
- [ ] Does agreement contain recommended pricing? → GREEN (permissible)
- [ ] Does agreement restrict active sales outside territory? → GREEN (generally permissible)

---

## Intellectual Property — Trade Marks Act 1994

### Trademark Licensing in Franchise Context (s 28)

**Key provisions:**

| Section     | Rule                                                                                                                        | Franchise Application                                    |
| ----------- | --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **s 28**    | Statutory framework for trademark licensing                                                                                 | Franchise IP licence must comply                         |
| **s 28(4)** | No statutory right to sub-licence; only if head licence provides                                                            | Master franchise must expressly permit sub-licensing     |
| **s 30**    | Licensee can call on proprietor to take infringement proceedings; if proprietor fails within 2 months, licensee may proceed | Franchise agreement should address infringement response |

**Quality control requirements:**

- Trademark owner must exercise **adequate control** over licensee use
- Failure to control quality may dilute the mark
- Franchise agreements should include: inspection rights, compliance standards, right to
  approve/disapprove products/services

**Registration:**

- Until an application to register the licence has been made with the IPO, the licence is
  ineffective against third parties acquiring conflicting interests, and the licensee does
  not have s 30/31 protections
- Best practice: register all trademark licences with the IPO

**REVIEW CHECKLIST — IP:**

- [ ] Is the trademark licence separate from (or clearly identifiable within) the franchise
      agreement? → Best practice: separate IP licence clause
- [ ] Is the licence exclusive or non-exclusive? → Best practice for franchise: non-exclusive
- [ ] Does the agreement include quality control provisions? → If absent → YELLOW (risk of
      mark dilution)
- [ ] Is the licence registered (or provision made for registration) with the IPO? →
      If not → YELLOW
- [ ] Does the agreement address IP infringement response? → If silent → YELLOW
- [ ] Does the agreement address domain names and social media? → If silent → YELLOW
      (ownership should be specified)
- [ ] Does the agreement address franchisee-developed IP? → If silent → YELLOW
- [ ] Who owns customer databases? → Should be specified clearly

---

## Penalty Clauses — _Cavendish Square v Makdessi_ [2015]

### The Modern Test

The Supreme Court in _Cavendish Square Holding BV v Talal El Makdessi_ [2015] UKSC 67
replaced the old "genuine pre-estimate of loss" test:

**New test**: Whether the provision is a **secondary obligation** which imposes a detriment
**out of all proportion** to any **legitimate interest** of the innocent party in enforcement
of the primary obligation.

**Application to franchise agreements:**

| Common Provision                                   | Penalty Risk | Analysis                                                                      |
| -------------------------------------------------- | ------------ | ----------------------------------------------------------------------------- |
| Liquidated damages for breach of non-compete       | Low-medium   | If proportionate to legitimate interest in protecting goodwill                |
| Accelerated royalties on termination               | Medium       | Must relate to legitimate interest, not punishment                            |
| Forfeiture of deposit/franchise fee on termination | Medium-high  | Must be proportionate; forfeiture of entire fee for minor breach likely penal |
| Transfer fee as percentage of sale price           | Low          | Generally a primary obligation, not triggered by breach                       |
| Late payment interest                              | Low          | Standard commercial practice if rate is reasonable                            |
| De-identification costs charged to franchisee      | Low-medium   | If costs are genuine and proportionate                                        |

**REVIEW CHECKLIST — Penalty Clauses:**

- [ ] Are there liquidated damages provisions? → Assess proportionality to legitimate interest
- [ ] Is the franchise fee forfeited on early termination? → If for any breach (including
      minor) → RED (likely penal)
- [ ] Are accelerated royalties charged on termination? → Assess justification and
      proportionality
- [ ] Is there a minimum payment on early termination? → Assess against _Makdessi_ test
- [ ] Are costs of de-identification/rebranding charged to franchisee? → YELLOW if
      disproportionate

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points.

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

### Step 1: Accept Agreement and Determine Context

**⟁ CLARIFY** — UK franchise context:

1. **Is the franchisor a BFA member?** → If yes, BFA Code is binding and provides additional
   benchmarks. If no, use BFA Code as best practice only.
2. **Which side are you on?** Prospective Franchisee / Existing Franchisee / Franchisor
3. **Governing law?** English law / Scots law / Northern Irish law → material differences
   may apply
4. **Franchise model?** Single-unit / Multi-unit / Master franchise / Area development
5. **Industry?** Food & beverage / Retail / Services / Estate agency / Automotive / Other
6. **Deal stage?** Pre-signing / Post-signing / Renewal / Transfer / Dispute
7. **Is this a multi-tier structure?** → If yes, Trading Schemes Act may apply
8. **Risk tolerance?** Conservative / Pragmatic / Deal-centric

### Step 2: Pre-Contractual Disclosure Assessment

**⟁ CLARIFY** — What disclosure was provided?

1. **Full BFA-standard disclosure**: Assess completeness and timing
2. **Partial disclosure**: Identify gaps against BFA best practice
3. **No formal disclosure**: Flag risk. What representations were made? (emails, meetings,
   brochures, financial projections)
4. **Master franchise**: Was disclosure provided at both levels?

Even without a legal disclosure requirement, document what was disclosed and how, as this
affects misrepresentation risk.

### Step 3: Clause-by-Clause Analysis (UK-Calibrated)

Apply the 16-category framework from the general franchise review skill with UK-specific
calibration. Categories with material UK-specific variation:

#### Category 1: Initial Franchise Fee — UK Calibration

- No statutory disclosure requirement for fees, but BFA best practice requires full disclosure
- No escrow or financial assurance requirements (unlike US/AU)
- Fee forfeiture on termination must pass _Makdessi_ penalty test
- Trading Schemes Act: if applicable, timing restrictions on payments may apply

#### Category 2: Ongoing Royalties and Fees — UK Calibration

- Late payment interest: must be proportionate (_Makdessi_)
- Minimum royalty provisions: assess reasonableness
- Unilateral fee increase power: UCTA s 3 reasonableness challenge + Braganza duty

#### Category 3: Territory — UK Calibration

- **Competition law critical**: VABEO compliance required
- Active sales restrictions outside territory: generally permissible
- Passive sales restrictions: **hardcore** — cannot prevent unsolicited orders from outside
  territory
- Online sales: cannot prevent effective use of internet as sales channel
- Wide retail parity obligations: **hardcore** under UK VABEO (divergence from EU)
- Non-derogation from grant: if franchisor grants territory then undermines it, franchisee
  may terminate early

#### Category 4: IP and Trademark — UK Calibration

- Trade Marks Act 1994 s 28 compliance
- Quality control provisions essential to maintain mark
- Licence registration with IPO recommended
- Sub-licensing requires express provision (s 28(4))
- Domain name and social media ownership must be specified

#### Category 5: Quality Control / Operations Manual — UK Calibration

- Unilateral variation of operations manual: UCTA s 3 challenge if manual is incorporated
  by reference
- Braganza duty may apply to franchisor's discretion in changing standards
- Material changes should require notice and consultation

#### Category 9: Term and Renewal — UK Calibration

- No statutory renewal protections (unlike CFRA §20025 or Australian Code)
- Franchisor's discretion on renewal subject to Braganza duty if contractual
- _Winkworth v Goble_: clear renewal conditions will be enforced as written
- Best practice: clear renewal criteria, reasonable notice, predictable conditions

#### Category 10: Transfer — UK Calibration

- No statutory transfer protections
- Consent "not to be unreasonably withheld" is best practice but not required
- "Sole discretion" consent: subject to Braganza duty (must be rational)
- BFA best practice: reasonable transfer conditions

#### Category 11: Termination — UK Calibration

- No statutory good cause requirement
- Good faith / Braganza duty may constrain arbitrary termination
- Termination for trivial breach: UCTA s 3 challenge (unreasonable for standard terms)
- BFA Code: written notice and reasonable cure period
- Penalty clauses triggered by termination must pass _Makdessi_ test

#### Category 12: Post-Termination Non-Compete — UK Calibration

**Apply the _Dwyer v Fredbar_ framework in full** (see Section above).

This is where UK law diverges most from other jurisdictions. Key differences:

| Feature                             | UK                                   | US (most states)                        | California    | Australia                        |
| ----------------------------------- | ------------------------------------ | --------------------------------------- | ------------- | -------------------------------- |
| Standard                            | Restraint of trade — proportionality | Reasonableness (time, geography, scope) | Void (§16600) | Prima facie void; reasonableness |
| Bargaining power factor             | **Yes** — post-_Dwyer_               | Generally no                            | N/A           | Not a primary factor             |
| Severance                           | Limited — _Dwyer_ refused rewrite    | Blue-pencil widely available            | N/A           | Cascading clauses standard       |
| Sliding scale by franchise duration | Recommended post-_Dwyer_             | Not standard                            | N/A           | Not standard                     |

#### Category 15: Dispute Resolution — UK Calibration

- No mandatory ADR (unlike Australian Code)
- BFA members have access to BFA dispute resolution services
- Arbitration clauses are enforceable under Arbitration Act 1996
- Court proceedings: Business and Property Courts (B&PC), Chancery Division, or Commercial
  Court
- Consider mediation provision — increasingly expected by courts
- Costs consequences: losing party typically pays costs in English litigation

#### Category 16: Representations and Acknowledgments — UK Calibration

- Non-reliance clauses: must pass UCTA s 11 + Misrepresentation Act s 3 reasonableness test
- Cannot exclude liability for fraud
- Entire agreement clauses: do not necessarily exclude misrepresentation claims
- Post-_Papa Johns_: non-reliance clauses in non-negotiable agreements are vulnerable

### Step 4: UCTA Screening

Run all exclusion, limitation, non-reliance, and entire agreement clauses through the UCTA
s 11 reasonableness test. For each:

1. Identify the clause
2. Identify what it excludes or limits
3. Assess reasonableness against s 11 factors (bargaining power, advice opportunity, clarity,
   negotiation)
4. Classify: GREEN (likely reasonable) / YELLOW (arguable) / RED (likely unreasonable)

### Step 5: Competition Law Check

Run VABEO hardcore restriction screening against:

- Pricing provisions (RPM check)
- Territory provisions (passive sales check)
- Online sales provisions (internet channel check)
- Retail parity provisions (UK-specific hardcore check)

### Step 6: Quality Verification

Before delivering analysis, run quality checks:

1. **Case law currency**: Every case cited — verify it has not been overturned or
   distinguished
2. **UCTA screening complete**: All exclusion/limitation clauses assessed
3. **Restraint of trade analysis**: _Dwyer v Fredbar_ framework applied to all
   post-termination restrictions
4. **Competition law**: VABEO hardcore restrictions screened
5. **Misrepresentation exposure**: Non-reliance clause assessment complete

---

## Anti-Patterns — UK-Specific

1. **Treating UK franchise law as "unregulated"**: While there is no franchise-specific
   statute, general contract law (UCTA, misrepresentation, restraint of trade, good faith)
   provides substantial franchisee protections. The absence of a Franchise Act does not mean
   the absence of legal constraints.

2. **Applying US franchise law concepts**: No registration requirement, no mandatory
   disclosure period, no FDD equivalent, no state relationship laws. Analysing a UK franchise
   agreement as if these exist is misleading.

3. **Ignoring _Dwyer v Fredbar_**: This 2022 Court of Appeal decision fundamentally changed
   the non-compete analysis for franchise agreements. Any analysis using the old "reasonable
   restraint in commercial context" approach without considering inequality of bargaining
   power is outdated.

4. **Treating non-reliance clauses as bulletproof**: Post-_Papa Johns_, non-reliance clauses
   in non-negotiable franchise agreements are vulnerable to UCTA challenge. They never
   exclude liability for fraud.

5. **Missing VABEO hardcore restrictions**: RPM and passive sales restrictions can invalidate
   the entire franchise agreement under competition law — with penalties up to 10% of
   worldwide turnover. This is the highest-exposure risk in UK franchise agreements.

6. **Ignoring the Braganza duty**: Where the franchise agreement gives the franchisor
   discretionary powers (termination, transfer approval, territory changes), the Braganza
   duty of rationality likely applies regardless of what the contract says.

7. **Assuming good faith is not implied**: Post-_Yam Seng_, franchise agreements as
   "relational contracts" are strong candidates for implied good faith obligations. Ignoring
   this is a gap in the analysis.

8. **Treating BFA membership as determinative**: Most UK franchisors are not BFA members.
   BFA standards are best practice benchmarks even for non-members, but non-membership is
   not itself a red flag.

9. **Missing the Trading Schemes Act**: For multi-tier franchise structures, the Trading
   Schemes Act 1996 provides specific (if limited) protections including a cooling-off
   period. Missing this where applicable is a regulatory gap.

10. **Overlooking the _Makdessi_ penalty test**: Franchise agreements commonly include
    liquidated damages, fee forfeiture, and accelerated payment provisions. These must be
    assessed under the current (post-2015) penalty test, not the old "genuine pre-estimate
    of loss" standard.

11. **Applying EU VBER instead of UK VABEO**: Post-Brexit, the UK has its own vertical
    agreements regime with material divergences (retail parity, shared exclusivity). Using
    EU analysis for UK agreements is incorrect.

12. **Ignoring Vodafone reform signals**: While no legislation has been enacted, the
    government review signals a direction of travel. Franchisors who adopt best practice now
    are better positioned for potential regulatory change.

---

## Quality Assurance Framework

### Citation Quality Gates — UK

| Gate           | Rule                                                                   | Fail Action                    |
| -------------- | ---------------------------------------------------------------------- | ------------------------------ |
| **Source**     | Every claim cites statute, case, or BFA Code provision                 | Add citation or "[UNVERIFIED]" |
| **Format**     | Cases: _Name_ [year] Court Ref; Statutes: Act year s X                 | Fix format                     |
| **Currency**   | Check: post-_Dwyer_? Post-VABEO? Post-_Makdessi_?                      | Flag "[CHECK CURRENCY]"        |
| **Domain**     | English law only; flag Scots/NI variations                             | Confirm jurisdiction           |
| **Confidence** | Uncertainty stated, especially for evolving areas (good faith, reform) | Add qualifier                  |

### Confidence Scoring

- **Definite (0.95-1.0)**: Clear statute directly on point (UCTA s 2(1), Trade Marks Act s 28)
- **High (0.80-0.94)**: Strong case law authority (_Dwyer_ on non-competes, _Makdessi_ on
  penalties)
- **Probable (0.60-0.79)**: Good authority with some uncertainty (_Yam Seng_ good faith —
  not yet confirmed by Supreme Court for franchise context)
- **Possible (0.40-0.59)**: Genuinely open question (scope of Braganza duty in franchise
  renewal decisions)
- **Unlikely (0.0-0.39)**: Speculative; flag "[UNCERTAIN]"

---

## Glass Box Audit Trail

```yaml
glass_box:
  agreement: "[Franchise Agreement title and date]"
  franchisor: "[Franchisor name]"
  franchisor_bfa_member: "Yes / No / Unknown"
  agreement_type: "[Single-unit / Multi-unit / Master Franchise / Area Development]"
  user_side: "[Prospective Franchisee / Existing Franchisee / Franchisor]"
  operating_jurisdiction: "United Kingdom — [England & Wales / Scotland / Northern Ireland]"
  governing_law: "[English / Scots / Northern Irish]"
  applicable_frameworks:
    - "Common law (contract, restraint of trade, misrepresentation)"
    - "Unfair Contract Terms Act 1977"
    - "Misrepresentation Act 1967"
    - "Competition Act 1998 / UK VABEO (SI 2022/516)"
    - "Trade Marks Act 1994"
    - "[BFA Code of Ethics if member]"
    - "[Trading Schemes Act 1996 if multi-tier]"
  disclosure:
    provided: "Yes / No / Partial"
    timing: "[days before signing]"
    bfa_compliant: "Yes / No / N/A (non-member)"
  ucta_screening:
    standard_form: "Yes / No"
    exclusion_clauses_assessed: "[number]"
    reasonableness_concerns: "[number] — [list]"
  restraint_of_trade:
    post_term_present: "Yes / No"
    duration: "[months]"
    geographic_scope: "[description]"
    dwyer_analysis: "Enforceable / Vulnerable / Unenforceable"
    severance_available: "Yes / No / Not assessed"
  good_faith:
    relational_contract: "Yes (likely) / Uncertain"
    braganza_duty_applicable: "Yes / Uncertain / No"
    discretionary_powers_identified: "[number]"
  misrepresentation:
    non_reliance_clause: "Present / Absent"
    reasonableness_assessment: "Likely reasonable / Arguable / Likely unreasonable"
    pre_contractual_representations: "[identified / none identified]"
  competition_law:
    vabeo_applicable: "Yes / No (market share >30%)"
    hardcore_restrictions: "[None / RPM / Passive sales / Online / Parity — list]"
  penalty_clauses:
    identified: "[number]"
    makdessi_analysis: "Proportionate / Disproportionate / Mixed"
  clauses_reviewed: 16
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  legalcode_mcp: "Connected / Not connected"
  statutes_consulted:
    - "UCTA 1977 — [VERIFIED / UNVERIFIED]"
    - "Misrepresentation Act 1967 — [VERIFIED / UNVERIFIED]"
    - "Competition Act 1998 — [VERIFIED / UNVERIFIED]"
    - "UK VABEO (SI 2022/516) — [VERIFIED / UNVERIFIED]"
    - "Trade Marks Act 1994 — [VERIFIED / UNVERIFIED]"
  case_law_consulted:
    - "[Case — VERIFIED / UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Scope limitations, assumptions, caveats]"
  reviewer: "AI-assisted — requires qualified UK franchise solicitor review"
```

---

## Provenance

Created by Legalcode (2026-03-19). Jurisdiction-specific variant of
`legalcode-franchise-agreement-review`. UK-specific research covering:

- BFA Code of Ethics (EFF-aligned)
- Unfair Contract Terms Act 1977
- Misrepresentation Act 1967
- Competition Act 1998 / UK VABEO (SI 2022/516)
- Trade Marks Act 1994
- Trading Schemes Act 1996
- _Dwyer v Fredbar_ [2022] EWCA Civ 889 (non-compete enforceability)
- _Yam Seng v ITC_ [2013] (good faith in relational contracts)
- _Braganza v BP Shipping_ [2015] UKSC 17 (duty of rationality)
- _Cavendish Square v Makdessi_ [2015] UKSC 67 (penalty clauses)
- _Hunters v Brybond_ [2022], _Winkworth v Goble_ [2023] (franchise case law)
- Vodafone franchise dispute and reform proposals (2025-2026)
- DMCCA 2024 and CMA powers

Research sources:

- [ICLG Franchise Laws England & Wales 2026](https://iclg.com/practice-areas/franchise-laws-and-regulations/england-and-wales)
- [BFA Code of Ethics](https://www.thebfa.org/wp-content/uploads/The-Code-of-Ethics-for-Franchising.pdf)
- [UK VABEO (SI 2022/516)](https://www.legislation.gov.uk/en/uksi/2022/516/made)
- [CMA VABEO Guidance (CMA166)](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1091830/VABEO_Guidance.pdf)
- [Fieldfisher — Dwyer v Fredbar Analysis](https://www.fieldfisher.com/en/services/franchising/franchise-commercial-law-blog/court-of-appeal-confirms-that-post-termination-res)
- [Fieldfisher — Non-Reliance Clauses](https://www.fieldfisher.com/en/insights/non-reliance-clauses-in-franchise-agreements-court-of-appeal-confirms-they-are-subject-to-the-reasonable-test)
- [Travers Smith — Good Faith](https://www.traverssmith.com/knowledge/knowledge-container/do-franchisors-need-to-act-in-good-faith/)
