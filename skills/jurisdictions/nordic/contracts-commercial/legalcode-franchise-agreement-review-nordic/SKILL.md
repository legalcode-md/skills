---
name: legalcode-franchise-agreement-review-nordic
description: Review franchise agreements for operations in Norway, Sweden, Denmark, Finland or Iceland.
  Assess disclosure, unfair terms, competition restrictions, non-competes, termination and dispute resolution
  under the applicable national and EU/EEA rules. Produce prioritized findings, confidence assessments
  and an auditable review.
metadata:
  jurisdiction: Nordic (Norway, Sweden, Denmark, Finland, Iceland)
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review franchise agreements for Nordic operations (Norway, Sweden, Denmark, Finland, Iceland) — analyse against the Swedish Franchise Disclosure Act (Lag 2006:484, the only Nordic franchise-specific statute), apply the shared Nordic Contracts Act Section 36 (unreasonable terms) and Section 38 (non-compete) framework across all five jurisdictions, verify EU/EEA VBER 2022/720 compliance for competition law obligations (RPM, territory, online sales, post-term non-compete: 1-year max, premises-only, know-how indispensable), distinguish between commercial franchise non-competes (Contracts Act §38, no compensation required) and employment non-competes (mandatory compensation in all Nordics: Norway WEA 14A, Sweden ~60%, Denmark 60%, Finland 40-60%), evaluate rupture brutale-equivalent notice requirements for termination/non-renewal under Nordic good faith principles, assess arbitration clause prevalence (90%+ in Sweden) and enforceability, review EFF/BFA Code of Ethics compliance for national franchise association members, and address small-market dynamics for Iceland (~380,000 population). GREEN/YELLOW/RED classification with confidence scoring and Glass Box audit trail. Use when reviewing franchise agreements for operations in any Nordic country. Jurisdiction-specific variant of legalcode-franchise-agreement-review.


# Legalcode Franchise Agreement Review — Nordic Countries

> **Disclaimer / Ansvarsfraskrivelse**: This skill provides a framework for AI-assisted
> franchise agreement review under Nordic law. It does not constitute legal advice
> (juridisk rådgivning). All outputs require review by a qualified lawyer in the relevant
> Nordic jurisdiction before reliance. Nordic franchise law is primarily governed by general
> contract law, competition law, and industry self-regulation — only Sweden has franchise-
> specific legislation (Lag 2006:484). The legal framework varies between countries despite
> shared Contracts Act heritage. Verify current law in the specific jurisdiction. Statutory
> and case law references cited from memory carry hallucination risk — verify against
> authoritative sources before relying on them.

---

## Purpose and Scope

This skill reviews franchise agreements for operations in the five Nordic countries: Norway,
Sweden, Denmark, Finland, and Iceland. Despite shared legal heritage (the joint Nordic
Contracts Act drafting process of the early 20th century), each country has distinct
features. Only Sweden has franchise-specific legislation. All five share EU/EEA competition
law obligations through the VBER. The Nordic model emphasises freedom of contract,
arbitration, and industry self-regulation through national franchise associations affiliated
with the European Franchise Federation (EFF).

**Covers:**

- Swedish Franchise Disclosure Act (Lag 2006:484) compliance (Sweden only)
- Contracts Act Section 36 (unreasonable terms) analysis across all Nordics
- Contracts Act Section 38 (non-compete) enforceability across all Nordics
- EU/EEA VBER 2022/720 competition law compliance
- Post-term non-compete analysis: commercial (§38) vs. employment distinction
- Termination and non-renewal notice requirements under good faith principles
- Arbitration clause assessment (90%+ prevalence in Swedish franchise agreements)
- National franchise association (EFF) Code of Ethics compliance
- Small-market considerations (Iceland)
- Lease/franchise agreement interaction (critical in Sweden)
- GREEN / YELLOW / RED deviation classification with confidence scoring
- Glass Box audit trail

**Does not:**

- Draft new franchise agreements from scratch
- Provide legal advice or replace qualified Nordic counsel
- Cover non-Nordic franchise law (see `legalcode-franchise-agreement-review` for general;
  jurisdiction-specific variants for US-CA, AU, UK, EU-FR)
- Provide employment law advice beyond franchise-specific non-compete distinction
- Cover oil/petroleum franchise arrangements

**Related skills:**

- `legalcode-franchise-agreement-review` — General multi-jurisdictional franchise review
- `legalcode-non-compete-analysis-is` — Iceland non-compete enforceability analysis
- `legalcode-contract-review` — General commercial contract review

---

## Jurisdiction Matrix

### Country-by-Country Overview

