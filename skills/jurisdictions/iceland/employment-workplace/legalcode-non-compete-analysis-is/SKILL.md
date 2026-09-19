---
name: legalcode-non-compete-analysis-is
description: 'Analyse non-compete clause (samkeppnisákvæði) enforceability under Icelandic law — apply
  the two-prong test under Section 37 of Lög nr. 7/1936 (Contracts Act): (1) necessity to prevent competition,
  and (2) unreasonable restriction on freedom of employment (atvinnufrelsi), with balancing of the rightholder''s
  interest under 37(2). Use when reviewing non-compete provisions in Icelandic employment agreements (ráðningarsamningar),
  executive contracts (stjórnendasamningar), severance agreements (starfslokasamningar), shareholder agreements
  (hluthafasamningar), or business sale agreements (kaupsamningar um atvinnurekstur); evaluating post-employment
  covenant enforceability; advising on restrictive covenant strategy for Icelandic employers; or comparing
  Icelandic non-compete rules against Nordic peers (Norway, Denmark, Sweden, Finland).'
metadata:
  jurisdiction: Iceland
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Analyse non-compete clause (samkeppnisákvæði) enforceability under Icelandic law — apply the two-prong test under Section 37 of Lög nr. 7/1936 (Contracts Act): (1) necessity to prevent competition, and (2) unreasonable restriction on freedom of employment (atvinnufrelsi), with balancing of the rightholder's interest under 37(2). Screen for automatic voidance under Section 37(3) where the employee was dismissed without cause or constructively dismissed. Evaluate duration, geographic scope, activity scope, compensation adequacy, and legitimate business interests in the context of Iceland's small market (~380,000 population). Covers employment non-competes, business-sale restrictions, non-solicitation, and the statutory trade secret protection under Lög nr. 57/2005. Distinguish between restrictive covenant types (samkeppnisbann, bann við hvatningu viðskiptavina, trúnaðarskylda). Apply Section 36 (general fairness override) where applicable. Generate enforceability risk matrix with confidence-scored assessment, recommended modifications, and auditable Glass Box trail. Use when reviewing non-compete provisions in Icelandic employment agreements (ráðningarsamningar), executive contracts (stjórnendasamningar), severance agreements (starfslokasamningar), shareholder agreements (hluthafasamningar), or business sale agreements (kaupsamningar um atvinnurekstur); evaluating post-employment covenant enforceability; advising on restrictive covenant strategy for Icelandic employers; or comparing Icelandic non-compete rules against Nordic peers (Norway, Denmark, Sweden, Finland). Produces GREEN/YELLOW/RED classification with confidence-scored enforceability assessment and auditable Glass Box trail.


# Legalcode Non-Compete Analysis — Iceland (samkeppnisákvæði)

> **Disclaimer / Fyrirvari**: This skill provides a framework for AI-assisted non-compete
> enforceability analysis under Icelandic law. It does not constitute legal advice (lögfræðiráðgjöf).
> All outputs require review by a qualified Icelandic lawyer (lögfræðingur / lögmaður) before
> relying on them for any enforcement, litigation, compliance, or negotiation decision. Icelandic
> non-compete law derives primarily from Section 37 of a 1936 statute and is heavily shaped by
> case law — verify current judicial treatment before acting. Statutory and case law references
> cited from memory carry hallucination risk — verify against authoritative sources (Althingi,
> Hæstiréttur, Landsréttur) before relying on them. This skill does not substitute for
> individual legal advice regarding specific employment situations or non-compete enforcement
> strategy.

---

## Purpose and Scope

This skill analyses whether a non-compete clause (samkeppnisákvæði) is enforceable under
Icelandic law, identifies risk factors that courts consider, generates confidence-scored
enforceability assessments, and produces actionable modification suggestions.

**Covers:**

- Full analysis under Lög nr. 7/1936, 37. gr. (Contracts Act, Section 37) — the primary
  non-compete provision in Icelandic law
- Two-prong statutory test: necessity (1. mgr.) and unreasonable restriction (1. mgr. + 2. mgr.)
- Automatic voidance screening under 37(3) — dismissal without cause / constructive dismissal
- Section 36 (general fairness override) as supplementary ground for challenging enforceability
- Trade secret protection under Lög nr. 57/2005 (Surveillance of Commercial Practices and Marketing)
  — statutory 3-year post-employment prohibition on disclosing professional secrets
- Distinction between employment non-competes and business-sale non-competes
- Compensation analysis (not statutory but strongly affects enforceability assessment)
- Duration, geographic scope, and activity scope analysis for Iceland's concentrated market
- Liquidated damages / contractual penalty (samningsbætur) clauses for non-compete breach
- Nordic comparative context (Norway §14A WEA, Denmark Employment Clauses Act, Finland 2022
  reform, Sweden 2015 CBA) for employers operating across the Nordics
- Enforceability risk matrix with confidence-scored classification
- Glass Box audit trail

**Does not:**

- Draft new non-compete clauses from scratch (see `legalcode-employment-agreement-review`)
- Provide personal legal advice or guarantee court outcomes
- Analyse non-competes governed by non-Icelandic law (see `legalcode-non-compete-enforceability`
  for US; jurisdiction-specific variants for UK, Germany, France, China)
- Cover competition law / antitrust restrictions (Lög nr. 44/2005 um samkeppni)
- Cover non-compete provisions in franchise agreements or agency agreements as primary analysis

**Related skills:**

- `legalcode-non-compete-enforceability` — US 50-state non-compete enforceability analysis
- `legalcode-employment-agreement-review` — full employment agreement clause-by-clause review
- `legalcode-nda-triage` — NDA and confidentiality covenant review
- `legalcode-iceland-real-estate-contracts` — Icelandic real estate transaction documents

---

## Jurisdiction and Governing Law

This skill is **specific to Iceland** and analyses enforceability under:

| Statute             | Full Name (Icelandic)                                                                               | Coverage                                                                                                  |
| ------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Lög nr. 7/1936**  | Lög um samningsgerð, umboð og ógilda löggerninga                                                    | Primary non-compete provision (37. gr.) and general fairness (36. gr.)                                    |
| **Lög nr. 57/2005** | Lög um eftirlit viðskiptahátta og markaðssetningu                                                   | Statutory trade secret protection — 3-year post-employment prohibition on disclosing professional secrets |
| **Lög nr. 55/1980** | Lög um starfskjör launafólks og skyldutryggingu lífeyrisréttinda                                    | Collective agreement framework — CBAs set minimum employment terms                                        |
| **Lög nr. 19/1979** | Lög um rétt verkafólks til uppsagnarfrests frá störfum og til launa vegna sjúkdóms og slysaforfalla | Notice period and termination rights                                                                      |

