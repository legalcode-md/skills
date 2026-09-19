---
name: legalcode-biometric-data-compliance
description: Assess biometric data privacy compliance across Illinois BIPA (740 ILCS 14), Texas CUBI (Tex.
  Use when auditing employer biometric timekeeping or access control programs, reviewing retail facial
  recognition deployments, assessing consumer device biometric authentication, evaluating healthcare or
  financial services biometric verification, analyzing vendor/processor contracts for biometric data,
  preparing for regulatory inquiry or class action exposure, or designing a biometric privacy program
  from scratch.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Assess biometric data privacy compliance across Illinois BIPA (740 ILCS 14), Texas CUBI (Tex. Bus. & Com. Code § 503.001), Washington My Health MY Data Act (HB 1155, 2024), California CCPA/CPRA sensitive PI framework, Colorado CPA (HB 24-1130, effective July 1, 2025), GDPR Article 9 special category processing, UK GDPR, and emerging US state laws (New York S1422 proposed, Massachusetts, Virginia, Connecticut biometric provisions). Covers: consent and written release requirements, written biometric data policy and retention/destruction schedules, sale and profit prohibitions, third-party disclosure controls, vendor/processor contractual obligations, individual rights response procedures, DPIA requirements for GDPR high-risk processing, FTC risk assessment standards, incident response obligations, and penalty exposure modeling. Use when auditing employer biometric timekeeping or access control programs, reviewing retail facial recognition deployments, assessing consumer device biometric authentication, evaluating healthcare or financial services biometric verification, analyzing vendor/processor contracts for biometric data, preparing for regulatory inquiry or class action exposure, or designing a biometric privacy program from scratch. Scope covers fingerprints, voiceprints, retina/iris scans, facial geometry templates, hand geometry, keystroke and gait patterns, and other biometric identifiers and biometric information derived therefrom. Related skills: legalcode-dpia-generator, legalcode-gdpr-legal-basis-assessment, legalcode-data-processing-agreement-drafter, legalcode-us-state-privacy-comparison, legalcode-vendor-privacy-assessment, legalcode-breach-response-checklist.


# Legalcode Biometric Data Compliance Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted biometric data compliance
> assessment. It does not constitute legal advice. All outputs must be reviewed by a qualified
> legal professional licensed in the relevant jurisdiction before use. Laws change rapidly in
> this area; verify current applicability — including the 2024 BIPA SB 2979 amendment, the
> 2025 Colorado HB 24-1130 effective date, and state legislative developments — before
> relying on any provision described here. Statutory citations and enforcement case references
> carry hallucination risk; verify against authoritative sources before relying on them.
> Biometric data is immutable — a data breach cannot be remedied by issuing new credentials.
> This makes compliance failures uniquely consequential.

## Purpose and Scope

This skill assesses an organization's biometric data practices against applicable privacy laws
and best practices, identifies compliance gaps, classifies findings by severity, and produces
an actionable remediation roadmap.

**Covers:**

- Applicability determination across all major US state biometric laws and GDPR/UK GDPR
- Written consent, notice, and written policy requirements (BIPA, CUBI, Washington, GDPR)
- Retention schedules, destruction obligations, and security requirements
- Sale, profit, and third-party disclosure prohibitions and controls
- Vendor and processor contract assessment (BIPA delegated liability; GDPR Article 28)
- Individual rights fulfillment (deletion, access, correction, portability)
- GDPR Article 9 lawful basis and Article 35 DPIA requirements
- FTC Act § 5 risk assessment obligations (2023 FTC Biometric Policy Statement)
- Penalty exposure modeling (BIPA per-violation damages; Texas AG civil penalties; GDPR fines)
- Incident response obligations for biometric data breaches

**Does not:**

- Draft biometric data policies from scratch (see legalcode-privacy-policy-drafter)
- Draft Data Processing Agreements (see legalcode-data-processing-agreement-drafter)
- Conduct Data Protection Impact Assessments (see legalcode-dpia-generator)
- Provide legal advice or replace qualified privacy counsel
- Cover non-biometric sensitive personal information comprehensively

## Jurisdiction and Governing Law

This skill is **multi-jurisdictional**. Biometric data compliance obligations are triggered by
the **location of the individuals whose data is collected**, not solely the organization's
headquarters. An employer headquartered in Texas but operating a biometric timekeeping system
for Illinois employees is subject to BIPA. A US company offering services to EU residents
must comply with GDPR Article 9.

**Primary frameworks assessed:**

| Framework                                    | Jurisdiction   | Key Trigger                                                              |
| -------------------------------------------- | -------------- | ------------------------------------------------------------------------ |
| BIPA (740 ILCS 14)                           | Illinois, US   | Biometric identifier/info of IL residents                                |
| CUBI (Tex. Bus. & Com. Code § 503.001)       | Texas, US      | Biometric identifiers collected for commercial purpose from TX residents |
| My Health MY Data Act (HB 1155)              | Washington, US | Consumer health data incl. biometrics from WA residents                  |
| CCPA/CPRA (Civil Code § 1798.100 et seq.)    | California, US | Biometric info as Sensitive PI of CA residents                           |
| Colorado CPA (HB 24-1130, eff. July 1, 2025) | Colorado, US   | Biometric identifiers of CO residents                                    |
| GDPR Article 9                               | EU/EEA         | Biometric data processed to uniquely identify EU/EEA residents           |
| UK GDPR + DPA 2018 Sch. 1                    | United Kingdom | Biometric data for identification of UK residents                        |
| FTC Act § 5                                  | US Federal     | Unfair/deceptive biometric practices by FTC-regulated entities           |

[JURISDICTION-SPECIFIC] Additional frameworks may apply:

- **New York S1422** (proposed; modeled on BIPA — monitor for enactment) [VERIFY current status]
- **Virginia CDPA** and **Connecticut CTDPA**: Biometric data as sensitive data category
- **Massachusetts proposed bills** (S.2608, HD.3523): BIPA-modeled, not yet enacted [VERIFY]
- **Michigan SB 359** (2025, not yet enacted) [VERIFY]
- **Arkansas Act 504**: Biometric data as personal information
- **DOJ Rule (Dec 2024)**: Restricts bulk transfers of biometric identifiers to covered foreign persons

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
context that would change the analysis, the workflow pauses and asks when:

- Jurisdictional applicability is unclear or straddles multiple frameworks
- The type of biometric data or collection method affects which law applies
- The organization's current compliance posture is unknown
- Enforcement risk classification depends on facts not yet provided

Use the **⟁ CLARIFY** pattern (structured options with descriptions) at the points marked
below. If the user has already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:

- **Policy documents**: Biometric data policy, privacy notice, employee consent forms
- **Contracts**: Vendor agreements, DPAs, service agreements involving biometric systems
- **Program description**: Description of the biometric system, its purpose, data types, jurisdictions
- **Prior assessment**: Previous compliance report or audit for gap analysis
- **No documents**: Conduct an intake-based assessment via the CLARIFY questions below

If no input is provided, begin with Step 2 to gather context.

### Step 2: Gather Context

**⟁ CLARIFY** — Ask these questions before beginning the assessment. Present as structured
options where possible. Skip questions already answered by the input.

1. **Assessment mode**: What is the primary objective?
   - **Full compliance audit**: Comprehensive multi-jurisdiction assessment against all applicable laws
   - **Gap analysis**: Identify gaps in an existing biometric program
   - **Applicability screening**: Determine which laws apply before building a program
   - **Vendor contract review**: Assess whether vendor agreements satisfy biometric law requirements
   - **Incident response**: Assess obligations following a biometric data incident or breach
   - **Litigation exposure**: Estimate class action and regulatory penalty exposure
   - _Why this matters_: Determines depth and focus of the assessment.

2. **Biometric data types collected** (select all that apply):
   - Fingerprints
   - Facial geometry / facial recognition templates
   - Retina or iris scans
   - Voiceprints / voice recognition
   - Hand geometry
   - Keystroke patterns / behavioral biometrics
   - Gait analysis
   - Other (describe)
   - _Why this matters_: Some laws define "biometric identifier" more narrowly than others
     (e.g., Texas CUBI covers specific types; GDPR requires data used for identification).

3. **Geography of individuals affected** (select all that apply):
   - Illinois residents → BIPA applicability
   - Texas residents → CUBI applicability
   - Washington state residents → My Health MY Data Act applicability
   - California residents → CCPA/CPRA applicability
   - Colorado residents → CPA HB 24-1130 applicability (effective July 1, 2025)
   - EU/EEA residents → GDPR Article 9 applicability
   - UK residents → UK GDPR applicability
   - Other US states → emerging law monitoring needed
   - _Why this matters_: Applicability is determined by the location of the data subjects,
     not the organization's domicile.

4. **Use case context** (select primary):
   - **Workplace** (employee timekeeping, access control, time-and-attendance)
   - **Consumer product** (device unlock, payment authentication, consumer app)
   - **Retail / surveillance** (facial recognition for customer tracking, loss prevention)
   - **Healthcare / clinical** (patient ID, biometric authentication for EHR access)
   - **Financial services** (KYC/AML verification, fraud prevention, authentication)
   - **Security / physical access** (building access, data center access)
   - **Background checks / identity verification**
   - **Multiple or other** (describe)
   - _Why this matters_: Workplace use implicates employment-law consent mechanics; retail
     facial recognition faces the strictest scrutiny; healthcare may have HIPAA interaction.

5. **Current compliance posture**:
   - **No program in place**: No written policy, no formal consent, no retention schedule
   - **Basic program**: Some consent forms, no formal policy or destruction procedures
   - **Partial program**: Written policy exists but lacks some required elements
   - **Mature program**: Full written policy, consent, destruction schedule, vendor contracts
   - **Prior incident or litigation**: Assessment in the context of a claim or investigation
   - _Why this matters_: Determines starting point for gap analysis and remediation depth.

6. **Third-party / vendor involvement**:
   - **No third parties**: All biometric processing done in-house
   - **Single vendor**: One third-party biometric system provider
   - **Multiple vendors**: Multiple providers across different systems
   - **Cloud/SaaS biometrics**: Biometric data sent to external cloud for processing
   - **Sub-processors**: Vendor uses sub-processors for biometric template storage/matching
   - _Why this matters_: BIPA § 15(b) consent requirements apply to disclosure to third
     parties; GDPR Article 28 requires DPAs with all processors.

### Step 3: Gather Legal Authority

Use **legalcode-mcp** to verify current statutory text and enforcement developments for the
applicable jurisdictions identified in Step 2.

**Research targets:**

- Current text of 740 ILCS 14 (BIPA), including SB 2979 amendment (signed August 2, 2024) [VERIFY]
- Texas Bus. & Com. Code § 503.001 (CUBI), including Meta $1.4B AG settlement (March 2025) [VERIFY]
- Washington My Health MY Data Act final rules (HB 1155; large entities March 31, 2024;
  small businesses June 30, 2024) [VERIFY]
- California Civil Code § 1798.100 et seq. (CCPA/CPRA); CPPA biometric enforcement guidance [VERIFY]
- Colorado CPA HB 24-1130 (biometric amendment; effective July 1, 2025) [VERIFY]
- GDPR Articles 4(14), 9, 22, 28, 35; ICO biometric data guidance (2024) [VERIFY]
- FTC Policy Statement on Biometric Information Technology (May 18, 2023) [VERIFY]
- Status of New York S1422 and other proposed state bills [VERIFY]

Save the most relevant results to `/tmp/legalcode-biometric-research.md`.

**If legalcode-mcp is not connected:**

- Mark all statutory citations with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — manual verification required"`
- Proceed using research embedded in this skill, but flag that authority has not been
  independently verified against the current text

### Step 4: Applicability Gate

Determine which frameworks apply based on the geography of individuals and data types
collected. Map each applicable framework to the relevant assessment domains.

**Applicability matrix:**

| Law         | Trigger                                                                             | Key Threshold                                                                      |
| ----------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| BIPA        | Any IL resident's biometric identifier or information                               | No revenue/size threshold; applies to any "private entity"                         |
| CUBI        | TX resident's biometric identifier for "commercial purpose"                         | No threshold; AG-only enforcement                                                  |
| WA MHMD     | WA consumer's "consumer health data" (incl. biometrics)                             | Revenue/volume thresholds apply; small business exemption [VERIFY]                 |
| CCPA/CPRA   | CA resident's biometric information as Sensitive PI                                 | Threshold: 100K consumers OR 25K consumers if 50% revenue from selling PI [VERIFY] |
| CO CPA      | CO resident's biometric identifier (effective July 1, 2025)                         | 100K consumers/year threshold [VERIFY]                                             |
| GDPR Art. 9 | Biometric data "processed for the purpose of uniquely identifying" EU/EEA residents | Territorial: offering goods/services to or monitoring EU/EEA persons               |
| UK GDPR     | Biometric data processed to identify UK residents                                   | UK establishment or UK targeting                                                   |
| FTC Act § 5 | Any US entity subject to FTC jurisdiction (not banks, common carriers, nonprofits)  | Risk-based; applies to unfair/deceptive practices                                  |

**⟁ CLARIFY** — If applicability is genuinely uncertain for any framework (e.g., the
organization is unsure whether it has Illinois employees, or whether its EU operations
involve biometric identification), ask:

- "Does your workforce or customer base include individuals located in [state/country]?
  Even a single Illinois employee using a biometric timekeeping system triggers BIPA."
- "Does your biometric system use data to uniquely identify individuals, or only for
  authentication (1:1 match)? GDPR Article 9 applies where the purpose is unique
  identification; authentication-only use may fall outside Article 9 [VERIFY with ICO
  guidance — the line is contested]."

### Step 5: Domain 1 — Biometric Data Inventory and Program Governance

Assess whether the organization has a foundational governance structure:

**5.1 Biometric Data Inventory**

- [ ] All biometric data types collected identified and documented
- [ ] All systems, applications, and processes collecting biometric data mapped
- [ ] All vendors and processors with access to biometric data identified
- [ ] Data flows documented (collection → storage → processing → transmission → destruction)
- [ ] Geographic scope of collection documented (which states/countries)
- [ ] Legal entities (parent, subsidiaries, affiliates) sharing or accessing biometric data identified

**5.2 Written Biometric Data Policy (BIPA § 15(a) — mandatory)**

- [ ] Written biometric data retention and destruction policy exists
- [ ] Policy is publicly available (posted on website or accessible to affected persons)
- [ ] Policy specifies: (a) what biometric data is collected; (b) the specific purpose
- [ ] Policy specifies: (c) the retention schedule for each data type/purpose
- [ ] Policy specifies: (d) destruction timeline (BIPA: whichever is first — (i) original
      purpose satisfied OR (ii) 3 years after last interaction with individual)
- [ ] Policy specifies: (e) guidelines for destruction (secure deletion/destruction method)
- [ ] Policy updated at least annually or upon material change in collection practices

**5.3 Data Minimization and Purpose Limitation**

- [ ] Biometric data collected only for the stated, specific purpose
- [ ] No secondary use of biometric data beyond original purpose without new consent
- [ ] Data retention is actually limited as stated in policy (no indefinite storage)
- [ ] Biometric templates stored separately from identifying information where possible
- [ ] Ephemeral processing used where possible (verify and discard rather than store)

**Classification**: Apply COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY.

### Step 6: Domain 2 — Consent and Notice Requirements

Assess compliance with consent and notice requirements for each applicable jurisdiction.

**6.1 BIPA Consent (740 ILCS 14/15(b)) — Illinois**

- [ ] Written release (or electronic signature; SB 2979 clarified e-signatures accepted as
      of August 2, 2024) obtained BEFORE collection or disclosure of biometric data
- [ ] Written release specifies: (a) that biometric identifier/information is being collected
- [ ] Written release specifies: (b) the specific purpose of collection/use
- [ ] Written release specifies: (c) the length of time data will be collected, stored, used
- [ ] Written release obtained for each distinct purpose and collection method
- [ ] Written release renewed if purpose, method, or retention period changes
- [ ] Written release obtained before disclosure to third parties (separate from collection consent)
- [ ] Note: post-SB 2979, a single violation per individual per method of collection
      is the damages unit (not per scan/timestamp) [VERIFY — SB 2979 effective August 2, 2024]

**6.2 CUBI Consent (Tex. Bus. & Com. Code § 503.001) — Texas**

- [ ] Consent obtained before collection (lower standard than BIPA — written not explicitly required)
- [ ] Purpose of collection disclosed
- [ ] No sale or profit from biometric identifiers without consent
- [ ] Consent obtained before disclosure to third parties
- [ ] Note: AG-only enforcement; no private right of action; $25,000 per violation [VERIFY]

**6.3 GDPR Article 9 Lawful Basis — EU/EEA**

- [ ] Article 6 lawful basis identified AND separate Article 9 condition documented
- [ ] If relying on explicit consent (Art. 9(2)(a)):
  - Consent is freely given (not condition of employment/service unless strictly necessary)
  - Specific to the identified purpose
  - Affirmative opt-in action (pre-ticked boxes invalid)
  - Withdrawal mechanism exists and is as easy as giving consent
  - Withdrawal does not affect prior lawful processing
- [ ] If relying on employment law authorization (Art. 9(2)(b)):
  - Applicable EU/Member State law or collective agreement specifically authorizes processing
  - Processing is necessary (not merely convenient)
  - Subject to appropriate safeguards (Art. 88 conditions)
  - [JURISDICTION-SPECIFIC] Identify Member State law authorizing biometric processing in employment context
- [ ] If relying on substantial public interest (Art. 9(2)(g)):
  - Explicit authorization by EU/Member State law
  - Processing proportionate to aim pursued
  - Appropriate safeguards for fundamental rights
- [ ] Article 13/14 transparency notice covers biometric data processing, lawful basis,
      retention period, rights of data subjects, special category nature

**6.4 CCPA/CPRA Sensitive PI — California**

- [ ] Privacy notice discloses collection of biometric information as Sensitive PI
- [ ] "Limit the Use of My Sensitive Personal Information" link/mechanism provided
- [ ] Consumer right to correct biometric data honored within statutory timeline [VERIFY]
- [ ] Consumer right to delete biometric data honored [VERIFY]
- [ ] Consumer right to opt-out of sale honored
- [ ] No use of biometric data beyond disclosed purposes without new consent

**⟁ CLARIFY** — For workplace deployments, ask:

- "Is participation in biometric timekeeping or access control voluntary, or a condition of
  employment? BIPA requires informed written consent before collection; courts have split on
  whether making it a condition of employment vitiates consent. If employees can refuse,
  have alternative time-keeping or access methods been provided?"
- "Has your organization notified new hires of biometric data collection prior to their start
  date, or is consent collected after hiring (which creates retroactive exposure under BIPA)?"

**Classification**: Apply separately per jurisdiction. A BIPA non-compliance does not cure a
GDPR deficiency and vice versa.

### Step 7: Domain 3 — Retention, Destruction, and Security

**7.1 Retention Schedule Compliance**

- [ ] Retention schedule documented per policy (Step 5.2)
- [ ] **BIPA**: Deletion triggered by: (a) original purpose satisfied OR (b) 3 years after
      last interaction with the individual — whichever comes first
- [ ] **GDPR**: Data deleted when no longer necessary for the specified purpose (Art. 5(1)(e));
      retention period documented in ROPA (Art. 30)
- [ ] **CCPA/CPRA**: Retention beyond what is reasonably necessary avoided
- [ ] Automated deletion workflows or manual deletion audit schedules in place
- [ ] Backup media and disaster recovery systems included in deletion scope (critical failure
      mode: organizations delete production data but retain biometric templates in backups)
- [ ] Employee/former employee deletion timeline enforced (post-termination deletion within
      retention schedule)
- [ ] Third-party confirmation of destruction obtained after vendor relationship ends

**7.2 Secure Destruction**

- [ ] Biometric templates destroyed using appropriate irreversible method
- [ ] Destruction certificates maintained for audit trail
- [ ] Physical storage media containing biometric data destroyed or degaussed per policy
- [ ] Cloud-hosted biometric data deletion confirmed with vendor via contractual obligation
      and certification (generic "we deleted it" is insufficient)

**7.3 Technical and Organizational Security Measures**

- [ ] Encryption at rest for biometric template storage
- [ ] Encryption in transit for biometric data transmission
- [ ] Access controls (principle of least privilege; need-to-know basis)
- [ ] Segregation of biometric template data from personally identifying information (separate
      database or encryption key management where feasible)
- [ ] Regular security audits and penetration testing of biometric systems
- [ ] Incident detection and response capability specific to biometric data
- [ ] Employee/contractor training on biometric data handling
- [ ] Physical security for biometric capture devices

**Classification**: Incomplete destruction workflows and backup retention of biometric
templates are among the most common enforcement findings. Classify accordingly.

### Step 8: Domain 4 — Sale, Profit, and Disclosure Prohibitions

**8.1 Sale and Profit Prohibition**

- [ ] **BIPA § 15(c)**: Biometric identifier or information NOT sold, leased, traded, or
      otherwise profited from. This is absolute — no consent exception. [VERIFY — SB 2979 did
      not change the sale/profit prohibition]
- [ ] **Colorado HB 24-1130** (eff. July 1, 2025): Consent required for sale, lease, or
      disclosure; additionally, payment must be made to the subject [VERIFY]
- [ ] **GDPR**: No explicit sale prohibition, but commercial sale of biometric data requires
      an Article 9 condition; explicit consent is the only viable basis in most cases; consent
      for sale to third parties would need to be specific, informed, and freely given
- [ ] Organization has conducted a legal review of any revenue model involving biometric data
- [ ] Third-party analytics, advertising networks, or data brokers do NOT receive biometric
      data without explicit, specific consent

**8.2 Third-Party Disclosure Controls (BIPA § 15(d))**

- [ ] No disclosure to third parties without: (a) written release from data subject, OR
      (b) financial transaction requirement (subject to legal review), OR (c) court/law
      enforcement order, OR (d) first party transmitting to its agent to perform services
      [VERIFY — § 15(d)(4) agent carveout; agent must also receive no financial benefit]
- [ ] All third-party disclosures documented with legal basis
- [ ] Third-party recipients required by contract to comply with BIPA and other applicable laws
- [ ] No bulk transfer of biometric data lists to commercial databases

**⟁ CLARIFY** — For cloud SaaS biometric systems, ask:

- "When your biometric vendor processes templates in its cloud, is this considered a
  'disclosure' under BIPA § 15(d) or does it fall within the agent carveout (§ 15(d)(4))?
  This is actively litigated — confirm via counsel whether your vendor agreement uses agency
  language and whether the vendor extracts any independent financial benefit from the data."

### Step 9: Domain 5 — Vendor and Third-Party Processor Management

**9.1 BIPA Vendor Obligations**

BIPA creates direct liability for disclosing biometric data to vendors, and courts have held
employers liable for vendor BIPA violations in the context of timekeeping systems.

- [ ] Written contract with each vendor handling biometric data executed before data sharing
- [ ] Contract prohibits vendor from selling, profiting from, or further disclosing biometric data
- [ ] Contract specifies vendor's retention/destruction schedule (aligned with organization's policy)
- [ ] Contract grants organization audit rights to verify compliance
- [ ] Contract addresses breach notification obligations to organization
- [ ] Contract allocates liability and indemnification for BIPA violations
- [ ] Vendor's own BIPA compliance assessed (sub-vendor chain audited)

