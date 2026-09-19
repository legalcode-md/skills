---
name: legalcode-lease-abstractor
description: Extract and summarize key commercial lease terms into a structured abstract for portfolio
  management, date tracking, financial modeling, and quick reference. Use when building a lease database,
  onboarding a new lease into a portfolio system, tracking renewal and termination option deadlines, abstracting
  lease terms for due diligence, or creating a machine-readable lease record for import into Yardi, MRI,
  CoStar, VTS, Tango, or similar platforms.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Extract and summarize key commercial lease terms into a structured abstract for portfolio management, date tracking, financial modeling, and quick reference. Use when building a lease database, onboarding a new lease into a portfolio system, tracking renewal and termination option deadlines, abstracting lease terms for due diligence, or creating a machine-readable lease record for import into Yardi, MRI, CoStar, VTS, Tango, or similar platforms. Produces a 14-category structured abstract covering rent and escalations, CAM and operating expenses, TI allowances, renewal/expansion/termination options, assignment and subletting, co-tenancy, exclusivity, use restrictions, insurance, maintenance, guarantees, SNDA, default and cure periods, and holdover provisions — with extraction confidence scoring, critical date computation, amendment reconciliation, and structured JSON/CSV export. Jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers. Does not assess risk, generate redlines, or replace qualified real estate counsel review.


# Legalcode Lease Abstractor

> **Disclaimer**: This skill provides a framework for AI-assisted lease abstraction. It
> does not constitute legal advice. All outputs should be reviewed by a qualified real
> estate professional or attorney licensed in the relevant jurisdiction before use or
> reliance. Commercial lease law varies significantly by jurisdiction and changes
> frequently — verify current applicability before acting on any extracted provision.
> Extracted data carries hallucination risk; verify all critical dates, financial figures,
> and option mechanics against the original lease document before entering into any
> portfolio management or decision-making system.

## Purpose and Scope

This skill extracts and summarizes key lease terms from commercial leases into a
structured, standardized abstract optimized for portfolio management, financial modeling,
date tracking, and system import. It captures what the lease actually says — field by
field, provision by provision — and exports the results in both human-readable markdown
and machine-readable formats.

**Covers:**

- 14-category lease extraction framework covering all material lease provisions
- Base rent, rent schedule, and escalation mechanics (fixed, CPI, FMR, percentage)
- CAM, operating expenses, base year/expense stop, gross-up, caps, and reconciliation
- Tenant Improvement Allowance (TIA), disbursement conditions, and restoration obligations
- Renewal, expansion, contraction, ROFO, ROFR, and termination options — with absolute
  exercise date computation
- Assignment, subletting, recapture rights, permitted transfers, and profit-sharing
- Co-tenancy provisions — trigger, remedy, notice, and reconstitution mechanics
- Exclusivity and use restrictions
- Insurance requirements, indemnification flow, and waiver of subrogation
- Maintenance and repair obligation allocation
- Personal guarantee scope, guarantor identity, good-guy clause mechanics
- SNDA (subordination, non-disturbance, and attornment) provisions
- Default, cure periods, self-help, and remedies
- Holdover rate, conversion mechanics, and consequential damages exposure
- Amendment and exhibit reconciliation — building the consolidated current-terms abstract
- Critical date computation — converting relative references to absolute calendar dates
- Extraction confidence scoring (DEFINITE / HIGH / PROBABLE / PARTIAL / MISSING)
- Structured data export (JSON, CSV, Markdown) for portfolio system import
- Glass Box audit trail with extraction completeness metrics

**Does not:**

- Assess risk or classify findings as GREEN / YELLOW / RED
- Generate negotiation redlines or recommend positions (see `legalcode-commercial-lease-review`)
- Provide legal advice or replace qualified real estate counsel
- Apply to residential leases, ground leases, or agricultural tenancies
- Substitute for a formal title search, survey, or environmental site assessment

**Related skills:**

- `legalcode-commercial-lease-review` — Risk assessment, redlines, and negotiation strategy
  for commercial leases; use when reviewing a lease before signing or in dispute
- `legalcode-contract-metadata-extractor` — General-purpose contract metadata and party
  extraction for non-lease commercial agreements
- `legalcode-obligation-tracker` — Ongoing obligation tracking and milestone calendar
  across a portfolio of contracts
- `legalcode-contract-renewal-analysis` — Deep renewal decision analysis including
  cost-benefit framework and auto-renewal trap detection

---

## Jurisdiction and Governing Law

This is a jurisdiction-agnostic skill. Lease abstraction is a data extraction workflow,
not a legal interpretation workflow — the abstract records what the lease says, not what
the law requires. Jurisdiction matters primarily for:

1. **Critical date computation** — [JURISDICTION-SPECIFIC] Option notice windows are
   interpreted strictly in most jurisdictions; missed deadlines forfeit the option.
   Confirm local rules on whether notice periods are calendar days or business days
   and whether notice by mail extends the exercise window.

2. **CAM and operating expense recovery** — [JURISDICTION-SPECIFIC] Some jurisdictions
   (e.g., California under state Retail Leases standards; UK under RICS Code 2020;
   Australian states under Retail Leases Acts) impose limits on recoverable expenses or
   mandatory disclosure obligations. Note these restrictions in the abstract when identified.

3. **Proportionate share calculation** — [JURISDICTION-SPECIFIC] BOMA standards differ
   by property type (2017 Office, 2010 Industrial, 2016 Retail). Flag which standard is
   referenced; a mismatch between the stated standard and the actual measurement affects
   CAM charges.

4. **Assignment and subletting consent standard** — [JURISDICTION-SPECIFIC] Landlord and
   Tenant Act 1988 (UK) imposes a reasonableness standard that cannot be contracted out.
   US states vary on implied duty not to unreasonably withhold consent.

5. **Holdover conversion** — [JURISDICTION-SPECIFIC] Month-to-month vs. year-to-year
   conversion rules vary by jurisdiction. Note any statutory default and any lease
   provision that modifies it.

6. **SNDA and security of tenure** — [JURISDICTION-SPECIFIC] UK business tenants have
   statutory security of tenure under Landlord and Tenant Act 1954 (unless contracted
   out under s.38A). US leases subordinate by agreement subject to NDA protections.
   Australian retail leases have mandatory SNDA-equivalent protections under Retail Leases
   Acts.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when the answer changes the extraction scope,
output format, or validation approach.

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

### Step 1: Accept the Lease Package

Accept the lease in any of these formats:

- **File(s)**: PDF, DOCX, or scanned document — the original lease plus all amendments,
  riders, exhibits, and schedules
- **Pasted text**: Lease text pasted directly into the conversation
- **URL**: Link to a lease in a CLM, document storage, or data room system

**⟁ CLARIFY** — Confirm the completeness of what has been provided:

- Is this the **executed** version or a draft?
- Are there **amendments** or **letter agreements** that modify original terms? If so,
  request them before extracting — abstractions based on the original lease without
  amendments are a primary source of material error.
- Are all **exhibits and schedules** available? (Critical for: permitted use definitions,
  floor plans confirming RSF, construction exhibits defining landlord's work, insurance
  schedules, guarantee forms.)

If any amendments or exhibits are unavailable, proceed but mark all affected fields
`PARTIAL — pending amendment reconciliation` in the abstract.

### Step 2: Gather Extraction Context

**⟁ CLARIFY** — Ask these questions before beginning. Skip any already answered:

1. **Which side are you on?**
   - Options: **Tenant** | **Landlord** | **Acquirer / Due Diligence** | **Lender / CMBS Underwriter** | **Other**
   - _Why this matters_: Determines which stakeholder perspective informs the abstract
     summary language and which fields receive priority annotation (e.g., an acquirer
     prioritizes option exercise dates and financial exposure; a lender prioritizes
     SNDA and insurance compliance).

