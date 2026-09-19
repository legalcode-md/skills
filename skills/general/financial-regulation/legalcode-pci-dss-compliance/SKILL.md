---
name: legalcode-pci-dss-compliance
description: 'PCI DSS v4.0.1 compliance assessment for merchants, service providers, and their technology
  teams covering the full lifecycle: CDE scoping and network segmentation validation, SAQ type determination
  (SAQ A / A-EP / B / B-IP / C / C-VT / D / P2PE / HCE / SPoC), all 12 PCI DSS requirements analysis (network
  security controls, stored account data protection, transit encryption, malware protection, secure development,
  access control, authentication, physical security, logging and monitoring, security testing, organizational
  policies), QSA preparation and ROC readiness, compensating controls documentation, customized approach
  Targeted Risk Analysis (TRA), third-party service provider (TPSP) management, merchant level and acquirer
  compliance obligations (Visa, Mastercard, Amex, Discover, JCB), and cross-framework mapping (NIST CSF,
  SOC 2, ISO 27001, DORA).'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

PCI DSS v4.0.1 compliance assessment for merchants, service providers, and their technology teams covering the full lifecycle: CDE scoping and network segmentation validation, SAQ type determination (SAQ A / A-EP / B / B-IP / C / C-VT / D / P2PE / HCE / SPoC), all 12 PCI DSS requirements analysis (network security controls, stored account data protection, transit encryption, malware protection, secure development, access control, authentication, physical security, logging and monitoring, security testing, organizational policies), QSA preparation and ROC readiness, compensating controls documentation, customized approach Targeted Risk Analysis (TRA), third-party service provider (TPSP) management, merchant level and acquirer compliance obligations (Visa, Mastercard, Amex, Discover, JCB), and cross-framework mapping (NIST CSF, SOC 2, ISO 27001, DORA). Produces COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY classified findings, prioritized remediation roadmaps, compensating controls worksheets, SAQ recommendation reports, and Glass Box audit trails. Use when a merchant or service provider needs to determine PCI DSS compliance posture, select the correct SAQ, prepare for a QSA assessment, remediate audit findings, implement scope reduction strategies (tokenization, P2PE, network segmentation), document compensating controls, build a customized approach TRA, map PCI DSS to NIST CSF or SOC 2 for harmonized control implementation, or respond to a card-data breach affecting in-scope systems.


# PCI DSS v4.0.1 Compliance Assessment

> **Disclaimer**: This skill provides an AI-assisted framework for assessing compliance
> with the Payment Card Industry Data Security Standard version 4.0.1 (PCI DSS v4.0.1),
> published by the PCI Security Standards Council (PCI SSC). It does not constitute legal
> advice, regulatory guidance, or a compliance certification. PCI DSS requirements,
> PCI SSC guidance documents, and card-brand enforcement rules change — verify all
> requirement numbers, testing procedures, and validation obligations against the current
> PCI DSS v4.0.1 specification and applicable card-brand programs before relying on them.
> AI-generated compliance analysis carries hallucination risk for cited authority: any
> requirement numbers, SAQ eligibility criteria, or QSA testing procedure references
> should be independently verified against the official PCI SSC documentation at
> pcisecuritystandards.org. This skill does not replace a formal QSA assessment, a
> qualified penetration test, or ASV scanning — it produces a structured framework to
> support human-led compliance work, not a substitute for it. Compliance with PCI DSS
> does not guarantee immunity from card-brand fines, issuer liability, or data breach
> liability — consult qualified legal counsel for those determinations.

---

## Purpose and Scope

This skill assesses an organization's compliance posture against PCI DSS v4.0.1 across
all 12 requirements and supports the full compliance lifecycle from initial scoping
through QSA assessment readiness.

**Covers:**

- Cardholder Data Environment (CDE) scoping and system component classification
- Network segmentation design and validation requirements
- SAQ type determination and eligibility qualification
- All 12 PCI DSS requirement areas with sub-requirement-level analysis
- Future-dated requirement readiness (April 1, 2025 mandatory controls)
- Compensating controls documentation (CCW framework)
- Customized approach Targeted Risk Analysis (TRA) under Req 12.3.2
- Third-party service provider (TPSP) management (Req 12.8)
- QSA/ROC preparation and assessor evidence packaging
- Merchant level determination and acquirer validation obligations
- Cross-framework mapping: PCI DSS ↔ NIST CSF 2.0, SOC 2 TSC, ISO 27001
- DORA overlay for EU-regulated payment processors
- Cloud environment scoping and provider responsibility matrices
- Post-breach compliance re-assessment framework

**Does not:**

- Certify PCI DSS compliance — certification requires a QSA-conducted ROC (Level 1) or
  merchant-signed SAQ; this skill produces assessment documentation, not certification
- Replace an ASV-conducted external vulnerability scan (Req 11.2.1) — those require a
  PCI-approved scanning vendor
- Substitute for a qualified penetration test (Req 11.3) — those require qualified testers
  with defined methodology and organizational independence
- Provide legal opinions on card-brand fine exposure, contractual liability, or litigation
  strategy — consult qualified legal counsel
- Cover non-card payment data standards (EMV, PCI PIN, PCI P2PE as a solution provider
  standard) — those are separate PCI SSC standards with their own assessment regimes
- Apply to PCI DSS predecessor versions (v3.2.1 was retired March 31, 2024)

**Related skills:**

- `legalcode-nist-csf-mapping` — NIST CSF 2.0 maturity assessment with PCI DSS overlay;
  use when mapping PCI DSS to CSF for board-level cybersecurity governance reporting
- `legalcode-incident-response-plan-builder` — multi-regime IR plan builder including
  card-brand breach notification obligations; use when building or testing an IR plan
- `legalcode-vendor-privacy-assessment` — TPRM framework including TPSP PCI DSS compliance
  monitoring; use for ongoing third-party risk management beyond Req 12.8
- `legalcode-dora-compliance-assessment` — DORA ICT risk management for EU financial
  entities; use when a payment processor must comply with both PCI DSS and DORA
- `legalcode-hipaa-compliance-assessment` — HIPAA Security Rule assessment; use when an
  organization processes both card data and protected health information (e.g., healthcare
  payment processors requiring dual-regime compliance)
- `legalcode-sox-compliance-assessment` — SOX IT general controls; use when a public
  company's payment systems intersect with financial reporting controls

---

## Jurisdiction and Governing Law

**Standard**: PCI DSS v4.0.1, published January 31, 2024 by the PCI Security Standards
Council (PCI SSC), a private industry body established by Visa, Mastercard, American
Express, Discover, and JCB. PCI DSS is a **contractual requirement**, not a statute —
compliance obligations arise from merchant agreements and card-brand operating rules, not
from a single governing law.

**Key version milestones**:

- PCI DSS v4.0: Published March 2022; v3.2.1 retired March 31, 2024
- PCI DSS v4.0.1: Published January 31, 2024 (clarifications; not a material revision)
- **April 1, 2025**: All future-dated requirements became mandatory

**Contractual enforcement chain**:
Card brands (Visa, Mastercard, Amex, Discover, JCB) → Acquirers/Issuing Banks →
Processors → Merchants / Service Providers

**[JURISDICTION-SPECIFIC]** Legal obligations vary:

- **United States**: No federal PCI DSS statute; some states reference PCI DSS in data
  breach liability statutes (e.g., Minnesota Plastic Card Security Act, Minn. Stat.
  §§ 325E.64-65; Nevada Rev. Stat. § 603A.215). Breaches may trigger 50-state breach
  notification laws independently of PCI DSS.
- **European Union**: PCI DSS overlaps with GDPR obligations for cardholder personal data;
  DORA (Reg. 2022/2554, effective January 17, 2025) imposes ICT operational resilience
  requirements on EU financial sector entities including payment processors.
- **United Kingdom**: Post-Brexit, UK GDPR applies; UK FCA oversight of payment service
  providers under the Payment Services Regulations 2017 (SI 2017/752).
- **Australia**: Privacy Act 1988 (Cth) and Australian Privacy Principles (APPs) apply
  to cardholder personal data; APRA CPS 234 for regulated financial entities.
- All jurisdictions: Card-brand operating rules impose PCI DSS obligations as a condition
  of accepting card payments, independent of local law.

---

## Interactive Clarification

This skill uses **⟁ CLARIFY** markers at key decision points. When you encounter a
CLARIFY marker, pause and ask the structured questions shown. Only ask when the answer
will materially change the analysis direction. If context has already been provided,
skip that question and proceed.

**Standard clarification format:**

```
⟁ CLARIFY — [Decision point name]

[Short context: why this question matters]

1. [Option A]: [Description]
2. [Option B]: [Description]
3. [Option C]: [Description]

**Why this matters**: [One sentence on how the answer changes the analysis direction]
```

---

## Workflow

### Step 1: Accept Input

Accept input in any of these formats:

- **Organization description**: Entity type (merchant or service provider), industry
  vertical, annual card transaction volume, processing methods, technology stack,
  existing compliance documentation, prior SAQ or ROC status
- **Document set**: Uploaded network diagrams, policies, prior SAQ/ROC findings, ASV
  scan reports, penetration test reports, vendor inventory, incident logs
- **Assessment request**: Prior assessment findings for re-evaluation or annual update
- **Breach trigger**: Post-incident PCI DSS posture review (coordinate with IR workflow)
- **New deployment**: Greenfield compliance build, new payment channel, cloud migration,
  or technology change affecting the CDE

**Minimum required context**: Entity type (merchant or service provider), primary
payment processing methods (card-present, card-not-present, e-commerce), approximate
annual transaction volume, and current compliance posture (no controls / some controls /
formally assessed).

