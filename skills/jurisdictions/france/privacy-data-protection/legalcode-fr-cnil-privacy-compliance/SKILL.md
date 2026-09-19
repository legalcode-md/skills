---
name: legalcode-fr-cnil-privacy-compliance
description: 'Assess an organization''s privacy compliance against French data protection law: the Loi
  Informatique et Libertés (LIL, Loi n°78-17 du 6 janvier 1978 modifiée), CNIL regulatory guidance, and
  GDPR as implemented in France. Covers CNIL cookie guidelines (2020/2022), France''s 15-year digital
  age of consent, employee data and CSE consultation obligations, DPO designation and CNIL registration,
  mandatory DPIA (AIPD) list, data breach notification, processing register (Article 30), data subject
  rights, international transfers, and CNIL enforcement trends. Use when conducting a CNIL compliance
  assessment, preparing for a CNIL inspection (contrôle), auditing a privacy program in France, advising
  on French-specific GDPR derogations, reviewing cookie consent mechanisms for French audiences, assessing
  employee monitoring compliance under French labor law, or performing M&A privacy due diligence on a
  French entity. France-specific skill covering CNIL enforcement cases and administrative sanction procedure.'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode — CNIL Privacy Compliance Assessment (France)

> **Disclaimer**: This skill provides a framework for AI-assisted privacy compliance assessment
> under French data protection law. It does not constitute legal advice. All outputs should be
> reviewed by a qualified French legal professional (avocat spécialisé en droit des données
> personnelles) or certified Data Protection Officer before use. Laws, CNIL guidelines, and
> enforcement guidance change frequently; verify current applicability on Légifrance and CNIL's
> official website before relying on any provision described here. Statutory, regulatory, and case
> references carry hallucination risk — verify against authoritative sources (Légifrance,
> www.cnil.fr, EDPB official publications) before relying on them. This skill does not assess
> criminal data protection exposure — for criminal liability under Articles 226-16 et seq. of
> the Code pénal, engage a criminal defense specialist.

---

## Purpose and Scope

This skill assesses an organization's privacy compliance program against French data protection
law, including GDPR as supplemented and modified by French national law.

**Covers:**

- Applicability of the Loi Informatique et Libertés (LIL) and GDPR in a French context
- CNIL-specific requirements going beyond baseline GDPR
- Cookie and tracker consent compliance (Article 82 LIL; CNIL Guidelines 2020)
- France's digital age of consent (15 years — Article 7-1 LIL)
- Employee data: monitoring, biometrics, geolocation, CSE consultation obligations
- DPO designation and mandatory CNIL registration (Déclaration DPD)
- DPIA/AIPD requirements: CNIL's mandatory processing list
- Data breach notification to CNIL (72-hour rule; portal notifications.cnil.fr)
- Processing register (Registre Article 30) — structure and content requirements
- Data subject rights: the 8 GDPR rights plus French additions (droit au déréférencement,
  post-mortem directives, indirect access to sensitive government files)
- International data transfers: SCCs, EU-US DPF, Transfer Impact Assessments
- CNIL enforcement process: contrôles, mises en demeure, sanctions, formation restreinte
- CNIL sectoral référentiels and binding Règlements-Types (biometrics, genetics, health data)
- Commercial prospecting rules under French law (opt-in/opt-out rules; Bloctel registry)
- AI and automated decision-making: Article 10 LIL; CNIL AI guidance series 2024-2026

**Does not:**

- Provide general GDPR compliance assessment (use a dedicated GDPR skill for multi-jurisdiction
  needs; this skill focuses on French-specific requirements)
- Cover criminal data protection liability under the Code pénal
- Assess processing by public authorities in the exercise of their public power (specific
  French administrative law rules apply)
- Cover the Système National des Données de Santé (SNDS) health data framework in full —
  health data processing requires a dedicated assessment against CNIL's health data référentiels
- Replace an assessment by a CNIL-accredited compliance reviewer or external DPO

---

## Jurisdiction and Governing Law

**Primary Jurisdiction**: France (République Française)

**Governing Framework**:

| Source                                | Reference                                               | Role                                                    |
| ------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| EU General Data Protection Regulation | Regulation (EU) 2016/679                                | Directly applicable; primary framework                  |
| Loi Informatique et Libertés (LIL)    | Loi n°78-17 du 6 janvier 1978 modifiée                  | French national law implementing and supplementing GDPR |
| LIL Reform Act                        | Loi n°2018-493 du 20 juin 2018                          | Transposed GDPR into French law                         |
| Implementation Ordinance              | Ordonnance n°2018-1125 du 12 décembre 2018              | Technical harmonization with GDPR                       |
| ePrivacy (cookies)                    | Article 82 LIL (transposing Directive 2002/58/EC)       | Cookie and tracker rules                                |
| CNIL Cookie Guidelines                | Délibération du 17 septembre 2020 (publiée 1 oct. 2020) | Binding guidance on cookie consent                      |
| CNIL Cookie Recommendation            | Recommandation du 1er octobre 2020                      | Practical implementation guidance                       |
| Code du travail                       | Various articles — L.2312-8, L.2312-37, L.1222-4        | Employee monitoring consultation obligations            |
| Code pénal                            | Articles 226-16 à 226-24                                | Criminal liability for data protection violations       |

**Regulatory Authority**: Commission Nationale de l'Informatique et des Libertés (CNIL), 3 Place de Fontenoy, 75007 Paris. Established by the original 1978 LIL. CNIL exercises its supervisory authority through:

- **Formation plénière**: Full assembly for major policy and guideline decisions
- **Formation restreinte**: Restricted sanctioning body (6 members, independent from investigation teams) for ordinary sanction procedure
- **Président de la CNIL**: Simplified sanction procedure (procédure simplifiée) and mises en demeure

[VERIFY] Confirm CNIL composition and current President on www.cnil.fr before any reference to CNIL personnel or current procedure.

**Territorial Scope**: The LIL and GDPR apply to:

- Controllers and processors established in France
- Controllers not established in France but whose processing activities target French data subjects (offering goods/services to persons in France, or monitoring their behaviour in France)
- Any processing where French law applies by virtue of international public law

---

## French-Specific Derogations from GDPR

The following French national derogations are the core focus of this skill. Understanding these distinguishes French/CNIL compliance from generic GDPR compliance:

| Topic                                   | GDPR Default                                            | French Derogation (LIL)                                                                                                          |
| --------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Age of digital consent**              | 16 years (Article 8 GDPR — member state may set 13-16)  | **15 years** (Article 7-1 LIL — "majorité numérique")                                                                            |
| **Cookie consent**                      | Silence may equal consent depending on context          | Silence = refusal (Article 82 LIL); continuation of browsing is NOT consent                                                      |
| **Cookie refusal mechanism**            | No specific requirement                                 | Reject button must be as easy as Accept button ("refus aussi facile que l'acceptation")                                          |
| **Analytics cookie exemption**          | No specific exemption                                   | Exempt from consent if 7 strict conditions met (CNIL Guidelines 2020)                                                            |
| **Post-mortem data rights**             | GDPR does not apply to deceased persons                 | Articles 84-86 LIL — data subjects may leave instructions for post-death handling; heirs may exercise certain rights             |
| **NIR (national ID number)**            | General special category rules                          | Article 22 LIL — strict authorization required; only authorized entities may process                                             |
| **DPO registration**                    | Notify supervisory authority                            | Formal online registration with CNIL required; SIREN/SIRET needed; public registry maintained                                    |
| **Employee monitoring**                 | General GDPR proportionality                            | Code du travail: CSE must be informed and consulted before implementing monitoring systems; "nominator" rule for personal emails |
| **Biometric systems**                   | General Article 9 conditions                            | CNIL Règlement Type Biométrie (2019) — binding; DPIA mandatory before implementation                                             |
| **Criminal liability**                  | Outside GDPR scope                                      | Code pénal Articles 226-16 et seq. — up to 5 years' imprisonment and €300,000 fine for certain violations                        |
| **Health data**                         | General Article 9 conditions + Member State derogations | CNIL authorization required for health data warehouses; specific référentiels MR-001 to MR-006 for research                      |
| **Indirect access to restricted files** | Standard rights                                         | CNIL acts as intermediary for access to police/national security files                                                           |
| **Commercial prospecting**              | General GDPR + ePrivacy Directive                       | B2C: opt-in required; B2B to professional addresses: opt-out suffices; Bloctel cold-call registry                                |

