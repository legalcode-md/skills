---
name: legalcode-eu-dma-compliance
description: Assess compliance with the EU Digital Markets Act (Regulation (EU) 2022/1925, "DMA") for
  any organisation that may be a gatekeeper or that provides products or services on a designated gatekeeper's
  core platform service. Use when advising a potential gatekeeper on designation risk, conducting a DMA
  gap analysis, preparing an annual compliance report, responding to a Commission information request,
  building a DMA compliance programme from scratch, advising a third-party developer or business user
  on their DMA rights, or assessing enforcement exposure after the April 2025 Apple/Meta fines.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Assess compliance with the EU Digital Markets Act (Regulation (EU) 2022/1925, "DMA") for any organisation that may be a gatekeeper or that provides products or services on a designated gatekeeper's core platform service. Covers: gatekeeper designation thresholds (Art. 3), core platform service (CPS) classification (Art. 2), Art. 5 per se prohibitions (data combination, MFN/parity clauses, anti-steering, multi-homing restrictions, exclusive pre-installation), Art. 6 contestability obligations (self-preferencing, FRAND access, sideloading/alternative app stores, data portability, interoperability of hardware features), Art. 7 messaging interoperability (NICS cross-platform communication), Art. 8 compliance framework establishment, Art. 11 annual compliance reporting, Art. 13 anti-circumvention, Art. 15 consumer profiling audit, Art. 18 systematic non-compliance and structural remedies, Art. 28 compliance officer and function requirements, Commission enforcement (fines up to 10%/20% of global turnover), interaction with GDPR/competition law, and designated gatekeeper CPS mapping. Use when advising a potential gatekeeper on designation risk, conducting a DMA gap analysis, preparing an annual compliance report, responding to a Commission information request, building a DMA compliance programme from scratch, advising a third-party developer or business user on their DMA rights, or assessing enforcement exposure after the April 2025 Apple/Meta fines.


# Legalcode EU Digital Markets Act Compliance Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted DMA compliance assessment.
> It does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional — ideally one experienced in EU competition law and digital regulation —
> before reliance. The DMA is a live and rapidly evolving regulatory framework: Commission
> enforcement decisions, non-compliance determinations, binding interoperability orders, and
> implementing acts are issued regularly. Statutory and regulatory references cited from
> memory carry hallucination risk — verify against authoritative sources (EUR-Lex,
> digital-markets-act.ec.europa.eu, and Commission enforcement notices) before acting on them.

## Purpose and Scope

This skill assesses compliance with Regulation (EU) 2022/1925 (Digital Markets Act) for
organisations operating core platform services in or affecting the European Union.

**Covers:**

- Gatekeeper designation threshold analysis (Art. 3 quantitative and qualitative criteria)
- Core Platform Service (CPS) classification across all 10 categories (Art. 2)
- Art. 5 per se prohibited conduct: data combination without consent, MFN/parity clauses,
  anti-steering, multi-homing restrictions, exclusive pre-installation, access-restriction
- Art. 6 contestability obligations: self-preferencing, FRAND access, sideloading,
  alternative app stores, real-time data portability, hardware/software interoperability
- Art. 7 messaging interoperability for number-independent interpersonal communications
  services (NICS)
- Art. 8 compliance framework and interoperability specifications
- Art. 11 annual compliance reporting obligations
- Art. 13 anti-circumvention prohibition (structural, contractual, technical, and UI-based)
- Art. 15 consumer profiling techniques audit and transparency
- Art. 18 systematic non-compliance: enhanced remedies and structural measures
- Art. 26 Commission investigative powers and market investigations
- Art. 28 compliance officer and function requirements
- Enforcement exposure: fines (up to 10%/20% global turnover), periodic penalties (5% daily)
- DMA–GDPR interplay (Art. 5(2) data combination and GDPR consent requirements)
- DMA–competition law interaction (Art. 102 TFEU lex specialis analysis)
- Business user and third-party developer DMA rights
- Remediation roadmapping and compliance programme design

**Does not:**

- Provide legal advice or replace qualified DMA/competition law counsel
- Cover the Digital Services Act (DSA) content-moderation obligations (see legalcode-eu-dsa-compliance)
- Assess individual content moderation decisions
- Substitute for the Art. 15 independent profiling audit by an accredited third party
- Cover national competition law enforcement (DMA enforcement is Commission-exclusive)

## Jurisdiction and Governing Law

This is an EU-specific skill governed by Regulation (EU) 2022/1925, which applies directly
and without transposition in all 27 EU Member States.

**Key regulatory instruments:**

- Regulation (EU) 2022/1925 (DMA) — in force 1 November 2022; applicable 2 May 2023
- Gatekeeper designations: first six designated 6 September 2023; Apple iPadOS April 2024;
  Booking.com May 2024
- Compliance deadline: 7 March 2024 for Arts. 5, 6, and 7 obligations
- Commission Implementing Regulation on Art. 7 interoperability technical specifications
  [VERIFY current status on EUR-Lex]
- Commission Decision establishing the DMA Gatekeepers' Portal

**Territorial reach:**
The DMA applies to any gatekeeper providing core platform services to business users located
in the EU or end users located in the EU, regardless of where the gatekeeper is established
(Art. 1(2)). There is no EU establishment requirement — a non-EU gatekeeper with sufficient
EU user scale is fully subject to DMA obligations.

**Enforcement authority:**
Unlike the DSA, **the European Commission is the sole enforcement authority** for the DMA.
Member States have no direct DMA enforcement power, though they may refer cases to the
Commission and provide investigative assistance.

[EU-SPECIFIC] The DMA is a regulation — it applies uniformly across all Member States
without national transposing legislation. National competition authorities may, however,
investigate the same conduct under national competition law, subject to the lex specialis
principle (see Obligation Analysis Framework below).

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
gatekeeper status or compliance posture, the workflow pauses and asks when:

- Designation status is uncertain and determines the entire obligation set
- The organisation operates across multiple CPS categories with different obligation clusters
- GDPR consent architecture is relevant to an Art. 5(2) assessment
- Risk tolerance or business context would affect remediation prioritisation
- The assessment is for the gatekeeper itself versus a third-party business user seeking
  to exercise their DMA rights

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

### Step 1: Accept the Assessment Scope

Accept the assessment scope in any of these formats:

- **Compliance questionnaire**: Answers to structured questions about platform type, user
  counts, revenue, CPS architecture, existing compliance measures, and enforcement history
- **Existing compliance documentation**: Internal DMA gap analyses, compliance reports,
  legal opinions, or Commission correspondence
- **Service description**: Free-text description of the platform, its services, and
  business model
- **Annual report or press release**: For designated gatekeepers, publicly available
  compliance reports submitted under Art. 11

