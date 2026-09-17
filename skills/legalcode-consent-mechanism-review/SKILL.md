---
name: legalcode-consent-mechanism-review
description: Reviews consent collection mechanisms for validity under GDPR Article 7, EDPB Guidelines
  05/2020 on consent, and EDPB Guidelines 03/2022 on deceptive design patterns. Use when auditing cookie
  banners, consent management platforms, account sign-up flows, app permission requests, or any consent
  mechanism before DPA review, product launch, or following enforcement enquiry.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Reviews consent collection mechanisms for validity under GDPR Article 7, EDPB Guidelines 05/2020 on consent, and EDPB Guidelines 03/2022 on deceptive design patterns. Detects dark patterns including pre-ticked boxes (Planet49), bundled consent, cookie walls, forced consent, asymmetric button design, confirmshaming, withdrawal obstruction, and consent fatigue tactics. Evaluates all four validity conditions — freely given, specific, informed, and unambiguous — plus withdrawal parity (Article 7(3)) and proof burden (Article 7(1)). Covers consent granularity (purpose-by-purpose), children's consent under Article 8 with national age thresholds, explicit consent for Article 9 special categories, power-imbalance contexts (employment, public authorities, large platforms), and consent refresh triggers. Assesses LGPD consent requirements (Brazil Articles 7–8, 11, 14), India DPDP Act 2023/Rules 2025 consent framework, UK ICO guidance and PECR cookie consent, CNIL recommendations (France), and US CCPA/CPRA opt-in requirements for minors and sensitive data. Produces consent mechanism audit report with COMPLIANT / REQUIRES REMEDIATION / NON-COMPLIANT classification per element, dark pattern identification with enforcement citations, remediation recommendations, compliant design patterns, and prioritised action plan. Use when auditing cookie banners, consent management platforms, account sign-up flows, app permission requests, or any consent mechanism before DPA review, product launch, or following enforcement enquiry.


# Legalcode Consent Mechanism Review

> **Disclaimer**: This skill provides a framework for AI-assisted review of consent collection
> mechanisms under GDPR, UK GDPR, LGPD, DPDPA, and related frameworks. It does not constitute
> legal advice. All outputs must be reviewed by a qualified privacy counsel or Data Protection
> Officer licensed or operating in the relevant jurisdiction before any reliance, regulatory
> submission, or remediation action. Privacy law, EDPB guidelines, and supervisory authority
> guidance evolve rapidly — verify currency before treating any provision here as current.
> Statutory, case law, and regulatory references cited from training data carry hallucination
> risk — verify against authoritative primary sources before use. Mark any unverified citation
> **[VERIFY]** before delivery.

---

## Purpose and Scope

This skill audits whether a consent collection mechanism meets the legal requirements for valid
consent across the GDPR/UK GDPR, LGPD, DPDP Act, and US state privacy frameworks. It examines
the mechanism itself — the banner, form, CMP, or flow — not the underlying processing activities.

The consent mechanism is the operative moment where legal validity is created or destroyed. A
technically sophisticated consent management platform with a well-categorised cookie inventory
can still produce invalid consent if the interface design manipulates users. This skill exists
to catch exactly that gap.

**Covers:**

- Core validity assessment: freely given, specific, informed, unambiguous (GDPR Art. 4(11), Art. 7)
- Withdrawal parity test: as easy to withdraw as to give (GDPR Art. 7(3))
- Accountability proof: controller burden of proof and consent record adequacy (GDPR Art. 7(1))
- Dark pattern detection across the full EDPB six-category taxonomy (Guidelines 03/2022)
- Consent granularity: per-purpose, per-vendor, no omnibus bundling
- Children's consent: Article 8 EU thresholds (13-16) + UK (13) + national implementations
- Special category explicit consent: Article 9 heightened standard
- Power-imbalance contexts: employment, public authorities, dominant market platforms
- Consent-or-pay analysis: EDPB Opinion 08/2024 freely given assessment
- Cross-regime comparison: EU GDPR / UK GDPR / CNIL / Brazil LGPD / India DPDPA / CCPA/CPRA
- CMP technical implementation failures and pre-consent blocking verification
- Consent refresh trigger analysis
- Remediation recommendations with compliant design patterns

**Does not:**

- Conduct a full cookie/tracking technology audit — see `legalcode-cookie-compliance-audit`
- Assess which legal basis to use for processing — see `legalcode-gdpr-legal-basis-assessment`
- Conduct a legitimate interest assessment — see `legalcode-legitimate-interest-assessment`
- Draft or review a privacy policy — see `legalcode-privacy-policy-drafter`
- Generate a DPIA — see `legalcode-dpia-generator`
- Draft Data Processing Agreements — see `legalcode-data-processing-agreement-drafter`
- Build a ROPA — see `legalcode-ropa-generator`
- Provide legal advice or replace qualified data protection counsel

**Complementary skills:**

- `legalcode-cookie-compliance-audit` — what tracking technologies fire; pre-consent blocking test
- `legalcode-gdpr-legal-basis-assessment` — whether consent is the correct basis at all
- `legalcode-legitimate-interest-assessment` — when LI may substitute for consent
- `legalcode-dpia-generator` — triggered by high-risk processing identified in the consent audit
- `legalcode-privacy-policy-drafter` — receives consent mechanism disclosures for policy drafting
- `legalcode-vendor-privacy-assessment` — deeper review of individual third-party consent partners

---

## Jurisdiction and Governing Law

This skill covers four regulatory layers that may apply simultaneously.

### Layer 1: EU GDPR + EDPB (Governs EU/EEA Data Subjects)

| Instrument                                                                 | Key Provision                                                                                                      | Scope                                                                                  |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| GDPR Regulation 2016/679                                                   | Art. 4(11) — consent definition; Art. 7 — consent conditions; Art. 8 — children; Art. 9(2)(a) — special categories | All processing of EU/EEA data subjects' personal data where consent is the legal basis |
| EDPB Guidelines 05/2020 on Consent (v1.1)                                  | Six requirements for valid consent; cookie wall prohibition; withdrawal parity                                     | All EU consent-based processing                                                        |
| EDPB Guidelines 03/2022 on Deceptive Design Patterns (v2.0, February 2023) | Six dark pattern categories; interface design prohibitions                                                         | Social media + general digital interfaces                                              |
| EDPB Opinion 08/2024 on Consent-or-Pay                                     | Cookie walls and pay-or-consent impermissible for Large Online Platforms without free alternative                  | LOPs using consent-or-pay models                                                       |
| EDPB Cookie Banner Taskforce Report (January 2023)                         | Minimum threshold: reject must be accessible at first layer                                                        | Cookie banner design                                                                   |
| ePrivacy Directive 2002/58/EC (Art. 5(3))                                  | Prior informed consent before placing/accessing terminal equipment                                                 | All cookies and tracking technologies                                                  |

### Layer 2: UK GDPR + PECR (Governs UK Data Subjects)

[JURISDICTION-SPECIFIC] UK GDPR and PECR apply to UK data subjects and UK-established controllers. Post-Brexit, EDPB guidelines are not binding but remain highly persuasive in UK DPA enforcement. The ICO published updated cookie consent guidance in December 2024 and is conducting a rolling review of the top 1,000 UK websites (January 2025 initiative).

| Instrument                                  | Key Provision                                                                           |
| ------------------------------------------- | --------------------------------------------------------------------------------------- |
| UK GDPR                                     | Mirror of EU GDPR Art. 4(11), Art. 7 — same consent standard                            |
| PECR 2003, Regulation 6                     | Prior informed consent for cookies — same standard as ePrivacy Directive                |
| Data (Use and Access) Act 2025              | Potential analytics cookie exemptions under development [VERIFY — ICO guidance pending] |
| ICO Cookie Consent Guidance (December 2024) | Reject All required; no pre-consent tracking; withdrawal parity                         |

### Layer 3: National EU Implementations — Selected Key Jurisdictions

[JURISDICTION-SPECIFIC] Verify the applicable national transposition for the controller's primary audience:

| Country     | National Law                         | Key Additional Requirement                                                                                                                                                                     |
| ----------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| France      | Art. 82 Loi Informatique et Libertés | Reject All required at first layer; consent invalid if accept/reject asymmetric; CNIL fines Google €150M (2022) + €325M (2025), Facebook €60M (2022), TikTok €5M (2023) for asymmetric designs |
| Germany     | §25 TDDDG (in force December 2021)   | Active opt-in required; browser-level cookie settings do not constitute valid consent; DSK Orientierungshilfe v1.2 (November 2024)                                                             |
| Netherlands | Telecommunicatiewet Art. 11.7a       | Strict consent requirement; cookie walls explicitly prohibited                                                                                                                                 |
| Spain       | LSSI-CE                              | AEPD enforcement active                                                                                                                                                                        |
| Belgium     | Wet van 13 juni 2005                 | Belgian DPA fined IAB Europe €250K for TCF (2022, upheld 2025)                                                                                                                                 |

