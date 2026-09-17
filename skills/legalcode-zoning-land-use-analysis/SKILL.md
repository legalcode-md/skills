---
name: legalcode-zoning-land-use-analysis
description: Analyze zoning and land use compliance for any property or development project. Use when
  evaluating development feasibility, checking zoning compliance before purchase, assessing variance necessity,
  analyzing entitlement risk, advising on project approvals, or reviewing planning conditions and obligations.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Analyze zoning and land use compliance for any property or development project. Covers permitted use classification (by-right vs. discretionary), conditional/special use permits (CUPs/SUPs), area and use variances, nonconforming use rights (legal nonconforming status, abandonment, expansion), setback and bulk standards, subdivision regulation and platting, development agreements and vesting rights, environmental review (CEQA/NEPA), historic preservation (Section 106 NHPA, UK Planning (Listed Buildings and Conservation Areas) Act 1990), and exaction proportionality (Nollan/Dolan/Koontz/Sheetz). US and UK coverage: US Euclidean zoning, form-based codes, state enabling legislation, California Development Agreements (Gov. Code §§65864–65869.5), CEQA (14 CCR §§15000–15387), NEPA (40 CFR Parts 1500–1508); UK Town and Country Planning Act 1990, Use Classes Order 2020 (SI 2020/757 as amended), GPDO 2015, Planning and Infrastructure Act 2025, NPPF 2024, Section 106 obligations, and Community Infrastructure Levy. Use when evaluating development feasibility, checking zoning compliance before purchase, assessing variance necessity, analyzing entitlement risk, advising on project approvals, or reviewing planning conditions and obligations. Jurisdiction-aware with [JURISDICTION-SPECIFIC] markers for US states, UK nations, and other common law systems.


# Legalcode Zoning and Land Use Analysis

> **Disclaimer**: This skill provides a framework for AI-assisted zoning and land use
> analysis. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional licensed in the relevant jurisdiction before any reliance
> or action. Zoning codes and planning policies vary significantly by municipality and
> change frequently — verify current applicability before relying on any provision
> described here. Statutory and case law references cited from memory carry hallucination
> risk — verify against authoritative sources before relying on them. This skill does not
> substitute for formal applications, environmental review, permit submissions, or legal
> filings.

---

## Purpose and Scope

This skill analyzes the zoning and land use status of a property or development project.
It identifies compliance issues, entitlement risks, and regulatory requirements, and
produces a confidence-scored, auditable analysis with actionable recommendations.

**Covers:**

- Use classification analysis (zoning district, permitted vs. discretionary uses)
- Conditional/Special Use Permit (CUP/SUP) requirements and standard findings
- Variance analysis (area variances and use variances)
- Nonconforming use rights — establishment, abandonment, expansion, amortization
- Dimensional and bulk standards (setbacks, height, lot coverage, FAR, parking)
- Subdivision regulation and platting requirements
- Development agreements and vesting rights (including California Gov. Code §§65864–65869.5)
- Environmental review — CEQA (California) and NEPA (federal nexus projects)
- Historic preservation — Section 106 NHPA process and local landmark review
- UK planning system — TCPA 1990, Use Classes Order 2020, GPDO 2015, Planning and Infrastructure Act 2025, NPPF 2024, Section 106 obligations, CIL
- Exaction constitutionality (Nollan/Dolan/Koontz/Sheetz nexus and proportionality)
- Regulatory takings risk assessment (Lucas, Penn Central, Murr frameworks)

**Does not:**

- Draft planning applications, environmental documents, or permit submissions
- Provide site-specific engineering or survey analysis
- Substitute for formal zoning confirmation letters from the municipality
- Apply to residential leases, agricultural water rights, or mineral rights (covered by specialist skills)
- Provide legal advice or replace qualified land use counsel

**Related skills:**

- `legalcode-commercial-lease-review` — for lease-level zoning and permitted-use covenants
- `legalcode-construction-contract-review` — for construction contract compliance once entitlements are secured

---

## Jurisdiction and Governing Law

This skill is jurisdiction-aware, covering the US and UK as primary systems, with
[JURISDICTION-SPECIFIC] markers throughout to indicate where local law diverges
materially.

**United States:**

- Federal constitutional floor: Euclid v. Ambler Realty, 272 U.S. 365 (1926) (police
  power / rational basis); Penn Central Transportation Co. v. City of New York, 438 U.S.
  104 (1978) (regulatory takings); Nollan, Dolan, Koontz, Sheetz (exactions); Lucas v.
  South Carolina Coastal Council, 505 U.S. 1003 (1992) (per se taking)
- State enabling legislation: derived from the Standard Zoning Enabling Act (SZEA, 1922) and Standard City Planning Enabling Act (SCPEA, 1928). Most states have
  significantly updated enabling statutes [JURISDICTION-SPECIFIC]
- Environmental: CEQA (Cal. Pub. Resources Code §§21000–21189.3; 14 CCR §§15000–15387);
  NEPA (42 U.S.C. §§4321–4370m-12; 40 CFR Parts 1500–1508, Phase 2 Rule May 2024)
  [VERIFY current NEPA regulatory status — 2025 interim rule changes pending]
- Historic preservation: Section 106 NHPA (54 U.S.C. §306108; 36 CFR Part 800)
- Development agreements (California): Gov. Code §§65864–65869.5; vesting tentative
  maps: Gov. Code §§66498.1 et seq. [JURISDICTION-SPECIFIC — analogous statutes vary
  by state: Florida §163.3220 et seq.; Washington RCW 36.70B.170–210; Texas Local
  Gov. Code §212.172; Arizona A.R.S. §9-500.05]

**United Kingdom (England focus; devolution noted):**

- Town and Country Planning Act 1990 (TCPA 1990)
- Planning and Compulsory Purchase Act 2004 (PCPA 2004 s.38(6) — development plan
  presumption)
- Town and Country Planning (Use Classes) Order 2020 (SI 2020/757 as amended)
- Town and Country Planning (General Permitted Development) Order 2015
  (SI 2015/596 as amended, including Class MA amendment SI 2024/141)
- Planning and Infrastructure Act 2025 (Royal Assent 18 December 2025)
- National Planning Policy Framework (NPPF) December 2024 (grey belt; housing targets)
- Planning (Listed Buildings and Conservation Areas) Act 1990 (LB&CA Act)
- Planning Act 2008 and CIL Regulations 2010 (Community Infrastructure Levy)

[JURISDICTION-SPECIFIC] Scotland, Wales, and Northern Ireland each have devolved
planning systems and should be analyzed under their respective legislation (e.g.,
Town and Country Planning (Scotland) Act 1997; Planning (Wales) Act 2015;
Planning Act (Northern Ireland) 2011).

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming intent, the workflow pauses and asks when:

- The answer would change the direction of the analysis
- The applicable jurisdiction's law differs materially from the general framework
- The development program is unclear and determines which entitlement path applies
- Legal nonconforming status depends on historical facts only the user can provide
- Environmental review scope depends on project type and federal nexus

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

Accept the zoning analysis request in any of these formats:

- **Property description**: address, parcel number (APN/folio), or legal description
- **Development program**: proposed use, square footage, height, density, and any
  ancillary facilities
- **Documents**: zoning confirmation letter, planning application, EIR/MND, site plan,
  variance decision, development agreement, planning condition schedule
