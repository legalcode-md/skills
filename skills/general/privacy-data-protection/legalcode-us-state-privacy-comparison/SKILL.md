---
name: legalcode-us-state-privacy-comparison
description: Compare all enacted US state comprehensive privacy laws to determine applicability, map consumer
  rights obligations, and produce a compliance gap analysis for multi-state operations. Use when assessing
  whether your organization is subject to CCPA/CPRA (California), VCDPA (Virginia), CPA (Colorado), CTDPA
  (Connecticut), UCPA (Utah), ICDPA (Iowa), INCDPA (Indiana), DPDPA (Delaware), TIPA (Tennessee), MCDPA
  (Montana), NHPA (New Hampshire), NJDPA (New Jersey), OCPA (Oregon), TDPSA (Texas), NDPA (Nebraska),
  MODPA (Maryland), MCDPA (Minnesota), KCDPA (Kentucky), RIDTPPA (Rhode Island), or any other enacted
  US state comprehensive privacy law. Produces a threshold analysis table, consumer rights compliance
  matrix, sensitive data obligations mapping, opt-out mechanism assessment, enforcement risk profile,
  cure period status, and a prioritized gap analysis with remediation roadmap. Covers all 19 enacted comprehensive
  state privacy laws as of 2026, including 2025-2026 amendments, new UOOM mandates, and GPC requirements.
license: Legalcode Skills Source-Available License 1.0; see LICENSE.md
---

## Using this skill

Before following the workflow, read [runtime and evidence requirements](references/runtime-compatibility.md). They govern current tool use and source verification when older examples below differ from the connected runtime.


# Legalcode US State Privacy Law Comparison

> **Disclaimer**: This skill provides a framework for AI-assisted US state privacy law
> compliance analysis. It does not constitute legal advice. All outputs should be reviewed
> by a qualified privacy counsel licensed in the relevant jurisdiction before reliance.
> State privacy laws are amended frequently — verify current statutory text, regulations,
> and AG guidance before acting on any threshold, right, or requirement described here.
> Statutory and regulatory references cited from training data carry hallucination risk —
> verify against authoritative sources before relying on them. Mark any unverified claim
> with **[VERIFY]**.

---

## Purpose and Scope

This skill performs a comprehensive multi-state US privacy law gap analysis. It determines
which enacted state comprehensive privacy laws apply to a specific organization, maps all
required consumer rights and controller obligations, identifies compliance gaps, and
produces a prioritized remediation roadmap.

**This skill covers:**

- Applicability threshold analysis across all 19 enacted US state comprehensive privacy laws
- Consumer rights matrix: access, deletion, correction, portability, opt-out of sale,
  opt-out of targeted advertising, opt-out of profiling, appeal rights
- Sensitive data classification per state — definitions, consent model, and sale prohibitions
- Universal Opt-Out Mechanism (UOOM) / Global Privacy Control (GPC) mandate mapping
- Cure period status — which states still offer mandatory cure rights and when they expire
- Enforcement mechanism comparison — AG civil penalties, private right of action, treble
  damages, and AG investigatory powers
- Children and minor protections across states
- Data Protection Assessment (DPA / PIA) trigger analysis
- Controller vs. processor obligation split and contract audit
- Compliance gap analysis: COMPLIANT / PARTIAL / NON-COMPLIANT classification
- Prioritized remediation roadmap with 30/60/90-day action items
- Enforcement risk profile informed by actual enforcement actions (Sephora, DoorDash,
  Tractor Supply, Disney, Allstate/Arity, and others)

**This skill does not:**

- Provide legal advice or replace qualified privacy counsel review
- Address sector-specific laws that run alongside state privacy laws (HIPAA, GLBA, FERPA,
  COPPA, FCRA, DPPA, Washington My Health My Data Act, Illinois BIPA, etc.)
- Produce a comprehensive data protection impact assessment (see `legalcode-dpia-generator`)
- Draft data processing agreements (see `legalcode-dpa-review-and-negotiation`)
- Handle GDPR, UK GDPR, LGPD, PIPEDA, or other non-US privacy regimes (see the relevant
  cross-border and DSAR skills)

---

## Jurisdiction and Governing Law

This skill covers all US state comprehensive consumer privacy laws enacted as of early 2026. The "comprehensive" designation means laws that establish general consumer rights
over personal data, as distinct from sector-specific state laws (health data, financial
data, biometrics), marketing laws, or breach notification statutes.

### Enacted Laws Roster (19 laws as of 2026)

| #   | State         | Law Name                                                  | Abbrev.      | Citation                                | Effective Date                                                                          | Status                                  |
| --- | ------------- | --------------------------------------------------------- | ------------ | --------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------- |
| 1   | California    | California Consumer Privacy Act (as amended by CPRA)      | CCPA/CPRA    | Cal. Civ. Code § 1798.100 et seq.       | Jan. 1, 2020 (CCPA); Jan. 1, 2023 (CPRA amend.); Jan. 1, 2026 (ADMT/cybersecurity regs) | In force                                |
| 2   | Virginia      | Virginia Consumer Data Protection Act                     | VCDPA        | Va. Code § 59.1-571 et seq.             | Jan. 1, 2023                                                                            | In force                                |
| 3   | Colorado      | Colorado Privacy Act                                      | CPA          | Colo. Rev. Stat. § 6-1-1301 et seq.     | July 1, 2023                                                                            | In force; cure discretionary Jan. 2025  |
| 4   | Connecticut   | Connecticut Data Privacy Act                              | CTDPA        | Conn. Gen. Stat. § 42-515 et seq.       | July 1, 2023                                                                            | In force; major 2026 amendments pending |
| 5   | Utah          | Utah Consumer Privacy Act                                 | UCPA         | Utah Code § 13-61-101 et seq.           | Dec. 31, 2023                                                                           | In force                                |
| 6   | Iowa          | Iowa Consumer Data Protection Act                         | ICDPA        | Iowa Code § 715D.1 et seq.              | Jan. 1, 2025                                                                            | In force                                |
| 7   | Indiana       | Indiana Consumer Data Protection Act                      | INCDPA       | Ind. Code § 24-15-1 et seq.             | Jan. 1, 2026                                                                            | In force                                |
| 8   | Delaware      | Delaware Personal Data Privacy Act                        | DPDPA        | Del. Code tit. 6, § 12D-101 et seq.     | Jan. 1, 2025                                                                            | In force; cure discretionary Dec. 2025  |
| 9   | Tennessee     | Tennessee Information Protection Act                      | TIPA         | Tenn. Code § 47-18-3201 et seq.         | July 1, 2025                                                                            | In force                                |
| 10  | Montana       | Montana Consumer Data Privacy Act                         | MCDPA        | Mont. Code § 30-14-3401 et seq.         | Oct. 1, 2024 (orig.); Oct. 1, 2025 (amend.)                                             | In force; mandatory cure removed        |
| 11  | New Hampshire | New Hampshire Privacy Act                                 | NHPA         | RSA § 507-H:1 et seq.                   | Jan. 1, 2025                                                                            | In force; cure discretionary Jan. 2026  |
| 12  | New Jersey    | New Jersey Data Privacy Act                               | NJDPA        | N.J. Stat. § 56:8-166.1 et seq.         | Jan. 15, 2025                                                                           | In force; cure sunsets July 15, 2026    |
| 13  | Oregon        | Oregon Consumer Privacy Act                               | OCPA         | ORS § 646A.570 et seq.                  | July 1, 2024                                                                            | In force; cure discretionary Jan. 2026  |
| 14  | Texas         | Texas Data Privacy and Security Act                       | TDPSA        | Tex. Bus. & Com. Code § 541.001 et seq. | July 1, 2024                                                                            | In force; permanent cure                |
| 15  | Nebraska      | Nebraska Data Privacy Act                                 | NDPA         | Neb. Rev. Stat. § 87-1001 et seq.       | Jan. 1, 2025                                                                            | In force; permanent cure                |
| 16  | Maryland      | Maryland Online Data Privacy Act                          | MODPA        | Md. Code, Com. Law § 14-4701 et seq.    | Oct. 1, 2025 (collection); Apr. 1, 2026 (full)                                          | In force                                |
| 17  | Minnesota     | Minnesota Consumer Data Privacy Act                       | MCDPA/MNCDPA | Minn. Stat. § 325M.01 et seq.           | July 31, 2025                                                                           | In force; cure discretionary Feb. 2026  |
| 18  | Kentucky      | Kentucky Consumer Data Protection Act                     | KCDPA        | Ky. Rev. Stat. § [VERIFY citation]      | Jan. 1, 2026                                                                            | In force; permanent cure                |
| 19  | Rhode Island  | Rhode Island Data Transparency and Privacy Protection Act | RIDTPPA      | R.I. Gen. Laws § [VERIFY citation]      | Jan. 1, 2026                                                                            | In force; no cure period                |

