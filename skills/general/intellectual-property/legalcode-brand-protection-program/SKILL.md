---
name: legalcode-brand-protection-program
description: Develops and audits brand protection programs covering trademark monitoring, domain name
  disputes (UDRP/URS/ACPA), social media enforcement (Meta/Instagram, X/Twitter, TikTok, YouTube, LinkedIn),
  counterfeit investigation and test purchasing, online marketplace takedowns (Amazon Brand Registry/Project
  Zero/Transparency, eBay VeRO, Alibaba IPP, Etsy, Temu, Shein), and customs recordation (US CBP IPRS,
  EU AFA/608/2013). Use when building a brand protection program from scratch, auditing an existing program
  for gaps, responding to a counterfeiting crisis, evaluating enforcement options for a specific threat,
  or developing enforcement SOPs for in-house legal teams.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Develops and audits brand protection programs covering trademark monitoring, domain name disputes (UDRP/URS/ACPA), social media enforcement (Meta/Instagram, X/Twitter, TikTok, YouTube, LinkedIn), counterfeit investigation and test purchasing, online marketplace takedowns (Amazon Brand Registry/Project Zero/Transparency, eBay VeRO, Alibaba IPP, Etsy, Temu, Shein), and customs recordation (US CBP IPRS, EU AFA/608/2013). Builds multi-jurisdictional enforcement strategies with threat prioritization, evidence documentation workflows, and escalation frameworks covering civil, administrative, and criminal referral paths. Use when building a brand protection program from scratch, auditing an existing program for gaps, responding to a counterfeiting crisis, evaluating enforcement options for a specific threat, or developing enforcement SOPs for in-house legal teams. Also triggers for: "trademark monitoring," "domain dispute," "UDRP filing," "URS complaint," "takedown notice," "Amazon Brand Registry," "eBay VeRO," "Alibaba counterfeit," "customs recordation," "CBP recordation," "anti-counterfeiting program," "gray market enforcement," "social media brand enforcement," "trademark infringement online," "brand protection audit," "marketplace infringement," "product authentication," "counterfeit investigation," "brand protection strategy," or "online brand enforcement."


# Legalcode Brand Protection Program

> **Disclaimer**: This skill provides a framework for AI-assisted brand protection program
> development and enforcement analysis. It does not constitute legal advice. All outputs
> should be reviewed by a qualified legal professional (trademark counsel, IP litigation
> counsel, or brand protection specialist) licensed in the relevant jurisdiction before
> acting on them. Statutory references, platform policy citations, and enforcement
> statistics carry hallucination risk — verify against current authoritative sources
> (USPTO, WIPO, ICANN, platform IP portals, CBP, EUIPO) before relying on them. Platform
> policies change frequently; confirm current program requirements before filing. Brand
> protection strategy is intensely fact-specific; this skill provides analytical structure
> and frameworks, not final legal conclusions.

---

## Purpose and Scope

This skill develops and audits brand protection programs for trademark owners, brand
managers, and in-house counsel. It covers the full lifecycle from monitoring through
enforcement across digital and physical channels.

**Covers:**

- Trademark watch program design and gap assessment
- Domain name enforcement: UDRP, URS, ACPA, and negotiated transfers
- Social media brand enforcement across major platforms
- Online marketplace takedown programs: Amazon, eBay, Alibaba, and emerging platforms
- Counterfeit investigation methodology: test purchasing, digital investigation, supply chain tracing
- Customs recordation: US CBP IPRS and EU Application for Action (AFA)
- Criminal referral frameworks: DOJ, ICE-HSI, FBI, FDA (for counterfeit goods)
- Product authentication technology: holograms, QR, NFC, serialization
- Multi-jurisdictional enforcement strategy with priority market mapping
- Brand protection technology platform selection and integration
- Enforcement SOP development for in-house legal and brand teams

**Does not:**

- Draft or prosecute trademark applications (see trademark filing skills)
- Provide litigation strategy for pending trademark infringement lawsuits
- Replace qualified trademark counsel, brand protection investigators, or customs brokers
- Apply to copyright-only enforcement (see legalcode-dmca-takedown-workflow)
- Provide legal advice or conclusions

## Jurisdiction and Governing Law

This is a multi-jurisdictional skill. Brand protection programs operate across all
jurisdictions where a brand has trademark rights, commercial presence, or online
visibility — which in most cases means globally.

[JURISDICTION-SPECIFIC] When localizing, research and apply:

- **US**: Lanham Act (15 U.S.C. §§ 1051 et seq.), ACPA (15 U.S.C. § 1125(d)),
  Trademark Counterfeiting Act of 1984 (18 U.S.C. §§ 2320 et seq.), CBP IPRS recordation
- **EU**: EU Trade Mark Regulation 2017/1001 (EUTMR), EU Customs Regulation 608/2013
  (border enforcement), EU Trademark Directive 2015/2436, EUIPO AFA system
- **UK**: Trade Marks Act 1994, Fraud Act 2006, Trading Standards enforcement, UKIPO
- **China**: Trademark Law of China (2019 revision), administrative enforcement via CNIPA
  and AIC, customs recordation with GACC, criminal prosecution thresholds [VERIFY]
- **International**: TRIPS Agreement Arts. 16–17, 41–43 (minimum enforcement standards),
  Madrid Protocol (WIPO), Paris Convention for the Protection of Industrial Property

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's intent or brand's situation, the workflow pauses and asks when:

- The answer would change the direction of the analysis or enforcement recommendation
- Multiple enforcement pathways exist and the choice depends on business context
- Threat classification requires brand-specific risk tolerance information
- Evidence quality or availability is unknown

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

### Step 1: Accept the Brief

Accept input in any of these formats:

- **Program build**: User wants to build a brand protection program from scratch
- **Program audit**: User wants to audit an existing program for gaps
- **Specific threat**: User has an active infringement to address and needs an action plan
- **SOP development**: User wants enforcement SOPs and documentation templates
- **Platform-specific**: User needs help with a particular channel (e.g., Amazon Brand Registry, UDRP)

If no clear brief is provided, ask the user to describe their situation before proceeding.

### Step 2: Gather Brand and Threat Context

**⟁ CLARIFY** — Before beginning, ask the user these questions. Present as structured
options where possible. Skip any already answered by the initial prompt.

1. **Program mode**: What are you trying to accomplish?
   - Options:
     - **Build new program** — Design brand protection infrastructure from scratch
     - **Audit existing program** — Identify gaps in a current program
     - **Respond to active threat** — Address a specific infringement incident
     - **Develop SOPs** — Create enforcement procedures and documentation templates
     - **Channel-specific guidance** — Guidance for a specific platform or enforcement mechanism
   - _Why this matters_: Each mode produces a fundamentally different output.

2. **Brand profile**: What is the scope of the brand?
   - IP assets: Registered trademarks (number and jurisdictions), pending applications,
     common law marks, trade dress, domain portfolio, product authentication systems
   - Brand tier: Niche/emerging, established mid-market, or globally famous (dilution protection)
   - Industry: Consumer goods, pharma, luxury, tech, automotive, food/beverage, other
   - _Why this matters_: Enforcement priorities and available remedies differ significantly
     across brand tiers and industries. Famous marks have dilution protection; consumer
     health/safety industries warrant criminal referral more readily.