---

### Step 2: Gather Context

**⟁ CLARIFY** — Gather context before beginning. Ask (skip questions already answered):

1. **Assessment objective**: What is the primary goal?
   - _Full PCI DSS compliance assessment_: Comprehensive evaluation of all 12 requirements
   - _CDE scoping and SAQ selection only_: Determine scope and correct self-assessment form
   - _Gap analysis against specific requirements_: Focus on identified weaknesses (specify
     which requirement areas are in question)
   - _QSA/ROC readiness review_: Evidence-packaging and assessor preparation
   - _Compensating controls documentation_: CCW for specific control gaps
   - _Customized approach TRA_: Targeted Risk Analysis for non-standard controls
   - _Annual re-assessment update_: Validate continued compliance after changes
   - _Post-breach posture review_: Identify gaps exposed by a card-data incident
   - **Why this matters**: Full assessment vs. focused review changes depth, deliverables,
     and time investment significantly.

2. **Entity type**: How does this organization relate to payment card data?
   - _Level 1 Merchant_: 6M+ card transactions/year across all card brands
   - _Level 2 Merchant_: 1–6M transactions/year
   - _Level 3 Merchant_: 20,000–1M transactions/year
   - _Level 4 Merchant_: <20,000 transactions/year
   - _Level 1 Service Provider_: 300K+ transactions/year stored, processed, or transmitted
   - _Level 2 Service Provider_: <300K transactions/year
   - _Unsure / need to calculate_: Provide transaction volume and brands accepted
   - **Why this matters**: Merchant/service provider level determines validation method
     (ROC vs. SAQ), assessor requirements (QSA vs. internal), and acquirer obligations.

3. **Processing environment**: How is payment card data handled?
   - _Card-present only_: Physical POS, no e-commerce
   - _Card-not-present (CNP) only_: Mail order / telephone order, no in-person transactions
   - _E-commerce_: Online payments via web application
   - _Mixed_: Both card-present and CNP/e-commerce channels
   - _Service provider role_: Storing/processing/transmitting CHD on behalf of others
   - **Why this matters**: Processing environment is the primary SAQ eligibility driver;
     e-commerce with custom payment pages typically requires SAQ D.

4. **Data storage**: What cardholder data is retained?
   - _No electronic storage_: Only paper receipts; post-authorization data not retained
   - _Tokenized storage_: Only tokens (no PAN/SAD in databases)
   - _Full PAN stored_: PANs retained post-transaction (renders many SAQs ineligible)
   - _Sensitive Authentication Data (SAD) stored_: CVV/track data (prohibited except
     issuers with documented business need)
   - _Unsure — need inventory_: Data discovery and flow mapping required
   - **Why this matters**: Electronic PAN storage eliminates eligibility for SAQ A/B types;
     any SAD storage post-authorization is a Critical Deficiency.

5. **Existing controls**: What security infrastructure is in place?
   - _No formal controls_: Building from scratch
   - _Basic controls_: Firewall, AV, some access controls; no formal PCI compliance program
   - _Mature controls_: Documented policies, SIEM, MFA, ASV scanning in place
   - _ISO 27001 / SOC 2 / NIST CSF certified/implementing_: Existing framework to leverage
   - **Why this matters**: Existing frameworks accelerate compliance; gaps are identifiable
     rather than building from zero.

6. **Third-party technology**: Are third-party payment services in use?
   - _Fully outsourced to validated third party_: Redirect/iframe to PCI-compliant provider
   - _Validated P2PE solution_: Hardware terminal with PCI-listed P2PE (SAQ P2PE eligible)
   - _Partially outsourced_: Some CHD elements handled by third party, some by merchant
   - _In-house payment processing_: Full control of CDE
   - **Why this matters**: Outsourcing to validated providers can dramatically reduce scope
     and enable a less burdensome SAQ type.

---

### Step 3: Determine CDE Scope

**3.1 Define Cardholder Data**

Identify the types of account data in scope:

| Data Element                                  | Category                            | Storage Permitted?                     | Key Restrictions                                 |
| --------------------------------------------- | ----------------------------------- | -------------------------------------- | ------------------------------------------------ |
| Primary Account Number (PAN)                  | Cardholder Data (CHD)               | Yes — but must be rendered unreadable  | AES-256, truncation (max BIN+4), or hash         |
| Cardholder Name                               | CHD                                 | Yes — no restriction                   | No separate encryption required                  |
| Expiration Date                               | CHD                                 | Yes — no restriction                   | No separate encryption required                  |
| Service Code                                  | CHD                                 | Yes — no restriction                   | No separate encryption required                  |
| Full Magnetic Stripe / EMV Chip Data          | Sensitive Authentication Data (SAD) | **No** — prohibited post-authorization | Exception: issuers with documented business need |
| CAV2/CID/CVC2/CVV2 (Card Verification Values) | SAD                                 | **No** — prohibited post-authorization | No exception                                     |
| PIN / PIN Block                               | SAD                                 | **No** — prohibited post-authorization | No exception                                     |

**3.2 System Component Classification**

Classify every system component in the environment:

| Classification                   | Criteria                                                         | PCI DSS Treatment                          |
| -------------------------------- | ---------------------------------------------------------------- | ------------------------------------------ |
| **In-Scope: CDE**                | Stores, processes, or transmits CHD/SAD                          | Full PCI DSS applies                       |
| **In-Scope: Connected**          | Connected to CDE components or able to impact CDE security       | Full PCI DSS applies                       |
| **In-Scope: Security-Impacting** | Provides security services to CDE (DNS, NTP, AD, SIEM, patching) | Full PCI DSS applies                       |
| **Out-of-Scope**                 | Zero connectivity to CDE; zero security impact; no CHD/SAD       | PCI DSS does not apply — document evidence |

> **CRITICAL**: Out-of-scope determination requires documented evidence of zero connectivity
> AND zero security impact. Assumption or verbal assertion is insufficient. The burden of
> proof is on the organization to demonstrate out-of-scope status.

**3.3 Scope Reduction Strategies**

Evaluate and document any scope reduction controls in place:

| Strategy                    | How It Reduces Scope                                                    | SAQ Impact                                                   | Documentation Required                                                                                |
| --------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| **Network Segmentation**    | Isolates CDE from rest of network                                       | Reduces in-scope component count                             | Validated by penetration test and network diagram; not just VLAN configuration                        |
| **Tokenization**            | Replaces PAN with token; no real PAN in tokenized systems               | Systems holding only tokens may be out-of-scope              | Token vault vendor PCI compliance status; data flow confirming no PAN reaches tokenized systems       |
| **Validated P2PE Solution** | Encrypts at point-of-interaction; merchant never handles clear-text CHD | Enables SAQ P2PE (33 questions); significant scope reduction | P2PE solution must appear on PCI SSC validated P2PE list; terminal management via P2PE provider       |
| **Full Outsourcing**        | Third-party handles all CHD; merchant uses redirect/hosted payment page | May enable SAQ A (minimal requirements)                      | Third-party must have valid PCI DSS certification/AOC; merchant has no CHD flow through their systems |

**3.4 Network Segmentation Validation Requirements**

Network segmentation reduces scope only when:

- **Purpose-built**: Segmentation is intentionally configured to isolate CDE, not just
  VLANs assumed to separate traffic
- **Tested**: Annually, and after significant changes, segmentation must be validated via
  penetration testing confirming isolation (Req 11.4.5)
- **Documented**: Network diagrams showing all connections into/out of CDE; firewall rule
  review at least every 6 months (Req 1.2.2)
- **Monitored**: All traffic crossing segmentation boundaries logged; unauthorized
  crossing attempts generate alerts

> **⟁ CLARIFY** — Segmentation Validation Status
>
> Has existing network segmentation been formally validated?
>
> 1. _Yes — tested by penetration test within last 12 months_: Document segmentation
>    boundary and proceed with reduced scope
> 2. _Yes — but not tested by penetration test_: Segmentation cannot be relied upon for
>    scope reduction until validated; treat all connected systems as in-scope
> 3. _No formal segmentation in place_: Full flat-network scope applies; document all
>    in-scope components
> 4. _Unsure_: Conduct network mapping before scoping; segmentation cannot be assumed
>
> **Why this matters**: Unvalidated segmentation is a common ROC finding; QSAs cannot
> accept undocumented claims of segmentation for scope reduction purposes.

---

### Step 4: SAQ Type Determination

Evaluate SAQ eligibility based on the merchant's processing environment, technology stack,
and third-party arrangements. Present the recommended SAQ type with eligibility evidence.

#### SAQ Eligibility Matrix

