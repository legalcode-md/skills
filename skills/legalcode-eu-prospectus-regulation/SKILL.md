---
name: legalcode-eu-prospectus-regulation
description: Guides compliance with the EU Prospectus Regulation (Regulation (EU) 2017/1129, as amended
  by the EU Listing Act Regulation (EU) 2024/2809).
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Guides compliance with the EU Prospectus Regulation (Regulation (EU) 2017/1129, as amended by the EU Listing Act Regulation (EU) 2024/2809). Use when: (1) determining whether a securities offer or admission to trading requires a prospectus (applicability screening); (2) identifying applicable exemptions from the prospectus obligation (Article 1(4)/(5) offer and admission exemptions, including the new 18-month exemption and raised 30% tap exemption from 4 December 2024); (3) selecting the correct prospectus type (standard, base, EU Growth Issuance Prospectus, EU Follow-on Prospectus, Universal Registration Document / shelf registration); (4) advising on the NCA approval process, review timelines (10/20/7/5 working days), and home Member State selection; (5) navigating the EU single passport and NCA notification procedure; (6) assessing supplement obligations (Article 23) and investor withdrawal rights; (7) reviewing prospectus content requirements under Delegated Regulation (EU) 2019/980 including risk factors (Article 16, ESMA31-62-1293 guidelines), summary (Article 7, 7-page limit), financial information requirements, and incorporation by reference; (8) advising on civil liability for prospectus statements (Article 11) and NCA enforcement sanctions (Articles 38-41, maximum €5M or 3% of turnover); (9) guiding EMTN programme approvals, base prospectus annual updates, and Luxembourg/Ireland home state strategies for non-equity debt programmes; (10) implementing EU Listing Act reforms across the three tranches (4 December 2024, 5 March 2026, 5 June 2026). Triggers on: prospectus requirement, prospectus exemption, EU Growth Prospectus, EU Follow-on Prospectus, URD, base prospectus, EMTN programme, IPO prospectus, NCA approval, passporting, supplement, retail cascade, home Member State, BaFin/AMF/CSSF/CBI/AFM/CONSOB/CNMV approval, EU Listing Act, capital markets, securities offering, Eurobond, regulated market, SME Growth Market.


# Legalcode EU Prospectus Regulation

> **Disclaimer**: This skill provides a framework for AI-assisted EU Prospectus Regulation
> compliance assessment. It does not constitute legal advice. All outputs must be reviewed by a
> qualified legal professional — ideally one experienced in EU capital markets law — before
> reliance. The EU Prospectus Regulation is an actively evolving framework: the EU Listing Act
> (Regulation (EU) 2024/2809) has already introduced Phase 1 changes (4 December 2024), with
> further material changes on 5 March 2026 and 5 June 2026. ESMA implementing technical standards
> and delegated regulations are being adopted in parallel. All statutory references cited from
> memory carry hallucination risk — verify against EUR-Lex, ESMA's Interactive Single Rulebook,
> and the relevant NCA's published guidance before acting on them.

---

## Purpose and Scope

This skill supports the full lifecycle of prospectus analysis under **Regulation (EU) 2017/1129**
(as consolidated and amended by Regulation (EU) 2024/2809).

**Covers:**

- Prospectus obligation screening: is a prospectus required?
- Exemption analysis: all Article 1(4) offer exemptions and Article 1(5) admission exemptions,
  including post-Listing Act changes
- Prospectus type selection: standard, base, EU Growth Issuance, EU Follow-on, URD
- Home Member State determination and NCA selection
- NCA approval process: timelines, submission, comment rounds, clock-stopping
- Content requirements: Delegated Regulation (EU) 2019/980, risk factors, summary, financials
- Supplement obligations (Article 23) and investor withdrawal rights
- EU single passport and notification procedure (Articles 24–27)
- Civil liability (Article 11) and enforcement sanctions (Articles 38–41)
- EU Listing Act reform implementation roadmap (Phases 1–3)
- EMTN programme lifecycle: annual base prospectus update, final terms, incorporation by reference
- MAR interaction: inside information, protracted process, market soundings, buy-back programmes

**Does not:**

- Provide legal advice or replace qualified capital markets counsel
- Cover MiFID II product governance (separate regulatory framework)
- Cover prospectus requirements under UK law post-Brexit (UK Prospectus Regulation — separate regime)
- Cover US securities law registration requirements (SEC Form S-1, Form F-1, Rule 144A, Reg S)
- Cover crowdfunding prospectus under Regulation (EU) 2020/1503 (separate regime)
- Address collective investment undertaking (UCITS) disclosure requirements

---

## Jurisdiction and Governing Law

This is an **EU/EEA-specific skill** governing securities offerings and admissions to trading on
regulated markets within the European Economic Area.

**Primary instruments:**
| Instrument | Status |
|-----------|--------|
| Regulation (EU) 2017/1129 (Prospectus Regulation) | In force 20 July 2017; fully applicable 21 July 2019 |
| Regulation (EU) 2024/2809 (EU Listing Act — prospectus amendments) | In force 4 December 2024; further tranches March and June 2026 |
| Commission Delegated Regulation (EU) 2019/980 | Content, format, scrutiny, and approval rules |
| Commission Delegated Regulation (EU) 2019/979 | RTS on key financial info, supplements, advertisements, notification portal |
| ESMA Guidelines on Risk Factors (ESMA31-62-1293) | Effective December 2019; guides NCA review |
| ESMA Q&A on Prospectus Regulation (ESMA31-62-1258) | Interpretive guidance |

**Post-Brexit note**: The UK has its own UK Prospectus Regulation (Retained EU Law) and is undertaking
a comprehensive reform via the Public Offers and Admissions to Trading Regulations 2024. [VERIFY
current UK status.] This skill covers EU/EEA only.

**EEA integration**: The Regulation applies in Norway, Iceland, and Liechtenstein via the EEA
Agreement. EEA NCAs participate in ESMA convergence but are not EU Member States; specific EEA
adaptations apply. [VERIFY current EEA incorporation status.]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming scope,
the workflow pauses and asks when:

- The answer would materially change which analysis path to follow
- Multiple exemptions may apply and the most advantageous must be selected
- The home Member State choice has strategic implications
- The prospectus type decision requires understanding the issuer's capital markets programme

Use the **⟁ CLARIFY** convention wherever marked below. Present structured options with
descriptions. If the user has already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept the Assignment

Accept input in any of these forms:

- A specific question ("Does this offer require a prospectus?")
- A transaction description (IPO, EMTN update, secondary offering, rights issue, bond issuance)
- A draft or approved prospectus for review
- A regulatory question about the Listing Act reform timeline

If the assignment is unclear, proceed to Step 2 to gather context.

### Step 2: Gather Transaction Context

**⟁ CLARIFY** — Collect the following before proceeding. Present as a structured questionnaire:

1. **Transaction type**:
   - Options: Initial Public Offering (IPO), secondary equity offering (rights issue / accelerated
     book build), bond issuance (straight/convertible), EMTN programme (new/annual update), MTN
     tap issuance, admission to trading only, structured product, other
   - _Why this matters_: Determines the triggering obligation (offer to public vs. admission) and
     relevant exemptions.

2. **Issuer profile**:
   - Is the issuer currently listed? If yes, on which venue (regulated market, SME Growth Market, MTF)?
   - How long has the issuer been admitted to trading (specifically: 18+ months is relevant)?
   - Is the issuer an SME (< 250 employees, ≤ €43M balance sheet, ≤ €50M turnover)?
   - _Why this matters_: Determines eligibility for EU Growth Issuance, EU Follow-on, and 18-month
     exemption.

3. **Offer size and investor composition**:
   - Approximate total consideration (in EUR or equivalent)?
   - Will the offer be made to retail investors, or qualified investors only?
   - Approximate number of target investors per Member State?
   - _Why this matters_: Determines whether threshold exemptions or qualified investor exemptions apply.

4. **Geography**:
   - In which EU/EEA Member State(s) will the offer be made?
   - Which exchange(s) is the issuer targeting for admission?
   - Where is the issuer incorporated?
   - _Why this matters_: Determines home Member State, applicable NCA, and passporting needs.

5. **Securities type**:
   - Equity (shares, convertibles, depositary receipts over shares)?
   - Non-equity (bonds, notes, structured products, warrants)?
   - If non-equity: minimum denomination per security?
   - _Why this matters_: Non-equity with denomination ≥ €1,000 allows home Member State choice.