| Feature                        | Norway             | Sweden                   | Denmark           | Finland         | Iceland            |
| ------------------------------ | ------------------ | ------------------------ | ----------------- | --------------- | ------------------ |
| **Franchise-specific law**     | No                 | **Yes** (Lag 2006:484)   | No                | No              | No                 |
| **Pre-contractual disclosure** | None required      | Mandatory (SFDA)         | None required     | None required   | None required      |
| **Disclosure timing**          | N/A                | "In due time" (~14 days) | N/A               | N/A             | N/A                |
| **EU/EEA status**              | EEA (EFTA)         | EU                       | EU                | EU              | EEA (EFTA)         |
| **VBER application**           | Indirect (via EEA) | Direct                   | Direct            | Direct          | Indirect (via EEA) |
| **Contracts Act**              | Avtaleloven        | Avtalslagen              | Aftaleloven       | Oikeustoimilaki | Lög 7/1936         |
| **§36 (unfair terms)**         | Yes                | Yes                      | Yes               | Yes             | Yes                |
| **§38 (non-compete)**          | Yes                | Yes                      | Yes               | Yes             | Yes                |
| **Franchise association**      | NFF                | SFF                      | Franchise Danmark | FFA             | None (EFF)         |
| **Arbitration prevalence**     | High               | Very high (90%+)         | High              | High            | Moderate           |
| **Population**                 | ~5.5M              | ~10.5M                   | ~5.9M             | ~5.6M           | ~380K              |
| **Franchise systems**          | 400+               | 900+                     | N/A               | 250-300         | Limited            |

### When to Use This Skill vs. Country-Specific Analysis

Use this skill for:

- Review of franchise agreements operating in any Nordic country
- Multi-Nordic franchise networks (one master franchisee covering multiple countries)
- Comparative analysis across Nordic jurisdictions
- International brands entering the Nordic market

For deep-dive Iceland non-compete analysis, also use `legalcode-non-compete-analysis-is`.

---

## Sweden — Franchise Disclosure Act (Lag 2006:484)

### The Only Nordic Franchise-Specific Statute

Sweden is the **only Nordic country** with franchise-specific legislation. The Swedish
Franchise Disclosure Act (SFDA) comprises 6 sections.

**Definition (Section 1):** An agreement where a franchisor agrees that, in return for
compensation, the franchisee shall use the franchisor's special business concept for
marketing and selling goods/services, use the franchisor's trademark or other IP rights,
and participate in recurring controls.

### Disclosure Requirements (Section 3)

The franchisor must provide written information that is **clear and understandable** about:

| Item | Required Information                                                      |
| ---- | ------------------------------------------------------------------------- |
| 1    | Description of the franchise activity                                     |
| 2    | Information about other franchisees and volume of their activity          |
| 3    | Compensation the franchisee shall pay                                     |
| 4    | IP rights to be granted                                                   |
| 5    | Goods/services the franchisee must purchase or rent                       |
| 6    | Non-competition undertakings (during and after agreement)                 |
| 7    | Terms: modification, prolongation, termination, and economic consequences |
| 8    | Dispute resolution and cost allocation                                    |
| 9    | Other conditions necessary given the circumstances                        |

**Timing:** "In due time" before the franchise agreement is concluded. Legislative history
indicates **14 calendar days to 3 weeks** as sufficient; less than 14 days acceptable only
in exceptional circumstances.

### Penalties for Non-Compliance

**Key limitation:** The SFDA has **no deterrent remedies**:

- A franchisor who fails to disclose may be **ordered by the Patent and Market Court**
  (Patent- och marknadsdomstolen) to comply
- The court may impose a **fine** (vite) payable to the government
- Non-compliance does **NOT**: affect agreement validity, entitle franchisee to terminate,
  or entitle franchisee to damages
- **However**: omitted information could render clauses void under Contracts Act **§36**
  (unreasonable terms)

**REVIEW CHECKLIST (Sweden only):**

- [ ] Was SFDA-compliant disclosure provided? → If not → YELLOW (no direct remedy, but §36
      exposure)
- [ ] Was disclosure provided at least 14 days before signing? → If less → YELLOW
- [ ] Does disclosure cover all 9 mandatory items? → Missing items → YELLOW
- [ ] Are non-compete terms clearly disclosed (Item 6)? → If not → RED (could render
      non-compete void under §36)
- [ ] Are termination consequences disclosed (Item 7)? → If not → YELLOW

---

## Nordic Contracts Act Framework

### Section 36 — Unreasonable Terms

All five Nordic Contracts Acts contain Section 36, permitting courts to modify or set aside
contractual terms that are **unreasonable** (urimelig / oskälig / kohtuuton).

**Application to franchise agreements:**

- Historically, Nordic courts have been **restrictive** in applying §36 to commercial
  agreements, giving weight to freedom of contract between business parties
- This is **evolving** — particularly in Sweden, where courts are becoming more willing to
  intervene in commercial agreements
- Factors considered: bargaining power, fairness, changed circumstances, industry practice

**REVIEW CHECKLIST — §36 Screening:**

- [ ] Are there terms that create significant imbalance between the parties? → Flag for
      §36 analysis