2. **What is this abstract for?**
   - Options: **Portfolio system import (Yardi/MRI/VTS/CoStar)** | **Due diligence review** |
     **Lease renewal decision** | **General portfolio management** | **Litigation/dispute support** |
     **Other**
   - _Why this matters_: Determines export format preference and annotation depth.

3. **Is there an LOI or term sheet to validate against?**
   - Options: **Yes — attach it** | **No** | **Not applicable**
   - _Why this matters_: If yes, the abstract will include a delta-check table confirming
     whether negotiated LOI terms made it into the executed lease unchanged.

4. **Output format preference:**
   - Options: **Full markdown abstract + JSON export** | **Markdown abstract only** |
     **JSON/CSV data only (for system import)** | **All formats**
   - _Why this matters_: Determines output section delivery.

5. **Extraction scope:**
   - Options: **Full 14-category extraction** | **Priority focus: financial terms only** |
     **Priority focus: critical dates and options only** | **Custom — specify**
   - _Why this matters_: Full extraction is comprehensive but takes longer; scoped extraction
     delivers faster results when only certain categories are needed.

### Step 3: Inventory All Documents

Before extracting, inventory every document in the lease package:

1. **Identify the original lease** — note execution date, parties, and document length.
2. **Inventory all amendments** — list by number and execution date; note which sections
   each amendment modifies.
3. **Inventory exhibits and schedules** — list each by letter/number and subject matter.
4. **Confirm hierarchy**: Amendments override the original lease for any conflicting terms;
   exhibits are incorporated by reference; riders supplement but do not replace unless
   stated.
5. **Flag orphaned cross-references** — note any reference to an exhibit, schedule, or
   rider that is not in the package as `[MISSING EXHIBIT: describe]`.

Build a Document Inventory table as Step 3's output:

```
| Document | Type | Date | Sections Modified / Subject |
|----------|------|------|-----------------------------|
| [Lease title] | Original lease | [Date] | Full agreement |
| Amendment No. 1 | Amendment | [Date] | §§ X, Y, Z |
| Exhibit A | Floor Plan | [Date] | Premises definition |
| ...                                                      |
```

### Step 4: Extract — Financial Terms

Extract the complete financial regime from the lease as amended. This is the highest-stakes
section; errors in financial extraction propagate to portfolio financials, underwriting
models, and CAM reconciliation.

**Extraction sequence:**

1. Base rent — see §7 (14-Category Framework), Category 1
2. Rent schedule — build the full step-up table (see §8: Rent Schedule Abstraction)
3. Operating expenses / CAM — see §7, Category 2 and §9: CAM/OpEx Deep Capture
4. Additional rent components (parking, storage, antenna/rooftop, etc.)
5. Security deposit — amount, form, reduction schedule, return conditions
6. TI allowance — see §7, Category 3
7. Personal guarantee — see §7, Category 4

### Step 5: Extract — Key Dates and Milestones

Extract every date and convert relative references to absolute calendar dates. This is
the second-highest-stakes section; missed option exercise windows forfeit rights that
cannot be recovered.

