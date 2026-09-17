---
name: legalcode-trade-secret-audit
description: 'Audit an organization''s trade secret protection program against US DTSA (18 U.S.C. §§ 1836–1839),
  state UTSA variations, and EU Trade Secrets Directive 2016/943. Conducts a comprehensive crown-jewels
  identification, reasonable-measures gap analysis, contractual portfolio review, employee-departure-protocol
  assessment, and litigation-readiness evaluation. Produces a severity-scored findings register, prioritized
  remediation roadmap, and Glass Box audit trail. Use when assessing trade secret program strength before
  litigation, M&A due diligence, regulatory review, or proactive compliance improvement. Also triggers
  for: "trade secret audit," "reasonable measures assessment," "crown jewels identification," "trade secret
  protection review," "inevitable disclosure analysis," "DTSA compliance check," "EU Trade Secrets Directive
  gap analysis," "employee departure trade secret risk," "misappropriation risk assessment," or "trade
  secret litigation readiness."'
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode Trade Secret Audit

> **Disclaimer**: This skill provides a framework for AI-assisted trade secret program
> assessment. It does not constitute legal advice. All outputs should be reviewed by a
> qualified legal professional licensed in the relevant jurisdiction before use. Statutory
> references and case citations carry hallucination risk — verify against authoritative
> sources (Westlaw, LexisNexis, EUR-Lex, or equivalent) before relying on them. Trade
> secret law is intensely fact-specific and jurisdiction-dependent; this skill provides
> analytical structure, not legal conclusions.

---

## Purpose and Scope

This skill audits an organization's trade secret protection program across six domains:
(1) crown jewels identification, (2) reasonable measures (physical, IT, HR, contractual),
(3) contractual portfolio, (4) employee departure protocols, (5) litigation readiness, and
(6) M&A and third-party risk. It produces a severity-scored findings register and a
prioritized remediation roadmap.

**Covers:**

- Crown jewels identification and classification (Tier 1–4 asset register)
- Reasonable measures gap analysis under DTSA § 1839(3), UTSA § 1(4), and EU Directive Art. 2(1)
- Physical security, IT/DLP, HR program, and contractual portfolio assessment
- Employee departure protocol audit (pre-, during-, and post-departure)
- Inevitable disclosure doctrine exposure (jurisdiction-dependent)
- Whistleblower immunity compliance (DTSA § 1833(b))
- M&A and third-party trade secret risk
- Misappropriation remedies overview (injunctive relief, damages, exemplary damages)
- Litigation readiness scoring
- AI/ML-specific trade secret considerations

**Does not:**

- Provide legal advice or replace qualified trade secret counsel
- Conduct forensic investigation of suspected misappropriation (a separate engagement)
- Draft non-disclosure agreements, employment agreements, or restrictive covenants
- Perform technical source code or formula analysis
- Apply exclusively to one jurisdiction — jurisdiction-specific content is marked [JURISDICTION-SPECIFIC]

---

## Jurisdiction and Governing Law

This skill is designed for **US/EU primary coverage** with jurisdiction-agnostic markers
for other common law and civil law systems.

| Jurisdiction                | Primary Legal Framework                                                                                     |
| --------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **United States (Federal)** | Defend Trade Secrets Act (DTSA), 18 U.S.C. §§ 1836–1839 (enacted May 11, 2016)                              |
| **United States (State)**   | Uniform Trade Secrets Act (UTSA) — adopted in 48 states; CA, TX, NY, DE, IL, MA have significant variations |
| **European Union**          | Trade Secrets Directive 2016/943/EU (transposed across EU member states)                                    |
| **Germany**                 | Geschäftsgeheimnisgesetz (GeschGehG) 2019 — EU Directive implementing act                                   |
| **France**                  | Loi no. 2018-670 (Code de Commerce Art. L. 151-1 et seq.)                                                   |
| **UK (post-Brexit)**        | No single statute; common law + equitable obligations; draft legislation pending [VERIFY current status]    |
| **Other common law**        | [JURISDICTION-SPECIFIC] Equitable obligations of confidence; adapt to local statutory overlay               |
| **Other civil law**         | [JURISDICTION-SPECIFIC] Civil code obligations + local transpositions of EU Directive where applicable      |

[JURISDICTION-SPECIFIC] **State-by-state US variations**: California rejects the inevitable
disclosure doctrine (Whyte v. Schlage Lock Co. (2002)); Texas applies it (M-I LLC v. Stelly);
New York is mixed; Delaware is favorable to employers on reasonable measures. Always identify
the applicable state law, as federal DTSA and state UTSA may both apply concurrently.

[JURISDICTION-SPECIFIC] **EU post-Brexit note**: UK courts apply equitable principles from
Saltman Engineering Co. v. Campbell Engineering Co. [1963] and Coco v. AN Clark (Engineers)
Ltd [1969] (three-element test: information has necessary quality of confidence, imparted in
circumstances of confidence, unauthorized use causing detriment). No EU Directive transposition
in UK. [VERIFY: UK Trade Secrets Bill status as of date of audit]

---

## Interactive Clarification

This skill uses **interactive clarification** (marked **⟁ CLARIFY**) at key decision points.
Rather than assuming context, the workflow pauses when:

- The audit scope would materially change based on the answer
- Industry-specific or jurisdiction-specific customization is needed
- Risk tolerance or deal context affects severity classification
- Gaps in the user's documentation require a different analytical approach

If the user has already provided the information, skip the question and proceed.

---

## Workflow

### Step 1: Accept the Engagement Scope

Accept the engagement context in any of these formats:

- **Document package**: Trade secret policies, NDA templates, employment agreements, IT security policies, classification policies, audit reports, organizational charts
- **Questionnaire responses**: Answers to the intake questions below
- **Prior audit findings**: Previous trade secret audit reports to update or verify
- **M&A context**: Target company materials for acquisition due diligence
- **Litigation context**: Pre-litigation assessment of trade secret claim strength
- **Free description**: User describes the organization and situation in natural language

If no materials are provided, proceed with the intake questionnaire in Step 2.

### Step 2: Gather Context

**⟁ CLARIFY** — Ask the following questions before beginning. Present as a structured intake:

1. **Organization type and industry**:
   - Options: Technology/Software, Pharmaceutical/Biotech, Manufacturing, Financial Services,
     Consumer Products, Professional Services, Other
   - _Why it matters_: Industry determines which assets are crown jewels and which regulatory
     overlays apply (FDA, HIPAA, export controls, etc.).

2. **Primary jurisdiction(s)**:
   - Options: US only, US + EU, EU only, US + specific states, Global (specify key jurisdictions), Other
   - _Why it matters_: Determines applicable statutory framework, inevitable disclosure
     doctrine applicability, and NDA enforceability rules.

3. **Audit trigger**:
   - Options: Proactive/preventive program review, M&A due diligence (buy-side), M&A due
     diligence (sell-side), Pre-litigation readiness, Post-departure incident investigation,
     Regulatory requirement, Board/investor request
   - _Why it matters_: The trigger determines depth, sequencing, and report format.

4. **Organization size**:
   - Options: Startup (1–50), Small (51–250), Mid-market (251–2,500), Large (2,500–25,000),
     Enterprise (25,000+)
   - _Why it matters_: Scales the audit expectations; a startup with no DLP is different
     from an enterprise with no DLP.

5. **Available documentation** (check all that exist):
   - [ ] Trade secret register / IP asset register
   - [ ] Written information classification policy
   - [ ] IT security policies (DLP, access control, encryption)
   - [ ] Employee NDA templates
   - [ ] Contractor/consultant NDA templates
   - [ ] Vendor NDA templates
   - [ ] Employee offboarding checklist
   - [ ] Exit interview protocol
   - [ ] Trade secret training program
   - [ ] Prior trade secret audits or assessments
   - _Why it matters_: Documentation availability shapes Phase 1 asset identification depth.

6. **Focus areas** (if any):
   - Options: Full audit (all six domains), Reasonable measures only, Employee departure
     protocols only, Contractual portfolio only, Litigation readiness only, M&A due diligence
     focus, AI/ML assets focus
   - _Why it matters_: Allows scoped audits when time or scope is constrained.

