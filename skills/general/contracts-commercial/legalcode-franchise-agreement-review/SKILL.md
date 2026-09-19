---
name: legalcode-franchise-agreement-review
description: Review franchise agreements and Franchise Disclosure Documents (FDD/disclosure documents)
  clause-by-clause against regulatory requirements and market standards — flag deviations, generate confidence-scored
  redlines, and produce an auditable analysis covering initial franchise fees and ongoing royalties, territory
  rights and exclusivity, intellectual property and trademark licenses, quality control and operations
  manual compliance, advertising fund contributions, training and support obligations, term and renewal
  rights, transfer and assignment restrictions, termination and post-termination obligations, non-compete
  and restrictive covenants, financial performance representations (Item 19), and dispute resolution.
  Use when reviewing franchise agreements as a prospective franchisee, existing franchisee renegotiating
  terms, or franchisor ensuring compliance.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review franchise agreements and Franchise Disclosure Documents (FDD/disclosure documents) clause-by-clause against regulatory requirements and market standards — flag deviations, generate confidence-scored redlines, and produce an auditable analysis covering initial franchise fees and ongoing royalties, territory rights and exclusivity, intellectual property and trademark licenses, quality control and operations manual compliance, advertising fund contributions, training and support obligations, term and renewal rights, transfer and assignment restrictions, termination and post-termination obligations, non-compete and restrictive covenants, financial performance representations (Item 19), and dispute resolution. Use when reviewing franchise agreements as a prospective franchisee, existing franchisee renegotiating terms, or franchisor ensuring compliance. Covers US (FTC Franchise Rule, state registration), EU (country-specific disclosure laws), UK (BFA Code, common law), and Australia (Franchising Code of Conduct 2025). GREEN/YELLOW/RED classification with redlines for franchisee-favorable and franchisor-favorable positions. Produces Glass Box audit trail, negotiation priority tiers, and stakeholder impact map.


# Legalcode Franchise Agreement Review

> **Disclaimer**: This skill provides a framework for AI-assisted franchise agreement review.
> It does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before reliance. Franchise law varies
> significantly by jurisdiction — the US has federal FTC rules plus state-specific registration
> requirements, EU member states have varying disclosure laws, the UK relies on self-regulation
> and common law, and Australia has a mandatory Franchising Code of Conduct. Laws change
> frequently; verify current applicability before relying on any provision described here.
> Statutory and case law references cited from memory carry hallucination risk — verify
> against authoritative sources before relying on them.

## Purpose and Scope

This skill reviews franchise agreements and associated disclosure documents (FDD in the US,
disclosure documents elsewhere) clause-by-clause against regulatory requirements, industry
standards, and organizational playbooks. It identifies deviations from market norms and
legal requirements, classifies their severity, generates actionable redline suggestions,
and produces a confidence-scored, auditable analysis with a negotiation priority framework.

**Covers:**

- Clause-by-clause analysis of franchise agreements and disclosure documents
- FDD Item-by-Item compliance review (US) or equivalent disclosure review (EU/UK/AU)
- GREEN / YELLOW / RED deviation classification with confidence scoring
- Redline generation with franchisee-favorable and franchisor-favorable positions
- 16 franchise clause categories (8 deep, 8 standard)
- Missing clause detection and regulatory gap analysis
- Negotiation priority tiers (Tier 1 / Tier 2 / Tier 3)
- Stakeholder impact mapping (franchisee, franchisor, guarantors, lenders, landlords)
- Business impact assessment for each material deviation
- Quality-verified output with Glass Box audit trail
- Jurisdiction-aware analysis for US, EU, UK, and Australia

**Does not:**

- Draft new franchise agreements from scratch (see `legalcode-franchise-drafter` when available)
- Provide legal advice or replace qualified franchise counsel
- Substitute for due diligence on the franchisor's business, litigation history, or financial health
- Apply to business opportunity sales that do not meet the franchise definition
- Review franchise broker or sales agent agreements

**Related skills:**

- `legalcode-contract-review` — General commercial contract review
- `legalcode-nda-triage` — Review NDAs often signed before franchise disclosure
- `legalcode-commercial-lease-review` — Review premises lease (often required for franchise locations)
- `legalcode-obligation-tracker` — Track ongoing franchise obligations and milestone dates

---

## Jurisdiction and Governing Law

This is a jurisdiction-aware skill with coverage for the US, EU member states, UK, and
Australia. The franchise agreement's governing law clause, combined with where the
franchise will be operated, determines which regulatory framework applies. Multiple
frameworks may apply simultaneously (e.g., FTC Rule + California Franchise Investment Law).

### United States — Federal and State Framework

**Federal (FTC Franchise Rule — 16 C.F.R. Part 436):**

- Requires franchisors to provide a Franchise Disclosure Document (FDD) with 23 mandatory items
- FDD must be provided at least 14 calendar days before signing or payment
- Prohibits financial performance representations outside Item 19
- 2024 FTC guidance prohibits contract clauses that chill government communications
- 2024 FTC guidance on undisclosed fees as Franchise Rule and Section 5 violations [VERIFY]

**State Registration States (15 states require registration or filing):**

- California (Franchise Investment Law), New York (General Business Law Article 33),
  Illinois (Franchise Disclosure Act), Maryland, Minnesota, North Dakota, Rhode Island,
  South Dakota, Virginia, Washington, Wisconsin, Hawaii, Indiana, Oregon, Texas [VERIFY]
- State-specific relationship laws may provide additional franchisee protections (termination,
  non-renewal, encroachment)

**State Relationship Laws:**

- Many states have franchise relationship laws that override contrary contract terms
- Common protections: good cause termination, cure periods, non-renewal notice, encroachment
- California, Iowa, Minnesota, Nebraska, New Jersey, Washington, Wisconsin among others [VERIFY]

### European Union — Country-Specific Disclosure

**No EU-wide franchise law exists.** Each member state regulates franchising through national
law. Key variations:

**France (Loi Doubin — Article L330-3 Code de commerce):**

