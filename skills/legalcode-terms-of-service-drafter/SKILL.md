---
name: legalcode-terms-of-service-drafter
description: >
  Draft and review Terms of Service agreements for SaaS, web, and mobile platforms —
  generate jurisdiction-compliant terms covering account eligibility, acceptable use,
  user-generated content licensing, intellectual property, subscription and billing,
  auto-renewal disclosure, limitation of liability, dispute resolution, and governing law.
  Use when drafting consumer-facing or B2B platform terms, auditing existing TOS for
  regulatory compliance gaps, updating TOS for new regulatory requirements (DSA, DMA,
  UK DMCCA, AU unfair terms, US auto-renewal laws), creating B2B vs B2C variants, or
  generating jurisdiction-specific supplements for EU, UK, AU, CA, and US. Covers COPPA
  age gating, CAN-SPAM email compliance, DMCA safe harbor conditions, FTC Section 5
  unfair practices, Section 230 platform immunity conditions, DSA Arts. 14-27 platform
  transparency requirements, Consumer Rights Directive withdrawal rights, ACL unfair terms
  civil penalties, CASL express consent, and arbitration/class action waiver enforceability.
  Produces structured, confidence-scored drafting guidance with Glass Box audit trail.
allowed-tools: Read, Bash(grep:*), Glob
model: claude-opus-4-5-20251101
context: fork
agent: general-purpose
---

# Legalcode Terms of Service Drafter

> **Disclaimer**: This skill provides a framework for AI-assisted Terms of Service drafting
> and compliance review. It does not constitute legal advice. All outputs should be reviewed
> by a qualified legal professional licensed in the relevant jurisdiction(s) before publication
> or enforcement. Laws governing online platforms, consumer protection, and digital services
> evolve rapidly — verify compliance obligations against current regulatory guidance before
> finalizing any Terms of Service. Statutory and case law references cited from memory carry
> hallucination risk — verify against authoritative sources before relying on them. Consumer
> protection rules, especially for minors (COPPA, state AADC laws), auto-renewal, arbitration
> clauses, and unfair terms, are subject to active regulatory enforcement and litigation.
> Cross-border platforms may face conflicting requirements across jurisdictions — seek
> multi-jurisdictional counsel for global deployments.

---

## Purpose and Scope

This skill drafts, reviews, and audits Terms of Service (also called Terms of Use, User
Agreements, or Platform Terms) for SaaS applications, web platforms, and mobile apps.
It provides clause-by-clause drafting guidance, identifies mandatory disclosures by
jurisdiction, flags compliance gaps in existing terms, and surfaces platform-specific risks
across account management, content moderation, billing, and dispute resolution.

**Covers:**
- **Account and Eligibility**: Age verification, COPPA and KOSA obligations, parental consent,
  corporate entity account acceptance, identity verification requirements
- **Acceptable Use Policies (AUP)**: Prohibited conduct, content restrictions, anti-abuse
  provisions, suspension and termination triggers, enforcement discretion language
- **User-Generated Content (UGC)**: License grants to platform, content ownership retention,
  AI training data use restrictions, DMCA takedown procedures, moral rights handling
- **Intellectual Property**: Platform IP ownership, user content license scope, output
  ownership for AI-assisted tools, trademark and trade dress provisions
- **Subscription and Billing**: Pricing, payment terms, free trials, plan upgrades/downgrades,
  proration, failed payment handling, tax treatment
- **Auto-Renewal**: Conspicuous disclosure requirements, cancellation mechanics,
  click-to-cancel compliance (US state laws, FTC Rule, EU CRD, AU ACL)
- **Limitation of Liability and Warranty Disclaimers**: Aggregate caps, exclusions of
  consequential damages, jurisdictional enforceability, consumer guarantee carve-outs
- **Dispute Resolution**: Arbitration agreements, class action waivers, mass arbitration
  protections, mandatory pre-dispute notice, small claims carve-outs, EU ADR links
- **Privacy Cross-References**: Integration with Privacy Policy, GDPR/CCPA consent
  mechanisms, data processing disclosure in TOS vs. dedicated Privacy Policy
- **Termination and Suspension**: Platform termination rights, user termination rights,
  data retrieval windows, post-termination data handling, survival provisions
- **Modification Procedures**: Change notification timelines, continued use acceptance,
  material change treatment, versioning
- **Governing Law and Jurisdiction**: Choice of law, mandatory consumer protection overrides,
  EU Rome I, UK post-Brexit, forum selection
- **Platform-Specific Compliance**: DSA Arts. 14–27 transparency requirements, DMA Art. 5–6
  gatekeeper obligations, UK Online Safety Act 2023 content moderation duties, CASL

**B2B and B2C variants**: Generates separate clause versions for business-to-business and
business-to-consumer contexts where legal requirements differ materially.

**Does not:**
- Draft Privacy Policies (see `legalcode-privacy-policy-drafter`)
- Review commercial SaaS agreements between businesses (see `legalcode-saas-agreement-drafter`)
- Replace specialized legal counsel for regulated industries (financial services FINRA/FCA,
  healthcare HIPAA/CQC, gambling/gaming, children's platforms requiring FTC consultation)
- Apply to employment agreements or contractor terms (see `legalcode-employment-agreement-review`)
- Constitute legal advice; all output requires qualified legal review before use

**Related skills:**
- `legalcode-privacy-policy-drafter` — generates the complementary Privacy Policy document
- `legalcode-saas-agreement-drafter` — B2B SaaS master service agreements
- `legalcode-dpa-review-and-negotiation` — data processing addendum for GDPR/CCPA contexts
- `legalcode-dsar-workflow-builder` — operational DSAR workflow to underpin TOS privacy commitments
- `legalcode-contract-risk-scorer` — quantified risk scoring of final platform terms

---

## Jurisdiction and Governing Law

This is a multi-jurisdiction skill. TOS agreements face mandatory consumer protection rules
that override contractual choice of law in many jurisdictions. The drafting process identifies
applicable jurisdictions early and applies mandatory requirements before optional customization.

[JURISDICTION-SPECIFIC] **United States** — mandatory requirements:
- **COPPA** (15 U.S.C. §§6501–6506): Operators of websites and online services directed to
  children under 13, or with actual knowledge of child users, must obtain verifiable parental
  consent before collecting personal information. TOS must include clear age gates and
  no-children representations. FTC enforcement is active — review FTC's COPPA Rule (16 C.F.R.
  Part 312), most recently updated effective April 22, 2024.
- **KOSA** (Kids Online Safety Act): [VERIFY current status — Senate passed in July 2024,
  House passage and presidential signature required; check current law before relying on this]
- **FTC Act §5** (15 U.S.C. §45): Deceptive practices in TOS (buried terms, illusory consent,
  misleading renewal disclosures) subject to FTC enforcement; unfairness standard applies to
  practices causing substantial harm consumers cannot reasonably avoid.
- **CAN-SPAM Act** (15 U.S.C. §§7701–7713): Governs commercial email; TOS email opt-out
  mechanisms must comply. Clear opt-out, physical address, no deceptive headers required.
- **DMCA §512** (17 U.S.C. §512): Platform safe harbor for copyright infringement requires
  designated DMCA agent registered with Copyright Office, repeat infringer policy in TOS,
  accommodation of standard technical copyright protection measures.
- **Section 230** (47 U.S.C. §230): Platform immunity for third-party content, but does not
  immunize the platform's own content or federal criminal law violations; FOSTA-SESTA
  exception (Pub. L. 115-164, 2018) applies to sex trafficking content.
- **Auto-renewal**: California B&P Code §§17600–17606 (amended, effective July 1, 2025 for
  online services — affirmative consent for material changes, easy online cancellation,
  acknowledgment email required); New York GBL §527-A (amended effective November 5, 2025);
  FTC Click-to-Cancel Rule final rule published October 2024 — Eighth Circuit vacated July 8,
  2025; state law compliance still mandatory; check additional state laws (Illinois, Oregon,
  Washington, Minnesota, North Carolina, Virginia) [VERIFY currency].
- **Ending Forced Arbitration of Sexual Assault and Sexual Harassment Act of 2022**
  (Pub. L. 117-90): Mandatory arbitration clauses are unenforceable for claims arising from
  sexual assault or sexual harassment, regardless of TOS terms.
- **State UDAP laws**: Unfair and deceptive practices statutes in all 50 states — California
  UCL (Bus. & Prof. Code §17200), CLRA (Civil Code §1750 et seq.) are among the most
  aggressive. Unlawful terms subject to private right of action.

[JURISDICTION-SPECIFIC] **European Union** — mandatory requirements:
- **Consumer Rights Directive** (Directive 2011/83/EU): Art. 6 mandatory pre-contract
  information; Art. 16 exceptions to 14-day withdrawal right; Art. 22 express consent for
  automatic renewal; Directive 2019/2161 (Omnibus) amendments for digital services in force
  May 2022 — digital content provisions fully apply.