**Key regulatory and judicial bodies:**

- **Hæstiréttur Íslands** (Supreme Court) — final authority on non-compete enforceability
- **Landsréttur** (Court of Appeal, est. 2018) — intermediate appellate review
- **Héraðsdómstólar** (District Courts) — first instance
- **SA** (Samtök atvinnulífsins / Confederation of Icelandic Enterprise) — employer guidance
- **ASÍ** (Alþýðusamband Íslands / Icelandic Confederation of Labour) — worker protections

**Authoritative text sources:**

- Althingi: https://www.althingi.is/lagas/nuna/1936007.html (Lög nr. 7/1936 — current text)
- Official English translation: https://www.stjornarradid.is/media/atvinnuvegaraduneyti-media/media/acrobat/samningalog_tyddaensku.doc

---

## Key Legal Framework — Section 37 of Lög nr. 7/1936

### 37. gr. 1. mgr. — The Two-Prong Test (All Non-Competes)

> "Hafi maður, í því skyni að varna samkeppni, áskilið sér hjá öðrum manni að sá maður reki
> eigi verslun eða aðra atvinnu, eða hann ráði sig eigi til starfa við slíkt fyrirtæki, þá er
> það loforð eigi bindandi fyrir þann mann ef telja verður, þegar litið er til allra atvika, að
> skuldbinding þessi sé víðtækari en nauðsynlegt er til þess að varna samkeppni eða hún skerði
> með ósanngjörnum hætti atvinnufrelsi þess manns sem tókst þessa skyldu á herðar."

**English:** If, for the purpose of preventing competition, a person has obtained a commitment
from another person not to engage in a commercial undertaking or other business, or not take
up employment at such an undertaking, the promise is **not binding** if, in light of all
circumstances, the commitment:

1. **Goes beyond what is necessary** to prevent competition (necessity prong); **OR**
2. **Unreasonably restricts** the freedom of employment (atvinnufrelsi) of the bound person
   (reasonableness prong)

**Either prong failing is sufficient to void the clause.** Both must be satisfied for
the non-compete to be enforceable.

### 37. gr. 2. mgr. — Balancing the Rightholder's Interest

> "Við mat á hinu síðastnefnda atriði skal einnig hafa hliðsjón af því hversu miklu það varðar
> rétthafann að þessi skuldbinding sé haldin."

**English:** In assessing the reasonableness of the restriction, **regard shall also be had
to how much it matters to the rightholder** that the commitment be upheld.

This is a **proportionality balancing test**: the more significant the employer's interest
in enforcing the restriction, the wider a scope the court will tolerate. But the restriction
must never go beyond necessity (1. mgr., first limb) regardless of the employer's interest.

### 37. gr. 3. mgr. — Employee-Specific Automatic Voidance

> "Hafi starfsmaður við verslun eða annað fyrirtæki tekið á sig slíka skuldbindingu [...] þá er
> sú skuldbinding ógild ef honum er sagt upp stöðunni eða vikið úr henni án þess að hann hafi
> sjálfur gefið nægilega ástæðu til þess eða ef hann sjálfur fer löglega úr stöðunni sakir þess
> að sá, sem fyrirtækið rekur, vanefnir skyldur sínar við hann."

**English:** An employee's post-employment non-compete obligation is **void (ógild)** if:

1. The employee is **dismissed or removed without having given adequate cause** (uppsögn án
   nægilegrar ástæðu); **OR**
2. The employee **lawfully leaves** because the employer **breached its obligations** toward
   the employee (constructive dismissal / vanefndir vinnuveitanda)

**This is an automatic voidance rule — not a factor in a balancing test.** If either condition
applies, the non-compete is void regardless of its scope, compensation, or the employer's
legitimate interests.

**Practical implication:** Non-compete enforceability in Iceland depends significantly on
**how the employment ended**. This must be established at Step 2 before any further analysis.

### 36. gr. — General Fairness Override

Section 36 of Lög nr. 7/1936 provides that **any contract** may be set aside, in whole or in
part, or amended, if invoking it would be "unfair or contrary to good business practices"
(ósanngjarnt eða andstætt góðri viðskiptavenju). This is a supplementary ground for
challenging a non-compete that passes the Section 37 test but is nonetheless unconscionable
in the specific circumstances.

Courts consider: the substance of the contract; the parties' positions; circumstances at
formation; and subsequent developments. Section 36 has Nordic-wide equivalents (the
"general clause") and is broadly applied across all Nordic jurisdictions.

---

## Statutory Trade Secret Protection — Lög nr. 57/2005

Separate from any contractual non-compete, Icelandic law provides a **statutory prohibition**
on disclosing professional secrets:

- Anyone with knowledge or control over professional secrets (atvinnuleyndarmál) may not
  provide such information without permission for **three years** following the end of employment
- Anyone entrusted with plans, descriptions, recipes, models or the like is forbidden from
  using this information or providing it to others without authorisation
- This applies **regardless of whether a contractual non-compete exists**
- It protects **information**, not competitive activity — it does not prevent the former
  employee from working for a competitor, only from disclosing or using secrets

**Practical implication:** Even where a non-compete clause is void (e.g., under Section 37(3)),
the employer retains statutory trade secret protection for three years. This is the fallback
enforcement mechanism — similar to DTSA/UTSA in the US context.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points marked **⟁ CLARIFY**
throughout the workflow. Rather than assuming context, the analysis pauses when:

- The termination scenario is unknown (critical for 37(3) automatic voidance)
- The context is employment vs. business sale (determines which subsections of 37. gr. apply)
- The employee's role and access to trade secrets is unclear
- Compensation arrangements are ambiguous
- The clause applies across multiple Nordic jurisdictions
- Geographic scope is broad relative to Iceland's small market

Present clarification questions as structured options with brief "Af hverju skiptir þetta máli /
Why this matters" explanations. If context has already been provided, skip the question and
**state your assumption explicitly**.

---

## Workflow

### Step 1: Accept Input

Accept the non-compete clause in any of these formats:

- **Clause text:** Pasted directly from the employment or business agreement (Icelandic or English)
- **Full agreement:** PDF, DOCX, or full agreement text (skill extracts the relevant clause)
- **Description:** User describes the non-compete terms verbally
- **Multiple clauses:** Set of non-compete clauses from an employment audit or M&A diligence