- **Specific question**: targeted query about a single element (e.g., "Is this a
  non-conforming use?", "What variance standard applies?")

If the property's address and proposed use are not supplied, prompt the user to provide
them before proceeding.

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning the analysis, ask the user the following. Skip any
questions already answered by the input:

1. **Jurisdiction**: What is the governing jurisdiction?
   - Options: US — specify state and municipality; UK — England / Scotland / Wales /
     Northern Ireland; Other (specify)
   - _Why this matters_: Zoning codes are locally adopted; state enabling law and CEQA/NEPA
     vs. UK EIA rules differ fundamentally.

2. **Stakeholder role**: Who are you acting for?
   - Options: Property owner/investor, Developer/applicant, Purchaser conducting due
     diligence, Lender, Adjacent/neighboring property owner, Municipal staff, Other
   - _Why this matters_: The analysis flips — a property owner seeking a variance has
     different risk exposure than a purchaser in due diligence or a neighbor objecting.

3. **Development program**: What is the proposed use and scale?
   - Options: Residential (units: **_), Commercial (type: _**; SF: **_), Mixed-use,
     Industrial/logistics, Institutional, Subdivision, Change of use (from _** to \_\_\_),
     Other
   - _Why this matters_: Determines which use class, entitlement pathway, and
     environmental thresholds apply.

4. **Current zoning status**: What is the current zoning classification and use?
   - If known: state the zoning district and current use.
   - If unknown: note that the first step is to confirm from the official zoning map
     and municipal code.
   - _Why this matters_: Analysis cannot proceed without knowing the baseline zoning
     district and current use.

5. **Specific concerns**: Are there any known issues or focus areas?
   - Options: Nonconforming use status, Variance needed, Environmental triggers
     (CEQA/NEPA), Historic designation, Development agreement / vesting rights,
     Exaction challenge, No specific focus — full analysis
   - _Why this matters_: Allows the analysis to lead with the most critical issues.

If the user provides partial context, state assumptions explicitly (e.g., "I am assuming
the property is in an unincorporated area of California subject to county zoning — confirm
if incorrect and I will adjust.").

### Step 3: Load the Regulatory Framework

Identify and load the applicable regulatory framework before analyzing the property.

**For US properties:**

1. Identify the local zoning authority (city, county, or both for unincorporated areas)
2. Confirm the current zoning district from the official zoning map (GIS portal if
   accessible via legalcode-mcp)
3. Read the applicable zoning code provisions for: permitted uses table; CUP/SUP
   standards; variance standards; dimensional/bulk standards; nonconforming use
   provisions; subdivision regulations
4. Identify the applicable general plan/comprehensive plan land use designation
5. Determine whether CEQA review is required or triggered (lead agency, project type)
6. Identify any federal nexus triggering NEPA review
7. Identify any National Register or local landmark designations affecting the property

[JURISDICTION-SPECIFIC] California: Also load the applicable Specific Plan if any.
Check for Housing Accountability Act (HAC) and builder's remedy applicability where
local housing element is out of compliance.

**For UK properties (England):**

1. Identify the local planning authority (LPA — district, borough, or unitary authority)
2. Confirm the current use class under the Use Classes Order 2020 (SI 2020/757)
3. Check for permitted development rights under the GPDO 2015 (and any Article 4
   Direction removing PD rights in the area)
4. Identify the applicable Local Plan policies and saved policies
5. Check for Green Belt designation, Conservation Area, and Listed Building status
6. Identify any existing Section 106 obligations or CIL charging schedule
7. Determine whether Environmental Impact Assessment (EIA) is required (Town and
   Country Planning (EIA) Regulations 2017)
8. Check whether the property falls within a Spatial Development Strategy area
   (post-Planning and Infrastructure Act 2025)

**Use legalcode-mcp** to search for:

- Current zoning code provisions for the identified district
- Recent amendments to local ordinances or development standards
- Relevant case law in the applicable jurisdiction on variance standards, nonconforming
  use doctrine, or exaction constitutionality
- UK: current NPPF 2024 policies on grey belt, housing, and infrastructure

Save the most relevant results to a local reference file:

```
/tmp/legalcode-zoning-research-[property-identifier].md
```

**⟁ CLARIFY** — If the zoning district or current use cannot be confirmed from the
documents provided, ask the user:

- "I cannot confirm the current zoning district from the documents provided. Can you
  confirm the official zoning designation from the municipal zoning map or a zoning
  confirmation letter? Without this, I can only analyze the framework generally."
- "The current use is unclear from the materials. Is the existing use the one you wish to
  continue, or are you proposing a change of use to the development program described?"

### Step 4: Use Classification Analysis

Analyze whether the proposed use is permitted in the applicable zoning district.

For each proposed use in the development program:

| Analysis Step              | US (Euclidean)                                              | UK (UCO 2020)                                                                       |
| -------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Identify use class         | Check permitted uses table for the district                 | Confirm current UCO 2020 class (E, F.1, F.2, C1–C4, sui generis)                    |
| By-right or discretionary? | Listed as "P" (permitted), "C" (conditional), or not listed | Within UCO class = free change; between classes = prior approval or full permission |
| Specific standards         | Applicable development standards in zoning code             | Applicable GPDO Part 3 prior approval criteria                                      |
| General plan consistency   | Check general plan land use designation                     | Check Local Plan policies and NPPF presumption                                      |

**Key distinctions:**

- **US — By-right (ministerial) approval**: A use listed as "permitted" in the zoning
  district requires only a building permit confirming dimensional compliance. No public
  hearing. CEQA ministerial exemption may apply (Pub. Resources Code §21080(b)(1)).
  Recent California housing legislation (SB 9, SB 10, AB 2011, SB 423 as extended)
  dramatically expands by-right approvals for qualifying housing projects — check
  current statutory eligibility [JURISDICTION-SPECIFIC — California].

- **US — Conditional/discretionary**: A use listed as conditionally permitted requires
  a CUP/SUP. The decision is quasi-judicial, triggering procedural due process
  requirements. CEQA review is generally required.

- **UK — Changes within Class E**: Moving from retail (formerly A1) to office (formerly
  B1), restaurant, medical, or fitness use within Class E is freely permitted — no
  planning permission required. This creates significant flexibility for commercial
  tenants.

- **UK — Class MA (most significant 2024 amendment)**: Change of use from Class E
  (commercial) to Class C3 (dwellinghouses) is permitted development under GPDO Part 3,
  Class MA (SI 2024/141, in force 5 March 2024): the 3-month vacancy requirement and
  floorspace upper limit are removed. Prior approval from the LPA is still required for
  specified matters (transport; contamination; flooding; noise from commercial premises;
  adequate natural light; impact on surrounding area; national security). LPA has 8 weeks
  to determine; silence defaults to approval.

- **UK — Sui generis uses**: Uses outside any defined class (theatres, fuel stations,
  nightclubs, casinos, HMOs of more than 6 persons, large shops above threshold [VERIFY
  current sqm threshold]) require planning permission for any change to or from them.

**⟁ CLARIFY** — If the use classification is ambiguous:

- "The proposed use spans multiple categories (e.g., restaurant with takeaway; live-work
  unit). I need to classify the primary use. Which is the predominant activity by floor
  area and revenue?"
- "UK: The existing use is unclear. If it pre-dates the Use Classes Order 2020, I need
  to determine what class it falls under the new structure. Do you have a planning
  permission or other evidence of the lawful use?"

### Step 5: Entitlement Analysis — CUPs, SUPs, and Planning Permission

Where the proposed use requires discretionary approval, analyze the applicable standard
and the strength of an application.

**For US — Conditional/Special Use Permits:**

Evaluate each standard finding required by the applicable ordinance. Typical findings:

1. **Consistency with general plan**: Is the proposed use consistent with the land use
   element and any applicable specific plan? Note any general plan amendment needed.
2. **Public health, safety, and welfare**: Identify impacts (traffic, noise, nuisance)
   and available mitigations. A traffic impact analysis (TIA) may be required.
3. **Development standards compliance**: Do the site plan and proposed development comply
   with applicable bulk, setback, parking, and landscaping standards?
4. **Compatibility with surrounding uses**: Compare the proposed use against adjacent and
   nearby zoning and uses. Identify any buffer or separation requirements.
5. **Conditions of approval**: Anticipate what conditions will be imposed (operating
   hours, noise limits, screening, traffic management). Check whether conditions create
   exaction issues post-Sheetz (2024).

**Exaction analysis** (triggered whenever the municipality proposes conditions involving
property dedication or monetary payment):

- Apply the **Nollan/Dolan/Koontz/Sheetz** framework:
  - **Essential nexus** (Nollan): Is there a nexus between the exaction and a legitimate
    state interest advanced by the permit condition?
  - **Rough proportionality** (Dolan): Is the burden imposed roughly proportional to the
    impact of the proposed development?
  - **Monetary exactions** (Koontz): The nexus/proportionality requirement applies to
    demands for money, not just property dedications.
  - **Legislative fee schedules** (Sheetz v. County of El Dorado, 601 U.S. 267 (2024)):
    The Nollan/Dolan requirements apply to generally applicable legislative impact fee
    schedules, not just individualized administrative conditions. Impact fee ordinances
    must now satisfy nexus and proportionality on their face.

**For UK — Planning Applications (TCPA 1990 s.70; PCPA 2004 s.38(6)):**

Evaluate the application against:

1. **Development plan presumption (s.38(6) PCPA 2004)**: The application must be
   determined in accordance with the development plan unless material considerations
   indicate otherwise. Identify the weight of relevant Local Plan policies.
2. **NPPF presumption in favour of sustainable development**: Where the development
   plan is absent, silent, or out of date (including sub-5-year housing land supply),
   the "tilted balance" strongly favours approval unless adverse impacts significantly
   and demonstrably outweigh benefits, or specific NPPF policies indicate otherwise.
3. **Material considerations**: Government policy (NPPF 2024); representations from
   statutory consultees (Highways England, Environment Agency, Historic England,
   OFWAT); design quality; economic effects; environmental impact (EIA where required).
4. **NPPF 2024 — Grey Belt**: Where the site is located in the Green Belt and classified
   as "grey belt" (limited contribution to the five Green Belt purposes), apply the golden
   rules: increased affordable housing requirement (50% target); infrastructure
   contributions; no new development with a net loss of trees. [VERIFY current grey belt
   methodology pending final NPPF 2025]
5. **Section 106 obligations (CIL Reg. 122 tests)**: Any proposed planning obligation
   must be: (1) necessary to make the development acceptable in planning terms; (2)
   directly related to the development; and (3) fairly and reasonably related in scale
   and kind. These tests parallel Nollan/Dolan/Koontz proportionality. Challenge
   non-compliant obligations.
6. **CIL liability**: Confirm whether the LPA has an adopted CIL charging schedule. CIL
   is charged per sqm of new floorspace above a minimum threshold, collected at
   commencement. Failure to submit a Commencement Notice before development begins
   triggers automatic loss of all CIL reliefs and surcharges.

**⟁ CLARIFY** — Where the project requires a discretionary decision and the required
findings are in doubt:

- "The proposed use may face compatibility challenges with adjacent [use type]. Do you
  want me to develop a mitigation framework, or first assess whether a rezone or
  development agreement might be preferable to a CUP?"
- "UK: The site is within the Green Belt. Is there existing evidence that this site
  qualifies as grey belt under the NPPF 2024 grey belt methodology? Without that
  evidence, the Green Belt sequential test applies and the application faces high risk."

### Step 6: Variance Analysis

Where dimensional non-compliance exists or a use variance is sought, apply the applicable
variance standard.

**Two categories of variances:**

| Type                 | Standard                 | Common Test                                                                                                | Availability                                     |
| -------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **Area/Dimensional** | "Practical difficulties" | Less demanding; considers feasibility, economic injury, substantiality, neighborhood impact, self-creation | Available in most US jurisdictions               |
| **Use**              | "Unnecessary hardship"   | Most demanding; requires conditions peculiar to property, not self-created, contrary to public interest    | Prohibited in some jurisdictions; rarely granted |

**Unnecessary Hardship Test (Use Variances) — 4-part analysis:**

1. Strict application would create unnecessary hardship (beyond mere inconvenience or loss
   of profit — loss of profit alone is insufficient in most jurisdictions)
2. The hardship results from conditions peculiar to the property (not the owner's
   personal circumstances)
3. The hardship was not self-created (e.g., prior owner's construction at the setback
   line does not justify a variance for an addition)
4. The variance will not be contrary to the public interest

**Practical Difficulties Test (Area Variances) — multi-factor balancing:**

- Whether strict compliance is feasible
- Whether significant economic injury results from strict compliance
- Whether the variance is substantial (variance of 10% is different from 50%)
- Whether it will adversely affect the neighborhood
- Whether the difficulty is self-created

[JURISDICTION-SPECIFIC] New York: Courts apply a five-factor test (Otto v. Steinhilber)
for use variances. California: area variances require findings that: strict application
is inconsistent with the purpose of the title; the variance will not impair the public
health, safety, and welfare (zoning code standard varies by municipality). UK: no
directly analogous variance procedure — non-compliant applications are determined on
their merits as planning applications with material considerations, and conditions or
Section 106 obligations can mitigate non-compliance.

**⟁ CLARIFY** — For borderline variance applications:

- "A dimensional variance of [X%] from the [setback/height/coverage] standard is
  sought. I need to know whether this is a dimensional variance (practical difficulties)
  or whether the underlying use also requires a use variance (unnecessary hardship). Can
  you clarify whether the use itself is not permitted in the zone, or only the dimensions
  are non-compliant?"
- "Is there documented evidence of physical conditions of the property (irregular shape,
  topography, existing encumbrances) that distinguish it from neighboring properties?
  This evidence is critical to a variance application."