- **Unfair Contract Terms Directive** (Directive 93/13/EEC): Non-individually negotiated
  B2C terms are unfair if they create significant imbalance contrary to good faith; Annex
  contains indicative list of unfair terms (unilateral modification, jurisdiction, limitation
  of liability). Not amenable to choice of law override in consumer contracts.
- **Digital Services Act** (Regulation 2022/2065, applicable February 17, 2024): All
  intermediary services with EU users — Art. 14 (TOS content requirements: restrictions,
  enforcement, redress, complaints); Art. 15 (reporting obligations); Art. 24 (transparency
  reporting for very large online platforms/search engines — 45M+ EU monthly active users);
  Art. 27 (recommender system disclosure in TOS); Arts. 17–20 (notice-and-action mechanism,
  trusted flaggers, appeals, out-of-court dispute settlement). Non-compliance carries fines
  up to 6% of global annual turnover.
- **Digital Markets Act** (Regulation 2022/1925): Designated gatekeepers face additional TOS
  obligations under Arts. 5–6 including prohibition on self-preferencing, interoperability
  requirements, and data portability. [JURISDICTION-SPECIFIC] — applies only to designated
  gatekeepers (Apple, Alphabet, Meta, Amazon, Microsoft, TikTok/ByteDance as of 2024).
- **EU Copyright Directive** (Directive 2019/790, CDSM): Art. 17 — platforms with annual
  revenues over €10M or more than 5M monthly users must obtain licenses or demonstrate
  best efforts to block infringing uploads; upload filters required at scale; Art. 18–23
  cover fair remuneration for creators.
- **Rome I Regulation** (Regulation 593/2008): Art. 6 — choice of law clause in B2C contracts
  cannot deprive consumer of protection of mandatory rules of the consumer's habitual residence.
  EU consumer protection minimum cannot be contracted away.
- **GDPR** (Regulation 2016/679): TOS must cross-reference Privacy Policy; consent in TOS
  for data processing is generally invalid (Art. 7(4) — consent must be freely given, not
  bundled with service acceptance). Process under separate legal basis.

[JURISDICTION-SPECIFIC] **United Kingdom** — mandatory requirements:
- **Consumer Rights Act 2015**: Part 2 (unfair terms in consumer contracts) replaces UTCCR
  1999 — terms must be fair, transparent, and prominent; grey list of terms presumptively
  unfair; limitation of liability for death/personal injury from negligence unenforceable.
- **Digital Markets, Competition and Consumers Act 2024** (DMCCA 2024): Part 5 (subscription
  contracts) introduces new requirements for subscription reminders, cooling-off periods,
  and easy cancellation — some provisions effective from date TBC [VERIFY effective date].
- **UK Online Safety Act 2023**: Platforms must include minimum Terms of Service provisions
  for safety duties; Ofcom enforcement from January 2024. Duties to protect users from
  illegal content and (for category 1 platforms) legal but harmful content.
- **UK Arbitration Act 2025**: Updated arbitration framework — [VERIFY effective date and
  consumer arbitration implications].
- **UTCCR / CRA 2015 unfair terms**: Jurisdiction clauses that require consumers to litigate
  outside their habitual residence are presumptively unfair.

[JURISDICTION-SPECIFIC] **Australia** — mandatory requirements:
- **Australian Consumer Law** (ACL, Competition and Consumer Act 2010 Sch. 2): Consumer
  guarantees (ss. 60–64) cannot be excluded; remedies for breach of guarantee mandatory;
  limitation clauses that purport to exclude consumer guarantees are void. B2C TOS must
  include ACL guarantee acknowledgment.
- **Unfair contract terms** (ACL ss. 23–28, amended by Treasury Laws Amendment (More
  Competition, Better Prices) Act 2022, effective November 9, 2023): Civil penalties of
  up to AUD 50M per contravention now apply to unfair terms in standard form B2C and
  small business contracts (turnover threshold: AUD 5M or fewer than 100 employees).
  ACCC enforcement activity has escalated significantly.
- **Automatic renewal**: No comprehensive federal statute — but false or misleading
  representations about renewal obligations are prohibited under ACL ss. 18, 29. Some
  states have additional requirements [VERIFY].
- **Privacy Act 1988** (amended by Privacy and Other Legislation Amendment Act 2024):
  TOS must cross-reference APP-compliant Privacy Policy.

[JURISDICTION-SPECIFIC] **Canada** — mandatory requirements:
- **PIPEDA** (Personal Information Protection and Electronic Documents Act): TOS must
  reference compliant Privacy Policy; Bill C-27 / Consumer Privacy Protection Act (CPPA)
  [VERIFY current legislative status — not yet in force as of March 2026].
- **Quebec Law 25** (An Act to modernize legislative provisions respecting the protection
  of personal information, S.Q. 2021, c. 25): Privacy Policy transparency requirements;
  confidentiality incident reporting; automated decision-making disclosure; TOS must
  cross-reference. Provisions phased in from September 2022 (phase 1), September 2023
  (phase 2), September 2023 (phase 3).