If no information is provided, prompt the user to supply a description of the platform
and its approximate EU monthly active user count and annual EU revenue.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user these questions. Skip any already answered:

1. **Perspective**: Who is this assessment for?
   - Options: A potential or designated gatekeeper (first-party compliance), A third-party
     business user or developer asserting DMA rights, A business user in contract negotiations
     with a gatekeeper, An investor or M&A diligence team, A regulator or policymaker
   - _Why this matters_: A gatekeeper-side assessment focuses on obligation compliance; a
     business-user-side assessment focuses on enforcing DMA rights (interoperability
     requests, data access, anti-steering protections).

2. **Designation status**: Has the organisation been designated as a gatekeeper?
   - Options: Yes — formally designated (provide designation date and designated CPS),
     No — not yet designated but assessing risk, Under Commission investigation for
     designation, Unknown
   - _Why this matters_: Only designated gatekeepers have DMA obligations; undesignated
     organisations face only designation risk analysis.

3. **CPS type(s) operated**: Which core platform services does the organisation provide?
   - Options (multi-select): Online intermediation service (app store, marketplace),
     Online search engine, Online social network, Video-sharing platform, Messaging/NICS,
     Operating system, Web browser, Virtual assistant, Cloud computing, Online advertising
   - _Why this matters_: Each CPS has a distinct obligation cluster; messaging NICS
     triggers Art. 7 interoperability; advertising triggers Art. 5(7); OS/browsers trigger
     sideloading and default-setting obligations.

4. **Assessment objective**: What must this assessment produce?
   - Options: Initial gap analysis for a new compliance programme, Pre-Commission inspection
     readiness review, Response to a Commission information request (Art. 21), Annual
     compliance report preparation (Art. 11), Enforcement exposure quantification after a
     preliminary non-compliance finding, Third-party rights enforcement advisory, Other
   - _Why this matters_: Determines depth, output format, and urgency framing.

5. **Prior compliance work**: Has the organisation already implemented DMA measures?
   - Options: No measures in place, Partial measures (documentation available), Full initial
     programme in place, Prior Commission engagement on compliance approach
   - _Why this matters_: A gap analysis over existing measures is more efficient than
     building from scratch; prior Commission engagement creates evidence of good faith.

6. **GDPR consent architecture** (if Art. 5(2) data combination is relevant):
   - Options: Separate consent mechanism in place per CPS, "Consent or pay" model,
     Legitimate interest as legal basis, No consent mechanism yet, Unknown
   - _Why this matters_: The April 2025 Meta fine of EUR 200 million turned on whether
     the consent mechanism under Art. 5(2) was genuinely free — GDPR and DMA consent
     requirements must be analysed together.

If the user provides partial context, proceed with what is available and **state
assumptions explicitly** at the outset of the analysis.

### Step 3: Gatekeeper Designation Threshold Analysis

If the organisation has not yet been formally designated, assess designation risk by
applying the Art. 3 threshold framework.

**Quantitative thresholds (Art. 3(2)) — all three must be satisfied for presumption:**

| Threshold                    | Test                                                                                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Revenue/market cap           | EU annual revenue ≥ EUR 7.5 billion in each of the last 3 financial years, OR average market capitalisation ≥ EUR 75 billion in the last financial year |
| Monthly active end users     | ≥ 45 million monthly active end users in the EU in the last financial year, for the same CPS in at least 3 Member States                                |
| Annual active business users | ≥ 10,000 annual active business users established in the EU, for the same CPS                                                                           |

**Rebuttable presumption:** If all three quantitative thresholds are met, the qualitative
criteria (entrenched and durable gatekeeper position; significant impact on the internal
market) are presumed satisfied. The gatekeeper bears a substantial burden to rebut.

**Alternative qualitative designation (Art. 3(8)):** The Commission may designate a
company meeting only the qualitative criteria after a market investigation considering:

- Turnover and market capitalisation relative to the CPS market
- Number and switching behaviour of business users and end users
- Network effects, data advantages, and economies of scale
- Degree of multi-homing, lock-in, and vertical integration

**⟁ CLARIFY** — If the organisation is near (within 20%) of a quantitative threshold, ask:

- "The EU monthly active user count is within range of the 45-million threshold. How
  confident are you in this estimate? Methodological choices in user counting can push the
  organisation above or below the threshold."
- "Revenue figures cross the EUR 7.5 billion threshold in some years but not others. Do
  you have audited figures for all three financial years?"

**Designation timeline:**

- Organisations meeting thresholds must notify the Commission within 2 months (Art. 3(3))
- Failure to self-notify is itself an infringement
- Commission has 45 business days to assess and open a market investigation for designation

### Step 4: Gather Current DMA Regulatory Authority

Use **legalcode-mcp** to gather current DMA regulatory material for this assessment.

**Research process:**

1. Search for: the DMA full text (Regulation (EU) 2022/1925), any implementing regulations,
   Commission guidelines, non-compliance decisions, and enforcement notices relevant to the
   CPS type(s) under assessment.

2. Search specifically for: any Commission decisions relating to the gatekeeper or CPS under
   assessment; any binding interoperability specifications issued under Art. 8; any Art. 15
   profiling audit templates issued by the Commission; the most recent designated gatekeepers
   list at digital-markets-act.ec.europa.eu/gatekeepers-portal.

3. Save the most relevant results to a local reference file:

   ```
   /tmp/legalcode-dma-authority.md
   ```

   Structure as:

   ```markdown
   # DMA Regulatory Authority Reference

   ## Date: [date]

   ## Gatekeeper / CPS under assessment: [name]

   ### DMA Text References

   - [Article, paragraph, current text or summary]

   ### Commission Decisions and Non-Compliance Findings

   - [Decision, date, violation, fine or remedy]

   ### Implementing Regulations and Guidelines

   - [Instrument, date, relevance]

   ### Enforcement Tracker

   - [Entity, Art. under investigation, status, outcome if known]
   ```

4. Use this reference file throughout the obligation analysis. Mark any legalcode-mcp
   citation as VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**

- Mark all statutory and decision references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed using the obligation framework below, which incorporates the research conducted
  in the creation of this skill

### Step 5: CPS Classification and Obligation Mapping

Map the organisation's services to the DMA's 10 CPS categories and identify the applicable
obligation cluster for each.

**⟁ CLARIFY** — If the organisation's service architecture spans multiple CPS categories,
or if there is ambiguity about whether a service qualifies as a given CPS type, ask:

- "The service combines a search engine with a shopping comparison tool. For DMA purposes,
  these may be treated as separate CPS requiring separate obligation analysis. Should I
  assess each component separately?"
- "The messaging product is bundled with a social network. Does the combined product meet
  the NICS threshold, or only the social network component? This affects Art. 7 interoperability."