---

## Interactive Clarification

This skill uses **interactive clarification** at key decision points. Rather than assuming
organizational context, the workflow pauses and asks when:

- The assessment scope or trigger would materially change the approach
- Organizational complexity (group structure, multiple entities) affects analysis
- The program maturity level determines appropriate depth of review
- A CNIL contrôle notice changes the urgency and priorities

Use the **⟁ CLARIFY** pattern wherever marked. If the user has already provided the
information, skip the question and proceed. For batch or non-interactive runs, use the
defaults stated at each CLARIFY point.

---

## Workflow

### Step 1: Accept Input

Accept the assessment input in any of these formats:

- **Program documentation**: Privacy policy, DPO designation records, processing register,
  cookie audit report, DPIA documentation, DPA agreements, consent records, breach register,
  employee monitoring policies, data retention schedules
- **CNIL contrôle preparation package**: Documentation assembled in response to a CNIL
  inspection notice or questionnaire
- **Organization description**: User describes the organization and its processing activities
  without formal documentation — lower confidence output; all findings flagged [LOW CONFIDENCE]
- **Specific topic focus**: Cookie banner review only, DPO assessment only, employee
  monitoring assessment only — run the relevant workflow module only

If no documentation is provided, confirm the assessment will be description-based and all
findings will carry [LOW CONFIDENCE — based on description only].

---

### Step 2: Gather Context

**⟁ CLARIFY** — Before beginning, gather the following context (skip questions already answered):

1. **Assessment trigger** — What prompted this review?
   - Options: **CNIL contrôle notice received** (highest urgency — prepare for inspection),
     **Annual internal review**, **M&A due diligence** (assess target's CNIL compliance
     posture), **New processing or product launch** (pre-launch assessment), **Complaint
     received** (individual complaint via CNIL), **Cookie banner remediation** (focused
     on cookie compliance), **DPO designation review**, **Breach response**, **Other**
   - _Why this matters_: A CNIL contrôle triggers immediate gap-closure and document preparation;
     a new product launch requires a prospective DPIA; M&A changes what is material to assess.
   - Default (batch): Annual internal review

2. **Organization type** — What kind of entity?
   - Options: **French-registered company (SA/SAS/SARL/etc.)**, **French branch of foreign
     company**, **French subsidiary of multinational group**, **Foreign company processing
     data about French residents**, **Public authority**, **Healthcare provider**
   - _Why this matters_: Foreign companies targeting French residents face the same LIL/GDPR
     obligations but with different DPO registration paths; healthcare providers face stricter
     health data authorization requirements.

3. **Main activities** — What are the primary processing activities?
   - Options (multiple): **E-commerce / online retail**, **B2B services**, **HR / employment**,
     **Healthcare / medico-social**, **Finance / insurance**, **Marketing / advertising**,
     **Technology / SaaS / app provider**, **Public service**, **Research**, **Other**
   - _Why this matters_: Marketing triggers aggressive cookie enforcement; healthcare triggers
     CNIL authorization requirements; HR triggers CSE consultation obligations.

4. **CNIL history** — Any prior CNIL contact?
   - Options: **No prior contact**, **Prior contrôle (no sanction)**, **Mise en demeure
     received (currently or historically)**, **Prior sanction (paid)**, **Active enforcement
     matter**, **Don't know**
   - _Why this matters_: Repeat violations attract higher sanctions. Prior mises en demeure
     on the same topic increase non-compliance risk classification.

5. **Assessment scope** — Full assessment or targeted?
   - Options: **Full 10-domain assessment**, **Cookies and trackers only**, **Employee
     data compliance only**, **DPO and governance**, **DPIA program review**, **Data
     subject rights procedure**, **International transfers**, **Breach notification procedure**
   - Default (batch): Full 10-domain assessment

---

### Step 3: Gather Legal Authority

Use **legalcode-mcp** (if connected) to search for current CNIL guidance, relevant
enforcement decisions, and legislative updates relevant to the organization's sector.

**Research process:**

1. Identify the organization's primary processing sectors (from Step 2) and search for:
   - Current CNIL guidance relevant to those sectors (sectoral référentiels)
   - Recent CNIL enforcement decisions involving similar processing or sectors
   - Any EDPB coordinated enforcement topics relevant to this assessment
   - Recent LIL amendments or CNIL guidance updates

2. Save relevant results to `/tmp/legalcode-cnil-assessment-authority.md` structured as:

   ```markdown
   # CNIL Authority Reference — [Organization Name]

   ## Date: [date]

   ### Applicable CNIL Guidance

   - [Guideline/Recommendation/Règlement-Type + relevance]

   ### Recent CNIL Enforcement — Relevant Cases

   - [Entity, fine amount, violation, date — sourced from CNIL sanctions page]

   ### Sector-Specific Référentiels

   - [Référentiel name, binding or advisory, scope]

   ### EDPB Coordinated Enforcement

   - [Active coordination topics, deadlines]
   ```

3. Throughout the assessment, cite from this reference file. Mark all legalcode-mcp-sourced
   citations as VERIFIED in the Glass Box audit trail.

**If legalcode-mcp is not connected:**

- Mark all CNIL guidance references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — all citations require verification"`
- Focus the assessment on structural compliance gaps rather than legal authority depth

---

### Step 4: Run the 10-Domain Compliance Assessment

Assess the organization across the 10 compliance domains below. For each domain, classify
findings using the four-tier system in **Compliance Classification** below. Generate
actionable remediation steps for every PARTIAL, NON-COMPLIANT, and CRITICAL DEFICIENCY finding.

**⟁ CLARIFY** — For large or complex organizations with multiple entities or group structures:

- Ask whether to assess a single entity or a group
- If group: ask whether the French entity acts as controller-in-chief for the group, or
  whether each subsidiary is assessed independently
- Confirm whether a single DPO serves multiple entities (shared DPO designation)

---

### Step 5: Prioritize Findings

Apply the **Prioritization Framework** to organize findings by urgency and materiality.
Build the remediation roadmap based on the three-tier prioritization structure.

---

### Step 6: Quality Verification

Before delivering the assessment, run the quality checks in the **Quality Assurance
Framework** section:

1. Run the 5 Citation Quality Gates silently. Revise failures before delivery.
2. For every CRITICAL DEFICIENCY finding, run the 3-pass Self-Interrogation.
3. Assign Confidence Scores to all material findings.
4. Verify that all French-specific derogations have been assessed where applicable.
5. Generate the Glass Box Audit Trail and append it to the output.

---

### Step 7: Deliver Assessment

Structure the output using the **Output Format Template** at the end of this skill.

---

## 10-Domain Compliance Assessment Framework

### Domain 1: Governance Foundations

**Key elements to assess:**

