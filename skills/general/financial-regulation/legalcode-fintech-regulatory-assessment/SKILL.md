---
name: legalcode-fintech-regulatory-assessment
description: Assess fintech regulatory compliance across four major jurisdictions — US, UK, EU, and Singapore.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Assess fintech regulatory compliance across four major jurisdictions — US, UK, EU, and Singapore. Covers money transmission licensing (state MTL requirements, FinCEN MSB registration, exemption analysis), UK FCA authorisation (payment institution, e-money institution, FCA regulatory sandbox), EU payments regulation (PSD2 AISP/PISP licensing, PSD3/PSR transition, EMD2, strong customer authentication), EU crypto-asset regulation (MiCA CASP licensing, e-money tokens, asset-referenced tokens), EU digital resilience (DORA applicability), Singapore MAS licensing (Payment Services Act, Standard/Major payment institution, digital payment token services), bank-as-a-service partnerships (sponsor bank model, third-party risk management, BSA/AML compliance), open banking regulatory frameworks (UK Open Banking, EU PSD2 access-to-accounts, US CFPB Section 1033 rule), and US charter selection (national bank, ILC, state bank, special purpose fintech charter). Produces a jurisdiction-specific regulatory gap assessment with COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL severity ratings, licensing pathway recommendations, BaaS partnership risk analysis, and a prioritised remediation roadmap. Use for pre-launch regulatory readiness reviews, licensing strategy decisions, BaaS partnership due diligence, product expansion assessments, and regulatory examination preparation. Triggers on: fintech licensing, money transmission licence, MTL, MSB registration, FinCEN, payment institution, e-money institution, FCA authorisation, PSD2, PSD3, open banking, AISP, PISP, MiCA, CASP, DORA, MAS licensing, Payment Services Act, BaaS, bank-as-a-service, sponsor bank, OCC charter, ILC charter, fintech charter, BSA AML compliance, Section 1033, consumer financial data rights.


# Legalcode Fintech Regulatory Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted fintech regulatory
> compliance assessment. It does not constitute legal advice. All outputs must be reviewed
> by qualified financial services counsel licensed in the relevant jurisdiction(s) before
> use. Fintech regulation changes rapidly — new licensing rules, regulatory guidance,
> and enforcement actions emerge continuously. Statutory citations, thresholds, and
> regulatory positions cited from memory carry hallucination risk. Regulatory failures
> can result in cease-and-desist orders, civil money penalties, licence revocation, and
> criminal exposure — do not rely on this skill alone to confirm regulatory compliance
> or to make licensing decisions.

---

## Purpose and Scope

This skill assesses the regulatory compliance posture and licensing requirements for
fintech companies operating or planning to operate in the United States, United Kingdom,
European Union, and Singapore. It identifies regulatory gaps, recommends licensing
pathways, analyses BaaS partnership structures, and produces a prioritised remediation
roadmap.

**Covers:**

- US money transmission: state MTL requirements across all 50+ jurisdictions, FinCEN
  MSB registration, exemption analysis (agent-of-payee, bank agent, de minimis)
- US bank charters: national bank (OCC), state bank, ILC, thrift/FSA, special purpose
  fintech charter, and CUSO model — comparative analysis for fintech applicants
- US BaaS: sponsor bank model, OCC/FDIC third-party risk management guidance, BSA/AML
  programme requirements, Regulation E obligations, UDAP/UDAAP exposure
- US open banking: CFPB Section 1033 final rule (Personal Financial Data Rights), scope,
  timelines, data access obligations, and third-party authorisation framework
- UK FCA authorisation: Authorised Payment Institution (API) vs. Small Payment Institution
  (SPI) vs. Authorised E-Money Institution (AEMI) vs. Small E-Money Institution (SEMI),
  registration vs. authorisation distinction, passporting post-Brexit, regulatory sandbox
- UK open banking: CMA Order, FCA oversight of open banking, OBIE/JROC successor
  arrangements
- EU PSD2/PSD3/PSR: current PSD2 licensing framework (AISP, PISP, ASPSP), SCA
  requirements, proposed PSD3 and Payment Services Regulation transition, EMD2
- EU MiCA: CASP licensing obligations, e-money token (EMT) rules, asset-referenced token
  (ART) issuer requirements, grandfathering provisions
- EU DORA: applicability to regulated fintech entities, ICT risk management requirements,
  incident reporting timelines
- Singapore MAS: Payment Services Act 2019 licence tiers (Standard/Major/Money-changer),
  seven payment service categories including digital payment token (DPT) services, MAS
  regulatory sandbox
- BaaS partnership structure: risk mapping, contract terms to require, regulatory
  accountability allocation, BSA/AML programme integration

**Does not:**

- Provide legal advice or substitute for qualified regulatory counsel
- Perform live regulatory filings, licence applications, or submissions to regulators
- Cover insurance, securities, commodities, or investment advisory regulation (except
  where intersecting with fintech payment services)
- Apply exclusively to one jurisdiction — assessment adapts to the company's target
  operating footprint with [JURISDICTION-SPECIFIC] markers

---

## Jurisdiction and Governing Law

This skill covers **four regulatory domains** that operate under distinct legal frameworks:

| Domain             | Primary Regulators                                                  | Key Legislative Basis                                                                                              |
| ------------------ | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **United States**  | FinCEN, OCC, FDIC, Federal Reserve, CFPB, state banking departments | BSA, Dodd-Frank, state MTL statutes, Electronic Fund Transfer Act                                                  |
| **United Kingdom** | FCA, PSR, Bank of England                                           | Payment Services Regulations 2017, Electronic Money Regulations 2011, Financial Services and Markets Act 2000      |
| **European Union** | National Competent Authorities (NCAs), EBA, ECB                     | PSD2 (Directive 2015/2366), EMD2 (Directive 2009/110/EC), MiCA (Regulation 2023/1114), DORA (Regulation 2022/2554) |
| **Singapore**      | MAS                                                                 | Payment Services Act 2019 (as amended), MAS Notices PSN01/PSN02                                                    |

[JURISDICTION-SPECIFIC] A fintech operating across multiple jurisdictions requires
separate compliance analysis for each. Never assume that compliance in one jurisdiction
satisfies requirements in another, even where frameworks are broadly similar (e.g., UK
and EU post-Brexit). Always verify current regulatory text, as this field changes rapidly.

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
the user's regulatory situation, the workflow pauses and asks when:

- The company's operating model is unclear and affects which licences are required
- Multiple licensing pathways exist and the optimal route depends on business objectives
- Jurisdiction scope needs to be confirmed before deep analysis begins
- The BaaS partnership structure materially affects the compliance analysis

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

### Step 1: Accept the Assessment Request

Accept input in any of these formats:

- **Company description**: Business model, product type, target geographies, current
  regulatory status
- **Document**: Existing compliance review, licence application draft, BaaS term sheet,
  product spec, or regulatory correspondence
- **Specific question**: Point question about a licence requirement or regulatory obligation

If only a vague topic is provided, proceed to Step 2 to gather the specific context needed.

### Step 2: Gather Business Context

**⟁ CLARIFY** — Before beginning the analysis, gather these parameters:

1. **Business model** — What does the company do?
   - Options: Payments / remittance, Digital banking / neobank, Crypto / DeFi, BaaS / embedded finance, Lending, Wealth management / robo-advisory, Regtech / compliance tooling, Multiple (describe)
   - _Why this matters_: Determines which regulatory regimes apply and which licences are required.

2. **Target jurisdictions** — Which markets are in scope?
   - Options: US only, UK only, EU only (specify member states), Singapore only, US + UK, US + EU, US + UK + EU, US + UK + EU + Singapore, Other (describe)
   - _Why this matters_: Determines the regulatory frameworks that must be analysed.

3. **Current regulatory status** — What licences or registrations does the company currently hold?
   - Options: None — pre-launch, FinCEN MSB registration only, State MTL (specify states), FCA regulated (specify type), EU regulated (specify country/licence type), MAS regulated (specify licence), Other (describe)
   - _Why this matters_: Shapes the gap analysis — what is already in place vs. what needs to be obtained.