### Layer 4: Multi-Regime (Brazil, India, US)

[JURISDICTION-SPECIFIC] For controllers with data subjects in these jurisdictions, apply the cross-regime assessment in Step 8.

| Regime           | Key Instrument                                       | Core Consent Standard                                                                          |
| ---------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Brazil           | LGPD (Law 13,709/2018), Articles 7–8, 11, 14         | Free, informed, unambiguous; purpose-specific; written or demonstrable; burden on controller   |
| India            | DPDP Act 2023 + DPDP Rules 2025 (effective May 2027) | Free, specific, informed, unconditional, unambiguous; clear affirmative action; notice first   |
| US (California)  | CCPA/CPRA                                            | Opt-out for adults; opt-in required for minors under 16 and for sensitive personal information |
| US (Multi-state) | CO CPA, CT CTDPA, TX TDPSA, etc.                     | Opt-in for sensitive data processing in most states                                            |

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points, marked with **⟁ CLARIFY**
below. Rather than assuming, the workflow pauses and asks when:

- The answer changes which regulatory layer applies
- The mechanism type determines the analysis framework
- Business context is needed to classify severity correctly (e.g., whether the controller is a
  Large Online Platform affects consent-or-pay analysis)
- Technical access limitations constrain the audit scope

If the user has already provided the relevant information, skip the question and proceed. For
non-interactive batch runs, use these defaults: EU primary jurisdiction, B2C digital service,
full audit scope, no existing consent scan.

---

## Workflow

### Step 1: Accept Input

Accept the consent mechanism in any of these formats:

- **Website/app URL**: The primary page or sign-up flow to audit
- **Screenshots**: Images of the consent banner, preference centre, and/or sign-up flow
- **CMP configuration export**: Configuration export from OneTrust, Cookiebot/Usercentrics,
  Didomi, TrustArc, Axeptio, iubenda, or similar CMP
- **Written description**: Description of the consent flow, options presented, and button design
- **Privacy policy / cookie policy**: Existing consent-related disclosures
- **Enforcement context**: If responding to a DPA inquiry, provide the DPA's specific concerns

If no mechanism is provided, prompt the user to supply a URL, screenshots, configuration
export, or written description.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the following questions. Skip any already answered.

1. **Primary regulatory jurisdiction?**
   - Options: EU (specify primary country or "all EU"), UK, EU + UK (multinational), Brazil,
     India, US only, Multi-regime (all), Other
   - _Why this matters_: Determines which validity conditions and national requirements apply.

2. **Type of consent mechanism?**
   - Options: Cookie/tracking consent banner, Account registration / sign-up flow, App
     permission request, Email marketing opt-in, Special category data consent (health,
     biometrics, etc.), Children's service consent flow, Research/clinical consent, Other
   - _Why this matters_: Different mechanisms trigger different special requirements.

3. **Controller type?**
   - Options: Commercial B2C platform, B2B service, Large Online Platform (social media,
     video, marketplace — annual turnover >€10M or >45M EU users), Public authority,
     Employer (employee consent context), SME (<250 employees), Healthcare/clinical, Other
   - _Why this matters_: Power imbalance contexts, LOP consent-or-pay rules, and special
     category requirements differ substantially by controller type.

4. **Does the mechanism involve any of the following special contexts?**
   - Options (multiselect): Children's data, Special category data (health/biometric/genetic
     etc.), Employment context, Consent-or-pay model, Research/scientific use, Non-EU/UK
     additional regimes (LGPD/DPDPA/CCPA)
   - _Why this matters_: Each triggers additional analysis requirements.

5. **Audit scope?**
   - Options: Full audit (all 18 assessment elements), Dark patterns only, Validity conditions
     only (freely given/specific/informed/unambiguous), Cross-regime comparison only,
     Withdrawal mechanism only, Specific element per user's instructions
   - _Why this matters_: Scopes the analysis depth and output format.