| CPS Category                                   | Key Obligations Triggered                                                                                                                                            |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Online intermediation (app store, marketplace) | Art. 5(1)(a) pre-installation; Art. 5(3)-(5) off-platform pricing/access; Art. 6(4) FRAND access; Art. 6(5) self-preferencing; Art. 6(7) third-party app sideloading |
| Online search engine                           | Art. 6(5) self-preferencing in results; Art. 6(11) ranking data access; Art. 6(12) advertising data access                                                           |
| Online social network                          | Art. 5(2) data combination; Art. 6(9) data portability; Art. 6(13) profiling consent interface                                                                       |
| Video-sharing platform                         | Art. 5(2) data combination; Art. 6(9) portability; Art. 6(12) advertising transparency                                                                               |
| Messaging / NICS                               | Art. 7 interoperability (3-month deadline per request); Art. 5(2) data combination                                                                                   |
| Operating system                               | Art. 5(1)(a) pre-installation/defaults; Art. 6(3) hardware/software feature access; Art. 6(7) third-party app installation                                           |
| Web browser                                    | Art. 5(1)(a) default browser; Art. 6(3) API access; Art. 6(7) extension installation                                                                                 |
| Virtual assistant                              | Art. 5(1)(a) pre-installation; Art. 6(3) hardware integration access                                                                                                 |
| Cloud computing                                | Art. 6(4) FRAND interoperability; Art. 6(9) data portability                                                                                                         |
| Online advertising                             | Art. 5(2) cross-service data; Art. 6(8) real-time price transparency; Art. 6(9) advertiser data access                                                               |

### Step 6: Article 5 Per Se Obligations Assessment

Assess compliance with the Art. 5 quasi-automatic prohibitions. These are **not susceptible
to further specification or justification** — any deviation is a per se infringement.

For each prohibition, make a binary determination: **COMPLIANT** or **NON-COMPLIANT**.

#### Art. 5(1)(a) — Exclusive Pre-Installation and Default-Setting Prohibition

- The gatekeeper must not require exclusive pre-installation of its own CPS on devices
  operating its OS or browser
- End users must be able to change default settings to competing services through a
  neutral and easy-to-use selection screen (choice screen)
- **Assessment questions:**
  - Does the OS ship with non-removable, exclusively pre-installed first-party applications?
  - Is there a genuine and neutral default-selection mechanism for search, browser, voice
    assistant, and similar services?
  - Are default settings changed back to first-party services after OS updates?

#### Art. 5(2) — Personal Data Combination Without Consent

- The gatekeeper must not combine personal data from different CPS or from sign-in services
  it provides, without obtaining separate, explicit, and freely-given consent
- **Assessment questions:**
  - Are distinct consent mechanisms in place for each CPS's data use?
  - Is consent genuinely optional — i.e., does the service function meaningfully for users
    who do not consent to cross-service data combination?
  - Is a "consent or pay" mechanism in use? [NOTE: The April 2025 Meta fine (EUR 200M) held
    that a "consent or pay" binary that forces users to pay to avoid profiling does not
    constitute freely-given consent under Art. 5(2). [VERIFY this precedent has not been
    reversed on appeal.]]
  - Is the GDPR consent architecture aligned? Art. 5(2) consent requirements are calibrated
    with GDPR Art. 7 (freely given, specific, informed, unambiguous, separately given).

#### Art. 5(3) — Preventing Alternative Sales Channels

- Business users must be able to offer the same products and services at different prices
  or conditions through third-party intermediation services or direct channels
- **Assessment questions:**
  - Do gatekeeper platform terms prohibit or penalise business users from offering lower
    prices or better conditions on competing platforms or direct channels?
  - Are MFN/price-parity clauses imposed on business users? [These are per se prohibited
    under Art. 5(3) as applied in EU competition enforcement.]

#### Art. 5(4) — Anti-Steering: Communication and Promotion Rights

- Business users must be able to communicate with and direct end users acquired via the CPS
  to offers outside the gatekeeper's ecosystem, free of charge
- **Assessment questions:**
  - Do app store terms prohibit developers from displaying links to external payment options?
  - Are developers permitted to inform users that the same product is available at a lower
    price outside the platform?
  - [NOTE: The April 2025 Apple fine (EUR 500M) turned on App Store terms that prohibited
    developers from "steering" users to external purchases. [VERIFY appeal status.]]

#### Art. 5(5) — End User Access to Content Acquired Outside Platform

- End users must be able to access content, subscriptions, features, or services acquired
  via a business user's application or service outside the platform
- **Assessment questions:**
  - Can users access in-app subscriptions and content purchased directly from a developer
    through any channel, without being forced to re-purchase via the platform?

#### Art. 5(6) — Multi-Homing Restrictions

- The gatekeeper must not technically restrict business users from offering identical
  products or services simultaneously on competing platforms
- **Assessment questions:**
  - Are there technical or contractual barriers to business users deploying their service
    on multiple platforms concurrently?
  - Do terms prohibit or penalise simultaneous presence on competing app stores, marketplaces,
    or operating systems?

#### Art. 5(7) — Exclusive Identification and Authentication Service

- The gatekeeper must not require business users to use any of the gatekeeper's
  identification services as a condition of using its CPS
- **Assessment questions:**
  - Is "Sign in with [gatekeeper]" required as the only login method for third-party apps?
  - Are alternative identity/authentication providers technically or contractually excluded?

### Step 7: Article 6 Contestability Obligations Assessment

Assess compliance with the Art. 6 obligations, which are susceptible to further
specification through Commission decisions. Good-faith implementation and documented
compliance efforts are relevant to enforcement outcomes.

For each obligation, classify: **COMPLIANT**, **PARTIAL** (with gaps identified), or
**NON-COMPLIANT** (with specific deficiencies described).

#### Art. 6(3) — Hardware and Software Feature Interoperability

- Operating systems and hardware gatekeepers must provide FRAND access to OS, hardware,
  and software features (notifications, near-field communications, near-field proximity,
  gesture control, voice, biometrics, etc.) to third-party providers for interoperability
- **Assessment questions:**
  - Do third-party applications and services have access to hardware/software APIs on equal
    terms to the gatekeeper's own applications?
  - Are API access conditions documented and published?
  - Is there a dispute resolution mechanism for third parties denied access?

#### Art. 6(4) — FRAND Access for Business Users

- Business users and competitors must receive access to the gatekeeper's CPS on fair,
  reasonable, and non-discriminatory (FRAND) terms
- App store developers, advertisers, and competing services must have access on FRAND
  terms to ranking, search, and platform infrastructure
- **Assessment questions:**
  - Are access terms documented and published for third-party developers?
  - Are there discernible differences in access quality, speed, or cost between
    the gatekeeper's own services and competing third-party services?
  - Is there an accessible process for third parties to request access and resolve disputes?

