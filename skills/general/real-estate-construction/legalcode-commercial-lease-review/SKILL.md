---
name: legalcode-commercial-lease-review
description: Review commercial lease agreements clause-by-clause against a Letter of Intent and market
  benchmarks — flag deviations, generate confidence-scored redlines, and produce an auditable analysis
  covering base rent and escalation, CAM charges and reconciliation rights, tenant improvement allowances,
  personal guarantees and good-guy clauses, use restrictions and exclusivity, assignment and subletting
  rights, default and cure periods, landlord access and relocation rights, insurance requirements, environmental
  obligations, ADA/accessibility compliance, holdover provisions, and early termination and contraction
  options. Use when reviewing office, retail, or industrial leases; comparing executed lease terms against
  LOI commitments; or evaluating landlord-side or tenant-side risk exposure before signing, renewal, or
  dispute.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Review commercial lease agreements clause-by-clause against a Letter of Intent and market benchmarks — flag deviations, generate confidence-scored redlines, and produce an auditable analysis covering base rent and escalation, CAM charges and reconciliation rights, tenant improvement allowances, personal guarantees and good-guy clauses, use restrictions and exclusivity, assignment and subletting rights, default and cure periods, landlord access and relocation rights, insurance requirements, environmental obligations, ADA/accessibility compliance, holdover provisions, and early termination and contraction options. Use when reviewing office, retail, or industrial leases; comparing executed lease terms against LOI commitments; or evaluating landlord-side or tenant-side risk exposure before signing, renewal, or dispute. Jurisdiction-aware for US, UK, and Australia with [JURISDICTION-SPECIFIC] markers for all jurisdiction-dependent rules. GREEN/YELLOW/RED classification with redlines for tenant-favorable and landlord-favorable positions. Produces Glass Box audit trail, negotiation priority tiers, and stakeholder impact map.


# Legalcode Commercial Lease Review

> **Disclaimer**: This skill provides a framework for AI-assisted commercial lease review.
> It does not constitute legal advice. All outputs should be reviewed by a qualified legal
> professional licensed in the relevant jurisdiction before reliance. Laws and regulations
> governing commercial leases vary significantly by jurisdiction and change frequently —
> verify current applicability before relying on any provision described here. Statutory
> and case law references cited from memory carry hallucination risk — verify against
> authoritative sources before relying on them.

## Purpose and Scope

This skill reviews commercial lease agreements clause-by-clause against a Letter of Intent
(LOI), organizational playbook, or general market standards. It identifies deviations,
classifies their severity, detects LOI drift (terms agreed in negotiation that were altered
during drafting), generates actionable redline suggestions, and produces a confidence-scored,
auditable analysis with a negotiation priority framework.

**Covers:**

- Clause-by-clause analysis of office, retail, industrial, and mixed-use commercial leases
- LOI vs. executed lease delta analysis (first-class step, not an afterthought)
- GREEN / YELLOW / RED deviation classification with confidence scoring
- Redline generation with tenant-favorable and landlord-favorable positions
- 14 lease clause categories (7 deep, 7 standard)
- Missing clause detection and gap analysis
- Negotiation priority tiers (Tier 1 / Tier 2 / Tier 3)
- Stakeholder impact mapping (tenant, landlord, guarantors, lenders, insurers)
- Business impact assessment for each material deviation
- Quality-verified output with Glass Box audit trail
- Jurisdiction-aware analysis for US, UK, and Australia

**Does not:**

- Draft new leases from scratch (see `legalcode-saas-agreement-drafter` for SaaS-specific drafting patterns)
- Provide legal advice or replace qualified real estate counsel
- Apply to residential leases, ground leases, or agricultural leases
- Substitute for a formal title search, survey, or environmental site assessment

**Related skills:**

- `legalcode-contract-review` — General commercial contract review (non-lease)
- `legalcode-redline-generator` — Standalone redline generation for any contract
- `legalcode-obligation-tracker` — Track ongoing lease obligations and milestone dates
- `legalcode-indemnification-analysis` — Deep indemnification analysis applicable to lease indemnity clauses

---

## Jurisdiction and Governing Law

This is a jurisdiction-aware skill with primary coverage for US, UK, and Australia. The
lease's own governing law clause determines which legal framework applies. The review
identifies the governing law early and adapts the analysis accordingly.

[JURISDICTION-SPECIFIC] When localizing for a specific jurisdiction, research and apply:

**United States:**

- State landlord-tenant acts (California, New York, Texas, Florida, Illinois have significant variations)
- CERCLA (42 U.S.C. § 9601 et seq.) environmental liability and lender liability
- Americans with Disabilities Act (42 U.S.C. § 12101) — shared landlord/tenant compliance duties
- IRC § 467 for deferred rent and below-market or above-market rent issues
- State rent control ordinances (San Francisco, New York City, Seattle)
- State-specific security deposit limits and handling requirements
- State usury and penalty clause limits on holdover penalties
- FIRPTA (26 U.S.C. § 1445) if landlord is a foreign entity
- UCC Article 2A for embedded lease financing structures

**United Kingdom:**

- Landlord and Tenant Act 1954 (security of tenure for business tenants) — [VERIFY break clauses must be strictly complied with]
- Landlord and Tenant Act 1988 (consent to assignment/subletting — reasonableness standard)
- RICS Code for Leasing Business Premises 2020 (market standard for full repairing and insuring (FRI) leases)
- Landlord and Tenant (Covenants) Act 1995 (tenant liability on assignment)
- Equality Act 2010 (accessibility and adjustment obligations)
- Environmental Protection Act 1990 and Environmental Act 2021
- Commercial Rent (Coronavirus) Act 2022 (historical protected rent arrears)
- SDLT/LTT/LBTT on lease premiums and first-year rent — flag if not addressed

**Australia:**

- Retail Leases Act (NSW 1994, VIC 2003, QLD 1994, WA 1985, SA 1995, TAS 1993 — significant variation)
- The Franchising Code of Conduct (if tenant is a franchisee)
- PPSA (Personal Property Securities Act 2009) — for any security interest granted by tenant
- Work Health and Safety Act 2011 (Cth) — shared premises obligations
- Competition and Consumer Act 2010 (Australian Consumer Law — unfair contract terms)
- State environmental protection legislation (EPBC Act, state EPAs)
- GST Act 1999 — check whether rent and outgoings are GST-inclusive or exclusive

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the direction or tone of the analysis
- Tenant-side vs. landlord-side framing requires opposite severity classifications
- LOI commitments are absent or ambiguous
- Lease type materially affects clause interpretation
- Risk tolerance or business context is needed to classify severity correctly

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

### Step 1: Accept the Lease

Accept the lease in any of these formats:

- **File**: PDF, DOCX, or other document format
- **URL**: Link to a lease in a CLM, cloud storage, or document system
- **Pasted text**: Lease text pasted directly into the conversation

If no lease is provided, prompt the user to supply one.

### Step 2: Accept the Letter of Intent (LOI)

**⟁ CLARIFY** — Was a Letter of Intent signed before the lease?

1. **LOI available**: Provide the LOI (file, URL, or text) so the review can flag any
   LOI-to-lease drift.
   - _Why this matters_: The single most common commercial lease error is terms agreed
     in the LOI silently changing during drafting — free rent periods shortened, TIA
     amounts reduced, renewal options disappearing. A delta check catches this immediately.
