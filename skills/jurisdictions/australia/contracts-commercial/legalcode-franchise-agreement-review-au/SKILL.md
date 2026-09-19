---
name: legalcode-franchise-agreement-review-au
description: Review franchise agreements for Australian operations against the Franchising Code of Conduct
  2025 (Competition and Consumer (Industry Codes—Franchising) Regulations 2024) and Australian Consumer
  Law (Competition and Consumer Act 2010, Schedule 2) — verify disclosure document compliance with Schedule
  1, screen for unfair contract terms under the expanded UCT regime (penalties from 9 November 2023),
  evaluate good faith obligation compliance (s 6), analyse restraint of trade provisions including new
  s 42 prohibition on non-renewal restraints, review significant capital expenditure disclosure (Items
  14(1A), 14(1B) from 1 November 2025), assess early termination compensation obligations (s 43), evaluate
  "reasonable opportunity for return on investment" requirement (s 44), review specific purpose fund obligations,
  verify 14-day consideration period and cooling-off compliance, and assess ACCC enforcement risk. Use
  when reviewing any franchise agreement for operations in Australia.
metadata:
  jurisdiction: Australia
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review franchise agreements for Australian operations against the Franchising Code of Conduct 2025 (Competition and Consumer (Industry Codes—Franchising) Regulations 2024) and Australian Consumer Law (Competition and Consumer Act 2010, Schedule 2) — verify disclosure document compliance with Schedule 1, screen for unfair contract terms under the expanded UCT regime (penalties from 9 November 2023), evaluate good faith obligation compliance (s 6), analyse restraint of trade provisions including new s 42 prohibition on non-renewal restraints, review significant capital expenditure disclosure (Items 14(1A), 14(1B) from 1 November 2025), assess early termination compensation obligations (s 43), evaluate "reasonable opportunity for return on investment" requirement (s 44), review specific purpose fund obligations, verify 14-day consideration period and cooling-off compliance, and assess ACCC enforcement risk. Covers standard franchise, multi-unit development, master franchise, and new vehicle dealership agreements. GREEN/YELLOW/RED classification with confidence scoring and Glass Box audit trail. Use when reviewing any franchise agreement for operations in Australia. Jurisdiction-specific variant of legalcode-franchise-agreement-review.


# Legalcode Franchise Agreement Review — Australia

> **Disclaimer**: This skill provides a framework for AI-assisted franchise agreement review
> under Australian law. It does not constitute legal advice. All outputs require review by
> an Australian-qualified lawyer experienced in franchise and competition law before reliance.
> Australian franchise regulation is federal — the Franchising Code of Conduct 2025 sits under
> the Competition and Consumer Act 2010 (Cth) and is enforced by the ACCC. The Code underwent
> major reform effective 1 April 2025, with further provisions commencing 1 November 2025.
> Verify current applicability before relying on any provision described here. Statutory and
> case law references cited from memory carry hallucination risk — verify against authoritative
> sources (Federal Register of Legislation, Federal Court, ACCC) before relying on them.

---

## Purpose and Scope

This skill reviews franchise agreements for compliance with Australia's mandatory Franchising
Code of Conduct 2025 and the Australian Consumer Law. Australia has one of the most
comprehensive franchise regulatory regimes in the world — a mandatory federal code with civil
penalties, a broad unfair contract terms regime with penalties up to $50 million, and an
active regulator (ACCC) with a track record of franchise enforcement.

**Covers:**

- Full Franchising Code of Conduct 2025 compliance review
- Disclosure document review against Schedule 1 requirements
- Unfair contract terms screening under Australian Consumer Law (as amended 9 November 2023)
- Good faith obligation analysis (s 6)
- Restraint of trade analysis including new s 42 non-renewal restraint prohibition
- Early termination compensation (s 43) and return on investment (s 44) analysis
- Significant capital expenditure disclosure review (Items 14(1A), 14(1B))
- Specific purpose fund compliance
- Consideration period (14 days) and cooling-off period (14 days) verification
- New vehicle dealership specific provisions (ss 45-46) where applicable
- ACCC enforcement risk assessment
- Cascading restraint clause analysis (Australian practice)
- GREEN / YELLOW / RED deviation classification with confidence scoring
- Glass Box audit trail

**Does not:**

- Draft new franchise agreements from scratch
- Provide legal advice or replace qualified Australian franchise counsel
- Cover non-Australian franchise law (see `legalcode-franchise-agreement-review` for general;
  jurisdiction-specific variants for US-CA, UK, EU-FR, Nordics)
- Cover the Oil Code of Conduct (petroleum franchise arrangements)
- Provide employment law advice beyond franchise-specific provisions

**Related skills:**

- `legalcode-franchise-agreement-review` — General multi-jurisdictional franchise review
- `legalcode-franchise-agreement-review-us-ca` — California franchise law focus
- `legalcode-contract-review` — General commercial contract review
- `legalcode-commercial-lease-review` — Franchise premises lease review

---

## Jurisdiction and Governing Law

### Why Australia Requires a Dedicated Skill

Australia's franchise regime is fundamentally different from common law jurisdictions like
the UK and from the US registration model:

1. **Mandatory federal code**: The Franchising Code of Conduct is a prescribed mandatory
   industry code under the Competition and Consumer Act 2010, s 51AE — compliance is not
   voluntary
2. **Civil penalty regime**: Breach of Code provisions attracts penalties up to $10M+ for
   serious breaches, and unfair contract terms penalties up to $50M per contravention
3. **2025 Code reform**: Major changes effective 1 April 2025 (restraint of trade, early
   termination compensation, specific purpose funds, enhanced disclosure) with further
   changes 1 November 2025
4. **Active regulator**: ACCC has a demonstrated enforcement record in franchising — $23M
   (_Jump Loops_), $2.014M (_Ultra Tune_), $1.5M contempt (_Ultra Tune_)
5. **Unfair contract terms regime**: Since 9 November 2023, unfair terms attract penalties —
   the ACCC found in 2023 that **every franchise agreement reviewed** contained potentially
   unfair terms