#### Art. 6(5) — Self-Preferencing Prohibition

- The gatekeeper must not rank or treat its own products, services, or content more
  favourably than equivalent third-party products, services, or content in ranking,
  display, or algorithmic treatment
- **Assessment questions:**
  - Do search results, recommendation systems, or feed algorithms apply identical criteria
    to first-party and third-party content?
  - Is ranking methodology auditable and transparent to third parties?
  - Are any placement or labelling advantages afforded to the gatekeeper's own products
    (e.g., auto-populated first-party results, dedicated placement zones)?

#### Art. 6(7) — Sideloading and Alternative App Stores

- For OS gatekeepers: end users must be able to install software applications from sources
  other than the gatekeeper's app store ("sideloading")
- Developers must be able to distribute applications through alternative app stores
- **Assessment questions:**
  - Is sideloading technically enabled on the OS?
  - Are there "security warnings" or friction mechanisms that disproportionately
    discourage users from sideloading? [UI friction that effectively prevents sideloading
    may constitute anti-circumvention under Art. 13(4).]
  - Are alternative app stores permitted to operate on the OS on equal technical terms?

#### Art. 6(8) — Real-Time Auction and Pricing Transparency for Advertisers

- Advertisers and publishers must have access to performance measurement tools and
  real-time pricing data for the gatekeeper's advertising services
- **Assessment questions:**
  - Are advertisers provided with real-time price and auction data sufficient to evaluate
    the value of their campaigns independently?
  - Is there a third-party verification mechanism for advertising effectiveness?

#### Art. 6(9) — Real-Time Data Portability

- End users and business users must be provided continuous, real-time data portability
  through high-quality technical interfaces (APIs), free of charge
- Scope: all data generated through use of the CPS (usage data, content data,
  behavioural data, derived insights)
- **Assessment questions:**
  - Is a publicly documented API available for data export?
  - Is export available in a machine-readable, interoperable format?
  - Are there throttling, rate-limiting, or technical restrictions that impair
    real-time continuous access?
  - Can business users port data to competing platforms without degradation?

#### Art. 6(11) — Search Ranking and Query Data Access

- For search engine gatekeepers: provide access to ranking, query, click, and view data
  to competing search engines on FRAND terms
- **Assessment questions:**
  - Is ranking methodology documented and accessible to competing search engines?
  - Is query, click, and view data available to third-party search providers on FRAND terms?

#### Art. 6(12) — Online Advertising Data Access

- Advertisers and publishers must be provided access to price, fee, and remuneration
  data for each advertising service of the gatekeeper
- **Assessment questions:**
  - Are advertising fee structures transparent and accessible to advertisers and publishers?
  - Can advertisers independently verify the fees charged and the value delivered?

#### Art. 6(13) — GDPR-Compliant Consent Interface for Profiling

- The gatekeeper must not process end-user personal data for targeted advertising unless
  the user has given explicit, specific, and freely-given consent under Art. 6(13) DMA
  and GDPR Art. 6(1)(a)
- **Assessment questions:**
  - Is there a granular, per-purpose consent interface for advertising profiling?
  - Is consent withdrawal as easy as consent grant?

### Step 8: Article 7 Messaging Interoperability Assessment

Article 7 applies only to gatekeepers providing **number-independent interpersonal
communications services (NICS)** (messaging, voice, or video calling not dependent on
publicly assigned phone numbers). If NICS is not a designated CPS, skip this step.

**Mandatory interoperability requirements:**

| Functionality             | Deadline                                | Technical Requirement                                      |
| ------------------------- | --------------------------------------- | ---------------------------------------------------------- |
| One-to-one text messaging | 3 months after interoperability request | Interoperability with requesting third-party NICS provider |
| One-to-one voice calls    | 3 months after request                  | Cross-platform voice calling                               |
| One-to-one video calls    | 3 months after request                  | Cross-platform video calling                               |
| Group messaging           | 2 years from designation                | Interoperable group chats                                  |
| Group voice/video         | 4 years from designation                | Interoperable group calls                                  |

**Assessment questions:**

- Has the gatekeeper published technical specifications and documentation for third-party
  NICS providers to request interoperability?
- Have any interoperability requests been received? Have they been implemented within the
  3-month deadline?
- Are end-to-end encryption and security standards maintained across interoperable services?
  [Art. 7(2) requires that the security level of the service is maintained.]
- Is the minimum data principle observed: only strictly necessary personal data is exchanged
  in the interoperability technical interface?
- Are interoperability endpoints documented on a publicly accessible technical portal?

**⟁ CLARIFY** — If the gatekeeper uses end-to-end encryption (E2EE) and has received an
interoperability request, ask:

- "The interoperability obligation must maintain E2EE where applicable. Has the organisation
  assessed the technical feasibility of federated E2EE across different providers (e.g.,
  Signal protocol extensions, MLS standard)? The Commission's position is that E2EE is
  achievable through technical solutions — non-compliance cannot be justified by encryption
  concerns alone."

### Step 9: Compliance Function and Transparency Obligations

#### Art. 28 — Compliance Officer and Function

- Gatekeepers must establish an **independent compliance function** with:
  - A head of compliance function with sufficient authority and stature
  - Direct reporting access to the board/management body
  - Sufficient budget and personnel
  - Responsibility for monitoring, overseeing, and reporting on DMA compliance
  - Authority to raise non-compliance risks to the board

**Assessment questions:**

- Has a compliance function been formally established and documented?
- Does the compliance officer have genuine independence from revenue-generating operations?
- Does the compliance officer have direct board access and authority to escalate risks?
- Is the compliance function appropriately resourced (budget, headcount, legal support)?
- Are employee training programmes on DMA obligations in place?

#### Art. 11 — Annual Compliance Reporting

- Gatekeepers must submit an annual compliance report describing:
  - All measures implemented for Arts. 5, 6, and 7 obligations
  - Implementation approach and timeline for each obligation
  - Any changes to the technical implementations since the prior report
  - Interoperability endpoints and their implementation status
  - Data portability mechanisms and usage statistics
  - Internal audit findings on compliance status

**Assessment questions:**

- Has the annual compliance report been submitted within 6 months of designation and
  annually thereafter?
- Does the report contain both a public (non-confidential) and a confidential version?
- Are all required obligations addressed with sufficient technical detail?

#### Art. 15 — Consumer Profiling Techniques Audit

- Within 6 months of designation, the gatekeeper must submit an **independently audited**
  description of the profiling techniques applied to end users, covering:
  - Whether personal data is processed
  - Processing techniques and their purpose
  - Duration of profiling and data retention
  - Number of users exposed to each technique annually
  - Steps taken to obtain and verify consent
  - Cross-service profiling architecture
  - Impact assessment of profiling practices