| SAQ Type                     | Eligible Merchant/SP Profile                                                                                                         | Typical Question Count | Key Exclusions                                                                         |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------- | -------------------------------------------------------------------------------------- |
| **SAQ A**                    | CNP merchants only; fully outsourced to validated third party; no electronic CHD storage; no website code accessing CHD              | ~20                    | Card-present transactions; any merchant website code touching CHD; partial outsourcing |
| **SAQ A-EP**                 | E-commerce merchants; third-party handles CHD; merchant's website only receives payment data (no direct CHD storage/processing)      | ~190                   | Card-present; merchant storing CHD; merchant's servers processing CHD                  |
| **SAQ B**                    | Card-present via imprint-only machines or standalone dial-up/dial-out terminals; no electronic CHD storage                           | ~40                    | IP-connected terminals; e-commerce; electronic storage                                 |
| **SAQ B-IP**                 | Card-present via IP-connected certified PTS devices; no electronic CHD storage; isolated payment terminal network                    | ~80                    | E-commerce; electronic storage; non-certified terminals                                |
| **SAQ C**                    | Card-present via internet-connected payment application; no electronic CHD storage; payment app isolated from other business systems | ~160                   | Electronic storage; e-commerce channel; systems not isolated                           |
| **SAQ C-VT**                 | Web-based virtual terminal only (single manual-entry transaction at a time); isolated device; no electronic storage                  | ~80                    | Batch processing; electronic storage; multiple concurrent transactions                 |
| **SAQ D (Merchant)**         | All merchants not qualifying for A–C; electronic storage; complex environments                                                       | ~328                   | N/A — catch-all for merchants                                                          |
| **SAQ D (Service Provider)** | All service providers eligible for SAQ (Level 2)                                                                                     | ~328                   | N/A — catch-all for SPs                                                                |
| **SAQ P2PE**                 | Card-present using only PCI-validated P2PE hardware solution; no electronic storage                                                  | ~33                    | Software-based encryption; non-validated P2PE solutions; e-commerce                    |
| **SAQ HCE**                  | Mobile NFC payment using Host Card Emulation; controlled access; no electronic storage                                               | ~50                    | Traditional POS; e-commerce                                                            |
| **SAQ SPoC**                 | Secure Payment on Cloud (SPoC) validated solutions only; mobile devices with secure card reader                                      | ~35                    | Non-validated SPoC solutions                                                           |

#### SAQ Determination Decision Tree

```
Is the merchant a Level 1 (6M+ transactions)?
  ├─ YES → ROC required (QSA-led); SAQ not applicable
  └─ NO → Continue SAQ selection

Are all transactions card-present (no e-commerce, no CNP)?
  ├─ P2PE validated solution only? → SAQ P2PE
  ├─ Imprint or standalone dial-up only? → SAQ B
  ├─ IP-connected PTS device, isolated network? → SAQ B-IP
  ├─ Internet-connected payment app, no storage? → SAQ C
  └─ Complex / storage / other → SAQ D (Merchant)

Are all transactions card-not-present / e-commerce?
  ├─ Fully outsourced, redirect/hosted page, no merchant website code? → SAQ A
  ├─ Third-party handles CHD, but merchant website receives data? → SAQ A-EP
  ├─ Virtual terminal only, isolated device, no storage? → SAQ C-VT
  └─ Complex / storage / custom payment app → SAQ D (Merchant)

Mixed card-present + CNP/e-commerce?
  └─ SAQ D (Merchant) — multi-channel requires full assessment
```

> **⟁ CLARIFY** — SAQ Eligibility Confirmation
>
> Based on the processing environment described, the recommended SAQ type is [X].
> Before proceeding, confirm these eligibility facts:
>
> 1. _Confirm no electronic CHD storage_ (required for all SAQs except D): [describe
>    > how post-authorization data is handled]
> 2. _Confirm third-party PCI compliance status_ (for SAQ A/A-EP): Has the third-party
>    provider provided a current AOC? What is the AOC coverage date?
> 3. _Confirm processing method accuracy_: Are there any payment channels not yet described
>    (e.g., phone orders, recurring billing, loyalty program redemption)?
>
> **Why this matters**: Incorrect SAQ selection is a material compliance risk; using a
> simpler SAQ than the environment warrants creates exposure to card-brand fines and
> breach liability.

---

### Step 5: Analyze All 12 PCI DSS Requirements

For each requirement, assess compliance status, identify gaps, and assign severity
classification. Apply the **Defined Approach** unless the organization is implementing
a **Customized Approach** for specific requirements (see Step 7).

---

#### Requirement 1 — Install and Maintain Network Security Controls

**Security objective**: Protect CDE from unauthorized network traffic; deny all traffic
not explicitly required.

| Sub-Requirement | Control Description                                                                       | Evidence Required                                                  |
| --------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| 1.2.1           | Firewall rules restrict inbound/outbound CDE traffic to documented minimum necessary      | Firewall rule review; data flow diagram; change management records |
| 1.2.2           | All firewall rule changes follow documented change control; rules reviewed every 6 months | Change logs; biannual review records                               |
| 1.2.3           | Firewalls between all wireless networks and CDE; only authorized traffic permitted        | Network diagram; wireless firewall configuration; scan results     |
| 1.3.1           | Inbound traffic to CDE restricted to that necessary for the cardholder data environment   | Firewall configuration review                                      |
| 1.3.2           | Outbound traffic from CDE restricted to that necessary                                    | Firewall configuration review; egress filtering evidence           |
| 1.4.1           | Network security controls separate trusted/untrusted networks                             | Network diagram; segmentation test results                         |
| 1.4.2           | Prohibit direct public access between internet and CDE components                         | Firewall rules; DMZ architecture                                   |
| 1.5.1           | Security controls for devices connecting to both internet and CDE                         | Split-tunneling policy; MDM records                                |

**Common findings**: Missing egress filtering (outbound traffic unrestricted); firewall
rule bloat (dozens of "any-any" rules); undocumented temporary rules never removed;
wireless networks bridging to CDE without inspection; overly broad DMZ allowing lateral
movement.

---

#### Requirement 2 — Apply Secure Configurations to All System Components

**Security objective**: Eliminate known vulnerabilities introduced by vendor defaults and
misconfigured systems.

| Sub-Requirement | Control Description                                                    | Evidence Required                                                     |
| --------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------- |
| 2.1.1           | All vendor-supplied defaults changed before deployment                 | Configuration baseline; hardening checklist; scan results             |
| 2.2.1           | Configuration standards developed for all component types              | Written configuration standards; CIS Benchmark or DISA STIG alignment |
| 2.2.7           | All non-console administrative access encrypted                        | SSH/TLS configuration evidence; no Telnet/FTP                         |
| 2.3.1           | Wireless environments: change defaults (SSID, passwords, SNMP strings) | Wireless configuration review                                         |

**Reference standards**: CIS Benchmarks, DISA STIGs, vendor hardening guides, NIST
SP 800-70. At minimum, configuration standards must address: operating systems, network
devices, applications, databases, and virtualization platforms.

---

#### Requirement 3 — Protect Stored Account Data

**Security objective**: Protect stored cardholder data using strong cryptography or
rendering methods; prohibit SAD storage post-authorization.

| Sub-Requirement | Control Description                                                                                | Evidence Required                                                                                           |
| --------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| 3.2.1           | SAD not stored post-authorization (except issuer with documented need)                             | Database schema review; data discovery scan; application architecture review                                |
| 3.3.1           | SAD stored before completion of authorization is encrypted                                         | Encryption configuration; key management policy                                                             |
| 3.4.1           | PAN rendered unreadable wherever stored                                                            | Encryption specification (AES-256 preferred); hash specification (HMAC-SHA-256+); truncation implementation |
| 3.5.1           | PAN secured with strong cryptography: keys documented, key custodians trained                      | Key management policy; key inventory; custodian training records                                            |
| 3.6.1           | Key management procedures cover generation, distribution, storage, access, retirement, replacement | Key management policy; key ceremony records; KMS configuration                                              |
| 3.7.1           | Key management procedures for systems using cryptographic keys                                     | HSM implementation; no keys in source code or plaintext files                                               |

**Permitted PAN protection methods**:

- **AES-256 encryption**: Industry standard; keys must be managed separately from encrypted data; HSM recommended
- **HMAC-SHA-256 (or stronger) hashing**: Keyed hash of entire PAN; cannot be reversed without key; cannot be combined with truncation
- **Truncation**: Retain maximum first 6 + last 4 digits only; remaining digits permanently removed
- **Tokenization**: Replace PAN with token lacking exploitable value; tokens stored in separate vault (out-of-scope if segmented)

> **CRITICAL DEFICIENCY TRIGGER**: Any SAD (CVV, track data, PIN) stored post-authorization
> is an automatic Critical Deficiency regardless of encryption. Requires immediate remediation.

---

#### Requirement 4 — Protect Cardholder Data with Strong Cryptography During Transmission over Open/Public Networks

**Security objective**: Prevent interception of cardholder data in transit.

| Sub-Requirement | Control Description                                                                             | Evidence Required                                                                               |
| --------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| 4.1.1           | Wireless networks transmitting CHD or connected to CDE use strong cryptography                  | Wireless security configuration; WPA3 or WPA2-AES preferred                                     |
| 4.2.1           | Strong cryptography used; only trusted keys/certificates accepted                               | TLS configuration (1.2+ required; 1.3 preferred); SSL/TLS 1.0/1.1 disabled; cipher suite review |
| 4.2.1.1         | Certificate inventory for keys/certificates protecting PAN in transit [Mandatory April 1, 2025] | Certificate inventory; expiration monitoring; revocation check procedures                       |
| 4.2.2           | PANs secured with strong cryptography in end-user messaging                                     | Email/SMS/chat security controls; no PAN in plain-text messages                                 |

**Prohibited protocols** (must be disabled/removed): SSLv2, SSLv3, TLS 1.0, TLS 1.1, RC4,
DES, 3DES (TDES). Verify no legacy fallback capability exists.

**Mandatory cipher suites**: TLS 1.2+ with forward secrecy preferred (ECDHE);
AES-GCM/AES-CBC; SHA-256+. Weak ciphers (RC4, DES, NULL, EXPORT, ANON) explicitly prohibited.

---

#### Requirement 5 — Protect All Systems and Networks from Malicious Software

**Security objective**: Prevent malware from compromising system components.