**Note on 2025 legislation**: No additional states enacted comprehensive privacy laws in 2025. Florida has a narrow Digital Bill of Rights (large tech companies only). Washington
state's My Health My Data Act covers health data but is not a comprehensive privacy law.
Illinois, Massachusetts, and others had bills pending as of early 2026 but had not enacted
them. [VERIFY for any new enactments after the skill's training data cutoff.]

---

## Interactive Clarification

This skill uses **CLARIFY** prompts at key decision points where the answer materially
changes the direction or output of the analysis. When a CLARIFY point is encountered,
pause and ask the user. Do not proceed on assumptions that would change the analysis.

If the user provides information proactively that answers a CLARIFY question, skip the
question and proceed.

---

## Workflow

### Step 1: Accept Organizational Profile

Accept a description of the organization being analyzed. Collect or ask for:

1. **Entity type**: For-profit corporation, nonprofit, government entity, educational
   institution, financial institution (GLBA-regulated), healthcare entity (HIPAA-covered)
2. **Business model**: B2C, B2B, marketplace, SaaS, data broker, advertising technology,
   healthcare, insurance, financial services, mixed
3. **Annual gross revenue** (last fiscal year)
4. **Geographic footprint**: States in which the organization conducts business or targets
   residents; if uncertain, specify industries/sectors served
5. **Data profile**:
   - Approximate number of consumers whose personal data is processed per state per year
   - Whether the organization sells, shares, or discloses personal data to third parties
   - If yes, estimated percentage of gross annual revenue derived from such sales
   - Whether sensitive data categories are processed (and which categories)
6. **Sector-specific regulation**: Is the organization subject to HIPAA, GLBA, FERPA,
   COPPA, FCRA, DPPA, Illinois BIPA, or other sector-specific federal or state laws?

**CLARIFY** — If insufficient organizational profile information is provided, ask:

- "What is the organization's approximate annual gross revenue?"
- "Does the organization process personal data of consumers in multiple states?"
- "Does the organization sell or share consumer personal data with third parties, and if
  so, what percentage of gross revenue is derived from those data sales?"
- "Does the organization process any sensitive data categories (health, biometric, precise
  geolocation, racial/ethnic origin, children's data, financial credentials)?"

If information is genuinely unavailable, proceed with conservative assumptions and
**state all assumptions explicitly** in the output.

### Step 2: Entity-Level Exemption Screen

Before running threshold tests, determine whether the organization is categorically exempt
from any state laws due to entity type. Two exemption architectures exist:

**Entity-level exemption**: The entire organization is exempt. Example: Iowa and Tennessee
provide full entity-level exemptions for HIPAA-covered entities, meaning a hospital subject
to HIPAA is entirely exempt from the Iowa ICDPA and Tennessee TIPA — even for non-PHI
personal data.

**Data-level exemption**: Only the specifically regulated data is exempt; all other
personal data remains in scope. Example: Most states exempt only PHI or GLBA-regulated
financial data, not the healthcare organization or financial institution as a whole.

Run the following exemption checks for each state in scope:

| Exemption Type                    | States with Entity-Level Exemption                                                                                | States with Data-Level Only                                                                                                                             |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Government agencies               | All states                                                                                                        | —                                                                                                                                                       |
| Nonprofit organizations           | Most states (broad exemption)                                                                                     | Delaware (narrow carve-out only), Maryland (narrow), Minnesota (narrow insurance fraud only), New Jersey (NOT exempt), Oregon (covered as of July 2025) |
| HIPAA-covered entities            | Iowa, Nebraska, Tennessee (entity-level)                                                                          | All other states (PHI exempt; non-PHI not)                                                                                                              |
| GLBA financial institutions       | Iowa, New Hampshire, Tennessee (entity-level)                                                                     | Montana, Connecticut, Oregon, California, Minnesota (data-level only); most others [VERIFY per state]                                                   |
| Small businesses (SBA definition) | Texas, Nebraska (SBA-defined small businesses exempt entirely, though cannot sell sensitive data without consent) | All other states (no SBA exemption; numeric thresholds instead)                                                                                         |

**CLARIFY** — If the organization is a nonprofit: "Several states (Delaware, Maryland,
Minnesota, Montana, New Jersey, Oregon) have materially narrowed or eliminated the
nonprofit exemption. Does the organization operate in any of these states?"

### Step 3: Run Threshold Analysis

For each state where the organization operates or targets residents, apply that state's
specific applicability tests. Track results in a threshold table.

**Threshold test architecture**: Most states use an OR test between two or three prongs.
A few require satisfying ALL prongs (AND logic). Apply the correct logic for each state.

#### Master Threshold Table