### Step 7: Nonconforming Use Analysis

Analyze whether any existing use or structure has legal nonconforming status and the
scope of rights that flow from that status.

**Establishing Legal Nonconforming Status — 3-part test:**

1. **Lawful establishment**: Was the use lawfully established (with applicable permits)
   before the current zoning restriction was enacted?
2. **Antedating the restriction**: Did the use predate the enactment of the applicable
   zoning restriction that now prohibits or restricts it?
3. **Continuity**: Has the use been maintained continuously since establishment?

**Abandonment Analysis — 2-part test:**
Most ordinances create a rebuttable presumption of abandonment after a specified non-use
period (commonly 6 months to 2 years — [JURISDICTION-SPECIFIC]). To establish or rebut
abandonment, evaluate both:

- **Objective discontinuance**: Evidence of physical vacancy, removal of equipment,
  cessation of operations, change of locks, utility disconnection
- **Subjective intent**: Correspondence, lease terminations, business closures, owner
  statements, or conversely, evidence of intent to return (storage of business equipment,
  maintenance of utilities, active marketing for retenancy)

**Expansion and Intensification:**

- Expansion in area, floor area, or footprint is generally prohibited or requires a CUP
  in most jurisdictions
- Intensification of the same use (more trips, longer hours, higher volume) may be
  permitted within the scope of the original use or may require CUP depending on the
  local ordinance
- Change to a different nonconforming use: generally prohibited or requires showing the
  new use is equally or less nonconforming

**Natural Expansion Doctrine** [JURISDICTION-SPECIFIC — minority rule, Pennsylvania and
some others]: Allows expansion where reasonably necessary for the owner to remain
economically viable. Verify whether this doctrine applies in the applicable jurisdiction.

**Amortization:**
Some jurisdictions (California, some others) allow amortization of nonconforming uses
over a reasonable period rather than immediate termination. Courts have upheld
amortization as sufficient compensation. Pennsylvania and New Jersey have rejected
amortization as a per se taking requiring compensation. [JURISDICTION-SPECIFIC — verify
current state law on amortization]

**UK equivalent — Lawful Development Certificates:**
In the UK, the equivalent of nonconforming use analysis is a **Lawful Development
Certificate (LDC)** for existing use (TCPA 1990 s.191). An LDC certifies that:

- The existing use is lawful (has not been challenged within the 10-year limitation period
  for change of use enforcement)
- The existing use or operations are lawful as of a specified date

The 4-year rule applies to operational development and change of use to a single
dwellinghouse; the 10-year rule applies to other changes of use and breaches of condition.
[VERIFY current position under Planning and Infrastructure Act 2025 — proposed
unification of limitation periods]

**⟁ CLARIFY** — Where nonconforming use status is critical:

- "I need to confirm whether the use was lawfully established before the current zoning
  restriction. Do you have: (a) original building permits or certificates of occupancy
  from the pre-restriction era; (b) business licenses predating the restriction; or (c)
  aerial photography, assessor records, or other documentation establishing the use
  before the applicable zoning change?"
- "Has the property been vacant for any period since the use was established? If so, for
  how long, and were there any steps taken to demonstrate intent to return (e.g.,
  continued licensing, maintenance, marketing for tenants)?"

### Step 8: Subdivision, Development Agreements, and Vesting

**Subdivision Analysis:**

If the project involves division of land, evaluate:

1. **Minor vs. major subdivision threshold**: Typically fewer than 4–5 lots qualifies
   as a minor subdivision with expedited administrative processing; larger divisions
   require full planning commission review [JURISDICTION-SPECIFIC]
2. **Platting requirements**: Preliminary plat/tentative map → conditions of approval
   → final plat/map → recordation
3. **Dedication and improvement requirements**: Streets, utilities, open space, parks,
   drainage — evaluate against Nollan/Dolan/Koontz/Sheetz nexus and proportionality
   where dedications or fees are imposed