6. **Restraint of trade doctrine**: Unlike the US (where restraints are analysed under state
   law) or California (where post-term restraints are void), Australia applies a common law
   reasonableness test with cascading clause practice — plus the new s 42 statutory prohibition

### Federal Regime — No State Franchise Laws

Australia operates a **federal franchise regulatory regime**. There are no separate state
franchise registration or relationship laws (unlike the US model). The Franchising Code
applies uniformly across all states and territories.

State and territory bodies that may be involved:

- **ASBFEO** (Australian Small Business and Family Enterprise Ombudsman) — ADR appointment,
  name-and-shame powers
- **Victorian Small Business Commission** — low-cost mediation for franchise disputes
- **NSW/QLD/SA Small Business Commissioners** — mediation and informal dispute resolution
- **State fair trading bodies** — consumer protection enforcement

---

## Franchising Code of Conduct 2025 — Key Provisions

### Good Faith Obligation (s 6)

**"Each party to a franchise agreement must act towards each other with good faith, within
the meaning of the unwritten law."**

**Scope:**

- Applies to all aspects: negotiations, entry, performance, termination, non-renewal
- Requires acting honestly, reasonably, and not arbitrarily or for irrelevant purpose
- Does **not** require acting solely in the other party's interests
- Does **not** prevent acting in own legitimate commercial interests
- The franchise agreement **must not limit** the good faith obligation — **civil penalty**
  applies for including limiting terms

**Key case law:**

- _ACCC v Ultra Tune Australia Pty Ltd_ [2019] FCA 12 — $2.014M penalty; good faith requires
  honest exercise of powers [VERIFY]
- _Virk Pty Ltd v Yum! Restaurants Australia Pty Ltd_ [2017] FCAFC 190 — good faith does not
  require franchisor to act "reasonably" in sense of acting in franchisee's interest [VERIFY]
- _AHG WA v Mercedes-Benz Australia/Pacific Pty Ltd_ [2023] FCA 1022 — good faith does not
  prevent non-renewal for legitimate commercial purposes (agency model transition) [VERIFY]

**REVIEW CHECKLIST:**

- [ ] Does agreement limit or exclude the good faith obligation? → **RED** (civil penalty
      for including limiting terms)
- [ ] Does agreement contain provisions that could be exercised in bad faith? (Unilateral
      variation, sole discretion powers) → **YELLOW** (UCT risk + good faith risk)
- [ ] Does agreement acknowledge good faith obligation? → GREEN if present, YELLOW if absent

### Disclosure Document Requirements (Schedule 1)

The Disclosure Document must comply with **Schedule 1** of the Code and be provided at least
**14 days** before the franchisee signs the agreement (the "consideration period").

**Required disclosures include:**

| Item                             | Description                                                        | Key Review Points                                             |
| -------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------- |
| Franchisor details               | Corporate structure, ABN, business history                         | Verify currency and accuracy                                  |
| Business experience              | Directors and key personnel backgrounds                            | Gaps or concerns?                                             |
| Litigation history               | Pending and past proceedings                                       | Volume and nature of franchisee disputes                      |
| Intellectual property            | Trade marks, licences, registrations                               | Registration status, prior disputes                           |
| Financial information            | Solvency statement + financial reports (2 FY) or independent audit | Financial stability concerns?                                 |
| Fees                             | Franchise fee, royalties, specific purpose fund contributions      | Consistency with agreement                                    |
| Territory/sites                  | Geographic territory, exclusivity, online sales provisions         | Clear boundaries? Online carve-outs?                          |
| Supply arrangements              | Franchisor-controlled suppliers, restrictions, rebates             | Competitive pricing? Rebate disclosure?                       |
| Significant capital expenditure  | Rationale, amount, timing, nature, outcomes, benefits, risks       | Realistic? Recoupable? (Items 14(1A), 14(1B) from 1 Nov 2025) |
| Earnings information             | Historical and projected earnings                                  | Basis? Substantiated?                                         |
| Specific purpose fund statements | Receipts and expenses for each fund                                | Attached? Current?                                            |
| Existing franchisee contacts     | Contact details for due diligence                                  | Complete? Updated?                                            |
| Termination, transfer, renewal   | Conditions for each                                                | Consistent with agreement?                                    |

**Timing requirements:**

- Disclosure Document: at least **14 days** before signing (consideration period)
- Updated within **4 months** after end of each financial year
- Retained for **6 years**

**Opt-out for existing franchisees:** An existing franchisee may opt out of receiving the
Disclosure Document when entering another similar agreement with the same franchisor for the
same or substantially the same business. The consideration period (14 days) still applies
even when disclosure is opted out.

### Consideration Period and Cooling-Off Period

**Consideration period (14 days before signing):**

- Franchisee must receive Disclosure Document, agreement, and Code at least 14 days before
  signing
- Applies even when franchisee opts out of disclosure
- Purpose: allow franchisee time for independent legal, business, and accounting advice

**Cooling-off period (14 days after signing):**

- Franchisee may terminate the agreement within 14 days of signing **without penalty**
- **Opt-out available**: If franchisee has or recently had another franchise agreement with
  the same franchisor, agreement is substantially the same, and business is same or
  substantially similar
- Franchisor must refund franchise fee minus reasonable expenses already incurred

**REVIEW CHECKLIST:**

- [ ] Does agreement acknowledge 14-day consideration period? If silent → YELLOW
- [ ] Does agreement acknowledge 14-day cooling-off period? If excluded → **RED**
- [ ] If cooling-off opt-out claimed, do conditions apply? Verify eligibility
- [ ] Does agreement impose penalties for cooling-off termination? → **RED** (Code prohibits)

### Specific Purpose Fund Requirements

The 2025 Code broadened "marketing funds" to **"specific purpose funds"** covering any
contributions for a specified common purpose.

**Requirements:**

- Money must be held in a **separate bank account** for each fund
- Annual **financial statement** for each fund showing receipts and expenses
- Statements must be **prepared and provided to each franchisee within 30 days** of preparation
- Statements must be **attached to the Disclosure Document**
- **Civil penalty** for failure to provide statements
- Reporting for non-marketing/non-cooperative specific purpose funds begins **1 November 2025**