- **CASL** (Canada's Anti-Spam Legislation, S.C. 2010, c. 23): Express consent required
  for commercial electronic messages; TOS acceptance is not sufficient CASL consent unless
  it meets CASL's specificity requirements. Separate CASL opt-in required.
- **Consumer protection**: Province-level — Quebec Consumer Protection Act, Ontario CPA
  2002 ss. 38–41 (internet agreements), BC Business Practices and Consumer Protection Act.
  Internet agreements in Ontario and Quebec have specific disclosure requirements [JURISDICTION-SPECIFIC].

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
platform type, audience, or jurisdiction, the workflow pauses and asks when:

- The answer changes which clause variants to draft (B2B vs. B2C vs. both)
- The platform type determines which mandatory regulatory frameworks apply
- The target jurisdictions determine which mandatory disclosures are required
- Multiple valid drafting approaches exist (arbitration vs. litigation, governing law choices)
- The user's risk tolerance shapes the limitation of liability structure

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

### Step 1: Accept Input

Accept the task in any of these formats:

- **New draft request**: A description of the platform, its users, and target jurisdictions
- **Existing TOS for review/audit**: A file, URL, or pasted TOS text to review for compliance gaps
- **Specific clause request**: A request to draft or improve a specific TOS provision
- **Compliance gap check**: A regulatory framework (DSA, COPPA, ACL, DMCCA) to check against existing TOS
- **B2C → B2B conversion**: An existing consumer TOS to adapt for business users or vice versa

If no platform description or TOS text is provided, ask the user to supply one before proceeding.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, ask the user the following questions. Present as structured
options. Skip any question already answered by the input:

1. **Platform type and model:**
   - Options: SaaS / web application (browser-based), Mobile app (iOS/Android/both),
     Marketplace / multi-sided platform, Social / UGC platform, E-commerce, Gaming/entertainment,
     API / developer platform, Other (specify)
   - *Why this matters*: Platform type determines which regulatory frameworks apply
     (DMCA safe harbor, DSA upload obligations, COPPA UGC rules, KOSA duties,
     marketplace seller liability, etc.).

2. **User audience:**
   - Options: B2C consumers only, B2B businesses only, Both B2C and B2B (generate separate
     variants), B2B2C (platform for businesses that serve consumers), Government/public sector
   - *Why this matters*: Consumer protection rules (unfair terms, auto-renewal, arbitration
     enforceability, liability caps, withdrawal rights) apply to B2C contexts only. B2B
     terms have significantly more drafting flexibility.

3. **Geographic scope:**
   - Options (multi-select): US only, EU (and/or EEA), UK, Australia, Canada, All of the above
     (US/EU/UK/AU/CA), Global (jurisdiction-agnostic with all markers), Other (specify)
   - *Why this matters*: Each jurisdiction has mandatory disclosure requirements and terms
     that cannot be overridden by choice of law. The DSA applies to any platform with EU users
     regardless of incorporation. The ACL applies regardless of where the company is based if
     it supplies to Australian consumers.

4. **Services requiring special treatment:**
   - Options (multi-select): User-generated content (UGC), AI-generated content / AI features,
     Subscription / recurring billing, Free trial with auto-conversion, Marketplace (third-party
     sellers), Minor users or children's platform, Financial services integration,
     Healthcare data handling, Gambling or regulated content, None of the above
   - *Why this matters*: UGC triggers DMCA/DSA analysis; AI features require output ownership
     and training data provisions; subscriptions require auto-renewal law compliance; minors
     trigger COPPA and KOSA; financial services and healthcare face sector-specific overlays.

5. **Task objective (if not clear from input):**
   - Options: Draft new TOS from scratch, Audit existing TOS for compliance gaps,
     Update specific TOS provisions, Add jurisdiction-specific supplement, Create B2B variant
     from existing B2C TOS, Other
   - *Why this matters*: Determines whether the skill generates clause text, analyzes existing
     text, or both.

For batch or non-interactive runs, default to:
- Platform type: SaaS/web application
- User audience: Both B2C and B2C variants required
- Geographic scope: US/EU/UK/AU/CA (full multi-jurisdiction coverage)
- Services: UGC, subscription/billing, AI features included
- Task: Draft new TOS from scratch with compliance annotations

### Step 3: Regulatory Framework Assessment

Before drafting, identify all mandatory requirements that apply to the platform:

#### 3a. Mandatory Applicability Screening

Run this screening checklist silently and report results to the user before drafting:

```
Framework                           | Applies? | Trigger                          | Key Obligations
------------------------------------|----------|----------------------------------|-----------------
COPPA (US)                          |          | Children's platform or actual    | Parental consent, age gate, COPPA
                                    |          | knowledge of child users          | Rule compliance (16 C.F.R. Part 312)
KOSA (US)                           |          | [VERIFY status] Platform used    | [VERIFY obligations]
                                    |          | by minors                        |
DMCA §512 Safe Harbor (US)          |          | UGC or third-party content       | Designated agent, repeat infringer
                                    |          | hosting                          | policy, accommodation of TPMs
Section 230 (US)                    |          | All platforms with user content  | Does not require affirmative steps
                                    |          |                                  | but FOSTA-SESTA exception applies
DSA (EU)                            |          | Intermediary service with EU     | Arts. 14–20, 27 TOS requirements
                                    |          | users                            | (all platforms); VLOP/VLOSE rules
                                    |          |                                  | (45M+ EU MAUs)
DMA (EU)                            |          | Designated gatekeeper only       | Arts. 5–6 gatekeeper obligations
EU Copyright Directive Art. 17      |          | >€10M revenue or >5M monthly    | License or best-efforts blocking
                                    |          | users with EU users              |
Consumer Rights Directive (EU)      |          | B2C digital services to EU       | Arts. 6, 16, 22 mandatory disclosures
                                    |          | consumers                        |
Unfair Contract Terms Dir. (EU)     |          | B2C standard form contracts      | Fairness requirement, Annex terms
UK Consumer Rights Act 2015         |          | B2C with UK consumers            | Unfair terms Part 2 requirements
UK Online Safety Act 2023           |          | Platform with UK users           | Safety duties, content moderation TOS
UK DMCCA 2024 (subscriptions)       |          | Subscription services with UK    | Reminders, cooling-off, cancellation
                                    |          | consumers                        |
ACL (AU)                            |          | Services to Australian           | Consumer guarantees, unfair terms
                                    |          | consumers                        | civil penalties (AUD 50M)
CASL (CA)                           |          | Commercial email to Canadian     | Express consent, opt-out mechanism
                                    |          | recipients                       |
Quebec Law 25 (CA)                  |          | Personal data of Quebec          | Privacy Policy cross-reference,
                                    |          | residents                        | automated decision disclosure
FTC Act §5 (US)                     |          | All US platforms                 | No deceptive or unfair practices
FTC Auto-Renewal / State Laws (US)  |          | Subscription services with US    | Conspicuous disclosure, easy cancel
                                    |          | consumers                        | (CA, NY, IL, OR, WA, MN, NC, VA)
```

#### 3b. Platform Classification Under DSA

For EU-facing platforms, determine DSA category:
- **Mere conduit / caching**: Minimal obligations
- **Hosting service**: Arts. 14–17 notice-and-action, repeat infringer, trusted flaggers
- **Online platform** (hosting + dissemination): Full DSA obligations including TOS Arts. 14, 27;
  out-of-court dispute settlement; DSC complaints mechanism
- **Very Large Online Platform (VLOP)**: 45M+ EU monthly active users — enhanced obligations
  including annual risk assessment, independent audits, algorithmic transparency, DSC coordinator access
- **Very Large Online Search Engine (VLOSE)**: Search-specific equivalent

[JURISDICTION-SPECIFIC] DSA Art. 24 annual transparency reports mandatory for VLOPs and VLOSEs.
Designation is by European Commission; check current designated list before advising on VLOP status.

### Step 4: Draft Core TOS Sections

Draft each section in order, flagging mandatory requirements, recommended language, and
alternatives. Use the classification system (REQUIRED / RECOMMENDED / OPTIONAL) for each
clause element.

#### Section 1: Acceptance and Agreement Formation

**REQUIRED elements:**
- [ ] Clear statement that use of the service constitutes acceptance of TOS
- [ ] Effective date / version identification (for modification tracking)
- [ ] Age minimum statement (minimum 13 for COPPA; 16 for GDPR-compliant EU services; 18 for
  some regulated content — adapt to platform)
- [ ] B2C: affirmative click-through for new users (not just "continued use" acceptance
  — EU Consumer Rights Directive requires affirmative assent for paid services)
- [ ] B2B: company acceptance mechanism, authority representation by individual accepting

**RECOMMENDED elements:**
- [ ] Summary / "plain language" introduction or "quick summary" box (EU best practice,
  DSA Art. 14(1) requires "clear and unambiguous language, plain and intelligible")
- [ ] TOS versioning URL / changelog link
- [ ] Cross-reference to Privacy Policy and any DPA, Cookie Policy, AUP (if separate)

**⟁ CLARIFY** — Age gate approach:
- Simple age declaration ("I am 13 or older") — lightweight but limited verification
- Date-of-birth collection with neutral design (no "age-steering" to bypass gate)
- COPPA-compliant parental consent flow for under-13 users
- Platform-wide 18+ restriction (simplest but forecloses younger users)
*Why this matters*: COPPA requires operators to either (a) screen out under-13 users or
(b) implement verifiable parental consent. Age declaration alone has been challenged by
FTC in enforcement actions. California AADC [VERIFY current law] requires age-appropriate
design by default, not just gating.

**Anti-pattern flag**: Do NOT use pre-ticked checkboxes for TOS acceptance — GDPR Recital 32
and CRA 2015 require affirmative, unambiguous assent. Pre-ticked boxes are specifically
cited as invalid consent mechanisms.

---

#### Section 2: Account Registration and Security

**REQUIRED elements:**
- [ ] User representations on accuracy of registration information
- [ ] Account security obligations (password protection, unauthorized access notification)
- [ ] Platform right to require verification or suspend unverified accounts
- [ ] No-transfer-of-account provision (important for B2C; may have exceptions for B2B)
- [ ] Business account: authorized representatives, organizational binding

**RECOMMENDED elements:**
- [ ] Multi-factor authentication offering or requirement (good practice; SEC/NIST guidance)
- [ ] Account recovery process reference
- [ ] Dormant account handling (data retention limits under GDPR Art. 5(1)(e))

**Classification**:
- REQUIRED: All items above for any account-based platform
- RECOMMENDED: MFA, account recovery, dormant account
- OPTIONAL: API key management provisions (for developer platforms)

---

#### Section 3: Acceptable Use Policy (AUP)

**REQUIRED elements** (all platforms):
- [ ] Prohibited content categories (at minimum): illegal content, CSAM, hate speech
  (mandatory under UK OSA 2023 and DSA Arts. 14, 28), harassment, malware/phishing,
  spam, fraud, unauthorized access attempts
- [ ] Prohibited conduct: account sharing in violation of plan limits, circumventing
  technical measures, automated access without authorization (scraping), impersonation,
  reverse engineering
- [ ] Enforcement discretion clause: platform right to remove content, suspend, or terminate
  at sole discretion for AUP violations
- [ ] No liability for third-party content (Section 230 / DSA Art. 6 immunity preservation)

**RECOMMENDED elements**:
- [ ] Tiered enforcement: warning → content removal → temporary suspension → termination
- [ ] Notice of enforcement action (AUP violation notice before suspension where possible,
  except for emergency removal)
- [ ] Appeals mechanism (mandatory under DSA Art. 20 for online platforms; recommended
  generally for good practice)
- [ ] Reporting mechanism for AUP violations by other users (mandatory for DSA hosting
  services under Art. 16 notice-and-action)

**B2C vs. B2B note**: B2C AUPs must be clearly written and not overreaching — consumer
protection regulators (FTC, CMA, ACCC) have challenged AUPs that give platforms unchecked
termination rights without due process in consumer contexts. B2B AUPs may be more exacting
and include SLA-linked consequences.

**⟁ CLARIFY** — AUP enforcement: Does the platform want a detailed tiered enforcement
framework in the TOS itself, or a short TOS provision that cross-references a separate AUP document?
- In-TOS detailed AUP: More comprehensive, harder to update
- TOS + separate AUP document: More flexible, easier to update AUP without full TOS revision
  (preferred for large platforms)
*Why this matters*: Platforms subject to DSA must update content moderation rules with
notice (Art. 14(4)) — a separate AUP document is easier to maintain with proper notification
mechanisms.

---

#### Section 4: User-Generated Content (UGC) and Intellectual Property

##### 4a. User Content License

**REQUIRED elements**:
- [ ] User retains ownership of content they submit (cannot claim ownership transfer
  without explicit, prominently disclosed consent — FTC guidance; EU law)
- [ ] License grant to platform: scope must be defined — minimum: worldwide, royalty-free,
  non-exclusive, sublicensable (for CDN/hosting), license to host, store, reproduce,
  display, and distribute user content in connection with the service
- [ ] Termination of license: what happens to license on account deletion or content removal?
  Standard: license terminates except for copies made in ordinary course of platform operation
  (backups, cached copies)

**⟁ CLARIFY** — AI Training Data Use: Does the platform intend to use user content to train AI models?
- No AI training use — include explicit prohibition or omit
- AI training permitted — requires specific, prominent disclosure; separate opt-in recommended
  for EU (GDPR Art. 6 / Art. 9); user backlash has been significant (Meta, Twitter/X backlash
  in 2023–2025); California AB 2355 [VERIFY] may impose additional consent requirements
- AI training with opt-out — EU GDPR requires basis; UK ICO guidance suggests legitimate
  interests may apply with opt-out; recommended for non-EU markets where opt-in is not mandatory
*Why this matters*: Using user content for AI training without disclosed consent has triggered
regulatory action (CNIL investigation of Meta; UK ICO investigations; Italian DPA block of
Replika). Including without disclosure creates material regulatory and reputational risk.

**RECOMMENDED elements**:
- [ ] Moral rights waiver (B2C EU/UK — waiver is limited in some EU jurisdictions; UK CDPA
  1988 s. 87 permits waiver; France droit moral not fully waivable; include with [JURISDICTION-SPECIFIC] note)
- [ ] User representations on content (does not infringe third-party IP, does not violate
  applicable law) — establishes basis for DMCA safe harbor / DSA notice-and-action
- [ ] DMCA repeat infringer policy: platform will terminate accounts of users who repeatedly
  infringe copyrights — required for DMCA §512 safe harbor
- [ ] Takedown process reference: link to or describe DMCA notification address and process

##### 4b. Platform Intellectual Property

**REQUIRED elements**:
- [ ] Reservation of platform IP: platform and its licensors own all platform IP
- [ ] License to user: limited, revocable, non-exclusive, non-transferable license to use
  the service as provided
- [ ] No IP transfer by virtue of using the service
- [ ] Trademark restrictions: no use of platform marks without written permission
- [ ] API terms: if applicable, any additional license restrictions, rate limits, no
  competitive use of API output

**RECOMMENDED elements** (AI-assisted platforms):
- [ ] Output ownership: who owns AI-generated content produced using the platform?
  - Common approach: user owns outputs generated from their inputs; platform retains
    right to use anonymized/aggregated output data for service improvement
  - Note: EU AI Act does not directly address output ownership but AI-generated output
    may have diminished IP protection (CJEU Cofemel [2019]; UK IPO guidance on AI [VERIFY])
- [ ] AI limitations: outputs are not legal/medical/financial advice; no accuracy warranties
- [ ] Third-party model restrictions: if platform uses third-party AI models, pass-through
  restrictions may apply (OpenAI, Anthropic, Google Gemini usage policies)

---

#### Section 5: Subscription, Billing, and Auto-Renewal

##### 5a. Subscription Terms

**REQUIRED elements**:
- [ ] Pricing: current pricing or reference to pricing page; right to change prices
  (with required advance notice — CA requires 30 days for material price changes;
  EU CRD Art. 22 requires prior notice for changes to ongoing digital services)
- [ ] Billing cycle: monthly, annual, other; prorated refunds or credits on upgrades
- [ ] Payment methods accepted; recurring billing authorization
- [ ] Failed payment: grace period, service suspension, account cancellation on failure
- [ ] Taxes: user responsible for applicable taxes; platform will collect where legally required

**B2C specific**:
- [ ] Free trial auto-conversion disclosure: conspicuous notice before trial ends
  (required by FTC Click-to-Cancel principles, CA B&P §17600, NY GBL §527-A)
- [ ] Refund policy: mandatory cooling-off / withdrawal rights for digital services in EU
  (CRD Art. 14–16: 14-day right of withdrawal for digital services unless service has
  already begun with consumer's prior express consent and acknowledgment of loss of
  withdrawal right); UK CRA 2015 equivalent; Australia: no general cooling-off right for
  services (ACL) but misleading representations are prohibited

**B2B specific**:
- [ ] Invoice terms, net payment periods
- [ ] True-up mechanics for seat-based pricing
- [ ] Suspension on breach vs. suspension on non-payment (distinguish)

##### 5b. Auto-Renewal Compliance

This is an area of active US regulatory enforcement. Draft auto-renewal provisions to
comply with the most stringent applicable state law (California B&P §§17600–17606).

**REQUIRED elements** (for any subscription with auto-renewal):
- [ ] **Conspicuous disclosure** of auto-renewal terms: plain language, before acceptance,
  separate from other terms or visually prominent — California requires "clear and conspicuous"
  presentation, not buried in TOS body
- [ ] **Offer terms disclosure** at time of subscription: price, billing frequency, length
  of subscription term, how to cancel
- [ ] **Acknowledgment**: affirmative assent specifically to auto-renewal terms (separate
  checkbox recommended for California compliance)
- [ ] **Renewal notice**: email notification before renewal for annual subscriptions
  — California requires 3–30 days' advance notice for auto-renewing contracts over 1 year;
  New York GBL §527-A requires 15–30 days' notice [VERIFY current text]; UK DMCCA 2024
  requires reminder notices [VERIFY precise timing]
- [ ] **Easy online cancellation**: "click-to-cancel" mechanism; FTC principles (even if
  final rule vacated) are reflected in many state laws. California requires the cancellation
  mechanism to be at least as easy to use as the enrollment mechanism.
- [ ] **Post-cancellation confirmation**: email confirmation of cancellation (FTC, CA)
- [ ] **Price change notification**: advance notice before applying pricing changes to
  existing subscriptions; allow cancellation as remedy

**⟁ CLARIFY** — Governing auto-renewal law: Which US state is most restrictive for this platform's user base?
- If the platform has significant California users: California B&P §§17600–17606 governs
- If national/global: California as baseline (most stringent); verify NY, IL, OR, WA [JURISDICTION-SPECIFIC]
- EU: Consumer Rights Directive Art. 22 is the baseline; some member states have stricter rules
*Why this matters*: Non-compliance with California auto-renewal law has resulted in multi-million
dollar class action settlements (LinkedIn, Amazon, Instacart, DoorDash) and FTC enforcement actions.

---

#### Section 6: Disclaimer of Warranties

**REQUIRED elements**:
- [ ] "AS IS" and "AS AVAILABLE" warranty disclaimer
- [ ] Disclaimer of implied warranties of merchantability, fitness for a particular purpose,
  non-infringement, accuracy, and reliability
- [ ] No warranty that service will be error-free, uninterrupted, secure, or free of viruses

**Jurisdiction-specific enforceability**:
- [JURISDICTION-SPECIFIC] **US**: UCC §2-316 warranty disclaimer must be conspicuous (all caps
  or other notice-drawing format) if UCC applies; most courts treat SaaS as services (not goods)
  so UCC applies by analogy at most. Disclaimer still requires conspicuousness for enforcement.
- [JURISDICTION-SPECIFIC] **EU/UK B2C**: Cannot disclaim conformity of digital content/service
  with contract (EU: Directive 2019/770; UK: CRA 2015 ss. 34–36 for digital content). Consumer
  has right that service/content is fit for purpose, as described, and satisfactory quality.
  Disclaimer of B2C quality standards is unfair and void.
- [JURISDICTION-SPECIFIC] **Australia**: ACL consumer guarantees (fitness for purpose,
  acceptable quality) cannot be excluded for consumers. For B2C services, disclaimers that
  purport to exclude ACL guarantees are void and may attract civil penalties.
- [JURISDICTION-SPECIFIC] **Canada**: Consumer protection statutes in Ontario (CPA 2002),
  BC, and Quebec impose implied warranties that cannot be disclaimed in consumer contracts.

**RECOMMENDED drafting practice**: Use all-caps for warranty disclaimer in US-governed TOS;
include jurisdiction-specific savings language ("to the extent permitted by applicable law")
to avoid voiding entire clause in consumer jurisdictions.

---

#### Section 7: Limitation of Liability

**REQUIRED elements**:
- [ ] Exclusion of consequential, indirect, incidental, special, and punitive damages
- [ ] Aggregate liability cap: common structures include 12-month fees paid, $100 flat cap
  (B2C), or fee paid in the 30 days preceding the claim
- [ ] Exceptions to cap (standard carve-outs): death/personal injury from negligence
  (mandatory carve-out in UK and EU B2C — unfair/void to exclude), fraud, gross negligence
  or willful misconduct (US negotiated), IP infringement claims, breach of confidentiality

**Jurisdiction-specific enforceability**:
- [JURISDICTION-SPECIFIC] **US B2B**: High enforceability under mutual agreement; unconscionability
  challenge available but rarely succeeds in commercial contexts. Follow UCC §2-719 or
  common law enforceability standards depending on characterization.
- [JURISDICTION-SPECIFIC] **US B2C**: Courts have voided liability caps in consumer TOS
  under CLRA, UCL, and unconscionability doctrine — particularly where platform's own
  negligence is involved. Cap at one-year fees is generally the floor for B2C; flat caps
  below $100 have been voided.
- [JURISDICTION-SPECIFIC] **UK**: UCTA 1977 s. 2 — liability for death/personal injury from
  negligence cannot be excluded; s. 3 — exclusion of other liabilities in standard-form
  B2B contracts subject to reasonableness test; CRA 2015 s. 65 — same prohibition for B2C;
  s. 62 — unfair terms (including liability caps) are not binding on consumers.
- [JURISDICTION-SPECIFIC] **EU**: Unfair Contract Terms Directive — limitation of liability
  to amount paid has been challenged in consumer contexts; "significant imbalance" test.
  GDPR Art. 82 — platform liability for data protection violations cannot be contractually
  limited against data subjects.
- [JURISDICTION-SPECIFIC] **Australia**: ACL s. 64 — any term that purports to exclude ACL
  consumer guarantee liability is void; s. 64A — liability can be limited to replacement,
  repair, or re-supply for goods; for services — refund of price or re-supply.

**⟁ CLARIFY** — Liability cap structure:
- Mutual cap (both parties): Standard for B2B; platform may accept mutual cap with carve-outs
- Unilateral platform-only cap: Standard for B2C; user's liability often uncapped for
  IP infringement, AUP violations, payment obligations
- Tiered caps by claim type: Higher cap for data breaches (market trend); lower cap for SLA
  claims; separate super-cap for fraud/gross negligence
*Why this matters*: Cap structure determines the platform's risk exposure. B2C caps below one
year of fees paid have been successfully challenged.

---

#### Section 8: Dispute Resolution

##### 8a. Arbitration Agreement (US-Focused)

**REQUIRED elements** (if using arbitration):
- [ ] **Conspicuous disclosure** that arbitration waives jury trial right and class action rights
  — US courts require this to be prominent; "ALL CAPS" notice is standard
- [ ] **Opt-out mechanism**: 30-day opt-out window recommended for enforceability
  (JAMS Consumer Arbitration Rules require opt-out; AAA Consumer Due Process Protocol)
- [ ] **Arbitration administrator**: specify AAA or JAMS; include link to rules
- [ ] **Cost allocation**: consumer may not pay fees exceeding what a court would charge
  — FTC and state AGs challenge arbitration agreements that shift costs to consumers
- [ ] **Individual claims only**: class and representative action waiver
- [ ] **Small claims court carve-out**: small claims court available for qualifying claims
  — required for AAA/JAMS consumer arbitration acceptance; some state statutes require it
- [ ] **EFASSHA carve-out**: sexual assault and sexual harassment claims not subject to
  arbitration (Pub. L. 117-90, mandatory, cannot be contracted away)
- [ ] **Governing law for arbitration**: FAA governs; specify if California arbitration law applies

**Mass arbitration considerations**:
- [ ] Mass arbitration protocol: batching provisions, bellwether procedures, trial group
  selection — companies including DoorDash, Amazon, and StubHub have adopted these after
  mass arbitration abuse tactics by plaintiffs' bar
- [ ] Filing fee limits: consider fee-splitting for mass arbitration (above individual
  threshold) — balance enforceability against mass arbitration gaming

**Jurisdictional inapplicability** [JURISDICTION-SPECIFIC]:
- **EU**: Mandatory arbitration clauses in B2C contracts are unfair under Directive 93/13/EEC
  Annex (1)(q); EU consumers retain right to sue in their local courts (Rome I Art. 6).
  Arbitration must be genuinely optional and mutually agreed upon.
- **UK**: Consumer arbitration agreements for claims under £5,000 are unenforceable if
  consumer opposes (Arbitration Act 1996 s. 91; CRA 2015 Part 2). New UK Arbitration
  Act 2025 [VERIFY consumer provisions].
- **Australia**: Class action waivers in standard form B2C contracts are presumptively unfair
  under ACL unfair terms regime.
- **Canada**: Consumer arbitration agreements face scrutiny in Quebec (art. 11.1 CPA),
  and Ontario (CPA 2002 s. 7(2) — arbitration clauses in consumer contracts unenforceable
  as to consumer rights claims unless mutual and fair).

##### 8b. Governing Law and Jurisdiction

**REQUIRED elements**:
- [ ] Choice of governing law: common choices are Delaware (business-friendly, predictable),
  California (but more plaintiff-friendly), Ireland/England and Wales (for EU/UK platforms)
- [ ] Forum selection / jurisdiction clause: exclusive jurisdiction in specified courts
- [ ] Mandatory consumer protection override savings clause: "[Notwithstanding the choice of
  governing law, you may benefit from the mandatory consumer protection provisions of your
  country or state of habitual residence to the extent that such provisions cannot be
  excluded by agreement]" — essential for EU, UK, AU, CA consumer compliance