**9.2 GDPR Article 28 Data Processing Agreement**

For any processor handling biometric data of EU/UK persons:

- [ ] DPA executed before processing begins
- [ ] DPA covers: subject matter, duration, nature and purpose of processing, type of personal
      data (including biometric data), categories of data subjects, obligations and rights [Art. 28(3)]
- [ ] DPA requires: processing only on documented instructions; confidentiality; security
      measures; sub-processor restrictions and approval; data subject rights facilitation;
      deletion/return after service; audit cooperation [Art. 28(3)(a)–(h)]
- [ ] Sub-processor list maintained; prior written authorization obtained for sub-processors
- [ ] Article 32 security measures for special category data specified in DPA
- [ ] Breach notification obligation to controller within 72 hours of discovery

**9.3 Security Requirements for Vendors**

- [ ] Vendor security requirements contractually specified (encryption, access controls,
      penetration testing, SOC 2 Type II or equivalent)
- [ ] Vendor incident response obligations defined (notification timeline, scope, contact)
- [ ] Annual or trigger-based vendor security review in place
- [ ] Right to terminate if vendor fails security assessment

**Classification**: Vendor management failures are a leading cause of BIPA class action
exposure. An organization cannot outsource its BIPA obligations to a vendor.

### Step 10: Domain 6 — Individual Rights and Response Procedures