| State         | Revenue Floor                                                                     | Consumer Volume (Primary)                             | Consumer Volume (Secondary)                  | % Revenue from Data Sales                         | Logic                                | B2B/Employee Exclusion                        |
| ------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------- | -------------------------------------------- | ------------------------------------------------- | ------------------------------------ | --------------------------------------------- |
| California    | >$26.625M (2025; CPI-adjusted annually)                                           | 100,000 consumers or households/yr                    | —                                            | 50%+ gross revenue from selling/sharing PI        | OR                                   | None explicit                                 |
| Virginia      | None                                                                              | 100,000 consumers/yr                                  | 25,000 consumers                             | 50%+ from sale of PI                              | OR                                   | Employees and B2B contacts excluded           |
| Colorado      | None                                                                              | 100,000 consumers/yr                                  | 25,000 consumers                             | Revenue or discounts from sale of PI              | OR                                   | No explicit exclusion                         |
| Connecticut   | None (until July 2026: 100,000 or 25,000+25%; from July 2026: 35,000 or any sale) | 100,000/yr (until July 2026); 35,000 (from July 2026) | 25,000 (until July 2026); 1 (from July 2026) | 25%+ (until July 2026); any sale (from July 2026) | OR                                   | No explicit exclusion                         |
| Utah          | ≥$25M revenue                                                                     | 100,000 consumers/yr                                  | 25,000 consumers                             | 50%+ from sale of PI                              | Revenue AND (volume OR %)            | No explicit exclusion                         |
| Iowa          | None                                                                              | 100,000 consumers/yr                                  | 25,000 consumers                             | 50%+ from sale of PI                              | OR                                   | No explicit exclusion                         |
| Indiana       | None                                                                              | 100,000 consumers/yr                                  | 25,000 consumers                             | 50%+ from sale of PI                              | OR                                   | No explicit exclusion                         |
| Delaware      | None                                                                              | 35,000 consumers/yr                                   | 10,000 consumers                             | 20%+ from sale of PI                              | OR                                   | No explicit exclusion                         |
| Tennessee     | >$25M revenue                                                                     | 175,000 consumers/yr (highest!)                       | 25,000 consumers                             | 50%+ from sale of PI                              | Revenue AND (volume OR %)            | No explicit exclusion                         |
| Montana       | None                                                                              | 25,000 consumers/yr (post-2025 amend.; prev. 50,000)  | 15,000 consumers (prev. 25,000)              | 25%+ from sale of PI                              | OR                                   | No explicit exclusion                         |
| New Hampshire | None                                                                              | 35,000 consumers/yr                                   | 10,000 consumers                             | 25%+ from sale of PI                              | OR                                   | No explicit exclusion                         |
| New Jersey    | None                                                                              | 100,000 consumers/yr (excl. payment transaction data) | 25,000 consumers                             | Revenue or discounts from data sales              | OR                                   | No explicit exclusion                         |
| Oregon        | None                                                                              | 100,000 consumers/yr                                  | 25,000 consumers                             | 25%+ from sale of PI                              | OR                                   | No explicit exclusion                         |
| Texas         | None — SBA small business exemption                                               | No numeric consumer threshold                         | —                                            | —                                                 | SBA definition: NOT a small business | B2B contacts unclear; SBA definition controls |
| Nebraska      | None                                                                              | 100,000 consumers/yr                                  | 25,000 consumers                             | 25%+ from sale of PI                              | OR                                   | No explicit exclusion                         |
| Maryland      | None                                                                              | 35,000 consumers/yr                                   | —                                            | No revenue % alternative threshold                | Sole trigger: 35,000 consumers       | No explicit exclusion                         |
| Minnesota     | None                                                                              | 100,000 consumers/yr                                  | 25,000 consumers                             | 25%+ from sale of PI                              | OR                                   | No explicit exclusion                         |
| Kentucky      | None                                                                              | 100,000 consumers/yr                                  | 25,000 consumers                             | 50%+ from sale of PI                              | OR                                   | Employees excluded [VERIFY]                   |
| Rhode Island  | None                                                                              | 35,000 consumers/yr (excl. payment transaction data)  | 10,000 consumers                             | 20%+ from sale of PI                              | OR                                   | No explicit exclusion                         |

**Threshold calculation notes:**

- Thresholds are measured on a rolling 12-month basis in most states (not calendar year).
  Seasonal spikes can push an organization into scope mid-year.
- California's household count means a single internet address can represent multiple
  consumers — particularly relevant for data brokers and household-level services.
- Colorado counts non-monetary benefits (discounts, rewards) in the "revenue from data
  sales" numerator — broader than other states.
- Maryland has no revenue-percentage alternative — 35,000 consumers is the sole threshold.
  No data sales required. This captures mid-size B2C businesses that other states might not.
- Connecticut's July 2026 threshold reduction is dramatic: from 100,000 consumers to
  35,000, and from 25,000+25% to any consumer data sale regardless of volume.

**CLARIFY** — After completing the threshold analysis, present the applicability summary:
"The following state privacy laws apply to [Organization]. The following states are
approaching thresholds. The following states do not currently apply. Do you want me to
proceed to the full gap analysis, or focus on specific laws?"

### Step 4: Sensitive Data Identification

For each applicable law, identify whether the organization processes sensitive data
categories. Present the following state-by-state sensitive data mapping.

**Core sensitive data categories and state coverage:**

| Category                      | CA  | VA  | CO   | CT  | UT  | IA  | IN  | DE  | TN  | MT  | NH  | NJ  | OR  | TX  | NE  | MD  | MN  | KY  | RI  |
| ----------------------------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Racial/ethnic origin          | ✓   | ✓   | ✓    | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |
| Physical/mental health        | ✓   | ✓   | ✓    | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |
| Biometric data (for ID)       | ✓   | ✓   | ✓    | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |
| Genetic data                  | ✓   | ✓   | ✓    | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |
| Precise geolocation           | ✓   | ✓   | ✗(!) | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |
| Sexual orientation/sex life   | ✓   | ✓   | ✓    | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |
| Religious beliefs             | ✓   | ✓   | ✓    | ✓   | ✗   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |
| Citizenship/immigration       | ✓   | ✓   | ✓    | ✓   | ✗   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |
| Financial credentials/account | ✓   | ✗   | ✗    | ✗   | ✗   | ✗   | ✗   | ✓   | ✗   | ✗   | ✗   | ✓   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✓   |
| Union membership              | ✓   | ✗   | ✗    | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   |
| Philosophical beliefs         | ✓   | ✗   | ✗    | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   |
| Transgender/nonbinary status  | ✓   | ✗   | ✗    | ✗   | ✗   | ✗   | ✗   | ✓   | ✗   | ✗   | ✗   | ✓   | ✗   | ✗   | ✗   | ✓   | ✓   | ✗   | ✗   |
| Children's data (<13)         | ✓   | ✓   | ✓    | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |

**Key sensitive data differentiators to flag:**

- **Colorado (CPA)**: Precise geolocation is NOT in the sensitive data definition — a
  significant gap versus all other laws. [VERIFY against current statutory text.]
- **California (CCPA/CPRA)**: Broadest definition. Includes union membership, philosophical
  beliefs, SSN, account log-in credentials, financial account information plus access codes.
  Also has a unique "Limit" right allowing consumers to restrict certain uses of sensitive
  PI that is separate from opt-in consent.
- **Maryland (MODPA)**: Sale of sensitive data is PROHIBITED OUTRIGHT — no consent
  mechanism overrides this ban. Opt-in consent is required for processing, but even with
  consent, the organization cannot sell sensitive data.
- **Delaware (DPDPA) and New Jersey (NJDPA)**: Include transgender/nonbinary status
  explicitly.
- **New Jersey (NJDPA)**: Includes financial account data (broader than GLBA coverage).

**Sensitive data consent model by state:**

| Consent Model                                                                     | States                                                                                                                                                    |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Opt-in consent required** (cannot process until affirmative consent obtained)   | Virginia, Colorado, Connecticut, Texas, Oregon, Montana, Delaware, Indiana, Kentucky, Nebraska, New Hampshire, New Jersey, Minnesota, Maryland, Tennessee |
| **Opt-out / Limit** (may process unless consumer opts out or requests limitation) | California (unique "Limit" right for sensitive PI), Iowa, Utah                                                                                            |

### Step 5: Map Consumer Rights Obligations

For each applicable law, map the consumer rights the organization must support.

#### Consumer Rights Matrix

