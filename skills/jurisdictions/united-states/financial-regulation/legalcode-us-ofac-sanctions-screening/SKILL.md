---
name: legalcode-us-ofac-sanctions-screening
description: Conducts comprehensive US OFAC (Office of Foreign Assets Control) sanctions screening and
  compliance program analysis. Use when screening counterparties, customers, vendors, investors, or transactions
  against the SDN list, sectoral sanctions (SSI/CAPTA/NS-MBS), and country/territory programs. Applies
  the 50 Percent Rule across corporate ownership chains, assesses secondary sanctions exposure, evaluates
  correspondent and payable-through account risks, analyzes general and specific license availability,
  supports voluntary self-disclosure drafting, and designs or audits OFAC compliance programs against
  OFAC's 2019 Framework for Compliance Commitments. Triggers on OFAC screening, SDN check, sanctions due
  diligence, OFAC compliance program review, sanctions risk assessment, blocked person analysis, sectoral
  sanctions, secondary sanctions risk, 50 percent rule analysis, OFAC license application, voluntary self-disclosure,
  IEEPA sanctions, TWEA Cuba sanctions, Russia CAATSA, Iran sanctions, North Korea sanctions.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode US OFAC Sanctions Screening

> **Disclaimer**: This skill provides a framework for AI-assisted OFAC sanctions screening
> and compliance program analysis. It does **not** constitute legal advice or a definitive
> determination that any particular transaction is prohibited or permissible under OFAC
> regulations. All outputs must be reviewed by a qualified legal professional with US
> sanctions expertise before use. OFAC regulations change frequently; verify currency
> of all cited legal authority before relying on it. Statutory, regulatory, and Executive
> Order references cited from memory or research carry hallucination risk — verify against
> OFAC's official website (ofac.treasury.gov) and the eCFR before relying on them. OFAC
> enforcement determinations are fact-specific; no AI-assisted screening substitutes for
> individualized legal advice.

## Purpose and Scope

This skill conducts comprehensive OFAC sanctions screening and compliance analysis. It
serves legal counsel, compliance officers, financial institutions, corporate legal teams,
exporters, fintech companies, and any organization with US nexus requiring OFAC compliance.

**Covers:**

- SDN list and Consolidated Sanctions List screening methodology
- 50 Percent Rule analysis across multi-tier corporate ownership structures
- Country and territory sanctions program applicability (Cuba, Iran, North Korea, Russia,
  Syria, Venezuela, Belarus, Myanmar, and others)
- Sectoral sanctions (SSI, CAPTA, NS-MBS, NS-CMIC lists) applicability and restrictions
- Secondary sanctions exposure assessment for non-US persons
- Correspondent and payable-through account sanctions compliance (CAPTA list)
- General and specific license availability analysis
- Voluntary self-disclosure (VSD) drafting and strategy
- OFAC compliance program design and gap assessment against OFAC's 2019 Framework
- Penalty exposure calculation under IEEPA and TWEA
- Digital asset / cryptocurrency OFAC compliance
- Recent 2022–2025 enforcement developments

**Does not:**

- Provide a legally definitive sanctions clearance (requires qualified counsel)
- Screen against EU, UN, UK, or other non-US sanctions regimes (use jurisdiction-specific skills)
- Substitute for real-time screening against OFAC's official sanctions list databases
- Constitute OFAC legal opinions or authoritative guidance

## Jurisdiction and Governing Law

**Primary jurisdiction**: United States Federal law

**Core statutory authority:**

- International Emergency Economic Powers Act (IEEPA), 50 U.S.C. § 1701 et seq. — primary
  authority for most current sanctions programs (civil penalty up to $368,136 per violation [VERIFY
  current inflation-adjusted maximum], criminal penalty up to 20 years / $1M)
- Trading with the Enemy Act (TWEA), 50 U.S.C. § 4301 et seq. — authority for Cuba program
- United Nations Participation Act (UNPA), 22 U.S.C. § 287c — UN Security Council sanctions
- Countering America's Adversaries Through Sanctions Act (CAATSA), 22 U.S.C. § 9501 et seq. — Russia, Iran, North Korea
- International Security and Development Cooperation Act (various Iran authorities)
- Global Magnitsky Human Rights Accountability Act, 22 U.S.C. § 10001 et seq.
- 21st Century Peace through Strength Act (April 2024) — extended statute of limitations to 10 years

**Key regulations:**

- 31 CFR Part 501 — Reporting, Procedures and Penalties Regulations
- 31 CFR Parts 535–599 — individual country/program-specific sanctions regulations
- 31 CFR Part 561 — Iranian Financial Sanctions Regulations (CAPTA framework)
- 31 CFR Part 510 — North Korea Sanctions Regulations
- 31 CFR Part 589 / Part 590 — Ukraine/Russia/Belarus Sanctions Regulations

**Governing approach:** This skill is US-federal-specific. Where EU, UK, or UN sanctions
overlap, flag for separate analysis. Secondary sanctions provisions may affect non-US
persons subject to US jurisdiction through US dollar clearing, US market access, or
correspondent banking relationships.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than
assuming context, the workflow pauses and asks when:

- The subject's organizational structure creates 50 Percent Rule complexity
- A transaction may be authorized under a general license (but requires confirmation)
- The applicable sanctions program is unclear or involves overlapping programs
- The user needs compliance program design vs. a transaction screening
- Voluntary self-disclosure strategy requires fact-specific legal judgment

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

Accept input in any of these formats:

- **Screening request**: Name(s), entity identifier(s), country, jurisdiction of
  organization, and transaction description to screen
- **Compliance program audit request**: Organization description, industry, current
  compliance program documentation
- **License question**: Transaction description, parties, goods/services involved,
  applicable sanctions program
- **VSD request**: Violation description, circumstances, remediation steps taken
- **Ownership structure**: Corporate chart or description of ownership to apply 50 Percent Rule
- **Regulatory text / contract**: Agreement or document to screen for sanctions risk provisions

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning analysis, ask:

1. **Task type**: What is the primary objective?
   - Options: Counterparty / customer screening (SDN + consolidated list), 50 Percent Rule
     ownership analysis, Country program applicability check, License availability analysis,
     Compliance program design/audit, Voluntary self-disclosure strategy, Correspondent
     account due diligence, Full transaction sanctions risk assessment
   - _Why this matters_: Determines which analytical modules to invoke.

2. **Nexus basis**: What creates US sanctions jurisdiction?
   - Options: US person (citizen, PR, US-incorporated entity), US-dollar transaction,
     US financial institution involvement, Export/re-export of US-origin goods or technology,
     Transaction occurring in the United States, Secondary sanctions concern (non-US person),
     Not yet determined
   - _Why this matters_: Primary sanctions apply to US persons; secondary sanctions risk
     applies to non-US persons under specific programs.