- [ ] Is the franchisee in a substantially weaker bargaining position? → Increases §36
      vulnerability
- [ ] Are there unilateral modification powers for the franchisor? → YELLOW (§36 risk)
- [ ] Are termination consequences disproportionate? → YELLOW (§36 risk)
- [ ] Are fees excessive relative to services provided? → YELLOW (§36 risk)

### Section 38 — Non-Compete Clauses

All five Nordic Contracts Acts contain Section 38, governing non-compete clauses **outside**
employment relationships — including franchise agreements.

**Common principles across all Nordics:**

- Non-compete clauses are enforceable if they do not **unreasonably restrict** the bound
  party's freedom of action (ability to earn income)
- No statutory maximum duration for commercial non-competes (unlike employment)
- No statutory compensation requirement for commercial non-competes (unlike employment)
- Courts apply a **reasonableness test** considering: geographic scope, duration, activity
  scope, and the bound party's ability to earn a livelihood

**Critical distinction from employment non-competes:**

| Feature               | Commercial/Franchise (§38)                | Employment                                                                |
| --------------------- | ----------------------------------------- | ------------------------------------------------------------------------- |
| **Compensation**      | **Not required**                          | Required in all Nordics                                                   |
| **Maximum duration**  | No statutory max (VBER: 1 year post-term) | NO: 12 months, SE: 9-18 months, DK: 12 months (6 combined), FI: 12 months |
| **Governing law**     | Contracts Act §38                         | Employment-specific legislation                                           |
| **Judicial scrutiny** | Moderate (commercial context)             | Strict (protective context)                                               |

**Risk**: If a franchise relationship is **reclassified as employment** (due to excessive
franchisor control over day-to-day operations), the employment non-compete regime applies
— requiring compensation and imposing duration limits.

---

## Non-Compete Analysis — Country-by-Country

### Norway

**In-term:** Enforceable under Avtaleloven §38 if reasonable. No statutory maximum during
the agreement term (VBER: 5 years). No compensation required.

**Post-term:** Governed by Avtaleloven §38. Under VBER principles (applied in practice):
1 year maximum, limited to premises, indispensable for know-how protection. No compensation
required for commercial non-competes.

**Employment distinction (WEA Chapter 14A, effective 1 January 2016):**

- Maximum 12 months post-termination
- Written agreement required
- Employer must pay compensation
- If franchisee is reclassified as employee, WEA applies

**Key case:** _HR-2008-01590-A (Rema 1000 v. Skatland)_: Supreme Court addressed termination
rights and scope of franchise agreements. [VERIFY]

### Sweden

**In-term:** Enforceable during the agreement. SFDA requires disclosure of non-compete terms
(Item 6). VBER: maximum 5 years.

**Post-term:** Generally enforceable for **6 months**, occasionally up to **2 years**
depending on business type. If longer period needed, ex-franchisee **must receive
compensation** to avoid §38 unreasonableness finding. VBER: 1 year max, premises, know-how.

**Employment distinction:**

- Maximum 9-18 months
- Compensation: approximately 60% of salary
- 2025 Labour Court rulings found non-competes unenforceable without compensation provisions

**Lease interaction:** Swedish Rental Act (Hyreslagen, Chapter 12 Jordabalken) provides
tenant protections that **cannot be contracted away**. A franchisor who terminates a
franchise agreement and takes over the leased premises may owe the franchisee **tenant
compensation** under rental law — even if no franchise law compensation is owed.

### Denmark

**In-term:** Enforceable if necessary to maintain common identity and reputation of the
franchise network. VBER: maximum 5 years.

**Post-term:** Permitted for a reasonable period. VBER parameters apply (1 year, premises,
know-how). Danish case law suggests approximately **6 months** as a reasonable notice/
transition period.

**Employment distinction (Act on Restrictive Employment Clauses, 1 January 2016):**

- Maximum 12 months for standalone non-compete
- Maximum 6 months for combined non-compete + non-solicitation
- Compensation: 60% of remuneration
- **Non-solicitation clauses are illegal and invalid** under the Act — this does not apply
  to commercial franchise non-solicitation, but the distinction must be clear

**Key case:** _Danish Supreme Court, 25 April 2000_: Terminated dealer awarded DKK 200,000
compensation under "very special circumstances" — short agreement duration had not duly
compensated for efforts. Potentially extends to franchise relationships. [VERIFY]

### Finland

**In-term:** Enforceable under Oikeustoimilaki §38 if duration is not indefinite. VBER:
maximum 5 years.

**Post-term:** Generally enforceable if 1 year or less, limited to premises, indispensable
for know-how (VBER parameters). §38 reasonableness test applies.

**2022 employment non-compete reform (effective 1 January 2022):**

- All employment non-competes now require mandatory compensation:
  - 40% of salary for periods up to 6 months
  - 60% of salary for periods over 6 months