6. **Timeline**:
   - Indicative launch / closing date?
   - Any hard regulatory deadlines (annual update expiry, prospectus validity expiry)?
   - _Why this matters_: Determines NCA review path and whether accelerated procedures are needed.

If the user provides partial context, proceed with stated assumptions and flag them explicitly.

### Step 3: Applicability Screening

Determine whether a prospectus is required at all.

#### 3a. Identify the Triggering Event

**Article 3** establishes two independent triggering events:

| Trigger                                                      | Requirement                                  |
| ------------------------------------------------------------ | -------------------------------------------- |
| **Offer of securities to the public** within the EU          | Prospectus required unless exemption applies |
| **Admission to trading** on a regulated market within the EU | Prospectus required unless exemption applies |

Both triggers are independent: a pure private placement still requires a prospectus if admission to
a regulated market is sought; admission without a new public offer still requires a prospectus.

#### 3b. Check Whether Securities Are In Scope

**Article 1(2)** excludes the following from the entire Regulation:

- Units issued by non-closed-end collective investment undertakings (UCITS)
- Non-equity securities issued by EU/EEA Member States, central banks, regional/local authorities,
  and public international bodies (IMF, World Bank, EIB, etc.)
- Securities unconditionally and irrevocably guaranteed by Member States or public international bodies
- Non-profit organization securities issued to fund non-profit objectives
- Non-fungible shares representing a right to occupy real estate

**Practical note**: Money market instruments with maturity under 12 months are excluded from the
definition of "securities" (Article 2(a) via MiFID II Article 4(1)(44)).

#### 3c. Apply the Threshold

**Article 3(2) — Lower threshold zone**:

- **Below €1,000,000** (total consideration, 12-month rolling): Entirely outside the Regulation.
  No prospectus and no alternative disclosure required under EU law (national rules may apply).
- **€1,000,000 to €8,000,000** (currently; rising to €12,000,000 from **5 June 2026**): Member
  States may exempt these offers from the prospectus obligation. Each Member State sets its own
  threshold; verify the specific Member State's current threshold. [VERIFY current thresholds in
  relevant Member States via ESMA31-62-1193 National Thresholds Document.]
  - Germany: €8M (Securities Information Sheet / WIB required instead)
  - Spain: Planning to stay at €8M [VERIFY]
  - France: Undecided between €12M and €5M [VERIFY]
- **Above €8,000,000** (currently; above €12,000,000 from June 2026): Full Regulation applies,
  unless a specific Article 1(4) or 1(5) exemption applies.

**Aggregation rule**: All offers of the same class of securities from the same issuer over a rolling
12-month period must be aggregated to determine whether the threshold is crossed.

#### 3d. Check Article 1(4) Offer Exemptions

If the total consideration exceeds the threshold, check whether any of the following exemptions
remove the prospectus obligation for the **offer to the public** aspect:

| Exemption                                | Condition                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **(a) Qualified investors only**         | Offer addressed solely to qualified investors (as defined in MiFID II)                                                                                                                                                                                                                                       |
| **(b) Fewer than 150 persons**           | Offer to < 150 natural or legal persons per Member State (excluding qualified investors)                                                                                                                                                                                                                     |
| **(c) Large denomination**               | Securities with minimum denomination of €100,000 per unit                                                                                                                                                                                                                                                    |
| **(d) Large per-investor consideration** | Each investor acquires ≥ €100,000 worth of securities per offer                                                                                                                                                                                                                                              |
| **(da) Tap issue — 30% rule**            | New fungible securities admitted to regulated market or SME Growth Market, representing < 30% of same-class securities admitted over rolling 12 months; requires filing of 11-page Annex IX document (no approval); issuer not in restructuring/insolvency [**Effective 4 December 2024** — raised from 20%] |
| **(db) 18-month continuous admission**   | Fungible securities where original class has been continuously admitted for ≥ 18 months; not connected to takeover/merger/division; issuer not in restructuring/insolvency; 11-page Annex IX document required [**Effective 4 December 2024** — new]                                                         |
| **(e) Substitution shares**              | Shares issued in substitution for shares of same class without capital increase                                                                                                                                                                                                                              |
| **(f) Takeover — exchange offer**        | Securities offered in connection with a takeover by exchange offer (with transaction description document)                                                                                                                                                                                                   |
| **(g) Merger or division**               | Securities offered in connection with a merger or division (with transaction description document)                                                                                                                                                                                                           |
| **(h) Dividend in shares**               | Dividends paid in shares of same class (with information document)                                                                                                                                                                                                                                           |
| **(i) Employee share schemes**           | Securities offered/allotted to existing or former directors or employees by employer or affiliated group company (with information document)                                                                                                                                                                 |
| **(j) Credit institution non-equity**    | Non-subordinated, non-convertible non-equity securities issued by credit institution; aggregate consideration < €150M per institution per rolling 12 months [**Effective 4 December 2024** — raised from €75M]                                                                                               |
| **(k) Crowdfunding**                     | Securities offered via crowdfunding within Regulation (EU) 2020/1503 thresholds                                                                                                                                                                                                                              |

**Combining exemptions**: Multiple Article 1(4) exemptions may be combined (e.g., QI-only + fewer
than 150 persons for non-QI investors).

#### 3e. Check Article 1(5) Admission to Trading Exemptions

If admission to a regulated market is sought, check whether any of the following remove the
prospectus obligation for the **admission** aspect:

| Exemption                                | Condition                                                                                                                                                                                                            |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **(a) Tap issue — 30% rule**             | Fungible securities < 30% of admitted same-class securities over 12 months [**Effective 4 December 2024** — raised from 20%]                                                                                         |
| **(b) Conversion/exchange shares — 30%** | Shares from conversion/exchange < 30% of same-class admitted shares over 12 months [**Effective 4 December 2024** — raised from 20%]                                                                                 |
| **(ba) 18-month continuous admission**   | Fungible securities admitted for admission on regulated market; original class continuously admitted ≥ 18 months; not takeover/merger/division-connected; not in restructuring [**Effective 4 December 2024** — new] |
| **(c) Recovery/resolution**              | Shares resulting from conversion/exchange by resolution authority under bank recovery directives                                                                                                                     |
| **(d) Substitution shares**              | Same class, no capital increase                                                                                                                                                                                      |
| **(e) Takeover exchange offer**          | With transaction description document                                                                                                                                                                                |
| **(f) Merger/division**                  | With transaction description document                                                                                                                                                                                |
| **(g) Free shares/dividends**            | Same class, for existing shareholders                                                                                                                                                                                |
| **(h) Employee schemes**                 | Same class, to directors/employees                                                                                                                                                                                   |
| **(i) Credit institution non-equity**    | < €150M aggregate over 12 months [**Effective 4 December 2024** — raised from €75M]                                                                                                                                  |

**⟁ CLARIFY** — If multiple exemptions appear to apply, identify all applicable exemptions and
present them with a recommendation of which to rely upon (or which to combine), together with any
conditions that must be satisfied and any disclosure obligations that remain (e.g., Annex IX document
for 18-month/30% exemptions).

### Step 4: Determine the Home Member State

The **home Member State** (Article 2(m)) determines which NCA has jurisdiction to approve the
prospectus. This is a critical strategic decision for non-equity issuers.

| Securities Type                                       | Home Member State Rule                                                                                                                                                |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Equity securities — EU issuer**                     | Member State of registered office. No choice.                                                                                                                         |
| **Non-equity with denomination < €1,000 — EU issuer** | Member State of registered office. No choice.                                                                                                                         |
| **Non-equity with denomination ≥ €1,000 — EU issuer** | Issuer's **choice** among: (i) Member State of registered office; (ii) Member State where securities admitted to trading; (iii) Member State where offered to public. |
| **Third-country issuers (non-equity only)**           | Issuer's choice of Member State where first EU offering or admission is sought.                                                                                       |
| **Third-country issuers (equity)**                    | Member State of first EU offer or admission — typically where primary listing sought.                                                                                 |

**Strategic considerations for non-equity issuers** (choosing between Luxembourg and Ireland):

- **Luxembourg (CSSF)**: World's largest venue for international bond/Eurobond listings (LuxSE).
  Highly experienced with EMTN programmes; pragmatic approval process; English accepted; delegated
  publication to LuxSE; e-Prospectus portal (prospectus.help@cssf.lu).