| Right                              | CA         | VA  | CO  | CT  | UT  | IA  | IN  | DE  | TN  | MT  | NH  | NJ  | OR  | TX  | NE  | MD  | MN         | KY  | RI  |
| ---------------------------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
| Right to access/know               | ✓          | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓          | ✓   | ✓   |
| Right to delete                    | ✓          | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓          | ✓   | ✓   |
| Right to correct                   | ✓          | ✓   | ✓   | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓          | ✓   | ✓   |
| Right to portability               | ✓          | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓          | ✓   | ✓   |
| Opt-out of sale                    | ✓          | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓          | ✓   | ✓   |
| Opt-out of targeted advertising    | ✓          | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓          | ✓   | ✓   |
| Opt-out of profiling               | ✓          | ✓   | ✓   | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓          | ✓   | ✓   |
| Limit use of sensitive PI          | ✓(CA only) | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗          | ✗   | ✗   |
| Appeal right                       | ✓          | ✓   | ✓   | ✓   | ✗   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓          | ✓   | ✓   |
| Know specific 3rd parties          | ✗          | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✓   | ✗   | ✗   | ✗   | ✓          | ✗   | ✗   |
| Profiling explanation/reevaluation | ✗          | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✗   | ✓(MN only) | ✗   | ✗   |

**Response timelines:**

- Most states: 45 days with 45-day extension available (90 days total).
- California (CCPA/CPRA): 45 days with 45-day extension.
- Iowa (ICDPA): 90 days initial; 45-day extension.
- Delaware (DPDPA): 45 days with 45-day extension.
- Oregon (OCPA): 45 days with 45-day extension.
- Appeal rights: typically 60 days to respond to an appeal.

### Step 6: Assess UOOM / GPC Compliance

Determine which universal opt-out mechanisms (UOOMs) are mandated and whether the
organization currently honors them.

#### UOOM Mandate Status

| State         | UOOM Required?                                        | Technical Standard                                                                   | Effective Date         |
| ------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------ | ---------------------- |
| California    | YES                                                   | GPC recognized; AB 566 (if enacted) would require browser-level opt-out by Jan. 2027 | Enforcement began 2024 |
| Virginia      | NO                                                    | Must provide opt-out mechanisms but no UOOM signal requirement                       | —                      |
| Colorado      | YES — GPC only (first and only recognized as of 2024) | GPC recognized Dec. 2023 by AG                                                       | July 1, 2024           |
| Connecticut   | YES                                                   | Must honor recognized UOOMs; GPC qualifies                                           | Jan. 1, 2025           |
| Utah          | NO                                                    | —                                                                                    | —                      |
| Iowa          | NO                                                    | —                                                                                    | —                      |
| Indiana       | NO [VERIFY]                                           | —                                                                                    | —                      |
| Delaware      | YES                                                   | Must honor recognized UOOMs                                                          | Jan. 1, 2026           |
| Tennessee     | NO [VERIFY]                                           | —                                                                                    | —                      |
| Montana       | YES                                                   | GPC recognized                                                                       | Oct. 1, 2024           |
| New Hampshire | YES                                                   | Must honor recognized UOOMs                                                          | Jan. 1, 2025           |
| New Jersey    | YES                                                   | Must honor recognized UOOMs                                                          | July 15, 2025          |
| Oregon        | YES                                                   | Must honor recognized UOOMs; HB 2008 expanded                                        | Jan. 1, 2026           |
| Texas         | YES                                                   | GPC and other recognized mechanisms                                                  | Jan. 1, 2025           |
| Nebraska      | YES                                                   | Must honor recognized UOOMs                                                          | Jan. 1, 2025           |
| Maryland      | YES                                                   | Must honor recognized UOOMs                                                          | Oct. 1, 2025           |
| Minnesota     | YES                                                   | Must honor recognized UOOMs                                                          | July 31, 2025          |
| Kentucky      | NO [VERIFY]                                           | —                                                                                    | —                      |
| Rhode Island  | NO [VERIFY]                                           | —                                                                                    | —                      |

**GPC implementation requirements:**

1. Read the `Sec-GPC: 1` HTTP header on all incoming requests
2. Read the `navigator.globalPrivacyControl = true` JavaScript property on page load
3. Honor a positive signal as an immediate, valid consumer opt-out of sale and targeted
   advertising
4. Propagate the opt-out to all downstream advertising technology integrations — not just
   record the preference
5. Apply the opt-out to the device/browser level and, if the consumer is authenticated,
   to the consumer's account profile
6. Maintain the opt-out preference across sessions (persistent)
7. Extend UOOM compliance to mobile apps (exact mechanism varies by state; [VERIFY CPPA
   guidance on mobile implementation])

**Enforcement signal**: GPC failure is the most actively enforced CCPA requirement. The
Sephora ($1.2M, 2022), Tractor Supply ($1.35M, 2025), and Disney ($2.75M, 2026)
enforcement actions all centrally involved GPC/UOOM non-compliance. A joint California,
Colorado, and Connecticut GPC sweep was announced in September 2025.

### Step 7: Children and Minor Protections Analysis

For each applicable law, assess whether the organization's services may be accessed by
minors and what protections apply.

#### Minor Protections Matrix

| Tier                           | States                                                       | Threshold      | Protection                                                                                                       |
| ------------------------------ | ------------------------------------------------------------ | -------------- | ---------------------------------------------------------------------------------------------------------------- |
| Federal COPPA                  | All states                                                   | Under 13       | Parental consent required for online services directed to or knowingly collecting from children under 13         |
| State-level under-13 sensitive | All 19 states                                                | Under 13       | Children's data classified as sensitive; opt-in consent required for processing                                  |
| Teen targeted advertising ban  | CA, CO (amended), CT (2025 amend.), NH, OR (2025 amend.), MN | 13-15 or 13-16 | Affirmative consent required for targeted advertising and sale of teen data                                      |
| Under-18 prohibition           | Maryland (MODPA)                                             | Under 18       | Targeted advertising and data sales prohibited where controller "knew or should have known" consumer is under 18 |

**Critical Maryland distinction**: Maryland's "knew or should have known" standard for
under-18 restrictions eliminates the willful blindness defense. Organizations offering
services to broad consumer audiences in Maryland that could be accessed by minors must
assess and control for this risk, not merely disclaim it.

**Oregon 2025 amendment (HB 2008, effective Jan. 1, 2026)**: Bans sale of personal data
of persons known to be under 16.

### Step 8: Cure Period Risk Assessment

Present the current cure period landscape — this is a critical enforcement risk factor
for many organizations.

#### Cure Period Status

| State         | Cure Available?                         | Days          | Expires / Expires When               | Risk Level                        |
| ------------- | --------------------------------------- | ------------- | ------------------------------------ | --------------------------------- |
| California    | NO mandatory cure (CPPA); AG discretion | —             | No mandatory cure                    | HIGH — enforcement without notice |
| Virginia      | YES — permanent                         | 30            | No expiry                            | LOW                               |
| Colorado      | Discretionary only (expired Jan. 2025)  | 60 if offered | Mandatory cure expired Jan. 1, 2025  | HIGH                              |
| Connecticut   | Discretionary only (expired Jan. 2025)  | 60 if offered | Mandatory cure expired Jan. 1, 2025  | HIGH                              |
| Utah          | YES — permanent                         | 30            | No expiry                            | LOW                               |
| Iowa          | YES — permanent                         | 90            | No expiry                            | LOW                               |
| Indiana       | YES — permanent                         | 30            | No expiry                            | LOW                               |
| Delaware      | Discretionary only (expired Dec. 2025)  | 60 if offered | Mandatory cure expired Dec. 31, 2025 | HIGH                              |
| Tennessee     | YES — permanent [VERIFY]                | 60            | No expiry [VERIFY]                   | LOW                               |
| Montana       | NO mandatory cure (removed Oct. 2025)   | —             | Removed by SB 297 amendments         | HIGH                              |
| New Hampshire | Discretionary only (expired Jan. 2026)  | 60 if offered | Mandatory cure expired Jan. 1, 2026  | HIGH                              |
| New Jersey    | YES — sunsets July 2026                 | 30            | July 15, 2026                        | MEDIUM → HIGH after July 2026     |
| Oregon        | Discretionary only (expired Jan. 2026)  | 30 if offered | Mandatory cure expired Jan. 1, 2026  | HIGH                              |
| Texas         | YES — permanent                         | 30            | No expiry                            | LOW                               |
| Nebraska      | YES — permanent                         | 30            | No expiry (attestation required)     | LOW                               |
| Maryland      | YES — with AG discretion                | 60            | No reported expiry [VERIFY]          | MEDIUM                            |
| Minnesota     | Discretionary only (expired Feb. 2026)  | 30 if offered | Mandatory cure expired Jan. 31, 2026 | HIGH                              |
| Kentucky      | YES — permanent [VERIFY]                | 30            | No expiry [VERIFY]                   | LOW                               |
| Rhode Island  | NO — no cure period at all              | —             | Never existed                        | HIGH — immediate enforcement      |

