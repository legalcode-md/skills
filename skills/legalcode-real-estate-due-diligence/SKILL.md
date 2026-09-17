---
name: legalcode-real-estate-due-diligence
description: Conducts comprehensive real estate due diligence for property acquisitions, financing, development,
  and disposal transactions. Use when acquiring commercial or residential property, securing real estate
  financing, conducting pre-development due diligence, or reviewing a vendor's due diligence pack.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Conducts comprehensive real estate due diligence for property acquisitions, financing, development, and disposal transactions. Covers eight workstreams: title examination, survey and boundary review, environmental assessments (Phase I/II ESA), zoning and planning compliance, permit and certificate verification, lease audit, property tax review, and encumbrance identification. Generates a PASS/FLAG/FAIL risk-scored report with priority tiers and actionable remediation recommendations. Use when acquiring commercial or residential property, securing real estate financing, conducting pre-development due diligence, or reviewing a vendor's due diligence pack. Supports UK conveyancing (Land Registration Act 2002, RICS practice standards, SDLT), US commercial real estate (ASTM E1527-21 Phase I ESA, ALTA/NSPS survey, title insurance), and Australian conveyancing (Torrens title, NEPM contaminated land, state planning approvals). Jurisdiction-agnostic framework with deep UK/US/AU localization markers. Also triggers on: property purchase checklist, title search, environmental site assessment, zoning compliance check, lease due diligence, real estate risk report, conveyancing due diligence, property acquisition checklist.


# Legalcode Real Estate Due Diligence

> **Disclaimer**: This skill provides a framework for AI-assisted real estate due diligence.
> It does not constitute legal advice. All outputs must be reviewed by a qualified legal
> professional (solicitor, attorney, or conveyancer) licensed in the relevant jurisdiction
> before any reliance or transaction decision is made. Property law is highly
> jurisdiction-specific and changes frequently. Statutory and case law references cited
> from memory carry hallucination risk — verify against authoritative sources before
> relying on them.

## Purpose and Scope

This skill conducts structured real estate due diligence across eight workstreams,
producing a risk-classified report with actionable findings and remediation steps.

**Covers:**

- Title examination: title search, ownership verification, title insurance analysis (US),
  Land Registry filings (UK), Torrens title (AU)
- Survey and boundary review: ALTA surveys (US), RICS surveys (UK), registered survey
  plans (AU), boundary disputes, flood zone assessment
- Environmental due diligence: Phase I/II ESA (ASTM E1527-21 US), desktop/intrusive
  studies (UK/AU), contaminated land registers, CERCLA liability (US), Part IIA EPA
  1990 (UK), NEPM 2013 (AU)
- Zoning and planning: use class compliance, planning permissions/variances, overlay
  districts, non-conforming uses
- Permits and certificates: building permits, certificates of occupancy/completion,
  fire and safety compliance, ADA compliance (US), EPC ratings (UK)
- Lease audit: rent rolls, lease expiry and renewal options, permitted use, make-good
  obligations, outgoings, tenant covenant strength
- Property tax: tax liens, assessments, stamp duty/transfer duty, SDLT (UK), GST (AU)
- Encumbrances: easements, restrictive covenants, charges, mortgages, overriding
  interests, adverse possession risks

**Does not:**