- **Ireland (Central Bank of Ireland)**: Popular for structured products, ABS, certain EMTN
  programmes; common law jurisdiction; English-only; average 15 calendar days processing (2024
  statistics); dedicated prospectus portal; March 2024 Q&A (2nd Edition).
- **Germany (BaFin)**: Required home state for German equity issuers; experienced with bond
  programmes; MVP Portal for submissions; €16,915 approval fee (FinDAGebV).
- **France (AMF)**: Required for French equity issuers; detailed published doctrine; France's
  threshold choice (€12M vs. €5M) pending [VERIFY].
- **Netherlands (AFM)**: Dutch or English accepted; SFTP submission portal; 2025 focus on risk
  factor quality; advance notice requested for European Green Bonds.
- **Italy (CONSOB)**: English permitted even for domestic offerings; pre-filing available for
  significant issuances; Italian summary translation still required.

**⟁ CLARIFY** — For non-equity issuers with denomination ≥ €1,000: Ask whether the issuer has an
existing programme with a designated home state (which should be preserved for programme continuity),
or is making a fresh selection. Changing home state between issuances of the same programme creates
significant complications.

### Step 5: Select the Correct Prospectus Type

Based on the transaction and issuer profile, determine which prospectus type applies.

#### Decision Tree

```
Is the issuer admitted to trading continuously for ≥ 18 months?
├── YES, on regulated market OR SME Growth Market
│   ├── Is the offer/admission within the tap exemption (< 30%, 18-month rule)?
│   │   └── YES → Consider Annex IX document (no prospectus required)
│   ├── Is this a secondary issuance (fungible or new equity)? [From 5 March 2026]
│   │   └── YES → EU Follow-on Prospectus (Art. 14b): 50-page limit, 7-day review
│   └── EMTN / base prospectus programme? → Base Prospectus (Art. 8)
├── NO (first-time issuer / < 18 months listed)
│   ├── Is the issuer an SME / SME Growth Market issuer / offer ≤ €50M?
│   │   ├── YES [until 4 March 2026] → EU Growth Prospectus (Art. 15): current regime
│   │   └── YES [from 5 March 2026] → EU Growth Issuance Prospectus (Art. 15): 75-page limit
│   └── Standard issuer → Standard Prospectus (Art. 6)
└── Is the issuer a frequent issuer on regulated market/MTF?
    └── YES → Universal Registration Document (URD, Art. 9-10) as shelf component
```

#### Prospectus Types Summary

| Type                                      | Authority                  | Review Period                       | Key Features                                                                                 |
| ----------------------------------------- | -------------------------- | ----------------------------------- | -------------------------------------------------------------------------------------------- |
| **Standard Prospectus**                   | Art. 6                     | 10 WD (20 WD for first-time issuer) | Single or three-part document; full content requirements; all issuers                        |
| **Base Prospectus**                       | Art. 8                     | 10 WD (20 WD first-time)            | Non-equity programmes (EMTN, MTN); final terms for each issuance; 12-month validity          |
| **EU Growth Prospectus**                  | Art. 15 (until 4 Mar 2026) | 10 WD (20 WD first-time)            | SMEs, SME Growth Market ≤€500M market cap, others ≤€20M; lighter content                     |
| **EU Growth Issuance Prospectus**         | Art. 15 (from 5 Mar 2026)  | 10 WD                               | SMEs, SME Growth Markets (all), others ≤€50M + <500 employees; 75-page cap                   |
| **EU Follow-on Prospectus**               | Art. 14b (from 5 Mar 2026) | **7 WD**                            | 18+ months listed; secondary issuances; 50-page cap; 1-year financials                       |
| **Universal Registration Document (URD)** | Art. 9-10                  | 10 WD (1st year) then automatic     | Annual shelf registration for frequent issuers; URD + securities note + summary = prospectus |
| **Supplemented Base Prospectus**          | Art. 23                    | 5 WD for supplement                 | Updates to base prospectus during 12-month validity                                          |

**WD = working days.**

**⟁ CLARIFY** — If the issuer is eligible for multiple prospectus types (e.g., both EU Growth
Issuance and EU Follow-on from March 2026), present the options with a comparison of page limits,
review timelines, financial information requirements, and eligibility conditions. Recommend the
type that best matches the issuer's timeline and capital markets programme.

### Step 6: Assess Content Requirements

#### 6a. General Content Standard (Article 6)

Every prospectus must contain information that is:

- **Complete**: All material information investors need to make an informed assessment
- **Consistent**: No internal contradictions between sections
- **Comprehensible**: In easily analysable, concise, and comprehensible form

The standard is: information material to an investor for making an informed assessment of the
assets, liabilities, profits, losses, financial position, and prospects of the issuer and guarantor;
the rights attaching to the securities; and the reasons for the issuance.

#### 6b. Three-Part Structure

| Part                      | Content                                                        | Who Needs It                                                                                     |
| ------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Registration Document** | Issuer: legal, business, financial, governance, ownership      | All prospectuses                                                                                 |
| **Securities Note**       | Specific securities: terms, rights, pricing, use of proceeds   | All prospectuses                                                                                 |
| **Summary**               | Investor-facing overview; max 7 A4 pages; 4 mandatory sections | All prospectuses except: non-equity with denomination ≥ €100K, or exclusively QI-segment trading |

**From 5 June 2026**: Equity prospectuses capped at **300 pages** (excluding summary, incorporated
materials, and complex financial history disclosures); mandatory standardized format and sequence
per Commission delegated acts.

#### 6c. Risk Factors (Article 16 + ESMA Guidelines ESMA31-62-1293)

Risk factors must be:

| Requirement                      | Detail                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Material and issuer-specific** | Generic, disclaimer-only, or industry-wide risks not specific to the issuer are **prohibited** [codified from 4 December 2024] |
| **Categorized by nature**        | Group by type of risk (e.g., risks relating to the issuer, risks relating to the securities, market risks)                     |
| **Ordered within each category** | By decreasing materiality (probability × magnitude assessment)                                                                 |
| **Non-duplicative**              | Avoid repeating risk factors across categories                                                                                 |
| **ESG risks included**           | Environmental, social, and governance risks must be included where material                                                    |

**ESMA 2019 risk factor guidelines** (ESMA31-62-1293) assess: (1) specificity, (2) materiality,
and (3) proportionality of presentation. NCAs focus heavily on risk factors during review — the
AFM in 2025 and most NCAs per ESMA guidelines will return comments on generic risk factors.

**In the summary**: Include only the most material risk factors (market practice: maximum 15).

#### 6d. Financial Information Requirements

| Prospectus Type                   | Historical Financials Required                                                                                                                     |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Standard equity                   | 2 years audited (from 5 June 2026; currently 3 years under legacy Delegated Reg. 2019/980 transitional rules) [VERIFY applicable transition rules] |
| Standard non-equity               | 1 year audited                                                                                                                                     |
| EU Growth Issuance / EU Follow-on | 1 year audited                                                                                                                                     |
| Base prospectus                   | 1 year audited (for standard debt programmes)                                                                                                      |

**Age of financials**: Most recent audited financials must not be more than 16–18 months old at
the prospectus date (depending on whether interim financial information is included). If the
prospectus is published more than 9 months after the financial year-end, interim financials are
typically required.

**Pro forma**: Required where there has been a "significant gross change" (major acquisition or
disposal) since the last audited balance sheet date.

**Working capital statement**: Required in equity prospectuses; must confirm the issuer has (or
does not have) sufficient working capital for at least the next 12 months. NCAs verify consistency
with risk factors, auditor's report, use of proceeds, and disclosed strategy.

#### 6e. Incorporation by Reference (Article 19)

Permitted for: previously approved prospectuses and supplements; annual reports and financial
statements; audit reports; regulated information under Transparency Directive; articles of
association; asset valuations.

**Listing Act update (effective 4 December 2024)**: Base prospectus issuers may incorporate future
financial information published after approval (annual/interim reports) **without requiring a
supplement**, as long as no significant new development is revealed. This significantly simplifies
EMTN programme maintenance.

**Cross-reference requirement**: Where information is incorporated by reference, a cross-reference
list (margin references or a separate cross-reference table) must indicate which part of the
prospectus is replaced by which incorporated document and where in the incorporated document the
relevant information can be found.