**Critical date computation rule**: For every relative reference (e.g., "no fewer than
12 months and no more than 6 months prior to expiration"), compute the absolute earliest
and latest exercise date based on the lease expiration date. Flag all computed dates with
`[COMPUTED FROM §X]` and note the formula used.

See §10: Options Abstraction Framework for options-specific date extraction.

### Step 6: Extract — Obligations, Rights, and Restrictions

Extract the non-financial provisions in the following sequence:

- Category 5 (Use and Exclusivity)
- Category 6 (Assignment and Subletting)
- Category 7 (Default and Cure)
- Category 8 (Landlord Access and Relocation)
- Category 9 (Insurance)
- Category 10 (Maintenance and Repair)
- Category 11 (Environmental)
- Category 12 (ADA/Accessibility)
- Category 13 (Holdover)
- Category 14 (SNDA and Estoppel)

### Step 7: LOI Delta Validation (if LOI provided)

If the user provided an LOI, term sheet, or prior commitment document:

1. Identify each material term agreed in the LOI.
2. Locate the corresponding lease provision.
3. Confirm whether the executed lease matches the LOI term, varies from it, or omits it.
4. Build a delta table:

```
| LOI Term | LOI Agreement | Lease Provision | Match? | Notes |
|----------|--------------|-----------------|--------|-------|
| Base rent | $X/SF/yr     | §4.1: $Y/SF/yr  | ❌ DRIFT | Rent increased by $Z/SF |
| TI allowance | $X/SF | §7.2: $X/SF | ✅ Match | — |
| ...                                                            |
```

Flag any `DRIFT` items — terms that were agreed in the LOI but changed in the executed
lease without apparent justification.

### Step 8: Build Abstract, Quality-Check, and Export

1. **Assemble the full abstract** using the Output Format Template (§18).
2. **Run the Extraction Quality Gates** (§12) silently.
3. **Run Self-Interrogation** (§13) — three passes.
4. **Score each data point** using the Confidence Scoring system (§14).
5. **Flag all PARTIAL, MISSING, and AMBIGUOUS fields** in the abstract.
6. **Build the structured data export** (§11) in the requested format(s).
7. **Populate the Glass Box Audit Trail** (§15).
8. Deliver the complete abstract with the Glass Box as the final section.

---

## 14-Category Lease Extraction Framework

This is the systematic extraction guide for each category. For each data point: identify
the provision location (section and page), extract the precise language, assign a
confidence score, and note any cross-references to other sections or exhibits.

---

### Category 1 — Base Rent and Escalation

**Extract:**

| Field | Location | Extracted Value | Confidence |
| ----- | -------- | --------------- | ---------- |

- **Annual base rent**: $ per year
- **Monthly base rent**: $ per month
- **Rent per RSF**: $/RSF/year (rentable square foot)
- **Rent commencement date**: the date rent first becomes payable (may differ from lease
  commencement if free rent period exists)
- **Free rent / rent abatement**: months and periods of abatement; which rent components
  are abated (base rent only vs. all rent)
- **Escalation type**: one of:
  - _Fixed percentage_: annual step-up by X% on each anniversary
  - _Fixed dollar step_: rent increases by $X/SF on stated dates (build full schedule)
  - _CPI/CPI-U_: record base index, measurement month, floor (minimum), ceiling
    (maximum), and frequency of adjustment
  - _Fixed market reset at option_: note determination mechanism
  - _No escalation_: confirm explicitly
- **Full rent schedule**: See §8 — build the line-item table for the entire term
- **Percentage rent** (retail): breakpoint (natural or artificial), percentage rate, gross
  sales definition, reporting frequency, landlord audit rights, exclusions from gross sales

**Cross-reference check**: Confirm rent schedule matches any exhibit or schedule that
tabulates rent. Note discrepancies.

---

### Category 2 — CAM, Operating Expenses, Taxes, and Insurance

**Lease type classification** (determines the entire recovery structure):

- **Gross / Full-Service Gross**: landlord pays all operating expenses above base rent
- **Modified Gross**: some expenses pass through; specify which
- **Net / NNN**: tenant pays all operating expenses directly
- **Double Net (NN)**: tenant pays taxes and insurance; landlord pays structural
- **Base Year Stop**: tenant pays pro-rata share of increases above base year expenses
- **Expense Stop**: tenant pays pro-rata share above a fixed $/SF stop amount
- **Industrial Gross**: similar to modified gross but common in industrial/warehouse

**Extract for non-gross leases:**

- **Tenant's proportionate share**: fraction or percentage; how the denominator is defined
  (leased area, leasable area, occupied area, gross leasable area — note which)
- **BOMA standard referenced**: note which measurement standard; flag if unstated
- **Base year** (for base year stop leases): year, actual expenses in base year if stated
- **Expense stop** (for expense stop leases): $/SF amount
- **Controllable expense cap**: percentage, whether cumulative or non-cumulative,
  which expenses are excluded from cap (taxes and insurance almost always excluded)
- **Gross-up provision**: whether expenses may be grossed up, occupancy threshold used
  (typically 95%), and which expense categories are subject to gross-up
- **Specific exclusions from CAM**: list all named exclusions (capital expenditures,
  depreciation, debt service, management fees above stated cap, ground lease payments,
  leasing commissions, costs attributable to other tenants, etc.)
- **Non-standard inclusions**: any unusual expenses included in CAM (e.g., capital
  expenditure amortization, roof reserves)
- **CAM reconciliation mechanics**: timeline for annual reconciliation (typically 60–120
  days after lease year-end), format, tenant audit rights (notice period, records
  retention, dispute resolution procedure, audit cost responsibility)
- **Real estate tax provisions**: assessment challenge rights, tax increment exclusions,
  special assessment treatment
- **Insurance cost passthrough**: landlord-carried property/liability/umbrella included in
  CAM recovery; limits stated

[JURISDICTION-SPECIFIC] Note any statutory limits on recoverable expenses applicable
in the identified jurisdiction (e.g., AU Retail Leases Acts restrict CAM to defined
operating costs; UK RICS Code 2020 principles on service charge transparency).

---

### Category 3 — Tenant Improvement Allowance and Construction

**Extract:**

- **TIA amount**: total dollar amount or $/RSF amount
- **Application**: what TIA may be used for (construction hard costs, soft costs, FF&E,
  moving expenses, cabling, signage — note any restrictions)
- **Use-it-or-lose-it deadline**: last date by which TIA must be spent or requested
- **Disbursement conditions**: required documentation (AIA draw forms, lien waivers,
  completion certificates, architect sign-off)
- **Who controls construction**: tenant-managed with allowance vs. landlord turnkey
- **Landlord's work**: what the landlord is obligated to deliver at lease commencement;
  delivery standard (turnkey, warm shell, cold dark shell, as-is)
- **Delivery deadline and delay remedy**: when landlord must deliver possession; rent
  abatement or termination right if delivery is delayed
- **Warranty on landlord's work**: duration and scope
- **Restoration obligations**: what alterations or improvements must be removed and
  premises restored at expiration; whether landlord can designate "specialty improvements"
  that must be removed
- **Alteration consent threshold**: dollar or scope threshold above which landlord consent
  is required; consent standard (not to be unreasonably withheld?)

---

### Category 4 — Personal Guarantee and Guarantor Liability

**Extract:**

- **Guarantor identity**: full legal name(s) of guarantor(s); whether individual or entity
- **Guarantee type**: full/unconditional vs. limited
- **Guarantee cap**: dollar limit or duration limit (e.g., "guaranteed obligations not
  exceeding 24 months of base rent")
- **Good-guy clause**: exists or not; trigger event (typically: notice given and actual
  vacation of premises + surrender in required condition); what obligations are released
  upon good-guy trigger; any conditions (no default on surrender date)
- **Guarantor release conditions**: conditions under which guarantor is released (e.g.,
  tenant meeting net worth/net revenue thresholds, time-based release after X years)
- **Surviving obligations**: obligations that survive good-guy release (e.g., restoration,
  cleanup, holdover liability)
- **Guarantor notice rights**: whether guarantor is entitled to copies of landlord notices
  to tenant; cure rights independent of tenant

---

### Category 5 — Permitted Use, Exclusivity, and Co-Tenancy

**Extract:**

- **Permitted use clause**: exact language (broad vs. restrictive); note whether "and for
  no other purpose" language limits use
- **Exclusivity clause**: exact prohibited activity; geographic scope of exclusivity
  (within project, within radius); named carve-outs for existing tenants; enforcement
  mechanism (rent reduction, termination right) and notice/cure before remedy
- **Prohibited uses**: list all explicitly prohibited uses
- **Go-dark / continuous operation covenant**: whether tenant must remain open and
  operating; hours; remedy for violation
- **Radius restriction**: whether tenant is prohibited from operating a competing location
  within a stated radius
- **Co-tenancy provisions** (retail/mixed-use — one of the most commonly under-abstracted
  clauses):
  - Named anchor tenants required to remain open
  - Occupancy threshold trigger (e.g., 80% of GLA occupied)
  - How occupancy is measured and by whom
  - Remedy upon co-tenancy failure: reduced rent (specify new rate), percentage rent
    only, or right to terminate
  - Notice period before remedy activates; cure period for landlord
  - Duration of below-threshold occupancy before termination right accrues
  - Reconstitution provision: when co-tenancy is restored, when does full rent resume;
    any reconciliation of reduced rent paid during co-tenancy failure period

---

### Category 6 — Assignment and Subletting

**Extract:**

- **Landlord consent required**: yes/no; consent standard ("sole and absolute discretion"
  vs. "not to be unreasonably withheld, conditioned, or delayed")
- **Permitted transfers** (consent-free): affiliates, subsidiaries, parent, successors by
  merger/acquisition/restructuring — define exactly what qualifies; any conditions
  (e.g., acquirer's net worth must equal tenant's)
- **Landlord's recapture right**: whether landlord may recapture premises upon assignment/
  subletting request; partial vs. full recapture; whether tenant may withdraw request if
  recapture exercised
- **Profit-sharing on sublease**: how excess sublease rent (above tenant's base rent) is
  split; what is excluded from "profit" (e.g., tenant's costs of subleasing,
  improvements, concessions)
- **Original tenant liability after assignment**: fully released upon approved assignment,
  or continuing as guarantor of assignee's performance
- **Assignee/sublessee use restriction**: whether assignee/sublessee is limited to tenant's
  permitted use
- **Change of control**: whether a change of control of tenant constitutes an assignment
  requiring consent; how change of control is defined

[JURISDICTION-SPECIFIC] UK: Landlord and Tenant Act 1988 imposes a duty to respond
within a reasonable time and not to unreasonably withhold consent, which cannot be
excluded. Note if the lease attempts to exclude this.

---

### Category 7 — Default, Cure Periods, and Remedies

**Extract:**

- **Monetary default**: notice requirement and cure period (typically 3–10 days)
- **Non-monetary default**: notice requirement and cure period (typically 30 days) plus
  any extended cure period for complex defaults (e.g., "30 days plus additional time
  reasonably necessary if cure commenced within 30 days")
- **Landlord's remedies upon tenant default**: termination and re-entry, reletting with
  recovery of shortfall, acceleration of future rent, damages, self-help
- **Tenant's self-help right**: whether tenant may perform and offset after landlord
  default; notice and cure period required before self-help; dollar cap on offset
- **Consequential/punitive damages waiver**: mutual or one-sided; any carve-outs
- **Landlord default notice and cure**: notice and cure period if landlord fails to
  perform obligations
- **Dispute resolution**: litigation vs. arbitration; governing law; venue; jury trial waiver

---

### Category 8 — Landlord Access and Relocation Rights

**Extract:**

- **Landlord access rights**: notice requirement (if any) for inspections, repairs, showing
  to prospective tenants; emergency access exception
- **Scope of landlord access**: inspection only vs. right to perform work; whether work
  may interrupt tenant's operations
- **Relocation right**: whether landlord has right to relocate tenant; notice period;
  comparable space standard (size, configuration, location within building/project);
  moving cost responsibility; rent adjustment if relocated space differs in size or quality
- **Signage rights**: building exterior, monument, lobby directory; tenant approval rights
  over landlord's signage

---

### Category 9 — Insurance

**Extract:**

_Tenant-required coverages:_

- Commercial general liability: per occurrence and annual aggregate limits
- Property / contents: replacement cost standard; landlord's property excluded
- Business interruption: coverage period and amount
- Workers' compensation and employer's liability: statutory limits
- Umbrella / excess liability: limits, follow-form requirement
- Any specialized coverages required (e.g., liquor liability, professional liability,
  contractor's all-risk during construction)
- Additional insured: landlord (and landlord's lender) named as additional insured on
  CGL; any other required additional insureds
- Waiver of subrogation: whether tenant's insurer waives subrogation against landlord
- Certificate delivery obligations: when required, to whom, on what trigger

_Landlord-required coverages:_

- Property insurance on building shell (limits, replacement cost vs. actual cash value)
- Commercial general liability for common areas
- Umbrella limits

_Mutual indemnification flow:_

- Tenant indemnifies landlord for: (state scope)
- Landlord indemnifies tenant for: (state scope)
- Limitation of landlord liability: landlord's liability capped at landlord's interest
  in property (note if personal liability of partners/members is excluded)

---

### Category 10 — Maintenance and Repair Obligations

**Extract:**

_Landlord's obligations:_

- Structural components: roof, foundation, exterior walls, load-bearing elements
- Building systems: HVAC, plumbing, electrical to the premises; common area systems
- Common areas: lobbies, corridors, parking, landscaping
- Any specific landlord maintenance obligations unique to this lease

_Tenant's obligations:_

- Interior non-structural: interior walls, flooring, ceilings, fixtures, interior doors
- HVAC serving premises exclusively (if responsibility transferred to tenant)
- Trade fixtures, equipment installed by tenant
- Compliance with requirements triggered by tenant's alterations or specific use

_Repair vs. replacement:_ note any provision allocating capital replacement obligations
(e.g., if HVAC replacement is needed, who pays — common dispute point)

_End-of-term condition:_ required surrender condition; "broom clean" standard vs. more
specific; restoration obligations cross-referenced from Category 3

---

### Category 11 — Environmental Obligations

**Extract:**

- **Pre-existing contamination representation**: whether landlord represents that, as of
  commencement, no hazardous materials exist on the premises or property in violation
  of applicable law; scope of the representation
- **Tenant's use restrictions**: prohibited substances; MSDS/SDS reporting obligations;
  tenant's environmental compliance responsibility
- **Notification obligations**: duty to notify landlord of any contamination discovered
  or suspected; timeframe
- **Remediation responsibility**: which party is responsible for remediation; whether
  pre-existing contamination is carved out of tenant's responsibility
- **Phase I/II ESA**: whether lease requires a Phase I environmental site assessment
  before commencement; any ongoing monitoring obligations
- **CERCLA / hazardous waste indemnity** [JURISDICTION-SPECIFIC US]: whether the lease
  addresses CERCLA liability allocation between landlord and tenant [VERIFY current
  statutory scheme in applicable jurisdiction]

---

### Category 12 — ADA / Accessibility Compliance

[JURISDICTION-SPECIFIC] This category is jurisdiction-dependent. Flag the applicable
accessibility compliance framework:

- **US**: Americans with Disabilities Act (ADA), 42 U.S.C. § 12181 (public accommodations)
- **UK**: Equality Act 2010, s.20 duty to make reasonable adjustments
- **Australia**: Disability Discrimination Act 1992; Building Code of Australia (ABCB)

**Extract:**

- **Allocation of responsibility**: common areas (landlord) vs. leased premises (tenant)
- **Initial compliance vs. ongoing compliance**: who is responsible for bringing the
  premises into compliance at commencement vs. ongoing alterations-triggered compliance
- **Indemnification for ADA/accessibility violations**: tenant indemnifies landlord for
  tenant's use-triggered violations; landlord indemnifies tenant for pre-existing
  violations in common areas
- **Alterations compliance obligation**: whether tenant-initiated alterations trigger
  a path-of-travel upgrade obligation and who bears that cost

---

### Category 13 — Holdover Provisions

**Extract:**

- **Holdover rent rate**: typically 125–150% of last month's base rent; note whether
  additional rent components also increase
- **Holdover characterization**: month-to-month vs. year-to-year (triggers full-year
  liability risk if year-to-year)
- **Landlord's remedy for holdover**: right to terminate at will, right to recover
  consequential damages (e.g., costs of holding over from a successor tenant)
- **Notice to quit requirement**: whether landlord must give notice to quit before
  treating holdover tenant as a trespasser
- **Tenant's financial exposure**: compute the maximum holdover rent exposure (holdover
  rate × monthly rent × estimated exposure period)

[JURISDICTION-SPECIFIC] Some jurisdictions have statutory holdover rules that override
lease language. Note any statutory default in the identified jurisdiction.

---

### Category 14 — SNDA, Estoppel, and Security of Tenure

**Extract:**

- **SNDA requirement**: whether lease requires landlord to deliver a Subordination,
  Non-Disturbance, and Attornment Agreement from landlord's lender; timing (at execution
  or within X days); condition precedent to commencement
- **NDA (Non-Disturbance) condition**: whether NDA protection is conditioned on tenant
  not being in default at time of foreclosure
- **Tenant's recognition rights post-foreclosure**: whether successor landlord must
  recognize tenant's rights under the lease
- **Estoppel certificate obligation**: notice period; deemed-approved provision (if tenant
  fails to respond, estoppel is deemed given as stated by landlord — flag this risk);
  frequency limit on requests
- **Security of tenure** [JURISDICTION-SPECIFIC UK]: note whether the lease has been
  contracted out of the Landlord and Tenant Act 1954 and whether the s.38A statutory
  procedure was followed (Section 25 / Section 26 notice rights eliminated if so); note
  the consequences

---

## Renewal, Expansion, Termination, and ROFO/ROFR Options

### Options Extraction Framework

Each option is a distinct, high-value right that requires its own structured record.
**Extract every option into a separate option record.** A common extraction error is
recording that an option exists without capturing the precise mechanics.

For **each option found**, complete this record:

```
OPTION RECORD — [Type: Renewal / Expansion / Contraction / Termination / ROFO / ROFR]

Option Number:          [1st Renewal / 2nd Renewal / etc.]
Applicable Premises:    [Full premises / Partial: describe]
Scope:                  [X additional months/years at renewal / Y RSF expansion space]

EXERCISE WINDOW (CRITICAL — COMPUTE ABSOLUTE DATES):
  Notice window language:   [Exact lease language, e.g., "no earlier than 18 months
                              and no later than 12 months prior to then-current expiration"]
  Lease expiration date:    [Date]
  EARLIEST exercise date:   [COMPUTED: expiration minus 18 months = DD/MM/YYYY]
  LATEST exercise date:     [COMPUTED: expiration minus 12 months = DD/MM/YYYY]
  RECOMMENDED ADVANCE DATE: [Latest exercise date minus 60 days for compliance buffer]
  Notice method required:   [Written / Certified mail / Overnight courier / Any]
  Notice to:                [Landlord at address stated in §X]

RENT AT OPTION (if renewal):
  Rent determination method: [Fixed amount / Fixed formula / FMR / CPI adjustment]
  If FMR: determination process [Appraisal / Mutual agreement / Arbitration fallback]
  Arbitration mechanism:    [Describe if applicable]
  Cap on FMR reset:         [If any — e.g., "FMR shall not exceed 110% of prior rent"]
  Contains own escalation:  [Yes: describe / No]

CONDITIONS PRECEDENT:
  No default at exercise:   [Yes / No / Not stated]
  Tenant must be in possession: [Yes / No / Not stated]
  No prior assignment/subletting: [Yes / No / Not stated]
  Other conditions:         [Describe]

TERMINATION / CONTRACTION ECONOMICS (if applicable):
  Termination fee formula:  [Describe — e.g., unamortized TIA + 6 months base rent]
  Effective termination date: [Date or relative trigger]
  Surrender condition:      [Describe]

EXPANSION ECONOMICS (if applicable):
  Expansion rent:           [At then-current base rent / FMR / formula]
  TIA for expansion space:  [Amount / Pro-rated / None]
  Expansion space condition: [As-is / Landlord turnkey / tenant improvement]

STATUS:                     [Active — not yet exercised / Expired / Exercised on: date]
CONFIDENCE:                 [DEFINITE / HIGH / PROBABLE / PARTIAL / MISSING]
SOURCE:                     [§X, page Y; also Exhibit Z]
```

---

## Rent Schedule Abstraction

Build a complete line-item rent schedule for the full lease term, including all option
periods if exercisable with known economics. Present as a table:

```
| Period | Start Date | End Date | Monthly Base Rent | Annual Base Rent | $/RSF/Yr | Escalation Basis | Notes |
|--------|-----------|----------|------------------|-----------------|---------|-----------------|-------|
| Year 1 | [date]    | [date]   | $X,XXX           | $XX,XXX         | $XX.XX  | —               | 3 months free rent: [dates] |
| Year 2 | [date]    | [date]   | $X,XXX           | $XX,XXX         | $XX.XX  | 3% fixed step   | — |
| Year 3 | [date]    | [date]   | $X,XXX           | $XX,XXX         | $XX.XX  | 3% fixed step   | — |
| ...    |           |          |                  |                 |         |                 |     |
```

For **CPI escalations**: note base index period, measurement period, floor (minimum
increase), ceiling (maximum increase), and frequency. Mark future CPI-adjusted amounts
as `[CPI: TO BE COMPUTED at adjustment date]`.

For **FMR resets**: mark as `[FMR AT OPTION: TO BE DETERMINED per §X process]`.

**Total occupancy cost summary**: if CAM and operating expense passthrough data is
available, compute:

```
Year X Total Occupancy Cost = Base Rent + CAM Estimate + Tax Estimate + Insurance + Other
```

Flag as estimate and note basis.

---

## CAM and Operating Expense Deep Capture

The CAM and operating expense regime is the most complex and error-prone section of
any commercial lease abstract. The following precision is required:

**Gross-up provision**: When extracting a base year stop lease, determine:

- Whether expenses may be grossed up to a stated occupancy level
- The occupancy threshold (commonly 95%; note if different)
- Which expense categories are subject to gross-up (variable expenses only — taxes and
  insurance are fixed and should NOT be grossed up)
- The direction of the gross-up (grossing UP to reduce tenant's effective base year;
  grossing DOWN does not occur)

**Controllable cap mechanics**: Note explicitly whether the cap is:

- _Non-cumulative_: each year's increase is measured against the prior year (can compound
  if landlord hits the cap every year — Year 3 cap base is Year 2 actuals, not Year 1)
- _Cumulative_: each year's increase is measured against the base year (total increase
  capped from inception)
- Which expenses are excluded (taxes, utilities, and insurance are standard exclusions)

**Base year**: Record actual base year expenses if stated. If not stated, flag as
`[BASE YEAR EXPENSES NOT STATED — request from landlord for budget modeling]`.

**CAM reconciliation**: Extract the exact timeline and procedure. Flag the audit right
notice period (commonly tenant has 12–24 months from receipt of reconciliation to
audit; after that the reconciliation is deemed final).

---

## Extraction Completeness Classification

Assign one of these four statuses to each extracted data point:

| Status                   | Meaning                                                                                                  | Action                                                      |
| ------------------------ | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **DEFINITE** (0.95–1.0)  | Explicit, unambiguous data point with clear lease language                                               | State with confidence; record source section                |
| **HIGH** (0.80–0.94)     | Data point present but requires minor interpretation or cross-reference verification                     | State with brief caveat; record source section              |
| **PROBABLE** (0.60–0.79) | Data point present but requires substantive interpretation or depends on external document not available | State with reasoning; flag for professional review          |
| **PARTIAL** (0.40–0.59)  | Data point partially present; conflicting provisions; or depends on missing exhibit                      | Flag explicitly; describe what is known and what is missing |
| **MISSING** (0.00–0.39)  | No reference to this data point found in the lease package                                               | Record as MISSING; flag if this data point is material      |

**AMBIGUOUS** is a special status applied when the lease contains conflicting language
about the same data point (e.g., two sections state different cure periods). For ambiguous
items: record both versions, cite both sources, and flag for legal review.

---

## Structured Data Export

Produce a machine-readable export for portfolio management system import. The export
structure maps to the common field schema of Yardi, MRI, CoStar, and VTS.

**JSON export structure:**

```json
{
  "abstract_metadata": {
    "skill_version": "legalcode-lease-abstractor v1.0",
    "extraction_date": "YYYY-MM-DD",
    "extracted_by": "AI-assisted — requires professional review",
    "document_set": [
      "Lease (executed YYYY-MM-DD)",
      "Amendment No.1 (YYYY-MM-DD)",
      "..."
    ],
    "completeness_score": "X/14 categories complete",
    "confidence_overall": "HIGH / MEDIUM / LOW"
  },
  "property": {
    "address": "",
    "suite_unit": "",
    "building_name": "",
    "premises_rsf": null,
    "boma_standard": "",
    "building_total_rsf": null,
    "tenant_proportionate_share": null
  },
  "parties": {
    "landlord_legal_name": "",
    "landlord_notice_address": "",
    "tenant_legal_name": "",
    "tenant_notice_address": "",
    "guarantor": [{ "name": "", "type": "individual/entity", "scope": "" }]
  },
  "term": {
    "execution_date": "",
    "commencement_date": "",
    "rent_commencement_date": "",
    "expiration_date": "",
    "term_months": null,
    "free_rent_periods": [{ "start": "", "end": "", "components_abated": "" }]
  },
  "financial": {
    "lease_type": "",
    "base_rent_year_1_annual": null,
    "base_rent_year_1_monthly": null,
    "base_rent_per_rsf": null,
    "escalation_type": "",
    "escalation_rate_or_index": "",
    "rent_schedule": [
      {
        "period_start": "",
        "period_end": "",
        "monthly_rent": null,
        "annual_rent": null,
        "per_rsf": null
      }
    ],
    "security_deposit": {
      "amount": null,
      "form": "",
      "reduction_schedule": ""
    },
    "ti_allowance_total": null,
    "ti_per_rsf": null,
    "ti_use_it_or_lose_it_date": "",
    "cam_recovery_type": "",
    "tenant_cam_share_pct": null,
    "cam_cap_controllable_pct": null,
    "cam_cap_cumulative": null,
    "base_year": null,
    "gross_up_occupancy_threshold_pct": null
  },
  "critical_dates": {
    "rent_commencement": "",
    "lease_expiration": "",
    "renewal_option_1_latest_exercise": "",
    "renewal_option_1_earliest_exercise": "",
    "renewal_option_2_latest_exercise": "",
    "expansion_option_latest_exercise": "",
    "termination_option_latest_exercise": "",
    "ti_application_deadline": "",
    "cam_audit_right_deadline_yr1": "",
    "snda_delivery_deadline": "",
    "insurance_renewal_trigger": ""
  },
  "options": [
    {
      "type": "renewal/expansion/contraction/termination/rofo/rofr",
      "number": 1,
      "term_or_space": "",
      "exercise_window_earliest": "",
      "exercise_window_latest": "",
      "rent_at_option": "",
      "conditions_precedent": [],
      "status": "active/expired/exercised",
      "confidence": "DEFINITE/HIGH/PROBABLE/PARTIAL/MISSING"
    }
  ],
  "flags": {
    "missing_critical_clauses": [],
    "ambiguous_provisions": [],
    "partial_data_points": [],
    "missing_exhibits": [],
    "loi_drift_items": []
  }
}
```

**CSV export**: Flatten the JSON into a single-row record per lease using the field names
above as column headers. Multi-value fields (rent schedule, options) are delivered as
separate linked CSVs or as pipe-delimited values in a single field.

---

## Extraction Quality Gates

Run these five gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate                   | Rule                                                                                                                              | Fail Action                                                                                                             |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Source**             | Every extracted data point identifies its source location (section number, page, exhibit letter)                                  | Add source reference or flag `[SOURCE UNKNOWN]`                                                                         |
| **Completeness**       | All cross-references to other sections, exhibits, and schedules are noted and, where available, resolved                          | Note unresolved cross-references as `[CROSS-REF PENDING: §X]`                                                           |
| **Version**            | Extraction is from the consolidated current-terms document (original as amended); no superseded provision is extracted as current | Reconcile all amendments; note any term extracted from the unamended original as `[UNCONFIRMED — check Amendment No.X]` |
| **Ambiguity Flag**     | Any conflicting or unclear language is flagged for manual review rather than silently resolved                                    | Add `[AMBIGUOUS: describe conflict]` and record both versions                                                           |
| **Format Consistency** | All dates in ISO 8601 (YYYY-MM-DD); all currency in $/SF/year and $/month; all percentages stated as X.X%                         | Apply standard formatting throughout                                                                                    |

---

## Self-Interrogation

After completing the extraction, run these three passes silently before delivering:

**Pass 1 — Extraction Completeness**

- Have all 14 categories been addressed?
- Are there any exhibits or schedules referenced that were not in the package and
  could contain material terms (e.g., work letter defining landlord's work, insurance
  rider defining required coverages, guarantee form)? If so, flag each.
- Are there sections of the lease not captured in any of the 14 categories? (Check
  for unusual bespoke provisions, supplemental riders, building rules and regulations
  incorporated by reference.)

**Pass 2 — Ambiguity and Conflict Check**

- Are there any provisions that appear to conflict with each other? (Common: rent
  schedule in body vs. exhibit; cure periods in default section vs. notice section;
  permitted use in body vs. exhibit A use restriction; option conditions in body vs.
  option rider.)
- Are there any terms that are defined elsewhere in the lease in a way that changes the
  meaning of an extracted provision? (Example: "Tenant" defined to exclude affiliates
  changes the assignment analysis.)
- Are there any blanks, brackets, or draft language left in the executed lease?
  Flag each as `[INCOMPLETE DRAFTING: §X — contains blank / bracketed language]`.

**Pass 3 — Reasonableness Check**
Does the extracted data make internal sense?

- Commencement date is before expiration date ✓
- Rent commencement is not before commencement (unless error) ✓
- TI allowance amount is plausible relative to stated RSF ✓
- Option exercise window is before option term commences ✓
- Proportionate share denominator is ≥ numerator ✓
- Holdover rate is ≥ base rent ✓
- All absolute dates computed from relative references produce calendar dates
  in the correct time sequence ✓

Record `self_interrogation: PASS` or `FLAGGED: [issue description]` in the Glass Box.

---

## Confidence Scoring

Apply to each major extracted data point:

| Level        | Range     | Meaning                                                                                      | Extraction Example                                                                                                                                            |
| ------------ | --------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **DEFINITE** | 0.95–1.0  | Explicit, unambiguous language; no interpretation required                                   | "Base rent for Year 1 shall be $180,000 per annum, payable in monthly installments of $15,000." — DEFINITE (0.98)                                             |
| **HIGH**     | 0.80–0.94 | Data point clear but requires minor cross-reference or interpretation                        | CAM cap: "controllable expenses shall not increase more than 5% per year" — no statement on cumulative vs. non-cumulative — HIGH (0.88)                       |
| **PROBABLE** | 0.60–0.79 | Data point present but dependent on external document or requires substantive interpretation | Renewal rent: "fair market rent as agreed or determined per §X appraisal process" — §X appraisal process references an exhibit not provided — PROBABLE (0.68) |
| **PARTIAL**  | 0.40–0.59 | Data partially present; conflicting or incomplete                                            | Co-tenancy: lease states "Tenant shall have co-tenancy rights as set forth in Rider 3" — Rider 3 not in package — PARTIAL (0.45)                              |
| **MISSING**  | 0.00–0.39 | No reference found in lease package after thorough search                                    | Early termination right: full search of lease and all amendments, no early termination right found — MISSING (0.00)                                           |

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-lease-abstractor"
  version: "1.0"
  extraction_date: "[YYYY-MM-DD]"

  # DOCUMENT PACKAGE
  document: "[Lease title and execution date]"
  property_address: "[Address]"
  lease_type: "[Office / Retail / Industrial / Mixed-Use]"
  governing_law: "[Jurisdiction]"
  user_side: "[Tenant / Landlord / Acquirer / Lender / Other]"
  document_package:
    - "Original lease: [execution date]"
    - "Amendment No. 1: [date]"
    - "Exhibits available: [list by letter/number]"
    - "Missing exhibits: [list or None]"

  # EXTRACTION SCOPE AND COMPLETENESS
  extraction_scope: "[Full 14-category / Priority: specify]"
  categories_completed: "[X/14]"
  data_points_definite_high: "[count]"
  data_points_probable: "[count]"
  data_points_partial: "[count]"
  data_points_missing: "[count]"
  data_points_ambiguous: "[count]"

  # KEY EXTRACTIONS — VERIFICATION STATUS
  parties_confirmed: "[Yes / Partial / No]"
  dates_confirmed: "[Yes / Partial / No]"
  options_extracted: "[count] options; [count] with DEFINITE/HIGH confidence"
  financial_completeness: "[All / Most / Partial]"
  rent_schedule_complete: "[Yes / Partial / No]"
  cam_fully_extracted: "[Yes / Partial / No — describe gaps]"

  # QUALITY CHECKS
  amendment_reconciliation: "[Complete / Partial — [N] amendments incorporated /
    None — [reason]]"
  loi_delta_check: "[Complete / N/A — no LOI provided]"
  self_interrogation: "[PASS / FLAGGED: describe issues]"
  cross_reference_check: "[PASS / FLAGGED: list unresolved cross-references]"
  data_validation: "[PASS / FLAGGED: list reasonableness failures]"

  # FLAGS SUMMARY
  ambiguities_flagged:
    - "[Describe each ambiguity found]"
  conflicting_provisions:
    - "[Describe each conflict]"
  missing_critical_clauses:
    - "[List material clauses not found]"
  incomplete_drafting:
    - "[List any blanks or brackets found in executed lease]"
  missing_exhibits:
    - "[List exhibits referenced but not provided]"
  loi_drift_items:
    - "[List any terms that differ from LOI — N/A if no LOI]"

  # EXPORT STATUS
  export_formats_delivered: "[Markdown / JSON / CSV / All]"
  export_portfolio_ready: "[Ready for system import / Requires manual cleanup:
    describe]"

  # EXTERNAL TOOLS
  legalcode_mcp: "[Connected / Not connected]"
  external_tools_used: "[None / legalcode-mcp / perplexity-search]"

  # LIMITATIONS AND CAVEATS
  limitations:
    - "[Any scope limitation, assumption, or caveat applicable to this extraction]"
  confidence_overall: "[HIGH / MEDIUM / LOW] — [rationale]"
  reviewer:
    "AI-assisted extraction — recommend qualified real estate professional
    or attorney review before entry into portfolio system or reliance in
    any decision"