**Enforcement implication**: As of early 2026, the majority of US state privacy laws no
longer offer mandatory cure rights. Organizations can no longer rely on a cure window as a
compliance buffer. Build programs as if no cure right exists.

### Step 9: Enforcement Landscape Assessment

Assess the enforcement risk profile based on actual enforcement actions and regulator
priorities. For each applicable state, note enforcement posture.

#### Key Enforcement Actions (2022–2026)

| Enforcement Action                | Date      | State             | Penalty                           | Core Violation                                                                                                |
| --------------------------------- | --------- | ----------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Sephora                           | Aug. 2022 | California (AG)   | $1.2M                             | GPC failure; failure to disclose data sales; failure to cure                                                  |
| DoorDash                          | Feb. 2024 | California (AG)   | $375K                             | Marketing co-op data sharing = "sale"; no opt-out disclosure                                                  |
| Allstate/Arity                    | Jan. 2025 | Texas (AG)        | Lawsuit filed                     | Hidden SDK; geolocation/behavioral data sold without consent; data broker non-registration                    |
| LinkedIn                          | Jan. 2025 | Texas (AG)        | Notice issued                     | AI training data used without consent                                                                         |
| Tractor Supply Co.                | Sep. 2025 | California (CPPA) | $1.35M                            | GPC failure; ineffective opt-out; privacy policy not updated annually; job applicant notice; vendor contracts |
| Background Alert, Inc.            | 2025      | California (CPPA) | Operational shutdown through 2028 | Data broker non-registration under Delete Act                                                                 |
| 100+ Companies                    | 2024-2025 | Texas (AG)        | Noncompliance notices             | Various; geolocation, sensitive data, consent                                                                 |
| CA/CO/CT Joint GPC Sweep          | Sep. 2025 | Multi-state       | Ongoing                           | GPC/UOOM non-compliance across companies                                                                      |
| Walt Disney Company               | Feb. 2026 | California (AG)   | $2.75M (record)                   | Opt-out mechanisms failed to stop data flows even for authenticated users                                     |
| Oregon — OCPA Enforcement Reports | 2024-2025 | Oregon (AG)       | Advisory and investigations       | Among most active non-California enforcers                                                                    |

**Enforcement priority areas (confirmed from actual enforcement actions):**

1. **GPC / UOOM compliance** — Top enforcement priority across California, Colorado, Texas
2. **Opt-out mechanisms that don't actually stop data flows** — "Partial compliance is
   noncompliance" (Disney settlement)
3. **Privacy policy currency** — Annual update requirement (California)
4. **Data broker registration** — Easy to detect; aggressively pursued by CPPA
5. **Children's data** — FTC updated COPPA rules; multiple states add teen protections
6. **AI training data** — LinkedIn case signals this is a rising enforcement area
7. **Hidden data collection** — Allstate/Arity SDK case
8. **Job applicant privacy** — Tractor Supply enforcement expanded CCPA scope
9. **Vendor contract compliance** — Missing required terms is a systematic exposure
10. **Coordinated multi-state enforcement** — CA/CO/CT joint sweep is a new pattern

### Step 10: Gap Analysis

Produce a structured gap analysis. Classify each compliance dimension as:

- **COMPLIANT**: Organization meets the requirement
- **PARTIAL**: Organization has some measures in place but has identified gaps
- **NON-COMPLIANT**: Organization does not meet the requirement
- **UNKNOWN**: Requires further investigation to determine compliance status

#### Gap Analysis Dimensions

| Dimension                        | Assessment Required                                                                                 |
| -------------------------------- | --------------------------------------------------------------------------------------------------- |
| Privacy notice currency          | Updated in last 12 months (CA requirement); discloses all required elements per each applicable law |
| Consumer rights intake           | Functional mechanism for access, delete, correct, portability, opt-out, appeal                      |
| Rights response timelines        | Responses within 45 days (most states); appeal responses within 60 days                             |
| UOOM/GPC compliance              | GPC signal recognized and honored across web and app                                                |
| Opt-out effectiveness            | Opt-out actually stops downstream data flows to advertising partners                                |
| Separate opt-out rights          | Sale opt-out and targeted advertising opt-out are distinct (not merged)                             |
| California "Limit" right         | Separate mechanism for Limit Use of Sensitive PI (California only)                                  |
| Sensitive data consent           | Opt-in consent obtained before processing sensitive categories per each state                       |
| Maryland sensitive data sale ban | Sensitive data is not sold (any sales prohibited in Maryland)                                       |
| Children's data controls         | Age verification or age-appropriate design controls; COPPA compliance                               |
| Teen data controls               | Affirmative consent for targeted advertising/sale for 13-16 where required                          |
| Under-18 controls (Maryland)     | Knew/should-have-known standard applied for advertising/sale to minors                              |
| PIA/DPA program                  | PIAs conducted and documented for all triggering activities                                         |
| Vendor contracts                 | All contracts include required processor/service provider terms                                     |
| GPC in vendor contracts          | Service provider contracts prohibit vendors from disregarding GPC signals                           |
| Data minimization                | Collection limited to reasonably necessary purposes                                                 |
| Data retention schedules         | Retention periods defined and enforced                                                              |
| Security controls                | Reasonable security measures proportionate to data sensitivity                                      |
| Data broker registration         | CA and TX data broker registration status confirmed                                                 |
| AI training disclosure           | CT (effective July 2026): LLM training disclosure in privacy notice                                 |
| Specific 3rd party disclosure    | OR, MN: Discloses specific third parties in privacy notice                                          |
| Data inventory                   | Living record of personal data processed (required for MN; foundational for PIAs)                   |

For each dimension where a gap is identified, produce a gap detail entry using the format
defined in the **Output Format Template** section below.

### Step 11: Quality Verification

Before delivering the analysis, apply the quality checks defined in the
**Quality Assurance Framework** section.

### Step 12: Deliver Gap Analysis

Deliver the structured output using the **Output Format Template**. Include a Glass Box
audit trail and a remediation roadmap with 30/60/90-day priorities.

---

## Severity Classification Framework

Classify each compliance gap as HIGH, MEDIUM, or LOW severity.

### HIGH Severity (Immediate Action Required)

A gap is classified HIGH if any of the following apply:

- The gap involves a requirement that has been the subject of an actual enforcement action
  (GPC, opt-out effectiveness, data broker registration, children's data, privacy policy
  currency, vendor contracts)