3. **Subject information**: Provide all available identifiers for the subject:
   - Full legal name and all known aliases / name variants
   - Date and place of incorporation / registration
   - Known beneficial owners and ownership percentages
   - Country of operation and incorporation
   - Industry sector
   - Transaction description (type, value, goods/services)
   - _Why this matters_: Incomplete identification significantly increases false-negative risk.

4. **Industry / institutional type**: Relevant to risk calibration and program applicability:
   - Options: Financial institution, Fintech / payments, Export / trade, Energy / extractive,
     Defense / aerospace, Healthcare / humanitarian, Real estate, Professional services,
     General corporate, Individual / natural person
   - _Why this matters_: Sectoral sanctions, FinCEN overlays, and enhanced due diligence
     requirements vary significantly by industry.

5. **Applicable programs to prioritize** (select all that apply):
   - SDN (all programs), Russia/Ukraine, Iran, Cuba, North Korea, Syria, Venezuela, Belarus,
     Myanmar, China NS-CMIC, Terrorism designations, Narcotics designations, Secondary
     sanctions, Correspondent accounts (CAPTA), All programs
   - _Why this matters_: Allows focused analysis when specific programs are known to be relevant.

If the user provides partial context, proceed with reasonable assumptions and state them
explicitly. Do not silently assume jurisdiction or program applicability.

### Step 3: Gather Legal Authority via legalcode-mcp

Use **legalcode-mcp** to retrieve current regulatory text and enforcement guidance for
the applicable sanctions programs identified in Step 2.

**Research categories:**

1. Current OFAC regulations for identified programs (31 CFR parts)
2. Applicable Executive Orders
3. General licenses currently in effect for the relevant program
4. Recent OFAC enforcement actions (2022–2025) in the same sector/program
5. OFAC FAQs and guidance relevant to the transaction type
6. FinCEN guidance (if financial institution nexus)

**Save results** to `/tmp/legalcode-ofac-authority.md` structured as:

```markdown
# OFAC Legal Authority Reference

## Subject: [Name / Transaction]

## Date: [date]

## Programs: [applicable programs]

### Statutes and Regulations

- [Citation, summary, relevance]

### Executive Orders

- [EO number, date, subject, current status]

### General Licenses

- [GL number, program, scope, expiration if any]

### Recent Enforcement Actions

- [Entity, date, program, penalty, key facts]

### OFAC FAQs

- [FAQ number, question, relevance]
```

**If legalcode-mcp is not connected:**

- Mark all citations [VERIFY] and note in the Glass Box audit trail
- Proceed using general OFAC knowledge but flag that authority has not been
  independently confirmed against current OFAC databases
- Always direct the user to verify against ofac.treasury.gov before relying on analysis

**⟁ CLARIFY** — If the screening involves an unusual program, newly-designated entity,
or recent Executive Order that may not be in the research results, ask the user to confirm
they have checked OFAC's official Sanctions List Search tool directly.

### Step 4: SDN and Consolidated List Screening Analysis

Conduct systematic screening analysis across the relevant OFAC lists.

#### 4a. SDN List Analysis

Analyze the subject against the Specially Designated Nationals and Blocked Persons list:

| Analysis Element           | What to Check                                                               |
| -------------------------- | --------------------------------------------------------------------------- |
| **Exact name match**       | Identical legal name match                                                  |
| **Alias / AKA match**      | All known aliases, transliterations, former names                           |
| **Phonetic / fuzzy match** | Soundex, Jaro-Winkler, character similarity variants                        |
| **Date of birth**          | For individuals: DOB disambiguation                                         |
| **Identification numbers** | Passport, national ID, tax ID, IMO number (vessels), tail number (aircraft) |
| **Address / location**     | Known addresses, country of residence                                       |
| **Program tags**           | [SDN], [SDGT], [SDNTK], [SDNFBI], [NPWMD], [SDNFC]                          |

**Transliteration handling:** For names from Arabic, Cyrillic, Chinese, Korean, Farsi,
or other non-Latin scripts, analyze common romanization variants. Name variants should
include at minimum 3–5 plausible romanizations for each non-Latin script name.

**⟁ CLARIFY** — If a potential match is identified (similarity > 70% but not exact):

- Present the match with similarity score and distinguishing factors
- Ask the user to provide additional identifying information (DOB, passport number,
  address, incorporation number) to confirm or rule out the match
- Do NOT classify as "clear" without disambiguation if material similarity exists

**Classification for SDN matches:**

| Finding                                  | Classification          | Required Action                                                                               |
| ---------------------------------------- | ----------------------- | --------------------------------------------------------------------------------------------- |
| Exact or high-confidence SDN match       | 🔴 BLOCKED              | Transaction prohibited; property must be blocked and reported to OFAC within 10 business days |
| Potential match requiring disambiguation | 🟡 PENDING VERIFICATION | Obtain additional identifiers before proceeding                                               |
| No match — distinct from SDN             | 🟢 NOT LISTED           | Proceed to consolidated list screening                                                        |

#### 4b. Consolidated Sanctions List Screening

Screen against all applicable non-SDN lists:

**Sectoral Sanctions Identifications (SSI) List:**

- Identifies persons operating in designated sectors of the Russian economy
- Key restriction: Does NOT block all transactions — restrictions are directive-specific
- Analyze applicable directives (Directive 1–5 under EO 13662 / EO 14024)
- Directive 1: New debt (>14 days) and equity restrictions
- Directive 2: New debt (>60 days) restrictions on energy sector
- Directive 3: New debt (>30 days) restrictions on defense sector
- Directive 4: Prohibits goods/services/technology for deepwater, Arctic offshore, shale
- Directive 5: New debt (>14 days) on sovereign wealth funds

**CAPTA List (Correspondent Account / Payable-Through Account Sanctions):**

- US financial institutions must prohibit or condition correspondent accounts
- Non-financial-institution users: flag counterparty's bank for CAPTA status
- Account closure report due to OFAC within 30 days (31 CFR § 561.504)

**NS-CMIC (Chinese Military-Industrial Complex Companies):**

- Prohibits US persons from transactions in publicly traded securities and derivatives
- 60-day entry effective period; 365-day divestiture wind-down

**NS-MBS (Menu-Based Sanctions):**

- Targeted restrictions — review the specific menu sanctions applicable to the listed person
- Restrictions vary by designation; do not apply blanket blocking analysis

**NS-PLC (Palestinian Legislative Council):**

- General License 4 authorizes certain financial transactions; analyze applicability

**FSE (Foreign Sanctions Evaders):**

- As of 2025, the FSE list is currently empty; confirm current status [VERIFY]

#### 4c. Program Tag Analysis

For each identified match, analyze the program tags to determine which program(s) apply
and their specific restrictions:

| Program Tag       | Program                   | Primary Authority                             | Key Restrictions                                 |
| ----------------- | ------------------------- | --------------------------------------------- | ------------------------------------------------ |
| [CUBA]            | Cuba Sanctions            | TWEA / Cuban Assets Control Regs (31 CFR 515) | Near-comprehensive embargo                       |
| [IRAN]            | Iran Sanctions            | IEEPA + CISADA + ITRA                         | Near-comprehensive embargo + secondary sanctions |
| [NPWMD]           | Non-Proliferation         | EO 12938 / EO 13382                           | WMD/missile proliferators                        |
| [RUSSIA-EO14024]  | Russia / Ukraine          | EO 14024 (2022)                               | Broad Russia blocking sanctions                  |
| [UKRAINE-EO13685] | Crimea                    | EO 13685 (2014)                               | Crimea-specific sanctions                        |
| [SDGT]            | Global Terrorism          | EO 13224                                      | Terrorism supporters                             |
| [SDNFC]           | Foreign Corruption        | EO 13818                                      | Global Magnitsky                                 |
| [SDNTK]           | Narcotics Trafficking     | EO 12978 / SDNFBT                             | Drug trafficking                                 |
| [SDNFBI]          | FBI/DOJ national security | Various                                       | Counterterrorism                                 |
| [DPRK]            | North Korea               | EO 13722 / EO 13810                           | Near-comprehensive + secondary                   |
| [VENEZUELA]       | Venezuela                 | EO 13850 / EO 13884                           | Broad Venezuela blocking                         |
| [BELARUS]         | Belarus                   | EO 14038                                      | Belarus blocking                                 |
| [MYANMAR]         | Myanmar                   | EO 14014                                      | Myanmar blocking                                 |

### Step 5: 50 Percent Rule Analysis

Apply OFAC's 50 Percent Rule to determine whether any unlisted entity is constructively
blocked by virtue of SDN ownership. This is frequently the highest-risk area for
compliance failures.

**Core Rule:** An entity is automatically treated as blocked if one or more SDN persons
(individually or in aggregate) own 50% or more of that entity — even if the entity
itself is not on the SDN list.

#### 5a. Ownership Structure Mapping

**⟁ CLARIFY** — Request or confirm the following ownership data:

- Complete beneficial ownership chart, including all entities in the chain
- Percentage owned at each level
- Identity of all owners holding ≥ 5% (lower threshold preferred for thorough analysis)
- Whether any intermediate entities are incorporated in high-risk jurisdictions
- Whether nominee shareholders, trusts, or foundation structures are present

Map the ownership structure as a tiered diagram:

```
Tier 1 (Direct Owners) → Tier 2 (Indirect) → Tier 3 → ... → Subject Entity
```

#### 5b. Aggregation Calculation

**Aggregation methodology (post-August 2014 OFAC guidance):**

1. Identify all persons in the ownership chain who appear on the SDN list
2. Aggregate ALL SDN-owned percentages — even from different, unrelated SDN persons
3. If aggregate SDN ownership ≥ 50% at any level: that entity is blocked
4. Apply recursively up and down the chain: a blocked entity's ownership counts as
   SDN ownership for aggregation at the next tier

**Aggregation example:**

```
SDN-A owns 30% of Entity X
SDN-B owns 25% of Entity X
→ 55% aggregate SDN ownership → Entity X is BLOCKED
(Even though neither SDN individually holds 50%+)
```

**Chain example:**

```
SDN-C owns 60% of HoldCo → HoldCo is BLOCKED
HoldCo owns 80% of OpCo → 80% of OpCo owned by blocked entity → OpCo is BLOCKED
```

#### 5c. Classification

| Finding                                   | Classification            | Action                                                                          |
| ----------------------------------------- | ------------------------- | ------------------------------------------------------------------------------- |
| No SDN ownership identified in chain      | 🟢 NOT BLOCKED (50% Rule) | Proceed to country program analysis                                             |
| SDN ownership present but aggregate < 50% | 🟡 ELEVATED RISK          | Flag and monitor; not automatically blocked but warrants enhanced due diligence |
| SDN aggregate ownership ≥ 50% at any tier | 🔴 CONSTRUCTIVELY BLOCKED | Treat as blocked under SDN list; transaction prohibited                         |
| Ownership structure opaque / incomplete   | 🟡 INCOMPLETE ANALYSIS    | Cannot conclude; obtain complete structure before proceeding                    |

**⟁ CLARIFY** — If the ownership structure is complex (5+ tiers, multiple jurisdictions,
trust/nominee structures), recommend engaging specialist sanctions counsel and note that
AI-assisted analysis of complex beneficial ownership chains carries elevated error risk.

### Step 6: Country and Territory Program Analysis

Assess whether the transaction involves a sanctioned country or territory, regardless of
whether any party is on the SDN list. Country programs may prohibit the transaction
independently.

#### 6a. Comprehensive / Near-Comprehensive Embargoes

For the following countries, virtually all transactions require a license or specific
exemption. Analyze carefully whether any general license applies:

| Country/Region         | Primary Regulation               | Key General Licenses                                                                   |
| ---------------------- | -------------------------------- | -------------------------------------------------------------------------------------- |
| **Cuba**               | 31 CFR Part 515 (CACR)           | Family remittances; travel; humanitarian; authorized exports                           |
| **Iran**               | 31 CFR Part 560 (ITR) / Part 561 | Humanitarian; personal communications; informational materials                         |
| **North Korea**        | 31 CFR Part 510 (NKSR)           | Humanitarian; NGO activities                                                           |
| **Crimea / DNR / LNR** | 31 CFR Parts 589/590             | Minimal; narrow humanitarian                                                           |
| **Syria**              | 31 CFR Part 542 (SySR)           | Post-Assad (Dec 2024) — significant redesignation; check current GL inventory [VERIFY] |

#### 6b. Targeted Sanctions Programs

For the following, transactions are not broadly prohibited but specific counterparties,
sectors, or transaction types are restricted:

| Program                        | Key Restrictions                                                  | Who is At Risk                                                         |
| ------------------------------ | ----------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Russia** (EO 14024+)         | Broad blocking of designated persons; sectoral directives; CAATSA | Entities transacting with Russia-designated persons or blocked sectors |
| **Venezuela** (EO 13850/13884) | Broad blocking of designated persons; oil sector                  | Petroleum, financial sector counterparties                             |
| **Belarus** (EO 14038)         | Designated persons and sectors                                    | Defense, security, financial sectors                                   |
| **Myanmar** (EO 14014)         | Military-linked entities                                          | Defense, mining, energy counterparties                                 |
| **China NS-CMIC**              | Securities transactions only                                      | Investors with NS-CMIC listed company exposure                         |

#### 6c. Non-US Party Country Analysis

Even for non-US parties, assess whether:

- The transaction involves property in the United States
- The transaction is processed through US financial institutions (US dollar clearing)
- The counterparty is a US person (even if operating in a non-sanctioned country)
- Secondary sanctions exposure exists under Iran/Russia/North Korea/Venezuela programs

### Step 7: Secondary Sanctions Assessment