| Element                                       | What to Check                                                                                                                             | Common Issues                                                                                                                                         |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Processing register (Registre Article 30)** | Exists; up-to-date; covers all processing activities; includes legal basis, retention periods, third-country transfers, security measures | Missing; outdated; covers systems not processing activities; no legal basis column; no retention periods                                              |
| **Legal basis documentation**                 | Each processing activity has a documented legal basis before processing begins; balancing test documented for legitimate interest claims  | Legal basis selected post-implementation; consent used where more stable basis applies; legitimate interest used for marketing without balancing test |
| **Retention schedules**                       | Defined retention periods per processing activity; enforced in systems (not just on paper); data deletion verified                        | Retention periods stated but not enforced; "as long as necessary" without specific timeframe; no deletion verification                                |
| **Controller / processor mapping**            | All processors identified; Article 28 DPAs in place                                                                                       | Processors operating without DPA; sub-processors not disclosed to CNIL in transfer documentation                                                      |
| **Privacy governance ownership**              | Senior accountability established; privacy by design/default documented                                                                   | No designated privacy responsibility; no privacy review in product development                                                                        |

**French-specific checks:**

- Is the Registre maintained with CNIL's recommended additional columns (legal basis, DPIA required)?
- Is the NIR (numéro de sécurité sociale) processed, and if so, is authorization confirmed?

---

### Domain 2: DPO Designation and Registration

**Mandatory designation triggers (GDPR Article 37):**

1. Processing by a public authority or body
2. Core activities consist of processing requiring **regular and systematic monitoring of data subjects at large scale**
3. Core activities consist of **large-scale processing of special categories** (Article 9) or criminal conviction data (Article 10)

**French-specific DPO registration requirement:**

Unlike many EU member states, CNIL requires **formal online registration** of the DPO:

- Registration portal: connexion.pro.cnil.fr
- Required information: organization's SIREN/SIRET, DPO's identity, contact details, roles covered (if shared DPO for a group), effective date
- CNIL issues a **Numéro de désignation (DPO-XXXX)**
- The DPO registry is publicly searchable
- DPO changes must be notified promptly with designation number and effective date

**Key elements to assess:**

| Element                    | What to Check                                                                                                              |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Designation obligation** | Does the organization trigger any of the three mandatory cases?                                                            |
| **Voluntary designation**  | If not mandatory, has voluntary designation been considered? CNIL encourages this for SMEs                                 |
| **CNIL registration**      | DPO registered on connexion.pro.cnil.fr? Designation number current?                                                       |
| **DPO qualifications**     | Legal and technical data protection expertise; sector knowledge; adequate resources                                        |
| **DPO independence**       | Reports to highest management; no conflicting roles (CISO, CFO, CEO, Head of IT are conflicted roles at same organization) |
| **DPO accessibility**      | Easily reachable by data subjects; contact details published in privacy notice                                             |
| **DPO resources**          | Time allocated; access to IT systems; budget for training and tools                                                        |

**⟁ CLARIFY** — If the organization is part of a group with a shared DPO:

- Ask whether the shared DPO covers all French entities in the CNIL registration
- Ask whether the DPO has sufficient time and resources given the group's French processing footprint

---

### Domain 3: Cookie and Tracker Compliance (Article 82 LIL)

This is consistently CNIL's highest enforcement category. Assess with precision.

**Legal basis:**

- Article 82 of the LIL implements the ePrivacy Directive (2002/58/EC as amended)
- CNIL Lignes directrices cookies (adopted 17 September 2020, published 1 October 2020)
- CNIL Recommandation cookies (1 October 2020)
- Note: Legitimate interest is NOT a valid legal basis for advertising/tracking cookies under
  Article 82 LIL / ePrivacy — explicit consent is required [VERIFY against CNIL latest guidance]

**Cookie audit checklist:**

**A — Tracker Inventory**

- [ ] Complete audit of all cookies and trackers deployed (first-party and third-party)
- [ ] Each tracker categorized: strictly necessary / audience measurement / functional / advertising / social media
- [ ] Third-party trackers identified with provider and purpose

**B — Consent Mechanism**

- [ ] No non-exempt trackers deposited before user makes a choice (including on page load)
- [ ] Consent banner displayed on first visit with clear Accept All / Refuse All options
- [ ] "Refuse all" button as visually prominent as "Accept all" (same size, color, position tier)
- [ ] No dark patterns: no auto-dismiss, no misleading pre-selections, no confusing button labeling
- [ ] Granular consent by purpose category available (or global Accept All / Refuse All)
- [ ] Pre-ticked boxes absent
- [ ] Consent proof stored: timestamp, scope, version, user identifier (pseudonymous)

**C — Consent Withdrawal**

- [ ] Easy withdrawal mechanism available at all times (footer link, cookie settings icon)
- [ ] Withdrawing consent as easy as giving it
- [ ] Preferences persist and are not reset on each visit (unless user explicitly re-consents)

**D — Re-solicitation**

- [ ] CNIL recommends re-soliciting consent no more frequently than every **6 months** for both consent and refusal
- [ ] No repeated consent banners designed to wear down user refusals

**E — Cookie Lifespan**

- [ ] Consent cookie maximum **13 months** lifespan (not auto-renewed on each visit)
- [ ] Analytics cookies maximum 13 months; data retention maximum 25 months

**F — Analytics Cookie Exemption**
Analytics tools are exempt from consent ONLY if ALL of the following 7 conditions are met:

1. Purpose strictly limited to audience measurement for the publisher's own site/app
2. Data only used by the publisher — not shared with third parties
3. Statistical data anonymized at collection point
4. No tracking across multiple sites or apps
5. No cross-linking with other processing operations
6. Cookie lifespan maximum 13 months (no auto-renewal)
7. Data retention maximum 25 months
8. Opt-out mechanism available
9. Users informed via privacy policy

If any condition is not met → **consent required**.

**G — Cookie Walls**

- [ ] Does the site use a "cookie wall" (access conditional on cookie acceptance)?
- [ ] If yes: is a genuine paid/tracker-free alternative offered at a reasonable price?
- [ ] Pure "consent or leave" walls without alternatives are generally non-compliant

**H — Special Technologies**

- [ ] Fingerprinting/canvas fingerprinting: treated same as cookies under Article 82 LIL → consent required
- [ ] Social media pixels (Facebook Pixel, LinkedIn Insight, etc.): consent required before loading
- [ ] Session replay tools: likely require consent under CNIL's draft 2026 guidance [VERIFY]
- [ ] A/B testing with persistent tracking: consent required if trackers used across sessions

**Recent enforcement cases (for calibration):**

- Google: €150M (2022), €325M (2025) — cookie refusal harder than acceptance, advertising cookies without consent
- Facebook/Meta: €60M (2022) — cookie refusal harder than acceptance
- Microsoft: €60M (2023) — cookie refusal harder than acceptance; analytics cookies without consent
- Amazon: €35M (2021) — auto-depositing advertising cookies without consent
- Shein: €150M (2025) — cookies placed without consent
- American Express France: €1.5M (2025) — cookie non-compliance

---

### Domain 4: Employee Data and CSE Consultation

French law adds significant obligations to GDPR's general principles for employee data.

**Core principles from CNIL and Code du travail:**

- Proportionality: monitoring measures must be proportionate to the stated objective
- Prior information: employees must be clearly informed before any monitoring system is implemented
- CSE consultation: the works council must be consulted before implementing monitoring systems
- "Nominator" rule: messages marked "personal" or "private" by the employee cannot be accessed by the employer without the employee present or judicial authorization

**Key assessment areas:**

**A — Employee Information (Art. L.1222-4 Code du travail)**

- [ ] Employees informed of all monitoring systems before implementation (written notice)
- [ ] Privacy notice provided at onboarding covering employer's data processing activities
- [ ] Information covers: monitoring purpose, legal basis, data retention, access rights

**B — CSE Consultation (Arts. L.2312-8 and L.2312-37 Code du travail)**
Mandatory prior consultation before implementing:

- [ ] Video surveillance systems or cameras
- [ ] Internet/email monitoring systems
- [ ] Geolocation/GPS tracking
- [ ] Biometric access control
- [ ] HR management software with significant impact on working conditions
- [ ] AI/algorithmic systems affecting employment decisions
- [ ] Any other system materially affecting the conditions, content, or duration of work