**REVIEW CHECKLIST:**

- [ ] Does agreement require contributions to funds beyond marketing? → All are now "specific
      purpose funds" subject to reporting requirements
- [ ] Does agreement provide for annual financial statements of each fund? If not → YELLOW
      (Code requires regardless of contract terms)
- [ ] Does agreement give franchisor discretion to create new funds without franchisee
      consent? → YELLOW (potential UCT)
- [ ] Does agreement allow fund to be used for purposes other than stated? → **RED**

### Restraint of Trade — New s 42 Prohibition

**Critical 2025 change**: Franchise agreements must **not** include a restraint of trade
that applies when ALL of these conditions are met:

1. The agreement **expires** (natural end of term, not termination for cause)
2. The franchisee gave **written notice** to renew/extend before expiry
3. The franchisee requested terms **substantially the same** as current standard terms
4. The franchisee **met all renewal/extension conditions**
5. The franchisee was **not in serious breach** and did not misuse IP or breach confidentiality

**Civil penalties apply** to franchisors who include prohibited restraint terms.

**Practical impact**: A franchisee who does everything right — meets all conditions, seeks
renewal on standard terms, has no serious breaches — cannot be hit with a post-term
non-compete if the franchisor simply declines to renew. This prevents the "double penalty"
of losing the franchise and being unable to compete.

**Note**: s 42 does **not** prohibit all post-term restraints. Post-term non-competes remain
enforceable where:

- The franchisee **did not seek renewal** or sought non-standard terms
- The franchisee was **in serious breach**
- The franchisee **misused IP or breached confidentiality**
- The franchise was **terminated for cause** (not expired)

**REVIEW CHECKLIST:**

- [ ] Does agreement contain a post-term non-compete? → Analyse against s 42 conditions
- [ ] Does the restraint clause carve out the s 42 scenario? If not → **RED** (blanket
      restraint that would apply in prohibited scenarios)
- [ ] Does agreement use cascading restraint clauses? → YELLOW to GREEN (standard Australian
      practice, but each level must pass reasonableness test)
- [ ] Is there a post-termination restraint (vs. post-expiry)? → s 42 does not prohibit
      this, but common law reasonableness still applies

### Restraint of Trade — Common Law Analysis

For restraints not prohibited by s 42, the common law test applies:

**Principle**: All restraints are **prima facie void** unless the party seeking enforcement
proves reasonableness.

**Reasonableness factors:**

- **Legitimate protectable interest**: Confidential information, know-how, goodwill, customer
  relationships. The franchisor's system, methods, and brand constitute legitimate interests.
- **Geographic scope**: Must correspond to the area in which the franchise operated. A
  nationwide restraint for a single-location franchise is likely unreasonable.
- **Duration**: Must be proportionate. Typically 1-2 years is reasonable; longer periods
  require stronger justification (time for new franchisee to establish customer relationships).
- **Activity scope**: Must be limited to genuinely competing activities. Prohibiting all
  business activity is likely unreasonable.
- **Assessed at date of entry**: Reasonableness determined at time the agreement was signed,
  not at time of enforcement.

**Cascading restraint clauses** — standard Australian practice:

Cascading restraints provide descending levels of restriction (broadest to narrowest in
time, area, and activity). If the broadest restraint is unreasonable, the court enforces
the next level down.

Example structure:

```
The Franchisee must not, for a period of:
  (a) 3 years; or alternatively (b) 2 years; or alternatively (c) 1 year
within a radius of:
  (a) 20km; or alternatively (b) 10km; or alternatively (c) 5km
from the Premises, carry on or be engaged in:
  (a) any business similar to the Franchised Business; or alternatively
  (b) any business competing directly with the Franchised Business
```

Upheld in _Hanna v OAMPS Insurance Brokers Ltd_ [2010] NSWCA 267 (27 possible restraint
combinations held acceptable). [VERIFY]

**REVIEW CHECKLIST:**

- [ ] Does the restraint protect a legitimate interest? → Must identify specific interest
- [ ] Is geographic scope proportionate to franchise territory? If exceeds → YELLOW to RED
- [ ] Is duration proportionate? 1-2 years → GREEN to YELLOW; 3+ years → RED
- [ ] Is activity scope limited to genuinely competing activities? If overly broad → YELLOW
- [ ] Does the agreement use cascading clauses? If not → YELLOW (best practice in Australia)
- [ ] Does the restraint survive wrongful termination by franchisor? → **RED** (unlikely
      enforceable; argue lack of clean hands)

### Early Termination Compensation (s 43) — From 1 November 2025

**Section 43** requires franchisors to compensate franchisees on early termination in
specific circumstances:

- Franchisor **withdraws from the Australian market**
- Franchisor **rationalises the network** (reduces number of franchisees)
- Franchisor **changes the distribution model** (e.g., moves to agency/direct model)

**Compensation formula must reference:**

1. Lost profit (direct and indirect)
2. Unamortised capital expenditure
3. Loss of opportunity in selling goodwill
4. Cost of winding up the franchised business

**Franchisor must also buy back or compensate for:**

- Outstanding stock
- Essential specialty equipment
- Branded product/merchandise specified by the franchisor

**REVIEW CHECKLIST:**

- [ ] Does agreement address s 43 compensation? → Must be present for agreements from
      1 November 2025
- [ ] Does compensation formula reference all four elements? If incomplete → **RED**
- [ ] Does agreement include buy-back obligations? If absent → YELLOW (Code applies regardless)
- [ ] Does agreement attempt to limit s 43 compensation? → **RED** (cannot contract out of
      Code protections)

### Reasonable Opportunity for Return on Investment (s 44) — From 1 November 2025

**Section 44**: Franchise agreement must provide the franchisee a **"reasonable opportunity
to make a return"** on any investment required by the franchisor.

**Practical implications:**