4. **BaaS partnership** — Is the company using a bank-as-a-service or sponsor bank model?
   - Options: Yes — assessing or active BaaS partnership, No — seeking own licence(s), Uncertain — exploring both paths
   - _Why this matters_: BaaS fundamentally changes the licensing analysis and shifts the compliance obligations to the programme level.

5. **Product activities** — Which specific activities does the company perform?
   - Multiple-select options: Money transmission / remittance, Currency exchange, Issuing prepaid / stored value, Receiving deposits, Lending, Account services (FDIC-insured), Card issuance (debit / credit), Crypto custody / trading, Stablecoin issuance, Open banking / data aggregation, Other (describe)
   - _Why this matters_: Each activity triggers different licensing obligations within each jurisdiction.

6. **Timeline** — Is there a regulatory deadline or launch target?
   - Options: Urgent (weeks), Near-term (3-6 months), Planning (6-12 months), No fixed deadline
   - _Why this matters_: Affects prioritisation — immediate blockers vs. roadmap items.

### Step 3: Map Regulatory Obligations

Based on the confirmed business model and jurisdictions, map the applicable regulatory
frameworks. Produce a preliminary obligation matrix:

| Activity     | US Obligation         | UK Obligation         | EU Obligation           | SG Obligation                     |
| ------------ | --------------------- | --------------------- | ----------------------- | --------------------------------- |
| [activity 1] | [MTL / MSB / charter] | [API / AEMI / exempt] | [PSD2 licence / exempt] | [Standard PI / Major PI / exempt] |
| [activity 2] | ...                   | ...                   | ...                     | ...                               |

Use the **Regulatory Framework Reference** section below to map activities to obligations.

**⟁ CLARIFY** — If the obligation mapping reveals ambiguity about whether an activity is
licensed or exempt, present the relevant exemption analysis and ask the user to confirm
their understanding of how their product works:

- "Your product description could fall under the agent-of-payee exemption in some US
  states if [condition]. Does your model satisfy that condition?"
- "In the EU, your token could be classified as an e-money token (EMT) under MiCA or as
  a unit in a collective investment scheme under MiFID. Which reflects your structure?"

### Step 4: Gather Legal Authority

Use **legalcode-mcp** (if connected) to search for current regulatory requirements,
recent enforcement actions, and regulatory guidance for the identified frameworks.

**Research targets:**

- Current MTL requirements for the identified US states
- Recent FinCEN/OCC/FDIC guidance on the identified activities
- FCA Authorisation conditions for the identified licence type
- EBA technical standards and guidelines under PSD2 and PSD3 transition documents
- MAS regulatory notices and circulars relevant to the licence type
- Recent enforcement actions in the target jurisdictions for similar business models

Save results to `/tmp/legalcode-fintech-authority.md`. Structure as:

```markdown
# Regulatory Authority Reference — [Company Name / Project]

## Date Gathered: [date]

## Jurisdictions: [list]

### US Authority

- [Statute / Regulation / Guidance — source — key requirement]

### UK Authority

- [FCA Policy Statement / FSMA provision / PSRs provision]

### EU Authority

- [Directive / Regulation / EBA Guideline]

### Singapore Authority

- [MAS Notice / PSA provision / MAS Circular]

### Enforcement Actions

- [Regulator, entity, activity, penalty — year]
```

**If legalcode-mcp is not connected:**