[JURISDICTION-SPECIFIC] EU Rome I Art. 6: Choice of law cannot deprive consumer of
mandatory protection of the law of their habitual residence. Platform must comply with EU
consumer protection minimum regardless of governing law clause.

[JURISDICTION-SPECIFIC] Australian courts: ACCC and state fair-trading regulators can
apply ACL regardless of governing law clause if service is supplied to Australian consumers.

**⟁ CLARIFY** — Governing law choice:
- Delaware: Best for B2B, investor-facing, or US-incorporated entities
- California: Transparent for California consumer base; subjects platform to CLRA, UCL
- England and Wales: Good for global B2B; familiar to many international parties
- Ireland: Preferred for EU-incorporated entities; GDPR supervisory authority (DPC)
*Why this matters*: Choice of law affects unconscionability doctrine, warranty disclaimers,
arbitration enforceability, and litigation cost exposure. California choice of law combined
with B2C exposure is highest-risk combination for class action exposure.

---

#### Section 9: Privacy Cross-Reference and Data Protection

**REQUIRED elements**:
- [ ] Cross-reference to Privacy Policy: TOS must reference and incorporate the Privacy Policy
- [ ] No consent in TOS for data processing: GDPR Recital 43 and Art. 7(4) — consent for
  data processing must be separate from service acceptance and freely given; bundle consent
  is not freely given; do NOT place data processing consent in TOS acceptance
