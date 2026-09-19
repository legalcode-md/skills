---
name: legalcode-environmental-compliance-review
description: Reviews environmental compliance obligations across US, EU, and UK regulatory frameworks.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Reviews environmental compliance obligations across US, EU, and UK regulatory frameworks. Use when conducting Phase I or Phase II Environmental Site Assessment review, assessing CERCLA liability and innocent landowner or bona fide prospective purchaser defenses, evaluating NEPA environmental impact assessment requirements, auditing Clean Air Act Title V or PSD/NSR permit compliance, reviewing Clean Water Act Section 404 wetlands permitting or NPDES discharge compliance, assessing RCRA hazardous waste generator status or TSD permit obligations, reviewing EU Environmental Impact Assessment Directive (2011/92/EU) compliance, evaluating EU Industrial Emissions Directive (IED 2.0, 2024/1785) permit requirements, analyzing UK Environment Act 2021 biodiversity net gain or Office for Environmental Protection obligations, reviewing UK Environmental Permitting Regulations 2016 compliance, assessing Part IIA contaminated land liability, conducting M&A environmental due diligence, evaluating PFAS hazardous substance liability post-April 2024 EPA designation, reviewing EU REACH SVHC obligations, analyzing EU CS3D or CSRD environmental due diligence requirements, and assessing remediation obligations under NCP, state VCPs, or EU/UK remediation regimes. Covers pre-transaction environmental screens, post-acquisition compliance programs, permit transfer requirements, and regulatory reporting obligations. Jurisdiction-specific analysis available for US (federal and state), EU (Member State implementation), and UK (England and Wales; Scotland; Northern Ireland) with cross-border PFAS, REACH, and Taxonomy alignment.


# Legalcode Environmental Compliance Review

> **Disclaimer**: This skill provides a framework for AI-assisted environmental compliance
> review. It does not constitute legal advice. All outputs should be reviewed by a qualified
> environmental lawyer or licensed environmental professional in the relevant jurisdiction
> before reliance. Environmental statutes, regulations, and enforcement policies change
> frequently — verify all citations and regulatory thresholds against current authoritative
> sources. Statutory and case law references cited from memory carry hallucination risk —
> treat any unverified citation as requiring independent confirmation before use.

---

## Purpose and Scope

This skill conducts structured environmental compliance reviews across US, EU, and UK
regulatory frameworks — whether for pre-acquisition due diligence, ongoing operational
compliance, regulatory permit audits, or M&A transaction support.

**Covers:**

- Phase I ESA (ASTM E1527-21) review and recognized environmental condition (REC) assessment
- Phase II ESA scope design (ASTM E1903-19) and findings interpretation
- CERCLA liability analysis: PRP status, landowner defenses (BFPP, Innocent Landowner,
  Contiguous Property Owner), arranger liability (Burlington Northern standard), PFAS exposure
- NEPA review: EA/EIS requirements, categorical exclusions, scoping, post-2025 framework
- Clean Air Act: Title V operating permits, PSD/NSR, HAP standards, GHG reporting
- Clean Water Act: post-Sackett WOTUS jurisdiction, Section 404 dredge/fill, NPDES, Section 401
- RCRA: generator status classification, TSD permit obligations, corrective action
- EU EIA Directive (2011/92/EU as amended by 2014/52/EU): Annex I/II screening, scoping, BAT
- EU Industrial Emissions Directive (IED 2.0, Directive 2024/1785): permits, BAT conclusions
- EU REACH: SVHC candidate list obligations, authorization, restriction
- EU Environmental Liability Directive (2004/35/CE): operator liability, remediation obligations
- EU CS3D (2024/1760): environmental due diligence in value chains
- UK Environment Act 2021: biodiversity net gain (BNG), OEP, environmental targets
- UK Environmental Permitting Regulations 2016: permit types, transfers, registered exemptions
- UK Part IIA contaminated land: Class A/B liability, remediation notices, special sites
- Remediation standards: CERCLA/NCP ARARs, risk-based cleanup, brownfield programs
- M&A environmental due diligence: permit transferability, indemnification, PLL insurance
- Climate/sustainability disclosure: EU CSRD/Taxonomy, SEC climate rule, UK TCFD

**Does not:**

- Provide legal advice or replace qualified environmental counsel
- Substitute for a physical Phase I ESA conducted by a licensed Environmental Professional
- Generate actual compliance filings or regulatory submissions
- Apply exclusively to one jurisdiction — jurisdiction-agnostic with [JURISDICTION-SPECIFIC] markers

---

## Jurisdiction and Governing Law

This skill covers three primary jurisdictions, each with distinct regulatory architectures:

| Jurisdiction             | Primary Frameworks                                                                   | Regulator(s)                                                  |
| ------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| **US Federal**           | CERCLA, NEPA, CAA, CWA, RCRA                                                         | EPA, Army Corps of Engineers, CEQ                             |
| **US State**             | State voluntary cleanup programs (VCPs), state SIPs/NPDES delegation                 | State environmental agencies                                  |
| **EU**                   | EIA Directive, IED, REACH, ELD, CS3D, EU Taxonomy                                    | European Commission, ECHA, Member State competent authorities |
| **UK (England & Wales)** | Environment Act 2021, EPR 2016, Part IIA EPA 1990, UK EIA Regs SI 2017/571, UK REACH | Environment Agency, Natural England, HSE                      |

[JURISDICTION-SPECIFIC] US state programs differ materially. California, New York, and
New Jersey have more stringent VCPs and site cleanup standards. Texas, Arizona, and
Florida have real estate transfer statute requirements. Always verify state-specific
obligations for the target state.

[JURISDICTION-SPECIFIC] EU: Member States implement EIA, IED, and ELD through national
law. France, Germany, the Netherlands, and Belgium have additional national-level provisions.
Northern Ireland remains subject to EU REACH under the Windsor Framework.

[JURISDICTION-SPECIFIC] UK post-Brexit: UK EIA Regulations (SI 2017/571) retained in
English law but no longer must track EU Directive amendments. UK REACH diverges from
EU REACH and is evolving independently. _Finch v. Surrey_ (2024) extends EIA scope to
downstream combustion emissions from fossil fuel extraction projects.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's context, the workflow pauses and asks when:

- The regulatory framework depends on which jurisdiction's law applies
- The review purpose (transactional vs. operational) changes the scope and output format
- Site-specific facts are needed to determine permit requirements or liability exposure
- Risk tolerance or deal context is needed to classify severity correctly

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

### Step 1: Accept the Review Request

Accept the request in any of these formats:

- **Document**: Phase I/II ESA report, permit application, environmental audit, government
  correspondence, regulatory database search results
- **Site description**: Property address, coordinates, or description of facility and operations
- **Transaction materials**: Purchase agreement, due diligence checklist, seller disclosures,
  target company environmental records
- **Pasted text**: Regulatory correspondence, permit conditions, or compliance records

If no specific document or site is provided, proceed with context-gathering (Step 2).

### Step 2: Gather Review Context

**⟁ CLARIFY** — Before beginning, ask the user these questions. Present as structured options:

1. **Review purpose**: What type of environmental compliance review is needed?
   - Options: Pre-acquisition due diligence (M&A), Operational compliance audit,
     Permit review or transfer, Phase I/II ESA interpretation, CERCLA liability analysis,
     Remediation obligation assessment, Regulatory response/enforcement, Cross-border
     environmental screen (CS3D/CSRD), Other
   - _Why this matters_: Transaction due diligence requires a different output format (PASS/FLAG/FAIL)
     than an ongoing compliance audit (COMPLIANT/PARTIAL/NON-COMPLIANT).