### Step 7: Navigate the NCA Approval Process

#### 7a. Submission Timeline

| Issuer Type                                                      | First Draft Review Period                 |
| ---------------------------------------------------------------- | ----------------------------------------- |
| First-time issuer (no prior securities admitted or public offer) | **20 working days** from first submission |
| Existing issuers                                                 | **10 working days** from first submission |
| Frequent issuers (URD, separate documents, 5+ WD advance notice) | **5 working days**                        |
| EU Follow-on Prospectus (from 5 March 2026)                      | **7 working days**                        |
| Supplement                                                       | **5 working days**                        |

**Clock-stopping**: When the NCA sends comments, the clock resets from the date the revised draft
or supplementary information is submitted. Multiple rounds are common (2–4 comment rounds for IPOs).
Each reset triggers a fresh 10-working-day (or 20-working-day for first submissions of first-time
issuers) review period.

**Failure to decide**: NCA failure to decide within the time limit does NOT constitute approval.

#### 7b. Practical Submission Steps

1. **Pre-filing consultation**: Contact the NCA before drafting to agree on the timetable and
   identify potential problem areas. For first-time IPOs, a **pre-consultation meeting 3 months
   before first submission** is strongly recommended. NCAs typically provide problem-area checklists.

2. **Register on the NCA's portal**:
   - BaFin: MVP Portal
   - CSSF: e-Prospectus portal (e-prospectus.support@cssf.lu)
   - AFM: SFTP connection (service.prospectus@afm.nl)
   - CBI: CBI prospectus approval portal
   - CONSOB: electronic filing system

3. **Assemble supporting documents** per Delegated Regulation (EU) 2019/980 Article 42:
   - Cross-reference list (unless margin references used)
   - All historical financial information (audited)
   - Expert valuations (if applicable: mining, real estate, reserves)
   - Pro-forma financial information (if applicable)
   - Directors and officers information
   - Full RTS 2019/979 Annex VII metadata (must be complete by approval date)

4. **Respond to NCA comments**: Each round must be substantively addressed. Unanswered comments
   are escalated in subsequent rounds. Maintain a comment-tracking log (NCA comment / response
   status / reference).

5. **Approval notification**: NCA notifies the issuer of the approval decision in writing.
   The approved prospectus is automatically submitted to ESMA's central storage system.

#### 7c. Publication (Article 21)

Publish the approved prospectus **at least 3 working days** before the offer period closes [reduced
from 6 working days by Listing Act, effective 4 December 2024].

Publication channels:

- Issuer/offeror website
- Financial intermediaries' websites (if applicable)
- Regulated market operator website (where admission sought)
- ESMA central storage (automatic upon NCA approval)

Requirements:

- Free of charge; no registration, login, or fee-gate
- Downloadable and printable
- Hyperlinks remain functional for the **10-year storage period**
- Electronic delivery upon request replaces paper copy obligation [Listing Act, effective 4 December 2024]

**Validity**: 12 months from approval. Both the prospectus and any standalone registration document
or URD have individual 12-month validity periods.

### Step 8: Assess Supplement Obligations

#### 8a. Supplement Trigger (Article 23)

A supplement is required for every:

> "significant new factor, material mistake or material inaccuracy relating to the information
> included in a prospectus which may affect the assessment of the securities"

that arises or is noted between:

- Prospectus approval, AND
- The **later of**: (i) closing of the offer period OR (ii) commencement of trading on a regulated market

The obligation is **ongoing** throughout the offer period and up to listing. "Significant" and
"material" are objective standards; when in doubt, file a supplement.

**Listing Act update (effective 4 December 2024)**: No supplement is required solely because new
annual or interim financial information has been published during a **base prospectus**'s validity
period — that information may be incorporated by reference instead. [Note: This relief is specific
to base prospectuses; equity standard prospectuses may still require supplements for material
financial developments.]

**Supplements cannot introduce a new type of security** into a base prospectus [Listing Act,
effective 4 December 2024; pending ESMA guidance on what constitutes a "new type"].

#### 8b. Supplement Approval

Supplements are approved in **5 working days** via the same NCA process as the original.

#### 8c. Investor Withdrawal Rights

Where a supplement relates to a **public offer** and the triggering event occurred **before the
closing of the offer period or delivery of securities** (whichever is first):

- Investors who already agreed to purchase or subscribe have the right to **withdraw their
  acceptances** within **3 working days** of supplement publication [extended from 2 working days
  by Listing Act, effective 4 December 2024]
- The issuer may extend this withdrawal period
- The supplement must include: a prominent statement specifying withdrawal eligibility, exact
  withdrawal period dates, and contact information for exercising withdrawal

**Financial intermediary obligations**: Notify investors of the supplement by end of the **first
working day** after supplement publication. Investors who refused electronic contact must be warned
to monitor the issuer/offeror website.

**⟁ CLARIFY** — If a material development occurs during the offer period (profit warning, material
litigation development, key customer loss, regulatory decision, auditor qualification), confirm
whether it constitutes a supplement trigger. If uncertain, the conservative approach is to file.
Failure to supplement when required is an enforcement risk.

### Step 9: Navigate the EU Passport

#### 9a. The Single Prospectus Passport (Article 24)

An approved prospectus is valid across the **entire EU/EEA** without re-approval in host Member
States. The home NCA's approval is the single authorization.

#### 9b. Notification Procedure (Article 25)

1. Issuer/offeror requests notification from their home NCA
2. Home NCA issues a **Certificate of Approval (CoA)** and sends it via the **ESMA notification
   portal** to the host NCA(s), together with a copy of the approved prospectus
3. Timing: Notification occurs within **1 working day** of receiving the request (or, where the
   request accompanies the draft prospectus, within 1 working day of approval)

**Final terms** under a base prospectus: Filed with the home NCA and **automatically passported**.
No separate notification procedure required for final terms.

**Registration documents / URDs (Article 26)**: Can be separately passported to host NCAs upon
request, enabling the issuer to draw up only the securities note and summary for subsequent
issuances in other jurisdictions.

#### 9c. Language Requirements (Article 27)

| Document               | Language Rule                                                                                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Full prospectus**    | May be in a language customary in international finance (typically English), if accepted by the home NCA. Host NCAs **cannot** require full translation. |
| **Prospectus summary** | Must be translated into the official language of each **host** Member State (or another language accepted by that host NCA).                             |
| **From 5 June 2026**   | Greater flexibility: prospectuses may be drawn up in English even for purely domestic single-Member-State offerings, unless the Member State opts out.   |

**ESMA language acceptance table** (ESMA32-384-5080): Lists which languages each NCA accepts for
scrutiny and which each host NCA requires for summary translation. Consult this table before
drafting the summary translation programme.

### Step 10: Assess Civil Liability and Enforcement Exposure

#### 10a. Civil Liability (Article 11)

**Who is liable** (Member States must ensure civil liability attaches to):

- The **issuer** (or its administrative, management, or supervisory bodies)
- The **offeror**
- The **person asking for admission** to trading on a regulated market
- The **guarantor** (as applicable)

**Responsible persons** must be identified in the prospectus by name and function (individuals) or
name and registered office (legal persons), with a declaration that to the best of their knowledge
the information is in accordance with the facts.

**Standard of liability**: [JURISDICTION-SPECIFIC] Article 11 sets minimum requirements; civil
liability standards vary significantly by Member State. Most EEA states require at least negligence
(fault-based). No EEA jurisdiction currently imposes strict liability. ESMA published technical
advice on further harmonization in June 2025 (ESMA32-117195963-1413) — consult for current position
and any Commission follow-up action.

**Summary liability** (Article 11(2)): Civil liability does NOT attach solely based on the summary
unless the summary, when read together with the rest of the prospectus, is:

- Misleading, inaccurate, or inconsistent with the other parts; OR
- Fails to provide key information in order to aid investors when considering whether to invest.

#### 10b. Administrative Sanctions and Enforcement (Articles 38–41)

| Subject             | Maximum Sanction                                                                                      |
| ------------------- | ----------------------------------------------------------------------------------------------------- |
| **Legal persons**   | ≥ €5,000,000 OR ≥ 3% of total annual turnover (whichever is higher); Member States may provide higher |
| **Natural persons** | ≥ €700,000; Member States may provide higher                                                          |

**NCA supervisory powers**:

- Request any information and documents; conduct on-site inspections
- Temporarily prohibit or suspend a public offer
- Suspend or require suspension of trading on the securities
- Exclude securities from trading
- Withdraw approval of a prospectus
- Require supplement publication
- Issue public warnings identifying the responsible persons

**Recent enforcement**: ESMA publishes annual aggregate sanctions data across EU NCAs. In 2023,
NCAs issued >970 administrative sanctions with aggregate fines >€71M (across all securities
regulations). Prospectus-specific enforcement focuses on: failure to publish approved prospectus,
failure to supplement, failure to notify investors of withdrawal rights, and misleading risk factors.

### Step 11: EU Listing Act Reform Implementation Roadmap

Present this roadmap to flag which rules are already in force, which are upcoming, and when to
update the issuer's processes.

| Change                                           | Effective Date      | Impact                                   |
| ------------------------------------------------ | ------------------- | ---------------------------------------- |
| 30% tap exemption (raised from 20%)              | **4 December 2024** | More secondary issuances exempt          |
| New 18-month continuous admission exemption      | **4 December 2024** | Unlimited volume exempt (with Annex IX)  |
| Credit institution threshold raised to €150M     | **4 December 2024** | Wider exemption for bank bonds           |
| Investor withdrawal period extended to 3 WD      | **4 December 2024** | Longer withdrawal right                  |
| No supplement for periodic reporting (base only) | **4 December 2024** | Simplifies EMTN maintenance              |
| Electronic delivery replaces paper copy          | **4 December 2024** | Process change                           |
| Minimum IPO offer period: 3 WD (from 6 WD)       | **4 December 2024** | Faster IPO execution                     |
| Risk factors: generic/disclaimer prohibited      | **4 December 2024** | Codifies prior ESMA guidance             |
| URD frequent issuer: 1 year (from 2 years)       | **5 March 2026**    | Faster shelf access                      |
| EU Follow-on Prospectus (Art. 14b)               | **5 March 2026**    | 50-page / 7-WD for listed 18+ months     |
| EU Growth Issuance Prospectus (Art. 15 replaced) | **5 March 2026**    | 75-page / €50M threshold                 |
| Equity prospectus: 300-page cap                  | **5 June 2026**     | Format standardization                   |
| Standardized prospectus format/sequence          | **5 June 2026**     | ESMA technical standards to be consulted |
| €12M harmonized lower threshold                  | **5 June 2026**     | Replaces Member State discretion zone    |
| English for purely domestic offerings            | **5 June 2026**     | Subject to Member State opt-out          |
| Non-equity: 1-year financials (statutory)        | **5 June 2026**     | Reduced burden                           |
| Equity: 2-year financials (statutory)            | **5 June 2026**     | Reduced from 3 years                     |
| ESG/sustainability bond disclosures              | **5 June 2026**     | New obligations for ESG-labelled bonds   |
| MAR protracted process reform                    | **5 June 2026**     | Only final event requires disclosure     |
| MiFID II research rebundling                     | **6 June 2026**     | Bundled execution + research permitted   |

**WD = working days.**

