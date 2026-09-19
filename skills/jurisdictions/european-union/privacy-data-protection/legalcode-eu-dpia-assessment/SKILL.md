---
name: legalcode-eu-dpia-assessment
description: Perform EU Data Protection Impact Assessments (DPIAs) under GDPR Article 35, EDPB Guidelines
  WP 248 rev.01, EDPB Opinion 28/2024 (AI/ML systems), EDPB Guidelines 01/2025 (Pseudonymisation), and
  national supervisory authority (SA) blacklists.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.

## Full scope from the source skill

Perform EU Data Protection Impact Assessments (DPIAs) under GDPR Article 35, EDPB Guidelines WP 248 rev.01, EDPB Opinion 28/2024 (AI/ML systems), EDPB Guidelines 01/2025 (Pseudonymisation), and national supervisory authority (SA) blacklists. Triggers on: "DPIA", "DSFA", "Datenschutz-Folgenabschätzung", "évaluation d'impact", "AIPD", "Data Protection Impact Assessment", "impact assessment", "Art. 35", "Art. 36", "do I need a DPIA", "high-risk processing", profiling, AI systems, biometrics, special categories of data, large-scale monitoring, employee surveillance, connected vehicles, smart cities, genetic data, prior consultation questions, Art. 36 submission preparation, and any vendor or processor involvement in high-risk processing. Covers: threshold assessment (Art. 35(3) mandatory triggers + nine EDPB criteria + multi-jurisdictional national blacklist analysis), systematic description (Art. 35(7)(a)), necessity and proportionality (Art. 35(7)(b)), risk assessment with 5×5 scoring matrix (Art. 35(7)(c)), mitigation measures (Art. 35(7)(d)), residual risk framing, Art. 36 prior consultation threshold and package preparation, DPO involvement (Art. 35(2)), data subject consultation (Art. 35(9)), AI/ML dual-phase DPIA per EDPB Opinion 28/2024, AI Act FRIA interaction, vendor and processor DPIA obligations (Art. 28), and authority-facing documentation standards. EU/EEA-specific with national SA coverage for Germany (DSK), France (CNIL), Netherlands (AP), Ireland (DPC), Belgium (APD), Italy (Garante), and Poland (UODO). Use as the native Legalcode DPIA assessment workflow, replacing any imported DPIA tooling.


# Legalcode EU DPIA Assessment

> **Disclaimer**: This skill provides a framework for AI-assisted DPIA analysis under
> GDPR Article 35 and EDPB guidance. It does not constitute legal advice. Involve your
> DPO (Art. 35(2)) and qualified privacy counsel for final decisions on high-risk
> processing. All legal references cited from memory carry hallucination risk — verify
> against EUR-Lex, EDPB publications, and your national SA's website before relying on
> them. Laws, guidelines, and enforcement posture change; check currency before use.

---

## Purpose and Scope

This skill produces a complete DPIA assessment package for processing activities that
may create high risk to the rights and freedoms of natural persons under GDPR Article 35.

**Covers:**

- Threshold determination: whether a DPIA is required, recommended, or not needed
- Art. 35(3) mandatory trigger analysis (three absolute cases)
- Nine-criteria EDPB analysis per WP 248 rev.01
- Multi-jurisdictional national SA blacklist and whitelist checks
- Threshold Justification Memo (for negative determinations, Art. 5(2) accountability)
- Systematic description of processing (Art. 35(7)(a))
- Necessity and proportionality assessment (Art. 35(7)(b))
- Risk identification and 5×5 scoring from the data subject's perspective (Art. 35(7)(c))
- AI/ML dual-phase analysis per EDPB Opinion 28/2024
- Mitigation measures with pre/post scoring (Art. 35(7)(d))
- Residual risk determination and Art. 36 prior consultation threshold check
- DPO involvement documentation (Art. 35(2))
- Vendor and processor DPIA obligations under Art. 28
- AI Act FRIA vs. GDPR DPIA interaction
- Authority-facing documentation: full DPIA report, Art. 36 consultation package,
  executive summary, and threshold memo

**Does not:**

- Provide legal advice or replace DPO or qualified privacy counsel
- Guarantee regulatory approval or SA non-intervention
- Substitute for security penetration testing or technical security assessments
- Cover UK GDPR specifically (shares the GDPR framework but has ICO-specific nuances;
  adapt for UK with ICO guidance and Article 35/36 ICO lists)
- Cover US, Canadian, or other non-EU/EEA privacy regime DPIAs

---

## Jurisdiction and Governing Law

**Primary jurisdiction:** European Union and EEA Member States.

**Governing instruments:**

- Regulation (EU) 2016/679 (GDPR) — Arts. 35–36 (DPIA and prior consultation),
  Art. 5(2) (accountability), Art. 9 (special categories), Art. 22 (automated
  decision-making), Art. 25 (data protection by design and by default), Art. 28
  (processor obligations), Art. 30 (records of processing activities)
- EDPB Guidelines on DPIA, WP 248 rev.01 (adopted 4 April 2017, revised 4 October
  2017, endorsed by EDPB Endorsement 1/2018) [VERIFY currency]
- EDPB Opinion 28/2024 on AI models [VERIFY currency — adopted October 2024]
- EDPB Guidelines 01/2025 on Pseudonymisation (adopted 17 January 2025) [VERIFY]
- EDPB Guidelines 3/2019 on processing of personal data through video devices [VERIFY]
- EDPB Guidelines 1/2020 on connected vehicles and mobility data [VERIFY]
- National SA Art. 35(4) blacklists: Germany (DSK), France (CNIL), Netherlands (AP),
  Ireland (DPC), Belgium (APD), Italy (Garante), Poland (UODO) — see **National
  Blacklist Reference** section
- Regulation (EU) 2024/1689 (AI Act) — for FRIA obligations alongside DPIA

**DPIA obligation geography:** The DPIA obligation follows the nature of the processing,
not the controller's location. Check blacklists for every jurisdiction where the
controller has an establishment, where data subjects are located, or where processing
physically takes place. The one-stop-shop (Art. 56) governs enforcement jurisdiction —
it does NOT limit which Art. 35(4) blacklists apply.

---

## Interactive Clarification

This skill uses **⟁ CLARIFY** at key decision points. Rather than assuming intent,
the workflow pauses when:

- The answer would change the threshold verdict or risk classification
- Multiple valid approaches exist (mode selection, scope)
- Processing details are ambiguous and the ambiguity is material to outcome
- Risk tolerance decisions need to be made explicit

Present options as structured choices with descriptions. If the user has already provided
the information, skip the question. For batch/automated runs, use reasonable defaults and
state assumptions explicitly.

---

## Workflow

### Step 1: Mode Selection

**⟁ CLARIFY** — Identify which mode the user needs:

| Mode                                 | When to Use                                                                               | Output                                                        |
| ------------------------------------ | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **A — Threshold Assessment**         | "Do I need a DPIA?" — quickly determine whether to run one                                | Threshold verdict with reasoning and national blacklist check |
| **B — Full DPIA**                    | Threshold confirmed or assumed; conduct complete DPIA                                     | Full DPIA report (all seven Art. 35(7) elements)              |
| **C — Threshold Negative Memo**      | Processing assessed as low-risk; document Art. 5(2) accountability                        | Formal memo documenting why DPIA is not required              |
| **D — Art. 36 Consultation Package** | DPIA concluded with very high residual risk; prepare SA submission                        | Art. 36(3) compliant consultation package                     |
| **E — DPIA Review and Update**       | Existing DPIA needs refreshing (material change, new technology, 12-month review trigger) | Annotated gap analysis + updated sections                     |

If the user describes new processing or a proposed feature, assume **Mode A** (threshold)
first, then proceed to Mode B if required.

### Step 2: Gather Processing Context

**⟁ CLARIFY** — Collect the following before proceeding. Present as a structured
questionnaire; accept partial answers and state what is assumed.

**2a. Processing overview:**

- What is the processing activity's name and purpose?
- What categories of personal data are involved? (Basic contact, behavioral, location,
  health, biometric, genetic, financial, criminal, other)
- Who are the data subjects? (Employees, customers, children, patients, public, other)
- Approximate number of data subjects (or range: <1,000 / 1,000–100,000 / >100,000)?
- How is data collected, and from what sources?
- What technology or systems are used? (AI/ML, biometrics, surveillance, IoT, etc.)

**2b. Controller and jurisdiction:**

- Controller name and main EU establishment (for lead SA determination)
- All EU/EEA Member States where the controller has an establishment involved in this
  processing
- All EU/EEA Member States where data subjects are located
- Any third-country transfers involved?

**2c. Processing characteristics:**

- Processing purpose — is this an existing activity (review/update) or a new one?
- Are processors or sub-processors involved? If so, which?
- Does the processing involve automated decisions? If so, do they have legal or similarly
  significant effects on data subjects?
- Is this processing novel (new technology, new combination of existing systems)?
- Has a DPIA already been conducted? If so, when and what were its conclusions?

**2d. DPO involvement:**

- Does the controller have a mandatory or voluntary DPO?
- Has the DPO been consulted at this stage?

**⟁ CLARIFY** — If any of the following are described, flag immediately and confirm
before proceeding:

- Processing of Art. 9 special category data (health, biometric, genetic, race, etc.)
- Automated profiling producing legal or similarly significant effects (Art. 22)
- Surveillance of publicly accessible areas (video, location tracking, sensor networks)
- AI/ML model training or deployment on personal data

### Step 3: Gather Legal Authority via legalcode-mcp

Search **legalcode-mcp** for the specific processing context:

- National SA blacklist entries for all relevant jurisdictions
- Sector-specific SA guidance (employment monitoring guidelines, health sector rules)
- Recent enforcement decisions related to the processing type
- Applicable EDPB opinions and guidelines

Save results to `/tmp/legalcode-dpia-authority.md`. Structure as:

```
# DPIA Legal Authority — [Processing Activity Name]
## Date: [date]
## Relevant Jurisdictions: [list]

### Applicable EDPB Guidance
[guideline, adoption date, relevance]

### National SA Blacklist Entries
[SA, blacklist entry, match assessment]

### Recent Enforcement
[case, date, fine, relevance]

### Sector-Specific Guidance
[guidance, SA, relevance]
```

**If legalcode-mcp is not connected:** Proceed using the National Blacklist Reference
and EDPB guidance in this skill. Mark all blacklist matches as [VERIFY — check current
SA list] and note in the Glass Box: `legalcode_mcp: "Not connected"`.

### Step 4: Threshold Assessment

Run in this sequence. Stop at the first positive finding.

#### 4a. Art. 35(3) Mandatory Triggers

Check all three. Each is an absolute requirement — no balancing test, no discretion.
If any applies, the verdict is DPIA REQUIRED.

**Trigger (a): Systematic and extensive evaluation of personal aspects**
Based on automated processing, including profiling, on which decisions are based that
produce legal effects concerning natural persons or similarly significantly affect them.

- Applies to: credit scoring, algorithmic hiring, insurance pricing, AML risk profiling,
  recidivism prediction, benefits eligibility decisions
- Threshold: both "systematic and extensive" (not one-off) AND legal/significant effects
- "Legal effects" = denial of citizenship, benefits, credit, border entry
- "Similarly significant effects" = credit denial, insurance refusal, access to essential
  services

**Trigger (b): Large-scale processing of special categories (Art. 9(1)) or criminal data (Art. 10)**

- Art. 9 categories: racial/ethnic origin, political opinions, religious/philosophical
  beliefs, trade union membership, genetic data, biometric data processed for unique
  identification, health data, sex life or sexual orientation
- Art. 10: criminal convictions and offences
- "Large scale" uses four factors: number of data subjects, volume of data, duration,
  geographic extent. A single doctor's records = not large scale. A hospital system = large scale.
  No fixed numerical threshold exists.

**Trigger (c): Systematic monitoring of a publicly accessible area on a large scale**

- Covers: city-wide CCTV, drone surveillance, public Wi-Fi/Bluetooth tracking, smart
  city sensor networks, facial recognition in public spaces
- "Publicly accessible" includes privately owned spaces open to the public (shopping
  malls, transport hubs)
- "Systematic" = pre-arranged, organized, methodical, continuous or at regular intervals

**Output for 4a:** Present a table: Trigger | Applies? (YES/NO) | Reasoning

#### 4b. Nine-Criteria EDPB Analysis (WP 248 rev.01)

Assess all nine criteria. Document the finding for each.

| #   | Criterion                                                                                                                                                                                                                                                    | Applies? | Reasoning |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- | --------- |
| 1   | **Evaluation or Scoring** — Profiling and predicting aspects of data subjects (performance, economic situation, health, behavior, preferences, location)                                                                                                     | —        | —         |
| 2   | **Automated Decision-Making with Legal/Significant Effect** — Art. 22 alignment; "rubber-stamp" human review counts as automated                                                                                                                             | —        | —         |
| 3   | **Systematic Monitoring** — Pre-arranged, organized, continuous observation (CCTV, email monitoring, GPS tracking, behavioral tracking, IoT)                                                                                                                 | —        | —         |
| 4   | **Sensitive Data or Highly Personal Data** — Art. 9/10 categories plus financial data, continuous location, private communications, browsing/search history, smart home data, data from which Art. 9 can be inferred                                         | —        | —         |
| 5   | **Large-Scale Data Processing** — Apply four-factor test: number of subjects, data volume, duration, geographic extent                                                                                                                                       | —        | —         |
| 6   | **Matching or Combining Datasets** — Data from two or more processing operations for different purposes and/or by different controllers; cross-service data integration; AI training from multiple sources                                                   | —        | —         |
| 7   | **Vulnerable Data Subjects** — Children (under 18), employees, elderly, patients, persons with disabilities, asylum seekers, persons with mental health conditions. Note: "consent" is generally unreliable where vulnerability exists                       | —        | —         |
| 8   | **Innovative Use or New Technological Solutions** — Novel tech or familiar tech in novel context where consequences are not well-understood: generative AI/LLMs, real-time facial recognition, BCIs, blockchain for personal data, emotion AI, digital twins | —        | —         |
| 9   | **Prevents Exercising a Right or Service** — Processing aimed at determining access to services or contracts: bank account screening, algorithmic service access, shared blacklists, platform bans with significant consequences                             | —        | —         |

**Applying the two-criteria rule:**

- **2+ criteria met:** Strong presumption DPIA is required. Document thoroughly if
  proceeding without one; justification must be retained (Art. 5(2)).
- **Exactly 1 criterion:** DPIA recommended but not presumptively required. Assess
  how strongly it applies and whether any national blacklist entry applies.
- **0 criteria:** DPIA likely not required; still check national blacklists.
- **Best practice:** When in doubt, conduct the DPIA. Cost of an unnecessary DPIA is
  low; cost of a missing one: up to €10M or 2% global turnover (Art. 83(4)(a)).

#### 4c. National Blacklist Analysis

**For each relevant jurisdiction,** check the Art. 35(4) national list. A blacklist match
in **any** relevant jurisdiction triggers a DPIA for that processing.

**⟁ CLARIFY** — Identify all relevant jurisdictions:

- Where does the controller have an establishment involved in this processing?
- Where are data subjects located?
- Where does processing physically take place (servers, devices, cameras)?

**Key blacklist entries (summary — verify current lists with national SAs):**

**Germany — DSK Blacklist [VERIFY current version]:**

- Employee monitoring systems (email, internet, DLP, keyloggers)
- Biometric access control for logical or physical access
- Workplace video surveillance systems (particularly CCTV covering individual workstations)
- AI systems for HR decisions (hiring, performance evaluation, termination)
- Health data processing by health insurance providers at large scale
- Tracking systems using geolocation data for employees

**France — CNIL List (14 mandatory categories) [VERIFY current version]:**

- Biometric processing for controlling access to workplaces or processing terminals
- Data processing using genetic data for purposes other than medical care or research
- Processing involving surveillance of employee activity at scale
- Profiling systems for banking and insurance that determine service access
- AI systems for social benefit eligibility determinations
- Processing of health data at large scale (social protection or health care organizations)
- Data processing for social scoring purposes
- Interconnection of personal data files from different controllers (data enrichment)
- Data on criminal offences or security breaches managed by private persons
- Large-scale video surveillance processing in public places
- Systematic monitoring of communications of employees
- Profiling of persons with vulnerable characteristics
- Genetic data processing for research
- Geolocation data processing at large scale to track individuals

**Netherlands — AP List [VERIFY current version]:**

- Processing of genetic data other than in medical context
- Profiling of persons in vulnerable situations
- Black lists (shared exclusion registers)
- Credit scoring and creditworthiness assessment
- Processing involving observation of publicly accessible areas on large scale
- Systematic monitoring of employees
- Biometric processing for unique identification

**Ireland — DPC List [VERIFY current version]:**

- Large-scale processing of special category data
- Systematic monitoring of employees
- Profiling at scale that may affect access to services
- AI/automated decision-making with legal or similarly significant effects
- Large-scale location tracking

**Belgium — APD List [VERIFY current version]:**

- Biometric data processing for authentication or identification (including low-tech)
- Systematic monitoring of individuals (employees, customers in public spaces)
- Large-scale processing of special category data
- Shared exclusion registers and credit scoring

**Italy — Garante List [VERIFY current version]:**

- Large-scale health data processing
- Biometric and genetic data processing
- Systematic monitoring of employees
- AI systems for automated decision-making with significant effects
- Data processing in judicial proceedings at scale
- Matching/cross-referencing datasets for profiling

**Poland — UODO List [VERIFY current version]:**

- Monitoring of employee work time and location
- Processing of large-scale personal data in e-commerce or online services
- Biometric data processing
- Large-scale health data processing
- Profiling for marketing purposes using special category data

**Whitelist check:** Apply only if a national whitelist exists and the processing matches
a whitelist entry precisely in ALL conditions. A blacklist match in another relevant
jurisdiction OVERRIDES a whitelist exemption.

**Multi-jurisdictional conflict resolution framework:**

1. Identify all relevant jurisdictions
2. Run Art. 35(3) mandatory trigger check (universal)
3. Run EDPB nine-criteria analysis (universal)
4. Check Art. 35(4) blacklist for EACH relevant jurisdiction
5. A blacklist match in ANY jurisdiction = DPIA required for that processing
6. Check whitelists only where they exist; whitelist exemption only valid if no blacklist
   match in any other relevant jurisdiction AND processing matches entry precisely

#### 4d. Threshold Verdict

Present the consolidated verdict in this format:

```
THRESHOLD VERDICT: [DPIA REQUIRED / DPIA RECOMMENDED / DPIA NOT REQUIRED]

Art. 35(3) mandatory triggers: [X of 3 applicable]
EDPB nine criteria: [N applicable — list which ones]
National blacklist matches: [SA: entry — YES/NO for each relevant jurisdiction]

Justification: [Plain language explanation of the basis for the verdict]

Accountability note: [If DPIA not required, note that this analysis must be retained
under Art. 5(2) to demonstrate accountability.]
```