**Assessment questions:**

- Has the Art. 15 profiling audit been completed and submitted?
- Was the audit conducted by a genuinely independent third party?
- Has the annual update been submitted?
- Has a copy been provided to the European Data Protection Board (EDPB)?

### Step 10: Anti-Circumvention Assessment

Article 13 contains two distinct anti-circumvention prohibitions.

#### Art. 13(1) — Threshold Circumvention

- Gatekeepers must not structure, split, or reorganise CPS to evade designation thresholds
- **Assessment questions:**
  - Has the organisation restructured CPS boundaries, spun out services, or altered user
    counting methodology in ways that reduce measured thresholds?
  - Are revenue or user metrics reported differently for DMA threshold purposes than for
    financial reporting or investor disclosure purposes?

#### Art. 13(4) — Behavioral Anti-Circumvention (Conduct Undermining Effective Compliance)

- Gatekeepers must not engage in any conduct — contractual, commercial, technical, or UI-based
  — that undermines effective compliance with Arts. 5, 6, and 7

**High-risk anti-circumvention patterns to assess:**

| Pattern                        | Example                                                                                                                                     | Risk                              |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| Dark patterns                  | Presenting external payment options with deterrent warnings or extra friction                                                               | NON-COMPLIANT                     |
| Asymmetric UI design           | Making sideloading technically possible but presenting it through 7-step friction flows                                                     | NON-COMPLIANT                     |
| Contractual workarounds        | Prohibiting developers from displaying external payment links through a separate "developer conduct policy"                                 | NON-COMPLIANT                     |
| Technical throttling           | Degrading API performance for third-party interoperability endpoints vs. own services                                                       | NON-COMPLIANT                     |
| Loyalty mechanism lock-in      | Designing reward/loyalty programmes that incentivise single-platform use in ways that undermine multi-homing                                | Review required                   |
| Security-justified obstruction | Invoking security grounds to block sideloading, alternative browsers, or third-party payment processors without proportionate justification | NON-COMPLIANT if disproportionate |

**Assessment questions:**

- Are there UI design patterns that create disproportionate friction for user choices
  that would favour competing services?
- Do developer/business-user contracts contain clauses that achieve prohibited outcomes
  by indirect means?
- Are technical interfaces for third-party access degraded or rate-limited relative to
  the gatekeeper's own service access?

### Step 11: Enforcement Exposure Calculation

Quantify the enforcement exposure for each identified non-compliance finding.

**Fine structure (Art. 29):**

| Infringement                                        | Maximum Fine                                                  |
| --------------------------------------------------- | ------------------------------------------------------------- |
| First violation of Arts. 5, 6, 7, 11, 12, 15, or 28 | 10% of global annual turnover                                 |
| Repeated infringement within 8 years                | 20% of global annual turnover                                 |
| Periodic penalty payments                           | 5% of average daily global turnover per day of non-compliance |

**Systematic non-compliance (Art. 18):**
If the Commission finds at least 3 non-compliance decisions in 8 years constitute a
"systematic infringement," it may impose additional remedies including:

- Mandatory interoperability with third-party services
- Mandatory access to data or operating system features
- **Structural remedies** (divestitures, separation of business units) as a last resort

**Reference enforcement data:**

- April 2025: Apple fined EUR 500 million (App Store anti-steering, Art. 6(4)/(5)) [VERIFY]
- April 2025: Meta fined EUR 200 million ("consent or pay" data combination, Art. 5(2)) [VERIFY]
- First fines established precedent that formal compliance without substantive compliance
  ("going through the motions") does not satisfy the DMA

**⟁ CLARIFY** — When calculating exposure, ask:

- "Do you have the global annual turnover figure for the most recent financial year? This
  is the base for fine calculation — EU-only revenue is not used."
- "Has the organisation been subject to any prior DMA non-compliance decisions, even for
  different CPS? Repeated infringements within 8 years trigger the 20% cap."

### Step 12: Remediation Prioritisation

Classify all findings and build a remediation roadmap.

**⟁ CLARIFY** — Before delivering the remediation roadmap, ask:

- "Does the organisation have a compliance programme delivery timeline or an existing
  remediation tracker? If so, I can map findings to that tracker rather than generating
  a standalone roadmap."
- "Are there findings where the Commission has already opened formal proceedings or issued
  preliminary findings? Those require an accelerated remediation track with legal counsel
  engagement."

**Prioritisation framework:**

| Priority     | Criteria                                                                                                               | Typical Action                                                                        |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Critical** | Art. 5 per se violation; active Commission investigation; repeated infringement risk                                   | Immediate suspension of non-compliant conduct; legal counsel engagement within 5 days |
| **High**     | Art. 6/7 material non-compliance; significant enforcement exposure (>EUR 100M); customer/developer complaints received | Remediation plan within 30 days; Commission voluntary compliance communication        |
| **Medium**   | Art. 6 partial implementation; documentation gaps; Art. 11/15/28 reporting deficiencies                                | Remediation plan within 90 days                                                       |
| **Low**      | Process improvements; enhanced documentation; training; monitoring enhancements                                        | Address in next annual compliance cycle                                               |

### Step 13: Quality Verification and Output Delivery

Before delivering the assessment:

1. Run the 5 **Citation Quality Gates** (see Quality Assurance Framework). Revise any
   failures before delivery.
2. For every Critical or High finding, run the 3-pass **Self-Interrogation**. Revise if
   any pass reveals an error.
3. Apply **Confidence Scoring** to every legal claim and finding.
4. Complete the **Glass Box Audit Trail** template.
5. Verify: No jurisdiction-specific concepts from member state law are stated as DMA
   universal requirements; all DMA article references match the regulation text; all
   enforcement data is marked VERIFIED or [VERIFY].

---

## Obligation Analysis Framework

### Article 5 — Per Se Prohibitions Summary

| Art.    | Prohibition                                    | Per Se | First Precedent                    |
| ------- | ---------------------------------------------- | ------ | ---------------------------------- |
| 5(1)(a) | Exclusive pre-installation and default-setting | Yes    | —                                  |
| 5(2)    | Cross-CPS data combination without consent     | Yes    | Meta EUR 200M (Apr 2025) [VERIFY]  |
| 5(3)    | Preventing alternative sales channels / MFN    | Yes    | —                                  |
| 5(4)    | Anti-steering / communication restriction      | Yes    | Apple EUR 500M (Apr 2025) [VERIFY] |
| 5(5)    | Restricting off-platform content access        | Yes    | —                                  |
| 5(6)    | Multi-homing restrictions                      | Yes    | —                                  |
| 5(7)    | Mandatory identification service               | Yes    | —                                  |

### Article 6 — Contestability Obligations Summary