- Investment required by the franchisor includes: franchise fee, fit-out costs, equipment,
  initial stock, training costs
- "Reasonable opportunity" is assessed against the term, territory, fee structure, and
  projected earnings
- A short term with high initial investment and no renewal right may fail the s 44 test

**REVIEW CHECKLIST:**

- [ ] Is the term length proportionate to the required investment? → Short term + high
      investment → **RED** (may fail s 44)
- [ ] Does the agreement provide realistic renewal rights? → No renewal with high sunk
      cost → YELLOW to RED
- [ ] Are significant capital expenditure requirements proportionate to remaining term? →
      Major refit requirement near end of term → **RED**

### Termination Requirements

**Standard termination:**

- Franchisor must provide notice and opportunity to cure (except serious breaches)
- Notice must specify the breach and what is required to remedy it
- Cure period must be reasonable

**Serious breach termination — 7 days' notice:**

- Seven days' written notice for serious breaches
- No ADR available for serious breaches
- Serious breach includes: fraud, endangering public health/safety, being convicted of a
  serious offence, operating business in a way that endangers public health/safety

**REVIEW CHECKLIST:**

- [ ] Does agreement define "serious breach" consistently with the Code? If broader → YELLOW
      (potential UCT)
- [ ] Does agreement provide reasonable cure periods for non-serious breaches? → 14-30 days
      minimum expected
- [ ] Can franchisor terminate for minor/non-material breaches? → **RED** (UCT risk +
      good faith risk)
- [ ] Does agreement provide for repurchase/compensation on termination? → Review against
      s 43 requirements

### Transfer Requirements

- Franchisor **must not unreasonably withhold consent** to transfer — **civil penalty**
  for unreasonable refusal
- Transferring franchisee must provide disclosure to incoming transferee
- Franchisor may impose reasonable conditions (training, financial capacity, etc.)

**REVIEW CHECKLIST:**

- [ ] Is consent standard "not unreasonably withheld"? If "sole discretion" → **RED**
      (Code override + civil penalty risk)
- [ ] Are transfer conditions reasonable and non-discriminatory?
- [ ] Is transfer fee proportionate?
- [ ] Does agreement require transferring franchisee to provide disclosure to transferee?

### Dispute Resolution (Code-Mandated Process)

The Code prescribes a specific dispute resolution process:

1. **Written notice** of dispute — outline dispute, desired resolution
2. **Direct negotiation** — 21 days to resolve
3. **Referral to ASBFEO** — either party may refer if unresolved
4. **ASBFEO appoints ADR practitioner** within 14 days (specialist panel, accredited)
5. **ADR process** (mediation/conciliation) — mandatory attendance; genuine effort required;
   costs shared equally (approx. $2,000 per party)
6. **Arbitration** — if parties agree in writing (not mandatory)
7. **Court proceedings** — Federal Court or state/territory courts

**New enforcement**: ASBFEO can **publicly name** franchisors who refuse to engage in or
withdraw from ADR.

**REVIEW CHECKLIST:**

- [ ] Does agreement dispute resolution clause comply with Code process? If incompatible →
      **RED** (Code overrides)
- [ ] Does agreement attempt to bypass Code ADR? → RED
- [ ] Does agreement mandate binding arbitration without option for court? → YELLOW (Code
      requires written agreement for arbitration)
- [ ] Does agreement impose costs on franchisee disproportionately? → YELLOW (Code provides
      for equal sharing)

### Penalties for Non-Compliance

| Breach Type                                    | Maximum Penalty (Body Corporate)                                      | Maximum Penalty (Individual) |
| ---------------------------------------------- | --------------------------------------------------------------------- | ---------------------------- |
| Standard civil penalty                         | $198,000 (600 penalty units)                                          | Lower amount                 |
| Serious breach (e.g., s 34 disclosure failure) | Greater of: 3× benefit obtained, OR 10% annual turnover. Minimum $10M | $500,000                     |
| Infringement notice                            | $19,800 (60 penalty units)                                            | $3,960 (12 penalty units)    |

---

## Australian Consumer Law — Franchise Implications

### Unfair Contract Terms Regime (as Amended 9 November 2023)

**Critical 2023 change**: Unfair contract terms now attract **civil penalties**:

- Corporations: **$50 million** per contravention
- Individuals: **$2.5 million** per contravention
- Each unfair term may attract a **separate penalty**
- It is now unlawful to **propose, use, apply, or rely on** an unfair term

Previously, unfair terms were merely voidable. The penalty regime fundamentally changes the
risk calculus for franchisors.

**Applies to**: Standard form contracts with consumers and small businesses, including most
franchise agreements.

**A term is unfair if it:**

1. Would cause a **significant imbalance** in the parties' rights and obligations
2. Is **not reasonably necessary** to protect the legitimate interests of the advantaged party
3. Would cause **detriment** (financial or otherwise) to the other party

**ACCC 2023 Franchise Compliance Report — five prevalent unfair terms:**

| Potentially Unfair Term                                    | Why It's Problematic                                                  | Prevalence                        |
| ---------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------- |
| **Unilateral variation** (including via Operations Manual) | Franchisor can change obligations without consent                     | Found in every agreement reviewed |
| **Withholding/set-off of payments**                        | Franchisor can withhold amounts owed without independent verification | Found in every agreement reviewed |
| **Audit at sole discretion**                               | One-sided right with no limits on frequency or scope                  | Found in every agreement reviewed |
| **Restraints of trade** favouring franchisor               | Broader than reasonably necessary to protect legitimate interests     | Found in every agreement reviewed |
| **Termination for minor breaches**                         | Disproportionate consequence for immaterial non-compliance            | Found in every agreement reviewed |

**REVIEW CHECKLIST — UCT Screening:**

- [ ] **Unilateral variation**: Can franchisor change fees, standards, or requirements
      without consent? → **RED** (highest UCT risk; ACCC priority)
- [ ] **Operations manual changes**: Is manual incorporated by reference with unilateral
      change power? → YELLOW to RED (amount to unilateral variation of agreement)