**If DPIA REQUIRED or RECOMMENDED** → Proceed to Steps 5–10 (Mode B).
**If DPIA NOT REQUIRED** → Proceed to Mode C (Threshold Negative Memo) unless the
user requests full documentation.

### Step 5: Systematic Description (Art. 35(7)(a))

Document the processing in sufficient detail for a DPO and SA to understand what is
happening, why, and how.

**5.1 Controller information**

- Controller name and contact details
- DPO name and contact (mandatory under Art. 37 if applicable)
- EU representative if controller not established in EU (Art. 27)
- Lead SA and relevant SAs (based on main establishment and processing scope)

**5.2 Purposes of processing**

- State each purpose explicitly
- For each purpose, explain why data processing is necessary to achieve it

**5.3 Legal basis (Art. 6 and Art. 9 if applicable)**

- Identify the Art. 6 legal basis for each purpose
- **Critical:** If processing Art. 9 special categories, identify BOTH the Art. 6 basis
  AND the Art. 9(2) exception — these are separate legal hurdles
- If relying on legitimate interests (Art. 6(1)(f)): document the LIA balancing test
- If relying on consent: document consent mechanism and withdrawal path

**5.4 Categories of personal data**

- List every data category processed for each purpose
- Flag Art. 9/10 data explicitly
- Note data from which Art. 9 categories could be inferred (behavioral proxies)

**5.5 Data subjects**

- Categories of data subjects (with any vulnerable groups identified)
- Approximate number of data subjects (use four-factor scale: <1K / 1K–100K / 100K–1M / >1M)
- Any power imbalance between controller and data subjects?

**5.6 Data sources**

- Direct collection from data subjects
- Third-party sources (data brokers, social media, public databases, business partners)
- Automated inference or generation (AI outputs, scores, predictions)

**5.7 Data flow**

- Collection → Storage → Processing → Sharing → Deletion
- Produce or reference a data flow diagram

**5.8 Technology and systems**

- Systems used (databases, AI/ML models, surveillance infrastructure, IoT)
- Cloud providers and hosting locations
- If AI: model type, training data source, inference mechanism

**5.9 Recipients, processors, and sub-processors**

- All recipients (internal and external)
- All processors under Art. 28 (with Art. 28 DPA in place?)
- Sub-processor chains
- **⟁ CLARIFY** — For each processor: Do you have an Art. 28 DPA in place? Have
  you assessed their technical and organizational measures?

**5.10 International transfers**

- All transfers to third countries (non-EU/EEA)
- Transfer mechanism for each: Adequacy Decision, Standard Contractual Clauses (2021
  EU SCCs), Binding Corporate Rules, other
- Supplementary measures (encryption, pseudonymization, contractual clauses)
- Transfer Impact Assessment (TIA) conducted?

**5.11 Retention periods**

- Retention period for each data category with justification
- Deletion mechanisms and verification

**5.12 Data subject rights implementation**

- Access (Art. 15): how is it implemented?
- Rectification (Art. 16): how is it implemented?
- Erasure (Art. 17): what limits apply (legal retention, Art. 17(3) exceptions)?
- Portability (Art. 20): applicable for consent/contract basis processing?
- Objection (Art. 21): especially for LI-based processing
- Restriction (Art. 18): mechanism for temporary freeze
- For Art. 22 automated decisions: right to human review, explanation, contest

### Step 6: Necessity and Proportionality (Art. 35(7)(b))

**6.1 Necessity analysis**
For each data category and processing operation, assess:

- Is this data necessary to achieve the stated purpose?
- Could the purpose be achieved with less personal data?
- Could the purpose be achieved through less invasive means?
- Data minimization: flag any data collected "just in case" without specific necessity

**6.2 Proportionality analysis**

- Does the benefit from the processing justify the intrusion?
- Are less privacy-invasive alternatives available that would serve the same purpose?
- Is the retention period proportionate to the purpose?
- Is the geographic scope of data sharing proportionate?

**6.3 Legal basis adequacy**

- For legitimate interests: produce or reference an LIA balancing test
- For consent: is consent truly freely given, specific, informed, and unambiguous?
  Is there a genuine choice? Can data subjects withdraw without detriment?
- For legal obligation: cite the specific legal provision

**6.4 Data minimization**

- Confirm that only data strictly necessary for each purpose is collected
- Identify any fields that should be removed or made optional
- Note any "nice to have" data that should be eliminated

**6.5 Conclusion**

- PROPORTIONATE: Processing is necessary and proportionate to the purposes
- DISPROPORTIONATE: [Areas where redesign is needed]
- CONDITIONAL: Proportionate subject to [specific changes]

### Step 7: Risk Assessment (Art. 35(7)(c))

**Important:** Risks are assessed from the **data subject's perspective**. Assess risks
to the rights and freedoms of natural persons (Recital 75 GDPR), not corporate or
business risks.

#### 7a. Risk Identification

Using the **Risk Catalogue** below, identify all relevant risks for this processing. Do
not present the entire catalogue — select risks that are genuinely applicable based on
the processing description.

For each identified risk:

- Assign a Risk ID from the catalogue (or define a new one)
- Describe the specific risk scenario for this processing
- Identify the affected rights category (EU Charter reference)
- Assess **pre-mitigation** likelihood (1–5) and severity (1–5)

**Proactively propose risks** based on the processing type — do not wait for the user
to identify them.

#### 7b. Risk Scoring (5×5 Matrix)

**Likelihood Scale:**

| Score | Level       | Description                                                                                                                              |
| ----- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | Negligible  | Theoretically possible but no realistic scenario; extensive proven safeguards; would require extraordinary combination of failures       |
| 2     | Limited     | Unlikely under normal conditions; requires unusual combination of failures or sophisticated attack; rare precedent in sector             |
| 3     | Moderate    | Could occur in foreseeable circumstances; some precedent in similar contexts; safeguards reduce but do not eliminate possibility         |
| 4     | Significant | Likely to occur without additional safeguards; has occurred in comparable contexts; current controls insufficient; active threat vectors |
| 5     | Maximum     | Almost certain; inherent in processing design; known active exploitation in sector; affirmative countermeasures required to prevent      |

**Factors increasing likelihood:** Large scale / internet-connected systems / multiple
recipients / novel technology / weak access controls / inadequate staff training /
sector incident history / high data value to malicious actors

**Severity Scale (Impact on Data Subject):**

| Score | Level       | Description                                                                                                                                                        |
| ----- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1     | Negligible  | Minor inconvenience easily overcome; no lasting effect (e.g., unwanted marketing email)                                                                            |
| 2     | Limited     | Temporary difficulties overcome with effort; no permanent damage (e.g., re-registration required, minor financial cost)                                            |
| 3     | Significant | Serious difficulties overcome with real effort, time, or cost (e.g., blacklisting dispute, financial cost €100–€10,000, employment difficulty)                     |
| 4     | High        | Serious, potentially irreversible consequences (e.g., job loss, health deterioration, long-term financial damage, relationship breakdown)                          |
| 5     | Maximum     | Devastating, potentially irreversible (e.g., endangerment of life, permanent financial ruin, severe discrimination with lasting social exclusion, loss of liberty) |

**Factors increasing severity:** Art. 9 data > financial > behavioral > basic contact;
vulnerable data subjects; irreversible harm; power imbalance; essential service affected;
wider population impact; difficulty of remediation; cascading harm effects

**Risk Level Matrix:**

|           | **Sev 1** | **Sev 2** |  **Sev 3**   |  **Sev 4**   |  **Sev 5**   |
| --------- | :-------: | :-------: | :----------: | :----------: | :----------: |
| **Lik 5** | 5 Medium  |  10 High  | 15 Very High | 20 Very High | 25 Very High |
| **Lik 4** | 4 Medium  |  8 High   |   12 High    | 16 Very High | 20 Very High |
| **Lik 3** |   3 Low   | 6 Medium  |    9 High    |   12 High    | 15 Very High |
| **Lik 2** |   2 Low   | 4 Medium  |   6 Medium   |    8 High    |   10 High    |
| **Lik 1** |   1 Low   |   2 Low   |    3 Low     |   4 Medium   |   5 Medium   |

**Risk Level Thresholds:**

| Score | Level         | Implication                                                                                                                                                         |
| ----- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1–3   | **Low**       | Acceptable. Document and monitor. No specific action required beyond existing safeguards.                                                                           |
| 4–6   | **Medium**    | Action recommended. Implement additional safeguards. Monitor effectiveness.                                                                                         |
| 7–12  | **High**      | Action required. Significant mitigation before processing proceeds. Document justification if residual risk remains.                                                |
| 13–25 | **Very High** | Processing may not be permissible without fundamental redesign. Art. 36 prior consultation likely required if residual risk remains after all feasible mitigations. |

**Scoring discipline:**

- Always justify scores against the anchor descriptions — never assign scores without reasoning
- Score **pre-mitigation first**, then re-score after mitigations (mandatory for defensible DPIA)
- Mitigations primarily reduce **likelihood**; severity is largely inherent to data and context
- Avoid the "medium-medium trap" (3×3 default): use anchors to force honest calibration
- If genuinely uncertain, give a range and explain the uncertainty

#### 7c. Risk Register Format

Present each risk in this format:

| Risk ID | Description              | Rights Category      | Likelihood | Severity | Score | Level      |
| ------- | ------------------------ | -------------------- | ---------- | -------- | ----- | ---------- |
| [ID]    | [Specific risk scenario] | [EU Charter article] | [1–5]      | [1–5]    | [LxS] | [L/M/H/VH] |

### Step 8: Mitigation Measures (Art. 35(7)(d))

#### 8a. Select and Document Mitigations