2. **Jurisdiction(s)**: Which regulatory framework(s) apply?
   - Options: US Federal only, US Federal + specific state(s) [specify], EU Member State(s)
     [specify], UK (England & Wales), UK (Scotland), Cross-jurisdictional (specify),
     Let me assess based on site/transaction description
   - _Why this matters_: CERCLA, NEPA, Part IIA, and EIA Directive have very different
     liability structures, timelines, and defenses.

3. **Site context**: What is the nature of the property/facility?
   - Options: Undeveloped land, Industrial/manufacturing, Commercial/office, Mixed-use,
     Previously contaminated brownfield, Active TSD facility, Agricultural/forestry,
     Coastal/wetlands, Multiple properties
   - _Why this matters_: Industrial and former TSD sites trigger Phase II ESA and corrective
     action analysis; wetlands trigger CWA Section 404 jurisdiction post-Sackett.

4. **Role and side** (for transactional reviews):
   - Options: Acquiror/buyer, Seller/target, Lender/secured creditor, Lessor/landlord,
     Lessee/tenant, Regulator/permittee, Operator/facility owner, Other
   - _Why this matters_: CERCLA defenses available to acquirors differ from operator
     obligations; lender SCE analysis applies only to secured creditors.

5. **Environmental history**: Any known conditions?
   - Options: Known contamination (RECs present), Regulatory action/cleanup underway,
     Permits in place (specify type), No known history, Unknown
   - _Why this matters_: Known RECs require Phase II scope design; active cleanup triggers
     remediation obligation analysis; open regulatory actions require enforcement risk
     assessment.

If the user provides partial context, proceed with stated assumptions and note them
explicitly. Do not silently assume.

### Step 3: Gather Jurisdiction-Relevant Legal Authority

Use **legalcode-mcp** to build a working legal reference file for the review.

Search for:

- Applicable statutes and regulations (CERCLA, CAA, CWA, RCRA with current CFR citations;
  EU directives as implemented by the relevant Member State; UK retained law)
- Recent regulatory developments (PFAS designations, post-Sackett WOTUS updates, BNG
  implementation dates, IED 2.0 entry into force)
- Enforcement policy guidance (EPA brownfields comfort letters, Environment Agency
  enforcement position statements)
- State/Member State-specific requirements where jurisdiction-specific analysis is requested

Save results to `/tmp/legalcode-env-authority.md`. Reference throughout the analysis.

**Without legalcode-mcp:**