3. **Threat landscape**: What infringement activity is occurring?
   - **Domain threats**: Cybersquatting, typosquatting, phishing domains, social engineering
   - **Marketplace threats**: Counterfeits on Amazon/eBay/Alibaba/Temu/Shein, unauthorized resale
   - **Social media threats**: Impersonator accounts, unauthorized brand use in advertising
   - **Physical/retail threats**: Counterfeit goods, gray market imports, parallel imports
   - **Digital threats**: Brand name in keyword advertising, unauthorized app use, phishing
   - _Why this matters_: Determines which enforcement channels to prioritize.

4. **Current program maturity**:
   - Options: No program (starting from scratch), Basic (ad hoc responses), Intermediate
     (some monitoring/takedowns), Advanced (systematic program with metrics)
   - _Why this matters_: Determines how much infrastructure needs to be built vs. refined.

5. **Jurisdictional scope**: Which markets matter most?
   - Primary markets (where most revenue is generated or brand is most exposed)
   - Problem markets (where counterfeiting/infringement is concentrated)
   - Emerging markets requiring protection build-out
   - _Why this matters_: Resource allocation and enforcement strategy differ dramatically
     between US/EU (mature systems) and China/India/Brazil (higher enforcement complexity).

6. **Resources and urgency**:
   - Available budget: Minimal (in-house only), Moderate (some external support), Significant
     (dedicated brand protection budget)
   - Urgency: Crisis (active harm), Standard (ongoing program), Strategic (long-term build)
   - _Why this matters_: Determines the tier of monitoring technology and external counsel
     engagement to recommend.

If partial context is provided, state assumptions explicitly and proceed.

### Step 3: Load Existing Program Documentation

If auditing an existing program, check for documentation including:

- Current trademark registration portfolio and watch services
- Domain portfolio management records
- Platform enrollment records (Amazon Brand Registry, eBay VeRO, etc.)
- CBP/EU customs recordation records
- Past enforcement actions and takedown history
- Brand protection technology platform in use
- Enforcement policy or SOPs

**⟁ CLARIFY** — If documentation is available, ask the user to share it (or describe it)
so the audit can compare the current state against the program framework in Step 4.

If no existing program documentation exists, proceed with the new program build workflow.

### Step 4: Gather Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** to gather relevant legal authority for the key jurisdictions in scope.

**For each primary jurisdiction, research:**

1. Trademark enforcement statutes and remedies available (civil and criminal)
2. Domain dispute resolution mechanisms available beyond UDRP/URS (national ccTLD policies)
3. Customs recordation system and requirements
4. Administrative enforcement options (trademark office, consumer protection agencies)
5. Criminal prosecution thresholds for trademark counterfeiting
6. Recent significant enforcement decisions or regulatory changes

**If legalcode-mcp is not connected:**