For each identified risk, specify mitigation measures in three categories:

**Technical measures:**

- Encryption (at rest and in transit) with sound key management
- Pseudonymization (genuine — with technically separated additional information;
  per EDPB Guidelines 01/2025 on Pseudonymisation)
- Data minimization (collection minimization, anonymization at output stage)
- Access controls (RBAC/ABAC, MFA, privileged access management, need-to-know)
- Edge/local processing instead of cloud transmission (reduces exposure surface)
- Differential privacy, federated learning (for AI/ML systems)
- Audit logs with integrity protection
- Security testing, penetration testing, vulnerability management
- Data retention automation (deletion scripts, TTL policies)
- Security monitoring (SIEM, anomaly detection, SOC)

**Organizational measures:**

- Staff training and awareness on data protection
- Data protection by design and default (Art. 25) embedded in development process
- Clear data processing policies and procedures
- Incident response and breach notification procedures
- Vendor security assessments (Art. 28 compliance)
- Regular internal audits and DPO reviews
- Records of processing activities (Art. 30 ROPA)
- Purpose limitation and usage governance controls

**Legal and contractual measures:**

- Art. 28 DPAs with all processors (covering all Art. 28(3) mandatory clauses)
- Sub-processor approval mechanisms and flow-down clauses
- Contractual restrictions on secondary use of data
- Data sharing agreements with joint controllers
- Standard Contractual Clauses for third-country transfers
- Transfer Impact Assessments and supplementary measures
- Consent management platforms with granular records

#### 8b. Post-Mitigation Scoring

For each risk, re-score likelihood and severity after applying mitigations:

| Risk ID | Pre-Likelihood | Pre-Severity | Pre-Score | Mitigation(s) | Type | Post-Likelihood | Post-Severity | Residual Score | Residual Level |
| ------- | -------------- | ------------ | --------- | ------------- | ---- | --------------- | ------------- | -------------- | -------------- |

**Scoring principle:** Mitigations primarily reduce likelihood (encryption, access
controls, pseudonymization reduce probability of risk materializing). Severity is
rarely reduced by technical measures — if the risk does materialize, the impact on
the data subject is often unchanged. Data minimization is an exception: less data
means less exposure if a breach occurs, which can reduce severity.

### Step 9: Residual Risk and Art. 36 Prior Consultation

#### 9a. Residual Risk Summary

```
Residual Risk Summary
─────────────────────────────────────────────────────
Level          Count    Risk IDs
Very High       [N]     [IDs]
High            [N]     [IDs]
Medium          [N]     [IDs]
Low             [N]     [IDs]

Overall Position: [ACCEPTABLE / ACCEPTABLE WITH CONDITIONS / ART. 36 CONSULTATION REQUIRED]
```

**ACCEPTABLE:** All residual risks are Low or Medium. Processing can proceed.

**ACCEPTABLE WITH CONDITIONS:** High residual risks remain, but mitigation plan is
documented and conditions for implementation are defined. Processing can proceed
provided conditions are met and documented.

**ART. 36 CONSULTATION REQUIRED:** Very High residual risk remains after all feasible
mitigations. DPIA concludes that processing cannot proceed without SA consultation.

#### 9b. Art. 36 Prior Consultation Threshold

**Trigger:** DPIA concludes that residual risk remains high despite all measures (Art. 35(1)).
The EDPB interprets "high risk" for Art. 36 purposes as Very High residual risk (13–25
on the 5×5 matrix) that cannot be further mitigated with feasible measures.

**If Art. 36 consultation is required:**

- Processing must **not begin** until SA response is received or the response period
  has elapsed (Art. 36(2))
- SA has **8 weeks** to respond (extendable by a further 6 weeks for complex cases;
  Art. 36(2))
- SA may: provide written advice, exercise investigative/corrective powers, ban the
  processing, impose conditions
- For controller with EU establishment: consult the **Lead SA** (Art. 56 one-stop-shop)
- For controller without EU establishment: consult **each SA** in jurisdictions where
  data subjects are affected — one-stop-shop does NOT apply

**Art. 36(3) submission requirements:**
The consultation package must contain:

- (a) Respective responsibilities of controller and any joint controllers / processors
- (b) Purposes and means of intended processing
- (c) Measures and safeguards to protect data subjects
- (d) DPO contact details
- (e) DPIA (full report)
- (f) Any other information requested by the SA

Prepare a complete Art. 36 consultation package using the **Output Format Template**,
Section 4.

### Step 10: DPO Involvement and Data Subject Consultation

**10a. DPO involvement (Art. 35(2) — mandatory if DPO exists):**

- Document: DPO consulted on [date]
- DPO recommendation: [Proceed / Proceed with conditions / Do not proceed]
- DPO concerns raised (if any)
- Controller response to DPO concerns
- If controller disagrees with DPO: document divergence and reasoning

**⟁ CLARIFY** — If the controller has a DPO but has not yet consulted them, pause
and instruct: "GDPR Art. 35(2) requires the controller to seek the advice of the DPO
when carrying out a DPIA. Please consult your DPO before finalizing this assessment."

**10b. Data subject consultation (Art. 35(9) — where appropriate):**

- Art. 35(9) requires seeking the views of data subjects or their representatives
  "where appropriate" (without prejudice to commercial or public interest protection,
  or the security of processing operations)
- Document the decision: whether consultation was conducted, and why/why not
- If conducted: methodology used (survey, representative body, user research) and
  key findings

### Step 11: Document Generation

Select the appropriate output format based on mode:

| Mode                   | Primary Output                  | Secondary Output                      |
| ---------------------- | ------------------------------- | ------------------------------------- |
| A — Threshold only     | Threshold Verdict (in-session)  | Threshold Justification Memo (Mode C) |
| B — Full DPIA          | Full DPIA Report                | Executive Summary One-Pager           |
| C — Threshold Negative | Threshold Justification Memo    | —                                     |
| D — Art. 36 Package    | Art. 36 Consultation Package    | Full DPIA Report as Annex             |
| E — Review/Update      | Gap Analysis + Updated Sections | Updated Full DPIA Report              |

Generate .docx if the docx skill is available. Otherwise, generate well-formatted Markdown.

### Step 12: Quality Verification

Before delivering any output, run the **Quality Assurance Framework** (see section below):

1. Run 5 Citation Quality Gates silently — revise any failures
2. For every Very High risk classification and for the Art. 36 threshold conclusion,
   run 3-pass Self-Interrogation — revise if any pass identifies an error
3. Assign Confidence Scores to the threshold verdict and to each Very High risk finding
4. Complete the Glass Box Audit Trail
5. Review output against Writing Standards

---

## AI and Profiling Use Cases

### EDPB Opinion 28/2024 — Dual-Phase AI DPIA

For AI systems, EDPB Opinion 28/2024 requires treating training and deployment as
**separate processing activities** with distinct risk profiles. A deployer cannot rely
on the model provider's DPIA.

**Training Phase analysis:**

- Algorithmic bias baked into training data (DISC-01)
- Proxy discrimination via correlated neutral variables (DISC-02)
- Model memorization and data leakage — can the model reproduce training data? (CONF-04)
- Model inversion and membership inference attacks (PSEU-02)
- Function creep: was data scraped from the web or sourced from another controller? (CTRL-03)
- Was consent obtained from data subjects whose data was used for training?
- Was anonymization of training data genuinely achieved? Singling-out attacks may apply.

**Deployment Phase analysis:**

- Hallucinations generating false biographical information (REPD-04)
- Discriminatory outputs from trained bias (DISC-01)
- Opacity of decision-making — can data subjects understand how they are profiled? (CTRL-01)
- Difficulty exercising rights against AI-generated profiles (CTRL-02)
- Automated decisions with legal/significant effects triggering Art. 22 (DENY-01)

**Key legal questions for AI DPIAs:**

- Is the processing "anonymized"? Assess singling-out risk rigorously — if singling out
  is possible, data is personal data, not anonymous data
- Does the model produce outputs about identifiable natural persons?
- Who is the controller for training vs. deployment? (May differ for fine-tuned models)
- Does the deployer have access to the model weights, architecture, and training metadata
  needed to conduct a meaningful DPIA?

### AI Act FRIA vs. GDPR DPIA

For high-risk AI systems under Regulation (EU) 2024/1689 (AI Act), deployers that are
bodies governed by public law, or private bodies providing public services, may also be
required to conduct a **Fundamental Rights Impact Assessment (FRIA)** under Art. 27 AI Act.

| Dimension          | GDPR DPIA (Art. 35)                                        | AI Act FRIA (Art. 27)                                                       |
| ------------------ | ---------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Legal basis**    | GDPR Art. 35                                               | AI Act Art. 27                                                              |
| **Scope**          | Risks to data subjects' privacy and data protection rights | Broader fundamental rights (Art. 7 + Art. 8 EU Charter + others)            |
| **Trigger**        | High-risk data processing                                  | High-risk AI system deployment                                              |
| **Who must do it** | Controllers (always)                                       | Deployers who are public bodies or private bodies providing public services |
| **Output**         | DPIA report, published if required by SA                   | FRIA, notified to market surveillance authority                             |
| **Overlap**        | Can be conducted jointly; FRIA references DPIA             | FRIA may incorporate DPIA by reference                                      |

**Practical rule:** One does not replace the other. For high-risk AI systems processing
personal data deployed by covered entities, both a DPIA and a FRIA are required. They
can be produced as a combined document but must address each instrument's requirements.

### Profiling and Automated Decision-Making

For scoring, ranking, or automated decision systems:

**⟁ CLARIFY** on these key questions:

- Does a human make the final decision, or does the algorithm? What is the scope of
  human review — genuine independent judgment, or rubber-stamp?
- Are there legal effects? (Benefit denial, contract refusal, credit decision, border access)
- Are there "similarly significant effects"? (Access to essential services, employment,
  housing, insurance — assess by the importance of what is denied or granted)

**Documentation requirements for Art. 22 systems:**

- Meaningful information about the logic involved
- Significance and envisaged consequences for the data subject
- Right to obtain human intervention, express a point of view, and contest the decision
- Ensure human reviewer has access to and exercises genuine judgment (not mere confirmation)

---

## Vendor and Processor Involvement

### Controller Obligations Under Art. 28

When processors handle personal data on the controller's behalf, the controller remains
responsible for DPIA compliance. Processors support the controller but do not own the
DPIA obligation for the controller's processing.

**What to require from processors (Art. 28(3)(f)):**

- Assist the controller with security, breach notification, erasure, and DPIA
- Specifically: "assist the controller in ensuring compliance with the obligations
  pursuant to Articles 32 to 36" — this includes DPIA

**Due diligence steps for processors:**

1. Request the processor's technical and organizational security measures (TOMs) description
2. Review the processor's own records of processing (Art. 30(2))
3. Confirm the processor's sub-processor list and sub-processing agreements
4. Assess whether the processor's system architecture is compatible with your DPIA mitigations
5. For high-risk processors: conduct a security audit or review audit reports (ISO 27001,
   SOC 2 Type II) — but note that certifications reduce likelihood, not severity

**Art. 28 DPA mandatory clauses check (Art. 28(3)):**

- (a) Process only on documented instructions
- (b) Ensure persons authorised to process are bound by confidentiality
- (c) Implement appropriate security measures (Art. 32)
- (d) Sub-processing only with controller's prior written authorization
- (e) Assist controller with data subject rights exercise
- (f) Assist with security, breach notification, erasure, and DPIA
- (g) Delete or return data at end of service
- (h) Provide all information necessary to demonstrate compliance

**Processor's own DPIA:** If the processor uses the data for its own purposes, it may
become a controller for those activities and must conduct its own DPIA. A processor's
DPIA covering its own processing does not substitute for the controller's DPIA.

### Sub-Processor Chains

In complex data flows with multiple sub-processors:

- Map the complete processor chain (controller → processor → sub-processor → …)
- Each link in the chain must have a compliant Art. 28 agreement
- Controller's Art. 28 DPA must require processor to impose equivalent obligations on
  sub-processors (Art. 28(4))
- Material sub-processor changes require controller's prior written authorization
- Assess jurisdiction risk at each node (CLOUD Act, government access requests)

---

## Risk Catalogue (EU Charter–Referenced)

Select relevant risks from this catalogue based on the processing description. Do not
present the entire catalogue — propose the applicable risks proactively.

### Discrimination (Art. 21 EU Charter)

| ID      | Risk                                                                             | Primary Triggers                                                      |
| ------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| DISC-01 | Algorithmic bias producing discriminatory outcomes                               | AI/ML scoring, hiring algorithms, credit decisions, insurance pricing |
| DISC-02 | Proxy discrimination via neutral data correlating with protected characteristics | Zip code profiling, browsing patterns, purchasing behavior            |
| DISC-03 | Differential service quality based on profiling                                  | Dynamic pricing, tiered service, customer value scoring               |
| DISC-04 | Health-status discrimination from wearable/medical data                          | Insurance exclusions, employment screening via health proxies         |

### Identity Theft and Fraud (Art. 8 EU Charter)

| ID      | Risk                                             | Primary Triggers                                      |
| ------- | ------------------------------------------------ | ----------------------------------------------------- |
| IDTH-01 | Identity theft from exposed personal identifiers | Large-scale databases with names, IDs, dates of birth |
| IDTH-02 | Account takeover from compromised credentials    | Password stores, biometric template databases         |
| IDTH-03 | Social engineering enabled by detailed profiles  | Comprehensive CRM data, behavioral profiles           |
| IDTH-04 | Deepfake creation from biometric data            | Facial images, voice recordings                       |

### Financial Loss (Art. 17 EU Charter)

| ID      | Risk                                                 | Primary Triggers                              |
| ------- | ---------------------------------------------------- | --------------------------------------------- |
| FINL-01 | Direct financial loss from unauthorized transactions | Payment data, banking integrations            |
| FINL-02 | Credit damage from inaccurate automated scoring      | Credit scoring, shared blacklists             |
| FINL-03 | Insurance denial or inflation from profiling         | Health data, driving behavior, lifestyle data |
| FINL-04 | Employment loss from unfair automated evaluation     | Performance AI, hiring/firing algorithms      |

### Reputational Damage (Arts. 1, 7 EU Charter)

| ID      | Risk                                                   | Primary Triggers                                      |
| ------- | ------------------------------------------------------ | ----------------------------------------------------- |
| REPD-01 | Public exposure of private information                 | Data breaches, unauthorized sharing                   |
| REPD-02 | Incorrect association with criminal/unethical activity | AML false positives, blacklist errors                 |
| REPD-03 | Social stigma from disclosed sensitive data            | Health conditions, sexual orientation, addiction data |
| REPD-04 | AI-generated false biographical information            | LLM hallucinations producing incorrect personal facts |

### Loss of Confidentiality (Art. 7 EU Charter, professional secrecy)

| ID      | Risk                                                 | Primary Triggers                                 |
| ------- | ---------------------------------------------------- | ------------------------------------------------ |
| CONF-01 | Breach of professional secrecy (legal, medical, tax) | Law firm data, medical records, tax records      |
| CONF-02 | Unauthorized disclosure to third parties             | Processor breaches, over-broad access            |
| CONF-03 | Foreign government access to protected data          | US CLOUD Act exposure, Schrems II transfer risks |
| CONF-04 | AI model memorization and data leakage               | LLMs reproducing training data, model inversion  |

### Reversal of Pseudonymization (Art. 8 EU Charter, Art. 25 GDPR)

| ID      | Risk                                           | Primary Triggers                                               |
| ------- | ---------------------------------------------- | -------------------------------------------------------------- |
| PSEU-01 | Re-identification through data linkage         | Pseudonymized data + auxiliary data                            |
| PSEU-02 | Model inversion / membership inference attacks | ML models revealing training data                              |
| PSEU-03 | Singling out in "anonymous" datasets           | Location traces, transaction patterns, behavioral fingerprints |

### Physical Harm (Arts. 2, 3 EU Charter)

| ID      | Risk                                              | Primary Triggers                                     |
| ------- | ------------------------------------------------- | ---------------------------------------------------- |
| PHYS-01 | Stalking or harassment via location data          | Real-time tracking, movement history                 |
| PHYS-02 | Domestic violence risk from exposed personal data | Shared accounts, family trackers, address disclosure |
| PHYS-03 | Safety risks from vehicle data manipulation       | Connected vehicle systems, remote control access     |
| PHYS-04 | Medical harm from inaccurate health data          | Wrong medication alerts, faulty diagnostic AI        |

### Loss of Control Over Personal Data

| ID      | Risk                                                                 | Primary Triggers                                       |
| ------- | -------------------------------------------------------------------- | ------------------------------------------------------ |
| CTRL-01 | Opaque processing — data subjects cannot understand how data is used | Complex AI, multi-layered data flows                   |
| CTRL-02 | Inability to exercise rights effectively                             | Technical barriers, cross-system complexity            |
| CTRL-03 | Function creep — data repurposed beyond original collection          | Ecosystem platforms, M&A data integration, AI training |
| CTRL-04 | Indefinite retention without justification                           | No deletion policy, blockchain immutability            |

### Chilling Effect on Freedoms (Arts. 11, 12, 45 EU Charter)

| ID      | Risk                                          | Primary Triggers                                             |
| ------- | --------------------------------------------- | ------------------------------------------------------------ |
| CHIL-01 | Self-censorship due to surveillance awareness | Workplace monitoring, public surveillance, online tracking   |
| CHIL-02 | Deterrence from legitimate activity           | Political profiling, protest surveillance, academic chilling |
| CHIL-03 | Behavioral conformity pressure                | Social scoring, employee ranking, reputation systems         |

### Denial of Services

| ID      | Risk                                         | Primary Triggers                                       |
| ------- | -------------------------------------------- | ------------------------------------------------------ |
| DENY-01 | Automated denial of essential services       | Algorithmic gatekeeping in banking, insurance, housing |
| DENY-02 | Platform ban with significant consequences   | Content moderation algorithms                          |
| DENY-03 | Cross-sector blocking from shared blacklists | Industry exclusion lists, credit bureau entries        |

### Manipulation and Exploitation (Art. 1 EU Charter — dignity)

| ID      | Risk                                          | Primary Triggers                                         |
| ------- | --------------------------------------------- | -------------------------------------------------------- |
| MANP-01 | Behavioral manipulation through dark patterns | UX exploiting psychological biases                       |
| MANP-02 | Exploitation of psychological vulnerabilities | Targeted ads to persons in distress, addiction targeting |
| MANP-03 | Micro-targeting for political manipulation    | Behavioral profiling for political advertising           |

### Processing-Specific Risk Profiles

**AI/ML Systems:**
Training phase: DISC-01, DISC-02, CONF-04, PSEU-02, CTRL-03
Deployment phase: REPD-04, DISC-01, CTRL-01, CTRL-02, DENY-01

**Employee Monitoring:**
Email/internet monitoring: CHIL-01, CONF-01, CTRL-01
DLP systems: DISC-01 (false positives → discipline), REPD-02, CHIL-01
GPS/fleet tracking: CHIL-01, CTRL-03 (off-hours tracking), PHYS-01

