---
name: legalcode-advertising-marketing-compliance
description: Reviews advertising and marketing materials for legal compliance across US, EU, and UK regulatory
  frameworks. Use when auditing ad campaigns, influencer partnerships, email or SMS marketing programs,
  sponsored content, or marketing compliance programs for legal exposure.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Reviews advertising and marketing materials for legal compliance across US, EU, and UK regulatory frameworks. Use when auditing ad campaigns, influencer partnerships, email or SMS marketing programs, sponsored content, or marketing compliance programs for legal exposure. Covers FTC Act Section 5 deceptive and unfair practices, FTC Endorsement Guides (2023 update) including influencer disclosures, FTC Green Guides and environmental claims, FTC health claims substantiation (CARSE standard), CAN-SPAM Act email marketing requirements, TCPA telephone and text marketing consent, COPPA 2025 children's online privacy and advertising restrictions, CARU children's advertising guidelines, EU Unfair Commercial Practices Directive and Omnibus/EmpCo greenwashing amendments, UK ASA/CAP Code, EU and UK comparative advertising rules, and Lanham Act Section 43(a) false advertising. Also triggers for native advertising disclosure review, paid promotion transparency, testimonial compliance, affiliate marketing oversight, and advertising compliance program gap analysis.


# Legalcode Advertising & Marketing Compliance

> **Disclaimer**: This skill provides a framework for AI-assisted advertising and marketing
> compliance review. It does not constitute legal advice. All outputs should be reviewed
> by a qualified legal professional licensed in the relevant jurisdiction before use. Laws
> and regulations change; verify current applicability — particularly penalty amounts,
> rulemaking status, and enforcement guidance — before relying on any provision described
> here. Statutory and regulatory citations from training data carry hallucination risk;
> verify against authoritative sources before reliance.

## Purpose and Scope

This skill reviews advertising and marketing content, campaigns, and programs against
applicable legal frameworks. It identifies compliance gaps, classifies their severity,
generates actionable remediation steps, and produces a confidence-scored, auditable
assessment.

**Covers:**

- Claim substantiation analysis (FTC reasonableness / CARSE standard; EU/UK equivalents)
- Influencer and endorser disclosure compliance (FTC 2023 Guides; EU UCPD; UK CAP Code)
- Environmental ("green") claims review (FTC Green Guides; EU EmpCo Directive 2024/825; UK ASA)
- Health and medical claim verification (FTC health products guidance; EU Regulation 1924/2006)
- Children's advertising restrictions (COPPA 2025 amendments; CARU guidelines)
- Email marketing compliance (CAN-SPAM Act)
- Telephone and text marketing consent (TCPA; state mini-TCPA laws)
- Native advertising and sponsored content disclosure
- Comparative advertising rules (EU Directive 2006/114/EC; Lanham Act § 43(a); UK CAP Code)
- Advertising compliance program architecture and gap analysis
- Four-tier compliance classification (COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY)
- Remediation roadmap with stakeholder ownership assignments

**Does not:**

- Provide legal advice or replace qualified counsel
- Substitute for in-depth regulatory opinion from an advertising law specialist
- Apply exclusively to one jurisdiction — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers
- Cover securities advertising (regulated separately by SEC/FINRA/FCA)
- Cover political advertising (distinct federal and state regulatory regimes)
- Cover pharmaceutical prescription drug advertising (FDA OPDP jurisdiction)

---

## Jurisdiction and Governing Law

This skill is jurisdiction-agnostic but covers the three primary advertising law regimes
in depth:

| Regime           | Key Instruments                                                                                                                                                                         | Enforcement Authority                                    |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **US Federal**   | FTC Act § 5 (15 U.S.C. § 45); Endorsement Guides (16 C.F.R. Part 255); Green Guides (16 C.F.R. Part 260); CAN-SPAM (15 U.S.C. § 7701); TCPA (47 U.S.C. § 227); COPPA (15 U.S.C. § 6501) | FTC, FCC, DOJ, state AGs                                 |
| **US State**     | State UDAP statutes (CA UCL/CLRA/FAL; NY GBL §§ 349–350; FL FDUTPA; IL CFA); FTSA; OTSA                                                                                                 | State attorneys general; private right of action         |
| **EU**           | UCPD 2005/29/EC; Omnibus Directive 2019/2161; EmpCo Directive 2024/825; EU Regulation 1924/2006 (health claims)                                                                         | National consumer protection authorities; CPC Regulation |
| **UK**           | CAP Code; BCAP Code; DMCCA 2024; UK NHC Register                                                                                                                                        | ASA, Ofcom, CMA, Trading Standards                       |
| **Cross-border** | Comparative Advertising Directive 2006/114/EC; Lanham Act § 43(a)                                                                                                                       | Courts; Lauham Act private rights of action              |

[JURISDICTION-SPECIFIC] When working outside US/EU/UK, research the applicable national
advertising law authority and enforcement regime. Common additional frameworks:

- **Canada**: Competition Act (misleading advertising), CASL (email), CRTC (broadcast)
- **Australia**: Australian Consumer Law, ACCC enforcement, ASB self-regulation
- **Germany**: UWG (Gesetz gegen den unlauteren Wettbewerb); Heilmittelwerbegesetz (health claims)
- **France**: Code de la consommation; ARPP self-regulation

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points, marked **⟁ CLARIFY**
below. Rather than assuming context, the workflow pauses when:

- The answer determines which regulatory regimes apply
- Product category changes the substantiation standard required
- Business context is needed to classify severity correctly
- The user's risk tolerance affects remediation prioritization

Present each CLARIFY as a structured set of options. If the user has already provided the
information, skip the question and proceed. For batch/automated runs, use the defaults
stated in each CLARIFY.

---

## Workflow

### Step 1: Accept Input

Accept materials in any of these formats:

- **Campaign materials**: Ad copy, creative assets, scripts, landing pages, social posts,
  email templates, influencer briefs
- **Substantiation files**: Clinical studies, consumer surveys, test results, expert
  opinion letters, substantiation memos
- **Program documents**: Advertising compliance policy, claims approval workflow,
  influencer contract templates, affiliate agreements, training materials
- **URLs**: Links to live ads, social media posts, websites, or campaign dashboards
- **Description only**: Written description of the campaign or practice to review when
  materials cannot be shared

If no materials are provided, prompt the user to supply them or to describe the campaign
in sufficient detail to proceed.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user the following questions. Present as
structured options where possible:

1. **Assessment mode**: What is the primary goal?
   - Options:
     - **A — Pre-launch audit**: Review campaign or claims before going live
     - **B — Post-launch review**: Audit a campaign already running
     - **C — Program gap analysis**: Assess the organization's advertising compliance program
     - **D — Incident response**: A complaint, warning letter, or enforcement inquiry has been received
     - **E — Transaction diligence**: Reviewing an acquisition target's or partner's ad practices
   - _Why this matters_: Determines urgency, depth, and output format. Mode D and E require privileged context consideration.

2. **Product/service category**: What is being advertised?
   - Options: General consumer goods, Health/wellness/dietary supplement, Medical device,
     Financial product or service, Environmental/sustainability product, Food/beverage,
     Children's product or service, Technology/AI/software, Cryptocurrency/digital assets, Other
   - _Why this matters_: Health, financial, and children's categories trigger elevated
     substantiation standards and specialized regulatory overlays.

3. **Geographic markets**: Which markets are targeted?
   - Options: US only, EU only, UK only, US + EU, US + UK, US + EU + UK, Other/global
   - _Why this matters_: Different regimes apply. A campaign compliant under FTC standards
     may require material changes for EU or UK compliance.

4. **Advertising channels**: Which channels are used?
   - Options (select all that apply): Traditional media (TV/radio/print), Digital display,
     Search advertising, Social media (organic), Social media (paid), Influencer/creator
     partnerships, Email marketing, SMS/text marketing, Native advertising, Podcast, Other
   - _Why this matters_: Channel determines applicable rules (TCPA for SMS, CAN-SPAM for
     email, COPPA for child-directed digital, CAP Code for UK non-broadcast).