4. **Vesting Tentative Map (California)**: Cal. Gov. Code §§66498.1 et seq. — approval
   vests rights to develop in accordance with laws and standards in effect at the time
   the application is deemed complete; vesting period: 2 years after final map approval,
   extendable by application

**Development Agreements (US):**

Evaluate whether a development agreement would benefit or protect the project:

- **California** (Gov. Code §§65864–65869.5): Agreement must be consistent with the
  general plan; adopted by ordinance (subject to referendum); must specify duration,
  permitted uses, density, intensity, maximum height and size, and dedication provisions
  (§65865.2); vests developer's right to develop in accordance with existing policies,
  rules, and regulations for the term (§65866); recorded within 10 days (§65868.5); runs
  with the land and binds successors; typical terms 5–25 years
- **Other states**: Florida §163.3220 et seq.; Texas Local Gov. Code §212.172;
  Washington RCW 36.70B.170–210; Arizona A.R.S. §9-500.05 — each with materially
  different procedures and vesting protections [JURISDICTION-SPECIFIC]
- **Retained authority exception**: Local agency retains authority to impose new
  requirements if necessary to prevent a serious threat to public health or safety
  (Cal. Gov. Code §65869.5) — analyze scope of retained authority

**UK — Section 106 Agreements:**

Evaluate planning obligations under TCPA 1990 s.106:

- Does each proposed obligation satisfy all three CIL Regulation 122 tests?
  (necessary; directly related; fairly and reasonably related in scale)
- Are affordable housing obligations expressed as a percentage of units or sqm? Is there
  a viability assessment on file if obligations deviate from policy?
- Does the s.106 agreement survive changes of ownership and bind successors in title?
- Is there a mechanism to review or reduce obligations if market conditions change
  (viability review clauses)?
- What are the consequences of breach? (injunction; enforcement notice; withholding of
  reserved matters approval)

### Step 9: Environmental Review and Historic Preservation

**CEQA Analysis (California):**

Determine the applicable CEQA pathway:

| Pathway                   | Applies when                                                                        | Key risk                                                                                                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Statutory exemption**   | Explicitly exempt by statute (ministerial, emergency, qualifying infill housing)    | Confirm all qualifying conditions are met; exemptions are narrowly construed                                                                                                       |
| **Categorical exemption** | Fits a defined class (14 CCR §§15301–15333); no unusual circumstances or exceptions | Exception at §15300.2: significant historical resource; environmentally sensitive area; cumulative impacts; unusual circumstances — any of these defeats the categorical exemption |
| **Initial Study → ND**    | IS finds no substantial evidence of significant effect                              | "Substantial evidence" standard is low; any evidence that the project may have a significant effect can defeat an ND                                                               |
| **IS → MND**              | Significant effects can be mitigated to less than significant; MMRP required        | "Fair argument" standard: if any substantial evidence in the record supports a fair argument that impacts may be significant, an MND may be challengeable                          |
| **EIR**                   | Substantial evidence supports a fair argument that significant impacts may occur    | Must analyze: project description, alternatives (including No Project), environmental setting, significant impacts, mitigation, cumulative impacts, growth-inducing impacts        |

**CEQA VMT analysis (SB 743)**: Traffic significance is now measured in vehicle miles
traveled (VMT), not level of service (LOS). Applies statewide. Infill projects in
transit-priority areas may qualify for VMT presumption of less-than-significant impact.
[VERIFY current VMT thresholds by applicable CEQA lead agency or regional guidelines]

**CEQA litigation risk**: Petitioners must exhaust administrative remedies (raise each
issue before the lead agency during the public comment period). Statute of limitations:
30 days from posting of Notice of Determination (NOD); 180 days from approval if no NOD.
Apply the substantial evidence standard: courts uphold agency findings if supported by
substantial evidence in the whole record.

**NEPA Analysis (federal nexus projects):**

NEPA applies only when a federal nexus exists (federal funding, permit, license, or
action). Key trigger categories:

- Section 404 CWA wetlands fill permit (USACE) → NEPA review
- FHWA/FTA transportation project funding → NEPA review
- FHA/HUD/CDBG financing → NEPA review
- Coastal development in states with CZMA federally-approved coastal programs → NEPA
  may apply via federal consistency review

If a federal nexus exists, determine the NEPA tier:

1. **Categorical Exclusion (CE)**: No EA/EIS required if the action falls within an
   agency-specific CE and no extraordinary circumstances apply
2. **Environmental Assessment → FONSI**: For actions of uncertain significance; must
   complete within 1 year (Phase 2 rule, effective July 2024; verify current regulatory
   status — 2025 interim rule may affect some provisions)
3. **Environmental Impact Statement (EIS)**: For significant impacts; Draft EIS (45-day
   public comment minimum) → Final EIS → Record of Decision (ROD). Must complete within
   2 years under Phase 2 rule.

[VERIFY current NEPA regulatory framework — CEQ issued an interim rule in 2025 reverting
some Phase 2 provisions; verify current CFR text before relying on specific time limits]

**Section 106 NHPA Historic Preservation (US):**

Apply the 4-step process under 36 CFR Part 800 where a federal undertaking is present:

1. **Initiation (§800.3)**: Confirm federal undertaking and nexus. Define Area of
   Potential Effects (APE) — geographic area within which the undertaking may directly or
   indirectly alter the character or use of historic properties.
2. **Identification (§800.4)**: Identify and evaluate historic properties within the APE
   against National Register criteria (36 CFR §60.4, Criteria A–D). Confirm integrity
   in applicable aspects (location, design, setting, materials, workmanship, feeling,
   association). Consult with SHPO/THPO and consulting parties.
3. **Assessment of Adverse Effect (§800.5)**: Determine whether the undertaking will
   diminish the integrity of any historic property's character-defining features (direct
   or indirect physical, visual, auditory, atmospheric changes). Adverse effect examples:
   demolition; alteration of character-defining features; relocation; visual intrusion.
4. **Resolution of Adverse Effects (§800.6)**: Consult to develop alternatives or
   mitigations to avoid, minimize, or mitigate adverse effects. Outcome: Memorandum of
   Agreement (MOA) or Programmatic Agreement (PA) — legally binding; recorded with ACHP.
   Section 106 does not prohibit adverse effects; it requires consultation and good-faith
   mitigation.

**UK Historic Preservation:**

- **Listed Building Consent (LBC)**: Required for any works of demolition, extension,
  or alteration that would affect the character of a listed building — including interior
  features. Grades: I (exceptional, ~2%); II* (particularly important, ~6%); II (special
  interest, ~92%). Unauthorized works are a criminal offence. No statute of limitations
  for LBC enforcement. Historic England must be consulted for Grade I and II* buildings.
- **Conservation Area designation**: Within Conservation Areas, PD rights are restricted
  (Article 4 Directions commonly apply); trees protected (6 weeks' notice required for
  felling/lopping); LPA must preserve or enhance the character or appearance of the area.
- **EIA Historic Environment**: Schedule 2 EIA projects in or affecting sensitive historic
  environments require an Environmental Statement assessing heritage impact.

**⟁ CLARIFY** — Where environmental or historic review is triggered:

- "CEQA: The project falls within a potential categorical exemption (Class [X]), but the
  site is [near a potentially historic resource / within a sensitive environmental area].
  Has an environmental review been conducted or ordered by the lead agency? The categorical
  exemption may not apply."
- "Section 106: I have identified a federal nexus [specify]. Has the federal agency
  initiated the Section 106 process? If not, this must be completed before the federal
  authorization can be issued."

### Step 10: Risk Assessment, Recommendations, and Quality Verification

Before delivering the analysis, perform the quality verification sequence in the **Quality
Assurance Framework** section. Then produce the output using the **Output Format Template**.

**Risk Summary:**

For each identified issue:

- Classify severity using the **Zoning Status Classification** system
- Assign a confidence score using the **Confidence Scoring** framework
- For RED/NON-COMPLIANT items, run the **Self-Interrogation** 3-pass review
- Generate specific actionable recommendations

**Regulatory Takings Screening:**

Where the client is a property owner subject to a restrictive regulation, assess:

- **Lucas per se taking**: Does the regulation deprive the property of all economically
  beneficial use? (rare; limited to complete wipeout of value)