**Video Surveillance / Facial Recognition:**
Standard CCTV: CHIL-01, CTRL-03, CHIL-02
Facial recognition: DISC-01, REPD-02, IDTH-04, CHIL-01

**Health and Genetic Data:**
Health databases: PSEU-01, DISC-04, CONF-01
Genetic testing: DISC-04 (familial privacy risk), FINL-03, CTRL-01
Implantable devices: PHYS-04, CONF-02, CTRL-01

**Financial and Credit Processing:**
Credit scoring: DISC-01, FINL-02, DENY-01, CTRL-01
Shared blacklists: DENY-03, FINL-02, REPD-02

**Connected Vehicles:**
Location/telemetry: CHIL-01, CTRL-03, FINL-03
Biometric (drowsiness/attention): DISC-04, CHIL-01, CTRL-03
Edge/local processing significantly reduces CHIL-01 and CTRL-03 likelihood

---

## Severity/Status Classification

### Threshold Verdict

| Verdict               | Meaning                                                                        | Required Action                                                                                |
| --------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| **DPIA REQUIRED**     | Art. 35(3) trigger applies OR 2+ EDPB criteria met OR national blacklist match | Conduct full DPIA before processing begins; do not begin processing without completed DPIA     |
| **DPIA RECOMMENDED**  | 1 EDPB criterion met; no blacklist match; processing is borderline             | Strongly consider conducting DPIA; document decision either way under Art. 5(2)                |
| **DPIA NOT REQUIRED** | 0 criteria met; no blacklist match; documented analysis                        | Retain Threshold Justification Memo for Art. 5(2) accountability; review if processing changes |

### DPIA Position (Residual Risk)

| Position                          | Meaning                                                                     | Required Action                                                                          |
| --------------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **PROCEED**                       | All residual risks Low or Medium                                            | Processing can begin; monitor and review at next trigger                                 |
| **PROCEED WITH CONDITIONS**       | High residual risks remain; mitigation plan defined                         | Processing can begin provided conditions are implemented; document implementation        |
| **ART. 36 CONSULTATION REQUIRED** | Very High residual risk remains after all feasible mitigations              | Do not begin processing; consult Lead SA (Art. 36); await SA response or response period |
| **DO NOT PROCEED**                | Processing cannot be made lawful; fundamental rights impact is unacceptable | Redesign or abandon processing; document conclusion                                      |

### Risk Level

| Level         | Score Range | Action                                                                                     |
| ------------- | ----------- | ------------------------------------------------------------------------------------------ |
| **Low**       | 1–3         | Acceptable; document and monitor                                                           |
| **Medium**    | 4–6         | Action recommended; implement additional safeguards                                        |
| **High**      | 7–12        | Action required; significant mitigation before go-live; document justification if residual |
| **Very High** | 13–25       | May not be permissible; Art. 36 consultation likely if residual                            |

---

## Prioritization Framework

Prioritize findings and mitigations across four tiers:

| Tier       | Label      | Criteria                                                                                                                                          | Timeline                                         |
| ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **Tier 1** | CRITICAL   | Art. 36 consultation required; Very High residual risk; processing legally impermissible without redesign                                         | Immediate — block processing until resolved      |
| **Tier 2** | HIGH       | High residual risk; significant mitigation required before go-live; missing Art. 28 DPAs; Art. 9 processing without both Art. 6 + Art. 9(2) bases | 0–30 days; must resolve before launch            |
| **Tier 3** | STANDARD   | Medium residual risk; mitigation recommended; documentation gaps; DPO consultation pending                                                        | 30–90 days; processing can begin with monitoring |
| **Tier 4** | MONITORING | Low residual risk; ongoing review sufficient; next review trigger in 12 months or at material change                                              | Standard review cycle                            |

---

## Quality Assurance Framework

### Citation Quality Gates

Run these five gates silently before delivering any output. Revise before delivery if any gate fails.

| Gate           | Rule                                                                                                                     | Fail Action                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific GDPR article, EDPB guideline, or established principle                                | Add citation or mark "[UNVERIFIED]"                      |
| **Format**     | All citations use recognizable format: "GDPR Art. 35(3)(a)", "WP 248 rev.01, p. 11", "EDPB Opinion 28/2024"              | Fix format                                               |
| **Currency**   | Every cited guideline and blacklist entry checked for updates or replacement                                             | Flag "[CHECK CURRENCY — verify against current SA list]" |
| **Domain**     | Analysis stays within EU/EEA GDPR scope; national law claims are jurisdiction-specific; no US/UK law stated as universal | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden; uncertain assessments carry appropriate qualifiers                            | Add confidence qualifier                                 |

### Self-Interrogation for Very High Risk and Art. 36 Determinations

For any risk classified Very High and for any Art. 36 consultation threshold conclusion,
apply this 3-pass adversarial review:

**Pass 1 — Legal Chain Integrity:** Does the risk classification follow logically from
the cited legal authority and the specific facts of this processing? Would a DPA/SA
actually reach this conclusion given the context?

**Pass 2 — Completeness:** Have all relevant factors been considered — EDPB guidelines,
relevant SA guidance, comparable enforcement decisions, sector-specific rules?

**Pass 3 — Challenge:** What is the strongest argument that this risk is lower, or that
Art. 36 consultation is not required? Under what circumstances would a reasonable DPO
or SA reach a different conclusion? Document the counter-argument and why it does not
change the classification.

### Confidence Scoring

| Level        | Range     | Meaning                                                                                      | Action                                                           |
| ------------ | --------- | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Definite** | 0.95–1.0  | Art. 35(3) trigger — clear mandatory requirement; settled EDPB guidance                      | State with full confidence                                       |
| **High**     | 0.80–0.94 | Strong authority; EDPB criteria clearly met; blacklist entry clearly applicable              | State with brief caveat                                          |
| **Probable** | 0.60–0.79 | Good arguments; criteria may apply depending on facts; blacklist match requires verification | State with reasoning and contra-indicators                       |
| **Possible** | 0.40–0.59 | Genuinely uncertain; reasonable DPOs could disagree on threshold; facts are ambiguous        | Flag for DPO/counsel review with both sides                      |
| **Unlikely** | 0.0–0.39  | Weak basis; speculative                                                                      | Do not assert; flag "[UNCERTAIN — professional review required]" |

Apply Confidence Scoring to:

- The threshold verdict
- Each blacklist match assessment
- Each Very High risk classification
- The Art. 36 consultation threshold conclusion

---

## Glass Box Audit Trail

Include this YAML block in every delivered DPIA output for full traceability:

```yaml
glass_box:
  skill_name: "legalcode-eu-dpia-assessment"
  mode: "[A-Threshold / B-Full DPIA / C-Threshold Memo / D-Art36 Package / E-Review]"
  processing_activity: "[Processing activity name]"
  controller: "[Controller name]"
  relevant_jurisdictions: "[List of relevant Member States]"
  lead_sa: "[Lead SA — based on main establishment]"
  legalcode_mcp: "[Connected / Not connected]"
  research_reference_file: "[Path to /tmp/legalcode-dpia-authority.md or 'Not created']"
  threshold_verdict: "[DPIA REQUIRED / RECOMMENDED / NOT REQUIRED]"
  art35_3_triggers_met: "[0-3]"
  edpb_criteria_met: "[0-9 — list which ones]"
  blacklist_matches: "[List: SA: entry — YES/NO for each jurisdiction checked]"
  risk_register_count: "[N risks identified]"
  highest_inherent_risk: "[Score and level]"
  highest_residual_risk: "[Score and level]"
  dpia_position: "[PROCEED / PROCEED WITH CONDITIONS / ART. 36 REQUIRED / DO NOT PROCEED]"
  dpo_consulted: "[YES / NO / Not applicable]"
  data_subject_consultation: "[Conducted / Not conducted — reasoning]"
  art36_consultation_required: "[YES / NO]"
  citations_verified: "[N VERIFIED via legalcode-mcp / N marked VERIFY]"
  confidence_threshold_verdict: "[Level — X.XX]"
  confidence_art36: "[Level — X.XX / N/A]"
  limitations:
    - "[Blacklist entries: verify against current SA lists as these change]"
    - "[legalcode-mcp not connected: all legal references require manual verification]"
    - "[AI Act FRIA assessment requires separate analysis — not included in DPIA scope]"
  reviewer: "AI-assisted — requires DPO involvement (Art. 35(2)) and qualified legal review"
```

---

## Anti-Patterns

What NOT to do when conducting or reviewing DPIAs:

1. **Running the DPIA retroactively.** GDPR Art. 35(1) requires DPIAs to be carried out
   _before_ processing begins. A post-hoc DPIA can document compliance gaps but does not
   remediate the violation of starting processing without one.

2. **Treating Art. 35(3) triggers as an exhaustive list.** The three mandatory triggers
   are a floor, not a ceiling. Processing not falling within Art. 35(3) may still require
   a DPIA if the EDPB nine-criteria analysis or a national SA blacklist entry applies.

3. **Relying on the one-stop-shop to skip national blacklist checks.** The one-stop-shop
   (Art. 56) governs enforcement jurisdiction — it does NOT limit which Art. 35(4) lists
   apply to the DPIA obligation. A controller led by the Irish DPC must still check the
   DSK blacklist for German processing.

4. **Treating pseudonymized data as automatically low-risk.** Assess re-identification
   risk genuinely. If singling out from the dataset is technically feasible, the data
   remains personal. Per EDPB Guidelines 01/2025 on Pseudonymisation, effective
   pseudonymization requires technical separation of the additional information.