If no clause is provided, ask: "Vinsamlegast deildu samkeppnisákvæðinu eða lýstu meginatriðum
þess (tímalengd, landfræðilegt gildissvið, takmarkaðar athafnir og bætur á samningstímabilinu)."
/ "Please share the non-compete clause text or describe its key terms (duration, geographic
scope, restricted activities, and any compensation during the restriction period)."

---

### Step 2: Gather Context

**⟁ CLARIFY** — Before analysing enforceability, confirm these facts:

**1. Is this an employment non-compete or a business-sale non-compete?**

- Options: Employment agreement (ráðningarsamningur), Executive/director contract
  (stjórnendasamningur), Shareholder agreement (hluthafasamningur), Business sale
  (kaup á atvinnurekstri), Partnership (félag), Other (describe)
- _Why this matters (Af hverju skiptir þetta máli)_: Section 37(3) automatic voidance
  applies **only to employees**. Business-sale non-competes face the 37(1)-(2) test but
  with greater deference to the parties' commercial bargain, and courts tolerate longer durations.

**2. How did (or will) the employment end?** (Employment context only)

- Options: Employee resigned voluntarily (starfsmaður sagði upp sjálfur), Employee was
  dismissed without cause / redundancy (uppsögn án ástæðu), Employee was dismissed for cause
  (uppsögn vegna ástæðu), Constructive dismissal — employee left due to employer breach
  (vanefndir vinnuveitanda), Still employed (prospective analysis), Not applicable (business sale)
- _Why this matters_: Under Section 37(3), the non-compete is **automatically void** if the
  employee was dismissed without adequate cause or left due to employer breach. This is a
  binary gate — if triggered, no further enforceability analysis is needed.

**3. What is the employee's role and access to sensitive information?**

- Options: Senior executive / C-suite (æðstu stjórnendur), Mid-level manager, Technical specialist
  with trade secret access, Sales / client-facing with key customer relationships, General employee,
  Board member (stjórnarmaður), Other (describe)
- _Why this matters_: The necessity prong of Section 37(1) requires the employer to demonstrate
  a legitimate business interest. Higher-level roles with genuine access to trade secrets or
  strategic customer relationships support stronger non-competes. General employees without
  such access are harder to restrict.

**4. Is compensation provided during the restriction period?**

- Options: Yes — continued salary (full or partial), Yes — lump sum at termination or signing,
  Yes — enhanced salary during employment served as consideration, No compensation, Unknown
- _Why this matters_: Iceland does not have a mandatory compensation requirement (unlike
  Norway, Denmark, Finland). However, the absence of compensation weighs heavily against
  enforceability in the reasonableness assessment under 37(1)-(2). Compensation strengthens
  the employer's position significantly.

**5. What industry and sector?**

- Options: Financial services (fjármálaþjónusta), Technology / software (tæknifyrirtæki),
  Healthcare (heilbrigðisþjónusta), Fisheries / maritime (sjávarútvegur), Tourism / hospitality
  (ferðaþjónusta), Energy (orkumál), Professional services / consulting (ráðgjöf), Retail /
  commerce (verslun), Other (describe)
- _Why this matters_: Iceland has no sector-specific non-compete legislation, but the nature
  of the industry affects the necessity analysis. In Iceland's small, concentrated market,
  some industries have only 2-3 major employers — broad non-competes may effectively
  prevent the employee from working in their field entirely.

**6. Does the clause apply across multiple Nordic jurisdictions?**

- Options: Iceland only, Iceland + Norway, Iceland + Denmark, Iceland + Sweden, Iceland +
  Finland, Pan-Nordic, Other
- _Why this matters_: If the employer operates across the Nordics, a single non-compete
  clause may be subject to different enforceability standards. Norway requires mandatory
  compensation; Denmark caps combined non-compete + non-solicitation at 6 months; Finland
  requires 40-60% compensation. Multi-jurisdiction analysis may be needed.

---

### Step 3: Extract Clause Terms

From the provided non-compete text or description, extract:

| Element                         | Icelandic Term             | Extracted Value                                                                         | Notes |
| ------------------------------- | -------------------------- | --------------------------------------------------------------------------------------- | ----- |
| Duration                        | Tímalengd                  | [X months / years]                                                                      |       |
| Geographic scope                | Landfræðilegt gildissvið   | [Iceland-wide / Capital area / Named competitors / None stated]                         |       |
| Activity scope                  | Samkeppnisumfang           | [All competing business / Specific role / Specific named companies / Specific products] |       |
| Compensation during restriction | Bætur á samningstímabilinu | [None / Salary continuation / Lump sum / Enhanced salary]                               |       |
| Legitimate interest stated      | Lögmætir hagsmunir         | [Trade secrets / Customer relationships / Training investment / None stated]            |       |
| Contractual penalty clause      | Samningsbætur              | [Amount / Formula / Absent]                                                             |       |
| Severability clause             | Aðskilnaðarákvæði          | [Present / Absent]                                                                      |       |
| Termination trigger             | Lokaákvæði                 | [All terminations / Employee resignation only / Any party / Silent]                     |       |

If any element is absent or ambiguous, **⟁ CLARIFY** with the user before proceeding.

---

### Step 4: Apply Section 37(3) Automatic Voidance Screening

**This is the first enforceability gate — apply before any other analysis.**

If the context is **employment** (not business sale), check the termination scenario
established at Step 2:

| Termination Scenario                                                      | Section 37(3) Result                                                      | Action                                                           |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Employee dismissed without adequate cause (uppsögn án nægilegrar ástæðu)  | **VOID (ógild)**                                                          | Stop analysis. Return BAN classification.                        |
| Constructive dismissal — employee left due to employer breach (vanefndir) | **VOID (ógild)**                                                          | Stop analysis. Return BAN classification.                        |
| Employee resigned voluntarily (starfsmaður sagði upp sjálfur)             | Not void — proceed to Step 5                                              | Continue analysis.                                               |
| Employee dismissed for cause (uppsögn vegna ástæðu starfsmanns)           | Not void — proceed to Step 5                                              | Continue analysis.                                               |
| Redundancy / restructuring (skipulagsbreytingar)                          | **Likely VOID** — redundancy is dismissal without employee cause [VERIFY] | Flag as HIGH RISK; likely void under 37(3).                      |
| Still employed (prospective analysis)                                     | Not yet triggered — analyse assuming voluntary departure                  | Note that enforceability depends on future termination scenario. |

