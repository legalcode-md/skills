---
name: legalcode-ai-training-data-copyright
description: Analyze copyright implications of AI training data. Use when evaluating whether scraped or
  licensed content can be used to train AI/ML models, assessing legal exposure from bulk data acquisition,
  reviewing TDM (text and data mining) rights under EU DSM Directive Articles 3 and 4, analyzing US fair
  use defenses for model training, checking compliance with EU AI Act Article 53 training data transparency
  obligations, assessing opt-out mechanisms (robots.txt, TDM reservations), reviewing Creative Commons
  and data license compatibility with AI training, evaluating right of publicity risks in training datasets,
  analyzing DMCA Section 1202 copyright management information claims, or preparing a litigation risk
  assessment for an AI training dataset.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Analyze copyright implications of AI training data. Use when evaluating whether scraped or licensed content can be used to train AI/ML models, assessing legal exposure from bulk data acquisition, reviewing TDM (text and data mining) rights under EU DSM Directive Articles 3 and 4, analyzing US fair use defenses for model training, checking compliance with EU AI Act Article 53 training data transparency obligations, assessing opt-out mechanisms (robots.txt, TDM reservations), reviewing Creative Commons and data license compatibility with AI training, evaluating right of publicity risks in training datasets, analyzing DMCA Section 1202 copyright management information claims, or preparing a litigation risk assessment for an AI training dataset. Covers the NYT v. OpenAI and Getty Images v. Stability AI litigation landscape, EU AI Act GPAI provider obligations, US fair use four-factor analysis for training, web scraping legality under the CFAA and ToS law, and training data licensing strategies. Jurisdictions: United States and European Union, with coverage of cross-border scenarios.


# Legalcode AI Training Data Copyright

> **Disclaimer**: This skill provides a framework for AI-assisted legal analysis of
> copyright issues in AI training data. It does not constitute legal advice. All outputs
> must be reviewed by a qualified IP lawyer licensed in the relevant jurisdiction before
> use. This is a rapidly evolving area — cases cited may have been reversed, settled, or
> superseded; statutes may have been amended; verify all citations against authoritative
> sources. Statutory and case law references from memory carry hallucination risk —
> mark unverified references [VERIFY] and treat outputs as preliminary analysis only.

---

## Purpose and Scope

This skill analyzes the copyright, contractual, and regulatory implications of using
content to train AI and machine learning models. It produces a classified risk assessment
with actionable recommendations for AI developers, model operators, data teams, and
legal counsel.

**Covers:**

- US fair use four-factor analysis for AI training data (17 USC § 107)
- EU DSM Directive TDM exceptions (Articles 3 and 4 of Directive 2019/790/EU)
- EU AI Act GPAI provider transparency obligations (Article 53, Regulation (EU) 2024/1689)
- Web scraping legality under the CFAA and Terms of Service law
- robots.txt and machine-readable TDM reservation mechanisms
- Creative Commons license analysis for training data compatibility
- Right of publicity risks in training datasets (US state law)
- DMCA Section 1202 copyright management information (CMI) claims
- Key litigation landscape (NYT v. OpenAI; Getty Images v. Stability AI; Andersen v.
  Stability AI; Raw Story Media v. OpenAI; Kadrey v. Meta) [VERIFY current status]
- Training data licensing strategies and best practices
- Memorization/regurgitation risk in model outputs

**Does not:**

- Draft data licensing agreements (see `legalcode-technology-license-agreement`)
- Assess database sui generis rights in isolation (addressed where relevant)
- Handle patent or trademark issues for AI (see `legalcode-patent-landscape-analysis`)
- Provide legal advice or replace qualified IP counsel

---

## Jurisdiction and Governing Law

This skill provides primary coverage across two jurisdictions:

| Jurisdiction       | Primary Framework                                                                                                                 | Key Standard                                                                                                              |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **United States**  | Copyright Act 1976 (17 USC §§ 101–1332); CFAA (18 USC § 1030); DMCA (17 USC §§ 512, 1201–1205)                                    | Fair use four-factor test (17 USC § 107); Feist originality; AWF v. Goldsmith (2023) transformative use standard [VERIFY] |
| **European Union** | DSM Directive 2019/790/EU (Arts. 3–4); EU AI Act 2024/1689/EU (Art. 53); InfoSoc Directive 2001/29/EC; Database Directive 96/9/EC | TDM exception with opt-out; GPAI transparency obligations; "own intellectual creation" (Infopaq [VERIFY])                 |

**Cross-border scenarios**: When scraping occurs in one jurisdiction but training in
another, or when content originates from multiple jurisdictions, the analysis must address
each applicable regime. Generally, the law of the country where the allegedly infringing
act occurs governs (lex loci protectionis). [VERIFY for specific scenarios]

[JURISDICTION-SPECIFIC] For jurisdictions outside US/EU, research:

- Whether a fair use (US-style, open-ended) or fair dealing (UK/Canadian-style,
  enumerated) system applies, or whether a TDM exception exists
- Japan has a broad TDM exception (Article 30-4 of the Japanese Copyright Act [VERIFY])
- UK: post-Brexit, UK copyright law includes a non-commercial research/text mining
  exception (CDPA 1988 s. 29A [VERIFY]) but no general commercial TDM exception
- Singapore, Israel, South Korea: varying TDM exceptions [VERIFY]
- Berne Convention membership: determines baseline protection requirements [VERIFY]

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the risk classification
- Multiple legal analyses apply and the user's facts determine which governs
- Commercial vs. non-commercial use affects TDM exception eligibility
- Opt-out compliance status requires facts the user must supply

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

### Step 1: Accept the Materials

Accept materials in any of these formats:

- **Dataset description**: Written description of the data sources, acquisition method,
  content types, and scale
- **Dataset documentation**: Existing data cards, model cards, or dataset documentation
- **License files**: License texts for source datasets, robots.txt excerpts, ToS clauses
- **Contract text**: Data licensing agreements, API terms, or scraping agreements
- **Model card or training report**: Published documentation for an existing model

If no materials are provided, prompt the user to describe the training data in terms of:
source URLs or platform, acquisition method, content types, volume, and intended model.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the analysis, ask the user the following questions.
Present as structured options where possible:

1. **Role and objective**: What analysis is needed?
   - Options: **Pre-training clearance** (assess before building dataset), **Post-training
     risk assessment** (evaluate an existing dataset), **Litigation defense** (evaluate
     claims against us), **Litigation offense** (evaluate claims we may bring), **Policy
     compliance** (EU AI Act, GPAI obligations), **Licensing strategy** (find a compliant
     path)
   - _Why this matters_: Pre-clearance emphasizes avoiding risk; litigation defense
     emphasizes building arguments; policy compliance focuses on disclosure requirements.

2. **Commercial use**: Is the intended model commercial?
   - Options: **Commercial** (for-profit products or services), **Non-commercial/research**
     (academic, scientific research, non-profit), **Mixed** (research now, commercial later)
   - _Why this matters_: EU DSM Art. 4 TDM exception applies to commercial use subject
     to opt-out; Art. 3 exception applies to research organizations only. US fair use
     Factor 1 weighs commercial use negatively.