- **Penn Central balancing**: (1) Economic impact on the claimant; (2) interference with
  distinct investment-backed expectations; (3) character of the governmental action.
  Note: Penn Central applies to the parcel as a whole — contiguous commonly owned parcels
  may be aggregated (Murr v. Wisconsin, 582 U.S. 383 (2017)).
- **Exaction unconstitutionality**: Apply Nollan/Dolan/Koontz/Sheetz analysis to any
  permit conditions imposing property dedication or monetary payment.

---

## Zoning Issue Analysis Reference

### 1. Use Classification and Permitted Uses — Deep Analysis

**Key review points:**

- Confirm the current zoning district from the official zoning map (not informal sources)
- Identify the use table for the district: permitted (P), conditional (C), not permitted (NP)
- Check for overlay zones that may restrict or expand base district permissions
  (flood zone, airport overlay, coastal zone, historic overlay)
- Verify whether recent ordinance amendments have changed use tables for the district
- For mixed-use developments, classify each use component separately

**Common issues:**

- Relying on outdated zoning maps or informal representations without checking the
  current adopted zoning ordinance
- Failing to identify overlay zones that further restrict permitted uses
- Assuming that a use is permitted because a similar use was historically permitted
  without verifying the current use table
- UK: Assuming that a change within the UCO does not require prior approval when a
  Class MA or other prior approval right has specific conditions

**[JURISDICTION-SPECIFIC]** California: Housing Accountability Act (Gov. Code §65589.5)
limits local government authority to deny qualifying affordable housing projects
consistent with objective standards. Builder's remedy: when a local jurisdiction lacks
a valid housing element, applicants may seek approval for projects that provide
affordable housing even where the project does not conform to the general plan or zoning.

### 2. Conditional/Special Use Permits — Deep Analysis

**Key review points:**

- Identify each finding required by the applicable ordinance
- Assess the strength of evidence supporting each finding
- Anticipate conditions of approval and assess their impact on project feasibility
- Evaluate whether any proposed conditions would constitute an unconstitutional exaction
  (Sheetz — applies to legislatively enacted fees; Nollan/Dolan/Koontz — applies to
  administrative conditions)
- Assess appeal rights and the standard of review (de novo vs. substantial evidence)

**Common issues:**

- Underestimating the impact of discretionary review on project timeline and cost
  (environmental review alone can add 12–24 months for complex projects)
- Accepting overly broad conditions of approval that effectively eliminate project
  feasibility
- Failing to challenge exactions that lack essential nexus or rough proportionality
  to the project's impacts
- Missing the statute of limitations on challenging CUP conditions
  [JURISDICTION-SPECIFIC — California: typically 90 days from decision]

### 3. Variances — Deep Analysis

**Key review points:**

- Confirm whether a dimensional or use variance is needed (different standards)
- Identify conditions peculiar to the property that distinguish it from its neighbors
  (irregular lot shape, topographic constraints, existing encumbrances, physical
  conditions)
- Verify the hardship was not self-created
- Assess whether granting the variance would establish an adverse precedent for the
  neighborhood
- For use variances: assess whether any state law prohibits use variances in the
  applicable jurisdiction

**Common issues:**

- Conflating unnecessary hardship (use variance) with practical difficulties (area
  variance) — the standards are materially different and the wrong argument defeats
  the application
- Relying on financial hardship alone (loss of profit) — courts consistently reject
  this as a basis for variance
- Self-created hardship (e.g., prior owner constructed without permits, reducing
  available setbacks; owner subdivided a lot creating inadequate buildable area)
- Failing to document property-specific physical conditions in the application record

### 4. Nonconforming Use — Deep Analysis

**Key review points:**

- Confirm the use was lawfully established before the applicable restriction
- Assess the sufficiency of documentary evidence (permits, licenses, aerial photography,
  assessor records, historic maps, witness declarations)
- Analyze the abandonment risk under the applicable ordinance period and the
  objective/subjective factors
- Assess expansion and intensification rights under the local ordinance
- Evaluate amortization exposure if applicable [JURISDICTION-SPECIFIC]

**Common issues:**

- Assuming a use is nonconforming without documenting that it was lawfully established
  before the applicable restriction
- Failing to recognize that a period of vacancy (even partial) may trigger the
  abandonment presumption, with the burden shifting to the owner to rebut intent to return
- Attempting to expand a nonconforming use beyond the scope of the original use,
  triggering loss of nonconforming status
- UK: Failing to apply for an LDC to establish lawful use status before investing in
  improvements — without an LDC, enforcement action remains possible within the
  limitation period

### 5. Subdivision and Platting — Standard Analysis

**Key review points:**

- [ ] Correct subdivision classification (minor vs. major; threshold [JURISDICTION-SPECIFIC])
- [ ] Preliminary plat/tentative map completeness: lot configuration, streets, utilities,
      drainage, easements
- [ ] Conditions of approval are feasible and proportionate (Nollan/Dolan/Koontz/Sheetz
      for any dedication or fee requirements)
- [ ] Final plat/map requirements: licensed surveyor certification; lot lines, bearings,
      and dimensions; easements; dedications
- [ ] Recordation requirements: timing; county recorder requirements; subsequent
      conveyances only possible after recordation

**[JURISDICTION-SPECIFIC]** California Vesting Tentative Map: Confirm application was
deemed complete before the vesting tentative map was filed; confirm vesting period;
verify consistency with the general plan as of the date of deemed-complete application.

### 6. Environmental Review (CEQA/NEPA) — Deep Analysis

**Key review points:**

- [ ] CEQA: Confirm lead agency identity; determine applicable pathway (statutory
      exemption, categorical exemption, ND, MND, or EIR)
- [ ] Categorical exemption: Verify no exception applies (§15300.2 — significant
      historical resource; ESA; cumulative impacts; unusual circumstances)
- [ ] EIR: Confirm project description adequacy (the "rule of reason" — description
      must be stable and accurate enough for meaningful public review)
- [ ] VMT analysis: Post-SB 743, traffic analyzed under VMT methodology, not LOS
- [ ] CEQA exhaustion: All grounds for challenge must be raised before the lead agency
      during the comment period, or they are waived in subsequent litigation
- [ ] NEPA: Identify federal nexus; determine CE/EA/EIS tier; review 2-year EIS deadline
      and 1-year EA deadline under Phase 2 rule (verify current regulatory status)
- [ ] Cumulative impacts: Both CEQA and NEPA require analysis of the project's
      contribution to cumulative environmental effects from related projects

**[JURISDICTION-SPECIFIC]** CEQA applies only in California. Other states have their own
SEPAs (e.g., Washington SEPA, RCW Ch. 43.21C; New York SEQRA, Environmental Conservation
Law Art. 8) with different standards and processes. NEPA applies nationwide for projects
with a federal nexus regardless of state.

### 7. Historic Preservation — Deep Analysis

**Key review points:**

- [ ] US — Section 106: Identify federal undertaking; define APE; identify historic
      properties in the APE (National Register listed or eligible); assess adverse effect;
      resolve adverse effect through MOA or PA consultation
- [ ] National Register eligibility: Apply Criteria A–D and assess integrity in relevant
      aspects (location, design, setting, materials, workmanship, feeling, association)
- [ ] Local landmark status: Identify whether local historic landmark or historic district
      designation applies and what design review requirements flow from designation
- [ ] UK — Listed Building Consent: Confirm grade; identify required works; confirm LBC
      application and Historic England consultation for Grade I and II\* buildings
- [ ] UK — Conservation Area: Confirm CA boundary; assess PD right restrictions (Article 4
      Directions); tree protection requirements; preservation or enhancement of character test

**[JURISDICTION-SPECIFIC]** Section 106 NHPA applies only where there is a federal
undertaking (federal agency action, funding, permit, or license). Purely local and state
projects without any federal nexus are not subject to Section 106, though local historic
preservation ordinances may impose analogous requirements.

---

## Zoning Status Classification

### COMPLIANT — No Action Required

The property, use, and development program fully comply with applicable zoning, permits,
entitlements, and standards. No further regulatory action is required for the proposed
use or development.

**Examples:**

- Proposed office use is listed as permitted in the commercial district; dimensions
  comply with setback and height limits
- UK: Change from retail (Class E) to office (Class E) — no planning permission required

**Action**: Note for awareness. Proceed with development program.

### REQUIRES ACTION (YELLOW) — Entitlement or Compliance Steps Needed