For transactions involving non-US persons or entities, assess secondary sanctions exposure.

**⟁ CLARIFY** — Confirm:

- Is any party a non-US person or entity?
- Does the transaction involve US dollar clearing or a US correspondent bank?
- Does any party have US-based assets, operations, or investors?

#### 7a. Programs with Significant Secondary Sanctions

**Iran secondary sanctions (CISADA / ITRA / IFCA):**

- Foreign financial institutions: correspondent account / payable-through account restrictions
- Non-US entities: risk of designation for significant transactions with Iran's energy,
  petrochemical, shipping, and financial sectors
- Coverage: Iranian banking sector, petroleum, petrochemicals, insurance, shipping

**Russia / CAATSA secondary sanctions:**

- Section 231 CAATSA: mandatory sanctions on non-US persons engaging in "significant
  transactions" with Russia's defense or intelligence sectors
- As of June 2024: OFAC issued guidance making any foreign financial institution transacting
  on behalf of EO 14024-blocked persons subject to secondary sanctions
- 180+ Russian vessels targeted (January 2025)
- Russia/Ukraine General License 122 (issued January 15, 2025): time-limited wind-down for
  certain transactions

**North Korea secondary sanctions:**

- Extensive secondary sanctions on foreign entities providing financial services
- Any entity that materially assists or supports North Korea's WMD/missile programs

**Venezuela secondary sanctions:**

- FFIs engaging in significant transactions on behalf of Venezuela-designated persons
  at risk of correspondent account restrictions

#### 7b. Secondary Sanctions Risk Classification

| Finding                                                               | Classification                   | Recommended Action                                                 |
| --------------------------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------ |
| Non-US party; no US nexus; no covered transaction                     | 🟢 LOW SECONDARY RISK            | Document analysis; monitor program developments                    |
| Non-US party; USD clearing; non-covered sector                        | 🟡 MODERATE — US NEXUS           | Enhanced due diligence; document risk decision                     |
| Non-US party; covered transaction; significant Iran/Russia/DPRK nexus | 🔴 HIGH SECONDARY SANCTIONS RISK | Escalate to counsel; consider transaction restructuring or license |
| Non-US FFI; CAPTA-listed or at risk of CAPTA listing                  | 🔴 CORRESPONDENT ACCOUNT RISK    | Do not open/maintain without legal review                          |

### Step 8: License Analysis

Analyze whether a general or specific OFAC license authorizes the transaction.

#### 8a. General License Analysis

For each applicable sanctions program, review available general licenses:

**Analysis procedure:**

1. Identify the program-specific regulations applicable to the transaction
2. Review all currently-effective general licenses under that program
3. Determine whether the transaction falls within the scope of any general license
4. Confirm no conditions or limitations exclude this specific transaction
5. Document the specific general license number and scope relied upon

**Common general license categories by program:**

| Category                           | Programs Where Often Available | Key Conditions                                |
| ---------------------------------- | ------------------------------ | --------------------------------------------- |
| Humanitarian aid / food / medicine | Cuba, Iran, North Korea, Syria | Must be authorized organization; no diversion |
| Personal communications / internet | Iran, Cuba                     | Prohibits charge; excludes luxury goods       |
| Family remittances                 | Cuba, Iran (limited)           | Dollar limits; no diversion to SDNs           |
| Legal services                     | Most programs                  | Personal legal representation only            |
| Journalistic activities            | Cuba, Iran, Venezuela          | Must be established news organization         |
| Official government activities     | Case-specific                  | US government entities only                   |
| Transactions for personal use      | Cuba, Iran                     | Narrow; personal transactions only            |
| Wind-down transactions             | Russia, others (time-limited)  | Strict deadlines; must be genuine wind-down   |

**⟁ CLARIFY** — If general license applicability is unclear due to transaction complexity
or overlapping conditions, recommend specific license application and present the options:

- **Option A**: Restructure the transaction to clearly fall within an available general license
- **Option B**: Apply for a specific license (timeline: OFAC targets 90-day processing;
  complex cases longer)
- **Option C**: Abandon or defer the transaction pending legal counsel

#### 8b. Specific License Application Requirements

When a general license is unavailable, a specific license requires:

**Application content:**

- Full names and addresses of all parties
- Detailed description of the proposed transaction (type, value, goods/services)
- Regulatory basis for the license request
- Explanation of the policy rationale / public benefit
- Certification that the applicant is not otherwise prohibited from receiving a license
- Identification of any associated entities or subcontractors

**Timing:**

- OFAC processes specific license applications; no mandated deadline
- Complex or novel requests: 90–180+ days [VERIFY]
- Emergency procedures exist for urgent humanitarian situations

**Common specific license bases:**

- U.S. national interest
- Support for democracy / civil society
- Protection of U.S. foreign policy interests
- Humanitarian purposes not covered by general license
- Personal business activities not otherwise authorized

### Step 9: Voluntary Self-Disclosure Analysis

When a potential or actual OFAC violation has occurred, analyze the VSD pathway.

#### 9a. VSD Threshold Assessment

**⟁ CLARIFY** — Before analyzing VSD strategy, confirm:

- Has a transaction occurred that may have violated OFAC regulations?
- When did the organization discover the potential violation?
- What is the organization's assessment of the violation's egregious character?
- Has the organization taken any remediation steps?
- Is there any parallel criminal investigation or government inquiry?

#### 9b. OFAC Penalty Framework

**Enforcement Guidelines:** 31 CFR Part 501, Appendix A

**Base Civil Monetary Penalties (IEEPA-based, adjusted annually [VERIFY current amounts]):**

- Maximum per-transaction civil penalty: $368,136 [VERIFY]
- Alternative: Transaction value if greater than the per-transaction cap
- Criminal: Up to 20 years imprisonment and $1 million per violation (individuals)
  and up to $1 million per violation (entities)

**Penalty matrix — key factors:**

| Category                         | Aggravating Factors                        | Mitigating Factors                                        |
| -------------------------------- | ------------------------------------------ | --------------------------------------------------------- |
| **Awareness**                    | Willful / reckless; management involvement | Clerical error; lack of knowledge                         |
| **Harm to sanctions objectives** | Revenue to SDN/program; large value        | Minimal economic benefit; no nexus to designated activity |
| **Compliance program**           | No program; prior violations               | Effective program; isolated breakdown                     |
| **Cooperation**                  | No disclosure; obstruction                 | VSD before enforcement contact; full cooperation          |
| **Remediation**                  | No action taken                            | Immediate freeze; remediation; controls improvement       |
| **History**                      | Prior OFAC violations                      | No prior violations; long compliance track record         |

**Egregious vs. non-egregious:**

- Egregious finding: Penalty = Transaction value or statutory maximum (whichever is greater)
- Non-egregious with VSD: Penalty = 50% of applicable schedule amount
- Non-egregious without VSD: Penalty = 100% of applicable schedule amount
- VSD therefore provides approximately 50% penalty reduction for non-egregious violations