```

---

## Anti-Patterns in Lease Abstraction

What NOT to do when abstracting a commercial lease:

1. **Abstracting the original lease without amendments** — The single most common and
   consequential error. Always inventory all amendments first and reconcile every amended
   term before extracting. An abstract of the unamended original is worse than no abstract
   because it appears authoritative while reflecting superseded terms.

2. **Recording that an option exists without capturing the exercise window** — A renewal
   option is useless if the exercise deadline is not tracked. Always compute absolute
   earliest and latest exercise dates. Missed option windows are almost universally
   forfeited with no remedy.

3. **Confusing lease execution date with commencement date with rent commencement date** —
   These are three distinct dates. The execution date is when the lease was signed. The
   commencement date is when the term begins (possession). The rent commencement date is
   when rent first becomes payable (often after a free-rent period). Using the wrong date
   can cause months of misallocated financial records.

4. **Oversimplifying CAM as "pro-rata share"** — Recording only the tenant's proportionate
   share percentage without capturing the gross-up provision, the controllable expense cap,
   the base year, and all named exclusions produces a CAM abstract that is factually
   incomplete and financially misleading.

5. **Missing co-tenancy and exclusivity mechanics** — Recording "co-tenancy clause present"
   without capturing the trigger threshold, the remedy type, and the reconstitution
   provision. Tenants have paid full rent for 18+ months after anchor closure because
   the co-tenancy remedy was not tracked. Extract the full mechanics.

6. **Missing options buried in exhibits or riders** — Renewal, expansion, and termination
   options frequently appear in exhibits or riders appended to the main lease rather than
   in the lease body. Read all exhibits before concluding no options exist.

7. **Treating CPI-adjusted rent as unknowable** — CPI escalations cannot be precomputed
   without future CPI data, but the abstract should still record: the base index period,
   the adjustment measurement period, the floor, the ceiling, and the frequency. This
   allows future computation at adjustment time.

8. **Failing to track conditions precedent on options** — Options are commonly conditioned
   on: no default, tenant still in possession, no prior assignment or subletting. If these
   conditions are not tracked, the abstract may show an exercisable option that in fact
   cannot be exercised without curing the conditions.

9. **Abstracting TI allowance amount only, missing the use-it-or-lose-it deadline** — A
   large TI allowance left untracked for its application deadline can expire before the
   tenant has submitted draw requests, resulting in forfeiture.

10. **Ignoring the holdover rate** — Holdover at 125–150% of base rent is standard and
    creates significant financial exposure if a tenant holds over even briefly. The
    holdover rate and characterization (month-to-month vs. year-to-year) must be extracted.
    Year-to-year holdover converts a brief overhold into a full additional year of rent.

11. **Silently resolving ambiguous language** — When the same data point is stated
    differently in two places (e.g., cure period stated as 5 days in the notice section
    and 10 days in the default section), do not silently choose one version. Flag as
    AMBIGUOUS, record both versions, and note both sources.

12. **Not flagging the estoppel deemed-approved trap** — Many leases provide that if
    tenant does not respond to a landlord-delivered estoppel certificate within X days,
    the estoppel is deemed given in the form submitted by landlord. This is a significant
    risk that must be extracted explicitly and flagged for calendar tracking.

13. **Missing the assignment recapture right** — When a tenant submits an assignment or
    subletting request, many landlords have a right to recapture the premises rather than
    consent. This fundamentally changes the assignment economics. Missing this right
    produces an abstract that overstates the tenant's flexibility.

14. **Extracting proportionate share without the denominator definition** — The denominator
    for CAM cost recovery (how the building's total area is measured) varies — leased area,
    leasable area, occupied area, or total GLA. The choice of denominator can produce
    significantly different CAM charges. Always extract both the fraction and the
    denominator definition.

15. **Failing to note good-guy clause trigger conditions** — A good-guy clause that releases
    the guarantor upon surrender is extremely valuable to the guarantor, but it is
    conditional on: giving required notice, vacating in required condition, and leaving
    with no monetary defaults. Extracting "good-guy clause present" without these
    conditions overstates the guarantor's protection.

---

## Writing Standards

Before delivering any output:

1. **Accuracy first**: If the lease language is ambiguous or the extracted value is less
   than DEFINITE confidence, say so — never present uncertain extractions as certain.
   Confident but wrong data is worse than uncertain data flagged for review.

2. **Source every extraction**: Every extracted value should identify its source provision.
   Use the format `[§4.2, p.12]` inline with extracted values. This allows rapid
   verification against the original document.

3. **Exact language for critical terms**: For options, rent escalations, and co-tenancy
   provisions, quote the exact lease language alongside the extracted summary. This
   prevents the summary from inadvertently changing the meaning of the original.

4. **Absolute dates for all relative references**: Never leave a relative date reference
   uncomputed if the base date is known. Always show the formula: `[COMPUTED: expiration
(YYYY-MM-DD) minus 12 months = YYYY-MM-DD]`.

5. **Flag gaps explicitly**: A data point that is genuinely absent from the lease is more
   useful to the reader as `MISSING — no early termination right found` than as a blank
   field. The absence of a right is as material as its presence.

6. **No legal interpretation**: The abstractor's role is extraction, not legal advice.
   When the lease says "at fair market rent as mutually agreed or as determined by
   appraisal," extract that language faithfully — do not interpret what FMR likely is.

7. **Portfolio-system-ready formatting**: Structure the markdown output so that section
   headers, tables, and flagged items allow rapid navigation. Use consistent field labels
   across every abstract in a portfolio for comparability.

---

## Output Format Template

```markdown
# LEASE ABSTRACT — [Property Address, Suite/Unit]