7. **Recent events** (if any):
   - [ ] Recent high-risk employee departure to competitor
   - [ ] Active or threatened trade secret litigation
   - [ ] M&A transaction (buy-side or sell-side)
   - [ ] Significant cybersecurity incident
   - [ ] Workforce reduction or restructuring
   - [ ] Joint venture or partnership with a competitor
   - _Why it matters_: Recent events trigger elevated scrutiny of specific domains.

### Step 3: Load Legal Framework

Read the applicable legal framework for the identified jurisdiction(s). Use **legalcode-mcp**
to gather verified legal authority.

**Search legalcode-mcp** for:

- DTSA § 1836–1839 current text and recent amendments [VERIFY]
- Applicable state UTSA — the state's specific version and notable divergences from the 1985 or 1995 uniform act
- EU Trade Secrets Directive 2016/943 and relevant implementing legislation
- Leading case law on reasonable measures in the applicable jurisdiction (see Case Law Reference below)
- Recent appellate decisions on inevitable disclosure doctrine in the applicable state
- DTSA § 1833(b) whistleblower immunity requirements

Save key findings to `/tmp/legalcode-trade-secret-authority.md`.

**If legalcode-mcp is not connected**: Mark all statutory and case law references [VERIFY].
Note in the Glass Box audit trail: `legalcode_mcp: "Not connected"`.

### Step 4: Crown Jewels Identification

Identify and classify the organization's trade secret assets before assessing how well they
are protected. An organization cannot prove reasonable measures without first identifying
what it is protecting.

**⟁ CLARIFY** — If no trade secret register exists, prompt the user to identify crown jewels
across these asset categories:

| Asset Category                 | Examples                                                                         | Typical Classification                  |
| ------------------------------ | -------------------------------------------------------------------------------- | --------------------------------------- |
| Formulas and compositions      | Drug formulas, food recipes, chemical compositions, material specifications      | Tier 1 Trade Secret                     |
| Source code and algorithms     | Proprietary software, ML model architectures, trading algorithms, search ranking | Tier 1 Trade Secret                     |
| Technical processes            | Manufacturing methods, purification processes, assembly techniques               | Tier 1 Trade Secret                     |
| Customer and prospect data     | Customer lists, pricing history, usage patterns, contract terms                  | Tier 1–2 depending on compilation value |
| Business and financial         | Strategic plans, pricing models, M&A pipeline, financial projections             | Tier 2 Trade Secret                     |
| Research and development       | Pre-publication research, clinical trial data, experimental results              | Tier 1–2                                |
| Know-how and negative know-how | "What doesn't work" knowledge, failed approach documentation                     | Tier 2 Trade Secret                     |
| Personnel information          | Compensation structures, performance data, organizational plans                  | Tier 2–3                                |
| Supplier and vendor data       | Supplier identities, pricing, performance data, sourcing strategies              | Tier 2–3                                |

**Crown Jewels Identification Techniques**:

1. **Value-Secrecy Matrix**: Plot each asset on two axes: (a) competitive damage if disclosed
   to a competitor, (b) current degree of secrecy. High-value, high-secrecy = Tier 1 crown jewels.

2. **Reconstruction Cost Test**: What would it cost a competitor to independently develop
   this information? Reconstruction cost exceeding $1M or 12 months of R&D suggests Tier 1.

3. **Loss-of-Advantage Test**: What would happen to the company's competitive position if
   this information became public tomorrow? If the answer is "material harm to market position,"
   it is a crown jewel.

4. **Competitor-Interest Test**: What information do sophisticated competitor recruiters and
   intelligence operations specifically seek? This is often the crown jewels.

5. **DTSA Particularity Screen**: Could the organization identify this information with
   sufficient particularity to survive a motion to dismiss a misappropriation claim? If not,
   the information may lack the specificity required under DTSA / UTSA.

**Classification Tiers**:

| Tier       | Label                               | Criteria                                                                                                       | Example Controls                                                                               |
| ---------- | ----------------------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Tier 1** | Trade Secret / Highly Confidential  | Highest competitive value; reconstruction cost >$1M or competitive damage >$10M; existential to business value | Need-to-know only; separate access controls; enhanced DLP; logged access; marked on every page |
| **Tier 2** | Confidential / Internal Proprietary | Commercially sensitive; competitive advantage but not existential                                              | Role-based access; standard DLP; marked on documents; covered by standard NDAs                 |
| **Tier 3** | Internal Use Only                   | Non-public but not commercially sensitive; business operations                                                 | General employee access; not shared externally without authorization                           |
| **Tier 4** | Public / Unrestricted               | Cleared for external disclosure; no competitive value from secrecy                                             | No restriction                                                                                 |

**CRITICAL CHECK**: A court will dismiss a trade secret claim if the plaintiff cannot
identify the trade secret with particularity before discovery. Document each Tier 1 and
Tier 2 asset with: (a) description, (b) date of creation/acquisition, (c) competitive value
basis, (d) measures taken to protect it, (e) persons who have access.

### Step 5: Reasonable Measures Assessment

Assess whether the organization has taken "reasonable measures" to maintain secrecy — the
threshold legal requirement under DTSA § 1839(3)(A), UTSA § 1(4)(ii), and EU Directive
Art. 2(1)(b).

**The legal standard**: Courts apply a fact-intensive, context-dependent analysis. There is
no fixed list of required measures; courts ask whether the measures taken were reasonable
under the circumstances. Key principle from _Rockwell Graphic Systems, Inc. v. DEV
Industries, Inc._, 925 F.2d 174 (7th Cir. 1991): perfection is not required, but a
meaningful effort must be shown. Courts weigh the value of the secret against the cost
of protection.

#### 5a. Physical Security Assessment

| Control                                                                        | Present?             | Consistent? | Finding |
| ------------------------------------------------------------------------------ | -------------------- | ----------- | ------- |
| Restricted access to facilities where trade secret work occurs (badge/keycard) | ☐ Yes ☐ No ☐ Partial |             |         |
| Visitor sign-in, escort, and visitor NDAs for sensitive areas                  | ☐ Yes ☐ No ☐ Partial |             |         |
| "Authorized Personnel Only" signage on restricted areas                        | ☐ Yes ☐ No ☐ Partial |             |         |
| Locked storage for physical documents, samples, and prototypes                 | ☐ Yes ☐ No ☐ Partial |             |         |
| Shredding and secure destruction protocols for physical materials              | ☐ Yes ☐ No ☐ Partial |             |         |
| Clean desk policy for crown jewel work areas                                   | ☐ Yes ☐ No ☐ Partial |             |         |
| Security cameras covering sensitive areas                                      | ☐ Yes ☐ No ☐ Partial |             |         |
| Prohibition on photography or recording in restricted areas                    | ☐ Yes ☐ No ☐ Partial |             |         |
| Separate secure zones for R&D, server rooms, prototyping                       | ☐ Yes ☐ No ☐ Partial |             |         |

#### 5b. IT and Digital Security Assessment

**Access Controls:**
| Control | Present? | Consistent? | Finding |
|---|---|---|---|
| Role-based access control (RBAC) for systems containing trade secrets | ☐ Yes ☐ No ☐ Partial | | |
| Principle of least privilege — employees access only what they need | ☐ Yes ☐ No ☐ Partial | | |
| Multi-factor authentication (MFA) for crown jewel systems | ☐ Yes ☐ No ☐ Partial | | |
| Privileged access management (PAM) for admin-level access | ☐ Yes ☐ No ☐ Partial | | |
| Access reviews conducted at least annually | ☐ Yes ☐ No ☐ Partial | | |
| Logging and monitoring of access to crown jewel repositories | ☐ Yes ☐ No ☐ Partial | | |
| Contractor and vendor access time-limited and revoked promptly | ☐ Yes ☐ No ☐ Partial | | |

**Data Loss Prevention (DLP):**
| Control | Present? | Consistent? | Finding |
|---|---|---|---|
| DLP tools monitoring email, web upload, USB, and cloud sync | ☐ Yes ☐ No ☐ Partial | | |
| Content-aware DLP policies based on document classification | ☐ Yes ☐ No ☐ Partial | | |
| Alerting on anomalous bulk downloads or access patterns | ☐ Yes ☐ No ☐ Partial | | |
| USB and removable media restrictions for crown jewel systems | ☐ Yes ☐ No ☐ Partial | | |
| Blocking or watermarking of highly confidential documents when printed | ☐ Yes ☐ No ☐ Partial | | |