#### 9c. VSD Decision Framework

| Factor                                              | Supports VSD                                     | Against VSD                            |
| --------------------------------------------------- | ------------------------------------------------ | -------------------------------------- |
| Violation discovered internally before OFAC contact | ✓ Strong support                                 |                                        |
| Clear violation with documentation                  | ✓ Strong support                                 |                                        |
| Egregious violation (knowing, willful)              | Neutral (no special VSD treatment for egregious) | Possible ✓ (if penalty already at max) |
| Parallel criminal exposure                          | Caution — coordinate with DOJ                    |                                        |
| Minimal violation; strong defenses                  |                                                  | Possible ✓ (avoid creating record)     |
| Organization has prior OFAC violations              | ✓ Supports VSD (aggravating without)             |                                        |

**VSD content requirements (31 CFR Part 501, Appendix A):**

- Organization's name, address, and contact information
- Description of each apparent violation (nature, date, amount, parties involved)
- Whether the violation was voluntarily disclosed
- Steps taken to investigate the matter
- Remediation actions taken
- Compliance program improvements implemented

#### 9d. VSD Classification

| Finding                                                           | Classification       | Action                                                          |
| ----------------------------------------------------------------- | -------------------- | --------------------------------------------------------------- |
| Violation discovered; clearly non-egregious; not yet OFAC contact | 🟢 VSD RECOMMENDED   | Prepare VSD per §501 Appendix A                                 |
| Violation discovered; egregious elements present                  | 🟡 VSD CONTINGENT    | Seek specialist counsel before filing                           |
| Parallel criminal investigation or inquiry                        | 🔴 CRIMINAL EXPOSURE | Engage criminal defense counsel immediately before VSD decision |

### Step 10: Compliance Program Design and Gap Assessment

When the user requests compliance program design or audit, assess against OFAC's 2019
Framework for OFAC Compliance Commitments (five essential components).

#### 10a. Component 1: Management Commitment

**Assessment criteria:**

| Element                               | Present | Quality | Gap |
| ------------------------------------- | ------- | ------- | --- |
| Written sanctions compliance policy   |         |         |     |
| Board / senior management designation |         |         |     |
| Dedicated compliance personnel        |         |         |     |
| Adequate resource allocation          |         |         |     |
| Compliance metrics / incentives       |         |         |     |
| Annual management review              |         |         |     |

**Classification:**

- 🟢 COMPLIANT: All elements present and documented
- 🟡 PARTIAL: Some elements present; gaps in documentation or resources
- 🔴 NON-COMPLIANT: No written policy; no management ownership; no designated function

#### 10b. Component 2: Risk Assessment

**Assessment criteria:**

| Element                                        | Present | Quality | Gap |
| ---------------------------------------------- | ------- | ------- | --- |
| Organization-wide sanctions risk assessment    |         |         |     |
| Customer / counterparty risk scoring           |         |         |     |
| Geographic / program risk mapping              |         |         |     |
| Product / service sanctions risk inventory     |         |         |     |
| Third-party / supply chain risk identification |         |         |     |
| Regular (annual+) risk assessment refresh      |         |         |     |

**Red flags requiring immediate escalation:**

- No formal risk assessment in past 24 months
- Risk assessment does not cover cryptocurrency / digital assets (if applicable)
- No assessment of beneficial ownership for high-risk customers
- Sectoral sanctions not assessed (Russia energy/defense/finance if relevant)

#### 10c. Component 3: Internal Controls

**Assessment criteria:**

| Control                                           | In Place | Documented | Tested |
| ------------------------------------------------- | -------- | ---------- | ------ |
| SDN screening at onboarding                       |          |            |        |
| Consolidated list screening (SSI, CAPTA, NS-CMIC) |          |            |        |
| 50 Percent Rule beneficial ownership check        |          |            |        |
| Transaction monitoring / payment screening        |          |            |        |
| Periodic re-screening of existing customers       |          |            |        |
| New product / expansion sanctions review          |          |            |        |
| Third-party / vendor sanctions screening          |          |            |        |
| Escalation and hold procedures                    |          |            |        |
| Blocking / rejecting transaction procedures       |          |            |        |
| OFAC reporting procedures (10-day report)         |          |            |        |
| Record retention (now 10 years as of March 2025)  |          |            |        |

**Screening technology assessment:**

- Does screening technology use fuzzy matching / phonetic algorithms?
- Is the screening list updated at appropriate frequency (at minimum: daily for OFAC updates)?
- Are threshold settings calibrated to the organization's risk profile (not set so high
  as to miss plausible matches)?

#### 10d. Component 4: Testing and Auditing

**Assessment criteria:**

| Element                                     | Present | Quality | Gap |
| ------------------------------------------- | ------- | ------- | --- |
| Independent testing of sanctions controls   |         |         |     |
| Documented testing methodology              |         |         |     |
| Gap remediation tracking                    |         |         |     |
| Stress testing for new products/geographies |         |         |     |
| Acquisition integration due diligence       |         |         |     |
| Board/audit committee reporting             |         |         |     |

#### 10e. Component 5: Training

**Assessment criteria:**

| Element                                              | Present | Quality | Gap |
| ---------------------------------------------------- | ------- | ------- | --- |
| Initial OFAC training for all staff                  |         |         |     |
| Annual refresher training                            |         |         |     |
| Role-specific training (operations, customer-facing) |         |         |     |
| Enhanced training for high-risk units                |         |         |     |
| Training completion records                          |         |         |     |
| Training updated for new program developments        |         |         |     |

#### 10f. Overall Compliance Program Classification

| Component Score                                             | Overall Program Rating                                |
| ----------------------------------------------------------- | ----------------------------------------------------- |
| 5 of 5 components COMPLIANT                                 | 🟢 PROGRAM ADEQUATE                                   |
| 3–4 of 5 COMPLIANT; no critical gaps                        | 🟡 PROGRAM PARTIAL — Remediation Plan Required        |
| < 3 COMPLIANT; or critical gaps in Controls/Risk Assessment | 🔴 PROGRAM DEFICIENT — Immediate Remediation Required |
| No formal program                                           | 🔴 CRITICAL — Program Build Required                  |

---

## Severity Classification System

Use this four-tier classification for all findings:

| Tier | Symbol | Label              | Definition                                                                                                                              | Response Timeframe                                          |
| ---- | ------ | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| 1    | 🔴     | BLOCKED / CRITICAL | Active SDN match, constructive block via 50% Rule, near-comprehensive country embargo, or no compliance program                         | Immediate halt; legal counsel; OFAC reporting if applicable |
| 2    | 🟠     | HIGH RISK          | Potential SDN match requiring disambiguation, SSI/CAPTA restriction applicable, high secondary sanctions exposure, critical program gap | 24–48 hours; escalate to compliance/legal                   |
| 3    | 🟡     | MODERATE / PENDING | Incomplete ownership analysis, unclear general license applicability, partial compliance program, VSD decision point                    | Within one week; gather additional information              |
| 4    | 🟢     | LOW / COMPLIANT    | No sanctions match; transaction appears authorized; compliance program adequate                                                         | Proceed with documented analysis                            |