5. **Third-party involvement**: How is the advertising created and distributed?
   - Options: In-house only, External advertising agency, Influencer/creator partners,
     Affiliate network, Multiple third parties
   - _Why this matters_: Brand retains primary compliance responsibility regardless of
     third-party involvement, but oversight requirements intensify with influencers and
     affiliates.

6. **Regulatory history**: Has the organization had prior advertising compliance issues?
   - Options: Clean history, Prior FTC/ASA/national authority inquiry or warning letter,
     Prior formal enforcement action, Currently under investigation, Unknown
   - _Why this matters_: Prior Penalty Offense Notices from the FTC, or prior ASA
     compliance actions, materially affect the standard of care required.

7. **Program maturity**: Does a formal advertising compliance program exist?
   - Options: No formal process, Early-stage (some guidelines exist), Established
     (claims approval workflow and training in place), Advanced (substantiation database,
     real-time monitoring, legal pre-clearance)
   - _Why this matters_: Determines which of the Five Pillars require structural build-out
     vs. refinement.

For batch/automated runs, use these defaults: Mode A (pre-launch audit), general consumer
goods, US + EU + UK, digital/social, multiple third parties, clean history, early-stage program.

**⟁ CLARIFY** — If operating in Mode D (incident response), ask before proceeding:

- "Is this review being conducted at the direction of counsel for purposes of litigation
  or regulatory response? If yes, this review should be covered by attorney-client
  privilege, and findings should be communicated through counsel, not in a written report."
- Privilege consideration: state assumptions explicitly and flag if privileged treatment
  is needed.

### Step 3: Determine Applicable Regulatory Regimes

Based on the context gathered in Step 2, map the applicable regulatory frameworks using
the table below. This determines which rules govern the assessment in Step 5.