**Encryption and Device Management:**
| Control | Present? | Consistent? | Finding |
|---|---|---|---|
| Encryption at rest for systems containing trade secrets | ☐ Yes ☐ No ☐ Partial | | |
| Encryption in transit (TLS) for all crown jewel transmissions | ☐ Yes ☐ No ☐ Partial | | |
| Full disk encryption on laptops used for crown jewel work | ☐ Yes ☐ No ☐ Partial | | |
| Mobile Device Management (MDM) for devices accessing crown jewels | ☐ Yes ☐ No ☐ Partial | | |
| BYOD policy restrictions for crown jewel work | ☐ Yes ☐ No ☐ Partial | | |
| Remote wipe capability for devices containing trade secrets | ☐ Yes ☐ No ☐ Partial | | |

**Pre/Post-Departure Monitoring:**
| Control | Present? | Consistent? | Finding |
|---|---|---|---|
| User Activity Monitoring (UAM) for employees in notice period | ☐ Yes ☐ No ☐ Partial | | |
| Anomaly detection for large file downloads near departure dates | ☐ Yes ☐ No ☐ Partial | | |
| Forensic imaging of company devices returned by departing employees | ☐ Yes ☐ No ☐ Partial | | |

#### 5c. HR Program Assessment

**At Hire:**
| Control | Present? | Consistent? | Finding |
|---|---|---|---|
| NDA / confidentiality agreement signed **before** start date | ☐ Yes ☐ No ☐ Partial | | |
| Inventions assignment agreement at hire | ☐ Yes ☐ No ☐ Partial | | |
| Representation re: prior employer confidential information ("no importation") | ☐ Yes ☐ No ☐ Partial | | |
| Trade secret awareness training within first 30 days | ☐ Yes ☐ No ☐ Partial | | |
| Acknowledgment of classification policy | ☐ Yes ☐ No ☐ Partial | | |

**During Tenure:**
| Control | Present? | Consistent? | Finding |
|---|---|---|---|
| Annual trade secret training refresher | ☐ Yes ☐ No ☐ Partial | | |
| Restrictive covenant agreements with adequate consideration | ☐ Yes ☐ No ☐ Partial | | |
| Access provisioning tied to role (not legacy broad access) | ☐ Yes ☐ No ☐ Partial | | |
| Access reviewed and adjusted on role changes | ☐ Yes ☐ No ☐ Partial | | |
| Elevated monitoring for at-risk employees (notice period, disgruntled, recruited) | ☐ Yes ☐ No ☐ Partial | | |

**At Exit:**
| Control | Present? | Consistent? | Finding |
|---|---|---|---|
| Exit interview conducted by trained personnel | ☐ Yes ☐ No ☐ Partial | | |
| Exit certification signed (return of all materials, continuing obligations reminder) | ☐ Yes ☐ No ☐ Partial | | |
| IT deactivation same day or immediately on departure | ☐ Yes ☐ No ☐ Partial | | |
| Return of all company property (checklist signed) | ☐ Yes ☐ No ☐ Partial | | |
| Garden leave provision for senior/crown-jewel-access employees | ☐ Yes ☐ No ☐ Partial | | |

#### 5d. Classification and Marking Program Assessment

| Control                                                    | Present?             | Consistent? | Finding |
| ---------------------------------------------------------- | -------------------- | ----------- | ------- |
| Written classification policy exists and is current        | ☐ Yes ☐ No ☐ Partial |             |         |
| Policy defines each tier with clear criteria               | ☐ Yes ☐ No ☐ Partial |             |         |
| Documents marked on every page (not just cover pages)      | ☐ Yes ☐ No ☐ Partial |             |         |
| Electronic DMS enforces or supports classification         | ☐ Yes ☐ No ☐ Partial |             |         |
| Document templates include classification markings         | ☐ Yes ☐ No ☐ Partial |             |         |
| Classification reviewed before any external sharing        | ☐ Yes ☐ No ☐ Partial |             |         |
| Process for declassification/reclassification exists       | ☐ Yes ☐ No ☐ Partial |             |         |
| Classification training in onboarding and annual refresher | ☐ Yes ☐ No ☐ Partial |             |         |

**⟁ CLARIFY** — If documents are not consistently marked, ask: "Are employees instructed
to apply 'Confidential' markings when in doubt, or do they apply markings only on explicit
direction?" Absence of a default-to-confidential instruction is a HIGH finding.

### Step 6: Contractual Portfolio Review

Assess whether the organization's contract portfolio provides adequate legal protection
for trade secrets.

**⟁ CLARIFY** — If no contracts are available for review, perform a policy-level assessment
of whether the types of agreements described below are systematically in place.

#### 6a. Employee Agreements