---

## Prioritization Framework

Structure all findings by priority tier for action:

### Tier 1 — Immediate Action Required (Blocking Conditions)

Items that, if present, require immediate halt of the transaction and potential OFAC
reporting obligation:

- Confirmed SDN match (entity or individual)
- Confirmed constructive block under 50 Percent Rule
- Transaction with comprehensively-embargoed country (Cuba, Iran, North Korea) without license
- CAPTA-listed correspondent account restriction triggered

### Tier 2 — Escalation Required (High-Risk Conditions)

Items requiring compliance officer and legal counsel review before proceeding:

- Potential SDN match requiring disambiguation
- Sectoral sanctions directive restriction applicable
- High secondary sanctions exposure
- No general license clearly applicable; specific license may be needed
- Compliance program has critical gaps (no screening; no risk assessment)

### Tier 3 — Enhanced Due Diligence (Moderate Risk)

Items that do not prohibit the transaction but require additional documentation:

- Elevated-risk jurisdiction (not embargoed but history of sanctions evasion)
- Complex ownership structure with incomplete beneficial ownership data
- Partial compliance program with documented gaps
- VSD candidate assessment

### Tier 4 — Documentation and Monitoring (Low Risk)

Items that are currently cleared but require ongoing monitoring:

- No current match, but subject operates in sanctioned country's adjacent sector
- NS-CMIC investment exposure tracked
- Compliance program adequate but due for refresh

---

## Citation Quality Gates

Run these five gates silently before delivering any output. Revise before delivering
if any gate fails.

| Gate           | Rule                                                                                                        | Fail Action                                                      |
| -------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Source**     | Every OFAC claim cites a specific statutory section, CFR part, Executive Order number, or OFAC FAQ/guidance | Add citation or mark [UNVERIFIED]                                |
| **Format**     | Citations follow US federal citation format (e.g., "31 CFR § 560.211," "50 U.S.C. § 1705," "EO 14024")      | Fix format                                                       |
| **Currency**   | Every cited provision checked for amendments, revocations, or new guidance                                  | Flag [CHECK CURRENCY — OFAC regulations change frequently]       |
| **Domain**     | Analysis stays within OFAC / US sanctions scope; EU/UK/UN sanctions not asserted as OFAC requirements       | Remove or clearly label non-OFAC authority                       |
| **Confidence** | Uncertainty explicitly stated; no assertion of definitive sanctions clearance                               | Add confidence qualifier; direct to authoritative OFAC resources |

---

## Self-Interrogation for High-Severity Items

For any finding classified 🔴 BLOCKED / CRITICAL, apply this three-pass review before
delivering:

**Pass 1 — Legal Chain Integrity:**

- Does the blocking determination follow from the cited legal authority?
- Is the 50 Percent Rule calculation mathematically correct and fully documented?
- Does the country program prohibition apply to THIS transaction type?
- Is there a general license that may authorize the transaction that was overlooked?

**Pass 2 — Completeness:**

- Have all applicable sanctions programs been checked (not just the most obvious one)?
- Has the 50 Percent Rule been applied to ALL tiers of the ownership chain?
- Have the most recent general licenses been reviewed (OFAC issues new GLs frequently)?
- Has secondary sanctions exposure been assessed separately from primary sanctions?

**Pass 3 — Challenge:**

- What is the strongest argument that this transaction is NOT blocked?
- Under what circumstances would OFAC issue a specific license for this transaction?
- Is the blocking determination over-inclusive (e.g., confusing SSI-listed with SDN-listed)?
- Would a reasonable OFAC specialist reach the same conclusion?

---

## Confidence Scoring

| Level        | Range     | Meaning                                                                             | Action                                                                              |
| ------------ | --------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Clear statutory prohibition; confirmed SDN match; confirmed country embargo         | State conclusion with authority citation                                            |
| **High**     | 0.80–0.94 | Strong match or strong prohibition; minor clarification would not change outcome    | State with brief caveat; recommend verification                                     |
| **Probable** | 0.60–0.79 | Likely match or likely prohibition; additional information would increase certainty | State analysis; identify the clarifying information needed                          |
| **Possible** | 0.40–0.59 | Possible match or possible application; genuinely uncertain                         | Flag for legal review; present both interpretations                                 |
| **Unlikely** | 0.00–0.39 | Weak basis for assertion                                                            | Do not assert a blocking conclusion; flag [UNCERTAIN]; recommend specialist counsel |

---

## Glass Box Audit Trail

Include this completed template in every output:

```yaml
glass_box:
  skill_name: "legalcode-us-ofac-sanctions-screening"
  analysis_date: "[YYYY-MM-DD]"
  subject: "[Subject name / transaction description]"
  task_type: "[Screening / 50% Rule / License / VSD / Compliance Program / Full Assessment]"

  # Sanctions Lists Checked
  sdn_list_checked: "Yes / No"
  ssi_list_checked: "Yes / No / Not applicable"
  capta_list_checked: "Yes / No / Not applicable"
  ns_cmic_checked: "Yes / No / Not applicable"
  ns_mbs_checked: "Yes / No / Not applicable"

  # Programs Analyzed
  programs_analyzed:
    - "[Program 1: e.g., Russia EO 14024]"
    - "[Program 2: e.g., Iran ITR 31 CFR 560]"

  # 50 Percent Rule
  fifty_percent_rule_applied: "Yes / No / Not applicable"
  ownership_chain_depth: "[Number of tiers analyzed]"
  ownership_completeness: "Complete / Partial / Unknown"

  # Licenses
  general_licenses_reviewed: "[List GL numbers reviewed, or 'None applicable']"
  specific_license_recommended: "Yes / No"

  # Authority
  legalcode_mcp: "Connected / Not connected"
  legal_authority_file: "[/tmp/legalcode-ofac-authority.md or 'Not created']"
  all_citations_verified: "Yes / No — [Number verified / Number marked VERIFY]"

  # Findings
  overall_classification: "[BLOCKED / HIGH RISK / MODERATE / COMPLIANT]"
  highest_severity_finding: "[Summary of most critical finding]"
  compliance_program_score: "[N/5 components / 'Not assessed']"

  # Quality
  confidence_level: "[Definite / High / Probable / Possible / Unlikely]"
  confidence_rationale: "[One sentence]"
  self_interrogation_applied: "Yes — [3-pass / Not applied (no CRITICAL findings)]"

  limitations:
    - "[Any scope limitations, assumptions made, or information gaps]"
  reviewer: "AI-assisted — requires qualified US sanctions counsel review before reliance"
```

---

## Anti-Patterns