- Employers may terminate with notice of 1/3 of restriction period (minimum 2 months)
- Does **not** apply to commercial franchise agreements — but if franchisee is reclassified
  as employee, these rules apply
- The reform has made Finnish employers more cautious about non-competes, indirectly
  influencing franchise drafting practices

**Key case:** _KKO:1996:27_: Supreme Court upheld arbitration clause in franchise agreement
as acceptable and binding despite unequal footing. [VERIFY]

### Iceland

**In-term:** Enforceable under Lög 7/1936 §38 if reasonable. VBER parameters via EEA.

**Post-term:** Subject to §38 reasonableness test. VBER: 1 year, premises, know-how.

**Small-market factor (~380,000 population):** Non-compete clauses have outsized impact in
Iceland's concentrated market. Restricting someone from a geographic area may effectively
exclude them from the profession entirely. Courts should (and likely will) consider this
when assessing §38 reasonableness. See also `legalcode-non-compete-analysis-is` for deep
Iceland-specific non-compete analysis.

**Competition authority activity:** The Icelandic Competition Authority (Samkeppniseftirlitið)
has actively scrutinised non-compete arrangements — including requiring abolition of
non-compete clauses for all pharmacists in one settlement. [VERIFY]

### Non-Compete Review Decision Tree

```
Is there a post-term non-compete?
├── YES
│   ├── Duration ≤ 1 year? (VBER Art. 5(3))
│   │   ├── YES → PASS duration gate
│   │   └── NO → RED — outside VBER block exemption
│   ├── Limited to premises (locaux/lokaler) only?
│   │   ├── YES → PASS geography gate
│   │   └── NO → RED — VBER requires premises-only
│   ├── Indispensable to protect know-how?
│   │   ├── YES (genuine, specific know-how) → PASS know-how gate
│   │   └── NO (generic industry knowledge) → RED
│   ├── Limited to competing goods/services?
│   │   ├── YES → PASS activity gate
│   │   └── NO → YELLOW to RED
│   └── Country-specific overlay:
│       ├── Sweden: >6 months without compensation → YELLOW (§38 risk)
│       ├── Iceland: assess small-market impact → may be RED even if <1 year
│       └── All: if franchisee reclassified as employee → employment regime applies
└── NO → No post-term non-compete issue

Is there an in-term non-compete?
├── YES
│   ├── Duration ≤ 5 years? (VBER Art. 5(1)(a))
│   │   ├── YES → PASS
│   │   └── NO → RED — outside VBER block exemption
│   └── Reasonable scope? → Assess under §38
└── NO → No in-term non-compete issue
```

---

## Competition Law — EU/EEA VBER 2022/720

### Application Across the Nordics

| Country | Status     | VBER Application                                                           |
| ------- | ---------- | -------------------------------------------------------------------------- |
| Sweden  | EU member  | Directly applicable                                                        |
| Denmark | EU member  | Directly applicable                                                        |
| Finland | EU member  | Directly applicable                                                        |
| Norway  | EEA (EFTA) | Indirectly applied; NCA interprets Competition Act §10(3) in light of VBER |
| Iceland | EEA (EFTA) | Indirectly applied; ICA mirrors EU competition rules                       |

### Hardcore Restrictions (Franchise-Relevant)

| Restriction                                     | Status                    | Notes                                                               |
| ----------------------------------------------- | ------------------------- | ------------------------------------------------------------------- |
| **RPM** (fixed/minimum resale prices)           | **Hardcore**              | Recommended/maximum prices OK                                       |
| **Passive sales restrictions**                  | **Hardcore**              | Cannot prevent fulfilling unsolicited orders from outside territory |
| **Online sales ban**                            | **Hardcore**              | Cannot prevent effective use of internet                            |
| **Marketplace bans**                            | **Not hardcore**          | May restrict third-party platforms                                  |
| **Active sales restrictions** outside territory | **Generally permissible** | Standard franchise territory protection                             |
| **In-term non-compete > 5 years**               | **Not block-exempt**      | Art. 5(1)(a)                                                        |
| **Post-term non-compete > 1 year**              | **Not block-exempt**      | Art. 5(1)(b) / Art. 5(3)                                            |
| **Post-term non-compete beyond premises**       | **Not block-exempt**      | Art. 5(3)                                                           |

**REVIEW CHECKLIST — Competition Law:**

- [ ] RPM: Does agreement impose minimum/fixed resale prices? → **RED**
- [ ] Passive sales: Are unsolicited orders from outside territory restricted? → **RED**
- [ ] Online sales: Is internet selling prohibited or materially restricted? → **RED**
- [ ] Territory: Are active sales restrictions proportionate? → Assess scope
- [ ] Market share: Are both parties below 30%? → If above, VBER safe harbour unavailable
- [ ] Post-term non-compete: Complies with VBER Art. 5(3) parameters? → See decision tree

---

## Termination and Non-Renewal

### General Principles Across the Nordics

None of the Nordic countries have franchise-specific termination legislation. General
contract law and good faith principles govern:

**Notice requirements:**

- No statutory minimum notice period for franchise agreements in any Nordic country
- Courts apply good faith and reasonableness principles to determine adequate notice
- Analogy from commercial agency law: notice periods up to **6 months** for long-standing
  relationships
- Best practice: include clear notice periods in the franchise agreement

**Country-specific guidance:**

| Country | Termination Notice Guidance                                              | Compensation on Termination                                                                                            |
| ------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| Norway  | Reasonable notice required; good faith applies during and after          | No statutory franchise goodwill compensation. Commercial agent analogy: up to 6 months notice                          |
| Sweden  | No mandatory minimum; contractual terms govern                           | No mandatory compensation. But **tenant compensation** may apply if franchisor takes over leased premises (Hyreslagen) |
| Denmark | ~6 months considered reasonable in case law                              | Generally no compensation. Possible in "very special circumstances" (_Supreme Court, 2000_ — DKK 200,000)              |
| Finland | Reasonable period by analogy from commercial agents law (up to 6 months) | No statutory compensation. Insolvency protections exist (moratorium during restructuring)                              |
| Iceland | Reasonable notice under good faith principles                            | No statutory compensation. Small-market context may amplify impact                                                     |

**REVIEW CHECKLIST — Termination:**

- [ ] Does the agreement provide clear termination notice periods? → If silent → YELLOW
- [ ] Are notice periods proportionate to the relationship duration? → Short notice for
      long relationship → YELLOW to RED
- [ ] Can the franchisor terminate without cause? → Analyse good faith constraints
- [ ] Are termination grounds clearly defined? → Vague grounds → YELLOW
- [ ] Is there a cure period for curable breaches? → No cure period → YELLOW
- [ ] Are termination rights reciprocal? → Non-reciprocal → YELLOW (§36 risk)
- [ ] Does the agreement address post-termination consequences (de-identification,
      repurchase, data return)? → If silent → YELLOW
- [ ] **Sweden-specific**: Does termination interact with a connected lease? → If yes,
      assess Hyreslagen tenant compensation exposure

---

## Arbitration in Nordic Franchise Agreements

### Prevalence and Practice

Over **90%** of Swedish franchise agreements contain arbitration clauses. Prevalence is
similarly high across the Nordics. The most common arbitration institution is the
**Stockholm Chamber of Commerce (SCC)**.

**Key features:**

- Nordic arbitration has deep historical roots and is the preferred dispute resolution
  method for commercial agreements
- Arbitral awards have very limited grounds for challenge
- The result is **very limited publicly available franchise case law**

**Enforceability:**

- _KKO:1996:27 (Finland)_: Supreme Court upheld arbitration clause in franchise agreement
  despite unequal footing [VERIFY]
- _NJA 1992 s. 290 (Sweden)_: Supreme Court held arbitration clause not unreasonable in
  franchise agreement [VERIFY]

**Considerations for franchisees:**

- Arbitration costs can be substantial — especially SCC arbitration
- Cost may create a barrier to justice for smaller franchisees
- Courts may apply §36 to modify or set aside arbitration clauses that create
  disproportionate cost barriers

**REVIEW CHECKLIST:**

- [ ] Does the agreement contain an arbitration clause? → Note: standard practice in Nordics
- [ ] Which institution? (SCC, ICC, ad hoc) → Note for cost analysis
- [ ] Are costs shared or allocated to one party? → Disproportionate cost → YELLOW
- [ ] Is the seat/venue accessible to both parties? → Remote venue → YELLOW
- [ ] For small claims: is there a simplified/expedited procedure? → If not → YELLOW (cost
      barrier)
- [ ] **Iceland-specific**: Is arbitration in Iceland or abroad? → Foreign seat may be
      disproportionate for small market participant

---

## National Franchise Associations and EFF Code of Ethics

### Association Membership

| Country | Association                          | EFF Member? | Code of Ethics                      |
| ------- | ------------------------------------ | ----------- | ----------------------------------- |
| Norway  | Norges Franchiseforening (NFF)       | Yes         | EFF Code + independent ethics board |
| Sweden  | Svenska Franchiseforeningen (SFF)    | Yes         | EFF Code                            |
| Denmark | Franchise Danmark                    | Yes         | EFF Code                            |
| Finland | Suomen Franchising-Yhdistys ry (FFA) | Yes         | EFF Code (updated 2017)             |
| Iceland | None                                 | No          | N/A                                 |

### EFF European Code of Ethics for Franchising

The Code is binding on all EFF national association members. Key provisions:

- Franchisor must have operated successfully in at least one pilot unit before franchising
- Full and accurate written disclosure within reasonable time before signing
- Fairness shall characterise all dealings
- Franchisors must recruit only franchisees with basic skills, education, and adequate capital
- Written notice of breach required; reasonable time to remedy