| Art.  | Obligation                           | Specifiable | Key FRAND Element                                  |
| ----- | ------------------------------------ | ----------- | -------------------------------------------------- |
| 6(3)  | Hardware/software feature access     | Yes         | Equal API access                                   |
| 6(4)  | FRAND access for third parties       | Yes         | Published access terms                             |
| 6(5)  | Self-preferencing prohibition        | Yes         | Identical ranking criteria                         |
| 6(7)  | Sideloading / alternative app stores | Yes         | Technical enablement, no disproportionate friction |
| 6(8)  | Advertising transparency             | Yes         | Real-time price data                               |
| 6(9)  | Real-time data portability           | Yes         | Continuous API access                              |
| 6(11) | Search ranking data access           | Yes         | Query/click/view data                              |
| 6(12) | Advertising data access              | Yes         | Fee and remuneration transparency                  |
| 6(13) | Profiling consent interface          | Yes         | Aligned with GDPR Art. 6(1)(a)                     |

### DMA–GDPR Interplay

The DMA operates alongside GDPR without displacing it. Key intersection points:

| DMA Obligation                       | GDPR Requirement                                | Compliance Action                                                                             |
| ------------------------------------ | ----------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Art. 5(2) cross-CPS data combination | GDPR Art. 6(1)(a) + Art. 7 consent requirements | Both must be satisfied; a single consent mechanism must meet both standards                   |
| Art. 6(9) data portability           | GDPR Art. 20 data portability                   | DMA adds real-time/continuous/API requirements beyond GDPR; implement both                    |
| Art. 6(13) profiling consent         | GDPR Art. 6(1)(a) and Recital 43 (freely given) | Consent must be specific, informed, freely given, and revocable; "consent or pay" scrutinised |
| Art. 15 profiling audit              | GDPR Art. 35 DPIA                               | Profiling audit should be integrated with or build upon DPIA infrastructure                   |

### DMA–Competition Law Interaction

| Aspect               | Analysis                                                                                                                                  |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Lex specialis        | Where DMA provides a specific rule for gatekeeper conduct, DMA takes precedence over general Art. 102 TFEU application                    |
| Parallel application | DMA and Art. 102 TFEU can apply simultaneously to the same conduct, but only one regime's penalty should be imposed (ne bis in idem risk) |
| Standard of proof    | DMA uses presumptive designation (lower burden); Art. 102 TFEU requires full dominance proof                                              |
| Jurisdiction         | Only Commission enforces DMA; national competition authorities may apply Art. 102 TFEU to gatekeeper conduct on separate grounds          |
| Remedy scope         | DMA: behavioural + structural (Art. 18); Art. 102: generally behavioural unless exceptional circumstances                                 |

---

## Compliance Classification System

Classify each DMA obligation area using the four-tier system:

| Status            | Meaning                                                                                        | Output Required                                                               |
| ----------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **COMPLIANT**     | Obligation met; documented; auditable                                                          | Record with supporting evidence                                               |
| **PARTIAL**       | Obligation partially implemented; gaps identified                                              | Gap description + specific remediation steps                                  |
| **NON-COMPLIANT** | Obligation not met; per se violation or material deficiency                                    | Full analysis of violation + legal basis + remediation + enforcement exposure |
| **CRITICAL**      | Per se Art. 5 violation under active investigation or with first-precedent fine already issued | Immediate escalation; legal counsel engagement required                       |

---

## Prioritisation Framework

| Tier                                                   | DMA Area                                                                                                               | Rationale                                                                                                         |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Tier 1 — Mandatory immediate action**                | All Art. 5 per se prohibitions; Art. 28 compliance function establishment; Art. 11 first annual report                 | Per se violations carry full fine exposure with no justification available; compliance function is mandatory      |
| **Tier 2 — Must resolve before Commission engagement** | Art. 6(5) self-preferencing; Art. 6(7) sideloading; Art. 7 interoperability requests; Art. 13 anti-circumvention audit | These are high-enforcement-priority areas where preliminary findings have been issued against leading gatekeepers |
| **Tier 3 — Implement within 90-day compliance cycle**  | Art. 6(3)/(4)/(8)/(9)/(11)/(12) FRAND and data access; Art. 6(13) profiling consent; Art. 15 profiling audit           | Material compliance obligations with moderate enforcement risk                                                    |
| **Tier 4 — Address in next annual compliance review**  | Documentation enhancements; training updates; monitoring improvements; minor process gaps                              | Governance improvements that reduce systemic infringement risk over time                                          |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                                       | Fail Action                       |
| -------------- | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| **Source**     | Every DMA obligation cited references a specific Article and paragraph                                                     | Add citation or mark [UNVERIFIED] |
| **Format**     | All EU legislative references use the standard format: Regulation (EU) [year]/[number], Article [N], paragraph [N]         | Fix format                        |
| **Currency**   | Every cited provision checked for amendment, implementing regulation, or Commission specification                          | Flag [CHECK CURRENCY]             |
| **Domain**     | Analysis stays within DMA scope — no conflation with DSA, AI Act, or national competition law without explicit distinction | Remove or flag cross-regime bleed |
| **Confidence** | Uncertainty explicitly stated, particularly for enforcement positions based on preliminary findings or appeals in progress | Add confidence qualifier          |

### Self-Interrogation for Critical/High Findings

For any finding classified as **Critical** or **High**, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the non-compliance finding follow logically from
the DMA article cited? Would the Commission actually classify this conduct as a violation
under the current enforcement approach?

**Pass 2 — Completeness**: Have all relevant DMA articles, implementing decisions, and
Commission guidance been considered? Are there Art. 6 specification decisions that define
what compliant implementation looks like for this obligation?

**Pass 3 — Challenge**: What is the strongest argument that this conduct is compliant?
Is there a security or interoperability justification available under Art. 9 (suspension)?
Has the Commission indicated it would accept a particular implementation approach?

### Confidence Scoring

| Level        | Range     | Meaning                                                        | Action                                 |
| ------------ | --------- | -------------------------------------------------------------- | -------------------------------------- |
| **Definite** | 0.95–1.0  | Settled by Commission decision or black-letter DMA text        | State with confidence                  |
| **High**     | 0.80–0.94 | Strong enforcement precedent or clear article text             | State with brief caveat                |
| **Probable** | 0.60–0.79 | Good arguments from enforcement pattern but no direct decision | State with reasoning                   |
| **Possible** | 0.40–0.59 | Genuinely uncertain; reasonable interpretations differ         | Flag for expert review with both sides |
| **Unlikely** | 0.0–0.39  | Speculative; insufficient legal basis                          | Do not assert; flag [UNCERTAIN]        |

---

## Glass Box Audit Trail

Every DMA compliance assessment should include the following audit trail:

```yaml
glass_box:
  skill_name: "legalcode-eu-dma-compliance"
  mode: "Compliance assessment"
  topic: "EU Digital Markets Act (Regulation (EU) 2022/1925)"
  jurisdiction: "European Union"
  gatekeeper_or_party_assessed: "[Name of gatekeeper or business user]"
  designation_status: "[Designated / Undesignated / Under investigation]"
  cps_assessed: "[List of CPS assessed]"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "/tmp/legalcode-dma-authority.md / Not created"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  article_5_findings: "[COMPLIANT / NON-COMPLIANT by article — list]"
  article_6_findings: "[COMPLIANT / PARTIAL / NON-COMPLIANT by article — list]"
  article_7_findings: "[COMPLIANT / PARTIAL / NON-COMPLIANT / N/A]"
  critical_findings: "[Number of Critical findings]"
  high_findings: "[Number of High findings]"
  fine_exposure_estimate: "[EUR range or 'Not calculated']"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "Appeals pending on first-precedent fines (Apple/Meta) may alter enforcement interpretation"
    - "Implementing regulations for Art. 7 interoperability technical specifications may add requirements [VERIFY]"
    - "DMA enforcement is Commission-discretionary — timeline and targeting are uncertain"
    - "[Any additional scope limitations or assumptions]"
  reviewer: "AI-assisted — requires review by qualified EU competition/digital regulation counsel"
```

---

## Anti-Patterns

What NOT to do when assessing or implementing DMA compliance:

1. **Conflating DMA with DSA**: The DMA and DSA are distinct regulations with different
   scope, obligations, enforcement authorities, and penalty structures. Applying DSA
   analysis to DMA obligations (or vice versa) produces incorrect results. The DMA covers
   only designated gatekeepers; the DSA covers all digital intermediary services.

2. **Treating formal compliance as sufficient**: The Apple and Meta April 2025 fines
   established that going through the technical motions of compliance without enabling
   genuine user choice or developer freedom constitutes non-compliance. Form-over-substance
   compliance is an anti-pattern under Art. 13(4).

3. **Assuming Art. 6 obligations are self-executing**: Unlike Art. 5 per se prohibitions,
   Art. 6 obligations are susceptible to further specification. Not checking whether the
   Commission has issued implementing decisions specifying how compliance must be achieved
   for a particular CPS or obligation leads to incomplete assessments.

4. **Treating "consent or pay" as lawful by default**: The Meta fine invalidated the
   assumption that offering a paid ad-free alternative alongside a consent-to-profiling
   option satisfies Art. 5(2). Consent must be genuinely free — the DMA and GDPR consent
   standards must be assessed together. [VERIFY current enforcement position on this issue
   post-appeal.]

5. **Ignoring UI dark patterns as a compliance risk**: Anti-circumvention under Art. 13(4)
   explicitly covers user interface design that technically enables a choice but makes it
   practically very difficult. A 7-step sideloading process with security warnings at each
   step has been treated as a circumvention mechanism, not compliant implementation.

6. **Calculating fine exposure on EU-only revenue**: DMA fines are calculated on **global
   annual turnover** — not EU revenue. Using EU-only figures dramatically understates the
   financial exposure of a DMA non-compliance finding.

7. **Treating the compliance officer as a formality**: Art. 28 requires genuine independence
   and board-level authority. Designating a mid-level employee without board access, or a
   compliance officer whose authority can be overridden by product teams, does not satisfy
   Art. 28. The Commission will assess whether the compliance function has real power.

8. **Applying the Art. 9 suspension argument without legal scrutiny**: Gatekeepers may
   request suspension of obligations on grounds of third-party security risks or exceptional
   circumstances. This is a narrow exception that the Commission scrutinises closely — it
   cannot be used as a routine compliance delay mechanism.

9. **Overlooking the 3-month interoperability response deadline**: Art. 7 requires NICS
   gatekeepers to make interoperability functionalities operational within 3 months of
   receiving a reasonable request. Treating this as advisory or subject to commercial
   negotiation is a non-compliance risk.

10. **Failing to align the Art. 15 profiling audit with the GDPR DPIA**: The Art. 15
    profiling audit covers much of the same ground as a GDPR Data Protection Impact
    Assessment. Running both in isolation creates inconsistency, documentation burden, and
    risk of contradictory findings.

11. **Treating DMA and Art. 102 TFEU as mutually exclusive**: The Commission applies the
    lex specialis principle — DMA takes precedence for gatekeeper conduct it specifically
    addresses. However, the Commission may still apply Art. 102 TFEU to gatekeeper conduct
    that falls outside DMA scope, and national competition authorities can act on the same
    conduct under national law for non-DMA aspects.

12. **Ignoring the systematic non-compliance threshold**: If the Commission has issued 3
    non-compliance decisions in 8 years, Art. 18 authorises structural remedies including
    divestitures. Organisations with multiple prior DMA findings should assess systematic
    non-compliance risk and model potential structural remedy scenarios.

13. **Mischaracterising business users as end users (or vice versa)**: Many DMA obligations
    have different requirements depending on whether the subject is a business user
    (developer, merchant, advertiser) or an end user (consumer). Conflating the two
    produces incorrect obligation mapping.

14. **Failing to publish interoperability technical documentation**: Art. 7 requires
    gatekeepers to publish technical specifications enabling third-party NICS providers to
    request and implement interoperability. The obligation to publish documentation is
    independent of whether any request has been received.

15. **Neglecting annual compliance report deadlines**: The Art. 11 annual report must be
    submitted within 6 months of designation and annually thereafter. Late or incomplete
    reports are themselves infringements, independent of whether the underlying obligations
    are met.

16. **Assessing compliance without tracking live Commission enforcement**: DMA enforcement
    is active and accelerating. Compliance assessments conducted without checking the current
    enforcement tracker at digital-markets-act.ec.europa.eu may miss recently opened
    proceedings, preliminary findings, or binding decisions that directly affect the
    assessment's legal conclusions.

---

## Writing Standards

Before delivering any DMA compliance output, apply these standards:

- **State the DMA article, paragraph, and subparagraph** for every obligation discussed —
  not just "Article 5" but "Article 5(2)(b)" where relevant
- **Distinguish per se prohibitions from specifiable obligations** — never describe an Art. 5
  prohibition as "subject to good-faith assessment"
- **Clearly separate findings from conclusions** — a finding is a factual observation
  ("the app store terms contain a clause prohibiting external payment links"); a conclusion
  is a legal characterisation ("this constitutes a violation of Art. 5(4)")
- **Use active voice for findings**: "The gatekeeper's App Store terms prohibit developers
  from displaying external payment options" — not "There may be issues with the App Store terms"
- **Mark every enforcement data point with its verification status** — enforcement decisions
  that are on appeal may be reversed; compliance assessments must track this uncertainty