> Note: Failure to consult the CSE is a violation of French labor law independent of GDPR.
> This can render the monitoring system unlawful under both data protection law AND employment law.

**C — Email and Internet Monitoring**

- [ ] Acceptable use policy (charte informatique) in place and accessible to employees
- [ ] Policy incorporated into internal regulations (règlement intérieur) where required
- [ ] Monitoring proportionate to stated purpose; not continuous surveillance of all activity
- [ ] "Personal" / "private" labeled emails: employer access only with employee present or judicial authorization
- [ ] Browser history monitoring: proportionate purpose documented

**D — Geolocation of Vehicles**

- [ ] Geolocation limited to: fleet management, route optimization, security, billing by mileage
- [ ] Geolocation **prohibited outside working hours** unless employee provides specific consent for safety/emergency purpose
- [ ] Constant position monitoring during working hours: only if justified by nature of work
- [ ] Data retention: maximum 2 months for location data
- [ ] CSE consulted; employees informed

**E — Biometric Systems at the Workplace**

- [ ] CNIL Règlement Type Biométrie (28 March 2019) reviewed and applied [VERIFY currency]
- [ ] Three-tier gabarit (template) storage: individual holds template (preferred) → shared → employer-held (last resort)
- [ ] DPIA (AIPD) completed before implementation
- [ ] Necessity justification documented: biometrics only where genuine security need; badge/PIN alternative insufficient
- [ ] CSE consulted; employees informed

**F — Video Surveillance**

- [ ] Purpose legitimate and documented before installation
- [ ] No cameras in areas where employees have reasonable privacy expectation (break rooms, toilets, private offices where no safety/theft risk)
- [ ] No continuous surveillance of employees without specific security justification
- [ ] CSE consulted; employees informed; regulatory authority (inspecteur du travail) notified for certain types
- [ ] Retention period defined and applied (CNIL recommendation: typically not to exceed 30 days except for specific incidents)

**G — BYOD (Bring Your Own Device)**

- [ ] BYOD policy distinguishes personal from professional use
- [ ] No access to employee's personal data on private devices
- [ ] Employee consent obtained for any MDM (mobile device management) on personal devices

**H — HR Algorithmic Tools and Profiling**

- [ ] AI-based recruitment, performance evaluation, or departure-prediction tools: DPIA completed
- [ ] CSE consulted before deployment of AI tools affecting working conditions
- [ ] Candidates and employees informed of automated decision-making processes
- [ ] Human review available for algorithm-based employment decisions

---

### Domain 5: DPIA (AIPD) Program

**Legal basis**: GDPR Article 35; CNIL's official mandatory DPIA list [VERIFY current version]

**When a DPIA is mandatory in France:**

CNIL publishes both a "must-do" list and a "not required" list. A DPIA is required when processing meets any item on the must-do list, OR when it meets at least 2 of the 9 EDPB risk criteria:

**CNIL's 9 Risk Criteria (2+ criteria triggers mandatory DPIA):**

1. Evaluation/scoring/profiling (creditworthiness, performance, location)
2. Automated decision-making with legal or similarly significant effect
3. Systematic monitoring (employee surveillance, user tracking)
4. Sensitive data (health, genetic, biometric, religion, politics, sexuality, criminal)
5. Large-scale processing
6. Dataset matching/combination from multiple sources
7. Vulnerable data subjects (children, elderly, patients, job seekers, asylum seekers)
8. Innovative use of new technologies (biometrics, IoT, AI)
9. Processing that prevents exercise of rights or use of services

**CNIL's Mandatory DPIA List (selected highlights) [VERIFY against current CNIL PDF]:**

- Health data in medical establishments (patient records, medical algorithms, telemedicine)
- Genetic data of vulnerable persons
- HR profiling to profile employees (recruitment algorithms, high-potential detection, departure prediction)
- Continuous employee activity monitoring (DLP, video surveillance of cash handlers)
- Whistleblowing systems (Sapin II / Loi de Vigilance alerts)
- Health data warehouses and registries (entrepôts de données de santé)
- Profiling for contract exclusion (credit scoring, fraud detection, insurance exclusion)
- Biometric identification of vulnerable persons (pupils, patients)
- Large-scale geolocation tracking (mobile apps, transit ticketing)
- Profiling from external sources (data broker combinations, online ad personalization)
- Social/medico-social support processing

**DPIA assessment checklist:**