**Extracted by**: legalcode-lease-abstractor | **Date**: YYYY-MM-DD
**Version**: [Executed lease (date) + Amendment Nos. X as of date]
**Confidence overall**: HIGH / MEDIUM / LOW
**Completeness**: [X/14 categories complete; Y data points PARTIAL/MISSING]

---

## 1. Document Inventory

| Document        | Type       | Date   | Scope               |
| --------------- | ---------- | ------ | ------------------- |
| [Lease title]   | Original   | [date] | Full agreement      |
| Amendment No. 1 | Amendment  | [date] | Modifies §§ X, Y, Z |
| Exhibit A       | Floor Plan | [date] | Premises RSF        |
| ...             |            |        |                     |

⚠️ **Missing exhibits**: [List or "None"]

---

## 2. Parties and Property

| Field                        | Value | Confidence | Source |
| ---------------------------- | ----- | ---------- | ------ |
| Landlord (legal name)        |       |            |        |
| Landlord (notice address)    |       |            |        |
| Tenant (legal name)          |       |            |        |
| Tenant (notice address)      |       |            |        |
| Guarantor                    |       |            |        |
| Property address             |       |            |        |
| Suite / Unit                 |       |            |        |
| Premises RSF (rentable)      |       |            |        |
| Building RSF (total)         |       |            |        |
| Tenant's proportionate share |       |            |        |
| BOMA standard                |       |            |        |