- [ ] Cookie Policy cross-reference (if cookies used)
- [ ] Data breach notification process reference (consumer-facing: link to process or
  outline key timelines — GDPR 72 hours to supervisory authority; GDPR Art. 34 — without
  undue delay to data subjects for high-risk breaches)

**RECOMMENDED elements**:
- [ ] GDPR data subject rights summary (brief, with link to full Privacy Policy)
- [ ] CCPA opt-out of sale/sharing cross-reference and link to "Do Not Sell or Share"
  mechanism (if applicable)
- [ ] Quebec Law 25: reference to automated decision-making disclosure if platform uses
  automated decision-making affecting users

---

#### Section 10: Termination and Suspension

**REQUIRED elements**:
- [ ] Platform rights to suspend or terminate: for-cause (AUP violation, fraud, failure to pay),
  with-notice (platform discontinuing service), immediate (for serious violations)
- [ ] User right to terminate: how users cancel / close accounts
- [ ] Effect of termination: access cessation, data retrieval window, data deletion timeline
- [ ] Survival: which provisions survive termination (indemnification, IP, limitation of
  liability, dispute resolution, governing law — standard)

**B2C considerations**:
- [ ] Reasonable prior notice before suspension for non-emergency AUP violations
  — DSA Art. 17 requires statement of reasons for content moderation decisions and
  suspension of access; CMA (UK) and ACCC (AU) have challenged TOS that give platforms
  absolute termination discretion without process in consumer contexts
- [ ] Data portability window: GDPR Art. 20 data portability right on termination;
  EU Data Act switching rights (applicable from September 12, 2025); recommend minimum
  30-day data export window post-termination
- [ ] No punitive data deletion on termination: platforms should not delete data immediately
  on termination without reasonable notice and export opportunity; GDPR data portability
  right applies at termination

**B2B considerations**:
- [ ] Termination for convenience with notice period (30–90 days typical)
- [ ] Termination for cause with cure period (typically 30 days for remediable breaches)
- [ ] Effect on committed subscriptions and refund obligations
- [ ] Data handling post-termination (GDPR Art. 28(3)(g) — processor must delete or return
  data on termination per instructions)

---

#### Section 11: Modification of Terms

**REQUIRED elements**:
- [ ] Platform right to modify TOS: right reserved with notice obligation
- [ ] Notice mechanism: email or prominent in-product notice; advance notice period
  — recommend minimum 30 days for material changes (EU best practice; DMCCA 2024 subscription changes)
- [ ] Acceptance mechanism for changes: continued use = acceptance (acceptable for B2B;
  for B2C, material changes may require affirmative re-acceptance — EU best practice)