- Mark all specific statutory thresholds and recent guidance with [VERIFY]
- Proceed using the Regulatory Framework Reference in this skill
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`

### Step 5: Jurisdiction-by-Jurisdiction Assessment

Assess each applicable jurisdiction in depth. For each jurisdiction:

1. Identify required licences / registrations for the confirmed activities
2. Assess current compliance status against each requirement
3. Classify each finding as COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL
4. Identify the licensing pathway or remediation steps
5. Flag recent regulatory developments that affect the analysis

Use the **Regulatory Framework Reference** section below as the analytical basis.

**⟁ CLARIFY** — For ambiguous regulatory perimeters where classification turns on
product-specific facts, ask before classifying:

- "Does your platform take possession of user funds at any point, or do you always
  transmit directly? This determines whether state MTL is required in most jurisdictions."
- "Does your crypto product offer a stablecoin redemption guarantee? This would likely
  classify it as an EMT under MiCA."

### Step 6: BaaS Partnership Analysis (if applicable)

If the company is using or considering a BaaS / sponsor bank model, assess the structure
against the BaaS Risk Framework in this skill. Cover:

1. **Regulatory accountability allocation**: Which obligations does the bank own vs.
   the fintech?
2. **BSA/AML programme**: Who is the programme owner? How is suspicious activity
   monitoring structured?
3. **FDIC representation risk**: Is the fintech making any representations about
   deposit insurance that could violate 12 USC § 1828(a)?
4. **Third-party risk management**: Does the bank's programme satisfy OCC/FDIC/Federal
   Reserve guidance?
5. **Contract adequacy**: Does the programme agreement include the required provisions?

**⟁ CLARIFY** — If the BaaS term sheet or agreement is available, ask the user to
provide it so the contract terms can be assessed against the BaaS Contract Requirements
checklist below.

### Step 7: Prioritise Findings and Build Roadmap

Classify all findings by severity (see Severity Classification below) and organise into
a three-tier remediation roadmap:

- **Tier 1 — CRITICAL / BLOCKING**: Issues that prevent lawful operation or pose immediate
  regulatory or criminal exposure. Must be resolved before launch or continued operation.
- **Tier 2 — MATERIAL**: High-risk gaps that require remediation before scale. Should be
  resolved within 3-6 months.
- **Tier 3 — REMEDIATE**: Moderate gaps to address in the next compliance cycle. Lower
  urgency but should be tracked.

For each finding, provide:

- Finding description
- Severity classification
- Affected jurisdiction(s)
- Recommended remediation action
- Regulatory deadline (if applicable)
- Estimated complexity of remediation

### Step 8: Quality Verification

Before delivering the assessment, run the quality checks:

1. Run the 5 Citation Quality Gates silently. Revise any failures before delivery.
2. For every CRITICAL item, run the 3-pass Self-Interrogation.
3. Assign a Confidence Score to each material compliance determination.
4. Verify that all activities have been mapped to the applicable regulatory frameworks.
5. Verify that no jurisdiction-specific concepts have leaked into other jurisdictions.
6. Generate the Glass Box Audit Trail.

### Step 9: Deliver Assessment

Deliver the output using the Output Format Template at the end of this skill.

---

## Regulatory Framework Reference

### US Framework

#### A. Money Transmission and FinCEN MSB

**FinCEN MSB Registration**

Any entity that transmits more than $1,000 in funds for any person on the same day
[VERIFY: 31 CFR § 1010.100(ff)] must register with FinCEN as a Money Services Business
(MSB) within 180 days of beginning operations. MSB registration covers federal BSA/AML
obligations but does NOT substitute for state MTLs.

BSA/AML programme requirements for MSBs [VERIFY: 31 CFR § 1022.210]:

- Written AML programme
- Policies, procedures, and internal controls
- Designation of a compliance officer
- Ongoing employee training
- Independent audit function
- Customer Identification Programme (CIP) [VERIFY: 31 CFR § 1022.220]
- Suspicious Activity Report (SAR) filing [VERIFY: 31 CFR § 1022.320]
- Currency Transaction Report (CTR) for transactions over $10,000

**Recent MSB enforcement examples:**

- **Paxful (FinCEN/DOJ, 9 December 2025):** $3.5 million civil monetary penalty for
  willful failure to maintain MSB registration, failure to implement an effective
  risk-based AML programme, and failure to file timely and complete SARs. Significant:
  FinCEN simultaneously published its first "Compliance Considerations" guidance document
  establishing expectations for how peer-to-peer crypto platforms must operate.
- **TD Bank (OCC/FinCEN/DOJ, 2024):** Over $3 billion AML penalty — the largest in US
  history — for systemic AML failures enabling drug trafficking. While not a fintech,
  sets the regulatory enforcement appetite for transaction-volume institutions.

**State Money Transmission Licences (MTL)**

Money transmission is regulated at the state level. Most states require a licence for
any entity receiving money for transmission, regardless of the transmission mechanism.
There is no federal preemption of state MTL requirements for non-bank entities.

[JURISDICTION-SPECIFIC] State-by-state key considerations:

| Tier                 | States                                                                                 | Notes                                                                                |
| -------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Most Complex**     | New York (BitLicense for crypto + MTL), California (DFPI), Texas (TDOB), Florida (OFR) | Highest capital requirements, longest processing times (12-24 months)                |
| **Challenging**      | Illinois, Pennsylvania, Washington, Georgia, New Jersey                                | Significant net worth and surety bond requirements; active examination programmes    |
| **Expedited / NMLS** | States using NMLS multistate licensing — majority of states                            | NMLS allows concurrent applications; reduces administrative burden                   |
| **Crypto Specific**  | New York (BitLicense separate from MTL), Wyoming (SPDI), Louisiana                     | Additional crypto-specific licences required alongside or instead of traditional MTL |

Key MTL requirements across most states [VERIFY per state]:

- Net worth / minimum capital requirements (typically $50,000-$1,000,000+ depending on state and activity volume)
- Surety bond (typically $25,000-$500,000, indexed to transaction volume)
- Permissible investments sufficient to cover outstanding money transmission obligations
- Principal and key officer background checks
- Business plan and financial statements
- BSA/AML programme documentation
- Cybersecurity programme documentation

**Common MTL Exemptions** [VERIFY per state]:

| Exemption             | Conditions                                                                                                                                     | Risk                                                                |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Agent-of-payee**    | Transmitting to a payee who has directed the collection; no money transmission licence required if agent receives funds on behalf of the payee | Very narrow; conditions tightly interpreted; varies by state        |
| **Bank agent**        | Acting as agent of a licensed bank; bank assumes regulatory accountability                                                                     | Requires formal bank agency agreement; bank must maintain oversight |
| **De minimis**        | Some states exempt very low-volume transmitters                                                                                                | Thresholds vary; not available in major jurisdictions               |
| **Payroll processor** | Some states exempt payroll processing                                                                                                          | Activity-specific; not available for consumer-facing products       |

**Criminal exposure**: Operating as an unlicensed money transmitter violates 18 U.S.C.
§ 1960 — a federal crime carrying up to $250,000 in fines and five years imprisonment.
This applies regardless of whether the violation was knowing. Fintechs that launch
nationwide operations on a limited state licence stack face criminal risk in unlicensed
states from day one of operation.

**Red flag**: Relying on exemptions without a written legal opinion from counsel admitted
in each relevant state creates material regulatory exposure.

#### B. US Bank Charter Selection

| Charter Type                             | Regulator                   | Key Advantage                                             | Key Constraint                                                                                                                                                                 | Fintech Fit                                                       |
| ---------------------------------------- | --------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| **National Bank**                        | OCC                         | Federal preemption of state law; nationwide branching     | Full banking regulation; BHCA triggers; capital requirements                                                                                                                   | High — maximum regulatory certainty; complex/expensive            |
| **State Bank (Fed member)**              | State + Federal Reserve     | Dual regulation flexibility                               | Less preemption; state-by-state compliance                                                                                                                                     | Medium — suited to state-specific strategies                      |
| **State Bank (non-member)**              | State + FDIC                | Lower federal burden                                      | Weakest preemption; limits expansion                                                                                                                                           | Low for multi-state fintechs                                      |
| **ILC / Industrial Loan Company**        | State (FDIC insured)        | Non-bank parent company can own; commercial owner allowed | Limited to specific states (Utah, Nevada, California, Hawaii); limited BHCA application                                                                                        | High for commercial-parent fintechs (e.g., Rakuten, Square/Block) |
| **Federal Savings Association / Thrift** | OCC (as FSOA)               | Federal preemption; nationwide                            | Qualified Thrift Lender test                                                                                                                                                   | Medium — well-suited to mortgage-heavy models                     |
| **Special Purpose Fintech Charter**      | OCC                         | Nationwide; no full banking powers required               | Litigation-contested; not deposit-taking [VERIFY: OCC v. Vullo litigation]                                                                                                     | Speculative — current legal uncertainty                           |
| **Wyoming SPDI**                         | Wyoming Division of Banking | No BHCA; 100% reserve; digital asset custody/payment      | No FDIC insurance; no lending; $5M minimum capital; Wyoming principal office required; Federal Reserve master account denied to date [VERIFY: Custodia Bank litigation status] | Digital asset custodians; institutional clients                   |
| **CUSO Model**                           | NCUA + State                | Access to credit union distribution; no banking licence   | Cannot hold deposits directly; limited to credit union relationships; 51%+ customers must be CU members                                                                        | Niche — B2B2C embedded finance model                              |

[JURISDICTION-SPECIFIC] **OCC charter update (December 2025):** The OCC issued
conditional approvals for national trust bank charters on 12 December 2025 to five
crypto/digital asset companies (Circle, Ripple, BitGo, Fidelity Digital Assets, Paxos).
11 total applicants as of March 2026 including Stripe subsidiary Bridge, Coinbase, and
Payoneer. A regulatory amendment effective 1 April 2026 clarified that national trust
banks may engage in non-fiduciary custody and safekeeping activities. **Only Anchorage
Digital Bank** holds a fully operational national trust bank status; all December 2025
approvals are conditional. The national trust bank charter does not authorise deposit-
taking; it provides nationwide custody/trust services. The broader "special purpose
fintech charter" (non-deposit-taking, without trust powers) remains in legal uncertainty
[VERIFY: Second Circuit resolution of CSBS challenge; current OCC policy on non-trust
fintech applications as of assessment date].

#### C. BaaS / Sponsor Bank Model

The BaaS model allows a non-bank fintech to offer banking-like products (FDIC-insured
accounts, debit cards, ACH access) through a contractual relationship with a licenced
bank. The bank holds the charter; the fintech provides the technology and customer
interface.

**Regulatory accountability under BaaS:**

| Obligation          | Bank Responsibility                                                     | Fintech Responsibility                                                           |
| ------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| FDIC insurance      | Owns and must not allow misrepresentation                               | Cannot represent coverage extends to custodial/pooled funds not in customer name |
| BSA/AML programme   | Programme owner; cannot delegate ultimate accountability                | Must implement bank-approved transaction monitoring; SARs filed by bank          |
| Regulation E        | Bank is the financial institution; holds liability for error resolution | Must implement dispute-capture process; feed into bank's error resolution        |
| UDAP / UDAAP        | Bank subject to OCC / FDIC UDAP; fintech subject to CFPB UDAAP          | Marketing materials, fee disclosures, and onboarding flows must be reviewed      |
| Third-party risk    | Bank must manage fintech as a critical third party                      | Must submit to bank's vendor assessment, audit rights, and programme oversight   |
| Consumer complaints | Must route to bank for Reg E and FDCPA purposes                         | Must maintain complaint log; escalate to bank within agreed SLA                  |

**Recent BaaS enforcement landscape:**

- **June 2023:** Fed/FDIC/OCC issued joint Interagency Guidance on Third-Party
  Relationships — lifecycle risk management framework covering BaaS partnerships
- **July 25, 2024:** Fed/FDIC/OCC Joint Statement specifically on bank-fintech deposit
  arrangements, confirming bank's regulatory obligations cannot be delegated to fintechs
- **2024 consent orders (named banks):** Axiom Bank (OCC — halt on new partnerships),
  Piermont Bank (FDIC — inadequate controls), Sutton Bank (FDIC — AML outsourcing),
  Cross River Bank (FDIC — CDD and transaction monitoring deficiencies)
- **OCC formal enforcement actions in 2024:** 36 — more than triple 2023 volume; more
  than half related to BaaS or third-party risk [VERIFY final 2024 tally]
- **Key operational risk:** Bank partner receives regulatory action → fintech programme
  suspended or terminated; retroactive transaction lookbacks required in ~79% of cases
- **Synapse Financial Technologies (Chapter 11, April 2024):** The most consequential
  BaaS failure to date. Synapse was a middleware provider connecting ~120 fintech customers
  (2M active users) to partner banks including Evolve Bank & Trust and Lineage Bank. Its
  bankruptcy caused ~$265M in customer funds to be frozen and exposed an ~$85M shortfall
  due to batch reconciliation discrepancies between Synapse's ledger and bank records.
  **FDIC proposed "Synapse Rule" (October 2024):** Would require BaaS banks to maintain
  accurate, real-time beneficial owner recordkeeping for all custodial/FBO accounts.
  [VERIFY: whether FDIC final rule has been issued as of assessment date]

**BaaS Contract Requirements Checklist:**

- [ ] Clear allocation of BSA/AML programme ownership and responsibilities
- [ ] Transaction monitoring architecture and SAR filing process defined
- [ ] Onboarding / KYC standards aligned with bank's CIP programme
- [ ] Fintech represented as bank's agent for regulatory purposes (where applicable)
- [ ] FDIC insurance disclosure obligations and prohibitions defined
- [ ] Regulation E error resolution process and SLAs specified
- [ ] Consumer complaint escalation process and SLAs
- [ ] Audit rights: bank can examine fintech's systems, records, and programme
- [ ] Programme suspension rights: bank can suspend fintech programme for compliance failure
- [ ] Termination provisions: reasonable wind-down period; data portability
- [ ] Indemnification for fintech-caused regulatory actions
- [ ] UDAAP review: bank must approve fintech marketing and disclosure materials
- [ ] Sub-servicer provisions: fintech obligations if bank is acquired or loses FDIC cover

#### D. US Open Banking — CFPB Section 1033

The CFPB finalised the Personal Financial Data Rights rule under Dodd-Frank § 1033 on
22 October 2024. The rule covered data providers (banks, credit unions, card issuers,
and digital wallet providers above the $850M asset threshold) with phased compliance
dates from April 2026 through April 2030 by asset size.

**Current legal status (as of early 2026): The rule is STAYED pending litigation.**
Bank trade associations filed suit in the Eastern District of Kentucky challenging the
rule. The court granted a stay in July 2025. The CFPB issued an ANPR in August 2025
with 36 questions and has indicated intent to substantially revise the rule, citing
concerns about the original rule's scope. Original compliance timelines are suspended.

The rule would require covered data providers to:

- Provide consumers with access to 24 months of account and transaction data
- Authorise third-party data recipients certified under the rule's standards
- Restrict data use to the authorised purpose; honour revocation at any time
- Renew consumer authorisation annually

[JURISDICTION-SPECIFIC] The underlying statutory authority (Dodd-Frank § 1033) remains
in force regardless of the rulemaking status. Monitor CFPB's revised rulemaking closely —
the regulatory obligation exists; the implementation details are contested. Third-party
fintechs accessing consumer financial data should track whether the ANPR results in
narrower or broader third-party authorisation requirements than the stayed rule.

---

### UK Framework

#### A. FCA Authorisation — Payments and E-Money

All firms providing payment services in the UK must be either authorised or registered
with the FCA under the Payment Services Regulations 2017 (PSRs 2017), implementing
PSD2 in the UK. Firms issuing electronic money must be authorised or registered under
the Electronic Money Regulations 2011 (EMRs 2011).

**Licence types and thresholds** [VERIFY: FCA published thresholds; may be updated]:

| Licence                                   | Activity                                         | Threshold                                  | Key Obligations                                                                                                     |
| ----------------------------------------- | ------------------------------------------------ | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| **Authorised Payment Institution (API)**  | Full payment services without transaction limits | None                                       | Full FCA authorisation; safeguarding all relevant funds; £125,000 initial capital (varies by service type) [VERIFY] |
| **Small Payment Institution (SPI)**       | Payment services below threshold                 | Monthly payment transactions ≤ €3M average | Registration (not authorisation); lighter requirements; no passporting; cannot use agent network broadly            |
| **Authorised E-Money Institution (AEMI)** | Issuance of e-money                              | None                                       | Full FCA authorisation; safeguarding e-money funds; £350,000 initial capital [VERIFY]                               |
| **Small E-Money Institution (SEMI)**      | E-money issuance below threshold                 | Average outstanding e-money ≤ €5M          | Registration; no passporting; limited agent use                                                                     |

**Safeguarding requirements — Strengthened Regime [FCA PS25/12, effective 7 May 2026]:**
FCA Policy Statement PS25/12 (published 7 August 2025) introduces the most significant
overhaul of safeguarding since inception:

- All authorised PIs and AEMIs must appoint a qualified auditor for an annual safeguarding
  audit (exemption: firms that have not had to safeguard more than £100,000)
- Monthly safeguarding return to FCA required, due within 15 business days of month-end
  (reconciliations, shortfalls, breaches, account details)
- Defined list of eligible secure liquid assets for safeguarded funds (certain government
  securities, qualifying UCITS funds)
- Insurance/guarantee method: policy must be replaced at least 3 months before expiry;
  if no replacement with less than 3 months remaining, firm must switch to segregation
- Context: ~£26 billion held in safeguarded e-money accounts in the UK in 2024

**Pre-PS25/12 safeguarding requirements** [PSRs 2017, Reg. 23; EMRs 2011, Reg. 20]:

- Relevant funds must be segregated in a safeguarding account at an authorised credit
  institution or insured in an insurance policy
- The PS25/12 enhanced regime applies from 7 May 2026 — verify current obligations if
  assessing a firm pre- vs. post-implementation date

**Post-Brexit passporting:**
The UK left the EU single market on 31 December 2020. UK-authorised payment institutions
can no longer passport services into the EEA, and EEA-authorised firms cannot passport
into the UK. Firms operating in both markets require separate UK and EU authorisations.

**FCA Regulatory Sandbox:**
The FCA operates a regulatory sandbox allowing eligible firms to test innovative products
under a bespoke regulatory framework with restricted authorisation and consumer
safeguards. Eligibility requires: genuine innovation, consumer benefit, regulatory
challenge requiring sandbox (product would not be possible under existing rules or
requires testing before committing to full authorisation).

[JURISDICTION-SPECIFIC] A separate Digital Sandbox provides a testing environment
with synthetic data for firms at an earlier development stage. Sandbox cohorts are
periodically open for applications.

#### B. UK Open Banking

The UK Open Banking framework was established by the Competition and Markets Authority
(CMA) Order in 2016 and implemented through the FCA's PSRs 2017 (open banking
provisions). It requires the nine largest current account providers (CMA9) to provide
APIs enabling third-party access to customer data and payment initiation.

[JURISDICTION-SPECIFIC] The Joint Regulatory Oversight Committee (JROC), comprising
the FCA and PSR, oversees the transition of Open Banking. 11.7 million active open
banking users as of late 2025; Variable Recurring Payments (VRPs) accounted for 16%
of all open banking payments as of November 2024. HM Treasury legislation expected in
2026 to grant FCA formal open banking rulemaking powers. The FCA will consult on a
Long-Term Regulatory Framework for open banking before end of 2026. The Data (Use and
Access) Act is expected to extend open banking principles to other financial sectors
("smart data"). [VERIFY: whether HM Treasury legislation has been introduced as of
assessment date; current JROC roadmap milestones.]

**FCA Consumer Duty** [PRIN 12; in force]:

- Open products and services: **31 July 2023**
- Closed products and services: **31 July 2024**
- First Board Annual Consumer Outcomes Report due: **31 July 2024**
- Applies to all FCA-regulated firms across the distribution chain that can influence
  any material aspect of a retail product or service — including PIs, AEMIs, fintech
  lenders, and (per 2025 FCA consultation) crypto-asset firms
- Four required outcomes: products/services suitability; price and value; consumer
  understanding; consumer support
- Board must annually review and approve a Consumer Outcomes Report
- Consumer Duty is an ongoing obligation — not a one-time exercise

---

### EU Framework

#### A. PSD2 Licensing (Current Framework)

Payment Services Directive 2015/2366 (PSD2) is transposed into national law across EU
member states. Authorisation is granted by National Competent Authorities (NCAs) and
carries passport rights across the EEA.

**PSD2 licence types:**

| Licence                                         | Activity                                                                                                                                   | Key Requirements                                                                                  |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| **Payment Institution (PI)**                    | Executing payment transactions, issuing payment instruments, acquiring payment transactions, money remittance, payment initiation services | Authorisation by NCA; capital requirements; safeguarding; passporting available                   |
| **E-Money Institution (EMI)**                   | Issuing electronic money + payment services                                                                                                | EMD2 authorisation; capital €350,000 initial [VERIFY]; safeguarding; passporting                  |
| **Account Information Service Provider (AISP)** | Accessing payment account information only (read-only)                                                                                     | Lighter authorisation or registration; no safeguarding; professional indemnity insurance required |
| **Payment Initiation Service Provider (PISP)**  | Initiating payments from user accounts held at ASPSPs                                                                                      | Authorisation required; professional indemnity insurance; no holding of funds                     |
| **Credit Institution**                          | All of the above plus deposit-taking                                                                                                       | Full banking licence; CRD VI / CRR III capital requirements                                       |

**Strong Customer Authentication (SCA):**
PSD2 requires SCA for online payment initiation and account access [VERIFY: RTS on SCA
and Common and Secure Communication — Commission Delegated Regulation (EU) 2018/389].
SCA requires at least two of: something the customer knows, something the customer has,
something the customer is. Exemptions: low-value (≤ €30 per transaction, ≤ €100
cumulative or ≤ 5 consecutive transactions), low-risk transactions (Transaction Risk
Analysis), trusted beneficiaries, recurring transactions [VERIFY].

#### B. PSD3 / PSR Transition

**Current status:** Provisional political agreement reached 27 November 2025. Official
Journal publication expected end of Q2 2026. **Not yet in force.** [VERIFY: Official
Journal citation once published]

**Anticipated timeline:**

- PSR application date: ~18 months after entry into force (estimated late 2027 / early 2028)
- PSD3 transposition deadline: 18 months after entry into force
- Payee-name/IBAN verification obligation: 24 months after entry into force
- Existing PI/EMI authorisations remain valid for 24 months (extendable to 30 months);
  re-authorisation required within that window [VERIFY on final text]

**Key changes from PSD2:**

- **PSR is a Regulation** (directly applicable, no transposition variability — eliminates
  the regulatory arbitrage created by uneven PSD2 national implementation)
- **EMD2 absorbed:** EMIs become a sub-type of payment institution; must re-apply as
  "payment institutions authorised to issue e-money." EMD2 is repealed.
- **Fraud liability tightened:** Payee-name/IBAN matching mandatory; failure to implement
  creates direct liability for misdirected payments. Impersonation fraud reimbursement
  mandated for certain categories.
- **Open banking more prescriptive:** Enumerated prohibited API obstacles; mandatory
  performance standards for dedicated interfaces; EBA guidelines on interface criteria.
- **SCA accessibility mandate:** At least one SCA method suitable for customers without
  smartphones, with disabilities, or low digital literacy.
- **MiCA intersection:** Simplified authorisation pathway for providers already MiCA-licensed.

[JURISDICTION-SPECIFIC] PSD2 remains current law until PSD3 transposition deadline.
Assess firms against PSD2 now; build transition roadmap for PSD3/PSR once final text
confirmed. [VERIFY: Official Journal citation and exact application dates on publication]

#### C. EU MiCA — Markets in Crypto-Assets Regulation

Regulation (EU) 2023/1114 (MiCA) entered into force on 29 June 2023, with full
application from 30 December 2024 (titles III/IV, covering ART and EMT issuers, applied
from 30 June 2024) [VERIFY current application dates].

**MiCA asset classification:**

| Category                         | Description                                                                     | Key Requirements                                                                                            |
| -------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **E-Money Token (EMT)**          | Crypto-asset referencing a single official currency                             | Must be issued by an authorised credit institution or AEMI; subject to EMD2-equivalent rules; MiCA Title IV |
| **Asset-Referenced Token (ART)** | Crypto-asset referencing other assets (basket of currencies, commodities, etc.) | Requires ART issuer authorisation from NCA; significant ART rules; MiCA Title III                           |
| **Utility Token**                | Provides access to goods/services of issuer only                                | Whitepaper requirement; no financial licence typically required                                             |
| **Other crypto-assets**          | Crypto-assets not qualifying as financial instruments, EMT, or ART              | Whitepaper; lighter regime                                                                                  |

**CASP (Crypto-Asset Service Provider) licensing:**
Firms providing crypto-asset services (custody, operation of trading platforms, exchange,
portfolio management, advice, transfer services) require CASP authorisation from an NCA
[VERIFY: MiCA Article 59 et seq.]. CASP authorisation carries EEA passport rights.

**MiCA grandfathering [Article 143 MiCA]:** Entities providing crypto-asset services
under applicable national law before 30 December 2024 may continue until a maximum of
1 July 2026 (or until authorisation granted/refused). However, grandfathering periods
vary significantly by member state:

| Status                                                                       | Member States                                                      |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Transitional period already expired** (full MiCA compliance mandatory now) | Netherlands, Finland, Latvia, Lithuania, Hungary, Poland, Slovenia |
| **12-month transitional period** (expiring ~December 2025)                   | Germany, Ireland, Greece, Spain, Liechtenstein                     |
| **Longer periods (up to July 2026 maximum)**                                 | Other member states (verify per state)                             |

[VERIFY current grandfathering status per member state — firms operating in multiple
EU member states must check each state where they operate, not just home state.]

Over 102 CASP licences issued across the EU as of December 2025; ESMA maintains public
CASP register. Netherlands and Germany issued the first licences on 30 December 2024 /
mid-January 2025 respectively. ESMA's CASP authorisation taxonomy (iXBRL whitepaper
format) effective 23 December 2025.

**CASP minimum capital requirements [MiCA Article 62] [VERIFY against final ESMA RTS]:**

| CASP Activity                                   | Minimum Capital              |
| ----------------------------------------------- | ---------------------------- |
| Advisory and analysis services                  | €50,000                      |
| Custody/administration or exchange against fiat | €125,000                     |
| Operating a trading platform                    | €150,000                     |
| Multiple services                               | Highest applicable threshold |

**Significant CASP (sCAP) designation:** Triggered automatically when average annual
active EU users exceed 15 million. Subject to direct ESMA oversight and heightened
supervision. Non-EU providers restricted to reverse solicitation only — cannot actively
market to EU residents without authorisation.

#### D. DORA — Digital Operational Resilience Act

Regulation (EU) 2022/2554 (DORA) applies from 17 January 2025 [VERIFY]. It covers ICT
risk management, incident reporting, operational resilience testing, and third-party ICT
risk management for regulated financial entities.

**DORA applicability to fintechs:**
DORA applies to "financial entities" as defined in Article 2, including: credit
institutions, payment institutions, e-money institutions, investment firms,
crypto-asset service providers (under MiCA), and ICT third-party service providers
that serve financial entities.

Non-regulated fintechs that provide ICT services to regulated financial entities are
subject to DORA as "ICT third-party service providers" and may be designated as
"critical ICT third-party service providers" subject to direct oversight by ESAs.

**Key DORA obligations for regulated fintechs:**

- ICT risk management framework (Article 5-15)
- Classification and reporting of major ICT incidents to NCA (Article 19-23): major
  incident initial report within 4 hours; intermediate within 72 hours; final within
  one month [VERIFY specific timelines]
- Digital operational resilience testing: TLPT (Threat-Led Penetration Testing) for
  larger entities
- Third-party ICT risk register and contractual requirements (Article 28-30)

---

### Singapore Framework

#### A. Payment Services Act 2019 (PSA) — Licence Tiers

The MAS Payment Services Act 2019 (amended 2021) establishes a three-tier licensing
framework for payment service providers.

**Seven regulated payment services:**

| Payment Service                      | Description                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------- |
| Account issuance                     | Issuing payment accounts (e-wallets, stored-value accounts)                     |
| Domestic money transfer              | Transferring money between accounts within Singapore                            |
| Cross-border money transfer          | Transmitting money internationally                                              |
| Merchant acquisition                 | Processing merchant payments                                                    |
| E-money issuance                     | Issuing electronic money (redeemable against value stored)                      |
| Digital payment token (DPT) services | Buying/selling, exchanging, or facilitating transfer of DPTs (cryptocurrencies) |
| Money-changing                       | Changing physical currency                                                      |

**Licence tiers:**

| Licence                                | Scope                                    | Key Thresholds [VERIFY]                                                           | Capital Requirement [VERIFY] |
| -------------------------------------- | ---------------------------------------- | --------------------------------------------------------------------------------- | ---------------------------- |
| **Money-Changing Licence**             | Money-changing only                      | N/A                                                                               | S$100,000                    |
| **Standard Payment Institution (SPI)** | Any payment service(s), below thresholds | Monthly transactions ≤ S$3M (per service type) OR stored value outstanding ≤ S$5M | S$100,000                    |
| **Major Payment Institution (MPI)**    | Any payment service(s); no thresholds    | Above SPI thresholds                                                              | S$250,000                    |

**DPT-specific requirements [MAS PS-G01, revised August 26, 2024]:**
DPT services require MPI licence (not SPI). Key requirements from revised MAS Guidelines:

- **Legal opinion:** All new applications adding DPT services must submit opinion from
  a qualified Singapore law firm assessing whether services are regulated under PSA
- **External auditor assessment:** Qualified independent auditor must assess AML/CFT and
  consumer protection policies; report due within 3 months of application
- **In-house compliance officer:** DPT compliance officer must be in-house in Singapore
  — cannot be outsourced (key practical constraint for foreign entrants)
- **Fit and proper:** Enhanced proactive demonstration of honesty, integrity, reputation,
  and financial soundness required for DPT applicants
- Firms providing DPT services implement: AML/CFT per MAS Notice PSN02 (full CDD, EDD,
  transaction monitoring, Travel Rule compliance for DPT transfers, STRO reporting),
  technology risk management per MAS Technology Risk Management Guidelines

**Note:** PSA 2019 expanded scope of regulated activities effective 4 April 2024.
Entities that were providing DPT services before this date under transitional provisions
were required to submit external auditor attestation by 4 January 2025 — failure to do
so is a potential enforcement risk.

**MAS Regulatory Sandbox (three tiers):**

- **Standard Sandbox:** Application reviewed within 21 days; regulated activities relaxed
  for sandbox duration; defined space and exit deadline
- **Sandbox Express:** Fast-track entry within 21 days using pre-defined parameters
  [VERIFY: currently available templates as of assessment date]
- **Sandbox Plus (2022):** Enhanced assistance including grants up to S$500,000 (50%
  co-funding), deal-making platform, simplified application; grant disbursed over three
  tranches during and after sandbox period

**Eligibility for all sandbox tiers:**

- Genuine fintech innovation in Singapore's financial ecosystem
- Ability to contain risk during sandbox period
- Intent and ability to apply for the full licence upon exiting the sandbox

**Key risk:** The sandbox does not authorise commercial-scale operations and has a fixed
exit deadline. Operating past sandbox expiry without a full licence application is
a CRITICAL compliance gap.

#### B. Singapore DTSP Regime (Offshore-Focused Crypto)

Effective **30 June 2025**, the Financial Services and Markets Act 2022 (FSMA) established
a separate Digital Token Service Provider (DTSP) licensing regime for firms providing
digital token services **exclusively to overseas customers** from a Singapore base of
operations [VERIFY: FSMA 2022, effective date of DTSP regime].

- Minimum base capital: **S$250,000**
- MAS has signalled it will "generally not issue a DTSP licence" for business models
  where substantive activity is entirely offshore (AML/CFT risk is higher; MAS cannot
  effectively supervise offshore customer conduct)
- This regime closes the regulatory gap for offshore-only crypto service providers with
  Singapore nexus who previously fell outside PSA scope

**Key risk:** Fintechs operating crypto services from Singapore targeting only overseas
customers must assess DTSP applicability — this is not a carve-out from regulation, it
is a separate licensing pathway with its own requirements.

---

## Severity Classification

### CRITICAL — Immediate Action Required

Operating without required licence or registration. Involves criminal exposure, cease-and-
desist risk, or potential loss of ability to operate. Regulatory action is imminent or
already underway.

**Examples:**

- Money transmission operations in a state without an MTL or applicable exemption
- Providing payment services in the UK without FCA authorisation/registration
- Offering CASP services in the EU after MiCA application date without CASP authorisation
- Providing DPT services in Singapore without MPI licence
- Representing consumer funds as FDIC-insured when they are not
- Operating without any BSA/AML programme as a registered MSB

**Action**: Cease the activity or obtain legal authority immediately. Present options for
emergency remediation. Consult outside counsel before continuing operations.

### NON-COMPLIANT — Material Gap Requiring Prompt Remediation

Activity is technically possible but one or more material regulatory requirements are not
met. No immediate criminal exposure, but regulatory examination would find deficiencies.
Enforcement risk is elevated.

**Examples:**

- MSB registered with FinCEN but AML programme is incomplete or untested
- FCA-authorised but safeguarding arrangements are deficient
- PSD2 SCA implementation missing required exemptions or authentication factors
- BaaS partnership operating without a written programme agreement or audit rights
- MAS-licensed DPT firm with inadequate AML/CFT controls per PSN02
- DORA-covered firm without incident classification and reporting process

**Action**: Develop and implement remediation plan within 3-6 months. Track against
regulatory examination cycle.

### PARTIAL — Partially Compliant

Regulatory requirements are partially met. Core framework is in place but specific
provisions are missing or inadequate. Lower risk but not fully defensible.

**Examples:**

- MTL obtained in major states; expansion states not yet covered
- BaaS contract has most required provisions; some SLAs and audit rights missing
- CASP licence application in progress; grandfathering period not yet expired
- Section 1033 compliance in progress; technical interface not yet implemented

**Action**: Identify and close specific gaps. Timeline depends on regulatory deadline
and examination risk.

### COMPLIANT — Meets Requirements

The identified regulatory requirements are met. No immediate action required. Ongoing
monitoring to track regulatory developments.

**Action**: Confirm through periodic monitoring. Schedule next review against regulatory
update cycle.

---

## Actionable Output Per Finding

For each finding, provide:

```
**Finding**: [description of the compliance gap or status]
**Jurisdiction**: [US / UK / EU / SG / Multiple]
**Severity**: [CRITICAL / NON-COMPLIANT / PARTIAL / COMPLIANT]
**Regulatory basis**: [specific statute, regulation, or regulatory guidance — or [VERIFY]]
**Confidence**: [Definite / High / Probable / Possible / Unlikely]
**Impact**: [what the regulatory consequence is if not addressed]
**Remediation**: [specific steps to achieve compliance]
**Complexity**: [Simple (days-weeks) / Moderate (weeks-months) / Complex (months-years)]
**Dependencies**: [other workstreams, third parties, or regulatory approvals required]
```

---

## Prioritisation Framework

### Tier 1 — CRITICAL / BLOCKING

Must resolve before launch or continued operation:

- Operating without a required licence or registration
- Missing BSA/AML programme for registered MSB
- FDIC deposit insurance misrepresentation
- Criminal exposure under any jurisdiction's money transmission or banking laws
- Regulatory cease-and-desist or enforcement action underway
- DORA major incident not reported within required timeline

**Strategy**: Stop the activity. Engage outside regulatory counsel. Pursue emergency
remediation or interim regulatory authorisation.

### Tier 2 — MATERIAL

Resolve within 3-6 months:

- MTL gap for expansion states (if current states operational)
- Deficient BSA/AML programme elements (incomplete but programme exists)
- BaaS contract missing material provisions
- FCA safeguarding arrangements not fully documented
- MiCA CASP licence application not yet submitted (within grandfathering window)
- DORA ICT risk management framework not yet documented

**Strategy**: Prioritise against regulatory examination calendar. Build internal
compliance capability or engage specialist compliance consultants.

### Tier 3 — REMEDIATE

Address in next compliance cycle (6-12 months):

- MTL expansion into lower-priority states
- BaaS contract refinements and SLA optimisation
- AISP/PISP professional indemnity insurance adequacy review
- MAS sandbox exit and full licence application
- Section 1033 interface optimisation
- DORA TLPT scheduling

**Strategy**: Include in annual compliance roadmap. Assign ownership and track.

---

## Citation Quality Gates

Run silently before delivering any output. Revise if any gate fails.

| Gate           | Rule                                                                                                                                                    | Fail Action                                                                                    |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Source**     | Every regulatory claim cites a specific statute, regulation, regulatory notice, or established principle                                                | Add citation or mark "[UNVERIFIED — counsel to confirm]"                                       |
| **Format**     | All citations follow a consistent format for the jurisdiction (e.g., "31 CFR § 1022.210" for US; "PSRs 2017, Reg. 23" for UK; "MiCA Article 59" for EU) | Fix format                                                                                     |
| **Currency**   | Fintech regulation changes rapidly — every cited threshold, date, and requirement should be flagged for current verification                            | Flag "[CHECK CURRENCY — this area changes frequently; verify against current regulatory text]" |
| **Domain**     | Analysis stays within the identified jurisdictions. No assumption that compliance in one jurisdiction satisfies another                                 | Remove or flag cross-jurisdictional bleed                                                      |
| **Confidence** | Uncertainty explicitly stated, not hidden — particularly for thresholds, dates, and recent regulatory changes                                           | Add confidence qualifier; mark with [VERIFY]                                                   |

---

## Self-Interrogation for CRITICAL Items

For any item classified as CRITICAL, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**: Does the CRITICAL classification follow from the
cited regulatory authority? Would the relevant regulator actually take enforcement action
on these facts? Is there a credible exemption or safe harbour that hasn't been considered?

**Pass 2 — Completeness**: Have all relevant statutory frameworks been considered? Is
there an overlapping federal / state / supranational authority that modifies the analysis?
Has recent regulatory guidance or enforcement action been checked?

**Pass 3 — Challenge**: What is the strongest argument that this activity is actually
compliant? Under what circumstances might a reasonable regulatory counsel advise a
different classification? Is CRITICAL proportionate, or is NON-COMPLIANT more accurate
given the timeline and enforcement risk?

If any pass reveals a weakness, revise before delivery. Mark the audit trail with
`self_interrogation: PASS` or `self_interrogation: REVISED`.

---

## Confidence Scoring

| Level        | Range     | Meaning                                                                          | Action                                                           |
| ------------ | --------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Definite** | 0.95-1.0  | Established regulatory requirement; black-letter law                             | State with confidence                                            |
| **High**     | 0.80-0.94 | Well-established requirement; minor interpretation questions at the margins      | State with brief caveat                                          |
| **Probable** | 0.60-0.79 | Likely requirement; regulatory position not fully settled or threshold uncertain | State with reasoning; note contra-indicators                     |
| **Possible** | 0.40-0.59 | Genuinely uncertain; regulatory perimeter unclear or novel product               | Flag for counsel review; present both sides                      |
| **Unlikely** | 0.0-0.39  | Weak basis; speculative regulatory risk                                          | Do not assert; flag "[UNCERTAIN — regulatory counsel to advise]" |

---

## Glass Box Audit Trail

Every assessment output MUST include a Glass Box audit section:

```yaml
glass_box:
  skill_name: "legalcode-fintech-regulatory-assessment"
  assessment_subject: "[Company name or project]"
  business_model: "[Description of activities assessed]"
  jurisdictions_assessed:
    - "[US / UK / EU / SG — and specific activities in each]"
  current_licences: "[what the company currently holds]"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "[Statute — VERIFIED (legalcode-mcp) or UNVERIFIED]"
  enforcement_actions_reviewed: "[yes / no — sources]"
  findings_count:
    critical: "[number]"
    non_compliant: "[number]"
    partial: "[number]"
    compliant: "[number]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "Fintech regulation changes rapidly — all thresholds and dates require verification against current regulatory text"
    - "[Any scope limitations or assumptions]"
  reviewer: "AI-assisted — requires qualified financial services regulatory counsel review"