**10.1 Right to Delete / Destroy**

- [ ] **BIPA**: Individuals can request deletion of biometric data (implied from policy and
      retention requirements; no explicit deletion right in BIPA text, but destruction obligation
      runs independently) [VERIFY — some courts have recognized deletion rights under BIPA]
- [ ] **GDPR Art. 17**: Right to erasure honored for biometric data; grounds include
      withdrawal of consent, no longer necessary, objection to processing
- [ ] **CCPA/CPRA**: Right to delete biometric info honored within 45 days (with 45-day
      extension) [VERIFY]
- [ ] Deletion request intake process exists (clear channel for requests)
- [ ] Deletion request response timeline meets applicable law requirements
- [ ] Deletion confirmed in production systems AND backup/archival systems
- [ ] Third-party processors notified of deletion obligation upon individual request

**10.2 Right of Access and Correction**

- [ ] **GDPR Art. 15**: Right of access to biometric data (what data held, how processed,
      recipients, retention period, rights)
- [ ] **CCPA/CPRA**: Right to know what biometric information has been collected
- [ ] **CCPA/CPRA**: Right to correct inaccurate biometric information
- [ ] Response procedures exist for access and correction requests

**10.3 Right to Object (GDPR Art. 21) / Opt-Out**

- [ ] If processing on legitimate interests (Art. 6(1)(f)) or public task basis AND not
      using Art. 9(2) condition requiring overriding interest, right to object honored