---

## 3. Lease Term and Critical Dates

| Field                     | Value | Confidence | Source |
| ------------------------- | ----- | ---------- | ------ |
| Execution date            |       |            |        |
| Commencement date         |       |            |        |
| Rent commencement date    |       |            |        |
| Free rent period(s)       |       |            |        |
| Lease expiration date     |       |            |        |
| Term (months)             |       |            |        |
| Holdover characterization |       |            |        |
| Holdover rate             |       |            |        |

---

## 4. Base Rent and Rent Schedule

[Rent schedule table — see §8]

**Escalation type**: [describe]
**Free rent / abatement**: [describe]

---

## 5. Operating Expenses / CAM

**Lease type**: [Gross / NNN / Base Year Stop / Expense Stop / etc.]
**Tenant's proportionate share**: [X%]
**Base year / Expense stop**: [Year or $/SF]

| CAM Field                         | Value | Confidence | Source |
| --------------------------------- | ----- | ---------- | ------ |
| Controllable cap                  |       |            |        |
| Cap: cumulative or non-cumulative |       |            |        |
| Gross-up threshold                |       |            |        |
| Named exclusions                  |       |            |        |
| CAM reconciliation deadline       |       |            |        |
| Tenant audit right window         |       |            |        |

---

## 6. TI Allowance and Construction