- 20-day pre-contractual disclosure requirement (Document d'Information Précontractuelle — DIP)
- Must include franchisor identity, network history, financial condition, territory, terms
- Failure to comply may allow franchisee to void the contract [VERIFY]

**Italy (Law 129/2004 — Legge sull'affiliazione commerciale):**

- 30-day pre-contractual disclosure requirement
- Minimum 3-year initial term required
- Must disclose territory, royalties, know-how transfer details [VERIFY]

**Belgium (Book X, Code of Economic Law):**

- 30-day pre-contractual disclosure requirement
- Covers any commercial partnership agreement (broader than franchise-specific) [VERIFY]

**Spain (Royal Decree 201/2010):**

- 20-day pre-contractual disclosure requirement
- Franchisor must be registered in the Register of Franchisors
- Disclosure document (Información Precontractual) required [VERIFY]

**Germany:**

- No specific franchise disclosure law
- General pre-contractual duty of good faith (Treu und Glauben) applies
- German Franchise Association (DFV) voluntary code of ethics

**EU Competition Law (Regulation (EU) 2022/720 — Vertical Block Exemption):**

- Entered into force June 1, 2022; valid until May 31, 2034
- Safe harbor for vertical agreements if market share thresholds met
- Hardcore restrictions: resale price maintenance, absolute territorial protection, etc.

### United Kingdom — Self-Regulatory Framework

**No franchise-specific statute exists.** Franchise relationships governed by:

- General contract law (common law)
- Competition Act 1998 (UK equivalent of EU competition rules)
- Consumer Rights Act 2015 (if franchisee is a "consumer" — rare but possible)
- Intellectual property law (Trade Marks Act 1994 for trademark licensing)

**British Franchise Association (BFA) Code of Ethics:**

- Voluntary self-regulatory framework
- BFA members must provide full and accurate disclosure within reasonable time before signing
- Prospective franchisees must receive copy of Code of Ethics
- Code requires disclosure of: franchisor business and finances, people involved, franchise
  proposition, franchisee details, financial projections, agreement terms [VERIFY]

**Key UK Considerations:**

- No statutory disclosure period — timing governed by BFA Code for members, good practice otherwise
- Restraint of trade doctrine applies to post-termination non-competes (must be reasonable)
- Misrepresentation Act 1967 — remedy for pre-contractual misstatements

### Australia — Mandatory Franchising Code of Conduct

**Franchising Code of Conduct (Competition and Consumer (Industry Codes—Franchising) Regulation 2024):**

- Mandatory code under Competition and Consumer Act 2010 (Cth)
- New code effective April 1, 2025 with transition period to November 1, 2025
- Enforced by Australian Competition and Consumer Commission (ACCC)

**Key Requirements:**

- Franchisors must provide disclosure document at least 14 days before signing
- Key Facts Sheet requirement removed in 2025 Code (information consolidated into disclosure document)
- Mandatory cooling-off period of 14 days after signing
- Good faith obligation (statutory since 2015)
- Dispute resolution process prescribed (mediation, then ACAT/court)
- Marketing fund financial statements must be available to franchisees [VERIFY]

**Australian Consumer Law (Competition and Consumer Act 2010 — Schedule 2):**

- Unfair contract terms regime applies to small business contracts (including many franchises)
- Misleading or deceptive conduct prohibition (broader than US fraud standards)

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the direction or tone of the analysis
- Franchisee-side vs. franchisor-side framing requires opposite severity classifications
- Regulatory requirements differ materially by jurisdiction
- Risk tolerance or business context is needed to classify severity correctly
- The franchise model (single-unit, multi-unit, area development, master franchise) affects analysis

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

### Step 1: Accept the Franchise Agreement

Accept the franchise agreement in any of these formats:

- **File**: PDF, DOCX, or other document format
- **URL**: Link to agreement in a document management system
- **Pasted text**: Agreement text pasted directly into the conversation

If no agreement is provided, prompt the user to supply one.

### Step 2: Accept the Disclosure Document (FDD or Equivalent)

**CLARIFY** — Was a Franchise Disclosure Document (US) or equivalent disclosure document
provided?

1. **FDD/Disclosure available**: Provide the document (file, URL, or text) so the review
   can verify compliance with disclosure requirements and cross-reference agreement terms.
   - _Why this matters_: Franchise agreements often incorporate FDD representations. Discrepancies
     between disclosure and agreement terms are a major red flag and potential fraud indicator.
2. **No disclosure document**: Proceed without disclosure review. Flag this as a potential
   regulatory violation if the jurisdiction requires pre-contractual disclosure.
3. **Disclosure exists but unavailable**: Note this. Recommend obtaining the disclosure
   document before signing. In US registration states, signing without receiving the FDD
   14 days prior may give the franchisee rescission rights.

### Step 3: Gather Context

**CLARIFY** — Before beginning the review, ask:

1. **Which side are you on?**
   - Options: **Prospective Franchisee** (default — most common use case), **Existing
     Franchisee** (renegotiating or disputing terms), **Franchisor** (reviewing for compliance
     or negotiation preparation)
   - _Why this matters_: The entire severity classification flips. A broad termination right
     is RED for the franchisee and GREEN for the franchisor. State assumptions if user skips.

2. **Franchise model?**
   - Options: **Single-unit** (one location), **Multi-unit** (development agreement for
     multiple locations), **Area Development** (exclusive territory with development schedule),
     **Master Franchise / Sub-Franchisor** (right to sub-franchise in territory)
   - _Why this matters_: Multi-unit and area development agreements have additional performance
     obligations, development schedules, and territory considerations. Master franchise
     agreements involve sub-licensing analysis.

3. **Jurisdiction where franchise will operate?**
   - Options: US (specify state), EU (specify country), UK, Australia, Other
   - _Why this matters_: Determines applicable franchise disclosure law, relationship law
     protections, and competition law framework.

4. **Franchise industry/sector?**
   - Options: Food & Beverage / QSR, Retail, Services (cleaning, fitness, education, etc.),
     Automotive, Hospitality, Healthcare, Other
   - _Why this matters_: Industry-specific regulations may apply (food safety, healthcare
     licensing, automotive dealer laws). Fee structures and royalty norms vary by industry.

5. **Deal stage?**
   - Options: **Pre-signing** (evaluating whether to sign), **Post-signing** (reviewing
     existing agreement for compliance or dispute), **Renewal** (evaluating renewal terms),
     **Transfer** (evaluating as buyer of existing franchise)
   - _Why this matters_: Different issues are actionable at different stages. Pre-signing
     allows negotiation; post-signing focuses on compliance and dispute preparation.

6. **Risk tolerance?**
   - Options: **Conservative** (flag all deviations from market standards), **Pragmatic**
     (flag material deviations only), **Deal-centric** (flag only deal-breakers)
   - _Why this matters_: Calibrates the YELLOW/RED threshold without changing legal analysis.

### Step 4: Load Playbook or Market Standards

**If a playbook is provided:**

1. Read the playbook to extract the organization's standard positions for each of the
   16 clause categories.
2. Note any clause types the playbook does not address — treat those as "general market
   standards" fallbacks.
3. Confirm playbook jurisdiction alignment with the franchise's operating jurisdiction.

**If no playbook is provided (general market standards mode):**

1. Use jurisdiction-specific research conducted in Step 5 to establish market baselines.
2. Apply the Playbook Fallback Defaults table below.
3. State the benchmarks used explicitly in the output.
4. Document all benchmarks in the Glass Box audit trail.

**Playbook Fallback Defaults (Franchisee-Favorable Benchmarks):**

| Clause Category                 | Franchisee-Favorable Benchmark                                                                                   |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Initial franchise fee           | Market-comparable for industry; financing options available; fee covers substantive pre-opening support          |
| Ongoing royalties               | 4-8% of gross sales (industry-dependent); cap or floor provisions where appropriate                              |
| Advertising fund                | 1-4% of gross sales; audited financial statements available; franchisee advisory council input                   |
| Territory                       | Protected/exclusive territory; no encroachment from franchisor-owned units, e-commerce, or alternative channels  |
| IP license                      | Clear trademark usage rights; franchisor indemnifies for IP infringement claims                                  |
| Quality control                 | Reasonable standards; advance notice of changes; cost pass-through limits for mandatory upgrades                 |
| Training                        | Comprehensive initial training included in franchise fee; ongoing training at reasonable cost                    |
| Operations manual               | Incorporated by reference but material changes require notice; franchisee input on changes                       |
| Term                            | 10+ years initial term; renewal rights with predictable conditions                                               |
| Renewal                         | Right to renew if in compliance; no requirement to sign "then-current" agreement with materially different terms |
| Transfer                        | Consent not unreasonably withheld; ROFR on reasonable terms; family transfers facilitated                        |
| Termination by franchisor       | Good cause only; meaningful cure periods; no termination for de minimis violations                               |
| Termination by franchisee       | Exit rights for material franchisor breach; buyout option after minimum term                                     |
| Post-termination non-compete    | 1 year maximum; limited to franchise territory; reasonable scope                                                 |
| Financial performance (Item 19) | Substantiated representations based on actual franchisee performance; clear basis and assumptions                |
| Dispute resolution              | Choice of forum reasonably convenient; arbitration optional not mandatory; class action waiver only if mutual    |

### Step 5: Research Jurisdiction-Relevant Legal Authority

Before clause-by-clause analysis, gather jurisdiction-relevant legal authority.

**With legalcode-mcp connected:**

1. Search for franchise disclosure laws in the governing jurisdiction
2. Search for franchise relationship laws and franchisee protection statutes
3. Search for leading cases on franchise disputes (encroachment, termination, non-compete enforceability)
4. Search for regulatory guidance from FTC, ACCC, or relevant authority
5. Save results to `/tmp/legalcode-franchise-review-research.md`

**Without legalcode-mcp (fallback):**

1. Use Perplexity search for jurisdiction-specific franchise law
2. Run targeted queries: `[jurisdiction] franchise law disclosure requirements 2024 2025`
3. Mark all statutory and case law references in the analysis with **[VERIFY]**
4. Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`

**Key Research Areas by Jurisdiction:**

| Jurisdiction | Priority Research Topics                                                                                                                     |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| US (Federal) | FTC Franchise Rule 16 C.F.R. Part 436; 2024 FTC policy statement on franchising; Item 19 requirements                                        |
| US (CA)      | California Franchise Investment Law (Corp. Code § 31000 et seq.); Franchise Relations Act (Bus. & Prof. Code § 20000); encroachment case law |
| US (NY)      | General Business Law Article 33; franchise registration requirements                                                                         |
| US (State)   | State franchise relationship law; good cause termination requirements; non-compete enforceability standards                                  |
| France       | Loi Doubin (Article L330-3 Code de commerce); DIP requirements; rescission rights                                                            |
| Italy        | Law 129/2004; minimum term requirements; disclosure obligations                                                                              |
| UK           | BFA Code of Ethics; restraint of trade doctrine; Misrepresentation Act 1967                                                                  |
| Australia    | Franchising Code of Conduct 2025; ACCC guidance; Australian Consumer Law unfair terms                                                        |

### Step 6: FDD / Disclosure Document Compliance Review (If Applicable)

If a disclosure document was provided in Step 2, conduct a dedicated compliance review
before clause-by-clause agreement analysis.

**US FDD — 23 Item Review:**

| Item | Description                                        | Key Review Points                                                      |
| ---- | -------------------------------------------------- | ---------------------------------------------------------------------- |
| 1    | The Franchisor                                     | Verify corporate structure, parent/affiliates, predecessors            |
| 2    | Business Experience                                | Key personnel background — gaps or concerns?                           |
| 3    | Litigation                                         | Pending/resolved litigation — volume and nature of franchisee disputes |
| 4    | Bankruptcy                                         | Franchisor or key personnel bankruptcy history                         |
| 5    | Initial Fees                                       | Consistency with agreement; refund policy                              |
| 6    | Other Fees                                         | Complete? Hidden fees? Consistency with agreement                      |
| 7    | Estimated Initial Investment                       | Realistic? Based on actual data?                                       |
| 8    | Restrictions on Sources                            | Approved supplier requirements; rebate disclosure                      |
| 9    | Franchisee's Obligations                           | Summary table — does it match agreement?                               |
| 10   | Financing                                          | Franchisor financing terms; third-party arrangements                   |
| 11   | Franchisor's Assistance                            | Pre-opening, ongoing support; advertising programs                     |
| 12   | Territory                                          | Exclusive? Protected? Encroachment policy                              |
| 13   | Trademarks                                         | Registration status; prior disputes; licensed marks                    |
| 14   | Patents, Copyrights, Proprietary Information       | Relevant IP protections                                                |
| 15   | Obligation to Participate                          | Owner-operator requirements                                            |
| 16   | Restrictions on Goods/Services                     | Restrictions on what franchisee can sell                               |
| 17   | Renewal, Termination, Transfer, Dispute Resolution | Summary — must match agreement                                         |
| 18   | Public Figures                                     | Celebrity endorsements; compensation                                   |
| 19   | Financial Performance Representations              | Present? Substantiated? Clear assumptions?                             |
| 20   | Outlets and Franchisee Information                 | System growth/shrinkage; contact list for validation calls             |
| 21   | Financial Statements                               | Audited? Fiscal year? Concerning trends?                               |
| 22   | Contracts                                          | All agreements attached?                                               |
| 23   | Receipts                                           | Proper acknowledgment?                                                 |

**FDD Red Flags to Highlight:**

| Red Flag                                           | Significance                                                        |
| -------------------------------------------------- | ------------------------------------------------------------------- |
| High litigation volume (Item 3)                    | Pattern of franchisee disputes — investigate causes                 |
| Net unit decline (Item 20)                         | More closures/terminations than openings — business model concerns  |
| No Item 19 disclosure                              | Franchisor has data but chooses not to disclose — ask why           |
| Unrealistic Item 7 estimates                       | Low-balled initial investment — budget overruns likely              |
| Extensive approved suppliers (Item 8) with rebates | Hidden profit center for franchisor; limited franchisee flexibility |
| Weak financials (Item 21)                          | Franchisor stability concerns; ability to provide support           |
| High turnover in Item 20                           | Franchisees exiting system — validation call priority               |

**Non-US Disclosure Review:**
Apply equivalent analysis to the jurisdiction's required disclosure format (DIP in France,
disclosure document in Australia, BFA-required disclosures in UK for members).

### Step 7: Clause-by-Clause Analysis

Analyze the franchise agreement across the 16 clause categories below. Follow the deep vs.
standard depth protocol:

**Deep analysis** (full regulatory/market analysis, multi-pass review, self-interrogation for RED items):
Categories 1, 2, 3, 4, 9, 10, 11, 12

**Standard analysis** (presence/reasonableness check, market benchmark comparison):
Categories 5, 6, 7, 8, 13, 14, 15, 16

---

#### Category 1: Initial Franchise Fee and Payment Terms (DEEP)

**What to analyze:**

- Initial franchise fee amount vs. industry benchmarks
- What the fee includes (training, site selection assistance, pre-opening support)
- Payment terms (lump sum, installments, financing)
- Refund policy if franchise does not open or is terminated early
- Consistency between FDD Item 5 and agreement terms
- Whether fee is for a single unit or covers development rights

**Common Issues:**

- Non-refundable fee with no pre-opening support specified
- Fee higher than industry average without justification
- No financing options when competitors offer them
- FDD Item 5 discrepancy — additional fees not disclosed

[JURISDICTION-SPECIFIC]:

- **US**: FDD Item 5 must disclose all initial fees; refund policy required
- **Australia**: Disclosure document must specify all pre-entry payments
- **France**: DIP must include fee details; non-disclosure may void contract

**Franchisee-Favorable Position**: Initial fee covers comprehensive training, site selection,
and pre-opening support; partial refund if franchise does not open through no fault of
franchisee.

**Franchisor-Favorable Position**: Fee is earned upon signing; non-refundable; additional
fees for optional services.

---

#### Category 2: Ongoing Royalties and Fees (DEEP)

**What to analyze:**

- Royalty rate (percentage of gross sales vs. fixed amount)
- Definition of "gross sales" — exclusions, deductions
- Reporting and payment frequency
- Late payment penalties and interest
- Other ongoing fees (technology, software, audit, mystery shopper, etc.)
- Consistency with FDD Item 6
- Whether minimum royalty applies regardless of sales

**Common Issues:**

- Royalty based on gross revenue with no deductions for returns, taxes, or tips
- Hidden fees not clearly disclosed in FDD
- Excessive late payment penalties (may be unenforceable penalty in some jurisdictions)
- Minimum royalty that exceeds realistic early-stage revenue
- Technology fees that increase without cap or franchisee input

[JURISDICTION-SPECIFIC]:

- **US**: FDD Item 6 must disclose all recurring fees
- **Australia**: Franchising Code requires disclosure of all payments
- **UK**: Penalty clauses may be unenforceable if not genuine pre-estimate of loss

**Franchisee-Favorable Position**: Royalty on net sales (excluding taxes, returns); no hidden
fees; technology fees capped to CPI increases; no minimum royalty in first year.

**Franchisor-Favorable Position**: Royalty on gross sales; broad fee authority in operations
manual; minimum royalty applies from month one.

---

#### Category 3: Territory Rights and Exclusivity (DEEP)

**What to analyze:**

- Whether territory is exclusive, protected, or non-exclusive
- Definition of territory (geographic boundaries, population, etc.)
- Exceptions to exclusivity (e-commerce, national accounts, alternative channels)
- Franchisor's reservation of rights (company-owned units, other franchisees)
- Encroachment provisions and remedies
- Performance requirements to maintain territory rights
- Impact of transfer or renewal on territory

**Common Issues:**

- "Protected" territory that only prevents other franchisees, not company-owned units
- E-commerce exception that allows franchisor to sell directly in territory
- National accounts exception that captures major customers
- Territory contingent on development schedule that is unrealistic
- No remedy specified for encroachment violations

[JURISDICTION-SPECIFIC]:

- **US**: Some states have encroachment laws (e.g., Iowa, Minnesota) [VERIFY]
- **EU**: Vertical Block Exemption permits exclusive territories subject to conditions
- **Australia**: Franchising Code requires disclosure of territory details

**Franchisee-Favorable Position**: Exclusive territory with no encroachment from any channel;
franchisor compensation if encroachment occurs; territory retained on renewal.

**Franchisor-Favorable Position**: Non-exclusive territory; broad reservation of rights;
territory rights contingent on meeting development schedule.

---

#### Category 4: Intellectual Property and Trademark License (DEEP)

**What to analyze:**

- Scope of trademark license (marks, trade dress, proprietary systems)
- Geographic and temporal scope of license
- Quality control requirements tied to license
- Franchisor's obligations to protect and enforce marks
- Franchisor indemnification for IP infringement claims
- Restrictions on franchisee's use of marks (social media, domain names, local marketing)
- Consequences of trademark loss or challenge
- Treatment of franchisee-developed IP (local marketing materials, improvements)

**Common Issues:**

- No franchisor indemnification for trademark infringement claims
- Franchisor can unilaterally change marks with no compensation for rebranding costs
- Franchisee loses all rights to domain names and social media accounts on termination
- No remedy if franchisor fails to maintain or defend trademark registrations
- Overbroad restrictions on franchisee's local marketing

[JURISDICTION-SPECIFIC]:

- **US**: FDD Item 13 requires disclosure of trademark status and prior disputes
- **UK**: Trade Marks Act 1994; quality control necessary to maintain licensed mark
- **EU**: Community trademarks may cover multiple jurisdictions

**Franchisee-Favorable Position**: Franchisor indemnifies for IP claims; advance notice of
rebranding with cost-sharing; franchisee retains social media content (not accounts).

**Franchisor-Favorable Position**: Franchisee bears costs of any rebranding; all franchisee
marketing materials become franchisor IP; immediate trademark license termination on default.

---

#### Category 5: Quality Control and Operations Manual (Standard)

**What to analyze:**

- Scope of operations manual incorporation by reference
- Franchisor's right to modify manual and standards
- Notice requirements for material changes
- Franchisee's obligations to implement changes (timing, cost)
- Audit and inspection rights
- Consequences of non-compliance

**Common Issues:**

- Operations manual changes effective immediately with no notice
- Franchisee bears all costs of compliance with new standards
- No limit on frequency or scope of mandatory upgrades
- Inspection rights without reasonable notice
- Non-compliance treated as immediate termination event

**Franchisee-Favorable Position**: Material changes require 90-day notice; cost-benefit
analysis required; franchisee advisory input; inspections with 48-hour notice.

---

#### Category 6: Advertising Fund and Marketing Contributions (Standard)

**What to analyze:**

- Contribution rate (percentage of gross sales)
- Whether franchisor contributes on same basis as franchisees
- How funds are used (production, media, administrative)
- Audit rights and financial statement availability
- Local advertising requirements in addition to fund
- Franchisee input (advisory council, approval rights)
- Whether fund can be used for recruitment advertising

**Common Issues:**

- No audit rights or financial transparency
- Excessive administrative costs (should be <15-20% of fund)
- Fund used for franchise sales rather than consumer marketing
- No local advertising credit against fund contribution
- Franchisor-owned units contribute at lower rate

[JURISDICTION-SPECIFIC]:

- **US**: FDD Item 11 requires disclosure of advertising program details
- **Australia**: Franchising Code requires marketing fund financial statements

**Franchisee-Favorable Position**: Audited statements annually; franchisee advisory council;
local spending credit; no recruitment use of fund.

---

#### Category 7: Training and Support Obligations (Standard)

**What to analyze:**

- Initial training program (duration, location, who pays travel/lodging)
- Ongoing training requirements and costs
- Field support and consultation availability
- Technology and systems support
- Marketing and promotional support
- Site selection and build-out assistance

**Common Issues:**

- Initial training at franchisee's expense with no quality standards
- No ongoing support obligations specified
- Response time for support requests not defined
- Training requirements that exceed operational needs (pretext for termination)

[JURISDICTION-SPECIFIC]:

- **US**: FDD Item 11 must describe training and support in detail

**Franchisee-Favorable Position**: Comprehensive initial training included in franchise fee;
ongoing training at franchisor cost; defined support response times.

---

#### Category 8: Approved Suppliers and Sourcing (Standard)

**What to analyze:**

- Scope of approved supplier requirements
- Process for approving alternative suppliers
- Whether franchisor or affiliates are suppliers (conflict of interest)
- Rebate and volume discount disclosure
- Specification vs. source requirements
- Competitive pricing requirements

**Common Issues:**

- All supplies must come from franchisor or affiliates at above-market prices
- No process for approving alternative suppliers
- Rebates not disclosed or not shared with franchisees
- Specifications designed to exclude competitors

[JURISDICTION-SPECIFIC]:

- **US**: FDD Item 8 requires disclosure of supplier restrictions and rebates
- **Australia**: ACCC scrutinizes supplier arrangements for unfair terms

**Franchisee-Favorable Position**: Specifications rather than source requirements; rebates
shared with franchisees; alternative supplier approval within 30 days.

---

#### Category 9: Term, Renewal, and Extension Rights (DEEP)

**What to analyze:**

- Initial term length
- Number of renewal terms and length
- Conditions for renewal (compliance, remodel, fee, training)
- Whether franchisee must sign "then-current" agreement at renewal
- Notice requirements for renewal election
- Automatic renewal vs. option to renew
- Term extension for force majeure or construction delays

**Common Issues:**

- Short initial term (under 10 years) with no renewal right
- Renewal conditioned on signing materially different then-current agreement
- Excessive renewal fee or mandatory remodel requirement
- Short notice window to elect renewal (franchisee may miss deadline)
- Renewal requires waiver of existing claims

[JURISDICTION-SPECIFIC]:

- **US**: Some states require good faith renewal (Wisconsin, Iowa) [VERIFY]
- **Italy**: Law 129/2004 requires minimum 3-year initial term
- **Australia**: Franchising Code requires disclosure of renewal conditions

**Franchisee-Favorable Position**: 10+ year initial term; renewal on substantially same terms;
reasonable renewal fee; 12-month notice window.

**Franchisor-Favorable Position**: 5-year term; renewal on then-current terms; remodel
required; 6-month notice window.

---

#### Category 10: Transfer and Assignment (DEEP)

**What to analyze:**

- Franchisor consent requirement (not to be unreasonably withheld?)
- Right of first refusal (ROFR) terms and timing
- Transfer fee amount and what it covers
- Transferee qualification requirements
- Whether existing franchisee remains liable after transfer
- Family/estate transfer provisions
- Change of ownership/control triggers
- Franchisor purchase option on transfer

**Common Issues:**

- Consent "in franchisor's sole discretion" (no reasonableness standard)
- ROFR with extended matching period that chills buyer interest
- Excessive transfer fee (should be comparable to franchise fee or lower)
- Transferor remains liable for transferee's obligations
- Death/disability transfer requires new franchise fee
- Change of ownership trigger at low threshold (10-20%)

[JURISDICTION-SPECIFIC]:

- **US**: Some states limit transfer restrictions; ROFR timing limits [VERIFY]
- **Australia**: Franchising Code requires good faith in transfer decisions

**Franchisee-Favorable Position**: Consent not unreasonably withheld; 30-day ROFR; reasonable
transfer fee; no continuing liability; family transfer facilitated.

**Franchisor-Favorable Position**: Consent in sole discretion; 90-day ROFR; full franchise
fee on transfer; transferor guarantees transferee.

---

#### Category 11: Termination by Franchisor (DEEP)

**What to analyze:**

- Grounds for termination (for cause vs. at will)
- Cure periods for different violation types
- Notice requirements
- What constitutes "material" breach
- Cross-default provisions (multiple units)
- Automatic termination events (bankruptcy, felony conviction, abandonment)
- Franchisor's termination remedies

**Common Issues:**

- Termination for "any" breach with no materiality threshold
- Inadequate cure periods (should be 30-60 days for curable defaults)
- No opportunity to cure for operational violations
- Cross-default across entire franchise portfolio
- Subjective termination grounds ("in franchisor's judgment")

[JURISDICTION-SPECIFIC]:

- **US**: Many states require good cause for termination and reasonable cure periods
  (California, Illinois, Iowa, Minnesota, Nebraska, New Jersey, Washington, Wisconsin, etc.) [VERIFY]
- **Australia**: Franchising Code requires 30-day cure period for most breaches

**Franchisee-Favorable Position**: Termination only for material breach; 30-day notice and
cure for monetary defaults; 60-day notice and cure for operational defaults; no cross-default.

**Franchisor-Favorable Position**: Broad termination rights; short cure periods; automatic
termination for brand-damaging conduct; cross-default across system.

---

#### Category 12: Post-Termination Obligations and Non-Compete (DEEP)

**What to analyze:**

- De-identification requirements (signage, trade dress removal)
- Covenant not to compete (duration, geography, scope)
- Customer list and data return/destruction
- Telephone number and domain name transfer
- Assignment of lease to franchisor
- Ongoing confidentiality obligations
- Liquidated damages for violation
- Payment of outstanding amounts
- Right to purchase assets

**Common Issues:**

- Non-compete exceeds 1 year or extends beyond territory
- Non-compete scope too broad (any "similar" business)
- Franchisee must assign lease even if personally guaranteed
- Confidentiality obligations are perpetual
- De-identification at franchisee cost with unrealistic timeline
- No right to sell assets to third parties

[JURISDICTION-SPECIFIC]:

- **US (California)**: Non-competes generally unenforceable except for sale of business [VERIFY]
- **US (Most states)**: Non-competes must be reasonable in time, geography, and scope
- **UK**: Restraint of trade doctrine — must protect legitimate interest and be reasonable
- **Australia**: Restrictive covenants must be reasonable; Franchising Code limits

**Franchisee-Favorable Position**: Non-compete limited to 1 year and territory; reasonable
de-identification timeline (90 days); right to sell to third parties; no lease assignment
obligation.

**Franchisor-Favorable Position**: 2-year non-compete in 25-mile radius; immediate de-identification;
mandatory lease assignment; franchisor purchase option at book value.

---

#### Category 13: Financial Performance Representations (Standard — US Specific)

**What to analyze:**

- Whether Item 19 is included in FDD
- Basis for representations (actual results, projections, company-owned vs. franchisee units)
- Geographic and temporal scope of data
- Clear assumptions and qualifications
- Substantiation available
- Whether oral representations exceed Item 19 disclosure

**Common Issues:**

- No Item 19 when franchisor has data
- Item 19 based only on top-performing units
- Assumptions buried in footnotes
- Company-owned units outperform franchisees (different cost structure)
- Sales figures without corresponding profitability data

[JURISDICTION-SPECIFIC]:

- **US**: FTC Rule requires any financial performance representation be in Item 19
- **Other jurisdictions**: Similar disclosure requirements may apply

**Red Flags:**

- Oral claims of earnings not in Item 19 — potential FTC Rule violation
- Selective data (e.g., only units open 3+ years)
- No expense data to validate profitability claims

---

#### Category 14: Insurance Requirements (Standard)

**What to analyze:**

- Coverage types required (general liability, property, workers' comp, auto, cyber, etc.)
- Minimum limits
- Franchisor as additional insured
- Certificate requirements and timing
- Consequences of lapse
- Who bears premium cost increases

**Common Issues:**

- Excessive coverage requirements for business size
- Franchisor has unilateral right to increase requirements
- No cure period for insurance lapse
- Specialty coverage that is difficult to obtain

**Franchisee-Favorable Position**: Reasonable coverage limits; 30-day cure for lapse;
franchisor cannot unilaterally increase requirements beyond CPI.

---

#### Category 15: Dispute Resolution and Governing Law (Standard)

**What to analyze:**

- Governing law selection
- Venue/forum selection
- Mandatory arbitration vs. litigation
- Arbitration rules and venue
- Class action waiver
- Jury trial waiver
- Mediation requirement
- Prevailing party attorney's fees
- Limitation on damages (consequential, punitive)

**Common Issues:**

- Inconvenient venue (franchisor's home state regardless of franchise location)
- Mandatory arbitration with rules favoring franchisor
- Class action waiver eliminates franchisee collective action
- Waiver of statutory rights that cannot be waived

[JURISDICTION-SPECIFIC]:

- **US**: Some state franchise laws cannot be waived by choice of law; FAA generally
  enforces arbitration clauses; class action waivers increasingly challenged [VERIFY]
- **Australia**: Franchising Code mandates dispute resolution process

**Franchisee-Favorable Position**: Litigation option; venue where franchise operates;
no class action waiver; no limitation on statutory claims.

**Franchisor-Favorable Position**: Mandatory arbitration in franchisor's state; class action
waiver; jury waiver; limitation on punitive damages.

---

#### Category 16: Representations, Warranties, and Acknowledgments (Standard)

**What to analyze:**

- Franchisee's representations (financial capacity, business experience, etc.)
- Franchisor's representations (authority, no material litigation, etc.)
- Integration clause (entire agreement)
- Acknowledgments (no unauthorized representations, reviewed with counsel, etc.)
- Disclaimers (no guarantee of success, etc.)
- Survival of representations

**Common Issues:**

- One-sided disclaimers that eliminate franchisor accountability for pre-sale statements
- Acknowledgments that franchisee did not rely on any representations (contradicts FDD)
- Waiver of misrepresentation claims
- Acknowledgments designed to defeat fraud claims

**Franchisee-Favorable Position**: Mutual representations; no waiver of fraud claims;
acknowledgments do not override FDD disclosures.

---

### Step 8: Missing Clause and Gap Detection

After analyzing the clauses that are present, check for important elements that are absent:

**Regulatory Compliance Gaps:**

- [ ] Required disclosure document was not provided (RED in registration jurisdictions)
- [ ] Cooling-off period not specified (RED in Australia)
- [ ] Good faith obligation not referenced (YELLOW in Australia)
- [ ] Dispute resolution process does not comply with Franchising Code (AU)
- [ ] No personal guarantee form attached when personal guarantee required

**Market Standard Gaps:**

- [ ] No termination for franchisor breach (franchisee has no exit for franchisor default)
- [ ] No force majeure provision
- [ ] No development milestone extensions for construction delays
- [ ] No franchisee advisory council or input mechanism
- [ ] No financial performance disclosure (Item 19) when data exists

**CLARIFY** — When gap significance depends on context not provided:

- "This agreement has no termination right for franchisee if franchisor breaches. Is this
  acceptable, or should this be flagged as a RED gap?"
- "There is no Item 19 (financial performance representations). Did the franchisor provide
  earnings information verbally? If yes, this is a RED flag — oral claims must be in Item 19."

### Step 9: Flag Deviations

Classify each deviation from the playbook or market standards using the three-tier system:

### GREEN — Acceptable

The clause aligns with or is better than market standards. Minor variations that are
commercially reasonable and do not materially increase risk.

**Examples:**

- Royalty rate at low end of industry range
- 15-year initial term with two 5-year renewals
- Exclusive territory with clear boundaries
- Franchisor indemnifies for IP infringement claims

**Action**: Note for awareness. No negotiation needed.

### YELLOW — Negotiate

The clause falls outside market standards but within a negotiable range. The term is common
but not franchisee-favorable. Requires attention and likely negotiation.

**Examples:**

- Royalty at high end of industry range
- Territory "protected" rather than "exclusive"
- Renewal on "then-current" terms with reasonableness standard
- 6-month post-termination non-compete (shorter than typical but still restrictive)

**Action**: Generate specific redline language. Provide fallback position. Estimate business
impact of accepting vs. negotiating.

### RED — Escalate

The clause falls outside acceptable range, violates regulatory requirements, or poses material
risk. Requires senior review, outside counsel involvement, or walk-away consideration.

**Examples:**

- No cure period for termination (may violate state law)
- Uncapped royalties or fees
- 3-year post-termination non-compete nationwide
- No renewal rights after initial term
- Financial performance representations that exceed Item 19 disclosure
- No FDD provided within 14 days (rescission rights may apply)
- Cross-default across unrelated franchise systems

**Action**: Explain specific risk with legal basis. Provide market-standard alternative.
Estimate exposure. Recommend escalation path.

---

### Step 10: Generate Redlines

**CLARIFY** — Before generating redlines, ask if not clear from context:

- **Relationship dynamic**: New franchisor relationship, established brand with leverage,
  or competitive situation where multiple brands are being evaluated?
- **Volume of redlines**: "I've found [N] items worth negotiating. Do you want redlines for
  all of them, or should I focus on the top [X] most impactful?"

For each YELLOW and RED deviation, generate a redline using this format:

```
**Clause**: [Section reference and clause name]
**Current language**: "[exact quote from the agreement]"
**Proposed redline**: "[specific alternative language]"
**Rationale**: [1-2 sentences explaining why, suitable for external sharing]
**Legal basis**: [Relevant statute, regulation, or principle — or "General commercial practice"]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative position if primary redline is rejected]
```

### Redline Best Practices for Franchise Agreements

1. **Know your leverage**: Franchisors of established brands rarely negotiate standard agreements;
   focus on the most critical issues. Emerging franchisors may have more flexibility.
2. **Lead with regulatory compliance**: If a term may violate franchise law, lead with that
   argument — franchisors must comply regardless of negotiation posture.
3. **Reference FDD disclosures**: If the agreement contradicts the FDD, the discrepancy itself
   is the argument.
4. **Quantify financial impact**: "This clause could cost $X over the term" is more compelling
   than "this clause is unfair."
5. **Propose balanced alternatives**: One-sided redlines are rejected; propose terms that
   address both parties' legitimate interests.
6. **Identify non-negotiables**: Be clear about which issues are deal-breakers vs. preferences.

---

### Step 11: Business Impact Summary

Provide a summary covering:

- **Overall risk assessment**: High-level view of the franchise opportunity's risk profile
- **Top 5 issues**: Most important items to address, with severity and business impact
- **Regulatory compliance**: Any disclosure or relationship law compliance issues
- **Negotiation strategy**: Which issues to lead with, what to concede, sequencing
- **Validation call priorities**: Based on FDD Item 20, which franchisees to contact

**CLARIFY** — If context unclear and would materially affect strategy:

- "Is this a well-established brand where negotiation is unlikely, or an emerging franchise
  where terms may be more flexible?"
- "Are you evaluating multiple franchise opportunities, giving you walk-away leverage?"
- "Has the franchisor made verbal representations about earnings or support that are not
  in the FDD?"

---

### Step 12: Quality Verification

Before delivering the analysis, run the quality checks:

1. **Run the 5 Citation Quality Gates** silently. Revise any failures before delivery.
2. **For every RED-classified item**, run the 3-pass Self-Interrogation. Revise if any pass
   reveals a weakness.
3. **Assign a Confidence Score** to each material clause analysis.
4. **Verify completeness**: Confirm all 16 clause categories addressed (present or flagged missing).
5. **Generate the Glass Box Audit Trail** and append to output.

---

## Negotiation Priority Framework

### Tier 1 — Must-Haves (Deal Breakers)

Issues where the franchisee should not proceed without resolution:

- Regulatory compliance (FDD timing, required disclosures)
- Meaningful territory protection
- Reasonable termination cure periods
- Enforceable non-compete scope (not overbroad)
- Renewal rights with predictable conditions
- Franchisor IP indemnification

### Tier 2 — Should-Haves (Strong Preferences)

Issues that materially affect risk but have negotiation room:

- Transfer consent standard (reasonable vs. sole discretion)
- Advertising fund transparency
- Limitation on fee increases
- Development schedule flexibility
- Personal guarantee scope

### Tier 3 — Nice-to-Haves (Concession Candidates)

Issues that improve position but can be conceded strategically:

- Preferred venue for disputes
- Notice period lengths
- Specific remodel requirements
- Insurance limit details
- Minor operational manual provisions

**Negotiation strategy**: Lead with Tier 1 regulatory issues. Package Tier 2 requests together.
Trade Tier 3 concessions to secure Tier 2 wins. Never proceed without Tier 1 resolution.

---

## Quality Assurance Framework

### Citation Quality Gates

| Gate           | Rule                                                               | Fail Action                         |
| -------------- | ------------------------------------------------------------------ | ----------------------------------- |
| **Source**     | Every legal claim cites specific statute, regulation, or principle | Add citation or mark "[UNVERIFIED]" |
| **Format**     | All citations follow consistent format for jurisdiction            | Fix format                          |
| **Currency**   | Every cited provision checked for recent amendments                | Flag "[CHECK CURRENCY]"             |
| **Domain**     | Analysis stays within governing law scope                          | Remove or flag jurisdictional bleed |
| **Confidence** | Uncertainty explicitly stated                                      | Add confidence qualifier            |

### Self-Interrogation for RED Items

For any clause classified as RED, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**:

- Does the risk assessment follow from the statute/principle cited?
- Would a court in this jurisdiction reach this conclusion?
- What is the counterargument the franchisor will make?

**Pass 2 — Completeness**:

- Have all relevant franchise laws been considered?
- Are there relationship law protections in this jurisdiction?
- Have regulatory guidance documents been checked?

**Pass 3 — Challenge**:

- What is the strongest argument this clause IS acceptable?
- Under what circumstances might a reasonable franchisee accept this risk?
- Is RED proportionate, or is this actually YELLOW with mitigations?

### Confidence Scoring

| Level        | Range     | Meaning                           | Action                                     |
| ------------ | --------- | --------------------------------- | ------------------------------------------ |
| **Definite** | 0.95-1.0  | Clear statute, no ambiguity       | State with confidence                      |
| **High**     | 0.80-0.94 | Strong authority, minor questions | State with brief caveat                    |
| **Probable** | 0.60-0.79 | Good arguments but could differ   | State with reasoning and contra-indicators |
| **Possible** | 0.40-0.59 | Genuinely uncertain               | Flag for counsel review                    |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative           | Do not assert; flag "[UNCERTAIN]"          |

---

## Glass Box Audit Trail

Every franchise agreement review output MUST include a Glass Box audit section:

```yaml
glass_box:
  agreement: "[Franchise Agreement title and date]"
  franchisor: "[Franchisor name]"
  agreement_type: "[Single-unit / Multi-unit / Area Development / Master Franchise]"
  user_side: "[Prospective Franchisee / Existing Franchisee / Franchisor]"
  operating_jurisdiction: "[Jurisdiction where franchise will operate]"
  governing_law: "[Governing law per agreement]"
  applicable_frameworks:
    - "[FTC Franchise Rule / State law / Franchising Code / etc.]"
  disclosure_document_reviewed: "Yes / No / Not Provided"
  disclosure_compliance: "Compliant / Deficiencies Found / Not Reviewed"
  playbook_used: "[Playbook name or 'General market standards']"
  clauses_reviewed: 16
  clauses_present: "[number]"
  clauses_missing: "[number] — [list]"
  legalcode_mcp: "Connected / Not connected"
  research_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "[Statute 1 — VERIFIED or UNVERIFIED]"
  case_law_consulted:
    - "[Case 1 — VERIFIED or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Scope limitations, assumptions, caveats]"
  reviewer: "AI-assisted — requires qualified franchise counsel review"
```

---

## Multi-Stakeholder Mapping

For every franchise agreement, identify ALL affected stakeholders:

| Stakeholder             | Role        | Affected Clauses                         | Impact           | Action Required           |
| ----------------------- | ----------- | ---------------------------------------- | ---------------- | ------------------------- |
| Franchisee entity       | Party       | All                                      | Primary          | Sign / Negotiate          |
| Individual guarantor(s) | Guarantor   | Personal guarantee, termination          | Direct liability | Review guarantee scope    |
| Franchisor              | Party       | All                                      | Primary          | Negotiate                 |
| Landlord                | Third party | Site approval, lease assignment          | Indirect         | Coordinate site selection |
| Lender                  | Third party | Collateral, default cross-triggers       | Financing        | Review lending covenants  |
| Employees               | Internal    | Training, operations manual, termination | Employment       | Staffing planning         |
| Customers               | Third party | Service standards, brand promise         | Experience       | No direct action          |
| Regulator (FTC/ACCC)    | Regulator   | Disclosure compliance                    | Compliance       | Ensure FDD timing         |

---

## Anti-Patterns

What NOT to do in franchise agreement review:

1. **Ignoring the disclosure document** — The FDD is not separate from the agreement; it contains
   material representations that inform agreement interpretation. Always review together.

2. **Accepting "standard" as justification** — "This is our standard agreement" does not mean
   terms are market-standard or that negotiation is impossible. Evaluate independently.

3. **Skipping the Item 20 analysis** — The franchisee contact list is your best due diligence
   tool. Net unit growth/decline and turnover tell the real story.

4. **Missing the Item 19 red flag** — If the franchisor provides verbal earnings information
   but has no Item 19, this is a potential FTC Rule violation. Document and escalate.

5. **Underestimating post-termination obligations** — Non-competes, lease assignments, and
   de-identification requirements can be more damaging than the franchise itself. Analyze carefully.

6. **Ignoring state relationship laws** — Many states override "for cause" termination and
   non-renewal restrictions in the agreement. Research applicable state law.

7. **Treating territory as binary** — "Protected" and "exclusive" mean different things.
   E-commerce, national accounts, and alternative channels can eviscerate territory protection.

8. **Overlooking fee escalation** — The initial royalty rate matters less than the mechanism
   for fee increases over a 10-20 year relationship. Look for caps.

9. **Missing the cross-default trap** — Multi-unit agreements with cross-default can cause
   one underperforming unit to bring down an entire portfolio.

10. **Failing to validate** — No amount of document review substitutes for calling existing
    franchisees. The FDD gives you the contact list for a reason.

11. **Accepting non-compete at face value** — Overbroad non-competes may be unenforceable,
    but the cost of litigation to prove it is itself a burden. Negotiate reasonable scope upfront.

12. **Ignoring the operations manual** — If the manual is incorporated by reference and can
    be changed unilaterally, the franchisor can impose material new obligations post-signing.

13. **Skipping renewal analysis** — A great initial term means nothing if renewal is at
    franchisor's discretion or requires signing materially different terms.

14. **Treating advertising fund as minor** — 2-4% of gross sales over 20 years is substantial.
    Ensure transparency and franchisee input.

15. **Not calculating total cost** — Initial fee + royalties + advertising + required purchases
    - mandatory upgrades over the full term. Model the total investment.

---

## Writing Standards

Apply plain-language discipline to all output:

**For redline rationales** (shared with franchisor's counsel):

- Plain language, no jargon or filler
- Active voice: "This clause allows termination without cure period"
- Short sentences, one point per sentence
- Name the actor: "The franchisor must..." not "It is required that..."
- Specific: cite the relevant provision or regulatory requirement

**For internal analysis**:

- Same plain-language standards
- Technical legal analysis where appropriate
- Confidence qualifiers where uncertain
- Glass Box audit trail appended

**Quality gates before delivery**:

1. Can a business owner without legal training understand the executive summary?
2. Can the franchisor's counsel understand and respond to each redline?
3. Is every legal claim backed by citation (or flagged [VERIFY])?
4. Are any phrases vague or ambiguous? Fix them.
5. Could any sentence be shorter without losing meaning? Shorten it.

---

## External Tool Integration

This skill works with **legalcode-mcp** for legal research.

**With legalcode-mcp connected:**

- Search for franchise statutes and regulations by jurisdiction
- Search for franchise relationship law cases
- Search for FTC guidance and enforcement actions
- Save results to `/tmp/legalcode-franchise-review-research.md`
- Mark legalcode-mcp citations as VERIFIED in Glass Box

**Without legalcode-mcp:**

- Mark statutory and case law references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Focus on commercial risk assessment rather than legal certainty
- Recommend franchisor validation calls and independent counsel review

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Franchise Agreement Review Summary

**Franchisor**: [Franchisor name]
**Agreement Type**: [Single-unit / Multi-unit / Area Development / Master Franchise]
**Your Side**: [Prospective Franchisee / Existing Franchisee / Franchisor]
**Operating Jurisdiction**: [State/Country where franchise will operate]
**Governing Law**: [Per agreement]
**Industry**: [QSR / Retail / Services / etc.]
**Review Date**: [date]

---

## Disclosure Document Compliance

**FDD Received**: [Yes / No / Not Applicable]
**14-Day Waiting Period**: [Compliant / Not Compliant / Unknown]
**Key FDD Findings**: [Summary of Item 3, 19, 20 analysis]

---

## Key Findings

[Top 5 issues with severity flags (RED/YELLOW) and one-line summaries]

---

## Missing Elements

[List any of the 16 clause categories that are absent or incomplete, with severity]

---

## Clause-by-Clause Analysis

### [Clause Category] — [GREEN / YELLOW / RED] | Confidence: [level]

**Agreement says**: [summary of provision]
**Market standard**: [benchmark]
**Deviation**: [description of gap]
**Business impact**: [practical meaning]
**Redline** (if YELLOW or RED):

> [Specific proposed language]

[Repeat for each category]

---

## Negotiation Strategy

**Tier 1 (Must-Haves)**: [list]
**Tier 2 (Should-Haves)**: [list]
**Tier 3 (Concession Candidates)**: [list]

**Recommended approach**: [sequencing, leverage points, strategic trades]

---

## Validation Priorities

Based on FDD Item 20, prioritize calls to:

1. [Franchisee type to contact and questions to ask]
2. [...]

---

## Stakeholder Impact Map

[Table per Multi-Stakeholder Mapping section]

---

## Next Steps

[Specific actions with owners and deadlines]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

This skill covers US, EU (France, Italy, Belgium, Spain, Germany), UK, and Australia.
To create a jurisdiction-specific variant:

1. Replace [JURISDICTION-SPECIFIC] markers with verified local content
2. Add jurisdiction-specific clause categories (e.g., good faith requirements in Australia)
3. Add jurisdiction-specific anti-patterns
4. Cite specific statutes, regulations, and case law
5. Update frontmatter to reference the specific jurisdiction
6. Note local language requirements for contracts (if any)

**Planned jurisdiction-specific variants:**

- `legalcode-franchise-agreement-review-us-ca` — California Franchise Investment Law focus
- `legalcode-franchise-agreement-review-au` — Australia Franchising Code 2025 focus
- `legalcode-franchise-agreement-review-uk` — UK common law and BFA Code focus
- `legalcode-franchise-agreement-review-eu-fr` — France Loi Doubin focus

---

## Provenance

Created by Legalcode (2026-03-19). Original synthesis combining:

- FTC Franchise Rule (16 C.F.R. Part 436) and 2024 FTC guidance
- Australia Franchising Code of Conduct 2025
- EU franchise disclosure laws (France, Italy, Belgium, Spain)
- UK BFA Code of Ethics and common law framework
- Franchise agreement best practices from American Bar Association Forum on Franchising
- Quality assurance frameworks from legalcode-contract-review reference standard

Research sources:

- [FTC Franchise Rule](https://www.ftc.gov/legal-library/browse/rules/franchise-rule)
- [FTC Franchise Rule Compliance Guide](https://www.ftc.gov/system/files/documents/plain-language/bus70-franchise-rule-compliance-guide.pdf)
- [ACCC Franchising Code of Conduct](https://www.accc.gov.au/business/industry-codes/franchising-code-of-conduct)
- [Australia Treasury New Franchising Code 2025](https://treasury.gov.au/publication/p2025-633841)
- [Franchising.eu EU Regulations Overview](https://franchising.eu/my-business/30/franchise-regulations-in-the-eu-and-other-european-countries/)
- [ICLG Franchise Laws UK 2026](https://iclg.com/practice-areas/franchise-laws-and-regulations/england-and-wales)
- [NASAA Post-Term Non-Compete Analysis](https://www.nasaa.org/wp-content/uploads/2025/01/Post-Term-Non-Compete-Provisions-in-Franchise-Agreements-Should-Be-Reasonable.pdf)