```

---

## Anti-Patterns

What NOT to do in fintech regulatory assessment:

1. **Assuming MSB registration = state MTL compliance** — FinCEN MSB registration is a
   federal BSA/AML obligation. It does not substitute for state money transmission
   licences, which are separate, state-by-state requirements. Operating without state
   MTLs while relying solely on MSB registration is a common and serious error.

2. **Treating the agent-of-payee exemption as universally available** — This exemption
   exists in some US states but is interpreted narrowly and differs across jurisdictions.
   It cannot be relied upon without a written legal opinion per state confirming the
   specific product satisfies the exemption conditions.

3. **Assuming post-Brexit UK passporting still works** — UK-authorised payment
   institutions lost EEA passporting rights on 31 December 2020. Firms that rely on
   historical EU authorisation for UK operations, or vice versa, have a critical
   compliance gap.

4. **Conflating e-money with uninsured deposits** — E-money is not a bank deposit and
   is not FDIC-insured (US) or FSCS-protected (UK). Representing it as such, or as
   "bank-like" without clear disclosures, creates UDAP/UDAAP exposure in the US and
   FCA enforcement risk in the UK.

5. **Ignoring state MTL requirements for crypto exchanges** — Several states treat
   crypto-to-fiat exchanges and even crypto-to-crypto exchanges as money transmission.
   The New York BitLicense is separate from and in addition to the MTL. Not all states
   have clear guidance; treating ambiguity as exemption is not a defence.

6. **Underestimating BaaS regulatory accountability** — The fintech partner is not the
   regulated entity in a BaaS model, but it bears significant compliance obligations
   through its programme agreement with the bank. A bank that fails its BSA/AML
   examination may suspend or terminate the fintech programme, causing operational
   disruption regardless of the fintech's own compliance quality.

7. **Relying on grandfathering without verifying dates** — MiCA grandfathering
   provisions vary by member state and expire on different dates. Operating past the
   grandfathering deadline without a CASP application on file is a CRITICAL gap.

8. **Assuming MiCA covers all crypto products** — MiCA covers crypto-assets that are not
   financial instruments under MiFID II, e-money under EMD2, or deposits under CRD. NFTs
   may or may not fall within MiCA depending on their structure. DeFi protocols that are
   not "issuers" or "providers" may be outside MiCA for now. Verify the specific product's
   classification before asserting MiCA applicability or non-applicability.

9. **Ignoring DORA as a "banks only" regulation** — DORA applies to payment institutions,
   e-money institutions, and MiCA-regulated CASPs, not just credit institutions. A licensed
   fintech that has not implemented ICT risk management and incident reporting frameworks
   is non-compliant with DORA.

10. **Treating all Singapore DPT activities equally** — The MAS has progressively
    tightened DPT service requirements. Not all crypto activities require an MPI licence,
    and the MAS sandbox does not provide indefinite protection. Verify the specific DPT
    services against current MAS guidance and PSA licence category requirements.

11. **Using NMLS multistate licensing as a substitute for state legal analysis** — NMLS
    streamlines the administrative process of applying for MTLs in multiple states. It
    does not homogenise state law requirements. Each state's MTL statute, capital
    requirements, and permissible investment rules must still be reviewed separately.

12. **Ignoring Section 1033 as a "data compliance" issue only** — The CFPB's Personal
    Financial Data Rights rule creates substantive obligations on both data providers and
    data recipients. Fintechs accessing consumer financial data must be authorised data
    recipients under the rule's framework, not just data providers.

13. **Assuming ILC exempts a fintech from BHCA** — The ILC charter exempts the
    commercial parent from the Bank Holding Company Act in most cases, but this is a
    complex area with pending regulatory scrutiny. Do not assume BHCA non-applicability
    for ILC owners without specific legal advice.

14. **Single-point-in-time analysis** — Fintech regulation is one of the most rapidly
    evolving areas of financial services law. An assessment that was current six months
    ago may be materially out of date. Build regulatory monitoring into the compliance
    programme rather than treating this assessment as perpetually valid.

15. **Treating the MAS sandbox as regulatory cover** — The MAS sandbox provides a
    controlled testing environment with specific regulatory relief. It does not authorise
    commercial-scale operations and has an exit deadline. Firms must apply for the full
    licence before sandbox expiry.

16. **Ignoring the FCA Consumer Duty for fintech products** — The FCA Consumer Duty
    (PS22/9), effective July 2023, applies to all FCA-authorised firms offering products
    or services to UK retail consumers. It imposes obligations on firms in the distribution
    chain, not just manufacturers, and requires ongoing outcomes monitoring — not a
    one-time compliance exercise.

---

## Writing Standards

Apply plain-language discipline to all assessment output:

**For regulatory findings** (may be shared with regulators or board):

- Active voice: "The company must obtain MTLs in each state where it transmits money"
  not "MTLs are required to be obtained by the company"
- Concrete actions: specify the regulator, the filing, the deadline
- Name the actor: "FinCEN requires..." not "It is required that..."
- Specific citations: reference the statute or regulation, not just the topic
- No jargon without definition on first use

**Quality gates before delivery:**

1. Can a non-lawyer founder understand the executive summary and the top three action items?
2. Can regulatory counsel verify every citation from the references provided?
3. Is every threshold, date, and requirement flagged [VERIFY] where not sourced from a verified authority?
4. Are any sentences vague, hedging, or ambiguous? If yes, fix.
5. Does the remediation roadmap include owners, timelines, and dependencies?

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- Search for current MTL requirements by state and relevant MAS/FCA/NCA guidance
- Verify regulatory thresholds (capital requirements, transaction limits, safe harbour limits)
- Search for recent enforcement actions that inform the severity of identified gaps
- Check for recent regulatory announcements affecting PSD3 transition, MiCA
  grandfathering, or DORA implementation
- Mark legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all specific thresholds, dates, and recent regulatory developments with [VERIFY]
- Rely on the Regulatory Framework Reference in this skill for structural analysis
- Recommend the user engage specialist regulatory counsel to verify specific requirements
  before taking action
- Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`