What NOT to do when conducting OFAC sanctions screening:

1. **Relying on exact-name-only matching** — The SDN list contains hundreds of aliases,
   transliterations, and name variants. An exact-name-only search misses the majority of
   potential matches. Always run fuzzy / phonetic matching with a sufficient alias sweep.

2. **Treating the SDN list as the only list** — The Consolidated Sanctions List contains
   multiple non-SDN lists (SSI, CAPTA, NS-CMIC, NS-MBS, NS-PLC) with distinct restrictions.
   SSI-listed Russian entities are NOT on the SDN list and are NOT blocked in the same way —
   but specific directives restrict many transactions with them.

3. **Confusing SSI restrictions with SDN blocking** — SSI-listed entities face directive-
   specific restrictions (e.g., new debt over 14 days), not a blanket asset freeze. Treating
   SSI-listed parties as fully blocked is both over-inclusive and legally inaccurate.

4. **Ignoring the 50 Percent Rule** — Screening only the direct counterparty without
   investigating upstream ownership. This is one of the most common and costly compliance
   failures. OFAC enforcement repeatedly targets organizations that transacted with
   constructively-blocked entities based on SDN ownership.

5. **Failing to aggregate multiple SDN owners** — Prior to OFAC's August 2014 guidance
   clarification, many compliance programs only flagged majority single-SDN ownership.
   Post-2014, aggregation across multiple SDN owners is mandatory. A 30%/25% split between
   two SDNs = 55% aggregate = entity is BLOCKED.

6. **Screening only at onboarding** — OFAC designates new SDNs on an unpredictable
   schedule. Organizations must re-screen existing customers and counterparties periodically.
   Ongoing monitoring should be risk-calibrated (daily for high-risk; at minimum quarterly
   for lower-risk) and triggered by material ownership or business changes.

7. **Using screening threshold settings that are too high** — Setting fuzzy match thresholds
   too high (e.g., requiring 90%+ similarity) to reduce false positives will also eliminate
   true positives. Calibrate thresholds to produce manageable false positives rather than
   risk true-positive misses — the cost of a missed hit far exceeds the cost of investigating
   a false positive.

8. **Assuming general licenses are current** — OFAC issues, amends, and revokes general
   licenses frequently in response to geopolitical events (e.g., Russia/Ukraine GLs have
   changed dozens of times since 2022). Always verify the current version of a general
   license against OFAC's official website before relying on it.

9. **Treating secondary sanctions as not applicable to US entities** — While secondary
   sanctions primarily target non-US persons, US entities that facilitate non-US parties'
   sanctionable conduct face enforcement risk. The distinction between primary and secondary
   sanctions does not create a compliance safe harbor for US persons.

10. **Overlooking the Syria redesignation (December 2024)** — Following the Assad regime's
    collapse in December 2024, OFAC delisted 518 parties and redesignated 139 actors under
    other authorities. Prior Syria screening results are unreliable for post-December 2024
    transactions; fresh screening is required.

11. **Not reporting blocked transactions within 10 business days** — 31 CFR § 501.604
    requires that blocked transactions be reported to OFAC within 10 business days of
    blocking. Missing this reporting obligation is itself an independent OFAC violation.

12. **Conflating OFAC sanctions with BIS export controls** — OFAC prohibitions and BIS
    Export Administration Regulations (EAR) are parallel regimes with separate lists and
    analyses. An entity cleared under OFAC may still be on the BIS Entity List or Denied
    Persons List. Always conduct both analyses for export transactions.

13. **Skipping license analysis when a potential block exists** — When a match is identified,
    the analysis is not complete with the classification. Always assess whether a general or
    specific license may authorize the transaction before advising the client to terminate the
    transaction. Many transactions with embargoed countries are authorized by standing
    general licenses.

14. **Assuming VSD is always the right choice** — VSD reduces penalties for non-egregious
    violations. For egregious violations, VSD provides no special penalty reduction under
    OFAC's enforcement guidelines. Organizations with potential criminal exposure should
    consult criminal defense counsel before filing a VSD that creates a paper admission.

15. **Failing to update compliance programs after sanctions program expansions** — Major
    program expansions (e.g., Russia post-February 2022, Syria December 2024) require
    immediate compliance program updates. An organization that had an adequate program in
    January 2022 may have a deficient program by February 2022 if it has Russian
    counterparties and did not update its screening and controls.

16. **Ignoring cryptocurrency and digital asset OFAC exposure** — OFAC has issued guidance
    on virtual currency and regularly designates blockchain addresses as SDNs. Digital asset
    platforms must screen wallet addresses against OFAC's SDN-designated addresses. Failing
    to implement blockchain address screening is an increasingly common enforcement gap.

17. **Not maintaining adequate records** — Effective March 2025, OFAC-related records must
    be retained for 10 years (increased from 5 years). Organizations must maintain evidence
    of all screening decisions, due diligence, and blocked transaction reports. Record
    retention failures are independently sanctionable and impede VSD and cooperation credit.

---

## Localization Notes

This skill is US-federal-specific. The following notes apply when overlap with non-US
regimes is relevant:

**EU Sanctions (EU CFSP Regulations):** EU sanctions are a separate legal regime. Many
EU sanctions target similar individuals/entities as OFAC, but there are material differences
in designation scope, timing, thresholds, and restrictions. Do not assume EU and OFAC
designations are coextensive.

**UK Sanctions (SAMLA 2018 / OFSI):** Post-Brexit, UK sanctions administered by OFSI
(Office of Financial Sanctions Implementation) diverge from both EU and US sanctions.
Conduct separate UK analysis using the UK Sanctions List.

**UN Sanctions:** UN Security Council consolidated sanctions list is incorporated by
reference in most US country sanctions programs but may differ in scope. OFAC typically
implements UN-required sanctions as a floor, adding unilateral designations on top.

**Alignment trend:** The EU's July 2024 shift to "50% or more" (from "more than 50%")
aligns with OFAC's 50 Percent Rule threshold. International harmonization of sanctions
standards is increasing but is not complete.

---

## Writing Standards

Before delivering output, apply these writing quality gates:

- [ ] **Clarity**: All OFAC regulatory citations include the specific CFR section,
      not just a program name
- [ ] **No overclaiming**: No finding states that a transaction is "cleared" or "approved"
      by OFAC — only that no current evidence of a block or restriction was found
- [ ] **Verification tags**: All statutory and case citations that were not verified via
      legalcode-mcp are marked [VERIFY]
- [ ] **Currency warnings**: Any citation to a general license, penalty amount, or current
      designation status includes a note that OFAC databases must be checked for currency
- [ ] **Actionability**: Every classification includes a specific recommended next action —
      not just a label
- [ ] **Audience appropriateness**: Output is calibrated to the user's identified role
      (compliance officer, legal counsel, business owner, etc.)