3. **Data sources**: How was the training data acquired?
   - Options: **Web scraping** (automated crawling of public websites), **Licensed
     datasets** (purchased or licensed from data providers), **Open datasets** (publicly
     released datasets such as Common Crawl, C4, The Pile), **API access** (content
     pulled through platforms' APIs), **Mixed sources**, **Unknown composition**
   - _Why this matters_: Each acquisition method raises different legal issues.

4. **Geographic scope**: Where does training occur and where will the model be deployed?
   - Options: **US only**, **EU only**, **US and EU**, **Global deployment**
   - _Why this matters_: EU AI Act GPAI obligations apply to models deployed in the EU
     regardless of where training occurs. TDM exception analysis is jurisdiction-specific.

5. **Opt-out awareness**: Are you aware of robots.txt exclusions or TDM reservations
   in your dataset sources?
   - Options: **Yes — we have records of opt-outs honored**, **Yes — we know some
     sources excluded our crawler**, **No — we did not systematically check opt-outs**,
     **Unknown — this is what we need to assess**
   - _Why this matters_: Under EU DSM Art. 4, failure to honor machine-readable opt-outs
     eliminates the TDM exception for commercial use. Non-compliance with opt-outs also
     strengthens willfulness arguments in litigation.

6. **Model output risk**: Does the trained model reproduce training content verbatim or
   near-verbatim (memorization)?
   - Options: **Known memorization identified** (e.g., via adversarial prompting),
     **Unknown — not tested**, **No known memorization**, **Generative model with
     extraction capability**
   - _Why this matters_: Memorization converts a potential training input fair use
     defense into a direct copying claim, as argued in NYT v. OpenAI. [VERIFY]

If partial context is provided, proceed with stated assumptions and flag them explicitly.

### Step 3: Gather Jurisdiction-Relevant Legal Authority

Identify the applicable jurisdictions from context. Use **legalcode-mcp** to gather
current legal authority.

**Research process:**

1. **Search legalcode-mcp** for:
   - Current text of 17 USC § 107 (fair use) and recent cases interpreting it for AI
   - EU DSM Directive 2019/790 Arts. 3 and 4 as implemented in relevant member states
   - EU AI Act Art. 53 and implementing guidance from the EU AI Office
   - CFAA (18 USC § 1030) and recent circuit court decisions on scraping
   - DMCA § 1202 recent case law (CMI removal in AI context)
   - Key AI training copyright cases: NYT v. OpenAI, Getty Images v. Stability AI,
     Andersen v. Stability AI, Raw Story Media v. OpenAI, Kadrey v. Meta

2. **Save results** to `/tmp/legalcode-ai-training-copyright-authority.md`:

   ```markdown
   # Legal Authority Reference — AI Training Data Copyright

   ## Date: [date]

   ## Jurisdictions: [US / EU / cross-border]

   ### US Copyright Framework

   - [17 USC § 107, current text; key fair use cases for AI]

   ### EU TDM Framework

   - [DSM Directive Arts. 3–4; implementation status; opt-out mechanism standards]

   ### EU AI Act

   - [Art. 53; GPAI transparency requirements; enforcement status]

   ### Key Litigation

   - [Each case, court, current status, key rulings]

   ### CFAA / Scraping Law

   - [hiQ v. LinkedIn; Van Buren; current circuit split status]

   ### Recent Developments

   - [Legislative developments, regulatory guidance, 2024–2026]
   ```

3. **Use the reference file throughout** the analysis. Mark legalcode-mcp-sourced
   citations as VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Proceed with structural risk assessment; flag that legal citations require independent
  verification before relying on them

### Step 4: Characterize the Training Data

Systematically characterize the training data before applying the legal framework.
This step determines which legal analyses apply.

**⟁ CLARIFY** — If the dataset composition is unclear:
"To complete the legal analysis, I need to characterize the training data. Can you
provide: (a) the primary content types (text, images, code, audio, video, data), (b)
the primary sources (news, books, social media, academic papers, proprietary content),
(c) approximate scale (tokens, items, GB/TB), and (d) any known opt-outs or license
constraints flagged in the dataset?"

Build a **Data Characterization Table**:

| Data Category     | Sources                     | Estimated Volume | Known Licenses/Restrictions | Acquisition Method      |
| ----------------- | --------------------------- | ---------------- | --------------------------- | ----------------------- |
| [Text / literary] | [e.g., news sites, books]   | [X tokens / GB]  | [None / CC-BY / Paywalled]  | [Scraped / Licensed]    |
| [Code]            | [e.g., GitHub, GitLab]      | [X tokens]       | [Various OSS licenses]      | [API / Scraped]         |
| [Images]          | [e.g., Getty, Flickr]       | [X images]       | [Watermarked / CC / Getty]  | [Licensed / Scraped]    |
| [Audio/video]     | [e.g., YouTube, podcasts]   | [X hours]        | [CC / ToS restricted]       | [Downloaded / Licensed] |
| [Structured data] | [e.g., Wikipedia, Wikidata] | [X records]      | [CC-BY-SA / ODC]            | [Dump / API]            |

Flag **high-risk data categories** immediately:

- **Paywalled / subscription content**: Strong claim of unauthorized access (NYT-type
  claims)
- **Opt-out markers present**: robots.txt, Robots Exclusion Standard, C2PA metadata
- **Watermarked images**: DMCA § 1202 CMI claim risk (Getty-type claim)
- **Human faces / biometrics**: Right of publicity; state biometric privacy law (BIPA,
  Texas CUBI) [VERIFY]
- **Personal data**: GDPR / CCPA analysis required (outside scope of this skill —
  refer to data protection counsel)

### Step 5: Assess Scraping and Acquisition Legality

**⟁ CLARIFY** — If web scraping was used:
"Was the scraping done via automated crawlers? Were robots.txt files checked and
honored? Were Terms of Service reviewed before scraping? Was any data behind a login,
paywall, or other access control?"

Analyze the acquisition method against three legal theories:

#### 5a. Copyright in the Scraped Content

Apply the US/EU copyright analysis from Step 6 to the **act of scraping** (reproducing
content onto storage media to create a training dataset is itself a reproduction).

Assess: Is the reproduction temporary and transient (not a basis for infringement
under 17 USC § 512 / InfoSoc Art. 5(1) [VERIFY])? Or is it a persistent reproduction
that requires a license or fair use justification?

#### 5b. Computer Fraud and Abuse Act (US)

Assess CFAA exposure (18 USC § 1030): [VERIFY all]

- **Van Buren v. US (2021)**: SCOTUS narrowed CFAA — "exceeds authorized access" means
  accessing data one is not entitled to access, not just misusing authorized access.
  Scraping publicly accessible pages by people with general public access is generally
  outside CFAA's scope per the Ninth Circuit's hiQ v. LinkedIn analysis. [VERIFY]
- **hiQ Labs v. LinkedIn (9th Cir. 2022)**: CFAA does not prohibit scraping publicly
  accessible data. Public data scraping does not constitute "unauthorized access" when
  the data is available without authentication. [VERIFY current status]
- **Key caveat**: CFAA risk arises if: scraping bypasses technical access controls
  (login walls, CAPTCHAs, IP rate limiting), a cease-and-desist was ignored, or data
  behind a paywall was scraped.

**Classification**: CLEAR (public data, no ToS restriction, no C&D) / CAUTION (ToS
prohibits scraping, no C&D) / RISK (bypassed access controls or received C&D).

#### 5c. Terms of Service Breach

Most major platforms (OpenAI, LinkedIn, Twitter/X, Reddit, The New York Times) prohibit
automated scraping in their ToS. Analyze:

- Was the platform's ToS reviewed before scraping?
- Does the ToS prohibit automated access, scraping, or commercial use of scraped data?
- Was a cease-and-desist received? Was scraping discontinued?

**Legal significance**: ToS violation is primarily a breach of contract claim, not
copyright infringement. However, ToS violations: (1) undermine the ToS-as-license
defense, (2) may support claims that access was "unauthorized" under the CFAA, (3)
support willfulness arguments in copyright claims. [VERIFY jurisdiction-specific treatment]

**Classification**: CLEAR (no ToS restriction) / CAUTION (ToS ambiguous or prohibits
scraping, but no enforcement) / RISK (ToS explicitly prohibits scraping, enforcement action).

### Step 6: Analyze Copyright Ownership and TDM Exceptions

This is the core analysis step. Apply the applicable legal framework(s) based on jurisdiction.

#### 6a. US Fair Use Analysis (17 USC § 107)

Apply all four factors. A fair use determination requires holistic balancing — no single
factor is determinative.

**⟁ CLARIFY** — If the use is borderline on Factor 4:
"Does the trained model compete in any market where the copyright owners are active or
would likely license their content? Are there active licensing programs for AI training
data from the copyright owners at issue?"

**Factor 1 — Purpose and Character of Use (most contested)**

| Sub-factor                                                    | Analysis                                                                                                                                                                                                                                                                                                                                                                        | Classification                        |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **Commercial vs. non-commercial**                             | Training a commercial AI product weighs against fair use; academic/research training weighs in favor                                                                                                                                                                                                                                                                            | Factor weight: negative if commercial |
| **Transformativeness (post-AWF v. Goldsmith, 2023 [VERIFY])** | Is the purpose of the use "different in kind" from the original purpose, or merely the same in different packaging? Text used to train a language model to generate text may be held non-transformative if outputs compete with the original; use for classification, indexing, or search may be more transformative (cf. Authors Guild v. Google Books, 2d Cir. 2015 [VERIFY]) | Factor weight: highly fact-specific   |
| **Good faith and opt-out honoring**                           | Ignoring robots.txt opt-outs or scraping past a C&D increases bad faith argument                                                                                                                                                                                                                                                                                                | Factor weight: negative if bad faith  |

**Factor 2 — Nature of the Copyrighted Work**

- Factual / informational content (news reports, databases, factual text): weighs in
  favor of fair use
- Highly creative works (fiction, poetry, visual art, music, film): weighs against
  fair use
- Published vs. unpublished: published works lean toward fair use

**Factor 3 — Amount and Substantiality Used**

- Ingesting entire works (books, full articles) into training data is the entire work —
  weighs against fair use
- Ingesting massive quantities of works (billion-token corpora) — each work used in full
- Note: Google Books scanned entire books but only displayed snippets — different fact
  pattern from AI training where the entire work shapes the model

**Factor 4 — Market Harm (most important per courts)**

- **Substitution test**: Does the AI model's output substitute for or compete with the
  market for the original work?
- **Memorization risk (NYT v. OpenAI theory)**: If the model can be prompted to reproduce
  substantial portions of the original verbatim, this creates a direct substitution market
  harm argument. [VERIFY current case status]
- **Licensing market**: Does a market exist (or would develop) for licensing content for
  AI training? Growing evidence of licensing programs (Getty/NVIDIA, AP/OpenAI,
  publishers) supports the argument that a cognizable market exists. [VERIFY]
- **Holistic assessment**: A generative AI that can reproduce entire articles on demand
  has a much more negative Factor 4 than a sentiment classifier.

**2025 Emerging Framework from Thomson Reuters / Bartz / Kadrey:**

Ask these threshold questions in sequence before applying the four-factor analysis:

1. **Source question**: Was the training data obtained from legitimate sources (licensed,
   purchased, open web with lawful access) or pirated/unauthorized sources? → Piracy
   severely undermines fair use even for transformative LLM training (per Bartz).

2. **Functional overlap question**: Does the AI system's output serve the **same market
   function** as the copyrighted works used to train it? → If yes, the use is unlikely
   transformative under AWF v. Goldsmith and Thomson Reuters v. Ross.

3. **Market harm question**: Can the copyright owners demonstrate concrete market harm
   (actual substitution, lost licensing revenue, undermined licensing market)? → Absence
   of proven market harm was decisive in Kadrey; presence of licensing market was
   decisive in Thomson Reuters.

**Overall US Fair Use Assessment table:**

| Factor                      | Weight in Precedent  | 2025 Guidance                                                                                                                                                        | Direction |
| --------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| 1. Purpose — commercial     | High                 | Commercial: negative; Research: positive                                                                                                                             | ⬆/⬇       |
| 1. Purpose — transformative | Highest post-AWF     | Same function as original → not transformative (Ross); different function (LLM language understanding vs. reading for entertainment) → transformative (Bartz/Kadrey) | ⬆/⬇       |
| 1. Source legality          | Now material (Bartz) | Pirated source → defeats fair use; licensed/purchased → preserves fair use analysis                                                                                  | ⬆/⬇       |
| 2. Nature of work           | Medium               | Factual: positive; Creative: negative                                                                                                                                | ⬆/⬇       |
| 3. Amount used              | Medium               | Entire works: negative; guardrails preventing output reproduction: somewhat positive (Copyright Office guidance)                                                     | ⬇         |
| 4. Market harm              | Highest              | Substitution or licensing market: negative; no proven market harm evidence: positive (but plaintiffs building licensing programs)                                    | ⬆/⬇       |

**Classification** (updated with 2025 case law):

- **GREEN**: Non-commercial research; factual content; no piracy; no functional overlap
  with output; no licensing market in the relevant content category
- **YELLOW**: Commercial use of primarily factual content; legitimately sourced; no
  verbatim memorization; licensing market uncertain or nascent
- **RED**: Commercial use of creative works; any pirated source content; functional
  overlap identified (output competes with original); memorization identified; active
  copyright holders with established licensing programs (publishers, news orgs)

#### 6b. EU TDM Exception Analysis (DSM Directive 2019/790/EU)

**Article 3 — Research Organization Exception (mandatory minimum)**

- Applies to: scientific research conducted by research organizations or cultural
  heritage institutions
- Requires: for scientific research purposes only; member-state implementation required
- Opt-out: **No opt-out permitted** — this exception cannot be contractually overridden
- Key limitation: "Research organization" defined narrowly — commercial entities that
  do research generally do not qualify; publicly funded research preferred [VERIFY
  specific member state implementation]

**Article 4 — General Commercial TDM Exception (subject to opt-out)**

- Applies to: any person (including commercial AI developers)
- Requires: lawful access to the content being mined
- Opt-out mechanism: Rights holders may **reserve** the right to exclude their content
  from TDM by means of a **machine-readable statement** (e.g., robots.txt, metadata)
- If opt-out is properly communicated: the Art. 4 exception does NOT apply → need
  license
- If no opt-out: the Art. 4 exception applies and no license is needed (for the mining
  itself, not for retaining a comprehensive copy)

**EU AI Act linkage (Art. 53, Regulation 2024/1689)** [VERIFY current implementation status]:

- General-Purpose AI (GPAI) providers must:
  - (d)(i): Comply with EU copyright law, including the opt-out provisions of DSM Art. 4
  - (d)(ii): Make publicly available a sufficiently detailed summary of training data
    (transparency obligation)
  - GPAI providers who rely on DSM Art. 4 must be able to demonstrate that opt-outs
    were checked and honored
- EU AI Office is developing guidance on the training data summary format [VERIFY]

**Opt-out check matrix:**

| Opt-out Mechanism                             | Legally Effective Under DSM Art. 4?                             | Notes                                                  |
| --------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------ |
| `robots.txt` with AI-specific rules           | Yes (if machine-readable) [VERIFY]                              | User-agent specific rules (e.g., `User-agent: GPTBot`) |
| `Robots Exclusion Standard` (RES) in metadata | Yes [VERIFY]                                                    | HTTP `X-Robots-Tag` header                             |
| C2PA rights assertion metadata                | Likely yes [VERIFY]                                             | Coalition for Content Provenance and Authenticity      |
| IPTC photo metadata with `Rights` field       | Likely yes [VERIFY]                                             | Embedded in image EXIF/IPTC                            |
| Contractual restriction only (ToS)            | Uncertain — arguably not "machine-readable" [VERIFY]            | ToS requires human review                              |
| Paywall / technical access control            | Creates "unlawful access" issue — Art. 4 requires lawful access | Scraping past paywall destroys the exception           |

**Classification**:

- **GREEN**: Lawful access; no machine-readable opt-out; Art. 4 exception applies
- **YELLOW**: Lawful access but opt-out check was not systematic; partial compliance
- **RED**: Unlawful access (bypassed controls); or machine-readable opt-outs were ignored

#### 6c. Interaction: Fair Use vs. TDM Exception

| Scenario                                          | US Analysis                                    | EU Analysis                                               |
| ------------------------------------------------- | ---------------------------------------------- | --------------------------------------------------------- |
| Commercial training, public web, opt-outs honored | Fair use uncertain (contested)                 | Art. 4 applies (clear if opt-outs honored)                |
| Commercial training, creative works, memorization | Fair use very weak (NYT-type risk)             | Art. 4 may apply to mining, but output liability separate |
| Non-commercial research                           | Fair use stronger                              | Art. 3 applies (if research org)                          |
| Paywalled content                                 | Fair use not available for unauthorized access | Art. 4 requires lawful access — cannot apply              |

### Step 7: Evaluate Opt-out and TDM Reservation Compliance

Systematically assess the opt-out compliance posture across the dataset sources.

**⟁ CLARIFY** — If opt-out records are incomplete:
"Do you have logs of your crawl/scraping runs showing which robots.txt files were
encountered and whether opt-out rules were honored? This is critical for your EU AI Act
Art. 53 compliance argument and your DSM Art. 4 defense."

**Opt-out Compliance Checklist:**

- [ ] Were robots.txt files fetched before scraping each domain?
- [ ] Were AI-specific user-agent rules (e.g., `GPTBot`, `ClaudeBot`, `CCBot`,
      `Google-Extended`) respected?
- [ ] Were HTTP `X-Robots-Tag` headers checked?
- [ ] Were C2PA or IPTC metadata fields checked for images?
- [ ] Is there a crawl log or record demonstrating opt-out compliance?
- [ ] Were ToS terms reviewed for scraping prohibitions before crawling?
- [ ] For licensed datasets: does the license explicitly permit AI training use?

**For EU AI Act GPAI Compliance:**

- Maintain machine-readable records of opt-out status by domain
- Keep provenance metadata linking training data to source and access date
- Prepare training data summary for Art. 53 disclosure (content categories, sources,
  volume, any restrictions)

### Step 8: Assess License and Creative Commons Compatibility

Analyze the license terms for each dataset category.

#### 8a. Creative Commons License Matrix

| CC License                         | AI Training Permitted?                                     | Commercial AI Training? | Notes                                                                   |
| ---------------------------------- | ---------------------------------------------------------- | ----------------------- | ----------------------------------------------------------------------- |
| **CC0 (Public Domain Dedication)** | Yes                                                        | Yes                     | No restrictions                                                         |
| **CC BY**                          | Yes                                                        | Yes                     | Attribution required — models must credit sources                       |
| **CC BY-SA**                       | Likely yes (model not a derivative work per most analyses) | Yes                     | Attribution; debate on whether fine-tuned models are SA-covered         |
| **CC BY-NC**                       | Non-commercial only                                        | **No**                  | Commercial training violates NC restriction                             |
| **CC BY-ND**                       | Uncertain — debate whether model is "derivative work"      | Uncertain               | "No derivatives" — if model is derivative, commercial training violates |
| **CC BY-NC-SA**                    | Non-commercial only                                        | **No**                  | Both NC and SA restrictions apply                                       |
| **CC BY-NC-ND**                    | Non-commercial only, no derivatives                        | **No**                  | Most restrictive; commercial training clearly violates                  |

**Additional restrictions to check:**

- **No-AI-Train addendum** (nolai.org or similar): Some creators add AI-specific
  restrictions alongside CC licenses. These may be enforceable as contractual terms
  even if not part of the CC license itself. [VERIFY enforceability]
- **C2PA rights assertion**: Data Use Allowed metadata field specifies permitted uses
  including whether training is allowed [VERIFY coverage]

#### 8b. Open Dataset License Assessment

| Dataset                            | License                            | Commercial Training?                   | Key Notes                                    |
| ---------------------------------- | ---------------------------------- | -------------------------------------- | -------------------------------------------- |
| Common Crawl                       | CC0 / no license claim             | Subject to underlying content licenses | Source URLs carry their own rights           |
| Wikipedia / Wikitext               | CC BY-SA 3.0                       | Yes (attribution + share-alike)        | Share-alike debate for models                |
| C4 (Colossal Clean Crawled Corpus) | Based on Common Crawl — same issue | Uncertain                              | Filtered from CC                             |
| The Pile (EleutherAI)              | Mixed — subset-dependent           | Mixed                                  | Books3 subset has copyright issues           |
| LAION-400M / LAION-5B              | CC BY 4.0 (dataset itself)         | Yes (dataset metadata)                 | Underlying images carry own rights           |
| GitHub Code (Codex training)       | Mixed OSS licenses                 | Dependent on license                   | GPL, MIT, Apache, etc. — varying attribution |

[VERIFY current status of all datasets above — licensing posture changes]

#### 8c. Proprietary Dataset Risk

For any dataset acquired without a license or whose license terms are ambiguous:

- Flag as RISK
- Identify whether the copyright holders have active licensing programs (evidence of
  market harm under fair use Factor 4)
- Check whether the copyright holders are plaintiffs in active AI training litigation

### Step 9: Analyze DMCA Section 1202, Right of Publicity, and Other Claims

#### 9a. DMCA Section 1202 — Copyright Management Information (CMI)

17 USC § 1202(b) prohibits: knowingly removing or altering CMI (copyright notices,
author info, title, terms and conditions) from a work, or distributing works knowing
CMI has been removed, when done to facilitate infringement. [VERIFY]

**AI training relevance:**

- Training data preprocessing often strips CMI (metadata, author bylines, watermarks,
  copyright notices) to normalize inputs
- If a model learns to generate content without CMI that the original had, and this
  facilitates reproduction without attribution, § 1202 claims are plausible
- **Getty Images v. Stability AI**: Includes § 1202 claims based on alleged removal of
  Getty watermarks and copyright metadata from training images. [VERIFY current status]
- **Raw Story Media v. OpenAI** (SDNY): Court allowed § 1202 claim to proceed (2024),
  finding that CMI removed from article text in training data may satisfy § 1202(b).
  [VERIFY current status]
- Requires "knowing" removal and intent to facilitate infringement — intent is contested

**Checklist for § 1202 risk:**

- [ ] Does the dataset preprocessing pipeline strip author names, bylines, or
      copyright notices from text?
- [ ] Were image watermarks or IPTC metadata removed from training images?
- [ ] Were terms and conditions fields removed from scraped content?
- [ ] Is the model capable of reproducing content without its original CMI?

**Classification**: CLEAR (CMI preserved throughout pipeline) / CAUTION (some CMI
stripping without systematic tracking) / RISK (systematic CMI removal, especially of
watermarks from commercial image sources)

#### 9b. Right of Publicity

Training data that includes images, audio recordings, or text about identifiable real
people creates right of publicity exposure (US state law):

| State          | Statute                                                                                                                         | Key Provisions                                                                                                                                                                | AI Relevance                                                                                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **California** | Cal. Civ. Code § 3344; common law                                                                                               | Name, likeness, voice protection                                                                                                                                              | Cal. AB 2602 / SB 1071 (2024 — digital replicas) [VERIFY status]                                     |
| **New York**   | NY Civil Rights Law §§ 50–51                                                                                                    | Commercial use of name/likeness                                                                                                                                               | NY proposed legislation (2024) [VERIFY]                                                              |
| **Tennessee**  | ELVIS Act (2024)                                                                                                                | Protects voice explicitly against AI                                                                                                                                          | Enacted; applies to AI-generated voice replicas [VERIFY]                                             |
| **Federal**    | **NO FAKES Act (S.1367/H.R.2794, 119th Congress) — passed both chambers in 2025** [VERIFY enactment and presidential signature] | Creates federal property right in voice and visual likeness; prohibits AI digital replicas; DMCA-style notice-and-takedown; preempts pre-2025 state laws for digital replicas | Supported by OpenAI, Google, Amazon, SAG-AFTRA, RIAA. Opposed by EFF, CDT on First Amendment grounds |

**Assessment triggers:**

- Training data includes celebrity images, audio, or video: evaluate right of publicity risk
- Training data includes content depicting private individuals who did not consent to
  inclusion: privacy tort risk [VERIFY]
- Model can generate convincing voice or visual replicas of real people: output liability risk

**Classification**: CLEAR (no identifiable people in training data) / CAUTION (public
figures in training data, consent unclear) / RISK (commercial use of training data
featuring recognizable individuals for voice/likeness replication)

#### 9c. Database Sui Generis Rights (EU)

Under Database Directive 96/9/EC, the maker of a database has sui generis protection if
there has been "substantial investment" in obtaining, verifying, or presenting the
database contents. [VERIFY]

- **Applies to**: Structured databases where scraping would extract a substantial part
- **Extraction for TDM**: DSM Art. 3 and 4 explicitly apply to databases (Recital 14
  of DSM Directive states TDM exceptions override database protection) [VERIFY]
- Therefore, if the TDM exception applies, database sui generis rights do not block TDM

### Step 10: Assess EU AI Act GPAI Disclosure Obligations

For models that qualify as General Purpose AI (GPAI) under the EU AI Act [VERIFY scope]:

**Qualification threshold**: A model trained on large amounts of data using self-supervision
at scale that has significant generality and is capable of competently performing a wide
range of distinct tasks. [VERIFY Art. 3(63) definition and thresholds]

**Systemic risk threshold**: Models trained on >10^25 FLOPs or designated by the EU AI
Office as posing systemic risk face additional obligations. [VERIFY]

**Enforcement timeline:** [VERIFY]

- August 2, 2025: GPAI obligations (Article 53) **now in effect** — training data summary
  template published (July 2025), GPAI Code of Practice finalized
- August 2, 2026: Full enforcement powers — fines up to €15 million or 3% of global
  annual turnover, whichever is greater
- If your model is a GPAI deployed in the EU, you are **already required** to comply
  with Article 53 as of August 2025

**Standard GPAI obligations (Article 53):** [VERIFY current guidance]

| Obligation                   | Requirement                                                                                           | Status                     |
| ---------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------- |
| **Copyright compliance**     | Comply with EU copyright law including DSM Art. 4 opt-outs; implement copyright compliance policy     | **In effect Aug. 2, 2025** |
| **Training data summary**    | Publish sufficiently detailed summary using the EU AI Office mandatory template (published July 2025) | **In effect Aug. 2, 2025** |
| **Technical documentation**  | Maintain and keep up-to-date technical documentation of training process                              | **In effect Aug. 2, 2025** |
| **Downstream provider info** | Provide information to downstream deployers to enable their own compliance                            | **In effect Aug. 2, 2025** |

**Training data summary content** (EU AI Office mandatory template, published July 2025): [VERIFY]
The template balances transparency with trade secret protection — narrative/aggregated
reporting, not work-by-work disclosure. Required fields include: general training
modalities and data size; identification of large public datasets used; narrative
descriptions of licensed data, private data, scraped web content (including most
relevant domains), user-generated data, and synthetic data; and steps taken to identify
and honor machine-readable TDM opt-outs.

**California AB 2013 (Training Data Transparency Act):** [VERIFY]
California's AB 2013, effective January 1, 2026, requires developers of generative AI
systems made available in California to publicly post a high-level summary of training
datasets. Disclosure must cover: dataset sources, types of data, whether copyrighted
materials were included, and whether personal information was included. xAI challenged
the law in December 2025; failed to obtain preliminary injunction (February 2026).
OpenAI and Anthropic have both posted compliant AB 2013 disclosures. [VERIFY current
enforcement status]

**⟁ CLARIFY** — If EU AI Act compliance is a primary objective:
"Is this model commercially available in the EU? Has it been determined to be a GPAI
model under the EU AI Act? Have you completed a copyright policy for DSM Art. 4 opt-out
compliance? Do you have a draft training data summary?"

### Step 11: Quality Verification and Output

Before delivering the analysis, run the quality checks defined in the Quality Assurance
Framework:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every RED-classified item, run the 3-pass Self-Interrogation.
3. Assign Confidence Scores to each major analysis.
4. Verify all [JURISDICTION-SPECIFIC] markers are correctly placed.
5. Confirm no jurisdiction-specific concepts are stated as universal.
6. Verify completeness: all relevant data categories, acquisition methods, and
   jurisdictions have been addressed.
7. Generate the Glass Box Audit Trail and append it to the output.

---

## Topic Analysis Reference

### §1. US Fair Use Doctrine — AI Training Summary

**Governing statute**: 17 USC § 107 [VERIFY current text]

**US Copyright Office Guidance**: In May 2025, the Copyright Office released its
108-page _Copyright and Artificial Intelligence, Part 3_ report (the most authoritative
US guidance to date). Key findings: [VERIFY for any updates since May 2025]

- AI training is transformative "as a matter of degree" — not categorically transformative
- Uses for **noncommercial research or analysis** that do not enable reproduction of
  content in outputs are **likely fair use**
- Making **commercial use of vast troves of copyrighted works to produce expressive
  content competing in existing markets** — especially through illegal access — **goes
  beyond established fair use boundaries**
- The Office recommended allowing voluntary licensing markets to develop (no compulsory
  licensing recommended)

**The 2025 Fair Use Trilogy — Summary:**

| Case                                             | Output Function                   | Source                       | Result                                                                                        |
| ------------------------------------------------ | --------------------------------- | ---------------------------- | --------------------------------------------------------------------------------------------- |
| Thomson Reuters v. Ross (D. Del., Feb. 11, 2025) | Same as original (legal research) | Third-party compilation      | **Not fair use** [VERIFY appeal status]                                                       |
| Bartz v. Anthropic (N.D. Cal., Jun. 23, 2025)    | Different (LLM language model)    | Legitimately purchased books | **Fair use** (settled Aug. 2025) [VERIFY]                                                     |
| Bartz v. Anthropic (N.D. Cal., Jun. 23, 2025)    | Different (LLM language model)    | Pirated copies               | **Not fair use** — piracy defeats fair use even for transformative LLM training [VERIFY]      |
| Kadrey v. Meta (N.D. Cal., Jun. 25, 2025)        | Different (LLM language model)    | Pirated copies               | **Fair use** — no market harm evidence produced by plaintiffs (narrow ruling) [VERIFY appeal] |

**Thomson Reuters Enterprise Centre GmbH v. Ross Intelligence, Inc.** (D. Del., Feb. 11, 2025,
Judge Bibas, on appeal to 3d Cir.): [VERIFY current status]

- First merits ruling holding AI training is **not fair use**
- Factor 1 decisive: under AWF v. Goldsmith (2023), the court required "a different
  purpose or character." Because Ross's AI legal research tool served the **same
  purpose** as Westlaw (facilitating legal research), the use was not transformative
- Factor 4: even without an existing licensing market, the court credited Thomson
  Reuters's potential ability to develop one
- Key lesson: if an AI output tool **serves the same market function** as the works
  used to train it, fair use is very unlikely

**Bartz v. Anthropic** (N.D. Cal., Judge Alsup, decided Jun. 23, 2025, settled Aug. 2025): [VERIFY]

- LLM training on **legitimately purchased print books** = fair use (transformative; purpose
  entirely different from entertainment reading; no meaningful market harm from LLM training)
- LLM training on **pirated copies** = not fair use. Downloading from pirate sites created
  a "central library" beyond any fair use justification regardless of downstream transformativeness
- **Critical principle**: provenance of the training data matters. Piracy defeats fair use
  even if the training use itself would otherwise qualify

**Kadrey v. Meta** (N.D. Cal., Judge Chhabria, decided Jun. 25, 2025): [VERIFY appeal status]

- Summary judgment for Meta; LLM training on books (even pirated books) held fair use
  because plaintiffs produced **no concrete market harm evidence**
- Judge Chhabria: "using copyrighted works to train AI models without permission **likely
  will constitute infringement**, especially if it undermines the market for those works"
  — the ruling was narrow and fact-specific, not a blanket endorsement
- **Tension with Bartz**: Bartz held piracy defeats fair use; Kadrey found fair use despite
  piracy because of absent market harm evidence. Appellate resolution needed.

**Other key precedents** (verify current status before relying):

- _Feist Publications v. Rural Tel. Serv. Co._, 499 U.S. 340 (1991): Originality [VERIFY]
- _Campbell v. Acuff-Rose Music_, 510 U.S. 569 (1994): Transformativeness [VERIFY]
- _Authors Guild v. Google_, 804 F.3d 202 (2d Cir. 2015): Book scanning for search
  index was fair use; snippet display transformative [VERIFY]
- _Oracle America v. Google_, 141 S.Ct. 1183 (2021): Reimplementation of Java API [VERIFY]
- _Andy Warhol Foundation v. Goldsmith_, 598 U.S. 508 (2023): Narrowed transformativeness;
  commercial licensing use that competes with copyright owner's market not transformative
  even if stylistically different [VERIFY]
- _The New York Times Co. v. Microsoft Corp. et al._ (SDNY MDL No. 3143): MTD denied
  March 26, 2025; discovery ongoing; OpenAI ordered to produce 20M ChatGPT conversation
  logs (Jan. 2026). Regurgitation/memorization theory central to complaint [VERIFY]

**The memorization problem**: Training a model on a work does not inevitably infringe,
but if the model can reproduce substantial portions of the work verbatim in response to
prompts, the reproducibility itself may constitute infringement separate from the training
act. This is the central legal theory in NYT v. OpenAI. Bartz also established that the
**source** of the training data (pirated vs. licensed/purchased) is legally material. [VERIFY]

### §2. EU DSM Directive TDM Exceptions — Detail

**Directive 2019/790/EU on copyright in the digital single market** (DSM Directive)

**Article 3 — Mandatory TDM Exception for Research:**

- Beneficiaries: "research organisations and cultural heritage institutions" carrying
  out scientific research
- Works: lawfully accessible
- Purpose: for scientific research purposes
- Storage: may retain copies for scientific research, including for verification of
  results
- Override: cannot be excluded by contract
- Key gap: does not cover commercial AI development
- Member state implementation required by June 2021 [VERIFY implementation status per
  member state]

**Article 4 — Permissive TDM Exception (Subject to Opt-out):**

- Beneficiaries: "any person" (including commercial AI companies)
- Works: lawfully accessible reproductions of works or other subject matter
- Scope: reproductions and extractions for TDM
- Opt-out: rights holders "may reserve the rights" by means of a "machine-readable
  manner" — Recital 18 of the DSM Directive specifically mentions metadata and terms
  and conditions of websites [VERIFY implementation]
- If opt-out reserved: Art. 4 does not apply; license required
- Retention of copies: for as long as necessary for TDM, then must be deleted or
  anonymised
- Contract override: Art. 4 cannot be excluded by contract terms; if a website's ToS
  prohibits scraping, this does not constitute an effective opt-out under Art. 4 (only
  machine-readable opt-outs count) [VERIFY]

**Key practical point**: The DSM Directive gives commercial AI developers a legal basis
to train on content from the open web as long as rights holders have not reserved their
rights via machine-readable opt-outs and access was lawful. This is a materially clearer
legal basis than US fair use, which remains highly contested.

**LAION v. Kneschke — Hamburg courts confirm Art. 3 scope** (LG Hamburg Sep. 2024;
upheld OLG Hamburg Dec. 2025): [VERIFY]

- LAION (nonprofit) qualifies as a "research organization" under Art. 3 because it is
  nonprofit and its dataset is freely available for public benefit
- robots.txt opt-outs cannot block Art. 3 because Art. 3 admits no opt-out
- Even if Art. 4 applied, Kneschke's robots.txt was not sufficiently machine-readable
  under Art. 4(3) — creates important precedent on what constitutes a valid opt-out
- Limitation: Art. 3 applies to qualifying nonprofits; commercial AI developers must
  rely on Art. 4 with its opt-out requirement

**GEMA v. OpenAI — Munich court opposing view** (LG Munich, 2024-2025): [VERIFY]

- Munich court ruled against OpenAI; found TDM exception insufficient to cover AI
  training processes that involved reproduction of protected works within the model
- Creates Hamburg/Munich split in Germany — appellate resolution or CJEU guidance needed
- Until resolved, Art. 4 defense in Germany carries litigation uncertainty beyond other
  EU member states

**Machine-readable vs. machine-actionable gap**: The EU Commission launched a 2025
consultation recognizing that while Art. 4(3) requires "machine-readable" opt-outs, no
universally recognized technical standard exists. robots.txt signals access restriction
but may not legally articulate a copyright reservation specifically. The GPAI Code of
Practice commits signatories to respect robots.txt as a **baseline minimum**, not a
complete solution. [VERIFY current consultation status and any new standards adopted]

**EU AI Act connection (Art. 53(1)(d))**: GPAI providers relying on Art. 4 must:

- Implement a copyright compliance policy
- Make publicly available a summary of training data
- This creates a documentation and audit trail obligation [VERIFY final guidance]

### §3. Machine-Readable Opt-out Mechanisms

| Mechanism                           | Technical Form                          | Coverage                                | Industry Adoption                                                   |
| ----------------------------------- | --------------------------------------- | --------------------------------------- | ------------------------------------------------------------------- |
| **robots.txt — AI User-Agents**     | `User-agent: GPTBot` / `Disallow: /`    | Website-level; text content             | Common Crawl, OpenAI, Anthropic, Google all have user-agent strings |
| **robots.txt — CCBot**              | `User-agent: CCBot` / `Disallow: /`     | Common Crawl crawler                    | Widely used by publishers                                           |
| **`tdmrep.json` (W3C draft)**       | JSON file at `/.well-known/tdmrep.json` | More granular TDM-specific reservations | W3C TDM Reservation Protocol — draft status [VERIFY]                |
| **HTTP `X-Robots-Tag` header**      | HTTP response header                    | Per-URL control                         | Supported by major crawlers                                         |
| **C2PA rights assertion**           | Embedded in image/content metadata      | Multimedia content                      | Growing adoption by Getty, Adobe, news orgs                         |
| **IPTC `Rights` field**             | Image EXIF/IPTC metadata                | Images                                  | Standard in professional photography                                |
| **HTML `<meta name="robots">` tag** | HTML metadata                           | Web pages                               | Standard but less AI-specific                                       |

**Practical recommendation**: Honor all of the above as opt-outs for purposes of EU AI
Act compliance and fair use good faith analysis. Implement a crawl pipeline that checks
and logs opt-out status per URL/domain.

### §4. Key Litigation Landscape (as of Q1 2026)

[All case statuses require verification — this area evolves rapidly — [VERIFY all]]

| Case                                   | Court                      | Key Claims                                                       | Status / Key Rulings                                                                                                                                                      |
| -------------------------------------- | -------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| _Thomson Reuters v. Ross Intelligence_ | D. Del.                    | Copyright infringement (headnotes for AI training)               | **Summary judgment for Thomson Reuters (Feb. 11, 2025) — first "not fair use" ruling for AI training.** On appeal, 3d Cir. [VERIFY]                                       |
| _Bartz v. Anthropic_                   | N.D. Cal.                  | Copyright infringement (books, including pirated copies)         | **Summary judgment Jun. 23, 2025:** purchased books = fair use; pirated copies = not fair use. **Settled Aug. 26, 2025.** [VERIFY]                                        |
| _Kadrey v. Meta_                       | N.D. Cal.                  | Copyright infringement (books in LLaMA training)                 | **Summary judgment for Meta Jun. 25, 2025:** LLM training fair use; no market harm evidence. Narrow ruling. [VERIFY appeal]                                               |
| _The NYT v. Microsoft / OpenAI_        | SDNY MDL No. 3143          | Direct infringement, DMCA § 1202, hot news misappropriation      | MTD denied Mar. 26, 2025; OpenAI ordered to produce 20M ChatGPT logs (Jan. 2026); discovery ongoing [VERIFY]                                                              |
| _Authors Guild v. OpenAI_              | SDNY (consolidated in MDL) | Mass infringement of literary works                              | Consolidated class-action complaint filed May 2025; motions to dismiss briefed; discovery proceeding [VERIFY]                                                             |
| _Andersen v. Stability AI_             | N.D. Cal.                  | Class action; visual artist copyright claims                     | Survived dismissal (Aug. 2024); narrowed claims; in discovery [VERIFY]                                                                                                    |
| _Getty Images v. Stability AI_         | D. Del.                    | Copyright infringement (images), DMCA § 1202 (watermark removal) | Discovery phase; key § 1202 watermark claims active [VERIFY]                                                                                                              |
| _Raw Story Media v. OpenAI_            | SDNY                       | DMCA § 1202 CMI removal                                          | § 1202 claim survived MTD; in litigation [VERIFY]                                                                                                                         |
| _Doe v. GitHub_                        | N.D. Cal. → 9th Cir.       | DMCA § 1202 (Copilot strips OSS license headers)                 | **9th Circuit accepted interlocutory appeal (Sep. 2024); opening brief filed Apr. 9, 2025; decision pending** — will resolve identicality requirement for § 1202 [VERIFY] |
| _LAION v. Kneschke_                    | LG Hamburg → OLG Hamburg   | Photographer sought injunction; Art. 3 TDM exception             | **LAION upheld under Art. 3 (Sep. 2024, upheld Dec. 2025):** LAION is nonprofit research org; robots.txt cannot opt out of Art. 3 [VERIFY]                                |
| _GEMA v. OpenAI_                       | LG Munich                  | Music rights; TDM exception insufficient for AI training         | Munich court ruled against OpenAI — creates Hamburg/Munich split in Germany awaiting higher court resolution [VERIFY]                                                     |
| _Concord Music Group v. Anthropic_     | M.D. Tenn.                 | Music lyrics infringement (training + output)                    | In progress [VERIFY]                                                                                                                                                      |

**Strategic observations** (as of Q1 2026):

- **The 2025 trilogy** (Thomson Reuters / Bartz / Kadrey) creates the emerging framework:
  functional overlap with original purpose → not fair use; transformative LLM purpose
  - legitimate sources → fair use; piracy → undermines fair use even if transformative
- **Provenance documentation is now essential**: Bartz established that pirated source
  data defeats fair use even for otherwise transformative LLM training — distinguishing
  legitimately acquired from pirated training data is legally material
- **§ 1202 identicality battle**: Doe v. GitHub in the Ninth Circuit will settle the
  most contested procedural question in CMI claims; watch for decision mid-2026
- **EU Hamburg/Munich split** awaiting higher court resolution; CJEU guidance may
  eventually be needed on Art. 3/4 scope
- **No appellate or Supreme Court decision** has yet settled the core fair use question
  for generalized LLM training on internet-scraped content — the Bartz/Kadrey tension
  on piracy needs Third Circuit or Ninth Circuit resolution [VERIFY]

### §5. Training Data Licensing Strategies

**Licensing approaches (risk-ordered):**

| Approach                                 | Risk Level   | Description                                                                    | Best For                                             |
| ---------------------------------------- | ------------ | ------------------------------------------------------------------------------ | ---------------------------------------------------- |
| **Direct licensing from rights holders** | CLEAR        | Pay-for-use licenses negotiated directly with publishers, news orgs, authors   | High-value, identifiable content owners              |
| **Collective licensing / PLUS registry** | CLEAR        | License through collecting societies or rights aggregators                     | Large-scale image / music licensing                  |
| **Open dataset (verified clean)**        | GREEN–YELLOW | Use only datasets with verified permissive licenses; audit provenance          | Baseline for any commercial model                    |
| **Open web + opt-out compliance**        | YELLOW       | Scrape public web, honor all opt-outs; EU Art. 4 compliant                     | Commercially viable if opt-out compliance documented |
| **Licensed data exchanges**              | GREEN        | AI-specific licensing platforms (e.g., AP/OpenAI, Shutterstock/OpenAI deals)   | Images, news, specialized content                    |
| **Synthetic data augmentation**          | GREEN        | Use model outputs or procedurally generated data; avoids copyright             | Specific domains where generation is feasible        |
| **Open web without opt-out tracking**    | RED          | Scraping without systematic opt-out review; standard practice for older models | High litigation risk in current environment          |

---

## Risk Classification System

### GREEN — Legally Defensible

Strong legal basis for the training data use. Reasonable arguments available under fair
use and/or TDM exception. Low litigation risk absent specific rights holder action.

**Examples:**

- CC0 or CC-BY licensed open datasets with verified provenance
- Publicly available factual text with no opt-outs, used for non-commercial research
- Content licensed directly from rights holders for AI training
- Web content where all machine-readable opt-outs were systematically honored and logged,
  accessed lawfully, for a genuinely transformative (non-substituting) purpose

**Action**: Document the legal basis. Maintain compliance records for EU AI Act Art. 53.

### YELLOW — Material Risk — Mitigation Required

Identifiable legal risk, but mitigations exist. Proceed with legal counsel review and
documented mitigation steps. Do not deploy commercially without addressing the risks.

**Examples:**

- Commercial use of primarily factual public web content with partial opt-out compliance
- Open datasets where the underlying content license is ambiguous
- CC-BY-SA content where the share-alike obligation's application to models is contested
- Training data that includes some creative works alongside predominantly factual content
- Historical training data where opt-out records are incomplete

**Action**: Identify the risk source. Obtain legal counsel advice. Implement mitigations
(improve opt-out compliance, seek licenses for identified high-value content, document
fair use arguments). Add to EU AI Act training data summary.

### RED — High Legal Risk — Do Not Deploy Without Resolution

Material legal risk with weak or no defenses. Counsel review required before proceeding.
Likely requires licensing, dataset curation, or model retraining.

**Examples:**

- Paywalled / subscription content scraped without authorization
- Content from rights holders who have served cease-and-desist letters
- Images with DMCA § 1202 CMI (watermarks, metadata) stripped in preprocessing
- Creative works from active AI litigation plaintiffs (NYT, Getty, major publishers)
- Training data where memorization is identified and the model can reproduce substantial
  portions of copyright owner's works verbatim
- Commercial model trained on CC-BY-NC licensed datasets

**Action**: Escalate to senior IP counsel. Evaluate: (a) licensing, (b) dataset curation
to remove high-risk content, (c) model retraining, (d) litigation defense strategy.
Do not commercially deploy without resolution.

### BLOCKED — Use Is Almost Certainly Unlawful

No viable legal defense. Use requires explicit authorization from rights holders.

**Examples:**

- Scraping past login/paywall controls to acquire training data
- Using content where a court injunction or TRO prohibits use
- Deliberately stripping watermarks or CMI to evade detection
- Training on private/confidential data without authorization

**Action**: Stop use immediately. Seek legal counsel. Engage rights holders for licensing.

---

## Actionable Output per Finding

For each identified risk, produce:

```
**Data Category**: [Category and source]
**Risk Classification**: [GREEN / YELLOW / RED / BLOCKED]
**Legal Basis**: [Statute, case, or principle — mark [VERIFY] if unverified]
**Confidence**: [Definite / High / Probable / Possible / Unlikely]
**Issue**: [Description of the specific legal issue]
**Business Impact**: [Practical consequence if risk materializes]
**Mitigation Options**:
  1. [Primary recommendation]
  2. [Alternative approach]
  3. [Minimum viable step]
**Priority**: [Tier 1 Must-Resolve / Tier 2 Strong Preference / Tier 3 Best Practice]
**Next Steps**: [Specific actions, owners, and timeline]
```

---

## Prioritization Framework

### Tier 1 — Must-Resolve Before Commercial Deployment

Issues that create immediate, material legal exposure or that are prerequisites for
compliance:

- RED or BLOCKED risk data categories
- Active litigation plaintiff content in training data
- Paywalled or access-controlled content scraped without authorization
- DMCA § 1202 CMI removal without remediation
- EU AI Act Art. 53 compliance obligations for GPAI models deployed in EU
- Right of publicity claims from identifiable individuals whose likeness/voice was
  used commercially

### Tier 2 — Strong Preference (Address Within 90 Days)

Issues that represent material risk but have viable mitigation paths:

- YELLOW risk categories with incomplete opt-out compliance records
- Open datasets with ambiguous license provenance
- Missing training data summary for EU AI Act (if GPAI model deployed in EU)
- Share-alike license compliance for CC-BY-SA content
- Historical scraping runs without opt-out documentation

### Tier 3 — Best Practice (Address in Next Dataset / Model Version)

Issues that represent good legal hygiene or forward-looking risk management:

- Adding TDM reservation checks for additional metadata standards (C2PA, tdmrep.json)
- Establishing direct licensing relationships for high-value content categories
- Building synthetic data augmentation pipelines to reduce reliance on scraped content
- Publishing a voluntary training data summary beyond EU AI Act minimum requirements
- Implementing a systematic opt-out monitoring program for existing licensed data sources

**Strategy**: Resolve Tier 1 before deployment. Develop a roadmap for Tier 2 items.
Build Tier 3 into next dataset refresh cycle.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                               | Fail Action                                                  |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Source**     | Every legal claim cites a specific statute, regulation, or established principle                                                                   | Add citation or mark "[UNVERIFIED — counsel to confirm]"     |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction                                                                        | Fix format                                                   |
| **Currency**   | Every cited provision checked for amendments, repeal, or superseding case law                                                                      | Flag "[CHECK CURRENCY — may have been amended or overruled]" |
| **Domain**     | Analysis stays within the applicable jurisdiction. No US-only concepts applied to EU analysis or vice versa                                        | Remove or flag jurisdictional bleed                          |
| **Confidence** | Uncertainty explicitly stated, not hidden. If a legal position is genuinely contested (as most AI training fair use positions are), say so clearly | Add confidence qualifier                                     |

**AI training copyright-specific gate**: Because this area is actively litigated with no
binding appellate precedent on the core fair use question as of early 2026, apply an
additional **Contested Doctrine** gate: any statement about fair use for AI training must
acknowledge that the doctrine is unsettled and that litigation outcomes could shift the
analysis materially.

### Self-Interrogation for RED Items

For any item classified as RED, apply this 3-pass self-interrogation before delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the risk assessment follow logically from the statute or case cited?
- Would a court applying the most current relevant case law actually reach this conclusion?
- Is there a counter-argument (e.g., a fair use defense, a lack of standing argument,
  a damages limitation) that the analysis has not addressed?

**Pass 2 — Completeness**:

- Have all relevant legal theories been considered (copyright, DMCA § 1202, ToS contract,
  CFAA, right of publicity, database protection)?
- Are there facts the user has not provided that would change the classification?
- Have EU and US frameworks both been applied where the model operates in both markets?

**Pass 3 — Challenge**:

- What is the strongest argument that this RED item is actually acceptable (fair use,
  TDM exception, implied license, de minimis)?
- Under what circumstances might a court rule for the AI developer?
- Is the RED classification proportionate to the actual litigation risk, or is it driven
  by worst-case assumptions?

If any pass reveals a weakness, revise before delivery. Mark: `self_interrogation: PASS`
or `self_interrogation: REVISED`.

### Confidence Scoring

| Level        | Range     | Meaning                                                    | Action                                                |
| ------------ | --------- | ---------------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled law, clear statute, unambiguous application        | State with confidence                                 |
| **High**     | 0.80-0.94 | Strong authority, minor interpretation questions           | State with brief caveat                               |
| **Probable** | 0.60-0.79 | Good arguments but doctrine unsettled or contested         | State with reasoning and contra-indicators            |
| **Possible** | 0.40-0.59 | Genuinely uncertain; competing authorities or no precedent | Flag for counsel review with both sides               |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative                                    | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

**Calibration note for AI training copyright**: The core question of whether AI model
training on internet-scraped content constitutes fair use under 17 USC § 107 was not
settled as of early 2026. Most fair use assessments in this area should be scored at
**Probable** (0.60-0.79) at best for commercial AI developers, reflecting genuine legal
uncertainty. Claims that fair use is "clear" or "settled" in this context are overconfident.

---

## Glass Box Audit Trail

Every analysis output MUST include a Glass Box audit section at the end:

```yaml
glass_box:
  skill_name: "legalcode-ai-training-data-copyright"
  analysis_date: "[date]"
  dataset_description: "[Brief description of the training dataset analyzed]"
  jurisdictions: "[US / EU / Cross-border]"
  model_use: "[Commercial / Non-commercial / Unknown]"
  primary_acquisition_method: "[Scraping / Licensed / Mixed / Unknown]"
  opt_out_compliance: "[Systematic / Partial / Unknown / N/A]"
  data_categories_assessed: "[number] categories"
  risk_summary:
    green: "[number of GREEN findings]"
    yellow: "[number of YELLOW findings]"
    red: "[number of RED findings]"
    blocked: "[number of BLOCKED findings]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  key_statutes:
    - "[17 USC § 107 — VERIFIED / UNVERIFIED]"
    - "[DSM Directive Art. 4 — VERIFIED / UNVERIFIED]"
    - "[EU AI Act Art. 53 — VERIFIED / UNVERIFIED]"
  key_cases_consulted:
    - "[NYT v. OpenAI — VERIFIED / UNVERIFIED]"
    - "[Getty v. Stability AI — VERIFIED / UNVERIFIED]"
    - "[AWF v. Goldsmith — VERIFIED / UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence_overall: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "Core US fair use doctrine for AI training is unsettled as of early 2026 —
      no binding appellate court ruling on point. Analysis reflects strong arguments
      rather than settled law."
    - "EU AI Act implementing guidance on Art. 53 training data summary format was
      not finalized as of drafting — verify current guidance before relying."
    - "[Any specific scope limitations, assumptions, or caveats]"
  reviewer: "AI-assisted — requires qualified IP lawyer review before relying"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do when analyzing AI training data copyright:

1. **Citing Google Books as a fair use precedent without qualification** — _Authors
   Guild v. Google_ (2d Cir. 2015) involved snippet display for search indexing with
   no verbatim reproduction of books to end users. It did not hold that training a
   generative model on copyrighted works is fair use. Drawing a direct analogy overstates
   the precedent.

2. **Treating the EU TDM exception as an unconditional green light** — DSM Art. 4
   applies only when access was lawful and no machine-readable opt-out was reserved.
   Skipping the opt-out check renders the defense unavailable for any domain that posted
   an effective opt-out.

3. **Assuming robots.txt is legally binding as a contract** — robots.txt is not a
   contract, but ignoring it: (a) eliminates the Art. 4 TDM exception for that domain,
   (b) constitutes evidence of bad faith for US fair use, and (c) may support a cease-
   and-desist or CFAA claim if other access controls were also bypassed.

4. **Conflating the act of training with the act of output reproduction** — Training
   a model on a work and the model reproducing the work verbatim in output are distinct
   legal acts. A model that can reproduce substantial portions of NYT articles verbatim
   on demand faces liability for both the training and the reproduction.

5. **Treating all Creative Commons licenses as permissive** — CC-BY-NC, CC-BY-ND, and
   CC-BY-NC-ND impose material restrictions. NC restrictions clearly prohibit commercial
   training use. ND restrictions raise genuine questions about whether a trained model
   is a derivative work. Do not assume all "open" content is freely trainable.

6. **Overlooking DMCA Section 1202 in preprocessing pipelines** — The legal community
   initially focused on direct copyright infringement. Post-_Raw Story Media v. OpenAI_
   and _Getty v. Stability AI_, § 1202 CMI claims are a live theory with different
   elements (no need to prove substantial similarity). Audit preprocessing pipelines
   for CMI stripping.

7. **Assuming the CFAA does not apply to scraping because _hiQ_ said so** — _hiQ Labs v.
   LinkedIn_ held the CFAA does not prohibit scraping publicly accessible data. But it
   did not hold that bypassing technical access controls (CAPTCHAs, IP blocks, login
   walls) is permissible. CFAA risk is real when access controls are circumvented.

8. **Ignoring ToS violations as "just a contract issue"** — ToS violations can: (a)
   eliminate the "lawful access" predicate for DSM Art. 4 (contested — see discussion
   above), (b) support willfulness arguments in copyright claims, and (c) constitute
   independently actionable breach of contract with significant damages.

9. **Failing to distinguish EU Art. 3 and Art. 4** — Art. 3 is mandatory (cannot be
   opted out of) but limited to qualifying research organizations. Art. 4 is general
   (commercial AI developers can use it) but subject to opt-out. Conflating them leads
   to incorrect conclusions about who can rely on each exception.

10. **Treating US and EU frameworks as interchangeable** — US fair use is a flexible
    four-factor balancing test with no binding precedent for AI training. EU DSM Art. 4
    is a codified exception with a clear opt-out mechanism. The EU framework provides
    significantly more legal certainty (if opt-outs are honored) than US fair use.
    Never apply EU analysis to a US claim or vice versa.

11. **Assuming no licensing market exists** — Rights holders have been actively
    establishing licensing programs for AI training (AP/OpenAI, Getty/NVIDIA,
    Shutterstock/OpenAI, various publisher deals). The existence of a licensing market
    is the most powerful argument against fair use under Factor 4. Always check whether
    the relevant content category has an active licensing program.

12. **Overlooking right of publicity in training datasets with human-generated content** —
    Datasets including images, audio recordings, or video of real people trigger right
    of publicity analysis in US state law. The ELVIS Act (Tennessee, 2024) explicitly
    covers AI-generated voice replicas. The analysis is separate from copyright and
    requires state-law-specific review.

13. **Ignoring the EU AI Act training data summary obligation** — For GPAI models
    deployed in the EU, Art. 53 creates a mandatory public disclosure obligation about
    training data. Failing to comply is a regulatory violation independent of copyright
    infringement. Build the compliance documentation pipeline from the start, not
    retroactively.

14. **Treating older datasets as automatically clean** — Many widely used training
    datasets (The Pile, LAION-5B, Books3) contain content that their creators
    acknowledged as legally uncertain or that has since been challenged in litigation.
    Historical use does not create immunity; new deployments on older models face
    forward-looking liability.

15. **Confusing dataset-level licensing with content-level licensing** — A dataset may
    be released under CC-BY, but the underlying content in the dataset may be scraped
    from sources with their own rights. The dataset creator's license only covers their
    original contribution (compilation, metadata), not the underlying third-party
    content. Always trace to the original content rights.

---

## Writing Standards

Apply plain-language discipline to all output:

**For executive summaries**:

- Active voice: "Training this model infringes X" not "Infringement of X may be a risk
  that could potentially be associated with training this model"
- Short sentences. One legal point per sentence.
- Lead with the classification (GREEN / YELLOW / RED / BLOCKED), then the reason
- Avoid false certainty ("this is clearly fair use") in an unsettled area

**For detailed analyses**:

- Cite the specific statute section and case, not generic references
- Use "may", "likely", "probably" appropriately to reflect legal uncertainty
- Distinguish between what is settled (Feist originality standard) and what is contested
  (fair use for commercial AI training)
- Separate EU analysis from US analysis — never blend the two without flagging it

**Quality gates before delivery**:

1. Can a non-lawyer CTO or product manager understand the executive summary?
2. Can IP counsel immediately locate the legal basis for each finding?
3. Is every claim marked with a confidence level appropriate to the uncertainty?
4. Are any phrases vague, hedging without reason, or ambiguous?
5. Is the distinction between "settled" and "contested" doctrine clear throughout?
6. Has jurisdiction bleed been checked — no US concepts in EU-only analysis?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 3, search for current text of 17 USC § 107, DSM Directive Arts. 3–4, EU AI
  Act Art. 53, and DMCA § 1202
- Search for current status of NYT v. OpenAI, Getty v. Stability AI, and Andersen v.
  Stability AI — case status changes frequently
- Search for EU AI Office guidance on Art. 53 training data summary format
- Search for new US legislative developments (Shields Act, NO FAKES Act status)
- Save verified authority to `/tmp/legalcode-ai-training-copyright-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Add prominent notice: "Case law cited in this analysis requires current verification
  — AI training copyright litigation is moving rapidly and case status changes frequently"
- Focus on structural risk assessment and framework application; limit reliance on
  specific case outcomes that may have changed

---

## Output Format Template

Structure the final deliverable as:

```markdown
## AI Training Data Copyright Analysis

**Dataset / Model**: [name or description]
**Analysis Date**: [date]
**Jurisdictions**: [US / EU / Cross-border]
**Commercial Use**: [Yes / No / Mixed]
**Acquisition Method**: [Scraping / Licensed / Mixed]
**Opt-out Compliance Status**: [Systematic / Partial / Unknown]
**Requested Analysis**: [Pre-clearance / Post-training risk / Litigation / GPAI compliance]

---

## Executive Summary

**Overall Risk Classification**: [GREEN / YELLOW / RED / BLOCKED]

[2-3 sentence plain-language summary of the key findings and recommended action]

**Top 3 Issues** (if any YELLOW/RED/BLOCKED):

1. [Issue, classification, one-line summary]
2. [Issue, classification, one-line summary]
3. [Issue, classification, one-line summary]

---

## Data Characterization

[Data Characterization Table from Step 4]

---

## Acquisition Legality Assessment

### Web Scraping — CFAA Analysis

[Finding, classification, confidence]

### Terms of Service Compliance

[Finding, classification, confidence]

---

## Copyright and TDM Analysis

### US Fair Use Assessment (17 USC § 107)

| Factor                   | Analysis   | Direction                                 |
| ------------------------ | ---------- | ----------------------------------------- |
| 1. Purpose and character | [analysis] | [⬆ favorable / ⬇ unfavorable / ~ neutral] |
| 2. Nature of work        | [analysis] | [⬆/⬇/~]                                   |
| 3. Amount used           | [analysis] | [⬆/⬇/~]                                   |
| 4. Market harm           | [analysis] | [⬆/⬇/~]                                   |

**Overall Fair Use Assessment**: [classification and confidence]

### EU TDM Exception Analysis (DSM Directive Arts. 3–4)

**Article 3 (Research)**:
[Applicable / Not applicable — reason]

**Article 4 (General)**:
[Opt-out compliance status; whether exception applies; classification]

### EU AI Act GPAI Compliance (Art. 53)

[Applicable / Not applicable; compliance status; outstanding obligations]

---

## Specific Risk Findings

### Finding 1: [Title] — [GREEN / YELLOW / RED / BLOCKED]

[Actionable Output per Finding format]

### Finding 2: [Title] — ...

[Repeat for each identified risk]

---

## License Compatibility Assessment

[Creative Commons and dataset license matrix results]

---

## Ancillary Claims Assessment

### DMCA Section 1202 (CMI)

[Finding and classification]

### Right of Publicity

[Finding and classification — US states only]

### Database Sui Generis (EU)

[Finding and classification — if applicable]

---

## Prioritized Recommendations

**Tier 1 (Must-Resolve Before Deployment)**:

- [Action item, owner, deadline]

**Tier 2 (Strong Preference — Address Within 90 Days)**:

- [Action item, owner, timeline]

**Tier 3 (Best Practice — Next Dataset Version)**:

- [Action item]

---

## Training Data Licensing Strategy

[Recommended approach based on the risk findings and the Training Data Licensing
Strategies table from §5 of the Topic Analysis Reference]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

This skill is primary-scoped to US and EU law. For other jurisdictions:

**United Kingdom** (post-Brexit):

- CDPA 1988 s. 29A provides a non-commercial text/data mining exception [VERIFY]
- No general commercial TDM exception equivalent to EU DSM Art. 4 exists in UK law
- UK AI training copyright position is governed by traditional fair dealing categories,
  which are significantly narrower than US fair use and lack the EU commercial TDM
  exception [VERIFY]
- In early 2025, the UK government proposed adopting an EU-style TDM exception with an
  opt-out mechanism — a significant potential post-Brexit convergence with the EU
  framework. As of March 2026, legislation has not been passed; consultation response
  pending. [VERIFY current legislative status]

**Japan**:

- Article 30-4 of the Japanese Copyright Act provides a broad non-enjoyment-purpose
  use exception that likely covers AI training (information analysis exception) [VERIFY]
- Generally considered favorable for AI training by Japanese IP scholars [VERIFY]

**Canada**:

- Section 29 "fair dealing" (not fair use) — research exception may cover some AI
  training [VERIFY]
- No explicit TDM exception; reform proposals ongoing [VERIFY]

**Singapore, South Korea, Israel**: Various exceptions exist; research local law [VERIFY]

**China**: No explicit TDM exception; copyright reform ongoing [VERIFY]

[JURISDICTION-SPECIFIC] For any non-US/EU jurisdiction: (1) research local TDM or
fair use/dealing exceptions; (2) check whether local copyright reform has introduced
AI-specific provisions; (3) apply the framework from §1 and §2 adapted to local law;
(4) verify with qualified local counsel.

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis covering the US fair use and EU
DSM TDM exception frameworks for AI training data, incorporating the EU AI Act GPAI
transparency obligations, key litigation landscape analysis, and practical opt-out
compliance guidance. Informed by the `legalcode-contract-review` and
`legalcode-copyright-infringement-assessment` quality frameworks. Calibrated against
the Legalcode gold standard (18 required quality elements). Research basis: US Copyright
Act, EU DSM Directive 2019/790/EU, EU AI Act 2024/1689/EU, DMCA, CFAA, US state right
of publicity law, W3C TDM Reservation Protocol, and publicly available AI copyright
litigation filings. All case citations require verification — this is an active
litigation area.