The property or development program does not comply as of right but can achieve
compliance through a defined regulatory process (CUP, variance, LDC, prior approval).
The outcome is achievable but requires time, cost, and discretionary decision-making.

**Examples:**

- Proposed use requires a CUP; standard findings can likely be satisfied with appropriate
  mitigations and conditions
- Dimensional variance of modest scope (under 20%) where property-specific hardship
  evidence is available
- Nonconforming use at risk of abandonment if a 60-day vacancy period is exceeded

**Action**: Describe the required process, standard findings, estimated timeline, and
key risks. Recommend specific preparatory steps before application submission.

### NON-COMPLIANT / ESCALATE (RED) — Material Risk Requiring Immediate Attention

The property or development program cannot proceed without significant regulatory
action (rezoning, EIR, development agreement), faces a material legal challenge
(exaction unconstitutionality, takings claim, Section 106 violation), or is in active
violation of zoning code.

**Examples:**

- Proposed use is not listed as permitted or conditionally permitted in the applicable
  district — rezoning required
- Nonconforming use has been abandoned — legal nonconforming status lost
- CEQA EIR required but not prepared; project approval without EIR is subject to
  CEQA litigation challenge
- Exaction fee schedule lacks Sheetz-compliant nexus study — challenge viable
- Active unpermitted construction or change of use in violation of zoning code or
  planning condition

**Action**: Explain the specific risk with legal basis, identify the available remedial
path(s), estimate exposure (enforcement costs, delay, monetary penalties), and recommend
escalation to qualified land use counsel immediately.

### LEGAL UNCERTAINTY (AMBER) — Genuinely Uncertain; Professional Review Required

The legal status of the use, entitlement, or obligation is genuinely uncertain due to
ambiguous ordinance language, conflicting authority, pending regulatory changes, or
insufficient factual information to make a definitive determination.

**Examples:**

- Whether a particular use falls within Class E or is sui generis under UCO 2020 where
  the use is a novel hybrid activity
- Whether a prior use was lawfully established before the applicable restriction, where
  documentary evidence is incomplete
- Whether an amortization ordinance constitutes an unconstitutional taking in a
  jurisdiction that has not squarely addressed the question

**Action**: Present both interpretations, identify the key factual or legal questions that
must be resolved, and recommend professional review and/or a formal zoning confirmation
letter from the municipality.

---

## Prioritization Framework

### Tier 1 — Must-Resolve (Project-Critical)

Issues where the development cannot proceed without resolution:

- Zoning district does not permit the proposed use — rezoning or plan amendment required
- Active enforcement violation or stop-work order
- EIR required but not completed — any project approval without EIR is voidable
- Section 106 consultation not completed — federal authorization cannot issue
- Loss of legal nonconforming status through abandonment — use must cease
- Development agreement vesting rights expired or not established — project exposed to
  intervening ordinance changes

### Tier 2 — Material Issues (Strong Recommendations)

Issues that materially affect project feasibility, timing, or cost but have a defined
resolution path:

- CUP/SUP required — assess standard findings and timeline (typically 3–9 months)
- Variance required — assess hardship evidence and approval probability
- CEQA MND or EIR pathway — scope environmental review and timeline (ND: 2–3 months;
  MND: 3–6 months; EIR: 12–24+ months)
- Historic preservation mitigation required via MOA — negotiate scope of mitigation
- UK Section 106 obligation compliance — review terms and conditions

### Tier 3 — Advisory (Optimize and Protect)

Issues that improve the position or protect against future risk but can be addressed
on a secondary schedule:

- Development agreement recommended to vest development rights for large or phased
  projects
- LDC application recommended to formally establish legal nonconforming status
- Exaction nexus study review — challenge excessive impact fees legislatively
- UK: Prior approval application to confirm Class MA PD right
- Monitoring of pending zoning amendments that could affect the project

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise
before delivering.

| Gate           | Rule                                                                                                                                                                                                       | Fail Action                                              |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, code provision, regulation, or established case law principle                                                                                                  | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | All citations follow a consistent, recognizable format for the jurisdiction (e.g., US Code: 42 U.S.C. §4321; Cal. Gov. Code §65864; UK: TCPA 1990 s.55; SI 2020/757)                                       | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments, repeals, or pending regulatory changes                                                                                                                       | Flag "[CHECK CURRENCY — may have been amended]"          |
| **Domain**     | Analysis stays within the applicable jurisdiction's law. No assumptions from other jurisdictions leaking in (e.g., applying CEQA principles to a UK planning analysis; applying TCPA 1990 to a US project) | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden. If genuinely uncertain about a local ordinance standard or case law application, say so                                                                         | Add confidence qualifier                                 |

### Self-Interrogation for RED/NON-COMPLIANT Items

For any issue classified as RED or NON-COMPLIANT, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity:**

- Does the non-compliance finding follow logically from the cited statute, ordinance
  provision, or case law?
- Would a local zoning administrator or planning commission actually reach this conclusion
  on these facts?
