---
name: legalcode-franchise-agreement-review-us-ca
description: Review franchise agreements for California operations against the California Franchise Investment
  Law (Corp. Code §31000-31516) and California Franchise Relations Act (Bus. & Prof. Code §20000-20043)
  — verify DFPI registration and FDD California addendum compliance, screen for non-waivable franchisee
  protections (good cause termination §20020, 60-day cure §20020, 180-day non-renewal notice §20025, transfer
  approval §20028, forum selection §20040.5), analyse post-termination non-compete enforceability under
  Bus. & Prof. Code §16600 (as broadened by AB 1076 and SB 699), review FDD 23-item compliance with California-
  specific addendum requirements (Cal. Use when reviewing any franchise agreement where the franchise
  will operate in California or where the franchisee is domiciled in California — CFRA applies in both
  cases (§20015).
metadata:
  jurisdiction: United States — California
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review franchise agreements for California operations against the California Franchise Investment Law (Corp. Code §31000-31516) and California Franchise Relations Act (Bus. & Prof. Code §20000-20043) — verify DFPI registration and FDD California addendum compliance, screen for non-waivable franchisee protections (good cause termination §20020, 60-day cure §20020, 180-day non-renewal notice §20025, transfer approval §20028, forum selection §20040.5), analyse post-termination non-compete enforceability under Bus. & Prof. Code §16600 (as broadened by AB 1076 and SB 699), review FDD 23-item compliance with California- specific addendum requirements (Cal. Code Regs. tit. 10, §310.114.1), evaluate escrow and financial assurance conditions, assess FAST Act (AB 1228) implications for fast food franchises, and flag anti-reliance disclaimer violations under AB 676. GREEN/YELLOW/RED classification with California-specific redlines, confidence scoring, and Glass Box audit trail. Use when reviewing any franchise agreement where the franchise will operate in California or where the franchisee is domiciled in California — CFRA applies in both cases (§20015). Jurisdiction-specific variant of legalcode-franchise-agreement-review.


# Legalcode Franchise Agreement Review — California

> **Disclaimer**: This skill provides a framework for AI-assisted franchise agreement review
> under California law. It does not constitute legal advice. All outputs require review by a
> California-licensed attorney experienced in franchise law before reliance. California has
> two overlapping franchise statutes — the California Franchise Investment Law (CFIL, Corp.
> Code §31000-31516) and the California Franchise Relations Act (CFRA, Bus. & Prof. Code
> §20000-20043) — plus the broad non-compete ban under Bus. & Prof. Code §16600. These
> statutes are frequently amended; verify current applicability before relying on any
> provision described here. Statutory and case law references cited from memory carry
> hallucination risk — verify against authoritative sources (California Legislature, DFPI,
> court records) before relying on them.

---

## Purpose and Scope

This skill reviews franchise agreements for California compliance, combining FTC federal
requirements with California's robust state-level franchisee protections. California is one
of the most heavily regulated franchise jurisdictions in the United States, with mandatory
registration, non-waivable relationship protections, and the nation's broadest non-compete ban.

**Covers:**

- Full CFIL compliance review — DFPI registration, exemptions, disclosure requirements
- FDD 23-item review with California addendum compliance (Cal. Code Regs. tit. 10, §310.114.1)
- CFRA relationship protections — good cause termination, cure periods, non-renewal, transfer
- Post-termination non-compete analysis under §16600 (as amended by AB 1076, SB 699)
- California escrow and financial assurance requirements
- Forum selection and choice-of-law override analysis (§20040.5)
- AB 676 anti-reliance disclaimer prohibition
- SB 919 franchise broker registration (effective July 1, 2026)
- AB 1228 / FAST Act implications for fast food franchises
- Joint employer exposure analysis (Dynamex ABC test implications)
- GREEN / YELLOW / RED deviation classification with confidence scoring
- Redline generation with California-specific legal basis
- Glass Box audit trail

**Does not:**

- Draft new franchise agreements from scratch
- Provide legal advice or replace qualified California franchise counsel
- Cover non-California franchise law (see `legalcode-franchise-agreement-review` for general;
  jurisdiction-specific variants for AU, UK, EU-FR, Nordics)
- Review franchise broker agreements (see SB 919 requirements below)
- Analyse California employment law beyond franchise-specific provisions

**Related skills:**

- `legalcode-franchise-agreement-review` — General multi-jurisdictional franchise review
- `legalcode-contract-review` — General commercial contract review
- `legalcode-non-compete-enforceability` — US 50-state non-compete enforceability analysis
- `legalcode-nda-triage` — NDA review (often signed before franchise disclosure)
- `legalcode-commercial-lease-review` — Franchise premises lease review

---

## Jurisdiction and Governing Law

### Why California Requires a Dedicated Skill

California franchise law is materially different from every other US state:

1. **Dual-statute regime**: CFIL (registration/disclosure) + CFRA (relationship protections)
   create overlapping but distinct requirements that do not exist in most states
2. **Non-compete ban**: Bus. & Prof. Code §16600 makes post-termination non-competes
   presumptively void — the opposite of most US jurisdictions
3. **Non-waivable protections**: CFRA §20010 voids any contractual waiver of its provisions,
   creating a floor of franchisee rights that cannot be contracted away
4. **DFPI registration**: Active regulatory oversight with examiner comment process, escrow
   requirements, and enforcement actions
5. **Recent legislative activity**: AB 676, AB 1076, SB 699, AB 1228, SB 919 have materially
   changed the landscape since 2023

### CFRA Jurisdictional Reach (§20015)

The CFRA applies when **either**:

- The franchisee is **domiciled in California**, OR
- The franchised business **is or has been operated in California**

This means CFRA protections apply even if the franchise agreement selects another state's
law, provided either nexus exists. A franchise agreement governed by Delaware law but
operating in California must still comply with CFRA.

### Choice-of-Law Analysis

California law does not automatically override out-of-state choice-of-law clauses. Under
_1-800-Got-Junk LLC v. Millennium Asset Recovery Inc._ (2010 Cal. App.), a non-California
choice of law is valid **only if** the chosen state's law provides protections **equal to or
greater than** CFRA. If enforcement would diminish franchisee's rights below the CFRA floor,
the clause is void under §20010.

**Analysis steps:**

1. Identify the governing law in the franchise agreement
2. Compare that state's franchise protections to CFRA requirements
3. If the other state provides equal or greater protections → choice-of-law is valid
4. If CFRA protections exceed the other state's law → CFRA overrides for California operations

---

## California Franchise Investment Law (CFIL) — Corp. Code §31000-31516

### Registration Requirement (§31110)

Every franchisor must register with the DFPI before **any offer or sale** of a franchise in
California. "Offer" includes advertisements, solicitations, and preliminary discussions.

**Registration process:**

- Filing: Uniform Franchise Registration Application + FDD with California addendum +
  audited financial statements + sales agent disclosures + consent to service of process
- Fee: $675 initial registration
- Timeline: Typically 8-12 weeks (includes examiner review and comment letter process)
- Comment letters: DFPI attorneys review applications and commonly issue comment letters
  requiring changes or clarifications — franchisor must respond before registration is granted

**Annual renewal:**

- Due within 110 days after fiscal year end (for calendar year-end: approximately April 20)
- Fee: $1,245
- Must include clean FDD and marked-up copy showing all changes from prior year
- Must be submitted at least 15 business days before current registration expires
- **If registration lapses, application is treated as initial filing**

**RED flag**: If a franchisor is selling franchises in California without current DFPI
registration (and no applicable exemption), the entire transaction is voidable and the
franchisor is subject to DFPI enforcement (desist and refrain orders, consent orders,
civil penalties).

### Registration Exemptions

| Exemption                    | Section      | Key Requirements                                                                                                                     | Disclosure Still Required?   |
| ---------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| **Large Franchisor**         | §31101       | Net worth thresholds; 5+ years in business OR 25+ franchisees                                                                        | Yes — must still provide FDD |
| **Petroleum Distributor**    | §31104       | Petroleum corporation doing business continuously for 5 years; no advance fees                                                       | Limited                      |
| **Fractional Franchise**     | §31108       | Adds product/service line to franchisee's existing business; franchisee has 24+ months in substantially similar business             | Yes                          |
| **Sophisticated Franchisee** | §31109       | Corporate: assets >$5M; Individual: net worth >$1M (excluding home/retirement) OR gross income >$300K/year ($500K joint) for 3 years | Yes                          |
| **Insider**                  | §31106(a)(2) | Partners, officers, directors, or managers already associated with franchisor                                                        | Limited                      |

**Notice filing**: Required for §§31101, 31104, 31108, 31109 — $450 initial, $150 renewal,
$50 amendment. Must be filed once per calendar year before any exempt offer or sale.

**Analysis step**: When reviewing a franchise transaction, verify:

1. Is the franchisor currently registered with DFPI? (Check DFPI database)
2. If not registered, does a valid exemption apply?
3. Was notice filing completed for the applicable exemption?
4. Was an FDD still provided even under an exemption?

### California FDD Addendum Requirements (Cal. Code Regs. tit. 10, §310.114.1)

The California addendum is a mandatory exhibit that overrides conflicting franchise agreement
terms to comply with California law. Required elements:

**California State Cover Page** (immediately follows FTC Rule Cover Page):

- California-specific risk factor disclosures
- Cross-references to California addendum provisions
- DFPI registration number and date

**Item 17 California Modifications** — must include:

| Standard Provision                                | California Override                                                          |
| ------------------------------------------------- | ---------------------------------------------------------------------------- |
| Termination at will or without cause              | **Void** — CFRA requires good cause (§20020)                                 |
| Cure period less than 60 days                     | **Modified** — minimum 60 days (§20020), not to exceed 75 days               |
| Non-renewal without 180-day notice                | **Void** — §20025 requires 180 days                                          |
| Transfer in franchisor's sole discretion          | **Modified** — must meet then-existing non-discriminatory standards (§20028) |
| Out-of-state forum selection                      | **Void** for California claims (§20040.5)                                    |
| Waiver of CFRA protections                        | **Void** — §20010 voids all CFRA waivers                                     |
| Waiver of CFIL protections                        | **Void** — §31512 voids all CFIL waivers                                     |
| Anti-reliance disclaimer                          | **Void** — AB 676 (effective Jan. 1, 2023)                                   |
| General release as condition for renewal/transfer | **Restricted** — cannot require release of CFIL/CFRA claims                  |

**RED flag if missing**: A franchise agreement offered in California without the California
addendum, or with an addendum that does not address all of the above, is a regulatory
compliance deficiency that should be escalated immediately.

### Financial Assurance / Escrow Requirements

The DFPI may impose financial assurance conditions when the franchisor lacks sufficient
financial stability:

1. **Escrow**: Initial franchise fees escrowed with authorized California financial institution
2. **Surety bond**: Bond posted to protect franchisee fees
3. **Fee deferral**: Collection of initial franchise fees deferred until franchisee is open
   for business and all pre-opening obligations are satisfied

**Analysis step**: Check if the DFPI has imposed any financial assurance conditions on this
franchisor's registration. Escrow conditions protect the franchisee's initial investment
but may also indicate franchisor financial instability.

### Private Right of Action and Remedies (§§31300-31302.5)

California franchisees have a statutory private right of action for CFIL violations:

| Remedy                  | Section  | Requirements                           |
| ----------------------- | -------- | -------------------------------------- |
| **Rescission**          | §31300   | Willful violation + reliance + damages |
| **Damages**             | §31301   | Violation caused measurable damages    |
| **Additional remedies** | §31302.5 | Supplementary relief                   |

**Statute of limitations**: 2 years from violation OR 1 year from discovery, whichever
expires first. Cannot be contractually shortened (§31512).

**Both rescission and damages may be sought simultaneously** (Civil Code §1692).

---

## California Franchise Relations Act (CFRA) — Bus. & Prof. Code §20000-20043

### Non-Waiver Rule (§20010)

**"Any condition, stipulation or provision purporting to bind any person to waive compliance
with any provision of this law is contrary to public policy and void."**

This is the single most important provision for franchise agreement review in California.
Every franchise agreement clause must be tested against CFRA requirements — if the clause
provides less protection than CFRA mandates, it is void and the CFRA provision controls.

### Good Cause Termination (§§20020-20021)

**§20020 — General Rule:**
No franchisor may terminate a franchise prior to expiration of its term except for **good
cause**. "Good cause" is limited to the franchisee's **failure to substantially comply with
lawful requirements** of the franchise agreement.

**Cure period requirements:**

- Franchisor must give at least **60 days** to cure a material default
- Cure period shall not exceed **75 days** unless extended by agreement
- Notice must identify the specific default and what constitutes cure

**§20021 — Immediate Termination Without Cure** (10 or fewer days' notice):

| Ground                                                                 | Section   | Standard                                  |
| ---------------------------------------------------------------------- | --------- | ----------------------------------------- |
| Bankruptcy, insolvency, assignment for creditors                       | §20021(a) | Automatic                                 |
| Abandonment — failure to operate 5+ consecutive required business days | §20021(b) | Clear evidence of abandonment             |
| Mutual written agreement                                               | §20021(c) | Must be genuinely mutual                  |
| Material misrepresentation in franchise acquisition                    | §20021(d) | Must be "material"                        |
| Conduct reflecting materially and unfavorably upon system              | §20021(e) | Material + unfavorable                    |
| Failure to comply with applicable laws                                 | §20021(f) | Must be laws, not just internal standards |
| Repeated defaults (even if individually cured)                         | §20021(g) | Pattern of non-compliance                 |
| Failure to timely pay franchisor                                       | §20021(h) | Late payment                              |

**REVIEW CHECKLIST:**

- [ ] Does the agreement restrict termination to "good cause"? If not → RED (§20020 override)
- [ ] Does the agreement provide at least 60-day cure period? If not → RED (§20020 override)
- [ ] Does the agreement allow termination for non-material breaches? → RED (must be
      "substantial" non-compliance)
- [ ] Are the immediate termination grounds limited to §20021 categories? If broader → YELLOW
      (CFRA may override but litigation risk exists)
- [ ] Does the agreement include cross-default across multiple franchise units? → Analyse
      whether cross-default for non-material breach at one unit can trigger termination of
      another — may conflict with good cause requirement

### Non-Renewal Protections (§§20025-20026)

**§20025 — Non-renewal requirements:**

1. At least **180 days prior written notice** of intent not to renew
2. During 180-day period, franchisor must permit franchisee to sell to qualified purchaser
   meeting franchisor's **then-current standards**
3. Non-renewal **cannot** be for purpose of converting franchisee's premises to a
   franchisor-operated location (unless franchisor exercises ROFR)
4. Franchisor may exercise **right of first refusal** to purchase

**REVIEW CHECKLIST:**

- [ ] Does agreement require 180-day non-renewal notice? If less → RED (§20025 override)
- [ ] Does agreement preserve franchisee's right to sell during 180-day period? If
      restricted → RED
- [ ] Does agreement allow non-renewal to convert to company-owned? → RED unless ROFR
      properly exercised
- [ ] Does agreement grant adequate renewal rights? If no renewal right at all → YELLOW
      (CFRA protects against improper non-renewal but does not mandate renewal)

### Transfer Protections (§20028)

**§20028 — Transfer requirements:**

- Franchisor **may not prevent** transfer to person meeting **then-existing, non-discriminatory
  standards**
- Franchisor has **60 days** to approve or disapprove a transfer request
- If no response within 60 days → transfer is **deemed approved**
- If disapproved, franchisor must identify **reasonable grounds**
- Franchisor may exercise ROFR upon receipt of bona fide offer
- Franchisor **cannot impose conditions** on transfer not currently required of new/renewal
  franchisees

**REVIEW CHECKLIST:**

- [ ] Is transfer consent standard "not unreasonably withheld"? If "sole discretion" → RED
      (§20028 overrides)
- [ ] Does agreement provide 60-day response period? If shorter → note CFRA override
- [ ] Does agreement allow franchisor to impose new requirements on transferee beyond
      current standards? → RED (§20028 prohibits)
- [ ] Is ROFR timeline reasonable? Excessive ROFR periods (90+ days) may chill buyer interest
- [ ] Does transferor remain liable after transfer? → YELLOW (common but aggressive)
- [ ] Does death/disability transfer require new franchise fee? → YELLOW

### Forum Selection (§20040.5)

**"A provision in a franchise agreement restricting venue to a forum outside this state is
void with respect to any claim arising under or relating to a franchise agreement involving
a franchise business operating within this state."**

This means:

- Any clause requiring litigation/arbitration outside California is **void** for California
  franchise claims
- The franchisee has the right to bring California franchise claims in California
- This applies to **both litigation and arbitration** venue
- Burden is on the party seeking out-of-state forum to show it would not diminish
  franchisee's substantive rights

**REVIEW CHECKLIST:**

- [ ] Does agreement require out-of-state venue? → RED for California claims (§20040.5 void)
- [ ] Does agreement require out-of-state arbitration? → RED (same override)
- [ ] Does California addendum properly disclaim out-of-state venue requirements? If addendum
      is silent → RED

### Repurchase Obligations (§§20022, 20035-20037)

Even for **lawful** termination or non-renewal, the franchisor must purchase from the
franchisee:

- All **inventory, supplies, equipment, fixtures, and furnishings** purchased in accordance
  with franchise agreement requirements
- At the **price paid** by the franchisee, minus reasonable depreciation (§20022)

For **unlawful** termination or non-renewal:

- Franchisor must offer to repurchase franchisee's resalable current inventory at lower of
  fair wholesale market value or price paid (§20035)
- Franchisor may offset amounts owed (§20036)

**REVIEW CHECKLIST:**

- [ ] Does agreement address repurchase obligations? If silent → note CFRA statutory
      protections apply regardless
- [ ] Does agreement attempt to waive repurchase? → RED (§20010 voids)
- [ ] Does agreement provide for fair valuation of assets on termination?

---

## Non-Compete Analysis — Bus. & Prof. Code §16600

### The California Non-Compete Ban

**§16600**: "Except as provided in this chapter, every contract by which anyone is restrained
from engaging in a lawful profession, trade, or business of any kind is to that extent void."

This is the broadest non-compete ban in the United States. As amended by AB 1076 (effective
January 1, 2024), §16600 must be **"read broadly"** to void any noncompete in any context
unless a statutory exception applies.

### Statutory Exceptions

| Exception                     | Section  | Application to Franchising                                                                                                            |
| ----------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Sale of business goodwill** | §16601   | Seller of goodwill or all ownership interest may agree to refrain from competing within geographic area where business was carried on |
| **Partnership dissolution**   | §16602   | Departing partner may agree not to compete in partnership's geographic area                                                           |
| **LLC dissolution**           | §16602.5 | Similar to partnership exception                                                                                                      |

### Franchise Non-Compete Analysis Framework

**Post-termination non-competes** (franchise ends, franchisor restricts former franchisee):

- **Presumptively VOID** under §16600
- Extremely narrow exception: may be enforceable to protect **trade secrets** only — requires
  showing that the information genuinely constitutes a protectable trade secret under
  California's Uniform Trade Secrets Act, and the non-compete is the least restrictive means
  of protecting it
- The §16601 sale-of-business exception may apply when a franchisee **sells** the franchise
  — the seller can agree not to compete within the franchise territory
- **Post-AB 1076/SB 699 risk**: Even if the agreement is governed by another state's law,
  SB 699 (§16600.5) makes the non-compete unenforceable in California regardless of where
  or when signed

**In-term non-competes** (franchise is active, franchisee restricted from competing):

- Not automatically void, but subject to scrutiny
- _Comedy Club, Inc. v. Improv West Associates_ (553 F.3d 1277, 9th Cir. 2009): In-term
  covenant invalid if it "forecloses competition in a substantial share of the affected line
  of commerce" — **market foreclosure test**
- _Dayton Time Lock Service, Inc. v. Silent Watchman Corp._ (1975 Cal. App.): In-term
  covenant not automatically void — different analysis than post-term
- Court may **blue-pencil** overbroad in-term covenant (limit to specific geography where
  franchisee actually operates)

**Non-solicitation clauses**:

- Customer non-solicitation: likely enforceable during term, likely void post-term under
  §16600 unless narrow trade secret exception applies [VERIFY]
- Employee non-solicitation: generally unenforceable under §16600 post-AB 1076 [VERIFY]

### AB 1076 and SB 699 Impact (Effective January 1, 2024)

**AB 1076 — §16600.1:**

- Codifies broad reading of §16600
- Required employers (by February 14, 2024) to notify all current and former employees
  (employed after January 1, 2022) who signed noncompetes that such agreements are **void**
- Note: This provision was drafted for employment relationships — its application to
  franchise business relationships is an open question, but the broad statutory language
  ("any contract by which anyone is restrained") creates significant risk

**SB 699 — §16600.5:**

- Void noncompetes are unenforceable **regardless of where and when signed**
- Creates **private right of action**: injunctive relief, actual damages, reasonable
  attorney's fees and costs
- Creates **civil violation** for entering into or attempting to enforce a void restrictive
  covenant
- Extends California's ban extraterritorially — a non-compete signed in Texas by a
  franchisee who later operates in California is void under §16600.5

### Non-Compete Review Decision Tree

```
Is there a post-termination non-compete?
├── YES
│   ├── Is the franchise being SOLD (not just terminated)?
│   │   ├── YES → §16601 sale-of-business exception MAY apply
│   │   │   ├── Is scope limited to geographic area of the business? → Likely enforceable
│   │   │   └── Scope exceeds business geography? → Likely unenforceable
│   │   └── NO → Presumptively VOID under §16600
│   │       ├── Does franchisor claim trade secret protection?
│   │       │   ├── YES → Narrow exception; must be genuine trade secret + least restrictive
│   │       │   └── NO → VOID — flag as RED
│   │       └── Was agreement signed outside California?
│   │           └── SB 699 (§16600.5): VOID regardless of where/when signed
│   └── CLASSIFICATION:
│       ├── Post-term non-compete (no sale) → RED — presumptively void
│       ├── Post-term non-compete (with sale, reasonable scope) → YELLOW — may be enforceable
│       └── Post-term non-compete (with sale, overbroad) → RED — likely unenforceable
└── NO → No §16600 issue for post-term

Is there an in-term non-compete?
├── YES
│   ├── Does it foreclose competition in a substantial share of relevant market?
│   │   ├── YES → RED — likely unenforceable (*Comedy Club* test)
│   │   └── NO → YELLOW — may be enforceable but subject to scrutiny
│   └── Is scope limited to actual franchise operations?
│       ├── YES → GREEN — reasonable in-term restriction
│       └── NO → YELLOW to RED depending on breadth
└── NO → No §16600 issue for in-term
```

---

## AB 676 — Anti-Reliance Disclaimer Prohibition (Effective January 1, 2023)

**Key provisions:**

- Franchise agreements may **not** require the franchisee to disclaim reliance on franchisor
  representations or on the FDD
- Franchise agreements may **not** require a general release as a condition for emergency-
  related assistance to the franchisee

**REVIEW CHECKLIST:**

- [ ] Does the agreement contain an acknowledgment that franchisee did not rely on any
      representations? → RED (AB 676 violation)
- [ ] Does the agreement contain a general integration clause that could be read to disclaim
      reliance on FDD representations? → YELLOW (may violate spirit of AB 676)
- [ ] Does the agreement require a general release as condition for renewal, transfer, or
      franchisor assistance? → RED (§20010 + AB 676)

---

## AB 1228 / FAST Act — Fast Food Franchise Considerations (Effective April 1, 2024)

**Applies to**: National fast food chains with **60+ establishments** nationally.

**Key provisions:**

- **$20/hour minimum wage** for fast food workers (effective April 1, 2024)
- **Fast Food Council** (9 members) can set annual wage increases beginning 2025, capped at
  lesser of 3.5% or CPI
- Council can recommend regulations on health/safety, security, protected leave,
  anti-harassment
- **Sunset**: January 1, 2029

**Franchise agreement implications:**

- Does the agreement address minimum wage escalation risk?
- Does the agreement allocate responsibility for FAST Act compliance between franchisor
  and franchisee?
- Are labor cost projections in Item 7 / Item 19 realistic given FAST Act wage increases?
- Does the agreement address potential regulatory changes from the Fast Food Council?

**REVIEW CHECKLIST (fast food franchises only):**

- [ ] Does franchisor's Item 7 (estimated initial investment) account for $20+/hour minimum
      wage? → If using pre-FAST Act estimates → RED
- [ ] Does Item 19 (if present) reflect FAST Act wage increases? → If based on pre-FAST Act
      data → YELLOW
- [ ] Does agreement address cost-sharing for FAST Act compliance obligations?
- [ ] Does agreement address potential additional Fast Food Council regulations?
- [ ] Does agreement address the 2029 sunset and post-sunset planning?

---

## SB 919 — Franchise Broker Registration (Effective July 1, 2026)

**Key provisions:**

- Franchise brokers must **register with DFPI** before offering or selling franchises in
  California
- Broker must provide prospective franchisee with broker's **disclosure document** before
  any communication about franchise opportunities
- Fees: $450 initial, $150 renewal, $50 amendment

**REVIEW CHECKLIST:**

- [ ] Was a franchise broker involved in this transaction?
- [ ] If so, is the broker registered with DFPI? (After July 1, 2026)
- [ ] Did the broker provide their disclosure document before communications?
- [ ] Are broker commissions disclosed in the FDD?

---

## Joint Employer Exposure

### Current State of California Joint Employer Law

The application of the Dynamex ABC test to franchise joint employer status remains
**unresolved** in California:

- _Vazquez v. Jan-Pro_ (9th Cir.): ABC test applies — suggests broader joint employer
  liability for franchisors [VERIFY]
- _Curry v. Equilon_ and _Salazar v. McDonald's_: ABC test does not apply to joint employer
  context [VERIFY]
- California Supreme Court has not directly addressed the issue

**Federal developments:**

- **American Franchise Act** (H.R. 5267 / S. 3525, introduced Sept./Dec. 2025): Would codify
  that franchisor is joint employer **only** if it exercises "substantial direct and
  immediate control" over essential employment terms. Pending. [VERIFY]

**REVIEW CHECKLIST:**

- [ ] Does the agreement contain operational control provisions that could create joint
      employer liability? (Direct control over hiring, firing, wages, scheduling, training)
- [ ] Does the agreement disclaim joint employer status? (Necessary but not sufficient)
- [ ] Does the agreement contain indemnification for joint employer claims?
- [ ] For fast food franchises: additional scrutiny given FAST Act regulatory environment

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when the answer would change the direction of analysis.

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

### Step 1: Accept Agreement and Identify California Nexus

Accept the franchise agreement and immediately determine California applicability:

**⟁ CLARIFY** — California nexus determination:

1. **Franchise will operate in California**: CFRA applies; CFIL registration required
   (unless exempt); §16600 non-compete ban applies
2. **Franchisee is domiciled in California but franchise operates elsewhere**: CFRA applies
   (§20015); CFIL may apply if offer made in California; §16600 may apply (SB 699)
3. **Neither**: This skill is not the primary tool — use `legalcode-franchise-agreement-review`
   for general review, with California analysis only if cross-border issues arise

### Step 2: Accept FDD and California Addendum

**⟁ CLARIFY** — FDD and addendum status:

1. **FDD with California addendum provided**: Full compliance review against both FTC Rule
   and California addendum requirements
2. **FDD provided without California addendum**: Flag as **RED** — California addendum is
   mandatory for any franchise offered in California
3. **No FDD provided**: Flag as **RED** — potential CFIL violation if franchise offered in
   California without registered FDD. Determine if exemption applies.
4. **FDD exists but unavailable**: Recommend obtaining before signing. Note that signing
   without receiving FDD 14 days prior triggers rescission rights.

### Step 3: Gather California-Specific Context

**⟁ CLARIFY** — In addition to standard franchise review context (side, model, industry,
deal stage, risk tolerance per general skill), ask:

1. **Is this a fast food franchise covered by AB 1228?**
   - Options: Yes (national chain, 60+ establishments) / No / Uncertain
   - _Why this matters_: FAST Act creates $20+/hour minimum wage and regulatory council
     authority — materially affects financial projections and operational obligations

2. **Was a franchise broker involved?**
   - Options: Yes / No / Uncertain
   - _Why this matters_: SB 919 (effective July 1, 2026) requires broker registration and
     disclosure. Broker involvement also raises FDD disclosure obligations.

3. **Is the franchisor currently registered with DFPI?**
   - Options: Yes / No / Uncertain — will verify
   - _Why this matters_: Unregistered franchise offering is a CFIL violation with rescission
     remedies available to franchisee

### Step 4: DFPI Registration Verification

Before proceeding to clause-by-clause analysis, verify DFPI registration status:

1. Check DFPI franchise registration database for franchisor's current registration
2. If registered: note registration number, effective date, any conditions (escrow, bond)
3. If not registered: determine if valid exemption applies (§§31101, 31104, 31108, 31109)
4. If neither registered nor exempt: **RED** — potential CFIL violation; franchisee may
   have rescission rights under §31300

### Step 5: California Addendum Compliance Review

If FDD with California addendum is available, verify all required California modifications
are present:

| Required Modification                         | Present? | Compliant? |
| --------------------------------------------- | -------- | ---------- |
| Good cause termination (§20020)               | [ ]      | [ ]        |
| 60-day cure period (§20020)                   | [ ]      | [ ]        |
| 180-day non-renewal notice (§20025)           | [ ]      | [ ]        |
| Transfer approval standards (§20028)          | [ ]      | [ ]        |
| Forum selection — California venue (§20040.5) | [ ]      | [ ]        |
| Non-waiver of CFRA (§20010)                   | [ ]      | [ ]        |
| Non-waiver of CFIL (§31512)                   | [ ]      | [ ]        |
| Anti-reliance disclaimer prohibition (AB 676) | [ ]      | [ ]        |
| General release restrictions (AB 676)         | [ ]      | [ ]        |
| DFPI registration number                      | [ ]      | [ ]        |

**Any missing or non-compliant modification → RED**

### Step 6: Clause-by-Clause Analysis (California-Calibrated)

Apply the same 16-category framework from the general franchise review skill, but with
California-specific calibration at each category:

#### Category 1: Initial Franchise Fee — California Calibration

**Additional California analysis:**

- Are escrow or fee deferral conditions imposed by DFPI?
- Is the fee consistent with FDD Item 5 **and** any California addendum modifications?
- If DFPI required fee deferral, does the agreement comply?

#### Category 2: Ongoing Royalties and Fees — California Calibration

**Additional California analysis:**

- Late payment penalties: California does not have specific franchise fee regulations, but
  the general penalty/liquidated damages analysis applies (Civil Code §1671)
- Technology fees: unlimited unilateral increase authority → YELLOW (may conflict with
  implied covenant of good faith under CFRA)

#### Category 3: Territory — California Calibration

**Additional California analysis:**

- Encroachment: No statutory protection, but implied covenant of good faith applies
  (_Bryman v. El Pollo Loco_) [VERIFY]
- Even without exclusive territory, franchisor cannot act to "destroy the franchisee's
  right to enjoy the fruits of the contract"
- Express contract language disclaiming exclusive territory can defeat encroachment claims —
  but if combined with development schedule requirements and ROFR on prime locations,
  the practical effect may still constitute actionable bad faith

#### Category 4: IP and Trademark — California Calibration

**No material California-specific variation** from general framework.

#### Category 9: Term, Renewal, Extension — California Calibration

**Critical California analysis:**

- **180-day non-renewal notice**: Agreement must provide at least 180 days (§20025)
- During 180-day period, franchisee must be permitted to sell to qualified buyer
- Non-renewal cannot be used to convert to company-owned location (§20025)
- Renewal on "then-current" terms → YELLOW (CFRA does not require renewal, but §20010
  requires good faith in all dealings)

#### Category 10: Transfer — California Calibration

**Critical California analysis:**

- Consent standard: "sole discretion" → RED (§20028 requires then-existing non-discriminatory
  standards)
- 60-day deemed approval: if franchisor does not respond within 60 days, transfer is deemed
  approved (§20028)
- Conditions on transfer: franchisor cannot impose conditions not required of new/renewal
  franchisees (§20028)
- ROFR: permitted, but timing and scope should be reasonable

#### Category 11: Termination — California Calibration

**Critical California analysis:**

- Good cause required: §20020 — failure to substantially comply with lawful requirements
- 60-day cure: minimum cure period for curable defaults (§20020)
- 75-day maximum: cure period shall not exceed 75 days unless extended by agreement
- Immediate termination limited to §20021 grounds (bankruptcy, abandonment, misrepresentation,
  etc.)
- **Repurchase obligation on termination**: §20022 requires franchisor to purchase inventory,
  supplies, equipment, fixtures purchased per agreement requirements

#### Category 12: Post-Termination and Non-Compete — California Calibration

**Critical California analysis — this is where California most differs:**

| Provision                                    | General US                          | California                                                       |
| -------------------------------------------- | ----------------------------------- | ---------------------------------------------------------------- |
| Post-term non-compete (1-2 years, territory) | Generally enforceable if reasonable | **VOID** under §16600 (no reasonableness analysis)               |
| Post-term non-compete (franchise sold)       | Enforceable if reasonable           | **May be enforceable** under §16601 sale-of-business exception   |
| In-term non-compete                          | Enforceable                         | **Subject to market foreclosure test** (_Comedy Club_)           |
| Customer non-solicitation post-term          | Usually enforceable                 | **Likely VOID** under §16600 post-AB 1076                        |
| Employee non-solicitation post-term          | Usually enforceable                 | **VOID** under §16600 post-AB 1076                               |
| Confidentiality post-term                    | Enforceable                         | **Enforceable** — trade secret protection not affected by §16600 |
| De-identification                            | Standard                            | Standard — not affected by §16600                                |

**Redline guidance for post-term non-compete in California:**

If the agreement contains a post-termination non-compete:

```
**Current language**: "[Non-compete provision]"
**Proposed redline**: "This Section [X] shall not apply to franchisees operating in
California or domiciled in California, as post-termination non-compete provisions are void
under California Business and Professions Code §16600. Notwithstanding the foregoing,
Franchisee's obligations regarding confidential information and trade secrets under Section
[Y] survive termination in accordance with applicable law, including the California Uniform
Trade Secrets Act."
**Rationale**: California Bus. & Prof. Code §16600 voids post-termination non-compete
provisions. AB 1076 (effective January 1, 2024) codifies that §16600 must be read broadly.
SB 699 (§16600.5) makes this provision unenforceable regardless of where or when signed.
**Legal basis**: Cal. Bus. & Prof. Code §§16600, 16600.1, 16600.5
**Priority**: Must-have — provision is void as matter of law
**Fallback**: At minimum, California addendum must exclude California from non-compete scope
```

#### Category 15: Dispute Resolution — California Calibration

**Critical California analysis:**

- Out-of-state forum: **VOID** for California franchise claims (§20040.5)
- Arbitration: permitted if standards are not less than CFRA requirements and arbitrators
  chosen from AAA or impartial panel (§20040)
- Class action waivers: increasingly challenged in California; PAGA representative actions
  may not be waivable [VERIFY]
- Jury waivers: generally enforceable in California if knowing and voluntary [VERIFY]

#### Category 16: Representations and Acknowledgments — California Calibration

**Critical California analysis:**

- Anti-reliance disclaimer: **VOID** under AB 676
- General release: restricted under AB 676 (cannot be condition for emergency assistance)
- Waiver of CFIL/CFRA claims: **VOID** under §§31512, 20010
- Integration clause: valid, but cannot override FDD representations (AB 676)

### Step 7: Missing Clause and Gap Detection — California Focus

**California-specific gaps to flag:**

| Gap                                         | Severity | Basis                                 |
| ------------------------------------------- | -------- | ------------------------------------- |
| No California addendum                      | RED      | Cal. Code Regs. tit. 10, §310.114.1   |
| No good cause termination provision         | RED      | CFRA §20020 (but CFRA applies anyway) |
| No 180-day non-renewal notice               | RED      | CFRA §20025                           |
| No repurchase obligation on termination     | YELLOW   | CFRA §20022 applies regardless        |
| No California venue provision               | RED      | CFRA §20040.5                         |
| No FAST Act wage acknowledgment (fast food) | YELLOW   | AB 1228                               |
| No anti-reliance language in addendum       | YELLOW   | AB 676                                |
| No DFPI registration number on cover page   | RED      | CFIL registration required            |

### Step 8: Flag Deviations, Generate Redlines, Business Impact

Apply the same GREEN/YELLOW/RED framework from the general skill, but with California-
specific legal basis for each classification. Every California-specific deviation should
cite the relevant California statute.

### Step 9: DFPI Enforcement Risk Assessment

For any RED items that involve CFIL violations (unregistered sale, missing addendum, etc.),
assess enforcement risk:

**Recent DFPI enforcement actions for context:**

- Noble Franchising, Inc. (Feb. 2025) — Consent order for offering 4+ unregistered franchises
- Path to Prosperity, LLC (Dec. 2024) — Consent order for selling 9 unregistered "territory
  holder agreements"
- Xpotential Fitness, Inc. (Nov. 2024) — Consent order [VERIFY]
- Alleviant Health Centers, LLC (2019) — Citation with desist and refrain order [VERIFY]

**Enforcement tools available to DFPI:**

- Desist and refrain orders (§31402)
- Consent orders
- Citations and administrative penalties
- Civil actions
- Referral to Attorney General

### Step 10: Quality Verification

Before delivering analysis, run quality checks per general skill, plus:

1. **California statute verification**: Every California-specific claim must cite a specific
   statute section (Corp. Code §, Bus. & Prof. Code §, Cal. Code Regs. §)
2. **CFRA non-waiver check**: Confirm that any contract term classified as GREEN would not
   be overridden by a CFRA provision that provides greater protection
3. **§16600 compliance**: Confirm all non-compete analysis applies the broad California
   standard, not the reasonableness standard used in other states
4. **AB 676 check**: Confirm no anti-reliance disclaimers accepted as GREEN

---

## Key California Franchise Case Law

### Non-Compete Enforceability

- **_Comedy Club, Inc. v. Improv West Associates_** (553 F.3d 1277, 9th Cir. 2009):
  In-term covenant invalid if it forecloses competition in substantial share of affected
  commerce; blue-penciling remedy applied. Key precedent for in-term franchise non-compete
  analysis in California. [VERIFY]

- **_Dayton Time Lock Service, Inc. v. Silent Watchman Corp._** (1975, Cal. App. 3d 52):
  In-term non-compete not automatically void; different analysis than post-term. Post-term
  non-compete conceded as violating §16600. [VERIFY]

### Forum Selection / Choice of Law

- **_1-800-Got-Junk LLC v. Millennium Asset Recovery Inc._** (2010 Cal. App.): CFRA §20010
  only voids choice-of-law provision if enforcement would **diminish** franchisee's CFRA
  rights below statutory floor. Washington law upheld because it was more protective. [VERIFY]

### Encroachment

- **_Bryman v. El Pollo Loco, Inc._** (Cal. Super. Ct.): Opening nearby franchisor-owned
  location may breach implied covenant of good faith, even without exclusive territory
  grant. [VERIFY]

### CFIL Private Action

- Both rescission and damages may be sought simultaneously (Civil Code §1692 applied to
  CFIL claims per _Mortensonist Taggart Adams_ analysis). [VERIFY]

---

## Anti-Patterns — California-Specific

What NOT to do in California franchise agreement review:

1. **Applying "reasonableness" to post-term non-competes**: California does not use a
   reasonableness test. Post-term non-competes are void. Period. Do not analyse duration,
   geography, or scope as if the clause could be saved by narrowing it.

2. **Treating the California addendum as optional**: The addendum is required by regulation
   (Cal. Code Regs. tit. 10, §310.114.1). Missing addendum = regulatory deficiency.

3. **Accepting out-of-state forum selection**: §20040.5 voids this for California franchise
   claims. Do not classify as YELLOW — it is RED.

4. **Ignoring the 60-day cure minimum**: Many franchise agreements provide 30-day cure
   periods. In California, this is overridden by CFRA §20020 — minimum 60 days. Do not
   treat 30-day cure as merely suboptimal; it is legally deficient.

5. **Missing the deemed-approval on transfer**: If the agreement does not provide for 60-day
   response on transfer requests, note that CFRA §20028 creates a deemed-approval right
   after 60 days regardless of contract language.

6. **Conflating CFIL and CFRA violations**: CFIL violations (registration, disclosure) create
   rescission rights and DFPI enforcement exposure. CFRA violations (termination, non-renewal,
   transfer) create franchisee relationship protections. Both may apply simultaneously but
   the remedies differ.

7. **Ignoring SB 699 for out-of-state agreements**: A franchise agreement signed in another
   state with a non-California choice of law still cannot enforce a non-compete against a
   California franchisee. §16600.5 makes void non-competes unenforceable regardless of
   where or when signed.

8. **Overlooking AB 676 anti-reliance provisions**: Franchise agreements commonly include
   acknowledgments that the franchisee did not rely on any representations beyond the FDD.
   Since January 1, 2023, these are void in California.

9. **Failing to check DFPI escrow conditions**: A franchisor may be registered but subject
   to escrow or fee deferral conditions. If the agreement collects fees that should be
   escrowed, this is a compliance failure.

10. **Treating FAST Act as irrelevant for non-fast-food**: While AB 1228 directly applies
    only to fast food chains with 60+ locations, it signals California's regulatory direction
    on franchise labor practices. Broader franchise worker protection legislation is possible.

11. **Accepting "standard" California addendum language**: Some franchisors use boilerplate
    California addenda that track statutory language without substantive modifications.
    Verify the addendum actually modifies the agreement terms, not merely restates the law.

12. **Missing the CFRA "floor" concept**: CFRA sets minimum protections. If the franchise
    agreement provides greater protections in some areas, those survive. But any provision
    providing less than CFRA minimum is void (§20010).

---

## Quality Assurance Framework

### Citation Quality Gates — California

| Gate           | Rule                                                                                                         | Fail Action                         |
| -------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| **Source**     | Every California-specific claim cites Corp. Code §, Bus. & Prof. Code §, or Cal. Code Regs. §                | Add citation or mark "[UNVERIFIED]" |
| **Format**     | All California statute citations follow standard format: "Bus. & Prof. Code §20020"                          | Fix format                          |
| **Currency**   | Check for recent amendments (AB 676, AB 1076, SB 699, AB 1228, SB 919)                                       | Flag "[CHECK CURRENCY]"             |
| **Domain**     | California law applies only to franchises with California nexus (§20015)                                     | Confirm nexus before applying       |
| **Confidence** | Uncertainty explicitly stated, especially for evolving areas (joint employer, AB 1076 franchise application) | Add confidence qualifier            |

### Self-Interrogation for RED Items

Apply 3-pass review per general skill, plus California-specific pass:

**Pass 4 — California Override Check**:

- Does CFRA provide a non-waivable protection that overrides this contract term?
- Would §16600 void this provision in California even if enforceable elsewhere?
- Has recent legislation (2023-2026) changed the analysis?
- Is there DFPI enforcement precedent on this issue?

### Confidence Scoring

Per general skill framework, with additional calibration:

- **Definite (0.95-1.0)**: Clear California statute directly on point (e.g., §16600 voiding
  post-term non-compete)
- **High (0.80-0.94)**: Strong statutory basis with confirming case law (e.g., §20040.5
  voiding out-of-state forum)
- **Probable (0.60-0.79)**: Statutory basis with unresolved questions (e.g., AB 1076
  application to franchise non-competes)
- **Possible (0.40-0.59)**: Genuinely open question (e.g., Dynamex ABC test application
  to franchise joint employer)
- **Unlikely (0.0-0.39)**: Speculative; flag "[UNCERTAIN]"

---

## Glass Box Audit Trail

Every California franchise agreement review output MUST include:

```yaml
glass_box:
  agreement: "[Franchise Agreement title and date]"
  franchisor: "[Franchisor name]"
  agreement_type: "[Single-unit / Multi-unit / Area Development / Master Franchise]"
  user_side: "[Prospective Franchisee / Existing Franchisee / Franchisor]"
  operating_jurisdiction: "California"
  governing_law: "[Per agreement — note if non-California and CFRA override applies]"
  california_nexus: "[Operations in CA / Franchisee domiciled in CA / Both]"
  applicable_frameworks:
    - "FTC Franchise Rule (16 C.F.R. Part 436)"
    - "California Franchise Investment Law (Corp. Code §31000-31516)"
    - "California Franchise Relations Act (Bus. & Prof. Code §20000-20043)"
    - "California Non-Compete Ban (Bus. & Prof. Code §16600, AB 1076, SB 699)"
    - "[AB 676 if applicable]"
    - "[AB 1228 / FAST Act if fast food]"
  dfpi_registration:
    status: "[Registered / Exempt / Not Registered / Unknown]"
    registration_number: "[if available]"
    conditions: "[Escrow / Bond / Fee Deferral / None / Unknown]"
  california_addendum:
    present: "Yes / No"
    compliant: "Compliant / Deficiencies Found — [list]"
  disclosure_document_reviewed: "Yes / No / Not Provided"
  disclosure_compliance: "Compliant / Deficiencies Found / Not Reviewed"
  non_compete_analysis:
    post_term: "[VOID under §16600 / §16601 exception applies / Not present]"
    in_term: "[Market foreclosure test applied / Not present]"
    non_solicitation: "[VOID under §16600 / Not present]"
  cfra_compliance:
    good_cause_termination: "[Compliant / Non-compliant — §20020 override]"
    cure_period: "[≥60 days / <60 days — §20020 override]"
    non_renewal_notice: "[≥180 days / <180 days — §20025 override]"
    transfer_standard: "[Non-discriminatory / Sole discretion — §20028 override]"
    forum_selection: "[California / Out-of-state — §20040.5 void]"
    anti_reliance: "[Absent / Present — AB 676 void]"
  fast_food_analysis: "[AB 1228 applicable / Not applicable]"
  broker_analysis: "[SB 919 applicable / Not applicable / Pre-effective date]"
  clauses_reviewed: 16
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  legalcode_mcp: "Connected / Not connected"
  statutes_consulted:
    - "Corp. Code §31000-31516 (CFIL) — [VERIFIED / UNVERIFIED]"
    - "Bus. & Prof. Code §20000-20043 (CFRA) — [VERIFIED / UNVERIFIED]"
    - "Bus. & Prof. Code §16600-16601 — [VERIFIED / UNVERIFIED]"
    - "Bus. & Prof. Code §16600.1 (AB 1076) — [VERIFIED / UNVERIFIED]"
    - "Bus. & Prof. Code §16600.5 (SB 699) — [VERIFIED / UNVERIFIED]"
  case_law_consulted:
    - "[Case 1 — VERIFIED or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Scope limitations, assumptions, caveats]"
  reviewer: "AI-assisted — requires qualified California franchise counsel review"
```

---

## Output Format Template

Structure the final deliverable as:

```markdown
## California Franchise Agreement Review

**Franchisor**: [name]
**Agreement Type**: [Single-unit / Multi-unit / Area Development / Master Franchise]
**Your Side**: [Prospective Franchisee / Existing Franchisee / Franchisor]
**Operating Jurisdiction**: California — [city/county if known]
**Governing Law**: [Per agreement]
**Industry**: [QSR / Retail / Services / etc.]
**FAST Act Applicable**: [Yes / No]
**Review Date**: [date]

---

## DFPI Registration Status

**Registered**: [Yes / No / Exempt]
**Registration Number**: [if available]
**Conditions**: [Escrow / Bond / Fee Deferral / None]

---

## California Addendum Compliance

[Table of required modifications and compliance status]

---

## California-Specific Key Findings

[Top findings unique to California analysis — §16600 non-compete, CFRA overrides, DFPI issues]

---

## FDD / Disclosure Compliance

[Per general skill, with California addendum findings]

---

## Clause-by-Clause Analysis (California-Calibrated)

[Per general skill, with California legal basis for each classification]

---

## Non-Compete Analysis

[Dedicated §16600 analysis — post-term, in-term, non-solicitation]

---

## CFRA Compliance Summary

[Table of CFRA protections and agreement compliance]

---

## Negotiation Strategy (California-Informed)

[Priority items with California legal leverage]

---

## Glass Box Audit Trail

[YAML block per Glass Box section above]
```

---

## Provenance

Created by Legalcode (2026-03-19). Jurisdiction-specific variant of
`legalcode-franchise-agreement-review`. California-specific research covering:

- California Franchise Investment Law (Corp. Code §31000-31516)
- California Franchise Relations Act (Bus. & Prof. Code §20000-20043)
- California Non-Compete Ban (Bus. & Prof. Code §16600, AB 1076 §16600.1, SB 699 §16600.5)
- AB 676 Anti-Reliance Disclaimer Prohibition
- AB 1228 / FAST Act Fast Food Franchise Worker Protections
- SB 919 Franchise Broker Registration Law
- DFPI franchise registration and enforcement actions (2019-2025)
- California franchise case law (_Comedy Club_, _Dayton Time Lock_, _1-800-Got-Junk_,
  _Bryman v. El Pollo Loco_)

Research sources:

- [DFPI — About the Franchise Investment Law](https://dfpi.ca.gov/regulated-industries/franchises/about-the-franchise-investment-law/)
- [DFPI — California Franchise Relations Act](https://dfpi.ca.gov/rules-enforcement/laws-and-regulations/regulations-and-legislation-franchise-investment-law/california-franchise-relations-act/)
- [DFPI — Filing Instructions](https://dfpi.ca.gov/instructions-on-how-to-file-a-complete-franchise-application/)
- [California Legislature — Bus. & Prof. Code §16600](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=16600.)
- [FTC Franchise Rule (16 C.F.R. Part 436)](https://www.ftc.gov/legal-library/browse/rules/franchise-rule)
- [NASAA Post-Term Non-Compete Analysis](https://www.nasaa.org/wp-content/uploads/2025/01/Post-Term-Non-Compete-Provisions-in-Franchise-Agreements-Should-Be-Reasonable.pdf)