**Note:** Iceland has **no franchise association** affiliated with the EFF — there is no
self-regulatory framework applicable to Icelandic franchise operations.

**REVIEW CHECKLIST:**

- [ ] Is the franchisor a member of the national franchise association? → If yes, EFF Code
      is binding
- [ ] If a member, was EFF-standard disclosure provided? → If not → potential Code breach
- [ ] Were fair dealing principles observed? → Assess against Code requirements
- [ ] **Iceland**: No association — use EFF Code as best practice benchmark only

---

## Lease/Franchise Agreement Interaction (Sweden-Specific)

### The Swedish Tenant Compensation Issue

In Sweden, franchise and lease agreements are typically **bundled and signed simultaneously**.
The Swedish Rental Act (Hyreslagen, Chapter 12 Jordabalken) provides tenant protections that
**cannot be contracted away**.

**Key risk:** If the franchisor terminates the franchise agreement and takes over the leased
premises to operate the business itself, the franchisee (as tenant) may be entitled to
**tenant compensation** under rental law — even though no franchise-specific compensation
exists.

**Best practice:**

- Franchisor should require franchisee to sign a **separate waiver of tenant compensation
  rights**, approved by the court **before** the franchisee moves in
- Without this waiver, the franchisor faces significant financial exposure on termination

**REVIEW CHECKLIST (Sweden only):**

- [ ] Is the franchise agreement connected to a lease? → If yes, this section applies
- [ ] Has the franchisee signed a court-approved waiver of tenant compensation? → If not →
      **RED** (significant exposure for franchisor)
- [ ] Does the agreement address the lease/franchise interdependence? → If silent → YELLOW
- [ ] What happens to the lease on franchise termination? → Must be clearly specified

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

### Step 1: Identify the Nordic Jurisdiction

**⟁ CLARIFY** — Which Nordic country/countries?

1. **Norway**: No franchise law; Avtaleloven; EEA competition law
2. **Sweden**: SFDA disclosure law; Avtalslagen; EU competition law; lease interaction
3. **Denmark**: No franchise law; Aftaleloven; EU competition law
4. **Finland**: No franchise law; Oikeustoimilaki; EU competition law
5. **Iceland**: No franchise law; Lög 7/1936; EEA competition law; small market
6. **Multi-Nordic**: Identify primary and secondary jurisdictions

### Step 2: Gather Context

**⟁ CLARIFY** — Standard franchise review context plus Nordic-specific:

1. **Which side?** Prospective Franchisee / Existing Franchisee / Franchisor
2. **Is the franchisor a national franchise association member?** → EFF Code applicability
3. **Is this a master franchise for multiple Nordic countries?** → Multi-jurisdiction analysis
4. **Industry sector?** Food & beverage, retail, services, fitness, cleaning, education, other
5. **Deal stage?** Pre-signing / Post-signing / Renewal / Transfer / Dispute / Termination
6. **Sweden-specific**: Is the franchise connected to a lease?
7. **Iceland-specific**: Assess small-market dynamics

### Step 3: Disclosure Review (Sweden Only)

If the franchise operates in Sweden, review SFDA compliance per checklist above.

For other Nordic countries, assess disclosure against EFF Code best practice (if franchisor
is an association member) or general good faith obligations.

### Step 4: Clause-by-Clause Analysis (Nordic-Calibrated)

Apply the 16-category framework from the general franchise review skill with Nordic
calibration. Categories with material Nordic variation:

#### Category 2: Ongoing Royalties — Nordic Calibration

- Typical Nordic royalty: 5-10% of gross sales
- Advertising/marketing fund: typically 2-5% of gross sales
- Unilateral fee changes: §36 risk across all Nordics
- In Sweden, SFDA requires disclosure of compensation structure (Item 3)

#### Category 3: Territory — Nordic Calibration

- VBER applies across all Nordics (directly in SE/DK/FI, indirectly in NO/IS)
- Active sales restrictions: generally permissible
- Passive sales restrictions: hardcore (prohibited)
- Online sales: cannot ban; marketplace restrictions may be permissible
- **Iceland**: territory restrictions in a 380,000-person market have amplified impact

#### Category 9: Term and Renewal — Nordic Calibration

- Typical Nordic term: 5-20 years
- No statutory renewal protections in any Nordic country
- Non-renewal: good faith and reasonable notice required
- **Sweden**: lease/franchise interaction on non-renewal
- **Denmark**: ~6 months notice considered reasonable

#### Category 10: Transfer — Nordic Calibration

- Freedom of contract governs transfer provisions across all Nordics
- Consent requirements are standard and enforceable
- No statutory protections against unreasonable refusal (unlike Australia or California)

#### Category 11: Termination — Nordic Calibration

- No statutory good cause requirement in any Nordic country
- Good faith and reasonableness constrain arbitrary termination
- Non-reciprocal termination: §36 risk
- Commercial agent analogy: up to 6 months notice for long relationships

#### Category 12: Post-Term Non-Compete — Nordic Calibration