- **Avoid generic compliance language**: "Ensure compliance with all applicable DMA obligations"
  is not actionable; "Implement a genuinely neutral choice screen for default browser and
  search engine selection, equivalent to the one currently offered in the EU (if applicable)"
  is actionable

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary regulatory research tool.

**With legalcode-mcp connected (preferred):**

- In Step 4, search for the current DMA text, Commission decisions, implementing regulations,
  and any enforcement notices relevant to the CPS under assessment
- Verify the current designated gatekeeper list and associated CPS
- Search for any Commission guidelines or technical specifications issued under Arts. 7 and 8
- Save verified results to `/tmp/legalcode-dma-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with the obligation framework in this skill, which incorporates verified research
  from the skill creation date (2026-03-21)
- Mark all enforcement data and article references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Advise the user to verify current enforcement status at:
  digital-markets-act.ec.europa.eu/enforcement

---

## Localization Notes

The DMA is a directly applicable EU regulation — it does not require national transposition
and applies uniformly across all 27 EU Member States.

**EEA extension**: The DMA applies within the EEA (Norway, Iceland, Liechtenstein) through
EEA Agreement incorporation. [VERIFY current EEA incorporation status.]

**UK divergence**: The UK no longer applies the DMA following Brexit. The UK has enacted
the Digital Markets, Competition and Consumers Act 2024 (DMCCA), which creates a similar
but distinct "Strategic Market Status" (SMS) designation regime administered by the UK
Competition and Markets Authority (CMA). Key differences:

- UK SMS designation is CMA-administered (not Commission-administered)
- Conduct requirements are negotiated individually between the CMA and designated firms
  ("Conduct Requirements") rather than applying automatically by statute
- UK fine cap: up to 10% of global turnover (same cap, different enforcement body)
- Cross-border gatekeepers must comply with both DMA (EU) and DMCCA (UK) — assess both
  regimes separately

**Third-country gatekeepers**: A non-EU gatekeeper (e.g., US-headquartered tech platform)
is fully subject to DMA obligations if it meets the designation thresholds in relation to
EU users. There is no establishment requirement. The Commission may issue information
requests, open proceedings, and impose fines against non-EU entities.

---

## Output Format Template

Deliver the DMA compliance assessment in the following format:

```markdown
# DMA Compliance Assessment — [Gatekeeper/Organisation Name]

**Date:** [Assessment date]
**CPS assessed:** [List]
**Designation status:** [Designated / Undesignated / Risk assessment only]
**Perspective:** [Gatekeeper compliance / Business user rights / Investor diligence]

---

## Executive Summary

**Overall compliance status:** [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL]
**Critical findings:** [N] | **High:** [N] | **Medium:** [N] | **Low:** [N]
**Estimated fine exposure:** [EUR range or N/A]
**Immediate actions required:** [Top 3 bullet points]

---

## Gatekeeper Designation Analysis

[For undesignated entities: threshold assessment and designation risk]
[For designated entities: confirmation of designation date, designated CPS, and
compliance deadline]

---

## Article 5 Per Se Prohibitions Assessment

| Art.    | Prohibition                      | Status                                 | Finding            |
| ------- | -------------------------------- | -------------------------------------- | ------------------ |
| 5(1)(a) | Exclusive pre-installation       | [COMPLIANT / NON-COMPLIANT]            | [One-line finding] |
| 5(2)    | Data combination without consent | [COMPLIANT / NON-COMPLIANT / CRITICAL] | [One-line finding] |
| 5(3)    | Alternative channels / MFN       | [COMPLIANT / NON-COMPLIANT]            | [One-line finding] |
| 5(4)    | Anti-steering                    | [COMPLIANT / NON-COMPLIANT / CRITICAL] | [One-line finding] |
| 5(5)    | Off-platform content access      | [COMPLIANT / NON-COMPLIANT]            | [One-line finding] |
| 5(6)    | Multi-homing restrictions        | [COMPLIANT / NON-COMPLIANT]            | [One-line finding] |
| 5(7)    | Mandatory identification service | [COMPLIANT / NON-COMPLIANT]            | [One-line finding] |

**Detailed findings for any NON-COMPLIANT or CRITICAL items:**

### [Article citation]: [Prohibition name]

- **Finding**: [Factual description of the non-compliant conduct]
- **Legal basis**: [DMA article + paragraph; enforcement precedent if applicable]
- **Enforcement exposure**: [EUR estimate; fine tier]
- **Recommended action**: [Specific remediation step]
- **Confidence**: [Level / Score]

---

## Article 6 Contestability Obligations Assessment

[Same table + detailed findings structure as Article 5 section]

---

## Article 7 Interoperability Assessment

[NICS only — mark N/A if not applicable]

---

## Compliance Function and Transparency Assessment

[Art. 11 / Art. 15 / Art. 28 findings]

---

## Anti-Circumvention Assessment

[Art. 13 findings]

---

## Enforcement Exposure Summary

| Finding                      | Art.   | Priority                   | Fine Basis             | Exposure Estimate |
| ---------------------------- | ------ | -------------------------- | ---------------------- | ----------------- |
| [Description]                | [Art.] | [Critical/High/Medium/Low] | [% of global turnover] | [EUR range]       |
| **Total estimated exposure** |        |                            |                        | **[EUR range]**   |

---

## Remediation Roadmap

### Immediate Actions (0–30 days)

[For Critical and High findings]

### Short-Term Actions (30–90 days)

[For Medium findings and documentation/reporting gaps]

### Medium-Term Actions (90–180 days)

[For programme-building, training, and governance improvements]

---

## DMA–GDPR and DMA–Competition Law Intersection

[Flag any obligations requiring coordinated GDPR or competition law analysis]

---

## Audit Trail

[Glass Box YAML block]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

- Regulation (EU) 2022/1925 (Digital Markets Act) full text
- Commission enforcement decisions: Apple EUR 500M (April 2025) and Meta EUR 200M
  (April 2025) [VERIFY appeal status]
- Commission formal proceedings opened March 2024 against Alphabet, Apple, and Meta
- Commission preliminary non-compliance findings against Alphabet (March 2025) [VERIFY]
- Commission binding interoperability decision against Apple (March 2025) [VERIFY]
- Designated gatekeeper list as of March 2024 (Alphabet, Amazon, Apple, ByteDance,
  Meta, Microsoft) plus Apple iPadOS (April 2024) and Booking.com (May 2024)
- eu-digital-markets-act.com article-level analysis
- Bruegel, Bird & Bird, Noerr, Utrecht Law Review, and Oxford Competition Law academic
  analysis on DMA enforcement and Art. 102 TFEU interaction
- Legalcode 2-agent research pipeline + web-backed legal research (March 2026)