- [ ] **Set-off/withholding**: Can franchisor withhold payments to franchisee without
      independent verification? → YELLOW to RED
- [ ] **Audit powers**: Are audit rights unlimited in scope/frequency with no notice? → YELLOW
- [ ] **Termination for minor breach**: Can franchisor terminate for any non-compliance? →
      **RED** (ACCC enforcement priority)
- [ ] **One-sided indemnity**: Does franchisee indemnify franchisor but not vice versa? → YELLOW
- [ ] **Automatic renewal at changed terms**: Does agreement auto-renew on different terms
      without franchisee consent? → YELLOW to RED
- [ ] **Liability caps**: Does agreement cap franchisor's liability but not franchisee's? → YELLOW
- [ ] **Entire agreement clause**: Does it purport to exclude pre-contractual representations? →
      YELLOW (may not prevent s 18 ACL misleading conduct claims)

### Misleading or Deceptive Conduct (s 18 ACL)

**"A person must not, in trade or commerce, engage in conduct that is misleading or deceptive
or is likely to mislead or deceive."**

Franchise context:

- False representations about profitability, earnings, territory, operational costs
- Failure to disclose material information during franchise sales process
- Oral representations inconsistent with Disclosure Document
- Franchisee financial performance representations without reasonable basis

**Key cases:**

- _ACCC v Campbell / Jump Loops_ [2019] FCA 1487 — **$23M penalty** for 762+ false
  representations about swim school franchise timeframes [VERIFY]
- _ACCC v Retail Food Group_ — misleading conduct re: sale of 42 loss-making stores.
  Settled: $8M + $1.82M debt waiver + $5M to marketing fund. No admission [VERIFY]
- _ACCC v Ultra Tune_ [2019] FCA 12 — false/misleading representations to prospective
  franchisee [VERIFY]

**REVIEW CHECKLIST:**

- [ ] Do agreement representations match Disclosure Document? Any discrepancy → **RED**
- [ ] Are earnings claims in the Disclosure Document substantiated? If not → RED
- [ ] Were oral representations made during sales process? → Document and compare to
      Disclosure Document
- [ ] Does agreement attempt to exclude pre-contractual representation claims? → YELLOW
      (s 18 ACL cannot be excluded by contract)

### Unconscionable Conduct (ss 20-22 ACL)

**Section 21** (statutory unconscionable conduct): Broader scope than equitable doctrine;
does not require exploitation of special disadvantage.

**Factors courts consider:**

- Relative bargaining strength
- Whether franchisee was required to comply with conditions not reasonably necessary
- Whether franchisee could understand the documents
- Whether undue influence, pressure, or unfair tactics were used
- Amount and circumstances of the transaction

**REVIEW CHECKLIST:**

- [ ] Is there a substantial power imbalance in the agreement? → Document for context
- [ ] Were unfair tactics used in negotiation or during franchise operation? → Flag
- [ ] Does the agreement impose conditions not reasonably necessary? → YELLOW to RED

---

## New Vehicle Dealership Provisions (ss 45-46)

**Expanded definition**: "Motor vehicle dealership" now includes servicing or repairing
of motor vehicles (not just sales).

**Motor vehicle dealership agreements are deemed franchise agreements** regardless of whether
standard franchise definition elements are met.

**Key provisions (effective 1 April 2025):**

- Multi-party dispute resolution: Two or more franchisees may request to deal with franchisor
  together about disputes of the same nature
- Capital expenditure disclosure must include discussion about likelihood of recoupment
- End-of-term obligations apply to renewals/extensions of existing NVDAs entered into before
  1 June 2020

**Key case law:**

- _AHG WA v Mercedes-Benz Australia/Pacific Pty Ltd_ [2023] FCA 1022 — agency model
  transition upheld; no goodwill compensation at natural expiry; good faith does not prevent
  non-renewal for legitimate commercial purposes [VERIFY]
- Full Federal Court appeal (July 2025) — appeal dismissed; confirmed not unconscionable to
  advance own commercial interests in non-renewal [VERIFY]

**REVIEW CHECKLIST (motor vehicle dealerships only):**

- [ ] Is the agreement a "new vehicle dealership agreement"? → If yes, ss 45-46 apply
- [ ] Does agreement address multi-party dispute resolution? If not → YELLOW
- [ ] Does capital expenditure disclosure address recoupment? If not → RED (from 1 Nov 2025)
- [ ] Is franchisor transitioning to agency model? → Analyse s 43 compensation implications
- [ ] Are end-of-term obligations compliant with ss 45-46?

---

## 2025 Code Transition Analysis

### Effective Date Matrix

| Provision                                           | Effective Date  | Impact on Current Review                         |
| --------------------------------------------------- | --------------- | ------------------------------------------------ |
| Good faith obligation (s 6)                         | 1 April 2025    | Applies to all new/renewed agreements            |
| Restraint of trade prohibition (s 42)               | 1 April 2025    | Must be reflected in agreement                   |
| Specific purpose fund framework                     | 1 April 2025    | Applies; non-marketing fund reporting from 1 Nov |
| Updated disclosure format                           | 1 April 2025    | Must comply with Schedule 1                      |
| Consideration/cooling-off rules                     | 1 April 2025    | Must be observed                                 |
| New vehicle dealership provisions (ss 45-46)        | 1 April 2025    | Applies immediately                              |
| ASBFEO name-and-shame powers                        | 1 April 2025    | Enforcement context                              |
| New penalty framework                               | 1 April 2025    | Enforcement context                              |
| Early termination compensation (s 43)               | 1 November 2025 | Must be in agreements from this date             |
| Return on investment (s 44)                         | 1 November 2025 | Must be addressed from this date                 |
| Significant capex disclosure (Items 14(1A), 14(1B)) | 1 November 2025 | Must be in Disclosure Document                   |
| Non-marketing specific purpose fund reporting       | 1 November 2025 | Reporting obligation begins                      |

### Grandfathering

- Agreements entered before 1 April 2025 are **not required** to be updated
- The **Old Code continues to apply** until the agreement is terminated, transferred, renewed,
  or extended