---

## Output Format Template

```markdown
## Fintech Regulatory Assessment

**Subject**: [Company name / project]
**Assessment Date**: [date]
**Business Model**: [summary]
**Jurisdictions**: [US / UK / EU / SG — and specific activities]
**Current Regulatory Status**: [what is currently held]
**Assessment Basis**: [legalcode-mcp + regulatory framework reference / framework reference only]

---

## Executive Summary

[3-5 sentence summary: critical findings, overall risk posture, top three action items]

---

## Regulatory Obligation Map

| Activity   | US Obligation | UK Obligation | EU Obligation | SG Obligation | Status   |
| ---------- | ------------- | ------------- | ------------- | ------------- | -------- |
| [activity] | [requirement] | [requirement] | [requirement] | [requirement] | [status] |

---

## Jurisdiction-by-Jurisdiction Assessment

### United States

#### Money Transmission

[Finding, severity, remediation]

#### Bank Charter / BaaS Structure

[Finding, severity, remediation]

#### BSA/AML Programme

[Finding, severity, remediation]

#### Open Banking (if applicable)

[Finding, severity, remediation]

### United Kingdom

#### FCA Authorisation Status

[Finding, severity, remediation]

#### Safeguarding

[Finding, severity, remediation]

#### Consumer Duty (if applicable)

[Finding, severity, remediation]

### European Union

#### Payment Services (PSD2 / PSD3)

[Finding, severity, remediation]

#### Crypto-Assets (MiCA)

[Finding, severity, remediation]

#### Digital Resilience (DORA)

[Finding, severity, remediation]

### Singapore

#### MAS Licensing

[Finding, severity, remediation]

#### DPT Services (if applicable)

[Finding, severity, remediation]

---

## BaaS Partnership Assessment (if applicable)

[Findings on BaaS structure, contract adequacy, regulatory accountability allocation]

---

## Remediation Roadmap

### Tier 1 — CRITICAL / BLOCKING (Immediate)

| Finding   | Jurisdiction   | Remediation | Owner   | Deadline   |
| --------- | -------------- | ----------- | ------- | ---------- |
| [finding] | [jurisdiction] | [steps]     | [owner] | [deadline] |

### Tier 2 — MATERIAL (3-6 months)

| Finding   | Jurisdiction   | Remediation | Owner   | Target Date |
| --------- | -------------- | ----------- | ------- | ----------- |
| [finding] | [jurisdiction] | [steps]     | [owner] | [target]    |

### Tier 3 — REMEDIATE (6-12 months)

| Finding   | Jurisdiction   | Remediation | Owner   | Target Date |
| --------- | -------------- | ----------- | ------- | ----------- |
| [finding] | [jurisdiction] | [steps]     | [owner] | [target]    |

---

## Licensing Pathway Recommendations

[For each jurisdiction requiring a new licence or registration, provide:]

**[Licence type]** — [Jurisdiction]

- **Eligibility**: [key eligibility criteria]
- **Timeline**: [typical processing time]
- **Capital requirement**: [amount — VERIFY against current requirements]
- **Key conditions**: [core ongoing obligations]
- **Alternative**: [if a BaaS or lighter-touch pathway is available]

---

## Next Steps

[Specific prioritised actions, with owners and timeframes]

---

## Glass Box Audit Trail

[YAML block per Glass Box section]
```