- Draft purchase contracts, leases, or financing documents
- Conduct physical building inspections (that is a surveyor's function)
- Provide legal advice or replace qualified conveyancing counsel
- Apply to all jurisdictions — covers UK, US, and Australia with [JURISDICTION-SPECIFIC]
  markers; other jurisdictions require separate analysis

## Jurisdiction and Governing Law

This skill covers three primary jurisdictions with deep localization. For each jurisdiction,
the legal framework differs significantly:

| Jurisdiction                | Title System                                                 | Key Statutes                                                           | Environmental Standard                                             | Survey Standard                  |
| --------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------- | ------------------------------------------------------------------ | -------------------------------- |
| **UK (England & Wales)**    | Land Registration Act 2002; unregistered land under LPA 1925 | EPA 1990 Part IIA; TCPA 1990; LTA 1954; SDLT (Finance Act 2003)        | RICS Phase I ESA (desktop + walk-over)                             | RICS Measured Survey             |
| **US (Federal + State)**    | Deed recording / title insurance system                      | CERCLA 42 U.S.C. § 9601 et seq.; Clean Water Act; state recording acts | ASTM E1527-21 Phase I; ASTM E1903-19 Phase II                      | ALTA/NSPS 2021 Minimum Standards |
| **Australia (State-based)** | Torrens indefeasibility (state-based land titles)            | State conveyancing acts; NEPM 1999/2013; state planning acts           | NEPM Phase 1 (Preliminary Site Investigation) / Phase 2 (Detailed) | State survey standards           |

[JURISDICTION-SPECIFIC] For jurisdictions outside UK/US/AU, replace the applicable
framework with local equivalents. Engage local counsel to identify mandatory pre-contract
enquiries, search requirements, and disclosure obligations.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
intent, the workflow pauses and asks when:

- The answer would change the scope or direction of the due diligence
- Jurisdiction or transaction type determines which workstreams are mandatory
- A finding requires business context to classify correctly as FLAG or FAIL
- The user must decide whether to proceed, renegotiate, or walk away

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

### Step 1: Accept Property Details

Accept property information in any of these formats:

- **Address and description**: property address, type, size, current use
- **Due diligence pack**: vendor-supplied documents (title register, searches, surveys, leases)
- **Document set**: uploaded PDFs, title certificates, environmental reports, lease extracts
- **URL or CLM link**: link to a document repository or deal room

If no property information is provided, ask the user to describe the property or provide
documents.

### Step 2: Gather Transaction Context

**⟁ CLARIFY** — Before beginning, ask the user these questions. Present as structured
options where possible:

1. **Transaction type**: What is the purpose of this due diligence?
   - Options: **Purchase (freehold/fee simple)**, **Purchase (leasehold/leasehold interest)**,
     **Financing / lender due diligence**, **Pre-development site assembly**, **Lease of
     premises (tenant's review)**, **Lease (landlord's review)**, **Disposal / sale**, **Other**
   - _Why this matters_: Determines which workstreams are mandatory and the analysis perspective.

2. **Jurisdiction**: Which jurisdiction does the property sit in?
   - Options: **England & Wales (UK)**, **Scotland**, **Northern Ireland**, **United States
     — specify state**, **Australia — specify state/territory**, **Other (specify)**
   - _Why this matters_: The entire legal framework, searches, and standards depend on jurisdiction.

3. **Property type**:
   - Options: **Commercial office**, **Retail / mixed-use**, **Industrial / warehouse**,
     **Residential (single)**, **Residential (multi-unit/BTR)**, **Development site (greenfield)**,
     **Development site (brownfield)**, **Hospitality / leisure**, **Agricultural**, **Other**
   - _Why this matters_: Determines environmental risk profile, lease audit scope, and
     zoning analysis requirements.

4. **Role**: Who does this analysis serve?
   - Options: **Purchaser**, **Lender**, **Tenant**, **Developer**, **Vendor (preparing
     vendor pack)**, **Other**
   - _Why this matters_: Determines the risk perspective — a lender focuses on security
     of title and enforceability; a developer focuses on planning and environmental.

5. **Scope of review**: What depth is needed?
   - Options: **Full due diligence** (all 8 workstreams), **Priority review** (title +
     environmental + zoning only), **Single workstream** (specify which), **Lender's
     abbreviated review** (title + environmental + leases)
   - _Why this matters_: Allows appropriate scope management for complex portfolios.

6. **Timeline**: When is exchange/completion/closing scheduled?
   - Options: **Urgent (< 2 weeks)**, **Standard (2-6 weeks)**, **Flexible (> 6 weeks)**
   - _Why this matters_: Affects how to prioritize findings and flag outstanding items.

If the user provides partial context, proceed with stated assumptions. For example:
"Assuming England & Wales jurisdiction, freehold purchase, purchaser's perspective — let
me know if any of these are wrong."

### Step 3: Gather Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** to build a working legal reference for this review.

Search for jurisdiction-relevant authority across:

- Title registration statutes and overriding interests
- Environmental liability regime and contaminated land registers
- Planning and zoning framework
- Applicable stamp duty / transfer duty / SDLT thresholds
- Mandatory pre-contract enquiries and search requirements
- Lease-specific statutes (e.g., LTA 1954 for business tenancies in England)

Save results to a local temp file (e.g., `/tmp/legalcode-re-dd-authority.md`).

**If legalcode-mcp is not connected:**

- Mark all statutory references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Proceed using general knowledge of UK/US/AU property law, but flag that legal authority
  requires independent verification

**⟁ CLARIFY** — If the jurisdiction raises unusual complexity (e.g., tribal land US,
commonhold UK, community title AU, foreign ownership restrictions), flag this to the user
before proceeding and confirm the correct legal framework.

### Step 4: Title Examination

Conduct a systematic title examination. See **Workstream 1: Title Examination** below
for the full checklist.

**⟁ CLARIFY** — If any of the following are discovered, pause and ask before proceeding:

- **Unregistered title (UK)**: "The title appears unregistered. First registration will
  be required on purchase. Do you want me to flag all deduction of title requirements?"
- **Gap in chain of title (US)**: "There is a gap in the recorded chain of title between
  [year A] and [year B]. Title insurance will likely be required. Should I proceed
  noting this defect, or would you like to investigate further?"
- **Foreign ownership restriction (AU/US)**: "The property may be subject to foreign
  investment restrictions [FIRB AU / CFIUS US]. Is the purchaser a foreign person or entity?"
- **Beneficial interest / trust**: "The title is held by a trustee. Are there overreaching
  requirements or beneficiary consent issues that need to be addressed?"

### Step 5: Survey and Boundary Review

Review all available survey materials. See **Workstream 2: Survey and Boundaries** below.

**⟁ CLARIFY** — For investment or development acquisitions:

- "No ALTA survey [US] / no current measured survey [UK] / no registered plan check [AU]
  has been provided. For a transaction of this type, I recommend [ordering an ALTA / commissioning
  a measured survey / obtaining a current survey plan]. Should I flag this as a Tier 1 item?"

### Step 6: Environmental Due Diligence

Review all environmental materials and assess adequacy. See **Workstream 3: Environmental
Due Diligence** below.

**⟁ CLARIFY** — If the property has industrial, commercial, or former-use history that
raises environmental concern:

- "A Phase I ESA [US] / Phase I desktop study [UK] / Preliminary Site Investigation [AU]
  has [been provided / not been provided]. Based on the property's apparent history and
  use, a Phase II intrusive investigation [may / is likely to] be required. Do you want
  me to flag this as a Tier 1 condition?"

### Step 7: Zoning and Planning Review

Verify permitted use and planning compliance. See **Workstream 4: Zoning and Planning** below.

**⟁ CLARIFY** — If the current or intended use does not clearly match the recorded
zoning/use class:

- "The property's current use appears to be [X], but the zoning/use class is [Y].
  [A change of use application / a variance / a development application] may be required
  to regularize or expand the use. Is the intended use confirmed? This may affect value
  and insurability."

### Step 8: Permit and Certificate Verification

Check that all permits, consents, and certificates are in order. See **Workstream 5:
Permits and Certificates** below.

### Step 9: Lease Audit

**⟁ CLARIFY** — Ask the user to confirm before commencing:

- "Does the property have existing tenants? If yes, please provide the rent roll and
  lease documents. If no tenants, I will skip this workstream."

If applicable, conduct the lease audit. See **Workstream 6: Lease Audit** below.

### Step 10: Property Tax Review

Review all property tax obligations. See **Workstream 7: Property Tax** below.

### Step 11: Encumbrance Identification

Identify all encumbrances, burdens, and restrictions on title. See **Workstream 8:
Encumbrances** below.

### Step 12: Compile Risk Summary

After completing all applicable workstreams:

1. Aggregate all PASS/FLAG/FAIL findings into the risk matrix
2. Classify each finding by priority tier (see **Prioritization Framework**)
3. Identify all Tier 1 (deal-blocking) findings and present them first

**⟁ CLARIFY** — For any FAIL findings classified as Tier 1 (deal-breakers):

- "I've identified [N] FAIL findings that may block or materially affect the transaction.
  Before completing the report, do you want me to: (A) Complete the full report with
  all findings, (B) Present only the Tier 1 FAIL findings and pause, or (C) Provide
  a brief summary for a go/no-go decision?"

### Step 13: Quality Verification

Before delivering the report:

1. Run the 5 Citation Quality Gates silently — revise any failures before delivery
2. For every FAIL item, run the 3-pass Self-Interrogation
3. Assign Confidence Scores to all material findings
4. Verify all 8 workstreams are addressed or explicitly scoped out
5. Generate and append the Glass Box Audit Trail

---

## Due Diligence Workstreams

### Workstream 1: Title Examination

**Purpose**: Verify the vendor holds good, marketable title free of undisclosed defects.

#### 1a. Registered Title Review

| Item                                                                                      | What to Check                                                                                     | Red Flags                                                                    |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Proprietorship register (UK) / Grantor-Grantee chain (US) / Certificate of Title (AU)** | Registered owner matches vendor; ownership clearly established                                    | Owner mismatch; unexplained transfers; recently acquired from unusual source |
| **Charges register (UK) / Deed of Trust / Mortgage (US) / Dealings (AU)**                 | All mortgages, charges, and liens identified                                                      | Undisclosed mortgages; charges not to be discharged on completion            |
| **Property register (UK) / Legal description (US) / Registered plan (AU)**                | Correct property description; correct lot/plan; no ambiguity                                      | Missing parcels; overlapping descriptions                                    |
| **Restrictions and notices (UK) / Covenants (US/AU)**                                     | All restrictions identified and reviewed                                                          | Restrictions that prevent intended use                                       |
| **Class of title (UK)**                                                                   | Absolute title preferred; possessory/qualified/good leasehold require investigation               | Non-absolute title without insurance                                         |
| **Overriding interests (UK — LRA 2002 Sch 3)**                                            | Inspect for occupation by persons other than registered proprietor; legal easements; short leases | Unregistered interests of persons in actual occupation                       |
| **Title insurance (US — Schedule B exceptions)**                                          | List all Schedule B exceptions; assess materiality                                                | Broad blanket exceptions; exceptions affecting intended use                  |
| **Indefeasibility (AU — Torrens)**                                                        | Confirm no caveats registered; no adverse possessor's claim pending                               | Caveats not explained; pending court orders                                  |

#### 1b. UK-Specific Searches

[JURISDICTION-SPECIFIC: England & Wales only]

| Search                                                | Purpose                                                          | Key Issues                                           |
| ----------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------- |
| **Official copies (HMLR)**                            | Current register of title                                        | See above                                            |
| **LLC1 (Local Land Charges)**                         | Financial charges and restrictions registered by local authority | Financial charges, prohibition on development        |
| **CON29 (enquiries of local authority)**              | Planning, highways, drainage, regeneration                       | Road schemes; enforcement notices; CIL liability     |
| **CON29O (optional)**                                 | Public footpaths, common land, radon, noise                      | Radon-affected area                                  |
| **Water and drainage search (CON29DW)**               | Sewer connection, water authority routes                         | Drains crossing land; adoption status                |
| **Environmental search (e.g., Groundsure)**           | Flood risk, contamination, planning constraints                  | Flood risk zones 2/3; contaminated land              |
| **Coal Authority search**                             | Mining subsidence risk                                           | Mining area; subsidence                              |
| **Chancel repair search**                             | Potential liability for chancel repair of a church               | Potential liability in historic parishes             |
| **Commons registration search (CR21)**                | Rights of common; village green applications                     | Village green application pending                    |
| **Land charges search (K15/K16 — unregistered land)** | Puisne mortgages, equitable charges, restrictive covenants       | Undisclosed charges                                  |
| **Index Map search (SIM — unregistered land)**        | Confirm title is unregistered                                    | Partial registration                                 |
| **Pre-contract enquiries (CPSE or TA forms)**         | Seller's replies on material facts                               | False or incomplete replies; material latent defects |

[JURISDICTION-SPECIFIC: Scotland — separate system; engage Scottish solicitors for Registers of Scotland, ARTL, and Property Enquiry Certificates]

#### 1c. US-Specific Title Requirements

[JURISDICTION-SPECIFIC: United States only]

| Item                                            | What to Check                                                                                             | Red Flags                                                       |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Preliminary title report / title commitment** | Schedule A (insured interest, legal description); Schedule B-I (requirements); Schedule B-II (exceptions) | Broad B-II exceptions; requirements not capable of satisfaction |
| **Chain of title**                              | Continuous chain for statutory period (typically 30-60 years, varies by state)                            | Gaps; straw man deeds; unusual transfers                        |
| **Judgment liens**                              | Search judgment indices for lien creditors                                                                | Unsatisfied judgments against seller                            |
| **Mechanics' liens**                            | Recent construction work creating lien risk                                                               | Unpaid contractors; lien period not expired                     |
| **Lis pendens**                                 | Pending litigation affecting title                                                                        | Active foreclosure; partition; title dispute                    |
| **Federal tax liens**                           | IRS Form 668; state tax liens                                                                             | Undischarged federal / state tax liens                          |
| **UCC Article 9 fixture filings**               | Fixtures potentially encumbered                                                                           | Fixtures claimed as personal property by creditor               |
| **HOA / condo association records**             | CC&Rs, HOA dues, special assessments; resale certificates                                                 | Special assessments outstanding; pending litigation             |
| **FIRPTA compliance**                           | Foreign seller withholding requirements                                                                   | Foreign seller — 15% withholding required [VERIFY]              |
| **Gap period coverage**                         | Title insurance commitment to closing date                                                                | Uninsured gap between commitment and closing                    |

#### 1d. Australian Title Requirements

[JURISDICTION-SPECIFIC: Australia only]

| Item                                         | What to Check                                                             | Red Flags                                         |
| -------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------- |
| **Title search (eCT / manual CT)**           | Registered proprietor; registered dealings; mortgages; caveats; easements | Caveats with no explanation; undisclosed dealings |
| **Property certificate / title certificate** | Current search including all dealings                                     | Date-currency of certificate                      |
| **Crown grants**                             | Nature of original grant; any Crown reservations                          | Crown reservations affecting use                  |
| **FIRB approval**                            | Foreign Investment Review Board clearance for foreign purchasers          | Foreign purchaser without FIRB approval           |
| **PEXA workspace / settlement**              | Electronic conveyancing (PEXA) workspace preparation                      | Discrepancies between title and workspace         |
| **Land tax certificate**                     | No unpaid land tax as statutory charge on land                            | Outstanding land tax; incorrect exemption applied |
| **Strata / community title (if applicable)** | Strata plan, by-laws, lot entitlement, sinking fund, strata roll, levies  | Special levies; strata disputes; by-law breaches  |
| **Body corporate disclosure**                | Disclosure statement per state requirements                               | Material non-disclosures                          |

---

### Workstream 2: Survey and Boundaries

**Purpose**: Confirm physical boundaries, improvements, encroachments, and flood risk.

| Item                         | What to Check                                                                               | Red Flags                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Boundaries**               | Do fences, walls, and structures match the title plan / survey?                             | Encroachments onto or by neighboring land; disputed boundaries                               |
| **Easement locations**       | Easements shown on title plan — do they correspond to actual use on the ground?             | Easements over buildable land; informal easements not on title                               |
| **Access**                   | Legal right of access to the property (public road / private easement); width and condition | Access over third-party land without registered easement                                     |
| **Flood risk**               | FEMA Flood Zone (US); Environment Agency Flood Zone 2/3 (UK); catchment/flood mapping (AU)  | Zone A or AE (US = high risk); Zone 3 (UK = 1% annual chance); identified overland flow (AU) |
| **Physical condition**       | Condition of improvements, structures, retaining walls, drainage                            | Structural defects; unapproved structures; retaining wall failure risk                       |
| **Contamination indicators** | Visible site contamination (staining, dead vegetation, drums, UST vents)                    | Visible RECs not disclosed in Phase I                                                        |
| **Party walls (UK)**         | Party Wall Act 1996 compliance; party wall notices; awards                                  | Missing party wall awards for recent works                                                   |

#### UK Survey Standards

[JURISDICTION-SPECIFIC: England & Wales]

- RICS Level 1 (Condition Report): Basic survey for standard residential property
- RICS Level 2 (HomeBuyer Report): Standard residential survey with valuation
- RICS Level 3 (Building Survey): Comprehensive structural survey for older/complex buildings
- RICS Measured Survey: For commercial/investment property — confirms GIA/NIA/GEA areas

#### US Survey Standards

[JURISDICTION-SPECIFIC: United States]

- ALTA/NSPS 2021 Land Title Survey: Gold standard for commercial acquisitions; confirms
  legal description, improvements, easements, encroachments; Table A optional items
  include flood zone, utilities, parking count
- Topographic survey: Required for development; establishes contours and drainage
- FEMA flood zone determination: Mandatory for federally backed financing; Letter of Map
  Amendment (LOMA) process for incorrect designations

#### Australian Survey Standards

[JURISDICTION-SPECIFIC: Australia]

- Registered survey plan: State-registered plan showing lot boundaries
- Feature and level survey: Shows improvements, features, and levels for development
- Identification survey: Confirms boundaries of existing improvements
- SWIM (Survey and Infrastructure Works Methodology): State-specific

---

### Workstream 3: Environmental Due Diligence

**Purpose**: Identify environmental contamination, regulatory liability, and remediation
obligations that could affect value, use, or financing.

This is the highest-risk workstream for brownfield or former industrial sites. Proceed
with heightened care.

#### 3a. Phase I / Desktop Environmental Assessment

| Item                                                | What to Check                                                                         | Red Flags                                                           |
| --------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Recognized Environmental Conditions (RECs — US)** | Phase I identifies RECs per ASTM E1527-21; each REC must be assessed                  | Petroleum releases; chlorinated solvents; industrial waste          |
| **Historical uses**                                 | Aerial photography; fire insurance maps (Sanborn US); OS maps (UK); state EPA records | Prior gas stations, dry cleaners, industrial facilities, rail yards |
| **USTs / ASTs**                                     | Records of underground/aboveground storage tanks; closure documentation               | Active or closed USTs with no assessment; LUST (leaking UST)        |
| **Regulatory database review**                      | CERCLIS / NPL (US); contaminated land register (UK EPA); state EPA databases (AU)     | Proximate Superfund/contaminated land sites; hydraulic connectivity |
| **Regulatory interviews**                           | Contact with state/local environmental authority                                      | Pending enforcement actions; compliance orders                      |
| **Vapor intrusion**                                 | Proximity to chlorinated solvent sites; pathway analysis                              | Vapor intrusion pathway to occupied structures                      |
| **Asbestos**                                        | Pre-1980s construction (US: likely ACM); pre-2000 (UK/AU: likely ACM)                 | ACM in poor condition; scheduled for disturbance                    |
| **Lead paint**                                      | Pre-1978 construction (US); older buildings (UK/AU)                                   | Lead paint in deteriorating condition; occupancy by children        |
| **Radon**                                           | CON29O search (UK); EPA radon zone map (US); state radon guidance (AU)                | Radon-affected area; basement occupancy                             |
| **PFAS**                                            | Proximity to airports, military, fire training areas                                  | Active or historical PFAS use; impacted groundwater                 |
| **Wetlands (US)**                                   | Section 404 Clean Water Act; Army Corps jurisdiction; delineation                     | Wetlands on or adjacent to site; Section 404 permit required        |

[JURISDICTION-SPECIFIC: US — CERCLA 42 U.S.C. § 9601 et seq. Innocent Purchaser Defense
(IPD) requires completion of All Appropriate Inquiries (AAI) per 40 C.F.R. Part 312,
which references ASTM E1527-21. Without a compliant Phase I, the purchaser cannot
invoke the IPD and may face joint-and-several CERCLA liability. [VERIFY currency of AAI rule]

[JURISDICTION-SPECIFIC: UK — Environmental Protection Act 1990 Part IIA. Contaminated
land identified by local authority must be remediated by the "appropriate person"
(polluter first; then owner/occupier). Purchaser may inherit liability. Check local
authority contaminated land register and Contaminated Land Enquiry (form 3) from CON29.
[VERIFY]

[JURISDICTION-SPECIFIC: AU — National Environment Protection (Site Contamination) Measure
1999/2013 (NEPM). State EPAs (EPA NSW, EPA VIC, EPA WA etc.) maintain contaminated site
registers. Contaminated Land Management Act 1997 (NSW), Environment Protection Act 1970
(VIC) and equivalents impose remediation liability. "Polluter pays" but subsequent
owners/occupiers can be directed parties. [VERIFY state-level variants]

#### 3b. Phase II / Intrusive Investigation Triggers

Recommend a Phase II ESA [US] / intrusive investigation [UK/AU] when ANY of the
following are present:

- Phase I identifies a Recognized Environmental Condition (REC) (US)
- Phase I identifies controlled RECs (CRECs) with ongoing institutional controls
- Site has known or historic petroleum, solvent, or industrial use
- Visible contamination indicators observed during site reconnaissance
- Site is in a known contaminated land cluster (proximity to industrial estate, historical
  gas works, landfill)
- Lender or insurer requires Phase II as a condition of financing/underwriting
- Brownfield site or site with prior demolition

A Phase II that reveals contamination requires:

- Quantification of contamination extent and type
- Remediation cost estimate (include contingency: typically 20-30% for brownfield)
- Risk assessment against intended use (human health, ecological, controlled waters)
- Regulatory engagement strategy (voluntary cleanup vs. directed remediation)
- Institutional control requirements (deed restrictions, monitoring wells, vapor barriers)

---

### Workstream 4: Zoning and Planning

**Purpose**: Verify that current and intended use is lawful and that planning history
is free of unresolved issues.

#### 4a. Current Use and Zoning Compliance

| Item                                   | What to Check                                                                                                                           | Red Flags                                                                                    |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Permitted use**                      | Does the actual current use fall within the permitted use class / zoning designation?                                                   | Unauthorized change of use (UK); non-conforming use without variance (US); unlawful use (AU) |
| **Use class or zone**                  | Confirm the use class (UK: Use Classes Order); zoning designation (US: specific zoning map); zone (AU: state/local planning instrument) | Residential zoning for commercial intent; industrial zone for sensitive use                  |
| **Planning permission history**        | Extract all planning permissions; check they were implemented within time limits                                                        | Lapsed or unimplemented permissions; conditions not discharged                               |
| **Enforcement notices**                | Check for live enforcement notices (UK); compliance orders (US); orders (AU)                                                            | Live enforcement notice; breach of condition notice; stop notice                             |
| **Listed buildings / heritage**        | Listed building designation (UK); historic landmark (US); heritage listing (AU)                                                         | Unlawful alterations to listed/heritage building                                             |
| **Conservation area (UK)**             | Article 4 directions removing PD rights; demolition in CA consent                                                                       | Works without conservation area consent                                                      |
| **National Park / AONB / SSSI (UK)**   | Additional planning restrictions; SSSI management obligations                                                                           | SSSI notification; Habitat Regulations assessments                                           |
| **Section 106 / CIL obligations (UK)** | Unilateral undertakings; planning obligations binding on land and successors                                                            | Outstanding S106 financial obligations; CIL liability not factored into price                |
| **Development contributions (AU)**     | Section 7.11/7.12 contributions (NSW); development contributions plans                                                                  | Outstanding development contributions                                                        |

#### 4b. Intended Development / Change of Use

If the purchaser intends to develop or change use:

- Identify planning authority and applicable local development plan / local plan
- Assess likelihood of obtaining required consents (review planning officer guidance,
  recent appeal decisions, local plan policies)
- Identify material constraints: heritage, ecology, flood risk, highways, noise
- Estimate planning timeline and cost (pre-application advice recommended)
- Flag if Environmental Impact Assessment (EIA/EIS/EIS) is likely required

[JURISDICTION-SPECIFIC: US — Zoning variances, special use permits (SUPs), and conditional
use permits (CUPs) are granted locally and may not run with the land in all states.
Confirm whether entitlements transfer on sale. Confirm non-conforming use status (legal
non-conforming vs. illegal). [VERIFY state-specific rules]

[JURISDICTION-SPECIFIC: UK — Permitted Development rights (GPDO 2015) allow certain works
without full planning permission. Article 4 directions can remove PD rights. Prior Approval
is required for some PD development. Permitted Development applies to the existing use
class — a change of use to a new class removes previous PD rights. [VERIFY]

[JURISDICTION-SPECIFIC: AU — Development consent under the Environmental Planning and
Assessment Act 1979 (NSW) or equivalent state act. State Environmental Planning Policies
(SEPPs) can override local environmental plans. Complying Development Certificates (CDCs)
for straightforward works. [VERIFY state-level variants]

---

### Workstream 5: Permits and Certificates

**Purpose**: Confirm that all physical improvements were lawfully constructed and are
properly certified for occupation and use.

| Item                                                      | What to Check                                                                                                         | Red Flags                                                                                                   |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Building permits / development consents**               | All structures have building permits; permits were finaled / completed                                                | Unapproved structures; permits not finaled                                                                  |
| **Certificate of Occupancy (US) / Occupancy Permit (AU)** | Issued for all occupied buildings; matches current use and occupancy                                                  | No C/O; C/O inconsistent with current use; temporary C/O                                                    |
| **Completion certificate (UK — Building Regulations)**    | Building Regulations approval; completion certificate issued                                                          | Incomplete works; no completion certificate                                                                 |
| **Energy Performance Certificate (EPC — UK)**             | EPC rating; Minimum Energy Efficiency Standards (MEES) compliance                                                     | EPC F or G rating; non-compliant with MEES for letting [VERIFY MEES thresholds — note 2025 pending changes] |
| **Fire safety certificate / report**                      | Fire risk assessment (UK — RRFSO 2005); fire inspection compliance (US); essential fire safety measures (AU)          | Outstanding fire compliance notices; no fire risk assessment                                                |
| **Elevator / lift certificates**                          | Current statutory inspections (Lifting Operations and Lifting Equipment Regulations 1998 UK; state inspections US/AU) | Expired inspection certificate; outstanding defects                                                         |
| **Asbestos management plan (UK)**                         | Regulation 4, Control of Asbestos Regulations 2012; asbestos register up to date                                      | No asbestos management plan; ACM in poor condition                                                          |
| **Gas and electrical certificates (UK)**                  | Gas Safe certificate; EICR (Electrical Installation Condition Report)                                                 | Expired EICR; unsatisfactory condition                                                                      |
| **ADA / DDA compliance (US/UK)**                          | Accessibility compliance for public-use buildings                                                                     | Pending ADA enforcement; DDA audit showing non-compliance                                                   |
| **Pool compliance (AU / US)**                             | Pool safety certificate; barrier compliance                                                                           | Non-compliant pool barrier; no certificate                                                                  |
| **Cladding / fire safety (UK)**                           | Building Safety Act 2022 compliance for higher-risk buildings; EWS1 form for residential blocks                       | EWS1 B2 rating; building safety remediation orders                                                          |

[JURISDICTION-SPECIFIC: UK Building Safety Act 2022 — Higher-risk buildings (18m+ /
7 storeys+) have enhanced regulatory requirements including a Building Safety Case.
Remediation orders and building safety charges can be registered against the title. [VERIFY]

---

### Workstream 6: Lease Audit

**Purpose**: For income-producing properties, verify the quality, content, and security
of the existing tenancy income.

Conduct only if the property has existing occupational tenants or if the purchaser is
acquiring a tenanted investment.

#### 6a. Rent Roll Analysis

For each tenancy, extract:

| Field                                  | What to Record                                                                | Red Flags                                                       |
| -------------------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Tenant name**                        | Legal entity; credit quality                                                  | Weak covenant; related party                                    |
| **Lease term**                         | Start date; expiry date; break options; options to renew                      | Short remaining term; unexercised break imminent                |
| **Passing rent**                       | Current contractual rent                                                      | Over-rented vs. market (ERV); under-rented without review       |
| **Rent review**                        | Next rent review date; type (upward-only, open market, indexed, fixed uplift) | Upward-only reviews with rent above market; no review mechanism |
| **Permitted use**                      | Specific use permitted; Keep open obligation                                  | Use inconsistent with zoning; permitted use too narrow          |
| **Service charge / outgoings**         | Gross or net lease; service charge cap; apportionment                         | Service charge disputes; uncapped service charge cap            |
| **Repairing obligations**              | FRI (Full Repairing and Insuring); internal-repairing only                    | Dilapidations liability not provided for                        |
| **Assignment / subletting**            | Landlord's consent required; unreasonably withheld?                           | Restrictive assignment provisions; unauthorized underlets       |
| **Break clauses**                      | Tenant break options; conditions precedent                                    | Break conditions preventing exercise (rent arrears, repair)     |
| **Security of tenure (UK — LTA 1954)** | Is the lease contracted out of the 1954 Act?                                  | Inside the Act with significant lease renewal rights            |
| **Make-good / dilapidations**          | Tenant's obligations on expiry                                                | Dilapidations liability not quantified                          |
| **Rent arrears**                       | Outstanding rent; payment history                                             | Arrears; history of late payment; service charge disputes       |
| **Guarantor / rent deposit**           | Guarantor creditworthiness; rent deposit amount                               | No guarantor for weak covenant                                  |

[JURISDICTION-SPECIFIC: UK — Landlord and Tenant Act 1954 grants business tenants the right
to renew their lease on expiry unless the lease is "contracted out" by court order or
statutory declaration under s.38A. Inside-the-Act tenants may resist eviction and receive
market rent on renewal. Verify contracting-out procedure for all business leases. [VERIFY]

[JURISDICTION-SPECIFIC: US — No equivalent to LTA 1954. Holdover tenancy rules vary by
state. Estoppel certificates from tenants verify lease status and waive defenses against
purchaser. SNDA agreements (Subordination, Non-Disturbance, Attornment) address lender
priority. [VERIFY state-specific holdover rules]

[JURISDICTION-SPECIFIC: AU — Retail Leases Acts (state-based) impose mandatory terms for
retail tenants (RECA NSW, Retail Leases Act VIC, etc.); information disclosure
requirements; mediation of disputes. [VERIFY applicable state act]

#### 6b. Lease Structural Review

For each material lease, apply the following checklist:

- [ ] Lease executed by correct parties and properly stamped/registered
- [ ] If leasehold, head lease reviewed; sub-lease permitted; head lease not forfeited
- [ ] Alienation provisions — are they standard or unusually restrictive?
- [ ] Rent deposit deed reviewed and deposit held in designated account
- [ ] Surety/guarantor agreement reviewed and legally binding
- [ ] Keep-open clause (if any) — enforceability under governing law [VERIFY]

---

### Workstream 7: Property Tax

**Purpose**: Identify outstanding tax liabilities, deferred taxes, and transaction taxes
affecting the purchase.

#### 7a. Transaction Taxes

[JURISDICTION-SPECIFIC: UK — Stamp Duty Land Tax (SDLT — England and Northern Ireland),
Land and Buildings Transaction Tax (LBTT — Scotland), Land Transaction Tax (LTT — Wales).
Higher rates apply to: additional dwellings (3% surcharge); non-resident purchasers (2%
surcharge); acquisitions by companies above threshold; mixed-use properties. VAT: where
seller has made an "option to tax" election, SDLT and VAT may interact. Transfers of
going concerns (TOGC) may be VAT-exempt. [VERIFY current thresholds — SDLT holiday periods
may affect timing; check Finance Act provisions]]

[JURISDICTION-SPECIFIC: US — No federal transfer tax. State/county recording taxes, transfer
taxes, and grantor's taxes vary significantly by state (e.g., NY Transfer Tax + Mansion
Tax; CA Documentary Transfer Tax). NYC RPTT for NYC transactions. 1031 exchange:
like-kind exchange deferring capital gains requires strict timeline (45 days identification,
180 days closing). FIRPTA: foreign seller subject to 15% withholding. [VERIFY state rates]

[JURISDICTION-SPECIFIC: AU — Stamp duty/transfer duty (state-based; varies by state and
dutiable value). Land tax (state-based; annual; land value-based; principal residence
exemption varies). GST: if the property is a "new residential premises" or "commercial
residential premises" — GST applies (margin scheme may reduce GST liability). Going
concern exemption may apply. Foreign purchaser surcharge duty (all states) and surcharge
land tax. [VERIFY state rates and surcharges — rates changed frequently 2023-2026]

#### 7b. Outstanding Tax Liabilities

| Item                                                        | What to Check                                                   | Red Flags                                                                   |
| ----------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Property tax / rates / council rates**                    | Current assessment; payment status; any arrears                 | Arrears constituting a lien on property                                     |
| **Special assessment district / CIL / infrastructure levy** | Confirmed and quantified                                        | Large unbudgeted special assessments; CIL liability not factored into price |
| **Business rates (UK)**                                     | Rateable value; relief applied; empty property relief           | Rating revaluation appeal outstanding; empty property rates liability       |
| **Land tax clearance (AU)**                                 | Land tax certificate confirming no outstanding land tax         | Outstanding land tax is a first charge on land in most states               |
| **Municipal tax certificates (US)**                         | Confirm no outstanding municipal liens                          | Tax sale risk; unpaid municipal improvements                                |
| **VAT option to tax (UK)**                                  | Has seller opted to tax? What is buyer's VAT recovery position? | Buyer cannot recover VAT; unexpected cash flow cost                         |

---

### Workstream 8: Encumbrances

**Purpose**: Identify all encumbrances, burdens, and third-party rights that affect use,
value, or marketability.

| Encumbrance Type                                                                                 | What to Check                                                                                              | Red Flags                                                                                  |
| ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Easements**                                                                                    | Benefit and burden; express (registered), implied, prescriptive; easements of necessity                    | Easements over developable portions; undisclosed prescriptive rights                       |
| **Restrictive covenants**                                                                        | Registered covenants; breach history; indemnity chain; insurability                                        | Breach in existence; covenant prevents intended use; no indemnity insurance                |
| **Positive covenants (UK)**                                                                      | Positive covenants do not bind successors in title at common law; Halsall v Brizell exception              | Positive covenants with ongoing financial obligations; no valid mechanism to enforce chain |
| **Rights of way / public footpaths**                                                             | Public footpaths (UK — commons registration; DMMO); public access easements; statutory rights of way       | Right of way bisecting development site                                                    |
| **Profits à prendre (UK/AU)**                                                                    | Right to take something from the land (grazing rights, fishing rights, mineral rights)                     | Mineral rights severed; valuable resource subject to third-party profit                    |
| **Rentcharges (UK)**                                                                             | Estate rentcharges; registered rentcharges; Rentcharges Act 1977                                           | Rentcharge with forfeiture rights; not due to expire                                       |
| **Mortgages and charges**                                                                        | Registered mortgages; equitable charges; floating charges (company vendor)                                 | Floating charge crystallization risk; undisclosed second charges                           |
| **Adverse possession (UK: LRA 2002 Schedule 6; US: varying state periods; AU: limitation acts)** | Squatter applications; possessory title; fencing disputes                                                  | Adverse possessor's application pending; possessory title with weak evidence               |
| **Overriding interests (UK — LRA 2002 Sch 1 and 3)**                                             | Legal easements created before 13 Oct 2003; rights of persons in actual occupation; legal leases ≤ 7 years | Unregistered occupants with beneficial interests; short leases not revealed on register    |
| **Options and pre-emptions**                                                                     | Options to purchase; rights of pre-emption; right of first refusal                                         | Unregistered option; right of pre-emption preventing free sale                             |
| **Land assembly constraints**                                                                    | Ransom strips; access monopolies                                                                           | Ransom strip owner with unreasonable demands                                               |
| **Insolvency / administrator's disposals**                                                       | Voidable transactions; transaction at undervalue; gratuitous disposals                                     | Sale by administrator within risk period; transaction at undervalue risk                   |

---

## Finding Classification System

Every due diligence finding is classified across two dimensions: **status** and **materiality**.

### Status Classification

| Status      | Meaning                                                                                          | Action                                                           |
| ----------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| **✅ PASS** | No material issues identified in this workstream                                                 | Note for record; no action required                              |
| **⚠ FLAG**  | Issues identified requiring attention, further investigation, or negotiation of price/conditions | Address before completion; or accept and document the risk       |
| **🚫 FAIL** | Material defects, blocking issues, or unacceptable risks that must be resolved before proceeding | Stop / escalate / renegotiate; do not proceed without resolution |

### Materiality Tiers

| Tier                              | Description                                                                                 | Examples                                                                                                                                                                                                        |
| --------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tier 1 — Deal-Breaker**         | Fundamental defect that prevents or should prevent completion without resolution            | Vendor does not hold good title; contamination requiring $1M+ remediation; unlawful use that cannot be regularized; undischarged mortgage with no redemption undertaking                                        |
| **Tier 2 — Material Risk**        | Significant issue that must be resolved, priced-in, or accepted on an informed basis        | Phase II reveals contamination requiring <$500K remediation; planning enforcement notice (not yet served but threatened); lease with unexpired break option; minor title defect insurable at reasonable premium |
| **Tier 3 — Minor/Administrative** | Lower-risk items that can be addressed by undertaking, insurance, or post-completion action | Missing completion certificate for minor outbuilding; small rent arrears with payment plan; EPC improvement works possible within MEES timeline                                                                 |

### Actionable Output per Finding

For each ⚠ FLAG and 🚫 FAIL finding, provide:

```
**Finding**: [workstream] — [specific issue description]
**Classification**: ⚠ FLAG / 🚫 FAIL
**Tier**: 1 / 2 / 3
**Evidence**: [source document, register entry, or observation]
**Legal basis**: [statute, principle, or established practice — mark [VERIFY] if unverified]
**Business impact**: [practical effect on value, use, or transaction]
**Remediation options**:
  A. [Primary remedy — timeline and estimated cost]
  B. [Alternative remedy — if A is not available]
  C. [Risk acceptance — conditions under which this can be accepted with eyes open]
**Pre-conditions for proceeding**: [what must happen before completion can proceed]
```

---

## Prioritization Framework

### Tier 1 — Deal-Breakers (Must Resolve Before Proceeding)

Issues in this tier prevent completion unless fully resolved:

- Vendor has no title or materially defective title (e.g., Possessory title with adverse
  possessor pending; unregistered title with broken chain)
- Environmental contamination with undefined or excessive remediation liability
- Property in breach of applicable law with no clear remediation path
- Outstanding mortgages or charges not to be discharged at completion
- Material planning breach with live enforcement action
- No certificate of occupancy for occupied building (US); fundamental building regulations
  failure (UK); unlawful occupation (AU)

**Action**: Do not proceed without resolution. Raise with buyer/lender leadership.

### Tier 2 — Material Risks (Resolve, Price-In, or Accept with Documented Risk)

Issues in this tier are material but may be capable of resolution, insurance, or
negotiated price adjustment:

- Phase II contamination with quantified but manageable remediation cost
- Title defect insurable under title indemnity policy at reasonable premium
- Lease with upcoming break option or near-term expiry
- Planning condition not yet formally discharged
- Missing completion certificate for main structure (insurable)
- Positive covenant with ongoing financial obligation
- Adverse soil conditions affecting construction cost estimates

**Action**: Present options to client (resolve / insure / price reduction). Obtain written
client instructions before proceeding.

### Tier 3 — Minor/Administrative (Address by Undertaking or Post-Completion)

Issues in this tier are manageable and should not delay completion:

- Minor missing documentation capable of replacement (e.g., lost completion certificate
  for garden outbuilding)
- Low-level rent arrears with payment plan in place
- Minor planning condition with easy discharge mechanism
- EPC improvement works within MEES compliance window
- Low radon assessment score within action level

**Action**: Document, take seller's undertakings where appropriate, and complete.

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise any failures before delivery.

| Gate           | Rule                                                                                                                             | Fail Action                                                |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, standard, or established principle                                       | Add citation or mark "[UNVERIFIED — solicitor to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction (e.g., LRA 2002 s.27; ASTM E1527-21; EPA 1990 s.78A) | Fix format                                                 |
| **Currency**   | Every cited provision checked for amendments, repeal, or replacement                                                             | Flag "[CHECK CURRENCY — may have been amended]"            |
| **Domain**     | Analysis stays within the applicable jurisdiction's legal framework; no cross-border contamination of legal concepts             | Remove or flag jurisdictional bleed                        |
| **Confidence** | Uncertainty explicitly stated; confidence qualifier assigned to every material finding                                           | Add confidence qualifier                                   |

### Self-Interrogation for FAIL Items

For any finding classified as 🚫 FAIL, apply this 3-pass review before delivery:

**Pass 1 — Legal Chain Integrity**:

- Does the FAIL classification follow logically from the cited statute/principle/condition?
- Would a qualified conveyancer or property lawyer in this jurisdiction reach the same conclusion?
- What counter-argument will the vendor's solicitor make?

**Pass 2 — Completeness**:

- Have all relevant statutes, regulations, and professional standards been considered?
- Has the interaction between this finding and other workstreams been checked?
- Are there remediation options not yet identified?

**Pass 3 — Challenge**:

- What is the strongest argument that this issue is not a FAIL — only a FLAG or PASS?
- Under what conditions (indemnity, price reduction, contractual undertaking) could a
  reasonable purchaser proceed?
- Is the FAIL classification proportionate, or should this be a FLAG with conditions?

Revise any finding where a pass reveals a weakness. Mark the audit trail:
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

Assign a confidence level to each material finding:

| Level        | Range     | Meaning                                                 | Action                                                  |
| ------------ | --------- | ------------------------------------------------------- | ------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Clear statutory provision or unambiguous register entry | State with confidence                                   |
| **High**     | 0.80-0.94 | Strong authority; minor interpretation questions        | State with brief caveat                                 |
| **Probable** | 0.60-0.79 | Good basis; reasonable minds could differ               | State with reasoning and contra-indicators              |
| **Possible** | 0.40-0.59 | Genuinely uncertain; competing readings                 | Flag for professional review with both sides            |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative                                 | Do not assert; mark "[UNCERTAIN — solicitor to advise]" |

---

## Glass Box Audit Trail

Append this YAML block to every due diligence report:

```yaml
glass_box:
  skill_name: "legalcode-real-estate-due-diligence"
  property: "[Property address / identifier]"
  transaction_type: "[Purchase / Financing / Lease / Development / etc.]"
  property_type: "[Commercial / Residential / Industrial / Development site / etc.]"
  jurisdiction: "[England & Wales / US — State / Australia — State / etc.]"
  role: "[Purchaser / Lender / Tenant / Developer / etc.]"
  workstreams_completed:
    - "1. Title Examination: [PASS / FLAG / FAIL]"
    - "2. Survey and Boundaries: [PASS / FLAG / FAIL]"
    - "3. Environmental Due Diligence: [PASS / FLAG / FAIL]"
    - "4. Zoning and Planning: [PASS / FLAG / FAIL]"
    - "5. Permits and Certificates: [PASS / FLAG / FAIL]"
    - "6. Lease Audit: [PASS / FLAG / FAIL / N/A]"
    - "7. Property Tax: [PASS / FLAG / FAIL]"
    - "8. Encumbrances: [PASS / FLAG / FAIL]"
  total_findings:
    pass: "[number]"
    flag: "[number]"
    fail: "[number]"
  tier_1_findings: "[number — list summaries]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no FAIL items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Any scope limitations, documents not reviewed, or assumptions]"
  review_date: "[date]"
  reviewer: "AI-assisted — requires qualified legal / conveyancing professional review"
```

---

## Anti-Patterns

Real estate due diligence-specific catalogue of what NOT to do:

1. **Accepting a vendor due diligence pack uncritically** — A vendor-prepared pack is
   naturally curated to present the property favorably. Verify key items independently.
   A vendor's Phase I ESA may be outdated or may not address a recent use. Order your
   own searches where material.

2. **Treating title insurance as a substitute for due diligence** — Title insurance
   compensates after loss; it does not prevent you from acquiring a property that cannot
   be used for the intended purpose. Insurance should supplement, not replace, proper title
   investigation.

3. **Skipping the environmental workstream for "clean" properties** — A commercial office
   in a city center may sit on a former industrial site or gasworks. Always check historical
   uses. Environmental liability is strict, retrospective, and can exceed property value.

4. **Failing to check overriding interests (UK)** — Overriding interests under LRA 2002
   Sch 3 bind a purchaser whether or not they appear on the register. A person in actual
   occupation who discloses their interest on reasonable inquiry is protected. Physical
   inspection of the property and occupier enquiries are essential.

5. **Ignoring the Landlord and Tenant Act 1954 (UK)** — Acquiring a tenanted commercial
   investment without verifying whether each lease is contracted out of the LTA 1954 is
   a critical error. An inside-the-Act tenant has a statutory right to renew at market
   rent and cannot be evicted without a statutory ground.

6. **Assuming zoning / planning permission transfers automatically** — In the US, some
   entitlements (variances, CUPs) are personal and do not run with the land. Confirm
   transferability. In the UK, planning permission runs with the land — but conditions
   and S106 obligations also run with the land.

7. **Not investigating CERCLA liability exposure (US)** — Purchasing contaminated property
   without completing All Appropriate Inquiries (AAI) under ASTM E1527-21 eliminates the
   innocent purchaser defense. The buyer may face joint-and-several liability under CERCLA
   for the entire site cleanup, even if they caused none of the contamination.

8. **Ignoring positive covenants in a chain of title (UK)** — Positive covenants (obligations
   to spend money) do not bind successors in title at common law in England and Wales
   (Rhone v Stephens [1994]). However, chains of indemnity and the benefit/burden doctrine
   can create enforcement routes. Failure to understand this creates unexpected liability.

9. **Confusing floor area metrics (UK)** — Gross Internal Area (GIA), Net Internal Area
   (NIA), and Gross External Area (GEA) are RICS-defined metrics with specific meanings.
   A lease based on incorrect area measurement creates rent review and service charge
   issues. Verify measured areas against RICS standards.

10. **Not requesting estoppel certificates from tenants (US)** — Estoppel certificates
    are the purchaser's primary protection against lease-related surprises (undisclosed
    modifications, offset rights, landlord defaults). Failing to require these from all
    material tenants before completion is a significant gap.

11. **Overlooking the Land Tax clearance certificate (AU)** — In most Australian states,
    land tax is a first charge on land that binds the purchaser regardless of whether the
    vendor disclosed the liability. Always obtain a land tax clearance certificate and
    verify its currency at settlement.

12. **Treating the ALTA survey Table A items as optional** — Certain Table A items in
    US commercial transactions are effectively mandatory for proper due diligence: Item 6
    (zoning), Item 7 (utilities), Item 11 (location of overhead utilities), Item 13
    (parking). Omitting them to save cost can create material blind spots.

13. **Conflating use class / zoning designation with legal use** — The fact that a use
    class or zone permits a use does not mean the specific property has been lawfully
    operating in that use. Confirm the property's existing lawful use, not just the
    theoretical permitted use.

14. **Skipping the lease audit for investment acquisitions** — The lease income stream
    is the primary value driver for an investment property. A leased investment acquired
    without reviewing individual leases may have key tenants with imminent break options,
    over-rented space with rent review risk, or make-good obligations creating deferred
    capital expenditure.

15. **Ignoring flood risk at any stage** — Flood risk affects insurability, financing,
    value, and planning. Properties in FEMA Zone A/AE (US), Environment Agency Zone 2/3
    (UK), or high flood hazard areas (AU) require specialist flood assessment, insurance
    review, and may not be financeable on standard terms. The trend of flood risk is
    increasing under climate change; historical flood data understates future risk.

16. **Completing without a redemption undertaking for mortgages** — In the UK, purchasing
    a mortgaged property without a solicitor-to-solicitor undertaking to redeem the
    mortgage on completion creates the risk that the mortgage is not discharged and the
    purchaser takes subject to it.

17. **Assuming stamp duty / transfer duty calculations are straightforward** — Multiple
    surcharges, reliefs, and exemptions apply in all three jurisdictions (first-time buyer
    relief, SDLT higher rates for additional dwellings, mixed-use analysis, AU foreign
    purchaser surcharges). Incorrect SDLT/duty calculations create irrecoverable penalties.
    Always verify with a tax specialist.

---

## Localization Notes

### United Kingdom (England & Wales)

**Property registration**: HMLR registration is now essentially universal for all dealings
with title. Unregistered title is increasingly rare but requires first registration on
sale. Priority of interests follows registration.

**Legal framework**: Conveyancing governed by Law of Property Act 1925; Land Registration
Act 2002; Land Charges Act 1972 (unregistered); Law of Property (Miscellaneous Provisions)
Act 1989 (formalities); Landlord and Tenant Act 1954 (business tenancies); Law of Property
Act 1925 ss. 52-53 (formal requirements).

**Pre-contract searches**: Standard residential pack: HMLR official copies, LLC1, CON29,
CON29DW, environmental search, chancel search. Commercial adds: CON29O, mining search,
CPSE enquiries, bespoke searches per property location.

**SDLT**: Higher rates for additional dwellings (3%); non-resident surcharge (2%);
commercial/mixed-use rates differ. Finance Act 2003 Schedule 4ZA (higher residential
rates). [VERIFY: thresholds change with each Finance Act]

**Scotland and Northern Ireland**: Separate systems. Engage Scottish solicitors and
Registers of Scotland for Scottish property. NI Land Registry for Northern Ireland.

### United States

**State variability**: Property law is primarily state law. Recording acts vary (race,
notice, race-notice). Title standards differ. Due diligence requirements for commercial
transactions differ by state and asset class.

**All Appropriate Inquiries**: 40 C.F.R. Part 312 (incorporating ASTM E1527-21) is the
federal standard for AAI. Completing a compliant Phase I before purchase is critical to
preserving the innocent purchaser defense under CERCLA.

**Title insurance**: Standard for both residential and commercial transactions. ALTA
Owner's Policy and ALTA Lender's Policy are the market standards. Endorsements (ALTA 3.1
for zoning, ALTA 9 for restrictions and encumbrances, ALTA 28 for easements) add
important protections.

**State-specific requirements**: California (AB 1498, disclosure requirements), New York
(RPSL, municipal search requirements), Texas (survey requirements, title commitment
standards) all have significant local practice requirements. [VERIFY]

### Australia

**Torrens system**: Title by registration; indefeasibility of registered title (with
exceptions: fraud; in personam claims; certain overriding statutes). No need to trace
chain of title — register is authoritative.

**State-based jurisdiction**: Conveyancing and property law is predominantly state/territory
law. Each state has its own Conveyancing Act, Real Property Act, Environmental Planning
Act, Duties Act (stamp duty), and Land Tax Act. Engage state-specific conveyancing advice.

**Electronic conveyancing**: PEXA (Property Exchange Australia) is the primary electronic
settlement platform. Ensure PEXA workspace is established and verified before settlement.

**Foreign investment**: FIRB (Foreign Investment Review Board) approval required for
foreign purchasers of Australian residential real estate and certain commercial real
estate above thresholds. Foreign purchaser surcharge duties apply in all states. [VERIFY
current FIRB thresholds — revised periodically]

---

## Writing Standards

Apply plain-language discipline to all due diligence output:

**For finding descriptions and risk summaries** (shared with client and advisors):

- Active voice: "The vendor does not hold registered title" not "Registered title is not held by the vendor"
- Specific: cite the specific entry, search result, or document reference
- Quantify where possible: "£45,000 in outstanding service charges" not "significant outstanding charges"
- Name the risk holder: "The purchaser will take the property subject to this encumbrance
  unless it is discharged before completion"
- Plain English: no unexplained Latin maxims, no excessive cross-references

**For legal citations**:

- Format consistently per jurisdiction: LRA 2002 s.27; ASTM E1527-21 § 8.1; EPA 1990
  Part IIA s.78A
- Mark unverified citations: [VERIFY]
- Mark currency-uncertain citations: [CHECK CURRENCY]

**Quality gates before delivery**:

1. Can a non-lawyer business decision-maker understand the Executive Summary?
2. Is every finding linked to a specific evidence source?
3. Is every Tier 1 FAIL item presented with clear remediation options?
4. Is every legal claim backed by a citation or flagged [VERIFY]?
5. Could any sentence be shorter without losing meaning? If yes, shorten.

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- In Step 3, search for jurisdiction-relevant statutes, regulations, and professional
  standards applicable to the property's jurisdiction
- For contaminated land and environmental findings, search for current regulatory
  guidance and enforcement precedent
- For planning/zoning findings, verify current policy context and appeal decision trends
- For SDLT/stamp duty findings, verify current thresholds and rates
- Save verified authority to `/tmp/legalcode-re-dd-authority.md`
- Mark all legalcode-mcp citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory and case law references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Focus the analysis on structural risk assessment; flag that legal thresholds (tax rates,
  statutory timeframes, regulatory limits) require independent verification by local counsel
- Do not cite specific case law — refer to principles instead (e.g., "common law
  principle of indefeasibility" rather than a specific case)

---

## Output Format Template

Structure the final due diligence report as:

```markdown
## Real Estate Due Diligence Report

**Property**: [address and brief description]
**Transaction Type**: [Purchase / Financing / Lease / etc.]
**Property Type**: [Commercial / Residential / Industrial / etc.]
**Jurisdiction**: [England & Wales / US — State / Australia — State]
**Role**: [Purchaser / Lender / Tenant / Developer]
**Review Date**: [date]
**Scope**: [Full / Priority / Single workstream]

---

## Executive Summary

**Overall risk status**: [PASS / FLAG / FAIL — one-line summary]

**Tier 1 (Deal-Breaker) findings**: [N items — list]
**Tier 2 (Material) findings**: [N items — list]
**Tier 3 (Minor) findings**: [N items — list]

**Recommended action**: [Proceed / Proceed with conditions / Pause pending investigation / Do not proceed]

---

## Workstream Status Overview

| Workstream                  | Status            | Tier | Key Finding        |
| --------------------------- | ----------------- | ---- | ------------------ |
| 1. Title Examination        | ✅ / ⚠ / 🚫       | —    | [one-line summary] |
| 2. Survey and Boundaries    | ✅ / ⚠ / 🚫       | —    | [one-line summary] |
| 3. Environmental            | ✅ / ⚠ / 🚫       | —    | [one-line summary] |
| 4. Zoning and Planning      | ✅ / ⚠ / 🚫       | —    | [one-line summary] |
| 5. Permits and Certificates | ✅ / ⚠ / 🚫       | —    | [one-line summary] |
| 6. Lease Audit              | ✅ / ⚠ / 🚫 / N/A | —    | [one-line summary] |
| 7. Property Tax             | ✅ / ⚠ / 🚫       | —    | [one-line summary] |
| 8. Encumbrances             | ✅ / ⚠ / 🚫       | —    | [one-line summary] |

---

## Detailed Findings

### Workstream 1: Title Examination — [✅ PASS / ⚠ FLAG / 🚫 FAIL]

**Finding 1.1**: [description]
**Classification**: [PASS / FLAG / FAIL] | **Tier**: [1 / 2 / 3]
**Evidence**: [source document or search result]
**Legal basis**: [statute or principle — [VERIFY] if unverified]
**Business impact**: [practical effect]
**Remediation options**:
A. [Primary]
B. [Alternative]
C. [Accept with conditions — if possible]

[Repeat for each finding in each workstream]

---

## Conditions for Proceeding

[List all pre-completion conditions — items that must be resolved before exchange/completion/closing]

1. [Condition 1] — Responsibility: [Vendor / Purchaser / Both] — Deadline: [Date]
2. [Condition 2] — Responsibility: [...] — Deadline: [...]

---

## Post-Completion Undertakings

[Items that can be resolved after completion but require active management]

---

## Documents Outstanding / Still Required

[List any documents requested but not yet received]

---

## Next Steps

[Specific actions, responsibility, and deadline]

---

## Glass Box Audit Trail

[YAML block as defined in Glass Box section]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on:

- UK conveyancing practice standards: Law Society Conveyancing Protocol; RICS practice
  notes (Environmental Risks and Global Real Estate 3rd edition); CON29 / LLC1 search
  practice; LRA 2002 practice directions
- US real estate due diligence standards: ASTM E1527-21 Phase I ESA standard; ALTA/NSPS
  2021 Minimum Standard Detail Requirements for Land Title Surveys; CERCLA 42 U.S.C. §
  9601 et seq. AAI rule 40 C.F.R. Part 312; state-specific conveyancing practice
- Australian conveyancing standards: PEXA electronic conveyancing practice; NEPM 1999/2013
  site contamination assessment guidance; state-based conveyancing acts; FIRB guidelines
- General real estate due diligence best practices from commercial law firm knowledge
  bases and institutional investor checklists
- Repository reference standard: `legalcode-contract-review` skill quality framework
  (Legalcode gold standard)

All legal references require independent verification against authoritative current sources.
This skill does not constitute legal advice.