| Field                      | Value | Confidence | Source |
| -------------------------- | ----- | ---------- | ------ |
| TI allowance total         |       |            |        |
| TI per RSF                 |       |            |        |
| Use-it-or-lose-it deadline |       |            |        |
| Disbursement conditions    |       |            |        |
| Landlord's work scope      |       |            |        |
| Delivery deadline          |       |            |        |
| Restoration obligations    |       |            |        |

---

## 7. Options Summary

[One option record per option — see §10 template]

### Critical Option Dates — Calendar Summary

| Option     | Earliest Exercise | Latest Exercise | Recommended Notice | Status |
| ---------- | ----------------- | --------------- | ------------------ | ------ |
| [Option 1] | [COMPUTED]        | [COMPUTED]      | [Latest − 60d]     | Active |
| ...        |                   |                 |                    |        |

---

## 8. Security Deposit and Guarantee

| Field                        | Value | Confidence | Source |
| ---------------------------- | ----- | ---------- | ------ |
| Security deposit amount      |       |            |        |
| Deposit form                 |       |            |        |
| Reduction schedule           |       |            |        |
| Guarantor                    |       |            |        |
| Guarantee scope              |       |            |        |
| Good-guy trigger             |       |            |        |
| Good-guy conditions          |       |            |        |
| Guarantor release conditions |       |            |        |