- Mark all statutory references with [VERIFY]
- Focus on structural compliance assessment and risk flagging rather than legal certainty
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`

### Step 4: Determine Review Scope

Based on the context gathered, determine which of the following modules to activate:

| Module                                    | Trigger Conditions                                                                          |
| ----------------------------------------- | ------------------------------------------------------------------------------------------- |
| **A — Phase I ESA Review**                | Phase I report provided; pre-acquisition review; AAI/BFPP defense assessment                |
| **B — Phase II ESA Scope/Findings**       | RECs identified in Phase I; contamination confirmed; remediation planning                   |
| **C — CERCLA Liability Analysis**         | Property acquisition; known/suspected contamination; cost recovery claim                    |
| **D — NEPA Compliance**                   | Federal nexus (federal permit, federal funding, federal land); major infrastructure project |
| **E — Clean Air Act**                     | Facility with air emissions; permit review; PSD/NSR pre-construction assessment             |
| **F — Clean Water Act**                   | Wetlands/waterways present; discharge operations; Section 404/402 permit                    |
| **G — RCRA**                              | Hazardous waste generation, storage, treatment, or disposal                                 |
| **H — EU EIA/IED**                        | EU project with significant environmental effects; industrial emissions facility            |
| **I — UK Environmental Regime**           | UK property, facility, or development; BNG; Part IIA contaminated land                      |
| **J — M&A Environmental Package**         | Transaction due diligence; combines A–G/H/I as applicable to target                         |
| **K — Climate/Sustainability Disclosure** | CSRD/CS3D/SEC climate rule obligations; EU Taxonomy alignment                               |

**⟁ CLARIFY** — For complex transactions covering multiple jurisdictions and modules,
confirm the scope before proceeding:

- "Based on your description, I'm planning to activate modules [A, B, C, J]. Does this
  match your needs, or should I add or remove any modules?"

### Step 5: Execute the Review

Execute each activated module. For each finding, apply the severity classification and
produce actionable output per the frameworks below.

---

## Module A — Phase I ESA Review (ASTM E1527-21)

### AAI Compliance Check

Verify the Phase I ESA was conducted in compliance with **All Appropriate Inquiries (AAI)**
under 40 C.F.R. Part 312, which requires use of ASTM E1527-21 (effective **February 13, 2023**):

**Required Components Checklist:**

| Component           | Requirement                                                                                                                                                                                       | Status                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| Records review      | Minimum radius searches per ASTM database type; 4 standard historical sources (aerial photos, fire insurance maps, city directories, topographic maps); title search for environmental liens/AULs | [ ] Present / [ ] Absent / [ ] Deficient |
| Site reconnaissance | On-site inspection by qualified EP; photographs of site boundaries and major features                                                                                                             | [ ] Present / [ ] Absent / [ ] Deficient |
| Interviews          | Current owner/occupants; former owners if accessible; local government officials if accessible; all attempts documented                                                                           | [ ] Present / [ ] Absent / [ ] Deficient |
| User Questionnaire  | Environmental liens/AULs; community knowledge; specialized experience; price differential analysis; obvious contamination                                                                         | [ ] Present / [ ] Absent / [ ] Deficient |
| EP qualifications   | Environmental Professional under 40 C.F.R. § 312.10                                                                                                                                               | [ ] Verified / [ ] Unverified            |
| Currency            | Report completed within 1 year of acquisition; components within 180 days                                                                                                                         | [ ] Current / [ ] Stale                  |

**Validity Assessment:**

- If the Phase I was completed under ASTM E1527-13 (pre-February 2023) and used for AAI
  after February 13, 2023 → **NON-COMPLIANT** — AAI defenses not established
- If more than 180 days have elapsed since site reconnaissance or searches →
  **PARTIAL** — update required before closing

### REC Classification Matrix

For each recognized environmental condition identified, classify per E1527-21:

| REC Type                  | Definition                                                                                                                                                     | Compliance Impact                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **REC**                   | Presence or likely presence of hazardous substances/petroleum due to confirmed release, conditions indicative of release, or material threat of future release | Triggers Phase II scope; BFPP defense cannot proceed without NCP compliance        |
| **Historical REC (HREC)** | Past release addressed to regulatory satisfaction under unrestricted use standards; no ongoing concern                                                         | No further action required if confirmed under unrestricted cleanup standards       |
| **Controlled REC (CREC)** | Release addressed with hazardous substances remaining in place under regulatory-approved controls (deed restrictions, AULs, institutional controls)            | Requires ongoing compliance with institutional controls; document in CREC register |
| **De Minimis Condition**  | Condition presenting no significant risk; not subject to regulatory concern                                                                                    | Photographic documentation required; confirm de minimis threshold met              |

**⟁ CLARIFY** — If RECs are present and the transaction is still pending:

- "RECs have been identified. Should I (A) recommend a Phase II scope to characterize
  the RECs, (B) assess whether BFPP defense prerequisites can be met without Phase II,
  or (C) both?"

### AAI Defenses Assessment

Verify prerequisites for each available CERCLA landowner defense:

**Bona Fide Prospective Purchaser (BFPP) — 42 U.S.C. § 9601(40):**

- [ ] Property acquired after January 11, 2002
- [ ] All disposals occurred before acquisition
- [ ] No affiliation with liable parties
- [ ] AAI completed (ASTM E1527-21 if post-February 13, 2023)
- [ ] Continuing obligations plan in place (see Module C)

**Innocent Landowner — 42 U.S.C. § 101(35)(B):**

- [ ] No RECs identified during AAI (if RECs exist, Innocent Landowner defense unavailable)
- [ ] No prior knowledge of contamination
- [ ] AAI completed and no RECs found
- [ ] Continuing obligations plan documented

---

## Module B — Phase II ESA / Remediation Assessment

### Phase II Scope Design

When Phase I identifies RECs, design Phase II scope per **ASTM E1903-19**:

| Investigation Element                                       | Applicability                                                                   | Priority                                                                |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Soil borings (surface + subsurface)                         | All RECs involving soil contamination                                           | Required                                                                |
| Groundwater monitoring wells                                | RECs with groundwater migration potential                                       | Required if below water table                                           |
| Vapor intrusion assessment (soil gas, sub-slab, indoor air) | RECs with VOC contamination; enclosed structures present                        | Required per EPA 2015 VI Guidance                                       |
| PFAS sampling                                               | Sites with fire suppression systems, military history, manufacturing, landfills | **Required post-July 2024** (PFOA/PFOS are CERCLA hazardous substances) |
| RCRA 8 metals + TAL metals                                  | Industrial/manufacturing RECs                                                   | Required                                                                |
| SVOC/PAH analysis                                           | Former UST, dry cleaning, manufactured gas plant                                | Required                                                                |

**PFAS [VERIFY — Current Threshold]:** As of **July 8, 2024**, PFOA and PFOS are
designated CERCLA hazardous substances (89 Fed. Reg. 24,070). Phase II scopes for any
site with industrial operations, military history, fire suppression systems (AFFF), or
proximity to airport/military installations must include PFAS analysis.

### Remediation Standards

| Standard Type           | Applicable Framework                                         | Cleanup Level                                                                                   |
| ----------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| CERCLA ARARs            | Must attain Applicable/Relevant and Appropriate Requirements | State/federal MCLs for groundwater; background for soil unless risk-based alternative available |
| Risk-based cleanup      | CERCLA/NCP where no ARAR                                     | Cancer risk: 10⁻⁶ to 10⁻⁴; Hazard index ≤1 for non-carcinogens                                  |
| State VCP standards     | State-specific (verify per state)                            | Risk-based, often with use-based standards (residential/commercial/industrial)                  |
| EU risk-based standards | [JURISDICTION-SPECIFIC] Member State implementation          | Varies; Netherlands NEN 5740; UK EA CLR 11 model                                                |
| UK Part IIA             | "Significant pollution linkage" test                         | Risk-based; Category 4 screening values                                                         |

---

## Module C — CERCLA Liability Analysis

### PRP Status Assessment

Identify and assess each potentially responsible party category:

**Current Owner/Operator** — 42 U.S.C. § 9607(a)(1):

- Strict, retroactive, joint and several liability
- Defenses: BFPP, Innocent Landowner, Contiguous Property Owner, Act of God/War, Third Party

**Past Owner/Operator at Time of Disposal** — 42 U.S.C. § 9607(a)(2):

- Liability attaches to period of ownership if disposal occurred during that period
- Key diligence: date of disposal events vs. dates of ownership

**Arranger Liability** — 42 U.S.C. § 9607(a)(3):

- _Burlington Northern & Santa Fe Ry. v. United States_, 556 U.S. 599 (2009): requires
  **intent to dispose** — mere knowledge spills may occur during sale of useful product
  is insufficient [VERIFY — current circuit interpretations]
- Common traps: selling used equipment/containers, off-spec materials, waste streams

**Transporter Liability** — 42 U.S.C. § 9607(a)(4):

- Only transporters who **selected** the disposal site

### Lender Secured Creditor Exemption (SCE)

42 U.S.C. § 9601(20)(E)-(F); Asset Conservation, Lender Liability, and Deposit Insurance
Protection Act of 1996:

- Protects lenders holding "indicia of ownership" primarily to protect a security interest
- Does **not** protect lenders who "participate in the management" of the facility
- Post-foreclosure: may sell, liquidate, wind up operations, or conduct response actions
  without losing SCE, provided not seeking long-term profit from the property

**⟁ CLARIFY** — For lender clients: "Are you conducting a pre-loan environmental review
or have you already taken security/foreclosure? This determines which SCE elements I
should prioritize."

### Continuing Obligations (BFPP/Innocent Landowner)

Post-closing continuing obligations that must be maintained to preserve defenses:

| Obligation             | Requirement                                                                                                               |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| No new disposal        | Must not dispose of any hazardous substance at the property                                                               |
| Reasonable steps       | Take reasonable steps regarding existing releases (stop continuing releases, prevent exposure, cooperate with regulators) |
| Institutional controls | Monitor and maintain all AULs, deed restrictions, and engineering controls                                                |
| Regulatory cooperation | Provide site access, respond to information requests, comply with land use restrictions                                   |
| Environmental liens    | Monitor for new federal/state environmental liens on the property                                                         |

---

## Module D — NEPA Compliance

### NEPA Applicability Threshold

NEPA applies to **major federal actions significantly affecting the quality of the human
environment** (42 U.S.C. § 4332(C)). Determine federal nexus:

- Federal permits required (Section 404, Title V, Section 402)?
- Federal funding involved?
- Federal agency with approval authority?
- Federal land involved?

If no federal nexus → NEPA does not apply. State-level EIA equivalents may still apply.

### NEPA Analysis Level

| Level                                    | Trigger                                                                        | Requirements                                                                     |
| ---------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| **Categorical Exclusion (CE)**           | Category of action with no significant effects; no extraordinary circumstances | No EA or EIS required; document CE basis                                         |
| **Environmental Assessment (EA)**        | Action not clearly insignificant; not categorically excluded                   | Analyze significance; issue FONSI or elevate to EIS                              |
| **Environmental Impact Statement (EIS)** | Significant effects on human environment                                       | NOI in Federal Register → scoping → Draft EIS → public comment → Final EIS → ROD |

**Post-February 3, 2025 Framework Note:** A federal court vacated the CEQ Phase 2 Rule
(Biden administration NEPA modernization) on February 3, 2025, holding NEPA does not
authorize CEQ to issue binding regulations. Practitioners must now rely on agency-specific
NEPA regulations. [VERIFY — current CEQ/agency-specific procedural requirements]

### EIS/EA Content Requirements

For EIS (40 C.F.R. Part 1502, current agency procedures):

- Statement of purpose and need
- Alternatives analysis (including no-action alternative)
- Affected environment description
- Environmental consequences of each alternative
- Cumulative impacts analysis (indirect and cumulative effects)
- Mitigation measures

---

## Module E — Clean Air Act Compliance

### Permit Type Determination

| Permit Type                  | Applicability                                                                                                                                  | Key Requirements                                                                                |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Title V Operating Permit** | Major sources (100 TPY criteria pollutants; 10 TPY single HAP; 25 TPY multiple HAPs); sources subject to NSPS, NESHAP, or Acid Rain provisions | Comprehensive permit covering all applicable requirements; public participation; 5-year renewal |
| **PSD Permit**               | New major source or major modification in NAAQS-attainment area                                                                                | BACT analysis; ambient air quality analysis; Class I area review if within 100km                |
| **Nonattainment NSR Permit** | New major source or major modification in NAAQS-nonattainment area                                                                             | LAER; emission offsets (>1:1 ratio); SIP consistency                                            |
| **Minor Source Permit**      | Below major source thresholds; state-specific                                                                                                  | State-specific requirements; watch "synthetic minor" permit conditions                          |

**Synthetic Minor Permits — RED Flag:** Permits with legally-enforceable emission caps
to avoid major source status require strict operational compliance. Violations of synthetic
minor permit limits can trigger major source reclassification, retroactive NSR review
obligations, and significant enforcement exposure.

### GHG Reporting — 40 C.F.R. Part 98

Mandatory threshold: **25,000 metric tons CO2e/year** from stationary fuel combustion.

- All Subparts applicable to the facility's operations must be checked
- Subpart W (petroleum and natural gas): EPA May 2024 final rule expanded reporting
  scope for certain facilities [VERIFY — current effective date and thresholds]

### Change of Control — CAA Obligations

- Title V permits require **notice of modification** for change of ownership; permits do
  not automatically transfer to new entity
- New owner must apply for permit revision or new permit before operating as the permittee

---

## Module F — Clean Water Act Compliance

### Post-Sackett WOTUS Jurisdiction Analysis

_Sackett v. Environmental Protection Agency_, 598 U.S. \_\_\_ (2023) (May 25, 2023):
Adopted the **continuous surface connection test** — CWA jurisdiction extends only to
wetlands with a continuous surface connection to relatively permanent waters that are
WOTUS in their own right. "Significant nexus" test abandoned. [VERIFY — any subsequent
EPA rulemaking or circuit court decisions]

EPA/Army Corps conforming rule: September 8, 2023 — revised WOTUS definition to require
continuous surface connection for "adjacent" wetlands.

**Jurisdictional Determination Required Where:**

- Wetlands, streams, or water bodies are present on or adjacent to the site
- Site contains intermittent or ephemeral streams (may no longer be WOTUS post-Sackett)
- Wetlands are separated from WOTUS by upland barriers

**State Protections:** Many states have independent wetland protection laws that extend
beyond federal CWA jurisdiction. [JURISDICTION-SPECIFIC] Verify applicable state program.

### Permit Requirements

| Permit                        | Regulator              | Trigger                                                           | Key Requirement                                                                      |
| ----------------------------- | ---------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Section 404 Dredge/Fill**   | Army Corps + EPA       | Discharge of dredged/fill material into WOTUS                     | No practicable alternative with less environmental impact; Section 401 certification |
| **Section 402 NPDES**         | EPA or delegated state | Point source discharge into WOTUS                                 | Effluent limitations; monitoring; reporting                                          |
| **Section 401 Certification** | State/tribal agency    | Any federal permit for activity with potential discharge to WOTUS | State may grant, condition, or deny (up to 1 year to act)                            |

### Change of Control — CWA Obligations

NPDES permits are not automatically transferred. New permittee must file a transfer request
or new permit application before taking over discharging operations.

---

## Module G — RCRA Compliance

### Generator Status Classification

Determine generator category based on **monthly** generation of hazardous waste:

| Category                                 | Monthly Non-Acute HW | Monthly Acute HW       | Accumulation Time             | Key Obligations                                                                  |
| ---------------------------------------- | -------------------- | ---------------------- | ----------------------------- | -------------------------------------------------------------------------------- |
| **VSQG (Very Small Quantity Generator)** | < 100 kg             | < 1 kg                 | No time limit                 | Send to approved facility; no manifest required within certain limits            |
| **SQG (Small Quantity Generator)**       | 100–1,000 kg         | 1 kg–1 kg accumulation | 180 days (270 if TSD >200 mi) | Emergency coordinator; personnel training; permitted storage area                |
| **LQG (Large Quantity Generator)**       | > 1,000 kg           | > 1 kg                 | 90 days                       | Full RCRA training program; emergency contingency plan; manifest; LDR compliance |

RCRA Generator category must be assessed **monthly** — a single month exceeding
thresholds elevates status for that entire month. Episodic generation rules apply
(VSQGs/SQGs may generate above thresholds during episodic events without permanent
reclassification; specific procedures required).

### TSD Facility Due Diligence

Acquiring a Treatment, Storage, or Disposal (TSD) facility is a high-risk transaction:

- TSD permits require formal modification for **change of ownership** under 40 C.F.R.
  Part 270, Subpart D — regulatory approval must precede or accompany closing
- **Corrective action obligations** attach to the facility (not just the permit): all
  solid waste management units (SWMUs) must be investigated and remediated
- **Financial assurance** obligations continue for the new owner: closure, post-closure,
  and corrective action financial assurance instruments must be updated
- TSD corrective action can be open-ended and extremely costly; scope all SWMUs in Phase II

---

## Module H — EU Environmental Compliance (EIA / IED / ELD / REACH)

### EU EIA Directive — 2011/92/EU as amended by 2014/52/EU

**Annex I Projects** (mandatory EIA): oil refineries, nuclear power stations, large
infrastructure projects, waste disposal facilities above specified thresholds. EIA
always required.

**Annex II Projects** (screening required): smaller versions of Annex I; projects in
sensitive areas; other described categories. Competent authority screens based on
Annex III criteria.

**Scoping** (2014/52/EU amendment): Binding scoping opinion from competent authority;
sets scope and detail required in the environmental statement.

**Public Participation — Article 6:** Reasonable time allocation; public and authorities
must be consulted; decision must be published with main reasons and conditions.

**Member State Implementation:** [JURISDICTION-SPECIFIC] Consult the applicable national
implementing regulation. Germany: UVPG; France: Code de l'Environnement; Netherlands:
Besluit milieueffectrapportage. Thresholds and screening criteria vary by Member State.

### EU Industrial Emissions Directive — IED 2.0 (Directive 2024/1785)

Entered into force **August 4, 2024**. Covers >50,000 of the EU's largest industrial
installations.

**BAT Conclusions** are legally binding for permit conditions. Operators must:

- Hold integrated permits from national competent authority
- Comply with permit conditions based on BAT conclusions
- Permit to be reviewed/updated when new BAT conclusions published

**Change of Operator:** [JURISDICTION-SPECIFIC] Member States require operators to notify
the competent authority. Permits do not automatically transfer — new operator must apply
for permit transfer before assuming operations.

### EU REACH — EC No 1907/2006

**SVHC Candidate List Obligations** (triggered at 0.1% w/w in articles):

- Communicate safe use information to customers within 45 days of customer request
- Notify ECHA via SCIP database
- As of early 2026: **253+ substances** on the Candidate List [VERIFY current count at
  ECHA website]

**Authorization (Annex XIV):** Substances with sunset dates require authorization to
continue use. Verify whether any substances used at target facility are subject to
authorization obligations.

**UK REACH Divergence:** [JURISDICTION-SPECIFIC] UK REACH (administered by HSE) applies
in Great Britain; EU REACH continues in Northern Ireland. Companies with operations in
both regions face dual compliance obligations. UK and EU REACH are diverging increasingly.

### EU Environmental Liability Directive — 2004/35/CE

**Annex III Operators (Strict Liability):** Dangerous activities (industrial, waste
management, transport of dangerous goods) — liability without fault.

**Non-Annex III Activities (Fault-Based):** Damage to protected species/habitats —
requires fault or negligence.

**Remediation Obligations:**

- Primary remediation: restore damaged resources to baseline condition
- Complementary remediation: geographically linked off-site actions where primary
  remediation insufficient
- Compensatory remediation: addresses interim loss of natural resources and services

### EU CS3D — Directive 2024/1760

In-scope companies must conduct environmental due diligence in their **value chains**,
including identifying, preventing, and remediating adverse environmental impacts.

**Thresholds (post-Omnibus I, December 2025):**

| Phase                           | Deadline  | Employees | Turnover            |
| ------------------------------- | --------- | --------- | ------------------- |
| Phase 1 (largest EU companies)  | July 2027 | >5,000    | >€1,500M worldwide  |
| Phase 2 (mid-size EU companies) | July 2028 | >3,000    | >€900M worldwide    |
| Phase 3 (smaller EU + non-EU)   | July 2029 | >1,000    | >€450M worldwide/EU |

Covered environmental issues: waste handling, biodiversity, marine pollution,
international environmental instrument violations (see CS3D Annex).

---

## Module I — UK Environmental Compliance

### UK Environment Act 2021 — Biodiversity Net Gain (BNG)

**Mandatory BNG Requirements** (Schedule 14 Environment Act 2021 / Schedule 7A TCPA 1990):

| Development Type                                       | Mandatory BNG Date    |
| ------------------------------------------------------ | --------------------- |
| Large TCPA developments                                | **February 12, 2024** |
| Small sites                                            | **April 2, 2024**     |
| Nationally Significant Infrastructure Projects (NSIPs) | Expected May 2026     |

**Core requirements:**

- Minimum **10% net biodiversity gain** quantified using statutory biodiversity metric
- Habitat enhancements must last minimum **30 years**
- Biodiversity Gain Plan must be submitted and approved before development commencement
- Delivery: on-site, off-site biodiversity units, or statutory biodiversity credits from
  government (last resort)

**Common compliance failures:**

- Incorrect pre-development biodiversity baseline calculation
- Off-site units purchased without checking proximity and habitat type requirements
- Exemptions misapplied (narrow: householder applications, permitted development, <25m² sites)

### UK Environmental Permitting Regulations 2016 (SI 2016/1154)

**Permit Types:** Environmental permit (standard rules or bespoke); registered exemption;
flood risk activity permit.

**Change of Operator — Critical Compliance Point:**

- Permits are **not automatically transferred** on change of ownership or control
- New operator must apply for a permit transfer to the Environment Agency **before**
  assuming operations
- Operating without a transfer constitutes an unlicensed operation — strict liability

**Permit Consolidation:** EPR 2016 consolidates waste operations, water discharge,
groundwater activities, IED installations, radioactive substances, and flood risk.
Check all applicable permit categories for the target facility.

### UK Contaminated Land — Part IIA Environmental Protection Act 1990

**Identification:** Local authorities must inspect and identify contaminated land
presenting an unacceptable risk to human health or the environment.

**Liability (Remediation Notice):**

- **Class A persons** (primary): Persons who "caused or knowingly permitted" the
  contamination — targeted first
- **Class B persons** (fallback): Current owner or occupier where no Class A person
  can be found

**Knowing Permitter:** Knowledge of contamination combined with failure to act creates
knowing permitter liability even without physical involvement in causing contamination.

**Exclusion Tests:** Statutory guidance provides 6 exclusion tests to determine
liability allocation among multiple Class A persons. [VERIFY current statutory guidance]

**Special Sites:** Regulated by the Environment Agency rather than local authorities;
typically for sites with significant groundwater contamination, radioactive substances,
or other complex contamination scenarios.

### UK EIA — SI 2017/571 (Post-Brexit)

Retained EU law post-Brexit. Key 2024 development:

_Finch v. Surrey County Council_ [2024] UKSC: EIAs for fossil fuel extraction projects
must assess **downstream combustion emissions** if they are likely direct or indirect
environmental effects of the project and are readily quantifiable. Applies to any
project whose downstream use involves GHG emissions that are "readily quantifiable."

---

## Module J — M&A Environmental Due Diligence Package

### Pre-LOI Environmental Screen

- Run EPA Envirofacts, ECHO, and SEMS/CERCLIS searches for target properties
- Check EPA Superfund site listings (NPL, proposed NPL, archived)
- Review SEC and annual report disclosures for material environmental liabilities
- Preliminary PFAS screening based on site history and operations
- Review target's environmental insurance policies

### Due Diligence Checklist

**Phase I ESA:**

- [ ] Phase I ESA (ASTM E1527-21) for all real property — update if >1 year old
- [ ] Components >180 days old must be updated before closing
- [ ] PFAS screen incorporated (required for sites with industrial use, AFFF, military history)
- [ ] All RECs, CRECs, and HRECs identified and classified

**Phase II ESA (where RECs exist):**

- [ ] Scope designed to characterize all RECs
- [ ] PFAS sampling included where site history warrants
- [ ] Vapor intrusion assessment for VOC-related RECs with structures
- [ ] Results reviewed for cost estimation and risk-to-deal assessment

**Permit Review:**

- [ ] All environmental permits identified (CAA Title V, NPDES, Section 404, RCRA TSD,
      state air/water, UK EPR, EU IED, EU/UK REACH)
- [ ] Transferability of each permit assessed (which require regulatory pre-approval?)
- [ ] Timeline for permit transfers relative to closing date confirmed
- [ ] Any pending renewals, modifications, or compliance schedules identified
- [ ] Financial assurance instruments assessed (RCRA, closure bonds)

**Government Correspondence:**

- [ ] NOVs (Notices of Violation) — past 5 years minimum
- [ ] Consent orders, administrative orders, or judicial decrees
- [ ] Inspection reports and any open deficiency items
- [ ] Correspondence with EPA/state agency/Environment Agency
- [ ] PRP notifications (CERCLA Section 104(e) information requests, special notices)

**Environmental Insurance:**

- [ ] Review all existing PLL (pollution legal liability) and environmental impairment
      liability policies
- [ ] Assess whether legacy policies cover known conditions
- [ ] Evaluate need for new PLL coverage or Reps & Warranties insurance with
      environmental carve-out

### Severity Classification for M&A

| Classification | Definition                                                                                                                                      | Transaction Impact                                                           |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **PASS**       | No material environmental issues; permits current; Phase I clean or CRECs manageable                                                            | Proceed without condition                                                    |
| **FLAG**       | Environmental issues present but quantifiable and manageable; open permits, pending NOVs, CRECs with known costs                                | Proceed with indemnification, price adjustment, or escrow                    |
| **FAIL**       | Material unquantified contamination; open CERCLA liability; TSD corrective action; PFAS exposure uncharacterized; permits cannot be transferred | Do not proceed without Phase II + cost estimation; consider deal termination |

### Environmental Representations and Warranties

Standard environmental reps should cover (negotiate carve-outs for known issues):

- Compliance with all Environmental Laws
- No pending or threatened environmental claims, suits, administrative orders, or investigations
- No known releases of hazardous substances at any owned/leased property
- No underground storage tanks not disclosed
- All required environmental permits held and in good standing
- No off-site disposal at sites that are now Superfund sites
- No CERCLA Section 104(e) information requests received
- No asbestos, lead paint, or PCBs in violation of applicable law
- **No PFAS contamination at owned/operated properties** (now standard post-July 2024)
- No open RCRA corrective action or financial assurance deficiencies

### Transaction Structuring for Environmental Risk

| Structure                         | Environmental Benefit                                                          | Risk                                                                           |
| --------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| **Asset purchase**                | Generally avoids successor liability for pre-existing contamination            | Exceptions: de facto merger, continuation of enterprise, fraudulent conveyance |
| **Stock purchase**                | Target retains all permits without transfer                                    | Buyer inherits all target's environmental liabilities                          |
| **Environmental indemnification** | Allocates known/unknown liability to seller                                    | Survival period, cap, and creditworthiness of seller matter                    |
| **PLL insurance**                 | Transfers residual risk to insurer; covers pre-existing and third-party claims | Premium; policy exclusions; claims-made vs. occurrence form                    |
| **Price adjustment/escrow**       | Quantified liability held back at closing                                      | Quantification accuracy; escrow period                                         |

---

## Operational Compliance Program (Post-Acquisition)

**Immediate (Day 0–30):**

- Confirm all environmental permits are current and updated for new entity
- Verify RCRA manifest system, emergency coordinator designation, and training records
- Confirm NPDES/discharge monitoring reports are current
- Check GHG reporting obligations and reporting cycle

**Short-Term (30–90 Days):**

- Complete inventory of all RECs/CRECs; establish institutional control monitoring program
- Transfer all permit applications filed and acknowledged
- Conduct introductory environmental compliance training for relevant personnel
- Review environmental management system (ISO 14001 if applicable)

**Ongoing:**

- Annual internal environmental compliance audit
- Monthly hazardous waste generator status assessment
- Monitoring of PFAS regulatory developments (additional hazardous substance designations
  expected from EPA)
- Track BNG monitoring reports (UK: 5-year mandatory monitoring check)
- CS3D/CSRD annual reporting where in-scope

---

## Severity / Status Classification Framework

### Compliance Severity Levels

| Level                | Classification                       | Definition                                                                                                           | Required Action                                                                    |
| -------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| ✅ **COMPLIANT**     | No deficiency                        | Full compliance with applicable legal requirements; permits current; no known violations                             | Document compliance; maintain records                                              |
| ⚠️ **PARTIAL**       | Deficiency present                   | Technical deficiency, procedural gap, or missing documentation that can be remediated without regulatory enforcement | Remediation action with defined timeline; document corrective measures             |
| 🔴 **NON-COMPLIANT** | Material violation                   | Material violation of permit condition, statutory requirement, or regulatory standard; enforcement risk              | Immediate corrective action; counsel notification; consider voluntary disclosure   |
| 🚨 **CRITICAL**      | Imminent enforcement or deal-breaker | Active enforcement action; unquantified contamination; permit cannot be transferred; criminal referral risk          | Halt or condition transaction; engage specialist environmental counsel immediately |

### Self-Interrogation for CRITICAL Findings

For any finding classified as CRITICAL, apply this 3-pass self-interrogation before delivery:

**Pass 1 — Legal Chain Integrity:**

- Does the enforcement risk follow logically from the cited statutory provision or permit condition?
- Would a regulator actually pursue enforcement on this basis given current enforcement priorities?
- Is there a compliance defense, exemption, or safe harbor the analysis has not considered?

**Pass 2 — Completeness:**

- Have all applicable statutes, regulations, and guidance documents been considered?
- Have relevant state/Member State requirements been checked (not just federal/EU)?
- Is the PFAS exposure assessment up to date (post-July 2024 CERCLA designation)?

**Pass 3 — Challenge:**

- What is the strongest argument that this finding is PARTIAL rather than CRITICAL?
- What mitigation steps, if taken immediately, would reduce the severity classification?
- Is the CRITICAL classification proportionate to the exposure, or is it creating unnecessary
  deal friction for a manageable issue?

If any pass reveals a weakness, revise before delivery. Mark the audit trail:
`self_interrogation: PASS` or `self_interrogation: REVISED`.

---

## Prioritization Framework

### Environmental Risk Priority Tiers

**Tier 1 — Critical / Immediate Action:**

- CERCLA PRP status with no available defense
- PFAS contamination in groundwater above drinking water MCLs adjacent to receptors
- Active RCRA corrective action or EPA enforcement action
- Phase II results showing contamination exceeding risk-based levels with no remediation plan
- Permits that cannot transfer (TSD, complex IED permits) without regulatory approval that
  cannot be obtained before closing
- UK Part IIA Special Site designation pending

**Tier 2 — High / Near-Term Action Required:**

- Phase I RECs requiring Phase II investigation not yet completed
- CRECs with institutional controls requiring ongoing compliance monitoring
- NOVs or compliance schedules with near-term milestones
- RCRA generator status potentially mis-classified (LQG operating as SQG)
- Title V permit renewal overdue or pending modification
- BNG compliance gap for in-progress or recently completed development
- SVHC Candidate List substances in articles without SCIP notification

**Tier 3 — Medium / Managed:**

- HRECs (historical RECs addressed to unrestricted use standards) — document and close
- Minor permit administrative deficiencies with straightforward correction
- GHG reporting thresholds to be monitored as operations change
- CS3D/CSRD compliance program under development (company approaching but not yet at threshold)
- Post-Sackett WOTUS jurisdictional uncertainty for isolated wetlands — state law screen recommended

**Tier 4 — Low / Monitor:**

- De minimis conditions properly documented in Phase I
- REACH substances below 0.1% w/w threshold
- NEPA categorical exclusions properly documented
- State VCP closure obtained (note: does not extinguish CERCLA liability — monitor for
  EPA interest)

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                                                                 | Fail Action                                                |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute (with USC/CFR citation), regulation, case, or established regulatory guidance                             | Add citation or mark "[UNVERIFIED — counsel to confirm]"   |
| **Format**     | Citations follow consistent, recognizable format (42 U.S.C. § 9601; 40 C.F.R. Part 300; 2011/92/EU; SI 2016/1154)                                    | Fix format                                                 |
| **Currency**   | Regulatory thresholds, SVHC candidate list entries, PFAS designations, and permit requirements verified as current                                   | Flag "[CHECK CURRENCY — may have been amended or updated]" |
| **Domain**     | Analysis stays within the applicable regulatory framework. No assumptions from other jurisdictions unless cross-border analysis explicitly requested | Remove or flag jurisdictional bleed                        |
| **Confidence** | Uncertainty explicitly stated, not hidden. If regulatory interpretation is contested or in flux (post-CEQ vacatur, post-Sackett), say so             | Add confidence qualifier                                   |

### Confidence Scoring

For each material finding, assign a confidence level:

| Level        | Range     | Meaning                                                                                   | Action                                                                 |
| ------------ | --------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, clear statutory requirement, no ambiguity                                    | State with confidence                                                  |
| **High**     | 0.80–0.94 | Strong authority, minor regulatory interpretation questions                               | State with brief caveat                                                |
| **Probable** | 0.60–0.79 | Good regulatory basis but contested or evolving (e.g., post-Sackett WOTUS, post-CEQ NEPA) | State with explicit reasoning and contra-indicators                    |
| **Possible** | 0.40–0.59 | Genuinely uncertain; competing regulatory interpretations                                 | Flag for environmental counsel review with both sides                  |
| **Unlikely** | 0.0–0.39  | Weak regulatory basis, speculative                                                        | Do not assert; flag as "[UNCERTAIN — environmental counsel to advise]" |

---

## Glass Box Audit Trail

Every environmental compliance review output MUST include a Glass Box audit section:

```yaml
glass_box:
  review_type: "[Phase I Review / M&A Due Diligence / Compliance Audit / CERCLA Analysis / Other]"
  site_or_transaction: "[Site name/address or transaction identifier]"
  jurisdiction: "[US Federal / State(s) / EU Member State(s) / UK / Multi-jurisdiction]"
  modules_activated: "[List of modules: A, B, C, D, E, F, G, H, I, J, K]"
  review_purpose: "[Pre-acquisition / Operational / Permit Transfer / Regulatory Response]"
  phase_i_standard: "[ASTM E1527-21 / E1527-13 (pre-Feb 2023 — note compliance gap) / N/A]"
  pfas_in_scope: "[Yes / No / Unknown]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[/tmp/legalcode-env-authority.md or 'Not created']"
  statutes_consulted:
    - "[42 U.S.C. § 9601 et seq. (CERCLA) — VERIFIED or UNVERIFIED]"
    - "[40 C.F.R. Part 312 (AAI) — VERIFIED or UNVERIFIED]"
    - "[Add additional statutes as reviewed]"
  recs_identified: "[number of RECs / number of CRECs / number of HRECs]"
  findings_by_severity:
    critical: "[number]"
    non_compliant: "[number]"
    partial: "[number]"
    compliant: "[number]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL items)"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Physical inspection not performed — Phase I review is desk-based only]"
    - "[State-specific requirements not assessed — verify for applicable state]"
    - "[Add any scope limitations]"
  reviewer: "AI-assisted — requires review by qualified environmental lawyer and/or licensed Environmental Professional"