---

## Localization Notes

This skill covers four specific regulatory domains. When assessing a company operating
outside these four jurisdictions:

1. **Identify the applicable regulatory regime** using web research or legalcode-mcp
2. **Map the analogous licence types** (most payment regulation globally draws from
   FATF recommendations and internationally recognised frameworks)
3. **Use [JURISDICTION-SPECIFIC] markers** for jurisdiction-specific requirements
4. **Research recent enforcement actions** to calibrate severity classification
5. **Note explicitly** that the Regulatory Framework Reference in this skill does not
   cover the jurisdiction, and rely on sourced legal authority

Common adjacent jurisdictions not covered by this skill that may require separate
assessment: Canada (FINTRAC / provincial MSB + EMI), Australia (AUSTRAC + ASIC),
Hong Kong (HKMA / SFC + VATP licensing), UAE (CBUAE / DFSA / ADGM), Japan (FSA).

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis drawing on the Legalcode quality
framework established in `legalcode-contract-review`, adapted for multi-jurisdictional
fintech regulatory compliance assessment. Research basis: US BSA/AML regulatory framework
(FinCEN, OCC, FDIC, CFPB published guidance), UK FCA PERG (Perimeter Guidance manual)
and PS22/9 Consumer Duty, EU PSD2 (Directive 2015/2366), MiCA (Regulation 2023/1114),
DORA (Regulation 2022/2554), Singapore PSA 2019 and MAS published regulatory notices.
All specific thresholds, dates, and regulatory guidance should be verified against current
authoritative sources before use.