- [ ] Opt-out mechanism for CCPA sale/sharing of biometric info provided
- [ ] Alternative methods offered where opt-out of biometric system requested (workplace
      context — employees cannot be constructively forced to consent)

**⟁ CLARIFY** — If the organization has received individual deletion or access requests, ask:

- "Have any individuals requested deletion of their biometric data? If so, was the deletion
  confirmed across all systems, including backups and third-party processors? Incomplete
  deletion (confirmed in primary systems but retained in backups) is a specific enforcement
  risk — the Amazon Alexa COPPA settlement ($25M, 2023) involved this exact pattern."

### Step 11: Domain 7 — GDPR/UK GDPR Special Category Obligations

This domain applies only when EU/EEA or UK residents' biometric data is processed.

**11.1 Article 35 DPIA Requirement**

GDPR Article 35(3)(b) requires a DPIA for "large-scale processing of special categories of
data" and processing using "new technologies" likely to result in "high risk":

- [ ] DPIA conducted before implementing biometric data processing involving EU/UK persons
- [ ] DPIA covers: systematic description of processing operations; necessity/proportionality
      assessment; risk to rights and freedoms; measures to address risks
- [ ] DPIA documents the Article 9 condition and why processing is necessary
- [ ] DPIA addresses bias risks in automated biometric recognition systems
- [ ] DPIA reviewed and updated when processing purposes or technology change materially
- [ ] Where DPIA indicates residual high risk, DPA (supervisory authority) consulted before
      processing begins [Art. 36]
- [ ] DPIA maintained in Records of Processing Activities [Art. 30]

**11.2 Records of Processing Activities (Art. 30)**

- [ ] Biometric processing listed in ROPA with: controller/processor identity; purpose;
      categories of data subjects and data (including special category); recipients; transfers;
      retention periods; security measures