| Sub-Requirement | Control Description                                                                                        | Evidence Required                                                            |
| --------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 5.2.1           | Anti-malware deployed on applicable components (covers all malware types)                                  | AV/EDR deployment inventory; coverage report                                 |
| 5.2.2           | Anti-malware detects, removes, and protects against all known types of malware                             | EDR capabilities documentation; threat coverage assessment                   |
| 5.3.1           | Anti-malware kept current (automatic definition updates)                                                   | Update policy; scheduled scan configuration                                  |
| 5.3.2           | Periodic scans performed (or continuous behavioral monitoring)                                             | Scan schedule; scan logs                                                     |
| 5.3.3           | Anti-malware cannot be disabled/altered by users unless documented exception (time-limited, risk-accepted) | Anti-tamper configuration; exception log                                     |
| 5.4.1           | Anti-phishing mechanisms for users                                                                         | Email security gateway; user awareness training; phishing simulation records |

**Modern implementations**: Endpoint Detection and Response (EDR) platforms (CrowdStrike,
SentinelOne, Microsoft Defender ATP) satisfy Req 5 more comprehensively than signature-only
AV. Application whitelisting (allowlisting) on high-risk systems recommended.

---

#### Requirement 6 — Develop and Maintain Secure Systems and Software

**Security objective**: Prevent exploitation of vulnerabilities in systems and applications.

| Sub-Requirement | Control Description                                                                                     | Evidence Required                                                  |
| --------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| 6.2.1           | Bespoke/custom software developed per secure coding guidelines                                          | SDLC policy; secure coding standards (OWASP Top 10 alignment)      |
| 6.2.4           | Training for developers in secure coding (annually)                                                     | Training records; curriculum                                       |
| 6.3.1           | Security vulnerabilities identified and assigned risk ranking                                           | Vulnerability management policy; CVSS scoring methodology          |
| 6.3.2           | Inventory of bespoke/custom software maintained                                                         | Software inventory; SBOM where applicable                          |
| 6.3.3           | All software protected from known vulnerabilities via security patches                                  | Patch management policy; patch records; CVSS-based prioritization  |
| 6.4.1           | Web-facing applications protected against web-based attacks                                             | WAF (preferred) or code-review program; OWASP Top 10 coverage      |
| 6.4.2           | Automated technical solution deployed to detect and prevent web-based attacks [Mandatory April 1, 2025] | WAF deployment and active blocking mode evidence                   |
| 6.4.3           | All payment page scripts authorized, integrity-checked, and inventoried [Mandatory April 1, 2025]       | Script inventory; SRI hash verification; third-party script policy |

**Vulnerability remediation timelines** (updated April 1, 2025):

- **Critical (CVSS 9.0–10.0)**: Patch within **30 days**
- **High (CVSS 7.0–8.9)**: Patch within **3 months** (sooner if risk warrants)
- **Medium/Low**: Address per organization's risk-ranked timeline

**OWASP Top 10 coverage required** (minimum): Injection, Broken Authentication, Insecure
Direct Object References, Security Misconfiguration, Cryptographic Failures, Vulnerable
Components, Identification/Authentication Failures, SSRF, XXE, Insecure Deserialization.

**E-commerce script management** (Req 6.4.3): All JavaScript executing on payment pages —
whether first-party or third-party CDN-loaded — must be inventoried, authorized, and
integrity-protected (Subresource Integrity / SRI hashes or Content Security Policy).
This is a critical Magecart/skimmer attack mitigation.

---

#### Requirement 7 — Restrict Access to System Components and Cardholder Data by Business Need to Know

**Security objective**: Ensure only authorized individuals can access CDE; deny all other
access by default.

| Sub-Requirement | Control Description                                                    | Evidence Required                                                   |
| --------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------- |
| 7.2.1           | Access control system(s) in place for all CDE components               | IAM system documentation; role definitions                          |
| 7.2.2           | Access assigned based on job classification/function (least privilege) | Access matrix; role definitions; job function mapping               |
| 7.2.3           | Required approvals documented for access granted                       | Access request/approval workflow; ticket records                    |
| 7.2.4           | User access reviewed at least every 6 months                           | Access review logs; certification records; offboarding verification |
| 7.2.5           | Application/system accounts and access reviewed                        | Service account inventory; access rights review                     |
| 7.3.1           | All access to CDE components managed via access control system         | No manual/ad-hoc access grants; IAM system is authoritative         |

**Default-deny principle**: All access to CDE components must be explicitly denied unless
a specific rule grants access based on documented business need. "Default allow with
exceptions" is non-compliant.

---

#### Requirement 8 — Identify Users and Authenticate Access to System Components

**Security objective**: Ensure every access to CDE is tied to a unique, authenticated
individual; prevent unauthorized access via compromised credentials.

| Sub-Requirement | Control Description                                                                        | Evidence Required                                                              |
| --------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| 8.2.1           | All user IDs unique; no shared/generic credentials for CDE access                          | User account inventory; no shared IDs                                          |
| 8.2.2           | Group/shared accounts managed only when operationally necessary (service accounts)         | Policy; service account inventory; purpose documentation                       |
| 8.3.4           | Invalid authentication attempts limited to 6; lockout ≥30 min                              | Account lockout policy configuration                                           |
| 8.3.6           | Password/passphrase minimum length ≥12 characters (if used)                                | Password policy configuration                                                  |
| 8.3.9           | Passwords/passphrases changed every 3 months (if no risk-based authentication)             | Password rotation policy; automated enforcement                                |
| 8.3.10          | Guidance provided re: protecting passwords from disclosure                                 | Security awareness training; policy                                            |
| 8.4.1           | MFA implemented for all non-console administrative access to CDE [Mandatory April 1, 2025] | MFA configuration; admin access logs                                           |
| 8.4.2           | MFA implemented for all non-console access into the CDE [Mandatory April 1, 2025]          | MFA configuration for all CDE user roles                                       |
| 8.4.3           | MFA for all remote network access originating from outside entity's network                | VPN/remote access MFA configuration                                            |
| 8.5.1           | MFA systems implemented to prevent replay attacks; all factors must succeed                | MFA vendor configuration; independence of factors                              |
| 8.6.1           | Application/system accounts managed and authenticated strongly                             | Service account credential policy; no hardcoded passwords                      |
| 8.6.2           | Passwords/passphrases not hardcoded in scripts/applications [Mandatory April 1, 2025]      | Code review; secrets management solution                                       |
| 8.6.3           | Passwords for application/system accounts protected from misuse [Mandatory April 1, 2025]  | Privileged Access Management (PAM) solution; vault-based credential management |

**MFA implementation requirements** (Req 8.4.2 — April 1, 2025 mandatory):

- **Expanded scope**: MFA now required for ALL non-console CDE access, not just remote access
- **Factor independence**: At least two different authentication factor types must succeed
- **No bypass**: MFA cannot be bypassed under any circumstances except documented, time-limited management exceptions
- **Factor types**: Something you know (password/passphrase) + something you have (hardware token, authenticator app, smart card) or something you are (biometric)
- **OTP/TOTP**: Software authenticators (Google Authenticator, Microsoft Authenticator, Duo) satisfy "something you have" — phishing-resistant hardware keys (FIDO2/WebAuthn) preferred for highest assurance

> **⟁ CLARIFY** — MFA Coverage Verification
>
> The April 1, 2025 MFA expansion is one of the highest-impact v4.0 changes.
>
> 1. _MFA in place for all CDE access (console + remote)_: Document coverage and proceed
> 2. _MFA for remote access only (pre-April 2025 configuration)_: Gap exists for
>    non-remote CDE access — requires remediation; this is now a NON-COMPLIANT finding
> 3. _No MFA implemented_: CRITICAL DEFICIENCY — immediate remediation required
>
> **Why this matters**: Failure to implement MFA for all CDE access is the single most
> commonly cited v4.0 gap finding and a Critical Deficiency trigger.

---

#### Requirement 9 — Restrict Physical Access to Cardholder Data

**Security objective**: Prevent unauthorized physical access to CDE components and devices.

| Sub-Requirement | Control Description                                                | Evidence Required                                           |
| --------------- | ------------------------------------------------------------------ | ----------------------------------------------------------- |
| 9.1.1           | Security controls implemented to restrict physical access to CDE   | Badging system; locks; key management                       |
| 9.2.1           | Individual identification of visitors and badge management         | Visitor log; badge issuance records; escort policy          |
| 9.2.2           | Visitor badges expire or are distinguishable; visitors escorted    | Badge policy; visitor log review                            |
| 9.3.2           | Physical access rights reviewed at least annually                  | Physical access review records                              |
| 9.4.1           | Media with cardholder data protected                               | Media classification policy; secure storage evidence        |
| 9.4.2           | Media sent outside facility via secured courier / tracked shipment | Courier policy; shipment logs                               |
| 9.4.5           | Electronic media destroyed before disposal; destruction documented | Media destruction policy; certificates of destruction       |
| 9.5.1           | Point-of-interaction (POI) devices protected from tampering        | Device inventory; tamper inspection policy; inspection logs |
| 9.5.1.1         | POI device surface inspections conducted periodically              | Inspection log; training for staff                          |
| 9.5.1.2         | POI device training for personnel to detect tampering/substitution | Training records; awareness materials                       |

---

#### Requirement 10 — Log and Monitor All Access to System Components and Cardholder Data

**Security objective**: Detect unauthorized access and anomalous activity in real time;
preserve evidence for forensic investigation.