- At renewal/transfer/extension, the New Code applies in full
- Disclosure Documents issued before 31 March 2025 under old obligations remain compliant
  even if agreement signed after 31 March 2025

**REVIEW CHECKLIST:**

- [ ] When was the agreement entered? → Determines which Code version applies
- [ ] Has the agreement been renewed/transferred/extended since 1 April 2025? → If yes,
      New Code applies in full
- [ ] If agreement pre-dates 1 April 2025 and has not been renewed, Old Code still applies
      (but UCT regime applies regardless)
- [ ] For agreements entered 1 April – 31 October 2025: ss 43 and 44 do not yet apply
- [ ] For agreements from 1 November 2025: full New Code applies

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

### Step 1: Accept Agreement and Determine Agreement Type

Accept the franchise agreement and determine the type:

**⟁ CLARIFY** — Agreement type:

1. **Standard franchise agreement** (single unit) — most common
2. **Multi-unit development agreement** — developer granted rights for multiple units
3. **Master franchise agreement** — international brand granting territory for sub-franchising
4. **New vehicle dealership agreement** — motor vehicle sales, servicing, or repair
5. **Other** — describe the arrangement

### Step 2: Accept Disclosure Document

**⟁ CLARIFY** — Disclosure Document status:

1. **Disclosure Document provided**: Full compliance review against Schedule 1
2. **Disclosure Document not provided**: Flag — was consideration period observed? Did
   franchisee opt out of disclosure?
3. **Pre-1 April 2025 disclosure**: Check if still compliant during transition period
4. **Master franchise**: Was disclosure provided at both master and unit levels?

### Step 3: Gather Context

**⟁ CLARIFY** — In addition to standard franchise review context:

1. **Which side are you on?** Prospective Franchisee / Existing Franchisee / Franchisor
2. **Agreement date?** Determines Code version and transition provisions
3. **Is this a new vehicle dealership?** If yes, ss 45-46 apply
4. **Is the franchisor an international brand?** Master franchise structure considerations
5. **Industry sector?** Food & beverage, retail, services, automotive, education, fitness,
   cleaning, other — affects UCT and enforcement risk assessment
6. **State/territory of operation?** Determines available state-level ADR (VSBC, SBC)
7. **Deal stage?** Pre-signing / Post-signing / Renewal / Transfer
8. **Risk tolerance?** Conservative / Pragmatic / Deal-centric

### Step 4: Code Version Determination

Based on agreement date, determine which Code version applies and which provisions are in
effect. Document this in the Glass Box audit trail.

### Step 5: Disclosure Document Compliance Review

If Disclosure Document is available, review against Schedule 1 requirements:

**Completeness check:**

| Schedule 1 Item                         | Present? | Compliant? | Notes |
| --------------------------------------- | -------- | ---------- | ----- |
| Franchisor details and ABN              | [ ]      | [ ]        |       |
| Business experience                     | [ ]      | [ ]        |       |
| Litigation history                      | [ ]      | [ ]        |       |
| IP details and licence                  | [ ]      | [ ]        |       |
| Financial information (solvency + 2 FY) | [ ]      | [ ]        |       |
| Fees (all)                              | [ ]      | [ ]        |       |
| Territory/sites                         | [ ]      | [ ]        |       |
| Online sales provisions                 | [ ]      | [ ]        |       |
| Supply arrangements                     | [ ]      | [ ]        |       |
| Significant capex (from 1 Nov 2025)     | [ ]      | [ ]        |       |
| Earnings information                    | [ ]      | [ ]        |       |
| Specific purpose fund statements        | [ ]      | [ ]        |       |
| Existing franchisee contacts            | [ ]      | [ ]        |       |
| Termination conditions                  | [ ]      | [ ]        |       |
| Transfer conditions                     | [ ]      | [ ]        |       |
| Renewal conditions                      | [ ]      | [ ]        |       |

**Disclosure Document red flags:**

| Red Flag                                 | Significance                                                   |
| ---------------------------------------- | -------------------------------------------------------------- |
| High litigation volume                   | Pattern of franchisee disputes — investigate causes            |
| Net unit decline                         | More closures/terminations than openings — viability concerns  |
| No earnings information                  | Franchisor may have data but chooses not to disclose — ask why |
| Unrealistic capex estimates              | Low-balled investment — budget overruns likely                 |
| Weak financials / no solvency statement  | Franchisor stability concerns                                  |
| Missing specific purpose fund statements | Code non-compliance → potential civil penalty                  |

### Step 6: UCT Pre-Screen

Before clause-by-clause analysis, run the UCT pre-screen against the ACCC's five priority
areas. Flag any potentially unfair terms for deeper analysis.

### Step 7: Clause-by-Clause Analysis (Australian-Calibrated)

Apply the 16-category framework from the general franchise review skill with Australian
calibration:

**Categories with material Australian variation:**

#### Category 3: Territory — Australian Calibration

- No statutory encroachment protection — purely contractual
- Franchisor must disclose in Disclosure Document whether it will offer similar
  services/products in the territory or **online**
- Exclusive territories permitted subject to competition law (no substantial lessening
  of competition)
- Online sales carve-outs must be clearly disclosed

#### Category 5: Quality Control and Operations Manual — Australian Calibration

**CRITICAL UCT RISK**: Unilateral variation of Operations Manual = potential unilateral
variation of agreement → highest-risk UCT area identified by ACCC.

- [ ] Can franchisor change Operations Manual without notice? → **RED** (UCT)
- [ ] Must franchisee comply with manual changes without consent? → **RED** (UCT)
- [ ] Are material manual changes subject to consultation or notice period? → GREEN if yes

#### Category 6: Specific Purpose Funds — Australian Calibration

Apply specific purpose fund requirements per Code (above). All funds are now subject to
separate accounting and annual reporting obligations.

#### Category 9: Term and Renewal — Australian Calibration

- s 44 (from 1 Nov 2025): Must provide "reasonable opportunity for return on investment"
- s 42: Post-expiry restraint prohibited if franchisee sought renewal and met conditions
- Term length must be proportionate to required investment