5. **Conflating DPIA with a corporate security risk assessment.** DPIA assesses risks to
   the rights and freedoms of _data subjects_ (Recital 75 GDPR) — not to the organization.
   A CISO's security assessment and a DPO's DPIA serve different purposes and must not
   be conflated or substituted for each other.

6. **Allowing the processor to conduct the DPIA for the controller's processing.**
   The DPIA obligation belongs to the controller. Processors may assist (Art. 28(3)(f)),
   but the controller's DPIA covers the controller's processing purposes. A processor's
   own DPIA covering its platform does not discharge the controller's obligation.

7. **Treating profiling systems with "human review" as automatically safe from Art. 22.**
   If the human reviewer routinely approves algorithmic outputs without independent
   analysis, the review is a rubber-stamp and the system qualifies as automated
   decision-making under Art. 22.

8. **Using a single DPIA for multiple distinct processing activities.** Each distinct
   high-risk processing activity requires its own DPIA. Combining unrelated activities
   into one document undermines the specificity required for meaningful assessment.

9. **Documenting mitigations without showing inherent risk scores.** The DPIA must show
   pre-mitigation likelihood × severity and post-mitigation residual scores. Showing only
   residual risk without the baseline makes the DPIA unauditable.

10. **Using a fixed numerical threshold for "large scale."** The EDPB's four-factor test
    (number of subjects, data volume, duration, geographic extent) has no fixed numerical
    floor. Never state that a specific number of data subjects equals or does not equal
    "large scale."

11. **Failing to document the "no DPIA needed" decision.** Where threshold assessment
    concludes DPIA is not required, the analysis must be retained under Art. 5(2)
    accountability. An undocumented "no DPIA" decision is a compliance gap in the event
    of an SA inquiry.

12. **Treating the DPO's opinion as an advisory rubber-stamp.** Art. 35(2) requires the
    controller to seek the DPO's advice and document that advice. Where the controller
    disagrees with the DPO, the divergence must be documented with reasons — not silently
    overridden.

13. **Using the AI model provider's DPIA for the deployer's processing.** Per EDPB Opinion
    28/2024, training and deployment are separate processing activities. A deployer's use
    of a third-party AI model requires the deployer to conduct its own DPIA covering how
    the model processes personal data in the deployment context.

14. **Treating Art. 9 processing as requiring only "extra justification."** Processing
    special category data requires BOTH a valid Art. 6 legal basis AND a specific Art. 9(2)
    exception. These are two independent legal requirements — one cannot substitute for
    the other.

15. **Concluding "no DPIA needed" based solely on a whitelist entry without checking for
    blacklist entries in other relevant jurisdictions.** A whitelist exemption in France
    does not override a blacklist entry in Germany if the processing occurs in both Member
    States. Multi-jurisdictional analysis must run to completion.

16. **Treating vendor SOC 2 or ISO 27001 certification as eliminating DPIA risk.**
    Certifications reduce the _likelihood_ that a risk will materialize (controls exist and
    are audited). They do not reduce _severity_ — if a breach occurs, the impact on data
    subjects is unchanged. Score both dimensions independently.

17. **Ignoring aggregation effects when combining datasets from different sources.** Combining
    two datasets that are individually innocuous can create a combined risk profile that
    crosses the DPIA threshold. Assess the combined dataset, not each source in isolation.

18. **Conducting the DPIA as a one-time exercise.** GDPR requires DPIAs to be reviewed
    when processing changes materially. Triggers for review: significant change in
    processing scope or technology, new data categories, new recipients, new jurisdictions,
    security incidents, 12-month routine review, new EDPB guidance, new SA enforcement action.

19. **Failing to assess the AI Act FRIA obligation alongside the DPIA.** For controllers
    deploying high-risk AI systems that are bodies governed by public law or private bodies
    providing public services, the FRIA obligation under AI Act Art. 27 is independent of
    and cumulative with the GDPR DPIA obligation.

20. **Assuming that "legitimate interests" is a flexible basis to avoid consent for
    high-risk processing.** Where processing meets DPIA threshold criteria — particularly
    involving vulnerable data subjects, special category data inferences, or automated
    decisions with significant effects — the LIA balancing test is highly unlikely to be
    satisfied. Legitimate interests cannot be used to launder consent-dependent processing.

---

## Writing Standards

Apply these standards before delivering any DPIA output:

**Plain language for the executive summary and threshold verdict:**

- Write as if addressing a C-suite executive who is not a lawyer
- Avoid jargon in executive sections; define technical terms the first time they appear
- Use short sentences (aim for <25 words per sentence in executive sections)
- Lead with the recommendation, then the reasoning

**Precision for the technical analysis sections:**

- Cite specific GDPR articles and EDPB guidelines, not vague references to "data
  protection law"
- Use the exact EDPB language for the nine criteria and risk scoring anchors
- Do not paraphrase Art. 35(3) triggers — reproduce them precisely with appropriate
  qualification

**Language requirements for authority submissions:**

- Art. 36 consultation packages submitted to a national SA should generally be in the
  official language of that SA [JURISDICTION-SPECIFIC — verify with the relevant SA]
- German DSK: packages addressed to the German lead SA typically require German
- French CNIL: French language required for CNIL submissions [VERIFY]
- Irish DPC: English is acceptable (DPC operates in both English and Irish)
- For multi-jurisdictional submissions to a lead SA: submit in the language of the
  lead SA; attach an English translation if requested by the SA

**DPIA classification and handling:**

- Mark DPIA documents with appropriate classification: CONFIDENTIAL or RESTRICTED
- DPIA reports contain sensitive information about security vulnerabilities; distribute
  on a need-to-know basis
- Do not publish DPIA reports externally unless required by the SA (some SAs publish
  summaries of DPIAs for certain types of processing)

**Quality gate before delivery:**

- [ ] All Art. 35(3) trigger analyses cite the specific trigger text
- [ ] All nine-criteria findings include reasoning, not just YES/NO
- [ ] All blacklist entries are flagged as [VERIFY] if not confirmed via legalcode-mcp
- [ ] All risk scores have written justification against the anchor descriptions
- [ ] All Very High risks have undergone 3-pass Self-Interrogation
- [ ] Glass Box YAML is complete
- [ ] Threshold verdict and DPIA position are stated clearly at the top of the output
- [ ] DPO consultation status is documented

---

## External Tool Integration

### legalcode-mcp (Primary Legal Research)

Use legalcode-mcp to search for:

- Current Art. 35(4) blacklist entries for each relevant Member State SA
- Recent SA enforcement actions related to the processing type
- EDPB opinions and guidelines on specific processing activities
- Sector-specific guidance (health data, employee monitoring, AI systems)
- Transfer Impact Assessment resources for third-country transfers

**With legalcode-mcp connected:**

- Search for each relevant SA's current blacklist before running Step 4c
- Search for enforcement context for Very High risk findings
- Mark legalcode-mcp sourced citations as VERIFIED in the Glass Box audit trail
- Save research results to `/tmp/legalcode-dpia-authority.md`

**Without legalcode-mcp:**

- Use the National Blacklist Reference in this skill (static snapshot — may not reflect
  current lists)
- Mark all blacklist assessments as "[VERIFY — check current SA list at [SA website]]"
- Mark all legal references as [VERIFY] where not contained verbatim in this skill
- Note in Glass Box: `legalcode_mcp: "Not connected"`
- Instruct the user to verify blacklist entries directly with each relevant SA

### Docx Generation

For document generation, check for the `docx` or `docx-processing-anthropic` skill.
If available: generate .docx following the Output Format Template structure.
If unavailable: generate well-formatted Markdown as fallback, clearly labeled as
suitable for pasting into Word or Google Docs.

---

## Output Format Template

### Template 1: Full DPIA Report