- Proceed with the general multi-jurisdictional framework below
- Mark all jurisdiction-specific statutory references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`

### Step 5: Program Framework Assessment

Assess the brand protection program across eight domains. For each domain, evaluate:
(a) current state (if auditing), or (b) what must be built (if creating from scratch).

For each finding, apply the **Severity Classification** defined below.

---

#### Domain 1: Trademark Portfolio and Registration Strategy

**Assess:**

- [ ] Core brand elements registered in all key commercial jurisdictions
- [ ] Madrid Protocol filings for cost-effective multi-jurisdiction coverage
- [ ] Class coverage appropriate for the brand's goods/services and realistic extensions
- [ ] Defensive registrations in key problem markets (e.g., China — register before entering)
- [ ] Trade dress and 3D mark registrations where applicable
- [ ] Renewal calendar and docketing system in place
- [ ] Trademark watch service configured and active
- [ ] Watch coverage: exact match, phonetic similarity, visual/logo similarity, related classes
- [ ] Watch vendor(s) in use (Corsearch, CompuMark/SAEGIS, TrademarkNow, etc.)
- [ ] Response protocol for watch alerts (triage criteria, response timelines, escalation)

**Critical gaps:**

- No trademark registration in a key commercial market (CRITICAL)
- No trademark watch service (CRITICAL for active brands)
- Watch coverage limited to exact matches only (HIGH — misses phonetic/visual threats)
- No response protocol for watch alerts, causing backlogs (HIGH)
- Class coverage misses adjacent product lines (MEDIUM)
- No defensive registrations in high-counterfeiting markets (MEDIUM for consumer goods)

[JURISDICTION-SPECIFIC] China requires separate registration via CNIPA — Madrid Protocol
alone does not guarantee Chinese protection. File directly with CNIPA in relevant classes.
India requires filing in each class separately; Madrid Protocol coverage has been improving.
Brazil backlog: allow 24-36 months for registration [VERIFY current timelines].

#### Domain 2: Domain Name Enforcement Program

**Assess:**

- [ ] Core brand domains registered across all primary TLDs (.com, .net, .org, country codes)
- [ ] Common misspellings, typosquats, and hyphenated variants registered defensively
- [ ] Domain monitoring service active (monitoring new registrations containing brand elements)
- [ ] Decision matrix for domain threats: monitor vs. UDRP vs. URS vs. ACPA vs. negotiate
- [ ] UDRP filing process documented and external counsel identified
- [ ] URS process documented for new gTLD threats
- [ ] ACPA litigation option evaluated for US-targetted cybersquatting with monetary harm
- [ ] Negotiated transfer protocol (cease and desist + transfer offer) for non-adversarial cases

**UDRP checklist (if filing):**

A UDRP complaint must establish all three elements under ICANN UDRP Policy ¶ 4(a):

1. The domain is identical or confusingly similar to a trademark or service mark in which
   the complainant has rights
2. The registrant has no rights or legitimate interests in respect of the domain
3. The domain has been registered and is being used in bad faith

**Evidence to gather for UDRP:**

- [ ] Evidence of trademark rights (registration certificates or evidence of common law use)
- [ ] Screenshots showing confusing similarity between the domain and the mark
- [ ] Evidence of bad faith: commercial use, offer to sell to brand owner, use for phishing/malware,
      pattern of cybersquatting, no legitimate use visible on or before notice of dispute
- [ ] Evidence negating registrant's legitimate interests (no license granted, not commonly known
      by the domain, not legitimate noncommercial/fair use)

**URS vs. UDRP decision matrix:**

| Factor             | URS                                     | UDRP                                    |
| ------------------ | --------------------------------------- | --------------------------------------- |
| Remedy             | Suspension only (registration term)     | Transfer or cancellation (permanent)    |
| Standard of proof  | Clear and convincing                    | Preponderance of evidence               |
| Timeline           | ~3 weeks                                | 2-4 months                              |
| Cost               | ~$375                                   | ~$1,500+                                |
| Applicable domains | New gTLDs only (.xyz, .io, .app, etc.)  | All TLDs                                |
| Best for           | Blatant squatting, rapid interim relief | Contested ownership, permanent transfer |

**ACPA (15 U.S.C. § 1125(d)) triggers:**

- Domain targets a US-based or US-famous mark
- Monetary damages sought ($1,000–$100,000 per domain) in addition to transfer
- Criminal prosecution potential (DOJ/ICE involvement warranted)
- In rem action available when registrant is unidentifiable [VERIFY]

[JURISDICTION-SPECIFIC] Country-code TLD (ccTLD) disputes (e.g., .uk, .de, .cn) are
governed by national/registrar policies, not UDRP. Nominet DRS governs .uk; DENIC for
.de; CNNIC for .cn. Research the applicable policy for each ccTLD in dispute.

#### Domain 3: Social Media Brand Enforcement

**Assess:**

- [ ] Official accounts established and verified on all major platforms relevant to the brand
- [ ] Monitoring in place for brand name misuse in usernames, handles, and page names
- [ ] Monitoring in place for unauthorized use of brand logos and trademarks in profiles/posts
- [ ] Monitoring in place for counterfeit product promotion and fraudulent giveaways
- [ ] Platform-specific enforcement workflows documented

**Platform-specific enforcement processes:**

| Platform                  | Report Type                           | Portal                                          | Typical Timeline                   | Notes                                             |
| ------------------------- | ------------------------------------- | ----------------------------------------------- | ---------------------------------- | ------------------------------------------------- |
| Meta (Facebook/Instagram) | Trademark infringement, impersonation | IP Reporting Center (ipprotection.facebook.com) | 24–72 hours                        | Centralized for trademark + copyright             |
| X (Twitter)               | Trademark violation, impersonation    | trademark.twitter.com / impersonation form      | 3–7 days                           | Robust handle/username transfer process           |
| TikTok                    | Trademark infringement                | TikTok IP infringement form                     | 3–10 days                          | Slower processing; escalation available           |
| YouTube/Google            | Trademark + DMCA                      | YouTube webform + Google Ads trademark policy   | 48 hours (YouTube); variable (Ads) | Separate DMCA for content; trademark for branding |
| LinkedIn                  | Brand impersonation, trademark misuse | LinkedIn IP portal                              | 3–5 days                           | Strongest for professional/B2B brand issues       |
| Pinterest                 | Trademark infringement                | Pinterest IP reporting form                     | 3–7 days                           | Important for product imagery infringement        |

**For each platform report, document:**

- [ ] Trademark registration details: jurisdiction, registration number, goods/services
- [ ] Links to all infringing profile URLs or content
- [ ] Screenshots with timestamps showing the infringement
- [ ] Description of how the use causes consumer confusion or falsely implies affiliation
- [ ] Requested remedy: account suspension, username change, content removal

**Impersonation vs. trademark infringement distinction:**

- **Impersonation**: Account falsely claims to be or represent the brand — use impersonation
  process on platforms that treat this more aggressively and with faster turnaround
- **Trademark infringement**: Account uses trademark in commerce causing likelihood of
  confusion — use trademark report process

**⟁ CLARIFY** — If multiple infringing accounts exist across platforms, ask whether
the user wants to:

- Run all takedowns in parallel (maximizes speed)
- Prioritize by platform based on where the brand has greatest exposure
- Run a test batch on one platform to calibrate evidence packages before scaling

#### Domain 4: Online Marketplace Takedown Program

**Assess:**

- [ ] Amazon Brand Registry enrollment (required before other Amazon tools available)
- [ ] Amazon Project Zero enrollment (if eligibility criteria met)
- [ ] Amazon Transparency Program enrollment (for product authentication)
- [ ] eBay VeRO enrollment and VeRO Participant Profile created
- [ ] Alibaba/AliExpress IPP Platform account set up with IP rights uploaded
- [ ] Temu Brand Guardian Initiative enrollment (if applicable)
- [ ] Other platform programs: Etsy, Shein, Wish (platform-specific processes)
- [ ] Takedown SOP documented: evidence standards, submission workflow, escalation
- [ ] Enforcement metrics tracked: takedowns submitted, removed, rejected, re-listed

**Amazon Brand Registry enforcement ladder:**

| Tool                     | Purpose                                        | Cost          | Eligibility                              |
| ------------------------ | ---------------------------------------------- | ------------- | ---------------------------------------- |
| Brand Registry           | Core enrollment; all other tools require this  | Free          | Active registered trademark              |
| Report a Violation (RAV) | Manual takedown of individual listings         | Free          | Brand Registry enrollment                |
| Project Zero             | Self-service automated takedown                | Free          | Brand Registry + eligibility review      |
| Transparency             | Unit-level authentication via QR/serialization | Per-unit cost | Brand Registry + supply chain capability |
| IP Accelerator           | Expedited trademark registration support       | Variable      | Direct application                       |

**Amazon Project Zero accuracy requirement**: Maintain 99%+ accuracy rate on takedowns.
False positives (removing legitimate listings) can result in program suspension. Maintain
an evidence review process before every removal action.

**Amazon Transparency interoperability (2025)**: Existing product serial numbers can be
used — no new barcodes or packaging changes required. Available in US, UK, DE, FR, IT,
ES, CA, AU, JP, IN.

**eBay VeRO enrollment requirements:**

- Submit request to vero@ebay.com [VERIFY current submission address]
- Provide: trademark registration certificate or number + evidence of right to use
  (license agreement or owner confirmation)
- After enrollment: File Notice of Claimed Infringement (NOCI) for each infringing listing
- Create a VeRO Participant Profile explaining the brand's IP policies

**Alibaba/AliExpress IPP Platform workflow:**

1. Create account at ipp.alibabagroup.com — provide company details + identity verification
2. Upload IP rights: trademark registration, copyright, patents as applicable
3. Account/IPR review: up to 3 business days
4. After approval: submit takedown requests (standard < 3 days; high-priority < 24 hours)
5. Monitor for relisting (systematic relisting = escalate to Alibaba IP enforcement team)

**⟁ CLARIFY** — For high-volume counterfeit environments (>50 infringing listings/month),
ask whether to recommend:

- Manual takedown process (current scale) with documentation templates
- Semi-automated process using a brand protection platform (Red Points, Corsearch, BrandShield)
- Fully automated platform with AI-driven detection and takedown automation

**Evidence package for any marketplace takedown:**

- [ ] Brand trademark registration(s): jurisdiction, class, registration number, certificate
- [ ] Clear identification of the infringing listing: URL, ASIN/SKU, seller name
- [ ] Side-by-side comparison of authentic vs. infringing product/packaging
- [ ] Test purchase documentation (if conducted): order confirmation, photos, authentication analysis
- [ ] Statement that use is unauthorized and not licensed
- [ ] Rights holder contact information

#### Domain 5: Counterfeit Investigation and Test Purchasing

**Assess:**

- [ ] Monitoring program in place across targeted platforms and physical markets
- [ ] Test purchase protocol documented (anonymity, chain of custody, authentication)
- [ ] Authentication process for suspected counterfeits (internal QC, third-party lab)
- [ ] Evidence documentation standards meeting legal proceeding requirements
- [ ] Digital investigation capabilities (web scraping, reverse image search, metadata analysis)
- [ ] Supply chain tracing capability (following counterfeit goods back to source)
- [ ] Investigation firm relationships (if outsourcing physical investigation)

**Test purchase protocol:**

| Step               | Action                                                                       | Documentation Required                                            |
| ------------------ | ---------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| 1. Identify target | Confirm listing is suspected counterfeit before purchase                     | Screenshots, listing URL, ASIN/seller ID                          |
| 2. Purchase        | Use anonymous/non-branded account; personal credit card; residential address | Order confirmation, payment receipt                               |
| 3. Receive         | Document unboxing completely                                                 | Video of unboxing, photos of packaging, insert materials, product |
| 4. Authenticate    | Compare to authentic product; send to QC team or lab if needed               | Authentication report, side-by-side photos                        |
| 5. Document        | Create complete evidence file with chain of custody                          | Chain of custody log, all documentation                           |
| 6. Store           | Preserve physical evidence securely                                          | Evidence storage log                                              |
| 7. Use             | Support takedown requests, law enforcement referral, or litigation           | Evidence package with all documentation                           |

**Critical test purchase rules:**

- Never purchase from an account linked to the brand (destroys anonymity; could alert seller)
- Never destroy the physical product after authentication (physical evidence is critical)
- Maintain strict chain of custody from purchase through potential court proceedings
- In some jurisdictions, test purchases by or at direction of law enforcement may be required
  for criminal proceedings — coordinate with local counsel before conducting test purchases

**Digital investigation toolkit:**

| Tool Type                  | Purpose                              | Examples                                            |
| -------------------------- | ------------------------------------ | --------------------------------------------------- |
| Reverse image search       | Identify stolen product/brand images | Google Reverse Image, TinEye, Bing Visual Search    |
| Brand monitoring platforms | Automated marketplace/web scanning   | Red Points, Corsearch, BrandShield, MarkMonitor     |
| WHOIS/domain investigation | Domain registrant research           | ICANN WHOIS, DomainTools, DomainIQ                  |
| Social media intelligence  | Seller network mapping               | Platform native search, social listening tools      |
| Web archiving              | Preserve ephemeral evidence          | Wayback Machine (archive.org), screenshot tools     |
| Supply chain mapping       | Trace counterfeit source             | Shipping documents, seller account cross-references |

#### Domain 6: Customs Recordation and Border Enforcement

**Assess:**

- [ ] US CBP IPRS recordation: all federally registered trademarks recorded
- [ ] US CBP: renewal calendar tracked (term-limited recordation)
- [ ] EU AFA: Application for Action filed with EUIPO for key trademarks
- [ ] EU AFA: Union AFA strategy (single filing covering multiple Member States)
- [ ] Other key jurisdiction customs recordations: China GACC, UK HMRC, Brazil RFB, India
- [ ] Customs enforcement contacts identified and relationships maintained
- [ ] Border seizure response protocol: actions to take when CBP/customs detains goods
- [ ] Authentic product samples and brand information on file with customs

**US CBP IPRS recordation process:**

| Element                 | Detail                                                                             |
| ----------------------- | ---------------------------------------------------------------------------------- |
| Portal                  | iprr.cbp.gov (e-Recordation)                                                       |
| Eligible IP             | Federally registered trademarks (USPTO), registered copyrights (USCOP)             |
| Fee                     | $190 per International Class (trademark) or per copyright; $80/IC renewal          |
| Validity                | Fixed term; renewable                                                              |
| CBP authority           | Detain, seize, forfeit, and destroy merchandise bearing infringing mark            |
| Gray market distinction | CBP has limited authority over genuine gray market goods vs. outright counterfeits |
| Contact                 | IPE Branch, Regulations and Rulings: HQIPRBranch@cbp.dhs.gov                       |

**CBP seizure response protocol:**
When CBP detains a shipment as potentially infringing:

1. CBP notifies the trademark owner of the detention (if recorded with IPRS)
2. Trademark owner has the opportunity to confirm: authentic vs. counterfeit
3. Provide CBP with: authenticated product samples, brand guidelines, distinctive features
4. If confirmed counterfeit: CBP proceeds with forfeiture and destruction
5. Obtain detention/seizure records for use in civil or criminal enforcement

**EU Application for Action (AFA) under Regulation 608/2013:**

| Element              | Detail                                                                            |
| -------------------- | --------------------------------------------------------------------------------- |
| Legal basis          | EU Regulation 608/2013 (repealed 1383/2003)                                       |
| Portal               | EUIPO IP Enforcement Portal (IPEP) or national customs portals (COPIS-integrated) |
| Mandatory electronic | eAFA required since October 3, 2024 — no paper filings accepted                   |
| Scope                | National AFA (one Member State) or Union AFA (multiple Member States)             |
| Cost                 | Free                                                                              |
| Duration             | 1 year; extendable and updatable                                                  |
| Eligible rights      | EU trademarks, EU designs, national marks where filed with national customs       |

[JURISDICTION-SPECIFIC] China GACC customs recordation: Register with GACC (Customs
Intellectual Property Management System) to enable Chinese customs enforcement. Required
for effective border protection in China — do not rely solely on CNIPA trademark registration.
[VERIFY current GACC registration procedures and fees]

[JURISDICTION-SPECIFIC] India Customs: India has a customs recordation system under
IP (Customs) Rules 2007, administered by CBIC (Central Board of Indirect Taxes and
Customs). Registration required for active border enforcement. [VERIFY current procedure]

#### Domain 7: Criminal Referral Framework

**Assess:**

- [ ] Criminal referral threshold criteria documented (when to escalate beyond civil)
- [ ] Relationships with relevant law enforcement agencies established
- [ ] Documentation standards meeting criminal evidence requirements
- [ ] DOJ/USA guidelines understood for trademark counterfeiting prosecution
- [ ] Consumer safety implications assessed (triggers mandatory criminal reporting in some cases)

**Criminal referral triggers (US):**

| Trigger                                            | Agency                                                  | Legal Basis                                     |
| -------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------- |
| Trademark counterfeiting (commercial scale)        | DOJ / US Attorney's Office, ICE-HSI                     | 18 U.S.C. § 2320 (Trademark Counterfeiting Act) |
| Counterfeit goods affecting consumer health/safety | FDA (pharma, food), CPSC (products), NHTSA (auto parts) | Product safety statutes                         |
| Import of counterfeit goods                        | CBP + ICE-HSI                                           | Customs laws, § 2320                            |
| Mail/wire fraud via counterfeit sales              | FBI                                                     | 18 U.S.C. §§ 1341, 1343                         |
| RICO patterns (organized counterfeiting)           | FBI + DOJ                                               | 18 U.S.C. §§ 1961–1968                          |

**Criminal penalty benchmarks (US — 18 U.S.C. § 2320) [VERIFY current sentencing guidelines]:**

- First offense, individual: up to $2 million fine + 10 years imprisonment
- First offense, organization: up to $5 million fine
- Subsequent offenses: penalties approximately doubled/tripled
- Counterfeit goods with consumer safety impact: enhanced sentencing

**Criminal evidence requirements (higher than civil/administrative):**

- Chain of custody documentation must be pristine
- Test purchases conducted or supervised by law enforcement
- Financial investigation data (seller transaction records, profit evidence)
- Organized network evidence (multiple sellers, coordinated supply chain)
- Undercover purchases may require law enforcement involvement
- Document and preserve all digital evidence under forensic standards

**⟁ CLARIFY** — Before recommending criminal referral, ask:

- "Do you have evidence of the counterfeiter's identity and physical location?"
- "Is there a consumer health/safety risk from the counterfeit product?"
- "Is there evidence of an organized network (multiple sellers, coordinated distribution)?"
- "Has civil enforcement (takedowns, ACPA, litigation) been attempted and failed?"

Criminal prosecution is resource-intensive for both the brand and law enforcement. Focus
referrals on cases with: (a) consumer safety risk, (b) organized distribution networks,
(c) significant commercial scale, or (d) identifiable targets in reachable jurisdictions.

#### Domain 8: Product Authentication and Anti-Counterfeiting Technology

**Assess:**

- [ ] Authentication technology in use or evaluated
- [ ] Consumer-facing authentication tools deployed
- [ ] Authentication data collection and analysis in place
- [ ] Gray market detection capability (authentication codes used outside intended channel)
- [ ] Packaging security features (holograms, inks, substrates)

**Authentication technology comparison:**

| Technology                 | Counterfeit Resistance            | Consumer Accessibility | Data Collection | Cost        |
| -------------------------- | --------------------------------- | ---------------------- | --------------- | ----------- |
| Holograms                  | Medium (increasingly replicated)  | High (visual)          | None            | Low         |
| QR codes (database-linked) | Medium (requires secure database) | High (smartphone)      | High            | Very low    |
| NFC tags                   | High (cryptographic, anti-clone)  | High (smartphone)      | Very high       | Medium      |
| Serialization              | High (supply chain track/trace)   | Medium (requires scan) | Very high       | Medium-High |
| RFID                       | High (supply chain)               | Low (requires reader)  | High            | High        |

**Recommended hybrid approach for consumer products:**

1. Serialization: Unique identifier on every unit (supply chain integrity)
2. QR code or NFC: Consumer-facing authentication (smartphone-accessible)
3. Packaging security feature: Visual deterrence (hologram, security ink)
4. Authentication database: Central verification system with geolocation analytics

**Gray market detection through authentication:**

- Authentication codes scanned in an unauthorized market (e.g., product meant for Europe
  scanned in US) indicate gray market diversion
- Use authentication data to identify distributors violating territorial restrictions
- Authentication data provides evidence for distributor agreement enforcement

---

### Step 6: Threat Classification and Prioritization

Classify each identified threat or program gap using the five-tier severity system:

#### Severity Classification

**CRITICAL — Immediate Action Required**

Active infringement causing material harm to brand, consumers, or business. Irreversible
harm risk if not addressed within 24-72 hours.

**Examples:**

- Counterfeit pharmaceuticals, food, automotive parts, or children's products (safety risk)
- Phishing domain actively harvesting consumer credentials using brand identity
- Organized counterfeit network with high sales volume and wide distribution
- Domain impersonating brand for fraudulent sales/financial fraud
- Trademark registration filing by third party in key market (requires opposition window action)

**Action**: Escalate immediately. Activate crisis protocol. Engage external counsel.
Consider criminal referral, emergency injunction, or ex parte seizure order.

---

**HIGH — Priority Enforcement (48–72 hours)**

Significant active infringement with material brand dilution or consumer confusion risk.
Not immediate safety risk but requires prompt response.

**Examples:**

- Multiple marketplace listings of counterfeit products with high sales volume
- Verified social media impersonator accounts with significant follower counts
- Active UDRP-eligible cybersquatting domain diverting brand traffic
- Counterfeit goods at physical retail (markets, brick-and-mortar stores)
- Brand name used in keyword advertising directing to competitor or counterfeit site

**Action**: Initiate enforcement action. File takedown requests/UDRP within 48-72 hours.
Document evidence thoroughly. Engage brand protection platform if volume is high.

---

**MEDIUM — Standard Enforcement (1-2 weeks)**

Moderate infringement requiring response but not immediately damaging.

**Examples:**

- Marketplace listings with moderate sales volume; likely counterfeits but unverified
- Social media accounts with small following using brand identity without authorization
- Monitoring alerts for potentially infringing trademark applications
- Domain registrations that may be cybersquatting but are not yet in active use
- Unauthorized use of brand in low-visibility digital contexts

**Action**: Document, investigate, file takedowns or oppositions. Standard enforcement
workflow. Test purchase if marketplace listing to confirm before action.

---

**LOW — Monitor and Assess (30–90 days)**

Low-risk infringement or potential infringement requiring monitoring but not immediate action.

**Examples:**

- Dormant domains with brand name registered but no active use
- Social media accounts with near-zero engagement and brand element use
- Trademark applications in non-competing classes in non-key markets
- Authorized resellers slightly deviating from brand guidelines

**Action**: Log. Monitor for escalation. No immediate enforcement unless escalation occurs.

---

**MONITOR — Watch List (Ongoing)**

Borderline situations where the line between infringement and legitimate use is unclear.
Requires monitoring to determine whether enforcement action is warranted.

**Examples:**

- Parody, commentary, or criticism accounts using brand elements
- Resellers using brand name in descriptive/nominative fair use contexts
- Fan accounts with authentic product photography
- Potentially infringing trademark applications by non-competitors in adjacent classes

**Action**: Document. Monitor actively. Consult trademark counsel before acting on
borderline cases — enforcement against legitimate fair use or parody can result in
negative publicity and § 1125(d) / misuse liability.

---

### Step 7: Develop the Enforcement Action Plan

For each threat identified, generate an actionable enforcement plan using this format:

```
**Threat ID**: [T-001, T-002, etc.]
**Description**: [Brief description of the specific infringement]
**Platform/Channel**: [Where the infringement is occurring]
**Severity**: [CRITICAL / HIGH / MEDIUM / LOW / MONITOR]
**Evidence Status**: [Collected / In Progress / Insufficient — requires test purchase]
**Recommended Action**: [Specific enforcement mechanism]
**Action Owner**: [In-house team / External counsel / Brand protection platform / Law enforcement]
**Timeline**: [Specific deadline for first action]
**Estimated Resolution Time**: [Typical timeline for this mechanism]
**Escalation Path**: [If initial action fails or is rejected]
**Success Metric**: [How to measure resolution: takedown confirmed / domain transferred / etc.]
```

**Escalation ladder for persistent infringement:**

```
Level 1: Platform takedown / UDRP / AFA request
    ↓ (if rejected or relisted within 30 days)
