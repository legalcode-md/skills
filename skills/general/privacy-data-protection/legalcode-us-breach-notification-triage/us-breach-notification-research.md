# US Breach Notification Law — Comprehensive Research Reference

**Purpose**: Production research document for building the `legalcode-us-breach-notification-triage` skill covering all 50 US states, DC, Puerto Rico, US Virgin Islands, Guam, and American Samoa.

**Research date**: 2026-03-01
**Scope**: Current law as of early 2026, reflecting 2024–2025 legislative updates.

**Verification note**: Citations marked [VERIFY] should be independently confirmed against primary sources before inclusion in final skill output. All other citations are sourced from official statutory texts, government websites, or established legal publishers and are treated as high-confidence.

---

## Table of Contents

1. [Federal Overlay Requirements](#1-federal-overlay-requirements)
2. [State-by-State Summary Table](#2-state-by-state-summary-table)
3. [Deep-Dives: Six Most Complex States](#3-deep-dives-six-most-complex-states)
4. [Cross-Cutting Issues Analysis](#4-cross-cutting-issues-analysis)
5. [Safe Harbor Analysis](#5-safe-harbor-analysis)
6. [Territories](#6-territories)
7. [Source URLs](#7-source-urls)

---

## 1. Federal Overlay Requirements

### 1.1 HIPAA Breach Notification Rule

**Cite**: 45 CFR §§ 164.400–164.414
**Regulator**: HHS Office for Civil Rights (OCR)
**Covered entities**: HIPAA-covered entities (healthcare providers, health plans, healthcare clearinghouses) and their business associates.

#### Triggering Threshold

A "breach" is the acquisition, access, use, or disclosure of **unsecured** Protected Health Information (PHI) not permitted by the HIPAA Privacy Rule. Unsecured = not rendered unusable, unreadable, or indecipherable through valid encryption or proper destruction. Note: There is a **presumption of breach** unless the covered entity demonstrates, via a documented risk assessment, a **low probability** that the PHI has been compromised.

#### The Four-Factor Risk Assessment (45 CFR § 164.402)

Before concluding a breach does NOT require notification, the entity must assess:

1. **Nature and extent of PHI** — identifiers involved, sensitivity of content (e.g., HIV status, SSN), likelihood of re-identification.
2. **Identity of the unauthorized person** — was the recipient another covered entity with legal obligations, or a truly unauthorized third party?
3. **Whether PHI was actually acquired or viewed** — e.g., a misdirected fax retrieved immediately without viewing.
4. **Extent to which risk has been mitigated** — e.g., satisfactory assurances obtained from recipient.

If the entity cannot demonstrate low probability across all four factors, breach notification is **required**.

#### Notification Timelines

- **Individual notification**: Without unreasonable delay, **no later than 60 calendar days** after discovery of the breach. (§ 164.404)
- **HHS notification**:
  - Breaches affecting **500+ individuals in a state or jurisdiction**: Notify HHS **simultaneously** with individual notification (within 60 days). (§ 164.408)
  - Breaches affecting **fewer than 500 individuals**: Log the breach and submit an annual report to HHS no later than **60 days after the end of the calendar year** in which the breach occurred. (§ 164.408)
- **Media notification**: For breaches affecting **500+ individuals in a state or jurisdiction**, notify prominent media outlets in that state/jurisdiction, also within 60 days. (§ 164.406)

#### Content Requirements (§ 164.404(c))

- Brief description of what happened, including date of breach and date of discovery.
- Description of types of unsecured PHI involved.
- Steps individuals should take to protect themselves.
- Description of entity's investigation, mitigation steps, and protections offered.
- Contact procedures for questions (toll-free phone, email, website, or postal address).

#### Safe Harbor — Encryption and Destruction

PHI that is encrypted per NIST SP 800-111 (for data at rest) or NIST SP 800-52 / FIPS 140-2 (for data in transit), where the encryption key was not also compromised, is considered "secured" and does not trigger notification. PHI that is properly destroyed (paper shredded/burned/pulverized; electronic media cleared/purged/destroyed per NIST 800-88) is also exempt. [Source: HHS Breach Safe Harbor Guidance]

#### Business Associate Obligations (§ 164.410)

A business associate that discovers a breach must notify the covered entity **without unreasonable delay and within 60 calendar days** of discovery.

---

### 1.2 GLBA Safeguards Rule — FTC Breach Notification Amendment

**Cite**: 16 CFR Part 314 (as amended, effective May 13, 2024)
**Regulator**: Federal Trade Commission
**Covered entities**: Non-banking financial institutions subject to FTC jurisdiction (e.g., mortgage lenders, payday lenders, auto dealers, tax preparers, fintechs, investment advisers not registered with SEC).

#### Triggering Threshold

"Notification event" = unauthorized **acquisition** of unencrypted customer information (nonpublic personal information that is personally identifiable) of **500 or more customers**.

#### Notification Requirements

- **Notify FTC**: As soon as possible, **no later than 30 days** after discovery of the notification event.
- **No direct consumer notification requirement** under the FTC GLBA rule itself (though state laws still apply).
- The FTC intends to publish notification event reports in a **publicly available database**.

#### GLBA Notification Content

- Name and contact information of the reporting financial institution.
- Description of the types of information involved.
- Date and estimated date range of the notification event.
- Number of customers affected (or estimated number).
- General description of the notification event.
- Whether law enforcement has advised delay.

[Sources: FTC Press Release Oct 27, 2023; Federal Register Nov 13, 2023 (88 FR 79826); FTC Blog May 2024]

---

### 1.3 FTC Section 5 — General Data Security Duty

**Cite**: 15 U.S.C. § 45 (FTC Act Section 5)
FTC treats **unreasonable data security practices** as unfair or deceptive acts or practices. There is no explicit statutory breach notification obligation under Section 5 itself, but the FTC has brought enforcement actions against companies for failing to implement reasonable security measures that led to breaches. The FTC Health Breach Notification Rule (16 CFR Part 318) separately applies to vendors of personal health records not covered by HIPAA, requiring notification within 60 days of discovery.

---

### 1.4 SEC Cybersecurity Rules

**Cite**: Securities Exchange Act Rules 13a-11 / 15d-11; Item 1.05 of Form 8-K; Form 20-F (foreign private issuers); Regulation S-P (amended 2024)
**Adopted**: July 26, 2023; **Effective for large accelerated filers**: December 18, 2023; **Smaller reporting companies**: June 15, 2024.
**Regulator**: Securities and Exchange Commission

#### Material Incident Disclosure (Item 1.05 Form 8-K)

- Public companies must disclose **material cybersecurity incidents** on Form 8-K, Item 1.05, within **four business days** of determining that the incident is **material**.
- Materiality determination must be made **without unreasonable delay** but there is no fixed timeframe for making the determination itself.
- Required disclosures: nature, scope, and timing of the incident; its material impact or reasonably likely material impact.
- **Important**: Item 1.05 is ONLY for incidents determined to be material. Immaterial incidents should NOT be disclosed under Item 1.05 (may be voluntarily disclosed under Item 8.01).
- National security/law enforcement delay: The SEC may grant confidential treatment upon DOJ request.

#### Annual Governance Disclosure (Form 10-K / 20-F)

Companies must disclose material information about their cybersecurity risk management program, strategy, and governance annually.

#### Regulation S-P Amendment (2024)

- Broker-dealers, investment companies, investment advisers: Must notify affected individuals of a breach of "sensitive customer information" **as soon as practicable but not later than 30 days** after becoming aware [VERIFY — rule finalized May 2024, effective dates phased].

---

### 1.5 FCC Breach Notification Rules (Telecom Carriers)

**Cite**: 47 CFR Part 64, Subpart U (as amended by FCC Report and Order, effective March 13, 2024)
**Regulator**: Federal Communications Commission
**Covered entities**: Telecommunications carriers (including VoIP providers)

#### 2024 Update — Expanded Scope

- Prior rules covered only Customer Proprietary Network Information (CPNI).
- 2024 rules expanded to cover **any customer personally identifiable information (PII)**, including both intentional and **inadvertent** breaches.

#### Notification Timelines

- **Federal agency notification** (FBI + Secret Service + FCC): Within **seven business days** after reasonable determination of a breach affecting **500 or more customers**. (Individual per-breach reports required; annual report for all breaches regardless of size.)
- **Customer notification**: Without unreasonable delay, **no later than 30 days** after reasonable determination of a breach (eliminating prior 7-day waiting period before customer notification).

#### Harm-Based Exception

No customer notification required where:

- Carrier can reasonably determine that **no harm to customers is reasonably likely**; OR
- Breach involves only **encrypted data** and encryption key was not compromised.

[Source: FCC Federal Register Feb 12, 2024 (89 FR 9974); Sixth Circuit upheld rules Aug 13, 2025]

---

### 1.6 CIRCIA — Cyber Incident Reporting for Critical Infrastructure Act (2022)

**Cite**: 6 U.S.C. §§ 681 et seq. (as amended)
**Regulator**: CISA (Cybersecurity and Infrastructure Security Agency)
**Status as of March 2026**: NPRM published April 4, 2024 (89 FR 23644). Final Rule expected May 2026 per Spring 2025 Unified Regulatory Agenda. **Not yet in effect.**

#### Proposed Timelines (NPRM — subject to change in Final Rule)

- **Covered cyber incidents**: Report within **72 hours** of discovery.
- **Ransom payments**: Report within **24 hours** of payment.

#### Covered Entities

Critical infrastructure sectors as defined in Presidential Policy Directive 21. CISA is holding sector-specific town halls in early 2026 to refine scope.

**Practitioner note**: Organizations in critical infrastructure sectors should monitor CISA rulemaking. CIRCIA will impose obligations in addition to existing state and sector-specific laws once finalized.

---

## 2. State-by-State Summary Table

**Legend for columns**:

- **Timeline (Individual)**: Deadline to notify affected residents
- **AG/Regulator Notification**: Required government notification and threshold
- **PI Definition**: Key categories beyond name + SSN/DL/financial (abbreviated)
- **Risk of Harm Threshold**: Y = notification only required if risk of harm; N = notification automatic on breach of qualifying data
- **Encryption Safe Harbor**: Y = explicit; N = not explicit / implied by "unsecured" definition
- **Credit Monitoring**: Y = mandatory (with duration if known); N = not required

> All citations should be [VERIFY]'d against current primary sources before use in production. State laws change frequently. This table reflects research as of early 2026.

| State                    | Statute                                                              | Timeline (Individual)                                                                    | AG/Regulator Notification                                                                                | Risk of Harm                                                          | Encryption Safe Harbor | Credit Monitoring                                      |
| ------------------------ | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------ |
| **Alabama**              | Ala. Code § 8-38-1 et seq.                                           | 45 days                                                                                  | AG (no threshold stated)                                                                                 | Y                                                                     | Y                      | N                                                      |
| **Alaska**               | AS § 45.48.010 et seq.                                               | Expedient/without unreasonable delay                                                     | AG if >500 residents [VERIFY]                                                                            | Y                                                                     | Y                      | N                                                      |
| **Arizona**              | Ariz. Rev. Stat. § 18-552                                            | Expedient/without unreasonable delay                                                     | AG (civil enforcement only; no pre-notification requirement)                                             | Y                                                                     | Y                      | N                                                      |
| **Arkansas**             | Ark. Code Ann. § 4-110-105                                           | Expedient/without unreasonable delay; to those likely to be harmed                       | N/A                                                                                                      | Y                                                                     | Y                      | N                                                      |
| **California**           | Cal. Civ. Code §§ 1798.29, 1798.82                                   | **30 days** (eff. Jan 1, 2026)                                                           | AG within 15 days of consumer notification, if >500 CA residents                                         | Y (no explicit risk of harm clause — notification generally required) | Y                      | N (statute does not mandate)                           |
| **Colorado**             | C.R.S. § 6-1-716                                                     | **30 days** from determination breach occurred                                           | AG within 30 days if >500 CO residents                                                                   | N (notification required upon breach determination)                   | Y                      | Y — 12 months if SSN compromised                       |
| **Connecticut**          | Conn. Gen. Stat. § 36a-701b                                          | **60 days**                                                                              | AG no later than when residents notified                                                                 | N                                                                     | Y                      | Y — 24 months if SSN compromised                       |
| **Delaware**             | Del. Code tit. 6, § 12B-102                                          | **60 days**                                                                              | AG if not reasonably likely to harm                                                                      | Y                                                                     | Y                      | Y — 1 year if SSN compromised                          |
| **District of Columbia** | D.C. Code §§ 28-3851 to 28-3853                                      | Expedient/without unreasonable delay                                                     | AG if >50 DC residents                                                                                   | N                                                                     | Y                      | Y — 18 months (identity theft protection)              |
| **Florida**              | Fla. Stat. § 501.171                                                 | **30 days** (extendable 15 days for good cause shown in writing)                         | AG (Dept. of Legal Affairs) within 30 days if >500 FL residents                                          | Y                                                                     | Y                      | N (but notice must describe services offered)          |
| **Georgia**              | Ga. Code Ann. § 10-1-912                                             | Expedient/without unreasonable delay                                                     | Notify CRAs if >10,000 residents [VERIFY]; no AG notification required                                   | Y                                                                     | Y                      | N                                                      |
| **Hawaii**               | Haw. Rev. Stat. § 487N-2                                             | Expedient/without unreasonable delay                                                     | N/A                                                                                                      | Y                                                                     | Y                      | N                                                      |
| **Idaho**                | Idaho Code § 28-51-105                                               | Expedient/without unreasonable delay                                                     | AG within 24 hours (for public agencies); private entities: expedient [VERIFY]                           | Y                                                                     | Y                      | N                                                      |
| **Illinois**             | 815 ILCS 530/1 et seq.                                               | Expedient/without unreasonable delay                                                     | AG, no later than when consumers notified                                                                | N                                                                     | Y                      | N                                                      |
| **Indiana**              | Ind. Code § 24-4.9-3-1 et seq.                                       | Without unreasonable delay                                                               | N/A if risk of harm                                                                                      | Y                                                                     | Y                      | N                                                      |
| **Iowa**                 | Iowa Code § 715C.1 et seq.                                           | Expedient/without unreasonable delay                                                     | N/A                                                                                                      | Y                                                                     | Y                      | N                                                      |
| **Kansas**               | Kan. Stat. Ann. § 50-7a01 et seq.                                    | Expedient/without unreasonable delay                                                     | N/A                                                                                                      | Y                                                                     | Y                      | N                                                      |
| **Kentucky**             | Ky. Rev. Stat. § 365.732                                             | Without unreasonable delay; immediately if harm likely                                   | N/A                                                                                                      | Y                                                                     | Y                      | N                                                      |
| **Louisiana**            | La. Rev. Stat. § 51:3071 et seq.                                     | **60 days**                                                                              | AG if >500 LA residents [VERIFY]                                                                         | Y                                                                     | Y                      | N                                                      |
| **Maine**                | Me. Rev. Stat. tit. 10, § 1347 et seq.                               | **30 days**                                                                              | AG (no threshold — all breaches)                                                                         | Y                                                                     | Y                      | N                                                      |
| **Maryland**             | Md. Code Ann., Com. Law § 14-3501 et seq.                            | **45 days**                                                                              | AG before or simultaneously with consumer notification                                                   | N                                                                     | Y                      | N                                                      |
| **Massachusetts**        | Mass. Gen. Laws ch. 93H                                              | Expedient/without unreasonable delay                                                     | AG + OCABR (no threshold)                                                                                | N                                                                     | Y                      | Y — 18 months if SSN; CRAs must provide 42 months      |
| **Michigan**             | Mich. Comp. Laws § 445.63 et seq.                                    | Without unreasonable delay                                                               | N/A                                                                                                      | Y (substantial loss or injury threshold)                              | Y                      | N                                                      |
| **Minnesota**            | Minn. Stat. § 325E.61                                                | Without unreasonable delay                                                               | Notify CRAs within 48 hours if >500 residents; no AG notification                                        | N                                                                     | Y                      | N                                                      |
| **Mississippi**          | Miss. Code Ann. § 75-24-29                                           | Without unreasonable delay                                                               | AG if ≥100 individuals                                                                                   | Y                                                                     | Y                      | N                                                      |
| **Missouri**             | Mo. Rev. Stat. § 407.1500                                            | Expedient/without unreasonable delay                                                     | AG if >500 MO residents                                                                                  | Y                                                                     | Y                      | N                                                      |
| **Montana**              | Mont. Code Ann. § 30-14-1704                                         | Without unreasonable delay                                                               | AG (all breaches, no threshold)                                                                          | Y                                                                     | Y                      | N                                                      |
| **Nebraska**             | Neb. Rev. Stat. § 87-803                                             | Without unreasonable delay                                                               | AG simultaneously with consumer notification                                                             | N                                                                     | Y                      | N                                                      |
| **Nevada**               | Nev. Rev. Stat. § 603A.220                                           | Expedient/without unreasonable delay                                                     | N/A (no AG notification requirement in statute) [VERIFY]                                                 | Y                                                                     | Y                      | N (but notice must include CRA contact info)           |
| **New Hampshire**        | N.H. Rev. Stat. § 359-C:20                                           | Expedient/without unreasonable delay                                                     | AG + CRAs if >1,000 NH residents                                                                         | Y                                                                     | Y                      | N                                                      |
| **New Jersey**           | N.J. Stat. Ann. § 56:8-163 et seq.                                   | Expedient/without unreasonable delay                                                     | Division of State Police before individual notification; CRAs if >1,000 residents                        | N                                                                     | Y                      | N                                                      |
| **New Mexico**           | N.M. Stat. Ann. § 57-12C-6                                           | **45 days**                                                                              | AG if >1,000 NM residents, within 45 days                                                                | Y                                                                     | Y                      | N                                                      |
| **New York**             | N.Y. Gen. Bus. Law § 899-aa; N.Y. State Tech. Law § 208 (SHIELD Act) | **30 days** (eff. Dec 21, 2024)                                                          | AG, Dept. of State, OCFS notification required; service providers must notify data owner within 30 days  | N                                                                     | Y                      | N                                                      |
| **North Carolina**       | N.C. Gen. Stat. § 75-65                                              | Without unreasonable delay                                                               | AG if >1,000 NC residents                                                                                | Y                                                                     | Y                      | N                                                      |
| **North Dakota**         | N.D. Cent. Code § 51-30                                              | Expedient/without unreasonable delay                                                     | AG if >250 ND individuals                                                                                | Y                                                                     | Y                      | N                                                      |
| **Ohio**                 | Ohio Rev. Code § 1347.12                                             | Expedient/without unreasonable delay                                                     | AG notification [VERIFY threshold]                                                                       | Y                                                                     | Y                      | N (but NIST safe harbor for litigation)                |
| **Oklahoma**             | Okla. Stat. tit. 24, § 163                                           | Without unreasonable delay                                                               | N/A (no AG notification)                                                                                 | Y                                                                     | Y                      | N                                                      |
| **Oregon**               | Or. Rev. Stat. § 646A.604                                            | **45 days**                                                                              | DOJ (AG) within 45 days if >250 OR residents; CRAs without unreasonable delay if >1,000                  | Y                                                                     | Y                      | N                                                      |
| **Pennsylvania**         | 73 Pa. Stat. § 2303 et seq. (eff. Sep 26, 2024)                      | Without unreasonable delay                                                               | AG if >500 PA residents                                                                                  | N                                                                     | Y                      | Y — 12 months (SSN, DL, or financial account breaches) |
| **Rhode Island**         | R.I. Gen. Laws § 11-49.3-4                                           | **45 days**                                                                              | AG within 30 days of consumer notification                                                               | Y                                                                     | Y                      | N                                                      |
| **South Carolina**       | S.C. Code Ann. § 39-1-90                                             | Expedient/without unreasonable delay                                                     | Dept. of Consumer Affairs + CRAs if >1,000 SC residents                                                  | Y                                                                     | Y                      | N                                                      |
| **South Dakota**         | S.D. Codified Laws § 22-40-20                                        | **60 days**                                                                              | AG if >250 SD residents                                                                                  | Y                                                                     | Y                      | N                                                      |
| **Tennessee**            | Tenn. Code Ann. § 47-18-2107                                         | **45 days**                                                                              | N/A (no AG notification) [VERIFY]                                                                        | Y                                                                     | Y                      | N                                                      |
| **Texas**                | Tex. Bus. & Com. Code § 521.053                                      | **60 days** (individuals); AG within **30 days** if ≥250 TX residents (eff. Sep 1, 2023) | AG within 30 days if ≥250 TX residents                                                                   | N                                                                     | Y                      | N                                                      |
| **Utah**                 | Utah Code Ann. § 13-44-202 (amended May 1, 2024)                     | Within 30 days if >500 UT residents [VERIFY exact threshold vs. deadline]                | AG + Utah Cyber Center                                                                                   | Y                                                                     | Y                      | N                                                      |
| **Vermont**              | 9 V.S.A. § 2435                                                      | **45 days**                                                                              | AG (DFR for regulated entities: 14 business days); all breaches require AG notice before consumer notice | Y                                                                     | Y                      | N                                                      |
| **Virginia**             | Va. Code Ann. § 18.2-186.6                                           | Without unreasonable delay                                                               | AG (all breaches); notify CRAs if >1,000 VA residents simultaneously                                     | Y                                                                     | Y                      | N                                                      |
| **Washington**           | RCW 19.255.010                                                       | **30 days**                                                                              | AG within 30 days if >500 WA residents                                                                   | Y                                                                     | Y                      | N                                                      |
| **West Virginia**        | W. Va. Code § 46A-2A-101 et seq.                                     | Expedient/without unreasonable delay                                                     | AG + CRAs if >1,000 WV residents [VERIFY]                                                                | Y                                                                     | Y                      | N                                                      |
| **Wisconsin**            | Wis. Stat. § 134.98                                                  | Without unreasonable delay                                                               | N/A (no AG notification)                                                                                 | Y                                                                     | Y                      | N                                                      |
| **Wyoming**              | Wyo. Stat. Ann. § 40-12-502                                          | Without unreasonable delay                                                               | N/A (no AG notification) [VERIFY]                                                                        | Y                                                                     | Y                      | N                                                      |

---

## 3. Deep-Dives: Six Most Complex States

### 3.1 California

**Primary statutes**: Cal. Civ. Code §§ 1798.29 (public agencies), 1798.82 (businesses); CCPA/CPRA (Cal. Civ. Code §§ 1798.100 et seq.) adds a private right of action for certain breaches.

#### Timeline (as amended, effective January 1, 2026)

- Businesses must notify affected California residents within **30 calendar days** of discovering the breach.
- Two exceptions allow delay: (1) to accommodate legitimate needs of law enforcement; (2) as necessary to determine the scope of the breach and restore the reasonable integrity of the data system.

#### AG Notification

- Disclosure to the California AG required **within 15 days of notifying affected consumers** when **more than 500 California residents** are notified.
- AG notification must include a copy of the breach notice.
- Prior to the 2025 amendment, there was **no explicit timeline** in the original statute — only "most expedient time possible and without unreasonable delay."

#### Personal Information Definition

California has one of the broadest PI definitions. Triggers breach notification when name or ID + any of the following is compromised:

- SSN, driver's license/state ID, passport, military ID, tax ID number
- Account number or credit/debit card number + access credentials
- Medical information (broad — any information regarding an individual's medical history, condition, or treatment)
- Health insurance information
- **Unique biometric data** (fingerprints, retina/iris scans, facial geometry, voiceprints, etc.)
- **Username or email address + password** or security question/answer
- Information collected through an automated license plate recognition system
- **Genetic data** [VERIFY — added by later amendment]

Additionally, breach of a **username or email address and password** or security question/answer, without other PI, triggers notification under a streamlined notice provision (limited notice describing the breach, urging user to change credentials).

#### CCPA Private Right of Action

Cal. Civ. Code § 1798.150 creates a **private right of action** for consumers when a business fails to implement reasonable security procedures and a subsequent breach exposes:

- SSN, driver's license, account number + credentials, medical/health insurance info, biometric, username/password.
- Statutory damages: $100–$750 per consumer per incident OR actual damages, whichever is greater.
- Class actions permitted.

#### Content Requirements

Breach notices must include:

- Name and contact information of reporting business.
- List of categories of PI that were or are reasonably believed to have been subject to breach.
- If SSNs, DL numbers, or financial account numbers: include information on steps to place a fraud alert or security freeze.
- Toll-free numbers for major credit bureaus.
- AG contact information [VERIFY — added in 2024+ amendment].
- Written notices must follow a specific format (heading in 10-point font or larger; mandated sections).

#### Substitute Notice

Available when: (1) cost of notice exceeds $250,000; or (2) number of persons to be notified exceeds 500,000; or (3) insufficient contact information.

- Consists of: email notice + conspicuous website posting for at least 30 days + notification to major statewide media.

#### Safe Harbor

Encrypted or redacted data is explicitly excluded from notification requirements. No HIPAA or other federal-compliance safe harbor in the statute itself, but HIPAA-covered entities may satisfy California requirements through HIPAA-compliant notifications.

---

### 3.2 New York

**Primary statutes**: N.Y. Gen. Bus. Law § 899-aa (commercial entities); N.Y. State Tech. Law § 208 (state agencies); SHIELD Act (Stop Hacks and Improve Electronic Data Security Act, signed July 25, 2019); Amendment signed December 24, 2024.

#### Timeline

- **30 days** from discovery of the breach (eff. December 21, 2024 — amendment signed Dec 24, 2024).
- Prior standard: "most expedient time possible and without unreasonable delay."
- **Service providers** must notify the data owner within **30 days** of discovering a breach; service providers do not notify consumers directly.

#### Private Information Definition (expanded)

NY uses the term "private information" = personal information + one or more of:

- SSN
- Driver's license number or non-driver ID card number
- Account number, credit or debit card number + credentials
- Account password / security question & answer
- Biometric information
- **Medical information** (added effective March 21, 2025) — medical history, conditions, treatments, diagnoses
- **Health insurance information** (added eff. March 21, 2025) — policy numbers, subscriber IDs, claims history

Note: NY defines "breach" as unauthorized **access** (not merely acquisition) to private information — broader than many states.

#### AG Notification

- Notify AG, Dept. of State, and OCFS (Office of Children and Family Services, if applicable) **in the most expedient time possible and without unreasonable delay**.
- No explicit numerical resident threshold for AG notification (all material breaches should be reported).
- AG has active enforcement posture.

#### Content Requirements

Notices must include:

- Contact information for reporting party.
- Description of categories of private information involved.
- Telephone numbers and websites for relevant state and federal agencies.
- If breach involved username/password: advise user to change credentials; check other accounts using same credentials.

#### Safe Harbor

No separate HIPAA or PCI safe harbor in statute. Encrypted/redacted data excluded from definition of "private information."

---

### 3.3 Colorado

**Primary statute**: C.R.S. § 6-1-716 (amended by HB21-1119, effective September 1, 2021)

#### Timeline

- **30 days** from the date the entity determines that a security breach has occurred.
- "Determination that a security breach has occurred" = the point in time at which there is sufficient evidence to conclude that a security breach has taken place (not the initial discovery date).
- Third-party service providers must notify Colorado covered entities within **30 days** of discovery.

#### AG Notification

- If **500 or more Colorado residents** are affected: notify Colorado AG within the same 30-day window.

#### Personal Information Definition

- Name + SSN, DL/state ID, passport, military ID, military dependent ID card
- Account number / credit/debit card number + credentials
- Medical information + first name or initial + last name
- Health insurance information + first name or initial + last name
- **Biometric data** (fingerprint, voiceprint, retina/iris scan, or other unique biological characteristic)
- **Username or email address + password** or security question/answer
- Student ID + personal identification number, password, or passcode used to access education records

#### Credit Monitoring

- Free credit monitoring required for **12 months** if the breach included an SSN.

#### Risk of Harm Assessment

Colorado does **not** have a "risk of harm" exemption from notification. Notification is required upon determination that a breach has occurred (though the entity must reach that "determination" threshold).

#### Safe Harbor

Encrypted/secured data is excluded. Entities complying with their own notification procedures (which must be consistent with Colorado's 30-day deadline and otherwise comply with the statute) may satisfy Colorado requirements.

---

### 3.4 Florida

**Primary statute**: Fla. Stat. § 501.171 (Florida Information Protection Act — FIPA)

#### Timeline

- **30 days** from determination of a breach (or reason to believe a breach occurred).
- Extension: If good cause is presented **in writing to the AG within the 30-day window**, an additional **15 days** may be granted.
- Prior law required 45 days — the 30-day deadline was tightened.

#### AG Notification

- **500 or more Florida residents** affected: notify AG (Dept. of Legal Affairs) as expeditiously as practicable, **no later than 30 days**.

#### Personal Information Definition

- Name + SSN, DL number, passport number, military ID, or tax ID
- Account number / credit/debit card number + credentials
- Medical history, condition, treatment, or diagnosis
- Health insurance information
- Username/email + password or security question/answer [VERIFY — added in recent amendment]
- Biometric data [VERIFY — added in 2022 amendment]

#### Penalties

- $1,000 per day for each of the first 30 days following a violation.
- $50,000 per 30-day period (or portion thereof) for subsequent periods up to 180 days.
- Maximum civil penalty: $500,000 per breach.
- AG may investigate and sue; no private right of action.

#### Credit Monitoring

Florida's statute does not explicitly mandate free credit monitoring, but notices must describe services being offered to individuals. [VERIFY — some sources indicate credit monitoring was added for 500+ SSN breaches; confirm against current statute text.]

#### Risk of Harm

FIPA allows covered entities to forego notification if, after an investigation and consultation with relevant law enforcement, the entity **reasonably determines** that the breach has not and will not likely result in identity theft or financial harm. This determination must be **documented in writing and retained for at least 5 years**.

---

### 3.5 Texas

**Primary statute**: Tex. Bus. & Com. Code § 521.053 (amended by SB 768, effective September 1, 2023)

#### Timeline (Two-Track System)

- **Individual notification**: Without unreasonable delay, **no later than 60 days** after the entity determines the breach occurred.
- **AG notification**: As soon as practicable, **no later than 30 days** after determining the breach occurred, if **250 or more Texas residents** are affected.

#### Personal Information Definition

- Name + SSN, DL/state ID, government-issued ID
- Account number + credentials
- Financial account information
- Health information [VERIFY extent — Texas HB 300 (medical records) adds additional protections]

#### Safe Harbor

Texas does not have an explicit encryption safe harbor in § 521.053, but encrypted data is generally understood to not constitute "sensitive personal information" for notification purposes [VERIFY].

#### Penalties

AG may bring suit; civil penalties of up to $500 per individual per violation, not to exceed $50,000 per incident [VERIFY current cap — Texas penalties were tightened by 2023 amendment]. The AG may also seek up to $250 per day for continuing violations.

#### Third-Party Obligations

Third parties maintaining data on behalf of others must notify the data owner as soon as practicable. Data owner then has 60 days (individuals) / 30 days (AG if ≥250 residents) from its own determination.

---

### 3.6 Massachusetts

**Primary statutes**: Mass. Gen. Laws ch. 93H; 201 CMR 17.00 (Written Information Security Program requirements)

#### Timeline

- "As soon as reasonably possible and without unreasonable delay" — **no fixed deadline**.
- Massachusetts is unusual in that it has one of the most robust data security program requirements (201 CMR 17.00 mandates a formal written information security program — WISP) but does not have a hard numeric deadline for individual notification.

#### AG + OCABR Notification

- Notify **both** the AG and the Office of Consumer Affairs and Business Regulation (OCABR) — no numeric threshold; **all breaches** affecting MA residents must be reported.
- Notification to AG and OCABR must include:
  - Nature of the breach.
  - Number of MA residents affected at time of notification.
  - Name and address of entity.
  - Type of personal information compromised.
  - A sample copy of the consumer notice.

#### Personal Information Definition

- Name + SSN, DL/state ID, financial account number + credentials.
- Massachusetts has a broader "personal information" definition that can include other data — practitioners should review the full statute.

#### Credit Monitoring

Massachusetts amended ch. 93H to require **at least 18 months** of free credit monitoring services when SSNs are compromised. Consumer reporting agencies are required to provide **at least 42 months** of free credit reports to affected consumers. MA also prohibits requiring consumers to waive their private right of action as a condition of receiving credit monitoring.

#### Written Information Security Program (WISP)

201 CMR 17.00 requires all businesses that own, license, store, or maintain PI about MA residents to implement and maintain a comprehensive WISP containing:

- Designated employee responsible for security program.
- Identification and assessment of risks to PI.
- Employee security training.
- Selection of qualified third-party service providers.
- Discipline policies for security program violations.
- Computer system security requirements (access controls, encryption for transmitted/stored PI on laptops/portable devices, monitoring systems, etc.).

This is one of the most prescriptive data security frameworks in the US.

#### Private Right of Action

Massachusetts ch. 93A (Consumer Protection Act) provides for private rights of action and up to treble damages for willful violations [VERIFY applicability to ch. 93H breaches specifically].

---

## 4. Cross-Cutting Issues Analysis

### 4.1 Definition of "Personal Information" — Category Coverage by State

The following chart summarizes which categories of data trigger notification obligations across states. A "breach" of name + identifier is what typically triggers the law; the identifier categories are what vary.

| PI Category                            | Most States                      | Notable Inclusions                                  | Notable Exclusions                                          |
| -------------------------------------- | -------------------------------- | --------------------------------------------------- | ----------------------------------------------------------- |
| SSN                                    | All 50 states + DC + territories | Universal                                           | None                                                        |
| Driver's License / State ID            | All 50 states + DC + territories | Universal                                           | None                                                        |
| Financial Account Number + credentials | All 50 states + DC + territories | Universal                                           | Some states require credentials; others just account number |
| Credit/Debit Card + CVV/PIN            | All 50 states                    | Universal                                           |                                                             |
| Medical Information                    | Majority (~35+ states)           | CA, CO, CT, DC, FL, IL, NY, OR, TX, WA, many others | Some states still exclude                                   |
| Health Insurance Information           | Growing (~25+ states)            | CA, CO, CT, DC, FL, NY, WA                          | Many states lack                                            |
| **Biometric Data**                     | ~20+ states                      | CA, CO, IL, NY, OR, WA, TX (limited), VT            | Many states lack                                            |
| Username/Email + Password              | ~15+ states                      | AL, CA, CO, CT, FL, IL, NE, NV, NY, OR, RI, SD, WY  | Many states lack; rapidly expanding                         |
| **Precise Geolocation**                | ~3-5 states                      | CT (eff. Oct 1, 2023) [VERIFY others]               | Most states lack                                            |
| Genetic Information                    | ~5-8 states                      | CA, DC, NY, VT [VERIFY full list]                   | Most states lack                                            |
| Military ID / Passport                 | ~20+ states                      | CA, CO, CT, FL, NY, TX                              | Many states still limited to SSN/DL                         |
| Student ID + PIN                       | CO                               | CO specifically; [VERIFY other states]              | Most states lack                                            |
| Tax Identification Number (ITIN)       | VT, others [VERIFY]              | Growing                                             | Many states lack                                            |

**Important trend**: State PI definitions are rapidly expanding to include biometric, geolocation, credential, and genetic data. Any skill built on this research should note that definitions should be verified against current state law at time of use.

---

### 4.2 Breach Definition — Access vs. Acquisition

States differ on what triggers the definition of "breach":

| Standard                                                             | States                                          | Notes                                                           |
| -------------------------------------------------------------------- | ----------------------------------------------- | --------------------------------------------------------------- |
| **Unauthorized acquisition** (stricter — actual possession required) | Traditional standard; still used in many states | Requires proof that data was actually taken                     |
| **Unauthorized access** (broader — viewing is sufficient)            | NY (SHIELD Act), CO, CT, OR, WA, and others     | Mere exposure or access is sufficient even without exfiltration |
| **Acquisition or access**                                            | Most modern statutes                            | Combined approach                                               |

**Practitioner implication**: A misconfigured S3 bucket that was publicly accessible but may or may not have been accessed requires notification in states using the "access" standard (including NY, CO) but may not in states using only "acquisition."

---

### 4.3 Risk of Harm Threshold

Approximately half of states condition notification on a "risk of harm" or "likelihood of harm" assessment. The other half require notification whenever qualifying PI is involved in an unauthorized access/acquisition, regardless of harm likelihood.

**States WITH risk of harm threshold** (notification may not be required if no risk of harm, with documented determination):

- AK, AR, AZ, DE, FL, GA, HI, IN, IA, KS, KY, LA, ME, MI, MO, MT, NC, ND, NV, NH, OK, OR, RI, SC, SD, TN, UT, VA, WI, WY, and others.

**States WITHOUT risk of harm threshold** (automatic notification upon qualifying breach):

- CA, CO, CT, IL, MA, MN, NE, NJ, NY, TX, WA, and others.

**Documentation requirement**: Most states with a risk of harm exemption require the entity to **document the determination in writing** and retain for 3–5 years (varies by state). Failure to document properly can eliminate the exemption.

---

### 4.4 Attorney General Notification — Thresholds Reference Table

| AG Notification Threshold       | States                                                                                                                                          |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **All breaches (no threshold)** | MA (AG + OCABR), ME, MT, NE, NY, TX (actually: ≥250), VT                                                                                        |
| **≥50 residents**               | DC                                                                                                                                              |
| **≥100 residents**              | MS                                                                                                                                              |
| **≥250 residents**              | ND, SD, TX (AG), UT [VERIFY]                                                                                                                    |
| **≥500 residents**              | CA (within 15 days of consumer notice), CO, FL, MO, PA, WA                                                                                      |
| **≥1,000 residents**            | NM, NH (CRAs + AG), NJ (CRAs), VA (CRAs), WV [VERIFY]                                                                                           |
| **≥10,000 residents**           | GA (CRAs only)                                                                                                                                  |
| **No AG notification required** | AK (risk of harm notification to AG), AR, AZ, HI, ID (limited), IN, IA, KS, KY, MN (CRAs only), NV, NC (≥1,000 for AG) [VERIFY], OK, TN, WI, WY |

> Many states that don't require AG pre-notification still permit or encourage voluntary notification to AG. AG offices typically maintain breach notification portals.

---

### 4.5 Third-Party / Vendor Notification Requirements

When a breach occurs at a service provider/vendor holding a covered entity's data:

| Jurisdiction                            | Vendor Notification Deadline to Covered Entity                                                          |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **HIPAA (Business Associates)**         | 60 days of discovery (to covered entity)                                                                |
| **FTC Health Breach Notification Rule** | 60 days (to business contact if no designee in contract)                                                |
| **New York (SHIELD Act)**               | 30 days (service provider to data owner; data owner then has 30 days to notify consumers)               |
| **Oregon**                              | 10 days (vendor must notify covered entity within 10 days of discovering breach)                        |
| **Colorado**                            | 30 days (third-party service provider to covered business)                                              |
| **California**                          | Expedient/without unreasonable delay (no fixed deadline for vendor-to-owner notice in statute) [VERIFY] |
| **Vermont**                             | Without unreasonable delay (no fixed deadline)                                                          |
| **Most other states**                   | Without unreasonable delay / expedient time                                                             |

Key principle: The **covered entity** (data owner) owns the notification obligation to consumers; the vendor/service provider generally does not notify consumers directly.

---

### 4.6 Substitute Notice

Substitute notice is available when direct individual notice is cost-prohibitive or impracticable. The common triggers (with state-specific thresholds) are:

**Standard triggers** (apply in most states):

1. Cost of notification would exceed **$250,000** (some states use different thresholds).
2. Number of affected persons exceeds **500,000** (California); other states use different thresholds.
3. Sufficient contact information is not available.

**Substitute notice methods** (typically all three required):

- Email notice (if email address available and not compromised).
- Conspicuous posting on the entity's website for a defined period (typically 30 days).
- Notification to major statewide media outlets.

**State variations on cost threshold**:

- California: $250,000
- Illinois: $250,000 (and/or >500,000 IL residents) [VERIFY]
- Most states: $250,000 is the de facto standard inherited from the California model.
- A few states use lower thresholds or don't specify (VERIFY against specific state statute).

---

### 4.7 Credit Monitoring — States Requiring Mandatory Credit Monitoring

| State                | Credit Monitoring Required | Trigger                            | Duration                                                         |
| -------------------- | -------------------------- | ---------------------------------- | ---------------------------------------------------------------- |
| Colorado             | Yes                        | SSN compromised                    | 12 months                                                        |
| Connecticut          | Yes                        | SSN compromised                    | 24 months                                                        |
| Delaware             | Yes                        | SSN compromised                    | 12 months                                                        |
| District of Columbia | Yes                        | Any qualifying breach              | 18 months (identity theft protection)                            |
| Massachusetts        | Yes                        | SSN compromised                    | 18 months (CRAs must provide 42 months)                          |
| Pennsylvania         | Yes                        | SSN, DL, or financial account      | 12 months                                                        |
| Florida              | [VERIFY]                   | SSN breach affecting 500+ [VERIFY] | [VERIFY]                                                         |
| California           | No                         | N/A                                | N/A (mandates offering services for certain breaches under CCPA) |
| New York             | No                         | N/A                                | N/A                                                              |
| Most other states    | No                         | N/A                                | N/A                                                              |

---

### 4.8 Private Rights of Action

| State             | Private Right of Action                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------- |
| California        | Yes — CCPA § 1798.150 (limited to specified categories; $100–$750/consumer/incident or actual damages)                  |
| DC                | Yes — unfair trade practice claim available to any consumer                                                             |
| Massachusetts     | Potentially via ch. 93A (Consumer Protection Act) [VERIFY]                                                              |
| Puerto Rico       | Yes                                                                                                                     |
| Alabama           | No                                                                                                                      |
| Florida           | No (AG enforcement only)                                                                                                |
| Mississippi       | No                                                                                                                      |
| Pennsylvania      | No (AG enforcement only)                                                                                                |
| Most other states | No explicit private right of action in breach notification statutes; some may allow via unfair trade practices statutes |

---

### 4.9 Good Faith Acquisition Exemption

Most state breach notification statutes include an exemption for good faith acquisition of PI by an employee or agent of the entity if:

- The acquisition was for legitimate business purposes; AND
- The PI is not used for unauthorized purposes or subject to further unauthorized disclosure.

This is sometimes called the "employee safe harbor." It generally exempts inadvertent internal access from triggering notification. [VERIFY applicability in each state before relying on it.]

---

### 4.10 Cure Periods

Very few state breach notification statutes include formal cure periods. However:

- Some AG offices have informal practice of providing notice before seeking penalties.
- HIPAA has a tiered penalty structure that accounts for unknowing violations and good-faith corrections.
- Generally, breach notification statutes impose strict liability once a breach is confirmed; there is no statutory "right to cure" the failure to notify (unlike some comprehensive privacy laws like the old CCPA before CPRA).

---

## 5. Safe Harbor Analysis

### 5.1 Encryption Safe Harbor

**Mechanism**: Nearly all US state breach notification laws define "personal information" subject to notification requirements as data that is **not encrypted** (or not secured by equivalent measures). Properly encrypted data, when the key has not been compromised, is treated as not being "personal information" for breach notification purposes — eliminating the notification obligation.

**Standard**: Most statutes do not specify an encryption algorithm standard; however, common references include:

- NIST FIPS 197 (AES-128, AES-256)
- NIST SP 800-111 (storage encryption)
- NIST SP 800-52 (TLS for data in transit)
- FIPS 140-2 (cryptographic module validation)

**Key caveat**: If the encryption key is **also compromised** in the breach, the encrypted data is no longer considered secure and notification may be required. This applies under HIPAA and is implied in most state laws.

**States with explicit encryption safe harbor**: All 50 states + DC essentially have this (it is built into the definition of PI or "breach").

**States with explicit destruction safe harbor**: Most states that define "secured" information include properly destroyed data.

### 5.2 HIPAA as State-Law Safe Harbor

Several states explicitly exempt HIPAA-covered entities from their state breach notification requirements, provided the entity complies with HIPAA's breach notification requirements:

**States with HIPAA safe harbor** (explicit statutory exemption):

- Arkansas [VERIFY]
- Georgia [VERIFY]
- Louisiana [VERIFY]
- New Mexico
- Oklahoma [VERIFY]
- South Carolina [VERIFY]
- Tennessee [VERIFY]
- Virginia (partial — for health information)
- Wisconsin [VERIFY]

**States without HIPAA safe harbor** (both state and HIPAA obligations apply):

- California — CA law applies independently; HIPAA-covered entities must also comply with CA § 1798.29
- New York — No HIPAA exemption
- Colorado — No HIPAA exemption
- Massachusetts — No HIPAA exemption (though state AG typically coordinates with federal enforcement)
- Florida — No complete HIPAA exemption
- Texas — No HIPAA exemption

**Practitioner note**: Even where a HIPAA safe harbor exists, the state's definition of "personal information" may be broader than PHI (e.g., SSN-only breaches outside HIPAA context). HIPAA compliance only satisfies the health data breach; non-health data breaches are governed by state law.

### 5.3 GLBA as State-Law Safe Harbor

A number of state breach notification statutes exempt entities subject to GLBA/Safeguards Rule compliance from state-level obligations, provided they comply with GLBA breach notification requirements. Note that GLBA's FTC-facing notification requirement (30 days, 500+ consumers) does not require direct consumer notification — so states may still require direct consumer notice even where they grant a GLBA safe harbor.

**States with GLBA/financial institution exemptions** [VERIFY each]:

- Many states exempt financial institutions regulated under GLBA (e.g., banks, credit unions, registered broker-dealers regulated by FFIEC agencies).
- This exemption typically covers entities under the jurisdiction of federal banking regulators (OCC, FDIC, Fed, NCUA) who are subject to the Interagency Guidance on Response Programs for Unauthorized Access to Customer Information.

### 5.4 NIST Framework / Cybersecurity Program Safe Harbor (Ohio Model)

**Ohio**: Ohio SB 220 (2018) — Ohio Data Protection Act — created the first breach **litigation safe harbor** in the US. A business that:

- Creates, maintains, and complies with a **written cybersecurity program**;
- That **reasonably conforms** to one of the named frameworks (NIST CSF, NIST SP 800-171, NIST SP 800-53, FedRAMP, CIS Critical Security Controls, ISO 27000 family, HIPAA, GLBA, FISMA, HITECH, or PCI DSS + one of the above);

...has an **affirmative defense** against tort claims arising from a breach. This is a litigation safe harbor, **not** an exemption from notification obligations.

**Similar legislation** [VERIFY current status]:

- **Connecticut** (PA 21-59) — created a cybersecurity safe harbor from punitive damages for entities with qualifying security programs (similar to Ohio). Effective July 6, 2021.
- **Utah** (HB 80) — created cybersecurity affirmative defense for entities with qualifying security programs. Effective March 2021 [VERIFY].
- **Iowa** (HF 2310) — safe harbor for entities with qualifying programs [VERIFY status].
- **Indiana** (HEA 1372) — safe harbor [VERIFY status].
- **Illinois** (SB 1624) — proposed [VERIFY if enacted].

### 5.5 PCI DSS Provisions

PCI DSS (Payment Card Industry Data Security Standard) is an industry standard, not a law. However:

- Some state statutes reference PCI DSS compliance in safe harbor provisions (e.g., Ohio Data Protection Act).
- Nevada NRS 603A.215 specifically addresses payment card security: a data collector that accepts payment cards and is compliant with PCI DSS is not liable for damages from a breach of security of the payment card information, except in limited circumstances. [VERIFY current text]
- **No state completely exempts PCI-compliant entities from breach notification obligations** — PCI DSS compliance addresses security standards for card data, not state notification law compliance.

---

## 6. Territories

### 6.1 District of Columbia

**Statute**: D.C. Code §§ 28-3851 to 28-3853 (Security Breach Protection Amendment Act of 2020)

- **Timeline**: Most expedient time possible and without unreasonable delay.
- **AG Notification**: Required if breach affects **50 or more** DC residents.
- **PI Definition**: Broad — includes medical, genetic, biometric, health insurance, username/email + credentials.
- **Credit Monitoring**: 18 months of identity theft protection required for all qualifying breaches.
- **Private Right of Action**: Yes — unfair trade practice; consumers may sue.
- **Penalties**: Civil penalties enforceable by AG.

### 6.2 Puerto Rico

**Statute**: P.R. Laws Ann. tit. 10, §§ 4051–4055 (Citizen Information on Data Banks Security Act, originally HB 1184, 2005)

- **Timeline**: Agency/Regulator notification within **10 days** (non-extendable); consumer notification as expeditiously as possible.
- **Regulator Notification**: Notify Department of Consumer Affairs (DACO) within 10 days; DACO makes public announcement within 24 hours.
- **PI Definition**: Name + SSN, DL number or other official ID, financial account/banking credentials.
- **Private Right of Action**: Yes.
- **Penalties**: $500–$5,000 per violation.

### 6.3 US Virgin Islands

**Statute**: V.I. Code Ann. tit. 14, §§ 2208–2210 (enacted ~2005)

- **Timeline**: Most expedient time possible and without unreasonable delay.
- **AG/Regulator Notification**: **No requirement** to notify any government agency.
- **PI Definition**: Name + SSN, DL, financial account credentials.
- **Safe Harbor**: Encrypted data exempt.

### 6.4 Guam

**Statute**: 9 Guam Code Ann. §§ 48.10 et seq.

- **Timeline**: Without unreasonable delay, consistent with measures to determine scope.
- **AG/Regulator Notification**: Not specified in available sources [VERIFY].
- **PI Definition**: Standard (name + SSN, DL, financial account).
- **Safe Harbor**: HIPAA-compliant entities may satisfy Guam requirements through HIPAA compliance.

### 6.5 American Samoa

American Samoa does **not** have a dedicated breach notification statute. Federal laws (HIPAA for covered entities, GLBA for financial institutions, etc.) apply to applicable entities operating in American Samoa. [VERIFY — some sources include American Samoa in the "all 50 states + DC + territories" count but the territory may not have enacted standalone breach notification legislation.]

---

## 7. Source URLs

The following sources were used in compiling this research document:

### Federal Sources

- HHS HIPAA Breach Notification Rule: https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html
- HHS Breach Safe Harbor Guidance: https://www.hhs.gov/guidance/document/breach-safe-harbor
- 45 CFR § 164.404 (eCFR): https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-D
- FTC GLBA Safeguards Rule Amendment (Oct 2023): https://www.ftc.gov/news-events/news/press-releases/2023/10/ftc-amends-safeguards-rule-require-non-banking-financial-institutions-report-data-security-breaches
- FTC Safeguards Rule Notification Now in Effect (May 2024): https://www.ftc.gov/business-guidance/blog/2024/05/safeguards-rule-notification-requirement-now-effect
- Federal Register GLBA Amendment: https://www.federalregister.gov/documents/2023/11/13/2023-24412/standards-for-safeguarding-customer-information
- SEC Cybersecurity Rules Press Release (July 2023): https://www.sec.gov/newsroom/press-releases/2023-139
- CIRCIA CISA Page: https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/cyber-incident-reporting-critical-infrastructure-act-2022-circia
- CIRCIA NPRM Federal Register (Apr 2024): https://www.federalregister.gov/documents/2024/04/04/2024-06526/cyber-incident-reporting-for-critical-infrastructure-act-circia-reporting-requirements
- FCC Data Breach Rules Federal Register (Feb 2024): https://www.federalregister.gov/documents/2024/02/12/2024-01667/data-breach-reporting-requirements

### State Sources

- California AG Data Breach Reporting: https://oag.ca.gov/privacy/databreach/reporting
- California Cal. Civ. Code § 1798.82: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.82
- California 30-day timeline (Data Protection Report): https://www.dataprotectionreport.com/2025/11/california-tightens-data-breach-notification-timelines-imposes-30-day-notice-requirement/
- New York SHIELD Act AG Page: https://ag.ny.gov/resources/organizations/data-breach-reporting/shield-act
- New York 30-day amendment (Inside Privacy): https://www.insideprivacy.com/cybersecurity-2/new-york-adopts-amendment-to-the-state-data-breach-notification-law/
- Colorado C.R.S. § 6-1-716 (Justia 2024): https://law.justia.com/codes/colorado/title-6/fair-trade-and-restraint-of-trade/article-1/part-7/section-6-1-716/
- Florida Fla. Stat. § 501.171 (2025): https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0500-0599/0501/Sections/0501.171.html
- Texas Bus. & Com. Code § 521.053 (2024 Justia): https://law.justia.com/codes/texas/business-and-commerce-code/title-11/subtitle-b/chapter-521/subchapter-b/section-521-053/
- Texas DWT Update (2023): https://www.dwt.com/blogs/privacy--security-law-blog/2023/06/texas-data-breach-notification-law-update
- Illinois AG Data Breach: https://illinoisattorneygeneral.gov/consumer-protection/for-businesses/data-breach/
- Massachusetts Mass.gov Requirements: https://www.mass.gov/info-details/requirements-for-data-breach-notifications
- Massachusetts ch. 93H: https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXV/Chapter93h
- Washington RCW 19.255.010 (WA Leg): https://app.leg.wa.gov/rcw/default.aspx?cite=19.255.010
- Washington AG Data Breach Laws: https://www.atg.wa.gov/washington-s-data-breach-notification-laws
- Virginia Va. Code § 18.2-186.6: https://law.lis.virginia.gov/vacode/title18.2/chapter6/section18.2-186.6/
- Ohio Data Protection Act (Alston & Bird): https://www.alstonprivacy.com/ohio-enacts-cybersecurity-safe-harbor-law/
- Nevada NRS 603A.220 (Justia 2024): https://law.justia.com/codes/nevada/chapter-603a/statute-603a-220/
- Oregon ORS 646A.604: https://oregon.public.law/statutes/ors_646a.604
- Connecticut Conn. Gen. Stat. § 36a-701b (Justia 2024): https://law.justia.com/codes/connecticut/title-36a/chapter-669/section-36a-701b/
- Pennsylvania 2024 Update (Perkins Coie): https://perkinscoie.com/insights/update/2024-breach-notification-law-update-unique-new-state-obligations-and-widespread-new
- Vermont 9 V.S.A. § 2435: https://legislature.vermont.gov/statutes/section/09/062/02435
- Mississippi Miss. Code Ann. § 75-24-29: https://law.justia.com/codes/mississippi/title-75/chapter-24/general-provisions/section-75-24-29/
- South Dakota SB 62: https://natlawreview.com/article/south-dakota-enacts-data-breach-notification-law
- North Dakota breach notice law (NDLEG): https://ndlegis.gov/cencode/t51c30.pdf
- DC Code § 28-3852: https://code.dccouncil.gov/us/dc/council/code/sections/28-3852
- Puerto Rico breach law: https://law.justia.com/codes/puerto-rico/title-ten/subtitle-3/chapter-310/4052/
- US Virgin Islands Code § 2208: https://law.justia.com/codes/virgin-islands/2019/title-14/chapter-110/subchapter-i/2208/
- Guam breach notification (DataGuidance): https://www.dataguidance.com/sites/default/files/notification_of_breaches_of_personal_information_ss48-10_et_seq._of_title_9_of_the_guam_code_annotated.pdf

### Secondary / Aggregator Sources

- NCSL Security Breach Notification Laws: https://www.ncsl.org/technology-and-communication/security-breach-notification-laws
- Davis Wright Tremaine State Statutes Map: https://www.dwt.com/gcp/state-data-breach-statutes
- Perkins Coie Security Breach Notification Chart: https://perkinscoie.com/insights/publication/security-breach-notification-chart
- IAPP US State Data Breach Notification Chart: https://iapp.org/resources/article/state-data-breach-notification-chart
- Foley State Data Breach Notification Laws (Apr 2024 PDF): https://www.foley.com/wp-content/uploads/2024/04/23.45248-Data-Breach-Chart-4.10.24.pdf
- Mintz Matrix (Feb 28, 2025): https://www.mintz.com/sites/default/files/media/documents/2025-02-27/Mintz%20Matrix%20-%20State%20Data%20Breach%20Matrix%20%20AS%20OF%20FEB%2028%202025.pdf
- Perkins Coie 2024 Breach Law Update: https://perkinscoie.com/insights/update/2024-breach-notification-law-update-unique-new-state-obligations-and-widespread-new
- Perkins Coie 2025 Breach Law Update: https://perkinscoie.com/insights/update/2025-breach-notification-law-update
- Privacy Rights Clearinghouse 2026 Survey: https://privacyrights.org/resources-tools/reports/data-breach-notification-laws-50-state-survey-2026-edition
- Connecticut Safe Harbor (Akin Gump): https://www.akingump.com/en/insights/blogs/ag-data-dive/connecticut-expands-breach-reporting-and-creates-cybersecurity-safe-harbor
- Massachusetts Credit Monitoring Amendment (Inside Privacy): https://www.insideprivacy.com/data-security/data-breaches/massachusetts-amends-data-breach-notification-law-to-require-free-credit-monitoring/
- FCC 2024 Rules (Cybersecurity Dive): https://www.cybersecuritydive.com/news/fcc-data-breach-reporting-rules/710444/
- Sixth Circuit FCC ruling (Nelson Mullins): https://www.nelsonmullins.com/insights/alerts/fcc-download/all/the-data-security-practices-of-communications-service-providers-sixth-circuit-upholds-2024-fcc-data-breach-reporting-and-notification-rules

---

## Appendix A: States with Hard Numeric Deadlines vs. "Expedient" Standard

### Hard Numeric Deadlines (Individual Notification)

| Deadline    | States                                                                             |
| ----------- | ---------------------------------------------------------------------------------- |
| **30 days** | CA (eff. Jan 1, 2026), CO, FL (from determination), ME, NY (eff. Dec 21, 2024), WA |
| **45 days** | AL, MD, NM, OR, RI, TN, VT                                                         |
| **60 days** | CT, DE, LA, SD, TX                                                                 |
| **90 days** | [None currently — CT reduced from 90 to 60 days]                                   |

### "Expedient" / "Without Unreasonable Delay" Standard (No Fixed Deadline)

AK, AR, AZ, GA, HI, ID, IL, IN, IA, KS, KY, MA, MI, MN, MS, MO, MT, NE, NV, NC, ND, NH, NJ, OH, OK, PA, SC, UT, VA, WI, WV, WY, DC, VI, GU

> Note: Within the "expedient" states, many regulators and courts have interpreted this standard as 30–45 days. Pennsylvania tightened its law in 2024 (SB 824) but retained "without unreasonable delay" language while adding AG notification at 500+ residents.

---

## Appendix B: Penalty Overview by State

| State             | Civil Penalty Range                               | Max per Breach                     | Enforcement                 |
| ----------------- | ------------------------------------------------- | ---------------------------------- | --------------------------- |
| Alabama           | $5,000/day                                        | $500,000                           | AG                          |
| Alaska            | Up to $500/resident not notified                  | $50,000                            | AG                          |
| Arizona           | Up to $10,000/consumer                            | $500,000                           | AG                          |
| California (CCPA) | $2,500–$7,500/intentional violation               | No statutory cap                   | AG; private right of action |
| DC                | [VERIFY per-violation amount]                     | [VERIFY]                           | AG; private right of action |
| Florida           | $1,000/day (first 30 days); $50,000/30-day period | $500,000                           | AG                          |
| Hawaii            | Up to $2,500/violation                            | [VERIFY]                           | AG                          |
| Idaho             | Civil action; up to $25,000/breach                | $25,000                            | AG                          |
| Indiana           | Up to $1,000/violation                            | $500,000                           | AG                          |
| Maine             | Up to $500/violation                              | $2,500/day                         | AG                          |
| Virginia          | [VERIFY per-violation]                            | $150,000 per breach series         | AG                          |
| Texas             | Up to $500/individual/violation                   | $50,000/incident [VERIFY]          | AG                          |
| HIPAA             | $137–$2,067,813/violation                         | $2,067,813/violation category/year | HHS OCR                     |

> Penalties vary widely. Most state enforcement is through AG civil actions. Private rights of action are rare in breach notification statutes specifically (vs. underlying privacy statutes like CCPA).

---

_End of Research Document_

**Prepared for**: `legalcode-us-breach-notification-triage` skill development
**Research methodology**: Web searches using WebSearch tool targeting official statutory sources, government websites (HHS, FTC, SEC, FCC, CISA, state AG offices), and established legal publisher resources (Perkins Coie, Davis Wright Tremaine, IAPP, NCSL, Mintz, Foley).
**Confidence level**: High for federal law and Group A/B states; Medium for Group C states (recommend verification against primary state statutes before production use).
**Items marked [VERIFY]**: Should be checked against the cited statute's current text before inclusion in any client-facing or production legal AI output.