```markdown
# DATA PROTECTION IMPACT ASSESSMENT

## [Processing Activity Name]

**Reference:** DPIA-[YYYY]-[NNN]
**Version:** [X.Y]
**Date:** [Date]
**Controller:** [Name]
**DPO:** [Name, contact]
**Classification:** CONFIDENTIAL

---

## Document Control

| Version | Date | Author | Changes | Approved By |
| ------- | ---- | ------ | ------- | ----------- |

---

## Disclaimer

Prepared with AI-assisted guidance (Legalcode EU DPIA Assessment). Not legal advice.
Final DPIA decisions are those of the identified individuals herein, subject to DPO
review (GDPR Art. 35(2)) and qualified legal advice.

---

## Executive Summary

[Recommendation: PROCEED / PROCEED WITH CONDITIONS / ART. 36 CONSULTATION / DO NOT PROCEED]

### Processing Overview

[2-3 paragraphs, plain language]

### Key Findings

[Top risks, overall DPIA position — suitable for C-suite]

### Required Actions

| Action | Owner | Deadline |
| ------ | ----- | -------- |

---

## Section 1: Threshold Assessment

### 1.1 Art. 35(3) Mandatory Triggers

| Trigger                                                              | Applies? | Reasoning |
| -------------------------------------------------------------------- | -------- | --------- |
| (a) Systematic extensive evaluation with legal/significant effects   |          |           |
| (b) Large-scale Art. 9/Art. 10 processing                            |          |           |
| (c) Systematic monitoring of publicly accessible area at large scale |          |           |

### 1.2 Nine-Criteria Analysis (EDPB WP 248 rev.01)

| #   | Criterion | Applies? | Reasoning |
| --- | --------- | -------- | --------- |

[all 9 rows]

### 1.3 National Blacklist Analysis

| Jurisdiction | Why Relevant | Blacklist Checked | Match? | Entry Reference |
| ------------ | ------------ | ----------------- | ------ | --------------- |

### 1.4 Threshold Verdict

**[DPIA REQUIRED / RECOMMENDED / NOT REQUIRED]**
[Consolidated justification]

---

## Section 2: Systematic Description (Art. 35(7)(a))

[Subsections 2.1–2.12 per workflow Step 5]

---

## Section 3: Necessity and Proportionality (Art. 35(7)(b))

[Subsections per workflow Step 6]

---

## Section 4: Risk Assessment (Art. 35(7)(c))

### 4.1 Methodology

5×5 semi-quantitative risk matrix. Risks assessed from data subject's perspective
per Recital 75 GDPR and EDPB WP 248 rev.01.

### 4.2 Risk Register

| Risk ID | Description | Rights Category | Likelihood | Severity | Score | Level |
| ------- | ----------- | --------------- | ---------- | -------- | ----- | ----- |

### 4.3 Risk Heat Map

[5×5 table with risk IDs mapped to cells, color-coded: Low/Medium/High/Very High]

---

## Section 5: Mitigation Measures (Art. 35(7)(d))

| Risk ID | Risk | Pre-Score | Mitigation(s) | Type | Post-L | Post-S | Residual Score | Residual Level |
| ------- | ---- | --------- | ------------- | ---- | ------ | ------ | -------------- | -------------- |

---

## Section 6: Residual Risk

### 6.1 Summary

| Level | Count | Risk IDs |
| ----- | ----- | -------- |

### 6.2 Overall DPIA Position

**[PROCEED / PROCEED WITH CONDITIONS / ART. 36 CONSULTATION REQUIRED / DO NOT PROCEED]**
[Justification]

---

## Section 7: Art. 36 Prior Consultation

[If applicable: decision + reasoning + residual risks requiring consultation]

---

## Section 8: DPO Opinion (Art. 35(2))

DPO consulted: [YES/NO/N/A]
DPO recommendation: [text]
Controller response: [text]
Divergence documented: [YES/NO — if YES, explain]

---

## Section 9: Data Subject Consultation (Art. 35(9))

Consultation conducted: [YES/NO]
Reasoning: [why/why not]
Findings: [if conducted]

---

## Section 10: Review and Monitoring

Next review date: [date]
Review triggers: material change / new technology / incident / new guidance / 12 months
Review owner: [name/role]

---

## Section 11: Approval and Sign-Off

| Role              | Name | Date |
| ----------------- | ---- | ---- |
| DPIA Author       |      |      |
| DPO               |      |      |
| Processing Owner  |      |      |
| IT Security       |      |      |
| Senior Management |      |      |

---

## Annexes

A: Data flow diagram
B: ROPA extract (Art. 30)
C: Legal basis documentation (LIA, consent records)
D: Reference documents (Art. 35 GDPR, WP 248, applicable national lists)

---

[Glass Box YAML]
```

### Template 2: Threshold Justification Memo

```markdown
# THRESHOLD JUSTIFICATION MEMO

## [Processing Activity Name] — DPIA Not Required

**Reference:** THRESH-[YYYY]-[NNN]
**Date:** [Date]
**Controller:** [Name], [EU establishments relevant to this processing]
**Relevant Jurisdictions:** [All jurisdictions checked]
**Classification:** CONFIDENTIAL

**VERDICT:** DPIA NOT REQUIRED — retained for Art. 5(2) accountability

### Processing Description

[Brief, plain-language description]

### Art. 35(3) Mandatory Trigger Analysis

| Trigger | Applies? | Reasoning |
[3 rows — all must be NOT APPLICABLE]

### Nine-Criteria Analysis

| # | Criterion | Applies? | Reasoning |
[9 rows]

### National Blacklist Analysis

| SA | List Reference | Match? | Reasoning |
[All relevant jurisdictions]

### Whitelist Exemptions Checked

[If applicable]

### Conclusion

DPIA not required. [Summary of reasoning.]
This memo is retained under Art. 5(2) GDPR to demonstrate accountability for this
processing decision. This analysis should be reviewed if the processing changes
materially.

**Prepared by:** [Name, role, date]
**DPO review:** [Name, date, opinion]
```

### Template 3: Art. 36 Consultation Package

```markdown
# GDPR ART. 36 PRIOR CONSULTATION

## [Processing Activity Name]

**Controller:** [Name, address, contact]
**DPO:** [Name, contact] (Art. 36(3)(d))
**EU Representative:** [If applicable] (Art. 36(3)(a))
**Addressed to:** [Lead SA name and address]
**Date:** [Date]
**DPIA Reference:** DPIA-[YYYY]-[NNN]
**Reference:** ART36-[YYYY]-[NNN]

**Note:** SA has 8 weeks to respond (extendable by 6 weeks for complex cases; Art. 36(2)).
Processing must not begin until SA response is received or response period has elapsed.

### 1. Respective Responsibilities (Art. 36(3)(a))

[Controller/joint controller/processor responsibilities]

### 2. Processing Description (Art. 36(3)(b))

[Purposes and means]

### 3. Measures and Safeguards (Art. 36(3)(c))

[All mitigations applied; why very high residual risk remains]

### 4. Residual Risks Requiring Consultation

| Risk ID | Description | Residual Score | Level | Why Cannot Be Further Mitigated |
| ------- | ----------- | -------------- | ----- | ------------------------------- |

### 5. DPO Contact (Art. 36(3)(d))

[Name, email, telephone]

### 6. DPIA Summary (Art. 36(3)(e))

[Condensed key findings — refer to full DPIA as Annex 1]

### 7. Other Information (Art. 36(3)(f))

[Transfer assessment, processor arrangements, sector-specific considerations]

### Attachments

1. Full DPIA Report (DPIA-[YYYY]-[NNN])
2. Data flow diagram
3. ROPA extract (Art. 30)
4. Processor agreements (Art. 28 DPAs)
5. Transfer documentation (SCCs, TIA)
```

---

## Localization Notes

This skill covers EU/EEA DPIAs with national SA variations. Key localization points:

**Germany (DSK):**

- DSK has separate guidance for employee monitoring — specific blacklist entries for DLP,
  keyloggers, GPS tracking, and email monitoring
- German Beschäftigtendatenschutzgesetz (Employment Data Protection Act) proposals
  [VERIFY current legislative status] may impose additional requirements
- State-level DPAs (Landesdatenschutzbehörden) may have additional sector guidance

**France (CNIL):**

- CNIL's list has 14 mandatory DPIA categories — one of the most comprehensive in the EU
- CNIL publishes DPO registration requirements; DPOs must be registered at connexion.pro.cnil.fr
- CNIL's PIA software (CNIL PIA tool) provides a structured methodology aligned with WP 248
- AI systems: CNIL has published guidance on AI and GDPR — check current publications

**Netherlands (AP):**

- AP has published sector-specific guidance for health data and child data
- AP enforcement has been active on AI systems in government/public sector

**Ireland (DPC):**

- DPC is Lead SA for many US tech multinationals with EU headquarters in Ireland
- DPC publishes updated blacklist and sector guidance; check dpc.ie
- DPC's Art. 36 submissions process is documented on its website

**Belgium (APD):**

- APD Entry 1 (biometric data processing) has a low threshold — applies to any biometric
  processing regardless of scale
- APD has been active on cookie consent enforcement

**Italy (Garante):**

- Garante requires specific DPO registration for health data controllers
- Garante has published guidance on AI and automated decisions in employment contexts
- Italian processing in the public sector may have specific requirements under national law

**Poland (UODO):**

- UODO has been active in enforcement on employee monitoring and CCTV
- Polish implementation law (UODO Act) includes specific provisions on employee data
- Working time and location monitoring blacklist entries are actively enforced

**Sector-Specific Notes:**

- Health data across all EU SAs: subject to additional national health sector legislation
  alongside GDPR — always check applicable sector laws [JURISDICTION-SPECIFIC]
- Financial sector: DPIA requirements interact with DORA (Regulation (EU) 2022/2554) for
  ICT risk management — ICT-related DPIAs should reference DORA requirements
- Public sector: Art. 37 mandates DPO for public authorities; public processing often has
  specific legal bases in national administrative law

---

## Provenance

Created by Legalcode, 2026-03-22. Mode A (create from scratch) — Legalcode original synthesis.

This skill synthesizes:

- **Imported DPIA Sentinel** (Oliver Schmidt-Prietz, AGPL-3.0): EDPB nine-criteria analysis,
  legal precision points, multi-jurisdictional framework, risk catalog, scoring methodology,
  and document template structure — reproduced in adapted form with attribution
- **EDPB Guidelines WP 248 rev.01**: Nine criteria, Art. 35(3) mandatory triggers, Annex 2
  minimum DPIA requirements
- **EDPB Opinion 28/2024**: AI/ML dual-phase DPIA analysis framework
- **EDPB Guidelines 01/2025 on Pseudonymisation**: Updated mitigation effectiveness guidance
- **Legalcode DPIA Generator** (general/compliance/legalcode-dpia-generator): General
  workflow structure and quality framework patterns
- **Legalcode Contract Review** (legalcode-contract-review): Quality assurance framework
  patterns (Citation Quality Gates, Self-Interrogation, Confidence Scoring, Glass Box audit
  trail, anti-patterns catalogue, writing standards)
- **EU DSA/DMA/CSRD Compliance Skills**: EU-specific skill structural patterns and frontmatter
  conventions

**This skill replaces the imported `imported-lawvable-dpia-sentinel` as the native Legalcode
DPIA assessment tool for EU/EEA processing activities.**