**⟁ CLARIFY** — Ask whether the user wants a transaction-specific reform impact assessment (which
changes affect this specific deal) or a programme-level update review (which changes affect the
issuer's ongoing capital markets programme).

---

## Compliance Classification System

Classify each prospectus compliance element using this four-tier system:

| Status            | Definition                                                     | Action Required                                                                  |
| ----------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **COMPLIANT**     | Fully meets Regulation requirements; no action needed          | Document and confirm                                                             |
| **CONDITIONAL**   | Meets requirements subject to verification or NCA discretion   | Verify specific conditions; obtain NCA confirmation where appropriate            |
| **PARTIAL**       | Partially meets requirements; gaps or ambiguities exist        | Remediate identified gaps; seek legal advice on borderline elements              |
| **NON-COMPLIANT** | Does not meet Regulation requirements; enforcement risk exists | Immediate remediation required; assess whether to file supplement or cease offer |

For exemption determinations:

| Status                   | Definition                                                                         |
| ------------------------ | ---------------------------------------------------------------------------------- |
| **EXEMPT**               | All conditions of the exemption are clearly satisfied                              |
| **CONDITIONALLY EXEMPT** | Exemption appears to apply but requires verification of specific factual condition |
| **NOT EXEMPT**           | Exemption conditions are not satisfied; prospectus required                        |

---

## Severity Classification for Content Deficiencies

When reviewing a prospectus draft for NCA submission or post-approval compliance, classify
deficiencies using this system:

| Severity        | Definition                                                                         | NCA Likelihood | Action                                                |
| --------------- | ---------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------- |
| **CRITICAL**    | Fundamental omission or misstatement; likely prospectus withdrawal or refusal      | Very high      | Mandatory remediation before submission or disclosure |
| **HIGH**        | Material gap or inconsistency; NCA will likely require correction; supplement risk | High           | Remediate before submission                           |
| **MEDIUM**      | Partial gap or unclear disclosure; NCA may request clarification                   | Moderate       | Improve before submission; flag for review            |
| **LOW**         | Minor drafting issue; unlikely to prompt NCA comment                               | Low            | Improve if possible; document rationale               |
| **OBSERVATION** | Best-practice improvement; not a legal deficiency                                  | Very low       | Consider for next update                              |

---

## Actionable Output Per Finding

For each compliance issue identified, provide:

1. **Finding**: What is the issue (specific article, regulation, or ESMA guidance reference)?
2. **Severity**: CRITICAL / HIGH / MEDIUM / LOW / OBSERVATION
3. **Current status**: COMPLIANT / CONDITIONAL / PARTIAL / NON-COMPLIANT
4. **Analysis**: Why does this constitute a deficiency or risk?
5. **Required action**: What specifically must be done to remediate?
6. **Responsible party**: Who needs to act (issuer, issuer's counsel, auditor, NCA, etc.)?
7. **Deadline**: When must this be resolved (pre-submission, pre-launch, pre-closing)?

---

## Prioritization Framework

Prioritize findings across three tiers:

**Tier 1 — Deal-Critical** (address immediately; cannot proceed without resolution):

- Missing prospectus where required (no valid exemption)
- Wrong home Member State selected
- NCA approval not obtained before offer opens
- Financial information missing or materially stale
- CRITICAL-severity content deficiencies

**Tier 2 — Material** (address before submission or launch):

- Incorrect prospectus type selected
- Generic or non-compliant risk factors
- Missing working capital statement
- Missing or defective supplement when required
- HIGH-severity content deficiencies

**Tier 3 — Process Improvements** (address before closing or for next issuance):

- Suboptimal passporting language programme
- Incomplete cross-reference list
- Investor withdrawal notification procedures not documented
- MEDIUM/LOW-severity content deficiencies

---

## Citation Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                             | Fail Action                                  |
| -------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| **Source**     | Every legal claim cites a specific article, delegated regulation, or ESMA guideline                              | Add citation or mark "[UNVERIFIED]"          |
| **Format**     | All citations follow consistent EU legal citation format (e.g., "Art. 1(4)(da), Regulation (EU) 2017/1129")      | Fix format                                   |
| **Currency**   | Every cited provision checked for Listing Act amendments — flag which implementation tranche applies             | Add "[CHECK CURRENCY — Listing Act Phase X]" |
| **Domain**     | Analysis stays within EU/EEA Prospectus Regulation; does not bleed into UK, US, or other non-EU regimes          | Remove or flag out-of-scope content          |
| **Confidence** | Uncertainty explicitly stated; areas of NCA discretion flagged; [VERIFY] used where ESMA/NCA guidance is pending | Add confidence qualifier                     |

---

## Self-Interrogation for NON-COMPLIANT and CRITICAL Items

For any item classified NON-COMPLIANT or CRITICAL, apply this three-pass review:

**Pass 1 — Legal Chain Integrity**: Does the non-compliance finding follow logically from the
cited article and delegated regulation? Would the NCA actually raise this during scrutiny? Is there
an ESMA Q&A or NCA guidance that addresses this point?

**Pass 2 — Completeness**: Have all applicable exemptions been checked? Is there an alternative
prospectus type that would address the issue? Has the Listing Act tranche-by-tranche timeline been
applied correctly (some relief measures may already be in force; others are future-dated)?

**Pass 3 — Challenge**: What is the strongest argument that the issuer is not non-compliant?
Under what interpretation of the Regulation or ESMA guidance might the current approach be
defensible? If defensible, what is the enforcement risk?

---

## Confidence Scoring

| Level        | Range     | Meaning                                                      | Action                                           |
| ------------ | --------- | ------------------------------------------------------------ | ------------------------------------------------ |
| **Definite** | 0.95–1.0  | Settled Regulation text; clear NCA practice                  | State with confidence                            |
| **High**     | 0.80–0.94 | Strong authority; minor questions or NCA variation           | State with brief caveat                          |
| **Probable** | 0.60–0.79 | Good arguments; NCA practice may vary; ESMA guidance pending | State with reasoning and contra-indicators       |
| **Possible** | 0.40–0.59 | Genuinely uncertain; NCA discretion significant              | Flag for specialist legal advice with both sides |
| **Unlikely** | 0.0–0.39  | Weak basis; ESMA guidance contradicts                        | Do not assert; flag "[UNCERTAIN — do not rely]"  |

**Areas of particular uncertainty** where lower confidence scores apply:

- Interpretation of "significant new factor" for supplement purposes
- Whether a development constitutes a "new type of security" in a supplement to a base prospectus
- NCA-specific procedural preferences (varies by NCA; verify with local counsel)
- Civil liability standards (entirely governed by Member State law; [JURISDICTION-SPECIFIC])
- Whether specific ESG risks are "material" in any given prospectus
- Listing Act areas pending ESMA technical standards (standardized format, EU Growth Issuance
  content requirements, EU Follow-on content requirements)

---

## Glass Box Audit Trail

Include this YAML block at the end of every prospectus compliance assessment:

```yaml
glass_box:
  skill_name: "legalcode-eu-prospectus-regulation"
  mode: "Prospectus compliance assessment"
  date: "[YYYY-MM-DD]"
  transaction:
    type: "[IPO / EMTN update / secondary offering / etc.]"
    issuer: "[Name or anonymous description]"
    securities: "[Equity / Non-equity / Base programme]"
    home_member_state: "[Germany (BaFin) / Luxembourg (CSSF) / Ireland (CBI) / etc.]"
    total_consideration: "[EUR X million]"
    target_jurisdictions: "[List of Member States]"
  regulation_version: "Regulation (EU) 2017/1129 as amended by Regulation (EU) 2024/2809"
  listing_act_tranches_applied:
    phase_1_4_dec_2024: "[Applied / Not yet applicable]"
    phase_2_5_mar_2026: "[Applied / Not yet applicable — effective 5 March 2026]"
    phase_3_5_jun_2026: "[Applied / Not yet applicable — effective 5 June 2026]"
  legalcode_mcp: "Connected / Not connected — [note]"
  research_reference_file: "[path or 'Not created']"
  prospectus_required: "YES / NO / CONDITIONAL — [basis]"
  exemptions_identified: "[List of Article 1(4)/(5) exemptions checked]"
  prospectus_type_recommended: "[Type]"
  home_nca: "[NCA name]"
  approval_timeline: "[X working days]"
  passport_jurisdictions: "[List]"
  supplement_risk: "LOW / MEDIUM / HIGH — [rationale]"
  findings_summary:
    critical: "[N]"
    high: "[N]"
    medium: "[N]"
    low: "[N]"
  citations_verified: "[N VERIFIED] / [N UNVERIFIED]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, areas requiring specialist legal advice, pending ESMA guidance]"
  reviewer: "AI-assisted — requires qualified EU capital markets legal review"
```

---

## Anti-Patterns

These are the most common errors in EU Prospectus Regulation compliance. Flag any that are present
in the transaction under review.

1. **Failing to exhaust exemptions before deciding a prospectus is required**: Do not assume a
   prospectus is needed before checking all Article 1(4) offer exemptions and Article 1(5)
   admission exemptions. The 18-month exemption (effective 4 December 2024) is frequently
   overlooked for frequently issuing listed companies.

2. **Miscalculating the consideration threshold**: The €8M (or current Member State threshold)
   is calculated on a **rolling 12-month** basis aggregating all offers of the same class from the
   same issuer — not a calendar year. Failing to aggregate across multiple tranches, intermediary-
   offered securities, or employee benefit plans can create unintended obligation.

3. **Wrong home Member State for debt programmes**: For non-equity securities with denomination
   ≥ €1,000, EU issuers have a home state choice. Defaulting to the registered office without
   considering Luxembourg or Ireland for Eurobond/EMTN programmes misses significant advantages in
   processing speed, market practice familiarity, and programme flexibility.

4. **Changing home Member State mid-programme**: Switching NCA between issuances under the same
   EMTN programme creates complex grandfathering issues, inconsistent disclosure obligations, and
   potential investor confusion. The home state choice should be made once and maintained.

5. **Missing the supplement obligation during offer period**: The obligation to supplement arises
   from "significant new factor, material mistake or material inaccuracy" — a broad standard.
   Issuers frequently miss supplement triggers from: profit warnings, analyst guidance updates,
   loss of a material contract, regulatory investigation commencement, or key person departure.
   When in doubt, supplement.

6. **Publishing supplement after offer closes without investor notification**: A supplement
   published after the offer closes does not trigger the 3-day withdrawal right — but it does not
   eliminate the enforcement risk if the NCA concludes the supplement should have been published
   earlier. Timing is critical.

7. **Using EU Growth Prospectus/Growth Issuance for companies already on a regulated market**:
   These simplified regimes are **expressly unavailable** to issuers already admitted to a regulated
   market (to avoid two-tier disclosure). A company on Euronext Paris cannot use the EU Growth
   Issuance Prospectus. Use EU Follow-on Prospectus (from March 2026) instead.

8. **Risk factors that are generic, industry-wide, or disclaimer-only**: Post-ESMA 2019 guidelines
   and now codified by the Listing Act (effective 4 December 2024), generic risk factors are
   prohibited. Each risk factor must be specific to the issuer and the securities, and ordered
   within its category by decreasing materiality. NCA comment rounds most commonly focus on risk
   factor specificity.

9. **Stale financial information in the prospectus**: Historical financials more than 16–18 months
   old (depending on whether interim financials are included) will be rejected by NCAs. For issuers
   with February/March/April year-ends, this creates a tight window for late-calendar-year deals.
   Plan the financial information cut-off early.

10. **Missing the cross-reference list or table for incorporated-by-reference information**:
    Where documents are incorporated by reference, a cross-reference list or margin annotations are
    mandatory. An NCA cannot approve a prospectus that incorporates documents by reference without
    a reader-navigable reference structure.

11. **Assuming incorporation by reference for base prospectuses eliminates supplement obligations
    entirely**: The Listing Act relieved base prospectus issuers from supplementing for new periodic
    financial information only — not for significant new developments, material mistakes, or
    inaccuracies. The supplement obligation remains for substantive developments.

12. **Neglecting the summary translation programme for multi-jurisdiction passport**: The full
    prospectus need not be translated (English is typically accepted by home NCAs), but the
    **summary must be translated** into the official language of each host Member State where the
    prospectus is used for a public offer. Failure to translate the summary for, e.g., an offer in
    Germany when prospectus is Luxembourg-approved (summary in English only) is a compliance breach.

13. **Passporting delays leaving offers technically unopened in host states**: The notification to
    host NCAs must occur before the offer opens in that host state. A 1-working-day NCA processing
    time means the request must be submitted at least 1 working day before launch in each host
    state. Coordinating multiple host state launches requires careful timetabling.

14. **Failing to notify investors of their withdrawal right after a supplement**: After a supplement
    is published, investors who have already subscribed must be notified of their withdrawal right
    within the first working day. Financial intermediaries in a retail cascade must also notify
    their clients. Failures here carry direct regulatory risk.

15. **Using the wrong URD filing approach for the securities note**: Once an issuer has frequent
    issuer status (after 1 year of URD approvals, from 5 March 2026), the issuer can file URDs
    without prior approval — but the securities note and summary still require NCA approval. An
    unapproved URD + unapproved securities note = no valid prospectus.

16. **Ignoring the Listing Act phased application and applying pre-Listing-Act rules**: The Listing
    Act amendments are applied in three tranches. Advisers still working with pre-4-December-2024
    checklists risk advising on outdated exemption thresholds (30% tap / 18-month exemption /
    €150M credit institution threshold) and outdated investor withdrawal rights (3 vs. 2 days).
    Update template documentation immediately.

17. **Failing to assess ESG/sustainability risk factors as material**: For issuers with significant
    climate, biodiversity, or social risks, ESG risks may be among the most material risk factors
    in the prospectus. Omitting or downplaying them exposes issuers to regulatory scrutiny and
    investor claims. From June 2026, ESG/sustainability bond disclosures become mandatory for
    ESG-labelled securities.

18. **Forward-looking statements without adequate issuer-specific disclaimers**: The EU lacks a
    statutory safe harbour equivalent to the US PSLRA. Risk factors must specifically address the
    risks that forward-looking statements will not materialize, and forward-looking statements must
    be clearly identified with issuer-specific caveats.

19. **Commencing bookbuilding before NCA approval**: The prospectus must be approved by the NCA
    and published before the formal offer period opens. Pre-deal investor education (pilot fishing,
    investor testing) is permissible, but formal marketing or order-taking before approval is a
    regulatory violation. Distinguish carefully between permissible testing activity and prohibited
    pre-marketing offers.

20. **Overlooking home Member State advertising rules (Article 22)**: Advertisements relating to
    a public offer must comply with Article 22: they must be identifiable as advertisements, must
    not be misleading or inaccurate, and must be consistent with the prospectus. Advertisements
    published before the approved prospectus must include a statement that a prospectus has been
    or will be published and where investors can obtain it.

---

## Writing Standards

Before delivering any compliance assessment or prospectus review output:

- **Precision over vagueness**: Every finding must cite a specific article, paragraph, or ESMA
  guideline. Findings without legal authority are observations only, not compliance assessments.
- **Active voice**: "Article 23 requires a supplement" not "a supplement is required by Article 23."
- **Separate law from practice**: Distinguish between what the Regulation requires (law) and what
  NCAs commonly request or prefer (practice). Label each clearly.
- **No false certainty**: Where NCA practice varies or Listing Act implementation guidance is
  pending, state this explicitly. Use confidence qualifiers.
- **Jurisdiction-specific items marked**: Any item that varies by Member State must be marked
  [JURISDICTION-SPECIFIC] and must not be stated as a universal EU rule.
- **Unverified references marked**: Any legal reference not confirmed against EUR-Lex or ESMA
  sources must carry [VERIFY].
- **Plain language**: Define legal terms on first use. Avoid unexplained jargon. The output should
  be usable by a non-specialist senior manager who needs to understand the key risks and required
  actions.

**Quality gate before delivery**: Does every CRITICAL and HIGH finding have a specific remediation
action, a responsible party, and a deadline? If any finding lacks these three elements, add them
before delivering.

---

## External Tool Integration

**With legalcode-mcp connected (preferred)**:

- In Step 3 (applicability screening) and Step 6 (content review), use legalcode-mcp to verify
  current Regulation text (consolidated version as amended by the Listing Act)
- Search for the specific article and paragraph being relied upon
- Verify current ESMA Q&A position on the point at issue
- Check NCA-published guidance for the home Member State's procedural requirements
- Check EUR-Lex for the current consolidated text of Delegated Regulation (EU) 2019/980 (Annexes
  are extensive; retrieve only the relevant Annex for the prospectus type)
- Save the most relevant results to `/tmp/legalcode-prospectus-research.md`
- Mark all legalcode-mcp sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp**:

- Proceed using the legal research embedded in this skill
- Mark all statutory and ESMA references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — verify all citations against EUR-Lex"`
- Recommend the user verify against:
  - EUR-Lex consolidated Regulation (EU) 2017/1129: eur-lex.europa.eu
  - ESMA Interactive Single Rulebook (Prospectus): esma.europa.eu
  - Relevant NCA published guidance (BaFin, AMF, CSSF, CBI, AFM, CONSOB, CNMV websites)
  - ESMA Q&A document (ESMA31-62-1258) for interpretive issues

---

## Localization Notes

### Home NCA Procedural Variations [JURISDICTION-SPECIFIC]

Verify current NCA-specific procedures before each submission. Key procedural differences:

| NCA                             | Notable Characteristics                                                                                                                                                                          |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **BaFin (Germany)**             | MVP Portal; German summary for domestic offerings; Securities Information Sheet (WIB, max 3 pages) for sub-€12M offers [from June 2026]; approval fee ~€16,915; pre-IPO consultation recommended |
| **AMF (France)**                | Detailed published doctrine; French summary for domestic offerings; France threshold choice (€12M vs €5M) pending [VERIFY]; multiple-vote shares permitted (Law 2024-537)                        |
| **CSSF (Luxembourg)**           | e-Prospectus portal; English accepted; delegated publication to LuxSE; popular for Eurobond/EMTN; pragmatic and experienced; prospectus.help@cssf.lu                                             |
| **CBI (Ireland)**               | CBI prospectus portal; English only; average 15 calendar days (2024); March 2024 Q&A (2nd Edition); popular for structured products and certain EMTN programmes                                  |
| **AFM (Netherlands)**           | SFTP submission; Dutch or English; advance notice requested for EuGB; 2025 focus on risk factor quality and AI risk disclosure                                                                   |
| **CONSOB (Italy)**              | English permitted for domestic offerings; Italian summary mandatory for offers in Italy; pre-filing available for significant issuances; simplified procedures since 2022 reform                 |
| **CNMV (Spain)**                | Planning to maintain €8M threshold [VERIFY]; Spanish summary required; standard EU review timelines                                                                                              |
| **Finansinspektionen (Sweden)** | Standard EU review timelines; Swedish or English accepted; consult fi.se for current procedural requirements                                                                                     |

### Civil Liability — Member State Variations [JURISDICTION-SPECIFIC]

Civil liability under Article 11 is implemented differently in each Member State. Key variations:

- **Standard of fault**: Most require negligence minimum; some require intent for specific claims
- **Burden of proof**: Some shift burden once statutory breach is established
- **Limitation periods**: Range widely (typically 3–10 years from discovery or end of offer)
- **Eligible claimants**: Purchaser during offer vs. any holder varies
- **Class actions / collective actions**: Availability varies significantly

For any liability assessment, **local counsel in the relevant Member State must be engaged**.
This skill does not substitute for jurisdiction-specific civil liability advice.

### Post-Brexit UK [JURISDICTION-SPECIFIC]

The UK operates under its own UK Prospectus Regulation (Retained EU Law as modified). The UK's
Public Offers and Admissions to Trading Regulations 2024 introduced significant further changes.
UK and EU requirements are **not equivalent** post-Brexit; separate analysis is required. If a
transaction involves both the UK and EU, obtain separate UK and EU legal advice.

---

## Output Format Template

Deliver the prospectus compliance assessment in this structure:

```markdown
# EU Prospectus Regulation Assessment

**Transaction**: [Type and brief description]
**Issuer**: [Name or anonymous description]
**Date of assessment**: [YYYY-MM-DD]
**Skill version**: legalcode-eu-prospectus-regulation (Reg. (EU) 2017/1129 as amended by Reg. (EU) 2024/2809)

---

## Executive Summary

[3–5 bullet points covering: (1) prospectus required or exempt; (2) recommended prospectus type;
(3) home NCA recommended; (4) most critical compliance issues; (5) key Listing Act changes
applicable to this transaction]

---

## 1. Applicability Screening

**Triggering events present**: [Yes — offer to public / admission to trading / both]
**Total consideration**: [EUR X million over 12 months]
**Threshold applicable**: [€8M / €12M / Member State threshold]
**Prospectus required**: [YES / NO / CONDITIONAL]

### Exemptions Assessed

| Exemption                  | Article       | Status              | Conditions          |
| -------------------------- | ------------- | ------------------- | ------------------- |
| [e.g., 30% tap issue]      | Art. 1(4)(da) | EXEMPT / NOT EXEMPT | [If conditions met] |
| [18-month exemption]       | Art. 1(4)(db) | EXEMPT / NOT EXEMPT | [Annex IX required] |
| [Qualified investors only] | Art. 1(4)(a)  | EXEMPT / NOT EXEMPT |                     |

**Conclusion**: [Prospectus required / Not required / Exemption applies — describe]

---

## 2. Home Member State and NCA

**Securities type**: [Equity / Non-equity ≥ €1,000 / Non-equity < €1,000]
**Home Member State options**: [If choice available, list options]
**Recommended home Member State**: [Name — rationale]
**Competent NCA**: [Name and contact]
**NCA review timeline**: [X working days]
**Pre-filing consultation recommended**: [Yes/No — timing]

---

## 3. Prospectus Type Recommendation

**Recommended type**: [Standard / Base / EU Growth Issuance / EU Follow-on / URD + securities note]
**Rationale**: [Why this type is most appropriate]
**Eligibility conditions**: [Confirm each eligibility condition is met]
**Page limits**: [Applicable page caps]
**Financial information required**: [X years audited + any interim]

---

## 4. Content Assessment (where draft available)

### Risk Factors

| Finding                             | Article                  | Severity | Status  | Required Action                                   |
| ----------------------------------- | ------------------------ | -------- | ------- | ------------------------------------------------- |
| [e.g., Generic climate risk factor] | Art. 16 + ESMA31-62-1293 | HIGH     | PARTIAL | Rewrite to be issuer-specific; quantify magnitude |

### Summary

| Finding                      | Article | Severity | Status        | Required Action                      |
| ---------------------------- | ------- | -------- | ------------- | ------------------------------------ |
| [e.g., Exceeds 7-page limit] | Art. 7  | HIGH     | NON-COMPLIANT | Condense; remove non-key information |

### Financial Information

| Finding                               | Article            | Severity | Status        | Required Action                    |
| ------------------------------------- | ------------------ | -------- | ------------- | ---------------------------------- |
| [e.g., 3rd year financials are stale] | Del. Reg. 2019/980 | CRITICAL | NON-COMPLIANT | Include updated audited financials |

### Liability and Responsibility Statement

| Finding                               | Article | Severity | Status  | Required Action                  |
| ------------------------------------- | ------- | -------- | ------- | -------------------------------- |
| [Responsibility statement incomplete] | Art. 11 | HIGH     | PARTIAL | Identify all responsible persons |

---

## 5. Supplement Risk Assessment

**Current trigger assessment**: [LOW / MEDIUM / HIGH]
**Identified trigger risks**: [List known or foreseeable material developments]
**Supplement monitoring obligations**: [Timeline and events to watch]
**Withdrawal right obligations**: [3-working-day period; notification procedure]

---

## 6. Passport and Language Programme

**Host Member States**: [List]
**Notification timeline**: [1 WD per notification; request must precede offer in host state]
**Summary translation required**: [Languages; NCAs]
**Language acceptance**: [Confirm against ESMA32-384-5080]

---

## 7. EU Listing Act Impact

**Phase 1 (4 December 2024) changes applicable**: [List applicable changes for this transaction]
**Phase 2 (5 March 2026) changes applicable**: [List — note if future-dated]
**Phase 3 (5 June 2026) changes applicable**: [List — note if future-dated]
**Process updates required**: [Changes to issuer's template documents, internal processes]

---

## 8. Civil Liability and Enforcement

**Liable parties identified**: [Issuer / offeror / guarantor / persons requesting admission]
**Civil liability standard**: [JURISDICTION-SPECIFIC — refer to [NCA jurisdiction] counsel]
**Enforcement risk areas**: [Any identified compliance gaps with enforcement exposure]

---

## 9. Priority Action Plan

### Tier 1 — Deal-Critical (resolve before proceeding)

| #   | Action   | Responsible Party | Deadline |
| --- | -------- | ----------------- | -------- |
| 1   | [Action] | [Party]           | [Date]   |

### Tier 2 — Material (resolve before NCA submission)

| #   | Action   | Responsible Party | Deadline |
| --- | -------- | ----------------- | -------- |
| 1   | [Action] | [Party]           | [Date]   |

### Tier 3 — Process Improvements (resolve before closing or next issuance)

| #   | Action   | Responsible Party | Deadline |
| --- | -------- | ----------------- | -------- |
| 1   | [Action] | [Party]           | [Date]   |

---

## 10. Glass Box Audit Trail

[Insert YAML audit trail]

---

_This assessment does not constitute legal advice. Obtain qualified EU capital markets legal advice
before relying on any conclusion herein. Verify all statutory references against EUR-Lex and ESMA
publications. Last updated: [YYYY-MM-DD]._
```

---

## Glossary

| Term                              | Definition                                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Admission to trading**          | Formal process of listing securities on a regulated market or MTF                                       |
| **Base prospectus**               | Prospectus for non-equity securities issued under a programme; supplemented by final terms per issuance |
| **Certificate of Approval (CoA)** | Document issued by home NCA certifying prospectus approval; used for passporting                        |
| **CPS**                           | Core Platform Service (DMA term — distinct from prospectus regulation)                                  |
| **EMTN**                          | Euro Medium Term Note programme; a debt issuance programme using base prospectus structure              |
| **EU Growth Issuance Prospectus** | Simplified prospectus type for SMEs, SME Growth Market issuers, and small offers (from 5 March 2026)    |
| **EU Follow-on Prospectus**       | Simplified 50-page prospectus for companies listed ≥ 18 months (from 5 March 2026)                      |
| **Final terms**                   | Document issued per individual issuance under a base prospectus; not approved by NCA                    |
| **Frequent issuer**               | Issuer who has filed a URD for at least 1 consecutive year (from 5 March 2026; 2 years previously)      |
| **Home Member State**             | Member State whose NCA has jurisdiction to approve the prospectus                                       |
| **MAR**                           | Market Abuse Regulation (EU) 596/2014                                                                   |
| **MTF**                           | Multilateral Trading Facility — a non-regulated trading venue (e.g., AIM, Euronext Growth)              |
| **NCA**                           | National Competent Authority — the regulator responsible for prospectus approval in each Member State   |
| **Offer to the public**           | Communication presenting sufficient information on offer terms to enable investment decision            |
| **Qualified investor**            | Professional investor as defined in MiFID II Annex II (institutional/sophisticated)                     |
| **Regulated market**              | MiFID II-authorized stock exchange (e.g., main market of Deutsche Börse, Euronext, LSE)                 |
| **Retail cascade**                | Financial intermediary using issuer's approved prospectus for further retail offers                     |
| **SME**                           | Small and Medium Enterprise: < 250 employees, ≤ €43M balance sheet, ≤ €50M turnover (2 of 3)            |
| **SME Growth Market**             | MTF meeting MiFID II criteria for SME Growth Market registration (e.g., AIM, Euronext Growth)           |
| **Supplement**                    | Approved update to a prospectus addressing significant new factors, material mistakes, or inaccuracies  |
| **URD**                           | Universal Registration Document — annual shelf registration document (Articles 9–11)                    |

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis via Mode A skill creation workflow with
2-agent parallel research pipeline. **Research Agent 1** covered: Regulation (EU) 2017/1129 full
text (EUR-Lex consolidated version as of 4 December 2024); exemption thresholds and Article 1(4)/(5)
structure; prospectus type architecture (standard, base, EU Growth, URD); NCA approval timelines
and procedures; supplement obligations; passporting; civil liability Article 11; ESMA Guidelines
ESMA31-62-1293 (risk factors); ESMA Q&A ESMA31-62-1258; Delegated Regulations (EU) 2019/980
and 2019/979; BaFin, AMF, CSSF, CBI procedural guidance. **Research Agent 2** covered:
Regulation (EU) 2024/2809 (EU Listing Act) full text and phased application dates (4 December
2024 / 5 March 2026 / 5 June 2026); new EU Follow-on Prospectus (Art. 14b); new EU Growth
Issuance Prospectus (Art. 15 revised); 18-month exemption; 30% tap exemption; credit institution
€150M threshold; URD frequent issuer 1-year qualification; base prospectus incorporation by
reference relief; supplement reform; ESG bond disclosure requirements; MAR reform (protracted
process, market soundings safe harbour, buy-back, PDMR thresholds); MiFID II research unbundling
reversal; NCA procedural details (BaFin, AMF, CSSF, CBI, AFM, CONSOB, CNMV); enforcement and
sanctions (Articles 38–41); ESMA civil liability final report June 2025 (ESMA32-117195963-1413);
anti-patterns from practitioner sources (Davis Polk, Ashurst, Slaughter and May, A&O Shearman,
Mayer Brown, Cleary Gottlieb, Arthur Cox, Norton Rose Fulbright). Structural patterns from
legalcode-contract-review (18-element quality framework) and legalcode-eu-dma-compliance (EU
regulatory compliance adaptation). Quality: 18/18 Legalcode quality elements present. Prompt
engineering score: 38/40.
