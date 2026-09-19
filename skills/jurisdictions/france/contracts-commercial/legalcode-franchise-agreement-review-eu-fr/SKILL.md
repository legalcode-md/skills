---
name: legalcode-franchise-agreement-review-eu-fr
description: 'Review franchise agreements for French operations against the Loi Doubin (Art. L330-3 Code
  de commerce) and Decree 91-337 (Art. R330-1) — verify Document d''Information Précontractuelle (DIP)
  compliance with mandatory 20-day pre-contractual disclosure period, screen for significant imbalance
  (déséquilibre significatif) under Art. L442-1 I(2) Code de commerce, evaluate post-term non-compete
  enforceability under Art. L341-2 (Macron Law 2015: maximum 1 year, limited to premises, indispensable
  for know-how protection), analyse abrupt termination (rupture brutale) exposure under Art. L442-1 II
  (18-month safe harbour), assess good faith compliance under Art. 1104 Code civil (mandatory, d''ordre
  public), review competition law compliance under EU VBER 2022/720 (RPM, online sales, territory), evaluate
  intuitu personae transfer restrictions and pre-emption rights (droit de préemption), and review defect
  of consent (vice du consentement) exposure for DIP failures.'
metadata:
  jurisdiction: France
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review franchise agreements for French operations against the Loi Doubin (Art. L330-3 Code de commerce) and Decree 91-337 (Art. R330-1) — verify Document d'Information Précontractuelle (DIP) compliance with mandatory 20-day pre-contractual disclosure period, screen for significant imbalance (déséquilibre significatif) under Art. L442-1 I(2) Code de commerce, evaluate post-term non-compete enforceability under Art. L341-2 (Macron Law 2015: maximum 1 year, limited to premises, indispensable for know-how protection), analyse abrupt termination (rupture brutale) exposure under Art. L442-1 II (18-month safe harbour), assess good faith compliance under Art. 1104 Code civil (mandatory, d'ordre public), review competition law compliance under EU VBER 2022/720 (RPM, online sales, territory), evaluate intuitu personae transfer restrictions and pre-emption rights (droit de préemption), and review defect of consent (vice du consentement) exposure for DIP failures. GREEN/YELLOW/RED classification with confidence scoring and Glass Box audit trail. Use when reviewing franchise agreements governed by French law or where the franchise will operate in France. Jurisdiction-specific variant of legalcode-franchise-agreement-review.


# Legalcode Franchise Agreement Review — France (Contrat de Franchise)

> **Avertissement / Disclaimer**: This skill provides a framework for AI-assisted franchise
> agreement review under French law. It does not constitute legal advice (conseil juridique).
> All outputs require review by a qualified French avocat experienced in franchise and
> distribution law before reliance. French franchise law combines the Loi Doubin pre-
> contractual disclosure regime with general contract law (Code civil), commercial practices
> law (Code de commerce), and EU/national competition law. The legal framework is shaped
> significantly by Cour de cassation jurisprudence. Verify current case law before acting.
> Statutory and case law references cited from memory carry hallucination risk — verify
> against authoritative sources (Légifrance, Cour de cassation, Autorité de la concurrence)
> before relying on them.

---

## Purpose and Scope

This skill reviews franchise agreements (contrats de franchise) for French compliance.
France is the largest franchise market in continental Europe (~2,035 networks, ~92,132
outlets, EUR 88.49 billion turnover as of 2024) and has a distinctive legal regime: mandatory
pre-contractual disclosure via the DIP, strong protection against significant imbalance
(déséquilibre significatif), strict post-term non-compete limitations under the Macron Law,
and a unique doctrine of abrupt termination (rupture brutale) that constrains how franchise
relationships end.

**Covers:**