2. **No LOI**: Proceed without LOI comparison. The review will use market benchmarks only.
3. **LOI exists but unavailable**: Note this. Flag any clause where an LOI commitment is
   commonly negotiated (rent, TIA, renewal options, etc.) and recommend the user obtain
   the LOI before execution.

### Step 3: Gather Context

**⟁ CLARIFY** — Before beginning the review, ask:

1. **Which side are you on?**
   - Options: **Tenant** (default — most common use case), **Landlord**
   - _Why this matters_: The entire severity classification flips. A missing TIA cap is
     RED for the tenant and GREEN for the landlord. State assumptions if user skips this.

2. **Lease type?**
   - Options: **Office**, Retail / Shopping Center, Industrial / Warehouse, Mixed-Use,
     Ground Lease (note: ground lease analysis is outside this skill's scope)
   - _Why this matters_: Retail leases trigger percentage rent, exclusivity, co-tenancy,
     and Retail Leases Act protections (AU). Industrial leases have different maintenance
     and environmental profiles. Office leases have specific CAM and operating expense
     structures.

3. **Property jurisdiction?**
   - Options: US (specify state), UK (England & Wales, Scotland, Northern Ireland), Australia
     (specify state/territory), Other
   - _Why this matters_: Determines applicable landlord-tenant statutes, required disclosures,
     security of tenure rights (UK), and Retail Leases Act obligations (AU).

4. **Review basis?**
   - Options: We have an **organizational playbook** (provide it), Use **general market
     standards** (skill uses research-backed benchmarks), Start minimal — flag only
     **critical risks**
   - _Why this matters_: Playbook-based review is more precise; market-standards review
     is jurisdiction-aware but not org-specific.

5. **Lease term and deal size?** (Optional — assists with proportionality of analysis)
   - Term length (years), approximate aggregate rent commitment (if known)
   - _Why this matters_: A 10-year lease at $10M aggregate requires more scrutiny on
     escalation, renewal, and termination than a 2-year short-form lease.

6. **Risk tolerance?**
   - Options: **Conservative** (flag all deviations), **Pragmatic** (flag material
     deviations only), **Deal-centric** (flag only deal-breakers)
   - _Why this matters_: Calibrates the YELLOW/RED threshold without changing legal analysis.

### Step 4: Load Playbook or Market Standards

**If a playbook is provided:**

1. Read the playbook to extract the organization's standard positions for each of the
   14 clause categories.
2. Note any clause types the playbook does not address — treat those as "general market
   standards" fallbacks.
3. Confirm playbook jurisdiction alignment with the lease's governing law.

**If no playbook is provided (general market standards mode):**

1. Use the jurisdiction-specific research conducted in Step 5 to establish market baselines.
2. State the benchmarks used explicitly in the output (e.g., "BOMA 2024 standards for
   office gross-up," "RICS Code for Leasing 2020 for FRI lease scope").
3. Document all benchmarks in the Glass Box audit trail.

**Playbook fallback defaults:**

| Clause Category         | Tenant-Favorable Benchmark                                                                                                               |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Base rent               | At or below market; CPI-capped escalations; no mid-term landlord-initiated reset                                                         |
| CAM charges             | Cap at 3-5% controllable cost increase/year; exclude capital expenditures; audit right                                                   |
| TIA                     | Full build-out cost covered; disbursed in tranches on milestone; not conditional on tenant's good standing beyond reasonable             |
| Personal guarantee      | Limited (rolling or good-guy) guarantee; capped at 6-12 months' rent; terminates on lease assignment approval                            |
| Use restriction         | Broad permitted use; exclusivity protection against competing tenants                                                                    |
| Assignment / subletting | Landlord consent not unreasonably withheld; deemed consent after 20 business days                                                        |
| Default / cure          | 5-day notice for monetary default (with 2 cure opportunities/year); 30-day notice for non-monetary; complex cure chain for non-monetary  |
| Landlord access         | 48-hour notice except emergency; no relocation right without tenant consent                                                              |
| Insurance               | Market-standard limits; mutual waiver of subrogation; tenant as additional insured on landlord's policy                                  |
| Environmental           | Landlord represents no existing contamination; tenant not responsible for pre-existing conditions                                        |
| ADA                     | Landlord responsible for common areas and existing structural elements; tenant responsible only for tenant-specific fit-out improvements |
| Holdover                | Month-to-month holdover at 110-125% of base rent; no automatic multi-year renewal trigger                                                |
| Early termination       | Buyout at 3-6 months' rent + unamortized TIA + landlord's brokerage; not conditional on replacement tenant                               |
| Renewal options         | Personal and assignable to approved assignee; market rent reset with binding arbitration mechanism                                       |

### Step 5: Research Jurisdiction-Relevant Legal Authority

Before clause-by-clause analysis, gather jurisdiction-relevant legal authority.

**With legalcode-mcp connected:**

1. Search for landlord-tenant statutes in the governing jurisdiction
2. Search for leading cases on lease enforceability, rent control, and tenant protections
3. Search for regulatory guidance on ADA/accessibility, environmental disclosure, and insurance
4. Save results to `/tmp/legalcode-commercial-lease-research.md`

**Without legalcode-mcp (preferred fallback):**

1. Use Perplexity search (see skill: `perplexity-search`) for jurisdiction-specific landlord-tenant law
2. Run targeted queries: `[jurisdiction] commercial lease tenant rights statute 2024 2025`
3. Mark all statutory and case law references in the analysis with **[VERIFY]**
4. Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`

**Key research areas by jurisdiction:**

| Jurisdiction    | Priority Research Topics                                                                                                                                                          |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US (all states) | State-specific landlord-tenant act; security deposit rules; holdover penalty limits; ADA enforcement risk                                                                         |
| US (CA)         | Civil Code §§ 1941-1942 (habitability); Oakland/SF rent control applicability to commercial; Proposition 65 (hazmat disclosure); AB 434 / Title 24 energy compliance              |
| US (NY)         | NYC Admin. Code § 22-902 (commercial tenant protections); RPL § 227-e (lease remediation); NYC energy benchmarking (LL84)                                                         |
| UK              | LTA 1954 — whether tenant has opted in or out of security of tenure; SDLT on NPV of rent; MEES (Energy Act 2011 — minimum EPC rating for commercial premises from 2023/2025)      |
| AU              | Retail Leases Act applicability (threshold annual rent and use type varies by state); PPSA security interest registration; Work Health and Safety Act shared-premises obligations |

### Step 6: LOI vs. Lease Delta Analysis

If an LOI was provided in Step 2, conduct a dedicated LOI-to-lease drift check before
clause-by-clause analysis.

**For each LOI commitment, verify that the executed lease:**

1. Reflects the agreed base rent and rent-free period exactly
2. Reflects the agreed TIA amount, disbursement mechanism, and scope
3. Preserves any renewal options, expansion rights, or rights of first offer/refusal
4. Preserves the agreed lease commencement date and any conditions precedent
5. Reflects the agreed landlord work obligations
6. Reflects any agreed exclusivity, use protections, or co-tenancy requirements
7. Does not add obligations not present in the LOI (guarantees, caps, restrictions)

**LOI Drift Classification:**

| Delta Type                                                    | Severity                              |
| ------------------------------------------------------------- | ------------------------------------- |
| Material financial term changed (rent, TIA, free rent period) | RED — escalate immediately            |
| Tenant right removed or narrowed (renewal, expansion, ROFR)   | RED                                   |
| Landlord obligation removed or weakened                       | YELLOW / RED                          |
| Administrative term changed (notice address, payment account) | YELLOW                                |
| New obligation added for tenant not in LOI                    | YELLOW / RED depending on materiality |
| Drafting clarification of an LOI ambiguity                    | GREEN (if consistent with LOI intent) |

Present the LOI delta in a table before the clause-by-clause analysis:

```
| LOI Commitment | Lease Provision | Delta | Severity |
|----------------|-----------------|-------|---------|
| [term]         | [provision]     | [difference] | GREEN / YELLOW / RED |
```

### Step 7: Clause-by-Clause Analysis

Analyze the lease across the 14 clause categories below. Follow the deep vs. standard
depth protocol:

**Deep analysis** (full statutory / market analysis, multi-pass review, self-interrogation for RED items):
Categories 1, 2, 3, 4, 7, 9, 10

**Standard analysis** (presence / reasonableness check, market benchmark comparison):
Categories 5, 6, 8, 11, 12, 13, 14

---

#### Category 1: Base Rent and Escalation Provisions (DEEP)

**What to analyze:**

- Base rent amount vs. market (if knowable from context or LOI)
- Escalation mechanism: fixed percentage (common 2-3% annually), CPI-indexed, fair
  market value reset, or landlord-determined increase
- Frequency of escalation: annual vs. multi-year
- Timing of first escalation (year 1 or year 2?)
- Effective date definition and free-rent period alignment
- Gross lease vs. net lease vs. triple-net — implications for rent definition
- Percentage rent provisions (retail only): sales breakpoint calculation, reporting
  requirements, audit rights over percentage rent
- Base year establishment for expense stops (full-service/gross leases)

**Common issues to flag:**

- CPI escalation with no cap (unlimited exposure in high-inflation environments)
- Mid-term fair market value reset with no binding arbitration mechanism — RED
- Base year expense stop set in an abnormally low-expense year (pandemic year) — RED
- Gross-up adjustment for vacant space in base year — tenant often not aware this inflates base year
- Percentage rent breakpoint set too low (triggers too early) — RED for retail tenants

[JURISDICTION-SPECIFIC] Research current market rent for the property type and submarket.
In the UK, rent review clauses commonly use upward-only open market rent review — flag as
[VERIFY] whether the RICS Code recommends alternatives. In AU, retail leases in most states
cap CPI rent increases; verify applicable Retail Leases Act provisions. [VERIFY]

---

#### Category 2: Common Area Maintenance (CAM) Charges and Reconciliation Rights (DEEP)

**What to analyze:**

- CAM definition: which expenses are included (management fees, capital expenditures,
  marketing, reserves, property taxes, insurance)?
- Controllable vs. non-controllable expense distinction
- Annual CAM cap on controllable costs (market standard: 3-5% per year, cumulative or non-cumulative)
- Base year for CAM (same issues as rent base year)
- Gross-up provision: can landlord gross up to 95-100% occupancy?
- Exclusions: capital expenditures (unless amortized per useful life and directly benefiting tenant),
  depreciation, leasing commissions, landlord's income tax, costs of correcting landlord's
  defects, legal fees for other tenant disputes
- Audit rights: tenant's right to audit CAM within 12-24 months after year-end reconciliation
- Reconciliation timeline: landlord's obligation to deliver annual CAM statement (typically
  within 90-120 days after year-end)
- Estimated vs. actual payments mechanism
- Pro-rata share calculation: tenant's rentable area / total rentable area (verify denominator)

**Common issues to flag:**

- No CAM cap (unlimited exposure on controllable costs) — RED
- Capital expenditures included without amortization — RED
- Management fee: landlord charging market-rate fee without cap (market: 3-5% of gross revenues) — YELLOW
- No audit right — YELLOW / RED depending on lease size
- Reconciliation statement delivery obligation not specified — YELLOW
- Gross-up clause: verify tenant pays for vacant space (landlord, not tenant, should absorb vacancy) — RED
- No exclusion for prior-year deficiencies (landlord cannot backfill shortfalls into current year) — RED

[JURISDICTION-SPECIFIC] In the UK, service charge transparency is governed by the RICS
Service Charge Code for Commercial Property (3rd ed., 2018). In AU, retail lease outgoings
disclosure requirements vary by state; NSW requires a Disclosure Statement before execution.
[VERIFY]

---

#### Category 3: Tenant Improvement Allowance (TIA) and Construction Obligations (DEEP)

**What to analyze:**

- TIA amount per square foot (market ranges: office $50-150/RSF, retail $40-100/RSF, industrial $15-40/RSF in major US markets — [VERIFY current benchmarks])
- What TIA covers: hard costs only, or hard + soft costs (architecture, permits, FF&E, cabling)?
- Disbursement mechanism: lump sum, milestone-based, or reimbursement after completion?
- Conditions for disbursement: reasonable (lien wavers, inspections) vs. onerous (tenant must not be in default)
- TIA forfeiture: can landlord claw back unamortized TIA on early termination?
- Landlord's Work: what is landlord obligated to deliver (shell condition, HVAC, base building systems)?
- Completion deadline and remedies for delay (free rent extension, termination right?)
- Landlord's contractor vs. tenant's contractor: who controls construction?
- Over-allowance: who pays costs above the TIA? Responsibility for cost overruns
- Reimbursement vs. direct payment to contractor — tax implications

**Common issues to flag:**

- TIA conditioned on tenant not being in default at time of disbursement — YELLOW / RED
  (tenant may need TIA to open; minor technical default should not trigger forfeiture)
- No outside delivery date for landlord's work with termination right — RED
- Broad unamortized TIA clawback on any tenant default (not just voluntary termination) — RED
- No lien protection for tenant (landlord construction liens attach to leasehold) — RED
- Tenant's architect approval right: landlord veto over tenant's design professional — YELLOW

[JURISDICTION-SPECIFIC] In the UK, construction and fit-out obligations are typically
governed by the lease's dilapidations clause; verify whether the lease contemplates
reinstatement at end of term. In AU, check whether fit-out works require development approval
or building permit under state planning legislation. [VERIFY]

---

#### Category 4: Personal Guarantees and Good-Guy Clauses (DEEP)

**What to analyze:**

- Guarantor identity: principals, parent entity, or third-party guarantor?
- Scope of guarantee: full unconditional guaranty vs. limited guaranty
- Duration: perpetual, co-terminus with lease, or rolling/burning-off structure?
- Cap: dollar-limit or time-limit on guarantor's exposure?
- Good-Guy clause structure (if present):
  - Notice period required (typically 3-6 months)
  - Conditions for release: proper notice, current on all payments, vacancy in broom-clean condition
  - Guarantor liability cap post good-guy trigger
- Guarantee release on assignment: does guarantee terminate if tenant assigns to creditworthy assignee?
- Death or disability of individual guarantor: automatic release or continuation?
- Remedies: does landlord need to pursue tenant first before calling on guarantor (exhaustion requirement)?
- Guaranty enforceability under governing law: note jurisdiction-specific defenses (community property, spousal consent)

**Common issues to flag:**

- Perpetual full unconditional guaranty with no cap or time limit — RED
- No good-guy option for early exit — YELLOW
- Guarantee survives full lease assignment to creditworthy entity — YELLOW / RED
- Guaranty of obligations that extend beyond lease term (e.g., holdover, damages) — RED
- Individual guarantor (sole proprietor) without spousal consent where required — [VERIFY jurisdiction]
- No termination right for guarantor if lease is modified without consent — YELLOW

[JURISDICTION-SPECIFIC] In Australia, guarantees may engage the PPSA if structured as a
security interest; check registration obligations under PPSA Part 2.2. In the UK, guarantee
law is governed by case law principles; surety defenses (material variation without consent)
are well-established — [VERIFY Holme v Brunskill (1878)]. In the US, state-specific rules on
guaranty enforceability vary widely; California has anti-deficiency rules; New York has
specific guaranty validity requirements. [VERIFY]

---

#### Category 5: Use Restrictions and Exclusivity Provisions (STANDARD)

**What to analyze:**

- Permitted use definition: broad (any lawful use) vs. narrow (specific to current business)?
- Exclusivity: does tenant have exclusive right to operate in a specific category within the project?
- Exclusivity scope: precisely defined (avoiding over/under-breadth), existing tenant carve-outs
- Co-tenancy rights (retail): what happens if anchor tenant vacates?
- Use change procedure: can tenant change use without landlord consent?
- Prohibited uses: restricted uses (gambling, adult entertainment, hazardous materials) that restrict tenant
- Operating covenants: is tenant required to remain open and operating? (Retail — significant risk)

**Common issues to flag:**

- Operating covenant without exclusivity protection — RED (tenant bears obligation without protection)
- Permitted use so narrow it prevents business evolution — YELLOW
- Exclusivity without remedy (e.g., no rent abatement or termination right on breach) — YELLOW
- Co-tenancy trigger not defined or remedy inadequate — YELLOW
- Operating hours requirement without limitation for emergency or remodeling — YELLOW

[JURISDICTION-SPECIFIC] In AU, Retail Leases Acts in NSW, VIC, QLD prohibit landlords from
requiring tenants to observe specified trading hours in certain cases. UK does not have specific
exclusivity protections in statute; governed by lease terms only. [VERIFY]

---

#### Category 6: Assignment and Subletting Rights (STANDARD)

**What to analyze:**

- Assignment right: absolute prohibition vs. consent required vs. right to assign to affiliates
- Landlord consent standard: "sole discretion" vs. "not to be unreasonably withheld or delayed"
- Deemed consent: does silence after X business days constitute consent?
- Processing timeline: landlord response obligation (market: 15-30 business days)
- Recapture right: can landlord recapture space from tenant rather than consenting to assignment?
- Profit-sharing on assignment: does landlord share in assignment premium?
- Affiliate exception: free assignment to parent, subsidiary, or successor by merger
- Original tenant guaranty survival: does original tenant remain liable post-assignment?
- Subletting rights: sub-subletting, subletting to affiliates, subletting obligations

**Common issues to flag:**

- No deemed consent provision — YELLOW
- Landlord can refuse consent for any reason ("sole discretion") — RED
- Recapture right without fair compensation mechanism — RED
- Assignment premium 100% to landlord — YELLOW (market: landlord shares 50%)
- Original tenant remains liable indefinitely post-assignment — YELLOW

[JURISDICTION-SPECIFIC] UK: Landlord and Tenant Act 1988 requires landlord to provide
consent or withhold consent with reasons within a reasonable time. [VERIFY] AU: Retail
Leases Acts typically require landlord to consent or withhold consent with reasons within
28 days. [VERIFY state-specific timeframes]

---

#### Category 7: Default Provisions and Cure Periods (DEEP)

**What to analyze:**

- Monetary default notice and cure period: typical market is 3-5 days notice + 5 business
  days cure; verify what lease provides
- Non-monetary default notice and cure period: market is 30 days notice + cure obligation
  (with extension for complex cure requiring more time)
- Complex cure chain: should allow cure if tenant commences cure within 30 days and
  diligently pursues to completion (no hard outside date without landlord consent)
- Constructive eviction: does lease define conditions?
- Cross-default: does default under other leases with same landlord trigger cross-default?
- Landlord's default and tenant's remedies: notice period + cure period for landlord default
- Landlord default rent abatement: does tenant have right to abate rent on landlord failure to deliver services?
- Self-help right: can tenant cure landlord default and offset costs against rent?
- Bankruptcy protections: 11 U.S.C. § 365 (US) — rejection, assumption, and the impact on
  the lease in bankruptcy of either party
- Lockout: can landlord lock out tenant without court order? (Jurisdiction-specific rules)

**Common issues to flag:**

- No non-monetary default cure period beyond 30 days for complex remediation — RED
- Cross-default triggered by any breach (including minor technical breach) of other leases — RED
- No landlord default provision or remedy — RED (tenants have no recourse for landlord failure)
- Self-help right absent (tenant has no mechanism to cure landlord default without court) — YELLOW
- Automatic renewal of default notice waiver: if tenant accepts notice, does cure period restart? — YELLOW
- Constructive eviction doctrine unavailable (lease waives it) — RED

[JURISDICTION-SPECIFIC] US: Lockout without court order is prohibited in most states
(TX is a notable exception — TPC § 93.002 allows commercial lockout with specific procedures).
UK: Forfeiture law is complex; landlords must serve Section 146 notice (LPA 1925) before
forfeiture; waiver by acceptance of rent is a key trap. [VERIFY] AU: State landlord-tenant
acts govern re-entry procedures; WA Commercial Tenancy (Retail Shops) Agreements Act 1985
sets specific requirements. [VERIFY state-specific]

---

#### Category 8: Landlord Access and Relocation Rights (STANDARD)

**What to analyze:**

- Landlord access notice requirement: market standard is 48 hours; verify
- Emergency access exception: properly defined?
- Access scope: inspection, maintenance, showing to prospective tenants/purchasers
- Relocation right: can landlord relocate tenant to different space?
- Relocation conditions: notice period, comparable space standard, landlord pays costs?
- Relocation remedy: right to terminate if relocated space is not comparable?
- Substitution right: landlord can substitute comparable space during construction

**Common issues to flag:**

- Landlord access without notice requirement — YELLOW
- Unlimited relocation right with no comparable space standard — RED
- Relocation without moving cost reimbursement — RED
- No termination right if relocation space is not comparable — YELLOW

---

#### Category 9: Insurance Requirements (DEEP)

**What to analyze:**

- Tenant's required coverages: CGL, property, workers' compensation, business interruption
- CGL limits: market standard $1M per occurrence / $2M aggregate (higher for retail,
  hospitality, and medical use — $2-5M)
- Property insurance: replacement cost value vs. stated value; who insures tenant improvements?
- Business interruption: coverage period (market: 12 months minimum)
- Umbrella/excess liability: landlord may require umbrella if base limits are below threshold
- Additional insured: landlord and property manager named as additional insured on CGL
- Waiver of subrogation: mutual waiver so neither party's insurer can subrogate against the other
- Certificate delivery obligations: timing, form (ACORD 25 in US), and cancellation notice
- Landlord's insurance: what is landlord required to carry? (All-risk property; CGL; loss of rents)
- Who insures tenant improvements (TI): landlord's policy or tenant's policy?
- Insurance proceeds: in the event of casualty, who receives proceeds and how are they applied?

**Common issues to flag:**

- No mutual waiver of subrogation — RED (either party's insurer can sue the other)
- Landlord not required to carry property insurance on the building — RED
- Tenant required to insure TI improvements at replacement cost: who built them (landlord's contractor)?
  If landlord built and paid for TI, landlord's policy should cover — YELLOW
- No cross-liability coverage in additional insured endorsement — YELLOW
- Cancellation notice: ACORD 25 no longer guarantees 30 days cancellation notice; verify endorsement — YELLOW

[JURISDICTION-SPECIFIC] UK: Insurance in FRI leases typically placed by landlord with tenant
paying a proportionate share of premiums. Verify adequate reinstatement valuation.
AU: Workers' Compensation insurance requirements vary by state; WorkCover/WorkSafe premiums
are employer obligations. [VERIFY]

---

#### Category 10: Environmental Obligations (DEEP)

**What to analyze:**

- Landlord's representation: no existing contamination, Hazardous Substances not stored at premises
- Tenant's environmental covenant: limitation on storage/use of Hazardous Substances to
  ordinary office supplies or specifically defined chemicals
- Pre-existing conditions: tenant not responsible for pre-existing contamination
- Environmental indemnification: mutual indemnification structure (each party responsible for
  contamination they cause)
- Phase I/II ESA: has one been conducted? Results provided to tenant?
- Reporting obligations: tenant's obligation to notify landlord of spills or releases
- Remediation: if contamination discovered, who remediates and who bears cost?
- Underground storage tanks (USTs): are there USTs on the property? If so, landlord should represent USTs are in compliance
- HVAC/MERV filtration: is landlord required to maintain specific air quality standards?
- Asbestos and mold: landlord representation regarding asbestos-containing materials (ACM) and prior mold remediation

**Common issues to flag:**

- No landlord representation that no hazardous materials have been stored/released — RED
- Tenant broadly responsible for all environmental remediation regardless of cause — RED
- No pre-existing condition carve-out for tenant's environmental liability — RED
- Landlord's Phase I ESA not provided to tenant pre-execution — YELLOW
- No mold/asbestos representation from landlord for older buildings — YELLOW

[JURISDICTION-SPECIFIC] US: CERCLA § 107(a) owner/operator liability; "Innocent Landowner"
defense requires Phase I ESA pre-acquisition (ASTM E1527-21). California: Proposition 65
requires notice of chemicals exceeding established thresholds. [VERIFY] UK: Environmental
Protection Act 1990 Part IIA contaminated land regime; Environment Agency guidance on
Commercial Property Survey practice. [VERIFY] AU: State EPAs govern contaminated land;
PFAS contamination liability is a current enforcement priority. [VERIFY]

---

#### Category 11: ADA/Accessibility Compliance Responsibilities (STANDARD)

**What to analyze:**

- Who is responsible for ADA/accessibility compliance in common areas vs. leased premises?
- Market standard: landlord is responsible for common areas, paths of travel, parking,
  and the building's structural and base-building elements; tenant is responsible for
  tenant-specific fit-out within the leased premises
- Lease allocation: does it mirror market standard or shift all obligations to tenant?
- Ongoing vs. initial compliance: lease should not shift landlord's ongoing common area
  compliance obligations to tenant
- Cost allocation for accessibility improvements during tenant's construction

**Common issues to flag:**

- Lease places full ADA compliance responsibility on tenant including common areas — RED
- No carve-out for pre-existing structural conditions — RED
- Tenant required to bring base building systems into ADA compliance — RED

[JURISDICTION-SPECIFIC] US: ADA Title III — both landlord and tenant can be liable
regardless of lease allocation; courts will not permit lease to eliminate one party's
ADA liability entirely. [VERIFY] UK: Equality Act 2010 — duty to make reasonable adjustments
applies to both landlord and tenant depending on who controls the relevant area. [VERIFY]
AU: Disability Discrimination Act 1992 (Cth) — similar dual-liability framework. [VERIFY]

---

#### Category 12: Holdover Provisions (STANDARD)

**What to analyze:**

- Holdover rate: market is 110-150% of base rent (monthly); some leases specify 150-200%
  after initial holdover period
- Notice required for holdover: tenant obligates landlord to accept holdover or not?
- Month-to-month vs. year-to-year: what type of tenancy does holdover create?
- Landlord's remedies: consequential damages for extended holdover (e.g., loss of new
  tenant deal) — is tenant exposed to lost-deal damages?
- Right to terminate during holdover: either party's notice period
- Constructive holdover: if tenant fails to deliver in proper condition, does holdover clock start?

**Common issues to flag:**

- Holdover rate exceeds 150% without stepped increase — YELLOW
- Holdover at 200% from day 1 without any grace period — RED
- Tenant liable for consequential damages including landlord's lost deals without cap — RED
- Year-to-year holdover tenancy created without tenant's affirmative election — RED
  (can trap tenant in extended lease at high rate)

---

#### Category 13: Early Termination and Contraction Options (STANDARD)

**What to analyze:**

- Termination right: absolute right vs. conditional on triggering event (key person departure,
  financial covenant, demolition/redevelopment)?
- Termination fee: buyout formula (unamortized TIA + leasing commissions + free rent +
  rent to end of term? Or fixed number of months?)
- Notice period for termination right exercise
- Effective date: how far in advance can tenant terminate?
- Contraction option: right to reduce space by a specific amount
- Contraction fee: typically based on unamortized economics of the surrendered space
- ROFO/ROFR (Right of First Offer/Refusal): does tenant have the right to additional space?
- Demolition/redevelopment clause: landlord's right to terminate early for demolition;
  tenant's protections (notice period, relocation, replacement space)?
- Death or disability clause for solo occupants

**Common issues to flag:**

- No termination right at all — YELLOW for long-term leases (>5 years)
- Termination fee formula requires payment of full remaining rent (not just unamortized economics) — RED
- Demolition/redevelopment clause with insufficient notice period (< 12 months) — RED
- No obligation on landlord to offer relocation space on redevelopment — YELLOW

---

#### Category 14: Renewal Options and Rights of First Offer/Refusal (STANDARD)

**What to analyze:**

- Renewal term: number and duration of renewal options
- Rent on renewal: fixed, fair market value, CPI, or blended?
- Fair market value reset: how is it calculated? Who determines it? Binding arbitration mechanism?
- Option personal or assignable: can assignee exercise renewal option?
- Conditions to exercise: tenant must not be in default at time of exercise? (Some condition is market-standard; requiring "not ever been in default" is not)
- Exercise notice period: typically 9-12 months prior to term expiration
- Right of First Offer (ROFO): tenant has first right to lease additional space when it becomes available
- Right of First Refusal (ROFR): tenant can match any third-party offer for additional space
- Expansion option: tenant's right to lease additional space at pre-negotiated terms

**Common issues to flag:**

- Fair market rent reset with no binding arbitration mechanism — RED (landlord-controlled determination)
- Renewal option cannot be exercised if tenant has ever been in default — YELLOW (should be "not currently in monetary default")
- No renewal option at all for leases > 5 years — YELLOW
- ROFO not triggering on space adjacent to tenant's premises — YELLOW

---

## Classification System

Apply GREEN / YELLOW / RED classification to each finding in each clause category.

### GREEN — Acceptable

The provision:

- Aligns with the organizational playbook or general market standards
- Represents a minor variation that is commercially reasonable
- Does not materially increase the reviewing party's risk
- May be noted for awareness but requires no negotiation

**Action**: Note with confidence score. No redline required.

### YELLOW — Negotiate

The provision:

- Falls outside the organizational playbook or general market standards
- Is common in the market but not preferred
- Represents moderate risk that is negotiable
- Requires a redline with a primary position and fallback

**Action**: Generate full redline (clause / current language / proposed / rationale /
legal basis / priority / fallback). Identify as Tier 2 or Tier 3 in negotiation tiers.

### RED — Escalate

The provision:

- Falls materially outside acceptable range or triggers an escalation criterion
- Exposes the reviewing party to significant financial, legal, or operational risk
- May be legally unenforceable or in violation of applicable statute
- Requires senior review, business decision, or legal counsel input before proceeding

**Automatic RED triggers (tenant-side):**

- Uncapped CAM charges with no controllable expense cap
- No cure period for monetary default
- Landlord's unilateral right to relocate without comparable space guarantee
- No environmental pre-existing condition carve-out
- TIA conditioned on tenant maintaining zero defaults throughout construction
- All ADA compliance obligations shifted to tenant
- Holdover at >150% with consequential damage exposure
- No binding mechanism for fair market rent determination on renewal
- Termination fee = full remaining rent obligations
- Cross-default clause covering unrelated properties

**Confidence thresholds:**

- RED classification requires confidence ≥ 0.80 that the issue is material
- YELLOW classification requires confidence ≥ 0.60
- Below 0.60: flag as uncertain and recommend professional counsel review

---

## Prioritization Framework

### Tier 1 — Must-Haves (Deal Breakers)

Issues where the reviewing party cannot proceed without resolution. Concession requires
escalation to leadership or walk-away consideration.

**Examples (tenant-side):**

- No monetary default cure period
- Full uncapped environmental liability for pre-existing conditions
- Landlord's unilateral rent reset with no arbitration mechanism
- TIA forfeiture on any technical default

**Strategy**: Lead with Tier 1 issues. Do not trade them. Escalate if landlord refuses.

### Tier 2 — Should-Haves (Strong Preferences)

Issues that materially affect risk but where negotiation room exists. Trade Tier 3
concessions to win Tier 2 items.

**Examples (tenant-side):**

- CAM cap from 5% to 3% per year
- Assignment consent deemed after 20 vs. 30 business days
- Renewal rent reset with binding arbitration (vs. appraisal only)
- Good-guy clause in lieu of full perpetual guarantee

**Strategy**: Prioritize highest-dollar-impact items. Offer Tier 3 concessions in exchange.

### Tier 3 — Nice-to-Haves (Concession Candidates)

Issues improving position but acceptable to concede strategically.

**Examples (tenant-side):**

- Specific notice delivery method preferences
- Additional insured endorsement form specification
- Phase I ESA format requirements
- Governing state of guarantee (if landlord's jurisdiction is acceptable)

**Strategy**: Concede these readily to secure Tier 1 and 2 wins.

---

## Quality Frameworks

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before delivering.

| Gate           | Rule                                                                           | Fail Action                                              |
| -------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------- |
| **Source**     | Every legal claim cites specific statute, regulation, or established principle | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations use consistent, recognizable format for jurisdiction             | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments or repeal                         | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within lease's governing law scope; no jurisdictional bleed     | Remove or flag jurisdiction creep                        |
| **Confidence** | Uncertainty explicitly stated, not hidden                                      | Add confidence qualifier                                 |

**Lease-specific additional gates:**

| Gate                   | Rule                                                                             | Fail Action                                              |
| ---------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **LOI Integrity**      | Any LOI commitment must be verified against lease before classification          | Flag as "[LOI COMPARISON REQUIRED]" if LOI not available |
| **Statutory Override** | Check for mandatory landlord-tenant statute provisions that override lease terms | Flag as "[STATUTORY OVERRIDE — VERIFY]"                  |

### Self-Interrogation for RED Items

For any item classified RED, apply this 3-pass review before delivery:

**Pass 1 — Legal Chain Integrity**: Does the risk assessment follow logically from the cited
authority? Would a court in this jurisdiction actually reach this conclusion? What is the
strongest counter-argument?

**Pass 2 — Completeness**: Have all relevant statutes, regulations, and principles been
considered? Any regulatory dimensions not addressed (zoning, environmental, ADA, energy codes)?
Case law on the specific lease clause type?

**Pass 3 — Challenge**: What is the strongest argument that this clause IS acceptable?
Under what commercial circumstances might a reasonable real estate attorney accept it
(e.g., very short lease term, creditworthy landlord, market norms in this specific submarket)?
Is RED classification proportionate?

**Mark as**: `self_interrogation: PASS` or `self_interrogation: REVISED` in the Glass Box audit trail.

### Confidence Scoring

| Level        | Range     | Meaning                                          | Action                                                |
| ------------ | --------- | ------------------------------------------------ | ----------------------------------------------------- |
| **Definite** | 0.95-1.0  | Settled law, clear statute, no ambiguity         | State with confidence                                 |
| **High**     | 0.80-0.94 | Strong authority, minor interpretation questions | State with brief caveat                               |
| **Probable** | 0.60-0.79 | Good arguments, reasonable minds could differ    | State with reasoning + contra-indicators              |
| **Possible** | 0.40-0.59 | Genuinely uncertain, competing authorities       | Flag for professional review with both sides          |
| **Unlikely** | 0.0-0.39  | Weak basis, speculative                          | Do NOT assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every review output must include this YAML block at the end:

```yaml
glass_box:
  skill_name: "legalcode-commercial-lease-review"
  document: "[Lease title or identifier]"
  property_address: "[Property address]"
  lease_type: "[Office / Retail / Industrial / Mixed-Use]"
  lease_commencement: "[Commencement date or 'Not specified']"
  lease_term_years: "[Number of years or 'Not specified']"
  renewal_options: "[Summary of renewal options or 'None']"
  user_side: "[Tenant / Landlord]"
  governing_law: "[Jurisdiction identified from lease]"
  loi_provided: "[Yes — delta analysis completed / No — market benchmarks only / Not available]"
  loi_drift_items: "[Number of LOI drift issues found or 'N/A']"
  playbook_used: "[Playbook name or 'General commercial standards']"
  clauses_reviewed: "[number — of 14 categories]"
  clauses_present: "[number]"
  clauses_missing: "[number] — [list with severity]"
  legalcode_mcp: "[Connected / Not connected]"
  authority_reference_file: "[path to temp file or 'Not created']"
  statutes_consulted:
    - "[Statute 1 — VERIFIED (legalcode-mcp) or UNVERIFIED]"
    - "[Statute 2 — ...]"
  case_law_consulted:
    - "[Case 1 — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  citations_verified: "[count VERIFIED] / [count UNVERIFIED]"
  self_interrogation: "[PASS / REVISED — description of revision / NOT APPLICABLE]"
  red_items: "[count]"
  yellow_items: "[count]"
  green_items: "[count]"
  confidence: "[DEFINITE / HIGH / PROBABLE / POSSIBLE / UNLIKELY] — [rationale]"
  limitations:
    - "[Any scope limitation, assumption, or caveat]"
    - "[Second limitation if applicable]"
  reviewer: "AI-assisted — requires review by a qualified real estate attorney licensed in the governing jurisdiction"
```

---

## Anti-Patterns

What NOT to do when reviewing commercial leases:

1. **Reviewing without knowing which side you represent.** Tenant-favorable and
   landlord-favorable positions are inverses. A missing rent cap is RED for the tenant,
   GREEN for the landlord. Always clarify the reviewing party's position first.

2. **Skipping the LOI delta check.** The most common commercial lease error is silent
   drift from LOI to executed lease. Free rent periods shrink. TIA amounts drop. Renewal
   options disappear. The LOI delta check is not optional — it is the first substantive
   analysis step.

3. **Applying CAM analysis without understanding the lease type.** A gross lease has no
   separate CAM pass-through. A triple-net lease has full operating expense pass-through.
   A modified-gross lease has specific carve-outs. Applying the wrong CAM framework
   produces nonsensical findings.

4. **Treating base year expense stops as boilerplate.** In full-service/gross leases,
   the base year is a critical financial parameter. A base year set in an anomalously
   low-expense year (pandemic years, first-year-of-operation years) can generate massive
   operating expense escalations that dwarf base rent. Analyze carefully.

5. **Missing the gross-up issue in CAM.** Landlords often "gross up" occupancy for CAM
   calculation purposes, assuming the building is 95% occupied even when it is 60%
   occupied. This increases the per-square-foot CAM charge tenants pay. Flag all
   gross-up provisions and verify that gross-up is limited to controllable variable costs,
   not fixed costs like property taxes.

6. **Treating insurance as a formality.** The waiver of subrogation provision is critical.
   Without mutual waiver, one party's insurer can sue the other party for fire damage or
   flood damage — destroying the landlord-tenant relationship and exposing both parties
   to uncapped claims. Flag absence as RED.

7. **Overlooking ADA shared liability.** Lease language that places all ADA compliance
   on the tenant does not eliminate the landlord's liability to third parties under the
   ADA. A tenant who accepts sole ADA responsibility is accepting indemnification
   obligations for the landlord's own statutory duties. This is a significant hidden risk.

8. **Ignoring environmental pre-existing conditions.** A tenant who accepts environmental
   liability without a pre-existing condition carve-out may be responsible for prior
   contamination from the landlord's own activities, previous tenants, or even off-site
   migration. This risk can exceed the aggregate lease value.

9. **Accepting "any default" as a trigger for cross-default.** Cross-default clauses that
   trigger on any breach anywhere in the tenant's real estate portfolio (or corporate
   affiliate portfolio) can cascade from a minor administrative default into a multi-site
   lease termination. Scrutinize the trigger carefully.

10. **Underweighting holdover risk.** A tenant who holds over without agreement can face
    200% rent penalties, consequential damages for the landlord's lost-deal claims, and
    automatic conversion to a year-to-year tenancy. The holdover analysis is not academic —
    calculate actual dollar exposure before classifying severity.

11. **Redlines without fallback positions.** "Delete this clause" is a dead-end in
    commercial real estate negotiation. Every redline must have a primary position and
    an acceptable fallback. The fallback is often what gets agreed.

12. **Jurisdiction bleed.** Do not apply US landlord-tenant law to UK leases (LTA 1954
    security of tenure does not exist in the US), or Australian Retail Leases Act protections
    to office leases (they typically apply only to retail premises). Use [JURISDICTION-SPECIFIC]
    markers throughout and verify which regime applies.

13. **Overstating enforceability of lease ADA/accessibility allocations.** Courts in most
    jurisdictions will not enforce a lease provision that purports to eliminate one party's
    statutory accessibility obligations. Do not advise tenants that they have fully shifted
    this risk; advise that the lease provision is of limited protective value.

14. **Ignoring the guarantee guaranty on assignment.** Many tenants successfully negotiate
    a lease assignment to a more creditworthy entity but fail to negotiate release of the
    original guarantor. This results in a principal being personally liable for a business
    they no longer control. Flag as RED without exception.

15. **Assuming LOI terms survived drafting.** LOIs are non-binding; lease drafting attorneys
    frequently miss, narrow, or inadvertently omit LOI commitments. Never assume an LOI
    term made it into the lease without direct cross-reference verification.

16. **Skipping the renewal rent reset mechanism.** A renewal at "fair market rent" without
    a binding arbitration mechanism gives the landlord effective unilateral control over
    renewal rent. This is the economic equivalent of no renewal right at all if the landlord
    is unreasonable. Always flag absence of a binding rent reset mechanism.

17. **Reviewing clauses in isolation.** Base rent, CAM charges, operating expense stops,
    and property tax escalations interact. The effective total occupancy cost (TOC) may
    look very different from the base rent alone. Always analyze the aggregate financial
    exposure across all monetary provisions before writing the executive summary.

18. **Treating early termination fees as fixed.** Termination fee formulas can require
    payment of unamortized TI, unamortized free rent, unamortized brokerage commissions,
    and full remaining rent — all in some leases. Calculate the actual dollar exposure
    before classifying severity. A 50-year-ago termination right with a $5M fee is not
    a meaningful right.

19. **Missing the difference between relocation and substitution.** A relocation right
    allows the landlord to move the tenant to different space. A substitution right
    allows the landlord to substitute comparable space during construction. Both require
    comparable space, moving cost reimbursement, and notice periods — but have different
    operational impacts. Analyze both, but do not conflate them.

20. **Delivering analysis without recommending next steps.** A lease review that identifies
    RED and YELLOW items without prioritized action items leaves the client without
    guidance. Always deliver a recommended next-steps section with specific owners, actions,
    and deadlines.

---

## Writing Standards

### For redline rationales (shareable with counterparty's counsel):

- Plain language, no jargon or filler
- Active voice: "Landlord must maintain the roof structure" not "The roof structure is to be maintained"
- Short sentences, one point per sentence
- Name the actor: "The tenant shall..." not "It is required that..."
- Be specific: cite section reference, not "the relevant clause"
- Professional and non-adversarial in tone: "This allocation differs from market standard because..." rather than "This clause is unreasonable"

### For internal analysis:

- Same plain-language discipline
- May include more technical legal analysis and statutory citations
- Confidence qualifiers where appropriate
- Glass Box audit trail appended

### Quality gates before delivery:

1. Can a non-lawyer business stakeholder understand the executive summary?
2. Can the counterparty's counsel understand and respond to each redline?
3. Is every legal claim backed by a specific citation or flagged [VERIFY]?
4. Are there any vague, hedging, or ambiguous phrases? Fix them.
5. Can any sentence be shortened without losing meaning? Shorten it.
6. Does every RED finding have a self-interrogation pass documented?
7. Is the Glass Box audit trail complete?

---

## External Tool Integration

### With legalcode-mcp connected (preferred):

1. In Step 5, search for landlord-tenant statutes in the governing jurisdiction
2. Search for relevant case law on lease enforceability, rent control, environmental liability, and ADA compliance
3. Search for current regulatory guidance on building codes, energy requirements, and tenant rights
4. Save results to `/tmp/legalcode-commercial-lease-research.md`
5. Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Search queries (adapt to jurisdiction):**

- `[state/country] commercial landlord tenant act 2024`
- `ADA commercial lease landlord tenant responsibility enforcement`
- `CERCLA innocent landowner defense Phase I ESA requirements`
- `[jurisdiction] CAM charges tenant audit rights commercial lease`
- `commercial lease personal guarantee enforceability [state]`

### Without legalcode-mcp:

1. Mark all statutory and case law references in the analysis with **[VERIFY]**
2. Use perplexity-search for web-backed synthesis when needed
3. Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
4. Focus enhancement on structural quality, workflow design, and market-standard analysis

---

## Redline Format

For every YELLOW or RED finding, provide a redline in this format:

```
**Clause**: [Section reference and clause name]
**Current language**: "[exact quote from lease — or 'Not present / Missing']"
**Proposed redline**: "[specific alternative language, ready to insert]"
**Rationale**: [1-2 sentences suitable for external sharing with counterparty's counsel]
**Legal basis**: [Statute, regulation, or established principle — or "General commercial practice" if no specific authority]
**Priority**: [Tier 1 — Must-Have / Tier 2 — Should-Have / Tier 3 — Nice-to-Have]
**Fallback**: [Alternative position if primary redline is rejected by landlord]
**Confidence**: [Level — e.g., High (0.85) — rationale for classification]
```

**Best practices:**

1. **Be specific**: Exact language, not vague guidance; ready to paste into the lease
2. **Be balanced**: Firm on Tier 1 issues; commercially reasonable on Tier 3
3. **Explain rationale**: Professional, non-adversarial, shareable with the other side's counsel
4. **Provide fallback**: Always — "Delete this clause" alone is a dead-end
5. **Prioritize**: Identify Tier 1 / 2 / 3 explicitly so the client knows where to hold and where to concede
6. **Reference law**: Cite statute or principle; if from memory, mark [VERIFY]

---

## Stakeholder Impact Map

For each material deviation (YELLOW or RED), identify affected stakeholders:

| Stakeholder              | Role in Lease                | Impact of Finding                   |
| ------------------------ | ---------------------------- | ----------------------------------- |
| Tenant (entity)          | Primary obligor              | [summary]                           |
| Individual guarantor(s)  | Guarantor                    | [summary — if guarantee clause]     |
| Tenant's lender          | Leasehold mortgagee (if any) | [summary]                           |
| Landlord                 | Landlord                     | [counterparty impact]               |
| Landlord's lender        | Lienholder                   | [summary — if SNDAs involved]       |
| Subtenants / licensees   | Occupancy rights at risk     | [summary — if assignment clause]    |
| Insurance companies      | Subrogation risk             | [summary — if insurance clause]     |
| Environmental regulators | Compliance authority         | [summary — if environmental clause] |

---

## Output Format Template

```markdown
## Commercial Lease Review

**Document**: [Lease title or identifier]
**Property**: [Property address]
**Parties**: [Landlord name] (Landlord) / [Tenant name] (Tenant)
**Your Side**: [Tenant / Landlord]
**Lease Type**: [Office / Retail / Industrial / Mixed-Use]
**Lease Term**: [Commencement date — Expiration date] + [Renewal option summary]
**Governing Law**: [Jurisdiction]
**Review Basis**: [Playbook name / General market standards]
**Date of Review**: [Date]

---

## LOI Delta Summary (if LOI provided)

| LOI Commitment | Lease Provision | Delta        | Severity               |
| -------------- | --------------- | ------------ | ---------------------- |
| [term]         | [provision]     | [difference] | [GREEN / YELLOW / RED] |

**LOI drift findings**: [count] items requiring attention

---

## Executive Summary

[3-5 bullet points identifying the top risks with one-line severity flags]

**Overall assessment**: [GREEN — acceptable / YELLOW — negotiate before signing / RED — do not sign without resolution]

---

## Missing Clauses

| Missing Clause | Severity     | Recommended Action |
| -------------- | ------------ | ------------------ |
| [clause type]  | [RED/YELLOW] | [specific action]  |

---

## Clause-by-Clause Analysis

### [1. Base Rent and Escalation] — [GREEN / YELLOW / RED] | Confidence: [level]

**Lease provides**: [summary of provision]
**Standard position**: [playbook or market standard]
**Deviation**: [description of gap, if any]
**Business impact**: [financial or operational consequence]

[Redline block if YELLOW or RED]

---

[Repeat for each of the 14 clause categories]

---

## Negotiation Strategy

### Tier 1 — Must-Haves (Do Not Concede)

- [Finding 1] — [section reference] — Exposure: [dollar amount or description]
- [Finding 2] — ...

### Tier 2 — Should-Haves (Negotiate Firmly)

- [Finding 1] — [section reference]
- [Finding 2] — ...

### Tier 3 — Nice-to-Haves (Concession Candidates)

- [Finding 1] — [section reference]
- [Finding 2] — ...

**Recommended approach**: [sequencing guidance — e.g., "Lead with Tier 1 items in initial
markup. Package Tier 2 items as a set. Offer to accept landlord's position on [Tier 3 item]
in exchange for [Tier 1 concession]." ]

---

## Stakeholder Impact Map

[Table per Stakeholder Impact Map section above]

---

## Next Steps

| Action                                     | Owner                  | Deadline                 | Priority  |
| ------------------------------------------ | ---------------------- | ------------------------ | --------- |
| Obtain LOI if not already provided         | Tenant's counsel       | Before markup submission | Immediate |
| Escalate [RED finding] to leadership       | [Business stakeholder] | [Date]                   | Immediate |
| Submit initial markup                      | Tenant's counsel       | [Date]                   | High      |
| Obtain insurance quotes at required limits | Risk team              | Before execution         | High      |
| Confirm CAM audit rights in playbook       | Legal team             | Before execution         | Medium    |

---

## Glass Box Audit Trail

[YAML block per Glass Box Audit Trail section above]
```

---

## Provenance

Created by Legalcode as an original synthesis (2026-03-01). Informed by deep web-backed
research on US, UK, and Australian commercial lease law and practice; structural patterns
from the `legalcode-contract-review`, `legalcode-employment-agreement-review`, and
`legalcode-nda-triage` reference skills; and a 2-agent parallel analysis pipeline
(Structural Analyst + Prompt Engineering Analyst). Covers 14 clause categories across
the commercial lease lifecycle with jurisdiction-specific guidance for US, UK, and Australia.

**Does not cover**: Ground leases, residential leases, agricultural leases, or jurisdiction-specific
variants (planned: `legalcode-commercial-lease-review-ew` for England & Wales FRI leases;
`legalcode-commercial-lease-review-au-retail` for Australian Retail Leases Act compliance).

**Version**: 1.0
**Last updated**: 2026-03-01