Level 2: Cease and desist letter / Legal demand
    ↓ (if no response or continued infringement)
Level 3: Civil litigation (injunction, damages, ACPA, trademark infringement)
    ↓ (if organized network or consumer safety risk)
Level 4: Criminal referral (DOJ/ICE-HSI/FDA + relevant international agencies)
```

### Step 8: Generate Program Documentation

Based on the assessment and enforcement plan, produce the following deliverables as requested:

**8a. Program Gap Register** (for audits): List of identified gaps with severity classification,
remediation actions, responsible party, and timeline.

**8b. Takedown SOP**: Step-by-step procedure for each enforcement channel with:

- Evidence collection checklist for that channel
- Submission instructions (portal, required fields, documentation format)
- Timeline expectations
- What to do if rejected
- Relisting protocol

**8c. Enforcement Priority Matrix**: Visual priority map organizing all active threats by
severity and urgency.

**8d. Budget and Resource Recommendation**: Tiered recommendations based on brand size and
threat volume:

| Tier                     | Annual Spend Range | Infrastructure                                                                                                                                        |
| ------------------------ | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tier 1 (Emerging)**    | $10K-$50K          | Manual monitoring, platform self-enrollment, limited takedowns                                                                                        |
| **Tier 2 (Established)** | $50K-$250K         | Brand protection platform subscription, dedicated in-house coordinator, periodic external counsel                                                     |
| **Tier 3 (Enterprise)**  | $250K+             | Enterprise platform, dedicated brand protection team, full-time external counsel, customs recordation all jurisdictions, criminal referral capability |

**⟁ CLARIFY** — Ask the user which deliverables they need before generating them to
avoid producing unrequested documentation.

### Step 9: Multi-Jurisdictional Strategy

For brands operating internationally, build an enforcement strategy matrix:

**Priority market tiers:**

| Tier                              | Markets                                              | Strategy Focus                                                                                     |
| --------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Tier 1: Core markets**          | US, EU, UK, Canada, Australia                        | Full program: monitoring + all enforcement channels + customs recordation                          |
| **Tier 2: Active growth markets** | Brazil, India, Mexico, Singapore, Japan, South Korea | Trademark registration first, customs recordation, platform enforcement                            |
| **Tier 3: Problem markets**       | China, Türkiye, Vietnam, Indonesia                   | Dedicated strategy: CNIPA registration, GACC customs, local enforcement firm, Alibaba IPP priority |
| **Tier 4: Monitor markets**       | Remaining jurisdictions                              | Trademark registration in key classes, passive monitoring                                          |

**2025 USTR Priority Watch List** (markets requiring intensified attention): [VERIFY against current USTR Special 301 Report]
China, India, Argentina, Chile, Indonesia, Mexico, Russia, Venezuela

**China-specific brand protection program:**

- Register with CNIPA directly (do not rely on Madrid Protocol alone)
- Record with GACC Customs Protection for border enforcement
- Enroll on Alibaba IPP Platform, JD.com, Pinduoduo IP platforms
- Engage a China-based IP enforcement firm for local administrative actions
- Monitor 1688.com (domestic wholesale B2B platform — major source of counterfeits)
- Consider criminal referral to Public Security Bureau for large-scale organized counterfeiting;
  note 2025 PSB procedural changes affecting case filing thresholds [VERIFY]

**⟁ CLARIFY** — For brands with significant China exposure, ask whether to:

- Develop a standalone China brand protection strategy section
- Recommend external counsel specializing in China IP enforcement
- Prioritize Alibaba IPP enrollment vs. CNIPA administrative enforcement vs. criminal referral

### Step 10: Quality Verification

Before delivering the program assessment or enforcement plan, apply the quality framework:

1. Run the 5 Citation Quality Gates silently. Revise failures before delivery.
2. For every CRITICAL classification, run the 3-pass Self-Interrogation.
3. Assign a Confidence Score to each major legal claim.
4. Verify all 8 program domains have been addressed.
5. Generate the Glass Box Audit Trail and append it to the output.

---

## Enforcement Priority Framework

### Tier 1 — Immediate Response (0-72 hours)

Issues requiring immediate action to prevent ongoing or escalating harm:

- Consumer health/safety threat from counterfeit products
- Active phishing or fraud domain using brand identity
- Organized counterfeiting network at scale
- Trademark opposition deadline imminent

### Tier 2 — Priority Enforcement (1-2 weeks)

Issues requiring prompt response to prevent brand dilution or revenue harm:

- High-volume marketplace counterfeits
- Verified social media impersonator accounts
- Active cybersquatting domain with traffic diversion
- UDRP filing deadline approaching (generally: as soon as identified, no statutory deadline)

### Tier 3 — Standard Enforcement (2-4 weeks)

Issues requiring systematic response but not urgent:

- Individual marketplace listings (moderate volume)
- Low-follower social media brand misuse
- Uncontested trademark applications (follow opposition deadlines)
- Defensive domain registration gaps

### Tier 4 — Program Maintenance (Ongoing)

Ongoing program health activities:

- Watch alert triage and response
- CBP/EU AFA renewals before expiration
- Platform enrollment renewals
- Enforcement metrics reporting and program calibration

---

## Redline/Recommendation Format

For each program gap or enforcement action:

```
**Finding ID**: [F-001, F-002, etc.]
**Domain**: [Trademark Portfolio / Domain / Social Media / Marketplace / Investigation / Customs / Criminal / Authentication]
**Finding**: [Description of the gap or threat]
**Severity**: [CRITICAL / HIGH / MEDIUM / LOW / MONITOR]
**Current State**: [What is in place today, if auditing]
**Recommended Action**: [Specific action to take]
**Priority**: [Tier 1 / Tier 2 / Tier 3 / Tier 4]
**Resource Required**: [In-house / External counsel / Brand protection platform / Law enforcement]
**Legal Basis**: [Statute, regulation, platform policy, or principle — mark [VERIFY] if from memory]
**Confidence**: [Definite / High / Probable / Possible / Unlikely]
**Fallback**: [Alternative if primary action fails or is unavailable]
```

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before delivering.

| Gate           | Rule                                                                                                            | Fail Action                                                              |
| -------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Source**     | Every legal claim cites a specific statute, regulation, platform policy, or established principle               | Add citation or mark "[UNVERIFIED — counsel to confirm]"                 |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction                                     | Fix format                                                               |
| **Currency**   | Platform policies and program details verified for current applicability (platforms change policies frequently) | Flag "[CHECK CURRENCY — platform policies change; verify before filing]" |
| **Domain**     | Analysis stays within the trademark/IP domain. No assumptions from unrelated legal areas                        | Remove or flag domain bleed                                              |
| **Confidence** | Uncertainty explicitly stated, not hidden — especially for jurisdictions outside primary research               | Add confidence qualifier                                                 |

### Self-Interrogation for CRITICAL Items

For any threat classified as CRITICAL, apply this 3-pass review before delivering:

**Pass 1 — Classification Integrity**: Does the evidence actually support a CRITICAL
classification? Is consumer safety genuinely at risk, or is this a HIGH threat that has
been over-classified? Would a trademark counsel and a brand protection investigator
independently reach the same classification?

**Pass 2 — Completeness**: Have all available enforcement mechanisms been considered?
For CRITICAL threats: has criminal referral been evaluated? Has emergency injunction
been evaluated? Has customs detention been activated? Is there a coordinated multi-channel
response?

**Pass 3 — Challenge**: What is the strongest argument that this threat is actually lower
severity? Are there legitimate defenses available to the alleged infringer (fair use, prior
rights, descriptive use)? Could enforcement action create risk (§ 1125(d) misuse liability,
negative PR from aggressive enforcement against a legitimate fair use)?

If any pass reveals a weakness, revise the classification and analysis before delivery.

### Confidence Scoring

| Level        | Range     | Meaning                                                              | Action                                                |
| ------------ | --------- | -------------------------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, clear statute, confirmed platform policy                | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong authority, minor questions on application to specific facts   | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments but platform policies or jurisdictions vary           | State with reasoning and contra-indicators            |
| **Possible** | 0.40–0.59 | Genuinely uncertain — platform policy unclear, jurisdiction varies   | Flag for counsel review with both sides               |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative, or jurisdiction lacks clear legal framework | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every brand protection program assessment MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-brand-protection-program"
  mode: "[Program Build / Program Audit / Threat Response / SOP Development / Channel-Specific]"
  brand: "[Brand name or 'Not disclosed']"
  industry: "[Consumer goods / Pharma / Luxury / Tech / Other]"
  primary_jurisdictions: "[List]"
  program_domains_assessed: "[number — max 8]"
  total_threats_identified: "[number]"
  threats_by_severity:
    critical: "[number]"
    high: "[number]"
    medium: "[number]"
    low: "[number]"
    monitor: "[number]"
  legalcode_mcp: "Connected / Not connected"
  enforcement_channels_covered: "[Trademark monitoring / Domain / Social media / Marketplace / Customs / Criminal / Authentication]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  platforms_checked:
    - "[Platform 1 — policy current as of YYYY-MM-DD or NOT VERIFIED]"
    - "[Platform 2 — ...]"
  china_coverage: "Full strategy / Basic / Not covered"
  limitations:
    - "[Any scope limitations, jurisdictions not covered, evidence not yet collected]"
  reviewer: "AI-assisted — requires qualified trademark/IP counsel review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in brand protection program management:

1. **Registering trademarks after entering a market** — In first-to-file jurisdictions
   (China, Brazil, many others), trademark rights go to the first to register, not the
   first to use. Not registering before entering a market can forfeit rights to a squatter
   or competitor. Register defensively in problem markets (especially China) even before
   commercial entry.

2. **Relying on UDRP for every domain dispute** — UDRP is the right tool for cybersquatting
   but not for all domain conflicts. Disputes with former business partners, licensees, or
   registrants with arguable legitimate interests are unlikely to succeed under UDRP (bad
   faith is hard to prove). Consider negotiated transfer, ACPA litigation, or trademark
   litigation for these cases.

3. **Filing UDRP without meeting all three elements** — A UDRP complaint that lacks clear
   bad faith evidence will fail and may foreclose re-filing on the same domain. Do not file
   until all three elements (confusing similarity, no legitimate interest, bad faith) can be
   established with documented evidence.

4. **Ignoring the URS option for new gTLD squatting** — For blatant cybersquatting in new
   gTLDs (.app, .io, .xyz, etc.), URS is faster (~3 weeks) and cheaper (~$375) than UDRP.
   Brand protection programs often overlook URS despite its utility for urgent relief.

5. **Sending DMCA/takedown notices for trademark (not copyright) issues** — DMCA is for
   copyright infringement. Sending a DMCA notice for trademark infringement misidentifies
   the IP right and may cause platforms to reject the notice, delay response, or create
   § 512(f) misrepresentation risk. Use the correct platform portal for trademark reports.

6. **Amazon takedowns without Brand Registry enrollment** — Amazon's enforcement tools
   (Project Zero, Report a Violation, Transparency) require Brand Registry enrollment.
   Attempting platform enforcement without enrollment first wastes time. Enroll in Brand
   Registry as the mandatory first step.

7. **Over-filing Amazon Project Zero without accuracy controls** — Amazon requires 99%+
   accuracy on Project Zero removals. Removing listings without confirming infringement
   (via test purchase or strong visual comparison) risks program suspension. Quality-check
   every removal before clicking "Protect."

8. **Neglecting relisting monitoring** — Filing a takedown and declaring victory without
   monitoring for relisting is a systemic program failure. Counterfeiters routinely relist
   under new seller accounts. Effective programs track relist rates and escalate to the
   enforcement ladder when relist rates are high.

9. **Treating gray market goods as counterfeits** — Gray market (parallel import) goods are
   genuine goods unauthorized for a particular territory. They are not counterfeit. Filing
   counterfeit claims against gray market goods with platforms or customs can constitute
   false claims and expose the brand owner to liability. Identify the correct legal theory
   (breach of distribution agreement, material differences doctrine) before taking action.

10. **Criminal referrals without sufficient evidence or relationship** — Law enforcement will
    not pursue trademark counterfeiting cases without: (a) evidence of commercial scale,
    (b) identifiable targets, (c) clear jurisdiction, and (d) a credible brand owner as
    complainant with documentation ready. Premature referrals without these elements waste
    enforcement resources and damage the brand's relationship with law enforcement.

11. **Ignoring the CBP customs recordation renewal calendar** — CBP trademark recordations
    expire and must be renewed. An expired recordation means CBP has no obligation to detain
    infringing goods at the border. Build renewal tracking into the trademark docketing
    system. The same applies to EU AFA (1-year validity, renewable).

12. **Conflating UDRP providers** — ICANN-approved UDRP providers (WIPO, NAF/Forum, ADNDRC)
    have different panelist pools, procedural nuances, and statistical outcomes. The choice
    of UDRP provider can affect outcomes, particularly in close cases. Consult with domain
    dispute counsel before selecting the provider.

13. **Running test purchases from brand accounts** — Test purchases from email addresses or
    payment methods associated with the brand alert sophisticated counterfeiters, who may
    ship authentic goods to that address while continuing to ship counterfeits to real
    consumers. Use anonymous accounts and unconnected payment methods.

14. **Enforcing against legitimate fan accounts or parody** — Enforcement against genuine
    fan accounts, parody accounts, or clear commentary can generate significant negative
    publicity ("the brand attacked its own fans") and potentially constitute trademark misuse
    or tortious interference. Establish clear screening criteria distinguishing unauthorized
    commercial impersonation from non-commercial fan expression before enforcement.

15. **No enforcement metrics or program review** — Running a brand protection program without
    tracking metrics (takedowns submitted, removed, rejected, relisted; UDRP success rate;
    marketplace counterfeit volume over time) makes it impossible to evaluate program
    effectiveness, justify budget, or identify which channels require more resources. Establish
    KPIs at program inception.

16. **Assuming platform takedowns resolve recurring sellers** — Platforms allow sellers to
    create new accounts after removal. A prolific counterfeiter removed from Amazon will often
    return under a new seller identity within days. Effective programs track seller
    fingerprints (product photos, listing copy patterns, pricing, shipping origin) to identify
    recidivists and escalate to platform Trust & Safety or law enforcement.

17. **No coordinated multi-channel response to organized networks** — Large-scale counterfeit
    operations exist simultaneously on multiple channels (Alibaba for wholesale, Amazon for
    retail, social media for marketing, a domain for order processing). Treating each channel
    separately instead of coordinating simultaneous takedowns allows the network to shift
    volume to surviving channels.

18. **Delegating brand protection entirely to an automated platform without human review** —
    AI-driven brand protection platforms can generate high volumes of false positives,
    particularly when matching brand terms in legitimate reseller listings, review sites, or
    news articles. Fully automated takedowns without human review can create legal liability
    and damage legitimate commercial relationships.

19. **Not maintaining product authentication samples with CBP and key customs authorities** —
    Customs officers need reference materials to identify counterfeits at the border. Providing
    CBP and key national customs authorities with authentic product samples, brand guidelines,
    and distinctive feature descriptions dramatically improves seizure effectiveness.

20. **Failure to educate internal stakeholders** — Brand protection programs frequently fail
    because internal business units don't know how to report suspected infringement, what
    constitutes authorized vs. unauthorized use, or how to preserve evidence. Internal
    education and a clear reporting channel are essential program infrastructure.

---

## Writing Standards

Apply plain-language discipline to all output:

**For enforcement recommendations and SOP documentation:**

- Active voice: "File the UDRP complaint with WIPO" not "A UDRP complaint should be filed"
- Imperative form for procedural steps: "Screenshot the listing" not "The listing should be screenshotted"
- Specific over general: "File within 30 days of discovery" not "File promptly"
- Name the actor: "Brand protection counsel files the complaint" not "The complaint is filed"
- One action per sentence in SOPs

**For legal analysis sections:**

- Cite the authority: "Under 15 U.S.C. § 1125(d)(1)(A)(i), ACPA requires..." not "Under law..."
- Flag uncertainty explicitly: "[VERIFY]" or "Confidence: Probable (0.65)"
- Distinguish analysis from conclusion: "The evidence suggests..." not "This is..."
- No legalese when plain language serves: "registered trademark" not "mark registered pursuant to"

**Quality gates before delivery:**

- [ ] Every actionable recommendation has a named actor, a specific action, and a deadline
- [ ] Every legal reference is either verified or marked [VERIFY]
- [ ] No jurisdiction-specific concepts stated as universal
- [ ] Every CRITICAL finding has passed the 3-pass Self-Interrogation
- [ ] Glass Box audit trail is complete

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for current trademark enforcement statutes and remedies in each jurisdiction in scope
- Verify current platform IP program policies and enrollment requirements
- Research recent significant enforcement decisions or regulatory changes
- Verify CBP/EU AFA fee schedules and procedural requirements
- Research ccTLD dispute resolution policies for each country-code domain in issue
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with the general multi-jurisdictional frameworks and platform guidance above
- Mark all statutory and procedural references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Recommend that brand protection counsel verify all legal references and current platform
  policies before acting on any recommendation

**Brand protection platform integration:**
This skill generates program strategy and enforcement plans. For execution at scale, it
should be paired with:

- A brand monitoring platform (Corsearch, MarkMonitor, Red Points, BrandShield)
- A trademark management system for docketing renewals and oppositions
- A case management system for tracking enforcement actions and outcomes

If a brand protection platform is connected via MCP or integration:

- Pull current monitoring alerts for triage and classification
- Log enforcement actions and outcomes
- Track enforcement metrics and generate program reports

---

## Output Format Template

Structure every brand protection program deliverable as follows:

---

# Brand Protection Program [Assessment / Audit / Threat Response]

**Brand**: [Brand name]
**Date**: [Date of assessment]
**Scope**: [Jurisdictions, channels, and threat categories in scope]
**Prepared by**: AI-assisted analysis — requires qualified trademark/IP counsel review

> **Not legal advice**. All recommendations require verification and review by qualified
> trademark counsel before implementation. Platform policies change frequently; verify
> current procedures before filing.

---

## Executive Summary

[3-5 sentences summarizing: (1) overall program maturity or threat severity, (2) the 2-3
most critical findings requiring immediate action, (3) recommended priority actions.]

---

## Program Assessment by Domain

| Domain                       | Status       | Critical Gaps | Priority Actions  |
| ---------------------------- | ------------ | ------------- | ----------------- |
| 1. Trademark Portfolio       | 🔴 / 🟡 / 🟢 | [Gap summary] | [Priority action] |
| 2. Domain Enforcement        | 🔴 / 🟡 / 🟢 | ...           | ...               |
| 3. Social Media              | 🔴 / 🟡 / 🟢 | ...           | ...               |
| 4. Marketplace Takedowns     | 🔴 / 🟡 / 🟢 | ...           | ...               |
| 5. Counterfeit Investigation | 🔴 / 🟡 / 🟢 | ...           | ...               |
| 6. Customs Recordation       | 🔴 / 🟡 / 🟢 | ...           | ...               |
| 7. Criminal Referral         | 🔴 / 🟡 / 🟢 | ...           | ...               |
| 8. Product Authentication    | 🔴 / 🟡 / 🟢 | ...           | ...               |

---

## Findings Register

| ID    | Domain   | Finding       | Severity                 | Priority     | Recommended Action |
| ----- | -------- | ------------- | ------------------------ | ------------ | ------------------ |
| F-001 | [Domain] | [Description] | CRITICAL/HIGH/MEDIUM/LOW | Tier 1/2/3/4 | [Action]           |
| F-002 | ...      | ...           | ...                      | ...          | ...                |

---

## Detailed Findings

### [Finding ID]: [Finding Title]

**Severity**: [CRITICAL / HIGH / MEDIUM / LOW / MONITOR]
**Domain**: [Enforcement domain]
**Finding**: [Detailed description of the gap or threat]
**Legal basis**: [Applicable statute, regulation, or principle] [VERIFY if needed]
**Recommended action**: [Specific steps to take]
**Priority**: [Tier 1 / 2 / 3 / 4]
**Timeline**: [When first action should occur]
**Resource required**: [In-house / External counsel / Brand protection platform / Law enforcement]
**Escalation path**: [If initial action is rejected or fails]
**Confidence**: [Definite / High / Probable / Possible / Unlikely — score]

---

## Enforcement Action Plan

[Table of active threats with: Threat ID, Description, Platform/Channel, Severity, Evidence
Status, Recommended Action, Owner, Timeline, Escalation Path]

---

## Program Roadmap

### Immediate (0-30 days)

- [Action 1: specific, owner, deadline]
- [Action 2: ...]

### Short-term (30-90 days)

- [Action 1: ...]

### Long-term (90+ days / Ongoing)

- [Action 1: ...]

---

## Resource and Budget Recommendation

[Tiered recommendation based on brand tier and threat volume]

---

## Localization Notes

[Any jurisdiction-specific requirements not addressed in the general framework above]

---

## Glass Box Audit Trail

```yaml
[Complete Glass Box YAML as defined in the Quality Assurance Framework]
```

---

## Localization Notes

When localizing this skill for specific jurisdictions, adapt:

- **Customs recordation**: Each jurisdiction has a separate system (US CBP IPRS, EU AFA,
  China GACC, India CBIC, UK HMRC). Replace [JURISDICTION-SPECIFIC] markers with the
  specific filing portal, fees, and procedural requirements.
- **Criminal referral thresholds**: Vary significantly. In the US, commercial-scale
  counterfeiting under 18 U.S.C. § 2320 is the standard. In the EU, Directive 2004/48/EC
  governs civil enforcement; criminal enforcement is governed by national laws that vary
  across Member States. In China, the criminal threshold is ¥50,000 in counterfeit goods
  sales value or 2+ criminal convictions [VERIFY current thresholds].
- **Platform availability**: Not all platforms operate in all jurisdictions. Temu and
  Shein's IP enforcement programs are evolving; verify current programs before relying
  on them in enforcement plans.
- **UDRP vs. local dispute resolution**: UDRP applies to gTLDs (.com, .net, .org, new
  gTLDs). ccTLDs use national policies. .uk → Nominet DRS; .de → DENIC Policy;
  .eu → EURid ADR; .cn → CNDRP (CNNIC). Research the applicable policy for each ccTLD.
- **Parallel imports / gray market**: Legal treatment varies dramatically. EU has regional
  exhaustion (gray market goods lawfully sold in EU can be resold across EU; goods from
  outside EU can be restricted). US has national exhaustion with a "material differences"
  exception. Research the applicable exhaustion doctrine before characterizing gray market
  goods as infringing.

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis based on multi-agent research
pipeline covering: Lanham Act (15 U.S.C. §§ 1051 et seq.), ACPA (15 U.S.C. § 1125(d)),
Trademark Counterfeiting Act (18 U.S.C. § 2320), EU Trade Mark Regulation 2017/1001,
EU Customs Regulation 608/2013, TRIPS Agreement Arts. 16–17, ICANN UDRP Policy and
Rules (2024), WIPO UDRP Guide, CBP IPRS e-Recordation System, EUIPO eAFA system
(mandatory electronic filing October 2024), Amazon Brand Registry + Project Zero +
Transparency Program (including 2025 Transparency Interoperability feature and 10-country
expansion), eBay VeRO Program, Alibaba/AliExpress IPP Platform, USTR 2025 Special 301
Report (Priority Watch List), USTR 2025 Notorious Markets List, Corsearch/TrademarkNow
platform capabilities, CompuMark/SAEGIS coverage data, Red Points/BrandShield platform
positioning, product authentication technology comparison (holograms/QR/NFC/serialization),
test purchase chain of custody methodology, and China 2025 Anti-Unfair Competition Law
amendments. Reference standard: legalcode-contract-review (Gold standard skill).