- [ ] ROPA updated when biometric processing operations change
- [ ] Sub-processor entries in ROPA (for processor's ROPA under Art. 30(2))

**11.3 Transfers of Biometric Data Outside EU/EEA/UK**

- [ ] **EU → Third Country**: Standard Contractual Clauses (2021 SCCs) or other Chapter V
      mechanism in place [VERIFY current SCC form and Transfer Impact Assessment requirements]
- [ ] **UK → Third Country**: UK IDTA or UK Addendum to EU SCCs [VERIFY current UK ICO guidance]
- [ ] Transfer Impact Assessment (TIA) conducted for transfers to high-risk destinations
- [ ] Biometric data classified as sensitive in data transfer documentation

**11.4 Automated Decision-Making (Art. 22)**

- [ ] If biometric recognition used to make significant decisions about individuals
      (e.g., access denial, performance assessment), Art. 22 analysis completed
- [ ] If Art. 22(1) applies (solely automated decisions with legal/significant effects):
      Art. 22(2) exception identified or not used without exception
- [ ] Human oversight mechanism documented where Art. 22 applies

**Classification**: GDPR violations involving biometric data as special category data carry
fines up to €20 million or 4% of global annual turnover, whichever is higher. Classify
DPIA absence and unlawful Art. 9 processing as CRITICAL DEFICIENCY.

### Step 12: Domain 8 — Incident Response and Breach Notification

**12.1 Biometric Data Breach Preparedness**

Biometric data breaches are uniquely severe: unlike passwords, biometric identifiers cannot
be reset. A breach creates permanent impairment to the affected individual.

- [ ] Incident response plan specifically addresses biometric data incidents
- [ ] Biometric data identified as highest-sensitivity category in incident triage framework
- [ ] Containment procedures for biometric template exposure defined
- [ ] Internal escalation path from initial detection to privacy/legal team defined
- [ ] Evidence preservation procedures for biometric incidents documented

**12.2 Regulatory Notification Obligations**

- [ ] **GDPR Art. 33**: Breach notification to supervisory authority within 72 hours of
      becoming aware (except where unlikely to result in risk to individuals) [VERIFY per-DPA rules]
- [ ] **GDPR Art. 34**: Notification to affected individuals without undue delay if breach
      likely to result in high risk (biometric data breaches should presumptively trigger Art. 34)
- [ ] **State breach notification**: Applicable US state breach notification laws assessed for
      biometric data incidents [VERIFY — biometric data triggers breach notification in IL, TX,
      WA, CA, CO and most other states under sensitive PI categories]
- [ ] Processor (GDPR) notification to controller within 72 hours of discovering breach [Art. 28(3)(f)]

**12.3 Remediation Following Breach**

- [ ] Affected individuals notified of their options (deletion, reissuance of alternative
      credential, monitoring services)
- [ ] Biometric system taken offline if templates are confirmed compromised
- [ ] Vendor root cause investigation initiated
- [ ] DPIA updated to reflect changed risk profile post-breach

### Step 13: Penalty Exposure Modeling

Estimate enforcement exposure to prioritize remediation.

**BIPA (Illinois) — Post-SB 2979 (August 2, 2024)**

- $1,000 per individual per method of collection where violation is negligent [VERIFY]
- $5,000 per individual per method of collection where violation is intentional or reckless [VERIFY]
- Plus attorneys' fees, costs, and other litigation damages
- Per-violation unit post-SB 2979: one violation per individual per method (not per scan) [VERIFY]
- Statute of limitations: 5 years from violation (Tims v. Black Horse Carriers, 2023) [VERIFY]
- Key settlements: Facebook $650M (2020), Google $100M (2022), TikTok $92M (2022),
  Clearview AI $51.75M (2025), Six Flags $36M (2021) [VERIFY current figures]
- Class action risk: any organization with 10+ employees using biometric systems in IL
  without consent faces significant exposure

**Texas CUBI**

- AG civil penalty: $25,000 per violation [VERIFY]
- No private right of action (key distinction from BIPA)
- AG enforcement only; benchmark: Meta $1.4 billion settlement (March 2025) [VERIFY]
- Note: even with AG-only enforcement, exposure can be massive at scale

**GDPR (EU/UK)**

- Up to €20 million or 4% of global annual turnover, whichever is higher (GDPR Art. 83(5))
- UK GDPR: up to £17.5 million or 4% of global annual turnover [VERIFY]
- Supervisory authority can impose corrective measures, processing bans, fines
- High-profile enforcement for biometric data without proper lawful basis or DPIA

**FTC Act § 5**

- FTC cannot impose civil penalties for first-time violations of § 5 (only for consent order violations)
- Subsequent violations: civil penalties up to $51,744 per violation per day [VERIFY 2024 adjusted]
- FTC may require disgorgement, deletion, and ongoing oversight

**⟁ CLARIFY** — For exposure modeling, ask:

- "How many individuals have been subject to biometric data collection without compliant
  consent? This determines the BIPA exposure scale."
- "What is your organization's global annual turnover? This anchors the GDPR penalty ceiling."
- "Is there any active litigation, regulatory inquiry, or consent order in place? Prior
  enforcement history affects both exposure and the applicable penalty multiplier."

### Step 14: Quality Verification

Before delivering the assessment, run the quality checks below.

1. Run all 5 Citation Quality Gates silently. Revise failures before delivery.
2. For every CRITICAL DEFICIENCY finding, run the 3-pass Self-Interrogation.
3. Assign Confidence Scores to each material finding.
4. Verify completeness: confirm all 8 domains have been addressed.
5. Verify no JURISDICTION-SPECIFIC assumptions have been stated as universal.
6. Confirm every statutory citation is marked [VERIFY] if not confirmed via legalcode-mcp.
7. Generate the Glass Box Audit Trail and append it to the output.

### Step 15: Generate Assessment Output

Write the full assessment using the **Output Format Template** below.

---

## BIPA Definitions Reference

**Biometric identifier** (740 ILCS 14/10): A retina or iris scan, fingerprint, voiceprint,
or scan of hand or face geometry. Does NOT include: writing samples, written signatures,
photographs, human biological samples for scientific testing or screening, demographic data,
tattoo descriptions, physical descriptions, or information collected, used, or stored for
health care treatment, payment, or operations under HIPAA.

**Biometric information** (740 ILCS 14/10): Any information, regardless of how it is
captured, converted, stored, or shared, based on an individual's biometric identifier used
to identify an individual. Includes derivative works from biometric identifiers.

**Important**: BIPA covers both biometric identifiers (raw data) AND biometric information
(derived templates). Many organizations focus only on raw capture and miss template storage obligations.

---

## Classification System

### ✅ COMPLIANT

The biometric data practice meets the applicable legal requirement. No action required
beyond ongoing monitoring.

**Examples:**

- Written consent obtained before collection with purpose and retention period specified
- Written biometric policy publicly posted with retention/destruction schedule
- Third-party DPA in place with Art. 28-compliant terms
- DPIA completed and documented before EU biometric processing began

**Action**: Monitor; incorporate into next review cycle.

### ⚠️ PARTIAL

The biometric data practice partially meets the requirement but has identifiable gaps that
create enforcement risk. Remediation needed within the near-term horizon.

**Examples:**

- Written policy exists but does not specify destruction timeline
- Consent form obtained but lacks specific retention period statement
- DPA in place but lacks biometric-specific security specifications
- DPIA conducted but not updated after biometric system upgrade

**Action**: Identify specific gaps; schedule near-term remediation with responsible team.

### ❌ NON-COMPLIANT

The biometric data practice fails to meet the requirement. Material enforcement risk exists.
Remediation must be prioritized.

**Examples:**

- No consent obtained from employees before biometric timekeeping enrollment
- Written policy not publicly available
- No DPA with vendor processing GDPR-scope biometric data
- Biometric data retained 5+ years with no documented retention schedule or destruction

**Action**: Immediate escalation to privacy/legal team; remediation plan required within
30-90 days.

### 🔴 CRITICAL DEFICIENCY

Active, ongoing legal violation or immediate enforcement trigger. Requires immediate
escalation and action within 0–30 days.

**Automatic CRITICAL DEFICIENCY triggers:**

1. **No consent mechanism at all**: Biometric data being collected with no written consent
   or release of any kind from affected individuals (BIPA § 15(b) direct violation)
2. **No written biometric data policy**: No publicly available written retention and
   destruction policy (BIPA § 15(a) direct violation; presumptive class action trigger)
3. **Biometric data sold or profited from**: Any revenue-generating disclosure of biometric
   identifiers without lawful authority (BIPA § 15(c) absolute prohibition)
4. **Disclosure to third parties without written release**: Biometric data shared with
   vendors, partners, or service providers without individual written releases or applicable
   BIPA exception (§ 15(d) violation)
5. **GDPR processing without Article 9 condition**: EU/UK biometric data processed with
   no identified Article 9 condition — explicit consent, employment law, vital interests, or
   other listed condition (Art. 9(1) absolute prohibition on processing)
6. **No DPIA for high-risk GDPR biometric processing**: Large-scale biometric processing of
   EU/UK persons without a completed DPIA (Art. 35 mandatory requirement; supervisory
   authorities impose fines for this omission alone)
7. **Biometric data retained beyond BIPA 3-year maximum**: Data retained for Illinois
   individuals more than 3 years after last interaction without renewed consent or legal basis
8. **Active class action or regulatory enforcement**: Ongoing BIPA class action or state AG
   investigation with known exposure — requires immediate legal response
9. **No DPA with GDPR-scope biometric processor**: Third-party vendor processes biometric
   data of EU/UK persons without an Article 28-compliant DPA (Art. 28(1) violation)
10. **Biometric data breach with no notification capability**: Known or suspected biometric
    template exposure with no incident response procedures and no notification plan in place

---

## Remediation Priority Framework

### IMMEDIATE (0–30 days)

For any CRITICAL DEFICIENCY and for active exposures with ongoing harm.

**Examples:**

- Any automatic CRITICAL DEFICIENCY trigger above
- Deploy interim consent mechanism for IL employees using biometric timekeeping
- Remove biometric data from sale/commercial data product immediately
- Engage outside counsel for active class action or AG inquiry
- Take biometric system offline if vendor has experienced confirmed template breach

### NEAR-TERM (30–90 days)

For NON-COMPLIANT findings and for PARTIAL findings with significant enforcement risk.

**Examples:**

- Draft and publish written biometric data policy (BIPA § 15(a)) with retention/destruction schedule
- Retroactively obtain written consent from employees enrolled without compliant consent
  (note: retroactive consent does not cure pre-consent BIPA violations; it prevents future ones)
- Execute DPAs with all vendors processing GDPR-scope biometric data
- Complete DPIA for existing GDPR biometric processing operations
- Build biometric data deletion workflow including backup systems
- Update vendor contracts to include BIPA-required protections

### BACKGROUND (90+ days)

For PARTIAL findings with lower enforcement risk and for program enhancement.

**Examples:**

- Implement automated retention/deletion workflows
- Conduct annual biometric program review
- Add biometric data handling to employee privacy training curriculum
- Evaluate less privacy-invasive alternatives for biometric use cases
- Develop enterprise-wide biometric data standards for multi-jurisdiction consistency
- Consider safe harbor certification programs if applicable

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. If any gate fails, revise before
delivering.

| Gate           | Rule                                                                                                           | Fail Action                                                                          |
| -------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Source**     | Every finding cites specific statute, regulation, enforcement action, or established principle                 | Add citation or mark [UNVERIFIED — counsel to confirm]                               |
| **Format**     | Citations follow consistent format (740 ILCS 14/§15(b); Art. 9(1) GDPR; etc.)                                  | Fix format                                                                           |
| **Currency**   | Every cited provision checked for amendments (BIPA SB 2979 Aug 2024; CO HB 24-1130 Jul 2025; GDPR SCC updates) | Flag [CHECK CURRENCY — may have been amended]                                        |
| **Domain**     | Analysis stays within the applicable jurisdiction(s); no bleed from inapplicable frameworks                    | Remove or label as inapplicable; flag [JURISDICTION-SPECIFIC — verify applicability] |
| **Confidence** | Penalty amounts, compliance deadlines, and judicial interpretations explicitly marked [VERIFY]                 | Add confidence qualifier; do not assert contested positions as settled               |

### Self-Interrogation for CRITICAL DEFICIENCY Findings

For any finding classified as CRITICAL DEFICIENCY, apply this 3-pass review:

**Pass 1 — Legal Chain Integrity**:

- Does the CRITICAL classification follow logically from the cited statutory or regulatory text?
- Is there a genuine defense (HIPAA exemption, GLBA financial institution exemption, employee
  handbook exception) that has not been addressed?
- For BIPA: Has the correct post-SB 2979 violation unit been applied?

**Pass 2 — Completeness**:

- Have all relevant exemptions and safe harbors been considered?
  (e.g., BIPA: written release exception, law enforcement, financial transaction necessity)
- Has the correct threshold been verified (CCPA/CPRA consumer count threshold; CO CPA threshold)?
- Are there compensating controls (e.g., verbal consent where written required) that reduce
  but do not eliminate the risk?

**Pass 3 — Challenge**:

- What is the strongest counter-argument that this is not a CRITICAL DEFICIENCY?
- Under what circumstances could a reasonable privacy professional classify this as NON-COMPLIANT
  rather than CRITICAL?
- If the counter-argument is strong, downgrade and note the basis.

Record the outcome: `self_interrogation: CONFIRMED` or `self_interrogation: REVISED — [reason]`.

### Confidence Scoring

Assign a confidence level to each material finding:

| Level        | Range     | Meaning                                                           | Action                                              |
| ------------ | --------- | ----------------------------------------------------------------- | --------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled statutory text; unambiguous violation                     | State with confidence                               |
| **High**     | 0.80–0.94 | Strong authority; minor interpretive questions                    | State with brief caveat                             |
| **Probable** | 0.60–0.79 | Good arguments; contested area (e.g., BIPA agent exception scope) | State reasoning + note uncertainty                  |
| **Possible** | 0.40–0.59 | Genuinely uncertain; unsettled law or novel facts                 | Flag for attorney review with both sides            |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative application                               | Do NOT assert; mark [UNCERTAIN — counsel to advise] |

**Specific [VERIFY] callouts** (these are particularly active areas of legal uncertainty):

- SB 2979 "same method of collection" definition boundaries [VERIFY — active litigation]
- BIPA application to out-of-state entities whose biometric systems affect IL residents [VERIFY]
- BIPA healthcare/HIPAA carveout scope [VERIFY — narrowly construed by courts]
- GDPR authentication vs. identification distinction for Art. 9 applicability [VERIFY — ICO guidance]
- CO HB 24-1130 effective date and transition period details [VERIFY]
- Status of proposed state laws (NY S1422, MA, MI) [VERIFY current legislative status]

---

## Glass Box Audit Trail

```yaml
glass_box:
  skill_name: "legalcode-biometric-data-compliance"
  assessment_date: "[YYYY-MM-DD]"
  organization_name: "[name or 'Confidential']"
  assessment_mode: "[Full audit / Gap analysis / Applicability screening / Vendor contract review / Incident response / Litigation exposure]"
  biometric_data_types:
    - "[fingerprints / facial geometry / retina-iris / voiceprint / hand geometry / keystroke / gait / other]"
  applicable_frameworks:
    bipa_illinois: "[Yes / No / Not assessed]"
    cubi_texas: "[Yes / No / Not assessed]"
    washington_mhmd: "[Yes / No / Not assessed]"
    ccpa_cpra_california: "[Yes / No / Not assessed]"
    colorado_cpa_hb24_1130: "[Yes / No / Not assessed]"
    gdpr_article_9: "[Yes / No / Not assessed]"
    uk_gdpr: "[Yes / No / Not assessed]"
    ftc_act_section_5: "[Yes / No / Not assessed]"
    other_frameworks: "[list or 'none']"
  use_case: "[workplace / consumer / retail / healthcare / financial / security / other]"
  domains_assessed:
    domain_1_inventory_governance: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY / Not assessed]"
    domain_2_consent_notice: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY / Not assessed]"
    domain_3_retention_destruction_security: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY / Not assessed]"
    domain_4_sale_disclosure_prohibitions: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY / Not assessed]"
    domain_5_vendor_processor_management: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY / Not assessed]"
    domain_6_individual_rights: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY / Not assessed]"
    domain_7_gdpr_special_category: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY / Not assessed]"
    domain_8_incident_response_breach: "[COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY / Not assessed]"
  critical_deficiency_count: "[N]"
  non_compliant_count: "[N]"
  partial_count: "[N]"
  compliant_count: "[N]"
  vendors_with_biometric_access: "[N or 'not assessed']"
  dpa_coverage_gdpr: "[All / Partial / None / Not applicable]"
  dpia_completed: "[Yes / No / Not required / Not assessed]"
  bipa_sb2979_amendment_applied: "[Yes — post-Aug 2, 2024 analysis / No — pre-amendment / Not applicable]"
  penalty_exposure_modeled: "[Yes / No]"
  estimated_bipa_exposure: "[$ range or 'not modeled']"
  legalcode_mcp: "[Connected / Not connected — citations marked VERIFY]"
  research_reference_file: "[path or 'Not created']"
  self_interrogation_outcomes:
    - "[Finding ID]: [CONFIRMED / REVISED — reason]"
  citations_verified: "[N VERIFIED via legalcode-mcp / N marked [VERIFY]]"
  confidence_overall: "[Definite / High / Probable / Possible] — [rationale]"
  limitations:
    - "Statutory citations carry hallucination risk; verify all before reliance"
    - "BIPA SB 2979 'same method of collection' interpretation is actively litigated [VERIFY]"
    - "Colorado HB 24-1130 effective July 1, 2025; verify current status and implementing guidance [VERIFY]"
    - "Proposed state biometric laws (NY, MA, MI) pending enactment; verify current legislative status [VERIFY]"
    - "GDPR authentication vs. identification distinction for Article 9 applicability is not fully settled [VERIFY]"
    - "[Assessment-specific limitations or assumptions]"
  reviewer: "AI-assisted — requires review by qualified privacy attorney before reliance"
```

---

## Anti-Patterns

The following are the most common biometric data compliance failures. Every item on this
list is traceable to actual litigation, enforcement actions, or regulatory findings.

1. **Treating BIPA as consent-at-onboarding**: Obtaining a single general consent at
   employment start that covers all future biometric uses. BIPA requires consent to specify
   the purpose AND the retention period. If the system changes or a new biometric type is
   added, new consent is required.

2. **Using verbal consent for BIPA compliance**: Verbal acknowledgment of a biometric
   policy does not satisfy BIPA's written release requirement (pre- or post-SB 2979).
   E-signatures accepted post-SB 2979; verbal is insufficient.

3. **Confidentiality agreement as BIPA release**: Including biometric data consent in a
   general confidentiality or NDA provision. BIPA requires a standalone or clearly
   identifiable written release specifically for biometric data.

4. **Publishing a policy without a destruction schedule**: Having a publicly available
   biometric data policy that says "we destroy biometric data when no longer needed"
   without specifying the BIPA-required timeline (3 years/purpose completion). This
   violates § 15(a).

5. **No deletion from backup systems**: Deleting biometric templates from production
   databases but retaining them in backup tapes, disaster recovery snapshots, or archival
   storage. This is a primary enforcement target — the Amazon Alexa COPPA case ($25M)
   involved exactly this pattern and biometric programs face the same risk.

6. **Assuming HIPAA exemption covers BIPA**: Healthcare providers and health insurers
   sometimes assume their HIPAA compliance exempts them from BIPA. The HIPAA exemption
   in BIPA § 15(d) is narrow — it applies only to data that is subject to and compliant
   with HIPAA. Many healthcare contexts (insurance fraud detection, visitor badging,
   biometric payroll) are not HIPAA-covered uses.

7. **GLBA financial institution exemption overreach**: Banks and financial institutions
   subject to the Gramm-Leach-Bliley Act sometimes claim BIPA exemption. Courts have
   narrowly construed the BIPA financial institution exception — it applies only where
   the specific biometric use is governed by a federal law [VERIFY case law].

8. **Vendor contract without BIPA language**: Using a software or services agreement
   with a biometric vendor that has no biometric-specific protections (sale prohibition,
   destruction obligation, audit right, BIPA indemnification). Courts have found employers
   liable for vendor BIPA violations.

9. **"No sale" policy without contractual enforcement downstream**: Adopting an internal
   policy prohibiting sale of biometric data but failing to include anti-sale provisions
   in vendor contracts. If a vendor sells or profits from the data, the originating
   organization may face exposure.

10. **Applying GDPR legitimate interests to biometric data**: Attempting to rely on
    Article 6(1)(f) legitimate interests as a basis for biometric processing and forgetting
    that Article 9(1) still requires an independent Article 9(2) condition. Legitimate
    interests is an Article 6 basis only; biometric data processing still needs an Art. 9
    condition regardless of the Art. 6 basis used.

11. **Treating facial recognition as lower-risk than fingerprinting**: Assuming that
    contactless biometric collection (facial recognition cameras) has fewer legal
    requirements than active biometric collection (fingerprint scanners). Under BIPA and
    GDPR, both facial geometry scans and fingerprint scans are biometric identifiers
    subject to the same requirements.

12. **No separate consent for different biometric uses**: Using a single consent form to
    cover timekeeping, building access, cafeteria payment, and other uses. Best practice —
    and the direction of law — is separate consent for each distinct purpose.

13. **Ignoring Illinois employees of multi-state employers**: An employer headquartered
    in Texas or California with even a single Illinois employee using a biometric system
    is subject to BIPA for that employee. The size of the organization is irrelevant;
    geographic presence of a data subject is the trigger.

14. **Collecting biometric data for one purpose and repurposing for another**: Using
    biometric timekeeping data to also conduct performance monitoring, emotion detection,
    or behavioral analytics without separate consent. Secondary uses require new,
    purpose-specific consent under BIPA and Article 9 GDPR.

15. **No incident response protocol for biometric template exposure**: Generic data breach
    plans that do not account for biometric template exposure. Unlike account credentials,
    biometric data cannot be revoked and reissued. Biometric incidents require immediate
    system quarantine, proactive notification, and alternative credential issuance.

16. **Ignoring the immutability risk when setting retention periods**: Keeping biometric
    data "until needed" rather than on a strict destruction schedule. Because biometric
    identifiers cannot be changed after a breach, organizations that hold biometric data
    longer than necessary face permanent impairment risk for every day of excess retention.

17. **Treating biometric data as pseudonymous or anonymous**: Claiming biometric templates
    are anonymized because they are stored as mathematical vectors rather than photographs.
    Biometric templates are pseudonymous at best — they can be re-linked to individuals via
    the biometric system. GDPR and BIPA apply regardless of the storage format.

---

## Writing Standards

1. **Cite specifically**: Every finding cites the applicable statutory provision, Article, or
   enforcement action. "BIPA" without a section reference is insufficient. Use "740 ILCS
   14/15(b)" or "BIPA § 15(b)."

2. **Mark amendment status**: Flag findings arising from the 2024 BIPA SB 2979 amendment
   as **[POST-SB 2979]** and the August 2, 2024 effective date. Flag Colorado HB 24-1130
   findings as **[EFFECTIVE JULY 1, 2025 — VERIFY]**.

3. **Mark uncertainty explicitly**: All penalty amounts, SOL periods, legislative status
   markers, and contested interpretations must be marked [VERIFY]. Do not state contested
   positions as settled law.

4. **Separate finding from recommendation**: The finding describes the gap; the recommendation
   describes the specific action, the responsible team, and the deadline. "No written policy
   exists (NON-COMPLIANT)" is a finding. "Draft and publish a BIPA-compliant biometric data
   retention and destruction policy within 30 days — Responsible: Privacy/Legal team" is a
   recommendation.

5. **No absolute compliance guarantees**: Never state "adopting these recommendations ensures
   BIPA compliance" or "no class action risk will remain." The legal landscape is contested;
   express findings as risk assessments, not guarantees.

6. **Plain language for non-lawyers**: Assessments are often read by HR, IT, and business
   leaders, not only lawyers. Write findings in plain language with the legal citation in
   parentheses.

7. **Calibrate to jurisdiction**: Do not state BIPA requirements as universal or GDPR
   requirements as applying to US-only entities. Jurisdiction scope is always explicit.

---

## External Tool Integration

### legalcode-mcp (Preferred)

Use legalcode-mcp in Step 3 to verify:

- Current text of 740 ILCS 14 post-SB 2979 (August 2, 2024 amendment)
- Texas Bus. & Com. Code § 503.001 current text and AG enforcement guidance
- GDPR Article 9, 28, 35 current text and DPA supervisory authority guidance
- ICO biometric data guidance (most recent update)
- FTC enforcement actions under the 2023 Biometric Policy Statement
- Status of proposed state laws (NY S1422, MA, MI, etc.)
- Recent enforcement settlements (Meta/Texas AG $1.4B, Clearview AI $51.75M) [VERIFY current figures]

Save to `/tmp/legalcode-biometric-research.md`.

**Without legalcode-mcp:**

- Mark all statutory and enforcement citations with [VERIFY]
- Note in Glass Box: `legalcode_mcp: "Not connected — citations marked VERIFY"`
- Proceed using the legal framework embedded in this skill
- Advise the user that all legal citations should be verified against current authoritative
  sources before reliance

---

## Localization Notes

### US State-by-State Quick Reference

| State       | Law                      | Private Right of Action    | Damages                                           | Status                     |
| ----------- | ------------------------ | -------------------------- | ------------------------------------------------- | -------------------------- |
| Illinois    | BIPA (740 ILCS 14)       | Yes                        | $1K negligent / $5K intentional                   | In force; SB 2979 Aug 2024 |
| Texas       | CUBI (§ 503.001)         | No (AG only)               | $25K/violation                                    | In force                   |
| Washington  | My Health MY Data Act    | Yes (private)              | Actual/statutory [VERIFY]                         | Effective 2024             |
| California  | CCPA/CPRA (Sensitive PI) | Limited (CPPA enforcement) | Civil penalties up to $7,500/intentional [VERIFY] | In force                   |
| Colorado    | CPA (HB 24-1130)         | No (AG/AGs only)           | Up to $20K/violation [VERIFY]                     | Effective July 1, 2025     |
| New York    | S1422 (proposed)         | Yes (modeled on BIPA)      | $1K/$5K (proposed)                                | Pending [VERIFY]           |
| Arkansas    | Act 504                  | [VERIFY]                   | [VERIFY]                                          | In force                   |
| Virginia    | VCDPA                    | No (AG only)               | $7,500/intentional [VERIFY]                       | In force                   |
| Connecticut | CTDPA                    | No (AG only)               | $5,000/violation [VERIFY]                         | In force                   |

### GDPR — Member State Variations

[JURISDICTION-SPECIFIC] Several EU Member States have adopted national law conditions for
biometric data in employment contexts:

- **Germany**: Betriebsräte (works councils) must be consulted before implementing biometric
  systems in the workplace; Betriebsverfassungsgesetz (BetrVG) co-determination rights apply [VERIFY]
- **France**: CNIL requires authorization for certain biometric processing in workplaces;
  specific guidance on time-and-attendance biometric systems [VERIFY]
- **Netherlands**: Works council approval required for biometric processing decisions under
  the WOR (Works Councils Act) [VERIFY]
- **Spain**: AEPD guidance on biometric processing in employment context; explicit consent
  or collective agreement required [VERIFY]
- **Italy**: Garante guidelines on biometric recognition systems [VERIFY]

For each EU Member State where biometric data is processed in employment context, research:

1. Whether national law or collective agreement authorizes Art. 9(2)(b) processing
2. Whether works council or employee representative consultation is required
3. Whether the national DPA has issued sector-specific biometric guidance

---

## Output Format Template

```markdown
# Biometric Data Compliance Assessment

**Organization**: [name]
**Assessment date**: [YYYY-MM-DD]
**Assessment mode**: [Full audit / Gap analysis / Applicability screening / etc.]
**Biometric data types assessed**: [list]
**Applicable frameworks**: [BIPA / CUBI / CCPA-CPRA / GDPR / etc.]
**Use case**: [workplace / consumer / retail / healthcare / financial / security]

---

## Executive Summary

| Domain                               | BIPA          | TX CUBI           | GDPR              | CCPA/CPRA         | Overall  |
| ------------------------------------ | ------------- | ----------------- | ----------------- | ----------------- | -------- |
| 1. Inventory & Governance            | [✅/⚠️/❌/🔴] | [✅/⚠️/❌/🔴/N/A] | [✅/⚠️/❌/🔴/N/A] | [✅/⚠️/❌/🔴/N/A] | [status] |
| 2. Consent & Notice                  |               |                   |                   |                   |          |
| 3. Retention, Destruction & Security |               |                   |                   |                   |          |
| 4. Sale & Disclosure Prohibitions    |               |                   |                   |                   |          |
| 5. Vendor & Processor Management     |               |                   |                   |                   |          |
| 6. Individual Rights                 |               |                   |                   |                   |          |
| 7. GDPR Special Category Obligations | N/A           | N/A               |                   | N/A               |          |
| 8. Incident Response & Breach        |               |                   |                   |                   |          |

**Overall compliance posture**: [HIGH RISK / MODERATE RISK / LOW RISK]
**Class action exposure (BIPA)**: [IMMEDIATE / ELEVATED / MODERATE / LOW]
**GDPR enforcement exposure**: [IMMEDIATE / ELEVATED / MODERATE / LOW / N/A]

**Top 3 priority actions:**

1. [IMMEDIATE] [Finding] — [Action] — Owner: [Role] — Deadline: [Date]
2. [NEAR-TERM] [Finding] — [Action] — Owner: [Role] — Deadline: [Date]
3. [NEAR-TERM] [Finding] — [Action] — Owner: [Role] — Deadline: [Date]

---

## Critical Deficiencies (IMMEDIATE Action Required)

### CD-[N]: [Short title]

**Domain**: [domain name]
**Applicable law(s)**: [BIPA § 15(b); GDPR Art. 9(1); etc.]
**Finding**: [Specific factual description of the deficiency]
**Enforcement risk**: [Class action / AG enforcement / DPA enforcement / FTC action]
**Remediation**: [Specific steps with owner and deadline]
**Timeline**: IMMEDIATE (0–30 days)
**Confidence**: [Definite / High / Probable]
**Self-Interrogation**: [CONFIRMED / REVISED — reason]

---

## Non-Compliant Findings (NEAR-TERM Remediation)

### NC-[N]: [Short title]

**Domain**: [domain name]
**Applicable law(s)**: [citation]
**Finding**: [Description]
**Enforcement risk**: [Description]
**Remediation**: [Specific steps with owner and deadline]
**Timeline**: NEAR-TERM (30–90 days)
**Confidence**: [level]

---

## Partial Compliance Findings

### PC-[N]: [Short title]

**Domain**: [domain name]
**Applicable law(s)**: [citation]
**Finding**: [Description of gap]
**What is in place**: [What the organization has done correctly]
**What is missing**: [The specific gap]
**Remediation**: [Specific steps]
**Timeline**: [NEAR-TERM / BACKGROUND]
**Confidence**: [level]

---

## Vendor and Processor Assessment Summary

| Vendor | Biometric Data Type | BIPA Contract Provisions | GDPR DPA     | Security Requirements | Status        |
| ------ | ------------------- | ------------------------ | ------------ | --------------------- | ------------- |
| [name] | [type]              | [Yes/No/Partial]         | [Yes/No/N/A] | [Met/Unmet/N/A]       | [✅/⚠️/❌/🔴] |

---

## Penalty Exposure Estimate

**BIPA (Illinois)**

- Affected individuals (estimated): [N]
- Violation type: [Negligent / Intentional-reckless / Mixed]
- Exposure per individual (post-SB 2979): [$1,000–$5,000] [VERIFY]
- Estimated total exposure range: [$X–$Y]
- Class action risk level: [IMMEDIATE / ELEVATED / MODERATE / LOW]
- Statute of limitations: 5 years from violation [VERIFY — Tims v. Black Horse Carriers, 2023]

**Texas CUBI**

- Applicable: [Yes / No]
- AG penalty: $25,000 per violation [VERIFY]
- Estimated exposure: [$X–$Y based on violation count]

**GDPR**

- Applicable: [Yes / No]
- Maximum penalty ceiling: €20M or 4% global turnover, whichever higher [VERIFY]
- Global annual turnover: [$ or 'not provided']
- Penalty ceiling: [€X / 4% of $Y = $Z, whichever higher]

---

## Remediation Roadmap

### IMMEDIATE (0–30 days)

- [ ] [Specific action] — [Responsible team] — [Outcome metric]

### NEAR-TERM (30–90 days)

- [ ] [Specific action] — [Responsible team] — [Outcome metric]

### BACKGROUND (90+ days)

- [ ] [Specific action] — [Responsible team] — [Outcome metric]

---

## Glass Box Audit Trail

[Insert completed YAML from Glass Box Audit Trail template above]
```

---

## Related Skills

- **legalcode-dpia-generator**: For conducting GDPR Article 35 Data Protection Impact
  Assessments for high-risk biometric processing
- **legalcode-gdpr-legal-basis-assessment**: For deep analysis of Article 9 conditions and
  Article 6 bases for biometric data processing
- **legalcode-data-processing-agreement-drafter**: For drafting or reviewing vendor DPAs
  covering biometric data processing
- **legalcode-vendor-privacy-assessment**: For comprehensive vendor privacy risk assessment
  including biometric processors
- **legalcode-us-state-privacy-comparison**: For multi-state sensitive data comparison
  including biometric data treatment across state laws
- **legalcode-breach-response-checklist**: For managing the immediate response to a biometric
  data incident
- **legalcode-consent-mechanism-review**: For reviewing whether consent mechanisms satisfy
  BIPA and GDPR biometric consent requirements

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis using the 2-agent research pipeline:

**Structural Agent**: Analysis of `legalcode-coppa-compliance-assessment` and
`legalcode-dora-compliance-assessment` reference skills; extraction of 4-tier classification
architecture, CLARIFY point design, Citation Quality Gates, Self-Interrogation, Confidence
Scoring, Glass Box YAML patterns, anti-pattern catalogue structure, and output format
template conventions for adaptation to biometric data compliance.

**Legal Research Agent**: Comprehensive web research covering:

- 740 ILCS 14 (BIPA) including SB 2979 (August 2, 2024 amendment)
- Texas Bus. & Com. Code § 503.001 (CUBI) including Meta $1.4B AG settlement (2025)
- Washington My Health MY Data Act (HB 1155, effective 2024)
- California CCPA/CPRA biometric/sensitive PI framework
- Colorado CPA HB 24-1130 (effective July 1, 2025)
- GDPR Articles 4(14), 9, 22, 28, 35 and ICO biometric recognition guidance
- UK GDPR + DPA 2018 Schedule 1 Part 2
- FTC Policy Statement on Biometric Information Technology (May 18, 2023)
- Proposed state biometric laws (NY S1422, MA, MI)
- Landmark enforcement: Facebook $650M BIPA (2020), Google $100M (2022), TikTok $92M (2022),
  Clearview AI $51.75M (2025), Six Flags $36M (2021)
- Rosenbach v. Six Flags (IL Sup. Ct. 2019) standing without injury
- Tims v. Black Horse Carriers (IL Sup. Ct. 2023) 5-year SOL
- Post-SB 2979 "same method of collection" single-violation unit interpretation
- FTC biometric enforcement actions and 2023 Policy Statement
- IAPP, ACLU, EFF biometric privacy frameworks and best practices

Quality framework adapted from the legalcode-contract-review, legalcode-coppa-compliance-
assessment, and legalcode-dora-compliance-assessment reference standards.