- [ ] Non-acceptance right: user right to terminate if they do not accept material changes
  — required for EU/UK B2C (unfair to impose material changes without exit right);
  DSA Art. 14(4) requires notification period before new restrictions take effect

**B2C compliance note**: Under EU Unfair Contract Terms Directive and CRA 2015, unilateral
modification clauses without adequate notice and exit rights are presumptively unfair.
Minimum: 30 days' notice + right to terminate without penalty if user objects to changes.

**Version control best practice**: Maintain TOS version history with effective dates;
link to prior versions at bottom of TOS. Required for DSA Art. 14 compliance.

---

#### Section 12: DSA-Specific TOS Requirements

**Applicable to**: Any online platform or hosting service with EU users.

**Art. 14 — Terms and Conditions Content Requirements**:
The TOS must include:
- [ ] Information on restrictions on use of the service (content moderation, prohibited
  content categories, enforcement measures)
- [ ] Enforcement measures that may be applied: content removal, account suspension,
  account termination
- [ ] Internal complaint-handling procedure reference (Art. 20)
- [ ] Reference to out-of-court dispute settlement body (Art. 21 — listed DSC-certified body)
- [ ] Applicable law (Art. 14(1)(d))
- [ ] Reference to trusted flaggers (Art. 22 — for platforms)
- [ ] Information on the Digital Services Coordinator (DSC) of establishment for complaints
- [ ] For algorithmic recommender systems: Art. 27 requires TOS to identify recommender
  systems, explain main parameters, and describe options to modify or opt out

**Art. 15 — Reporting Obligations**:
- [ ] Obligation to report CSAM (child sexual abuse material) to relevant national authorities
  immediately — mandate applies regardless of Art. 14

**VLOP-specific** (45M+ EU monthly active users):
- [ ] Annual transparency report on content moderation
- [ ] Systemic risk assessment
- [ ] Independent audit access
- [ ] Real-time database access for vetted researchers

---

### Step 5: Drafting Quality Framework

Apply these frameworks to each drafted clause before finalizing:

#### Citation Quality Gates

Run these 5 gates silently for every legal claim made in the draft TOS guidance:

| Gate | Rule | Fail Action |
|------|------|-------------|
| **Source** | Every mandatory requirement cites specific statute, regulation, or enforcement guidance | Add citation or mark "[UNVERIFIED]" |
| **Format** | Citations follow consistent format for each jurisdiction | Fix format |
| **Currency** | Every cited provision verified for amendments — consumer law changes frequently | Flag "[CHECK CURRENCY]" |
| **Domain** | Analysis stays within applicable jurisdiction's legal framework | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty in legal interpretation explicitly stated | Add confidence qualifier |

**High-volatility areas requiring extra verification** (consumer law changes rapidly):
- US auto-renewal laws: California, New York, FTC Rule status — verify quarterly
- UK DMCCA 2024 subscription provisions — effective dates may not all be in force
- KOSA / state minors' law — legislative status changes frequently
- DSA VLOP designation list — updated by European Commission
- COPPA Rule amendments — FTC updates on irregular schedule

#### Self-Interrogation for High-Risk Provisions

For any clause classified as HIGH RISK (mandatory requirement, non-waivable, or subject to
active regulatory enforcement), apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**: Does the mandatory requirement follow from the cited
statute? Would a regulator (FTC, DPC, CMA, ACCC) reach this conclusion?

**Pass 2 — Completeness**: Have all relevant jurisdictions' mandatory requirements been
considered? Are there related regulatory dimensions (e.g., GDPR overlap with auto-renewal
consent) not yet addressed?

**Pass 3 — Challenge**: What is the strongest argument that this requirement does NOT apply?
Under what circumstances would this provision be at reduced risk?

#### Confidence Scoring

| Level | Range | Meaning | Application |
|-------|-------|---------|-------------|
| **Definite** | 0.95–1.0 | Clear statutory mandate, recent enforcement | State as required with statutory citation |
| **High** | 0.80–0.94 | Strong authority, minor interpretation questions | State as required with brief qualification |
| **Probable** | 0.60–0.79 | Strong arguments, some uncertainty | State as strongly recommended; note uncertainty |
| **Possible** | 0.40–0.59 | Genuine regulatory uncertainty | Flag for legal review; present both views |
| **Unlikely** | 0.0–0.39 | Speculative or minority view | Do not assert; flag "[UNCERTAIN]" |

---

### Step 6: B2C vs. B2B Clause Comparison

For platforms that serve both audiences, generate a comparison table for each high-impact clause:

| Clause | B2C Version | B2B Version | Mandatory Difference |
|--------|-------------|-------------|----------------------|
| Warranty disclaimer | Limited by ACL, CRA 2015, EU Dirs. | Full AS IS disclaimer | YES — consumer laws void B2C disclaimers |
| Limitation of liability | Must carve out death/injury, GDPR, ACL | More flexibility; mutual negotiation | YES — UCTA s.2, ACL s.64 |
| Arbitration | Opt-out required; EU unenforceable | Generally enforceable with proper drafting | YES — consumer protection laws |
| TOS modification | 30-day notice + exit right | Shorter notice acceptable | YES — unfair terms rules |
| Auto-renewal | Conspicuous disclosure, easy cancel | Standard business practice | YES — state auto-renewal laws |
| Jurisdiction clause | Consumer habitual residence override | Freely negotiated | YES — Rome I Art. 6, CRA 2015 |
| Termination notice | Reasonable notice + data export | For convenience with notice | RECOMMENDED — CMA/ACCC scrutiny |

---

### Step 7: Quality Verification

Before delivering the draft TOS guidance, verify against the Legalcode quality bar:

#### Completeness Check

```
Element                          | Present | Quality (1-5) | Notes
---------------------------------|---------|---------------|------
1. Rich frontmatter              |         |               |
2. Disclaimer                    |         |               |
3. Purpose and Scope             |         |               |
4. Jurisdiction handling         |         |               |
5. Interactive Clarification     |         |               |
6. Multi-step workflow           |         |               |
7. Deep topic analysis           |         |               |
8. Severity classification       |         |               |
9. Actionable output per finding |         |               |
10. Prioritization framework     |         |               |
11. Citation Quality Gates       |         |               |
12. Self-Interrogation           |         |               |
13. Confidence Scoring           |         |               |
14. Glass Box audit trail        |         |               |
15. Anti-patterns (10+)          |         |               |
16. Writing standards            |         |               |
17. External tool integration    |         |               |
18. Output format template       |         |               |
```

#### Regulatory Coverage Check

For each applicable jurisdiction, confirm:
- [ ] Mandatory disclosure requirements addressed
- [ ] Forbidden clause types excluded (unfair terms, banned arbitration provisions)
- [ ] Consumer guarantee carve-outs included where required
- [ ] Auto-renewal compliance verified against most stringent applicable state/national law
- [ ] Privacy cross-reference complete; no bundled GDPR consent
- [ ] DMCA repeat infringer policy included (if UGC platform)
- [ ] DSA Art. 14 TOS content requirements met (if EU platform)

---

## Severity Classification System

Classify each TOS provision and any compliance gap on this scale:

| Classification | Meaning | Action Required |
|----------------|---------|-----------------|
| **REQUIRED** | Mandatory by statute or regulation; absence creates regulatory or legal liability | Must include — no discretion |
| **REQUIRED (B2C)** | Mandatory for consumer-facing services; optional for B2B | Include for B2C variant; flag for B2B |
| **RECOMMENDED** | Industry standard; absence creates risk of regulatory scrutiny or enforcement | Include with high urgency |
| **OPTIONAL** | Depends on business model or risk tolerance; no mandatory basis | Include if relevant; flagged as discretionary |
| **FORBIDDEN (B2C)** | Clause type is unenforceable or illegal in consumer contracts | Remove; do not include |
| **FORBIDDEN (Jurisdiction)** | Clause type is unenforceable in specific jurisdiction | Remove or add [JURISDICTION-SPECIFIC] carve-out |

**Gap Classification** (for TOS audit mode):
| Gap Severity | Meaning | Urgency |
|--------------|---------|---------|
| **CRITICAL** | Missing mandatory provision; active regulatory enforcement risk | Address before publication |
| **HIGH** | Missing important provision; regulatory scrutiny risk or significant legal exposure | Address within 30 days |
| **MEDIUM** | Missing recommended provision; below-market standard; moderate risk | Address within 90 days |
| **LOW** | Minor gap; best practice only; minimal risk | Address in next review cycle |

---

## Prioritization Framework

When building or auditing TOS, prioritize in this order:

### Tier 1 — Regulatory Must-Haves (address immediately)
1. COPPA / age gate provisions (active FTC enforcement; per-violation penalties up to $51,744)
2. DMCA safe harbor requirements (repeat infringer policy, designated agent)
3. DSA Art. 14 TOS content requirements (6% global revenue fines)
4. ACL unfair terms / consumer guarantee carve-outs (AUD 50M civil penalties)
5. GDPR: no bundled consent in TOS; Privacy Policy cross-reference
6. Auto-renewal: California B&P §§17600–17606 (class action and AG exposure)
7. Ending Forced Arbitration Act — EFASSHA carve-out from mandatory arbitration
8. UK OSA / DSA — content moderation duties in TOS (Ofcom enforcement)

### Tier 2 — Legal Risk Mitigators (address before launch or major update)
9. Warranty disclaimer conspicuousness (US); savings clause for consumer jurisdictions
10. Limitation of liability cap validity and carve-outs
11. Arbitration agreement enforceability — opt-out, EFASSHA, AAA/JAMS compliance
12. TOS modification procedure with adequate notice and exit rights
13. Data portability and post-termination data handling (GDPR Art. 20)
14. UGC license scope and AI training data disclosure

### Tier 3 — Best Practice Enhancements (next review cycle)
15. Multi-tier enforcement framework for AUP (warning → removal → suspension → termination)
16. Appeals mechanism for content moderation decisions (DSA Art. 20 for EU platforms)
17. Recommender system transparency (DSA Art. 27)
18. TOS version history and changelog
19. Plain-language summary / quick guide
20. Localization supplements for each jurisdiction

---

## Anti-Patterns for Terms of Service Drafting

What NOT to do when drafting or reviewing TOS:

1. **Burying auto-renewal disclosure**: Auto-renewal terms buried in body text or in
   a footnote are non-compliant with California B&P §17600 ("clear and conspicuous"
   presentation required); class action settlements averaging $10M+ have resulted from this.

2. **Bundling GDPR consent into TOS acceptance**: GDPR Art. 7(4) and Recital 43
   prohibit making service access conditional on consent to data processing that is not
   necessary for the service. A single "agree to TOS" checkbox is insufficient basis for
   GDPR processing consent. Process data on a different lawful basis (Art. 6(1)(b), (c),
   or (f)) or obtain separate, specific consent.

3. **Mandatory arbitration for EU consumers**: Arbitration clauses that purport to
   prevent EU consumers from suing in their local courts are unfair under Directive
   93/13/EEC and unenforceable. Rome I Art. 6 allows EU consumers to invoke mandatory
   consumer protection law regardless of choice of law.

4. **Over-broad UGC license**: Claiming ownership-level rights to user content (perpetual,
   irrevocable, transferable in all media) triggers FTC and user backlash. Meta's 2023
   backlash and 2024 X/Twitter (formerly Twitter) class action settlement over AI training
   data use illustrate the reputational and legal risk of overbroad license language.

5. **Excluding ACL consumer guarantees (Australia)**: Any term purporting to exclude
   ACL consumer guarantees is void (ACL s. 64) and since November 2023 can attract civil
   penalties of up to AUD 50M per contravention. ACCC has escalated enforcement following
   the penalty amendment.

6. **Unilateral modification without exit right (EU/UK B2C)**: TOS clauses allowing
   the platform to unilaterally modify any term without notice and without allowing users
   to terminate if they object are presumptively unfair under Directive 93/13/EEC Annex (1)(j)
   and CRA 2015 s. 62. Minimum: 30 days' notice + termination right.

7. **No EFASSHA carve-out in arbitration clause**: Post-Pub. L. 117-90 (2022), mandatory
   arbitration of sexual assault or sexual harassment claims is unenforceable regardless of
   TOS language. Including a mandatory arbitration clause without the EFASSHA carve-out
   creates a per se unenforceable provision and signals outdated legal review.

8. **Section 230 reliance without repeat infringer policy**: DMCA §512 safe harbor
   (which complements but differs from §230) requires a clearly stated repeat infringer
   termination policy. Platforms that terminate inconsistently or without a policy risk
   losing safe harbor protection.

9. **Vague "we may share your data" without Privacy Policy cross-reference**: TOS
   data-sharing provisions without a referenced Privacy Policy create GDPR compliance gaps
   (Arts. 13–14 transparency), FTC deceptive practices exposure, and COPPA notice deficiencies.
   All data practices must be in a GDPR-compliant Privacy Policy; TOS should cross-reference.

10. **All-cap limitation of liability applied to consumer claims (AU/UK/EU)**: All-caps
    styling does not create enforceability in jurisdictions where the underlying clause is
    void as against consumer protection law. UCTA 1977, CRA 2015, and ACL void limitation
    clauses regardless of presentation format.

11. **DSA non-compliance assuming "we're not big enough"**: DSA applies to ALL hosting
    services and online platforms with EU users — not just large companies. VLOP/VLOSE
    enhanced obligations apply at 45M EU MAUs, but Art. 14 TOS requirements, notice-and-action
    (Art. 16), out-of-court dispute settlement (Art. 21), and CSAM reporting apply from day one.

12. **Governing law + jurisdiction clause without consumer savings clause**: Without a
    savings clause preserving mandatory consumer protection rights, the governing law clause
    is unenforceable against EU consumers (Rome I Art. 6), UK consumers (CRA 2015), and
    Australian consumers (ACL). Including the savings clause costs nothing; omitting it
    voids the governing law clause partially.

13. **Silently using user content for AI training**: Using user content for AI model
    training without disclosed, specific consent has triggered CNIL investigations (Meta),
    Italian DPA blocks (Replika), UK ICO concerns, and US class actions (OpenAI, Stability
    AI). If AI training is intended, disclose it specifically and provide appropriate opt-out
    or opt-in mechanism depending on jurisdiction.

14. **No appeals mechanism for account suspension (DSA/UK OSA)**: DSA Art. 20 requires
    online platforms to implement an internal complaint-handling mechanism for content
    moderation decisions (removal, restriction, suspension). UK OSA 2023 requires user
    redress mechanisms. Platforms without these face regulatory fines and loss of safe harbor.

15. **Recursive or circular TOS documents**: TOS that incorporate by reference dozens of
    separate documents (AUP, Community Guidelines, Privacy Policy, Cookie Policy, API Terms,
    Developer Agreement, Brand Guidelines) without hyperlinks or version control create
    enforceability problems — courts have voided TOS for insufficient notice of incorporated terms.
    Keep incorporation by reference to essential documents; hyperlink with version stamps.

16. **No consideration of CASL for email-based features**: If the platform sends
    commercial electronic messages to Canadian users, CASL (S.C. 2010, c. 23) requires
    express consent separate from TOS acceptance. CASL consent obtained via TOS checkbox
    is considered implied at best, insufficient for commercial messages. Separate CASL
    opt-in is required.

17. **Liquidated damages disguised as platform fees**: Auto-renewal fees, account
    reinstatement fees, or early termination fees that are disproportionate to actual harm
    may be unenforceable as penalties in UK/EU (penalty rule), as unfair terms (CRA 2015,
    93/13/EEC), or as deceptive practices (FTC §5). Include proportionality language and
    connect fees to actual business costs.

18. **Minors' assent without parental consent verification**: COPPA requires verifiable
    parental consent — age declarations ("I am 13 or older") are not verifiable parental
    consent mechanisms. For platforms where under-13 use is foreseeable, a COPPA-compliant
    parental consent flow is required; age declarations alone have been challenged in FTC
    enforcement. California AADC (if enacted and effective [VERIFY]) imposes age-appropriate
    design by default.

19. **Blanket indemnification of platform by users (B2C)**: Requiring consumers to
    indemnify the platform for any claim arising from their use of the service — without
    carve-outs — is overbroad and may be an unfair term under 93/13/EEC Annex (1)(b) and
    CRA 2015. B2C indemnification should be limited to user-caused violations (AUP breach,
    IP infringement) not general platform risk.

20. **No version history or effective date**: TOS without a clearly stated effective date
    and version identifier make it impossible to determine which version governs a dispute.
    This affects enforceability and creates regulatory compliance tracking problems.
    DSA Art. 14 requires TOS to be machine-readable and dated.

---

## Writing Standards

Before delivering any TOS clause or guidance, apply these writing discipline checks:

**Plain Language Gates** (especially important for B2C TOS — DSA Art. 14(1) requires
"clear and unambiguous language, plain and intelligible"):

1. **Readability**: Can a user with a high-school education understand this clause? If not, rewrite.
2. **Active voice**: Use active voice for clarity. "We may terminate your account" not
   "Your account may be subject to termination by us."
3. **No legalese shortcuts**: "Notwithstanding the foregoing" → "Despite what we said above";
   "indemnify, defend, and hold harmless" → define each term if using (or simplify in B2C context).
4. **Defined terms**: Any term that appears more than twice should be defined on first use and capitalized.
5. **Sentence length**: Aim for maximum 30-word sentences in consumer-facing provisions.
6. **No double negatives**: "Users shall not fail to comply" → "Users must comply."
7. **Scannable structure**: Use headers, numbered lists, and tables for long provisions.
   DSA Art. 14 and CMA guidance recommend easy navigability.