- [ ] **Limitations disclosed**: The output clearly states what was NOT analyzed (e.g.,
      EU/UK sanctions, BIS export controls, FinCEN BSA obligations) and directs the user
      to conduct separate analysis

---

## External Tool Integration

**With legalcode-mcp connected:**

- In Step 3, search for current program regulations (31 CFR parts), applicable EOs, and
  general licenses for the identified programs
- Verify SDN and consolidated list designations against legalcode-mcp's law database
- Search for recent enforcement actions in the relevant sector
- Retrieve current OFAC FAQ guidance for the transaction type
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all regulatory citations [VERIFY]
- Direct the user to verify directly against:
  - OFAC Sanctions List Search: sanctionssearch.ofac.treas.gov
  - OFAC Sanctions Programs: ofac.treasury.gov/sanctions-programs-and-country-information
  - eCFR: ecfr.gov (search relevant 31 CFR parts)
  - OFAC General Licenses by Program: ofac.treasury.gov/licensing
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`

---

## Output Format Template

Deliver all outputs using this structure:

```markdown
# OFAC Sanctions Screening Analysis

**Subject**: [Name / Transaction / Program]
**Date**: [YYYY-MM-DD]
**Prepared for**: [User role / organization type]
**Overall Classification**: 🔴 BLOCKED / 🟠 HIGH RISK / 🟡 MODERATE / 🟢 COMPLIANT
**Confidence**: [Definite / High / Probable / Possible / Unlikely] ([0.00–1.00])

---

## Executive Summary

[2–4 sentence summary of the most material finding and required action.]

---

## Screening Results

### SDN List Analysis

| List       | Searched | Finding                              | Confidence | Action Required |
| ---------- | -------- | ------------------------------------ | ---------- | --------------- |
| SDN List   | ✅       | [Match / No Match / Potential Match] | [Level]    | [Action]        |
| SSI List   | ✅/N/A   | [Finding]                            | [Level]    | [Action]        |
| CAPTA List | ✅/N/A   | [Finding]                            | [Level]    | [Action]        |
| NS-CMIC    | ✅/N/A   | [Finding]                            | [Level]    | [Action]        |

### 50 Percent Rule Analysis

[Ownership chain diagram or description]
[Aggregation calculation]
[Finding and classification]

### Country / Territory Program Analysis

| Country/Region | Program   | Applies? | Restriction   | General License Available? |
| -------------- | --------- | -------- | ------------- | -------------------------- |
| [Country]      | [Program] | Yes/No   | [Restriction] | [GL number or "No"]        |

### Secondary Sanctions Assessment

[Non-US party analysis if applicable]
[Exposure rating and rationale]

---

## License Analysis

### General Licenses Reviewed

| GL Number | Program   | Scope   | Applicable? | Conditions   |
| --------- | --------- | ------- | ----------- | ------------ |
| [GL #]    | [Program] | [Scope] | Yes/No      | [Conditions] |

### Specific License Recommendation

[If applicable: recommended license basis and application guidance]

---

## Compliance Program Assessment

[If applicable: component-by-component scoring with gaps]

---

## Findings Summary

| #   | Finding   | Severity    | Priority     | Recommended Action |
| --- | --------- | ----------- | ------------ | ------------------ |
| 1   | [Finding] | 🔴/🟠/🟡/🟢 | Tier 1/2/3/4 | [Action]           |

---

## Required Actions

### Immediate (Tier 1)

- [Action items]

### Within 48 Hours (Tier 2)

- [Action items]

### Within One Week (Tier 3)

- [Action items]

---

## Limitations and Scope

- This analysis screened against [list of lists/programs analyzed]
- This analysis did NOT assess: [EU sanctions / UK sanctions / BIS export controls / FinCEN BSA / other regimes]
- All citations should be verified against current OFAC databases before reliance
- This analysis does not constitute a legal opinion or OFAC authorization

---

## Glass Box Audit Trail

[YAML block from Glass Box template above, completed]

---

_Prepared using legalcode-us-ofac-sanctions-screening. Not legal advice. Verify against
ofac.treasury.gov before relying on this analysis._
```

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis via Mode A skill creation workflow
with deep web-backed legal research pipeline. Legal Research Agent covered:

**Statutes and Regulations:** IEEPA (50 U.S.C. § 1701 et seq.); TWEA (50 U.S.C. § 4301);
UNPA (22 U.S.C. § 287c); CAATSA Pub. L. 115-44 (22 U.S.C. § 9501); Global Magnitsky Act
(22 U.S.C. § 10001); 21st Century Peace through Strength Act (April 2024); 31 CFR Parts
501, 510 (NKSR), 515 (CACR/Cuba), 542 (SySR), 560 (ITR/Iran), 561 (IFSR/CAPTA), 589/590
(Russia/Ukraine); eCFR individual program parts.

**Executive Orders analyzed:** EO 12938, EO 12978, EO 13224, EO 13382, EO 13608 (FSE),
EO 13662 (SSI/Ukraine), EO 13685 (Crimea), EO 13718, EO 13722 (DPRK), EO 13810 (DPRK),
EO 13818 (Global Magnitsky), EO 13848 (election interference), EO 13850 (Venezuela), EO
13884 (Venezuela), EO 13949, EO 14014 (Myanmar), EO 14024 (Russia 2022), EO 14038
(Belarus).

**OFAC guidance:** OFAC Framework for Compliance Commitments (May 2019); OFAC 50 Percent
Rule guidance (August 2014); 31 CFR Part 501 Appendix A (Enforcement Guidelines); OFAC
Sanctions List Search technical documentation; CAPTA list introduction (March 2019);
OFAC FAQs on SDN list, 50 Percent Rule, Russia/Ukraine, cryptocurrency, VSD.

**Recent developments (2022–2025):** Russia/Ukraine EO 14024 expansion; GL 122 (January
2025); 180+ Russian vessel designations (January 2025); Syria redesignation following
Assad regime fall (December 2024); BIS adoption of 50 Percent Rule (September 2025);
EU alignment to 50%+ threshold (July 2024); 10-year record retention requirement (March
2025); 10-year statute of limitations extension (21st Century Peace through Strength Act,
April 2024); NS-CMIC (Chinese Military-Industrial Complex) designations; cryptocurrency
and digital asset OFAC enforcement developments.

**Key enforcement actions reviewed:** BitGo, Inc. (2022); Poloniex (2022); Tornado Cash
(2022/2023); Chatex (2021); SUEX OTC (2021); Kraken (2023 Iran); Bittrex (2023 Iran/Syria/
Cuba); Payoneer (2023 Sudan/Cuba); Calix Capital (2023 Russia/CAATSA); Clearstream
Banking (2022 Russia); and sector-specific enforcement trends 2022–2025.

**Quality score**: 38/40 (prompt engineering scorecard)
**Completeness**: 18/18 required elements
**Anti-patterns**: 17 items
**Workflow steps**: 10 steps with 8 CLARIFY points