| Agreement Type                    | Coverage                                                                                                                                                                                                              | Gap Analysis |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **Confidentiality / NDA**         | All employees with access to Tier 1–2 assets? Signed before start (not after)?                                                                                                                                        |              |
| **Inventions Assignment**         | Assigns all work-product inventions to employer? [JURISDICTION-SPECIFIC: carve-outs required in CA (Lab. Code § 2870), DE, MN, IL, WA, NC]                                                                            |              |
| **Non-compete**                   | [JURISDICTION-SPECIFIC] Reasonable scope/duration/geography for the applicable state? Post-FTC rule vacatur: enforceable in most states except CA, MN, ND, OK, and others. Adequate consideration?                    |              |
| **Non-solicitation (employees)**  | Scope of prohibited solicitation (direct recruit only vs. "encouraging to leave")? Duration?                                                                                                                          |              |
| **Non-solicitation (customers)**  | Limited to customers the employee actually served? Reasonable duration?                                                                                                                                               |              |
| **Whistleblower Immunity Notice** | DTSA § 1833(b) immunity notice included in any agreement governing confidential information (or in a policy cross-referenced)? [CRITICAL: absence forfeits right to exemplary damages and attorneys' fees under DTSA] |              |

**DTSA § 1833(b) Whistleblower Immunity — Critical Compliance Point**:
An employer that fails to provide the required immunity notice "in any contract or
agreement with an employee that is entered into or updated after the date of enactment"
(May 11, 2016) **forfeits the right to exemplary damages and attorneys' fees** in a DTSA
action, even if the misappropriation is willful. [18 U.S.C. § 1833(b)(3)] [VERIFY current
text]. Review ALL employment agreements, contractor agreements, and NDAs entered after
May 11, 2016 for this notice.

#### 6b. Vendor and Supplier Agreements

| Agreement Type                        | Coverage                                                                                                                  | Gap Analysis |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **Vendor NDA**                        | Required before any disclosure of Tier 1–2 information to vendors?                                                        |              |
| **NDA term**                          | Indefinite (preferred) or time-limited for trade secrets? A time-limited NDA may not adequately protect trade secrets     |              |
| **Return/destruction clause**         | Requires return or destruction of confidential information on termination?                                                |              |
| **Audit rights**                      | Allows audit of vendor's compliance with confidentiality obligations?                                                     |              |
| **Onward disclosure restriction**     | Prohibits vendor from sharing the organization's confidential information with sub-vendors or affiliates without consent? |              |
| **Information security requirements** | Vendor required to maintain specified security standards for the organization's information?                              |              |

#### 6c. Consulting and Contractor Agreements

| Agreement Type                     | Coverage                                                         | Gap Analysis |
| ---------------------------------- | ---------------------------------------------------------------- | ------------ |
| **NDA**                            | Signed before engagement begins?                                 |              |
| **Work-for-hire / IP assignment**  | All developed IP assigned to organization?                       |              |
| **Non-solicitation**               | Reasonable scope?                                                |              |
| **Access limitation**              | Access limited to what is necessary for the specific engagement? |              |
| **DTSA § 1833(b) immunity notice** | Included? (applies to contractors as well as employees)          |              |

#### 6d. Customer Agreements

| Agreement Type                    | Coverage                                                                   | Gap Analysis |
| --------------------------------- | -------------------------------------------------------------------------- | ------------ |
| **Mutual NDA**                    | In place before sharing product roadmaps, technical specs, pricing models? |              |
| **Onward disclosure restriction** | Prohibits sharing with customer's affiliates without consent?              |              |
| **"Confidential" marking**        | Materials shared with customers marked appropriately?                      |              |

#### 6e. M&A and Partnership Agreements

| Agreement Type                         | Coverage                                                                                       | Gap Analysis |
| -------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------ |
| **Clean room protocol**                | For competitively sensitive information in M&A due diligence?                                  |              |
| **Standstill and non-use**             | Prohibits use of disclosed information except for deal evaluation?                             |              |
| **Return/destruction on deal failure** | Requires return or destruction if transaction does not close?                                  |              |
| **IP ownership in collaboration**      | Background vs. foreground IP clearly delineated in joint ventures and research collaborations? |              |
| **Publication approval rights**        | Prevents disclosure of jointly developed information via academic publication without consent? |              |

### Step 7: Employee Departure Protocol Assessment

Departing employees represent the highest-frequency vector for trade secret misappropriation.
Assess the organization's departure protocol against best practices.

**⟁ CLARIFY** — If a specific departure is under review, ask:

- When did the employee depart (or when is the expected departure date)?
- What level of crown jewel access did the employee have (Tier 1, 2, or 3)?
- Is the successor employer known? If so, is it a direct competitor?
- Were any anomalies detected in the employee's access behavior before departure?

#### 7a. Pre-Departure Phase Assessment

| Protocol Element                                                                             | Present?             | Finding |
| -------------------------------------------------------------------------------------------- | -------------------- | ------- |
| IT security / HR / Legal notified immediately on notice of departure                         | ☐ Yes ☐ No ☐ Partial |         |
| User Activity Monitoring (UAM) activated for notice period                                   | ☐ Yes ☐ No ☐ Partial |         |
| Retroactive review of access logs (30–90 days before notice)                                 | ☐ Yes ☐ No ☐ Partial |         |
| Anomaly detection run: bulk downloads, unusual access, email forwarding to personal accounts | ☐ Yes ☐ No ☐ Partial |         |
| Access rights reviewed and restricted as appropriate during notice period                    | ☐ Yes ☐ No ☐ Partial |         |
| Restrictive covenant agreements reviewed to determine scope of post-departure obligations    | ☐ Yes ☐ No ☐ Partial |         |
| Successor employer identified and assessed for competitive risk                              | ☐ Yes ☐ No ☐ Partial |         |

#### 7b. Departure Day Protocol Assessment

| Protocol Element                                                                                      | Present?             | Finding |
| ----------------------------------------------------------------------------------------------------- | -------------------- | ------- |
| Exit interview conducted by trained HR / counsel                                                      | ☐ Yes ☐ No ☐ Partial |         |
| Employee reminded of all signed confidentiality and restrictive covenant agreements (copies provided) | ☐ Yes ☐ No ☐ Partial |         |
| Employee asked to identify all company information in their possession                                | ☐ Yes ☐ No ☐ Partial |         |
| Direct question asked re: copying/transfer of confidential information to personal devices/accounts   | ☐ Yes ☐ No ☐ Partial |         |
| Exit certification signed                                                                             | ☐ Yes ☐ No ☐ Partial |         |
| Return of all company property (checklist itemized and signed)                                        | ☐ Yes ☐ No ☐ Partial |         |
| IT access revoked same day (email, VPN, SaaS, code repo, database)                                    | ☐ Yes ☐ No ☐ Partial |         |
| Employee accounts disabled (not deleted) for preservation                                             | ☐ Yes ☐ No ☐ Partial |         |
| Returned devices forensically imaged before repurposing                                               | ☐ Yes ☐ No ☐ Partial |         |
| Shared account passwords changed                                                                      | ☐ Yes ☐ No ☐ Partial |         |

#### 7c. Post-Departure Phase Assessment

| Protocol Element                                                                                                             | Present?             | Finding |
| ---------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------- |
| Forensic preservation of returned devices (minimum 12 months for standard employees; indefinite for Tier 1 access employees) | ☐ Yes ☐ No ☐ Partial |         |
| Network access logs monitored for post-departure unauthorized access attempts                                                | ☐ Yes ☐ No ☐ Partial |         |
| Background investigation triggered when successor employer is direct competitor + Tier 1 access                              | ☐ Yes ☐ No ☐ Partial |         |
| Letter sent to departing employee reminding of obligations (where successor employer is known competitor)                    | ☐ Yes ☐ No ☐ Partial |         |
| Litigation hold triggered if misappropriation evidence found                                                                 | ☐ Yes ☐ No ☐ Partial |         |

#### 7d. Inevitable Disclosure Doctrine Analysis

[JURISDICTION-SPECIFIC] The inevitable disclosure doctrine allows a court to enjoin a
former employee from working for a competitor even absent direct evidence of misappropriation,
on the theory that the employee "inevitably" will use or disclose trade secrets in the new role.

| Jurisdiction Posture             | States / Status                                                                                                                                                                                                       |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Accept inevitable disclosure** | Illinois (_PepsiCo, Inc. v. Redmond_, 54 F.3d 1262 (7th Cir. 1995)); Texas (_M-I LLC v. Stelly_, 2009); Pennsylvania (limited) [VERIFY]                                                                               |
| **Reject inevitable disclosure** | California (_Whyte v. Schlage Lock Co._ (2002) 101 Cal.App.4th 1443); New York (split — _EarthWeb, Inc. v. Schlack_ (S.D.N.Y. 1999) skeptical); [VERIFY state-specific current status]                                |
| **EU Directive position**        | Directive Art. 9 allows "preventive" injunctions to prevent imminent misappropriation; does not explicitly adopt inevitable disclosure but permits preventive relief [VERIFY implementation in specific member state] |

**When assessing inevitable disclosure exposure**:

- Identify the new role: is the employee in a position where trade secret use is genuinely inevitable?
- Assess specificity of trade secrets: broad categories (e.g., "marketing strategies") are harder to protect; specific technical formulas are stronger candidates
- Review restrictive covenants: a valid non-compete in an enforcement-friendly jurisdiction is the stronger remedy

### Step 8: Litigation Readiness Assessment

Assess whether the organization's documentation is sufficient to **prove** reasonable measures
in litigation — distinct from whether measures exist.

Courts require proof that is: (1) specific (names specific assets, controls, and policies),
(2) documented (paper trail exists), and (3) consistently enforced (not merely paper policies).

#### 8a. Trade Secret Asset Register

| Criterion                                                                                                 | Present?             | Finding |
| --------------------------------------------------------------------------------------------------------- | -------------------- | ------- |
| Maintained register identifying each Tier 1–2 trade secret                                                | ☐ Yes ☐ No ☐ Partial |         |
| Each entry includes: description, date created/acquired, competitive value basis, access controls applied | ☐ Yes ☐ No ☐ Partial |         |
| Register updated at least annually                                                                        | ☐ Yes ☐ No ☐ Partial |         |
| Register is itself maintained as a confidential document                                                  | ☐ Yes ☐ No ☐ Partial |         |

#### 8b. Documentation of Measures

| Document                                                                              | Present?             | Finding |
| ------------------------------------------------------------------------------------- | -------------------- | ------- |
| Written policies governing physical, IT, and HR security (with version history)       | ☐ Yes ☐ No ☐ Partial |         |
| Training completion records (every employee, every year)                              | ☐ Yes ☐ No ☐ Partial |         |
| NDA execution records (signed copies for every employee, contractor, relevant vendor) | ☐ Yes ☐ No ☐ Partial |         |
| Access control logs (who accessed crown jewel systems and when)                       | ☐ Yes ☐ No ☐ Partial |         |
| Audit trails from DLP, IAM, and monitoring systems                                    | ☐ Yes ☐ No ☐ Partial |         |
| Prior incident records and organizational response                                    | ☐ Yes ☐ No ☐ Partial |         |
| Exit documentation (signed exit certifications)                                       | ☐ Yes ☐ No ☐ Partial |         |
| Enforcement records (evidence measures were enforced, not just on paper)              | ☐ Yes ☐ No ☐ Partial |         |

**⟁ CLARIFY** — If the organization has policies but enforcement is inconsistent, ask:
"Can you provide examples of the policy being enforced — e.g., a disciplinary action
for a classification violation, or an access revocation log?" Courts look skeptically at
paper policies that were not consistently enforced. Inconsistent enforcement is a HIGH or
CRITICAL finding depending on the frequency and significance.

#### 8c. DTSA Seizure Readiness

[JURISDICTION-SPECIFIC — US only] DTSA § 1836(b)(2) provides for an extraordinary
ex parte civil seizure order, available in extraordinary circumstances when a TRO would be
inadequate (e.g., the defendant is about to flee the country, or is unlikely to preserve
evidence in response to a TRO). Assessment:

| Element                                                                                 | Status     |
| --------------------------------------------------------------------------------------- | ---------- |
| Organization has access to qualified forensic vendor (pre-selected relationship)        | ☐ Yes ☐ No |
| Legal counsel experienced in emergency DTSA injunctive relief is identified             | ☐ Yes ☐ No |
| Evidence preservation protocol and litigation hold procedure exist                      | ☐ Yes ☐ No |
| Organization can document each element of a DTSA claim with specificity on short notice | ☐ Yes ☐ No |

### Step 9: AI/ML Trade Secret Considerations

AI and machine learning assets raise novel trade secret issues that the standard audit
framework may underweight.

**⟁ CLARIFY** — Ask: "Does the organization develop, use, or license AI/ML models or
training data assets?" If yes, assess the following:

| AI/ML Asset                                          | Trade Secret Issues                                                                                                                                                                               | Assessment Criteria                                                                                                    |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Training datasets**                                | Compilations can qualify as trade secrets if they derive independent economic value from secrecy and reasonable measures are taken. Key risk: datasets often processed by third-party AI vendors. | Is the training data disclosed to any third-party AI/ML vendor? Under what contractual terms?                          |
| **Model weights and architecture**                   | Model files (weights, hyperparameters, architecture) may qualify. Risk: public API access allows model extraction attacks.                                                                        | Are model weights stored with Tier 1 controls? Are APIs rate-limited and monitored for extraction behavior?            |
| **AI-generated improvements**                        | If an AI model generates improvements to an existing trade secret (e.g., an AI-optimized formula), who owns the improvement?                                                                      | Check assignment clauses in AI vendor contracts — many claim ownership of derived models.                              |
| **Third-party AI tool use (ChatGPT, Copilot, etc.)** | Employees inputting proprietary data into third-party AI tools may constitute unauthorized disclosure.                                                                                            | Does the acceptable use policy explicitly cover third-party AI tools? Is there a documented list of approved AI tools? |
| **Open source contamination**                        | AI model trained on open source data subject to GPL or similar "copyleft" conditions may require disclosure of training data or model weights.                                                    | Has a license compliance review been conducted for all training data sources?                                          |

---

## Severity Classification

Every audit finding is classified using the following four-tier system:

### CRITICAL — Existential Risk

Findings that directly threaten the legal existence of trade secret protection or expose
the organization to immediate and severe harm. Requires immediate action (within 5 business days).

**Automatic CRITICAL triggers**:

- Crown jewels publicly disclosed (website, conference, patent application, open source release) — **trade secret status destroyed**
- Active evidence of misappropriation with no preservation or litigation hold in place
- Complete absence of NDAs with employees having Tier 1 access
- No reasonable measures whatsoever (no classification, no access controls, no contractual obligations) — claim would not survive pleading stage
- Devices wiped or accounts deleted rather than preserved when misappropriation suspected
- DTSA § 1833(b) immunity notice absent from all agreements — **forfeits exemplary damages and attorneys' fees**
- Evidence of ongoing unauthorized disclosure (e.g., crown jewels currently accessible to unauthorized parties)

### HIGH — Material Risk

Findings that significantly weaken trade secret protection and legal position but do not
immediately destroy trade secret status. Requires remediation within 30 days.

**Automatic HIGH triggers**:

- Systematic NDA gaps: material population of Tier 1–2 access employees without executed NDAs
- No DLP or access logging for crown jewel systems
- No exit protocol for Tier 1 access employees (no exit interview, no forensic imaging, no UAM during notice period)
- Classification program absent or unenforced in practice
- No trade secret register — organization cannot identify secrets with specificity
- Known high-risk departure to competitor with no investigation and no responsive action
- DTSA § 1833(b) immunity notice absent from agreements signed after May 11, 2016
- IT access not revoked within 24 hours of departure for Tier 1 employees
- No forensic imaging of returned devices from Tier 1 access employees
- Vendor NDAs absent for vendors receiving Tier 1 information

### MEDIUM — Significant Gap

Findings that weaken the program in ways that may affect litigation position and leave
the organization exposed to incremental risk. Requires remediation within 90 days.

**Examples of MEDIUM findings**:

- Inconsistent classification marking (many documents unmarked or inconsistently marked)
- NDAs exist but signed after start date for some employees
- Annual trade secret training not completed by a material percentage of employees
- Access control reviews not conducted in the past 12 months
- Contractor/consultant NDA coverage incomplete (gaps, not systematic absence)
- No written acceptable use policy covering third-party AI tools
- M&A integration NDAs not updated after acquisition
- Non-compete agreements not reviewed for enforceability in applicable states following FTC rule developments
- Vendor audit rights absent from vendor NDAs

### LOW — Best Practice Gap

Findings that represent deviations from best practice but do not materially affect trade
secret status or litigation position. Remediate within 180 days or next policy review cycle.

**Examples of LOW findings**:

- Physical security at non-crown-jewel areas slightly below best practice
- Annual access review conducted every 14 months rather than 12
- Garden leave provisions absent in employment agreements (not universally required; jurisdiction-specific)
- Visitor NDA procedures not followed in offices without crown jewel access
- Document template classification markings absent on lower-sensitivity templates
- Training completion rate at 90% rather than 100%

---

## Remediation Framework

For each finding, generate a remediation action using this format:

```
**Finding ID**: [TS-001, TS-002, ...]
**Domain**: [Crown Jewels / Reasonable Measures / Contractual / Departure Protocol / Litigation Readiness / AI/ML]
**Severity**: [CRITICAL / HIGH / MEDIUM / LOW]
**Finding**: [Specific gap described in factual terms]
**Legal Risk**: [Specific legal consequence if not remediated — cite applicable provision or case]
**Remediation Action**: [Specific, actionable steps — not vague guidance]
**Owner**: [Legal / CISO / HR / Procurement / Corp Dev]
**Deadline**: [5 / 30 / 90 / 180 days based on severity]
**Litigation Readiness Impact**: [How this finding would affect the organization's position if a trade secret claim were filed today]
```

### Prioritization Framework

**Tier 1 — Do First** (CRITICAL findings; all within 5 business days):

- Preserve evidence of any suspected misappropriation
- Address trade-secret-destroying disclosures (remove publicly accessible crown jewels where possible)
- Execute NDAs with all Tier 1 access employees missing them
- Add DTSA § 1833(b) immunity notices to current agreements via amendment or policy cross-reference
- Activate forensic imaging for any pending high-risk departures

**Tier 2 — Do Next** (HIGH findings; all within 30 days):

- Implement systematic NDA execution tracking
- Deploy or expand DLP tooling for crown jewel systems
- Establish exit protocol for Tier 1 employees (written procedure, training, checklists)
- Create or update the trade secret register
- Ensure all Tier 1 agreements signed after May 2016 contain DTSA immunity notice

**Tier 3 — Roadmap** (MEDIUM findings; within 90 days):

- Roll out consistent classification marking program
- Conduct access control review sweep
- Complete NDA execution gap remediation for Tier 2 employees
- Update acceptable use policy for AI tools
- Review non-compete enforceability across applicable states

**Tier 4 — Policy Cycle** (LOW findings; within 180 days or next policy review):

- Best practice improvements to physical security
- Garden leave provision drafting
- Visitor NDA consistency improvements
- Training completion rate improvements

---

## Quality Assurance Framework

### Citation Quality Gates

Run these 5 gates silently before delivering any output:

| Gate           | Rule                                                                                                                                         | Fail Action                                              |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or established principle                                                             | Add citation or mark "[UNVERIFIED — counsel to confirm]" |
| **Format**     | Citations follow consistent format (DTSA: 18 U.S.C. § **_; EU: Directive 2016/943/EU Art. _**; case: [Name], [Citation] ([Year]))            | Fix format                                               |
| **Currency**   | Every cited provision checked for amendments or repeal; FTC rule and state non-compete law in particular are rapidly changing                | Flag "[CHECK CURRENCY]"                                  |
| **Domain**     | Analysis stays within identified jurisdiction(s); do not assume DTSA concepts (inevitable disclosure, ex parte seizure) apply in EU analysis | Remove or flag jurisdictional bleed                      |
| **Confidence** | Uncertainty explicitly stated, not hidden; trade secret law is intensely fact-specific                                                       | Add confidence qualifier                                 |

### Self-Interrogation for CRITICAL Findings

For any finding classified CRITICAL, apply this 3-pass review before delivering:

**Pass 1 — Legal Chain Integrity**:

- Does the risk assessment follow logically from the statute or case law cited?
- Would a court in this jurisdiction actually reach this conclusion on these facts?
- Is the "trade secret status destroyed" conclusion really warranted, or is the information merely weakened?

**Pass 2 — Completeness**:

- Have all available protective measures been considered? (An organization without a formal classification policy may still have enforceable NDAs and access controls.)
- Are there compensating controls that partially offset the gap?
- Have all relevant DTSA / UTSA / EU Directive elements been analyzed?

**Pass 3 — Challenge**:

- What is the strongest argument that this organization's measures ARE reasonable under the circumstances?
- Under what circumstances might a court accept a less formal program as "reasonable"? (Note: _Rockwell Graphic Systems_ suggests that even imperfect measures can satisfy the standard if the owner made a genuine effort.)
- Is CRITICAL classification proportionate, or should this be HIGH with expedited remediation?

### Confidence Scoring

| Level        | Range     | Meaning                                                        | Action                                                |
| ------------ | --------- | -------------------------------------------------------------- | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, clear statute, clear facts                        | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong authority, minor factual questions                      | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good arguments but fact-intensive; court could differ          | State with explicit reasoning and contra-indicators   |
| **Possible** | 0.40–0.59 | Genuinely uncertain — competing authorities or sparse case law | Flag for counsel review with both sides               |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                                        | Do not assert; flag "[UNCERTAIN — counsel to advise]" |

---

## Glass Box Audit Trail

Every trade secret audit output MUST include this section:

```yaml
glass_box:
  skill_name: "legalcode-trade-secret-audit"
  engagement_type: "[Proactive / M&A buy-side / M&A sell-side / Pre-litigation / Post-incident / Regulatory]"
  organization_type: "[Industry]"
  jurisdiction_primary: "[US / EU / US+EU / Other]"
  state_utsa: "[Applicable state(s) if US]"
  inevitable_disclosure_applies: "[Yes / No / Uncertain — state: ___]"
  crown_jewels_identified: "[Number of Tier 1 assets; Number of Tier 2 assets; 'Not identified']"
  reasonable_measures_domains_assessed: "[Physical / IT / HR / Contractual / Classification — list assessed]"
  total_findings: "[Number]"
  critical_findings: "[Number]"
  high_findings: "[Number]"
  medium_findings: "[Number]"
  low_findings: "[Number]"
  dtsa_immunity_notice_status: "[Compliant / Non-compliant / Partial / Not assessed]"
  legalcode_mcp: "[Connected / Not connected]"
  authority_reference_file: "[path or 'Not created']"
  statutes_consulted:
    - "18 U.S.C. §§ 1836–1839 (DTSA) — [VERIFIED / UNVERIFIED]"
    - "EU Directive 2016/943 — [VERIFIED / UNVERIFIED]"
    - "[State UTSA citation] — [VERIFIED / UNVERIFIED]"
  cases_consulted:
    - "[Case name and citation] — [VERIFIED / UNVERIFIED]"
  citations_verified: "[number VERIFIED] / [number UNVERIFIED]"
  self_interrogation: "[PASS / REVISED / NOT APPLICABLE (no CRITICAL items)]"
  confidence: "[HIGH / MEDIUM / LOW] — [rationale]"
  limitations:
    - "[Any scope limitations, assumptions, documentation gaps, or caveats]"
  reviewer: "AI-assisted — requires qualified trade secret counsel review"
```

---

## Case Law Reference

Key cases for reasonable measures and related trade secret issues [all citations require [VERIFY]]:

| Case                                              | Citation                           | Holding                                                                                                                                                        |
| ------------------------------------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| _PepsiCo, Inc. v. Redmond_                        | 54 F.3d 1262 (7th Cir. 1995)       | Recognized inevitable disclosure doctrine; enjoined executive from joining competitor                                                                          |
| _Whyte v. Schlage Lock Co._                       | 101 Cal.App.4th 1443 (2002)        | California rejects inevitable disclosure doctrine as inconsistent with Business & Professions Code § 16600                                                     |
| _Rockwell Graphic Systems v. DEV Industries_      | 925 F.2d 174 (7th Cir. 1991)       | Imperfect secrecy measures can suffice; owner need not take every conceivable precaution                                                                       |
| _EarthWeb, Inc. v. Schlack_                       | 71 F.Supp.2d 299 (S.D.N.Y. 1999)   | Skeptical of inevitable disclosure; emphasizes need for specific evidence of misappropriation risk                                                             |
| _Faiveley Transport Malmo AB v. Wabtec Corp._     | 559 F.3d 110 (2d Cir. 2009)        | TRO/injunction standard in trade secret cases; risk of immediate harm required                                                                                 |
| _Waymo LLC v. Uber Technologies, Inc._            | N.D. Cal. 2017-2018                | High-profile DTSA case; ex parte seizure order issued; settled                                                                                                 |
| _Turret Labs USA, Inc. v. CargoSprint, LLC_       | 5th Cir. 2023                      | Customer list trade secret; compilation value from aggregation even if individual elements public [VERIFY citation]                                            |
| _Mission Measurement Corp. v. Blackbaud, Inc._    | 216 F.Supp.3d 915 (N.D. Ill. 2016) | Early DTSA case on cross-border misappropriation                                                                                                               |
| EU _Coco v. AN Clark (Engineers) Ltd_             | [1969] RPC 41 (UK)                 | Three-element test for equitable breach of confidence: (1) necessary quality of confidence, (2) imparted in confidence, (3) unauthorized use causing detriment |
| _Saltman Engineering Co. v. Campbell Engineering_ | [1963] 3 All ER 413 (UK)           | Foundational UK confidential information case                                                                                                                  |

[JURISDICTION-SPECIFIC] Search legalcode-mcp for jurisdiction-specific cases in the applicable US state or EU member state. The above list is not exhaustive and requires independent verification.

---

## Anti-Patterns

Explicit catalogue of what NOT to do in trade secret protection and trade secret auditing:

1. **Treating NDAs as the whole program** — An NDA is necessary but not sufficient. Courts
   have rejected reasonable measures arguments where the only protective measure was an NDA
   with no classification, no access controls, and no consistent enforcement. The NDA is one
   layer; the program requires multiple overlapping layers.

2. **Vague trade secret identification** — Claiming everything is a trade secret without
   being able to identify specific assets with particularity. Courts routinely dismiss
   trade secret claims (at summary judgment and on 12(b)(6) motions) where the plaintiff
   cannot identify the specific trade secret at issue. The audit must identify assets
   specifically, not categorically.

3. **Overlooking the DTSA § 1833(b) immunity notice** — Failing to include the whistleblower
   immunity notice in employment agreements, NDAs, and contractor agreements signed after
   May 11, 2016. This single omission forfeits the right to exemplary damages (up to 2x
   actual damages) and attorneys' fees under DTSA § 1836(b)(3)(C), even in cases of willful
   misappropriation. It is the easiest fix with the highest payoff.

4. **Paper policies without consistent enforcement** — Having a beautifully drafted
   classification policy that no one follows. Courts in 2024–2025 have consistently looked
   skeptically at policies that were not enforced in practice. Document enforcement actions,
   not just policies.

5. **Delayed NDA execution** — Signing NDAs days, weeks, or months after an employee's
   start date. Courts have scrutinized whether consideration was adequate for post-hire NDAs.
   NDAs should be signed before or on the first day, not after.

6. **Uniform access without need-to-know controls** — Giving all engineers (or all employees)
   access to all crown jewel systems because it's easier. "Everyone had access to everything"
   is the opposite of reasonable measures for high-value assets. Implement RBAC and audit
   regularly.

7. **Treating the inevitable disclosure doctrine as a universal remedy** — Assuming
   inevitable disclosure provides an injunction basis without checking the applicable
   jurisdiction. California categorically rejects the doctrine. Even in favorable
   jurisdictions, the doctrine requires specific evidence that the new role makes use of
   the trade secret unavoidable — not just that the employee "knows" the secrets.

8. **No forensic preservation on departure** — Allowing departed employees' devices to
   be wiped and repurposed before forensic imaging. Once a device is wiped, the evidence
   of any pre-departure exfiltration is gone. Preservation is a one-time, low-cost action
   with potentially decisive evidentiary value.

9. **Disclosing in patent applications without analysis** — Filing a patent application
   that discloses information that was a trade secret. Patent and trade secret protection
   are mutually exclusive for the disclosed subject matter. Any decision to patent must
   include analysis of what trade secrets are consumed by the disclosure.

10. **Importing the predecessor employer's trade secrets** — Onboarding an employee who
    brings confidential information from a prior employer, either deliberately or by using
    prior employer materials for the new role. This creates derivative misappropriation
    liability. Conduct a prior employer "hygiene" process at hire and implement a documented
    "no importation" procedure.

11. **Indefinite non-compete + no trade secret program** — Relying on aggressive
    restrictive covenants instead of building an actual trade secret protection program.
    Post-FTC rule vacatur (September 2025), non-competes remain state-law-dependent and
    unenforceable in an increasing number of jurisdictions. A trade secret program that
    depends on restrictive covenants as its primary protection is fragile. Build the program
    independent of enforcement of non-competes.

12. **No clean room in M&A** — Allowing target company employees (potential competitors)
    access to the acquirer's crown jewels during due diligence. Even in a friendly deal,
    clean room protocols are essential for any information that would give the target a
    competitive advantage if the deal does not close.

13. **Open source contamination** — Publishing code (to GitHub, npm, PyPI, etc.) that
    contains or is derived from trade secret source code. This is particularly risky with
    AI/ML models: training a model on proprietary data and then open-sourcing the model
    weights may disclose the training data's properties through the model's behavior.

14. **Third-party AI tool disclosure** — Employees inputting Tier 1 trade secret
    information (formulas, source code, customer data, strategic plans) into third-party
    AI tools (ChatGPT, Copilot, Gemini, etc.) without assessing whether the AI provider
    uses inputs for model training or retains them. Many enterprise AI agreements require
    explicit opt-out from training data use. Default policies at some providers retain
    prompts. This is an inadvertent unauthorized disclosure.

15. **Skipping the audit because "we've never had a problem"** — Trade secret
    misappropriation is often discovered months or years after it occurs, if at all.
    The absence of a known incident does not mean the program is adequate. Employee
    departure data exfiltration studies suggest that >65% of employees take some company
    data when they leave (DTEX Systems 2024 report estimate — [VERIFY]). Most incidents
    are never discovered. An audit is valuable precisely because it identifies vulnerabilities
    before they become losses.

16. **Over-classifying everything** — Marking all documents "Highly Confidential / Trade
    Secret" regardless of actual competitive value. Over-classification dilutes the signal
    and trains employees to ignore markings. Courts have noted that routine internal
    documents marked "Trade Secret" suggest an organization that does not take the
    classification seriously. Classify with precision.

17. **Treating the EU Directive as identical to DTSA** — The EU Trade Secrets Directive
    2016/943 has important differences from DTSA: the "lawful means" carve-out is broader;
    the "legitimate interests" defense for former employees is more developed; the remedies
    framework differs (injunctions, recall, destruction of goods, damages, publication of
    decision). Do not assume a DTSA-compliant program is EU Directive-compliant.

18. **No succession planning for the trade secret register** — Maintaining the trade
    secret register in a single person's head or in their personal files. When that person
    departs, the register is gone. The register must be institutionalized, version-controlled,
    and backed up as part of the organization's knowledge management infrastructure.

---

## Writing Standards

Apply plain-language discipline to all audit output:

**For findings and remediation actions**:

- Active voice: "The organization has no DLP controls" not "DLP controls are absent"
- Specific, not vague: "Section 5.1 of the employee handbook last updated 2019 does not include trade secret training requirements" not "training may be inadequate"
- One point per finding: do not bundle multiple gaps into one finding
- Legal basis cited for every CRITICAL or HIGH finding; [VERIFY] tag on all unverified citations

**For executive summaries** (shared with non-lawyer senior management):

- Plain language; no Latin or unexplained legal terminology
- Lead with the most significant risks and their practical business consequences
- Quantify exposure where possible (e.g., "forfeits exemplary damages and attorneys' fees under DTSA")
- Specific, prioritized action list

**Quality gates before delivery**:

1. Can a non-lawyer business leader understand the severity and business impact of each finding?
2. Is every CRITICAL and HIGH finding backed by a specific statute, case, or principle (or tagged [VERIFY])?
3. Does every finding have a specific, actionable remediation step with a named owner and deadline?
4. Are all jurisdiction-specific conclusions properly flagged with the applicable jurisdiction?
5. Is the Glass Box audit trail complete, with confidence level and limitations noted?

---

## External Tool Integration

**With legalcode-mcp connected (preferred)**:

- In Step 3, search for DTSA / UTSA / EU Directive current text and leading case law
- Search for jurisdiction-specific non-compete enforceability updates (2024–2026 rapidly evolving)
- Search for DTSA § 1833(b) immunity notice requirements and recent cases
- Search for the applicable state's UTSA text and key divergences from the uniform act
- Save verified authority to `/tmp/legalcode-trade-secret-authority.md`
- Mark all legalcode-mcp-sourced citations as VERIFIED in the Glass Box audit trail

**Without legalcode-mcp**:

- Mark all statutory and case law references with [VERIFY]
- Note in Glass Box audit trail: `legalcode_mcp: "Not connected"`
- Focus the audit on structural program quality and process gaps rather than legal authority
- Recommend that counsel independently verify all statutory citations and case law
- Include a prominent notice that legal citations require independent verification

---

## Localization Notes

When adapting this audit to jurisdictions outside the US and EU:

**United Kingdom (post-Brexit)**:

- No EU Directive transposition; apply equitable breach of confidence principles
- _Coco v. AN Clark (Engineers) Ltd_ [1969] three-element test as the analytical framework
- Non-compete enforceability: reasonable scope and duration under _Tillman v. Egon Zehnder_ [2019] UKSC 32
- Garden leave: well-recognized in England and Wales; factor against non-compete duration
- [VERIFY: UK Trade Secrets Bill current legislative status]

**Canada**:

- Common law breach of confidence; no federal trade secrets statute [VERIFY for provincial variations]
- Federal court jurisdiction available where federal law applies; otherwise provincial courts
- Non-solicitation and non-compete: context-dependent enforceability; _Shafron v. KRG Insurance_ [2009] SCC 6

**Australia**:

- Equitable breach of confidence + potential misleading or deceptive conduct under ACL
- Non-compete enforceability: blue-pencil or read-down approach varies by state
- _Corrs Pavilion Pty Ltd v. Cobb_ [VERIFY citation] and related Australian confidentiality cases

**[JURISDICTION-SPECIFIC]** For any jurisdiction not listed, apply this framework:

1. Identify the applicable statute or equitable doctrine governing confidential information
2. Identify the reasonable measures / reasonable steps threshold in the applicable law
3. Identify non-compete enforceability rules and any whistleblower protection equivalents
4. Flag all local-law-specific conclusions with the jurisdiction name

---

## Output Format Template

Structure the final audit report as:

```markdown
## Trade Secret Audit Report

**Organization**: [Name or identifier]
**Engagement Type**: [Proactive / M&A / Pre-litigation / Post-incident]
**Jurisdiction(s)**: [Primary applicable law]
**Audit Scope**: [Full audit / Scoped — specify]
**Date of Audit**: [Date]
**Prepared by**: AI-assisted analysis — requires qualified legal review

---

## Executive Summary

[3–5 sentence overview: overall program maturity, most significant findings, and top priorities]

**Program Maturity Rating**: [Strong / Adequate / Developing / Inadequate]
**Immediate Action Required**: [Yes / No — brief description]
**Litigation Readiness**: [High / Medium / Low]

---

## Crown Jewels Register

| Asset ID | Description                         | Tier | Business Unit | Access Controls in Place | Measures Adequate?   |
| -------- | ----------------------------------- | ---- | ------------- | ------------------------ | -------------------- |
| CJ-001   | [e.g., Proprietary algorithm for X] | 1    | Engineering   | [RBAC, DLP, NDA]         | [Yes / Partial / No] |
| ...      |                                     |      |               |                          |                      |

---

## Findings Summary

| Finding ID | Domain   | Severity | Summary            | Remediation Deadline |
| ---------- | -------- | -------- | ------------------ | -------------------- |
| TS-001     | [Domain] | CRITICAL | [One-line summary] | 5 business days      |
| TS-002     | [Domain] | HIGH     | [One-line summary] | 30 days              |
| ...        |          |          |                    |                      |

**Total Findings**: [N] | CRITICAL: [N] | HIGH: [N] | MEDIUM: [N] | LOW: [N]

---

## Detailed Findings

### [TS-001] [Finding Title] — CRITICAL | Confidence: [Level]

**Domain**: [Crown Jewels / Reasonable Measures / Contractual / Departure / Litigation Readiness / AI/ML]
**Finding**: [Specific factual description of the gap]
**Legal Risk**: [Specific legal consequence — cite applicable provision; mark [VERIFY] if unverified]
**Business Impact**: [What this means practically for the organization]
**Remediation Action**: [Specific steps]
**Owner**: [Legal / CISO / HR / Procurement]
**Deadline**: [5 business days / 30 days / 90 days / 180 days]
**Litigation Readiness Impact**: [How this affects the organization if a trade secret claim is filed]

[Repeat for each finding]

---

## Reasonable Measures Scorecard

| Domain                   | Controls Assessed | Present & Adequate | Partial | Absent | Score   |
| ------------------------ | ----------------- | ------------------ | ------- | ------ | ------- |
| Physical Security        | [N]               | [N]                | [N]     | [N]    | [%]     |
| IT / DLP                 | [N]               | [N]                | [N]     | [N]    | [%]     |
| HR Program               | [N]               | [N]                | [N]     | [N]    | [%]     |
| Contractual Portfolio    | [N]               | [N]                | [N]     | [N]    | [%]     |
| Classification & Marking | [N]               | [N]                | [N]     | [N]    | [%]     |
| **Overall**              |                   |                    |         |        | **[%]** |

---

## Contractual Portfolio Summary

| Agreement Type                 | Coverage Rate | Key Gap       | Priority                   |
| ------------------------------ | ------------- | ------------- | -------------------------- |
| Employee NDAs                  | [%]           | [Description] | [CRITICAL/HIGH/MEDIUM/LOW] |
| Contractor NDAs                | [%]           |               |                            |
| Vendor NDAs                    | [%]           |               |                            |
| DTSA § 1833(b) Immunity Notice | [%]           |               |                            |
| Inventions Assignment          | [%]           |               |                            |

---

## Departure Protocol Assessment

| Protocol Stage           | Status                        | Key Gap |
| ------------------------ | ----------------------------- | ------- |
| Pre-departure monitoring | [Adequate / Partial / Absent] |         |
| Exit interview           | [Adequate / Partial / Absent] |         |
| IT deactivation          | [Adequate / Partial / Absent] |         |
| Forensic preservation    | [Adequate / Partial / Absent] |         |
| Post-departure follow-up | [Adequate / Partial / Absent] |         |

---

## Remediation Roadmap

### Tier 1 — Immediate (0–5 Business Days)

1. [Specific action — Owner — Deadline]
2. ...

### Tier 2 — Near-Term (0–30 Days)

1. [Specific action — Owner — Deadline]
2. ...

### Tier 3 — Roadmap (0–90 Days)

1. [Specific action — Owner — Deadline]
2. ...

### Tier 4 — Policy Cycle (0–180 Days)

1. [Specific action — Owner — Deadline]
2. ...

---

## Litigation Readiness Score

| Element                                                      | Adequate | Partial | Absent |
| ------------------------------------------------------------ | -------- | ------- | ------ |
| Trade secret register (assets identified with particularity) | ☐        | ☐       | ☐      |
| Written protection policies (with version history)           | ☐        | ☐       | ☐      |
| NDA execution records                                        | ☐        | ☐       | ☐      |
| Training completion records                                  | ☐        | ☐       | ☐      |
| Access control logs                                          | ☐        | ☐       | ☐      |
| Exit documentation (certifications)                          | ☐        | ☐       | ☐      |
| Enforcement records                                          | ☐        | ☐       | ☐      |
| Forensic preservation capability                             | ☐        | ☐       | ☐      |

**Litigation Readiness Score**: [X/8] — [High ≥7 / Medium 5–6 / Low ≤4]

---

## Next Steps

[Specific actions, with owners and deadlines]

1. [Owner] to [action] by [date]
2. ...
```

---

## Misappropriation Remedies Reference

For audit findings where misappropriation is suspected or has occurred, these are the
available remedies under the primary frameworks [all statutory references require [VERIFY]]:

### Under DTSA (18 U.S.C. § 1836) [VERIFY current text]

| Remedy                     | Scope                                                                                                     | Notes                                                                                                     |
| -------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Injunctive relief**      | Temporary restraining order (TRO), preliminary injunction, permanent injunction                           | Cannot prevent person from accepting employment; cannot conflict with applicable state law re: employment |
| **Ex parte civil seizure** | Available in extraordinary circumstances where TRO inadequate; allows seizure of materials before hearing | Rarely granted; requires specific showing of imminent harm and inadequacy of TRO                          |
| **Damages**                | Actual damages + unjust enrichment (no double-counting), OR reasonable royalty as alternative             | Court may choose measure most favorable to plaintiff                                                      |
| **Exemplary damages**      | Up to **2x actual damages** for willful and malicious misappropriation                                    | **Forfeited if DTSA § 1833(b) immunity notice absent from agreements**                                    |
| **Attorneys' fees**        | Available for willful misappropriation or bad faith claims                                                | **Forfeited if DTSA § 1833(b) immunity notice absent**                                                    |

### Under UTSA (State Law) [Varies by state — VERIFY]

| Remedy                     | Scope                                                              | Notes                                                                   |
| -------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| **Injunctive relief**      | Standard for threatened or actual misappropriation                 | Some states follow PepsiCo inevitable disclosure approach               |
| **Damages**                | Actual damages + unjust enrichment, OR reasonable royalty          |                                                                         |
| **Exemplary damages**      | Up to 2x damages (most states; check state-specific UTSA adoption) |                                                                         |
| **Attorneys' fees**        | Willful misappropriation or bad faith                              |                                                                         |
| **Statute of limitations** | **3 years** from discovery of misappropriation (most states)       | Discovery rule applies; continuing misappropriation doctrine may extend |

### Under EU Trade Secrets Directive 2016/943 [VERIFY implementing legislation in specific member state]

| Remedy                               | Scope                                                                                           | Notes                                     |
| ------------------------------------ | ----------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **Injunctions / prohibitory orders** | Against acquisition, use, disclosure; recall of infringing goods                                | Art. 12 — court considers proportionality |
| **Corrective measures**              | Recall, destruction, modification of infringing goods                                           | Art. 12                                   |
| **Damages**                          | Actual loss + unfair profits, OR lump sum based on royalties/fees the infringer would have paid | Art. 14 — both methods available          |
| **Publication of judicial decision** | Court may order publication at infringer's expense                                              | Art. 15                                   |
| **Statute of limitations**           | At least **6 years** under Art. 8 (member state implementations vary)                           | [VERIFY specific member state]            |

---

## Provenance

Created by Legalcode (2026-03-20). Original synthesis from: DTSA statutory text (18 U.S.C.
§§ 1836–1839); EU Trade Secrets Directive 2016/943; WIPO Guide to Trade Secrets and Innovation
(June 2024); McGuireWoods 2025 Trade Secret Year in Review; Mintz trade secret audit
methodology analysis (September 2025); Baker Botts reasonable measures analysis (2021);
DTEX Systems insider threat research; PepsiCo v. Redmond (7th Cir. 1995); Whyte v. Schlage
Lock (Cal. App. 2002); Rockwell Graphic Systems v. DEV Industries (7th Cir. 1991);
practitioner guidance from Smith Law, Ward and Smith, and Redgrave LLP. All citations
require independent verification against authoritative primary sources before reliance.