```

---

## Anti-Patterns

Environmental compliance review failures that recur in practice. Do not repeat them.

1. **Treating a pre-February 2023 Phase I as AAI-compliant** — ASTM E1527-13-based Phase
   I ESAs do not satisfy 40 C.F.R. Part 312 AAI requirements for acquisitions after
   February 13, 2023. BFPP and Innocent Landowner defenses are not established.

2. **Assuming Innocent Landowner defense is available when RECs are identified** — If
   Phase I identifies a REC, the Innocent Landowner defense (which requires no prior
   knowledge) is unavailable. Only the BFPP defense is available, and it requires
   additional prerequisites including continuing obligations.

3. **Skipping PFAS in Phase II scope** — PFOA and PFOS became CERCLA hazardous
   substances on July 8, 2024. Any Phase II ESA conducted after that date for sites
   with industrial operations, fire suppression systems, military history, or nearby
   PFAS-impacted groundwater that omits PFAS analysis creates a material gap in
   site characterization.

4. **Applying Burlington Northern intent standard without circuit analysis** — The intent
   requirement for arranger liability is nuanced and circuit-dependent. Do not assert
   that a party has or does not have arranger liability without analyzing the specific
   facts under the Burlington Northern standard and the applicable circuit's interpretation.

5. **Relying on state VCP closure to extinguish CERCLA liability** — State VCP closure
   (state no-further-action letter) does not extinguish federal CERCLA liability absent
   EPA concurrence or specific statutory protection. PRP status under CERCLA can still
   be asserted by EPA or private parties after state VCP closure.

6. **Post-Sackett wetlands analysis without state-law check** — After Sackett, many
   isolated wetlands fell outside federal CWA jurisdiction. But state wetland protection
   laws may still apply and are often more protective. A wetland that is no longer WOTUS
   may still require state permits.

7. **Failing to assess permit transferability before signing** — Many environmental
   permits (RCRA TSD, Title V, NPDES, UK EPR, EU IED) require regulatory approval to
   transfer and cannot be assigned by contract alone. Closing before permit transfer
   approval creates unlicensed operations. Assess all permits during due diligence and
   build regulatory timelines into the transaction schedule.

8. **Generator status snapshot rather than monthly assessment** — RCRA hazardous waste
   generator status must be assessed monthly. Using an annual snap calculation based on
   average generation rates can misclassify a facility that occasionally spikes above LQG
   thresholds, creating manifesting and storage-time violations.

9. **Assuming NEPA categorical exclusions apply without extraordinary circumstances review**
   — A CE is not self-executing. The agency must still document the CE basis and
   determine that no extraordinary circumstances exist. Extraordinary circumstances
   (threatened species, historic properties, wetlands, CERCLA sites) can elevate a
   CE to an EA.

10. **Not obtaining updated WOTUS jurisdictional determination before Section 404 work**
    — The post-Sackett conforming rule changed jurisdictional boundaries significantly.
    A prior approved JD may no longer reflect current jurisdiction. Commission a new
    jurisdictional determination before commencing any dredge/fill activity.

11. **Treating BNG as a planning consent condition rather than a statutory pre-commencement
    obligation** — BNG is a **statutory pre-commencement requirement**, not merely a
    planning condition that can be discharged post-completion. Development commenced
    before a Biodiversity Gain Plan is approved is unauthorized development.

12. **Missing UK EPR permit transfer requirement at closing** — UK environmental permits
    are not automatically transferred on a change of control or asset sale. Operating
    the facility without a transferred permit from day one of ownership constitutes a
    regulatory offence under EPR 2016. Apply for permit transfer in parallel with
    transaction negotiations.

13. **EU IED BAT conclusion review gap** — When BAT conclusions are updated (via a new
    Implementing Decision), permit conditions must be reviewed and updated within 4 years
    (under IED 2.0). Facilities operating under outdated BAT conclusions may be
    non-compliant even if their permit was recently renewed.

14. **REACH SVHC obligation triggered but not actioned** — The 0.1% w/w threshold in
    articles triggers immediate obligations (communicate, notify SCIP). Companies
    manufacturing or importing products containing SVHCs above threshold who have not
    completed SCIP notifications are in violation of REACH obligations even if the
    substance was only recently added to the Candidate List (45-day notification window).

15. **Environmental indemnification with insufficient survival period** — Environmental
    claims can surface years or decades after contamination occurs. An indemnification
    provision with a 2- or 3-year survival period may expire before CERCLA, Part IIA,
    or EU ELD claims materialize. Negotiate survival periods tied to the applicable
    statute of limitations, not a fixed term.

16. **Ignoring climate-related regulatory risk in regulatory authority analysis** — Post-Finch
    v. Surrey (UK) and increasing climate integration in EIA practice globally, regulatory
    risk assessments must consider whether downstream GHG emissions from the project or
    facility could be quantified and whether failure to assess them in an EIA creates
    grounds for challenge.

17. **Relying on seller environmental reps without independent investigation** — In
    transactions involving potentially contaminated properties, standard reps and
    warranties insurance typically **excludes** known environmental conditions and may
    exclude environmental liabilities generally. Independent Phase I/II ESA and permit
    review is the primary protection — reps and warranties are supplementary, not
    substitutes.

18. **Failing to account for CS3D environmental due diligence in supply chain contracts**
    — In-scope companies must address adverse environmental impacts across their value
    chains. Supply and procurement contracts with key suppliers should include contractual
    rights of audit, representations regarding environmental compliance, and termination
    rights for material environmental violations. Failing to build these rights into
    contracts before CS3D applicability dates creates implementation gaps.

---

## Writing Standards

Apply plain-language discipline to all environmental compliance review output:

**For executive summaries and findings:**

- Plain language accessible to a CFO or board member, not only environmental counsel
- Lead with the risk, not the regulatory citation: "The site has uncharacterized PFAS
  contamination near a municipal drinking water supply" — not "Potential CERCLA §107(a)
  arranger liability exposure due to PFOA/PFOS presence"
- Active voice: "The permit expired in 2023 and has not been renewed" — not "The permit
  has been allowed to lapse"
- Specific numbers: "The Phase I identified 3 RECs and 1 CREC" — not "Several RECs were
  identified"

**For legal analysis and recommendations:**

- Same plain-language standards
- Include regulatory citation for each legal claim
- Use Confidence Scoring qualifiers where appropriate
- Distinguish between established requirements and contested interpretations

**Quality gates before delivery:**

1. Can a non-environmental-lawyer business stakeholder understand the Executive Summary?
2. Is every finding backed by a specific statutory, regulatory, or guidance citation (or
   marked [VERIFY])?
3. Is the severity classification (COMPLIANT/PARTIAL/NON-COMPLIANT/CRITICAL) justified
   by the evidence and the applicable legal standard?
4. Is the Confidence Score appropriate for the regulatory certainty of the finding?
5. Are all PFAS, WOTUS, BNG, and other recently-changed requirements current as of 2025?

---

## External Tool Integration

This skill is designed to work with **legalcode-mcp** as its primary legal research tool.

**With legalcode-mcp connected (preferred):**

- Search for current CERCLA, CAA, CWA, RCRA, and state environmental regulatory texts
- Verify Phase I ESA standards and AAI regulatory requirements
- Research current PFAS CERCLA designation status and enforceable MCLs
- Confirm EU EIA/IED BAT conclusion status for relevant industrial sectors
- Verify REACH SVHC Candidate List current count and relevant substances
- Check UK Part IIA statutory guidance and EPR 2016 current status
- Search for recent EPA enforcement guidance, brownfields policies, and compliance orders
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all statutory thresholds, regulatory citations, and case references with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Provide structural compliance assessment and risk framework; note that regulatory
  thresholds and citation currency require independent verification
- Do not create the local authority reference file

---

## Output Format Template

Structure the final deliverable as:

```markdown
## Environmental Compliance Review