| Product Category      | US Federal Regime                                            | US State Overlay                    | EU Regime                              | UK Regime                                |
| --------------------- | ------------------------------------------------------------ | ----------------------------------- | -------------------------------------- | ---------------------------------------- |
| General consumer      | FTC Act § 5, Endorsement Guides                              | State UDAP statutes                 | UCPD + Omnibus                         | CAP Code                                 |
| Health/wellness       | FTC Act § 5, CARSE standard, Health Products Guidance (2023) | State UDAP; state health claim laws | UCPD; EU Regulation 1924/2006          | CAP Code; UK NHC Register                |
| Food/beverage         | FTC Act § 5; FDA-FTC overlap                                 | State UDAP                          | UCPD; EU Regulation 1924/2006          | CAP Code; BCAP Code                      |
| Environmental         | FTC Green Guides (16 C.F.R. Part 260)                        | State AG focus (CA, NY)             | EmpCo Directive 2024/825; UCPD         | CAP/ASA Green Claims Guidance            |
| Children's product    | FTC Act § 5; COPPA (16 C.F.R. Part 312); CARU guidelines     | State children's privacy laws       | UCPD; GDPR Art. 8 (children's consent) | CAP Code §§ 5/5h; BCAP Code §§ 5/5h      |
| Financial product     | FTC Act § 5; FTC Income Disclosure requirements              | State UDAP; UDAP financial overlays | UCPD; MiFID II (if investments)        | CAP Code; FCA financial promotions rules |
| Email marketing       | CAN-SPAM (15 U.S.C. § 7701)                                  | State privacy laws (CA, VA, CT)     | GDPR consent; ePrivacy Directive       | PECR; UK GDPR                            |
| SMS/text marketing    | TCPA (47 U.S.C. § 227); TSR                                  | FTSA; OTSA; state mini-TCPAs        | GDPR consent; ePrivacy                 | PECR; UK GDPR                            |
| Crypto/digital assets | FTC Act § 5; SEC/FTC coordination                            | State money transmission laws       | MiCA; UCPD                             | FCA financial promotions; CAP Code       |

**⟁ CLARIFY** — If the product category creates uncertainty about regulatory scope (e.g.,
a supplement making health claims, a fintech product making earnings claims, or a product
marketed as "natural" or "clean"), ask:

- "Based on the claims made, this product may trigger [X additional regime]. Should I apply
  that framework to this review?"

### Step 4: Gather Legal Authority

Use **legalcode-mcp** to research current legal authority for the applicable regimes
identified in Step 3.

**legalcode-mcp search queries to run:**

```
US substantiation:
  "FTC Act Section 5 deception unfairness standard advertising"
  "FTC Health Products Compliance Guidance January 2023"
  "FTC competent reliable scientific evidence standard"
  "FTC Penalty Offense Notices advertising substantiation 2023"

Endorsements/influencers:
  "FTC Endorsement Guides 16 CFR Part 255 2023 final rule"
  "FTC influencer disclosure material connection 2024 enforcement"
  "FTC Consumer Review Rule August 2024 fake reviews"

Environmental/green claims:
  "FTC Green Guides 16 CFR Part 260 environmental marketing"
  "EU Directive 2024/825 Empowering Consumers Green Transition"
  "ASA environmental claims green carbon neutral advertising guidance 2023 2024"

Children's:
  "COPPA Rule 16 CFR Part 312 2025 amendments behavioral advertising"
  "CARU Children's Advertising Review Unit guidelines 2022"

Email/text:
  "CAN-SPAM Act FTC enforcement requirements 2024"
  "TCPA prior express written consent FCC 2024 2025 rulemaking"

EU/UK:
  "EU UCPD Unfair Commercial Practices Directive 2005/29"
  "Omnibus Directive 2019/2161 implementation fake reviews search rankings"
  "UK CAP Code influencer disclosure ASA enforcement 2024"
  "UK DMCCA 2024 consumer protection advertising"

Recent enforcement:
  "FTC advertising enforcement actions 2024 2025"
  "ASA rulings upheld advertising 2024"
  "State attorney general false advertising enforcement 2024"
```

Save the most relevant results to `/tmp/legalcode-admarcom-authority.md`.

**If legalcode-mcp is not connected:**

- Mark all regulatory citations throughout this assessment with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with training-data knowledge; flag that penalty amounts, rulemaking status,
  and recent enforcement require independent verification
- In particular, flag with [VERIFY]:
  - Current inflation-adjusted FTC civil penalty amounts
  - Green Guides update status (expected revision not yet finalized as of research date)
  - TCPA rulemaking status (one-to-one consent rule vacated; revised rule pending [VERIFY])
  - EmpCo Directive 2024/825 transposition and application dates (March 27, 2026; September 27, 2026)
  - State mini-TCPA law landscape (Florida FTSA, Oklahoma OTSA, and growing list)

### Step 5: Assess Compliance Across Five Pillars

Read all submitted materials before assessing. Assess each pillar sequentially, but keep
cross-pillar interactions in mind (e.g., a health claim violation in Pillar 1 also affects
Pillar 3 if children are targeted).

**⟁ CLARIFY** — For large campaign suites (10+ assets) or comprehensive program audits:

- "This is a large review. Should I perform a full assessment of all five pillars, or
  focus on the areas of greatest concern given your [mode / product category / channel]?"
- "Are any assets already pre-cleared by counsel or substantiation file? If so, I can
  focus my review on the remaining materials."

---

#### Pillar 1: Substantiation and Claims Verification

**Legal basis:**

- US: FTC Act § 5; FTC Policy Statement on Advertising Substantiation (_Thompson Medical Co._, 1984); FTC Health Products Compliance Guidance (January 2023); FTC Green Guides (16 C.F.R. Part 260)
- EU: UCPD Art. 6–7 (misleading actions and omissions); EU Regulation 1924/2006 (food/beverage health claims)
- UK: CAP Code Rule 3.7 ("Before distributing an ad, advertisers must hold documentary evidence to prove all claims that consumers are likely to regard as objective and capable of substantiation")

**Core principle — Prior Substantiation Requirement:**
Advertisers must possess a reasonable basis for every objective claim _before_ dissemination.
Evidence created after the claim is made generally cannot substitute for pre-existing substantiation.

**Claim type analysis matrix:**

| Claim Type                                                                   | US Standard                                                                                                      | EU/UK Standard                                                                                              | Evidence Level                                                    |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **General product performance**                                              | "Reasonable basis" (FTC factors test)                                                                            | UCPD: objective, verifiable basis required (Art. 6.1(b))                                                    | Consumer studies, in-house tests, expert opinion                  |
| **Health / efficacy** (general wellness)                                     | Competent and reliable scientific evidence (CARSE)                                                               | UCPD Art. 6; CAP Code Rule 12                                                                               | Expert-evaluated studies generally accepted in the field          |
| **Health / structure-function**                                              | CARSE; FDA structure/function disclaimer required [VERIFY]                                                       | EU Regulation 1924/2006 positive list (food health claims)                                                  | RCT-level evidence preferred; at minimum 2 well-designed studies  |
| **"Clinically proven"**                                                      | CARSE + typically ≥2 adequate, well-controlled RCTs                                                              | UCPD; CAP Code Rule 3.7                                                                                     | ≥1–2 adequate RCTs; single study more vulnerable                  |
| **Disease treatment / cure**                                                 | Drug territory — FDA approval required for labeling; FTC enforces advertising [VERIFY FDA-FTC boundary]          | Prohibited for food/supplements under EU Regulation 1924/2006; UCPD Annex I (false claim of curing illness) | Prescription/OTC drug approval required; prohibited without it    |
| **Comparative superiority**                                                  | Competent and reliable tests using accepted industry methodology                                                 | EU Dir. 2006/114 Art. 4 (objective, verifiable, representative features)                                    | Head-to-head testing; methodology must be disclosed if relevant   |
| **Environmental ("green", "eco-friendly", "sustainable", "carbon neutral")** | FTC Green Guides; unqualified absolute claims very likely deceptive                                              | EmpCo Dir. 2024/825 (in force Sep. 27, 2026) prohibits unqualified generic claims                           | Full product lifecycle evidence; specific, not generic            |
| **"Net zero" / "carbon neutral" future commitments**                         | FTC Green Guides: offsetting alone may not suffice                                                               | EmpCo Dir. 2024/825: requires verifiable, time-bound plans with independent verification                    | Detailed transition plans with interim targets; third-party audit |
| **Made in USA / local origin**                                               | FTC Made in USA Rule (all or virtually all domestic content) [VERIFY penalty amounts]                            | UCPD Art. 6.1(f) (geographic origin)                                                                        | Supply chain documentation                                        |
| **Consumer testimonials**                                                    | FTC Endorsement Guides: atypical results must be disclosed; "results not typical" alone is no longer safe harbor | UCPD Art. 6; CAP Code (typical results required)                                                            | Survey data on typical results; before/after methodology          |
| **"Free" / price claims**                                                    | FTC Act § 5; must not have undisclosed conditions                                                                | UCPD Annex I no. 20 (free with conditions prohibited)                                                       | Clear documentation of all conditions                             |
| **Puffery**                                                                  | Not actionable — subjective superiority ("the best," "world-class") without objective claim                      | UCPD: puffery generally acceptable if clearly not taken literally                                           | No substantiation required for genuine puffery                    |

**Key review checklist:**

- [ ] Every objective, verifiable claim identified in all materials
- [ ] Substantiation file exists for each claim, dated **before** campaign launch
- [ ] Substantiation evidence meets the standard appropriate to the claim type
- [ ] Health claims: CARSE-level evidence present; FDA/EFSA authorization confirmed if applicable
- [ ] Green claims: lifecycle evidence available; "carbon neutral" / "net zero" claims have documented plans with independent verification
- [ ] Comparative claims: methodology documented; compared on material, relevant, verifiable features
- [ ] Testimonials: typical-results data available; atypical results disclosed in proximity to the testimonial
- [ ] "Free" claims: all conditions clearly disclosed
- [ ] No structure/function claims that cross into disease claim territory
- [ ] Claims made on social media, influencer posts, and third-party channels are covered by substantiation files

**⟁ CLARIFY** — If substantiation files are not available or are incomplete:

- "No substantiation documentation has been provided for [claims X, Y, Z]. Should I:
  (A) Classify these claims as NON-COMPLIANT pending receipt of documentation?
  (B) Describe what documentation would be needed and classify as PARTIAL?
  (C) Assume adequate substantiation exists and proceed on that basis (higher risk)?"

---

#### Pillar 2: Disclosures and Transparency

**Legal basis:**

- US: FTC Endorsement Guides (16 C.F.R. Part 255, 2023 update); FTC .COM Disclosures Guidance (2013) [VERIFY if updated]; FTC Native Advertising Enforcement Policy Statement (2015); FTC Consumer Review Rule (effective October 21, 2024)
- EU: UCPD Art. 7 (misleading omissions, including commercial intent); Omnibus Dir. 2019/2161 (paid search rankings, fake reviews); EmpCo Dir. 2024/825 (sustainability labels)
- UK: CAP Code Section 2 (ads must be obviously identifiable); ASA influencer disclosure guidance

**Disclosure trigger analysis:**

_When is a material connection disclosure required?_

A disclosure is required whenever:

1. There is a material connection between the endorser/creator and the brand (payment,
   free product, discount, affiliate commission, brand relationship, employment), AND
2. A significant minority of the audience (FTC guidance: as low as ~10%) would not
   understand or expect that connection to exist

_Clear and conspicuous standard (US FTC):_

- Difficult to miss and easily understood
- Same medium as the endorsement (audio disclosure for audio; visual + audio for video)
- Positioned before engagement with the content, not at the end
- Not buried in hashtags, behind "read more" links, or in profile bios
- Platform-provided labels (e.g., Instagram "Paid Partnership" tag) are a helpful tool
  but may not be sufficient standing alone if the audience would not understand its meaning
- Must be tailored to audience language if non-English speaking

_Acceptable disclosure labels:_ "Ad," "#ad," "Advertisement," "Paid Partnership with [Brand],"
"Sponsored," "Sponsored Advertisement" (in clear contexts)

_Insufficient labels (UK ASA guidance; FTC guidance):_ "#gifted," "#sp," "#collab,"
"#ambassador," "#partner," "in association with" — these are ambiguous and enforcement
has found them inadequate

_Video disclosure requirements:_

- Disclosure must appear at the **start** of the video, not the end
- Must be superimposed on screen AND stated verbally (or clearly on screen with adequate duration)
- Cannot require pause or expansion to read

**Pillar 2 review checklist:**

- [ ] All paid, gifted, and affiliate relationships identified in materials
- [ ] Material connection disclosed in every individual post/asset (profile bio alone is insufficient)
- [ ] Disclosure appears before audience engagement with content (beginning of video; top of post)
- [ ] Disclosure language passes "clear and conspicuous" test in each medium and channel
- [ ] No deceptive formatting — sponsored content not formatted to resemble organic editorial
- [ ] Native advertising: disclosure appears before consumer engages; "Sponsored Advertising Content" or "Advertisement" (not ambiguous "Promoted" or "Presented by") [VERIFY FTC current list]
- [ ] Paid search: search ad placement paid-for promotions clearly labeled
- [ ] CAN-SPAM (email): from/to/reply-to accurate; subject line non-deceptive; physical address present; opt-out mechanism clear and functional; "advertisement" identifier present (unless prior affirmative consent)
- [ ] Price promotions: EU/UK "prior price" for claimed discounts is the lowest price in prior 30 days [VERIFY Omnibus implementation dates per Member State]
- [ ] Sustainability labels: label is based on recognized certification or public authority standard (EmpCo Dir. 2024/825, Annex I)
- [ ] Consumer reviews: no incentivized reviews without disclosure; no suppression of negative reviews; no insider reviews without clear conflict-of-interest disclosure; no AI-generated fake reviews (FTC Consumer Review Rule, effective Oct. 21, 2024)

**⟁ CLARIFY** — For influencer campaigns:

- "Do the influencer contracts for this campaign include disclosure obligations? If contracts
  are available, I can review them as part of the Pillar 4 (Third-Party Compliance) assessment."
- "Are there campaign materials showing how disclosures are actually being made in the live
  posts? Screenshots or examples would allow me to assess placement and prominence."

---

#### Pillar 3: Audience and Vulnerability Protection

**Legal basis:**

- US: COPPA (15 U.S.C. § 6501; 16 C.F.R. Part 312, 2025 amendments effective June 23, 2025; full compliance required April 22, 2026); CARU Guidelines (effective January 1, 2022; 2024 AI compliance warning); FTC Act § 5 unfairness standard (exploiting vulnerable populations)
- EU: UCPD Arts. 5(3), 8–9 (vulnerable groups; aggressive practices); EmpCo Dir. 2024/825
- UK: CAP Code Sections 5 and 5H (children's advertising); BCAP Code Sections 5 and 5H; CAP Code Section 3.39 (exploitation of vulnerable persons)

**Children's advertising assessment:**

_Is this advertising directed to children?_ Apply the mixed-audience test:

- **Child-directed**: Primary audience is children under 13 (US COPPA) / under 12 or 13 (CARU) — strongest protections apply
- **General audience with child appeal**: Content or platform attracts children — partial protections; COPPA actual knowledge standard
- **Teen (13–17) audience**: GDPR Art. 8 age of digital consent (16, or lower with Member State variation to 13); emerging COPPA/state law protections

_COPPA 2025 amendments (effective June 23, 2025; full compliance April 22, 2026) [VERIFY]_:

- Behavioral advertising to children now requires **separate verifiable parental consent**
  (cannot bundle into general consent)
- Persistent identifiers (cookies, device IDs) for behavioral advertising to children prohibited
  without parental consent; internal operations exception narrowed
- Biometric data of children added to protected categories
- Targeted advertising to under-13s using third-party ad networks without parental consent: NON-COMPLIANT

_CARU review checklist (applies to child-directed advertising in all media):_

- [ ] Product accurately represented (size, performance, features — especially toys)
- [ ] No high-pressure selling tactics (urgency, fear, shame, peer pressure)
- [ ] Clearly distinguishes advertising from content / gameplay / editorial
- [ ] No in-app/in-game purchase pressure on children
- [ ] Testimonials from children do not create unrealistic peer expectations
- [ ] Characters/influencers used in child-directed content are not using the product in a deceptive way
- [ ] Healthy food standards followed if food/beverage is advertised to children
- [ ] AI-generated content complies with all CARU standards (2024 CARU AI compliance warning)

_Vulnerability protection — general (all audiences):_

- [ ] No exploitation of financial distress, mental health vulnerability, bereavement, age-related cognitive decline
- [ ] Financial product advertising does not target financially vulnerable consumers with deceptive claims
- [ ] No aggressive commercial practices: harassment, coercion, undue influence (UCPD Arts. 8–9)
- [ ] No pressure sales techniques exploiting urgent circumstances
- [ ] UCPD Annex I blacklist: no bait-and-switch; no false "limited time" claims to deprive consumers of decision time; no false claim of curing illness

**⟁ CLARIFY** — If the product targets or has appeal to children:

- "Does this campaign or platform collect personal data from users who may be under 13?
  If yes, COPPA compliance (including the 2025 behavioral advertising amendments) must
  be assessed immediately. This may be a CRITICAL DEFICIENCY if behavioral advertising
  to under-13s is occurring without parental consent."

---

#### Pillar 4: Third-Party Compliance — Influencers, Agencies, and Affiliates

**Legal basis:**

- US: FTC Endorsement Guides (2023) — both brand and influencer/endorser may be liable;
  FTC Consumer Review Rule (2024); FTC Act § 5
- EU: UCPD Art. 7(2) — commercial intent disclosure obligation; brand/agency may be
  co-responsible for influencer's non-disclosure
- UK: CAP Code — advertiser is responsible for ensuring ads comply regardless of production source

**Foundational principle — Non-delegable compliance responsibility:**
A brand cannot escape liability by delegating advertising creation or distribution to
an agency, influencer, or affiliate. The brand retains primary responsibility for the
compliance of all advertising made on its behalf. Third-party reliance is permitted as
a practical matter but does not transfer legal responsibility.

**Influencer partnership assessment:**

_Pre-engagement due diligence:_

- [ ] Influencer background reviewed: prior FTC/ASA complaints or enforcement?
- [ ] Platform account authenticity verified: follower counts and engagement real?
- [ ] Influencer audience demographics assessed for potential children's audience overlap

_Contract review:_

- [ ] Disclosure obligations explicitly required in contract (specific language, placement, format)
- [ ] Substantiation for any product performance claims shared with influencer before posting
- [ ] Influencer bound to use claim-specific language consistent with substantiation files
- [ ] Brand review/approval right over posts containing objective product claims
- [ ] Contract specifies that influencer must not make claims not in the approved brief
- [ ] Termination right for non-compliance with disclosure and substantiation requirements
- [ ] Record-keeping requirements for posts (screenshots, archiving)

_Post-publication monitoring:_

- [ ] Live influencer posts monitored against contracted disclosure and claim requirements
- [ ] Non-compliant posts flagged and influencer notified with take-down/correction timeline
- [ ] Evidence of correction documented in compliance file

**Agency compliance:**

- [ ] Agency agreement requires compliance with FTC Act, CAP Code, UCPD, and applicable advertising law
- [ ] Agency provides substantiation documentation for any claims it originates
- [ ] Brand retains right to audit agency-produced materials for compliance
- [ ] Agency's pre-clearance procedures reviewed

**Affiliate network compliance:**

- [ ] Affiliate agreements prohibit use of unsubstantiated claims or misleading copy
- [ ] Brand's substantiation library made available to affiliates to use (no improvisation)
- [ ] Audit process in place for affiliate ad copy before it goes live
- [ ] Non-compliant affiliate content take-down mechanism documented

**User-generated content (UGC) and review programs:**

- [ ] No incentivized reviews conditioned on positive sentiment (FTC Consumer Review Rule 2024)
- [ ] Insider reviews (employee, agency, family) disclosed as such
- [ ] No suppression of negative reviews through legal threats or selective publication
- [ ] AI-generated reviews prohibited (FTC Consumer Review Rule)
- [ ] Seeding campaigns (sending product for unsolicited reviews) assessed: if brand has
      editorial influence over review content, disclosure is required

**⟁ CLARIFY** — For influencer programs:

- "How many influencer partners does this campaign involve? For programs with 20+ influencers,
  I can outline a monitoring sampling approach rather than individual review."
- "Are influencer contracts available for review? If not, I can assess the required
  contractual elements that should be present."

---

#### Pillar 5: Monitoring, Program Architecture, and Enforcement Response

**Legal basis:**

- US: FTC Act § 5; FTC Compliance Program considerations in penalty assessments; Penalty
  Offense Authority (prior notice required for civil penalties up to $51,744 per violation [VERIFY])
- EU: UCPD; penalties up to 4% of annual turnover in affected Member State(s) or €2M
  minimum [VERIFY national implementing legislation]; EmpCo Dir. 2024/825 same penalty framework
- UK: DMCCA 2024; ASA enforcement escalation to Trading Standards and CMA

**Program architecture review:**

| Element                                   | Present? | Quality | Gap |
| ----------------------------------------- | -------- | ------- | --- |
| Claims approval workflow                  |          |         |     |
| Substantiation library / database         |          |         |     |
| Pre-launch legal review gate              |          |         |     |
| Influencer compliance protocol            |          |         |     |
| Affiliate compliance protocol             |          |         |     |
| Email/SMS consent management              |          |         |     |
| Consumer complaint tracking (advertising) |          |         |     |
| Post-launch monitoring process            |          |         |     |
| Incident response procedure               |          |         |     |
| Annual compliance training                |          |         |     |
| Regulatory change monitoring              |          |         |     |

**Pre-launch review process:**

- [ ] Defined approval gate before any new campaign or claim goes live
- [ ] Claims reviewed against substantiation library at approval gate
- [ ] Legal pre-clearance for health claims, comparative claims, environmental claims
- [ ] High-risk claim categories (health, green, financial) flagged for elevated review

**Post-launch monitoring:**

- [ ] Live ads monitored against approved campaign brief
- [ ] Social media posts and influencer content sampled post-publication
- [ ] Customer/consumer complaints about advertising claims tracked and triaged
- [ ] Competitor advertising tracked for parity claim verification needs
- [ ] Substantiation evidence refreshed when material changes in the product or evidence base occur

**Email/SMS consent management:**

_CAN-SPAM (US email):_

- [ ] Opt-out mechanism functional, processes within 10 business days
- [ ] Opted-out addresses not re-added without fresh affirmative consent
- [ ] Physical postal address in every commercial email
- [ ] From/to/reply-to information accurate and non-deceptive

_TCPA (US text/phone):_

- [ ] Prior express written consent (PEWC) obtained before automated text marketing
      to wireless numbers (consent elements: signed agreement, clear disclosure of autodialed/
      prerecorded contacts, disclosure that consent is not a purchase condition) [VERIFY]
- [ ] National DNC Registry scrubbed at least every 31 days
- [ ] Internal DNC list maintained; opt-out requests honored immediately
- [ ] Calling/texting only between 8 a.m.–9 p.m. local time of recipient (FL: 8 a.m.–8 p.m.)
- [ ] State mini-TCPA compliance assessed: FL FTSA frequency cap (max 3 per 24 hours);
      OK OTSA frequency cap (max 3 per 24 hours) [VERIFY current state law landscape]

_EU/UK electronic marketing (GDPR + ePrivacy/PECR):_

- [ ] Opt-in consent obtained before email/SMS marketing to individual (B2C) contacts
- [ ] Soft opt-in (existing customer relationship) exception documented if relied upon
- [ ] Opt-out from future marketing honored; records maintained
- [ ] [JURISDICTION-SPECIFIC] Verify national ePrivacy Directive implementation

**Incident response:**

- [ ] Process defined for responding to FTC inquiry, ASA complaint, or state AG contact
- [ ] Voluntary correction / corrective advertising procedures documented
- [ ] Escalation path from compliance team to General Counsel to executive leadership clear
- [ ] Records preservation triggered upon receipt of formal inquiry or complaint
- [ ] Outside counsel relationship established for advertising law matters

### Step 6: Classify Findings

Using the **Compliance Classification System** below, assign a classification to each
finding from the Five Pillars, then derive an overall program classification.

**⟁ CLARIFY** — For borderline classifications:

- "This finding [X] could be classified as PARTIAL or NON-COMPLIANT depending on
  whether [context factor]. Based on your [product / audience / regulatory history], I'm
  recommending [classification]. Do you agree, or should I re-analyze with a different
  assumption?"
- "I've found multiple PARTIAL findings across several pillars. Should I apply a
  conservative classification (aggregate partial = NON-COMPLIANT) or assess each
  independently?"

### Step 7: Quality Verification

Before delivering the assessment, run all checks in the **Quality Assurance Framework**:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every CRITICAL DEFICIENCY finding, run the 3-pass Self-Interrogation. Revise if any pass reveals a weakness.
3. Assign Confidence Scores to each material finding.
4. Verify that all five pillars have been addressed (present or flagged as not applicable).
5. Verify no jurisdiction-specific claims are stated as universal standards.
6. Generate the Glass Box Audit Trail.

### Step 8: Deliver Assessment

Produce the output using the **Output Format Template** below. Deliver:

1. The formatted assessment report
2. The Glass Box Audit Trail (appended)
3. An executive summary suitable for senior leadership or board presentation (if Mode C or D)

---

## Compliance Classification System

### COMPLIANT

Claims fully substantiated per applicable standard (FTC/CARSE/EU/UK) **before**
dissemination. Disclosures clear, conspicuous, appropriately placed. Third-party
compliance documented. Consent and opt-out programs functional. Monitoring active.
Regulatory exposure: minimal (defensible in audit; adequate program evidence available).

_Examples:_

- Health claim backed by two adequate RCTs; expert reviewed; substantiation file dated before launch
- Influencer posts begin with "#ad" or "Advertisement" superimposed; no content buried
- TCPA PEWC documentation complete; DNC scrubbed within 31 days; opt-outs processed within 10 days
- Carbon offset claim states specific offset registry, additionality basis, and scope; verified by accredited third party

### PARTIAL

Most claims substantiated; disclosures present but timing, placement, or language is
suboptimal; third-party documentation incomplete; some monitoring gaps; consent records
present but incomplete. Correctable before escalation to enforcement risk. Regulatory
exposure: moderate (FTC warning letter or ASA informal resolution possible; corrective
action achievable without campaign suspension).

_Examples:_

- Health claim substantiated by one adequate RCT (second study would strengthen position)
- Influencer disclosures present but placed at end of posts or require "read more" expansion
- DNC scrubbed every 45 days instead of required 31 days
- "Sustainable" claim limited to packaging materials without full lifecycle evidence

### NON-COMPLIANT

Material claims unsubstantiated or inadequately substantiated; material disclosures
missing or buried; no third-party oversight documentation; no functional consent or
opt-out programs; no monitoring. Enforcement risk elevated — FTC formal complaint, ASA
upheld ruling, or state AG action likely without prompt remediation. Campaign correction
or suspension may be required.

_Examples:_

- Health claims with no substantiation file or only anecdotal consumer testimonials
- Influencer posts with no disclosure despite paid partnership
- Behavioral advertising to children under 13 without parental consent (pre-COPPA 2025
  amendment date: existing COPPA standard; post-June 23, 2025: 2025 standard applies)
- Email marketing without functioning opt-out mechanism or physical address
- "Eco-friendly" or "carbon neutral" applied to entire product line without evidence

### CRITICAL DEFICIENCY

Campaign fundamentally misrepresents the product or service in a way likely to cause
consumer harm. Claims designed to evade compliance controls. Material facts intentionally
concealed. Vulnerable populations (children, financially distressed, elderly) targeted
with deceptive practices. **Immediate risk of FTC formal enforcement, state AG
investigation, private class action, ASA referral to Trading Standards, or CMA action.**
Campaign must be paused and legal counsel engaged immediately.

_Examples:_

- Disease treatment or cure claims on product that is not FDA-approved (drug claim without approval)
- Behavioral advertising to children under 13 combining data from multiple platforms without any parental consent mechanism
- Falsified consumer reviews or clinical evidence submitted to substantiation file
- TCPA violations: texting consumers on internal DNC list after opt-out request; mass texts without any PEWC
- Prior FTC Penalty Offense Notice received; same prohibited conduct continued — civil penalties of up to $51,744 per violation apply [VERIFY current amount]
- Pyramid promotional scheme with false earnings representations

---

## Quality Assurance Framework

### Citation Quality Gates

Run silently before delivering any output. If any gate fails, revise before delivery.

| Gate           | Rule                                                                                                                                                                                            | Fail Action                                |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **Source**     | Every regulatory claim cites a specific statute, regulation, enforcement action, or authoritative guidance document                                                                             | Add citation or mark "[UNVERIFIED]"        |
| **Format**     | All citations follow a consistent, recognizable format (e.g., "15 U.S.C. § 45," "16 C.F.R. Part 255," "UCPD Art. 6," "CAP Code Rule 3.7")                                                       | Fix format                                 |
| **Currency**   | Each cited provision checked for amendments, repeal, or pending revision (Green Guides update status; TCPA rulemaking status; COPPA 2025 effective dates; EmpCo Directive transposition status) | Flag "[CHECK CURRENCY — may have changed]" |
| **Domain**     | Analysis stays within the applicable jurisdiction framework; no cross-regime contamination (e.g., do not apply GDPR consent rules as if they were FTC rules)                                    | Remove or label [JURISDICTION-SPECIFIC]    |
| **Confidence** | Uncertainty explicitly stated; emergent doctrine distinguished from settled law                                                                                                                 | Add confidence qualifier per scale below   |

### Self-Interrogation for CRITICAL DEFICIENCY Findings

For every CRITICAL DEFICIENCY finding, apply this 3-pass review before finalizing:

**Pass 1 — Regulatory chain integrity**: Does the classification follow logically from the cited authority? Would the FTC, ASA, or relevant regulator actually cite this provision for this conduct? Is there a settled enforcement precedent?

**Pass 2 — Completeness**: Have all relevant authorities been considered, including safe harbors, exceptions, and industry-standard evidence thresholds? For health claims: have I considered whether puffery applies or whether the claim is a structure/function claim rather than a disease claim? For green claims: have I considered whether a qualified claim with adequate scope limitation would be compliant?

**Pass 3 — Challenge**: What is the strongest argument the advertiser could make that this classification is wrong? Under what circumstances might a regulator find the current practice acceptable or within an enforcement de-prioritization zone? What compensating controls or remediation actions would most effectively reduce risk?

**Outcome**: CONFIRMED (classification stands) or REVISED (reclassify with explanation).

### Confidence Scoring

| Level        | Range     | Meaning                                                                                                                                                                                      | Action                                                           |
| ------------ | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled regulatory requirement with clear enforcement precedent (e.g., FTC Act § 5 "deception" standard; COPPA parental consent requirement; CAN-SPAM opt-out processing)                    | State with confidence                                            |
| **High**     | 0.80–0.94 | Strong regulatory authority, minor interpretive questions (e.g., FTC Endorsement Guides; ASA disclosure standards; UCPD Art. 7 commercial intent)                                            | State with brief caveat                                          |
| **Probable** | 0.60–0.79 | Good authority, but interpretive or jurisdictional uncertainty exists (e.g., green claims substantiation standards for specific claim types; TCPA ATDS definition post-_Facebook v. Duguid_) | State with reasoning and contra-indicators                       |
| **Possible** | 0.40–0.59 | Genuine uncertainty — law evolving or enforcement guidance inconsistent (e.g., AI-generated advertising compliance; state mini-TCPA landscape outside FL/OK)                                 | Flag for professional legal review with both-sides analysis      |
| **Unlikely** | 0.0–0.39  | Speculative application of novel or unclear doctrine                                                                                                                                         | Do not assert; flag "[UNCERTAIN — professional review required]" |

### Glass Box Audit Trail Template

Append to every delivered assessment:

```yaml
glass_box:
  skill_name: "legalcode-advertising-marketing-compliance"
  assessment_date: "[YYYY-MM-DD]"
  mode: "[Pre-launch audit / Post-launch review / Program gap analysis / Incident response / Transaction diligence]"

  inputs:
    materials_reviewed: "[number and type of assets reviewed]"
    substantiation_files_reviewed: "[yes / no / partial]"
    contracts_reviewed: "[yes / no / partial]"

  regulatory_regimes_applied:
    - "[List each regime applied, e.g., 'FTC Act § 5 (US)', 'FTC Endorsement Guides 2023 (US)', 'UCPD 2005/29/EC (EU)', 'CAP Code (UK)']"

  legalcode_mcp: "Connected — citations marked VERIFIED | Not connected — citations require independent verification"
  research_reference_file: "[/tmp/legalcode-admarcom-authority.md | Not created]"

  citations:
    verified_count: "[number]"
    unverified_count: "[number — requires [VERIFY] tag]"
    check_currency_count: "[number of items flagged for currency verification]"

  assumptions:
    - "[Assumption 1: e.g., 'Assumed US Federal + EU + UK regimes apply based on user-stated markets']"
    - "[Assumption 2: e.g., 'Assumed product category is general consumer goods — health claims rules not applied']"
    - "[Any assumption about children's audience composition]"

  self_interrogation:
    critical_deficiency_count: "[number]"
    confirmed_count: "[number]"
    revised_count: "[number]"
    revised_notes: "[explain any reclassifications]"

  confidence_distribution:
    definite: "[count]"
    high: "[count]"
    probable: "[count]"
    possible: "[count]"
    unlikely: "[count]"

  privilege_note: "[None | 'Review conducted at direction of counsel — attorney-client privilege may apply. Findings should not be disclosed outside of privileged channel.']"

  limitations:
    - "[e.g., 'Green Guides update status not confirmed — 2012 version assumed current; verify before reliance']"
    - "[e.g., 'TCPA rulemaking status not confirmed — post-2025 rule landscape requires verification']"
    - "[e.g., 'State mini-TCPA landscape (beyond FL/OK) not comprehensively surveyed']"
    - "[e.g., 'No substantiation files provided — claims analysis is theoretical']"

  reviewer: "AI-assisted — requires review by qualified advertising law counsel before action"
```

---

## Anti-Patterns Catalogue

What NOT to do in advertising compliance. All patterns are empirically derived from
FTC enforcement actions, ASA rulings, and regulatory guidance.

### Substantiation Anti-Patterns

1. **Checkbox substantiation**: Substantiation files exist but have never been reviewed
   for whether the evidence actually supports the specific claim being made. A study on
   a different population, dosage, or outcome cannot substantiate a targeted claim.

2. **Animal study substitution**: Relying on animal or in-vitro studies to substantiate
   human efficacy claims. FTC CARSE requires human clinical evidence for consumer-directed
   health claims.

3. **Stale substantiation**: Substantiation collected 3+ years ago without refresh.
   Science evolves; if more recent studies contradict older evidence, the overall body of
   evidence may no longer support the claim.

4. **Implied claim blindness**: Treating a claim as "technically true" while ignoring
   the net impression. If "Reduces fine lines in 95% of users" is substantiated only in
   a study of 20 people over 1 week, the implied claim of broad efficacy is unsubstantiated.

5. **Influencer reliance trap**: Assuming the influencer holds the substantiation because
   they made the claim. The brand retains the obligation. If the influencer improvises a
   performance claim not in the brand brief, the brand must remove or disclaim the claim
   promptly.

6. **Structure/function boundary creep**: Gradually shifting language from safe
   structure/function claims ("supports healthy immune function") toward disease claims
   ("prevents colds and flu") over successive campaign iterations without recognizing when
   the boundary is crossed.

7. **"Our product is better" without test data**: Comparative superiority claims ("rated
   #1," "outperforms [Competitor]") made without head-to-head testing using accepted
   industry methodology. "Better" is only puffery if entirely subjective; specific
   comparative claims require evidence.

8. **Green claims via offsets alone**: Claiming "carbon neutral" or "net zero" based
   solely on purchasing carbon offsets, without disclosing the offset type, registry,
   additionality, and methodology. Post-EmpCo Directive (Sep. 27, 2026), this is
   prohibited in the EU regardless of disclosure [VERIFY]. [JURISDICTION-SPECIFIC]

9. **Generic sustainability labels**: Applying "eco-friendly," "green," "sustainable,"
   or "natural" to products without lifecycle evidence supporting the claim for all
   material environmental attributes. These unqualified absolute claims are per se
   misleading under the EmpCo Directive (Annex I blacklist addition from Sep. 2026) and
   subject to FTC scrutiny under the Green Guides.

10. **Testimonial overreach**: Publishing a single consumer testimonial showing
    exceptional results without disclosing that results are atypical. "Results not typical"
    alone is not safe harbor under FTC 2023 guidance; the ad must not convey a false
    general impression about typical results.

### Disclosure Anti-Patterns

11. **Fine print burial**: A prominent headline claim is contradicted or materially
    qualified by a disclosure in 6-point type at the bottom of the page or screen. If the
    overall net impression is misleading, a buried disclosure does not cure it.

12. **End-of-video disclosure**: Influencer videos where the "#ad" disclosure appears
    only in end cards or end-of-description text. FTC and ASA both require disclosure
    before engagement — at the start of videos.

13. **Profile bio disclosure substitution**: Influencer places "works with brands" or
    "#ambassador" in their bio, then makes individual posts without per-post disclosure.
    Bio disclosure is insufficient; each individual post requires disclosure.

14. **Platform label reliance**: Relying on Instagram's "Paid Partnership" feature or
    similar platform labels as the sole disclosure mechanism, without considering whether
    the label is sufficiently conspicuous and whether the target audience understands its
    meaning. ASA has found platform labels insufficient in some circumstances.

15. **Ambiguous disclosure language**: Using "#sp," "#gifted," "#collab," "#partner,"
    "Thanks [Brand]," or similar ambiguous labels. These are insufficient under FTC and
    ASA standards. Clear, unambiguous terms — "Ad," "#ad," "Advertisement," "Sponsored" —
    are required.

16. **Native content design mimicry**: Producing sponsored content in exact visual style
    of the platform's or publisher's organic content, with disclosure only in metadata or
    on a separate disclosure page. If the format is indistinguishable from editorial, the
    disclosure is insufficient.

17. **Affiliate link opacity**: Disclosing affiliate relationships in terms of service,
    account bio, or a separate "disclosure policy" page rather than proximate to the
    specific recommendation. Disclosure must be in reasonable proximity to the claim.

### Audience Protection Anti-Patterns

18. **Child audience miscalculation**: Advertising on platforms where the audience is
    a significant proportion of children (gaming, children's YouTube, certain TikTok content)
    without triggering COPPA analysis. COPPA "directed to children" analysis considers
    not just the target audience but the platform's known child audience.

19. **COPPA behavioral advertising post-2025**: Continuing to serve targeted ads to
    under-13s on child-directed platforms after June 23, 2025, without verifiable parental
    consent, on the assumption that prior practices are grandfathered. The 2025 COPPA
    amendments require separate consent for behavioral advertising regardless of prior
    practices. [VERIFY effective dates and compliance deadlines]

20. **Vulnerability targeting by design**: Using programmatic ad targeting parameters
    (e.g., users searching for "debt relief," "payday loans," "cancer treatment") to
    deliver materially misleading claims to consumers precisely because they are vulnerable.
    FTC unfairness doctrine applies when consumers cannot reasonably avoid the harm.

### Third-Party Anti-Patterns

21. **Agency compliance delegation**: Executing an agency statement of work without
    advertising compliance requirements, then assuming the agency handles all compliance
    obligations. The brand is always the responsible advertiser; the agency contract must
    specify compliance obligations and audit rights.

22. **Influencer contract void of substantiation requirements**: Paying influencers
    to recommend products without providing approved claim language or substantiation,
    and without contractually prohibiting improvised health, performance, or comparative claims.

23. **Affiliate network fire-and-forget**: Enabling an affiliate program, distributing
    creative assets, and never reviewing affiliate-generated ad copy for claim accuracy
    or disclosure compliance. Affiliate ad copy that makes false claims implicates the brand.

24. **UGC review program misclassification**: Running a program that asks customers to
    post reviews in exchange for product, discounts, or other benefits, without requiring
    disclosure of the benefit — on the theory that you "didn't ask for positive reviews."
    The FTC Consumer Review Rule (2024) prohibits incentivized reviews without disclosure
    of the material connection.

25. **Fake review commissioning**: Using AI-generated reviews, purchasing reviews from
    review farms, or seeding fake testimonials — whether under the brand's name or via
    third parties. Prohibited by FTC Consumer Review Rule (2024); UCPD Omnibus Directive
    blacklist; ASA enforcement.

### Monitoring Anti-Patterns

26. **Pre-launch-only review**: Claims reviewed at launch and never revisited as new
    studies emerge, the product formulation changes, competitor claims evolve, or regulatory
    guidance updates. Substantiation is an ongoing obligation, not a one-time event.

27. **Social post monitoring gap**: Ads approved for TV or display, but identical or
    adapted copy deployed on social media without equivalent compliance review. Social
    channels are subject to the same legal standards.

28. **Competitor parity reasoning**: Adopting a competitor's claim ("Competitor says X,
    so we can say X too") without independent verification. A competitor's non-compliant
    claim does not create a safe harbor; it may indicate an industry-wide enforcement sweep
    is forthcoming.

29. **Complaint-as-only-monitoring**: Relying solely on consumer complaints to identify
    compliance issues rather than proactive sampling. By the time a formal complaint is
    received, the non-compliant ad may have been running for months.

30. **No corrective advertising plan**: Organization has no pre-established procedure
    for what to do if a campaign is found to be non-compliant. Delayed response after
    FTC inquiry or ASA complaint significantly worsens regulatory outcomes.

---

## Writing Standards

Apply before delivering any output from this skill:

1. **Claim-specific language**: Every finding must identify the specific claim, channel,
   and asset where the issue was found. "The email campaign" is insufficient; "Email
   campaign dated [X], subject line '[Y]'" is required.

2. **Jurisdiction-labeling discipline**: When a standard applies in one jurisdiction but
   not another, label it explicitly: "[US FTC only]," "[EU only — EmpCo Dir. 2024/825],"
   "[UK ASA only]." Do not imply universal application.

3. **Severity consistency**: Do not downgrade a CRITICAL DEFICIENCY finding to avoid
   alarm. The classification must reflect the actual risk. If the finding implicates
   a prior Penalty Offense Notice, COPPA children's behavioral advertising, or material
   misrepresentation, maintain the CRITICAL classification regardless.

4. **Actionable remediation**: Every finding must include a specific, actionable remediation
   step with a recommended timeline, not just a description of the problem. "Revise
   disclosure" is insufficient; "Add '#ad' to the beginning of all current and future
   influencer posts for this campaign within 5 business days; update influencer contract
   template for future engagements" is adequate.

5. **Confidence qualification**: Do not state an emerging or contested doctrine as settled
   law. If the law is evolving (TCPA ATDS definition, green claims standards, AI advertising
   rules), say so with a confidence qualifier.

6. **No jurisdiction bleed**: Do not apply GDPR consent requirements to US-only email
   programs, or FTC substantiation doctrine to EU-specific health claims governed by
   Regulation 1924/2006. Maintain clean analytical separation between regimes.

7. **Plain language for remediation roadmap**: The remediation roadmap should be
   understandable by marketing, product, and business teams — not just legal counsel.
   Translate regulatory requirements into operational actions.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

Before Step 5, search legalcode-mcp for:

- Current FTC enforcement releases (last 12–24 months) matching the product category and
  claim types under review
- Most recent ASA rulings on claims similar to those being assessed
- Current EU UCPD enforcement sweeps and EDPB guidance relevant to advertising
- State AG enforcement activity in California, New York, Texas, and Florida for the
  product category
- Current status of any pending rulemaking (Green Guides update; TCPA rulemaking; COPPA
  enforcement actions under 2025 amendments)

Mark all legalcode-mcp-sourced citations as **VERIFIED** in the Glass Box audit trail.

**Without legalcode-mcp:**

- Mark all statutory and regulatory citations with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Flag with [CHECK CURRENCY] in particular:
  - FTC civil penalty per-violation amounts (inflation-adjusted annually)
  - Green Guides update status
  - TCPA rulemaking status
  - COPPA 2025 amendment effective dates and compliance deadlines
  - EmpCo Directive 2024/825 Member State transposition status
  - State mini-TCPA law landscape beyond Florida and Oklahoma
- Proceed with assessment; flag limitations in Glass Box

---

## Localization Notes

### Jurisdiction-Specific Items Requiring Local Research

| Topic                               | US                                                         | EU                                                                                          | UK                                                             |
| ----------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Influencer disclosure label**     | "#ad" or "Advertisement" (FTC)                             | "Werbung"/"Publicité"/local equivalent — national guidance varies [VERIFY per Member State] | "#ad" or "Ad" (ASA); "#gifted" insufficient                    |
| **Prior price for discounts**       | No federal equivalent (state UDAP vary)                    | Lowest price in prior 30 days (Omnibus Dir.) [VERIFY Member State implementation]           | DMCCA 2024 implements Omnibus standard                         |
| **Health claims (food)**            | CARSE standard; FDA structure/function disclaimer          | EU Regulation 1924/2006 positive list (EFSA-authorized claims only)                         | GB NHC Register (post-Brexit positive list)                    |
| **Green claims threshold**          | FTC Green Guides (2012); unqualified absolute claims risky | EmpCo Dir. blacklist (Sep. 2026); UCPD Art. 6 already applies                               | ASA: absolute claims require lifecycle evidence (enforced now) |
| **Email marketing consent**         | CAN-SPAM: opt-out model                                    | GDPR + ePrivacy: opt-in required (B2C)                                                      | PECR + UK GDPR: opt-in required (B2C)                          |
| **SMS marketing consent**           | TCPA PEWC; DNC Registry                                    | GDPR + ePrivacy: opt-in                                                                     | PECR + UK GDPR: opt-in                                         |
| **Children's advertising (online)** | COPPA (under-13); CARU                                     | GDPR Art. 8 (age of consent 13–16 per Member State)                                         | PECR; UK GDPR; CAP Code child audience rules                   |
| **Penalty scale**                   | Up to $51,744/violation (FTC) [VERIFY current]             | Up to 4% annual turnover or €2M minimum                                                     | ASA: reputational; CMA: up to 10% global turnover              |

---

## Output Format Template

```markdown
# Advertising & Marketing Compliance Assessment

**Organization**: [Name]
**Assessment Date**: [YYYY-MM-DD]
**Mode**: [Pre-launch audit / Post-launch review / Program gap analysis / Incident response / Transaction diligence]
**Materials Reviewed**: [List assets, documents, or program elements reviewed]
**Regimes Applied**: [FTC Act § 5 / FTC Endorsement Guides 2023 / EU UCPD / UK CAP Code / CAN-SPAM / TCPA / COPPA / Other]
**Assessed by**: legalcode-advertising-marketing-compliance (AI-assisted — requires legal review)

---

## Executive Summary

**Overall Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]

| Pillar                                  | Classification | Findings Count |
| --------------------------------------- | -------------- | -------------- |
| 1. Substantiation & Claims Verification | [tier]         | [N findings]   |
| 2. Disclosures & Transparency           | [tier]         | [N findings]   |
| 3. Audience & Vulnerability Protection  | [tier]         | [N findings]   |
| 4. Third-Party Compliance               | [tier]         | [N findings]   |
| 5. Monitoring & Program Architecture    | [tier]         | [N findings]   |

**Top 3 Priority Actions:**

1. [Most critical finding — CRITICAL DEFICIENCY or NON-COMPLIANT, with immediate action]
2. [Second priority]
3. [Third priority]

**Jurisdiction Compliance Summary:**

| Regime                   | Overall Status | Critical Issues |
| ------------------------ | -------------- | --------------- |
| US FTC / Federal         | [status]       | [yes/no]        |
| US State UDAP            | [status]       | [yes/no]        |
| EU UCPD                  | [status]       | [yes/no]        |
| UK CAP Code              | [status]       | [yes/no]        |
| CAN-SPAM (if applicable) | [status]       | [yes/no]        |
| TCPA (if applicable)     | [status]       | [yes/no]        |
| COPPA (if applicable)    | [status]       | [yes/no]        |

---

## Pillar Assessments

### Pillar 1: Substantiation and Claims Verification

**Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]

| Claim          | Claim Type | Substantiation Status               | Classification | Finding       |
| -------------- | ---------- | ----------------------------------- | -------------- | ------------- |
| "[Claim text]" | [Type]     | [Documented / Inadequate / Missing] | [Tier]         | [Description] |

**Findings:**

#### Finding 1.1 — [Classification] — [Brief title]

- **Claim**: "[Exact claim text]"
- **Applicable rule**: [FTC / EU / UK standard and citation]
- **Issue**: [Description of the substantiation gap]
- **Confidence**: [Level and score]
- **Remediation**: [Specific action]
- **Timeline**: [IMMEDIATE / 15 days / 30 days / 60 days]
- **Owner**: [Legal / Marketing / Medical/Scientific Affairs]

[Repeat for each finding]

---

### Pillar 2: Disclosures and Transparency

**Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]

[Same structure: summary table, then individual findings]

---

### Pillar 3: Audience and Vulnerability Protection

**Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]

[Same structure]

---

### Pillar 4: Third-Party Compliance

**Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]

[Same structure]

---

### Pillar 5: Monitoring and Program Architecture

**Classification**: [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]

**Program Maturity Assessment:**

| Element                        | Status                       | Gap           | Priority              |
| ------------------------------ | ---------------------------- | ------------- | --------------------- |
| Claims approval workflow       | [Present / Absent / Partial] | [description] | [HIGH / MEDIUM / LOW] |
| Substantiation library         |                              |               |                       |
| Influencer compliance protocol |                              |               |                       |
| Email/SMS consent management   |                              |               |                       |
| Post-launch monitoring         |                              |               |                       |
| Incident response procedure    |                              |               |                       |
| Compliance training            |                              |               |                       |

---

## Remediation Roadmap

### IMMEDIATE (0–5 business days) — CRITICAL DEFICIENCY items

| #   | Finding             | Action            | Owner   | Success Metric             |
| --- | ------------------- | ----------------- | ------- | -------------------------- |
| 1   | [Finding reference] | [Specific action] | [Owner] | [How to verify completion] |

### NEAR-TERM (15–30 days) — NON-COMPLIANT items

| #   | Finding | Action | Owner | Success Metric |
| --- | ------- | ------ | ----- | -------------- |

### STANDARD (31–60 days) — PARTIAL items

| #   | Finding | Action | Owner | Success Metric |
| --- | ------- | ------ | ----- | -------------- |

### BACKGROUND (60–90 days) — Program architecture improvements

| #   | Element | Action | Owner | Success Metric |
| --- | ------- | ------ | ----- | -------------- |

---

## Glass Box Audit Trail

[Insert YAML from template above]

---

_This assessment was produced using the legalcode-advertising-marketing-compliance skill
(AI-assisted). It does not constitute legal advice. All findings should be reviewed by
qualified advertising law counsel licensed in the relevant jurisdiction before action is
taken. Regulatory requirements change; verify all citations before relying on them._
```

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis based on deep research of US
(FTC, CAN-SPAM, TCPA, COPPA), EU (UCPD, Omnibus Directive, EmpCo Directive 2024/825,
EU Regulation 1924/2006), and UK (ASA/CAP Code, BCAP Code, DMCCA 2024) advertising and
marketing regulatory frameworks. Structural patterns and quality frameworks adopted from
the Legalcode compliance skill reference architecture (`legalcode-anti-bribery-compliance`,
`legalcode-aml-kyc-compliance`, `legalcode-hipaa-compliance-assessment`, and the
`legalcode-contract-review` gold standard). Legal research conducted via web search of
primary regulatory sources, FTC guidance documents, ASA published rulings, EUR-Lex, and
authoritative practitioner commentary. All citations require independent verification
against current primary sources before professional reliance.