#### Category 10: Transfer — Australian Calibration

- Code: consent must not be unreasonably withheld (civil penalty for unreasonable refusal)
- Transferring franchisee must provide disclosure to incoming transferee

#### Category 11: Termination — Australian Calibration

- Serious breach: 7 days' notice, no ADR
- Non-serious breach: notice + reasonable cure period
- s 43 (from 1 Nov 2025): compensation for early termination in specified circumstances
- Repurchase obligations for stock, equipment, branded merchandise

#### Category 12: Post-Termination and Restraint of Trade — Australian Calibration

- s 42 analysis (above)
- Common law reasonableness test for restraints not caught by s 42
- Cascading clause assessment
- UCT screening for disproportionate restraints

#### Category 15: Dispute Resolution — Australian Calibration

- Must comply with Code-prescribed process (notice → negotiation → ASBFEO → ADR → court)
- Incompatible dispute resolution clause → **RED**
- ASBFEO name-and-shame powers create enforcement incentive for compliance

#### Category 16: Representations and Acknowledgments — Australian Calibration

- s 18 ACL (misleading or deceptive conduct) cannot be excluded by contract
- Entire agreement clause cannot exclude pre-contractual representation claims under ACL
- Good faith obligation cannot be limited (s 6, civil penalty)

### Step 8: Missing Clause and Gap Detection — Australian Focus

| Gap                                                      | Severity | Basis                     |
| -------------------------------------------------------- | -------- | ------------------------- |
| No good faith acknowledgment                             | YELLOW   | s 6 applies regardless    |
| Good faith limitation clause                             | **RED**  | Civil penalty             |
| No cooling-off period provision                          | **RED**  | Code mandates             |
| No Code-compliant dispute resolution                     | **RED**  | Code mandates             |
| No s 43 compensation provision (from 1 Nov 2025)         | **RED**  | Code mandates             |
| No s 44 return on investment provision (from 1 Nov 2025) | **RED**  | Code mandates             |
| No specific purpose fund reporting                       | YELLOW   | Code mandates regardless  |
| Missing significant capex disclosure (from 1 Nov 2025)   | **RED**  | Schedule 1                |
| No restraint of trade (s 42) carve-out                   | YELLOW   | Code overrides regardless |

### Step 9: ACCC Enforcement Risk Assessment

Assess ACCC enforcement risk based on:

1. **Nature of non-compliance**: UCT, Code breach, misleading conduct, unconscionable conduct
2. **Severity of potential harm**: Financial loss to franchisees, systemic issues
3. **Franchisor's history**: Prior ACCC action, compliance culture
4. **Industry context**: Sector-specific ACCC focus areas
5. **Penalty exposure**: Calculate potential penalties based on breach type

**Recent ACCC enforcement benchmarks:**

| Case                           | Penalty          | Breach Type                                            |
| ------------------------------ | ---------------- | ------------------------------------------------------ |
| _Jump Loops / Campbell_ [2019] | $23M             | Misleading representations (762+ instances)            |
| _Ultra Tune_ [2019]            | $2.014M          | Code breaches (good faith, marketing fund, misleading) |
| _Ultra Tune_ [2024]            | $1.5M (contempt) | Failure to comply with court orders                    |
| _Retail Food Group_ [2022]     | $8M settlement   | Unconscionable conduct, misleading (no admission)      |
| _Mable Technologies_ [2025]    | Pending          | UCT (first case under expanded regime)                 |

### Step 10: Quality Verification

Before delivering analysis, run quality checks per general skill, plus:

1. **Code compliance**: Every Code-related claim cites the specific section
2. **UCT analysis**: Every potentially unfair term assessed against the three-limb test
3. **Transition check**: Correct Code version applied based on agreement date
4. **Good faith**: No provision classified as GREEN that limits good faith obligation
5. **Restraint of trade**: s 42 analysis completed for all post-term restraints

---

## Anti-Patterns — Australia-Specific

1. **Applying US registration analysis**: Australia has no registration requirement. The
   Franchising Code is a mandatory industry code, not a registration regime.

2. **Ignoring the UCT regime**: Since 9 November 2023, unfair terms attract penalties up to
   $50M per contravention. This is not theoretical — ACCC found unfair terms in every
   franchise agreement it reviewed. Treat UCT seriously.

3. **Treating Operations Manual as separate from the agreement**: If the manual is
   incorporated by reference with unilateral change power, manual changes are effectively
   agreement amendments → UCT risk.

4. **Assuming all post-term restraints are enforceable**: s 42 now prohibits restraints in
   non-renewal scenarios where the franchisee met conditions. Common law reasonableness
   still applies to all other restraints.

5. **Ignoring cascading restraint clause analysis**: Cascading clauses are standard
   Australian practice. Analyse each level, not just the broadest.

6. **Missing the good faith civil penalty**: Including a clause that limits good faith is
   itself a Code breach with civil penalty consequences — not just contractual override.

7. **Overlooking s 43 and s 44 timing**: These provisions commence 1 November 2025, not
   1 April 2025. Applying them to agreements entered 1 April – 31 October 2025 is incorrect.

8. **Treating ACCC as passive**: ACCC has an active franchise enforcement record. Recent
   penalties ($23M, $2.014M, $1.5M contempt) demonstrate willingness to act.

9. **Ignoring state-level ADR options**: While the Code provides federal ADR, state Small
   Business Commissioners offer additional (often cheaper) dispute resolution.

10. **Applying "Key Facts Sheet" requirements**: The Key Facts Sheet was removed in the 2025
    Code. Information is now consolidated into the Disclosure Document.

11. **Missing the specific purpose fund broadening**: The 2025 Code expanded "marketing
    funds" to all "specific purpose funds" — any contribution for a specified common purpose.
    Technology fees, training levies, and similar arrangements may now be caught.

12. **Treating franchise agreements as B2B-only**: Australian Consumer Law unfair contract
    terms regime applies to small business standard form contracts including franchises.
    The consumer protection framework applies even in business contexts.