---

## 9. Permitted Use, Exclusivity, and Co-Tenancy

**Permitted use**: [Exact language]
**Exclusivity**: [Yes — describe / No]
**Co-tenancy**: [Yes — describe / No]
**Continuous operation**: [Yes — describe / No]

---

## 10. Assignment and Subletting

| Field                             | Value | Confidence | Source |
| --------------------------------- | ----- | ---------- | ------ |
| Landlord consent required         |       |            |        |
| Consent standard                  |       |            |        |
| Permitted transfers               |       |            |        |
| Recapture right                   |       |            |        |
| Profit-sharing                    |       |            |        |
| Tenant liability after assignment |       |            |        |

---

## 11. Insurance Requirements

| Coverage               | Tenant Required    | Landlord Required | Additional Insured | Source |
| ---------------------- | ------------------ | ----------------- | ------------------ | ------ |
| CGL — per occurrence   |                    |                   |                    |        |
| CGL — annual aggregate |                    |                   |                    |        |
| Umbrella               |                    |                   |                    |        |
| Property / contents    |                    |                   |                    |        |
| Business interruption  |                    |                   |                    |        |
| Workers' comp          |                    |                   |                    |        |
| Waiver of subrogation  | Mutual / One-sided |                   | N/A                |        |

---

## 12. Maintenance and Repair

| Obligation              | Landlord | Tenant | Source |
| ----------------------- | -------- | ------ | ------ |
| Structural              |          |        |        |
| Roof                    |          |        |        |
| Exterior walls          |          |        |        |
| HVAC                    |          |        |        |
| Plumbing / electrical   |          |        |        |
| Common areas            |          |        |        |
| Interior non-structural |          |        |        |

---

## 13. Default and Cure Summary

| Default Type                    | Notice | Cure Period | Source |
| ------------------------------- | ------ | ----------- | ------ |
| Monetary default                |        |             |        |
| Non-monetary default            |        |             |        |
| Complex default (extended cure) |        |             |        |
| Landlord default                |        |             |        |

---

## 14. SNDA and Estoppel

| Field                           | Value | Confidence | Source |
| ------------------------------- | ----- | ---------- | ------ |
| SNDA required                   |       |            |        |
| SNDA delivery deadline          |       |            |        |
| NDA conditioned on no default   |       |            |        |
| Estoppel certificate obligation |       |            |        |
| Estoppel response deadline      |       |            |        |
| Deemed-approved provision       |       |            |        |

[JURISDICTION-SPECIFIC UK: Security of tenure status — [contracted out / not contracted out]]

---

## 15. LOI Delta Summary (if LOI provided)

| LOI Term | LOI Agreement | Lease Provision | Match? | Notes |
| -------- | ------------- | --------------- | ------ | ----- |
| ...      |               |                 |        |       |

---

## 16. Flags and Issues

### ⚠️ AMBIGUOUS Provisions

[List each with competing interpretations and source sections]

### ⚠️ MISSING Critical Clauses

[List each absent clause and its significance]

### ⚠️ PARTIAL Extractions

[List each partial data point with what is known and what is missing]

### ⚠️ Missing Exhibits / Cross-References Pending

[List each]

### ⚠️ LOI Drift (if LOI provided)

[List each term that differs from LOI]

---

## 17. Structured Data Export

[JSON export block]
[CSV file path or inline CSV]

---

## 18. Glass Box Audit Trail

[YAML block per §15]
```

---

## Localization Notes

When abstracting leases in non-US jurisdictions, adapt the following:

**United Kingdom:**

- Use UK lease terminology: "demised premises" not "leased premises"; "rent review" not
  "escalation"; "service charge" not "CAM"; "break clause" not "early termination option"
- Record Landlord and Tenant Act 1954 status (contracted out or not) — critical for
  renewal rights
- Note RICS Code of Practice on Service Charges (2020) compliance
- Flag any SDLT/LTT/LBTT implications noted in the lease

**Australia:**

- Note whether Retail Leases Act applies (state-specific — NSW 1994, VIC 2003, QLD 1994,
  WA 1985, SA 1995, TAS 1993) and any mandatory disclosure statement delivered
- Extract any regulated outgoings categories under applicable state Retail Leases Act
- Note ACCC / state-level mandatory code provisions if relevant
- Record NZ equivalents if New Zealand lease (Property Law Act 2007; ADLS lease standard)

**Europe (general):**

- Note civil law jurisdiction implications — leases may be subject to mandatory provisions
  that cannot be contracted out; flag any statutory protections not addressed in the lease
- Record indexation mechanism — EU leases frequently use HICP or national CPI indices
  with different mechanics than US CPI adjustments

---

## External Tool Integration

**With legalcode-mcp connected:**

- In Step 4 and Step 5, search for jurisdiction-relevant statutes governing commercial
  leases, CAM recovery limits, and option enforceability rules in the identified governing
  law jurisdiction
- Verify current text of any statutory provisions cited in the lease (e.g., Landlord and
  Tenant Act 1954 status, Retail Leases Act provisions, ADA scope)
- Flag as VERIFIED in the Glass Box any citation confirmed via legalcode-mcp
- Use to resolve AMBIGUOUS provisions where statutory construction or jurisdiction-specific
  interpretation is needed

**Without legalcode-mcp:**

- Proceed with extraction and flag all statutory cross-references as `[VERIFY against
current statute]`
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Extraction quality is not impaired — the skill's core value is faithful data extraction,
  not legal interpretation

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis built from:

- Structural analysis of `legalcode-contract-review`, `legalcode-commercial-lease-review`,
  and `legalcode-redline-generator` reference skills (2-agent structural analysis pass)
- Web research synthesizing industry sources on lease abstraction best practices including
  BOMA standards, NAIOP/IREM professional frameworks, and practitioner guidance from CoStar,
  PropertyMetrics, REBOLease, Springbord, Prophia, Occupier, Adventures in CRE, RIOO,
  and Bryckel AI
- The 14-clause taxonomy is aligned with the `legalcode-commercial-lease-review` skill to
  ensure consistent clause coverage across the abstraction and review workflows
- Anti-patterns derived from industry-documented error rates (~10% material error rate at
  portfolio scale) and the most commonly cited extraction failures in commercial lease
  abstraction practice