- The gap involves a bright-line prohibition (Maryland sensitive data sale ban, Maryland
  under-18 advertising prohibition)
- The gap is in a state where no cure period exists (California, Colorado post-2025,
  Connecticut post-2025, Oregon post-2026, Montana post-2025, Minnesota post-2026,
  Rhode Island)
- The gap involves UOOM/GPC non-compliance and the organization is subject to at least
  one UOOM-mandating state
- The gap involves children's data where the organization cannot demonstrate COPPA
  compliance or state law equivalent

### MEDIUM Severity (Remediate Within 60 Days)

A gap is classified MEDIUM if:

- The requirement is clearly established but enforcement focus is not yet documented in
  specific actions
- The gap involves a state with an active cure period that has not yet expired
- The gap involves a technical deficiency (e.g., appeal right not implemented) that is
  correctable through a defined operational change
- The gap involves privacy notice deficiencies that do not involve the highest-priority
  requirements (GPC, opt-out mechanisms)

### LOW Severity (Remediate Within 90-180 Days)

A gap is classified LOW if:

- The gap involves a best-practice obligation where enforcement is unlikely near-term
- The gap involves a requirement unique to a low-volume or low-priority applicable state
- The gap involves a procedural documentation requirement with no immediate enforcement
  history

---

## Actionable Output per Finding

For each gap identified, provide:

1. **Gap ID**: Unique identifier (e.g., `CA-OPT-001`)
2. **Applicable Law(s)**: Specific statute and section
3. **Requirement**: Plain-language statement of the specific requirement
4. **Current State**: What the organization currently has in place
5. **Gap Description**: Specific nature of the non-compliance
6. **Severity**: HIGH / MEDIUM / LOW with rationale including enforcement precedent
7. **Remediation Steps**: Specific, actionable steps
8. **Effort Level**: Low / Medium / High
9. **Priority Deadline**: Cure expiry, law effective date, or enforcement deadline

---

## Prioritization Framework

Structure the remediation roadmap in three tiers:

### Tier 1 — Immediate (0-30 Days)

**Must fix before any enforcement contact:**

- GPC / UOOM signal recognition across all consumer touchpoints (web + app)
- Opt-out mechanism effectiveness — ensure downstream data flows actually stop
- "Do Not Sell or Share" link / equivalent link — present and functional
- California "Limit Use of Sensitive Personal Information" mechanism (if CA applies)
- Data broker registration (California, Texas) — if applicable
- Job applicant privacy notices (California)

### Tier 2 — High Priority (31-60 Days)

**Remediate before cure periods expire or as foundational compliance:**

- Privacy notice update — all required elements, state-specific disclosures
- Consumer rights intake mechanism — all rights for all applicable states
- Appeal right mechanism — distinct from DSR intake
- Sensitive data consent workflows — opt-in mechanisms per state
- Maryland sensitive data sale prohibition — operational controls
- Vendor contract audit — identify and remediate required term gaps
- PIA program — establish for triggering activities

### Tier 3 — Medium Priority (61-90 Days)

**Address before year-end or at next program review cycle:**

- Children/teen data controls — age verification, consent, advertising restrictions
- Data minimization program — collection limitation, retention schedules
- Data inventory / RoPA — living record of processing activities
- Third-party disclosure (Oregon, Minnesota) — specific third-party list in privacy notice
- AI training disclosure (Connecticut — effective July 2026)
- Security controls review
- Training program for employees handling personal data

---

## Quality Assurance Framework

### Citation Quality Gates

Run these five gates silently before delivering any output. Revise before delivery if any
gate fails.

| Gate           | Rule                                                                                                                                       | Fail Action                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- |
| **Source**     | Every legal claim cites a specific statute, regulation, or enforcement action                                                              | Add citation or mark "[UNVERIFIED]"                |
| **Format**     | All citations follow a consistent, recognizable format                                                                                     | Fix format                                         |
| **Currency**   | Thresholds, cure periods, and UOOM mandates are the most frequently changing elements — flag any that may have changed since training data | Add "[CHECK CURRENCY — law may have been amended]" |
| **Domain**     | Analysis covers only US state comprehensive privacy laws; do not import GDPR or other non-US law concepts into US state analysis           | Remove or clearly separate                         |
| **Confidence** | Uncertainty is explicitly stated — do not state uncertain conclusions as definitive                                                        | Add confidence qualifier; mark [VERIFY]            |

### Self-Interrogation for HIGH-Severity Gaps

For every gap classified as HIGH severity, apply this 3-pass review before delivery:

**Pass 1 — Legal Chain Integrity**: Does the gap assessment follow logically from the
cited statute or enforcement action? Would a regulator or court actually reach this
conclusion based on the cited authority?

**Pass 2 — Completeness**: Are there related statutory provisions, AG guidance documents,
or enforcement advisories that should modify the analysis? Are there exemptions or
defenses that apply?

**Pass 3 — Challenge**: What is the strongest argument that the organization is compliant?
Is the organization's current practice potentially defensible? State the strongest
counterargument before confirming the HIGH classification.

### Confidence Scoring

| Level        | Range     | Meaning                                          | Action                                                |
| ------------ | --------- | ------------------------------------------------ | ----------------------------------------------------- |
| **Definite** | 0.95–1.0  | Settled law, confirmed enforcement action        | State with confidence                                 |
| **High**     | 0.80–0.94 | Strong statutory basis, minor ambiguity          | State with brief caveat                               |
| **Probable** | 0.60–0.79 | Good basis but regulatory interpretation pending | State with reasoning; note open questions             |
| **Possible** | 0.40–0.59 | Genuinely uncertain                              | Flag for counsel review; present both interpretations |
| **Unlikely** | 0.0–0.39  | Weak basis, speculative                          | Do not assert; flag "[UNCERTAIN]"                     |

---

## Anti-Patterns Catalogue

What NOT to do when advising on US state privacy law compliance:

1. **Treating CCPA and Virginia-model laws as interchangeable** — California is an
   opt-out regime for sensitive data; most other states are opt-in. California has a
   tripartite service provider/contractor/third party structure; other states use a binary
   controller/processor model. California's CPPA has dedicated rulemaking authority; most
   states have AG-only enforcement. Never apply California contract templates to
   Virginia-model law relationships without adapting them.

2. **Misapplying thresholds — revenue vs. volume** — Most states have no revenue threshold
   at all (only consumer volume). Utah and Tennessee require a revenue floor AND volume.
   Maryland has only a consumer volume threshold with no revenue percentage alternative.
   Run each state's test independently. Do not shortcut by applying one state's test to
   all states.

3. **Ignoring GPC / UOOM mandate scope** — As of mid-2025, 12+ states require honoring
   GPC signals. Organizations that check GPC compliance only for California and miss
   Colorado, Connecticut, Montana, Delaware, Minnesota, New Jersey, New Hampshire, Texas,
   Nebraska, Oregon, and Maryland are exposed in multiple jurisdictions simultaneously.

4. **Conflating opt-out of sale with opt-out of targeted advertising** — Under Virginia-
   model laws, these are separate opt-out rights. Under California, "sharing" is a third
   category. A single opt-out checkbox does not cover all required mechanisms. Implement
   granular opt-out infrastructure.

5. **Implementing opt-out links that don't actually stop data flows** — Tractor Supply
   and Disney enforcement established that nominal opt-out compliance (visible link,
   confirmation screen) is insufficient if downstream data flows to advertising partners
   continue. The opt-out must propagate to all data destinations.