- Is there a counter-argument (e.g., the use falls within a broader category; the
  ordinance is ambiguously drafted in the project's favor)?

**Pass 2 — Completeness:**

- Have all relevant ordinance provisions been considered (base district; overlay zones;
  supplemental use regulations; recently adopted amendments)?
- Have all available regulatory pathways been evaluated (CUP; variance; development
  agreement; rezoning; vesting tentative map)?
- Are there applicable state or federal preemptions that may override local restrictions
  [JURISDICTION-SPECIFIC — California HAC, builder's remedy; federal telecommunications
  preemption under Section 332 of the Communications Act]?

**Pass 3 — Challenge:**

- What is the strongest argument that this classification is incorrect?
- Under what circumstances might a qualified land use attorney accept or mitigate this
  risk without the action recommended?
- Is the RED classification proportionate, or is this actually AMBER (genuinely
  uncertain) or YELLOW (correctable through a defined process)?

If any pass reveals a weakness, revise before delivery. Mark the audit trail:
`self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

For each material finding, assign a confidence level:

| Level        | Range     | Meaning                                                                           | Action                                                         |
| ------------ | --------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear zoning ordinance text; settled case law; no ambiguity                       | State with confidence                                          |
| **High**     | 0.80–0.94 | Strong authority; minor interpretive questions; well-established standard         | State with brief caveat                                        |
| **Probable** | 0.60–0.79 | Good arguments but reasonable minds could differ; ordinance language is ambiguous | State with reasoning and contra-indicators                     |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing interpretations; insufficient facts                | Flag for professional review with both sides of the argument   |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                                                           | Do not assert; flag "[UNCERTAIN — land use counsel to advise]" |

---

## Glass Box Audit Trail

Every zoning and land use analysis output MUST include a Glass Box audit section at the
end. This makes the reasoning traceable and auditable.

```yaml
glass_box:
  property_identifier: "[Address, APN, or property description]"
  analysis_type: "[Zoning Compliance Assessment / Variance Analysis / Entitlement Risk Review / Environmental Review / Historic Preservation Review / Full Zoning Analysis]"
  client_role: "[Property owner / Developer / Purchaser / Lender / Municipal / Adjacent owner]"
  jurisdiction: "[State and municipality (US) / LPA name (UK)]"
  zoning_district: "[Confirmed from official zoning map, or UNCONFIRMED]"
  proposed_use: "[Development program as analyzed]"
  regulatory_framework_loaded: "[Zoning ordinance, year adopted; CEQA / NEPA if applicable; NPPF year if UK]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path to temp file or 'Not created']"
  topics_analyzed: "[number]"
  issues_identified:
    red_non_compliant: "[number]"
    yellow_requires_action: "[number]"
    amber_uncertain: "[number]"
    green_compliant: "[number]"
  statutes_consulted:
    - "[Statute / ordinance provision — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  case_law_consulted:
    - "[Case — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no RED items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  assumptions:
    - "[Any assumptions made where facts were unclear]"
  limitations:
    - "[Scope limitations: e.g., 'Local zoning code not available — analysis based on standard zoning enabling statute framework'; 'Environmental review not analyzed — separate CEQA review required']"
  reviewer: "AI-assisted — requires qualified land use counsel review before reliance"
```

---

## Anti-Patterns

Common errors in zoning and land use analysis that this skill is designed to detect and
avoid:

1. **Relying on informal zoning representations** — Accepting an owner's, broker's, or
   escrow officer's oral statement about zoning rather than confirming from the official
   adopted zoning ordinance and zoning map. Zoning codes are amended frequently; the only
   authoritative source is the current official ordinance and the GIS zoning map portal.
   Always confirm the current zoning district from official sources.

2. **Ignoring overlay zones** — Analyzing only the base zoning district while overlooking
   overlay zones (flood zone, coastal zone, airport hazard overlay, historic preservation
   overlay, groundwater overlay, wildland-urban interface overlay) that impose additional
   use restrictions or development standards. Always check for overlay zones after
   confirming the base district.

3. **Confusing variance standards** — Arguing "practical difficulties" for a use variance
   (which requires "unnecessary hardship") or vice versa. The distinction is
   jurisdictionally specific but almost universally material: the wrong standard is fatal
   to the application. Identify the variance type before selecting the applicable test.

4. **Treating loss of profit as unnecessary hardship** — Courts uniformly reject economic
   loss alone as a basis for variance. Hardship must arise from conditions peculiar to
   the property, not the owner's financial circumstances. Frame hardship arguments around
   physical characteristics (irregular shape, topography, encumbrances), not inability
   to maximize investment returns.

5. **Assuming continuous nonconforming use without documentation** — Asserting legal
   nonconforming status without documentary evidence that: (a) the use was lawfully
   established before the applicable restriction; and (b) the use has been maintained
   continuously since. Without documentation, the burden cannot be met. Identify and
   secure all available pre-restriction permits, licenses, aerial photos, and assessor
   records before asserting nonconforming status.

6. **Ignoring the abandonment clock** — Failing to monitor vacancy periods for
   nonconforming uses against the applicable ordinance's abandonment presumption period.
   Even a brief vacancy that tips the ordinance threshold shifts the burden to the owner
   to demonstrate intent to return. Establish a vacancy monitoring protocol for properties
   with nonconforming uses.

7. **Applying CEQA categorical exemptions without checking exceptions** — Using a CEQA
   categorical exemption without confirming that none of the §15300.2 exceptions apply.
   The exceptions — significant historical resource; environmentally sensitive area;
   cumulative impacts; unusual circumstances — are broader than they appear and are a
   common basis for CEQA litigation. Always run the §15300.2 exception analysis before
   invoking a categorical exemption.

8. **Failing to exhaust CEQA administrative remedies** — Omitting to raise specific
   issues during the public comment period before the lead agency. Under CEQA (Pub.
   Resources Code §21177), a petitioner cannot challenge an approval in court on a ground
   not raised before the lead agency at the earliest practicable opportunity. Track all
   issues raised during the administrative process.

9. **Omitting Section 106 consultation when a federal nexus exists** — Proceeding with
   a federal permit or funding application without initiating or completing Section 106
   review under 54 U.S.C. §306108. Section 106 is a prerequisite to the federal
   authorization. Failure to consult can invalidate the federal action and expose the
   project to NHPA litigation.

10. **Confusing UK "Section 106" with US "Section 106"** — These are entirely different
    legal instruments. UK TCPA 1990 s.106 (planning obligations between developer and
    LPA) is unrelated to US NHPA Section 106 (federal historic preservation review
    process under 54 U.S.C. §306108). Using the wrong framework causes fundamental
    analytical error in cross-border projects or multi-jurisdiction analyses.

11. **Ignoring Sheetz in legislative fee challenges** — Post-Sheetz v. County of El
    Dorado (601 U.S. 267 (2024)), the Nollan/Dolan nexus and proportionality requirements
    apply to legislatively enacted impact fee schedules, not just individualized
    administrative conditions. Impact fees set by ordinance can now be challenged as
    unconstitutional exactions. Always assess whether impact fees imposed on a project
    satisfy nexus and proportionality requirements — and advise clients of litigation
    options where they do not.

12. **Misidentifying the Penn Central parcel** — Applying Penn Central takings analysis
    to an isolated portion of the property (e.g., air rights, a portion of the lot) rather
    than the parcel as a whole. Murr v. Wisconsin (582 U.S. 383 (2017)) confirmed that
    contiguous commonly owned parcels may be treated as one parcel for Penn Central
    purposes, making a per se Lucas taking less likely. Always identify the full extent
    of commonly owned contiguous land before applying a regulatory takings analysis.

13. **Misclassifying UK use classes post-UCO 2020** — Applying pre-2020 use class
    analysis (A1/A2/A3/B1) to post-2020 planning applications. The UCO 2020 (SI
    2020/757 effective 1 September 2020) created Class E, F.1, and F.2, replacing the
    former A and most B1 classes. Analysis using the old classes is wrong. For pre-2020
    permissions and uses, apply the transitional provisions.

14. **Treating Class MA prior approval as a planning refusal mechanism** — Assuming that
    LPA concerns about a Class MA (E-to-C3) prior approval application can include general
    planning merits objections. Prior approval for Class MA is limited to the specified
    enumerated criteria (transport; contamination; flooding; noise; natural light; impact
    on surrounding area; national security). The LPA cannot refuse prior approval on
    general design or planning policy grounds not in the enumerated list.

15. **Underestimating Section 106 agreement enforceability** — Failing to check whether
    proposed Section 106 obligations satisfy the CIL Regulation 122 three-part test.
    Non-compliant obligations are void and unenforceable — the LPA cannot rely on them,
    and the developer cannot be bound by them. Review each obligation against the test
    before signing.

16. **Accepting development agreement terms without recording verification** — Executing
    a development agreement without confirming it was adopted by ordinance (California
    requirement) and recorded within 10 days. An unrecorded development agreement does
    not run with the land and does not protect successors in interest. Verify the full
    execution formalities before relying on vesting protections.

17. **Failing to monitor NPPF and local plan updates** — Treating the NPPF and local
    plan as static documents. Both are updated periodically (NPPF 2024; NPPF 2025
    consultation ongoing as of March 2026). A local plan that was current at the time of
    application may be superseded by NPPF changes that shift the presumption in favour
    of or against the proposed development. Track policy update cycles throughout the
    planning application period.

---

## Writing Standards

Apply these standards before delivering any output.

**Plain-language discipline:**

- Use active voice: "The proposed use requires a CUP" not "A CUP is required for the
  proposed use to proceed"
- Name the actor: "The applicant must demonstrate..." not "It must be demonstrated that..."
- Short sentences. One point per sentence.
- Specific citations, not vague references: "Pub. Resources Code §21177" not "CEQA's
  exhaustion requirement"
- No filler: "This is a complex regulatory landscape" adds nothing — describe the
  specific complexity

**Quality gates before delivery:**

1. Can a property owner without legal training understand the executive summary?
2. Can a planning attorney understand and respond to each specific recommendation?
3. Is every legal claim backed by a specific citation or flagged [VERIFY]?
4. Are any phrases vague, hedging, or ambiguous? Fix them.
5. Could any sentence be shorter without losing meaning? Shorten it.
6. Are all [JURISDICTION-SPECIFIC] markers correctly placed — no jurisdiction-specific
   law stated as universal?

**For client-facing summaries:**

- No jargon without explanation at first use
- Lead with the bottom line (compliance status) before the reasoning
- Prioritize issues in order of severity (RED before YELLOW before GREEN)
- Include specific next steps with responsible party and estimated timeline

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 3, search for the current local zoning ordinance provisions for the applicable
  district and use tables
- Search for relevant CEQA or NEPA case law in the applicable jurisdiction
- Search for National Register listings and determinations for the APE
- Search for recent local ordinance amendments affecting the property or district
- Save the most relevant results to `/tmp/legalcode-zoning-research-[property].md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Proceed with web search for publicly available zoning ordinances, GIS portals, and
  planning department resources
- Mark all ordinance section references, case law citations, and regulatory standards
  with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected"`
- Focus the analysis on framework and workflow; advise the user to verify specific
  local ordinance provisions from the official municipal code

---

## Multi-Stakeholder Mapping

For every zoning analysis, identify all affected stakeholders — not just the applicant:

| Stakeholder                  | Role        | Affected Issues                                        | Impact     | Action Required                                            |
| ---------------------------- | ----------- | ------------------------------------------------------ | ---------- | ---------------------------------------------------------- |
| Property owner               | Primary     | All issues                                             | Direct     | Owns entitlement risk and cost                             |
| Developer/applicant          | Primary     | CUP, EIR, s.106 process                                | Direct     | Prepares and submits applications                          |
| Adjacent property owners     | Third party | Compatibility, variances, nonconforming use            | Indirect   | Notice and comment rights; standing to appeal and litigate |
| Municipality/LPA             | Regulator   | All issues                                             | Regulatory | Decision-maker; enforcement authority                      |
| Historic preservation bodies | Regulator   | Section 106 NHPA; LBC; Conservation Area               | Regulatory | Consulting party; ACHP / Historic England comment          |
| Environmental agencies       | Regulator   | CEQA/NEPA; Section 404 CWA; ESA                        | Regulatory | Lead agency or commenting agency                           |
| Lender                       | Financier   | Zoning compliance; entitlement risk; nonconforming use | Financial  | Due diligence; title insurance; loan condition compliance  |
| Future purchasers/successors | Third party | Development agreement vesting; s.106 obligations       | Long-term  | Run with the land; bound by recorded obligations           |

---

## Localization Notes

**United States — State-by-State Divergences:**

- **California**: Most comprehensive land use regulatory framework in the US; CEQA,
  Subdivision Map Act, HAC, builder's remedy, specific plans, development agreements,
  vesting tentative maps, Density Bonus Law, SB 330, SB 9, SB 10, AB 2011, SB 423.
  Also note: amortization of nonconforming uses is permitted (MBIA v. City of Glendale);
  5-year and 10-year development permit extension statutes.
- **New York**: Zoning based on enabling legislation Town Law §261 et seq. / Village Law
  §7-700 et seq. / General City Law §20(24). Strong use variance standard (Otto v.
  Steinhilber — 4-part test). City of New York: NYC Zoning Resolution, ULURP process.
  SEQRA (State Environmental Quality Review Act) for state/local environmental review.
- **Texas**: No statewide zoning enabling statute for cities over 5,000 but broad home
  rule; Houston famously lacks traditional zoning. No SEPA equivalent. Development
  agreements under Local Gov. Code §212.172.
- **Florida**: Growth management framework; state-mandated comprehensive planning
  (Ch. 163 Florida Statutes); Development of Regional Impact (DRI) process for large
  projects; development agreements under §163.3220 et seq. Florida Environmental Policy
  Act (FEPA) for state projects.
- **Washington**: SEPA (RCW Ch. 43.21C); Growth Management Act (RCW Ch. 36.70A);
  development agreements under RCW 36.70B.170–210; Critical Areas Ordinances (CAOs)
  for wetlands, fish and wildlife habitat, geologically hazardous areas.

**United Kingdom — Devolution:**

- **England**: TCPA 1990, PCPA 2004, Planning and Infrastructure Act 2025, NPPF 2024.
  Central government retains significant influence via NPPF and Secretary of State
  call-in powers.
- **Scotland**: Town and Country Planning (Scotland) Act 1997; Scottish Planning Policy
  (SPP); National Planning Framework 4 (NPF4, February 2023). Significant differences
  from England: no CIL; planning obligations under s.75 TCPA 1997 (Scotland).
- **Wales**: Planning Policy Wales (PPW); Technical Advice Notes (TANs). Planning Act
  (Wales) 2015 reforms. No CIL — developer contributions by s.106 only.
- **Northern Ireland**: Planning Act (Northern Ireland) 2011; Strategic Planning
  Policy Statement (SPPS). Department for Infrastructure (DfI) retains significant role.

---

## Output Format Template

```markdown
# Zoning and Land Use Analysis — [Property Identifier]

**Prepared for**: [Client name / role]
**Property**: [Address / APN / description]
**Zoning District**: [Confirmed classification / Unconfirmed — source]
**Current Use**: [Existing use]
**Proposed Use/Development**: [Development program]
**Jurisdiction**: [Municipality, State/Country]
**Regulatory Framework**: [Zoning ordinance year; CEQA / NPPF / UCO 2020 / etc.]
**Analysis Date**: [Date]
**Prepared by**: AI-assisted analysis — requires qualified land use counsel review

---

## Executive Summary

[2–4 sentences: overall compliance status; most critical issues (RED/NON-COMPLIANT
items first); recommended immediate actions. Lead with the bottom line.]

---

## Compliance Status Overview

| Issue Category                            | Status                                                    | Confidence                        | Priority     |
| ----------------------------------------- | --------------------------------------------------------- | --------------------------------- | ------------ |
| Use classification                        | [COMPLIANT / REQUIRES ACTION / NON-COMPLIANT / UNCERTAIN] | [Definite/High/Probable/Possible] | [Tier 1/2/3] |
| Entitlement (CUP/SUP/planning permission) | —                                                         | —                                 | —            |
| Dimensional/bulk compliance               | —                                                         | —                                 | —            |
| Nonconforming use status                  | —                                                         | —                                 | —            |
| Subdivision / platting                    | —                                                         | —                                 | —            |
| Environmental review                      | —                                                         | —                                 | —            |
| Historic preservation                     | —                                                         | —                                 | —            |
| Development agreement / vesting           | —                                                         | —                                 | —            |
| Exaction proportionality                  | —                                                         | —                                 | —            |

---

## Issue-by-Issue Analysis

### [Issue Category] — [COMPLIANT / REQUIRES ACTION / NON-COMPLIANT / UNCERTAIN] | Confidence: [level]

**Current status**: [What the current ordinance / regulation provides]
**Analysis**: [Analysis of how the property / proposed use relates to the standard]
**Legal basis**: [Specific statutory, ordinance, or case law citation]
**Risk**: [Consequence of non-compliance or the applicable risk if requires action]
**Recommendation**: [Specific next steps]

[Repeat for each issue]

---

## Prioritized Action Plan

### Tier 1 — Must-Resolve Before Proceeding

- [ ] [Action item]: [Specific step; responsible party; estimated timeline; estimated cost]

### Tier 2 — Material Issues to Address in Parallel

- [ ] [Action item]: [Specific step; responsible party; estimated timeline]

### Tier 3 — Advisory / Future Risk Management

- [ ] [Action item]: [Specific step; timing recommendation]

---

## Stakeholder Impact Map

[Table from Multi-Stakeholder Mapping section, populated with project-specific data]

---

## Next Steps Summary

| Action                                     | Owner                         | Timeline    | Estimated Cost |
| ------------------------------------------ | ----------------------------- | ----------- | -------------- |
| [e.g., Submit CUP application]             | Applicant / Land use attorney | [X months]  | [Range]        |
| [e.g., Commission traffic impact analysis] | Applicant / Traffic engineer  | [X weeks]   | [Range]        |
| [e.g., Obtain zoning confirmation letter]  | Owner / Attorney              | [1–2 weeks] | [Low]          |

---

## Glass Box Audit Trail

[YAML block from Glass Box template above, fully populated]
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis for the `legalcode-zoning-land-use-analysis` skill. Based on deep research into US zoning and land use law (Village of Euclid v. Ambler Realty Co., 272 U.S. 365 (1926); Penn Central Transportation Co. v. City of New York, 438 U.S. 104 (1978); Nollan v. California Coastal Commission, 483 U.S. 825 (1987); Dolan v. City of Tigard, 512 U.S. 374 (1994); Koontz v. St. Johns River Water Management District, 570 U.S. 595 (2013); Sheetz v. County of El Dorado, 601 U.S. 267 (2024); Lucas v. South Carolina Coastal Council, 505 U.S. 1003 (1992); Murr v. Wisconsin, 582 U.S. 383 (2017)); CEQA (Pub. Resources Code §§21000–21189.3; 14 CCR §§15000–15387); NEPA (42 U.S.C. §§4321–4370m-12; 40 CFR Parts 1500–1508, Phase 2 Rule May 2024); Section 106 NHPA (54 U.S.C. §306108; 36 CFR Part 800); California Development Agreements (Gov. Code §§65864–65869.5); UK Town and Country Planning Act 1990; Use Classes Order 2020 (SI 2020/757 as amended by SI 2024/141); GPDO 2015 (SI 2015/596 as amended); Planning and Infrastructure Act 2025; NPPF December 2024; Planning (Listed Buildings and Conservation Areas) Act 1990; CIL Regulations 2010. Structural methodology adapted from the legalcode-contract-review gold standard quality framework (2-agent analysis pipeline, 18 required elements, Glass Box audit trail, Self-Interrogation, Citation Quality Gates, Confidence Scoring, Anti-Patterns catalogue, Writing Standards).