**Site / Transaction**: [identifier]
**Review Type**: [Phase I ESA Review / M&A Due Diligence / Compliance Audit / CERCLA Analysis]
**Jurisdiction(s)**: [US Federal + State / EU / UK / Multi-jurisdiction]
**Modules Activated**: [A, B, C, D, E, F, G, H, I, J, K]
**Date of Review**: [date]
**Basis**: [Documents reviewed / Phase I report / Regulatory records / Description only]

---

## Executive Summary

[Top 3–5 findings with severity flags (CRITICAL/NON-COMPLIANT/PARTIAL) and one-line
summaries. Lead with the most material risk to the transaction or operations.]

---

## Key Risk Indicators

| Finding     | Severity         | Jurisdiction | Confidence | Priority Tier |
| ----------- | ---------------- | ------------ | ---------- | ------------- |
| [Finding 1] | 🚨 CRITICAL      | US Federal   | High       | Tier 1        |
| [Finding 2] | 🔴 NON-COMPLIANT | UK           | Probable   | Tier 2        |
| [Finding 3] | ⚠️ PARTIAL       | EU           | High       | Tier 2        |
| [Finding 4] | ✅ COMPLIANT     | US           | Definite   | N/A           |

---

## Phase I / Phase II ESA Assessment

[If Module A/B activated]