- Loi Doubin / DIP compliance — Art. L330-3 and Art. R330-1 Code de commerce
- 20-day pre-contractual disclosure period verification
- Defect of consent (vice du consentement) analysis for DIP failures
- Significant imbalance screening — Art. L442-1 I(2) Code de commerce
- Good faith analysis — Art. 1104 Code civil (mandatory, d'ordre public)
- Post-term non-compete analysis — Art. L341-2 Code de commerce (Macron Law 2015)
- Abrupt termination (rupture brutale) exposure — Art. L442-1 II
- EU VBER 2022/720 competition law compliance
- Intuitu personae / transfer restrictions and pre-emption rights
- Penalty clause analysis under Art. 1231-5 Code civil
- GREEN / YELLOW / RED deviation classification with confidence scoring
- Bilingual terminology (French legal terms + English explanation)
- Glass Box audit trail

**Does not:**

- Draft new franchise agreements from scratch
- Provide legal advice or replace qualified French franchise counsel (avocat)
- Cover non-French franchise law (see `legalcode-franchise-agreement-review` for general;
  jurisdiction-specific variants for US-CA, AU, UK, Nordics)
- Cover commercial agency law (agents commerciaux — separate regime under Art. L134-1 et seq.)
- Provide employment law advice beyond franchise-specific provisions

**Related skills:**

- `legalcode-franchise-agreement-review` — General multi-jurisdictional franchise review
- `legalcode-franchise-agreement-review-uk` — UK common law focus
- `legalcode-franchise-agreement-review-au` — Australia Franchising Code focus
- `legalcode-contract-review` — General commercial contract review

---

## Jurisdiction and Governing Law

### Why France Requires a Dedicated Skill

French franchise law differs materially from other jurisdictions:

1. **Loi Doubin**: Mandatory 20-day pre-contractual disclosure via DIP — unique content
   requirements and a consequence framework based on defect of consent, not automatic
   nullity
2. **Significant imbalance**: Art. L442-1 I(2) gives the Minister of Economy independent
   standing to challenge clauses — even after parties have settled (_Domino's Pizza_, Cass.
   com., Feb. 28, 2024)
3. **Macron Law non-compete limits**: Art. L341-2 imposes strict conditions (1 year max,
   premises only, indispensable for know-how) — stricter than most EU countries
4. **Rupture brutale**: The doctrine of abrupt termination of established commercial
   relationships creates a unique notice obligation framework for franchise non-renewal
5. **Good faith is mandatory**: Art. 1104 Code civil (since 2016 reform) makes good faith
   obligatory at all contract phases — it is d'ordre public and cannot be waived
6. **No franchise-specific comprehensive statute**: Despite Loi Doubin, France does not have
   a comprehensive franchise act — the regime is assembled from multiple Code provisions
   and jurisprudence

### Scope of Loi Doubin — Broader Than Franchise

Art. L330-3 applies to **all forms of organised commerce** (commerce associé), not only
franchise agreements. It covers any contractual relationship where:

1. A trade name, brand, or sign (enseigne) is made available; **AND**
2. An exclusivity or quasi-exclusivity commitment is required

This includes: franchise (franchise), concession (concession), commission-affiliation,
trademark licence (licence de marque), cooperative commerce, and any exclusive or
quasi-exclusive distribution arrangement.

### Governing Law Considerations

- Parties are free to choose governing law for the franchise agreement (liberté contractuelle,
  Art. 1102 Code civil)
- However, **mandatory French provisions** (dispositions d'ordre public) apply regardless of
  choice of law when the franchise operates in France:
  - Art. L330-3 (DIP obligation) — applies when the franchise is offered in France
  - Art. L442-1 (significant imbalance, rupture brutale) — applies to relationships affecting
    the French market
  - Art. L341-2 (non-compete limits) — applies to post-term restrictions on French territory
  - Art. 1104 (good faith) — mandatory in all contracts under French law
- Master franchise agreements between foreign franchisors and French master franchisees may
  be governed by non-French law, but sub-franchise agreements within France must comply with
  mandatory French provisions

---

## Loi Doubin — Pre-Contractual Disclosure (DIP)

### Art. L330-3 Code de Commerce — Core Obligation

The franchisor must provide the franchisee with a Document d'Information Précontractuelle
(DIP) and the draft franchise agreement at least **20 calendar days** before:

- The contract signature, **OR**
- The payment of any sum of money, **OR**
- Any investment commitment related to the franchise

Any change in the information between provision of the DIP and contract execution must be
communicated in writing before execution.

### DIP Required Contents (Art. R330-1)

| Category                        | Required Information                                                                                                    | Review Focus                    |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **A. Franchisor Identity**      | Company name, legal form, registered office, capital, RCS registration, identity of directors, bank domiciliation       | Verify accuracy and currency    |
| **A. Franchisor History**       | Date of creation, main stages of evolution, seniority and experience                                                    | Gaps or concerns?               |
| **A. Financial Information**    | **Audited annual accounts (comptes annuels) for last 2 financial years** — appended                                     | Financial stability? Trends?    |
| **A. Trademark**                | Date and number of trademark registration; registration number of trademark licence agreement                           | Current registration? Disputes? |
| **B. Network**                  | Number of franchised outlets; full list of addresses in France                                                          | Network size and health         |
| **B. Network Relations**        | Nature of relationship with franchisor; contract dates                                                                  | Consistency with agreement      |
| **B. Departures**               | Number and reasons for terminations/non-renewals in preceding year (distinguishing franchisor vs. franchisee initiated) | High attrition → RED flag       |
| **C. Market**                   | General and local state of the relevant market; development prospects                                                   | Realistic? Substantiated?       |
| **D. Contract Terms**           | Duration, renewal/termination/transfer conditions, scope of exclusivities                                               | Consistency with agreement      |
| **D. Financial Terms**          | Nature and amount of expenses and investments before operations begin (droit d'entrée, specific investments)            | Complete? Realistic?            |
| **D. Pre-contractual Payments** | If sum required before signing: services provided in return; reciprocal obligations on withdrawal                       | Fair? Proportionate?            |

### DIP Compliance Review Checklist

- [ ] Was a DIP provided? → If not → **RED** (criminal contravention + civil exposure)
- [ ] Was the DIP provided at least 20 days before signing or payment? → If not → **RED**
- [ ] Was the draft contract provided with the DIP? → If not → **RED** (Art. L330-3 requires
      both simultaneously)
- [ ] Does the DIP contain all Art. R330-1 required elements? → Missing elements → YELLOW
      to RED depending on materiality
- [ ] Are audited annual accounts for the last 2 years appended? → If not → **RED**
- [ ] Does the DIP list all network outlets in France with addresses? → If incomplete → YELLOW
- [ ] Does the DIP disclose departures (terminations/non-renewals) in the preceding year? →
      If omitted → YELLOW to RED
- [ ] Is the market analysis (general + local) substantiated? → Vague or outdated → YELLOW
- [ ] Were any changes communicated between DIP and contract signing? → If changes occurred
      without notification → YELLOW
- [ ] Is DIP information consistent with the franchise agreement? → Discrepancies → RED

### Consequences of DIP Non-Compliance

**Criminal sanctions:**

- Complete absence of DIP: fifth-class contravention (contravention de cinquième classe)
- Fine: up to EUR 1,500 (individuals) / EUR 7,500 (legal entities); doubled for repeat
  offences
- Note: criminal penalty requires **complete absence** of DIP, not mere incompleteness

**Civil sanctions — the vice du consentement framework:**

**Critical principle** (Cour de cassation, established since 1998): DIP failure does **not**
automatically result in contract nullity. The franchisee must prove a **defect of consent**
(vice du consentement):

| Ground                 | Standard                                                                     | Typical Scenario                                                       |
| ---------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Error (erreur)**     | Franchisee would not have contracted with correct/complete information       | Missing or misleading market data; inaccurate financial projections    |
| **Fraud/deceit (dol)** | Intentional misrepresentation or concealment by franchisor to induce consent | Deliberately hiding network failures; fabricated financial projections |

**If defect of consent is proven:**

- **Nullity (nullité)** of the franchise agreement with retroactive effect — restitution of
  sums paid
- **Damages** for losses suffered (costs, investments, lost profits)

**If defect of consent is not proven:**

- Nullity denied, but **damages** may still be awarded for losses caused by inadequate
  disclosure

**Practical implication**: An incomplete DIP is a serious deficiency but not automatic grounds
for contract avoidance. The franchisee bears the burden of proving that the deficiency
actually affected their decision to contract.

---

## Significant Imbalance — Art. L442-1 I(2) Code de Commerce

### The Déséquilibre Significatif Doctrine

Art. L442-1 I(2) prohibits submitting or attempting to submit a partner to obligations
creating a **significant imbalance** (déséquilibre significatif) in the parties' rights and
obligations.

**Assessment methodology:**

- Courts conduct an **overall review** (appréciation globale) of the agreement
- Clauses are assessed in context — not in isolation
- The **benefits of network membership** (brand value, know-how, assistance) are weighed
  against the obligations imposed
- Both individual clauses and cumulative effect are evaluated

**Key features:**

- The **Minister of Economy** (Ministre de l'Économie) has **independent standing** to bring
  actions — even after the parties have settled between themselves
- Fines up to EUR 5 million (or proportion of turnover)
- Courts can declare imbalanced clauses null and void

**Landmark case — _Domino's Pizza_ (Cass. com., Feb. 28, 2024):**

- Upheld EUR 500,000 fine
- Cancelled clauses lacking reciprocity (termination clause, minimum procurement) or being
  too imprecise (non-assignment clause)
- Confirmed the Minister's action is not barred by settlements between parties [VERIFY]

**Other notable cases:**

- _Subway_ (Paris Commercial Court): Cancelled clauses on significant imbalance grounds;
  also analysed arbitration clause creating onerous barriers to justice [VERIFY]
- _Carrefour_ (Tribunal de commerce de Rennes, July 3, 2025): Collective action admitted for
  systematic imbalance claim; Minister of Economy joined as party [VERIFY]

### Significant Imbalance Screening

**Clauses frequently challenged:**

| Clause Type                                         | Imbalance Risk  | Analysis                                                                      |
| --------------------------------------------------- | --------------- | ----------------------------------------------------------------------------- |
| **Unilateral termination** without reciprocal right | **HIGH**        | _Domino's_: non-reciprocal termination clause cancelled                       |
| **Minimum procurement** without justification       | **HIGH**        | _Domino's_: minimum procurement cancelled for lack of reciprocity             |
| **Non-assignment** overly broad                     | **MEDIUM-HIGH** | _Domino's_: imprecise non-assignment cancelled                                |
| **Unilateral price changes**                        | **HIGH**        | Franchisor power to change fees without consent                               |
| **Unilateral modification of obligations**          | **HIGH**        | Via operations manual or supplier requirements                                |
| **One-sided termination triggers**                  | **HIGH**        | Franchisor can terminate for minor breach; franchisee has no equivalent right |
| **Mandatory arbitration abroad**                    | **MEDIUM**      | _Subway_: onerous arbitration clause challenged                               |
| **Excessive non-compete**                           | **MEDIUM**      | May also fall under Art. L341-2                                               |
| **Exclusive supply with above-market pricing**      | **MEDIUM**      | Assess justification and proportionality                                      |

**REVIEW CHECKLIST:**

- [ ] Are termination rights **reciprocal**? → Non-reciprocal → **RED**
- [ ] Are procurement obligations **justified** and proportionate? → Minimum purchase without
      rationale → RED
- [ ] Can the franchisor **unilaterally modify** material obligations? → RED
- [ ] Are fee increase mechanisms **predictable** and **capped**? → Unlimited increases → YELLOW
- [ ] Is arbitration **accessible** (cost, location)? → Foreign/expensive arbitration → YELLOW
- [ ] Are penalties **proportionate** to breach? → Excessive penalties → YELLOW
- [ ] Does the **overall balance** of the agreement favour one party disproportionately? →
      Assess globally

---

## Good Faith — Art. 1104 Code Civil

**"Les contrats doivent être négociés, formés et exécutés de bonne foi."**
(Contracts must be negotiated, formed, and performed in good faith.)

**Key characteristics:**

- **Mandatory** (d'ordre public) since the 2016 Code civil reform
- Applies at **all phases**: negotiation, formation, and performance
- **Cannot be waived** by contract
- Extends the pre-contractual information duty (Art. 1112-1)

**Application to franchise agreements:**

- Franchisor must provide **sincere** and **accurate** information during DIP/negotiation
- Franchisor must perform support obligations **as promised**
- Franchisor must not act to **undermine the purpose** of the franchise agreement
- Good faith does not require the franchisor to sacrifice its own legitimate commercial
  interests, but it prohibits acting dishonestly or in bad faith to the franchisee's detriment

**REVIEW CHECKLIST:**

- [ ] Does the agreement contain a clause excluding good faith? → **RED** (void as contrary
      to d'ordre public)
- [ ] Are franchisor's obligations clearly defined? → Vague support obligations → YELLOW
      (enforcement difficulty)
- [ ] Does the agreement contain obligations that could be exercised in bad faith? → Identify
      and flag

---

## Post-Term Non-Compete — Art. L341-2 Code de Commerce (Macron Law 2015)

### The Four Cumulative Conditions

Any post-term clause restricting the former franchisee's commercial activity is **deemed
non-written** (réputée non écrite) unless it satisfies ALL four conditions:

| Condition                         | Requirement                                                                                                                  | Analysis                                                                                 |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **1. Competing goods/services**   | Restriction concerns goods and services that **compete** with those covered by the franchise                                 | Must be limited to genuinely competing activity; overly broad definitions are vulnerable |
| **2. Limited to premises**        | Restriction is limited to the **land and premises** (locaux et terrains) from which the franchisee operated                  | Cannot cover an entire territory, radius, or region — strictly the physical premises     |
| **3. Indispensable for know-how** | Restriction is **indispensable** to protect the **substantial, specific, and secret** know-how transmitted by the franchisor | Must demonstrate genuine protectable know-how, not just standard industry practice       |
| **4. Maximum one year**           | Duration does not exceed **one year** from end of contract                                                                   | Non-negotiable maximum; any longer is automatically deemed non-written                   |

### Key Case Law

- **Cass. com., June 5, 2024**: Art. L341-2 applies to **service-sector** franchises (real
  estate agencies), not just retail/goods — extending its scope [VERIFY]
- **Cass. com., June 26, 2024 (ERA France / Vision Méditerranée immobilier)**: Post-
  contractual non-reaffiliation clause held **ineffective** (inopposable) — "not indispensable
  to the protection of the franchisor's know-how and excessively impaired the franchisee's
  freedom to conduct his business" [VERIFY]
- **Non-retroactivity**: Art. L341-2 does not apply retroactively to contracts concluded
  before August 6, 2015

### VBER Art. 5(3) — EU Competition Law Overlay

Post-term non-competes are excluded from the VBER block exemption unless:

- Limited to **one year** after termination
- Limited to the **point of sale** from which the buyer operated
- Indispensable to protect know-how transferred by the supplier
- Relates to competing goods or services

The ECJ strictly interpreted "premises and land" — it cannot extend to an entire territory.

### Non-Compete vs. Non-Reaffiliation

French courts distinguish between:

- **Non-compete** (clause de non-concurrence): restricts competing activity
- **Non-reaffiliation** (clause de non-réaffiliation): restricts joining a competing network

Both are subject to Art. L341-2 conditions (_ERA France_, 2024).

### No Compensation Required (Unlike Employment)

| Feature                | Employment Non-Compete                 | Franchise Non-Compete                       |
| ---------------------- | -------------------------------------- | ------------------------------------------- |
| Compensation required  | **Yes** — min. ~30% of gross salary    | **No** — not required                       |
| Legal basis            | Cour de cassation (Soc.) case law      | Art. L341-2 Code de commerce                |
| Maximum duration       | Typically 1-2 years                    | **1 year** (statutory maximum)              |
| Geographic scope       | Must be reasonable                     | **Premises only** (locaux et terrains)      |
| Consequence if invalid | Null and void; compensation still owed | **Deemed non-written** (réputée non écrite) |

**REVIEW CHECKLIST:**

- [ ] Does the agreement contain a post-term non-compete? → Analyse against all 4 conditions
- [ ] Duration > 1 year? → **RED** (automatically deemed non-written)
- [ ] Scope extends beyond premises? → **RED** (must be limited to locaux et terrains)
- [ ] Is the know-how genuinely substantial, specific, and secret? → If generic industry
      knowledge → RED (indispensability not met)
- [ ] Is the restricted activity limited to competing goods/services? → Overly broad → YELLOW
- [ ] Does the agreement contain a non-reaffiliation clause? → Same conditions apply
      (_ERA France_, 2024)
- [ ] Was the contract concluded before August 6, 2015? → Art. L341-2 does not apply
      retroactively; prior proportionality rules govern

---

## Abrupt Termination — Art. L442-1 II Code de Commerce (Rupture Brutale)

### The Rupture Brutale Doctrine

Art. L442-1 II prohibits the **abrupt termination** (rupture brutale), even partial, of an
established commercial relationship (relation commerciale établie) without adequate prior
written notice.

**Applies to:**

- Termination of a franchise agreement
- Non-renewal of a fixed-term franchise agreement
- Significant reduction of the commercial relationship (partial rupture)
- Any established commercial relationship — broader than franchise alone

### Notice Period Requirements

**No fixed statutory minimum**: The required notice is determined case-by-case, considering:

- **Duration** of the commercial relationship
- **Trade practices** and industry norms
- **Economic conditions** of the market

**General guideline**: Approximately **one month per year** of the relationship (not a strict
rule but a frequently applied benchmark).

**Safe harbour / maximum cap**: The notice-giving party cannot be held liable if they gave
at least **18 months' notice** — regardless of the relationship length (Art. L442-1 II,
al. 2).

**Exceptions** (no notice required):

- Non-performance by the other party of its obligations (faute grave)
- Force majeure

### Damages for Rupture Brutale

- Based on **tortious liability** (responsabilité délictuelle)
- Damages cover the **loss caused by the brutal character** of the termination (not the
  termination itself — the party is entitled to terminate, but must give adequate notice)
- Typically calculated as the **margin** the franchisee would have earned during a reasonable
  notice period
- Full compensation principle (réparation intégrale): actual loss, not punitive damages

### Important Distinctions

**No goodwill indemnity for franchisees**: Unlike commercial agents (agents commerciaux)
who receive goodwill compensation (indemnité de clientèle) under Art. L134-12, franchisees
have **no statutory right** to goodwill compensation on termination. This can only be
provided contractually.

**REVIEW CHECKLIST:**

- [ ] Does the agreement provide for termination/non-renewal notice? → If silent on notice
      period → YELLOW (rupture brutale exposure)
- [ ] Is the notice period adequate given the relationship duration? → ~1 month per year as
      guideline; 18 months is the safe harbour cap
- [ ] Does the agreement give the franchisor immediate termination without notice? → Only
      valid for faute grave; otherwise → RED (rupture brutale risk)
- [ ] Does the agreement address compensation on non-renewal? → No statutory right, but
      absence may be relevant to overall balance assessment
- [ ] Does the agreement distinguish between termination for cause and termination without
      cause? → If not → YELLOW

---

## Termination Under French Law

### Fixed-Term Agreements (Durée Déterminée)

- Most common structure in French franchising (5-10 years typical)
- Expires automatically at end of term unless renewed
- If renewed without specific terms, may become indefinite-term (Art. 1215 Code civil)
- Non-renewal subject to rupture brutale notice requirements if relationship is "established"

### Termination for Breach (Résiliation pour Faute)

**Common grounds:**

- Failure to pay royalties (redevances)
- Material breach of the franchise concept
- Disclosure of confidential know-how
- Infringement of intellectual property
- Failure to comply with exclusive sourcing requirements
- Failure to respect quality standards

**Procedure:**

1. **Mise en demeure** (formal notice): contractual requirement in most agreements
2. **Cure period**: must be provided unless agreement specifies otherwise
3. **Judicial termination** (résiliation judiciaire, Art. 1227) or **unilateral termination**
   (résiliation unilatérale, Art. 1226 — for sufficiently serious breach)
4. A contractual termination clause (clause résolutoire) will be enforced if properly
   triggered

### Unilateral Termination (Art. 1226 Code Civil — Since 2016 Reform)

Since the 2016 reform, a party may terminate unilaterally by notice in cases of
**sufficiently serious breach** (inexécution suffisamment grave), at the terminating party's
risk. If challenged, the court may award damages if the termination was unjustified.

**REVIEW CHECKLIST:**

- [ ] Does the agreement contain a clause résolutoire? → Review trigger conditions and
      cure periods
- [ ] Are termination grounds clearly defined? → Vague grounds → YELLOW
- [ ] Is there a meaningful cure period (mise en demeure + time to remedy)? → Immediate
      termination for curable breach → YELLOW to RED
- [ ] Is termination reciprocal? → Franchisor can terminate for minor breach but franchisee
      cannot → RED (significant imbalance risk)
- [ ] Does the agreement address the consequences of wrongful termination?

---

## Transfer and Assignment — Intuitu Personae

### The Personal Nature of Franchise Agreements

French franchise agreements are concluded **intuitu personae** — based on the personal
qualities of the franchisee. This means:

- The franchisee **cannot freely transfer** the agreement or the franchised business (fonds
  de commerce) without the franchisor's consent (agrément)
- The consent requirement applies to: sale of fonds de commerce, transfer of shares/equity,
  merger, demerger, or contribution of assets
- The franchisor's refusal must be **reasonable** — unreasonable refusal may be challenged
  as abusive

### Pre-Emption Rights (Droit de Préemption)

Pre-emption clauses are common in French franchise agreements and are legally analysed as
**preference pacts** (pacte de préférence, Art. 1123 Code civil).

**Requirements for enforceability:**

- Scope must be clearly defined (types of transactions triggering the right)
- Franchisor must have a legitimate interest
- Franchisee must provide **complete information** when contemplating transfer — the pre-
  emption deadline only begins when exhaustive information is received

**Remedies for violation:**

- Sale to third party may be declared **null and void**
- Franchisor may **substitute** the third-party buyer (Art. 1123 Code civil, since 2016)

### Recent Case Law on Intuitu Personae

**_Pizza Center France_ (Cass. com., May 2024):**

- Transfer of **all shares** in the franchisor company does **not** require prior franchisee
  consent (absent specific contractual provision)
- Rationale: share transfer does not change the legal entity party to the agreement
- **However**, a merger of the franchisor entity would constitute a transfer requiring consent
- Also ruled: franchise agreement and business lease are **interdependent contracts** (contrats
  interdépendants) [VERIFY]

**REVIEW CHECKLIST:**

- [ ] Does the agreement contain an agrément (consent) requirement for transfer? → Standard;
      assess reasonableness of conditions
- [ ] Does the agreement contain a pre-emption clause (droit de préemption)? → Assess scope,
      timing, and information requirements
- [ ] Does the agreement apply intuitu personae to both parties (bilateral)? → Best practice;
      unilateral → YELLOW
- [ ] Does the agreement address share transfers vs. asset transfers? → If silent → YELLOW
- [ ] Does the agreement address franchisor changes of control? → If not → YELLOW
      (_Pizza Center France_ — share transfer of franchisor does not require consent absent
      contractual provision)

---

## Competition Law — EU VBER 2022/720

### Direct Application in France

The VBER applies directly as in all EU member states. In force June 1, 2022; expires May 31, 2034. Market share threshold: both parties must each hold ≤30%.

### Hardcore Restrictions (Franchise-Relevant)

| Restriction                                     | Status                    | Consequence                                                                           |
| ----------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------- |
| **RPM** (fixed/minimum resale prices)           | **Hardcore**              | Recommended/maximum prices OK; minimum/fixed prohibited                               |
| **Passive sales restrictions**                  | **Hardcore**              | Cannot prevent franchisee from fulfilling unsolicited orders from outside territory   |
| **Online sales ban**                            | **Hardcore**              | Cannot prevent effective use of internet as sales channel                             |
| **Marketplace bans**                            | **Not hardcore**          | May restrict third-party platform sales (e.g., Amazon); benefits from block exemption |
| **Active sales restrictions** outside territory | **Generally permissible** | Can restrict franchisee from actively soliciting in other franchisees' territories    |
| **Dual pricing** (online vs. offline)           | **Not per se hardcore**   | Permissible if proportionate and justified                                            |

### Autorité de la Concurrence Enforcement

**De Neuville (2024)**: EUR 4,068,000 fine for restricting franchisees' online sales and
allocating professional customers between franchisees (2006-2022). [VERIFY]

This demonstrates active French enforcement of competition law in franchise networks.

### Post-Term Non-Compete Under VBER Art. 5(3)

Post-term non-competes are excluded from block exemption unless:

- Limited to 1 year
- Limited to point of sale (premises)
- Indispensable to protect know-how
- Relates to competing goods/services

This aligns with (and is supplemented by) the stricter French domestic provision, Art. L341-2.

**REVIEW CHECKLIST:**

- [ ] Does the agreement impose minimum/fixed resale prices? → **RED** (RPM — hardcore)
- [ ] Does the agreement restrict passive sales? → **RED** (hardcore)
- [ ] Does the agreement ban online sales entirely? → **RED** (hardcore)
- [ ] Does the agreement restrict marketplace sales? → YELLOW (permissible but assess
      proportionality)
- [ ] Are territory restrictions proportionate? → Analyse active vs. passive sales
- [ ] Does the in-term non-compete exceed 5 years? → **RED** (outside VBER Art. 5(1))

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

### Step 1: Accept Agreement and DIP

**⟁ CLARIFY** — Documentation status:

1. **Franchise agreement + DIP provided**: Full compliance review
2. **Agreement only, no DIP**: Flag as potential Loi Doubin violation; assess defect of
   consent exposure
3. **DIP only**: Review DIP compliance; note that agreement is also required
4. **Master franchise agreement**: Determine if sub-franchise DIP obligations apply

### Step 2: Gather Context

**⟁ CLARIFY** — French franchise context:

1. **Which side are you on?** Prospective Franchisee / Existing Franchisee / Franchisor
2. **When was the DIP provided?** Date → calculate whether 20-day period was observed
3. **When was the agreement signed?** Date → determine applicable law version (pre/post
   Macron Law 2015, pre/post 2016 Code civil reform)
4. **Is this a renewal, new agreement, or transfer?** Affects rupture brutale analysis
5. **Industry sector?** Food & beverage (restauration), retail (commerce de détail),
   services, real estate (immobilier), fitness, cleaning, other
6. **Is the franchisor a FFF member?** → European Code of Ethics applies as best practice
7. **Deal stage?** Pre-signing / Post-signing / Renewal / Transfer / Dispute / Termination
8. **Risk tolerance?** Conservative / Pragmatic / Deal-centric

### Step 3: DIP Compliance Review

Apply the DIP review checklist (above) systematically. Document all findings.

### Step 4: Clause-by-Clause Analysis (French-Calibrated)

Apply the 16-category framework from the general franchise review skill with French-specific
calibration:

#### Category 1: Droit d'Entrée (Initial Franchise Fee) — French Calibration

- Must be disclosed in the DIP (Art. R330-1, Category D)
- No statutory limit on amount
- Typical range: EUR 10,000-50,000 (varies by sector and brand)
- Forfeiture on early termination: assess under Art. 1231-5 (penalty clause proportionality)

#### Category 2: Redevances (Ongoing Royalties) — French Calibration

- Must be disclosed in the DIP
- Typical range: 2-8% of gross revenue; some networks charge fixed amounts
- Advertising fund (redevance publicitaire): typically 1-3% additionally
- Unilateral change mechanism: significant imbalance risk (Art. L442-1 I(2))

#### Category 3: Territoire (Territory) — French Calibration

- No legal obligation to grant exclusive territory
- If exclusivity is granted, franchisor must respect it strictly
- Violation (opening competing outlet in exclusive zone) = breach + damages
- VBER: active sales restrictions permissible; passive sales restrictions prohibited
- Online sales: _De Neuville_ (2024) — cannot restrict franchisees' online sales

#### Category 9: Durée et Renouvellement (Term and Renewal) — French Calibration

- Typical term: 5-10 years
- No maximum statutory term (but in-term exclusivity >5 years may lose VBER exemption)
- Non-renewal: no automatic right; but rupture brutale applies if relationship is "established"
- Renewal without specific terms may create indefinite-term contract (Art. 1215)

#### Category 10: Cession (Transfer) — French Calibration

- Intuitu personae: consent (agrément) required
- Pre-emption rights (droit de préemption): common, enforceable if properly structured
- Share transfer vs. asset transfer: different legal treatment
- Unreasonable refusal of consent may be abusive

#### Category 11: Résiliation (Termination) — French Calibration

- Termination for cause: mise en demeure + cure period standard
- Unilateral termination (Art. 1226): available for sufficiently serious breach since 2016
- Clause résolutoire: enforced if properly triggered
- Reciprocity: non-reciprocal termination rights → significant imbalance risk
- Repurchase: no statutory obligation (unlike some other jurisdictions)

#### Category 12: Non-Concurrence Post-Contractuelle — French Calibration

**Apply the Art. L341-2 four-condition test in full** (see section above).

| Feature               | French Law                             | US (most states)             | UK                                 | Australia                      |
| --------------------- | -------------------------------------- | ---------------------------- | ---------------------------------- | ------------------------------ |
| Max duration          | **1 year** (statutory)                 | Varies (typically 1-2 years) | No statutory max; _Dwyer_ guidance | No statutory max; common law   |
| Geographic scope      | **Premises only** (locaux et terrains) | Varies; usually territory    | Proportionate to territory         | Proportionate; cascading       |
| Compensation required | **No**                                 | Generally no                 | No                                 | No                             |
| Invalid =             | **Deemed non-written**                 | May be blue-pencilled        | May be severable                   | May be severable via cascading |
| Basis                 | Art. L341-2 + VBER Art. 5              | State statute / common law   | Common law restraint of trade      | Common law + Code s 42         |

#### Category 15: Règlement des Litiges (Dispute Resolution) — French Calibration

- Arbitration clauses are enforceable in B2B contracts in France
- But arbitration clause creating onerous barriers (foreign seat, high costs) may be
  challenged as significant imbalance (_Subway_) [VERIFY]
- Governing law choice: valid, but mandatory French provisions apply regardless
- French courts (Tribunal de commerce) have jurisdiction for commercial disputes
- Mediation: increasingly encouraged; not mandatory

#### Category 16: Déclarations et Reconnaissances — French Calibration

- Non-reliance clauses: less common in French practice; Art. 1112-1 pre-contractual
  information duty and Art. 1130-1144 defect of consent provisions override
- Integration / entire agreement clauses: French courts give less weight to these than
  common law jurisdictions; pre-contractual representations may still be actionable
- Good faith (Art. 1104) cannot be excluded

### Step 5: Significant Imbalance Screening

Apply the Art. L442-1 I(2) screening (above) to the overall agreement. Assess global
balance, not just individual clauses.

### Step 6: Rupture Brutale Analysis

If the review concerns termination, non-renewal, or a dispute:

- Determine if the relationship qualifies as "established" (relation commerciale établie)
- Calculate the appropriate notice period (~1 month per year; 18-month cap)
- Assess whether adequate notice was given
- Calculate potential damages exposure

### Step 7: Quality Verification

Before delivering analysis:

1. **French statute verification**: Every French-specific claim cites Art. L/R/Code civil
2. **Art. L341-2 compliance**: Every post-term non-compete assessed against all 4 conditions
3. **Significant imbalance**: Global balance assessment completed
4. **Good faith**: No clause classified as GREEN that would violate Art. 1104
5. **DIP compliance**: All Art. R330-1 elements checked
6. **VBER compliance**: Hardcore restrictions screened

---

## Anti-Patterns — France-Specific

1. **Treating DIP failure as automatic nullity**: French law requires proof of vice du
   consentement. An incomplete DIP alone does not void the contract — the franchisee must
   prove the deficiency affected their decision to contract.

2. **Applying territory-based non-compete analysis**: Art. L341-2 limits post-term
   non-competes to **premises** (locaux et terrains), not territory. A clause covering a
   radius, city, or region is deemed non-written regardless of reasonableness.

3. **Ignoring the Macron Law for pre-2015 contracts**: Art. L341-2 applies only to contracts
   concluded on or after August 6, 2015. Earlier contracts are governed by the prior
   proportionality framework.

4. **Forgetting the Minister's independent standing**: The Minister of Economy can challenge
   significant imbalance even after the parties have settled. The franchisor cannot "fix"
   the problem by settling with the franchisee alone.

5. **Assuming goodwill indemnity**: Unlike commercial agents, franchisees have **no statutory
   right** to goodwill compensation (indemnité de clientèle) on termination. Don't confuse
   franchise law with commercial agency law.

6. **Treating non-reaffiliation differently from non-compete**: Since _ERA France_ (2024),
   both non-compete and non-reaffiliation clauses are subject to Art. L341-2 conditions.

7. **Ignoring the rupture brutale 18-month cap**: Even for very long relationships, 18 months
   of notice is the maximum that can be required. Longer notice obligations are not
   enforceable.

8. **Applying common law non-reliance analysis**: French pre-contractual information duties
   (Art. 1112-1) and defect of consent (Art. 1130-1144) are more protective than common law
   misrepresentation. Non-reliance clauses carry less weight in French law.

9. **Assuming franchise non-competes require compensation**: Unlike employment non-competes
   in France (which require ~30% of salary), franchise non-competes do not require financial
   compensation. French courts have consistently refused to extend this requirement.

10. **Missing the adhesion contract analysis**: If the franchise agreement qualifies as a
    contrat d'adhésion (Art. 1171 Code civil), unfair terms creating significant imbalance
    can be struck down — but this is subject to the lex specialis of Art. L442-1.

11. **Overlooking the interdependence of contracts**: _Pizza Center France_ (2024) ruled
    that franchise agreement and business lease are interdependent contracts. Termination of
    one may affect the other.

12. **Using English-only analysis**: French franchise law uses specific legal terminology
    (vice du consentement, rupture brutale, réputée non écrite, mise en demeure, agrément,
    droit de préemption). Analysis should use bilingual terminology to ensure precision.

---

## Quality Assurance Framework

### Citation Quality Gates — France

| Gate           | Rule                                                                  | Fail Action                    |
| -------------- | --------------------------------------------------------------------- | ------------------------------ |
| **Source**     | Every claim cites Art. L/R Code de commerce, Art. Code civil, or case | Add citation or "[UNVERIFIED]" |
| **Format**     | Statutes: "Art. L341-2 C. com." / Cases: "Cass. com., date, No. X"    | Fix format                     |
| **Currency**   | Check: post-Macron Law 2015? Post-2016 reform? Post-2022 VBER?        | Flag "[CHECK CURRENCY]"        |
| **Domain**     | French law only; flag EU overlay where relevant                       | Confirm jurisdiction           |
| **Confidence** | Uncertainty stated, especially for evolving case law                  | Add qualifier                  |

### Confidence Scoring

- **Definite (0.95-1.0)**: Clear statute directly on point (Art. L341-2 non-compete limits,
  Art. 1104 good faith)
- **High (0.80-0.94)**: Strong case law (Cass. com.) confirming interpretation (_Domino's_
  on significant imbalance)
- **Probable (0.60-0.79)**: Lower court decisions or evolving Cour de cassation position
  (_ERA France_ on non-reaffiliation — recent, may be refined)
- **Possible (0.40-0.59)**: Genuinely open question (application of Art. 1171 when
  Art. L442-1 also applies)
- **Unlikely (0.0-0.39)**: Speculative; flag "[UNCERTAIN]"

---

## Glass Box Audit Trail

```yaml
glass_box:
  agreement: "[Contrat de franchise — title and date]"
  franchisor: "[Franchisor name]"
  agreement_type: "[Standard / Multi-unit / Master Franchise / Sub-franchise]"
  user_side: "[Prospective Franchisee / Existing Franchisee / Franchisor]"
  operating_jurisdiction: "France"
  governing_law: "[French / Other — note mandatory French provisions apply regardless]"
  agreement_date: "[date — determines applicable law version]"
  applicable_frameworks:
    - "Loi Doubin (Art. L330-3 / R330-1 C. com.)"
    - "Art. L442-1 C. com. (déséquilibre significatif, rupture brutale)"
    - "Art. L341-2 C. com. (Macron Law — non-compete)"
    - "Art. 1104 Code civil (good faith)"
    - "EU VBER 2022/720"
    - "[FFF Code de déontologie if member]"
  dip_compliance:
    provided: "Yes / No"
    timing: "[days before signing] — 20-day minimum"
    art_r330_1_elements: "Complete / Deficiencies — [list]"
    annual_accounts_appended: "Yes / No"
    network_departures_disclosed: "Yes / No"
    market_analysis_substantiated: "Yes / No / Insufficient"
  defect_of_consent:
    risk_level: "Low / Medium / High"
    grounds: "[Error / Dol / Neither identified]"
  significant_imbalance:
    clauses_screened: "[number]"
    potentially_imbalanced: "[number] — [list]"
    global_balance_assessment: "Balanced / Imbalanced / Mixed"
  good_faith:
    art_1104_exclusion: "None / Present (RED)"
    concerns: "[list or none]"
  non_compete:
    post_term_present: "Yes / No"
    art_l341_2_compliant: "Compliant / Non-compliant — [which condition(s) failed]"
    duration: "[months]"
    geographic_scope: "[premises / broader — specify]"
    know_how_indispensability: "Demonstrated / Not demonstrated / Not assessed"
  rupture_brutale:
    applicable: "Yes / No / Not yet relevant"
    relationship_duration: "[years]"
    notice_provided: "[months]"
    adequate_notice: "Yes / No / Not assessed"
  termination:
    reciprocal: "Yes / No"
    cure_period: "[days / none]"
    clause_resolutoire: "Present / Absent"
  transfer:
    agrement_required: "Yes / No"
    preemption_right: "Present / Absent"
    intuitu_personae: "Bilateral / Unilateral / Absent"
  competition_law:
    vber_applicable: "Yes / No (market share >30%)"
    hardcore_restrictions: "[None / RPM / Passive sales / Online — list]"
  clauses_reviewed: 16
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  legalcode_mcp: "Connected / Not connected"
  statutes_consulted:
    - "Art. L330-3 / R330-1 C. com. — [VERIFIED / UNVERIFIED]"
    - "Art. L341-2 C. com. — [VERIFIED / UNVERIFIED]"
    - "Art. L442-1 C. com. — [VERIFIED / UNVERIFIED]"
    - "Art. 1104 Code civil — [VERIFIED / UNVERIFIED]"
    - "VBER 2022/720 — [VERIFIED / UNVERIFIED]"
  case_law_consulted:
    - "[Case — VERIFIED / UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Scope limitations, assumptions, caveats]"
  reviewer: "AI-assisted — requires qualified French avocat review"
```

---

## Provenance

Created by Legalcode (2026-03-19). Jurisdiction-specific variant of
`legalcode-franchise-agreement-review`. French-specific research covering:

- Loi Doubin (Art. L330-3 / R330-1 Code de commerce) and DIP requirements
- Art. L341-2 Code de commerce (Macron Law 2015) — post-term non-compete
- Art. L442-1 Code de commerce — significant imbalance and rupture brutale
- Art. 1104 Code civil — mandatory good faith
- EU VBER 2022/720 — vertical agreements block exemption
- Cour de cassation jurisprudence (_Domino's Pizza_ 2024, _ERA France_ 2024,
  _Pizza Center France_ 2024)
- Autorité de la concurrence enforcement (_De Neuville_ 2024)
- FFF European Code of Ethics for Franchising

Research sources:

- [ICLG Franchise Laws France 2026](https://iclg.com/practice-areas/franchise-laws-and-regulations/france)
- [Légifrance — Art. L330-3 C. com.](https://www.legifrance.gouv.fr/)
- [Légifrance — Art. R330-1 C. com.](https://www.legifrance.gouv.fr/)
- [Légifrance — Art. L341-2 C. com.](https://www.legifrance.gouv.fr/)
- [Autorité de la concurrence — De Neuville](https://www.autoritedelaconcurrence.fr/)
- [FFF — Code de déontologie](https://www.franchise-fff.com/)
- [Lexology — Post-term non-compete in franchise](https://www.lexology.com/)
- [Concurrences — Domino's Pizza / ERA France](https://www.concurrences.com/)