---

## Quality Assurance Framework

### Citation Quality Gates — Australia

| Gate           | Rule                                                             | Fail Action                    |
| -------------- | ---------------------------------------------------------------- | ------------------------------ |
| **Source**     | Every claim cites specific Code section, ACL provision, or case  | Add citation or "[UNVERIFIED]" |
| **Format**     | All citations follow: "Franchising Code s X" or "ACL s Y" format | Fix format                     |
| **Currency**   | Check: 2025 Code or Old Code? 2023 UCT amendments?               | Flag "[CHECK CURRENCY]"        |
| **Domain**     | Australian law only; no cross-jurisdictional bleed               | Confirm jurisdiction           |
| **Confidence** | Uncertainty stated, especially for new provisions (ss 43, 44)    | Add qualifier                  |

### Confidence Scoring

- **Definite (0.95-1.0)**: Clear Code provision with ACCC guidance (e.g., s 6 good faith
  civil penalty)
- **High (0.80-0.94)**: Strong statutory basis with confirming case law (e.g., UCT regime
  applied to franchise agreements)
- **Probable (0.60-0.79)**: Statutory basis with limited judicial interpretation (e.g.,
  s 42 restraint prohibition — new, untested)
- **Possible (0.40-0.59)**: Genuinely open question (e.g., s 44 "reasonable opportunity"
  threshold)
- **Unlikely (0.0-0.39)**: Speculative; flag "[UNCERTAIN]"

---

## Glass Box Audit Trail

```yaml
glass_box:
  agreement: "[Franchise Agreement title and date]"
  franchisor: "[Franchisor name]"
  agreement_type: "[Standard / Multi-unit / Master Franchise / New Vehicle Dealership]"
  user_side: "[Prospective Franchisee / Existing Franchisee / Franchisor]"
  operating_jurisdiction: "Australia — [State/Territory]"
  governing_law: "Australian federal law"
  code_version:
    applicable: "[2025 Code / Old Code (grandfathered)]"
    agreement_date: "[date]"
    ss_43_44_applicable: "[Yes / No — effective 1 November 2025]"
    capex_disclosure_required: "[Yes / No — effective 1 November 2025]"
  applicable_frameworks:
    - "Franchising Code of Conduct 2025 (Competition and Consumer (Industry Codes—Franchising) Regulations 2024)"
    - "Australian Consumer Law (Competition and Consumer Act 2010, Schedule 2)"
    - "Competition and Consumer Act 2010 (Cth)"
    - "[Oil Code of Conduct if applicable]"
  disclosure_document:
    provided: "Yes / No / Opt-out"
    schedule_1_compliant: "Compliant / Deficiencies Found — [list]"
    consideration_period_observed: "Yes / No / Unknown"
    cooling_off_period: "Applicable / Opted Out / Not Applicable"
  uct_analysis:
    terms_screened: "[number]"
    potentially_unfair: "[number] — [list]"
    accc_priority_areas_flagged: "[number]"
  good_faith:
    acknowledged: "Yes / No"
    limited_by_agreement: "Yes (RED) / No"
  restraint_of_trade:
    post_term_present: "Yes / No"
    s_42_analysis: "[Compliant / Non-compliant / Not applicable]"
    cascading_clauses: "Yes / No"
    common_law_reasonableness: "[Reasonable / Unreasonable / Mixed]"
  s_43_compensation: "[Addressed / Not addressed / Not yet applicable]"
  s_44_return_on_investment: "[Addressed / Not addressed / Not yet applicable]"
  specific_purpose_funds:
    identified: "[number]"
    separate_accounts: "Yes / No / Unknown"
    annual_statements: "Available / Not available / Unknown"
  new_vehicle_dealership: "[Yes — ss 45-46 applied / No / Not applicable]"
  dispute_resolution: "[Code-compliant / Non-compliant — [details]]"
  clauses_reviewed: 16
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  legalcode_mcp: "Connected / Not connected"
  statutes_consulted:
    - "Franchising Code of Conduct 2025 — [VERIFIED / UNVERIFIED]"
    - "ACL ss 18, 20-22 — [VERIFIED / UNVERIFIED]"
    - "ACL Part 2-3 (UCT) — [VERIFIED / UNVERIFIED]"
  case_law_consulted:
    - "[Case — VERIFIED / UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Scope limitations, assumptions, caveats]"
  reviewer: "AI-assisted — requires qualified Australian franchise counsel review"
```

---

## Provenance

Created by Legalcode (2026-03-19). Jurisdiction-specific variant of
`legalcode-franchise-agreement-review`. Australian-specific research covering:

- Franchising Code of Conduct 2025 (Competition and Consumer (Industry Codes—Franchising)
  Regulations 2024)
- Australian Consumer Law (Competition and Consumer Act 2010, Schedule 2)
- UCT regime amendments (9 November 2023)
- ACCC franchise enforcement actions (2019-2025)
- Australian restraint of trade doctrine and cascading clause practice
- New vehicle dealership provisions (ss 45-46)
- 2025 Code transition provisions

Research sources:

- [Treasury — Franchising Code of Conduct](https://treasury.gov.au/franchising-code-of-conduct)
- [Treasury — Table of Key Changes](https://treasury.gov.au/publication/p2025-633841)
- [ACCC — Franchising Code of Conduct](https://www.accc.gov.au/business/industry-codes/franchising-code-of-conduct)
- [ACCC — UCT in Franchise Agreements (2023)](https://www.accc.gov.au/about-us/publications/unfair-contract-terms-in-franchise-agreements)
- [ACCC — Guidance on Changes to the Franchising Code](https://www.accc.gov.au/business/industry-codes/franchising-code-of-conduct/guidance-on-changes-to-the-franchising-code)
- [Federal Register of Legislation — 2024 Regulations](https://www.legislation.gov.au/F2024L01605/latest)
- [ASBFEO — Franchising Code and ADR](https://www.asbfeo.gov.au/disputes-assistance/franchising/franchising-code-conduct-and-alternative-dispute-resolution)