If 37(3) is triggered, return immediately:

> **⛔ AUTOMATIC VOIDANCE — NON-COMPETE IS VOID (ógild)**
> Under Section 37(3) of Lög nr. 7/1936, the employee's post-employment non-compete obligation
> is void because [the employee was dismissed without adequate cause / the employee lawfully
>
> > left due to the employer's breach of obligations].
> > **Confidence:** DEFINITE (0.95) — Section 37(3) is a clear statutory rule.
> > **Note:** The statutory trade secret protection under Lög nr. 57/2005 remains in effect for
> > three years regardless of non-compete voidance. The employer may still protect confidential
> > information through confidentiality obligations.

---

### Step 5: Apply the Two-Prong Test Under Section 37(1)-(2)

For clauses that survive the 37(3) screening, apply the two-prong test:

**Prong 1 — Necessity (er skuldbindingin víðtækari en nauðsynlegt?)**

The restriction must not go **beyond what is necessary** to prevent competition. Evaluate:

**5a. Legitimate Business Interest (lögmætir hagsmunir)**

| Interest Category                                                | Enforceability Weight  | Iceland-Specific Notes                                                                                                                                                 |
| ---------------------------------------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Trade secrets / proprietary knowledge (atvinnuleyndarmál)**    | HIGH — strongest basis | Overlaps with statutory protection under Lög nr. 57/2005 (3-year duty of confidence). Non-compete adds value by preventing competitive employment, not just disclosure |
| **Client relationships / customer goodwill (viðskiptatengsl)**   | HIGH — well-recognised | In Iceland's small market, key client relationships are particularly valuable; departing employees can divert business quickly given the concentrated market           |
| **Specialised training / employer investment (sérhæfð þjálfun)** | MODERATE               | Must be extraordinary training beyond standard industry education; employer must have made significant investment                                                      |
| **Business strategies / pricing (viðskiptaáætlanir)**            | MODERATE               | Must actually be confidential; generic market knowledge is not protectable                                                                                             |
| **Market-sensitive information**                                 | MODERATE               | Particularly relevant in Iceland's thin financial markets                                                                                                              |

**5b. Scope Necessity**

Is the restriction wider than necessary to protect the identified interest? Consider:

- Could a **narrower restriction** (non-solicitation, confidentiality) achieve the same protection?
- Does the restriction cover activities **unrelated** to the protectable interest?
- In Iceland's small market, even a moderate restriction may effectively bar the employee
  from their entire profession — does the restriction account for this?

**Prong 2 — Unreasonable Restriction on Freedom of Employment (ósanngjörn skerðing á atvinnufrelsi)**

Under 37(1), second limb, the restriction must not **unreasonably restrict** freedom of
employment. Under 37(2), the court must also weigh **how much it matters to the rightholder**
(employer) that the restriction be upheld.

**Factors in the reasonableness balancing test:**

| Factor                              | Favours Enforcement                                    | Favours Voidance                                |
| ----------------------------------- | ------------------------------------------------------ | ----------------------------------------------- |
| **Compensation during restriction** | Salary continuation or substantial lump sum            | No compensation — employee bears full burden    |
| **Duration**                        | 6-12 months                                            | > 12 months (see Section 6 duration analysis)   |
| **Geographic scope**                | Targeted (named competitors, specific area)            | Iceland-wide or unlimited                       |
| **Activity scope**                  | Limited to employee's actual role / products           | All competing activity regardless of connection |
| **Employee seniority**              | Senior executive with significant access               | Junior / general employee                       |
| **Alternative employment**          | Multiple alternative employers exist in Iceland        | Employee effectively barred from profession     |
| **Employer's interest (37(2))**     | Genuine trade secrets, high-value client relationships | Generalized interest in preventing competition  |
| **Iceland's small market**          | Restriction accounts for limited alternatives          | Restriction ignores market concentration        |

**Iceland's small market — the critical contextual factor:**

Iceland has approximately 380,000 people, with the greater Reykjavik capital area housing
~230,000 (63%). Many industries have only a handful of employers. A non-compete that would
be reasonably scoped in a larger market may be **unreasonably restrictive** in Iceland because
the employee has nowhere else to go. Courts must weigh this reality when assessing whether
the restriction "unreasonably restricts freedom of employment."

Example: A non-compete barring an employee from working for "any competing financial services
firm in Iceland" may effectively bar the employee from the entire Icelandic financial sector
(5-8 major firms). The same restriction in a larger market with hundreds of firms would be
more reasonable.

**If either prong fails:** Classify as RED. Proceed to Step 7 for modification analysis.

---

### Step 6: Duration, Geographic, and Activity Scope Analysis

#### 6a. Duration Analysis — Icelandic Context

| Duration     | Enforceability Assessment                                                                                             | Notes                                                                        |
| ------------ | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| ≤ 6 months   | Generally reasonable; strong enforceability signal                                                                    | Within standard range; courts unlikely to object on duration alone           |
| 7–12 months  | Reasonable for senior roles with genuine trade secret access                                                          | Standard range; supported by Hæstiréttur 124/2003 reasoning                  |
| 13–18 months | Elevated scrutiny; needs strong justification and compensation                                                        | Approaches outer bounds; Iceland's small market makes this more burdensome   |
| 19–24 months | HIGH scrutiny; upheld in Hæstiréttur 124/2003 but only because restriction was narrowly targeted to 4 named companies | Exceptional; requires narrow scope + strong business interest + compensation |
| > 24 months  | Presumptively unreasonable for employment non-competes                                                                | Likely void under Section 37(1) unless extraordinarily narrow scope          |

**Business sale context:** Longer durations (2-5 years) are more readily accepted where the
seller received purchase consideration reflecting the goodwill being protected.

**Nordic comparison (employment non-competes):**

| Country     | Maximum Duration                          | Mandatory Compensation                     |
| ----------- | ----------------------------------------- | ------------------------------------------ |
| **Iceland** | No statutory cap (6-12 months typical)    | No (but strongly favours enforceability)   |
| **Norway**  | 12 months (statutory cap)                 | Yes — 100% salary up to 8G                 |
| **Denmark** | 12 months (6 months for combined NC + NS) | Yes — 40-60% of salary                     |
| **Finland** | 12 months                                 | Yes — 40-60% of salary (since 2022 reform) |
| **Sweden**  | 9-18 months (CBA guidance)                | 60% of salary (CBA standard)               |

#### 6b. Geographic Scope Analysis — Iceland-Specific

| Scope                                  | Enforceability Assessment                              | Iceland-Specific Notes                                     |
| -------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------- |
| Named competitors (specific companies) | STRONGEST — follows Hæstiréttur 124/2003 approach      | Clearly bounded; employee knows exactly what is restricted |
| Specific sector in capital area        | Generally reasonable                                   | Capital area ≈ 63% of population, major economic centre    |
| Iceland-wide, specific sector          | Moderate — reasonable if sector has multiple employers | Scrutinise whether employee has realistic alternatives     |
| Iceland-wide, broad industry           | ELEVATED RISK — may be overbroad given small market    | Could effectively bar employee from profession             |
| Unlimited / global                     | HIGH RISK — overbroad for most Icelandic employers     | Only defensible for genuinely international businesses     |

#### 6c. Activity Scope Analysis

| Activity Scope                                          | Enforceability Assessment                                   |
| ------------------------------------------------------- | ----------------------------------------------------------- |
| Limited to employee's actual role / product lines       | Strong — correlates to protectable interest                 |
| Specific named competitors (as in Hæstiréttur 124/2003) | Strong — clear and limited                                  |
| "Competing business" in same sector                     | Moderate — acceptable if sector-specific and duration short |
| "Any business competing with any product or service"    | OVERBROAD — RED flag; likely fails necessity prong          |
| "Any employment in the industry"                        | HIGH RISK — overbroad in Iceland's concentrated market      |

---

### Step 7: Compensation Analysis

Although Iceland does not **mandate** non-compete compensation (unlike Norway, Denmark,
Finland, and Sweden), compensation is a **critical factor** in the enforceability assessment:

| Compensation Arrangement                                       | Effect on Enforceability                                                       |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Salary continuation during restriction (full or substantial)   | STRONG positive factor — employee not financially harmed                       |
| Lump sum at signing or termination                             | MODERATE positive factor — weaker than salary continuation                     |
| Enhanced salary during employment (as in Hæstiréttur 124/2003) | MODERATE positive factor — court acknowledged salary increase as consideration |
| Only continued employment as consideration                     | WEAK — may be insufficient for mid-employment amendments                       |
| No compensation                                                | NEGATIVE factor — weighs heavily against enforceability in reasonableness test |

**Recommendation:** Even though not legally required, advise employers to provide compensation
during the non-compete period. This dramatically strengthens enforceability and aligns with
Nordic best practice. As a benchmark, use the Nordic range: 40-60% of salary.

---

### Step 8: Contractual Penalty / Liquidated Damages Analysis (samningsbætur)

Icelandic non-compete clauses frequently include contractual penalty provisions. Per
Hæstiréttur 124/2003:

- **Contractual penalties are enforceable** under Icelandic law
- The employer **does not need to prove actual damages** when a valid penalty clause exists
- Courts retain **discretion to adjust the penalty amount** — in Case 124/2003, the court
  adjusted the amount from the stipulated daily penalty rate to a figure based on the
  employee's monthly salary and the salary increase received at contract signing (ISK 900,000)
- **Section 36 may be used to moderate** an unconscionable penalty amount

| Penalty Assessment                                                         | Enforceability                                                                     |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Fixed, reasonable amount (proportional to salary and restriction duration) | Enforceable; court may adjust at margins                                           |
| Daily/weekly accumulating penalty                                          | Enforceable in principle; court likely to cap total amount                         |
| Disproportionately large amount (e.g., multiples of annual salary)         | Risk of Section 36 moderation; court will reduce                                   |
| No penalty clause                                                          | Employee is only liable for proven actual damages — harder for employer to enforce |

---

### Step 9: Generate Enforceability Score and Classification

**9a. Enforceability Classification**

| Classification | Score Range | Meaning                                                               | Action                                                           |
| -------------- | ----------- | --------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **🟢 GREEN**   | 0.75–1.0    | Likely enforceable; reasonable scope and supporting factors           | Enforce as written; minor modifications only                     |
| **🟡 YELLOW**  | 0.50–0.74   | Mixed enforceability signals; some risk factors                       | Redline to reduce scope; enforceable if modifications adopted    |
| **🔴 RED**     | 0.20–0.49   | Significant enforceability risk; likely fails one or both prongs      | Substantial redlines required; high litigation risk              |
| **⛔ VOID**    | 0.0–0.19    | Void by operation of law (Section 37(3)) or clearly fails both prongs | Cannot be enforced; focus on Lög 57/2005 trade secret protection |

**9b. Redline Generation**

For each enforceability weakness, generate a redline suggestion:

_Duration overbreadth:_

> **Current:** "í 24 mánuði frá starfslokum" / "for 24 months from termination"
> **Redline:** "í 12 mánuði frá starfslokum" / "for 12 months from termination"
> **Rationale:** 24-month duration exceeds typical Icelandic benchmarks for employment
> non-competes. 12 months is within the standard range and aligns with Nordic norms.
> **Confidence:** PROBABLE (0.70)

_Scope overbreadth:_

> **Current:** "í hvers kyns samkeppnisstarfsemi á Íslandi" / "in any competing activity in Iceland"
> **Redline:** "hjá [nafngreindum fyrirtækjum]" / "with [named competing companies]" or
> "í [tiltekinni starfsemi] á höfuðborgarsvæðinu" / "in [specific activity] in the capital area"
> **Rationale:** Iceland-wide blanket restriction on all competing activity effectively bars
> the employee from their profession given the concentrated market. Narrowing to named
> competitors or specific activities preserves the employer's interest while respecting
> freedom of employment. Follows the approach upheld in Hæstiréttur 124/2003.

_No compensation:_

> **Current:** No compensation provision during restriction period
> **Redline:** Add: "Á samningstímabilinu greiðir vinnuveitandi starfsmanni [X]% af
> meðalmánaðarlaunum síðustu [12] mánaða" / "During the restriction period, employer shall
> pay employee [X]% of average monthly salary over the preceding [12] months"
> **Rationale:** Although not legally required in Iceland, compensation dramatically
> strengthens enforceability and aligns with Nordic standards (Norway 100%, Denmark 40-60%,
> Finland 40-60%, Sweden 60%).

_Missing termination trigger:_

> **Current:** Clause applies to "all terminations"
> **Redline:** Add: "Samkeppnisákvæðið gildir ekki ef starfsmanni er sagt upp án fullnægjandi
> ástæðu" / "The non-compete does not apply if the employee is dismissed without adequate cause"
> **Rationale:** Section 37(3) already makes this the law — but stating it explicitly in the
> contract avoids disputes and demonstrates the employer's understanding of the legal framework.

---

### Step 10: Glass Box Audit Trail

Append a completed Glass Box audit section to every output (template in Section 14).

---

## Section 11: Business Sale vs. Employment — Key Distinctions

| Factor                     | Employment Non-Compete                            | Business Sale Non-Compete                             |
| -------------------------- | ------------------------------------------------- | ----------------------------------------------------- |
| **Governing provision**    | 37. gr. 1. + 2. + **3. mgr.**                     | 37. gr. 1. + 2. mgr. only                             |
| **Section 37(3) voidance** | Yes — void if dismissed without cause             | Not applicable                                        |
| **Court scrutiny**         | Strict — employee has unequal bargaining power    | More deferential — seller freely chose to sell        |
| **Typical duration**       | 6-12 months (max ~24 months if very narrow)       | 2-5 years routinely upheld                            |
| **Geographic scope**       | Must account for Iceland's small market           | Wider scope acceptable (seller was paid for goodwill) |
| **Compensation**           | Not mandatory but strongly affects enforceability | Purchase price serves as consideration                |
| **Rationale**              | Employee needs to earn a living                   | Seller received purchase price reflecting goodwill    |

---

## Section 12: Non-Compete vs. Related Restrictive Covenants in Iceland

### Samkeppnisbann (Non-Compete)

- Prevents working for a competitor or engaging in competing business
- Subject to full 37. gr. analysis (most restrictive; hardest to enforce)
- Most likely to be challenged on reasonableness grounds

### Bann við hvatningu viðskiptavina (Non-Solicitation)

- Prevents actively soliciting the employer's clients or recruiting employees
- Still subject to Section 37 but **easier to enforce** — narrower restriction
- Does not prevent working for a competitor, only approaching specific relationships
- Courts more likely to uphold because it targets specific relationships rather than
  broadly restricting freedom of employment

### Trúnaðarskylda / þagnarskylda (Confidentiality / Non-Disclosure)

- Prevents disclosure or use of confidential information
- Easiest to enforce — does not restrict where someone works
- Supplemented by **statutory** trade secret protection under Lög nr. 57/2005 (3 years)
- Enforceable even where the non-compete itself is void

**Enforceability hierarchy (most to least restrictive / hardest to easiest to enforce):**

1. Non-compete (samkeppnisbann) — hardest to enforce
2. Non-solicitation (bann við hvatningu) — moderate
3. Confidentiality (trúnaðarskylda) — easiest to enforce (+ statutory backstop)

---

## Section 13: EEA / Nordic Comparative Context

### EEA Free Movement

Iceland is an EEA member. Article 28 of the EEA Agreement guarantees free movement of workers.
While non-compete clauses are treated as private contractual matters (not state-imposed barriers),
an overbroad non-compete that effectively prevents cross-border employment within the EEA could
be challenged on free movement grounds. No EFTA Court decision has directly addressed this
intersection, but the principle supports strict scrutiny of non-competes that extend beyond
Iceland's borders.

### Iceland's Position Among the Nordics

Iceland is the **least regulated** Nordic country for non-competes:

- No mandatory compensation (Norway, Denmark, Finland, and Sweden's CBAs all require it)
- No statutory maximum duration (Norway: 12 months; Denmark: 12 months; Finland: 12 months)
- No mandatory written form requirement (though standard practice)
- No advance notice requirement

This makes Iceland more employer-flexible but also means enforceability is **more uncertain** —
courts have wide discretion under the general Section 37 framework, and the absence of clear
statutory rules means outcomes are less predictable.

**Trend risk:** All other Nordic countries have moved toward mandatory compensation and
statutory duration caps. Iceland may follow. The 2026 EEA landscape includes no pending
EU directive on non-competes, but domestic reform pressure may emerge.

---

## Section 14: Glass Box Audit Trail

Every non-compete enforceability output MUST include a Glass Box section:

```yaml
glass_box:
  skill_name: "legalcode-non-compete-analysis-is"
  analysis_date: "[ISO date]"
  jurisdiction: "Iceland"
  governing_law: "Lög nr. 7/1936, 37. gr. (Contracts Act, Section 37)"
  context_type: "[employment / business sale / shareholder agreement / other]"
  section_37_3_applicable: "[yes — employment context / no — business sale or other]"
  section_37_3_triggered: "[yes — void (dismissed without cause or constructive dismissal) / no / not applicable]"
  termination_scenario: "[voluntary resignation / dismissal without cause / dismissal for cause / constructive dismissal / still employed / N/A]"
  employee_role: "[description]"
  industry: "[sector]"
  duration_extracted: "[X months / years]"
  geographic_scope_extracted: "[description]"
  activity_scope_extracted: "[description]"
  compensation_during_restriction: "[none / salary continuation / lump sum / enhanced salary / describe]"
  contractual_penalty: "[amount / formula / absent]"
  prong_1_necessity: "[met / failed — restriction broader than necessary]"
  prong_2_reasonableness: "[met / failed — unreasonable restriction on atvinnufrelsi]"
  section_37_2_balancing: "[employer interest HIGH / MODERATE / LOW — outweighs / does not outweigh restriction burden]"
  section_36_applicable: "[yes — unconscionable terms / no]"
  trade_secret_statutory_protection: "Lög nr. 57/2005 — 3-year statutory duty applies regardless of non-compete enforceability"
  iceland_small_market_factor: "[significant — limited alternatives / moderate / not applicable]"
  nordic_cross_border: "[yes — multi-jurisdiction analysis needed / no — Iceland only]"
  classification: "[GREEN / YELLOW / RED / VOID]"
  confidence_score: "[0.0–1.0]"
  confidence_level: "[Definite / High / Probable / Possible / Unlikely]"
  self_interrogation_applied: "[yes — passed / yes — revised / not applicable]"
  key_case_law: "Hæstiréttur 124/2003 (non-compete enforced; 2-year, 4 named companies; ISK 900,000 penalty)"
  legalcode_mcp: "[Connected — citations verified / Not connected — citations marked VERIFY]"
  redlines_generated: "[yes — N redlines / no]"
  limitations:
    - "Icelandic non-compete case law is limited; Section 37 framework provides wide judicial discretion"
    - "Compensation is not mandatory but absence significantly weakens enforceability"
    - "Small market factor must be assessed case-by-case — no bright-line rule"
    - "Section 37(3) voidance depends on factual determination of 'adequate cause' for dismissal"
    - "[Additional analysis-specific limitations]"
  reviewer: "AI-assisted — requires review by qualified Icelandic lawyer (lögfræðingur / lögmaður)"
```

---

## Section 15: Citation Quality Gates

| Gate           | Rule                                                                                                                                       | Fail Action                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| **Source**     | Every determination cites a specific Icelandic statute (with section number) or Hæstiréttur / Landsréttur case (with case number and year) | Add citation or mark "[VERIFY]"                                 |
| **Format**     | Icelandic statutes cited as "Lög nr. [X/year], [section]. gr."; cases as "Hæstiréttur [nr./year]" or "Landsréttur [nr./year]"              | Standardise format                                              |
| **Currency**   | Statute verified against current text at althingi.is; case law checked for subsequent override                                             | Flag "[VERIFY CURRENCY]" if uncertain                           |
| **Domain**     | Analysis applies Icelandic law only unless explicitly comparing with Nordic peers                                                          | Remove jurisdictional bleed; clearly label comparative analysis |
| **Confidence** | Every determination includes confidence score (0.0–1.0)                                                                                    | Add confidence level before delivering                          |
| **Language**   | Icelandic legal terms preserved alongside English translations on first use                                                                | Add Icelandic term if missing                                   |

---

## Section 16: Self-Interrogation for RED Classifications

For any non-compete clause classified as RED, apply this three-pass review:

**Pass 1 — Statutory Clarity:** Is the RED classification grounded in clear statutory provision
(e.g., 37(3) automatic voidance) or in the general reasonableness analysis? If based on
reasonableness, is there Icelandic case law supporting the assessment? Would the classification
differ if the restriction were narrower (e.g., named competitors instead of industry-wide)?

**Pass 2 — Completeness:** Have all elements of the Section 37(1)-(2) analysis been applied?
Has the 37(2) balancing test given adequate weight to the employer's interest? Is there any
factor (compensation, narrow scope, short duration) that might tip the balance? Could Section 36
(general fairness) provide an alternative basis for the classification?

**Pass 3 — Realistic Enforcement:** What is the employer's strongest argument? Under what
factual scenario might an Icelandic court enforce this clause? Would the court adjust the
clause under Section 36 rather than void it entirely? What is the realistic litigation
environment — Icelandic non-compete litigation is rare, and court outcomes are hard to predict
with the limited case law available.

**Revise RED to YELLOW** if any pass reveals: (a) the overreach could be cured by narrowing
(Icelandic courts may have power to modify under Section 36); (b) the employer's interest
under 37(2) is unusually strong; (c) compensation supports a borderline case. **Retain RED**
if all three passes confirm the clause likely fails both prongs. Document the result in the
Glass Box.

---

## Section 17: Confidence Scoring — Iceland-Specific Calibration

| Level        | Range     | Meaning                                         | When to Apply                                                                                                    |
| ------------ | --------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Definite** | 0.90–1.0  | Clear statutory rule; no ambiguity              | Section 37(3) voidance (dismissed without cause); statutory trade secret protection under Lög 57/2005            |
| **High**     | 0.75–0.89 | Strong statutory + limited case law support     | Narrowly scoped restriction (named competitors, ≤12 months, with compensation) in line with Hæstiréttur 124/2003 |
| **Probable** | 0.55–0.74 | Reasonable arguments; outcome uncertain         | Moderately scoped restriction; some enforceability weaknesses but not fatal                                      |
| **Possible** | 0.35–0.54 | Genuinely uncertain; limited Icelandic case law | Broader restrictions without compensation; court outcome unpredictable                                           |
| **Unlikely** | 0.0–0.34  | Weak enforceability basis                       | Overbroad scope, no compensation, no clear protectable interest                                                  |

**Critical calibration note:** Icelandic non-compete case law is **sparse** compared to the US,
UK, or Germany. The limited body of precedent means that confidence scores should be
**conservatively calibrated**. Even well-structured restrictions carry more uncertainty than
in jurisdictions with extensive case law. **No reasonableness-based determination should
exceed High (0.75–0.89)** without verified Icelandic case law directly on point.

---

## Section 18: Anti-Patterns

**What NOT to do when analysing Icelandic non-compete enforceability:**

1. **Assuming Nordic uniformity.** Iceland, Norway, Denmark, Sweden, and Finland share
   legislative heritage but have diverged significantly on non-competes. Norway mandates
   100% salary compensation; Iceland mandates nothing. Applying Norwegian rules to an
   Icelandic non-compete is wrong.

2. **Ignoring Section 37(3) automatic voidance.** Before spending time on scope and
   reasonableness analysis, check the termination scenario. If the employee was dismissed
   without cause, the clause is void — full stop.

3. **Treating "no mandatory compensation" as "compensation doesn't matter."** While Iceland
   does not legally require compensation during the restriction period, the absence of
   compensation weighs heavily against enforceability in the Section 37(1)-(2) reasonableness
   test. An uncompensated restriction is much harder to enforce.

4. **Ignoring Iceland's small market.** A restriction that would be reasonable in Germany
   (83 million people) or the UK (67 million) may be unreasonably restrictive in Iceland
   (~380,000 people). Always assess the restriction against the actual number of alternative
   employers available to the employee.

5. **Applying US state-by-state analysis to Iceland.** Iceland has a single, unified legal
   framework under Lög nr. 7/1936. There are no regional variations, income thresholds,
   or ban states. The US patchwork approach does not apply.

6. **Overlooking the statutory trade secret backstop.** Even when a non-compete is void,
   Lög nr. 57/2005 provides 3-year statutory protection for professional secrets. Always note
   this as the fallback enforcement mechanism.

7. **Conflating employment and business-sale non-competes.** Section 37(3) applies only to
   employees. Business-sale restrictions face the general 37(1)-(2) test with greater judicial
   deference. Applying the stricter employee standard to a business sale is wrong; applying
   the looser business-sale standard to an employee is also wrong.

8. **Over-relying on Hæstiréttur 124/2003.** This is the leading case, but it is a single
   data point from 2003. The two-year, four-named-companies restriction upheld there was
   unusually narrow. Using it to support a broader restriction is a stretch.

9. **Treating Section 36 (general fairness) as interchangeable with Section 37.** Section 36
   is a supplementary ground; Section 37 is the specific non-compete provision. Start with
   Section 37. Only invoke Section 36 for circumstances not covered by Section 37 (e.g.,
   unconscionable penalty amounts, changed circumstances after signing).

10. **Asserting high confidence in reasonableness determinations.** Icelandic non-compete
    case law is limited. Courts have wide discretion under the open-textured Section 37
    framework. Confidence should be conservatively calibrated — acknowledge the uncertainty
    rather than projecting false precision.

11. **Failing to note the EEA free-movement dimension.** For restrictions that extend beyond
    Iceland's borders, note the potential tension with EEA Article 28 (free movement of workers),
    even though no EFTA Court decision has directly addressed this.

12. **Neglecting to advise on the contractual penalty clause.** Icelandic non-competes
    frequently include samningsbætur (contractual penalties). If the clause includes one,
    analyse its proportionality. If it doesn't, note that the employer would need to prove
    actual damages — which is harder.

---

## Section 19: Writing Standards

1. **Clarity**: State findings in plain language. Provide Icelandic legal terms alongside
   English translations on first use: "samkeppnisákvæði (non-compete clause)."

2. **Specificity**: Cite "Lög nr. 7/1936, 37. gr., 3. mgr." — not "Icelandic contract law."
   Cite "Hæstiréttur 124/2003" — not "Icelandic case law."

3. **[VERIFY] markers**: Every citation whose currency or accuracy is uncertain carries
   a "[VERIFY]" marker. Given the sparse Icelandic case law, be liberal with these.

4. **Confidence attribution**: Every determination carries its confidence score inline.

5. **Dual-framing**: For employers, frame findings as enforceability risks and remediation.
   For employees, frame as defences and voidability arguments.

6. **No gratuitous legalese**: Avoid unexplained Latin or Icelandic legal jargon. Define
   terms on first use.

7. **Nordic comparative notes**: Where Icelandic law is unusual among the Nordics (no
   mandatory compensation, no statutory duration cap), note the comparison to help
   multi-jurisdiction clients understand Iceland's position.

---

## Section 20: Output Format Template

```markdown
# Non-Compete Enforceability Analysis — Iceland (samkeppnisákvæði)

**Date:** [ISO date]
**Context:** [Employment / Business sale / Other]
**Industry:** [Sector]

---

## ⟁ Initial Screening — Section 37(3) Automatic Voidance

| Check                   | Result                                                              |
| ----------------------- | ------------------------------------------------------------------- |
| Context type            | [Employment — 37(3) applies / Business sale — 37(3) not applicable] |
| Termination scenario    | [Description]                                                       |
| Section 37(3) triggered | [⛔ YES — VOID / ✅ No — proceed to full analysis]                  |

---

## Clause Terms Extracted

| Element                    | Value                |
| -------------------------- | -------------------- |
| Duration                   | [X months / years]   |
| Geographic scope           | [Description]        |
| Activity scope             | [Description]        |
| Compensation               | [Description / None] |
| Contractual penalty        | [Amount / Absent]    |
| Legitimate interest stated | [Description / None] |

---

## Two-Prong Analysis — Lög nr. 7/1936, 37. gr.

### Prong 1: Necessity (víðtækari en nauðsynlegt?)

[Analysis of whether restriction goes beyond what is necessary to prevent competition]
**Assessment:** [Met / Failed — specify dimension]
**Confidence:** [Score + level]

### Prong 2: Unreasonable Restriction on Freedom of Employment (ósanngjörn skerðing?)

[Analysis of reasonableness, including Section 37(2) balancing of employer's interest]
**Iceland small-market factor:** [Impact assessment]
**Assessment:** [Met / Failed — specify dimension]
**Confidence:** [Score + level]

---

## Compensation Assessment

[Analysis of compensation arrangements and effect on enforceability]

---

## Contractual Penalty Assessment (samningsbætur)

[Analysis of penalty clause proportionality — if present]

---

## Enforceability Classification

|                            |                                                    |
| -------------------------- | -------------------------------------------------- |
| **Overall classification** | [🟢 GREEN / 🟡 YELLOW / 🔴 RED / ⛔ VOID]          |
| **Confidence score**       | [0.0–1.0]                                          |
| **Confidence level**       | [Definite / High / Probable / Possible / Unlikely] |
| **Rationale**              | [1-2 sentence explanation]                         |

---

## Recommended Modifications

| Priority | Modification  | Rationale |
| -------- | ------------- | --------- |
| Tier 1   | [Must fix]    | [Reason]  |
| Tier 2   | [Should fix]  | [Reason]  |
| Tier 3   | [Recommended] | [Reason]  |

---

## Trade Secret Fallback — Lög nr. 57/2005

[Note on statutory 3-year trade secret protection regardless of non-compete enforceability]

---

## Glass Box Audit Trail

[YAML block — see Section 14]
```

---

## Provenance

| Source                                                                                               | Type                                    | Usage                                                                     |
| ---------------------------------------------------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------- |
| Lög nr. 7/1936, 37. gr. (Contracts Act)                                                              | Primary legislation                     | Core enforceability framework                                             |
| Lög nr. 7/1936, 36. gr. (General fairness)                                                           | Primary legislation                     | Supplementary ground for challenge                                        |
| Lög nr. 57/2005 (Commercial Practices Act)                                                           | Primary legislation                     | Statutory trade secret protection (3 years)                               |
| Hæstiréttur Íslands, mál nr. 124/2003                                                                | Case law                                | Leading non-compete case — 2-year, 4 named companies, ISK 900,000 penalty |
| Official English translation of Lög nr. 7/1936                                                       | Government translation                  | English text of statutory provisions                                      |
| Unnur Hólmfríður Brjansdóttir, "Samkeppnisákvæði og samningafrelsið: Um 37. gr. samningalaga" (2013) | Academic thesis (University of Iceland) | Comprehensive academic treatment of Section 37                            |
| Lög nr. 55/1980 (Collective Agreement Act)                                                           | Primary legislation                     | Collective agreement framework context                                    |
| Lög nr. 19/1979 (Notice Period Act)                                                                  | Primary legislation                     | Termination and notice period context                                     |
| `legalcode-non-compete-enforceability`                                                               | Legalcode reference skill               | Structural template and quality framework                                 |
| Nordic contract law comparative literature                                                           | Comparative analysis                    | Nordic harmonisation context and divergence                               |
| Mayer Brown, "Restrictive Covenants" series (2024)                                                   | Legal commentary                        | Cross-jurisdictional comparison                                           |
| L&E Global, "Restrictive Covenants" country guides                                                   | Legal commentary                        | Nordic and European comparative framework                                 |
| OECD, "Five Facts on Non-Compete and Related Clauses"                                                | Policy research                         | International non-compete policy context                                  |