- [ ] Process in place to identify processing requiring a DPIA (using CNIL's mandatory list + 9 criteria)
- [ ] DPIAs completed and documented for all required processing (using CNIL's PIA methodology)
- [ ] DPO consulted during DPIA process (GDPR Article 35(2))
- [ ] DPIAs reviewed when processing changes significantly
- [ ] Prior consultation with CNIL completed for residual-high-risk processing (GDPR Article 36)
- [ ] CNIL PIA software used or equivalent documented methodology applied

**Prior consultation with CNIL (Article 36 GDPR):**
When residual risk after mitigation remains high, the controller **must consult CNIL before beginning processing**. CNIL has 8 weeks to respond (extendable to 14 weeks for complex cases). Proceeding without consultation when it is required is a CRITICAL DEFICIENCY.

---

### Domain 6: Data Subject Rights

**The 8 GDPR rights as implemented in France + French additions:**

| Right                             | Standard                                          | French Addition                                                                                        |
| --------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Right to information              | Articles 13-14 GDPR                               | —                                                                                                      |
| Right of access                   | Article 15 GDPR; 1 month (extendable to 3 months) | Indirect access to restricted files via CNIL                                                           |
| Right to rectification            | Article 16 GDPR                                   | —                                                                                                      |
| Right to erasure                  | Article 17 GDPR                                   | Droit au déréférencement (de-indexation from search engines — distinct from erasure)                   |
| Right to restriction              | Article 18 GDPR                                   | —                                                                                                      |
| Right to portability              | Article 20 GDPR                                   | —                                                                                                      |
| Right to object                   | Article 21 GDPR; absolute for direct marketing    | —                                                                                                      |
| Right against automated decisions | Article 22 GDPR                                   | Article 10 LIL: individuals informed of profiling contributing to (but not solely automated) decisions |
| Post-mortem directives            | Not covered by GDPR                               | Articles 84-86 LIL: instructions for data after death; heir rights                                     |

**Rights handling assessment:**

- [ ] Procedure to receive, log, and track rights requests (by type and deadline)
- [ ] Response within **1 month** from receipt; extension to 3 months with notification within first month
- [ ] Identity verification procedure: proportionate; does not create unreasonable burden
- [ ] Template responses for each right type (access, erasure, portability, objection)
- [ ] Erasure: confirmed that data actually deleted across all systems (including backups, processors, sub-processors within reasonable timeframe)
- [ ] Direct marketing opt-out honored **immediately**; suppression list maintained
- [ ] Post-mortem directive system: can the organization receive and process death instructions?

**CNIL complaint mechanism:**

- Individuals must typically first contact the organization before filing a CNIL complaint
- CNIL received 17,772 complaints in 2024 (record high)
- Most frequent complaint categories: telecoms/web/social media (49%), commerce (19%), employment (13%)
- CNIL provides investigation resources for individual complaints that can escalate to enforcement

**⟁ CLARIFY** — Ask whether the organization has received any unresolved CNIL complaints or
has pending matters with the CNIL's rights department. This significantly changes enforcement risk.

---

### Domain 7: Data Breach Notification

**Legal basis**: GDPR Articles 33-34; CNIL portal: notifications.cnil.fr

**72-hour rule:**

- Timeline starts when the controller has **reasonable certainty** a breach occurred (not when first suspicion arises)
- Preliminary notification within 72 hours acceptable — supplement as more information becomes available
- Missed deadline requires explanation in the notification

**Mandatory notification content to CNIL:**

1. Nature of the breach (confidentiality / integrity / availability)
2. Approximate categories and number of affected individuals
3. Approximate number of affected records
4. DPO or data protection contact details
5. Likely consequences for individuals
6. Measures taken or planned to address the breach
7. For delayed notifications: justification for delay

**Individual notification trigger:**
Required when breach presents **high risk** to individuals' rights and freedoms. Assessment factors:

- Sensitivity of data involved (health, financial, biometric, credentials)
- Scale and nature of breach
- Possible consequences (identity theft, discrimination, financial loss, reputation damage)

Individual notification must include: nature of breach, DPO/contact details, likely consequences, recommended protective steps (e.g., change passwords, monitor accounts).

**Internal breach register:**
All organizations must maintain an internal breach log regardless of notification thresholds. Log must record: date, nature, categories affected, approximate numbers, consequences, remedial measures.

**Breach notification assessment:**

- [ ] Internal breach register maintained and current
- [ ] Breach detection procedures in place (logs, monitoring, alerts)
- [ ] 72-hour notification procedure defined, tested, and role-assigned
- [ ] CNIL notification portal access configured (authenticated account)
- [ ] Individual notification procedure for high-risk breaches
- [ ] Processor notification obligation: processors must notify the controller promptly (typically well within 24-48 hours to allow controller to assess and notify CNIL within 72 hours)
- [ ] Template notifications prepared (CNIL notification, individual notification)

---

### Domain 8: International Data Transfers

**Legal basis**: GDPR Chapter V (Articles 44-49); CNIL guidance on cloud/US transfers

**Valid transfer mechanisms:**

| Mechanism                                    | Status                                         | Key Requirements                                                                       |
| -------------------------------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Adequacy decisions**                       | Preferred — no additional measures needed      | Check current EU Commission adequacy list [VERIFY]                                     |
| **EU-US Data Privacy Framework (DPF)**       | Adequate as of July 10, 2023                   | US recipient must be DPF-certified; verify on dataprivacyframework.gov                 |
| **Standard Contractual Clauses (2021 SCCs)** | Valid; most widely used                        | Must use EU Commission's June 2021 SCCs (not pre-2021 versions); select correct module |
| **Binding Corporate Rules (BCRs)**           | Valid for intragroup transfers                 | BCR authorization from lead EU DPA required; CNIL can be lead authority                |
| **Article 49 derogations**                   | Exceptional only; not for systematic transfers | Explicit consent, contract performance, vital interests, legal claims, public interest |

**Transfer Impact Assessment (TIA / Analyse d'Impact des Transferts — AITD):**
When using SCCs for transfers to countries without adequacy decisions (including the US for
non-DPF certified entities), organizations must conduct a TIA to verify that SCCs provide
effective protection given the destination country's legal framework (surveillance laws, access
by public authorities).

**Transfer assessment checklist:**

- [ ] Inventory of all third-country data transfers (including via SaaS/cloud providers, processors, sub-processors)
- [ ] Valid transfer mechanism identified for each transfer
- [ ] EU-US transfers: DPF certification checked for US recipients; or 2021 SCCs in place
- [ ] TIA conducted for SCC-based transfers (especially to the US)
- [ ] 2021 SCCs used (not pre-2021 versions); correct module selected (Controller-Controller / Controller-Processor / Processor-Controller / Processor-Processor)
- [ ] Sub-processor chains documented: SCCs flow down to sub-processors
- [ ] Annual DPF certification checks scheduled (certification expires annually)

**CNIL's specific focus: Google Analytics and US analytics tools**

- CNIL issued formal notices in 2022 to multiple website publishers for using Google Analytics
  without adequate transfer safeguards (US transfers without SCCs + TIA)
- This remains an enforcement priority; assess all US-based analytics, CRM, and marketing tools

---

### Domain 9: Special Processing Categories

**A — Children's Data (France's 15-Year Threshold)**

Under Article 7-1 LIL, information society services relying on consent require:

- For data subjects **aged 15 and over**: data subject may consent independently
- For data subjects **under 15**: **joint consent required** — both the minor's agreement AND a holder of parental authority ("titulaire de l'autorité parentale")

This applies to: social networks, apps, online platforms, any information society service using consent as legal basis.

**Children's data assessment:**

- [ ] Does the service target or knowingly accept users under 15?
- [ ] Age verification mechanism implemented (proportionate to service risk)
- [ ] For under-15 users: parental consent mechanism implemented
- [ ] Privacy notices and consent flows designed for age-appropriate comprehension
- [ ] Marketing to children without parental consent: CRITICAL DEFICIENCY
- [ ] DPIA completed for large-scale processing of children's data (CNIL mandatory list item)

**B — Health Data**

Health data processing in France requires more than meeting GDPR Article 9 exceptions. For certain health data processing:

- **CNIL référentiel/authorization**: Health data warehouses (entrepôts de données de santé) require CNIL authorization before processing — this is a hard legal stop
- **Research référentiels (MR-001 to MR-006)**: Specific authorization frameworks for clinical, epidemiological, and actuarial research [VERIFY current référentiels on CNIL website]
- **SNDS access**: Access to the Système National des Données de Santé requires specific authorization

**Health data assessment:**

- [ ] Health data processing identified in the register
- [ ] Applicable CNIL authorization or référentiel identified and complied with
- [ ] DPIA completed (always required for health data in medical establishments under CNIL list)
- [ ] Health data security measures: encryption, access controls, audit logs

**C — Biometric Data**

CNIL's Règlement Type Biométrie (28 March 2019) is binding. Any biometric processing not covered by this règlement-type must obtain specific CNIL authorization.

- [ ] Processing falls within the scope of the Règlement Type Biométrie, or specific authorization obtained
- [ ] Three-tier storage hierarchy applied (individual template preferred)
- [ ] DPIA completed before implementation

---

### Domain 10: Commercial Prospecting and AI

**A — Commercial Prospecting (Démarchage commercial)**

French law supplements ePrivacy with specific rules on unsolicited communications:

| Channel           | B2C                                                                                                               | B2B (professional addresses)                                     |
| ----------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Email             | Prior opt-in consent required (past customer exception: existing relationship for similar products — soft opt-in) | Legitimate interest; professional must be able to opt out easily |
| SMS/text          | Prior opt-in consent required                                                                                     | Prior opt-in generally required                                  |
| Phone calls       | Bloctel cold-call registry must be checked; individual must not be listed                                         | Legitimate interest; opt-out must be respected                   |
| Phone auto-dialer | Prohibited for B2C without consent                                                                                | Restricted                                                       |

- [ ] B2C email campaigns: documented opt-in consent obtained at collection point
- [ ] Bloctel registry checked before phone outreach campaigns
- [ ] Opt-out/unsubscribe honored immediately; suppression list maintained and clean
- [ ] Data broker lists: consent chain verified (did data subjects consent to transfer for direct marketing?)
- [ ] "Soft opt-in" exception: limited to existing customers, similar products/services, clearly offered opt-out at collection point

**B — AI and Automated Decision-Making**

**GDPR Article 22 / Article 10 LIL:**

- Data subjects have the right NOT to be subject to solely automated decisions with legal or similarly significant effects
- Exceptions: (a) necessary for contract, (b) authorized by EU/French law with appropriate safeguards, (c) explicit consent
- Where an exception applies: individual must be informed; right to obtain human review; right to express view; right to contest the decision
- **Article 10 LIL adds**: Individuals must be informed of profiling that **contributed to** a decision, even if not solely automated — this is stricter than GDPR Article 22

**AI assessment:**

- [ ] AI systems using personal data inventoried
- [ ] Article 22 assessment: does any AI produce solely automated decisions with significant effects?
- [ ] If yes: valid exception documented; human review procedure in place
- [ ] Privacy notices explain: existence of automated processing, logic involved, significance of outcome
- [ ] DPIA completed for AI systems meeting multiple CNIL risk criteria
- [ ] CSE consulted for AI systems affecting employment decisions (French labor law requirement)
- [ ] CNIL AI guidance series 2024-2026 reviewed and applied where relevant [VERIFY current guidance]

---

## Compliance Classification

### COMPLIANT — No Action Required

The organization meets the applicable CNIL and LIL requirements for this element. Minor
process improvements may be noted but do not affect compliance status.

**Indicators:**

- Documented procedures in place and followed in practice
- Evidence of compliance available (logs, records, policies)
- No recent CNIL enforcement decisions on this element for similar organizations

**Action:** Note for awareness. No remediation required.

---

### PARTIAL — Remediation Required (Non-Critical)

The organization has compliance measures in place but they are incomplete, outdated, or
not consistently applied. Risk of CNIL sanction is moderate.

**Indicators:**

- Documentation exists but not current or not covering all processing
- Procedures exist but are not consistently followed
- Gap between policy and practice (e.g., retention periods set but not enforced in systems)
- Missing components of an otherwise functional program

**Action:** Identify specific gaps. Provide concrete remediation steps with deadline.

---

### NON-COMPLIANT — Significant Gap

The organization lacks a required compliance element or has a material deviation from
CNIL requirements. CNIL contrôle or complaint in this area would likely result in a
mise en demeure or sanction.

**Indicators:**

- Required element entirely absent (no DPIA for mandatory processing, no DPO registration)
- Active violation of CNIL guidance (cookie tracker deposited before consent)
- Recent CNIL enforcement decisions in this area for similar violations

**Action:** Provide specific remediation steps with urgent timeline (typically 30-60 days).
Self-interrogation applied to confirm classification.

---

### CRITICAL DEFICIENCY — Immediate Action Required

A fundamental compliance failure that creates significant legal risk and/or potential
for CNIL emergency intervention. Requires immediate escalation and remediation.

**Indicators:**

- Health data processing without CNIL authorization — **processing must stop** until
  authorization obtained
- Large-scale processing of personal data without any DPIA (on CNIL mandatory list)
- Prior CNIL mise en demeure on the same issue not remediated within the deadline
- Active data breach without CNIL notification beyond the 72-hour window
- Continuous, unjustified employee monitoring constituting permanent surveillance
- Processing of under-15 data without parental consent in an information society service
- Prior sanction and continued same violation

**Action:** Escalate immediately. Provide concrete stop/remediate/notify steps. Apply
3-pass Self-Interrogation before confirming classification. Consider consulting qualified
French legal counsel immediately.

---

## Prioritization Framework

Organize remediation findings into three tiers:

### Tier 1 — Immediate (0–30 days)

Issues that require immediate action due to legal risk, regulatory urgency, or ongoing harm:

- Any CRITICAL DEFICIENCY finding
- Active CNIL contrôle notice: prepare documents, close outstanding gaps
- Cookie banner lacking a reject button (CNIL's highest enforcement category in 2025 with 21 sanctions)
- Ongoing data breach requiring 72-hour CNIL notification
- DPO not registered with CNIL when designation is required
- Health data processing without CNIL authorization

### Tier 2 — Near-Term (30–90 days)

Material compliance gaps with significant enforcement risk:

- Cookie analytics tool without valid exemption or consent
- Missing DPAs with processors handling significant personal data
- DPIA required by CNIL mandatory list but not completed
- Employee monitoring implemented without CSE consultation
- B2C marketing without documented opt-in consent
- Processing register incomplete or significantly outdated
- Third-country transfers without valid transfer mechanism

### Tier 3 — Planned (90–180 days)

Process improvements and completeness measures:

- Processing register refinement (add legal basis, TIA columns, DPIA references)
- Rights request procedure formalization (templates, response tracking)
- DPO resource adequacy review
- Retention period enforcement verification across all systems
- Privacy notice updates to reflect current processing
- Annual transfer impact assessment reviews for SCC-based transfers
- Post-mortem directive procedure (if not yet in place)
- Bloctel registry integration for phone marketing

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output. Revise failures before delivery.

| Gate           | Rule                                                                                                                       | Fail Action                                                               |
| -------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific LIL article, CNIL guideline, GDPR provision, or established principle                   | Add citation or mark "[UNVERIFIED — verify on Légifrance / CNIL website]" |
| **Format**     | All citations follow a recognizable format (e.g., "Article 82 LIL", "GDPR Article 35", "CNIL Délibération SAN-2022-XXX")   | Fix format                                                                |
| **Currency**   | Cited provisions checked for amendments; CNIL guidelines checked for superseding guidance                                  | Flag "[CHECK CURRENCY — may have been updated]"                           |
| **Domain**     | Analysis stays within French/CNIL law. No assumptions from other data protection regimes (CCPA, UK GDPR, etc.) bleeding in | Remove or flag cross-regime bleed                                         |
| **Confidence** | Uncertainty explicitly stated, not hidden. If unsure of CNIL's current position, say so                                    | Add confidence qualifier                                                  |

### Self-Interrogation for CRITICAL DEFICIENCY Items

For any CRITICAL DEFICIENCY finding, apply this 3-pass self-interrogation before delivering:

**Pass 1 — Legal Chain Integrity:**

- Does the CRITICAL classification follow logically from the cited CNIL authority?
- Would CNIL's formation restreinte actually reach this conclusion on these facts?
- Is there a counter-argument available (e.g., sector-specific exemption, transitional period)?

**Pass 2 — Completeness:**

- Have all relevant CNIL guidelines, LIL articles, and GDPR provisions been considered?
- Is there a CNIL référentiel or sectoral guidance that might authorize or moderate this issue?
- Have any recent CNIL enforcement decisions on similar facts been considered?

**Pass 3 — Challenge:**

- What is the strongest argument that this is NON-COMPLIANT rather than CRITICAL DEFICIENCY?
- Under what circumstances might CNIL issue only a mise en demeure rather than a sanction?
- Is the organization aware of and actively remediating the issue? (Mitigates sanction risk)

Mark audit trail: `self_interrogation: PASS` or `self_interrogation: REVISED`.

### Confidence Scoring

| Level         | Range     | Meaning                                                                     | Action                                                            |
| ------------- | --------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Définitif** | 0.95–1.0  | Settled CNIL requirement; clear article or binding règlement-type           | State with confidence                                             |
| **Élevé**     | 0.80–0.94 | Strong CNIL guidance; minor interpretation questions                        | State with brief caveat                                           |
| **Probable**  | 0.60–0.79 | Reasonable interpretation of CNIL position; CNIL enforcement trend supports | State with explicit reasoning and contra-indicators               |
| **Possible**  | 0.40–0.59 | Genuinely uncertain; CNIL guidance not specific to this scenario            | Flag for counsel review with both sides                           |
| **Incertain** | 0.0–0.39  | Weak basis; speculative                                                     | Do not assert; flag "[INCERTAIN — conseil juridique à consulter]" |

---

## Glass Box Audit Trail

Every CNIL compliance assessment MUST include this audit section:

```yaml
glass_box:
  skill_name: "legalcode-fr-cnil-privacy-compliance"
  organization: "[Organization name or description]"
  assessment_date: "[date]"
  assessment_trigger: "[Annual review / CNIL contrôle / M&A due diligence / Other]"
  jurisdiction: "France — Loi Informatique et Libertés + GDPR"
  assessment_scope: "[Full 10-domain / Targeted: specify domains assessed]"
  domains_assessed: "[Number] / 10"
  legalcode_mcp: "Connected / Not connected"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "Loi n°78-17 du 6 janvier 1978 modifiée (LIL) — [VERIFIED / UNVERIFIED]"
    - "GDPR Regulation (EU) 2016/679 — [VERIFIED / UNVERIFIED]"
    - "CNIL Lignes directrices cookies (17 sept. 2020) — [VERIFIED / UNVERIFIED]"
    - "[Additional citations as relevant]"
  enforcement_cases_reviewed:
    - "[Case reference, year, relevance — VERIFIED / UNVERIFIED]"
  french_derogations_assessed:
    - "Age of consent (15 years): [assessed / N/A]"
    - "Cookie refusal mechanism: [assessed / N/A]"
    - "DPO CNIL registration: [assessed / N/A]"
    - "Employee monitoring / CSE consultation: [assessed / N/A]"
    - "DPIA mandatory list: [assessed / N/A]"
    - "Post-mortem data rights: [assessed / N/A]"
    - "NIR processing: [assessed / N/A]"
    - "Health data authorization: [assessed / N/A]"
    - "Commercial prospecting (Bloctel): [assessed / N/A]"
  findings_summary:
    critical_deficiency: "[number]"
    non_compliant: "[number]"
    partial: "[number]"
    compliant: "[number]"
  self_interrogation: "PASS / REVISED / NOT APPLICABLE (no CRITICAL DEFICIENCY items)"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "[Scope limitations: description-based assessment, specific domains not assessed, etc.]"
    - "[Currency: CNIL guidance verified as of [date]; check for subsequent updates]"
    - "[Documentation: assessment based on [provided documents / description only]]"
  reviewer: "AI-assisted — requires qualified French legal professional or CNIL-registered DPO review"
```

---

## Anti-Patterns

Explicit catalogue of what NOT to do in CNIL compliance work:

1. **Treating generic GDPR compliance as sufficient** — France's LIL adds significant obligations (15-year age threshold, DPO CNIL registration, cookie refusal UI requirements, CSE consultation, NIR authorization). Organizations compliant elsewhere in the EU are not automatically compliant in France.

2. **Using silence as GDPR consent for cookies** — Article 82 LIL is stricter than GDPR: continued browsing does NOT constitute consent. "Silence = refusal" is the French rule. Any banner that interprets inaction as acceptance violates Article 82 LIL.

3. **One-click accept, multi-click refuse** — The single biggest CNIL cookie enforcement trigger (Google, Meta, Microsoft all sanctioned on this). The reject button must be as prominent and accessible as the accept button. Any asymmetry in design is a dark pattern that CNIL will target.

4. **Claiming analytics cookie exemption without meeting all 7 conditions** — The analytics exemption is narrow and easily lost. A tool that aggregates data with a third party, cross-links across sites, or uses non-anonymized data does not qualify. Google Analytics in its standard configuration does NOT meet the exemption conditions.

5. **Implementing employee monitoring without CSE consultation** — This is a French labor law violation independent of GDPR. Organizations implementing new monitoring systems (cameras, GPS, email monitoring, HR AI tools) without prior CSE consultation commit two violations simultaneously. This includes remote monitoring tools introduced since 2020 without appropriate governance.

6. **DPO conflicts of interest** — Designating a DPO who is also the IT Director, CISO, HR Director, General Counsel with line management, CFO, or CEO creates a GDPR Article 38(6) conflict. CNIL enforcement has targeted organizations where the DPO cannot exercise independence. The DPO role is distinct and must report to the highest management level.

7. **Forgetting to register the DPO with CNIL** — Unlike most EU states, CNIL requires formal online registration via connexion.pro.cnil.fr. An unregistered DPO is effectively invisible to CNIL. Organizations believing they have designated a DPO without CNIL registration have completed only half the requirement. Shared group DPOs must list all covered entities in their CNIL registration.

8. **Processing health data without CNIL authorization** — Health data in France is not just special category data under Article 9 GDPR; specific processing requires CNIL authorization (health data warehouses) or conformity with a référentiel. Processing health data without authorization is a CRITICAL DEFICIENCY. The Cegedim Santé sanction (€800,000, 2024) demonstrated CNIL's willingness to enforce this.

9. **Conducting DPIA after processing begins** — A DPIA is a **prior** obligation (GDPR Article 35(1): "prior to the processing"). Conducting it post-hoc does not satisfy the requirement. Organizations that begin processing on the CNIL mandatory list before completing a DPIA have committed a non-compliance that cannot be entirely remediated retroactively.

10. **Using pre-2021 Standard Contractual Clauses** — The European Commission's June 2021 SCCs replaced the 2001/2004 versions. The old SCCs ceased to be valid for new contracts after December 2022. Organizations still relying on the old format for ongoing transfers have an invalid transfer mechanism and are effectively conducting unlawful third-country transfers.

11. **Missing the Transfer Impact Assessment** — Using 2021 SCCs without a Transfer Impact Assessment (TIA/AITD) for transfers to countries with significant surveillance law concerns (including the US for non-DPF entities, Russia, China) is non-compliant. Uber's €290 million sanction (Dutch DPA, 2024) demonstrated that merely having SCCs in place is insufficient without evaluating whether they provide effective protection.

12. **Processing the NIR (numéro de sécurité sociale) without authorization** — Article 22 LIL makes NIR processing strictly controlled. Only authorized entities may process this number. Including NIR in a standard employee record, HR database, or insurance system without verifying that the organization is on the authorized list is a compliance violation.

13. **Children's data without parental consent** — Article 7-1 LIL sets France's digital age of consent at 15, lower than most EU states. Online services targeting children or knowingly accepting under-15 users without implementing parental consent are non-compliant. "Date of birth" age gates without meaningful verification are insufficient.

14. **B2C marketing without prior opt-in** — French rules are stricter than some EU interpretations of ePrivacy for B2C marketing: prior affirmative consent is required for email and SMS marketing (except the narrow existing customer soft opt-in). Purchasing lists from data brokers without verifying consent chains does not satisfy this.

15. **Non-cooperation with CNIL** — CNIL issued 14 sanctions in 2025 for non-cooperation alone. Failing to respond to CNIL questionnaires, documentary control requests, or inspection notices is itself a violation. Organizations that receive any CNIL correspondence must respond promptly and completely.

16. **Ignoring the Article 10 LIL automated decision transparency requirement** — Article 10 LIL goes further than GDPR Article 22 by requiring individuals to be informed of profiling that contributed to (but did not solely determine) a decision. Organizations using ML models, scoring, or algorithms to assist human decisions must disclose this in their privacy notices, not just when the decision is fully automated.

17. **Post-mortem data rights as an afterthought** — Articles 84-86 LIL create a French legal framework for data subjects' instructions about their data after death, and for heirs to exercise certain rights. Organizations without any process for receiving and implementing post-mortem directives are technically non-compliant with a uniquely French requirement.

18. **Assuming the enforcement risk is low because the organization is small** — CNIL's simplified procedure allows sanctions up to €20,000 for smaller entities with straightforward violations. The 2025 statistics show 67 of 83 sanctions used the simplified procedure. Small businesses are not immune — they face lower maximum fines, but the process is faster and CNIL's complaint-driven workflow reaches all sizes.

---

## Writing Standards

Apply plain-language discipline to all assessment output:

**For executive summaries and remediation recommendations (shared with non-legal stakeholders):**

- Plain language; avoid GDPR/CNIL jargon without explanation
- Active voice: "CNIL requires prior consent" not "Prior consent is required by CNIL"
- Short sentences; one point per sentence
- Quantify where possible: "21 of 83 CNIL sanctions in 2025 involved cookies"
- Name the action required: "Update the cookie banner to add a 'Refuse all' button as prominent as 'Accept all'"

**For legal analysis sections (shared with DPO or legal counsel):**

- Same plain-language standards
- Include specific LIL article, CNIL decision, or GDPR provision
- State confidence qualifiers explicitly
- Flag [VERIFY] for any citation not confirmed against authoritative source

**Quality gates before delivery:**

1. Can a non-privacy-specialist business stakeholder understand the executive summary and top 3 findings?
2. Is every legal claim backed by a specific citation (or flagged [VERIFY])?
3. Is every remediation step specific and actionable (who, what, by when)?
4. Are any phrases vague, hedging, or ambiguous? If yes, fix.
5. Could any sentence be shorter without losing meaning? If yes, shorten.

---

## External Tool Integration

**With legalcode-mcp connected (preferred):**

- In Step 3, search for current CNIL guidance, recent sanctions, and sector-specific référentiels
- Save results to `/tmp/legalcode-cnil-assessment-authority.md`
- Verify statutory references against current LIL text (Légifrance)
- Search for CNIL's latest annual statistics and enforcement priorities
- Check whether the organization's sector appears on CNIL's current year inspection priorities
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp:**

- Mark all CNIL guidance and LIL article references with [VERIFY]
- Note in the Glass Box: `legalcode_mcp: "Not connected — all citations require verification on Légifrance and www.cnil.fr"`
- Focus the assessment on structural gaps and process compliance rather than legal authority depth
- Provide the following verification checklist to the user alongside the assessment:
  ```
  Verification checklist — check these on www.cnil.fr and Légifrance:
  □ Current CNIL cookie guidelines (confirm Délibération 17 sept. 2020 still in force)
  □ Current mandatory DPIA list (confirm against CNIL's published PDF)
  □ Current DPO registration portal URL and requirements
  □ Current CNIL sectoral référentiels relevant to this organization's sector
  □ Latest CNIL annual enforcement statistics
  □ Current EDPB coordinated enforcement priorities
  ```

---

## Output Format Template

Structure the final CNIL compliance assessment as:

```markdown
## CNIL Privacy Compliance Assessment

**Organization**: [name or description]
**Assessment Date**: [date]
**Assessment Trigger**: [Annual review / CNIL contrôle / M&A / etc.]
**Assessment Scope**: [Full 10-domain / Targeted domains]
**Assessment Basis**: [Full documentation / Partial documentation / Description only]

---

## Executive Summary

[3-5 sentences: overall compliance posture, highest-priority findings, immediate actions required]

**Overall risk level**: HIGH / MEDIUM / LOW — [brief rationale]

---

## Critical Deficiencies — Immediate Action Required

[If any CRITICAL DEFICIENCY findings — list here with one-line description and
link to Domain finding below. Empty section if none.]

---

## Domain-by-Domain Findings

### Domain 1: Governance Foundations — [COMPLIANT / PARTIAL / NON-COMPLIANT / CRITICAL DEFICIENCY]

**Finding**: [Summary of compliance status]
**Specific gaps**: [Bulleted list of gaps found]
**Remediation**: [Specific actions required]
**Priority**: [Tier 1 / 2 / 3]
**Confidence**: [Définitif / Élevé / Probable / Possible / Incertain]

[Repeat for each domain assessed]

---

## Remediation Roadmap

### Tier 1 — Immediate (0–30 days)

| Action   | Owner  | Deadline | Finding Reference |
| -------- | ------ | -------- | ----------------- |
| [action] | [role] | [date]   | [Domain X]        |

### Tier 2 — Near-Term (30–90 days)

[Same table format]

### Tier 3 — Planned (90–180 days)

[Same table format]

---

## French-Specific Derogation Status

| French Derogation                        | Status                                      | Notes |
| ---------------------------------------- | ------------------------------------------- | ----- |
| Age of consent (15 years)                | [COMPLIANT / PARTIAL / NON-COMPLIANT / N/A] |       |
| Cookie refusal UI ("refus aussi facile") | [status]                                    |       |
| DPO CNIL registration                    | [status]                                    |       |
| CSE consultation for monitoring          | [status]                                    |       |
| DPIA mandatory list compliance           | [status]                                    |       |
| NIR authorization                        | [status]                                    |       |
| Health data authorization                | [status]                                    |       |
| Post-mortem directives                   | [status]                                    |       |
| Commercial prospecting (Bloctel)         | [status]                                    |       |

---

## Enforcement Exposure Calibration

[Assess potential CNIL enforcement exposure based on findings:

- Most likely CNIL response (reminder / mise en demeure / simplified sanction / ordinary procedure)
- Comparable enforcement cases from CNIL's published decisions
- Estimated sanction range if non-compliant items were subject to enforcement]

---

## Next Steps

1. [Immediate action] — Owner: [role] — Deadline: [date]
2. [Second action] — Owner: [role] — Deadline: [date]
   [...]

---

[Glass Box Audit Trail — YAML format as per Quality Assurance Framework section]
```

---

## Localization Notes

**French Territories and DOM-COM:**

- GDPR and the LIL apply to all French metropolitan territory and DOM (Départements d'Outre-Mer: Guadeloupe, Martinique, Guyane, La Réunion, Mayotte) [VERIFY current application to all DOM-COM territories]
- French Polynesia, New Caledonia, and other COM have different regulatory status — GDPR may not apply directly; French laws apply with modifications. [VERIFY applicable data protection framework for specific COM territory]

**Bilingual assessments:**

- CNIL guidance and the LIL are in French. Key terms used in this skill with French originals:
  - Délégué à la Protection des Données (DPD) = Data Protection Officer (DPO)
  - Registre des Activités de Traitement = Record of Processing Activities
  - Analyse d'Impact relative à la Protection des Données (AIPD) = Data Protection Impact Assessment (DPIA)
  - Responsable de traitement = Data Controller
  - Sous-traitant = Data Processor
  - Consentement = Consent
  - Base légale = Legal Basis
  - Mise en demeure = Formal compliance notice
  - Formation restreinte = Restricted sanctioning body
  - Contrôle = Inspection

**Related Legalcode skills:**

- `legalcode-fr-sapin-ii-compliance` — Anti-corruption compliance including GDPR interaction
- `legalcode-fr-contrat-de-travail-cdi` — Employment contracts including CNIL employee data guidance
- `legalcode-legitimate-interest-assessment` — GDPR Article 6(1)(f) legitimate interest balancing test
- `legalcode-whistleblower-program-builder` — CNIL whistleblowing system DPIA requirements (Sapin II)
- `gdpr-data-processing-addendum` — EU Article 28 DPA template

---

## Provenance

Created by Legalcode (2026-03-21). Original synthesis based on:

- Loi n°78-17 du 6 janvier 1978 modifiée (Loi Informatique et Libertés) — Légifrance
- GDPR Regulation (EU) 2016/679 — EUR-Lex
- CNIL Lignes directrices cookies et autres traceurs (17 septembre 2020) — www.cnil.fr
- CNIL Recommandation relative aux cookies et autres traceurs (1er octobre 2020)
- CNIL annual enforcement statistics 2023-2025 — www.cnil.fr/fr/bilan-sanctions
- CNIL mandatory DPIA list — www.cnil.fr/sites/cnil/files/atoms/files/liste-traitements-aipd-requise.pdf
- CNIL Règlement Type Biométrie (28 mars 2019)
- Code du travail Articles L.1222-4, L.2312-8, L.2312-37 — Légifrance
- Code pénal Articles 226-16 à 226-24 — Légifrance
- Enforcement decisions: Google SAN-2022-001 (€150M), Facebook SAN-2022-002 (€60M), Microsoft SAN-2023-XXX (€60M), Orange (€50M, Nov 2024), Google (€325M, Sept 2025), Shein (€150M, Sept 2025)
- CNIL reference frameworks (référentiels) and cadres de référence — www.cnil.fr/fr/les-cadres-de-reference
- Legalcode 2-agent research pipeline methodology
- Reference skill: `legalcode-fr-sapin-ii-compliance` (structural benchmark for France compliance skills)
- Reference standard: `legalcode-contract-review` (quality framework benchmark)

All statutory and enforcement citations should be verified against current sources on Légifrance and www.cnil.fr before use in legal proceedings or formal compliance documentation.