6. **Missing the appeal right** — The appeal right is distinct from DSR intake. A deletion
   denial triggers a right to appeal on a separate timeline (typically 60 days). Many
   compliance programs implement DSR intake but skip the appeal mechanism.

7. **Treating sensitive data definitions as uniform** — Colorado excludes precise
   geolocation from its sensitive data definition. California includes union membership
   and philosophical beliefs. Maryland prohibits selling sensitive data outright. New
   Jersey and Delaware include transgender/nonbinary status. Sensitive data compliance
   must be mapped against each state's specific definition.

8. **Missing Maryland's outright sensitive data sale ban** — No other US state prohibits
   selling sensitive data regardless of consent. Organizations that treat Maryland as just
   another Virginia-model state will violate this absolute prohibition.

9. **Assuming cure is still universally available** — As of early 2026, a majority of
   US state privacy laws no longer offer mandatory cure. Building a compliance program
   with cure periods as a safety buffer is now a dangerous strategy.

10. **Ignoring nonprofits' shifting exemption status** — Delaware, Maryland, Minnesota,
    Montana, New Jersey, and Oregon have materially narrowed or eliminated the nonprofit
    exemption. A nonprofit active in these states cannot assume it is exempt.

11. **Missing Connecticut's July 2026 threshold reduction** — Connecticut's threshold
    drops from 100,000 to 35,000 consumers, and from 25,000+25% to any consumer data
    sale regardless of volume, effective July 1, 2026. Organizations approaching but not
    yet reaching Connecticut's current thresholds may be subject to CTDPA after July 2026.

12. **Implementing a "Do Not Sell" link without a "Do Not Share" component** — California's
    CPRA added "sharing" for cross-context behavioral advertising as a concept distinct from
    "sale." The link must be labeled "Do Not Sell OR Share" and must stop both categories
    of data flows. California enforcement has focused heavily on this.

13. **Using one contract template for all vendor relationships** — California's tripartite
    classification (service provider, contractor, third party) requires different contract
    terms for each relationship type. A single DPA template cannot satisfy California and
    Virginia-model states simultaneously without multi-layered structure.

14. **Data minimization blind spot during rights fulfillment** — Asking consumers to
    provide extensive personal information to verify their identity for a rights request
    is itself a data minimization violation. The CPPA cited this as an enforcement priority
    before any formal actions; Honda was investigated for this in 2025.

15. **Ignoring data broker registration obligations** — If any business function involves
    aggregating, enriching, or reselling consumer data, the California and Texas data
    broker registration requirements likely apply. Non-registration is one of the easiest
    enforcement targets because it is publicly observable. The CPPA launched a data broker
    strike force in 2025.

16. **Missing job applicant privacy obligations** — California's CCPA applies to job
    applicant personal information. Tractor Supply enforcement included job applicant notice
    failures. Privacy notices at the point of job application collection are a required
    element of CCPA compliance.

17. **Treating minor data controls as limited to under-13 (COPPA)** — Multiple states
    have added teen protections (13-16) for targeted advertising and data sales. Maryland's
    "knew or should have known" standard applies to all consumers under 18. Organizations
    that limit children's compliance to federal COPPA are non-compliant in multiple states.

---

## Writing Standards

Before delivering any output, verify:

- [ ] **Disclaimer present**: Every output includes the standard AI-assisted review
      disclaimer and [VERIFY] markers on uncertain claims
- [ ] **State-specific accuracy**: Each law's requirements are attributed to the correct
      state; no cross-contamination of one state's rules into another
- [ ] **Tables formatted correctly**: All comparison matrices display correctly; column
      alignment preserved
- [ ] **Statutory citations present**: Every requirement cites a specific statute and
      section, not just the law name
- [ ] **Enforcement precedent cited**: HIGH-severity findings reference the specific
      enforcement action that establishes the risk
- [ ] **[VERIFY] applied**: All uncertain items — cure period status, specific citation
      numbers, recent amendments — are marked [VERIFY]
- [ ] **Remediation steps are specific**: Not "review your privacy notice" but "update
      the privacy notice to disclose [specific element] required by [specific statute]"
- [ ] **Severity classification justified**: Every HIGH classification states why it is
      HIGH, not merely that it is
- [ ] **No GDPR contamination**: US state privacy law analysis uses US-specific
      terminology (controller/processor or business/service provider as applicable per
      state; not "data subject" — use "consumer")
- [ ] **Plain language**: Legal analysis is intelligible to a compliance professional
      without a law degree; explain legal concepts where necessary

---

## External Tool Integration

### With legalcode-mcp (Preferred)

When legalcode-mcp is connected, use it to:

- Verify current text of specific statutory provisions before citing them
- Confirm whether any state laws have been amended since the skill's training data
- Search for recent AG enforcement actions, guidance documents, and advisory opinions
- Confirm CPPA regulation status (ADMT, cybersecurity audits, risk assessments)
- Verify cure period expiry dates and sunset provisions

Save results to `/tmp/legalcode-us-privacy-research.md` and cite as VERIFIED in the
Glass Box audit trail.

### Without legalcode-mcp

Proceed with the analysis using the skill's built-in knowledge. Mark all citations with
[VERIFY]. Note in the Glass Box audit trail: `legalcode_mcp: "Not connected — all
citations require independent verification before reliance."` Focus gap analysis on
structural compliance gaps rather than specific statutory citation verification.

---

## Localization Notes

This skill is US-specific and covers all 50 states for enacted comprehensive privacy laws.
For organizations also subject to international regimes:

- **GDPR / UK GDPR / EU regime**: See `legalcode-cross-border-transfer-assessment` and
  `legalcode-dpa-review-and-negotiation`
- **LGPD (Brazil) / PIPEDA (Canada)**: See `legalcode-dsar-workflow-builder` for cross-
  regime DSAR handling
- **Illinois BIPA**: Not a comprehensive privacy law; separate biometric-specific analysis
  required
- **Washington My Health My Data Act**: Not a comprehensive privacy law; health-data-
  specific analysis required; runs alongside any applicable state comprehensive law

---

## Glass Box Audit Trail

Every output should include the following audit trail template completed for the specific
analysis run.

```yaml
glass_box:
  skill_name: "legalcode-us-state-privacy-comparison"
  analysis_date: "[Date of analysis]"
  organization: "[Organization name or 'Anonymous']"
  entity_type: "[For-profit / Nonprofit / Government / Educational / Financial / Healthcare]"
  revenue: "[Annual gross revenue or 'Not disclosed']"
  states_analyzed: "[Number of states where org operates or targets consumers]"
  laws_applicable: "[Number of state comprehensive privacy laws that apply]"
  laws_approaching_threshold: "[Number approaching but not yet meeting thresholds]"
  sensitive_data_processed: "[Yes / No / Unknown]"
  uoom_states_applicable: "[Number of UOOM-mandating states applicable to org]"
  gpc_currently_honored: "[Yes / No / Partial / Unknown]"
  cure_periods_available: "[States with mandatory cure / States without]"
  gaps_identified:
    high: "[Number of HIGH-severity gaps]"
    medium: "[Number of MEDIUM-severity gaps]"
    low: "[Number of LOW-severity gaps]"
    unknown: "[Number requiring further investigation]"
  legalcode_mcp: "[Connected — citations verified / Not connected — manual verification required]"
  confidence: "HIGH / MEDIUM / LOW — [rationale]"
  limitations:
    - "All threshold calculations based on information provided; independent verification required"
    - "State laws are frequently amended; confirm current statutory text before relying on any specific provision"
    - "Enforcement action descriptions are based on publicly available information; confirm current status"
    - "[Any other scope limitations or assumptions]"
  reviewer: "AI-assisted — requires review by qualified privacy counsel before reliance"
```