### REC Register

| #   | REC Type        | Location      | Chemicals of Concern | Severity | Action Required |
| --- | --------------- | ------------- | -------------------- | -------- | --------------- |
| 1   | [REC/CREC/HREC] | [description] | [chemicals]          | [level]  | [action]        |

### AAI Compliance

[Findings on Phase I ESA standard compliance, component completeness, currency]

### Landowner Defense Assessment

[BFPP / Innocent Landowner / Contiguous Property Owner eligibility and prerequisites]

---

## Regulatory Compliance Findings

### [Module C: CERCLA] — [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL]

**Issue**: [Description]
**Regulatory Basis**: [42 U.S.C. § 9607(a); 40 C.F.R. Part 300]
**Confidence**: [Level (range)]
**Remediation**: [Specific action required]
**Timeline**: [Immediate / Before closing / Within 30/90/180 days]

[Repeat for each module activated]

---

## M&A Environmental Summary

[If Module J activated]

### Overall Classification: [PASS / FLAG / FAIL]

**Permit Transferability Matrix**:
| Permit | Type | Transfer Mechanism | Timeline | Risk |
|--------|------|-------------------|----------|------|
| [Permit 1] | [Type] | [Regulatory pre-approval] | [weeks] | [HIGH/MED/LOW] |

**Environmental Indemnification Recommendations**:

- [Specific indemnification provisions, survival periods, caps]

**PLL Insurance Considerations**:

- [Coverage gaps, PLL recommendation, existing policy assessment]

---

## Priority Action Plan

**Tier 1 — Immediate (Before Closing / This Week):**

1. [Action, owner, deadline]

**Tier 2 — High (Within 30 days):**

1. [Action, owner, deadline]

**Tier 3 — Medium (Within 90 days):**

1. [Action, owner, deadline]

**Tier 4 — Monitoring:**

1. [Regulatory developments to monitor]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

When adapting this skill for jurisdiction-specific use:

**US State-Specific:**

- Replace [JURISDICTION-SPECIFIC] markers with applicable state VCP requirements
- Add state-specific hazardous waste and air/water permit requirements
- Check state transfer-of-ownership environmental notification statutes (New Jersey ISRA;
  Connecticut RCSA; Indiana IDEM transfer requirements)

**EU Member State-Specific:**

- Add national EIA implementing regulation details (Germany UVPG thresholds; France
  Code de l'Environnement; Netherlands Besluit m.e.r.)
- Verify national implementation of ELD and IED
- Add Member State-specific BAT conclusions for the relevant industrial sector

**UK Scotland:**

- Scottish Environment Protection Agency (SEPA) rather than Environment Agency
- Scottish planning system (NPF4) rather than NPPF
- Nature Scot (formerly SNH) for biodiversity
- BNG not yet mandatory in Scotland [VERIFY current status]

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on deep research into US
environmental law (CERCLA, NEPA, Clean Air Act, Clean Water Act, RCRA, Phase I/II ESA
under ASTM E1527-21/E1903-19, PFAS hazardous substance designation April 2024), EU
environmental law (EIA Directive 2011/92/EU, IED 2.0 Directive 2024/1785, REACH, ELD
2004/35/CE, CS3D Directive 2024/1760, EU Taxonomy Regulation 2020/852), and UK
environmental law (Environment Act 2021 BNG, EPR 2016, Part IIA EPA 1990, UK EIA
Regulations SI 2017/571, Finch v. Surrey [2024] UKSC). Quality frameworks (Citation
Quality Gates, Self-Interrogation, Confidence Scoring, Glass Box audit trail, Anti-patterns)
adapted from the legalcode-contract-review reference standard.

Key legal developments incorporated: ASTM E1527-21 as required AAI standard (February 2023);
Sackett v. EPA WOTUS narrowing (May 2023); EPA PFOA/PFOS CERCLA designation (July 2024);
CEQ Phase 2 NEPA Rule vacatur (February 2025); mandatory UK BNG (February–April 2024);
Finch v. Surrey EIA combustion emissions (2024); IED 2.0 entry into force (August 2024);
CS3D publication (July 2024); EU Omnibus I CS3D/CSRD scope reduction (December 2025).