**Apply the non-compete analysis framework in full** (see section above).

#### Category 15: Dispute Resolution — Nordic Calibration

- Arbitration is the dominant dispute resolution mechanism (90%+ in Sweden)
- SCC Arbitration Rules most common
- §36 may apply to disproportionately costly arbitration clauses
- Courts are a fallback but franchise litigation is rare in the Nordics

### Step 5: §36 Screening

Run all potentially unreasonable terms through the Contracts Act §36 analysis. Flag terms
that create significant imbalance, especially:

- Unilateral modification powers
- Non-reciprocal termination rights
- Disproportionate fee structures
- Excessive non-compete scope
- Costly arbitration barriers

### Step 6: Competition Law Check

Run VBER hardcore restriction screening (RPM, passive sales, online sales, non-compete
duration/scope).

### Step 7: Quality Verification

Before delivering analysis:

1. **Correct jurisdiction**: Every claim specifies which Nordic country's law applies
2. **SFDA compliance** (Sweden): All 9 disclosure items checked
3. **§38 analysis**: Every non-compete assessed under the correct country's §38
4. **VBER compliance**: Hardcore restrictions screened
5. **Lease interaction** (Sweden): Tenant compensation risk assessed if applicable
6. **§36 screening**: Potentially unreasonable terms flagged

---

## Anti-Patterns — Nordic-Specific

1. **Treating all Nordics as identical**: Despite shared heritage, material differences
   exist. Only Sweden has a franchise law. Employment non-compete rules differ. Lease law
   varies. Iceland's small market creates unique dynamics.