If partial context provided, state assumptions explicitly (e.g., "Assuming EU primary
jurisdiction and B2C full-scope audit — confirm if different").

### Step 3: Map Applicable Regulatory Obligations

Based on Step 2 context, document the regulatory scope:

1. **EU GDPR requirements?**
   - Apply if: controller processes EU/EEA data subjects' personal data AND relies on consent
   - Core obligation: All four Art. 7 conditions + Art. 7(3) withdrawal parity + Art. 7(1) proof
   - Special: Art. 8 if children involved; Art. 9(2)(a) if special category data; EDPB dark
     pattern prohibition per Guidelines 03/2022

2. **UK PECR/UK GDPR?**
   - Apply if: UK users or UK-established controller
   - Core obligation: PECR Reg. 6 cookie consent; UK GDPR consent standard
   - Note: EDPB guidelines not directly binding; ICO guidance operative

3. **Brazilian LGPD?**
   - Apply if: data subject in Brazil, or service offered in Brazil
   - Core obligation: Art. 8 consent requirements; Art. 11 sensitive data; Art. 14 children
   - ANPD enforcement: active since 2023; administrative sanctions up to R$50M per violation

4. **Indian DPDPA?**
   - Apply if: data subject in India or service offered to Indian users
   - Core obligation: Section 6 (consent), Section 5 (notice), Section 9 (children)
   - Timeline: Consent manager registration Nov 2026; full obligations May 2027

5. **US CCPA/CPRA?**
   - Apply if: California residents; or multi-state applicability
   - Core obligation: Opt-in for sale/sharing of under-16 data; sensitive PI use limitation

Mark applicable layers: `EU APPLICABLE | UK APPLICABLE | LGPD APPLICABLE | DPDPA APPLICABLE | US (CA) APPLICABLE`

### Step 4: Gather Legal Authority

Use **legalcode-mcp** to gather jurisdiction-relevant authority before analysing the mechanism.

**Research process:**

1. Search for applicable DPA guidance, enforcement decisions, and judicial rulings for the
   primary jurisdiction identified in Step 3.

2. Key sources to retrieve:
   - EDPB Guidelines 05/2020 on Consent (v1.1) — core validity framework
   - EDPB Guidelines 03/2022 on Deceptive Design Patterns — dark pattern definitions
   - EDPB Opinion 08/2024 on Consent-or-Pay — for LOP assessment
   - ICO Guidance on Cookies and Similar Technologies (December 2024) — UK requirements
   - CNIL guidelines and enforcement decisions — French requirements
   - Applicable DPA enforcement decisions in the relevant sector/technology type

3. Save findings to `/tmp/legalcode-consent-review-authority.md`:

   ```markdown
   # Legal Authority Reference — Consent Mechanism Review

   ## Jurisdiction: [Jurisdiction]

   ## Date Gathered: [date]

   ### Primary Statutes and Regulations

   - [Statute/Regulation, Article, Key Provision]

   ### DPA Guidance Documents

   - [DPA, Document Title, Key Requirement]

   ### Enforcement Decisions

   - [DPA, Case, Fine, Key Holding]

   ### Judicial Authority

   - [Court, Case, Citation, Key Holding]
   ```

**If legalcode-mcp is not connected:**

- Proceed with training data knowledge; mark all statutory and DPA references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`

### Step 5: Core Validity Assessment

Assess the mechanism against each of the six validity requirements. For each, classify as
**COMPLIANT** / **REQUIRES REMEDIATION** / **NON-COMPLIANT** with supporting evidence.

**⟁ CLARIFY** — If reviewing a complex multi-stage flow (account registration + cookie consent

- special category consent), ask: "Should I assess all consent stages in the flow, or focus
  on a specific stage?"

See **Core Validity Assessment Framework** section for the detailed criteria.

### Step 6: Dark Pattern Detection

Systematically test the mechanism against the EDPB six-category dark pattern taxonomy
(Guidelines 03/2022) and the 25-item anti-patterns catalogue in this skill.

For each dark pattern identified:

- Cite the specific EDPB category (Overloading / Skipping / Stirring / Hindering / Fickle /
  Left in the Dark)
- Note the enforcement precedent (where applicable)
- State the GDPR provision violated
- Classify: CRITICAL / HIGH / MEDIUM (see Classification System)

See **Dark Pattern Detection Catalogue** section for the full checklist.

### Step 7: Special Context Analysis

For any special contexts flagged in Step 2, apply the relevant framework:

**Children's consent (Art. 8)**:

- Identify the applicable national age threshold (13-16 in EU; 13 in UK; 12 in Brazil)
- Assess whether an age gate exists; test its adequacy
- Assess parental consent mechanism if below threshold
- See **Special Context: Children** section

**Article 9 explicit consent**:

- Identify all special category data in scope (health, biometric, genetic, racial/ethnic
  origin, religious belief, political opinion, trade union membership, sexual orientation)
- Assess whether the consent obtained is "explicit" rather than merely "unambiguous"
- See **Special Context: Article 9 Special Categories** section

**Employment consent**:

- Presumption: employment consent is not freely given
- Assess whether processing genuinely cannot rest on a different legal basis
- See **Special Context: Power Imbalance** section

**Consent-or-pay / Cookie walls**:

- Identify whether service access is conditional on consent
- For LOPs: apply EDPB Opinion 08/2024 framework
- See **Special Context: Consent-or-Pay** section

### Step 8: Cross-Regime Assessment

**⟁ CLARIFY** — Ask: "Should I compare this mechanism against all applicable regimes, or
focus on the primary jurisdiction identified?"

For each applicable non-EU regime (LGPD, DPDPA, CCPA/CPRA), assess:

- Whether the EU-compliant mechanism also satisfies the non-EU requirement
- Any additional obligations not covered by GDPR compliance
- Any conflicts between regimes requiring jurisdiction-specific variants

See **Cross-Regime Assessment** section for the framework.

### Step 9: Technical Review

Assess the technical implementation for consent mechanism integrity:

1. **Pre-consent blocking**: Are non-essential scripts/cookies blocked before consent is given?
   - Test: Load the page in a fresh browser (no cookies/localStorage) without interacting
     with the banner; inspect Network tab and Application/Storage for pre-consent firing
   - Classification: Any pre-consent non-essential firing = NON-COMPLIANT (critical)

2. **Consent record adequacy**: Does the system log the consent events required for Art. 7(1)?
   - Minimum required: timestamp, consent version shown, options presented, choices made,
     user identifier (or session identifier for anonymous users)
   - Test: Request consent log extract from CMP or backend system

3. **CMP configuration integrity**: Common CMP failure points to check (see Anti-Patterns
   AP-01 through AP-25 and CMP Implementation Issues section)

4. **Withdrawal mechanism access**: Is there a persistent mechanism (footer link, floating
   icon) allowing withdrawal from every page?

5. **Signal propagation**: Are consent choices reliably transmitted to all third-party tags?
   - Test: Give consent for Category A only; verify Category B tags do not fire

**⟁ CLARIFY** — Ask: "Do you have live technical access to test the site, or should I assess
based on the provided screenshots/description?"

### Step 10: Produce Consent Mechanism Audit Report

Compile all findings into the structured output using the **Output Format Template**. Run the
**Citation Quality Gates** before delivery. Apply **Self-Interrogation** to all CRITICAL and
NON-COMPLIANT findings.

Present:

- Executive summary with overall compliance status
- Per-element classification table (COMPLIANT / REQUIRES REMEDIATION / NON-COMPLIANT)
- Dark pattern findings list with enforcement citations
- Cross-regime gap analysis
- Prioritised remediation action plan (Tier 1/2/3)
- Compliant design patterns to implement
- Glass Box audit trail

---

## Core Validity Assessment Framework

### Condition 1: Freely Given

The data subject must have genuine choice and control. Consent is **not** freely given if:

| Sub-test                                   | COMPLIANT                                                                   | NON-COMPLIANT                                                                                      |
| ------------------------------------------ | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **1.1 Conditionality**                     | Processing for which consent is sought is not a condition of service access | Service access is gated on consent to non-essential processing (cookie wall)                       |
| **1.2 Detriment**                          | Refusing consent has no adverse consequences                                | Reduced functionality, service degradation, or exclusion results from refusal                      |
| **1.3 Power imbalance — employer**         | Consent not used as primary basis for employment data processing            | Employees pressured to consent as condition of employment or to obtain employment-related benefits |
| **1.4 Power imbalance — public authority** | Alternative legal basis (legal obligation / public task) used               | Public authority relies on consent for routine data processing                                     |
| **1.5 Granularity**                        | Separate consents available for each distinct processing purpose            | Single bundled consent covers multiple unrelated purposes                                          |
| **1.6 Cookie wall**                        | Service fully accessible without accepting non-essential cookies            | Non-essential cookie consent required for any site access                                          |
| **1.7 Consent-or-Pay (LOPs)**              | Genuine equivalent free alternative without behavioural advertising offered | Binary choice: behavioural advertising consent or pay — no free contextual alternative             |
| **1.8 No nagging after refusal**           | Consent not re-requested repeatedly after refusal                           | Consent requests repeated on each visit or session after explicit refusal                          |

**Authority**: GDPR Art. 7(1), (4); Recital 43; EDPB Guidelines 05/2020 §3.1; EDPB Opinion 08/2024.

### Condition 2: Specific and Granular

Each processing purpose must have its own consent. Omnibus consent is void.

| Sub-test                                | COMPLIANT                                                                                       | NON-COMPLIANT                                                        |
| --------------------------------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **2.1 Per-purpose granularity**         | Separate opt-in control for each distinct purpose (analytics, marketing, personalisation, etc.) | Single "I accept all" checkbox covering multiple distinct purposes   |
| **2.2 No purpose bundling**             | Marketing and analytics consent are separately obtainable                                       | Single toggle for "analytics and marketing" combined                 |
| **2.3 No T&Cs bundling**                | Consent for data processing is visually separated from acceptance of general terms              | Checkbox 1 = terms + conditions + cookie consent all in one          |
| **2.4 Purpose description specificity** | Specific purposes stated (e.g., "targeted advertising on Meta platforms")                       | Vague descriptions ("improve your experience", "work with partners") |
| **2.5 Purpose limitation respected**    | Consent scope not retroactively expanded                                                        | New processing purposes added without fresh consent                  |

**Authority**: GDPR Art. 4(11); Art. 7(2); EDPB Guidelines 05/2020 §3.2; Planet49 (C-673/17).

### Condition 3: Informed

Data subjects must receive minimum information before consent is given.

| Required Information Element     | Present?                                                              | Adequate? |
| -------------------------------- | --------------------------------------------------------------------- | --------- |
| **3.1 Controller identity**      | Named controller(s) identified                                        |           |
| **3.2 Processing purposes**      | Each purpose specifically described                                   |           |
| **3.3 Data types**               | Categories of personal data collected stated                          |           |
| **3.4 Third-party recipients**   | Named or categorised third-party recipients identified                |           |
| **3.5 Cookie/storage duration**  | Duration each cookie remains active stated                            |           |
| **3.6 Right to withdraw**        | Withdrawal right explained; mechanism described                       |           |
| **3.7 Plain language**           | Information in clear, accessible language; no legal jargon            |           |
| **3.8 Multi-controller consent** | For consent shared across multiple controllers: each controller named |           |

**Authority**: GDPR Arts. 13/14 read with Art. 7; Art. 7(2); Planet49 (C-673/17) (cookie duration + third-party access are required); EDPB Guidelines 05/2020 §3.3.

### Condition 4: Unambiguous Indication

Consent requires a **clear affirmative act**. Passive mechanisms are void.

| Sub-test                        | COMPLIANT                                                                 | NON-COMPLIANT                                                                                     |
| ------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **4.1 Active opt-in**           | User must actively check a box, click a button, or take a positive action | Consent inferred from inaction, silence, or passive browsing                                      |
| **4.2 No pre-ticked boxes**     | All optional consent checkboxes default to unchecked                      | Any non-essential processing checkbox pre-selected by default                                     |
| **4.3 No browsing-as-consent**  | Banner does not state "by continuing, you accept"                         | Continued browsing or page navigation treated as consent                                          |
| **4.4 No scrolling-as-consent** | Scrolling not equated with consent                                        | Banner states or implies scrolling = acceptance                                                   |
| **4.5 Affirmative CTA clarity** | Button text clearly indicates consent (e.g., "Accept all cookies")        | Button text is ambiguous (e.g., "Got it", "OK", "I understand") without indicating what is agreed |

**Authority**: GDPR Art. 4(11); Recital 32; Planet49 (C-673/17); EDPB Guidelines 05/2020 §3.4.

### Condition 5: Withdrawal — As Easy as Giving (Article 7(3))

| Sub-test                  | COMPLIANT                                                                      | NON-COMPLIANT                                                                               |
| ------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| **5.1 Click parity**      | Withdrawing consent requires no more clicks than giving consent                | Consent given in 1 click; withdrawal requires 3+ clicks through menus                       |
| **5.2 Persistent access** | Withdrawal mechanism accessible from every page (footer link or floating icon) | Withdrawal only accessible from settings menu not linked from pages                         |
| **5.3 Same interface**    | Withdrawal mechanism is on the same interface used to give consent             | Consent given via popup; withdrawal only in account settings                                |
| **5.4 Immediate effect**  | Processing ceases promptly after withdrawal                                    | Processing continues for an unreasonable period post-withdrawal                             |
| **5.5 Informed of right** | Right to withdraw stated in consent notice, before consent is given            | Right to withdraw only mentioned in Privacy Policy (not at point of consent)                |
| **5.6 No penalty**        | No adverse consequence communicated or applied for withdrawal                  | Warning that features will be lost upon withdrawal (disproportionate to processing refused) |

**Authority**: GDPR Art. 7(3); EDPB Guidelines 05/2020 §3.5; TikTok €345M (Irish DPC, 2023).

### Condition 6: Proof and Accountability (Article 7(1))

| Sub-test                            | COMPLIANT                                                               | NON-COMPLIANT                                                                        |
| ----------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **6.1 Consent records**             | System logs: timestamp, consent version, options presented, choice made | No consent record; records lack one or more required elements                        |
| **6.2 Version control**             | Consent notice version tied to each consent record                      | Version not recorded; cannot establish what information was shown when consent given |
| **6.3 User identifier**             | Record tied to user or session identifier                               | Consent events not linkable to specific data subject                                 |
| **6.4 Double opt-in (recommended)** | Confirmation email or secondary confirmation used for email consent     | No confirmation mechanism (single-step email sign-up without confirmation)           |
| **6.5 Audit trail accessibility**   | Consent records producible on DPA request                               | Consent logs stored but not searchable or exportable                                 |

**Authority**: GDPR Art. 7(1); Art. 5(2) accountability principle; EDPB Guidelines 05/2020 §3.6.

---

## Dark Pattern Detection Catalogue

Apply the EDPB six-category taxonomy (Guidelines 03/2022) systematically. For each pattern
identified, cite the category, the enforcement precedent, and the GDPR provision violated.

### Category 1: Overloading

| Test                                                                                                                                           | Finding |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| Are consent requests re-presented repeatedly after rejection? (AP-15 — Nagging)                                                                |         |
| Does the consent dashboard contain so many vendor toggles that reasonable users will click "Accept All" to escape? (IAB TCF-style overloading) |         |
| Is the user presented with excessive privacy information upfront, causing decision fatigue?                                                    |         |

### Category 2: Skipping

| Test                                                                                                            | Finding |
| --------------------------------------------------------------------------------------------------------------- | ------- |
| Are consent requests embedded within general terms acceptance without visual separation? (AP-10 — Bundled T&Cs) |         |
| Does completing registration or another task trigger data processing consent without separate notice?           |         |
| Are privacy settings buried multiple navigation layers deep?                                                    |         |

### Category 3: Stirring (Visual/Emotional Manipulation)

| Test                                                                                                                                        | Finding |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| Is the "Accept All" button visually larger, more prominent, or differently styled than "Reject All"? (AP-01 — Asymmetric Button Prominence) |         |
| Does the reject option use emotionally loaded negative language? (AP-06 — Confirmshaming)                                                   |         |
| Is the "Accept" button a high-contrast primary color and "Reject" a grey, low-contrast secondary element? (AP-18 — Low-Contrast Reject)     |         |
| Is the reject/decline option styled as a hyperlink instead of a button?                                                                     |         |
| Is the rejection text phrased to suggest harm to the user ("reduce my experience", "limit my benefits")?                                    |         |

### Category 4: Hindering (Obstruction)

| Test                                                                                                                                  | Finding |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| Is the first-layer banner missing a "Reject All" button, requiring navigation to a second layer? (AP-03 — Missing First-Layer Reject) |         |
| Does accepting consent require fewer clicks than rejecting? (AP-02 — Asymmetric Click Depth)                                          |         |
| Is the withdrawal mechanism not accessible from the homepage/all pages? (AP-14 — Withdrawal Obstruction)                              |         |
| Must users navigate through multiple menus to exercise rejection after the first-layer banner?                                        |         |
| Is the consent preference centre hard to find (no footer link, no floating icon)?                                                     |         |

### Category 5: Fickle

| Test                                                                                           | Finding |
| ---------------------------------------------------------------------------------------------- | ------- |
| Are consent controls displayed inconsistently across devices (desktop vs. mobile) or sessions? |         |
| Are toggles ambiguously designed — unclear whether "on" means "I consent" or "I am protected"? |         |
| Does the same setting appear in multiple places with conflicting state?                        |         |
| Are cookie categories inconsistently named across the banner and the preference centre?        |         |

### Category 6: Left in the Dark

| Test                                                                                                            | Finding |
| --------------------------------------------------------------------------------------------------------------- | ------- |
| Are purpose descriptions vague or generic? (AP-10 — Vague Purpose Descriptions)                                 |         |
| Are third-party recipients not named or adequately described? (AP-11 — Undisclosed Third Parties)               |         |
| Is cookie duration absent from the notice? (AP-12 — No Duration Information)                                    |         |
| Is the controller identity not clearly stated at the point of consent?                                          |         |
| Is information about third-party sharing and real-time bidding (where applicable) hidden? (AP-24 — TCF Opacity) |         |

---

## Special Context Analysis

### Special Context 1: Children's Consent (GDPR Article 8)

Apply when the service is an information society service (digital service, social media, games,
e-commerce, streaming, app stores) or is likely to be accessed by children.

**Framework:**

1. **Identify applicable national age threshold:**

   | Country                                | Threshold      | Source                                        |
   | -------------------------------------- | -------------- | --------------------------------------------- |
   | Germany, Netherlands, Hungary, Ireland | 16             | National data protection acts                 |
   | France                                 | 15             | Loi Informatique et Libertés                  |
   | Austria, Spain                         | 14             | DSG; LOPDGDD                                  |
   | Italy                                  | 14             | Legislative Decree 101/2018                   |
   | Portugal, Belgium (interpretation)     | 13             | LPDP; Belgian DPA                             |
   | UK                                     | 13             | UK Data Protection Act 2018                   |
   | Brazil (child)                         | Under 12       | LGPD Art. 14                                  |
   | India                                  | Under 18 (TBC) | DPDP Act 2023 §9; Rules 2025 pending [VERIFY] |
   | US (COPPA)                             | Under 13       | 15 U.S.C. §6501                               |
   | US (CCPA sale/sharing)                 | Under 16       | Cal. Civ. Code §1798.120                      |

2. **Assess age gate adequacy:**
   - Is an age gate implemented? If so, what verification method?
   - Self-declaration: LOW assurance (inadequate for high-risk processing)
   - Credit card verification: MEDIUM assurance
   - Identity document / digital locker: HIGH assurance
   - What happens if user claims to be below threshold? Is parental consent flow triggered?

3. **Assess parental consent mechanism:**
   - How is parental consent obtained?
   - Is the parental consent itself valid under the applicable standard?
   - Is parental identity reasonably verified?
   - Does the service design serve the best interests of children? (Required under LGPD Art.
     14; UK Children's Code; TikTok enforcement — EDPB Binding Decision 2/2023)

4. **Special prohibitions for children:**
   - No behavioural advertising to children (UK Children's Code; CCPA for under-16)
   - No public-by-default account settings for children (TikTok €345M, 2023)
   - No nudging children toward privacy-invasive choices (EDPB Binding Decision 2/2023)
   - No profiling that could harm children's development or wellbeing

[JURISDICTION-SPECIFIC] Verify current national threshold for each EU member state where
children are a primary audience. Thresholds are subject to change through national legislation.

### Special Context 2: Article 9 Explicit Consent for Special Categories

Apply when the consent mechanism covers health data, biometric data, genetic data, racial/ethnic
origin, religious beliefs, political opinions, trade union membership, or sexual orientation.

**Explicit consent standard (GDPR Art. 9(2)(a)):**

Article 9 requires **explicit** consent — a higher standard than the Art. 7 "unambiguous clear
affirmative action" standard. Explicit consent requires:

- An **express statement** from the data subject (not merely clicking a pre-checked box that
  was unchecked)
- A clear indication that the specific special category is being processed
- In practice: a signed written declaration or equivalent explicit oral/digital statement
  specifically referencing the special category data and its purpose

**Assessment tests:**

| Test                                                                    | COMPLIANT                                                                         | NON-COMPLIANT                                                         |
| ----------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Is the special category data clearly identified in the consent request? | Specific category named (e.g., "your health data" / "your biometric fingerprint") | Generic wording covering all types of data                            |
| Does the mechanism require an express statement?                        | Dedicated signed/checked consent specifically for the special category            | Single consent checkbox covers both general and special category data |
| Is granularity maintained?                                              | Separate consent for each type of special category data                           | One omnibus special category consent                                  |
| Is the explicit consent not bundled with general consent?               | Separate consent step for special category data                                   | Special category consent included in general T&Cs acceptance          |

**Common violations:**

- Health app using standard opt-in mechanism (ticking a box) rather than an explicit consent
  form for health data processing
- Biometric authentication consent bundled with general privacy acceptance
- Gyms/fitness platforms requiring a single consent for both ordinary processing and biometric
  data collection (see Danish DPA gym facial recognition case, 2024)

[JURISDICTION-SPECIFIC] Brazil (LGPD Art. 11) requires "free, specific, highlighted, and
informed consent" for sensitive data — broadly equivalent to explicit consent. India's DPDPA
does not use a separate "explicit" consent tier but applies heightened scrutiny through
prescribed notice and consent formalities.

### Special Context 3: Power Imbalance — Employment and Public Authorities

**Employment consent:**

The EDPB Guidelines 05/2020 state: "In most cases, it will not be possible for employees to
freely give, refuse or revoke consent, given the dependency resulting from the employer-employee
relationship." Employment consent is presumed **NOT freely given** unless:

- Refusing consent has absolutely no adverse consequence (confirmed in writing)
- The processing genuinely cannot be based on any other legal basis (contract performance,
  legal obligation, legitimate interest)
- The employee has a genuine, un-coerced choice

**Assessment:** Is consent used as the primary legal basis for routine employment processing
(CCTV, email monitoring, IT access, performance monitoring)? If so, recommend replacing with
Article 6(1)(b) or 6(1)(c) unless the above narrow exceptions apply.

**Public authority consent:**

Recital 43 GDPR: "Consent should not provide a valid legal ground for processing... where there
is a clear imbalance between the data subject and the controller, in particular where the
controller is a public authority." Public authorities should rely on Art. 6(1)(c) (legal
obligation) or Art. 6(1)(e) (public task) for most processing. Consent is valid only for
voluntary, supplementary services where citizens have genuine free choice.

Example violation: hospital requesting consent via Instagram for health-related content (Danish
DPA, 2023) — ordered deletion within 4 weeks.

### Special Context 4: Consent-or-Pay / Cookie Walls

**Cookie walls (all controllers):**
Service access may not be conditioned on consent to non-essential processing. Cookie walls that
offer only "accept cookies" or "leave the site" are NON-COMPLIANT per EDPB Guidelines 05/2020.

**Consent-or-pay (Large Online Platforms under EDPB Opinion 08/2024):**

Apply the following assessment for controllers meeting LOP criteria:

| Factor                                                                                      | Analysis                                                                |
| ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Is a free, non-behavioural-advertising alternative offered?                                 | Required — platforms cannot offer only "consent or pay"                 |
| Is the fee proportionate?                                                                   | Fee must not be set at a level that effectively compels consent         |
| Is a third option offered (contextual advertising without behavioural tracking)?            | Highly recommended; EDPB noted this as best practice                    |
| Does the fee model reflect actual lost advertising value?                                   | Punitive fees that exceed lost ad revenue are disproportionate          |
| Do users face exclusion from professional networks, content, or connections if they refuse? | This is a factor making consent non-freely given (EDPB Opinion 08/2024) |

---

## Cross-Regime Assessment

### EU GDPR vs. Other Regimes — Gap Analysis

| Requirement                             | EU GDPR                   | UK GDPR       | Brazil LGPD                           | India DPDPA                         | CCPA/CPRA                 |
| --------------------------------------- | ------------------------- | ------------- | ------------------------------------- | ----------------------------------- | ------------------------- |
| Opt-in for all consent-based processing | Yes                       | Yes           | Yes                                   | Yes (from May 2027)                 | No — opt-out for adults   |
| Freely given / no bundling              | Art. 7(4)                 | Mirror        | Art. 8 §2                             | §6                                  | Limited                   |
| Withdrawal as easy as giving            | Art. 7(3)                 | Mirror        | Art. 8 §5                             | §6(4)                               | Not explicit              |
| Cookie walls prohibited                 | EDPB 05/2020              | ICO guidance  | Not explicit                          | Not explicit                        | Not addressed             |
| Children threshold                      | 13-16 (varies)            | 13            | 12                                    | 18 (pending)                        | 13 (COPPA); 16 (CCPA)     |
| Special category heightened standard    | Explicit consent (Art. 9) | Mirror        | Free, specific, highlighted (Art. 11) | Standard consent (no separate tier) | Right to limit use (CPRA) |
| Consent record retention                | Art. 7(1)                 | Mirror        | Art. 8 §5                             | §6 + 7-yr log (Rules)               | Not specified             |
| Notice before consent                   | Arts. 13/14               | Mirror        | Art. 8                                | §5 notice first                     | Privacy notice            |
| Granularity per purpose                 | Required                  | Required      | Required                              | Required                            | Not required              |
| Consent refresh obligation              | Best practice             | Best practice | Best practice                         | Not explicit                        | Not specified             |

**For each non-EU regime gap identified, state:**

- What additional action the controller must take beyond EU GDPR compliance
- Whether a separate consent flow is required or whether the EU mechanism can be extended

[JURISDICTION-SPECIFIC] India DPDPA consent manager requirements (Section 6(3), DPDP Rules 2025) are a structural innovation not required by GDPR — controllers offering services to Indian
users from November 2026 must register with or interface with DPDPA-compliant Consent Managers.
Verify current ANPD/DPDPA guidance for updated implementation timelines. [VERIFY]

---

## Consent Refresh Triggers

Identify whether the mechanism includes automated consent refresh for all applicable triggers.

### Mandatory Refresh Triggers

| Trigger                        | Description                                             | Refresh Required By                                                                    |
| ------------------------------ | ------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Purpose change**             | New processing purpose beyond original consent scope    | Before processing begins under new purpose                                             |
| **New data category**          | New categories of personal data to be collected         | Before collection begins                                                               |
| **New third-party recipients** | Named or categorised recipients change materially       | Before sharing with new recipients                                                     |
| **Withdrawal + re-engagement** | User withdrew consent; controller wishes to re-obtain   | Cannot presume consent revives; must re-obtain explicitly                              |
| **Controller identity change** | Merger, acquisition, restructuring affecting controller | Before processing under new controller identity (if not disclosed at original consent) |

### Recommended/Best Practice Refresh Triggers

| Trigger                            | Description                                                            | Recommended Practice                                                                        |
| ---------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Dormancy**                       | No interaction between controller and data subject for extended period | Refresh after 12-24 months of dormancy (depends on relationship type and contact frequency) |
| **CNIL specific**                  | For cookie consent in France                                           | Refresh every 6 months maximum per CNIL guidance                                            |
| **Material privacy policy change** | Significant changes to how data is processed                           | Proactive re-consent beyond policy notice alone                                             |
| **ICO guidance**                   | UK DPA recommendation                                                  | Consider refresh every 2 years as practical default                                         |

### Consent Refresh Mechanism Assessment

| Test                                                     | COMPLIANT                                | REQUIRES REMEDIATION                                                 |
| -------------------------------------------------------- | ---------------------------------------- | -------------------------------------------------------------------- |
| System can detect purpose changes and trigger re-consent | Automated trigger in CMP                 | Manual process only; no systematic tracking                          |
| Dormant consent monitoring in place                      | Automated dormancy alerts                | No dormancy monitoring                                               |
| Versioned consent records that enable comparison         | Each consent event records version       | Version not tracked; no change detection                             |
| Re-consent mechanism is as rigorous as original consent  | Full notice re-presented; genuine choice | Only a "we've updated our policy" email without re-consent mechanism |

---

## Classification System

### Per-Element Classification

Apply to each element assessed in Steps 5-9:

| Class                    | Definition                                                                                                                            | Action Required                                               |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **COMPLIANT**            | Element fully meets applicable legal requirements; no material gaps identified                                                        | Monitor; no immediate action                                  |
| **REQUIRES REMEDIATION** | Element partially meets requirements; gaps identified that pose regulatory risk but are not per se violations in every interpretation | Remediation within 3 months; legal counsel review recommended |
| **NON-COMPLIANT**        | Element fails to meet one or more clear legal requirements; regulatory violation identifiable with high confidence                    | Immediate remediation; DPA notification risk assessed         |

### Severity Tiering for Non-Compliant Findings

| Tier         | Criteria                                                                         | Example                                                                                   |
| ------------ | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **CRITICAL** | Clear, obvious violation; enforcement action risk; significant fine exposure     | Pre-ticked checkboxes; cookies firing before consent; no first-layer reject button        |
| **HIGH**     | Material non-compliance requiring prompt remediation; documented in DPA guidance | Asymmetric button styling; missing third-party names; withdrawal obstruction              |
| **MEDIUM**   | Non-compliance with best practice; gap in implementation                         | Missing cookie duration; no explicit consent duration disclosure; dormancy refresh absent |
| **LOW**      | Minor gap or ambiguity; unlikely to be primary enforcement focus                 | Borderline wording; incomplete documentation                                              |

### Overall Consent Mechanism Assessment

The overall mechanism is classified as:

- **COMPLIANT** — All six validity conditions met; no material dark patterns; cross-regime gaps minimal
- **REQUIRES REMEDIATION** — One or more conditions REQUIRES REMEDIATION; no CRITICAL violations
- **NON-COMPLIANT** — One or more conditions rated NON-COMPLIANT/CRITICAL; immediate action required

---

## Actionable Findings and Remediation

For each finding, produce a structured finding entry:

```
FINDING: [Reference number, e.g., F-001]
Element: [Which validity condition or dark pattern]
Classification: [COMPLIANT / REQUIRES REMEDIATION / NON-COMPLIANT]
Severity: [CRITICAL / HIGH / MEDIUM / LOW]
Regulatory basis: [GDPR Art. X; EDPB Guideline; enforcement precedent]
Evidence: [What was observed in the mechanism]
Enforcement risk: [Fine range; comparable enforcement action]
Remediation: [Specific, actionable steps to achieve compliance]
Compliant pattern: [What the implementation should look like]
Timeline: [Recommended remediation timeline]
```

### Example Finding Entry

```
FINDING: F-001
Element: Withdrawal parity (GDPR Art. 7(3))
Classification: NON-COMPLIANT
Severity: CRITICAL
Regulatory basis: GDPR Art. 7(3); EDPB Guidelines 05/2020 §3.5;
  CNIL v. Google (€150M, January 2022) — 5-click rejection vs. 1-click acceptance
Evidence: Accept All button on first-layer banner; Reject All accessible only via
  "Manage Cookies" > Preferences > Toggle all off > Save — 4 additional clicks
Enforcement risk: CNIL enforcement precedent up to €325M (Google, 2025);
  ICO formal enforcement possible for UK sites
Remediation: Add "Reject All" button to first-layer banner with identical styling,
  size, color contrast, and click depth as "Accept All" button
Compliant pattern: Two symmetrical buttons — "Accept all cookies" / "Reject all
  cookies" — same size, same color family, same visual weight, same position level
Timeline: Immediate — within 30 days
```

---

## Prioritization Framework

### Tier 1 — Critical / Immediate Regulatory Risk

Must fix within 30 days. These issues are per se violations documented in DPA enforcement:

- Pre-consent cookie/tracking firing before user interaction (universally enforced)
- No reject mechanism at all (consent banner offers only "Accept")
- Pre-ticked boxes on non-essential consent (Planet49 violation)
- Cookie wall without alternative (EDPB Guidelines 05/2020)
- Asymmetric click depth: 1-click accept vs. 3+ clicks reject (CNIL precedent)
- Missing first-layer reject button (CNIL/EDPB requirement)
- Processing special category data without explicit consent (Art. 9 violation)
- Children's service with no age gate below applicable threshold

### Tier 2 — High Priority / Regulatory Risk Within 90 Days

Fix within 3 months. These are documented compliance requirements with enforcement precedent:

- Asymmetric button styling (size, color, prominence)
- Missing third-party recipient names from consent notice (Planet49)
- Missing cookie duration disclosure (Planet49)
- No persistent withdrawal access (floating icon / footer link absent)
- Confirmshaming language (ICO: "almost always" a violation)
- Bundled consent across unrelated purposes
- No consent records / inadequate logging
- Employment consent used for routine processing
- Consent-or-pay without free alternative (LOPs)

### Tier 3 — Good Practice / Proactive Compliance

Address within 6 months. These represent best practice or compliance risk mitigation:

- Consent refresh mechanism for dormancy
- Double opt-in for email marketing
- Enhanced transparency for IAB TCF / vendor list
- Age verification enhancement beyond self-declaration
- Accessibility (WCAG 2.1) of consent banner
- CMP signal propagation audit
- Cross-regime consent variations documentation

---

## Citation Quality Gates

Run these five gates silently before delivering the audit report. If any gate fails, revise
before delivery.

| Gate           | Rule                                                                                                                  | Fail Action                                                       |
| -------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Source**     | Every finding cites a specific GDPR article, EDPB guideline, DPA decision, or enforcement case                        | Add citation or mark "[UNVERIFIED]"                               |
| **Format**     | Citations follow consistent, recognisable format (e.g., "EDPB Guidelines 05/2020, §3.1" or "CJEU C-673/17, para. 73") | Fix citation format                                               |
| **Currency**   | Each provision checked for amendments; DPA guidance verified as current                                               | Flag "[CHECK CURRENCY]" for provisions that may have been updated |
| **Domain**     | Analysis stays within the skill's regulatory scope; no overstatement of legal requirements                            | Remove or caveat claims that go beyond established authority      |
| **Confidence** | Uncertainty explicitly stated; probability levels expressed where genuinely uncertain                                 | Add confidence qualifier using Confidence Scoring scale           |

---

## Self-Interrogation for Critical and High-Severity Findings

For any finding classified CRITICAL or HIGH severity, apply this 3-pass review before delivery:

**Pass 1 — Legal Chain Integrity**: Does the non-compliance finding follow logically from the
cited legal authority? Would the relevant DPA actually reach this conclusion? Would the EDPB
Enforcement Tracker record of comparable fines support this classification? (e.g., "The CNIL
has specifically fined controllers €150M for asymmetric button design — CRITICAL is justified.")

**Pass 2 — Completeness**: Have all relevant GDPR articles, EDPB guidelines, national DPA
guidance, and enforcement decisions been considered? Are there exceptions or safe harbours
that might apply (e.g., strictly necessary cookie exemption; analytics exemption under CNIL)?
Have I considered whether there is a technical explanation for the finding that might be
non-compliance through misconfiguration rather than dark pattern design intent?

**Pass 3 — Challenge**: What is the strongest argument that this mechanism is actually compliant?
Under what interpretation might a DPA find it acceptable? Document the counter-argument
and explain why the finding nonetheless stands. (e.g., "Controller might argue button colors
reflect brand guidelines rather than intentional manipulation — but EDPB Guidelines 03/2022
focus on the effect, not the intent, making this argument unlikely to succeed.")

---

## Confidence Scoring

| Level        | Range     | Meaning                                                                         | Action                                                                                          |
| ------------ | --------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear statutory text; CJEU ruling; DPA enforcement decision directly on point   | State violation with full confidence                                                            |
| **High**     | 0.80–0.94 | Strong EDPB/ICO guidance; multiple DPA enforcement actions in same pattern area | State with brief caveat (e.g., "confirmed by EDPB Guidelines and multiple enforcement actions") |
| **Probable** | 0.60–0.79 | Good arguments from principle; limited specific enforcement                     | State with reasoning; note open question                                                        |
| **Possible** | 0.40–0.59 | Genuinely contested interpretation; DPA positions diverge                       | Flag for professional review; present both positions                                            |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                                                         | Do not assert; flag "[UNCERTAIN]"                                                               |

---

## Glass Box Audit Trail

Include the following YAML block in every consent mechanism audit report:

```yaml
glass_box:
  skill_name: "legalcode-consent-mechanism-review"
  audit_date: "[ISO 8601 date]"
  mechanism_type: "[cookie banner / sign-up flow / app permissions / etc.]"
  controller: "[Controller name or 'Not disclosed']"
  primary_jurisdiction: "[EU / UK / EU+UK / Multi-regime]"
  eu_applicable: true/false
  uk_applicable: true/false
  lgpd_applicable: true/false
  dpdpa_applicable: true/false
  us_applicable: true/false
  special_contexts:
    children: true/false
    special_categories: true/false
    employment: true/false
    consent_or_pay: true/false
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "[path] / Not created"
  overall_assessment: "COMPLIANT / REQUIRES REMEDIATION / NON-COMPLIANT"
  validity_conditions_assessed: 6
  dark_patterns_tested: "[number]"
  critical_findings: "[number]"
  high_findings: "[number]"
  medium_findings: "[number]"
  low_findings: "[number]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats]"
    - "Technical access: [live testing / screenshots / description only]"
    - "Consent logs: [reviewed / not reviewed / not available]"
  reviewer: "AI-assisted — requires qualified privacy counsel review before reliance"
```

---

## Anti-Patterns Catalogue

The following 25 anti-patterns represent the most common and most-fined consent mechanism
failures. Check each systematically.

| #     | Anti-Pattern                                                                                                  | GDPR Violation                                   | Enforcement Precedent                                                       | Severity |
| ----- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | --------------------------------------------------------------------------- | -------- |
| AP-01 | **Asymmetric Button Prominence** — Accept large/colored; Reject small/grey                                    | Art. 5(1)(a); Art. 7                             | CNIL v. Google €150M + €325M; Facebook €60M                                 | CRITICAL |
| AP-02 | **Asymmetric Click Depth** — 1 click to accept; 3+ clicks to reject                                           | Art. 7(3); Art. 5(1)(a)                          | CNIL v. Google (5 clicks to reject); CNIL v. TikTok €5M                     | CRITICAL |
| AP-03 | **Missing First-Layer Reject Button** — No reject in initial banner layer                                     | Art. 7 (freely given); Art. 5(1)(a)              | EDPB Cookie Banner Taskforce 2023; CNIL enforcement                         | CRITICAL |
| AP-04 | **Pre-Ticked Checkboxes** — Non-essential processing checked by default                                       | Art. 4(11); Recital 32; Art. 7                   | Planet49 (C-673/17); universally enforced                                   | CRITICAL |
| AP-05 | **Browsing/Scrolling as Consent** — "By continuing you accept cookies"                                        | Art. 4(11); Recital 32                           | Planet49; EDPB Guidelines 05/2020                                           | CRITICAL |
| AP-06 | **Confirmshaming** — Rejection phrased as harm to user                                                        | Art. 5(1)(a); Art. 7(1)                          | ICO: "almost always a violation"; EDPB Guidelines 03/2022                   | HIGH     |
| AP-07 | **Cookie Wall Without Alternative** — Service access requires consent                                         | Art. 7(1) (freely given); conditionality         | EDPB Guidelines 05/2020; Dutch DPA; Belgian DPA                             | CRITICAL |
| AP-08 | **Consent-or-Pay (LOP) Without Free Alternative** — Binary pay/consent for LOPs                               | Art. 7(1)                                        | EDPB Opinion 08/2024                                                        | CRITICAL |
| AP-09 | **Bundled Consent** — Multiple unrelated purposes in single checkbox                                          | Art. 4(11); Art. 7; EDPB Guidelines 05/2020      | Austrian DPA; EDPB §3.2                                                     | HIGH     |
| AP-10 | **Vague Purpose Descriptions** — "Improve your experience"; "partner ecosystem"                               | Arts. 13/14; Art. 7(2) (informed)                | Belgian DPA v. IAB Europe €250K                                             | HIGH     |
| AP-11 | **Undisclosed Third-Party Recipients** — No names or categories                                               | Arts. 13(1)(e)/14(1)(e); Planet49                | Planet49 (information requirement for third-party access)                   | HIGH     |
| AP-12 | **Missing Cookie Duration** — No disclosure of cookie lifetime                                                | Art. 13(2)(a); Planet49                          | Planet49 explicit holding on duration disclosure                            | HIGH     |
| AP-13 | **LI Claimed for Tracking/Advertising** — LI invoked to avoid consent for behavioural tracking                | Art. 6; Art. 5(1)(a)                             | LinkedIn €310M (2024); Meta €390M (2023)                                    | CRITICAL |
| AP-14 | **Withdrawal Obstruction** — No persistent withdrawal mechanism; buried in settings                           | Art. 7(3)                                        | TikTok €345M (Irish DPC, 2023); EDPB Guidelines 05/2020                     | CRITICAL |
| AP-15 | **Post-Rejection Nagging** — Repeated re-requests after explicit refusal                                      | Art. 5(1)(a); Art. 7(1)                          | EDPB Guidelines 03/2022 (Overloading)                                       | HIGH     |
| AP-16 | **Notice-Only Banner** — Only "OK" or "Got it" button; no accept/reject                                       | Art. 4(11)                                       | Universally enforced by all EU DPAs                                         | CRITICAL |
| AP-17 | **Deceptive Cookie Categorisation** — Marketing cookies labelled "necessary"                                  | Art. 5(1)(a); Arts. 13/14                        | EDPB Cookie Banner Taskforce Report 2023                                    | HIGH     |
| AP-18 | **Low-Contrast Reject Text** — Reject option rendered in low-contrast color                                   | Art. 5(1)(a); EDPB Guidelines 03/2022 (Stirring) | EDPB Guidelines 03/2022; CNIL enforcement                                   | HIGH     |
| AP-19 | **Processing Before Consent** — Non-essential cookies/pixels fire on page load                                | ePrivacy Art. 5(3); GDPR Art. 6                  | Universally enforced; ICO 2025 review found 67% of top 200 sites            | CRITICAL |
| AP-20 | **Withdrawal Not Effective** — Processing continues after consent withdrawal                                  | Art. 7(3)                                        | EDPB Guidelines 05/2020 §3.5                                                | CRITICAL |
| AP-21 | **Forced Account Creation to Refuse** — Rejection requires registration                                       | Art. 7(1) (freely given; detriment)              | EDPB Guidelines 05/2020                                                     | HIGH     |
| AP-22 | **Employee Consent for Employment Processing** — Routine employment data processing on consent basis          | Art. 7(1) (power imbalance)                      | EDPB Guidelines 05/2020 §3.1; Danish DPA hospital case 2023                 | HIGH     |
| AP-23 | **Regular Consent for Art. 9 Special Category Data** — Standard tick box for health/biometric/etc.            | Art. 9(2)(a) (explicit consent required)         | Danish DPA gym facial recognition case 2024                                 | CRITICAL |
| AP-24 | **TCF/CMP Opacity** — Consent signals distributed to hundreds of adtech vendors without meaningful disclosure | Arts. 5(1)(a); 13/14; 7(2)                       | Belgian DPA v. IAB Europe €250K (upheld Brussels Court of Appeal, May 2025) | HIGH     |
| AP-25 | **Legal Basis Switching After Rejection** — Switching to LI or contractual necessity after consent refused    | Art. 5(1)(a); Art. 7; purpose limitation         | Meta €390M (Irish DPC, 2023) — LB switching is itself a violation           | CRITICAL |

---

## Writing Standards

Apply these standards before delivering the audit report:

1. **Plain language**: Use accessible, non-technical language in remediation recommendations.
   Write for a product manager and legal counsel simultaneously.

2. **Active voice**: "The banner fails to display a Reject All button at the first layer"
   not "A Reject All button is absent from the first banner layer."

3. **Specific evidence**: Quote the exact observed language or describe the exact visual
   element. "The 'Accept All' button is rendered in #007AFF blue at 16px with a filled
   background; the 'Manage Cookies' link is rendered in #6C757D grey at 12px as a hyperlink"
   not "the buttons look different."

4. **Enforcement-anchored severity**: For every CRITICAL or HIGH finding, cite a specific
   enforcement case. DPAs have multi-million euro enforcement records to draw on.

5. **Remediation specificity**: Each remediation recommendation must describe the target state,
   not just the problem. "Add a 'Reject all' button identical in size, styling, and position
   to the 'Accept all' button on the first layer of the consent banner" not "make the reject
   button more visible."

6. **Confidence qualifiers**: Any legal claim that is not anchored in a cited statutory text,
   EDPB guideline, or enforcement decision must carry a confidence qualifier or [VERIFY] tag.

7. **Jurisdiction specificity**: Do not state EU requirements as universal. State: "Under GDPR
   and EDPB guidance, [requirement]" not "you must [requirement]."

8. **No hallucinated citations**: Never invent a fine amount, a case citation, or a DPA
   decision. If uncertain of a specific citation, use general authority (e.g., "EDPB Guidelines
   05/2020") rather than inventing a specific paragraph number.

---

## External Tool Integration

**With legalcode-mcp connected:**

- In Step 4, search for recent DPA enforcement decisions in the relevant sector
- Verify current EDPB guidance versions and any updates
- Search for sector-specific guidance (e.g., healthcare, financial services, children's apps)
- Retrieve national DPA guidance documents for non-standard member states
- Verify current national children's age threshold if in doubt

**Without legalcode-mcp:**

- Proceed with training data knowledge
- Mark all DPA guidance references with [VERIFY] for currency
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Recommend that counsel verify current guidance before reliance on the audit findings
- The skill remains fully functional for structure and dark pattern identification; legal
  authority depth is reduced

---

## Output Format Template

````markdown
# Consent Mechanism Audit Report

**Controller**: [Name or "Not disclosed"]
**Mechanism audited**: [Cookie banner / Sign-up flow / App permissions / etc.]
**Date of audit**: [Date]
**Primary jurisdiction(s)**: [EU/UK/LGPD/DPDPA/CCPA]
**Overall assessment**: [COMPLIANT / REQUIRES REMEDIATION / NON-COMPLIANT]

---

## Executive Summary

[2-3 paragraph summary of findings. State the overall assessment, the most critical
finding(s), enforcement exposure level, and top 3 immediate actions.]

**Critical findings**: [N]
**High priority findings**: [N]
**Medium findings**: [N]
**Compliant elements**: [N]

---

## Regulatory Scope

Applicable frameworks:

- [✓/✗] EU GDPR + EDPB Guidelines 05/2020 / 03/2022
- [✓/✗] UK GDPR + PECR
- [✓/✗] Brazil LGPD
- [✓/✗] India DPDPA
- [✓/✗] US CCPA/CPRA

Special contexts:

- [✓/✗] Children's consent (Art. 8)
- [✓/✗] Special category data (Art. 9)
- [✓/✗] Employment context
- [✓/✗] Consent-or-pay / cookie wall

---

## Validity Assessment — Element Scorecard

| #   | Element                         | Classification | Severity |
| --- | ------------------------------- | -------------- | -------- |
| 1   | Freely given                    |                |          |
| 2   | Specific / granularity          |                |          |
| 3   | Informed                        |                |          |
| 4   | Unambiguous indication          |                |          |
| 5   | Withdrawal parity (Art. 7(3))   |                |          |
| 6   | Proof / audit trail (Art. 7(1)) |                |          |

---

## Dark Pattern Analysis

| Dark Pattern   | EDPB Category                                                 | Present? | Severity               | Authority  |
| -------------- | ------------------------------------------------------------- | -------- | ---------------------- | ---------- |
| [Pattern name] | [Overloading/Skipping/Stirring/Hindering/Fickle/Left in Dark] | [Yes/No] | [CRITICAL/HIGH/MEDIUM] | [Citation] |
| ...            |                                                               |          |                        |            |

---

## Detailed Findings

### CRITICAL Findings

#### F-001: [Finding title]

[Full finding entry per structured template above]

### HIGH Priority Findings

#### F-00X: [Finding title]

...

### MEDIUM Findings

#### F-00X: [Finding title]

...

---

## Cross-Regime Gap Analysis

[If multi-regime applicable]

| Regime       | Gap vs. EU Mechanism | Action Required |
| ------------ | -------------------- | --------------- |
| Brazil LGPD  | [Gap description]    | [Action]        |
| India DPDPA  | [Gap description]    | [Action]        |
| US CCPA/CPRA | [Gap description]    | [Action]        |

---

## Consent Refresh Assessment

| Trigger                                             | Mechanism in Place? | Classification |
| --------------------------------------------------- | ------------------- | -------------- |
| Purpose change                                      |                     |                |
| New data categories                                 |                     |                |
| New third-party recipients                          |                     |                |
| Dormancy (12-24 months)                             |                     |                |
| [CNIL 6-month cookie refresh, if France applicable] |                     |                |

---

## Prioritised Remediation Action Plan

### Tier 1 — Immediate (0–30 days)

| #   | Action            | Finding Ref | Estimated Effort |
| --- | ----------------- | ----------- | ---------------- |
| 1.  | [Specific action] | F-00X       | [hours/days]     |

### Tier 2 — Near-term (30–90 days)

| #   | Action | Finding Ref | Estimated Effort |
| --- | ------ | ----------- | ---------------- |

### Tier 3 — Longer-term (90–180 days)

| #   | Action | Finding Ref | Estimated Effort |
| --- | ------ | ----------- | ---------------- |

---

## Compliant Design Patterns to Implement

[For each CRITICAL/HIGH finding, include the target compliant state:]

### Pattern 1: Equal Prominence Accept/Reject Buttons

[Description of what the compliant implementation looks like, with visual specifications]

### Pattern 2: First-Layer Reject Mechanism

...

### Pattern 3: Granular Purpose Controls

...

---

## Glass Box Audit Trail

```yaml
[Full YAML from Glass Box Audit Trail section above]
```
````

---

## Next Steps

1. [Immediate action — Tier 1 item #1]
2. [Recommended legal counsel review for [specific element]]
3. [Technical implementation steps for CMP reconfiguration]
4. [Consider: DPA pre-engagement / voluntary self-reporting if significant violations found]
5. [Complementary skills: legalcode-cookie-compliance-audit for pre-consent blocking test]

---

## Limitations and Professional Review

This audit was produced using AI-assisted analysis of the consent mechanism as provided.
It does not constitute legal advice. Limitations include:

- [Technical access scope: live testing / screenshots / description only]
- [Jurisdiction: limited to frameworks assessed above; local counsel required for [jurisdiction]]
- [Special contexts: [any not assessed due to scope]]
- All GDPR, EDPB, and DPA references carry hallucination risk — verify against primary sources
- Laws and DPA guidance evolve: verify currency of all cited instruments before reliance

```

---

## Provenance

Created by Legalcode (2026-03-02). Original synthesis using the 2-agent research pipeline.
Agent 1 (Structural & Legal Research Analyst) covered GDPR Article 7 framework, EDPB Guidelines
05/2020 and 03/2022, Planet49 (CJEU C-673/17) ruling analysis, UK ICO guidance, CNIL enforcement
decisions, Brazil LGPD Articles 7-8-11-14, India DPDP Act 2023 and DPDP Rules 2025, GDPR
Article 8 children's consent national thresholds, CCPA/CPRA opt-in requirements, and consent
refresh trigger doctrine. Agent 2 (Dark Patterns & Prompt Engineering Analyst) covered the
EDPB six-category dark pattern taxonomy, CMA/ICO joint OCA taxonomy, Planet49 five key
holdings, 25-item anti-patterns catalogue, enforcement actions (Google, Meta, TikTok, LinkedIn,
IAB Europe), compliant design patterns, and IAB TCF/CMP implementation failures.

**Key sources consulted** (verify currency before reliance):
- EDPB Guidelines 05/2020 on Consent under Regulation 2016/679 (v1.1)
- EDPB Guidelines 03/2022 on Deceptive Design Patterns (v2.0, February 2023)
- EDPB Opinion 08/2024 on Valid Consent in the Context of Consent or Pay Models
- EDPB Cookie Banner Taskforce Report (January 2023)
- CJEU Case C-673/17 (Planet49), judgment of 1 October 2019
- ICO Guidance on Cookies and Similar Technologies (December 2024)
- CNIL Cookie Guidelines and enforcement decisions (2022-2025)
- Belgian DPA v. IAB Europe (February 2022, upheld Brussels Court of Appeal May 2025)
- Irish DPC v. TikTok (€345M, September 2023)
- Irish DPC v. Meta Ireland (€390M, January 2023)
- Irish DPC v. LinkedIn Ireland (€310M, October 2024)
- ICO/CMA Joint Position Paper on Harmful Design in Digital Markets (August 2023)
- LGPD Law No. 13,709/2018 (Brazil)
- DPDP Act 2023 and DPDP Rules 2025 (India)
- CCPA/CPRA Cal. Civ. Code §1798.100 et seq.
- Nouwens et al., "Dark Patterns after the GDPR" (MIT/CHI 2020)

This is a Legalcode original synthesis. No external skills were imported. The skill occupies
a defined position in the legalcode privacy skill family — between `legalcode-gdpr-legal-basis-
assessment` (selecting the correct basis) and `legalcode-cookie-compliance-audit` (auditing
tracking technology implementations). Together, these three skills form the complete GDPR
consent compliance chain: basis selection → mechanism validity → technical implementation.
```