| Sub-Requirement | Control Description                                                                                                                                  | Evidence Required                                                    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| 10.2.1          | Audit log captures required events (user actions, root/admin access, auth events, changes, audit log access, initialization/stop/pause of audit log) | Log configuration; sample log review                                 |
| 10.2.1.1-7      | Specific event types captured per sub-requirement                                                                                                    | Log configuration checklist                                          |
| 10.3.1          | Audit logs read-only / protected from destruction or modification                                                                                    | Log integrity controls; SIEM immutable log storage                   |
| 10.3.2          | Audit log protected from unauthorized access                                                                                                         | RBAC on log system; network controls                                 |
| 10.3.3          | Audit log files backed up promptly to centralized log server                                                                                         | SIEM/log aggregation architecture                                    |
| 10.4.1          | Daily log review process for all CDE components [Automated by April 1, 2025]                                                                         | SIEM alert configuration; manual review SOPs; alert response records |
| 10.4.1.1        | Automated mechanisms used to perform log reviews [Mandatory April 1, 2025]                                                                           | SIEM deployment; automated alerting; correlation rules               |
| 10.5.1          | Retain audit logs ≥12 months; last 3 months readily available                                                                                        | Log retention configuration; archival policy                         |
| 10.6.1          | Maintain accurate time synchronization on all CDE systems (NTP)                                                                                      | NTP configuration; time source documentation                         |
| 10.7.1          | Failures of critical security controls detected, alerted, reported, and responded to promptly                                                        | Monitoring configuration; alert records; response procedures         |

**Log retention requirements**: 12 months total; last 3 months must be immediately available
for analysis (not archived/offlined). Immutable logging strongly recommended (write-once
storage, SIEM with tamper-detection).

**SIEM implementation**: While not explicitly mandated by name, Req 10.4.1.1 (effective
April 1, 2025) effectively requires automated log review — making SIEM or equivalent
log analysis platform a practical necessity for any organization with more than a handful
of in-scope systems.

---

#### Requirement 11 — Test Security of Systems and Networks Regularly

**Security objective**: Identify vulnerabilities before attackers do; validate segmentation
and security controls through independent testing.

| Sub-Requirement | Control Description                                                                | Evidence Required                                                           |
| --------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| 11.2.1          | Quarterly internal vulnerability scans; rescan until no high-risk vulnerabilities  | Scan reports (quarterly); remediation evidence                              |
| 11.2.2          | Quarterly external vulnerability scans by ASV; passing scans required              | ASV scan reports (quarterly, from PCI-approved ASV); passing status         |
| 11.3.1          | Annual external penetration test by qualified internal/external tester             | Penetration test report; tester qualifications; scope documentation         |
| 11.3.1.1        | All exploitable vulnerabilities remediated; retest conducted                       | Remediation records; retest report                                          |
| 11.3.2          | Annual internal penetration test                                                   | Internal pen test report; methodology documentation                         |
| 11.3.2.1        | Segmentation controls tested at least annually and after changes                   | Segmentation test methodology; test results confirming isolation            |
| 11.4.1          | Intrusion-detection/prevention system (IDS/IPS) in place                           | IDS/IPS deployment architecture; alert configuration                        |
| 11.5.1          | Intrusion-detection mechanisms detect unauthorized file changes, alert personnel   | FIM (File Integrity Monitoring) implementation; alert logs                  |
| 11.5.2          | Change-detection mechanism deployed for payment pages [Mandatory April 1, 2025]    | Payment page integrity monitoring solution; alert evidence                  |
| 11.6.1          | Change- and tamper-detection mechanism for payment pages [Mandatory April 1, 2025] | HTTP header monitoring; CSP implementation; real-time page integrity alerts |

**ASV scan requirements** (Req 11.2.2): Must use a PCI-approved Approved Scanning Vendor
(full list at pcisecuritystandards.org). Passing scan requires no High (CVSS 4.0+) or
Critical vulnerabilities unresolved. At least one passing scan required per quarter;
rescans required after significant changes.

**Penetration testing methodology**: Must include external and internal perspectives;
segmentation testing (confirming no path from non-CDE to CDE); application layer testing
for internet-facing systems. Testers must have defined methodology (PTES, OSSTMM,
NIST SP 800-115); results must be validated with evidence of remediation.

---

#### Requirement 12 — Support Information Security with Organizational Policies and Programs

**Security objective**: Embed security into organizational governance; manage third-party risk;
maintain an incident response capability.

| Sub-Requirement | Control Description                                                                           | Evidence Required                                                      |
| --------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 12.1.1          | Information security policy established, published, and reviewed annually                     | Policy document; annual review evidence; distribution records          |
| 12.1.2          | Information security policy reviewed at least once every 12 months                            | Review sign-off; version history                                       |
| 12.2.1          | Acceptable use policies defined for all technologies in use                                   | Acceptable Use Policy; coverage of end-user devices                    |
| 12.3.1          | Cardholder data environment risks formally identified and managed                             | Risk assessment documentation; risk register                           |
| 12.3.2          | Targeted Risk Analysis for each customized approach requirement                               | TRA per requirement; controls matrix; management approval [see Step 7] |
| 12.3.3          | All cryptographic cipher suites and protocols inventoried and reviewed                        | Cryptographic inventory; annual review; deprecation tracking           |
| 12.3.4          | Hardware/software reviewed annually for continued PCI DSS support eligibility                 | Technology lifecycle review; vendor EOL tracking                       |
| 12.4.1          | Service provider: executive management responsibility assigned for PCI DSS                    | Board/executive responsibility assignment document                     |
| 12.5.1          | PCI DSS scope and in-scope components documented; updated annually and after changes          | Scope documentation; annual review; change-triggered update process    |
| 12.5.2          | PCI DSS scope confirmed at least once every 12 months and after changes                       | Scope confirmation sign-off; trigger for changes                       |
| 12.6.1          | Security awareness program in place; employees trained at hire and annually                   | Training program documentation; completion records                     |
| 12.6.3          | Personnel understand and acknowledge policies annually                                        | Acknowledgment records                                                 |
| 12.8.1          | List of TPSPs who have CHD access or can impact CDE security maintained                       | TPSP inventory; service descriptions                                   |
| 12.8.2          | Written agreements with TPSPs confirming their PCI DSS obligations                            | TPSP agreements; PCI DSS responsibility clauses                        |
| 12.8.3          | Due diligence on TPSPs before engagement                                                      | Vendor assessment records; AOC/ROC review for each TPSP                |
| 12.8.4          | TPSP compliance status monitored at least annually                                            | Annual AOC/ROC review records; compliance confirmation                 |
| 12.8.5          | Responsibility matrix maintained for shared PCI DSS requirements                              | Shared responsibility matrix (PCI DSS control-by-control)              |
| 12.9.1          | Service provider: acknowledge to customers in writing which PCI DSS requirements are in scope | Customer acknowledgment letters/agreements                             |
| 12.10.1         | Incident response plan established; tested annually                                           | IRP document; tabletop test records; contact list                      |
| 12.10.5         | Alerts from security monitoring included in incident response                                 | IRP integration with SIEM/monitoring; alert routing                    |
| 12.10.7         | Procedures for responding to detection of stored PAN where not expected                       | Data discovery response procedures                                     |

**TPSP management (Req 12.8)**: Every third-party service provider with access to CHD
or the ability to impact CDE security must be inventoried, covered by written PCI DSS
obligations, assessed annually (via their AOC/ROC review), and tracked in a shared
responsibility matrix. "Impact CDE security" includes cloud providers, managed security
services, IT support, and SaaS tools with access to in-scope systems — even if they never
see raw PANs.

---

### Step 6: Severity Classification and Finding Prioritization

Classify each identified gap using a four-tier system and assign remediation priority:

#### Severity Classification

| Classification          | Criteria                                                                                                               | Examples                                                                                                                                                                   |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CRITICAL DEFICIENCY** | Fundamental control failure creating immediate, significant risk; card-brand reportable; potential liability trigger   | SAD stored post-authorization; no encryption on stored PAN; MFA completely absent; SSL/TLS 1.0 still active; no network segmentation with flat access to CHD               |
| **NON-COMPLIANT**       | Requirement not met; clear gap that must be remediated before compliance attestation                                   | Incomplete MFA coverage (partial implementation); no ASV scanning; log retention <12 months; firewall rules not reviewed in >12 months; no penetration test in >12 months  |
| **PARTIAL**             | Requirement partially met; compensating control may exist; gap is documentable but does not create immediate high risk | SAQ eligibility uncertain pending vendor AOC review; configuration standards exist but not fully applied; patch process exists but timelines missed for low-severity items |
| **COMPLIANT**           | Requirement fully met with documented evidence                                                                         | All controls in place; evidence available for QSA review; no material gaps                                                                                                 |

#### Prioritization Framework

**Tier 1 — Immediate (within 30 days)**:

- All CRITICAL DEFICIENCY findings
- Req 3: SAD stored post-authorization (immediate data destruction required)
- Req 4: Prohibited protocols (SSL/TLS 1.0) still active on CHD transmission paths
- Req 8: No MFA for CDE access (all channels)
- Any finding creating active exploitable risk

**Tier 2 — Near-Term (within 90 days)**:

- NON-COMPLIANT findings not in Tier 1
- Missing ASV scans (next scan within quarter)
- Missing penetration test (schedule immediately)
- Incomplete log retention
- TPSP inventory and AOC gaps

**Tier 3 — Planned (within 6 months)**:

- PARTIAL findings requiring process improvement
- Configuration standard gaps
- Training and awareness gaps
- Documentation completeness issues

**Tier 4 — Background (within 12 months)**:

- Long-term architectural improvements (segmentation redesign, tokenization implementation)
- Framework harmonization (NIST CSF mapping, SOC 2 alignment)
- Enhanced monitoring capabilities