2. **Applying US franchise law concepts**: No registration (except Sweden's limited
   disclosure). No mandatory waiting periods (except Sweden's ~14 days). No statutory
   relationship protections. No FDD equivalent.

3. **Ignoring the §38/employment distinction**: Commercial franchise non-competes (§38) do
   not require compensation. Employment non-competes do. Conflating the two is a
   fundamental error — but if the franchise relationship is reclassified as employment,
   the employment regime applies.

4. **Overlooking Swedish lease/franchise interaction**: In Sweden, terminating a franchise
   connected to a lease can trigger tenant compensation under Hyreslagen. This is a
   unique Swedish risk not present in other Nordics.

5. **Underestimating arbitration prevalence**: Most Nordic franchise disputes are resolved
   in arbitration, not courts. This means very limited public case law. Practitioners must
   rely on statutory analysis and limited reported decisions.

6. **Applying VBER post-term non-compete to entire territory**: VBER Art. 5(3) limits
   post-term non-competes to **premises** (the physical location), not the franchise
   territory. This is strictly interpreted.

7. **Ignoring Iceland's small-market dynamics**: A non-compete that would be reasonable in
   a 10-million-person market (Sweden) may be unreasonable in a 380,000-person market
   (Iceland) where it effectively bars someone from their profession.

8. **Treating EFF Code as binding on non-members**: The EFF Code binds only franchise
   association members. Most franchisors in each country are not members. Use the Code as
   best practice, not a compliance standard.

9. **Assuming no franchise case law means no law**: The Nordics have extensive contract law,
   competition law, and general commercial law that applies to franchise agreements. The
   lack of franchise-specific case law reflects arbitration prevalence, not legal vacuum.

10. **Missing the Finnish 2022 reform impact**: While the Finnish employment non-compete
    reform does not directly apply to commercial franchises, it has influenced market
    expectations and drafting practices across Finnish B2B relationships.

---

## Quality Assurance Framework

### Citation Quality Gates

| Gate             | Rule                                                               | Fail Action                    |
| ---------------- | ------------------------------------------------------------------ | ------------------------------ |
| **Source**       | Every claim cites specific national law, VBER article, or case     | Add citation or "[UNVERIFIED]" |
| **Format**       | National statutes: "Avtaleloven §38" / EU: "VBER Art. 5(3)"        | Fix format                     |
| **Jurisdiction** | Every claim identifies which Nordic country's law applies          | Flag "[JURISDICTION UNCLEAR]"  |
| **Currency**     | Check: post-VBER 2022? Post-Finnish 2022 reform? Post-Danish 2016? | Flag "[CHECK CURRENCY]"        |
| **Confidence**   | Uncertainty stated, especially for cross-border and evolving areas | Add qualifier                  |

### Confidence Scoring

- **Definite (0.95-1.0)**: Clear statute directly on point (SFDA Section 3; VBER Art. 5(3))
- **High (0.80-0.94)**: Strong authority (Nordic Supreme Court decisions; established §36/§38
  principles)
- **Probable (0.60-0.79)**: Good authority with some uncertainty (Danish termination
  compensation — "very special circumstances" test)
- **Possible (0.40-0.59)**: Genuinely open question (§36 application to modern franchise
  imbalances — evolving)
- **Unlikely (0.0-0.39)**: Speculative; flag "[UNCERTAIN]"

---

## Glass Box Audit Trail

```yaml
glass_box:
  agreement: "[Franchise Agreement title and date]"
  franchisor: "[Franchisor name]"
  agreement_type: "[Standard / Multi-unit / Master Franchise / Multi-Nordic]"
  user_side: "[Prospective Franchisee / Existing Franchisee / Franchisor]"
  operating_jurisdiction: "[Norway / Sweden / Denmark / Finland / Iceland / Multi-Nordic]"
  governing_law: "[Specify country]"
  eu_eea_status: "[EU (SE/DK/FI) / EEA-EFTA (NO/IS)]"
  applicable_frameworks:
    - "[Country] Contracts Act — §36 (unreasonable terms), §38 (non-compete)"
    - "EU/EEA VBER 2022/720"
    - "[SFDA (Lag 2006:484) — Sweden only]"
    - "[EFF Code of Ethics — if member]"
    - "[Hyreslagen Ch. 12 — Sweden lease interaction]"
  franchise_association:
    member: "Yes / No"
    association: "[NFF / SFF / Franchise Danmark / FFA / None]"
  sfda_compliance:
    applicable: "[Yes — Sweden / No — other country]"
    disclosure_provided: "Yes / No / N/A"
    timing: "[days before signing]"
    items_complete: "[9/9 or specify missing]"
  contracts_act_36:
    terms_screened: "[number]"
    potentially_unreasonable: "[number] — [list]"
  non_compete:
    post_term_present: "Yes / No"
    duration: "[months]"
    geographic_scope: "[premises / broader — specify]"
    vber_compliant: "Yes / No — [details]"
    section_38_assessment: "Reasonable / Unreasonable / Mixed"
    employment_reclassification_risk: "Low / Medium / High"
  competition_law:
    vber_applicable: "Yes / No (market share >30%)"
    hardcore_restrictions: "[None / RPM / Passive sales / Online — list]"
  termination:
    notice_period: "[months / none specified]"
    good_faith_assessment: "Adequate / Inadequate / Not assessed"
    reciprocal: "Yes / No"
    sweden_lease_interaction: "[Applicable / Not applicable]"
  arbitration:
    present: "Yes / No"
    institution: "[SCC / ICC / ad hoc / other]"
    cost_proportionality: "Proportionate / Disproportionate / Not assessed"
  small_market_analysis: "[Applicable — Iceland / Not applicable]"
  clauses_reviewed: 16
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  legalcode_mcp: "Connected / Not connected"
  statutes_consulted:
    - "[Country] Contracts Act — [VERIFIED / UNVERIFIED]"
    - "VBER 2022/720 — [VERIFIED / UNVERIFIED]"
    - "[SFDA 2006:484 — VERIFIED / UNVERIFIED — Sweden only]"
  case_law_consulted:
    - "[Case — VERIFIED / UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Scope limitations, assumptions, caveats]"
  reviewer: "AI-assisted — requires qualified Nordic franchise counsel review"
```

---

## Provenance

Created by Legalcode (2026-03-19). Jurisdiction-specific variant of
`legalcode-franchise-agreement-review` covering Norway, Sweden, Denmark, Finland, and
Iceland. Research covering:

- Swedish Franchise Disclosure Act (Lag 2006:484)
- Nordic Contracts Acts (§36 unreasonable terms, §38 non-compete)
- EU/EEA VBER 2022/720
- Norwegian Working Environment Act Chapter 14A
- Danish Act on Restrictive Employment Clauses (2016)
- Finnish 2022 employment non-compete reform
- Icelandic Competition Act (Samkeppnislög 44/2005) and small-market dynamics
- EFF European Code of Ethics for Franchising
- Swedish Rental Act (Hyreslagen) lease/franchise interaction
- Nordic franchise case law (HR-2008-01590-A, NJA 1992 s. 290, KKO:1996:27)
- Nordic competition authority developments (2023-2026)

Research sources:

- [ICLG Franchise Laws Sweden 2025](https://iclg.com/practice-areas/franchise-laws-and-regulations/sweden)
- [ICLG Franchise Laws Finland 2026](https://iclg.com/practice-areas/franchise-laws-and-regulations/finland)
- [Chambers Franchising 2025 Denmark](https://practiceguides.chambers.com/practice-guides/franchising-2025/denmark)
- [Legal 500 Denmark Franchise & Licensing](https://www.legal500.com/guides/chapter/denmark-franchise-licensing/)
- [Swedish Franchise Disclosure Act (Lag 2006:484)](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2006484-om-franchisegivares_sfs-2006-484/)
- [Norges Franchiseforening](https://norgesfranchiseforening.no/)
- [Finnish Franchise Association](https://franchising.fi/)
- [Franchise Danmark](https://denmark.franchise-association.org/)
- [VBER 2022/720](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32022R0720)
- [Icelandic Competition Authority](https://en.samkeppni.is/)