---

## Output Format Template

Structure the final output as follows.

---

````markdown
## US State Privacy Law Gap Analysis

**Organization**: [Name]
**Analysis Date**: [Date]
**Prepared By**: Legalcode AI (requires qualified privacy counsel review before reliance)

---

### Part A: Applicability Summary

| State   | Law       | Applies?               | Trigger                     | Effective | Cure Period      | UOOM Required |
| ------- | --------- | ---------------------- | --------------------------- | --------- | ---------------- | ------------- |
| [State] | [Abbrev.] | Yes / No / Approaching | [Which threshold triggered] | [Date]    | [Yes/No/Expired] | [Yes/No]      |

**Laws applicable**: [N] of 19 enacted US state comprehensive privacy laws apply.
**Laws approaching threshold**: [States approaching threshold — monitor].
**Laws not applicable**: [States not applicable — brief reason].

---

### Part B: Compliance Status Dashboard

| Compliance Dimension             | Status                                        | Priority            |
| -------------------------------- | --------------------------------------------- | ------------------- |
| Privacy notice completeness      | COMPLIANT / PARTIAL / NON-COMPLIANT / UNKNOWN | HIGH / MEDIUM / LOW |
| Consumer rights intake           | [Status]                                      | [Priority]          |
| Rights response timelines        | [Status]                                      | [Priority]          |
| UOOM / GPC compliance            | [Status]                                      | [Priority]          |
| Opt-out mechanism effectiveness  | [Status]                                      | [Priority]          |
| California "Limit" right         | [Status / N/A]                                | [Priority]          |
| Sensitive data consent           | [Status]                                      | [Priority]          |
| Maryland sensitive data sale ban | [Status / N/A]                                | [Priority]          |
| Children's data (under-13)       | [Status]                                      | [Priority]          |
| Teen data controls (13-16/17)    | [Status]                                      | [Priority]          |
| PIA/DPA program                  | [Status]                                      | [Priority]          |
| Vendor contracts                 | [Status]                                      | [Priority]          |
| Data minimization                | [Status]                                      | [Priority]          |
| Data broker registration         | [Status / N/A]                                | [Priority]          |
| Data inventory                   | [Status]                                      | [Priority]          |

---

### Part C: Gap Detail — Prioritized by Severity

#### HIGH SEVERITY GAPS

**Gap ID**: [e.g., CA-OPT-001]
**Applicable Law**: [e.g., Cal. Civ. Code § 1798.135; CPPA Enforcement Action re Tractor Supply (2025)]
**Requirement**: [Plain-language statement]
**Current State**: [What the organization currently has]
**Gap**: [Specific non-compliance]
**Severity Rationale**: HIGH — GPC failure is the most actively enforced CCPA requirement;
Sephora ($1.2M), Tractor Supply ($1.35M), and Disney ($2.75M) all involved this violation.
California has no cure period; enforcement can follow immediately.
**Remediation Steps**:

1. [Specific step 1]
2. [Specific step 2]
3. [Specific step 3]
   **Effort**: Low / Medium / High
   **Deadline**: [Date or description]

[Repeat for each HIGH gap]

#### MEDIUM SEVERITY GAPS

[Gap detail entries for each MEDIUM gap]

#### LOW SEVERITY GAPS

[Gap detail entries for each LOW gap]

#### UNKNOWN STATUS — Requires Investigation

[Items requiring internal data gathering before classification]

---

### Part D: Vendor Contract Gap Summary

[List of required contract terms missing from existing processor/service provider agreements,
number of affected contracts, and remediation approach]

---

### Part E: State-by-State Requirement Checklist

**[State Name] — [Law Abbreviation]** (Effective: [Date])

| Requirement                      | Statutory Basis | Status          | Notes |
| -------------------------------- | --------------- | --------------- | ----- |
| Privacy notice includes [X]      | § [citation]    | COMPLIANT / GAP |       |
| Consumer rights intake — [right] | § [citation]    | COMPLIANT / GAP |       |
| UOOM/GPC honored                 | § [citation]    | COMPLIANT / GAP |       |
| ...                              | ...             | ...             |       |

[Repeat for each applicable state]

---

### Part F: Remediation Roadmap

#### 30-Day Priority Actions (Tier 1 — Immediate)

- [ ] [Action] — Responsible: [Team/Role] — Deadline: [Date]
- [ ] [Action]
- [ ] [Action]

#### 60-Day Priority Actions (Tier 2 — High Priority)

- [ ] [Action] — Responsible: [Team/Role] — Deadline: [Date]
- [ ] [Action]

#### 90-Day Priority Actions (Tier 3 — Medium Priority)

- [ ] [Action] — Responsible: [Team/Role] — Deadline: [Date]
- [ ] [Action]

---

### Part G: Enforcement Risk Assessment

[Narrative summary of the enforcement landscape most relevant to the organization's
specific gap profile, sector, and processing activities. Cross-reference gaps with
specific enforcement actions demonstrating the risk of each.]

**Highest enforcement risk areas for this organization:**

1. [Area] — [Enforcement precedent]
2. [Area] — [Enforcement precedent]
3. [Area] — [Enforcement precedent]

---

### Glass Box Audit Trail

```yaml
[Complete Glass Box YAML as defined in the Glass Box section]
```
````

---

> **Legal Review Required**: This analysis is AI-assisted and does not constitute legal
> advice. All conclusions must be reviewed by qualified privacy counsel licensed in the
> applicable jurisdictions before any reliance. State privacy laws are amended frequently;
> verify current statutory text and regulatory guidance before implementing any
> remediation steps. Citations marked [VERIFY] have not been independently verified.

```

---

## Provenance

Created by Legalcode (2026-03-01). Legalcode original synthesis — created from scratch
via a two-agent parallel research pipeline:

- **Agent 1 (Structural Analyst)**: Researched and synthesized legal substance across all
  19 enacted US state comprehensive privacy laws — full threshold matrices, consumer rights
  matrix, sensitive data definitions per state, children/minor protections, UOOM mandates,
  cure period status, enforcement mechanisms, and key distinguishing features per law.
  Sources: IAPP US State Privacy Laws Report (2025), CPPA enforcement actions, state AG
  websites and enforcement reports, Perkins Coie/Manatt/Mintz/Osano/Koley Jessen law firm
  analyses, Oregon AG OCPA Enforcement Reports, California AG press releases.

- **Agent 2 (Workflow/Anti-patterns Analyst)**: Researched and synthesized compliance
  workflow methodology, threshold analysis decision tree, gap analysis dimensions,
  controller vs. processor obligation mapping, privacy program component matrix,
  anti-patterns catalogue (17 items), enforcement landscape (2022-2026 enforcement
  actions), GPC technical requirements, and output format best practices. Sources: IAPP
  state law tracker, Husch Blackwell/Steptoe privacy law comparison resources, CPPA
  enforcement advisories, California AG settlement documents, Texas AG enforcement
  filings, multi-state GPC sweep announcements, FPF Anatomy of a State Privacy Law
  report.

Research as of March 2026. All statutory provisions, threshold figures, cure period
expiry dates, and enforcement actions should be re-verified before reliance as the US
state privacy landscape evolves rapidly.
```