---

### Step 7: Compensating Controls and Customized Approach

#### 7a. Compensating Controls (CCW)

For findings where the defined requirement cannot be met due to a documented legitimate
technical or business constraint, prepare a Compensating Controls Worksheet (CCW):

**CCW Required Elements** (one per compensating control):

```
1. Constraint: [Technical or business reason why the defined requirement cannot be met]
2. Objective: [What the original requirement is designed to achieve]
3. Risk Identified: [Specific risks posed by the constraint]
4. Compensating Control: [Alternative controls addressing the risk; must exceed the
   security intent of the original control; cannot simply restate other PCI DSS requirements]
5. Validation: [How the compensating control is tested; testing methodology and results]
6. Maintenance: [How the control will remain effective going forward; annual review plan]
```

**Eligibility criteria for compensating controls**:

- The control must be above and beyond other PCI DSS requirements already in place
- The original constraint must be legitimate (not cost or preference)
- The control must address the risk created by the original gap
- Must be implemented at time of gap identification — not retroactively
- QSA/ISA must validate the compensating control as sufficient

> **⟁ CLARIFY** — Compensating Control Eligibility
>
> For [requirement X], the proposed compensating control is [describe control].
>
> 1. _Document as CCW_: Constraint is legitimate, control exceeds standard security
>    posture, QSA will validate — proceed with CCW
> 2. _Remediate the gap instead_: Control cannot be documented as compensating (e.g.,
>    cost constraint is not eligible; proposed control merely restates another requirement)
> 3. _Explore customized approach_: If the organization wants to permanently implement
>    an alternative design, Customized Approach under Req 12.3.2 may be more appropriate
>
> **Why this matters**: Improperly documented CCWs are rejected by QSAs; legitimate
> compensating controls must be validated, not assumed.

#### 7b. Customized Approach (Targeted Risk Analysis)

For each PCI DSS requirement implemented via the Customized Approach, prepare a
Targeted Risk Analysis (TRA) per Req 12.3.2:

**TRA Required Elements**:

```yaml
customized_approach_tra:
  requirement: "[PCI DSS requirement number and title]"
  customized_approach_objective: "[Verbatim objective from PCI DSS v4.0.1 Appendix D]"

  risk_analysis:
    threats_identified:
      - "[Threat 1 the requirement objective addresses]"
      - "[Threat 2]"
    likelihood_assessment: "[HIGH / MEDIUM / LOW with rationale]"
    impact_assessment: "[HIGH / MEDIUM / LOW with rationale]"
    inherent_risk: "[Combined risk level without controls]"

  controls_design:
    custom_controls:
      - control: "[Custom control description]"
        how_it_addresses_objective: "[Mapping to objective]"
        how_it_reduces_identified_risks: "[Risk-control mapping]"
    controls_matrix: "[Reference to detailed controls matrix document]"

  testing_plan:
    testing_procedures: "[How controls will be tested/validated]"
    success_criteria: "[What passing looks like]"
    testing_frequency: "[Annual / quarterly / continuous]"

  governance:
    senior_management_approval:
      approver: "[Name, title]"
      approval_date: "[Date]"
    annual_review_date: "[Next review date]"
    reviewed_by: "[QSA name if applicable]"
```

---

### Step 8: Third-Party Service Provider (TPSP) Inventory

For each TPSP with CHD access or CDE security impact, document:

| TPSP Name       | Service Type                                    | CHD Access                                        | PCI DSS Scope                                      | AOC/ROC Status                                       | AOC Expiration | Responsibility Matrix       |
| --------------- | ----------------------------------------------- | ------------------------------------------------- | -------------------------------------------------- | ---------------------------------------------------- | -------------- | --------------------------- |
| [Provider name] | [Cloud / Payment processor / Managed IT / etc.] | [Direct / Indirect / None but security-impacting] | [Services covered by TPSP's PCI DSS certification] | [Compliant — AOC received / Pending / Not confirmed] | [Date]         | [Responsibility matrix ref] |

**TPSP management checklist**:

- [ ] TPSP inventory maintained and current (Req 12.8.1)
- [ ] Written agreements include PCI DSS responsibility clauses (Req 12.8.2)
- [ ] Due diligence conducted before engagement (Req 12.8.3)
- [ ] Annual AOC/ROC review completed (Req 12.8.4)
- [ ] Shared responsibility matrix documented for each TPSP (Req 12.8.5)
- [ ] For service providers: customer acknowledgment letters issued (Req 12.9.1)

---

### Step 9: Cross-Framework Mapping

#### PCI DSS v4.0.1 ↔ NIST CSF 2.0 Alignment

| PCI DSS Req                | NIST CSF 2.0 Function/Category | Overlap Notes                                     |
| -------------------------- | ------------------------------ | ------------------------------------------------- |
| Req 1 (Network Controls)   | PR.AC-5, PR.PT-3, PR.PT-4      | Strong overlap; CSF adds asset-based segmentation |
| Req 2 (Secure Config)      | PR.IP-1, PR.PT-3               | CSF adds supply chain context                     |
| Req 3 (Stored Data)        | PR.DS-1, PR.DS-5               | CSF broader (all data); PCI specific to CHD       |
| Req 4 (Transit Encryption) | PR.DS-2                        | Near-identical objective                          |
| Req 5 (Malware)            | DE.CM-4, PR.PT-3               | EDR/behavioral analysis covered by both           |
| Req 6 (Secure Dev)         | PR.IP-2, PR.IP-12, ID.RA-1     | CSF adds software supply chain risk (GV.SC)       |
| Req 7 (Access Control)     | PR.AC-1, PR.AC-3, PR.AC-4      | Near-identical; CSF adds identity governance      |
| Req 8 (Authentication)     | PR.AC-6, PR.AC-7               | PCI more specific on MFA thresholds               |
| Req 9 (Physical)           | PR.AC-2                        | Near-identical scope                              |
| Req 10 (Logging)           | DE.CM-1, DE.CM-3, RS.AN-1      | PCI adds specific retention periods               |
| Req 11 (Testing)           | ID.RA-1, DE.CM-8, RS.AN-3      | PCI mandates specific scan/test frequency         |
| Req 12 (Governance)        | GV.OC-1, GV.RM-1, RS.MI-2      | CSF adds supply chain governance (GV.SC)          |

**Harmonization value**: Organizations already implementing NIST CSF 2.0 typically achieve
60–75% PCI DSS coverage; remaining gaps concentrate in PCI-specific requirements
(ASV scanning, QSA validation, specific retention periods, card-brand-specific TPSP rules).

#### PCI DSS v4.0.1 ↔ SOC 2 Alignment

| PCI DSS Cluster           | SOC 2 Trust Service Criteria | Overlap                                             |
| ------------------------- | ---------------------------- | --------------------------------------------------- |
| Req 1-2 (Network/Config)  | CC6.1, CC6.6, CC6.7          | 80%+ overlap on logical access and network controls |
| Req 3-4 (Data Protection) | CC6.1, C1 (Confidentiality)  | SOC 2 confidentiality criterion aligns closely      |
| Req 5 (Malware)           | CC6.8                        | Direct overlap                                      |
| Req 7-8 (Access/Auth)     | CC6.1, CC6.2, CC6.3          | Near-identical; SOC 2 more principle-based          |
| Req 10 (Logging)          | CC7.2, CC7.3                 | SOC 2 logging for anomaly detection aligns          |
| Req 11 (Testing)          | CC7.1, CC4.1                 | SOC 2 monitoring aligns; ASV not required by SOC 2  |
| Req 12 (Governance)       | CC1, CC2                     | SOC 2 governance criteria broadly align             |

**Harmonization value**: SOC 2 Type II-certified organizations typically have 70–80% PCI
DSS control overlap. Primary gaps: PCI-specific requirements (ASV quarterly scans,
specific log retention, TPSP responsibility matrix, QSA validation requirements).

---

### Step 10: QSA/ROC Preparation

For organizations preparing for a QSA-conducted ROC, produce an evidence package organized
by requirement:

#### Evidence Package Structure

```
evidence/
├── req-01-network/
│   ├── firewall-config-export-[date].txt
│   ├── network-diagram-[version]-[date].pdf
│   ├── firewall-review-record-[date].xlsx
│   └── change-control-log-[period].csv
├── req-02-config/
│   ├── configuration-standards-[component-type].pdf
│   └── baseline-scan-results-[date].pdf
├── req-03-stored-data/
│   ├── data-flow-diagram-[date].pdf
│   ├── encryption-specification.pdf
│   ├── key-management-policy.pdf
│   └── key-inventory-[date].xlsx
├── req-04-transit/
│   ├── tls-scan-results-[date].pdf
│   └── certificate-inventory-[date].xlsx
├── req-05-malware/
│   ├── av-deployment-report-[date].pdf
│   └── av-configuration-screenshots-[date].pdf
├── req-06-secure-dev/
│   ├── secure-coding-policy.pdf
│   ├── developer-training-records.xlsx
│   ├── patch-management-policy.pdf
│   └── patch-records-[period].xlsx
├── req-07-access-control/
│   ├── access-matrix-[date].xlsx
│   └── access-review-records-[date].xlsx
├── req-08-authentication/
│   ├── mfa-configuration-screenshots.pdf
│   ├── password-policy-configuration.pdf
│   └── account-lockout-configuration.pdf
├── req-09-physical/
│   ├── physical-access-policy.pdf
│   ├── visitor-log-[period].xlsx
│   └── poi-inspection-log.xlsx
├── req-10-logging/
│   ├── siem-architecture-diagram.pdf
│   ├── log-retention-configuration.pdf
│   └── sample-log-review-records.xlsx
├── req-11-testing/
│   ├── asv-scan-q1.pdf / q2.pdf / q3.pdf / q4.pdf
│   ├── penetration-test-report-[date].pdf
│   ├── segmentation-test-results-[date].pdf
│   └── internal-scan-reports-[period].pdf
└── req-12-governance/
    ├── information-security-policy.pdf
    ├── risk-assessment-[date].pdf
    ├── tpsp-inventory-[date].xlsx
    ├── tpsp-aoc-copies/
    ├── incident-response-plan.pdf
    ├── tabletop-test-record-[date].pdf
    └── security-awareness-training-records.xlsx
```

---

## Citation Quality Gates

Run these five gates silently before delivering any compliance output. Revise before
delivering if any gate fails.

| Gate           | Rule                                                                                                         | Fail Action                                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **Source**     | Every PCI DSS requirement cited uses the correct v4.0.1 requirement number                                   | Verify against official PCI DSS v4.0.1 specification; mark `[VERIFY req number]` if uncertain                 |
| **Format**     | All requirement citations follow "Req [number].[sub]" format consistently                                    | Fix formatting                                                                                                |
| **Currency**   | All future-dated requirement status (April 1, 2025) correctly reflected as mandatory                         | Flag `[CHECK DATE]` if applicability date is uncertain                                                        |
| **Domain**     | Analysis stays within PCI DSS scope; no HIPAA, GDPR, or other regime requirements stated as PCI requirements | Remove or clearly label cross-regime items                                                                    |
| **Confidence** | Uncertainty explicitly stated, not hidden                                                                    | Add confidence qualifier; mark `[VERIFY]` for any requirement details not confirmed against the specification |

---

## Self-Interrogation for Critical Deficiency Items

For any item classified as CRITICAL DEFICIENCY, apply this 3-pass adversarial review
before including it in the assessment output:

**Pass 1 — Accuracy Check**: Does this item reflect an actual v4.0.1 requirement, or
a prior-version requirement that has changed? Verify the specific sub-requirement exists
in PCI DSS v4.0.1 and that the compliance gap is correctly identified.

**Pass 2 — Completeness**: Have all relevant requirements been applied to this gap?
A single control failure often implicates multiple requirements (e.g., no MFA affects
Req 8.4.1, 8.4.2, and 8.4.3). Are there compensating control options that have not
been considered? Is scope analysis complete (could the component be out-of-scope)?

**Pass 3 — Challenge**: What is the strongest argument that this item is NOT a Critical
Deficiency? Is there a reasonable configuration or architecture that the assessment has
not identified that would satisfy the requirement? Under what circumstances might a QSA
classify this as PARTIAL rather than CRITICAL DEFICIENCY?

---

## Confidence Scoring

| Level        | Range     | Meaning                                                                          | Action                                                               |
| ------------ | --------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Requirement clearly stated; gap is unambiguous; directly tested                  | State finding with confidence                                        |
| **High**     | 0.80–0.94 | Strong basis; minor interpretive questions                                       | State with brief caveat                                              |
| **Probable** | 0.60–0.79 | Good analysis; some ambiguity in requirement application or evidence             | State with reasoning; note contra-indicators                         |
| **Possible** | 0.40–0.59 | Genuinely uncertain; requirement interpretation contested or evidence incomplete | Flag for QSA/qualified assessor review; present both interpretations |
| **Unlikely** | 0.0–0.39  | Weak basis; limited evidence; speculative                                        | Do not assert; flag `[UNCERTAIN — VERIFY WITH QSA]`                  |

---

## Glass Box Audit Trail

Include the following YAML block at the end of every compliance assessment output:

```yaml
glass_box:
  skill_name: "legalcode-pci-dss-compliance"
  skill_version: "PCI DSS v4.0.1 (January 2024)"
  assessment_date: "[ISO 8601 date]"
  organization: "[Anonymous identifier or name if consented]"
  entity_type: "[Merchant Level X / Service Provider Level X]"
  processing_environment: "[Card-present / CNP / E-commerce / Mixed]"
  recommended_saq: "[SAQ type or ROC-required]"
  cde_scope_determined: "[Yes — documented / Pending / Partial]"
  future_dated_requirements_status:
    mfa_all_cde_access_req_8_4_2: "[COMPLIANT / NON-COMPLIANT / PARTIAL]"
    certificate_management_req_4_2_1_1: "[COMPLIANT / NON-COMPLIANT / PARTIAL]"
    automated_log_review_req_10_4_1_1: "[COMPLIANT / NON-COMPLIANT / PARTIAL]"
    payment_page_script_control_req_6_4_3: "[COMPLIANT / NON-COMPLIANT / PARTIAL]"
    payment_page_tamper_detection_req_11_5_2: "[COMPLIANT / NON-COMPLIANT / PARTIAL]"
  findings_summary:
    critical_deficiency: "[count]"
    non_compliant: "[count]"
    partial: "[count]"
    compliant: "[count]"
  compensating_controls_required: "[Yes — N controls / No]"
  customized_approach_tra_required: "[Yes — N requirements / No]"
  legalcode_mcp: "[Connected / Not connected]"
  citations_verified: "[N VERIFIED] / [N marked VERIFY]"
  confidence: "[HIGH / MEDIUM / LOW — rationale]"
  limitations:
    - "[Any scope limitations, assumptions, or caveats specific to this assessment]"
    - "Assessment does not substitute for QSA-conducted ROC or qualified penetration test"
    - "All PCI DSS requirement numbers and testing procedures should be verified against official PCI SSC documentation"
  reviewer: "AI-assisted — requires qualified QSA or ISA review before compliance attestation"
```

---

## Anti-Patterns

What NOT to do in PCI DSS compliance work:

1. **Treating compliance as an annual audit exercise**: PCI DSS requires continuous compliance.
   Controls must be operational 365 days/year. Organizations that tune firewalls, rotate
   credentials, and patch systems only before audits create exploitable windows and face
   liability for non-compliance at the time of a breach.

2. **Assuming VLAN segmentation equals network segmentation**: VLANs alone do not satisfy
   network segmentation for PCI DSS purposes. Segmentation must be intentionally configured,
   purpose-built, and validated by penetration testing confirming no path exists from
   untrusted networks to CDE components.

3. **Using the wrong SAQ type**: Selecting SAQ A when the merchant's website code directly
   handles or redirects to a payment form (SAQ A-EP territory) is a material misrepresentation.
   SAQ eligibility must be confirmed, not assumed, especially for e-commerce merchants.

4. **Storing Sensitive Authentication Data post-authorization**: Storing CVV/track
   data/PIN — even encrypted — after authorization is complete is a Critical Deficiency.
   No encryption level makes SAD storage compliant post-authorization (except issuers
   with documented business need). Encrypt-and-store is not a valid remediation.

5. **Incomplete MFA coverage**: Implementing MFA for VPN/remote access but not for
   internal CDE access creates a compliance gap under v4.0.1 Req 8.4.2. MFA must cover
   ALL non-console CDE access — internal administrative access included — since April 1, 2025.

6. **Relying on third-party PCI compliance without verification**: Assuming a cloud provider
   or payment processor is PCI compliant without reviewing their current AOC, understanding
   what services their certification covers, and documenting the shared responsibility matrix
   is a Req 12.8 violation. A provider's general "PCI compliant" marketing claim does not
   satisfy the requirement.

7. **Treating compensating controls as permanent solutions**: Compensating controls are
   intended as temporary workarounds with a path to full remediation. Using them year-over-year
   without a remediation timeline signals systemic non-compliance to QSAs and may be rejected.

8. **Mixing truncated PAN with hashed PAN in the same environment**: Storing both the truncated
   PAN (first 6 + last 4 digits) and a hash of the full PAN in the same system allows
   correlation attacks. PCI DSS Req 3.4.1 explicitly prohibits this combination.

9. **Neglecting POI device tamper inspection**: Point-of-interaction device skimming attacks
   (Req 9.5.1) are a leading cause of card-present data breaches. Organizations that do not
   train staff to inspect devices and do not maintain inspection logs create both compliance
   gaps and material breach risk.

10. **Ignoring scope creep from cloud migrations**: Moving systems to cloud environments
    without re-evaluating CDE scope often inadvertently brings cloud management planes,
    shared tenancy interfaces, and DevOps toolchains into scope. Cloud migrations require
    re-scoping analysis, updated network diagrams, and review of cloud provider AOC coverage.

11. **Certificate inventory neglect**: Req 4.2.1.1 (mandatory April 1, 2025) requires a
    certificate inventory for all keys/certificates protecting PAN in transit. Organizations
    with dozens or hundreds of certificates across microservices, load balancers, and APIs
    that do not have automated certificate lifecycle management are systematically
    non-compliant and vulnerable to expired-certificate outages.

12. **Hardcoded credentials in application code or scripts**: Req 8.6.2 (mandatory April 1, 2025) prohibits hardcoded passwords/passphrases in scripts and applications. CICD
    pipelines and automation scripts with embedded credentials are both a compliance failure
    and an acute security risk (particularly if code repositories are shared or public).

13. **No e-commerce payment page integrity monitoring**: Magecart and web skimmer attacks
    inject malicious JavaScript into payment pages to exfiltrate card data. Reqs 6.4.3 and
    11.5.2/11.6.1 require script authorization, integrity verification, and real-time
    change detection. Organizations without these controls are high-value targets and
    systematically non-compliant.

14. **Inadequate log retention**: 12-month log retention with last 3 months immediately
    available (Req 10.5.1) is non-negotiable. Archiving logs to offline storage that
    requires days to retrieve violates the "readily available" requirement. Forensic
    investigations cannot be conducted effectively without accessible logs.

15. **Treating PCI DSS compliance as solely an IT function**: PCI DSS Req 12 imposes
    governance, policy, training, and third-party management obligations that require
    legal, finance, HR, and executive involvement. Organizations that silo compliance
    within IT teams fail at risk assessments, incident response, and TPSP management.

16. **Applying v3.2.1 controls to a v4.0.1 assessment**: v3.2.1 was retired March 31, 2024.
    Controls validated under v3.2.1 may not map directly to v4.0.1 requirements —
    particularly the future-dated requirements (MFA scope, script control, certificate
    inventory, automated log review). Annual assessments must be conducted against v4.0.1.

17. **Missing segmentation penetration test after significant changes**: Network changes —
    firewall replacements, cloud migrations, new network segments, VLAN reconfiguration —
    trigger the requirement to re-validate segmentation (Req 11.3.2.1). Organizations that
    test segmentation only on annual schedule and make network changes in between create
    unvalidated segmentation windows.

---

## Writing Standards

Apply these standards before delivering any assessment output:

- **Active, imperative instructions**: Write "remediate the gap by [action]" not "the gap
  should be considered for remediation"
- **Specific citations**: Reference the exact sub-requirement number (e.g., "Req 8.4.2")
  not just the parent requirement ("Req 8")
- **Classify every finding**: Every identified gap must receive a severity classification
  (CRITICAL DEFICIENCY / NON-COMPLIANT / PARTIAL / COMPLIANT) before delivery
- **Remediation action per finding**: Every non-COMPLIANT finding must include a specific
  remediation action, not just a description of the gap
- **No hidden uncertainty**: If a finding is uncertain, say so explicitly using confidence
  scoring; do not present uncertain analysis as definitive
- **Tiered output**: Lead with CRITICAL DEFICIENCY findings, then NON-COMPLIANT, then
  PARTIAL, then COMPLIANT; executives and QSAs read in this order
- **Avoid PCI DSS jargon without explanation**: When using terms like "ASV," "QSA," "POI
  device," "CDE," or "SAD," define them on first use in client-facing documents
- **[VERIFY] discipline**: Any requirement number, testing procedure, or legal reference
  that has not been confirmed against the official PCI SSC documentation must be marked
  `[VERIFY]`

---

## External Tool Integration

**With legalcode-mcp connected** (preferred for enhanced accuracy):

- Search for current PCI SSC guidance documents, information supplements, and FAQ updates
- Verify card-brand operating rule references (Visa, Mastercard, Amex, Discover, JCB)
- Search for recent PCI SSC blog posts clarifying requirement interpretation
- Look up current ASV and QSA listings from pcisecuritystandards.org
- Search for jurisdiction-specific legal references to PCI DSS (state breach notification
  statutes, DORA implementing measures for payment processors)
- Save research to `/tmp/legalcode-pci-dss-research-[date].md`

**Without legalcode-mcp** (fallback mode):

- Proceed with built-in framework knowledge and repository analysis
- Mark all requirement numbers and testing procedure details `[VERIFY against PCI DSS v4.0.1]`
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Recommend QSA review for all compliance determinations before attestation

---

## Localization Notes

PCI DSS itself is a contractual standard, not a statute, making it jurisdiction-agnostic
as a framework. However, contextual legal obligations vary by jurisdiction:

**[JURISDICTION-SPECIFIC: United States]**

- Minnesota Plastic Card Security Act (Minn. Stat. §§ 325E.64-65): Merchants compliant
  with PCI DSS at time of breach have limited liability to financial institutions [VERIFY
  current statute — some provisions have been amended]
- Nevada Rev. Stat. § 603A.215: Data security obligation references PCI DSS compliance
- 50-state breach notification laws apply independently of PCI DSS compliance status
- FTC Act § 5 "unfair or deceptive acts" enforcement: FTC has pursued companies with weak
  payment security under Section 5 [VERIFY recent enforcement actions]

**[JURISDICTION-SPECIFIC: European Union]**

- GDPR (Reg. 2016/679): Cardholder name, email, and other personal data elements in
  payment records are personal data; PCI DSS technical controls may satisfy some GDPR
  Art. 32 security obligations but are not coextensive
- DORA (Reg. 2022/2554, effective January 17, 2025): ICT operational resilience requirements
  for EU financial entities including payment processors; PCI DSS and DORA overlap
  significantly in ICT risk management, testing, and incident reporting but are not
  equivalent — both must be addressed for EU-regulated payment processors
- PSD2 (Dir. 2015/2366) / PSD3 (forthcoming): Strong Customer Authentication (SCA)
  requirements for payment service providers; SCA and PCI DSS MFA requirements overlap
  but are governed by separate regulatory regimes

**[JURISDICTION-SPECIFIC: United Kingdom]**

- UK GDPR (Data Protection Act 2018): Post-Brexit equivalent of EU GDPR for UK data
- Payment Services Regulations 2017 (SI 2017/752): UK FCA oversight of payment service
  providers; operational resilience requirements complement PCI DSS
- FCA PS20/15 operational resilience rules: Impact tolerance requirements for important
  business services including payment processing

**[JURISDICTION-SPECIFIC: Australia]**

- Privacy Act 1988 (Cth) / Australian Privacy Principles: Cardholder personal data covered;
  Notifiable Data Breaches scheme triggers may overlap with card-brand breach notification
- APRA CPS 234 (Information Security): Prudential standard for APRA-regulated entities
  (banks, insurers, super funds); APRA-regulated payment processors must comply with both

---

## Output Format Template

Structure every PCI DSS compliance assessment output as follows:

```markdown
# PCI DSS v4.0.1 Compliance Assessment

**Organization**: [Name/identifier] | **Assessment Date**: [Date] | **Assessor**: AI-assisted (legalcode-pci-dss-compliance)

---

## Executive Summary

**Recommended Validation Method**: [SAQ type / ROC required]
**Overall Compliance Status**: [CRITICAL GAPS / GAPS IDENTIFIED / SUBSTANTIALLY COMPLIANT / COMPLIANT]
**Critical Deficiencies**: [count] findings requiring immediate remediation
**Non-Compliant**: [count] findings requiring remediation before attestation
**Partial**: [count] findings requiring improvement
**Compliant**: [count] requirements fully met

[2-4 sentence executive narrative]

---

## CDE Scope Summary

- **CDE System Components**: [count and brief description]
- **Network Segmentation**: [Validated / Unvalidated / None — with implications]
- **Scope Reduction Controls in Place**: [Tokenization: Y/N | P2PE: Y/N | Outsourcing: Y/N]
- **Data Discovery Status**: [SAD found post-authorization: Y/N | PAN storage: Y/N/Tokenized]

---

## SAQ / Validation Recommendation

**Recommended SAQ Type**: [Type and rationale]
**Eligibility Basis**: [Key facts supporting eligibility]
**Eligibility Conditions**: [Any confirmations needed before finalizing SAQ selection]

---

## Critical Deficiency Findings

[For each: Requirement | Finding | Severity | Evidence Gap | Remediation Action | Timeline]

### [CD-01] [Finding Title]

- **Requirement**: Req [X.X]
- **Finding**: [Description of the gap]
- **Evidence Gap**: [What is missing]
- **Remediation Action**: [Specific steps to remediate]
- **Timeline**: IMMEDIATE (Tier 1 — within 30 days)
- **Confidence**: [Level and rationale]

---

## Non-Compliant Findings

[Same structure as Critical Deficiency, with NON-COMPLIANT classification]

---

## Partial Findings

[Same structure, with PARTIAL classification and improvement actions]

---

## Compliant Controls

[Tabular summary: Requirement | Control Description | Evidence Basis | Status]

---

## Prioritized Remediation Roadmap

| Priority           | Requirement | Finding | Action | Owner | Target Date |
| ------------------ | ----------- | ------- | ------ | ----- | ----------- |
| Tier 1 (Immediate) |             |         |        |       |             |
| Tier 2 (90 days)   |             |         |        |       |             |
| Tier 3 (6 months)  |             |         |        |       |             |
| Tier 4 (12 months) |             |         |        |       |             |

---

## TPSP Inventory Summary

[Table of TPSPs with AOC status]

---

## Compensating Controls Documentation

[CCW for each applicable control, if any]

---

## Customized Approach TRA

[TRA YAML for each customized approach requirement, if any]

---

## Cross-Framework Notes

[PCI DSS ↔ NIST CSF / SOC 2 / ISO 27001 alignment observations, if relevant]

---

## Next Steps for QSA Readiness

1. [Most critical action]
2. [Second priority]
   ...

---

[Glass Box Audit Trail YAML]
```

---

## Provenance

Created by Legalcode (2026-03-20). Original Legalcode synthesis using 2-agent research
pipeline (structural analysis + prompt engineering analysis), deep web-backed legal research
on PCI DSS v4.0.1 (January 2024 update), PCI SSC guidance documents, card-brand validation
programs, April 2025 future-dated requirements, and quality bar calibration against the
`legalcode-hipaa-compliance-assessment` and `legalcode-nist-csf-mapping` reference skills.
Research sources include PCI SSC official blog, Secureframe, StrikeGraph, Thoropass,
BasisTheory, ISMS.online, and practitioner guidance across all 12 requirement areas and
the SAQ determination methodology. No external SKILL.md was imported; this is an original
Legalcode synthesis.