8. **Cross-references**: All internal cross-references should use section numbers and descriptive
   labels (e.g., "see Section 8 (Dispute Resolution)" not just "see above").

**Legal Precision Gates** (applies to all TOS, including B2B):
1. All monetary amounts in specific currency with ISO 4217 code if multi-jurisdiction.
2. All notice periods as exact calendar day counts.
3. All survival provisions explicitly enumerated.
4. Effective date of TOS and any amendments stated explicitly.

---

## External Tool Integration

### legalcode-mcp

When legalcode-mcp is connected, use it for:
- Searching for current statutory text for each jurisdiction's auto-renewal, consumer
  protection, and arbitration statutes (verify effective dates and recent amendments)
- Finding enforcement actions by FTC, CMA, ACCC, DPC, CNIL relevant to platform TOS
- Searching DSA/DMA implementing regulations and delegated acts
- Verifying DMCA §512 designated agent registration requirements (US Copyright Office)
- Finding current AAA/JAMS consumer arbitration rules updates

Save research results to `/tmp/legalcode-tos-research.md` for reference during drafting.

**Without legalcode-mcp** (graceful degradation):
- Proceed with knowledge-based drafting and flag all statutory citations with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Prioritize client review of: COPPA Rule current text; California B&P §17600 as amended;
  DSA Art. 14 guidance; UK DMCCA 2024 effective dates; ACL penalty regime

### Perplexity Search (fallback research)

Use the perplexity-search skill for:
```bash
uv run ~/.claude/skills/perplexity-search/scripts/perplexity_search.py "<query>"
```

Recommended queries:
- "Terms of service legal requirements US EU UK Australia 2025 2026"
- "COPPA enforcement actions FTC 2024 2025 age verification"
- "California auto-renewal law B&P 17600 amendments July 2025"
- "DSA Article 14 terms of service requirements compliance"
- "UK DMCCA 2024 subscription contract requirements effective date"
- "ACL unfair contract terms civil penalties ACCC enforcement 2024 2025"

---

## Glass Box Audit Trail

Include this template in the analysis header for every TOS drafting or audit session:

```yaml
glass_box:
  skill_name: "legalcode-terms-of-service-drafter"
  session_type: "Draft from scratch / Compliance audit / Clause review / Update"
  platform_type: "[SaaS / Mobile / Marketplace / Social / E-commerce / API / Other]"
  user_audience: "[B2C / B2B / Both]"
  target_jurisdictions:
    - "[US / EU / UK / AU / CA / Other]"
  special_services:
    - "[UGC / AI features / Subscription / Minors / Marketplace / Other]"
  regulatory_frameworks_assessed:
    - "[COPPA / DMCA / DSA / DMA / ACL / CRA 2015 / DMCCA 2024 / CASL / CAN-SPAM / Other]"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "/tmp/legalcode-tos-research.md or Not created"
  quality_score: "[X]/40"
  completeness: "[X]/18 elements"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED — marked [VERIFY]]"
  high_risk_provisions:
    - "[Auto-renewal / Arbitration / Liability cap / UGC AI training / COPPA / Other]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "All statutory references carry hallucination risk — verify against authoritative sources"
    - "Consumer protection law changes frequently — verify currency before publication"
    - "Specialized legal counsel required for HIPAA, FINRA, gambling, children's platforms"
    - "[Any additional scope limitations]"
  reviewer: "AI-assisted — requires qualified legal review before publication"
```

---

## Output Format Template

Structure all TOS drafting guidance using this template:

```markdown
# Terms of Service Drafting Report

**Platform**: [Platform name / type]
**Audience**: [B2C / B2B / Both]
**Target Jurisdictions**: [List]
**Report Date**: [Date]
**Skill Version**: legalcode-terms-of-service-drafter v1.0
**Status**: [DRAFT — Requires Legal Review Before Publication]

---

## Glass Box Audit Trail
[Insert YAML glass_box block]

---

## Regulatory Framework Assessment

| Framework | Applicable | Key Obligations | Confidence |
|-----------|------------|-----------------|------------|
| COPPA (US) | [YES/NO] | [Summary] | [0.0-1.0] |
| DMCA §512 | [YES/NO] | [Summary] | [0.0-1.0] |
| DSA (EU) | [YES/NO] | [Summary] | [0.0-1.0] |
| ... | | | |

---

## Clause-by-Clause Drafting Guidance

### 1. Acceptance and Agreement Formation

**Classification**: [REQUIRED / RECOMMENDED / OPTIONAL]
**Compliance Risk**: [CRITICAL / HIGH / MEDIUM / LOW]
**Confidence**: [0.0-1.0]

**Recommended Draft Language:**
> [Draft TOS text in plain language, formatted for inclusion]

**Jurisdictional Notes:**
- **US**: [Note]
- **EU**: [Note]
- **UK**: [Note]
- **AU**: [Note]
- **CA**: [Note]

**Regulatory Basis**: [Statutory citation(s)]
**Review Required**: [YES/NO and reason]

---

### 2. Account Registration and Security
[Repeat structure for each section]

---
[Continue for all applicable sections]

---

## B2C vs. B2B Comparison

[Insert B2C/B2B comparison table for high-impact clauses]

---

## Compliance Gap Summary (Audit Mode)

| Gap | Severity | Jurisdiction | Action Required | Deadline |
|-----|----------|-------------|-----------------|---------|
| [Description] | [CRITICAL/HIGH/MEDIUM/LOW] | [Jurisdiction] | [Action] | [Timeline] |

---

## Prioritized Action Plan

### Tier 1 — Address Before Publication
- [ ] [Action item with statutory basis]

### Tier 2 — Address Within 30 Days
- [ ] [Action item]

### Tier 3 — Next Review Cycle
- [ ] [Action item]

---

## Recommended Next Steps

1. [Specific legal review items — counsel to verify auto-renewal compliance]
2. [Specific regulatory consultation items — COPPA age gate implementation]
3. [Privacy Policy alignment — ensure TOS cross-references are consistent]
4. [Implementation items — DMCA agent registration with US Copyright Office]
5. [Monitoring items — quarterly check on auto-renewal law amendments]

---

*This analysis was produced by legalcode-terms-of-service-drafter. It does not constitute
legal advice. Review by qualified legal professionals licensed in each applicable jurisdiction
is required before publishing or enforcing any Terms of Service.*
```

---

## Localization Notes

When creating jurisdiction-specific TOS supplements or standalone jurisdiction TOS:

### EU-Specific Supplement
- Include EU consumer protection rights summary (withdrawal rights, conformity guarantee)
- DSA Art. 14 compliant content moderation section with appeals reference
- EU ADR / out-of-court dispute settlement link (DSA Art. 21)
- GDPR data subject rights summary with link to Privacy Policy
- No mandatory arbitration clause — litigation in local courts available
- Governing law savings clause for Rome I Art. 6 compliance
- VAT/GST disclosure and digital services place-of-supply rules

### UK-Specific Supplement
- CRA 2015 Part 2 unfair terms compliance (grey list review)
- DMCCA 2024 subscription reminder and cancellation provisions (when in force)
- Online Safety Act 2023 safety duties acknowledgment
- UK GDPR data subject rights cross-reference
- UK courts as alternative to arbitration for consumer claims under £5,000

### Australia-Specific Supplement
- ACL consumer guarantee acknowledgment — cannot be excluded
- ACL unfair terms compliance — review all standard-form terms against grey list
- ACCC complaint escalation reference
- Privacy Act 1988 / APP compliance cross-reference

### Canada-Specific Supplement
- CASL: separate email marketing consent mechanism; TOS acceptance ≠ CASL consent
- PIPEDA Privacy Policy cross-reference
- Quebec Law 25: automated decision-making disclosure; PI incident cross-reference
- Ontario CPA 2002 internet agreement disclosures (if applicable)
- Province-specific consumer protection references [JURISDICTION-SPECIFIC]

---

## Provenance

Created by Legalcode as a new original synthesis (2026-03-01). Research-backed drafting
skill covering US (COPPA, DMCA §512, Section 230, FTC Act §5, FAA, Ending Forced Arbitration
Act 2022, CAN-SPAM, state auto-renewal laws — California B&P §§17600–17606, New York GBL
§527-A), EU (Consumer Rights Directive 2011/83/EU, Unfair Contract Terms Directive
93/13/EEC, Digital Services Act 2022/2065, Digital Markets Act 2022/1925, CDSM Directive
2019/790, Rome I Regulation 593/2008, GDPR 2016/679), UK (Consumer Rights Act 2015, Digital
Markets Competition and Consumers Act 2024, Online Safety Act 2023), Australia (ACL —
unfair contract terms civil penalties from November 2023, consumer guarantees, Privacy Act
1988 as amended), and Canada (PIPEDA, CASL, Quebec Law 25). 18-element Legalcode quality
framework applied. All statutory references marked [VERIFY] for currency verification.
Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers throughout.
